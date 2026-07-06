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
<img src="https://cdn4.telesco.pe/file/hFKH2Nz-yflLidgTchok_cRdkvEConDCDdA348uGclv2P_bDvnS8eFCYGuTsSk2_IstKp3pUbmROw0I2-pBMCc0Rn3bca8zZvorWuBJdoSfKhDlswVy-RHEUiBfMAGPaZqjieuo_AjvEM9leLphhZQTkcwtvsaxF_Q1qlQECoakTm2je77zzhG4eukLFIsA9xMnfBMZ9lirbbzYgdBRVnL2Mt73AzR-gL5ox_JcjD6I5y13h0xL-uvysOWaK2t4PqrQu-YUYN-OOhlRcJq2MEVq3kRzf4Op-Gx_eElwTkmQscNkHVh8qNPfOsFVBxwl75z-SBqfdJpp0WgtvMKFSjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 407K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
<hr>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blxsZRunyg-iJoRwNfltssY7jldyzl3AkIDtl6gfXchS_K7d-9Z9yVN5fjNOlxoBDXV32CS1jltt84-MfrqZMwk1dTzqOHT_wovyzMwgDZXKOKLrPyMPxegNPtGyruB7gPORYzrwsP5yRZOOGG_LoO-SGvBfZuQXmRUfZkDItet_7lH4Skb17aDr1vwKx3Bc7JOaM_Bnfh0pvlxCA3F9TbBEF7EpnFqR9k4ZY9LbsbRBnsP6hGGG9-SZGAOdVGXBB8K8RzRoCZlcPkO2UPD8r0AHmDENaUH-dULJg2VTDcXWIfR2MRUrWPIoDylovKJ_Nu6fLrD-LlFJoq6kXc5dSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkNz-7wJA4tpdsciNasX9K88NEFiiUItO0PFAJzshY34nB4pZ8RrhvnJsgc1Z_7iXsSR4TGg-_zgKM2GY487fXJ0GEqXwHP69lVfLc9Hnn0acbd75ZhmtqXVPXU6iC138DFnPlirJWMuMZWcW_iBESZgtI8HQIJIU3YHrOHc-mPMGhLV-sfdCn-XBeS-VMWM7B4E9qcczzuuqjvK1sSWMLPOxzBlImFEVK9ccRgND1Vp-d4YlsfF6Q8MFJOZ2Ybs7etmJxWsu_iPu29J6znZ8z3AmW8RM51FhOPrjEHgg9Jzn6Jx49QIvE6O5zaAziO3MX8Gt61X53r-_zK2u-vlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l27Zv0blkLa6Sq-hr85jRJ50D9IxXR5qiHIG8FdgQLIMhbCgYxQ3SXDPPmNsVFfpXLtesx7cPN2n3pbe3ilA0TXofZI1vXdSsNLIXLjy32IS9sFJqj-7vn6hhPi5mpCekMZ-JHHZbf1A-px0DFohfmLm-h77xMkq6zmpSmAXa3D91iRIt-bsS0IPln1NlC4zsYt6QqvRLRBqiOc_bOPG4YxnzUcmWVWNFAXKT6sZfmlaPhse6-MLgjlOVnws0dfVXIeYCYtbv7AKZxB1kkfWKBY6B7lfiKU-cv4phyAQbKk1pEHZ9lRVfdTzg_Ey_-IcDDTGDHSEfqPy2nP2rD30Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHFNnEPe_8BdpyrPRZlgUCw6AYtAJMZCMIzmJIYdRgYJjOB6rHPJnGRWgohX0VJjU_Jg0vz5ClHcm5FX-nsbOfmbKSh5u-3oyo9XqreqdLqVK1L6aaVQm4qqcxmgYu4iFflIm92BBCxYNvmHSifyyrtFzqhDgIySS1pYTvhh2--8hHYeSM519PeWOisdDi0lUvNMOYl_DDx3i5_MXRHAxCLHZlZ9y035q1sV-pCl3APBmdDORBmUIbq91NBA18VHqHUXYKmfra8ZKL5EBDv6-jUgagLWXL_yql2xITp--9XLxtW6N35-9gXwmY_fI0RWqV0SBzwON_efK0fQ_VM2Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgv29uWkuaByt302QSMmkjqWq4YDCNmYoPLU8z94N1SHw6TCZvrt99lhGyYcN43VrJrzKmHtZfjj2RG6wpT2rkfwGQ5Oa2GrxoldfXsDxrZoxWhyxVvw2MrGaJhAKitPc3cUwbsm2l_Z--XDo-OqjRcUra4Ajz0Zw_1ucocMknoiHKUfxBhETpqcG5n6xQeo4YUpB8rECv4K52XFkvRmettfZ71Z0ZAitGPiwuO9WT81VItmQMLJ1L2lAdl6VchxbEWP0BVCQf7ChRGubA-_-SFVBxTBERg6WC1YyR4C6tkOZeUiOzmFAjBexSQZ1QFNDxPzBe7Hr3ZcX70DejEggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8N7CkeRJbrGnQuWIJXDEFX00cqI4HE9Ds97lVAatYClPt-r3jTZMtAYzrGNdODughGhTUcrnfeYRWruWyqOKZMaxFjxGSPnUTpsoxI2tVKu7p9qiKutmWW8aoK72Cl6XuJimLFkYNDY-s3ohtDYHNMVfGz8mggsfXYSthT6_1zVl630Txn9FqnUPAhtPVoeO-iKSM6jLxubxeGtUuSnliYo7Y2fHTxMWUd93GPCBDjzi4OUPnhJjbHGa-dRhgSdzy3ly3oddWonUenO45zmGefKi5muw1_2AuWDt-kGRfGvLmOfONkAPU8rU7BpTJ2fALNjMu37mCY2N3E8DcPEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GoY4PnnZkcZ-GZVKJWVZED2r1Jx9ITdX4-t6Zhwmq_v4jPNP6m1ROKvfeQ90uaetJAyzNFkw2cvoibcxjUjqDEPZThr1CocmZwNOZoaP0ulU3JKpKXH-OsbFR6VurLcqP1NtKjo1NGbVGSj6du73GwSux9eVhSobkbbzcl895oROUBFMzd3_3boPVBNV69oflpzM7IViZ6kA0_5MKUQRd-Isy1uFolVwrq78ElAnNwKGWhMbNZ2fYMrHrKq3IgQqjL9AdxVF2sbuDJgmD1wGyF6ljWDXS7vygT1me3rYmfNG-K-SmoEZ0IJ2lvJ9SulXgPPxZ-66nTs9XFehgxBUGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GoY4PnnZkcZ-GZVKJWVZED2r1Jx9ITdX4-t6Zhwmq_v4jPNP6m1ROKvfeQ90uaetJAyzNFkw2cvoibcxjUjqDEPZThr1CocmZwNOZoaP0ulU3JKpKXH-OsbFR6VurLcqP1NtKjo1NGbVGSj6du73GwSux9eVhSobkbbzcl895oROUBFMzd3_3boPVBNV69oflpzM7IViZ6kA0_5MKUQRd-Isy1uFolVwrq78ElAnNwKGWhMbNZ2fYMrHrKq3IgQqjL9AdxVF2sbuDJgmD1wGyF6ljWDXS7vygT1me3rYmfNG-K-SmoEZ0IJ2lvJ9SulXgPPxZ-66nTs9XFehgxBUGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB1x6NC-iiRiczoWmmGgxLns5JJLd3cWL4b30emzT1TruAatRTMh6RFcxTd9PlTGObAdI8xXMz1iT357DV_aUi4V3sNVi6I0t7VYwh5kkrNkp1ZJGAvsyk4r7uOFxw7l-M53zIp0mJvuIXNiumJvu_mA0nH93Jl1V4NFXowQwhmAlonFpHzuA6GZznVuBjZ2Diyi6Ueok5hNC3NCHPNmXPxjioUofvPPFK9xwdB8i1TVErAeb22G3ra0FjKEd1-lvSfVMFmbY6Mgwa3yllm5oXVwCzl7cMUaFAepi0OaiA_as_oO614pOQmEGwLqBDkvM40rHr2KVJvLp0wJqUnkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhMIaw21gr57EMmvOSpQ9y_yPDVJY_ROmR4_wR_oEqoYM88zhBaSSD0hDNb_rnzbxzii_ZSW9lRSQ4DDQJ8LsMHUWH1R2Nrz2k6OaMxvEymIvZ4H_fpEmZcEGdqch4eiFFEArT-IeS-cFv1bmAIb_LtpnX_umiiksA0EAP40vclptE_k1pPYNw43tr7LfKAbzCo-aDs_NXBUNLbJqBB1Sg0xnitHryFCc76SHc7vVM60QhfVV0EwTwSvtnfa3TSY34QSjeR6uZzlvt2pHSAXNRtf4UulEgdQ_Gabvs2PJjB_ZwM7EEVH8WiKCygCuzOLP1557cJNFe-4SvHqxoqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXEYrNfFR0ui5w61Wkb88stMMMMv1oohBDR5bC6iLNGEhkx8zgzVW-Rzp6Q22H9rGuH2ygxD4GMnbhqzB8vxdhoKgEuVnoOMTAiY9M3qZipbQjabCa9QXYN6rsCggPjyAEbYYcYqISB1EztG4kd9whcWpNDfgGXArKhTT_w0f1sdUA-atAwIoELGPHeKMjtgaE29UUPcoeeSbMyaeqk9gt1EANLb5YlcMXD7471wjGANvt9PJgLGC_BxpRNTV7AtuX1SLGFOb6qB4vD5_biumWA3yUdXeXIX5pMdnIVH4y_4mGjp4ofvEsjC0ga60RjrqjhiBlGEF-RaKUE6-i2YWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKzrWkHRvLs-uOQjwmpZnWZVq8TqwFJCkYvAj0qLnAXHychwHvYC3CNgPN09WKmS1E-X0CSEg2zyKR__WejJpBSSEuQbubG73vcHzJ5wS3PKegjY_muV8tzDq2oMhsU-1vHMX1loacscxl8IJl-zi-APp0fIaMzkKRuL2swLq0NoeQczM3nvzVNOMfFVlJ5NJf_CsLhdkTU7zewyN7064k6-fzTSeyNMoQmkTQELQzKgeClXj379aelD8F1pfpYSIHWcvaHV0_NhNj2yyoAEXtQo01zv5vTNMLtkNDcZlL533-8IX1G12RVWhiWpT7fcGHJGUJ9AEbisoTZYDOKh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmKcfckfUyMbgxUlIKcJczzzgxk-6mlgT27Z7RvSdJgwySqTgrTGuam9Rn_wZPnjngFGQfdTm-ymfbUujE0M7K9QEWBbKf8lbv6IL0BNfwhFedgVwfI9s1R75zp7njbESWJJcvGsFJkqlZU_Jrh8XlOlKRL4SDnG1_9WtX8reinsWx3Ji6AOrI_XrGsADCwmQMcxn2uRcYRr4VLkHco5eUwgRTFCs0hFaGFzNtIvrsCHBsWQ3h44d6uhpq47oNEcGzkxxgZCjscBXnHoUXusPwS8MQ7mzVR-JXPoyRHhOfc-olBsUCuPKbOjonwzjDx-lZ1zgpRIivE7ok_h0EckAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcNePoO5K3P52q1k5SEjSfLThauOiRb9-SQYl79kQMs2eo7cd3U-V9g0obA5z1KwV5YnIO--pEoUTfiBSTzdDSP_PO5N05UfBD_WhJlwciN7VfY3yW4lJoDcvrMWlPghBDvDxggnfRC-TMxEJXhgLxUK-SnOyJiAzQFtCWt1qdwtBEuQUKfuH5KBT8W1BeEiwZp7fqShVZM5OuOPza-1Fg_ECHOJaUImU_app4d8tnIa9JsD_V3ohU6KrU1XjJvsxXg3PMH02x7wKOGwMQLI4iyEoFsUhvinlBuEZMwUf_HPZd8sa_ILYgJgb8ZYaFkY7klGhwYbzYtvzDZTMAbQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv33PDrxW0R47Y8Z8qPrkS_vB6FSbZvLWiFeTCH372PMYKhttmjPtr2-HdMZTvJcO2MZ1kBpAmT7q6CtuAfSA2MRHx4X9L6aE8E2R-46ViGpMrzHiL_ghoTbxgqN0s5j_rMr3eQhJFpe1ThHO9WylAjYabuK2syuTY3a9KY3cqDxJ35H5gbbWSYdWEIgVi73Dtt_JtrohIC57kjmqp0QCO8riXvHk5DzwgLY1b2HWKCRYezAa9uSAtlYh9DzYSsdcB1Nh7mbowWbli1BGw8lQLjwnYql2hNg4zsNVAg9uEiCEcJbL-a07uab4NoQS39hre2Y17Up5N9M-EZjqD2Uww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwjBJI36Bc_iEi2nKhajL7HokReJFnECTG2IHyfVHqjWbMQyQRf9DPIRHSfIcdEGacpe-fJ7MOTWRf-hhybq7fEpxvRJMeOz7h5z7LAcnZzEoiPuLvjbjYfgqChFFAEHVtpkkiXi2W22U4rbTXTfg_Yic9zNs618p7G5AfZPE6f3wrSgXuvxw_fZ8iSKU5Yi5Yn9-RiQdlHYYaPjJ57kMm_fbDNzQxncWkhxG250qAF3_rrnK4gCcLalgya9ZkkymSKyMSw_RGKm51wfw5usPhlkaxobgoPqw4eQR-jkfF8VgABUPqkYFhdo_VWTCsNaKSk-ZTrhzxs6g51IVbABTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es-YXevwXZ9d17ACmRPENexkVB_VCoqxcsNnVVaJ1ybpWxll2U3e6S0BCe33sMouBx_Sgo5usmK71e11Rh4UCD2j8O67LFp0B-iN-JY-xNk9v-YFL8JaT34m-JzbJ2ALJmkerzsk3Isv66PXM-K6rS7vA0vwRVx-Vmaln1UMjqv5tLR79N7h2ULsegOkPU824rxxeAsRXaz5t4kTbWuKRpiEMvzyWJcfRmEXlpl-umrLs6BZmY7eewuuyum5Mux2xbZoZu7MeiLsZ22YbsGFir774kM1gSDvu-5B5dKmFKtrIRbGTXS1YIIBI3BHeU_r0SNnGwixh2UkG6eiHJtuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGCRnOWdc86_ulxOrzs3flT2ObGGXaKa10lix4bN_zGXPiqjkLsl6H6fvCH5H2zUKfMTODjhbB-AU-VhRtwdeE0TU-wbXSa5M6C36FWOEt4H2kIrKKfcKXyON_lSYyNn7rsySDJ8CWw-EQfSBzwPJITEgLTC6Nur6oGoQi9eBPKbE05puK5-5ccPQF5w4kKUeFg7Ml9hdS7r8kjT7kvo5ZKsaGx5a0Sw2dlw5CwSxDucyp0QyKQ5-5Ev3XzgfJccjALZbE6PGomaNoNWEQWiHFfLC43F-kMqQ2x53Z4RVm7QR11lficx9kW48p0XsZm2W2CF2BWaY9LKHaobCmvStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4KVl68s9lyOpyciNuL8ExBJgyk96gAi2rT2C11T1Mi8aWezXHFDK-sp3Krc0GsBLSbmcTB_TmuUdWxrBRqSTCdl7C5wP2GeseANOO4V5MKcSj_SyaOYGQ6ZLHIcleMykG6LJ879LUQ1A8BuznKdAYoFDTQFERb8fPd5BJude81wrouyZLD0O_E8UDuVRPZWNvmsRbrPaa5Qrif9EOxhC-nwhk9abySdOYMcZv0JidSrUpquQFSqzwzyx6Yn8wr2Ww26bxoRMhnOAsbl3RGgsdqtYDzOWA9iOZjcSHMivc6mA2jdWxk-fLABArT7VRAc02h5SwfmIKguVCplho9JDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAX__n-x_eKeIQpAqRsNKKOck5I1tfv_ZPv7hWSKlp-phxvMWinfnOg6d6Yc1zVvHthMY50IKqaQnT0Mcajen7JUhItNBO8Aqrs-iZ7jwPbQI3XXP6CKjhha1uQiiwrm-LihKJHWRRU_yg8PJUzGcsdtWqYKjZEv-PbCwyzVraQKKyshIVT-5L-AJbFV1ohMPjUNcejfnXOw1I54tZ0IQCpONMDd5dC0SmCw45WkEwUsTT_i8iIJwLbhE-y0vJdw410WS0nHdYa20UzZ153pSq49_Dt7X0ZE7Gb470oE8ZqSn4CiVCT4Opg27wEJl889JauXPdjeeA8VIs2bqECfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A62YeORBEqOd7lDyi3pTKs8q7wpggFWY0i22_qRN8xeEOmcZJdAyUPwsTdsIo16oZtk6gxLJ0MclufRyRbR-z-TnRh2fvb9PZPEXcl9AgtovuYSVRLXmjTeFLcReqFtgYFnMsIV8Sevf2nl0_pXS2lgZJXDzih-5xxuAiQT6KrBCGdQAb2nyTq_-_bWvZRtq9zdWymXoA61mmiLBZHNpnq4hQrhffDtv-hJJbN7ejN1BpW8prCCX6wAhHASUI0BYrmMQ1gJT90CARk-nxjL_bjGqTNA9g3GwpMMo5yzZ1Ye7Z5nymikCNClci4B_Y6_GgMILNzZ9Yc_BIlENFuEQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=npCBaLvNhxWkgtq_2P-qY7cOGmgqRkJpG1JRs_S6jHJnwTzoquWfbTK4pmnBFZ8LvScfwDQ9_cwPhrg9huDTxXHt7IG8FWjs-smke7g1IA45L0SwV7ggYSjzYJF1XV7DHanUZShTl8nshIkXfScJCA6442BfwNxKH-TR2GfiZxz6w5NZxDMEOiCgGoonQ6WqHaYz0OZfSMM0xVJnEHp07hI13S-xX3EpMxhSsu49LhhBn2oJY957ulkyDarOVqIUkPtAkqBqcdBBsgPkQj5MG6Ee2aQczH_5wo5ohUu1LIC7kSiaggtel2A9LsW5_VPtG3c9m3HLBmkOrcQbPYQ5pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=npCBaLvNhxWkgtq_2P-qY7cOGmgqRkJpG1JRs_S6jHJnwTzoquWfbTK4pmnBFZ8LvScfwDQ9_cwPhrg9huDTxXHt7IG8FWjs-smke7g1IA45L0SwV7ggYSjzYJF1XV7DHanUZShTl8nshIkXfScJCA6442BfwNxKH-TR2GfiZxz6w5NZxDMEOiCgGoonQ6WqHaYz0OZfSMM0xVJnEHp07hI13S-xX3EpMxhSsu49LhhBn2oJY957ulkyDarOVqIUkPtAkqBqcdBBsgPkQj5MG6Ee2aQczH_5wo5ohUu1LIC7kSiaggtel2A9LsW5_VPtG3c9m3HLBmkOrcQbPYQ5pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSH8-X5E43xJYN5kzNZJIkof-nwHRadEfjIQIQy-OfGkL49m77uMLLh5YLer-QKDNQ1dKEwnmNaAQgPIfTZ-Va4d4LAHsdDXZFqaCW4ULO-nz-XG6OUeadXUQkn0LRoAh6HZ9tWhiNyotCRpihxZxNVw17W5VEUfndVrAHuDVdJqQzBe5YAZdFmNW3ma-5IC4-VWMYiIckXPEMTUZC0qNZ4zqi1rIwwqlzdMQKb_Ki9Qyd7Jkmc3Dkwzq9nnnb1x71B8uAE2C0BzJ7zhaN9u6eq8EGEQn4iz6Jozjh31NapdtB1O0YPobNKz5aoNz1Z0MnezTZh5_LkMLi5rtfk2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYpsuU0F7Db91lkw2stWe9Oi1uGV_k6s9laUJ9OmmMlqhsJjzfja4NlIatEIXuWH2TifamnKoOlOl3urojmvAtyumxGA02lh-esG5_MCOPDlPbExi_jwJTZJuVoTy0NqGhA_0i0ENbNBqcXgEwlXUTTB9ZaxO8gjqOfiUfPV-2XdICrbwDhE6HiKY5rGmTCdKav7rYAC_t0Ef8BdBIwf23vJr63Y_UiI2bnGWCoPdYP1ORxjFPd53_P-JfQOtVUDXzzM7QzaQMK4Oc1iN3K87HBFqrhwoJcDFyhJqPoiuC14U2wLAskpyd6SnFj2H0Lv5mYSSYdPgH1gnbUO0gnx9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRx6DIH98SCfcWdFxzyry_R0-UX5v4MM7is0wCZX8dV6sgR3JOxYeSZEvWS5CfqutlL4GqMcNoO9xbUxc3M5SFOhjtWO-YPKym5yzpSn6uQrSc4u4IvYlUzzgWOIm3UMBaepTz1k1-Xo6AYI_NCtsCvI84r8wQ2-TybsXGga8kGO9qEBbAr1BkVbdhwTqN5tN7Qfq0D_4Hh_V21OoIVD2qmp4PSyH15UY9-pk4_PYss-NjykoSQ6nh2-xmbOOuu9yGGr9LAW6iw_058mGaMkhpyvTsryUsF5DW5Urg9dYN3O9c5ESctEnSdSgTDjJdS47nENH8zoMn5TwEMbcdHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myzUStoTmA4XWTeQacdYUUh3MvLqOAfLx1BMDF4vwOZNzQU9UrB89mieu2EdnWvACxFVAP3n25Ifa-3f4tScqpnH5HIFzGnGcKG5wsMP3C7UEQ_ElfzJFdanQYJXFgPay6UNDPvOB4oPOoV9QKrOaxozRVGy7UKj5zijU2-FgE-Cv5huK8jODWMQcD_PQszwIcchyis5wDUa89sskdjEd-x4yhEDShQcHS-Gv_nS_DrLMpSIhUntxB1KAont1Iz0c6qbncz80XtqEgZU9x9uTI2wbrj9MBPLkzs7uc9055r2mpvpBHCyh4mDmx594MOHAWbmGvQm_Xn8567j4V9w-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHRyiiMLQRUORNRe7mra8mPHrVFeYYs_HSvY7G9YluaNG394MzKMkHkXB0vY8xg23uWnR0NBGU4RzagmIkxJPxb5fshXUwTL2R0otSl2coC6UycVBSMDb8e40-AYNq6Lf4kbOk0J-nnJQRROWrecTMuDaojPEZNLc_BtR2_skdYYAH9eiY52M5mg6mjVW9lFRBhn_UmTqHAJYz89_EBROm6VNmvl_06OwCzwHvJ8_qmZPNlxS8lD-pZsNl9NeyzXTWDJkxKsBJ8ttfQTRYxZJZf1amuNJZenMM5aMBTpipH2099s_WAk1t5CEb1Y2OfSuRrhD-TnhtwN4FFjhBvDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3u1zFo5vR-nu97moXX_W_T-pUOU4Jr8mIUttzAbUXzBymIDkJRLpaihGSoZa7yA1v6_R4x3AaU-tf94EOgINiwdXu-ZfegvAtIBXacSylFKb-RXCNwfAe8jRB5x5WoHj7vbGotktPeCyx5GuvggOZ9dl15W4k35WOP5lycaOknpIhJdkIaXlWOTr3FgKjso1HKm2o0FF-zE7bGRjqb7_u1tYmgELHMvwqEVqRdBkPb2eAMiTeoLf03p807lIJcKPOK1Jn3ZRwLYtud1Nw7MxDNhNQBbRQ9RjE8MFGjd_h3NFtpNHU5OakMHKd6Ov5s6NdbaYPUCZLl_V9zZg7JsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiPb9kIFHklPnDpua3cKfFhW78ORdpLrsCwEHO7ZF0w1asb_ssuWKxic5m8PEVrIHNuILJQxU9uhsQHA-XyNaD_o434ygWR4afbrF9qWw1N-QfXmLdu-BK5nL0KDYfJA-x4xCVfbC8dP-zu396X2ebg2jy17KMjTPDQIlBPxtRyClOB-jyLJnMwnh6WHs_XwB3LCPaGsxrAo2VCZTppvwJnZCXm-fF8kd8luKrCE-YvG1v80DkyvgL9-QrjYXTpta0SUidadEGL2g_8QruwT7OuLvCEEiPzHx1kUpSUiBQdaN7SsErv5ZXAPmjQyUWLxAE-nOlDLvcJi7jSeXTR8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=ErOPdljHi4Saemq5HPyau_BwiRj7iPAdUUYgVvU9Centa554aGELj7DPyDe40vjYg8z8iv-tW7Q7-fVOZIMMA2xtmT91WEVkb69XtMWlBgykVDtLJwJ7QBfpwvFY-gHYuQk1PolH2ZV6-MS8NX1gTS-BlflL1xPD78jHdSkd-M1o2qiHNCD-0Iy-HGi2oZHl-mabCKAXJWhl_iGKG4-jykmILNXmo0weiicpw_rqFi-cI5usImUyE4_oPQp_pk8EMVBBcdnrfiBqctbFgwNRxNZx333LDh0ZxTIQK6vqXL89dmyv2DXP_9nnUe3BZrF1gneak_Hz9AxvFLqe7ZtaAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=ErOPdljHi4Saemq5HPyau_BwiRj7iPAdUUYgVvU9Centa554aGELj7DPyDe40vjYg8z8iv-tW7Q7-fVOZIMMA2xtmT91WEVkb69XtMWlBgykVDtLJwJ7QBfpwvFY-gHYuQk1PolH2ZV6-MS8NX1gTS-BlflL1xPD78jHdSkd-M1o2qiHNCD-0Iy-HGi2oZHl-mabCKAXJWhl_iGKG4-jykmILNXmo0weiicpw_rqFi-cI5usImUyE4_oPQp_pk8EMVBBcdnrfiBqctbFgwNRxNZx333LDh0ZxTIQK6vqXL89dmyv2DXP_9nnUe3BZrF1gneak_Hz9AxvFLqe7ZtaAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l34sqmnj4lLtuR8QxwBLf-2iAuYImVazTuK4-ARF-Fi7Q84vUnWnDLPY5KtADv8sX5DXH4BXqzMuMXHahtI0mGliGNCn3Sx5QByxjm8v6xbXhqGV4ynl0GmN_3LozdJaRlE7vVaLXo5yjZrQeRao6wvCy8rGToSCHCrdYGsO68UenDeTU0ga7uxAUsNen2vhevvOIKxOAfuBOSY4ahcEmEXKKcNfGItYlEhbZ0bYRghbvzSJJMQtNKteFtvHxpLXckw96AcKRjN33MbaLXeSHS8GP9nt0Hv-hv9U4sY9O4v-S4xzjhOX3ZQs6Xfz6j4fB-llrq_YY-kbl6V25h4EwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXCUMI0gdZCOKHLZNQxAmgCN-ONmmPapZjpN7WYA9BcjZ5_CIQs9VbUEUoQaNho0rNdOiap_akCZDSw4Hd6Swpcz0LQA3gnSseLNA0NzvHqIrOS9QWmLdYZImjDHqS33gsLAaJjNXV7gjCgi76OFkKWwiKdkQ5sTTyLRfZmaYidPaRW3480PFkiNoX2XAVWm5E8d-BZoQV3pxmaiUd37e3SapRv-iOanyzaZt0-I-x87xjg071puhJz5lwTmUo5nW6yP3GaETg_otMaFsfok60im8Q6sPmF1MGIwouuIyWvCaUDvUcT1Eipvunutcb1kqDP1kj3G2NnTcRWU905tOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=Ubl2icXw531sW3zcf1HMKbqbt_L89t3CnmY7jixsvgPI05m7bV3NCg8HCZyCHkrLzIEUd2urVpvD5SNtf9CVzsoJ3TmM6JG_W1PVDRh2hVOIvq80t5x8jvHO9CteNU6v2aQoG9h7bci1di2w-IGcQZX1bLCJiLiysnaP7lEcoeYsi3-keVtBroijwzx4irhfClR_QQmyaWJo86IF1WXhFHycBOU3AbmA8l5OGz3I_X_lMdUkPkmaYpM1xqo1qBT21HFZ0zatRcZCPVlpo5Mei626ENHwDBvA6uehOIvF2xfp1cZbgkYUECDhlzyBaQMG1L8hfRr848TXMREyweO1Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=Ubl2icXw531sW3zcf1HMKbqbt_L89t3CnmY7jixsvgPI05m7bV3NCg8HCZyCHkrLzIEUd2urVpvD5SNtf9CVzsoJ3TmM6JG_W1PVDRh2hVOIvq80t5x8jvHO9CteNU6v2aQoG9h7bci1di2w-IGcQZX1bLCJiLiysnaP7lEcoeYsi3-keVtBroijwzx4irhfClR_QQmyaWJo86IF1WXhFHycBOU3AbmA8l5OGz3I_X_lMdUkPkmaYpM1xqo1qBT21HFZ0zatRcZCPVlpo5Mei626ENHwDBvA6uehOIvF2xfp1cZbgkYUECDhlzyBaQMG1L8hfRr848TXMREyweO1Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=ZJtyV02pugCuC_pHp7D87I5smCCCvynq08tCKzo5aGc5qL_--LNWqcyW8_AfAOX6ZEtLT5lXiyq5iiDOKoAEgpiv9SrbSTKSudt_QKtPHvoGmRKPjVLhsVx1OkOiEbhbYzOBo-GF3yy9sXoc-sLd0fqnysYIeCbZOAdPVxxaxxKbHTKfrmYUTG2Q-UdS5lM_0Q5UQMuW00llf6mrQMGeCd6o_QGBGehIqFiLWBuJtD11WuqrLs63YV_xpLNtcUZojOHWDfcIQn8hTFouiyjkAFIXpAVvL7oqpjlP-mk7xOHvKazWwdgE6LaK9TS7CiHnmN9mTgJFiQl7s9TSicbxag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=ZJtyV02pugCuC_pHp7D87I5smCCCvynq08tCKzo5aGc5qL_--LNWqcyW8_AfAOX6ZEtLT5lXiyq5iiDOKoAEgpiv9SrbSTKSudt_QKtPHvoGmRKPjVLhsVx1OkOiEbhbYzOBo-GF3yy9sXoc-sLd0fqnysYIeCbZOAdPVxxaxxKbHTKfrmYUTG2Q-UdS5lM_0Q5UQMuW00llf6mrQMGeCd6o_QGBGehIqFiLWBuJtD11WuqrLs63YV_xpLNtcUZojOHWDfcIQn8hTFouiyjkAFIXpAVvL7oqpjlP-mk7xOHvKazWwdgE6LaK9TS7CiHnmN9mTgJFiQl7s9TSicbxag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=v_1LH_W04JQjNLDjLUb9QoagcBd6EUjhIEdFD2W0s3yasE7JEbwU5CyOeaXUcSVDoHRwlermyb6FOmkChIseqhpr62wjFuvnYAE-i3wkFpmd2nv6jpR42Gpq9Wyr3RTgU87pQasPHJdz4GDCAjZcr_RmPnsn9Iuk5fl6wsVtMTX3urrsHDWhOiLG2ELYu0RKWeaC249meR9i-x1bl7zWzdPdFleBxc7nJ5g7a9PQcVIDhHlEfXcSdWqnLThHBHQVtZjireFW4SylPwQKmrJhs1tqn8VZM5RXc5PGEy8Dg-5Be-Pe2UZkKLCcGVH9Sisv4Bdq-4G1iEBGuFPbROcXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=v_1LH_W04JQjNLDjLUb9QoagcBd6EUjhIEdFD2W0s3yasE7JEbwU5CyOeaXUcSVDoHRwlermyb6FOmkChIseqhpr62wjFuvnYAE-i3wkFpmd2nv6jpR42Gpq9Wyr3RTgU87pQasPHJdz4GDCAjZcr_RmPnsn9Iuk5fl6wsVtMTX3urrsHDWhOiLG2ELYu0RKWeaC249meR9i-x1bl7zWzdPdFleBxc7nJ5g7a9PQcVIDhHlEfXcSdWqnLThHBHQVtZjireFW4SylPwQKmrJhs1tqn8VZM5RXc5PGEy8Dg-5Be-Pe2UZkKLCcGVH9Sisv4Bdq-4G1iEBGuFPbROcXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=d6VEyuK-VgKOXlm9qFJTDokqti2xyZA691Hf0W6AHWXKBMr2UQbVh69HqBZUKOf_HhCqxKpv8vmGWpNm1fX2EVRqhcbAY1sJ06EauaxKnLxAaUkj7l0NO0UbzPSG_JPftXdlHKhzawN8q1JcSPMeByvG9GJZfWL_2FNjcWl7ndzvhYqfEAnjEGGoEqhYEOT68EEGLZqcVlMrM141r1y1fknRCo5PAw5PISIzxwDtdk7AEsdYDrHa3TEa88_ELs32Hh1tdenK2kLP3CsBpb4oZXvjCiCoxpuzag-ZbNp78Leuu7pnTN_9KAOpb3FUPPUZBuIVG7T017syvMALHIABEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=d6VEyuK-VgKOXlm9qFJTDokqti2xyZA691Hf0W6AHWXKBMr2UQbVh69HqBZUKOf_HhCqxKpv8vmGWpNm1fX2EVRqhcbAY1sJ06EauaxKnLxAaUkj7l0NO0UbzPSG_JPftXdlHKhzawN8q1JcSPMeByvG9GJZfWL_2FNjcWl7ndzvhYqfEAnjEGGoEqhYEOT68EEGLZqcVlMrM141r1y1fknRCo5PAw5PISIzxwDtdk7AEsdYDrHa3TEa88_ELs32Hh1tdenK2kLP3CsBpb4oZXvjCiCoxpuzag-ZbNp78Leuu7pnTN_9KAOpb3FUPPUZBuIVG7T017syvMALHIABEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=E-nEcjkiYrQSGdDpB9DcSJ8r9u-TqsV8WSNYOPhaAHCH9go8fi_iBy_uuxYh1NrtpcLMYc-vZgYDcaxae6PDRj0GiXevminIxro2yzrDxlrQS4030z0PTd_T8gfh8NGCHQJj-J9Os143kHA4XVuMyvBfk5ms72ZAm_XQh99KpY5sFY_ZNaaNxS7ZaW7nbTPeYEUXeXPQs30t2XWk84oby9DK_rjksNnYMNmo_l8iIjH85HHvjicycCVAEqHiLHuekvfD2PxTcjEPagcpnyFMUclIMG3GLz4ZxWGT-ZNqcq_mqquOP7cpSTguPafy7VrEs-Mhp6wQ3YC3-mVbmbYC3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=E-nEcjkiYrQSGdDpB9DcSJ8r9u-TqsV8WSNYOPhaAHCH9go8fi_iBy_uuxYh1NrtpcLMYc-vZgYDcaxae6PDRj0GiXevminIxro2yzrDxlrQS4030z0PTd_T8gfh8NGCHQJj-J9Os143kHA4XVuMyvBfk5ms72ZAm_XQh99KpY5sFY_ZNaaNxS7ZaW7nbTPeYEUXeXPQs30t2XWk84oby9DK_rjksNnYMNmo_l8iIjH85HHvjicycCVAEqHiLHuekvfD2PxTcjEPagcpnyFMUclIMG3GLz4ZxWGT-ZNqcq_mqquOP7cpSTguPafy7VrEs-Mhp6wQ3YC3-mVbmbYC3DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPN5alZd33dbBDgOnEL6Q2xsase1ut8bZBrN0H2B3K-76543Cr74TfVu21SNRahSi4VhGciH2-7Y0FoEW7QHlbZumDCHCncWHGsDYlI1zK54asV9unFfS3ecB1ro2cJToRpuwHyTWnaSCea85VA5vfyX1jCDmxPtNzjWbN1mVCHx2WlcdYHSKVLVfpnMLrV10H-lIUxPR_xpxnMEAPbFufP4z1xzUfmdxWNL_g6FLFN1SuddeuSUbL_bjdWDBZi4A3D-oyfKluKReyL-_RknMs6DWaACLSzRTmbBCMWKSu5hpobR9ugq-WokXTpXjV6BSMvLFCg0sDirPeaJAd7bPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IJ2RucYi_vKLJ3jvp7tnNlttNWnbC-pcfQOcHkeSk1P_m0ggGdkj3hBHtPBR9LT8ewlvyZOiYRISHtrlTHCwPYvNUX2TkjYTdWJWyw5FSDb4tgLt5BakkINiJsQptz2KEz6qrqIK_cm3EkDHelJMG1TfLX84jCUojrrUrxAEIk4F6lwOuy5-44924fzDFV45Wpma37PCTX4MVQdzCpiMqeJydU2TIroCLxBERVb7xmPyp8toUACLydKnZ1qRWEKsdMoC332mFf50-DkFkhrPhcHUPmmKP39VQhj99i_L9o9GGrICN97CelBjHuUNIdwLz9genpGR-GGOgzl5WaoK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2a9QDVxnFfQAIwUVwAAkIFOuOLeBw5LeacQuTTROzCxJ2out6Ggh4juJK8U7Wrtx4qsQv96BZkLFqs7DWNujXrdqgQHjQCHI_1VV7EErGm-PmfQgiNCimiWTiUHJkpotnckwJBFjQv4cI2-WS8_qBRtouL5LRlwRBKD_IdiCBHrDuQTMg1qOXqLCGTHHq0J2jBpi_tvY7J-KKXCWO5cndzAmdmRzbMiZkCbRJpefW1zJZd1m3SoYHGNqjBcESKZxiMUz9Ne-h_1FDXYfnNToxSARjp-jIKyDhvqvbPf0HhWmusJBejz-NnCzFX-Rf3D1hCeGQmT6S1I5wmRwQrh0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juARUNgDC1CbxwGK_XSAm_X_lKJa4fqEVsKCbUT4klCV8sA0meXjsbP4EJYPaaPCdpOzEU4IACthzxLLrq8xwwhwb10YFTBApGtRC6Qb6b3DbCcifRVNIXV7SqQomsseHgSdJfJPeAicAo6vDENUPd4NjdLfdTPAlyHwHDGZ56zcYsdroxXfn1902HpvSPvQTqYMby7N6zUXFwAfFV4t72lK5l0bGZLNzaudxI-uyCw5mUiC2VOvFM1oS5GhNyCcCWoiI6XfNtjg8Ck8BNG6irPfsU-_Z16IQSPd8_FmpEciyClKyqxaiI00wSFyFE_cb6BwYX-PiaBeBlGK6ucMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phK5KKOq-otZ0S_a79KDlL6nFW3w2J8lP4kT9GWPesaCPbPqsHHJQDLsXg2mHWfyV2MluFBTb6qTK6G_blGtgppCyHa79JVWuRvGAORI7AUkFOpcVagTgOMWVHvFqjQFRM1vGISsJlEFe2HuiqnuJIsxaOWHA4XxTDNKrETxJzSOqqmEtvC-BjKIPXm9tV6nvYY-cHZN3jXSND9IRY5qe-pbJmPND09NQyNi8t0mT64YxjV3rj5Gzv7QljX6VneqQcgqG3nthKq_3fZfnfzuFDpxinOGB06xVCttw1_vd6ntAhooY9fnBaZq2pbcqomW6lv1nAoE08BIrGk0v9Piog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMlfMuU-xIX037BE4SUiSK9WjGcw-T1L-D-WgI29NvqO7vDFEdXeGSDJXq2G9QYDyWtBXXj8W7xbI9MePoOmyHPFlABLqZIqJBZFdJJBBtnvS1VaMGeJ9BHxRtROTEe1qUwTF1rgZOj81PwqRea8GFcAuvq8erEKw-tZwk_IPjBQFQc0gsXhJF_iA0Hh3vSIZOLYRrVbP4DoGKB0LHJZ_KCJ_iDT0wOq4jjSr0mfPPr18uasbWm_teIu-QrC1GVUXSw2hN9tEZmruYpcmlrOYhu_JjTMjSu-6mtO5lpgSZf0LsXFvD0Qw1U9FnS4dfZuDSG66fkcLLJ6eMMYEpCxMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoQgLT5b86wWYX-yW4YLx_LGXhhAOyDmC_bzBojdrqyLY9cab27WiMEYUnTUv8e_M09X9EsJ-KARlGzEx4vHhwa42qPcC1F4qs_QKxlKNC-4Bcf2KT8p6DekyczRWbaulrnz5sV-A3Nz3KHs64rHaKYEXSzN0mmi3mzhc1A58J5KG8ZoLGTQ3MiDkmPLBClczpn030GWBvcNH_u0n7h9DXkVdy5cDiwJWikkvWcHqOkc3dbtwxeYuGqZ8POg12T7Df09-RET-WeENp0TRvt0c_wiDwnJAMkjFASJLvFkvaFNHR9EQUdTolgAj7R_cJrsTjpm7azZFQonAiwBOYSRng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC4Iq14FTAdXn2PXybDnJ1YbbVLK_I6S2eO4oe5BE-lobHAUZK_AeovKjrOtImiFlVWLqB0OJNjNvDyt7hHhAYPNhZ1vAnT1Xnhss4M1mlRlOQBGK58I-JDFTLngMB8gdlIHEyZ_AuNs9XloDIF6K8S-bchDSKCA8ISOhewRXG5Q285OcvEAQingLDwX_DGsJEDFjpAj9NPqCFKFo_CY4USAz2vtO9cgLACcIiNO_bNMs5kUPsbqeiLbeTcQsQzA2GtTM68TpZseWnj1BGffINEXQYweMkYZJovIlle0ivEuEWsPYwPOrz-KSdJN5ceJ0R_WuS5Y3Y7JJz9axG2-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gamiLJu8Q7sZpsrf9FLBEqPuGWOLtcyKGbNZ4Gj1G8TMc-8mGCDkcKYo1rcOfUR-YUokEWY-9UhSjzFR9dIrV6S39I3Q_ry1l1ropCXnMMpSX2HuDr57AH591dq_k4yjszB1PBiATPUycA8NF7qdL4nEFraNJD_yT-TG9uABRnbgZMym-hFHOne58rKrlOO-c88jdWWxtZFrwCz_uGLR-p6LfYGR_zTNrJc1_Y2Kr1gNc2SSrwJbhrrz_lkDeP4W48HDGBX0zTJuBN-Lgy91p05_01NDjIU9pK8R1De8cbpAzKuJ1b528ZWsrTbdoivZHqD4UuukO-pUxXXG4rapVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwl94rumq8-lpBVN2Ah8nbE0FAIPZpL270gKwVyOZ20XC4J_3tPaQq2Vh0DSc-tlGm9k0uH3mlztyCoeWpz47Ko8TVNR6EBY9bPrK8hlkUwjm_UeBXgQZhpxHfcILRZk7tzjyWP7nAE97Dl-1-BnL4vnHnEZl8f_9ezlwNVe4AFs-Fat65mooUqNOe82QWl18NoD9V704BVSYOCNVOmFdeC8Mn9wOqN9T2wFbrlaOAoMjcqSXX9wrW1P0FqeiGdqr1X4qAkz-PA44fID7zlIFIqh30qZcgmSvBnMkpuVtnNMRstUe8FECYuYqZUnGQbfnza7IPUNZDOEZrmhwSmuNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPHhXcsvnSaDyTkmiWA-xmlpnO5wBnM3duqjS3MqoKnZK5DJXmSM5dd0bWNmp5oUEDymvSs2JVqnxoJY1iWod_egKW2Okt3juutzAvMk-U6oBzIcZPdJSqhPgD9Oi_jHUI_8KwPn1p6IxAX2zCOKOpBzpvkx0YY7_yPDAWV_opmH6bpDZzdbTTNsG77iE8qgMwhQh4EpYzBt7cMb3RzbcbmyLpmC5LL35vGIJlgnovvhoOEkK3-eknvdcZEk8UoaMrAAxd_US6MM5q0BW0BW6OLb25M1XipmkNsusKqT7lldmPz7kGXtLVJdFQBEZsH9LQibsTYBwlP6i-rUjN4Pmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW5q-fIOS1quqmh4GuIi86VlrdyGApMjHDLiwTsDcNqrXsQl0d1g3hHKzM9Ikv2gTf9kC5q0Z-NDPziTabe5QOSkhqEF47miBzLQFA5nzGDBYBWtcrO5OQVPXzAVUvZPnVlCrKnbyrxPC1CBltcg8fS-xBWBfJKyvqoDaZ149r3KuUG23GZIg5MaHSxighnffTMHgUXk1aOp7oJzwvM7pTHEjFf4b2f2DOAWO_JP8lbWtdM_mJy1xDjfotur363T9Qj4-Ye-IhcZrCz3RiSklmyT2-015-TCbAny-Yj6NWhEojNXSG5pImfp3vNIDGd-xujCqSTfg_a54Mt3CiY22w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=RfnWnxC0N8VWsg8bMw5cH1_HTrYDr9LqHXrDP-cPyYQgzSLu6OBKt8yB57mJEkIr0xLz_cDgbLG8Ct7u7SIhhZ_L4ohUGw9a1xbSN_PNiGGNVQfr3ahMDmOpqwlHjgY7t-bIjeJMAJi2nEy9Hl7StgVBdHSM1Yxld46oBRC9iOx3Wdsmrfs9fNhjRRPbfUEV4RfwlL-87UK_qwJLZWdHpPYZyqZ-Xe1sptC7mZAz5zvdzc8ShC1aw7hBU4OD-2MESpvRiCNORV1SOspojZiToqu9VqZw22d4rWDB4rRspbEjkXiRSZLGEXuQ2okjyu2pwi4PUHsXMiCW4DNHbm1t9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=RfnWnxC0N8VWsg8bMw5cH1_HTrYDr9LqHXrDP-cPyYQgzSLu6OBKt8yB57mJEkIr0xLz_cDgbLG8Ct7u7SIhhZ_L4ohUGw9a1xbSN_PNiGGNVQfr3ahMDmOpqwlHjgY7t-bIjeJMAJi2nEy9Hl7StgVBdHSM1Yxld46oBRC9iOx3Wdsmrfs9fNhjRRPbfUEV4RfwlL-87UK_qwJLZWdHpPYZyqZ-Xe1sptC7mZAz5zvdzc8ShC1aw7hBU4OD-2MESpvRiCNORV1SOspojZiToqu9VqZw22d4rWDB4rRspbEjkXiRSZLGEXuQ2okjyu2pwi4PUHsXMiCW4DNHbm1t9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=njlU8QuoeC_rm4f4gtYX9FjeZj956fwVxvqjE77QwJ3lgje-1sQym7didO407wCT7ttcD3rVFf-tVNGImS_MYFe0DCKYsV9mmqq8d2yAEW85CPpEs__kqyZ_bHaiiQ0KZKiOY49zeQoz0167uVu27b_qaZwMnQXc_WXOjb9Zke8xZF2MR6YPW-7eUPKWBqUswiOp4WsmemgFwTO3J5H8zny-Oseq_8oBvPYSGn4tyeGCYHMwKOgzBwPQwoNFJbq4TVwFYqqX9bjCovMH0Ir_PrgsLeNaxWVJuNa58aQhTHkkaPghvAxYUOM2GJNobdv3854nMJkrOaz7LWZXoVuHfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=njlU8QuoeC_rm4f4gtYX9FjeZj956fwVxvqjE77QwJ3lgje-1sQym7didO407wCT7ttcD3rVFf-tVNGImS_MYFe0DCKYsV9mmqq8d2yAEW85CPpEs__kqyZ_bHaiiQ0KZKiOY49zeQoz0167uVu27b_qaZwMnQXc_WXOjb9Zke8xZF2MR6YPW-7eUPKWBqUswiOp4WsmemgFwTO3J5H8zny-Oseq_8oBvPYSGn4tyeGCYHMwKOgzBwPQwoNFJbq4TVwFYqqX9bjCovMH0Ir_PrgsLeNaxWVJuNa58aQhTHkkaPghvAxYUOM2GJNobdv3854nMJkrOaz7LWZXoVuHfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tB_roHRN5ODjnQpRVyt4Ce8egfSoaYZd9ETl1ZLcdq3jkrY_hb8eq2fnWNHNcHh5whhpqjYCamlIERsgGMIlVhSbKdO9wPxsOUSkSYus8gYHHllmmZh4JpmY1wQbX-NFwGvLZxSH2ytAh1YD8_wK8coJTDGL5vNjFqVr8hnSzWkP1sPJzBEGMjjubjmLWFP0Uf00ufRUm4I_XMl_dPwekgmAHTiQ90miHHG5qv-EgUAhS61KPha82UQhl9CsJ9jRorKrD8R4KlQKc3J2HCTUoA_X69Mj2Xu-gJhiD8BUEvgRRn4hA90pbsMpsRnyVGRR1zRNXg7rztGS6CBzLdop1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=tB_roHRN5ODjnQpRVyt4Ce8egfSoaYZd9ETl1ZLcdq3jkrY_hb8eq2fnWNHNcHh5whhpqjYCamlIERsgGMIlVhSbKdO9wPxsOUSkSYus8gYHHllmmZh4JpmY1wQbX-NFwGvLZxSH2ytAh1YD8_wK8coJTDGL5vNjFqVr8hnSzWkP1sPJzBEGMjjubjmLWFP0Uf00ufRUm4I_XMl_dPwekgmAHTiQ90miHHG5qv-EgUAhS61KPha82UQhl9CsJ9jRorKrD8R4KlQKc3J2HCTUoA_X69Mj2Xu-gJhiD8BUEvgRRn4hA90pbsMpsRnyVGRR1zRNXg7rztGS6CBzLdop1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITUGgn2YnURkPOdHB_UwZ0cnQjGIEfY7cr4FrRAfB_U_P5IFV5c1Ild5OXWhoOSeUG6OPXKtS8-tLrLHvYTcSj1Xu_vbuQ836l68XPAFlDCndQL1OORDIS--BYUV6LT4TdhF9tcao0MDoTZ8yq0V98BshNW0rqCkMexJlfs-yqXRLz1d62orLs_tWDxMqXdWT6HYkLj1Pf-WwjTK0mGm8DVt2yhWnN2zDHXH2taihAhltwMxbjcdWjNCIVEEGWd-ZlumPeLCFn4Jak92wXl_-hIycZI70OvwzOMLFXo0Wl4mfncRWQ2MFX-bEMAKTCqy-IBK1Y7WCLsB1NyvTG3ZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfyM68wXTSsF1zuRox29phtiqRAtJSukvwQatHNhoBepPcc9dDVk5QhtRItGIgzNjiU7M1tet1CmdM7tr23UmGt0PvZauSnRHiEqMRnoMTp6l5mQTdhSEro_USfZm-PzpBLHZ5cmMyQpqtgDC2K0FPZCQHkgzlFbiQG3C0CK3OXlAvtQAGXWLQUS5agHTcLErtbv-2sEGuRwTsORBVoQZcl8CgH7rUoXZ6VlLy3uqIiQ-N4up9W01X9Xy0OqDmeUi8KXHNwYRT2rpddvxq9RXqVY-NBVUOJeYtGff8DRZGNmS9lIhPQ4p2NbVpI7wIQgy5FEtRWlV501dI6ciX9zrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTs3HZChaDk230rUJeh_PlIjfLRjQl_Nwzx1JzZuGMyhV_5iSz-er94jmEQ8jm5nu2U3p7xmyHtYQ8DiIa3_LQh0-Nhb1bVTxNgPVFDOx5frINGTBX07bx_iZtnpbMhcD6oIhOMU7f2NTpAQMASqK9d_GM1LUm_UOoTUxU_lyjbpme9mHvGk5VhxDeJlskTPbXH7VScVuww03ZyTrVUwFLfHz1Ph9d9CGbNCl2k5CGQYW5S9T-MhFGp8yjTen2L9PhDxIfx0UbXx_UVeMu-KcnEWs-m2MBcNUyTTJ8d9txGAojssoXaWwoGHhfBPL03uGDl_WDu58nlkszkEYx-V2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=X3DZlg_kYk0DCHKqX-8_TjP7qfBckzdHLoEJOjW7OXow6kHC2654Tj40PQvF1bdkp_YfkBoGYkdr_COmzNwh1El2P5S0Jqqx6LgldCoOccxsbQvY1Hh9Put0w-LG0vfghoKUBdrXIk-A9r7HlIHGHL08sFWGyzLLljezbQeIHh1N2aCFSmjcvUcP74fpF5FFUMWFe67aftKc5pjt49UrwAgYenG2UEYUzy_XmyvBT61wrZiwQWeznat6MOCGUIfy2lAEhcZAt6oZBlO816MI3t58_GwmvvrZnYH0dzWTKd4vPNERblvfqRUh06myFOOyJwc-KvhgRPMEoysHt3N6HRudkcGP8P88knK8lLtI3m5T2TRv1IfUFNTHrW-Iu5xZooVj9jWSw6A-JhHByK_FN-UI3BVn71A9hC3nvbs2X328Ztn4CX9yLIc5GRl3o19HazENFBVem-Lu7WxTFq0oAO0k9uSEE57E_M8c5IODvFxjiVByiKEUa-sQb8Y81LobcslUTrVeZ6JY2neAbbxPha_AAz_6mePDEwR_Ea4GNzFUM3QqkRuD_3Wjxp2kjSOlx24dyvIW5Br9_RzSXfwRQkiZoQJKFc4nt8sr2Y1mL584QmuIFn74apikurYpIug4MVrb-rJIKBwWvCfaKQhfEljtuewBHWfR4G2vG2SxPjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=X3DZlg_kYk0DCHKqX-8_TjP7qfBckzdHLoEJOjW7OXow6kHC2654Tj40PQvF1bdkp_YfkBoGYkdr_COmzNwh1El2P5S0Jqqx6LgldCoOccxsbQvY1Hh9Put0w-LG0vfghoKUBdrXIk-A9r7HlIHGHL08sFWGyzLLljezbQeIHh1N2aCFSmjcvUcP74fpF5FFUMWFe67aftKc5pjt49UrwAgYenG2UEYUzy_XmyvBT61wrZiwQWeznat6MOCGUIfy2lAEhcZAt6oZBlO816MI3t58_GwmvvrZnYH0dzWTKd4vPNERblvfqRUh06myFOOyJwc-KvhgRPMEoysHt3N6HRudkcGP8P88knK8lLtI3m5T2TRv1IfUFNTHrW-Iu5xZooVj9jWSw6A-JhHByK_FN-UI3BVn71A9hC3nvbs2X328Ztn4CX9yLIc5GRl3o19HazENFBVem-Lu7WxTFq0oAO0k9uSEE57E_M8c5IODvFxjiVByiKEUa-sQb8Y81LobcslUTrVeZ6JY2neAbbxPha_AAz_6mePDEwR_Ea4GNzFUM3QqkRuD_3Wjxp2kjSOlx24dyvIW5Br9_RzSXfwRQkiZoQJKFc4nt8sr2Y1mL584QmuIFn74apikurYpIug4MVrb-rJIKBwWvCfaKQhfEljtuewBHWfR4G2vG2SxPjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBCcop-X82dNlUSaU2dP-XUSjJQLK9tCfD85aUQXBUdXdvP-505SYrsrI4iqpw6E23PCYIPGTQO2_6tXjeqdSpDB4KB-SY2UN1HrpqfydKF8hKsv9dbp_MQFcgOriRpoLbw9AP6Ke-jz4WjrnpbdQqd3gSH7U68OEpYcliVF9Nc3jnpT02J7XnjXrV6FWp2fzaXvSZp9RJjivM1N7onvPE9aW8xKNYNivuRH5ncdSNSqxIY7GN9RKaI63AqF8FPEp0mW3Y1NKfM6lD1Vbhweh_Ox6kZ6BgmDsNSPJZJ-l42YjWt9UY7yvJxPBJ7m0wwVbvy5nK6WqlsBkofT7WdJRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChauiyryphAevaB9JbF0saPRgZDCFtaCR55qLOaUab2dVSz33YWd6z1Ionu7hMoD6HHGks4jUrF9X5siuORB6Oe7oTVofuB7nVuW2HZAYqHT9xQudAKeKkprGMSkcWRAr_-FHOIS3BEp_dQUi_edcxMYW34FYsnfQv97rAV2HAboUo72MatkCxKI3Sbqf0lqpt0hjl_0Xyj8VJ2IVAUFo46fspLA9VcTjc_IENg-YrvCfjhCMBMl03EAVl5ODEHUcxk23GlWu0Ht0F1V1KBU-2SwW9bcaN2YCcf1J6GkpKe7xb0uL9TCgIfgqvVLpdG5D_ca_WjukD4d7oTduyUGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsGBH3g4Qvl97svqLaRdv0tYc8x0YLLJgFsv56EIck-zV7z_-IuFIcoCblPZK-ybxhsL_m6FhPqA-5P17Dbu68nMH8VIaWkb3SU9cydaOea8dif5hqmdd8ePgapBdu5K0XMG3632hr4aJN_wz9doxQRRzOyew_r-JnRZ-SThm5iXzpSl85rUmKXzhqJZstN4R9-PmHHAaEBmYmwEHSgFQvJv6O2qJljPxJemF-IqNe5-CMPBSVHt_I2siFrJc5zkQhtsF3ZLnM9cSNauguC1F0imTieam8zr0gfr8mUf9k9nVzPt0qJPgQLwBr5XFOIcBDbt_2ozL58RnMl2a8ywEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFHeTZr8Hir6uksepXVgF76V6S7gTwdxjFD9Z8GR3noUdj2DeG5FnOp7NwFfIlLaaE-aOcQ3ZkxEQVx73Zf65xuAqUqqJ2sDwZSXs6xu_cDirhqOv2uFdWulntq-n2G7zildTClllj-aSSUqyllY4pxqn3BFWuB_YwblsMBMibCU5CzlhzGyEShLRu241ZTYdcjec_JbOmx_sDtKHszTkNveYXISBPYWQlR1bLxB86Q-0djNmoJTYq587FAJz6FwW6WWK-RJYvMwh36bEh1tBwkB27ZKH8Cde04XWW3I3pjicDulMpv1ldGtMt2EYBRS_pW91w0EhSLEViL8bBM8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmwP1hnb20Qb8qEl7BmX-xQqd75NQ1BGLs644wddYahPhXH6540PIHFiyZbYMj9S-C86YTpCWdzTzCO8azKVEODfWFXQvafODMXqo0bPq1HA0kpVc69FFbj33dBD20z4lQlRvm0F3Yy1YBSM0F_v17eG6_QoTctn0S0k5weFM110XoHSGOallGMSoGteHAA57rhi8vvUIMOhPmGbXACFXWMY5cjaLrUtzc94z03hu69WAXgt5mo2qIshUqRWS5F35y6XsdBCcNR_wjh1Ooq-2lpMalxuMCmRBqxt6Ohr1dRCMXx4KBP19HkgdBJYUH1TEPx7QDMORX6rmGHKlj2nIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQKQ8AJgkEztJHzF28Ma2rJzU4EaWPSth66KU0eYxGX_FjKLMIMEAmaZ6-mxQbe30tdYcpRSWkqyTjhiaDy6jPuS1-bfVAairLcmaz_yLZOIsS1FyRo130kg63i_Wpt_piXKS6IscZ5-5yc92ApsZq1eYdBLy0_NIjIn61eKgZoXeWNvUqZMNqi5kfkrxdrfAj3O9F8QW5ZytOxm4-PsMqDRLJaxsX-t_yVpBUr04LnbA73JLkUiVyXlGDRvLsDIwk7Iacr54XhxmyrSR1hlM4eyz5wk_oG5z1g80CwmLM3ubSMCW185AcCnQ_YrEAMQicCKwvUzUXqOC-OVDOd38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-FV9x2ZOw1lHi_SLlgsztKFP682B45N8IvhX9oxQlo8UFxWejkWbmiK0gR07_YO3GjuXlQjaH1hdzYZ3x7C7_GJprAG5LwyGaduQEeP2B3UZ_Af7LQeJwi4GBc92WZzms7Xl7NBFinY2NjFpdrMdu9yTCXEQRNXPQ-wxsmdaD6vdVjbpVPUDVEGb2HnTokzKOddJyDmXUQ7zE6MX1t3zQNIj_iti9yBFWsTqjWu-If9Xs9rMJdfOOQ_nbhA_ItQEgRBm39tPxee2NJ3pt1wEfFQxQPz54ztKrefGZe4628mA78TaaSxhFTJXCyUWIgthK6D_6wTBI9CeJV6ImnKDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbAJaNZXQh6gxM6V_Vwuh2Bq_4CWC678L2i-VgfgubDeLeyC93xRLlyklaFEYtP1QLDe1c8Gu6tbgQOnTuwwl2S_MUKq0uSkTarZIQBmiNhhcHFzga_49Q266arHZHVehBBwvOISqnTmX-77lqN9XBlZfXZSKbs-DnITsu6FnUapcXNFoPf8Bwaks_fBNxDfpAdaM5unvnFRFWiSFng2ei9CdMl6GjtpWy538dIzTUoBAak_sRcXLfI6VlE7HkzIEB0gY2nHzrSU359T3yUab3-TeNM8ipi_F1CDmdlE2eetXh0dhEleHWrbO4A_SQ_4CBJ4OB2r32QPj1PjRqRIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnJQYacd1A_qfAOolR4ojxRXwntk_gsQiGmLQKUSjV-IuxDAH6lmf2AE5rwaWdddsOEvVcj0WYqyCJvW9gIG-763fmrvrP9Ox9yZhvgg8PPTHyHjdAeY9mggBukkTOiB7VSHGjjUM77_wmybhYNb2hWJ0i70UF77LQCCMerGph379VPzBZZxIk48GUiBx_e3GAxoGLJmquIHFpgyMiwwXv2w57ZR1ec7h75iQ_Dg1XIbYJQ6rV-evwqAmYFal8_QacnHDq--mF10p0hrw7J-s97sv4Xja8wqCjq0IlP3824uhZlIO1dy6cH2_-etDddAnUfBgb2y7hBWowE9M6qNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_ucEkoLYDkbFf3vHW6TNcuecIALT_TIjeGEg7_ILBzgV6rz2IQHgUv-G9W_Ail7-bcNiGPZwq-UQvR6J4AaH8QUNZuUiIDrS3x8JIwY6LXCQcR5Cy2nBpnCLNeUvWn_H6P_iuYQZaPvInK1vgvV2apYg4_zTCPDJS-EXgGEU8yyEZSkmaE7O5puK3ud4Ps-D5PC_zx5sEJ6sc18lmxEJ5fXvcZM0Ca6Alrnwk_AUYclJKXAPS_U1hPJEHyHDOXEzHbXKamWWYm5hdM_EL7y2CQo1Z1tsrMFWsnUGi5j4KMQ09QFjcKk9ohydGH1Y3KefQi674yJzYKQdTPX-sSyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dc7Tiiod8Fpx72CG-OgdEV3fnRgYbQwLeRSBLxNMz1uazntGRljtlvfqaMnGM3ulcnzF4LOgoNh7RUorkcmRCk8zFMF4ICOJ7qivoaiqMWy8SwHDgHtQ1berwpTLnOOD-dS7bum_dQzeBKh7C56fK7WtsiZRWV-c3R1sW2tU--t9oUG7cVnp79Xa_CReWCc0rsMLb_CTG834gq0xXh2RwhNH60RJJ22YzY6Azk_t_ZHTyh1NLcPTbWcFvgL6gbe9OvdDv4UG3eACp07yUNFFwSs3MyBNsAWhn9FGwH5avCqjgfXpBZ7svx1wS_daoMLyVqZpzoo9wrelzmXzVKY_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/El5H4DyyJ70FASYHG950rMQm9YouKqA5w6lExZJ3EEBxofE3fgPJYZ8hyTdo_XTR3jXuV5kDlaciiDaknI2pGV6HSfaljCEdySqHd_Bt8gFs9lLfS3zeu_nJowiRCQ2uQRGn-qsn0mdtes22nQBBjn0k6PPIYLdJwWnaBWQGYx37lMvNEPHX7ghJIeSbDNKEaQUksk3eIV6hwlBB8eENmBIHE66-YRDFwFhrbBVZEms5fBnXhjGJ2skCbBS9Ktm2H-ZoqJEue2EEz5TkOX6wjE8j1AziqZdRzYSZLbMwBoNb-qPNrdotlD0JGOvTMK1N14X-J0-wTU8cd5aZXDLiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=B2LO5hsqApnnUnwqbRCk6OJQA15149n6AON9Bspt-cXD_uvduzX9hP-z2nOoXZufloStmeJmFIUPb81APMOznyAYfw6j9aEf6CmWXhgb55aaLZjym4GAWc61ddOrnXo3mbWvibwfA8bySYUMgt2ACAVGn96Bcx-V9r6BRj912T3ZIU9l_OoNbDbt3o6iBj7YXJrTUuUTOBF1uwsGIY-qCZ_wg-DPSPtdS6X21y_LWg2OceP_11pnDpmNM8llmZPMbVp5Er68arhfxRr9U6eq1QRgKg4VKf9gRQFSYR6fA9Zb2i5EyubHwldlYcQfwpbsxGOENp0XfyXVcA4BUk1vSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=B2LO5hsqApnnUnwqbRCk6OJQA15149n6AON9Bspt-cXD_uvduzX9hP-z2nOoXZufloStmeJmFIUPb81APMOznyAYfw6j9aEf6CmWXhgb55aaLZjym4GAWc61ddOrnXo3mbWvibwfA8bySYUMgt2ACAVGn96Bcx-V9r6BRj912T3ZIU9l_OoNbDbt3o6iBj7YXJrTUuUTOBF1uwsGIY-qCZ_wg-DPSPtdS6X21y_LWg2OceP_11pnDpmNM8llmZPMbVp5Er68arhfxRr9U6eq1QRgKg4VKf9gRQFSYR6fA9Zb2i5EyubHwldlYcQfwpbsxGOENp0XfyXVcA4BUk1vSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=B7GW0avTBIVYeGLdAyMKGwWOQw3CXbKmawzSVpjT9CG0v6I3TRVpd5Xyk28QAb3_Mh3-HIRb7CSkt9twDG-im7MfdpVtGmdfAuZZ3mHVN4MkSnPJPMRW27aiLH-yg9D0Pv5xyiZFnBzFyLC5Q-0nrm-k3xIUi0pVQcwHXR7UdMIsPM7oJa5LekdPvZzTpAWOcuZ7D6y8tNAWNvl_ZvmZiztSli6pxHRx-kE3yicw_MYJ2ZlHceZe-n1tG2s3eWfrQ90tX-y1creqwcZricca_mUcj3Z99OVTLiYV-0DxCUowp95yk2I0Kyph2a3yPXPxRq8ReBvTZnABO_S0DRirmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=B7GW0avTBIVYeGLdAyMKGwWOQw3CXbKmawzSVpjT9CG0v6I3TRVpd5Xyk28QAb3_Mh3-HIRb7CSkt9twDG-im7MfdpVtGmdfAuZZ3mHVN4MkSnPJPMRW27aiLH-yg9D0Pv5xyiZFnBzFyLC5Q-0nrm-k3xIUi0pVQcwHXR7UdMIsPM7oJa5LekdPvZzTpAWOcuZ7D6y8tNAWNvl_ZvmZiztSli6pxHRx-kE3yicw_MYJ2ZlHceZe-n1tG2s3eWfrQ90tX-y1creqwcZricca_mUcj3Z99OVTLiYV-0DxCUowp95yk2I0Kyph2a3yPXPxRq8ReBvTZnABO_S0DRirmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePHbUvT15OKXKF20iAtYor2W9hOIu9ud_YyRZenJwiKcxoODbIDk9v0eldytHikBoe-IzRgJ3MAnVismMEZu8t3K-t8PsGjO6pq1RzTXTmp6EQ8Eu_p2IadOPdAsvI9qo-Wlr0lX-x8qouKtOBuiR8E7vDtShoS2MtKlRt2t_50n5VsLvtOOeieDu_03pK6z5qYXBykTxG2DCIPOJICenj5w8QoLSi-LbbY14uFsDgqTr_P5Fq3LPbWeiIpbql7jV2kAY_h6tz0eCHGdBUFIK1IkkRc7DmDTjn85c_qOxaNScGbArv58lvx97Q-PZIMKbgdjtTTJn93mrUpR34rBrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqvtHsms7PK0Q3-0lpXGHfL0q6H3bcwINFT-TuXcW2yYZcAMiDpHtnRlkoVRKu6GXbX11VL8uCGg7LQ3tOy-Nwx_YVjwGXBBytwgeY7G931cvGcfy4e_5QmcFLvUjKrv_nk-TRQZh3haOXrXZ1nkI9SuBgf0vQCCRJc1DbU7vTJp-H-xcwJBlRJsLK2ABc513NoSqmltdzLapUr-O4aWONd3swL-0H5y9QtQuZHG6LR-pIY1gSeLxY6LtSaQciSUW0cpcln52omVi7nuvmP5HfE5eGPBGR8tWI-s93qEp0x-xB-evc0JU-vVFEI4CgRmH3Sv6YMEJTnE-OzjhaTZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L71Qg7Mpb9x0LwCUMRFuqDAvjDOfwmY1FvvwqV5xAHHZz9zfRxxrBHpnwJGRuLuyH8p2CK40NH9-pYq7srQzLLysufb6WPYGA27bOeoXgOwgKbPZbkJ9sWaz3Caziwa0mIwplJ4rNTN4FTzld2uFei_rbUMlxtZXmc9EYW4IAK0kuVE98-XjFzqhdWn8lQJ3wRrF2DSw6jpbQV18NMn8RYAqiCp_ns8Wx8kPk3rDBbl7RLQu70QtVp9wcWn-lanXbXlh8zBHyu0e1E6HyX1lay3tGIizcOG-JaOClxPkI1i7YHDBfIaumTvRt-X0SG3w-b3uK42EG3UGI1Zhm2rNYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv9-FY-HhkM7LsTE0lHzDiTHqDNcY9JRQ39uusCNTjsRcxrBYx2Ck6wjhWCYD46wb7HvvcMIOM-gBh9XDGuuPZSIAcLeT93EyqbzAoXaidgIj7ygwv5W-H-_ZHWT3X2Z32DRhvSon60viEGWO2V2-WhSxOPkAhxPXaNUizPogWv75aINqWE-jTqXg77bY-X-2AGZ2TfUQGJixvpKC_OMr6baI2W-feVZfAJLd0f3O4OEA_pM0pdFH9s5RoFQdEtziU1v4wXV8S9t9teBNpHfs_Mzvoblp0ts5ZJB-HpLJzFyWNh6w32jvwTRKnDkno-5T0fMzzGfwLU3Ite4a5yuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miKI9LX-7fvTKVx_9yvVXogjuRa4_C5IKaWImDZd-HvUsfh-kF8TBKa-YqZ0ws2mKKSS6up_ef-QqD5KkaFZhrL29FEH0swuslQfy9o8u-RjjLA9BYtyXyjXGuX5KVxmzs2A1aovNw6A52Pkj5kD_8BPpsP2NNvBRjjRNNwtpNN96FNa69tvVZMrb7Zp4QfM24kUqZ22JmxCvmujpyFIBDtyLKVngjniwZj4hQ-VTYLYV-f1PQeuPxs6y-pb1xzp52RooTTSrq8wwrVpONOidi-3TBl0afert3KTGthYPTDC3s6fdte8uEzTcE2qAzAK1nPuhwKfV6DJL3QwJwMR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYpXY9BMUH2plU-J1ibu2mqwouPC7ixHReHTzOgVnvF9OV6-otWHgm_WDs7h22XBuPSXnTbhV34MhuQf9hgfXDhFFO7l9tzBavrAUPDNNaCDG0lSNPofAGP6kGzt2Fq1GWWy9X8_vQFAUCaYziHEiYY2_gas9B9OwMJ70933ARXFcGz5zqUw5odbB3zdyG9e1Nn9FrHVSzL_2ejOFLE6gPekrIOo5tSV7d-SkoSSNZwo16a-rLjTMYk8qbnt2UEcDiueh3YwwVyWjbcpglr5cPeHcuhDCRuCIoI7jp4UNv5zwMIcUd-FIYFLtcuhM6aSSdqwCBmQ2yMFx-foxMJ7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnMmJvXM8uoiaa_9BG6qiwjySCuXkKhSkosS0b1KtsECVUVl_Vz57mrdWKbRZFpnGl7QWJJpceD78luiWwoCJ9tUQ0gxHW6vIRU4swxPwT2FYMLPkgYIwx7VhLSNPD50mIEIKHyzbZrUz-_NGIZ8ElhjKup-Q6wGzWC5w-eyLuHA8BgJtCzluVzZL57IDMoANG2WKXBuImBRsTKwQjmhgJ6Kfi9XPMovpUArc2LUBmQXDeGVL1NrNUBv2W4q-hmezYkGLvjPHEgYKbuOot3pod6_wl7qsJJfjJC4q5SBmtgF9i_x53q8UljZx8XZ8Tq3XjnkZPg0l-kMU7KWWU8xZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7aOxDTcuzVru1wZSUA-FHKF65QzT6NcRk6pfnlhPxwucmXd2P4ecTanca3y-RVyk4peymBPPllKCQEMKKigtfkpkgpLqGmFLggwzABtCsLqQqOezTt97eHBoKqzVPn8sxdFWaCaAVIRkgwFXoPbDqfInbt5y_zlZfsj9r6quM9ChM9DEYwBUFOPXvyxaUdj_-qZ5h-DGn3mvESCKs8-8oz460iyhH7vSQnVnpbRY3mykerJPY_io2wOhXcNuFDm0bsu6EtW9QCwqStNkDERpLU3Gd8lt56WvAG6FYH4ST8dzV4IkAwA4H5Ji2xB1sTJ03e1qhRxgRPCi9ibugHuFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=cy4VupEVreTwlbfXUIFeARHuVPqMP7KvxtnoJbkIPZBeVZGzXcAIh3f1RCQ6Xe9mJITjS0rpnhx5HCzVXa5_Eav9Q2nD8FRIWEdBN3jVYGE_gKJOTN8Qtf6x4ARPO-X6icunnOxEw6SO-vaY9yMQ7pgRfd_k0NGnii4EQ3kUdEQkiFlvVhoau8p5JaVijG0cgxn3riQgKB358wy2-W4yT3Rdp1pGkwPoarAId_ihA64Sra_OJ5ivKFD-HL_0GbJ6pJHft4VhsUI4KrwTf7c6VvM6YoAruaDndM_1gJCGsvRvhh9-JDlDMm2Un3lVpVh8H6X7YEwPIcCYkXEjVzNTxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=cy4VupEVreTwlbfXUIFeARHuVPqMP7KvxtnoJbkIPZBeVZGzXcAIh3f1RCQ6Xe9mJITjS0rpnhx5HCzVXa5_Eav9Q2nD8FRIWEdBN3jVYGE_gKJOTN8Qtf6x4ARPO-X6icunnOxEw6SO-vaY9yMQ7pgRfd_k0NGnii4EQ3kUdEQkiFlvVhoau8p5JaVijG0cgxn3riQgKB358wy2-W4yT3Rdp1pGkwPoarAId_ihA64Sra_OJ5ivKFD-HL_0GbJ6pJHft4VhsUI4KrwTf7c6VvM6YoAruaDndM_1gJCGsvRvhh9-JDlDMm2Un3lVpVh8H6X7YEwPIcCYkXEjVzNTxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFyMXZkb-CTGC0m7VdUY-iL6ScywHDdJFGi6cdsJFGQP9KaW4AWNNDZ7WA-UT42MrnANwIE6-Hc1PL7hoY4cor339axXYAXEjmvOxHj2YZfXfY46D-478E7ldbRW6DNn_za-tzHSt_O_FiMMznwsGxbRQHTZCHi_pPWmYNMeibI9h4A22Ftgduq8R5mYALnb-vGQVhQgi2VLtYlbCo3Y2ZXsWDe0vfCDO2kTOdNPI-I26zgABmcze3VZFK_un3SI4D3lTJ3Ntw2oGjmUgkt2Yt1tBLMtKTTvIfNTh6UCzPOtW_BmIuKGF_AWOw4s9AA-Qcxun66I7fBsF5Jv8Bm2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=vOC4oXLMRkzlG81J6WNv17dDkTWQlOFkuV1Okz7v3jN9QvBvduEaptPDGZLb983wqDpGjDUuH7g1UjinhF4URt6nhT9Ocb3LFtPoTuUbrCIZRL_j-elKYx-AjazhpU1MLKmKQw3oXKoWKErcbF7iY_XzGCkhcxraHjWnOeEXny6AX9pRBtajFxP2CYB-Am6J1fcTZ01I8xczoU9vlgMmCVsSaG7q-5_yspStLaWXUA9NkomI6pZinpZMfXEN2naljStupXlwZWjKm_wTzyI4cTjeEvfFLhre_lTTEs0QGmG4fMICxg7iSjlV7tjlYu-v2GU9I4jqw9XCW2bdJOqFwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=vOC4oXLMRkzlG81J6WNv17dDkTWQlOFkuV1Okz7v3jN9QvBvduEaptPDGZLb983wqDpGjDUuH7g1UjinhF4URt6nhT9Ocb3LFtPoTuUbrCIZRL_j-elKYx-AjazhpU1MLKmKQw3oXKoWKErcbF7iY_XzGCkhcxraHjWnOeEXny6AX9pRBtajFxP2CYB-Am6J1fcTZ01I8xczoU9vlgMmCVsSaG7q-5_yspStLaWXUA9NkomI6pZinpZMfXEN2naljStupXlwZWjKm_wTzyI4cTjeEvfFLhre_lTTEs0QGmG4fMICxg7iSjlV7tjlYu-v2GU9I4jqw9XCW2bdJOqFwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSOrr7r1RRIHGEgGL6HUvelSR6B2J_JQShiZ4FFclCL2zCsEn6eA76d1xhrAPP7HSMy-xO-CYtEMwiOZy1arL8M2Tb5DrxiZrCN8hQm-pEcmHGDgJMyDoBMowYapvvKJ5F8HdqjWE7N9GMYPgSXRoj5f1-Xq3sSoooGJQZ2VmDDSylq-B1WmYXC3JC5kd_xs9Z_ssc7hI0vtqcYpjsX2GKdBFCcuJXUwlWo7iCvalOE2benLymDJJaH6YXjibsl4wQNTsHIiJarYEHc-gkoh66I1yahc9kG98-6qgCTzoFp80ArnROu8EeO5uu2ltybefoOxiGG5MJwESuJCsc6--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSrCGpofTT31CWAx4h9oEI9UZpTPvQ4YOUVPnwa6g0th0yCqJEdBsxHds1u84__EbpRNrECrhHltslKhmlFW3LQciOr8ad7gbxSpByUEwFkKLDQaCqNPOsKwPYDzhALv0gQmxD2pv73qzFS1O3DdzaAM0TOQbcU2UU3yMQ0yHsK0XuWP354JDoDBVK6ERtXi43dCqdCdKACSvbYz0coKhRUOcAlh_i9OHKP7WrLBFpyRvcOcD6o_ttAF7LmPyuIJxtmPmLvx2xsP7fKoaoWiUzJRC-Um5lWppBeRnV03tP1_AY36QzX_0mDXR_Pe5xC7IJdgz15rAtIWfMy-H8hV6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=nYqMgSbjFBjbGzhNHiZnYgRIuvxBhbGczdIs8B6gDjxVZZI08kjVyMFKPfU5wsKN1Np7HHPRn1HEqDRKJHAnbBZ6JVtibyRzoInF3--bmaLi3ZVWhNMaHvHTh8gisIsjQOxCBVNTiuFLvgwFGCS2zkybT_4k3Cfln8E6lEyfn9ERDrSufkr2QEGRVI5_y-NXs0v5LHk3XX_quc8ibGQpOuQwIc19F4MPisQARWen85WPEmQOUJ82blYGx2JNbVo8lDNjUM8cXNz6YhT9ENPayFLDUQ4wDinXNonfiEFjto8dwVzB3tWm-JElhGTRT2jK5ibQPfg7jLmaEefwSiAM7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=nYqMgSbjFBjbGzhNHiZnYgRIuvxBhbGczdIs8B6gDjxVZZI08kjVyMFKPfU5wsKN1Np7HHPRn1HEqDRKJHAnbBZ6JVtibyRzoInF3--bmaLi3ZVWhNMaHvHTh8gisIsjQOxCBVNTiuFLvgwFGCS2zkybT_4k3Cfln8E6lEyfn9ERDrSufkr2QEGRVI5_y-NXs0v5LHk3XX_quc8ibGQpOuQwIc19F4MPisQARWen85WPEmQOUJ82blYGx2JNbVo8lDNjUM8cXNz6YhT9ENPayFLDUQ4wDinXNonfiEFjto8dwVzB3tWm-JElhGTRT2jK5ibQPfg7jLmaEefwSiAM7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oiw3FJfo8w6LvUIzSi14i1CprU8Mz-JDiE7YwPOwHeoyEBgJ0S1p1yd888oqouVZYxA7iBs2_-AIlCac1F00kut2bdadelivIhu8Fl-oBnG-Wu3hDt9km-WZNE3ADVarZP9N8G54wXj4JXPbC19RLdyOtXpFOK80DTfTFV0NyEI1YhsF-FESsZJCXLiQLfZEx6ZvOQ5W0bsghxUBxs-Oj6qybXlqhq8cofq6vf0enIzM1oShI6evXD43zCMYkiho_ua4ZiVkl7o5QQu6n2NXtEzY_2zJMT8hdREOg7YmdTZ0F_8R8k7rSEIn4DLsG8YGpweTnE6DKghpbwk0FFrj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoMM7CvoQNa3VNriZhqatu6WigA2sUTt4yXTZPW-po_HYJGoJ22j40yX9BWwnASvCHYP0TwHZOhI5EbjhYJNVK4hKb5saTOLlXugT8-1N7pzed-743PJwNqgiKlq-V2xrfw61jaVhNcOODx3oQ6MH0WkOGZqkvaBPz2sW902AvakowBt1nxCJ-YUn7zCgNZNAKD_hjI-Cx_5y_jghBMzyM0bY7vHMm-dyvoJ-0Lhtxx0WTrw3Ry47hRdxudlt4-7ZXgvFZfAtHwVIS035cuyPfkCqHx-WWCh5BZmviFfRLCFPkf9rihe2E-RK_wRO0e6SqEP5at8JH3pEjCJG6yRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMH7sAXjs4IuZHrEXR_5CC-a8QrP9hatpNSXxszsuw1S7N1PvQqE5zymSiwcT49I64r-jGEbbOy-IItb4LAtY_RMzlknQ4xBQQNr8HM_-EPGK-wbdnaYdrDij56T-WbLh03-1dhwEoUxZVeMAEFZFZ1bbsF_uS9SOSesv2HZk58mM7lxs0WJLf-0wYYnjDt9KDWMFN8PJ1e2FV-Wg4halTIqdJ2WLkH_3DDQc3p2eAt3hxnB7LLzsY_7MTBZm7GpU72uXsg02JlkD6zvXc-t3VEQMkw4bHqXcZRgZTkN5rykt9uSQQgW6RzyGXXbPi3bC0nKUDmPy91EIre0Xh-7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnm2pxkRHBNpSYiU_bTog9JOTEw4_btxFmn4Nlcu7l9pMGP7ox6OllpgseYPpp1tCfsHcyX1uXJ5W7jnGFeTxfyYqLvHxbcInRXTrUGJRxr5mg1SWBGIl-MKGssxQUK-YjKOz6VeTvBgnnEQc318Qy4oAJH1ul1_Fhp-dJfc9S_WW6gC2oRsERVViL3fcuhNRWIfGyzeayjRydh34DpbhyKd8LaqHX9xmNdFUvBvLig_d7jtHY_uJlgeVysbBsbBZIErHOp9-a9dr1Nc_-ahTSvDuEK_OIDZktIPO-OTyu1Bb_25_eW197wEOYKcipOjmdnaljKmgFTzmoqKocOpyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vhvl5seLTnUbY24cG58Mm4U2QJ7E23H2hBI-oW9welNzKJcllnY_uVRvIZJ2bnRUGAIbwkJM1yycJx72rdj7TBMbC2A_h60l0YpFX3-UhUDlFZ4C4mAt9WSdD0Sv54y0DysB4vrB45PPVn1WwLDcImfwh4Xn8yTqowHI2g8UhNuOwTL5Xb-KPm19-Ox6IGkFS_nT5HuFV21C34SV2uExuQoh91dPVYfu-GkYKCQfImqiLOQCtCMphD3vMWWpL8JRfwexx_1TZlv7q79vhuH2wXH8cu0pogjF3xyksFrhA-aTSPXu78nn9u5V_w33dLUhs0Jj-jTxZ-v06lcfIzxaPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSPkTZE8XhjrenIUx5sugafYeyY7foK0cYkDIWT27ga-rf_KqbwaUPtkbS30Qgk5TTGqDlgevbWc-HXg_1BR-y48bUuJ6Ll7iIMujfd_v1MMIyEmfoCcx1OgjaZCmZoDGhnFFZBIAK0ibj_cu9ta7ObYgZuccIxA6BGbV25civqpowkunw20IgZoL8llQYouSaWY5nfw2W0BmjQ8JhYShFOfF5E6WID_ww4BkKFROAb6XDpO6EWb7I4KmX-aXw8-GC_sDdbRL_K7C8-yiftzMwZtfpHtbLeLjbtDbLCkQaRBDEAp8BjJ7hiBMlGF0kfvhdxW4Yy3yO42kzB14q8Yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNmIoHSNUjUdl-Vq6nfVLpB2y5MvAgjjyfG2Fqog-Ew6XTXCdpBBkFXcSR_GZSWJ8aURCqMrNx1sW6Htvtt0UC4FSF36xjGfICqkk6VhyhytDh7pUatLu01tejY6HrC21qBLFnTs9-9pKeaW_DZ4x3zSL6cJ4ueB9Y2d88oY7tRbV6U4d_LKPIeTO7Om_n162XdpEVuuIPU_EHgU8o2yAaXUjZnaSsy2jvf88ifyvxziGxEWuqGXGqacor50edAC8ubV6An__9Zox3s6cWq5CwVTWSGr-9UJkX481Uj8BhCBUvVcS6oRw76fwft4EXXkqoLBlSId8JoZo3UrEcPRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbkj9_p58UGJX3tBK4EPv_L-_Sbq7tukqNaOxPAP7Cmt7XPA8i8uQbLLnlHnTNAUZG3roU9W0_kYd953KQSkVZVHucY9f1u69MUK5xWltisidn6bT_yjEnRUjtaJFIYT7kUFn9OcC3xRVcc7aJ1w0BbYAgYTgkw65pWZJrV4QOTwkkORfZGZ2_A4Jss1sOvsuzJ6yWcfkh0yrt6Fhutml_5YW8gsUGXzvq5KNT78aAhHvAlphkpMuGliVGv2j_mdiNI6verYKKTGAw97nc5tVyNhZD1hBKMflp62FUaCZuy01lNyGpiNAnw13bX3Sm3O4S0kF6ybirhlyHBAMVd8WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSuS5fSUJJpwlkl3QAeKmsuAk8Lua3dEy6oEtXQ3gZQYJmsqcllwtOG3qZIHnBYOeB-niyaHFl1IqIjIBZ0nuitbyPm-0xYshqENT9okRJOvEXTzaquNNOsZTdGOkuiC7ldLUhGnN9zoVDGMyeUbtnNrYN0UvvNvFbj_tdr_POXhXfHo5sMJKPgm1yHSw5xAk2f24O8p95tBlVryXNP2UA3C7G7y0O5y2ixJXZiGi1eJ71WdJyB_7NpCFzWmSkYZFIEguOXwfVUYDtZuGQ4ilzMKfYcI8BFehjuJ7P27NdkvQ0c04lqtO6qNRcjEnDcJSY9ozvff7Nw8GtyaoMPE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFK79yabQA6RD5mxHsK8y-5qsxaBOaQos5s9VZoNIgS5VXfnl6AYOPrIDk1tbth_p0-NFj6Z0yPzKn_Lk0NCQsJSRdw1nJ_aQFInPonU3jShcsK-qBN9kazSA0uOoHAkAC3xfbo3didNn3e-Gj3FeriEr_1jkPhsQtD07gc28Vx3ELtQlYI5y8_UcMcQ-YBZ9VUi0Ja3jVkEI8ejAB5D4Rnq82ud-IV9yVVNRsw-a5TnuSBQA7-EG5_WR7i9dIz9szpnX_s_1LBP2RsYlWtMA3XNgGvpLemU-_I4UKanT7cOqafEAzXMfCxbkcqDDEYM0IAo3ktk4k_IATX5vONqgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Wb_uS7rfkSP0biKPmEre17RqgUNhuebMB0LX2lX8r7Ez8r5k9KJdxHyOodIgt0KssgYpMzDZzMkLQLyrqJpeZN9bmdPjmSuwqKIb15JIpis6hlPaWUFq719xpuUuIFRFwAwOhobv8C6bFkWnbZq4SF_VNrPvKK8kGu-laNUB0ymD-SAN-kDFTzA4ABoAQ5o_3_ocLd1tkgunDs77yZo9DMo2kXWaU_7V-VIXHs5G0f57W7pd5xH8gAalyWu0OE5_HUMeqPIou7ll3LgKxBBTCoW_yuZnG6Xy2O0h-KConJ75DWesMczopBX0KZ8TkNUNkpq5KImBSXbO0s67U2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNopazo-uLf1gHjrgq17RVdd-EpnzVhLvmMXrzTNpr-R8pERiVVAVjag-hsxzuiM4IKaDfKVnABqTcvq_TxppVPBJ-UCPKMT4tqN6c5jct2SZjwN0Bz5WN0-exXIEvmhuFUN-6DEdyh0P4UprzWYp3U5YZS_3IJEb-w-U3bKyY1CFcmBniw7sOyvihl2_jPPYfvfk-fcRddLFK7wGa8PeHJ2FVoE4vwN5Z8nmKaxaBgDf7zmhds6fEX0v7L6Gic6ffrkDJlq3BNeJpa6xMse--p8ilRJlyHhEeUh5QnzcslHiIP6eWDuiMjfX_jWTpautdZD6EClbdoccwwD26wNrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRYmZJSGO7zM9-GvjVIvxZFLbvrTiesEpQxVe0LqerxfKCdHtPFe6rVTt8LZTUpmc4KUsuUR3rcR47p2F7xG7KdPR3-1D784t3MVyaqywlrSOR-RWGPfEOgphfvoQ9uvv5fQukeJxuptfkEgzufpAHVdhDeTHqqyxJXKAUx514EdLMl4fDol1jQEW5-aKEjgkWfXao7qHQOSVrSFXF98lYCmEJ3nOC8G30OmE26mHlIRLkvgNi5lM-xffGCROUKdngFn4KMxnufnkADXE92M0VUh9wVJXUX_RFXhiQZTTjWnyXbzxI6uqnqSN5dAszblWOIELW1R7Cyu_07eOpshHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIiDE8QxWStJBl-rrcT0Nk8-2JfTJsE0-zPfvwqfE5jN9xRO0tD5Sj9fXvyCsTuyQvJ72NHKl1v-L9RVfRhBWkG2G650zDtH7wfDHaRzFLWWXObPmhXj3s5wS7LAiJibtsUe_Ce5Ov_z5UJmGXK853tfv2M6MVw2jhHc50ODkFY6M3g1--U_T81ce0c6FUDGBLtlXuMdrtZ56zcNEUYGiHpyOtU50dTv70nyI6s33bPuN3bu9cz2UmozHEPwuGcq38vBORh7tHk5jGiCQvIgSrQXfW7WJoCSJ9MAujH30_FuHbT_4je8TETw56uRU599IyCqipnb5TpUKgHZmNu7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYaQi1pvg7OhlEMNuOyDvH-blkQx5npU0ItH9jSpE4JHmJr6Oc4FmCQmi9bMjqhmd8hTRLqvoQ9GtjX7pQwf0Z_ca71RdV9p4zejhB2iBcX4UJXJAhqkv4hElbllYsgAAertGQqaJ2wk5MpdnZu5BcAbZ1deWdD8BdbL6eHdriaoHuRShmOPp6PqoKci7DiB809sQtUaEyqRD5s7DfYTKzM1PX93GThiLpPUCDKDyuhZwelG5_5IjLT4wvxik5XrqBd8e8OI9mkVHpu4ELqFnKedWjMUNeCzby8psN95HEsPs9Vbo2tN7J8bHTBfGrEDkEBCWGZVCmZf3oBOUNp4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/litm_NOozDFvkhSM-oACEuOZolLxPE9UKNClFXmgTeyN5PChW38kQEP6FJnJDdn_Yt_24FwNiAOMis70m_yMrS5Zif6LQt7YNDCeN1e6F7KcYw6PIuBOncfQSH1lun3wDJ3onQ8vbXjU3UrgFlWwOexq3JmiwoAM7_bAnZg7txU9vcAX4ieXSyZelQy_w_I0IOLBhSdnXhD4T0FuV_ycaTSEtTVyQe4Va_kTpnSMcoJtOIEycAzLBVotSdsy8nuC-Ym3p_Z73sfKp_wqjSanUCFPUfGSgz2K7Q9W9JpUmXmkYKyzGk1xmSEpABe6RasYwqZPnat5Zppnt9NDKTwP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo83CCZkWl5-TW574Z5m0G71qStgJWuKOc677Q7CHTJTqivFXPhkhwJeByzO7lzl6W0gnpJEIsqGE2M4vkCSLbRewSs15NyvOUOyIjZoLRFSMcHftwyziKv0u_eF97wkxmWl4rkAl_BkObRQAAuEkk9EPu-PYK3bd_cee_l36-VjnP1gNmbXSuyKZq81SucbkYdKPa897kqsHlXi9PVF4-md7trUd9SZ7_WmljOgvLxUuNlF33xH13JQqNexTqmSDQ7Fwo0OcVEKpxQV_Sui_bc7G-qHzDBpice4nN94MAhJ6ANdyHOpPrKXWZT9iULIYIMkplPoHhNzLWMuV3n2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXnRQa8z_zf5wljRJfTZQLAPp5nPEoJEq6lzIR-8ccGEqCu901_4C7zDM5PhjArXWNFzWQLnqE2oN-14R6PSgyEQfcj1WT83yRnimlogL1e9P6mhFzg25wZu02e-V6dZ9PieWtQICixAkueku3Cng3UpJLp9c7riiJOWkIWf2ssd7GFiJ2xLJYKsJzAWfFP_kEdhot-aLIjxgv33ndkt2BF3t6zKcE3cPAOkWB_yokfw3PB9yCvNlM5JgSiFAlBU_o2v8qFBZhHrfMSIAQPXiGKBbx2DdY-liH1myuLqmKt4NU_ljOyKlShGiF3L8w9kOd6AhOkZFtZyUM2V3xaNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIN97lhDzLaVQZNJ460Et9SE_6aGZ9zQNdGM0wi1OEDZuNYb58pTCt53mwso22qhF6nh7ErXlq-ZWLKN_aXLgd7uVUm8H059xs49fkMr5h4Usm-8YXgMDBv0qPv4xoGCGhpCno7jzQSnkBYiNx4N_MSIN9mnYouY_DJtnIjEzX8hvOxwzCtZQLDuS12x19GJEl-ZMMbzWst9NZfqtvrqIvv-vqhASYw6osqyw5GFRCIQA6eZIP4SueFdUOkUoB1Pm1Tb_x3QfsLuP5y2Aj2Q9jxdqjU-IBTy55vk8sXvUxg3FDhQ9_NPFr6baU7wr8scwvK_5k0Pss7XoBTisRRY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdtFyHaZa9WBVM7RxUSC6kTcSCGNo8NfSsKobWIEj79vYWrRQM1XwWXOB_OdZuQC7NZomrudco6Q6bk9plLmPjQEe9_vbDuGwNxYDKthbjN1qtFSg0A53b4XS7JpC41Qm3eZKltDMaehL3rw-SvNdMP-TXJYAhRAR8e0s5LtuMpgjwxWFGn9_7x-lvwk9F5U0kbeJQUtHIgViqXiTY6b9nq8g_tMqxaw-VvO8w1nZ-cX_OnHCpvkqEcI4GBsj5iPsep2z6D_9je9iQFqrXOAMRAMGAdrzHY4phR0wWOEnNANNXDNefQxelCEgDOmHz7WeOJLm74QGl1b-UD9SDzJAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
