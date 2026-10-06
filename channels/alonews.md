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
<img src="https://cdn4.telesco.pe/file/uuaO_30NAUJFOZne5QEs6BFqWzcpVW1cDLkuBzsJ7iKzdEsDSeTpvyVvolx1fevRsMWz-rDvUz5Fbnj7anr_OTt7_CUx3lADW6w34HDrdEmjiPFo58uKp9UyAYFbcIP23whoSQlYezdEwxW35pjI5t1naZKG7ltae7-w2h_8ShvYkhmhRe35V7QhD8yn6AfwO0hQ8xEt3ZMaa341qh2L4D5L6Vjq7WQo-I30LoQxCjL0kKqKp3sDDdw7cJhDAwSSX_s_hgXTGmZR0YgjDta6xbCSwRBTfBZbrTMo2v2mdSisN1B8n9Q-p0qQjLOTvNrYgV0Dbd64PxWE1aFiWs7wgg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-15 02:39:50</div>
<hr>

<div class="tg-post" id="msg-151371">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ونس: ایران باید برای پایان دادن به جنگ، توانایی‌های غنی‌سازی اورانیوم خود را کاهش دهد
🔴
مشخص نیست ایران چگونه تصمیمات خود را می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/alonews/151371" target="_blank">📅 02:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151370">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIncuUvQuBM3a01RBchnEplP-XdtoBmb7HtaQ1DdnttThRtb79orUZj1eaTwiDa44SSYTxCNYRkPCp5iDT1beaw8vzDn-BswP2T5U_5Rer4bNGpgtlkaKn-IRxN7-W2KwnwdMvkml-uV0mYPqb5E_M3oGe0g3jvsZCNQER1KvMHdSL3L57xyxjrOwZHKlXAnlgo1AKOWmNBUePzE9EyI6761p-tw2gnFzCGv0hrc3UaG-LkFayAdoMaqMoYhFFRZejlCN6DqekQfU-_1FoBSMyRo7sXLdwEszg8gao8lkhzzZHcUaoWdRykmbC6srwM7EXi3fitLwzU1-aKmCfJekA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری حامد بهداد در حمایت از مهشاد کشانی و جاویدنام علیرضا سپاهی
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/151370" target="_blank">📅 01:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151369">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
👈
ترامپ :
رژیم ایران باید مدت‌ها پیش نابود می‌شد، زیرا با گذشت زمان، مقابله با آن دشوارتر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/151369" target="_blank">📅 01:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151368">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گریه های مسی تو اتوبوس تیم ملی در راه ورزشگاه  @AloSport</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/151368" target="_blank">📅 01:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151367">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gedL_NjjqnYFZapQaUdDxg9CIIKhdFQNYnhRY0oHhkLrxjWcJXrW3b9B1hMscnwUQ5dRLmruKt1Jy6qrOACbawmp3ACyMPn3q9azNoZT-6yYxaJF7_JFumu56gynfmQNgt4A7OCZTieDgnW4fOJKU_q4wLp5ivjovJsjAuiM78HOOk7dJL28I0p_5_LrNyjKYjpkY9sHcYUn8imF6lij9EVlTmJlLz1hzIhkWVEebWP9RrIKby18JsoTMoq5fchnALthoz9tqA9O8OynOklnm1N-vpdZ2pYlYg0z_JpzHzr3I1GqdSQxhABCsGrnfxMUvBa_ZP8G7sffvkqwt6qB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی:
بر اساس اطلاعاتی که به دستم رسیده، ذوالنور، نماینده انقلابی قم تو مجلس، درحال حفاری غیرمجاز برای پیدا کردن آثار تاریخی و گنجه !
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/151367" target="_blank">📅 01:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151366">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAgHj_9_fWhDABZY87d2FPElNmFrLOqwh-i2btxXsryreDNhSwibLYPhukqs_Ik2nSK7bzlqazFu0Tm_RAag8y62Y0y8nrrWR7hH-ypEt6-8K3sEx1hZZrsr1uOReaxq9xEbp03E1QmR86a7KI7CZHsybBYkWMzcMJIT0HZvJFwm5dZWlospsDlQK7-FC7yHFH1bh1GFvS1SPLnjvG7JThIMx6KaSjmVMK6_O38c1hl6p0aGW_8OGVDmhsI7T3lla61biMVLjCVFvu9lu0KpJRT6Aa3MqSwxwh6hTMTV6d9kmrABSBawGN2wL_7Kwm71rRPlSWjczfZCtJAeX4RCQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
هر ۱گرم کوکائین در بازار ایران‌ معادل ۲.۵گرم طلا
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/151366" target="_blank">📅 01:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151365">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcQh7H-YrFVv3qnfH8_qpoiLWX2vp5BkT2lnz6nRkCW81VRCugRaksildZDS_Ls-VixN6Q268VB9jkPUoVcwtB2myRdaRzlyFxMpbt4N7ClRL7LzXZmILbY5gT82NlpsEK7TtptphCjkKVOZrZ_p7Ix48AhTcYE9GS-exw5LWE10F8r2mwfUgD8Q3qMPDDE2wNQjPaN8W76TnWuLYIXALauEo5pF9bWJQFp-xJupart_CGZU7m0ILVBZB8gmM_OZqyA4brbhI84Zv37hVgT-ErPgfjOlv0U-kDZgJoUkr79e58Qz67DgFpFtqxHkJjiADZz3yT7yKQjlbeV1Xhwjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی:
بزودی سیم‌کارت با قابلیت درآمد زایی عرضه میکنم
🔴
پ.ن: خدا بخیر کنه از دست این دزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/151365" target="_blank">📅 01:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151364">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=Mj8SAmxvm7ERNOg-qiIZPl9LIeBnsFOsxsWqd20Q4WWQBxtmqzFwcdAl2Pj2cCpAzHpeLdYDL_YSpErcgENSujxfLxqA99-xxoo5J_-plR0heNjUCZgN85zLDczXMIB1miwkGMaM8j2Ruxs8HpdZglVXmsl0t7MUjFRksi7FRqw_bSeeT9f8Jb6Nkdu1wWS3u46PCTy90qbL7Dc5IkzQDrgObiTlv499_Fm-3aX9iNN59LElHLNKPWNyFyld5Rz2IUVf_pgEyDdyhmdaUYQsCar-wd2rwynix0V__96bQyX9gEvBqLoR2_vEvmFR5nPif2M5dil57KMl0xE1CuijEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c65f0143c.mp4?token=Mj8SAmxvm7ERNOg-qiIZPl9LIeBnsFOsxsWqd20Q4WWQBxtmqzFwcdAl2Pj2cCpAzHpeLdYDL_YSpErcgENSujxfLxqA99-xxoo5J_-plR0heNjUCZgN85zLDczXMIB1miwkGMaM8j2Ruxs8HpdZglVXmsl0t7MUjFRksi7FRqw_bSeeT9f8Jb6Nkdu1wWS3u46PCTy90qbL7Dc5IkzQDrgObiTlv499_Fm-3aX9iNN59LElHLNKPWNyFyld5Rz2IUVf_pgEyDdyhmdaUYQsCar-wd2rwynix0V__96bQyX9gEvBqLoR2_vEvmFR5nPif2M5dil57KMl0xE1CuijEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: در مورد شیوع بیماری طاعون در روسیه، آیا با پوتین صحبت کرده‌اید؟
🔴
ترامپ: قرار است خیلی زود با او تلفنی صحبت کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/151364" target="_blank">📅 01:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151363">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
اسکات بسنت:
ایران وزیر نفت جدیدی انتخاب کرده، ولی الان این وزیر نفت، چی رو مدیریت میکنه؟ چون از ۲۵ اوت به این سمت اونا حتی یه بشکه نفت هم بارگیری نکردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/151363" target="_blank">📅 00:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151362">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM-B-DFTJIolrPDTJVY0vGvX5__U8-YkFRQgmTjXQyZGWRmGsfKKnB8ChQ3zou4t1ATA6O9QO2FPegMEo7BWyjcM84twBS-l9nfdA2hdNF5md_EqOb43HCmntiSaoPfQjAUlkIMGBH11uOUtG7RfyNlGMYhw34dP4Tt3sZpOFf1ciRP3-5RikvD1bgnQ5wn7Ox7qjoJa41D2Lmitf3_HxJlxxCI26vSi836FHd_fujDLL_s7BJYEhkNSxkcBNiuWTlYQg4MWt-rmLqz9xkyrMWw21fKGZGgt2sjUCpl_glJv4OJ7N_XfHQsbDwbCnB6czsVCuQha3sMY9wnvr55rsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی: دشمن میخواست اقتصاد مارو خراب کنه اما هیچی نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/alonews/151362" target="_blank">📅 00:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151361">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd964e9cf0.mp4?token=EfBNOkFhZc1iVRLahtDKbYTIDxwtcWdIRsl8OwETDvvAUpvpowSZo5_PAFh8u99cpm9VSfYu29CVV4k2cXu8eYaKyc6EDjOe2-_kQLjVW0tTJ8Z89euYXRhqdLX6gLRP8m0MadqD8_erOokygTNymS_76TLSVhMlQzg9hV35R237M7ms7iGq6DR7lQ6MnBzZLSDWfvn2JWzCgzgBm-CakGW40XFGAcSlhQtQZDynfvxJ8fCIOBfUGwza3SCRb-2AZ9y_g0XVM7fSJhXboFtdf1VAuNUjFiMHMIdRn_UJgT9JG3gNx71IcHeA6fBWP_c6uCku8ztQAsPen8rTSgbiYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd964e9cf0.mp4?token=EfBNOkFhZc1iVRLahtDKbYTIDxwtcWdIRsl8OwETDvvAUpvpowSZo5_PAFh8u99cpm9VSfYu29CVV4k2cXu8eYaKyc6EDjOe2-_kQLjVW0tTJ8Z89euYXRhqdLX6gLRP8m0MadqD8_erOokygTNymS_76TLSVhMlQzg9hV35R237M7ms7iGq6DR7lQ6MnBzZLSDWfvn2JWzCgzgBm-CakGW40XFGAcSlhQtQZDynfvxJ8fCIOBfUGwza3SCRb-2AZ9y_g0XVM7fSJhXboFtdf1VAuNUjFiMHMIdRn_UJgT9JG3gNx71IcHeA6fBWP_c6uCku8ztQAsPen8rTSgbiYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت بعد از اعدام علیرضا سپاهی:
🔴
عمویم محسن ‌اژه‌ای دمت گرم، اصلا اذون صبح یه جور دیگه با دل آدم بازی می‌کنه.
🔴
وقتی اذون صبح رو میگن میفهمم یکی از دشمنان خفه و سقط شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/151361" target="_blank">📅 00:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
بمب خبری
‼️
🔴
گاتزتا دلا اسپورت: رونالدو بخاطر خیانت همسرش عصبانی بود و برای همین اردوی تیم‌ملی را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/alonews/151360" target="_blank">📅 00:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9Rduu8UvLUMftFi1gtBn-y2w0ohCu3GI8BHBsVUBJxjHV2o_8RR5v0a9BtRxCVerZxIZZsB5lBNXm7ZBYuaAwMF2Vb9duCEsrJwI7CMoVl8qB2OqxPzo8sH64RajZnNbrYTCvngFS0VvvC3h6-f0IGWpnIzOeH4uPm06hD-DWyv62a8e1w8rDFl9rcDcUbGMd_w-3Gyq1IP2G-LPf4Jk4QS2WG8ku1h-yqLPEv51MmwxglkF4ccRyak35bOHhFHgywhb5USXj4GtEuJXe1vL5uJinptxGWNPU2EFcTyfeC-LeqQFvNf3LMZao0UEhVtZ9Iq3fdpMm0dSY_JFteBag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمب خبری
‼️
🔴
گاتزتا دلا اسپورت: رونالدو بخاطر خیانت همسرش عصبانی بود و برای همین اردوی تیم‌ملی را ترک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/151359" target="_blank">📅 00:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: ما 8 جنگ را به پایان رساندیم!
🔴
فکر می‌کردم پایان دادن جنگ روسیه و اوکراین ساده باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/151358" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=T6Zsl4bFgpPiWxRlsiHLl2cSXltsF12DnSdo99rVTHHh5vRscMxQOnO0_HTN7bmNT1-ogY8DeHFm_FlB06N45lOS7TrPidlrMM6od5BnUzwQWI76RQ5-KsN1-NxqOghf9zoKDyLATJHElU9q0uEcc2vxpQS8iKbORGkhItjFT-x1MzjPIAOnUF2MVocGVS31hbsZzS1-sow6ZhirLF0ZFqgY6KHLZ6BNirS_v5u-XzFKBw6PaiXYvcTCrNTpB4tePYWUnjzAAOw_9JSYJXIFXpExL8WTqPG8EcYA0kzmamAcm6YljkJfVnf4UypkTlOeIGWtBe_9dZO9VMLyLKGlSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f6433023f.mp4?token=T6Zsl4bFgpPiWxRlsiHLl2cSXltsF12DnSdo99rVTHHh5vRscMxQOnO0_HTN7bmNT1-ogY8DeHFm_FlB06N45lOS7TrPidlrMM6od5BnUzwQWI76RQ5-KsN1-NxqOghf9zoKDyLATJHElU9q0uEcc2vxpQS8iKbORGkhItjFT-x1MzjPIAOnUF2MVocGVS31hbsZzS1-sow6ZhirLF0ZFqgY6KHLZ6BNirS_v5u-XzFKBw6PaiXYvcTCrNTpB4tePYWUnjzAAOw_9JSYJXIFXpExL8WTqPG8EcYA0kzmamAcm6YljkJfVnf4UypkTlOeIGWtBe_9dZO9VMLyLKGlSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: می‌گویند: "ما برای شش ماه وارد ایران خواهیم شد."
🔴
ما واقعاً این موضوع را به محض اینکه بمب‌افکن‌های B-2 به هدف خود رسیدند، پایان دادیم، زیرا آن نقطه پایانی برای برنامه هسته‌ای آن‌ها بود و این ۹۵ درصد دلیل انجام این کار ما بود. شاید حتی ۱۰۰ درصد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/151357" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673z_-IjXnwIj3vUyeZvKce5JWMR6kemlxmbUPVOCYjWCQOur8lcw44gYopss3TpJtz6A2oNOuYaL9-FdROvQHpKANic3yHpk0-caRoySDqTzNk4bQUKadbbjv2ilbM-4wqLzqFwBIwcZnoe3okQ0iGO6GVCFLOlsRPIbIvY1-b3GQv46vnw_KlKgsqCvBVFkMxa7EcMS2qUktm2adzhOn58mFlDRpecFEfr_L5mRyzRZFhjXIznR8KRgcTFH4iIqpEKjR6gYD5Bz72Z_O1NWUtsvGiHrmjC17Ft8rLOy_ayHpVehwh8j490xW3g96S2j014YfYOApJACMcOOO3GTgIec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bb6008cb.mp4?token=BNDxnlkHW9GZuH743iwTcw6Ph4IOtk_WQbyzr_XHjUd4bUCEpVGnZRO_TC1QH9mySkcDxVh0Y1jvyGXMmhFvTIYe_VolL9ti4oE_S1wtjjtDeVgCXKZ1bsuT11RZHYDprNVi-MyXbJllgRJ5b05HPN9bwyEBTfL1vSblt3dleiH26ShwSvHzSqlilTnDEtxjqGOFgXzNgaZFVTGM3pPm-AN-NpKVVGT4Z6Un2tOZIbbZnACrAuR3AY1dWQpyQBDwhzmB4Y8KEQ3k10aIrCTtkPne3oZa9KEsq5Nur7FSxKjzF2m1K-oZSSVWbz7Egzmq-BdmisedxQIgPTCByU673z_-IjXnwIj3vUyeZvKce5JWMR6kemlxmbUPVOCYjWCQOur8lcw44gYopss3TpJtz6A2oNOuYaL9-FdROvQHpKANic3yHpk0-caRoySDqTzNk4bQUKadbbjv2ilbM-4wqLzqFwBIwcZnoe3okQ0iGO6GVCFLOlsRPIbIvY1-b3GQv46vnw_KlKgsqCvBVFkMxa7EcMS2qUktm2adzhOn58mFlDRpecFEfr_L5mRyzRZFhjXIznR8KRgcTFH4iIqpEKjR6gYD5Bz72Z_O1NWUtsvGiHrmjC17Ft8rLOy_ayHpVehwh8j490xW3g96S2j014YfYOApJACMcOOO3GTgIec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
من مدام از رهبران جهان تلفن‌هایی دریافت می‌کنم که از من [به خاطر جنگ با ایران] بسیار تشکر می‌کنند.
🔴
من گفتم: "خیلی خوب. چه زمانی می‌خواهید برای آن هزینه را پرداخت کنید؟"
🔴
ما بارِ کل جهان را بر دوش خود حمل می‌کنیم. ما از انجام این کار لذت می‌بریم، زیرا ما قوی‌تر شده‌ایم و دیگران ضعیف‌تر.
🔴
آنها فقط ضعیف شده‌اند. آنها ناکارآمد شده‌اند. ما کارهایی را انجام می‌دهیم که هیچ کشور دیگری نمی‌توانست انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/151356" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76faad4536.mp4?token=U9NRIBAgAblcllc7TEGu9UfjJKS5-OBhSWp8tY7piyeEyWw7_rCl8YWiJp-2GR8NOApyXp5s79giE_Dq5JW1HcqM6dRfjyK91eRsQeweQCqTa9tnjrLf9272TaV0nJkyh5JjiQY_NC9Qprg3JS55tXsKJAviPJthqErT3Fpao4xH8z5PE3K2v465_CgdvZzA7phXq1mUe2_PBSHRfmQdnw25zFWkUGoB7sBFLHCLElZKeGT9s69NTqnJ2aoFR6ODC-fUj7jau5bl_9u8zOAt8GYVG3yhr0J-galFpFpHzyw37WFH5-LWpTUSsw2wGIytTX-0e5yK216MWqGpCX8Z2RqiHMONJ4vIMB9nyoadilIRQE7NYxNrQvBONrdQjNtOs5xKKF4srQtgycyrC7cBAyYv1ODW43-zd3-3c-mjNMvr2NldG2cl8LpO685z789UatsfVhAcCw-EhPvcEc5EW6XnrU0rnKfBItlcK3xjX-pvZ5v_NwWwyM3o5KU81scno0IwCWMDlnI4DTtxvC6u9Y24LtNnesiv0VC5IjRAu9OdmTQUxnO8gPaSHUMP_DgmqmynvQpQFx5myJzWSP0WnH4uNmFrVJ9bkfvuo8F7XSzblEPIuDWgCtNXyQF5HBwhlSyTHJR7s60s65cY3e49nxBRklp8JWsJJ2tt97GmE2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76faad4536.mp4?token=U9NRIBAgAblcllc7TEGu9UfjJKS5-OBhSWp8tY7piyeEyWw7_rCl8YWiJp-2GR8NOApyXp5s79giE_Dq5JW1HcqM6dRfjyK91eRsQeweQCqTa9tnjrLf9272TaV0nJkyh5JjiQY_NC9Qprg3JS55tXsKJAviPJthqErT3Fpao4xH8z5PE3K2v465_CgdvZzA7phXq1mUe2_PBSHRfmQdnw25zFWkUGoB7sBFLHCLElZKeGT9s69NTqnJ2aoFR6ODC-fUj7jau5bl_9u8zOAt8GYVG3yhr0J-galFpFpHzyw37WFH5-LWpTUSsw2wGIytTX-0e5yK216MWqGpCX8Z2RqiHMONJ4vIMB9nyoadilIRQE7NYxNrQvBONrdQjNtOs5xKKF4srQtgycyrC7cBAyYv1ODW43-zd3-3c-mjNMvr2NldG2cl8LpO685z789UatsfVhAcCw-EhPvcEc5EW6XnrU0rnKfBItlcK3xjX-pvZ5v_NwWwyM3o5KU81scno0IwCWMDlnI4DTtxvC6u9Y24LtNnesiv0VC5IjRAu9OdmTQUxnO8gPaSHUMP_DgmqmynvQpQFx5myJzWSP0WnH4uNmFrVJ9bkfvuo8F7XSzblEPIuDWgCtNXyQF5HBwhlSyTHJR7s60s65cY3e49nxBRklp8JWsJJ2tt97GmE2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تنگهٔ هرمز متعلق به آمریکاست؛ جایش همان‌جاست و همین الان هم در همان‌جا قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/151355" target="_blank">📅 00:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69e4b8c78.mp4?token=isZQSNd6RZNyRveTWmIrgExg89_ljBa_-E3hWldEFB9NztYZzmuZO87VmOarhW87CpFoZ9tsNekGqfAIZwPQuLZLi9qSKTHv-NHRnS4bjRW3RMWWxncMllP_qJTUjyjb1C3I7hcZihPhaOlYaf7AFpY-xka4IDjatYBWkPhhWcJ3jck_3gjSyggJU67tijKxWIIziOFHdkNaEWeysB3LWlaOJhmrh8ylc-Ndox4QyC4ptvSPXamzkHNhOqgJfAs40zdpicyeI2sEMfMPni3pIlFnQlY7UiA-W1ZtkDRV8avOzVtnrhn_sILPiCIJkdG9FY6rYJ_wME4yciYy0pO68Iu4yehxk9f3LXFxku4PY-JmlT6nTX_YJR2ecpKcvlp41wuUbrSz2xHNZOXFJEbnkdxZycQYq5oBaUYM7buNyVNv0LtZu6nFH7604w1mOKoaIdct4nSElEYZaBknTdrx_Xa0ChAeovW-j35C_D9Io2D5fPU03-8dhfLGbUjtHIUjDcquEVz9OcfGCkURCql_xB7mq61M_KkmC9Qmk-Pzs0RBVMOqOY1m5uKs2j1N1JmpuAcAJjg_mB76Rx62nUJUG3elHz3GEXe1YztgWwykBAjtcnTrL7BgQ5KdBJe0X2csfzOFNvp-9cId0E1qPWpY49djqVTeI33TFWQA2YxvpTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69e4b8c78.mp4?token=isZQSNd6RZNyRveTWmIrgExg89_ljBa_-E3hWldEFB9NztYZzmuZO87VmOarhW87CpFoZ9tsNekGqfAIZwPQuLZLi9qSKTHv-NHRnS4bjRW3RMWWxncMllP_qJTUjyjb1C3I7hcZihPhaOlYaf7AFpY-xka4IDjatYBWkPhhWcJ3jck_3gjSyggJU67tijKxWIIziOFHdkNaEWeysB3LWlaOJhmrh8ylc-Ndox4QyC4ptvSPXamzkHNhOqgJfAs40zdpicyeI2sEMfMPni3pIlFnQlY7UiA-W1ZtkDRV8avOzVtnrhn_sILPiCIJkdG9FY6rYJ_wME4yciYy0pO68Iu4yehxk9f3LXFxku4PY-JmlT6nTX_YJR2ecpKcvlp41wuUbrSz2xHNZOXFJEbnkdxZycQYq5oBaUYM7buNyVNv0LtZu6nFH7604w1mOKoaIdct4nSElEYZaBknTdrx_Xa0ChAeovW-j35C_D9Io2D5fPU03-8dhfLGbUjtHIUjDcquEVz9OcfGCkURCql_xB7mq61M_KkmC9Qmk-Pzs0RBVMOqOY1m5uKs2j1N1JmpuAcAJjg_mB76Rx62nUJUG3elHz3GEXe1YztgWwykBAjtcnTrL7BgQ5KdBJe0X2csfzOFNvp-9cId0E1qPWpY49djqVTeI33TFWQA2YxvpTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
به لطف مردان و زنان نیروهای مسلح آمریکا، ده‌ها
رهبر تروریستی ایران
منفجر شدند و از هستی محو شدند و مستقیم به دروازه‌های جهنم فرستاده شدند.
🔴
رهبرانشان رفتند. بزرگ‌ترین مشکلی که من دارم این است که هیچ‌کس نمی‌داند چه کسی کشور را اداره می‌کند. شاید این چیز خوبی باشد.
🔴
خامنه‌ای را یادت هست؟ همه‌شان از بین رفته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/151354" target="_blank">📅 00:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عربستان به یه پسر ۲۴ ساله، بخاطر کامنت توهین به پیامبر حکم اعدام داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/151353" target="_blank">📅 00:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151352">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf346aec4.mp4?token=aO1KQp-hG0qIIDkBKnfErcjhnq17-etH2do727hxp5hUAsYQ6WSA-KaBMVEKg1sAxVn6epl_B5aT3RcZdhT1kp0I5kzEbiWV8YszP3Ytg0ISOPxyZnB4x0DkaOaDZ5VRRWDMu7eo9mbOND_iqEHwlfOxkTmqc0MVxjk_83mDVugzfxGHfDg5NUbRdLq8Oxtlri3_Vy9vVssChM0NcGWWC6CAC_9ufsDDdoV-e4CPomrIUh6Fw38xf1XjXauiMi9lIezVcAmLjxvxpJj4xS3FIQXH54R08-HnC59hTN7CYrmSkQm6mcBy2l8Onq1Y_t63xdynm33UfqhQHvwFvtfFog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf346aec4.mp4?token=aO1KQp-hG0qIIDkBKnfErcjhnq17-etH2do727hxp5hUAsYQ6WSA-KaBMVEKg1sAxVn6epl_B5aT3RcZdhT1kp0I5kzEbiWV8YszP3Ytg0ISOPxyZnB4x0DkaOaDZ5VRRWDMu7eo9mbOND_iqEHwlfOxkTmqc0MVxjk_83mDVugzfxGHfDg5NUbRdLq8Oxtlri3_Vy9vVssChM0NcGWWC6CAC_9ufsDDdoV-e4CPomrIUh6Fw38xf1XjXauiMi9lIezVcAmLjxvxpJj4xS3FIQXH54R08-HnC59hTN7CYrmSkQm6mcBy2l8Onq1Y_t63xdynm33UfqhQHvwFvtfFog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من مطمئن نیستم که شجاعت ورود به زیردریایی‌ها را داشته باشم.
🔴
شماها آن‌ها را دوست دارید، اما من ترجیح می‌دهم روی سطح دریا شناور باشم
🔴
بنابراین، من ایده یک زیردریایی خودکار را دوست دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/151352" target="_blank">📅 00:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151351">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISiiXNxWmtZFaOhTOuNlrJjXptQZO7-Caf2NwtKu6L4VSZs9JpXvo6iTUqjvZttIaB_NcAF9TRWaIbBPJBhJcE03bHM4vVpy5NTzoJA5v3K0Nc0ZbmbAq4FMoQieuoyTONJ25tIPXYd6iN3lWqF2oicYlKHd4W9EtPBhWKTAmGSRMfDzpX7EzfrxBKi38_-_jkXSbuVN_Z6yoyjYodYHRSJ6Fpf5ilKLtLhMlBGKBNC3HqyA92UzxzkyFcWsRrBQKtIHdJBQthHDiGuqrdkwUUfHN0bnDMXLqwBj2g7Q6dFF1Wxq4aAX-ekIJQ16bbkIVEVtXk0YF3pr50GVrLGXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوررری / سفارت آمریکا در مسکو، اخطاری بهداشتی صادر کرده است، مبنی بر گزارش‌هایی مبنی بر یک مورد مشکوک از بیماری طاعون ریوی در منطقه ایرکوتسک روسیه، که منجر به یک مورد فوت شده است.
🔴
این سفارتخانه اعلام کرده است که گزارش‌های مربوط به اقدامات قرنطینه و بسته‌شدن بیمارستان‌ها در ایرکوتسک را زیر نظر دارد و هشدار داده است که دولت آمریکا توانایی محدودی برای کمک به شهروندان آمریکایی در روسیه، به ویژه خارج از مسکو، دارد.
🔴
همچنین، این سفارتخانه بار دیگر بر توصیه سطح ۴ خود مبنی بر "عدم سفر" به روسیه تاکید کرده و از شهروندان آمریکایی که در حال حاضر در این کشور حضور دارند، خواست تا فوراً آنجا را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/151351" target="_blank">📅 23:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151350">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3279701bab.mp4?token=hsBhzGDYLx3WVYyEQEM9Ac6WIN1ghYzSAyghkj1rjNmcli6J__Ac3iuoF4xEwyTdXn8FQipBydKDpJnxbKLHBR_0kZPITO6ScBmwftA56NHsoUW2ZzZTmlXeRzImXT5HVoYV7Jjvd7xGFb1CFRyRfazC9X1Qg6SsTJ87TaaYDmZBcGVzliuUFxgvk4WPYvFMDpfYp0pTiLHK0WqXntYrfBF7C25UtYvuZhtiHXo8-gLSD3PcDSfVSGrfmam3yGw1BRoX3UUpuu5sJnkionXvY3UpARcnyDyaT26GprGYBPR1sH3w6zd_dNOVjOhn9Bb4pemq-Vza59YjYBxeryhEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3279701bab.mp4?token=hsBhzGDYLx3WVYyEQEM9Ac6WIN1ghYzSAyghkj1rjNmcli6J__Ac3iuoF4xEwyTdXn8FQipBydKDpJnxbKLHBR_0kZPITO6ScBmwftA56NHsoUW2ZzZTmlXeRzImXT5HVoYV7Jjvd7xGFb1CFRyRfazC9X1Qg6SsTJ87TaaYDmZBcGVzliuUFxgvk4WPYvFMDpfYp0pTiLHK0WqXntYrfBF7C25UtYvuZhtiHXo8-gLSD3PcDSfVSGrfmam3yGw1BRoX3UUpuu5sJnkionXvY3UpARcnyDyaT26GprGYBPR1sH3w6zd_dNOVjOhn9Bb4pemq-Vza59YjYBxeryhEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: در دوره اول ریاست‌جمهوری‌ام، ارتش ما را بازسازی کردم و در دوره دوم نیز تا حدودی از ارتش استفاده کردیم.
🔴
آنچه ما انجام داده‌ایم، شگفت‌انگیز است - و همه این‌ها برای صلح و خیرخواهی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/151350" target="_blank">📅 23:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151349">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72aac66a14.mp4?token=IIFLIrbZcgvqeJiIO4A56i_bE00pE3XyBHGxWAFisJugLdYNXroYbz3VkFTx3pF-UsEnmlUy51Fx79Q8n2eYXhSGAcbZ4mCbPnFdSFTzJM_MCSUh1pT7__Xs1jCbrjf9GNBIXO3MejOghOqBbv7rNNP0SPyTw0adrvB0QCgPVt4cyMLbdwwvlnWiU9akwkin0_jGpNWeUBiQsolwJ5sC9ji97XWEw-PhgDzwVU8hM-lNYv_lVZAF1bRVkb8z3zeRIvl3zB-_h_Jhed6XnawYw7T-IwPAEBSvib2i7GYIEPaxWpi5NWYGKuOB94jgOZ4s7uRs-ByIzuWIh4M5thK8NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72aac66a14.mp4?token=IIFLIrbZcgvqeJiIO4A56i_bE00pE3XyBHGxWAFisJugLdYNXroYbz3VkFTx3pF-UsEnmlUy51Fx79Q8n2eYXhSGAcbZ4mCbPnFdSFTzJM_MCSUh1pT7__Xs1jCbrjf9GNBIXO3MejOghOqBbv7rNNP0SPyTw0adrvB0QCgPVt4cyMLbdwwvlnWiU9akwkin0_jGpNWeUBiQsolwJ5sC9ji97XWEw-PhgDzwVU8hM-lNYv_lVZAF1bRVkb8z3zeRIvl3zB-_h_Jhed6XnawYw7T-IwPAEBSvib2i7GYIEPaxWpi5NWYGKuOB94jgOZ4s7uRs-ByIzuWIh4M5thK8NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : حزب جمهوری‌خواه به سرعت در حال پیشرفت است. امروز کسی گفت: «من تعجب می‌کنم که چرا؟»
🔴
من مجبور شدم به میدان بیایم و این کارها (گردهمایی‌ها) را انجام دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/151349" target="_blank">📅 23:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151348">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca07627b0.mp4?token=A2s5AZh95qUOSfJsUIiIVKPQjWNIyRBTntJUzmLb6qWnburv-xo2HP8AAWzCcBuYP6lMmE_ZKEj1Py4UTujD3lm1leeF5Ux0FXiZl4Ht0HV7OpNJHh0KsVwYymssZ6wqwcGrhLhE5a3e5AXFc6eXQSYLPvTfOkMhjnMfaZXtcRCAhjMKDO218u8EFW8FA0R5OIACjz-1XAwPwils-_nOBxYuX5TU6xXXriSxRb5xjCkoquoL63wnZHBXGracDj5SGb6u21mtWvAhD7ZooeHYIwnwpMQICfHoIfqJxWH4Inn1zOVgesmv97tCTDlgSpHBenrID_IN9tC247H2Q5Il3gEyL4La3-oEwMo3deRRp8ZP4ADpx3ACyvMe6CnzGBnf4MJcuxoXE5a1XRXLGeo5efWMiNswwHOGrWxwwvS3NSp-2alhGOgHooiGHHFiUbqiLnJgoUmdsnNn6rKiqLSWNU2s8f92_fwPAdaqrRwHyZjCQsmlDtwZiUEOK7h0arJzIPB-epSiAt4Xxrk-3CfOoh6aAq0dPklsMJ6HufjIz92lv4jSh4JzwxSSQWJta31E9CDuD4EgNUhM9l_05lUOYNbMS-l_6ESXeDBXdD5P8dNKI1co2cDFt-vEiFcc4nRe-Q1xKGsu4pzh2RVU4Fll-dhfHM8nENqkxswoR1n6lg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca07627b0.mp4?token=A2s5AZh95qUOSfJsUIiIVKPQjWNIyRBTntJUzmLb6qWnburv-xo2HP8AAWzCcBuYP6lMmE_ZKEj1Py4UTujD3lm1leeF5Ux0FXiZl4Ht0HV7OpNJHh0KsVwYymssZ6wqwcGrhLhE5a3e5AXFc6eXQSYLPvTfOkMhjnMfaZXtcRCAhjMKDO218u8EFW8FA0R5OIACjz-1XAwPwils-_nOBxYuX5TU6xXXriSxRb5xjCkoquoL63wnZHBXGracDj5SGb6u21mtWvAhD7ZooeHYIwnwpMQICfHoIfqJxWH4Inn1zOVgesmv97tCTDlgSpHBenrID_IN9tC247H2Q5Il3gEyL4La3-oEwMo3deRRp8ZP4ADpx3ACyvMe6CnzGBnf4MJcuxoXE5a1XRXLGeo5efWMiNswwHOGrWxwwvS3NSp-2alhGOgHooiGHHFiUbqiLnJgoUmdsnNn6rKiqLSWNU2s8f92_fwPAdaqrRwHyZjCQsmlDtwZiUEOK7h0arJzIPB-epSiAt4Xxrk-3CfOoh6aAq0dPklsMJ6HufjIz92lv4jSh4JzwxSSQWJta31E9CDuD4EgNUhM9l_05lUOYNbMS-l_6ESXeDBXdD5P8dNKI1co2cDFt-vEiFcc4nRe-Q1xKGsu4pzh2RVU4Fll-dhfHM8nENqkxswoR1n6lg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، اکنون ونزوئلا را به عنوان یک "سفر" توصیف می‌کند: ما روابط بسیار خوبی با ونزوئلا داریم. ما میلیاردها دلار نفت از آنجا استخراج می‌کنیم.
🔴
ما هزینه این سفر، این سفر کوچک، را بارها و بارها پرداخت کرده‌ایم.
🔴
همانطور که می‌دانید، "پیروزی از آنِ فاتح است". این یک عبارت قدیمی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/151348" target="_blank">📅 23:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151347">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
خواهر تتلو «امیرحسین مقصودلو» خبر از عفو برادرش داد
🔴
شرط دادگاه پاک کردن کل تتوهای بدنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/151347" target="_blank">📅 23:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151346">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ac1779ac.mp4?token=QIz3iZNIE_JNOGFHWMuzYSpptFx4bEjWocg9mKyDb0w6BqXTKIJrmFhZPqPu4BTpQv4tKRXSVckPCYNE_Y0TOe4mLgwTwIZ4SZ3g1fsTHpEh0RoE7A3Bhl-TMH58AOmG6iUUNgKJssVJaobCaT1G5W8Y7B85rsTY0P4sWqaNV_KV0csFu4GcGTR_EBRL-nQgNX7nNrKKOvwVt_GHsv1KKDK-OI8pnXKp7kmALs10ft9DmKax0oomDGDzOLwH8v5aWQ-i7RcOdGtVbTSsxzVpGhQh2ndxJLd3tnWX_Ct-hLN8echq9M2XYVi1FrgYdXW_C6xvho6s2qD-JyeIQSZhRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ac1779ac.mp4?token=QIz3iZNIE_JNOGFHWMuzYSpptFx4bEjWocg9mKyDb0w6BqXTKIJrmFhZPqPu4BTpQv4tKRXSVckPCYNE_Y0TOe4mLgwTwIZ4SZ3g1fsTHpEh0RoE7A3Bhl-TMH58AOmG6iUUNgKJssVJaobCaT1G5W8Y7B85rsTY0P4sWqaNV_KV0csFu4GcGTR_EBRL-nQgNX7nNrKKOvwVt_GHsv1KKDK-OI8pnXKp7kmALs10ft9DmKax0oomDGDzOLwH8v5aWQ-i7RcOdGtVbTSsxzVpGhQh2ndxJLd3tnWX_Ct-hLN8echq9M2XYVi1FrgYdXW_C6xvho6s2qD-JyeIQSZhRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «ما کمی از نیروهای نظامی استفاده کرده‌ایم؛ اما تمام این اقدامات را برای صلح و حسن‌نیت انجام داده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/151346" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151345">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d5c29e4b.mp4?token=FDCb63Ye5yfkwWiNMRiFKDTwoBTvpo-Gsg0UD-GPL2KzOGPs6mqvvxWTWC4d8QD78f0-O4JSrRSbSfkZigT399SjjUV7tFMnBt9oF617h4ykURlM8vnxuiY3UZk3ECqcbOI7QhcGyp1SGFhN88APd4T970R9UT0dly90YAnioipIk47XkpGTk7kvs4PWBG6EAguS__tqsJ-EkuHiNEiWLaQEO6qbSmj51KwB7iaPnH_FtgVTyxZkGVBqQQl31rnn6a69WLYGwAf3PiBhLdWGKOslzMapLZj8l0UteJ0b-56pojVc_LkIICFDK9w_YzeE4bxhzjvJ7IPHio0p97GrYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d5c29e4b.mp4?token=FDCb63Ye5yfkwWiNMRiFKDTwoBTvpo-Gsg0UD-GPL2KzOGPs6mqvvxWTWC4d8QD78f0-O4JSrRSbSfkZigT399SjjUV7tFMnBt9oF617h4ykURlM8vnxuiY3UZk3ECqcbOI7QhcGyp1SGFhN88APd4T970R9UT0dly90YAnioipIk47XkpGTk7kvs4PWBG6EAguS__tqsJ-EkuHiNEiWLaQEO6qbSmj51KwB7iaPnH_FtgVTyxZkGVBqQQl31rnn6a69WLYGwAf3PiBhLdWGKOslzMapLZj8l0UteJ0b-56pojVc_LkIICFDK9w_YzeE4bxhzjvJ7IPHio0p97GrYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد ایران: باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/151345" target="_blank">📅 23:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151344">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7257ff1afd.mp4?token=QrAfWGMYh1PE8pCYePGjRFWpxyJjImmncSfEvHbLQy7DG7crDQmFqM4iIY4CqUrntSnVnKJlJ0HkQmMMI0qbpqTNCJdC3WfzRQI6E95UrQ-3kf5m7Uzbwcj47HEpcsGAWkScvCut8yR6rpZRG1RiScTGrApuxFTj_fIiMcXf33UJfb4q__mw0glYN1kB659AUS9AQeKcvAATi6Yagam2t3UqpdsMPXMSPxCQWlbTpIG0TFce9e_IwN9h-HWc-4NMA1SZnQ9BHM4xkwftgJRVVjDOBkCbJ46Lhvw3kym08NTPsaVxOyJS3MXbMBi4g-gzFeSFn0Tucf7WZgY2zHPRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7257ff1afd.mp4?token=QrAfWGMYh1PE8pCYePGjRFWpxyJjImmncSfEvHbLQy7DG7crDQmFqM4iIY4CqUrntSnVnKJlJ0HkQmMMI0qbpqTNCJdC3WfzRQI6E95UrQ-3kf5m7Uzbwcj47HEpcsGAWkScvCut8yR6rpZRG1RiScTGrApuxFTj_fIiMcXf33UJfb4q__mw0glYN1kB659AUS9AQeKcvAATi6Yagam2t3UqpdsMPXMSPxCQWlbTpIG0TFce9e_IwN9h-HWc-4NMA1SZnQ9BHM4xkwftgJRVVjDOBkCbJ46Lhvw3kym08NTPsaVxOyJS3MXbMBi4g-gzFeSFn0Tucf7WZgY2zHPRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خواهر تتلو «امیرحسین مقصودلو» خبر از عفو برادرش داد
🔴
شرط دادگاه پاک کردن کل تتوهای بدنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/151344" target="_blank">📅 23:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151343">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در سلیمانیه عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/151343" target="_blank">📅 23:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151342">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/151342" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151341">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
معاریو عبری: برآوردهای نظامی می‌گه اسرائیل احتمالاً خیلی زود قراره تو یکی از جبهه‌های منطقه وارد یه عملیات نظامی بشه.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151341" target="_blank">📅 23:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151340">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA3wnOyZdADqBC33gPtBG_mGQGv8yCJ1J397dzUhg8AK2cM-MUQ3itDQszBFDCAkPs748RmAjMfMWqG0jQnTeIhChQEkFkvrDV5bXfJZCW1kn1iyowaYAcwa2ySo1c7T8RgBz2epU5NKnW81gHNzRt_u2_nDNNsGXJ23pFaqBRQe7pB27cwWZSdBRN46XvL63oCq7ZkU_E-K7cLig7C2wttUZ6NmgiRd4OB3LbsK7Ey6Mrxmd00xow37do1Hr8HROTMB1ug0QOD33MrP48OPvkhf9uFFV8h_sRhqKMV3sjEwmhTujeyJ9R2g7WeU5GMGiof_o2BYJmFmaw90HHlyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنر عجیب نصب شده تو پارک با موضوع عفاف و حیا و تشبیه بانوان به سوراخ
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/151340" target="_blank">📅 23:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151339">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b88401b5.mp4?token=gHyHcWMW7Ud-mGXqN8FT96rJVrs-pu2U_DzO0A4VoB433ZcMedSrT4gHmG3x733-XmH8UQKiOtIEnUl1mi2bYhCWRHNHjojz2Ef6Y-xmqhj8Ak-5wbFX0UJjRKDNvwuVai8Y4vHu8ujpfjHrM1RrqegPpV1qAijYxURSUnkd8CjN8hLONhYUhNQq6QlfGz9aZbCrqK-P86lZwm-vmUv2NRlGBTUDjc8gcp1WSFsgF89rWkzTAS1jKLMUEPTPzkES7mowtOmlNRdNlWzRRBm9OXw2RqpU58zAgma8NnfLGdPwJC9X8vdKVs1Cxaf6HIqhCiF6ms8R65oW6p2t2Tybww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b88401b5.mp4?token=gHyHcWMW7Ud-mGXqN8FT96rJVrs-pu2U_DzO0A4VoB433ZcMedSrT4gHmG3x733-XmH8UQKiOtIEnUl1mi2bYhCWRHNHjojz2Ef6Y-xmqhj8Ak-5wbFX0UJjRKDNvwuVai8Y4vHu8ujpfjHrM1RrqegPpV1qAijYxURSUnkd8CjN8hLONhYUhNQq6QlfGz9aZbCrqK-P86lZwm-vmUv2NRlGBTUDjc8gcp1WSFsgF89rWkzTAS1jKLMUEPTPzkES7mowtOmlNRdNlWzRRBm9OXw2RqpU58zAgma8NnfLGdPwJC9X8vdKVs1Cxaf6HIqhCiF6ms8R65oW6p2t2Tybww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره انتخابات میان‌ دوره‌ای: فکر می‌کنم عملکرد بسیار خوبی خواهیم داشت
🔴
فکر می‌کنم در انتخابات میان‌دوره‌ای عملکرد بسیار خوبی خواهیم داشت.
🔴
تجمع‌های انتخاباتی من واقعاً در حال تغییر شرایط به نفع ما هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/151339" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151338">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: ما دلار بسیار قدرتمندی داریم؛ دلیلش این است که عملکرد خوبی داریم.
🔴
دلار قوی باعث می‌شود تورم نداشته باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/151338" target="_blank">📅 22:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151337">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ: انتقال نفت به سطح پیش از جنگ بازگشته و گاهی از آن هم فراتر می‌رود
🔴
فقط طی چند روز گذشته، حجم عظیمی معادل میلیون‌ها بشکه نفت منتقل شده است.
🔴
اکنون انتقال نفت در سطحی انجام می‌شود که با پیش از جنگ برابری می‌کند و گاهی حتی از آن فراتر می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/151337" target="_blank">📅 22:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151336">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
ترامپ درباره ایران: وزیر نفت ایران همین الان استعفا داد. او گفت: «ما نه اقتصاد داریم، نه نفت داریم، هیچ‌چیز نداریم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/151336" target="_blank">📅 22:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151335">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
هیمتی: بسنت اعلام کرد تا دو هفته دیگر ایران فروپاشی اقتصادی می شود؛ ده روز از این دو هفته گذشت و اتفاقی نیافتاد
🔴
من گفتم میلیارد ها دلار خریدیم و دپو کردیم حالا فکر کرده اند ما رفتیم از فردوسی دلار خریدیم؛ منظور من چیز دیگری بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/151335" target="_blank">📅 22:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151334">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فاکس نیوز»: ناو هواپیمابر «بوش» خاورمیانه را ترک می‌کند و تنها ناو هواپیمابر «جورج واشینگتن» در منطقه خواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/151334" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151333">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
تحلیلگر صداوسیما: آمریکا چون دزدی می‌کنه دلارش بی‌برکته و به همین خاطر مردمش گرسنه هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/151333" target="_blank">📅 22:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151332">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه اینجا رو بخون تا از بازار جا نمونی
👇
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/151332" target="_blank">📅 22:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151331">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
فارس: جنگنده‌های آمریکایی در چند روز گذشته چند بار تا نزدیک مرزهای ایران آمدند مانور انجام دادند و برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/151331" target="_blank">📅 22:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151330">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=q8wc51_Q2_Cj6P9f_wO8xwQplgjxgzeYihGEwJs6VITjQjzW0NkOM64xdCKb94jh9UCSk3lV88Jrm36jPrCgqLZr5wW4bzdixmHpro8ajwALWay628rWCpEkgy7c3mcVsH8Th7KNHpaU5dRpWehbZ1D8ZmzsEhOvBnA9_YKrWCslnw1PJsKb74CoTetmkkX60i596feEhKtgcZ2ATxcDCZokdqmedujPy1FXpb4ic9EnO4iihiVaNJ-CJ1512BDQ5l_ljbt5fwqaFfBlEKUyd2Lv9QDVO7i8-KP1Jx8zWURfzaM724_eKO_-XOOu6APYgLIn38c5Qt5vJ3bjFkwy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb203d7cdb.mp4?token=q8wc51_Q2_Cj6P9f_wO8xwQplgjxgzeYihGEwJs6VITjQjzW0NkOM64xdCKb94jh9UCSk3lV88Jrm36jPrCgqLZr5wW4bzdixmHpro8ajwALWay628rWCpEkgy7c3mcVsH8Th7KNHpaU5dRpWehbZ1D8ZmzsEhOvBnA9_YKrWCslnw1PJsKb74CoTetmkkX60i596feEhKtgcZ2ATxcDCZokdqmedujPy1FXpb4ic9EnO4iihiVaNJ-CJ1512BDQ5l_ljbt5fwqaFfBlEKUyd2Lv9QDVO7i8-KP1Jx8zWURfzaM724_eKO_-XOOu6APYgLIn38c5Qt5vJ3bjFkwy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل هوادارای لیونل مسی برای خداحافظی در آستانه آخرین بازی این بازیکن برای آرژانتین
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/151330" target="_blank">📅 21:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151329">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فکت : آخرین باری که روسا گفتن وضعیت تحت کنترله، ۴۸ ساعت بعدش کل اروپا درگیر تشعشات هسته‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/151329" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151328">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عمان: یک کشتی در مسندم هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/151328" target="_blank">📅 21:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151327">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
الجزیره: در پی گسترش اعتراضات دانش‌آموزان، دولت فرانسه مدارس را تا آخر هفته تعطیل کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/151327" target="_blank">📅 21:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151326">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ثابتی: رسایی جز افراد بزرگ تاریخ ایرانه حقیقت رو گفت و روی حرفاش ایستاد و رفت زندون به خاطرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/151326" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151325">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
شرکت ایران خودرو مجددا درخواست افزایش قیمت 40 درصدی تمام زباله های خودش رو به دولت ارائه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/151325" target="_blank">📅 21:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
گزارش دو انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/151324" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151322">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLOdP8NKkEnGaVAByKoMuZRn04Yydrwv0IbesUpauOnVujVbDxeIP0FHlE2ok8Q_-bEbkXVTtky130clZmjqMpsB4yX6e0z6r6SjI-c5FZUBgJ42ANXdBIWOXzW6hwH359RBOKTNsX_-s4s2VQTa4db_sT3xKSPJlIKV8EM50AjybKpzqlaVfrgkNGcjKXxjvs-N0t-OpQfbZu8DhRBmLCpgo37vkQvimRwO1035fMaZmQgw6jNv2J3ZVvAR1fikWGXtuX31C7zwY8CtEjQofujptlnVU8DxcBNBc8RGK-PHdy1W9fUaqlA-S3Lv1RiJoVjK8htSCtwGWT565d--yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bN5GTw3i5POCrt09OpxkFz0gRo50BWjfUgu7yT8vTxyntlpPZSGjFWrzC0ohKsllyHE7JaLnAHX3h35b4I2yZk3WCJYhsUIfhXjodxRJL1aagfr1cWbO1L7te2uzWnrOqSIcdqDvgkAk5L6vssITQmuHLHcsCUUs-ux1qUeiZrTps2E5jdXvrFXsU-TcZBz8GQV8FBYM5fU6OTWDYJzFTfqTDD6lA8cTza5jGp6JNdEu4Ztzr3nT6QMWmxqApwazHJz_4ypGfPnmBlSBTi8CC8r002jzqmRadeB7D5KETtH6zQBFIASN9DAyBjzhquujkK0k2vIorF2ZlM01013zTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدیدی از ستون‌های دود برخاسته از تأسیسات آرامکو در روز گذشته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/151322" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری / روزنامه عبری «معاریو»: برآوردهای قطعی نظامی حاکی از آن است که اسرائیل در آستانه انجام یک عملیات نظامی در یکی از جبهه‌های منطقه قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/151321" target="_blank">📅 20:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فاینشنال تایمز: مذاکرات ایران و آمریکا پشت پرده ادامه دارد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/151320" target="_blank">📅 20:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مرگ مشکوک در آزمایشگاه ایرکوتسک روسیه؛ آمریکا از احتمال بروز طاعون ریوی ابراز نگرانی کرد
🔴
وزارت خارجه ایالات متحده: گزارش‌ها را با دقت زیر نظر داریم
🔴
مسکو اطلاعات دقیق را «سریع و شفاف» منتشر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/151319" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
الجزیره: رهبران دموکرات، شوخی ترامپ درباره اجازه دادن به ایران برای بمباران لس‌آنجلس و سن‌دیگو را محکوم کردند
🔴
آن‌ها رئیس‌جمهور آمریکا را «آشفته و خطرناک» توصیف کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/151318" target="_blank">📅 20:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTaawvfS0gbeDa_wYkr87v_Kd8OlM0R_KuIlOViyRwnkobU9eM3crkJD5HJOerXkHpl5j2MFgZ0Mx_lM1sMIMEqSgN4v4hqD6KREApmpH8M1gfsNbjFoYpSZhdqC0DC75E6hmGmIe7AR9qr-oNrlCxs_5ile1_qCanq7W-cLKBNcgZIbS5SK2lIHw5twC3moh8NSrLH2D8BSur0VBgWc8vVrLa-2UZGi70iWGevW3hDcV0mWkiQaBaz889F2WZ-S2G-OKe4IUhRoaF3k5vNoTg3djWPsOOraTAjNpUgo8dR-97xdL3TeKm_JYy3B9GIl3VZwQy9md_UihzRgOAnboQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تردد پروازها در فرودگاه القریات عربستان سعودی، در نزدیکی مرز اردن، متوقف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/151317" target="_blank">📅 20:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ریانووستی: یوری اوشاکوف، دستیار رئیس‌ جمهور روسیه اعلام کرد که ولادیمیر پوتین، رئیس‌جمهور این کشور در جریان سفر خود به ترکمنستان برای شرکت در نشست سران کشورهای مستقل مشترک‌المنافع، روز جمعه نهم اکتبر با مسعود پزشکیان همتای ایرانی خود به‌صورت دوجانبه دیدار خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/151316" target="_blank">📅 20:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شلیک موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/151315" target="_blank">📅 20:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یک مقام قطری: مذاکرات بین ایالات متحده و ایران همچنان ادامه دارد و پیام‌ هایی بین واشنگتن و تهران رد و بدل می‌شود و قطر نقش میانجی را ایفا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/151314" target="_blank">📅 19:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
رایتل رسما اعلام ورشکستگی کرد و سهام خودشو به مبلغ 130 همت در مزایده قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/151313" target="_blank">📅 19:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر کشور برای انتقال پیام امیر قطر به پزشکیان عازم تهران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/151312" target="_blank">📅 19:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151310">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=fTSj2FdB4qn3ftXzDPAIjzlKT4GONe0aFs-ZI-lVUEOMZcfizMOSu888HqYXstai7mf_igTyYzq1d2gB9_JxC0hxEbbv0UOzzHuufNw7rCf_M5Dlx868WJrWmFL1V2lBMIG_MnOog5lExRIZKt7tBjBf9RkLA_qSbiDce6-LRy6bsrgto6pvz1XY9BFgg1cQ6RVg-1dFf2Nnqf0q35vSg0SdAWykTyXjoKXnGQuMmQhfUPnSovpN0Q0_o5FOIAwYzdQ1SaQnbZgssN8Ylkov4TI69b5Up68VkVAk1lLjyvQ8sRKwayCNHE5seUfYKyhdoirR0coX_7AwI7TOwd5mSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab32d7fd77.mp4?token=fTSj2FdB4qn3ftXzDPAIjzlKT4GONe0aFs-ZI-lVUEOMZcfizMOSu888HqYXstai7mf_igTyYzq1d2gB9_JxC0hxEbbv0UOzzHuufNw7rCf_M5Dlx868WJrWmFL1V2lBMIG_MnOog5lExRIZKt7tBjBf9RkLA_qSbiDce6-LRy6bsrgto6pvz1XY9BFgg1cQ6RVg-1dFf2Nnqf0q35vSg0SdAWykTyXjoKXnGQuMmQhfUPnSovpN0Q0_o5FOIAwYzdQ1SaQnbZgssN8Ylkov4TI69b5Up68VkVAk1lLjyvQ8sRKwayCNHE5seUfYKyhdoirR0coX_7AwI7TOwd5mSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدون شک این عجیب‌ترین پرونده فساد توی تاریخ ورزش کشوره!
یه خانم با تیمای بزرگ فوتبال مملکت قرارداد می‌بسته و می‌گفته بهم پول بدین، منم در ازاش با داور سکس میکنم تا نتیجه رو به نفع شما بگیره!
بعد از دستگیری، این خانم اعتراف کرده که با بیش از ۴۰ داور سکس داشته و باعث صعود خیلی از تیما شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/151310" target="_blank">📅 19:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad6fe8b02.mp4?token=CS5a0K4v01_wFX6Yz5Yzd37SjgKXSNu96fVMOeGBr0wcYYCSZ3CA0wAfqrHLjFgQGtF0G2A1M7bfxmCl0pHGz4-dT-nn5zLTjvbasFc4KYUiGTgPpEHXTS4uojEOnOebioh4yY9ZbOekkKhOuVredi0EdeoOGsr95HCFdm0A-SAO7TX2cH20TEiYinIQuX7ST3-yXcPFOMGdCdguHWI-vVhFbslXOVuO7NFnyeOeA_M8X85FRXA_zy7hIHS8QLEqtz0Xg0uXhvQfbFQfcwdaS5CVtzUfa0cUY2aKv37Q7ADGkduA-ivanTOLigMkXFeVnQTH3o8fAqQTWI4hFlHcGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad6fe8b02.mp4?token=CS5a0K4v01_wFX6Yz5Yzd37SjgKXSNu96fVMOeGBr0wcYYCSZ3CA0wAfqrHLjFgQGtF0G2A1M7bfxmCl0pHGz4-dT-nn5zLTjvbasFc4KYUiGTgPpEHXTS4uojEOnOebioh4yY9ZbOekkKhOuVredi0EdeoOGsr95HCFdm0A-SAO7TX2cH20TEiYinIQuX7ST3-yXcPFOMGdCdguHWI-vVhFbslXOVuO7NFnyeOeA_M8X85FRXA_zy7hIHS8QLEqtz0Xg0uXhvQfbFQfcwdaS5CVtzUfa0cUY2aKv37Q7ADGkduA-ivanTOLigMkXFeVnQTH3o8fAqQTWI4hFlHcGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/151308" target="_blank">📅 19:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151306">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏
👈
پاکستان: خبر استقرار ۳۰ تا ۴۰ هزار نیروی نظامی ما در عربستان، ساختگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/151306" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151303">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DZi4IVFZgJDAHSzddQ6v2EKo1dKpsmkSBbraRPR8bB3ey2E_aqHXTKdMRmTStsN2LLZeD3KyeuHFXSWlLzhTD_eb0i1LwPROG9ieS6v0UNyUfOeTNR544aMTpYNH6613Ci9rpcnjmAQN56iytH95gX7DrbQkFttK25H6qlCv05TeMuS0xxuFwOL6l2xXP8XYWiTbUzNoNKZTeVWVVW9exywTGRZtxpDztaf6t5u21iX7jVZXgXwe5lMnI79eVdjEymW14uA_OXbRQpbi9CWP3tW0k8zpA2wqIoQozTIArjSp9SFxzHD6Hsu8q8e1KbVOb7a4kVFt_57hJNUKTOgUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZI93l5R3L0lt4ASH-xc3-Q6p3ReL7suT-Xgbmlpbe7XavSDbp2CXmD72MlAkCso9eFOwseLcHslO9vAlZh1cI-kie9ZZiLHcMgl3X2ILTxvabfoqhxH_nl_iSBEYMxXs8Y8fio3vw2yoMZojVqRsY4bcokAkTWMAO_5EHsIZ2vCFQz90Vtzyiog56WCfRgOSBK9jU96LXa7mwjQLMHGiKU4m7LNPC-DxNEnBFkIUACERum14xQIDPoyfHoi7J0GNXoKfJoVXHhm3J4zwUC7bPMqM1U7xaYVYohYQj3A-c2NhqSFQPr-hdNO42CgNhuyqCJMKbhm4lsNVr_vO5KZ_qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5c69c2aaa.mp4?token=TR1whVBWsHQSSNZk2VeLOcG2Ez9wcyL94w0HHDsY-uSDpwhkg9uGPNrlkMCxt5nzH7q4pe-phS_dCYHlhfMI1eq85FGC9Szus74CqVNJG_W_9loNl3VNh1e8X7v89AUU31D6hGoSwB3Fk95vuj3DqEpLwwPGq4UUkesegXw0Lx3Dc3HnYQH9XpY3ay8pKRVF78qybwf0os4p_a8B5nmpwqvtf77xl0shxgr63KFQCR-76nPuxvTKE0QugQtbx4UGtL-mQbrRLYQ5rnosMzFwnqpZyL28eEqy3K0Oj35Qj_P3XiWuf8G8FUkPpmiomUjt4CYt7vJfMqp2W_smoITZRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5c69c2aaa.mp4?token=TR1whVBWsHQSSNZk2VeLOcG2Ez9wcyL94w0HHDsY-uSDpwhkg9uGPNrlkMCxt5nzH7q4pe-phS_dCYHlhfMI1eq85FGC9Szus74CqVNJG_W_9loNl3VNh1e8X7v89AUU31D6hGoSwB3Fk95vuj3DqEpLwwPGq4UUkesegXw0Lx3Dc3HnYQH9XpY3ay8pKRVF78qybwf0os4p_a8B5nmpwqvtf77xl0shxgr63KFQCR-76nPuxvTKE0QugQtbx4UGtL-mQbrRLYQ5rnosMzFwnqpZyL28eEqy3K0Oj35Qj_P3XiWuf8G8FUkPpmiomUjt4CYt7vJfMqp2W_smoITZRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم و تصاویری از بمباران توپخانه اسرائیل که بیت یاحون را در جنوب لبنان هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/151303" target="_blank">📅 19:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151298">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8Tj8koKC0Gycq4BZaRtnqBVAwwWQxFZJWeFWmbdz8uUixgabVxZRatHj2tBRisBDo5igpinpU7AEGm3L4aqnKYAqFhL5uZdDk4kxfoQ83ywTi2dI0qf_Ck-UXkY9LbmwMXofLm2A6USLWN-WRZSbU42MxpCqiRRhDJWIBjQTirPOjgnHja0r1f_SKlM78nrJa-1-31kI18E_yQS9djTrpBVDmqTNPeUdNbuAspuhJb2nZkL5Y_cao6knzFx_BonHocSeyz702kgP4Mr09rOAd6cdFcsMSWd5XHHEX5KAYSfFexTQeeAAHvSRmI3yOPToj77p9NxrWRss0cY-_jMzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درمورد اتفاقات فرانسه:
آنچه در فرانسه در حال رخ دادن است چیزی کمتر از مهاجرت انبوه و خارج از کنترل نیست. این موضوع درباره مدارس نیست؛ این درباره اسلام است که می‌خواهد کشوری را که زمانی بزرگ بود تسخیر کند! رئیس‌جمهور دی‌جی‌تی
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/151298" target="_blank">📅 19:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151297">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شورای امنیت ملی اسرائیل به اسرائیلی‌ها هشدار داده است که ممکن است فردا، در سالگرد ۷ اکتبر، مورد حملاتی در خارج قرار گیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/151297" target="_blank">📅 18:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151296">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZciWHD_dQN9zPccC62vwYBLUgC9sfmCB-_Il6qNuFr89FCo-1Zc5mS_0VlPmRQK1T7YWWaD_VS-edveXwRUoYWn6H4BX2Nml7yf-dy3llBXdvVRZcsk1OuyX-jbfo6teUraeA3QCttjMT8HNOC-whGYMJ73e0PsLqp2d3wxl4SXIxfKo_XfG0fxjS-LyZo4jfani4823QUn7OWBmaYnCfo5pV_075A8mz6F8jyFjzrFc--pARWSkm6G4VruPROuUSldk5m-IkkEqJrbYZ2g-Z5CK3kw2jphBhWAYvVE32L4IxUm8Ro2yhVGhx3uIa3F-aizpZWspS4YFkGuxq690Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طاعون روسی دومین کشته خودشو ثبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/151296" target="_blank">📅 18:41 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151295">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d58e2d38.mp4?token=WW_nLL2Xp2_a3_4Ebxh28QqLWPY8kY4RivVbpSWAm11NycfGQzNVcgwSgp77V5syEXfBypG5jGaGpdgBI78AHPbuGJD81nd90FgiKVghGI_gu9jqb_cunCCo4dpyUAb6zTVHOWURSyooz0FjMeUm_4G5ovawCID_dXuE8rcqpxpIUMDbRuNEaZJqUvDnezszeDaiTerMuFdUKyaabZcE5Nazsylln602ajsXgVAEjLy8KPslFKbDt1pUOn4EjWfvcJnAsIR834WOtVHget1NMkRJGdwTbHK80wPrIO90Z9w5_oKCp_f7frqdhUYPIX59RRtEzrSLMRQI5QUoUuTAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d58e2d38.mp4?token=WW_nLL2Xp2_a3_4Ebxh28QqLWPY8kY4RivVbpSWAm11NycfGQzNVcgwSgp77V5syEXfBypG5jGaGpdgBI78AHPbuGJD81nd90FgiKVghGI_gu9jqb_cunCCo4dpyUAb6zTVHOWURSyooz0FjMeUm_4G5ovawCID_dXuE8rcqpxpIUMDbRuNEaZJqUvDnezszeDaiTerMuFdUKyaabZcE5Nazsylln602ajsXgVAEjLy8KPslFKbDt1pUOn4EjWfvcJnAsIR834WOtVHget1NMkRJGdwTbHK80wPrIO90Z9w5_oKCp_f7frqdhUYPIX59RRtEzrSLMRQI5QUoUuTAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت عجیب آرامکو
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/151295" target="_blank">📅 18:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151294">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رویترز: پالایشگاه‌های مستقل چین با کاهش شدید عرضه نفت ایران، خرید نفت از عراق و قطر را افزایش داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/151294" target="_blank">📅 18:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151293">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مدیرعامل آرامکو: تا تنگۀ هرمز باز نشود، فشار بر بازار نفت ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/151293" target="_blank">📅 18:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151292">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLb70JhNIRf8gwu8C28t2HJCob_DdNpBl0ZdgGZDGZbZyLTeRMvdIb_78Cil0HcurP0UfrK5lQVy7ojAinSo0yupe3Gy7wPr4N77GxKnaHmq9lO2eyPAvGNQUs1qWQhq_5E_keBwNORI_uh-4JY1BNu1uaLS21qYkn2AxVB-YUzlR01VfUB0Q6iAY3aB8jfpw7CXPxysAhHxmBxnxX8fb57xFfbGZPpU8QBJfDcvY6yL1JWaHrIqJ6X83i22vF8Bwvn335FQ9-RYdAS-44kgOxXTrLPL5Od8aa8lnRghq1ioBvr0P9BHVscPYsLiXDQZ1jUAOQbyl5Kbv-NRaFZmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق تروث سوشال:
گردهمایی‌های من بار دیگر حزب جمهوری‌خواه را نجات می‌دهند!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/151292" target="_blank">📅 17:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151291">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‏
👈
ایران سفیر فرانسه رو بخاطر سرکوب اعتراضات در فرانسه احضار کرد
😂
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/151291" target="_blank">📅 17:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151290">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d4fc5eba.mp4?token=haehAV77ciDz-2vbzlJtXJKZbvNRJE0LRrE9SBBFuNhTM8HyX2U4QJ66oNymDe0u6wyuszit3BePbEJl1JVho7FOOIUOrRGNOFjzXIRIlCxhilGTsL88Cc0wE61zHKhe5syGUkPJLSAPRl5mPeyCSq1iMxXjiyBxwkrxEwPAtVaVU0jzfraA6d2J-KJBb-FAk1MrgYE0gUI2L_DNtkVVaSKQLg7cx4cUfOTi4WFzbb_JHyBEjEt9nyX-t-OswJXSs48y6Rf40GFPFwyPmUkcNXLk7AQN303FRqYQgjUrv0t4Bb4XjKBgnrmUGrZvMUqhBtGqtNJ_StZstzIBXn_aJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d4fc5eba.mp4?token=haehAV77ciDz-2vbzlJtXJKZbvNRJE0LRrE9SBBFuNhTM8HyX2U4QJ66oNymDe0u6wyuszit3BePbEJl1JVho7FOOIUOrRGNOFjzXIRIlCxhilGTsL88Cc0wE61zHKhe5syGUkPJLSAPRl5mPeyCSq1iMxXjiyBxwkrxEwPAtVaVU0jzfraA6d2J-KJBb-FAk1MrgYE0gUI2L_DNtkVVaSKQLg7cx4cUfOTi4WFzbb_JHyBEjEt9nyX-t-OswJXSs48y6Rf40GFPFwyPmUkcNXLk7AQN303FRqYQgjUrv0t4Bb4XjKBgnrmUGrZvMUqhBtGqtNJ_StZstzIBXn_aJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه آخوند تو تجمعات شبانه :
یکی داشت رد میشد گفت حاجی پرچمت خیلی بزرگ نیست؟ گفتم از این به بعد تاکید رو چوبِ پرچمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/151290" target="_blank">📅 17:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151288">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
یک پزشک تو فضای مجازی : اگه طاعون تو ایران شیوع پیدا کنه، تعداد کشته ها تو ایران خیلی زیاد خواهد بود چون مردم ما علاقه زیادی به مصرف آنتی بیوتیک دارن و از گذشته به خاطر سرماخوردگی آنتی بیوتیک مصرف کردن و الان بدنشون نسبت به آنتی بیوتیک مقاوم شده و اگه خدایی نکرده به طاعون مبتلا بشن دارو دیگه روشون جواب نمیده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/151288" target="_blank">📅 17:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151287">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏
👈
دستگیری سارق تلفن همراه سیاوش طهمورث
‏
🔴
سارق سابقه‌دار: معتادم، کسی به من کار نمی‌دهد!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/151287" target="_blank">📅 17:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151286">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
گوترش دبیرکل سازمان ملل متحد: خیلی نگران جنگم از آمریکا و ایران میخوام خیلی سریع دیپلماسی بازگردند و به جنگ پایان دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/151286" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151285">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64f2b181f4.mp4?token=ZAM_8b3tS9LutO_onoBmp2BjQ1XI4DlQ5mzpRjZ7oaSW-fwIn6_Ja8iwJlJzox9fljVbZ0TkTwbLyTNdFi7sViNyDEqETYjfLFQJ8vtzHC6Ro9Zp1DLfS33pYd1LW23GHNnCnaoW2vHzHzJptr0LCpb9nRJjDX7xNxg6fUzWpTwHrhtLDkvoC7Io6CuyaOWf6pMWtuA4RyINYwiw1PrRWhAnvYNrp2ZxCwiE2Yp1sOMZAVzB3ijOTeigZLjV-NR-tjnoCQzvFFtRnoKyIGZR3aBVioROaZCTr92EcIMeKONVOAMaaLFVgQBY38djkrFMKpDbuSWT5twa0DCjN0Vcjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64f2b181f4.mp4?token=ZAM_8b3tS9LutO_onoBmp2BjQ1XI4DlQ5mzpRjZ7oaSW-fwIn6_Ja8iwJlJzox9fljVbZ0TkTwbLyTNdFi7sViNyDEqETYjfLFQJ8vtzHC6Ro9Zp1DLfS33pYd1LW23GHNnCnaoW2vHzHzJptr0LCpb9nRJjDX7xNxg6fUzWpTwHrhtLDkvoC7Io6CuyaOWf6pMWtuA4RyINYwiw1PrRWhAnvYNrp2ZxCwiE2Yp1sOMZAVzB3ijOTeigZLjV-NR-tjnoCQzvFFtRnoKyIGZR3aBVioROaZCTr92EcIMeKONVOAMaaLFVgQBY38djkrFMKpDbuSWT5twa0DCjN0Vcjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی به ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/alonews/151285" target="_blank">📅 16:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151284">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی به آمریکا:
شما در جنگ نظامی شکست خوردید و در جنگ اقتصادی نیز شکست خواهید خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/151284" target="_blank">📅 16:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151283">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDWUUxjP2cHXmRhocMWFrXWl4Ulg_eBDpdwB0njqdJDgTrql3-up9VyrfwX_f7rM37c8fHLQBoc9681s2ag1luqmcGnXyYxBQ90uECxLw53G6kB3jogBRnucKJdggrnQgEKMoCCUYP_UQOozUhokrjiEx6zBzTFkIiZ6ak-ANBss7ierY6h9FJX04lbRDji3-tRlQDrGEJKkJlK46A3XGXFUdT0LplYwx8zOw8vddSEFlu_1K3zhSUUuMIqzCt-zRK67FpiRH2psOm0yvgvpl3RlhhIWwywVbcNuSjg7BnfhEk9-tWCKHrxzx88nN2Kc-F0MCann7llITyD50DEJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: گزارش ها مبنی بر سقوط یکی از هلیکوپترهای ما دیشب در دریای سرخ نادرست است. نیروهای ما در خاورمیانه در امنیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/151283" target="_blank">📅 16:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151282">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJXtr_LqaonnANHb-yF-NL1AWo65YqcX5T71FC7FQZrtkqclQ0-hEIfl9fggdsmOb35m4NQ3USQT8YG45mlRYzyPZnzEQOTlMVfIhU04xhVS3EOQ98M42Kyw4GnqdW8GYFcRmCxL9HcqOlCPOqr_OFzv8dLX3RQ6QyJ3DKRI5n4qSqC3u5qbOfOVj5Cm6znAktoAnPtWomp18sfdDLo9a3zZms2D5S4eVYwNgZxe-znxmRTXDEusufobBrPWwYaarZeieBnrAYfV1jL-YXN9IPUtyHM1q1hPAvuHRHlqODt8RGPWxFof7ZwwUr62Km38iNzt5sxOIGDJm0rPZAsFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت هم‌اکنون ۹۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/151282" target="_blank">📅 16:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151281">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=hcXk320HXxHf1VDCAcCbJerGEIh-Ao7CU5RG8iBful4h6O9UIvDe4VbY_KnOadmorsybFF8ITynv-UVIOBaKutAwihLXIE3piTcbseDiyouK1A5m4PAisU1EXgDyoITB1LbHxtakQQzhbWGf9jTDDDx8jy2mPBbPylDkXivtMF3T1YB38bXy_p5IDH9m2A5TFM8qZlE5tOarO8wMgqFXx3AIMlhjG0maDLaGDXDlAU6QUIyqXpFd7yYYOyViKvxk_ti4Jmhbw9BjgnrKIAp_NQnC1_zPCDcOPwstBzi8J-gHJ8cRcVWzNDKHPxgEnmfRqNFlqNWUgVeO32Y1Zpt4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24468a4f6c.mp4?token=hcXk320HXxHf1VDCAcCbJerGEIh-Ao7CU5RG8iBful4h6O9UIvDe4VbY_KnOadmorsybFF8ITynv-UVIOBaKutAwihLXIE3piTcbseDiyouK1A5m4PAisU1EXgDyoITB1LbHxtakQQzhbWGf9jTDDDx8jy2mPBbPylDkXivtMF3T1YB38bXy_p5IDH9m2A5TFM8qZlE5tOarO8wMgqFXx3AIMlhjG0maDLaGDXDlAU6QUIyqXpFd7yYYOyViKvxk_ti4Jmhbw9BjgnrKIAp_NQnC1_zPCDcOPwstBzi8J-gHJ8cRcVWzNDKHPxgEnmfRqNFlqNWUgVeO32Y1Zpt4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد  #سیرک
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/151281" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151280">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پزشکیان با صدور حکمی پاک‌نژاد وزیر سابق نفت را به عنوان مشاور خود منصوب کرد
#سیرک
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/151280" target="_blank">📅 16:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151279">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پلیس انگلیس: یک شهروند به اتهام تلاش برای انجام اقدامات تروریستی در نزدیکی پایگاه نیروی هوایی فیرفورد دستگیر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/151279" target="_blank">📅 16:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151278">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93e00a668e.mp4?token=vRNaaeWRlZbsSAYANDRPMPy08yw0Nxfq9v3i88eT-11iyoOm-lu263TjxSmngcJkImGGJxumNurokuq7kqQiayOZaEdKf6ouLCBzgLJd_SaZ5N-J7gGj0EirWGG6WGtCnadjVTvs1r8Ktu0XKY53cBGZeO9QKgOnXKhOHWebPwre9dMbKVP_HLRi2EbsdNk_yU1hmPKdGAycC6wvk4axSrwhfCkzD9R5H8RBAe9916haMSd2NQ2tLsaON65f8KaiMZMMFKG7jRuYjtYZ2fxIiZ7gfVvT8tW0RbW93GzNBla_rZjgsnEj_Gmzg4GivjesxG56FQhQaAEi7DAI80mMsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93e00a668e.mp4?token=vRNaaeWRlZbsSAYANDRPMPy08yw0Nxfq9v3i88eT-11iyoOm-lu263TjxSmngcJkImGGJxumNurokuq7kqQiayOZaEdKf6ouLCBzgLJd_SaZ5N-J7gGj0EirWGG6WGtCnadjVTvs1r8Ktu0XKY53cBGZeO9QKgOnXKhOHWebPwre9dMbKVP_HLRi2EbsdNk_yU1hmPKdGAycC6wvk4axSrwhfCkzD9R5H8RBAe9916haMSd2NQ2tLsaON65f8KaiMZMMFKG7jRuYjtYZ2fxIiZ7gfVvT8tW0RbW93GzNBla_rZjgsnEj_Gmzg4GivjesxG56FQhQaAEi7DAI80mMsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حداد عادل : هربار میومدم خونه و میدیدم یه جفت کفش له و درب و داغون جلو دره، میفهمیدم مجتبی اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/151278" target="_blank">📅 16:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151277">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
مارکو روبیو: جهان در طول ۲۰ سال گذشته تغییر کرده است. تمرکز ما تغییر کرده است.
🔴
من فکر می‌کنم ایسلند و موقعیت آن نقش حیاتی در دفاع از اروپا و میهن ایالات متحده ایفا می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/151277" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151276">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a8054a9b.mp4?token=nxKu2qEnIzaw2YU1EXnE4LHOz0BZDnLRuO9ZPrtBNC4u-IOKtAlxXu57H7il2nrXw4MUCF3j437-mAPrpxk84t6zY2B513b5BFRfNKvGD-3i8KG6NGcQjYqNoMoBjIRFiSKQjRZdQoBUinDnc-Byc8WICiPlTZ_M7aDDr-nNI3xBhHHEn-Tl_QQwHAJrPOqj-6hYCeHk4yjbljIOHvGR9GaTzPjbLC_8ViK_llfswMpo4CF6X1ssX2MrYBAOz6DH-xGW8dLL6gEmSnSGvsdKB8JM-B0PEx-0OLOOp2NlNqAzaOasJoBTXJo61P01z8Lp42PPw8gqQobTbhWioFkHao3YLZgL-uTIGex4Ojq9KBgcPPZD_M8Xb_skZr1iGk-Jzts6U3z-B-WCk_FyOXBwQ0HDZdBW31ivp8i-zZZ1PwZhN1F8KSmxQ08wwxoOyaC67l4sozlM3eV1DHWwPSjir7a0jHz3GKnNB_-eAB_VJyLVtnBhs6vH2-Rjwz-TUpsnpVOwZuUMlJhvX7IaqI_wt4lRs7bWq4heQeTUJxMbcuwG5OrOijO_BIkZJ7bAZa_YJ0Zal0XJDHNusDblWYJTHmphzDlqmxTAuxtC7yoYxQfpI9ueM7351n8QLwSomV-w98sily5zzyB5W2SFx2Za6OyA0KO2P1jzg6cZuBiA7AM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a8054a9b.mp4?token=nxKu2qEnIzaw2YU1EXnE4LHOz0BZDnLRuO9ZPrtBNC4u-IOKtAlxXu57H7il2nrXw4MUCF3j437-mAPrpxk84t6zY2B513b5BFRfNKvGD-3i8KG6NGcQjYqNoMoBjIRFiSKQjRZdQoBUinDnc-Byc8WICiPlTZ_M7aDDr-nNI3xBhHHEn-Tl_QQwHAJrPOqj-6hYCeHk4yjbljIOHvGR9GaTzPjbLC_8ViK_llfswMpo4CF6X1ssX2MrYBAOz6DH-xGW8dLL6gEmSnSGvsdKB8JM-B0PEx-0OLOOp2NlNqAzaOasJoBTXJo61P01z8Lp42PPw8gqQobTbhWioFkHao3YLZgL-uTIGex4Ojq9KBgcPPZD_M8Xb_skZr1iGk-Jzts6U3z-B-WCk_FyOXBwQ0HDZdBW31ivp8i-zZZ1PwZhN1F8KSmxQ08wwxoOyaC67l4sozlM3eV1DHWwPSjir7a0jHz3GKnNB_-eAB_VJyLVtnBhs6vH2-Rjwz-TUpsnpVOwZuUMlJhvX7IaqI_wt4lRs7bWq4heQeTUJxMbcuwG5OrOijO_BIkZJ7bAZa_YJ0Zal0XJDHNusDblWYJTHmphzDlqmxTAuxtC7yoYxQfpI9ueM7351n8QLwSomV-w98sily5zzyB5W2SFx2Za6OyA0KO2P1jzg6cZuBiA7AM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره اوکراین: عضویت در ناتو در حال حاضر روی میز نیست
🔴
در حال حاضر، ما صرفاً بر پایان این تعارض تمرکز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/151276" target="_blank">📅 16:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151275">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مارکو روبیو درباره مورد مشکوک طاعون در روسیه: به نظر می‌رسد روسیه موظف است که به وضوح اطلاعات بیشتری را با جهان به اشتراک بگذارد
🔴
این کاری است که باید انجام دهند. امیدواریم که این کار را انجام دهند
🔴
ما این موضوع را به دقت زیر نظر داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/151275" target="_blank">📅 16:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151274">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/151274" target="_blank">📅 16:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151273">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151273" target="_blank">📅 16:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151272">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP48Egffxc1UAh4dEfh30EGCVRYa3ofkZdohrRAXNfb9dZmzPsjVcwz8utXXQuWZUYDKxu6ZTBmykr0d91rDzG5PRu_2QCi78u3r0sz6GKNqI3EP3E4aZwsDfq9L9iLm5Fp_9VAzS3U0JB3XzNZIQcTXYHsbfNBe2Yb1bE4x-3i9d7HmdJQ0ACemAVBrfH8sUcMl5w3dYA_bY3lAeHTlkOqCFWtlxczkZR_v7SIUXqDDin6ATOml3VNpoSSnpv6qzB4ATT6fIKLVMY4Vn5nr7lSIcbW3-et9FN29XYIk3sH_Dv2mZwatvRbDlvGhwq0NnbV6mWFbgHKe6pJVa6kXWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: باید جلوی دستیابی ایران به سلاح های هسته ای را بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/151272" target="_blank">📅 16:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151270">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNLqIceCoAhnUc1YLW7EEvaF6F1eeW8GFdLJT2ycVQ8o_0-cPzQpJB7B83EVrGiNoQZBov05nBBGE4X7gFPBBvanu5MeEgo0TkM0e1O4uqEG4jm7pqukOO6MXD8RLpAUEL6wdIeBwNjnBFhdDS48PnabacwZCtO-6YLJkWlpfqT_wPN4hyisjGdM3wjJIu_ppfwHr84MuKuC1UQMJB4ZiAdQUj8TbE18XieehpA3QdCAQN2sJQQ0EYI9-vJXntzHtyr9V7mQyO5hH2yzfRFngovSHF7AoDOpab-_RK6esCKelef3DcfE0RCfnZR34PEkg1tBlOvwrLmQj2kw0TL7yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
یک نفتکش که در حال عبور خروجی از تنگه هرمز بود، در تاریخ ۶ اکتبر هدف اصابت یک پرتابه ناشناس قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151270" target="_blank">📅 15:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151269">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گزارشات از اختلال شدید در اینترنت
👎
👍
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/151269" target="_blank">📅 15:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151268">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر کشور در دوحه: از نقش منصفانه و میانجی‌گرایانه قطر و پاکستان تشکر کردیم
🔴
بحث‌های مطرح شد که ان‌شاءالله سطح تنش‌ها کاهش پیدا کند و سایه جنگ از منطقه دور شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/151268" target="_blank">📅 15:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151267">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز: پالایشگاه‌های نفتی چین، خرید خود از نفت خام عراق را افزایش داده‌اند تا کمبود عرضه نفت ایران از طریق تنگه هرمز را جبران کنند
🔴
بر اساس این گزارش، حداقل ۱۲ میلیون بشکه نفت خام از عراق و قطر خریداری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/151267" target="_blank">📅 15:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151266">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
عارف: ما به هیچ‌وجه نگران تحریم‌ها نیستیم، چونکه کشور ما در برابر تحریم‌ها آب‌دیده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/151266" target="_blank">📅 15:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151265">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تسنیم: پلیس فرانسه حقوق معترضین رو رعایت نمیکنه و تا حالا ۶۰۰۰ نفر از معترضین رو بازداشت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151265" target="_blank">📅 15:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151264">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرگزاری دولتی سوریه: احمد الشرع برای دیدار با محمد بن سلمان وارد ریاض شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/151264" target="_blank">📅 15:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151263">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
قاتل فراری پس از ۱۹ سال دستگیر شد
🔴
مردی که سال ۱۳۸۶ در جریان درگیری در یک زمین کشاورزی در فشافویه، فردی را با شلیک گلوله به قتل رسانده و متواری شده بود، پس از ۱۹ سال شناسایی و دستگیر شد
🔴
براساس تحقیقات، ماجرا پس از ورود گوسفندان به زمین مقتول و اعتراض او آغاز شد. در جریان درگیری و تیراندازی، چوپان با سلاح شکاری به سمت صاحب زمین شلیک کرد که به مرگ او منجر شد.
🔴
کارآگاهان اداره دهم پلیس آگاهی تهران بزرگ پس از سال‌ها پیگیری، سرنخی از محل اختفای متهم در یکی از روستاهای اطراف مشهد به دست آوردند و او را در عملیاتی دستگیر کردند.
🔴
متهم برای ادامه تحقیقات در اختیار پلیس آگاهی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/151263" target="_blank">📅 15:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151262">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
وزیرخارجه روسیه: مذاکرات ایران و آمریکا به بن‌بست خورده و بعیده توافقی انجام بشه.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/151262" target="_blank">📅 15:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151261">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41d64143a.mp4?token=WHQE7uNGMUh_1JlxUK_GEf7TOL7bJmy3kYQVLPNyPtY433yZ6l8QH1H2U7_gRetBzh3rT6oZgM3VIIzenmme33Lr784jvs3mFwI_CblFEkIlQhxLRkFN8cEQ2rgQscFasQkHQ5TC43DaKkrXHo6ldSP7BlYRffZTUMOn-y6dMosX9WFUQ0GXBoXwug8Tbw8RYdytGcEz2GMVj7ZrGONF4g_VpdoflOiew2tYM8rJYKhUy4rcL4UPiXCbT--YNUT9hXJp8ol3_Op2gpyZIkLT_VIdmXkq7AMDGDmRnd-3WjjWIRCY8S1ia_qq3C6M0V_o7geF2g7Ao8KFxRkaEEjuY7YPcPREG-Q0ZK6Q4JWaCJCs7DlLNTGSOysLeUUU0kGVj9UCfM2dSRwOsI-ev8JjDO_qIoqaeJXWGcLbHZY1KVbg8Lu-LpGtElObzA6ZlSJ6yb3ZGSPRcLlRzyG-d0NTl70UptzU61KaSybvTTNi8Z8VIzDlwJYaUgXbzF-Yo07MciXTLy7OBiZhRYeEpEF27MogxjbMxkFEp3lxpCZoaeoF-Qm2EyZEM09adLQAYDXIQ6Sa5smhjp0CVgtJJ9Im2-p54ACw7QrssgEWIVXsvkEqnk3UlOaGwLbRjkUJAg-Y_uWZenHtn3nNAg45zueO_pYzLFXBt3-SkWw20qEcIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41d64143a.mp4?token=WHQE7uNGMUh_1JlxUK_GEf7TOL7bJmy3kYQVLPNyPtY433yZ6l8QH1H2U7_gRetBzh3rT6oZgM3VIIzenmme33Lr784jvs3mFwI_CblFEkIlQhxLRkFN8cEQ2rgQscFasQkHQ5TC43DaKkrXHo6ldSP7BlYRffZTUMOn-y6dMosX9WFUQ0GXBoXwug8Tbw8RYdytGcEz2GMVj7ZrGONF4g_VpdoflOiew2tYM8rJYKhUy4rcL4UPiXCbT--YNUT9hXJp8ol3_Op2gpyZIkLT_VIdmXkq7AMDGDmRnd-3WjjWIRCY8S1ia_qq3C6M0V_o7geF2g7Ao8KFxRkaEEjuY7YPcPREG-Q0ZK6Q4JWaCJCs7DlLNTGSOysLeUUU0kGVj9UCfM2dSRwOsI-ev8JjDO_qIoqaeJXWGcLbHZY1KVbg8Lu-LpGtElObzA6ZlSJ6yb3ZGSPRcLlRzyG-d0NTl70UptzU61KaSybvTTNi8Z8VIzDlwJYaUgXbzF-Yo07MciXTLy7OBiZhRYeEpEF27MogxjbMxkFEp3lxpCZoaeoF-Qm2EyZEM09adLQAYDXIQ6Sa5smhjp0CVgtJJ9Im2-p54ACw7QrssgEWIVXsvkEqnk3UlOaGwLbRjkUJAg-Y_uWZenHtn3nNAg45zueO_pYzLFXBt3-SkWw20qEcIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امانوئل مکرون، رئیس‌جمهور فرانسه، شاهد اولین آزمایش پرتاب موشک بالستیک جدید M51.3 از زیردریایی هسته‌ای "لو ویژیلانت" بود.
🔴
مکرون گفت این آزمایش، قابلیت اطمینان بازدارنده هسته‌ای فرانسه را نشان می‌دهد و افزود: "برای اینکه آزاد باشید، باید ترسناک باشید. و برای اینکه ترسناک باشید، باید قدرتمند باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/151261" target="_blank">📅 15:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151260">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
یدیعوت آحارونوت: از زمان حادثه فلای دبی، 7415 اسرائیلی از امارات به کشورشان بازگردانده شده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151260" target="_blank">📅 15:06 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
