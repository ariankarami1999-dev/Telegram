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
<img src="https://cdn5.telesco.pe/file/huH1SWU_PLgyH5k2JruYd6cOsT8i45jhkbxv7sNCIZIr8nuOTWLcpE9L-qNO2UpXxibztjQ7b1Z-GE0YO_qrcmHNYtMzh_qmvgswTbLJhuI3mgIcBLWAbPIC0QW_zm5WnPFwAtBC0LGA7O-oic16q1WyA0IpJS75Na9PKqO-dAjC0AmsthLfutcq2nJOZ0OMr8K79jRwxaUYGU3zYIUGUJaKBlWV_ntGFeeyBy9Xjxm6iyoVwrE4Z8Q_vpcxKdwbFck7m4hIxWs1ai6hpPfBhlPVrscwK7_KmcSbxstWXfAplWOm68xEzNVlTpaT4HusDPqD4olQTQAh21hoaHVp-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 600K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 18:56:49</div>
<hr>

<div class="tg-post" id="msg-99404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jj2rz31vgUnenkpibh0eEUOq4t46h-zV18c2zuPeXuD6jEboclh0PTka-VqhNnruc6pi9KAjzuPKgtTTbNMOtJsFfvc9g4asHm03h4bizC4BDfMAFSNhiG_Kj9jmvgTf5838sjG2YNRp7e2ranI6SV-xJHKZaW1YyFWQp8iazhe2PBrSGvWM-i-sNSGl84vJuWYHU-47EdH5bSpesZmYD--FIQuDt_FuJYWWxjLW91U4yLa-OOHvuA3AoJzi6R6jYxG_hc6HxWtdefKT0ZLX1zboe8EPZ_HuFHBaOpo1IBdsF_PcqJaFF-UXK0UXUDFmj9idhDJryaAKqjrFmTCN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇵🇹
خورخه ژسوس:
کریستیانو هرگز مشکل تیم ملی نخواهد بود، نه برای من و نه برای تیم. کریستیانو نماد فوتبال پرتغالی است. او می‌خواهد به پیروزی ادامه دهد و دوران حرفه‌ای خود را در النصر به پایان برساند. کار کردن با کریستیانو آسان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/Futball180TV/99404" target="_blank">📅 18:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECu7ywxPTFYGn1SlxxF75gAn_HDTOU36itdfpjKksqhQ33jDSglRefqhNybnuiJpxcrs6SiIEAu3wWNlgxMjmZJaWLkZDXsvRj226VwfHOWI4jVSs6H8TpH2hgSipfytXoC8qR3YcO-JRS6X1BFz_8n62zrDVF6irSV14lIx5OrPVo5lOXDd4zm6KulQhPBMUbM_MzU7_GWtvO8ZVQsFf5Dr5R3zp-2PxpRACP3XyyU6ynZeWqpOUGkZFf6xJQ-JY55iEcf98_VAnAPbBWIZRPUBn-TXWBASacBWiQ93ZKZTdI6z34l-iV-isJea7kUGbsKkmGwNtxNHd6IlH2W6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی اینترمیامی برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/Futball180TV/99403" target="_blank">📅 18:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
ترامپ: ایران از ما خواست که مذاکرات را ادامه دهیم. ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/99402" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqtUYLgR7msF2j3Q03eGvz2msE-_XU5QAV23ZkDRRMBxvUVAu57FzTfgcoAOcC-8xvnZYHiEwxukfiA2VWUr9wsv7IzkiLA1WIQHz5zR9_CnIyMXkFYyZnVVH2EMTfmgqamt536p3xy4vbJ7jDNBFBViweDXdFCmrdnr9PFbRj5fA40CpEUMSXjZtg-GsRH18dI2udBN1N43xeSaU3XvmlbVbVizq2XpmZhJXa15mKxi8klOixJZfKJ_0tSrNkNplqYyuL_fhIY2DYxnqz7dMy4p041x71ZlF0jlNTuYGHxqaoAcN55YAzIYG5_fxRNG2zhSyxU7F_Dge7_SJgw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین ربات  بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو ربات و ببین
🔥
@TNT_Winner_Bot
@TNT_Winner_Bot</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/Futball180TV/99401" target="_blank">📅 18:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnJSC96TZo4SrsUkwjR7LsB63B5TMHsdJMSeHa_RYFcRAncDjHS6gS8xfAmkhWPPPH3R6ur2VGVzeFHUfyl0x9EuOSb9oMTJMhEZ1mtbRVfOPbH4SPEhz7u-SJRDsw-2iiAihS7-Tb4Mhp9nqHBOmGZBH4ZRdizJEmzH8sGUtVtyuA2rmIe0-3HlwaRl6IKD1LgIhAI2CqjkJCARb9vRFNTDQVnAtOPrcVnx8ksCWltYrRx0C4r7VRbBfQV9l11HqDipA4bhMhiCB0Yn-3H1c3I-foL0MbXX5xnIanKBdUX9jjjtPkENUOt8RN9PgdMYxRmo1RpHmh6EHb698FD0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر گارسیا، دوس دختر پدری، دوس دختر و خواهر گاوی، دوس دختر و خواهر کوبارسی تو امریکا؛ همه خوشگلا تو یه عکس جمع شدن
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/99400" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4zspXmnrFoQ0muCRbLXwfu_6YxSvMsQA6mwDlt18vliFLcspuZagnE0tNhhO_-nlbKLpBji_PjqLAKxLOlNlDuwhE58ixMWByu8qAO9Eca2-YsbofiYcfuW5hbBkotu1AbKadNfuyATAScHUHwWDfmxU1AhfRoW2vJh6NpNOquAkwSIwRkXJVFF5IwJ_MOtCIH8Xi1aDby-vgoPL5Y5qo2ydWAaR2aE4DMLAKBzqbH0-gFInYFQrYxnuPtnUM8guDb_-6bODC00gpZhy9x_v4ZqJnW85uc4Y7LJTYKRs3k_-Ts_aqqsFeKsTu769su7jSzg5she_wtueZejlHVUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری
؛ اسپورت: باشگاه بارسلونا حداکثر مبلغ ۱۳۰ میلیون یورو برای جذب آلوارز به باشگاه اتلتیکومادرید پیشنهاد خواهد داد و رقم بیشتری پیشنهاد نمی‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/99399" target="_blank">📅 18:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
ترامپ: ایران از ما خواست که مذاکرات را ادامه دهیم. ما با مذاکره با ایران موافقت کردیم، اما ایالات متحده به صراحت به آنها اعلام کرد که آتش‌بس پایان یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/Futball180TV/99398" target="_blank">📅 18:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/626fb89fc7.mp4?token=sOLxAm_7tN3nSbk8DK-4I0j83xngA6JSrQo5Yph4V21Ij2pAIVvqy4p0IQDiMo7bHCwUk-S4WJzFTmq39muaVCdxSieVRasaDuOxvEGH5XW7XFY8o1vS3Ru_9hMDcNksc_Hh6PgsTeeGqdDnGiJWyfP2924x_tHuq8ku6bGAFdrU2X0-UghcEWQldZC9Kligk9jOWIbcgzyX4EZp2joJALJa9wzQhSoBCaZcprHdGI94VqXvyBpsTcpGchl8ItHLKY10Ar4_1_UdGDSYLOuCzFSP6KlLqO3-oowgqUF4k4u_euWM_N5oOodIcPwDSe5v7h7YoZ25Ugqiw4ykDnhopw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/626fb89fc7.mp4?token=sOLxAm_7tN3nSbk8DK-4I0j83xngA6JSrQo5Yph4V21Ij2pAIVvqy4p0IQDiMo7bHCwUk-S4WJzFTmq39muaVCdxSieVRasaDuOxvEGH5XW7XFY8o1vS3Ru_9hMDcNksc_Hh6PgsTeeGqdDnGiJWyfP2924x_tHuq8ku6bGAFdrU2X0-UghcEWQldZC9Kligk9jOWIbcgzyX4EZp2joJALJa9wzQhSoBCaZcprHdGI94VqXvyBpsTcpGchl8ItHLKY10Ar4_1_UdGDSYLOuCzFSP6KlLqO3-oowgqUF4k4u_euWM_N5oOodIcPwDSe5v7h7YoZ25Ugqiw4ykDnhopw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🤯
🤯
گل‌زیبای امباپه از این‌نمای تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/Futball180TV/99397" target="_blank">📅 18:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40b511411.mp4?token=qc0I7gMVBD-OLFSiict26OOUuJgUJq82EuvAyI1k-5B5bu09aWPNqAc-8WI-2Y8yV1lEVav2H8HVyjDXaeYxB_CktHKR4PaxeF-KHeBHD2R_-djPbJDKDdHX59kLcYhk6KCto6PFWC8uwdzYH-YaEoY8heuKuqkT01p36Dl0bH_1K0xFoDXU12y_rLU6ewNfK8WLu90OvZcJnDpjiVUfMLKR99vSIOpATsyicAZoKVFvYF0TiLwJc7GYlyp2fK6ehHKcs3KAHU1z6r57_qs5gPZMcptqP1qzmORYbf3lMkOOwpq-X0vQ2wJIjH053-LLItf_WLdej-C-GB9d-DuEJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40b511411.mp4?token=qc0I7gMVBD-OLFSiict26OOUuJgUJq82EuvAyI1k-5B5bu09aWPNqAc-8WI-2Y8yV1lEVav2H8HVyjDXaeYxB_CktHKR4PaxeF-KHeBHD2R_-djPbJDKDdHX59kLcYhk6KCto6PFWC8uwdzYH-YaEoY8heuKuqkT01p36Dl0bH_1K0xFoDXU12y_rLU6ewNfK8WLu90OvZcJnDpjiVUfMLKR99vSIOpATsyicAZoKVFvYF0TiLwJc7GYlyp2fK6ehHKcs3KAHU1z6r57_qs5gPZMcptqP1qzmORYbf3lMkOOwpq-X0vQ2wJIjH053-LLItf_WLdej-C-GB9d-DuEJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇫🇷
هوادارای مراکش جدی‌جدی باورشون شده که امباپه دیکتاتور هست
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/99396" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0602625ec8.mp4?token=obGNUTGwuxpByhrLt228MNozNEsbq_hu0SM2xEpzy7hpKK1ml8PYf-gMDFRUREUqWYptUJQAl8ajhLh4I_RgsAFyIfsKsEEVmU5VTuzj4LCrNx-Y3vGszStTSYxsbixRfTGPCCK1vY88etTFHRkFhnBtYTDdWYrf2sVjjNh2DDauYfzKvrc0Xx4_6yPu82MkMsXoSjaLPDoWUSF5dHVVdEgGItX9EFZwigBfw60Pw4QvjLjECG3b9M_kFR4LaC1oLzTPtUxJM3PAcwe0uJG4O7Tzy1TIplJug0UFv_7Vphaf-3cgwRrQ0EAuqIPBBQdrNeB12qZb-NdnwU1zodsw6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0602625ec8.mp4?token=obGNUTGwuxpByhrLt228MNozNEsbq_hu0SM2xEpzy7hpKK1ml8PYf-gMDFRUREUqWYptUJQAl8ajhLh4I_RgsAFyIfsKsEEVmU5VTuzj4LCrNx-Y3vGszStTSYxsbixRfTGPCCK1vY88etTFHRkFhnBtYTDdWYrf2sVjjNh2DDauYfzKvrc0Xx4_6yPu82MkMsXoSjaLPDoWUSF5dHVVdEgGItX9EFZwigBfw60Pw4QvjLjECG3b9M_kFR4LaC1oLzTPtUxJM3PAcwe0uJG4O7Tzy1TIplJug0UFv_7Vphaf-3cgwRrQ0EAuqIPBBQdrNeB12qZb-NdnwU1zodsw6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنایه سردار آزمون به میثاقی:
آقا عادل واقعا دوست داریم شما برگردی به جایگاه سابقت، حیفه واقعا کسایی جات بشینن که لیاقتش رو ندارن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/99395" target="_blank">📅 17:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE8l1uO5RGbjE5Ianfx5heefrlsYdABxcp-S81SlwLcXMCvHcFWKh5Q5tK2HjluO4cyYK2NPybbRbIkVSJRNJPVkgGzLvSURUOMlrOaOzs-30Tj7SWuV8Mo9SVEGQ1RN1UKWtw7PlM9V1hLGkZQ8j8wyt26xiVrbKwxicGjak4cGlTRpXtsJ_CnQFdMBK1R40P0hJ0CxY_pPneYUJbuzAHQcorlVZwNbUhHfBETeA6IfhUPzT4iZdj9HlXKt3XysieCLySVDUYMXceUcdoyhB88tXVedP5Uh1rncgu7cojV_1_c5RPKlC3c5oj6W6a_7yLbsOi9oBrUi35_b3aSD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
خورخه ژسوس رسما سرمربی پرتغال شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/99394" target="_blank">📅 17:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b97dc0ec.mp4?token=Tm3m7UKJrQfkHbq5H0nsPBKp58MRhKlBuf8N7k0afaslhAQ8TTjFOhAMYJVUSK9zZnASWCex4Rqs65WcsTFrc3gLmknWqfS4YCzDoYGVwj2E-1CPnLFpSBic9dYoWUM4rbvGx-sZFjeZ_OryIrMbHUaxodDsSBRaIMeVeLWvQrOF6Vd04bUZp19vm1dqaqICUKDjrSkNlej7RYV9cZpp7vZlO2qR8QKeDqqQB2G5q3ArE5dP_4y0Pp7ZkSm7zHn07KyDWRcgviuUrsmQ9ltynL6L8hixe6WQ5xTdrty-BABMeVhAsKZFEFs-cxgxMlpjjnrv3pwpVJY_U6RWCxLdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b97dc0ec.mp4?token=Tm3m7UKJrQfkHbq5H0nsPBKp58MRhKlBuf8N7k0afaslhAQ8TTjFOhAMYJVUSK9zZnASWCex4Rqs65WcsTFrc3gLmknWqfS4YCzDoYGVwj2E-1CPnLFpSBic9dYoWUM4rbvGx-sZFjeZ_OryIrMbHUaxodDsSBRaIMeVeLWvQrOF6Vd04bUZp19vm1dqaqICUKDjrSkNlej7RYV9cZpp7vZlO2qR8QKeDqqQB2G5q3ArE5dP_4y0Pp7ZkSm7zHn07KyDWRcgviuUrsmQ9ltynL6L8hixe6WQ5xTdrty-BABMeVhAsKZFEFs-cxgxMlpjjnrv3pwpVJY_U6RWCxLdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
نظارت دیکتاتور امباپه روی ۶ تیم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99393" target="_blank">📅 17:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bb018ba05.mp4?token=upW1UU09YuJyacpOtZw1Ayj1opi-IjGGNCg9HAOCtT2g63Z9Vwef_E5VCm23LwLr_VbVpZEHbJlhFoSDrvrW_jo-UxWRwurB7HQ_M_hDRbF4redcXXIahdDhiwYHjT0KToG1kfPn1ufYWzK4HTwemhhOPOBgWMjfw39ViR2vBA1EAGNExiuqVCbclA-dWnk0iO46popxTbd7oCtS9kCcSqbLDzqnN1y2MrbduOJgQIavHPOeNKpiwkkR5MtkNydqRbEUCEd8DZToHL9mL1YtgK-3fekW8aJ1fah7HFiO-JEESho-EKhNsDp4IQqWlvEZTE6qjCfkg05qSOZ9CVSpYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bb018ba05.mp4?token=upW1UU09YuJyacpOtZw1Ayj1opi-IjGGNCg9HAOCtT2g63Z9Vwef_E5VCm23LwLr_VbVpZEHbJlhFoSDrvrW_jo-UxWRwurB7HQ_M_hDRbF4redcXXIahdDhiwYHjT0KToG1kfPn1ufYWzK4HTwemhhOPOBgWMjfw39ViR2vBA1EAGNExiuqVCbclA-dWnk0iO46popxTbd7oCtS9kCcSqbLDzqnN1y2MrbduOJgQIavHPOeNKpiwkkR5MtkNydqRbEUCEd8DZToHL9mL1YtgK-3fekW8aJ1fah7HFiO-JEESho-EKhNsDp4IQqWlvEZTE6qjCfkg05qSOZ9CVSpYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
جوری که جام‌جهانی برای آرژانتین پیش میره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/99392" target="_blank">📅 17:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI1mjeSPp2onJthtR_G05FZi5zcDlbCwuPhNf8o4EQEwejBQImiVaLuHSizsY7UQc4R4erDagwtaAAazm5_h36tI_xYl8kZyBqN6MsTKF9rHArg6gtwnZZuNJC3zCkkRt0Gbgfc3cX8730djuPtJK8gl4PrT66lE1g57_hnZXwR3ILoQhfHHwRi5qdgsmD4oDt824AfgzLTHj7kxwy0AIdd44QuMMdEDk-FTeUZfpJ7ahEYWMaMA1_gUS0D4gcAqf_k-VTubsqgghgIGFW-as0p5LhhLM7cVyX_NRObkYp4LXJ2GVtb27Pd2cM4EjVLccKPer7ohtPvfIoiIhf4URg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
دوسال پیش در چنین روزی فلیک رسما سرمربی بارسلونا شد. آمار و دستاوردهای هانسی فلیک:
🏟️
• [117] مسابقه.
✅
• [87] برد.
🤝
• [11] تساوی.
❌
• [19] باخت.
🔥
– [323] گل زده شد.
🫣
– [134] گل دریافت شد.
🏆
– لیگ اسپانیا [2 بار].
🏆
– جام حذفی اسپانیا [1 بار].
🏆
– سوپر جام اسپانیا [2 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99391" target="_blank">📅 16:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE3BtUnDrVwkRrlc0r0_w6lJ2308oloNT0m66zMYaGCWqx7aAeGjjNTSehIC6nDuCQh4QSIreqSYrQfrX5u-WSgV0XoWSy4jCoflLPwn7W7xvoXOdbV9joakXpFGCukVkjDSSIqhiP5GKPgblji35lbvEb5gIsOcPjz5-PUabbcQWUHJjYOZ_Zcn4tsRjpeg1o2LLEkzHc6PxiJsSOPUOGiYUgNyWRRcOuRF2CNspMo6nZH0X1Z_6kov-kLC0xnvzblgA8dyZoIjn0FYRqmB6Qxyawn3vVSW_AGtiiQLUbbYTX4X5Cy_DxfGj1fjQX8tdbmTeYfP2esxvaIscNj_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اردوی تیم‌ملی انگلیس بازیکنا و کادر فنی به جود بلینگهام میگن Unc یعنی همون عمو
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99390" target="_blank">📅 16:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👍
▶️
🇦🇷
خانه‌قدیمی دیگو مارادونا در آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/99389" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIffmSpNuh-9kIuQV6wbK87nYCxwSWGpu6SdtjXPFCW53XSo-wfjGpMd2VlbO0SlA9vX8YZ7J-jHtrgovvUzZP2PnkAAduQ4iMrqcSnexwCYU4y0OZKD3c50vHuZLZ9aXJeztRYoJnCPIYWOKYrE7fjyZ4fcQh5frbyIQUow48smYXJzJ1c3RgYeVmu5qFhq6n2PRlD4j4dX20z--_xd6q5_xq17a5A6nUMuHWZREbnCz15AXYAS-sZAQzx4R3skzLStdMuiMWyUyYGHmEL3ACgs00Iytb6-GRCVL74t-HE6-lGPzGKVcc-0thd2lYQCAzl8SnHekJq7UgJ-Obp82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🏆
در چنین روزی
اسطوره تاریخ، لیونل مسی، اولین جام خود را با آرژانتین به دست آورد، با قهرمانی در کوپا آمریکا مقابل برزیل، آن هم در خاک برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/99388" target="_blank">📅 16:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEGMp9srQIMQf5z-mza6vwizK2A6z2VtVIB6H7Zl499gXcELZqM6HEQzC7TEqG3y7yQSgbFGz0pK31ys6zt7CVyhvY2kjflALEK-5nDh1BxHfe6w0XcEITfy6GLoqdDG4S5q_cAWgReuYoGbMszg1Od7ahC7o9bk7OP9p-rnvxW_rhWcYISXK1X_0xKc3lMAW8sgjBwksgP8s6jO9I3NzqMPN7cSNOjgt5A557F8k0HQh04gv3DbPJuuHQqHS95D-JrRVBMz-_W_wPIQEoHegh5Fx4F4nfjVAMpyketM9Jet30v60WNkA0oBNyKlAfkWhr6JH2rIUcWOU5wJHry9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚫️
برونو گیماریش به طور مستقیم به ادی هاو اطلاع داده است که می‌خواهد به قهرمان انگلیس بپیوندد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99387" target="_blank">📅 15:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e356e0dc3a.mp4?token=EjUNAu1R7xI-0593mAbjHm5ialJMl4-fbNXukTH3lD3u0uJ9ypBrBSGw7DyRTSZ0-Sd5GqmIXMihUtDFzXyQ0PomLStsZ66XrV5BcTMkaYCwLpYCOrsGpW-hscuHS2H63WEJ-nDJDeGUfxWOYBBjihfDAdbNUsJVZ1MSeK1QeIgyucLTHWQiBl0LT8-Ei9ylGEYi8JhF0AnWLP5FEleANYQpQr77Cbe8Tm-1RbKWTCPGJh7tyvhy8ko2uyJ1INsGwPp7joF31EFPvXVxflBTG_fHwqvLP4uI0fIFqWzoJablCFuuNVTgB_C2urQzjB5GMkoPpMqBd5Q2NqkcOyWGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e356e0dc3a.mp4?token=EjUNAu1R7xI-0593mAbjHm5ialJMl4-fbNXukTH3lD3u0uJ9ypBrBSGw7DyRTSZ0-Sd5GqmIXMihUtDFzXyQ0PomLStsZ66XrV5BcTMkaYCwLpYCOrsGpW-hscuHS2H63WEJ-nDJDeGUfxWOYBBjihfDAdbNUsJVZ1MSeK1QeIgyucLTHWQiBl0LT8-Ei9ylGEYi8JhF0AnWLP5FEleANYQpQr77Cbe8Tm-1RbKWTCPGJh7tyvhy8ko2uyJ1INsGwPp7joF31EFPvXVxflBTG_fHwqvLP4uI0fIFqWzoJablCFuuNVTgB_C2urQzjB5GMkoPpMqBd5Q2NqkcOyWGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
صحبت‌های ناهید کیانی از تقابل با کیمیا علیزاده و فشارهایی که بابت بردن تحمل کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99386" target="_blank">📅 15:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4b043e06.mp4?token=J0_TcYxElYzNnd-EgaOMExJRAw87q5-V7H8amfoJ7SWQ2uKWIF_nJSUX0k3fsgFxiT8t0k3S4P-eJe_IEvwlnUsK4HNE3m9T5XWziwfO-lMagwyHaNW1G37TWrxOD1a1avgPtqyFIHhypRxQdQ6Y_rzVM0eITB_VCSJibEySr7MG0CIqcVBpKS_-o76lJS0jMLvRjoX9p0yExBb95HlF2Eyp3WxE-0ZnONNTWYrj9Z80h9--chDSrVhxIoeac5mP8bGLKloCwGMQBc2hjdKzggIkevHUFLSJYjMpwBQQMEAwLoY_hXb-0HbPvrqazD66ebVgv1jtwJvlnZogtuzNmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4b043e06.mp4?token=J0_TcYxElYzNnd-EgaOMExJRAw87q5-V7H8amfoJ7SWQ2uKWIF_nJSUX0k3fsgFxiT8t0k3S4P-eJe_IEvwlnUsK4HNE3m9T5XWziwfO-lMagwyHaNW1G37TWrxOD1a1avgPtqyFIHhypRxQdQ6Y_rzVM0eITB_VCSJibEySr7MG0CIqcVBpKS_-o76lJS0jMLvRjoX9p0yExBb95HlF2Eyp3WxE-0ZnONNTWYrj9Z80h9--chDSrVhxIoeac5mP8bGLKloCwGMQBc2hjdKzggIkevHUFLSJYjMpwBQQMEAwLoY_hXb-0HbPvrqazD66ebVgv1jtwJvlnZogtuzNmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
افشاگری رضا جاودانی از دلایل کناره‌گیری از مسابقات مردان آهنین پس از سالها برای اولین بار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99385" target="_blank">📅 15:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2HHd4Tm7khCZ1tAJSxoyKWAN_7fMOOBlkVkMm-PpKO_S-RPb515cy04wAJpqz-YbU0hpZhTyMTLdISU1fx6EOXPs2xzmnkYEYFkFStze_2NDkMDaY4MeXmOwT9PplPgW8a2-bxvXVeiLCx1_kc8RiH29Bssii6RhLg3ReZZ1hDPuZESfDdrgr5P23vl51BxfGgicu15QhCNYV6Sf63YawAEMaQVRvNNeFVqGh2dzpzozxVL3w1fAxTLEqdQy4WE21ZsyLSKLNUMzY6IlFmfZuBAOWrp6DIpGq5hVGaXBi6fY3CKhFNoEM7wRO2avuzxK9di-MGeEMhVuafO8fb1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
بلژیک رکورددار بیشترین گل و پاس گل توسط بازیکنان تعویضی در جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99384" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99383">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHiSBcGepIxwEf1ACm0IAxqbNRqJH9wn5o__vtNpncYZOWt7gG7KBHlLkRo6hce2_TvvdHMA-0BaffgixJhZlDrppI7FCjjLB6aMdGFfSQNGR42-sAyobTweghSJ3LO5bEkoS4BJrrMqhgTUaUPc9nsXqUC1N2Jir51fzisNDUTJ4NwwLfH_q0I56KcjlTnf8f8QNR8sigESDGnHqgvZz6x3WLeWxQkt0DYcKecy3Dla7f8bAP4shBiK0lPd4DAlNsUfl10RWBiPXPZVWxsZ0DhFowgTsbSQVuCSBZ7u2Zmghg8khTg4PwcX_fJ7PFszQJRD1hZQ4mrsrD49mXRLZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری شکیرا در کنار بابای امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/99383" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99382">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99382" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99382" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99381">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NKlmxM8nGpRbUUvaYLgCYXiTx_0ngoDoUm6rUC5iIi_1XlKFoD1frQjF9_9ygUXd7BgjPQe8xlhKuLYEx0lNHjEfPqcUl33aKcgOv1QbVq2QxamU3lYzKagmP9yA1Y_PNzQnUSuSPIvMRVUIxn0XS2WE-_FmnyYIgVuUrXK6d0Huu0-exXgzUYlqdiFM_A5jdJ1sv8H_8ZU33EpvRGJGJn74Dh3k0yRtrLqfm2ZlNzArBc8HERZ4PSs6JYRS7nymcskG1eRKvbDF-_xHVjfnAX797gZwpQRUQLGxPLUTI4SDmhHqd-rzjcS-O5kRJ6QXZMIa_7b_XnaiQMj-gKziVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/99381" target="_blank">📅 15:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99380">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d05baf7f.mp4?token=eZjfWR5lDTKNzpytfMVEGEK1woP-lo3rYTblTJPiDWDurk--D8R6nAvUmJBLXXDC6EqdTxsawRLbRn3LaXosfvFtFbkCFHsXJ0RK7UpB5qasqmdPDD8m4vUUdha5D-G3auCq8LHPcYU0AWY14ub3yMbK_1sapKP3tSiAE-yqOWXxtawZ14X-YhIKqj2p3xRAO2F05wtSYWdoJYH_e6mQBKu3S6zTJytMSeods7yJDvFxIigFftlzkBRJBphb06xhxBgBT3w7P8Hv7hVGymLEarm8HxMlyFKamFhbdLhHBqwHNBqsDMYact02iEuaYvrfatcEA7ycU3JBUQnsfHtt7GQdVTIeZ-Ue_sayyy1Sz0HITf4Q49DWu1cKfxJaM4WdTbWp_TbHnL-KbPqcAFMo9s86y9M3d19ZwNS-fZ5l3hzsEl6qkYwm6t0vauKgaN3ASs74U2pm2TRfgVyhZu3NlohzfW9vt2N8j1WrZDyIqEl6IjU6x2093YVOkbOUDmPocfyHIxFgIN7UbrF8alsSC7YOynMmn--QvqmvqEv6b0aBZK9SROY6IWuEi5Q8jwOhXI036MjZh7a4ilh53fFrmnhVAx_pmFkmZl2MySVSMBpt5qLKtI7wZjDIVbgILh582nYD2jasOSeJC2dILz3gL0i1GDEJtUpUcnAdLuKIDSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d05baf7f.mp4?token=eZjfWR5lDTKNzpytfMVEGEK1woP-lo3rYTblTJPiDWDurk--D8R6nAvUmJBLXXDC6EqdTxsawRLbRn3LaXosfvFtFbkCFHsXJ0RK7UpB5qasqmdPDD8m4vUUdha5D-G3auCq8LHPcYU0AWY14ub3yMbK_1sapKP3tSiAE-yqOWXxtawZ14X-YhIKqj2p3xRAO2F05wtSYWdoJYH_e6mQBKu3S6zTJytMSeods7yJDvFxIigFftlzkBRJBphb06xhxBgBT3w7P8Hv7hVGymLEarm8HxMlyFKamFhbdLhHBqwHNBqsDMYact02iEuaYvrfatcEA7ycU3JBUQnsfHtt7GQdVTIeZ-Ue_sayyy1Sz0HITf4Q49DWu1cKfxJaM4WdTbWp_TbHnL-KbPqcAFMo9s86y9M3d19ZwNS-fZ5l3hzsEl6qkYwm6t0vauKgaN3ASs74U2pm2TRfgVyhZu3NlohzfW9vt2N8j1WrZDyIqEl6IjU6x2093YVOkbOUDmPocfyHIxFgIN7UbrF8alsSC7YOynMmn--QvqmvqEv6b0aBZK9SROY6IWuEi5Q8jwOhXI036MjZh7a4ilh53fFrmnhVAx_pmFkmZl2MySVSMBpt5qLKtI7wZjDIVbgILh582nYD2jasOSeJC2dILz3gL0i1GDEJtUpUcnAdLuKIDSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
خاطره بامزه فیروز کریمی از تاکتیک معروف «آفتاب‌پرست»!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99380" target="_blank">📅 15:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99379">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b94688a21.mp4?token=U1p_-dbTHuE_WBPH_dQSe_pv-FlKJdGEWZi5J5uuKAk5n6z-t0GpyrdJv9ryYvV-2P7FyxGY0h8JxzxbcO2Azl_3u3swiY3Md0Z0yZph2_rrASrVbN6SLnp4Nj1UW309NGNayACm2vkSVpfSDdVbk3YYIJ4TdpHHeRDRwyaEVGS8TLHfEZZnB5-7EHDJV_-VCZoUEVZTN5sdpLRGsDSZX7TkedJ5pKEnIoPVySJr4JFf0TMCtHlzDgZM1NvlZKLWjsS7IIUEG710Ua8Ebezv4CEPHgYvXyb9bjntsVDMw3h_dt4dO00fMKl_jsJOf1yabKD-vBvKAZwlZu3IjViziQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b94688a21.mp4?token=U1p_-dbTHuE_WBPH_dQSe_pv-FlKJdGEWZi5J5uuKAk5n6z-t0GpyrdJv9ryYvV-2P7FyxGY0h8JxzxbcO2Azl_3u3swiY3Md0Z0yZph2_rrASrVbN6SLnp4Nj1UW309NGNayACm2vkSVpfSDdVbk3YYIJ4TdpHHeRDRwyaEVGS8TLHfEZZnB5-7EHDJV_-VCZoUEVZTN5sdpLRGsDSZX7TkedJ5pKEnIoPVySJr4JFf0TMCtHlzDgZM1NvlZKLWjsS7IIUEG710Ua8Ebezv4CEPHgYvXyb9bjntsVDMw3h_dt4dO00fMKl_jsJOf1yabKD-vBvKAZwlZu3IjViziQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
لحظه احساسی و نوستالژی مصاحبه جاودانی و زنده‌یاد دکتر حمیدرضا صدر
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99379" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99378">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfEAO5EHz-sjeuo5JWIoDDWqrg_LOVsSNvLNlLqQMBkZH_6VrRG-vywUyv_LNxAPiBzVAu6cBVgoyVa8rL75A25ueAP7BPOyBqSqjpiEBOcLvgtLa2ulNqrG2fPSJSo7ALl2aJeRWUceoNbe2eIJiox1I9FassoA6nYuxm1aw-HNZG5VMRDl549LBnWeqk-Pl3bMsHW1y60pbY113bhOR3kPdrVUtsQacTJfplMHuVxG5rGdfOlKcG3Vd4qlNjJC7RIY4Or9zROXKXSulBNkpZ7BuBolJZ9f6OZ9FGT7DlY_F9pHtaG52KinztG6GE_5qCIODlnhh8SlLMMvLf7plA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کلود لی روی درباره جیانی اینفانتینو:
وی تنها یک ویژگی دارد، اینکه به چند زبان صحبت می‌کند، اما یک احمق چندزبانه است و برای فوتبال خطرناک است. او هیچ چیز مثبتی ارائه نداده است، بلکه باعث شده این ورزش در نظر همه، مشکوک به نظر برسد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/99378" target="_blank">📅 14:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99377">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7bfe33636.mp4?token=M935iSez0rZDdCJ_7Q0VMiodxyvf1dCeoi9ox-PmVjSbfdvihh_3CiUONkcfuHsGeJiPvoZXJRi335MgwEo857ckIfpDCRVTi2F-XXRM9Q-qmef5U7nMKhahLClJSZG-yo4eYf0rmGRkL0l5qNyB-0RyQwAMUOTAikDO2luB9lMVpa0Qknum21IMlnsVRRTsYYzrz3i_3_rXSRJx6SPm391ZesdD4L0CjwIUWmcUfzAAST0Mtde7KAPvOo9yVmrczm_O1KsmAXRhUhcWxXxyNAGSYMJsg_0uqxz4ljg7M9z2KxFxjDE6xfVIE-l5gZf9M6W0GEVEOA2V2_mcRgm-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7bfe33636.mp4?token=M935iSez0rZDdCJ_7Q0VMiodxyvf1dCeoi9ox-PmVjSbfdvihh_3CiUONkcfuHsGeJiPvoZXJRi335MgwEo857ckIfpDCRVTi2F-XXRM9Q-qmef5U7nMKhahLClJSZG-yo4eYf0rmGRkL0l5qNyB-0RyQwAMUOTAikDO2luB9lMVpa0Qknum21IMlnsVRRTsYYzrz3i_3_rXSRJx6SPm391ZesdD4L0CjwIUWmcUfzAAST0Mtde7KAPvOo9yVmrczm_O1KsmAXRhUhcWxXxyNAGSYMJsg_0uqxz4ljg7M9z2KxFxjDE6xfVIE-l5gZf9M6W0GEVEOA2V2_mcRgm-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
💥
صحبت‌های شنیدنی رضا جاودانی درباره عادل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/99377" target="_blank">📅 14:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99376">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4Ys9X8GLKz4z92Rcy9_6ZovHu_eOTISZbBWPX9vK4boGPFZUMsA7jRvktTKoaaL9DyJyasK-lnUlssAi02FT6_NcYfgLYLnNR8N9iBSealoK3dheQvOFwOTrnaKeVUL60ex-5bF9c9P5GmPJnZX1MhOJwzEUfkQC2V6_e4lGqt60JBSstVkWuXyivz8Y9uBRZhLILYg9sK2KH5yhGXucFbL_sRnwMy1QrH1nyr_p98iiw2o2Q1thKYboji_oQeY2S7EUFVuTUDa-oaUxDVIQYOW_otHt20eaZqHIcafGdYfODyWx0dVMb-qUxZn5w7IScof2efYfNT6hiW9782X4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کادر مربیگری جدید رئال مادرید با حضور سامی خدیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/99376" target="_blank">📅 14:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99375">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAB_JaHEZI7CX5xRCL00RCryT5NNuGNUX63S1cD5_TupQU9k_WvpM9mV_zxT--WMq6wi00hG61gVEAWcGrtluMyvQHB2DgcHjh0EuM321YBTl39DpuevF1kT-IC-mBj_zRqkKSiturKgJR4DLRPhf0At8dLiAzArtxLY5d6-c8Z1Xal4CZtJd1lMk4myD7swbNtwBkz6yBp3iPZ0fBCfzZhaMTzsSaFhMWqMJVKlqQ3vRis4Um-xZU064JeZV52wwXWI3_DB03A93h5w1Sa7Rr2JZ0-qPu0HdYXXqgjATBPaLkFBbWa-6QD_xISyhl9ikByZSf4KxjBw_ARV1_YDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇸🇳
پس از حذف از جام‌جهانی، سادیو مانه ستاره سنگال بزودی از بازی‌های ملی خداحافظی می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/99375" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99374">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCDfPNk_529PXUmsbCsTVksllwZGf1JGf4cWaIAc54cGrLDruxu-yeODZkyQk0otHneGYevNuP5uZOivXsCQgDHNEi1ZPb0h0dIF2cxjE1WERTK6JY1rqjG8ZD6zQ73d_kjrZzclcTQh9GFmAw-avZd3BkPf_GjyPkZEfbxk-NGsVjCwsEMIFMqow5qYvNlGSCvrGRuv1kG18HwcaKPHEP-un8UCy6TMVJ81NE2KJlo2hjWn4C-EmQ2g4o0neHOucab5nqlCaKFwu1kAmn4WPa8wnUZvDp7DutaFcJAtp6vHJQpyWkmL-vLvxNIs5qTQw2xSgy8dZzynlRNo4-C3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
#رسمیییییی
؛ ابوالفضل‌جلالی مدافع سالیان اخیر استقلال با قراردادی دو ساله پرسپولیسی شد
📊
👀
🔵
آمار ابوالفضل جلالی در استقلال: ثبت ۱۶ پاس‌گل و ۴ گل در ۱۱۰ بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99374" target="_blank">📅 14:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99373">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1-Bvg5Io38cvsQN3ac0NtSBsGo0J3RM2myDQ3QFEWp__UmViAutzH7mCK9hkdwG5Uyi_Fw-Y87Bd_xCpZ-vAJ4F2MLg8bDRGmrrXXLpQBHwD0Oae-jOYOn3-2rMuZFAy8bk_CstjdzxcP8tpfEt0KV6XVTBOqv7ZEZFp0ZM_BZ7h2V1Ixt1mK3k4-y1x0uyh-HW077pW8tPh8bIJCt0ASwnu9aW2u_JRNPCNIAjkOPLWyevGJEMBHGz5zfP5UN8NWQNeHj9jPMvI2CmehJBUQUqbMQkhp633riMuBQ9U45bGbOnRnrMAme0Pg1zWRtTWyI_aydHLqLOBctqAc3L6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
🗣️
لامین یامال: "اوج اقتدار در فوتبال چیست؟ بنظرم کریستیانو رونالدو."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99373" target="_blank">📅 14:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b3897abd1.mp4?token=kABxUN7MKZd9qHe3gSOKQ0JL69SL8qumdZtZqMO3hAMhKn8eCxlJxIqMzofXi5BYKBpFN02TZHbpVBe9FHp6kLniqPcE0gUVyWJfBROT5BnTp3JPVtBclXxPrIgqc-6tWXPmQjrmPyUgVA084Zi1knaHogM9es-5dYkhXriQ3cRjEPDzRmTDPLOUrfg7XMXU78IAwV2E9MDxBiI9rrVquHtYh92Dk0nYkQeLuo8o-j0q7D6ArEo-5Ql0Hl9AXmqs6t7atuE0Uh9bTvzdroJjVtQNoID_xDQTgq7oslBD1nnuH6GjL6MJq6ipmKZ4v_ip15pg8HP1g5Plxl-XKT5C-rsHj7EEh9NX5iVft9Dydc0r74ISV-orafOTPgzp3_sxYyfiFP1iUgODModSvVh4FS79skSYsLKsoS9eB5gwliLgrevdptcevwu4gsRX8MmWXlKTREu2V0Qe4E8mSBUuoqpsHLg4YC1NVQmj56aVabrqPCSi4haE8jGolKED8zJytM65VwItwHijpS2OCgJL1zJ1Kngbz1zV36S76-pjvRyrthsysfENdlpc1AQgsdniX76q3RpApRFJFkP9kAwShJInA9S2CTUTi0zQP6Veyr3ND32DRFjFQ5kpUeCJ9G2xTGnxvn-twFEybKhsfw8moLtyehSxqnaVcLlq4HRqeGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b3897abd1.mp4?token=kABxUN7MKZd9qHe3gSOKQ0JL69SL8qumdZtZqMO3hAMhKn8eCxlJxIqMzofXi5BYKBpFN02TZHbpVBe9FHp6kLniqPcE0gUVyWJfBROT5BnTp3JPVtBclXxPrIgqc-6tWXPmQjrmPyUgVA084Zi1knaHogM9es-5dYkhXriQ3cRjEPDzRmTDPLOUrfg7XMXU78IAwV2E9MDxBiI9rrVquHtYh92Dk0nYkQeLuo8o-j0q7D6ArEo-5Ql0Hl9AXmqs6t7atuE0Uh9bTvzdroJjVtQNoID_xDQTgq7oslBD1nnuH6GjL6MJq6ipmKZ4v_ip15pg8HP1g5Plxl-XKT5C-rsHj7EEh9NX5iVft9Dydc0r74ISV-orafOTPgzp3_sxYyfiFP1iUgODModSvVh4FS79skSYsLKsoS9eB5gwliLgrevdptcevwu4gsRX8MmWXlKTREu2V0Qe4E8mSBUuoqpsHLg4YC1NVQmj56aVabrqPCSi4haE8jGolKED8zJytM65VwItwHijpS2OCgJL1zJ1Kngbz1zV36S76-pjvRyrthsysfENdlpc1AQgsdniX76q3RpApRFJFkP9kAwShJInA9S2CTUTi0zQP6Veyr3ND32DRFjFQ5kpUeCJ9G2xTGnxvn-twFEybKhsfw8moLtyehSxqnaVcLlq4HRqeGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
عظمت تخت‌جمشید کهن و تاریخی از دید هوش‌مصنوعی؛ چه شاهکاری هست واقعا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99372" target="_blank">📅 14:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99371">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp08Lj3R__AA3kO9OLQD-0jQpO82cjTTv2wwiVRM3Nct8x9WqVImNI2kgv93cVI1d1hFgD1bCAtbPG93R-tb2t5HE8myFP2VtCLSEZhkW4-r2AcFIczpVgd4VzEnqNfY3DKsVAbDbhbQUMhUt572BxU8xBF99FphXVJXR6BotS9BX2nKonejGxnBVGwQrUGmvRh_IwCtQDglMVS3UF70o_Vob3WGMm6H6wJ-yJd5VXXZ638CPU1qTJbRKsx1lGu6gsTVs-TZ7VQTZi_M0A1ysN9lFp5bvYmhP2U9JcK7GdeI-YHshW4KJLYhjgcraY-lSes38AS0wsKfmVgc4V8asg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🦠
دیلی‌میل: دکلان‌رایس در آستانه بازی با نروژ مبتلا به ویروس شده و در دو روز اخیر نتوانسته تمرینات مناسبی انجام دهد و محل اقامتش از سایر بازیکنان جدا شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/99371" target="_blank">📅 13:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99370">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=oBY2h-voIJ79mbhuCbDOYfuZZSMbp3JyNttHb0DycjtuiduSe6tyQpNdeUNjGFPUde3D4SQopNFgO5rQGIB2aGSnmKqq00SVMKIAN94-Td9PffkzU96S6Gu_fsztXNemrHM5A6OQMeeAmZfEUhbO8VdEeY7TyIqhkmzku4IB4kXVGExZV6mVMocTFPvvBgDlFYDHZMbzBYCR28qkXT8gWZOo5uSWkMX3OSeTfh8GpaMeEoEfy0mS9MU9ToHlXmszLYU_JuORmZAUARjnezbDv8nWfOfeHelKvocOHSJSm-ViEjcrbOcHhQhGeecC7owRCWDo7wFqMRuI_cP3tWqLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86b45ed0e.mp4?token=oBY2h-voIJ79mbhuCbDOYfuZZSMbp3JyNttHb0DycjtuiduSe6tyQpNdeUNjGFPUde3D4SQopNFgO5rQGIB2aGSnmKqq00SVMKIAN94-Td9PffkzU96S6Gu_fsztXNemrHM5A6OQMeeAmZfEUhbO8VdEeY7TyIqhkmzku4IB4kXVGExZV6mVMocTFPvvBgDlFYDHZMbzBYCR28qkXT8gWZOo5uSWkMX3OSeTfh8GpaMeEoEfy0mS9MU9ToHlXmszLYU_JuORmZAUARjnezbDv8nWfOfeHelKvocOHSJSm-ViEjcrbOcHhQhGeecC7owRCWDo7wFqMRuI_cP3tWqLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرانسه به نیمه نهایی جام جهانی رسید.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99370" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99369">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
قرعه‌کشی مرحله گروهی لیگ‌نخبگان آسیا و لیگ‌سطح دو آسیا ۲۷ مرداد برگزار می‌شود. استقلال، تراکتور و چادرملو سه نماینده فصل‌آینده ایران در آسیا هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/99369" target="_blank">📅 13:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99368">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBdmGXHydkJEJlYCR4xZ1Ht0KJm6_B21n5TllIp2kmAjKSzOqJ2YpFQAXgZeEjMen7y8A8ba165rS-ShpokPMSko3MCH9TwB3eU_rWqKRpi1s9sOWBQl_YJkNwRZG1ZXjC-3UHZLlFBoNjjYa_DkRWVw7YexsBSaF1y5510wts-80RflpZva4kgSerFPvxWAtl7dYyTwYfSfP8AEYj3cOO047jGY5HRxG2-gyNEOZtgQGCOqQBtmSjsdsEr5EIcgkWFoaQBL_DoyFoqF-cSiYxFqNHTepyCOiYMwsFwxhfRTQhj1bvqtD8BNKy_Yw5W9UkktOUNxT1juveuEQ1KzXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇾
سیلیست آماریلا، یکی از اعضای مجلس سنای پاراگوئه، ادعا کرد که حساب اینستاگرام او هک شده است و او مسئول پست‌هایی که در آن توهین‌های نژادی به کیلیان امباپه وارد کرده، نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/99368" target="_blank">📅 13:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99367">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1Cfw_zq8gqQP5JjDwUKgBvevMa317UJ1BzUu5_6jgKJu4V08umoCL0O5mD7dbWh6Q3uYJZTbC3DfGWkY6Q79NRorapJQSl7e_BjRqmEIffrD-y9TuZw5QW3t4-QqDUfok0oBRBpfnqXdoosilUa3YyqiDR33LBF49d9QcDpQPy0RLL_0KXjWrqPD1e3Npd6VNcc6Frgh0mApqaSwAPcEHWQTvlORZmfs8fzQD545l22S8ijcEq1SZSHsgP-qh3cCjbETnGC4JrW-G3syu7JFhZWelH6vDY8lHscB0-d1UN60-Ef74DjPCGIGJGyy6nw1XdhldTmp39gV3jIAmXQMBII" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2aaf37559.mp4?token=sKcDt1Tshqpp4FTkxdO60uLT7PibRvv3ZhYNRd2KkE4hvDGf4w20-PZlBu5JRZDsfhpG5Q2_NqvMIPjdppcnaKQ4oaOJMSCx_MtSWa0SwpxDA4PSlR0olbIYn1C5ShqQdRFo-Z7CI5W6Y9f7wdnhdkOHL2gB6UXJ0NSwiEu8-RKNLHvosxNaUciAmktNTD5aXAt8K31LpqKCJsHyd7AnKjSq7wsjpYsvlyeiq75fVNbGB9CRHGFkJ_LcwqETwWH8ABJTDGc__6MOOzblL9o5V1wYfP5GOoj2CTCd9cD62I73FxhWhzEafR59J1Rg4wewPDtLNlaCTihEc7wChCiH1Cfw_zq8gqQP5JjDwUKgBvevMa317UJ1BzUu5_6jgKJu4V08umoCL0O5mD7dbWh6Q3uYJZTbC3DfGWkY6Q79NRorapJQSl7e_BjRqmEIffrD-y9TuZw5QW3t4-QqDUfok0oBRBpfnqXdoosilUa3YyqiDR33LBF49d9QcDpQPy0RLL_0KXjWrqPD1e3Npd6VNcc6Frgh0mApqaSwAPcEHWQTvlORZmfs8fzQD545l22S8ijcEq1SZSHsgP-qh3cCjbETnGC4JrW-G3syu7JFhZWelH6vDY8lHscB0-d1UN60-Ef74DjPCGIGJGyy6nw1XdhldTmp39gV3jIAmXQMBII" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
بازیکن‌سابق پرسپولیس نطق جدید کرده که البته برای اولین‌بار احتمالا حرفاش درسته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99367" target="_blank">📅 13:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99366">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRbJuYKeRBTrw0nEnKKhhH6ik3n7st5m-Nc6I-YblVhZhRIfDnjyJaV-WteP6xKY4PcIigmva1L62GaIg1C697cO9lL_CayA5-so035ZJ5lRs_FAu7Y9BC6A3Dblh9KLoOSmx9jb0mEHjhjd5W5rHYW2CeHM2oQ8eb_aOL_s6ih51SFJjXnzmAHWlsbHTQgu7adQ8SuEaNCKIhShUSJefWs5lJAfHw-b16AdNv8C5C4loZR-sGhZg9NjE6WgsRst03lPNyHLqfMvqQNW436RL9Dj3lAKuaUzxdfTvuqzCm1l7fgEOUSpiENl-tppTeEFHjwouLZi6S49kPGvcEVVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
موندو دپورتیوو:
احتمال رقابت بین منچسترسیتی و لیورپول برای جذب ادوارد کاماوینگا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99366" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99365">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=iXnBn2_QXqeiHzlKimeavSgnpnrsmagq4J78KIK8Jo67iyxTDhGurx4Mm7WhM7pBDoweK5kK29laXW5hLlQi5sHXYALcyNtddWvxRUs_YSCrZwZLSC2ibdkivdvlIQl5NjYZ6N5n4lzIV7pmeDzLHORsO0Z0QdJ-dAhFGPIhbQNU7Ybx7DasGNaLr3a6iIEZpvddDR5lLWklNVESz2aiXM_SBifuhHwMw2fZ67khhsnPrKZVVB0QIrYJyptSuqn_eB3HxuLReovEWIxeC_AblvCyz6Xvj_ZM9dbjlaP5_EFADt1oYA-r2zj8oojJQDziTUlAdd6g_kIput-46LcNYB6VkEpgIG5FWgrmOZ1AIkGNEjKmZ2R11YVZvuBRahlonzhsW_DrviWP_XhkimK78S0zfK_QjY3j15nw_oWrGRbmOBC3Qmr7Z35vf21Ar6eWUMrGlJwszPGOJModYPzf_3UUuHBBUDT-Xzsj_Yjfl6y3wpxKt7OzKm_zlgDqgLwoMpY8A9nHIEQhcL3Ef6dMM2nTedx0RXCv6KoGMJSthGcsG0zPIl4qhSYgpAGG94lta9l6XAl1B1mNRlW0KewBXVI2VzsvongVF4q9xQd55qnfPf3xIfrepai0A9ra8xKBEKE2NWM6V5r9_SqqCcLHsUndbrQxacpkcnnNCEt3mRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e9ae322.mp4?token=iXnBn2_QXqeiHzlKimeavSgnpnrsmagq4J78KIK8Jo67iyxTDhGurx4Mm7WhM7pBDoweK5kK29laXW5hLlQi5sHXYALcyNtddWvxRUs_YSCrZwZLSC2ibdkivdvlIQl5NjYZ6N5n4lzIV7pmeDzLHORsO0Z0QdJ-dAhFGPIhbQNU7Ybx7DasGNaLr3a6iIEZpvddDR5lLWklNVESz2aiXM_SBifuhHwMw2fZ67khhsnPrKZVVB0QIrYJyptSuqn_eB3HxuLReovEWIxeC_AblvCyz6Xvj_ZM9dbjlaP5_EFADt1oYA-r2zj8oojJQDziTUlAdd6g_kIput-46LcNYB6VkEpgIG5FWgrmOZ1AIkGNEjKmZ2R11YVZvuBRahlonzhsW_DrviWP_XhkimK78S0zfK_QjY3j15nw_oWrGRbmOBC3Qmr7Z35vf21Ar6eWUMrGlJwszPGOJModYPzf_3UUuHBBUDT-Xzsj_Yjfl6y3wpxKt7OzKm_zlgDqgLwoMpY8A9nHIEQhcL3Ef6dMM2nTedx0RXCv6KoGMJSthGcsG0zPIl4qhSYgpAGG94lta9l6XAl1B1mNRlW0KewBXVI2VzsvongVF4q9xQd55qnfPf3xIfrepai0A9ra8xKBEKE2NWM6V5r9_SqqCcLHsUndbrQxacpkcnnNCEt3mRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
قصه سوراخ کفش فوتبالیست‌ها چیه؟ این ویدیو رو ببینید نکات جالبی گفته شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99365" target="_blank">📅 13:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99364">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcHsy_ULNojM5DQIqMHFGa89LeJpAXCLvSrk9AHbzVc_AaYL814zXACYI0HT_HSSE_lRG94qlCLoOpL5JciPZ7bgBpnCIT_ngArTPkYpxA_s66IYME8hyyWRkjq3ivIyBYiIRXtOfrCiajX1XbL6zS8-16v75G7wmjZZEGzbSCSERjVQvVKsJ7VocAY0lp77ren2tMhpJdxzr34J52QNGEPPZGD15tgPGzfojBRn-6ILun46BlaTMVxLMfbU5gSHEphM2SSoJ6I0-eVZiVmd-XB8lwS7vqf_sKqnwPv3Kiv2NzPT7AyAXx2FW9Kz9H8Sur87e9WyCLPPnsgi9wswTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیلی میل:
دکلان رایس به ویروس مبتلا شده و برای جلوگیری از سرایت عفونت از بازیکنان تیم ملی انگلیس جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99364" target="_blank">📅 13:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99363">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qs9he_3i2FeOua5ky1BBRqbM19wlVMY16W6DMirGPabYMbeEXPPyfnGKT19IFGiBcWCYFCXa78T-2xZmD5fbUGcrXy5H91QHGLSY2Z7hhnZTwCx4g-1HBcXc1-eRmrrqv4VlRxG4I6usVsgwQS5bmzqcHI1iiybNhh4IAD-DH-3kjeh1-DOMJl4w4t6BAXPvEFkqUZ25MevV4SlZJbTRFCyyCLCJueGiiAMsz2hWbMflAwJ_xrH1QN7j-u93TicbIl92AkMveBHpzgvE0v6K1mau1-4A13LangezB2B6BY83XQEF8s8onSGes2wn-cOYoeH4TztvkACzRisSUaE7EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
بیشترین حضور در نیمه‌نهایی جام‌جهانی
🇩🇪
•
آلمان — 12 بار.
👑
🇫🇷
• فرانسه — 8 بار.
🇧🇷
• برزیل — 8 بار.
🇮🇹
• ایتالیا — 7 بار.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99363" target="_blank">📅 12:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99362">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiyJPK4eJwxqEuO-8XURq35rz4jEFjKnj4lBNlYdKDJfLqRjk7yD6gfgM-jvG8t1yMqnM70cae2iZUekxEUzv4AqlMldNU94rUu3MVW4qNUr_qT-oaBESD4q_soc11sVcRApqZNIywSVzBCczARRzopCPzuotgRLgg5I10-XNH4_xpUhCvgrM14Een1X92JPevkCBuK0jnXB4JXypLxJjheVuC4DHq3jKKP9yDslT9HLzAA4S6nIeIlU4jJuReB1TaO8Q6k5z8EanDMNTs6-H6LmYWQDxD-SRaA0F8HVdusJ9UKJG6HQ08ZG9ai6os_95_QvnjpAkzZ9wtuCPenS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیکو ویلیامز:
در 19 جولای قهرمان جام جهانی میشم. دوست دارم در فینال به مصاف آرژانتین بروم و با لیونل مسی پیراهنم را عوض کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99362" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99361">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1-OyOrbLdotk4DZ4C9ufpuhRBhFLCBtZtuEj463R3KLB8qrBs92wXjnp9ws2g90G3E0AzNFAL9quyQP3UvCJyex4RPUBGA7Xf7WOZQHadpqy1cMakb2A0K3SWlvUWu5ibv1YfY9qyeMKGRjBt6D5wm7lnHem0EdrUZGGFZXorgxjsdHx4iGbg3WOmHfusOjJIQ5wkaL2YueHLwZEDl433J33WoAVfIrPl7cpgaT4MBCWnTp6w4dB6HrXUyh-wY7yeEWJ5tXrBy1YERLoEMtZoCe18UOoen_UbNGDQrrnsBhwVv99j8tKpznlZKwuGgC9CpTqzQ1fcHIowhtK5EruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📅
در چنین روزی، یک سال پیش؛ اسطوره، لوکا مودریچ، آخرین بازی خود را انجام داد و از تیم رئال مادرید جدا شد.
👋
💔
📊
آمار و دستاوردهای اسطوره کروات، لوکا مودریچ، در باشگاه رئال مادرید:
🏟️
**• [597] بازی.
⚽️
**• [43] گل.
🪄
**• [88] پاس گل.
🏆
– **لیگ قهرمانان اروپا [6 بار].
🏆
– **جام باشگاه‌های جهان [5 بار].
🏆
– **لیگ قهرمانان اروپا [5 بار].
🏆
– **لیگ اسپانیا [4 بار].
🏆
– **سوپرجام اسپانیا [5 بار].
🏆
– **جام حذفی اسپانیا [1 بار].
⭐️
– **جام بین قاره‌ای [1 بار].
🏆
– **توپ طلایی [1 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99361" target="_blank">📅 12:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99360">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaxWpvNs36Km71XxonJGyYvemMl0ypnWXhcx_g_wiO2jIe88zZRUVyNNZXyBn5cWKHvRR9Nk36hckNn-Zo9f0rNW18sY-StKBPxEO-soKQzGGLa5DmCgyKLub9aCWBzltUeHWunDvAvgIRGl5DJ1WlDhCuuODCmWueP-iujgLHuW1k4xEKCzw2zgr932Fx-NGEulN8yvsphUhnhkuXkmOVxzeJKiyL1NDv9IujQFWp2270CmCOBDZ58ZnOUkFzyIx2g_rgcqTz2RVHLGceSwIDsH3thoqTIJ4tZVAH9ZmUPyx82kFqMPc5srbqC4Ur4BSt6znTo7IrctRyauRPfheg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
استقبال مردم مصر از تیم ملی کشورشون بعد از حذف تو جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99360" target="_blank">📅 12:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99359">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN8_6g6SsGI0ygRsVRdDhFE_AvwXK7KTrGu95Gsgy3sxEFY9GTELalwdVsknqExMcLdTJIA4dcFvXwEIXk3Mo7JZknAECWoxGSvwC7XVzl0bQ0ae_2tWVBt0yY-1QMr0TEfVL88jLiWVONU1U_T_Xl9DnQI8oNt2px0SA0BU6OGzGJG0pDXQYkRY7D0e_EfHTAnaG69ax_SmRSLDdhYvxlvQWlmyFsyVFi6nxJPQ2t8B2lT4EUymMOd6wgGpzK_w1q-WkUpylWM6_RO-HVKyi50nSyyNUVh6DKjkGlqOUQkXHzG79PIFP3EyjhMxs12dhax0FzcHtEKsHwwUA3b-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📅
در چنین روزی، ۸ سال پیش؛ اسطوره پرتغالی، کریستیانو رونالدو، باشگاه رئال مادرید را ترک کرد.
👋
🇪🇸
📊
آمار و دستاوردهای اسطوره کریستیانو رونالدو در رئال مادرید:
🏟️
• [438] بازی
⚽️
• [450] گل
🔴
• [131] پاس گل
🔥
• [44] هت‌تریک
🏆
– لیگ قهرمانان اروپا [4 بار].
🏆
– لالیگا اسپانیا [2 بار].
🏆
– جام حذفی اسپانیا [2 بار].
🏆
– جام باشگاه‌های جهان [5 بار].
🏆
– سوپرجام اسپانیا [2 بار].
🏆
– سوپرجام اروپا [3 بار].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99359" target="_blank">📅 12:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99358">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We0Y2kp0hEVACnnUl9SJJqPjC8FtObufgdNaRPGmqz7ntyIwYV1VvsJCZF9nxKPW0vIu7HO2__V8PYQ4_nWj_1mJhMfLwU_ddPhWyLUtTYPvgy6Twy45rTJdIiLR2aPQK_VHM4RGaBpCMQnnZA2HqVW2jrYj5lCuKjwEGkCfmqjWyno20la6_pYbc0aH7F1buOSLkq8aPAFJD49RtzGKpcE2YKjCNemxVdSilHZUVJaQBvGer38SaTwbdU_6D5JvcA-VnqWz2QPat6AqBmMBKD2YK6JdRXMuS2kDRuDzvUK6r_qoOr3jBEZj8qsxt4EOUc-21Z4sniUKAWgMOJRddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇫🇷
کارنامه کیلیان امباپه در جام‌های جهانی:
🔺
🏆
۲۰۱۸: قهرمان
🔺
🥈
۲۰۲۲: نایب‌قهرمان
🔺
🔥
۲۰۲۶: صعود به نیمه‌نهایی (تا این لحظه)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/99358" target="_blank">📅 12:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99357">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c816ba371.mp4?token=HNfk7jtvutu1q6KSgJCm50IfWaOxPkgPxlWGTlPCJ_UJhpBZ1vLRJUfuc7SPg54s3cnj-gwELwGIxAmDE_Jyr7Pcn-SUFPAqDdFbhb8YZw2vEVPNrTpVbu7ZEouq1KomPpbdsuoJmuG4mKrYiElYNJTS9d9dMpYvZO604Q0lN6OLo_4DFeY-G-1JPIUU8tN5dwcTXGiX6y2TWI7nuzYbKXEdFgYhrSB4f-xRJM8KiT02J_Xnt03j-d5NwbmlzZavCYOkqQhkmpofd_SvbQv2_LG-jo0HS_joIrgVlb8hu2VBrEJrX4bXQ3fWzIRe-H0qprrHf5KRfN3uMiwzBOVKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c816ba371.mp4?token=HNfk7jtvutu1q6KSgJCm50IfWaOxPkgPxlWGTlPCJ_UJhpBZ1vLRJUfuc7SPg54s3cnj-gwELwGIxAmDE_Jyr7Pcn-SUFPAqDdFbhb8YZw2vEVPNrTpVbu7ZEouq1KomPpbdsuoJmuG4mKrYiElYNJTS9d9dMpYvZO604Q0lN6OLo_4DFeY-G-1JPIUU8tN5dwcTXGiX6y2TWI7nuzYbKXEdFgYhrSB4f-xRJM8KiT02J_Xnt03j-d5NwbmlzZavCYOkqQhkmpofd_SvbQv2_LG-jo0HS_joIrgVlb8hu2VBrEJrX4bXQ3fWzIRe-H0qprrHf5KRfN3uMiwzBOVKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مهدی‌رحمتی: دروازه‌بانی در تیم‌های بزرگ به مراتب از تیم‌های کوچک سخت‌تر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99357" target="_blank">📅 12:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99356">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d32845b6.mp4?token=rNNCzUHpoCz_o4pUPgGnA7kxWhQhmNmhXE3efXiV8TlDsjywJMyWelsdv8winDMpee8cR3R6LPcYNfIKSpM3n3nEd7mbN77q6ve5YSDkjZ6eUDazJ4gS438ZLJqNwZOj0iWAHU4BpCsx7YWvfPhN-nFJr6viNmy4JDZ3hgfwJmB8--fheAA23dcQKgKVg4ah6qBJziwY8jMC7og7yF221LhX6nOlTembheHWVMDb34PjbyXeJ0jGrJvRtdjMhUU3OhnzIUMETz_jldKZbDriQbp5DXU9ckkcv0Ieqz2hYRar6-psnob-gQ9wChpEAVQmpFPsO5p3du-i_1IO5TyC0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d32845b6.mp4?token=rNNCzUHpoCz_o4pUPgGnA7kxWhQhmNmhXE3efXiV8TlDsjywJMyWelsdv8winDMpee8cR3R6LPcYNfIKSpM3n3nEd7mbN77q6ve5YSDkjZ6eUDazJ4gS438ZLJqNwZOj0iWAHU4BpCsx7YWvfPhN-nFJr6viNmy4JDZ3hgfwJmB8--fheAA23dcQKgKVg4ah6qBJziwY8jMC7og7yF221LhX6nOlTembheHWVMDb34PjbyXeJ0jGrJvRtdjMhUU3OhnzIUMETz_jldKZbDriQbp5DXU9ckkcv0Ieqz2hYRar6-psnob-gQ9wChpEAVQmpFPsO5p3du-i_1IO5TyC0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایتی از اتفاق عجیب و جالب در جام جهانی ۲۰۱۸ روسیه در بازی ایران و مراکش که برای مجید حسینی رخ داد و زندگی فوتبالیش را تغییر داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99356" target="_blank">📅 11:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99355">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxWIpbB7YwznhgxxUhkwRStKfnx_JaYfT1H9sx4paMEnQmHGCkqmkYSjT1ATgrTy1_rfzQJQycSSstMGnrwqVLYXDHqcxJH_XYBMN7Mx4Tcx25emF19yzsFAf4-SOirKIvqEkF07GZ4bDunIshzCzLlYbc1ehHuI6getatqRwABW0LysGDONyJ2TzYmwRcvOnoqFwYE3jdiINZ8RABFhHiOjHP5rjS7GNiWpiP0gwnSMkuAg4VV2Erqj72CLQOvDAGitTUO87BCJ-fQpeP86HHZ1rtjMdorLBlkknvTOqsMvopZgWEHWHhw7is2mcICK9pdDmeyaosvxo39LXj7dzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روی کین درباره جود بلینگهام:
جود بلینگهام یک بازیکن سطح جهانی است. اگر انگلیس قهرمان شود، جود بِلینگهام و کین نقش اصلی را ایفا خواهند کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99355" target="_blank">📅 11:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99354">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c176e8c357.mp4?token=GneNDriKK0xTfR9mR2X6K846-q0YORrwgtpaVPqal04o3E4bC_vs8QOt8_WNyu3d4jwq6TUkC62C9b7Sz00eRlQYuid8Lxj_QfxT4-ILl_S-vSj4OywnAVEq4eQrfQge84h0leeGDDX6s0ZF-pzN_7CMy_kmtzIWMUcC_4FxTGW0bs6EV90bkKTjCtT-PFf3NVJBM8oyOclm_1YC2RdfL_BoYCuFRWHM302VrvPtgUMuQebKsFNZcgItWha9gqAmEUsJ091b4lzxErPnKrHBP-IInR542v0tlBu5eOhH5lc2ZpNNrQy8QChPHly7b_uHDpwrdrk7zmpgL7khjiRStQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c176e8c357.mp4?token=GneNDriKK0xTfR9mR2X6K846-q0YORrwgtpaVPqal04o3E4bC_vs8QOt8_WNyu3d4jwq6TUkC62C9b7Sz00eRlQYuid8Lxj_QfxT4-ILl_S-vSj4OywnAVEq4eQrfQge84h0leeGDDX6s0ZF-pzN_7CMy_kmtzIWMUcC_4FxTGW0bs6EV90bkKTjCtT-PFf3NVJBM8oyOclm_1YC2RdfL_BoYCuFRWHM302VrvPtgUMuQebKsFNZcgItWha9gqAmEUsJ091b4lzxErPnKrHBP-IInR542v0tlBu5eOhH5lc2ZpNNrQy8QChPHly7b_uHDpwrdrk7zmpgL7khjiRStQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق‌وحال جورجینا در جت‌شخصی CR7
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99354" target="_blank">📅 11:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99353">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da77d29953.mp4?token=uBiLlbsdcvtV8dYQydluzUvL32aK3kZhvMaJ4uSDVZBEPtkQd0hNODID_Kcmn4OwsqkkEbECZT5XB1A11XbmlGS5O2O5bi4A9MSI6qTeiiLl1dQIuNcGmgu2y7xSIAB2KE7kKUodcVsWB1X6QqmeKAwT35jGR7DWL5I_F3Js2yAcAlt7l4OtMHPnXRdSAa91uTB4ndYpCsvOpXhGYoNCaMTXpfzb-V6GoNrRvupcHGdGfHz4gmQK66sGGably140WFaOmqxkW6K8KeiDkH_QlW6AHp7vFfVRmYIGsQsosv-bPvqTzTZO0coxJtdQDRrYa7VMyobajMdUtI_dK1RCWE65O6OokCzp-tJWBXz77ywHu96Q-ZOH1Rz5Ehscgp2x531JM6N26bVEyO_MLnoX7nRVlIbfrdBdxzZ6Su6YY0fwPV44LLZF8hBI8admXNqpNis59unrcBmcvVubjqiCfI5DZ_gNuVzXrD6cqut8Hc5xVuA4jIVRnlGNpLtJa8ygzXMFXvuDvAKN8GuwDCzt_hoZVpTWKl2tmdeea5sgq9v5xGOur7HOfkJlZccwBFPUCu0shAzj5RD3q4ZIDSZs6MiJwIVLQmhTwLXYA4WZml68Q2AiXq0u0TMZ-Fu3H5iGVv7K0q-osUa0DtUTv0yWtyrBedtPzO6rIrPPFrzgfI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da77d29953.mp4?token=uBiLlbsdcvtV8dYQydluzUvL32aK3kZhvMaJ4uSDVZBEPtkQd0hNODID_Kcmn4OwsqkkEbECZT5XB1A11XbmlGS5O2O5bi4A9MSI6qTeiiLl1dQIuNcGmgu2y7xSIAB2KE7kKUodcVsWB1X6QqmeKAwT35jGR7DWL5I_F3Js2yAcAlt7l4OtMHPnXRdSAa91uTB4ndYpCsvOpXhGYoNCaMTXpfzb-V6GoNrRvupcHGdGfHz4gmQK66sGGably140WFaOmqxkW6K8KeiDkH_QlW6AHp7vFfVRmYIGsQsosv-bPvqTzTZO0coxJtdQDRrYa7VMyobajMdUtI_dK1RCWE65O6OokCzp-tJWBXz77ywHu96Q-ZOH1Rz5Ehscgp2x531JM6N26bVEyO_MLnoX7nRVlIbfrdBdxzZ6Su6YY0fwPV44LLZF8hBI8admXNqpNis59unrcBmcvVubjqiCfI5DZ_gNuVzXrD6cqut8Hc5xVuA4jIVRnlGNpLtJa8ygzXMFXvuDvAKN8GuwDCzt_hoZVpTWKl2tmdeea5sgq9v5xGOur7HOfkJlZccwBFPUCu0shAzj5RD3q4ZIDSZs6MiJwIVLQmhTwLXYA4WZml68Q2AiXq0u0TMZ-Fu3H5iGVv7K0q-osUa0DtUTv0yWtyrBedtPzO6rIrPPFrzgfI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ایده‌های نویدکیا برای تغییر قوانین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99353" target="_blank">📅 11:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99352">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnEdIWjOTNyvKx9Z9Vd9fue0V9re4EbHFzlUKYSApd0avOnP5BIfhna_AbB1Y-MsTK4KjdSeoXhZgj81zuiv43TfrVXCzvUVIDlDwTlu5OGpggkpdbpTQNylY8IMwJ-ZuvSFIjN3jgaxnNM2lUx_dcHKAcNlDkNZqmdThzSyEt5vTKtyDuDj9j6HhyZSBop395gmgx7H9Nv39i1MK8L2qc7x-gnT1Otwd3u4kJb1zQxyh3IOjglKqCeuvPQKVSspre3bnfQLgKsBhn1sibMA_K4ZtTeAovhPW838UlHqa2Bbr4B_RM1cXLnxNo8EfEjfMmsIv1mS0DF3YzYw70flNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو در مورد چلسی:
این یکی از بهترین باشگاه های جهان است و در دهه های اخیر به موفقیت های بزرگی دست یافته است. این افتخار بزرگی است که بخشی از آن باشم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99352" target="_blank">📅 10:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99351">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebc842a555.mp4?token=kd7hpIxU215kCutcVz7fEVUbUbCK7hgpE8aWDjAE54uFq8TqU0RGZKzTqTtjMQwOJvWouTGAJwz5qhxjgdBL0vEOkCpXr_LI-kVuli3TCCAje1wk-5nYD3tW9ZRg6byDqnpBjRVt1bh9seL9zJ6aNnLwAql__PaNmJKJkgtye8EClhVZpp2YiTrDckEsBcoD1LYopdj4k9nhBOYndz7lFs4t1GIhZns8mSsSSZ0e2btTut2VnnxY2YLiZM4oO7ewvZTsWAA7Xvogzk3u-qMi3J8F1xcB9mEUBYn3Yy69EOioQv5xBAnqfFPD5RjMAOJNDdUDkDPZkcYzms-kV7PVow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebc842a555.mp4?token=kd7hpIxU215kCutcVz7fEVUbUbCK7hgpE8aWDjAE54uFq8TqU0RGZKzTqTtjMQwOJvWouTGAJwz5qhxjgdBL0vEOkCpXr_LI-kVuli3TCCAje1wk-5nYD3tW9ZRg6byDqnpBjRVt1bh9seL9zJ6aNnLwAql__PaNmJKJkgtye8EClhVZpp2YiTrDckEsBcoD1LYopdj4k9nhBOYndz7lFs4t1GIhZns8mSsSSZ0e2btTut2VnnxY2YLiZM4oO7ewvZTsWAA7Xvogzk3u-qMi3J8F1xcB9mEUBYn3Yy69EOioQv5xBAnqfFPD5RjMAOJNDdUDkDPZkcYzms-kV7PVow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
ناهید کیانی: کیمیا علیزاده بهترین رفیقم بود، هیچ وقت نمیتونستیم با هم مبازره کنیم حتی تو تمرین‌ها چون صمیمیت زیادی داشتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99351" target="_blank">📅 10:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99350">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db66dc2928.mp4?token=E2xpp2u6Uj2bJ4f5DUCkvHcAM8aR2goxKRK_2FxrIJ486Jtg0FqbQHFZirhEmvV139tG_sH9oyNj8Qi--kxV3t2RASyg9rTMOVRSPD4kuP9LKD56kiiNRqlZO-XwbnVaEhz5a6hbe442VW_o4Ji2s6LCNrOzMy9urFl2IkyTKIib3u_HoEvEJYMKNRwOqTmYpb78EFChsu67ArhE773Q26U02HQe2tYGHr7N2Bhi2ysBX2UoRK88PvvSrlWLHuOGTHbo2GySDkA9wDbkq3C-y-QuZtXNcfmVHcfzxaATGS6U0AEoJByfImnzCa9Q1GtXZuxwj_2oWPVrbJCpcluEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db66dc2928.mp4?token=E2xpp2u6Uj2bJ4f5DUCkvHcAM8aR2goxKRK_2FxrIJ486Jtg0FqbQHFZirhEmvV139tG_sH9oyNj8Qi--kxV3t2RASyg9rTMOVRSPD4kuP9LKD56kiiNRqlZO-XwbnVaEhz5a6hbe442VW_o4Ji2s6LCNrOzMy9urFl2IkyTKIib3u_HoEvEJYMKNRwOqTmYpb78EFChsu67ArhE773Q26U02HQe2tYGHr7N2Bhi2ysBX2UoRK88PvvSrlWLHuOGTHbo2GySDkA9wDbkq3C-y-QuZtXNcfmVHcfzxaATGS6U0AEoJByfImnzCa9Q1GtXZuxwj_2oWPVrbJCpcluEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
احترام ویژه طرفداران مسی به رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99350" target="_blank">📅 10:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99349">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ1PUSIJ2NVW43n10FqouxUnTE5036PzVpBj8zjA_6-ZeM6Gd_nF3lK0B86Tju1ZbawCk5mxzGzksy9YtH7buZQiP62Aata6lTQK2M4p0F3gVftIDvoAQQpS_h-75OLUIx5kQyhOIpO6nkb5DWvv_d126SzHBs1f4nv4D4ugqKd4KACGUSjqEMNUCKazox0tVTCbLfqOf0fyGU1QUpDa8hYv7zZvA9FB91iM4_fnqOEpb-oT54kP4dpvvwBmJ0Z9pzEKawkTIzYddN3zQWkab3Zquz_8ZKHDwMAKdmU7pTsmhHFGnTII30t4HcTSZsf1VHbQIlWHZuhfGJ_21ARKkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
🔥
🇫🇷
آمار تاریخی دشان با تیم ملی فرانسه در جام جهانی:
‏• 25 مسابقه
‏• 20 پیروزی
‏• 3 تساوی
‏• 2 باخت
‏
🏆
قهرمان جام جهانی 2018
‏
🥈
نائب قهرمان جام جهانی 2022
‏
🥇
رکورددار بیشترین تعداد مسابقات انجام شده در تاریخ (به صورت مشترک).
‏
🥇
رکورددار بیشترین تعداد پیروزی در تاریخ.
‏
🥇
رکورددار بیشترین تعداد پیروزی در مرحله حذفی در تاریخ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99349" target="_blank">📅 10:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99348">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a112d5bf.mp4?token=tvwRqpifyew0Jf_XYV7WFeJgoHAyHiRvMDblmprPZPsUoEUtiaTv2acCPwgH6LAThDZ0sZ8DVEy8n3D3tcRvIF06C70nJg_RTk1pL_bWR6Yo98-qQLHGeChy4zuYOiiBUthdXdp2hNAJwRqQdidBwI4r1iZEtfzjy9grYdYgYPLycopTPBEzqwvIWF5tewueH3LEguulnXVASv56VURiLXKBu8x5OX38a6YA2lomJG6B3z7WocFQmTaReehkZvF3d66YAwxtFxWfDNM2JFcSDD03YVpI0h3t6fhtNnNnFyTvTwELsF8l0LgH7jfl4ZVTmN1aZXooKM8mjlKq-kdjBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a112d5bf.mp4?token=tvwRqpifyew0Jf_XYV7WFeJgoHAyHiRvMDblmprPZPsUoEUtiaTv2acCPwgH6LAThDZ0sZ8DVEy8n3D3tcRvIF06C70nJg_RTk1pL_bWR6Yo98-qQLHGeChy4zuYOiiBUthdXdp2hNAJwRqQdidBwI4r1iZEtfzjy9grYdYgYPLycopTPBEzqwvIWF5tewueH3LEguulnXVASv56VURiLXKBu8x5OX38a6YA2lomJG6B3z7WocFQmTaReehkZvF3d66YAwxtFxWfDNM2JFcSDD03YVpI0h3t6fhtNnNnFyTvTwELsF8l0LgH7jfl4ZVTmN1aZXooKM8mjlKq-kdjBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی یک قهرمان ورزش کشور بدون تعارف از واقعیتی حرف می‌زند که میلیون‌ها زن هر ماه تجربه‌اش می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/99348" target="_blank">📅 09:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99347">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2516de958.mp4?token=dyGVe4wLI5z1lfkNLXg10u6SsWlhfGBRwrbpAu_BUhedDiBcHaf-Afb3TSS6nVfAj-Pf3hlxR5Lf8XezvxgL84X55Cz4KyYJLHMlCvvKPQr94v8ds-_Nx2_vvmiajddxvOGg9lm53CRw1m0PKCIPhV2Da61yph5HU1msDCoF6ikD3z8JW3TCIdzchiL74Y8WDUqXem9HRcsDa6DXr6IOzYGkm0B2ATks9_in2o0grvKsaZL18MqHCIILGZJ2wKTkNU1jy6UCiG4qZVn6dpMcv3a_uoYK3oSvTdVY1aPSwPpG2h6A576ZBMZQA_yvaTk77OE3xQi04EX7fxJlL4Pqkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2516de958.mp4?token=dyGVe4wLI5z1lfkNLXg10u6SsWlhfGBRwrbpAu_BUhedDiBcHaf-Afb3TSS6nVfAj-Pf3hlxR5Lf8XezvxgL84X55Cz4KyYJLHMlCvvKPQr94v8ds-_Nx2_vvmiajddxvOGg9lm53CRw1m0PKCIPhV2Da61yph5HU1msDCoF6ikD3z8JW3TCIdzchiL74Y8WDUqXem9HRcsDa6DXr6IOzYGkm0B2ATks9_in2o0grvKsaZL18MqHCIILGZJ2wKTkNU1jy6UCiG4qZVn6dpMcv3a_uoYK3oSvTdVY1aPSwPpG2h6A576ZBMZQA_yvaTk77OE3xQi04EX7fxJlL4Pqkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇦🇷
🇪🇬
مردم غزه درحال تماشای بازی مصر که البته با باخت مقابل آرژانتین همراه بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99347" target="_blank">📅 09:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99346">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab94d8d11.mp4?token=UxWS0MCMSr4oa0W4aH61S2k1HsFv8h2MC89XsR39KLicinyhmZdIPQdtTqakEryKFRLCpNYvhbr3KKEbSDjeB0cOSynfqtvXtD7NhDTso_icHzdaiRLKVygE4At-4MqYkZJIDAKaIQAWOPPvzVcCNszKXi0tDoLmE3xmkeglpO8NDHMo8ss5MbciO4dDO_xV-Dh8v711j5KhO_2v7hs-hM_DwKogaSiYS-lVBK5mncrKyOBxf9M6zVn09M0dtbf4wYgfRTaIy0BbttgG3RqwcQsG-F8TAZ63r1a3rXHDgpa_deg9yh6BFD0WaQjRGSvb4BbmXw93ge3SwyvjuxJcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab94d8d11.mp4?token=UxWS0MCMSr4oa0W4aH61S2k1HsFv8h2MC89XsR39KLicinyhmZdIPQdtTqakEryKFRLCpNYvhbr3KKEbSDjeB0cOSynfqtvXtD7NhDTso_icHzdaiRLKVygE4At-4MqYkZJIDAKaIQAWOPPvzVcCNszKXi0tDoLmE3xmkeglpO8NDHMo8ss5MbciO4dDO_xV-Dh8v711j5KhO_2v7hs-hM_DwKogaSiYS-lVBK5mncrKyOBxf9M6zVn09M0dtbf4wYgfRTaIy0BbttgG3RqwcQsG-F8TAZ63r1a3rXHDgpa_deg9yh6BFD0WaQjRGSvb4BbmXw93ge3SwyvjuxJcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
برخی از پنالتی‌های از دست رفته جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/99346" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99345">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKzxY2iGhDbJPlxS6K9XNu3jZnXOjkkkl-Op9kGQZ4KUNQVCxuD9SGOoXukQC9e1q2jH4Rvb9YFjykjr4H_panBg11EzR7I7MgJAWW00e9AGkQPKIx-W2R7fI9Xw3hYetncqMBE5PYN_Ws-tkhJx58RfrxWSAnYPI8wirE0MmgYu1quLkUB5dt9zGfMNMmrz_1eeIw3u8ZZSjTGXG6XgPDdqwyrdmye67xu_rn5oiq-0HbE9CaVa-WoDVOVLb4n8WNP0TGwu0NVeiprOM7PTMct3_Uf-GzWWst_KDbiKkvNLabJFyrSQWwXKY9MNWjr5TQiNaqdsS-zzAHsZ7i2e1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
نیمار قراره هفته آینده به سانتوس برگرده تا در جلسه‌ای سرنوشت‌ساز با هیئت مدیره سانتوس، درباره آینده‌اش تصمیم‌گیری شود.
🟢
نیمار پیشنهاداتی رو از چند تیم لیگ MLS داره و
احتمال بازنشستگیش هم همچنان وجود داره
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99345" target="_blank">📅 07:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99344">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2abecac88.mp4?token=mNK7LOwj_JW2fFsSrzskjlxvw9ic4dKPJ8pQ3RKaM82T5VaGMA8UT-4p1WS0xVLFtgZsZGJpb13vmCjTj8D9YkUAaGonYYTnOtQO9cauz4f_66iXDVZJ8iNC-kLD_FLLr7V7CcmfUjKkT07Rk2pkGEyBTyr8nJcV1CdpZ4-kC5QBa-gC7QVS9j_uJlpG0XuprxNwkD6gSRBeMp28A1D3ArMzju0DxTPYx1YUTtsLfT7MIZ5agKF6wqOMAlvq_TWPMG_A5VZI16m7EIJ-9UkmFkn5_4vsY5UGe6t6pn40F6qrzQ8gyBZz7xb7g8fmM_spBnhoKj6r3HFynslV8R4juw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2abecac88.mp4?token=mNK7LOwj_JW2fFsSrzskjlxvw9ic4dKPJ8pQ3RKaM82T5VaGMA8UT-4p1WS0xVLFtgZsZGJpb13vmCjTj8D9YkUAaGonYYTnOtQO9cauz4f_66iXDVZJ8iNC-kLD_FLLr7V7CcmfUjKkT07Rk2pkGEyBTyr8nJcV1CdpZ4-kC5QBa-gC7QVS9j_uJlpG0XuprxNwkD6gSRBeMp28A1D3ArMzju0DxTPYx1YUTtsLfT7MIZ5agKF6wqOMAlvq_TWPMG_A5VZI16m7EIJ-9UkmFkn5_4vsY5UGe6t6pn40F6qrzQ8gyBZz7xb7g8fmM_spBnhoKj6r3HFynslV8R4juw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
📌
افشاگری کلوپ درباره انتقال امباپه به لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/99344" target="_blank">📅 07:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99343">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuJRzR0QMZRjAmVoPyTRCY2kPdGIDT1AJJctpjSNQ-VaFvC39h_gMzyb618QKo3wlf1Q2VEbmN9XONjYMeQ_h2cvN4XA6poJ74dh8-S70O5x7e60U8k1gKkRbIXLwsya0n3cFr6pTRRCfH6gaJwhC-6BHxQs-hV-OX9eMUfuTaesiskGRskVY38GNRuEaLBZQSPQZgl9ukI5cSkyuFmItmOmQsCRTE5TIhZF2YjN7nBYhhRGLYa8IwKc86yBDxeKH5TqgsjTRoxanv1yyQij1gobe3lXCIYgQQgc5-ZtCYuvcnvPaH4xGdP8DY-GYmHt_E3uInsYZsojmnVAHJAJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Legend
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99343" target="_blank">📅 05:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99342">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7TGzOwMApo4_0luIXFTHc428x8z9ttCkNCkrRZiK1YespP2PV8vaS4-zHDKSc8EZ27TG6dM3XDm1Watnt2DbOlHh7qET_yCv-OJhdcLie4SNTq1tlGgbVJi21g4n2Oe-i4F4SzNm66RHIjiffEK6rOUWoDXzl9ovcDb14NExR40ORFach53bm2sI8kGgn9Xcn2O4yrobIoMEthTrOxd0rajWdXlO-m35O-Fgm1InOmvU-MDbNkOaoUkNUk2XUebJRUhClRinS6o0fH1ZWNPTVlm_Y6EWotTKZgZtTSaecpbfH0ftjTG1N2JRF-jYzu9l7OYp2Jsew25ZCaMf0J5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
مصریای کصخل بعد بازی با آرژانتین یه کمپین راه انداختن برای آنفالو کردن مسی، بعد از 511 میلیون نفر فالوورای مسی رسیده به 512 میلیون نفر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99342" target="_blank">📅 04:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qut_ymDc6ynM857jX2XdiDbcde_lnVC76PTJXCs3YRzSLC1VrUH4yZFrd-u84knHRC7oBUNzQ5mdmRAEjx9UgxNsAi6Uka6P-AoW21hllsWjLUIQmZ8YygQC3Bz54unrvF_xpa_ks1ueUa71y96V7MvARl1YiI54F8bxXXJ3b9bSKtl6z030zpmsCbvJ5v3Fz2UcWlmjhNTWubmp2ndqu3RPzWyzjW-NP8fgNoS3IhMsQw6a1q2rYbiQNXuGZeXFqqX822qxv2fGhp00uzVEZyGJUaCbUwey0FoiTxcpS9xrA4r8eTBo9rOLrJJyvp7gYpYjd0RcXwSv0R98nvk8Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMnA3Zm6aDPvh9VNZyf0l6jcHFX2TdBsteGtziHCkJMFJaaKShO6hJhDUqz3UndpvQTh2dYGG4rPYkKJSjEg7gmWb5HXp3bSZFizYGg18AnryB7jL4r5RqadPi40wJxUeNpXa0ov06A6IHpcBOfPEKWZZtwXQ9RNX_KvQSnDWM6epNq4RHV2CwCnBoZpfLO0ss2r0AvlovA_ems_r2iNtijt9CVf4I2D-SutPM8JMBRYVHDFKmTRL8I3LXZMykbr0r1Z4vLR1Klh1pcJvOTxUtqQbHbcZP4fEa0dWFdiFyGefrj8-h85wJxXh7VVQ8u4-uPCsj68yDFAdXsgrhXpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-P77KP6sFpuQ0Ozy7QgH8CBj6fsWeOPhz10WOYV6GSYVdEaTzj_NDc4NEOk7i5z4AdB63UnCSZ1ANPVoI07MMjaReIuFjFuO55ZlMjbx2EyhMg5uSye0LJ4sUpkTfqs6ufcrzzIDGKLdI0pdwY3JhqI7E3JhV6hr_yS6ElqqG8jI8MtvOB4HEJU91BZq8-0gxwjhVxq_Cf0dHYlpHDTdKnSaV4W3CYq9kNy5nNOctkNbjC_AiaBLUdh-2R4NMqkRGhfxtamo3qJwz3kwH4LqL8jctPfKUpFnWJ00sXjPQBkjpIJYwSB3U7IoCyj7V1LdPVYqyr1QdbeC-zR_WkbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FuSIBVxkTc_MU4cb5cjTX2549RgYZvzYT4F36H-L-1OdPlLTBlqLoEt1TAF4VYPYc1K26SmATc2ACCP525k7OxUvavQk2NB6xRV1qvtzlL0hg1PWTtbxDLIZW1aLjQ48pp-eEg-WPtNnPOhziIj020X5ZWopFTGJ2e-sKDZRxUpuKY439q_3sbXFIWrqvigX6lrFFSzwtifT5plsr9DSnshqIcv8lxP6aIiV10uHlYI1oE5545X-c9vfOICGlwzuWW0Euo6JGNjbzsWZeFBATWxzYECzmgp81aKOzZtg6jPYWMMNdYCHjwdRjnBDE_9xfzVukRcikyAhhb6FNggI1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8EsM4LwFoVtTLTgW9WWKHNd_hRbC8na3OtY-k5GwQTovzqaTQJahnvI23c3dYEedAgn0R1-tVDXqndUAkeAmzcGsr0w9bH8Q_xdV8CFW-ef5oe4c8x6g0tC0nH9-_Z1jaGhbxHlsui-hRklrZ2PLDrSX_HboiO1JRPmD2qTVuhq2OB841-OKUXLF7tXm3ozKXvW2UaAlSYvTWsnU6j2gTYTlHpeWcbgvhpvkNlN8yRNqX6rNSeXfspb7LeIDvPbSQToJLA1jHK-iZ_Sj2QZQRaSEq5gxqfKZAcgmI_cpXBqhlrCXhBnTKYyBnZ1uv6NdrcTHd2S6mNTjOjHs2bsiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/99337" target="_blank">📅 03:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=Pn1XhtrcvSDX0sGbJcGjTgAdwE7QXne1scvSC_UXzcltuWDznxQTSt0zpO5yMRZNvQw41RbiIEW-DJE7hnIaHl1cZvdaAMpQZVc4lxk0rSFMvzR6Gx-ANOsKa5IhYQ1INRIeCjV03YOICs57t-YdRYsSoXkeVNS-rFxXdLccVOFE5tEw8zApf6r1d4UNxsxMMagSFuzq9cq2g-R6NuQCh-CaJEhu7d4-wbVcboq1YHS7WlsFTcwQAZ-Y9Cs6RfYjxBwHvEkwm0fctfyHLecTeMmeOx32PxW2V8mJXl-rAWcKqlZmlD86AXXnKGOvJ2sTbr7AtFZUEx9ZVrGOozDViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8c2f73aa.mp4?token=Pn1XhtrcvSDX0sGbJcGjTgAdwE7QXne1scvSC_UXzcltuWDznxQTSt0zpO5yMRZNvQw41RbiIEW-DJE7hnIaHl1cZvdaAMpQZVc4lxk0rSFMvzR6Gx-ANOsKa5IhYQ1INRIeCjV03YOICs57t-YdRYsSoXkeVNS-rFxXdLccVOFE5tEw8zApf6r1d4UNxsxMMagSFuzq9cq2g-R6NuQCh-CaJEhu7d4-wbVcboq1YHS7WlsFTcwQAZ-Y9Cs6RfYjxBwHvEkwm0fctfyHLecTeMmeOx32PxW2V8mJXl-rAWcKqlZmlD86AXXnKGOvJ2sTbr7AtFZUEx9ZVrGOozDViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه نداره از دوره بعدی بیای آلمان؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/99336" target="_blank">📅 02:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71f8503771.mp4?token=nQkGfbxT2aIS9m1iasAWz503DNzsKStKPOLnydd9VLMntl4ZfzqOonlF6YOygPRt6ifIX2nf9Tkm36g89Z3lRo9imEahNHuEaGI6INTLrEtNWIKs1zglX8TA8JiSvHKxgl0L_2dVP56g2o9nt-FqzGZK2kw6lstcl-ZERzHlBkW04RW70JULILzjebrNOLut40PifsHC1ssMsWo1FcghfYXiGkCpoA59O7-3SYRXM3N5XNc0oR8v2cVnI_qKl5vxoSe-q3vmihE7eqElk_QgBGT06Z6LNgXymD0pq0X4v_T0WYbhw6WHW4syYAgzwjh8SIoiJUQJgkS2UIFZR2HbkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71f8503771.mp4?token=nQkGfbxT2aIS9m1iasAWz503DNzsKStKPOLnydd9VLMntl4ZfzqOonlF6YOygPRt6ifIX2nf9Tkm36g89Z3lRo9imEahNHuEaGI6INTLrEtNWIKs1zglX8TA8JiSvHKxgl0L_2dVP56g2o9nt-FqzGZK2kw6lstcl-ZERzHlBkW04RW70JULILzjebrNOLut40PifsHC1ssMsWo1FcghfYXiGkCpoA59O7-3SYRXM3N5XNc0oR8v2cVnI_qKl5vxoSe-q3vmihE7eqElk_QgBGT06Z6LNgXymD0pq0X4v_T0WYbhw6WHW4syYAgzwjh8SIoiJUQJgkS2UIFZR2HbkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
😆
برسونید دست گزارشگر صداوسیما بازی امشب مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/99335" target="_blank">📅 02:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99333">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eb3q8gYWeAiPAeYGx5olpOO84BBh3Ws-Ox53_LRj_ODuO39mwezvYwvXBaQZx-VqxaxDiqALPGIJYP0wiVBBwUgYvDObhq-xhwNVdluLkPjaXR-RNSnwONZlZJAr-yXEhjbVZODNpuw7rGrbR-Dp0m2eexTG_OgBJ8ZxDyC2yAcd3jUe79Y_pQJFi2y0tp0169itKayF7DEi5yB5FWqGjRvakI4Y_LV96RFclSfFwyJBtLHcK2o13FWkgNfSZXfYk-5j-RIxSXzo5t3_aeyABwQEiwifn8nfgLKWMAhaxtbqazR8dHVC7RvopJE6YmGR2EwE8ZkdhRCxhd3xSBocBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyZoO1wvdCCvMw4aC9Zdy3Rk1nBT7G-NVbcurDR_yG_2zTtwan_QEDN3pHGIzlRwJ9b1MJn5oQ5xIfvY6N9GT4OdvI1dSB_q7XruXg69XK4qnX-TVvyCD1ocP4oHB4MzBInMaVYSNgu4QpHbXGPUz-LVBIclFZV3s1_BpyyEbCn7mpfxKVeViqkXHJ4DuLlpH6FV6EqRoRv7ejgHJB_dzdoHnQ1UFy8TKeqOeCzyCbh29lz92HHSLvJkD0lRxeMUhoijcaBAEAR5WrpddpgdIR9VmZ72tLmPy47udp6wMdQVa-8u7dX4wEALRXLRaxVCGkhuEIxCIxP0Ks-hrurZNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
📊
🏆
در طول 60 سال گذشته، تنها 4 بار پیش آمده است که یک بازیکن در یک بازی از جام جهانی، هم گل زده باشد، هم پاس گل داده باشد و هم یک پنالتی را از دست بدهد.
جالب اینجاست که 2 مورد از این 4 مورد در 3 روز گذشته رخ داده است:
🇦🇷
لیونل مسی در مقابل مصر
🇫🇷
کیلیان امباپه در مقابل مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99333" target="_blank">📅 02:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99332">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
🇪🇸
#فوری
؛ بر اساس قوانین لالیگا، بازی هفته اول بارسا و رئال در لالیگا بدلیل داشتن حداقل یک بازیکن در مرحله نیمه‌نهایی جام‌جهانی به تعویق خواهد افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99332" target="_blank">📅 01:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNmHqFfyDPMV6n9Oxozta3yWDmwYSN1p9l6yCkod8VzY_bb4Jk3qdVSM403Uf0xgj8vE2JkRTyK4XOwHfoT3IDt2y784j7Y4Ov20s1RcYv9-xgkpAS82iWNOJlM0Ju-y2htx8Jr54l30TrVSNPzT8gvsifVyD1GWKl005gI3xx9kIBMyLC_VrLir9AuNWsZkPCyFsM3aqne7mZJ-3sPxIiIb_dCfKHc0_AzStB4lL_N4LQDPEQxGb2OP-6oeeOYIG6sp6QyjtK9pvpTcLo4dfDZgF_ANETjRAXIhEPkx3i4PLEKcz74Fhh0Bnt2J4N6J8ydGKpK484q2FPjNtycSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🏆
| تیم‌ملی فرانسه با قضاوت داوران از آرژانتین تاکنون 6 پیروزی در جام جهانی کسب کرده است، که بالاترین تعداد پیروزی برای هر تیمی در تاریخ این مسابقات است.
🇫🇷
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99331" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXgzsmiWrZ0l1iV6EJmMgaqbTxIw_Je2EMWcatXTfxoQ89qs4J7bpQM5UvspK6eb7rd-d1rtapS0gfGOKbFSccAcYMdTycUMjqDzd3tr_uCRBRDwfCIN9gLp3QUWshWOYLRHqciPSnC3Hn8Z2f_b8_gLeC1BcOlWpjtwC2CIGGUnIWGqvlbe3irxxzWoNi-a1W6gTuBuv1ARG243xixbCxcAZ7ujjtxlKhfcC1H_sr8fR9b2Z8CwGuQ5Qoy7S2WWjzvrLRXQ-IXuhqRtXJXjiUUQIL4-NNRY9GlRmL6xEZbY2eyY4QNrwO8u6pn9NbQLX0LOW4KzuwE13VGaveG7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🏆
کیلیان امباپه: از ناراحتی اشرف حکیمی اصلا ناراحت نشدم زیرا در زمین مسابقه چیزی به نام احساسات وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99330" target="_blank">📅 01:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🏆
Man Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99329" target="_blank">📅 01:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oG5-7fMw4i7RPQSmcBXLMe7weDaXIuRviuu-QAg8QBsOiZAeKKqKXMWIVMMSeT3Y7Hu5Rt3wwR0mF-YIk6YsOcqdqMX96-VqKatkjUBW7OAEdc2d_s4spQxV_z05L3NXuDbDdji4-rfztkLB1WW9JCeK-PgvbJ2la18ld6hNLDE3JQ6DFFNK3cr6AhcqF5m5e-S_M5mT3hVgLD0gYdXpxQjb_02fqxA3cUDd-gr-N6n3QX24YnlPbUUkOUGMem8HKqFwsKV8IIcFpIoS7MBK3XvqGnEMyB9mFCnrvDFlV0FEXPsYJmQN-RnCQ1f9HPsBHqhgLMdQObHUVwG2uv6GDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
M
an Of The Match.
🇫🇷
👑
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/99328" target="_blank">📅 01:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuZvz8xU98ba5WvJyHEFykqMUDzHpa6Dw6Wfvuca6u_Dgu8rMfl-BvItjkP6fVIpvEoAepgbTzI5nkk3LeYwsz9NyrxFi8HYJE9j3KpfGOR7nbJGJj7kTyTduJ6p88k92r3C7PX1-QBZ98ta9mJyhsjOtR6ELWCL8HuxEbk_J1iqf6F4U78gDtC_OqSYzTFKP2HVtsXtqzZi3jSaCaZP_3P37mNA7WhbV50z6qbRJmBi0oL8RjBPLT8qKi5x5xunc9Hy1LcGbpOKPsUxoboeFkKwgOSh78ljWUl65TktCZEXc1Fv2rJxqp_YSvnot-96UwydBSBKbhWFeTV_8AoUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
😀
-
😏
مراکش
🇲🇦
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/99327" target="_blank">📅 01:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbZjJa6-l1vIGrVLYMDh7CLZPISdyfN32m03NIb5a4ewozFUGkaHCvFF6UAvr2x4rQ_Y8uzk-rC1MifsKsc0IfAF1oYPBSCG92Je2VA3QZAQfBzJ8TBXMA5QHkD-3c4WoixbM-KX7RpCKZQ2Tq-1--DOA7i_QDyzy67AzNb_VmFDc9M2U4--mDB26KDknYdAR_aP8ZU7rMfIo8FbnOCtKPRDgYbQ3Mg6tR4Rn0kgP-OUA6ofQ6tVLWZHEZW8h9ODa2qDLtdZ1XpCIIdBB-zRprdT2hplUXBJIWtGJqRsw4c2046VOH2h2dP_1ueg5yU0Vk776ObszK0HtKyoq9jL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمامی تیم های آفریقایی از جام جهانی 2026 حذف شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99326" target="_blank">📅 01:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM_sdRj99ue4BgO_6yRp5jxTTtKOjXxzLQSwhKU6-UPZwXWpiyJ8P8VSGk-NBU4bo7j_u55dA75te5jP3HlTr8TJWlwT_HTxClF6Fbb5l78YUnhqOtVojspChCikFZ9IyQjmMg09w2I73vvFjfm2cObCzOxdUrLb_WIubCIIClxnxd7cblHZRYIVlht5ytUeDzGYKRxd6Q6vIdOy2gHzvqxuwc3FHdJPpsCoL4fW5vlTRHrUfve-jH4sXFBYzj-yy8fUXdm7xjrjVE0vTYeyZ15dPpSN0qCkXpXGYy7ul2i4JDtVeQDMAAgSqz-Bfkw1o4USAS66YxaQH0Wf3HqDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان با یورگن کلوپ بعد از پایان مسابقه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99325" target="_blank">📅 01:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPsHUZ-yC5_M2TaS_SqneUVJ1e9rbCUUJRRzXxEai46F-G8oS4XL1ucNBWvqs4AiFPrffo6AS_J7qCzGXaC_LdYvkGCest99OmY8Vk0xl-U916y9peCsFmx8HippmIx_cjpMJwE77sjB9s0PFidV6b0nxNlKnYjs03d0J4j32cEpjhlbn0qkCiHdx8w4Y2Vbuu5VirUGH074LBN7Ooy6uXcmVwhgLaTOEAS6xeUXzaYdE7uXtxxiMr0LLTJnDaJnow9SG0cDNH0E5hnQQymz4YxKSzoEiUIPppKlSPy52Tcs1VJP0CBaqaexJag9nwN3tANLeSVPHpZtwQaI1NlKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• کیلیان امباپه در رقابت‌های سال 2022:
🏟️
— 7 مسابقه
⚽️
— 8 گل
🅰️
— 2 پاس گل
🚨
📊
• کیلیان امباپه در رقابت‌های سال 2026:
🏟️
— 6 مسابقه
⚽️
— 8 گل
🅰️
— 3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/99324" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLeCAguFeyMzkcLCEAaaOP3H2GfduA6MzJce1kn4K-FIS7vTQLjQPiO4xL6uidpeB-cyNJngq_NhIy5MHOydV_DUAxf_HbJdiSHSlxLksh5IlHI7EIs0iFIa3QKFW3In3JKYOb6PF9f55NEilUcGa0TRTt8gUFV5Lw28jATCQYxchlk7c2BDLU7Sh9CfSJcXU6WRDSGzm5oSQReIBVxxzvCjX8M6dfFlZSZoOihTxtveP1bkmX2UW20R8yp_n7JJHDSow7JrWqnFR0eiTyaZQ79BG81OOGSiL18jvLkF7J3kkgdDDeQiiuNKEmFdnSjWn0jZvgNdCgAJw9VknQjmPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آخرین آپدیت مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99323" target="_blank">📅 01:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erdoTDNKndyU0JVFHYxt2iDwov2aTuSCj6aFSFG5M_3sieLfLouA0lJ5zOWPaFEQNlGHpmxtO1VxtVc9wtrs1P4xVLliWZQjqWFe-ILvOFVK6_qgOiEIOWgI9f-0bbSuAywCdOW1rzKNgnEcjLEY_6PFaMAHgsphE8bOZ_zzXYeVso_4cOMNJvcg32Kf-SghYOkou1AadMV3olkByKw9BQbhSoe4i-WdSfOUk8GwjNvv9knhxYT9oo46cHjqbKIK-_XwuyKZK-5unkfaMrdXl3u0WrFW9t4nMPMiUmqy2QMJiMTpyAyqpOPcdqczFVlasNJ80N3encSKWJS9ZYr8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 بازی در جام جهانی؛ 20 گل، کیلیان فاکینگ امباپه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99322" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99318">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tV-ZeJy2T4Hhaj16tGBk6wHwQ9DPQ2XoPMQgaDamiIi8kcIrGlAIZVWfKHcNVBSzt3q5UZqFgHgc_Ys7BIFj0mifhPqXCkO1gWMauUbvmitJ41WS3yrECDGgphR9Rxp76nDGMjFYMqhRgqByvS_4sfv6NS9X7HUbWqWXBzCama6yX4yRm9E0TfwwTA_SqfiZH_w4uZKgXNSoWZSr_rOLKB19ZHqHmXXhdjGcqiaw27YsynGKzerJklSaINgfthHa_Dub7UZ_n6JLPKOFT2P6GQjqRSoJfBgSnNPfDpCikJUW0JhC4ZcQiPcP6KILBYmcwup8I-R9gxtNkF75sZe4dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U0WBEW59JSmDdFzXo66ncZktL9x3ORfmzBt9YL7WY1DZ1kz_yGZTpuLuTFodJ8wcoeKxZlbOTOoxImYPS-ryE4jNphIquhpXhaM4lm-JvLc3lOnyDXN5JUaafOKwoQHYaRg-FlrkFqcppoTVhNdGxNZ7ZiSd4e4p_12LJWWOUj1_aO0nClmCjyxMpao2Nm4FIUfUG7Ls2xD67CIb8SpVOi5B8RsTXW_VqJjZCynZ33ZSeQ_Skk-IRgRmoLS8sl5ZuwpHOiylcDsp1rx-57ZXNAkLAGBBRb5J60CkiiCbvdfPrHHLqcnM1_RrfabZXhZfJh1xgZFUNjxKs8_gj6YczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sve9xS-_xwxdB8WBi9zrGjtZGN0ofQtce1SQfSa_zoydmRYsBUsSDlduD8QtHsUWvyvFZUZgnXRr-xcD6cFwk9LMR0rpoQXMKtY3NIdpe97MoqMbcP1vBdp6VLxHFIoBFrPQaE3Q9fPEGpaeiZuMkMgUEIc6bG4Hb9vucMLHQHTesDGWirtsS8JLKS4O-o2r-p9ckasyXtU3eOljJq8vMkpC5s8oL-72Gk866BZryQTv-lb-Q-YJwSygR_TMLoFBXGHBjjryyl7QTWtTXbOXVwIWcdCfLlm1LpxH1qBXwcAfuMF0Mnv8qMl3elqmY0NfAr9CkI4Pwo5CCDk1F0OBgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vLtNQUkx5gGZSvUznO7ZYJ_MY-GWcPAZD7rh5MDG8hm7rDx4O99y1qKHNqJ151xyxMq0JMdlqvlhcEvj5cumVEQIBQNld55pF_ie2s1LTzQr-8mhe1RmDss7NKw2PZFChlMxwYe8SGrQXwORR2HlmjyU1z5InNKp_KFSO2dQirCx9jiVCNpg046wTAVFAeDNLo8HXn19BvAVfRUmQm-Rqr5QZCtU_F9ZgigSi1cigvuks-o9VZsxYH93I5ZqBARcl9CWAi2h9AX2Sqi9TbF1aYWj0obpPL3GwX2Lj0cgScv-2uw2olUwBbe6ipoecVSAyC6J-SsQ-ywLFECHlTT-2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🤯
📊
🏆
آمار گلزنی مهاجمان فرانسوی در ۶ بازی اول جام جهانی:
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
کیلیان امباپه
⚽️
⚽️
⚽️
⚽️
⚽️
🎯
🎯
عثمان دمبله
🎯
🎯
🎯
🎯
🎯
اولیسه
⚽️
⚽️
🎯
بارکولا
⚽️
🎯
دوئه
آمار فوق‌العاده‌ای از خط حمله وحشی و عجیب و غریب تیم‌ملی فرانسه.
🇫🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99318" target="_blank">📅 01:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99317">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc7i3d8SdlWPuyawUutIEdgOPQTZxTTiEMj2MHzARKidLMp-wqJ2k4joAh8r0s06HpMQl9C-KHfMyfK92IbQ9oGTvKVa72CizaQ_KY2VgrGydTFVOA3bUW1jSNm1Sqz0N9Amfp941IJ-tyv-a8Jei21Kl3AV9wXuwObaNT-bzN37_X-KsaZVE1ayxmVrAjtDTpk8hzXKCA45Dqxdsk4ufx-PrsiotAhOR5wXkIrl7i9kN6bDKPmNfI9nGGd4HNKIYP_Q9YmFlNKIrNCQgsbhrvo-B0EQrg0b_GcKsZI5sBZV5nIVH2ODu1Hzu56x1RyOjW20BUc1lgZ-WekU_AaCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه در 11 گل از 16 گل فرانسه در جام جهانی 2026 نقش داشته است.
8 گل
3 پاس گل‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99317" target="_blank">📅 01:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99316">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkJxw9Hbyr5nqwgyi8D55fCs1pvk_JXZypNeOSzl4HRMiJ1xeAXBsN3DEWDj0gFOkLOEgrogs_w93jpLMCR1IXd5VBJwe-YgWaYJgjUVfaTDlr41d58pQch30FKLYJ1W6v8s9PgHOh88xqeuG4yrJ9kvookx3c9DVc6RtLH6hAJTNiUTAGzhE2tkxDGF1nU3dNwSWA7kwktNSXTxlYROPJmRwXb1TkniO73WWahrBP_7EIzk_yB64Rt1PsJLe1WjE8-UUDEvkC-0LgIj5kh5Sv6ewH_ShsdySQBcu9lq1K_7Zl9WHk_-IH4M62N-KfFKgPoarItNM4_Lj0lhrFbIUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🤯
🤯
کیلیان امباپه همچنان در حال تاریخ
‌سازی است
✅
اولین بازیکنی از سال 1970 که در یک دوره از جام جهانی به 11 گل یا پاس گل رسیده است.
✅
اولین بازیکنی از سال 1966 که در دو دوره متوالی از جام جهانی، بیش از 10 گل یا پاس گل داشته است.
آقای دیکتاتور کیلیان امباپه.
🇫🇷
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99316" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99315">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99315" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99314">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MuRYALNu2de5H1HwbPQz6qJ0VWehI6rUl5wwxEnmdughtph-eCTQ-X5DNrEUDuXBozrceysZFsuRqn6iq8SYU8ve_63WzdDz6NOYZwCx_fGc79OqtQKJLvOm1osRE6u9fwg8eDQRLZIWxSz32tJRS0vSNfuT0hnbCWCM2U00-rILTrCHxwkFg9_k40hMCV0Aaz_gWiu-f2KZQOWz1wrkgSPNZK3i1zh8SHSFxd2NZmKAbf8GnhUvEL4cHuQI8RgFbjbTwySsPUPjX2-6pXkowMbC3wOBeeBgvX-EVK8ueysOsVR1cdofH6X4PqFa312xmZMMri-9ui2CFzLEmXSJiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99314" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99313">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smr_d_luRKySc3vknZ5p3UJc3ehW4qLksc4MbbP7NjX-g3oInr3A7nSyGeRnETF0sf3UPbUkqscXRrsecQ3J422g4u9OeykZFRaX_cY2IHO5fbIazBPN9f_Q_hr3BPwL-QTNoARbG0urSFhTbIVzLWoDoZqNqAjzLcAbNSpNXZLF26QwQ1uy1KyylcDeOEi9DfkFiCr9uNu7K2flz7g7lyg84mo3Fed2dECNjbwW8m7YEn452FSW5OEPFGJcO4ZfIZD001leJ52WVZAqaBd4ZgEWty9BUm-drPB3jajgW9--gZqtL42AzNoXCEuE1ih_fY4TjXJqPIfxF2zsmOzHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
کیلیان امباپه بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99313" target="_blank">📅 01:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99312">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj7W9yCeKE200xV-XIhuqDnbodz_zuw4uvs09fUK3acFZkh72jCs5R2mFcVgTWgyFq9q0rcITKDWPlMW-3sA8b6fXRHm0OCss1xGoJdSLZVViSHlDKjQaMHAOOojRJjDCp7jsDx7H6iI5PCuXpaVQQyqIsV_Vx4a6s5x3ZIBeIXoudhYYIOPNfn0J5hptJzjv5gmiIWvHe-ede1uYdO9dNuuK-m9GdS51RfHhU1iHeCmrTU_GTZ91r-zVF0bldecMthl7iHi7wK685oqf10LqNh7V3FlCcyh0q2Kcof6Pcp8sTVjCbc-4g29xhWJkzaAWDJ58o-rMKyZ2LW7SKl6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنده دیدار فرداشب بلژیک و اسپانیا به مصاف فرانسه در نیمه‌نهایی خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99312" target="_blank">📅 01:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99311">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUjEb_o-PLDmDXoXrt8q8lUEedKAFcTCAGA87_hb1ZslbrnIoCrIbRQ3o9E-4-Kah14PhqrosMYQt8VBUlWK79TkbG53y7lgktbue1C6U8CDO3fJZU6cW0pE6uylY3Xr3eHcyN_lmAbs_vWZwyV0bCfB8HXZq7yW-L67DxKWRxLSbkxkIXp2ncgJc5Emf2nToSWS-Q_0jrAgKjS0qrEc18T46_VQzZzi_pdloi4HPhDIuRRVkVy0Q0xi1DrFhFWfDwfTL-TFE_Rg6YHJC-YpScLFlXYfQ0rwzCS3nsK1na0OVUVXWfBJNfmD7U8H0wJ6QQwsMsE_J7ShCqQB7S28mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|اولین تیم نیمه‌نهایی مشخص شد؛ بوی قهرمانی شدیدا به مشام می‌رسد؛ فرانسه به رهبری دیکتاتور امباپه با برد مقابل مراکش برای سومین دوره پیاپی راهی نیمه‌نهایی شد
🇫🇷
فرانسه
😀
-
😏
مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/99311" target="_blank">📅 01:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99310">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nROumuTucG_tDPLlxgAuJWQdCghvGxWc1Avtgd_iK_OupBiNJL9bg2z_DNhqua2hXHa40k-KPv5kpEPR8lGZHdNj72Z4T6kVyBfWn5h9Td7zdKLqJr0W543zO4KkZ1vN5cuzXHScQ9WxK0-JgTG8vtAjBDufId-F2mpJehdr1VbkUY6lrlMzIE1Xmjb_SOBQh0wWOMJSDPihduTFsW3OKEVTdSfXKFsD_Z1wt3QfXBs4f30QOqCeFTuo3vssXwD6abufVrvwXlfuueNbV81GB2Og-bFIKcpj9-p46aDw8Qx_0Bsew7SntW9qOzHTuG57b32SmmSBY6Au_Ck-IHYwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این داداشمون چرا ناراحته؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99310" target="_blank">📅 01:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99309">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxl9rz0aUqtuAkgLjWU9kgY0zxhhPcVOPWjLM5j_5rmTJOkHsi85fWlZrWS0KMJYPECpWVYX1A9vERviviVxy_lwfC6eVdooPezF5HYhPhQySqv9r95R5eOw1bnoJ7-SAUNGh8g1mIWym8bTKiuc9DNhMQQPTIFhrpxP8KYcwoxzNklZUmhPllMydlpZdtv4otFv_ZL_w8RUCsku5WOU2LAtUt8m6DHbJkCUv3y0f4euxx-bzpK7Zk8AG5OREIB7_6JELglZpbeLCU0XTmBv5-OwRHRXFYYuT6He__UoBlfsehRIhzVz85HkF81dTnhVjWbcvllli7uBRztJpgo40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
کیلیان امباپه در تمام مسابقات این فصل:
👕
58 بازی
🌟
68 گل/ پاس گل
⚽️
56 گل
🅰️
12 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99309" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">باید یه تحقیقی روی آربلوا بکنن بفهمن چطوری موفق شده بود از این امباپه هیولا اون شیر تعزیه‌ای که تو نیم‌فصل دوم دیدیمو بکشه بیرون. این همه نبوغ نباید یه راز کشف‌نشده باقی بمونه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/99308" target="_blank">📅 01:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99307">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5N-epY4b9-jDJp4KshPBqcTpHsuij0XAR51BDtRu1T77-_4Xc9AjH-p9qjrrrfF_AomAKMUD6gbLAZtfDThutF_7gTHzqoIrZT2LX7xrbjstbVAl3JGMGAEAqFAIzeAImbMaMIr2eX9UgMeaIg9lEA_JetL5xQZ9yOJxJ4En9YEVFxZ4Aqp6Uv_1iIfjMJng7_VG_fZT-_7tusErC1Kj12UkntBdaQrT0G2xBbLKN1CN17k3JKWB1XBDT27ZAnnbXM1IZWmjkw9rO1oXfaHETDS75wNvnrMKC5scjpnZHP3yl5ae1ZoUMowiUDN4a3eDtVh3TmPyHeXnBNxihT2ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لحظه‌ای که لاکشپت درخواست تعویض داد
مصدوم شد یا خودشو زد به مصدمیت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99307" target="_blank">📅 01:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99306">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امباپه تعویض شد</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99306" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99305">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3U2v47zSIacGaa1ugiRqcbKSlWsSoFlLOpkZ_aVcmp-9wmFFeTvvE1nYup7LA2iW2MUnnLGVwIJ1pvJW0CrdUKMxDowUcax7ekUCliiJpB-Z_NcF3_z6ay_LiR9EmYO5C0pC7tsq41sMkRLDolxeq4u3RZwe3j6ChYs-VZANPxRZfVwz3B3e5KaZXvLWQzjeXSu4M3090WSCGbx3dVB-toZ5rU_wWGAuByx6P6XcfllnCv74hw7639UB230OSpYHoS7B64arIWVoRh0f36iAAkzuOOh2dAvSw3W5x22qqOKvKgvcQzvbFP37wAV9tNXm1huyUdTYCI5WfirKUkLYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🌎
بیشترین مشارکت در گل‌ها در تاریخ جام جهانی:
🇦🇷
🤩
[30] مشارکت برای لیونل مسی.
🇫🇷
🇫🇷
[24] مشارکت برای کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99305" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99304">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f95dc0a96.mp4?token=riaIZ0xfIo3YZD_cpPzmdN_cVZkL2bxOLYy-i-klhSKUc9ntW77EjfsnRPnqYojXfFwtUcYmoBVIG_vufDBazUbZW51PUTlntRb3o7striyuhoaLl6_PTaLFgdEqhURI0S7xmSWwwp96oQUdBFqI91KbedR1cjHw_s9Dbtx_4nNbPduNyTgB4UWea6Faklkb58VOAi9xNmGCQ4YaJBWVuNaaXZ1wUXrjGR--qyPkNwkGQjVRDrMJiewzUuesji63NbMJ1IY551765rpR7lAz-6zToYEKnFL2JXaQnNTGJr2dfF7LVPDq_2lZSQJKPScHJ3kbYf1txcZ1KPHthZ7vOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f95dc0a96.mp4?token=riaIZ0xfIo3YZD_cpPzmdN_cVZkL2bxOLYy-i-klhSKUc9ntW77EjfsnRPnqYojXfFwtUcYmoBVIG_vufDBazUbZW51PUTlntRb3o7striyuhoaLl6_PTaLFgdEqhURI0S7xmSWwwp96oQUdBFqI91KbedR1cjHw_s9Dbtx_4nNbPduNyTgB4UWea6Faklkb58VOAi9xNmGCQ4YaJBWVuNaaXZ1wUXrjGR--qyPkNwkGQjVRDrMJiewzUuesji63NbMJ1IY551765rpR7lAz-6zToYEKnFL2JXaQnNTGJr2dfF7LVPDq_2lZSQJKPScHJ3kbYf1txcZ1KPHthZ7vOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌دوم فرانسه با گزارش عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/99304" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99303">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTvscWQV9UeNyKSnn9i7LO76PKK9WnRVyuhRrvKYs0dHZI1r4h-lCEbqv3RO6VWWZz1eW1ZysvIUpVsYFRYtDZcebcEAcyg1syIr-gmiJpisj6TgaxDlUri2Dovgr75B19604GSDyodl4poO3TZ9QRsMt8kEsahzezGcr5n47FFVqEyLJCwz4uNW4dqPgNNryNOjya5b3prrvenLiMVRkqqUus8Ymtyj6WyCviwu_u80tevWQPD8tI8UBVXX_BcoEuq3A5vIFzYTfWZOPbZOQ96RmuHi8PyhzXKsv7VaTdWh2PPKPqVZVv1rrUM87dv2K88ckCx_aODDPYUJ3IOngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار کیلیان امباپه در جام جهانی تاکنون :
20 بازی
20 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/99303" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99302">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آرژانتینی خایه کن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/99302" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99301">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چه سوپررررر گلی زددددد</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99301" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99300">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دمبلهههههههههه</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99300" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99299">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دومممممممم فرانسههههههه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99299" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99298">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگگلگلگللا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/99298" target="_blank">📅 01:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99297">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4PVI47rtr7NVl2LwwYTp2OFTtYBThFawqGU6yHxPzC1-CbA-2u2MU5bI7sid0rRGe8WMwmvIO0nIHbbg-aCZKE3sP7sXzTEydq-4rj_7OTOC0a1N8RNmiAPDE9HvJZFC9ir4QVHT-8LiVb9PYnJprelVpMWVKm6jVK4Uwn9P0iDXnTy9OC5lB6z_ApuSEUxp2ZHl-w0kJX52MHa4cAVI25bdaFPuEmTaynaG54NwOLCr9RNZsJATHxRJPn7PgCOkD7IL2vOXPofu678GZJRqQiq4KqWcDa0b9S6yLJ-y5nShgb9wzxxjihXl0Rz7dB-WN7pgwy7Ambd6WOa0wWyAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گل‌اول فرانسه به مراکش توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99297" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
