import * as yup from "yup";

const validSchema = yup.object().shape({
  key: yup
    .string()
    .required("Autorisierung notwendig!")
    .test("jwt", "Kein gültiger Schlüssel!", (value) => {
      if (value === undefined || value === null || value === "") return true;
      try {
        const base64Url = value.split(".")[1];
        const base64 = base64Url.replace(/-/g, "+").replace(/_/g, "/");
        const jsonPayload = decodeURIComponent(
          atob(base64)
            .split("")
            .map((c) => {
              return "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2);
            })
            .join("")
        );
        return JSON.parse(jsonPayload);
      } catch (e) {
        return false;
      }
    }),
  ...Array.from({ length: 2 }, (_, i) => ({
    [`mk-field${i + 1}`]: yup.string().required("MK notwendig!"),
  })).reduce((acc, curr) => ({ ...acc, ...curr }), {}),
  ...Array.from({ length: 18 }, (_, i) => ({
    [`field${i + 1}`]: yup.string(),
  })).reduce((acc, curr) => ({ ...acc, ...curr }), {}),
});

export default validSchema;
