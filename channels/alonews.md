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
<img src="https://cdn4.telesco.pe/file/Z5vcp_n5lZ7RwExGaDUUb4meZGTeh__6tifoF5qod44DicENwkVnm73wD9uFpuey7ZPFNkPQ_7P8JVUtlhCs0IIgPI9Drib2-2Rz5eYVTSytiwt-NwmmG6qmCfUZq3mjagMp0JI269gkz9TXmyCPh-Pyu17xQrjH93_vni8qmL4qa1QHcNdzHxLjEd5PDAUb2rFe-nZl8KI4gPkB1zDL6RgvFlq8zOwONNNlfJ69wUNlNwEDg1Xmd_nxhTlNAAJ5jUx0ll3n27a-gwsnn_rIuX8CwbCDBmbJICUvbWA0gzunMO_dDRw5ZsLnmGfCU1KuIT7IMjdqhmBEMsxCJIqgXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-152399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTURBO VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9oRsymSGQfdS8h2j92Csf43k4-zW37GvceuGTeqdhaRzDAYfnSbZCw0Xvk2poSPi5jMjWWtE-dDNnsrvoMZVkEcWgG0qDWdk5VSe8kecz6aXcGCvOpkaIo1EO3Ru9AeEXNC7Zc1JsrLgwo6Cm7Ygbh_sOpmn3SgSflHgrWA227Vtezi3PzFS-0TD-VL6lZXe3a-DM0BMFpA83WQu9sL-XFk_t6Y_wayaN7MSHHorbfGyrdAH2gu8H6WJyk4cbnCLAFzMAIbe5uzvQyydqoWVj69exQnznv2fllCFvTjE92ixrvC-MxRTX-4D3lBoe2fiHo27mgBM83fu2FsQP0cPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
🔥
قدرتمندترین سرور WireGuard ایران آماده شد!
🚀
در روزهای اختلال اینترنت، با تلاش
شبانه‌روزی
تیم فنی، سروری قدرتمند و پایدار براتون آماده کردیم!
🚀
🎮
مناسب گیم‌های آنلاین و شوتر مثل
Call of Duty و CS2
⚡
اتصال
سریع
،
پایدار
و
پینگ پایین
📈
مناسب
ترید
و بازارهای
مالی
❤️
ایده‌آل برای
اینستاگرام
و استفاده
روزمره
🌐
IP ثابت برای اتصال مطمئن‌تر
🛒
خرید از ربات:
@turbovpn_new_bot
👨🏻‍💻
پشتیبانی ۲۴ساعته:
@kasrazandi
.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/152399" target="_blank">📅 01:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر دفاع سابق آمریکا : هیچ راه آسانی برای خروج از درگیری‌ها در خاورمیانه وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/alonews/152398" target="_blank">📅 01:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKjrK7lYknHRYwaJGYcud6JFV5zmHd_qnh1xfamLExloeMS-8LvRzxoZ0k6Uaje2ti1HIfLf9DuJ3Xl0SiWjsNDrUNe30gNBd_UMiKKSuG4bSYdGCKEY20qF_Nqagg89zpbq-C6iyGrpEHT9A92yF1t4874SF3tkJ4v7pAPqwitQEZIfQh57kiBhutFZHJaFGY4Xz-uTenwf9fOgKusSt49LIc23eFVnOkZV01nLa-eoCI8zMxhYQxdf8ijFAGDcsFp-UV8E5rTODRhc3Jm3JXY-kX-GL8us4KRmxF8_CXPyyjNEFaXxYJjBK4J92k22tn9r8rbRIDqJ4TUkYhxC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم: به من چه بچه‌ام جاسوس بوده؟ مهم اینه توبه کرد و آزاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/152397" target="_blank">📅 01:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ترامپ: ممکن است با کیم جونگ اون دیدار کنم. این اتفاق هیجان‌انگیزی خواهد بود. من با او رابطه خوبی دارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/152396" target="_blank">📅 01:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152395">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-poll">
<h4>📊 شما به عنوان یک ایرانی از صنعت نصفه و نیمه اتمی خیری دیدید؟</h4>
<ul>
<li>✓ نه جز بدبختی چیزی نداشته چون هدف ساخت بمبه</li>
<li>✓ اره کلی برق و دارو تولید کردیم</li>
</ul>
</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/alonews/152395" target="_blank">📅 01:03 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152394">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e3835b1dc.mp4?token=f8s3o3QjhQ9jcDNzA7YaxzvfgGTLusAPMK2zMvFXtFykjiFelRIkOGct5A5LXOwSTww1OpgO_KKBf4n0v-nxpv1lJBM200jF5XBDcJecqM_pHb1TOWr6YiZ7SpSe5JL_csw9kwQjcJ6h7yVocN9BmMdbcWuUtnswFH-JTCfI3LOTylcbcWlBeYe3wGL-w_UQQjc9cGdjRnVaAUjCb5-3kiBqq6BSCBqWFYBeAHUvhlGjEInJUrpLgmIq6ehYARXyzf6nrI35o4XCDWFaMEw1NPI5z9dleUutSi1MsHNgoooZTLIsirMb_czOJs9yqDZ35vkyfeQap6ySKdnKAEyLTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e3835b1dc.mp4?token=f8s3o3QjhQ9jcDNzA7YaxzvfgGTLusAPMK2zMvFXtFykjiFelRIkOGct5A5LXOwSTww1OpgO_KKBf4n0v-nxpv1lJBM200jF5XBDcJecqM_pHb1TOWr6YiZ7SpSe5JL_csw9kwQjcJ6h7yVocN9BmMdbcWuUtnswFH-JTCfI3LOTylcbcWlBeYe3wGL-w_UQQjc9cGdjRnVaAUjCb5-3kiBqq6BSCBqWFYBeAHUvhlGjEInJUrpLgmIq6ehYARXyzf6nrI35o4XCDWFaMEw1NPI5z9dleUutSi1MsHNgoooZTLIsirMb_czOJs9yqDZ35vkyfeQap6ySKdnKAEyLTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
رفتار حوثی ها اصلا خوب نیست، حواسم هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/alonews/152394" target="_blank">📅 00:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152392">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">⚠️
دیدن این فیلم برای اشخاصی که توان غم زیاد رو ندارن توصیه نمیشه
🔴
اگه کمکی داشتید میتونید از طریق زیر انجام بدید
👇
Ir150130100000000405720701
5894638800062288
موسسه فرشتگان دانژه
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/152392" target="_blank">📅 00:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152391">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: جنگ با ایران به زودی پایان می‌یابد و قیمت بنزین در آن زمان کاهش می‌یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/152391" target="_blank">📅 00:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152390">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/152390" target="_blank">📅 00:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152389">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
اتاق جنگ اسرائیل: به مردم قول میدیم تا قبل 5 آبان حمله ای نمیکنیم ، مگه اینکه ایران حمله کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/152389" target="_blank">📅 00:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152387">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssnfY1jqXYaMgmf3qE-J0pIyCD-hU7lsZtvSIVMc5eONpqJuR6xcY8FEBpTr3vHz1-nzIW4TwlcxhiUuZ8Hd2ZSLRL5cB2QKo5nKQINMxoBunEA3e-KakB0c0yBis6qTk6hGX7Leekwflnx5B2ziQ7odOnlL5RYRHysTFp_BdkdyyvPnlBaS4hJOB-vmSTzLcWVZefzyp9dCi7Xu-Yv-IeoeaiP2DbIO0FZ2h_nFV91D2BhRTpGZ018VUjRSAZkSJHPTjsU4buSfAuOLgjbHzg9_usyS6UVfsvJPrAvCTooPPsXlWxrqs-t_usbJK-SYVsHhDdQLqiW7m8WXqDJ5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgPjintR1f2ccHaPeOQAdlMloDcZlf12mHnBxXH50b9wWY_1f3qv41yb0oJ-sacKxlfDBIgNd0J730OnIOAQ7s4KLQxEdsCcTUeEMNUiEjhFVqLKxZnV5dr9w_SG7MKzsxsytmSFsrhWha2Hunyf4sidHjbpUlo9868GDZYwkePaGSiH91-DCPAPnLPP5YzmqcEI2ecXQKc_m-RU61rsWtDKzUBQExFxCC4k8QJd-uXbrtVO7Ya4N22qF5xZAwgsqex6_YYBYXAXU5Yi3ZIIeSZIQF7Ke_lMUc_xJYL061dg4trqyTqWn321yR7ffmfvrUmrlGGQqsXbTBWRwVn0CQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
بازیگر سریال "بریکینگ بد"، آر.جی. میته، که بیشتر به خاطر نقش والتر وایت جونیور شناخته می‌شد، در تاریخ ۱۲ اکتبر در ایالت تگزاس در سن ۳۴ سالگی درگذشت
🔴
به گزارش‌ها، او به زندگی خود پایان داد و مقامات اعلام کردند که تحقیقات در مورد این حادثه همچنان ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/152387" target="_blank">📅 00:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152386">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCN5yJ-GJag8sl6-l16ZdKldlhOOjt4Y2Lfco8FG6jGrmV5mDAwUVZJuvKFh5igtEg9H0satmORw_-LSVC45EOFWQvXZJ_PxDAa49BtLuvb_6tiRjfCQpDoc3cbr6LdBbOObrMnwS4xH1eti7RQtq_uKI-wYs7jP9sQ4pYtq0X201CQq_E33ANNbPvRizwB2SBgR82o5vMap79tgD2I9irAzwxLw5-yjQ08hC9iFuUl1wKJ7gDEUpxk7UiuGpIBm1ktTEIFNFGEphszMGU8qc4P0QD4_Pl7O6fYnHoml96AQ97WfeayyEiZJX_Uao9HaxOkzZ-kEW2LdXJF7kbXZyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهرنیا:
آمریکا در نهایت ایران رو درستش میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/152386" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152384">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfmN0CVpvzp_h65NCzlFOzcoUn-u5We4oBk7Q8VBR0YHrbKlRVT6VeOAUlA_qWmiV0ay6RVG2qdRh7GFynPeY97folDffX7sLJIeHjF0_-Bf37ISlFJW_uhO4rglovbmmBQpI_AVcTOHdyeQEUqVX6pDMnxiPhKp7fnAp8mfSJtzvchw_YYmsF0Zs07MMUFQ-2poJ6aZIDV6VBtBss0pGtdq3oE_rZd_Wj0r-en_veX2tLaN2PCxGoL-dFFDF1XJFtOzcafvoRx18gXTbr7irR7_66x-GFgNYWdkRH2FC1vO-EfsdoW3SWQs7oNf_mBksyZ5TF1S3YDyxy8hdgcOwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2zwInt2RHheGNpEpSZkYBZ_nRypzYiafMH_ix04_9f5YiXWhoBSBiyMDb6vv1cQRVB1VbsAbtQMxMAJuglT6rW0dt9IbFmsg0QBYqmpZrWvfPQX4LC-SydQWjeajBxOxdeujjfjpQD16wBZ6sJz33lym3CvTTo5kIj3dCkD9R0lpLmezbjrb23ytZLsP5RA_FnqIxbcRk7pG8UYLjW6satIzpITNwOBwv7vriOTdgJNDbPLpbNf-Qo9o4MYoQc28RfGkALlNCw1IJ4YGWvc6jWUAFT0Myw27K1IzCZYOkSLzc6U8wiHK2gXeMG_2jEuUy-k22cMXlli7RAmqgqz9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ادامه تعليق پذیرش پروازها در تعدادی از فرودگاه‌های عربستان سعودی:
🔴
نجران و جازان: بیش از 155 ساعت
🔴
ریاض: حدود 57 ساعت
🔴
ینبع: بیش از 28 ساعت
🔴
عرعر: حدود 15 ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/152384" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152383">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
بارزانی، رئیس اقلیم کردستان: تو جنگ نزاشتیم از خاک ما ایرانو بزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/152383" target="_blank">📅 00:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152382">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQtxci6e-_eNmta2b3nb46jfjtuJ9jP7hTc7CUB6PgGW2tolvJj05ytPGT7MmtWD8IpISypTa9tpct8PkLXV1umznKbCgwblAI8JOOzynx5oCfveCOnaOA7zw2etC7SwkHRCi4HM0_kyRrMTiDXOpFdAvmJoRkfnIkurJeAl5omdqcEB5sILUf7QP6HGZnCzN97gC5yauxxhf2cHUe2C_u6F4X79xjIljQuyGKuAT-0bPrYMxnciK-IKD5WwLXcFfFMUboDsjPUusbTB8gfjmt4zsNc85cClESMehvARHJHRqn41tuQQ7n9U_STNI5ZPdns6UOZsQEZ17iJUQcieKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازار ارزهای دیجیتال خبر از جنگ میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/152382" target="_blank">📅 23:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152381">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هاآرتص: نتانیاهو به عربستان گفته اگه باهامون داداشی میشی میام براتون حوثی‌ها رو کلا شخم میزنیم ولی بن‌سلمان فعلا مخالفت کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/152381" target="_blank">📅 23:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152380">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">جدال تیم‌های میان رده ایران و قطر با پیروزی ۲بر۱ تیم ایرانی تمام شد
@AloSport</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/152380" target="_blank">📅 23:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152379">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw9CiFUvoutv9Ds7aPY0TpL_iBoEsBcHWUE3TZh5be1VblQrynD9kDpASxfLMNz6z6B7eOAn43e-vP1OkLqiHEl1KLWGhdSuqx0MbFvcGHht40v9OzeSgtky2w8tU7RmsR0ttVhi0QVRJLMst1ddUv0Ue5-lSDd6qdcE0auqsxxucuz9deoRtX9H73uxGxwjdkpD1ZqZ1fAdwYVaqnoZuOGZ0wrr8q7ok3Tw2WdoA8dytPUnETF537MzLCXRDstf9SoUM3jeCIDqUzXjNXLxOMr2F37jIBCjqlJ7rF6LcGawjewXOxDVRCJj0yBHZ7qaS3mUNMaBIenEXURW94MlHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه جده دوباره متوقف شده است و حدود 5 هواپیما در حال حاضر در آسمان معلق هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/152379" target="_blank">📅 23:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152378">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
هم اکنون قدرتنمایی جنگنده‌های ایرانی در آسمان کرمانشاه، در غرب ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/152378" target="_blank">📅 23:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152377">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وضعیت اینترنت کشور ۷۰درصد افت داشته چون احتمال شروع جنگ خیلیه
‼️
🔴
اگه سرویس متصل و پایدار حتی تو قطعی میخواهید سریع تهیه کنید
👇
https://t.me/voxnet_bot
https://t.me/voxnet_bot
با پول یه پفک اینترنتت رو بیمه کن
✔️</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/152377" target="_blank">📅 23:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152376">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
عحیب اما واقعی
‼️
🔴
ایران اعلام کرده آماده میانجی گری هست و عربستان قبول کرده اما یمن قبول نکرده
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/152376" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
منابع خبری از شنیده شدن صدای انفجار در شهر ریاض پایتخت عربستان خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/152375" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عراقچی: وزارت خارجه استفاده از ظرفیت‌های دیپلماسی را برای تأمین منافع ملی با جدیت دنبال می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/152374" target="_blank">📅 23:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152371">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5bOZghN3g9ZMnIO_D2aIJsQZRVlJ01p5XZo80SSrok-KI9F2XyXQNr2XbraKapWuzNIeeW8LIYg41ovC93pbozcwApLvRsgPbd1Kb_NHO8XIygC0VkD7uzvvsbNfY9vjOaSeukvrt-6pxBvtPVQBfc0vuSdZ_dtbdwWeBV1aGaFE3qtt59yxjxs3YcLuiZKzghw0BFVfxa7gBUkHgntAi1S7FVS_ysR48cWCr7RAsjaJKNji_9UfxOXj2Ukxnpwj5ukjsykBNnpiUlLswQFMznZdHb_Sq9PRYNAagV7OWiabDtTXTn-Gq3Wc56A7Q00ZYHABoNT32pvemRrn7WUJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BG4Gr2-b0sokVE06MxIoswyY3NIi8mory0jdtdzAOhhFYusEiAsN-GbQhaVoOWkAbru2iEhlh_2TyKcUP7iuNyQLhbJ-lDTZf-lgeIa46UU6uzsZE05lg37odWLJUAS1NqxpdAGeGBXPS5wCTef7TzlMgi0eW4jXBuiQfdWHXDQuUJLSe5P1cLlMFMewCOn3ewbB7EVY9gTOpmZ_imkjPI2P4ppjfSO1cFYP-eBGWetIf2YMSc4uX-iYIg4A-EYU3PVc12WgiOow_yOXHujlftOAZpJ-qDvjJV8vGU9fl-YLle4p2LD_zXYaueMXAnN90NgXGukP08QspwIcX4GDkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CiyXwbLCzD6tziQkLrcV7N7y8gGUmNUf1aL5g7_YgV1JAU-jWxwoXWf_sO-TMNyf4s9aK5O8VCshQXnH8M2YsBts95LzrmXMJEyTgioHH6xj0g_jV87d-4atXqmKAylbMHTjzpofOmC13E3eX2u6KzsKqmhgGDY1nPAVz2fK1Ydn4E5d-Jb3nvD98AITtdsViikhov2frnHin7YIwv_tkzYUHAw1tam22_UA1kbQqM7DiKvQ7HZg6TmWg6c3BC4DADiy-ra3bjyvXExsI3qmRfP7BggV6kE3E1YVqilwNSFp0Qzms8jsLeEqy4TWDi2zUuJgIutK1FOTNss5yL9MZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حدیث ستاری، دختر ۲۵ ساله ایرانی، به عنوان زیباترین زن سال ۲۰۲۶ در خاورمیانه انتخاب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/152371" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152370">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!  @AloSport</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152370" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152369">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔵
سوپر گل دوم تیم دوم تهران به غرافه   @AloSport</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/152369" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152368">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puNvx0kuThSWzWr2FNHWGCX9QOn_yA4DNoAhGbnbTP9PVjzvxj0WmSdGvcdjjhxMRtmJ8aKvUKI0yXulgtRWKvbjFWECU7bmPuYE4_Pxb-aZmGfJ0H024yCyQMlhqqjpbSTD6Bjm5GB0CgUVldCoFBLFphFXjyFjjg004asZVGs_knAly-xKGtVvWdaShLISXBuweuuHMhBWTSEWl-dQUXQg6nnWC790FhEP5qX0puumyY1nNk3LD0xRLorWVPvU0tUF3l5QBVjFZ7CRpiqupSiGhqAZd28YUk86FDPdw0UT8pl5fxug-h7uOwSB2Sto7m8t88k7Kl53GF_6w0R6lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اثر پرفشار جنب‌حاره‌ای روی ایران، روزهای پیش رو هوا گرم‌تر از معمول می‌شه. دمای تهران به ۳۰ درجه می‌رسه که حدوداً ۱۰ درجه بالاتر از میانگین این فصل میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/152368" target="_blank">📅 23:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152367">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: نفتالی بنت در رقابت با نتانیاهو برای نخست‌وزیری پیشتاز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/152367" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152366">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری / ایران برای میانجی‌گری میان عربستان و حوثی‌ها اعلام آمادگی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/152366" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152365">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01481363bb.mp4?token=LmEYZWVMjFPO7MTdo4jue4WUKttrt8h5nx0wQjfSNxUQJ1i3gyY7qEkHhp2WFbKjwqVWkWO8wPNOlhaoZeA42kP-8LZZbW9uClExxNb92mIv2LHK04hCN0urYRymwv4N25q7jO5jGAQXX3cpoqlWPHN6Na4_X4fh2SGgRbCGxJWTHoZCSXqX9sBPTuAStClODC7_Ydn_IjRInFZUFjOjqM_W9QWFgGkrGgXdYrH-thLc6XiynRV3RjDX1WY7_6tz8Za65kWw5X7J0WmVwepo08Cg5uUA5STma58sW72eRuL5gcpC85_R20bsercPcb4gzPLEnCsFUwF3BP6m0zdhIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01481363bb.mp4?token=LmEYZWVMjFPO7MTdo4jue4WUKttrt8h5nx0wQjfSNxUQJ1i3gyY7qEkHhp2WFbKjwqVWkWO8wPNOlhaoZeA42kP-8LZZbW9uClExxNb92mIv2LHK04hCN0urYRymwv4N25q7jO5jGAQXX3cpoqlWPHN6Na4_X4fh2SGgRbCGxJWTHoZCSXqX9sBPTuAStClODC7_Ydn_IjRInFZUFjOjqM_W9QWFgGkrGgXdYrH-thLc6XiynRV3RjDX1WY7_6tz8Za65kWw5X7J0WmVwepo08Cg5uUA5STma58sW72eRuL5gcpC85_R20bsercPcb4gzPLEnCsFUwF3BP6m0zdhIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار امشب تجمعات: ظریف یا جاسوسه یا نفهمه، ظریف بگید که روحانی نفهمه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/152365" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152364">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
شرکت هواپیمایی دلتا راه‌اندازی پرواز مستقیم برنامه‌ریزی‌شده میان آتلانتا و ریاض را تا مارس ۲۰۲۷ به تعویق انداخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/152364" target="_blank">📅 22:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152363">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc14f87f27.mp4?token=u-IkBKppv6Y4geuq3s0k794MjSLcdKnhcRaz4I_bmItlYSBIhupOdJ315vec-FM1xzLshWgXdQaqkAOrjIh5YxrwfH6Hq1wUnAcbI3sfjgVyI0N9euhy9Btl3y-yth1tZnD3hdb8kbvRL8Lg3S1z3jfFAIOEIIDy5l_B9v_X5D86MvZIB9SIJ-pmRQ8baA-g83QvlEDmuVZOj9SrSyKQAqUG8UsJcQ26wwD8red0aVAoiPcfFUhOYoNRwKlZLULF2wWhGJJDTMI9cfMarMxX5xVjzm8NmmfRC2d3xPVSCdNciOR0WhVBj-kFFg7wLpXNjhuQH-CGSyc2vK6tqE7dbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc14f87f27.mp4?token=u-IkBKppv6Y4geuq3s0k794MjSLcdKnhcRaz4I_bmItlYSBIhupOdJ315vec-FM1xzLshWgXdQaqkAOrjIh5YxrwfH6Hq1wUnAcbI3sfjgVyI0N9euhy9Btl3y-yth1tZnD3hdb8kbvRL8Lg3S1z3jfFAIOEIIDy5l_B9v_X5D86MvZIB9SIJ-pmRQ8baA-g83QvlEDmuVZOj9SrSyKQAqUG8UsJcQ26wwD8red0aVAoiPcfFUhOYoNRwKlZLULF2wWhGJJDTMI9cfMarMxX5xVjzm8NmmfRC2d3xPVSCdNciOR0WhVBj-kFFg7wLpXNjhuQH-CGSyc2vK6tqE7dbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت شهر ریاض هم اکنون
🔴
فعال شدن سپر دفاعی و آژیرهای هشدار در ریاض در پی حمله موشکی حوثی ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/152363" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152362">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
👇
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/152362" target="_blank">📅 22:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152361">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1812bda590.mp4?token=bHRvhEX4ysnequpXpuKPIXacBNDgs4XnacBr3vNu9LCJ01XbWMvoLb9xb2pI76-2jM7Warmiw_gyIOwkh9Msxa5INwmoRli4DzUMZDb-lEQBLv9rSCi2pnIr22aZjQAQKmlHqD8to6a0ogM_5Xsj2Kp9P63psKlmsLwKnT91wMBycOY5D4oT1v2O0cR6ZBYuTyjcd9tGmz740GXyOuywmfx_UxO7eoZ95Juh1ktBwIXfXDln9WafwKOLzCUk6LUnFKxwTMRJ3B7l_rNK_FEOwi8CENnEMzDHabQK6qjPywWH2B469yuu_ISfmVPDeW-t5xZ3QzXKeXt4Sw8haaySxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1812bda590.mp4?token=bHRvhEX4ysnequpXpuKPIXacBNDgs4XnacBr3vNu9LCJ01XbWMvoLb9xb2pI76-2jM7Warmiw_gyIOwkh9Msxa5INwmoRli4DzUMZDb-lEQBLv9rSCi2pnIr22aZjQAQKmlHqD8to6a0ogM_5Xsj2Kp9P63psKlmsLwKnT91wMBycOY5D4oT1v2O0cR6ZBYuTyjcd9tGmz740GXyOuywmfx_UxO7eoZ95Juh1ktBwIXfXDln9WafwKOLzCUk6LUnFKxwTMRJ3B7l_rNK_FEOwi8CENnEMzDHabQK6qjPywWH2B469yuu_ISfmVPDeW-t5xZ3QzXKeXt4Sw8haaySxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🔵
گل اول تیم دوم تهران به غرافه
@AloSport</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/152361" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152359">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/رونالدو برای امنیتش به مکان نامعلومی منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/152359" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!  @AloSport</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/152358" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2514cbb0e.mp4?token=sTIuxZEBWwArUVghgk9Ctyw72z69WIy-TJ4UQPHt4sb7TGyKOzox4kfa8AuQXXP8XBLMFROkUJ3hh-n51C6gOLPCvkELDEhx27-7iWhZG9v0Mca-Av_RhvM9uh_VkmWxv0JEq3fG8JE2hgnP_Ui8TBFN59zcxov9GQzcc5bUSrZOwK1dClw88spniJuKhxKB2XZbQAEDXfO1tPXXKrvZmdSphKwnhbxKOdawOwq5EptPHzq8okDIdoRPtUmrWcjmHSyjqyOCxNcvSXtyRuzC0XmNVNqoTD7nTZ7hVCKOh0ccKPQt55m5kUlLasfUfeR0O4XtTUIkwgpyCfMyPmh9IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2514cbb0e.mp4?token=sTIuxZEBWwArUVghgk9Ctyw72z69WIy-TJ4UQPHt4sb7TGyKOzox4kfa8AuQXXP8XBLMFROkUJ3hh-n51C6gOLPCvkELDEhx27-7iWhZG9v0Mca-Av_RhvM9uh_VkmWxv0JEq3fG8JE2hgnP_Ui8TBFN59zcxov9GQzcc5bUSrZOwK1dClw88spniJuKhxKB2XZbQAEDXfO1tPXXKrvZmdSphKwnhbxKOdawOwq5EptPHzq8okDIdoRPtUmrWcjmHSyjqyOCxNcvSXtyRuzC0XmNVNqoTD7nTZ7hVCKOh0ccKPQt55m5kUlLasfUfeR0O4XtTUIkwgpyCfMyPmh9IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‌آتش‌سوزی‌های گسترده در ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/152357" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=Sy7fm7-Fly428oTwjCC7ydV0J9AkgTQXCGw5WUGS9f_KZdCZJ9g6LrXTKTzhz85XtUtsYELOQiNzuT6wRBr75Et2yE_5CZtd1-4iQV8Rl3PbB6Uq75fqsSVB026I1CFo9b2joVej4_ASc1_YhbmXtAzV_4dGgBOg93jokPjG4npLRxoDIC_7khedI6kE9KRZnv_LHvze0LQ1EmDp0O55L3e_gPnIjSOOK0OCYWaiwoVzvRIMG_gAIV8Nwa4FRDIawalw-bhtMzoJkbRG9FvFYEoPOwsDpH4PQcR7IAiSZKrNNaittM8T02h7CGB06cRcXfILj75Mf22aMpvxtU4-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=Sy7fm7-Fly428oTwjCC7ydV0J9AkgTQXCGw5WUGS9f_KZdCZJ9g6LrXTKTzhz85XtUtsYELOQiNzuT6wRBr75Et2yE_5CZtd1-4iQV8Rl3PbB6Uq75fqsSVB026I1CFo9b2joVej4_ASc1_YhbmXtAzV_4dGgBOg93jokPjG4npLRxoDIC_7khedI6kE9KRZnv_LHvze0LQ1EmDp0O55L3e_gPnIjSOOK0OCYWaiwoVzvRIMG_gAIV8Nwa4FRDIawalw-bhtMzoJkbRG9FvFYEoPOwsDpH4PQcR7IAiSZKrNNaittM8T02h7CGB06cRcXfILj75Mf22aMpvxtU4-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏
بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
@AloSport</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/152356" target="_blank">📅 22:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
دقایقی پیش، دو هواپیمای باری نظامی آمریکایی به امارات و کویت رسیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/152355" target="_blank">📅 22:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گزارشات از حمله به یک کشتی دیگر در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/152354" target="_blank">📅 22:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
غریب‌آبادی: پاسخ ایران به ملاحظات آمریکا درباره پیشنهاد طرح آتش‌بس هفت‌روزه همچنان در دست بررسی است؛ پس از تکمیل رایزنی‌ها، موضع نهایی را از طریق میانجی‌ها منتقل خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/152353" target="_blank">📅 21:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
حملات جدید حوثی های یمن به ریاض پایتخت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/152352" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152351">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
حملات جدید حوثی های یمن به ریاض پایتخت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/152351" target="_blank">📅 21:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152350">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fp_gSz907vzgvm9Nql8NLhm7gkORn1Jc17MVI1wl5aCIRxMHGSMlETaHJryKWBP9sMU8p8kdnqpYupZoLjcWtnL52yuyU0fxPty-bJLRB3HowxJAu5wkX2FPQ30lEpwCmOceuCj7OHs5z-c2EprgMPy-j-jItjto1bYzb5Kmo-Zywr7ShutSk7EIK79ojlg0uIv07MkSquzd-R8Gnc3qr_SpQof-BFrEIgGWKH8X7UYDpXvDp1DJdj4A3KjkiRZPSKwSvH80G11fXHRhoXvfGSIjYwldKk4zRRjoo4SB8x-rxVfZ84wLymye89r7wjM2xWEOTTwDcOIk_x7AezKLxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ابرنفتکش‌هایی که می‌خواستند به فجیره بروند، منصرف شدند
🔴
۱۰ ابرنفتکش که در حال نزدیک شدن به بندر فجیره بودند، اخیراً مسیر خود را متوقف یا تغییر داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/152350" target="_blank">📅 21:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152349">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
هاآرتص به نقل از یک منبع دیپلماتیک گزارش داد که عربستان سعودی درخواست اسرائیل را که از طریق ایالات متحده برای مداخله نظامی علیه حوثی ها ارسال شده بود، رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/152349" target="_blank">📅 21:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152348">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه اینجا رو بخون تا از بازار جا نمونی
👇
👇
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/152348" target="_blank">📅 21:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152347">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbXYjXqQOornt1OM4SklHzJAuqVmxYbzEwNHIIHDJUbigQHKg9xZEpLt2EEU6ICi9XqMQ8A3fwYLcU6wanLpCUxVKusGrNmTKys0PNF_UqbNjbJkDdv-VOBYWkxXlZNsVB6LdvadjSD2Q6a_wDS4nK1uIsaBwOewDgyWKupMixUE5gvmSH1-4xB3NYsP4xny7iV9Nn7y4N79BaQ6lPH_Gsl7yDjfFb01ODEAbQRuoquBo_ptZ-Un5r9S-EAWKHhGtBUUCi5Cabni-w-b45Da3B8H3Km6PSINcQZeMIyH6hrxl4dQyxDeKd0fpQbEz-sGdc5i1zACXpE0slWxzRlAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فروش تابلوی عجیب آرزوها در خیابان انقلاب تهران
🔴
دلار و آیفون، شمس طلا،  پاسپورت آمریکا و کوکائین و شیشه! هفت و نیم میلیون تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/152347" target="_blank">📅 21:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152346">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
۶۰ کشور طی بیانیه‌ای مشترک اعلام کردند متعهد به آزادی کشتیرانی در تنگه هرمز و مخالف با وضع عوارض بر کشتی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/152346" target="_blank">📅 20:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152345">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رویترز: حملات مداوم از یمن به فرودگاه ریاض، حریم هوایی پایتخت عربستان را از هرگونه تردد هوایی خالی کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/152345" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
حملات متداوم ارتش اسرائیل (IDF) به جنوب لبنان مواضع حزب‌الله
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/152344" target="_blank">📅 20:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سخنگوی شهرداری تهران: تمامی درختانی که در پارک جنگلی چیتگر قطع شدند، آفت‌زده بودند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/152343" target="_blank">📅 20:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
الهام علی‌اف رسما حجاب رو تو مدارس ممنوع اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/152342" target="_blank">📅 20:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdBNzBxKtjmmD5GnktaRB4z71_ZUmGGyO9bfEVnNi7P2crEZ0UYTsjqzdT5no3krsBMJ8DsMR4MENSDEgqtdt2QLyBJPGp__UNPUJzI1RjFIyDUqPkqHtCOZoOJ7r6SoIOZR0_6fkl9KynUjOKhUJhYoHZcXUPlHLlOtgomowMiT0RlvmPtRdS2NmW_NAVlGYeArrSj9RpLs3UQToyvsfrOWx6eDZ8hpGyFKAb1MENWWX8UKrsIKExbTVRXg9i2jb4tMQcS5A_bOZnJussCCfEoKOYImUvxWpARoK0JiVTBHY-gCHc6oKoO78qg9gwIh2r1T1rCbWwCmYifC2wdzdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر کشور با الهام علی اف دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/152341" target="_blank">📅 20:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یائیر لاپید، رهبر اپوزیسیون اسرائیل در گفت‌وگو با یک رادیو اسرائیلی اعلام کرد که بر اساس اطلاعات در اختیارش، انتظار ندارد پیش از انتخابات اسرائیل جنگ جدیدی با ایران آغاز شود؛ بااین‌حال، وقوع چنین جنگی را کاملاً منتفی ندانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/152340" target="_blank">📅 19:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152339">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X17W4G7tgDxYmbj_54d_uh-_ALd3ygG74go4IWIXzYzXOQM0vTFIFsU5GK2wQXuY_-dbrLw9SJV4WLMfEHt4nxdNDx1PENvdEBhxB095AOoXXRJvnqzFz-L4kqHh2s4YEp8aOTSicfMkW-FczvZ4RmkKf3f4Bqniua3oz8ktg7oBAnjeRco7E5BkROofiTYKCEbWjHO7DW0V6bBSy_3EJfu31S63Tapj6sKIuaUM_FEFicL48tPHQEJfhckQADqtlbqeoEql6kP5RakUq4ne6z0zbLk4dB8Vxm-naX-deO0Nbh2XUOAKeLPiliWkHfxByruwwheNlEfBL5uF-J27Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید کاخ سفید
🔴
امریکا به سوی پیروزی می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/152339" target="_blank">📅 19:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152338">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ولودیمیر زلنسکی، رئیس جمهور اوکراین:
اگر ترامپ می‌خواهد  رئیس  جمهور  را در اوکراین تغییر دهد، باید بداند که فقط مردم ما می‌توانند رهبر را تغییر دهند.
🔴
من واقعاً برای انتخابات آماده‌ام. ما به دستکم۶۰ روز برای امنیت زیرساخت‌ها نیاز داریم تا انتخابات را آماده کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/152338" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152337">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCyfHOfNhmECGlkmT9cL5rTKkdEQ2ISygtldNWMJx7CWn-mjv47sGfTNuAW-arS6LyY_VcUYZlSF4m11GjtjCc-TSg8yWn62A6rkIlI5rjj_tYRtMEhzkP74H39xnt6G9OQAJvQfwxQKBIAEthEIik_IbVD5HcU4Ee4oKzS1axd3Lu9akBjDlrTEFTkLVBn2jsp3A0nb8-1HECLSXZ7j2E7e72Qe5WnLnTTAE1pRpnfSbnmUOcSE41MyfCQGNPe0x9Z2B5BaEy4p5tu7lZPAoT1pTzeHn3v68Qp0uHdXLCmOpasf8GTZIci7Z5IqSu0zv3nJJnyhD-jcac_jLKIp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تهران، خیابان ویلا، سال ۱۳۵۷...
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/152337" target="_blank">📅 19:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152336">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVc9b2HDwV27-mSPxZ4Q8LAG-ZcyJUYX48XucIvurKrJR8RXaAi2wd6v0KfHkomjlhFWfI__WgN3J12yE9pvTo7KlyWOudKzU9Q0e9uvfbGxsvZ5cFtrJv7aZCwIk16RJVHayAqre0RRDhbZQtGJ8Rbo5iII8EmMML-SWk6X3dgJbdIYV0ZRAYrYnTB_z3rTljghkqNd8y4JuoyXf4jjT4qLpReKlqNmzxG96enCkAzDAYW9lTMG7R_9LxIH-DuciRMSG2n8q4Ygw8RCpNDBN6fqOhmz-B-S9yuOxY_C_BhWWl3dFgv9Vc3hGd395bBfxKaUCZU9eXy6_P-fTABfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی با تأخیر دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز به سمت خارج از آن، هدف اصابت یک پرتابه قرار گرفته است.
🔴
بر اساس این گزارش، خدمه نفتکش در سلامت هستند، اما هنوز مشخص نیست که این حادثه چه پیامدهای زیست‌محیطی به دنبال داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/152336" target="_blank">📅 19:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152335">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVoX NET | وکس نت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDllzabb775xTZBC5e9VIIvbWZDimdCBxNDg4-1wCvB7DY-h8QnabPR0rJdOMoMRjcWV3B5aYsm0yEjXxi4SY9qPHyDqxpKlcLlK8xXVfPQTAQ4widvklntYrT48ztL4PnD5jZ71HuLzBAFrW3IDCC5XKUncVDjvzZymddBam4kZ253Xoqj1IK2xg5WpBqfU_mhOWxE_qmMEb4wbWcbtFX1KdtCNwEh1XpY9i8rAcTWoA67NRGTZZcZLU5iKgrA1Tow-Ike_X4aVv-TdLSHDxhI0zFshQGUKBC2YgBiK4Xi24cEzeOFZ6vrZFj6v_yUpt_yJ0a30bVqfPO2CgLklGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینگ کانفیگ های اقتصادی
🔥
برای خرید از بات زیر اقدام کنید
👇
☝️
@VOXNET_BOT</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/152335" target="_blank">📅 19:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152334">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هشدار امنیتی دوباره سفارت آمریکا در ریاض
🔴
کارکنان دولت آمریکا شاغل در عربستان، برای استفاده از هر فرودگاهی در عربستان سعودی به مجوز ویژه نیاز دارند.
🔴
شهروندان آمریکا باید از احتمال لغو پروازها، بسته شدن حریم هوایی، و اختلالات سفر آگاه باشند.
🔴
توصیه می‌کنیم وضعیت خروج پرواز خود را مستقیماً با شرکت هواپیمایی و فرودگاه بررسی کنید.
🔴
لطفاً اگر تصمیم به استفاده از فرودگاه‌های عربستان سعودی گرفتید، احتیاط شدید را رعایت کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/152334" target="_blank">📅 19:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152333">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
گاردین: پس از دیدار مقامات آمریکایی با یمنی‌ها و اطمینان از اینکه کشتی‌های آمریکا هدف حمله قرار نمی‌گیرند، واشنگتن از حمایت نظامی از عربستان خودداری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/152333" target="_blank">📅 19:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152332">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayAUBsaZ2G3UD_IX4QD5dxlvcPLBtdT4RrblI4_-wiZwokhjFqd7qgyEI4U2GFXkmubYPf2hN0PswgpupjIUk8XlAXOfVqrDSXLAlkMnK0YQQKcPQL0XJp_6-gTpK0_6HdNMaHthzwQ-JwewvkdFUnsa466W9QdNNzuUUNt8ufrFEk2Rm6DwPaKjJKGp7Gu4DZ4vYz5LR6LyyrEPC8E9GAvQJDHq3mM6DLUV8vFlxAgDa7o-ZZEr3cjoAK292A7v8XlY86ATcbyQCmuzEuoJnZmu3Gnwsw9lwlFs1PFbnUsr1r3fZGqMKhc5TtNmuRCAjvKpkBMcXRvZxdtORNFIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون اصل نود: زمستان سختی در پیش داریم
#کارما
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/152332" target="_blank">📅 19:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152331">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc547ce9c1.mp4?token=MavpXifFbFfGZaJ8tJdJ1sVUOMqxnDB5U8H1eO_gw4XcfksJJkbEtsHbAoWNR-3mRBPsFuf6-hA1bkVaPiBV8MMddSmTgTD3GDDXEAzTEqWoGn4l-1cU4rxByNlzNeIf-KDdxXgDQI6z5doa_yfNcqxkUdIiGy4TLkuQlbZicTrdG40pEeVCxIuSnxT7b5nLmIce-2vyMMSuVv0ooBgAr-CI8v87gVVCsYJOEhJs5LIfZUOaZtckRNQp1f8t2irAEhYY5iriciM6YmvOCYl4NKTaNHRrQ5J87LRnGDtMkp-V82nHxcNDaTdT6nzrYiJdmquTtccCrbqRrhLuLPoXrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc547ce9c1.mp4?token=MavpXifFbFfGZaJ8tJdJ1sVUOMqxnDB5U8H1eO_gw4XcfksJJkbEtsHbAoWNR-3mRBPsFuf6-hA1bkVaPiBV8MMddSmTgTD3GDDXEAzTEqWoGn4l-1cU4rxByNlzNeIf-KDdxXgDQI6z5doa_yfNcqxkUdIiGy4TLkuQlbZicTrdG40pEeVCxIuSnxT7b5nLmIce-2vyMMSuVv0ooBgAr-CI8v87gVVCsYJOEhJs5LIfZUOaZtckRNQp1f8t2irAEhYY5iriciM6YmvOCYl4NKTaNHRrQ5J87LRnGDtMkp-V82nHxcNDaTdT6nzrYiJdmquTtccCrbqRrhLuLPoXrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه هموطن سیم‌کشی ضبط ماشینش مشکل پیدا کرده و تصمیم میگیره خودش دست به کار بشه که در نهایت اختراعی ثبت می‌کنه که توی دنیا، شبیهش وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/152331" target="_blank">📅 19:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152330">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: تلاش برای حمله به فیرفورد احتمالاً در ایران و به‌طور مستقیم از سوی سپاه پاسداران هماهنگ شده بود. پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/152330" target="_blank">📅 19:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152329">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: تلاش برای حمله به فیرفورد احتمالاً در ایران و به‌طور مستقیم از سوی سپاه پاسداران هماهنگ شده بود. پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/152329" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152328">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Buir2s5gkyAq4csHGfAH8yzp7gVw14j_DaEq2wf0Q3laxaEITE51NL-HS54NRrVb2tkLD0Se14adV2DyW1MdaleY-NpGqYOoeNaRc6kDRkVZ7P7JykBrdRiGjWZ-8yC3gm1vhqDb0z-aKiSB2lnQ1V_YejbLrjM3tiTmQ3FobNkPKbKh1AgZeU-ROTJlrR3phDwbRkxw4A7BsYcK6nQ1YOKjIyVHXNBG3npZXJlhvehQbhkUn9OChVA1kVO3j0ED7q_LbDBnQsrImRHQzaLCfx037XX4K5BFcCAjtojSi8FowaZ-1eUoiTuKU9mRl_xANuF6dv8RoHh2H9e4hH1PFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الهام علی‌اف حجاب را در مدارس جمهوری آذربایجان ممنوع اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/152328" target="_blank">📅 19:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152327">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
اندی برنهام: ما در کنار عربستان سعودی در برابر حوثی ها خواهیم ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/152327" target="_blank">📅 19:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152326">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
۲۹ کشور ایران را عامل حادثه پایگاه فیرفورد خواندند
🔴
۲۹ کشور از جمله آمریکا و انگلیس تو بیانیه‌ای مشترک ایران رو در حادثه پایگاه فیرفورد متهم کردن. این بیانیه بدون اشاره به جزئیات، تهران رو مسئول دونسته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/152326" target="_blank">📅 18:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152325">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وضعیت اینترنت کشور ۷۰درصد افت داشته چون احتمال شروع جنگ خیلیه
‼️
🔴
اگه سرویس متصل و پایدار حتی تو قطعی میخواهید سریع تهیه کنید
👇
https://t.me/voxnet_bot
https://t.me/voxnet_bot
با پول یه پفک اینترنتت رو بیمه کن
✔️</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/152325" target="_blank">📅 18:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152324">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1rqZ-bds4x1Lz-5sPnjkkMQd4lVovaDlQVHEEV-B3gsVoY8zUqcFXahhI9Z4Aa4Ha2bAHXWewNJ7pCfJzBAx_zSL_g3fL4ewyb9KmhZHLpbb8d1nmjqkOtPn1iCQ12QrV8sjsWBbIVWJXK2t0xTnzYFRE9qRPiWLk-MbIjeolBe-Hqh5s9uukEWvcBcgrCew1FiMRLydTZ9bjCxqwnRNYrfedb3voZvqw1rm5fNHV4KZI0Wm1_zK-nU-vAsaRHHsJni4I6UXvDFX3v6V8nEPSpaeRtq5GGUx9PHri1UbR7QsWxiyia559Jf7lN4SKzJd6CmrQDLVGAE72YBDJzN8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتش توپخانه ارتش اسرائیل در منطقه منصوری، جنوب لبنان، گزارش شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/152324" target="_blank">📅 18:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152323">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رویترز: بریتانیا دو فرد ایرانی تبار وابسته به ج.ا را به فهرست تحریم های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/152323" target="_blank">📅 18:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152322">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا: تلاش برای حمله به فیرفورد احتمالاً در ایران و به‌طور مستقیم از سوی سپاه پاسداران هماهنگ شده بود. پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/152322" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152321">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f4e0a1584.mp4?token=AW8e2y-0aeEP2fPHtVuiaEDisc_s7HYKNerhIfh70IFJWyv7KISRXAru-tkoQPCGCe162SaXRsothtREwy3UeraQjr0jOjjeMSCqOB2HxzzmBzq68ujqA9Cp8MtOkzRyRrr8EzE-ADDtOkKh-08awep3fwrysJorkmepOv-bY19lh7nSeD-xy-OyM7MQDoITzJoMcObmFpkpy4J1kfyX0vFDtGSNQJFMqXplfLoKNBWniixCU7M4sCbqBN09Qd8qIU9fhPxYgTCb9b-oHv1hLdxU80732UeK_ZMvHMaHOZ4EsPFQfvv9ocTVTWQGKhFRRBGjJFlotKjG8eI4_TPO1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f4e0a1584.mp4?token=AW8e2y-0aeEP2fPHtVuiaEDisc_s7HYKNerhIfh70IFJWyv7KISRXAru-tkoQPCGCe162SaXRsothtREwy3UeraQjr0jOjjeMSCqOB2HxzzmBzq68ujqA9Cp8MtOkzRyRrr8EzE-ADDtOkKh-08awep3fwrysJorkmepOv-bY19lh7nSeD-xy-OyM7MQDoITzJoMcObmFpkpy4J1kfyX0vFDtGSNQJFMqXplfLoKNBWniixCU7M4sCbqBN09Qd8qIU9fhPxYgTCb9b-oHv1hLdxU80732UeK_ZMvHMaHOZ4EsPFQfvv9ocTVTWQGKhFRRBGjJFlotKjG8eI4_TPO1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوروش احمدی:
ترامپ در توافق، تحریم های اولیه و ثانویه ایران و مشخصا تحریم ها علیه نهادهای ایرانی که بعضاً نهادهای سپاه بودند را برداشت
🔴
تحریم پرداخت دلار در ازای صدور نفت از مبدا ایران را هم برداشت
🔴
شما وقتی این لغو محاصره دریایی و لغو تحریم های نفتی را ازش دیدی، باید یک مقدار به طرف مقابل فرصت بدی که ببینی آزادسازی پول های ایران را هم انجام می‌دهد یا نه
🔴
آمریکا در مورد لغو کلیه انواع تحریم ها علیه ایران متعهد به لغو شده بود؛ خب این خیلی مسئله مهمی است، همین که اصلا وارد ادبیات رسمی آمریکایی شده قبلا غیر ممکن بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/152321" target="_blank">📅 18:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152320">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آش چه شور شده صدای خضریان هم دراومده
🔴
رييس سازمان اداري که از دوستاي رييس سازمان بورسه براي اينکه رفيقش رييس سازمان بورس بمونه الکي نامه زده که استفاده از اين پيرمرد مشکل نداره.
🔴
خضريان پایدارچی هم فهميده و ماجرا لو رفته نوشته:
سازمان اداري و استخدامي غلط کرده براي افراد مجوز صادر ميکنه/ سازمان اداري غلط کرده قانون ممنوعيت به کارگيري بازنشستگان رو دور بزنه/ مگه تو کشور جوون بدرد بخور نيست که افتاديد دنبال بازنشسته ها؟ هيچکس تو کشور مخصوصا سازمان اداري و استخدامي کشور، حق نداره ديگه با نامه اداری، برای خودش قانون بزاره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152320" target="_blank">📅 18:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152319">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
تتر 260هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/152319" target="_blank">📅 18:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152318">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djfz2pyNiOiOsYRD6ZzHOy25h36UGtGVzJZRTUEUF22n89MNIZ7UxzYjjwByWFpjMTZ0UqOROcRjFIYtdZwRvmLkvY-09ZXddI2SF-PRK6XE-iidHJ3TD9FYARtnAFfdfjPUHx5_TzakY2UHtkkaTSm_Wcapl3ic9LxwDOiKc-bJV_bjroqinKQq6joH3XtDMAuvGoFTJ8MyGercgbd8kkQsnVz1sFRn2jDqY6sHbU6DeeGLUpzkGdyFtFwEvpif8ZjDeQ3WPpIZXnq1hLdZIvKaGpympSGiy0sWk6J07NN8DpT6_0KXus5TOZLyB4CU6f8oM9_Rgl-y9IakhZAkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف:
زمین و زمان را برای خود دشمن کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/152318" target="_blank">📅 17:54 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152317">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏
👈
معاریو: برآورد نهادهای امنیتی نشان میدهد اگر ایران [به اسرائیل] حمله نکند رویارویی به بعد از انتخابات موکول خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152317" target="_blank">📅 17:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152315">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTo1NhEQcswl7nmffl-4pBOwpms9DN19CNXIetRCaS3dlC2yewelfxoNBA-S9xQU_ULMx6NX3v3K7uMPphoibqPl6ZkgTeFRO_wD7UQuiTfm2-fBsOfrmAX0s_TAbqKgzliTSbTqY2_lsFutV-cdI26m2u5tsXgP5nE9l2YN3bT6xMibrHIYZO1srHXqPdyMAlA_ip0ZmkgDai4MxbuSZep2E-puDp7TY60sRW5x9q-k7NuTkmKSNRYQUU0Xk8kaIRcHm5ObWXjk1A1rpNYLHFc710r_itQmSoi0OsUMcLHlqbOeAb8LwgLCT-Rj5t3CWT9uisZKmmSBIBv6nmVmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEceuaTIkIagIsUdD1FOArJE34hs_ESS7y35zBmYWvpzOFzLu5-tnWdGtZAX2f5TLNweHP0L5MlTY3Q8DB0WBuEDI2vib7rfiEGW0IZ3q31YUpGA1iomC4s1_7VMDRlnKZd9VetCJazfjcx_jj9iZcvFNxjXO-kZ_-rgHmc29t8eJIO5A_ienr4EkJIbPwc9sLHS6RtJzUnf3gvANh2zPoCKz0jF4KIEB9aSe2KGoGYQ9rs0_5dPfB-ubrAMxogc7SjWruD3Su-uhatLtybViFGZYQ8tXjFF4y5DEVO8T_1ApTlU2B_1yMDf9wJ6DeLPs4mD-vqWxa1w4zHnqwCFUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
چندین موشک بالستیک از یزد، اصفهان و کرمانشاه احتمالاً به عنوان بخشی از تمرینات بازدارندگی موشکی در حال انجام پرتاب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152315" target="_blank">📅 17:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152314">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ec666f45.mp4?token=YJhUC2Lkohwi2tBVuk9M1-MCTQmMf6_jijnVbAhSOMw5JTDrgTLcx4Oytj513W6vy1N534NyNBRrRgrMdG24es8zGXd-RIpQLLyw1BIIaQJqvZ-RiEJVHoZ41zWUYGLdG0kCtTXJUno21nE7UelOxzS3Rx2UzddKtxxDhfPkSRAsdrPTYflxCLFzhSNjXWcNHJyMKCOLO3vHbMoL3XLSmlgRcZHgvR0LnyFD1LFNOCnqnIW2jPMcSKocSAUWAMjeQnM8Th8dJMuQNf177GyBZvuxi_CTfOtmb_yIVOtEi6h1XJOW2EVWPi22aQsjmqAh-byjzhwEkAOQ6Hsoi4LobA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ec666f45.mp4?token=YJhUC2Lkohwi2tBVuk9M1-MCTQmMf6_jijnVbAhSOMw5JTDrgTLcx4Oytj513W6vy1N534NyNBRrRgrMdG24es8zGXd-RIpQLLyw1BIIaQJqvZ-RiEJVHoZ41zWUYGLdG0kCtTXJUno21nE7UelOxzS3Rx2UzddKtxxDhfPkSRAsdrPTYflxCLFzhSNjXWcNHJyMKCOLO3vHbMoL3XLSmlgRcZHgvR0LnyFD1LFNOCnqnIW2jPMcSKocSAUWAMjeQnM8Th8dJMuQNf177GyBZvuxi_CTfOtmb_yIVOtEi6h1XJOW2EVWPi22aQsjmqAh-byjzhwEkAOQ6Hsoi4LobA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شامگاه یکشنبه تو میمه اصفهان مردم برای تبدیل شهرشون به شهرستان تجمع کردن. یگان ویژه با ساچمه و سلاح جنگی معترضان رو متفرق کردن و تعداد زیادی زخمی شدن. میگن چند نفر هم کشته شدن و بعضی مجروحا رو از بیمارستان بازداشت کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/152314" target="_blank">📅 17:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152313">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
دلار میریره یا بالا میره؟
تحلیل عجیب نخبه ایرانی
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152313" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152311">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKoVz4TruhAYGuXl54Qr347ou5DBHqxKnRG0Dg16MnigEp_AqDi-gTUWZabKQxvFqi6ReVI7poV14j-K64WOzZEXrni4OFQEf9zyU44gJLvob_W2tn2oSS6z82INKZGDZVcX2M-9nifWBQeOvsisdGiDRSnkUA8-z3_nicxYTQF8nSxxSvvEr0FVVJyccQS5IMAQDL_WmSpUWnvtuj0FKWl051v1xQP7NlnYSqcq1lmbY-PSm37zL26w8yUesCcmmzzPHYByT4uiWxQNEsOxCXNOjx2_V5CV6iOECe5A-eiMIaZARpXMzwFnn8P2FYNatwQwvQNlJFKl0vLFwr043A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBdKB5AdkE0l_O7BQk7whHCcXgMDOKmUO8hmJWiTeoAQS635L6ap-3iAzA_-CRH6nNDBBmA5xN4cYI86ugO1kBortTSMxshfOuoP6ZSPjCXKkEx-C3Poyn5Ictv5A6jsuwUbiUBhB9A0NC7t4S4Dr-X7oXcjSi3Kg7dPohUlYiJF_efGTaby6MuUmi1U94d2TBF1OLOvZGpBQMhFMBIzHGKl3CEZvxBEAi0zUlCtceXvwyv2Qq5FOlVtlOSR3iZO-M8ePWS3A62XCdMHsxjWJ7Ncd-CHGaockKA0HdQYDcOQ5NdHD8xgEvni-sKbovVHkidfNrs2W97EHc_Ef94lTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از ازمایشات موشکی سپاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/152311" target="_blank">📅 17:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152310">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Y0CmVqG3rsL33L6xHvKvkSEXbZjYxSwcYSKGfD8i9pCuimNEPHEfsSY5evGQ-62Xl2KdvkgGmZ-J3oROiP0xPQKF_e10EAvvrNlHuuK9eHTZ7LaqXd62cpEcMphcqRCmh7uC-AThAis0ZQxM6hllF_ssVCFEqRed_iKeM1MEncxGbQtxu-F_wUDJGI4BSl3hWjevLCEw7n5j7OOuBjiY_fecKNMJhJflmoo5uDKhTGtGFRWq97DNGZZNLDTcwonBDPwvfKW-tgYffYoFbKbDOu9MQFyWDK2AkcIUhK7AJw-DkK6dGNbC1FZ5wPYH6WCvpF70q6w1pImBiugKeo7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏هیمتی: دلار میریزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/152310" target="_blank">📅 16:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152309">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دوتا پست بالا از دوتا زن ایرانی با دوتا فرهنگ و محیط متفاوت
خیلی جالب اما غم انگیز</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/152309" target="_blank">📅 16:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152308">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657dc51454.mp4?token=hlk7H1KYvRB9mIjXSugF8aC3k9Rsu8pwVghIdFcZL-5MW_3tYnoHksp8j79FF3vcu2Jh8OsOar6HnPI-NqAB3qAK-Z28UEI8ykxeKBeeGnnYa475ogUoiJWv5oVYz6Oxt55pCa2v0uO4q54ngqGlG9DV_SFIgemKDhbVnTPUTheAU5wiNu9oc2t4BsW6QxyDpVas4Z-oOfHmmzzlfDtY1FcKI6zYeg1Uhi6cWxL_gORpvhW4j3QF7UHyfZcoyfFYbMmfqf1-wkfvCzeJP3W4OdNuwUpi86qZMUOYLWGF7cIz6vo4y0nBS6-VQkWPcqwL2JcDv_ioJeXcM4C3RqlYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657dc51454.mp4?token=hlk7H1KYvRB9mIjXSugF8aC3k9Rsu8pwVghIdFcZL-5MW_3tYnoHksp8j79FF3vcu2Jh8OsOar6HnPI-NqAB3qAK-Z28UEI8ykxeKBeeGnnYa475ogUoiJWv5oVYz6Oxt55pCa2v0uO4q54ngqGlG9DV_SFIgemKDhbVnTPUTheAU5wiNu9oc2t4BsW6QxyDpVas4Z-oOfHmmzzlfDtY1FcKI6zYeg1Uhi6cWxL_gORpvhW4j3QF7UHyfZcoyfFYbMmfqf1-wkfvCzeJP3W4OdNuwUpi86qZMUOYLWGF7cIz6vo4y0nBS6-VQkWPcqwL2JcDv_ioJeXcM4C3RqlYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر شایسته ایرانی به مرحله ۱۲ نفر پایانی رسید
🔴
حدیث ستاری، دندونپزشک و مدل ایرانی، توی مسابقات دختر شایسته 2026 تو تایلند تا مرحله ۱۲ نفر پایانی بالا اومد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/152308" target="_blank">📅 16:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152307">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4Gbjy3QI8OKB5vWN7Zc0ymujSKSU8F9Pemby5CLHPTbnigRXcv6CWz1AyNDCWXi3XwgVCNyQN-P3w-OkKFp3LKH0tJJDgIook0fS65stjb_y09bTop3NKjqhsXg29LHTfNyW5uzLkirZE5tPSR3CeV4xVhel-NHRcyItffmiLITCKHaMWXVXoZfz_IPqgdF-oCw4dgWYc8GjSFy6i6RtCx62EZ4CH-LDXuWrYy4XG_eGdoK9-JbAn4pGre-RNoFbsLIndnABaa06VS0ipqL8biapqTcBJggezpzDhcxEgWuOTZJf8-FHnHFHltQwsNYa6PVlmfoQBAMyoqqoMbDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قتلی هولناک در قشم
‼️
🔴
مریم یارمحمدی زنی ۲۸ ساله اهل روستایی در قشم بامداد ۱۳ مهر توسط برادرش و با کمک شوهرش و «با انگیزه ناموسی» با چاقو کشته شده و اندام جنسی او بریده شده است..
🔴
شوهرش ابتدا بچه‌ها را از خانه بیرون برده و سپس برادرش شبانه به او هجوم آورده و با چاقو، پستان‌ها، واژن و گردن مریم را مورد اصابت ضربات متعدد چاقو قرار داده و به قتل رسانده است..
🔴
هر دو بعد از ارتکاب قتل بازداشت شده‌اند اما خانواده مریم گفته‌اند هیچ شکایتی ندارند و مرگ حق او بوده است..
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/152307" target="_blank">📅 16:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152306">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری/بافل طالبانی رهبر اتحادیه میهنی اقلیم کردستان عراق از آغاز روند خلع سلاح و اجرای روند صلح احزاب مسلح کُرد ایرانی خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/152306" target="_blank">📅 16:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152305">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: تلاش حکومت سعودی برای تبدیل‌شدن به قطب هوش مصنوعی اکنون با خطرات جدیدی روبه‌روست؛ چراکه دیتاسنترها جزو اهداف حوثی های یمن هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/152305" target="_blank">📅 16:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152304">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u8brNJwuSpPAiT2n3i1_b34B50RLIEDA48qXsqQVNo6dyEIRunmjXn2JVN8tnGvPfyYn6v3fN7EB9Q51n-f0tEmlXeZfkCeiegFtkfqSBgEx2HnL780y5LRVecWsU4zx0voQfeC89XQeacmf-F_LaGp-v4LJ44WzLFhZ5ZiY4uslkGdcBC2ZFXfVZe2nFq3Q91dSBxbgzocwLTheiRdLrxJ7fcfW6UTkm8WTX5vPO66qmRh8CmAM59vUxZ7luvpMMkGOz2PQJ4cYOJ_5r3UveEkiZVJugtIZarPq52ZRfH3RR76BGGlkmB6CMG5gHnwUomloOYQBuAua8T6Du7jFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت ایران نسبت به هفته گذشته 70 درصد افت کیفیت داشته، کم کم به مرحله ای رسیده که فیلترشکن های رایگان و پروکسی درحال از کار افتادن.
این یه نوع پیش آمادگی برای قطع سریع اینترنت در زمان حمله و آغاز جنگ آیندست.
از دیدگاه مقامات ایران جنگ قطعیه و بین بازه ۲۰ الی ۳۰ مهر جنگ ایران و آمریکا در ابعاد بسیار گسترده تر از جنگ ۴۰ روزه آغاز میشه.
🔴
ولی این سری قطع شدن اینترنت همزمان با آغاز جنگ قطعیه.
🔗
اینترنت پایدار و متصل
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/152304" target="_blank">📅 16:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152303">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4daef3062.mp4?token=uy6PSVp8QTfoUI8GB-0Cp90bapeXuvDuKb5V-gM6odkpOVErjvYKQ77MxKuhfd3aviqFtUI4ACXMAnW85rOU7DVccJ0cU4vd6n5TmHw4t78M4kCVkg2M03qhAMFm-f-LEdGmZL8zLLeK5UB8mdZvIvS9bxzwQwy52bbZdVleFvN4BVvb4a591UgC9MJvAPb0Vi_59FomVPFhUu229MBZMHC2ifcjT15EVL6FkVd9M7m1E2C0liu9Cb2oIlSYOKyzelmwSxwEmuOLuU0fNcje6PqSo7YYlqs9JEGFHQHkGkVgx4dr_OSnxLC03uLyWmlqD-tKYQj9ZqqJ1FQ95fRnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4daef3062.mp4?token=uy6PSVp8QTfoUI8GB-0Cp90bapeXuvDuKb5V-gM6odkpOVErjvYKQ77MxKuhfd3aviqFtUI4ACXMAnW85rOU7DVccJ0cU4vd6n5TmHw4t78M4kCVkg2M03qhAMFm-f-LEdGmZL8zLLeK5UB8mdZvIvS9bxzwQwy52bbZdVleFvN4BVvb4a591UgC9MJvAPb0Vi_59FomVPFhUu229MBZMHC2ifcjT15EVL6FkVd9M7m1E2C0liu9Cb2oIlSYOKyzelmwSxwEmuOLuU0fNcje6PqSo7YYlqs9JEGFHQHkGkVgx4dr_OSnxLC03uLyWmlqD-tKYQj9ZqqJ1FQ95fRnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالگرد های اسرائیلی در حال انتقال مجروحان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/152303" target="_blank">📅 16:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152302">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ۲۰ مجروح در حادثه در منطقه الجلیل، حال یکی از آن‌ها وخیم و حال دو نفر دیگر خطرناک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/152302" target="_blank">📅 16:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152301">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سفیر پیشین ایران در بیروت: پیجر من قبل‌از انفجار نوشت یک پیام فوری دارید!
🔴
اولین‌بار بود که با چنین پیامی مواجه می‌شدم؛ روی صفحهٔ پیجر نوشته بود که «برای مشاهده پیام دکمه را فشار دهید» و به‌محض فشاردادن دکمه، پیجر منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/152301" target="_blank">📅 16:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152300">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: کشورها، حتی آنهایی که به ما حمله می‌کنند، به آرامی و پنهانی می‌گویند که حکومت ایران باید سرنگون شوند، آنها ما را خفه می‌کنند
🔴
ما مطمئن خواهیم شد که آنها سرنگون شوند. آنها سرنگون خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/152300" target="_blank">📅 16:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152299">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
عربستان سعودی به دنبال افزایش ظرفیت لوله‌های نفت به ۱۰ میلیون بشکه در روز است
🔴
عربستان سعودی در نظر دارد ظرفیت خط لوله نفت خود را به 10 میلیون بشکه در روز افزایش دهد و توانایی خود را برای انتقال نفت خام در سراسر این کشور تقویت کند
🔴
این طرح ها ظرفیت خط لوله شرق به غرب را افزایش می دهد که نفت را از تاسیسات تولید در استان شرقی به بندر ینبع دریای سرخ می رساند
🔴
گسترش این شبکه به عربستان سعودی اجازه می دهد تا نفت خام بیشتری را بدون اتکا به تنگه هرمز صادر کند، تنگه هرمز که در طول درگیری های منطقه ای با اختلالات مکرر مواجه شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/152299" target="_blank">📅 15:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152298">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل: ۱۲ نظامی اسرائیلی در یک حادثه در جنوب لبنان زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/152298" target="_blank">📅 15:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152297">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b594a539.mp4?token=NhkmcFAw4qX3w5e3RDjy87_ICR0GGHf8Rit8_z7OChQABi8VkBAh4QGyJHnnTbzdStPFgpSKzfB4UsT54HvFP5hA9Tq-5HHusuxCJ62VwEiUgBFov6B5q1nmBjxeOTMZVSuz8LMB91lNgukUypTQvI0ZmPX2fS-VpeGP9LmEqllWJBlHnijoEFgqZbtVSxaZys38lUW9bX4NEywDryj0XqD_sqQHtnScmkjWJjF63pMwKQve26mhr1J9jVLwmN2kfK6KK0TMM7rhQCNUfaQbT-N9yNpKCbxEVZHyBkdPC1JW14gmBhA7HME7Ak9aGHzcFKhrCOO3AzIyaRki5P9JiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b594a539.mp4?token=NhkmcFAw4qX3w5e3RDjy87_ICR0GGHf8Rit8_z7OChQABi8VkBAh4QGyJHnnTbzdStPFgpSKzfB4UsT54HvFP5hA9Tq-5HHusuxCJ62VwEiUgBFov6B5q1nmBjxeOTMZVSuz8LMB91lNgukUypTQvI0ZmPX2fS-VpeGP9LmEqllWJBlHnijoEFgqZbtVSxaZys38lUW9bX4NEywDryj0XqD_sqQHtnScmkjWJjF63pMwKQve26mhr1J9jVLwmN2kfK6KK0TMM7rhQCNUfaQbT-N9yNpKCbxEVZHyBkdPC1JW14gmBhA7HME7Ak9aGHzcFKhrCOO3AzIyaRki5P9JiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: آنچه در کرینکی رخ داده، نسل‌کشی است
🔴
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، گفت روسیه در منطقهٔ کرینکی مانع دسترسی کودکان و بزرگسالان به غذا می‌شود و این وضعیت را نسل‌کشی توصیف کرد، نه قحطی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/152297" target="_blank">📅 15:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152296">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQcuGyntZMLFtWoEhncsKkOH5v1dK9dJoKIMAi6ugXkGcDZ-GbeGvrPGP8W6ZqgnSjJaSXMSiCyAhMEUqFPHVE2XtrMgYzCROzWNN4WwAcpkn8XfE_Winj3RaoTTTaRXO23QZiPIMVuf2Oj8Gzj99M2dN_c3Eq4AxGdy2K2j1bzisHZRHzso38_XoNn5NP6pDqJa3boUu9pZ1Qz4j6oCUeP3PITCB53-FqI7F97wqG-nMkluAweYfN56kDEjoytGQdoEDHUVxP9H0KRTzJmyVzzkfJwAqFtU9Y25q08bj3lEJ2LW0341rsBvJJvNrHOwurhOFOxvIBPtcuBQ6GtewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرسلیم:
اینکه پسرم با مجاهدین بوده به من چه؟ مهم اینه توبه کرد برای همین اعدام نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/152296" target="_blank">📅 15:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152295">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
نمیخوام جو بدم یا ته دل کسی رو خالی کنم ولی این چنلو داشته باشید بدونید چ‌خبره
👇
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/152295" target="_blank">📅 15:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152294">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر پیشنهادی دفاع: تقویت پدافند هوایی را با جدیت دنبال می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152294" target="_blank">📅 15:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152293">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
هواپیماهای ترابری نظامی آمریکایی به صورت پی در پی با حرکت از آلمان، لحظاتی قبل در اردن و اسرائیل فرود آمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/152293" target="_blank">📅 15:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152292">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geJT7AHwm42NIvnWQfXDZwsJVwdO9pbWENhfEILvCu6JoVllLWzxzDkyPUHgUvjDSQ6YgrMb5GmhK7W3ahrYOTMkvfZ76eLzIkxptkjqG-6wI-L5h4Zwpcm1pfAmn_8RxHVxvglnYjTLmrGNnsbasVdUqkkMI7qYjj5Y3uMvwqehP7zLN0MQ9A0vzWJAPkzEyO5QPqLfZpAI_lc-0oe8Nk49o7reNKmeMqSCZEYXCtDR7DBh_nRdtMg_X0hZ6OQ5gdEMCwslWVxX3WIvN8dTlxvUbgRKKTjKXPqOpzAEny0skm-3jAvO4hUNaDiQ0nVYbyhdRkzdPGvn_uLz6WzRDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برندگان جایزه نوبل اقتصاد ۲۰۲۶ معرفی شدند
🔴
آکادمی سلطنتی علوم سوئد: رابرت هال و مایکل وودفورد، دو پژوهشگر دانشگاهی آمریکایی، به‌دلیل پژوهش درباره «مبانی اقتصاد خرد تثبیت اقتصاد کلان»، برنده جایزه نوبل اقتصاد ۲۰۲۶ شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/alonews/152292" target="_blank">📅 15:20 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
