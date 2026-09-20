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
<img src="https://cdn4.telesco.pe/file/NWhLFD-6j2D70rOJqjJ53lZlJ-oB8dSYMz5miJho6x2dkU4NsvubCdtT6F6MRS3u0c8IHRYf6E7KzZqoY_6Klzs2PpaVdYAMETqKhtND1ntUjaR-RI6U9ssq0lmrgLHEoBRv4NDvA8Ote1In4GVBuunJtQuX2wP3A5qXpvjGheEZI_F06aRv-81fVPSTjLpvF03Cv9kL-Ral-10xYTLpNs0CXoE8c2Uxv8d7ld7sM7xUiEjOsL27LP4OPbK9zIIBvxRSU8x-AtN-qR8JBB-ntxxfxWmNaHNfQP_V21kUDezol7KMeMR6-1vfp1tnfvd9vHveVXi0h1x1zZ7LJhWiAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JamL_tp8AIgXmf93bWUgwrOj5kJVIpq-u_OLF8oI3AZRnUKA0pyo1570hn1Oh6rtFBLYLdbLtJJAa8Xq8M8PBV0QKDVojjqoyKBcARrq7TXkNikPn9N-eiFKhRx67vYxNSzoiJSMR3V0i5K2O91sYtLklYzoJHJ6JRw4Aa1ejplS01pfELNSvP1DRSQdKYj7bmuYksnwiZcJwpLiVLQsW3hC20fVW-aD01LI-PWvu-Nruvy_7FrUg6LHVWC8gfOiN76lf5B7ech_GCwDBBbWHQWvJUyT1Oxj9Rv78P_ILbHiA16IQmBaLkBtTk6TS1a6XERdW_MCpg36tn_SX5IGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید با دایرکت دادن دونیتش کنید میخواد پول دکیو جور کنه پس بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/funhiphop/83843" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMIrjkzVL5nlfzZAxc6THv4HM2soAnfo29QE_kgnXrwukDBY557KWYoOkWhtJnJlF4fCPyCi8ITIWlepzp1ErbKco8b7U-l2-O-N2Fibx3eDiHxYda76FqiDPCroowsZKOpgtDNQ1K0MW9Sxuu7eQ7g6w2QNHVBpcT1Yny2XEIHntceIyZ6KQRC3Q-f8bScg457_C6Iokjb2MMiwgEe6oh0YbPEKiVauKE2cnDXFTX8EEX-rQ8NPNk7g-8qIqKH9Gc2dlP99ii6uYgE1RCj2jAuyzd2Bml63Chk9f2Krqkty9aQ1QKd5zH0IRNrzicYHPADBEiEtV7gxp_dwB_o9OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت دربی مادرید الماس مادرید رو ببینیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/funhiphop/83842" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83841">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9TkT7evL5U4nctq2ptU9ncO6oR9A4Dc5OIVjQxScyf1B5K76DjRBwKsiIkTQGVMC7cxpu66UdFZG4jzokJZo9-2Eo_aXHi55YCzEjL-CzllWrjl2e072KqfkOvZ4plsBERoiHoTzvD71Y7Hj3nlUVxtC4VrHDzslqKtgP6sRoDoZ3Kj4JnIjL66qtooqEgfldb3xhnQfBLRJV1X_FcQCFw9sla9Qmn7hAoD35-BGVN4Tk1nsnAUuiKswgigigMOnGLJ7uubcSHJdh6NJoIrbOaU5gqNtw8__hyLjRgrn1G3pvdbQEjeNLQlHb9M2M8zKKy8i1oWNPX8H8JXBMpH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👁
سود روزانه میخوای؟بیا بری بت
💝
0️⃣
2️⃣
🔤
سود برد برای اولین واریز روزانه
👀
😎
کافیست با مبلغ دلخواه حساب خود را شارژ کرده و برگه شرطبندی سود برد را فعال نمایید
🥹
💵
10%
شارژ بیشتر برای شارژ با روش کریپتو
🙌
‼️
برای اطلاعات بیشتر به صفحه بونوس‌های سایت بری بت مراجعه نمایید.
😀
🤖
ادرس سایت:
🅰
g29
👍
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106
📨
کانال تلگرام :
👍
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/funhiphop/83841" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a15289855.mp4?token=e1I9NsydehZGffs7XUiuRBvFHYd1Z2EMs1oyvsWEjbJrh5F7e5IaGU5dxQbvDpVqFLPGPtNPaA1PD7t1aOb2L8Pmt8_Hy_PIlBi5fdizVNhgjD-dH6m0ykjXRJar9A0LrmNuVHtJWKD2-wsSLm5hMTIB7zysXdUy4tr3lpiu0UttSNVorAgR6inQA6jzcAPfTZKom-6N77gUP0ZueX2WFl2HGQSdCv7D0lWs2SI7WRZq6SZuijnCZaX7Xrpp_JTbubv-Acbc5x3llKdReYKkHA21FSLdBpgAabYZAFKMqZEU2Z6xDMBmLHdUTP1aALLVmNpy_woSBYl53R2Cc3EZNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a15289855.mp4?token=e1I9NsydehZGffs7XUiuRBvFHYd1Z2EMs1oyvsWEjbJrh5F7e5IaGU5dxQbvDpVqFLPGPtNPaA1PD7t1aOb2L8Pmt8_Hy_PIlBi5fdizVNhgjD-dH6m0ykjXRJar9A0LrmNuVHtJWKD2-wsSLm5hMTIB7zysXdUy4tr3lpiu0UttSNVorAgR6inQA6jzcAPfTZKom-6N77gUP0ZueX2WFl2HGQSdCv7D0lWs2SI7WRZq6SZuijnCZaX7Xrpp_JTbubv-Acbc5x3llKdReYKkHA21FSLdBpgAabYZAFKMqZEU2Z6xDMBmLHdUTP1aALLVmNpy_woSBYl53R2Cc3EZNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/83837" target="_blank">📅 16:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جنگ کنسله
صداسیما اعلام کرده حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/funhiphop/83836" target="_blank">📅 16:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/83835" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=iDmD0I_eXl9spfimrSQJCGdp9jRIolunQwaqyDXux4lIesPj0I61YVLZuEK3gHX8LCD5n_4Mqp89o6hjm9zvY7fcLQQZBr3Z2ka-xA6NF5ZXZ62yL0RyNy25Mvv_LNNYyWPsbCnnRNDnCc1ip1fyTmHcXHhGOPhi0AsxWikRL3Iew9PK0AsYVAISeITP86EDrNfWGqg3Pfmw_mcA6K-pvnbX2bmzuiL0wC-K6IxqU_QRdt-AtBTfLAJXuQ-PxEmKpPOUm_jYMX7qi3VT4PIWhc--kLhEHdW39Z2zHMs8sWDMbIIo3qNHdFeWtyQtTnPIM7gvzs_kHDik8M59izNxZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=iDmD0I_eXl9spfimrSQJCGdp9jRIolunQwaqyDXux4lIesPj0I61YVLZuEK3gHX8LCD5n_4Mqp89o6hjm9zvY7fcLQQZBr3Z2ka-xA6NF5ZXZ62yL0RyNy25Mvv_LNNYyWPsbCnnRNDnCc1ip1fyTmHcXHhGOPhi0AsxWikRL3Iew9PK0AsYVAISeITP86EDrNfWGqg3Pfmw_mcA6K-pvnbX2bmzuiL0wC-K6IxqU_QRdt-AtBTfLAJXuQ-PxEmKpPOUm_jYMX7qi3VT4PIWhc--kLhEHdW39Z2zHMs8sWDMbIIo3qNHdFeWtyQtTnPIM7gvzs_kHDik8M59izNxZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/83834" target="_blank">📅 15:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امشب یا یمن کونش پارس یا ما، همه شواهد نشون از عملیات آمریکا تو خاورمیانه میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83833" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83832">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قرارگاه خاتم: آمریکا میخواد با چراغ سبز کشورهای حاشیه خلیج فارس بهمون حمله کنه، بزنید همرو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83832" target="_blank">📅 14:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83831">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83831" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=FE9dZLyyDwATXeyYiKaHm_gt8RSyCNyLWwjDzAQN2Rwtui9kiNDfpSwNSzPLKSrT64jjyzAlP0V5aAeTN6FCGrbgJX0GPXuPddXAIjcatf2AtMDJzZ2yc1K1LJIp9__cQfiRx48GLDrW5xa39elqqGzFgeyPviKNrCFDNFeZlWcOedlhDTzvtDflCk0RIODPFCsWeP2HfuFyxbasiNlRYE7xzn60oFXfhVAhLuUE3zcWxmo7-o6RWBKsmeGgaT3FZDwLC3umDADYszl3G4DQoStdOHtzpMWZyzDIdPE8F7b6SQGjYKppxnKbBMAVe8fVeKRXZzmmI2dD3qB-kyXzAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=FE9dZLyyDwATXeyYiKaHm_gt8RSyCNyLWwjDzAQN2Rwtui9kiNDfpSwNSzPLKSrT64jjyzAlP0V5aAeTN6FCGrbgJX0GPXuPddXAIjcatf2AtMDJzZ2yc1K1LJIp9__cQfiRx48GLDrW5xa39elqqGzFgeyPviKNrCFDNFeZlWcOedlhDTzvtDflCk0RIODPFCsWeP2HfuFyxbasiNlRYE7xzn60oFXfhVAhLuUE3zcWxmo7-o6RWBKsmeGgaT3FZDwLC3umDADYszl3G4DQoStdOHtzpMWZyzDIdPE8F7b6SQGjYKppxnKbBMAVe8fVeKRXZzmmI2dD3qB-kyXzAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83830" target="_blank">📅 14:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=RiOcwpzYnA4MUPou51FVMCEqsfqnN1imBPL6hkDKF4ReSgtGzBwvY2Wvpi8JxD-B-BHm4WFdTrKGI2LEEig5-3zwe7UnaSthnVLrv_PQXrOm56i6ljfXmBfj-7AJlfwJ0LdZbnJWzekvnmBSqOofyeK61uSub_5qE1q3xIRkMuEz4s_v0bY3hdmoyJWHGYJ6tVcodX4hHM5waMOJTC7gjCt9GjWWiz4_cyEdKnWcquT8OVb1m4AW_SW7gl_CFsCAi_ovHR7gAnmu2fR4K-T-cjIRIs32wQaBwf_cNqxQUs4fbys2CiC2IiJmYHed4mP2RR0kc_vl5m62P5al4PhkQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=RiOcwpzYnA4MUPou51FVMCEqsfqnN1imBPL6hkDKF4ReSgtGzBwvY2Wvpi8JxD-B-BHm4WFdTrKGI2LEEig5-3zwe7UnaSthnVLrv_PQXrOm56i6ljfXmBfj-7AJlfwJ0LdZbnJWzekvnmBSqOofyeK61uSub_5qE1q3xIRkMuEz4s_v0bY3hdmoyJWHGYJ6tVcodX4hHM5waMOJTC7gjCt9GjWWiz4_cyEdKnWcquT8OVb1m4AW_SW7gl_CFsCAi_ovHR7gAnmu2fR4K-T-cjIRIs32wQaBwf_cNqxQUs4fbys2CiC2IiJmYHed4mP2RR0kc_vl5m62P5al4PhkQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83829" target="_blank">📅 13:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83827">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=qzXTTdS7NoCHqcInqkKWAaUvL-rrAi0uaHwbfcjP2uSKInZwnHCHBvdVDGdp5s331h50QasyOa46uI3ej_66I4mBO0GsGVToskFSsJlPfKN8YQTYRi9PGHJA34YinOJqSKQ89RPDQg4BGGClTwSDkCitW7fwd2pN9WclkwIa4-o3gABRVVC5H2njF0HYPEaBbbEVqaDoADbjsu-TGztqpsLoL5xu5fLd18vXt-auRjcg5x_wZLHG2nlakJ98BSDgYmAySd6JdizTXAPKlkniDf3yx2wxmJrU7I-YBGTM75axrVCPxfndI1XOy4s8_oixbrA4ODy4nE1viI-pLCS4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=qzXTTdS7NoCHqcInqkKWAaUvL-rrAi0uaHwbfcjP2uSKInZwnHCHBvdVDGdp5s331h50QasyOa46uI3ej_66I4mBO0GsGVToskFSsJlPfKN8YQTYRi9PGHJA34YinOJqSKQ89RPDQg4BGGClTwSDkCitW7fwd2pN9WclkwIa4-o3gABRVVC5H2njF0HYPEaBbbEVqaDoADbjsu-TGztqpsLoL5xu5fLd18vXt-auRjcg5x_wZLHG2nlakJ98BSDgYmAySd6JdizTXAPKlkniDf3yx2wxmJrU7I-YBGTM75axrVCPxfndI1XOy4s8_oixbrA4ODy4nE1viI-pLCS4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طناز بعد جدایی از شاهین افسرده شده و هر روز داره با آهنگای غمگین ویدیو میگیره و گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83827" target="_blank">📅 12:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83826">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=jKT96f2TGqNjOoFVYBr7ZPeJO272BK_PvTVe913dcVZotCb2-sX95xJLM4tHFGmMeXJl-uAyvbQM4ttdWNzizDkEiKUtUXH0tl6aSqO1ta4zJXAbsOQgHPpoKTtUDsQnED-qCAS0-t7RD6Saf6u2i3GSIcUXhf-CfrVQe6UxpgzCyX0TNGYZwrBjqpA6f3UU1cCSP7wFTwfDri1XOAB2XriGdS9Uj6yrm0QLn0wqzxDPjHlwjwGxTenrLcZ18I0BQ1w95EmJTyamKU4BWA2dmtqGdUPU4NHtOoNYYnADq4ir3oh5Gsu7uHfntDwTdi8mm1rs7tc4OdaS3LZNf3XW3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=jKT96f2TGqNjOoFVYBr7ZPeJO272BK_PvTVe913dcVZotCb2-sX95xJLM4tHFGmMeXJl-uAyvbQM4ttdWNzizDkEiKUtUXH0tl6aSqO1ta4zJXAbsOQgHPpoKTtUDsQnED-qCAS0-t7RD6Saf6u2i3GSIcUXhf-CfrVQe6UxpgzCyX0TNGYZwrBjqpA6f3UU1cCSP7wFTwfDri1XOAB2XriGdS9Uj6yrm0QLn0wqzxDPjHlwjwGxTenrLcZ18I0BQ1w95EmJTyamKU4BWA2dmtqGdUPU4NHtOoNYYnADq4ir3oh5Gsu7uHfntDwTdi8mm1rs7tc4OdaS3LZNf3XW3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83826" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DairUmCgEotNDCiG-Zv3VQNEqQmd0yIIszliJNy1y_6vJkGxzlKxtCJuW8BmIu695HOk90ToTGfn4OvmF7TGg9XqvHpg_lsqBoEA7W0Pjwx68vlY8Z9eXrT6TRIcBggStKTLrcETwEZRdb7Q4glk_mIgW26CrhgkW9fwofxFc8OE5-nDaXyBRwmjTtIIAW7gSVDZFv6UcRqhVSP3vV6gDNrTSCB3wjbwcZK0aH-81q3HHWEVy2CtoZ4ZbSoRNdsqMWBoeIvLlGbjkFrAEt-oO1fwztSs5ZIEHNdIimmV0yEr57h5bmt-Qr0vEC7erUWdyWH3wPamiyc8plh2gaVlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بورنموث - لیورپول
⏰
ساعت ۱۶:۳۰
🌎
📲
آث میلان - لچه
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R29
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83825" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83824" target="_blank">📅 11:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83823" target="_blank">📅 11:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83822" target="_blank">📅 11:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">صرافی او ام پی فینکس بالای ۳ ماهه پول مردمو به بهانه های مختلف بلوکه کرده و نمیده، همه مدیراش هم داخل ایرانن، حتما باید فرار کنن که براشون پرونده سازی و پیگیری بشه؟ حالا اگه فعالیت سیاسی داشتن زیر یه هفته بازداشت میشدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83821" target="_blank">📅 10:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU63l6eH4aCx3B_g02nuvIbCEQu0UC7_ESZPuLrYAlTmt5P7ykRiHw_oK1pwPvyprM25KkztK5AQFctzq6RRXM6wXTPtcOZKEfhifWTdzyszqP6CGAhfn2rgFn4WoCittylXT4KStIGvjlagDxL9V-wX6mGaGgg-QhuKBidpyQxVlzL3eejYEx91K60y3Mk72QVbqr69OMeV2KCaDSFgYdDwPCe6MXLto1Xqi-WqJJfgzd6qyDLn8b0ns2v8RSeq8U2r3c0FquDTVq2qTGBnW0NIun_Y3-C3EemypJ76RY4nE_WQWNG9YrnOdTUQ3IsrCbUPNeVMA-vtK1O7JdUQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلوت کنید این‌بار واقعا تعویقه
تمام برنامه‌های عمومی‌ای که ترامپ برای امروز داشت (از جمله سخنرانی‌هاش) به صورت ناگهانی و یکجا لغو شدند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83820" target="_blank">📅 05:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDG3wuhDwyS7SWOso23Z1V8Hzf0Lh33Dr-9dV4EwmkfkRd-oj7sdLf2AGPGZUM-hOfeU9Sp9vTGioOlwmK4ECptnyvAtaSepwyLGsw1maYqtWTbBgmP7j83WOi5j-TppBVsC315ZUypeDghjQEnfZmOlWNTb1SYVDggrrgpEPwJokRT1Gp0sBzEkbmts4-M_z8qe4ULRb4lXGgqlWfVdZJrVJ2fFa5UmA-2FNI1YZplpDwkxiFUp20exqKoWti_TNjgrQMD3meXhJhzYOMei3KeKsIeb7adP9bTm9s9Od5a2dulgT_9FK7THE5pG67Qlc-4c5oFItTgTf8XH7r4hdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83818" target="_blank">📅 02:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پیتزا فروشای اطراف پنتاگون سکته لاپایی زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83817" target="_blank">📅 02:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حاجی میگن ترامپ یهویی برگشت کاخ سفید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83812" target="_blank">📅 02:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83811" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83810" target="_blank">📅 01:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی.
تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل، فلسطین، اردن، قطر، عمان، کویت، عراق، عربستان و سفارت مجازی آمریکا در ایران به صورت جداگانه و فوری صادر شدن.
یه هشدار کلی هم وزارت خارجه آمریکا برا کل شهروندان خاورمیانه صادر کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83809" target="_blank">📅 01:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfrjIzgu1dFTiqy4qM0kdFGRqFfOA3mtIXrNadBkd5LQ-a_RyvkOY-ffk21y1YP2W7psM8CZMG3w_m-bTaWZAu9pHaMlMyRQJ1dqFR9vzNJYdRDzJRCXtj9WUuMGN8cRe9j5XOxvFT2H8Tu-TxcM_Y2GdO34Q2pK8XwPt4m3crnHVGBfkEf322mQsu_o6CRoIpNkbg2uJcYye5XkqfI39eW0hakRe0vDz_BbKbNN9jfkgsUlpPXILJGpUFi1-4NaSwzNeHPnltemlPS9jdGSQe3nAUWsQ1zidKMCLtqFK38WmrQGverWJ3teUJPD22Nznjv5oo_kuY3DhYdq3xtlmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر نمیدونید باید بگم سازنده جنگنده A-10، یعنی شرکت فیرچایلد ریپابلیک(FairchilDRepublic) یه زمان لوازم خونگی هم میساخته مثل ماشین ظرفشویی.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83808" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83805">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎓
آکادمی فتحی  انتخاب رشته تخصصی کنکور ۱۴۰۵  با ۱۶ سال سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما  مشاوره در ۳ جلسه: ① بررسی رتبه و شناخت علایق ② بررسی رشته‌ها و شرایط قبولی ③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83805" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83804">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ6IWJ7upLYiXuOAAf-OMLxQu91jTrSxlFevnpR__r44jZYhw1ZH5U7CVLyxep6eiXJziN_DkPK-l1kyO5CHD-P1-yY6O7lTX8OpAIFpWF4g1xdh3Dv1-wW_N6HKwK8HEODAoHhFqJpOc6bgYngEvjoeCrXeoiwmOurfbt54PrxDkYO-femMdDu9MoVDONf4LuLe3XxfIAjTrcNHqkoIvfYb3Sp52457BNRaAtMDUiUnxUQrTYdNOOZw2i4ooQP_2KJgfFo_Uhs-UU04AGR2x-qgnNhCoj24geWrxIdKTeqaIwGMypKkLeKROynrD7OQ4WwbKxg-p0Vq6q-MgNJQ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
آکادمی فتحی
انتخاب رشته تخصصی کنکور ۱۴۰۵
با
۱۶ سال
سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما
مشاوره در ۳ جلسه:
① بررسی رتبه و شناخت علایق
② بررسی رشته‌ها و شرایط قبولی
③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری و آنلاین
«انتخاب رشته آگاهانه، شروع یک مسیر تازه»
https://t.me/+XFqj-oe9FrdmYzBk</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83804" target="_blank">📅 00:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، یعنی چی کلا ۳ گل با یه نیمه اول سخت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/83802" target="_blank">📅 00:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/83800" target="_blank">📅 00:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83797">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یه زن دومم داشته انگار پوتک که اسمش دُرسا عه و فرار کرده</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83797" target="_blank">📅 00:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83796">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83796" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83795">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83795" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83794">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جواب آرتا به دول سه سانتی گفتن پوتک: لابد آمار غلط داده دخترت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83794" target="_blank">📅 00:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83793" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کیر تو آرتا داداشم رافینیا چه هتریکی کرد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83792" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83791" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83790">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bd75rtBnQQ8xTI5nx9BWn1UqWYMhFg7NJywK78crBRGDekp0r3XVrE2AkeuHJUgzLc5kuQ0e-jgXfqJ5IoA4ljzTmYY5LbV_1gxLXDmrcSTWsxG-2JGDv7dTEASeznQsEnKVLuYc9nEL15ecpGtSXPpHsORVHW1_h_59zjbDR1E4cN7nPd0UrsmA17HPO-x-izITSN5ItGJXjCkzSAMlfBjzha95TekUyGouOk8aJXOhpkNlfPpTkqrqcNQG7IfyX6AlPVhyMkbYVDEDAYTyconsWipTJHzl7Uab29RM3gl2EIaxaHHX5gLR4ZloZlTLtlFt-kEfS_IQ12nlkgEmKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83790" target="_blank">📅 00:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کسحل رسانه ای به من ربطی نداره ینی چی</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83788" target="_blank">📅 23:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">به من ربطی نداره ولی اگه پوتک هرچی گفته دروغه اینهمه فشار برا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83787" target="_blank">📅 23:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83786" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کوروش به معنای واقعی کلمه دیوونه شده
داره به تمام مخاطبایی که رو پستای فحاشی تو چنلش ریکشن پوکر فیس (
😐
) می‌زنن سنگین‌ترین فحش‌ها رو می‌ده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83785" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کوروش وانتونز همراه با این ویس، آیدی یک اکانت تلگرام با نام محمد باقری را در چنلش شیر کرده و مدعی است که این اکانت، اکانت تلگرام پوریا پوتک است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83784" target="_blank">📅 23:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuwvraI3NJAmttknELpK8piNEe6QMWwA7uwgESentO2U9A1v_Sc5o50rIewo_Qxb7nAuYdzHpoZFbgEi3zYZw2XNbMnlb2DXZupCrcWvuAgjqOUhI-BjQ1FfHtuvIvvm5NvLN3MiJPPwda-HzxSxzyQYPw-ZsGigfiQ9QAAcNDKxXpn2TooppxeJQmrAcP1-mT-wYcrMJ2KJQ2MsnaoUZPHt5G6Lrtx8FsG0sOvkNMFtKF8nhHBmod9Ecxs0EzPuLRZ8NeXv5E4zFkiTdgg5RToQCrklHAmbihntyg1AMZFyPj-PnjAU4o9YCsD-S-lHYnwF1397bmR6bP3oLKynng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که امشو بیداریم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83783" target="_blank">📅 22:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEmHOQOE4w6_K8p9Lnwp_2_eqHot9jAKKJLQvDgXaZWm26WhQGkb8HNkoWeblERyskaVAvECtxW9GF4LmSzgMVX9FP-7azwgREMLF5uJFjKYu5bNFFF_4mnYWtQi2Pr9arLvMtimIlMHkQwyCxmStMoQJzLbQhpbnoU8TVowUM55zuW5v1IQ_W2mBlN2pmgGfw5tgKhxCmEPansbG4vetVeFxfRYOSd1xTi_OCmw34qBMqymHO3ygjl8iOjt9Kw78FvXxS0m-TS5H-ZKUCwPHtW9OBMM1B9IKB5L-FZf5WRzCOC45YMvpv-z8LnR4mvDWDvsm4PnyaL1D4fgU4s1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که امشو بیداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83782" target="_blank">📅 22:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83781">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f81d21e878.mp4?token=JzGxata3OpcEJMAt-YRNJrUc6BRYqkJTgqepjd0a3iTkeEydIy4LgGA5GCmCHCNOt8iCVoW58idh6B1nvU2JxdCNUYnk9liCYvPEFxN_Blnd_XFQRBv_RoHvle8w_m09huzkxYmO7CSR8IrDsLyLrKvqJ0g5NL3dpTYdpC37slu6rQR4etncYNLTejXeViz9ZT_VM8xDp2xFuiKfX06BSQq3IPU6O5JessTEfD1IUV-QlV5J39S1CDZ8EUDhLYAczTOW6Qp6S-uG-vJNYuxM7PrO0_7EYoaC8A-eKJHl3788rO0uYwzrG-lxskadPvt6-6P1gn9ESGNhyv3Td-h95w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f81d21e878.mp4?token=JzGxata3OpcEJMAt-YRNJrUc6BRYqkJTgqepjd0a3iTkeEydIy4LgGA5GCmCHCNOt8iCVoW58idh6B1nvU2JxdCNUYnk9liCYvPEFxN_Blnd_XFQRBv_RoHvle8w_m09huzkxYmO7CSR8IrDsLyLrKvqJ0g5NL3dpTYdpC37slu6rQR4etncYNLTejXeViz9ZT_VM8xDp2xFuiKfX06BSQq3IPU6O5JessTEfD1IUV-QlV5J39S1CDZ8EUDhLYAczTOW6Qp6S-uG-vJNYuxM7PrO0_7EYoaC8A-eKJHl3788rO0uYwzrG-lxskadPvt6-6P1gn9ESGNhyv3Td-h95w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب با این پست اعلام کرد که دیگه با فوتبال ۳۶۰ و عادل فردوسی پور کار نمیکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83781" target="_blank">📅 22:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83780">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4x-aggt86kku_JsAwN1FZtFFaFpowSaQVByNvc--aLj6H5ZZczYiR9Z0U5k_1sXgPVeCTksHBsM9buV4h4xTx2iqZD_5mbyqyBk-PEIOX6Ml3RKCsfsz6RR5qeQa0nDHclbBjP1gnq7BCWtA1Ip9G6M3efR8EdV0aoYJh74_SFpM1aLqKEb_6C3ZlSwjOsGs2ZI9pleKrIp9RMJ3kcWZwbuTzkGWpFDE4vm07HbCAD13GHp085t05Sc3C8hA3EdoPwo8rVYvG451b5fl1ypyVDZIHh9uhs9OXfOsWrfxq5WwmTb2RWPBvO-WelBXXsmqNUqzzjt_EL0-bH99cSUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرتو گاییدم چرا تموم نمیشی تو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83780" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83779">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozN6jKTLPS0465D7OhsZqC1rv9VmZI7WvE-JeuKRSSStQKYPbvT6laMrJNUNrwWErdYw2re0Lr6nL4c8RYwtxxtiCKm_dua4uHyW67N5rWtjKRpYJYBwZBINI8_HV3U2dUKvMEvXc2tpOqjxLqPzPAi_JWff8HC4yK6I55EOb63_iBQr5NTKduc04llGZXV4j5jxEP5dlW-Gi8FGWe4TeF3vh-eyrtYOuQe4fDADVkqfH-Nn0VESyrLXbkY4tk9pWz-Bb3lHfwkZJ_adjOqoQRVQ7RMRBme1Y7fl7IB0K0vsZrrtHwb46dEmMROLyQYknQnF3GNiz-SKiCWS2AcHBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
10٪ شارژ اضافه بر روی واریزی‌های ارز دیجیتال برای کاربران بری بت
⭐️
🌟
📢
در سایت بری بت وارد حساب کاربری خود شوید.
💸
از روش ارز دیجیتال اقدام به شارژ نمایید.
🔋
🪩
بر روی واریزی‌های ارز دیجیتال تا
0️⃣
1️⃣
🔣
شارژ اضافه دریافت نمایید.
💰
✅
ورود به سایت:
👇
🅰
g28
⭐
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
🌟
کانال رسمی ما در تلگرام:
👇
🔗
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83779" target="_blank">📅 22:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83778">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83778" target="_blank">📅 21:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83777">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کوروش وانتونز با استناد به
یک کامنت
،
دیس‌ترک خود
را پر پانچ‌ترین دیس‌ترک رپ‌فارسی نامید و به فدایی فحاشی رکیک کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83777" target="_blank">📅 21:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83776">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=I6HGrFy20O_3JFhTyiInybZ3VsRYqXrlg0m5HZqgb2U4uhsrYoKYC5RiA6PBqvHwBJubVfY2QCg68r2lf5MfGeTAsxM7hNv_9D-uzLeUlgs3kveCtbA3-AVMAKT0APLWksNXtAWVrsOaEZHOFG3bYXeuOYuDkdDFMeSszRueiI0mcNDMFT-v-B11mcsC-jZBcAaHslRkGb27NLt-WKnIIXuNS6khKKe5T0TlbMYqHke5NExcxDMhwQ18jR0OgpGR8MhwKngCK3z5LHxZ4INacQ-692SZHB5tHBQjIKgTUaVpAPQzXJ-McGCxZYCRC5Y9_M6aMBncmu8oF0iW6DGtzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=I6HGrFy20O_3JFhTyiInybZ3VsRYqXrlg0m5HZqgb2U4uhsrYoKYC5RiA6PBqvHwBJubVfY2QCg68r2lf5MfGeTAsxM7hNv_9D-uzLeUlgs3kveCtbA3-AVMAKT0APLWksNXtAWVrsOaEZHOFG3bYXeuOYuDkdDFMeSszRueiI0mcNDMFT-v-B11mcsC-jZBcAaHslRkGb27NLt-WKnIIXuNS6khKKe5T0TlbMYqHke5NExcxDMhwQ18jR0OgpGR8MhwKngCK3z5LHxZ4INacQ-692SZHB5tHBQjIKgTUaVpAPQzXJ-McGCxZYCRC5Y9_M6aMBncmu8oF0iW6DGtzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیانو اینجوری تهدید کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83776" target="_blank">📅 20:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83775">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سهام شله با کون خورد زمین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83775" target="_blank">📅 18:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83774" target="_blank">📅 18:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">برایتون یکی فرو کرد به ارسنال
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83773" target="_blank">📅 18:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MULnWqJZfUCFkMYh4m8zrTSh9_chZMPbuTauxW0g6BeVPBwTqh0B3VsasT8ZXEilw2RiCpQ5zHbieybJJql1JZZkOASfh_Dl4rs28OHhjaZY38Qivg8-NkFFuCnLNxSAWRFzMdKWOMpcN1t9FI6qIAKan3RvgxOJaF6WNoW6_agZtar38jy7X9yt9rkP6pZnkLHhGvgaZxhg15cMHcrR4VO0svHGGBw1nbc3PKMyGTz_7G1Ly4wC4czO1Er5NjZIduK9Nvu6Va3LdztIuSZLFFPGuMZVgE7hq2LX6BD0Sm-mmTHm9yUkNatY1Yd0tGLaHZRzDHRE5-DSORku0sxd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#حافظه_تاریخی
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83772" target="_blank">📅 17:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/83771" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83770">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تاتنهام بالاخره گل زد</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83770" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvHO3WWXc_1uxBI-yoQe016qlb4ZjGCMQTJEnKypBPnZoL5WA2nDM6sGQbNL1KugtQ4ySEWAfSC1lllXFMYSGv1pRhQq2hWFygu5mrwtdTJdtzmVQ1LZKP7eDCUA080a7Ijrs9rVHx1gba2k3Z6rklfILYg_q1VMlvGNp2EXLvfwWRdyU_KJiP69ZUqUWMs_k3GzYbZsB15iQRzCH_EliLW4CXaWiy-S5-99cVt-MhfRS3BBAHXRzl65s1QV9znFHxeMDxuiOilWN_GReF1CYu8UJo-6FhnURyO5WL2Q_Nzqeguwzk81UWs48YVQcWCz3o7HFOYq-jRFq_ubpvJn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83769" target="_blank">📅 16:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqzsD8kNxlEEXXNdf0D6uSfZf_AWv0FcahKRV0dyucM7VCDrHIdJ8GAaqed8mkflOMYIPJkU7yb7rwXKXR4Cc3NRtVsESnjPjUB8j1yZohXM3qy_uYB9q-8fpei0pu45CMvGpd-zo3YMJZnW-2MW3BljwPx__CZZbeVgs6klb65UJYoMlOIeWmcvAu62b3VCoToTvfYodhtuakSIQ5H7OT04CGhIGbaKXjwP5NCnPg83dY0QUjXuV6Ttz7yiFtPjAw7WJIOoi04J_kCtZraxhShzHnYBQ7nueBdoqmTSSf_j4DAEWvpQ22whP878rKABCAXbtjAljFpcA_COXbaSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممنون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83768" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqRzla7_lFYgTyezB-1mg9jANKbPgtn_btQJkgwEFgLaJxzXtA-aH95xuW-vhhPRLHDD8YUJTC9-MeyRNJla66QBgEOLG3qNqT-Ci7y32nXVZneieD-L3LwC2JmX9uljF1-pax6fxmSfcrLajcvNGF5_fKvZ8dKlE5jqbrsZEJL4F_Y7-fqIRXE9ibCLWYxmB70thohtM7_TLbRNwFihh4JBhoPqAz-iJWKIsKQf3E1eSGtapGQ2wKTIFQMYrGIyErJvdywSgH5rYWz4zNShA1LVtaFgrYhwZW5Quu2-YU4eWMXv7Wv2Ln_74RWc1l5_u9kl21FXWkc39api_bEqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر قذافی که 7 ماه پیش آخرین امید مردم لیبی بود و مردم لیبی خواستار برگشتنش بودن و داشت با رسانه ها اوکی میشد تو سن 53 سالگی ترور شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83767" target="_blank">📅 14:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به قول امیر پارسا و ناگهان کص ننه چلسی</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83766" target="_blank">📅 14:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خروج رسمی امریکا از شورای حقوق بشر سازمان ملل.
آمریکا اعلام کرد عضویت و مشارکت خود در شورای حقوق بشر سازمان ملل را پایان داده است. وزارت خارجه این کشور شورای حقوق بشر را به ترویج ادبیات ضد آمریکایی و مماشات با رژیم های متهم به سرکوب مردم متهم کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83765" target="_blank">📅 13:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSL5PI4uch33KqNZf4xBzAQWAGAORvhP6XA83Ssayg2Ut11iLiWjb0-kFLE-Tj_Edod8HNQOmf41xZ__39mlherEbY4rxSEu-wSxxigkY3Yg6MQpgw0Q9My4OaebPv7_r07OymTw80KvkFASZ2CrLWth981KfSNFCMC03SFmUYsEtjTUZL44VVnS3sIUsUOrxuTgQPcwF-A8guAdLsqFfHS28tTW5Yj16tuDpnyc3hfscG7XeXbhd81zrK9cySmoEbCaTiiOK_OeVAXRSA96-B0UAtIUmSIi7_UJPXR7F5qlN-RXxV8kIBVuQfSGZyAQago9mZlCsTGk0V6M2Blt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسدالله مادرت گاییدس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83764" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=KNK3HmOKIkCIFoi2siPveIO_W4s90OK2uI4snRAwAxUIybmMvO1yuVpjokDFtU_pKSE0aqwhyrcHQMT5sgUQCeGQuVml_mHAX5ZCNtr3EL7Se8tKfaeO8_MRvHrpwgLhddl0Esy0W-C_BasCIjSr1h9SM_4rax9gjWIAcjRKXWvJCEqRZZXmMzQWwhaYP1UzXFKhPD_H9MGj_a3UB1mazQQWZbsuqL_YcUvSdnx0BohAicXkTsFhe9MmTPBeBLz7OTsRI6gQ3wUVZlwHoAo_Qt-mp9A3sGeBQHclUs4EnpWN6xnNzKxwzxc9fK5SytVKiDtdLD_KXGJmlrqgtHtZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ff3a5a22.mp4?token=KNK3HmOKIkCIFoi2siPveIO_W4s90OK2uI4snRAwAxUIybmMvO1yuVpjokDFtU_pKSE0aqwhyrcHQMT5sgUQCeGQuVml_mHAX5ZCNtr3EL7Se8tKfaeO8_MRvHrpwgLhddl0Esy0W-C_BasCIjSr1h9SM_4rax9gjWIAcjRKXWvJCEqRZZXmMzQWwhaYP1UzXFKhPD_H9MGj_a3UB1mazQQWZbsuqL_YcUvSdnx0BohAicXkTsFhe9MmTPBeBLz7OTsRI6gQ3wUVZlwHoAo_Qt-mp9A3sGeBQHclUs4EnpWN6xnNzKxwzxc9fK5SytVKiDtdLD_KXGJmlrqgtHtZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مصدومیت خوان گارسیا فلیک داره رافینیا رو تو پست گلر تست می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83763" target="_blank">📅 11:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7124a1535.mp4?token=hTbmT-Uy82XpxCSURYvIq_EcJqT0AzKmvIllhoPUA7CrHxxqGNi-Z-Lsr81DfoGBhDHfadfVcbNxByNi4G3Yr8uyTa-T8wKLVHUpKKjbCGNxxdxTv7_bjR56ig8clnJjeh3SMiPViu_tA97_K9Gj65EG13HQ75XbwtCxh9AldMo46VCt_PgmusGTAwLAaBjeTWmGGR5OxXGBe_evp5w3qHvXgNSjV2UU2UO45OJvn6dBCb-6p_MX9_HL2qRTbTg3et-SNwg_NISk2PmP9x-8gYGrwvh4WAfH_LioBa5ZnEWMDoKqeQaNmi8b8KZVVGcWnGBvcvKHdwQrODhDYaY8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7124a1535.mp4?token=hTbmT-Uy82XpxCSURYvIq_EcJqT0AzKmvIllhoPUA7CrHxxqGNi-Z-Lsr81DfoGBhDHfadfVcbNxByNi4G3Yr8uyTa-T8wKLVHUpKKjbCGNxxdxTv7_bjR56ig8clnJjeh3SMiPViu_tA97_K9Gj65EG13HQ75XbwtCxh9AldMo46VCt_PgmusGTAwLAaBjeTWmGGR5OxXGBe_evp5w3qHvXgNSjV2UU2UO45OJvn6dBCb-6p_MX9_HL2qRTbTg3et-SNwg_NISk2PmP9x-8gYGrwvh4WAfH_LioBa5ZnEWMDoKqeQaNmi8b8KZVVGcWnGBvcvKHdwQrODhDYaY8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اشکان شادکامی میتونست باعث بشه این کصشر قابل گوش دادن بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83762" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiG30pYGkLODV2toM3-tRr5hkJ253oea4_8X9-VWMADHZVpJrwb2AhjO6UdbERGBCZatDI4FJeMRofey4DWz7m5vrXVK0t8N2P26O8-cKASmMTIII-44hBkKVqXQkLmqtH-EfQJt4QqwAX1jh-RM4hSCHA1p9cATbvP9M97WHgFv02bI7lORt_uasnfdAy25g7UcafFFGOA2QYN3ne6-rVi7thiPoRpfjJxCI3kTSL95OihPkn3jhA55yKYLIvE4ARXo0nFxLreF_TRuHxoKYdvDSlAU7pCEBKP91s-UysMDiHTmpHRPkPZX_JpKl8ErLsBGDeUoYiaSmPWYAyPPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس شیر ایرانی رو بعنوان "بازیگر معروف هالیوودی" معرفی کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83761" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj4Ji6PNkLMLvXargQkIXaXA_LhPSSgbgFvluj55YfS4KDu3_GzIubHOeF4Cdg00oSYm3aAPuhaCLJdlTiXRB24VE25PmJg0r-FZJxUV85N6JY3f-V3HWkEEqZHkpcrl2KnjBOrc5CjErPz86VPPKmEQ4iY7KptPKnStwYg0ZUeNUw5P48qzx7mkr3wNSJ2CjRy9XQU8ioo1adm10QVqmbtulE9oSo-ReWh0eVqGMPbRmK0_Q8Gr7AkUabm5TUp2ozqn9sXoLwhpPSz5qoGu9-Q8RQ7Deqg0YUmOqzw6q-7W72MM-3UAQgzxTU0C_Fkmr-vE4gJmwuq1d1TJVrptLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
سویا - بارسلونا
⏰
ساعت ۲۲:۳۰
🌎
📲
اتلتیک بیلبائو - دپورتیوو الاوس
😀
ساعت ۱۷:۴۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R28
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83760" target="_blank">📅 10:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">افزایش قیمت بنزینم نتونست صفای پمپ بنزینا رو کمتر کنه، کونمون پارس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83759" target="_blank">📅 09:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این امیرمحمد کصکشو با تیر بزنید خیلی نرینه به مارکت موسیقی ترکیه، با همون بلوک۳ و سمی جنک و اینا جمع بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83758" target="_blank">📅 09:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مصدومیت اجازه میداد میزوگی اصلا نمیذاشت همچین سوالی تو فضای مجازی ردوبدل بشه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83757" target="_blank">📅 08:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2c6f49b83.mp4?token=L8umKcNMeMg_-Fe4EI0cWjQ3ExlbINsCvMfhg_QUl7KdvsWfrRfMl8N6IKZmLl38zwb-6QVnhjBNEGfTUntekq-xpHGcoofxnaPFyDyIapkcO3p1WNUcE2mdvqwo-dB1DlHeyHaDtqLiyyEUMaH3MAxBGmayI3Xqk7RSWXJ3ZNCKc12x38v69GFng3TXdSe3ilQytYCU3UNhbEaPxTvVqIO0pVQYjvg18G-DhJlLZ9GqvFF6YCsEh676ezSJdWyfh_IOYmzqMlPPFHTRWbVdFRtffJMvHeT1yzlozlrBzDwGbPPWNJzEEamPvDmfSPjv-Mgh9j0lHGUlXLUWgSZjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2c6f49b83.mp4?token=L8umKcNMeMg_-Fe4EI0cWjQ3ExlbINsCvMfhg_QUl7KdvsWfrRfMl8N6IKZmLl38zwb-6QVnhjBNEGfTUntekq-xpHGcoofxnaPFyDyIapkcO3p1WNUcE2mdvqwo-dB1DlHeyHaDtqLiyyEUMaH3MAxBGmayI3Xqk7RSWXJ3ZNCKc12x38v69GFng3TXdSe3ilQytYCU3UNhbEaPxTvVqIO0pVQYjvg18G-DhJlLZ9GqvFF6YCsEh676ezSJdWyfh_IOYmzqMlPPFHTRWbVdFRtffJMvHeT1yzlozlrBzDwGbPPWNJzEEamPvDmfSPjv-Mgh9j0lHGUlXLUWgSZjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت اجازه میداد میزوگی اصلا نمیذاشت همچین سوالی تو فضای مجازی ردوبدل بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83756" target="_blank">📅 08:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUDX6uHn6PGTAH8-0mmEP9TyhgyyER7a_nZYTyiOdibqi4QgvR0qUDkCwz8WaGe4s5nxySBMmis5vWutNGcU_bOnQA4UE0ItrhUDp9NT7IZtk1c-FPhFUXly2eatgAllRswCv_OaDk94cMh4rtTv55s-Gy1zEi5fySGAvWBrbzUS43O9CY1Zs2k4uG2CGRN1eTc4B65SlCHNmjosQn4S4bAUTrlZvrLiCg-FzwJyn2k9xtkdbd_e18xRRYGFuVApzv3CRTyAy7dmLfq3bWqx69Wq5oT-bM8itUETiW3UziSGHMpmIJo1l5_MR_5gbyDMvhJVN-qiuMoDUqlWKxcPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرفان کیر تو دهنت الان اونی که باید این گلو میداد تو میبودی نه سیجل.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83755" target="_blank">📅 07:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAGDkIR6_jdbOTzYNWftLx3WVi_jwC-mIe7JAJRq_-8idhurn5Yi9wMIuS-Yc63nSIGXn44q0SW_dvhJ5a7tiIgnNT_E7MVhnlJaZJQ32KbIuMVcstXD3bHg_xGK94h2rfXZICLaYvT7lMuaaAi-PJfD-8fSqaoHVzEPDZhtSp3pMP41dnKXLGL5hTLsWXj4d0KK3CXvJvwI0Cn8ivMaq0ia-SdfhfJcGM83ew3PRAuoPCVgbCtHkXOIFkoe1p2Gxp1baL_dDVmxMSlbUuJteUa62HGzkxxaP9dwe41_5kH8O1bSOrHfZ71ZhAWN9FUQoZoSqqHaLTSH4kWdD03Quw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83754" target="_blank">📅 02:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دیگه کم کم آخرین باری که یه نسل چهاری سوپر هیت دادو یادم نمیاد(اگه کصشرایی که با پول پخش کردن ترند میکننو سوپر هیت حساب نکنیم)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83753" target="_blank">📅 02:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83752">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بهداد اقبالی زنتو گاییدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/funhiphop/83752" target="_blank">📅 00:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvX5dz0OuJZj1-DuW-jJtaZnNdxp-GzPijeCouX6idvvkhFQJgeN3FdKDD262m1cjIuKlpq7WF653ghjZOnDlVBfwCx9o-JXmN9v9TjI3UQsJVotnuHrgppA0hAgHbBQ6eX-LSslidi482xJzjQZ2HGcvA0nt4Cp9UHlJzJPFAjKGnmFa02DZh16OmqJTsE5keepGa8FEY_txm-QOVDeuJZUXOf6dE74S2r46o3mAcbkVkyCgFlfvq10IqCZOARs4M6fPOsN5tKzsCukHzWxqE1N8rZizo7G2DEksdrQ3OjoUCbcjIrDVbQhYD_FZsNeHK8TBq2AQC5a5vsDyIcpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/funhiphop/83747" target="_blank">📅 22:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83745">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/83745" target="_blank">📅 22:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83744">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8926315b1c.mp4?token=nlTnEA8mjCBIKJzmOYff3DKA6PDQ3-MC0Z7kAEJM16hfEl2JSa50FVbap4UD4X7NdFAxRmcrFj3bLq7wEIzqBj-n31Nf-tvbPYLf5ENCWB6H0k218VvmMFSXhhbUps8igMoHJBjGqAKidQXX4shjsOjX5-ARKrwOKhdGY6Rsz2lNosCfs-8uv9rYZlAGarv7ENfVCkt7RgLRlq5rSAZPTfJiaH-EUtFglUtgPUMtasuUR4rh4TZvM-jvdxE1XwKqW-KAdkdShYRkjAM0mOu_J-JU2G41xLODfjsbNXBiJyc1oymipbkGwVaX0rnICpzViurTL4SnqtUtkdIUpVU-Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8926315b1c.mp4?token=nlTnEA8mjCBIKJzmOYff3DKA6PDQ3-MC0Z7kAEJM16hfEl2JSa50FVbap4UD4X7NdFAxRmcrFj3bLq7wEIzqBj-n31Nf-tvbPYLf5ENCWB6H0k218VvmMFSXhhbUps8igMoHJBjGqAKidQXX4shjsOjX5-ARKrwOKhdGY6Rsz2lNosCfs-8uv9rYZlAGarv7ENfVCkt7RgLRlq5rSAZPTfJiaH-EUtFglUtgPUMtasuUR4rh4TZvM-jvdxE1XwKqW-KAdkdShYRkjAM0mOu_J-JU2G41xLODfjsbNXBiJyc1oymipbkGwVaX0rnICpzViurTL4SnqtUtkdIUpVU-Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی هوش‌مصنوعی‌ای که آرتا الان و نیم‌ساعت قبل از کنسرتش تو عمان، از هلیا و پوتک تو اکانت اینستاگرامش پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/funhiphop/83744" target="_blank">📅 22:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83743">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0Rg0NfzHnZm08T5u-KNvddtpJiyIOP_eeJ1itH9NwwGXG-XjgfUgGXzQKSxaX5QKN_WAwySnJPHE-1SMZFF0i6PhI0K17KbXn1uLn5sYROeJ_ykyDDD0_I-HIRxOWmWKmfzvETLZ_NTizKoD9an9CcWQuK_3x7T1es7rmW_McIqsaHdrLhXqBWOO39PFyyEuPKCpgEXWwZfNpoZJVGsayAzqK2VEZQab96bDdmbCbBQbnmAx6EGL7OnZxaKV8HHd_Q4s3RIjLwWZyQji_apbgcEmaRenjh06tQY7hGH05_BRfGRb0Olqcr4EdhY5Ha8OW004ohlkdvKIRNbtyC0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب وقتشه که پنتاگونو بمبارون کنید  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83743" target="_blank">📅 22:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83742">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پوتک به ده تا رپر دیس داد دیشب
کی جوابشو داد؟ ایمانمون، تنها کسی که پوتک بهش هیچی نگفته بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83742" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83724">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83724" target="_blank">📅 21:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83723">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4397dc1e0c.mp4?token=SYpBSRqo33XTrQyFwZgbKi4NaUk0K-LfNG_JZStUirJ98El_U-YfLMeDkSy4S4_B2rtwNFM2IyKHvyUTw1-8pWQGAlEirU64soLc2hu9EnP4Ggqcv6Wk4ROJ1_n5M1Vi_0u4ixz2mGfF8mW5wOquUjFKvHMW86ZeHQ0FEdq8untvR1St64OYTAusRdpOIc3CJs0w54fkwOTFNNE56tx1WNVHTuTb1mdM1vR7ZOdOJQidGkPYVz2ierCN8u4LhUFk_0TeU-bRmYBy4LJTPT46zUxderbWQ34BNto5eHap_O36_7nggH7YdmENS3You5hLAH-SQL5U8BDC0GUaoGHUOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4397dc1e0c.mp4?token=SYpBSRqo33XTrQyFwZgbKi4NaUk0K-LfNG_JZStUirJ98El_U-YfLMeDkSy4S4_B2rtwNFM2IyKHvyUTw1-8pWQGAlEirU64soLc2hu9EnP4Ggqcv6Wk4ROJ1_n5M1Vi_0u4ixz2mGfF8mW5wOquUjFKvHMW86ZeHQ0FEdq8untvR1St64OYTAusRdpOIc3CJs0w54fkwOTFNNE56tx1WNVHTuTb1mdM1vR7ZOdOJQidGkPYVz2ierCN8u4LhUFk_0TeU-bRmYBy4LJTPT46zUxderbWQ34BNto5eHap_O36_7nggH7YdmENS3You5hLAH-SQL5U8BDC0GUaoGHUOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/83723" target="_blank">📅 21:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83721">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1443105ba1.mp4?token=qnSx0oqtFqH7Z2ndfJpf1N1Oo3h5mdX0DgvjQvAAHC_giCMNBtkH-sKy9QHzBAKkmBOmpYfPEnpCYxZKryLRhcqD3LNMtrX2Sc4GSGr-sjsQztGXzwIngo7o78vNUEeeARFxJAg8YYFzDZs9Pp9ys9jrj1PZnxvSo4MP_y3et9431B14uWgIRR9Oo5iRqvWMsO0io7qwUgu21PiNNtMM0vX_XyvQBwAs6suBAtmPIpAGxZa4GZj3I5qtK8GDcyglozNGc9ppLQHcmftEXUc4lHqLsAEjy91NkRg_vTKKoddAlKbHahv3F3jvE-G8yJOxsfxRYNFSzpr4u_ms7sHeUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1443105ba1.mp4?token=qnSx0oqtFqH7Z2ndfJpf1N1Oo3h5mdX0DgvjQvAAHC_giCMNBtkH-sKy9QHzBAKkmBOmpYfPEnpCYxZKryLRhcqD3LNMtrX2Sc4GSGr-sjsQztGXzwIngo7o78vNUEeeARFxJAg8YYFzDZs9Pp9ys9jrj1PZnxvSo4MP_y3et9431B14uWgIRR9Oo5iRqvWMsO0io7qwUgu21PiNNtMM0vX_XyvQBwAs6suBAtmPIpAGxZa4GZj3I5qtK8GDcyglozNGc9ppLQHcmftEXUc4lHqLsAEjy91NkRg_vTKKoddAlKbHahv3F3jvE-G8yJOxsfxRYNFSzpr4u_ms7sHeUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ایرانی که کون میداد فیلمشو میگرفت توبه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/83721" target="_blank">📅 21:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83720">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f7a3000ee.mp4?token=M8tqFxLqIy7tPEX3zu2EPmqApWn-GatjGgA6XfVzfuq09wlZWnKLwb3dV9dnRk_3e2ARLdI_t7sI4bQAwTBhawXYWSWMpnhnGU8oSqa2_bL4xcvMgXaab6JM1uVXEHHInfm9rCUfcQD7YQJcKuX3exBR_2dND1E5LrDqJWe8UoGwUPejHHEt6aJvg-JBwz_PvWtutUnhg7pdVR1qPpwUxL-J8f704wG6iTWDrv7wt-BTZwJnhKfSWuPqhfp9WSNDhe3frwbhlby6-QkEib9fMsfcEg2MDSYqI-koRNGjjQmKZYD_laBQ_b4TZRNR6--dvhiEFuJjKuCom7LtKUDHZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f7a3000ee.mp4?token=M8tqFxLqIy7tPEX3zu2EPmqApWn-GatjGgA6XfVzfuq09wlZWnKLwb3dV9dnRk_3e2ARLdI_t7sI4bQAwTBhawXYWSWMpnhnGU8oSqa2_bL4xcvMgXaab6JM1uVXEHHInfm9rCUfcQD7YQJcKuX3exBR_2dND1E5LrDqJWe8UoGwUPejHHEt6aJvg-JBwz_PvWtutUnhg7pdVR1qPpwUxL-J8f704wG6iTWDrv7wt-BTZwJnhKfSWuPqhfp9WSNDhe3frwbhlby6-QkEib9fMsfcEg2MDSYqI-koRNGjjQmKZYD_laBQ_b4TZRNR6--dvhiEFuJjKuCom7LtKUDHZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوروش هم فهمید که تولد ریری از همه‌ی این بچه بازیا مهم تره و همه‌چیز رو ول کرد تا بره تو اون یکی چنلش به ریری تبریک تولد بگه. تیم رسانه بین‌المللی و مردمی فان‌هیپ‌هاپ هم به نوبه و وسع خود، این رویداد استثنایی و تولد ریری را به خودش، فن‌هایش و تمام مردم جهان…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83720" target="_blank">📅 21:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83719">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b843e8143c.mp4?token=NPI_otD2pTlko2vFkMdLEkGrUzrpT2d7h4edNCqhiXuFbeVUQ5OaBv0MKyUdnShwEuV1pw5L-J4wjwY182xDSIdj6FmpqT3nDxjl0PrKo4M5gb5MY8EhmiyePIuiXmOte1NFtydXlkd4qOaorLZOJYsqUve1i92O_NfV5MURHSF7bWNDzmHpl5R_rRtTQM49C3iYTo7CX0eaw3_kedTw96znEPh2yUNFd45sy_sEboesVk62PRx3wDR5D8xYFRm6A-fneiCdhsjKfZes_TEGg9A1epVdo2oqrf9PxvGxmOjxl65McZZbkXqGByJmEBtDXHDLiYma2CWk-pmaKm1hxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b843e8143c.mp4?token=NPI_otD2pTlko2vFkMdLEkGrUzrpT2d7h4edNCqhiXuFbeVUQ5OaBv0MKyUdnShwEuV1pw5L-J4wjwY182xDSIdj6FmpqT3nDxjl0PrKo4M5gb5MY8EhmiyePIuiXmOte1NFtydXlkd4qOaorLZOJYsqUve1i92O_NfV5MURHSF7bWNDzmHpl5R_rRtTQM49C3iYTo7CX0eaw3_kedTw96znEPh2yUNFd45sy_sEboesVk62PRx3wDR5D8xYFRm6A-fneiCdhsjKfZes_TEGg9A1epVdo2oqrf9PxvGxmOjxl65McZZbkXqGByJmEBtDXHDLiYma2CWk-pmaKm1hxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوریا علاقه‌ی شدیدی به ایفای نقش باتم در رابطه جنسی BDSM با هرزگان دارد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83719" target="_blank">📅 20:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83718">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">آرتا داداش ۲۳ سانت دیگه دودول نیست دسته بیله، دودول برا همون ۳ سانته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83718" target="_blank">📅 20:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83717">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83717" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83716">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83716" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMKuceiQgUAnEBZ2tUdFzSznxOmumZRwYAb6NAaO9kaybMhq6efdjBJJHjVy6f3f8eU9kA8NHMIsrBHULmX8UcklyqT_Pk1okpXRBPcTiyHPIOW5rIEcaGHp_3X0ela8lFWV0a6Q0nuhN_QQa27jU1n4M1ZYrUwwBRs7CaGfIrkn_-QT2-gq89OQLxfh8f-S4IA0MRl5_hieHO7HjyWFxuuKs_tVcBnHLcCnVyYA3oR0TlIe_ZhuhOo2np759XtG0I1KdXVSNIzTRvwrI-9pvBcC_mnnZVHBWWGowYb1AbV5lC6sjAGHeibrMGTzy44hvps-CvBNvMTOmDvXhjyhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام "بدفاز" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83715" target="_blank">📅 19:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سال ۹۰ یه آلبوم سولو داد واقعا خفن بود</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83714" target="_blank">📅 19:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83713" target="_blank">📅 19:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld1qUiZeXSO23hqgXiMDXZ3U0LshkyQQcrNE-QohtfjvPA1VuBkvZ087XDVDCfVW2WLBmN8t2lgGgMotsldlRyop-k6C6kC8ovnKLktZNdun1ub4-GyWAszhzkHZPGM-CapwL5UoWPOx5Eqz-vmWa8iZ-Zi99EKsdrDpAHGpfaRtcUqCdL0gzkzldblIpXeOMC5UxhIVrNsK_UnuF8KxAU0oPUZMoZnIXITLjBZ2lBA0Iie8j89tVEfkCC8Zl2QDWOXOUqV3rKeqRVjUxEjyvPi4Ml5Ij25l7jX9PS-K8cpNSR0Vo3ndginox5Vnjc4cCO-LdEdjSp75lGea-B1ZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیکه‌ی سنگین علیرضا جی‌جی به محمود ویناک
😐
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83712" target="_blank">📅 19:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83711">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3xrPdJfqov9nj5l7Cj5zls7nk8WGI5q_p8bK4HU1YbRSL8F1CuCNgkJubLwoZZTO-uAiXyCtdyC5M9Q9w3PNaWcraCIU21IdkbnRTNgibrkvcMFd1irZXzDASEF_B1d-aD40tb9XXT9vxC9dp4paV0SxapU_KKvzwK3p3vNpCfeLbhmkxrLYNrF6-lnmvbd_Pmkvu7jIi8u789PqpDxGWc7Vp6pdw5o_kJdHF6NlLKFOpYzd_kXbuq5vdi9jEgvNsBes7V617lNTK5Y2j4ZNoj6Nl4-AMc4q267lNxpIZWmtw9gbobkkwb3rfhG7gaZr2f5oHMS7E0G4w-CkcG1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست جمعی روانی شدید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83711" target="_blank">📅 19:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83710">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مصاحبه ها یامال یجوریه که بیشتر از خودش برا امباپه میماله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83710" target="_blank">📅 19:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBQjUVc_IpTNg7T7ihogbBTEFv6W1GYYqFbGlFlDmoAICR_XtzZwSidmt1sivAENhjXq6xSzLlbb_Q2du9OS9sQI98kKTGlkoTrv0F7cX-W749oflSCLgelqXbeOep-MvAcfN0n-ziW_9zeQTeWE31up6eKBA8Fn8POAylqqFuIXW-tG03V-6PnVhVpKB4M_e14RFQwKVE1A4Wzuc58-vIIt3vdehCeLKY_ZEhcwA_6nPpq1weFJKjTXbfrKGD8NobIAVl195gFaLDQgQ4eNAWEp6JTsa1oCfUU2UJPygjh_p4rRtgFD60R4_I_JvwBkvR5JvlqdRRzCsz5Td-hTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااین اوبنه ای رفته تو رابطه؟</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83708" target="_blank">📅 18:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN3-Hxj3rJZVNCq2-YzOmVSIujvUQwfw3ScaXEB6fLj7oOpjVPiB78ej_Pf5blFaomZBbECUQqNDM9dRE0BS6RfBeKTACaxVe6-sJEEphxcWhU6oXGuy9xDw6YOmNBhoZpHET4Zl_WER9uHBCYcgkW-WdG0i_WvJ-GzBrUZd1VvOEToOhCbGP2ihAauC2WixDZRQFTMKWg31W2AB3m4VBxoFITkhJnY3Pv_uKUioHe4VDyMQUSGSxWnIkzLe00h8dWtUPL3LgmFJ6e3ENb3ObHR66SkKQ5ivq6UY_LsekfJb_EjGwiKTYaJBJpJNDXWi8HQTIIRDFIIaQ8kWc6nN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر پوتک همین دیروز با اسباب بازیاش بازی میکرد پوتک ویدیو میذاشت ازش، کی انقد بزرگ شد که بره تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83707" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83705">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دلو به منم پول بده تعریف کنم از ترکت</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83705" target="_blank">📅 18:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83704">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_a45z-rjJLdLaqv_qCAovzml_WyvjOqLZ0N6X940sm5AHCIWO2EiBu-CSkbuoLjVYa0Y1-aSC3AhVsQ4cwx1VL6P6ejfKFrdoJ7ygzh_nx4hOcbiTeY25WpNULM8-qm1DxxJ_rj-_XB7kGZwUhfRxzebP5pRBBncFbBf-BmburYqUK21HP0Hq-hevzoUttxbbaPsSlU_V9j4vrs9SJlnVtx3YeZbA2h3ZlUwe-_1GPhCIy369UEPr8-J0Z2d26xIgSGa9wWu3CWHvLHY9mMobHG2CGB6doEMOqLU0dARNuQL6IZttIVjHl7ISSFytNZBPs2XHqmY02Sn4lYtLKUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام DUH! ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83704" target="_blank">📅 18:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83701">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKF5GVIW2_ngTAnukL7PLGJGQjuMg6YH-a0fyoILBSp9VGRN7sh4a6-rlVWW-23H6gJYfmkuFf4Gxlk_J2dNy0eznAS3-HIff07jAw5CN2XloLBbeycF4QqQsFA-ePRLvvPTez0gPNVpzBg05lldSP2sw9NRuL1IdXSe5Q40mC-tV7zmDi5Do5INfPBu3rHE_RDtIqIx2TGA86Wtw_V25WMBzlbMGPX6tSd4d0uKCxeJB4yoixqWACJExaafGDE6RDNXBIbFXVdaqm9QJ8njZRFqWUxPYBFCuatVsD3QDOgVqwPiRoxewn9mToBJPlQ_iQjaCSKfghHLZFJpI_CE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا انگار داره آینده ای که نیمار پسش زد رو زندگی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83701" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
