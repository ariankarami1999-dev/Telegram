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
<img src="https://cdn4.telesco.pe/file/C-1Yd3f7YCI70nFMCb8CrNyNgR_Kqjo4pQwP2Rv-5DcuIGy7M0d7aOtoiVGk4JYHUAJlj5N2pATuIQRTOmpfPWCM1-WX4UYTYJuGMXEYIw3yWU7NtVtXkJXMV92Tz1QI6o2uhahxKlMmfdrYqhvgC8YwOc3JrIRmieeVMfvLGTJCIH4FzghrgGCIbxwRJTCuedT7TPSoDBMJN-aCKXGXXfIaQVp-KIqB-fdGR6pqpEN6fD-PV0ly0t6wCXDS4b_vlQhAhAHSX-Czu7XLAZ2i1mWMlPplFDLQgPqAhNLg_ghftyVbjMY-c3BWhhbWtCHbugdwgud16iLL9D3LuMgfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 15:30:20</div>
<hr>

<div class="tg-post" id="msg-81769">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf0fc8628.mp4?token=s9eB24ymKq-JAfSICLMIe7l7rhdZZgFGlNFhMtIa4tStLv3sz0dHgaE1xMdrYiYYuU-a6pj53s07i3Vo6ku2hXJiqoFZw3h2nsfx8raY9dJBeDJv0_jFmptF0nnWLtV93Jg1px7L_5J8zf0MNwTt6trbKNvJSEBD66250ZCQg-2_m--Vo8NUYKZgocxIHGm4qzb-5zkil3ck1GZAGlKZIC9twHtyR7JfCnU05INvfR4Hx-SBCgWxnLyWvSXEJ-49fJIh2wmMFi6GDfTnBEHnuDMQ9gf9BMDYr6z9IOQ1Yfhh0JTtC0GEe_2fUXLLd1n20ViXQSwYBQsnamG4gvxbmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf0fc8628.mp4?token=s9eB24ymKq-JAfSICLMIe7l7rhdZZgFGlNFhMtIa4tStLv3sz0dHgaE1xMdrYiYYuU-a6pj53s07i3Vo6ku2hXJiqoFZw3h2nsfx8raY9dJBeDJv0_jFmptF0nnWLtV93Jg1px7L_5J8zf0MNwTt6trbKNvJSEBD66250ZCQg-2_m--Vo8NUYKZgocxIHGm4qzb-5zkil3ck1GZAGlKZIC9twHtyR7JfCnU05INvfR4Hx-SBCgWxnLyWvSXEJ-49fJIh2wmMFi6GDfTnBEHnuDMQ9gf9BMDYr6z9IOQ1Yfhh0JTtC0GEe_2fUXLLd1n20ViXQSwYBQsnamG4gvxbmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد غفيرة تتوافد الى كربلاء المقدسة للمشاركة في تشييع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/naya_foriraq/81769" target="_blank">📅 15:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81768">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb89f2c55.mp4?token=fOkl8ZLTAJodK5n6jcjme6LAopJ4Vd6QPmf-EssX_InGCfcruKM4GRxnsVqp3O6OoIc_QFrQgM7T_sneCnYlkNsgmIsGBHe6Fwe-20KOdH75gM9XZOfvenmOj-6_b5FUTExAOUKCiTEehf5Khpak_wpUGXQhKoX1Kun4LSxV876USegP6zJYSPdDSVYazT_LpOfDnPXrDBR_tHq3bdE_bHVVtiwlXpaSvfxKvF1ejdW9PuridUfDCJtJK3GMlWzGzeF2Sc6UiSsF5OfAYfzqreP3FJG_8b3bRHrqiaeyDvKPsjBkL4TCeNWzHQ5o20AdyUyHYJAEGj1YMW_XVZT4_44_pfOh-VD8Rt_vtll1LhJXQW1bzUzbTYoVCvmDPCPcfWKnlleVLlWmY4GI9KmxS1EZC6-K55wySJkHgiHGiA_XCth_W6enUJTPb-X1MjiE2azerkilkD25qVONFc1VmXwii-c5dpXVfVlMnA-RcrZ6rEVoV2FkIrtNLowRGBaXM2YcCVG1fxg1O2iyEYQS6N1sLBtL6A_n_0qfNXhLtZVutYUjCCEbPwhYOj-gGWN__WMaEbaEYe16uwvh6LGL7X4Gv36z3VsggxyWY6NH_k6jGZPhh3rVkdUOIyrpJj7FK4vUKZZMZeducAU4aYu6FNhhePrGPA6gk4Hgg4N-LxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb89f2c55.mp4?token=fOkl8ZLTAJodK5n6jcjme6LAopJ4Vd6QPmf-EssX_InGCfcruKM4GRxnsVqp3O6OoIc_QFrQgM7T_sneCnYlkNsgmIsGBHe6Fwe-20KOdH75gM9XZOfvenmOj-6_b5FUTExAOUKCiTEehf5Khpak_wpUGXQhKoX1Kun4LSxV876USegP6zJYSPdDSVYazT_LpOfDnPXrDBR_tHq3bdE_bHVVtiwlXpaSvfxKvF1ejdW9PuridUfDCJtJK3GMlWzGzeF2Sc6UiSsF5OfAYfzqreP3FJG_8b3bRHrqiaeyDvKPsjBkL4TCeNWzHQ5o20AdyUyHYJAEGj1YMW_XVZT4_44_pfOh-VD8Rt_vtll1LhJXQW1bzUzbTYoVCvmDPCPcfWKnlleVLlWmY4GI9KmxS1EZC6-K55wySJkHgiHGiA_XCth_W6enUJTPb-X1MjiE2azerkilkD25qVONFc1VmXwii-c5dpXVfVlMnA-RcrZ6rEVoV2FkIrtNLowRGBaXM2YcCVG1fxg1O2iyEYQS6N1sLBtL6A_n_0qfNXhLtZVutYUjCCEbPwhYOj-gGWN__WMaEbaEYe16uwvh6LGL7X4Gv36z3VsggxyWY6NH_k6jGZPhh3rVkdUOIyrpJj7FK4vUKZZMZeducAU4aYu6FNhhePrGPA6gk4Hgg4N-LxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد غفيرة تتوافد الى كربلاء المقدسة للمشاركة في تشييع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/naya_foriraq/81768" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81767">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الاعلام الغربي عن مصدر: ترامب لم يؤكد إلغاء الاتفاق مع إيران خلال قمة حلف الناتو</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/naya_foriraq/81767" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81766">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">البنك المركزي العراقي: تحديد سقف الحصة النقدية للمسافر البالغ بمبلغ (2000) دولار أمريكي شهرياً بدلاً من (3000) دولار، وذلك في إطار تطوير إدارة عمليات بيع النقد الأجنبي</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/81766" target="_blank">📅 15:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81765">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/613440993d.mp4?token=uDn75JKdbGoRmAweANdeainHcm5Vdwh0nEeF6yr1Tpniz_SK39cfsf41-MKlANIvlMzbiAbH9BFIMPwUftvmXCE7F6FnsNj8LHCFJR1NXzng2nXVBf7Q7xVB73v2_rLr7SRCFkX3QI30E6MGPMS0t3idSA6PVVQcDNVZZ1ONo7-tnb8Hw3DrmlMlpcbnKHbfTjvToo2GTWikzd4UnDafNY0eeXllDXKHKfsJzrwdffNV-lOzhRNlXZ47q2KC34Ro7NikdG9gBNY21hZGYQOpqKXapPNWyufhKP-IJmQhnueS9WoYVzYFt_SdswYgT2fT6CMtlQG-xx4ZQhjzdPD284WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/613440993d.mp4?token=uDn75JKdbGoRmAweANdeainHcm5Vdwh0nEeF6yr1Tpniz_SK39cfsf41-MKlANIvlMzbiAbH9BFIMPwUftvmXCE7F6FnsNj8LHCFJR1NXzng2nXVBf7Q7xVB73v2_rLr7SRCFkX3QI30E6MGPMS0t3idSA6PVVQcDNVZZ1ONo7-tnb8Hw3DrmlMlpcbnKHbfTjvToo2GTWikzd4UnDafNY0eeXllDXKHKfsJzrwdffNV-lOzhRNlXZ47q2KC34Ro7NikdG9gBNY21hZGYQOpqKXapPNWyufhKP-IJmQhnueS9WoYVzYFt_SdswYgT2fT6CMtlQG-xx4ZQhjzdPD284WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد حاشدة في محافظة كربلاء المقدسة تنتظر وصول الجثمان الطاهر للسيد القائد</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/naya_foriraq/81765" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81764">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a42e7b63.mp4?token=QG-jjGpj-hmUKYFdelHlHtsugk3oJKkunOOLlOe16Hjm9m0aKfnbVVzD5x4OS1xZqfydYCQcG6DQqAcvHjzv8zoRYyjFWyXw0Qs864xx_WbLqcNAm1WaSLFnm2_SCmKpDZdufoteapGTDMJ7EwQm5_4D_kG87ko4Urz5WjPZ6ewg3HjhcCcGINnNZlmEP4F9SH_oFrSsAoEpV27LSsuMjGM1AhFcsTMJOmR79Vb1fZZwKtObrSg0Zpr5XMqi_SFBLJdhJsD3YpyyjPHZEH38X0zXCwCi5E7ZxNx76_v5HNgCzUmEGxpcKXtXXLnIsbdoHmru4KLh3unhoTKgu4D_6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a42e7b63.mp4?token=QG-jjGpj-hmUKYFdelHlHtsugk3oJKkunOOLlOe16Hjm9m0aKfnbVVzD5x4OS1xZqfydYCQcG6DQqAcvHjzv8zoRYyjFWyXw0Qs864xx_WbLqcNAm1WaSLFnm2_SCmKpDZdufoteapGTDMJ7EwQm5_4D_kG87ko4Urz5WjPZ6ewg3HjhcCcGINnNZlmEP4F9SH_oFrSsAoEpV27LSsuMjGM1AhFcsTMJOmR79Vb1fZZwKtObrSg0Zpr5XMqi_SFBLJdhJsD3YpyyjPHZEH38X0zXCwCi5E7ZxNx76_v5HNgCzUmEGxpcKXtXXLnIsbdoHmru4KLh3unhoTKgu4D_6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد عمليات الفرات الأوسط حشد شعبي اللواء علي الحمداني يوجه نداء لقطعات كربلاء المقدسة استعداداً لاستقبال النعش الطاهر</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/naya_foriraq/81764" target="_blank">📅 15:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81763">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طريق تشيع السيد القائد للتوضيح في محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/naya_foriraq/81763" target="_blank">📅 14:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81762">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دويلة البحرين: تصدينا واعترضنا عددا من الاعتداءات الجوية الإيرانية الغادرة</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/81762" target="_blank">📅 14:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81761">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49d1f85a2.mp4?token=SZLTSA66RyIHNsfggOOXX-9witX3GQgYA8bQx8jB9oDmQlpdE_QU7WYC1J5oEtFO7AAenxOxJwbtXfDxE-JAsVzzysfFg9tGjhAo4JDLFcxPH1XkZD7AsgC5jER4D3E0FzgDqu9KNH2iN5caR7L-_TxeszRdv22d45OotVGHIkPu_B8q9bZ74ZyFvqaLJWnTnDVBygURXPIZTtjrPXFvtYC_Gma-iiUbdnQWZMsdB0eM3vWURbxPza83CrFx8PuCN-wpligLQ8ORcMQSCzLcDVo_WybLrjQreO0j3NqJQ1HTT7hHPbCMdXTCug1wuYVqfegRd6F7jTSMZP71LYTEWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49d1f85a2.mp4?token=SZLTSA66RyIHNsfggOOXX-9witX3GQgYA8bQx8jB9oDmQlpdE_QU7WYC1J5oEtFO7AAenxOxJwbtXfDxE-JAsVzzysfFg9tGjhAo4JDLFcxPH1XkZD7AsgC5jER4D3E0FzgDqu9KNH2iN5caR7L-_TxeszRdv22d45OotVGHIkPu_B8q9bZ74ZyFvqaLJWnTnDVBygURXPIZTtjrPXFvtYC_Gma-iiUbdnQWZMsdB0eM3vWURbxPza83CrFx8PuCN-wpligLQ8ORcMQSCzLcDVo_WybLrjQreO0j3NqJQ1HTT7hHPbCMdXTCug1wuYVqfegRd6F7jTSMZP71LYTEWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لكتائب سيد الشهداء الحاج أبو آلاء الولائي يصل إلى المراقد المقدّسة في كربلاء المقدّسة للمشاركة في مراسم تشييع الإمام الشهيد السيد علي الخامنئي قدّس سرّه</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/naya_foriraq/81761" target="_blank">📅 14:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81760">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">منطقة بين الحرمين الشريفين في كربلاء تضج باهازيج العراقيين قبيل وصول الجثمان الطاهر لقائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/naya_foriraq/81760" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81757">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeKH_sEHvtQjIU2p-u7WHiGcemQmD6zXIliznQ60CiONGKY8HISc-JpgMkoweod-izPHkNUImTUCcgSXg0_wrAo98xw06_N-y335ScJm75enG9v74N7yr7Ixfcx3_ZB7z3F1MJjUgKc0fCXvERGLIhyUe9xnKoewX4-5IjUfZH-_UQ3rZxPTe-8Qu1sCHbdxYjUGabuuMqE0YT84MO-hSlLNYD2O1IQT72XxxEcIxgJwaCxNck8iAbu5V2PYxdgml0lfCt6MkyUl8LOPTvAByZa-MWvx0DW1bBiWpgPJACJlse-k2GUP9vL9h8vmweosSq0fa-JB51pARWBaA_0scw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDhMoJ0FB7XWri5U2fFpWYMjHsPFFtTRSDC3DWrhBeuUCgyAC91WaXxuUSfCCTFtdvP7WsN3kpnNoMxT8YEZVfqse1OlNkDgcDWSr0-IRDfEG6UGTTVZv-bhX7VGDMK-KA9g6jaaIizJxhLr4AmdP6Lkt7aX4HLfOOG7ssoZpaeSWFWd8EzH0mAYl0E4JnStGxjqmPd5qLMP5r-dFazuLgxnF3EAvM3L6VvbwQyk4gW5EIBbusGiSvf91ZOSuESkk-HrQyIluU5ceQt1DO1V2GPjsVVPYi-xXF6MA7THKphkSw1Mk6JwaxDSYp36Ah42zGKatePbVmZOfA0wtdbSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9vp9tnUif2Dhze2WERuwOfdQbQcPtcb34phgOgogiuIkPckx1ZsXc-pvP5yivSHsmxE47CdHgVfVfIVvCfTC-9cpbW2U0oEvSMFmIorF5MANxHHFYdIDDVXB5VtKoRzde1sgwYUij01CV4svbuQ4wiKADkXrGiM0i901ZZw4dk-e_uL9mc3V0BFZp02hYPYQy0xTqeGzAoF8mLTzz5NUAMG7wHJcGgobt2FkHWhdAe3M3Sjjq6KXqorBpC79jJRyoRVzSe2Ul9cdzdcfc_O_0r1biFIk-11DT7amDFWTGLUTZO66wp7TSFiFL8ivK8SH68-sbHj1zBy2wlMRlFK7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور من عدسة مسيرة
خاص نايا _ تشيع السيد القائد 2026</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/81757" target="_blank">📅 14:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81756">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64551946c5.mp4?token=eqVDl51MENcmF2p4DO_-tgN8IzzLtIxh4mANhMN64KEe9KnAEAsHB6z8R1XfCeXWfIbtriHhNEKwkVTMUTwc3XpGNcyTjaBcv0UfymKhfY7zRtMeAhPOSG9namrk_OMApUPZfkO3itjokxEa-4_nyvblyM0zGtNjxIt9H9YQNsBglFeWFR3haS3hTi3WTMhM3Xx02p1xntypXlUmDkuK5aOwu-ESQ3-2zjvp3HonpvP-h_UA2Goe6qEhHYx3a76Fu_ApTYdfwqCV06atYlBobHJoRO5w5fGBgBRcjVcDhTq-TNzTu4wKaqN5dGSR8BCOGjKa81B2RVnoic_nzfaCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64551946c5.mp4?token=eqVDl51MENcmF2p4DO_-tgN8IzzLtIxh4mANhMN64KEe9KnAEAsHB6z8R1XfCeXWfIbtriHhNEKwkVTMUTwc3XpGNcyTjaBcv0UfymKhfY7zRtMeAhPOSG9namrk_OMApUPZfkO3itjokxEa-4_nyvblyM0zGtNjxIt9H9YQNsBglFeWFR3haS3hTi3WTMhM3Xx02p1xntypXlUmDkuK5aOwu-ESQ3-2zjvp3HonpvP-h_UA2Goe6qEhHYx3a76Fu_ApTYdfwqCV06atYlBobHJoRO5w5fGBgBRcjVcDhTq-TNzTu4wKaqN5dGSR8BCOGjKa81B2RVnoic_nzfaCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لكتائب سيد الشهداء الحاج أبو آلاء الولائي يصل إلى المراقد المقدّسة في كربلاء المقدّسة للمشاركة في مراسم تشييع الإمام الشهيد السيد علي الخامنئي قدّس سرّه</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/81756" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81755">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a2f95c28.mp4?token=gC41a6XUB2exkYhshfZTeLbNYhHhlMpORH7fRBDxNvVeDyVtNR08mQMZaNxyFz8Y7DKyG-mxMfoVfjXtb49XangzaPmPTDslBMwmyQUBnos_mZ1iYeNGmUBMNhw6w1NoA0G9CrN0AxLiGAIuGXe6itU3NxPWOol2TGXfcSS6z7_qkX2zAYv4MXzwW2WO6h4tM9WhDQnlhEfOKvYbF7wm8sOMeL67EzNhzerJ8tt6rsbLi3wVAEjnkKjnNw_w1M_Wfl522wnwxeb_gH3b7-MFzCMHdMEgPET_88PfeFII3xdHDnsBOUSePhSD8up_C38vB8SfA-HAom4FK2zFTx52Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a2f95c28.mp4?token=gC41a6XUB2exkYhshfZTeLbNYhHhlMpORH7fRBDxNvVeDyVtNR08mQMZaNxyFz8Y7DKyG-mxMfoVfjXtb49XangzaPmPTDslBMwmyQUBnos_mZ1iYeNGmUBMNhw6w1NoA0G9CrN0AxLiGAIuGXe6itU3NxPWOol2TGXfcSS6z7_qkX2zAYv4MXzwW2WO6h4tM9WhDQnlhEfOKvYbF7wm8sOMeL67EzNhzerJ8tt6rsbLi3wVAEjnkKjnNw_w1M_Wfl522wnwxeb_gH3b7-MFzCMHdMEgPET_88PfeFII3xdHDnsBOUSePhSD8up_C38vB8SfA-HAom4FK2zFTx52Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشائر خان النص بانتظار نعش السيد الشهيد في طريق نجف كربلاء علما ان درجة الحرارة تتجاوز ٤٥ سليزية</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/81755" target="_blank">📅 14:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81752">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQDqYXKLqW6HbELMh1P8ByyduYVCVZssQ57Kyz6yrE8h6XQV5i-z0hha2f0rwndSKlojA3dlI6oqLRmaCfKt7AKMbej9GIML9e-LVAHN8AvozlJ16Ctac1DeufunhnFOaoSNGGi_OndKnI1zcbo2AEpuvC6B-2rmpbjUTWNdtYe9eTO4cy-ADDHxBA1CzWoAwfectMbBshRxmlQ1B2ezYOjDZ8SfeBdUa_qUJZzbjYgLVbfaodTh-LSIZEBH_fV29hhVcrTs2DzrRQTgAA3WwLrmOqMaiznfp-CKBzop2yle0TfD_grMv5e747-qNWZ7FtvE8wbcsnHHbt6LmesROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tjfDA-Eo_akXKz0_Jq9TlTWw3ifr4-f1dSVCQF6OgZlE5AuW3pClDnAUeySDRrq-ggu_yEos3CTo1vDLYdBmXv3ckara1FkSifbZNZdNoVJWmSUsl_ysz2zhkohXM89nGozti_NsXTHGMxg2MtV0b7c9jBLes0Q9TR71soVC-4RfuQGvnlbVG2mVenaHGSro_Fli3XR2IW6zFIP9IfluoeJSgz02VPmD9QBoVbulK3Ur4PrwQZkYoWvu4YZjtbK0bBBK7JgHv0pTXSplhQLo3552Vc_C6d6miCUsrPBLhBQGFhpjMGujRCYwoFv4bh4IU1bK2bR2UTfERhlY2GajgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTthO201aJvR7sWyMoK0nXf9ddZwz7LXsUTWNGW5n8AksG2EvMmdWilZf8OBwhqZBofRVhUAxmXV9l2TSVWEHUFeFDMvFEUmXh0t-ki1bJnGSKBZzcTeLoJSMA7cBX8unj73J0CDvIZXhxhNlZVMxPOzy5qVrZDa3CJ_Lhcxndd9grNRLy7z-aXzgmrBBNg4sbRrvRuq2L1uqp1nDNUqYuwRiqGSUkrwv2U7IpSKfV-tJE4vcc9p0Su8NyayeNGNBFtlP4EuT5GqKb25HfPkqpaSOqP1YGb8BdJiyqLgjanjl1ZW1YqIZAL82-X3QyrM6f6nZTtA2iuIPlKfrbY-sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Inside Hthrat imam Ali drone Picture Mavic 4
Naya team</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/naya_foriraq/81752" target="_blank">📅 14:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81751">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Naya drone over Alnajif city
1:00 Baghdad time
8 July 2026</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/naya_foriraq/81751" target="_blank">📅 14:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81750">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30da01e5e6.mp4?token=ZAE3zTBjcljRtk_5wT00aiByneGCySgyx1cXp6HC7Paaaq3IHXvaVMY4xyYSzLRr3JA-kSQUzHXvaBS68vlqZN9sMlFZ4ic1i3UL0xn6OPpOCMZ-9ShgRlmfX3I85Hn4qWa1KHaAU2vRJZXjDXLiSWmpJI_K-VyAYaN2IR5ZIhWKZtKPVf0y0TvLrqnPXhMaAu7QrHrYDSyZlA5f0EWcnqwJVl9DckKuMtbYjSarQSV-FvW3u-Y8rcp1DKlhvUfHw9tuQT3QC3GyB8sEzpvPCMrszRmj9S2HF32ZcNmluyNvYd8Jog8GJQAvTDz_2lcu29eRQ1NUZHolOvq6qDAVMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30da01e5e6.mp4?token=ZAE3zTBjcljRtk_5wT00aiByneGCySgyx1cXp6HC7Paaaq3IHXvaVMY4xyYSzLRr3JA-kSQUzHXvaBS68vlqZN9sMlFZ4ic1i3UL0xn6OPpOCMZ-9ShgRlmfX3I85Hn4qWa1KHaAU2vRJZXjDXLiSWmpJI_K-VyAYaN2IR5ZIhWKZtKPVf0y0TvLrqnPXhMaAu7QrHrYDSyZlA5f0EWcnqwJVl9DckKuMtbYjSarQSV-FvW3u-Y8rcp1DKlhvUfHw9tuQT3QC3GyB8sEzpvPCMrszRmj9S2HF32ZcNmluyNvYd8Jog8GJQAvTDz_2lcu29eRQ1NUZHolOvq6qDAVMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرس الثورة الاسلامية ينشر مشاهد من الرد الايراني على المصالح الامريكية فجر اليوم</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/81750" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81749">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‏المنظمة البحرية الدولية: 6000 بحار ما زالوا عالقين في مضيق هرمز</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/81749" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81748">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">كربلاء المقدسة تستعد لاحتضان الجثمان الطاهر للقائد للشهيد للثورة الاسلامية</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/naya_foriraq/81748" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81747">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اللهم إنا لا نعلم عنه إلا خيرًا.
مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد آية الله العظمى السيد علي الخامنئي بامامة العلامة آية الله السيد محمد تقي الحكيم في حرم الإمام علي بن أبي طالب عليه السلام.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81747" target="_blank">📅 13:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81746">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dd49b252.mp4?token=aAORy2QB-wt0tM_qh-UVn-mU7ToN_bAGIqeOX97_fFAVfnjtsYv4yrUxzEXhHAh2QPG9qoPr92QKHheGWHXCG-flXgL1XQXtFVnM6OyeR7zqnjqThCvpIbgdj1Mqknsf2u2geID0aVQfrWWyIJxFIswyhPnFG8Q2Ab-bkonS4aUuc8_U1h6GfGu-_7lmMDWUZSVNJh422f5Htm0Dmy7Fn-mCIxh_W6Kn50ZFAWSar7k621N41hBgBGimEP2IAZ8_0rTfgNffIqLiXYAkKJlgfUGBhHN5J-_HaSSkuuxcCpRfCmVeCLMbcgoL-dZpvrCVHICqTuQGio3b-ns26N_Fk0c-Cizb7GLhv4mCWQLopEj78yGW8niTnD72WSUnXng3x-V5h_NVffV_iU55O2jFE8EnO2r4dMHZHL8TU10hNb0pQBPWH8BouNsqgcar_iU7WP5k1soxxqRjSO4ASwD36QFbMnlSbZsxmY6SjaW2jbNSzwantTAh6jxeTggTLuf5ZExwGAO-PM_jdLImmci2O5pcqqgRESqhFQPDmwRiU5u44JvY86kkkIE4PWY-doFAL0UHJ_ZfbPV1LEi0Vadxwjb2f-xrk0vboB1MI6A8KJMhuVLuYl3lfoprtx6-YJlLM1v8wynhlQC3Zjxd6DS97dEBlcyliDntMbzAAGqfC-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dd49b252.mp4?token=aAORy2QB-wt0tM_qh-UVn-mU7ToN_bAGIqeOX97_fFAVfnjtsYv4yrUxzEXhHAh2QPG9qoPr92QKHheGWHXCG-flXgL1XQXtFVnM6OyeR7zqnjqThCvpIbgdj1Mqknsf2u2geID0aVQfrWWyIJxFIswyhPnFG8Q2Ab-bkonS4aUuc8_U1h6GfGu-_7lmMDWUZSVNJh422f5Htm0Dmy7Fn-mCIxh_W6Kn50ZFAWSar7k621N41hBgBGimEP2IAZ8_0rTfgNffIqLiXYAkKJlgfUGBhHN5J-_HaSSkuuxcCpRfCmVeCLMbcgoL-dZpvrCVHICqTuQGio3b-ns26N_Fk0c-Cizb7GLhv4mCWQLopEj78yGW8niTnD72WSUnXng3x-V5h_NVffV_iU55O2jFE8EnO2r4dMHZHL8TU10hNb0pQBPWH8BouNsqgcar_iU7WP5k1soxxqRjSO4ASwD36QFbMnlSbZsxmY6SjaW2jbNSzwantTAh6jxeTggTLuf5ZExwGAO-PM_jdLImmci2O5pcqqgRESqhFQPDmwRiU5u44JvY86kkkIE4PWY-doFAL0UHJ_ZfbPV1LEi0Vadxwjb2f-xrk0vboB1MI6A8KJMhuVLuYl3lfoprtx6-YJlLM1v8wynhlQC3Zjxd6DS97dEBlcyliDntMbzAAGqfC-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش القائد الشهيد يتجه لضريح الامام علي (ع)</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81746" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81745">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📰
‏
رويترز:
هجوم بمسيرة على ناقلة نفط لشيفرون الأميركية في البحر الأسود</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81745" target="_blank">📅 13:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81744">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نعش القائد الشهيد يتجه لضريح الامام علي (ع)</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81744" target="_blank">📅 13:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81743">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انتهاء مراسم تشييع السيد الشهيد علي الخامنئي في النجف الأشرف</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81743" target="_blank">📅 13:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81742">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGWeGzS6BJFqLa9AlrHmgZZY0A1Ljaw27Bw_3x1xh48Ptq5JFV0QJQRWh8HaxC3sVUXMmX1cKLV_GJ0bYsSDeF8PwRXLJh_wzUnVZ46T2O5r6cZMb_PuWjtw4vYNx4CwQhNeyrQ6GTOzRlMips6UykMANN81BTA0e4EuhUQtOAaJnmURedJH7xWCjCHbfepVqk9vy5kYFrsqQCo8DqHcjex2SA2bRSQUye1rIY8Zbln_AIYI45qed9QrO6nvcMvVXKeUw0KCJRHgqr8BMz_W3eTLe0vdDxWmPg6v0_mahZhUrVP_IYb15ftytJOTHQUSbws-qm9SHkKf8vSRdR5AcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
النائب الاول للرئيس الايراني:
التشييع المهيب لجثمان الإمام الشهيد في النجف وكربلاء، هو رمز لامع للأخوة والروابط الثقافية والدينية العميقة بين شعبي إيران والعراق. أتقدم من أعماق قلبي بالشكر إلى المراجع العظام، والعلماء، والطوائف الشريفة، والمجموعات والتجمعات الشعبية، والحكومة العراقية الموقرة على هذا الاستقبال المهيب. هذا الرابط المقدس لا يمكن أن ينقطع.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81742" target="_blank">📅 13:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81741">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03147dbc51.mp4?token=efRpTbfciUYY--rkULQsWh3OXpyGW1YVp9wCfxjIc8zd-qx6TT2Mb-jAdaeD0gJ7XLeAd8jCjZ-2n61KmGb_V31zxb9QLgXE6nIbpR3m1s6mb2Ks1TBPK66dMYsYPt0Nkc0VaslgWd_EXUPGT0eEKnApUXvAASewPnzrkPwF3PWZZyyYyThKrhsMJdK5fZlBPmoDomGHXRmA7hVKXC6_oXFCGBWhbv7UzHsQ2TU7oNC79Rq-QbWdt3u2xXlZdncEieQRpywyQNmGdwpG1gxgBoft214boHuzUd_6XrtYigBVNw-BxWX89494O3qLY9mrcj2BfT8nBJAtmoDkjcEz1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03147dbc51.mp4?token=efRpTbfciUYY--rkULQsWh3OXpyGW1YVp9wCfxjIc8zd-qx6TT2Mb-jAdaeD0gJ7XLeAd8jCjZ-2n61KmGb_V31zxb9QLgXE6nIbpR3m1s6mb2Ks1TBPK66dMYsYPt0Nkc0VaslgWd_EXUPGT0eEKnApUXvAASewPnzrkPwF3PWZZyyYyThKrhsMJdK5fZlBPmoDomGHXRmA7hVKXC6_oXFCGBWhbv7UzHsQ2TU7oNC79Rq-QbWdt3u2xXlZdncEieQRpywyQNmGdwpG1gxgBoft214boHuzUd_6XrtYigBVNw-BxWX89494O3qLY9mrcj2BfT8nBJAtmoDkjcEz1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هتافات الموت لامريكا تهز الحرم العلوي المطهر</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81741" target="_blank">📅 13:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81740">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11479656a.mp4?token=vJsGGuoNRGp7DycfJN2lgC2RCZTIfBd7jgDq2sR6DflnZVW-OXIJn8LGcwhjjFrUXJp2Nk5RNeVXlwkalGxu__9b968cxfUeR4KZA95t92Tc84ek73vl6m0BHTUPvisl1SMKzOhh5XPnSLKqnGF31k0S9SqZ0zr8lwdY2evEdTATgDNjZ4U_6JdyXjxQuZnZ9zWB1uZB5ny6OfvfjWVxa_p9eDQyfVL9tarAqYxIe757KYWWUD4b8ISG_KtVmN3chUrVm_3WHsEmdFxwt_lmszH3DILyCOLJOr9pyGtcMdbIYoRWKYU1vatE3AkGoEYTkKE8jwGDTAfDIndVOzrO7EJai9KMqspfnuOaO1Xlp08v3dz1k3NH4-pi_I_86M87aDAWa8rp540_-yEDkF3Btdn87HA9cmRTCs0gsvWzE8bx8UeKZpJtCZrr6clhsFym_VZXOtKbqcy9xt9OcEdKqj9tuPoBRa4axBoiBrNkqZmenjC4GKHvChX8qPXpsux39nJKRkq35WIcewQTu4Tj9yejP2OIB8lPPftYeAravL2gIY9mROQ7lBz7sXETOB_ynMGxz-_ScXQMix5WPmCXbyhewgLZsPO9fKTOLeYM3ORYHj-7qcGRKyrRslB0xaPcFR3sQeHDUWcO5QhE2g7P8fZABrg9RBdpcKMz2kjyqX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11479656a.mp4?token=vJsGGuoNRGp7DycfJN2lgC2RCZTIfBd7jgDq2sR6DflnZVW-OXIJn8LGcwhjjFrUXJp2Nk5RNeVXlwkalGxu__9b968cxfUeR4KZA95t92Tc84ek73vl6m0BHTUPvisl1SMKzOhh5XPnSLKqnGF31k0S9SqZ0zr8lwdY2evEdTATgDNjZ4U_6JdyXjxQuZnZ9zWB1uZB5ny6OfvfjWVxa_p9eDQyfVL9tarAqYxIe757KYWWUD4b8ISG_KtVmN3chUrVm_3WHsEmdFxwt_lmszH3DILyCOLJOr9pyGtcMdbIYoRWKYU1vatE3AkGoEYTkKE8jwGDTAfDIndVOzrO7EJai9KMqspfnuOaO1Xlp08v3dz1k3NH4-pi_I_86M87aDAWa8rp540_-yEDkF3Btdn87HA9cmRTCs0gsvWzE8bx8UeKZpJtCZrr6clhsFym_VZXOtKbqcy9xt9OcEdKqj9tuPoBRa4axBoiBrNkqZmenjC4GKHvChX8qPXpsux39nJKRkq35WIcewQTu4Tj9yejP2OIB8lPPftYeAravL2gIY9mROQ7lBz7sXETOB_ynMGxz-_ScXQMix5WPmCXbyhewgLZsPO9fKTOLeYM3ORYHj-7qcGRKyrRslB0xaPcFR3sQeHDUWcO5QhE2g7P8fZABrg9RBdpcKMz2kjyqX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبيك يا علي
الجثمان الطاهر يزور مرقد علي ابن ابي طالب</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81740" target="_blank">📅 13:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81739">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7f-eChNe-gk10uFKU9fyDLApNLQlcJgSXpjqYX9E1tb__Z48_K9RzfcOnzrtx1WyAPPrHTCyTnedtGZsrM2xYzYsB3AskyJ_gvQwJyaHw704gqmaV1Ljs0ZOjighHYYgoT89L7qEgyzCZhfHbpNJJ2mnyXT-MW3Juw8c1Sbd4lhcXxmT4zQobKAmpKqLeZvoh-R5enNWlNTiYvjrJlY9x7sgt83jWz6kall4ee_xoRJW9u70s1vux-UIewX0knIqS6k9Cg8ajDPY19l7gysAD7y5em4lQtBGibc-JakQma7OyRUGSAzTdn2diE_i2710VamVzfNVNIiHV9SdwGoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجثمان الطاهر للسيد الولي الشهيد يدخل مقام الإمام علي</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81739" target="_blank">📅 13:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81738">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">علماء حوزة النجف العلمية يتوافدون الى الحرم العلوي لاقامة صلاة الجنازة على جثمان قائد الثورة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81738" target="_blank">📅 13:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81737">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0bba8588.mp4?token=VMIIE4s0k820koL_hSM0aL8Rtj95-RgO84pXFspaCDbNnPow3TcE-wbhFSz9jkLQa0NrvWkexzKqAAxPNHSZUD6oUgxaeQ7TY8M8uvCW8i2u-UQtxvZj_ubGl5ndToJhq9unHNQYrvzYHh122gpXopqeWO9TiZmQvA1tmzayJoUuCuLElOissblhK4eDrIyQyVP0-ubtP85IcNNCaMxUr2zdKO03jwzsvTRKqQOCqLsd7KGAtAfZICeJZi5OQUi2mHAumsYJzkWKe5UyrvyybzDtbM3ORKmNsEyyfByzbq86uwA-keV4VyPC6-gTTzxqgpdXy9bDJY2bg7vWWq5S0yebnRftrYKRwT1XCkk-pd4qi6FJb8PJoSnlTwufmtUcbZsOYOisUG12PmFZ2VBruOgjN71wjSlGucmKA_jwo9Aj6s7hLfqCFYYA1VPxfz2P1CZYEkqmtBROFVGhOU3KoVtLuSjd4R21SFFSqhFtq5-nRO8r2NMe3pUgfLnNmMxXTg3i-qoGIvLdkFiNPBBYJUrKZ5L1auPaFs3cA1Py-hRIp6b6f61Wz0xhy6WxD8_d1hv9ZLsknfRPNhVemWTbXAFX2J9EKpLDVO2mZsWz6w7K2ioMRVlPwuf_7TBxeBu1GZyvsLsxREpAosHJYjzhllFGnSS7Smt4rys9QcYbuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0bba8588.mp4?token=VMIIE4s0k820koL_hSM0aL8Rtj95-RgO84pXFspaCDbNnPow3TcE-wbhFSz9jkLQa0NrvWkexzKqAAxPNHSZUD6oUgxaeQ7TY8M8uvCW8i2u-UQtxvZj_ubGl5ndToJhq9unHNQYrvzYHh122gpXopqeWO9TiZmQvA1tmzayJoUuCuLElOissblhK4eDrIyQyVP0-ubtP85IcNNCaMxUr2zdKO03jwzsvTRKqQOCqLsd7KGAtAfZICeJZi5OQUi2mHAumsYJzkWKe5UyrvyybzDtbM3ORKmNsEyyfByzbq86uwA-keV4VyPC6-gTTzxqgpdXy9bDJY2bg7vWWq5S0yebnRftrYKRwT1XCkk-pd4qi6FJb8PJoSnlTwufmtUcbZsOYOisUG12PmFZ2VBruOgjN71wjSlGucmKA_jwo9Aj6s7hLfqCFYYA1VPxfz2P1CZYEkqmtBROFVGhOU3KoVtLuSjd4R21SFFSqhFtq5-nRO8r2NMe3pUgfLnNmMxXTg3i-qoGIvLdkFiNPBBYJUrKZ5L1auPaFs3cA1Py-hRIp6b6f61Wz0xhy6WxD8_d1hv9ZLsknfRPNhVemWTbXAFX2J9EKpLDVO2mZsWz6w7K2ioMRVlPwuf_7TBxeBu1GZyvsLsxREpAosHJYjzhllFGnSS7Smt4rys9QcYbuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء إقامة الصلاة على جثمان القائد الشهيد السيد علي خامنئي في حرم الإمام علي في النجف الأشرف</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81737" target="_blank">📅 13:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81736">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مشاهد من تشييع جثمان قائد الثورة الاسلامية الشهيد داخل حرم امير المؤمنين</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81736" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81735">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c82fc0f43.mp4?token=dHgQDUnbupLhWEQPj0bs4KHr_3kqO46WvdftfNEPOIy-_P2bOCjG-PYzMRZNDyyGJApSrtfg46S643tiXvFD646PFfuqz4L5No-nqO9sO6SLT3Vk5e3I3MJpJFvUnQ9kZh1fnNZM3iuCGmgnProHyeUfWwGNT4Y1rA0MLIkUOEyZY2jlWIp2xlysd-Pmja-dwlPrYXU6YkX623MFd3gk0hOKxDmINOAW8bKVQvlWs9EaX4Ifdx2A0Q04Gb_hfaN18YmDphbkX3o29sUSaCeK0s55MmqZ6Vsvbz2CxsOWzgeHlx2uXSw-KEBK-OY1Lb8_R_MTrVzUmM8z-XuU7bxSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c82fc0f43.mp4?token=dHgQDUnbupLhWEQPj0bs4KHr_3kqO46WvdftfNEPOIy-_P2bOCjG-PYzMRZNDyyGJApSrtfg46S643tiXvFD646PFfuqz4L5No-nqO9sO6SLT3Vk5e3I3MJpJFvUnQ9kZh1fnNZM3iuCGmgnProHyeUfWwGNT4Y1rA0MLIkUOEyZY2jlWIp2xlysd-Pmja-dwlPrYXU6YkX623MFd3gk0hOKxDmINOAW8bKVQvlWs9EaX4Ifdx2A0Q04Gb_hfaN18YmDphbkX3o29sUSaCeK0s55MmqZ6Vsvbz2CxsOWzgeHlx2uXSw-KEBK-OY1Lb8_R_MTrVzUmM8z-XuU7bxSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان القائد الشهيد محمولا على الاكتف في حرم امير المؤمنين (ع)</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81735" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81734">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72ee1425a.mp4?token=INnpTqf0dABMz-PtFtAooIEnBq1cO0Mo6jd_s1FCWAYmbMD2kN8vgPdNFmYlWGUAGwmYnSQk8NkHh1-DvGbGPWPDRm-mBSRByaeOmwVwA0D1CzS2oeKuB_LEgie2q9X15ct0-wzvAqgx5I8RPnhtCQpB0r5nhGSSjvNG2Gu4sh3SqFVSVS33nLx-kgQ8Et5wi6Aw2IxU1CDI-I7a4HZKyUA0fHlZSSqeSbL21sBH0_CLoraGhkx6dhkvUmfW0aY9UFdSzbmni3G2zo2ambORqzzCDT15xUlbryUhHbsjo6eiAtOmPGq41s0MPMSO-asw8waU6AzPPAMc7hOF2eSSpw1Q0jpUFk2Cbb6Q0rrlrbPptPk29jQyQP8swcEd61DXmsSOxK80pJ7JuJAJ3NeOn9FETJBtzswZz5yo5Fx-ZKxd0_j1ppsskWkSc00gcjR9Mlc2rDXwx7C3wNoF_dL49DV7NzfzGIIN5MIlzo6y8qTku3oMYMccyIgK7XKg9xTotXPuI4BIG3nBGd2cHkRDQboDHnQuN3Vtx0Pvq4vd0zYTsDNEA_jXDpApAeVOpjIoOOdvxQkKDvtArBJSZ5SkLBJdzWmsX24xF-HtoRvhBx8BG1fhnbTumyzC1VYcRiY6kPgiFzass0G7b9-edQAS_T0CFrsyAuhrZLlYiED4XTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72ee1425a.mp4?token=INnpTqf0dABMz-PtFtAooIEnBq1cO0Mo6jd_s1FCWAYmbMD2kN8vgPdNFmYlWGUAGwmYnSQk8NkHh1-DvGbGPWPDRm-mBSRByaeOmwVwA0D1CzS2oeKuB_LEgie2q9X15ct0-wzvAqgx5I8RPnhtCQpB0r5nhGSSjvNG2Gu4sh3SqFVSVS33nLx-kgQ8Et5wi6Aw2IxU1CDI-I7a4HZKyUA0fHlZSSqeSbL21sBH0_CLoraGhkx6dhkvUmfW0aY9UFdSzbmni3G2zo2ambORqzzCDT15xUlbryUhHbsjo6eiAtOmPGq41s0MPMSO-asw8waU6AzPPAMc7hOF2eSSpw1Q0jpUFk2Cbb6Q0rrlrbPptPk29jQyQP8swcEd61DXmsSOxK80pJ7JuJAJ3NeOn9FETJBtzswZz5yo5Fx-ZKxd0_j1ppsskWkSc00gcjR9Mlc2rDXwx7C3wNoF_dL49DV7NzfzGIIN5MIlzo6y8qTku3oMYMccyIgK7XKg9xTotXPuI4BIG3nBGd2cHkRDQboDHnQuN3Vtx0Pvq4vd0zYTsDNEA_jXDpApAeVOpjIoOOdvxQkKDvtArBJSZ5SkLBJdzWmsX24xF-HtoRvhBx8BG1fhnbTumyzC1VYcRiY6kPgiFzass0G7b9-edQAS_T0CFrsyAuhrZLlYiED4XTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش القائد الشهيد يدخل مرقد الامام علي (ع)</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81734" target="_blank">📅 12:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81733">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b245887808.mp4?token=UBCAnTmx58r9c1revJSqkFoHVmUxtq2vtKJKIDemRWG4UaUaRxFwclv_JHwY41LfmPn_jd8oggymTPVQ1RLtkUnw8fD73m-cASoCXyyubkIBUCHokHHYlJq6EiTBzH0DcMqdpurvEsHH6ygxE4OhsNJKwOh2uYsBSJd0GB-eGcOFsbxKAk82AMb9QaH7pJ_ejGun4fpoKAF1trxq6mtStl8k3Fu2LsMROwr_WCYbefvOFXwwk1ZhpLpuW-HuQIMDFX9IxORCV5uyDOMf0eyMkNIZo5ewLfXxH_ExXazj-XUrbjGRF9001F6fnDT54QuWGqIpM82DgS3BccfPwQBZtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b245887808.mp4?token=UBCAnTmx58r9c1revJSqkFoHVmUxtq2vtKJKIDemRWG4UaUaRxFwclv_JHwY41LfmPn_jd8oggymTPVQ1RLtkUnw8fD73m-cASoCXyyubkIBUCHokHHYlJq6EiTBzH0DcMqdpurvEsHH6ygxE4OhsNJKwOh2uYsBSJd0GB-eGcOFsbxKAk82AMb9QaH7pJ_ejGun4fpoKAF1trxq6mtStl8k3Fu2LsMROwr_WCYbefvOFXwwk1ZhpLpuW-HuQIMDFX9IxORCV5uyDOMf0eyMkNIZo5ewLfXxH_ExXazj-XUrbjGRF9001F6fnDT54QuWGqIpM82DgS3BccfPwQBZtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش القائد الشهيد يدخل مرقد الامام علي (ع)</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81733" target="_blank">📅 12:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81732">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇷
رئيس الاركان الايراني:
سنحوّل سواحل إيران إلى جحيم بالنسبة للعدو</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/81732" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81731">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16f90049a.mp4?token=pRs5eg394JNrJpsY76Z55j_DOc11a6uNBZec7VCXdsLsaVmTIYTQ2vqkY5EqDBZw6vFEpfPyDtFAqijRG3BKvwKMl66KT9C2VBpMGOPsru0o660eJiZqtghRRynzKqKl4iTP683UQ3tUdK54WNhMzMUGezaSGgL0Ib_sa0GnAqbXUVu8Eb1oBfW1G-I8j83OMtFbzcbUCwfFK3FrCcvvcIp-osVgQxrd7YwEVae4RNXllCYftsYl0g1aStpidQol3rbCzlgGEZKbFQb6ofMiYIRfLXXumeN2qqh9GkPJ1uzQ-t12FX7-sOfQGZKMttxDUFZZYSleoz8lph5S_bcKFYx0YC6TnPqPXrslGP03UsGkFynMijQbCYOPhTxtvIoj8UT9bbrD9_leBk7ky8C8eau934n75hHF2S1nXr-YrvNrczTlTNL_fW742qgOBq3zgMZ9tWLJ3pQ_vUHlTHCfMhg1i4Hz5g1IZxyOjYitOsiv1dvZclwgZIfP55QEhR0GdRbYiKj72BDalQWmtoQOmJATjHZr7-L2yg5_VyuaM2V2f8F-lRu_YPQSSZhgF1LLKbQSmyO5NgwW-ceqQW4c3cnqXe0tRjp7JPbr4zbCdGPZkz4L2bEixi9TBR-Q6tL983B5Cx-qXa7ksrFTPDA51nnFNU7pvLac_b5ocpMPXo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16f90049a.mp4?token=pRs5eg394JNrJpsY76Z55j_DOc11a6uNBZec7VCXdsLsaVmTIYTQ2vqkY5EqDBZw6vFEpfPyDtFAqijRG3BKvwKMl66KT9C2VBpMGOPsru0o660eJiZqtghRRynzKqKl4iTP683UQ3tUdK54WNhMzMUGezaSGgL0Ib_sa0GnAqbXUVu8Eb1oBfW1G-I8j83OMtFbzcbUCwfFK3FrCcvvcIp-osVgQxrd7YwEVae4RNXllCYftsYl0g1aStpidQol3rbCzlgGEZKbFQb6ofMiYIRfLXXumeN2qqh9GkPJ1uzQ-t12FX7-sOfQGZKMttxDUFZZYSleoz8lph5S_bcKFYx0YC6TnPqPXrslGP03UsGkFynMijQbCYOPhTxtvIoj8UT9bbrD9_leBk7ky8C8eau934n75hHF2S1nXr-YrvNrczTlTNL_fW742qgOBq3zgMZ9tWLJ3pQ_vUHlTHCfMhg1i4Hz5g1IZxyOjYitOsiv1dvZclwgZIfP55QEhR0GdRbYiKj72BDalQWmtoQOmJATjHZr7-L2yg5_VyuaM2V2f8F-lRu_YPQSSZhgF1LLKbQSmyO5NgwW-ceqQW4c3cnqXe0tRjp7JPbr4zbCdGPZkz4L2bEixi9TBR-Q6tL983B5Cx-qXa7ksrFTPDA51nnFNU7pvLac_b5ocpMPXo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول السيد محمد تقي الحكيم إلى حرم الإمام علي (عليه السلام) لإقامة صلاة الجنازة على جثمان القائد الشهيد
للثورة</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81731" target="_blank">📅 12:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81730">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh4K4pfUs59Nf2uN--DTf93TybvHGj934J6wnVi-s1tJ_D4eJLihpgNfvyyetSKOqzPFr_hqjgVGplmWHH8qOqM2567YtFwSismRhHB_3-u3VMiUxE-F210OauH5bAtlXX-yURrfZgUBsp8IxDst0WpMgoKz-F3XAXnoQvz-g6kmcBLWJdJxmgUYVtEyZ9zhT8W8jeAFsn2Wv5hexYuosMTdXQxzs52OrdIjDNiKGQpWzCr0NyI-EPN4Z2guqhu6erNWHEs6qAHy7SP-y4gQlAkcfGs92OV1FQ2LXlnyEIUgdIvENyNHJMVWluJiCU5hhyseDhMpnrywNXT1uBkifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاية الفراق.. علي في حضرة علي</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81730" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81729">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">الكويت:
تم مهاجمتنا فجر اليوم بـ(2) صاروخ باليستي، وعدد (13) طائرات مسيّرة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81729" target="_blank">📅 12:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81728">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزير الحرب الأميركي يلغي زيارته إلى
إسرائيل</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81728" target="_blank">📅 12:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81727">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامب يتراجع:
ساستمر في المفاوضات في حال اراد مفاوضونا المواصلة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81727" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81726">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامب: اوقفنا جميع التجارة مع إسبانيا وجميع الزيارات إليها. إسبانيا قضية ضائعة، أنا لا أريد التجارة معها.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81726" target="_blank">📅 12:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81725">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5Z3RUQRrcIu0Xj_RxVP3ukDzA0OlguP6oZnXJ2GT0iyuBzXQSt1uZE9U4qFQNLrdo-SmH0N0-H_TmnBjQoXqFvo5tnwJ8KPhZL9sybqQ344hsSpmYqYGa9jhD89yfAcXG04JjFmH4TzBYUup3WL83oz4w_7g8BIQzllTHUTui--RkX9XLNqFhkb3zz09aJkdTPkRhkalXp5LFZpM_C01B2vGu54Gra25zdQZebjfWeXnLbUnPNM7yWnbhFkRw2wXUZR7UJdxqSnNFcx6PmEwjcOSn9OtQLbtz6Cwyl1sBzXYK3zkyq2YZ-Z9wKA0ODlTeCHqf2VHKKqnFZyOvU6ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصول أبناء المرجع الأعلى السيد علي الحسيني السيستاني (دام ظله) للمشاركة في مراسم الصلاة على النعش الطاهر للسيد الشهيد آية الله العظمى علي الحسيني الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81725" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81724">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">أسعار النفط ترتفع بأكثر من 5% بعد إعلان ترامب انتهاء مذكرة التفاهم مع إيران</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81724" target="_blank">📅 12:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81723">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">وصول أبناء المرجع الأعلى السيد علي الحسيني السيستاني (دام ظله) للمشاركة في مراسم الصلاة على النعش الطاهر للسيد الشهيد آية الله العظمى علي الحسيني الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81723" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81722">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byZ_AggqPNPYWSfJS5aVMa_Q06qxtwQ4lNXObyNLDdrLMQIAfymzIaYlsEiO8i1u0B8ffvzZiWpb3OjAphlluwurs7TEuZn972O1goz9sqFittHVDfnC_x0-XCGiDb97TyWee39qxfldf0RsXCrCJZp_Y3kRH4IRsNXYunEQ915mF2tojnofQV2-iZmiqfPb6WxjHMDd80phHYQz2DQ98jYA7BeMp_VTNYBWWgbUkYP5pzI-xjZEl6vhWMDo6ShHNlsfIjEe_2uh34xoE8x2dBy1r4_7xpoTWH3SwXJVdfgQMxfveNoC6_2NbaGtPqhoyRVBVGglR28phbHcUAmGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وصول أبناء المرجع الأعلى السيد علي الحسيني السيستاني (دام ظله) للمشاركة في مراسم الصلاة على النعش الطاهر للسيد الشهيد آية الله العظمى علي الحسيني الخامنئي (قدس سره).</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81722" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81719">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxL-F3aiCwr2nhBUR42Fu7ebs22VwO6bg1sBJ3vAz3K3GLlSkqrAKqnYCAULC_SDJohI99a_n8A5sSmk7DkdH3vT0WpglroKqfg84xNvpPfIZUPhv8XNfjBwC2JGi-Ma6Ai8kbqpKB7p-TdNsqaeS8Knu0iLSFVTs8q-TLejhsJ6HTJ0iQt0erU1LQZlY_NAo5bKRvJ3hPNxqiCqt3ge8j1K_a0GOBWFZQO-0FYOeoFcSCGAG0sAyLw98fIzHC23uXzMPZ-j7WGYkvFFiE-1mYceOQGPhlB2Ni9hCwKWgYvmKoLXsOiHc3xYjYuRU_l2fgrFGaxUQQ_x4hzj8lYIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fmd8bYXDATq8XB5i9wTNxl6xkeGF2Xvgiy9zyZViyE--P4os_TlPiLF9nK_Dlkjc1IVUffDwttvChJediOHFX6nUx2uCoR_z4WiMnDQCJXgs8JbcvVnUoOB_N_nKmLUi6x_EaisHx9fIiejeE6c4vjNXAW5NsAu-flLRRdDc_tzhedsE2nfEjxsp4bJDP-Fyuv4qFkNmHUzrs-A-DRdWOxp4MxRwNBY1qUAbNefh2kJNLQ7a6tSio0U53r6RMs89iveuoF9e94Zf7BfUNKVGFjwhW3r33kQFOU9haZqIFf0zzwcL-xqSjccfe5jFUCHz-S10BiyZSccPn_Gl9TcAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIDVFxS3yLN3tURbvSvN50fvpXSIPcU2xiadzLgXPZfKIoxBtFqU5psAIUeiXNXeiH30p8Fpjh5IA34Dqe31Bf-9fPoQnyOLzzvdcx8BXmBl4yjZfhq6JIX6bmcyUPQvbN9n7XfbJrLrw8Uq0_wBPQPtBgo1lBnGcjEiDs9Kc1U6EHxRbm2R9DMK6bUHhDkS1rzAjcYc4etaiRkLyQgDgqE0D0Z_PCk5jCKPKYHdFMjgnoVhyJlZBYp-XzJ5_aZV6GU5lZJbWhoAntzafvNT-pc0q319yKOmwXnH9aL3MibsavhnfrhUFn4d17mSNfQHue3rRiMuVXqbPPez70eBbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الطائرة المسيرة الامريكية التي تم اسقاطها في محافظة يوشهر الايرانية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81719" target="_blank">📅 11:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81718">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏ترامب: مذكرة التفاهم مع إيران انتهت</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81718" target="_blank">📅 11:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81717">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC-RKvDGPUwmK2veVb-kCLcpjtkm8wx6gQl_nwXV7pjDMMz_XohuYJh_fEZnt4Zsr2Jp9izls1GDOU5qhpO5GbmzY0SqLa5TX5votU6SKSxk66P7dl9d1Ubt0tcq1JlOfEYX02P4FzDrD2qSiZyRB9tH6mUvMTtNJCQ4Ri0SeTQ1Cs1lGAFUxvANZKFcoNzE7nj8v4FyEv-SX6EVDDhdHvAz2tKr7-sd2VGKl95pgkr6s0fPdbWQhdzR7WAe4ZsZCUX3e-DyDw5-sBLf3X1ejFnFsd0uYe1m7v9xn4rr5YbMHVxuXBRZ92IVcUtL9OCPanHrFiuNm3kdJBAb4JqQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
‏إن سلوك الحكومة الأمريكية بصفتها الدولة المضيفة لكأس العالم يتبع سياستها الخارجية المعهودة: التلاعب بالقواعد، وممارسة الترهيب ضد المنافسين، ووضع العراقيل، والغش. هذه هي استراتيجيتهم. إيران ترفض هذه الألاعيب. ونحن ندافع بحزم عن حقوقنا.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81717" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81716">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
ترامب: أولئك الأشخاص المرضى جدًا في إيران هناك شيء مريض في رؤوسهم. إنهم أشرار أنا أكرههم، ولا يحبهم أحد، إنهم فاشلون، وإلا لكانوا قد توصلوا إلى اتفاق منذ زمن لقد تخلصنا من قيادتهم الأولى، وحتى الثانية إنهم أشخاص أشرار ومريضون، يجب اقتلاعهم من جذورهم، مثل…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81716" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81715">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118db68564.mp4?token=T0XSJYppnJJVRKNiG3nc3NakxljEDJyOrdHGUtE6SfwPp_YISQ36Z1aj9vh4I90PMRZbdLvvh6or45AVEbFHJ1D2e_luwGiHPgkdoFl_bc99OQbeWXrq3bxcepYwYgfUsR3qWy2eVlMERXQfaMg9cTyRayBN4RxMfFfEdn5EnGLKLU6b9CqOswflWVPwfDGNHGCvGfb_tLC_Yz4vWw8RbhX8rE8jUlxxU2G6h84HcpBr2FYrWpmTUS3Q4W0RuPS1snhnLRKWqi3lgG30i6Z3NK3NxxR1x14eG6xoS09uQxLIvXQyq6H0COoAHYnb7xNESPxptbWtbTfysZ7vgRob2y2IPWm0koCDXIGI_3nmETHPypadfnXFYUYM3OLdAplObADyAEZ3pD-CgIA47MpfEuAoWn8IK3E5zdpx9oOcmByPdt-yCz9X61nGvAgzYV4wxs_6PBHr90M0eG8Ip_YAGWk9ti50IMORtz1S95d1zo1QRGdTA8Azb5FwcES4vkHekHP_F4cyF_DAH62p-bRHYnuxDiNcLxTyKo8E8M7YELiq2RxNPsK40sLhbYly6ddXPNCKLLY5eMDCHAHBW938rvTpBuXzeDVprRP1Ytt1VbRIZd2-_e3AmA0tuw25o0kIsSNz-5K64c5gAQzuI1NTCFEFmEXojGOxkS_fy27zapA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118db68564.mp4?token=T0XSJYppnJJVRKNiG3nc3NakxljEDJyOrdHGUtE6SfwPp_YISQ36Z1aj9vh4I90PMRZbdLvvh6or45AVEbFHJ1D2e_luwGiHPgkdoFl_bc99OQbeWXrq3bxcepYwYgfUsR3qWy2eVlMERXQfaMg9cTyRayBN4RxMfFfEdn5EnGLKLU6b9CqOswflWVPwfDGNHGCvGfb_tLC_Yz4vWw8RbhX8rE8jUlxxU2G6h84HcpBr2FYrWpmTUS3Q4W0RuPS1snhnLRKWqi3lgG30i6Z3NK3NxxR1x14eG6xoS09uQxLIvXQyq6H0COoAHYnb7xNESPxptbWtbTfysZ7vgRob2y2IPWm0koCDXIGI_3nmETHPypadfnXFYUYM3OLdAplObADyAEZ3pD-CgIA47MpfEuAoWn8IK3E5zdpx9oOcmByPdt-yCz9X61nGvAgzYV4wxs_6PBHr90M0eG8Ip_YAGWk9ti50IMORtz1S95d1zo1QRGdTA8Azb5FwcES4vkHekHP_F4cyF_DAH62p-bRHYnuxDiNcLxTyKo8E8M7YELiq2RxNPsK40sLhbYly6ddXPNCKLLY5eMDCHAHBW938rvTpBuXzeDVprRP1Ytt1VbRIZd2-_e3AmA0tuw25o0kIsSNz-5K64c5gAQzuI1NTCFEFmEXojGOxkS_fy27zapA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الولي الشهيد في حرم جده امير المؤمنين</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81715" target="_blank">📅 11:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81714">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامب: اوقفنا جميع التجارة مع إسبانيا وجميع الزيارات إليها. إسبانيا قضية ضائعة، أنا لا أريد التجارة معها.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81714" target="_blank">📅 11:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81713">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2869af20e0.mp4?token=C5eC2509CHaPEMv8_zcNSQ3elu1fbDh7IffHdWfRWu-h8S1uPIAgQihMbm4zUnmTMegR7mYg2iUm6eUNE56FofMWqrFtdhlPRfyu191Zi6sD2M7u0noOgbuhtM8Y48E2NaiBhRpyTkGHzZda9MIDGNP2YzhItUO2RP7b8eVXdw7TrUpzFBp5jkZfJnyxQL1D2-s5j4of_4w679WStQPzDGchoZbWqJ_7-g91InS11IdUGY3TRMTHLk6QbX2ZSRB2XWadUWeyxpcBzmR8lgcNS3BTn9CFMAg7qTIHBKBFdXcf_ZIDkLgotQGM3BZaD3gio1Ry9iR67a4WQhZqF4xydaCnsGvgjy06lkhMHwUMHNGF25Ybs1exmAE76qQxjcrBqEgeWVQoXq-7A6tzOQRZP2Q4U1vE5tm7CZqBD_k6v_fGiUgzJG6j-zUNxKm9vjmJq1rU9OKoKjrDsV_qQCPnG998oBUtv_YbJ5iQgZO3Etd3vInco7-UQiVE78-dQ73u4_xii6YDfckUPR_0p70xhL17UVrGw3q1V-8mKhJhDxVg7P28Vvbhj6E0T7aZP6Ag72AJEZ4X8EvQeLfsWcMcKStc4ujpLzoANL1dsG3wI6Khqh2zEAdhhsjIR9pvi8_X1KEk61xCU_Za40Fb8-wML3gf-zV39kcHGhaxxWoyDZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2869af20e0.mp4?token=C5eC2509CHaPEMv8_zcNSQ3elu1fbDh7IffHdWfRWu-h8S1uPIAgQihMbm4zUnmTMegR7mYg2iUm6eUNE56FofMWqrFtdhlPRfyu191Zi6sD2M7u0noOgbuhtM8Y48E2NaiBhRpyTkGHzZda9MIDGNP2YzhItUO2RP7b8eVXdw7TrUpzFBp5jkZfJnyxQL1D2-s5j4of_4w679WStQPzDGchoZbWqJ_7-g91InS11IdUGY3TRMTHLk6QbX2ZSRB2XWadUWeyxpcBzmR8lgcNS3BTn9CFMAg7qTIHBKBFdXcf_ZIDkLgotQGM3BZaD3gio1Ry9iR67a4WQhZqF4xydaCnsGvgjy06lkhMHwUMHNGF25Ybs1exmAE76qQxjcrBqEgeWVQoXq-7A6tzOQRZP2Q4U1vE5tm7CZqBD_k6v_fGiUgzJG6j-zUNxKm9vjmJq1rU9OKoKjrDsV_qQCPnG998oBUtv_YbJ5iQgZO3Etd3vInco7-UQiVE78-dQ73u4_xii6YDfckUPR_0p70xhL17UVrGw3q1V-8mKhJhDxVg7P28Vvbhj6E0T7aZP6Ag72AJEZ4X8EvQeLfsWcMcKStc4ujpLzoANL1dsG3wI6Khqh2zEAdhhsjIR9pvi8_X1KEk61xCU_Za40Fb8-wML3gf-zV39kcHGhaxxWoyDZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موكب الجثمان الطاهر لقائد الثورة الشهيد يصل حرم امير المؤمنين (عليه السلام)</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81713" target="_blank">📅 11:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامب: أهدرنا الكثير من الوقت مع إيران ويجب علينا القيام بعملنا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81712" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامب: الايرانيين مجانين</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81711" target="_blank">📅 11:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏ترامب: الإيرانيون قتلوا الآلاف وهم عصابة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81710" target="_blank">📅 11:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏ترمب: لا أعتقد أن ايران تعلم ما تقوم به</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81709" target="_blank">📅 11:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🌟
ترامب: لقد هاجمنا إيران بقوة كبيرة الليلة الماضية. الايرانيين مفاوضين قذرين. إيران أطلقت صواريخ على السفن، ولهذا السبب ردت الولايات المتحدة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81708" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81707">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌟
ترامب:
لقد هاجمنا إيران بقوة كبيرة الليلة الماضية. الايرانيين مفاوضين قذرين. إيران أطلقت صواريخ على السفن، ولهذا السبب ردت الولايات المتحدة.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81707" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81706">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">موكب الجثمان الطاهر لقائد الثورة الشهيد يصل حرم امير المؤمنين (عليه السلام)</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81706" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81705">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
مقر خاتم الأنبياء المركزي:
إن نقطة انطلاق أي دعم يُقدَّم للجيش الأمريكي الغازي لشن عدوان على سيادة إيران الإسلامية وأراضيها ستكون هدفاً مشروعاً للقوات المسلحة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/81705" target="_blank">📅 11:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81704">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">▪️
وزير الاتصالات مصطفى سند يعلن إطلاق طابع بريدي بمناسبة تشييع السيد الخامنئي</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/81704" target="_blank">📅 10:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81703">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b35997085.mp4?token=KrMaKkJmut2zOAETVcwCyO4O0lTwDT4oBJAk8-eD9hJO1oXKj_3md2Xm-a6NQ_hQKJ38eVHw9B01Dx5EAwawY4UrVijRxinZdXO3OpfhbDTiPZCt1ncdgdw4OeUOiypASv77mGlZfNqibkYsJGVqAF_qlC3pfOAwXL1yvg_9IGexOF5Gzhp7DBDbeMZDRQFy-j8KtpejtirKgMGblMz505aRJNIDJxCcDlIcqYqfR0p_SAey6vCjo4x_1zwFMULQO_XpiX30EaLIOlYjztVNaUMVk4ahA5XRdTgA1BES_UNC-Y8i4SqSspsDq1DwDdshQrF9KHL8asMrb99nqf02kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b35997085.mp4?token=KrMaKkJmut2zOAETVcwCyO4O0lTwDT4oBJAk8-eD9hJO1oXKj_3md2Xm-a6NQ_hQKJ38eVHw9B01Dx5EAwawY4UrVijRxinZdXO3OpfhbDTiPZCt1ncdgdw4OeUOiypASv77mGlZfNqibkYsJGVqAF_qlC3pfOAwXL1yvg_9IGexOF5Gzhp7DBDbeMZDRQFy-j8KtpejtirKgMGblMz505aRJNIDJxCcDlIcqYqfR0p_SAey6vCjo4x_1zwFMULQO_XpiX30EaLIOlYjztVNaUMVk4ahA5XRdTgA1BES_UNC-Y8i4SqSspsDq1DwDdshQrF9KHL8asMrb99nqf02kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما ضم راسه يا حسين ابنك
النجف الأشرف مباشر</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/81703" target="_blank">📅 10:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⭐️
وكالة سلامة الطيران الأوروبية:
على مشغلي الرحلات عدم تسييرها في المجالين الإيراني والعراقي.
عدم تسيير الرحلات بالمجالين الإيراني والعراقي يستمر حتى نهاية أغسطس.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81702" target="_blank">📅 10:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
🇮🇷
نتنياهو:
الخطر الإيراني لا يزال قائما وطهران لا تزال قادرة على إعادة بناء برنامجها النووي.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81699" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">الجثمان الطاهر للسيد الولي يصل بالقرب من مجسر ثورة العشرين وسط زخم بشري كثيف من المشيعين
🕊️
🕌</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81698" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MA8TeIq2euDixQik0bjdjLtufJX7hw5YWRE_CT7uxsgJsBDLlINjZNjNaMdzDQf2V4QQUtUExL7al3sJTk8A4OeHrUX9FIikdB52IPSzr0l-EFRLr5-9yq20XGwH5NJq7kJJR7foLlQM7nQJfeUvXxYiYK-6WnElFUd3kMGn8patF5hw0PNy8VzzGGJjLBdBKVDBQPQBiK9DpgZ9SOXgCj3vJ0-KA7iNKcHPml1mz1aSVqBHSKb7XBZyiYqqKvsQCOxMNnQf1acSTupByySIOg5cNoOKrDL2ExtH3LTkSXr9KI0ctnTW_iWMprJMe46J1fP_EgUkX4Q41nvrPmvKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رايات حزب الله في العراق تتصدر التشيع بالنجف الأشرف</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81697" target="_blank">📅 10:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوي انفجارات جديدة في بوشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81696" target="_blank">📅 10:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">أصوات انفجارات في بوشهر الإيرانية</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/81695" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">استقبال العراقيين للامام القائد</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81694" target="_blank">📅 10:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4544c070a4.mp4?token=CxUcjmIKz4wuqQSGS4J4Kt8jXUvbX4rnyDQMaC1ybg4pTx91M6NLSkE1iS8RoIZmU2PXxfWYfrWRVrANHTJelw7UNMF63-eb5vz0ma7Syv83rXCVk_MJSekrPGNJiaasDM2f2YqQpfeYi0wy8g_isivHydbH72Gbzcb4amUhkz45a5_FXrHHXDoe6NGGciZ6N7nsgg0oZZa7TeCAKuaNVkJuvZjxqpXVb-c7sY_8PrzBG3zywIk-yH4uV7D_0zxqzF-zPXHZuyJNdSEzm7I0ihSFb9I03WW0dzAsBcOwxwgjTsz80hMLb7rMkOHev0W1GHJ48q9rAlnpjgRX9Q3yRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4544c070a4.mp4?token=CxUcjmIKz4wuqQSGS4J4Kt8jXUvbX4rnyDQMaC1ybg4pTx91M6NLSkE1iS8RoIZmU2PXxfWYfrWRVrANHTJelw7UNMF63-eb5vz0ma7Syv83rXCVk_MJSekrPGNJiaasDM2f2YqQpfeYi0wy8g_isivHydbH72Gbzcb4amUhkz45a5_FXrHHXDoe6NGGciZ6N7nsgg0oZZa7TeCAKuaNVkJuvZjxqpXVb-c7sY_8PrzBG3zywIk-yH4uV7D_0zxqzF-zPXHZuyJNdSEzm7I0ihSFb9I03WW0dzAsBcOwxwgjTsz80hMLb7rMkOHev0W1GHJ48q9rAlnpjgRX9Q3yRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر للسيد الولي يصل بالقرب من مجسر ثورة العشرين وسط زخم بشري كثيف من المشيعين
🕊️
🕌</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81693" target="_blank">📅 10:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇮🇷
🌟
استشهاد أحد عناصر بحرية الحرس الثوري (محمدرضا خزيني) في مدينة ماهشهر بمحافظة خوزستان جراء العدوان الامريكي.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81692" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81688">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJnjniXTTGyhZCVCxbQHCDN6osyV5B6H3p9Ne6lvdnhruwwG7aadiq0IFHICC9o64ELUS0eu0IH1QVynnz4uYpBTq8yxZEh7Ms4UYx5N77MACPVBqP0eEoHzyX_EciQ0fYwGBZvTXOkC5GTiAyQfxjDAjNiuRQ1-SZqsk7ehBKHcVw9TsRZTCfzRvpC2heMxJacuaRny3GybLN_yqaHKvBAAHQU4qfSD-YVOAtnnkVuFKJbTWTKKrgYSsjTDSLY4fZS-bAt2Tv2c3WUD3NoxT7fkSv4I0hQPTgY5vil_Etv4IPebDt2seG9Fw7n9uz-npoIWH0QOV93nxXQyw_XVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dn3kYmV7UdTr5G73XQRQmQ1R1v6o67xPPyEGzGHdsq_ZEpeWNn9oFcu2nKAMpbL_xOHp40NT9YnuknryBgbH5u5NApKCgGiO5-EHTMSbuNI4lXHWlu3zRD8LlpRrAMw_5BctdXm6_NFioVzDfSiaOzQiVaUEIfQl3taicrfgsMhuccJGBjKEAdYrc0Ji2jiqZPiMCt_v2kKdZy6lWGoQohs-6rUE0vgVMU46L4apJtJI2EskKl0Nx-Ku7gFUqCZptGy4hTykq97CNItJEEJq49QcScO4K0B7noAg9kvhuEHqj4HjHBzf-2D4Xm4j5xBgkgHJsjclMUlxhqs9hIvUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4DOPa7d4Ok67sWXvaHVBUAP0il-T1ptNaauAm8YiXKwuh__tZwU9U0oYRuoUoJqL1_hJBr80MdJV4oiVL-UJt4zQUd2HXPwqCMfBSyX8lYayx1qkQ9IEYGLsa2qlQ-bA9MMUAWxhYUDUzjLqcFVsvB1m6bWJgmFDUNt2VroVHdgmnioFHECyC2zc5MHKiXhvu0zJUM6NMSniSckIjHFLbwPjh8v2sSnms5en214U2OvyPN-fcZrCpjqF2IWn05eUdNVbzMuGORQ8u1bQWZoI3r5tPucFr-XAjJ593Uta4b8-hXIUqjNUZ_SJk0QRE7Jw-l36rlDcVxVcl7LVBsYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udZPX3chwhe_JS96gQzttpwwcix20uOBKIxRSN6AaVkeY1-6evDsTu-Kzfp7QY8TuruPfe2YPFw20r8KEoS1G0Lue72XgOfGCy7D-jrqXT5vnIVD9fIRqJ7x3Ahpi8a1GSQyiqeQ6elObUla7ByTlc7v8r03mLbl_o0gt21LJpZK8pBG5DL5qo3UTVWYoVlAblTD-eEJHeSdD-5JTeHz1ajvTgmgWu7iMn4_fENU4CdcAdaU_Ou42p6I-kyFggb6IbQ3cTKKavF4Qi-gDtbhIlxsSOkdTfGt8TfAxIriGmRrG6AXBmKROz5HkXwKKsEuTTekHcMsZ-o7ey3DCrCY3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لحظة وصول جثامين عائلة الشهيد قائد الثورة الإسلامية إلى مرقد الإمام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81688" target="_blank">📅 10:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81687">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c977db3af.mp4?token=SZ1SSujtC38VDr6DGnMBKgng6iS1zlFaLwOJejOPSlbc_M-7nFZD7EgVCEGwea769_B7E7AUSH0w4gDz6Frql03XBA_TTZF5xAYD3ump8qpC1JONnCFqHS6Wnd6eX9Z8eTE_74MWKN8jFDkisquYsArG9_9wQz17_3W7gUJrxP5kkqwCaGegyK3mRPxDEdTEJSZJUWPBJFPGnzXZf60ltBntEXSyGkO0BHuPGGu2lqylafrvDBKXOa4idotyS6cd5RfIOZcYVy7Ttwxtio201NbBaaOCZ5rK0L0PVHJ3pgR1ctrteEQu5HNT6FGfL20dk9yslykiu1QnR61V5czWSF0f05D5kJNG8f3p2U8bZfFOoA6CEfQEX1sYKOv0QaviW5tEOBJESZ4VSchFZcbbMNt-nwHFLQoPC9qsip6dErKXhvMH72SZzIj1pLuo52QW_8h_pHrjd43QT2RX0e9ikc8bted3bkmG6EqDXH8lp_7YpgeOIxcYDKmf9LHL9PvEjxRdfRPXOrLfTyCyqmpq2-L0OUprjQE7CJBlhSUIja9M88bE38wFBGZHF9-33SuYAc26vH_Mz4RVitxO8HFqBPNUldjK1bJttBsQJKGc0DIxdtQDKtgAi8W9VqEdCza0uxaHTCq4qQoUQjt-NNNSfev7XKEPZHy6jgyRV_BqaYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c977db3af.mp4?token=SZ1SSujtC38VDr6DGnMBKgng6iS1zlFaLwOJejOPSlbc_M-7nFZD7EgVCEGwea769_B7E7AUSH0w4gDz6Frql03XBA_TTZF5xAYD3ump8qpC1JONnCFqHS6Wnd6eX9Z8eTE_74MWKN8jFDkisquYsArG9_9wQz17_3W7gUJrxP5kkqwCaGegyK3mRPxDEdTEJSZJUWPBJFPGnzXZf60ltBntEXSyGkO0BHuPGGu2lqylafrvDBKXOa4idotyS6cd5RfIOZcYVy7Ttwxtio201NbBaaOCZ5rK0L0PVHJ3pgR1ctrteEQu5HNT6FGfL20dk9yslykiu1QnR61V5czWSF0f05D5kJNG8f3p2U8bZfFOoA6CEfQEX1sYKOv0QaviW5tEOBJESZ4VSchFZcbbMNt-nwHFLQoPC9qsip6dErKXhvMH72SZzIj1pLuo52QW_8h_pHrjd43QT2RX0e9ikc8bted3bkmG6EqDXH8lp_7YpgeOIxcYDKmf9LHL9PvEjxRdfRPXOrLfTyCyqmpq2-L0OUprjQE7CJBlhSUIja9M88bE38wFBGZHF9-33SuYAc26vH_Mz4RVitxO8HFqBPNUldjK1bJttBsQJKGc0DIxdtQDKtgAi8W9VqEdCza0uxaHTCq4qQoUQjt-NNNSfev7XKEPZHy6jgyRV_BqaYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استطلاع رأي أجرها فريق نايا بين المعزين لكلمة وداعية للسيد الشهيد الخامنئي القائد..</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81687" target="_blank">📅 10:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81686">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQm9qo75VXImJEBp9Vt-vXWnuTtwxWVIS0Kjbdqp8YgHD8-tqb_Og9ffl8FwOq916cJyCkidQco8zp8CpIb4uTgf7tlJBh6zQaxCK4O_wfZxPW7yaCE9jW4eErTmEmu1y9dONj6tZAa-nfE0Vqi9Mlsd10kpHRg_HJkMBEgbaCLIvkoyWxbisz--1Oam0b_nug064_nYth7LTEiWlATAtDCYL8DtOKcepWw795PiP3o0kKTegznFUUEF8LKrY8zNGuHRLI_We6m3jZve_qRI4TKeOSrAfAn6fw1bfr4vP9DnEtzFtx6VuXIxhwRlzPQlflw5sKDSJEV8EpGEyIjkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
بيان وزارة الخارجية بشأن الهجمات العدوانية الأمريكية وانتهاك صارخ لمذكرة تفاهم إنهاء الحرب:
الجيش الإرهابي الأمريكي، في الساعات الأولى من صباح يوم الأربعاء، ارتكب انتهاكًا عسكريًا ضد عدة مراكز للمراقبة والرصد على السواحل الجنوبية لإيران، وذلك في انتهاك صارخ للبند الرابع من المادة الثانية لميثاق الأمم المتحدة. كما أن هذه الهجمات العدوانية تمثل انتهاكًا صارخًا للبند الأول من مذكرة تفاهم إنهاء الحرب، والذي ينص على وقف العمليات العسكرية.
🔹
تكرار الهجمات غير القانونية ضد إيران، إلى جانب قرار وزارة الخزانة الأمريكية الليلة الماضية بإلغاء ترخيص بيع النفط الإيراني، وهو ما التزمت به الحكومة الأمريكية بموجب البند العاشر من مذكرة تفاهم، بالإضافة إلى انتهاك الترتيبات الإيرانية في مضيق هرمز، واستمرار الهجمات العسكرية والإجراءات الإرهابية التي يرتكبها نظام الاحتلال الإسرائيلي ضد لبنان، قد أدى إلى إبطال الأجزاء الهامة والأساسية من اتفاقية إنهاء الحرب. تقع مسؤولية العواقب الخطيرة لتصعيد التوتر على عاتق النظام الأمريكي المخادع.
🔹
تؤكد وزارة الخارجية أيضًا على الالتزام القانوني الدولي لجميع الحكومات، وخاصة الدول المجاورة الواقعة على الساحل الجنوبي للخليج الفارسي، بمنع الأطراف المعتدية من استخدام أراضيها ومرافقها لارتكاب أعمال عدوانية ضد جمهورية إيران الإسلامية، وتؤكد أن أي تعاون في ارتكاب جريمة عدوان ضد إيران يعتبر تواطؤًا ومشاركة في الجريمة.
🔹
تدين وزارة الخارجية بشدة الهجمات العدوانية والانتهاكات المتكررة التي يرتكبها الجانب الأمريكي، وتذكّر بمسؤوليات مجلس الأمن التابع للأمم المتحدة والأمين العام للمنظمة فيما يتعلق بالسلام والأمن الإقليمي والدولي، وتؤكد أن القوات المسلحة القوية لجمهورية إيران الإسلامية، كما أظهرت مرارًا وتكرارًا، لن تتردد في الدفاع عن سلامة أراضي إيران وسيادتها الوطنية وأمنها القومي ضد العدوان العسكري الأمريكي، وفقًا للمادة 51 من ميثاق الأمم المتحدة، وستستهدف أيضًا مصدر العدوان.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81686" target="_blank">📅 10:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81685">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S51DFskCwHDy_kdG4T772wp0G4yZR7lhSQ6qqbWWoKH3GGG94D5mxcpXgAgdwReg3I3-dRaP9a1UhNpGbgU6NZwiC99ngAtjQ-ZMU08Ua2zeqMdZfKJCoqYG-Dv_JyjXTLCk2ynVV4NWQXo_HyUAaxvUaKTfZQkT25yCCV-zJ8II0REh2zc941iyNzYFIk8LRlQOdgmUtcJdcynfzk5YyWkPW1-6AzasV17kO3mBDQb_l9tr7O52rASIGwLPZgEJkCp-UU18__2xafgAqyKEX4rD9k0sCVPXnK20BgwXt2mKCLb140pcH9tNF8ETbjBRa8iRS-QykjsFoniBpvhUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موجة صاروخية جديدة تدك البحرين</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81685" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81684">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3569e18f7.mp4?token=ih_7p2nLmEeIDIE3sVZMY7YlZqJLiZVL5uLDRSLGaolaS1891m9yXUM-aBZQsr3-qVsMm6Ky6lQOOqNS2MBjsIFn8RZwjxf55oNPN0025dlOHfxTWdafSKK39bruezDXtEcPaJBwEKQwagGHZaYP3aqQpJMGhAicNo2TPJfMaJ-b1xlg3TJnH2JpiguttYFj541SOjzANbv8ksEiuAAQ-hq_EJEUEPdc6fb8ayj7WEWCq7AlQRM9sxE-DkSitcSjoTUj4WGIGxMJRCyZdPo8jS7Kr0U2-HuPeg353AzhCu96yLCaE_bgUdIWKmfUJurh457VhkJkstGMcIzyP4r5ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3569e18f7.mp4?token=ih_7p2nLmEeIDIE3sVZMY7YlZqJLiZVL5uLDRSLGaolaS1891m9yXUM-aBZQsr3-qVsMm6Ky6lQOOqNS2MBjsIFn8RZwjxf55oNPN0025dlOHfxTWdafSKK39bruezDXtEcPaJBwEKQwagGHZaYP3aqQpJMGhAicNo2TPJfMaJ-b1xlg3TJnH2JpiguttYFj541SOjzANbv8ksEiuAAQ-hq_EJEUEPdc6fb8ayj7WEWCq7AlQRM9sxE-DkSitcSjoTUj4WGIGxMJRCyZdPo8jS7Kr0U2-HuPeg353AzhCu96yLCaE_bgUdIWKmfUJurh457VhkJkstGMcIzyP4r5ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أُغلقت جميع الأبواب المؤدية إلى الضريح الشريف للإمام الحسين (ع) مؤقتًا أمام الزائرين، تمهيدًا لوصول الجثمان الطاهر لشهيد الأمة، حيث سيُطاف به داخل الحرم الحسيني الشريف في ظل إجراءات تنظيمية  مشددة.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81684" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81680">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kRPsGO7BO5Io4gOs9XFaxjPtIm6bzXChoqmIu6_kZ4-nBB_tvzheGbIngTlywQNZuE5qtOTJH9HCS1G2PjUBX8BblpYRzqvcIkTL_BUbN0MWhrNU60Yp3ElOIpMNswCmXMVpSgDcxGoyCrKxxztZjWm3s12lp3qMHV3Y9ehaJLCbbouurRYkaVhakX7S1QKhAsE5a_Yk8U97yovd98A1GekAR50uid4aaPs1bWfwXRMNnrRW961ejAqPXsTBQcJp6qn7aejCUUbx88gYjMxJYvx8xJdFyBWxjWM_ofIwBB-YEjreIzkmv5NBu4uPvpAPa_w8m0vVqCtd7UepzFFjCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Us3S_9kzVYlkGX84Gy0sr2dO9SuKBGvRS2Co-nFqMupijGn6zie-GFQe6DsT5A7LhABC67ClW1sFzTRHI5I8HdHcr-25dSawHAJ90uEvAMCevD4YjIIXXc-m2ihZAYIs-r63Rxcpdj-2ZhuKgCExWtsD7NUibvDtxEXKTUYWnI7gaKjiGI41Sbg_f5OpqwdMHHk3mhPt_7LMoi1i55eQajQTpfbn1M4ph_zQQH-Fbk3s9JsZHlJ5_f8wCjd1vKj-nVLgcta_IkOsh_0Uwl8IC8paSa5eFX6YQhjHZxLvBVJZjOIcSJAF7OIdHciVNb8lF9uALUUxUVmLLfKspjiMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-bTQMs9aS6WI5R35o2gim8V9u8rGfQwWI3LzCMRWn2dkI-CGK3umEl4167wTVb6gdQ0CHRjVGt8V962q7WRNEpbNEvpHgpaazHKTtGr2RxEw42NF9t08buaMtYbqGPo_KwYhhAKFY8msncCSUf51m9XZRBwseJNBwpm2mEqGvmqorVWm8JR7SMvgA4w6SO-wqwUoIy3D9kBuAx8sbi4EdG0juhh5mriVsTFz75iaU0v_EYy05tyXlP_bWaaRP51bQGd_y-uFUpwvK2eVllDKhOTYFeSLLS1OYyE8Wl6ZuB6o9gdEESTtVjLaQwTbeGxpSatzrTc_il5aNe_Wjo8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTG77jq1mDMp7YhpnCMq2TNMTh6tZE8kXWdkXAl1TwDOE261mZNekfoQ7OTx69i16na7BKva51rxyT6PGQZh2wngK1FcsuiHcSH2aAKokhs0fWX9sfMMO1IEq0mhUtGAIHSu5GAJPQAV0g2a0jN9vqKsZUy3O7qSJ6SaHapR60E-kBrrhsi_SQrTXx_feEh2nBQQybWCq_CrisMYAjo1DfvBGAX0Oe3SZ0lzfU3aUtxOaGsawldHLtWhrTxBn_kW_8DbdtyxJ6-PSQpIzk5Cr3h4LonVCsSLB0WK3VzyDcziyUoWfaATFY93QnyDdbl5VB3hOcX3Wfz7U9Nk5SE4lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجسر ثورة العشرين النجف الأشرف</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81680" target="_blank">📅 10:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81679">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">أصوات انفجارات في بندر عباس الإيرانية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81679" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81678">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbpPpGLgqh6gAPmZON1NT1JrP9z69QG8VATTAIlVLmTdFUYH0-aCjenAD7oKp6jUSVKmemel4FE7ej5PkW4Cxk6LvyWejtieV9qm3cW6qIY5_pPq-6zDNvWQKMcN4cL3d1PtlATmwy1ouP_XOudYrfP1zGu6tfluhdIomwASiZ6lLe_MjbKORjTVPPFte6OssWwkJN7QsKCLguyisXPpbEZW58CMoBY0V2si5GDQ4JhcDb9nnkM7vugIdWYAxUmAiy_3IhJw8D0QdRZOJb_Fqy_bnPy8MgYpi70XPPCUMQD8M5gmonyvW-RxxODmalwBB1WPr-u7idbygg_hBsmVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت تدين الهجمات الإيرانية التي طالتها
😭</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81678" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81677">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81677" target="_blank">📅 09:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81676">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مجددا انفجارات عنيفة تهز الكويت تحديدا منطقة الميناء</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81676" target="_blank">📅 09:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81675">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارات جديدة تهز البحرين</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81675" target="_blank">📅 09:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81674">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">أصوات انفجارات في بوشهر الإيرانية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/81674" target="_blank">📅 09:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81673">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">الجثامين الطاهرة عند ضريح الإمام العباس عليه السلام في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81673" target="_blank">📅 09:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81672">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عراقجي يعيد نشر فديو على صفحته الشخصية هكذا ودعنا الشعب العراقي من ضريح أمير المؤمنين بحفاوة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81672" target="_blank">📅 09:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81671">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c219ea94b6.mp4?token=kdS_wdP1mmrXwkE65r9VQ296M6FYg-C3bnYp5PVgqpwORfMz8B4ZXp22OlPXmNB6T4nVncovUWB7wKSwj7CvXzgZPheWnnXCG9Bf3kuxUlH9uld5CDMjRfufvWJQkLzNbzD_gZyFk_PF9GhwqKZItR7xEa-kQEEKyrQWT63qs-mbtXPpcQmt2WdvAAvaZyxVxhn-CJWtO-Bo57Aj4SEIhA3mR2clPN8EOWXOkIsuZBxCfq6lbzAirfAJWUvQWxAkEkt5aEotdRg58OkJD6pPv3tH_Ui1vUGnlPvyBhC2rAq7WwapvakKCwawcZuvKspuW6rFOK9_SWfx1M71Fg2hqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c219ea94b6.mp4?token=kdS_wdP1mmrXwkE65r9VQ296M6FYg-C3bnYp5PVgqpwORfMz8B4ZXp22OlPXmNB6T4nVncovUWB7wKSwj7CvXzgZPheWnnXCG9Bf3kuxUlH9uld5CDMjRfufvWJQkLzNbzD_gZyFk_PF9GhwqKZItR7xEa-kQEEKyrQWT63qs-mbtXPpcQmt2WdvAAvaZyxVxhn-CJWtO-Bo57Aj4SEIhA3mR2clPN8EOWXOkIsuZBxCfq6lbzAirfAJWUvQWxAkEkt5aEotdRg58OkJD6pPv3tH_Ui1vUGnlPvyBhC2rAq7WwapvakKCwawcZuvKspuW6rFOK9_SWfx1M71Fg2hqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وداعا قائدنا
🕊️
حان لهذا الجسد الطاهر أن يستريح بعد 80 عاماً من المقاومة
🕯️</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81671" target="_blank">📅 09:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81670">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الجثامين الطاهرة عند ضريح الإمام العباس عليه السلام في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81670" target="_blank">📅 09:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81669">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9793a6bc56.mp4?token=MTStiEqXtpWRewV2rhErLB3MKrL4Der_aWie6MYOzSFjepLdo_6kX0AxFptK8y2SHVK4-b59D53uaHGE9JCiY3fDM5n4k6c6NXFB4t2mY4KvfdLYyIpfdHNW1l7RSQ8kGIwj_cBGGucJSsNW4Lo0QiRNCT-V-oMG5G4KfLO5Srh0_JNUFuI5VUpmebHESyVhtNsBBLg5fgOqq6n9BaNImbi3SjLVjqoQMERgdiPaUwNWZRvmxF_MiqfSIkLEgc8a70d3paGIhoHLGraOMA8aRlp9h6CUY1xImEVuxIrt_Wau9R3UKSMIl7zcPCspPj9V4Obs-OWiyqFPY_7pV5n_SH-ulnN6CmxYUL1zzFFjcW3nE53GYXXoS55-MB5qqB6mYbjB4zxzByQKo8pHSdH0LYwfBvj_t4Px_pWZMMJmkzR-QRaesmFddqQ2sK6tGK3fGrpITmjFMox0emeUshYmEMVxI9jGJCyeNHHbhJ_lr1qjgdRtEy9EPfq24Cd0UWp-zzW7w8gofchFmFtXk3ik3ZjzZX-2BtRTA2m-jFFBpy2oIcm_6TuT5vW7JygTaMMWaB-rEx9mqVeU-P3plk6tkQTw52VB-PjgLej-M_4bQ6cEIl0cFghyafHOdwOdrEAW0PCHkYGkmR8TVED8tcswBT-dj9KJzGdTVL46hoW9b74" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9793a6bc56.mp4?token=MTStiEqXtpWRewV2rhErLB3MKrL4Der_aWie6MYOzSFjepLdo_6kX0AxFptK8y2SHVK4-b59D53uaHGE9JCiY3fDM5n4k6c6NXFB4t2mY4KvfdLYyIpfdHNW1l7RSQ8kGIwj_cBGGucJSsNW4Lo0QiRNCT-V-oMG5G4KfLO5Srh0_JNUFuI5VUpmebHESyVhtNsBBLg5fgOqq6n9BaNImbi3SjLVjqoQMERgdiPaUwNWZRvmxF_MiqfSIkLEgc8a70d3paGIhoHLGraOMA8aRlp9h6CUY1xImEVuxIrt_Wau9R3UKSMIl7zcPCspPj9V4Obs-OWiyqFPY_7pV5n_SH-ulnN6CmxYUL1zzFFjcW3nE53GYXXoS55-MB5qqB6mYbjB4zxzByQKo8pHSdH0LYwfBvj_t4Px_pWZMMJmkzR-QRaesmFddqQ2sK6tGK3fGrpITmjFMox0emeUshYmEMVxI9jGJCyeNHHbhJ_lr1qjgdRtEy9EPfq24Cd0UWp-zzW7w8gofchFmFtXk3ik3ZjzZX-2BtRTA2m-jFFBpy2oIcm_6TuT5vW7JygTaMMWaB-rEx9mqVeU-P3plk6tkQTw52VB-PjgLej-M_4bQ6cEIl0cFghyafHOdwOdrEAW0PCHkYGkmR8TVED8tcswBT-dj9KJzGdTVL46hoW9b74" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جثامين عائلة الإمام الشهيد الطاهرة في حضرة قمر العشيرة أباالفضل العباس عليه السلام.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81669" target="_blank">📅 09:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81668">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6a0226b7f.mp4?token=BUCJNS6wWP-uqoO_iPTTapxNaOTX_4xAQKDickeh_VmGcUWzuhfFzywCE3iCkTiT4wtkzJOK0IJwp9xs3cCMvwhIXP1-BBGyZXlahfQuShy_XM1Enl4pOegIa-OV1ug1JBzA0aajAopn69Lq5VJ4k0dvfoywe6P4f2xUGF0xeNfUhyp2TaPoXAmH5Y1X-t7aJ_MII3dctj5kqutU2tnnRAt0OGzILDzTV_mkRTxcr9UU0c7OD04ytVG6O3O4PV7GTfmb6kWsCswdw1BmM9U9is1YeX82iLfJbn1CPJuoDb5aM2wzLIPeDV6njm0J-C_HWOzt779GXRrIlctYy_YFAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6a0226b7f.mp4?token=BUCJNS6wWP-uqoO_iPTTapxNaOTX_4xAQKDickeh_VmGcUWzuhfFzywCE3iCkTiT4wtkzJOK0IJwp9xs3cCMvwhIXP1-BBGyZXlahfQuShy_XM1Enl4pOegIa-OV1ug1JBzA0aajAopn69Lq5VJ4k0dvfoywe6P4f2xUGF0xeNfUhyp2TaPoXAmH5Y1X-t7aJ_MII3dctj5kqutU2tnnRAt0OGzILDzTV_mkRTxcr9UU0c7OD04ytVG6O3O4PV7GTfmb6kWsCswdw1BmM9U9is1YeX82iLfJbn1CPJuoDb5aM2wzLIPeDV6njm0J-C_HWOzt779GXRrIlctYy_YFAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
جثامين عائلة الإمام الشهيد الطاهرة في حضرة قمر العشيرة أباالفضل العباس عليه السلام.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81668" target="_blank">📅 09:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81667">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9042c0965c.mp4?token=odt8TekeOeZTsMKCNEKlItuqWfKWhxrjswylkMdnGd3Ft-vvJfyigEB07kxy_aTLJMRxcHccrrLY0ps0OQ7VBUwAWLMWDu7QSiBW2WLCn1g643vGHENCrTQdSFHMKeQe3q0qItHvoCgs_ZowYGr7mPLOcipGqdMwtkVKojySidl0hyaRbrYyhAVq91LBuo6uiQnKh1mpXKL7YfPzd0HnJdMxWVjBgWzIRmk2epn3IfegxuFoTv5NYo7O8OiGTdsWgHY3W0K3mBlAmHj09fV2n4oL3O0st6Qkn6hHnW-rLCJJLnXqKxjUJRjGcLuGINlByI51d4enaNb_M0xneNi3mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9042c0965c.mp4?token=odt8TekeOeZTsMKCNEKlItuqWfKWhxrjswylkMdnGd3Ft-vvJfyigEB07kxy_aTLJMRxcHccrrLY0ps0OQ7VBUwAWLMWDu7QSiBW2WLCn1g643vGHENCrTQdSFHMKeQe3q0qItHvoCgs_ZowYGr7mPLOcipGqdMwtkVKojySidl0hyaRbrYyhAVq91LBuo6uiQnKh1mpXKL7YfPzd0HnJdMxWVjBgWzIRmk2epn3IfegxuFoTv5NYo7O8OiGTdsWgHY3W0K3mBlAmHj09fV2n4oL3O0st6Qkn6hHnW-rLCJJLnXqKxjUJRjGcLuGINlByI51d4enaNb_M0xneNi3mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">النجف تودع السيد القائد.. انتاجات نايا على التلغرام</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81667" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81664">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peg4zuroZBZapTNDm1qgHm0LbSCPyoWxV_sFBlzNkNEs1eS5l7mE6-CfeSAmPBx6lNDzl-j1nFOe6WS82SVbj7Aaee6ks2nXOsK_pzmO3VmnrC1K2HVFipFAs3bdyvPDZEL-lAuNKtOPyLj-Fb_EfQLISjQcYN3juoZKSywnU8O8BLg2R4-PipCiWQZnACBhAVy0EkeEzfnfp6zpakvmHjvSB45WrnlCmt3CMV7HoPT7zIkRo8KhQ6nXORdhyVNLk3Kt8CEr0lGPNbNVLJBgeTljlgGHTs_2L-TAjfrz7eNpx0f8N2fwH8oeARnJ3kotA8Jo6jjdFAsZHhdNeXGz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQ3wdc54GmifLshFwB0wCtQAfDf8OofN0ji4QpCvJa97U0D17hnVs2KcwZxwczWiaM9FJZoPoSsh3f48xhI_iNOhBoqRLB0lkBrDdbOtk6PKa3_HOdlQ5o5So8Y_V8qgVGGJt0O7-sjfpPuVs9VOZS_RXqVg4GRfZjCiiHFvMytYV6jG5KW5sljrQoT4Q4F1Sgq5hfNJpewZ94slM_-9u7RckTXqN7xixw2KR4qtm4lr7UnajA_idBDdUbZwjWIDwmcnKRv-zktZuLCmx7Qu8NxyNeQ1E7VfkEk-i53Lx-NJ-BTqIdPr5MJ0OigvCifvcpp-4hsDrancCxxaa0kqiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O01PrGoEJ8dUCvE6GFPcvlWmkT9zfTZDGXXP8EiY8bD8J1BTTifD_jCAyNatL3bT51_r0Vy8-Q8mQkj16W7LTFReC3BcUxJthYA3HCXTG6hYaBEVdFC-HU3I38oCClYM_Wjpfl_7y17JVrfQo5JCbFlewj27MOrqFOehs3HZo10mEXuS-fUW97sZLiTDQMA1sTBCv-qjw-GAl8bMRGlpor4xEN8fYFXYT6VhgK6RLd4CY3nQwNrfDVq7KDZGttD-iaUwjuMr9GNP3NKb7_pr--fiRwPUPKsYO4NIMO-SnRBgd2QvYRLnKDvVn5UwhgwaDZ1Yc4tIG_iglEs9wbP6KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">التشيع بالنجف الأشرف كان محاطا باعلام فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81664" target="_blank">📅 09:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81662">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/or2vBd-2K8LwbjSGHCTn35mN_QPWs1iFDmVETK1SboQW7WcOiSiHeX0Xh-lcRcQMC7b4JTjdTEZVI5imyYflrso4K5yOt-QOR3p-agKwt6k1oDzcKMmW1BRktf4LdgtkmL1okePC7GuFUmvQ38gpD9kuTH49qZzuypQWR8iy4gqRsMHf6nHs7ujj2dMVehxnVAx93a68ipSTGUfxGpANzDBs__b06clJIdHu1kI9lLNkXxzwrme6qU6Zt6kZEmrt2k9dOBOiMhEJMSqjvVbkpkPVMp7Irs1qyBgE4LCfe9-pspH8chM9PPhoxngA5-EOPIWbZ-ydTMhCdNzgHP3rig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nfd5x7a6Z4tfKLJBr7mcYYgnzfx1ogt4ZHt0ZuKHXmLx_UqCd-aot3Ph5ozuObWKH5OY-ltIf_eZRNa-XMFfNff56QfHKRYXnXabXTIDj4iNvcJLxJkJOQiYajhEMUF1OeGHygjpS1K5I8MGED6UMDXBjGqtdz8EQRBVoBYUCnX3Zjmo0hEDBOK37GCFImD1yKv_mAoPFjt6nCkY89uyPmdcyYOwS71ILXYa7aRuy7D0ZaDLvLcVUd2Sr_7UhAE5FPm0WSUd5tvOlK2clLmqWmTfR-ryREsX3XguvWrKe8OCz4vTypOLY0G3-6NgJr7Y7CNq7TzD1eBvdhEDqzrfFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تشييع جثامين الشهداء من عائلة السيد القائد الخامنئي في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81662" target="_blank">📅 09:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81658">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQ4-YCwT8s1k4h36J4JLrdkpMWXCNbMrSmzU_ufO_DL-ZoMH0rtLh91h0ov1YxFuxQbHHq6MKrdy-y-8agMKQZPHJmt1DCMq7bsGddY2xlNwWvtbFyzm7HUtfCV66Ogy6Un8DtAGuAv5DXZZ21MAiIeuUWVyPBCO3dzsvTqwo62Mfhzl1SBIkF1ajR7sZ2IbCawmAO2pQy0ciXz15IVKuhMRqH9Pfm2Vyo2Gh-SpXyJVVdoHmNbqNKGY3McqPjPOeR-1Wkct7fsasNrcSmH9R4bY8XaZUvsiNOr0QHZOl1UljtCZuDpkVWYOtiPJOjM1scMeW3AJea0BH5XUEhUokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMr3Kter8xD_Y2OOZHlF9IQwuyVsyVrT6wQ4xgXmtvz0DuwVYgKOJR40zUFltKb4sRnRL2f9fo-IuCl09Bs3xnxlwVJ6J3hlyZAzcISiS1pY_szXf3-SktCERsv4Rd8Ykpb6f8P6VEC_z0NaBZzFQU9VQ5n8E-2Q0IwG9zx2KRTxIGDXVGDuY9xn4m8fRev0nTf2LOPxtKw1-ihLo-NToF2PUlLGhAIYE-K0OAxIvHtZDmhGd31JwTFq7CbzVqf2NWqTuWMphgwxOs7QHN4y10s_yC8kQwDRleJuMMj_43vBWxLvLkVBOIGi421KDiaPujpRW-zhhAyg_TpNkNEx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgG96t0U8rBoW-EWpvmJ-o4ek3daDXSrYjyteerP3Ft2xtdl2CPKvaihQV_2zFWfuYcWdlJabD6kxn8C9C4QU0ZV8XUAkMV3-1tek1fFfqj6iLrdxjuktfUix19987KX-up9Jc5yNFDLtEVlJwhHK8olDwjlCWdH_DfwzRBMOIS5sC0iYx9tcBES9XZ6BYw0rTW_NkP1qL7eNUY77FGhESbIX3p88hXJJKit2F4jLCJ3eUmOcKRPrc7sLUQdRIzcIkL-eW63htKv9mIvlBfcjuCQDqRPxTDnvK38azNg1lOFG3diEMJQyBkI3oh5iDp_aCCraA3mQDWec_PvlaG9Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇮🇷
مليونية تشييع الإمام الخامنئي الشهيد في محافظة النجف الأشرف العراقية.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81658" target="_blank">📅 09:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81657">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مقتل غابرييل إدواردز القائد العام لسرب القتال البحري بالمروحيات (5-HS)، بعد سقوط طائرته في بحر العرب.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81657" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81656">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81656" target="_blank">📅 09:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81655">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875458cfdc.mp4?token=Queh_pRCa3B-opyhhvl6PMH_d2P09H4m2FTf0j3o7FFSJzdzq586RSIBmloYuqHyQMT0IJ1fA3z9ktqYYFZaa60J1lFAY_H79COWT8_PRwsxilKxxj4wGWyexAjn76p00MbrSOR0EiazpK2m7R3687_XtcHy-47hRMjGWJtTuBMxcgMlSPKqbv8uf6hgDccXrtYX7sHfvIsMWzlufDPlpQuw7HIGyiyB_WNqZUvqQ1PMEUSUfjhj0tZfcxiKKExIGg_CRq3l98Y78RdgOFVNXnPCgJ83H6Q0V5thBUWmsoKVRUYbVNq-VeyrE9V4CEy-ua2QVUqpQ0vmXUJEmPKD2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875458cfdc.mp4?token=Queh_pRCa3B-opyhhvl6PMH_d2P09H4m2FTf0j3o7FFSJzdzq586RSIBmloYuqHyQMT0IJ1fA3z9ktqYYFZaa60J1lFAY_H79COWT8_PRwsxilKxxj4wGWyexAjn76p00MbrSOR0EiazpK2m7R3687_XtcHy-47hRMjGWJtTuBMxcgMlSPKqbv8uf6hgDccXrtYX7sHfvIsMWzlufDPlpQuw7HIGyiyB_WNqZUvqQ1PMEUSUfjhj0tZfcxiKKExIGg_CRq3l98Y78RdgOFVNXnPCgJ83H6Q0V5thBUWmsoKVRUYbVNq-VeyrE9V4CEy-ua2QVUqpQ0vmXUJEmPKD2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Mavic 3 DJI over Alnajif street</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81655" target="_blank">📅 08:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81654">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bab1b56.mp4?token=VtvaWL6Km96riWu1G2bPzm60UUd8RKvMkn52OJoVRb57wUFNNGzwtHxcFXjYbmp2H7g-WUdgTrrBDh6Wq8tPkHTXww8IO8KdfiD-nFCJkfz9AznhLoywfmKkBjcEoweoqpPDGOpqx0h9sHtwrHHsDyhvW_PajVO3qHluoltjzwVq9yCZfpqwGZyLENJwu0OgbsvSYiNrj7jU9tbhVIBgjqZ5s9ZTxFeGFeKNe2gY2VRqvYcszZg_sRq01LtxROrub2ZEMUGzColv58vvE3Rn8c-J29nl6aSaWfe-IHOZBV3zT2uxN9FjCjJvCMSaU4dWrCuKK-W0ce44FCmjG7pFcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bab1b56.mp4?token=VtvaWL6Km96riWu1G2bPzm60UUd8RKvMkn52OJoVRb57wUFNNGzwtHxcFXjYbmp2H7g-WUdgTrrBDh6Wq8tPkHTXww8IO8KdfiD-nFCJkfz9AznhLoywfmKkBjcEoweoqpPDGOpqx0h9sHtwrHHsDyhvW_PajVO3qHluoltjzwVq9yCZfpqwGZyLENJwu0OgbsvSYiNrj7jU9tbhVIBgjqZ5s9ZTxFeGFeKNe2gY2VRqvYcszZg_sRq01LtxROrub2ZEMUGzColv58vvE3Rn8c-J29nl6aSaWfe-IHOZBV3zT2uxN9FjCjJvCMSaU4dWrCuKK-W0ce44FCmjG7pFcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العراق يشتعل حزنا بمغيب شمس ابا المجتبى الحسيني الخامنئي</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81654" target="_blank">📅 08:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81653">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e67f30d0.mp4?token=o5KBGAVnRzosSlO8rNfp7nkrUy1mXwXp6heH0wSJzovmpv98c-aHqmBwZibqGfbQDHUeezdb-ffijQIZcgV1AZkTL8Ftz7cujUAqBVhYdUym5dnhLbyZz-bMwHh_5OMqCCvb6QlCiJdFpe_SwB4-LOjk9I-p-rZA0BxoUeev7uO4LezyftnvSErPVrFFxMck_h4y7GMidNe4TeeQmJT1rEnLfw7CM7RRLX5BlQBwJbGRhoCnahLzXRKD7mQUDH6-Q3r76qHHyOAKuq0gAnqz57sZFjE1013TeWtbhFMNeHw5M5je93ZO00kMlV1W-EnMbJavfqk_m3Qms_6iEf7ZuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e67f30d0.mp4?token=o5KBGAVnRzosSlO8rNfp7nkrUy1mXwXp6heH0wSJzovmpv98c-aHqmBwZibqGfbQDHUeezdb-ffijQIZcgV1AZkTL8Ftz7cujUAqBVhYdUym5dnhLbyZz-bMwHh_5OMqCCvb6QlCiJdFpe_SwB4-LOjk9I-p-rZA0BxoUeev7uO4LezyftnvSErPVrFFxMck_h4y7GMidNe4TeeQmJT1rEnLfw7CM7RRLX5BlQBwJbGRhoCnahLzXRKD7mQUDH6-Q3r76qHHyOAKuq0gAnqz57sZFjE1013TeWtbhFMNeHw5M5je93ZO00kMlV1W-EnMbJavfqk_m3Qms_6iEf7ZuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه رسیدن پیکرهای مطهر خانواده آقای شهید به حرم حضرت اباعبدالله الحسین عليه السلام در کربلای معلی.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81653" target="_blank">📅 08:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81652">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مجددا انفجارات عنيفة تهز الكويت تحديدا منطقة الميناء</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81652" target="_blank">📅 08:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81651">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هجوم صاروخي وبالطيران المسير يستهدف البحرين وانفجارات عنيفة تسمع بعدة مناطق.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81651" target="_blank">📅 08:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81650">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
العلاقات العامة للجيش الإيراني: في أعقاب الهجوم العدواني الذي شنته القوات الأمريكية ضد المناطق العسكرية والمدنية في جنوب البلاد، وانتهاك بنود الاتفاق المكون من 14 بندًا، قامت الطائرات المسيرة الهجومية التابعة للجيش الإيراني، منذ فجر اليوم، بشن هجوم على مراكز…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81650" target="_blank">📅 08:45 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
