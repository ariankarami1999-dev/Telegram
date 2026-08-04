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
<img src="https://cdn5.telesco.pe/file/PR7HEnNfexSLnQAMZvN-2xy4IoABrpSMe3yAJY7tPm6wdlkTDWODgbJBa4-SYabZKT-vqnG1VXcTsYht7YCunyJ5ZOPq-BKGBKqflXqH8LqgbxoXayHnio_JTKaVV_08xBUvl8lyKmNI_5zt8qB510MdyIC2rWIhEwK8D_ftUFBhpUnB7l1-VeGDN369_TnfX4zZRHmbT4ve5gv3fOtLfnBmc4Cpr6OL5_0Dsqb6iuzGychrdCrMibk2Om6E8eE4UTR32BFDqmQ1PMLMA705dluSU37PYNmK8VxNOoO8Waf_WTOir4-82tmoMAGGQ9io_B30UBmqz_zpCa69chAZFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 497K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 12:47:33</div>
<hr>

<div class="tg-post" id="msg-102667">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=A2f-YeZmwIIYIzRlhjpuxeHyGCoeXjKZCzohmRumNoYbps420g4Osl1H7ZLZyrDZOkzGYoAIHL50J0ScSLwWj6Q0erjCMOsag1CPTnZiab_z2fxIb4rb-r0TIPWaeV8jmth7bAnAyovPQMQWwAh-dNmn7pFE-v2FWzjp7f5fYMy5FOdgFBjgz2p0lsoSjtNhXhLLBC3qCHqD8qb8XFRNdSR_jM3u51EJe2aVxZxzKhHQmakZbH8g04XvgFNbdmAjPSJ8VIp71HNhrQ1vqOyQ31OXTnPyB3HvjASCM37NoVMVMWPmN_sDj8TFN5Nk6i3-6oiOISjcy4ZeTdTRupgkdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/937fee7ba7.mp4?token=A2f-YeZmwIIYIzRlhjpuxeHyGCoeXjKZCzohmRumNoYbps420g4Osl1H7ZLZyrDZOkzGYoAIHL50J0ScSLwWj6Q0erjCMOsag1CPTnZiab_z2fxIb4rb-r0TIPWaeV8jmth7bAnAyovPQMQWwAh-dNmn7pFE-v2FWzjp7f5fYMy5FOdgFBjgz2p0lsoSjtNhXhLLBC3qCHqD8qb8XFRNdSR_jM3u51EJe2aVxZxzKhHQmakZbH8g04XvgFNbdmAjPSJ8VIp71HNhrQ1vqOyQ31OXTnPyB3HvjASCM37NoVMVMWPmN_sDj8TFN5Nk6i3-6oiOISjcy4ZeTdTRupgkdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
دلیل اینکه چرا کورتوا یک‌دهه جزو برترین دروازه‌بان فوتبال اروپا قرار داره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/Futball180TV/102667" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102666">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=uQyf5Lmm3Sbg320is1xfasuJKjNGsy-i1mNCZfq0vTscJe9SMDeMMnMVBU5SRYAq7U1My4XyUcNzpiCvlb8q8dMT0mbQ2d2Kw93iyUtju_JXg6rKzOtgcEPrrcoWu6EepvffGtt9J1F33AfHhDSYMzlI-ja8xvxbUKRa-wdr6troi3VTBESLm2MiHq517YMvNihoTD4R2OKsOXqUuWcD7wFJCUOKA3_tT-LAHj2crNvPukK14Y2CWxKZdfhUUi4byjHYtn_0Nk1zaSoEc7bbfHOMF2scpC0R6amBuC6GyXURsAql-WyBgetk3JDCZFu037WpbcdNx6aajz4DeCFc6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=uQyf5Lmm3Sbg320is1xfasuJKjNGsy-i1mNCZfq0vTscJe9SMDeMMnMVBU5SRYAq7U1My4XyUcNzpiCvlb8q8dMT0mbQ2d2Kw93iyUtju_JXg6rKzOtgcEPrrcoWu6EepvffGtt9J1F33AfHhDSYMzlI-ja8xvxbUKRa-wdr6troi3VTBESLm2MiHq517YMvNihoTD4R2OKsOXqUuWcD7wFJCUOKA3_tT-LAHj2crNvPukK14Y2CWxKZdfhUUi4byjHYtn_0Nk1zaSoEc7bbfHOMF2scpC0R6amBuC6GyXURsAql-WyBgetk3JDCZFu037WpbcdNx6aajz4DeCFc6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇰🇷
هونگ میونگ-بو، سرمربی کره جنوبی در جام جهانی ۲۰۲۶ مجبور شد در برابر مجلس ملی کره حاضر شود!
‼️
او توسط نمایندگان مجلس درباره تک‌تک تصمیمات تاکتیکی‌اش بازخواست شد. از تعویض‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت.
هونگ در ابتدای جلسه از مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/102666" target="_blank">📅 12:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102665">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=P4yWSJxVBBbwagXbFCi_OzsSCPJUjCc0gfgHkI64nkhHFLYOnqdHhMDxNdkuzJfuBJOi2sGIGWHGLM7dzffjimuwd0seD4cwHSWW8VncT_m47K0obTtmmLZ7JbiS1yImaJurT_UNg2u96MNheh6RJKcubxs91mZyhuqdi6M7vgYzvFP6FsksyUo1RDNNqgRVwW_J088am6uhTZjmfWe3TWu6xnbgyth5KBmZ-YZLjgkOxoPKDTkkw3Ez0UA1sl9XAF7omkvdDv6R7Z6AxgMILznPKGa_aXWlU3jKm9wQZ_YF2pUwG2IILLlUI3UD7SYppwN0dO_RUK21nHX15bAxFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be9e48b7ed.mp4?token=P4yWSJxVBBbwagXbFCi_OzsSCPJUjCc0gfgHkI64nkhHFLYOnqdHhMDxNdkuzJfuBJOi2sGIGWHGLM7dzffjimuwd0seD4cwHSWW8VncT_m47K0obTtmmLZ7JbiS1yImaJurT_UNg2u96MNheh6RJKcubxs91mZyhuqdi6M7vgYzvFP6FsksyUo1RDNNqgRVwW_J088am6uhTZjmfWe3TWu6xnbgyth5KBmZ-YZLjgkOxoPKDTkkw3Ez0UA1sl9XAF7omkvdDv6R7Z6AxgMILznPKGa_aXWlU3jKm9wQZ_YF2pUwG2IILLlUI3UD7SYppwN0dO_RUK21nHX15bAxFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
گشت‌وگذار امباپه و اکسپوزیتو کف بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/Futball180TV/102665" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102664">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOfEYMUW9kYYpgEIuA5FWmqnYV-4dHJT7WB92ssAmQZg1njsJpi4Z7fwbmve796miXcN7HlY6-2-lbzF7rujeBGkUBxOqV11rb9fVK85yIL1tIt61J7IQZIV5O2BE8cjp2jHYQdQ5rMoTzVzt-Ls9W38UgiCDjUZ3hXP0hyi6V-VFcfSY-CRvSRwP0aQrER9iO9G5Xr3uJMhMaF3JpKg6WAINodyZ8J3duwsiQrjwDcA7yh8xiqerCajGN0tLKoWK0vRKbNsFsnTWnvmzwAYgssIcJq8ZkpnTvZuRNnuL3AY0WFj_I8lgidrHrBnRsjOnlyOBLeUuxfyTevx63MYdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🟡
فلوریان‌پلتنبرگ: بایرلورکوزن درحال مذاکره با الاتحاد برای جذب موسی‌دیابی است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/102664" target="_blank">📅 12:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102663">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnFlWr6Cxgbwu6L06W8J5PaLzEFuKb-mDaI3Dhpu824y0GHoFSk_aBWA1PUMhy8PFqYzm5Q4NQJaM8jybwy9FFBCxpdnDMiL9F3PDrhNFgdjifMXbrP6mZITv8-S9Vld5LB7fIAtxS5dCJD2h6fw29VAtmXwkfCk6ljhJkGD4Vpb3yElZbumZpguiK4E7-N8BMBxIajBgJ-ZVFgb7UHnHn64hPktZ10GRDMzECjETzoYMKbkAdwFp2JJrpbzfM1dKEirs1cuGVnyB-ztwy5GXZE2Ic6p0v3uzQ9A5Jbz4qD_bOutIQ7HMeJKvqwh9o8h2tUvXBbDr7cNHdDErf8Dzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
فیفا با انتشار بیانیه‌ای خبر حمایت دونالد ترامپ از اینفانتینو را تکذیب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/Futball180TV/102663" target="_blank">📅 11:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102662">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UITp43Tu7Z3xq3KL78biQer--Ck-bMO4HJyZCtGZdRQslMKnQryuV_zwUXGRUHWfg2r7CCaN2gP22E-DCuENVDHOS3ShtTNABntWMJ2JGQkoBQj21BagPf1rv56x8v49f2yuBLicM6AXJNxZLOsPg-LscPqljpIqFQpYFGKThrmIt6JVkJUptkf8imJB3L0Co8bSIQsGBRZ1fVoxQEHpnEsiQ6-CoSSQRi8t_PMC8HDjsZOjrHAk3Ub5SZop0OaIIEVBXZ3wMGwdM7wxS53cIUkjOHT7yTlxASwYW7lNREJzZjYAx-OZkJfipWyVL1ZLaBe7aq1UqyosM1e3wKg6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
⚽️
#فوووووری
از مارکا: رودری دست رد به سینه سایر باشگاه‌ها زده و گفته که فقط به رئال‌مادرید میرم. قراره بزودی این معامله تکمیل بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/102662" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102661">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uQbn6QAtRi62l8XWh8BE1MgwsMQwrnirNBM0uGYYXhPJvtmfN_6RCgv2kqo43bhWUOwRkV4NLevuP8UdJ0gmXPE4p_LI4weOWkvKmorfPEQp7yaps_VL3-0B0O1eTQRcqLWTV83gTXPUxSiDQvcll1tfiD7q4raktdq7bzpGGQ-vzbjPjNRuyeyR1J0T4Vvn160MKPKNAtQ6MqPJ5ILh0h3ms8AemO-35fw7fn80EUNeyuna6K0Hytrdvb9oWg1f3nq6jWsaMqLxOviSkyV50vtHLuxqcl5S6Qu22lhd9q7l3S6qygqp1wBOP6a0_Zg2636rVAOsKB9El3gwcvUAsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#رسمیییییی
؛ نی‌لاند دروازه‌بان تیم‌ملی نروژ با عقد قراردادی به لایپزیگ آلمان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/Futball180TV/102661" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102660">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
😆
😆
🎙
ساکت الهامی: 55 میلیون تومان دادم کت شلوار آنچلوتی را خریدم تهش ۶ تا از استقلال خوردیم و باختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/Futball180TV/102660" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102659">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yao6cydMPDDf_6O5SveyjH3qjr_zvpZG21uLpWBQmWS1VYqyoW1zt_J3MuoEkXq6lidt7eOsuHuQOgo4D3q7dzYpfBpGv-SMZ9z2ZyYeV3lm4E2jbdOyy2uZXPfwYF0Oqq7E2eGqR4hHZ3XBVRhzqAPjW-MMvdrn6H71JAUOkAmeivDHto_dmNpEAn7jxx97jlkHxu7WRdzGhk_HHkhphNeEwyGLcWyY9ySCRKp-lCacK8RK_dFHzQAXHcl46Dr7tLyC62wR9cbDv86934V30tuvtwe0e7EDzry8YMTqKBYJP1WOsENpABI-PecFjemNRYg4UoneIi7roT0PFgJBAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژاکس آمستردام از جذب مارک آندره تراشتگن به صورت قرضی تا پایان فصل از بارسلونا خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102659" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102658">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=MmK2CnVJFUHfICvOtUyd8E8brqLznec6Dka4K_VoGYX_nNL0KpelVE0nPymbjSveuaGlwqkvTAN5r93Eah5aIsO5fnVTmidnjAMkIvEdQgk--NGjlEZuj9RFfY4WWScjPpb3dEOQiM3go_NKq0ZnHSNWthCVLGu_lID4fhejdMWBxb6SStDZK8v_ayV6pOlNPRR7PmGP1cYq10SwyaI71Gke5eMrISAtVfih1AuVIttdgQyo5xrCbbaOO1OrJNIOEi9nxCEQAwN4AGaRYqQgBZWyYGxioZTJNkQGGRsjHvz72EuXGyriG6s7y3Mr187EoscFD8Q4SlayZNTS-p8H5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf1a57969.mp4?token=MmK2CnVJFUHfICvOtUyd8E8brqLznec6Dka4K_VoGYX_nNL0KpelVE0nPymbjSveuaGlwqkvTAN5r93Eah5aIsO5fnVTmidnjAMkIvEdQgk--NGjlEZuj9RFfY4WWScjPpb3dEOQiM3go_NKq0ZnHSNWthCVLGu_lID4fhejdMWBxb6SStDZK8v_ayV6pOlNPRR7PmGP1cYq10SwyaI71Gke5eMrISAtVfih1AuVIttdgQyo5xrCbbaOO1OrJNIOEi9nxCEQAwN4AGaRYqQgBZWyYGxioZTJNkQGGRsjHvz72EuXGyriG6s7y3Mr187EoscFD8Q4SlayZNTS-p8H5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
پدر تشریفات ایران آداب استفاده از آسانسور و پله برقی رو بهمون یاد میده که بنظر هیچوقت نمیتونیم رعایت کنیم
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102658" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102657">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBzyfhZhytttqU8ZfdJLEBSLTEQdi_GgKs_Uw6zTzAWjeOaMyVKBpZbwBwHWkE4QJSg_f8cgIYAzkSE8fZTCNz5iSFFgZeDGFyl-NunYIAtGY50me_C1qyv09Jc8vZ-zi4Jjx2BMHFx-bBYCdtL1Y0Ao83IxPMH7QeE8Toiy0cOzCO_HppND_3llX3Tz6m5aITUfoe8RtT0MCsJUvmchgXqEwHH32eAjP3UHmo--RT8EchIjwJN5koWvEvKCOYcGsMNeUYZGTJ8_m60BTodFbp2KRgdGnKyozgJbD06SL3pmYM2BFX2orYfVIYl6AuHzARpXx0Mz0-c-LmCjQzZHcn10" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0e4679b6.mp4?token=EI_6HTaKTj012GwVCeMwVP0Eh0ojgqsiat9sT1CxRvyCwiy6va_h-7Ssu4W7hKddRIU8sTwQNufDvIdCSa8ZvhFmiWpgPrm5epcejSqcHUIfIAicJn_5YlwXcEj37w0tvusXVW48ReQZ8UjEiAalmFfV1wrieOhnlV6wVshrWitxkiSjmKoPN9MEIArCzITmEVywIpQQoSq47yHJ6PhK5tOLh5VbmYGqbhCLBQATV3XqReOmTQb-UVVPvND-0tbL_Evhp56i9U1fRMDhMjl4MZLycKesr9I40zM9pjbnYIotnWZnPkGx3Lyaay74x_gotu1diJZjcDt6muQxyP6MBzyfhZhytttqU8ZfdJLEBSLTEQdi_GgKs_Uw6zTzAWjeOaMyVKBpZbwBwHWkE4QJSg_f8cgIYAzkSE8fZTCNz5iSFFgZeDGFyl-NunYIAtGY50me_C1qyv09Jc8vZ-zi4Jjx2BMHFx-bBYCdtL1Y0Ao83IxPMH7QeE8Toiy0cOzCO_HppND_3llX3Tz6m5aITUfoe8RtT0MCsJUvmchgXqEwHH32eAjP3UHmo--RT8EchIjwJN5koWvEvKCOYcGsMNeUYZGTJ8_m60BTodFbp2KRgdGnKyozgJbD06SL3pmYM2BFX2orYfVIYl6AuHzARpXx0Mz0-c-LmCjQzZHcn10" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
▶️
آخرین فصل‌ لیونل‌مسی در بارسلونا
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102657" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102656">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برترین گل‌های محمد صلاح در تاریخ لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102656" target="_blank">📅 10:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102655">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzEIEP1EFY1we2j6I9Z9GxlL2t-mpIVEC9PoM7z3zwmG9sBxXHsyddIWPkVxzqSiZdNMWrZIVOVKYk-ujJ93sYHu-_5LYROHMA0zmcfr8P_l5OeSHlsY5cq9Fh-A0jcLp36Hy8lzGQrfywqyPgubZPWl6eosgIiIkcGvqzlRVHs5ySUsYaAR0PGbGJ0075RxBI6xmIRJwM0HNZPcUoa2-ePrZXgGAi4j4k9BKyeT_jUCqKz-rp0BKM8UjItra5-dA6AWk5d55oHaysqRHqId76FCiB67u5QCkHP2Sh_eudSjHZcXqxsJZBzM1QTtysVj8saDdodjK1Rfk-FrdxJi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
مدیرورزشی لایپزیگ: دیومانده به محض بهبود بیماری خود به اردوی تیم در اتریش ملحق میشه. دیومانده بازیکن تیم ماست و به قراردادش پایبنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102655" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102654">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👀
🇪🇸
🇪🇸
یادی‌کنیم از بازی دو سال قبل و پیش‌فصل الکلاسیکو که حسابی جنجالی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/102654" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102653">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
‼️
😔
🇮🇷
پرزیدنت مسعود پزشکیان در واکنش به جنجال‌های ۲۴ ساعت اخیر: استعفا نخواهم داد و خواهم ایستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/102653" target="_blank">📅 09:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102652">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47080196.mp4?token=bk-kFDh_fbuRyO6bxHl7N1lSJv3tjIXBkq1VYO-JVf8aTOFyuRsJX8-DV3pDBLSmqz7H56uBpER3k1V5L7KHqctVZUj8UjQt6ZtgV9Jq58wZHBa6M6uJqssp7Nz1ovOstSyG6YluLPSB1RvgL3RQ_mToBuUpLMeyvNWrvh0gXcw7e930GI7D1yBJme1tUabFFMfeF_dv2_xjPGorllaRUTHdO3Ilj8f-ICWhMf8BOLGgyk7kVCyIxUAejBE6vxN-ysWKbwip719RI3wOc8WBwfQe-a1MNRLqHKjplwa7m7bExBwj3gxVHRFomPcSdHu3S9TqgzQNE24KKeycTlmPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47080196.mp4?token=bk-kFDh_fbuRyO6bxHl7N1lSJv3tjIXBkq1VYO-JVf8aTOFyuRsJX8-DV3pDBLSmqz7H56uBpER3k1V5L7KHqctVZUj8UjQt6ZtgV9Jq58wZHBa6M6uJqssp7Nz1ovOstSyG6YluLPSB1RvgL3RQ_mToBuUpLMeyvNWrvh0gXcw7e930GI7D1yBJme1tUabFFMfeF_dv2_xjPGorllaRUTHdO3Ilj8f-ICWhMf8BOLGgyk7kVCyIxUAejBE6vxN-ysWKbwip719RI3wOc8WBwfQe-a1MNRLqHKjplwa7m7bExBwj3gxVHRFomPcSdHu3S9TqgzQNE24KKeycTlmPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روایت دیوید بکهام از میراث فرگوسن در یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102652" target="_blank">📅 09:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102651">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TttQfYtL06AB0GWuzd7LypBbWOM76yhCzoKJNK_wcF4OlK1Tev6AphSysA0P-U7SwDGlU7Qf7aOv8vQ_9G1NPdVkaamB1R3PNnZgwgCwuS9Mp26dIKYgWmU9VoQGCA86nistSelRr4n2MQiNqYKlp8iW3kzs6ghlNfKxqOZR5rc8bj74a3J0gNqGCUadh3pd1F_Ut50KOmfI3VwtODDZuHHqrS2Qb69Fiucbp5nbGe30VkCUUxAIi6ss3RlR0nYHBp31NxLZ--QAuvHCIkvePPLShTTixazyANAMt2lywvo0NGEVjVH4JgGnTpNabexmcfqmdV5gzzuZz_hirvMJ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
کشور عربستان سعودی در حال ساخت بزرگترین شهر ورزشی جهان با بودجه ۱۰ میلیارد دلار است.
🤯
این پول معادل هزینه خرید ۸ بمب افکن B2 یا ساخت ۱۰ تا برج خلیفه ست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102651" target="_blank">📅 09:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102650">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeIecWXv7za6JA807m-ERhRffFF8KUbFcTfk0D7Osmmv-4rhuSLT71Da6R7r_6H41SDPhsDaRbQbs8xpkkZzckFx-i76xNe_ss0GhVNHEMAvgwXdPPLN4fizxtmUxCxLfHrFhFAx9rxDezpPfm8jXRXYLggLClO-bJobxX5whbfvCvMzzS4U-dZeQcAWiPoM6uiVH5WFJWn-Zpe3Ovh4fwz871Wn-dW9JBd24b1XWe2iCabpAbHYeF85RbSrSxGOoM2Y7f3nr457fglDvJ3mK4tCFhof50BCDbEXaFskrcwFMLZWd7d0W8JdaStqcuos_8wvKGVZU7ziAFRG6W3qAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه سان‌انگلیس: باشگاه استون‌ویلا بدنبال جذب مارک‌برنال ستاره بارسلونا است و قصد دارد رقم ۳۰ میلیون یورو برای جذب این ستاره جوان پرداخت کند. هرچند که بارسایی‌ها این بازیکن را غیرقابل‌فروش اعلام کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102650" target="_blank">📅 02:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102649">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=ZgpLizEHSb1VRZXL13OK-JhPE3guoLxL50T2rSkjT8VdmQXrrfZIVD3j32JEuzXYJocqLLVWKnmuVH4ZYwOLA0e6ABaAomPDFOXXi9Nl7M_-JjTTzIbmL-74mRJGwCGCek-aFzOF-0CL89SHK6xY6luUN3ZsdtWq8MammAtiHJW8KzBanjTs00ldyLV3T1HuyTw09ZQKzSzhrU_NDyoojN28-xfaoKT-gH4Dole0hQmbHghIhSmsFLeZHunxyJoBvLbhYVzF0xwisXoRnwXpo2QRBTgyEvGV02vUtqSxicU6eNxttC9r5gUhCP6I2iUXqOrEJ30izKZHC1Ni1cymzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d8f16631.mp4?token=ZgpLizEHSb1VRZXL13OK-JhPE3guoLxL50T2rSkjT8VdmQXrrfZIVD3j32JEuzXYJocqLLVWKnmuVH4ZYwOLA0e6ABaAomPDFOXXi9Nl7M_-JjTTzIbmL-74mRJGwCGCek-aFzOF-0CL89SHK6xY6luUN3ZsdtWq8MammAtiHJW8KzBanjTs00ldyLV3T1HuyTw09ZQKzSzhrU_NDyoojN28-xfaoKT-gH4Dole0hQmbHghIhSmsFLeZHunxyJoBvLbhYVzF0xwisXoRnwXpo2QRBTgyEvGV02vUtqSxicU6eNxttC9r5gUhCP6I2iUXqOrEJ30izKZHC1Ni1cymzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا سپاه به پایگاه آمریکا در کویت حمله کرده و آتش‌سوزی رخ داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102649" target="_blank">📅 02:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102648">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇪🇸
#فوووووری از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102648" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102647">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuOH_Yp4V5-jDDnDcA8btBUP2sY6-5V0sQ_TGmKFAUAb4iOuf73-9hjO5AZhqNDQvjwxQDBAGOVoVtF7Vt-3cal-zZi0qwNNie3jyoOf9JDfu5E6babyOISpcTimWNWvhnWAZt0gphhPAcbGNDQepwiM5BT-JavpTAreyDhfqmihzP2Q18TblSn6cTmSkU8bNrBp4tVQKbkEcnUBfpVDo6-FsWbJYLezJVLqQyHnEEChvlzThfsf_iJtO-1AuiMTTBs8SksGI0LbhYTU6DpI5B7KCAkHm0SodArywt11LTT47Wafb1-1vNq6BwUuZTBTUjEwg5eU8G_5i0JTabpiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از ESPN: رئال‌مادرید پیشنهاد دستمزد ۲۲ میلیون یورویی در سال به وینیسیوس ارائه کرده و قصد افزایش این رقم را ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102647" target="_blank">📅 02:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102646">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obcSzdhUA0nGrDOwQ9N6RDb0Aq1scTLFANmXh-W2ytRDZICMHzV5yhNQOkTGbaaVwtCxVidsICqA9tq1vZtBU2tDd-GyOueIg536VV2ORtUcLsWSPBkzaHOxEfxMtr8MErcxHo92Cgh7_T9QooSNt3IXEPLCoSDSYsgS2FE1ygVR3OC7_XV7zuNNcv6ciUQAWHUq45dwyY6ISM6QZmT5SK8ri0B_YwGPCFm6z86Q3RrDch4dDOgTrD_-Xd8sXGUdkyokU5sHVZyL0ZMamzxfP2dLkqAlYD-YhYpK7ZU_YRNOsCket_KA3ieK3BveHOegLgj2rxPYUbAW0rzbyVwf7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
بن جیکوبز:
چفرین و ناصر الخلیفی در سالزبورگ دیدار میکنن تا درباره تحریم جام باشگاه‌های جهان در صورتی که اینفانتینو همچنان رئیس فیفا بمونه تصمیم بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102646" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102645">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KziZVXHRDlL7BFLJpO8-jSaMpo-xjjDQNu0wbnkh3SpNo5xXOKCms6R2uWNQmIlEW0HrLNwAvAFv6mtmkCDX2x7-_ZLjDkQjSFP1yu60zAkxJ8bZDAuiWPkIwgc9Nm4Jbm-j_owd2yGr6eLQaC10aPD7OXATL8nc5TGeMkxqwW4W6qTdbnkmNRXX8EEmOTruPMqjDysosMyimpHBguT_BgVxwIcjtGG1qi82Bi8ERSo_Lj-XDSx_WONCSPphXfRF8N_TWhCm_caEWvHzg-J5itZ95FeFwXZvSD_o3cNM8LQcJ-aMKfcZfxj6clNbp710DpBa59nqCePv48EuHtrJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پاریس؟
🎙
فران تورس:
خیلی خوبه که باشگاه هایی مثل پاریس بهت علاقه داشته باشن! هواداران بارسا باید احترام خودشونو به من نشون بدن تا بمونم، فقط باید بهم ثابت کنن که دوسم دارن و بیان باهام برای تمدید قرارداد مذاکره کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102645" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102644">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
با تایید تار تار و اعلام رسمی ایجنت بازیکن قرارداد نهایی شد
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102644" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102643">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZlxLj-srXeOdjonwpmkp9dL65bqFME80BHcihJ0I68kGfcaX2L2Zfj4jVeBYyi2Pj0ZgUc8DlCOKKAd1WjggOUUdYWBIt1R0YclF2kj3lTb_IGKn8vXBWBmI5tK9FXbLAn54sqgprjzBCi1QHto4cuv7cJWy04HNhxMVMBm2nxRMI6s3gqx3irko0tuoZJyZ-zy4OsoLzQPC36tYJqEpSm6kjWQD1rkKs8poPS_Pib51mOEi88JMam3XwMKupqsDo9rAkcERc2vCKyDD9g_mTfmYssXA68SLYySWnhGkshIJp58VouAVzQi_VSjGL_msHAXw90uQdsIY74Oy0PvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🔴
تارتار تایید داد؛ پرسپولیس بار دیگر خواهان جذب</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102643" target="_blank">📅 00:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102642">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDFUZcFo_lKcMwrjjHKnpPOBbBZ4hhMSJEnGKeX1HJ7EHzcxeXLz4xYcnUYE60VAX06CKXpIuJMlstKEbih-lZ-X_4QnfydmjRu_gP4QWBMHyzWlspmLharfZg5MD6ZRHM-V_9MeKd-AKTcPDRtSSidHfqt0gDLBEnLxHi0PpZs3kUHgRdlqQZYJy1alfI9XwUTu0f2RQKbWrW_wdDPAH3JGe1t-j39cf5HqSLFRtf429ZxMxEZh-qp_Z1FLm0sK4e34xZuA3f2O6_LRs5pM2LoMlSqTZ7HXa43jWSUMttybKY6xatCaE944nuPWBnwF_xIVmCiS8_84J3OsaGgVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
برناردو سیلوا:
بی صبرانه منتظر کار کردن با مورینیو هستم، اون کسیه که برای فوتبال پرتغال خیلی مهمه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102642" target="_blank">📅 00:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102641">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b215f0831.mp4?token=i2pKnuFEYWbzylQEMKhSLNd5Kd1uspyZD5LB58rxkQ9Xwb4lbANjhVag7p7wfojCqxIg_xn78tcyatLswYH6knPpmzHcqwgsODIZhLM0EePVZlNXBcRfmUGENUarp__XiFGeGI38Y8Q1upCqmiH-1_nNPY7Ee_gA495pqHwLZzS_ljBCemghkqluw-SkRw_zfA_1Ug2rZtG2OWj7OOfF_gJkHpzEvWsLOJNrHb9X8fBmRlhzJbZZGVVT_B4mCAqE2WDrbKEWd_D0AMEK2LqD-rXd8mvd3O8PgVjgDpM1KyDwvLy21D2ThDmdLRmNjMkD5Dm_ihN-5llVjkiThUubAh_8Hpeb0X3yw_gb_2LxmbD7tM0XndE5Wh3VW57Mf3C6ihWEjwH09OheRRaYgSo3-ZQiI6iv48p9Yppq-Ze2KrKc_FGe-w6_bmHDeuw-VIcRenAaDrR795kl2ZpD8wnZK-K4PVUHOX1FqKZQdiD_XDZLkQ0Cyv92haMqquTdEP9TcD3wPw7KJIgQFv1MP0QtzgdMrCpT13vzKTgiqZ6sTXbED9yJeu3-NaABBiV-edHUfNy2ZfhfOYXUk2J7-YYL8GOS3nlRliGhArjrQ9zgx7Vme0HLEu1783IDPB1DJNEuwx2BQ4DhuzxUs6aLF_92x4uNw19wbrd2zX_Jz7aahiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
برخی از بهترین گل‌های کاشته تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102641" target="_blank">📅 23:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102640">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290de4f011.mp4?token=RcpGfHRmeQ02nc4HshxFIG92GjANJNMK-rID186IWpkGm9gzneU9nriGomQ73KMJRKgG3f8X0vI7gOOjYZknb8vBcEZmR00fuwpA2vNvsHINhRmkFUttoIn3z5vU8zxvgDRlY7ovkHyf-Dz1zpf336criFlAr-l-W53NQLmBdCNDjHc_xO8bpj5-6K5yYEJeG7aMrTnyE8dIhRu1bcRD7IpDYvRncGc-bXqErLuhL3Fi793udkZCEluAhC1D47THnK8t-aEI8i-vXpdiy3J4NI3kEdEFpydjojFC4WZaY5mMFkfxh8mAZbDwDg-gKfAvAv9E9Nf3kfPweW55BauFhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
چرا بزرگ شدیم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102640" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102639">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTIZAy9ZTRakw1YxTvOYD3GSfikl64AOyC9XrWeMinDws7OVhHEiCyKgxoOj3GezBlyouUc9_Pe3wnwj6kfJSFLYOxo4-ja6sluA-T-ogmvIv4agNEvxdgwpzmDMizoSDHgVIbqbCmcCzt12vhQqOJxhgb48N_le3mG_gAdgZ2WbIKESqEUSwqJBi96a0NKLZMy5JJbJKiFm6IlTblyDDju0dvFOoNmup7SUdaxzH7snlAm1j-4Iw-Wk8mp0Rc4DVjgNGBhJNVy3Oq9qNHUlCvfzjujYGWOaO_qlPelt18nC-qyX6NWM-SwYAqmIKi3dfna7UlX8OUjgmgW0GR-jBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برناردو سیلوا : رئال مادرید بهترین باشگاه تاریخ فوتباله، نه گفتن به پیشنهاد این تیم غیرممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102639" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102638">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC4pYrDWA4Ifo-DAdwlVvQRgcQiorzAHrgh3DyA0LQktav4yrooy_LKRCsctSPdCU5NlJxyPmOaDjO-7wRV0aOflfeJgOPtzKsFDDAylgtj95rBxvx3O6RVr2X8c3Fo1KLQ0kDwfwG72miHYoB9gy9uSCIQ7m5blWkz5UTDP_Kl5HkBAwj0jqngea-p97GaarsuaKoueWbnAVjbQfEuAY6gvb5f-hCUK3_LwoYUQ09bZTgdFjKW-I4z9UQf2qQUu0E4Nn2pRNEtt9PtclKXcmEX1_u4qRAhhaUW2A56RzkEBJsGcDFlRcjUr5BPiZ8jFRxp1IiledudYoVFe_vqjWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102638" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac45ed94d.mp4?token=i4c9krYUGlryEiQlz8WBm2PNnl-rh0ZnwmJspHdiSge3jjfPGiMAc8W9AsIOopvi86CKDQAZ6fuIDbFzXtuyxkPUcFexvt3XhmB4q6zaC7fre-VCf8Q1DODIcNyRhOEy9bTLG7osloD-CWLTnl4RpIOCVifHPOfEn4e_yiwKhYE4gP2gQcMHionbgmZZffYUgX3X-AcJsCkb8tPVky94x6Qyzsbh0wlcvLv_u-kEK1WGZ9pS1PahIynA_GNLJRaxxTFLuWY_yXOCPGwL83ic1fnJhtomTJieWzQDuQ58n8nTTkBemPGK_iGz7vbPcPDZjfk9ClaDmwMyOEc2R_AX432RxXVjXYx9UA3i3mJseiU9xNKX46ReIYbWCMuMYtBWm2DikoWFIn73VEc6BbH8ObXhQ4TceZeBudUQNk0yRxkLV9NPJyqLOkultPIu7zWYliBOjubo85p49yTEH9NvF0PJJzzQvVHBCs045LNTk1SELDDmlZLda_lL4-ON5EnDYfZgGYdIuXjey6pWHtArsHWL_gxvnCByziDA4CRCO59vJsKobuqnIzVrt2ucNDtuzulSS_bcxCexKUhihXk_IIVP4HfLUsHNxxj5-x4d22FKnBk7h1j0rainFfxEgNE8SL2d53wiHyRsJghrx7eYUAduFi0HT1DubPNG56LRoW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دوران پرایم‌اسطوره مانوئل نویر در بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102637" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102635">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e7gT1QiNqLKATi9zuC_NKYoEWaM3i9kkSo4OIRWZRf6dcRUZn4gQKULC38QGjqL3OkeqUYuWtH5di4Oz6spTFqYbeJyylV__ZQxWfI5tkraFnLu1Jp3ZaKSnok22ABacQ3PjsPhU9JdnMgdPFJJ2o4nSVWzYOq3dwQBDzUDw48g0yoz-lU7p4GAHS5PH3dn2mJHAG3c7hSLPPuXlT5GxWCUgqsfVC6cKgUZ7-roduPmrGVdrH4JaBbeTrloaUvTYtZYYnqjP0-pu7cvX-D95nRKM1Li1kjsZ2v1zVV31Akh6-daSLH7edKpfaP_0H_tb0HXRO_7H5Aos2zk5gabsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UAfdqxt1D6Zv-5lQmh-q8sigVOHnQHg1yXi8TmF9SPn8tTRlM14sgRhREYzL-ugJ_TQ93z7bzqDORE7w-OahFYf-8XHeqR8G8LdiOQj1uU2MH8rGogJykb0PK-Kw7CaVcvNnwFIJ2fMGfpq9fjgyy1PnNHfb_PgF-buAOLPBgUuwOIxtJsexrhDQJREV-jrROq2Gyl53unF1Oi7wC-Qyf5uMDYiRTelEUVXSI81fKHs1KZzH_4fi7IqZigiEs6xrIoj6p3pMIYrVLAb1d3X0xAnwdiI-40c2FLVkIcmJxW4SfGvChriZScr85VxF_beqChRY40wL4bNVYfWf5zhmTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وندا چقدر چاق شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102635" target="_blank">📅 21:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102634">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbde7fbeb.mp4?token=LkzpuNqKiSEPnPy8WjyZsO3RPBYfRr74GMZWwHBS-vFAEWrtjATkgctxuldnPDFNMq8pBQwc3Z6BuasmnmOv_rVV4P_uMdrgF7RUBOPKiXdP_gJwU2aaD1ic6SrQAHCy9DSBd8ysOjxj-hSUnyJMf5Hcj1q6fnq1rHnB4VOPmj_-RdlKRO29DLkyirObDkOpSKDPLvYv2vuZSAeXJtarf0DNvo2wX3tr_fKPxSlvkkzEt17LqWfKL0s-eNMH64lsqNRTYsN-8f7OX90mDAOsub5Ed8fVCZ9eFG9LyXXL6NHvzjyyFEccMZcTIQ2HaJC0xQfbQGBf4XtiPM_dWi0rkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوانین به ظاهر ساده فوتبال که نکات کوچک ولی مهمی دارد و در لیگ برتر گاها داستان ایجاد می کتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102634" target="_blank">📅 21:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102633">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=uoc1QVrBqZqyFJxeGIZ5cwFS-u7EFik5VQ-bSjw_uiWwPrW17uFsagK-9KbleEMtBnRmt1a8OZbycWE2Zzf_qFzpD0jAg0R93PINEYz1AEW3z9ja2rdILt_cATTM0YUk9DBm5HuXMhBJq38Ixonj77eKov5nQAFMu4pDPzEc607QdfvIOWcKd8O2PjXstaWT0uiqc7VLtNOpxvASknyPjOjbu0d-9pT907C6sEPIVy9VFqE2vRy6nZRko2ZQkpNjakWfSmjhjwiG0oWOmJ8talFT3VbBYrO9IwzBBtFnvgx-mRKbdrNaLApdg9kIBRYqzf8IfZgv4ZMIP_s9fnap52ozjZ-XIiLZuwBOWf4Rmh0nbJ4mKtgDKiPH4KbBy7RObbLUn_gGGTpi2pfVh8K1MzBpbj22sWEtJm7I3RlZrT_-z7Krt_LHK0WY4dv5mrcmhH17B-EMXQqoRrW_lTY7_id3sq4T36F04ndGMKUqKgYm8-RbRMTj3vb5-M9kXUhpHymsjW0WKCEYxuxLmVS7_j08LrG0lQL726rFNukfseBr-KmYxXAboA7FBtxwz9u5Z7w3MPXiqIfTfXiMs6jkuX2bsBpnPYBV19ZGL0UPwjXCMt5LWpZx6aFR8fXkGJcJR_KAIg8JbQtNiofKUUn96elLxsweuz4zHGgszB63HHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b862859bc.mp4?token=uoc1QVrBqZqyFJxeGIZ5cwFS-u7EFik5VQ-bSjw_uiWwPrW17uFsagK-9KbleEMtBnRmt1a8OZbycWE2Zzf_qFzpD0jAg0R93PINEYz1AEW3z9ja2rdILt_cATTM0YUk9DBm5HuXMhBJq38Ixonj77eKov5nQAFMu4pDPzEc607QdfvIOWcKd8O2PjXstaWT0uiqc7VLtNOpxvASknyPjOjbu0d-9pT907C6sEPIVy9VFqE2vRy6nZRko2ZQkpNjakWfSmjhjwiG0oWOmJ8talFT3VbBYrO9IwzBBtFnvgx-mRKbdrNaLApdg9kIBRYqzf8IfZgv4ZMIP_s9fnap52ozjZ-XIiLZuwBOWf4Rmh0nbJ4mKtgDKiPH4KbBy7RObbLUn_gGGTpi2pfVh8K1MzBpbj22sWEtJm7I3RlZrT_-z7Krt_LHK0WY4dv5mrcmhH17B-EMXQqoRrW_lTY7_id3sq4T36F04ndGMKUqKgYm8-RbRMTj3vb5-M9kXUhpHymsjW0WKCEYxuxLmVS7_j08LrG0lQL726rFNukfseBr-KmYxXAboA7FBtxwz9u5Z7w3MPXiqIfTfXiMs6jkuX2bsBpnPYBV19ZGL0UPwjXCMt5LWpZx6aFR8fXkGJcJR_KAIg8JbQtNiofKUUn96elLxsweuz4zHGgszB63HHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاس‌گل‌هایی که ارزشش اندازه یک‌گل بوده
👀
💥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102633" target="_blank">📅 21:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102632">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c26f6b0dfb.mp4?token=vRU554IqIuraZ3s6R1ZghHL4i0mR9PIM017-e3Z2bfrWnFq9gRp9RFBZOWtUt_5IJaP94oljIYYGp-zGFkDnhMWdBISMVNJoau3c8yleqZfHQSaaWbROpzvs9pLJeafbiOnh3pOkVo6qqjgIT8oLUUYQZoPmPzXJM_0ADNtd0ps6XzUTeDyaqPibxBn3zuL-AIXVLjTDix8JGH1dp-SkRkWje7zEX_l71oniJcBFQqFfSuj7qTafvxdno4Y-6okFXo9ucnnpabl6Z7WyDoua84bQs3eMcUXwpRWCwSm1SVItsGeTFAc2ptDyR0L2ktpGwBWBFbjUn4jO6-s27r2sIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فران تورس درباره آینده و باشگاه رویاییش: "میخوام خوشحال باشم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102632" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102631">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRn9Zwurded4par3QENiQODDuEBbdTPBt6N5MN-WyYGz5si9tgoOOLTfvHtavxvRX1cLUKqz4vRVoUbwjIncxcla2iXPSvaPdKSProFb6r0UDfl3nzVUuwfRNke_t6hsAJ_-iQlttzOi2Ddd3J4IoJFETOQY6xJkQizN9PhSe4SxK8MYSofXWdzckU-qREh59rjE_Z7yrZl5YjHz-ysAFQ78MnbLWFNn_ZT8MqfuhygRgBKGFMKxc22xkkKdUGNxrhyoj5tD5atc4iNszR7BO824sxF-v3Ixcd6v5esM-7T0ngMYz0WA_Fd5s5ZM8920RD6glJPn_tMrBszYk4plSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇸
تلگراف|ترامپ تمام تلاشش رو میکنه تا جیانی اینفانتینو همچنان به عنوان رئیس فیفا به کارش ادامه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102631" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102629">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3MSHLdEA93RxTZRq0k0OwRw64pmHCfntfS_cB8GzQdllWsHAxsfIgqsydAvqMb4WtuEp-38JZGOLVAe9HzsgYSyczClys2HF6W8Gztewc25_OBuWg9zRL-Tt_BMXLyhjWmrMJxULbav35C50gChw_LaXs5xez9xBjD4M1HQoR_gD-aUFToRgtBPLbZ76Se6CgJgDgq_79mgqoBTnWT3UAeTFUTzgi4wYhFXhsyoHbOrpqyeoSGy5BeivgJWp0Y7bbQLzePUcAaL6qQe2QmOFswaQAlMcRW-AvBhryqkuV5ILHwvT9qym042MmfDVmc2xT7HXGKwF51fRx2DMFsDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQT9816BZr-y___1Zcl1Nv8owJg4TgzTJdm_12YJ1zOSzxMT3aq0eAdFn9r6DgOBug7d42XJE8e6Q1HQYyEf0h-4wBEsbOUBqxd4AXl-KMmhpo-I9RJMQBHmw0bC5KQ1eGaFLtXSBpm6-WmpMgEHGT75ac0smzcIQsIRWmqa5aEDISqucZdxjjMU6F55mfFXF7039BHFSjipsDMvuYB9C2Aog28KGoPQZQy0QroFmLTUvREw0pnydtjxtUwM_QLMj2ppNCK0hRxRo57NJdgOHK3rb44exNsr_y2TLyrKXR-M8yZ0yOmPXdW1tClkLnFOyFyJXUExMCnfdvUmShKeGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
حضور مودریک در تمرینات چلسی بعد از ۲۰ ماه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102629" target="_blank">📅 20:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owx5XO6NMefhBIwQT-6zEs4rLexupecnmfet_0JqDODeyGwu_n-zZnEiWgTeYg5Z8FXCK1gKvE6mJbQatc0OtHi4CqJH_Tvk1nc49h_OPNL3xpwDpK8mAvN7PbGA2zXmNQcGcs6tVCP7y7Z_RHs9lOscypbcYhzizgtGSz_QT47DbRdtz548brvqfvrNOS72D9WRRwgGk3AS0HJilJE0iL0qMPI_WtbjIT_J-i3j8eLV5MnsbnRaQxd3vGIIRr-zBcYiAnEkYu2LQ1INeRGe_FYxrkz71r5Ljy2bBC-zKPBcjpWWM0PvGHCdwqDEhryH_OmBBWdkbecOVyUr54FBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pXyRH4BvmWjGQB_0vBf3MFFW9OJo4AVDnG0UgRZDjkicT2de07iSyh2Npec8j-DW9-xdv-WvwlFajkgKgprOAhqlIogOhQgUbKmAlqtFyC6SK4XRE_vpr7IlVHb8my5tl9Wkqdrad77Jz488EgLF_MU2d_PZRK8GkDga5z0SfY3Wo721oQ5MDu1PY7GfEgGCosSO99kO3nWBMXjD3QOzVqCISGPH-0DVVHX2f3tUQbutZWFZa4nfVQNwAzhtsXJAzdAe1Ex3ycZP1abvMIuFtWPqlteIJriiwwWBCw_bghrUISDfk_IYGIeoaYlKoIKb6kb44kW623LOvehA3iWC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
باشگاه لایپزیگ اعلام کرد که پیتر گولاشی، یکی از اسطوره‌های این تیم، به ویارئال پیوست.
این دروازه‌بان در 11 فصل با لایپزیگ حضور داشت:
- 362 بازی
- 117 مسابقه کلین‌شیت
• در سال 2016 با این تیم به بوندسلیگا صعود کرد.
• 2 بار قهرمان جام حذفی آلمان شد.
• 1 بار قهرمان سوپرجام آلمان شد.
• 3 بار بهترین دروازه‌بان بوندسلیگا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQcQLUGi-Sr88dgpO_s0h2dNKiVzoM-SFk0tcZ8wqnup8yBYjlrMb89N5DMtlA6-5UVLVS31Tzz3yqfQpsNPTZ7N_S4i1psIlfTYeaVJx7PRWcs1nYpETrn92NVBb0_6yrrLDwNswSOGnZykAJlESpr59yiuH4druKRpQXm2m2Y-LxMNdCJOQTeqM8nWdWiCUOx8ww_2h-724GPh5T-5Su3vqjWhkY163KAKG6opujPqDdoGOe2ID-hEBE_uK2srS1JEP8x8-bmxXlfuoXeD-3vx8k_ZNM2tQsvYCBesRwq5CPY35ocnDdP4TQloGVMzVOGFXg6hN5M-8ygw7VPzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCAz7t4jTYD4buu1vpnvFphl5OYcOzqjZPgvcDFQoO7AZAn_mYSuSRnXJW40c8v9usD05q8C3ufdbZBkZDsjAnnG0WV0IDE1UCb-NzaeVPwUKUdFWCSNNMNnQeus2z_zkzz1LkLzBzgVjNEfFTBi_D4n8luokoxcMempvTrwnnbcFSIlKD3zc-DLGFvH6egYEkbCCy-Eu8Z7gR6T5d4zzzmbKx85SOzYDBDvLq-jfSr7OK-ePMBg_W5AVdMDGzCRGHOpZthcpdmc3FTDgy91HudEX-ddWhvI0ql3MMIfx8hYrdlY-Hzfzd-SImwEc0PIZq4UYpzsbnCCiiZtzt9UKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102622">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBIEA_HyimysYkoN1OPqa-ySsQ4dkk5VklLOUKLtpc1QzG7BmSHptD5U19EcQOu1s6SjdZvyyZQWS1HWYBaOtG1xSIebTkOZnEFVXVro8oB4mHuu8xtgLWBA-IHkWcYg26OOWvb9Ar3zIK9auFYwAaP2I2psR2BrwSRYiJ8kccWVL1OKzL0UvI9I2LW0d1A85ctSWkU1GiO9RYuPNzEsyc-awAS3hya-DES8mwUbxx_XFBlL0OKoKtr5LUOzgJ4gNMr7e0MaUAFX2Gwi27ygNoB7fJjg5EaZQJ2yvh_beT32qtV_3CmwtgZIUB4yv7CnOVQLPItLU1w9-EltcVauYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مسابقات سوپر جام در ماه آگوست، پیش از آغاز فصل جدید لیگ‌های اروپایی:
🔥
🏆
• سوپر جام اروپا:
• [
⚽️
] پاریس‌سن ژرمن
🆚
استون ویلا [
⚽️
]
🏆
• جام خیریه انگلیس:
• [
⚽️
] آرسنال
🆚
منچستر سیتی [
⚽️
]
🏆
• سوپر جام فرانسه:
• [
⚽️
] پاریس‌سن ژرمن
🆚
لانس [
⚽️
]
🏆
• سوپر جام آلمان:
[
⚽️
] بایرن مونیخ
🆚
دورتموند [
⚽️
]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwJueIpBSmSfl8eoUsIt-zRLfMN4oB8zQuiWMP43Zl2nJYPtRQ6Uq6p810_sF7X3Nrt1GuYB4GwCPLpV9WQtJNQf3R2E5jOZKGWq5mOvJaQJnPghuTmG4M9ix3RzbE86ewLtPtAqo9CVYt_BFH-ctDXgNC-3GdkGQSokDKDQiM21IQoMKkl8yPdeTH852GmO5NRd3gaLdrOmY4BcH58JwnwH0RA4K-eIydwUx0dHRC8YgfApXnO6LZ9ylELxWlXu45xEWk0okOUx_cgrBuFYp4-SammqTjC8AAq6M_4jLX9-0VL_OjTJQcDuaW41f2kTiSzMFb1kYbEjq4iY76ullA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری
از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnyKCdiK8cxNLPDT-sk67osyULAR2zL9x8tMjkF0zGr8wuScyby8nG-0-SrZ2V2lUZwPn6mj3lRtJgrCiC1_nFZfi-K58kunEaDJG5ierYotCfOQuoXy06Vos-PtOJ488RAmMklU3S2qVJt_Gz99j2Tzg0637UgCRvWlV_2kAgKs_UM4ufDoWSSeTSCJI-R2eg-eVL8QuzIvK-eMNNiKZQlB2C0THI09aWd66a69WMVwOoCv6ZF7Uc1oq1-OSu2YpGKOJVbIIxDnfTe3qWDkCHhLmAg_nAEHokzuL0rl2znD_r-gcxZFQYGJvRcLMnBPraKQ1-_5K8U22npKoKbfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpkR0Ki79ECeVNClilmNuAe_9pBUNs23aF-nB-tSyGtkVU2Rg-FdMEcAI0ALm2UJ8VpcmrSXa5bHJS6_tbqMtGPkkEM5V9tjxg1mGv1TvYuctK_cJvoT9rRWKjuc37yjVh2XbGKXF8zpKh-P7S_EUCJEXaizgEGTQWzU9by86fTfzwQHfSLMUa6-HWraS6TdUS-XgqGD0dqwG2LQHB7cEjsPNT-qTenT04xvEViwZ0x43jaze6HsYt1JD8U5QVBWZmvSaIlUO7K_EMvbz3PF-Ym7BCDZ7GGGC_GUgO-_w4OSe5dBL4iJogotK8qwBd-n-AwaR0oCq6raoqNZycRU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElJJIJaPra8QlTovgUAtvbG7eAnZvDwLenwfwSTihsP7PgOm4lLQ7S_aqTnHO25JIQWRRtw8Is0a8KlYPisYsiod-OzbzE90aWcU6v8aSHUG6tTFCMbE0qoiKJczkh3Uhtmcb-Ci5t2N6fDQK-7qc3L697LS9j9QUiYNPHiRiPUnuhfwKMOiTUGyjjaoQ-IPYHC85Y8F43Mkkn-PzNgstRKANsJTtaN0tVidMLyzWJk2NwidjMDcq2HpRJ3pfojxicUn9vpf523vxRd_Vrsav4TazvIOcwetFpgdCpzUBU0blzeVi7CQimb5cOhTuZOAhG8PHDbLbPOo6tMaJMzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP5xTQOq8oF_zPg0NSJ8spYtig1t3DDRAkIozDgcNRN7sF5cMf7QjEQcs-flZ1CKlcv3uZJVAcxQTZvMLeS1ov8kBRG0nXLZek0a3adT1bUHXJdUObWtB-cWg3DrYiTqdAHRMlOUIk8Ue_dj97cP34xisjQPYGuub3K50hr6eIl6oUe39pcfFUzPNkwvv6kev5nVOtRGqr9QhBcjpcCO9dO5_6pL3jrjhNHCGQRJDFvxtXX5PGcC8WJrSLtOCx8UcMnWt6-v0bo_aFkHV2KkiT4B9mecOTUSVOxL4CCfNAwgd9KvvRfZ1ulDdUEvK_nbLEzCgxlKMS7ve-gwTAJ-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2wwmUjIWLWRsqbJlCQVNJyzRo5WfK7yIOPLQoKOYRjR-VDZRYXWftL2APTK6IclJFibmlP1HVDGO4m2bpPqYP_yqwnD6NLBwQ0Ak2x6QqKc1tjBpsPig1wmJKp1hnYHFgKHsvazFcYHVVdfoZkP6c85CXjjV9XnFxZzxIt1gfVDrcw2O_KxURgsT6usI4v0LmFNn6UFe1vAM1qi2OGXkK4xcrV6Ye4oq1f4Jce_4Gh9BTch7WDCQbSRlvocqEYB8JMOARNIqSFZSw8tn7JXLbf3MwNXFVkQHmw7QDWy0WNxA_hVZfch5vGzKGyeWIm7Jmuc5w7veaFseOzr3HVISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidWYN-6zHdaT6ZPr88FheyDZpRkdvIwOoTuIl467SfZgXqANhXmEtMgL_e_qmiM6vCphsOZNz-ZEo340i_gJ5e9iVU07xqimMvQ8tJfvvHMC2NsfxBAU8utSvekurgTqEVbG-NGGH9XYPlsapTKugbo6CPqSDxUUlQHGx8YVOdltFZHsX3fgHryfZWcWbTR6HnB651w8vJTQG4Pxb8Tr59KsbvbmiHfe2_SlCfT77QmYTIF0kZuulmhQcNog__QoDVLI4-UZq6QadGs0jMvPHTf5rIUNIibL0Fc5kd7RXX5b6WJFZRDkZivw2nWjDjf-8WLMt9979fXz4Hkpwk2DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_kXsP7oGOktPjHpQ45mv_b5aWUaizAgwiqlxH1P0rGzwXnBJ_GEl_vvai8k3Kk0wu4GQ6zZ4j4fwvf_94PAVKnzFwYBr3Eu5PpheZRKQt_jTkJywzc_dVhyzkwqQsTh3vK1uhI_Gc77tWzWzwT0dAloACGTZfftIud8JLhKY7a3vW-kFBxXMJlSeS5iLL538SKuqalqFTCGErwv2n3Vf2Hl0qnTdACmlGLIG_EDglzoQwtwR9aRwraUg2eTkIxl0KDmVAgNIyy2WHvwZltG1mxy-_rhkuHbAD92UZaoXSEKmvKlYEyXVCWoYBkKPZlqz6H0zE9Hlj5QCeJHUdW0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=CfnOdheVcUU4UwbJFHiCpIfY2nyf3qTqidSi6dsKA1UHUdvlPuPtpz2ppt8scy_vND_VRR0AmsRgG0MMkyh38C2-pKg8tQVByUWOY63ZfRXGZKsp0VspK8yXlZoz8PgGlgfzbRaQXK6WFIE5y-BtjpUc-GeDa_bZLFSqxrCa94qHfwX3RzRxtafEEWbCznOBDfWWCBFWzOAFkoUOYUu2oSAiP5badLRvsAuzRf5073Hv0Ib005sRsjsv3yjCFnSq-mYlTATzYOQo_X34-YUWdvwoMm0HVjQvMo5mg62EHxo4CjLOtnxDG4Aa5OtpWQ-zpU87b-7WcWV_rhQJdfDDGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=CfnOdheVcUU4UwbJFHiCpIfY2nyf3qTqidSi6dsKA1UHUdvlPuPtpz2ppt8scy_vND_VRR0AmsRgG0MMkyh38C2-pKg8tQVByUWOY63ZfRXGZKsp0VspK8yXlZoz8PgGlgfzbRaQXK6WFIE5y-BtjpUc-GeDa_bZLFSqxrCa94qHfwX3RzRxtafEEWbCznOBDfWWCBFWzOAFkoUOYUu2oSAiP5badLRvsAuzRf5073Hv0Ib005sRsjsv3yjCFnSq-mYlTATzYOQo_X34-YUWdvwoMm0HVjQvMo5mg62EHxo4CjLOtnxDG4Aa5OtpWQ-zpU87b-7WcWV_rhQJdfDDGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6c_9DXIsB0OQBXzreDu9ANCZltLoqMu_fqNbuPhqygZERJqTpynbjf5bOqcD9Ukyprt7mh1Yxj7Mvif8JIoyovB5hCATgpcVUVv0vCH6ZLG3-Bvvn58RsX66tA7Y1-4Nv-VVEX7UFZxJWuNhUO5run_uOaP-kxMWKIF3AqBDIxEvw4T5jRRK8ULph-IbFRsnWL3BEjBf70USJa2csZaRH69vYu2fOjwola5tZauVB3Hb9pzsUQuC2dnRQikPHRorBo1L7mNsN_A79CiYMLEpGtjIS7w6wN7f9rRkW6e8epufFNhxpXgFbxrdIdEcsFpQTyBm-ZQCIO-eF31wSq5Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=b2S4itRYPEjzotdreSIBNpYg7jCMP8VDq26VenjBTJJmb6JJ4miXKwagrlMwJd2alXlBjPahfLQ2NCB-arXN3id-0IdCFhkYGcKEP2nBs8yiPrW75mfIMnt7SZdWUwdzc0-iZWb2IXilh5Mjc0yqQTUSxJy6VQj18DaMRTSCQ32O_9JBjBp5aVCh9V-FOA4w2G0TO8sGgkrzF5yvcbdI8wvsXpT0sjJkpvhFNAemR_cLnkd_SDsD1i_YbzFd09b6cH5DIHD4xDQPbLpl_EH4sT51rwldCstQSY15Freu9wpoQ7KnVqYSlIQXJRC9Qn6iSNOlsTKWghkJwk3CqDaHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=b2S4itRYPEjzotdreSIBNpYg7jCMP8VDq26VenjBTJJmb6JJ4miXKwagrlMwJd2alXlBjPahfLQ2NCB-arXN3id-0IdCFhkYGcKEP2nBs8yiPrW75mfIMnt7SZdWUwdzc0-iZWb2IXilh5Mjc0yqQTUSxJy6VQj18DaMRTSCQ32O_9JBjBp5aVCh9V-FOA4w2G0TO8sGgkrzF5yvcbdI8wvsXpT0sjJkpvhFNAemR_cLnkd_SDsD1i_YbzFd09b6cH5DIHD4xDQPbLpl_EH4sT51rwldCstQSY15Freu9wpoQ7KnVqYSlIQXJRC9Qn6iSNOlsTKWghkJwk3CqDaHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=h6KcY7t12u9w0aJcYKbp8ezVwiQkQRVfBlcMQ08GJvWdW1wNCOLY89PQfDh9hAeJZc5NuW6iWf8X7eg6z_oQSQ48NsG_gNvMxDVNUre-xrZhdCNb5pRwBW_h15t3AlG6jI_uj979NNsFDeBqBP-ZZ1JngcfRYLy49kWBKLBzPPb6vfjNZpUJBjjM9wBXeFgkDiqeVboB50XG0Fkf4xsKHZrWPNVaOaRqwrjfN6f_XlTdBj3PJh0C79bTAvIVMXbbsbYei-7ZwlN4l8Dsi9mKRVg95qofvysICGBbrUAIO4IF7ADXeWCDHSLXC6XTyC0P6XvWFCa60R7fdSE6KRw0lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=h6KcY7t12u9w0aJcYKbp8ezVwiQkQRVfBlcMQ08GJvWdW1wNCOLY89PQfDh9hAeJZc5NuW6iWf8X7eg6z_oQSQ48NsG_gNvMxDVNUre-xrZhdCNb5pRwBW_h15t3AlG6jI_uj979NNsFDeBqBP-ZZ1JngcfRYLy49kWBKLBzPPb6vfjNZpUJBjjM9wBXeFgkDiqeVboB50XG0Fkf4xsKHZrWPNVaOaRqwrjfN6f_XlTdBj3PJh0C79bTAvIVMXbbsbYei-7ZwlN4l8Dsi9mKRVg95qofvysICGBbrUAIO4IF7ADXeWCDHSLXC6XTyC0P6XvWFCa60R7fdSE6KRw0lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyyzfG7_7fSr21I2BytNQvfMmputyodIEyAbRQ9m3USJNMTIDmPcI58p7tb7oKkukmVnvvEFG4lEx0S24Z5swS8x0_zFlyWkTYY5_cMytJmV84JLcTNmAdmnPjOgVqhch42H_iZFtMANHRGAA_PuJ_WQHneIAG7iUixRbxAd8Gj836oCoz7dYOFTTTbPPojma4LTwB5VjsBYJhpuaxlIUrQHT1_j4RApX7U8FJb9gVNgC06O9nfZBIDrwflNWB5ETL9jzbfJW_ZaxJeJr4gxZ36PCWrHSlUU_fJAtf5IQ4RDYdocA01K1_oGzzcYsSDC3VH-SlvGI9yKTG-zk9FXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GVP3qBhEuFHJw1tmdWfo3-BAtC-v749G-ICVtdnMTqWN2Mhk3rU4unRu1NO2gS5Z-3woWk3Szq5_IqqcU5tcViG_cBVcmpEhWunaNOxNf6-74SUXjXKbeeFhNDUOwkdFT32IeKXgKCbvmKG5NfLB1y9LTB0OmTI6oo5cSb8S1PgwbFXfQAFXZefOALIpahW6S1hE1yruAz0x9tiXNqXf8TX1JRxRCS8v1rTTVkvguPWBBWBJn69X94oHhMncJECenqSLvEt6kmqZ2rh8-GPN50z5JNpviRJBEhdWcDQGo3P4JkwLwNR9Xgnet-A_5fPc6CaBlPavQ99cXjpGDdD2wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4m2Vhha21gLH9xJcaaXDC5QWmSAsVAcLbnoEDJ80KDa7Lm2YDckKG4nYwf4Cke--bXP3XVhvtKCTR1fTg6Ubp2IGUWSSOECqImx0pAwYj2HuWMQN60rI2aa_LPw_y4kyd6PrubaurFDDQPA3ivLBPOaN2ANB84B5IZyVeKQmK3eE4qKchnvzzLh3JwfFwnofz1nRh-EK0CRufIIIu-E9doDQjz2I9jjH6k348qWKlwc8KUYnYfQTc3BY1R6r6Tv3CjzLBFdBPykyvD6NlXRojc74oseD9_RvQKnUwdUC4WQA3FLnKDiUcCG2dyx6rDUs5k0utZ_jqyUoQZAxCCSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxSzOAv9Y-26PQvKJyXhlQyCnR8JtOi50tDd0qUSKUDYSlt7xQPpGEMurQYqXnl6zde7cC2t2xbg_ezqkYaC7hGGdcoRgDI50hPTyXsSI9YnifROUDF0uF2Yg6B4nv7RmV79fKK4B-c_b5mzbAqFrkt8Tpr-_7ArQuNzqPPvA6pODzXLCAM2gzq827xfGU-4r7ZQPXE_ObQyhGWS8GHa6ueT9dKismeZ5UXzGzzbHaw8geBoQwXAnRAfF8mWHwQnJyNjT0sp-Zi0tKjOe3r80YfYanjx7WgT9IiCYXMBdwVdUtwi0TQoamFVYacAZa4sZy8RXpizuORdmqgFwiJ6YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv9ciCdr35efEW4EAKKXywPxu5VXDi_q2E5VIT0htDgfMhdcTLqLmy0tV7dhyxiW-6UaceAwd-8gJtlEFDWjDfERkoPDbg5gWE-dKic2VCgMZgaucIJX493_8jge3-PHUyUUw8glteo8s5fHrxtuDgunX9RZo7n0sThBuRidEOe4ZCJpMmic4CSgFCz92vdFlBwOQdO7DSj1C-CdXvRZ3v-LFDfmEkSrRbUITRTmYwHWX66CUZOAVX1l2GHaNrIanMhXkycJ4D-icE8AjhcrhYFVYaHUzH5t64u2hvyW13A1AlBEkWyA3ICNtI9JTpHKG0CZ8GLgLy1H6uLrklCEWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkQcb5rJdg7Dwewc33xnsqWxhUwzoCZ2DhPVJQDgheenRU3A-L9viHsyn2H0Eiw-3ld4XiAuEIVJYG15FtNnku4Dez0NQSwPoMF7mp_ccU3rajiX8rvje6iKDJ6ccphY6y5CCqRXwafSgh5il5VPO9kvWAKveIN4lpOBoETpBhhkVDddf7-yzMALmHPiY8-0jhQxZmBWYaz32UslYAwLOv1JpRMgNq1wyhGMwoymVsm20OcYVvxx-Aw_X4p91OG0kMa1DJ2UA4b1KbriPZlxPb4KGM8o6dD3OasgtFYOFpDnXHHasYlS0PX0DFPXxpW3AjsE4VvCBw0ERK_JEUVN7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=oF5mY-CuNVVE725DLcp3VGaIwrkv0vHJR6m9QjVQ42_UwbLE2YyJ8gBBzcLqZEvjBrl1dBiqFoKBbBGTfrRKhMQtz7Q1VxBoy-ktbpGYzbmgaB3GAqOkDiW2ugwIs2OjF7nduePkxjX3MpVH1zFx7act3wUED00OmTZykJeTQAE1ZWA8rSxrnRhgfwSW4wZ9O_TUXoGI_l7oaPiDFEwjo5hNCMjH9WF3NvYShgz3FjzmUpwmGwsP8S4DjpQY4hse2RdLLNFqFn5uld5pAJiGIaVDaPFCqzFN7Ljqu_L3XfqN9eeoIuES3OwSWbw1rDgyVA4cNlnMkjs56bR-kjEf0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=oF5mY-CuNVVE725DLcp3VGaIwrkv0vHJR6m9QjVQ42_UwbLE2YyJ8gBBzcLqZEvjBrl1dBiqFoKBbBGTfrRKhMQtz7Q1VxBoy-ktbpGYzbmgaB3GAqOkDiW2ugwIs2OjF7nduePkxjX3MpVH1zFx7act3wUED00OmTZykJeTQAE1ZWA8rSxrnRhgfwSW4wZ9O_TUXoGI_l7oaPiDFEwjo5hNCMjH9WF3NvYShgz3FjzmUpwmGwsP8S4DjpQY4hse2RdLLNFqFn5uld5pAJiGIaVDaPFCqzFN7Ljqu_L3XfqN9eeoIuES3OwSWbw1rDgyVA4cNlnMkjs56bR-kjEf0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=RdJBwMyhVPdx6MOSJUIjwCZtEXWFykrj0kQljnssVL5i_CGq3Rl_YIof__elUguLtPEfi9nHjLealg5m6_LaHfS44sDfM6sGrRVUTje-xS0avw4CPX5ZuICfvrSUDFGablZDWZsUBqwPot8KqI0c2OlC__C8fmvyiqUWhuFv2Nu9os9XPT-C9rlEPzz_-LM-kxDDMiOFwrNa12y-aTAEAx8ZUV5z1HVzn0JFmv7YHNgpVbGl4kg8egLIaBgVLjUn6Toc1B3uWlwFQLCDn_VIXIkfmG5U-8wZ3leiekb06EcGKIVFD4AWQuA0E6XB6aru_iQfs2WuJIkG5BF-4V_RTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=RdJBwMyhVPdx6MOSJUIjwCZtEXWFykrj0kQljnssVL5i_CGq3Rl_YIof__elUguLtPEfi9nHjLealg5m6_LaHfS44sDfM6sGrRVUTje-xS0avw4CPX5ZuICfvrSUDFGablZDWZsUBqwPot8KqI0c2OlC__C8fmvyiqUWhuFv2Nu9os9XPT-C9rlEPzz_-LM-kxDDMiOFwrNa12y-aTAEAx8ZUV5z1HVzn0JFmv7YHNgpVbGl4kg8egLIaBgVLjUn6Toc1B3uWlwFQLCDn_VIXIkfmG5U-8wZ3leiekb06EcGKIVFD4AWQuA0E6XB6aru_iQfs2WuJIkG5BF-4V_RTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=tBthHAql_fOyEpsAOh67O0W84XQiKKeSrM3tZqFPKGyHZ70KfbQhQvKb7dIJajiqa2y_JCY-pfoHzOwzdkuqFEl7UTn_8U8zmx_eI4IP_UpfStDcDHTvU4XpB2cMID2jyYEXmQhaGZ1VHD_BA2XRrtIVjA9jWyGM4Sf4jvdnFPphxkz_UNRm7lRr4PL3zuiOVOAK8d61aq4vgMkEfMpANHxih9wuUCwBZ_7YFCtV_0aqCexm_FAtdI7R2PJ7zX7fO3HY88tddgx6wo_Vx8TVQEex24XXK8vbNhdi0a5oQ7c6sm5AUUL0KiONbO519HqLWrkZMhy4B6jj9jporUOb4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=tBthHAql_fOyEpsAOh67O0W84XQiKKeSrM3tZqFPKGyHZ70KfbQhQvKb7dIJajiqa2y_JCY-pfoHzOwzdkuqFEl7UTn_8U8zmx_eI4IP_UpfStDcDHTvU4XpB2cMID2jyYEXmQhaGZ1VHD_BA2XRrtIVjA9jWyGM4Sf4jvdnFPphxkz_UNRm7lRr4PL3zuiOVOAK8d61aq4vgMkEfMpANHxih9wuUCwBZ_7YFCtV_0aqCexm_FAtdI7R2PJ7zX7fO3HY88tddgx6wo_Vx8TVQEex24XXK8vbNhdi0a5oQ7c6sm5AUUL0KiONbO519HqLWrkZMhy4B6jj9jporUOb4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=iom4TKoOCXR44HzwO1YmLHddw6dD0b3yLwMHBjhaXisfuosRU_Xd6DXeMukILm1miPzNyqAog_wfB4v041J3JwrY1I-lSORUVgX4p5p7JInGuFCe6ZDziEFzmi1HTNsfdKElB8lBoypTu7WanBS_xqUqAPxnHuMMa11RYZTYGvDj62gW_Vj3-fTitOugXNPJZr_CkJFHR4Z86nbflANWL9TOQVwX9JYigdJSKIisEE6L-5hTENAA2X_C0PyAbKszqdN1S5T5cKF0p9JcFxW6x7Vq_IF0HiU51vA5Ls1Ly-9fL-_ewyLU7fbLwZAqjeTJXhht5ByeEM2VfoQJzjDd-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=iom4TKoOCXR44HzwO1YmLHddw6dD0b3yLwMHBjhaXisfuosRU_Xd6DXeMukILm1miPzNyqAog_wfB4v041J3JwrY1I-lSORUVgX4p5p7JInGuFCe6ZDziEFzmi1HTNsfdKElB8lBoypTu7WanBS_xqUqAPxnHuMMa11RYZTYGvDj62gW_Vj3-fTitOugXNPJZr_CkJFHR4Z86nbflANWL9TOQVwX9JYigdJSKIisEE6L-5hTENAA2X_C0PyAbKszqdN1S5T5cKF0p9JcFxW6x7Vq_IF0HiU51vA5Ls1Ly-9fL-_ewyLU7fbLwZAqjeTJXhht5ByeEM2VfoQJzjDd-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGNaiNHjSCpeDh-8hT3senb31FYo9CN11rqE6WG24nDQPgOA_qndAuwtDYO0kJvf5L01JhEk41A5KS-Mc2hETWTBni4kylPgQOOJb2qhL88Kp0QyWT6Vi34cRWs6fM3RXa35gFNHDUdn-j9PJfgiXiWFDRudAcW76lC69nHkcCMH1AWq4KG9y8zySaShVmAB6BNwdFgexMSDJnwJw-1PUE2rX9jfGUZt7dZp58fG4sVLOkSGESWmpUMrIsFuX4LM_Cy7-Ux-6vG0RTbHm7_TlxfX_VXNsMcxZQFT8Z03sDfasN2kiTFcfCYCspBuWmSO3xXPPA33AG80hjtIi-wpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-Lziz_YhlgNhiMRDJLZjYCTSxHOV2v9zDY9E0r4jAEBpaQAnL8s1_CXmqLFhg2B34s5FpDrPN0192FIEi2NNDXoHItxm4S8MeyWiPYTuE5MeGNstF8zXatMItfkYOJ0CXW35Gb8PWzt9oM320W281cpzb7gTeSBuZ-IJBNBOGOemJt9aYGhFnRMquj_2tZXExzmcovd7LNE5Mbl6xdXjX_CYY95C9dJwpagvBT67a17i9XI9Xgw6G7tcbABVF6fx2F3oimwur0kb-46NmDOTCn6rt1OfE3p621WVMGF3pzguBkOv_0Y0we4L2QsotEQcZFGiumXzw1gVTW0f1gPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3QOa5DuJbm63lcDu_R0E_E9d7O0tEZMC5mBb1EiOr-0bmaVucIouV6fyMAu3tbvmIGw-Dw114I34mRHeUm7MYZ-8ooP_xazKUreVIJYUAe7guwWJe7-y8bDBMoy4kPdQMH6cHG7NFP2pdKRwCCheoLP1YS_1c6FaoJlPHKkuvrnqqeux0utj6iOwlkOok7tgOT9AKZ-9ekDU8jry5P8d77I7w1_cO6vMQ7WUoiBVIi2rCm6dywZEzArn7AP3vvRMc27xwXbAHuYYZQRz3Cx_jvPyTRHAHjUiCLO3STaz8dwRPjqAVynxuGdtxRSBmmOrBvqSws0svj5hzHRnu8Mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=XAwZQ1in_579KPywC3aOMQSuzMGj5x4vMkWgAAfbvfcMq6jbME71B7wr-sh9-WTAXbxp5KwNtlr2mstIggRfdJYCozFQ6Xta1cPTEVaWD8JQhBgKgxwtHBnpXt4mpBF_qATRN__JyGFdJoy1BACJHBr378h4SOF3KAhImb6jEg9lWMvZE6K93OhCVitI1OPKiz4wmE0hFA0ojb96RKn23vHdrM6ouAaUykHEJPgaU2htMNtuweMkI7wrbDEMxf5TgxSqm9rHi3r-0SU13wuWai2Ho3EkGxX3Z6yUsQVy4B7fwhosttbGa3dFKttvbfLlfgedEl1Ogdq8jfspnh5pKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=XAwZQ1in_579KPywC3aOMQSuzMGj5x4vMkWgAAfbvfcMq6jbME71B7wr-sh9-WTAXbxp5KwNtlr2mstIggRfdJYCozFQ6Xta1cPTEVaWD8JQhBgKgxwtHBnpXt4mpBF_qATRN__JyGFdJoy1BACJHBr378h4SOF3KAhImb6jEg9lWMvZE6K93OhCVitI1OPKiz4wmE0hFA0ojb96RKn23vHdrM6ouAaUykHEJPgaU2htMNtuweMkI7wrbDEMxf5TgxSqm9rHi3r-0SU13wuWai2Ho3EkGxX3Z6yUsQVy4B7fwhosttbGa3dFKttvbfLlfgedEl1Ogdq8jfspnh5pKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=IYXNs96M5fVI8sWZ2OcfXUaY0yx1LjKhXYQWq5f4Exw7AtNPMb7mKiDH-TjJsFcv_vvCk08Oq_k60oPK-rP_aMKMD6QtlgtsS5Pn-8Jik3ITPdhaCzwT8tq7JpZII6oZMvNU6lvntuF0_LSerxLQyTcVGH0NctsWOQoL-M8QfY1XjXjm8mrjGEqHtx5VLpTqgyndmFDAypXc4fSeaMwE648E90lsvunqs52EgO6DGyY_OD8A5Sxzi4gsFtSEjpzVYR1aJaa6Vq809wo65RzjnGzY-MbQX41G0Ubpvt0c3_B8XTjakYs4f667KCYKcJfPl-uU4ZMP_hyxCCvRtIp7rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=IYXNs96M5fVI8sWZ2OcfXUaY0yx1LjKhXYQWq5f4Exw7AtNPMb7mKiDH-TjJsFcv_vvCk08Oq_k60oPK-rP_aMKMD6QtlgtsS5Pn-8Jik3ITPdhaCzwT8tq7JpZII6oZMvNU6lvntuF0_LSerxLQyTcVGH0NctsWOQoL-M8QfY1XjXjm8mrjGEqHtx5VLpTqgyndmFDAypXc4fSeaMwE648E90lsvunqs52EgO6DGyY_OD8A5Sxzi4gsFtSEjpzVYR1aJaa6Vq809wo65RzjnGzY-MbQX41G0Ubpvt0c3_B8XTjakYs4f667KCYKcJfPl-uU4ZMP_hyxCCvRtIp7rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TByjOH-svJYl-TgiI4XBWmmSzQrKIlU7DtPeMy9l4FVsIxE8yqJeLRzygAVYQNGljvZP4XY7u8a-IzqISpg4XyOjafKyINH4YFHTU4830ifdleKhRg8FP0UWDfF5uhHFrSdQ8uza1Hq4ttZcO5wJJ1eCH4gdOaFvOZ5Jj-fyH1Rsmrezv2V7OIbNx8QNajrbVNR5sG8MBrmA85_LflcQ9_oSoKGxE_30Fupsy-1BRIkqvJ1_5g7Sa2ETM5667-Q2h9dKKNW8Z_sGOgTMMG9x6TqfMgsJE4SnzLU-cBZIO6L54cJrLHWBPDr4CcS70vUjHsEwcZiekcf8fxadLtlbXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WuAqRLyNzp1nSKrv7JazkCiM2Cei0QBMfSi1UFfOQvR9f0BvtV-ecStOZYrfKXMJEJ6RGNrf7_2OEfm6GYYxqNHIwYsRhfnj-pQMPkzzicJ775gwtFYQN_zsEjw6OGdWPUj1nSlmTPueQWjKddj9j7FU3KxOSKRrYnxW0gDQi1NRaCGzgp-aslCxLg2BWsc_RtPt_mY547wGDCE4b5Q9raz64fYTiQYZaI7x7OX8-eaMRRbQ0LV-V5VSNvFeZN8BcGmxApsX9_X68-qBR0j5ldSH8wDql-WDg7xoeP-k_nhx-p5oOcosMrzch_z8aJ2MY2aV1U0GMPgprDyz1KzWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=Cc9dw7X_D_QDBl0rkLdDFCV8dmlc28Zve776s_SDVUQsTnSILyftN6ogKv7zYfpLyoeyQ3Ox_rEAVpyiknAzE43hPujYb3ShX9JiKCcYRpZZIz1mJkoRr4TiAml2gdpnnBldiYmJiOd1LhX6c9Lp4JYFHbDY_gRzvC8zSQbB6RZubz1Jk0CfNBNdY4zvVcGqfN-5TbehUH5rc5eWJhJivjotIZ3h5c2ODGGxS0DISAVah2Y1GfhoLgQkOHeTzpy3VidepOK163IMMHijElWrgomM5WW6n8IWBnm7e_oBR6LPbIGGyujy1tiRiKVu32fuBxwY4lZMWSPiuZTbzSDW1SIHVSh_XlP76g1nJ0pObW15ecY064tLwVYG-EvwjjJT-yPtNoNIgMUzybRSTSERXmiVQZc9IyQ3w69CHdWadXIWQICMSLaZ34cyn7gd2f18O-rchdiUJphy5CcPc3s-5M2jc9ebZWIvF31JeD37AFDHFI8041EpDofSnX-yIUOPVwAzK6VAxM6VzBXqVBvRtI4ZTCxPvWbKmx8eUXsssiSxNhv8zWeJqwRkN8OzF8f6hE1FqFjpD9Dsu7e0hg8xzGc0Fk1kuwE_099F-C6f8pIBPQmAkD3UGXs6BS0cYIWSFt_yzDiQIJPhNa6DhamUlWtBWiLtvhCmenvU6uRuU_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=Cc9dw7X_D_QDBl0rkLdDFCV8dmlc28Zve776s_SDVUQsTnSILyftN6ogKv7zYfpLyoeyQ3Ox_rEAVpyiknAzE43hPujYb3ShX9JiKCcYRpZZIz1mJkoRr4TiAml2gdpnnBldiYmJiOd1LhX6c9Lp4JYFHbDY_gRzvC8zSQbB6RZubz1Jk0CfNBNdY4zvVcGqfN-5TbehUH5rc5eWJhJivjotIZ3h5c2ODGGxS0DISAVah2Y1GfhoLgQkOHeTzpy3VidepOK163IMMHijElWrgomM5WW6n8IWBnm7e_oBR6LPbIGGyujy1tiRiKVu32fuBxwY4lZMWSPiuZTbzSDW1SIHVSh_XlP76g1nJ0pObW15ecY064tLwVYG-EvwjjJT-yPtNoNIgMUzybRSTSERXmiVQZc9IyQ3w69CHdWadXIWQICMSLaZ34cyn7gd2f18O-rchdiUJphy5CcPc3s-5M2jc9ebZWIvF31JeD37AFDHFI8041EpDofSnX-yIUOPVwAzK6VAxM6VzBXqVBvRtI4ZTCxPvWbKmx8eUXsssiSxNhv8zWeJqwRkN8OzF8f6hE1FqFjpD9Dsu7e0hg8xzGc0Fk1kuwE_099F-C6f8pIBPQmAkD3UGXs6BS0cYIWSFt_yzDiQIJPhNa6DhamUlWtBWiLtvhCmenvU6uRuU_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=I-qS6Pa_OuUcWy7TS_c5J4D15yMnqxux2zWi2BGMMvBiBOwgi7HD-IW65glHL2XrjuY1ZPy6JmIaVL41zpAyK9iYqKUjxFsZ6V7C5hFcUPSlPlyzxhfvjCh3FrNFHKbrVZUAR8bmIFHvFyAXyRNb-1VSz_KWRZ7fX7G8WsNzVZZswvcOV7CN_51yXN10KFM6J61ZGnYu1pTWX4oeOa83fm-L6wnVjh3st1LMpht1kHanE8ga3B5im0OZUbe6dsO6WzdimCjJc22vnvpjlzoYexgS_QqoWS3vQliEZ3IzyFSIY3p3wocd-yFhIH8G8fjBqi6YBaJMqbu8b5anr-2VLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=I-qS6Pa_OuUcWy7TS_c5J4D15yMnqxux2zWi2BGMMvBiBOwgi7HD-IW65glHL2XrjuY1ZPy6JmIaVL41zpAyK9iYqKUjxFsZ6V7C5hFcUPSlPlyzxhfvjCh3FrNFHKbrVZUAR8bmIFHvFyAXyRNb-1VSz_KWRZ7fX7G8WsNzVZZswvcOV7CN_51yXN10KFM6J61ZGnYu1pTWX4oeOa83fm-L6wnVjh3st1LMpht1kHanE8ga3B5im0OZUbe6dsO6WzdimCjJc22vnvpjlzoYexgS_QqoWS3vQliEZ3IzyFSIY3p3wocd-yFhIH8G8fjBqi6YBaJMqbu8b5anr-2VLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFABDxqyxv9nBXmZ99Ff4VSqOrJGhFSNGwKBNsfPea20t573IsymaYo__Kxwgy50jtHRneVbd5UFKqtCthkQ9JkT9FOzZi6uoU8ZY0om9qzvGuWgMp0fRBD77eyXG0L27dKOr4tBnRU151FKSYmnGm-l8AnwvI5r-qTvpfvg_CsoJJji5b8p4hxaq59MzIU3nTYbLQmSFnWNJV3YRqIT1-HvoZBa_C9ZvTB_fmBWrkc-9RDEH8F77pr_y95Or6zCIEG4Le16egxonzbStD4XHJeZca1J_s9DhtiAIwwBSlmb-JgjezxAGnHvcSWWvQ4i1NNOkDGJG-RFpxR_0NPrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWV9Rupn4z_snP76yaJZGyeHJuTkDLoW2_anIhGTOBCcdiL1a09D88w_PmBtvceGRuDIWcF077oY1XMHETsXXTfwJ_wGecwdkqvJ4THr-jxv1kIdxn80Oy0_38dls1Fdbu1GilFOWUyHsQGarrfV3_odwHjG2gyvmKRdDw7S1IhV5C1AWnzhyaFkq7Kv0co2g3Rj2he7h3Tyevq0pSfUi4qACXga_Suj5uyILag1HO3F6cYD5YeXxrNjG1Jm4MEzc_Y17h2Xvkwt4m1pcZmT5GR7-aA2UOcdclSuL65bFxV96MvNcaAsUeC7iHZpQvlGQMVlWIUvavPc2xtl5YdtNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0XWUjhOpjdWO-adTDPheYV-q4cKObTY4T_a1GsEMC-qq0aHFlMxfAe3TWjgbACgcG6HZ4vDsgu0yrdudUxXRN7qGBCLjJureexaXfWzlt5qvjVeahJpFzIMRILQWyj2xiMng5HbyUpitWu_dm55NUnRpZoT4bVl1jpaj6qH95hiQEeZszekN1nlnL6oAs3fo0R9fbY4r0TA5zWpT0NpJfFZTagyFCt1p9Objd2vsWoGMqwMaYjgmnwuaE4ylpw7OrODe0JFaaDH5GZJNp-qCqSWGLmneV5j7EIbSjTNfwDAT69-lWIvQ4apy5xT2TVrc4pMm2Ucmq1h_FZNOCLK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSRM4qBSbvpxawabC2Jb0U_Ux_dFjRDfWcjT-dBI3A4qdA4x_VGC_Kxi5TQzcJSNOfQ8FPbv3AYGF_9vsHDeu55iWmWYxRyiEl6ylVEoHBFAM4oHGSPGMtrYxKV3ER6HASCd6xNHJZSMkQ9wrIrL5mV_4lgO1nGs36wepYHk_5ctHFUcgzWMFQP3B2j6KXEWJyfbKWwOmhA_ne4julYShi2JDUedhNE3bRJxW4hfgQQWgqQx5N1Q63CRn_hQVyCoxqgBRFwHjVJh5X9NdVAFoAOZXQ5vEuPc1FZURZonlpkQw677mC2pRLHfb4qeD62vs2q3WLiU8wf-f5Uf2w5pvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaiiLYTdVH-TvNwcPNITFgKg4o0SaTc2l4s85vCaPWJigx8vKqnybj0fNadkAXIqtcKcFyVMKvSQ-iL_2NMvRWtpRmjblyGDX_R6NDaOHZiAaZnET2IzWINDZ6AvgPqasqiGaY4SqzYa_K5bV5fPFOHdzglDCLKdJ9iCd0WM3tHWnfMlnaZp3uCUOiwr24-SZAIgEse2NjnKUPZ__Wg5eFtStGNa5-zWchrpyJsVx2po56yaSNthJBNMqrDbTvvDraxJK43EUrkci6EZPkvhpPkQ_8mywXyRLOke4YcG4hJTJh8MYXp0M0Ft_f8FIG2_lSaclrgYrRYlyrXRVTQHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0mulZ64WAzW57SMMupqnUP2YCoscNWc7AUAlZoK0GC7uSmUGkzGoLz7_5BazFSK8GGCnnMNsI9IkC9pany4idzpiBCu91q2Nl1yd1yhQ6NSm7NL7U3Lf80rTY3GqWLaVtmL0T4cyv73a05ATXxM6VeAE01YWskfB0aPUeyk8mkaesFPjko-my1kgokHUeV7KJQmLJCkLl0AGu9DQY0RLY7YiE4-3uWiDuW3L6FgMLDwkfPI-CmyhrrbjoHCKOnNEb8S4qz3myCdH0qV3YphI_2L5bB57TdUDqvqKgcd4nMR6okZGSkgTzUTfryITn8ShZx3r2LSSQ1a2jqdZBBokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnJM2IP0bvbxcaD6JAIMribo45AG3sY9R_xDb_eWIPrA6iAx-6_HfVwNQedHMG_zX-t5xjD83dYpzByXH02d-uOYBvTttPJYd-yokHp_1CJtIlqDGTtgOpdULtvK6PJJgiiDbjiHW8dLXnTsiivlDTGGNRMy17DUbMA3yUoUA2kDUO9rlpA-QwwFCITrTh0QAnE4KBAHTB5EgeUbQl4HdAN97L4ooUFy4irUeft2AqXoBIyBEo5T-3uGCUphbTLGfcerzn2Zx2RyNWZiUiFclHNjfoMarbs-wVMtJoqQIV3F9TnCZegZ5u_IdWOMiGvUTE5gGZIQiqJmwWINVRgZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=j9Toc3WH141K3wdRNr1EVQYyB1yz-2cvX_YeBMOzWncUerfG4NtPle60Beg03BJ3bTdjF4RNmCKXVHZgOkzTNXqcIR34dDjd4o-w8cfKuZZlWRzREIRC844EPhl9KLaSoG678WUSBHYFsf3JggBEY63BmQYRn97M6M3UtorbdiVvLi91ayGw6CWFTKAIIBIV0NuPjR-Qj0zG-_gG0cSmMYUl3VJQpHq8tViSQSUjNp43G7uiCMm4gWKPjbwiNoMdPv4xaRrJpi7Yv5NJzAuD5cpl5c8IfXUXfEUbWFYQO6LX6qgRyjAN17mSvk2_TrS_JFAc1cF6VYvgJQt1R322nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=j9Toc3WH141K3wdRNr1EVQYyB1yz-2cvX_YeBMOzWncUerfG4NtPle60Beg03BJ3bTdjF4RNmCKXVHZgOkzTNXqcIR34dDjd4o-w8cfKuZZlWRzREIRC844EPhl9KLaSoG678WUSBHYFsf3JggBEY63BmQYRn97M6M3UtorbdiVvLi91ayGw6CWFTKAIIBIV0NuPjR-Qj0zG-_gG0cSmMYUl3VJQpHq8tViSQSUjNp43G7uiCMm4gWKPjbwiNoMdPv4xaRrJpi7Yv5NJzAuD5cpl5c8IfXUXfEUbWFYQO6LX6qgRyjAN17mSvk2_TrS_JFAc1cF6VYvgJQt1R322nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=sCfxZfv0ShTEbVn_AqYbrdz6C8VdA9JnENhJqCxNE5J8U2xxU4bIo8Q1m0mCsGjSsa4zj3GKkUzqzs7g9ZYFyXLp6apsba6QJN5b2TkEXOlqwbxA1_pxk-yxsSD7k3ZxQ1qIJ7TCyyB3dJO9-i56xEHgOHvtKP1GajLmRA0v3GaoE74GmLxgnV_3_PGdvystCcUNiS8lXGDnNQ-k7q_RltnBqIJ94QaLYCyEqSPPJHLJRx6oxZwwlmLV7GjpMcaSt4iRnO2e8Khg1_hiM-8CSSdbA0eDEaxhRurmp6jKEl5CCl6bX9Dd0Qa1ewYvgqJFs6sJS-GnRiHNpBKLfUqu5GReg55XwyeOyTwinU3XNa3LPjIUZt4PqpUs3ZpqnLLbdDb-Za8arMgQK4keTAXRrQFBKw3pTlCUs4qt_YFybw5Gc_jNsHXcOxVaX1X_a8IYKfkp8yxuS-Kx1Z75Ve63h5BBJZkXPNMLTcgQ1jXsyVwztxq3o7xYRjxWjB8F6yrbu80-MCYPkmlfMX3uxI2lMCvhck41EDjpKE6DjGXP7lo13D7yuhUPF1D3OesmAw6T8hV2coJHfh5EMdIPvvFxxVqGSz6huXaa2-gyRb0Jo5d1S8yg3Wmwqi0yja-tQIZxG1tG50HZV9YdoRMt6vuJP2nthVkPaRg0nIz15t0W-co" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=sCfxZfv0ShTEbVn_AqYbrdz6C8VdA9JnENhJqCxNE5J8U2xxU4bIo8Q1m0mCsGjSsa4zj3GKkUzqzs7g9ZYFyXLp6apsba6QJN5b2TkEXOlqwbxA1_pxk-yxsSD7k3ZxQ1qIJ7TCyyB3dJO9-i56xEHgOHvtKP1GajLmRA0v3GaoE74GmLxgnV_3_PGdvystCcUNiS8lXGDnNQ-k7q_RltnBqIJ94QaLYCyEqSPPJHLJRx6oxZwwlmLV7GjpMcaSt4iRnO2e8Khg1_hiM-8CSSdbA0eDEaxhRurmp6jKEl5CCl6bX9Dd0Qa1ewYvgqJFs6sJS-GnRiHNpBKLfUqu5GReg55XwyeOyTwinU3XNa3LPjIUZt4PqpUs3ZpqnLLbdDb-Za8arMgQK4keTAXRrQFBKw3pTlCUs4qt_YFybw5Gc_jNsHXcOxVaX1X_a8IYKfkp8yxuS-Kx1Z75Ve63h5BBJZkXPNMLTcgQ1jXsyVwztxq3o7xYRjxWjB8F6yrbu80-MCYPkmlfMX3uxI2lMCvhck41EDjpKE6DjGXP7lo13D7yuhUPF1D3OesmAw6T8hV2coJHfh5EMdIPvvFxxVqGSz6huXaa2-gyRb0Jo5d1S8yg3Wmwqi0yja-tQIZxG1tG50HZV9YdoRMt6vuJP2nthVkPaRg0nIz15t0W-co" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TmJIh7N0ow2TofaxtnJkmuqhHYM4lzrlSTR6H6qY_J0rt2-ICbV96s1ovO6Xby5Pl4jW0tX7qv7ICJvRgB2LoeUEH2m5p6ia6G2S7dfOHylHGmd5w2VDdrkEKpVEnI0vVe0rlmLE-rPfNXTPLyhzgg42BsqllWOyfyHXRkSCNlyAIUyhSR_tDKeenxN-ffpyfULn9HrvQL18Po5HsmmR-aPyse72X6fboHgeYBIjCQSjLUsrdkjPdSblqx_j_xQQFQGsaFXf3xzDv5u92FaXt1dKY0ZYdYF1PIagObH7PhTtLEHz-OE13_TNGr77EL4giaRz-5lyw3sSrrJ3-IhR2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mer5KFmH13epgA1nTuqCbkVVjo4JyekTLy42j5nPexFEqNkvNduistIGQImAv1GaEPmqPXKWe7899Ngt6hnuuo_L2CwOdzADqrSIZEVcromm2RmW_r7VsEZsl1S3vmZz9O5ihNrhe1urjF_9uSnqYFetKEXY5vGRmdsM6gSJweDNRelfqGuEN9c4ESlPBtVMnNsSeNyDw1ktacnF6AXQtgV-iSsuxPda85qJdW9DrnM27tLRcKwrNb3_l1qvgrCjvbiVgCu-Kr2dKGmqH20uw769xNMzoInXBgmj9UJQLvZMm8-iLIFX2fVmlIPw8oe65Z7kTqKOJ_Ghr9m0Op-dwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD7p60o9Mbes_GvlSChY83aRPDUyjoQ6Xg0R635UNwqnnNoALvl2NptZRFmpArxwhQdFK92LcGapl-wl81gG_dKuVqErZf2MIPW81FaWpN_0Ds3IXmYCyeAUaaY_YamxnGq_K9WaUaukm758Z_cpNqGvTaQ4D9ke7_XYlmEAb2ySQtQSFzfRDUoPBpktoIQ6N3uwhyEyBQInCroEhvLPK4GLYffJ_D73XkVjpPAfiRFtVjViWId24QIAl4jRVjWWzM1dJyjoDSX195Zhb2sFl6YM0hNOmaktRIhdw1lZnWZeTM05zUgJ4mh0ShpIzkcdbBJrgOHkCXn0XNzXfFs5GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUEljjt5v8Udo9PSexsrfDefJUd3r7GKHxcFmMWvoGGCALr6le50ABZlfWIBLdb-_2V-lMloJZKgYae-BgOpFw0CCScZBHL0Q0R7VGCN3DDHFNklV7E1r0cUPIOa5g2N8YhAVTeQJPfLEnUZlGPwJWu4Z8g2MtJOfrldxceUG2JhBzCB_dnhku4rmF6_CtjDM3J_qYbJGQo-PvOB6I3VrzfXF1XCxV-GuuVGVl0uOC6T3rD-G7bWmQJe4rBgaAariOVGOpUJKnDf4v9y5optGf7WV_n5gucu-w6m-BNySRZb_CS5132_-J6PK2ggzPCqcAzs3_Ai-bGlb8IwMZAggw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=X-DOn1zsQZ5stzd6vulI351t4g1W7sdd-ACgBOpxJeveAhNTZRynAJIrtZ9nnMThbu-p2ZME_Dv_fj_ALwOI22Xt-djzGMSxlvPB5HKbeZIGCP_W49QF52eoKhDBYnNRdTFAP98Augt0uK8rtZc7d0X_At8Yp5CaGvZDLVu1vR-T_HhndbH3IZPfS4DA3AnwzZzA3S3DadamGxVZ5p-5RXW60zj-R_28P-y41UXmo7tNsLDiGTIYYbiL20-b2CTDDrMySkxUXQZZJclgA0KT9tQHErLVBox_Sf0oWUydvm2LVqXqqQw51poe32KPl86INkWly0r_X4Hnr220hRNxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=X-DOn1zsQZ5stzd6vulI351t4g1W7sdd-ACgBOpxJeveAhNTZRynAJIrtZ9nnMThbu-p2ZME_Dv_fj_ALwOI22Xt-djzGMSxlvPB5HKbeZIGCP_W49QF52eoKhDBYnNRdTFAP98Augt0uK8rtZc7d0X_At8Yp5CaGvZDLVu1vR-T_HhndbH3IZPfS4DA3AnwzZzA3S3DadamGxVZ5p-5RXW60zj-R_28P-y41UXmo7tNsLDiGTIYYbiL20-b2CTDDrMySkxUXQZZJclgA0KT9tQHErLVBox_Sf0oWUydvm2LVqXqqQw51poe32KPl86INkWly0r_X4Hnr220hRNxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=PiwDQYgz4HWADOqu52HEpGLS8eIWfFfv6maB39ofrfDRhT-Zan4gxmc54H0Fzs_BqOuapgZKLXpKg0oIh0bgoRmnQ0NxS0cB1FKyGpqSe1_eU3lcWrv2yTTwhgxiIRWdPvH-CgfewWxRaoDE3nQt_Cfl165wZqRWfVh3rTtos8lcrlsytgBbuOll29UtwZZ4Gbd12rwPF_1ZHW_24V5TWEHC5azwFoP-LEBPRqpvg4Yr2q4SiMghnRnNqY58sjir-CfWmi-ZB2Jk3aUvgz1D1GZ_rmDWCJmtbWa-2zP0n_hBrxvzQK_gml3U86WQkmEZ93Xtco1A8n2igs3WhH5C-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=PiwDQYgz4HWADOqu52HEpGLS8eIWfFfv6maB39ofrfDRhT-Zan4gxmc54H0Fzs_BqOuapgZKLXpKg0oIh0bgoRmnQ0NxS0cB1FKyGpqSe1_eU3lcWrv2yTTwhgxiIRWdPvH-CgfewWxRaoDE3nQt_Cfl165wZqRWfVh3rTtos8lcrlsytgBbuOll29UtwZZ4Gbd12rwPF_1ZHW_24V5TWEHC5azwFoP-LEBPRqpvg4Yr2q4SiMghnRnNqY58sjir-CfWmi-ZB2Jk3aUvgz1D1GZ_rmDWCJmtbWa-2zP0n_hBrxvzQK_gml3U86WQkmEZ93Xtco1A8n2igs3WhH5C-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buMzIYFPysjoHa8lt9rasrDIfxPWlqIuBywuDouUF-4KJzGaDSyPkSOEx_OQ3B5h7O5U8s7yN5r7S7jBJYC9Xb4FwFfXIu_D9ySldP6O1Ns_uPUKacPg9RLqswh2vxsB1YpP20tppC3uObxHXm7NHFIOs8vMsUfDjJvqD3oB8sSffsHF4h07VKM4HeQqqVQh7MhnmQrlSbwwSXapeXOYuMh7eJIPDjrEAPV8m18pUlx6p-74Xx-NgoljQ5tg6rRxIWZtAYf1p3LORiVkcuNj6LHqhVxin90kL2nJGgVN-Hwq05vcGgbuGgQsZGjiu36zFkM-DYHVJjXIFo8rdlFoaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP2jCWWr3gNmhxMulxWI_zERBNTk23ng4UKwdkGjkZN_KVUAAhN_VnKaDd1rtR9CXodr8FHUbayiEci9q4ibDeMD22NID_6sDI0BJvoRgjn8qFOBawB6xNGmKJgVPcI4l06Q_qyPOnIeA-kcXeA-_eKk2tW4Akcvz9XgQ4j9iClsJdvyvYjvJjbwW8E1_qrhFyS1l8WBvCaBCs6b2iCLI4FfqIQaeryi_19Ps01cf6GrM3-JT9rcW4_JQdxdYAcsNEm7PKT_s_50rIGEzTPfdUG0aWlpPjXrHs4MgGWMHzWTSnCLmO8HSPesAAM_vKk6Polp2WEPCC83Zxz9drZVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSr7BiKF0OpDpqb3ERPB6qhvqME4pLfkFCRs6wq_5S836K8Pe3uB2KppY1uF8j89lj9FOBEAW3ILVHz8gd2ki9YW1Wib7OVeJlr_OiibF80wtlN2CjR08QwAMhtTpBI-l4VM27E329E1khHzNoj7V_NC_dbXlu2orY7qJgb34827XfMcTJ4S1brPSWQ74MAUBCCr5yMHTeGEo2fJznM2yO9PrICFkwO-2sxsmA_w7R9mu0tz2eAp1tsYfzS0n5nIzpbDc6Sp_tOX3rS03FObkQaq8e9UbSAkj46FQpf_GYtH0S8yhnExllLDqniGLdtiktmsEV2WTZJlJ21Yspl0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf2RXmOOdknUmIEM635gym7e5nEP4dqiDmVjsbAOSvFM2X89kdJAleSqrAvjuelX8VsC3b1_ul1mpJ8jtKW3sRr0jr2-63SkXeZAC1WbiPmsns5vqxFAI38ywYpw_dGls0SBMRiTlwU0yBHnOWdEgUyNuP4YXl7DvqFsfvye4Zq4iKAd2LoH6qFeYGIRxE8hT_G0vYTzaT2wvsoAlyZS2EVQ9T1SAZlJNMvkxdPfm3A_jb6sVSpfSEpbwAyFV3suQ2PTs4_-ZEo4M3M-W2rN4bkB9zfCSo0_TKf8PLpHT1Z2fRTP86yQ5yY43-b8D1u0fNL_xZpkJCof26BORRzOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=QfFaAYgsUqxai-zxEK-iKIvuaQZT0tmnddcf2sb-QzzBHaOIaC1S2iO-QY8I2cQwCfX_wj5LggoF2_TE4f0KMM7G3uv8Wfc1xoyA-V2A9iYisvmH4EyKORZllHQM76H0eYR4Wp4tl6RcC5Vy6yGimvB0nDFfBbht7bYgxVy16VYjTKc_R4S4HKhkBd3lrWEVlLzIq-5I_bK4G8cgt36-rbRIW-TuKSZ-6s40hf3XCw24i51lJoYLhE0HHa2fF6HZyhwTk91Urtr-E-SCm4TlD7gVwkJMmC6oECB4PYppHiaQEaPcWnIMwIynlPdwEwC3xX9NnCU69WIRZuEIPoCOeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=QfFaAYgsUqxai-zxEK-iKIvuaQZT0tmnddcf2sb-QzzBHaOIaC1S2iO-QY8I2cQwCfX_wj5LggoF2_TE4f0KMM7G3uv8Wfc1xoyA-V2A9iYisvmH4EyKORZllHQM76H0eYR4Wp4tl6RcC5Vy6yGimvB0nDFfBbht7bYgxVy16VYjTKc_R4S4HKhkBd3lrWEVlLzIq-5I_bK4G8cgt36-rbRIW-TuKSZ-6s40hf3XCw24i51lJoYLhE0HHa2fF6HZyhwTk91Urtr-E-SCm4TlD7gVwkJMmC6oECB4PYppHiaQEaPcWnIMwIynlPdwEwC3xX9NnCU69WIRZuEIPoCOeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
