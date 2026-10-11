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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 03:30:25</div>
<hr>

<div class="tg-post" id="msg-108317">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/Futball180TV/108317" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108316">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/Futball180TV/108316" target="_blank">📅 01:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108315">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Efxg--wUSExz0XfNXuQaNv3V8MiigM4UZ2AJ18gRmXdiY7JWaZlx991AlZd-YNHYqHdRKq9vYfF8_Qnq-QoQoQEZY9LGFga_M7zPHoPX7_Gn6M6AT6qPzCo1rMxJyQZhcMmRrmvdeI6Fri4xtz5a2Vdwp6pMKbz0FhW45lrvK_XduuLjjRZEi7drVtiVKMJyUBd6NQu2bmfEnvVDsDkT3FBAIAEqlvi8Y77YCr7yQLtN39MKZY4fT3fuhIqY29nXUfSLpiOMN1-7ynJF5HWaJI0vFQJyXke4kvuFMyQquFG1UdDNirVmzk9AXjx3iKHxRCWkMvnyJagwq6l1t3184w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
وینیسیوس با انتشار این استوری نوشت: همیشه تمامی صحنه‌هایی که کارت زرد و قرمز دارد متعلق به وینیسیوس است‌. چه رسوایی بزرگی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/Futball180TV/108315" target="_blank">📅 01:55 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108314">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWsNektcDE9XdJMkA71G3duZc4bPq5fE6b0Pqq4b7n4SHLbCeYd1xCv0j0U9KgI73bOh1czp5vU8Hos4ASsuUNdQbslR9znjGatgupPI5k5lYzOh4v_E_mRoyWwqDFDKfCdpXimWKq5NWVPBNi6C-A6zW62g9LRWgzd7qrBi3dW8N-rF6umMZqqjEzL5a8jEUDI9wTvXOwVOCEJ_wxpQIG9MSsponNZWl9HrZ5Z9autiStBnOqfENFHkqkgmEYLIcbNkLALwWukcTXY3wFtwxwovjwRqjvqZ1J6DX_HWDgnlwO5f9h_VRDoQ7mICQUOpj_Tg0HF6GDQPub_ECe2Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🟥
#رسمییییییی؛ طبق گزارش داور بازی امشب رئال، وینیسیوس بدلیل پرخاشگری و رفتار غیرورزشی از زمین اخراج شده و دوبازی بعدی رئال‌مادرید مقابل سویا و بارسلونا محروم خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/108314" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108313">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/108313" target="_blank">📅 01:47 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108310">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcXMkAKL2Itu0IBHwFArH94DpjkhwS0NTlh2f476sLHfmJH4oyu4mvIkjqRPHWRqi9l0kTSkIG2l9eIC26jQGAafTgj5h796BWveNo4vHP8B9wVeqv2ZndQCGHA0KXypiu0MOvIx-TpN8LhbP93WKTkdmprY-rXH2YkqqQd6fzkFaZywi14WaAMGgTjRZU6vq7VhDQunCTXZjsy5gBpuEN7rDM6rcpLZilokl9l3iGI9u1iHot6sN7JiuYTWeMa25iJ_VaIz34DDcV_Mt6Kfi62Pf6rsIK-Va7o5iMefiFHG3ajl5pbmgHqpB9TndQE5d5DsxQqKOr_nYjeRRoM5WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
🇪🇸
پست وینیسیوس در اینستاگرام
: من هنوز هم خوشحالم. می‌خواهم از هم‌تیمی‌هایم و هواداران رئال مادرید عذرخواهی کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/108310" target="_blank">📅 01:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108309">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVangJ-6_3b3-wQ-mZnSn4y7EncnN3Ge61su4Dchc9xRda3ibXmrRaHxHs3mcgS7RDqNwMAGu-JmXYN3nI0gJjDc1TPr6AtTmX0zbQ8XoSgK3v1chbg-PiZPbNv_gKsZWvAr81UM5-1MEYZelk7hNkHtBkVzg1RYduhIdHsEzE5vaG6JzuNhlabHjaGfYPfO6AoAYGCz2RSWhDoxO3CtAHI-jYc-DX3gi4wHzd4X6Kt_oLus5ky2n_o_-RcgyxUVwqIxHU4jcZXlVTQIhiaguFU4o_zrM4V_vEHF-B4Y7qmnsUYJ0MmCsnWBgnZ8FvUesMD4bZvghCjR0b9qOa7zkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
مورینیو بدلیل حواشی مربوط به وینیسیوس و احتمال غیبت در ال‌کلاسیکو در نشست خبری بعد از بازی حاضر نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/108309" target="_blank">📅 01:18 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108308">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH0MCfYU9jN6e-qf8WWE_4clrahu79_2ROjKayg98qTSEznerJCdTav6yA1ydbr2F4ry4jBUAcmGaWgUXt4IhV1_3POfywwJZ7dDCnQmr7o7drSyIu8QUVPB8AJ8-aJQx3dJDeMAuuFBCklFlxChXX32km4Gh6v90GaNiJ1QIDgzohr09QiS1Ir12DdB1kBPhwHjWM94QyO1o2vTbfg4Vb7bkmtKu8LEMJBwaQrBEkMQVNfrxlbfb7G3hPP1NMl10Eh2urjyUSxx71uo5ixd7pb6X4fpZsViRJszunL8rmgPVkOGd-qKdT7FwrcENM-JkYDJLO4VsnoUpWnEDSBhtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری رودریگو بازیکن رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/108308" target="_blank">📅 01:17 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108307">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
پایان بازی با برتری رئال‌مادرید مقابل ویارئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/Futball180TV/108307" target="_blank">📅 00:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108306">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/108306" target="_blank">📅 00:16 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108305">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108305" target="_blank">📅 00:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108304">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
بلند تر فریاد بزن نگررررررررریراااااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108304" target="_blank">📅 00:09 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108303">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vN5u2iFdeYI8bTGJogWLquRpR1CPByQnNXYhVkxgfB-0s8OBQ78FpXlckasMzIXhGv-tiwHuHBiQn4x7xwWYl68nEcAkqv4CRMjgbJAB9aBWStKk3wnmV15Hh8BbHBzuPgYzZ6C0S0hCV9XbppiBYmLEDXxJr9tAfC11qntGsSGIcVhI5q5Qd_lHCLuIF406Ts61rcB8d3bx6M3A_qBCPp9tsPaJWvXwvaljpn1P3oC3Gs2v2jymTEQ3NQuSU2C5prs2ST9c6QS4VQcBzrSmp6KR5gQyDE4LVz8hai7luxxY_H1otzWtiBniWCz2nNaXpC9ydUwvBZAPuPWkogGB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🇪🇸
گل وینیسیوس جونیور که بخاطر کشیدن موی بازیکن ویارئال مردود شد و بعدش هم از زمین مسابقه اخراج شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108303" target="_blank">📅 00:05 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108302">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108302" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108301">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0RMZ5B1cU7j-hXkjZv4pAdct5w-mqGiWMAIXl2LdzlSFsYXfENyFXJP81auBARwvsq58iKymgMXlZNTiCiGq5h7d32AyekJ6Y-DT08VRO7IzdFugY0oVTfcxBq61P7bf-PfF3VkusQCR1ykSyv_qJAZUFyP01cOyq8kIp_HjmwfG_GvLxDMLne91Mr_gDC5Pb8xD5vErpU3nPdtox0KkNq74y8nFfx-x8O6ZXsNR42f-IOC9tn_x6Q7IFSfuUHFrxtxCKQpqHlZ5RdbQ3DGK_c6ZhK-VNH3-MhI9iBVsCeM4G54kOWPoq14WrkiOwOE6xl5qp0vnKs41L3M9rMHTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممم بخاطر این صحنه اخراج شد
😐
😐
🚨</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108301" target="_blank">📅 00:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108300">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/108300" target="_blank">📅 00:02 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108299">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108299" target="_blank">📅 00:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108298">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بدل وینیسیوس گل زدددددددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/108298" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108297">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگللگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/108297" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108296">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/108296" target="_blank">📅 23:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108295">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نیمه‌اول بازی رئال‌مادرید بدون گل تموم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108295" target="_blank">📅 23:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108294">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
واکنش علیرضا خمسه به ویدئوی «خلوت کنید آقای خمسه هستن»: من پول بادیگارد ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108294" target="_blank">📅 22:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108293">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">برررریم سراغ بازی رئال‌مادرید و ویارئال</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108293" target="_blank">📅 22:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108292">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108292" target="_blank">📅 22:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108291">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zxl3XnwXuwRxib6kY45kTATYDu8SPSzSFdrPOQ8Cusyghj5QHqaKG1THfIE0vJRISCHOq1LSleIRR-W0686cHp02HAaxg4JvkF7IwYnzlC6-1wn5fc3GYiWh0K1sdMStKH93aPcOxpvMlekhFUqistLWYZu4xrAgQIQNn_oKIA-ZxZxiqKvuEwWvfADsCiqn8NzNJvyUHEP3KfUl9WPpI0INzaODJ7n-blHgeDjL8inQ4l02Su6aFLiTOdwWnEDNhD4_ThLO36v7fp2dROqzOUx47N_398oVKcWkCRNChBEmbQi_mioAwpXv3eMK-RDoIUYldhGbTgLmLZl5nvPctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
لیگ برتر انگلیس| منچستریونایتد از پس تاتنهامِ ١٠ نفره هم بر نیامد؛ مساوی که به درد هیچکدام از دو تیم نمی‌خورد
🔸
منچستریونایتد یک - تاتنهام یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108291" target="_blank">📅 21:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108290">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108290" target="_blank">📅 21:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108289">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کوندهههههه</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108289" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108288">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گلگلگلگگلگلگلگ سوم بارسلونا</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108288" target="_blank">📅 21:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108287">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dgss9-NYqjMYl1absTjh0r9zLIb4BRHPj2bk4NDgD7vn72cKwaXGxwY36Of7ixMxB7_TfeOvTK8cvRKecUkNw9N8jSFBPZn0QNVel8FlL3Q2GYZ65I9LUQTwGCQQ6EbE7JIznrVTbeUsW8iGOCJZvv21ABmVvjSjWAD5vIVkRDc7q7D3esjP9PnAZ9hgZapNIfRvMd__Zmtfgu3aAcaQRigfkLuu-4mzM5zwFStah9mMNs-lcaems3CMKtvmwpOOF4itAQht9AC1Nws82JbYnXjWsd-qIBfn7rUTdqj1azVBUUx96tYiM8dkwy3cll_g77zLOMwQClMfokjAx4Rlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل ویارئال؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108287" target="_blank">📅 21:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108285">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8kwp5HVRirLaxCNmDeRW9oS-s8B0pD4Y0EECCBarTh9VMoMK-GtsbXUJnT89W9JZ_89OEsTNn1x1jo2d1myCmq95oKC9NVAm5BThN5nv8hVj9OdAjS8dUk9OMXw74W6xBav416JBE11lQbUtQ72if44p6LM8x-db-4cEa1ZMPMYtqdH8rQJo0h_zY0nLeIa8t4kiV6s7ZBBw_wC2xsHMKi-jiagk-mGUcEwXvxrsB7C1K-DemSWKP7llq2uAXmHGjYqi7Whbf0Ne_U8qCQtu5LCbac2tsl6wq_dsc3QAcZNaWK6PJXR-8dmKWhG92RUB-VEGlTtgjFSt593tMg1Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇵🇹
فدراسیون فوتبال پرتغال از بازگشت رونالدو به تیم‌ملی در فیفادی نوامبر خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108285" target="_blank">📅 20:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108284">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108284" target="_blank">📅 20:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108283">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گابریل ژسووووووووووووس</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108283" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108282">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بارساااااا دومیووووو زدددددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108282" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108281">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلگلگگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108281" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108280">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=Ewqy9RoDywp4RFF-GSjNKXXr6IHGQMPKOer0xFE1H2kDz0tk20kPWOLtg6nFpXhLSIaSHjK7VA-vP8ZIiopO7aGAFLHFxBcV2B-kGv7E1wibWa-V4EGoY4u3CVh89-mFQJL7RFTRqIVnhpgyg6gcQ3TjryS7FvqUZnnG66JYMyhynX8O1agxt7S63SwZEIUCWFT11YYcyCQXHBqAoPlFKI_M3Wc-7wApBegpDdGqNMOcbiKBZntNoMfBpwEE-wn2Q1P5d0AaZK4Kyy2YuYrs5QT9quZO2bjrFxixueb46rX7x_inhYxh2uaz6oIvDuKlXMIOpPjT2r50sL3oZviZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9dcb84758.mp4?token=Ewqy9RoDywp4RFF-GSjNKXXr6IHGQMPKOer0xFE1H2kDz0tk20kPWOLtg6nFpXhLSIaSHjK7VA-vP8ZIiopO7aGAFLHFxBcV2B-kGv7E1wibWa-V4EGoY4u3CVh89-mFQJL7RFTRqIVnhpgyg6gcQ3TjryS7FvqUZnnG66JYMyhynX8O1agxt7S63SwZEIUCWFT11YYcyCQXHBqAoPlFKI_M3Wc-7wApBegpDdGqNMOcbiKBZntNoMfBpwEE-wn2Q1P5d0AaZK4Kyy2YuYrs5QT9quZO2bjrFxixueb46rX7x_inhYxh2uaz6oIvDuKlXMIOpPjT2r50sL3oZviZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
حجت احمدی: سیلی نبود، آقا ساکت بهم خسته نباشید گفت؛ پیشنهاد استقلال؟ خبری ندارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108280" target="_blank">📅 20:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108279">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108279" target="_blank">📅 20:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108278">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108278" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108277">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بارسلونا دقیقه ۲ گل زددددددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108277" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108276">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">گلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108276" target="_blank">📅 20:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108275">
<div class="tg-post-header">📌 پیام #61</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108275" target="_blank">📅 19:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108274">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی چلسی پنج - یک بورنموث
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108274" target="_blank">📅 19:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108273">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108273" target="_blank">📅 19:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108272">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108272" target="_blank">📅 19:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108271">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNT2hoZRKipvO2DmGHh8u7wwi8RFEUcFnj_21WR2vCtjAI0-ElxgChssYib00n6dSGVQtCaWnZEpY93gj1omd13Fg89PzEaJvJ9D2vuuFcbFcw_KTTQ6VxQCGNQFGubQ_B9C-Q_2wac06AWU8VNHp0Xmai1ZdlxI7SgWVtsWbZ2818V06f8umbxs14XXvfpgxQPdnxKdKlyARZ2fBqc6sP5Xc2_cPt0DcRZnxSoVHomqgt1hXzpXJbOv-fx5833KaHBzxkaSYD9I7YbdraFtw1gc2J6yRuYrg7vuiy4tu9UPyPykUnv5nEmdzBaUSOuXHR7MRsf7qCjNspcLfmSehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
پایان بازی هفته پنجم بوندسلیگا
⚽️
بايرن مونیخ 2 - 2 آگزبورگ
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108271" target="_blank">📅 19:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108270">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQNE5NBM94Z9luNhBeQrh9IZQlYqDit9mGWdILPOL-p7Lty0FZOOsA7PGWSJQ5VVf4nQ3tlGH42Dpox9S3B935M9nye-XWhFCE2gRa5x534jxFgrcoQJ9Ip6L-LP4V0p5KNJMhqdoTE3Pef3uZP1k6uzERbzrGbG5Ci9oVj66YJEqdH8XkdEuF5Kj9JM7oQ6vjxNadYz81avlsKvl1jzfXzdr-OdIIkxfoy4Jvmet7Rh2YZWnNcl_2lXaeMqOcbOimyxfL6V4Qe_9YlsjjbPl533WkSjZ-Dlb6ZgVV8QqPDZBoAZnvni7wMtNJdvlQpizCLXXJk4ctFyfuYCAEW6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108270" target="_blank">📅 18:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108268">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108268" target="_blank">📅 18:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108267">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWjVI8AGAlm9PIYXwO4oZlGjgdl-zVkJaqLlBaMcUbw6qhqyyE_xh2jrE4Y7mEW0yYz-iaaWiYxPHzUP64SZ3yTWIR_X9Fs9Yn6H4E9UbdhVg4aL1L-bb5yMzhJDyFxKF0vXf11hv6uK3KeVlNjFzIznb3L-u5tSVXK8jTscLj39lfq-VsDylrHjiM8TY4-V0WPdufAzBMpOkLygfhbcNvVPan9D_lc-4yiQqfmzjWwhocUZ3uzB0WdLAuPfztpp6p2Nv62AtGUi0Q8B3ejx2wnRwYIGwqnztKkshcX6YJ6yxWK0imfvvO8dryhMaX3XwDxeSQFpxbspdYtpuoFY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب بارسلونا مقابل ختافه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108267" target="_blank">📅 18:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108266">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pefL6TRlIQAkiZyaJVz4nizlKseXCK7W2Nu2erBOwIecdf1d-PuGXzFqHT9kYWhfmDWPY1y6EAYhWj6DgkL1QmxT1mTIWnG4qkrDI9OjGepqMfmB8csA7HAni7eYXe-58N0_X3gYguBDewg0Hwy79V_mg_lqeDpFVCkA1gcY5GUC4CxLPAb8M3w-LzjsQSt50Zibas0zkZOzLmEj1HY0uencBtx3KlOZsO82LYKo9FRgkexUgyOBAPU5Jjv53U05q_iN-WThOndA8lxNVsD5FxM6U7Az01igOGTWEWve83zoihalyADFbkxpae_Zwrd6Ny6UgKdQ3IYSuIrdvkVSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
با تصمیم محمدرضا زنوزی، علیرضا بیرانوند تا اطلاع ثانوی و پیش از سربازی خود در هتل تیم امید تراکتور مستقر خواهد شد و حق حضور در کنار تیم اصلی را نخواهد داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108266" target="_blank">📅 18:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108265">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108265" target="_blank">📅 18:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108264">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA292isKCBRkxuWgi8C9gioAriPYP4sr0uZX4NDlr4wTKsvSktcypGQYPv5CrIToiWBnHSAqMIhfDqG3mh7xwx9OXX8e-mhpIfs6KubNNau57bwbgVHCQQgfuvdhY5Tv0YCI_9oRE9nTH1Rl9OOI_hr3y-1dCoifdE3hjJ7WD6ExHxv-sP2JGrHzhqLojxsR15mHQ6BJDmUG_qRl4AU8ATs8Zi8qbEtiszoUKN7iLUqisqBTMdrnExBk6AMdGRi8mEupWwrp320k_v9hMxIeZcqDHQTfpAzi21N7OjEQ2nYmTqi0WFBJeyQIeq17N459oGajd9p_1TBkECTbNtUcbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های بارسا و رئال تا قبل الکلاسیکو
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108264" target="_blank">📅 18:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108263">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108263" target="_blank">📅 17:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108262">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108262" target="_blank">📅 17:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108261">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108261" target="_blank">📅 17:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108260">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108260" target="_blank">📅 17:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108259">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108259" target="_blank">📅 17:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108258">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
⚠️
‼️
‼️
⚠️
میرسلیم: مردم باید بنزین را لیتری ۲۵ هزار تومان بخرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108258" target="_blank">📅 17:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108257">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108257" target="_blank">📅 16:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108256">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1i1ZtP_zisU2cLjciNAJrhM02snpZd4edefjyxRGKfU6UsiosHLsx3K8TUJh1uElaTFTqwFaufabj-_3cAQvM93Y22qSl9fQBg2yYdTSIflOQnigTr78fsz9dH3jNI2KRgc66AHKTfNTiYJ9FOgvbIwPbfTCEYD0mKr_dLbk_1OmuAFOSK8fkgwsYv-M7fiIGaZv7mFbfDBKmddj4jiKfS8gvieLrn77GR6HpIpehKnpC3nx0yzkYlaoyPUzPO3gsFLxMZwcj_PfWSwiJoXMHCky5hCMPMx5IxGprVgsHWXdihXDsZC2ZJv3lOWZ6xyd4h7URTi17DfEQGMMQYjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل دوم آرسنال به لیدز توسط برونو گیمارش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108256" target="_blank">📅 16:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108255">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJ3D3NZ--49bhzqnrdaCTWKcyjNRZ1T4kQpZCBWOU00NBoONpRdl5rf2fvMLv2vmLooq6uxEDJx0GpzxKc9W7tXPPGN6WoBgFw5wRCSrrL6sxR0Hicc52I7vZfAUH-3ACZXRgpMC-yswoHgJripN_bLLmjIGipTnQlqVTOkeFCYoSYETNpRh8xrJYlAVZ2DgA7Ggnn9nnau20gUPrXn8CoAf9Er3wi-Yqt6fh-L05bopbsvznOuRX88lZM7w7qivy4GLzqrdDP7-992026imCuS16_o5efcEjb9UrEukHsKgbGl-WNeOfRvFUUwJ70-Lsh0NJkshgkb8-IrtOHyo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
کاروان استقلال لحظاتی‌پیش با پروازی مستقیم از تهران راهی دوحه شد. مدیران آبی‌ها در ساعات گذشته توانستند محاصره هوایی ایران را موقتا دور زده و مجوز مستقیم حضور در دوحه رو کسب کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108255" target="_blank">📅 16:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108254">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108254" target="_blank">📅 16:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108253">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108253" target="_blank">📅 16:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13447d981f.mp4?token=HGzWiFM3gn3S8lLX9TsCj5ifI_XeILpUF3C6Gl0C5OIje7bdZude4hu7WGfzAyr5vh5B1IazUoaiDN_JwKcDm4jNzDsr9P5DPlBSCuXeHUh368IBMytInI9wkpC-d-griOqmZ3qDZAaB1741Wqy9hkxWvyEH2N4aFDKV5osK7pnqDAiWnFHRD-q6O2EDEW8LOlAb4RF6ZI6U87FmVj5j_XfWIpNmghxfkPoJCFEVM-rw1bPRkwaKtYtjNX_fNS27fPQGjli4Hh--Ik11WebeVcO8yg4_527ZdP1kCTqqdRY_A4wN_HGEsKHHr6ZuW9Jlleh1lKA6uI22CCmTNasv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13447d981f.mp4?token=HGzWiFM3gn3S8lLX9TsCj5ifI_XeILpUF3C6Gl0C5OIje7bdZude4hu7WGfzAyr5vh5B1IazUoaiDN_JwKcDm4jNzDsr9P5DPlBSCuXeHUh368IBMytInI9wkpC-d-griOqmZ3qDZAaB1741Wqy9hkxWvyEH2N4aFDKV5osK7pnqDAiWnFHRD-q6O2EDEW8LOlAb4RF6ZI6U87FmVj5j_XfWIpNmghxfkPoJCFEVM-rw1bPRkwaKtYtjNX_fNS27fPQGjli4Hh--Ik11WebeVcO8yg4_527ZdP1kCTqqdRY_A4wN_HGEsKHHr6ZuW9Jlleh1lKA6uI22CCmTNasv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول لیدزیونایتد یونایتد به آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108252" target="_blank">📅 16:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To5uweVgEM0Be-q-itRT6iTlRIJOCZWfLTfnybf32RxdCvQG0DzhGTutknylBW47FTAfjxCHAcrzx0cxF0jSnqDqRGmfqjEIglihdNQrQLOKp7Cge97JCvbsd7bGKRHAAdZGcAcF3peM1veMVUFZ7dcr18AMixhcmsiFpxz_K0j5bdFMOULJnsYaCViIzpvZdlpUUyG0nDqDpNpEQsH4djGfOg_fUK96fzPrJ04M6uPW5WFaFR7P5HwB3jIyG5mjLTQACgBbS2tOhIMyYTwlXnxh7HFKBlAzPh0zTz1OQbjxfAWxn4x_Zx5-etx3aQkbolVvj22YBfLP99dZIVCFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
در فاصله دو روز مانده به بازی استقلال و الغرافه قطر، هواداران پرسپولیس درحال کامنت گذاری زیر پیج این تیم قطری درباره یاسر‌آسانی هستند. این درحالیست که آسانی بدلیل مصدومیت مقابل الغرافه به میدان نخواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108251" target="_blank">📅 16:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgnFNFtYHEkS0gqkK1AqD8cZc1aFfgaA0sdTv4lxj_YJ4W3FfpPzGaiZOTjcoB4eTvUm38uJqfr8D8PBAAGZ9VleizsH1HRDg8yvll-P618y0CRIHZrfLHk9ebstU8V-LwjqB4LGtr2ygFKkDz0KUCtiZeJouQfhVNMq_9OM9bzvo7CfrfZDIr4lxaVLhMTIu24QRQXKhp1qAZOp2-noHzmEwUD37JzmZJlMOebBnP5be_EjgpyKWxew7dfAWiSl44zm2PPVw-YCpnI8B46FKovUVKABzte0Zl6A1CAmhjFT8P3O9ZLf2X9v-4AYVOphoub81uWiWIXQtXOIGFvHNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇩🇪
شماتیک ترکیب بایرن‌مونیخ مقابل آکزبورگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108250" target="_blank">📅 16:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108249">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85108132e1.mp4?token=TeiCTfdApZ-_EOxBunl2PQEXrX_-Kq8LMSpK1UY6Ujg6yvcAFXCBfzQzF5gZ6Vj1seG7mhex46HC2NcXRXtPDPNjy68y5pN8UT70u9cueLbj1SkNo_T20UL9Eob97zPvJ_17Pw3S6nqjsibD00v-_lA4vF14uwMI7k_SWIITYgrYvnl4flmKB1ae9W1vXtVaG8C20aIVeCcgYUz9LdKafiHiiOdDT4kzOMuOJh8GgJ8udNNAcX8KV9YvA73TJQP9hy6AVldnne7LgvaTyc_3HpTFKSbsPycocZn7QoYkkOkq6LMlmywHv_MqJYhuGRy5LXtvpuTXW5-N5snZfB3QljzFPQuEPA_AwsmOjzx5XvJ8RnQmncByF6Nt0DztQFdCrxin318bz4wbnFD-afE-Z8lz7-2KoWrddD-UXEm8pQ1Go88a0-HA6LTW5h8rJind3Pe7C-23GUrsRtqLcwipXfPaCXxKNQnerwhHeDbchlM7l-tVKkBO1L9R-ayQqUP8VzgCtkCmwxoN2OZpIIIVZnIBQ06sr12DYEve4GeY6dA-SFrPaT5rriO1YYdf_qlRNkYvoaRXNa9-A7UIXKKYD_gOLqpsFgE8voiSAr56w4UOsN8ZxtXXG9sp00mdd9zJAVcrqOZ6Im4moalkAzJA3wwB0NGFLuBQtLS_tkEsSA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85108132e1.mp4?token=TeiCTfdApZ-_EOxBunl2PQEXrX_-Kq8LMSpK1UY6Ujg6yvcAFXCBfzQzF5gZ6Vj1seG7mhex46HC2NcXRXtPDPNjy68y5pN8UT70u9cueLbj1SkNo_T20UL9Eob97zPvJ_17Pw3S6nqjsibD00v-_lA4vF14uwMI7k_SWIITYgrYvnl4flmKB1ae9W1vXtVaG8C20aIVeCcgYUz9LdKafiHiiOdDT4kzOMuOJh8GgJ8udNNAcX8KV9YvA73TJQP9hy6AVldnne7LgvaTyc_3HpTFKSbsPycocZn7QoYkkOkq6LMlmywHv_MqJYhuGRy5LXtvpuTXW5-N5snZfB3QljzFPQuEPA_AwsmOjzx5XvJ8RnQmncByF6Nt0DztQFdCrxin318bz4wbnFD-afE-Z8lz7-2KoWrddD-UXEm8pQ1Go88a0-HA6LTW5h8rJind3Pe7C-23GUrsRtqLcwipXfPaCXxKNQnerwhHeDbchlM7l-tVKkBO1L9R-ayQqUP8VzgCtkCmwxoN2OZpIIIVZnIBQ06sr12DYEve4GeY6dA-SFrPaT5rriO1YYdf_qlRNkYvoaRXNa9-A7UIXKKYD_gOLqpsFgE8voiSAr56w4UOsN8ZxtXXG9sp00mdd9zJAVcrqOZ6Im4moalkAzJA3wwB0NGFLuBQtLS_tkEsSA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ماجرای خرید تراکتور توسط زنوزی به زبان نماینده مجلس سابق(عای هیمتی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108249" target="_blank">📅 16:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108248">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4ro8j-OIy7vQ-EVLgF4tbnfZdV1mY_Yx_mbRWQ3eqw5koYMwU8Bn3HqciNbexmLPElQ_SPE2UiS8lwmI-icBIoizSeF2X6EjWM-XNSBHF8tdfxF4eR3-dk8oJz444AH8TUcWscMQItGOuKTwlbS5aK-VpjTU07Zu8xZQP2UPpG6mwfCDyFMcCm_MU4zPwG11-Ply8FbL9YqHdwQI18ms-XUlSxmlj2Y_xQbhO12GsDYKqszHuTTcBHFjy4FdC6eVnC3kzzL9HcKiWwFFjYNFycBTLicPN5-7-dzxZwxEyLzBln-pxqvs9OhfCERt7PfDspi-cJAMxVx7kbcf-GKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108248" target="_blank">📅 15:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108247">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajBRNdp8pwkGwykNxvEuWcLVlNHSICbFus-VEwFE4TwZ8Z7ELLlxzwXvIHcsmZEJB6nFLW3sbSK0583m1jf0CoL7ktdrfdKo7xbnoRFPN4bNaSV7n4Hv1H6MzKS8rS70kNojufbFobpyDW5d7zTLd3o1iQHyzxO0p-QoIbD8-jknsxv_S9fESahRn6F6_NZ8k6U1IE9iw19sy3SCcdBLTGGTZAkUsKcVInFaiG-cc2CjKp0pB68Lb2X54tUCQ_I-D2wZiJvB4v2R6X94RvpS3iuREf3JJvzm_trCMdup7g5Dc7oUUaK_WUz9OAnnp2OSSoGh724tyARGzDkNmS1tCFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d024a83d11.mp4?token=G-PDiRlGZHInxlK-S1hcs9SAwyH612MpyH1yHM_Z1aFLS3j9TVcMsmwPvg9OhRKaZNx6R_SCORW30I3ldE1t5wgmt3ZVZ0BSfSvPqiiMhm65-Cs4HkaWV3RTKr_DNc_oEaA2nyb8ypbwFu6CCvaDFvj9rnu2vVBt3jtlnTAjs08e38CMcmd4luBa85bOCs6_Mq_CdwIq1TFh4Q5xlrhJ5S9uVxRqUFtXhU8WzDn-JTEh-7Klr-HQjXKclJamURsSfWbQlpvs0i5vBbpCR_fkXR6AymIGB9y7c0K7sCvYfkywtEctSMmx1jdZ1J308fb4ZvAFVyW3kpNieI0CLMnajBRNdp8pwkGwykNxvEuWcLVlNHSICbFus-VEwFE4TwZ8Z7ELLlxzwXvIHcsmZEJB6nFLW3sbSK0583m1jf0CoL7ktdrfdKo7xbnoRFPN4bNaSV7n4Hv1H6MzKS8rS70kNojufbFobpyDW5d7zTLd3o1iQHyzxO0p-QoIbD8-jknsxv_S9fESahRn6F6_NZ8k6U1IE9iw19sy3SCcdBLTGGTZAkUsKcVInFaiG-cc2CjKp0pB68Lb2X54tUCQ_I-D2wZiJvB4v2R6X94RvpS3iuREf3JJvzm_trCMdup7g5Dc7oUUaK_WUz9OAnnp2OSSoGh724tyARGzDkNmS1tCFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🚨
‼️
عزیزی در فرودگاه بغداد: فقط ۲ تا سگ دنبال مهدی شیری و اعضای تیم افتاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108247" target="_blank">📅 15:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108246">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=HvSnlze2Wzg9nXi1gy1GQbhPL9jf-9pPOXi5bNlpJlG-2mU3_CLUhtRBNdZkDoTOcLT4kxx1VkpoSpYdR0vOjbnzwanpLymOGS1ZRjSxUJBko93Lzt2FoOmlaoWz8JiEKAoMhZ8E2omv9y5AFgoUKgzQu_2GaqdYzn8MovC_rJ08nbtREoi6okWvMmKIeg5RT58M8I2nzX8NcyF4Wv4VzrUzmr-rFS5p8qJJPE4XTzR6I4kH7KNsKGeNL4bCaxWaiUFOUPJ7qSZ28kBCTaflV21CdbpVU1aT3gIpF1DLsHEMZcl5RhiquCjLrtcFlM_R4yNTgyGdasTaoDfS7B4GeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ba40b7cc.mp4?token=HvSnlze2Wzg9nXi1gy1GQbhPL9jf-9pPOXi5bNlpJlG-2mU3_CLUhtRBNdZkDoTOcLT4kxx1VkpoSpYdR0vOjbnzwanpLymOGS1ZRjSxUJBko93Lzt2FoOmlaoWz8JiEKAoMhZ8E2omv9y5AFgoUKgzQu_2GaqdYzn8MovC_rJ08nbtREoi6okWvMmKIeg5RT58M8I2nzX8NcyF4Wv4VzrUzmr-rFS5p8qJJPE4XTzR6I4kH7KNsKGeNL4bCaxWaiUFOUPJ7qSZ28kBCTaflV21CdbpVU1aT3gIpF1DLsHEMZcl5RhiquCjLrtcFlM_R4yNTgyGdasTaoDfS7B4GeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد مدت‌ها فردوسی پور و میثاقی رودرو شدن
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108246" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108245">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=vxFLP86rSvCECBC8E4X2h1ky5T0F-QXApTBfhtQ0663W-8nbktR9306FA-zMUYY3Sulk8Ndl_p_02bdfP4oeY4YtUDu8NubZL1RfloiLNgqIDuveOQo-Z7MmcW3rFZd1qHK7DVpsQiz1xpyu_JLYaNiV0w3nOLJmZhOzMH-LEnDZLYDpWQ0Q2zV4YT3DmadffyRq_HNY6hyiHmWYu4UMmvnEbtvR5FvgH-itsYacXJyyGlSZah5uqjVfxKgDe4n2n0vieTtNVKPSShI2Pttw-VTEvlULSmY1Wjk9E1Tm_sln9FJvKz8IjJK143tFuB-g1yY3ApfJ0rqE6ZcHiIw9EHj8zqpdRLUqW0eJmnRr1ooy_iTCUjLqlc6udu7ziN9c2vYdbrzaMSAnJvmFdM7w9U_wmdksohLrP13WPW38twVtzdVQO3U_AHZTDTrujrDqiBYK4eWREUj2QRIl7InxKoOMFgDtYbShJH7ZCLB1OuLbmCaKPR2Om0b5TjmuPzpEM078MsC1VHBquMmml6eh-DKh_W0lrwPEG7fHWfTKT9K51xxtEqo2i_QkxnLJQumHhv1kO4UNqFMQyyg4jEI3U2okk47pjdomqEvxINYE5OhnfTkifz3_jdcDgp5Q4WkWpGJtJO9_aTHRr45hsrpx2b8BfTGX11qEmoyHg3wRccM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a5e7db4ee.mp4?token=vxFLP86rSvCECBC8E4X2h1ky5T0F-QXApTBfhtQ0663W-8nbktR9306FA-zMUYY3Sulk8Ndl_p_02bdfP4oeY4YtUDu8NubZL1RfloiLNgqIDuveOQo-Z7MmcW3rFZd1qHK7DVpsQiz1xpyu_JLYaNiV0w3nOLJmZhOzMH-LEnDZLYDpWQ0Q2zV4YT3DmadffyRq_HNY6hyiHmWYu4UMmvnEbtvR5FvgH-itsYacXJyyGlSZah5uqjVfxKgDe4n2n0vieTtNVKPSShI2Pttw-VTEvlULSmY1Wjk9E1Tm_sln9FJvKz8IjJK143tFuB-g1yY3ApfJ0rqE6ZcHiIw9EHj8zqpdRLUqW0eJmnRr1ooy_iTCUjLqlc6udu7ziN9c2vYdbrzaMSAnJvmFdM7w9U_wmdksohLrP13WPW38twVtzdVQO3U_AHZTDTrujrDqiBYK4eWREUj2QRIl7InxKoOMFgDtYbShJH7ZCLB1OuLbmCaKPR2Om0b5TjmuPzpEM078MsC1VHBquMmml6eh-DKh_W0lrwPEG7fHWfTKT9K51xxtEqo2i_QkxnLJQumHhv1kO4UNqFMQyyg4jEI3U2okk47pjdomqEvxINYE5OhnfTkifz3_jdcDgp5Q4WkWpGJtJO9_aTHRr45hsrpx2b8BfTGX11qEmoyHg3wRccM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
آنالیز ساختار دفاعی استقلال در این‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108245" target="_blank">📅 14:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108244">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bed940014.mp4?token=C6TtX4_ohE6mXa1-N792ut2L2Uvpm9F5Jv7JwEimKYdkf84l9aNh2oHH4OXgWxT4_uJmpFW4-wKahMcdHsdDE62p99GziSKBlfuR6094Go0PVmTU3lygG9TN6l4G7KZ1OPu_Pxdy_oDby6WwzH4-Q4VrSmI9rS228rnqMOl7K-t9sGmsdFf2PvinZZuFWT6Z8yYmhOncjTzAHYWOGJ9_ZaC5XQownsklehQlOZ7aD83cnSNEla3rxsZTfb743ro24MwG_oiQH0onVVca5a_58qBbSBTAZqhOvcg1OM7_ksi0KrgNPv0_BXy5ikK9Q1DVeunx-SUkDAVSqDT9UX_6HKsx1jjQQWePwhvQRj5_iwIPbnHVpzsoveuwGJ33-n8aL2vpY1RmSuJQU1nBUh6OJVz7rI7-xgOEqR2yrpnZYJ1bsyvskZliWIF-7XJGFvNSQguSglpmPeHa2XPnO9KMiZa_CZLAf7HHYPRkvvTrLhc3BBL96CfBxm7m9NyTjuGtjVhtf3UKdN5WcKG_WAomlCECFzeb51gcbKAPVWTSIXgJT9d5riwaxFp_aVFA9cNh6zFetK39h5z6kJgEJ0OV-UIhGNFhJnefm2GFPmnepzC9MhVqcGdM2AER2c-GmqM21x4PBspS25BMh_O3zr2IpEkmPQ-MrrEBnFwyJeonwag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bed940014.mp4?token=C6TtX4_ohE6mXa1-N792ut2L2Uvpm9F5Jv7JwEimKYdkf84l9aNh2oHH4OXgWxT4_uJmpFW4-wKahMcdHsdDE62p99GziSKBlfuR6094Go0PVmTU3lygG9TN6l4G7KZ1OPu_Pxdy_oDby6WwzH4-Q4VrSmI9rS228rnqMOl7K-t9sGmsdFf2PvinZZuFWT6Z8yYmhOncjTzAHYWOGJ9_ZaC5XQownsklehQlOZ7aD83cnSNEla3rxsZTfb743ro24MwG_oiQH0onVVca5a_58qBbSBTAZqhOvcg1OM7_ksi0KrgNPv0_BXy5ikK9Q1DVeunx-SUkDAVSqDT9UX_6HKsx1jjQQWePwhvQRj5_iwIPbnHVpzsoveuwGJ33-n8aL2vpY1RmSuJQU1nBUh6OJVz7rI7-xgOEqR2yrpnZYJ1bsyvskZliWIF-7XJGFvNSQguSglpmPeHa2XPnO9KMiZa_CZLAf7HHYPRkvvTrLhc3BBL96CfBxm7m9NyTjuGtjVhtf3UKdN5WcKG_WAomlCECFzeb51gcbKAPVWTSIXgJT9d5riwaxFp_aVFA9cNh6zFetK39h5z6kJgEJ0OV-UIhGNFhJnefm2GFPmnepzC9MhVqcGdM2AER2c-GmqM21x4PBspS25BMh_O3zr2IpEkmPQ-MrrEBnFwyJeonwag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
على تاجرنيا رئیس هیئت‌مدیره استقلال: از فحاشى هواداران به مادرم خيلى ناراحتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108244" target="_blank">📅 14:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108243">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=V6Y-WR9lcyN77PjVPZ3-NobaixMD62GSDnDdo7bkY7fQMaiLOeQbdk6udMrLgAGDvIiq7JTOfDd6kop9pW_7vbzMOEBxPjzSAX6ky0iJ3NyMgtYdeU3G4enSA9rTRtmtWVjrjXvANFLL_HHuEZSoDd0lw2WOR3T13dVzCqMB6dBlAAWEJCrv07Vi7no0BRvT9Ccm-HbXPjXbnFz_btb5aAdA6mc5Om3NTu1zjHk5aeQ_NvrpJxIPArJ9jejLOoyIntjgnaYyEv_r23-WvkNu3rmcTnSoM_SvnJifH3IO8F5tqSUGapL7ZTUlSB1CfImAoQ4faHi60O7KG7MWHvzOzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879a0a76f5.mp4?token=V6Y-WR9lcyN77PjVPZ3-NobaixMD62GSDnDdo7bkY7fQMaiLOeQbdk6udMrLgAGDvIiq7JTOfDd6kop9pW_7vbzMOEBxPjzSAX6ky0iJ3NyMgtYdeU3G4enSA9rTRtmtWVjrjXvANFLL_HHuEZSoDd0lw2WOR3T13dVzCqMB6dBlAAWEJCrv07Vi7no0BRvT9Ccm-HbXPjXbnFz_btb5aAdA6mc5Om3NTu1zjHk5aeQ_NvrpJxIPArJ9jejLOoyIntjgnaYyEv_r23-WvkNu3rmcTnSoM_SvnJifH3IO8F5tqSUGapL7ZTUlSB1CfImAoQ4faHi60O7KG7MWHvzOzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر چالش را پر قدرت ادامه می‌دهد
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108243" target="_blank">📅 14:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108242">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s60T-MIiDLPdR0ni45J2ChAeOxKpCciZ8LvrEjROvL8mnru-8vxXdf1_BEXs4E8Ciiz90RJqyvRTEHiS_foMPIOI9gLS0tqtunQqmhiHtwMAwCm7NWlvzXiUj_vhuUaqqIpCzBUPVKzOZnOT-krKaVHOXbVtcv2gDKjsifG7RjM5KdzgEPBe_X2KEX8ppWCjujoaCaUXuLJz6B17IKhsdvfSWsrKXDgmhA-S04Lpo-MCP4HaCuEVsfXs3wFz0G8rrNc8pL9bvn4rwBQrIFcbgQvq-PRsAO39V3QsDf4jZmEOJo_PSLmj0EaisRUbbqLx1vaFmmXCC0dzkxGxhYZs7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
لیست بارسلونا برای بازی با ختافه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108242" target="_blank">📅 13:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108241">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPIGgXlNCThkIJZTgYJOGS90CBrC5bIF4Qc_zcC5D9f60ROxZN9ZIj3whPztSavi7W3dAjbfgixJ_3qSYGmOkrw7TY-3Ywz-xbl5HHqlWpnGn7Y5_WG-UgIBQcCM0Bl115Nl9xXpUgWNydTSut4ACX5fBWyRIvljinjlwaQjZbyglojwqSynUcu1gjaVsxUnMJSYdcfGHiKDwXrnRCIvnYHwNv40G_h6r51AwLoK_ABvkkr_62y3-9YAeCJIywRKsp2BcCD7ejZrHmYWRvvLd_rOBV0nJmW59qZlo0T9QRJCl8kQ06qJWWdkS7Q8_Zw_OKNulgqyiCDlGDKqRd-Dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب آرسنال برای بازی مقابل لیدز؛ ساعت ۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108241" target="_blank">📅 13:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108240">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCkmzNwy8rsd0ilpairF7DOYmjPOt9-c4RBAFaOAbLRrhW-mW7W8ipkWQRuqBKNrUMnUcIX4FvjQyHi8g0sJjUeh243cu7TSjXWrmrMVJjhqveeIgIAFX6RcePrcRuXUuOG0wtx7k7A1LXk9KxAALnct2WuUsRcYGyVYc1FuYT6pXY5XUxL0vyKrA9jOYjXb5G9gZsvkgY9os5OLYkDOTBB-SjO37-l9YWo7qsViFhOO-jwE_-H2SBv5BHnZnWlAZnRXIItnKCxiYQHB-Xo0eXl2qbg5anPM0GYxWbbRLQvp51vxL4UA3HUTlOQ4sDDUg-jRDpn8dynQ8VZMZdxj0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108240" target="_blank">📅 13:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108239">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=BFHba7IhGOJmLO_CnBBv7icFAlBLCE_tDS5sJoyKBLiimqOwkUMTgOYxJD0187hOk0wroQBTHI_cAo5HYVqnW2lNBz68pnx1hSMlu5_3FYEJGe0c5rc7GwuRSVllOUBx3HJWkHtl2eOdnTABgobc3vugR5-BZg-XXj02EAshpkZoJzFXWQcx2HijpwZd2ey6ROkMu0UWwbVCT9WbpZyk14mFCvHtDWfoYgoVNNOWeHV8Auwy_9fLhQbaQhDp0bngLB36v8OUj5a0Jfh7LURpBV8punBHKtoF2SoekmRS6HpqAiA7x_bUCwmrHQyHU1-AkYHD07iaDo07WB-M3acLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90ee39992.mp4?token=BFHba7IhGOJmLO_CnBBv7icFAlBLCE_tDS5sJoyKBLiimqOwkUMTgOYxJD0187hOk0wroQBTHI_cAo5HYVqnW2lNBz68pnx1hSMlu5_3FYEJGe0c5rc7GwuRSVllOUBx3HJWkHtl2eOdnTABgobc3vugR5-BZg-XXj02EAshpkZoJzFXWQcx2HijpwZd2ey6ROkMu0UWwbVCT9WbpZyk14mFCvHtDWfoYgoVNNOWeHV8Auwy_9fLhQbaQhDp0bngLB36v8OUj5a0Jfh7LURpBV8punBHKtoF2SoekmRS6HpqAiA7x_bUCwmrHQyHU1-AkYHD07iaDo07WB-M3acLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
باهنر: ایرانی که صداوسیما نشان می‌دهد کجاست که ما به آن پناهنده شویم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108239" target="_blank">📅 13:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108238">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8krM9isXK5xqZU-IT7SeZI5vMG1ead6avjc1iNI6x10w3_Djgrzl9Ye7069ZFkCvoJ-CO1yAxwNkwRzz2CjPbv3frJNe7svE9DRC-C6TSG53UjPdOBM8VUuq4iQW7_GpzuM-b4aHzARk2fl47P_v_SfPkPVzuS8MysHMjiR3F3cfLTm6JFVWTiSRKvaRIwCD1VXYg6hLcpJ7VPJ2OsPpv_TgaBWV1pLDlSnxB9kCQY9A2KWFvClwWGt-bY3fooH3g9OBuNuWqnuK9vJzUkF5-DNxemMRAXa7DYcb-V9Qs_oIy0iZMZC-ACUrgFEXXzfdmyNmx58ICpqpzlUKhYJzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد کول‌پالمر با چلسی تا سال 2034 میلادی تمدید شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108238" target="_blank">📅 13:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108237">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=Eu4fCXSJieXuiFTdl044cqodWHLsl6XzpM07dbqadfGBi5lA6WNjv-5qYM2-NAvh5UwB3-6qcEpyxPvzXpcaj43b_edIb_dmNpW-0yHT9t9vrypERsMnEriILo4HztzCe1e0iXpqsx9_yO45vZFUxoMbylaDRWQx4WCre-wHB7Er-ulbr7iYnqpCpeRLgQCo91BFkRX1APspZUTYAzIB_FibY9Y56w4_Ovyah9GvAhEZnntVoZZ7j6uvuXwPXns8WbtDM94Ir7GRG6H_BWJK-ffGjP9y5LA_G7gVlLcFSnsdiettQRViuez1CkxKpy57mXFblXwwbg4BbKW_z8HyUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3554e4463e.mp4?token=Eu4fCXSJieXuiFTdl044cqodWHLsl6XzpM07dbqadfGBi5lA6WNjv-5qYM2-NAvh5UwB3-6qcEpyxPvzXpcaj43b_edIb_dmNpW-0yHT9t9vrypERsMnEriILo4HztzCe1e0iXpqsx9_yO45vZFUxoMbylaDRWQx4WCre-wHB7Er-ulbr7iYnqpCpeRLgQCo91BFkRX1APspZUTYAzIB_FibY9Y56w4_Ovyah9GvAhEZnntVoZZ7j6uvuXwPXns8WbtDM94Ir7GRG6H_BWJK-ffGjP9y5LA_G7gVlLcFSnsdiettQRViuez1CkxKpy57mXFblXwwbg4BbKW_z8HyUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله جدید هادی‌چوپان به منتقدانش در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108237" target="_blank">📅 13:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108236">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=ASXMFHTn-u3RGanN_iYs5NFaOiZMZ2ry-p_S5erYGPYxLao1AfWc7pQPMz-vR7zuVYNDPxFuLxuWrdg7iZV__qaH6mM-FAxtIEcaT3H7vJp9E9jwOCiEYULDiKgP0ITxeLKzrBhI2I6W7hw3Ip-UFq-x_ktViQ9wIqzDMv2m7HbyW07aV3G0PTJQZ7pCq78hg95_4wtoQN2j8Xaj_kqZRA7OICrxjWyJTSGtO6bFsaXfVsTj6qA07tVA9xmETj1y5DJ5bDfALSrJ_JiC5CcWQvzQvCOHd6yazOqjU1RHUPaxnSZzWtFOoSogHtLaaZrjbi0GFAvmdRaYwxH7EuKlvR4AFgoJJ5z-vX6SgR0tSerhgqWsJ7VA0LzwlYYnqUDd5-OZKAkti9IbpACcMbcAoomAvhElMpDkFmZIqznmMFe4pBmZqrVwozf_NxYdkxUoGdHAGUz2DPzdoJ8iab1gSJwKxj5UrVqHgeR1_ccTCI8yPEgtPMbumnmrYMLaoCRZzBCD7opIUacLUCQgYNePdD3SqK9oerdb9TQsZcuINl7bmCwrw_i9bvn2EZYL72lT4LQZdRUr7ZaR_vvIieYVb80BKAhkDiUCJAdtfPK60yLgG_6cz4seX9pTwCD2PjUUHs5mZ9ywjLE78qE11Nz7K865mdLGGWA4iVM5X79YvUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f9b3658c.mp4?token=ASXMFHTn-u3RGanN_iYs5NFaOiZMZ2ry-p_S5erYGPYxLao1AfWc7pQPMz-vR7zuVYNDPxFuLxuWrdg7iZV__qaH6mM-FAxtIEcaT3H7vJp9E9jwOCiEYULDiKgP0ITxeLKzrBhI2I6W7hw3Ip-UFq-x_ktViQ9wIqzDMv2m7HbyW07aV3G0PTJQZ7pCq78hg95_4wtoQN2j8Xaj_kqZRA7OICrxjWyJTSGtO6bFsaXfVsTj6qA07tVA9xmETj1y5DJ5bDfALSrJ_JiC5CcWQvzQvCOHd6yazOqjU1RHUPaxnSZzWtFOoSogHtLaaZrjbi0GFAvmdRaYwxH7EuKlvR4AFgoJJ5z-vX6SgR0tSerhgqWsJ7VA0LzwlYYnqUDd5-OZKAkti9IbpACcMbcAoomAvhElMpDkFmZIqznmMFe4pBmZqrVwozf_NxYdkxUoGdHAGUz2DPzdoJ8iab1gSJwKxj5UrVqHgeR1_ccTCI8yPEgtPMbumnmrYMLaoCRZzBCD7opIUacLUCQgYNePdD3SqK9oerdb9TQsZcuINl7bmCwrw_i9bvn2EZYL72lT4LQZdRUr7ZaR_vvIieYVb80BKAhkDiUCJAdtfPK60yLgG_6cz4seX9pTwCD2PjUUHs5mZ9ywjLE78qE11Nz7K865mdLGGWA4iVM5X79YvUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز دیدنی از سبک پرس فوق‌العاده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108236" target="_blank">📅 12:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108235">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=TEXMGNUuA2osp2ZFA6aBDq5ZxK0U02qBsL1Mk2RzEtR1dZ3wZiTMxAv-xyobBte1nTFhBh9hsQ-_4RYBe4gbyecsGimqYcnf7TzXkCTcOyh59auZkhkVmAPLEBQzS8hZWSH4T4vpU39lzRe3w01Qwfcie2EqsSb4UWgRZbEwiDTHAOpx7g5YEouNSBIbTapsuaSUOhT_0gG8ITc4la6ks330PbuP28okdJMctNcNFFfHMqFskZBVcQcAVsWChFM7C0fLLhHVPKK3410L20o29GL_lAKEO4RRIMnRj1MGWH1fIhpe-_jMOpCC3iB_a9CO92Y_8Pmcvj_0pTvcM2iXNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ae47b4ef9.mp4?token=TEXMGNUuA2osp2ZFA6aBDq5ZxK0U02qBsL1Mk2RzEtR1dZ3wZiTMxAv-xyobBte1nTFhBh9hsQ-_4RYBe4gbyecsGimqYcnf7TzXkCTcOyh59auZkhkVmAPLEBQzS8hZWSH4T4vpU39lzRe3w01Qwfcie2EqsSb4UWgRZbEwiDTHAOpx7g5YEouNSBIbTapsuaSUOhT_0gG8ITc4la6ks330PbuP28okdJMctNcNFFfHMqFskZBVcQcAVsWChFM7C0fLLhHVPKK3410L20o29GL_lAKEO4RRIMnRj1MGWH1fIhpe-_jMOpCC3iB_a9CO92Y_8Pmcvj_0pTvcM2iXNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
دیس شنیدنی قیاسی به قیمت کالابرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108235" target="_blank">📅 12:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108234">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=Bu4C3x4LTfFHnMlP2N1RjsZagcSwyXSXZscXIgNva704asFNmqaj4nWDa752SjqPAftvAPX0Xeg5hlJPb5pYgxvYjCz1Ck1cWb_rLWp4QlzQ0tuYZbKxZzLXeMMIosvR9fUOHUymhNvN7AZJNBqihHv3ljuPBESKRXlZ_uadtEw6_YmoWYLGQgSSdlk0sHoUQ7bAUbCBurq-RTioTojOGkm5_Drckn4aBKdUmQkYrrSdALkoQvBcbcF1SVsxWctwrOsVQTu_y25hWOMqwrS1Uk06eehHleT0dfthMxa3ujal1vi9YmpQLGlB0D04t266MeDTAc8iWvOQsAidrY2aIS6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec43246d0.mp4?token=Bu4C3x4LTfFHnMlP2N1RjsZagcSwyXSXZscXIgNva704asFNmqaj4nWDa752SjqPAftvAPX0Xeg5hlJPb5pYgxvYjCz1Ck1cWb_rLWp4QlzQ0tuYZbKxZzLXeMMIosvR9fUOHUymhNvN7AZJNBqihHv3ljuPBESKRXlZ_uadtEw6_YmoWYLGQgSSdlk0sHoUQ7bAUbCBurq-RTioTojOGkm5_Drckn4aBKdUmQkYrrSdALkoQvBcbcF1SVsxWctwrOsVQTu_y25hWOMqwrS1Uk06eehHleT0dfthMxa3ujal1vi9YmpQLGlB0D04t266MeDTAc8iWvOQsAidrY2aIS6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😳
مصطفی میرسلیم، عضو کسخل مجمع تشخیص مصلحت نظام: تیبا با خودروهای خارجی قابلیت رقابت دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108234" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108233">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108233" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108232">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo06kDBTryLxytDQUwIRarHaZg381p2_CHVnZRW1nNCZeFb61gz27A5pShtZkNZINVxZWIdF_k9GFuVsSpRuEL-_ARpqFKRY2CadGfxCTOwkF9B2nniPNCY4OB-YDtfI-h_tQWk8-jy4Mlj3caa5x5w4XOYNGKAtx1LYKcw-rV5Mod2dWkNsGV6TZNBLdYjBoPMUel2JmONuvonPiG4dDYJV6MIKk3ROnTvoN3gnOso2cfQlpOIWUPCA7XyT_GxmTG5EZH925EfS0q8zb3YJV3QygfLuJ-4_IAcLi3J6KI49uSrjDa55Gg5HBjC8pGbkd1ZUKg21wfxaUJmfnTn_gw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/108232" target="_blank">📅 12:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108231">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=EEeA2nu07xLwzYZftVmI7JmaoHXal1nsNAiBweM6IpmTE8HnM2he3cAmcwsF2wyUu90vb0OWrBOpE0KA43qucZtpu-pRnS6vgKIU9KWsYq5bNIbEJLfGV5yDkL3uiPhZZwt2BkflLu8_gVUTnneAt0VMrdfc6U7uwFeVyz5V8V862YRxKGY2Iv6sXSi7k1pck2Cu8Sfoxa7PGOMIQch_Apsal-00vDaCVlFahZZjkavqR1IwZ-_k1pzDrGEod-qglfdzopSW037iielg4tssnZsnELOrurnSqTJ14yDdmvSkbBeYHR7NnVg7Y5vhovWXCtk0yWYOEbTft2Str-DNrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a6a1545e.mp4?token=EEeA2nu07xLwzYZftVmI7JmaoHXal1nsNAiBweM6IpmTE8HnM2he3cAmcwsF2wyUu90vb0OWrBOpE0KA43qucZtpu-pRnS6vgKIU9KWsYq5bNIbEJLfGV5yDkL3uiPhZZwt2BkflLu8_gVUTnneAt0VMrdfc6U7uwFeVyz5V8V862YRxKGY2Iv6sXSi7k1pck2Cu8Sfoxa7PGOMIQch_Apsal-00vDaCVlFahZZjkavqR1IwZ-_k1pzDrGEod-qglfdzopSW037iielg4tssnZsnELOrurnSqTJ14yDdmvSkbBeYHR7NnVg7Y5vhovWXCtk0yWYOEbTft2Str-DNrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
امیرحسین قیاسی: گلشیفته میخواد برگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108231" target="_blank">📅 11:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108230">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28909a001b.mp4?token=ORL8eS2OsJ6nv4PFhEdwx9IbPKxV-fm-65fK5mgTt9Ln32mZyBtN83qei4zK4YVkVzboVzjP_H7G2OdcWwXxDd7tQmsa_CeGmRnboDNdHfuX11t4ASKXJy4Uy8K-RW0jahnsdUhSryqZ0ENF5d6iaWRMlZ8vJhG2FOueokaMRgjOGYAnuuUp8JHrGT2bU7Z03cijsq2M_Pw-vhv8oxX6dQG3WmEd5EoTlGLbT8DGZ2tRAMDtgBy0ZJUEUVJE-b2zP2JszGyHI2Z8KXJ6RbrB2maU-poVB165usQhbaept5A06axOkK_v-p445aiS8D0Lrmc4CVF8LXQXT-Xc5_sMDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28909a001b.mp4?token=ORL8eS2OsJ6nv4PFhEdwx9IbPKxV-fm-65fK5mgTt9Ln32mZyBtN83qei4zK4YVkVzboVzjP_H7G2OdcWwXxDd7tQmsa_CeGmRnboDNdHfuX11t4ASKXJy4Uy8K-RW0jahnsdUhSryqZ0ENF5d6iaWRMlZ8vJhG2FOueokaMRgjOGYAnuuUp8JHrGT2bU7Z03cijsq2M_Pw-vhv8oxX6dQG3WmEd5EoTlGLbT8DGZ2tRAMDtgBy0ZJUEUVJE-b2zP2JszGyHI2Z8KXJ6RbrB2maU-poVB165usQhbaept5A06axOkK_v-p445aiS8D0Lrmc4CVF8LXQXT-Xc5_sMDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇱
نوادگان یوهان‌کرایوف در آکادمی آژاکس!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108230" target="_blank">📅 11:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108229">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=oET5s9DuQKgeOOazJLt1ykfrGTepyFqLhqA0nC1K_dZ91FGdQIT_Hx89vVWc9shyuQNEDYly8u0QY95U_xxESR3JNPNBcJsObwpWvgnxm5oCSo2fg6KRE0693JGAPjIWJtj8-gslfIffLjE-qPGUCGg8g69XcrwLTORc6G_KLAKOcB09y3kW4B0s81BDxsEP_f4Ra4UAFEvoWxTylrNR2EtnDDYQEKRS6k21bAX_5Ze1TEVH11L5EPdIxJr6HNI_maDvW5jNuA6czDJ4RCU_Ddyss79XEvwWOxd5QNA2FuQmgrD7iDXcLUA9_J5soCckqE2GUxB74n9rDBTISyKU2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d66cbfc.mp4?token=oET5s9DuQKgeOOazJLt1ykfrGTepyFqLhqA0nC1K_dZ91FGdQIT_Hx89vVWc9shyuQNEDYly8u0QY95U_xxESR3JNPNBcJsObwpWvgnxm5oCSo2fg6KRE0693JGAPjIWJtj8-gslfIffLjE-qPGUCGg8g69XcrwLTORc6G_KLAKOcB09y3kW4B0s81BDxsEP_f4Ra4UAFEvoWxTylrNR2EtnDDYQEKRS6k21bAX_5Ze1TEVH11L5EPdIxJr6HNI_maDvW5jNuA6czDJ4RCU_Ddyss79XEvwWOxd5QNA2FuQmgrD7iDXcLUA9_J5soCckqE2GUxB74n9rDBTISyKU2jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🎙
ماجرای خواستگار عجیب رضا گلزار: دختره بهم گفت نمیخوای تکلیفم رو روشن کنید آقای گلزار!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108229" target="_blank">📅 11:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108228">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=knQrXP9bNNFtL8h9eBlzo-I5JJyHiiafJni6w2h7_XjwGQu7yjcTIcU059Fc-XpDYoTyjA9-4cEUyXtq89OZQtRsmymBMVtJ2MjQQtZZSdB3HJxIpknda8Hl_MEwPTKgwQYHRExi0IT8GDExna3ff9yQjS2-2ezv9kAEgODwK6Du7snNtP9MguvemLujZxve_ucME1CdLhmU9rYYTSE8_QaRgdWbs0gpm7rX-2M4m-NUmtwAYWvaoSjeWNNQjXfUbguYXTEcfioy1YckDkqbnXYTZspbVpWBBEvMfUpwShn3xJ3ORLRBUwRL2r64tCytbZ7yLC8GAH4iXzm87YbfeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f9b62a8b.mp4?token=knQrXP9bNNFtL8h9eBlzo-I5JJyHiiafJni6w2h7_XjwGQu7yjcTIcU059Fc-XpDYoTyjA9-4cEUyXtq89OZQtRsmymBMVtJ2MjQQtZZSdB3HJxIpknda8Hl_MEwPTKgwQYHRExi0IT8GDExna3ff9yQjS2-2ezv9kAEgODwK6Du7snNtP9MguvemLujZxve_ucME1CdLhmU9rYYTSE8_QaRgdWbs0gpm7rX-2M4m-NUmtwAYWvaoSjeWNNQjXfUbguYXTEcfioy1YckDkqbnXYTZspbVpWBBEvMfUpwShn3xJ3ORLRBUwRL2r64tCytbZ7yLC8GAH4iXzm87YbfeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تاج ادعای کریمی را تکذیب کرد: نه تنها ۳۵۰ هزار یورو ندادیم، از مربی تیم ملی جریمه هم گرفتیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108228" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108227">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حسین‌کنعانی جلو این اسطوره سندورم‌داون داشت خودشو به فنا میداد که شانس آورد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108227" target="_blank">📅 10:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108226">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=UdXBT3rfcoDQj5FTECrSFt_VJEIPpKvE4N08ilue40FNxhBdjZ7JiCnAOEPQKpse8pgwG6bSwgc_mf8GxwRmlwqIzVJyt8141M4Ktzi4bt-rYEZd61Wd53XT9_XVAOAo16k_2XOyWphE6ZSfnsrEWn5q9BHftu4vYEb-RvpBy936s8xAsJTQnw_tiQ1LBPJay2YNEPH_0XPgVSZJFsKlH2sjXAqby3qoynMEm-W2uc5HqKX59FIUSLyOU-uUJTH5dfxQ6wyETfZidQbBuPmJi2z1GVscaA246yCvy5pzxJdiHNGwWAHMwgI3ruKPFRqDe9pyFbHXgmYyapQ7NdRjgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db6a9148c.mp4?token=UdXBT3rfcoDQj5FTECrSFt_VJEIPpKvE4N08ilue40FNxhBdjZ7JiCnAOEPQKpse8pgwG6bSwgc_mf8GxwRmlwqIzVJyt8141M4Ktzi4bt-rYEZd61Wd53XT9_XVAOAo16k_2XOyWphE6ZSfnsrEWn5q9BHftu4vYEb-RvpBy936s8xAsJTQnw_tiQ1LBPJay2YNEPH_0XPgVSZJFsKlH2sjXAqby3qoynMEm-W2uc5HqKX59FIUSLyOU-uUJTH5dfxQ6wyETfZidQbBuPmJi2z1GVscaA246yCvy5pzxJdiHNGwWAHMwgI3ruKPFRqDe9pyFbHXgmYyapQ7NdRjgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
گلرها بعد از تعطیلات فیفادی
🫨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/108226" target="_blank">📅 09:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108225">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=n4oWWbxXQMJNhAfiorwGKnKA3C8N9a7qacJIKFqXWUFbPiVb2oesKlu0Vj80loz_NGMcZFJPbPIeVmtFcldbNhB2NY_10k6YvoeKhlOtsbF5vbSBzQhGLC4324x5LQu8ZPq8BVa54BOI62KIcoob7kWVZV45m9P82FckEQmv42cGP9p3OjVUQ0-NcNGqprZqNOriXDxv8hdqqdabNqOLBoBxWy66XQiwVdLgqwz-BbcaJYKYvVX2R0liTJiaNLiJqzwEER4uCCQY8yckEStOb4G7dWd-L0XnxpKiuyJNAzgbGsO7YfNCem-JVxaR4IuOqx5C1XowA9tsWrTaWqCkqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e462fbf72a.mp4?token=n4oWWbxXQMJNhAfiorwGKnKA3C8N9a7qacJIKFqXWUFbPiVb2oesKlu0Vj80loz_NGMcZFJPbPIeVmtFcldbNhB2NY_10k6YvoeKhlOtsbF5vbSBzQhGLC4324x5LQu8ZPq8BVa54BOI62KIcoob7kWVZV45m9P82FckEQmv42cGP9p3OjVUQ0-NcNGqprZqNOriXDxv8hdqqdabNqOLBoBxWy66XQiwVdLgqwz-BbcaJYKYvVX2R0liTJiaNLiJqzwEER4uCCQY8yckEStOb4G7dWd-L0XnxpKiuyJNAzgbGsO7YfNCem-JVxaR4IuOqx5C1XowA9tsWrTaWqCkqzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
حمله علی‌علیپور به میثاقی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/108225" target="_blank">📅 09:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108224">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=ncMg_wKgSJxd4-jqwM8JEQBhZJ1vuEG2w6DI0Y9LSy7sypsC7GaRUyXNfHK90lZApS9qaKxRIylX598PtPO5YrH7gkmCjS0ZdUuqEUS8BOIvjWRurRf-usNzP4Jv4UlPPNhuK48-wPgMO_zaandHypVUpRLxEYwk0DQ50_6LxCw5tu2tJNzF2FQ_hfV1mk1HftqoUN6UA23OzyZFloU0RO4G9i_ylHpjVcboYQNGpSlW4VPuN3tLxkt2QMVYopKhcOCdBeY9mCWAIVeqUk2bnjGKxiEIed3qnJjvR5qQe7jFMIsj3897sqBJ117Wo5IjBnK3oZ_a56hR7bSc-kzmjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8286fc429.mp4?token=ncMg_wKgSJxd4-jqwM8JEQBhZJ1vuEG2w6DI0Y9LSy7sypsC7GaRUyXNfHK90lZApS9qaKxRIylX598PtPO5YrH7gkmCjS0ZdUuqEUS8BOIvjWRurRf-usNzP4Jv4UlPPNhuK48-wPgMO_zaandHypVUpRLxEYwk0DQ50_6LxCw5tu2tJNzF2FQ_hfV1mk1HftqoUN6UA23OzyZFloU0RO4G9i_ylHpjVcboYQNGpSlW4VPuN3tLxkt2QMVYopKhcOCdBeY9mCWAIVeqUk2bnjGKxiEIed3qnJjvR5qQe7jFMIsj3897sqBJ117Wo5IjBnK3oZ_a56hR7bSc-kzmjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
میرسلیم: چه کسی گفته نفت ایران متعلق به مردم ایران است؟ نفت ایران مال مردم نیست و متعلق به خدا و پیامبر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/108224" target="_blank">📅 09:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108223">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=kYGO7rHffqhQ39ro50YqV0_i2LrkTk4Zs4jmytH5SQLioHzE1oSZEBIb3BVmfmms6BS2h1XPAHpMM0lKrgDC1eC6cOGaG4A_8rkKnaO9qKToZFtbcFCfNuJ0tApFt4nKMkKuXnWhyyjgcHXYurLFk9ca4pVyayMgbm6upTHAkiYlXCLnfdJLpzDuOd6AW09_g9r8DB6H4iFpr-eY3YOQjjMTCTe_-ROpdGNdmYixptICQQ78NSUw1M3ItO4n7sOFxSlQo5APykeUC6QsScj7hNZzB-GjjOF-ndzx618QtyTRTxh_SAVq1NsrRoUgj_UFe1IC_Yj1zO9K5SsL1dqWUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdfc01a1a5.mp4?token=kYGO7rHffqhQ39ro50YqV0_i2LrkTk4Zs4jmytH5SQLioHzE1oSZEBIb3BVmfmms6BS2h1XPAHpMM0lKrgDC1eC6cOGaG4A_8rkKnaO9qKToZFtbcFCfNuJ0tApFt4nKMkKuXnWhyyjgcHXYurLFk9ca4pVyayMgbm6upTHAkiYlXCLnfdJLpzDuOd6AW09_g9r8DB6H4iFpr-eY3YOQjjMTCTe_-ROpdGNdmYixptICQQ78NSUw1M3ItO4n7sOFxSlQo5APykeUC6QsScj7hNZzB-GjjOF-ndzx618QtyTRTxh_SAVq1NsrRoUgj_UFe1IC_Yj1zO9K5SsL1dqWUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی، در برنامه هت‌تریک با آنالیز بازی پرسپولیس-صنعت نفت آبادان گفت: «سه بازیکن نقش پررنگی در پیروزی پرسپولیس داشتند؛ محمدمهدی محبی، بیفوما و ارونوف. صنعت نفت توان رودررویی با پرسپولیس را نداشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/108223" target="_blank">📅 08:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108222">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=ZW-fkDYnjv709_DOM7RSvSxwIuyIZO3PgY9YM_J0APAfpW2G-mIVkbrXccTVDuDfnJC2veoy39QkCmuVo8sqrnrFUHUmd3tQG6WYNWsw4Gt6PDAPgnCPexEyPU64aCS-1GeoAgY01o4BME-aBx3GrTSmIdH79dl6IUWdsBAE4_luMioB-oVwXlhGxFXO2dEjaGbI9tBxMyh889eFm3LmwXXVPvWP7eP9J-k44taiAyE1HEAj_-WURK8lzLqgrZ9lD7VmWq_kMGVykYGjcroh4hXwplP951f4huNKtIfCHa9Gn6Lu7jkJjLTYxFBp-U6qNbkDNSKGMm-Otp9c-3AxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ffece8e7c.mp4?token=ZW-fkDYnjv709_DOM7RSvSxwIuyIZO3PgY9YM_J0APAfpW2G-mIVkbrXccTVDuDfnJC2veoy39QkCmuVo8sqrnrFUHUmd3tQG6WYNWsw4Gt6PDAPgnCPexEyPU64aCS-1GeoAgY01o4BME-aBx3GrTSmIdH79dl6IUWdsBAE4_luMioB-oVwXlhGxFXO2dEjaGbI9tBxMyh889eFm3LmwXXVPvWP7eP9J-k44taiAyE1HEAj_-WURK8lzLqgrZ9lD7VmWq_kMGVykYGjcroh4hXwplP951f4huNKtIfCHa9Gn6Lu7jkJjLTYxFBp-U6qNbkDNSKGMm-Otp9c-3AxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
محمد تقوی با آنالیز بازی تراکتور و استقلال گفت: «من بازی را به دو بخش مجزا تقسیم می‌کنم؛ نیمه اول به طور کامل در اختیار استقلال و نیمه دوم تراکتور بازی را در اختیار داشت؛ استقلال شانس آورد که بازی را نباخت. اما مساوی، شایسته هر دو تیم بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/108222" target="_blank">📅 08:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108221">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=eAL0g5PFeU0BDmONWc_pyemPX2IevozcL1ATEXoe9WbM4QfvpbYi8BTO4gBGHlBoOeKVVrgQcKKYNYbnuoyILpFxaSgp4SA7Y6irVQxXTQAteiVo3aMEvECETo17XrztbaMhEJUlFnhwbMeJHcbuMycsnDbStIqhTccfKpbvCefsmoLXiJi-erFM8Gdt1DCStXj8PG9PS8b1Mgw2edgDD7YOzj7uddZ4hP2jOWSQsnD8A-v6Jf_N1KIg6nJ5TQuiCuoPdwOGN-ZbGrUBRlhTtdXkRhS-YW4ezpawI-jIUPcTtaRozKiN122qZIy8NVMbOiTnjMBWaShHALYB_PG-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c27c71fd.mp4?token=eAL0g5PFeU0BDmONWc_pyemPX2IevozcL1ATEXoe9WbM4QfvpbYi8BTO4gBGHlBoOeKVVrgQcKKYNYbnuoyILpFxaSgp4SA7Y6irVQxXTQAteiVo3aMEvECETo17XrztbaMhEJUlFnhwbMeJHcbuMycsnDbStIqhTccfKpbvCefsmoLXiJi-erFM8Gdt1DCStXj8PG9PS8b1Mgw2edgDD7YOzj7uddZ4hP2jOWSQsnD8A-v6Jf_N1KIg6nJ5TQuiCuoPdwOGN-ZbGrUBRlhTtdXkRhS-YW4ezpawI-jIUPcTtaRozKiN122qZIy8NVMbOiTnjMBWaShHALYB_PG-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقام بیرو از حجت؟ دیس‌بک بعد از ۲۸ ماه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/108221" target="_blank">📅 08:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108218">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKUWvrFBhBtgFbMkTh4ORNZqrys2lYm1NZ7bFy-uRxo26HovHK4Vt6j_bKboPxURyor8LE2szG9BguOTHbqkzw9lFdo5VdUqqYOw6INZne-MGLne1gD66Er_pgq0hTcETV71LgwoqsgcxVW0mREe6oDog8swwQbI3qeMsINgGNwWjvFWb2qAVbPhHXl_u-tl-bBvur6NlLHz2DwNMVawMtWGjwc0yUIuT76CdeVIM_Bytouk3_F5SzhgEqXU0ZawSZmaH2iW5T4x0g-kj1Qioh_ZXKNhpeG3N1ncjja7cd3NyqFKNH26z7uMQIV9daKGMH4Ft5QgvSoCKnKdnDOPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
#اختصاصی_فوتبال‌180
؛
🔴
در گفتگویی کوتاه با مدیران پرسپولیس این باشگاه اعلام کرد که در نیم‌فصل هیچ قصدی برای مذاکره و جذب بشار رسن یا بازیکن خارجی دیگر ندارد چون ظرفیت بازیکنان خارجی این تیم پر است و محدودیت‌های نقل‌وانتقالاتی فصل‌جدید مانع از جذب نفرات دیگر خارجی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/108218" target="_blank">📅 01:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pw5QiPks3viu9nQbg8rLX8a3mQQ-qiirEOomgf207_HuHdADAUc59wMphOm2XSeF5btl_6OJWPVOn-jWfYqmdiTZDKJL1QKXFEvSVt9q7usWGD0P03C0P96hwDqr7cCv2RsUfWqLWBSgZu4IoJ-rFB-qaOl_rTXnfwmmc5gAwWs6ziwWDqGdeSrxOd4W60w5g-CYlXxsvEQobEVwkhOmXRzBotbzmgubnJ9Hk_qODDsTDSTX-azb3Q0MlotA7nmP3unfoey1pDzBjFeXfHIJTWjvXDZQJxanRJ05u3q_LddBHGjkjQOeVZ4LRbUWV_mfrnxKCdyK9t3kzyfNZZ3xqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
❌
🚨
وزارت امور خارجه آمریکا در توییتر: به هیچ دلیلی به ایران سفر نکنید. شهروندان آمریکایی باید همین حالا ایران را ترک کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/108217" target="_blank">📅 00:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_885QB5j78ze5fQE8-1UHrujDoyxinMlWZIDgOIjM7pQficW8kWWSpHInb3b3SH1KFd8BBe11i0e0uI6bT2to8t-8kmJSNVOlLHlCKA20vRMf7kB7gRKSghCu5pTLHst0eaCrTs7poNVj1-28VyShw_HEu3pZ83E5FbTokAT3eIb0JX6PKWs5dE0clNu34rt3Pu97WKWMIuvn_7UiA2ukjC7cqM5OKEEZgt7TPm97dS2l6e8CjtvvNjWOq0HC5_BANdcEyd4nMoIGe99DSLJ7NisYUljU8pvcsquktHpaEIYQUkBfFPYwBZMqXtEFXqzBC-7874Ax5gTSweh0dtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🚨
ظاهراً سازمان نظام وظیفه به بیرانوند اعلام کرده تا زمان مشخص شدن وضعیت کمیسیون پزشکیش حق خروج از کشور رو نداره و حتی اگه بیرو با مدیران باشگاه به این اختلاف نمی‌خورد هم نمی‌تونست شاگردان نکونام رو در سفر به مسقط برای بازی با الشمال همراهی کنه مگه اینکه مشکل خروج از کشورش رو حل کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/108216" target="_blank">📅 00:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=LC9ZSFsO4XH68Vi0h5s_Y1hAZMkZSkJogjCXlg2QxXDohXU3AURxIXIrxRyHA5whin-f34K4hOHfIipDo4g_TJRu6PIroqfqG3Ydpt6cc8JDL5shbumVWChSOmQRlxFoSSAG3yEv9RcXe4X0mcQxJRIDpxhDxsL0SXsKsGle8SdnpbucnObjgyLWO1EcL7n72bR10OzFVyvMg8C7TksJfWabREl0aU0dqcEHchPo0eQZ5vG5zGEnUzpP3IqWh7N6wGUZLUcXIBIZ-_KuxbxFczrip5igifMjULmmvOUOq8yK66MI9rpLvM_kYGII-uBJcAsNvEfwQKJGeA-pUwh1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab16b6ba1.mp4?token=LC9ZSFsO4XH68Vi0h5s_Y1hAZMkZSkJogjCXlg2QxXDohXU3AURxIXIrxRyHA5whin-f34K4hOHfIipDo4g_TJRu6PIroqfqG3Ydpt6cc8JDL5shbumVWChSOmQRlxFoSSAG3yEv9RcXe4X0mcQxJRIDpxhDxsL0SXsKsGle8SdnpbucnObjgyLWO1EcL7n72bR10OzFVyvMg8C7TksJfWabREl0aU0dqcEHchPo0eQZ5vG5zGEnUzpP3IqWh7N6wGUZLUcXIBIZ-_KuxbxFczrip5igifMjULmmvOUOq8yK66MI9rpLvM_kYGII-uBJcAsNvEfwQKJGeA-pUwh1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
آخرین وضعیت شکایت باشگاه ها از آسانی از زبان رئیس فدراسیون فوتبال: هر تیمی دلش میخواد میتونه به CAS شکایت کنه و مانعی نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/108215" target="_blank">📅 23:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz_Z8an-r60xnyY7zfqCFg6l4s1uX7qYXGHqKRdx48BCtd8fZvexWB5CHt0XSlFZlCTwENdX2VTfczRJ5gkkMtasAJOjP0h1SwfV7Kblelv8VVqVHRBdX094gdCalmPlNH80e9v4sXtRdYoyYWly5OFbPhWwSs0RR-UwSajglfo92b7jTdmvhYsfuapxjZ0GwfwzQh5Y7gX4AqDatVwHntCpknySNDQtuRdHbWt__GLYWvmmZgoQEos6lpfCycsB3nrSTqHy-hbDHf9I-ju73y9kNiOPXQh40Ph3-pv6_B8nrXGrGRGRh3_BSdRdFUXppZwPQ-6yiY_oowXngZ92Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
فوری؛ بیرانوند از هتل اخراج شد!
علیرضا بیرانوند پس از درگیری لفظی با مدیران تراکتور و در آستانه سفر آسیایی این تیم، از حضور در اردوی تراکتور منع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/108214" target="_blank">📅 22:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS_MU5STZBQGXaNV3qvaUB1lbyqIQDjth6hSaIMYAgEiL6WU1IoGE36KY_BXqrGlN3SI5NIyuPOoIuheghnkpip8Ohv3ZejBeQV3v9aD4j6PodzDofeaQHK_kJf-xR7hD7jAjdsABlD4PfyyK0eP8pyAQUiuw9CWN7pJEH7N-XlKZKns5QpiXUvopMZfs9qCYioX5TdU8MxddS0D5Mw_ZE5mzF_grYfkN8DwgM8owHUyww5g14WCO08cmOf-Szntwlj2OKulb2NNqNiIVGZLgJDjcTQxJ6SWIMwzWxrPgYjbYJzZqSQ2jgiEm41WCZfsqaXyLDCgGpMBqBZQYCtwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
❌
محمد نوری پس از شکست مقابل پرسپولیس از هدایت نفت‌آبادان اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/108213" target="_blank">📅 22:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=aHiSX7KLYDghXVeNvFaY7r7DPML7-JZ6_MCf7s9-dEC76jc0yKMibmxF1YDkm90LsPze6Q1VeD3KIxm0hR0htPeV-vfAADnI9Y9FjrxSFw7EjN2K5qG1einyS6gAmdBSIzgMSEmPfwUcLSUiSW5bKIUN4s-xGIVsGtJu65qDh5v-jkuqX6CjhBNayGDXTkcbAKw749OBZSTzwr90uhl6fi9lKyPrFzrFjxrL_tAL2SGtb3OUQ3ac6ddWZVXQUYO9TCHqeBAb6KbHzB2YKrLPLB1U_1pk9_7UGawMD1QUg3MN6_5lnmfvu64u2I7ws5pWF34c2Gk-GF7S81ZYIEAcnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b78fb174d.mp4?token=aHiSX7KLYDghXVeNvFaY7r7DPML7-JZ6_MCf7s9-dEC76jc0yKMibmxF1YDkm90LsPze6Q1VeD3KIxm0hR0htPeV-vfAADnI9Y9FjrxSFw7EjN2K5qG1einyS6gAmdBSIzgMSEmPfwUcLSUiSW5bKIUN4s-xGIVsGtJu65qDh5v-jkuqX6CjhBNayGDXTkcbAKw749OBZSTzwr90uhl6fi9lKyPrFzrFjxrL_tAL2SGtb3OUQ3ac6ddWZVXQUYO9TCHqeBAb6KbHzB2YKrLPLB1U_1pk9_7UGawMD1QUg3MN6_5lnmfvu64u2I7ws5pWF34c2Gk-GF7S81ZYIEAcnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
گل‌شماره ۹۸۰ کریس‌رونالدو در بازی امشب النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/108212" target="_blank">📅 22:28 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
