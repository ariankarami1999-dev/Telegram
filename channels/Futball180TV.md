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
<img src="https://cdn5.telesco.pe/file/Acj64csvQBsys5TPezw2zR-1z6Ym67dejw6csrfrtdSTkL7LbKVLqLJHbhB_d76-q3469NcD4dmozNsvAPcFuAQFsn7a4QR3MJ0AzSiN-QMms3scuE5hAliNPkV2YmObXk-x2cfK8XONgm2X7k4UxdezN7ChkXL8D81YTDMA1sVRcT3uBnzqhLLXrzTszt5EhJ5-vbQ5XTg7GLSP5sUAWrVIWBG1lXZH7yByewbtmWAdwRPnAFNq56eb-YOxNAWAWar2MRisVK1KhYpeKS9Biz0L0kvmmXKwj1m8gD2uUxbVX4nresCXBGerj29azs6Na55TBNu5J9FxYR4FtniLSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 386K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 09:34:16</div>
<hr>

<div class="tg-post" id="msg-108320">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=YPKho9fFhdZfzCW8fAvRnk4WLTrqJhIkXxXbdTCb-oiY8Nna0Oj2rR_-fMWaiF2XdGZloKWqrn6bYs3ZfKNy5dLJSEEM2rvZ0nf_SzUTXqCx6t1Bv3_6NJa-Iaufv-8zHnRk6AbxPTVJLIEo62CSBlNDzp_vIzeaH-01jEr0yoHU_E65eS73SSgM_qAxOuduy1f6zVyTTLvxXZxw1h_4d-5mAI85g5XbITFY_ReBeOaIH7yDsrA2p8luzg4aPw59WnLp08wUuRpbHv83bWT3EoI8w2V39qVuXL3oFLDzOReRDVAmo8jp9Ne8nH5KgrhuFTywNFbfpOoyztFeQBGwOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c33311a6d.mp4?token=YPKho9fFhdZfzCW8fAvRnk4WLTrqJhIkXxXbdTCb-oiY8Nna0Oj2rR_-fMWaiF2XdGZloKWqrn6bYs3ZfKNy5dLJSEEM2rvZ0nf_SzUTXqCx6t1Bv3_6NJa-Iaufv-8zHnRk6AbxPTVJLIEo62CSBlNDzp_vIzeaH-01jEr0yoHU_E65eS73SSgM_qAxOuduy1f6zVyTTLvxXZxw1h_4d-5mAI85g5XbITFY_ReBeOaIH7yDsrA2p8luzg4aPw59WnLp08wUuRpbHv83bWT3EoI8w2V39qVuXL3oFLDzOReRDVAmo8jp9Ne8nH5KgrhuFTywNFbfpOoyztFeQBGwOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
پاسخ زیبای سیمئونه به سوال درباره مقایسه مسی و مارادونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/Futball180TV/108320" target="_blank">📅 09:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108319">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=Rs0sseDYA45qpdC08u8A5RySqriBxRfpJTRO06RLC4IGJoYdZeLzw5ASi4tg4iRdYmnzBCUZTu1Iu60Ou8-AV8cc-63Sv5qNGWAm-dBHbYkWvNyQmzlbs1IMc7WU12SEOa6LhPQgg6FGOwi_5H81OL9fQWFAQjamKyp8HRRBxd9v6Cbf_zDV-I5sBTiDoSrMErnd7UARr_rFWPipo9anIiZdlkV2ca1oiSspDZWo_1CvT5S5wn-dEy8XxVhkxlsSTR_Jqo7c-75tMO6LLRkJ7aiazvvI62T3uiuRYx7QPjO44s9aewMSX1vF7dmk-6kXcYIXYA8KqiG9mjLGwhizqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0b43363d.mp4?token=Rs0sseDYA45qpdC08u8A5RySqriBxRfpJTRO06RLC4IGJoYdZeLzw5ASi4tg4iRdYmnzBCUZTu1Iu60Ou8-AV8cc-63Sv5qNGWAm-dBHbYkWvNyQmzlbs1IMc7WU12SEOa6LhPQgg6FGOwi_5H81OL9fQWFAQjamKyp8HRRBxd9v6Cbf_zDV-I5sBTiDoSrMErnd7UARr_rFWPipo9anIiZdlkV2ca1oiSspDZWo_1CvT5S5wn-dEy8XxVhkxlsSTR_Jqo7c-75tMO6LLRkJ7aiazvvI62T3uiuRYx7QPjO44s9aewMSX1vF7dmk-6kXcYIXYA8KqiG9mjLGwhizqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
گلشیفته فراهانی توی جدیدترین فیلمش از جان سینا اسطوره کشتی کج و قهرمان دوران بچگی خیلی‌هامون لب‌ گرفته و حسابی خبرساز شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/108319" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108318">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=NO2piQbqpptF86NVhHoWEfzsLOT9XSBjPZ7E9XgSamySS6Pj-K-MNRH-G1kETWZy4Dk9DkKl5WVnCAIov2JiUgOkahm8xLIMulc1zH0hArofi7_VimVPEPrHVk5bvdHFvg--l6bhCwj75CA-Ol4q_tNQQ39RbRgeSd2Cpses5qWjLQ2OmgKe4L9x-1xWxLCJCLMPLFkkbUGHvvaWHXdVrQHr7r0aazbtuBORkRXTFe6TOJAZUhBXiglsJj_TADGJ79yBrPNOxX-sdTxGA-LteyTHrLjV6K1v-Sp2dKd8QMkGMqrQJg0SHbpyBZSVI4_GZRT3B34qKHLC7stzEiATfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf40f375f6.mp4?token=NO2piQbqpptF86NVhHoWEfzsLOT9XSBjPZ7E9XgSamySS6Pj-K-MNRH-G1kETWZy4Dk9DkKl5WVnCAIov2JiUgOkahm8xLIMulc1zH0hArofi7_VimVPEPrHVk5bvdHFvg--l6bhCwj75CA-Ol4q_tNQQ39RbRgeSd2Cpses5qWjLQ2OmgKe4L9x-1xWxLCJCLMPLFkkbUGHvvaWHXdVrQHr7r0aazbtuBORkRXTFe6TOJAZUhBXiglsJj_TADGJ79yBrPNOxX-sdTxGA-LteyTHrLjV6K1v-Sp2dKd8QMkGMqrQJg0SHbpyBZSVI4_GZRT3B34qKHLC7stzEiATfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
وضعیت هوادارای بارسا در این روزها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/108318" target="_blank">📅 08:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108317">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/108317" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108316">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/Futball180TV/108316" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108315">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Efxg--wUSExz0XfNXuQaNv3V8MiigM4UZ2AJ18gRmXdiY7JWaZlx991AlZd-YNHYqHdRKq9vYfF8_Qnq-QoQoQEZY9LGFga_M7zPHoPX7_Gn6M6AT6qPzCo1rMxJyQZhcMmRrmvdeI6Fri4xtz5a2Vdwp6pMKbz0FhW45lrvK_XduuLjjRZEi7drVtiVKMJyUBd6NQu2bmfEnvVDsDkT3FBAIAEqlvi8Y77YCr7yQLtN39MKZY4fT3fuhIqY29nXUfSLpiOMN1-7ynJF5HWaJI0vFQJyXke4kvuFMyQquFG1UdDNirVmzk9AXjx3iKHxRCWkMvnyJagwq6l1t3184w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
وینیسیوس با انتشار این استوری نوشت: همیشه تمامی صحنه‌هایی که کارت زرد و قرمز دارد متعلق به وینیسیوس است‌. چه رسوایی بزرگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/108315" target="_blank">📅 01:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108314">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWsNektcDE9XdJMkA71G3duZc4bPq5fE6b0Pqq4b7n4SHLbCeYd1xCv0j0U9KgI73bOh1czp5vU8Hos4ASsuUNdQbslR9znjGatgupPI5k5lYzOh4v_E_mRoyWwqDFDKfCdpXimWKq5NWVPBNi6C-A6zW62g9LRWgzd7qrBi3dW8N-rF6umMZqqjEzL5a8jEUDI9wTvXOwVOCEJ_wxpQIG9MSsponNZWl9HrZ5Z9autiStBnOqfENFHkqkgmEYLIcbNkLALwWukcTXY3wFtwxwovjwRqjvqZ1J6DX_HWDgnlwO5f9h_VRDoQ7mICQUOpj_Tg0HF6GDQPub_ECe2Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🟥
#رسمییییییی؛ طبق گزارش داور بازی امشب رئال، وینیسیوس بدلیل پرخاشگری و رفتار غیرورزشی از زمین اخراج شده و دوبازی بعدی رئال‌مادرید مقابل سویا و بارسلونا محروم خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/108314" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108313">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSfaowJ1uZbJKPkrTZIodPtlxzFYr2hMVnOEhJooiPHaNSZ_Tb8aGsie-UJw2zuy0lO4zb97BQU3nGp41qo4iOrH97I344ul7RnZ_a6th8uU5KVgJDiud-g4v7bRheOZSbWClwMbGa9KE5hlK-F2HqiT2xgI7nCL_jN9oEswhc4lpPv40iHSayzNTEXEWStoxV4UkxA-FrDx91HtNQcmn0JFLGv8_LNA0xhg4If1TeVXCD_XlRQ2llqehN5P-8INOz70lPU1JpSshD41nRrebkDEPC2XxVBXDt2XwMGxE4LuPRRnQFa6cDIbHpkbicIb-Sz9FVoBWb_Jwo1_TaI7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
وینیسیوس بدلیل حرکت غیر ورزشی حداقل ۲ جلسه از میادین محرومه و الکلاسیکو رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/108313" target="_blank">📅 01:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcXMkAKL2Itu0IBHwFArH94DpjkhwS0NTlh2f476sLHfmJH4oyu4mvIkjqRPHWRqi9l0kTSkIG2l9eIC26jQGAafTgj5h796BWveNo4vHP8B9wVeqv2ZndQCGHA0KXypiu0MOvIx-TpN8LhbP93WKTkdmprY-rXH2YkqqQd6fzkFaZywi14WaAMGgTjRZU6vq7VhDQunCTXZjsy5gBpuEN7rDM6rcpLZilokl9l3iGI9u1iHot6sN7JiuYTWeMa25iJ_VaIz34DDcV_Mt6Kfi62Pf6rsIK-Va7o5iMefiFHG3ajl5pbmgHqpB9TndQE5d5DsxQqKOr_nYjeRRoM5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
🇪🇸
پست وینیسیوس در اینستاگرام
: من هنوز هم خوشحالم. می‌خواهم از هم‌تیمی‌هایم و هواداران رئال مادرید عذرخواهی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/108310" target="_blank">📅 01:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVangJ-6_3b3-wQ-mZnSn4y7EncnN3Ge61su4Dchc9xRda3ibXmrRaHxHs3mcgS7RDqNwMAGu-JmXYN3nI0gJjDc1TPr6AtTmX0zbQ8XoSgK3v1chbg-PiZPbNv_gKsZWvAr81UM5-1MEYZelk7hNkHtBkVzg1RYduhIdHsEzE5vaG6JzuNhlabHjaGfYPfO6AoAYGCz2RSWhDoxO3CtAHI-jYc-DX3gi4wHzd4X6Kt_oLus5ky2n_o_-RcgyxUVwqIxHU4jcZXlVTQIhiaguFU4o_zrM4V_vEHF-B4Y7qmnsUYJ0MmCsnWBgnZ8FvUesMD4bZvghCjR0b9qOa7zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو بدلیل حواشی مربوط به وینیسیوس و احتمال غیبت در ال‌کلاسیکو در نشست خبری بعد از بازی حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/108309" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH0MCfYU9jN6e-qf8WWE_4clrahu79_2ROjKayg98qTSEznerJCdTav6yA1ydbr2F4ry4jBUAcmGaWgUXt4IhV1_3POfywwJZ7dDCnQmr7o7drSyIu8QUVPB8AJ8-aJQx3dJDeMAuuFBCklFlxChXX32km4Gh6v90GaNiJ1QIDgzohr09QiS1Ir12DdB1kBPhwHjWM94QyO1o2vTbfg4Vb7bkmtKu8LEMJBwaQrBEkMQVNfrxlbfb7G3hPP1NMl10Eh2urjyUSxx71uo5ixd7pb6X4fpZsViRJszunL8rmgPVkOGd-qKdT7FwrcENM-JkYDJLO4VsnoUpWnEDSBhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری رودریگو بازیکن رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108308" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
پایان بازی با برتری رئال‌مادرید مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108307" target="_blank">📅 00:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108306" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108305" target="_blank">📅 00:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108304" target="_blank">📅 00:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN5u2iFdeYI8bTGJogWLquRpR1CPByQnNXYhVkxgfB-0s8OBQ78FpXlckasMzIXhGv-tiwHuHBiQn4x7xwWYl68nEcAkqv4CRMjgbJAB9aBWStKk3wnmV15Hh8BbHBzuPgYzZ6C0S0hCV9XbppiBYmLEDXxJr9tAfC11qntGsSGIcVhI5q5Qd_lHCLuIF406Ts61rcB8d3bx6M3A_qBCPp9tsPaJWvXwvaljpn1P3oC3Gs2v2jymTEQ3NQuSU2C5prs2ST9c6QS4VQcBzrSmp6KR5gQyDE4LVz8hai7luxxY_H1otzWtiBniWCz2nNaXpC9ydUwvBZAPuPWkogGB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108303" target="_blank">📅 00:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=LsnC_I3MnBeMejsw60bO6wP7Ij0X2SfcE_4aYjmCj5qHYxxgYWY9UMgAGaUvvVCUdorgnOhm6sqpYGxhpddshtKiCTgouI6HXRM0TeppymVgohLdJEwtShBWA38A3nzz-KzOPUGdlN9ckpjDfea8DvIpF2hBHLTRr1ioLA6YLX7wJ0HLPt_NlUeLKMZiXSWlcAPYyi6A6kqntpHmmCF6jHeG_eOcjQYUnEbJF55AqlYEyjrSDEL-0BVc3fm3Aasl6rVmEipAIoecf4mlsElJf3t_q6V05eO6LW7RrzE0MswkRV6jOg_-adcR2ccEkJS85KaijyhQkGKxRLbHwOWoCDi501SoaVOqMn5dtsYXAqRg0VfL565MLUMOlt3KiJliqfk8uxeeoswGzsFMixaoW1HMd5Xz9fLmFK9WBYc-NZ3w9SGu4kT7xgXd5jRNsC0yyZg9hJ4KRfE1Cqv0oEBGuV_xs9ErkkF6y3l29la343VlWuMwHm1yVo5Zc8p82LxTMuPRBK6XPDBka03lHYrP96aUX_TImZZ1vDsYGHK_fZKMP-o8fMiax-VIEvWt1W4lHGrGfYYAxUkIH3ODh90Nx7dkf_hmqbFCsvzcXc8SsXMRvEQi_ykukHOUSHc9bHudk816kjTOV9mXFt_7gnr_1DP8l-myGpePwF6Y8G1rNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba8666e1e.mp4?token=LsnC_I3MnBeMejsw60bO6wP7Ij0X2SfcE_4aYjmCj5qHYxxgYWY9UMgAGaUvvVCUdorgnOhm6sqpYGxhpddshtKiCTgouI6HXRM0TeppymVgohLdJEwtShBWA38A3nzz-KzOPUGdlN9ckpjDfea8DvIpF2hBHLTRr1ioLA6YLX7wJ0HLPt_NlUeLKMZiXSWlcAPYyi6A6kqntpHmmCF6jHeG_eOcjQYUnEbJF55AqlYEyjrSDEL-0BVc3fm3Aasl6rVmEipAIoecf4mlsElJf3t_q6V05eO6LW7RrzE0MswkRV6jOg_-adcR2ccEkJS85KaijyhQkGKxRLbHwOWoCDi501SoaVOqMn5dtsYXAqRg0VfL565MLUMOlt3KiJliqfk8uxeeoswGzsFMixaoW1HMd5Xz9fLmFK9WBYc-NZ3w9SGu4kT7xgXd5jRNsC0yyZg9hJ4KRfE1Cqv0oEBGuV_xs9ErkkF6y3l29la343VlWuMwHm1yVo5Zc8p82LxTMuPRBK6XPDBka03lHYrP96aUX_TImZZ1vDsYGHK_fZKMP-o8fMiax-VIEvWt1W4lHGrGfYYAxUkIH3ODh90Nx7dkf_hmqbFCsvzcXc8SsXMRvEQi_ykukHOUSHc9bHudk816kjTOV9mXFt_7gnr_1DP8l-myGpePwF6Y8G1rNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108302" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0RMZ5B1cU7j-hXkjZv4pAdct5w-mqGiWMAIXl2LdzlSFsYXfENyFXJP81auBARwvsq58iKymgMXlZNTiCiGq5h7d32AyekJ6Y-DT08VRO7IzdFugY0oVTfcxBq61P7bf-PfF3VkusQCR1ykSyv_qJAZUFyP01cOyq8kIp_HjmwfG_GvLxDMLne91Mr_gDC5Pb8xD5vErpU3nPdtox0KkNq74y8nFfx-x8O6ZXsNR42f-IOC9tn_x6Q7IFSfuUHFrxtxCKQpqHlZ5RdbQ3DGK_c6ZhK-VNH3-MhI9iBVsCeM4G54kOWPoq14WrkiOwOE6xl5qp0vnKs41L3M9rMHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممم بخاطر این صحنه اخراج شد
😐
😐
🚨</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108301" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0z_YetksIXqgtF91TSN23s_ZlA2KmeOwH5mF6edEDOA1IBxCsszHJe6ivFuCNhSDRe6daamuUrvahphHIriB6ytc52j2zbi-1gL6Aswl9NgjHjakE_VN0THA9st674pAGgYvnlpg2gdvxDE2sA9P4oz2-fx3AUJtxNrJMttOm0c3P7Ij4FidCtr6-0VHQd7sON64FhCrG-04VrfiS8FEcR7k-pTulnY87MaCWvtAc3J689ymXRHjgSzIKVaOhb4fJ4010hWtio8rbh6PnchHM4d9aBPAkATWOqYAuU-9HkUzRD-qHw7KqDhmtKBtmfoYSI5WxMNKawHpOJhf1bw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس اخراج شد
😐
😐
😐
😐
😐
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108300" target="_blank">📅 00:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108299" target="_blank">📅 00:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108298" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلگلگللگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108297" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=MLLrVRcEfUuouOzlRD2Yy5Qw1Rtbtxcgyr5yyhWdtd3YAzz4BbVV4ytzgVRf7zjcn5tGUWzVQ4dld5NunH0lsq1JXB-wme0nQIHQHN0onNrJKwTqVEdKbrIs8MX80uj7rBCaq48ZgnZsh20mKdLQ-ezyPY3w2x5awaito3qtOfR_RxvQRI1NwLBMNNMHXuHbZU1nqfuOEbfN_Z-7TuKGJoCBUFnLRS25QERW_9juktarraiVFJ0mJq5ZVJyZDrwFegbsWNRm0xK8QSW_lDytv0dmr5Z7oKDAMhkFbBGDEioZsPMi6DlqOuHA-5hJjoYcSzEZHUCKNKdpQkzRX5xVgYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c230ecca1.mp4?token=MLLrVRcEfUuouOzlRD2Yy5Qw1Rtbtxcgyr5yyhWdtd3YAzz4BbVV4ytzgVRf7zjcn5tGUWzVQ4dld5NunH0lsq1JXB-wme0nQIHQHN0onNrJKwTqVEdKbrIs8MX80uj7rBCaq48ZgnZsh20mKdLQ-ezyPY3w2x5awaito3qtOfR_RxvQRI1NwLBMNNMHXuHbZU1nqfuOEbfN_Z-7TuKGJoCBUFnLRS25QERW_9juktarraiVFJ0mJq5ZVJyZDrwFegbsWNRm0xK8QSW_lDytv0dmr5Z7oKDAMhkFbBGDEioZsPMi6DlqOuHA-5hJjoYcSzEZHUCKNKdpQkzRX5xVgYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
گل‌اول رئال‌مادرید به ویارئال توسط دیامونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108296" target="_blank">📅 23:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نیمه‌اول بازی رئال‌مادرید بدون گل تموم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108295" target="_blank">📅 23:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
واکنش علیرضا خمسه به ویدئوی «خلوت کنید آقای خمسه هستن»: من پول بادیگارد ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108294" target="_blank">📅 22:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برررریم سراغ بازی رئال‌مادرید و ویارئال</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108293" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108292">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA7F70h_vAuMll7kIjPNGG26PiAvrSZClNvf2aJDj9tTdtutEHyCHG4lVnbdrH9Em-2JomY3ua8HPAd3Hw9uq3u--fWI46musH_f3o9qyfm1si57IkNbqGmrLWBGUfmOIoW1xibPL1AqD8QGOuQIhaHCxZE9JdShtWdXL6zQXa6pUKgnV0V7ADPGwnqzb54KLO9o2KF-zh13lhx0qFf29-NnWFipkoipEZIuXjr6IUDwVE7iM-2SnDs4usZB1_SJDctTeroNzP4ToxhCoLLJD3CDEVHinSZTcCyAgQ4DDezbAByoQXGGvgT5vysbrR1cmROfPEaJzCuhsVcbsCApbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌هشتم لالیگا؛ برتری قاطع و آسان در خانه؛ بدون حضور رافینیا هم برنده شدند
🇪🇸
بارسلونا
3️⃣
-
0️⃣
ختافه
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108292" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108291">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zxl3XnwXuwRxib6kY45kTATYDu8SPSzSFdrPOQ8Cusyghj5QHqaKG1THfIE0vJRISCHOq1LSleIRR-W0686cHp02HAaxg4JvkF7IwYnzlC6-1wn5fc3GYiWh0K1sdMStKH93aPcOxpvMlekhFUqistLWYZu4xrAgQIQNn_oKIA-ZxZxiqKvuEwWvfADsCiqn8NzNJvyUHEP3KfUl9WPpI0INzaODJ7n-blHgeDjL8inQ4l02Su6aFLiTOdwWnEDNhD4_ThLO36v7fp2dROqzOUx47N_398oVKcWkCRNChBEmbQi_mioAwpXv3eMK-RDoIUYldhGbTgLmLZl5nvPctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
لیگ برتر انگلیس| منچستریونایتد از پس تاتنهامِ ١٠ نفره هم بر نیامد؛ مساوی که به درد هیچکدام از دو تیم نمی‌خورد
🔸
منچستریونایتد یک - تاتنهام یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108291" target="_blank">📅 21:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108290">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=Wvn0CpwJdRn7x3o0FKCkH9WCX6XwyKdt0eaFyB9iB-vQZnNYVxBJUQGKAoLrlAY0iOzX8O9UpQaMaDQoVT2YJdVNPjkewhDAHwDzcz4H95bOrek8LcLDCP3d_bYgiCaDHirVcb7Q5SlZmQYbh48zrmkk67hZTwlNyPyNLJlK2VAmJ0LOUIONqXjKD7xv7lycl6scNkKrHPpT4V56iIBxD6pKhL6rsCg8DmIo69eDoiK9IgtTcFgTyK4jVAFePVJWvtaRQXda9U-EP46iBOX8g5mCcY16acRISAVIyEyuaX0XKeqBVZU0e-DGrDNajf7UaZBUGig0lIQjT45Rw8_ZbSnAFJaaKsCn-H3oR7RYlIcS4feOS2grl9FrG7h-8X4i6wAhCw1ZLz0p41KAqZhYDfYNlSOA0e_v10LdnGsiMm1mnnviFyWGrvOcK2izyVQD4EO4t3F9wfB1WqKfJjopeYJFRKsbShOBOicLLqomXRztlUknFJHHGlt_fSIzAKp3sYtUEcXjYygPuYxAoJ9y87ctIcb30I4Hh-VSeFhPU4xujJHMft01D6cm_jWCZEfV9bVwXpnqtqDrI78Fmorynffwax-LzI0CpbrKVr1q2oNRSWJDLedcyKGQRLKMFwb0OZpVsStC1fMkRRRb7sCx3NqL1KLopt_zy8noRXQ0WnU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eee0ed7a62.mp4?token=Wvn0CpwJdRn7x3o0FKCkH9WCX6XwyKdt0eaFyB9iB-vQZnNYVxBJUQGKAoLrlAY0iOzX8O9UpQaMaDQoVT2YJdVNPjkewhDAHwDzcz4H95bOrek8LcLDCP3d_bYgiCaDHirVcb7Q5SlZmQYbh48zrmkk67hZTwlNyPyNLJlK2VAmJ0LOUIONqXjKD7xv7lycl6scNkKrHPpT4V56iIBxD6pKhL6rsCg8DmIo69eDoiK9IgtTcFgTyK4jVAFePVJWvtaRQXda9U-EP46iBOX8g5mCcY16acRISAVIyEyuaX0XKeqBVZU0e-DGrDNajf7UaZBUGig0lIQjT45Rw8_ZbSnAFJaaKsCn-H3oR7RYlIcS4feOS2grl9FrG7h-8X4i6wAhCw1ZLz0p41KAqZhYDfYNlSOA0e_v10LdnGsiMm1mnnviFyWGrvOcK2izyVQD4EO4t3F9wfB1WqKfJjopeYJFRKsbShOBOicLLqomXRztlUknFJHHGlt_fSIzAKp3sYtUEcXjYygPuYxAoJ9y87ctIcb30I4Hh-VSeFhPU4xujJHMft01D6cm_jWCZEfV9bVwXpnqtqDrI78Fmorynffwax-LzI0CpbrKVr1q2oNRSWJDLedcyKGQRLKMFwb0OZpVsStC1fMkRRRb7sCx3NqL1KLopt_zy8noRXQ0WnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به ختافه توسط کونده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108290" target="_blank">📅 21:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108289">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">کوندهههههه</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108289" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108288">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلگلگلگگلگلگلگ سوم بارسلونا</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108288" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108287">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dgss9-NYqjMYl1absTjh0r9zLIb4BRHPj2bk4NDgD7vn72cKwaXGxwY36Of7ixMxB7_TfeOvTK8cvRKecUkNw9N8jSFBPZn0QNVel8FlL3Q2GYZ65I9LUQTwGCQQ6EbE7JIznrVTbeUsW8iGOCJZvv21ABmVvjSjWAD5vIVkRDc7q7D3esjP9PnAZ9hgZapNIfRvMd__Zmtfgu3aAcaQRigfkLuu-4mzM5zwFStah9mMNs-lcaems3CMKtvmwpOOF4itAQht9AC1Nws82JbYnXjWsd-qIBfn7rUTdqj1azVBUUx96tYiM8dkwy3cll_g77zLOMwQClMfokjAx4Rlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل ویارئال؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108287" target="_blank">📅 21:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8kwp5HVRirLaxCNmDeRW9oS-s8B0pD4Y0EECCBarTh9VMoMK-GtsbXUJnT89W9JZ_89OEsTNn1x1jo2d1myCmq95oKC9NVAm5BThN5nv8hVj9OdAjS8dUk9OMXw74W6xBav416JBE11lQbUtQ72if44p6LM8x-db-4cEa1ZMPMYtqdH8rQJo0h_zY0nLeIa8t4kiV6s7ZBBw_wC2xsHMKi-jiagk-mGUcEwXvxrsB7C1K-DemSWKP7llq2uAXmHGjYqi7Whbf0Ne_U8qCQtu5LCbac2tsl6wq_dsc3QAcZNaWK6PJXR-8dmKWhG92RUB-VEGlTtgjFSt593tMg1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇵🇹
فدراسیون فوتبال پرتغال از بازگشت رونالدو به تیم‌ملی در فیفادی نوامبر خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108285" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHiRS-i7k_VOMCVADCHYk9YbIi0ehrFxonDr6HP80sZdQWyWBKXJUF-hH-_33KpnB4ikEbwh3fRLgvcrRMzN9brB2ack_eG_Rz2YrF7MEliXxbOP82Ok5qNLebqa3yPXmh28MIL0oKgAWibOU3nqzF8nWkr9P_ZQjXowc6azYRg613SJoeePcWx5MZrB-wrUdHS1dokznXb-zu-snb7qb-dqpKS2xySVusvGSGI6UmmMnMmfzY_n7aSXKXeeXX02RWl-A9auj1sbeztPgUyaE4l60tqDhWXF-9JxiDuTofGKBLhXQggKpcB_bcpMs1a_GXHs8GGzujgGpXIejr6SrUIs" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9c23307a24.mp4?token=MKXuwreS0uYSEWaBI8w5KJ4sv6RSr7IbRA2tMYA8cRClqyxmXUXehbYq7UdUYK2HbjFaKJh34UyFvIqntg4lwqf4CT4faTTxSsvWZYgQj0T0njkwmvda1cFHYqr2oH--Sv1eBIaLcdSYkwG0rfypevkZuwEs6bzR4HvSG3e5WoT9wyvCEAyhdk4pHlIJPESCHqTuTm6AbqKbVdqHoYOxO_ppgw6gQ3YjE5HgQBAWlr2zlhmCLTSSNjm7VePhrQFRugxM-CplN_8ZrvB6ZzVgKOTP73moXRzz1t83xzZPnnL9b5Pcy9OTcqHuX-LMwixsYuIHHqju0PTwxMdEIQGFHiRS-i7k_VOMCVADCHYk9YbIi0ehrFxonDr6HP80sZdQWyWBKXJUF-hH-_33KpnB4ikEbwh3fRLgvcrRMzN9brB2ack_eG_Rz2YrF7MEliXxbOP82Ok5qNLebqa3yPXmh28MIL0oKgAWibOU3nqzF8nWkr9P_ZQjXowc6azYRg613SJoeePcWx5MZrB-wrUdHS1dokznXb-zu-snb7qb-dqpKS2xySVusvGSGI6UmmMnMmfzY_n7aSXKXeeXX02RWl-A9auj1sbeztPgUyaE4l60tqDhWXF-9JxiDuTofGKBLhXQggKpcB_bcpMs1a_GXHs8GGzujgGpXIejr6SrUIs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بارسلونا به ختافه توسط گابریل ژسوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108284" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گابریل ژسووووووووووووس</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108283" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بارساااااا دومیووووو زدددددد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108282" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108281" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=ARWG6e6_DyQHogdvMWFnBRrLmTZ2C2JRLM8p83ZzLlZbVoAmmGERZx1RWvJnPmvASGc-mR24Lvrr8sjjebdUZX99b8UFdEalm1gYnmd4lTutblPGptS9hajNQ8F3NTcjrPMRK9NRYIry-NupXqyN15qn2N0UCb2_fHqagCt4Hs8MuHwV6T_f2gnmCxaYt6I3hlpsPdtLtqsFbqMPsAKEbVpK6CT6d-dy1x8Rr_hVF-t_n8a7UAo7o0bVQp2xQb8tonBPl3Zv0gCQjk6-ojsw_yGUo2H1NWChjDQHZDAot4dLBeJaRW1LNn9Y-NzSiprU7uaY4o5IahQAG7c4GGHy0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=ARWG6e6_DyQHogdvMWFnBRrLmTZ2C2JRLM8p83ZzLlZbVoAmmGERZx1RWvJnPmvASGc-mR24Lvrr8sjjebdUZX99b8UFdEalm1gYnmd4lTutblPGptS9hajNQ8F3NTcjrPMRK9NRYIry-NupXqyN15qn2N0UCb2_fHqagCt4Hs8MuHwV6T_f2gnmCxaYt6I3hlpsPdtLtqsFbqMPsAKEbVpK6CT6d-dy1x8Rr_hVF-t_n8a7UAo7o0bVQp2xQb8tonBPl3Zv0gCQjk6-ojsw_yGUo2H1NWChjDQHZDAot4dLBeJaRW1LNn9Y-NzSiprU7uaY4o5IahQAG7c4GGHy0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
حجت احمدی: سیلی نبود، آقا ساکت بهم خسته نباشید گفت؛ پیشنهاد استقلال؟ خبری ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108280" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=OnQBDeyrLoBR-03dVDwfJiGFjtp8IJW7FnEjrE40Ywt2KnwOBE_l8Sk6iAwYenzHgo-e8HwfjvQRKdI7fzO2OrhHzxbrRlv-UY3r8qjugnIvZ92TMMyzjB4MoqYRlux3EUr8mCNIY-yYnb6KbMMO39swMW2ziJ47f2RI5gkc5D-LE_eEKp6G-EKvnPuj1neaWN76PtRdxNNybA9FFSjomP8bHlhAB6-y7mYLjUwdJ5FSKkHU3tPVkFvWkZ-Dxr9v9ss68_ZTKYak0YJLo7xc0oxOFwTTHZIKayJsfSg6Z8IWx3FI4z3SJO1aS74WZAE4e7hbQV4sDBltdoQHhBx7qz-LHhiQTdlyy-6kIyYYoHHf56uvSi13wZH4Ag8ksOIjY-ozqUUMY5AFaajTxYWv9FqGtaTWQ-6JNJvXgFURUiK2xsvuqJYvwJgb8p5fR4mWTuY5wR-KBUVf9o6GGHVIjUrNoA3KC3FkYGWDO1KTWlglrQElSNAMTIkZt9wC9dXSimHFLHWHSsBMQ0LrOLxJl3ZH2jhNtp7ivgdYLrRP29b86C2AMwAr271e9QJbLVOcV8LLD1yOc-LpU7L8uTzfnrcPWRs99RCO4k4Q3sOhB3rkxbLmz_CJNGxd7-kYz7QVtFUiP05brPglPAFi2ej99XXdOFY_zlwOsK-W2zTdNG4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/faa2aa1c08.mp4?token=OnQBDeyrLoBR-03dVDwfJiGFjtp8IJW7FnEjrE40Ywt2KnwOBE_l8Sk6iAwYenzHgo-e8HwfjvQRKdI7fzO2OrhHzxbrRlv-UY3r8qjugnIvZ92TMMyzjB4MoqYRlux3EUr8mCNIY-yYnb6KbMMO39swMW2ziJ47f2RI5gkc5D-LE_eEKp6G-EKvnPuj1neaWN76PtRdxNNybA9FFSjomP8bHlhAB6-y7mYLjUwdJ5FSKkHU3tPVkFvWkZ-Dxr9v9ss68_ZTKYak0YJLo7xc0oxOFwTTHZIKayJsfSg6Z8IWx3FI4z3SJO1aS74WZAE4e7hbQV4sDBltdoQHhBx7qz-LHhiQTdlyy-6kIyYYoHHf56uvSi13wZH4Ag8ksOIjY-ozqUUMY5AFaajTxYWv9FqGtaTWQ-6JNJvXgFURUiK2xsvuqJYvwJgb8p5fR4mWTuY5wR-KBUVf9o6GGHVIjUrNoA3KC3FkYGWDO1KTWlglrQElSNAMTIkZt9wC9dXSimHFLHWHSsBMQ0LrOLxJl3ZH2jhNtp7ivgdYLrRP29b86C2AMwAr271e9QJbLVOcV8LLD1yOc-LpU7L8uTzfnrcPWRs99RCO4k4Q3sOhB3rkxbLmz_CJNGxd7-kYz7QVtFUiP05brPglPAFi2ej99XXdOFY_zlwOsK-W2zTdNG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به ختافه توسط آنتونی گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108279" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108278" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بارسلونا دقیقه ۲ گل زددددددد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108277" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108276">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108276" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108275">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/326220841f.mp4?token=sB007Ytu50fxEPWA024gh8bk_bn-eVoQYYKHSVcpZOOWyvjZDsg0sNEIcaQhqDexDCowxWPShrUP3jkp9c3FVYMQ1T6EX-3wbBCKCq9AI-E6D-DAXOZ_3ovMf4LY7Iyet1yJeyTWiS9Mt1K6rnpXH4nxOjlt2kSoLvW-sm4bY_2jzOwRWdKPIFZElIKuJkrOmkPZhYSqzhJj9lZW_0Eg3KyRInZIVOi98C4_sLXzl-U7QSKr7Yt56petGc015o1RIcsF7xjIbCVZgkUvm0q1abaLdZzM97eAXaYKZaoGuT4D87VhE8ipsXMjfWYGpfDI5reFOhx2dcYWBi8F0zS89UqrDYqB0Oz2FJ05gIcYkuLeP0eKoIqyoKydje__82V2Pz5TeBCFZCU-OUAxtRaxuRdMKoZK-udSnByB_ZHMcoF2JLdi5TOearOPfHKqsLFwW11TyyagQC3F5eKx16xDTwH2g3TCXH-nsG6Qf61-4bQ5h8Pkn2TEbjVLSJbNRMbWBShvsLjeYbVCJ-Vf9VIb30E1I0dtKUVAILOw-mRe-NtJr4SqSod8tgZBzTIfkcl10UF9R404vERgKnuDXIJoPwFQ6BMVSqQbbQhTbm9kz4WExa2ONx6A6XOToJ72S7wxX9JGTMDdMUba4I8KWSch2kBEmUqnnw87wsZFb1UlA6U" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/326220841f.mp4?token=sB007Ytu50fxEPWA024gh8bk_bn-eVoQYYKHSVcpZOOWyvjZDsg0sNEIcaQhqDexDCowxWPShrUP3jkp9c3FVYMQ1T6EX-3wbBCKCq9AI-E6D-DAXOZ_3ovMf4LY7Iyet1yJeyTWiS9Mt1K6rnpXH4nxOjlt2kSoLvW-sm4bY_2jzOwRWdKPIFZElIKuJkrOmkPZhYSqzhJj9lZW_0Eg3KyRInZIVOi98C4_sLXzl-U7QSKr7Yt56petGc015o1RIcsF7xjIbCVZgkUvm0q1abaLdZzM97eAXaYKZaoGuT4D87VhE8ipsXMjfWYGpfDI5reFOhx2dcYWBi8F0zS89UqrDYqB0Oz2FJ05gIcYkuLeP0eKoIqyoKydje__82V2Pz5TeBCFZCU-OUAxtRaxuRdMKoZK-udSnByB_ZHMcoF2JLdi5TOearOPfHKqsLFwW11TyyagQC3F5eKx16xDTwH2g3TCXH-nsG6Qf61-4bQ5h8Pkn2TEbjVLSJbNRMbWBShvsLjeYbVCJ-Vf9VIb30E1I0dtKUVAILOw-mRe-NtJr4SqSod8tgZBzTIfkcl10UF9R404vERgKnuDXIJoPwFQ6BMVSqQbbQhTbm9kz4WExa2ONx6A6XOToJ72S7wxX9JGTMDdMUba4I8KWSch2kBEmUqnnw87wsZFb1UlA6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇪🇸
اتلتیکومادرید با این گل دقایق پایانی کوتی رومرو مقابل آلاوس دو بر یک برنده شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108275" target="_blank">📅 19:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی چلسی پنج - یک بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108274" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=d2hU__Qp15r-G3kkGnEbUgRT-2PeyV8zx869D8CzhQC6cxkU-AB50afn-oaloLdHrywXlmpTG_kW_WKuzkXXFcT9tGMgY8VTUsSePuY4SmYr_gX7OXc1B1-GqaRuk0OIMf4L49whZyNYjXEiQ6BkNxN4oZupr-6qjVwY1UkrWUQvp4SazdIuscAeo40f7tU1Dsskcqlo5leOWxP-tDirwtAUqZ6ZwZ3Hc0778-J8JxfC680Y6wBhNR-_qR07Yn0b-J3FcIB3zcQjLw4MajNkAtKEvP9GNFfPTiTuzsvMA93-AssU9juP0gaf5mPCJl92slptKHGiZ1gZzQ29Yg1ZEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5d3b26d2.mp4?token=d2hU__Qp15r-G3kkGnEbUgRT-2PeyV8zx869D8CzhQC6cxkU-AB50afn-oaloLdHrywXlmpTG_kW_WKuzkXXFcT9tGMgY8VTUsSePuY4SmYr_gX7OXc1B1-GqaRuk0OIMf4L49whZyNYjXEiQ6BkNxN4oZupr-6qjVwY1UkrWUQvp4SazdIuscAeo40f7tU1Dsskcqlo5leOWxP-tDirwtAUqZ6ZwZ3Hc0778-J8JxfC680Y6wBhNR-_qR07Yn0b-J3FcIB3zcQjLw4MajNkAtKEvP9GNFfPTiTuzsvMA93-AssU9juP0gaf5mPCJl92slptKHGiZ1gZzQ29Yg1ZEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرگل دیدنی و کاشته هندرسون بازیکن چلسی مقابل بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108273" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=q8Lgom4swdbFP8DCLQLirwoqJmP03a0K8Dqmilzrd6jxImQozh9CbjHXPKzdCXBGZLRhL53M_uUOKrklaB4zTw9z9GprjFNBDB8IHFw_zimpnCtEEPLU8xINl-WPTaEdHIihg-ZPh0wDGOLmnCKzoPOcVHmefwb6gOcIK_6b6s2oGWvr9YYoeD_3LHFE49m4YOwphRbcN8n5VbVpupBUPUNoIwdIQHs7Dr33j-gZh9_ulR7dTzryHTrGTvYVRPHe18SnL8Z0Gg1J09xr6WXGoUhkudnhtCIqgvH9xOwa0OPu6WfXbIgRZdF4kRkFkWJmXcIT6i6s7ZHWifjYtgAIMK7kWdjjEx9rajHezGv1PyPTezOI3uuJ6i5LUc-KSXp3qkE27GKS93xIyJvvKSD0tq7p9fz-nVIydyLZ1w0ny3NYpyVtrpO-KtIruXDJBfhhFM57hCfKnykQFGI_qKLmHu_oeIKRwgU8TCzRSbq3x7n-kct_HOHvWHG2S8gSzjO_EZJ8EFucNyQKMTix8Jv_rBbIo9Ij8Av--EcJW75j0EVoy679gHTrdMZGd2A-1pYHHo-Wq5vjnyB_ANKYTEPwTNOjJt5shqNQLvtAF_bUkwOZgzxFgKcgd4SZWe0BvPXli5qF7fjC7ZPL1EAqAGymhMvf8WAMqErZ1XEWnyXvOrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b95f1bafa.mp4?token=q8Lgom4swdbFP8DCLQLirwoqJmP03a0K8Dqmilzrd6jxImQozh9CbjHXPKzdCXBGZLRhL53M_uUOKrklaB4zTw9z9GprjFNBDB8IHFw_zimpnCtEEPLU8xINl-WPTaEdHIihg-ZPh0wDGOLmnCKzoPOcVHmefwb6gOcIK_6b6s2oGWvr9YYoeD_3LHFE49m4YOwphRbcN8n5VbVpupBUPUNoIwdIQHs7Dr33j-gZh9_ulR7dTzryHTrGTvYVRPHe18SnL8Z0Gg1J09xr6WXGoUhkudnhtCIqgvH9xOwa0OPu6WfXbIgRZdF4kRkFkWJmXcIT6i6s7ZHWifjYtgAIMK7kWdjjEx9rajHezGv1PyPTezOI3uuJ6i5LUc-KSXp3qkE27GKS93xIyJvvKSD0tq7p9fz-nVIydyLZ1w0ny3NYpyVtrpO-KtIruXDJBfhhFM57hCfKnykQFGI_qKLmHu_oeIKRwgU8TCzRSbq3x7n-kct_HOHvWHG2S8gSzjO_EZJ8EFucNyQKMTix8Jv_rBbIo9Ij8Av--EcJW75j0EVoy679gHTrdMZGd2A-1pYHHo-Wq5vjnyB_ANKYTEPwTNOjJt5shqNQLvtAF_bUkwOZgzxFgKcgd4SZWe0BvPXli5qF7fjC7ZPL1EAqAGymhMvf8WAMqErZ1XEWnyXvOrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گل های دیدار آگزبورگ دو - دو بایرن مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108272" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNT2hoZRKipvO2DmGHh8u7wwi8RFEUcFnj_21WR2vCtjAI0-ElxgChssYib00n6dSGVQtCaWnZEpY93gj1omd13Fg89PzEaJvJ9D2vuuFcbFcw_KTTQ6VxQCGNQFGubQ_B9C-Q_2wac06AWU8VNHp0Xmai1ZdlxI7SgWVtsWbZ2818V06f8umbxs14XXvfpgxQPdnxKdKlyARZ2fBqc6sP5Xc2_cPt0DcRZnxSoVHomqgt1hXzpXJbOv-fx5833KaHBzxkaSYD9I7YbdraFtw1gc2J6yRuYrg7vuiy4tu9UPyPykUnv5nEmdzBaUSOuXHR7MRsf7qCjNspcLfmSehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
پایان بازی هفته پنجم بوندسلیگا
⚽️
بايرن مونیخ 2 - 2 آگزبورگ
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108271" target="_blank">📅 19:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108270">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQNE5NBM94Z9luNhBeQrh9IZQlYqDit9mGWdILPOL-p7Lty0FZOOsA7PGWSJQ5VVf4nQ3tlGH42Dpox9S3B935M9nye-XWhFCE2gRa5x534jxFgrcoQJ9Ip6L-LP4V0p5KNJMhqdoTE3Pef3uZP1k6uzERbzrGbG5Ci9oVj66YJEqdH8XkdEuF5Kj9JM7oQ6vjxNadYz81avlsKvl1jzfXzdr-OdIIkxfoy4Jvmet7Rh2YZWnNcl_2lXaeMqOcbOimyxfL6V4Qe_9YlsjjbPl533WkSjZ-Dlb6ZgVV8QqPDZBoAZnvni7wMtNJdvlQpizCLXXJk4ctFyfuYCAEW6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108270" target="_blank">📅 18:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qc5TLZukBYzfPE8owarIAyCv7nhrX2dY0igwDfE5kJiB0t5SIC0KaP9M3k5B5NdEX-ALAxUnq3rFduQ9DNaY6Oeg3B7mnKGQi-1c_vkKLSbzqE0H8UQX-8uLb7779bq12yD8xKG4lHkdOJiTQPc9Q7x76HNuDW--6qd-KrgmYZuD36CJpS6fL3i6vc9i-Q2AI6oGO2iEwu3iN41d1DoF1-DQn2PsHnhnaQFeNciEQvop5iWrP_MUEahBcY-z8NK4EN_4T-HzrF7F12jwnY76UA9rU89N96qSLnMhGIl3X8XBGH7Kmc8NXOe8NOgNpV_BkXQPucrFqvaYudeFCzA_Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKVgult1H1wHzQojnPiQ56_lcFbAxaDhgwwkRFD791PnD-ak4odxCAlASw38UsaElQVTudY5w01Jy1vnaPH5HZB6_8Z2vZrqF1c5I5miI7InEWeAntjUvtWa__Po_pXMAiyBNok5-GDpI-Ca3beyYqawUJ5nLAHXCiRFD_KM2Tzq9eaJd90UsWT17v1wQ7a_9k0sLID4f9bv37PVoHsvY6tS6R98N4ilxVvjFq3NLCzshx0G9h2P4LnsBD5Hy7Wx-BaQhFvKd77qZvbe6jlPV-HUQQaYmugdeAv3sytPOcUZi6aLCS7tEa7i800aDQfCVKn0X7jLTEi4xBfkusmb8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب تاتنهام و منچستریونایتد؛
⏰
ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108268" target="_blank">📅 18:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWjVI8AGAlm9PIYXwO4oZlGjgdl-zVkJaqLlBaMcUbw6qhqyyE_xh2jrE4Y7mEW0yYz-iaaWiYxPHzUP64SZ3yTWIR_X9Fs9Yn6H4E9UbdhVg4aL1L-bb5yMzhJDyFxKF0vXf11hv6uK3KeVlNjFzIznb3L-u5tSVXK8jTscLj39lfq-VsDylrHjiM8TY4-V0WPdufAzBMpOkLygfhbcNvVPan9D_lc-4yiQqfmzjWwhocUZ3uzB0WdLAuPfztpp6p2Nv62AtGUi0Q8B3ejx2wnRwYIGwqnztKkshcX6YJ6yxWK0imfvvO8dryhMaX3XwDxeSQFpxbspdYtpuoFY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108267" target="_blank">📅 18:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pefL6TRlIQAkiZyaJVz4nizlKseXCK7W2Nu2erBOwIecdf1d-PuGXzFqHT9kYWhfmDWPY1y6EAYhWj6DgkL1QmxT1mTIWnG4qkrDI9OjGepqMfmB8csA7HAni7eYXe-58N0_X3gYguBDewg0Hwy79V_mg_lqeDpFVCkA1gcY5GUC4CxLPAb8M3w-LzjsQSt50Zibas0zkZOzLmEj1HY0uencBtx3KlOZsO82LYKo9FRgkexUgyOBAPU5Jjv53U05q_iN-WThOndA8lxNVsD5FxM6U7Az01igOGTWEWve83zoihalyADFbkxpae_Zwrd6Ny6UgKdQ3IYSuIrdvkVSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
با تصمیم محمدرضا زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108266" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33630db290.mp4?token=P1OBhLiGoZHWFxKlmH8cW56N_ZXA0VFGfg0kk6li7BKCBJ6hrGlQy7vql1MBBZFWdgok8h0Rg62Tgh3w8F9oqtlIJElyuZqCPN3VtTTj4R9TuRSVcyslAPR8RTWOZAR1RYv63eeWymZtNlkH-hZWDLCAyM4BobT5iUkDaSVuDLp4msyj9ta5Kz2kwMqLvs_XRiYGFNGWVRj2h3OhTTE-hojh8xIe2FntS_jsFyMj5sybTJqtAA3zfQACNlTLnTEpco7HDMh25CUhNITO96G4CmUiFCGepwCCKX4N7GSSVcvycb2zubKzV3vx1illsaVT52fXdzgLWUM9zHGnK-C-xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33630db290.mp4?token=P1OBhLiGoZHWFxKlmH8cW56N_ZXA0VFGfg0kk6li7BKCBJ6hrGlQy7vql1MBBZFWdgok8h0Rg62Tgh3w8F9oqtlIJElyuZqCPN3VtTTj4R9TuRSVcyslAPR8RTWOZAR1RYv63eeWymZtNlkH-hZWDLCAyM4BobT5iUkDaSVuDLp4msyj9ta5Kz2kwMqLvs_XRiYGFNGWVRj2h3OhTTE-hojh8xIe2FntS_jsFyMj5sybTJqtAA3zfQACNlTLnTEpco7HDMh25CUhNITO96G4CmUiFCGepwCCKX4N7GSSVcvycb2zubKzV3vx1illsaVT52fXdzgLWUM9zHGnK-C-xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
سیلی ساکت‌الهامی سرمربی پیکان به بازیکن تیمش پس از سوت پایان نیمه‌اول با شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108265" target="_blank">📅 18:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA292isKCBRkxuWgi8C9gioAriPYP4sr0uZX4NDlr4wTKsvSktcypGQYPv5CrIToiWBnHSAqMIhfDqG3mh7xwx9OXX8e-mhpIfs6KubNNau57bwbgVHCQQgfuvdhY5Tv0YCI_9oRE9nTH1Rl9OOI_hr3y-1dCoifdE3hjJ7WD6ExHxv-sP2JGrHzhqLojxsR15mHQ6BJDmUG_qRl4AU8ATs8Zi8qbEtiszoUKN7iLUqisqBTMdrnExBk6AMdGRi8mEupWwrp320k_v9hMxIeZcqDHQTfpAzi21N7OjEQ2nYmTqi0WFBJeyQIeq17N459oGajd9p_1TBkECTbNtUcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های بارسا و رئال تا قبل الکلاسیکو
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108264" target="_blank">📅 18:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=QtuNUI1XbZ4XQIYk8er_UmGa8HWf_42K5SKIwDiU_yAlvYaSPJX0u1wNnSgxhf5Ysvr4oEciPtrT884qfeUp-jmSblyt1LgWntBCGxHIE_wEY3ibcZhmaKFja7QwzYRfxama17CSYcskP5YYB8LOeT7ubPV5asM5U_tgpYa0mT8i2iB70wXTgfEm2i6pKHE0GO8UH2uRkGrTwtcjKRwzDSJ_1iYudZCFDtyQwVcBLqxWo79kVD3Yf9_OuKaLAOpwv8cY2Ek4EHHCoKpla49QcqtfimOtJE66oW9p94QwVsXzMJgdO2WH-klhv0R5Xqd9D-hZrOoy2FSNTRtyj-9snw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/974d9df6d8.mp4?token=QtuNUI1XbZ4XQIYk8er_UmGa8HWf_42K5SKIwDiU_yAlvYaSPJX0u1wNnSgxhf5Ysvr4oEciPtrT884qfeUp-jmSblyt1LgWntBCGxHIE_wEY3ibcZhmaKFja7QwzYRfxama17CSYcskP5YYB8LOeT7ubPV5asM5U_tgpYa0mT8i2iB70wXTgfEm2i6pKHE0GO8UH2uRkGrTwtcjKRwzDSJ_1iYudZCFDtyQwVcBLqxWo79kVD3Yf9_OuKaLAOpwv8cY2Ek4EHHCoKpla49QcqtfimOtJE66oW9p94QwVsXzMJgdO2WH-klhv0R5Xqd9D-hZrOoy2FSNTRtyj-9snw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
یامال نسخه ایرانی هم خوب داف میزنه زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108263" target="_blank">📅 17:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108262">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108262" target="_blank">📅 17:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108261">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCY6grdl3fVrLgwBPAxd7jhHuyYiPkmYFBd_ZFmhO8-6Mzfuyn3VmnQVjefb0A46jj9a8SGEk1ZS7WGtSImkrFDUqX5DI0mPrZFZr0HdPARskdvvTKTWJ3MfeCAHn8nKkNYLAg7LLGVAQPX8l_jdPLZwU3zUGIucld6qMfO3nHqUtQ5qgXoTja8mI4PRomVFcTOsHbbhSftCfZtZmnXnxJ2rsXp4JHjvoPqF71TvuxMnPoFxTQYXAwBOZzhoJ3QUSv0qqdFMFqSxvMwEbB80n-YQI7X0eqRfB3vNYFTPucNgJHjfdDAPVpvYsS9Huj11NhfwjaNrBTx-jfYBncZzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108261" target="_blank">📅 17:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=GoX_MmMrHLJQfVElNEfMxsUg6l41aziYGkxiesxSFiKjzFjDTFAx_JEQ9K0Vb6VVI36p6bMGCmJJaRBvobM1K6KEdSJfV0QDxxlu_cJi-PeQX-4gE2Oap0uNvpRJzL6_ZInZg-CDzcHbeQJxX6C4oD_eWxgZ03MMMXQktVyZQPV3o7TCH19oHr6xnLa4hZBqrUafJo_3SJwjWLBQOlQTA_GsdGEpqACb3PlJVOIqrEiz4A2lvBK7Bv8X7MQDe4FXWrSdEZuglUzC_PwUbm7SvV0mp99juN69Ire9oMC4ziHT9hgIWBVp6N8wiIH2YDKAnk9vzdfaopJuCQrWSu9URg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61d77833.mp4?token=GoX_MmMrHLJQfVElNEfMxsUg6l41aziYGkxiesxSFiKjzFjDTFAx_JEQ9K0Vb6VVI36p6bMGCmJJaRBvobM1K6KEdSJfV0QDxxlu_cJi-PeQX-4gE2Oap0uNvpRJzL6_ZInZg-CDzcHbeQJxX6C4oD_eWxgZ03MMMXQktVyZQPV3o7TCH19oHr6xnLa4hZBqrUafJo_3SJwjWLBQOlQTA_GsdGEpqACb3PlJVOIqrEiz4A2lvBK7Bv8X7MQDe4FXWrSdEZuglUzC_PwUbm7SvV0mp99juN69Ire9oMC4ziHT9hgIWBVp6N8wiIH2YDKAnk9vzdfaopJuCQrWSu9URg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بخشی از دادگاه انقلابی امیرعباس هویدا که وایرال شده است :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108260" target="_blank">📅 17:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=bxccI4FPjxiJcbdgs6CxYp14MDgqebDwz2p79W2cGQX1IheUYDzkRV8EXhK1EjP379KXWZDQFwK2NHqxAmn0w2IFINcNHbyBPJ0_1KBGyZlIPJy4PO_Gb0UwRO0DD67Hn1aar1zAmKLSy3cBRC9BWQbOYI-guH3SrWqUK4GqVTmvsaQlXNx2LokVkK5cz_egSV8AUSvlvGiwLaqEUA33AcWIwsXrPw_TzyIC2PflwtBkrEt4EQRmjDAFdB3CcZ69MuftOdTlW_WiKpEX3QwvRxHyM5ZMA4B0yaIMlZi4L6g3O8aZNwh-NXFTyZ1ejD6VOODnRdBfvGJPaDiHjUJLUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6680dee71.mp4?token=bxccI4FPjxiJcbdgs6CxYp14MDgqebDwz2p79W2cGQX1IheUYDzkRV8EXhK1EjP379KXWZDQFwK2NHqxAmn0w2IFINcNHbyBPJ0_1KBGyZlIPJy4PO_Gb0UwRO0DD67Hn1aar1zAmKLSy3cBRC9BWQbOYI-guH3SrWqUK4GqVTmvsaQlXNx2LokVkK5cz_egSV8AUSvlvGiwLaqEUA33AcWIwsXrPw_TzyIC2PflwtBkrEt4EQRmjDAFdB3CcZ69MuftOdTlW_WiKpEX3QwvRxHyM5ZMA4B0yaIMlZi4L6g3O8aZNwh-NXFTyZ1ejD6VOODnRdBfvGJPaDiHjUJLUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشتباه عجیب مانوئل نویر؛
گل آگزبورگ به بایرن مونیخ در ثانیه 5 بازی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108259" target="_blank">📅 17:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
⚠️
‼️
‼️
⚠️
میرسلیم: مردم باید بنزین را لیتری ۲۵ هزار تومان بخرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108258" target="_blank">📅 17:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bead49b429.mp4?token=KlOoN_V1TnTsknszvZ4crrEJEWZwD0mKLFF5jsfg6MHevhrkDHeJy-p5hEzGjx8Le__CGNNYjR-evUA8otNXm9VPHasNAmrMLxXZpWqjuc-iBqdpbh8zB9Z1Ptex1hsxR38EhbkiI0kaRWn_aiaIa4WKorp2-RsMAWjZRABQTyf9hEeNm4U-36PUSIuNKET1aMTUut3ClOyDMjz18w9YEPkg5thljQHj68DWy2e6_k0Z3x8_tV9unKbMoQsDigtXrPHPY2ylCKDhlAQwEqfQw312ljSC5PnSKTpQLHlbv5LRqd5LVXNcl0aozx6mhU9wzK8hCntstLs4j9zEdrvs8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bead49b429.mp4?token=KlOoN_V1TnTsknszvZ4crrEJEWZwD0mKLFF5jsfg6MHevhrkDHeJy-p5hEzGjx8Le__CGNNYjR-evUA8otNXm9VPHasNAmrMLxXZpWqjuc-iBqdpbh8zB9Z1Ptex1hsxR38EhbkiI0kaRWn_aiaIa4WKorp2-RsMAWjZRABQTyf9hEeNm4U-36PUSIuNKET1aMTUut3ClOyDMjz18w9YEPkg5thljQHj68DWy2e6_k0Z3x8_tV9unKbMoQsDigtXrPHPY2ylCKDhlAQwEqfQw312ljSC5PnSKTpQLHlbv5LRqd5LVXNcl0aozx6mhU9wzK8hCntstLs4j9zEdrvs8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
امیرحسین صادقی پیشکسوت استقلال: علیرضا بیرانوند به استقلال برود، من دیگر هوادار این باشگاه نخواهم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108257" target="_blank">📅 16:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1i1ZtP_zisU2cLjciNAJrhM02snpZd4edefjyxRGKfU6UsiosHLsx3K8TUJh1uElaTFTqwFaufabj-_3cAQvM93Y22qSl9fQBg2yYdTSIflOQnigTr78fsz9dH3jNI2KRgc66AHKTfNTiYJ9FOgvbIwPbfTCEYD0mKr_dLbk_1OmuAFOSK8fkgwsYv-M7fiIGaZv7mFbfDBKmddj4jiKfS8gvieLrn77GR6HpIpehKnpC3nx0yzkYlaoyPUzPO3gsFLxMZwcj_PfWSwiJoXMHCky5hCMPMx5IxGprVgsHWXdihXDsZC2ZJv3lOWZ6xyd4h7URTi17DfEQGMMQYjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108256" target="_blank">📅 16:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ3D3NZ--49bhzqnrdaCTWKcyjNRZ1T4kQpZCBWOU00NBoONpRdl5rf2fvMLv2vmLooq6uxEDJx0GpzxKc9W7tXPPGN6WoBgFw5wRCSrrL6sxR0Hicc52I7vZfAUH-3ACZXRgpMC-yswoHgJripN_bLLmjIGipTnQlqVTOkeFCYoSYETNpRh8xrJYlAVZ2DgA7Ggnn9nnau20gUPrXn8CoAf9Er3wi-Yqt6fh-L05bopbsvznOuRX88lZM7w7qivy4GLzqrdDP7-992026imCuS16_o5efcEjb9UrEukHsKgbGl-WNeOfRvFUUwJ70-Lsh0NJkshgkb8-IrtOHyo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
کاروان استقلال لحظاتی‌پیش با پروازی مستقیم از تهران راهی دوحه شد. مدیران آبی‌ها در ساعات گذشته توانستند محاصره هوایی ایران را موقتا دور زده و مجوز مستقیم حضور در دوحه رو کسب کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108255" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64417ab8f.mp4?token=v4J-rkA_YjYnfnaxZu21nVivmof46nRdlHeRe-7UoX02_-3oQiMJuu1CbBCnkS5xA7WngAoWrvCAZRj61FNgBbeP8NTr39SttQ8HV6aOBCNQ2Q4RbczTR4w_WYQTbc1hTcF44g5sY8VANXFq4viRAXI3oY6ij24C26zW9Q5vUmxs1UxwHw31gQMEno81z1vqaULUPyFXCRpaLCFI59gtjt5qxHEKyCZGnLE8a2zmm9mK2Nk4I3vGKS31ZQyzWmUXbjfXkZfc9I6dRyQKc-mveNSoSiD6g8btNsWNlchcRB-8MYv3ylTMyBLD_QPwhM4fEF-xAoPzVzsMPRAg_SNwqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64417ab8f.mp4?token=v4J-rkA_YjYnfnaxZu21nVivmof46nRdlHeRe-7UoX02_-3oQiMJuu1CbBCnkS5xA7WngAoWrvCAZRj61FNgBbeP8NTr39SttQ8HV6aOBCNQ2Q4RbczTR4w_WYQTbc1hTcF44g5sY8VANXFq4viRAXI3oY6ij24C26zW9Q5vUmxs1UxwHw31gQMEno81z1vqaULUPyFXCRpaLCFI59gtjt5qxHEKyCZGnLE8a2zmm9mK2Nk4I3vGKS31ZQyzWmUXbjfXkZfc9I6dRyQKc-mveNSoSiD6g8btNsWNlchcRB-8MYv3ylTMyBLD_QPwhM4fEF-xAoPzVzsMPRAg_SNwqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108254" target="_blank">📅 16:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108253">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb6a1e8ef.mp4?token=LXdjvYHXQCq5yZc4U6gNeoPQ7D3xA5CTxhOBav4iqHtPvUraaTpwAJvcHy96gX8CReLtQi5zdBlP9L-jTYVvf6DOjg3miGKdwUaui8qVZbX7Xz6PBpm4pjWS8qvUeZePFsYCJGM1dg9d2c7ujPqgaJ7bs2yVxHlEeVOJS0NDBOzjwNWi4-Cmh8kUWySdktDg2lPq7uAJuz_deWlYgoZttSpYEYlZvCixJ30aek97V5q0t2bDRQWhHVJtXBJOeeDPvnWmKAetMekLMnTcLGVoGLUzvxNYieBJu2pu5jEeYFTu26bvyaEUWGF7k-57xYApyaLCP3mdIabGm79COuGQHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb6a1e8ef.mp4?token=LXdjvYHXQCq5yZc4U6gNeoPQ7D3xA5CTxhOBav4iqHtPvUraaTpwAJvcHy96gX8CReLtQi5zdBlP9L-jTYVvf6DOjg3miGKdwUaui8qVZbX7Xz6PBpm4pjWS8qvUeZePFsYCJGM1dg9d2c7ujPqgaJ7bs2yVxHlEeVOJS0NDBOzjwNWi4-Cmh8kUWySdktDg2lPq7uAJuz_deWlYgoZttSpYEYlZvCixJ30aek97V5q0t2bDRQWhHVJtXBJOeeDPvnWmKAetMekLMnTcLGVoGLUzvxNYieBJu2pu5jEeYFTu26bvyaEUWGF7k-57xYApyaLCP3mdIabGm79COuGQHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول آرسنال به لیدز یونایتد توسط کالافیوری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108253" target="_blank">📅 16:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108252">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13447d981f.mp4?token=STA14p8WfvAszCqgWFvIasSREwUE-426preWDWqV7qLPEgfHINN5VzpNPwGKOWNn_55DeO5V-J4FR3yp5JX2-4Be74dlbMP-ayjNVrGZm4kb4ZHrT_bWuaytuz1G8kDtqgB5QiQSbu14JmiaASP7f8Rhj805uXRtTts6fFtXfVQigMWE-zHigt8-Is__tcITkUaFa5S8-ITRMeyq7mSRsutoWRlDd-nVU0aQYkPIQNowAK9C9RM7V1WyDprRAME3BHG0yuM5Z-f6WWeuC-TBcbI306MX16Thjf3gfbCmX-YLO7JHJKn9zjgeMQkdvI5phBaYbSuz5ScE5c_ZjmuEdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13447d981f.mp4?token=STA14p8WfvAszCqgWFvIasSREwUE-426preWDWqV7qLPEgfHINN5VzpNPwGKOWNn_55DeO5V-J4FR3yp5JX2-4Be74dlbMP-ayjNVrGZm4kb4ZHrT_bWuaytuz1G8kDtqgB5QiQSbu14JmiaASP7f8Rhj805uXRtTts6fFtXfVQigMWE-zHigt8-Is__tcITkUaFa5S8-ITRMeyq7mSRsutoWRlDd-nVU0aQYkPIQNowAK9C9RM7V1WyDprRAME3BHG0yuM5Z-f6WWeuC-TBcbI306MX16Thjf3gfbCmX-YLO7JHJKn9zjgeMQkdvI5phBaYbSuz5ScE5c_ZjmuEdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول لیدزیونایتد یونایتد به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108252" target="_blank">📅 16:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108251">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEgBLoZbpi8_HtA5ex_K1sSDRBuMsHjzGuZg8EP_pRNYeiI5wKnODsvNSa7MQ4LxM4Ms42SY6TUOJlP2kyVnVYDEFVsU-keP4sbIZMMKLgF3Eksds_SFhfsm-eWDniOGpD5_l3BCdhaMKCvleP1N95NCuz7Gkg7XLaELL3fsHBPNNWoKVgDee-7_nbjm_vmJg_X_T-be-rtPI51xYpaQAnf_rHRcBkRz8fTvmYufJ3IEsHYQ8ZMdw367vtP4qzNQbBEQif3AqkEJz8vA7KrUxp7rqjpmJOsch02axAV4ChNQM--iGXBmJn38iE8yFbuIrukVILsIdLh45hZ4xtSj5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
در فاصله دو روز مانده به بازی استقلال و الغرافه قطر، هواداران پرسپولیس درحال کامنت گذاری زیر پیج این تیم قطری درباره یاسر‌آسانی هستند. این درحالیست که آسانی بدلیل مصدومیت مقابل الغرافه به میدان نخواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108251" target="_blank">📅 16:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108250">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcEaJenp9Ls3YRY1gTfjDvUZReQIxVwNeBYT7TqRuJ3nZLGqsQoa2-NOjxcqUNHX3fPIOvBsBdqK5Dzd54SeXyPGP4_X85pxrtwhtE0UETQvASl5FQzVCw5tCENRvVWxswE8Q_bETGqu3kpvROrgHWbs-eSjzSzFHgpdV5txEdutGYzzKUhibY0vyqN6qHnu9NAuURdtH3n0gNKAV9-RDqlpJKu-4OJkdrT1hFosMO_he8ZmbO4xULvvwi4A7BGBT434cAsZNonEOUK27_vR1qqgIT7J9ALHtFSYi1ogLMu6ALd5m-jAYsXv5C1X6w4ofC9Yy8dTcNspgRNKvHx6ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇩🇪
شماتیک ترکیب بایرن‌مونیخ مقابل آکزبورگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108250" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108249">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85108132e1.mp4?token=lwEPjRCEdV2Gs08z1x5u4ZoHXTTRavDe0Ub8D7eGy_NC-MLHJD33THJ_bzje4HZKkn1EdywStan2nCmKo38L1_1aGcUWgAWhT7S5yn9S-JICvHwevfmRDw0CXLIaFbTxcqODYsf5R9Lsd890EHSaLxJ35uig2_urOdlqO-uzU_eXZAv35IWQiZlF6EpMTbXyMBSSoHH_i6v_kVtewhWCLHomCOidgBmExoYYPv8avApPzNgDDNSRjnw3EjnDgtNN3Yk_LZyu4GPOv-cuVtNWGISQT907sp0IXEO-mTl-qS8Y4ABwwi8nAq9RghNEwlDtLYy8kUue6LEOhUNqFAaObTZTW8FNEpMMrG3KCWiOgNm9ESdY6S92wXmGJRKBV_b7hs2A4aZAPW0p3mfbJ_F7GBCuKmyRu0VllyAq0yam916S2qdaK-GUqiJcXjnu6LIa0pDp-mJ4-JgOgvORxihvz5k1J63kSe6inil_k2L2NZkhUa4Wc4mrfFQ7DhcupwlNaOiTiNLBvjpQ7EQny8O-Cq-EunCDLUEPmWRcdZO7jChN73evv4lVYUiNe5RpakE0mdeGAtF8pK5NJj8OMof3KV_0fjIdMns1qelXCIUp4-gdrNV4h-7ZrLF2pJW0CgTvSMvctJfMIIc7-XBj7R0QcbQnXQs65_tDi4_QcKvMyBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85108132e1.mp4?token=lwEPjRCEdV2Gs08z1x5u4ZoHXTTRavDe0Ub8D7eGy_NC-MLHJD33THJ_bzje4HZKkn1EdywStan2nCmKo38L1_1aGcUWgAWhT7S5yn9S-JICvHwevfmRDw0CXLIaFbTxcqODYsf5R9Lsd890EHSaLxJ35uig2_urOdlqO-uzU_eXZAv35IWQiZlF6EpMTbXyMBSSoHH_i6v_kVtewhWCLHomCOidgBmExoYYPv8avApPzNgDDNSRjnw3EjnDgtNN3Yk_LZyu4GPOv-cuVtNWGISQT907sp0IXEO-mTl-qS8Y4ABwwi8nAq9RghNEwlDtLYy8kUue6LEOhUNqFAaObTZTW8FNEpMMrG3KCWiOgNm9ESdY6S92wXmGJRKBV_b7hs2A4aZAPW0p3mfbJ_F7GBCuKmyRu0VllyAq0yam916S2qdaK-GUqiJcXjnu6LIa0pDp-mJ4-JgOgvORxihvz5k1J63kSe6inil_k2L2NZkhUa4Wc4mrfFQ7DhcupwlNaOiTiNLBvjpQ7EQny8O-Cq-EunCDLUEPmWRcdZO7jChN73evv4lVYUiNe5RpakE0mdeGAtF8pK5NJj8OMof3KV_0fjIdMns1qelXCIUp4-gdrNV4h-7ZrLF2pJW0CgTvSMvctJfMIIc7-XBj7R0QcbQnXQs65_tDi4_QcKvMyBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ماجرای خرید تراکتور توسط زنوزی به زبان نماینده مجلس سابق(عای هیمتی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108249" target="_blank">📅 16:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108248">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4ro8j-OIy7vQ-EVLgF4tbnfZdV1mY_Yx_mbRWQ3eqw5koYMwU8Bn3HqciNbexmLPElQ_SPE2UiS8lwmI-icBIoizSeF2X6EjWM-XNSBHF8tdfxF4eR3-dk8oJz444AH8TUcWscMQItGOuKTwlbS5aK-VpjTU07Zu8xZQP2UPpG6mwfCDyFMcCm_MU4zPwG11-Ply8FbL9YqHdwQI18ms-XUlSxmlj2Y_xQbhO12GsDYKqszHuTTcBHFjy4FdC6eVnC3kzzL9HcKiWwFFjYNFycBTLicPN5-7-dzxZwxEyLzBln-pxqvs9OhfCERt7PfDspi-cJAMxVx7kbcf-GKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108248" target="_blank">📅 15:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108247">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajF_NyNK9DXwK9oR6YqiBl5qzSfWJfGIG8o8GhFbz11zFH9fLbMC6a6NBSGirJaGQjN2nQRdDcaZ3cdkCdRH2Yurq_TwZMdrtWXsePulZWp3FxfbJA2Env0eSuOJr8_sqM7GonHp5DBg8TSQZU3L3HTFjdr_yG3P18Yb-yNjII68a2GiDJ9aNTTzspiJpEs0v2wSkhuVDepxlXIBZfXZ5anIWZccGOeHmjYoPDUABsKP_YKZ7XRE40vEeRrqa7nhoNUrGOQuTP4eW5jyFIfE7ITeYmJ392uJHAYMdXCEiD8o0g9nf4jk6oEF8J1TGHaBNCSAYRbIifTZzZDO_mBT6RN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajF_NyNK9DXwK9oR6YqiBl5qzSfWJfGIG8o8GhFbz11zFH9fLbMC6a6NBSGirJaGQjN2nQRdDcaZ3cdkCdRH2Yurq_TwZMdrtWXsePulZWp3FxfbJA2Env0eSuOJr8_sqM7GonHp5DBg8TSQZU3L3HTFjdr_yG3P18Yb-yNjII68a2GiDJ9aNTTzspiJpEs0v2wSkhuVDepxlXIBZfXZ5anIWZccGOeHmjYoPDUABsKP_YKZ7XRE40vEeRrqa7nhoNUrGOQuTP4eW5jyFIfE7ITeYmJ392uJHAYMdXCEiD8o0g9nf4jk6oEF8J1TGHaBNCSAYRbIifTZzZDO_mBT6RN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🚨
‼️
عزیزی در فرودگاه بغداد: فقط ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108247" target="_blank">📅 15:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108246">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=d6O8vxUc16-wtvkZfz08NcIwPXremOTQxehj2W1cqvjl97D3Fs3-Id3m2lE597n9hJdXJ4Gqes5zKXKT2YrjAiAXPSnbkdvsQUE3NpGfNs9kDta6fDzjK06_1QZD1MH75uo52DPBAqjiFkZGdAQOrJ4GGA_JfGiNOUyPYmPky0lkjDhBHkffECPCp8a9eCQyJs1g4vqOrK9p4R2f4C2ZJk-BroHYB9nvCkDa9b31R9CIvWjx1rBQoCESLCr2JhDRHrFRRxI1hiOyBP14wPuMI4HYCNm_N-MnDYh1LoryMShRWfUyb0BathBFYkvEN6dQGiYMe1KTR4MGGDyR0lp97A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=d6O8vxUc16-wtvkZfz08NcIwPXremOTQxehj2W1cqvjl97D3Fs3-Id3m2lE597n9hJdXJ4Gqes5zKXKT2YrjAiAXPSnbkdvsQUE3NpGfNs9kDta6fDzjK06_1QZD1MH75uo52DPBAqjiFkZGdAQOrJ4GGA_JfGiNOUyPYmPky0lkjDhBHkffECPCp8a9eCQyJs1g4vqOrK9p4R2f4C2ZJk-BroHYB9nvCkDa9b31R9CIvWjx1rBQoCESLCr2JhDRHrFRRxI1hiOyBP14wPuMI4HYCNm_N-MnDYh1LoryMShRWfUyb0BathBFYkvEN6dQGiYMe1KTR4MGGDyR0lp97A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مدت‌ها فردوسی پور و میثاقی رودرو شدن
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108246" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108245">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=vxFLP86rSvCECBC8E4X2h1ky5T0F-QXApTBfhtQ0663W-8nbktR9306FA-zMUYY3Sulk8Ndl_p_02bdfP4oeY4YtUDu8NubZL1RfloiLNgqIDuveOQo-Z7MmcW3rFZd1qHK7DVpsQiz1xpyu_JLYaNiV0w3nOLJmZhOzMH-LEnDZLYDpWQ0Q2zV4YT3DmadffyRq_HNY6hyiHmWYu4UMmvnEbtvR5FvgH-itsYacXJyyGlSZah5uqjVfxKgDe4n2n0vieTtNVKPSShI2Pttw-VTEvlULSmY1Wjk9E1Tm_sln9FJvKz8IjJK143tFuB-g1yY3ApfJ0rqE6ZcHiIw9EK8KGsfktoDXnfpPPNjTxEDvwZ-Kx2Qq9g07WrcdKcm1QhVq95O88cVapa3OXoC4gFcVhXkNmkaNzcNGt4acJivZjIxtxC3bFISog00FZlGif1XeoqKnC7gim4bpkFl8VNbohZo7pDw_u6h354dfMTm-A8jPHnR-m-NUhBcIvCL0WAWEvs4t9wriyObRkU2nZntbHInu3hEXLjmTU_0elMkypfd1XQfwwunS3BIvPepZTKAmnwSggQOIUuu3IEg3CHX3qi1rApz64OBjXe-xGZB_ngXKHLZGGoL8dyZp-B-J9ImKSJc2TZBYVrTctmztpW2cHm2Obcl9CwZvG7xGKbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=vxFLP86rSvCECBC8E4X2h1ky5T0F-QXApTBfhtQ0663W-8nbktR9306FA-zMUYY3Sulk8Ndl_p_02bdfP4oeY4YtUDu8NubZL1RfloiLNgqIDuveOQo-Z7MmcW3rFZd1qHK7DVpsQiz1xpyu_JLYaNiV0w3nOLJmZhOzMH-LEnDZLYDpWQ0Q2zV4YT3DmadffyRq_HNY6hyiHmWYu4UMmvnEbtvR5FvgH-itsYacXJyyGlSZah5uqjVfxKgDe4n2n0vieTtNVKPSShI2Pttw-VTEvlULSmY1Wjk9E1Tm_sln9FJvKz8IjJK143tFuB-g1yY3ApfJ0rqE6ZcHiIw9EK8KGsfktoDXnfpPPNjTxEDvwZ-Kx2Qq9g07WrcdKcm1QhVq95O88cVapa3OXoC4gFcVhXkNmkaNzcNGt4acJivZjIxtxC3bFISog00FZlGif1XeoqKnC7gim4bpkFl8VNbohZo7pDw_u6h354dfMTm-A8jPHnR-m-NUhBcIvCL0WAWEvs4t9wriyObRkU2nZntbHInu3hEXLjmTU_0elMkypfd1XQfwwunS3BIvPepZTKAmnwSggQOIUuu3IEg3CHX3qi1rApz64OBjXe-xGZB_ngXKHLZGGoL8dyZp-B-J9ImKSJc2TZBYVrTctmztpW2cHm2Obcl9CwZvG7xGKbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
آنالیز ساختار دفاعی استقلال در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108245" target="_blank">📅 14:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108244">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bed940014.mp4?token=jDd1E5sSXHuAlNgpWVGl20hRPMvm913rMg3ZdzqNTQIxuwhL4Ug_DBzkA61_LJwROq1B5yP1r3sp3e8mObua3k3zRFe6lO7UcZTrAQlHt6KbITXmqA2jqK_uwt1EgGvzJEb_MlsuvNDVXhxOov9o_DFW51OMtegSdbxRuKvKveLGp-oiEwLPCmLbnogPf6I8ZLO9tar5Lmpkwoso79Hd-_tNLWFbhzHOJjEhrwBCqTmCXLLmDFdccV2orzqwNSeGtNzNhD4nnTMfgngcihqbjsGZhnuJCD3QATeB50u7a9fvgld77BoMYKovnLsU4ptr4C005ubzX6gsx6Xjuj1ZjrJD_t_jJsGDUnJlypxzhWFY0PoJWQwkDy1pzi05mpoFFa2fWrNKTHY9sEecK85_W78z9kDc1mAcGXNF48RGS2Q-6fFdpzufw02OZWkXwgn7UDzD42jZM9NcWyWXLuuUI7njOqa_uhisdMG9QuOAuiq3jO4sGB4nXrMoqJYOp6OGkXlMoDdAO8hxd5iYqwobcYB0MM-TEJbzSwNqhnS7OgpCkKro3CzoticeqSt1DtBW9iF7VoEojaOFBDJ-OkXMWOu2SaRjFuHQ1W-DE7y5QTjSTZL8K5zjt8P0ixENBE6IZ0j-SRn6EfEYNj-xFafIZTHRXCwZPlTBaVwDSpaRJ-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bed940014.mp4?token=jDd1E5sSXHuAlNgpWVGl20hRPMvm913rMg3ZdzqNTQIxuwhL4Ug_DBzkA61_LJwROq1B5yP1r3sp3e8mObua3k3zRFe6lO7UcZTrAQlHt6KbITXmqA2jqK_uwt1EgGvzJEb_MlsuvNDVXhxOov9o_DFW51OMtegSdbxRuKvKveLGp-oiEwLPCmLbnogPf6I8ZLO9tar5Lmpkwoso79Hd-_tNLWFbhzHOJjEhrwBCqTmCXLLmDFdccV2orzqwNSeGtNzNhD4nnTMfgngcihqbjsGZhnuJCD3QATeB50u7a9fvgld77BoMYKovnLsU4ptr4C005ubzX6gsx6Xjuj1ZjrJD_t_jJsGDUnJlypxzhWFY0PoJWQwkDy1pzi05mpoFFa2fWrNKTHY9sEecK85_W78z9kDc1mAcGXNF48RGS2Q-6fFdpzufw02OZWkXwgn7UDzD42jZM9NcWyWXLuuUI7njOqa_uhisdMG9QuOAuiq3jO4sGB4nXrMoqJYOp6OGkXlMoDdAO8hxd5iYqwobcYB0MM-TEJbzSwNqhnS7OgpCkKro3CzoticeqSt1DtBW9iF7VoEojaOFBDJ-OkXMWOu2SaRjFuHQ1W-DE7y5QTjSTZL8K5zjt8P0ixENBE6IZ0j-SRn6EfEYNj-xFafIZTHRXCwZPlTBaVwDSpaRJ-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
على تاجرنيا رئیس هیئت‌مدیره استقلال: از فحاشى هواداران به مادرم خيلى ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108244" target="_blank">📅 14:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108243">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=uIj8nNX_TXAKVGLRim0Ebg8JxdXD6NsvsIDz_zQk0Y6m6hKUjIQpPN0HXIFs8MS3PZpamDfn_cXU7YuOCFi-IjtCq3o4ezOLuDS8ZaE6A-beOiLzY4UcLzwX0yG8E5X09IoNUPiVouUMwBVlTE0Y49B96B4nDfSYWdMxBdIs1SNMkQZFKcojB62ewpB-YDOnwxo0nAVZM5NOoF_1a42Az6y8yKAqxQHRDmfLd3kEOudzjOEGFCgz99FW2X2XueJrlLG83uJ8gc3bDL08CRSIh6jQxN_C48U2vyRj5-RxbUOtlV1Dy5inWrTwIe8HJwHFEiPMk9WQb5Eb8HNGvBijyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=uIj8nNX_TXAKVGLRim0Ebg8JxdXD6NsvsIDz_zQk0Y6m6hKUjIQpPN0HXIFs8MS3PZpamDfn_cXU7YuOCFi-IjtCq3o4ezOLuDS8ZaE6A-beOiLzY4UcLzwX0yG8E5X09IoNUPiVouUMwBVlTE0Y49B96B4nDfSYWdMxBdIs1SNMkQZFKcojB62ewpB-YDOnwxo0nAVZM5NOoF_1a42Az6y8yKAqxQHRDmfLd3kEOudzjOEGFCgz99FW2X2XueJrlLG83uJ8gc3bDL08CRSIh6jQxN_C48U2vyRj5-RxbUOtlV1Dy5inWrTwIe8HJwHFEiPMk9WQb5Eb8HNGvBijyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر چالش را پر قدرت ادامه می‌دهد
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108243" target="_blank">📅 14:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108242">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbBymjN-GtijJ_bFpf9iASiWIaTPDwozdItTQR_FDiEPaziX5TII-LCCJ5zTwrHCMDTSmrhfQy3trQWHQYH_80vCBNu5KqkX0QYjggDdG5obS79GHpimsfNMp9f-csM0oJcHnS1-HBFBr2-j5cgUT3kdmZ3qyHSePMIDXsTlAUSpwNAhxF9ihhjhup6Y2oqNKRHma2URMHuL1Bhp_GtMoXXp_dNPLmZraW9hKIB0rkiAO2Ugr6_9rvzli5DS341FayAbiJuVX7aBWu-ZZdsfsht4cfAHXdXZN3H4uDroPjv8I_77Z9szsPHtnCdtrzwvXyWcdB0gwzQFNVYNByeTfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بارسلونا برای بازی با ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108242" target="_blank">📅 13:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108241">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsLWE0rT8t7bL3owAMbyJ4wowmvcc3zmWmkQVSm-1WK4BL9ZoTMmGAvueFjrGHPcheGg1veYSbQsATXUA6XNR5_XQJWH0Wzy-IecKEClbxnV1C6qO_yVJotA6KP6MIP4tdl1hl0YfPqHHWGpFl8OJwebCSXGq3SaCnIdj6qKjPm_YK8FE8G01qvU_PCnQ5b6to34HsxxxDVNqKDvVvXUeefZiipM9EnuQSxRAo5ghEwcojtRm1QGxIe7LBadVajrK4j_XxEHch0WrHJJEj4luM2b395t0JSaa87zVBLjRXuPQeyQueC7TleZJpdVIZf849A2fUxheLCpAdOH7umsYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال برای بازی مقابل لیدز؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108241" target="_blank">📅 13:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108240">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqMCA5quzZcp3CzbCww4D_jZVTx7Ok2oqeWQqzrZSW3TxFzks4CUj3vvaJRYyj7adKfglz0QojKPydP7fDfwkC_EdLTeVpjKK-WXv0fhYnpsSD4k0EFy6z-QCxrRdpUFgF5f69oFuQJrkI2YHAM8SvU2TGS5aCtlabtovMjUNcxaJAvACN6daSmce9E-_OxK1WqxpHyz-5tMJqz4sarorrPHS3jSiLhS1yO1UxnVy0j9rf-VKhshmyrBxi4DhE7EYOnxmZZjrFZDVG6IhDSufVb6zrJwGazUMSDCO3rgRUSpNpL1ryCq4diHVqzBrT1cufx1hWFwxi7DxvM60XhhRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚔️
🔥
بازی‌های باشگاهی بالاخره برگشتن و قراره طی ۴۸ ساعت آینده این بازی‌هارو داشته باشیم:
😍
🇪🇸
بارسلونا
🆚
ختافه
🇪🇸
🇪🇸
رئال‌مادرید
🆚
ویارئال
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🆚
تاتنهام
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
منچسترسیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108240" target="_blank">📅 13:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108239">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=fg5APBepfBkPpVXRB86yfjK91VaWb8BI-lIXcyOl6BfwAVp8RyMd7nv6o6ZoKS7zL6F8JoJO_Q5IIM8k7CPFIKfUVzj-BO-rDO3txKU7da5gs_9HM_LEgC5HI4lp7xpF5WnoniGwM4llkHEP53feXVL1qaCiZgshMPC9BxDiwWv5POjU3uATEan2LlBJhW_1NqSVP7gCaIcLyTU6gr4vVXLDb27S0sZTkOXhGxW5mDN4NQMQ3CDgbmLj5SnW64FGB9GtXEEzuRWoPGq44QpqN18zH0iRPSIksDMX4JXU4C3oGrcLc3wHlEu_x53faErIRUNhqPrH0NLawAfLUw-9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=fg5APBepfBkPpVXRB86yfjK91VaWb8BI-lIXcyOl6BfwAVp8RyMd7nv6o6ZoKS7zL6F8JoJO_Q5IIM8k7CPFIKfUVzj-BO-rDO3txKU7da5gs_9HM_LEgC5HI4lp7xpF5WnoniGwM4llkHEP53feXVL1qaCiZgshMPC9BxDiwWv5POjU3uATEan2LlBJhW_1NqSVP7gCaIcLyTU6gr4vVXLDb27S0sZTkOXhGxW5mDN4NQMQ3CDgbmLj5SnW64FGB9GtXEEzuRWoPGq44QpqN18zH0iRPSIksDMX4JXU4C3oGrcLc3wHlEu_x53faErIRUNhqPrH0NLawAfLUw-9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
باهنر: ایرانی که صداوسیما نشان می‌دهد کجاست که ما به آن پناهنده شویم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108239" target="_blank">📅 13:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108238">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seZS3oPDQwxxemQmYpHmMQq5Cn6OgIK1ilkuPbebp7nf1ipjX9l0a0F841QJWH9t6ROxEHhEfTXC-ppjuNW36L9k4WVGFV15-2ftlvN7-LQcPS_vLffZIbKENXzgKtLzxlqYZzt-3TZt-iZEO92g7BHNOgyIDKscAivund3sIDmgbyqlyig26ilmjABP75lRlTpBphHBe3Ui7NNmGpzQZhKw3az51gw_2-VYmi2-Y1wzsa-BgDBluRNGynpKg6T5M6dtWrKXlzgU_quTOrg3Zp7orQQ2Bw4SoR549BvCx-ZCNdQGx-vspCoi-f1lCZzVHr5kvoe3sN850tDwIzjxBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد کول‌پالمر با چلسی تا سال 2034 میلادی تمدید شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108238" target="_blank">📅 13:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108237">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=eogvjQtuAWjJvxWEUHCGJv3TlX0D2xWAAXuIG2FMOIEC5aPMWxh_AU9D5nCK-f7ytZ4k7QcQ8Z5Fg92hdGDY2d5DW8RY0URiDk_c8j2mlDNOKm6F6yeQLbNAkd3DfW22ILVabbrGuRNFN3_VmImpUTcIey44adkwS5mc1cI__CwwLukBv-zYYI7tfaZRWsl8mKoidsm3RH0RmYjS27AXoDRLz3uuxwFAbSKLgVcDjr0OCUEMwjcPffKp-df2kBeAsZQB1cLpW0qhnZsgkCFhiBShkuIEys3CxjngYtEBmg5NIXAe9OTSr8zFHoqgHUthjxVK7YYED4iW6AlFmaCJ9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=eogvjQtuAWjJvxWEUHCGJv3TlX0D2xWAAXuIG2FMOIEC5aPMWxh_AU9D5nCK-f7ytZ4k7QcQ8Z5Fg92hdGDY2d5DW8RY0URiDk_c8j2mlDNOKm6F6yeQLbNAkd3DfW22ILVabbrGuRNFN3_VmImpUTcIey44adkwS5mc1cI__CwwLukBv-zYYI7tfaZRWsl8mKoidsm3RH0RmYjS27AXoDRLz3uuxwFAbSKLgVcDjr0OCUEMwjcPffKp-df2kBeAsZQB1cLpW0qhnZsgkCFhiBShkuIEys3CxjngYtEBmg5NIXAe9OTSr8zFHoqgHUthjxVK7YYED4iW6AlFmaCJ9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله جدید هادی‌چوپان به منتقدانش در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108237" target="_blank">📅 13:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=qGeVP0H3-xBJSCEMpy-U2IEqYr3NF5fTOfp2r--s157IOEICWcytyhOUDCRQ62zKI7WStxFvuLNgPfZeDqJZJNpHU78Shers0aP2SIHGNQoXYd5oCrUpMuvc_kUZLv6ZFX9FWnYSDQ_PnZ2rMInyd3M6SPkByB0lZsVRwDznzFGjf23X5pTuaeDrd2Fdok7tbvHziAaBRQFFkUEMcAmpZWH5T9VzLGvlDTb2YH6TEepwHrusmY02sm5ehWaT9pR8mW9DvvCJPe2-BGRxoB39sQD5Etf_PXF_Z-I0wA29IncxjLE4BtznATsogsh2QqPy9K2EdgeWtIKf7cvk4HMdLHHMOZ2OTMXkBF16pc4iVdudB90gXU6pipQrJwRJ3rB76psU6hx3pmdnbnaVxCmB0MigAjnWSJ8brMXfcJLmbTb6k3LAc7Vrhw8kshjy6pw_PjrV0MFLO07yujnwutHTDfoNiCWOabS_SWUvmpfBDtfHi6EVpXc4lR9Z58o8_bDxPUJJWCdLQ4oLTI28xgXS-tt8vh2pKzuLAymkSjbXPTwrsHvHcB2cCgJ6FQq1tTWUABX_QCR0ehbT9JeD70GBzBqUVvsHxovSlVZbS41F3hhEv_1j04kUe282s-U_28wVZeJNCH9ZxgyDn4IPtfUaL4hXee_AX7UZL1AJmzWYqhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=qGeVP0H3-xBJSCEMpy-U2IEqYr3NF5fTOfp2r--s157IOEICWcytyhOUDCRQ62zKI7WStxFvuLNgPfZeDqJZJNpHU78Shers0aP2SIHGNQoXYd5oCrUpMuvc_kUZLv6ZFX9FWnYSDQ_PnZ2rMInyd3M6SPkByB0lZsVRwDznzFGjf23X5pTuaeDrd2Fdok7tbvHziAaBRQFFkUEMcAmpZWH5T9VzLGvlDTb2YH6TEepwHrusmY02sm5ehWaT9pR8mW9DvvCJPe2-BGRxoB39sQD5Etf_PXF_Z-I0wA29IncxjLE4BtznATsogsh2QqPy9K2EdgeWtIKf7cvk4HMdLHHMOZ2OTMXkBF16pc4iVdudB90gXU6pipQrJwRJ3rB76psU6hx3pmdnbnaVxCmB0MigAjnWSJ8brMXfcJLmbTb6k3LAc7Vrhw8kshjy6pw_PjrV0MFLO07yujnwutHTDfoNiCWOabS_SWUvmpfBDtfHi6EVpXc4lR9Z58o8_bDxPUJJWCdLQ4oLTI28xgXS-tt8vh2pKzuLAymkSjbXPTwrsHvHcB2cCgJ6FQq1tTWUABX_QCR0ehbT9JeD70GBzBqUVvsHxovSlVZbS41F3hhEv_1j04kUe282s-U_28wVZeJNCH9ZxgyDn4IPtfUaL4hXee_AX7UZL1AJmzWYqhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز دیدنی از سبک پرس فوق‌العاده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108236" target="_blank">📅 12:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=ASKp2KZmk15J3BEqrmnGCcdSViLfzWPEhzWtmZDY0eRb_8S-R-c5IYaH2PgJccm7eqUU9pLKFkzr5-6bDjPESGGuPWvkmIjHT3J9y7bHYXPFtNtCYlHv__fQhh6OwBBACmECrMDjmVaMatZFlZ2tVvoAeEZfRfPUU07Z1kE3UdOj6gobnmjBPvjhP1KmxUt8vwK9mlGoXbbHefBqlLqDh_A4o1RSpA00u3SRZGCW4aZpSWMkrtFMA08E3IDmjk1Rxt-cgDehpTJlBexWJLXSOlAd5ubrlaHBdfQQjd_P55595eHGwNOO0Bdm-tHaBEnC_jNeBkLoLj2pwBEt2CFStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=ASKp2KZmk15J3BEqrmnGCcdSViLfzWPEhzWtmZDY0eRb_8S-R-c5IYaH2PgJccm7eqUU9pLKFkzr5-6bDjPESGGuPWvkmIjHT3J9y7bHYXPFtNtCYlHv__fQhh6OwBBACmECrMDjmVaMatZFlZ2tVvoAeEZfRfPUU07Z1kE3UdOj6gobnmjBPvjhP1KmxUt8vwK9mlGoXbbHefBqlLqDh_A4o1RSpA00u3SRZGCW4aZpSWMkrtFMA08E3IDmjk1Rxt-cgDehpTJlBexWJLXSOlAd5ubrlaHBdfQQjd_P55595eHGwNOO0Bdm-tHaBEnC_jNeBkLoLj2pwBEt2CFStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دیس شنیدنی قیاسی به قیمت کالابرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108235" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=BRPHxC6r4e8Qk9W5kus8-PU3BYb_YUeojOEsbUbxbeIP7PGtw2a9D18wBBY1084CzwJHcFSwFJqP54tAd9KIdTL5hGcAhUHfgLqpQHWwUffZ7wBBTQciZXmFCvBmFgPX_vsIadA6qLCKA8leCv5IDKxFDCkXF8N2HDZvZ8dpGQ0y-sT7yVd_TG34i6Q-pXC5owMPfoj_uQmqRSKhoyEKibN4WQNUYEFL1UuCjv_V7k0nbCZSH2vRsP_Bz7IhWB6WR2DfCYimRYKJv1LqacGG4kMe1DdNqpknN9lIVlQewp9_BNYHSpGQ4OfJ_VeycBmXOHbAN0AA91-9afJE36aWU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=BRPHxC6r4e8Qk9W5kus8-PU3BYb_YUeojOEsbUbxbeIP7PGtw2a9D18wBBY1084CzwJHcFSwFJqP54tAd9KIdTL5hGcAhUHfgLqpQHWwUffZ7wBBTQciZXmFCvBmFgPX_vsIadA6qLCKA8leCv5IDKxFDCkXF8N2HDZvZ8dpGQ0y-sT7yVd_TG34i6Q-pXC5owMPfoj_uQmqRSKhoyEKibN4WQNUYEFL1UuCjv_V7k0nbCZSH2vRsP_Bz7IhWB6WR2DfCYimRYKJv1LqacGG4kMe1DdNqpknN9lIVlQewp9_BNYHSpGQ4OfJ_VeycBmXOHbAN0AA91-9afJE36aWU4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108234" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108233" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgOtqYUnxdXIkl9z3UQdvrFhQxILviHxpAp98nPlgMvth6PPHN0PRiuAY3IkxQd7nlmQ37x2dL8deQiqxPBfUqeUWLegJtRLdBMWojNjkjZMDgPHeRT_eCxeO4Lqync9S1bMcaza8-im8J345JoHdKJuByyPeSMseUp_SKxXht_1TAGvM_Dg4Ffr7sphAa8ejCgHquJX84In3ohlofQS1KR1qY6KkpBQu61rTq-1SigoFl2GIMLQ7pKvKK6AveD6SFT-CnVPOhjjw0nRdblwvfEWHYhW-n5VRQY6Y6fA1WjKZrphI42QK6KmgxTXA8cCSbAq1dJFNOanOiYIsWJZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108232" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=J6Q4NMn-46528WCrmloiYorZ-osiCGvA_4LzaOvHBEwgcZwCoB8eB7GhVCxlP7huyUd-u31y8EG3_c-I19suWiBpen2Xjnm74uHuDJfStoKY_u7Bwi0UmKXdPzhDBOEbDwN_rJxFqZIkM7yndIAVN6UDkyMxSaNskbJqBGnoUtO4_tpn1gxb4olmWWcfjQqJwrKEKqzrTYWRCKBguZgATrIJFVK0VJGfA686Etl7h0vN_vv8squHTrUSdlF01XctcuTcXtvkkKo3o2X3keIygD0cJ131BhIGAwVPEJhsAY-F7A2choqw-uY6VQByf8593Zytop4JUe_yFk74ZAmNig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=J6Q4NMn-46528WCrmloiYorZ-osiCGvA_4LzaOvHBEwgcZwCoB8eB7GhVCxlP7huyUd-u31y8EG3_c-I19suWiBpen2Xjnm74uHuDJfStoKY_u7Bwi0UmKXdPzhDBOEbDwN_rJxFqZIkM7yndIAVN6UDkyMxSaNskbJqBGnoUtO4_tpn1gxb4olmWWcfjQqJwrKEKqzrTYWRCKBguZgATrIJFVK0VJGfA686Etl7h0vN_vv8squHTrUSdlF01XctcuTcXtvkkKo3o2X3keIygD0cJ131BhIGAwVPEJhsAY-F7A2choqw-uY6VQByf8593Zytop4JUe_yFk74ZAmNig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرحسین قیاسی: گلشیفته میخواد برگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108231" target="_blank">📅 11:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108230">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28909a001b.mp4?token=AFIZH-ahrFNEaY6QLGMsoCMNrk7-pcQhoewJiYq8pqf5qjnobz90Fq_Q-CMnFH052gmqsfICcZ68zX-sqURMBNo5VnfLMKfsRaVThejqvlD1DPhesWdBPYLbgoRP9Pz9pFwZvUvj2JKzd38xs5pZlHCMidExtLe4oNWVAW8IFpPNUXm5nqjjyB-66ys4nit6-CXwLAoSjOx6cBCat4LN215zysse4Nc6-OxRSJZB73xcTE_btgIP4Li4sIhiWH_v59p15LbY2mgFiMALBP8V5QdigCX4KP4k-P2k4tXSKeNvVv9_4g2KW9t1JRa1TGzOWIQBcsVgsg4BPA7_WTCoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28909a001b.mp4?token=AFIZH-ahrFNEaY6QLGMsoCMNrk7-pcQhoewJiYq8pqf5qjnobz90Fq_Q-CMnFH052gmqsfICcZ68zX-sqURMBNo5VnfLMKfsRaVThejqvlD1DPhesWdBPYLbgoRP9Pz9pFwZvUvj2JKzd38xs5pZlHCMidExtLe4oNWVAW8IFpPNUXm5nqjjyB-66ys4nit6-CXwLAoSjOx6cBCat4LN215zysse4Nc6-OxRSJZB73xcTE_btgIP4Li4sIhiWH_v59p15LbY2mgFiMALBP8V5QdigCX4KP4k-P2k4tXSKeNvVv9_4g2KW9t1JRa1TGzOWIQBcsVgsg4BPA7_WTCoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
نوادگان یوهان‌کرایوف در آکادمی آژاکس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108230" target="_blank">📅 11:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=APs7i8V00s0IHNJPHZk3qLUEP-0WYuoenCuzq0rwvbgghReChC5GVeCw4jMrjWpYikS1qz5J4Fcx1lYOM-cgmG3M1bM_2ffr4DAUPYk1V1Vu5JUmCHY3Xqpe5peqnHI6CdSrT2w7p6IFXIV6bF_deXotzNd4qd5QYIqVzQKIvvBT2Xb-eA9jKrAhstoNM7bonjUkeq886xC51D0OtCOlkCtyfyX5K9zispozSZNUV29shhOE9Xl0NPaQooQoR7m6Aua8k7vw1tVt0CWRanwkW7dxjDvR_eQO1iuAPVzNC9tGDeGrrnYdWxKOafM7-6os154FIpYF1b8eeBK0Pq_IaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=APs7i8V00s0IHNJPHZk3qLUEP-0WYuoenCuzq0rwvbgghReChC5GVeCw4jMrjWpYikS1qz5J4Fcx1lYOM-cgmG3M1bM_2ffr4DAUPYk1V1Vu5JUmCHY3Xqpe5peqnHI6CdSrT2w7p6IFXIV6bF_deXotzNd4qd5QYIqVzQKIvvBT2Xb-eA9jKrAhstoNM7bonjUkeq886xC51D0OtCOlkCtyfyX5K9zispozSZNUV29shhOE9Xl0NPaQooQoR7m6Aua8k7vw1tVt0CWRanwkW7dxjDvR_eQO1iuAPVzNC9tGDeGrrnYdWxKOafM7-6os154FIpYF1b8eeBK0Pq_IaYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای خواستگار عجیب رضا گلزار: دختره بهم گفت نمیخوای تکلیفم رو روشن کنید آقای گلزار!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108229" target="_blank">📅 11:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108228">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=t67O210b2H1hXNGIritdj13jEksNfW8Gk-9k2bT54Ahode8mqmpJRChVAazuPAgJnSylD9zvfVY6WxneC8qaVEciJd6GC7oaVlYE9LE_mxPqdlpQZfl0rpm0eWib3ZLLkEfMEIJSG5KN0GUT5kfe1FAYMQsKinLy5SFm3iBJGzhoniWoE9xC0Gq3ze_Kt2_DdSpUe_K4afl8JaVcmPgK9y79mbZ1f1xu7z9p9CNh4_ibHdDkv4CI7u4dkqYoKyOKGWwZ6jNiUIHa7JFWylVLVXQ0iRBUMYH-XMUaGnFeuAjpnFjUavDicMgeGcLrF7bB-DDmBQhAaBCuAWTgFjic4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=t67O210b2H1hXNGIritdj13jEksNfW8Gk-9k2bT54Ahode8mqmpJRChVAazuPAgJnSylD9zvfVY6WxneC8qaVEciJd6GC7oaVlYE9LE_mxPqdlpQZfl0rpm0eWib3ZLLkEfMEIJSG5KN0GUT5kfe1FAYMQsKinLy5SFm3iBJGzhoniWoE9xC0Gq3ze_Kt2_DdSpUe_K4afl8JaVcmPgK9y79mbZ1f1xu7z9p9CNh4_ibHdDkv4CI7u4dkqYoKyOKGWwZ6jNiUIHa7JFWylVLVXQ0iRBUMYH-XMUaGnFeuAjpnFjUavDicMgeGcLrF7bB-DDmBQhAaBCuAWTgFjic4zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تاج ادعای کریمی را تکذیب کرد: نه تنها ۳۵۰ هزار یورو ندادیم، از مربی تیم ملی جریمه هم گرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/108228" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108227">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حسین‌کنعانی جلو این اسطوره سندورم‌داون داشت خودشو به فنا میداد که شانس آورد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108227" target="_blank">📅 10:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108226">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=j64WaVI40iL2wkR3J1M-1mWS_BNAljlhvoUBmaz_Nd4CpFnS9wlZ4G7a5p4l3ESBzgdkJiU0kw3EpeZOxJYwgv08KpPO5Gg6gwRcoq5kfS6ZkN1lK1WSDQGkQuQ-SQVpv65TaSHMSurKPqGLvgKb8_ZHalb5NeqPvhnFvwtI4OeKU2sbVfI1MS-Knb5Iex0FwPE8oGKR2VHHrERM1m-H45tCncZpDVvyRLzzeJfjrDwlYYXxn84vh2_q73LX6i6DXLz_vTsHeMkCR0n9LVhgwLoGYPZa6ie6gSnROzLQu6LmQVxgKORdN4J-1OpYKyKuZ0Tc-3f9D393QUdb28NjIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=j64WaVI40iL2wkR3J1M-1mWS_BNAljlhvoUBmaz_Nd4CpFnS9wlZ4G7a5p4l3ESBzgdkJiU0kw3EpeZOxJYwgv08KpPO5Gg6gwRcoq5kfS6ZkN1lK1WSDQGkQuQ-SQVpv65TaSHMSurKPqGLvgKb8_ZHalb5NeqPvhnFvwtI4OeKU2sbVfI1MS-Knb5Iex0FwPE8oGKR2VHHrERM1m-H45tCncZpDVvyRLzzeJfjrDwlYYXxn84vh2_q73LX6i6DXLz_vTsHeMkCR0n9LVhgwLoGYPZa6ie6gSnROzLQu6LmQVxgKORdN4J-1OpYKyKuZ0Tc-3f9D393QUdb28NjIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
گلرها بعد از تعطیلات فیفادی
🫨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108226" target="_blank">📅 09:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108225">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=X_XdjqePbymVEJn_IbXk0dQVodmdV9XueRywqBDI_l7PiHkeDzV-4up2ijFdmZJEiy6PnbHd1QywAtAk8hGo-5rTb7B1_r5JTkOI2AnC70927wQB4tACwZ4goYn02BQPeTfa2v3JopX6w_K9hS8K6BSWmkchj7lQSs6l0oxMqYBETRFKTjad14ynqCsXlUbPlzwDC0ryhIRYkQ-nII65MCsMEJvOztJh3tkqYo3BYPGMAx8igSoR-8f_XitRkQGFDch7TDzkNwFR_vN9muqSkObIMOX4nDVps93nIHZcVO6UOWSkan6fXzaBF2jixKDqStAA4p6KqvVn5kxjnjzhgoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=X_XdjqePbymVEJn_IbXk0dQVodmdV9XueRywqBDI_l7PiHkeDzV-4up2ijFdmZJEiy6PnbHd1QywAtAk8hGo-5rTb7B1_r5JTkOI2AnC70927wQB4tACwZ4goYn02BQPeTfa2v3JopX6w_K9hS8K6BSWmkchj7lQSs6l0oxMqYBETRFKTjad14ynqCsXlUbPlzwDC0ryhIRYkQ-nII65MCsMEJvOztJh3tkqYo3BYPGMAx8igSoR-8f_XitRkQGFDch7TDzkNwFR_vN9muqSkObIMOX4nDVps93nIHZcVO6UOWSkan6fXzaBF2jixKDqStAA4p6KqvVn5kxjnjzhgoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
حمله علی‌علیپور به میثاقی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/108225" target="_blank">📅 09:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108224">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=VD-x3cXh_I612NE0ObSd1_ceeCZiBYJYbzj9g3p4tXOKh9A_5h0ftVZr4xnyMGYL8I_yGFFkTmv-KG8P5N1TJsb12RshGAeYVi8QAyXdTESwdfFSc2EUT9uT5WRuvn3VLoixqW80nQrdvBVcnNUL53a5mVz9Uu6wMmTDHbJ3LiD5jUePRIplcSt4TQh38TAI9rF31JlmumJPP4qB6P4W1sI1VNcgp7YAXKkPgInJOFthXkjNg8hxig9j9wd7SLFc0OlAcQHYW36pjd0aHOq3_HOWt5Dz9WQf0OYlm08TS6QHpO2oJQmny58UHqAYaOHsOI6_WaB6gvE5vxSttma7TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=VD-x3cXh_I612NE0ObSd1_ceeCZiBYJYbzj9g3p4tXOKh9A_5h0ftVZr4xnyMGYL8I_yGFFkTmv-KG8P5N1TJsb12RshGAeYVi8QAyXdTESwdfFSc2EUT9uT5WRuvn3VLoixqW80nQrdvBVcnNUL53a5mVz9Uu6wMmTDHbJ3LiD5jUePRIplcSt4TQh38TAI9rF31JlmumJPP4qB6P4W1sI1VNcgp7YAXKkPgInJOFthXkjNg8hxig9j9wd7SLFc0OlAcQHYW36pjd0aHOq3_HOWt5Dz9WQf0OYlm08TS6QHpO2oJQmny58UHqAYaOHsOI6_WaB6gvE5vxSttma7TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میرسلیم: چه کسی گفته نفت ایران متعلق به مردم ایران است؟ نفت ایران مال مردم نیست و متعلق به خدا و پیامبر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/108224" target="_blank">📅 09:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108223">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=R8YmuO3oSqv5tEEaUsAlDeYGSyRCHQ-81eluFXB_b4SJbkek2MzbYKK5f9UP4C_NWD2SXjETYUJmYUJ7XgLLLux3w9aPANjYa0XjKxK2m_pTvYVR0-cd5O39IkJKE4w7kyaZHnh9JXRH4tvXDduRE3EZQE0eXMFXpEZ2j2jgNksAXKmhDsoOdnKND7z6JUMN1kmdXCClx7GN6LUx6be3sg51WT7jbPRwYHGCzfy2vl_lujSGicGcoivyJr6kkWx9O8q2Hc6ggU0dmmKc6SP83Ls-ZxJkqYpg5Nd5dSx3DgG752gTe6TzInCtnS-6xpNCoXqLayYHiSrTYSi1Gy_NnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=R8YmuO3oSqv5tEEaUsAlDeYGSyRCHQ-81eluFXB_b4SJbkek2MzbYKK5f9UP4C_NWD2SXjETYUJmYUJ7XgLLLux3w9aPANjYa0XjKxK2m_pTvYVR0-cd5O39IkJKE4w7kyaZHnh9JXRH4tvXDduRE3EZQE0eXMFXpEZ2j2jgNksAXKmhDsoOdnKND7z6JUMN1kmdXCClx7GN6LUx6be3sg51WT7jbPRwYHGCzfy2vl_lujSGicGcoivyJr6kkWx9O8q2Hc6ggU0dmmKc6SP83Ls-ZxJkqYpg5Nd5dSx3DgG752gTe6TzInCtnS-6xpNCoXqLayYHiSrTYSi1Gy_NnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی، در برنامه هت‌تریک با آنالیز بازی پرسپولیس-صنعت نفت آبادان گفت: «سه بازیکن نقش پررنگی در پیروزی پرسپولیس داشتند؛ محمدمهدی محبی، بیفوما و ارونوف. صنعت نفت توان رودررویی با پرسپولیس را نداشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/108223" target="_blank">📅 08:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108222">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=R5jhRL0Azq_RFX3-Vs6n7vrRvsEJlSEtUi3ySj7-A4_UmT4yVhcBWdMbGJ0UYEnCaBvbT-VB-rRm44Z5MefBeYRdX4NUb2xwFJKZAD5Iox-C39fAvKdndmG3PVkGwtqu9CmtJP7Q-BWmprzr-DfP1FwA2JC04sZ20rHnN5Ku4c7F2pk8gXNl10Uxg5NW4gOWFxjxxKRn9JGXW21RJXDlvhE2Cs8e1gBrcvAcJeYqlEvcxdXKwA1yc8yyhVamimfGNANkFKBXBfgDIzjaE5QNd0XztLXCxf6_lRZkBt6BbQ8f2zIIjqGXFVgdWSiFHr-z2Z-OeewdkacgvbVXnYB0oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=R5jhRL0Azq_RFX3-Vs6n7vrRvsEJlSEtUi3ySj7-A4_UmT4yVhcBWdMbGJ0UYEnCaBvbT-VB-rRm44Z5MefBeYRdX4NUb2xwFJKZAD5Iox-C39fAvKdndmG3PVkGwtqu9CmtJP7Q-BWmprzr-DfP1FwA2JC04sZ20rHnN5Ku4c7F2pk8gXNl10Uxg5NW4gOWFxjxxKRn9JGXW21RJXDlvhE2Cs8e1gBrcvAcJeYqlEvcxdXKwA1yc8yyhVamimfGNANkFKBXBfgDIzjaE5QNd0XztLXCxf6_lRZkBt6BbQ8f2zIIjqGXFVgdWSiFHr-z2Z-OeewdkacgvbVXnYB0oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی با آنالیز بازی تراکتور و استقلال گفت: «من بازی را به دو بخش مجزا تقسیم می‌کنم؛ نیمه اول به طور کامل در اختیار استقلال و نیمه دوم تراکتور بازی را در اختیار داشت؛ استقلال شانس آورد که بازی را نباخت. اما مساوی، شایسته هر دو تیم بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/108222" target="_blank">📅 08:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=EQJIkiYjYqBLaFnVmDaGpI5ZdD-Ud6C2EzYdrdN1JDmPljrvVkEgmZY-zbrLyDb13Baco2EmZJG413KG92t1GjBJ8b8B9qrDAnnA1-qkCk88vKeh2FhI29PNAYOTU4Yd8mQr3e8B4jfeNClw5apskaSH0PhpygrOu03jSeQRn77NqW8oB4SQJiq6v9TCMRebSAoBW3mGzEmZB3QgjQQIRFiFbnaVNwuXVGsgfT6EK-MXBfSQ8i6kDGlfpShzcU0phqUe3fwHw3D5d-3IVTNOt3fhVAKr36jDjFydIce85h_5Fz-KdNGHmvjkNKBddC0zORtquMIOq7_3gwTtSxd_yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=EQJIkiYjYqBLaFnVmDaGpI5ZdD-Ud6C2EzYdrdN1JDmPljrvVkEgmZY-zbrLyDb13Baco2EmZJG413KG92t1GjBJ8b8B9qrDAnnA1-qkCk88vKeh2FhI29PNAYOTU4Yd8mQr3e8B4jfeNClw5apskaSH0PhpygrOu03jSeQRn77NqW8oB4SQJiq6v9TCMRebSAoBW3mGzEmZB3QgjQQIRFiFbnaVNwuXVGsgfT6EK-MXBfSQ8i6kDGlfpShzcU0phqUe3fwHw3D5d-3IVTNOt3fhVAKr36jDjFydIce85h_5Fz-KdNGHmvjkNKBddC0zORtquMIOq7_3gwTtSxd_yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقام بیرو از حجت؟ دیس‌بک بعد از ۲۸ ماه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/108221" target="_blank">📅 08:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0blswb7V1w09FjVC0mtVcL5ucwVj-RWKEGlSCqsQ15zS46fppFht5TbqIvnQcyGjk5WA3BeH3QaBEVqUVOrdH_4PwrvP3vqdxNmVxcxDFYZ6q1FR9V9BnAnXduEQUUXBbEiQ3Jc5ndGTkCgKIBm09UXga9Dp1U6497DTNgVmOB-9Y9DIKrs2302rbCFdhooZJNoUA22EWSHaR5JvNVx3MTDcxXuKILWhxCgRnRSQY59FBevYfQmM9dbNlKlfkRr03HblIeENaoLhruPuOgUFt63q3ZKbt132cd1D4bnZyGtJSsGBFTijTXVd2EBOD3D31neCPzKjhSk3ZySsB-N2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
#اختصاصی_فوتبال‌180
؛
🔴
در گفتگویی کوتاه با مدیران پرسپولیس این باشگاه اعلام کرد که در نیم‌فصل هیچ قصدی برای مذاکره و جذب بشار رسن یا بازیکن خارجی دیگر ندارد چون ظرفیت بازیکنان خارجی این تیم پر است و محدودیت‌های نقل‌وانتقالاتی فصل‌جدید مانع از جذب نفرات دیگر خارجی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/108218" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7HYhoeFsMfC6XKz7fC27nCgX0yGzCc1mzPv7qgAb9iLaw2-iMXKLwmuNnmti19Zaad-PXswNIm4TE8z-mHA6hnjXltLaEUjSYkyp-IcD_5W37R2rmBmKQWWgXlQylB2fRIRWsE-bDsnC0ZLTiuNcWGVeBWNMG-5fAWkj3Ir7QkaUcMSyg7Uxpqw78tzhxVmbABxOI4Wbvbl6_y89w4Fl51MNqn1hIqaAu4o54PY1lcbjVpirV07I8jfEU5xU_LsfBN2_AdTvFCT8vlfZLb6fN_1O4dO36AB7F2YMkYVbrPWGLf0yL5hEO3WhM4L1zu-33YB0jMZusIV2f-O_PAoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
❌
🚨
وزارت امور خارجه آمریکا در توییتر: به هیچ دلیلی به ایران سفر نکنید. شهروندان آمریکایی باید همین حالا ایران را ترک کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/108217" target="_blank">📅 00:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF4puXQplhjrz7LszE-8BLEgy7N0OuPfITuHWLw2pvoqbPCMgTG_ILuw3IEGIwfyjy4jCdBiHq0Ky_iiTn7HvONw8VUBoMYpSSQJWLXu79WKD1gPmMnYDQ5cdjJEL5GmI8424Dg0UyVIStWuWmRlOD8_2g7vqtCgopLQJHNwWVclX4ot4Zyv92_Qd3pIwieR1nxXsuuRaA-pvOlpxAq8dbwea0obVrwYqKyQxhaqpSoxIetfA9mdizgUY2XRk_ngDNNZFL6SH40qpp-YHdCIz1aryrlQsALBSgCqmSZp9tGZU03qPa7Af9rE9at9c4S1-EzsN4_ohi1ZECzuEpHw1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🚨
ظاهراً سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکیش حق خروج از کشور رو نداره و حتی اگه بیرو با مدیران باشگاه به این اختلاف نمی‌خورد هم نمی‌تونست شاگردان نکونام رو در سفر به مسقط برای بازی با الشمال همراهی کنه مگه اینکه مشکل خروج از کشورش رو حل کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/108216" target="_blank">📅 00:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=kSfKH-h4-oiJ7x4WeGyKz76nsv3YF9eT4ZegNeX1sMgjss13NQ0RgyZbIR4ifyUIS874FYcbFPNWc2DnT_5HhvASorxKS97s4j64IAP70qj0CZEo4pfmXCJ_qFmzeQtv7EMGraRxa7uipoKlcRCd7ZH7Vd-gZuIcgqyAL_YFlYvQ52vyTnn5_9Odwe6coBPgK78xdrjwLYImRmDWB1hcxKSW6t1zA2lQb824VlFoznLNJGwQgNi3hhPHA8AAvLIVFxuoxpiTB55JlrQRLf4Ozqv2YyWsUF8EAhWCZ-9QffHZpUJxJIL1AdrVVfSqUpot0pWYKr7IgJ1LEu4YIa8wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=kSfKH-h4-oiJ7x4WeGyKz76nsv3YF9eT4ZegNeX1sMgjss13NQ0RgyZbIR4ifyUIS874FYcbFPNWc2DnT_5HhvASorxKS97s4j64IAP70qj0CZEo4pfmXCJ_qFmzeQtv7EMGraRxa7uipoKlcRCd7ZH7Vd-gZuIcgqyAL_YFlYvQ52vyTnn5_9Odwe6coBPgK78xdrjwLYImRmDWB1hcxKSW6t1zA2lQb824VlFoznLNJGwQgNi3hhPHA8AAvLIVFxuoxpiTB55JlrQRLf4Ozqv2YyWsUF8EAhWCZ-9QffHZpUJxJIL1AdrVVfSqUpot0pWYKr7IgJ1LEu4YIa8wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
آخرین وضعیت شکایت باشگاه ها از آسانی از زبان رئیس فدراسیون فوتبال: هر تیمی دلش میخواد میتونه به CAS شکایت کنه و مانعی نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/108215" target="_blank">📅 23:23 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
