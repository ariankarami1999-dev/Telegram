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
<img src="https://cdn5.telesco.pe/file/nAxnj0MPRgiJyS_Q0rlaa6LWj3MhChcs6lXnGVpAEmHdJOzstvXqLiUiLOvqS7El4fQDMVoM1Dp5UNWHDBty9pgSsr97HdMA8ujPOMKyDLD_oV9Hgeb6U_a5AsaTLW9LLxoBqrRtLS7pJYehS0y5U5pUWGobqUzZ88m7UZfBLB-giJ3MiXB_LwOmnUJmXZ3AB33fCA211U_OPZ1HvJchWqrNUcWolECC2Cla68crBsU9XTGtZ6iWrikvIYZJKki53_kcaY6537kYnbyXtxMY5DYWDdJqz7dG6H2Fx5WFnXk1ZtbxrtGOAeS60mbYKqABlwA4Jq0oue7INwtGaEOVHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 491K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 11:06:32</div>
<hr>

<div class="tg-post" id="msg-102845">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT7EpETOVcSlkVlrmY65c11-pEld7VN6ijnj-tFfrApCu89NwgTL37u3XzkOfTrbDfXHSj1s6PfL3PiVD1aD2E-7dvPriHbrba8WCHtNAJ9wJNl64yAhwcakQbns0oZhJ0QA2ZHziviQnosSxi_HBM-iipWPi_YRR4CoGogwRVXKF2s12FUw8T-wcwYcsRGKd9jzstn3oKE30XR96upvNrJrXo6GdbT1km7dfZTS5LXOntbKgTX-vaflaPUvuGxK0xOsYEPqdYq1RMauBAEO0TaAYCwlq1D_rt0Og6oWaUBdWCwX58Y3FrW3nJRLeAiG81PQNBAG0PCrGCHRadqgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به مناسبت آغاز لیگ‌های اروپایی؛ مروری بر پرافتخارترین تیم‌های پنج کشور برتر مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 552 · <a href="https://t.me/Futball180TV/102845" target="_blank">📅 11:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102844">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5d8ba0a4.mp4?token=Mrf9SNJ4jhcqZ3ZUi-g3dFhctGrumBXZF2-FhRzmnbutorNbfs9bNewyuuIoU6azT9_TD-hvVjKFjgoMKnRgXtflng0N2SDHiufL_zYhZgqdUxDdaX-SvfO0e3nWHH7r_aSlRHZ-2JjYFH0fMC2sQAOuJpvIJzZxmPd65z_g6hZHKO7YkTxUHcgRBV72mLhs6wnN7oIAidxtpgB0XnhSoox5dmpdVtKueqYZMChQ3J2O4rAU0wJiBOsRd3FjbxsWJgBRt3zXXckJiW09yr9RLlctg5GXLFHoYGINweoh0KSqHc2YnfDQfRfpsLzD9jKM9zL_5ZBlwZ_y_8KGPrvthYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5d8ba0a4.mp4?token=Mrf9SNJ4jhcqZ3ZUi-g3dFhctGrumBXZF2-FhRzmnbutorNbfs9bNewyuuIoU6azT9_TD-hvVjKFjgoMKnRgXtflng0N2SDHiufL_zYhZgqdUxDdaX-SvfO0e3nWHH7r_aSlRHZ-2JjYFH0fMC2sQAOuJpvIJzZxmPd65z_g6hZHKO7YkTxUHcgRBV72mLhs6wnN7oIAidxtpgB0XnhSoox5dmpdVtKueqYZMChQ3J2O4rAU0wJiBOsRd3FjbxsWJgBRt3zXXckJiW09yr9RLlctg5GXLFHoYGINweoh0KSqHc2YnfDQfRfpsLzD9jKM9zL_5ZBlwZ_y_8KGPrvthYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این مصاحبه در تاریخ ایران رو دستش نمیاد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/Futball180TV/102844" target="_blank">📅 11:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102843">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKXFGXr0vRO_c6vk0WQjCHxm_0hX37wZaKr4AysCuodz1-azRggrQNISUmrik8ZhYhXIYbSzRYrGOQ8thpOG7D15iN5yBcCJo5FQ0ktqih3lPuY4g_aS451HuNk_91xQYMEji3gRV8BvcuiOSnCPgeaKL_dzF4xaocsRfLvqHgd9DV3N6w1saFNq7CG-heY-TaxlkehIt0sKouNBDEILxrOERBZQOdpa7WAawi8uNXk3DAittMCDUA1JRc83UoWac0Fy-4mUXh7h1df6Ryn2Vr7_LXQ8CB5LTlcffZKlMoGD2uQrfJhylfLETpB5StiR-Gz3czNADI2Ly6XTiq_o8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
👤
#غیررسمی
؛ قرارداد وینیسیوس جونیور با رئال‌مادرید تا سال 2031 تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.62K · <a href="https://t.me/Futball180TV/102843" target="_blank">📅 10:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102842">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6a1ff7af.mp4?token=DpfKJTaePITjLigulT6AVskr9PXxxbVA0uMfmNuhasYrJEp0iI251S39pjuObPQ6SQYyG-unsCPvsNLpE_1VzHzffvFHiW-blvMix8IZrNg7mOplmlemvjCvDR3lreAit0fPAJZ7w51iioBv12nm0BnSi7kA_hUJjmBcS9Kk8jPHk8DsGqx3yZfOijvmdvIUVlyEZq8z1IOH-sHxhlXeQa-a25EeOKrq8LiqQOCKYB8cxbG8q5MnOxl4KE03nRyjUDEAXK70grvG42mLNLuGi3CRmzf9-5b3ljKV-G7S6TCXA_35GqnJYflVJ1PBhp755zqaKcJ1ySPQd9GBTUZKGiBgBwIXIh4khzNnVG2wsrAF5sM-dY8ohx2FcSbIyhc0UVnlfWaDYE7eyQiGtc_UdrA_rBbP20Vtm3q52TD0KOa4mOjqqV3jxGcfd_sJB2z8nx4qcNL2j1p2gpqV2fjcjydfl89-d2jlCA8b3g166rm-PraCKDKHlAtpiViOsHDsch_4wgDI3oPrsbtmbpHZXnbuCJz6Icr6m6f05cf2hls8p1GCvXfTyjT5bq61e-nCAuFpGt_uhhOpEXy-CbqCofHaQG84W42e6F_LZnWYhN6cU6Z6YqB4FMgMZywjfzJIa4y6vvnrmSkDdvbIiVBANSRMzt4d-vQrjHRmSQe87lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6a1ff7af.mp4?token=DpfKJTaePITjLigulT6AVskr9PXxxbVA0uMfmNuhasYrJEp0iI251S39pjuObPQ6SQYyG-unsCPvsNLpE_1VzHzffvFHiW-blvMix8IZrNg7mOplmlemvjCvDR3lreAit0fPAJZ7w51iioBv12nm0BnSi7kA_hUJjmBcS9Kk8jPHk8DsGqx3yZfOijvmdvIUVlyEZq8z1IOH-sHxhlXeQa-a25EeOKrq8LiqQOCKYB8cxbG8q5MnOxl4KE03nRyjUDEAXK70grvG42mLNLuGi3CRmzf9-5b3ljKV-G7S6TCXA_35GqnJYflVJ1PBhp755zqaKcJ1ySPQd9GBTUZKGiBgBwIXIh4khzNnVG2wsrAF5sM-dY8ohx2FcSbIyhc0UVnlfWaDYE7eyQiGtc_UdrA_rBbP20Vtm3q52TD0KOa4mOjqqV3jxGcfd_sJB2z8nx4qcNL2j1p2gpqV2fjcjydfl89-d2jlCA8b3g166rm-PraCKDKHlAtpiViOsHDsch_4wgDI3oPrsbtmbpHZXnbuCJz6Icr6m6f05cf2hls8p1GCvXfTyjT5bq61e-nCAuFpGt_uhhOpEXy-CbqCofHaQG84W42e6F_LZnWYhN6cU6Z6YqB4FMgMZywjfzJIa4y6vvnrmSkDdvbIiVBANSRMzt4d-vQrjHRmSQe87lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇭🇺
فرانس‌پوشکاش اسطوره تاریخ فوتبال دنیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/102842" target="_blank">📅 10:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102841">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d755c0e765.mp4?token=KrmHWlyvjao63jIVozIF4mMNofYAPOct_AtY4P6NRCXC99M4gsNth1qTYn6zQtvb9HcLQzwzCdKPy5MvIhn-xmYVvbzqvBLeC0TMGzOGOgKBavSzN3RQTOOydyMjdU6TVJR-yMqgYfpSE10A49ekVESwR-xiAoNck_0xK-XUVcqyrrvkBKjdYXrJE7FdEzk581sNQtF0f1eNUGYSN7HfbreaY8zYOlRP97O-WxxTi47dYEfUFejftX9a40nOunyW7hBYBMzD6z-SBsF4afh4yECVx0I6XQC4D7225JuYK2mc3YrT8_4sgaoO10ILlDJl3cL6QriNsLpJWgeINfYWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d755c0e765.mp4?token=KrmHWlyvjao63jIVozIF4mMNofYAPOct_AtY4P6NRCXC99M4gsNth1qTYn6zQtvb9HcLQzwzCdKPy5MvIhn-xmYVvbzqvBLeC0TMGzOGOgKBavSzN3RQTOOydyMjdU6TVJR-yMqgYfpSE10A49ekVESwR-xiAoNck_0xK-XUVcqyrrvkBKjdYXrJE7FdEzk581sNQtF0f1eNUGYSN7HfbreaY8zYOlRP97O-WxxTi47dYEfUFejftX9a40nOunyW7hBYBMzD6z-SBsF4afh4yECVx0I6XQC4D7225JuYK2mc3YrT8_4sgaoO10ILlDJl3cL6QriNsLpJWgeINfYWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
🔥
⚽️
سوپرگل دیشب بتیس به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/102841" target="_blank">📅 10:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102840">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe450fda7.mp4?token=h3xtCqtQ4D_M9LwjRsMyE-AvM6b8nLnfZtUvdL35zAD4McSRLvytJim-QG-e_0t3sZmeiKDJnbLDc8PYZ-cNplgMBztkwSrfbMvmp8beZ6t3vGH94WvCoq7OlOrXHcI-0JtW6ojgwLDD8vA1-QYlC-Ewm0ZwYo02KoRmJsNU6VdR_ckGrcrTAbkxaTH-FQOAa30qjzB5VnTPsv7jAM9XtxNG6jGbwF9xdCwUiMfdmCsGTNE5BtpfiPSEznFBXhVx_Ee8iigkpABLX32HFA3TOWxyGQOa8EcohnFXcgbt95LaXeI-ZdKkGwlv-ZajdBSd7IUMy53HgmMe37Q29ox8gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe450fda7.mp4?token=h3xtCqtQ4D_M9LwjRsMyE-AvM6b8nLnfZtUvdL35zAD4McSRLvytJim-QG-e_0t3sZmeiKDJnbLDc8PYZ-cNplgMBztkwSrfbMvmp8beZ6t3vGH94WvCoq7OlOrXHcI-0JtW6ojgwLDD8vA1-QYlC-Ewm0ZwYo02KoRmJsNU6VdR_ckGrcrTAbkxaTH-FQOAa30qjzB5VnTPsv7jAM9XtxNG6jGbwF9xdCwUiMfdmCsGTNE5BtpfiPSEznFBXhVx_Ee8iigkpABLX32HFA3TOWxyGQOa8EcohnFXcgbt95LaXeI-ZdKkGwlv-ZajdBSd7IUMy53HgmMe37Q29ox8gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
۶ سال پیش، "انفجار بیروت" که یکی از قدرتمندترین انفجارهای غیرهسته‌ای مصنوعی در تاریخ محسوب می‌شود، اتفاق افتاد. این انفجار معادل حدود ۱.۱ کیلوتن تی‌ان‌تی بود و زلزله‌ای با قدرت ۳.۳ ریشتر ایجاد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/Futball180TV/102840" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102839">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP9TY2OY81nRZsJdU7QDhq119gc825tRAAGtK3b23vPDW9z8a1fckRslo_6i4D07Be5BGwKhS5-2wKLYupMXtu_fXu2pjDX4F9CGmxJ1BoaBrS2zze3rtwlNJdy3oV9TEAgQuX7GWg9cPYzXXexWA9nnXfqVoEKlStuTFKNP1TPA6FWgJkpzWdRroFAUvibNw5qB1-tOhRzZAqAEUrQGrDEaLe0grqnbtxtId59gamTPPDCGRnKC5v6_u4gtnLmR-rw5A3D2ADcYvaAv-kYCyQp9WHGYKxGVip1Fr9qFG9DjoV-ediEzzAO9ZjLbBoO_dodPPXfoiiUomhiq0FvQbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇫🇷
⚽️
#فوووووری
از اسپورت: فران‌تورس به پیشنهاد پاریس بله گفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/Futball180TV/102839" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102838">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/102838" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پنالتی
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/Futball180TV/102838" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102837">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=nqNs8y0637-m0W4YYJyr8e7gB0f3bSN5siztWBvwV5PmoHeAxYSdAA0jdaoBeoMl05aBbTcL_1Lz5GVf6eCxUgn7QsxcT3DJprNKVo4KBN04MWyHy7p6wNp5jUKDXJMayvMR00s6DGPv0Ka7goerf43sTGyG9cO0v9v6HffMyMc91CDi6fVpXjfip96p4P0F5rhSPoeoCK2hTN63hu-3vkpQgyrTEGxYVVh5Zd2EEtCI94VQEdmgb97bDaUUrwvJQZH14y-GiRX-SM1-tTTJkKu-Bz6Ss6R3TwXgquEI3S5lEhXoOMiXlY2NuNOJ_8NHvcJ9eO94-LctJOKMcemcDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=nqNs8y0637-m0W4YYJyr8e7gB0f3bSN5siztWBvwV5PmoHeAxYSdAA0jdaoBeoMl05aBbTcL_1Lz5GVf6eCxUgn7QsxcT3DJprNKVo4KBN04MWyHy7p6wNp5jUKDXJMayvMR00s6DGPv0Ka7goerf43sTGyG9cO0v9v6HffMyMc91CDi6fVpXjfip96p4P0F5rhSPoeoCK2hTN63hu-3vkpQgyrTEGxYVVh5Zd2EEtCI94VQEdmgb97bDaUUrwvJQZH14y-GiRX-SM1-tTTJkKu-Bz6Ss6R3TwXgquEI3S5lEhXoOMiXlY2NuNOJ_8NHvcJ9eO94-LctJOKMcemcDzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آقاآآ این بازی
#پنالتی
چقدر خفنه
⚽
🟢
بازی خیلی حرفه ای و‌
#پولساز
پنالتی فقط‌ پلتفرم جهانی و معتبر
#بت_اینجا
✊
همین الان ویدیو
#آموزش
پنالتی زدن ‌رو ببین و با شارژ اضافی
🤩
🤩
درصدی که سایت بهت میده.
💖
حتما ویدیو
#آموزش
رو ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r15
@betinjabet</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/102837" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac92224ed.mp4?token=tcAkSDwdwoBdz2APZhPp0EYASthhoBxPm_ayR0oRdVzjm7h02ScHH__2FPsCVxBlML3slf1Hmahnni8fYDFYbJzwzJFAQZfy5fS_49mRdPkGYmYPdcXSN5bBwrKfWvkREVP_Pu39e3vHNv4PinTYutyA-9DxW1-sc2sP38V4UmOjbBWSqE45yv2nJSQN6S6vCRV_J0ycCDB6uiAnTDzE1ixhRffBH6q1WUpNfP0IU9W6ozik0KXpREXQyiQgDoCsjiNMM43W33bvCFcopyjhm0TjPPvKcIWAMc42vSjDSqc1AF3UHJnqnipmqq0QYo8EvqV0x42NEIlY9_pCrDaEeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac92224ed.mp4?token=tcAkSDwdwoBdz2APZhPp0EYASthhoBxPm_ayR0oRdVzjm7h02ScHH__2FPsCVxBlML3slf1Hmahnni8fYDFYbJzwzJFAQZfy5fS_49mRdPkGYmYPdcXSN5bBwrKfWvkREVP_Pu39e3vHNv4PinTYutyA-9DxW1-sc2sP38V4UmOjbBWSqE45yv2nJSQN6S6vCRV_J0ycCDB6uiAnTDzE1ixhRffBH6q1WUpNfP0IU9W6ozik0KXpREXQyiQgDoCsjiNMM43W33bvCFcopyjhm0TjPPvKcIWAMc42vSjDSqc1AF3UHJnqnipmqq0QYo8EvqV0x42NEIlY9_pCrDaEeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
👀
🔥
مروری بر آسان‌ترین پاس‌گل تاریخ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/102836" target="_blank">📅 09:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz-Sqsu64lErmRGJJEblsckSBnlXqf3uUotE-IP0VpuiFUWC0OJI2F_ch3zxgIuSuIOyDzct5LYT-erbymNEZGUMosertrArPMgNsdghBedW2Uby62FEJGIb-rmRoGhxBaTroyT989wCeXGwbNZCKnhaXmFomklYmkexn9eoI5ad8yMZ_QuG4A3TWJZ0TpFUSnPa1G6o_JMlMTmUzQCjmljVPWJIt0h8CUySR1Di0ffEZwHU-l7EQeR1IuswE7hBja3FXlHOcH4IY3Zv3GCVexvMA2Wecr4w1P4VYAMVlinJ7mGpz1Ilqalm2n2t6JMzHCXXUgETvjY1hAge1AgnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
وینیسیوس و رئال مادرید برای تمدید قرارداد به توافق رسیدند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/102835" target="_blank">📅 09:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102833">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f753cf0933.mp4?token=rjXDe1-15FTanlxIGTlzFSoanSPk-C7p3hGrSxbgi6xk2RIvuiyigbttYUlLRS2pQ13tsKJLSC_9U0_ZvNyeGuJ5xRvJCQr7Mv6X4_2ShIUdheFmL7mZAQjekM1yjPN3gsnVRGHGuGI4tRdLYgIgeglRBn_a-wvB7vF6D2bCtC2U4MRSinL74Ftz3M-_PzgUH70oaPtTO-2ZHypH9IoGxabUmoPcgbzO9kqnGGWuNQxLa2p95jSeUDlPPqZ1spZ1EP70Zmg96GS6IzjXPZU61xjMELqcq_e0BEfie3LmsrU70FVZgDd7flWp_BUzSblmL439jeYRJVuvWIxcJqglDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f753cf0933.mp4?token=rjXDe1-15FTanlxIGTlzFSoanSPk-C7p3hGrSxbgi6xk2RIvuiyigbttYUlLRS2pQ13tsKJLSC_9U0_ZvNyeGuJ5xRvJCQr7Mv6X4_2ShIUdheFmL7mZAQjekM1yjPN3gsnVRGHGuGI4tRdLYgIgeglRBn_a-wvB7vF6D2bCtC2U4MRSinL74Ftz3M-_PzgUH70oaPtTO-2ZHypH9IoGxabUmoPcgbzO9kqnGGWuNQxLa2p95jSeUDlPPqZ1spZ1EP70Zmg96GS6IzjXPZU61xjMELqcq_e0BEfie3LmsrU70FVZgDd7flWp_BUzSblmL439jeYRJVuvWIxcJqglDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💝
مراحل‌صورتی‌شدن گاوی بعد از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/102833" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102832">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqzM3FCI3i6xP5UbAVohlP2XtoXMLj2WcXlTHk67zk2MZAmvqoX8Qh0_agd9lR5vpqzJxrfuVtf6gXxwxSGfArVQKY3yHrmfHWEqkGvAZZfXWHnMvC33LIsX6WC7_USVVEtGnp1E5kin3Wy_O6xCCF_pyqKa8QsPAQnxnaPeW-1Huv43832oMzloJ1jpWuzzBa0LDZFW8tQu_7bMDb-mOWFMe0NAEKG2wdjWNQ98WSbhsiiYQrGQLmobATmCEQSlCHSwv47UpZz2P5YM8dMv97on-qjx0YjrK2LuQUWKoUCb8mfuzd4CUQWdAM5qzpSqBL8wL9k3QtDYxQExtl7ttA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سرمربیان تیم‌های پریمیرلیگ در فصل‌جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/Futball180TV/102832" target="_blank">📅 09:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10e40774ac.mp4?token=uO7PinmAqu-fDEcn7nrSl97hQmwV1sY-Dkt5RbbPXMMwSSiJdUPJGUiago5pzycm94UrhM9kKZe4A4xWiPp64QB_mYSygeJ1m8Buqdbn_7Df_cERHVBK5UjExnq-j0RbgqRoDZoUcqSXJ-3jjuYmkKMCa5ZZEt1VvndvlUaikrkZeuZLZ258WfY-b6JIhjt9OEKHf08vfiwgzFpwN-mt2B882W1GM6oimOd2eAUCQl2Ra3peEthF0dNrF8NN0z4WEJJdYXldXPNEbcnazaYq4wR-No6Wc-wa9IpKnTHWTGj21p7FClU9AyajMTM8hM4rPO1EgQ-U98qRMVA8cn53wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10e40774ac.mp4?token=uO7PinmAqu-fDEcn7nrSl97hQmwV1sY-Dkt5RbbPXMMwSSiJdUPJGUiago5pzycm94UrhM9kKZe4A4xWiPp64QB_mYSygeJ1m8Buqdbn_7Df_cERHVBK5UjExnq-j0RbgqRoDZoUcqSXJ-3jjuYmkKMCa5ZZEt1VvndvlUaikrkZeuZLZ258WfY-b6JIhjt9OEKHf08vfiwgzFpwN-mt2B882W1GM6oimOd2eAUCQl2Ra3peEthF0dNrF8NN0z4WEJJdYXldXPNEbcnazaYq4wR-No6Wc-wa9IpKnTHWTGj21p7FClU9AyajMTM8hM4rPO1EgQ-U98qRMVA8cn53wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🚀
🔥
🔥
🔥
دبل اسطوره لیونل‌مسی در بازی بامداد امروز تیمش اینترمیامی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/102830" target="_blank">📅 08:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102829">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3b409b3d.mp4?token=YbDSsCc-bvar8vw7fk8EJD_XOIi7zS0tg0eyFHb6fVVZCnYgn_oy1d0rrTt8ASDIEP8x8kCku6xUWMv8LOowRvndKcY8c4Uf2i0iFRrctz_KL18bTxVMEb7ZlItUOOTpg6nN8Utm6v66e8mEeTIDzhsBWa5xnyYaikg0InCnxeHE9WkR0iwuAjo7mQaiJGJlRCcseD4tC-7D--mfFRTaj2-5OrA0KsNW_JG4_er22ZZwwJmYEfKFRL9iT3LGHLcaLZVpV84dzCuSXYX5r1qMYKOcPU05Jc0evsSsv9s7ARvc9hsuTyY_BTjzfMEdGiDw8S3F-Nj2qWe1CL_Vmw_2Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3b409b3d.mp4?token=YbDSsCc-bvar8vw7fk8EJD_XOIi7zS0tg0eyFHb6fVVZCnYgn_oy1d0rrTt8ASDIEP8x8kCku6xUWMv8LOowRvndKcY8c4Uf2i0iFRrctz_KL18bTxVMEb7ZlItUOOTpg6nN8Utm6v66e8mEeTIDzhsBWa5xnyYaikg0InCnxeHE9WkR0iwuAjo7mQaiJGJlRCcseD4tC-7D--mfFRTaj2-5OrA0KsNW_JG4_er22ZZwwJmYEfKFRL9iT3LGHLcaLZVpV84dzCuSXYX5r1qMYKOcPU05Jc0evsSsv9s7ARvc9hsuTyY_BTjzfMEdGiDw8S3F-Nj2qWe1CL_Vmw_2Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
رئال‌مادرید و وینیسیوس در آستانه تمدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102829" target="_blank">📅 03:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a87de8fd.mp4?token=v1pgdLhAxp4IkV2yLWX71bLVONJllgK3kv-RY30B3SFb1FEecLo7v3vvfXGOUYOQOxVaYd3Xww5kaA-x_MLAg123qWhvIrCW-hcO452Zk8qgraHak9ntoDW1x676Cz3JhVCBaTi697zm38ywyU1ZLw7kR4ZGqFzvTKE2KLobAz_TwiDdlETPq5pvM29i9VQbnFrrWCBrJjvlrmochM1oekKgMNvGhNe5kC8c9-yaV3YIbwx8F4VcnZbOlZTjjxvtsnnMX53OoI7QdkyZjjb_mjNp8nCKM-73tPQqcUIfqGf_VKCAPYLAS9OofCaPIZXy6hVH-4eKERQu52WTajTE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a87de8fd.mp4?token=v1pgdLhAxp4IkV2yLWX71bLVONJllgK3kv-RY30B3SFb1FEecLo7v3vvfXGOUYOQOxVaYd3Xww5kaA-x_MLAg123qWhvIrCW-hcO452Zk8qgraHak9ntoDW1x676Cz3JhVCBaTi697zm38ywyU1ZLw7kR4ZGqFzvTKE2KLobAz_TwiDdlETPq5pvM29i9VQbnFrrWCBrJjvlrmochM1oekKgMNvGhNe5kC8c9-yaV3YIbwx8F4VcnZbOlZTjjxvtsnnMX53OoI7QdkyZjjb_mjNp8nCKM-73tPQqcUIfqGf_VKCAPYLAS9OofCaPIZXy6hVH-4eKERQu52WTajTE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
حسن‌روحانی: «یک اقلیتی هستند که می‌گویند اگر این جنگ گسترش بیابد، امام زمان زودتر ظهور می‌کند و برای ظهور امام باید جنگ را تشدید کنیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102828" target="_blank">📅 02:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJwrgxg3oS5JT4MyXRuCiPmdBqOnjSZnkw5VN6yuMXSyA7KiSnUmkmThVWguOJciCNwL3X0JLWB1b0mROS6DpThTo-TBsLhKGwGnE5gI87NwOm9qCkryk-DFruiQZ_4qVXN5Nh21oEfGTjpi_thKF-Y0AFi2EcrD6K0tzRiV3pyJ871_hOCN6mLHbnuOsw4ABbDUaKDUC6X-f-rQoMO_lFQygmzx2fTBxtRRZ4bTYmxKa09fSn2_JCAYEagWByT3IQTYydt3ndk1N-ygzcpOanhCVgOD4i9OOLrv8MhvedpjqvYnw8LSNw9SSxtCNbm4oJieT7FxTpygE0R8b4x-WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
✅
🇦🇷
لیونل‌مسی در ترکیب اصلی بامداد امروز اینترمیامی برای بازی با سن‌لوئیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102827" target="_blank">📅 02:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102825">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9dWfjSZf9SIag-ZXuHWaFGhCD7PT9PGB-tXT5otNh4Tb4cVgEHWC9IFBR7WN3in7g2_CRrrZfe-_m74Cx655MP5TCw2Ugm3InWePyfFX1wza2jHhyziCjrI8CtoDjIj9rZSxSz1wtamW-hlqa5jNshH7VBINzCp9i6pECsFiKrE4aesyHbf9BqzVTGxkcKiOXxNmkNYGNBoq2o3ES5dJ2BLJdbwlJwXW0_qvJu-TYn1HOZIqpc-0J9-UuQ9Jf6NCfNZfX8uTUGEhGWESxQ61HntZ1vSEpihWDXVcWOariCFpoHPEwFdYxCf-e2sX1dqpn_gwaK7AdJcqiwq66D6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
اعلامیه‌رسمی انتقال دیومانده به رئال‌مادرید طی ساعات‌آینده منتشر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102825" target="_blank">📅 01:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102823">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec57fa35e5.mp4?token=ukh5rD2zb-hPMw_IsMMhy7HTMOOlo-3Jvm9zdztEeaCyVg0YGt-O_7GlpJtB2bcJsOCjfg3YKanJfmx0I80p3wj24djs_zGZtvrQG6wWrGy6pMkiIA3H8J9fe8mLxvTLRhYwinNphvlh9TnVCtMn0hcBMDr8fXGYDES7CbNVBl5ZpPylFrOycI4idmPLG6NI1cBSwt0WNl_7rQMAGtnv2tkB7f2yDnuyj9vOEOBhiLfDXpqIonJ4WJXbTrwCc6M9Iax4CMKXI9tTscMu8-N-NovN_vpDr-tFiqmiVfNfvLqsizrHoh1EesaujPdStkdsmKtQhNZnwH-Et5Ht5IL7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec57fa35e5.mp4?token=ukh5rD2zb-hPMw_IsMMhy7HTMOOlo-3Jvm9zdztEeaCyVg0YGt-O_7GlpJtB2bcJsOCjfg3YKanJfmx0I80p3wj24djs_zGZtvrQG6wWrGy6pMkiIA3H8J9fe8mLxvTLRhYwinNphvlh9TnVCtMn0hcBMDr8fXGYDES7CbNVBl5ZpPylFrOycI4idmPLG6NI1cBSwt0WNl_7rQMAGtnv2tkB7f2yDnuyj9vOEOBhiLfDXpqIonJ4WJXbTrwCc6M9Iax4CMKXI9tTscMu8-N-NovN_vpDr-tFiqmiVfNfvLqsizrHoh1EesaujPdStkdsmKtQhNZnwH-Et5Ht5IL7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
‼️
خرازی دبیرکل حزب‌الله ایران و برادرزن مسعود خامنه‌ای:
ما باید از جمهوری اسلامی گذر کنیم و به حکومت اسلامی برسیم. علت اینکه این الدنگ (پزشکیان) رئیس جمهور شده و بی‌حجابی کشور رو گرفته اینه که هنوز از جمهوری اسلامی گذر نکردیم! خدا لعنت کنه شورای نگهبان رو که این آشغال رو توی پاچه ملت کرد. چهل ساله که با آقا مجتبی رفیقم و خیلی تندتر از پدرشه اما یار نداره. باید به نیت حضرت فاطمه از هر شهر 530 نفر جمع کنیم به تهران بریم و کار دولت پزشکیان رو تمام کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102823" target="_blank">📅 01:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102822">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb48689a3.mp4?token=YKfLfFseumFZvFe76DcgGoNBt_o5GpEsvlYK4L49MHBPIM6Sh_TLd4jhno17iXs1wCNKP_YxntKSr0rN1Vk_xiXAJAnUY-tPeOEpHpk07RyRYfMK1RV8NhLr-dK1ZgT2rCnHRbiCuIGXFLb8alCwtVUhlSTYtW1auiB7j6CFR7LQ2hW_HshNB82ddDaMSJzWsTrsX0Lb1O-bQlDP9KsymNfNNfyyaex6meMkpiDQQQjwI0R8sGoVWPWpFuNsH0Tna5zivKzsthiYv5WItJQz2y6iKRtdSniXfAP6g0QiSHC-4fRvI5s3Qxyv-xTTdiOft-1MhGvA2gywoMz_YbfqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb48689a3.mp4?token=YKfLfFseumFZvFe76DcgGoNBt_o5GpEsvlYK4L49MHBPIM6Sh_TLd4jhno17iXs1wCNKP_YxntKSr0rN1Vk_xiXAJAnUY-tPeOEpHpk07RyRYfMK1RV8NhLr-dK1ZgT2rCnHRbiCuIGXFLb8alCwtVUhlSTYtW1auiB7j6CFR7LQ2hW_HshNB82ddDaMSJzWsTrsX0Lb1O-bQlDP9KsymNfNNfyyaex6meMkpiDQQQjwI0R8sGoVWPWpFuNsH0Tna5zivKzsthiYv5WItJQz2y6iKRtdSniXfAP6g0QiSHC-4fRvI5s3Qxyv-xTTdiOft-1MhGvA2gywoMz_YbfqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
تفریحات علیرضا فغانی در ایام‌تابستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102822" target="_blank">📅 01:05 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102821">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmIALxeJtyMquKpXEIAs8sFpXHd7D5U48bZv0j2PrWuRSQrLYouuc4RTfBRPk7AzA6f1eiHV70Gh7nuaiIUxG4HTVjD60gUCu-3gHB5YKwnslcPYBPRMR1j6B7KtINN_8tLieSW8hb90WHdeu-uPPyKmBOWML2huRn8mJBcXZ5U6RYvL2vN0skZg4qPft08ZmheZ38nYtLreEsuQJyyygzoMZ6F_RITzQP70US0dcccvHpPdYVXqCKwRrBohIp5CXisvlcLZlfHSo23BoLFbPMgwRv-VlWf3HkfbTLcAfTxyfa1hzzJFf53NYETPhUMOQuqSAzfbZhpi7OY8SDJnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پایان‌بازی‌دوستانه؛
🇪🇸
مایورکا
😆
-
😏
PSG
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102821" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102820">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgdmFBCjz_6N-b6qCQM8-UqGW8oE7EYET11ODVSDd0Abtoz3a1e4vnvCFiisW-fww4XjuSTQUMLTecGgkuRQEeT3dfO98_rogNhSsu96vDcaIlPnMjN9oId9PAJl-y99uL9CXYix0M3IMwiKPkwPdM6Rszz1Ib6lovm8w7L61VwqCOvUGK4DmhHr1Ke813lCIPKIgcPGJ9XANkM7i5aDhwpsm4DQ0LB7omvm0mUBLnFmQYEDvdiqYhRVZnZBwH1LinJ6wyaXtDf7VmIHrrlCWXf5muS1eeqwLDlirdwher1OeJwmzpXg7G8YL2H2Kt3qC1ObrCMrlGJZAVbx8wsJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🗞
اصلانی‌با عقد قراردادی راهی لایپزیگ شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102820" target="_blank">📅 00:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102819">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2pPkWVvNjOPiyIpDyCLRAYcCkDGoY625ABdMUBK_eFNBxYVRHMpHaZ6xhFXyxCxiJOQzJgnBNCUNByw4KuLCOUs-o6MGWyXoiBpgKoV_NYoqT8dOZbkNrP_A7yli0YUlS0YbOw-4vsla64agmniZT9ki2e8jibAhh9CH98KHnBYaptLDdMNQTS3_KSl4f6MSJkTRagQWEKNYFJdPX8G7-Z6MycEqwFHMUle7qhvGMYmwdMauEQrbCzYPiRyDMc4bSil1KwCm6JjFncJhBZXGWdugOEedhiumdE-KsNCGq-VQvzN1W_UVu0c3OxmNww8PyeXqujYea59EW86kUdJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پایان‌بازی دوستانه؛
⚽️
آرسنال
😃
-
😆
بتیس
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102819" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102818">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/102818" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102818" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102817">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=s1D6oSOlUpYppRUxOM_KvKIP_yn20-J_O3pOP9QJZcxWl7_LxwoCWiRZU-NS2WqWkpSldUXN5mOt7TinLOqbKDXoW91X4d0mQ8_PGoOL-s3jp5etVmS_J7xujsf5Tp2FweVZ1PPQb_0GI_iyZPN71ln_X410jNqCLOiyNwpY4edpPXSZfBXoMaZRMw4cj5XOUD3e6hfFuhCv_l1txw38QtMhUmkEasWx6ztBilzym0lh78-XOXMQM0uinUrmO2daLWyA2HYmjsyVxaFutD2xPeO-ZX2Cm0jNJEvb_b7moDgKzhFcOnZKtyqmire7Bf4xeP7QnTpQRM0BTR1FPcb9Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=s1D6oSOlUpYppRUxOM_KvKIP_yn20-J_O3pOP9QJZcxWl7_LxwoCWiRZU-NS2WqWkpSldUXN5mOt7TinLOqbKDXoW91X4d0mQ8_PGoOL-s3jp5etVmS_J7xujsf5Tp2FweVZ1PPQb_0GI_iyZPN71ln_X410jNqCLOiyNwpY4edpPXSZfBXoMaZRMw4cj5XOUD3e6hfFuhCv_l1txw38QtMhUmkEasWx6ztBilzym0lh78-XOXMQM0uinUrmO2daLWyA2HYmjsyVxaFutD2xPeO-ZX2Cm0jNJEvb_b7moDgKzhFcOnZKtyqmire7Bf4xeP7QnTpQRM0BTR1FPcb9Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a14
@betinjabet</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102817" target="_blank">📅 00:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102816">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaeDplIUDMqOMnzm_FUdpFUMIswdkX5HPqkDSQyGREM4dB4Cw1C8Mf5Vc43WzeTa5CeH6k8gMqNP_W4l82D00f9bvhcPX-QyK20IxAk534wOxUPAmxk4K03ulU1Fv15rb-vK4bCx2vboWooA0ls60iNfVUmzKTou4fUtsg4EYTYA2m37gHa7rOy3o2RQ99nm1-lqA62OJ36Ichyehl3jnRAZI54g_nJYV4ZPPUtITGaV4JOt3dgSxB5YxMvLD4lBOWYmF9KhyWIrYWTzGNj8CSgemORMwW_LiFHgWCXQoLnO192UJrlkal9Qpgu2egrzhFyDopeth30BUIteV-qe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💭
کامنت یه کاربر زیر پست تلگرام:
من آدرس مخفیگاه پاول دروف رو می‌خوام.
‼️
📱
اکانت رسمی تلگرام:
اونو که نمی‌دونم ولی منو می‌تونی تو خونه مامانت پیدا کنی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102816" target="_blank">📅 00:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102815">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56fd322bcb.mp4?token=Bs_CaLGRG-ofz1lX_tBrEV9Tb05Z_ma3z5WilU94F3fywnNg4iO5Km0Er6iHp1WymsRxaBClLrS2Lrr---1xekWitWnzoJFa-VKG4qxp3qAG-PPUS4JKfFwq71GjcjSzaqAPZQgJXaupM4exWFT7XrXjeA3hW59y2-Z-r-w6EPAzYNn7-BNf5SacVQ4i9ctGmGAs9mRQdQQVCQIFBOQ5ezyh_cow925mxvEOnymY3uuW-Cth342asYbEzIpuD634zmU1wHWSvM8RC7tYxSZ2s6dsFOhGQmj8E7YHziejbnV1_G6maThUEI-32_RS2UGt2dQIg8gUoSvlLKcVGPEFYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56fd322bcb.mp4?token=Bs_CaLGRG-ofz1lX_tBrEV9Tb05Z_ma3z5WilU94F3fywnNg4iO5Km0Er6iHp1WymsRxaBClLrS2Lrr---1xekWitWnzoJFa-VKG4qxp3qAG-PPUS4JKfFwq71GjcjSzaqAPZQgJXaupM4exWFT7XrXjeA3hW59y2-Z-r-w6EPAzYNn7-BNf5SacVQ4i9ctGmGAs9mRQdQQVCQIFBOQ5ezyh_cow925mxvEOnymY3uuW-Cth342asYbEzIpuD634zmU1wHWSvM8RC7tYxSZ2s6dsFOhGQmj8E7YHziejbnV1_G6maThUEI-32_RS2UGt2dQIg8gUoSvlLKcVGPEFYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا مدیرعامل باشگاه استقلال: از عملکردم در مدت اخیر رضایت ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102815" target="_blank">📅 00:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102814">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP40D9F30psN-Tju7rV8FUsCor5ijGGcPAwyXsHpPr8GOvbedQfQlHDNgvCTXmNlFiDdZvY28oNzOaS-Mlw7q5xDyo-c8ArZ38BcOWLl-O4T3W5egn1Np8iUJy3v9pZow8rOApBOnN1ltDBHtBg9sG_f_gPys759f37j3enpyurNLSRjkF5Ya84jUEX6QfA-9M8ov7rVh4oMODbT8mml8o014cMXHMHkQ2Fe5n_MIMLJQ65v2yxSA_csvPp5CcUgbwewwFK_gYGU1OcmYR4qp8Zo6SAy0DnETJ3Y0ZyLvCcDPoKBbRzTlajUFF3UXZIVkdpCKwXv73DU9SllutOl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد صلاح:
من تو زندگیم تاحالا همچین چیزی رو ندیده بودم، 25 هزار نفر فقط برای خوش‌آمدگویی به من اینجا حاضر شده بودن، این باور نکردنیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102814" target="_blank">📅 00:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102813">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180 #فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102813" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102812">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7IA22RfNJOdhtpFD2zNaO8eeS8dUSaWzZxwGB2IsEcrk0WAVocj88pdybalg5RNNqNaygjG-Yg9qEWYrtQ47bUfj4nZumJmJKB9s5f74RUp2l4UoghrnihU82xXYW0lyCIxuUz9fuaik9EzkfQdCfTdUiASA391nGDnpkMYWo9pSVikcFRi59ogOiIUEPCwG850gJRBznwtPtpLRJNlZhI8g6ZSGhPGF1fDLhd_0hOJw-i7q753BCJh3u4TVin0ck9YUz4Ms1PLVdRtFNjHruIYVytpvAwNaA1Qpvc5CBWzbKXzfMHXxg4NpJ7w_gcRECoLTR2fDRTzKrovcQE86A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه تلاش و پشتکار:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102812" target="_blank">📅 23:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102811">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv_EMleGhaJ2Zv9h_eVbxIYkd8XjiZaNp2BWzkpbGJvHWWy4RkpF7BKI5rbe31EMNj2m91KHXMKEk6kC8I1GhqWuD1WTrPW6Guoj-VqRWlcQwzQjvPJ6mp7PsAmJ224VmN6A6-2RsW7nwM4SD29TKHMgWaoJHgyPehoLBmEg6S_wb7-66kPmERnhDma15eqL3l7Y25oWk73zDTtsgP4P35X4nYx8yp3306vbwUm0C00Em8VjD0XOIjIT6un_ISS8YAjIcAPQ2AsYXyKWbjnd_pJBBX9fjXfvpObXv7NSs8dQTo_gXAZRPHiOjl9SZ2IeGJMtZqh43-OgJb5L7sAXAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد صلاح:
من سخت تلاش میکنم تا در لیگ و در اروپا به موفقیت برسیم، چون من تو هر تیمی که بازی کردم، موفق بودم و همیشه یک بازیکن فوق العاده بودم، و این چیزیه که باید اینجا انجام بدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102811" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102810">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/102810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102810" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102807">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBjFr2_xlhuzRNGSgSgr3Zrw1PDrC_VXjRQTDUUzgdPmeWxvpqIDqhV87ghuWaLGAYzGeGl9lh665cdBZHvf4OVbaVJJui1R56gSY19UPCZNtvwqJVil2Yy_91RjrytO7vPSnicUppHqT6nn-Q6JMaWM8ntLr5_AoJYIgWbG2vcY9I0mNw_HPqu317tKYrCCUaDBROwGPCBfmVhIRZ71lqGL6er3UAfG4wgYHW04o9o9xLwem2Ig9Cap3z4L937ASukOKJbfT0IF9rDkYR8tBDkt4bF2OwGFHhHffbltbrThjt_rjmr_TtnuYjPdnIL0JkL4nHFPBgdJc6byYemE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyqG0Ck4kebPut_1y8BvvxNZHucv93uJZS-Tlm1vO1b5UBmnHHnE6o_pXORQnabEYBKTnDtYtu3Qm4GxNrZskAbcLDeWjqC9nDL3D5xj1xzEELJ9XRqpwMvsxUlnnoZvCCSHR70tgyg5Xn8aKtEmAAXQ2McXThHQWCPd9JdikAbjIEBsCt7Tr6De0QCuxP1fXjOuXGY3flyQ5Wlr247-KlGpsFrgGSq8oja0764uNSeMKV57v0eJyHeCgNv_WDKQR6yLn6TE-Jhygp6gYuMhLLu0vH1JXQie6yoLTMEOi4qoYGqfNV_ebpyc6jkzfOQWIfSN02agTp_JSoRckOXRbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1r5df2mFjtcu21w5na4Pail4dL-zjaAMPn7-1KMgMLpJ_-ocju-WGhhB6rznZRA6cErFTrWrHoNKOuAugbQ7jbDcI75QhejzOWmFUM8wpAhWy1CbvKUv711siHjDRM3dv9igbmSYif66sRXTD2mY_3BxYAweP1Bbql3jy92FxEOY-B5CdWKDwNvBevHemIebN1NKR7AhR9i5Mq27NSGsF9ZIV5-MJgZYBcMpZGbBiXAPzjMcDv8sTbjLQNbohjL0l1Il8j-462pfx8AZ_AS5fS2DH5iQqclnr6ZTI50PJKtdZznN0dsHaGIZADKG9OyJ95QrzKTuWdJPkamnudq9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استقبال برگ ریزون هوادارای ترابزون از صلاح رو ببیند و کیف کنید.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102807" target="_blank">📅 22:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102806">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8Bhwn9TnJAekqhs3KIyD8P1DNe7X22UcQDbgtC-JiwsaMsXADYzDA9rUwqy3VlT1MrPGbtULr1Wr_YHW4LyUq-ZRiBcaxv1_GGadQI9-C5kQzMPMNCfWUcrHsuThPMwr4OqyoShxczAn4cU9H3PXsrhxXHJXV2t87MXiv47cdxIvKgL4WyhwLLy0kgOTu0vnscrStpznTeULU-9BdBrh4WQ3l_rHIgNz1xTlP7jANEddIzVeoAVkCBAdB3xaLw_LQ3xywGzPcTtuWlBsv0N1_4OXAIQtsyHb0mv3UxaIdo_BAh2iNidZIGACN5bmGDbBh5kMuIGO8z93oroidcfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
‼️
وینیسیوس در اقدامی ایرانی طور تمامی پست‌های صفحه اینستاگرام خودش رو حذف کرد و عکس پروفایلش رو هم برداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102806" target="_blank">📅 22:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102805">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvHirn6fUa7Y_wJyv1gGcRh8av2JKBn_MIsnUlQtU8oxncF8s2U4O8yV4PHEqt0sUkYk13U46BG5j4TAXCtFi602dkiEgeiz2vuE88dm4-vo7LZSGYLbEtWdUmHwrJhvIfitr8VR3AxPj8UHMp-pTCzsCHiq3_Ea4N7G4zZnDatQ77I6H7Cj1WuNQKjffO06E3Z6sSDs3A5IEoHbNGfn651q_hbAmtr-wMJ3MnNBm23R3ZbRDfLuhN0Nn0MqS6kTjrHogDgJ-OK2Mn1Ef4KXaPvA2BojUJ9vERxbAvIeHE49yG5SUF4J7B3k8K-n8qxHKWmxxHgLi96gmSClJmVfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو: ژوزه‌مورینیو شخصا در پرونده تمدید قرارداد وینیسیوس جونیور وارد عمل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102805" target="_blank">📅 21:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102804">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETCNBPUc-WD5DG1hU8mdFnqqFss5MzjbSxibxWVMbiZTDA_A9i9tJJ0p1mLGD_bOy1IHDd4qknEK9WeYfO8t1EHJIQS4WWu-tku2oBcUQrGbY9hWYWno_REAueYSDp0i8R6tNaxjXkxPBQOWrz_JSLkrtNnwJZs3UpbUYWWGwYHW7jqjhTXB8HkLxnHFvGBdavJ31WsQnbvjDPSd9UXtjdNg1T9w_8xH2a_rEZA8ho1_4wJJ_1q3X8dXd8_MZWfX1FLRUFKrvlwUPrELSE3kIwltwQ_b8F3azhg-abBBLQgI5YHwJpzKaN-fl9lMJeAwVxUbDNhFwi56Rpe1t-Unmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کوکوریا و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102804" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102803">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCduLpiQbvJRhW2eTS1-mxX2MzKQ73X6ZBEY2ZGQXJ0CkQsd4f5IRJBZnnzZSBU_Ae2NjDNfvibqR4Z_WT8ngmjw_Ju72PjXwf0dlDDDU23siGsr_q9dp9ChTFmiC8pa77jXt7wJoGQmzXnOD9rDzSo0Rx9mN6xfr6tixhVjnHlOimzXaWksJjy6HrYYZVayMcHarnFo3qM7tA4RQvNXw1tii18I4nSQI6PeXuLXMglI7_oj8AsIjuqbvQSsrDcdjePv37ILkwJh7AmHmNx9_Rcop_cUhKXgVdQZ1-P4k4LeK6w80_7Pk_xtTXPjwU_avA2KOTffG7SGEuWwhM9uwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تاریخ
مرحله گروهی لیگ قهرمانان اروپا:
هفته اول: 8 تا 10 سپتامبر 2026
هفته دوم: 13/14 اکتبر 2026
هفته سوم: 20/21 اکتبر 2026
هفته چهارم: 3/4 نوامبر 2026
هفته پنجم: 24/25 نوامبر 2026
هفته ششم: 8/9 دسامبر 2026
هفته هفتم: 19/20 ژانویه 2027
هفته هشتم: 27 ژانویه 2027
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102803" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102802">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My7Tae5s9W3MhluxVUAra9BGYJC5m2g4hR1oUeHRQLTQ93MA7YqfFk0QAgpmduRDJuk89U1AaBVzmYeSKRysJ2yBkA0p4fcwM4Y-6WyeCRn1RdTFFzhFnY2WLH3jSuAGVptGYoYYzTYz1a1-9BXmD-fA9uhcTWZqHOMEUilHO9a0xJBwwJ45hjq8dBpnD2b8SdOjcwQm6cr0K6CLLpbRQjco98Kzh0U-zUxkFwJ2yo9KSTs5CAr9PzfD53M__2ySHqoV0Xa2DAW6kmxdCXF6CMvIgkIziVmprkOOYx7MCsC6DVD-Rk43srHxn8b0NRsJK-IKrX-fj5qY29u-_FgMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇲🇦
جیانی اینفانتینو به مراکش پیشنهاد داد که در صورت حمایت این کشور برای ابقای او به عنوان رئیس فدراسیون بین‌المللی فوتبال (فیفا)، میزبان فینال جام جهانی 2030 باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102802" target="_blank">📅 20:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102801">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=abFWD9rULuGBgl3KHQGvUR-aHwMagot2IbrsPKMI2fSRadO0Cj4n7SNBr0Kqx8kgmhnpxvUz9uHLq3Enrrf1CeinNTPr_n3ygEmZiKTGFeqqxeEtpHNIgeCvMY8bbfmkOTUEM6BaNdgPgRatfpEKQJQPG4QG3z53-pBvV3Ct2IgRES-ST7o37dkAGUTZZ8cXlBDZQxtv_eAxIkzqVi-Z3FyDJjtCK1S64Dvxn7HR1gwJVFQ18TZLU0nc2YpUGRypyJHN27mV9a9K1uSeQKbrpMJd_2ZXJEUwoggqr6TJRtjLRnyUO2iIuUcbyQW_1QYp6UmobAF-VBNBK1nDod7JYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=abFWD9rULuGBgl3KHQGvUR-aHwMagot2IbrsPKMI2fSRadO0Cj4n7SNBr0Kqx8kgmhnpxvUz9uHLq3Enrrf1CeinNTPr_n3ygEmZiKTGFeqqxeEtpHNIgeCvMY8bbfmkOTUEM6BaNdgPgRatfpEKQJQPG4QG3z53-pBvV3Ct2IgRES-ST7o37dkAGUTZZ8cXlBDZQxtv_eAxIkzqVi-Z3FyDJjtCK1S64Dvxn7HR1gwJVFQ18TZLU0nc2YpUGRypyJHN27mV9a9K1uSeQKbrpMJd_2ZXJEUwoggqr6TJRtjLRnyUO2iIuUcbyQW_1QYp6UmobAF-VBNBK1nDod7JYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8/5/2021
💔
🇪🇸
🗓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102801" target="_blank">📅 20:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102800">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn4MYVcUer6hFSA_1APDFjTYj_8Co2gpgkxmtLast69jAO7vYPTQ5EEDA8eoQ1b0cva6innlF6d4QH-M160-_idYf1GVuNOpNaKl0UBl175HCjgYl7jk2nCh2RQ0bl1-RnA48s7G1L3q0NuiFxqRV9dlQjKENplPfHc4j8VctFrsemEFGhk771YSvcAE9mtQ2ltKtcXqXO0nAdpg-p0VGrAjKnfgjTuFj42AKdPU_liG_GF5RXTrUSPSs_NjIoSGNPhtD04jOxQb0KQMwFZbqioS-0XL2Oab667foX5FIhcNrLvWu0UgIWf0ejc8JHu2H1cf4Bd-vCtwCZJkxl2hJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
استوری جدید رونالدو در حال صفا و آرامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102800" target="_blank">📅 19:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102799">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین صفحه رئال‌مادرید بازیکناشو اسکل کرده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102799" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102798">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKLs9OnZx1-hGG0Gi9cWge_F7mLqLhDSH34ra37a0_6sc5jbz3U18ZzkxMHhROW3teYDg4ZlyDvydga-omGAMVN1_QIOCMCchrVNGlJRoeYsaF81G5aiYL0M-6dGG3IG95R-mOJL54yCNJYFAPZt8E11uATQMAdjtd83-yL3E-mFPg12gqgJfEP2_Nh_ACsxmeyL5OXg42OV7MYuwhkZ3iBnkUaMcS8BXYpt_4PZgo0c-a1B6RoxNxduRAEj2TnSfpp7VhvREVvCO4DiWmXTh-ZPLpOhmaZDvqR_J756q7pO7811mmcdAHzFwTKULLkjJlJvsPealLD8bIguhJSPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🗞
با اعلام رومانو، مولینا مدافع راست اتلتیکومادرید راهی آا‌س‌رم شد
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102798" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102797">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚠️
هشدار، ویدیو حاوی صحنه دلخراش می باشد: صاعقه یک بازیکن فوتبال را در حین مسابقه در تایلند کشت
❌
تلاش‌ها برای احیای او در زمین بی‌نتیجه ماند. به گزارش رسانه‌های محلی، ۱۲ نفر دیگر نیز مجروح شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102797" target="_blank">📅 19:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102796">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq00Y6IF7KhBN2VSulcgs4wYTapBmIo7CqNG6K-gYBNNfWTAjfQ5jEgRNbcHudWa6mdZvnZemrEa5QHU8MZXpw9wm-GtzculHX8eB6NLwqtrhIaeDPDLaG-PJyRg08HhxeYa2j2NvQB797GtO2R2XI8gXlMqG4mAQRw6b8C6z3JBi6Q2sMD1QWPGc9dY0l3ZFP8borr1RiwmKJ56dmJ0iQlEufdfprR5r3gz28bxzJ3HBOcv24no9cLKOgQFzesMvgrov36TlEWpMPLPhN5WWpV33rk7vnhPW9PoR_DZnjClB-rCoavz87VhXJQdzkv2J2xkmgoTHRVxlGCOcJp0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
💥
جزئیات انتقال دیومانده از لایپزیگ به رئال‌مادرید به نقل از فلوریان پلتنبرگ:
🥶
مبلغ اصلی ۱۲۵ میلیون یورو
🫣
مبلغ اصلی با آپشن حدود ۱۳۵ میلیون یورو
✅
۵ درصد از حق فروش به لگانس‌اسپانیا تعلق داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102796" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFYs7hntxT2LOPMUDH7MTtMnW-XjzmGtIx3v3p6Ql7VTx3QZMAkghtaNjGpGcXIWe2uM_HsIRmTXPOziq-J0NjRKoPWNFAf4SN7NzmWIkRC2sqgQsej_Adi3nVysntEPhdAtTHpkxI7iNMuZDRYxxdt_zKLWi0VPWcrYi30T0mdSzYZSDE38csxaArFcVZk4ghB4QNI4Np6qy5SVJvY0ZEvAWyy16fFnBlVdmX9sPLwRiAHJY-D6lIRfivqd78LQC__5Ro0uLZahAAVvju_u2KagYbmVSYYz_Lc5CvI-pX0hDFn71JafPeV_FaV4wYsAtEdWtkBI5SnR3Id3DW0RZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
از اسکای‌اسپورت: وینیسیوس جونیور پس از مذاکرات امروز با رئال‌مادرید شانس بسیار زیادی برای تمدید قراردادش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102795" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
وینیسیوس گذشته خودشو فراموش کرده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102794" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102793" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX450VxPkNwhbNqhA9xvNBzkJQ9Epz1hfFQfmgKbhuXgsIuIMaUe_r7VT3rvKWQmtG1UXQEuafS6JJlwys6ZdN4Gg3OhIBc7ZS9Xh3i9o3IiUKbvZJZKkGm-bAnP-mbVUPl9-u39jgowWUoKwNiPnlw6wZnoQwrjyN8rUSCuuzlWdps_y-qH5i9sGeYIpQMhOe6S5E2PFQK73tqL3ZWYIVrCY0EGpTpOtGmD0z240AvsIs9lxp33AnLmi4ucBS6LDy_jpcwTbfTotiVdJNwKPYgOz5kP2WAxaCJ6mvMQj_-zRCnW6vdad72_4EI9qtr2MT4U3h-3niY7hyg9PLufIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102792" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚽️
برادر گارناچو که فوتبال‌بازی‌کردن یادش رفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102791" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102790">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایتی شنیدنی و جذاب از لوکا مودریچ افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102790" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102789">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102789" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102788">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL0D1clbb_8mHOrPH0a8ohuknTdJNyHGJc5WAoZd7Gl_sF8i0fVRtKDLPqppK-qSyt85z4EGXmcWJRT9VYH1SdQVdrRJ_HRgJDWZJkT9I8nYNvFkMytaejOub25eScTrIAg2cobSW2ezmd39DFGveZ1X1A9Y1RwWhfddxRnmEaZuUox2rAfzFxfawapNz8vpjdi3T_FQhIpv8XlQHbgb_VGmU_VUxu45m2BDumwyMl2nywTmOWnOgzdMoASv7AghCnLAqQSHibuPJ6YNGUACdmM1cfub-cYzBYa04Mht3xciCPzF6Y3i-I2IJ0U4plDYKpRfLZrJ13X2Vo2Nr-Jn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102788" target="_blank">📅 18:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102787">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UehO3pRaWzYnUFLetJs0EJu1aaDR1q-tIV_DcmKw-vT1wwl259uDXM1yVa3oKs_VSi94wPWj9alBJkfaT8EUulLFeRVMNvJGYEnX5VeX5SCPBYnMN_bMoxlKDnqhsIq8hlQy39kDWTE6vB6YG_no4dj1eJISU_8HdkhL0Nf-d70w2y7jWCArCSHVr0NraH2EQigkHgMdXbDuIip2GkZgGflFYWoKzuxO98dAhcFqe5IjN-D0iHaM0ocay9t8M2m62gSUL5SmyLNjqhQMCZ642QIlHavr2MJMT13kOmCXq1Hi8XbUBKv5bl3ZD7YseDRKE8s9_zsiKILlNn871_RCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
اینفانتینو همین الان باید کنار بره! رفتار او پست‌ترین، فریبکارانه‌ترین و خودخواهانه‌ترین رفتاریه که تا بحال دیدم، او برای خوشحال کردن رفقاش از هیچ کاری دریغ نمیکنه. ما باید شرافتمندانه زندگی کنیم و به یک قانون متعهد باشیم، فیفا هزاران مشکل داره، اما فقط یه راه‌ برای حلش وجود داره اونم رفتن اینفانتینوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102787" target="_blank">📅 18:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102786">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سکانس‌های تاریخی ورزش ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102786" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102785">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Nq2JxWHixCXK2aNhfB92lLbGvy9kW2euu1pt0Lhb-0qCzTJ0UID_yqVLazE8GHumyqeMCm_Ff1fH0OFLTPgoIOX6YKY6TwhpeD_rTonyc0Ji_JPvfXFlimzBu0glq3eMcJiIW8Mn19GrLsCe3LfqctWymCxTNg10Hy-zOx2JPbEfZovk4mSZeKv86T_q-tsdbCPkd0Io5q61d8qWa3d0V5M9kKRPRLWjGqTcFdZCTTbasLV0hODontadOQZNsFhKJxzIXR-EWZtcflWq7DxpHBupfz8NzZ0xwrcjblqlPByF42e-nYzy9IcyyXyZyuEk45Q_PnndQhmlmyWy5bBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنالی اینو داشته باش فعلا تا ببینیم چی پیش میاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102785" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102784">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
وزارت خزانه‌داری آمریکا: تحریم‌های ۳ نهاد مرتبط با ایران لغو شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102784" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102783">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات فری استایل یه دختر خانوم با توپ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102783" target="_blank">📅 17:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102782">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDYuZCrUU4iVRNhEVRVUiL2_LNpsjScPb2HM_8Lsc2EJliZYQvaqzxAkS-w2uQbPNigajFk_nPJloAT0YWZfF5du1qZuDgC87FcXKja3AQPKpNwgNfuzUFtHGFAfNdlQBP-PgL8ln4Dl9Nkzj4hry5P7lEBp9RIfJfR-GD0mh5zWbRJDeQjwg_EkWKPl--NMAoX_GXeN_ckOg6prkLjNXzv3ESVf38IDr3EmY_U-nwIP9H6H3hFuHR62BA-OJB-W3HO1UsmS1WTzzkWtqncgf15zuUi4FzKzVMDmGT_fSWY5H13XYHb0XGPgWFb-MN-KDwI-iPAW_yFRQ8A1t3HsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وندا جان دیگه کار از کار گذشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102782" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102781">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_7hsfd60WLtcePNY16yOa5vnMSGMHQJ1xUmz-kLd3JUwQ5t98xbAXaNcESatnRRCmIOIpjGQMMlCWqt2y4PRUTphpYJE6U5Ejt0X4PnA_4vCm_pff9LZz2PsQ8ZZVwLKFvueCm7qGs540DJn5nyw-eEIYR4T39Ugz6JqqT01qWqXD8htnvZL_I2zlRRXO_GYLwU7PZcp5pqPYDoyD-izz6FgP48fVVS97e-EcPyEbjhYlGwkB2cGKdWY67TGrwPP4bUvZnphSjMMnUlfCZntCAFThB8AuNbu0VcQZQMqNODM1htq7a7BwFNlkhe9HXXczrsp6DZ7TPmF-tVrTKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار در بارسا
🆚
پاری‌سن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102781" target="_blank">📅 17:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102780">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvaHtjwurhXGqWimkoaxscL5dWTNHbJpPgIO654ErvthSZrq3CmkDBYDekg5an7uux4WUjTY-gOJIFcqdQ8kg2UYQ7GrP8VW899UBobJqORC_tMAcWMl6mKHcVxHKaBzB4UgV8SPO3SS7NQ0S_l-I1z5gti1o5zRCYaFdhqPMUtUNjk-FtCLEQrelXnwofqMpk8UK1Gzqdk6R_UTQXyUW-cFfW2ATkvyiwgeqIHsT5cfh-yRrXlRXHTC-eOF7KtGGaRVOcSF1muMHf0EVpv17LunOVTzjN9AReYDuwlOmwI8S0ctdrczXZ207uqK01cqeKSPo8jtLSlXa7D7sxp2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بازیکنای مطرح حاضر در این فصل سوپرلیگ ترکیه:
🇹🇷
ترابزون اسپور: صلاح و اونانا
🇹🇷
بشیکتاش: تروسارد و نوبل
🇹🇷
گالاتاسرای: اوسیمن، گوندوغان و سانه
🇹🇷
فنرباغچه: گرینوود، کانته، آسنسیو، تالیسکا، آکه، اشکرینیار، سمدو، ادرسون و لیواکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102780" target="_blank">📅 17:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102779">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiHWCJQNfybpRJQYtfp-x3VunoVzVDg1AGd8-GMv4HInOyDY9SdzGKXjUmm1RhYaiLITeGTxuROEPaX9QJqVW_HgTA7_Xef_m3c7gKIMVKtBogahHbUILcY_lOy-JW44L50lmj2lJ0_CMNCY3yyLJnLybnYDmko7bGZT-FYIUM57q-XSn9RA9v9G9m64j0ldFw5-NSai2m4dXVR_l8LLXB9PVpD7i6CDvdC3q_cflWqde4bEz1q36qSeYNNH1D8CEbVKU0ARzQdpr-CI3kZcANLpd4RFJBHuX4tTwjgEtAzhdgIO8dXsAuYCuI93iArYG_QHDhu1tbkYf-5KzI3zoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
چلسی بازم تو بازی دوستانه باخت؛ این بار مقابل یوونتوس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102779" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102778">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnkKvFYTODE3nhUopS2AhUJqysXq8rVl6ih0xqJU8EwLtqmW87_Kd3aS1eIy4X241mE_qHvYUjwWQKwYydU183eew0dLUueFdYUxkT5Mx-XpJJk2N34JcS3vvf6a7-buuxAQx59-OzZvrDBLkMUYLjC4Rq9OCOkr1VVBf0dqxHM6e-v5MQqdUoxBaMJnhHD3iwvwlXDqmBhiMYbuSlZ31JeYvJN6Gch4AMXuO85BBEiXDPTR-EJaim9EI2mxVA14rIiEHroYawCKyyFksEFuc2giYT2_Ih7IEYkKdLnEghQIsLXeRxMxlaNg9f6ArrzAXdw28VssoYZ_YBEtJcK3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
چهار خرید رویایی رئال مادرید در سال 2009
:
🇵🇹
کریستیانو رونالدو (94 میلیون یورو)
🇧🇷
ریکاردو کاکا (67 میلیون یورو)
🇪🇸
ژابی آلونسو (40 میلیون یورو)
🇫🇷
کریم بنزما (35 میلیون یورو)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102778" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102777">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyVN60snFb_QYS57y-66RMqaoVe1BOOBg9MKvbyOhGZd7lLbZUXNzw2gVuoPgKeryjpqCZlHMmND5B2O9agNhb0S06kiQwDTGE3WIk3_Ey9r6Q48o_aQQighTAkg6pFn2VccYE2VydAuF6o4zAy2KK_KWiaBXk2tYh3zHAkORjjLbRACViaIzLM4UZzZIHAlY9L_vn4DMdUj-peX0zcFWUHdYTznT1kjPM-VWJkfN1ur0BhGEMYKsxGfH4ol4TcyspK2mt0k0YETM-EeA1Rv0QKnbi1mql0XX3eSjFclxwdnbA_uYb_y4lpLo0_Lo1PmZLQ2UAp7Erl2NUlzwuhsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
بارسلونا قرار است بزودی رقم ۱۳۰ میلیون یورو برای آلوارز به اتلتیکو پیشنهاد دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102777" target="_blank">📅 16:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102776">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=Ew2UW6H9DWW7O-CJRcDGwvPptxzAYdcP9cyAfTGA8pwR5OvXP2psZqVpVQ-J3GHiFiOiRKRlncD-ooTYMguY3JmCE_-ZQ0tmbZMDiiiQJ6skQkso14Sq2-OeO3LAQKFc8F9eVXlSUEGDM1_Lx6rw2AYrIELjo2En0l6WXKz0fB6HEAq-CxBo38MR3TEthc86bd9gMlqajMOoQlnxvazDZ1kJeIqR9QxjEdUgVwrTO-qsIWfhqE9pHm1uG6YZpxgYom8wBbHWEDQPEJpS80UT1_OniAcz3skC0QXz4RK-6fXVN5J_9n9T4Ll56Lm9KgW3zK-SR819omYukyUgmzOC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=Ew2UW6H9DWW7O-CJRcDGwvPptxzAYdcP9cyAfTGA8pwR5OvXP2psZqVpVQ-J3GHiFiOiRKRlncD-ooTYMguY3JmCE_-ZQ0tmbZMDiiiQJ6skQkso14Sq2-OeO3LAQKFc8F9eVXlSUEGDM1_Lx6rw2AYrIELjo2En0l6WXKz0fB6HEAq-CxBo38MR3TEthc86bd9gMlqajMOoQlnxvazDZ1kJeIqR9QxjEdUgVwrTO-qsIWfhqE9pHm1uG6YZpxgYom8wBbHWEDQPEJpS80UT1_OniAcz3skC0QXz4RK-6fXVN5J_9n9T4Ll56Lm9KgW3zK-SR819omYukyUgmzOC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🔥
🔥
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102776" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102773">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stidUZnm1IMoLxbxrGUf3hUlGi8RcJlyl5bTWHoc5w1iWbS1tkASh_QYXzybCiT9j-vZcAEW2frK6Zjv3Ed_spsyEHERlpD2HVb3JObySvXKbSDz2xYgWCAAz-54HfNKI9VKTtX-GlG4A5l23EH-vJMqzqOVq9RjMuf2JE8h1kqx3qMKDaqICC-nl4GRX074XVexX0g5X5Zlgk8hfQkEGufap116PViTIsTFRXIoPu1d85xVUuWeKDZ6aglEzMuBN-ek9WMC5ipvoH3yVWlMJK7ntaTJG0AC80kNWsGDzfUNNottTq3o-OT6DR2Jb0QG6YJ_V0u3zmtYu9ZS9BtoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsdrrl0Z_OUjwdpZvUt3nYnZkmIbIp51xaV8tFJmF6Fkm2X-5bslxPxntI1-_6U43FArpCqrH8cU5dN17UkMJM5r-WYdO2qJfuUNpbbtkzsbd7RFacWl3Eb_b3t4wiJR1CDs9cSBzld6ZwgS6cWYrmRKxAzEVoVTY0hWLXa1mTonuHDiza930fB0ZMb-_JX7zZc6YSpMmDdMp6OAAb6nVUL2AKWuHtgVBWvlZzW23yLNjFvrahUmDfsTlg3Nh7bdUkxysWla6oZzXgYQ128xXBQzV-cpqABEF5YqRgQ2xFemXaFDZ2MUQSXqD41B0LnUg99Zqdw2CCYa7DdAQQPQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqIggQhirsAcpT-oJ_IEsxm0ZVrGczqN7kCylhi1RaUXVF2Lesbvr5d9yJZKgwky_umOPbab7mHSgCu_0p0jejH8k4YcgXAixbqggHRQeXz1qVrfl4ZKsQSzzE41HFeHjFd17dpBZUq6QVF71LN1jh8RrrzlqwgPksM5nnIx6vwkzE9W6EYW09HloMn1pziM3x3p6YzeeMiZBfLcObcPYdyFQ2c5jv4mMzpACYhV86UAS92qi38RlgMpwCmomwLEC8wZq0Rja8pF97mto6McZGSz6bzPRWp-R_OiXrIVpDPproEQJei0VEnoLc_bH2a2xCUhGBxjCJ9sGlgJmHhUAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم «کومو» یکی از قشنگ‌ترین تیم‌های دنیاست.
لباسشون، شهرشون، استادیومشون و جوری که مرحله به مرحله و از سطح پایین‌تر ایتالیا رسیدن به سری آ و گرفتن سهمیه اروپا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102773" target="_blank">📅 16:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102772">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=bxNw0DhafwfHkJtIggkYxSDcj2NfqfG7ws_QUBKBsmRfkLHv_p35Wig-ycFdO5mSpn-toFrzdjg0xb8llBPv6ziu62gibtlpxb9LjWLPwXKOyVEDyk1Q1TFsOFdz2ZW9iYav2NebU4YhMbAlTxBwewJqbOZwHUfO2ZVp_XrPWwgbrohar5CbVPMozLrn1l_YXnGVx4v3JSWQB15MdUUztsVHgWOPTsa5B9eD0z_m92lJ3MV9nC4viz460kPa_rcV38NnbYAI0wT2rA_bv6-5vraIGFNsD6yhXj0Z524LMvr4c6uIyMrVVUXhpM9LrJtN-3O_PPsS4wLMm6zVdYF5Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=bxNw0DhafwfHkJtIggkYxSDcj2NfqfG7ws_QUBKBsmRfkLHv_p35Wig-ycFdO5mSpn-toFrzdjg0xb8llBPv6ziu62gibtlpxb9LjWLPwXKOyVEDyk1Q1TFsOFdz2ZW9iYav2NebU4YhMbAlTxBwewJqbOZwHUfO2ZVp_XrPWwgbrohar5CbVPMozLrn1l_YXnGVx4v3JSWQB15MdUUztsVHgWOPTsa5B9eD0z_m92lJ3MV9nC4viz460kPa_rcV38NnbYAI0wT2rA_bv6-5vraIGFNsD6yhXj0Z524LMvr4c6uIyMrVVUXhpM9LrJtN-3O_PPsS4wLMm6zVdYF5Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
روزی روزگاری رئال مادرید در بازیای پیش فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102772" target="_blank">📅 16:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102771">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk0Ht8wM6WfATOrXKeCpJZgllY0nKBsd_p4-UvAjZfaIioq1II1DrQQvvJGN2ZACVcLdSGX3bi3z_O_9Wnrho2S6OiEasAuNzgIGLVRTCQH4xyAir9u5LVQ383PwEy6IkTXn3lqJMy79QQ7JVNydMWbY6f0WnbK4tSCS67KZzJmLVu9Sfd1ZJw5vJD-2aFlXlLsYCvOV7KG6lcJb7vpgEqhWvL4o9dBXOZDad72mkmeVDgrpd1dKMZb2FVnISe1BJ3T5Ksqe85fHO_NpYzaTf5za-6yDzYjMEXeBoNtVySz8AUxU7yTtdmUCkz6PM88-GMx5BLfDeIxCc3HqaN6tsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس در واکنش به هوادارای رئال که فریاد می‌زدن: "وینی، بمون"، با علامت
👍
بهشون پاسخ داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102771" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102770">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=lno_qtcGlZ4RWlLxclhHOccn0CKfA-wsGpOZn8OmDZV_fLmfheK-Ev4sw7X8gpsBomUaH1SrkBTwSf6tF-WKCfzBZT0mq8aJh4L3d3yj8SIzSDk1Ew800bHfqwMxm2j2yIEQBI1H7Ra-9AMM2m_148q6EMpqNRB7oxCCIyo3-FQOVxX_O0d-rjhlK8zI66Ydn43jdlHW9w5CIFmyC5eQCEg_xgIY5mK6V-ivqI-32U2A82jeXazRRhgWlBI_BquaKm6fYaI344edtuSuAL0spCpL4HfltkT5OBEErYThC921QNqfdkqhnJqc0nDCQpB24BXCgNdmQ7XpEIl9s_nkpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=lno_qtcGlZ4RWlLxclhHOccn0CKfA-wsGpOZn8OmDZV_fLmfheK-Ev4sw7X8gpsBomUaH1SrkBTwSf6tF-WKCfzBZT0mq8aJh4L3d3yj8SIzSDk1Ew800bHfqwMxm2j2yIEQBI1H7Ra-9AMM2m_148q6EMpqNRB7oxCCIyo3-FQOVxX_O0d-rjhlK8zI66Ydn43jdlHW9w5CIFmyC5eQCEg_xgIY5mK6V-ivqI-32U2A82jeXazRRhgWlBI_BquaKm6fYaI344edtuSuAL0spCpL4HfltkT5OBEErYThC921QNqfdkqhnJqc0nDCQpB24BXCgNdmQ7XpEIl9s_nkpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی نیازی به تست دی‌ان‌ای نیست:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102770" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102769">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=MJSAyW_o7yrsRyrWp0RVc3F7VsONw0ayewKd0DyAyEWG9SOGwLD2C0cEaROrdJ2XUN_AoXKcwCyg-oJl2SZ4czlRG-3POFuye3xmzojMn_ESNUOk7PXIv57k_fs4n9GnPw3fmQcJqtJxxzrgwAytbN40HR7aYAd3i0NytzqyPZrmmDnlg2vGE334bIt7gUNzrPMzDNK7ubdNKhGzucSXy0dJjbKis4_KsFW1nkXWOAWz21SNeDWP9HcHTNnsrGjfkC3rcVyKh5clwlPl0tjiMoCpfCKaJdusSRCo6qPJQqZDg40uUgq07e5N5X_-d09m3eo-hXbbqp44uYtgxJ7qmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=MJSAyW_o7yrsRyrWp0RVc3F7VsONw0ayewKd0DyAyEWG9SOGwLD2C0cEaROrdJ2XUN_AoXKcwCyg-oJl2SZ4czlRG-3POFuye3xmzojMn_ESNUOk7PXIv57k_fs4n9GnPw3fmQcJqtJxxzrgwAytbN40HR7aYAd3i0NytzqyPZrmmDnlg2vGE334bIt7gUNzrPMzDNK7ubdNKhGzucSXy0dJjbKis4_KsFW1nkXWOAWz21SNeDWP9HcHTNnsrGjfkC3rcVyKh5clwlPl0tjiMoCpfCKaJdusSRCo6qPJQqZDg40uUgq07e5N5X_-d09m3eo-hXbbqp44uYtgxJ7qmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ياسين‌چوکو بادیگارد لیونل‌مسی این‌روزها علاوه بر بدنسازی به تمرینات دروازه‌بانی مشغوله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102769" target="_blank">📅 15:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102768">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=WzL9DejHcYSOg1fi5iMsUW69FkQwBHo8m6MKLQdeHxEjRg1RnNsh-UzmwUhzcEl8kMfURkvPx1w-vBZ3iT1xJAVAF60vbRnWm2Ti_tkWI6wRAy9um7Pb9mEHmXCLb1GoVXpJGkKVE-yrLp68_dV9llRA1ERVMx0NpwC8_XN-qDff6r97hPyUc0Ylqj1L1EqgI5FoOpDTT1hZcg6dNAl7Ehfm_qHiA5y0zRCTgcgpMiuH7x7Gqu9pirQTCI-dR2PQX1-3ZS12PcyYtQS1wXa7_6PRr95NZKmm3LHYUrStCxsRu9SYt5aYH0f1PWpCkg0vEGUzPbrXqNZffeWW5QXJnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=WzL9DejHcYSOg1fi5iMsUW69FkQwBHo8m6MKLQdeHxEjRg1RnNsh-UzmwUhzcEl8kMfURkvPx1w-vBZ3iT1xJAVAF60vbRnWm2Ti_tkWI6wRAy9um7Pb9mEHmXCLb1GoVXpJGkKVE-yrLp68_dV9llRA1ERVMx0NpwC8_XN-qDff6r97hPyUc0Ylqj1L1EqgI5FoOpDTT1hZcg6dNAl7Ehfm_qHiA5y0zRCTgcgpMiuH7x7Gqu9pirQTCI-dR2PQX1-3ZS12PcyYtQS1wXa7_6PRr95NZKmm3LHYUrStCxsRu9SYt5aYH0f1PWpCkg0vEGUzPbrXqNZffeWW5QXJnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
▶️
#نوستالژی
؛ مروری بر آخرین تیم قهرمان پریمیرلیگ انگلیس لسترسیتی دوست‌داشتنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102768" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102767">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e70775585.mp4?token=t10JmTXnZHem1IJ_R7sTs5pkUX8futSybdEBXvt0MkLY-H1_jibhbArLFq62F0rJMqXUwprGEx2fXqjCvLqUieYVkQC75JJX3qUdbxvSkfTLs4JNneCkFy5sGWrXKvzmVkKeFcd9Jr3qy2AviCHIK3-saH0I5rrl4Fs1kA51PgAGSAcFjJAH4ZifCi8Uz0DNgHe55J5NT_7Bhk3EfoVbuq6b09rcMh_I0IReg1C4XVIqILycAbnW3ZgPHW8-BYqe3TxkX6MRtmtbsY76UiDXQbsM7eztkUpWfHRHZPZcxkzGxsOVxH8qdkWUvu3WCTC5Oejdm7GOb5MJLIl8TC9ymQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e70775585.mp4?token=t10JmTXnZHem1IJ_R7sTs5pkUX8futSybdEBXvt0MkLY-H1_jibhbArLFq62F0rJMqXUwprGEx2fXqjCvLqUieYVkQC75JJX3qUdbxvSkfTLs4JNneCkFy5sGWrXKvzmVkKeFcd9Jr3qy2AviCHIK3-saH0I5rrl4Fs1kA51PgAGSAcFjJAH4ZifCi8Uz0DNgHe55J5NT_7Bhk3EfoVbuq6b09rcMh_I0IReg1C4XVIqILycAbnW3ZgPHW8-BYqe3TxkX6MRtmtbsY76UiDXQbsM7eztkUpWfHRHZPZcxkzGxsOVxH8qdkWUvu3WCTC5Oejdm7GOb5MJLIl8TC9ymQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
خیلی از بازیکنای جوون دنبال اینن که سریع‌تر بدَوَن یا تکنیک بیشتری داشته باشن، ولی فوتبال سطح بالا بیشتر از هر چیزی به فکر کردن و تصمیم درست گرفتن توی زمان درست وابسته‌ست.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102767" target="_blank">📅 14:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102766">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=ZiBX_bKRPaMLFwT0y7gz8E6SicxdwKx9Zu-55UT2FNhGbwpiMyJaGhOzGG7CPRhbslLIkdKyaxUSypy6zw0jboLEATJgtcYzye62ZiFf_mkH3_tOr0V_Q147WaKDRTPnn6MI0tqJs_fZps4CqB3Gkq-XyEagT3pmoUDBu52HWEDTK8cAJgOOm4MLE2Rw8g1bFGX_JTdcCkX0KiGhlFOImHE_SqI4PcY83uO6AZpXcCj1ICqKBDkS1rjEjSAjVkNvNN9gfAjmYkMnVQNiCCxhecoQumCDwk30t-ZikvSu8Gbfp_eyHQA-bHJ2IPL-n7fAhu4m7512mIPVdioXj5kZIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=ZiBX_bKRPaMLFwT0y7gz8E6SicxdwKx9Zu-55UT2FNhGbwpiMyJaGhOzGG7CPRhbslLIkdKyaxUSypy6zw0jboLEATJgtcYzye62ZiFf_mkH3_tOr0V_Q147WaKDRTPnn6MI0tqJs_fZps4CqB3Gkq-XyEagT3pmoUDBu52HWEDTK8cAJgOOm4MLE2Rw8g1bFGX_JTdcCkX0KiGhlFOImHE_SqI4PcY83uO6AZpXcCj1ICqKBDkS1rjEjSAjVkNvNN9gfAjmYkMnVQNiCCxhecoQumCDwk30t-ZikvSu8Gbfp_eyHQA-bHJ2IPL-n7fAhu4m7512mIPVdioXj5kZIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وقتی میراث فرگوسن نابود می‌شود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102766" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102765">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCuIT7AG6-SywrzOeq00KO5L7zrlaurlvtv9USBHqLoYfr0qR85Vo1ns1w-6p8E2qe7I8qjtsswhvYlZRa_CIJsCD_UjvBmnSYldHc062Hh21ZnYTNyotJIrIlfV28iwjbfPgzQ2-A86rWg8HHv_7qhxijLUuqt0LczL7XKRiMn1ec04WTzOX0l9_ySgp5yb4cUbFN9u6F1nJA9oqRSPqeW5JQiOVn3p8xM4Jqmoq-MUp5HKTVtN4FI1yhELnJiQZrrC-Br1o9oi9DjtK1M0oTZ0w3kz5d_yIgv6cvylHQWL4OQf_ngr2SqhmqMoN3prTaCS9OkS4XLDSTXAxtxfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔴
7 سال پیش تو چنین روزی کینگ هری مگوایر اسطوره فوتبال انگلیس با 80 میلیون پوند به منچستریونایتد پیوست و تبدیل به گرون قیمت ترین مدافع تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102765" target="_blank">📅 13:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102764">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctDVQIuEVBf9PpBHSqIwcXZzfdnb5XndiO59QEDaryP165XTkxldn7AlccIjhYiittBsVGpkybOWV6FI2RaswmlSLLaaHVISCRG8eOmf9hnQJtSLLtoM0BwJ9rPiEnJExbzOGAj7vkqhQnVk8qmmIoQvbnmCSkK0Ed9BLOlL9uPWzVWyaC9xu9hDGNnC6_hW51twvfTtaNRKqn8vZPSqXuZgcpJrccjrIk3t46DL_Lis_zuctiVnFayXMQnfqZlfx6Svv13PNSoti_8B52Pi8bzUq97SSX-KkZoQneenbfjk_jT6b5sfhYnmyYJHfURKqAOZBHOpUWepRWWsqllxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102764" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102762">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLBbDfiDqRDLrRTU4qeDpHPaGVoPt26js3CO4ueT9v1TklD1JZUZvvAjb3_E3Gfm-i6iA2LJiVMTXa8KiKlRxNA08yTGUw07yNsqVDZdm8QUf-4EvyOFgCOIMo2eZfJ0Jm0MP1O0DPObV_XW0vM_kmHKAz-j4NTzOj-9ShHZUGn7kmM8QJj9cg8TeT4zycx-FsrezWxsqBytKzPg0HdA8f8vtAffGVjP7bVWdaRiT7p0fUfGy2YtqgFIkMX6bAflsWdYF40MOzzQbfGJgn8vhJIMyFKjdGLDuLm_bRZPaem_f7ZGxnZom0KuSKUmZRAEbCygEKttwoRk7bVIrwyjMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه که بدونید فصل گذشته
فران تورس لورد بزرگ ۱۵ بازی پیاپی رو بدون گلزنی پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102762" target="_blank">📅 13:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102761">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=G3_YOHz-rvfjAZlSfkUj-bOU0efoJ23fLsAFfD4YBKZSjAFVr7RmmV0WCP91UfsjLFEKg-ctH9aHzXl51wPQ2l9sBfr-awjLQZdElZ-_NOXLl9avTWpHNoglR8W1fgkZajsltzJ_EVxQxaat5quiDc7yy4YU61lFVpTs09i-ZINTWtGw_QQ3uAqmcCJ0kZhJc0TATRn_U7jcrS55NubCwU_53GbF72YVPp7ENbu5SGioqG2GAdp6H1ZYgGauS4rgneCc1pJGeihqjiyqTjEntSIBV0JOEj7LF4Wj0S4hwuFzQfmdyeQd1rXGmYWoe-nppZAWnHqnEefKVgUB_CG9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=G3_YOHz-rvfjAZlSfkUj-bOU0efoJ23fLsAFfD4YBKZSjAFVr7RmmV0WCP91UfsjLFEKg-ctH9aHzXl51wPQ2l9sBfr-awjLQZdElZ-_NOXLl9avTWpHNoglR8W1fgkZajsltzJ_EVxQxaat5quiDc7yy4YU61lFVpTs09i-ZINTWtGw_QQ3uAqmcCJ0kZhJc0TATRn_U7jcrS55NubCwU_53GbF72YVPp7ENbu5SGioqG2GAdp6H1ZYgGauS4rgneCc1pJGeihqjiyqTjEntSIBV0JOEj7LF4Wj0S4hwuFzQfmdyeQd1rXGmYWoe-nppZAWnHqnEefKVgUB_CG9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
😐
⚠️
ارتش‌روسیه دیروز با پهپاد یه سبزی‌فروش اوکراینی‌رو تار و مار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102761" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102760">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuZLrLHCPqllOErR-fF28okIe2L1GyyTQeBlmZITD0gf0hD_xEAglfX0gKy61R4t5ZX2pF9Ix21DDfmZubt0rZPTyrbWGeLTtXQpHqmYlPJTUYKCn5MP3N6PCZTzfjCJDSGiNqjRCOyUUbY9m1fspBYSNyB2nZyyEJ1dHd0Iwcu7IQy9HH8RMca4nCC7967Dl3B6x5tDNexjGc3raFAoL5s9EFc_lPY5LzxYF68mEft7VfLcwlcpxboWnKzUYdnDCCTiArVHpCj87TYaeszJUZtD_HVCbrXvPAAYdV9fHBT6gBLyJ82hUu6HR0sLTxUqVJCJAHwx8NdqTxnxuV5zBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102760" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102759">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPujSNbe-ZyZYG-4f6FMpP9RbMWS4xCOXtY_-_pOr6OTJ4iFLyUFPb7vBF1alcX6plDOzA6XfRuAH8qIfrKFgNyEBhrObeCpytarQZOg7y5yKgYS4Svu1OqflenYGLRpqGPQeEMxW1XIq5PUt9YFjgLNtPBqwamVw207kepcWsvS8kXk5H10KHJqVGKG5k3xu82L-LFOIhAjYfFNfDEngWh3QIswAAnsGLnmz1W7kmZVxavxXo0QkTi2dnO_wpvnkXc4ge7bjuZRzoR351SU_8Mc4QVUMULTXCXX3BmLB_nT4zQSGjSeyF20bTy-5ekvk_UUKDPzXZhWXWWesqv_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بازی‌دوستانه؛ ترکیب منچسترسیتی مقابل منتخب ستارگان لیگ‌کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102759" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102758">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcG9Jm9WebkRDgo5NccL-RwlFz1PToN1FnHGgekpKUHuAR8S6cCU7eNMX9Zev8mT3vPPo1Khf-dSM4F-PYTsBl4Ujr1aCAp3XQiinNOjU4_xbUkHPw34JZ8s5ND7M2RjOAt7V-UcC3iRBKJOYXZxgycY77JGs2Of0PQjaPATLatbbWTG2nxF8hO_TBCZThpu0dBXO_3Z1iOce0x5QVfjj3PwcN2BmEadHjbun7rN6tyyvpiVNIhWCehfsEIYWmnky9nPrDjYdZotlP9wnz0lm63grp3nOmHI2l9flcdX-GnNdGsNBM8FYUvXFNWm6j4ThVtU9U0I4iPaUJfbWJ2-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
متئو مورتو: جاشوآ زیرکزی بازیکن شیاطین‌سرخ در آستانه انتقال به یوونتوس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102758" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102757">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=Y4jOIK1M5CS1Q782RIW5SsocH_yi_lXmuM5r4WnvCv9milpeQQkdHjXMpNpjBiew0EXN2R8qJYlprG9W8wofCY977FTvApu3iM3gVdnsmjb2z4OBKiwGNt4OrA89zxlDH7cCxYHPwuv0MhZwDAMEI516HXzOp_Wvtw_v72OfCQ64ZJJEWfwvLUWhyuko7Yi_cjnCA4ZNlS_78f1YCy4-gODb5fzp7yWBwchTNtDbGQqBU8maYalyXJSkzzT5dan0xFuSoC7QjGV4x9GE_OvjmKYZ5HfJMgY3mF7cHSbWQB3dU3DVu5YYDrcnyncakUSBu2o5BCIFNZpI9grV-RSEAlFAyFH8fPyP97M7dP-HAU4hkBLAHVx4bLzKFeZH89uetJU7ohiE4K-D2aUUOD57QZngNZ2yhvphIHDj8DQFuddOTGI7s26cB3BhcBqu2u1_abpBOtwvwCw8hVyuMGOAEPwI4DAAMWdt_zyAjUX1vKhKERQLS079rcqLAyd4RzK4fJwUjkHVqgNSVtBNfdNOvsqSQcvrjSigsk7hVmfI0JliWHgSr6kVYtqhrV7DQTyfxJzqUQCJcuqcDBMuQUV2vezjYxqji57V8zQYrYMrMemjYUZVknD664VM0G7rtj8Wz_vBEbg8530Mvb3mUpo7wDVgCkciFrGL_WNgB9aH5nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=Y4jOIK1M5CS1Q782RIW5SsocH_yi_lXmuM5r4WnvCv9milpeQQkdHjXMpNpjBiew0EXN2R8qJYlprG9W8wofCY977FTvApu3iM3gVdnsmjb2z4OBKiwGNt4OrA89zxlDH7cCxYHPwuv0MhZwDAMEI516HXzOp_Wvtw_v72OfCQ64ZJJEWfwvLUWhyuko7Yi_cjnCA4ZNlS_78f1YCy4-gODb5fzp7yWBwchTNtDbGQqBU8maYalyXJSkzzT5dan0xFuSoC7QjGV4x9GE_OvjmKYZ5HfJMgY3mF7cHSbWQB3dU3DVu5YYDrcnyncakUSBu2o5BCIFNZpI9grV-RSEAlFAyFH8fPyP97M7dP-HAU4hkBLAHVx4bLzKFeZH89uetJU7ohiE4K-D2aUUOD57QZngNZ2yhvphIHDj8DQFuddOTGI7s26cB3BhcBqu2u1_abpBOtwvwCw8hVyuMGOAEPwI4DAAMWdt_zyAjUX1vKhKERQLS079rcqLAyd4RzK4fJwUjkHVqgNSVtBNfdNOvsqSQcvrjSigsk7hVmfI0JliWHgSr6kVYtqhrV7DQTyfxJzqUQCJcuqcDBMuQUV2vezjYxqji57V8zQYrYMrMemjYUZVknD664VM0G7rtj8Wz_vBEbg8530Mvb3mUpo7wDVgCkciFrGL_WNgB9aH5nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽️
روایتی از تحقیرآمیز‌ترین گل‌تاریخ‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102757" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102756">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=f-7d9hoJsoRWYOBp7-8YCkl_VJedc6cgUTciQylixTeFMaQUmCP17Jg5gsR1wq3uRmfRtW9WEZPoV1XbAGgU3jiGESAIxSNtDqMmivu0e55NeRLPIkywplpjMrjieCdBOaucPtMs3rsiTsCOq9UsouodeWCeiSDyo2mPxHBY6Rx84i8F7DJVk_7GXa_j-8GAtpIobr-olxgDunMb9qYOTXrbsNdlR4mCge5PsBfWwZTVmYq9apG0YwEDVYl0kdONRkplaYy87tEhPQjwImjLMesjchW8pxOxPzz8qBnMKSF669AIAwqHPhHzOiML89Wm9afkvUMymNvdb-zcBH10Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=f-7d9hoJsoRWYOBp7-8YCkl_VJedc6cgUTciQylixTeFMaQUmCP17Jg5gsR1wq3uRmfRtW9WEZPoV1XbAGgU3jiGESAIxSNtDqMmivu0e55NeRLPIkywplpjMrjieCdBOaucPtMs3rsiTsCOq9UsouodeWCeiSDyo2mPxHBY6Rx84i8F7DJVk_7GXa_j-8GAtpIobr-olxgDunMb9qYOTXrbsNdlR4mCge5PsBfWwZTVmYq9apG0YwEDVYl0kdONRkplaYy87tEhPQjwImjLMesjchW8pxOxPzz8qBnMKSF669AIAwqHPhHzOiML89Wm9afkvUMymNvdb-zcBH10Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
تحول تاکتیکی تماشایی انریکه در پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102756" target="_blank">📅 12:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102755">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=cYve--iOMqKiAh88KcroPApyicQG79pc0g_xGd4_BB9i6DBxyZVOmbDKN22h6sUmC7BYAvHeMN0nphYzRjLAEVPStn5nuuGyefaVZrv1FZhiP-8npHH8Je11Tu6ksw1oWTWFggU0UJF9IW_UhqNQj-9qRQD0viALARr1LzJ0sVLg8ILtrp4reJD-Zmh111me3FK7uPuiD3TPYu9pwaG3XfpA8z5mx8LQCd8_Vps36Lk3qLEyWnbz9SWlmSOUpH3hksZhfYiyNKyp6ZR_SHqCaxNvaQJUEExeXsSi9eVXAJeOd6K1Pl9_R4Pxjdd6NRAqGAuUfpGTTUgm8JMNEVy3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=cYve--iOMqKiAh88KcroPApyicQG79pc0g_xGd4_BB9i6DBxyZVOmbDKN22h6sUmC7BYAvHeMN0nphYzRjLAEVPStn5nuuGyefaVZrv1FZhiP-8npHH8Je11Tu6ksw1oWTWFggU0UJF9IW_UhqNQj-9qRQD0viALARr1LzJ0sVLg8ILtrp4reJD-Zmh111me3FK7uPuiD3TPYu9pwaG3XfpA8z5mx8LQCd8_Vps36Lk3qLEyWnbz9SWlmSOUpH3hksZhfYiyNKyp6ZR_SHqCaxNvaQJUEExeXsSi9eVXAJeOd6K1Pl9_R4Pxjdd6NRAqGAuUfpGTTUgm8JMNEVy3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇦
آردا توران در تمرینات شاختار اوکراین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102755" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102754">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960818b54d.mp4?token=vXnaWS0CtQy_jZaqSBrJaVBNHh-HaWPkwjT1z85IFG8yVv8uFh2iGauAxhqxLjI4PnSEoVQS3cgLfrp2-TnxRIXcKZSkf3Cd6EZ06kPLaRSiNlvCCeRZ-AB8ZJPp8-3bw1b78_p7pVywkKC-iiGvKU9gnMVRmvvZVVcRLBCuRZZLaa6g1PCZkb0AOeAQtgxsbYwHEbMqAbbcxauUdskvHZCfH22HsRbEyVMaHvHH_hzGCqnRbErm6E4LmacYiyvoET7iXGPD9H3e1mw2YT0OCSOsnHsxZxjBP403zQ0FaZwN-5yxqNKwP7BocbDMmeSR3QXxfnuUvpM4wCXYtvxwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960818b54d.mp4?token=vXnaWS0CtQy_jZaqSBrJaVBNHh-HaWPkwjT1z85IFG8yVv8uFh2iGauAxhqxLjI4PnSEoVQS3cgLfrp2-TnxRIXcKZSkf3Cd6EZ06kPLaRSiNlvCCeRZ-AB8ZJPp8-3bw1b78_p7pVywkKC-iiGvKU9gnMVRmvvZVVcRLBCuRZZLaa6g1PCZkb0AOeAQtgxsbYwHEbMqAbbcxauUdskvHZCfH22HsRbEyVMaHvHH_hzGCqnRbErm6E4LmacYiyvoET7iXGPD9H3e1mw2YT0OCSOsnHsxZxjBP403zQ0FaZwN-5yxqNKwP7BocbDMmeSR3QXxfnuUvpM4wCXYtvxwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بنده خدا احسان علیخانی خوب مچ میثاقی رو گرفت قبل اینکه بخواد علیه عادل کودتا کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102754" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102753">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy-5ipRibG19sJFKI3vLHIMW6HZl0FqShyd2424aXnhBiaKBNdaFT2lvVhnPtTT6iH0yzEPnh0i0AtvPZoSXLXwXZjT6MHHZRTzawgPJXLYRDwSTjBdnCUN3Jd_kuVwh1HXP4yTb80D5vbkYccrw2eDYj-NI1FyZOxjK7FSp06Xkksn0L4Z6mXsZXoCYicF5kumHTkp_6rt5syus8rf59c0jmbyfOq2Kh12VBa_Rxu8L9oJFpevSE9NiXUV11qN6Y64QOaPhgb6npvXhyjZQehYh9ENMCt37uzDRHMhwLuxES7pkTRV8NbmcgiFBXrcINxqyoPESkSZbFT3kduzFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
بازگشت دیومانده به کمپ‌تمرینی لایپزیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102753" target="_blank">📅 12:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102752">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7jA_Dri-rABMwaaREtZH4-i-TRJsArb1LcAyrVemQi4VgQ4KDS50D7w2j9gx7DY7avEUd2MRpE-c3Hway-S5ze4O6fydr1pxP4wB-JrM43KXzPiR1E-QvIHlAQD3yx913LLzNlnUURN5NVIi5nl7DQKNvLYwl0xmapMb8SP-GMn1tbUvp3IebrX_oqyQPBwbM92MXihY_VDK6-IhlQ7L8HkGIOFWvNeMpzLsMx3_LBUigR6qLUzCIFhdJme1Y6wFXcnanrZTH6fLZARbuoP5FHvlmHXH86iC2UASshp36_ZXIFbUjEyD3MHVVbL0DJf8dFA_tPtHP7VJddOukMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
با اعلام رومانو، ماستانتانو بازیکن رئال‌مادرید با قراردادی قرضی راهی فیورنتینا شد
Here We Go
✅
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/102752" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102751">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJOsuBJF0hy_GoNu4ahEjPRZrvvu7UVBp8KMnp7y6iduBDHz53Zp-3sDDM2464ykw38MUFGNtHG1ujewNOFRmpSAyLwDEllfqMEBdHsd9HeMXmfLID3VA1SHfnJQ9l2zg5Ml5IlgxOTouthY6xzAMjgS9Fw0i8HylQ-ZAwGQroCcuMKPSpGNlGs-H7OzlAnZF5EloU3h-_3h0uVx2Pz0zP1HmbbLsJv39HuWJE-dUnCVw2HXyJrlMiDzl8WrBqelZ1sxnjTq_SQZLguYDdUKI0bc_pWJoorImgdmEbk0dx7X_8L1MwY4nXY2EsWiX5AvY_g4Szt8HuK7koOKr0M84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامین رضاییان رسما از استقلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102751" target="_blank">📅 12:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102747">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRg9vAOQsGC7HCsnNB-q2SfYBInSedA6ehwRLH4udcG2d5J0dQaB4mp5ghW8ADsM1npnhgsNvwcU3w6PKxFwX9PLyjhsnbb7e8S-nZbo8CA8IaslJ5S4a9jdotlp2JtUgHh7BRKBEDay_57ooB1qtNH7UqiFbVFIK_PeEu4QCXU4Gzg3OqyDwCq20I9eJ06Is-pSiKnJSiOdtuegHTPYSkbs9WbYykyQbi0ibtOh9_nBsyn8-taxcvyiq7ekK8vQVOTY-Nmv2ElV_wbTYcT1twiJtwSJGGqUKJDtLZMeVQ6ZA3wSXK8FR_D1-nG8HJ3X2pkXqchz8isBzTG9lko-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbajWrCGth5yrSNuXbrQZCEKlXcXrHw5_iFgwBBbvzj7AiKcXlZtrAQTz8soO_WPVDV-ScGnOuvjX39ExMtEf6n_UkQMCLWZXRXDOc26KGzNNhvNHPmuwi2kDn9aDO6NZ4ATDvw8negWZt8lOzC-oIp9t_hkQKVNqXPEI59xXKkXptsugpzRHoZqMmFG6mGcNOMQJ0yVB3Da6JgcKa3l07YF6u5zfhio5o-pvRJc9uPzEjK6LNmApelpNjaGQOS1p9sCNSDGtQSS04WF0GDkI7jOzTHWeJwdsY37CfkO-itkoGSmgmzD67u3b9agRT_tN0MMGIRofgYqL6GieHywSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgX8dxf3YJK6v4xw3n9o95tg86SmjL_hd_EDs2Jas1Txzy9HgcUTJ999LRNEBGVfnU7ftt2rK-yA1O78QuRNvY6_XuhvAg3tqSe_lPFH0EU3eIhU-hTpsTkkhgpJxY1qIM8Dam0uvwBqpWyf6O62J9g5meM0O24FYPTKfVXVHM5IutizMLZgy_g5n2kl-2zQnTKKRTUt0Wf7Ab3_uoXJpVhLQ181fTgphdfDfJQRlYsrAi5HzTVsnY6Jltu2JetVkKz-HUaEGcOtXpch6P34_NFMvd1LYd99J1KGCmOOImZZ7Y4pdOcgQcibMwSDuGRbJSS6YVd32qRw3GldC0KZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ulh_pDhNPLUy8Gj3_6tPRKHbXqtgzaMRWiAp8MyKnTXDtiHoV0U2bH5mexQn_62Sd9dVh9dPrlbPmy4FdJCOQDUZPORZgr7OarjOkl6MZ2Kq87VICYxsXACrs0mkUse-5CoueTeqzs6yAFgiGI_d_ScNmLYJHGhPi-pFNeED6yQl2alooavjQV7pIL2ZC8B499-Fh1HzOENapH89mTya6KxZgREya9UqjiT1iDn6Zd1zRzT-BX7S1LBUGXtYPEToenA-jKxBjKM0uKBTu0qgrTJ47vKff7vrRrEqIW_DZYcREHz-Qvo3tB261BgXmVr7WOa5XmLe287c3FfVVcn7mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔺
تیم کومو 7 سال پیش تو دسته چهارم فوتبال ایتالیا بازی میکرد و حالا به لطف نتایج درخشان با سرمربیگری سسک فابرگاس اونا فصل آینده یکی از تیم‌های حاضر تو چمپیونزلیگ هستن.
🔺
جالبه بدونید مجموع ارزش کومو تو ترانسفر مارکت تو فصل 2019/2020، 2.4 میلیون یورو بود و الان به 489 میلیون یورو افزایش یافته
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102747" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102746">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=cfDwQdZkmjRs-sLCc7MqasR_FQXWc3xw938ytRO16IlM30QN9WCajoVxaFdbRsBfIt0DYQsUNUO75ddqzQUXASS-9-2_HlAXZdPGc7dd-IAOfak1Jw1sCV1ioMPLaZ6YKnLFwH4Z-GP9rMQUReObJo7_87YD6ZP2VF0vKItZs9_TFxZlRXcJPE1ra7-axL8qrm1wAZs0GZuz5uFovIabRxPq34Cevmyu_w3AKytvGRpeJBKcxBy1iJ8Ng7f7V_VNnlCgifwwELviayFTZpcMJc2Icu0sanA6VIIDRku1Hmbz2WBV872WS4l39GJ-LKIsQFKtYHbw7v133sQzW6BluA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=cfDwQdZkmjRs-sLCc7MqasR_FQXWc3xw938ytRO16IlM30QN9WCajoVxaFdbRsBfIt0DYQsUNUO75ddqzQUXASS-9-2_HlAXZdPGc7dd-IAOfak1Jw1sCV1ioMPLaZ6YKnLFwH4Z-GP9rMQUReObJo7_87YD6ZP2VF0vKItZs9_TFxZlRXcJPE1ra7-axL8qrm1wAZs0GZuz5uFovIabRxPq34Cevmyu_w3AKytvGRpeJBKcxBy1iJ8Ng7f7V_VNnlCgifwwELviayFTZpcMJc2Icu0sanA6VIIDRku1Hmbz2WBV872WS4l39GJ-LKIsQFKtYHbw7v133sQzW6BluA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
✅
رونمایی رسمی باشگاه ترابزون‌اسپور از صلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102746" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102745">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=fAmZ4Pj628GNymE2EjRoV5bN8wpyPAxCgTUPUiNQZ1gUHA4u5WZna2ulM-gsm9g8ZJez9dFDaju4osZxPnTuQuunx9EpOKz4M_zdRrBsFO1cZjZFS35vmXw9WjCmFBErSekXR4bZNxykrWfeOGtPYZW5kCBw3Hx8O3c7tfp6OAM2jHfJwIfK3lxwfvR9ehiA0cuQlwv-61JPMHYoMY8SptejFSupw4ZQkXTcFAFQ9i0aEP29OOBYbPweIPfdoMMDL-WXtt_dIniDGid6ehJpcdp4ISzk3Q2T61iv7h7G0o1YMqc_i655EKV6yqGXEh_Veexnyee1kORDSoMen1-e-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=fAmZ4Pj628GNymE2EjRoV5bN8wpyPAxCgTUPUiNQZ1gUHA4u5WZna2ulM-gsm9g8ZJez9dFDaju4osZxPnTuQuunx9EpOKz4M_zdRrBsFO1cZjZFS35vmXw9WjCmFBErSekXR4bZNxykrWfeOGtPYZW5kCBw3Hx8O3c7tfp6OAM2jHfJwIfK3lxwfvR9ehiA0cuQlwv-61JPMHYoMY8SptejFSupw4ZQkXTcFAFQ9i0aEP29OOBYbPweIPfdoMMDL-WXtt_dIniDGid6ehJpcdp4ISzk3Q2T61iv7h7G0o1YMqc_i655EKV6yqGXEh_Veexnyee1kORDSoMen1-e-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این وزن و هیکلش یه حرکتی کرد که واسه نصف بازیکنای لیگ مملکت قفله:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102745" target="_blank">📅 11:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102744">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWck4JTfQQ7Y9VwEbv3NnjZHK_4ZWppibCgh_v9wgcIG3f4ybAozWj3S4gjGcHxsj-sT-Efq000YrMBZafTbodIC626wj4jRTyHJ4Dsc0_NlW2DUTjC_-pOKvXRcPRb8MHvyIXrI7318biT5qcsRX8wt7O-Ozd2s7P-ufeQPNvql3ddJ6mkR8LQwbsBeY5u1a0uPhdMeeC5vdxi5uiyWFHUWwhSjuxbyGo6HIIIzq7cE_ojSW8fDDOSxegPtUnYlnBMoHInXcdvHYldTh70vQPJvbFtajqu2-t-IQtC-4JkGFX91VOhrsUfy_Cxcp9wWFAeipwYLo4vf3_KbICPfG2txc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWck4JTfQQ7Y9VwEbv3NnjZHK_4ZWppibCgh_v9wgcIG3f4ybAozWj3S4gjGcHxsj-sT-Efq000YrMBZafTbodIC626wj4jRTyHJ4Dsc0_NlW2DUTjC_-pOKvXRcPRb8MHvyIXrI7318biT5qcsRX8wt7O-Ozd2s7P-ufeQPNvql3ddJ6mkR8LQwbsBeY5u1a0uPhdMeeC5vdxi5uiyWFHUWwhSjuxbyGo6HIIIzq7cE_ojSW8fDDOSxegPtUnYlnBMoHInXcdvHYldTh70vQPJvbFtajqu2-t-IQtC-4JkGFX91VOhrsUfy_Cxcp9wWFAeipwYLo4vf3_KbICPfG2txc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚽️
⚽️
روزی که لیونل‌مسی به مورینیو در الکلاسیکو درس فوتبال یاد داد و پاسخ تمسخر سرمربی رئال‌مادرید رو با درخشش فوق‌العاده‌ داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102744" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102743">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102743" target="_blank">📅 10:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102742">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBlPFJGM6KSp7CKCrjF9JD5W-1z2FhOFBjWOgKxGt1RNwjpNtxHbDMwZ5od1S1hhL5U3ztDjpwGbnZ2uPlV1pOuP7qKXwtzmSrZF5qcMlFJTRBrmbEOTK7dZClgALB43xYEa_9chxWhksYngVTWRnlsbApVBI5xumidNyjfwmoJ3HagdxlD0ENMvXw4YGW8etGntqDiUPjhUk-zqK_82e6ddlCqW8MwbOixb9b7OauESGSq3Sre9JjvJmOjdKWvL8KsllcOBfkHBO4oh4TaBnzHgNvn9LYc1Y5aIJY8leom192rmqaQRRbApCFze1j_JRzcyI3Gb1Nq5fMWhZG5GGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102742" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102741">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=iSHErJCY2-PtmoOMzFOrgaS9D6jTkHpWejsb0LeMoyu2WXogNA4SGbY3v3QLtTTc33hZD8-_dhPv5DbLOgQdGJFmiNIt3tK4VXZ5d9fgY0xf6It_PrZ21Un6rMEqLa1nYM4li05wxbWeDzdMtcfaLv0gkxVejrC1AwlryVe0h5HdLtoXkZB3djqpo9IzS1cVlu8Ummeo-WCTDPT4G9Y7OdF7N7lj82XQG9KQvfHIJnHtbxeLOUu4wn6OtnIdHEpLSojqIWoQRbe3pwzC_4HAO3JFEC14mYl7uFhL35mgwV4qghAsDB-A1BMo4W7b0130z4Dr0lHLyRMox532yENYOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=iSHErJCY2-PtmoOMzFOrgaS9D6jTkHpWejsb0LeMoyu2WXogNA4SGbY3v3QLtTTc33hZD8-_dhPv5DbLOgQdGJFmiNIt3tK4VXZ5d9fgY0xf6It_PrZ21Un6rMEqLa1nYM4li05wxbWeDzdMtcfaLv0gkxVejrC1AwlryVe0h5HdLtoXkZB3djqpo9IzS1cVlu8Ummeo-WCTDPT4G9Y7OdF7N7lj82XQG9KQvfHIJnHtbxeLOUu4wn6OtnIdHEpLSojqIWoQRbe3pwzC_4HAO3JFEC14mYl7uFhL35mgwV4qghAsDB-A1BMo4W7b0130z4Dr0lHLyRMox532yENYOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
▶️
تیزر دیدنی ترابوزان‌اسپور برای محمدصلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102741" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102740">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtOgM6TI4SLftA3SWtmgm2Te4zq2OuwargJWA43j2SresmN86Cuz_EoiYpNpDtMMWTs6pzrNfei1-nIMwjbeo1kAfrdSLSulYtAvPuIksA-Ryabqka1itCNKsFMtYxjLu8PYjuhKRLhEVwlHRet_eWSoEdT2RBo3wYiOB7pqM_r-LJVZQ6vehZnnB4oaokWvGoPpQOdejp5_HPzHFUUSz9F8Ytdu8c52Yx4VFeQlkGrUzRvMV_Hn-KHv_H-6KTD6edDM7cZ-sOHHe47-rPl3Il6oHxrGA0XkEANiQ63iBmlE9UjV5UVOJ7IzQ2MupqwV4Wx6NADLnWH40WtkOi1NRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ وینیسیوس و وکلاش برای مذاکره با رئال‌مادرید وارد کمپ این تیم شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102740" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102739">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=QAJkAEDPhyq-kitwqW10MT5MeXQbaC7CWdAdyK_jDsCI1aApQWydWHEiT6lsKWdix-5ixzVp41S5tP3PYYUpxNuut_1UtT70dEUV9YPihBxRXkbdC3ed6v0vF6kzI53WgkCOxdBXhbYioYjX4w7HNQfPyfTyT8w4Rtt59zcBc6AEu3s2WC51sBGAB963ta8FEqIs96sS_OmdJ3ySJ13bQSbVTjLAsyAsR-MYVJZ5Umk0_lVudo1aV7cCSn6m0uyrfzotHHVgsEdB0iC-8N3QaYkoEFeCEF6bP7jEXa-rR_P5Ev9zXuPz7Jqb6-njKcEpYirRlpA1Orje2jJE2zA7YIFmjV9b1PfPYo3Fan5i52zNvZuvb9pn7V42_UpOK6k9BLL044D6bzc7cgprujsuk2Q9Egy1uWJarTp5_7T1Vt9_MRyoWIgwIFJKBSpt1ppg-xQHW9AknekRHXXrGgebyOdI9PT1lc7O-BcIHGV7jFAX8Ju5DoywWc0WCbVuX8WHH04rlA6Huohe_Kyaapq7XDIlb25ZDHEmQFCuxyGoMfaLIDWSpKgw05TL8cPhzRWRhBcfvExSmMn5fpV3jC1qhRJTBzGxMDQyHzt6a6RsfPTEu9FGfU4q-xB_XlWHlJXfsom1DXKoDje9CMdN65GCYoEh4xKjLOdA-8tphbcMk_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=QAJkAEDPhyq-kitwqW10MT5MeXQbaC7CWdAdyK_jDsCI1aApQWydWHEiT6lsKWdix-5ixzVp41S5tP3PYYUpxNuut_1UtT70dEUV9YPihBxRXkbdC3ed6v0vF6kzI53WgkCOxdBXhbYioYjX4w7HNQfPyfTyT8w4Rtt59zcBc6AEu3s2WC51sBGAB963ta8FEqIs96sS_OmdJ3ySJ13bQSbVTjLAsyAsR-MYVJZ5Umk0_lVudo1aV7cCSn6m0uyrfzotHHVgsEdB0iC-8N3QaYkoEFeCEF6bP7jEXa-rR_P5Ev9zXuPz7Jqb6-njKcEpYirRlpA1Orje2jJE2zA7YIFmjV9b1PfPYo3Fan5i52zNvZuvb9pn7V42_UpOK6k9BLL044D6bzc7cgprujsuk2Q9Egy1uWJarTp5_7T1Vt9_MRyoWIgwIFJKBSpt1ppg-xQHW9AknekRHXXrGgebyOdI9PT1lc7O-BcIHGV7jFAX8Ju5DoywWc0WCbVuX8WHH04rlA6Huohe_Kyaapq7XDIlb25ZDHEmQFCuxyGoMfaLIDWSpKgw05TL8cPhzRWRhBcfvExSmMn5fpV3jC1qhRJTBzGxMDQyHzt6a6RsfPTEu9FGfU4q-xB_XlWHlJXfsom1DXKoDje9CMdN65GCYoEh4xKjLOdA-8tphbcMk_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
نیمار دیشب اینجوری بعد برد تیمش برای هواداران رقیب کری خوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102739" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102738">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102738" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102737">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8u4P19EmO30bmjACg9-nPj-srbN3yyH8u45zKzRHh5x6RVIwvtOvLo8tmm19z44UMOZhn8BA0JUcO01oGW0FCS4QLKE8l6bjR0u23tptSWqonmVNKxo-zfJ1XCdEX-MMVih0a0J1TZUACa-OixTyyqpymIaTo6DWcgnlvqjWUz8mGdwV21lL4xSDWYPCO_ndK8wFvLoh6ozspBQbhMQIeRhNX5EHVOUsmMKFGZgk6ASd76ysALLSJ2NB4xElnsGZD_Qsx7BXOsvQlyTclPAIWja1ADNl9WJlT493CbL0ZKOEGzGlfsxKGWlE_w868kknrO9h1H_50_lPrMOlqjPeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102737" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102736">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=eCUdCKM0qaBhPHZARLLVefQ34aR6iE7gHtDYSg1CTsaZj2IxG_6DbWThUu_8CfIlachzio31D2JRqo4hcSZPLdsu1mN6nbZGzgjE2iRmdZjDSk9YRzf6alpOjNgUVmp52DqBhkL7JeS1JbDln5IfwvnpwXD7PSWwdUeWjF7_ZLlMbIyRGwpn92bNGGEUJFD2FosJA6ywY5UuAb-UrhU5sM-XIa5N7w9Ol4Jb6WHdHCal3pY1AMG6omsZn-VdEtS5YEDocoMPQEZJhsRt70b8e9Mn80-uRuIbA-3Q41WOwojbWY_qZtJauSIT3sKLm6HdiW96yP2RZkI0ZV6WUbJrEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=eCUdCKM0qaBhPHZARLLVefQ34aR6iE7gHtDYSg1CTsaZj2IxG_6DbWThUu_8CfIlachzio31D2JRqo4hcSZPLdsu1mN6nbZGzgjE2iRmdZjDSk9YRzf6alpOjNgUVmp52DqBhkL7JeS1JbDln5IfwvnpwXD7PSWwdUeWjF7_ZLlMbIyRGwpn92bNGGEUJFD2FosJA6ywY5UuAb-UrhU5sM-XIa5N7w9Ol4Jb6WHdHCal3pY1AMG6omsZn-VdEtS5YEDocoMPQEZJhsRt70b8e9Mn80-uRuIbA-3Q41WOwojbWY_qZtJauSIT3sKLm6HdiW96yP2RZkI0ZV6WUbJrEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
🔥
نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102736" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102735">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45508d652.mp4?token=YHQ8LaNaLxHRlIrQe0YtznFPa9g2CwIM5MJUJ-Um26kvSOHOSZOMw_DwRhFKZYdXzKSreGJjbRfMlWei8R1baIv85nKc2MoSaVM4-2op4c0hwdP4oVMurKz9gWs_u4khJPG5VbuHpRSjzJ-JNgd4c-PJwHFPAYpIKgWuh0R8nVCu-WJ5ZA2BSEKAS1iY3SiVVQKMdGWoydWASt2k8qBNP-kvyi3lpKcvojrHtd2RDro5kdlqq9TKAfiZESwNntOsnschIRDHWD9GWcZDcpLaZGxOTI-aNBRqbVB9LQF0YMPzEivPyJdqbimHytccNzbJhua9TMnFdGGcgGAE50JZrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45508d652.mp4?token=YHQ8LaNaLxHRlIrQe0YtznFPa9g2CwIM5MJUJ-Um26kvSOHOSZOMw_DwRhFKZYdXzKSreGJjbRfMlWei8R1baIv85nKc2MoSaVM4-2op4c0hwdP4oVMurKz9gWs_u4khJPG5VbuHpRSjzJ-JNgd4c-PJwHFPAYpIKgWuh0R8nVCu-WJ5ZA2BSEKAS1iY3SiVVQKMdGWoydWASt2k8qBNP-kvyi3lpKcvojrHtd2RDro5kdlqq9TKAfiZESwNntOsnschIRDHWD9GWcZDcpLaZGxOTI-aNBRqbVB9LQF0YMPzEivPyJdqbimHytccNzbJhua9TMnFdGGcgGAE50JZrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل مدنظر شما چیه؟
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102735" target="_blank">📅 09:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102734">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puW5RztbDvbWv8dpLkoTIqdkgUAFuSb2gZr_jYhx5RfE_z0Wqjl-X7d-QYPK4L2K511mWPciwpDM04DnvwIsqQ8QHoJfOC_LIEL3fjCpk4d7Y-vF_8pi4DK_Gk7xSSdM61QWa3g-4cgM6YzLu0Ry_uRygQ960eJzygCNFtZfV8SfaQuYcpihIByxz78rOQecX-rwT-_vp9xhI1ad9MQNpAwoOYCCWno_sbch79QYMy3E1hvCVAi0p8agce_nSERiE1iwTkZ0o4vO-npw50PRRrqBQzTDguo7aahNkQO6YvTOyv_jg2orqbhldQ5oz45HVBZwCY88aMO0CqRHI9U3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🗓
روزشمار آغاز رقابت‌های فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102734" target="_blank">📅 09:25 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
