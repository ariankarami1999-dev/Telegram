<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/arvuIXHOnT2XDcLwFDYTz8STN5xnBOM_mccJS2aPwMGONRwUZJitEb63BGHXJ3ULkSNx9vSxSWiP8TQ8X-xDaquvu3rtZ1Dykk70lpvBDJ_XWzLa6M2u_XHmQ4V3zH8yX5RFgsjkM6VMatIx9E2gE-n2FQAf0vtLA8pr8EOKAfyIBMUONcIYgkZU87QJ7Pg711PA9gA40pslsQ8f6joaxR2nSQnxXhjyKXScJv2G5u1F1hmz00NJ1sx7qhRHQKD8DZ-nPHjuAswXZY_619IcUd__BqxsFa22iV2lFxphFN93FFWRlkLn6amU4AWTsPTM0GJO5yhd7aQGhOH8mc48_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 21:23:04</div>
<hr>

<div class="tg-post" id="msg-452160">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/642a887069.mp4?token=G5IHvJpdKbQnwgUyCqkONmfdEvfgf7HtScCiNvQzTCr79D_Qa7LDNoVaclClwuQxKONv8HBaVV7_i9yjL5ubv9BrRIZC-hF-Oph68p5ZKuNiwr540KxPMzamT1s8z1AhcgusfP7S0YYEzvcV3sazvIDnsia0sb_N-8eIXNLD_adS5iANugn0IIS8_GpZuvLoutUIH8XcylQiu6eLjcTR0S1G8cNchieAJXbWv-u5FKdLDhvTrqpahSyv9ug9VsC-mZdimKVkAE6-RfSQFfJxamqXZKWCkzTOEFuzZFXDwNF_8fgFniM2PaOk5NZJ7FH2TwF5S3RDkV9-J5QYxT9FCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/642a887069.mp4?token=G5IHvJpdKbQnwgUyCqkONmfdEvfgf7HtScCiNvQzTCr79D_Qa7LDNoVaclClwuQxKONv8HBaVV7_i9yjL5ubv9BrRIZC-hF-Oph68p5ZKuNiwr540KxPMzamT1s8z1AhcgusfP7S0YYEzvcV3sazvIDnsia0sb_N-8eIXNLD_adS5iANugn0IIS8_GpZuvLoutUIH8XcylQiu6eLjcTR0S1G8cNchieAJXbWv-u5FKdLDhvTrqpahSyv9ug9VsC-mZdimKVkAE6-RfSQFfJxamqXZKWCkzTOEFuzZFXDwNF_8fgFniM2PaOk5NZJ7FH2TwF5S3RDkV9-J5QYxT9FCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف طولانی موکب‌داران در مرز مهران برای خدمت به زائران در عراق
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 828 · <a href="https://t.me/farsna/452160" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452159">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdf0591852.mp4?token=X4JMIoDQZPBfMtURwpJl_C_F7HgvKWgNWXTjgngFYKRtuAj5rPqL18thrUUbumgFXX9RQ6IOVjJ0k-h0HM8CYe6MC3Ir-7HOIlXJ5i_ppxZuxzdDzoO9vHfoI-2t7MxUF8U3BHL_6FsOAYjQFMS3PPqudeC6a39vAgysOmXP3zD80AZMgd2v1HJt0OWK6PzgsXN9-x70NwUSedRGOqjZZiXcqW4wPsghF3wYh7rpRkAV8FpO6gOz8_MVRCtOz248-RtkgNJ7AiXNt2X4_ppX7crBcNbhGSqquI842Zv3qmL-UeDmgfnuATD2kgvOtqaL99bBAjqeAJledopP9RB65ESWzQb-0Wj9-OvreQaQibmjNrD4tWnL-hDkVjCUfZ0I1U28WckBcWWxZ7XiTZLQzSzm6N_Wob1J2fkKdIVReAkxnh6V_0Lxv3hlTdgVVtth9lXZSYjvVqKguBfyYEi8g_fitvV7RFsB2Z-WZ1HhqOXzjQIjDWkVhtTL6R7VNbsFueOo3dcwyTEqAcNfLOxaPan-TV1qaNsH2HrcAGqcQ5EPb8D7stkvcMLdg7IyMrEzx2dt7FshsKX6-rwcJf61esEfvKjjReT8eUYK21oLWsB9ytk8CnYqCnXPrJCCE6DNiVX6glxQjVbkozES-nLKpoF-8_IBywcU6udL_hQ0Ago" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdf0591852.mp4?token=X4JMIoDQZPBfMtURwpJl_C_F7HgvKWgNWXTjgngFYKRtuAj5rPqL18thrUUbumgFXX9RQ6IOVjJ0k-h0HM8CYe6MC3Ir-7HOIlXJ5i_ppxZuxzdDzoO9vHfoI-2t7MxUF8U3BHL_6FsOAYjQFMS3PPqudeC6a39vAgysOmXP3zD80AZMgd2v1HJt0OWK6PzgsXN9-x70NwUSedRGOqjZZiXcqW4wPsghF3wYh7rpRkAV8FpO6gOz8_MVRCtOz248-RtkgNJ7AiXNt2X4_ppX7crBcNbhGSqquI842Zv3qmL-UeDmgfnuATD2kgvOtqaL99bBAjqeAJledopP9RB65ESWzQb-0Wj9-OvreQaQibmjNrD4tWnL-hDkVjCUfZ0I1U28WckBcWWxZ7XiTZLQzSzm6N_Wob1J2fkKdIVReAkxnh6V_0Lxv3hlTdgVVtth9lXZSYjvVqKguBfyYEi8g_fitvV7RFsB2Z-WZ1HhqOXzjQIjDWkVhtTL6R7VNbsFueOo3dcwyTEqAcNfLOxaPan-TV1qaNsH2HrcAGqcQ5EPb8D7stkvcMLdg7IyMrEzx2dt7FshsKX6-rwcJf61esEfvKjjReT8eUYK21oLWsB9ytk8CnYqCnXPrJCCE6DNiVX6glxQjVbkozES-nLKpoF-8_IBywcU6udL_hQ0Ago" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهران تا کربلا؛ ۱۴۰۰ عاشق در مسیر امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/farsna/452159" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452157">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfJoVlTBta5cDP9HAIy6TmbTor_sQQosP5_W6kHnm_ASwlmaSDH_JMpVqs4kK_2hCxFRETGNXUZatjwMN3VeWMBoRhM3RSus-7Q19uuCgb5C3IbP51BjXjal5fkpL_JFZQ--pDtJIBBPaNmRwNwejZ5AYi4r3-OBpH9q9q0BtY8VQ__w1jBIqtQZujxNU7yM4aNSBMcXRiry11C2BycFXVQ9377RfOxj4PCxeHvR5US2ewufxXo14sLdnMnQl9fDAku9RRS1PVUF0ikaMHI1dpBCiiYyXLJbjGPPHOkpqn9IKRgGPx43J5MAe7e42YdQbCKc_Tlc9gN8h0lPNy7k5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU0iDQ2qK5fxYWwdujrdbBz3bSfFSEJBLdm3E-8PTQKKaWjQgd-yzAQoJSQ83SrQQQqz6aWI6kNRumHsD5_YNtiLwZXPI1M3vQlJWtgvlzfGqNYJct6XFsKh-_D4LkxkaiL0_aNo-ewTd1P17WTD8SbJ_D9vCi8rQ6ulgSTvSP5XbPP5uaUQzxriS3T8umDXHaPDusatFBRMipkck_Umj67LhhWCGzNtxm9qlmt69DpJg-1xQ5zcv_g_J8WnP8Z0-QOd8M6IxlOeml8tmBeafEaMNUhNk6O-e0-7YB7Yi8sZrzIIVDVQYSuahrYxWasTMmxE3k7WeB7eAe7XfZ9Kkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قدردانی فرمانده هوافضا از هیئت بنی‌فاطمه و طباخیان
🔹
فرمانده نیروی هوافضای سپاه با تقدیر از هیئت بنی‌فاطمه و حجت‌الاسلام طباخیان برای حمایت از رزمندگان، تأکید کرد که «در میانه رویارویی ایران با دشمنان، مجالس حسینی باید به سنگری برای بصیرت‌افزایی، حفظ اتحاد و تقویت انسجام ملی تبدیل شوند».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/farsna/452157" target="_blank">📅 21:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452156">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXhGiU-cwHoTKEOpmLvdKx-6JBCcH64HRPMJmA3UKzSnvEewVobk5lSabYUUgdmLLQhf0zKRfF_auihOJKEgbsj4k24Nz9_KexIVFPbUjMiLE5DGCdlVs3v52Q7lwuvhG0jM8TyjXiwrgnxnzfy0_sD3gqCbnkXIUVswvCNo3O8J7jQha5kdgbOaefSzBfjtxiqxErnX-4DepWwy6CduQ8xCeETWNd1aovEvyWJ6rWsSIHMfI-2kbeY3LQhB8XlEC0_6fRNKYAP3y2yPf9F55Ciu_VdFVUrYpJewSxAAkjl8JxKvzRMh1bO83ho6z2RC3SM0ELb5FooPST7cLzrdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش ایرانی از خط دزدی دریایی آمریکا عبور کرد
🔹
یک‌ نفتکش منتسب به ناوگان ایران دقایقی پیش با نادیده‌گرفتن محاصرهٔ ادعایی آمریکا از آب‌های آزاد وارد دریای عمان شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/452156" target="_blank">📅 20:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452155">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389a429d6a.mp4?token=kMmS-H0mpA_KFa9BQwUoNK6O_PABBgVhgKjpiWs3VCLs_WkdYfnVSirCWeqnFwCfth9b9Nvj00ChEO5bO5tATMdFCRhKF_JHf1eN80tyiUE17i_avMKG6nkkU6gEIBbUPvSaaaIIiWuiocv2TquDIhsOyJar27ztXjsqGECxaFAIIOlN-FUhvEJdGxjfc0m1F1J5EH5SIQjR9vHjKWqFz97MbMJvuCq-vJmX64J_dyq3LJ-6kOPc-59M09-0gdhfo3pepHwQGRBuxcEJEMDJb1uSh_PJGAZTpllEqWeYkqp7P8IIjk8zCGpFh84QywBChmhzz5Dxm_FhVXYMr9-iHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389a429d6a.mp4?token=kMmS-H0mpA_KFa9BQwUoNK6O_PABBgVhgKjpiWs3VCLs_WkdYfnVSirCWeqnFwCfth9b9Nvj00ChEO5bO5tATMdFCRhKF_JHf1eN80tyiUE17i_avMKG6nkkU6gEIBbUPvSaaaIIiWuiocv2TquDIhsOyJar27ztXjsqGECxaFAIIOlN-FUhvEJdGxjfc0m1F1J5EH5SIQjR9vHjKWqFz97MbMJvuCq-vJmX64J_dyq3LJ-6kOPc-59M09-0gdhfo3pepHwQGRBuxcEJEMDJb1uSh_PJGAZTpllEqWeYkqp7P8IIjk8zCGpFh84QywBChmhzz5Dxm_FhVXYMr9-iHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رأی مجلس نمایندگان آمریکا به پایان جنگ علیه ایران
🔹
مجلس نمایندگان آمریکا طرحی که خواستار توقف جنگ علیه ایران بدون مجوز کنگرهٔ این کشور است را با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف تصویب کرد.
🔹
در این رأی‌گیری ۴ نفر از اعضای حزب جمهوری‌خواه با دموکرات‌ها…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/452155" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452154">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f174f6ca73.mp4?token=NdjsvMYvzobv0LLwH2iO6BlBw79QOo1vk0mNeobeMp2lENtOb7MoqtDuHMNvZ_MsP4YJtHjbZwJpi9-o6UOlU4nK3HmvkAUUc_MHb3CkD4k7PrOLIFPJlY_L3tugxjBueEHm0PUPH3p7KZkRS9YMSAxOZo6nykigP8aju4U-0rOu5vvx1lAjuLbcKBcA73KsFulHwt6q3xsGX-MlwCK0s39wTHMmINNJxPMTVOn9GXaJG6WjPyVgjb_U-O2zW550Bl9ttb-hO0lQ--hW9rYwAQ5CjEgvIIXzK3Gy4dzUr1KYW2akiYARtsxHoBNkdcMLpts-A6F2i5DTLxrXc8eepZh1O7b-eGLo3-AYEVgINoW_JMOtjyY8ZjmTx3bJWFx9piD-RkNDYrCiTxuLPcc_cI15AAhsQdSgll0BWhaaw73VDs8C265KaX4niPKHhLOO-QldkWBlSDOtnNbzCSbTU_nH5O8ph6QKVKOamj-hrW5ZX7iKUBbgFwB_7LRdAV5Qqy1D76-qafbvz-c5KGBeJTMpr7p6zNS2BNDDxFU_CERF7ECMiWYGLebScJNUL-bzx0Rq4DwiTraFqxTMMAcfhCplajBgXI7ls8SvEpXXOUofZOL5L_jQtwGaUkoJ4hf8eOCPZCPIrOaBIbAo_sPhA_O57467vh92m6tsDafR2ws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f174f6ca73.mp4?token=NdjsvMYvzobv0LLwH2iO6BlBw79QOo1vk0mNeobeMp2lENtOb7MoqtDuHMNvZ_MsP4YJtHjbZwJpi9-o6UOlU4nK3HmvkAUUc_MHb3CkD4k7PrOLIFPJlY_L3tugxjBueEHm0PUPH3p7KZkRS9YMSAxOZo6nykigP8aju4U-0rOu5vvx1lAjuLbcKBcA73KsFulHwt6q3xsGX-MlwCK0s39wTHMmINNJxPMTVOn9GXaJG6WjPyVgjb_U-O2zW550Bl9ttb-hO0lQ--hW9rYwAQ5CjEgvIIXzK3Gy4dzUr1KYW2akiYARtsxHoBNkdcMLpts-A6F2i5DTLxrXc8eepZh1O7b-eGLo3-AYEVgINoW_JMOtjyY8ZjmTx3bJWFx9piD-RkNDYrCiTxuLPcc_cI15AAhsQdSgll0BWhaaw73VDs8C265KaX4niPKHhLOO-QldkWBlSDOtnNbzCSbTU_nH5O8ph6QKVKOamj-hrW5ZX7iKUBbgFwB_7LRdAV5Qqy1D76-qafbvz-c5KGBeJTMpr7p6zNS2BNDDxFU_CERF7ECMiWYGLebScJNUL-bzx0Rq4DwiTraFqxTMMAcfhCplajBgXI7ls8SvEpXXOUofZOL5L_jQtwGaUkoJ4hf8eOCPZCPIrOaBIbAo_sPhA_O57467vh92m6tsDafR2ws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کادر درمان اصفهان آمادهٔ جانفدایی در جنوب ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/452154" target="_blank">📅 20:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452153">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvcKvBttCrPmOWFiYmDAAsetbkgJAMb_KNJm3R4kQpn0v8AGfWq3bRv5UcabEdzXDoXVw2M0lvB4aHOcueBXygrgCnR2SEuBxL-TzyQzDzxFjNSEzjlgJsfA7fhMBbSDU4cxK3zfLLAaThlk2VrhUBImGoazbGDY3HobLUPnQi4EB1EN71Ho3aVbNxz_cdoGctwq5wu2uMSmN5nvJkP5X-bRzD1D36Wf1hT0xMrmJ7sEJJH8_9d-rHjl1SdjA4P1wmVuuAq9vWvGJutU99zGWSnzaGfkGumlwkprQ-lSE_SEUmi10XIAIgZ-ph-5f-3WcS8aHronFvIV2NL19HTxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
وزارت دفاع کویت: پایانهٔ مرزی العبدلی هدف حملهٔ چندین پهپاد قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/452153" target="_blank">📅 20:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452152">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzJwxFHihWtK1TTDQTWbpUE3jlleg_I8qxL1lehkQ7Yz8o4UhIYTWYsdX1upTL0-FvB7aPf2c9h0YBcZS6UUPpVKI6vhCNVWCm926gg_qaIIy5kOtq5blcTpxelYNspphE22hOHki5UeqBsP8X4wJVhO-d8-c1ykeeKcIaHdU3ZumuCHnl4QGrvaL7zn9Ugpub7WMl7WU0Z42-Mp64Ci8ZWsHd3Dy794Ib02OHzpMQKAt-YLBSoAFm4lSgFTF6G_8aBjpddZbm6ROcAQf5bLXVkkUp-jSsXspQfZaW8r2DGHMG3eqUwWRhY-0Sbo58ksDIw-oeEfUL69pAFTPMxSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
محسن رضایی: پاسخ ایران به حملات زیرساختی، تصاعدی و شدید خواهد بود.
🔹
حمله به زائران در شلمچه و تهدید به حملات زیرساختی چیزی جز استیصال و درماندگی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/452152" target="_blank">📅 20:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452151">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🎥
منابع عربی تصاویری از بلندشدن دود پس‌از انفجار در منطقهٔ مرزی کویت و عراق منتشر کردند  @Farsna</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/452151" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452150">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc396de329.mp4?token=eI0UecRJEdnPXXjXm7_SxXraGagIR5L_Ryh1UI6ugArJWXgGfi7hCcromFFq1nDfVm6uTe6alextFkD51CTXPN3IcY1Uvkfjlk-88cBviP0aht_Mp6VhxbM23EW3rF42uyEM8iz_7FvaF1ytgKJnU67uHX7PL8xr78yUSjZG4iPihhlMHf1GQrgc21QMwYhsbsGrfMkYz5sjX-PEdoKWhDgfEnMEiRq5Pnt7U3R6-_pswC_n-EXe0_AjVBMQ-tX1p07MjFXM5WC5um6W4aubkzG80Falr_3H3uovJkxuoZ4QqMWyIxdi4vVC_livdeskmmHG0AcfnKtIn2DZktGuMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc396de329.mp4?token=eI0UecRJEdnPXXjXm7_SxXraGagIR5L_Ryh1UI6ugArJWXgGfi7hCcromFFq1nDfVm6uTe6alextFkD51CTXPN3IcY1Uvkfjlk-88cBviP0aht_Mp6VhxbM23EW3rF42uyEM8iz_7FvaF1ytgKJnU67uHX7PL8xr78yUSjZG4iPihhlMHf1GQrgc21QMwYhsbsGrfMkYz5sjX-PEdoKWhDgfEnMEiRq5Pnt7U3R6-_pswC_n-EXe0_AjVBMQ-tX1p07MjFXM5WC5um6W4aubkzG80Falr_3H3uovJkxuoZ4QqMWyIxdi4vVC_livdeskmmHG0AcfnKtIn2DZktGuMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی تصاویری از بلندشدن دود پس‌از انفجار در منطقهٔ مرزی کویت و عراق منتشر کردند
@Farsna</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/452150" target="_blank">📅 20:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452149">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای انفجار در حوالی قشم و لارک
🔹
دقایقی پیش صدای انفجار در جنوب جزیرهٔ قشم حوالی روستای سوزا شنیده شد.
🔹
همچنین در محدوده جزیره لارک هم صداهای انفجار از سمت دریا شنیده شده است.
📝
اخبار تکمیلی متعاقباً اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/452149" target="_blank">📅 19:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452148">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">باز نفت گران شد ترامپ یاد مذاکره با ایران افتاد
🔹
رئیس‌جمهور آمریکا در مصاحبه با آکسیوس بار دیگر مدعی شد که ایران می‌خواهد با او مذاکره کند.
🔹
وی در ادامه گفت: «ولی آنها الان آماده توافق نیستند و هنوز به اندازه کافی احساس درد نکرده‌اند.
🔹
ادعاهای ترامپ اندکی بعد از عبور قیمت نفت از 100 دلار مطرح شده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452148" target="_blank">📅 19:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452144">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SAgvdfXD_L0-x_eAOca67fkdFQhjzKT-oFadRFQGVtMvpltV3E545aAJokFMZJRwHFk5-gPYlCwaOXLie5CsY72hn088DwODKigF-iAZHCsxaogfsSlo04vMa-0cVQuNNKeRcLWb1WpgBR4O3Va7cEWrW-EalWmUrJuCRWZb9qWiUBpWBQ07EhDGyP1K5lhO-ipVRyVRuWKcfJCFR7o8rEOO3Pt3ERftkvZ1tY9F1H1BULWda1IImdCEfoN5NBWdZpm8nAMtsRCjGzWqjkNxt46FgQbjtXonh_xN9rY5udU8HUN0EL5-zz9l9ZpfVf_ZOGKF9CYshM3qtFKZaLfM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OFtSyerWiXCypv26q3fKGfRO_WxTKmwWhT0vq9JKCmwOFzZsx_zTT7f20-SzdgJi0V6hio_8s-dxHDRqVAVDo9IE14zVpeep49YTi582P-GrTZfo0ER9LSks2emtB5wwrqItFbqYVnPXw2wRDapa5yLl0l0D1Dmbq5gjR6qL_ccJ1j8CZOEPiOYTdxyTTXdmdcXay4_Qc_nfU96jaaL7NId-l2CI6za-JKGK8emAO-qQ-N5gTPBdZXpG-6svSaizwLxh02jYkiIOiiIN4eFvufvIQlCx4_SIWc3CrVRFYcB_3_c5cChDxTIgDCLxWxGD075J-HqWbA04lKPU094VsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VFppQqb4US31o4YU9laTTL5fUC34OPgko1K8oKJyz-Fqcp9d6IgwFIphisdTqLoBIVNUSNCNZKia2W9C84h7HK_CMyYgxr8tT2E1DXUI0d8FTczKr8GH4eWpw29itBDSRwbn_ZEIHatcCad3jiYl-yUX57SsrcBpCgqBLqfn3Q-2wFGnCpajGXdTQXw4xJf9RJ1_KU_a4gz12ao7Nvi_hekYtkkrMIgc9Vi2fuUKHtLyR0jhDUA0jq_TSjFDSgjlnzP36Swiimh8ut7oUzM8g2xyC9sujlxTPpA_93ymHG_-RzhVwHhy64HjmGDKbdll2ykY4aHX917zMWsronT_zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWhkz5suAQXExr_Vibxy1o0z4pkPUYlS3lmDsXkxNbOCK9cnAa5UjapDLCsPEB_k2b2T8AL_1vtDkt3pU0sWAumU1lVtnF2yY8DzqO972x30qUMyGERvvlm_zt3w4TgDVExWPjgzpJNUBJYhq29rtZVKy8j0EdV7mG26PsXlIlyh3BqlvE9pRc6I84RAHgc6xBK-SRcADZFTJaYtYANCNG5TJDz7n_wUX4L3LmO77xU84by_1BIzN94f1Xvgdc8IIckJ0c316YDIh7d8Z3SyEkpk8fQoG2dbEw07jlV_kgEVyqqs0mgoL93ijUGR2iiCXpj3qDiEf3k3EB1Ns_MDAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آغاز برپایی موکب‌ها در مرز خسروی
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452144" target="_blank">📅 19:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452143">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y07xYZKvRQl85co4mqTwpCWpGV_Xt83Z2eG-wURJkddFu3efk1xhOUVYVoJot2amQx1FCcnRiYZZEo3mvPtSNlrcB4eUwIKnHzCuWglcu4xMpcQ7jot2blUwyJBDyUd8p2d2pWqAGsUyOyRrCGSR3IRO6iNTmjWt2UyYT2EmRkxmiy1XskDTvFw_7QoRPvT0YFkCUBa3BzJr1EthMSEnvDH8uqLeNmKN5jf9SKZUvSh-Yfry6m20Kvn10-7dyA1Z-S9HGMwF-PsYqvO-OLb9CBRYp3YoNeO5SD-UBbmrkCOos6k0DmdxnJZG_4gUrcoGs3jEyuJtxjbGtGZ40nACtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رأی مجلس نمایندگان آمریکا به پایان جنگ علیه ایران
🔹
مجلس نمایندگان آمریکا طرحی که خواستار توقف جنگ علیه ایران بدون مجوز کنگرهٔ این کشور است را با ۲۱۴ رأی موافق در برابر ۲۰۸ رأی مخالف تصویب کرد.
🔹
در این رأی‌گیری ۴ نفر از اعضای حزب جمهوری‌خواه با دموکرات‌ها همراه شدند و به این طرح رای مثبت دادند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452143" target="_blank">📅 18:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452142">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvHlIJ6cLMtfDzwh-H5boLf-3UW8XjVv8AXZ-PcoMiREEK48nGX0zdE6P8uWfxSJYgn0OM7hya4TPvJvX8X87xkrUHHI8xDxjjrgySsuRizjygrNU2Fw_UKzXHCqJPDWWi8JzF-_5PEwymGr8rWReEJ_dx8RrjxWNtAXM4SFqCntLCvUHuSW8rgsgaWgRyIYHumSJ7tYntEReRrnxZZJ8wDFwAd5ezi43-GWT9KMkl5Haotak2r29Wv8ZLdNWC5CFBdXmlp7y844aoJcZAqN1wMBfzpBvHqu7n2hvJHD7FVydUfZyWjWZPPRi9JyOv2u-6rHwWz7CMYWz-hsvRp17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نفت ۱۰۰ دلاری شد
🔹
قیمت نفت برنت که از چند روز قبل با اعمال کنترل بر تنگهٔ هرمز توسط ایران در پی نقض‌عهدهای آمریکا روند افزایشی گرفته، از ۱۰۰ دلار هم عبور کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/452142" target="_blank">📅 18:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452141">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌ سپاه: دیگر اجازه نمی‌دهیم آمریکا با آتش‌بس‌های فریبنده، ذخایر نفت و مهمات خود را جایگزین و پس‌از آن مجدداً حملات را از سر بگیرد.
🔹
ارتش متجاوز آمریکا که در تجاوزات خود بعداز شروع رسمی مجدد جنگ، از پرتاب موشک‌های کروز از شناورهای خود در اقیانوس هند بهره…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452141" target="_blank">📅 18:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452140">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌ سپاه: پاسخ حمله به مسیر زائران اباعبدالله را با حمله به پایگاه العدیری کویت دادیم
🔹
در ادامهٔ تنبیه متجاوز و پاسخ به جنایات ارتش کودک‌کش آمریکا که سحرگاه امروز با حمله به مسیر زائران امام‌حسین، ماهیت یزیدی خود را بیش از گذشته آشکار کرد، صبح امروز رزمندگان…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/452140" target="_blank">📅 17:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452139">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">📷
تردد زائران اربعینی از مرز شلمچه  عکس: فرید حمودی @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452139" target="_blank">📅 17:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452138">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu7mo3_6-oy5zXzSE89QUZdafmkPePnksl6W87pWgMq1EyzMwDq_vSIm3N_kKXuGT7xzc3fZotqgxJsdkjbdXykYj4tqGU6k3pCZqanP9Cz1H438rfJhe_QxxyQKgSlaE7ApfrgGmaKEhNllJZCqzLZog_cM5DMaX1g4CLJGVx8aWlQMr5U5QN_13zAl6WqbesF-zTE9kO_D8cGyXjvpYc5X8iPW2BlU5LyrUkEw3c8_zr0FqE3ge5KnxBGbC6F01pcf_3vM9B7UCZct7LI-KVq11BhYe2g7RBHZKzfwLOlB-2u7jFp6mzL9VnKCn3lLSHLAOLxWQRij1iIWjxaGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452138" target="_blank">📅 17:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452137">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DuTqa1ErNSBen2QdMaHvToxA66b2H5kbCHlaZ60_ORWbBwexHDsi3LqmjX3Ar7Z9CMSE44Ee7C5ilrhG4047ERp5W-GYOGOfVUBr30fdTzk2dg30nVQhnO-33MrwOQ1uJS9SsYx9d7nERYn2dMKgMsiLjLKm0mbgOTC3AktM_WRPfcR9bOX-9u_t7Q--O9J1wn2AyEdR64l2495oIqw3kHpcUmfK86SdGWxJd7LSWZZE-RnLVCz5bhRWOA4r7ON2G2aNEOQzMjGlUmfscHXrka9oaTpsLErb-PBofRU-wkXK5EcAgzzVJklbxGoNzDH_p1uGpVu4-VayIqomv4-0QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای شرکت در نشست شورای وزیران خارجهٔ سازمان همکاری شانگهای راهی قرقیزستان شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/452137" target="_blank">📅 17:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452133">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYMI_0-bWoRALkXRkWFgK632WS31z3pZK03PNfTraZIdkNvwgbOSjS1MBsunQ1YboSudSH44dI3xVgaliYZRy292fFnP6gkF2OEnJaV3LTgxbtChmzCRQuLhwCy5c28VNSN_D-4-lV7XHJv5-abiND3ep_ZdG53u2JtFR8YI-FF8itNH0JnI0TFqCHxPHJ_qy-EJlQEtg7-mUV7lf0cCc6rO41iDSokOBtHVCpJ-Sa9bbLxAkWiaAKjUmOyZW8jeCIjf674oVnhfePBk4mw1eZd9GUnwWNfVu1QVxKrr9nz6SNIt4qxKbBm34CvlssA3G9p-wk75U5ynY_bIy1pFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obYrucInf5f0I0ZkVsle2-6ESOcQ69gHMFnDVYZFVc7_OElvfmQ3yokRyWvmxZZ9oR7O_ez9PkDObo98FI8GXHOPxOm0SLy1O-IYi_0ZYVWqtzMsa8H7kaK6Nbqo_BPNpH0kyKSOhTT4fK4v3NzISRO5jwhnkjp_TVVX-7poJjDfidiEZn6E-gIvwRvMOXQI9-A8Fq6TRGB5STtgBh3PNIGcklJXr57du--nem7X1F7Deo6sC9Dysw1my09pwbLESGzqX5v7PIdaFOZfRKXu7HYcJP2_hjUvIXPqQzASabqmCGqfeUK63hcZf4b3oOhaS5jkeuzEPZuk4kYX8Yz1QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DoXktJN5yNByp8pxCaJIm7brs7OGs7C6leKojujvaQBtSI-LmUz971g_1dy1k7D--FkztfI9PDdZzYcRVMnYeApPPL1KFNqHwQummHGDKy8pfupJcNF3qxVgAOSM4EzFj5Mem1k9awuVdFvBuAhMgU3biaZAMDz2kBud7G0lItONdmLPCLjWJ-WpMo8ORfl8O38HxO9QiL3YM4jQ4waUqWsYRhcXNppfpfkXGsmrw5mcIZR3n-DA50jJP7zXtskbOBN4H4E66btVpmnzfxqGLgUhbXnYL7ZyNoKwvXZXKWTpfgmchA2pg1WwjXBWqSNs-WVlwzYmYlLOo43Pzvvvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GnBlyJsCv5JqKQNPHZhOBBnG0RSwORufGE6Xnh-1_S8hMvsrIJy2IXeBxR_tq2JTXo57lHffBxUERagszhRvI8DZjWHrh0VIz9PI8tqtXEw1v8X4TBdoIEh1ESMYxJIkJwSZw5D6Qhr-OiLP9Rjuw2_bVmV91qKekJMJJDNP4Onsw6-aufdTQsTDr712qZkBzsGV-dpvGP_0k-ZO_Yucib7jEyvZTa0gd91Kf0tZ0Qb-l516d1Mq9zFcmb4fA-ylzgSBvLFAf6rD5nw7vOc9r5q-zKouy3uEDWjlMwBDVtuyl25haytdRiHnukRRfqhC0B_2_LZ_SyH9GmVbsuDaMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‌
🔴
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه
🔹
معاون استاندار خوزستان: در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.   @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/452133" target="_blank">📅 17:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=Mv9vEhGCaTTGIW3RL-IzAeTdHWAatM08VNhJ0UKTxu3-da2ofinhHtu2S6Rhf8xVct0JMZisbr8sdcDL_GVihRQL0l3bSKIT7Rwhd5ptA1Zv122jZCkuUKM7ja29RGqTLvqHe2vaOH_hjasltMKOIV9xxNj23hM3MQ0NoIWPiGXHpIo8I8dni_vqibHAg6LHBSQnHv9oPb1otGn1E8U_PXj-k8rK_KhORiK5bbrl2dainZcQdYx3wysv8qu0Hgbsohy-YN2OUlj-pnOlhw61LToOjDYuBvV6xABQ5wGTIm6RHW2sR_-FrCigTuEiAE8levtJMoE9nGAeydgVtdc2yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=Mv9vEhGCaTTGIW3RL-IzAeTdHWAatM08VNhJ0UKTxu3-da2ofinhHtu2S6Rhf8xVct0JMZisbr8sdcDL_GVihRQL0l3bSKIT7Rwhd5ptA1Zv122jZCkuUKM7ja29RGqTLvqHe2vaOH_hjasltMKOIV9xxNj23hM3MQ0NoIWPiGXHpIo8I8dni_vqibHAg6LHBSQnHv9oPb1otGn1E8U_PXj-k8rK_KhORiK5bbrl2dainZcQdYx3wysv8qu0Hgbsohy-YN2OUlj-pnOlhw61LToOjDYuBvV6xABQ5wGTIm6RHW2sR_-FrCigTuEiAE8levtJMoE9nGAeydgVtdc2yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر حملات موشکی-پهپادی سپاه با شلیک موشک‌های عماد، خیبرشکن، ذوالفقار، فتاح و پهپادهای شاهد در موج ۲۶ با رمز «یا اباعبدالله الحسین» تقدیم به زائران اربعین
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452132" target="_blank">📅 17:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceeaf815f.mp4?token=SlbsWMyUkEZ-30PBJ0T4ydcoMTs4VUp8ZXW8p4xyEkLAVD7mZjY0STOtAGHLw91ytGp8CGu5n8IebSIdQfk-S_VyEToSzFJSH4koPZuW6cxeFcmezgMvs7uTSCjilENBjnCGY_7SDRwSnI-0LkKz1iGy_czsZcQ5bmnNDdrMggTciZbKibKy6i-15UzrOgAnN-sm0AndHn2cBZuIf4Zd7JXjAx7MzV0pXBf75NLfXOAq2m_WYtWfEA3qf3AsWn_vFPJfnOerWbj8yf06i6PNm6FWqs_RXW35unfgF2FS-Q8CplsmTMsHaXUvUOu5jGn0JdZTqmt1y2yiMWyJaIDhKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceeaf815f.mp4?token=SlbsWMyUkEZ-30PBJ0T4ydcoMTs4VUp8ZXW8p4xyEkLAVD7mZjY0STOtAGHLw91ytGp8CGu5n8IebSIdQfk-S_VyEToSzFJSH4koPZuW6cxeFcmezgMvs7uTSCjilENBjnCGY_7SDRwSnI-0LkKz1iGy_czsZcQ5bmnNDdrMggTciZbKibKy6i-15UzrOgAnN-sm0AndHn2cBZuIf4Zd7JXjAx7MzV0pXBf75NLfXOAq2m_WYtWfEA3qf3AsWn_vFPJfnOerWbj8yf06i6PNm6FWqs_RXW35unfgF2FS-Q8CplsmTMsHaXUvUOu5jGn0JdZTqmt1y2yiMWyJaIDhKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوت از همه مردم تهران، اتفاق ویژه در محر‌م‌شهر/ سر سفره خدا مهمان محرم شهر شد
🔹
از مردم تهران دعوت می‌شود جمعه ساعت ۲۰:۴۵ با حضور در میدان آزادی در برنامه سر سفره خدا که در حاشیه چهارمین سوگواره آئینی شهر تهران «محرم شهر» برگزار می‌شود، شرکت کنند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/452131" target="_blank">📅 17:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01ba910593.mp4?token=ao-LLTNWvaky50ixOC82O5PNSbel9uEvJx2LB7xGat08q9buaf8EDxMriNrQX0eDCEwZ_CqQ9wc4B8RdpDYTe9X6fK9Ua9BBNE8IgLbdHmF7AghBOUjClAvIRG02zHl1sLRb4CZx98TzMFROURQXMUHVu82TJR308RDrQcttAl0HklFOnrvqhsIAnngsAv7Oyg878pnGB2sEzlbD-OHKUTrda3OSm4bowTdsxfETBYdxdSEK4NFinjooChj6XnWzoMZeJORUu2lNidRjiRhz5BMBNiCsoLw9ZBfBJPDY7z_bdqyW6OVdCi_XrtpHi54vBKq8uru7w1IPWUsea677FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01ba910593.mp4?token=ao-LLTNWvaky50ixOC82O5PNSbel9uEvJx2LB7xGat08q9buaf8EDxMriNrQX0eDCEwZ_CqQ9wc4B8RdpDYTe9X6fK9Ua9BBNE8IgLbdHmF7AghBOUjClAvIRG02zHl1sLRb4CZx98TzMFROURQXMUHVu82TJR308RDrQcttAl0HklFOnrvqhsIAnngsAv7Oyg878pnGB2sEzlbD-OHKUTrda3OSm4bowTdsxfETBYdxdSEK4NFinjooChj6XnWzoMZeJORUu2lNidRjiRhz5BMBNiCsoLw9ZBfBJPDY7z_bdqyW6OVdCi_XrtpHi54vBKq8uru7w1IPWUsea677FzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گزارش ویدئویی از مراسم اهدای کلاه ایمنی رایگان توسط "بیمه دی" به راکبین موتورسیکلت قانون مدار در مازندران
🔸
این مراسم با حمایت بیمه دی و همکاری پلیس راهور مازندران برگزار شد .
#کانال
اطلاع رسانی شرکت بیمه‌دی
@dayins24
#دریافت
نظرات
@prday24
تلفن مرکز ارتباط( بدون پیش شماره) ۱۶۷۱</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452130" target="_blank">📅 17:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452129" target="_blank">📅 17:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbUCETaDFY9YVf2Vay51pgBS2dvls49B6a-JjfYbETbhpyUxE6tvYlMXAupYVilX20bCkEGPw4Yh7EHNTqr9XOvNOKF_xF8G30AdxZt7s21iq-8A9Kup15f6BVq9wmhKb6LmS5F_RIkhhDThJTrGcSW1rcCvrgHmK_hNI2ewOh6JYfICX8vyLYkjYbrHoFo4GrT3C7pnmXQqePo8thc6Bzb-iNx9GNM8YYovBvbLMRWhYAO5tt2jDrzXyI29xa0UGVxsIjrKfHo8NDdq-4dTFJdYPXKDAXuz5KpHiMdrXCnIAsqoxd3PSGfH4Ke-XPO4Dv5eWGJJA329pqma5W2xhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: نفت ۱۰۰ دلاری صرفاً نتیجۀ اختلال در روند حمل‌ونقل آن است نه تولید
🔹
آتشی که آمریکا در حال روشن کردن آن در میادین نفت و گاز منطقه است شعله‌هایش دامن همۀ جهان را خواهد گرفت.
🔹
نیروهای مسلح ما قطعا با ابتکار عمل و هوشمندی، میدان و سطح بازی را یک پله بالاتر…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/452128" target="_blank">📅 16:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMbNgRPp4VxSR0BKnVSD0y_vrqe_nQ7epcbls_0wVub6OZXBWbqU-0TGsHDXmspI1RSb8dZOP0jUKcltSey9bnokdJUxajmGb-Af-H_IIBOXLdM7DOJXhHoQbrbM7Yw0pTvnNqPoorTiv9EwWQ8rBFkvHEM3JFr3PqWn2QPRVJNYcHRqNa-LiDFZGjjGufHsNwGgFrdcriITihbWK3ErlzppPHxHIKX1BA8bFkpFwmJCjSfy72zAnjluJf_OX9hWpqG7AdujUrMKsiQf99ztUWnvADUbLoedBfnQG2LQityzMlMfxplHJD4G5Js7YNS3UIJlZdBnM-PZBrASs1o65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت از ۹۷ دلار عبور کرد.   @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452127" target="_blank">📅 16:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
وقوع یک عملیات ضدصهیونیستی جدید در کرانه باختری
🔹
منابع صهیونیستی از حملهٔ یک فلسطینی به یک نظامی صهیونیست در نزدیکی شهر جنین و زخمی‌کردن او خبر دادند. نظامیان صهیونیست هم او را به شهادت رساندند.
🔸
ظهر امروز هم رسانه‌های صهیونیستی از حملهٔ یک فلسطینی به یک شهرک‌نشین خبر داده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452126" target="_blank">📅 16:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452122">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8nQSpQ0a1WxGvgJUwkdLA-XAGsvCKqWz64xT7EXL11ZcZ5_zoZNNVex94drbbwF_JNIrFR4Q8OwOBp5rNcsoBAf32gJPBK-h3GkY4iFTP7OqqhRI1jvT604Xb6FsK6JSSbMKH1619ncIF4kPF50PVSKh4crq07JSyDOT8zkbqBz6sCuFjhDF4cse4KTiFgWw9nDPuyxqMsNiQTcQXRmlHMHa1ga9nlSL4CHLMYl2UpzK4U18c5zocM80LEllWCXmeUTT4KauEF5X6noiggH3u0NOw-kObI0fxW6Ifdxuk76zGMKiCAMZ1Pz9uJK-1s43gZveF57ce9vFRU9qgAP6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BLTxgQykd3I1hmsRHPX1HjP4Bw8Ub3dZ5eRo6bAeArR99sowvLcgD3pvgq9ILcRbJyMbl_8TehICzur_ymn_Uvg_Jw4nu60XCt7w4lN3wfObSwft9zILfhW2G_koMXxpvRGtgd2AO5vXW8-9bC4fNDMaGE6pxDQnfQ06Grm05ZaQK-T4I1XAn0e47MWy7TOvq_kZnWiSkN43_PibIgckusY6WLAt8krK78PJ8yK1qGuZJBG_hedjGbLSLYgcZNPLnZ6K9h0_x6cEsUwGiB8c3Aw15vWIgsWNgCyGshO1QSSaZvq3zrpEwcveMYTYGvQT7Vq7pkSnOFrEXn9FciqdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSpF2K08jYrTHcnVqbUczUD4iXfqrmFwIGu79Vmd-FFEdey5_DGWElGK1xfXCCeFqxCkqutvUwlpwpiMT_B5wBTSm7pt1qJBIaBUPR6Q7Ejf2xvQEI2UG8eVd5-nnpQqb1tp1aPPPX2p4Ar5B-YHAIXwWNzE5cAXS6LWisfSXjbITsIzfN8GWoJ7TPVeTW10wDDdIqJOYS8sLvonMGJExmWgNyR8LCjuiRVhABCwVzb7lqeusajJmdlNp9LYdHQ1B8lDTFPu4CKbj_Ll2vCqjQIBV8tgfjADs03Ua90gR0PJ2Ev4biBOpOeY_tHKRpO7qQAtuMUQfibr45I-u6q37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCB1_JY2oKAh0C-WgWxjoxItG1kxlhmKi7N8b9uqyg7XqzlaWnNybDKhlTpnjhtATboQn0hK9_Kn_e9-ECoeFiQotfxscf-XrgZ9XGnBpeTdD4QmQDEJNA2RCO2Xk-snZww5xk6WgQpIiiJfXvoRQdnGNpzIu5bo3vUEhoInIpu5q7uyFpVD8kqaFvRDweLv2lPhr3Rbe6AUpmKP4ZZ3G1hqcCk1KJi1bkfXSEEW9_I1BaWJN8gM3kx7KKHBXz1goWPDlBGhjhO_M4HIJ-GkS3AhyLDjdz6GahZXaDzuC4gNxqUFVLHpBmrvPELMtivrK0AJrPBrgTYqrCtSS9E4Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
فتاح، اولین مهمان اتاق گفت‌وگوی جدید خبرگزاری فارس
🔹
رئیس ستاد اجرایی فرمان امام (ره) امروز در خبرگزاری فارس حضور یافت و علاوه‌بر گفت‌وگو در جمع مدیران خبرگزاری، در استودیو و اتاق گفت‌وگوی جدید فارس خاطراتی از رهبر انقلاب گفت که به‌زودی منتشر می‌شود.  @Farsna…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452122" target="_blank">📅 16:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452121">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqPW3EQ_nYSyKjHAO3QGuh7m6vlfD6On_wznW2i8qZ4qNtlK3PcDNTxVhUqkql0iUNLgRtAeuXt1uItiDYgKCb0COb-bffTVQmL0QkySu-ZZ5e4etJq5o1AV2-YYSIx4wIXOpbVyjmv2PMqe2MKuZLfxk_QwVs0EntOp3SBS__zqLOofLRhQ22Ic3JJdgM0MwNAqMHLWegR7tBb5AEeacCJC8W9LnNRMGdqdX4KWwEeN9e4lSv8mJjK9K_y6NI26Yc4--lijKBcRlkONG1Uota8hXF3p-AX29lrWNiBzt_AvJ6xjfUTBtukT9RPA-sfMYOmf__4bURTRrwLT_px-ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
وزارت خارجه صدور مجوز استفادۀ آمریکا از پایگاه‌های انگلیس علیه ایران را محکوم کرد
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/452121" target="_blank">📅 15:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452120">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AawuTHlY8T4zKTPUNMW18Pf7SLHZxS1Xz6ZB07obKJ3-LMcu948b66kmkAz5VvLjtijWeryzoKRwNyylE9UUb0M2wI5y2ZzU16gF08L0bFndtjolY4JvFsfaNsu_ia8q90xMhyoOjXYi5ZX4TpPUed8MUtcWCiMGG9mriJVLzedLi03DYhgYOy3SFV7tV30qTXw2iG9-ESWp5aPM7DU0IZWj3524U45kSxbefKXWvPTfzUo-B0iei1Ggwd2WMaf1GCXO9sDvHBRHzN0ljqUvHXZG7w2BRX2ZmclOgpOq0-zLU26esSxvm5TdbQjlHssSgT078-lUSNsBnh5hjoHH4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توافق هسته‌ای با عربستان منوط به سازش با اسرائیل است
🔹
توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در دست تنظیم است (که به صراحت متضمن هیچ‌گونه غنی‌سازی مواد نخواهد بود) و تنها به مصارف غیرنظامی اختصاص دارد نظیر آنچه ایران، امارات و دیگران پیش‌تر از آن برخوردار بوده‌اند به تصویب خواهد رسید.
🔹
اما تحقق آن تماماً مشروط به پیوستن عربستان سعودی به «پیمان‌های بسیار محترم و موفق ابراهیم» است.
🔹
ایالات متحده مخالفتی با تاسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452120" target="_blank">📅 15:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452119">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انگلیس هشدار سفر به کویت و بحرین صادر کرد
🔹
انگلیس به شهروندانش هشدار داد که با توجه به شرایط غیرقابل پیش‌بینی منطقه، از سفرهای غیرضروری به کویت و بحرین خودداری کنند.
🔹
هشدار جدید لندن کمی پس از آن صادر شده که دولت انگلیس اعلام کرد کارکنان خود را به‌طور موقت از ایران خارج کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452119" target="_blank">📅 15:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5584145f6.mp4?token=g_nAjd5arKng_6HaPljsaQEoLQ6JlfzY8F0oLqVVWuVGhe2opC2FnveMY6cTlG3WygtjshRdiW6V-qelWxmZn_9GyX_AEwt4iit9SkhVtsKcxQtCHycPozFWzVfZHxnVomkWGM3yKApBA6iUsi3vVbNxlEaJg_DjC8KjwrQEWl8OqY8NgYucxj5cOFraGPb_gMo8smCdYKblDRHevWCKRfBDdeTSFNRzUXxbu36EP4uWVMoyqrxgaWqMl0HIvGB8vsSNxQqhkWohnoemIWG2mlGo-6k_LPjyQvRoZSe0ZLatMhormh8fksLsJje01xLQ1pW81I_REGYvLnI1BHRabmYQaUW6sh7k5YW8KKjCaY4KaV14Q8ziN7GeFyeRG24cVmNTQl0Hr-YLxZWbLaI5JOqfRiwGzkoBN-xMzdL-oixv_KwYif5TqnSxMWarrM0JW9fjHDaJDFy2T12q7H5q30WZoeYNfXj8Sc2AECCtigr_nk8K_FpbABqfxUYwqjpApSCIy3xvWftrDbiZ95gp7mSJ4xRSha-pRlzDbrt1UO2IQxGxBQSywX1vlWof69EuARUTDTg2MJjHqZtoz7I1avaeT-UEVrYyy2HK9xY4eIZTo21PHdtydOvwNWuY_g7GBAnGBF-6kq92cd5SfN6w2D8pgP8r9Xg6O_Wt3SX6GQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5584145f6.mp4?token=g_nAjd5arKng_6HaPljsaQEoLQ6JlfzY8F0oLqVVWuVGhe2opC2FnveMY6cTlG3WygtjshRdiW6V-qelWxmZn_9GyX_AEwt4iit9SkhVtsKcxQtCHycPozFWzVfZHxnVomkWGM3yKApBA6iUsi3vVbNxlEaJg_DjC8KjwrQEWl8OqY8NgYucxj5cOFraGPb_gMo8smCdYKblDRHevWCKRfBDdeTSFNRzUXxbu36EP4uWVMoyqrxgaWqMl0HIvGB8vsSNxQqhkWohnoemIWG2mlGo-6k_LPjyQvRoZSe0ZLatMhormh8fksLsJje01xLQ1pW81I_REGYvLnI1BHRabmYQaUW6sh7k5YW8KKjCaY4KaV14Q8ziN7GeFyeRG24cVmNTQl0Hr-YLxZWbLaI5JOqfRiwGzkoBN-xMzdL-oixv_KwYif5TqnSxMWarrM0JW9fjHDaJDFy2T12q7H5q30WZoeYNfXj8Sc2AECCtigr_nk8K_FpbABqfxUYwqjpApSCIy3xvWftrDbiZ95gp7mSJ4xRSha-pRlzDbrt1UO2IQxGxBQSywX1vlWof69EuARUTDTg2MJjHqZtoz7I1avaeT-UEVrYyy2HK9xY4eIZTo21PHdtydOvwNWuY_g7GBAnGBF-6kq92cd5SfN6w2D8pgP8r9Xg6O_Wt3SX6GQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فتاح، اولین مهمان اتاق گفت‌وگوی جدید خبرگزاری فارس
🔹
رئیس ستاد اجرایی فرمان امام (ره) امروز در خبرگزاری فارس حضور یافت و علاوه‌بر گفت‌وگو در جمع مدیران خبرگزاری، در استودیو و اتاق گفت‌وگوی جدید فارس خاطراتی از رهبر انقلاب گفت که به‌زودی منتشر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/452117" target="_blank">📅 15:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
انفجار و بلندشدن دود در گذرگاه مرزی العبدلی کویت  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/452116" target="_blank">📅 15:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452111">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTifrGrH1TQR5Yvhsn2Dp9Agnz1YMGs5kLaCmz8kGWR1ABo_KHM32cJcz5vK8HZCIlfP_cUA9ANt9iMZPiKODCF46yJNYbxGLhJjeAmvxDUpRLnaYv8CrteFRHIfH_s8MB8u0a7nH9S6eQPdzpiSPpuk7wMqSxQZi7JYD8wSy7JIob5Si4Ll7GSWfL80EXMcjJyBEIyZPq99APMWkm5r8R8nYPes3ssuHjah6iv1pe8Lixe-UTUelkacfMOtrK9SRIUKjqJI9zrcbhUJRMY8aWJvrZxlyt7KwXN9uCLWZYoAhG8YI9RIdcD5gwxNg0H71Ozmc1ydwAXysdcdsEq-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3417c43d1e.mp4?token=GdUgu9ObM0AIWXJ8eIOHgooxi87QsEItF1pkzBcobrMrsQ1WnO5S_goBC9nNXBECD5VP9DybaYrE4eHWU0QNY4UUv7AAiOQax9_g7R1UJXLV9XDGWr8xrim3hW6GI_gi7PzAwSNbrh1VzQzsR1wSG6GNOWOhcUCkcqghajuSNjhtkm5Q4uV90Ekzz60JwPVPOk8YW5MYCizar0lM4bGxQuD0s2tlidZqdbH1rXdIoLEj2gXVx9_N-PnsirKFKLNRke3gQW6zA9DpCmZEqJYFjS2opoLS3BdxPfdV6WQ1slPgF3iewMnqB69jxCbKVnVoVhHESWHY1oBanyZb83YkdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3417c43d1e.mp4?token=GdUgu9ObM0AIWXJ8eIOHgooxi87QsEItF1pkzBcobrMrsQ1WnO5S_goBC9nNXBECD5VP9DybaYrE4eHWU0QNY4UUv7AAiOQax9_g7R1UJXLV9XDGWr8xrim3hW6GI_gi7PzAwSNbrh1VzQzsR1wSG6GNOWOhcUCkcqghajuSNjhtkm5Q4uV90Ekzz60JwPVPOk8YW5MYCizar0lM4bGxQuD0s2tlidZqdbH1rXdIoLEj2gXVx9_N-PnsirKFKLNRke3gQW6zA9DpCmZEqJYFjS2opoLS3BdxPfdV6WQ1slPgF3iewMnqB69jxCbKVnVoVhHESWHY1oBanyZb83YkdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
۲ شهید و ۱۱ مجروح در حملۀ موشکی آمریکا به مرز شلمچه
🔹
معاون استاندار خوزستان: در حملۀ موشکی دشمن تروریستی آمریکا به مرز شلمچه، ۲ نفر از هموطنانمان شهید و ۱۱ نفر مجروح شدند.   @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/452111" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452110">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=r0nwL6Ou_Pym5eIE_PBO4yjUtbKRCoe4KqCzjQYj-p_SR6xY92ChgSv5Uc03-l-3ITwBo21lcP4bN174YcsRHiBi00Wm_rXA4IXaakGb9PS-l7HWnmwvfF1AaikZGRivi4471GlG-o_woyznV6ih9igLktAX0zXTOM0gwGLpKd9ktZTBmO2vux8v8a6a8UwwRYrkEfr-8Tzai2UAyWA7JZzyYmORNKThDLpiIJ0ZmC-3yc4vpvf3OjgktoQrqTDhOaOUZBXBozntKL97R60sHQwYAW9aqudbw3HI6q6ZXGzYGyJV2YVx5u548dBZ9oz-xV61GQAWDykZjIvRYxKwng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=r0nwL6Ou_Pym5eIE_PBO4yjUtbKRCoe4KqCzjQYj-p_SR6xY92ChgSv5Uc03-l-3ITwBo21lcP4bN174YcsRHiBi00Wm_rXA4IXaakGb9PS-l7HWnmwvfF1AaikZGRivi4471GlG-o_woyznV6ih9igLktAX0zXTOM0gwGLpKd9ktZTBmO2vux8v8a6a8UwwRYrkEfr-8Tzai2UAyWA7JZzyYmORNKThDLpiIJ0ZmC-3yc4vpvf3OjgktoQrqTDhOaOUZBXBozntKL97R60sHQwYAW9aqudbw3HI6q6ZXGzYGyJV2YVx5u548dBZ9oz-xV61GQAWDykZjIvRYxKwng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
پیام سپاه به مردم اردن: حق قانونی و شرعی و منطقی ماست که پایگاه آمریکایی مبدا تجاوز به کشورمان را هدف قرار دهیم
🔹
روابط‌عمومی سپاه پاسدارانی: مردم شریف و نجیب و اردن؛ برادران مجاهد شما در سپاه پاسداران انقلاب اسلامی، در تنبیه ارتش کودک‌کش آمریکا و پاسخ…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452110" target="_blank">📅 14:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452109">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6380e0c517.mp4?token=qybeIWlo664F2elWR9bCwrrJzdxN48-qkTJ04kzauDeEDtVxVB8okxpNtz5DIxubgseEiEX_gRnzyTLILWl_abm60dDSqoaaQTl3rQqPxlPpg11pe_PNZOxtrZERK49YOLj7AHB_VmmgPB2iozEHcWflEDzMarPn2rheMd7v_I5vNRTBkj7S36huxXzaGJtwo39jGU2j4dDbZJQeW13M7U3KjebeVUv2wWtLgjcTLVEdu5DSLaPrOEQvl4heFnuJWAK6b2ErMubuGGbPdgYDNNzI4dYdKeHoZvSnyyyUStJPJSqO9Dq4PLq6x13oNumz0SJyFuslg_hdri1Ikcqnxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6380e0c517.mp4?token=qybeIWlo664F2elWR9bCwrrJzdxN48-qkTJ04kzauDeEDtVxVB8okxpNtz5DIxubgseEiEX_gRnzyTLILWl_abm60dDSqoaaQTl3rQqPxlPpg11pe_PNZOxtrZERK49YOLj7AHB_VmmgPB2iozEHcWflEDzMarPn2rheMd7v_I5vNRTBkj7S36huxXzaGJtwo39jGU2j4dDbZJQeW13M7U3KjebeVUv2wWtLgjcTLVEdu5DSLaPrOEQvl4heFnuJWAK6b2ErMubuGGbPdgYDNNzI4dYdKeHoZvSnyyyUStJPJSqO9Dq4PLq6x13oNumz0SJyFuslg_hdri1Ikcqnxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: ایستایی یک زائر در شناسایی و مهر گذرنامه در مرز شلمچه فقط ۴ ثانیه طول می‌کشد
🔹
بیش از ۳۰۰ هزار نفر تا الان از مرزهای چندگانه وارد عراق شدند.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/452109" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcab2e787b.mp4?token=phBdzCikdLO9ukImB4HjzwoYgKqsIcW8cGvfzbBFwcjIlOCTDywaCFgyzS74j8aLyA5P-nVF9n4qsp5i6iFUNC3NvOZyiX4Hks_FWHVJwDbpy8c8uDjtJixGR97gO49hxeVWa8J5pZb_EyGnJeenR7oqk88bgmafSS16OAC7TMNyje1nmV-raa_1c9Me5l2VRfs-T06pRKX-nviYHK7iEg2FUuLfaPmt9nk3u4-NvgrBtMlp_rQDXHndO6n4MyQCpV2h4sm5s2or7X-HTHWbhsspivzK6FUf1vdhlveIrdwLRDnNW0KVUVcrnuUv5vq2p8HmfpXnAk47Qh5n7iUgZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcab2e787b.mp4?token=phBdzCikdLO9ukImB4HjzwoYgKqsIcW8cGvfzbBFwcjIlOCTDywaCFgyzS74j8aLyA5P-nVF9n4qsp5i6iFUNC3NvOZyiX4Hks_FWHVJwDbpy8c8uDjtJixGR97gO49hxeVWa8J5pZb_EyGnJeenR7oqk88bgmafSS16OAC7TMNyje1nmV-raa_1c9Me5l2VRfs-T06pRKX-nviYHK7iEg2FUuLfaPmt9nk3u4-NvgrBtMlp_rQDXHndO6n4MyQCpV2h4sm5s2or7X-HTHWbhsspivzK6FUf1vdhlveIrdwLRDnNW0KVUVcrnuUv5vq2p8HmfpXnAk47Qh5n7iUgZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نشست خصوصی پزشکیان با نخست‌وزیر عراق درحال برگزاری است  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452108" target="_blank">📅 14:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452107">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383c67b5bc.mp4?token=XKWCXckVXl_VnBO-9TfLXttQQyDup1B1VtBjOqmPxMMhGO8-rOtY5JMt0E68qOuWn9qgSEEC-GsvkFEaWEjEYl5ojN61iwyspLaeiQyGynXA9Mv7futV2215fHIOmGObbTcEsGugVImElTNuaXFIqHCafuytRKYy8URdqiBrW_FKtRiG01Q-Hxb91vCd53lGV8f1jqhj3uAH5C0mVSI_bFEF7bl2g-4IaVU1YKa-ybvCEB-1oRopoLv3ckes_2vkUAJRfhAYe67V7ooGKTNDkBS4xInwHzc9LXkkLA3j3Vt1vclAlHwF5EUMIsuhmc_V5lrZ5ciQkelMjXjX2VxdCq_ndh1tUCPkq-K_SkrsQoB1I1MlFGpp8p6on8Hyv1xKy7vDKGlQt_R4K8g9qrv1hflZrAeqP-RViSaUn5FnhQEDXWAOH21fr1KwIPjlPzp5cEf8Jw89Hj6xd2DLrtUSwlH7vZBGon1Jc2qQcomn6DCFuOeSRJX45ntTax5WLJlWESllv3OTn2ksPTiJxkfl-Y_QZzbZM7i0ENEL5T9aZSifWAwqt_2qCtUJtCsEhYuYmfA6qBuDpymDS1LfPVSb8640vOSmvEMkQw_vM0MR6EK0aP6nB0-Y8fEgoNqKJRUyoLzIQb2P-0HdzULt2U-K1MfOmfIiyGJJHq0cGmKY1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383c67b5bc.mp4?token=XKWCXckVXl_VnBO-9TfLXttQQyDup1B1VtBjOqmPxMMhGO8-rOtY5JMt0E68qOuWn9qgSEEC-GsvkFEaWEjEYl5ojN61iwyspLaeiQyGynXA9Mv7futV2215fHIOmGObbTcEsGugVImElTNuaXFIqHCafuytRKYy8URdqiBrW_FKtRiG01Q-Hxb91vCd53lGV8f1jqhj3uAH5C0mVSI_bFEF7bl2g-4IaVU1YKa-ybvCEB-1oRopoLv3ckes_2vkUAJRfhAYe67V7ooGKTNDkBS4xInwHzc9LXkkLA3j3Vt1vclAlHwF5EUMIsuhmc_V5lrZ5ciQkelMjXjX2VxdCq_ndh1tUCPkq-K_SkrsQoB1I1MlFGpp8p6on8Hyv1xKy7vDKGlQt_R4K8g9qrv1hflZrAeqP-RViSaUn5FnhQEDXWAOH21fr1KwIPjlPzp5cEf8Jw89Hj6xd2DLrtUSwlH7vZBGon1Jc2qQcomn6DCFuOeSRJX45ntTax5WLJlWESllv3OTn2ksPTiJxkfl-Y_QZzbZM7i0ENEL5T9aZSifWAwqt_2qCtUJtCsEhYuYmfA6qBuDpymDS1LfPVSb8640vOSmvEMkQw_vM0MR6EK0aP6nB0-Y8fEgoNqKJRUyoLzIQb2P-0HdzULt2U-K1MfOmfIiyGJJHq0cGmKY1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال پزشکیان از نخست‌وزیر عراق در کاخ سعدآباد  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452107" target="_blank">📅 14:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452106">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35decde86f.mp4?token=MI1DLgVPr4XFK7TZFypTVJmdfpxR_VcoqY5ekwkCkwcMI9CNEKOt67arcpfL_eIfZhhkSmQPk8mSGUL19m6hFDjkq7-HksgGnJog-CgraNLt3jwtQ0ltsO9Q4gdZvAu-PkgSusgADpcPUwQxdHfoBdvIM6MTzHv1AkI1ff8Go53Bbz4Wx6MCSqVoKMFl2ihiNVAOECPJ1WdZF7j4ibAcXNrSyl-ZWKnT8wadp2ySqTOJeu-3P8vSYyfUlPIUD-QiKBrTzpp_zYjlatUjWoF5MIMviUD8xUqq0vNaAB_LlzSvPdKffSveGgurm8QVNwwyE5WfR7HHVwuASIskjmeApg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35decde86f.mp4?token=MI1DLgVPr4XFK7TZFypTVJmdfpxR_VcoqY5ekwkCkwcMI9CNEKOt67arcpfL_eIfZhhkSmQPk8mSGUL19m6hFDjkq7-HksgGnJog-CgraNLt3jwtQ0ltsO9Q4gdZvAu-PkgSusgADpcPUwQxdHfoBdvIM6MTzHv1AkI1ff8Go53Bbz4Wx6MCSqVoKMFl2ihiNVAOECPJ1WdZF7j4ibAcXNrSyl-ZWKnT8wadp2ySqTOJeu-3P8vSYyfUlPIUD-QiKBrTzpp_zYjlatUjWoF5MIMviUD8xUqq0vNaAB_LlzSvPdKffSveGgurm8QVNwwyE5WfR7HHVwuASIskjmeApg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین اژدهایی برای دفاع از ایران، در تنب بزرگ قناصه به‌دست شد
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/452106" target="_blank">📅 14:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452105">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b027328a6.mp4?token=cVtBnYPFJRVTH5TQpsE7-FUawfJU6Gk2umzbU_HuCYN29f_1Nx13MqAMO0epasmSdidnvpHv733qwaJyAeivlZ9-wHkzMSpXNmOB8dqva3rx_K4l73PkswP_sDHlV2ExFYkW4RolHdtAOsvmQ83qWbWdpWS0IRSb71LKz99MCUbonB_btQCbxR4-W1hbRYb0XY5vCMZseYWVBWVmjU9VeHhyGXr_e0vOlFzY6PPWYxVPtA9ctDAoKGVkosF11T2R09RmRff0drl5tpHBN2or5ISMImnI_Frgs8-zLvlSQXGn-akm1CNntwGll19QPneC6o4H1Rnhg3x9xr1QFuBdww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b027328a6.mp4?token=cVtBnYPFJRVTH5TQpsE7-FUawfJU6Gk2umzbU_HuCYN29f_1Nx13MqAMO0epasmSdidnvpHv733qwaJyAeivlZ9-wHkzMSpXNmOB8dqva3rx_K4l73PkswP_sDHlV2ExFYkW4RolHdtAOsvmQ83qWbWdpWS0IRSb71LKz99MCUbonB_btQCbxR4-W1hbRYb0XY5vCMZseYWVBWVmjU9VeHhyGXr_e0vOlFzY6PPWYxVPtA9ctDAoKGVkosF11T2R09RmRff0drl5tpHBN2or5ISMImnI_Frgs8-zLvlSQXGn-akm1CNntwGll19QPneC6o4H1Rnhg3x9xr1QFuBdww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سه پایگاه آمریکا در کویت هدف مجدد حملات پهپادی ارتش قرار گرفت
🔹
روابط‌عمومی ارتش: در پاسخ به ادامۀ گستاخی‌ها و تجاوزات دشمن خبیث به کشورمان، ارتش ایران  در مرحلۀ بیست‌وسوم عملیات صاعقه، ساعاتی قبل محل استقرار انبارهای مهمات و اقلام لجستیکی  ارتش کودک‌کش…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/452105" target="_blank">📅 14:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e54c631b.mp4?token=aN_hfd8-4FUvg_29aPKgVgKUStVlp8Syjvq7lUVqIzkssKbGTmzSw2YtdKaMmtE151yeJBco70BipOJfckKvEmvE9OJJqnkGGLEvBzD4NHe0g-mE3Srr3vOLF2Q8gH_v2GHouwXUbkzpOeLitw_YRmNPVW7j2gyj8RQO1WCCUnkBy5Bn2jOGtNS-GwMohzrVZDP7OOWw6_as2Hhaz4BYabPfpNcXzi0IULsAzlY1By2nTi_t6mBmImxxVwF_UHh32XkJQERHaQ2d9WdVIbslFnTpcOqB2C0q1dkZf3sULj99mlvc4ze6zZKr1HC4hsRkAioTlPzA97XHtSUk69QzQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e54c631b.mp4?token=aN_hfd8-4FUvg_29aPKgVgKUStVlp8Syjvq7lUVqIzkssKbGTmzSw2YtdKaMmtE151yeJBco70BipOJfckKvEmvE9OJJqnkGGLEvBzD4NHe0g-mE3Srr3vOLF2Q8gH_v2GHouwXUbkzpOeLitw_YRmNPVW7j2gyj8RQO1WCCUnkBy5Bn2jOGtNS-GwMohzrVZDP7OOWw6_as2Hhaz4BYabPfpNcXzi0IULsAzlY1By2nTi_t6mBmImxxVwF_UHh32XkJQERHaQ2d9WdVIbslFnTpcOqB2C0q1dkZf3sULj99mlvc4ze6zZKr1HC4hsRkAioTlPzA97XHtSUk69QzQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لفاظی‌ روبیو: پاسخ ترامپ به ایران «سر در برابر چشم» خواهد بود
🔹
وزیر خارجه آمریکا بر تهدید دیروز دونالد ترامپ به هدف قرار دادن زیرساخت‌های ایران که مصداق جنایت جنگی است، تأکید کرد و مدعی شد ایران در صورت ادامه روند کنونی «بهای سنگین‌تری» خواهد پرداخت.
🔹
مارکو…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452104" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9Qho1XyXef9NEzM_QJhO2Bv-tX0K8xa7kZuGu5ia5MqyTQVAVYj8S3V6zWHfD_sKeVrOv4kaJiXVleaq0kNCiXBypYCPoDY92-qlUYsDgOVVPFxQ7Yy_GN0A_wBDzPuAFnlcxsTZksjRfplw9onAU-0ZPOpQCgtGJdWBPdJ_x0ldaI9qYQDvudFgcUGe7TDayhpgWdIxApaaYpCF6B6Wgcn5Fom-ZAchbCaf7-lb9cOrtgQ9GGZWrrLObdddGm_8_y0KFdtlYsbjnYx_YNTEFlScZZQs3oAGR5wGC-KMA9YcZ5ItjNND9sAn6sDGYAeJfW79Cddk90lMCzGZ8uopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مراسم بزرگداشت شهید زهرا حدادعادل از طرف خانوادهٔ ایشان
◾️
پنجشنبه ۱ مرداد، ساعت ۱۷ الی ۱۹
◾️
میدان فلسطین، مسجد امام صادق علیه‌السلام  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452103" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50e3811ea.mp4?token=LhXTZLrK1yPB6SGy4Zb6E-wyhEf0QMZ5H-Tmd5siSaRmwRZUSXXCwo4E9eLn3ziUopg3T85nCDaefwuIgjC1D7Rnju08CGhLpQrIE329FwoRyDxuH-j52V2UhbX5tRcncp0_A2HAWFWjp-5jJSTD-M1eKJDsf15m3tpUVzk278P9PAmAsuR_nhgLUFY_SfEoKb-haviqk9izPeAXcWiFzEjqHbnt6QRYqWTeo_33jrj83lr-YznIJL3COySsHSrpW3k-FpfMJFZYau0SXlSzGeWnBtoVNyHb3YZ9K0UEhvpaW4v8sn_QjxKT_6jYSZGsuKdV5TPaShV1lZdIGGcq5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50e3811ea.mp4?token=LhXTZLrK1yPB6SGy4Zb6E-wyhEf0QMZ5H-Tmd5siSaRmwRZUSXXCwo4E9eLn3ziUopg3T85nCDaefwuIgjC1D7Rnju08CGhLpQrIE329FwoRyDxuH-j52V2UhbX5tRcncp0_A2HAWFWjp-5jJSTD-M1eKJDsf15m3tpUVzk278P9PAmAsuR_nhgLUFY_SfEoKb-haviqk9izPeAXcWiFzEjqHbnt6QRYqWTeo_33jrj83lr-YznIJL3COySsHSrpW3k-FpfMJFZYau0SXlSzGeWnBtoVNyHb3YZ9K0UEhvpaW4v8sn_QjxKT_6jYSZGsuKdV5TPaShV1lZdIGGcq5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر ماهواره‌ای از حملات امروز ایران به پایگاه ملک فیصل در اردن  @Farsna</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/452102" target="_blank">📅 13:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b94d872.mp4?token=c7p15_HLeCMW7tRPqHluZhOThQhHIGTGmghs4NAVH_JDY7ajVTdqz_aO-7pM9i0-WvaRg2vs-qHr4_Q3fPV9CwbVm4sb5cfIg83iOXrUUNZAwT1s2Ve2jAZTtsPM5dFboWY4Bq9wso6AfT5f4rZ6qEdmvy3zUx6tZb1732yXwP9TQWIWAeWLaMWoJigNUMavMLw6QFP5fuS8vFvzKafGOZMjtwJD3of4bhEHrXguPJNI9TWGbYMimmX-zicAlYnf1J4sMZlwxgvaeC8l5SGZbXkit4-Ofm0GcJ_ejVFrxt2WANjnyPYXSEkGkYCHSGssInPIXWZnXGIG66L4xu0SLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b94d872.mp4?token=c7p15_HLeCMW7tRPqHluZhOThQhHIGTGmghs4NAVH_JDY7ajVTdqz_aO-7pM9i0-WvaRg2vs-qHr4_Q3fPV9CwbVm4sb5cfIg83iOXrUUNZAwT1s2Ve2jAZTtsPM5dFboWY4Bq9wso6AfT5f4rZ6qEdmvy3zUx6tZb1732yXwP9TQWIWAeWLaMWoJigNUMavMLw6QFP5fuS8vFvzKafGOZMjtwJD3of4bhEHrXguPJNI9TWGbYMimmX-zicAlYnf1J4sMZlwxgvaeC8l5SGZbXkit4-Ofm0GcJ_ejVFrxt2WANjnyPYXSEkGkYCHSGssInPIXWZnXGIG66L4xu0SLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روبوسیِ پزشکیان با نخست‌وزیر عراق  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452101" target="_blank">📅 13:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452100">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=hswwmAl7QMfqE2yDgNsBHq7D6HJb8uNIqpNG1fWFynfK3lt9v_mIUzOdrBaT6jDPgZ3B8R2Kcfq02h1GcfkY-GCqQ0sLorsrqfWiN_1bCY5oTsvgao6VELRHizUpB9tYUu-uJG5fLeHia9zI5NqAUpsgWGq7-gsrw5nYqqYIsjSCoG2AWDM7Ntfew33l72BTKYxayb1UoGM65zqAr8kMqhm70a7IECFrnelMkFjNLog3WSJWKU9iE5AEQpG6VNmZNmeMZuR8yBf6CK4QKGkBdgegpAd5JRpXpYW8qim-CUF0oZE5elbMqgTalc2xxUWUXjbBan2fEAz9zbHGqt4JXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be7716f95.mp4?token=hswwmAl7QMfqE2yDgNsBHq7D6HJb8uNIqpNG1fWFynfK3lt9v_mIUzOdrBaT6jDPgZ3B8R2Kcfq02h1GcfkY-GCqQ0sLorsrqfWiN_1bCY5oTsvgao6VELRHizUpB9tYUu-uJG5fLeHia9zI5NqAUpsgWGq7-gsrw5nYqqYIsjSCoG2AWDM7Ntfew33l72BTKYxayb1UoGM65zqAr8kMqhm70a7IECFrnelMkFjNLog3WSJWKU9iE5AEQpG6VNmZNmeMZuR8yBf6CK4QKGkBdgegpAd5JRpXpYW8qim-CUF0oZE5elbMqgTalc2xxUWUXjbBan2fEAz9zbHGqt4JXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر عراق به تهران رسید  @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452100" target="_blank">📅 13:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d19150166b.mp4?token=LfqsDYS4UkrPe6cMZhz48jUupOWh4mAsiDpm9YjpXvZyw6eOu1Kkf5nC3nsuhs3BIUM2F2GVu2Dv8DIxtlBIVo7HGw6IzGZA1e-pg4iaVUVr3aQhgF8ZdvW7_z8VXKCGx8mn9zdjwsIAjDpS8jKe0Hae2phpgl3ViZtB8SCQ-qYsYHXght7TTxXmm9-khADwxDzoxVAnYgQSHTXlaA3pUkE_udLspWyAbKLsbc6Zt04WirMAzIrqObs7U_RH4JAOoP8rm3mii9g9C7HSI76qEjgfXdPa6h2vBZXyoi-XaJGBBoLqXg2f-06lqw_YPpE2cSAql1i9lzdn-HpKd2n9PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d19150166b.mp4?token=LfqsDYS4UkrPe6cMZhz48jUupOWh4mAsiDpm9YjpXvZyw6eOu1Kkf5nC3nsuhs3BIUM2F2GVu2Dv8DIxtlBIVo7HGw6IzGZA1e-pg4iaVUVr3aQhgF8ZdvW7_z8VXKCGx8mn9zdjwsIAjDpS8jKe0Hae2phpgl3ViZtB8SCQ-qYsYHXght7TTxXmm9-khADwxDzoxVAnYgQSHTXlaA3pUkE_udLspWyAbKLsbc6Zt04WirMAzIrqObs7U_RH4JAOoP8rm3mii9g9C7HSI76qEjgfXdPa6h2vBZXyoi-XaJGBBoLqXg2f-06lqw_YPpE2cSAql1i9lzdn-HpKd2n9PDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لفاظی‌ روبیو: پاسخ ترامپ به ایران «سر در برابر چشم» خواهد بود
🔹
وزیر خارجه آمریکا بر تهدید دیروز دونالد ترامپ به هدف قرار دادن زیرساخت‌های ایران که مصداق جنایت جنگی است، تأکید کرد و مدعی شد ایران در صورت ادامه روند کنونی «بهای سنگین‌تری» خواهد پرداخت.
🔹
مارکو روبیو در گفت‌وگو با خبرنگاران در حاشیه نشست آسه‌آن در مانیل توهمات دونالد ترامپ درباره درخواست ایران برای مذاکره را تکرار کرد و گفت «ایران مستقیم و غیرمستقیم، التماس می‌کند «بیایید توافق کنیم. بیایید گفت‌وگو کنیم».
🔹
وزیر خارجه آمریکا همچنین در اشاره به پیام اخیر وزیر خارجه ایران عباس عراقچی که دکترین دفاعی جمهوری اسلامی ایران را «چشم در برابر چشم» توصیف کرد و گفت «هرگونه تجاوز علیه ایران، از جمله علیه زیرساخت‌های ما، با پاسخی قاطع و قدرتمند مواجه خواهد شد»، با افتخار به ارتکاب جنایت جنگی گفت که «سیاست رئیس‌جمهور (ترامپ) یک سر در برابر یک چشم است، قرار است همین‌طور باشد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452099" target="_blank">📅 12:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452098">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">هلاکت ۲ تروریست در درگیری با مرزبانان
🔹
فرمانده مرزبانی فراجا: در درگیری مسلحانۀ مرزبانان هنگ مرزی جکیگور با گروهک تروریستی، ۲ نفر از آنان به هلاکت رسیده و مقادیری سلاح و مهمات، فتیله و چاشنی انفجاری کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452098" target="_blank">📅 12:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هشدار حنظله درباره تداوم حملات سایبری به سامانه‌های کنترل صنعتی آمریکا
🔹
در پی حملۀ سایبری پیچیدۀ گروه هکری «حنظله» به زیرساخت‌های فناوری عملیاتی (OT) ایالت مریلند، این گروه با صدور یک بیانیه هشداردهنده، اعلام کرد که زیرساخت‌های حیاتی آمریکا در خط مقدم حملات آینده آنها قرار دارند.
🔹
حنظله تأکید کرده که دستکاری در کنترل‌کننده‌های منطقی برنامه‌پذیر (PLC) و سامانه‌های SCADA، تنها بخشی از توانمندی‌های تهاجمی این گروه است و تهدیدات گسترده‌تری متوجه شبکه‌های آب، برق و ترابری خواهد بود.
🔹
این هشدار در حالی منتشر می‌شود که اداره تحقیقات فدرال (FBI)، اخیرا با انتشار بیانیه‌ای امنیتی اذعان کرد که بازیگران سایبری، تجهیزات صنعتی شرکت‌های Rockwell Automation، Schneider Electric و Siemens را هدف قرار می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/452097" target="_blank">📅 12:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452096">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای هشدار به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیک‌ترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/452096" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4e206616.mp4?token=lIqBwe7B_yunAnpfmT-QpSTzTwdUoozD2hqrVVY1-fFq2GCaHTwX78QTzmLKMxa89fVz6px4Rj8hYmEg1nd_2YiAsOe-0SBLQlif-MkdImA_LJtKYVTnc_YCIo7xa-r9-VyGfd955dPaNQa5bX_0F6MpcRbx7LPG58EgDP1SRKuMtZDlrCDbnOIfe96dkhRoDyGpiPtxwn_TW8nbq0fXygjR3OgynatGsfLn_vHP7dakQjerDLVsjzOfM0t9IAtMreriYK1tz_jOx-eD8zE6PdqPZ8DruR_cblY5tLol0Qlr1buo8S0ltI6X250GCxh5z6q7eAdrWSd34pPxDIxaHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4e206616.mp4?token=lIqBwe7B_yunAnpfmT-QpSTzTwdUoozD2hqrVVY1-fFq2GCaHTwX78QTzmLKMxa89fVz6px4Rj8hYmEg1nd_2YiAsOe-0SBLQlif-MkdImA_LJtKYVTnc_YCIo7xa-r9-VyGfd955dPaNQa5bX_0F6MpcRbx7LPG58EgDP1SRKuMtZDlrCDbnOIfe96dkhRoDyGpiPtxwn_TW8nbq0fXygjR3OgynatGsfLn_vHP7dakQjerDLVsjzOfM0t9IAtMreriYK1tz_jOx-eD8zE6PdqPZ8DruR_cblY5tLol0Qlr1buo8S0ltI6X250GCxh5z6q7eAdrWSd34pPxDIxaHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هتک حرمت مسجدالاقصی با یورش بیش از ۲۳۰۰ صهیونیست
🔹
هزاران صهیونیست از صبح امروز در دسته‌های ۱۵۰ نفری تحت حفاظت شدید نیروهای اشغالگر اسرائیل و با همراهی ایتمار بن گویر به مسجد الاقصی یورش بردند.
🔹
وزارت اوقاف اسلامی قدس اعلام کرد تا این لحظه بیش از ۲۳۰۰ شهرک‌نشین افراطی، همزمان با مناسبت ادعایی «سالروز ویرانی معبد»، به مسجد الاقصی تعرض کرده‌اند.
🔹
گروه‌های افراطی معبد هر ساله این مناسبت را به عنوان سنگ‌بنا و ایستگاهی اصلی در مسیر تشدید اقدامات علیه مسجدالاقصی قرار می‌دهند. این روزی است که این گروه‌ها تلاش می‌کنند به هر طریق ممکن حضور و قدرت خود را در میدان ثابت کنند و خواهان تغییرات گسترده در وضعیت موجود مسجد و شهر (قدس) شوند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452092" target="_blank">📅 12:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مرز استان‌های فارس و کهگیلویه لرزید
🔹
دقایقی پیش زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر در عمق ۱۰ کیلومتری، حوالی بابامنیر شهری از توابع بخش ماهورمیلاتی شهرستان ممسنی در استان فارس را لرزاند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/452091" target="_blank">📅 12:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8922578c34.mp4?token=Jgho7lMZBPEiyzg_MIG5pwmEs0_64XajWxqvzBQ67OHg2Hyz0FFiX5X8uLwtt7VxbSkCjw3pMYKkKxYxJKhVNjz1EMC9EuUj8ECh3hMYLW25wtFAauvan-jSLZfk7F1Dd3RbS0Cwbk7QV7xTGUx2ASjYFoLtL3BYv6gT_fc5Gs4pQ2ATF_vrbQ7dpar_ARwWa3CdL3uDn8i2FcE7gUTfjewybuZ29bQakodG107eLbahV17IQHOsVePo2gxRSUxzxTbuQ65MfmMmCh11wYWZ1MtvxU_MI2Ftg7-Y99fXyPYmcUOWfrGCj28vVvPXyYsdN5Kg1HIqW4zzzan9664PrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8922578c34.mp4?token=Jgho7lMZBPEiyzg_MIG5pwmEs0_64XajWxqvzBQ67OHg2Hyz0FFiX5X8uLwtt7VxbSkCjw3pMYKkKxYxJKhVNjz1EMC9EuUj8ECh3hMYLW25wtFAauvan-jSLZfk7F1Dd3RbS0Cwbk7QV7xTGUx2ASjYFoLtL3BYv6gT_fc5Gs4pQ2ATF_vrbQ7dpar_ARwWa3CdL3uDn8i2FcE7gUTfjewybuZ29bQakodG107eLbahV17IQHOsVePo2gxRSUxzxTbuQ65MfmMmCh11wYWZ1MtvxU_MI2Ftg7-Y99fXyPYmcUOWfrGCj28vVvPXyYsdN5Kg1HIqW4zzzan9664PrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر عراق به تهران رسید
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/452090" target="_blank">📅 11:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1328df24d9.mp4?token=U06jcYwCA8Exv5R_-E4prB0hlFzLLTWTAtiVNs0gIB-mY-kCjmeJMBiRf97ZiD2xT_43TwEtAdyo2qxtduJxry5a9DLabCVHk27kqvBJaOA0fo8GI-FHnythloLYabPulgjhMdTJE_SvO1Ay4qnlBlYc5-0QxjhaYJSL0a09wm6acuHh92DOnMu-yYyHSu6ntuYFXLoRTILQBa29UTi3apQNRxPSEfxU5qTdDNPrnTQAgYa6CJZ9cZUkxlLwIXmB2rd1apvrqJGUcgHIEDi7A0BskrgqfcQAmDVNhNWxdUFJQC6Mztcy1g9K3pj--dkVIa5VMINIw4wKlOrZB8S8VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1328df24d9.mp4?token=U06jcYwCA8Exv5R_-E4prB0hlFzLLTWTAtiVNs0gIB-mY-kCjmeJMBiRf97ZiD2xT_43TwEtAdyo2qxtduJxry5a9DLabCVHk27kqvBJaOA0fo8GI-FHnythloLYabPulgjhMdTJE_SvO1Ay4qnlBlYc5-0QxjhaYJSL0a09wm6acuHh92DOnMu-yYyHSu6ntuYFXLoRTILQBa29UTi3apQNRxPSEfxU5qTdDNPrnTQAgYa6CJZ9cZUkxlLwIXmB2rd1apvrqJGUcgHIEDi7A0BskrgqfcQAmDVNhNWxdUFJQC6Mztcy1g9K3pj--dkVIa5VMINIw4wKlOrZB8S8VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقایقی پیش صدای چند انفجار در کنارک شنیده شد
.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452089" target="_blank">📅 11:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uA40rg22dc-yB9qQ1esuXy2w8l_eqWhljx8ar0d9LgM1t3__ODHuTHsxqW9mZoPPrgnf-yTMI9KrP46Xhgynkw0nuTFSBkoZYT6-fFg060AwmlaafZdAQbOsTALb6DbQgpW9zyAPLZa2aVDei0iRu0iraG2dxMZM_Od0VrV3c0Fcjt-GkivxZPUzKANZW_rXMuytPFvdkCU2iYWpXxqiWzC8qr9a_koiTmLxpP-cK5OKtFJdDfkRCCwLv8aVPUD87MGIqiTCTgp0d1q1FFrZKzNKiKnzMJtOuRryotFGA6cInGCkEzWKZa4KZSL2jI4_2oA-qQuvQxvKrCC6FIh9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت نفت از ۹۷ دلار عبور کرد
.
@Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/452088" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452087">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4r3GF-MpY6hmtra6m3sRHJ5EiUTFgqQfCCBJV5dgykh9DCWeEJhRId56Pv9MLBrK15niqNSoGiQEvHdLj_flX6ccTPvzvG5rR9Wy-bL0sGRljgMFRKkXpAsqVeA9Nq_vHuYJtHeCm7tCC7_xlXEEKu4P4y7ZjPQ_xkSWS1KbW3Fi_sJs5GnrLIEu9LXOoPcgQGH-ASTVb1iAr30rIfvxoI3V0P-R2R3JU8ERzv5pE-gyZwyDiE_td3BFxA74jyif2fRtdu6h7uj3MW-JeGCXi28cixUzT1OLH1_6QLmprZa1T59ckuXu3ZtuukRcdi9t1vX4XBR5-7UNRmiWcQsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌گروهی امید‌های ایران با چین، امارات و کره‌شمالی
🔹
قرعه‌کشی مسابقات فوتبال مردان بازی‌های آسیایی ناگویا ۲۰۲۶ برگزار شد و تیم ملی امید ایران در گروه B با تیم‌های چین، امارات و کره‌شمالی هم‌گروه شد.
🔹
هدایت تیم ملی امید ایران برعهدۀ حسین عبدی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452087" target="_blank">📅 10:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxwAhAjvd6QzYCvTNGq8Dw7NOlHfe4CY8_6u3fKeRuH92BJNl-pgEiIGHtfraUdknFX4B9mB8ayl_SrPTGw7sWScHfSpTWILxi-vA5REHhC2tkMthzT58_JSEAYxgXfNb4bIpCzyn0UTxJRleG1NHwB7981MeAyg4kMuA3R3I_-hWsYgK8wxnNFLnTGZHYVW8060R0wiqbWZJW2QoNRp7YemPop6SFrRsYqhJpzsTSBZebHuJqtRqSRpHS0uVve8CQ1D-MIastn1Ap7HGemBTTDC_y1PxZawhh6pZ2IopNu2egKX1zzKleS6LA12j2rWt4lriyn1qf9nz8kvAz2i8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فردوسی‌پور را باز کنید
🔹
«من را در صداوسیما ناجوانمردانه کنار گذاشتند. از چه می‌ترسید که اجازه نمی‌دهید کار کنم؟ من بله‌قربان‌گو نمی‌شوم، حتی اگر بخواهید مرا بازداشت کنید.» این جملات را عادل فردوسی‌پور پس از بسته‌شدن وبگاه «فوتبال ۳۶۰» در برنامهٔ ویژهٔ…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452086" target="_blank">📅 10:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452079">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qcJNYHOhLRw8Mb-IcBfSvzccdDyNOz6_PMJSnCHM9ZxDK5th42lywGs1msIMFjNS_RxxOzCotzVO1XzmCYDpp3bsEZrbBGjrnLxxQ2YXywV9dXWvpRoWnujFyuk3siAsKve3EF05kVSTs1zI7bXvRtQYe7X3KUlnhv9Ohqrug74KHuei3_YtbllCyRGd9kc5o0-EiWRbbD3yDG5xRLSO_f1yuOJRIp4OVs13FSY6Y1jsIK0HCt0gJXTWscn5t47kNWDGrEWofEdB1rtDsegtWjCrRHzUn9IiMZeV7ByR5KAPZqphNaogC1qTbXSPr3WRB2CKiOGt8i0_4i8bi0u42w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMO4ChfE97vHh2WcZwx9ZW-GyEYSsVDeEV5vyUT68ON9sjJ1HscsCKG2B1VbY_LPiNMUd0f4DOzE1ECcMqGoHh2WaFe-ljy3ZTfW9C9a2mFaiV3RhlfqJYT8UXjM5h_egzsMaovY5RB7IskmA9amQsFlJCclGOKaIhalVDozLEu-mpnpemUEXn-HnKdlUl4Jrgz4CusfQ08UKxyb3xMtVEg4LWxfnmV85WZ5xY1uLqgt600qxA_w9jKKRcICtqXXx6EWxxF4bnXtQJK69K5aXOt6Fajd8VrKNTBNFgsxLYi3dK9BFIYgMNava1jD3RjIxcAUFbppavo-Br4ycqnzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBtyBBqB87JQ5r5IjFmL2_MUxBOeME3vIn1KPDCfFVu4nabCGp8iGtSg823WyGgyFPwDATC4M7FMN6v-oEENQ1mo2mcJjj4qAHKT18k-QwuIhM6CEEzdua1VGWPB8XLpJEvbRBO3JSUo3ZPQSNndB_l_rrgKDa1VVDVDUASBj7UGANmYvYtJh5hCTDib7UNtfymQWAhbwLXEFaaX0fU4ckW29rrwN6F8WFD_NVykR3G1uCnqmZjUINHIA5xDndJD3p-g64EZjR-5ib3_N2plRl4WpZixRnsMSa1pROZjaJfXnnbTRPzKFcXs2n1clCrzCSLzjrJwbN_FlU41Owk3EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QyFL1f6Ka3EYfF4dt53Wj_cqYAfc-UGaOt9dv8c6UgADqQk8R5n5qDdsPQOk7TJvYg8zj5MOGjU1trHxVOKucHjPi1uCjfwL3iz0MMz83ykkriJNYIY7B-2sJwTaFnMWqbDKF3fVUIf662dkYrRbHZTfVpTQYmGqEMPj8--DBWenstsRyM6ho6B4ozT4rmE_5b99vkGMUGqpOQn-Pr4YChbmc7P65hnMtZKWc47RIEtPCdzf_1QYfxnR-OCz5xzWwQ0UBeSvbe-1vmcQHdAeSvj0YyxNFVxjpDg3LKKMDTlcc9pYiYy3xGvElvtjdQwzjhsev1iGZ-k6tzhuleueow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmntHuANTfE7YEl9zfGCOIhIA6Tq56sPVV9c5KOJ8eNmSccQpNFSDedbbcdVFb-zQEafBTyZInpeBdytqzpewajWjFXk_QwZpYvoDU0P-Sn6iJd-F6SF9OvzmOvmNhZvSLZbwpHCfR1_qbyAWTzdHIKUIhBF1sF5_Agp3Tnh0ZE2qt_xUA1F1WA-teFTXYRrv9mrvl-PmvYkffJQq4y9ey6JgFaqErVBkNSvFnYr_uU-1rVjpd4yBttPD-V06wcATLBMFx46ZAyaSudxKo68JHNXlQWyNKHXfO3SclTt2vqcFCG10aY29tFW4Y8CmYEuYcc82vle7K_0Q5Z0Kus0Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WG7rgPk2pjTQhYP4sFKDPk_0gvsVJ1O0uTl07cQqxRKN3GTWzS73MmVPo_-2vDSJXjWaDSjwwz7gXwpA2OLQl7acIOv7boMy4g81ARQCOqh79OMlEhRAzjvUuIPlYc2Tvpz8zQb2wVBxp3DPWWJRnhnd46gf_AE5vU1VLG0_xHc2s8p9jwkTx_wQ-Foe5QBey1gpgIWnRCdUy0fwIG9NCYE3fPiq8lHiUd5TIAjVztKS01ya2hDaT_34zN4xLSRYJrguBhPgoM-seEVnI-gBG_f4ltV4JcQD6MiiDmEnBv_fL0TpzZDreJFsN6QjSNF21mVV-glyBjkOniTHRL_M_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMK6JmvAOu5qk1VsjtwUIaE2prokalBGkhnci91iXDLEcajVWQSotAtE4Gq1i35KXjwOKO3bk5I05IjnkNi80GJWobIiZxJXG38ysraScm7ua_5wMMWeXLC7O3Pd4Hw5M_a9Y6t3U39A3uZvCfymg1_agtIgbo9t33nIzeGRhtH5kXxZwiYTvisOTlDh3YDr2PuC0SzsnE32Y_ytaOTrAgaulan37yHgVLyHbJ1P_X6zoqRcWDaQTFtKPw2op1hzULJp473tpLB2YzlvxzuHRytcA3va8vcUXZ9aGC_h8iVMc8FDxVR8XI6qWFOdpltOAkdkxaGnyEOsWuO9kSFW0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⬇️
با حضور اکثریت سهامداران رقم خورد
✅
تصویب صورت‌های مالی سال ۱۴۰۴ بانک صادرات ایران در مجمع عمومی
🔹
مجمع عمومی عادی سالانه بانک صادرات ایران با حضور اکثریت سهامداران برگزار شد و صورت‌های مالی منتهی به پایان اسفندماه ۱۴۰۴ به اتفاق آرا به تصویب رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/452079" target="_blank">📅 10:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452078">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw5KQtrEuGL1afjPGrEu5-tXF_9mJK-KsKpJe2rRWfyPQLu63qSbODGjA4s_glPzKAfnIVaHmzgbjdz7bqvgU5t2ZCGMy0DV-C9azsS1g5YCifdFtHxIkNCfPYkpHKbAlsyRtXQQyQr0UwUYw6XgF8qeIWQvScqioBIlUAnKHqcDWzlDPuQtBGop26piIEJ4Bl-EpTSrTAJXTUdeS0W604_VcECD7V1Kt-BBA6YgR66hCs5a6De-aVcs16UeymZbpo7nGXLtAMm8--ARHFq5sdso6bNGK7Sn2Cv4tJAFzJo7uihZNvWPWsKSQ4yhFi0K4ATqoerEMFMSBFzt95WtPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
به مناسبت اربعین حسینی و ایام شهادت امام رضا (ع)، سدن پوش برگزار می‌کند:
طرح فردوس – نذر حجاب
✨
چادر حریر اسود با قیمت نذر (بهای تمام شده، بدون سود)
چاپ رایگان طرح‌های مفهومی روی تیشرت
✨
هر تیشرت با هر طرحی که دوست دارید، در محل چاپ می‌شود
محصولات ارائه‌شده در این رویداد:
▪️
چادر حریر اسود نذرحجاب
👕
تیشرت‌های مفهومی
🧕
انواع عبا (بزرگسال و نوجوان)
▪️
انواع شومیز مناسب اربعین
🧴
انواع محصولات ارگانیک و بهداشتی
📍
آدرس
: تهران، نازی‌آباد، خیابان بابایی، بعد از کوچه ترابی، پاساژ زمرد، طبقه همکف، پلاک ۱۴ و ۱۵
📅
تاریخ
: ۳۱ تیر تا ۲۲ مرداد
🕙
ساعت
: ۱۰ تا ۲۱
✅
ایران‌تن | واحد رویداد‌های سدن‌پوش
🆔
@irantan_roydad</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/452078" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452077">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452077" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452076">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3u2t6jFgfj8PJgbwZaffkrwZNtQKvUwYtLsHmOX7EjTXJCWbD89WPFyk9fC_yibjqpNPvyYLgVn-O32mTPf1ywr1g7E1t9YZUv8NvizRDQD35Zi6uEy2XBF2jV_XbtVd1w0uQrOtcoOXcm8S5IpswWnA7VUu-JdS9BjoLyVJogK4N8pd_YkzFfIAAM5-XFNw_qwftL3vtOYSdhEvjtBJJMGWsboeu1cN1eCDrUuWo_FQ2GGd33I9PaqFIapsx1AETcs7eYrFcXECF4CoAvUXqpk5g4xf0b-TbFtU9eWmdMeUFtqWK_fvQZaBJOetHQzE5xrAi8lMbmb1Z8RfdCOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد توکلی، عضو مجمع تشخیص مصلحت نظام درگذشت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452076" target="_blank">📅 10:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452075">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVj-tFTLrwxo3j4lOj5dXGcwK8mcV-VpQlq7zaa75GsmDRHZtjRtOoWREt1K1fW4Auh1tIFGnIvugnwqm04UzdKtRuVcD4o6aOno4r_UyUacoSJ_nWt0-IYqbOfbhzCPAotcW92K3TAXU8fKR1RjZF0peppcAJicIWy7HD5dwNdhpANcbxs9RqFnzx4JEWHjr36n9FIcBWsHzk0pcVFeNqk3AJxC0pxgFNV9QkuhfPHEYkXLHJu6xlSpYiwPEKYd0g5Q5Ur17XTTu3Ft4RCwp-L9I4CUsTOfjIGOrGpRmrnx-mshGAD7BKCRJJxdWZx_7U518ZEjU29qgOoler_vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سردار قاآنی: رژیم صهیونیستی باید بپذیرد که با وجود همۀ جنایت‌‌ها نتوانسته مقاومت را متوقف کند
🔹
پیام سردار قاآنی درپی انتخاب خلیل الحیه به‌عنوان رئیس دفتر سیاسی حماس: عرض تبریک انتخاب دکتر خلیل الحیه به عنوان رئیس دفتر سیاسی حماس، باید این انتخاب را به شخصیت‌های…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farsna/452075" target="_blank">📅 09:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452074">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEnneJjOL2SMIOdhEzmS4pm9IdvlQefFLuiHpfrMdkHAZX2bzgSZzngDIr9DQnTuU5XTRD7ni6NClJ9OcMJ0yWfiVcaToJkZP7Fx78L3tGamaBKvP-TEJFSl6kr1PQUH2em8yPOgS-psf2ITrwGBwiRhoBDy7K1LITPopzVX9VCTYwLPonGtdeelyPZ5uvY59zws4bOQrYHFkuh36lJFPF9qyqHqrMbHB_ZBXuVsuAzC4SY2gr31FHLClEh1G4y3Opf0lCb908EqLE8X5KJCbgWoiIdByAavrYxD6bcoeneuUVViC41WzZyCrBtG5Pf8tdziYvcqUXpQ-6X810FSYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخابرۀ کد اضطراری توسط آواکس در آسمان عربستان
🔹
یک فروند هواپیمای آواکس E-3 سنتری (سیستم هشدار و کنترل هوابرد) نیروی هوایی آمریکا پس از ساعت‌ها فعالیت بر فراز شرق عربستان و در نزدیکی قطر و بحرین، بامداد امروز کد اضطراری ۷۷۰۰ را مخابره کرد و مسیر خود را به‌سمت پایگاه شاهزاده سلطان در عربستان سعودی تغییر داد.
🔹
مخابرۀ کد اضطراری ۷۷۰۰ به معنای وجود یک وضعیت اضطراری و فوری است که نیاز به فرود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452074" target="_blank">📅 09:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452073">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTTd4_R9t12ZqGT4FMUV1ebVDBeY2M86koIvCcFD8te0Sy6dMLaUJ_S9hiXCzUBFauBT3WKon9bjqkY8QsfpSivoCbXluV6RZCOtqt6ZiqdyMv46xlYiIqP1QVptwBc2n5_t-Q6G4uQ-APh5_7yJ2Q5zbdp-ddDtZjHlo9eeHAwdVMC5_5gYCU8ytfMCsMdBZXtvToa-402y9qSK_zq_s20LYVpt-IAqLdXYQZAfs5Lh4TA3CtaRXZSBbgF7iKvKaOr8_TXCW64iei0O-Vg_6rBjZ_vQoggmKYzNJGk-VwCPf4Ui0IcXQrsqHbzHrExcBXeuaAeszefomVkGwMG3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازدید معاون اجرایی رئیس‌جمهور از پل B1
🔹
این پل که می‌توانست ۳۰ درصد از ترافیک تهران و کرج را کاهش دهد در جنگ رمضان مورد حملۀ دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452073" target="_blank">📅 09:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452072">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452072" target="_blank">📅 09:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452071">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خطر سیلاب و طغیان رودخانه‌ها در ۴ استان
🔹
سازمان مدیریت بحران کشور: با توجه فعالیت سامانۀ بارشی از امروز تا شنبه هشدار سطح نارنجی در سیستان‌وبلوچستان، هرمزگان، کرمان و فارس صادر شده.
🔹
احتمال وقوع سیلاب، طغیان رودخانه‌های فصلی، سقوط سنگ از ارتفاعات، شکستن درختان کهنسال و آسیب به محصولات کشاورزی وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/452071" target="_blank">📅 08:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452070">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حملۀ هوایی دشمن آمریکایی به شهرستان کیار
🔹
معاون امنیتی استاندار چهارمحال‌وبختیاری: بامداد امروز در پی حملۀ تجاوزکارانۀ دشمن آمریکایی، نقطه‌ای در شهرستان کیار هدف حملۀ هوایی قرار گرفت. حادثه خسارت جانی نداشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/452070" target="_blank">📅 08:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452069">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">احتمال صدای انفجارهای کنترل‌شده در دزفول
🔹
روابط‌عمومی فرمانداری شهرستان دزفول: از ساعت ۹ صبح تا ۱۱ امروز، انفجارات کنترل‌شدۀ ناشی از امحای مهمات توسط نیروهای مسلح در برخی از نقاط شهرستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/452069" target="_blank">📅 08:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452068">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24bffd69d7.mp4?token=gkUfFUqEe6kaBMmePgi703y4e5FJR2EnhneRgKboQ7fipz1BYzpYTI5fdmt9Mgy1Y6nggvTxkGSRb75tTdjQ3mAljobH894v-W3O7y-PnRYW7pPC3XtlqV0fCe9fYgLvvYv3-Yg1_yzzAKJt_Mvzie8so3Plh9zACPwCMYDbOejZq7zK6dkKMbejC_I4yT8E99YQbGxEAHdr-OMjtLTXEl71UaMoCr85PbsVcHjtS7ho-TB5p3onsrgUJGDN4nBXzCJdqtJDAc3wzvYrLp19VDbQABO1YCIDI8eNyhwYU60mrxl1H3oa3bc3evZ90UgfGAHrw-hBhypkZO0_0jGkZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24bffd69d7.mp4?token=gkUfFUqEe6kaBMmePgi703y4e5FJR2EnhneRgKboQ7fipz1BYzpYTI5fdmt9Mgy1Y6nggvTxkGSRb75tTdjQ3mAljobH894v-W3O7y-PnRYW7pPC3XtlqV0fCe9fYgLvvYv3-Yg1_yzzAKJt_Mvzie8so3Plh9zACPwCMYDbOejZq7zK6dkKMbejC_I4yT8E99YQbGxEAHdr-OMjtLTXEl71UaMoCr85PbsVcHjtS7ho-TB5p3onsrgUJGDN4nBXzCJdqtJDAc3wzvYrLp19VDbQABO1YCIDI8eNyhwYU60mrxl1H3oa3bc3evZ90UgfGAHrw-hBhypkZO0_0jGkZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش ۱۲۰ متری آبشار «کردیت» در دل زاگرس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/452068" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452067">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a0fec006.mp4?token=Ab8Vyxf4YUWDTlBFPbiq52Iw800YFQPXsCDsw2mIHGn_xFWT_YjXbjPmOoD0HNfD5ks6P7U-37BlKFwRv9PyZMW0bu4ShEvL8dmQWyMJySK1_78eqb6VaQRfggJJ3Vx-vha6wCIXIep8SgX2SvrG4D6sj1zpYn9zxp3su8S0ITUI2sP5I8ufoN5xljyJE7oDiGuBQWZk229rNYxi3TfKPxZ-pJs1WpFyG2FMbSQTL4nO2GwsxjLA6EKluuv09jj3QTHzFqKVR_zrPsXy3oinPhAO0Fh-kE56PucqxxNB59syk8eMr7mRDl3Hkjrq6syTFvH-ZPzXpQzYR7Ci2bCeBjEfU3tj3_s_XzHUzhHnGd5qLQdE-XFeo-KGIXXOcZ5Tk3-NJyMnD9QXJpVlqNIdshzoDUDjJzNOxWNYaFvkdzJR2r0tccX-EeYXxYknSDbre7izjILS1mu8a6UJlTExk74J4XQNvdP5YJKFIv0CstHZrTR3P88M0r97nY18N6sY1omCsYkJMb0XNNyiZIKhH_nA0Ao2iX98t0JmfKS2PEzvO1abZgxot7P-LKZplaoVEgZisJX6lIu8DxP5cqBvTP_PlZXhlF8UjkJym93lDYBlJ557PEheMozDV_5MnyWv3fGjtWWrH7_o6H3pnXfSjgJvyaOWK0eH1sRf6FgXgb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a0fec006.mp4?token=Ab8Vyxf4YUWDTlBFPbiq52Iw800YFQPXsCDsw2mIHGn_xFWT_YjXbjPmOoD0HNfD5ks6P7U-37BlKFwRv9PyZMW0bu4ShEvL8dmQWyMJySK1_78eqb6VaQRfggJJ3Vx-vha6wCIXIep8SgX2SvrG4D6sj1zpYn9zxp3su8S0ITUI2sP5I8ufoN5xljyJE7oDiGuBQWZk229rNYxi3TfKPxZ-pJs1WpFyG2FMbSQTL4nO2GwsxjLA6EKluuv09jj3QTHzFqKVR_zrPsXy3oinPhAO0Fh-kE56PucqxxNB59syk8eMr7mRDl3Hkjrq6syTFvH-ZPzXpQzYR7Ci2bCeBjEfU3tj3_s_XzHUzhHnGd5qLQdE-XFeo-KGIXXOcZ5Tk3-NJyMnD9QXJpVlqNIdshzoDUDjJzNOxWNYaFvkdzJR2r0tccX-EeYXxYknSDbre7izjILS1mu8a6UJlTExk74J4XQNvdP5YJKFIv0CstHZrTR3P88M0r97nY18N6sY1omCsYkJMb0XNNyiZIKhH_nA0Ao2iX98t0JmfKS2PEzvO1abZgxot7P-LKZplaoVEgZisJX6lIu8DxP5cqBvTP_PlZXhlF8UjkJym93lDYBlJ557PEheMozDV_5MnyWv3fGjtWWrH7_o6H3pnXfSjgJvyaOWK0eH1sRf6FgXgb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرکت زائران اربعین از جنوب عراق استان ذی‌قار شهر ناصریه به‌سمت کربلا
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/452067" target="_blank">📅 08:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5783ddb53.mp4?token=nudY5Z_02z_EZMcuDIzWrpH7FkIbpktT0lw6UGHjBjKOlZbaSGHlCPBjmaPNo4M2SQz-yfMyLUGYNiHMzrRapJEcKGTEPXOibtxuZy1w_7dSVgC5qtpSdnUxeirgRQRGzDthECSV81AOzsAzHfX2hYEERl_k9ByjmWQigHbCyMNMY1CMfh9KL0pSgoPOl0YG07P-q8Ds7mC_NT2aUKoskYORcfaXbdworUIiApMhV5FPvw311DQUxYD1Klpcj6WiBWAJ7JucQ8BuvPgh_Ft_gPqK_cm84-lP6k6MB_GVCRyxV8xwcFoTKmGet8AsuKe95Hv1xh0jrkzA4_LqYCl22A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5783ddb53.mp4?token=nudY5Z_02z_EZMcuDIzWrpH7FkIbpktT0lw6UGHjBjKOlZbaSGHlCPBjmaPNo4M2SQz-yfMyLUGYNiHMzrRapJEcKGTEPXOibtxuZy1w_7dSVgC5qtpSdnUxeirgRQRGzDthECSV81AOzsAzHfX2hYEERl_k9ByjmWQigHbCyMNMY1CMfh9KL0pSgoPOl0YG07P-q8Ds7mC_NT2aUKoskYORcfaXbdworUIiApMhV5FPvw311DQUxYD1Klpcj6WiBWAJ7JucQ8BuvPgh_Ft_gPqK_cm84-lP6k6MB_GVCRyxV8xwcFoTKmGet8AsuKe95Hv1xh0jrkzA4_LqYCl22A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سه پایگاه آمریکا در کویت هدف مجدد حملات پهپادی ارتش قرار گرفت
🔹
روابط‌عمومی ارتش: در پاسخ به ادامۀ گستاخی‌ها و تجاوزات دشمن خبیث به کشورمان، ارتش ایران  در مرحلۀ بیست‌وسوم عملیات صاعقه، ساعاتی قبل محل استقرار انبارهای مهمات و اقلام لجستیکی  ارتش کودک‌کش آمریکا در پایگاه الدوحه، مخازن سوخت در پایگاه علی‌السالم و انبار مهمات در اردوگاه عریفجان کویت را هدف حملات پرحجم پهپادهای انهدامی خود قرار داد.
🔹
ارتش ایران با تاکید بر عظمت و استواری ایران در مصاف با شقی‌ترین دشمن بشریت، تاکید کرد : لازمۀ حفظ این اقتدار، تقویت اتحاد و هم‌افزایی و پایبندی به شعار همۀ ایران برای ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/452066" target="_blank">📅 08:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
پیام مهم سپاه به مردم کویت: آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده نه ما
🔹
روابط عمومی سپاه پاسداران: مردم شریف و نجیب کویت؛ برادران رزمنده شما در سپاه پاسداران انقلاب اسلامی در تنبیه ارتش کودک کش آمریکا و دخالت های آن در تنگه هرمز، یک انبار بزرگ تجهیزات نظامی، یک سامانه پدآفندی پاتریوت و یک آشیانه پهپادهای MQ9 آمریکا در پایگاه هوایی علی السالم را مورد حمله پهپادی قرار داده و منهدم کردند.
🔹
برادران شما همچنین محل اسکان نیروهای آمریکایی، دو آشیانه بالگردها در پادگان العدیری را مورد تهاجم قرار داده و ضمن کشته و مجروح کردن تعدادی از نیروهای متجاوز، به چندین فروند بالگرد و پهپاد، خسارت سنگینی وارد آوردند.
🔹
رزمندگان همچنین در پاسخ به حملات آمریکا به دکل‌های مخابراتی در ایران، یک دکل مخابراتی را هدف قرار دادند.
🔹
گاهی گفته می‌شود ایران با حملات خود استقلال، تمامیت ارضی و سیادت کشورها را هتک کرده، درحالی که چنین قضاوتی کاملاً نادرست است. از نظر ما استقلال، تمامیت ارضی و سیادت دولت شما کاملاً محترم است.
🔹
پایگاه آمریکایی در کشورها چگونه جایی است؟، جایی که بدون کنترل مرزبانی شما آمریکایی‌ها و هر کسی که آنها بخواهند، گاهی زندانیانی از کشورهای دیگر به آنجا وارد میشوند و خارج میشوند، دژبان ارتش آمریکا انضباط آنجا را برقرار می کند نه دژبان ارتش شما، قاضی آمریکایی در مورد جنایاتی که آنجا رخ میدهد حکم می کند نه قاضی شما، قانون آمریکایی در آنجا حاکم است نه قانون شما، نه فقط نظامیان شما حتی وزیر دفاع شما بدون اجازه دژبان آمریکا حق ورود به آنجا را ندارد.
🔹
پس این آمریکاست که تمامیت ارضی و سیادت شما را هتک کرده است و نه ما. ما داریم به زمین هایی که توسط ارتش آمریکا اشغال شده حمله می کنیم. ارتشی که جز جنایت هیچ کاری بلد نیست.
🔹
در روز گذشته، مردم داغدار میناب باقی مانده قطعات اجساد فرزندان دانش آموز خودشان را که در جستجوی زیر آوارها کشف شده بود را، تشییع و به اجساد آنها در قبور ملحق کردند. آنها ۱۶۸ دانش آموز بودند که روز اول این جنگ در حمله ارتش کودک‌کش آمریکا به شهادت رسیدند و این جنایت ها ادامه دارد و بخشی از آن با استفاده از پایگاه های آمریکا در خاک کویت صورت می گیرد و این حق قانونی و شرعی و منطقی ماست که متجاوز به کشورمان و قاتل فرزندانمان را از هر جایی که حمله می‌کند هدف قرار دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/452064" target="_blank">📅 08:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UthR7Xrp6hPKM2HdWS-hmG-mOCPPsiD8jtLmnwBEhmhpkBy5Gg5H5dCnQW9-3N14SZ1xZUJhnI414bKqOe644DGoYNxEZhbilyZsi2XtqPTgEIC5fojavIsIF_4vQ3g9oM5XGXpGjgUQvQ5H4KqglX_sLQboVihr40msTnBQ41x6Jp4EIlkuNUvkFqkSHsQtHgJaiMw7vyzrVUdAs58HEVEEVPw9Qa9YsoUap5V7ts0bHvM3-IpKvD1jrm1VRAXWkk5kqO3d19wy4e_1MHzeO4TxnAGZCphPyNz11KZpLLCeH8S5Ev2UZwegY6S1sSZuWU_xe8miqP7BHp8oTEBz0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت در چندقدمی ۳ رقمی شدن
🔹
به‌دنبال تنش‌ها در تنگۀ هرمز و باب‌المندب، نفت خام برنت به بالاترین سطح شش هفتۀ اخیر خود یعنی بالای ۹۶ دلار در هر بشکه رسید.
🔹
همزمان ذخایر نفت آمریکا طبق آمار هفتۀ قبل به کمتر از ۳۱۱ میلیون بشکه رسید که کمترین میزان در نیم قرن گذشته است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452063" target="_blank">📅 07:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2NT5JyoLQY-DP1doWrAo1WC9hEI6MbGUiR5_s1xbAP55Qrb1wiOGmnDqUdGz1hXf_kexJsu_2tjcjOgfVptkcONVJYBOKnoZd8eS4xm7lzks9ITcqQ0MZVgPpBgU349F9TLINyH-hpKZ9x8Vvz_gGUtVZor3n1Yh9luxc7DxVJXZ2ZgHul_OAahXIYCeSBYwOx8zLYLLf3lYoKv6PV848OC9HC5q3D2v3EXNY-GavbAqbMhOhcR7V0hFTDw-V9cGxNinX2ckCYrDlrQfz3htbmoMNaUSjrAbIsyOaWQSUIhfZ4koIVL-R00S7BWQH_gSBS2-EGFNmUAeFTDUa8wTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنایع تا دوماه قطعی برق ندارند
🔹
با دستور رئیس‌جمهور و با هدف جلوگیری از توقف تولید و حفظ اشتغال، برق صنایع در مرداد و شهریور قطع نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452062" target="_blank">📅 07:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
حملۀ دشمن به شناورهای نجات دریایی در آبهای هرمزگان
🔹
اداره‌کل بنادر و دریانوردی هرمزگان: بامداد امروز دو فروند شناور جست‌وجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در اقدامی خصمانه از سوی دشمن آمریکایی-صهیونیستی مورد اصابت قرار گرفته و آسیب‌های جدی دیدند.
🔹
مأموریت این شناورها صرفاً امدادی و انسان‌دوستانه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452061" target="_blank">📅 06:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452060">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‌
🔴
یمن: ۲ نفت‌کش عربستان را هدف قرار دادیم
🔹
سخنگوی نیروهای مسلح یمن: با اجرای یک عملیات نظامی ویژه، ۲ نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را به‌دلیل نقض دستور ممنوعیت تردد کشتی‌های عربستان، هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farsna/452060" target="_blank">📅 06:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452059">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB9kPlHxNOBfUC0k1NTrzJRgtmiv-bvUxMVSiiXGLmc8SCvvdMxxBhcR2PrTCtuLThUfKVpHnNs78WGyVTLuNaxOetp3Ub1SjjdExzjW8M5yYCmL5qnV0i1GdVU4Nb2iuJLlTS1sJoaAUQGmCuLAIHHMwyl4UyhaxAC--yMSLbCEzrH7D_C5ImHtsCVKZwrmvQ_lDBeagcYBLPrdRCh8NGOAqZZqMQ6cSCXSYkqQmM58HwruxNsiWrJjWuFMlfmxvcUv2kUOsjzoVusLmcmawaP2nnmiW0yE30OjzRqcrEm4XpEEHj6roVMpCCcSddaj5lazk3PRpeOBR8dOI5NG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشت ۹ کشتی از باب‌المندب پس از محاصرۀ یمن
🔹
خبرگزاری فرانسه: بعد از اعلام محاصرۀ عربستان سعودی توسط یمن، ۹ کشتی مسیر عبوری خود از تنگۀ باب‌المندب را تغییر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/452059" target="_blank">📅 06:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452058">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
حملۀ دشمن به حوالی اسلام‌آباد غرب
🔴
فرماندار شهرستان اسلام آباد: حوالی ساعت ۳:۴۰ بامداد امروز، در اثر حمله نیروهای تروریست آمریکا دو انفجار در اطراف شهرستان اسلام‌آباد غرب رخ داد.
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/452058" target="_blank">📅 06:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452057">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‌
🔴
شهادت ۲ نفر در حمله به مرز شلمچه
🔹
معاون استانداری خوزستان: تاکنون ۲ نفر در حملۀ دشمن تروریستی آمریکا به مرز شلمچه به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/452057" target="_blank">📅 04:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452056">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۲ انفجار در بوشهر
🔹
دقایقی قبل مردم بوشهر صدای ۲ انفجار از حوالی بوشهر شنیدند.  @Farsna</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farsna/452056" target="_blank">📅 04:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452055">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌
🔴
شهادت ۲ نفر در حمله به مرز شلمچه
🔹
معاون استانداری خوزستان: تاکنون ۲ نفر در حملۀ دشمن تروریستی آمریکا به مرز شلمچه به شهادت رسیده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/452055" target="_blank">📅 04:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452054">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
حملۀ موشکی به اطراف شهر اندیمشک
🔹
معاون استاندار خوزستان: یک نقطه در اطراف شهر اندیمشک مورد حملۀ موشکی دشمن تروریستی آمریکا قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farsna/452054" target="_blank">📅 03:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452053">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌ معاون استاندار خوزستان: دقایقی پیش اطراف پایانۀ مسافربری در مرز شلمچه مورد هجوم موشک های دشمن تروریستی آمریکا قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/452053" target="_blank">📅 03:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452052">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
تکمیلی؛ رسانه‌های عراقی: آمریکا به محل استراحت پلیس ایران در گذرگاه مرزی شلمچه حمله کرده است.  @Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/452052" target="_blank">📅 03:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452051">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a87e9abd4.mp4?token=nSrNlaDuFBRxNO5VAM-vQHxU2_kjH1b2Rszw-ighzG3jyN8XM_3LnNwpj6imGTdJUzM8ELSmVKg07LNfZaeTFR5Le8ziKxToyq6_buDB_VTnjK0C5Jnnb-NtmY0W7xknbo2YVPEYnT660qYWEmK40nuJ3rsNTngz5th7ohQb0_hEfI70qG370l1c2JC9cyb0cKqHlgHsePMIgs87pzc3NTDNVc7S0Zjv4nbtA9GbcNUVD4LxdlHAebdDWC1NZXXnrF1PD_2NWEe9l1x8y8aaFjF8NAc10UtDXwPtYgg0PsmBV_YNTTCA-GWC3lxx1Nnbb9h3qyNkTOPGM6HU7liuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a87e9abd4.mp4?token=nSrNlaDuFBRxNO5VAM-vQHxU2_kjH1b2Rszw-ighzG3jyN8XM_3LnNwpj6imGTdJUzM8ELSmVKg07LNfZaeTFR5Le8ziKxToyq6_buDB_VTnjK0C5Jnnb-NtmY0W7xknbo2YVPEYnT660qYWEmK40nuJ3rsNTngz5th7ohQb0_hEfI70qG370l1c2JC9cyb0cKqHlgHsePMIgs87pzc3NTDNVc7S0Zjv4nbtA9GbcNUVD4LxdlHAebdDWC1NZXXnrF1PD_2NWEe9l1x8y8aaFjF8NAc10UtDXwPtYgg0PsmBV_YNTTCA-GWC3lxx1Nnbb9h3qyNkTOPGM6HU7liuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
«صابرین‌نیوز» با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/452051" target="_blank">📅 03:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452050">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=T6YIvYkK_4J5261A_8GRRIP_Lud9Ne96BRv3Em15qScb2BC_uGC0z5iT1IsnSfo5nSA7aGaO81pM-PuwctJIPtg8anpP9IqjRPUT2jR7AP9BpBKPQZeOAe7WUsk_7Dj239rYVVLzLHxSmhU3cc_xAJOom-oeWV1w2JYSBQl59TK-0mvpOP6UJeyTwnO8b90zCP_pSaAcqojqnexk3fMggJ6SveoZYdMMJawLjQs86ofzGQaXy0ue8HTq2BCeNIVsNA7MzdXjNjRS943DZCqKvl05gB2jpajL4hOWLAYdg4me1NgWN_hy9yJtx7Ak_fmrV2gwKn5Vbw7euHar7Us2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8cf6f105.mp4?token=T6YIvYkK_4J5261A_8GRRIP_Lud9Ne96BRv3Em15qScb2BC_uGC0z5iT1IsnSfo5nSA7aGaO81pM-PuwctJIPtg8anpP9IqjRPUT2jR7AP9BpBKPQZeOAe7WUsk_7Dj239rYVVLzLHxSmhU3cc_xAJOom-oeWV1w2JYSBQl59TK-0mvpOP6UJeyTwnO8b90zCP_pSaAcqojqnexk3fMggJ6SveoZYdMMJawLjQs86ofzGQaXy0ue8HTq2BCeNIVsNA7MzdXjNjRS943DZCqKvl05gB2jpajL4hOWLAYdg4me1NgWN_hy9yJtx7Ak_fmrV2gwKn5Vbw7euHar7Us2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اخبار اولیه از حمله آمریکا به گذرگاه مرزی «شلمچه»
🔹
«صابرین‌نیوز» با انتشار تصاویری گزارش داد که منطقه‌ای در نزدیکی گذرگاه شلمچه در مرز بین ایران و عراق، هدف حمله تروریستی آمریکا قرار گرفته است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farsna/452050" target="_blank">📅 03:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452049">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
سپاه: یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگۀ هرمز را داشت دچار آتش‌سوزی و دو کشتی دیگر با سرعت به عقب برگشتند
🔹
سه فروند کشتی نفتکش با تحریک و وسوسۀ ارتش کودک‌کش آمریکا قصد عبور از مسیر مین‌گذاری شدۀ جنوب تنگۀ هرمز را داشتند که…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452049" target="_blank">📅 03:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452048">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
سپاه: یک فروند از سه فروند کشتی متخلف که قصد عبور از مسیر ناایمن تنگۀ هرمز را داشت دچار آتش‌سوزی و دو کشتی دیگر با سرعت به عقب برگشتند
🔹
سه فروند کشتی نفتکش با تحریک و وسوسۀ ارتش کودک‌کش آمریکا قصد عبور از مسیر مین‌گذاری شدۀ جنوب تنگۀ هرمز را داشتند که پس از انفجار و آتش‌سوزی شدید در یکی از آنها، دو فروند دیگر با سرعت دور زده و به عقب برگشتند.
🔹
نیروی دریایی مقتدر سپاه تاکید می‌کند که تنگۀ هرمز در کنترل ماست و تا زمان ادامۀ شرارت‌های آمریکا در منطقه، کاملا مسدود است و هیچ نفتکشی وارد و خارج نخواهد شد و هر کشتی که فریب آمریکا را بخورد و قصد عبور بدون هماهنگی با جمهوری اسلامی ایران را داشته باشد به همین سرنوشت دچار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/452048" target="_blank">📅 03:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452047">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
اخبار اولیه حاکی از وقوع چندین انفجار در بندر عقبه اردن است.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/452047" target="_blank">📅 03:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452046">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
منابع عربی: صدای چند انفجار در کویت شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farsna/452046" target="_blank">📅 03:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452045">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqFyyAFX9sdlltz5ixVsPAWzr9rLKNwDFH3QV5dwmJa2absYZDQuhQ36ZEPrLRvXZ7aLRAO-oiEjOn2JPhpNZhDO9H73pMQE2OCi-2R0hkOV44BO1OFr9KjpclKsRdTZFPGj5U5QzAvpvBIrruzGrH5vzuHfxa8N2NxdyvQt4MpkKt4gcq6XJGpt3GncXwcd-l6uOA3eppIoIH7nf6sTaHQsSRxUBRJxkY-KgT3tPNx7d8CGAZC9XHM3rXhqsWUy8MtoohIFaliWyAIZhDrCU9MkgnFpf-ardQvPPAIi3oaqyOu3-hSKjFiUS1Ite1zZYZEe7b8b7sJSIkJ6zGPZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ آمریکا: تفاهم‌نامه با ایران دیگر اجرا نمی‌شود
🔹
مارکو روبیو: تفاهم‌نامه با ایران، باز شدن تنگه هرمز و کشتیرانی آزاد را تصریح کرده بود و قرار بود ایران بیانیه‌ای صادر کند. اما آن‌روز آن‌ها یک کشتی را هدف قرار داده و به آن حمله کردند.
🔹
آنچه اکنون اتفاق می‌افتد واضح است؛ کشتی‌ها سعی می‌کنند از تنگۀ هرمز عبور کنند اما توسط ایرانی‌ها مورد حمله قرار می‌گیرند.
🔹
توافق‌ها بر اساس رعایت قوانین هستند و ما با ایران تفاهمی داشتیم که سپس آنها آن را نقض کردند و دیگر لازم‌الاجرا نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/452045" target="_blank">📅 02:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452044">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/britaZeWyb782rGh0-GDotTgF2-Ni4zSkpkI7u5_iaSRw_Mz81l5dVoTwa4cGFMf4EHcX_B5NdVpzlmb5-klMIHtABlOtFKrEZiwBxRIczaIFUGrlaTBi4X4DbRdQpxSPfB4LvyOqBFthg_evZveWnSTuR9cH1OfateKTSTLeInjzHNsec5ve0OU672lisy3Y_E055gH5oMotHEhUalmtmxeMlgoOxiu48Qoer7C4pLvBXyHAJ07bkuKKe1HzLRhgZiPRGaw4kTNr1_ubMNef4Wsur9LZvzd3fhbDdML397v4NlGK1DHXJXlruXkMBRcoMOOTdC9nIPZG4BJGmZzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌
🔴
منابع عربی: مواضع نظامیان آمریکایی در کویت هدف حملۀ پهپادی قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/452044" target="_blank">📅 02:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452043">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تصویب بودجۀ میلیاردی برای تداوم جنگ آمریکا علیه ایران
🔹
مجلس نمایندگان آمریکا لایحۀ بودجه ۱۱۵۰ میلیارد دلاری پنتاگون که شامل بودجۀ اضافی برای تداوم جنگ تحمیلی علیه ایران است را تصویب کرد.
🔹
این لایحه شامل ۶۰ میلیارد دلار بودجۀ نظامی اضافی است که انتظار می‌رود بخش عمده‌ای از آن هزینه‌های مربوط به جنگ تحمیلی علیه ایران را پوشش دهد.
🔹
بر اساس گزارش‌ها، این لایحه اکنون باید به مجلس سنای آمریکا برود و در صورت تصویب، برای ابلاغ به رئیس‌جمهور تروریست این کشور ارسال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/452043" target="_blank">📅 02:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5iydWX1PrbWzhsJzQDgAu1HhAWzuoYFd7164VmutFRa80giQSW3TZppD7VQYspEY86XHSjE13LAB0Bjh8oXzmKs2VZYlulDX8xtotIuYmI4OeuA6JrjfDNR7v5qfPzD-q8DGMM-7ikFgkDB1s0hcZ2PG0mbVmhzWXWaOoHl4G8woIC35GWMRQ9sM4P_pa0GOOqdP5SIgQdIF4B5LVyHUiqf-e5ecNM31VeZfOY59Uv5KNqJnAXfxyCUCItYf0g0qtqn6OA_C_CJFgT4V5-kKveSYDsRj4-MWQLNActMnvwNbQEAoOpO5GEu165o2JrZcg9jCix9zFwJA5M6KkUmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5j1qU-7bqDb9JPqWyWLgnW9NhF7DfBqgwpVEZ50Jb01L3xp-hsp378JPgPdId-2g7bZfeD-98xXSlalnfcjhkbbDAtSGc45QVKInsd7X3ql5Zz1ReW9T6jUrICR09oNbe_MVelpQECx1jAU3zIWFaC-vCM-pIYkbAiDace8Gn2HFthJIzXp_s4dKzjOdMxjXZp7F_btkYDUfnHcWkjKLcrdwVxDDriMsOfuvu7cBVxAO4giad0rKI1tCVT-9hdJ6ZCjDDd5Ozry3KXaxxkEo6QhLzICpK-si43WyNxAz2VOyrIJW7-uXJpqWKpaGipg2g0KykMvkNwoufIeM9n37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgQfdiUmh2YhznvSqGrSaRwk5K7DCPyiiL3bQ7_9uRMt1iy_a5GwezF69zh4B_4VHEQ_TL9kK8SBdXoTFelBmF65VgJvHWgfOR0DgDpmeqSDGSuorLPDoU6OcaiJ8_6-VrnvpumwaZVGBLc4P5UfhrqIc4otd4a3k7xT8AgalbEK8rCS-5Q4opT0DwoeVtLp-qt0xEoqntNcKaFkcsbJJhx3jGrHlw7u5oF4UI3TGtNrgaUOj14gUUvMZOs_hGqquXWPWvQpx3qxAR8H4EacjGOYqIZKzqVI2pCGtowPFDv4rpyULjdYPGsTTOecz6DCbqbXLBj4GyV14gMfZXkVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLRBnDJmZPAwlhJ0teBT9fd1wfSneCQsC1txrFxfJZWG_r_RrG5sdqqZx61UGDdjUzsepOPS81QY3G93wn4k2t5iwJki0NW0ERqV5Yd8lGkaP_9xxlB0mVESBsSCAkM089s1rbnzEV4RnQF0SArUF2b4gBBM1Gb2L2dI6HwH_Hby2qrTStc3IMePAd6paM6lWoaiAjL8sumwaKTiksfP913ejNyA78wSJXTOAedQGc5mqu119qNrGFqVfPBts7TkDPef-LGs65_DAgt5oSK-ACVDgQOPAs4eKPtwhSpLAwgIqHJFqXxv8vd3k-6W0wy3KccLDEdXEdQB0JR74lz-cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/452039" target="_blank">📅 01:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwDplfWRy4kQs2JzS9MLulpgqyz7A4CTn7JVYqjOA4_DVYrpj9tDNUZQqal5Y_j_L5KeoASJTRUlyoqV6ho5pgbo85FXktaDqIRzJUtZLgSwp3jQbK_NxC0EGPFN4XwtFJ2BhFK9NJzaWAnzdMB6VodNcqsQ4poRX746A9T282r4_m6Wxk1dliLu0gbrBgLbwd0rKRX4fgDWtjOGm29HM9x1LDIhq4tCSctEgr7zSJAGninTIUDrp7uZUeFcuui6I2eP9M4BQ8ych_yLHjeRrNKqKblSGXtlN9WOlxqgJqU9DAF4z-RhjScrx5YPf6IaUnpR2xYtluIvAS4M-7kOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oh_A7zg7g9gUmGxppKw6Bz1GcEQauHGVl_qN72fWQDKcguboAV0q3lE7ywze6G2Gy8NZfw6_ZbOSEnxxfTXkc4ZFw-vD3bElAi6r0FMGK-yxDsWpMbc7hbuohw3WoTMpPiNBxi06tI_696LjoGj1e2RPNEvkN0ZzjKBfJR3fy8qAim6wqnXzYBFcRzkRJAeA_Dw2p1c9NxOLa_CYOdhS9LW-rNwjqbNyPx2SV4di5oPl4y1GGgwMQ8ID_jU_GPOZK-xUv5GlqBRTaEagUTol82-ih4uF09PmYaA7ZJFM99Nj-BdzG8HJgsYG0MH3X90dq6hQoKcOedS9jhB3OQ8bEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YArPzdRIp5aEtR0jaqZVTTohsJWeN8JB0x2zChlrJjHq6nEaAdShyuPQWdFbaQgJx_MjqdQA8OWzXOth5_uVqgpszSOeCeIsqUMJaj6KUEyUIgaJySuBdEBnkh1_lD3bROKYSqLFUandnvihmctzx1h0R4l47VJEKI_aXdL4UA_pW45naOpXOoCdqVvcFG_ivvivzDwakMikunGpG43l2zMwE25YA6oNFwnnO5Zbu_kVa41Zkjxu4tk3Il2NEWZ1rZhSS-fcyZqqMg9yPqr77yCofPPYhxL8XW1MzvlhdFgQfffYPYJ-8SYLJaK8Jdx-2b25axqK7_4qMT30vXXmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vc-WQ0yRzQ65x3UN2qoCrcD2UhQu6tIynBQWW9RvxmG6o1xtGWAAIUTRjCRoErbJ4kd5Lg7p8eTiXpr8RKJIzoAzUF0mW1kEbhy7Q9O8JAup-T_qydpEnutx0dbyqT4RYQ93lWVrRaLCELmTm4aguZ24KRQFiGPHGJrlRKpjampySU4JGd-hmqp32REBJxDB-qAe1iXU2yeYHqij_iSas6hgElS-fwPXJBeG4YNgny-1XsGOHdZBqAZgRjfikDLNhqDjaKO5TvB_oNIiJaXt3loOAjpDHWQrJCU3VV262-LGJbV4Ddp6nem6PQgwU8cNK9IX4uk8Y2lgUeDbTwDDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkJu2eOk8pdvaN_EyVPLSO-4wDznFSQ49F4SzgwTVfAW3uJBL5FThRwH12H-kdV1JUhV6R_pZU3eGKDHfHK-MjgKt7yV1pzPslmlzY1NsUG7mD670XUvbgwJd3KVR1xMn1my-wWAPidvTjZgx4Hq9zXXY_qbVn6bKFvIVX_kC-6jz-ul_2IAMhVGYNZAOrlJPwzg5X6JgFcmBjBF70t48OjLb7PsFsXNrgyVR7f8-xmZfC1xMnzuGx7qb_BExJdoFZOALFY16_cu-HbxPbRFb5WweAXJMIObFQI4wDc7vznb_yBjVCesWNBOXyzJwTXErKr1uEvYHzMRLCCTBDR2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kA1sEZBNuHEEDgM_NvKiPQPiX_pkWUDM-4gkHTDT4rHIEIYwsng7ukUi9tNLV7JoAFIa6lCVNgDcOAlyWfo33dzWJ9Bj2WInkClFWVzEZZMDmIXlAaa10gqMpGCw1dxCAMBFU0u8fwge_XKh1xy6yIgCRquBSK_OAsrVACCwO9JuS8Da0z-QEAxFhdkMPkx0KYYkm0aiDW9300CO23Bm5IopQbQrWpMJnkDKN5Ox9_EbelfLybv5k_LjthdlGbBqM0rTjvkGkAe-Nqho8z7VK9HRP9TpmsTY2emgNsOFuFhtIrs7zsKnyKhWMf4lwynbJ6XMUvxGOV-XBbkGLqps6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tv7UI2m6eIhMunB3jjPLnumLZemAb1To6ezNPyIpD9thCDn990fqH1E7pb1eQ4Szxw2Zap4E15ffGNFn-KRSi_FepRc3PMFZWLBlO4v1pjmIVJlNpw0LaoOteXJrIxnbLWqiwTBFAYZ_Q3UfoQNHmDuOyzV75AWk3KlpREEhyJ6G3y-Ynd27o2_JfsbNs7JysB9edmnQmy9bht-5ZvKwxjtj24rMN1eyOT34o-PzRRL1iZLQSrQIOY1VBPeAF3apKdYhYUoeEWIUmvpB3RD11bey5dUWzP3HV8zofpjDhZq0-uRWkd_yKb7D7Cq8f5fAHMJplFxExpWQu-9vKxHHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTElTFZKqtgTcEzC2GMNx0n311awIhYlh7x6LT-n7PlVHf6owB_amsKDf7EHeIh8DHh0-Gc72t5efEgTepQB786AiHvh-2qBvgBbIE6yIKWoquR6Cpd9NHkh5qOwR8SdlqLQ26i_V2QfAaTLwZpyeO0WOXNtTjC4C42V8RtMvjRdEc51ClrUuWiDxGuTN_O5ROfTajkoatXRipu5OZajWZ2RCR-cwFo-iYhv-IdJICHOn6z2F9GF-DWv3Fe48MUgkdc8s-tzyLHqhPVs0RQeRBRHNbimq7N11qBNEcPhwiw36NNCHaSF2r9v6dqmfKsW5D6_ozkO8iaCR11YWucI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyEd57zed-Prm-nU-i301pfQ9wIirnYOjjd_KJFq7QYjYqMYPBt1k2BerxX7qN355hSn35uGwVUjblhL48SA4H8gevpp7RvDVND4deY6cdjjSHjyBuqOJmxr8mhdSxsx3e4bN6vOm5_3tdeDhH9nFENDVTH5DVE1ARL7fHi7rggvzs28JFqDy9NHS6z854oCWAfjlZzsSy9i3DQZP5Lx4rVDdv16ZFj0upEVcW2HuKUoGNE-geP9QnsSWYHS-Clvm0LyqaS24uNHUhZS0fWX5gFCg5k2nf-eu8uvnP3_lCDeGYzyOyIBVCTLDJR-0IgArmqgF1QZcD4g5rqEi8Iy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xmc702q3iRpH8r-l-6NwaGlMUhseU18eL1SED8KIFUQVT-JLNDJfPPyiCcAivpfS-nS8mzMvPJj0CLTi0sIuD8pUtnpJW2iEtzBEHPqZaEUJDQUrn0SRg8kXWFnKOjL8wBU2FoTtMyifC-odeIBSAIQV4b05NZWABK246Lp6Wj3fyUTSyMYpW-Vf5RhZJbjjjxU8sgpKMFD0wIFTte7-etQkQGqG1nRCBaMz6GRjGc20jflSrV7yLkTdoGEUPMwivj05ONFuYYz-y04gnSF032r8IwQxrJfo1hdCRlXru1j50U88swMRkEk3e-KceSMyxfKIiFhqf4RdeetcXjs3bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452029" target="_blank">📅 01:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQDkve-oB7X9_Esn2SRwJ99m3FoGhcjzvY_sN-IV3DP_k4R6hDGW5IIZEKw2jdK_UjMffDkrCD0oSbdMWKC6vqLlEdiBeYb3m0q6FpZD9pKYcQzGB-sm3cbmixRiR90jow8IG4KPY7syKMQSP-lRBZBnKpm6qmtGrzWXxu1NdLMbasiXrHApWAOqim1VmTJqsVACPX5YHJE8R3XzQ1cqxSiut4pBoRt3wUdDy9-Z48uo5Lbmx3XDtpzbV5V3zEZjrLxAHeUwMA6HTY_z4LafUMppo1qPNDO9s_6DoGGmTrO9sIfeiPw7QEPTQLSYi_mxIYmvQLRq-lg-1YNWWh7hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با دستور ترامپ، و با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/452028" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452027">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=uiSx3kk5pc08rW-HhmN599PuRkXsY9DKBAZZymZd2Ap9o-3Z3ymhIL8vcflmxgA5IT-fO7b9E9ShWsmZL3oha66x5hhguI6jKm8l09RqgfBRGv945TZozWE5RjoZ-vGdvBeoR552YZv6hv6d1nSjVlj6tGGdWruT_p7w5apd8Y4mZGzSkQ_BfF_47Zcp1VbNx3RyOCL-Y9UrGPhgUopWmCabBhtwbX2qN2QCilYRntLZ70hOS7IrtbcHHD7wMu_N1lqe3wrhRL4ch1QKEJ7nq28wgdioFug7f90laF8Z0idVfAVUPymv9rOdigimm5qbp6wosH3Q-NMuk4Tw9b7bNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=uiSx3kk5pc08rW-HhmN599PuRkXsY9DKBAZZymZd2Ap9o-3Z3ymhIL8vcflmxgA5IT-fO7b9E9ShWsmZL3oha66x5hhguI6jKm8l09RqgfBRGv945TZozWE5RjoZ-vGdvBeoR552YZv6hv6d1nSjVlj6tGGdWruT_p7w5apd8Y4mZGzSkQ_BfF_47Zcp1VbNx3RyOCL-Y9UrGPhgUopWmCabBhtwbX2qN2QCilYRntLZ70hOS7IrtbcHHD7wMu_N1lqe3wrhRL4ch1QKEJ7nq28wgdioFug7f90laF8Z0idVfAVUPymv9rOdigimm5qbp6wosH3Q-NMuk4Tw9b7bNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادی که به‌یاد دانش‌آموزان شهید مینابی پرتاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farsna/452027" target="_blank">📅 01:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452026">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/452026" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452025">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/452025" target="_blank">📅 01:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452024">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpOBhQLKrZLpAhKAg4RqcsbwpBC1b94gKy-xyHrUUg4i8KItmzfUFBVYuANoajhA1rWFJkX3wcs6ouGhmd3uMcDtScZJyXRBp6GGuzcnX8OnmJtsjmtxCMz0ir_UkeQ3eRqAJ16iYqRa-tuM-Kq1nrj5enQ-PG6xVANxtP6b2gKeAB-NKpqwaetq71iiSEVc5dYMcHht_xIj9PjTlgp8x2A-KPw5nBys6HB81TZoGQdUJRg2BJNOwBiSgdm96ZZTIU8aOyKNqqJiEG2C28VHQsNpShKGAv5MUDLPZliXgkbvXTWabV4fugnoVCnJxX372-GBSAqcBKD68YM4SmvIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع نظامی: تنگه هرمز همچنان مسدود بوده و ادعای سنتکام بی‌اساس است
🔹
یک منبع آگاه نظامی بامداد امروز در گفت‌وگو با خبرگزاری فارس، ادعای اخیر سنتکام درباره وضعیت تنگه هرمز را به‌کلی بی‌اساس خواند و تأکید کرد که این آبراه استراتژیک همچنان مسدود است.
🔹
این منبع نظامی در واکنش به اظهارات «سازمان تروریستی سنتکام» که مدعی شده بود کنترل تنگه هرمز در اختیار ایران نیست، گفت: «تنگه هرمز تا زمانی که اقدامات خصمانه و تجاوزکارانه آمریکا ادامه دارد، مسدود خواهد ماند و باز نخواهد شد.»
🔹
این منبع نظامی همچنین خاطرنشان کرد که مرجعیت مدیریت تردد در این آبراه منحصراً در اختیار ایران است.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/452024" target="_blank">📅 01:14 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
