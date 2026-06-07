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
<img src="https://cdn4.telesco.pe/file/iTP5dEGbN-JKPgO1U0Og-VqIdnEQwGx1lHjREcYd_j76Fn0z0BlKPAdTNEHVPv400Vq5kzpnwPXCPhoUrm8hmleYnm-JBRtj0OCbyQyhiLWmNBfqjfcOv1X5ZrL3C6pQWBle0TCdky2SWoFEVmh1qjwIFlb2HJsU8jwhDn80ZJ9a5Z7aeN_CSKPnw29BwiUM9W6H71td3auhpMZZb0prWgDatshhwRisBFVdYX5WN0UleM2xynIP6lZJsFEPjTpF2ZEGfY0Hst-gWOeGxqaBUuWO4F1pB7kV1KSKPiBBqn7MGiVfW7yoTTMUrR6j7dBLJ935PxL0TDrJCmRM7Gm5aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 970K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 18:19:09</div>
<hr>

<div class="tg-post" id="msg-125819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip6J4da-JFJL5siRT2P-XgjBZOjkRRjBpuHQVhYmuWPAz02iRfXXrJh0jEHSAEQ7_wIwKcC8EAJqlbephybJzUqbJTxbnrB6ExJaRx9eVT2_kJO6zrv2OobUJu5PjETKytvV47fqzesH4EWYSAJkVSPUXFJ0JFPpXwNhKI4CCiTeni9UGmLNe6xOljkmhAKaiCsFi4g8eF7mhv95F297vf7lz2BE4TWTYECoWAJ1l7frON7_gq9tSozUBGspC6w46ui7bqbYPBJXmX7L7g9-TPZtR3OD9t0VNQh8hEGUvK8u9wvu1dtvE-gskIEZIvY9kDlSPDgduiGnjWauEtqYuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در بندر صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/alonews/125819" target="_blank">📅 18:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
احتمالا تا ساعاتی دیگه حمله به بحرین انجام بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/125818" target="_blank">📅 18:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125816">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDx889t9H0wsPIbdJmWzfOBj_p_ri5ch_UREVFzUlQbr3v_Dh3KXXsR9a2AvDjQvJweR0bdrZ9co8uxp-ZIcq3MsZdTM4lXJh3JrAN1fGoxTSkpPXhEH9LBpV8T7ZxBzHGSwxwoI4__oL7N-ecoI67Yluq66GWsNL9hXXFi5r2q3FuYJ4T01Kz9v5Aty2BTx-r39GU92j4jrAuhjwRMskLCyslCgUxdDM4Fl9YckqrBpMs4UXQbLeM8S1Lo3BUMv-hOe62HJxumXam6ZYGJuoRC6Wh75q95tusZJmMUIiDWiFU1DbQqamZpBTo9DSfHHy1-mylzZVnyrnZUNwNuewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zf_yYZ_JNx382xSyoZ9i1TPb8iRVazQ2FPr0l-uRi_xA65i_-s52uhE1DPsXSkHamECCCYXU-pzcitgbnFvQSxyGFHuPLzqR-hH8GPh2rr5SVzFKYZqplehkajaaHMb4Si6pQ_XuID-FWhxhu7J_CylGkte3iFgfetSVYzoTTT_bQz095KITqoVC93qqpXtHZJPtP6976cmXZXclzwV7zRAb2ei76GMwA9UbvxpvBS9qJQqnHtlyW9sKylngEBk1LcC7Ddq9ruIVIk_arFXkmjJgxVbBqgzwSl5LVpq4bXvKlWPg7jfGON0Ti_OS3iH8E4FkbdhItJ3rZmgfueu4PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بمباران سنگین لبنان کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/125816" target="_blank">📅 18:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125814">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea8e6d5591.mp4?token=ez5M4SUof5lZXa8WIZYiKhPb4El9Wdq24bEEem-xNaQDB0EAUVw5wgAOapDlgRHzA5XzeF_vnvFwVA5iJslo2JRVcVFjFt0K4MneFzBHAJGzbYXeBbUd1KcPcLMOGME_fKnsYAGD8HNuj458c8dUVgw2Fvqq5EgbqTGnWVP3zRNjFuXd6nA3ySecK74G-r94YcNIMSmbD5xXfiqWEcA0bpLCF6nfJPYHaMPZ2wJjXzssm1PvRR5E1HB-wbN_5MqDWNx8XuNtPnCogAdU1ZEDiQ0L2f8WSGayDUvWb5iELqGD74S-P2RpiMLhu5V61RwmI0iMlpT_Sox1PCtO5R7ffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea8e6d5591.mp4?token=ez5M4SUof5lZXa8WIZYiKhPb4El9Wdq24bEEem-xNaQDB0EAUVw5wgAOapDlgRHzA5XzeF_vnvFwVA5iJslo2JRVcVFjFt0K4MneFzBHAJGzbYXeBbUd1KcPcLMOGME_fKnsYAGD8HNuj458c8dUVgw2Fvqq5EgbqTGnWVP3zRNjFuXd6nA3ySecK74G-r94YcNIMSmbD5xXfiqWEcA0bpLCF6nfJPYHaMPZ2wJjXzssm1PvRR5E1HB-wbN_5MqDWNx8XuNtPnCogAdU1ZEDiQ0L2f8WSGayDUvWb5iELqGD74S-P2RpiMLhu5V61RwmI0iMlpT_Sox1PCtO5R7ffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان با تهدید‌های ایران، ارتش اسرائیل موج سنگینی از حملات را به صور انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/125814" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125813">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025910fe6e.mp4?token=rQxt55Yf2_UXJLUF5Od_68WCFRfNSw0DcJuzOgP2fljkI7QpXCXJ0LzP3yb6yhD1visOIFLet3sRpiY3Pbf6PjTDuaRPBxTmlz_dAXe6mW_9vPFSbwK6Ys4mDsZhZd8yH1PIsT4pk-WZXBcbbGSA_aCNOtJp3ulMwutqNjSRTEz4k7ampkVttTYNkV032eYl9ZDFQ88IYQh7AURlBQm-kwC9ednfW0OV2Wz8s_e4m0XzlZ9QacQviYJHOz3pOHs4ve5O3ZRBkQFDYBXnHQ25oMOLWODmQt7kXLGrDxDw9orSp8HqYCqQSTTbJfrYXJYDXuykg4L436EAp_vp8BHUqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025910fe6e.mp4?token=rQxt55Yf2_UXJLUF5Od_68WCFRfNSw0DcJuzOgP2fljkI7QpXCXJ0LzP3yb6yhD1visOIFLet3sRpiY3Pbf6PjTDuaRPBxTmlz_dAXe6mW_9vPFSbwK6Ys4mDsZhZd8yH1PIsT4pk-WZXBcbbGSA_aCNOtJp3ulMwutqNjSRTEz4k7ampkVttTYNkV032eYl9ZDFQ88IYQh7AURlBQm-kwC9ednfW0OV2Wz8s_e4m0XzlZ9QacQviYJHOz3pOHs4ve5O3ZRBkQFDYBXnHQ25oMOLWODmQt7kXLGrDxDw9orSp8HqYCqQSTTbJfrYXJYDXuykg4L436EAp_vp8BHUqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات بی امان اسرائیل به لبنان
‼️
🔴
صحنه‌هایی از السکسکیه، جنوب لبنان، پس از یک حمله هوایی اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/125813" target="_blank">📅 18:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125812">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">💢
فوووووووووری/پرواز جنگنده‌های اسرائیلی به مقصد نامعلوم
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125812" target="_blank">📅 18:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125811">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMeeBj7S87MV3Xw_Dga5c_jxb6nsmGnIQkQCWVIEWVw3z5UjvDK8dt4eLL0GeOx6x1oGdE6Y_fqfd2OaeFtDVmx-VKhWkqbnw7RVPnfjxbbrkVHrVSuQi78CepiyKre0BHOta2-EenKFlarFWh6ytieHF8KrMDan8BQYexOm1qZCPCkZ-Y6s4uQEp4vONjzvPzcIwoGFtYqTSCVXtcOwg-8igg969sZYIkZAybWf7Ie9mrwh2yq4hKMIcM6-8kDEOHwwZ3gDpfCWxiRzWZXaoZyQpSD0aSffBe7gQWmLhBJXF3V3OvA6a886fyg_aHsAU8w9SpX4jEtUwokTEgMhOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125811" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125810">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/125810" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125809">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
اما احتمال اینکه یک عملیات محدود علیه اسرائیل انجام بشه خیلی زیاده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125809" target="_blank">📅 17:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125808">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
صدا و سیما عملا به یک رسانه زرد تبدیل شده و هرکی از راه میرسه موضع رسمی کشور رو میگه! عملا شده عین میدون انقلاب که مداح‌ها سیاست کلی تعیین میکنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125808" target="_blank">📅 17:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125807">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
تاکنون قرارگاه خاتم نگفته آماده اجرای وعده ۵ هست و تنها یک کارشناس تو شبکه خبر این حرفو گفته و این کارشناس هم پیشینه متوهمی داره و سالهاست میگه باید جنگ کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125807" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125804">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WViAWsco_IUUil2s9w4_thqySoJQLFcns8SkBzUU-TgNQJHGBGYafZQ_bhECkicP9zNF4S_RvV3VsXTpWNrUMAO83OqXJTeyXrwX9bgAdDxTclzxWT0P6ov89ai0F9uJ76ZfoebVXfnuMaHWR56k7OG5Eni6947LWXP5xtiEst2rs4J0JxK0dBvetagij81P-c-6erqsQFmtVC4qJbJLpCTO8hwYJcYHH-t1fywkU5duK2cOtEqDN_eVN5gUxHNN4Iorp5JnTDw-gmKD2yx7A1eGDF6Rjli3sQquLHqvWBPsy7pHzx0woV3L2IUZqBh1vqSkxLrAdp5sH-pJNua8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c821a588.mp4?token=DP1oCwA-4yVWHbKcI0TPWCX9A69OEHHE0o0vlzjhNH84hrR8qWNOF0JY9HS4xlrwEkemD53cnWAh-pxBOZxVdiq7I09ZLNn465udn8diSyMs2VlDD4yq7tynndMCom9sZ_yPe0LGq9r6BoW_Q1ItNmvnMnwC58RI8PmXBwecMdDGQVtm_Vpt87VjRyxAPBdOengkIY9YqcHyHd-rKLA6SNl5DkuKhB9rbGkunjc4bIQ-NEwrAnYz-jPmtgi5ZEa9wjOzhhahE9XmfxHcA14vSLhFkXMwnpMsSINSSAT0m2juvZ6unZFnVNB9akQHiX5bDozq0KhBiq3MD2W6kqPCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c821a588.mp4?token=DP1oCwA-4yVWHbKcI0TPWCX9A69OEHHE0o0vlzjhNH84hrR8qWNOF0JY9HS4xlrwEkemD53cnWAh-pxBOZxVdiq7I09ZLNn465udn8diSyMs2VlDD4yq7tynndMCom9sZ_yPe0LGq9r6BoW_Q1ItNmvnMnwC58RI8PmXBwecMdDGQVtm_Vpt87VjRyxAPBdOengkIY9YqcHyHd-rKLA6SNl5DkuKhB9rbGkunjc4bIQ-NEwrAnYz-jPmtgi5ZEa9wjOzhhahE9XmfxHcA14vSLhFkXMwnpMsSINSSAT0m2juvZ6unZFnVNB9akQHiX5bDozq0KhBiq3MD2W6kqPCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات شدید اسرائیل به صور، لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125804" target="_blank">📅 17:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125803">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
منابع عربی: تحرکات گسترده و انبوه موشکی در ایران مشاهده شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/125803" target="_blank">📅 17:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125802">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/شبکه خبر: ساعات مهمی در پیش داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125802" target="_blank">📅 17:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125801">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
العربیه:پیش‌نویس قطعنامه علیه ایران در شورای حکام آژانس که ایالات متحده آن را تهیه کرده و پیش از نشست این هفته به دیگر کشورها در شورا ارسال کرده است، ایران را ملزم می‌کند “اطلاعات دقیق” دربارهٔ سایت‌های هسته‌ای بمباران‌شده و ذخایر اورانیوم غنی‌شدهٔ خود ارائه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125801" target="_blank">📅 17:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125800">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
العربیه: حزب‌الله پس از بمباران حومه جنوبی بیروت شوکه شده زیرا مقامات ایران به رهبران حزب اطمینان داده بودند که اسرائیل این منطقه را بمباران نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125800" target="_blank">📅 17:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125799">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5346db6cc.mp4?token=gUR7KYmD_LpeO9x26hI-kYRJxicB4szB2cGY5V7gwtLX1QDXAY_jq5Ljhi972EmxEVvF6KrpB0WclVrj2_A3XfYIVOCn9afAUU_HXluX_27lJYtdskRSN3dZqfUpDcEcREHo7dui74upkX0LQoiDBfXFd7MSmg-X914dvP_PY7SgagarJ6RY3Xclx6VCVQ03s5HfgtLjNxPBWXvrVPtUI-u1Fv0qOG8YA4pRQGCUX2goz8mNl5qWcqsigGx9Q_foAUKZG0c-0_IRc7nTwvJ1_ysw7HKA2hktyu9OyVWCG0Vs5KtOHiqcsocCD-KVBvqSSuDXnVAxyHiN9iYU4dFbJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5346db6cc.mp4?token=gUR7KYmD_LpeO9x26hI-kYRJxicB4szB2cGY5V7gwtLX1QDXAY_jq5Ljhi972EmxEVvF6KrpB0WclVrj2_A3XfYIVOCn9afAUU_HXluX_27lJYtdskRSN3dZqfUpDcEcREHo7dui74upkX0LQoiDBfXFd7MSmg-X914dvP_PY7SgagarJ6RY3Xclx6VCVQ03s5HfgtLjNxPBWXvrVPtUI-u1Fv0qOG8YA4pRQGCUX2goz8mNl5qWcqsigGx9Q_foAUKZG0c-0_IRc7nTwvJ1_ysw7HKA2hktyu9OyVWCG0Vs5KtOHiqcsocCD-KVBvqSSuDXnVAxyHiN9iYU4dFbJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور پرتعداد پلیس تیخوانا در اطراف فرودگاه هنگام حضور تیم جمهوری اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125799" target="_blank">📅 17:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125798">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
خبری تحت عنوان پایان ۶۰روزه ضرب الاجل ترامپ به ایران فیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125798" target="_blank">📅 17:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125797">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icpx1ddMR1QPC7H8zvYE_aX4QgEvk9EY_R6BZ_VShEWVGabyaBZZO_V-0dEoFoIDcQkH3K4MGNrJmrtAp1EHG7FFfekyfXuyBqaXPjF-viAHUbHWI0jXXwBxI8USl53jWQsazVxLLvXtHimCM_hLtaGCc9OsPk0-anNRSeknH3Fs_mdVSO0zf57yEhIeDeKBG90LkEvFxXOicR5bYPCt--3tLbFkSLG-OPRN0c5M1fniqXt394ya7hyAFkgUAWXzYLWwqr78eOhp-VpMyn2Vx1eS-lamKrMb82bW3rxxA3liL4RAdxt-rx3sryd_BfVdBvPSIVlokmzq4VxcGCoBLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
👈
نمودار تغییرات قیمت دلار از ابتدای خرداد تا امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125797" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125796">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری/جبهه داخلی اسرائیل: مردم آماده دستورالعمل برای حمله احتمالی باشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125796" target="_blank">📅 17:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125795">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ به ان بی سی: ایران هنوز با ما توافق نکرده چون برای آن خیلی سخت است‌‌ اما چاره‌ای جز توافق ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125795" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125794">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کانال ۱۴اسرائیل: حمله به بیروت محدود بود و ایران طبق ارزیابی‌ها پاسخ نخواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125794" target="_blank">📅 17:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125793">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=VWkMOFcpbFE5edCiDvszY0EinHUfO-jVuS_pIldxtwNuiue3INzzNAzf2n4BbeK-pQ-ieGQC-aQHxMI4f2l1Z9i3pNDc2kuBkHst0-xD7TiueOinqSA-bmtbod9TQITio8L18K-4zcIaJ3VV4tl6RyW_uMrJl74UZAew5WyzKsCV4Jik6uI261LMBT2JSvzY8lEgX9fX7o9RdsmrM-b8IGGtRSs1V8wBU7J786y2RjmqGJxTWpzqSGNPEAEixuBR-Xs7C88luAYeCjdEo0mz6zsiZEHiFungcxDVCcOuIIpvqlnJx9rsyNz6ginl3PGDR-IkUw6bevADvmSHrxLCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=VWkMOFcpbFE5edCiDvszY0EinHUfO-jVuS_pIldxtwNuiue3INzzNAzf2n4BbeK-pQ-ieGQC-aQHxMI4f2l1Z9i3pNDc2kuBkHst0-xD7TiueOinqSA-bmtbod9TQITio8L18K-4zcIaJ3VV4tl6RyW_uMrJl74UZAew5WyzKsCV4Jik6uI261LMBT2JSvzY8lEgX9fX7o9RdsmrM-b8IGGtRSs1V8wBU7J786y2RjmqGJxTWpzqSGNPEAEixuBR-Xs7C88luAYeCjdEo0mz6zsiZEHiFungcxDVCcOuIIpvqlnJx9rsyNz6ginl3PGDR-IkUw6bevADvmSHrxLCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
: ما یک محاصره برقرار کرده‌ایم و بسیار مؤثر بوده است. دلیلش این است که آن‌ها سعی کردند محاصره ایجاد کنند، و حالا ما آن‌ها را محاصره کرده‌ایم.
آن‌ها محاصره ایجاد کردند، بنابراین ما هم آن‌ها را محاصره کردیم. ما محاصره نهایی را داریم.
من این را جنگ نمی‌دانم، اما اگر کسی بخواهد آن را جنگ تعریف کند، خب شاید بتواند چنین تعریفی داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125793" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125792">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: توافق آتش‌بس با ایران به درخواست برخی افراد بسیار خوب حاصل شد
🔴
ایران ممکن است در طول آتش‌بس، قابلیت‌های نظامی خود را اندکی افزایش داده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125792" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125791">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdVkYeaXaiQoEnbyDwoB9YfSPlGSaUfw5GlYN4xCyJjHtQUyx2cE-a4Sb3meNo1VTLCY1k5_q41idO7MN7ratmIIDcz8hV_rwnX6oWtJrOpl3uRFaEH2VvI4uAjlAQqkguuUGasW_EDuYZbJwEr4hje2aU96ocJFUI7qHZhC0R6n-H5mEm4ZV4_-Lf-0UledCCaUqnaXcKlhG0MIcnlRPLNlSIWHCwh4dedA6ZdBVwY_gW4hGParC4Xg7PTuA4sL83zhzvgUf2Mi2eo5c8Qau_5G_JGbg0qdwY149vsEUVE_M7AuNMSIVIj7tIZDcVJe_Xo0ePzBGyMV_h_mhMYLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: بخشی از چالش در اجرای سریع صلح این است که مستلزم تغییر اساسی در نگرش دیرینه تهران نسبت به ماست.
🔴
ایرانی‌ها قوی هستند و به خودشان افتخار می‌کنند، و کارهایی هست که هرگز انتظار انجامشان را نداشتند، اما مجبور به انجامشان خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/125791" target="_blank">📅 17:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125790">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ، گفت که او الزامی برای اینکه لبنان بخشی از یک توافق کوتاه‌مدت با ایران باشد، ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125790" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125789">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
منابع لبنانی گزارش دادند تعداد کشته و زخمی شدگان حمله هوایی اسرائیل بالاست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125789" target="_blank">📅 17:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125788">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
دونالد ترامپ به NBC گفت: اگر با ایران به توافق برسیم و روابط دوستانه‌ای داشته باشیم، با همکاری یکدیگر اورانیوم با غنای بالا را جمع‌آوری و نابود خواهیم کرد. تجهیزات متعلق به ما خواهد بود و این مواد را یا در همان محل از بین می‌بریم یا به جای دیگری منتقل کرده و نابود می‌کنیم.
🔴
این کار را با ایران یا بدون ایران انجام خواهیم داد، اما در صورت توافق کسی به سمت ما شلیک نخواهد کرد.
🔴
اما اگر توافقی حاصل نشود، با اقدام نظامی بسیار سخت با آن‌ها برخورد خواهیم کرد. در آن صورت ابتدا آن کار را انجام می‌دهیم و بعد وارد عمل می‌شویم تا از هر جهت امنیت داشته باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125788" target="_blank">📅 17:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125787">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
ترامپ : ما خیلی نزدیکیم، فقط چندتا چیز کوچیک مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125787" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125786">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ : مجتبی خامنه‌ای به شدت زخمی شده اما بسیار شجاعه
🔴
چون که خیلیا اگه جاش بودن عمرا تو این وضعیت به فکر اینکه با آمریکا چه مذاکره و توافقی داشته باشن اصلا فکر نمیکردن ولی اون براش مهمه پس شجاعه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125786" target="_blank">📅 17:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125785">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=XV2v8MtkHVAm8efXWbsRiaQcfvERj3mZlLrmP4W6xAV9ZU7f_j1NdzIQDqoW6CjLe3V0sTe4aXbl2I1oQgR0-ABWSdd0mUtEutHGdWlaOBvy8wrCmAOg-AriAsLthOK1A81_HNjwUviO_Ck-n9pSeywFpaev-o9nch9Nv4lz1TrzWURBjSYz2eNk4SrxA7_W27g1If-QfpwBwNwoF1IUtPT_3rrgdEW_iq79-XQdeF_b7PnrPeBt9WUDY6UMu2g2CBadSVCI97uX5afPYqO6xqBJMvzstbjfY2ScJKpmmoJXVoCMxKtmUMmNnbNW2Em6gM0CTTEuLWv6amNuMGYgeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c568dbc38.mp4?token=XV2v8MtkHVAm8efXWbsRiaQcfvERj3mZlLrmP4W6xAV9ZU7f_j1NdzIQDqoW6CjLe3V0sTe4aXbl2I1oQgR0-ABWSdd0mUtEutHGdWlaOBvy8wrCmAOg-AriAsLthOK1A81_HNjwUviO_Ck-n9pSeywFpaev-o9nch9Nv4lz1TrzWURBjSYz2eNk4SrxA7_W27g1If-QfpwBwNwoF1IUtPT_3rrgdEW_iq79-XQdeF_b7PnrPeBt9WUDY6UMu2g2CBadSVCI97uX5afPYqO6xqBJMvzstbjfY2ScJKpmmoJXVoCMxKtmUMmNnbNW2Em6gM0CTTEuLWv6amNuMGYgeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما یک محاصره داریم. این بسیار مؤثر بوده است. و دلیل اینکه ما این محاصره را داریم این است که آنها تلاش کردند محاصره کنند، و حالا ما آنها را محاصره کرده‌ایم.
🔴
آنها محاصره‌ای ایجاد کردند، پس ما آنها را محاصره کردیم. ما محاصره نهایی را داریم.
🔴
من این را جنگ نمی‌دانم، اما اگر بخواهید آن را اینگونه تعریف کنید، فکر می‌کنم می‌توانید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/125785" target="_blank">📅 17:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125784">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: بخشی از چالش در اجرای سریع صلح این است که مستلزم تغییر اساسی در نگرش دیرینه تهران نسبت به ماست.
🔴
ایرانی‌ها قوی هستند و به خودشان افتخار می‌کنند، و کارهایی هست که هرگز انتظار انجامشان را نداشتند، اما مجبور به انجامشان خواهند شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125784" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125783">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e549e15d94.mp4?token=R5MIFA0gbRTr61ajBTJlL-tX0aJN5CIpg6V-SBo8OlJo8BE4mEXbcQIwNl1_7mk6reWbHLskB4DRQ1W8GbXeNXsNnbwTD1Sikm1csEawl2kAImcSv3jXRQZp9bJUyvF-SvwB8sMS2td0ld8J6uMpgzs0KjeYA0BhvhpoZGn7RbKO7jV84xX3ZOgnj3a6yOnAoiXG4zmd5ecNiBkQL89yhwrfKF1ne-H_Sm0nYOZVCtT3fyFJpT_G7tf2ABUNnp17DK69PNVH69xvE1wQElrBPemR8gcrwqo_nV9pR5FuiB-286BTcGRwzA0tqVENQ3-RxCmSWaEMmlSHnX2R2TpA1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e549e15d94.mp4?token=R5MIFA0gbRTr61ajBTJlL-tX0aJN5CIpg6V-SBo8OlJo8BE4mEXbcQIwNl1_7mk6reWbHLskB4DRQ1W8GbXeNXsNnbwTD1Sikm1csEawl2kAImcSv3jXRQZp9bJUyvF-SvwB8sMS2td0ld8J6uMpgzs0KjeYA0BhvhpoZGn7RbKO7jV84xX3ZOgnj3a6yOnAoiXG4zmd5ecNiBkQL89yhwrfKF1ne-H_Sm0nYOZVCtT3fyFJpT_G7tf2ABUNnp17DK69PNVH69xvE1wQElrBPemR8gcrwqo_nV9pR5FuiB-286BTcGRwzA0tqVENQ3-RxCmSWaEMmlSHnX2R2TpA1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ می‌گوید جنگ ایران یک «تمرین نظامی» است و اضافه می‌کند، «این برای ما جنگ بزرگی نیست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125783" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125782">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: نیروهای آمریکایی را تا رسیدن به توافق نهایی با ایران در منطقه نگه خواهیم داشت
🔴
آمریکایی ها با پایان جنگ احساس آرامش خواهند کرد
🔴
من قصد ندارم نیروهای آمریکایی را حتی در صورت آتش‌بس خارج کنم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125782" target="_blank">📅 16:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125781">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: نیروهای آمریکایی را تا رسیدن به توافق نهایی با ایران در منطقه نگه خواهیم داشت
🔴
آمریکایی ها با پایان جنگ احساس آرامش خواهند کرد
🔴
من قصد ندارم نیروهای آمریکایی را حتی در صورت آتش‌بس خارج کنم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125781" target="_blank">📅 16:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125780">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ، درباره مجتبی خامنه‌ای :
اگه اون بخواد، منم حاضر به صحبت مستقیم هستم، ولی تا حالا هیچ تماس مستقیمی باهاش نداشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125780" target="_blank">📅 16:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125779">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ در مصاحبه‌ای با برنامه «Meet the Press» شبکه NBC News :
🔴
«اگر به توافقی برسیم و از این به بعد روابط دوستانه‌ای داشته باشیم، همه با هم خواهیم رفت. تجهیزات متعلق به ما خواهد بود. [ذخایر اورانیوم] را خارج می‌کنیم و نابودش می‌کنیم؛ چه در همان محل باشد و چه آن را به محل دیگری منتقل کنیم.»
🔴
او افزود: «و ما یا همراه آن‌ها خواهیم رفت یا بدون آن‌ها. اما اجازه نمی‌دهیم کسی به سمت ما شلیک کند، درست است؟»
🔴
ترامپ مدعی شد: «اگر به توافق نرسیم، آن‌ها را با اقدام نظامی بسیار سخت و شدید از میان خواهیم برد. و در آن صورت، پیش از رفتن ما این کار انجام خواهد شد؛ بنابراین به هر شکلی امنیت خواهیم داشت.»
🔴
ترامپ همچنین ادعا کرد که ایالات متحده می‌تواند این فعالیت‌ها را زیر نظر داشته باشد، زیرا از ظریق «نیروی فضایی» آمریکا، «دوربین‌هایی در فضا» دارد.
🔴
او گفت: «می‌دانید، ما آنجا را زیر نظر داریم؛ کاملاً و از همه جهات. اگر کسی آنجا قدم بزند، حتی اگر خود شما آنجا راه بروید، من می‌توانم نام کوچک شما را روی نشان سینه‌تان بخوانم.»
🔴
ترامپ افزود: «و این‌ها دوربین‌ هایی هستند که در فضا قرار دارند. فناوری واقعاً شگفت‌انگیزی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125779" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125778">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjqB3oL4KAjGZwmmtLzBpmCivnybC2M1icJG3lIkL5freMbC2--fJ380BQVTg8JAuWjwRu2cziNZS2QFeOxmPN2uakbo4qhFLnLrDeALPrPLDtqHK_oayuy6o0ACy4xYFRmDHngPiDTN0BgvIF4WwG_MBaSbtmea4jwvzAhHOcSrd03cjsJYB_aS8yLBePU8d31hh9D8wxWFZzi6YoZz3pwJIWOEnhViMq0bLRVJZ9dLeQ3_LWfAUOARjRBMqfLulX82C9NBsVISMMLQ1lVv6Wy5lubvZwWyE53DD7ZpxcsspO-merE5qBnx_WYFrZCZ2bBlIVKfqTWzZEYRxkoW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: اگر با ایران به توافقی برای پایان جنگ برسیم، با آنها برای بازیابی و نابودی اورانیوم با درصد غنای بالا اقدام می‌کنیم.
🔴
اگر به توافق نرسیم، به تضعیف ارتش ایران ادامه خواهیم داد تا نیروهایمان بتوانند اورانیوم ایران را با امنیت خارج کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125778" target="_blank">📅 16:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125777">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDC1VPVrm1S12zKICz03E7L7KFGnvsAyIhUzWmK2ymGbQwTpiesid1EkZfijfrrc7W3KaPdMO3NiUgg9f8pmZqDa0ZyeDVfWR_-2OlYAnxY6wq10NhKcEMfonKZpoXgP9MSGDM2fMqcDM1bLRi7czy7OBYOUXwWiDXiOMLkn3eFelESqQiOz-uCZSyOCDNpIcK33sxjSMYQaKaldEWPFzQCAa76VGpLO72L0rSdLedqUVeoopaMUTCUdbSfD9eVPQKLlLYkOJ_-g9MW-pbTRWkRE8zjGUSdFv7ttUuQqqHE5NTpsnB5DpfHlPDCdm5aAMrOBCh2SDD0gfAHN6SezSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارشناس صداوسیما:  منتظر واکنش قرارگاه خاتم‌الانبیا و حزب‌الله باشید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125777" target="_blank">📅 16:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125776">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
جمهوری اسلامی سقوط خواهد کرد و ملت ایران پیروز خواهند شد.
🤔
حتی یک لحظه هم شک نکنید، از واقعیت نمیشه فرار کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125776" target="_blank">📅 16:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125775">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ، درباره مکان مجتبی خامنه‌ای :  نمی‌خوام بگم که میدونم اون کجاست یا نه، اما احتمال خوبی وجود داره که بدونم کجاست
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125775" target="_blank">📅 16:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125774">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ به ان‌بی‌سی: ما و ایران به امضای توافق بسیار نزدیک هستیم، اما من تهران را تحت فشار قرار می‌دهم تا از جاه‌طلبی‌های هسته‌ای خود دست بردارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125774" target="_blank">📅 16:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125773">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISabRe_dWdHsgW42nnOVVExvL3gCgW_9Ve9EZyg3Yarz9-zWpS7_rOv3eybmmWkXCZUMTODwu2NXqicql5ZQPSeu_e4eIV1JdYK1nmV-j4em1tbczwXR-UW8L9gBpKvmO5r-ZPLlfYwx4wln9FQ--n9pT7u2ScjVGKvE2ESaljaf4b3WODsJvIKm8JfNlaUIHzOrLlZyWbmjUIlx0j4TF8hhzAP_XMmecc2FrwLHVtCY3_Z38MDd3_vMMAz-NN34EpPZPfCTax52dn14lEwcYXOPbH5XPB0uRrJHqYp2L7W8MO7CDiTKJefdbJWno1fi-fN_VlpSR7Vt7j61T5JcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، درباره مکان
مجتبی خامنه‌ای
:  نمی‌خوام بگم که میدونم اون کجاست یا نه، اما احتمال خوبی وجود داره که بدونم کجاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125773" target="_blank">📅 16:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125772">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ به ان بی سی: هیچ پولی از ایران آزاد نخواهم کرد. تحریم ها هم کاهش پیدا نمی کند
🔴
اگر برای پایان جنگ به توافق برسیم، با ایران برای بازیابی و نابودی اورانیوم غنی‌شده با غنای بالا همکاری خواهیم کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125772" target="_blank">📅 16:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125771">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ به ان بی سی: هیچ پولی از ایران آزاد نخواهم کرد. تحریم ها هم کاهش پیدا نمی کند
🔴
اگر برای پایان جنگ به توافق برسیم، با ایران برای بازیابی و نابودی اورانیوم غنی‌شده با غنای بالا همکاری خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125771" target="_blank">📅 16:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125770">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / ترامپ به ان بی سی: نمی‌خواهم لبنان بخشی از تفاهم با ایران باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/125770" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125769">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
الحدث: ترامپ از قبل از حمله بیروت مطلع شده بود»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125769" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125768">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwh7qVF1SX94qbghPf2gkdHat9YuyJJ1yK7BhiC76pIdsT__pYFZGhvgHGj1Y0kmLOeXH3KGXgbBf_Xa6DCtSXfiHnnEXMVkdisngfY43CMWh14U_LXUSijkjvq3N7Q_actRC6bXB2Kx_B_w0im0txefFtmnCqBKi_YjroWxF5Miap3iTu1PQlzTg8rinD8mj2qt3xAworx1_nN_voWPulARFstOqKV1N5Ca077RKiocM-ZFp4iRaRZbQDDiEMhjlI3ITGmizFD7n_Sbqot36CH4HRjsnEBi2SHrwowJ9F5gliK_kgXe7CrIOdRqtncXiQzYnGo1X1DpqrNnKE_X5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیرحسین ثابتی: راهکار پایان جنگ مذاکره نیست، بلکه قوی‌تر کردن متحدانمان در غزه، لبنان عراق و یمن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125768" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125767">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
تخفیف ویژه NETSPIRA VPN فعال شد!  فقط برای 100 نفر اول
⚡️
قیمت هر گیگ فقط 11,000 تومان
🔸
5GB → 55,000
🔸
10GB → 110,000
🔸
25GB → 275,000
🔥
آفر محدود NETSPIRA VPN فقط برای 100 نفر اول  برای ثبت سفارش از طریق بات اقدام کنید
🤖
@NetSpira1bot @NetSpira1bot</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/alonews/125767" target="_blank">📅 16:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125766">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vi2hoEqq4FdTP7rMDh0JrhCB0ecJlI8M1vKh-kFQ7ceIThXKZ_2k0N-0-rOYnGnxr04nvWkiwdQ1Fol4pZU0OwYOiN-1nWiCdW01lyh9pSIACOScBGg_a8pfRwH7PjG4O0aVFHdDuNEuBE_9OzGp2LBCcXwARyaj5KxvuDPOeRyXp1tWYdvADRuIigvDn84zHYu83E_NdC9gcVmoTsLfv0e2CjqG_OZ3cJKjNyv0bAwE7k9hAFAYqW94STjsRTV74ZOvbIJQxOKwGLEDGFtmppSmYPf10wKXOPyzAOZR2W958RAdrts-gu1BT67fp_7phn-OLzDTxR9-65AaBpN0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تخفیف ویژه NETSPIRA VPN فعال شد!
فقط برای 100 نفر اول
⚡️
قیمت هر گیگ فقط 11,000 تومان
🔸
5GB → 55,000
🔸
10GB → 110,000
🔸
25GB → 275,000
🔥
آفر محدود NETSPIRA VPN
فقط برای 100 نفر اول
برای ثبت سفارش از طریق بات اقدام کنید
🤖
@NetSpira1bot
@NetSpira1bot</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/alonews/125766" target="_blank">📅 16:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125765">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
یدیعوت احارونت: اتاق عملیاتی که ارتش اسرائیل در الضاحیه هدف قرار داد، خالی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125765" target="_blank">📅 16:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125764">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رسانه‌های عبری: حمله به ضاحیه با ده موشک و با استفاده از دو جنگنده صورت گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125764" target="_blank">📅 16:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125763">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری / خبرنگار الجزیره: یک موشک زمین به هوا به سمت جت‌های جنگنده اسرائیلی در آسمان منطقه نبطیه در جنوب لبنان شلیک شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125763" target="_blank">📅 16:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125762">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
منابع لبنانی گزارش دادند تعداد کشته و زخمی شدگان حمله هوایی اسرائیل بالاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125762" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125761">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
در لبنان گزارش می‌شود که شهروندان اکنون در حال تخلیه بیروت هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125761" target="_blank">📅 16:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125760">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل به نقل از یک منبع نظامی: پس از راهنمایی‌های اطلاعاتی، نیروی هوایی به یک هدف با ارزش بالا در حومه جنوبی حمله کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125760" target="_blank">📅 16:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125759">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
کانال ۱۲ سرائیل : اسرائیل قبل از حملِه به بیروت، به آمریکا گفته بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125759" target="_blank">📅 16:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125758">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
محل مورد هدف قرار گرفته در حومه جنوبی شهر است.
🔴
گویا ترور هدفمندی صورت گرفته
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125758" target="_blank">📅 16:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125757">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
رسانه‌های اسرائیلی : یه حمله محدود تو ضاحیه انجام شده و ارتش اسرائیل هم فکر می‌کنه ایران مستقیم به اسرائیل جواب نمیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125757" target="_blank">📅 16:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125756">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1015bb3474.mp4?token=r6UG8fgjs_3NeHFeUtldHvGEbF-7STAZG_L5om05cgAq7SFcjOjr5VH9N8-PE_dXkjFzR8XpFtNwZkTfHgB5e0MT852LuuzceA41caQF2GP-taZOi_YjgY0bdS0CoIImmahMK45duv8yf-QNQNzxhgteI6r-4jY4Nm1k-90QzryaNG5FeIH5FwH6Ya847cpsD6Y8vVinhbqJkxUorudURCyU7_Rm_ZJX20BdGmPsYCYC3SZKmU_rAwjDGAKBrDBLxy89xl4HO0_yYdiwvSysfg73ZKqC0Z5WVaYtanknGbHPtZcF2m4zRCc0k8h134xAM6eE90CHskxnUw4VO1R35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1015bb3474.mp4?token=r6UG8fgjs_3NeHFeUtldHvGEbF-7STAZG_L5om05cgAq7SFcjOjr5VH9N8-PE_dXkjFzR8XpFtNwZkTfHgB5e0MT852LuuzceA41caQF2GP-taZOi_YjgY0bdS0CoIImmahMK45duv8yf-QNQNzxhgteI6r-4jY4Nm1k-90QzryaNG5FeIH5FwH6Ya847cpsD6Y8vVinhbqJkxUorudURCyU7_Rm_ZJX20BdGmPsYCYC3SZKmU_rAwjDGAKBrDBLxy89xl4HO0_yYdiwvSysfg73ZKqC0Z5WVaYtanknGbHPtZcF2m4zRCc0k8h134xAM6eE90CHskxnUw4VO1R35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: ایران بعد از ۹ اسفند هیچ درخواستی برای مذاکره نداشته؛ همه اینها یک طرفه و از طرف آمریکا بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125756" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125755">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyKzyH2pZgkHPrqNmf0jZq3OWKc43R3W2vQPedbvYgZEmmbi37thsKb5nRrH6cNABYu9fqfowMCJeMwAXFZZPKMJz8byCyZgPaWZebqzznrqdl6Mep694q5qOLhhd_3e9ePr3Q4KWq6DubXhXrsNJoqK6TCgcwiiruSArRZiUaQkc1UWvZ702e_OTTr7VDvkRM1Rxz7zl27SXdX7J1a4p7Y6ufKOx-uO2IH80FHwz4Jg5HUiE1rZ5IASH_ib3yg7aeelyh49ouutp29usKoXH7Xv47genQuIf1-nWaVrULMoW0wdcUyzKDDNFMQnxYA1IKk9nIadNuXzQmhlgcHO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محل مورد هدف قرار گرفته در حومه جنوبی شهر است.
🔴
گویا ترور هدفمندی صورت گرفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125755" target="_blank">📅 15:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125754">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3XuO6QisNYtCd-j_0A45xRJ5umkHUNh75Gq9C9nLtA8pPaat3klb3bfYUxoEVC-cR0OuxB_UM36kALO9VU7DPKat1C0pyuWSXokSMg6P0qVVHSQ9mBFdwG3zJnzKHhgazRXGTxNwc_9M86iKKcq-OYaZphQEdc0t-D_CKkndpS5Dg-EFjzPE1YbBb0k4lDJ-Le-kHUuWlBJBFh5-Tjcd21fgy7abzjlDy5H5RFZl8caLCSE6U_2vprLGTYbAEoTdwpo5rxxMojP-IeALj9XtIHszKWrL5Vtepno-ilNFZw6x_SQ8XB4aBAjfk-18pnHvJdzarQCNlMBTpeJFQ56rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: پاکستان به دنبال جداسازی پرونده لبنان از توافق ایران و آمریکا
🔴
عبدالله خلوف، خبرنگار العربیه: پیام فرمانده ارتش پاکستان به رهبری ایران، تلاشی برای رسیدن به مرکز تصمیم‌گیری ایران است. اسلام‌آباد تلاش می‌کند «پرونده لبنان» را از توافق احتمالی میان واشنگتن و تهران جدا کند و آمادگی خود را برای کمک به ارتش لبنان در اعمال کنترل بر جنوب این کشور، پس از خروج عناصر حزب‌الله، اعلام کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125754" target="_blank">📅 15:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125753">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
عراقچی گفته بود اگه به ضاحیه حمله بشه، تهران با قدرت پاسخ می‌ده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125753" target="_blank">📅 15:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125752">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نخست وزیر و وزیر دفاع اسرائیل در بیانیه مشترک از انجام حملات هوایی به مراکز فرماندهی و زیرساخت حزب الله در ضاحیه در پاسخ به حملات راکتی امروز صبح حزب الله خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125752" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125749">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnp4BpexB5havb4Aqx7U1HMUs93PJvhgcVA6Smg7zEaVr6vQ8smgc5yZiVd65HWOS9-pLIWc-Vmhwn9ALUJDh1wUcugo8ISy4lp5eJrA1pLvCv7Wpl2dATS4IC5EGhgNcqAjOt1Ic56sg6DX2a8rd2XlLCp01sHxs37q6Z2lHkfQ-CBn9jjLCy6ukh-Vgkcdg0NrtydI8KgiExt7KiTilEmtYoFPlQpb_He2ei9-LCc9sKX5XfDzen0FgdFvmQMUvVPRf1m9KPL_PcTD-mbJyZgkfzDG8u6afu3Fwd8Lb9FOTrqvhku3w5Us0_LsCS5Y6-37NSt15m69buoRm936pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88104063b9.mp4?token=Z19UtgFuSmKCWTPV4wCnuUyr88CUsl6eb4jocoG2MDb0dPgq84ED8jPQC7yoWOwGsK3GUvj6R0A6gWfT90MIJJ1OBREy2lPsmmkzahjWxWMlV9s44WdAHcXZvN76pa6PkyJ9S7QQAMVhFt4IwxIVQIf7a7-hrsEmJNUFJPnwaQqSIR-mOnhvvPhuMrwdx9JiyU7MEEIs3FnEsPThX57wlxvNpaKaMhmxlmjD6MKLE3emVcp_17KjFaVGLBkGMHebdRrbEpUgySWIV5eluaKyBU4zN8tHAz2Xw16CHq-CKcKBgOgFTRlcBoq_yBWfhvljHpItuJDm49u5cJaHc_Wwkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88104063b9.mp4?token=Z19UtgFuSmKCWTPV4wCnuUyr88CUsl6eb4jocoG2MDb0dPgq84ED8jPQC7yoWOwGsK3GUvj6R0A6gWfT90MIJJ1OBREy2lPsmmkzahjWxWMlV9s44WdAHcXZvN76pa6PkyJ9S7QQAMVhFt4IwxIVQIf7a7-hrsEmJNUFJPnwaQqSIR-mOnhvvPhuMrwdx9JiyU7MEEIs3FnEsPThX57wlxvNpaKaMhmxlmjD6MKLE3emVcp_17KjFaVGLBkGMHebdRrbEpUgySWIV5eluaKyBU4zN8tHAz2Xw16CHq-CKcKBgOgFTRlcBoq_yBWfhvljHpItuJDm49u5cJaHc_Wwkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / حمله اسرائیل به ساختمانی در ضاحیه بیروت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125749" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125748">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سه زمین‌لرزه با فاصله تنها چند دقیقه‌ای از یک‌دیگر، امروز جزیره «اویا» (Evia) در یونان را لرزاند که قوی‌ترین آنها با بزرگی ۵.۲ ریشتر ثبت شده است. این زمین‌لرزه‌ها در مناطق مختلف از جمله ناحیه «آتیکا» و پایتخت یونان، آتن، نیز احساس شد.
🔴
به گزارش روزنامه «نشنال هرالد»، مقامات یونانی اعلام کردند تاکنون گزارشی از تلفات جانی یا مصدومیت ناشی از این زمین‌لرزه‌ها دریافت نشده است. با این حال، در برخی نقاط خسارات جزئی گزارش شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125748" target="_blank">📅 15:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125747">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فارس به نقل از یک منبع: بخشی از پرداخت‌ها برای عبور از تنگه هرمز، نقدی نیست و در قالب تتر، کالا یا تهاتر انجام می‌شود؛ یعنی برخی کشتی‌ها خدمات ارائه می‌کنند و ارزش آن از مبلغ قابل پرداخت کسر می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/125747" target="_blank">📅 15:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125746">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دبیر شورای صنفی نمایش: از نظر شورای صنفی نمایش پخش بازی‌های تیم ملی فوتبال ایران - که فعلاً در مرحله گروهی شامل سه بازی می‌شود - در سینماها با کسب مجوزهای لازم از ارگان‌های ذیرربط بلامانع است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125746" target="_blank">📅 15:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125745">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نتانیاهو: ما اجازه نخواهیم داد حماس دوباره مسلح شود یا به ما آسیب برساند، و ما به حذف رهبران برجسته آنها ادامه خواهیم داد.
🔴
ما حلقه محاصره را به دور حماس در غزه تنگ‌تر می‌کنیم و در حال حاضر ۵۰ درصد از مساحت نوار غزه را در کنترل داریم و به زودی به ۷۰ درصد خواهیم رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125745" target="_blank">📅 15:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125744">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFmLm0wQnePUD57A364KGV2xYiA6sL13Sce5Wy7RY43nNEzmPeO9tSjenau84yVEHLLrFP4Pojq3L5gB1QZaGVP9UX0enIOssIG-tr7DgKcDtrGCgmbLY9yoFYj99c-O-QiTANpAqXmCrCZXL5gH1Mm3unu-7HJL6-uqYtJeyRE5SlDO_Ljg7rO6tcoti0zlQLaIDP6nz7Jvw9iM9jvCEB04CLrM6ZvGz0OKW5sCeXJGd1F6bz_u1i3meKLwXMTm-9aTiduDFIhu9-p2SaGA-dAyxQan7jID3kH41qbPuE_4cMllt_43nqlegKgemHybDx1fuoZAS9X0v5cqYE11Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشیدی کوچی: خطر فرقه پایداری به‌مراتب جدی‌تر از تهدیدات خارجی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/125744" target="_blank">📅 15:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125743">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f40787a7c.mp4?token=efZ99UwQuR2_5bjrMQadfuP60riyzdPP4zvpGCzqH-EDVPahJlrbno_-Jzi6IUne7ixUuDt4lNxI-0SbrswQNPSJDEzPQCvWudPkq8HmcsEe-HtPbpiw_BwyjkpWE7oGdBOZK1ZfGKv30rMdl0zuqSPflvSO70yQG0QhPa9lAHk0lQMOZo7qoBmLmqazybQkOy9s_qihOXDcfCvrr7Bv1x9eWkU9NrgSqudHmlLNZQe2hcjD6RraVqsxhHs6Zk0vOW8Ar469mkz1uxH-aH6qAzXJBhAnKOvU_OgkZm0rYnAiCq_NkisdMziPUxwqKHpjIO-DtSLHJnZLLPw04t-3_ZibVGV5rQkaTxZ1_OfK-0g_8nqLjDYwGCpsWXLlndtxUNxRtNjPF0Dy6H0oxIgktERjdv6Rr1n5W6iofnmIAuOV-ri1bDtw8F6eo7hYjk-S8_NF6KzxLYd3gYfbT6obE3yAk6BXsaLhaso8eIrtxPkoPQRvH6wM8IHXRrRR2xkFMevg9u11cSpHtPZovU2N4Rs56OmeyIqea-jnEokCl0Y3GzxLiwrXM9eGxX4YuTftJR2xaHsasYeUKmkk0166RnayKrmojTnIINkasSZ9VupYrmdJ52thf3ZBTCFWMt_fY-XCwSQ-66qCHAR8fGElCbxYU1xMzglfEhxqmgkzxN8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f40787a7c.mp4?token=efZ99UwQuR2_5bjrMQadfuP60riyzdPP4zvpGCzqH-EDVPahJlrbno_-Jzi6IUne7ixUuDt4lNxI-0SbrswQNPSJDEzPQCvWudPkq8HmcsEe-HtPbpiw_BwyjkpWE7oGdBOZK1ZfGKv30rMdl0zuqSPflvSO70yQG0QhPa9lAHk0lQMOZo7qoBmLmqazybQkOy9s_qihOXDcfCvrr7Bv1x9eWkU9NrgSqudHmlLNZQe2hcjD6RraVqsxhHs6Zk0vOW8Ar469mkz1uxH-aH6qAzXJBhAnKOvU_OgkZm0rYnAiCq_NkisdMziPUxwqKHpjIO-DtSLHJnZLLPw04t-3_ZibVGV5rQkaTxZ1_OfK-0g_8nqLjDYwGCpsWXLlndtxUNxRtNjPF0Dy6H0oxIgktERjdv6Rr1n5W6iofnmIAuOV-ri1bDtw8F6eo7hYjk-S8_NF6KzxLYd3gYfbT6obE3yAk6BXsaLhaso8eIrtxPkoPQRvH6wM8IHXRrRR2xkFMevg9u11cSpHtPZovU2N4Rs56OmeyIqea-jnEokCl0Y3GzxLiwrXM9eGxX4YuTftJR2xaHsasYeUKmkk0166RnayKrmojTnIINkasSZ9VupYrmdJ52thf3ZBTCFWMt_fY-XCwSQ-66qCHAR8fGElCbxYU1xMzglfEhxqmgkzxN8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب‌الله پهپادهای انتحاری رو به سمت نیروها و خودروهای اسرائیلی تو جنوب لبنان شلیک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125743" target="_blank">📅 15:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125742">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
خبرگزاری رویترز نوشت: اعضای اوپک پلاس در نشست امروز (یکشنبه) خود احتمالاً برای چهارمین بار در چند ماه، بر افزایش سهمیه تولید نفت توافق می‌کنند.
🔴
این بحران با خروج امارات از این سازمان صادرکننده نفت پس از ۶۰ سال عضویت در این ائتلاف نفتی، عمیق‌تر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125742" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125741">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTa1NKDtxxBHCdZ_-5SSt4l8qWFg0DZFd-ukXf12yppKea9q-wiG-UqJs94zg62V507rkrv77cGaEmko5F8NqxLp-BfHLBnqXQLKh1XUzDo7iSDtOAkCFmKvvNtLGZKD8j3u6Zauuiq2-WQEaLBTXOWUKcIees5Y1p74CHRZy5lou9YSG1xOT0Hol4Ww6HrNq7Zz4Qu8z25hDg5_8zyKojJWftc88wCuN6xPcE6n7jda3B0U0WpWVgr9dcrnBCGAFNbGrSA4m-jAQCfiQpfJQ_A0tC51gm9b5b-XPOEjPmzpwxqSLi6BpSaId2HYQasj_KjvuGlDUWlMlt-v0k-dvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، با گذشت ۱۰۰ روز از آغاز جنگ توسط واشنگتن و اسرائیل، به نظر می‌رسد تلاش‌های ایران و آمریکا برای دستیابی به یک توافق موقت جهت پایان دادن به درگیری‌ها با پیشرفت ناچیزی همراه بوده است. همزمان، وقوع حملات جدید، فشار مضاعفی را بر آتش‌بس شکننده فعلی وارد کرده و دستیابی به صلح را دور از دسترس نشان می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125741" target="_blank">📅 15:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125740">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
بقائی: وضعیت آتش‌بس فعلی بسیار شکننده و خطرناک است
🔴
موضوع اصلی اختلافات ما، نپذیرفتن حقوق قانونی ایران از جمله «حق غنی‌سازی» توسط آمریکاست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125740" target="_blank">📅 14:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125739">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzEdP90RtRu9BV_kwObZA4VrzpSAmCBCc5n8wfVc-mxTU9HTn1FD3kKGOD-4ijseckuEtgA0Qhd-gGF46Dj9bWM2yGnUnwe6T7Injm0FAnZ7YLWvrpGNX6DyFwfc89mr773IuCkxh8vY5l4UWO_e_0xd2KXjC0tN2clBt1zicUI_gf1S1PswazJaNbEpSGJ5a7LPL8WsgYfs837RBw66buBQNdLIW43OfhSLNi9Hr-w4erZ6lIvS3VxqImucxn82tSH4iKeIFnhiXB4WL6mG_1pf40Bv1zJlr16PQvPzrxZJAqBW2HftCTfNhk8pi3zRqp9aCBRa6wxInorI0y51lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایمان صفا،بازیگر تلوزیون در صفحه اینستاگرام خود با هشتگ پخمگان نوشت:
جناب معاون گفتن در این جنگ‌های اخیر شاهد مهاجرت معکوس نخبگان بودیم. قیصر و صدف و یه سری بلاگرای دوزاری؟ اینا نخبه‌ان؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125739" target="_blank">📅 14:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125738">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3TJkRC6IebvPCxXy1iZ7D1VcJYg5j2E0qBjiVlfAJ4FiM3fYPdK04cqFQYOg3k-ywX-3SYH9U0yCcJBuSPp6jDb8mrsONCZfpeZhSO3tEIXozgMsd0IdxDbWfr6_oQYkot7jpJZCy2cXvvLJIKe_xe5Anqmbq5mtJOQKrkky78knKKWVngvwx1sn2gEVgwp3hUs3NC719ICO2UGJqov1RxSRXoB1UpsMxxlkADjJrVguNC-rb45XYV73HWXzq_t8lLjClDJCih6QIxEa2EmxC_g-rHxfzSZh4bFs8td4njCfy8M7R6Awb3yyyIfiaF5A3-b0a3RgSU_0pH9p3nLwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125738" target="_blank">📅 14:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125737">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان دستور داد که مبلغ کالابرگ افزایش پیدا کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125737" target="_blank">📅 14:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125736">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل : مردمِ شهر صور تو لبنان هرچی زودتر جمع کنن برن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125736" target="_blank">📅 14:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ULDeH6-J-fQhBnek07gRvaCDZDyeVuF-ryYT9uZ9BgL3YxUyFZ_g6PaJ0ZBZT_BPHIaNO23bcQReknE19WUKINqGSIfhilp7tUnDhZFGFI1ZaiLVMdOxZ-SLTSYU2YtY9xoNzKZ-BGIRZbgrg31Oa36XM_QJrK-cv39Mx9nV21dbO0uResxluW35gntONyW3TpChxFQseiDfr9ibGWX7byIUtJRaZiexvSRfmwp-98IzRtLkGG08Oo627QfIIQRzQfq9ysMzdpn77c5JwQ-PX9oThgxVtob1eR2mgFsznNSVQ1JDfstaNz1tzsTqRy5xbUbUgJQOOu_pAbjXGnBXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GVJeAbYagX2ZvxfZeTc-UYsjBaR3-rUz5rS533XmcFXfa63aW0NiClmCd46CnDaW1D8NNnef_ZgDVghaAQPE5OYhtSlDLDJbAylB1VB9aUQnpmA7AvpdLeT92e_AbEC56jEujBLMJ0C3WCgV2b87XdBUftFqbdvg1vqTmV5aMzNPLuj_FcJrz1PyOmRiRlX6v4d3Mv7VB9_cSFrIgxCoWMbTRSCItOyP8GVf7pz4kuOBJbFCIX1DQxbwsIb_qtTlWDy7xglUDnMcBYWQjWeFs53lMELWXA1tUUOUHpm-Vbach7kUUY8avLdjIW94oHtUkVYyRcBshnc628e4hbnxMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک فلسطینی با مسلسل کارلو به شهرک نشینان اسرائیلی حمله کرد که دستگیر شد
🔴
در جریان این حمله تاکنون یک اسرائیلی کشته و 6 تن زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125734" target="_blank">📅 14:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عضو کمیسیون آموزش: اعتراض به مصوبه کنکور فایده‌ای نداره؛ دانش‌آموزا برن درسشونو بخونن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125733" target="_blank">📅 14:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku195pOJqZ4fb9VG4HE3KHhk7IV66iThaEwUAkol1uOg8ZlYewrVVR1R7Tiz0lpX1dIPSaEIdicBBJ6KJo45087VCA58N7GQEuoWeqDbuG6B-i8Tkut_9H8ytzWh4IP0lphExQXCHrBXpAyU4zome_VUF20CMMahm_vbBZyAL39kZ_CIWVmjIzemdkmyU_0i1YPQiXlLCoFSzmVMTC09pMHLFpmLh_eyO0yhW3okk6gNmB2iXfLqca-hEsaETPtc4eeK_GgkdX5nhH6fL0XSu9_JARm2w6v7SJREOX7EZVQ2x51-mJQGFHPMLPAqiYqteFEG2Vw_lK84bBVj5Mty3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روند نزولی واردات نفت چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125732" target="_blank">📅 14:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه در گفتگو با سی‌ان‌ان: مشکل اصلی مذاکره با این آمریکا این است که شما باید با مواضع متغیر زیادی روبه‌رو شوید؛ تغییر مداوم خط قرمزها، اظهارات متفاوت و متناقض مقامات مختلف
🔴
وقتی آنها در مورد دارایی های مسدود شده ما صحبت می‌کنند، هیچ امتیازی اعطا نمی‌کنند
🔴
تعداد قابل توجهی از مسائل اختلافی وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125731" target="_blank">📅 14:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125730">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / ۲ زلزله پیاپی به قدرت ۲.۶ و ۲.۹ ریشتر  با عمق ۹ و ۷ کیلومتر پردیس را دقایقی پیش لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125730" target="_blank">📅 14:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125729">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpFBfpzwZJslH8tqZPcdd6L5AkK6lfQPq2-qRHEPk0WeZaCYeiD47baju1pSiSJvaMdBsecGF3QysJVYo5gGXf5a9fdMYQOH685V3NeGOjou46SZBm_EAIj9NuBXjR9FaRe6vMSVJpsFd1KPw0LZORqfdFU884_2_iWE_g2pFUocel3Lbr_mAt-tItlz-sm9F9dP0M3AVbVp1VNSYk8KynLLKfnVDZU-Iu1REbclRFOUJE2Bx13mzGbgnJ_dSSdMTkkwl-DASXq2jWCAHFqhzTA6qOT-xEGOcM1bfS59O9PiDRMUrVlbhdQSwgejZnEiFk6blPZI5vr3lldekokq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بانک مرکزی چین در ماه می بیش از ۱۰ تن طلا خریده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125729" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125728">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عضو کمیسیون برنامه و بودجه مجلس :
از کشتی های عبوری از تنگه هرمز ۱۰۵ تا ۲ میلیون دلار عوارض می گیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125728" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125727">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
عضو هیئت‌رئیسۀ مجلس: وزارت نفت صراحتاً اعلام کرده که قصد افزایش قیمت بنزین را ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125727" target="_blank">📅 13:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125726">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل: حمله در مرکز اسرائیل هشداری خونین درباره ضرورت ایجاد تغییری عمیق در میان عرب‌های اسرائیل است
🔴
اسموتریچ: گسترش جرم و افزایش افراط‌گرایی قومی در میان عرب‌ها در اسرائیل، خطری وجودی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125726" target="_blank">📅 13:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125725">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK2OvznSIqSM782t4jIopyErmKm5D_z6gKDRrL71DVrSfNaoNbxUXbo7Ibfr71MbCYq1HjjZURREhVfMOXGgHU3FhRB9mtTI4pkJYTVYzqyrnQkWo8LI2jwfRue5SiSmxa-zTmpcQO7ghN85S9yIlmR2sLWzGdX09vKQfhlQ_37zuIndhdAlDOO2Zziygjmy3TlT1LYuZYod3b1QReuaqMZuMIaxnzfqhDkbQ2Jn7zvp4UmhkeoT3ZIKnyW9FGwJG2CDhKQeqj9wctLMA8KyWAhgSQxmRscLd7bDSfZAM1ONBFis8S1fq9qE_r6bxOUDLORdTG-JuW4UhGw8ik08iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طرح«بانک زمان» توی منطقه ۴ تهران اجرایی شده و بزودی به بقیه شهرا هم میرسه. حالا چی هست؟
🔴
توی این طرح مردم به ازای پول، با زمانشون بهم دیگه خدمات میدن!
🔴
مثلا شما یه ساعت به یه نفر، زبان آموزش میدین و به جای اینکه ازش پول بگیرین، اعتبار دریافت میکنین.
🔴
با اون اعتبار مثلا میتونین ۱ ساعت ماساژ بگیرین، یا ۱ ساعت استخر برین و یا خدمات های دیگه...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125725" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125724">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت امور خارجه ایران: عراقچی و وزیر کشور پاکستان در مورد تحولات مسیر دیپلماتیک برای پایان دادن به جنگ تبادل نظر کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/125724" target="_blank">📅 13:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125723">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه ایران به سی‌ان‌ان: مشکل اصلی ایران در مذاکراتش با واشنگتن، مواضع متناقض آن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125723" target="_blank">📅 13:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125722">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری /  یک‌ مقام‌ ایرانی تایید کرد که در صورت استفاده از دارایی‌های ایران برای تعمیرات مناطق جنگ زده کشورهای خلیج فارس دوباره به آن زیر ساخت‌ها با شدت بیشتری حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125722" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125721">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دستگاه‌های اجرایی موظف به استفاده از پیام‌رسان‌های داخلی شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125721" target="_blank">📅 13:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125720">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoAcHURoOZWAGk74OaMuuz929I-I-IT6tubRd6imSLCKyjTaLNRdYv56WmFUuXUhzc-YHzhMrqWdUBzj8DyKPkowR6Y4Qeepbmgs-rXV5tk8eLtQkPKsZZudL_Zg3EHBdZQ1VwjYvj0YHMZChYRBNYkT5ID2dmAA85TDxcLMYZLzvsdP5XzLtYeyjs_RtDN4HyFwIfdboU9lFkiV9z3O-TgMT19Z_5rCCyfnH1w0aaRs7tPbY5CCaObJ9SF34kIQUQQYqwJlkXBjNEbfXgUZVop1GYN-2PP5L87OvtJr6uEdTqGbtR2j7CeFG522SPOSvX-meg5cNBXkz3H9s06YoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین 200 بوئینگ می خرد
🔴
مدیرعامل بوئینگ : این سفارش تنها «مرحله نخست» یک توافق بزرگ‌تر است و انتظار می‌رود در آینده سفارش‌های بیشتری از سوی چین ثبت شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125720" target="_blank">📅 13:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125719">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGxjASmqR0mS9rCzNFXKhtovfHD9UNuxj95cnnDfPe8qJ-6e98uIxrcKvdDnibZYsCmH0nMWvb6nNFajJcigOI4tgAB50DbvB2orvxCw80BLzSmmR-KSR6vUyFu_APd6KwenZi3tuXTL-jT1kEd2ujawMXSpAGOwCUbR6ff0eVUrSZxXuDd3pRgsLrZJy2CAoOwDmsR-Tpt_6SiYBUO4WPDU0dUtB7iXDhVvCPgVfxbLTDux11Oh-NcnOdU4v8LmEvONeR17Gf6gXYBYORUHvpKEM43OMrpF2yhagl-FIEZAwPMGDDxKy-LISpfqZyMUx2IoqmAgkLdK0DF--DFKlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125719" target="_blank">📅 13:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125718">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
معاون وزیر نیرو: در دوران جنگ اخیر بیش از ۷۰۰۰مگاوات نیروگاه ما دچار آسیب جدی شدند؛ البته همه آسیب‌ها و کمبود‌ها با صرفه‌جویی مردم حل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125718" target="_blank">📅 13:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125717">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وکیل: توبه «تتلو» از سوی دادگاه پذیرفته و برای طی مراحل نهایی پرونده به رییس قوه‌ قضائیه ارسال شد، ولی هنوز تصمیم نهایی اتخاذ نشده
🔴
اینکه موکلم برای ماه محرم درخواست مرخصی کرده تا بیرون از زندان مداحی کند، حقیقت ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125717" target="_blank">📅 13:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125716">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad0a1c177.mp4?token=emcTh-dmlW6e594gJzGFrxBsY45FkHGtjU1AvsGeJBfjF8L1f_Z2z_RAPclqIlneS9oGALt2oUY207WlJIRwwyfH3eCHPp1a7rZRjOb46THbdGZu6ljvB4VaHT0nNwfpIVuzN6ZrHUqz5W6NtI_JV6J-oPeZy4HPtYIeGcwZgOQ1aB-sdpnIek-o333paxIuMR5vjR-YD3TXTitF-g4rlhbYiwCUmW4EtXfjUBzBH5wdXSY3c1D9w47JWll4mePhiFBf7ZcVQGVy8-hJM74x90guM-UCz_3edxcUAbeECi_AGCOP6T0L3VIJlA7eZsyhSxyneZV22f6NVXj_lQj4Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad0a1c177.mp4?token=emcTh-dmlW6e594gJzGFrxBsY45FkHGtjU1AvsGeJBfjF8L1f_Z2z_RAPclqIlneS9oGALt2oUY207WlJIRwwyfH3eCHPp1a7rZRjOb46THbdGZu6ljvB4VaHT0nNwfpIVuzN6ZrHUqz5W6NtI_JV6J-oPeZy4HPtYIeGcwZgOQ1aB-sdpnIek-o333paxIuMR5vjR-YD3TXTitF-g4rlhbYiwCUmW4EtXfjUBzBH5wdXSY3c1D9w47JWll4mePhiFBf7ZcVQGVy8-hJM74x90guM-UCz_3edxcUAbeECi_AGCOP6T0L3VIJlA7eZsyhSxyneZV22f6NVXj_lQj4Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صف طولانی کشتی‌ها در هرمز از لنز دوربین یک گردشگر در عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125716" target="_blank">📅 12:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125715">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv8SArXlrWPEv7Fj7rIschOU1lUyS3jGPdCoXNe1vV9NamSI4EZe5eWIuCYpUbd4Q2fHU9iATge8k2MELsIdSG67NXlieCa2dh9EXUYYV9aFBa_h1TbYMfSSbiTXv8Cz2upP2i1F-jUVTUIbFbgPn0T-YPoZcASH4b-mBTcZjHpj0u9OGVtGhpx9gUurCiVjJWtTWmuv0y6F20-nkc8Z3JtJXEC5k3DjuxK2gdwYo_Pqt4-x4br8x4mB54yKp6jH55J8k4p7PWCeBcd3BBY7hGpnKgWD21ZzNRBPtRUy11m0-NStnMy_cjYcKK_xbSm6vC2cfRO4d5Vx2LXl_qwwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از زمان جنگ ایران خرید غلات و دانه‌های روغنی کشورهای خاورمیانه نصف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125715" target="_blank">📅 12:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125714">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH24ZkG_fZcHl0KDlCOJlg20UFlCLcTogjPjpoMZkLqWNr2gMJSilwgxA4exz2K1qSWcxpKCP9b1jnwDXZZisabeaeF25tRF_7Ga8c3aKkHxsRau8w3iHnp56H4IH-PP9obAp93F2RPeBhIw9l4SC4Jgwra9MdXl8vD7DrcGYCNzMseJU7_8cK2Vwnt-yN2jG76yhU4ryoXhNJ0oN9OVAl69M5HE3Blw3TmszYc1goe77Yim2RfMyAeR84i_3N7c2q-_VmMiw02CbPkYzMOJTIWq4oMC1e7qkJZsn_6UZYNxAmncrAxvGBlQpQYhwmvXm4EPm2qwtCSn9t9nTCeyBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انبارهای موشکی کره شمالی
🔴
دولت کره شمالی برنامه ای برای چند برابر کردن ظرفیت تولید موشک های بالستیک برای سال جاری میلادی در دست اجرا دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125714" target="_blank">📅 12:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125713">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزارت دفاع روسیه : تو ۲۴ ساعت گذشته ۵۰۰ پهپاد اوکراین رو منهدم کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125713" target="_blank">📅 12:46 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
