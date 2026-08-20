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
<img src="https://cdn5.telesco.pe/file/YfNe7Y_zVizrPqEDXkZycNBgkE3LiO7l9EPxIE7aNqpm5CEWUpNr1D3FYcjwPKQxk472br2xLXqrvaz__Bc7SoqqXiL9SyzImP3Z9jfTLaS0cNe1YGrUbV43S61dk_uxn-gN9ZyHZRDh51xh5mT8R65AxhBu3fel77cEJoVnsOaB0gdUXCklNvsqvwUMQjVRQi_7BxFXwbooOe3shfIOQ6wi2gx7Mza0nt_pcL3OMStLM6Aysvdjll_kUh9eTL_COQmad7Gsuc_oSBoREM6fxfRVcLbzGRIG995Jc3woi07kvvHV1dWIPsboNNWKAso7zWF1vT9j8bH0X0a3O_dyqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 453K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 01:20:35</div>
<hr>

<div class="tg-post" id="msg-104272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d167412a.mp4?token=lgoilQ0p2-n5fpehvfgsNcbGvVypSPyKyHJw67aJ9rcjKfqbVPKXJXOXlgoUzZWpRPaVDtck5t73Qx_BzlwBTg0-2mj0lajugBm_dY-fsoCENlKVLZdjjt0W07fEZlhx8mcrVLtQsM7KWWHc4lagG5aKqoXCJI_jslgEkRrWVRdXhl-CHioeCbo8b314CcFVMKwZ56K010ZJirZFTCptOv0MkTjqSrxELgIofKJUcYDVVtiLOfUkyqsn4_LDv5RWt34lYemegNLWmnZLNZyGsZ1B9HS3WlGGbU5ZUMvSbNF7HvcZo7doXzQTc9jM69OsGMNBzdpnlqUPFxx2NwD2Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d167412a.mp4?token=lgoilQ0p2-n5fpehvfgsNcbGvVypSPyKyHJw67aJ9rcjKfqbVPKXJXOXlgoUzZWpRPaVDtck5t73Qx_BzlwBTg0-2mj0lajugBm_dY-fsoCENlKVLZdjjt0W07fEZlhx8mcrVLtQsM7KWWHc4lagG5aKqoXCJI_jslgEkRrWVRdXhl-CHioeCbo8b314CcFVMKwZ56K010ZJirZFTCptOv0MkTjqSrxELgIofKJUcYDVVtiLOfUkyqsn4_LDv5RWt34lYemegNLWmnZLNZyGsZ1B9HS3WlGGbU5ZUMvSbNF7HvcZo7doXzQTc9jM69OsGMNBzdpnlqUPFxx2NwD2Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
😍
🇪🇸
قشنگ مشخصه یامال دلش بچه میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/Futball180TV/104272" target="_blank">📅 01:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=ElmJ39FrO2_3upxtTLyaciW567TeSz6ttBO61u9_og8E2oITUghxRlqzWb9AkQZ3NSCpI25urSgcwXsRUORDTPUJg_xkcsWjACMbS-jJLe3YCbPSfv6Cq6tgSaFDlW1WAn2KVSDLCcBbSO5otLuxvbQm_K3ap6Yk16bcRcxNMEAMGIsmArjxJcyfa6Jq9e7nBshLODwOYBhIdR8LKnZe8oMfOIfev2RgRnLgVhn9C8mLps_apU0XfVQybKX459miudtqVnTeVQ6nzMTXjfCV3EZiHHOHKAhezqGTw-jd2NMCMmYoGo3bWO6FNcRtW3jWleMiC2llv7nz7lkU_UlTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7cda8f28.mp4?token=ElmJ39FrO2_3upxtTLyaciW567TeSz6ttBO61u9_og8E2oITUghxRlqzWb9AkQZ3NSCpI25urSgcwXsRUORDTPUJg_xkcsWjACMbS-jJLe3YCbPSfv6Cq6tgSaFDlW1WAn2KVSDLCcBbSO5otLuxvbQm_K3ap6Yk16bcRcxNMEAMGIsmArjxJcyfa6Jq9e7nBshLODwOYBhIdR8LKnZe8oMfOIfev2RgRnLgVhn9C8mLps_apU0XfVQybKX459miudtqVnTeVQ6nzMTXjfCV3EZiHHOHKAhezqGTw-jd2NMCMmYoGo3bWO6FNcRtW3jWleMiC2llv7nz7lkU_UlTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😳
نحوه سوپر مخ‌زدن شیرازیا وسط بازی فجر
لاشی تو ورزشگاه با گوشی قلب میفرسته واسه جایگاه بانوان از اون ورم یه دختر قلب میفرسته واسش
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/104271" target="_blank">📅 00:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هایلایت بازی الفیحا 0-3 الهلال با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/104270" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=jksAgyCdTGXpqsjVi7cDu0tT-5saAtISJFalfN13-D0WWZuASqZx7KhH1I4DBamd89qst3UIVvBNvwCchBYcrM6aOddk7_SxN0T3w9_TUsEZpgO5wtnkTHfh2X3gYs-dDMZzNRqwjcSNsk4KY8WtcTwwOk7kS_19oIWpJB3c957nfilySw5zEyrsha_O7IGSx3Yg1l6SXHuebZP3rbU8nVtsN4GOYjLslP5P869rGIw-CD0gXAxcP3YhYxmIh6z7wSU9_4KBgByUgq435vxno2sWyRYYekC3XC0kWsXtiQSZASEmfQ0xnPm84VPJpPLxWaIcGQQNc3m90P1vAtmleA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdf2dd188.mp4?token=jksAgyCdTGXpqsjVi7cDu0tT-5saAtISJFalfN13-D0WWZuASqZx7KhH1I4DBamd89qst3UIVvBNvwCchBYcrM6aOddk7_SxN0T3w9_TUsEZpgO5wtnkTHfh2X3gYs-dDMZzNRqwjcSNsk4KY8WtcTwwOk7kS_19oIWpJB3c957nfilySw5zEyrsha_O7IGSx3Yg1l6SXHuebZP3rbU8nVtsN4GOYjLslP5P869rGIw-CD0gXAxcP3YhYxmIh6z7wSU9_4KBgByUgq435vxno2sWyRYYekC3XC0kWsXtiQSZASEmfQ0xnPm84VPJpPLxWaIcGQQNc3m90P1vAtmleA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف اوایل تیرماه: اگر به سوئیس نمی‌ رفتم، ۱۲ میلیارد دلار ایران آزاد نمی‌شد
❌
همتی، دیشب: یک دلار هم از پول‌های بلوکه‌ شده ایران آزاد نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/104269" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.  در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر  عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/Futball180TV/104268" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=G2O2sRyqTo0E9xpg1vNIPatRUa94Bmexgr_FirThFsjDCTHkejXNfHSCTzUUJfBFTWB9TJQUr4sazJpuNzD4zs7a70s2nuYAtlABHVvY9Aa8ZE1m7-CfbfvJpp5V1Fxo-OHjufMuIGF_eoQ-gj7H_dGxq1TdL7ZVfo665nLzNAkZpnH4zU9E9bCMBo_sHcl-Mfsni1ttiqXtiHxGAcwy3Crpssvl-WMXsQvPPHlXCcgdjjYd_0jF_eRzaCsuJcTmhSK6fnKqaEH48KgD7OjxnLPCwxZhmq18xVLaeQXq8n1D8gLHfqXZwKPHWxXGIGxSVOLwYY61Syx2hEY15ePt7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=G2O2sRyqTo0E9xpg1vNIPatRUa94Bmexgr_FirThFsjDCTHkejXNfHSCTzUUJfBFTWB9TJQUr4sazJpuNzD4zs7a70s2nuYAtlABHVvY9Aa8ZE1m7-CfbfvJpp5V1Fxo-OHjufMuIGF_eoQ-gj7H_dGxq1TdL7ZVfo665nLzNAkZpnH4zU9E9bCMBo_sHcl-Mfsni1ttiqXtiHxGAcwy3Crpssvl-WMXsQvPPHlXCcgdjjYd_0jF_eRzaCsuJcTmhSK6fnKqaEH48KgD7OjxnLPCwxZhmq18xVLaeQXq8n1D8gLHfqXZwKPHWxXGIGxSVOLwYY61Syx2hEY15ePt7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.
در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر
عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
شرط‌بندی باید با مدیریت سرمایه و مسئولیت‌پذیری باشد.
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/104267" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=ZuAofBMvQmmHxm0_lJxFCp1fMmElkgMYP8D20jQ0TZROW7xIaHxMWAz_Xmdo7zunKeqtHlYjHygz7EnEnNT95Hp0V_M8Bta4LWhxcejQPRaUnLqFbd558llzbX9SvIhAcuKo5OJLuW1jX9vqQMWeAmBWFeZhwqrhOEwR6VUzzcowFBR_4nD1B9CaYoqjwaPJ8golkhX8TOXR0md-mEGnJnPDaZ8OdG-yIg8TWA8VTaiB5zc5iv6MLk4TXK1gNRYstvdx0jPHBk_98wPz_00H9WMOSm5JmmZ8Zte-DQa7b8mmaPtmmdcmvbWZgGy3f3g_zfphq-PrKBL-0lyhUHX0_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1230d6d53d.mp4?token=ZuAofBMvQmmHxm0_lJxFCp1fMmElkgMYP8D20jQ0TZROW7xIaHxMWAz_Xmdo7zunKeqtHlYjHygz7EnEnNT95Hp0V_M8Bta4LWhxcejQPRaUnLqFbd558llzbX9SvIhAcuKo5OJLuW1jX9vqQMWeAmBWFeZhwqrhOEwR6VUzzcowFBR_4nD1B9CaYoqjwaPJ8golkhX8TOXR0md-mEGnJnPDaZ8OdG-yIg8TWA8VTaiB5zc5iv6MLk4TXK1gNRYstvdx0jPHBk_98wPz_00H9WMOSm5JmmZ8Zte-DQa7b8mmaPtmmdcmvbWZgGy3f3g_zfphq-PrKBL-0lyhUHX0_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
💙
نقل قول مهم میثاقی از کمیته انضباطی: دوستان اعلام کرده اند چون فسخ قرارداد یاسر آسانی در سازمان لیگ ثبت نشده است بنابر قوانین داخلی هیچ مشکلی برای بازی کردن ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/104266" target="_blank">📅 00:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104265">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY_QyqkEsU5Fe4JoPWePLXA0MFnSe4wHW9aiTD6i_dNmzKIbIORhvQXOkHngIOQFO0S97lL_lb6A_onto6ADgmPBHsiYcISmWmhlWNq8ZBxJxyAArBsJsvpR3Pbw4oJKdBlIxGx0TmnzzpbuZMLZBnoDgw7wBylnzyW9VqcjsrE4mNxh1TxfS5ZdjGFYsBNF6lPyjvsZo3DKOTMraA9A794lR64E9H9rDI30Q6hp7yuNWoHImn6RjEmHJgEvRuG8Fz_yYjQRCjWdEUx6C9saJXQV2AamDjGy_pU7QYkNt3moVppr-dazmmX8V1lBmKA6NVzngxQnJEdWLwCoMGhJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مارکا: متئو آلمانی اکنون به لندن رفته تا کارهای انتقال نیکولاس جکسون به اتلتیکو مادرید رو نهایی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/104265" target="_blank">📅 00:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=qcuvgu6uTQnO6ALLiHCniUtlfibFLyCXaSI4jVbYXKYpc-WJtX781DaszrnaCPOerPuHljX22NDbY6f497B8USTAh8aBT1oLwi74zgJjkj3Ftmkm66uufoaVcM0WLIIbDSahj51WdV63hkxqo5V4ij873QgAdc0kaHa56oljbU3SmIkJqjfTvw8s0xgRP5CpluVgpfFaFrXWUPqHT3D8mHdJ6WGDSQLLax5e79kNNI-GaELXULdFdDMvrXI6ypW2YbYyNwEJO-5g_NnIojQ-0kWat9JKGpK2lkgoneoBHnwvJZW3-OrhQrtKS8Y3GkLm4LOuVLDUCdYHXFjM42M-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e2e98ceda.mp4?token=qcuvgu6uTQnO6ALLiHCniUtlfibFLyCXaSI4jVbYXKYpc-WJtX781DaszrnaCPOerPuHljX22NDbY6f497B8USTAh8aBT1oLwi74zgJjkj3Ftmkm66uufoaVcM0WLIIbDSahj51WdV63hkxqo5V4ij873QgAdc0kaHa56oljbU3SmIkJqjfTvw8s0xgRP5CpluVgpfFaFrXWUPqHT3D8mHdJ6WGDSQLLax5e79kNNI-GaELXULdFdDMvrXI6ypW2YbYyNwEJO-5g_NnIojQ-0kWat9JKGpK2lkgoneoBHnwvJZW3-OrhQrtKS8Y3GkLm4LOuVLDUCdYHXFjM42M-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حجت الله بهمنی سخنگوی سازمان لیگ: یاسر آسانی یک قرارداد 2 ساله با باشگاه استقلال دارد و در سازمان لیگ هم ثبت شده است و درحال گذراندن آن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/104264" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=d9lb2dD2oNrPLxtDmRg-GaoNdLkk-g6tfWgxZmjNGb8c942r60ltYtQQjzSNF1Hl8DCV5VCRFyzEhQmsKxds_o1zkDps7mGp3L7uEMgB7zmbzUeKuwEZsJArhnUhsHnDvUQZqrct2LLG8eovkV75RAjq_8MeQvidH1pV8ISPqPCQG7PlfNVSUMu2TlaUYuqKVNpg9bft32lX1Vbwitt51pZC5GjqiVLebfDcsN_LO6krwr8Er9_1MvsR26z6UgGj_zParqolLT34iFH99IMgt_YKyMdunQpDZlUElZh_Ca4j1hneH14N7I-NiIZoc-bJ4lWn0y4_g4NGVCLD349hUYlIYkjK4MCnpuov9hN9uNkK8AuIl4yVVW-McnbALTiXruTke-Kh8a2Bk3YgFnRsBLzbUSQ0iKcMj-3QkxNZPNDuv0oqKteRtGUw3j95Bd8f5UG_LgIjyyHn2q0UrDXDeeG47OmmdsNoR9lVtR_dtZSq4zNkcfAUJnTNsWL7sqOLnpW--SFhzJ6l9y3z5mmNQeC5CrqSd2o3MRvNzKrvNWEk4i0GL88mfCge_9j59aJoxZYX7YgEb7BL90czKTgpnnWVwOzivPas3hRF_QzrDNjvlkdvb5hfUjrXx6CymLQ5idXkC8s1-WI2SGTMKdAQwH4ACNYzAPk9qwZWF_D5-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1449e6d243.mp4?token=d9lb2dD2oNrPLxtDmRg-GaoNdLkk-g6tfWgxZmjNGb8c942r60ltYtQQjzSNF1Hl8DCV5VCRFyzEhQmsKxds_o1zkDps7mGp3L7uEMgB7zmbzUeKuwEZsJArhnUhsHnDvUQZqrct2LLG8eovkV75RAjq_8MeQvidH1pV8ISPqPCQG7PlfNVSUMu2TlaUYuqKVNpg9bft32lX1Vbwitt51pZC5GjqiVLebfDcsN_LO6krwr8Er9_1MvsR26z6UgGj_zParqolLT34iFH99IMgt_YKyMdunQpDZlUElZh_Ca4j1hneH14N7I-NiIZoc-bJ4lWn0y4_g4NGVCLD349hUYlIYkjK4MCnpuov9hN9uNkK8AuIl4yVVW-McnbALTiXruTke-Kh8a2Bk3YgFnRsBLzbUSQ0iKcMj-3QkxNZPNDuv0oqKteRtGUw3j95Bd8f5UG_LgIjyyHn2q0UrDXDeeG47OmmdsNoR9lVtR_dtZSq4zNkcfAUJnTNsWL7sqOLnpW--SFhzJ6l9y3z5mmNQeC5CrqSd2o3MRvNzKrvNWEk4i0GL88mfCge_9j59aJoxZYX7YgEb7BL90czKTgpnnWVwOzivPas3hRF_QzrDNjvlkdvb5hfUjrXx6CymLQ5idXkC8s1-WI2SGTMKdAQwH4ACNYzAPk9qwZWF_D5-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
بهمنی: استقلال به عنوان میزبان دربی، ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت
!
استقلال میزبان است و ۹۰ درصد ورزشگاه در دربی در اختیار استقلال خواهد بود/ استقلال ۹۰ درصد گنجایش ورزشگاه را در اختیار خواهد داشت و بازی برگشت، این موضوع برعکس خواهد بود/ تمام تلاشمان را می‌کنیم تا دربی با قانون ۹۰ به ۱۰ برگزار شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/104262" target="_blank">📅 00:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bac35957.mp4?token=Gz00KqZZTnYDf63llkmUp3F_5MlXI4uMK_yYPaXI0_29SvJ5HN6i9pHMdmWmOLT8OLu7anZdOrQDuJyvwQAdVWOF0G401L9bUSntL7cPg9gw673xiC8JR_FzpGoQcTlRmEJdl7cpoC2irHMsbbeK33wFKD7HgkrOdV_n09VZb0SG_hNPhNsVA-aO6uW7SWWsrvn8WaAQgwX0J3vnZ61PG8BMfiTDRpfw_shiKeyUhjWIy811fKp1qhGLBNppm5qD_Y7V9wR_WY0rL2WgiyhHZ67nKBjed0LRr4NwFzLyMVS0YMaXGyMWVkPsINa4FtsSxAAKgXU5031GJC3yfjNdd6aQFKKXQuB0dRUsiKDSBY2nKQyAr13Hs8K7F1waGPfTXMBWaZPgNZ0hJzTNuQO23l_16mnS6QySY3p6XMatfwWdgUliXCmbpbtNS2iJ4lnafA5pYVRGYAaGJ8_ta6CayFU4JxYYm6gnA2FtM50QnPo_GDmhqoRQcL_0KhnBqeiMEgVXC6xvp7hXtbXGk88emJUma4r4p3W01aXQvj2y1TcNpGkdIbgutONmHwzvI0-qqJhMgA3aklQj-w9_Yvr45gLX8dv81JL3lLe6ahIbjIST4cbieNvskgng2akwYp3LVD5OYYgiPNWJ1XxeAfDWyafd3X_nQJDuadrtgQns-Zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bac35957.mp4?token=Gz00KqZZTnYDf63llkmUp3F_5MlXI4uMK_yYPaXI0_29SvJ5HN6i9pHMdmWmOLT8OLu7anZdOrQDuJyvwQAdVWOF0G401L9bUSntL7cPg9gw673xiC8JR_FzpGoQcTlRmEJdl7cpoC2irHMsbbeK33wFKD7HgkrOdV_n09VZb0SG_hNPhNsVA-aO6uW7SWWsrvn8WaAQgwX0J3vnZ61PG8BMfiTDRpfw_shiKeyUhjWIy811fKp1qhGLBNppm5qD_Y7V9wR_WY0rL2WgiyhHZ67nKBjed0LRr4NwFzLyMVS0YMaXGyMWVkPsINa4FtsSxAAKgXU5031GJC3yfjNdd6aQFKKXQuB0dRUsiKDSBY2nKQyAr13Hs8K7F1waGPfTXMBWaZPgNZ0hJzTNuQO23l_16mnS6QySY3p6XMatfwWdgUliXCmbpbtNS2iJ4lnafA5pYVRGYAaGJ8_ta6CayFU4JxYYm6gnA2FtM50QnPo_GDmhqoRQcL_0KhnBqeiMEgVXC6xvp7hXtbXGk88emJUma4r4p3W01aXQvj2y1TcNpGkdIbgutONmHwzvI0-qqJhMgA3aklQj-w9_Yvr45gLX8dv81JL3lLe6ahIbjIST4cbieNvskgng2akwYp3LVD5OYYgiPNWJ1XxeAfDWyafd3X_nQJDuadrtgQns-Zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
هواداران ملوان در بازی دیشب تیمشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104261" target="_blank">📅 22:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvMmrFnMieUM68jsSkExETbR87NbtCOwjxflJYTBSNRlj2jJEI0w7pKcTxbeA3K1TRH4BRo70y_WdYifvpakQdk1Ce8-J5xhQ8ypTRJDEoqrjddetCVvWmcbsVN_NaalI4IoKC1M25a4WLhWqtZfwNY4D7LEjKNbo5VwlUIt3aBuv5ft-H8ocyZYMTY98fM_FpvfvtwGQpzzytqslHGNnrt_4U5JAjdRgio03Zb34-xMKZECqowFtnBF4t837vczXramzP4-YCiVafqCsZplZyQvxM8KzUCf7Myaj0K3NwDhblYlRpHzgHrkGp9YGZv7ImLFADKeE6eVLmkWahWChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نادر محمدی(منجنیق) و هوادارانش در روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104260" target="_blank">📅 22:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lO02QtvKa_T0Qpncdmdd11LIla10BrRVU9r0ORlUWtnb8EipPPcemvrU3B4_j2yw9vDjycLtA95l0Iv5n2k3MTsEtECT-VUF9zrQp6sCcTvP7CmgD-bI2bpOEsXjh2BGJZzaCX3NryzWjIIq0vGPH88NprpluSIqi3xQaeBqB1wQ77WuwFzdyRcmoBB0-RhzjF3xPtAJjQJ1wNDx7cb7vSZxgrjW7s3pvZGuCum-S95ZdQRjTsiDsZ9c-qRbX8rhSPT1vM1F8W2-cE3iGaeislYUiTnK2n7YEv7G3m8jPEfUu9E_dNkvVlDFy_OTzgES73pVWs1_D7mQ5S9jlI7H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
خط هجوم بارسلونا بعد جذب احتمالی لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104259" target="_blank">📅 21:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnKhzi5GtTv7_EdQXiDK3ieTcQN_ualRT5uFXnzjhdf_FA4d_jDnhsBTi-NFIdWzwqMr8wwm74A5zQx8qUg0K9lb_fOIiIBClO-LyoYnJ1OTcXKwrgVM6xhG0m5c7zLjL6VTCPQGf4gSzXe-Mg4BIH2rgBjWSrruhl0Uuezg_CEcIfZ1YOFaUxmxcdvv0Y0SE7xIUE7xGQPldkUMTuS7YT6GCbdw8bJNpjD1v6XoavfQoNkO0SU9NLyPaBacEHlGXOpv2bgBFPGXldfpYwMemWtD0L6KUoDDT4q6H9gGiVBmCTzdSdfHq-jPG4ljujl1K8Or8hZvsHZaIpqAvQQMoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
رونالدو پس از دو بازی غیبت در لیست فرداشب النصر برای بازی الریاض قرار میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104258" target="_blank">📅 21:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a24abd1333.mp4?token=eMGcfz4-X1IpumhVMGeBUm9w9vOah9_Nwzdht8JDkpdBHoWGUDFC_X80Sbo5bu7dN1e8jq5awmKm9Vx1hc_glhEWUDoXmEEBG6TgKIH4dkiZqRA5LNILofRopZTzC_0T-Y0L0SJ2pMfl2HG5pKbskIIl9bSnSVdq4xY7M0akwUxBdH7F9x3EQ-5kYifwvNNYstEpdidgpXVmZ2ODrDoyvlb-sDHFSFnUpvE6mFRlbn-VvgmlADwbt0G_7A03-wV_UaT8kDlhMD93lI8oeqF-ucGL6A5BEXwqrWW7PduWVdVk1KJIjwIF2hIKNRYtIkm8ZhgAMEOi0IORO4lEEp-mxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a24abd1333.mp4?token=eMGcfz4-X1IpumhVMGeBUm9w9vOah9_Nwzdht8JDkpdBHoWGUDFC_X80Sbo5bu7dN1e8jq5awmKm9Vx1hc_glhEWUDoXmEEBG6TgKIH4dkiZqRA5LNILofRopZTzC_0T-Y0L0SJ2pMfl2HG5pKbskIIl9bSnSVdq4xY7M0akwUxBdH7F9x3EQ-5kYifwvNNYstEpdidgpXVmZ2ODrDoyvlb-sDHFSFnUpvE6mFRlbn-VvgmlADwbt0G_7A03-wV_UaT8kDlhMD93lI8oeqF-ucGL6A5BEXwqrWW7PduWVdVk1KJIjwIF2hIKNRYtIkm8ZhgAMEOi0IORO4lEEp-mxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
‼️
هیجان‌زده شدن یک نفر در خرم‌آباد از شعار بزن که خوب می‌زنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104257" target="_blank">📅 21:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa_ouZPQjt2G1dP6pPOjSZZjVMtRzOCrlnu-zyY6dxlZvuXnX4CKwjfuMh732KCHNx9YiOPjcMiFa9HYNQTlPlr5GMQY86dfOFupZjvBo6hSQOl99YEqMQ2Hsx1tzayAyuSwkCJvyyKf3zk-DJWEk5_2ADyckcwJdYJh1gFuUGHLptKHDe2BLHcbmobu8Kf2r8EdB6fG0MqIBiRzmp60LEAULjj8sOj9KYvlTlaKQBAm_WpMuNBM3OetUG766BQCzPl5TSnytjiQ750nW_IKu70BLqQUbQ-bqIeWwVQX819HFgcDKNDqrdcxEHZW30pwKClHjMkgK9pGrg9ZFvVIKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏆
آخرین‌رده‌بندی توپ‌طلا تا پایان ماه آگوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104256" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMmk95Z0bQhUs55GF6sKpX_I0jVWeymGFME7gxCX7XHT9QbQpn1DoGQ3kUvMAtABgmoWw9AlI0D-sJGDeILqSIDLVmMtQEcYtebdvOiLUdPRKDDyfH8xHhwDGJsx65m8N6zElXku_ByOV_2yEzgE7pxNVua5_RDQYfQYujZRrKV06haPTW0aUvaVVobPyFDrlzzHtKOAySsMG8GaCJ-mp8wzq_jj-00JR-o1JMChbQrbC-F1FmeshFPZH5mnvHe-QXhuUx6c4MgxAHiPMdYzo5O2v3MkPvQekOA3Mf6LyTSfU8QFIQgsL8asz4NwN32oRK1C1nSfp30aVvafcqvaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
رایو وایکانو
🆚
آلاوز
🇪🇸
🗓
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش‌بینی
💵
واریز و برداشت ارزی و ریالی
❗️
💰
۲۰٪ بونوس روی بالاترین واریز روزانه
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/104255" target="_blank">📅 20:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815fa09b1e.mp4?token=S5RwAXmIZQzRXZZwWkUM39EH3ia7ZCN5hkFqzKlbO5vI5EL9bqUWtqkdwa84qeYzSN6FMHqJ-j8u60o81ukHhmOSZjo6aGe7m-FRz9wudu-Ycy19j5r3BFyriSpM3adN4ewkWfCBSUjOWy6u6t9dIp5VjEFqCEQYnVT1_zj3XOzOzIx_i3n3QH4DS5awKeypkp8c3-sSRph9Rbrire2-zG0qZ7kr8E3qE9CILBuDEXA-PTZexVVF0_uWdEMqLFH0uCkCc6wFmrmx7MG77bgfv3CIfqJdFhFeo54m73myfj6j8SJ4ID0BX_fNtjFzLCeOCYt2mbTA2rZ70LMfw_Ly3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815fa09b1e.mp4?token=S5RwAXmIZQzRXZZwWkUM39EH3ia7ZCN5hkFqzKlbO5vI5EL9bqUWtqkdwa84qeYzSN6FMHqJ-j8u60o81ukHhmOSZjo6aGe7m-FRz9wudu-Ycy19j5r3BFyriSpM3adN4ewkWfCBSUjOWy6u6t9dIp5VjEFqCEQYnVT1_zj3XOzOzIx_i3n3QH4DS5awKeypkp8c3-sSRph9Rbrire2-zG0qZ7kr8E3qE9CILBuDEXA-PTZexVVF0_uWdEMqLFH0uCkCc6wFmrmx7MG77bgfv3CIfqJdFhFeo54m73myfj6j8SJ4ID0BX_fNtjFzLCeOCYt2mbTA2rZ70LMfw_Ly3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
لیواکوویچ سنگربان احتمالی جدید بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104254" target="_blank">📅 20:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05150752d5.mp4?token=L04jcx8iu-CNhmJyi_wrJJHGSUtEklUtdfM46Ah_CzFtcnZVsCPNo-w6LeSI8VXm9ly17AzDo5J8zNKBWu5o486xwBJj27PW2jG0BW8p3KmMStpdCELvHAjhPbYOiNP_WilnmmP_mweAG_r3mVCKmTdz60D29cPiWvHQRTAcjrobZyLA6OHHtJDmxX6TGkRXEtlVtFufzk2OHkAOiRxgreg_JDy27yTdKX8QK_5I11StpciwrACVO2ctIlfA67BWLANJh486xMOFyrJNg-u97A72ODJhIiQxBnPxYDOO16BkwkQF4llftwrKyMyIO3K2VSjyKIk2AaAua6fhS34rTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05150752d5.mp4?token=L04jcx8iu-CNhmJyi_wrJJHGSUtEklUtdfM46Ah_CzFtcnZVsCPNo-w6LeSI8VXm9ly17AzDo5J8zNKBWu5o486xwBJj27PW2jG0BW8p3KmMStpdCELvHAjhPbYOiNP_WilnmmP_mweAG_r3mVCKmTdz60D29cPiWvHQRTAcjrobZyLA6OHHtJDmxX6TGkRXEtlVtFufzk2OHkAOiRxgreg_JDy27yTdKX8QK_5I11StpciwrACVO2ctIlfA67BWLANJh486xMOFyrJNg-u97A72ODJhIiQxBnPxYDOO16BkwkQF4llftwrKyMyIO3K2VSjyKIk2AaAua6fhS34rTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇹🇷
ایزاک کارنی، یک هواداری که به خاطر علاقه به محمد صلاح و باشگاه لیورپول شناخته می‌شود، اخیراً در صفحه اینستاگرام خود، پیامی برای محمد صلاح منتشر کرد و برای او آرزوی موفقیت کرد. او به شهر ترابزون سفر کرد و با محمد صلاح دیدار کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104253" target="_blank">📅 20:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/338c9ad977.mp4?token=TbRWCBHn-jgomcqW3lGhF7f-fCh_L-Wmkz6ByvNZDtdiDzPkHy0QAPI2wE56HBsS-bfvwJpvaXLB4m9liE0C4lUdxu-tm_dN8d5FXS17pJeITglp7d7KFBgnQESuffS2MMov7T5sXy1-STL2WghPUsnlxERTJoZ-SG7QzJ5r4emzWguJuz3_Xg0LaO0Eye_1JI78VgXvVlfSWbV06N1KxD0NAsZ202_xVu08VnxCUNDGdWBBgLOJvW8cEM0Ayx8EbT9Z_npJPadbHv8ZnoC9txt4ld5UhPbvrvHNzc1eZ9nMn3e3i7CTEnctYcVDiqEPEXqR4UTwFG0H6b2CAQ0HXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/338c9ad977.mp4?token=TbRWCBHn-jgomcqW3lGhF7f-fCh_L-Wmkz6ByvNZDtdiDzPkHy0QAPI2wE56HBsS-bfvwJpvaXLB4m9liE0C4lUdxu-tm_dN8d5FXS17pJeITglp7d7KFBgnQESuffS2MMov7T5sXy1-STL2WghPUsnlxERTJoZ-SG7QzJ5r4emzWguJuz3_Xg0LaO0Eye_1JI78VgXvVlfSWbV06N1KxD0NAsZ202_xVu08VnxCUNDGdWBBgLOJvW8cEM0Ayx8EbT9Z_npJPadbHv8ZnoC9txt4ld5UhPbvrvHNzc1eZ9nMn3e3i7CTEnctYcVDiqEPEXqR4UTwFG0H6b2CAQ0HXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از گل مرادمند به پرسپولیس در فینال جام حذفی سال ۱۴۰۲، هزاران استقلالی در ورزشگاه آزادی اشک شوق ریختن که جاویدنام مهرداد مشتاقی هم بین اونا بود. روحت شاد و تولدت در آسمان‌ها مبارک بزرگمرد ایران
💙
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104252" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104247">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fbnkCvTl48s0P36PePbN0KgvGuyo2NzdeKqONBCbPS8EBLMNXUXa1kysSQiWqwbASF8_2nyF64VxSUhGs05G1QoQxr3UXBCoWFmSeyRBcFbb2n6Z8PNnBWbwotpGpt1th7zVAu6WKzvJ_m2BovKk0HeeyZNpsV0LrXTddHg-D1prgkWlFvNhZvOScATNi7d5AUyqCI-1Egxntn3mAdSL6OKoSivQKmUhtyS14potifJqx5j9F_-HJ4KLjMQ6FxBOx0C0hDJEFPCaA5K8yISAd9VgUppGa-WtVp2ZLZgkr7nSrple59vimDP0r7rrWldvSzudGDkbVtz6CNHPo6diHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgqcbAvKHYaGH0EQiHiaMldfxI6VAQF9IDFjg4b8OxEmkKcUL7euVsPxpwREkkFOERq9FtD_31Xp4viA-0PNVoTqOXbb5T06E1EwC2Zj9V69sxyxVhgjoSpPH0zCkwr6I0Hqipb9ClzpwJg2DcBpa96vK5hFSHSJU9urB0KUqvaZS57J1PLhzg8GtC6XxWcegCe2mupa4rs8P8TreAoLwWyRyvjJ_RgIt7kx8kZCe5RqTpWu1RtGBw6N6tNGv0PEtOanIuKclracUGSt4-iohRCIFnMqUwr2Fata3W03pVac72HF0bm9WrMO0Be9eVKh-qbyviERqt-uEQs9NQeHGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdZNMl_zYCB4nwCZbhKnlySROANG6lqNtkRklVwrvDtqgbyajOJrOT33R4w2YfJPspvjjHowFCUpp0XqwehYKJFf3y06Iov6BdZ_upuIfxbbZ8dtuPptNaIDhG-XkpZ5xb3KrzIhvPsDDFjm5eX9qyfRejfXVcKOLEP4OQi_aH-m4BODtm_8I0-IaLZhYtNKOllxRK2DWr-2atm4vAWjshnbYRIEdeBBOMXlbGz_r5L47Wfv0a2EV28w-13_NwfHWAEhGV4mf6PeDpQoDUkaWUlg-iMwaOhrlCnFVZ4QMYqIG8gbOOMKSmzoSABTM0gRQKalB71RJ0D1dk2M_ZrcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXbxvPG-qFIy5CGl50p1bsCoFt0QhcD3kuab-s4Y0DrIJpOamNmhThveorssbgAAr-EFyqSSPmyUola74_vK1StVqn8gk09eDw-76wXZddu1HpFvSfkJdpVoxmwaHhHtMWMQh0C-3Yc23DM8Or69W6KgTeClquEW4XyaX0Myxpky_TKZKYPHcC_JKGPtCW2e-8WkK7O1V6WJTEebgWOV0lKWx6DNNFbcWqEaRb78R_wgwCYyIDNFfn3GIvLGXu-6VZxWSHRtaj85RKQObxJBXQV4AxvGO9djesrQpIpORFsXuTPr_v7SgToKQhnWSzn9QA6vQF2fC6tLrCo-d0p7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrnM40i4x1rRYxZ83dyfmRH6PLWFiIliF6fhwQut8LNxmi7-nBCamZhAj3jlQ3e9sqQoLn4Ah2Tz_wvZ_r5ou2cpo1FFht7hbl7-O6Tb9FkXWnuWZF_JiVe2dhISB2nl-Rlpl6qDCywXGiSazMNXcEbCXw5gws5_YcJ8uEPXMsO0MxLzfdPMtjDPliFKx_SgLmH-VrFRCAfAbYaT2LRJfzH_6JkFgAx5btCAQj4gU8TmzogLIFWOobgK_vAZ7mTYyql-INZyGipe6nPevkRYfpnehWkad1xoIgeQtNdd8nVuX1xd6TBhQcW_FEz19Zivxye2gQTALIBFcCh1YfHFrw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
هوادار پرسپولیس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104247" target="_blank">📅 19:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104246">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdpfcaAjh9Z7Lez6ntqOi8iSv_qR4i4cauZfJqAFMAXpjNAMQ0pOql1Ri4urRtR0WTkt9fzUFM8sI-iw8mdTDcyQJCYMc0FfBo-Q-OFh9yGH74QsSSL0ZRLc-hCjT_XfWZdze1tUffNl1qWaauf7Z-wy1qw5kW7TjlwpfKMSJwdvjtQrAHmr3z1x_BMZxCzzS2OQm3ARWy8M7IH5HrlHDZ59mPPd5ppQe1C1z671CCdNB14PnIKWnosfu1g7JkAADb6qg2Kqtgz9Iat-CwY9fbVfp9iqx6rt_MrJvxGCteooZsXGinCJDGrAPyGNXp1iSgNqFF-EwvemWJJ2dFTJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
😍
پست
خداحافظی منیر الحدادی به هواداران استقلال
ممنونم استقلال!
💙
همیشه همه‌چیز آن‌طور که تصور می‌کنیم پیش نمی‌رود. شرایط باعث شد دوران حضورم در اینجا زودتر از چیزی که دوست داشتم به پایان برسد؛ اما با خودم خاطرات و چیزهایی می‌برم که کلمات قادر به بیانشان نیستند.
از هم‌تیمی‌هایم، کادر فنی و اجرایی و همه اعضای باشگاه که از همان روز اول کاری کردند احساس کنم در خانه خودم هستم، تشکر می‌کنم. همچنین تشکر ویژه‌ای از هواداران دارم؛ به‌خاطر تمام محبت و احترامی که همیشه به من نشان دادید.
امیدوارم روزی دوباره مسیرمان به هم برسد. با قلبی سرشار می‌روم و می‌دانم که این فصل از زندگی‌ام همیشه جایگاه ویژه‌ای در قلبم خواهد داشت.
تا دیداری دوباره
💙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104246" target="_blank">📅 19:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104245">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa83936b8.mp4?token=rF672uXCDVI3hjnuT82J6UVRh_tzDmUTvQHBYMZSqPB9Oi5rP09JTJ6tP0mIpVhcGNDjFGIeTnk9aGjDEiDvtXPd2yCDNQ6gkwqxcVyT5VzETRpiu5qawzjK7DBowNV7WKLLg25q8gF6L8mPyWR5hOBvwi1rzxvP4Kks03eT4xhfDNDcCLAzpvMEV2nBKG1uXi3T7wdrNlizePYHMA3GZrCelTvsGAH1NYQ5I7pXyJnnUb0OXqZrCyeqEmExkcBNzbHdceOiksQ3R0Y4vEPfagzTvtz9kV8DSrKNFfy2urcccEK3r2zz3E3Mrnw-WZHzRWVpT3u7GQ4PVmQvctPjTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa83936b8.mp4?token=rF672uXCDVI3hjnuT82J6UVRh_tzDmUTvQHBYMZSqPB9Oi5rP09JTJ6tP0mIpVhcGNDjFGIeTnk9aGjDEiDvtXPd2yCDNQ6gkwqxcVyT5VzETRpiu5qawzjK7DBowNV7WKLLg25q8gF6L8mPyWR5hOBvwi1rzxvP4Kks03eT4xhfDNDcCLAzpvMEV2nBKG1uXi3T7wdrNlizePYHMA3GZrCelTvsGAH1NYQ5I7pXyJnnUb0OXqZrCyeqEmExkcBNzbHdceOiksQ3R0Y4vEPfagzTvtz9kV8DSrKNFfy2urcccEK3r2zz3E3Mrnw-WZHzRWVpT3u7GQ4PVmQvctPjTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ریدمان لامین‌یامال در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104245" target="_blank">📅 19:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104244">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT-uxxAvaJnIuKFvMDVRiqG9STRkdYa22s3Y76EkWK4rgXt3imOfkRyMFIKA9b8tT35efqxzUWArnf0ZekjBpsn5hv9EuxJmcuMDly_c4slz5BkQObALJOJwm-QpW9_tLkJWi_Pi3w3g0GY9AdGMH8nlNWE4N1VyW0hPtbHYdAZSCWVdwJFlGhcSPNTyfs3AZ8MsVOwaS6vP8A5BCCAEd6ugGLpC60CvSAdGZuQUPSrZRGfXSq7tqJKZldA2PJzmf4HjHnuhPPCuicNj0RH--fyMeb4fmo-s3-4PkW8RN66zaX1QmHNSnBdHqrutZpH8lHz37hwhDkN9iCxtw68U4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
#فوووووری
؛ یکی از مدیران الوحده امارات در گفتگویی با رسانه الریاضیه این کشور اعلام کرد که رقم رضایت‌نامه محمد قربانی برای فروش این بازیکن به‌ پرسپولیس و سایر تیم‌های ایرانی و خارجی رقم 1.1 میلیون دلار است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104244" target="_blank">📅 19:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104243">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkb8QPVlThvJUDEkoITMbVe5KXNJ22t97s5TyWGpOmzsmCjxM2BHpNN60lstOKoxfHZcUyGJznaF8wiD1ARJxKaOVnTW9MQ5-4-If8bUlh95tN6RxQVia4jsDwlIZGj3B_WoPU297yxYz9tkTKTfn3ahwZu0zmlqD4sNY342jjlZoVcfcYcsrRUGIa1GtT2uNKnv93Vc32GpJ6GcZLV1chrA6D1SKOZSqD1S-gJatNyHDFweGxRtzrdvey3FmtpTjw6wAXiulcCB8EBy3fCja_HNFiMMdYip73jy8RAQFC2kiyDuLFVwSmSLkrJJolcIijTAg25eJ0fLiOPVAnnpbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
پرسپولیس امروز در دیداری تدارکاتی به مصاف آریو اسلامشهر رفت و با نتیجه ۴ بر ۲ به پایان رسید.
⚽️
گلزنان پرسپولیس: امیرحسین محمودی ('۳۲)، مهدی تیکدری ('۷۹ پنالتی)، پوریا شهرابادی ('۸۷)، محمدحسین صادقی ('۹۲)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104243" target="_blank">📅 18:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104242">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nzTZWoYTjqnklJCAkIVAfZoZbl7pgP-i4reve5scK8f_48KM90d6ajiqbMmzhUR4U3YJeIu0WYX04M_IRtp3PmJIvVtHP_OKnGhacyLnuAuxv-7OAs_ZyTVqkFwlCad1Ky8m_6OwI5UFyN2_Yuj9VcvBHBL7N64Ie2C2lwoHtAt6WMZq_Ye8fG1QF92YFlg7VSwJRLY1wWGnrxYTu5UBBNqvB6uTUj90rWbZswgjmSKGD30D_3cTZ_Sacep7ykV6XGYcJvedah5TZXcIA2zXBa6poD3ISWkhikScc7jioGanQhjK3pB1G6HGi5ZeIRkL3dSUb1i1oVhEJcVmJTv4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇮🇹
رومانو: تا این‌لحظه اینتر هیچ پیشنهادی از سوی بارسلونا برای جذب لائوتارو مارتینز دریافت نکرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104242" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104241">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8c825309.mp4?token=ov_xTLU-pFMLlkpX5739yjdYn65GiPjTzXocWZU3fGuUzeFC3Gs0K1lbhiwBtqa_017-e9_rP_AAF73JEhgdjNbb0sxY6U8wj7Y_kb0ud7Wys-TFGmY8zjk-q3J5zDxYRWzYeVX4M-KeoFbVRO5ezevDw07zB93e66rOL2_cIELE0gIEjO-X--xpXUvT_BJTr_BXoz5QpROYoViINkgFblnk7ks3X7hvW1YGv2b0EHqdqU1dIzvAIN1uIbmknPyLUo4PaFGG8dhtgZZtUn8tN77slaxYJYq0c_zFsT4THveEHwIiKTGQDCLYs9sY44XIX_js8ZgGiNoP8m2H1aXzFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8c825309.mp4?token=ov_xTLU-pFMLlkpX5739yjdYn65GiPjTzXocWZU3fGuUzeFC3Gs0K1lbhiwBtqa_017-e9_rP_AAF73JEhgdjNbb0sxY6U8wj7Y_kb0ud7Wys-TFGmY8zjk-q3J5zDxYRWzYeVX4M-KeoFbVRO5ezevDw07zB93e66rOL2_cIELE0gIEjO-X--xpXUvT_BJTr_BXoz5QpROYoViINkgFblnk7ks3X7hvW1YGv2b0EHqdqU1dIzvAIN1uIbmknPyLUo4PaFGG8dhtgZZtUn8tN77slaxYJYq0c_zFsT4THveEHwIiKTGQDCLYs9sY44XIX_js8ZgGiNoP8m2H1aXzFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
یه پسر دانشجوی ۲۱ ساله آمریکایی، به کمک هوش مصنوعی، یه مدل اونلی فنز به اسم «مایا» درست کرده و تونسته تو یه ماه اخیر ازش ۴۳ هزار دلار(۸ میلیارد) درآمد داشته باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104241" target="_blank">📅 18:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104240">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59287a8b90.mp4?token=NdM91P6fX4IesJGzq29pjbxsNH2AfhRD9CTJRKLFUYIJcApop9W3sHPiLiWtPiQPhTS6qZUr1fb40PgLlkr2tyh2vagsrlmu6P9tfCjLhMcklxGpX0edha-BJRt-IiZLKpNdTIHN6rzaqMS4eR4zbmbfLDi0hUlaTxiGOLNLtTa_yL5nFn9DuCJJRiXxTWst3MrvJ9DJnrRo4LbQW_kjOeJFuLWhG3Pq9mO1-O1m_2gCiDFb98MAod-ag6L1hyR2hL8GvPRt_xfgc7JdsUbWQ8wQHLMrhoM1nY1PwkEgmc5WLF-9BbCoLy88mBTM7psKvwR2ktGn2HeOE6MSWpwa1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59287a8b90.mp4?token=NdM91P6fX4IesJGzq29pjbxsNH2AfhRD9CTJRKLFUYIJcApop9W3sHPiLiWtPiQPhTS6qZUr1fb40PgLlkr2tyh2vagsrlmu6P9tfCjLhMcklxGpX0edha-BJRt-IiZLKpNdTIHN6rzaqMS4eR4zbmbfLDi0hUlaTxiGOLNLtTa_yL5nFn9DuCJJRiXxTWst3MrvJ9DJnrRo4LbQW_kjOeJFuLWhG3Pq9mO1-O1m_2gCiDFb98MAod-ag6L1hyR2hL8GvPRt_xfgc7JdsUbWQ8wQHLMrhoM1nY1PwkEgmc5WLF-9BbCoLy88mBTM7psKvwR2ktGn2HeOE6MSWpwa1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماشین جدید رضا گلزار، تنها رولز رویس کولینان منصوری ایران به ارزش 200 میلیارد تومن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104240" target="_blank">📅 18:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104239">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6c9d46d94.mp4?token=NTd5Dxz63Yag2i_eRW_dlJOYm0a5U0vTKWEtQdy3v72n5RrHqPjwwIPJsUZSVuXhavL9D69S3ug4NgCJPhYhjPDCqnbe6aRtzIuVDVEgcDJhfE4SbE-Z6tFLVUX55Sf9AdEhSE6QCagqPjV63i_6yvU09qc3_qusxKMKnIR0rWU3M2UB9lKVFkJC_LGKnIoPusetH5qEOpf9fLUxUk8TGRtxyHGqnC6qm3ek_yqbCspHJN0BZS7IiSiCSSkZNJwtwkrjQ6289aLiG8IAHBcE9ttf6ccHojLJYnkgC5xNIlZhDCR6dN-VAn7u0ETDseaJCI-_DGwcAFwdLJtGRRdvODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6c9d46d94.mp4?token=NTd5Dxz63Yag2i_eRW_dlJOYm0a5U0vTKWEtQdy3v72n5RrHqPjwwIPJsUZSVuXhavL9D69S3ug4NgCJPhYhjPDCqnbe6aRtzIuVDVEgcDJhfE4SbE-Z6tFLVUX55Sf9AdEhSE6QCagqPjV63i_6yvU09qc3_qusxKMKnIR0rWU3M2UB9lKVFkJC_LGKnIoPusetH5qEOpf9fLUxUk8TGRtxyHGqnC6qm3ek_yqbCspHJN0BZS7IiSiCSSkZNJwtwkrjQ6289aLiG8IAHBcE9ttf6ccHojLJYnkgC5xNIlZhDCR6dN-VAn7u0ETDseaJCI-_DGwcAFwdLJtGRRdvODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🎙
افشاگری ملیکا پارسادوست شاکی پرونده پژمان‌جمشیدی از اتفاقاتی که در این پرونده افتاد و منجر به شکایتش از پژمان جمشیدی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/104239" target="_blank">📅 17:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104238">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcca79f2bb.mp4?token=Mj2-v4S7UTFpzqPctLGLMAt3jZc0odALDCXAVK-i16p28833aFoteflHbCUdDAmH-F3Cg54PHRs7iQQ70CEvuYbMqGBtFdCcyD6mm-YxCzO0gAlivJtmDSwtmZm6-1Fy1EGNGlrdcGpbB1VYwO4oxGtqxF7H7zVx8IQ1KAW-L4XHHI-eCo5Bpz43h98Pc6UKmvIguls7798l5xrP6yi-lXzCA6EK_7YheJL8R-AO4Ci0DSUZFwhueQ_Ea_BtEJHtBbOFFCcaj9hxjzwFWzhHcPFLxG9sIj1QPNZl19y9XauGNtYtWHaU8gPIxvealQQA1gtoDWRpwkjKo-W_tCyhow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcca79f2bb.mp4?token=Mj2-v4S7UTFpzqPctLGLMAt3jZc0odALDCXAVK-i16p28833aFoteflHbCUdDAmH-F3Cg54PHRs7iQQ70CEvuYbMqGBtFdCcyD6mm-YxCzO0gAlivJtmDSwtmZm6-1Fy1EGNGlrdcGpbB1VYwO4oxGtqxF7H7zVx8IQ1KAW-L4XHHI-eCo5Bpz43h98Pc6UKmvIguls7798l5xrP6yi-lXzCA6EK_7YheJL8R-AO4Ci0DSUZFwhueQ_Ea_BtEJHtBbOFFCcaj9hxjzwFWzhHcPFLxG9sIj1QPNZl19y9XauGNtYtWHaU8gPIxvealQQA1gtoDWRpwkjKo-W_tCyhow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سمی‌ترین سرود یک‌تیم در مسابقات محلی مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104238" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104237">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
میدونستین تو ویپاری
با شارژ بالاتر از ۱۰۰ دلار ۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104237" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104236">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/104236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g29
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104236" target="_blank">📅 17:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104235">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
آخرین وضعیت استادیوم آزادی: آذرماه جدیدترین تاریخ اعلامی برای بازگشایی این استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104235" target="_blank">📅 17:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104234">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=hkLhgd7xI07RklFT_0B8et8OT6oFTE2qFTV9I_Su_JwZO4LPD13u8XhrYbyZ9DhNgtzuzSZY5z42RX_Vc2372LZ6KekSfaW7T7RK0P1qJtds3QwVTaWKSLPaUJUCji_GE4eUMgRGta9sfCZquL1faEQDsqubAcjFsaFfW2W-dz_SrGY_nYV8_aIFNvhsg1dHmS61eWhxWVXy0QOdEdWeo5oRAQRsavMj35ZGcCgzEz3NLK_cZgt2veKSCVN59dsoEdrlpUuoU1gvVmEZfKXK14eCD-MeG_piEeRwF5U_CWuarQddzsXOQCrQsFEe-n7INzbVu3bWG19ZCJzI1z5hWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1b80d7014.mp4?token=hkLhgd7xI07RklFT_0B8et8OT6oFTE2qFTV9I_Su_JwZO4LPD13u8XhrYbyZ9DhNgtzuzSZY5z42RX_Vc2372LZ6KekSfaW7T7RK0P1qJtds3QwVTaWKSLPaUJUCji_GE4eUMgRGta9sfCZquL1faEQDsqubAcjFsaFfW2W-dz_SrGY_nYV8_aIFNvhsg1dHmS61eWhxWVXy0QOdEdWeo5oRAQRsavMj35ZGcCgzEz3NLK_cZgt2veKSCVN59dsoEdrlpUuoU1gvVmEZfKXK14eCD-MeG_piEeRwF5U_CWuarQddzsXOQCrQsFEe-n7INzbVu3bWG19ZCJzI1z5hWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
مراسم خواستگاری دیشب کف نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104234" target="_blank">📅 16:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104233">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=uaCUIqBrYdanEdDFDK9ptx1CVYlqgzZP_8BzC04H9WbJMqi2-g6RSoCcK36oX6Kpaosk9JNeWFtnucv9rtSzZi4bj8lHYi0fnAICgWiClxNc-JQkNaPsNcahylFwBHbNFa5BpjKk-FUgjgGjh0TxOlJYJC1nx7Ndaf_5h9xZeUYGvenbetH-JhaWJ2WMgGvSoI4VDP5fyjNRouyc7d_Pg-FhGRwZU7fkasOO9eXKJnhLDLWhbMu1Mjhz05a_E3Hj8IOa0MfMBEsi0eqHoMeWj1AhgZnMXNh1D0bGmJpkI3spcY55l9XlYxxGabK0csm45otcl8-aAZEqVPEwM5wuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f3ef3446.mp4?token=uaCUIqBrYdanEdDFDK9ptx1CVYlqgzZP_8BzC04H9WbJMqi2-g6RSoCcK36oX6Kpaosk9JNeWFtnucv9rtSzZi4bj8lHYi0fnAICgWiClxNc-JQkNaPsNcahylFwBHbNFa5BpjKk-FUgjgGjh0TxOlJYJC1nx7Ndaf_5h9xZeUYGvenbetH-JhaWJ2WMgGvSoI4VDP5fyjNRouyc7d_Pg-FhGRwZU7fkasOO9eXKJnhLDLWhbMu1Mjhz05a_E3Hj8IOa0MfMBEsi0eqHoMeWj1AhgZnMXNh1D0bGmJpkI3spcY55l9XlYxxGabK0csm45otcl8-aAZEqVPEwM5wuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نحوه استقبال از تیجانی‌ریندرز توسط القادسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104233" target="_blank">📅 16:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104232">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=CdEaP2Rtf1l_QBtPdF7GKJ-AeGjw_k8sqB7UOVK8UIES_mR4clmCqQzyZzLgPy7QFCnLyVbnVnj5xCHckm3_lw_saUAoVeWxxRq1f9c2RlmRdDKMR1QPTbYHy4eYukRz7IKMjar3CJKBD5IHtHc38fkUiZl73-vCcff2Ca4MC5oWNJswGngPScRLdrIIw8gXZuVeI75iCTviz1G5YGIt3HuYSQg5yaav37HUMW_RP2aXe6nD-McRv07LcvAkUM006e3wxwaFUQCapHmgOekDOSpxaXHKfKSdqcF2w3YGuVtjKBtI1GrBv4eirwFS86ITK9na2UtnpZyClaLee4kfzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e04b7c878.mp4?token=CdEaP2Rtf1l_QBtPdF7GKJ-AeGjw_k8sqB7UOVK8UIES_mR4clmCqQzyZzLgPy7QFCnLyVbnVnj5xCHckm3_lw_saUAoVeWxxRq1f9c2RlmRdDKMR1QPTbYHy4eYukRz7IKMjar3CJKBD5IHtHc38fkUiZl73-vCcff2Ca4MC5oWNJswGngPScRLdrIIw8gXZuVeI75iCTviz1G5YGIt3HuYSQg5yaav37HUMW_RP2aXe6nD-McRv07LcvAkUM006e3wxwaFUQCapHmgOekDOSpxaXHKfKSdqcF2w3YGuVtjKBtI1GrBv4eirwFS86ITK9na2UtnpZyClaLee4kfzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
خاطره بامزه امیرحسین اصلانیان از اسطوره فوتبال ایران احمدرضا عابدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104232" target="_blank">📅 16:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104231">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=HDIsqZyS02cVjV-fvXmL2qzmDkM_WLmlKuhmfDlB2jVipd1qLapv6BkMDvGEpAqYcYkg8-1f-8MwIJguHN_JFBQmQjlWShdnF0foc_mJ1XXOa9NKr_Bq3HyxRYxNr7eUUMkwwm86np3xBeO4kMsIIBFWj_Q7bd_AWz-ihE7m3NdwIO8DHJ9Tm9CxsFCoJuDep7-mE0CGV6ReYo0LW31PRtZ7aAelEfgL8zqv0tOensICmLDimxBVnCc6ILR_qdTUvBvnNW9FrdGMgUWw99EnQ98kZ4Ecuq8jRaK9TotdBoVI29zcbs07Lm8bQAS6sX4ghpsVAJmzfbYFqIwVz0DGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea3bf7fa1.mp4?token=HDIsqZyS02cVjV-fvXmL2qzmDkM_WLmlKuhmfDlB2jVipd1qLapv6BkMDvGEpAqYcYkg8-1f-8MwIJguHN_JFBQmQjlWShdnF0foc_mJ1XXOa9NKr_Bq3HyxRYxNr7eUUMkwwm86np3xBeO4kMsIIBFWj_Q7bd_AWz-ihE7m3NdwIO8DHJ9Tm9CxsFCoJuDep7-mE0CGV6ReYo0LW31PRtZ7aAelEfgL8zqv0tOensICmLDimxBVnCc6ILR_qdTUvBvnNW9FrdGMgUWw99EnQ98kZ4Ecuq8jRaK9TotdBoVI29zcbs07Lm8bQAS6sX4ghpsVAJmzfbYFqIwVz0DGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
وقتی میخوای بیانیه یک باشگاه را یک نفس در ۳۰ ثانیه بخونی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104231" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104230">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af4cdf7dc.mp4?token=EPvQFRwCmp4DIUKBwcND60h6XTxAVlrdfkr2GRc0kVeyN15hR3k-BdHsbFcIFiqlZmYNGiPv3BFdsH8l7NQXfC3QMWCF7ARarVrPAux0GD4SP34GzLht5Ep2KvUZayBXHt365WxUoSQTZHz3PaGW5aGLSaFx0C4T7Kil6uEUlfWWgmFU8usFWT1pR4MrDAmddvd9se4amoQuXSrCFrX-6ox8U0B1Pmih_R7_KDj3yplvq1_vT7UBCs1C5oSP7U3jYqZJXAHM6zYxSABw5QXHF-Sco-hrnIxl1NdXxHHpN4K6RiiK4E8rmwd-uMUc76VJzprlwJIsBzIfaFolVX56aA8wX5hbonpjFwmbSsUUJMFDj3oNojs9e03cQCBdm3q0NKV5TsbH-bsrbCxclJaNemXQPCdFN4MglDtDlrjIb6XlhRZjrpg6oaT5ugxaxAk8xNAFmbkguBQfw3zWL2_lPI7dXG2J58lNqCMEsFHulBamGS-jH6NWgdojz2Sp-GcS1EygPpYhVj7CH0wACMnY2MvEBVh4yCZZLSQ9feFQmMNZR6tL-zhIJqShZUJPkuiN6_nkoFVwkvvnDWsUjC1eFnYqLbd6FLD3K1HjnuNq0yiRG-U4rQp6cNqY-nAgoDXxzlA6DsTT-LDkidb6oxeMPSFVeNh2LvZ36xtzbfrxTZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af4cdf7dc.mp4?token=EPvQFRwCmp4DIUKBwcND60h6XTxAVlrdfkr2GRc0kVeyN15hR3k-BdHsbFcIFiqlZmYNGiPv3BFdsH8l7NQXfC3QMWCF7ARarVrPAux0GD4SP34GzLht5Ep2KvUZayBXHt365WxUoSQTZHz3PaGW5aGLSaFx0C4T7Kil6uEUlfWWgmFU8usFWT1pR4MrDAmddvd9se4amoQuXSrCFrX-6ox8U0B1Pmih_R7_KDj3yplvq1_vT7UBCs1C5oSP7U3jYqZJXAHM6zYxSABw5QXHF-Sco-hrnIxl1NdXxHHpN4K6RiiK4E8rmwd-uMUc76VJzprlwJIsBzIfaFolVX56aA8wX5hbonpjFwmbSsUUJMFDj3oNojs9e03cQCBdm3q0NKV5TsbH-bsrbCxclJaNemXQPCdFN4MglDtDlrjIb6XlhRZjrpg6oaT5ugxaxAk8xNAFmbkguBQfw3zWL2_lPI7dXG2J58lNqCMEsFHulBamGS-jH6NWgdojz2Sp-GcS1EygPpYhVj7CH0wACMnY2MvEBVh4yCZZLSQ9feFQmMNZR6tL-zhIJqShZUJPkuiN6_nkoFVwkvvnDWsUjC1eFnYqLbd6FLD3K1HjnuNq0yiRG-U4rQp6cNqY-nAgoDXxzlA6DsTT-LDkidb6oxeMPSFVeNh2LvZ36xtzbfrxTZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
کیفیت دو چیز در استادیوم‌های فوتبال ایران تغییر نمی‌کنه؛ اول چمن‌های بازی، دوم ساندویچ‌هاش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104230" target="_blank">📅 15:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104229">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af1fb314e.mp4?token=P0QGGSNGUbBSxcxRnOqxjiEG0yoWj8oa3atRjLp2gN6ICInqehlmC4wGwpCwrjGbgvMCc3ognDjJ4NGlQbsJk3kdyPLBczs8jwkL6xTxxkqOFNwvz4lwWNWRvUk56u5HWBbjRuPBry2uUJ0MuoNkMZYevYFOKayFxgaJNPH2J0_XigYwMSe210AbyBmT2uJ24oHSgywF6k_m4oA0li22PAdvntNJpkMKyRJgVsonxzrlzUnU2YIiuxi-Zk1shRrZQSEVGdfM4kfvBQPX2PitDg515oT70iST7pc82QyDls7LynEePbrzHefrlblvKFzGAldAlyCHSU43EyKltHpNEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af1fb314e.mp4?token=P0QGGSNGUbBSxcxRnOqxjiEG0yoWj8oa3atRjLp2gN6ICInqehlmC4wGwpCwrjGbgvMCc3ognDjJ4NGlQbsJk3kdyPLBczs8jwkL6xTxxkqOFNwvz4lwWNWRvUk56u5HWBbjRuPBry2uUJ0MuoNkMZYevYFOKayFxgaJNPH2J0_XigYwMSe210AbyBmT2uJ24oHSgywF6k_m4oA0li22PAdvntNJpkMKyRJgVsonxzrlzUnU2YIiuxi-Zk1shRrZQSEVGdfM4kfvBQPX2PitDg515oT70iST7pc82QyDls7LynEePbrzHefrlblvKFzGAldAlyCHSU43EyKltHpNEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇪🇸
🇪🇸
وضعیت خط میانی بارسلونا و رئال مادرید در ال کلاسیکوهای این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104229" target="_blank">📅 14:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104228">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8411590ba1.mp4?token=rDLHHdzKMUc-_enRzkgzE2Mq-vkbeHtCjcO7DZ72lh6sry7mW_u8XtsOhydp_pH-mjC5qOwKkTJ_dTGepee6vWIw3TWdQv2n-VBiJl5bJqbrdBizrj7Lqqbvwsi7eFLgQHvbiSpZq9iBI96ZEvDxR0yRvWgzJ1TPngyKlB71BMAc-TkUmGZuDIBIggX03CIuyyQI5tnnpHYShs8kdJzvwMdY9PB4t-4tPNoZVzsqbb_E_K7Rr-u_Nae6f1Wc-fK6gqyM4j8KzP4Zr-biEeMIP7ObkNhk1NzwQWZqZOh1Ic2_E10YTL_5SF1U1u2JSp-Q7F4StDVVqpb2iE58jFObag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8411590ba1.mp4?token=rDLHHdzKMUc-_enRzkgzE2Mq-vkbeHtCjcO7DZ72lh6sry7mW_u8XtsOhydp_pH-mjC5qOwKkTJ_dTGepee6vWIw3TWdQv2n-VBiJl5bJqbrdBizrj7Lqqbvwsi7eFLgQHvbiSpZq9iBI96ZEvDxR0yRvWgzJ1TPngyKlB71BMAc-TkUmGZuDIBIggX03CIuyyQI5tnnpHYShs8kdJzvwMdY9PB4t-4tPNoZVzsqbb_E_K7Rr-u_Nae6f1Wc-fK6gqyM4j8KzP4Zr-biEeMIP7ObkNhk1NzwQWZqZOh1Ic2_E10YTL_5SF1U1u2JSp-Q7F4StDVVqpb2iE58jFObag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
هواداران فجرسپاسی در بازی دیشب
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104228" target="_blank">📅 14:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104227">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15540c4079.mp4?token=VlsxX-ffRIhPRqsxtkj_TDVIC-CKkpmpebpS2PDCRNqUSH7IBkCkGCr_UQ3CnlbVhOsBtF-CAkzg0aFRuvzgi5C8nGaawZ2aGSbjYBVmmC8tCasEZ_gXUerot4jnhwjgUesOM3I-Y1d9_SPcGelPWwtsy7akMAiCBF2b6RY2vLHceBgzMEA48B0K506r17T-E40BL1FU4GS_aY8g1r-2RhttVzqp5ybrcWjEJ3HYbaj7KoNymbPWSd-hqciqTUCBXkzF_4gA2JSRqpG1KL_ewjVKJuB4446rcsH9zbv2aNHfgpZMWr92eQu-2GO-LC8ceLETUyr2FJir98bkfiTUsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15540c4079.mp4?token=VlsxX-ffRIhPRqsxtkj_TDVIC-CKkpmpebpS2PDCRNqUSH7IBkCkGCr_UQ3CnlbVhOsBtF-CAkzg0aFRuvzgi5C8nGaawZ2aGSbjYBVmmC8tCasEZ_gXUerot4jnhwjgUesOM3I-Y1d9_SPcGelPWwtsy7akMAiCBF2b6RY2vLHceBgzMEA48B0K506r17T-E40BL1FU4GS_aY8g1r-2RhttVzqp5ybrcWjEJ3HYbaj7KoNymbPWSd-hqciqTUCBXkzF_4gA2JSRqpG1KL_ewjVKJuB4446rcsH9zbv2aNHfgpZMWr92eQu-2GO-LC8ceLETUyr2FJir98bkfiTUsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
متفاوت‌ترین جشن ممکن؛ یک کیسه پول پاداش برای بازیکنان؛ جشن متفاوت در رختکن دینامو تیرانا؛ رئیس باشگاه پس از صعود به پلی‌آف لیگ کنفرانس اروپا، با یک کیسه پر از پول وارد رختکن شد و میان بازیکنان توزیع کرد.
آردین بارزی با این حرکت غیرمنتظره، پاداش صعود تیمش را به بازیکنان پرداخت کرد و جشن رختکن را به صحنه‌ای متفاوت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104227" target="_blank">📅 14:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104226">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqfCMx4yCNuAwNj8YLguAGJfAcXdeIWuNZnoBrQcC-ZtNN2n7joXWuYrcrW_HDV72ulxaaf11csCIiZ1rRlRwz_Brt2ml8oGJAL-0IgJoalJZLbsemuOv6IADamuxSXZ5JOxdCL7XlaPjjHWHeT7aCEoZy6AQlRA4jSP3WjzOIyMA2AXg46N68U-rxckDnzHiuV4wcK-2ei1coP7bOUX4mfkAviamryP-x7i1wIRt5OLtKDNMcSBJ2CFYIiYT4QdtmgUVo615w-T1vvCtF0ZZNPr5qQ6xoJIy0ay2gohhLIwpXvZw09ejcI8u0HeX6IkbeZVjg5Fj3vyw_6N1Uy4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: بارسلونا از جذب آلوارز ناامید نشده و دنبال راهی هست تا در ۱۱ روز پایانی نقل‌وانتقالات بتونه این‌انتقال رو انجام بده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104226" target="_blank">📅 13:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104225">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab172d319.mp4?token=qg_28GfkA0ZVIwqEJH-_9zyDZ4eJWLppBZBdwaeZFgNPGIZD1p82fZ6lIjBI7mpF7VZWd2RF-LgWYmlvQdVkOlADdPIllZNWX-T2dcqhcbtuhKI69eWqtCgEya9Yq66hLEafScdtrIOBQ4FakOI5P7HvMNgyMkOzgTmkwm_0RDdWV48d4e6CvAG8LolPEhw__m8OvZOhD_Yglit_gau5fg0mmTYHdS_CmH6ZfL6aZT61993SCanG9CCHdks7sizhJfiAeFoBd2btxpXLfpvRzFlGJq5I99z4R51ODiaAHFZi9_eEqIZEaiy49JasCPZT_oXGO4dHUcAiR78zz0Qs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab172d319.mp4?token=qg_28GfkA0ZVIwqEJH-_9zyDZ4eJWLppBZBdwaeZFgNPGIZD1p82fZ6lIjBI7mpF7VZWd2RF-LgWYmlvQdVkOlADdPIllZNWX-T2dcqhcbtuhKI69eWqtCgEya9Yq66hLEafScdtrIOBQ4FakOI5P7HvMNgyMkOzgTmkwm_0RDdWV48d4e6CvAG8LolPEhw__m8OvZOhD_Yglit_gau5fg0mmTYHdS_CmH6ZfL6aZT61993SCanG9CCHdks7sizhJfiAeFoBd2btxpXLfpvRzFlGJq5I99z4R51ODiaAHFZi9_eEqIZEaiy49JasCPZT_oXGO4dHUcAiR78zz0Qs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
خروج صداوسیما از ماتریکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104225" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104224">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">▶️
🇪🇸
هایلایت بازی شب گذشته بارسلونا 2-1 الاهلی مصر با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/104224" target="_blank">📅 13:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104223">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ccac38661.mp4?token=uNmo0NNwWQW4ib_V5bEQ_Rxgc9V7HVUKrgCoOK9u-1DFRHYx56DkkJlOMDvOq59Ydn2VtWiXRni4g-7QEIhUoe9pCNr8litw_zI0EoGde3miDssXEAaBixgnipRbyTcLVfCaeHn5eyVzCNF65vRks1Xn8IZBKsOUANREi5ofL2Sqo651ixOxzcjo1AkxQZQ2MIFQ8OANgLKcBWM9joBJdEIF_8xFv--GpwnMb2tbowRekZyUzG5XPVJVLl1XoHdfhMBLq9VjRrlAdAhgHSvOyci4GG1gTv7pXhcthKPx42f1NaOUvZvUpYvJQzVUe-ydtYNHGsIHLc6nqdAmQ1ozLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ccac38661.mp4?token=uNmo0NNwWQW4ib_V5bEQ_Rxgc9V7HVUKrgCoOK9u-1DFRHYx56DkkJlOMDvOq59Ydn2VtWiXRni4g-7QEIhUoe9pCNr8litw_zI0EoGde3miDssXEAaBixgnipRbyTcLVfCaeHn5eyVzCNF65vRks1Xn8IZBKsOUANREi5ofL2Sqo651ixOxzcjo1AkxQZQ2MIFQ8OANgLKcBWM9joBJdEIF_8xFv--GpwnMb2tbowRekZyUzG5XPVJVLl1XoHdfhMBLq9VjRrlAdAhgHSvOyci4GG1gTv7pXhcthKPx42f1NaOUvZvUpYvJQzVUe-ydtYNHGsIHLc6nqdAmQ1ozLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇩🇪
قوی بمون، جمال موسیالا.
❤️
💪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104223" target="_blank">📅 13:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104222">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNr4_ZVUCGqJjROOMza_YAGYuHoyqyCKVjr93AhZxV2NCzXl_AYrEVZaZqPWrrFzQSl7vAQ8ttStbnMMVO33cK2WeubXWTZe574nBnGw6SGxzw-uh5Xs7SdKhj0dGkZ7IodVfC2mtOJjoSmZVGH8Nfp1pjkpcss55BtjucZ0VUXtwpdDRmuAyeXMNu42vgnbd2cAam1f3aDbsukABN7IvSM2JDawSP8kaDzgQpZDCvMhpebzBiZAAqK33LtRnEg_s-avoWBw_CpQZw5oM3cZu-wr9cAIEXDDxSl5pcNZ78AnNTIZMODrwxeSqppBJcx5r_1F71KMN8SVgl0RbTLfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمامی ورزشگاه‌های فصل‌جدید پریمیرلیگ انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104222" target="_blank">📅 12:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104221">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1d403113.mp4?token=taCGp1mZJ_zRhUoysne0VjFpZvdRE9nJ8mk-3DagBoYXmjHDHhDo-_pZel4CZvE9r0GdjZdRVGSUwieugqBT2tKhjimeAn30ibF_bv1pJAaEkJV-SPfC9Bfz8c3vXjM1K8sguLM6bkX28C8pNYy0M00MQZLG3lXdFZ6QxqVKEUpbzfSdzCEwrOIn5B0ALqfahZIYB7dYopejvHZTucXvSZMfcWRO0mZV8q1e-36C8x-zsp1DdWI_UyUAagcGp0kdPdqGpS4ZMoulc08HSbSGpoHgUPvT6TRK55BzOYzHFGCreONCDSad3tkidjJZJyDxko7t8xaYwU7Zh0sHEdrSgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1d403113.mp4?token=taCGp1mZJ_zRhUoysne0VjFpZvdRE9nJ8mk-3DagBoYXmjHDHhDo-_pZel4CZvE9r0GdjZdRVGSUwieugqBT2tKhjimeAn30ibF_bv1pJAaEkJV-SPfC9Bfz8c3vXjM1K8sguLM6bkX28C8pNYy0M00MQZLG3lXdFZ6QxqVKEUpbzfSdzCEwrOIn5B0ALqfahZIYB7dYopejvHZTucXvSZMfcWRO0mZV8q1e-36C8x-zsp1DdWI_UyUAagcGp0kdPdqGpS4ZMoulc08HSbSGpoHgUPvT6TRK55BzOYzHFGCreONCDSad3tkidjJZJyDxko7t8xaYwU7Zh0sHEdrSgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
برگردیم به زمانی که گرت بیل به رئال مادرید پیوست و EA تصمیم گرفت به این شکل تو FIFA 14 پیوستنش به رئالو اعلام کنه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104221" target="_blank">📅 12:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104220">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
‼️
🎙
افشاگری داوود سید عباسی از شب‌گردی‌های دردسرساز ستاره‌های تیم ملی در لبنان برای دیدن داف‌های بیروت در سال 2000: زور هیچکس بهشون نمی‌رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104220" target="_blank">📅 11:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104219">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0abb8b5a2b.mp4?token=v7Mbqu3b_i6zpvFsChe-csD6zC3I7rzF0OUwQ7yeC8C1UqFxapxC5Z48yGK5J63BH80tocnHCMSId9BRDwgasXdrr2oJUzMQs28kefzUH9L0i0B0MSe8AXpvzT7ILBu3FHlceG9vcj-A1sm8mKMvnWaAEPTAcg0nsVvHRCc3xGHdinDQAdY9Rfw7URKyEsJxFCvnNBXTc5VKzBr_92XIpZP5IoXwc7gHsBvDs80NczbpMoidPrwY2AvJoJEBjFt-BeWBzIsdCPoSByRmDRoKVgRXgudR7OjMPrsUSFkmm2ehr86z_i4zG-sTDL7kr7RRE4zxm9c2Z3WlgA1xN3SuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0abb8b5a2b.mp4?token=v7Mbqu3b_i6zpvFsChe-csD6zC3I7rzF0OUwQ7yeC8C1UqFxapxC5Z48yGK5J63BH80tocnHCMSId9BRDwgasXdrr2oJUzMQs28kefzUH9L0i0B0MSe8AXpvzT7ILBu3FHlceG9vcj-A1sm8mKMvnWaAEPTAcg0nsVvHRCc3xGHdinDQAdY9Rfw7URKyEsJxFCvnNBXTc5VKzBr_92XIpZP5IoXwc7gHsBvDs80NczbpMoidPrwY2AvJoJEBjFt-BeWBzIsdCPoSByRmDRoKVgRXgudR7OjMPrsUSFkmm2ehr86z_i4zG-sTDL7kr7RRE4zxm9c2Z3WlgA1xN3SuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه تند هومن افاضلی به نکونام: کاری که با محمد ربیعی شد بعدها با خود نکونام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/104219" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104218">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813ecb9de7.mp4?token=mtbcl7y45bNyp-pjKDb-baffNhvcC8sXuPYfn166p-9XBFzXmLlBSRPb67aEclTatp-WD0sodMKZbyhaAOREP-3pFT3oX9ImZ2j8185AkMu4C90zxChZNetWjvagLnnzkazHc4RfaNZfgfmQRyjqxJ9aLbWmZfwnwJbZU6C9pObogTXJz530coG20rqx4k2ZrUCvSEQYFmZ6sIH77Rj7YoHXrrjp_EswiHJNsv6AhGvF8izMrGgQLvhTzs98aqOxO35FqW_hdtgMqn0vtKJsG3iLi9aLcKejqmR93m0R4GrfIrRE-uWFdUOhc9cO1UjWUScZrxRLY6pt--zT3b7jvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813ecb9de7.mp4?token=mtbcl7y45bNyp-pjKDb-baffNhvcC8sXuPYfn166p-9XBFzXmLlBSRPb67aEclTatp-WD0sodMKZbyhaAOREP-3pFT3oX9ImZ2j8185AkMu4C90zxChZNetWjvagLnnzkazHc4RfaNZfgfmQRyjqxJ9aLbWmZfwnwJbZU6C9pObogTXJz530coG20rqx4k2ZrUCvSEQYFmZ6sIH77Rj7YoHXrrjp_EswiHJNsv6AhGvF8izMrGgQLvhTzs98aqOxO35FqW_hdtgMqn0vtKJsG3iLi9aLcKejqmR93m0R4GrfIrRE-uWFdUOhc9cO1UjWUScZrxRLY6pt--zT3b7jvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
‼️
حمایت ترانه علیدوستی از ملیکا پارسا شاکی پرونده پژمان جمشیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104218" target="_blank">📅 11:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104217">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452261b723.mp4?token=e1AeEU1J9Ri4_aPxX7L7m6zv2a7D8d5V7VrQkxryoeazUMEVdTUof9EGwTknDe2Lc1pSWYW5h90hPjMxcbqs_qRCDBwxfdMlDt6z-OsdY04aYvJ_V-fWJS6CX7U1mXyvhupblPRxC--vbhwcf7ykTtzOqXdQ1pA4A6Hg0z023kVbxASkAG0MCIhCrkLwamYJmrks2ilX6ZSO4jRGKkQaZj8ZwV3b8Vv6xpZBC5CPoEyzNiKzsksm3z36wfi3lWClkc1gyIzuNQ2KYMng_5Q3kvzUadPW3paqvPdhb58R8guzki4VMbGOzlxDMMAongf3iUOhvsZezmR607Do1Ft-K4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452261b723.mp4?token=e1AeEU1J9Ri4_aPxX7L7m6zv2a7D8d5V7VrQkxryoeazUMEVdTUof9EGwTknDe2Lc1pSWYW5h90hPjMxcbqs_qRCDBwxfdMlDt6z-OsdY04aYvJ_V-fWJS6CX7U1mXyvhupblPRxC--vbhwcf7ykTtzOqXdQ1pA4A6Hg0z023kVbxASkAG0MCIhCrkLwamYJmrks2ilX6ZSO4jRGKkQaZj8ZwV3b8Vv6xpZBC5CPoEyzNiKzsksm3z36wfi3lWClkc1gyIzuNQ2KYMng_5Q3kvzUadPW3paqvPdhb58R8guzki4VMbGOzlxDMMAongf3iUOhvsZezmR607Do1Ft-K4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسل‌جدید هواداران در استادیوم‌های ایران
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104217" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104216">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/104216" class="tg-doc-link" target="_blank">دانلود</a>
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
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104216" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104215">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMkftkE-pQSfDitEbKu5r_35lhvayhXHb6gsWeXRhvpYLLuUiacRAEFbv7ovUHTbB961QGnx439A9ILKhwWn8uXNXUHCBC755sLESBn-mOAEMkQtbZosvgQkhFfaNITL81s_DsC72algJZ_9dkaxtfWiwBRnkW_lHKiSmBBnqKQ_tc4mb2NAXiZOnbrRfrEODZdDd06Q06pdkzcGlWuhdzBtuJpt5bQLV89zB7n4pCAMEikfJkZgQ0IKZ3hty1AA9jaXWz-sdwJEbhhaxBBi2N9yzJ0kEwTh3Bq_RAufrbdZTZ1Dkv9i-1G9orBczdWZZsu9zwonQ1C3L5G0zpeg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r29
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104215" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104214">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95dab32c4.mp4?token=RVn3stWizLCLlMcNVepHUVOIXYvwb3K7RcReREVEUhmtvVaPukgndELpYhFAENyNDkdcLE058b7wE1qxfjREiGN6VQvN-JRTOPDQn4cLEDRzf7zZQTLFfroOFWWHr9QAnqFArk-_htRdi86LKiXEloMFPg_m1SSaJZC1pUpz91BMcmJPfwbvN_tRANFsy4WYMLndkyRWk-mS7HrzGeezXKv276SsQQc_18LFv8krfAWZke1Y9m1mLYrMSQeB7qOeBlVWaixNz7cRUDwj40t2NiqwdddfbIj1xMpZu9ffPC-QuOj_230A8eQ27Tzweg04gzYo5pih0tUhUHl9tJj1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95dab32c4.mp4?token=RVn3stWizLCLlMcNVepHUVOIXYvwb3K7RcReREVEUhmtvVaPukgndELpYhFAENyNDkdcLE058b7wE1qxfjREiGN6VQvN-JRTOPDQn4cLEDRzf7zZQTLFfroOFWWHr9QAnqFArk-_htRdi86LKiXEloMFPg_m1SSaJZC1pUpz91BMcmJPfwbvN_tRANFsy4WYMLndkyRWk-mS7HrzGeezXKv276SsQQc_18LFv8krfAWZke1Y9m1mLYrMSQeB7qOeBlVWaixNz7cRUDwj40t2NiqwdddfbIj1xMpZu9ffPC-QuOj_230A8eQ27Tzweg04gzYo5pih0tUhUHl9tJj1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تمرینات نفس‌گیر وینیسیوس برای دلبری از ژوزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104214" target="_blank">📅 10:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104211">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuEXkPS39CFEQMZMnrlEktacUoHxKx0VFU59W-Zzo_dkXa4L6eAgKfzWfJ561ESGf73FilFmihc1HntyPgW3Jqad4G8nGcxl7YzeZzbWXrLJlDVaBzAluanMzs5MRbgO2KehXyGDBIDD92TvKBQQ-S0vO6iBENkkOs4JgH6cLfBPZZ9qOAXqSo5dgTWUdyfiemywp8dz4rsQ0I7g0owTkdyjtgXhF4l-mvceQF1htXSrKoVKvYzhItpyzU0e9bKFP0fPdd0lfpQmHp0MCMaLgCLIIFWD8_EQ-Mil-B_AYRr4XWWhd5ntFPB1ODlWhCiDOP1ZsUzpBj1OfEF1V-tHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oe8rAzkKQ7GZpZizZDLLuUZXGdBOWWOgCyl3e3UEnN5GlECAZh4yDc6Jq_SdxMha5uEaAtOAGe2-EJ9VYiQ2G-bWFkeriuBDeQFSASN-2pwRVwNmB-upbjtmDzswlGCMC6hRKAWow0r6ZjGX2_O6y0IGIJA5Lpq5ltoUrSEYJi4RNJFTaCx8Nt4vX8TemRYV37TexKJ8I3CPiuKnov_ZADZxdwoechzDnRvQtjpEGjL1_DLfhOKNvPjFsvEUIN3z7N5LmCAa2AdR_VFh_Auw3fp-KAdEmeH-PGas3bPrDSdtM9gN0_yGTPkU5dEHqywLNe0ybwDqJV_5-7ih4XOvlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gy09337AQftdV2pDWiX9-IJ5-q3cQhu42DxFZhdxx6d8TO90lVmQkgLm5wFq_XCM5pyX9BU3nx-n9GV5NMdoULyr6iiJvMtd5Zg_0FLTILW8Rq7OLnZyq_YEH4QgzT3hzcGdPSAeY4kCJO23af8h9yWBjutbCehzmZ239dwSg8Zlr11RGrCBW2z7CDrIqv0rqQIN7Uy2I5iTEbi_rvJ1HTcEcF86fjqq-b1qf4iXRidbZ-QFSU3t2otEKM0JxKNsj9A4o1uJPwm114Xb4G9sPzhB0lCdjKK_u_t44aOSDZL5K57wvGhhJKPcWUn-MafKioSqCC2eAArdLjjNFRDISQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
هوادار فجرسپاسی در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104211" target="_blank">📅 10:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104210">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268128aa94.mp4?token=h9Vk7IAAqr5T4CaCjOmMDTCF27xdAiR-uBDH5yfCXrkL73gkmi5qNSMxW8ZkTGNYSx1i_NvCnrqgTEcps-GZ22NS-cdnFdvQUcmvI5cSAjXi8XrVXKSn_GZX8DDkg9m_pPN5kCATOYGN5aK55934lQtA7Ernd-ISKUXy8ZVYDYfx19UGxhm5jTE7H29h978j8Y1gkRU8lfiAdp2qYYx_7uLXqBHqi9JsRcHPCaNYUQsOfirCbmtm91foBlqiRusPMmqH5PynnstysMO3tFVoojHw_lGxjG5VJeyCT7eb3gNLfof4z0wpSt5Jf5HNscjdFbqlotI8zBDVCgzBKBx_24V_qyQBCNHvG8D6HYLSh2IvUaqYCb3-9gGPpKPlyacKjghfRCD9pzCz_bK-oFrvn4PX0fgrOdYK_KQELxU9XbzHOYioZDaY_yDzVwN3zpdn2f1b-T4xDbVITFNviGPsKCVt3naNRhv66EjULUTI7Fwef9NnCbq7jk5sXzCzkDcviizUreHdVgOMHCO9N98wyx85BVbjNTBkLtQcjcYZcT2kzywtT08U4bUiQ06Vk7Rn3AfxLOqT6QwqmKo5qh4I3B4s3D5I6Pgo8VpNRWaAu9yYr09Yrhw3chtsFCEwEssGsqs8Ifc3fhHVhK1j196zBuV0OTZwXKT3tdAUDKgmrUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268128aa94.mp4?token=h9Vk7IAAqr5T4CaCjOmMDTCF27xdAiR-uBDH5yfCXrkL73gkmi5qNSMxW8ZkTGNYSx1i_NvCnrqgTEcps-GZ22NS-cdnFdvQUcmvI5cSAjXi8XrVXKSn_GZX8DDkg9m_pPN5kCATOYGN5aK55934lQtA7Ernd-ISKUXy8ZVYDYfx19UGxhm5jTE7H29h978j8Y1gkRU8lfiAdp2qYYx_7uLXqBHqi9JsRcHPCaNYUQsOfirCbmtm91foBlqiRusPMmqH5PynnstysMO3tFVoojHw_lGxjG5VJeyCT7eb3gNLfof4z0wpSt5Jf5HNscjdFbqlotI8zBDVCgzBKBx_24V_qyQBCNHvG8D6HYLSh2IvUaqYCb3-9gGPpKPlyacKjghfRCD9pzCz_bK-oFrvn4PX0fgrOdYK_KQELxU9XbzHOYioZDaY_yDzVwN3zpdn2f1b-T4xDbVITFNviGPsKCVt3naNRhv66EjULUTI7Fwef9NnCbq7jk5sXzCzkDcviizUreHdVgOMHCO9N98wyx85BVbjNTBkLtQcjcYZcT2kzywtT08U4bUiQ06Vk7Rn3AfxLOqT6QwqmKo5qh4I3B4s3D5I6Pgo8VpNRWaAu9yYr09Yrhw3chtsFCEwEssGsqs8Ifc3fhHVhK1j196zBuV0OTZwXKT3tdAUDKgmrUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
فن‌کشتی بازی دیشب اینترمیامی و فیلادلفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/104210" target="_blank">📅 09:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104209">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08de822050.mp4?token=Mzz7odM9hDstZUeF4Ik26L0lSZWv1BBEKk4GG85MWRNsTP8BPNJd3vXZpJGhuUV97VbYURytS2BZeZM7ITxvQS5vsHuCUVH04Wtp-30bcOjo_aDG-isYAegJgXeMEbR9aB9IqNBFZu0cB5DGQKhwBXZ1UUqPHjC_ShJLZT4rLB7Ey9Fw1rUwUbuLgWog8VcvsShbgHWa8lHQ9ddjQ6FKGFyekz-mTFlLWXa4t5xAlEFcBL_YgZH1c4l-kijJa7KfI3v1XRCyH8F7CIyYjn_5WsKtird1rqYI9hM5qW3Rl8anPG7eNs7WfaBRowofLie6vNoOmp-R55_HYZCgtl48Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08de822050.mp4?token=Mzz7odM9hDstZUeF4Ik26L0lSZWv1BBEKk4GG85MWRNsTP8BPNJd3vXZpJGhuUV97VbYURytS2BZeZM7ITxvQS5vsHuCUVH04Wtp-30bcOjo_aDG-isYAegJgXeMEbR9aB9IqNBFZu0cB5DGQKhwBXZ1UUqPHjC_ShJLZT4rLB7Ey9Fw1rUwUbuLgWog8VcvsShbgHWa8lHQ9ddjQ6FKGFyekz-mTFlLWXa4t5xAlEFcBL_YgZH1c4l-kijJa7KfI3v1XRCyH8F7CIyYjn_5WsKtird1rqYI9hM5qW3Rl8anPG7eNs7WfaBRowofLie6vNoOmp-R55_HYZCgtl48Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
گلزنی لیونل‌مسی در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104209" target="_blank">📅 09:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104208">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiDE2VwIYdRTHX_Eqbiq7RLlw5m8qTtutwzbuK1TEkplkeSOsaEe0z8yeSoTv0Uu3Bs72E5IqZyJ77uxnn3E2CT_st23W5sJakXuwaxWA97DTaq26wONhy2CnJNFktcK3F-N4r2aNXB-btTuTFjPTdgrTJMts0t5kTJQj7DNV2jGSZ2JPw-46ZKWzdKNEbteaoMhUqTFrtKsnc644Q91RHVEI4FQBdY2W2pMNnCel-j-M_VIxYBJGufmLPb4U2TiY58fqxCELzfgQOiYo8y-keTT_2FAK2eYWCcOSTla5GkVHjKyu5QBi_c84ndb4cXIgQjL69KzmbCoP_K1iB-kOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/104208" target="_blank">📅 09:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104207">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d04c58120.mp4?token=NAK9aEBwLQyH4pcZOYevsA0gWFVAZZ27X2dkomRlBr4WSiuN7raakPUdfOb8uo0la9OjdHk49ep3oqg8ggc1j0jZjnQRrOSHpwDQSNSp3wxFOBoCgDxBe9PmS4IeMHt-TUJr74A1jdkeS_4FQxkdudQNBToMQ8KR-_wG2aJQGchkQTexaPdliHJNAWw8Rh0kpKk2VnA-HpCZBAl0DmKYJIxWWtuc7wofZtiKGxC4hTg6w4r_axYCjXX_OC6OS22svIOVb7EBh8-H5_GCXs61hxD98CQYJknvOxkutt40BygZZpGbCSh65mJG8NPpynJxkNwugjdEwxYmRHVG1pHvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d04c58120.mp4?token=NAK9aEBwLQyH4pcZOYevsA0gWFVAZZ27X2dkomRlBr4WSiuN7raakPUdfOb8uo0la9OjdHk49ep3oqg8ggc1j0jZjnQRrOSHpwDQSNSp3wxFOBoCgDxBe9PmS4IeMHt-TUJr74A1jdkeS_4FQxkdudQNBToMQ8KR-_wG2aJQGchkQTexaPdliHJNAWw8Rh0kpKk2VnA-HpCZBAl0DmKYJIxWWtuc7wofZtiKGxC4hTg6w4r_axYCjXX_OC6OS22svIOVb7EBh8-H5_GCXs61hxD98CQYJknvOxkutt40BygZZpGbCSh65mJG8NPpynJxkNwugjdEwxYmRHVG1pHvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
آرزوی دیدن دوباره آزادی برای هواداران!
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/104207" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104206">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9be7548134.mp4?token=VXFb4rvmCAO_vpkSXCdc1Oj1MVIC9VDqWuWVSINP2HS1rAOda43sftI7G1_KH36FISNiBrnMyCQkCr78bCq0DPLxrkU3Ri1PThvEajWCmV7ZELrYnFrRyGklTY41qadY8sFGbOwMNJq7v3RLQRlai7uxiKcELZ8oFRtwuinkeup3GD1kbIL0piqisRSgPmHwTzmIRK_2r4kCmPXCsWB19Lm6OmZ7G1cUBByNacxNoFLzI7obNJpYnXAfr1l5J0terjbVrc13IHkd4mu3R9EnaCEj0isZ50TxOg1xC9v9IRwu8DS0JmHhI18OzxfW1Sh7tOTo4yp6ZbVb_GDwGJ4n0GbbzbuH-TrvBA-sLkxqDS_Y6Fgr5BQDlxGujpRJhBQR8VcXvOTFXSXg5M4ksoK05BkzZMCJj5TkhRaK9Nz63_jAqcr_vWOr3V5A3Fx0bPhdN3iUO9cr_sRuae5_2YM5qQuWtBzaiM-NMTQ1Ergea7GY6kLTqU5Q8oE-lFlvw-q0JYWdBlRQJk6-OjzX0QRlznFy8jfshihdSDy68EpwgYOpfWLya4wzDe1sndAj9I6IjjkSKGX5KFVJke4h_8PX1YVWvLLcwvUVzOpb38izeEaA4n4znwQsvQ10K4RerHuaG8XMBx0kwnzw8EzkaU9l9JW426AjCu80wWfWiK7AhuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9be7548134.mp4?token=VXFb4rvmCAO_vpkSXCdc1Oj1MVIC9VDqWuWVSINP2HS1rAOda43sftI7G1_KH36FISNiBrnMyCQkCr78bCq0DPLxrkU3Ri1PThvEajWCmV7ZELrYnFrRyGklTY41qadY8sFGbOwMNJq7v3RLQRlai7uxiKcELZ8oFRtwuinkeup3GD1kbIL0piqisRSgPmHwTzmIRK_2r4kCmPXCsWB19Lm6OmZ7G1cUBByNacxNoFLzI7obNJpYnXAfr1l5J0terjbVrc13IHkd4mu3R9EnaCEj0isZ50TxOg1xC9v9IRwu8DS0JmHhI18OzxfW1Sh7tOTo4yp6ZbVb_GDwGJ4n0GbbzbuH-TrvBA-sLkxqDS_Y6Fgr5BQDlxGujpRJhBQR8VcXvOTFXSXg5M4ksoK05BkzZMCJj5TkhRaK9Nz63_jAqcr_vWOr3V5A3Fx0bPhdN3iUO9cr_sRuae5_2YM5qQuWtBzaiM-NMTQ1Ergea7GY6kLTqU5Q8oE-lFlvw-q0JYWdBlRQJk6-OjzX0QRlznFy8jfshihdSDy68EpwgYOpfWLya4wzDe1sndAj9I6IjjkSKGX5KFVJke4h_8PX1YVWvLLcwvUVzOpb38izeEaA4n4znwQsvQ10K4RerHuaG8XMBx0kwnzw8EzkaU9l9JW426AjCu80wWfWiK7AhuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
زادگاه‌زیبای اسطوره رونالدو در پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/104206" target="_blank">📅 09:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104205">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZaISrCIc7KNdETrM-F3RFLGXe7k-aidfPWq7NlCztMXDm8w6xJjzjbhg94xWHbIzV3pBkXiPED7q4gCqZYGq8goN9W4HT0LYGW9FaphFGIpY9rR7EOh8vAoRC9XSvspt-9Jfzw2HCIrfY9nDgRXLguEyJmS5HPAscd5gADd4kVLJzPTmJtArDyAHm_538Y0MSCVU4Uz12HwH6lVJ898znGY46F59-YbG2Dd4XLN8xe4ADkhJE0q3SVbtVJDz4KjCPxaqpgylMSvH2L-mqDoGlE1CfnwXzGAN2FV5Wo-YN8aXH58hC1lVK1ADDtG5Ak0sLf2vjJF5sQeofe8qKb1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇺🇸
ترامپ
: از این لحظه شدیدترین فشار اقتصادی تاریخ که تا به حال علیه یک کشور بوده، علیه جمهوری اسلامی اجرا می‌شود و‌ «هر کشوری» هرگونه کمکی از جمله اقتصادی، نفتی، صرافی و بیزنسی به ایران بکند را شدید‌ا مجازات می‌کنیم. این دیوانه‌ها گرفتار شدند و به آخر خط رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/104205" target="_blank">📅 08:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104204">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctLSOAQpeRw5_XAEj7lbN_weyZfQyN5aezxG7rSp3OKyZ9bU4KxrxwXlOraZJGlb4hw29g12xX95t9lee34zOSbx_PA0n4KsHBnbQW35M7uQF3T0kvm0AB8zSWRPdwfJ7pmNNqcyuZZ6GTTd6UNmVaaDrRvns26_OFnc2vQPgacREx7UJdAIBXl5RS1Qu1zhpk1PPkc3-WMaMFNLAexjgfX9pkwqSFgLdxA2328rLb4JxZuIfSvgqeQ-qN7bJUo6l0qpnNHbKmb_JOEkiclv5LyqHN3zjE9QL2_nIVVmppz8K98jelzIJKeEGaurorJTBUgqwRqtHKchFC-2NYC1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
افشاگری یک‌خبرنگار از دلایل عجیب و خنده دار عدم صدور کارتش برای ورود به استادیوم برای پوشش مسابقات لیگ‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/104204" target="_blank">📅 01:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104203">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185cc08019.mp4?token=h3BJ1Xc5zovMfNanpt6c9DK0uVUpSJiK-I2QR-clE36jPLJuJfnJEMwpI2285j_hEqQfjQpu-yrxfiOkvOp3rihDRjKRTUuGNYQTevmkeroPMQ63PwDi9bmRyD76ORuaMVaLGTA06aYhv5ntu88y_Q_f-zumICL5iRWoyZLWDQJO3UCH4ZFOoLWd4soVZWncneHaTFQqItZkSEGronf6z4BY4vjyzmq7KKnfzY5ihJTDhYlXCVK0z145gu1_wbOJWhVy2WhF5ngtlCzHdkT4xQIKhgsDNOCfGBH9_-1VjvY8dRwjmq-QEFTYXIrMGV4ZHmx1fsEUFKLfWiiPdixWhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185cc08019.mp4?token=h3BJ1Xc5zovMfNanpt6c9DK0uVUpSJiK-I2QR-clE36jPLJuJfnJEMwpI2285j_hEqQfjQpu-yrxfiOkvOp3rihDRjKRTUuGNYQTevmkeroPMQ63PwDi9bmRyD76ORuaMVaLGTA06aYhv5ntu88y_Q_f-zumICL5iRWoyZLWDQJO3UCH4ZFOoLWd4soVZWncneHaTFQqItZkSEGronf6z4BY4vjyzmq7KKnfzY5ihJTDhYlXCVK0z145gu1_wbOJWhVy2WhF5ngtlCzHdkT4xQIKhgsDNOCfGBH9_-1VjvY8dRwjmq-QEFTYXIrMGV4ZHmx1fsEUFKLfWiiPdixWhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚠️
یادآوری خاطرات تلخ برای پرسپولیسی‌ها توسط حامدلک در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/104203" target="_blank">📅 01:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
جدیدترین پیام هوادار روشن‌دل پرسپولیس: راضی از رفتن خیلی‌ها با چاشنی پیام برای یکی از مدیران پرسپولیس!
فقط هوادارای پشت‌سرش که هی سر به سرش میذارن بهش میگن علی‌پروین مادر...
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/104202" target="_blank">📅 01:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFBMwxF3j61S71rbqWqHvQ4NcBgcJRHhoRxF4nArQU26nFxVvtpjd_aPpUoZLnVSe2VbWNv-tIGWT6_29aHC46jzglBL2KWSz1PbP6PBIc219ZbEaGwuH4pyp6AOe5Q1AzlomcLNAshGwAUQi7dOhGI0oEDDniZWZ1BpmaR9Q3rkbSvUMya5I3Mkn0erlBd_We65lGt55E6RLBkvj6rOa1n_UG9Hk6nW59LCOcg6t6FpmgHu-Qi-ukZ8w9928TsiQZFf0J4S7Gm3lXNHvSf0ibBwa503OAfChEcpOSymKIe6BIesk1668ZrZ3sx0lhaIISSbsTc0vwy73cD25LH97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اورایلی درباره جدایی رودری از منچسترسیتی:
🔺
‏"همه می‌دانند که رودری چقدر بااستعداد است
‏و اینکه حضور او چقدر به عملکرد همه بازیکنان اطرافش کمک می‌کرد. حضور او، جریان بازی را تحت کنترل در می‌آورد
🔺
‏بنابراین، جدایی او یک ضرر بزرگ است، اما زمان سازگاری فرا رسیده است.
🔺
‏ما چند بازیکن جدید جذب کرده‌ایم و نمی‌دانیم آیا بازیکنان دیگری هم به ما خواهند پیوست یا خیر، بنابراین باید صبور باشیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/104201" target="_blank">📅 00:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0zBx00ZK_unztlHEkqWCEytaaco5xlh0GB_sLxwFGBY0cK72Fy45Sp66GByv9oDKmctE0a5AnA0ViCGVZaKqVBiHPMN501CYoCdl3BSaKK2LJ8MWGhnEJ9g5cb0MUFJsxeDlo2_7VYLuyRpe_TJBvi-bkb0DqWvs1fuJ7aQFZxzUQ8QVftE_QarLibWEwwICRhYYnDjcPbKa7FnP8uSC4wwENFaTT-dCUVrodk5HuqWWpefV_XPomNBi5Y69i9OI5Vvjunvhoh7chEOmgJ-o0L2Fd7LnjIjcI-Sgg6BQTn-3eoKgDAGmGVfCvoL9fR6m_xRiKddF5-sydC7JtPvqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: انزو مارسکا سرمربی سیتی شدیدا خواهان جذب انزو فرناندز شده. سیتیزن‌ها در روزهای پایانی نقل‌وانتقالات تمام تلاش خودشون رو برای جذب این بازیکن بکار میبرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104200" target="_blank">📅 00:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2nfqHw864nJh751YXuSCCOYg_soyTrlEHcs67iTEEAYinoOxcWj0np9_ZazEgmuW_sPIbRdTn4wEm1pOmxpeeUXxhNhRALsIICnBF4rHp-BJEm_E9-9CB0Cmc3R2v_0GFxkJKC9FoAT7fa-xeeCNStJ3k-6xiFXWlO8hY9dP7-J8d4qJ25gJB-iBsorT7Z68hguGX7LNNdpMFIa-DjsUBw1-z05pI-nptLzKnSS5hJrrIEDGg-nSvtDF7T-QPKlw5sKUT2gj7hiqeeaFAEx4rJCCPuoUAfiFpN_7YJ-a2F1YYhnJ7aowOt2PP7cPD1rP7g_9kb8Pdu21Fx-_RLJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
هفته‌اول لالیگا؛ برتری اتلتیکو در گام‌ نخست؛ جانشین کره‌ای آلوارز گل‌کاشت!
⚽️
اتلتیکومادرید
2️⃣
-
0️⃣
مالاگا
⚽️
⚽️
کانگ‌لی - الکس بائنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/104197" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaHugshshZItgVG3b4dzpcSOPf79M9tJY-B0bGRCa6p9uNw0rWRymv7tkmzrWRIefG61izorJaeuBDaygyzdr5pF6Jrz0LunbzB_sCLng6yx6D_xf4hZ75OqtZ1yy0SbpVkqWOIDxkCHpHqNXBVid8ItAVB2I2_vYO6DyNfeyk2yIYSs269a-xNikHd00tVIKBN7V-Z4sNmXMIDfiepWce5Iqq8oBwXMAzbqKXC0Mib-hHptNaWHY7QTxI6dwSA3b6aT-Tb-kPP00aOkYAewkWhuPhmiwjgp9zoEz9K0RUqhfH8PaMjiuWEpGdZvQjG2bkXT5xjPjtt7gSvHrB8xYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
دکو مدیر بارسلونا: قبل بسته شدن پنجره چندتا انتقال دیگه خواهیم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104196" target="_blank">📅 00:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9ViVJhZXdC0sWVEhymMKqX9bxZlO55AWkEI4vP7VFqmMNWu23LUrLBWlNu6uGMmj2zc7VKmb0czk1fHWZGgt2uDayEpWhb0j3v7LT1P1fyqQrlMZtBSN9TYFHYvxsLkAd8QzXBap1WLN-jhh1mdeeCCDT69qdfPHZPOSgyv8AM40l3xEZ9ewFQLe86SDrNOf5ZHNtd_Q8JpfyFBIEdrUTC3AxrWrOYEh74HTzKY9co32AZ0d_pkeX9jwwbC5JwFcMX9xktVXa4G5Kls2EdUiCUhWJef-NOSBLKF_Jwqm4DA_fa68_TAOzaO7bseSOVCwmytO8JwwgNHgDq6reUJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هانسی فلیک :
«ما به دنبال جذب مهاجم هستیم. دکو تا اینجا کار فوق‌العاده‌ای انجام داده. امیدوارم و کاملا فکر می‌کنم که این موضوع نهایی شده باشه. من به دکو اعتماد دارم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/104195" target="_blank">📅 00:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104191">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b7fd471b8.mp4?token=TyqBeBQipUFAqbRwG0KS1d5cXD2gukiUYGSGHm_yGG6W3rgpkX_aYtg5aIO89rMmePbLaBGYid8bYRdGKuQo2tN6Gy-5mz9ASGWsbzSGqarsUuHeE6IxuLHx9sBuhQUw2E0MlwbN-6xODS59H7oJzdcvK_zxHw1zBw_tpN1RPn8sVP5OhA_ha-x-4Fc7qhoZazj4hcBhOqTO5XEuYIMpfPyJ6E7hlR3y_J1E8E4yw-oJDDbC7vPAFy_cIuZSRFvQJ4mqU_FpeDfv3ZDak6ZvO1Gz6zY77czYbAcTUMwI-20lPmkods53KUx6DnfE5bjfoHRsBHp4SM486_EkM5jhJgSXv_qR3xwRmzkl07ySvILAhP1KHGbqZvAo6qXoBgnVkZ7qnrCca2t3BkfyVi4-YNM0XMkwnc75Qk36aJoNaRqI34FBvCtY0HxPK80W3RNUMLqLKHXNkYD2DLS8OGh-Ugu4FQ0_rRHQ0-N-dEMbTp68IggWgTisAFkQMb0SxFf4uBj1ne1TJYyqvUagcIxPJjcMFb1Al6r4VHRUL-B4w8J4er6EodwMiLmJ-pRri1QJv_-z-YnhDuy8LKKRQ0q_aMj4EHMkwdnyfhFwj26JqvMZWQONXkW84l_8bZzb8ly9s-06kdRWaUBXCz5cNMlFIpq5DZowsj0N-LP3WNEfB6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b7fd471b8.mp4?token=TyqBeBQipUFAqbRwG0KS1d5cXD2gukiUYGSGHm_yGG6W3rgpkX_aYtg5aIO89rMmePbLaBGYid8bYRdGKuQo2tN6Gy-5mz9ASGWsbzSGqarsUuHeE6IxuLHx9sBuhQUw2E0MlwbN-6xODS59H7oJzdcvK_zxHw1zBw_tpN1RPn8sVP5OhA_ha-x-4Fc7qhoZazj4hcBhOqTO5XEuYIMpfPyJ6E7hlR3y_J1E8E4yw-oJDDbC7vPAFy_cIuZSRFvQJ4mqU_FpeDfv3ZDak6ZvO1Gz6zY77czYbAcTUMwI-20lPmkods53KUx6DnfE5bjfoHRsBHp4SM486_EkM5jhJgSXv_qR3xwRmzkl07ySvILAhP1KHGbqZvAo6qXoBgnVkZ7qnrCca2t3BkfyVi4-YNM0XMkwnc75Qk36aJoNaRqI34FBvCtY0HxPK80W3RNUMLqLKHXNkYD2DLS8OGh-Ugu4FQ0_rRHQ0-N-dEMbTp68IggWgTisAFkQMb0SxFf4uBj1ne1TJYyqvUagcIxPJjcMFb1Al6r4VHRUL-B4w8J4er6EodwMiLmJ-pRri1QJv_-z-YnhDuy8LKKRQ0q_aMj4EHMkwdnyfhFwj26JqvMZWQONXkW84l_8bZzb8ly9s-06kdRWaUBXCz5cNMlFIpq5DZowsj0N-LP3WNEfB6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌های بازی بارسلونا ۲-۱ الاهلی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/104191" target="_blank">📅 23:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104190">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/065326b085.mp4?token=aNinth9LptZSM2iZPgLQHLqJJf3c_kttsCq9_8DN1F1Yi0ACfuo3wvnCA4skGcdzrRMZAfTfnyeA0k9WvZLVVtdcm0iQL8stqHzjfIbXkTzkAZo9b06EBKuj2xDxSWKl_X8_xLJtkDb6wAV041oHIF533yQyloXtqqy2H7jssPwDVXhFEL7cdqxbR8U2QFOos2zQAaYLMRVsberwUNrE8aX7ygtjiOjcubeRahuR1OndgGGQKwjb54tck0YLklvneZFbZINA4-OkQEHWcvDMAYVjeL9iA2qd8MugwLEr72LbQ8IWpckZSGzmOetqJB2bGUT0hKZGexxdGRPEPB2TxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/065326b085.mp4?token=aNinth9LptZSM2iZPgLQHLqJJf3c_kttsCq9_8DN1F1Yi0ACfuo3wvnCA4skGcdzrRMZAfTfnyeA0k9WvZLVVtdcm0iQL8stqHzjfIbXkTzkAZo9b06EBKuj2xDxSWKl_X8_xLJtkDb6wAV041oHIF533yQyloXtqqy2H7jssPwDVXhFEL7cdqxbR8U2QFOos2zQAaYLMRVsberwUNrE8aX7ygtjiOjcubeRahuR1OndgGGQKwjb54tck0YLklvneZFbZINA4-OkQEHWcvDMAYVjeL9iA2qd8MugwLEr72LbQ8IWpckZSGzmOetqJB2bGUT0hKZGexxdGRPEPB2TxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن خلیلی: اگر استقلال تصمیم بگیرد دربی رفت 90-10 باشد چرا که نه، ‌اتفاق بدی نیست که این قانون یکبار اجرا شود/ من الان «مهرزاد معدنچی» پرسپولیسم؛ ‌این هجمه‌ها کار دشمنان قدیمی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/104190" target="_blank">📅 23:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104189">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae9b74973.mp4?token=GFLtzWLg847hn591ti6IUkIVW4N6JWlPXU4kFchHVWoVl5CXxNRLycSWlHgSmNfTlYQIjnqNhObs44sscpru8COCCo5IaYEEw5AaT5_RjPE49kPljWJGB49YPZ7CPycOSQKN8TnaVjpBPivmIT5ZUg0wTFJ6lWDT4g060eQrAVs3mfY8E_udMA7uE3gPVBetlP0KfEJm5lraeealgHXjWQMmkOVerxe9LUwjnJ380f7bZI22w_PzH8mYswdFpcGMTfK4g4WMaalWJvBv0knWvTmD1ZA7eZSYFArCeFVjZPBtu2SJhgxSwVV7bhwJiXAo8AbbnvFfBWq2WrX4-_6W5C2kFvKBNUpOOSDn8DXoqveSzcFwGLz4vAnTMbE3X366Z3p0bW00_6N66O3Lho29UsFSQtk31SiT_ZMLZdpyvs6WruEOHa--1ICcy5U-ume_vIR8Q5-25eQ1v5LPvVXl16lIemfGmseCpbYD4gzh41ScrfW4XBrVBZqZQpBC2obgHZxfH8CKgvfXBCUWfGPZ2fA0PHl5M_GQurhe7hIesal20l9JuLFBsgf2yHqQ5YjKgXsttXTI15SPKbYrobPXu9o3_WUtE9w8oqDOOtG4fVQWWO849nkR0g_vBhp7CbCm1UJlw-lxaABWEGhmeT1lmPYl3WG5XsGp4X2L4HmGolE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae9b74973.mp4?token=GFLtzWLg847hn591ti6IUkIVW4N6JWlPXU4kFchHVWoVl5CXxNRLycSWlHgSmNfTlYQIjnqNhObs44sscpru8COCCo5IaYEEw5AaT5_RjPE49kPljWJGB49YPZ7CPycOSQKN8TnaVjpBPivmIT5ZUg0wTFJ6lWDT4g060eQrAVs3mfY8E_udMA7uE3gPVBetlP0KfEJm5lraeealgHXjWQMmkOVerxe9LUwjnJ380f7bZI22w_PzH8mYswdFpcGMTfK4g4WMaalWJvBv0knWvTmD1ZA7eZSYFArCeFVjZPBtu2SJhgxSwVV7bhwJiXAo8AbbnvFfBWq2WrX4-_6W5C2kFvKBNUpOOSDn8DXoqveSzcFwGLz4vAnTMbE3X366Z3p0bW00_6N66O3Lho29UsFSQtk31SiT_ZMLZdpyvs6WruEOHa--1ICcy5U-ume_vIR8Q5-25eQ1v5LPvVXl16lIemfGmseCpbYD4gzh41ScrfW4XBrVBZqZQpBC2obgHZxfH8CKgvfXBCUWfGPZ2fA0PHl5M_GQurhe7hIesal20l9JuLFBsgf2yHqQ5YjKgXsttXTI15SPKbYrobPXu9o3_WUtE9w8oqDOOtG4fVQWWO849nkR0g_vBhp7CbCm1UJlw-lxaABWEGhmeT1lmPYl3WG5XsGp4X2L4HmGolE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
نمی‌دانم شیر استقلال از کجا آمده!؟
🔴
مدیر روابط عمومی پرسپولیس: شیر به حق به پرسپولیس می‌رسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/104189" target="_blank">📅 22:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104188">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/702ffd5ee9.mp4?token=qV6NyP6DQhJvMQKHEYzdBe0KpDHacCUgzbsnpGz1yh_yInIDevqWWb57mZf2FTNQ85EAmPAmb3sCjoKXUN6ARitd3K053QONvfdjiWifyGAT75Z6bX70JFhuNWA8oUn4NT2KqOlzRgVnkozLS6jS8S0JhLysvIaDpahvlX6il1hfdXJXSO7W4pATmNc_ASjfxV_NmBmN9pHQThgWXH_-No0pti_v5NX5UUtihmT2nZuY8axooKeQt6_8XqHYeczdMjcaJCthXe9FyldEnxVyPBmgnnauFSbFmDBcbcHc5FUIzw3B_xYQvovC-5t2mRKXxRgwgty5MBcRZO7AlryxuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/702ffd5ee9.mp4?token=qV6NyP6DQhJvMQKHEYzdBe0KpDHacCUgzbsnpGz1yh_yInIDevqWWb57mZf2FTNQ85EAmPAmb3sCjoKXUN6ARitd3K053QONvfdjiWifyGAT75Z6bX70JFhuNWA8oUn4NT2KqOlzRgVnkozLS6jS8S0JhLysvIaDpahvlX6il1hfdXJXSO7W4pATmNc_ASjfxV_NmBmN9pHQThgWXH_-No0pti_v5NX5UUtihmT2nZuY8axooKeQt6_8XqHYeczdMjcaJCthXe9FyldEnxVyPBmgnnauFSbFmDBcbcHc5FUIzw3B_xYQvovC-5t2mRKXxRgwgty5MBcRZO7AlryxuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
کنعانی‌زادگان: ناراحتی اورنوف طبیعی است ولی همگی تابع تارتار هستیم/ دوست دارم یک گل هم نزنم ولی قهرمان شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/104188" target="_blank">📅 22:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104187">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_Egx_LgjgzhGXXZkG5RvUsmpaCH8sMuQv_5lRCsiOWu327HezV1-x_XR4gkMkJQHayJ3rAqiWX17J1K1vQ1JBP_gvvci-uBmIq65fwvr6JkK6ev5cQIBE7FA_pc-Wjmssl_pTdvyjNgJuUiD_1Zb0dGHJCmRJbC_2MajeKrY1DyG6-SiJvEnGSVKcgjVl0tdi90HszPAr9_TuMFtWi_jqonzVplym9UN-q7d3Rmrj0HNmCvpZM1d11UttUGbaok_jlprS6wniuhXQxLTso_7F0Cs1SpDoO13xmMSdYl_aEwnxCXWL3EbeK6wqR3ccONlfzkH0eJ0ZNN6IpLtyjpBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
📊
جدول لیگ برتر پس از پایان هفته دوم با صدرنشینی پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/104187" target="_blank">📅 22:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104186">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a4eaad83a.mp4?token=bAEdkCMYSupAKylMPbjyhZBg6nZ03M46I2A99KDoh4L0QhkZYiHcmIqzXIMxUniB_yvkVa3OzmTPUVhf_KwaLqZePx8B1C5zwal_MXpVrGYo4lTo0sc3j8ppcqNcbDrN7iMzgkjfo2SDYDECKOJlmlBjRkEY7SCdJpD4CWbtfSglilpYyowUL7Bt0MyiZBQtvW3lcA1FEeDa0lUKBGqjNANr1laxu5o7Z1FkXUk_DED5qabr7FHnbQQtmkDjT-lEuCnrd3PP91IhRcRCQpsZtVg2hNTN9ndfa4mKEG121PujIAGOYja3a6ICcUWo1F6JoxiYjvMob-SQ46faX62Nsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a4eaad83a.mp4?token=bAEdkCMYSupAKylMPbjyhZBg6nZ03M46I2A99KDoh4L0QhkZYiHcmIqzXIMxUniB_yvkVa3OzmTPUVhf_KwaLqZePx8B1C5zwal_MXpVrGYo4lTo0sc3j8ppcqNcbDrN7iMzgkjfo2SDYDECKOJlmlBjRkEY7SCdJpD4CWbtfSglilpYyowUL7Bt0MyiZBQtvW3lcA1FEeDa0lUKBGqjNANr1laxu5o7Z1FkXUk_DED5qabr7FHnbQQtmkDjT-lEuCnrd3PP91IhRcRCQpsZtVg2hNTN9ndfa4mKEG121PujIAGOYja3a6ICcUWo1F6JoxiYjvMob-SQ46faX62Nsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی بازگشا، سخنگوی باشگاه پرسپولیس: اگر تضمین بدهند در بازی برگشت با تراکتور هواداران حضور داشته باشند، آنوقت می‌توانیم تصمیم بگیریم که بازی رفت با تماشاگر باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/104186" target="_blank">📅 22:24 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104185">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85bc3fae83.mp4?token=j-Qs_bdZY9xOMdoDY87VXfOzPwKgwd2-cN2BCfZW7tgjLLPMQXulkDrIrflYBJ2sbgNZ8hiGv7HGUeRxEtgelOZrkG3et_PfzVt_Aq4EtQ4r6Upna54gDRsrJtzbLI7NvmTUfPLmEUXLLDhHUmJsvaNVRimBCVanAeU2V7OLXG0scWdGNHaK6aqZJa1PMXpRvSPuj21LNLm3zrWTYLaITMrGlnjotXWDRYM7uUnKMafULBv6ZypGO8gRjRNwsGZwio23ekZeHl7Q7hu_PKj-saQYT_9oD3lum8MqCpb8_XSz4uz6c28iKaZdFwwJLdG_-zo54HQpS8ezVOn6uJ3v7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85bc3fae83.mp4?token=j-Qs_bdZY9xOMdoDY87VXfOzPwKgwd2-cN2BCfZW7tgjLLPMQXulkDrIrflYBJ2sbgNZ8hiGv7HGUeRxEtgelOZrkG3et_PfzVt_Aq4EtQ4r6Upna54gDRsrJtzbLI7NvmTUfPLmEUXLLDhHUmJsvaNVRimBCVanAeU2V7OLXG0scWdGNHaK6aqZJa1PMXpRvSPuj21LNLm3zrWTYLaITMrGlnjotXWDRYM7uUnKMafULBv6ZypGO8gRjRNwsGZwio23ekZeHl7Q7hu_PKj-saQYT_9oD3lum8MqCpb8_XSz4uz6c28iKaZdFwwJLdG_-zo54HQpS8ezVOn6uJ3v7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
شهرآبادی، بازیکن پرسپولیس: امسال هدفمان قهرمانی است/ سال قبل تر از حضورم در استقلال به پرسپولیس رفتم اما قسمتم نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104185" target="_blank">📅 22:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104184">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43972e9198.mp4?token=gKqaI0cDCdupLAs9PZzl89-Fnur_H_hbmdaJg3m6Gulqnk_HUz91kiMPOC76yyI-koJkQ4dE46Qmp2kdOLlvrzT6JeSleFnQ6i5K5rFJ5KvIWTAQfewzu6U3hJFdoX9hCY6luRbMA2lqphAkmsnoklRuUUukoVro8rLEayx5L8CvHNz8G720GdmZOv9DtJZHhTXktz-mi4DbhjbEn7oTjBoV22UZcwzMB25Gs2cg65Nfrn6KjEWoHubi4LmpZGPigcqK2QIxRgyB2InI7YgtKqgrjRHqobfK3E-vQBDSUrE0Ej7KJp32llkjqdWqeAgtgMMlKc84mZKpS9WsbO7dK3-0IZQ9zH1PIFR85QxHrIVSwjuJa-Ac4QD9A2bzJUG9R8zo04K4eJ0SXzVxet624DCKMHYb3T9oGx3lbauKKAxa0A-wkHRpFWODZtCExEEty75Oi452ainH65N6ptAukJpPrT_Op8gu1sSSGb6uvZI5HAVvRuSME12tszs0_2ak_0uVeH-JPvJlDYBjlIv5bwpo1EsuEK7TaGonhw6bkLnDGmVHWZsuiBR8gFccfzawCduSr_ZtdC_3klj0WIQNK8_4A6LDe5a70h5slz7VJYU_9Zt9YQdrzwnHomLM2WWyLg97pIIEjGJn0u4OpQE2xkW7S_R9AqI4r2qpi1V4-QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43972e9198.mp4?token=gKqaI0cDCdupLAs9PZzl89-Fnur_H_hbmdaJg3m6Gulqnk_HUz91kiMPOC76yyI-koJkQ4dE46Qmp2kdOLlvrzT6JeSleFnQ6i5K5rFJ5KvIWTAQfewzu6U3hJFdoX9hCY6luRbMA2lqphAkmsnoklRuUUukoVro8rLEayx5L8CvHNz8G720GdmZOv9DtJZHhTXktz-mi4DbhjbEn7oTjBoV22UZcwzMB25Gs2cg65Nfrn6KjEWoHubi4LmpZGPigcqK2QIxRgyB2InI7YgtKqgrjRHqobfK3E-vQBDSUrE0Ej7KJp32llkjqdWqeAgtgMMlKc84mZKpS9WsbO7dK3-0IZQ9zH1PIFR85QxHrIVSwjuJa-Ac4QD9A2bzJUG9R8zo04K4eJ0SXzVxet624DCKMHYb3T9oGx3lbauKKAxa0A-wkHRpFWODZtCExEEty75Oi452ainH65N6ptAukJpPrT_Op8gu1sSSGb6uvZI5HAVvRuSME12tszs0_2ak_0uVeH-JPvJlDYBjlIv5bwpo1EsuEK7TaGonhw6bkLnDGmVHWZsuiBR8gFccfzawCduSr_ZtdC_3klj0WIQNK8_4A6LDe5a70h5slz7VJYU_9Zt9YQdrzwnHomLM2WWyLg97pIIEjGJn0u4OpQE2xkW7S_R9AqI4r2qpi1V4-QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🇮🇷
سوپرگل‌فولاد خوزستان مقابل شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/104184" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104183">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">▶️
🚨
🚨
🇮🇷
🇮🇷
خلاصه بازی پرگل و جذاب و دیدنی پرسپولیس و استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/104183" target="_blank">📅 21:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104182">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMa-mRIiopuMJF9ZOnebBh3dGnO_i0H2jatBHIT7UO1XUnU4AYByLcTO4d0tpPO3mDhhhCB1Fr81TKfTAuPWq56SulfX2R1zdEmMJR3icLPJNnyAsh_lZw-gMW51BNpmPyR_MOUs1Bbqzo9Be-WRR31QRrqQmAmGJbIuD3Ri7wftGwCSaOmX3z9lAnW6Vj2beEYicom07VTgWUIK8TCpU3qaoH3hX6nmMUxoMwBWKD99Prt6yxy3H8F-oz3HE77EBeXBh_Bu1KfEe75_7iBJiXJGCHpjg_m0CeOir-q7-Km9e_KqWuKwFxqApL9JIEiBj_x2H6aJ8IyYijZ6GMPgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
پایان‌بازی‌هفته‌دوم لیگ‌برتر ایران؛ بازی چشم‌نواز در شهر قدس؛ تیم تارتار برای رقبایش خط و نشان کشید
🇮🇷
پرسپولیس
😀
-
😃
استقلال خوزستان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/104182" target="_blank">📅 21:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104181">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a62ef1f46.mp4?token=e8rP8l3b2khuFvn7-hGhSZStCOlvh9lVJuQH6LOO68B6VsRUZugvk3p25uzuHeQjn6ecUDGrMJyFhTxGhLif8f4sETxZOwz76Sc0DOMONOeKF57e0bp6VrrE0LD_xGMLU2z9-G88WMRkW_MPKEmfmEkAGx78qxbYhTsIuZ4MZh-634xet6faAgd3P8V4aGpSn1xWkwnCVR3jz0asgrn9n0XSoC-mlTIJvK3ktXr0A2nftMgy_pW_XkwehVBAyqB5rCYPNuPRr2h1_Jv1Zd22hH_eUar8KtGPT9q9DmZv4ZU0PHbItfE-LoOGFY2t3jc5d6lpgU1sxwmySw7IzC5rFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a62ef1f46.mp4?token=e8rP8l3b2khuFvn7-hGhSZStCOlvh9lVJuQH6LOO68B6VsRUZugvk3p25uzuHeQjn6ecUDGrMJyFhTxGhLif8f4sETxZOwz76Sc0DOMONOeKF57e0bp6VrrE0LD_xGMLU2z9-G88WMRkW_MPKEmfmEkAGx78qxbYhTsIuZ4MZh-634xet6faAgd3P8V4aGpSn1xWkwnCVR3jz0asgrn9n0XSoC-mlTIJvK3ktXr0A2nftMgy_pW_XkwehVBAyqB5rCYPNuPRr2h1_Jv1Zd22hH_eUar8KtGPT9q9DmZv4ZU0PHbItfE-LoOGFY2t3jc5d6lpgU1sxwmySw7IzC5rFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل چهارم پرسپولیس به استقلال خوزستان توسط شهرآبادی(90+3)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/104181" target="_blank">📅 21:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104180">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2b2857b1d.mp4?token=l3G3eiL395NxaKz7Doo846dkN30l5Aen-6YCDS7lv62RQWh0OuRGK3iNSaSDe3-t6GhLfjrqm3MsydRnYRSM_e6kkKoq__5YvF7OwJt3Cj7OYe0Ir0zczfNORAk7de7g_rr9jVUi2A3H9NJjSmpyLT3RvnWUGdYxStCZVV4kEBpS6IzYkSMn6En18bekcgDFrdyOhRczYWerzpY89yqJL0e3ik3vSUAyPYb4Ky54rGxhEC--JUCCMMiHrSH1mfxENawrIeDOTEwThpZMJ1_vwiL3T6vwaR7XdjtMMWZhBcfi-Oq1lb9edKRo5spataOhzt3SfgkyD5HBRqBpsoa19g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2b2857b1d.mp4?token=l3G3eiL395NxaKz7Doo846dkN30l5Aen-6YCDS7lv62RQWh0OuRGK3iNSaSDe3-t6GhLfjrqm3MsydRnYRSM_e6kkKoq__5YvF7OwJt3Cj7OYe0Ir0zczfNORAk7de7g_rr9jVUi2A3H9NJjSmpyLT3RvnWUGdYxStCZVV4kEBpS6IzYkSMn6En18bekcgDFrdyOhRczYWerzpY89yqJL0e3ik3vSUAyPYb4Ky54rGxhEC--JUCCMMiHrSH1mfxENawrIeDOTEwThpZMJ1_vwiL3T6vwaR7XdjtMMWZhBcfi-Oq1lb9edKRo5spataOhzt3SfgkyD5HBRqBpsoa19g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇷
گل‌زیبای ملوان مقابل ذوب‌آهن دقیقه ۸۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/104180" target="_blank">📅 21:25 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104179">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM32g_RcFfGqNR-o4t3bBB5XSc1k4h9f8dHZEZEJjN9qbHWPEEJ532Gj3P1oeaJ3n1g9GsjIaLKk1UE2ilqBbytTFO3x7LY-tDjQF9at8Qx8zWOXms1i3r_17JbPVcjp05jNJOObIUhA59mc6ROmF48eZiGe0ihnJVW7ftKqBRZit8zkjOGcR72OBAvShvncOsyr8od0LQtd4bTdw00lZwIYkmKkhpwiO_hrn0W4_2PWiKe7BVXov959wG0LzyFQgjN7Dhjk-ZcfOu-t-bj4aS2cNKIZIBTUEqL_2yUF1ZzpvtImQH22txU1dDgmbuWUx8nllH2xj3y-EG9iR6PH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته‌اول لالیگا؛ ترکیب اتلتیکومادرید مقابل مالاگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104179" target="_blank">📅 21:21 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104178">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543b2ef6fe.mp4?token=VNnZyxTR2Xh-0t07B0OVEhlpwlMvN45l1foKS6IiY6Rcz0JG567Q6fBSvhrTT3SBBQrv_jES0mqXEpuV8jIM6U-D8SxZJBnJYzmTkAsaluPYiMn5TxXJrqbZ0qcnhRiWJ6LJgS2ojO-fHRMq4s93cqAe2cNEQO_X5ujjgRSySCyo8lrSVilnktudiLu6umzAsjJF60JJs9h5aB5M5TpJ9zQu6CcfxfthEx4Qh8rhv7SpO-e3ihY6O54s2RD9Ep57lAs5maOIwFMSH0ZjeC0dmrjM8sQhK64LoY6RcKw1kr-ols0-gZy-84DC209kgIQb6n1OukTo_iuyMX2V0fxxsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543b2ef6fe.mp4?token=VNnZyxTR2Xh-0t07B0OVEhlpwlMvN45l1foKS6IiY6Rcz0JG567Q6fBSvhrTT3SBBQrv_jES0mqXEpuV8jIM6U-D8SxZJBnJYzmTkAsaluPYiMn5TxXJrqbZ0qcnhRiWJ6LJgS2ojO-fHRMq4s93cqAe2cNEQO_X5ujjgRSySCyo8lrSVilnktudiLu6umzAsjJF60JJs9h5aB5M5TpJ9zQu6CcfxfthEx4Qh8rhv7SpO-e3ihY6O54s2RD9Ep57lAs5maOIwFMSH0ZjeC0dmrjM8sQhK64LoY6RcKw1kr-ols0-gZy-84DC209kgIQb6n1OukTo_iuyMX2V0fxxsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔥
🔥
🔥
🔥
سوپرگل پشم‌ریزون زبیر نیک‌نفس در بازی امشب مس‌شهربابک؛ یه لحظه روح مسی درون نیک‌نفس ظهور کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104178" target="_blank">📅 21:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104177">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58ba1302f.mp4?token=b4pOzz8ynxhSb7MMrVuyqLYgDnCE1Ps-niFCPE_v-rHk61l-5MvGjM8JksoPnqgsbjEuXHAcBuIJonZHJIH6LIC_emp8KeVa9IXEcWKeAt4zjAt-M_C5wPVA-GT_rIyao1LayA5EVFy0_96C5SIMNFfGvrj96e-Wm5lHBDAP4EsRdv4mA-ScGcpoxC-yJwm1HTLZO2ajW2RcXsZGaoRPcfMG-SLrUc4fGNFCHAic_otYYNhuesxB02IYpH9AH5vrJXa5FUcbQkQ1KL4pnFPPB8MMu3yTkMpYKLZ9gSEooZmB4l24TiZynlUjq6cB2klS0Og58Csy46yHwJUTz8aIdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58ba1302f.mp4?token=b4pOzz8ynxhSb7MMrVuyqLYgDnCE1Ps-niFCPE_v-rHk61l-5MvGjM8JksoPnqgsbjEuXHAcBuIJonZHJIH6LIC_emp8KeVa9IXEcWKeAt4zjAt-M_C5wPVA-GT_rIyao1LayA5EVFy0_96C5SIMNFfGvrj96e-Wm5lHBDAP4EsRdv4mA-ScGcpoxC-yJwm1HTLZO2ajW2RcXsZGaoRPcfMG-SLrUc4fGNFCHAic_otYYNhuesxB02IYpH9AH5vrJXa5FUcbQkQ1KL4pnFPPB8MMu3yTkMpYKLZ9gSEooZmB4l24TiZynlUjq6cB2klS0Og58Csy46yHwJUTz8aIdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول استقلال خوزستان به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104177" target="_blank">📅 20:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104176">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyQnL1gAoFFZWl64I7hqNSGhnQm2zlTLbNUY9oNh5-uEu4an_WLbO8SNmNukPkpJRx2AfPRxVBBM0ANQn6wMrQPoCE0uLbwon8v9LZKfZNt6LA57OFOXYGPQeUj_99hO79yBUUFjWzq8TMiT641LsrCS7NSy7JkVnOGfv2wcJdjKOon3ZOuBCm5Ad7JM7BgAmo0ORgNthQn40BhlKwbiV3631BFYkEJXcB1v4UNK-kDBvAJ5HKbwccGLHPCgnrHhc9cUvvRPR9MYHB8S1dGukw7wO0beQGrxPRawskqkyUraFNIf1jPJAuYA1_yhzW9udpbUNfZZsP409IO0SyZzcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استایل ساده‌زیست بالنسیاگا رامین‌رضاییان در ورزشگاه فولاد آره‌نا پیش از بازی فولاد
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104176" target="_blank">📅 20:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104175">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔥
🇪🇸
انفجار نیوکمپ پس از اعلام نام رودری و ورود این بازیکن به زمین چمن ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104175" target="_blank">📅 20:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104174">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke52-tctE6wsCsNLLH6YUybj5jY2RvGLymEIdwzrpXEKrfLRlSRVIRywrNrrh4BlIZ-bUr8aJIxOxcvsR4rRQ4sZWBvRxL9G9kHAcK7T7J_i0MNPpLUesZ35Wnbdirj-qBJzacGSPvqvxF08Ab1FON6JKTxENy2ONeye8rYXIXdJhgDhFHP1traTfoaS7k9Lovwp1LvgxJFcC9Ik-B4lNHyN-rW6I_zVrlT_WbCcl8tSG2lXXhzQY22w4wp-cZMFMSLw0VPqBwcIkfkgIxVu99DsSeYDzAilCaID0anOXVwWzjXRItV9ABW3M7_6iF4bR0Hht1QQWa6XaaRWk0aDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
😳
🚨
🚨
🚨
تفاوت آلوارز تو عکس‌های رسمی فصل های قبلی و این فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104174" target="_blank">📅 20:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104173">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41445f46c8.mp4?token=B5MP53x-cMKHnjTy83J6XsLLrDj3JsxegveSawwjpvHtbMerwd2C3HqZ5hJOtJs5-9M7tRDy72myME_h6CpSxZuSdQTfXCSKc2uK_hP_vGP0JQ5lx7J7fAOwv09VIN9k_grSlcccgELyz_SEfns_zw3IDoUgyo9yU0qPj236YjjVaKvldoVhGV4Y-TzpvOsqw4PdaFRCMzda4NvPGjwMVwE47a7fQ8qFGbaYKFFOAjHf8JyBbX_VbzOKKmoBIE2OnkFPCj41XpvQ8AWutTM-mcOCoSpyc2akK9e2IXyB3enNqfiap0jijqQ8A-vqvpJ67gl8xW65683fLUNwu2EV1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41445f46c8.mp4?token=B5MP53x-cMKHnjTy83J6XsLLrDj3JsxegveSawwjpvHtbMerwd2C3HqZ5hJOtJs5-9M7tRDy72myME_h6CpSxZuSdQTfXCSKc2uK_hP_vGP0JQ5lx7J7fAOwv09VIN9k_grSlcccgELyz_SEfns_zw3IDoUgyo9yU0qPj236YjjVaKvldoVhGV4Y-TzpvOsqw4PdaFRCMzda4NvPGjwMVwE47a7fQ8qFGbaYKFFOAjHf8JyBbX_VbzOKKmoBIE2OnkFPCj41XpvQ8AWutTM-mcOCoSpyc2akK9e2IXyB3enNqfiap0jijqQ8A-vqvpJ67gl8xW65683fLUNwu2EV1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
سیاوش یزدانی، مدافع پیشین گل‌گهر سیرجان به الطلبه عراق پیوست و‌ شاگرد علیرضا منصوریان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104173" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104172">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d92806f40.mp4?token=oa4ejVC18od8AT6RMqMNkTUsoDcg8YoefCS39TZedFLW7rNYhYB7wrWkWlo3s6gICMavQWZ_F7-6oSbOAuFrUzTQBlMFEAuQTF2MczcUwK5VV1yM07i8W3PQRVky4nr5x5C9V03OU1D9AdauT_e5TEh2yzoTvpsdvfBIP3nNn1x2o_Qjs_UCjOmpKfYmnmvekz3Y31fjllGtpO9zo8n1EYU56AjXw2Y6ATuYnJSuxX5zg7Ta3myOF3NmCznZVcy2_2YUzwpoAvJKkUx2HlxLbkSg_oZttcKwFX8GRO65DMAROw7dkP5K9Tg3Rh5QxmXUXjseQ9wbKa_Nk60_2KHgJABtjWx-Vs4Wect-nYDQF_VGShgz_Ub3E0bTjyCGjRnoy356pF5QdxFOfGfvOvQJCJ06GDxp-S1Os0lALOKautqFsK3LvLQKVDbeDVLnanNpm3rmVMdGamzMKyTBSOWjuk6q7R97jS44tY7vr5xffJ8StWXgxXgj_pOIr_MffB8Rqx4WZk9bpFobs0oaYj67oMvupW_Gw-rEZ7cRmmqyuUCnWV_vWv5cdwLgfWavUaZt31nrxt8YsVRwZB3QeDjGZ2-nq6oC0MTwcGIHwpXogvEteEo-6WUB1BlmbO7BRFKjfeKzOEVY7PznXyDoscMgaVIn04olOESO_73bLjg1ROU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d92806f40.mp4?token=oa4ejVC18od8AT6RMqMNkTUsoDcg8YoefCS39TZedFLW7rNYhYB7wrWkWlo3s6gICMavQWZ_F7-6oSbOAuFrUzTQBlMFEAuQTF2MczcUwK5VV1yM07i8W3PQRVky4nr5x5C9V03OU1D9AdauT_e5TEh2yzoTvpsdvfBIP3nNn1x2o_Qjs_UCjOmpKfYmnmvekz3Y31fjllGtpO9zo8n1EYU56AjXw2Y6ATuYnJSuxX5zg7Ta3myOF3NmCznZVcy2_2YUzwpoAvJKkUx2HlxLbkSg_oZttcKwFX8GRO65DMAROw7dkP5K9Tg3Rh5QxmXUXjseQ9wbKa_Nk60_2KHgJABtjWx-Vs4Wect-nYDQF_VGShgz_Ub3E0bTjyCGjRnoy356pF5QdxFOfGfvOvQJCJ06GDxp-S1Os0lALOKautqFsK3LvLQKVDbeDVLnanNpm3rmVMdGamzMKyTBSOWjuk6q7R97jS44tY7vr5xffJ8StWXgxXgj_pOIr_MffB8Rqx4WZk9bpFobs0oaYj67oMvupW_Gw-rEZ7cRmmqyuUCnWV_vWv5cdwLgfWavUaZt31nrxt8YsVRwZB3QeDjGZ2-nq6oC0MTwcGIHwpXogvEteEo-6WUB1BlmbO7BRFKjfeKzOEVY7PznXyDoscMgaVIn04olOESO_73bLjg1ROU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل سوم پرسپولیس توسط ایگور سرگیف در دقیقه (48)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104172" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104171">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhvmDlABuIzjD6bLmfMTLTCDaMwA67xVAJ9rngCruRhVF-rMreF9i7meY_0Dp2_ZVXR21LtJezhaYkx1fLi8FtyJpwvG4bz29No6jqOTyNrX2ervcJd_8Ozf6p_AvK3NWmoMujHZEfeRVC2MSfqH1MeYWy9opJgro_ryUArdDDq8QMhoVHSN-zqMKxowwe--akzbutqX7al1N1O5iIg2T7RimW8AvXrj1LUZR-WA3_4Xz4lA0QzWqiGsZT3E26kuMRyV5VtqIvVn2dCQOAi7vgv_XN-v-xCEEh3m_3k5i429DO1QLyz4LEr9ODPlbjrbv6CCfHEi75wofpasaAkk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمق خط هافبک بارسا
💀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104171" target="_blank">📅 20:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104169">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2bcc49ca.mp4?token=W4VH4cWrQp8D4XmAxBvx2KW8AHpcAJJW_nDd92gNTZC9Y13-B2rroz1T2YBN8i0Dc5dPzECxm2-GPDIc6H607qHvWMRveoq_66I467_gPDIESxHfj2ub5kQwVEhd1aYqdHSE0n6GduH9DLNCA_ZhG0tYBJKqujGLrHJgny9SjjQyn-ou9MPLPG-j305JPuLp_-vMmBWosV2MBD9X30vyVrItXVqkwiymiS30R_cS3ClmpWed_5NZSSoyz6sXPMLB0TwnMca74UXKpFoQhxQPxYC8IIY2kts4Wji-iRXvlVubFqAko4f_kfxCC6EohUz3uDbJACOYDCCVa0sJ7FmVXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2bcc49ca.mp4?token=W4VH4cWrQp8D4XmAxBvx2KW8AHpcAJJW_nDd92gNTZC9Y13-B2rroz1T2YBN8i0Dc5dPzECxm2-GPDIc6H607qHvWMRveoq_66I467_gPDIESxHfj2ub5kQwVEhd1aYqdHSE0n6GduH9DLNCA_ZhG0tYBJKqujGLrHJgny9SjjQyn-ou9MPLPG-j305JPuLp_-vMmBWosV2MBD9X30vyVrItXVqkwiymiS30R_cS3ClmpWed_5NZSSoyz6sXPMLB0TwnMca74UXKpFoQhxQPxYC8IIY2kts4Wji-iRXvlVubFqAko4f_kfxCC6EohUz3uDbJACOYDCCVa0sJ7FmVXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
🤕
ابوالفضل جلالی در دقیقه 26 مصدوم شد و از زمین بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104169" target="_blank">📅 19:59 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104168">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTRYvkEmYUGMi_anEBfrzb_20Z4fbjfh_XEAJ6CIid-XwJqo-DOqAP7-VHeVk4Dyx1mDcVqlx5QkvKY2nK3NCHmgH4Z235dhcvySjzYA1TZSKYfTi_I7ptzvTIk_apaoVn43Ce95GVQm6Ppo-r8sthf3rt2VeOv576JSgeGYvnD-FVff4yjUhUEGy5MNH6B50KN-_OOlqpoXdWPabSP0hPJ4Jz80HZ3GQKNlyoiuAqFBoaZH9FzmAcDz2DxyFCh9gJ85vxMG51ncMGFzvd5SNiYOslhxyov6wzb7YSBTJ1MiXykwpMZMmrvnuGnZlQGZwN9PRoDDbWLcSNCpFNoMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
ترکیب رسمی بارسا مقابل الاهلی؛ ساعت ۲۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104168" target="_blank">📅 19:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104167">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73b9b3bf6.mp4?token=iWYg6XheSg8wZVs6or--CSHJLyTBhVdS8lRMzLffX_JMCVBLApVePmFTXq-qw0I_YnDmTGFBxys6TWov6i_Rf-xhMMid74vRuJ-0prA5PbH35YzzAy-fPBTVzdVeMzPK-_OhNawuy-ONTuQAgv0xWSTYF60ntCmt6SpLJq4r-trLrdhIKim1uDp0w5Lylny0riCISfTUiRDxRZ6PjhLzHOzdqlahJLhEYnqFQyxxHV0q7ENTBAtbwsBxF7Pf9SBY46iXOnJQpCMMZn3k1i324Z69U2YlJe6qpXnwdSfeGjSmRXylWIwjakIcbX0qp2TbnBtVyu6HMXNGstep1WBb-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73b9b3bf6.mp4?token=iWYg6XheSg8wZVs6or--CSHJLyTBhVdS8lRMzLffX_JMCVBLApVePmFTXq-qw0I_YnDmTGFBxys6TWov6i_Rf-xhMMid74vRuJ-0prA5PbH35YzzAy-fPBTVzdVeMzPK-_OhNawuy-ONTuQAgv0xWSTYF60ntCmt6SpLJq4r-trLrdhIKim1uDp0w5Lylny0riCISfTUiRDxRZ6PjhLzHOzdqlahJLhEYnqFQyxxHV0q7ENTBAtbwsBxF7Pf9SBY46iXOnJQpCMMZn3k1i324Z69U2YlJe6qpXnwdSfeGjSmRXylWIwjakIcbX0qp2TbnBtVyu6HMXNGstep1WBb-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇮🇷
گل دوم پرسپولیس به استقلال خوزستان توسط علی علیپور 20
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104167" target="_blank">📅 19:52 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW_X4i_p-fmVSB-us77g2S-pozTcuboYlSlnW6Dv9OwPxe3o_yKbN6MUkWE5twy_2NGqFCMadSlYq_AElP-eWDpS1HN17ISbj2_qT-debDdB1AGTHOgUDg1ZWu4cY-M7qEuDebEvVcRb22m4CXYuT66c3LHwh2KgRi8KTd2cxBfuPqi-lxmX5DjInD9Yz2Qo0YZAyJRAvvMBlwRV2jCNfe0NdFTQi629cv65rJVDpzH6_ti7JbAJUnJYh57mLnr1W2C4Z0BgW2RJETvaW9w75kW89lK6VejMeD3wAZqIK9k4s2bgoltC1HcwEYtnfB4IbGCyaV938GDx6hA24K8A3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
جرارد رومرو:
لائوتارو گزینه ای که بارسا انتخاب کرده و تا پایان نقل انتقالات برای جذبش تلاش میکنه
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104166" target="_blank">📅 19:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6842cf509a.mp4?token=QyiyRVmf2VjCsLhi_8eP7ZDuAGoZwMXaeMqQeTlyBCHRf4P7_YqobiQ9wBZOoCekH8e504bWN4N57LrU3XmdPcudmtG1MyA59rJ3RsUXbpykyp6qHv9Aa8giFtktm6F8apF10p2rLFUVb8IDqomyEgoqICcWEVm0CpXl2V_dxaqoeoDU2GO97QKpfPzUUD5R9IBuBnGOGPTwUy1WglFrOPaHtBSsr8-JejTuM5Y8TzwQCp23xefYLX1vgWDb-BQoDs62btwwTec3oFpdp5yvlxlOcRY6HP0no7DKnZmzghQd52ygEo6JqsRTg0aCIFzGdiBA_Mpu7sMpzcFc-qozTQNG4RaZVSKHpCflkcXB2b6jHHGsYC5Dq5awxE35Wxogp-sews5aDPLzEEoxx9uXQz4zKX7TrBJo5i_eLwfY7ANcarh7wzOeTH7_9rAeLsxtVtMdAHNey_hwBkhg6Hv5PvGeV1zJh3rwBu505d5sPQ2PpifrIVDrWX1I4_OcadW_b2X_GDP2Z5pzih_wVTQwaV0ctGNsBxJn--8CAVRJ1wK4kgClKD161wqYV8mSYWd1srzgo0qd1Mft3mtLiTU-bOsSao6KH_xTe6ylDGOls7POdyZjtVWsLHCVBbtrVkxnggnZuzxjrnjUol2zjofKmVTHBTp3GvfX0I0S8Kv_Fx8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6842cf509a.mp4?token=QyiyRVmf2VjCsLhi_8eP7ZDuAGoZwMXaeMqQeTlyBCHRf4P7_YqobiQ9wBZOoCekH8e504bWN4N57LrU3XmdPcudmtG1MyA59rJ3RsUXbpykyp6qHv9Aa8giFtktm6F8apF10p2rLFUVb8IDqomyEgoqICcWEVm0CpXl2V_dxaqoeoDU2GO97QKpfPzUUD5R9IBuBnGOGPTwUy1WglFrOPaHtBSsr8-JejTuM5Y8TzwQCp23xefYLX1vgWDb-BQoDs62btwwTec3oFpdp5yvlxlOcRY6HP0no7DKnZmzghQd52ygEo6JqsRTg0aCIFzGdiBA_Mpu7sMpzcFc-qozTQNG4RaZVSKHpCflkcXB2b6jHHGsYC5Dq5awxE35Wxogp-sews5aDPLzEEoxx9uXQz4zKX7TrBJo5i_eLwfY7ANcarh7wzOeTH7_9rAeLsxtVtMdAHNey_hwBkhg6Hv5PvGeV1zJh3rwBu505d5sPQ2PpifrIVDrWX1I4_OcadW_b2X_GDP2Z5pzih_wVTQwaV0ctGNsBxJn--8CAVRJ1wK4kgClKD161wqYV8mSYWd1srzgo0qd1Mft3mtLiTU-bOsSao6KH_xTe6ylDGOls7POdyZjtVWsLHCVBbtrVkxnggnZuzxjrnjUol2zjofKmVTHBTp3GvfX0I0S8Kv_Fx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس توسط خدابنده‌لو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104165" target="_blank">📅 19:38 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
رومانو خبر جدیدی راجب آلوارز نذاشته و اخبار منتشر شده دقایق اخیر فیکه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/104164" target="_blank">📅 19:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104161">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e03b3c710.mp4?token=rgiwp6a2lFihHccmf9Jv45giBLNUvXH88pzG0d2e9PvR1N8xXT7swn6w4SKIrXGERKeK7v4DZrCxIF5P8MrF0c33U9pGrNVfSI0sXdWRwDHORsVcD5hPylle71HBJi7kzqa-xSWLRQbBXyu3sRdy8OLy4u_u_k77We6yLJcWiXg3c6vhpmbvr59EQd-NtQKumFI3Hn9WsyC1KeyFXBlVrPO102eWPfuhbZ3fmvskYVSEdhzHnxQ9SAMvLpS87rTIGby8DYIX1KAxcMouOAhDjHQ3f1tXa9WgWTawjyVJwbYlQUdMmTiDZ93ISVXmHUsVUAWSTfRgTPLgSUxyofydRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e03b3c710.mp4?token=rgiwp6a2lFihHccmf9Jv45giBLNUvXH88pzG0d2e9PvR1N8xXT7swn6w4SKIrXGERKeK7v4DZrCxIF5P8MrF0c33U9pGrNVfSI0sXdWRwDHORsVcD5hPylle71HBJi7kzqa-xSWLRQbBXyu3sRdy8OLy4u_u_k77We6yLJcWiXg3c6vhpmbvr59EQd-NtQKumFI3Hn9WsyC1KeyFXBlVrPO102eWPfuhbZ3fmvskYVSEdhzHnxQ9SAMvLpS87rTIGby8DYIX1KAxcMouOAhDjHQ3f1tXa9WgWTawjyVJwbYlQUdMmTiDZ93ISVXmHUsVUAWSTfRgTPLgSUxyofydRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
تیجانی ریندرز، هافبک 28 ساله منچستر سیتی با قراردادی به ارزش 61 میلیون یورو به القادسیه عربستان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104161" target="_blank">📅 18:54 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104160">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLaNJfbRx8HPvtwt5WEM5BLT3Ze7jlBJ_9KehyoR0MS6dFLqta9CgnXD9LUJka-s4FeGwa5n7yJH_tm3Wjb_1e7M5AdNyKx9MGhSMXYL4imGPO6Cnc-EO9op08nJwp0r4WAZkeCes4iKu1GTDI5fn68gpwOWSHex47roiLErZLV3JvAZ_dEw9Qx62Q4-sG6vQ4BQEOqDm762dChXagbL6fV2IkdVODTv8zIlNj0q_GTZNK8SvQUu0mxV6EgWEdqOOZ4bAd7QYFuRSOLJde0NcSwVxaQgFGPVcVIlS-ngih7vaOgC1E-S7FdqR87fki0DUJN_3U18jW9yjj-RzZK6uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
✅
شماتیک ترکیب امروز پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104160" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104159">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL_W-WOftvnGH3sSaeCPb8zHg4TESgLCPO9b5XsssWWbSN_WVMGuH5AY_ei_df2ALrgvg8ie-M9RyPxL07BYFY9Vo2mItb_kEXq0TYx_TSmfjGmxXDEzRIxoX0J2YXlue6siDKwFGGWDeUIVti4vcQej7B4XwbKbEkzPAoZ_CNOOZlMQKvsGftYI--aTaHkPaJy7RAldGFhk836IdNjU_iR0-NnfSoZCaO5il9oe5xcXTOmk4uOjGClx-PJSeM9Q7ArYlOvWCrTWOu7lS6sFPfn5M1ELOgotbMpc53D4fW3midMJz-cEIuVjhiPxJXBH0SDadXrHBVKyxM3ebms5Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
🇮🇷
🇮🇷
لیست بازیکنان اصلی و ذخیره پرسپولیس و استقلال خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/104159" target="_blank">📅 18:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-104158">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d63f7a79.mp4?token=bB0VcbpCfea5hoDhk9LUYT260NYlMlfJUmaA6YWRwFlIXmn1xIj5QECD1R8wkjfeZBDNSYKy6C_fewiJmg2QH6PewpTj-46s0-OHhpDyPZyG4M8C17UlOI6_bUShEpV3H6cNl_-L317iCtUuA5Pboxi9f1VL3x0o6NeiflfMLojUzeo0ej4I7sS6WzndGuaP2y-r4PVy5UA_pz0eiQDSIPm73otPQHLm4EfR2N72rUBVBiVcuYh24dE7LuVicZzZIJVlm-sxX793tSJZMaoYiwO_cVx3gNu_6kLOrWBJyIH3jLtECygaoCYg1qmFT7XZfHysDWSSCsOlztQ7emw79A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d63f7a79.mp4?token=bB0VcbpCfea5hoDhk9LUYT260NYlMlfJUmaA6YWRwFlIXmn1xIj5QECD1R8wkjfeZBDNSYKy6C_fewiJmg2QH6PewpTj-46s0-OHhpDyPZyG4M8C17UlOI6_bUShEpV3H6cNl_-L317iCtUuA5Pboxi9f1VL3x0o6NeiflfMLojUzeo0ej4I7sS6WzndGuaP2y-r4PVy5UA_pz0eiQDSIPm73otPQHLm4EfR2N72rUBVBiVcuYh24dE7LuVicZzZIJVlm-sxX793tSJZMaoYiwO_cVx3gNu_6kLOrWBJyIH3jLtECygaoCYg1qmFT7XZfHysDWSSCsOlztQ7emw79A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
🇮🇷
بانوی هوادار پرسپولیس: یاغی خوبی گیرمون اومد، استقلالیا قدر جلالی رو ندونستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104158" target="_blank">📅 18:26 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
