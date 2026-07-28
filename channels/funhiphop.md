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
<img src="https://cdn4.telesco.pe/file/GIS2peHtcf3msVut9FVfG1zY-UA2LjTa6JUZ1qV5tpXrEH5oqAFPEr-WMc5a7fBKGnYcwq2Y7Js2XcycUHWxmJ2pqg_qb7rwD2xjiiv3DDN-t4qMNYxcg172yxPQNYvQaAW62DtrFFuE7agDaFIkVr89Y5gXHD7I5almKt0FibHz_mB0wt0NVYt3ejNVDeHtOvKN376o9KEVmreOMjcJ_OnbZphqYtI3bfNIIEENlngi_LljvhMxhZoKMMXsEc7FMgDZilzsYt-AluJtyh0Gtsp-wqSF6DF9DsYKFNWIYG3vzqy1dXqluakcQ6yvHzqgWQwVJm9y_21S28uKfSohWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 209K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 03:26:08</div>
<hr>

<div class="tg-post" id="msg-81393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ظاهراً اینترنت اصفهان روبه قطعیه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/81393" target="_blank">📅 03:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=YorEUwtUbEwhPzl9pZ0_6sE3ZR3018TRJAWGRA4dxw9t8WPk_VH_nzx36b3HR4ZmiWUuG856JL_2PHdVLIniEnFrmApjAX54Fa3wfxAZbNnf3f5kJceiXeSULuQRw57d88RnXLmOVKlTHKaUCJLGC5tM2K6jgbrr_xOuG3TExympIxdljKL9g0tFQnR6BOVdijytFuyyRvcmRF0CsR-cRsp5s0yl33mC9PAq4YgEA6fwy08gbLC2orMXutp6rLE5UgYAX0AzsJOXpodyz3J8dvkEY5T9xx6mPKTdvtjxYqSxCIdYjOINeRFkviOUXSb6rOpRPKFSnCSiPVxixP1oNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81391">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ای کاش هیچوقت اذان پخش نشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/81391" target="_blank">📅 03:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=Qtrvv9vzT14GcIyX-Tp2etepsSR1p_iGK4rXyZ7XwDbywPR0OjBaTsLdi4c-b6uK8T6LE3pGAN90Ht6RawnFs9QQmPqQ11LaHOI9w3M5MH224jGNEtF9OhPMAMnjr9-FnHbC_KcWgOxNlRS3ruL1rLHeX3SK5tYwGntlQeLT5E-P0QWwuPgJSeXWDpphEJqdIuuzIJIJeFjOgchQUz9ysbrPJKz-LYGA0RDm1GnAAVFkexqem19G_0iOs5sxx9pdnvt3ILSnjuWUvXsvEanFGlHKDZTsRbrtSFnRA7OJ0zTJ6pKTqg91UXnwnwYWcrF0P8AR1mLs58TjixEv0f3kSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=Qtrvv9vzT14GcIyX-Tp2etepsSR1p_iGK4rXyZ7XwDbywPR0OjBaTsLdi4c-b6uK8T6LE3pGAN90Ht6RawnFs9QQmPqQ11LaHOI9w3M5MH224jGNEtF9OhPMAMnjr9-FnHbC_KcWgOxNlRS3ruL1rLHeX3SK5tYwGntlQeLT5E-P0QWwuPgJSeXWDpphEJqdIuuzIJIJeFjOgchQUz9ysbrPJKz-LYGA0RDm1GnAAVFkexqem19G_0iOs5sxx9pdnvt3ILSnjuWUvXsvEanFGlHKDZTsRbrtSFnRA7OJ0zTJ6pKTqg91UXnwnwYWcrF0P8AR1mLs58TjixEv0f3kSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5PeCruKyVXv5uvnHfP7XNi78XXQG3ivmgwsqi3UcseBaX5XAk-4j6donn5NAyf8pl1MLGIpZxn4r9MMDJTSKnO2eW2NOvzVu9C-6FbhBz70fiSaM66UGCmRLIj_JH5VYmyj0IovRfEw42I34p_izEf21wHeCFGt1KGmkNr0Dp7Ao6RI7YGU_Hd1qYmT-jVMHyWw74BEZWXyTEy3rEcZprdmrqf5OcObBW3SCLm15Uly-p_IwImrc8qdWMmLkXAgeq8S7iwQW7_tqkVWT7jyhV-Lfr-F_ae8ZhGgeMF27gqLrYlKvt7dib6dHWM8EbUZ26ZlOn3BeJPUIgmQQuZnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv1SNoDbktn05KN-JOe8FOyykdIWxbhRX2cwNgVzOeEH-CCulPXmBnpKHQrjM2Sqbxb4VoHv8b9YZFibJR5Orlq_dTaJ-4oh7DqCnNsdx4Lv1JiVS-rQNzuaV-5KIxSg9ibXI4EimaAxT5yFbxr1vXofcyBaV1nVLEUrHc6PvYfuIUYQD7z6SSaFHOk4t3GtMm9cYEA9ABKpREEtgWuPVhZ06m_rrmGRMxN0jzr5FmEtEQfoKn-szRE2fQa84ZIZyzUPCLgoWTgyEVeEEmdBdhtrJjW2gq4yjfHHWyZa-XVe9BuBagipxD4lnPWWj5yAe8O0HIDnqADS1ABrbIx1bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCkLV9TcPp5vql1qyrNNXiMBeL5Ol0ljLaImrRioGyoq6xyXUZaVamxPTzz-3kHYNwX1LxzLA62vkpsqLJ1HpI36DxmZCBRUz37P7D4qh9qjWuU6TFs_77OBAcQ2ZNC2Vggx7ymBN8O5fPIEzXjTViKHcUcVr9sv4zKXkGGxMVeVa9fxnPxeUyjiWUcwQPjRcwBPfsjAqHJ6XmXOIgzI4AQd7TjrdNEkLwq7VRWORAZ8Wmk5WX_PTp-93TKJfc9Wr4iR80tcyxm8W3YeMlnhM-wOXhY0yiwPfr38FuCpV2K0V7tDMMMAYHwWiw_xUyiU6H_eFLSVEgnWzzPvPLK58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81383">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hd7wZFJLt73QGgZOc_f-lPIbiEOnE4rIbIHAWc8BX_0YERU4mO-0cL2dtxyhiMPZwUhJtKMZNg-9nR0lul_ZxkT7tPitVsWc892-LCEnYfAzeI8DPGmVkMtkq0rvhfcAFAEUHWOGBKupj53ZwbuPyxD-STQ7SGfDK5Cuu3fFURVb6TV2_8jkWvAfX2d3CCWH5hsoAkhzbgGMuTnDkfex22HVOqimqiJXxmMhcNTmcSFIbBxLlNUXTOZBNEpQUr5sadBQlTYsiBp0EL4_K9aXOKI2vuXXVXenIe-crNRa4rwdndTbgtFE6aIUFn3e9KzXn5AGlrFRAtnuB1HggD945w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این دوس دختر علی سورناس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81383" target="_blank">📅 00:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81382">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw5ecBgLrWCy-GemSG6xX-haqfH2hYztd_V2mB0klwk29CSzyBaRgL4Gqk1emMikUwQqGQQmMuGKeBwrTMVMYEmp2LVlP3Wi3s5rDPhclCGFEjRk0d5QxSSEUA0kZPXPeuqv2qMi7EKjkGHoCFHNQP2oegC5X65va3qlX5nyttJ4YeNBuoGN8MwCfgHdL7ZyIhlSoPy86ETGSoq1jHPRUmsDy571zaLGLHD8Mbv4Ngn7rbs5b_5ViRdRuHM0AHKo0oDM4Jq9YPyg19DYVirlrFWKZySo0v9zBNqjknTZRfReV-PrjJNHxEdlj43VSa-b31__uPzLDUrMxD3ag_QpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری، از معترضین دی ماه در اصفهان، متاسفانه فردا قراره در ملأ عام اجرا شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81382" target="_blank">📅 00:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUYk1-iA6PgIu7NL-lweGzs274WOU_B7hKO7KWOgO2-VJAqXJUmhn7LJqm8bWwgwq1Wv_zz-4-EcuSsNKx0PdCPvEfssYzCStvhdZJFkX4L4w-uWIPN5dXOBlIhLKj2jONpGy6FqUZ1JZkt8CcRdYRKzZyYgj__1dGSQ4ObB4sYjD5soPvo-fQ3kzsQwqwL1Bx65ns4trDus81AsYZT7d_bfw5_arf53SyhQGR1eEoRBfAEjYeooIUNdRN7BCr5WVr9Sc6clnV1wP7FYD18K0cg8KSmsqKFE0mt4WfIRDqN2797AQNt1erTHEd-dM-ymYgyopiWN6_h2Nr-kROwEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81381" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBHHDdN_5VwmAbAr_DY64TYPzwjFRg9UhDCcdyzeDijdmNY3vfONSl70Mbv5eGfh6QP_r2loLV562riroKNBhlB2ljWrwnVhVncNAv6CK7CF7-LTL3c1HUy7_-i5yC6RDuCjN_nh_N3zeY3unfZaNgJZ8UahkzYo3Oiaw0OLGy4EQSjhyoCXcbsCh2KJ5CkCQaE1S245cRBMAd6oucav3Hzb_SGV5Xu1Aliaj7k8gLMMF1SZrmmMQkLnONhkSQmjXqCJgIyvFSJsLpTGw5_T5ShldKMeXgwiKogUFesGN2R3NvbVaCvr107IaY0NdCm4eUw9ufjUHywwFs30670Y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراد ویسی بالا باش داداش کلی تحلیلِ نکرده داریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81380" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obiQj-2lqrXnzIxcFkvCJTg-1fxrrMZiCPQDbspxgRoSA8pLd7uSUqQClHLzT_Sjj8oBJ94qeQ0Lo_8iJUPJb0SKXIq6wTRdlJbbB-_92wcoq9yDVr563PcK5Z_5liLA2iCNrdLQiw2dbbl-sBOWVMAFCLE02FjK9zX6KiAEk-W-A_t0kMG8RehKchIg-VyUKi2fJFgQeMiMOKc8UQuARcU1KvD606qmJGoWLLwj8an2omUOIgTqv9aqvSt0a-ZzjWSIMAr-NKsw_Ff_V0g9PqIphCXXKpR-DuAeegbHuU13zasB9kEw8CWrOoRgNnuCfpOeWQLaS7e_Ox-YOTMJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید فرزاد قدیمی به نام زل منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81379" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81378" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81377">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udni4PlaImHCDL9IFGwv7_1YYiJ3QzB4dhWo8S88XdWIQeWILXJbxdjXCWUYJap81u5imDtbIuWiOw-N7zW4fR2dh1y9bCXBKeEBWr37fy58PfhMmymMaiC4EVSqUu7_2pLDxWq8hj4ueJaTMq0-ppeUE873qSzsjtg1ZO4Mgj60ZeuR3rOGYmIlpXeRIuV5S-yimIUrrGXc0A1P2N644yBiDa4EpFqccgCW8gRGbGgF8LFv1sHtQ074G8iPJnbOwOiKXQrGMMoeaHM04A-ifPOalzrAiaU7WqTXGVWuZEKauRBT7EPj9cGYiVb-xvfZOuikwFXMTIhEq1pDKthpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکا وقتی غیرتی میشن:
Gay rat
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81377" target="_blank">📅 21:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9ZdsZtCq4m3xmvrQuxsp9EuFtlKA6C4_ARCT0Nl-S7UPneNTOym86v3QHz7qz9k0ZmgxIxcxlcFlR91fjOMosDVmxmFRmX5Ssja39cs9yRadpEXxZcYiCBxcWJOLGh1hhAD-g9O5aKZDwQcVZHc7QEmbhXHSUXvV7IBJXnl2s5WLs1RfYgCBSct55EPzaK0pYcdbnDYuRmhaTzWZgm6EUYxJDdwIvhM3I-M9e1f1WwNtr7iMTaXpNANv5FLVgJGr_PimhYNaX-MI8vctA8f4xnf0EQExMlnoG1o2XghQMHXbItX48NTqjXL20RBhWcWGDoSoInV38EeRJxObNWgPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81376" target="_blank">📅 21:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciS4YdJXbGuWDzD5ZyL0-q01v2wdIDGMCfYFNxw1rFJFecEZzNBQHoYiiPBmgEqRI7_cdhGMwiyaNQRyRhp3fG6KMJhmPgSM7_cneEANL60z1IcfuA98D9LpljOib_70V9-ZQl_Es9N4ZkqUq1NY8Mm9KOtdowZ7fCddvoZ1PL6aJ5ApPGlDMW9JamyLiNeHldW32ncfiZ6jCLcdgxW6Cn5KaGHZxD4YXLxXqTKmXDQ7FeIfWTmQGuAz50Xc42Or0By1P1ZracRqXx42bOoe1MxTkOumZutMjlewBpT61DPB0LFIRxv5TtDg65LhXDdf2V8o1cyP7vOi0EsJnCZZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81375" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWl2ydOqvsGxPofN9Kmm-qbsHdoIkJTIcbXbOoqWne2TB09WQ5AwaIQZhC0W4172-pbcsVRNdtZW5sNt1qEKQQuhCNFYZzQcBNBEtKGdDOIR8LbqFbICXKEgJMogDdZwg9MhjFL7q7ac149PUQGjSeH5SWPdoj92oNW8gTyBRZxEcGXqKFpU6A7oLIKeHsL04T7x6PohWEzr-UMM-PhvCc0afpZNDLsZRuUg6Oq4td97tuQi1tB-0I4gaCAzESfeJntvlCQ3GgUC_Z8N7h-bXLKPHfBzAY_53jyDJAHPkAHZ-VArg4a6g_HtpRC6kiJJG5xs9PDnuZmDjekV0dIHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته تابلو توی عکسو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81374" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKVmcMAopjdnljZhl4s2F2zr13mEoV9HZvT_SWqi50v-biLT4om8_9jL3MmoTBm2SEPUGjwDPkYfInYBaKJglC-iXApQzlfN3GiRX_RQ1_c-0l-zKRwanASRk0WduLdKbGe4f1z4kWcrxBVDypdgjuqvJ9MZUe4T3aQl-C8ZvaFknqsjjOurOzlntyTfeNH8JdW34izHIfhkW6F2t6Ma3zUYbD3r8TxTR7joFJzwGlX4Df3ruWCtAsH84c-WbfPYyQpbKfCCbTfjSTQ2oyaeBNeIorYnHFe7Jv_0XGJ5z4rdpAZn5opD6VU0o-NOzJwQO29h90dbSntL_JP74nv8mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پسر
خلاصه‌ی مصاحبه‌ی جدید ترامپ تو هواپیما که همین الان پخش شده
عجب حرفایی زده کولاک کرده این بشر
👏🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81373" target="_blank">📅 20:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7zRwTARC8J1ygNIdAG-bF4J5wJeMdlD2jFlxzFy7e6aYAH3DJUFCOjgWkOQSV9mdVUNikMYJZgHvtjvSTlGJF8H-iDgC9hPdqd9gmB9bYlgKsSjKCxPd0s1Fm6Aw47JltGAeeZMWAZ3lHwJj3W02yDPuE2ZdM0-aabSIXPFo2z5AYrRBSSdywa_M0kwtAt7UYjo6T9IzeQshT0WG7BTGzai8pGJl5IF0HB95keVeTNTierRH9AH-rZOYpZnRZDW4VLwpNDMU8KHxtyaI0-LYitOtBXTqdJTKEOt125Yty9oQ9hEXM3zSAOAsHMecQ0xNg29_CtFappj1QzC-dhGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81372" target="_blank">📅 20:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">خ
دونالد ترام به شبکه‌ی ۱۲ اسرائیل گفت که آمریکا درحال حاضر «گفت‌وگوهای بسیار عمیقی» را با ایران انجام می‌دهد، اما اگر این گفتگوها موفقیت‌آمیز نباشند، ما به اقدامات نظامی بسیار قوی بازخواهیم گشت.
زمان زیادی به دیپلماسی نمی‌دهم؛ یا این روند به سرعت پیش خواهد رفت و تنگه باز خواهد شد، یا اصلاً اتفاق نخواهد افتاد.
تصمیم به توقف حملات آمریکا گرفته‌ام، زیرا همه کسانی که در مذاکرات با ایران دخیل هستند، به من گفتند: "خواهش می‌کنیم شلیک نکن."
ایرانی‌ها شدیدا می‌خواهند به یک توافق برسند و با توقف حملات موافقت کردم، زیرا هیچ چیز برای به دست آوردن و هیچ چیز برای از دست دادن وجود نداشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81371" target="_blank">📅 18:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dylM9x1moJakiwRpoVgQallw9R6bUIA5lFrgA4Q57pDHn3UWD8jcF6ZrbX2tMWlB1OlJi7yAfvtJRTiwQNlz5SM9tHXQP0KmqQLIqq_lmOHtABgd_CSYZolZPUec9_ZXPwsJnsGafqBg5xQqZasGZc9HTPvTUnOCJp7RxOBD3mAx-tZsxLMoS9HlOffdtPeb_VsBDr03nOiLys1C_jz1SNh50ujctVGcr04iWbtq8x6qsFO90g88VvC6rHE__Opmjoy7Ot4durQrtEcFOPcGQ6r3XGj-4uTGq1Y3-r8LT3Qq9wHtsqcoJB2x0S9P0aMxwTmfDHIr1vwwOBAluftDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندروتیت
دوباره به جرم تجاوز به کودکان، پورنوگرافی، قتل، قاچاق اعضای بدن در میامی
دستگیر
و راهی
زندان
شد تا بهش بگن کصمادرش چه رنگیه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81370" target="_blank">📅 18:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okUspBLii1RcUEDHGWVQwz9VQa4TuG7UVeMvKY5NwoDw9mGwQl7IDd-ZHsei0s2mWlwtve92UbLVcysHy5I5aiH5TQkWlChMEGt4ZCJo3UAKORoOOxbrUJ3CxHuKDnct61U8cC6SCCftR67rKYrzrUnaFjaZmvnwT2t7rh4bKzkwS01GPz-CaPZy6q9xqLvzHMJGKcxfJlFWSS4TtZ26ueEIzbFXAd2XujEwL3nj0qYxPOeNIIIyCaYL0noxWXun3StlOWb56MEVd16HZIijbD1vtAY3zWZDPFpo2CqINy9_Ojw5sBbtkAUkKkL33W0FNqU-In8Dobjh4t3FhUkrVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTEgOz6k7hkDaIC5UjvMowDjZl_jjH_2SqC30RnwgSkowoJ1cXy5_YW22MjqbL1X3JasZVEC_ngQK3-xvEem9ATei9l6Xb2egFIjYC-DLXnMlXNNM5KD4KnBsdboUs_v1gm6vRyUbcg97F_rnFu9paaN267L4hrBRghdEFW-CdyUhRZnwV1LxJQrcpDd2ldgzHNi73h4Rqh5oT9MZTPgtVZToBKqHnpYYHkQdamagIAqk7yqJkbfUuK7AtOwMD1fk666JfX9vKv_1gKgm3otkx_N07iFAgnDSEd8k78Ve1Kz5pbuzzrbYUHM07oC-IdMhOKabLEPqjRKn_FeY4afnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رومرو درحال رقابت با صدفه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81368" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULSaJz_di_4on6BMnvE3fMfAohPqeDAKUbM6zCNVaOnQbLE6Vazl3shD74EP3vXHmm4s1NA1cXlZa4jvJZOMNb980cL3LC_FN5RcoJOKIaMQoMmTxx2xwVMiE4IkHgPvPkTPEAI7sL-cO9dx_aMERXBdFKjSehKVrd5zNabPZ0Ow9gl9KQUNKJxFPeTTYsm495yd2VZWnsbqu0Tu2Ec4eqsZ_1AgKcNTRzMNv0WYzhuAro0C2ABe1yo8vlNIuAOPjWUt3pq2Ihh3nwUZXAlMsLjjwQiRZ4f3gLmFUXrPK3y_Qal8fWADh5b-RGHMeog9SNidM7n1FRdBjSbCGb02Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81367" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل :
بنیامین نتانیاهو با چندین پیام مشخص در دیدار با دونالد ترامپ حاضر شده و قصد دارد تأکید کند که جمهوری اسلامی، به‌عنوان یک هدف راهبردی در آینده، باید از میان برداشته شود؛ زیرا آن را منشأ شرارت در جهان می‌داند.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81366" target="_blank">📅 18:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=cOmy6tsbPAx8Sm2hbdPhbUr_WMUaPAH5RK_CP44Ia9f7kD-j_GyBQUBmFQpdssbMoMvOkhD6lW6YJrgziM-W-VQRmJQrC0mkSwufsBOndOhN-bM8TkmVMbGg6VtSkTVGY9_c49t-mWLsM4rhP0NW1T_9lsU5JvtocwPlJ2uRTwOHLqZIsD_1fTo7UOLzkIjyKZ5ST8g4p9-4U8E5_IFWhHOt2STfOltl7meROfhz_aYpHUB_bvQ8Cw5dhTZMwykfrjjPRaFRgw9ID6nkjKVlle4hsrtTNFQ14Hfrh3r8Jzcrt09zFOM_cdFIEmdJa3Nva9sCTRRCV-oxqJ6mJPGIew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69a6c155e.mp4?token=cOmy6tsbPAx8Sm2hbdPhbUr_WMUaPAH5RK_CP44Ia9f7kD-j_GyBQUBmFQpdssbMoMvOkhD6lW6YJrgziM-W-VQRmJQrC0mkSwufsBOndOhN-bM8TkmVMbGg6VtSkTVGY9_c49t-mWLsM4rhP0NW1T_9lsU5JvtocwPlJ2uRTwOHLqZIsD_1fTo7UOLzkIjyKZ5ST8g4p9-4U8E5_IFWhHOt2STfOltl7meROfhz_aYpHUB_bvQ8Cw5dhTZMwykfrjjPRaFRgw9ID6nkjKVlle4hsrtTNFQ14Hfrh3r8Jzcrt09zFOM_cdFIEmdJa3Nva9sCTRRCV-oxqJ6mJPGIew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور:
من فرزند رسانه ملی هستم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81365" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUntBcC4ptxkuVkYG9AwWHDdpHV05cglzJAVa3lednL3VKfwhYgSU2ESUlFr09YWgmOMWSpfJ7_a30PmSVIHZV1mEQj6aVFi-urSiGX0JFfB33Y5RJ6nbdRk8X7of_DhTsi40egJ8DWsLEbPzUUgz0BGk1zKUV0JqApFT2n1LaQv5eUeYn5l1qM2wA0J3JSQs79_74JSmNSM1OYJVaa3WjoV8R9_Rf66bRvN4_uDhR_39zkqj6rxxXrAi1FXL0hDJnNvC9tKgwwczQ4xHwmv5W_6o8X6-XR3iKEbAzX4b0khnQtDKXOjC6femXnM9QyiiayVX4vTyJUR1ht-KcGHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام از این جا سیگاریا برام بخرید لطفا.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81363" target="_blank">📅 16:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUXPVenySKtuG0LqfEcgzP9cmzQ9cHEbJZo93u2SsBgkAH9NRWnOw9O8FxU1AYwFoWIsRUdfdyHqS1X-i45ZkSUEphb_7QXculQbG5_T8ZCL9PmrWrE8CIC5pJosVhBCJmn4JTlvUOaL9jPt7nrLWD7mhow6KosdcWSJQg7HGaPD2JTBzE-eALpdSAvFVo5rV68Pu95BywYuoG26B2UVsAXoVzfOTpLVDQ4LT6UdqXsxURKWi1gJz3kQR2M-Wm_EwVXln7b0FpV2FW2rCXCnEBn2ip-kRlKzt5dQ8ORVdqSPa2wLpRwYgr-7aLwip7ioP2W6uEFZ9SEe-e0BjXkeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AogR8DPCA5m7iruo5WblLix8I4lTAr8fhP7hvhOFd_sKULLvPW8370MLFiBomgCt8mAHh98NqBq8ZTpiVvP4IgSkyF7zBXNReH_6qv0DYWdnbRi1zw-ll5GNvnRV7UxvB_hoFetXWI3TJgDcEe1yp4BtKCIuW-mqr3AMF3tN4GR9_TVtbd3YdUqJQOX_RRdIyCISxvxWhHNfIFYGJDzRTx3g_gtid91NOjfpfj5bXRtF8E0PrmdQjcQRSWWNof8biShqltUM2-gUyayV6qHzYaeKvYk3kk0pbubhXW-b2L7t444KkCrS5Nf4_-7XFDQlK4g-kvilXT2h_1lxwX2YHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwBfMZEBIZMux85j3KMuCsk_JFlua-Pso2P7xwtn4KPWHX-2zBx3g0HKq39wx88MOvU_1aU6fIZ07UjMpP4kZ50xwf0OC4Zvw7uy4ecT2sKPO3Z0zf5Z7pPI-Sdkfr2vXVJAInk7B3KY6cB-lLnrnskKd270RFqxWBxar46lT_ZXYMKF1kZBQEplb0czGAdyq_wP_X8cWi79ciLu4C_2SPkzLxCxhk2yKo89AR9mUBTZci1ZMLJ9jsox98hNOW3WKZoSkbGzkecT2GrWsmiZlBdG7vOhQzXakHjx9H6ZE2m21zCfUxHdflLY22Lf-KWCJzVhxzMgYmu8NpNn223noA.jpg" alt="photo" loading="lazy"/></div>
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
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jifB5CG_aC5Rv2FDqh5aPmoULuQjcQOBwT6Ur-iElIY-03rICagjphsmw-tuRd4QtYUjX6r6oT07hT6ZEUaOr-J0ulelgGMHPJssbPshEt59ena6a24bqs9mQeMYB2_yO4mvsSg6LrapcSAlIX7E4fCV8ZTt21_ehs6I8jkrbsm9PzuRPqN0SKVikoGQmt68tOEjr_h2Wtk6OJ_HBvg4MBCZbQzt0_ZOxVWp8RUfIZ6wQhuOaAhwv3SkY1ImilhDx3gpa_Cd4ezrDvB9JSZkytkNgBsiXH7BkVkAYr5E049wDnTFKI_WaapePzkNzpi1AgemY8pXSGY_e6y1HGer3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdb-85EvJD3DhmGqoJs6T70-zzJTRcnf6rcbrI8fMo75IMVlLUTZowWwVWp6mbo_OSy7fEdALkVTsq1LS7VsJFqiLkoIBEC5D3jM4FvXz5Xk-1AQXDICNBG0YQow8qm-EYZccAyxv-UY9g4hBmN7xRs9TUSEFBnXJcWJCnIKqNcawFtdaaVWrjgBAtwUnqI2aLZgF448a4MqzmYw9PVCQ_GsQY_HhPLoiztvKhRj8FXWiCHYRi3LdZLYzNmv_P7s_EmyYmxIneskVRcnzDrXR7ErQ5h-JUR7yW8309aR6EGdp99aAnqVb6MU2QOkcRpxlmkjWEA6FAMgACvFyRMcIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGoDx1hL51hwwfIajUZmAmssv-CLt9RbJSAa8BcfGoL2ch_ZrnPGHHw9v27UIYmxwIDIn_4yMb2FxCbmlb_O8eKb1yBcgnLpzLPPUj3x45kgwdsJ67OwN7o1jptnUHdobEF8CBnJvhIF2TLGlykUAC0uEyJ42zAMrxZ6bAzrkJg4k4CFWejfX7zjJR3YHbDAd2dsw3o6W5ILA3QBFpolGPVj_N7kbcm-r-xSNoUkPRdQ0V_ekWA1hoYec7T_EiWclJhvjN5G3p1KYZxVR_a7wUbFx4OfInHNBOAQgFcC5WGlu3QVbeH853tE_hY-NQy24TMepTtoXXe0VNoigrzXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRYbhRe_r4zwmzBl3c4ELIt1c8IoDVdKooK4qR_rPctppDAOEVvmmAROBALelLxQ15JLDpYVKCB7eHgORM9YTrfJInmxMxz0qAfG7Kc9cbMwJMnfigr00kqinVFRdLufHIcSWJfyWhXW0tRgQ8KhNnqKCCOxAzqcTUc1jIChN5LBv2rkEO_YfpNNtuspZ90Uy2cSRrDNM2E5DE4IYBFgB6j4IHvBceRJUdFMcedeFPqw1CTHS27Fel0HiLoeUMP_hg9nxwIBOcFolMl873KlmFKcuTWNYLh3ckd3UDiHY2bLixeojMMTHYD0fm0c4MU-sBzcG1kPgm-a8_VHlU4x8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el5m_KeLZKuTw3It4SksB9__dZm19zKj_4QSNZnpw89iKsB3dWDzCmgrR3832gR--f36LRi30yXdMTmHkIVZSF47CxFlEE7tTMMkGxnnKThs1OINDwMTxVJVbqsXotTlxYdWGQbK8UnOXAK3OoTHiQvGetiwJG1AA0LFZY2sGftbtngaI0t1CiluGB67z9aHmlWeD1_Mc4KzUsPCMObG6Iug6OLVdZW4ClOsnviHmw1YM5hHcopivx53Vrw4lUOnE5R3rLG0oH0LRZ6HF6f7IkNfk4pJxY2LdDkv7GuX-zDKjN_-Ome4Cpr7Zg0TYn4YRlx7uVNu0XhxWvZYNc31lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTWTwipLMSlNaKj-0rxYgjwTGpGXaibWfmjnhFP9qTSODK-UT1_DmlQK6gxR7VTaUgT8MW_Zsr6ED6dAZMNfRT7Pd3MruIzZ2qwXBo14cb_YCvGrCoELHYfg5mnHDWrTUGbPHcalLsb4n1LrDKBfNj4ji2MlOu8y6DHLi5zUFDKEXOA2uZyg_l9XeFQ03hknry9-64JWCs_JE6fcLalETwgzJoSeVSyZ5bQ6QiCFSsnho9T8DP_lO33pWu-l5D_N1ebyIFkQ7ALVFItMq00VE35FnyyinuYRMsGTc7Kh_WbL62gXaU1RuLoeynx5Ws72UXVGWa8ihz4ogUiIGozVug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhuIh6o4Lk8QQvkG8Yqb3HDbKSHuXLDgMAio4zfyu5qSzw3JuMT4sNf2feJPJ6m3bWdiGLccBACXWLFHo7T9szNSJriP4f1R-Q3EiiXQZvU95bSMM-H4FV9KdNfhQI9On4jsnAPU1anLGXx6cgDj2Yt-Tow5m2vDyAxHELHY5MCDAyj_WgYBb4jJaMq7LeNIiEZVdhnydjVwAt5QmUzyF-q7gUbv8bawTEiN-a0e3NxpZoMTQm6w6e1FhKohAE2jfCKTzrvgW8rXlQJmcd0pD4jam-_WoaN5vQQOWfGCdX8Cy1yNqCspYCwtT1VYEjLYu_7Xqtw84niE-ANe0g9jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUQojo29Qjyh7goRX43QFrtYe-BhWdCEMI70WeFHYS8yV0E0eo9R17zdzKsMQtP9AnonZmriybdcQIYM7qeXeL4Br57tXMHiXVAsvWY_N4WWRCl6qcLHREWosviBlt_XFJ0O53DDLFI8i14qds5Na-kKWR7btG7P90aMBwaE9fOIMVTBEhDhjE4rgQOv6xCX5k4MpTYy72e0KuCNLPTpPrmxqQSMfywCSbXRn23ZWillfNdrceNHOu-raXqVkE1Zt7mMdova2AoZzg1SdJhR2z1bzW9PCWlX_nSuWGfx9VDckdoKRZVr8T3WmcHhL0Aq-9-VKaOkn111HItnB9MqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dbu8dE87Ipdv32jfnosFDPPlrQooLJOvm510fyLNqJw_kNf-4fCWiL2dfyYbzxlJRfpmd5qFEeOz6XQEH5NBffZKFZC6cprLPEV1UPdRMt1Yf7pniY3BGDWSQhGdw34Ib9egaPHJBmdQ9kEqlrtZ4jPuKt8gkeAxdk697nEiJA7efPC5TOMpfGZk3LfZ7N6qDnMfRL8nxsYDfyyIMU3sP-neswJdl6BeYLYTtyl0ghtMi6v4X8rI-Grrftb_IZv_-h8DA8_YHO-UYfUSXLI3ldcf_P1ToL7rDPypwvtU8NllGPdH349R5a5iTh3H7xwR1Qz--RRkBeGZNXZ7IPfw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=vXvZe8E1wWDJt57FVw6TmOfD227gSf89_Hg15hE6FOJfxovzI5gxBSrckLmJQAlaPYkita2CpJ7BMb4kof1G5RuSodKW9hoRyKvjY6EJJvOAz3YgXFlWop5RvRHRNa_m89hmhMTAiJTOgCPqMrcbo1RsP7oESTxHsFcNp8a1ElzWmPnErwzkrXZlFTrO2CA6R1k3dxpbo2wr9Yee00AHmFKwDGSmN8chqIlLqdRixAz9yc-wYSLjF4Y10jVtX8xe9DGH93w1GE2Y5x6u1EwgYiykqU8gCMjTcWL1K7WbVoDijVhG6xQoHd3vzLMWXxFiiE0cYtO1bXtlLlqGdlNegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7n9IWQHVqb-fZcykEW1RLfZdaGflsUh2IpNM_12OG9IU1v-aMdzsL30XWsfdNNvq4WffiMewIsbpL9eemnAuWMEWQJdEvZMR7gAxqtMpc3KKMJ-CX_kPaFziyoqwbG626fW-4GapEOcTw3NxvcEbDssuKN0KO8q8e9oEwXX3g2ou8BrxK2r8VR3rBQ7l15Acg-aBG5vRQVHm9qHnNcS8YenEtbXbWH3lkva4scisE0nOVV6tAEzVtYTY7HqeIhT6jaYsW8adlH2VkasCQKpT8Dt8hTuJshSRMKDx5mwyq-AIj_JZHcwQSr0nAAyTgOtTWd2YPMFHSoI7r8xCOlJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOPn4wOs4foIUO1qMqGXwCj8Mr7PJQESCQbI-EM1vfdypxiImk679Gy3tqShC9w5TfvOQGhoeg3mqJgnYbDYsyimnOTF9riRUYi2ZNwAc9eg_N1AutcN5qHQUG-1E-XeagW9lSc4GQ5L_cupQDgE45to53Ie6PFuWu74Mj3DiOkvFCvq9IJQWGMDBMaB-v0OuXyMSZIiT2t2nNjaTZWFQ7o5aX3Qcix5_n-P--TZMoaDn5cVTTtJyaDQaKzNpM_NpD24kayV1Dit61AyhGK4bhOd7yH8TtaBCrpqcjhHz6NikC0Nv89qv90ACTkFo9eszbzAVz8D4AjPfIMgN6iqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FMZXTrdTcUKulB6kwR7W5Du9uLxeM2_D8pbxt4AtJ0NLXANn2zrUYTb7xALhxO_4pIxi-XKr0LVDJcbA6OPKLjCIg2kDY538YexpcLpN_VASpqWU073Cpl9m8FaEi5GSzRfOoPULUSEPrR4_L8i46kILSxV5Um7HVlZhz9-OvbPePHDH7UrlsUp3Liuw4OaqEU0vYkJ4X3gDpvpIBJcHs_TBbc78uIEJ2WsTrnaHKM9S-WLR5nh9eGoush389U6WLaKt-AzOZCgNdEzIfzKGvhyMtVP3tEG1B7ocwYITyCEBRdbBLgbXCMDjde_XDYSmygH5fWjiBmMfO4UnuZvbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXIkhCgJcl8XbKMhv29XpFWzfYSIJCTcnlpISdFx4J7EVXfAJhvxNafIqHwH9YbeyONO-mrurAOKBR_2rPAd9uX4ANoL5UOG6CY1o9TLVqRrXMfBF1Agz6rqAhLBueB54yLyiUR0x56XNKZzNhEZ8Ltmvm0pwh0l6T3k67eLvX9cb48oZ46MGky9yfrlhRh4UJ3cFn_O90aJzrCU1iWkEhDr241aUh2GMOs13j9qsbPsS4oX2E_1-82MAmyf0syMyU2k1t0WfU1FI4plZzE1YXZ_Kua5ChUrJN0jvUWIpyUSqTkXMma_p6K1xididXgOqw2wDWtUuxFWp0DjbCbMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boOWSK50sPV-Sdu_ZB8qFzm_2mk9G45SazgonRFYC72r8cUyHXy6Ae9N_L34DK9yK-dThXE5IFjNPwa9AB1hH3nx7RB2iZTBbFEZf4VsfI6nTrYIRza3i2fdM1nTeKiQ2YlbU36-ZDpNXoCSLAq4nBweshGchHnsBBaucwwv0lVoYUqcceUHUtMMk1g32I027qD9Z1G9jP1LHRm84q-Vavidc0oJNK628y17BEKiwxcCImXMHGx0SdqE7nJLiB-p43SrNUCAWuAS5nFXvnTgMwfVHwtXoBXQ6MK91jotl8gxUe65_Ur-Qi6IhBsJc0S_y-h5fl_IituCPzXpfnYKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqORDhe99-X_4kWiSdv0UPnuFYNf73-6eU8Mr-YIKKoTElC66XJvQ4QDr5Oatya1R53SvswPfQr-1Z0KoXIGqMQspJfxRozsX5aXmQnn_U0wRMW0wwxsh650chCO2dTMmDxo0qJWc8kLFcRyvr3mr3nkUWcjbLnkrvvM_vXupRgbeuEsgBn8CsuG526HsyzlqbtIoS1Ic22mACvGtUUT64QEcM6RtcE5Ai1T-B8ritU-KBy1Bd-fbi7C0vWS-6ABFQpTqa9XSaPQi6olSyi7oNE7r4QnBVf7RP7fFo1wJf3q2w3082I3oQnQOanIeAMzAPSf-TiVCaXFXG6rx1KrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rrP2M9o60aT6TxS1xrsPYQ4UyP2SP6GCiRvmytPwoGXW0wnEBS9u7ZufFEjYaZRn3q5faarohYVrvn8-ljS3WBhMuUBzw4gB2ldCFQJDqClamZJHLZGRHUkic2Vq8csxEShsZYjd-MVSmEfoXadVlZMJDeHrm8ZV-hMDzSzixmFGgKG5DE7xcD5KMG6KjWsCkohHsG_su5S8HuyGuMe2RfaoQN5FBGUf5baokJjVKMKUNkDcJspQOV_IO1tisegIc6XHuPZpaaDgpif8NYhVe4C7RkgG3yPQoyLAUMaEYs-Eylo4dlgreBpULa9igSlrMTIvCG1LBAU0_p4TNihBrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vgs4n7lMNX-eBlh48Um964zy_gCJfWNU7cmPqnf_fKtkUsdexdHzNdZ3zTfKMNzFE56Sl2CcVMndsPx37gVhMqM3U_pWQQIGnZNHpYRgpRjXZHMOujReQoiOKjMP0o7Tq-kGPlX5EaAlwdec93AoSYPJAcJ1r5kWwBTWkTKApP47kR7pwYrV5I3iv54GlDsK9q11Uq-VISNiZktl8QxDF26ay4U2u1x4ptjcrnktCIOKM8bfD-XjGoBWK11pGeMcnWxCYzhLCpd8rt9_mb76_na-reo9_QgsXdQHdrPsoeoz-vFTugYn72EpA3zVL_2GY5HfjQngej3wAVSPq8GINw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhyxaT9Gqg5uYT1aNEqNHXyG62MIgj74a3UuMmotrxmmkKwbKMMH6SgPno9eKObl3Vt2LIjMdZZX5c75H9MbMPZTCIcdS9SQ3peSfDe6vfqm9BNH0aM5AOf204v_5Ip4b658dDerQsawg9_BfE3Wr6AUzxAvfAEXy-ksSH_HSqO-N2WjxHldOUK_rf47IfJo5scYObs33Q1YdheSGX91twtLIwjnlbFDwHaE0-DchWwD6BT3iNgLPihCt38_i2nUhQcLcA_jHYgtzmBgZPFnKB1RMWiSxPO1rNxIy6H2VS0EuCLGJsMniFbXFtrGBHPtlpMCJFizyuhu8kNNQ3LU5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbzZDpGQqntSa1HDH2tsSXwVWVTOsJ33wpFbWjPMWXOSB0P3XbQBrDetBVpoGnQc7TgTdLXgJKH_QZcIaeJzZrQV_p_7_iKKHFmaH4Yr0jKTQlpzzIDzQ6seN01SVWL7qgPbk7GpP_hsavx85FU3PnvJ_wMKuKSXJdYQpKv3xvLd2Rtrm2DHuR94rrc8_0TZpLor4oAUX2aAn1APu28w3GyFK9LbJjoShgUwHBgmXpmGKiuWcjd9a8TiEtA4e3u1PmrPNyQkzEtkZXdmTcGnUn5E7Y8dD0joK9msWds89kfBL_Xtt2izAT2CbVeWLq_JZs-ekHq-txrVjcu_HzMvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ai178guzjeoVk0nd73JUTHipkka6etLSH6yvGejyxX7j2q96T7Aj6g0raGP2PQxhRRJmf2YCuWBQa6obxNlhKpT-hwOyt9SF5f7LYJZNiBS8nv2s72hh2JJIPWSHl6QwSNwyAnqPtL5kuOQbpS6Yen24uSjsv5FQ4dnoB4hpAGlxTUB0acJVouE8z0pvPNhPxE6dLiIoR6OBJRGgOPTQnQPdaXVBF8nNuqj4QpjgnFmlMaN9UieFiUj5xQ5jj4bwlQRTVFt3qH44VYz6gGB1cErGL1F-y52p46QGILstOAFOVcNKzMnwSMSBi-pdVTy5lturU02eFUKp473KkEeqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukLDROIkoXGWNSIxJtLXQmPvoTub9kKitfeFtTv3glTRxyGib2xQkuEieVVRSa_w-noaK2NfxPl1fR363r7fMFrawY4hQF-n12iJ77WUBZcrpMVFZPvgCwTxxb38Pq-N-IoWa7POnZJHpz66K2bvQv_AxfpzyAmsGMuB5rTQ20qw55NDT6gTUsVPls1p3qovYYKHkUHGGhKf0X93LfshMge0fl0riNoI4sv51I3p4oAvmyBgwGuNdQdT0mTsvQGRRie91CqTiXKqgOPItWyctNa2UvbrY3KhlcaOacLRdjjROHqg9t8x0DtqW57kfjc9Vs_gTMvF7vwWsmfdxFmWxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSoRI1v4f4GePaS8-2Zir8cKz4TJdD_k7qcQdl5ZpOTiFqyKUtdTI9aw5_Kp8XxBEUu07ymrOth-yjGvgzPTfwlw6OoEFweMCHXJjoa2FAHMqNE_zPIbGJvdWMAM5339A3LMppJaVc8xkaqa4gt4DVQlqH32-4xERmR-0gMTQC_-gZUnYRbxhbNeAGH9YolXxgqYx-DY3eU4FHMMGtyKSH4CuhIYc8_qTxwQuRwTN0lFZ4ao1sptdyPsopdd7r5byfvr0YyF_iOFnWdJMy-xwFRDlf322S2ueQli8a6JCInFsy80ccVG02aBlLln4NyXehsYl7qYp_kQpji429TkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IqS_C7vbxfF-fVRDQqMjMx_m0V1D9YUML8Ilj5CHJz4G-6W46vvZYGgRdDQ26kZ7a7l4asVf-GIy_xG2ptxOVfgGG_MtFsYlNXofEXa7MyniP7F1H8S5vnw7IvdUA1FdxCCSQQymzYtkInHY76eSINX6xHZ9bTp1K_RykwCqcScFhehQ5b_P2bNIdX5mPY5V5B_cmXN83J_xsldMaSayFYQuYJ3kQHB_59EafW7SiLZCSm17-FP4wguexP_qyiuu8WE0CN9HGUoPJaDLthRFd4IOUSRLSQYhsWsYyzYMLCz55uLS5EMQPwqu6jQpAEfFHGkPU_XKNYe2Sj2AJUHUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gyqOeyMUOEOwa-r__hQyAh-KAhEFOSpIh67kNZ23Ip9-0z8-Nz66yNSLDE52Qh6OKBpDWOnXmGLURZSuTsqwEC3n-rzA3D3EIKY87DcTWQIuRhNJmbFPCnXyhoPu9EIyzKHpCqz0l1DWyS-hfdngMlMdngd0KDQlrcuhgoDrPBMS-FoaFRCsCq7rSYtK5Tzn73ZmNzPvrwx1TD4SoOzMJPphuJaGrFo_82Br4nRRfLgyN_4v26q59_tM3copiLBv2N6aWlkZa0plwyzU3hUwY5GPBnB57glB2VejuTkGoM7CDcG6RIejSEtCLPqEnHv0FVh-HmwMbqjPgFQBg4nwrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M82qaD0UDpOegz6oCcUm5aeAbOFrE6lkFBZiHq2xnUKbSHmdku8cgOVWhYAhRFUaW-9DrSY08ptRE8Tp8StGwavitWO3dA-aXNdMwXg2ZivRLx-KY9VJVXD2NZRAarslPwKzG8pEKjvHqamcD1c-rokn0plpFFKWiscIx3G7Dwpxq2Z81x2DX3AcWn1NpJx9u61RL2MgWFTNx9vaRo_KzzINs1_T2nyYa1ec0A9V793Di8kNJHe_tVwEDTtYjtSFDnT6lOcWY5FGwBDuLbyX6y5JwAz23PawhLTHOV5jl1RV3MkicCkSw2Jic60mlv7PDMfALWx_wXR2lumwNdlFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwoUZWSEMBquBfGOaTLIT5M5JxOBOQvbo8HdqLrMGLMEarikc7SJymIiwR80VGuO27_0HubBTguBiGcYUJ69lnDJlFtkg2mXGD-OglN1BUiAKrmkfxm-GO1VlGnGMGaXnorjjR7buxpVIEr5BAY9T81xxBrojRXzgthQkxh57GsN8sqXx9bT-uff-b_Q8nJnfNNLDXnARE6JAyfDEbEHa8Qvo1qSpjByN3Q3h6xTZYvJLBg-uNJKslqPHCbOeh1oci4DBrbqfM88vfBNdM_D3KVC2XA1dvXvH54iAiTf0CKRYPHHw2RmjnsgKa_Dkdu58E96FOsJYZqHUcNUTlSswQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2FWxChC-apXsrVeweXEAbmz2Lrg6XAtwZxhXk2YN_pTXBMovTTiHeqDvW5wF_xTlFpR7AUzfyfabPzoZQNvpSO_-B2GyV4HImCgOgPa2Z-XbhIpmHsvbseigORrDgZA0QneQVGulPX80fwo0aQ_v_LGepqEJUSrN9DHV-ZSbFk0VnZp8Ziif-OA7cQ-lzEAntWRogXXMQnAyPJ8HEU-s_1JdIlJfyEIGRTHQs6lm-2XLgZxIjkLOs1ZWaaqjjwmu5vUgGHbWVUKFlfVmh21irbWWkxMNaeQFo7-ZW69yZHgMpcmdf8G8Cyk31YAVtaLle7oZwoooImRzQ1TmWYrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tw5tR3baxK8KdiCWnoMERJy6WK0EQn4iIoIt4xvwNWNgS-t4WrBFbA8Y2bYdgQI7PMlpXn4eajR5CCDWaNtgsV_S4jbPde4sB0_HfAJAmHj_rT97baGt23cX6gTpiaCkEA-_7bY4iG9BbtO-y16XoNlo70AZ0Bzcd8SWVUL3UGnOrpC7yxLEGx39swGcwv3Lr3X02cq8Vrq_fGpQIXyCXZtYn_1im4fOpTBbteqjDHfot1yyOh573E2rp3au4jHWI5ou5_RsZQHIpWEsPrLKIQmP3OESYPHmC02FFgnZ61waPz4foXR0p-trEBvFfncy_N3sJJ2z26VpNeQAla-Rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-Hqw4DWfpEs_Lhuyseep_rIA0uBz_nIavoLF5C_tUkroQFpyzdhx57JQ522GqCH_miM_-ZsseLs4elb-fCeLzdqFAe8ovFXjZEj10znBxeUzqmLeJ5MDVeE8s48BQas3HTSkI3pUTMZBP45cNZdmnFNG93Z6uXKvSxVnviRbfRIh3y6vUrlc8lWTxt6QKVVXUmWjqqelzKkJAhSKrNNGZO6GH77uiu_13eYE9o7z_pkqYYnvF8qlqoSVpwwhnMj6xoGwTWs70w5jwJVu50tIxP11WNNLpxSQy3sjR3hw2eGuRaAwVmE4ro0pWqiRxiWkBigPUfHDjrMUfY7x2O_gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qq2ZKr5LNzX25bZzhw6qvtTYdwNAuy3P42zeOmabAB_x92X5gA2dm2M1-3AcS-HHOKUVpm0hRd4nbAv8mo7sYzBkRsG4Nu4x5-sjaYch_GaExgmLDBNJlzXZ449H15jG_P1te2L7X9HaOcVdNQLb79fS316zcyV_h94x-49lQQ8HXMHOSPSR4d1YScdDV_AEKVzjhgcUxujT4YaXA2mfss86S5DDKe1G6JDBKPLKeawhG9yXW-udOfMT9goQt6H8AJWG3lGNfPFVt0c8IzhE-JAQ9hniCmMkv-4xeamSUz12hu-qf2A-S76mnLL8xpjtcUFGd2BuRIDpiFBy8XMc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcb-j-V4dhcR56AF7RATGBEL1tOW4uTc84wl4KjK7-EEXOOnlsbqyBiEfk6b50LQFDKMJPSr9bded6apTEiqcKz6i4nv9GxygiFoYTlnMc0koKkfmpsob_nDLsFTDpKcxBpx3tWzuOzDKJkp-wmn2hcQV7XteYqf0C91jjmr8a4ULIJAr6CNBhHGa_0ZdLJEGFM_WZoZE9BNDZqPGZFcijfo5AlSNzABj-fd-9VjIM2Lyq7KbKM2WEaPyPX6YZqix06WMJqJjY5EumCjFnOPDDviZntJe4clvd5nq49oy_BFP-s9FYZNo8emayrBAd4HHuVUZqTnVIw8AHocubOnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وی‌پی‌ان پرسرعت و پایدار با قیمت اقتصادی!
فقط با گیگی 4/800 با بهترین کیفیت ممکن به اینترنت بین الملل متصل شو
😍
🔹
تست رایگان 12 ساعته
🆓
🔹
ویندوز، مک، اندروید، IOS، لینوکس
👁
🔹
دانلود و آپلود نامحدود
⚡️
🔹
مناسب وب‌گردی، گیم و استریم
🎮
🔱
20%
تخفیف ویژه
برای مخاطب های عزیز کانال فان هیپ هاپ
🎁
کد تخفیف
: funhiphop
🤖
برای دریافت اکانت تست یا خرید، از طریق ربات زیر اقدام کنید:
https://t.me/ToPoLvpnbot?start=start</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dq5lCdqVEuGsAoVEIEr3nL_fDL_P4Zlk7Xt7y2-iJWJJrUbD02igJRf1DTDl5sI431WJ-UVleokeQFpqtExpC3C8PachKZfmJJs6s-YDQ59tdWA3Jo8y1t7bKfckqHeSuDIolG6Kx2PF10zP5AGEUnVQpWkbrA82D4kOmwDiwbP55b2gQiRg1K5cLKDoDodhv9E0_E1AUqalnAiZ_B9SAic8h5LrjcwAapejHbOuYqjXGuyJzZWDBYgXFg_tj-kOabaU48bsXlUtMzmM4-9iJeb10ubYoM2QNk6MN3yMi741PM6yFWBi9WnygYfQucQO2S68L9zHbrxgfy_pMfbIug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0MZJMTaLUhGx-JgxLk3rNh1KzHIrcavZVm-ejwuij6LGkGOl81Ja2BHUsqJNsiBiPSDHN8vLuYHbeKLHV0u9l3_kkTrJ2x293Lm5HKJP9oUewGlu1jvvG5s6hLy7fZ19Jn83Aq0ahAIonNjqo2c85V0NjHWgUyTS22pbSTVfzPF-szSOJ-Rgm7lLMDhhC9Jxsu6OAs-37jMD8NAmup9jHPoHUmMmNZwHwvJ7yCT-qxqE4qZQq0_0Ix9dZRVrHgfkaUm_XLBfQcq9BGUogYzCwiID2o4qU3OODTspbo_dYAOl1ffvdgPW00XMuiMctJoIepJZZp9XJ5lLnXL-nBGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AagVQiVlmuoNz5xnylPLW5FRFCYtzdX2C5vUDCvunGnJDBVW1iov70fgE6RFD13Yg6oalAM_lPmcKaU-X9r3H6NwLntpYRNQw5GeUzT5MURzCCVmeEv4sml1KwcBBBT6BBz5cVwjrmw65ePna4pbCbxuSXTosaJqO2xsMxhvUlJX71B5vMGj52dNM2WfRamijYm0Rc6-dDFD5L7FoQfYNqyORlB0nfIAbFt-5aebxfPGxCaNs3O2uRAtU66ptqgH1o8NfCKW-QxoNMUXZgFeShwq6xRi9dBCV3HcrQLk6vj-8oO0bfE-JX7hSUgSiPjjQ84tkoF95EsA5DgSDj0eiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pneJbrPsbxcQqvSEYc0MUKRQjWdNHKHaluACDSH303OG_Nnk0WVZ-TXjzjFOzMGAES1v1o9QQzihnZVB9gJ13RmoLVMovUaUNiYoKthKzj7GLfAOsM5MhShaUqJs9opFSlZdgviIvbz2NbKggIIIpVWU1Lxye-45sUMNAfajE5SR7gTiQO789kqb64SEcuov1c4Bm_ZwcOB_sxJ-yFYzhzlUJCkUwNuoiv3NxPBtT7mb3q71GfWKmGhAhQT5uwnDGWjop7OxpuUSxZ2rJrghfsiTMohPek63kJfCJheIoge0kUMqZ63qp5yThtJTBveNNN3H0AeWEyZDgryPbKFSvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhVowE2fUQL1mcUoCYl3fnsmWstuc2PO4Fct_8Qj3fB6OWjV_RubG2CSK-OA_qSonyJ8qlUbSDcqa7KtlXvhRk6iTnu75q_zd4Gtvk8XAjoq7PSZu3Yt-leNULzt6qTLx5TABm7piLE6_470L2Gp5wUbcNVt7IzU-onVvaCzjTYtj18Xv5tPk_hzbOFB5ya6CyvJ3S9Am0y_mucESfABwioRaKRT2uOooyQ9XQd_pgXtj_dozDsbyBkhFtEt-nww7aM1jL5vPDJIaV5H_N2JmDJjjV5ZcXDeKKtjg64Ta9fQt9TveSbHYR7f5EAWcecs4YbjNlFIpSt_rFTQJOLJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81297" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=l77m1LgGlcqXNExRSxlorZgDP2Y2s926UzktKJEcXU2NGtoEY1S6xyvdFPYx5H7Ghd5fTlGatNreYFwWD2J1_xyLKaalwfNXCy0Z72axn6b0ZxEVsn4N6-j2zFvGeUlD8k8HcsXbSq2yYy5YPe48bHBYTLq76ZHfdDYFDjBiHxs7QPyZbmlF2KtkEvB7j6RBnRpV1mJgBIxZPVXmcY6spaotqA2aynnph6rOqIqWLJCrqwsk4GSurz5lFib_SXEx9Aw43uwIfJy9pdE6cLmEnzblUPdYKuTo2sQ6WazwQ-z8vV4UrUhxqqgm8_x3RpD5HPhRk9f4dw1SNQb_Cmn2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=l77m1LgGlcqXNExRSxlorZgDP2Y2s926UzktKJEcXU2NGtoEY1S6xyvdFPYx5H7Ghd5fTlGatNreYFwWD2J1_xyLKaalwfNXCy0Z72axn6b0ZxEVsn4N6-j2zFvGeUlD8k8HcsXbSq2yYy5YPe48bHBYTLq76ZHfdDYFDjBiHxs7QPyZbmlF2KtkEvB7j6RBnRpV1mJgBIxZPVXmcY6spaotqA2aynnph6rOqIqWLJCrqwsk4GSurz5lFib_SXEx9Aw43uwIfJy9pdE6cLmEnzblUPdYKuTo2sQ6WazwQ-z8vV4UrUhxqqgm8_x3RpD5HPhRk9f4dw1SNQb_Cmn2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=bhA_0WUnaqlGXwqLV5SIRtRXI6jNAVpLsVW_0WOGeac4BgXxt2--0brp_yPGGO8kbo_BLexu-Ynmj2iCI5_3OQ0Jr8sHxaV4V7bmhZGIGAsOP5tyAIvb60gv41R6Ufu0LsZEfD--nmhfq_4OhBNkg3TYDIQ0a6OchXNAasnjuiC6EvPG3pmcB_9NeshY4TUpOeqFifYkbFC8tOG2fecObPi7Vm0zn1kuqqu6X2Idmodh8Gj1O3j8DHGoPacqQ3uYRhoghqK_6hTOlNOnYMJ8yGcgUp_KiVwgy5SDLQP27fnkNlHV9jRYuUP3AxXPXppDHMHp-LpK4xGptSYagJMzHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=bhA_0WUnaqlGXwqLV5SIRtRXI6jNAVpLsVW_0WOGeac4BgXxt2--0brp_yPGGO8kbo_BLexu-Ynmj2iCI5_3OQ0Jr8sHxaV4V7bmhZGIGAsOP5tyAIvb60gv41R6Ufu0LsZEfD--nmhfq_4OhBNkg3TYDIQ0a6OchXNAasnjuiC6EvPG3pmcB_9NeshY4TUpOeqFifYkbFC8tOG2fecObPi7Vm0zn1kuqqu6X2Idmodh8Gj1O3j8DHGoPacqQ3uYRhoghqK_6hTOlNOnYMJ8yGcgUp_KiVwgy5SDLQP27fnkNlHV9jRYuUP3AxXPXppDHMHp-LpK4xGptSYagJMzHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxKNL4HGIK29KZSKeo4e3WFWCS4AIgYcow0BFPTET5AN2hYkNkG65RhAJWbX81g_SRmEpUgq1CL9eYAzCvkQzrrP8xlJGDC2C8b6HYfrbh5QOOSl7Fa3lCJr9x99H8UeucMKby6m2ozHW9DLvr83yPbC9SoL5Av7l1cZ7fheWvVU01ykTH6CG-aMSjqgNJzduWCt8bqlBEb0MDVScdNZZOC2khBvBVDFxIvXPreSS12Yu8oZGmJw_ENs0KGZmIYtHftg2-Jf9i2x3CpZ_epqTyE3XTHqzDAg2J6uhWIZpAXxllZ0AU0DriMXtzNqNEfgDvAlMXP07KXa5BscpiAq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Gc5lW4wpQeG9JhxrdCKyKo0NgEXcTmKTJjxNJzdEgTpx59V1M9XtSxfG02sLFsUKuyLdp03i5UGR6KkscttK5kY2yxkNL6DtbYx2JMi7r-yIQUT82T_BbJ_0ozi7Ev5H5sFCSzTE2rsbD5zhPd4H7NLRiMFWUcOX79mbvSh9Z-gD5fiwq_sVy1tQFSzSiagCoE4SunnZ6hHd33zOYej5RQMwUL70zEZe-5T_hvmXs5jHPAodVhGDgUeCUVxc6J8bza42n7du1gosYPMqSiVNiAg7Lx2UIwcZci73nHLMp7EsRIpg-qF99BrGmgqjJzM5Fu3a495N1HNd0U3zBCPIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=Gc5lW4wpQeG9JhxrdCKyKo0NgEXcTmKTJjxNJzdEgTpx59V1M9XtSxfG02sLFsUKuyLdp03i5UGR6KkscttK5kY2yxkNL6DtbYx2JMi7r-yIQUT82T_BbJ_0ozi7Ev5H5sFCSzTE2rsbD5zhPd4H7NLRiMFWUcOX79mbvSh9Z-gD5fiwq_sVy1tQFSzSiagCoE4SunnZ6hHd33zOYej5RQMwUL70zEZe-5T_hvmXs5jHPAodVhGDgUeCUVxc6J8bza42n7du1gosYPMqSiVNiAg7Lx2UIwcZci73nHLMp7EsRIpg-qF99BrGmgqjJzM5Fu3a495N1HNd0U3zBCPIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب آنتونی جاشوا موزیک سیاوش قمیشی رو به عنوان تم ورودی خودش به رینگ انتخاب کرد و وارد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIibR4TUFx16uXk3sFbT_3ujkL9GsszO-ytxtIOZsKxf0cBBejzDVYr76ia43DkUnfsqQGSDhGvBtmy1gLyxeksIqFJrMpRF6cYF8qhl43TKxHODFEmo9x7KXP0xVJ27F9dnVTbD-EJVE6nd-XdxKIz-yqxUBT4zJMO4JHLvAN7t3Ht-Ogpf-53bU3JlXp3R3_0cay9KO0hqaSukpilAN9X2sOUZ_7ReNKOxO17dZknd364kqIFcpWJSLXuV9MgN5RqpZAe3OYHDvRDamIq-Aptyve-mwjjCmsB3FBbGjREho3M3-YVE5SDTdFBVZ7kJpiB6zoMR3_79EfoDyDHNKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جفری اپستین تنها شانسی که تو زندگیش آورد این بود که زمانی خودکشی کرد که ادمین اکانت حافظه تاریخی حوزه پوشش زیاد گسترده نبود و اونقدرا هم حوصله‌ش سر نرفته بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81288" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEkeFT1c24OurgOs5un2TYXb1CADUMxC5IhWSrjmN3_acgANsNFNN6HRQUFIkFPRRZOJpco6BuiC2F0pFqNm3qrwKrN7TTY_qVIG53lBawNsVIK11ZlWOQGXknxFm0l1_yabv5-5LAeUAm2RihBu_xzrbT2MWw2AtsBuotqfulBha3w_NjN2GkY_v7R5Hg8nsH2rCPunltcI048ep_Tyjw3E58KwSMC6tIlYnzmcnxXkLtX5gxF8oT7bJKrOKuHCMHWJ8fg7ic1x4IY_Gf35aKeHEc2SiUqeQOacFaFvbj7x9WY4kp5hZ2nwOv5Ee5GJ15St9Yd50IW3FGXJ1BnFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو دیدید؟ رئال مادرید دو سال دیگه برا همین 250 میلیون یورو پول میده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81286" target="_blank">📅 12:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5D00mqQTYdk1Wo-mitEYnKPx3o7o9J1vUe8WKMpV-V5lBtpLTiuR-DtumLA6uKgz4kM5uXFzWiyLsUxVVaEaS_Lsot72cjMTrbv4PYJ_yqjB3HhIGaZnUkajbO_E58ehMM_2GfHfkyTyVloT84WktcHFDB-42Utk6WnMR7fs3QGqjNpNieRy-Kt5z7V8VTsb_bxE_MqR6GupbYJXxZpx4iauYw1co3mWVVVTU1uleDECpmBbyD6_JsubCR5oYgOGKxBKhbQVJPMeUHd8CmqgatAps2dMlPevEJlXl0JY8xPbpMdFg8M6SGh1GQpmK1BbFR-HwoEeYddLOIT2pN97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید صدف زن هیپهاپولوژیست :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81285" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwmrFclJwglAAODSjw_Y76j3gYnYZ4rrDSKKzm6YjcJA0gs8C_QqXXb3xVTaG38AwkMupj4yQg-NtcqsmQrAtWUH2r8FOHHKrW2Q_1TE1fJxNUfNv_FAB-l8jyhIZNNYU1I_-r7_2WRqbAzdKiedTGmdzJA81P2IxzDP4jlWoOl1_NZbYhyfz1r5tMsc-yopSeMnAZ_RxMwGPaJdzQmqZwjNxXh3YWBxqxVpBbG9YYonVSOvid1gop3ikMvNLob4_g8DUsEwmBCs7CP5tCkwtkeNYAf56lhz8MtCofrTepNqRg_E76VMnhzjm18GYGBdNEcQRaqorUZ__x0w4vTPUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81284" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vea2mUh9YJon9h4n10uVbYy-ffgoOib6vttIKzydAPz5u4TOOTFcr80kyEqm7vXKip-tZwt3Al5Og6MyhQwJt_QQ4FxP404PwSkhsA1bJLKXWDfOp1ax5dyF9oOcTedc9O6pVF-SgslDTw4PpUwY4UvJj5Mzt6k8IhCftYnPIewpePGGIbu5RKysTJpb4LCEXUuXyPG0OJ9VQWxD4n0zLex0QQUZ3YSueKjfzVhD-KdjflLIRihYf5m2Sdc8XtR5UIgFcIvT84jTrb0gp6LIDw_IeTnBIyg8sEcHDSBYb08P98ZstpT7ElZS-rW1jBmieam4OKViqyE6gbCBgIpazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تجهیزات آمریکا که تو دو هفته‌ی اخیر زدیم نابود کردیم ۲۰۶ تا ۱۰۰ میلیون دلار قیمتشه.
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81283" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خداوندگاران هفت آسمان را سپاس که امروز من را لایق زنده ماندن و توانا در شنیدن این معجزه‌ی جدید تمدن بشری دانستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81282" target="_blank">📅 10:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یادش بخیر امتحان نهایی فیزیکو فرمولاشو نوشتم تو کاغذ بردم سر جلسه، بعد نمیدونستم کدوم فرمول برا کدوم سواله، افتادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81281" target="_blank">📅 10:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-Cpu2HLbOndt6lnqRBpK6piDqQmtSIhppmtcxwKiGapF5gchLPL4RUeoC3tUK_P0XO_93AtE7p2wvZkq7DBeAGGznE3icTwnElZxj4Ne5A-5LT-5WzvU1lv4-_zNgcKjfzSfZxEZ0RR9_PEqIlW_QiZv_C_XbT2StpEuwR4i1NxiL5Q_uLKQVi4qFF7jkrPbo6Go0nQPn6brfm890rYO7tLediUO1AKx0vtpa3jXMqGREYQ8oKMhPwWp9i7l4E_Iwv-wrW6nL_uzfyYoMe2ry4aU1989YHMqLNz1ckfhWbO-PbWcd6XvU4kkkrqhg25xJSrKZAzK5UwaxgL1jt1JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاسی بسه، بریم دعوا جنسیتی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81280" target="_blank">📅 10:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81279">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آلوارز کلا سه تا مشتری داره پاریس، آرسنال و بارسا، آرسنال چون داره وینی رو میخره کنار کشیده، پاریسم چون فران رو داره میخره کشیده کنار، فقط بارسا مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81279" target="_blank">📅 09:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81278">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">امیدوارم زودتر بمیری مهدی اونوقت حافظه تاریخی داستان پسرعمو و F35 زدن رو به همه میگه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81278" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81277">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81277" target="_blank">📅 09:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81276">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81276" target="_blank">📅 09:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81275">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یارو پیرمرد افتاده مرده ملت ریختن سر جنازش میگن ۳۰ سال پیش خایمالی میکرده، خب کیر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81275" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81274">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سلبریتی تو ایران همین که خایمالی نکنه کارشو انجام داده بیشتر از اون بکنه یا فراریش میدن یا یه بلایی سرش میارن دیگه اون آدم سابق نشه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81274" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81273">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdE8NlXpOcV6aa9rA2ZmEazcVNBn5dyukFldaGmdo0F6nWsaieP6BZNtvYZQT0de7ubAJXF00B6FvxB5EWJ1kWpGf87nEPFCeaB7x7_g2uZsQbLkYv2tPWfeZ_hMYjL7m-ITi66RZVbUyA5Lbjjc4Ugaj34D6XacBRVK-pWKy0-LHIpg5O1uIb6Sbsx1g7f1wDPjNolrMJ7D1XkIqvOXSqfAjKG-uNrl6hwiLMoA7qk_C1yw-AD82DU2UqbWKVgAP24PXuk6YQ5InxY8pdrO-xHubsLu7ZDooNVTKhb8OVwAc2nitg9BELlcyVwyqFUIsMHfydxYdeYc6Ub1qLrhRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشید مظاهری اومد مستقیم گفت، چیکار براش کردید که از بقیه هم انتظار دارید بگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81273" target="_blank">📅 09:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81272">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmjnZqXMiJj9UESVo2PNqL9dSHiu1M407vlmW8tocHIHdvo7zMr1i9COAUFpOhIBsRrGsW4GOr6EpzjqEiGTrto8YtZg7fW6uldcp_jfSrKMvlTUuv915cmSCJu5klKNZrt4dPBStlihamuRuOhvpFAxK3bCOXlpS03A8mJ6ivX1fZOFOYBe5pxuI0-FoXB3agtRl-IG47XZtW2-a7LtuEC6OD0p0meno9USiezLT5BSR-MrnJSHuPrpS77lSE93oWazmHa1x3iDKuXZzM0ikMHnv6RI2duHBd9C3YW4aynYC_lW6_EWGGK25W2VdIqLfFYdHZrVwhgrPj769BY64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81272" target="_blank">📅 09:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81271">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فیتای ویناک و هیپهاپولوژیست از سپاتیفای پاک شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81271" target="_blank">📅 07:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81270">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUijfPdp2t5e71-aTqvjp_NlIDnZuBYr2FIqzB3SKbIqCJV75Ik_m3vyuRF7rOK8IAfuzJ_yVUMUihUVOMep4P6JqWOoGBsirLe3UFsDn_ZNVPx-McKssTet17NUKAgJmY9EOeuIYutsCOA1Wg7Zge675PonJ4OI3GeUhkIqKHKY5U5gBH2d9Cs1bnJspDLufXiEGUgtGx8SmVuokt1z_5Nivl2-17i7IICBG8rzW_09WREqCCropg5T9SeR8fSjfHXnyVz9YKmPwLqGEvHMqDoLMB4hMQ8sWecFiOw73dVYO5NJ4GiBp7TNyEFt0qpZ4X7TLC_toLLblLOqUtTIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود هم پاخور بوده پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81270" target="_blank">📅 02:35 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
