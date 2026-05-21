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
<img src="https://cdn4.telesco.pe/file/OUUXw45BSm7pBi7yTiMAvc11zQ3-0ZcDDe7T82vWAOOHGf0NHtA3QWf_NhpN02EJ6k2_rvQG0CULGYStsNwO1JAozu1bNDkEYpL5tuFLAjKhEI7ytz_HoVOeNM4QsQIHFlJGWtucbwjACRgM9966eB4XawaAnqzxiWvP4uT4ZPKfFPnVMwM8Mwt89UTCaylzwTtYnXKmQ6pyQ8D5Ejzggi1X0ppAZ2JCX3elcHHe_vu94EVgxmaTAGIFwyAeaeCWBn4HgimGg3nyCV5P_oKg6gR7PFOw4xjCmsjqGAC510hcLgb9OyXrifLBKwNQAprwZU7Eywmsa7WnJKH-brhSpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 130K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 00:16:57</div>
<hr>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=GYNC1-uXpWhLNN-99VSwjMqH7ffqlld12QVmmxmBXq_6tbYJuaV7iD0XhKJVJdr0_bBFSfs4w6gCoFDtGVmcejO1mjISiLez_-JiEJQaVjWCjwETXx3xR8moHGNJOVASh_27L1D4zvLN4XMiOaff-PJ6fqjZODHAk1kL_JvQUBXOijocE-AUWrYKbnJ5oOlR_s9Dzr0EzUiQM_MDPXNG5f8qcAp-uANMyIf3wfTOvAgBbXeojQzKxiaZ4tJF5dt3g9bLKyfojE8pPHWFG__z9fQ0mhXLy986n9eoM5Zlvwb6D3J09rQK_h-lcqZNORnIs6m9vz9qrhRqLHbMVtUk0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=GYNC1-uXpWhLNN-99VSwjMqH7ffqlld12QVmmxmBXq_6tbYJuaV7iD0XhKJVJdr0_bBFSfs4w6gCoFDtGVmcejO1mjISiLez_-JiEJQaVjWCjwETXx3xR8moHGNJOVASh_27L1D4zvLN4XMiOaff-PJ6fqjZODHAk1kL_JvQUBXOijocE-AUWrYKbnJ5oOlR_s9Dzr0EzUiQM_MDPXNG5f8qcAp-uANMyIf3wfTOvAgBbXeojQzKxiaZ4tJF5dt3g9bLKyfojE8pPHWFG__z9fQ0mhXLy986n9eoM5Zlvwb6D3J09rQK_h-lcqZNORnIs6m9vz9qrhRqLHbMVtUk0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 405 · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIfh36ICJdxBqDKFwwdSqKSuTELVgPNTf-CvBq6edG7PpwPAAAOV1XDwoDRrC9XQ-zwhEK1DGfg6RvUXUC3mOO7kt1S2krMyj3gBADCIl0SQ11vBlxKLOm9aAXDQI5eEzmC9rSyR7OdmVNu2IC7Fizr7W_WhmsYPMw91Edvs-1H6K6bgG4jZlmFwfM3o_I4H5AvHOFspx97M7WAHgRfThqojHS3J7eDh5N3uspkSPfQtsTz32H9Ax8FPKF0BDURAjLhSBagaPyC5QjNoEHYYJHj08WdJjUodBc3TJtveZEHn_KxR0dAHjJZELOIKBmF5W8JsZC02EU36hqIe-Ut3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKtK2GiOFTxscUWeO7Z-gZITVqO4SZ46RD-966WjUpoaIeNeLd3ouAN0epAjE4_wR1Q9m6qQA52eJheeYzTe1QW6ayvMPSozWVXxbv0xaeI9fxKVKN4BfB1YR-bh4MxfliwnwEj3ld2NnWOF9lNQiMn9UNn7nbTpm6KCOO9C-3DOBI92Vx-7HcF_zcmurwpFggEwM7QYjhykUQjmYYDvo4Yt6oJE1pe6OAsBiEb5LxDznnao01O_OZ9hRxmGNNJVG0j77JEjU5fCsW-6fpjw_hh3fW9Swo_w2TC5YhwhilxzIfe1IZYBRPRaCu29_Pedgd2QTb1fhwwigO0sAHlRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNehtLIEo4Wr2oUFeR62oVRqgfyRBwU0Cx7c2TorjYzMpsVjFluYEwpPr62uPxBvAV6OmVI1FrhNuDHVRoKCxPVxTv8pfv5qreyg5SXpX_Uwgu7avOs16t2057_xPK8ACct4NW_tYMkqskh3KCjYkUlkGZOlKfId5e-Q0HcmGbBvOe5RXj0g39TA6D3Nk0JhcVfxSwvz4b_zMUCZKRCT5rmu7ctDh8iiu_ZwgD6Xl7sikyRQz9xQzbW-S_NgZyf8GXZA4oN0C99-gG7c5sKtEjc4EQPe4rUlRzDwp9QtZWjZRr7kqPQRoGWtDwYdkQ5KPYr6_f3y5E0tFzH1rO6lrGP0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=Y8xsAy4WHfBmjTG-KteYP8Qsn2rBaSrqtT0loJIwyC1csoNuudbXjCcFiOscsb25CrE2AGedFVBqGAzWEOHSlBhaH4dBB1vhlbiWgJKbOc2Vk4oj6VN3M9Krt0ZuwBMcRqBeet3iNsG-1sYfwSYm3foBDpaIZjl7QVILujXtJn1wAGKlF4oJOEmCWA5A8CLkEiHe4uamO-JQCZ5C7KNRBgl2B2cdqsy1bNZ_Kdi_ALIfHBmfqhI9Fzn4uOGWFj20wd30sZSypYH1LgMi_YPwElHiSO4pjwWF_5bQDsCDmghgu4YryPibY4CeMMre1AseMTHj1-CtosTaVR-84XFNehtLIEo4Wr2oUFeR62oVRqgfyRBwU0Cx7c2TorjYzMpsVjFluYEwpPr62uPxBvAV6OmVI1FrhNuDHVRoKCxPVxTv8pfv5qreyg5SXpX_Uwgu7avOs16t2057_xPK8ACct4NW_tYMkqskh3KCjYkUlkGZOlKfId5e-Q0HcmGbBvOe5RXj0g39TA6D3Nk0JhcVfxSwvz4b_zMUCZKRCT5rmu7ctDh8iiu_ZwgD6Xl7sikyRQz9xQzbW-S_NgZyf8GXZA4oN0C99-gG7c5sKtEjc4EQPe4rUlRzDwp9QtZWjZRr7kqPQRoGWtDwYdkQ5KPYr6_f3y5E0tFzH1rO6lrGP0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=GQRja16rPa9RJojnr8tCYcwkvS4xx60KXt_Tq1J67sJl96ks-YORUHbTfma37lMaHhlwNMPodCXQcyDvNKtSlE49S5-jcyBLltYs9jP5a9C_urLq9AhxJ8tumy3MZDVnZuNlJ7b3AdsnXR5R0BHIUNN8vt0OJHDwUIF091jxzwxrtBu9CuHz4ZSnAAN_g6pTfGJ5GzMbiH5jZEXmnVQyWqTAngTo68rLsDh1dkVTBxkteQnKveNWdEUj2Ke8SbsxUd4vxwY6L0rzk-tZDBmy7scgqpU1fs9m3VNMV54iqpIyfrURgdXuEITPTbuhXQsVgJbDYQl_3Hhay4h1Rm0ShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=GQRja16rPa9RJojnr8tCYcwkvS4xx60KXt_Tq1J67sJl96ks-YORUHbTfma37lMaHhlwNMPodCXQcyDvNKtSlE49S5-jcyBLltYs9jP5a9C_urLq9AhxJ8tumy3MZDVnZuNlJ7b3AdsnXR5R0BHIUNN8vt0OJHDwUIF091jxzwxrtBu9CuHz4ZSnAAN_g6pTfGJ5GzMbiH5jZEXmnVQyWqTAngTo68rLsDh1dkVTBxkteQnKveNWdEUj2Ke8SbsxUd4vxwY6L0rzk-tZDBmy7scgqpU1fs9m3VNMV54iqpIyfrURgdXuEITPTbuhXQsVgJbDYQl_3Hhay4h1Rm0ShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlHvcCq8chlHFRqB0ST76sJaZDFvBcjsA8WUnVCTUl9SXoAa7em3OP_ixl_n0O5K_OQRb2SElWdT6OCcekgQ4L2MmOFy-tyC2CAYEFjo91Yy2Hqn1XOjlQGMIRqbqC9APPUXDWm4IiWmiFUAhkr5kmzNhQ7slyeh9GIvQXtgWkUyZXu_SvZT2OLd93VbkogfiwyNeoo23lWnTGpupCtH-LNftmXmzXjaKs7UbM9wqkBValhNiaQ007bANg1VW47kUtYNCBtqCL3yF5qUU3fR2cha-cLhbNeEIYVLjbizzbuST4ivF09ZVDBlLJraEQJyIZoWbg0fXr9uMcW4Wjxafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dM9DI21WTGdex8M5NgL9HdHQEwgrxyMY5fzEk26RBwc6BHzDyCgQgS3_wyXU2pzNunIoXvzVhfn0mCJi-8Y3Lczj4ZLqhqbihNokZB_rJqlq7-4y-k--wY37qfSIAj0kv94hnJ4rmI69Q-VqNMbH_5TgPwG-QViadASUz8B5K-WCcT0NSRzUaFmNCYqf4ZF1YVFdMG-HtJ29kYzPAJHO8zN_p15VdnCfZo8PWdpHzSThsZpS7znqX570ol3SMuHASNlogvHzC0nvvQzrRs4GO_6zdbsUL5ssJ-hsgezCfWP4Qm8Ws7QE8KLNJGA1h7dcVu_vhQyIIPpeVROvRHBR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90123" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/Futball180TV/90123" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCTqY30e0Qf1m1quRxCNlupCxSrbyi8LV_SW33ykAdWX2_p_ndg_o6jBdMHkLx73yW6kUjCAjXlTDldujxDzV8yYED07ZtIfjPcZlFPnc8YyNC4rZDX7lvy7U8u4vLayovkoCaLCKIOvjXFahjgywFxo5OfMuuVynDpU364RHfMjwXGx0eGavxl2ml7fSYOgvQnwVBR-nPP98AzPduqoLN_ThZoklQkVYNF4GLZdh97G3ZkI3m7dSnQ5hb7emmsvNns2zW3pVRTRiPlMF2snn3xJnLxYgSav6bwfnEfOKCal4Zs8NXkITosOm4E7RyVQWSZS5KRPiUqNHBqA5QzaaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/Futball180TV/90122" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg1t4ewwcCMIpIeNl70gLL0rMT9HFQ6vkcm733GQbD3-5iUdBGsEq0czj-Q8EvQXyNA_Or-4-GiAJ-VQF4JQyG5Hg9PaXCRYJdqVx84kJHn35xkI_SZB_PKBv5P9jlZQeY8kba9RcF7onB26N3ddmudlxL1vrGG6RcCrACgwRJQmeeCXkSnPHgYb1QiM8JZywd77FDELgnYnwc-qTckpHjujkz1qKJ_c8GWIAD5fUqq4NliyIWKMu3948_it7zHRCf4AupUyDdVtqHTcz0EzsxABUrlBbViimM-tAg-uRqgreBjnTFcEkv3mk5SKSMr4mbwIout6b9Unmh-YxTKCqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7XpYPzQ8A_UzgAPG8wAwTjy8Ak4Li5PCD64e00ydsNSiDYUk6H-9yJZb46dSPZqjEczFFPRZlQUl0R6BcC8u0D_tSS-RYsCMT6Y87fHaWXz0BU8jiUeXr0Luu_Jo_zLujEbs7iC-piE6lowdnRcZYdhR-FniHJPvlACBU5eS3BcenyB5BFATUzqi9WqGwXMQc-SCt9_GK0l1ET7hcmJTdkAeRS7KKIS9uwzaIqyORWX-oxNR7pKEWGLyD_osMaNawvQUb6tA7etKc6uxWqE28xqm-gZZnATngRljst-hDjrojG_vUIUWm8DAeLsXrOhG8FTe6SEXEPy70AYY1olnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBofHntMnRRsaDjtaxbP4sto5ngII_n0F_02RtB8tFSjtR3Zl_kSkeV2ogkeN8BnKAbQn2pt5ysOkDSMlK2eyyEvwNUWY-qcQ9Y0gAX-OoTEIbKt8tBqWhpOn9Z0xUAwIMKHIT9ALDiKBF26i8xci3LCgz2ICehSVHMK5YOw1-z-7Z4b8b7qjEhbbwt8ChHeACA0Hle5bXCro4HA1DuwtYby3w0W-02w_DUz427vMDLza5Iwjd-Fk281LGx-4JcIIyU0AaPe_w2yPvQy-7CltF3gsd4M6LmuOgx-U4gE1_KesZShQgOH1_YS2lPqHnx4mteLcPQ-4LPHHbBZbfl7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMcI560uX0Thktcp0_vwDre5dxdI3wxCE3MtYq851dSI4QvMk6XH4Wc6JU5SJCUFS2PBAW-tSNKMeycPLnOcteYLG2eDAsus2vxVDfq6gu-Fvd6bod1wnl7TdGWKKEMB4dO1B2wGV7XSEDcdjYg6iry2VUiOWKAxg4cx6ntNBk8fAN-DWmUo90hJk11kZowAaEpoxVjuUWQUrYataSCw_NGLTpB4JUGjjD49IoqMvTf-hfOc4ZcEljqsjXtpo76tivdATbiXcskE7JHejOHqEKQDc9SSmLtqZrLU9DUhnprvt_sW38RmvaocvNPSz-FAsrjqWHbfn3MmUV9DEBKMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHx6ARfP8v-sY94XM_VQk80lJRwrFGkmwgSDenFsfaxsA7u1GrviCF50p8-WBGXLESBfFIV-Dy_mK19kJM-NiLsdmC046pbUEd0Qx2ndgNDdXfZ4sp28ADvvH9hI0_6KqlfnLarEClfysVoi46vor6qkkfUFXNn6rlhfE0_xAk4cblzX1abIqXYE0U1WrGl9Rp3ffaRgGdk9nWazkBQfZfqgf4dPvUvIv6mSVZ9VFkakfw7cc2zyeriSH5eAS_S9f1S8dXkxK1X6DpM5gNyDbyJu1lfP0KJElTyHwtiENyqWdFFJhanLC8otnUd9PK4j7d4Du6SZcPWngqsg0QDWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90114" target="_blank">📅 00:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cTC-gIQ-IjxRbGOvmiLBxpIUlDOijI_rkt0-3M_bfJd6yPnZvGrhJ-ctIzzYangQM4gwL_j7XpIQv6lBWR7zEbSOpIeuyGyO0oVDp6EdUJ5EiOwQd4CWKmT9-5IceI-DCEB6kVIUBPYSfrUsbIjpUVUTirlEJfCQWO_14Dl9u_ssS-r7nVLhMAnQT3iKm7QHnU38cOrdQU6b49VDhklcyPg2yEtkONsUC0JL3GeKpZSHa5SLjMsD8S4WEENVaEJNzbQGqoiBEUFco3c1TX91IKRSMqHPD2igP4guUMkfSvqL3VRM3i_N1cR-dvX_Pa_-3HHfuDwjApKrong2TdIpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90113" target="_blank">📅 00:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwhSzVL6FhaYUDoMRW7KNxtK0RwFUwyH63zu_1UDERuAg5UXjYiCYyliwFuHah13GjzOvcKIRY4kfrncJ2XBoJpvUH_eYZrVlWKw1tvqXDKSAE-jb7CBhNgH4NlkvjGVsCNAhO1cAYrWg0vMzEFJUNtZxrvyTPRa8ckPgV7_wtyF42yAk5OHCNgE851i-ZKqH8G40-QiMR66BqQCO15QB4KC4JsMk5L8777tCcnHZ4EatcVt5XynPI3iNPxZv9TLioJwNQhBGAADKx4ky5qYTVp_LfqcuvSf5kQD69eo5tfQc8F6u4HkA1zdswl2ccxYwjEKs55PWX6060npEVwMDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYXQqy8Ic-lpnU9xv7eYrzF62irSym_Z6uFqQslc2URgdmJgtxFwDfgvFRsovDey_bA34AgAqkn1mkzzD-1mxV5i22jcLUzTEAFpyX43lAamu-9HHLafOhJyzoZw1Hx_5EyQV9voFDyImTqwXcws1PDGkAUIWbbby0slOWLNN0_YJ5BB5w9prDAK0LeRhepduCltLwREHKh6WLHbN2XQqrPjMh8-n5XKElLPHQpQpzAa6KG436T4oJ9wmfIs4AJrU5ZheguG4hIcXfCi3mQycsQ1W5oASUPjlXTcnMeT-jXfNlRDvr3uOFsoFzUibFVnwD8KuficMeEEUgbFFk9rcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔵
مجوز حرفه‌ای باشگاه استقلال برای حضور در لیگ‌نخبگان آسیا صادر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90108" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAlEZ058c_Qyg7Mj7EVClEoeCfwqANdMFrjY0VEq7Q2sIjYXxz0Fji-AqCTloPrGShBCX4WACyjElL5THcQPACxiH9fXRuWbkIvyK8kcyQvFLePU-z_sZZsL03RsEIt7BHqClmjqkaSa2-OrUkgQUd5UJn5ezPVVI9OAOU9U9Y8C3lmnIetBVwkAzI3zazn0kfXvDuLctHiFPQro5rvCX37GQxEn_zkmzPx0W7pm60d4bdh-MuNxfFsn6kwENb4ed4228Uy0VHnbKAiw1pY2r6gkhZw5elYZqL4NU0bvNNdaE-BKd5uqKHSt4JeNmP5JjINWen_1CJY8CB8s-a3BCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کریستیانو کریستیانو؛
همان شور و افتخار همیشگی؛ بیایید همه چیز را برای پرتغال ارائه دهیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/90107" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90106">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90106" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90106" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90105">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiMmHclv4LgjZYwhMfnJzOj0xS4Agw3eo42YPNtc-bPXLmHUtRW75MuHwyP_z_FtF6iZ5OJF8HPyU_7JgCS0cfvqcwHg5va1lJ0EEgZqI_gFgcjNIWq5eRj9uvJAcvbikUrudHjuz_o8Aw9HX8WmuqxJ2Fc85Y-uWlwhxb8DdUt7IkTbyXxeGGz9k5uqXMq9kXmKTfu420xj5rkZ0PcVc_x6T9F9kOMgWHLAb0FGUBkrFYNItaZO8vm4BFx_Pd3id-yYJ42Y6vdo1SPy5Oc-TTKpJE1SYVxSu58VKTuQWPp748i5YlglX3EC4I2EN8G5k4ImSChiqo_z6zVpUQ_kSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90105" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=JDILc4ZOJ7pG-OS3YlkJpl8gG79P4YBH-xu8tRhsjI-katMv1Oi3vNUYP2nonc8mS64fr6bEnGxRzNExbq0LWA4wRx7vqi-nyv7sTxFIWLin4CdXg0XKgNftUNoMpMn-HI1KrzVZafH_OinbyUE2eKD3RTC64bXWSrwBjgwgNEvtrpLvLKk9V115egWQuhvO6w1GUf89inJUW0qeYGrbD8u7m4-znEVLSpuuE-UocPYoMXIkPcLzmi_cpRw32yGtFq-iHsRyGpa7Cs8xeHFlLH22AIB5wWn49uqiNn3VarOopB-x3fW9rlwdspU8mNp7ooFDX3RTDUkHsZm0tfVSYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=JDILc4ZOJ7pG-OS3YlkJpl8gG79P4YBH-xu8tRhsjI-katMv1Oi3vNUYP2nonc8mS64fr6bEnGxRzNExbq0LWA4wRx7vqi-nyv7sTxFIWLin4CdXg0XKgNftUNoMpMn-HI1KrzVZafH_OinbyUE2eKD3RTC64bXWSrwBjgwgNEvtrpLvLKk9V115egWQuhvO6w1GUf89inJUW0qeYGrbD8u7m4-znEVLSpuuE-UocPYoMXIkPcLzmi_cpRw32yGtFq-iHsRyGpa7Cs8xeHFlLH22AIB5wWn49uqiNn3VarOopB-x3fW9rlwdspU8mNp7ooFDX3RTDUkHsZm0tfVSYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ترامپ : الان تو اسرائیل ۹۹٪ طرفدار دارم. می‌تونم برای نخست‌وزیری کاندید شم، شاید بعد این ماجرا برم اسرائیل واسه نخست‌وزیری
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90104" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=gBzyl-xB0-rt-juPGTDnRLIHa6zrvNaMfUUeZHLH43demPWk-EAz8GtW-ZCIOVNJBaAALrek6gbU9ImCOGNa2848_Bk7Yrzsq0ARBWsxsv_YIaUl2oyjWUcrtTFfQ4rc-bpd9djD1dzaKqZN1vPMB4ElQLCfaBXlt8Olk5gKi5B052HL8QYkKG9OXGlvw9rFbf-CUwpSJgVTP841u0xCKZJq_1cFUfOFDZ4HxxR8OV8eP4j0aXzpaHB4deqRSnbbquAlNjda9LB9SOpAXriPmTUm3SRU_Bi4o5m6SFyLDuGThmu2VV2-QkjPSp1R2HKeIz3QADzuAlfSyD1HmsByEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=gBzyl-xB0-rt-juPGTDnRLIHa6zrvNaMfUUeZHLH43demPWk-EAz8GtW-ZCIOVNJBaAALrek6gbU9ImCOGNa2848_Bk7Yrzsq0ARBWsxsv_YIaUl2oyjWUcrtTFfQ4rc-bpd9djD1dzaKqZN1vPMB4ElQLCfaBXlt8Olk5gKi5B052HL8QYkKG9OXGlvw9rFbf-CUwpSJgVTP841u0xCKZJq_1cFUfOFDZ4HxxR8OV8eP4j0aXzpaHB4deqRSnbbquAlNjda9LB9SOpAXriPmTUm3SRU_Bi4o5m6SFyLDuGThmu2VV2-QkjPSp1R2HKeIz3QADzuAlfSyD1HmsByEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدایی رسمی برناردو سیلوا از منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90103" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252c545abf.mp4?token=KQ-c0mD2vqUid_7WXUk4-rtPMlsaW6g6Keb2BD8VAAFK36l9C2WZaXbJ9Lgjcfv9QmGlY2tOprNDbgyx0UMc9VKxtjUhvTdCcvmwdtYQwQSXGnnPxheT0qYqvf8mcbTMBvOy5LPCccUIK84N8glNVEpif7SD1Jw_nV5h9JbRiTXMI9GiaR3ckQXWyForFhcygjXOgeQPf4-OxB1UfjuAjehhB3qiIpdnuuuXKKyK0L8FOlezuzF2lRcwC_DKSuurObn49PJdozwYC7yHEq3PcYwbnr0WfRtp0wMBYOYZXiuchsjlNQUzv2mGO03rVU5SlwEX7qwWpL9E5qRzE0MetQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252c545abf.mp4?token=KQ-c0mD2vqUid_7WXUk4-rtPMlsaW6g6Keb2BD8VAAFK36l9C2WZaXbJ9Lgjcfv9QmGlY2tOprNDbgyx0UMc9VKxtjUhvTdCcvmwdtYQwQSXGnnPxheT0qYqvf8mcbTMBvOy5LPCccUIK84N8glNVEpif7SD1Jw_nV5h9JbRiTXMI9GiaR3ckQXWyForFhcygjXOgeQPf4-OxB1UfjuAjehhB3qiIpdnuuuXKKyK0L8FOlezuzF2lRcwC_DKSuurObn49PJdozwYC7yHEq3PcYwbnr0WfRtp0wMBYOYZXiuchsjlNQUzv2mGO03rVU5SlwEX7qwWpL9E5qRzE0MetQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا شبکه‌اجتماعی غیر معتبر روسی با این ویدیو مدعی زنده بودن علی خامنه‌ای شدند و گفتند که به این کشور پناهنده شده :)
❌
سطح اعتبار این ویدیو : 0
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90102" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
⭕️
⭕️
🇪🇺
تمام باشگاه‌های لیگ‌برتر ایران بجز پرسپولیس و گل‌گهر سیرجان با ارسال نامه‌ای به مراجع مرتبط خواستار لغو ادامه مسابقات لیگ‌برتر و مشخص شدن تکلیف نهایی تیم قهرمان و سهمیه‌های احتمالی شدند
🔵
این تیم‌ها با عنوان کردن مشکلات مالی و ...، موافقت خود را با قهرمانی این‌فصل استقلال اعلام کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90101" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hvdKGhc2GT-h0yqrG_4anl_gsm8PP4qVngrhAPUFgABn70-C3QvXmiT0EDF_DpLmxM2IAL4bBH9VnYv5so7gV9cuTp7DMDWbyMdXyAfGx1muPieKYtREd64_ybtMvuxi3_U_zCF5NJA2YTCLH2nKL7QohlUdauE3lngs4bJ2wcrGI4_D0FEy7dfNuUDkSBwqCfPVwiOBSl2Gvi18kMrOFy8jM9ULX4ItOQl3ZCuKMC5YENXd7kw6abNpwm7u6P6IEeHM12sph72EBvBw-BSV1s_LN978PVtoug7DJJwkogPEV0gzaThy2aap0flbbH3OC-WogR3SDaKT0UNgkx6H_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eavRxWcV8lWEPI_Jsof70RHxeTC-1tbNw7327r27P1RfV7BktH2HFlgjocz-d6fLycRMxNBw12YlP2ph6zMx_uUouG57tUlH7naxP1u96kGxvKyRxkRI86Yl7L7RhsQXvem-pCJyGFUaLQcwvXtfdL1rv5r8DZeG2JmDS-EQX5vX9kJcpyKY9HQ2_Ym2ZaYC2Cgaasu9Z-FNdZULLS4f8HhNyKc0CVsdGa0DZELeVjIk4kxgwqijefeHngT9TQ_61Av6WjiMz2myRxslvd8N3LpBRil_sp5y09YRH5VN5hWIzE_UOVDkERDUw9ObLNNvWyc7bzeU86n0dF6bl27SpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینس گارسیا بلاگر ۲۱ ساله اسپانیایی و دوست دختر جدید لامین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90099" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
⭕️
رشید مظاهری سنگربان شریف سابق فوتبال ایران در حین خروج از کشور در فرودگاه بازداشت شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/90098" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90097">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=Dba_5siafDVi7V4CAo2gWyUx7xSJuOhmEFW7J1CahYSR5RHRc1GgU8EQrAkPwwthb_iS-D-9sNUBDELZV0r9gsdzY9SyaR0VNuOIxpf83T8AYeBRiZJFIn86mqELy-OlP1lNluGTc9ikfYqDAtCTYS4FCcc0CIzcVFyNNPInLICIqR-4d4kgbJN-snsbOHrEzc1ylGn0AuFD8D1tE9Feh6M1nTBL7excQO-93iONM7qirv7FZmebGwScoflf8_uvCTzDOS-ERJYEeaYDOIE5QGKXT6IbJVm9Bci1DGk6F02aQoYdYzs25ufZIEPjS5GqXLuo_ZgKMLvLsF0Z_JUtYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=Dba_5siafDVi7V4CAo2gWyUx7xSJuOhmEFW7J1CahYSR5RHRc1GgU8EQrAkPwwthb_iS-D-9sNUBDELZV0r9gsdzY9SyaR0VNuOIxpf83T8AYeBRiZJFIn86mqELy-OlP1lNluGTc9ikfYqDAtCTYS4FCcc0CIzcVFyNNPInLICIqR-4d4kgbJN-snsbOHrEzc1ylGn0AuFD8D1tE9Feh6M1nTBL7excQO-93iONM7qirv7FZmebGwScoflf8_uvCTzDOS-ERJYEeaYDOIE5QGKXT6IbJVm9Bci1DGk6F02aQoYdYzs25ufZIEPjS5GqXLuo_ZgKMLvLsF0Z_JUtYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی گابریل مدافع آرسنال با خانواده‌ش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/90097" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90096">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90096" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90095">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2-ywKl_V52NwQepr_gsdIKEdzljY4Opf1fLAw8SRIaD_YJ0rkvmDPjjGjSVeAJivqv0ka-DLfGomWoRsnzNwdTi4CBgc4g5hmm2x0ND-fT6yzfmFqvznZLlZG1VpsbYO7kLiHYUeBOqRUrYU1v5j7TVoGs5aEC3wFASrk0BtVDC5nCxe2DVZqRjciy-Y38SfLjDva6RKsiTV0fgO72rExclYEvUCXmUJ3J5hjpB8rieIIXb08yMFndD7kLsSr7OcGQUx4iV9RtxnYjhxtTObpyXaVZ1zTvkHiDSI2fMB-AuC2z3esBIcaO_gWCRUFmENGBH5iXXeUn_a2aQg0P62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Ole, La Liga:
بر روی رویدادهای مسابقات فوتبال لالیگا پیش بینی کنید
!
💰
در ابتدای هر هفته، یک پیش بینی رایگان دریافت می‌کنید.
✅
هرچه شرط‌ها بیشتر، پاداش بزرگ‌تر!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90095" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90094">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQHmKww_IK9FFz3EoofPoItXGJGxE6hnMF6cajWdtC7nCvftbpL0m6f0x8H9Zta_5C3E251eH3UOxVmQJ-h7UfFHElqpD-Nls2x3w8mqTurnk0j8TWPLm6NAkXVu1Bj0romrKYu1HIOfOmR6lixw89WEqYqFHOnjou3BYOOxNxyDvDcOs3-01kwAALfmOdMB9qMoB6-GpAhlilMuoUmgfi_hCcOyT4ngQl7hkRuvUXk91mbYHxNQlccdIZFwlSNXOeEeKrHV4_SK8o83mPUDyOhmXzrJPEE1Axhz_ipXrV9nfJarxp_plGnjFjZD8SRNUvoBGbAEEz9ij4MKCNIOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
توییت تاجرنیا در واکنش به شائبه‌ دخالت غیر فوتبالی در تعیین تیم‌های آسیایی: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده نباشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/90094" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90093">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56d546629.mp4?token=nWj4fvVX8odPOEVv6t-oyNZObfcQ0gi5Gnb-tUKr-n9HS_vUqWp40msZalhylIK7Dd24clbVSOwyQiaCbNxoJ2R0ao0xIkGoME3vh6Ardkkqw-4MZvpeHX3qFjXK-CCd4YSzXDlRA582P_YD0b33rKwrRO61S102gREvCxZ_-crX_4m2dmAqT-I0OAg7Z3ODi2ooRDTR7GTIPndLXARbwI2aoHWPgvBTGPzQkBEVciBBmfd3NGDrX2ZMXz2XGlpcyccfwY5aK4nTKEypfsPclUVjZyDEBretP1au2RCs6d_vRPFTzZ46GuFzwF5plZCvPHMYPgMQ3NQjQ50PsX2Njw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56d546629.mp4?token=nWj4fvVX8odPOEVv6t-oyNZObfcQ0gi5Gnb-tUKr-n9HS_vUqWp40msZalhylIK7Dd24clbVSOwyQiaCbNxoJ2R0ao0xIkGoME3vh6Ardkkqw-4MZvpeHX3qFjXK-CCd4YSzXDlRA582P_YD0b33rKwrRO61S102gREvCxZ_-crX_4m2dmAqT-I0OAg7Z3ODi2ooRDTR7GTIPndLXARbwI2aoHWPgvBTGPzQkBEVciBBmfd3NGDrX2ZMXz2XGlpcyccfwY5aK4nTKEypfsPclUVjZyDEBretP1au2RCs6d_vRPFTzZ46GuFzwF5plZCvPHMYPgMQ3NQjQ50PsX2Njw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: هر کی جنگ نمی‌خواد، جمع کنه بره‌‌‌‌...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90093" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90092">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🟢
باشگاه آلومینیوم اراک بدلیل مشکلات مالی در آستانه ورشکستگی و انحلال قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/90092" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90091">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=tTD14r0GdVZyy66aUZ-SQdIKpw6OE2zC3P5AUziAcL3sPZcou5pAO3lNyr4RlAS0ntyteukcCtLT8LGibBKyOHHIjIyZS2ys8crhjTBppfGywseqpMAQis_Q0M9dw0YQQ-doumhEQVGm3q6obhBwDxx4dC0tq7MfSAyXd7FMhvxQ1iXdBFNdfVtOvhdgbYHFLV670Vh_f1HUJJ6iM7bal7P7FnoK3mHJ_72rf2pkQDobWsX-9XRC_dwQemDcanMXw31ndgWSUYTHZdOO5kTFvYYrZzPH3kpSU-tVWr4ZvQo-_gs6s7Qi6MRMk79vLS3bL1TIKfducdtBm7l1xBKIqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=tTD14r0GdVZyy66aUZ-SQdIKpw6OE2zC3P5AUziAcL3sPZcou5pAO3lNyr4RlAS0ntyteukcCtLT8LGibBKyOHHIjIyZS2ys8crhjTBppfGywseqpMAQis_Q0M9dw0YQQ-doumhEQVGm3q6obhBwDxx4dC0tq7MfSAyXd7FMhvxQ1iXdBFNdfVtOvhdgbYHFLV670Vh_f1HUJJ6iM7bal7P7FnoK3mHJ_72rf2pkQDobWsX-9XRC_dwQemDcanMXw31ndgWSUYTHZdOO5kTFvYYrZzPH3kpSU-tVWr4ZvQo-_gs6s7Qi6MRMk79vLS3bL1TIKfducdtBm7l1xBKIqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
واکنش تند مامک جمشیدی، خواهر پژمان جمشیدی به خبر منتشر شده درباره صدور حکم پرونده برادرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90091" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90090">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔥
خیابان‌های لندن در تسخیر هواداران آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/90090" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90089">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSy7-Pvx857QJj8ZdeAEPW4CB_orvzpcW-BR4RbnVvmxjhrZRuxkm9zlg7ngUXT7cRNtZrJ8cWmZ8mV8dWy39cX0jopGQ_CItdEFctYDu7mF0NheZN7b5JrjXa_InLVSBFze6jq28UAuJuY3cLgja9LZ8kOz54P-oyxI0UPHON48tViJEpGCxBUIYAnSV4H-PSLrzGENXQFQqFuYT5onnwEff77cmEWsMToswsx3Hh67jtiWPkImfjp5Vn6V38JseasTLmNXwVNOBnuvkBcjK_mOOfKGEvosyfcrUMk3oHhV7ajsfvgC9i32WOG7hXQz8qNhvDZ3I0wmD8x597aGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد مسی، نیمار و رونالدو در ادوار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90089" target="_blank">📅 09:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90088">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=BwpciaT-WT9f4dni4oQs7yjQSOVBR60UtzUbkVNDz8K3Z3mR39EkgQQdOA7bluDi3UtyFZXyiJanosxyB_mQxZL-eLv1xCPd7nrtccPVLPmOZ4XeRFpCvAxupYJozq2c9LkpHieUVhIMa2HvclWgm3z7IwLUtcFFEpaKbVC5NiHD9zRsf4sndWMWuY2Wp_urfqpuPxR3nS7GnHRZrha0-0e1IpS587Ru0PpH10mcdvLSqjh18EuC_b_-P1qFzzJltBi7FmufRU6N2rsVo6yX-cftUDHIPekZFsNc6se1L4CXBfIYP2rWmVe0fXXHMqzuPaauVaFyclV2RHNZpA5RJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=BwpciaT-WT9f4dni4oQs7yjQSOVBR60UtzUbkVNDz8K3Z3mR39EkgQQdOA7bluDi3UtyFZXyiJanosxyB_mQxZL-eLv1xCPd7nrtccPVLPmOZ4XeRFpCvAxupYJozq2c9LkpHieUVhIMa2HvclWgm3z7IwLUtcFFEpaKbVC5NiHD9zRsf4sndWMWuY2Wp_urfqpuPxR3nS7GnHRZrha0-0e1IpS587Ru0PpH10mcdvLSqjh18EuC_b_-P1qFzzJltBi7FmufRU6N2rsVo6yX-cftUDHIPekZFsNc6se1L4CXBfIYP2rWmVe0fXXHMqzuPaauVaFyclV2RHNZpA5RJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
رختکن آرسنال دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/90088" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90087">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/Futball180TV/90087" target="_blank">📅 00:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90086">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQqS1qlhpUTFyPFb2lQGWsCKfYkYw5rd3999Wc1MyEH6uni8LMtXehl7_Z29HDVIBBMu4Qa0DATxE-LEAh-5KMdvosD59-vBdrclgnKESVwy5MuvV4dPLIg9jDjMXi4TDVUpahlTAn4FZflOHG_XPI42MGwWUEwMCaFs2aRISqYBpRr6y9Fnr6vD5uTYoEmBdunEccwTf6VO0wFDLRb4Kn_8uLXXioCpT10azkBnMmq5iB2gnohNGwQROtIQZK8qGxeyxAfufUNSzPAR_HGLorInrxMdyw8GekvfW4B2Mp6dIHXJgTrNb2DRWnqJwEdLa7XWxoFHjXeG_SyFqMHS7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال لیگ اروپا
⚪️
فرایبورگ - استون ویلا
⚫️
را در 1XBET پیش‌بینی کنید.
💥
بونوس صد درصدی 100% اولین واریز
💰
پیش بینی تکی برای بازی پیشنهادی قرار دهید و در صورت باختن پیش بینی بازپرداخت تا سقف ۱۰۰ دلار دریافت کرد!
⭐️
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید .
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90086" target="_blank">📅 00:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=lsGRtr3uk0zg1LslQvC28AlRJeBHgKGp1S_wQ70G5ep9scmsa9S-jmWzQvXl3Vu7-mrrJV1Gq6ikvMUYXTMD6bbmZxz6BbnqmZ3vTeqW5rXbhQBioLDppBuNigEX-Ua7L3OIZfA81ZBorLlyi5h9L42eL215ParEqT3ibqQ7jZSL3Xkd1KuaV7V_81FyKUDlUQ5xa3MvGqNuQ4KSXAxyfwG_O9TzcQRAGp26I5FSv14_uSLDgUlWaRmv7LuXcYqM_ptzHigabARjpUO1CTJ2fx8uY8CFYmB5rtMDsr7L9LB_OGJt6W3fuzyORntYRnEpoIvqBmf25iAKVtpeSk59Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=lsGRtr3uk0zg1LslQvC28AlRJeBHgKGp1S_wQ70G5ep9scmsa9S-jmWzQvXl3Vu7-mrrJV1Gq6ikvMUYXTMD6bbmZxz6BbnqmZ3vTeqW5rXbhQBioLDppBuNigEX-Ua7L3OIZfA81ZBorLlyi5h9L42eL215ParEqT3ibqQ7jZSL3Xkd1KuaV7V_81FyKUDlUQ5xa3MvGqNuQ4KSXAxyfwG_O9TzcQRAGp26I5FSv14_uSLDgUlWaRmv7LuXcYqM_ptzHigabARjpUO1CTJ2fx8uY8CFYmB5rtMDsr7L9LB_OGJt6W3fuzyORntYRnEpoIvqBmf25iAKVtpeSk59Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارجدید حمیدسحری با کپشن:
تاج‌گذاری میکل آرتتا در لیگ برتر.
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال قهرمان لیگ برتر در فصل 2025/26 شد.
🥳
⚽️
Channel:
@Futball180TV</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/Futball180TV/90085" target="_blank">📅 00:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90084">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8Fh2t_bwXwbAijhEod0kWlw6QvVV9zFlvgDVinm3qZTCbSlIcD0FkLSN2xXnbvu_XoSvd-KuiYKWy2-8tck3cD-j2-qNa6HCdKT-H71fLFI6UdoC70m3UVrZBoGaV44-j-8XrV9OVjzI4A58ROpGh5Q9ZrVu0J_jWwzoCJxbGSV5cHiRfvebHD8nQdc79oNxvQzgFCOrqC_WTeCooC3W-25QxxZC_tN2ro3_hkZSHsRmV1vmMjTQSwCZ9iAsLb0H8OH2f6gEX6hsKlpkueRgAfCbzVSbp8f7-JJkk0VhByPkJEWcybYSlYCYPTyM9cYgqn8x9b2YBkBmxvYjQy3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرایبورگ - استون ویلا
🏆
فینال لیگ اروپا‌
🇪🇺
⏰
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه بشیکتاش
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
فرایبورگ در
۸
دیدار اخیر خود در لیگ اروپا مساوی نکرده است.
✅
استون ویلا در
۱۳
دیدار اخیر خود در لیگ اروپا مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر فرایبورگ در لیگ اروپا
۲.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر استون ویلا در لیگ اروپا
۲.۸
گل در هر بازی بوده است.
🧠
وقتی پیش‌بینی برای فرار از فکر است، نه برای فکر کردن، خطر شروع شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/90084" target="_blank">📅 00:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90083">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/Futball180TV/90083" target="_blank">📅 23:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=uRU4ZvS-CsYD_nlqFIj80Nsr26IIPwktwbtk9v1yVGyEMlTd_hcHr0K46utSe_iTKYJ0ObEeOFWY_i_AaKKPV6jxqaOQgkA-LoCRFZ-Nk9jmFfN0ITWJJ58BCoVw7MyNVAd3aiF-5t0TGRc-qktnISxQrmDPHe5dO0BohZI8kxw9bDqOTYq4lPV_dbyjukc8PQKBR9HCfHOixgENWnOzqZ7PdZXjpUIbHg01K0OiInzdjQ67ArZvu-Mdm3g4e289dyGb6SNOu_wLmaO-A7hOxU1HE9x4w_RYvMFWJwK_sHWh7r25dHx0OF3T_LH8QgmKyTZ0J9drT98CMxkPn_Mtxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=uRU4ZvS-CsYD_nlqFIj80Nsr26IIPwktwbtk9v1yVGyEMlTd_hcHr0K46utSe_iTKYJ0ObEeOFWY_i_AaKKPV6jxqaOQgkA-LoCRFZ-Nk9jmFfN0ITWJJ58BCoVw7MyNVAd3aiF-5t0TGRc-qktnISxQrmDPHe5dO0BohZI8kxw9bDqOTYq4lPV_dbyjukc8PQKBR9HCfHOixgENWnOzqZ7PdZXjpUIbHg01K0OiInzdjQ67ArZvu-Mdm3g4e289dyGb6SNOu_wLmaO-A7hOxU1HE9x4w_RYvMFWJwK_sHWh7r25dHx0OF3T_LH8QgmKyTZ0J9drT98CMxkPn_Mtxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💙
سهراب بختیاری زاده سرمربی استقلال: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90082" target="_blank">📅 20:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8K5GAMABdfDSmlmd65N_60pZDc1I20j3byP0VDHrIP3F4TOVnDnQ7-X36p60PXTRFpD0uereRM22R6KgN_xqWK0l9HIPKCapWNkG41Z44M3FIbuBseHzThMDzpn2sHb2tdh_7DKOrpjWqdSbT5VqSXiPAD2VWQRNd_B9bO06S4GU-zPzH5HJG5J8QYs_Hcbkel8vgFNIaxnVhoaQN3yIQXX6nbY51zcBnQrxaw-yHN8o5YPLsTgHjFTPYuPAJVmO6-xLLYxxZhTrqALn7Sezzygn2kOwiQqqwee4vV63R2g9uMlfR6XiU-wOS77aLGiC4vukMkWcK3mrTEp-pvPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
از این منظر نگا کنیم؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90081" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90080">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90080" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90080" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90079">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MyFhjpa0E1M84rDDfc2yZaxj0GnI-4_oI77JoBzvqwoSg1K7ogEJ9VBDGinvEykjwnSsBwHJwFGLH_v0WofUa-VGZf7vxgPoJUzY0np4JnUf0Fs9Fi1CjEott-75LfBUNMVdiyUM6U5zx2SWGSbemLr97Z4X-7m-eUAbBGqZknRJng_xl0sPFuiSRsWt-9DyiQcwXjxcPAvFjXzfFlEsc0etO7PV2zpvl-gVRCG7dDlldO5ZWRHeFEcs1B1AF_x6f2MlXnKBwMlrKk7AOvRSbgHsc9G_V9P8HR-0-0L996k9XaFs4CEzUJXW2Kfdx3OrDCLsnxfOVlV48QTXwK7GXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
قرارداد «PSG: Champions Contract» خودت رو امضا کن و با قهرمانان واقعی یعنی پاری سن ژرمن و 1xBet درآمد کسب کن!
💰
پیش بینی روی PSG — جوایز تو در انتظارت
⚽️
🏅
شما در
Level 1
می‌تونین AirPods Pro، کیت خانگی PSG و جوایز دیگه رو ببرین، و در
Level 3
نینتندو سوییچ 2 یا حتی iPhone 17 Pro Max در انتظارتون هست!
😎
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90079" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=gEFmT1u-Hy1-0Fki4f-sR2BsYuJTVq8NMl-BXvxeEZVr6HcM7fbC6noEniEcGzk1iDqEgNbuE6DPRYXw-fIzQoyeijC5-ZgkPZ2WwS8b6wMXVla8Rb2ZvPuzMi4w1YTOYW9KR_XRAMblhB3fs_QTvm92rkanFYm2wK32Ow2N71kwndH_Ovr-OIijXl48ToGwKOV5XLME1BlKSa0aBe4pr837XpnF5EQLNhY8gPyOcylzUQU4SayNbQUR9XEFjpAb8Rs0tChE-MLgJ0WMFxfIthLA39Mn8FwD20c1xQciOlTsoWG2omaB7kDm-GTWH5hUvdwUXgSWXh_NqvhmeNfPEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=gEFmT1u-Hy1-0Fki4f-sR2BsYuJTVq8NMl-BXvxeEZVr6HcM7fbC6noEniEcGzk1iDqEgNbuE6DPRYXw-fIzQoyeijC5-ZgkPZ2WwS8b6wMXVla8Rb2ZvPuzMi4w1YTOYW9KR_XRAMblhB3fs_QTvm92rkanFYm2wK32Ow2N71kwndH_Ovr-OIijXl48ToGwKOV5XLME1BlKSa0aBe4pr837XpnF5EQLNhY8gPyOcylzUQU4SayNbQUR9XEFjpAb8Rs0tChE-MLgJ0WMFxfIthLA39Mn8FwD20c1xQciOlTsoWG2omaB7kDm-GTWH5hUvdwUXgSWXh_NqvhmeNfPEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
۵ صحنه بامزه از گزارشگران عربی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90078" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=rF-7cguCvFyWuun6Uu68-dJOryxjrXr4PZ49KbamI3QGev-ye-n96krK18YPeLHGUi7fYY1aTrmz_agDuV-H1LH25AP0TDVnziBL1nt-nHQvP3LSPQlvP11wDI3q6XMIlnZa98v8Z3VTdJgewJjPOX5ei70VHMQduWRE1XwKkR0CPW-PAZ4Fsefc1JB0E-HhV9xCna0dThbgu-Fl7ew-aF2eRaabO1XIg-nP1X5DMU3C6AWdIKSkESKkt2k4Cneax2NSm0qaCfnNSIEzJiFNF95kKb1VJQPm4BochkWEp7OTm4tCLZNq6fJjvpiG12BfaGqoSiu4c35RDCBV8lhLxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=rF-7cguCvFyWuun6Uu68-dJOryxjrXr4PZ49KbamI3QGev-ye-n96krK18YPeLHGUi7fYY1aTrmz_agDuV-H1LH25AP0TDVnziBL1nt-nHQvP3LSPQlvP11wDI3q6XMIlnZa98v8Z3VTdJgewJjPOX5ei70VHMQduWRE1XwKkR0CPW-PAZ4Fsefc1JB0E-HhV9xCna0dThbgu-Fl7ew-aF2eRaabO1XIg-nP1X5DMU3C6AWdIKSkESKkt2k4Cneax2NSm0qaCfnNSIEzJiFNF95kKb1VJQPm4BochkWEp7OTm4tCLZNq6fJjvpiG12BfaGqoSiu4c35RDCBV8lhLxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
شادی نیمار از حضور در لیست تیم‌ملی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/90077" target="_blank">📅 17:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90076">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bmDg_O4Xu7pjyaCM1_MIEQK6fF-Fb1_a4CMm4OB7cjWsHOwrvk5dIPl7MMnjC6hl5Z3ncbDpkorLHXT8U0OuAypVLFNvFOSYJ82FlXjTZlIsqA3TEY43TCNR-UYA-znh14wWvqPXDjL02xNSHJzS1VSPbUy6XmK6s-SusS99Shwoxcv3ioSdFWzTk7Z5S2V8lENxxIf2iLEvAdtrYSjleqD-aGk4ZiIr_r_3xbEY-W1BEk86DIf_oztBNeUDov03QY9Nb5V9pyAopxfzIhrDqwlXwM0JlTOcZv8Vhx7Vhk1GLVM5PMk2H9hx3QEHuUCYzopEeQS6bMzj2MQ0lwS5UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
لیست تیم‌ملی پرتغال برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90076" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=Id9gIEwwy5Xvgd4Qpg6OQu-rzPP1owiwvusW3wIox_ti4gW97PUw4kXAY_LrZY3i2Upd99PhAtLTzKqoqPrkwHlQdpuGWhQ2oj61klpBF6etOhkSS2Qowq_Hw7GslHB25yngAi7CMfJVCOUUYoGtGyQlBaJdMBbG0OyK1Z9h0bgDMpfAtr0S754QLFjKDAFWP2lDG5xJLfJDiNw-K7UD4CxwM6sTL_N-qRbe8th8ap_Dvjw0E5Txh54HTGAuf22NT0x_0R9olmNygPNPe92IBlWxc3kMY9x0Zy1X3GOa6XaQEwwX_Mus-eEB5FER9TqyxIGjLFCSXGffv7tQKXRqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=Id9gIEwwy5Xvgd4Qpg6OQu-rzPP1owiwvusW3wIox_ti4gW97PUw4kXAY_LrZY3i2Upd99PhAtLTzKqoqPrkwHlQdpuGWhQ2oj61klpBF6etOhkSS2Qowq_Hw7GslHB25yngAi7CMfJVCOUUYoGtGyQlBaJdMBbG0OyK1Z9h0bgDMpfAtr0S754QLFjKDAFWP2lDG5xJLfJDiNw-K7UD4CxwM6sTL_N-qRbe8th8ap_Dvjw0E5Txh54HTGAuf22NT0x_0R9olmNygPNPe92IBlWxc3kMY9x0Zy1X3GOa6XaQEwwX_Mus-eEB5FER9TqyxIGjLFCSXGffv7tQKXRqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدا رحمت کنه زنده‌یاد علی‌انصاریان عزیز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90075" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1631168f15.mp4?token=YAH42JFws4ueLVQ8wCjuLTztGZZ-Sp6OFj3lf2du9zPrnw1pa2Z6gpugTwPVTE82AuQcmJishg8Uxb_1VqtZK8lRsv0bcPqtaiTUB4DDHtG1Zn9pFMga5aZe-zm4AgSA7EtqSH-g7MPcW6ztUCtFPhdfDaMK4cnhjBamdS7KgCLaCwaII2LSSaO8YNuW53Rk2DFr0QOxApdCoUlfQWIavmvcp7m8aBofyF7c1Ey28Ty5-Wo80UqcnL4_Q-nkHerY17cze8WBIpbumjRtIY0lSobf4nII5bTmbpdkSnw3l32-M0nIyjKkzDjWcpSzODdbGcnjUVcPonwoen3nDc5lXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1631168f15.mp4?token=YAH42JFws4ueLVQ8wCjuLTztGZZ-Sp6OFj3lf2du9zPrnw1pa2Z6gpugTwPVTE82AuQcmJishg8Uxb_1VqtZK8lRsv0bcPqtaiTUB4DDHtG1Zn9pFMga5aZe-zm4AgSA7EtqSH-g7MPcW6ztUCtFPhdfDaMK4cnhjBamdS7KgCLaCwaII2LSSaO8YNuW53Rk2DFr0QOxApdCoUlfQWIavmvcp7m8aBofyF7c1Ey28Ty5-Wo80UqcnL4_Q-nkHerY17cze8WBIpbumjRtIY0lSobf4nII5bTmbpdkSnw3l32-M0nIyjKkzDjWcpSzODdbGcnjUVcPonwoen3nDc5lXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی شدید خانواده ژائو پدرو ستاره چلسی از عدم حضور در لیست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90074" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqbaBH22pHQv5oF_sQw3P8pDLhvik5Lqy97-auIkRbol5FhlPlPhTw-VtU0KKaQMlPGvqsFejzTcY5tgS4FAHzJ2S3itRp9pQXg4z4PLaUUQsKMpDo74gwIkRrKSMJfhFJXXR6_eHlbFS3E1EVU7TOkN0AGaYJRUyUzAa9rq32aaMEIMGfw7fJisMiRCc1zCb_HDfjRxcYWTjM6XgdELdyGmWbDzDHc9ZmB3pS72daRU14aCcwvpMhLQC_jeTxt3hMBIplsbGPXoceqRKr1jIJ5g94OtGO-enfVCUstMc_S2hV2IrHVz2Sm7-QE67U3iK5L1gg_oEgn5disRXY7CSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با ارائه پیشنهادی خواستار تمدید قرارداد یکساله با آنتونیو رودیگر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/90073" target="_blank">📅 13:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eM-RWys9P-nbPqO4yOuuo7LKnZ-HeEm2tjPUPeWYvs9b49j-82zqatsgarVyVHT2xilfbYL6eGRnxvKBRUMEQWBvhWfED7szbn5CdtfzdO-XiahZdLPwC4db2PF1wxxjZjrmiZ6Ye5ECiFE-Kc53xdtrbAZGYCqSBSxTROYja84UdlxriJ3G3zyz5EblDOl0qIN8a37UMw6b1t-p0kukJ21Z0vbmZGTCWpRb60uUD2uPq8TasI9_czC4kGrghwOD6tyYbVlEDWpDvBzwJPA__HSLYR8dwvNIPTJQXqwxT7fFGM-Dc49kOAgWKWkjFK492hsMhc5fvqYNV-ASzIRFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد قصد دارد با ارائه پیشنهاد هنگفت با لوئیز انریکه سرمربی فعلی پاری‌سن‌ژرمن قرارداد امضا کند اما در عین حال این مربی پس از پایان‌فصل قراردادش را تمدید می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/90072" target="_blank">📅 13:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c098031df0.mp4?token=CkfFCecbrBxN_AIhGdYvD0t1og2EwRmmpdo0nIRCJF_V5XeCLdNRpih4Gaeo6ccGCLUfgxPnD1bRpIvZ56z9-BvwN0QPocmdGNd5x2tcwRyf06oIUIen3aqQ5_TLBuO8t4GSNuqdl-EABEniHbxNHIEucrIVd5QaAMIUoTJRwiUwXNyYoghVcyJ-8zMhrXI5qIYrOvAMycDiN_TT87YQH0KIBfgD6wmwJQx_ZwbflUS0fPomcmUDCX1Bv0eG6RQXTFbZP-D_6p5dsQUC3gVfrVD7YA6rtcqPMegoSfvE0lI3kZb220wdMUVP0wf4Hr8zSeBlv0DrSU98O9rt7_9qLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c098031df0.mp4?token=CkfFCecbrBxN_AIhGdYvD0t1og2EwRmmpdo0nIRCJF_V5XeCLdNRpih4Gaeo6ccGCLUfgxPnD1bRpIvZ56z9-BvwN0QPocmdGNd5x2tcwRyf06oIUIen3aqQ5_TLBuO8t4GSNuqdl-EABEniHbxNHIEucrIVd5QaAMIUoTJRwiUwXNyYoghVcyJ-8zMhrXI5qIYrOvAMycDiN_TT87YQH0KIBfgD6wmwJQx_ZwbflUS0fPomcmUDCX1Bv0eG6RQXTFbZP-D_6p5dsQUC3gVfrVD7YA6rtcqPMegoSfvE0lI3kZb220wdMUVP0wf4Hr8zSeBlv0DrSU98O9rt7_9qLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پاکتا هافبک تیم‌ملی برزیل و دوس‌دخترش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/90071" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90070">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90070" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/90070" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90069">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFR7qivFEyv_0jZALyGDHuYn6wjMrzdHN_b8VOqvc0L_gWB4KF8PHji3vcA1YMyz-6UafrRSIXR7NEtpZwFQCs8tvzb2ReLMVmm0ZoF-5y7U8DB9aTpxudOLLqLN0YHCl6aWqM5_UhWfvQ4jbEeKfN3HPbyBAaCHVToNYIvgY9U5Sp-0jDWNvaCrIB6-j24dgHZUFpab-eKRq7UDQ2Qb7IjtAUKPcy3qsJiq0LLs9zTh9Ftzdd9mZnMhNTd_ui51F_fg3NL9VVYjOxHZoSKcG9ONmDRVYKjXi1h5FsQ3C0XaMLp0kT0RA8yXfoFqOgSdnXE_k_XxiZTImGcsH7jczg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Ole, La Liga:
بر روی رویدادهای مسابقات فوتبال لالیگا پیش بینی کنید
!
💰
در ابتدای هر هفته، یک پیش بینی رایگان دریافت می‌کنید.
✅
هرچه شرط‌ها بیشتر، پاداش بزرگ‌تر!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90069" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQPZsG3wEgXZ253LT_7fLsFlDJ9cPfaGHpQ4N0BN_Qoe4-LIpyfFLCdG2Kj_ZzNYs98cbtSx8PbXo9uScjVju77aRvRN0_BZiqFgf5TC4gnUs4iYrPwu23wAEGdP_Dav_G5Uud7O8yIGJbEK05AEQBOO_ScahK67oJ8lyYYDDlrgKq3ZofNZiqn2CwiHZZMKSxt5qlSx9hASg3yc0v4cob-sgx6jTXKiAIZHaTuxce-OHxDndrRfiIL-b-1YwE_LxiMXkhvfwnZLX4eFM0cFiMM8rjA5r7pem7M3OBX_svySxCq9RQkhkwyrSlUhTda45EIKCZ_FetG3mHV4LS0NKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کیت‌اول باشگاه اینتر در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90068" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKgDqzeCT-X6ylS8b1lXxD7diVJepOX2TUM0NKIgcbWfkmEKIB2SrkmVlQJ0NPjL3ypdVLFInXHzUsGsf_cDONbQsR8lRrrvGdKJPNglZG6K1SW34pJdICRDOcq5q2zB63b3yNo7MEn3ZhQLOy1XNauQr3s9UTFjI4hoNFzggycuDWDv5njgk1-sFbzQStcC2W2AaGef1vyyJjUmW3bo1XGJszByXXsGfSHDK2l3hdAxzwIJL_N2ZFVd_-Jn-YNDYPMNqdxfEmG8ankTkkdwHlyXdrHBLkOXglyiEWWLp2ZCoF5z-7K1706FnwshQIpAfCxvzOUnw-TI4CDMHTIkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول فصل‌آینده لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/90067" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=ikwJYmEe7jaz_gHJsjM1Yhtg20hgLp9vdQpSOpSyPhBnTZar75vs91QxETDiY6G625Fr6s7YRB5Krw3Tdzk9edddRZkRt6LzLRa7TAV-M8eIdCt8RAPgj0DY-Ma8aA_N71WKNFl6GyaTswNnmiM2I6TdiRFx7QVDoO6vP2o8kt-TgXu5CcfyxCf-SU95xV2FT30qkpZkXNBYuc08L0opkwe8Pzbnm_2nIiEr9UXJnaaAwDMfBt2hhhESqKOE4oT_hfst49ftNO_sM-tD4SLUvd49NYLFgRnuGluTVm4GIaAtsTj0pNjq2lT5L9_x0P5DO4h5RzRnmYaZTJ6u4DJcYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=ikwJYmEe7jaz_gHJsjM1Yhtg20hgLp9vdQpSOpSyPhBnTZar75vs91QxETDiY6G625Fr6s7YRB5Krw3Tdzk9edddRZkRt6LzLRa7TAV-M8eIdCt8RAPgj0DY-Ma8aA_N71WKNFl6GyaTswNnmiM2I6TdiRFx7QVDoO6vP2o8kt-TgXu5CcfyxCf-SU95xV2FT30qkpZkXNBYuc08L0opkwe8Pzbnm_2nIiEr9UXJnaaAwDMfBt2hhhESqKOE4oT_hfst49ftNO_sM-tD4SLUvd49NYLFgRnuGluTVm4GIaAtsTj0pNjq2lT5L9_x0P5DO4h5RzRnmYaZTJ6u4DJcYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر صحنه بازی دیشب آرسنال
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/Futball180TV/90066" target="_blank">📅 11:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد آرتتا با آرسنال در پایان فصل به مدت دو فصل دیگر تمدید خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/90065" target="_blank">📅 11:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnP1KnJtSDXeZGrz-LmztbsqSDePqlcG8POrnOiTjqbXix5kNgjSd24_ndGakVrNHBdE6Q1z8THL4QIQE3wlRl8npQy2xDTNsA3Mgi3c4nULo08-bZcepTJK5P4TJGjfV4anBIefa7d9erKOD4FyoQ-YN_FQ7bEamc6YAkPkGvqow3ZN0pUiggsNllKdkVn0f6YhWCwtB285dYKM6TI-E3pB7NWiqGPSJt_pO_Pb4MvuTO6QnzC4Qd519Nol6hnVoQHf5ltH-VabQnCKQRM8F1rQacK4dRDbPBUsEqzm918j-bbO0tFAcWJU3Pzmb1UaCU6Xaef_bC9Jj5INTAAFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
با اعلام‌فابریزیو رومانو، انزو مارسکا با عقد قراردادی سرمربی منچسترسیتی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90064" target="_blank">📅 10:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=GnCLh5KaXNbW0PiO_5AA31wlOav43bC49eUo-nMuS3yszUrVz_7_CF305NU2UZLqHbYEyL59tV5vzg3DqkNNLD8F9PAO683XZ6uh7SAwneRhU4M1cdK7s-bpwQd2Nd66BNvfG5LNEFFjSzB0jZZyb45poShZGsu19wgHZnAR7n-LOu5TA-I8YoLOu2HA_tSf4EXzNj9rapyqsnqAzCa0ppX8v-YjuY2PNZO6uvoJBtlS3o8HPbngd73_h1WZwtMIJjeVPr35fc6-mhb9qNr5O11wH_9QhVauNK8fcmIZ_2e8N3I78R1SkCFsjWguHcCWrIdziI3_37dyUovOTVhV0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=GnCLh5KaXNbW0PiO_5AA31wlOav43bC49eUo-nMuS3yszUrVz_7_CF305NU2UZLqHbYEyL59tV5vzg3DqkNNLD8F9PAO683XZ6uh7SAwneRhU4M1cdK7s-bpwQd2Nd66BNvfG5LNEFFjSzB0jZZyb45poShZGsu19wgHZnAR7n-LOu5TA-I8YoLOu2HA_tSf4EXzNj9rapyqsnqAzCa0ppX8v-YjuY2PNZO6uvoJBtlS3o8HPbngd73_h1WZwtMIJjeVPr35fc6-mhb9qNr5O11wH_9QhVauNK8fcmIZ_2e8N3I78R1SkCFsjWguHcCWrIdziI3_37dyUovOTVhV0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
شادی فوق‌العاده برزیلی‌ها از دعوت نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90063" target="_blank">📅 10:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=GBtWfi8m0VcZSTmG7DwkJdgKKe7qKbj29K_FrXJZv0-xMryG3xbae7NpoX3OMUvfyFMqiUC82PcuoUGGcegpO0yAIv4-C0PMcOFV06QXL6HQztRUtLGRv5c85VQhWBaUtXtqRETefZATbRSSJgu7fQyy9xQXlm5iu7EpdxoDVXZNwHIFeP5umko6vYZN_RL7xqTSqdTwsDGyJgru5J5lEOVvVi5wHKIkO0Hy__1gZSLSLbYHCmy4F99D-jwQnjV27-py6kBXvq49dUe5gEnJjp90M1DoOTQL9rdAhhQtTmbkQ-B4SvF8pZRTR6GKlx429MokbcXTcEo25_sRTheQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=GBtWfi8m0VcZSTmG7DwkJdgKKe7qKbj29K_FrXJZv0-xMryG3xbae7NpoX3OMUvfyFMqiUC82PcuoUGGcegpO0yAIv4-C0PMcOFV06QXL6HQztRUtLGRv5c85VQhWBaUtXtqRETefZATbRSSJgu7fQyy9xQXlm5iu7EpdxoDVXZNwHIFeP5umko6vYZN_RL7xqTSqdTwsDGyJgru5J5lEOVvVi5wHKIkO0Hy__1gZSLSLbYHCmy4F99D-jwQnjV27-py6kBXvq49dUe5gEnJjp90M1DoOTQL9rdAhhQtTmbkQ-B4SvF8pZRTR6GKlx429MokbcXTcEo25_sRTheQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خوشحالی اندریک در کنار زیدش پس از حضور در فهرست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/90062" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=nMD8pePOwloGtBv4roNjzATTUywVTK1hrZgqvwqpygzNkW6jVxeBIwmT7WXcrTLRcZMw6ciaD_CmY_0biZc2AWzbAMAEynK0eGzFlw0vzLBQQ3cxlV5ClUTondKau9SdAw5e8dihw80oRMT3azdygI74QIDG8niIaltY0ThqBUHoBEQhk-WcBmEBWk0qcqh6vbGiwn3QJUZ3PJnnLQu9MnB25iLHJdFudmYLvbL_hQV4OBnJrjHZGfF6wlGLkyV_HTWXeJBktuGpW3ot4hp2by1Yi7qFDr4cWofPMU4e_u20HLFncna0kULuyZsVbK7lwduubWtZggfB-Ab-3DAoHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=nMD8pePOwloGtBv4roNjzATTUywVTK1hrZgqvwqpygzNkW6jVxeBIwmT7WXcrTLRcZMw6ciaD_CmY_0biZc2AWzbAMAEynK0eGzFlw0vzLBQQ3cxlV5ClUTondKau9SdAw5e8dihw80oRMT3azdygI74QIDG8niIaltY0ThqBUHoBEQhk-WcBmEBWk0qcqh6vbGiwn3QJUZ3PJnnLQu9MnB25iLHJdFudmYLvbL_hQV4OBnJrjHZGfF6wlGLkyV_HTWXeJBktuGpW3ot4hp2by1Yi7qFDr4cWofPMU4e_u20HLFncna0kULuyZsVbK7lwduubWtZggfB-Ab-3DAoHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
پایان عصر لواندوفسکی در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90061" target="_blank">📅 08:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90060">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/Futball180TV/90060" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90059">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ueMBEPU-PtyPdKT9I1XuJoYD1mWcZckKJRQhFOtpJCZVd5bicbpOWXBX0jtqsFgpjvm2khPjkW6CSGYpi5XrJR3Ws5tC1J5e5EdL3YvN_rFVNmEghgVaxyDEzsPFBsqo6POlUmVvjQBVTR31qgKdOskG7O08NrYMfsTfbcx6vpeTHlkwLcMq2cSQNbfWFeOPkXTmrseDodfC4PUygSLMxndX00PCrk3id3PFI2FWz8N7IugvVwZWjOfkhDlJpWAdoo5E9kj8AWPZ5xrz61YcXo-xblIaRHkp3g9YWqqnhZI99Rs8y0RIBNnxGNsO_hU2bu4b8pejyIFOt2oqdr9duQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90059" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=pX6LI2IfNA3q5S-1QMo6HzbsmgiCruHuS2X-xqLqYc64hASooZrbyfGintjs5YRzS0wGBALSeKwxnZ2y1qMRJzxw7k1UaKSz4KnVVnZMvOp73Sx8KWMJhcz8Pc_Iw0iZ5BJRtoNuscY2BMn2c2GBPfgpnvAcl6IkOZe11ijIFjses-ey0brt-mTQj9wZ4EvSpgqQ4yXAQyMUN3rjZDiCK6_ycxFjt5F2OF4-8UR7JPhHcRMRGXtU2CcBSeWYts8HY6vce6gglJ_Q3Mfi-AEPkUlg2xWpPFFWH1AcEnxxvhegn-_dB6ISoDMioBM3tGUOB2_mgfU4SFsHLj5efszjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=pX6LI2IfNA3q5S-1QMo6HzbsmgiCruHuS2X-xqLqYc64hASooZrbyfGintjs5YRzS0wGBALSeKwxnZ2y1qMRJzxw7k1UaKSz4KnVVnZMvOp73Sx8KWMJhcz8Pc_Iw0iZ5BJRtoNuscY2BMn2c2GBPfgpnvAcl6IkOZe11ijIFjses-ey0brt-mTQj9wZ4EvSpgqQ4yXAQyMUN3rjZDiCK6_ycxFjt5F2OF4-8UR7JPhHcRMRGXtU2CcBSeWYts8HY6vce6gglJ_Q3Mfi-AEPkUlg2xWpPFFWH1AcEnxxvhegn-_dB6ISoDMioBM3tGUOB2_mgfU4SFsHLj5efszjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
خوشحالی مارسلو برای نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90058" target="_blank">📅 00:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lj7wHfWuUcccBTUqYXjPbYwxJBiHhTwq1BBxiQe6s-DqEd6GCpByGqG89dup-2kRrqcIlqpTxcMFAprXCXpOR8uc6BmpZ9UZUejN07qNEQr66-w7boaULifjMvGy3WKmw1jzWraI24HmCZDnykE9MsPXxlRhb08L_xRrh1h5BxPks5VAwlaDnT34Tr0i-Nfp_-dtR5Qli4t5rzZG2Srq0Ik5mb_B_AIN51q_0xJKQ1CvN76-GhaZIZqzV8dcYBD47W6NshbQfiexfn3LFdTOTeoNhgewfHQcr0sn0d1MHU5HTXvbdf-2iudbp3oXiBi_A0lrxsZqTStrKp48MqLErA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر انگلیس پس از برد امشب آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/90057" target="_blank">📅 00:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZjxfA1etEWCIk1eGfVJLJCDyhl9t79zeDlDAX-rOq1KYOOrsbqISUxnAHxGe8OLyHZwAxEMIBtDXnipFY2Zc8LQ6kDFCH842TyLdkM5xUbuezRw0QSOG71UZKtqJsl2Xizi8d8Un82azaLtmKUTt7VzwjKOWOeOCQ61vfTQQ2claNE2HeX8B1UjHPOjC68CX7Nkc35gecmKSagFBQH4nAfVO0YZJC5CRCACSuQWHiHssbU8saNW0CLxJsyYr0fbqfJLFdpTTIi1ui9dPfaqrhVRAB26FcsEi25lsCAaa3ZQWwnFANRACx4Z6eBOyhrCatiChloFB2SisdzTKojYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
لیست‌نهایی تیم‌ملی برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90056" target="_blank">📅 00:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7w40lm9D5i3cEXu4V9t93pgb_JbAzV9pNBNuoxOGwxjVP-aCb6v0m6lgtIXDvDfoTTAlrFcLMlFwPYunPaiut96t9Q1Hnc0-qlAMMYutuCEZAm9bd4c212nUm9fY8QXKqUtzaJvrvXpB4I3J1Jg8tBvc-Q4Ug-_p1HRVCE56G7hIQjJbHi6L5ySuhdkWt_zIK8mdgDWQKfxd6SN4WiBt-Hi_jQWEtC4c3nnUZtpTtMvn7eg-bg3YWe-0pI26GwJturSjXnoarrIT1xL0qA8UyAN97X28zc4bW5Edd3Z1qplTWxD4N9v3JyYfCWpqEG7zJ3Mym_KHCCmCpqSXwB7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90055" target="_blank">📅 00:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=nGLRoKLXHGDR3iqqtm-7XMQeSy1hM2X4Bfi1MmKVZUiaEm2U_iRUbzDYJtyMq9vz_WwA3B50ULX_rbs2ZBEpn8KDmP1diTcykQ8GZ2gGUNvulBVJIsdnOifL7_T1p8TMxO29XCbHWFf4SpKcKBgjGwORCO0M0UD194kWJNDC7E6CnX90uCWRmYgZonKvLbxH5uN1U1UfoVKrylciTqam8-wPc1Wr6_Mwr6WSN0Gt372oU8Yr96HPU_xGfySmfBbUaOgAliP79TmTtGYU51JGaHn6h1Kw7ZEhSIqDjHz48dmQezUvDWJoqFOGHtaYixLU4mJvjXEmHGJciki2ZKZQSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=nGLRoKLXHGDR3iqqtm-7XMQeSy1hM2X4Bfi1MmKVZUiaEm2U_iRUbzDYJtyMq9vz_WwA3B50ULX_rbs2ZBEpn8KDmP1diTcykQ8GZ2gGUNvulBVJIsdnOifL7_T1p8TMxO29XCbHWFf4SpKcKBgjGwORCO0M0UD194kWJNDC7E6CnX90uCWRmYgZonKvLbxH5uN1U1UfoVKrylciTqam8-wPc1Wr6_Mwr6WSN0Gt372oU8Yr96HPU_xGfySmfBbUaOgAliP79TmTtGYU51JGaHn6h1Kw7ZEhSIqDjHz48dmQezUvDWJoqFOGHtaYixLU4mJvjXEmHGJciki2ZKZQSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙂
شکار لحظه‌ای صداوسیما از بازی امشب آرسنال که با برتری یک‌گله این تیم همراه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90054" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdBZ7w0N4G9UxtQK1vPYiEdLTmDJ3MGpbmkIAhqoqYSXrdTuSO8_lejGSlcvB4n2xce3AV3XnOOJLaXoyTl2etwqrLdUOK38Dr8CrD73legW5rodqi9hzWa3jy0cvZHAYo1JqFjFB8Z-SftJzyOFZWrQQ9MBUBWDP7qIjvR1ZwApjiEPE9sb449gFNlyPtETjrckbLGkaMSJxG5hUeNYS8w_LRDRpTfiGmJqAfNtk-qCslH2E6nA7jpwPDMVW6il_tVlg3tQ-74GkrhS40OZdw_MBi1zmmROcv_EwArkIFN-hqQBqf4So4U5flLtmOWzYw-XghdQWV9D4oIjzQGZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90053" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🔵
🟡
🔴
با اعلام سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90052" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
لیست‌نهایی تیم‌ملی برزیل تا دقایقی دیگه توسط آنجلوتی در نشست خبری اعلام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90051" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90048" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLLmKKb1vsYxS3PKhG0I8V-JGd3Kk9lKrWntFydNloSUvAE7mXidoBzccPvthOQr43lBEQpO4BKjYlig3uhnt6C4qy-MlXesBDa9F6gaaF1ewcXDanCdhnV6A2ZdDMdWllY9Q-k8nH0B_OwLPksL34xur6zY68SeIKtAVfb6P6jvLqx_DAv1AHq3_qEZlQ30X9M1zm8mWtMEBLsaar1S0Up7hyJyF_PvrLWy90xVNLL_b1WmSkZp0hQdvsJJcSLZUw2k_8_2POzYCWKv23h0SfK9GbiB3BxdD32Cz233mulfwHYFqxR9pV4fJP4wneLPS7XGKWtxMexQxU5Szh4qmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90047" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
‼️
فوری از ترامپ: امیر قطر، ولیعهد عربستان و رئیس جمهور امارات از من خواستند که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی را که قرار بود فردا انجام شود متوقف کنیم، زیرا اکنون مذاکرات جدی در جریان است و بنظر آنها، بعنوان رهبران بزرگ و متحدان، یک توافق حاصل خواهد شد که برای آمریکا و تمام کشورهای خاورمیانه قابل قبول خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90046" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=WUrRMj3KnGZQ4VUjuHGEb_0lZQuIQk9bhQVxEFwgY3K0fSQsWxH34-G6XVwaoq2TTigHVuMH1cBHuTac7xZDCgooxgXHlMNVXj-GKgA2p7sFgOOaRSJs3knTP08xyaiFfVj-U8KoBLvfdeRPrwzK90zk_tpwpWD7rHlZAp5aJvlKVksU56ueRxhAE75xwq81NuXBktQeJelRuLDNB0kSIynshPZEJZ_qDlaNxAog0pzSz40XtDDiShEqnIc1FP88ISiTS57Ki0vMbUjmbRsSlw80i0lzE-hFPV7toVydmki-A6_HAKAVzKSD56v7aJTJehzxzQxQI_h0zHaci2jVMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=WUrRMj3KnGZQ4VUjuHGEb_0lZQuIQk9bhQVxEFwgY3K0fSQsWxH34-G6XVwaoq2TTigHVuMH1cBHuTac7xZDCgooxgXHlMNVXj-GKgA2p7sFgOOaRSJs3knTP08xyaiFfVj-U8KoBLvfdeRPrwzK90zk_tpwpWD7rHlZAp5aJvlKVksU56ueRxhAE75xwq81NuXBktQeJelRuLDNB0kSIynshPZEJZ_qDlaNxAog0pzSz40XtDDiShEqnIc1FP88ISiTS57Ki0vMbUjmbRsSlw80i0lzE-hFPV7toVydmki-A6_HAKAVzKSD56v7aJTJehzxzQxQI_h0zHaci2jVMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
لحظات احساسی لواندوفسکی در رختکن بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/90045" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJj5ZBNZWk1CGm0Km9CAOnX7Tc8MhfGKXiMyab9Me0uT2KLOuyTnLvlCtvDpkyuCXPKkPXkxt2nn5rRBCVhbWRe8JMRNGkBTsN3JYqUyEVVsjiAq895iO1nsztBvO3_KEMTEKmsGQOzU9wwLM8XfV16jn3s7WVrxEQu5GGuirXmUEi_yW2zc-jfX8YWodpJjldN1LQLTguzT3lF1PpK-77vqzEfYEMLgDSKcd2gVT6L0je46tC3g5aYGdShxXDz_aGoFeaMBIANbgXalzRgr1mBeLAndT4QbZj5n9jEcFNtLp790Yx0usbcKWnZOt1TT8WD4ykqs5HaC5cHLex2Kng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
عملکرد ژوزه مورینیو در رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90044" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90043">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/90043" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90042">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXh898CHCUrE3IKqlYV2DcMvbKcjhO-NKMdeHuPlERq0rPm5HacZPiHl8oBslEiha9qDbbTnLcqfDU-LZmG680XMYgszzWG6nSYlfOZoHGBo3LAPT7V-a49ikkHSAslVIhFZ3EWQgL4YEIoI-iDQX7PuZaFIAACdj9W_YmqsHUhyk46vXS_ywRcTMJ1v_KuG2hJWUJa2mFgj7FG5CksrtzPBLRgd_Kf9rupkw6WDE1TZLsmz92C8rKryiUAFN_a5tY7F7TZB7qliR_Gle_tPV2XFzCNbWOkqJ6Bktd_sL2tgSEaIpcN5dRH3E96LibQlAZ6slI_QGcaWx6uXa1zx8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/90042" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssEN7an1O1s-pKev7bZbqKgNzZBYNCE9CKJYu6P7BlgtSXU_zcDWJ94kua4k2jlhnlj_I2q9sqrFf0INqI-i0tbsqVNxAR9aUYzIeyecGE629IWH44kWJYs9AgujwAL4IcMqbd6nsft1EM1t0TaJhCxsneLd4zUM68LoFIM4XkbCbJHg4wx0e-9Bym6A9x9YbasdtCUeaWt9INYXlqWyud7fMjw20WkZVO1z_LtFqF2gSeZfE9Bt_pz2Ida7kuljZrCSToTCy_rwhVEob-SsFzRdvlrGqyjqhBrXN_VLSzQGUY5cp0QxblPMvELC_XJHOnDqwDZSq8a-teHF3UiwNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی که تا الان سهمیه حضور در فاز لیگی لیگ قهرمانان اروپا 27-2026 را کسب کرده‌اند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/90041" target="_blank">📅 19:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/b1hD0LNMRopzJm-N0tsgaMmj1UKDOeMi7ax5gUq7H2yEcfQB79P8jFe8-kLZ7pHkS_96_q9-YkiiLd7yU-GJ-VG5uwNeqBxgUmQloCkOe0wY3OOYTl_JGcZSap-VXPlaoXMmkf2vXXwLJribFTCIBTlZWQI53r962GlpOYeOnqyN5Ds5T6wsfnozIH0YZCf7O47yIiJ198QzgXGo0-fq8OkMyPFxo-zry4tyWkJVdKqhaqCBq13gLvSTRtPzeIjL00EJ9pmduQqbMPH-GbWLI9j1l3scrnKphsiJwDIikw1ijKRif9H4xGGL-dNWWewdKYq7G4AKNrCm_ywyURaGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/Futball180TV/90040" target="_blank">📅 19:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90039">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikC5kEF0PAKF0aSpui1Zvj-bCDdBjHotqXz92AOLzAxKewVtDNqDZFyc7A_oluua3vfCwAce9XFxDXsG8mC1tG_tA9YNdgupMGFzfj92iY_1RoLuVqR8zTjD-slx9Krb6DF7QIyjBq0CktM40wtTw3YHljWdf7XfgLuG57BSCVv4OYR3hIclvmiN08SzyUBhIE06xbDlXJ0J4dXTWKl4sFV3g1Wz_hFnrnkrksOkQ6QgrxDNV4H-hABoQsfyn5qTTjfvhP_CPvYZSPVXOvOICCpg7DVoPv6wafAKyBizCyfc131U7QdIWjy03wC9NbT3rzkWbFX_Z7Hr6_60bPu1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
لیست تیم ملی کرواسی برای جام جهانی 2026 و پنجمین حضور متوالی لوکا مودریچ در جام های جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/90039" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90038">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/be-doWZjn2clc2JHw9tXwxQiYldjY8nDArGXnyWB0Sm5BusWlIB127vD1IssOxOMGyzW-SD6cY0Q2lHNPamoRJLtYVkQkMIWypvyVCx8fAkpNAk6iuLxs7A1zmgRJRNxZwxjC9xhND-QRez5A-vC5oaAZ9dteMKgPf3JhnSZK98GtDy6PeJsEFzV6kMbPyM4c1MXGFHHCUSo3guESwM3PbleoEBmbzRz8Akc-_XU-95RNvReMrfFQq2PLnff3sMQGJFEtjXcR0NeL6h7u2yi3S-XZfaxYdT9W8hRP4Ld_sVrRfuTU3U6kIVNRWKTBYG1oPvWuHSyFRLzj7npT1nuJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسمی: هانسی فلیک تا ۲۰۲۸ تمدید کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/90038" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JulevE-aa3fWd0z2QUEbb8M84wDN3BVRSZmm1EGnZwvlI5Rk6GXOMzX0F0sjMyRA6JO5sjcPiYX9pAxml3e3mSPfqPs8dE581thNnlYgSXY5lVb0gnY_db0SzDEkiUtbaaHxXKudTH_txO121r7r2NuqK9f9_J_xv2sS76ptn2QDoSp4u61yz1MEtSTGmBt8WIW8Dakb0ZdjlFiDXshcPjN5Ft50iwOLVy4zNrx4-bm1x-cmkv1BXw7FbW6fmmN-c5WzZVWXNrXXks5WHLK5Sz2YbQGd5Dj_Z_LWtpnUIWaAn6LBxdVgqCF_Nt-CBiBv2PK_RRWECUcuHxAqRRBO7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی: کارواخال از رئال مادرید خداحافظی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/90037" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f48kXv5-TqPIrErYX9OZJqtleLeYuyK5pz-jmoLONP_hgQlr6pag58jea60JDePRMixTeDbklsKYIVrDzJnNtrGAVgQnmCe0OTnhfnsC0uxJwKOrwHXeT_SPILwlxIagNRhntTvTXU9sqtAcoFQu1xKJO7HqPs5vgBY4mlMayNbzBpXgeCPM1FIvVFkUE5UNf3Bc5g-CYzshgZ3tHvpkS8krzyzbyVSxGroAdSjnw5TUN1XYcpH7V9IuNWv-cvFDGHkQdqD3MWhVW8FY2zQrWCxg7NMpdKzYR-rpEcyRsU3LG-9xrXN9Woe5KfWZtpjCHUuwKTHifBBDhcX0abiY-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدایای ویژه و شگفت انگیز چیتابت
🎁
۵ درصد شارژ اضافه قطعی
⚽️
بونوس خوش آمد گویی ورزشی تا ۳۰۰ درصد
💹
صدرصد پاداش خوش آمد گویی انفجار و کراش
✅
ورود به سایت و دریافت هدایای ویژه
📱
@cheetabet</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/90036" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baWUgwXhxuFlzkyBHeFYxjRccx9yncK7411iCUyuqMvn3c2x_UsghW2BpMbQgyya_SImu4Tqmbc-x5TDc0ZXyPRcptv8PLNMdsELJLAFLPZU9B7-Y2XY0juA1O7eMWy5lnM6Lw01b_2tLlZ3IHT0izMlDKH0637do36pd27lY2bW7eftr_nUQ1KWsI-9731_ThcUuoWZgPZjjTV8hPclCRLU7emPatGFWDKJCx4yJ7VhY3xwaqw440EAm5kIZs6rLb8DopuKBIdCt0u4uUbRJS_sjbx8VCwq05llp-3Xon1c6tDuIs9t_FshMWFWp2vvap7BNDOp84EuuW1xZb0SzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردداران بیشترین بازی در تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/90035" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=sA_HRgsduUjo8AYVCmFw_XjxpNfophGQ3ogqarti1fcOa2rcHPHVoqPNXGa7DuB3-_yq3Y6tSBIMd3sthiPM22NHrjRStQd6PLOoqGTL2yScJRPWrewqQbJpsgvU2PlLCe9H9k4TtglzOOclcT7mBuY1SYJQQ2Ogw0Oim2eIJbL3NGlduPGKw6btf17d-XHE4AYSUr9eS3XtAuQpO7DlHKWPhcwg_Y3KrfqkfvWuwDas8OW-el6GePNvV23kiyQZde-7_eGqRFY9X6cHeKzBnjDnkCseCudkRssOP5XwHqEKwBT-4qqmvIMFFrSh-eLhziFsFGr0lHz1A9jUTm4pQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=sA_HRgsduUjo8AYVCmFw_XjxpNfophGQ3ogqarti1fcOa2rcHPHVoqPNXGa7DuB3-_yq3Y6tSBIMd3sthiPM22NHrjRStQd6PLOoqGTL2yScJRPWrewqQbJpsgvU2PlLCe9H9k4TtglzOOclcT7mBuY1SYJQQ2Ogw0Oim2eIJbL3NGlduPGKw6btf17d-XHE4AYSUr9eS3XtAuQpO7DlHKWPhcwg_Y3KrfqkfvWuwDas8OW-el6GePNvV23kiyQZde-7_eGqRFY9X6cHeKzBnjDnkCseCudkRssOP5XwHqEKwBT-4qqmvIMFFrSh-eLhziFsFGr0lHz1A9jUTm4pQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
📍
Tehran
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/Futball180TV/90034" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMe4AwQIig2BhSyl2FbMaQ-m85KVSSd7OzbdjGa_ak6-i7YGIMh971Z9RyyeAp5F7Vmad0VFjjbFLdK1cVLFf7N9rH8qoYCU3oazTEgTZyiwGh-9Hmqdx79Iah24DmbzdBfUcn-8pRrvcr-iEqhnF98gK_0GNenXy7heMUvB412v7tS6iHb3gI1Kas9jrEK8AUKm-LHGqtmQjdq5OmREqL_XUKydqyrsAye0IsgZArc7cg8WrSdL1vxJgC0iYO38v3A2AOqNZIEs381CLX0JYSdZNaEHGC3YCFUFXdUuss0GqSOnkxTKUWcjUvgTV71OFH6rJPvBKzXn5c_N-Uv51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
روبرت لواندوفسکی بعد از آخرین مسابقه‌ خود در ورزشگاه نیوکمپ، عکس نمادین اینیستا را بازسازی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/90033" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90032">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/90032" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90031">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ji_9LVYu3BeF9Al7D9q4DMp8MauJ_onmFm8Rhey_2G67xNhE2USMiAqY3NHbQ9PPYvj50kTv6qXEJBY-OVXMWk4biQeBW1QPRk3pDOB5GDM-5N9T9zkoNxBnvhF0OvQQrfk2wH4G8c_6BwVtrtqelohtipwswBDObgw77WGoInZ5LvCeWTe_34aJNdWcqAYCtR4EJPpgW3rvLRmDTY6hyQDWSLuW8K2ZInsM23vvh7vkEP3pl1e7zRo-K-nj7bMx88mKEyLEz9A9ufhPG6izueXvfkeNw3vjTgo1ORBwEgs8oPoF-cWdwn3-SulLLLdaUlQty-YBOP4xOvCVkJHnHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/90031" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=J2Kpa65I0UEz8ojYFg7DOboyGU8AO3XWPEDG-AKqYNjGM1jdX3BwiR1M725L_JAlMeLeRwzLJBISwk_Ce1koDWKtsnbRuT0w4JVs9lH4OCd8p2IuOk6foO9xbT9P0E9HdfUHFDDnRU5To0QFrNOww7HCKcrb7sO3SI9A8dN6IhMGh3olohTywFRw512Vh1r1C_83hXQ9UsrHJfqO7K0lBfvTUUye1KyV_xnM1Lgiz4wdFg7O0TVwnWoF9xIS-L1mWkaC1QrRidL0SYitB-rFWmMuQ49N6YL6UVz2q6_dmR9tEygbPSiKIj-aM51B7Tss5ZqyNqavmT56zKqtxw6aSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=J2Kpa65I0UEz8ojYFg7DOboyGU8AO3XWPEDG-AKqYNjGM1jdX3BwiR1M725L_JAlMeLeRwzLJBISwk_Ce1koDWKtsnbRuT0w4JVs9lH4OCd8p2IuOk6foO9xbT9P0E9HdfUHFDDnRU5To0QFrNOww7HCKcrb7sO3SI9A8dN6IhMGh3olohTywFRw512Vh1r1C_83hXQ9UsrHJfqO7K0lBfvTUUye1KyV_xnM1Lgiz4wdFg7O0TVwnWoF9xIS-L1mWkaC1QrRidL0SYitB-rFWmMuQ49N6YL6UVz2q6_dmR9tEygbPSiKIj-aM51B7Tss5ZqyNqavmT56zKqtxw6aSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استایل متفاوت جورجینا، همسر کریستیانو رونالدو، با موهای بلوند شده، در مهمانی جشنواره فیلم کن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/90030" target="_blank">📅 11:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc4Lx-dSNqHjzm1BAfmOlYjvBhSLnrEKwAnCFhXy6aFr4SsoyODI5qC7_oZsNTYL14LPF8CZ9qx17GZtwh1VHIw8eJt1Tw1IbeLKgy2y3m3TMS2o8xOGbcIznJRvq2EJVSbdLiMz3pdlCTiiWu_t_50BNHeVr5sBOcaE7PZP-iDkmewv9HCP5-w974GTwztJL6HAq7Ofyfk6O5H5hQFcKPGOt0vtHvzyNTTcZF4mTOaSX33tcDjJJ9MV85c95VEvL9CheQ-LlFro58Uog7uvYnb6pcgXHj-O6JtF1C4S-r0tvj5GbIDd-5A0bIX3y3q2OyIL2Fq9GOC_R_1xJmedCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت تورنمنت‌های رونالدو با النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90029" target="_blank">📅 09:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441c980280.mp4?token=R62anODR2W4udMu87WKC2aA7piIjU1YL5qDYkZIbvwdesLG1HnDmemA1fUMXKG6fGM6tuf1OuGBjeYlqkG2Pi0mKYpNrtzck2vg4OQ8sa21g3D_s88Al4qcJOKmlz1_stYE2o2_QK1UzQDT7LRTk_Ng25DxAJGYXQ48-LUBffhIp3fInot9nPc9yyTipY1YOsBJTFDd4U3VQc7jlP0DuIaNWNLiR1-yPxRimiDZMg3cU8uKvqWj-NNfXa5I8zLBcS2EwasMFjUjhp7Yew5J27zZNRUozK88YkmBN9MAMENKyJbAzncwLeS4l95vpeoDwS7vmW8dmYEARGzTHMOKhjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441c980280.mp4?token=R62anODR2W4udMu87WKC2aA7piIjU1YL5qDYkZIbvwdesLG1HnDmemA1fUMXKG6fGM6tuf1OuGBjeYlqkG2Pi0mKYpNrtzck2vg4OQ8sa21g3D_s88Al4qcJOKmlz1_stYE2o2_QK1UzQDT7LRTk_Ng25DxAJGYXQ48-LUBffhIp3fInot9nPc9yyTipY1YOsBJTFDd4U3VQc7jlP0DuIaNWNLiR1-yPxRimiDZMg3cU8uKvqWj-NNfXa5I8zLBcS2EwasMFjUjhp7Yew5J27zZNRUozK88YkmBN9MAMENKyJbAzncwLeS4l95vpeoDwS7vmW8dmYEARGzTHMOKhjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
جادوگری بامداد امروز لیونل‌مسی در آمریکا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90028" target="_blank">📅 07:41 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
