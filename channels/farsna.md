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
<img src="https://cdn4.telesco.pe/file/gLuGNg4tknGYL7og6NK0hS5jk-_dlpqX6ObhQoTld9q7NWgX3yAIRBp-FbQwLRIkNmONkvu4yGS5p4h0icQIDnxhChi83Dk3EO8CRw35CCKESxJrBXyjZdiOlgf62UHIlC9Ks4QJOK0f2si6rE7ohfElbny40EASIDnsfnuSIeah9l_lfng63VTdib7YxDgX6xcpE4RZDArXn6Y__eZuxXQs6ethw5NnUeqqwkqCQr19swEz0DgbwAiR-kaa5tv_oaVvB_tbN-Ofji_in1K7rOQ7Ii3PBscQ8oD0DAiHvO8_PAMkM7Th7nGze5rBlXXip3AA4XuhSdYfLXFFbY7zRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 23:14:41</div>
<hr>

<div class="tg-post" id="msg-454913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G03ZtnizsgVjz6QdJHmNFhVFSt-ptkDLu6Tv4ISmOoqDGt7sl3J42qgv0vM-vhXd6foUBpltFj-FPCFzX0ReOUgppR2JkcewU4h3VQlLS3oXeBOygkrmfZ9Vdu6iAo3lX0G3pDowWN03dPzUfAadxA6jnk11Z8En62KNYzHFQUkQu3oYohCJo7AeR5NRDDMHJmdvaiQ7db2zZ8fOOvjoM9I6uNLkOVe4JMxeULaGw2jsrinabyvuelwew5dUzw7NB07NAj6Q5b_4m0r-0rqZDp9zPeZNEYuQJMcoMP1iqIdPqIck0dF_gCemwmbdBABh5J7O1pbJYGUgoL0xpsO_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق مکه؛ ائتلافی برای نجنگیدن
🔹
عربستان سعودی، پاکستان و ترکیه امروز جمعه ۱۶ مرداد در مکه سندی امضا کردند که از آن با عنوان «توافقنامه دفاع مشترک مکه» یاد می‌شود. مهم‌ترین بند این سند، بر اساس بیانیه مشترک سه کشور، «اصل دفاع جمعی» است؛ به این معنا که هرگونه حمله مسلحانه به یکی از سه عضو، حمله به هر سه تلقی خواهد شد.
🔹
اما اولويت‌ها، سازو کار تصمیم‌گیری در سه کشور، تجهیزات و خلأهای فنی در توافق، تا حدی است که هرگز فرمان نبرد مشترک صادر نخواهد شد.
بیشتر بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 19 · <a href="https://t.me/farsna/454913" target="_blank">📅 23:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b4eca2cdf.mp4?token=TwSAKdydJruNPXwWf0e_fOp70zEIBe2_NR1bMf6PeW30T0MQutYEhgCaeHKHiUTT3p0gBDs-_Xg-vmRZRxmLkLQqAxNNMM-KNpSw6POU93gP8NAc6fzVa9RCTvN-TnMTquiksD2o4A40NFVUOsrM_lAwLs559FaYGP1w-OJeXLwvFpveuoWCPrrwpwt9K9N7TZRgEDDVwEoZ4uBYboGjL_K2r52FmaoldLIHHl_UZ6n9rIRNs5UxlyplAl3hboyaBUMy6YOnC2twJGHA-Jh20XGEInuxBS-KPtYN0Nm-HfQp-EevgJBp-ldRsDSiLjHu5ehlrRxkbMveifslIeKRxKC-3LeaxAUFOZsPBFuC8wZNhQTHm8_5396zpma6c0cUiV-smlMWZYMfrB-Wgd5mu56qoxhD5VupecdQmqzYAkvKbyuKqB8i3ZnU5XEZJ9emuNyrxTNqG4mVRCU_KEpy1C6ArShT6Gvv4ZR2rbnjQBZbubQSSoFLsmlqmN6QL6CcRvdso3Pyw0q8v_xgrCd0HtI_C9FuDj9casSdclX93gTwWpPzUb5tia546zGZ68GgTAohNGkOlKhYPtq417PVDIpGdj0OVvR6M4kwy0PoSugx5sNGWNqpxzwSTOQMN3pu8o7rCJe4iD0L3Vf5kMSmDal95vQ7hLPQY7nTtR7klIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b4eca2cdf.mp4?token=TwSAKdydJruNPXwWf0e_fOp70zEIBe2_NR1bMf6PeW30T0MQutYEhgCaeHKHiUTT3p0gBDs-_Xg-vmRZRxmLkLQqAxNNMM-KNpSw6POU93gP8NAc6fzVa9RCTvN-TnMTquiksD2o4A40NFVUOsrM_lAwLs559FaYGP1w-OJeXLwvFpveuoWCPrrwpwt9K9N7TZRgEDDVwEoZ4uBYboGjL_K2r52FmaoldLIHHl_UZ6n9rIRNs5UxlyplAl3hboyaBUMy6YOnC2twJGHA-Jh20XGEInuxBS-KPtYN0Nm-HfQp-EevgJBp-ldRsDSiLjHu5ehlrRxkbMveifslIeKRxKC-3LeaxAUFOZsPBFuC8wZNhQTHm8_5396zpma6c0cUiV-smlMWZYMfrB-Wgd5mu56qoxhD5VupecdQmqzYAkvKbyuKqB8i3ZnU5XEZJ9emuNyrxTNqG4mVRCU_KEpy1C6ArShT6Gvv4ZR2rbnjQBZbubQSSoFLsmlqmN6QL6CcRvdso3Pyw0q8v_xgrCd0HtI_C9FuDj9casSdclX93gTwWpPzUb5tia546zGZ68GgTAohNGkOlKhYPtq417PVDIpGdj0OVvR6M4kwy0PoSugx5sNGWNqpxzwSTOQMN3pu8o7rCJe4iD0L3Vf5kMSmDal95vQ7hLPQY7nTtR7klIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی بروجردی‌ها در شب ۱۶۰: لشکر با ابهت لرستان، گوش به فرمان امام زما(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farsna/454912" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572a4348e0.mp4?token=j0xSHqYcarGbLELLUEneP4WmvrmSRY85nlgErprl_fhAwzIrx3HEOwpMBwAw6x-xerHFOfREGA7G6khNcTcesoQjHMQlQYtk8O9gMAdmJvjGYrg31oJ7UeTkUOed0NVCfitxgHOUpID3KczrKAo5uFLHX_WS78vrmRT6_ijQQwFkhOoSJ9f9HQgs0m_Wo7pbKIOeKMK9LzcGG6qt-AHd5sFkhfU5BSofrdygl4G8yQ2x1ZRE-ab9q5fSuNE7cHci5_AxxRlHT8RgXka1pG_e8JdJbTqq3vdVVvw-dlN1LE2yKVw0lzM_8FbYUm3efno35lZ2Rkn0ieTszrgcr2VAkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572a4348e0.mp4?token=j0xSHqYcarGbLELLUEneP4WmvrmSRY85nlgErprl_fhAwzIrx3HEOwpMBwAw6x-xerHFOfREGA7G6khNcTcesoQjHMQlQYtk8O9gMAdmJvjGYrg31oJ7UeTkUOed0NVCfitxgHOUpID3KczrKAo5uFLHX_WS78vrmRT6_ijQQwFkhOoSJ9f9HQgs0m_Wo7pbKIOeKMK9LzcGG6qt-AHd5sFkhfU5BSofrdygl4G8yQ2x1ZRE-ab9q5fSuNE7cHci5_AxxRlHT8RgXka1pG_e8JdJbTqq3vdVVvw-dlN1LE2yKVw0lzM_8FbYUm3efno35lZ2Rkn0ieTszrgcr2VAkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با گفت‌وگو توانستیم جنگ لبنان را متوقف کنیم، محاصره را برداریم و برخی تحریم‌ها را کاهش دهیم.
🔹
عده‌ای می‌خواهند بجنگیم؛ همان چیزی که اسرائیل می‌خواهد تا ما را وادار به تسلیم کند.
🔹
ما کوتاه نخواهیم آمد و سر تعظیم فرود نخواهیم آورد. @Farsna</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/farsna/454911" target="_blank">📅 23:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5abfce3af6.mp4?token=VCCY4O30Z7ha1yhCt6SEoNtqBpTGYY7mX_7SLATHyVr92Rkw_DC4a8SA7D-hEl2lM9YkkAgvnXGo51yhdPTGrkhaVcM2nSkvUX7qVvbdb4_g7BSUj7E3KjLVMeTPHhom58cHjw2ooMKH2KFnmWw1yER8W_YTgN5vWBR3P3QpGl0tQOdkfgfg2fWqZPxVBKHsTiNe8jeDxoZCSLA-JLg6sTLR7OBAp4VEC0iqyqb5vX8g236fH4rXxeXjjcexlFyaOnguruzntYZ5ghXxjQCmtic9cMPKcTTFDdPLTmOl_txcZhxfTVCp4OZY6LE5Y4Tlmnawkdd3vwsv8L2SKzcSFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5abfce3af6.mp4?token=VCCY4O30Z7ha1yhCt6SEoNtqBpTGYY7mX_7SLATHyVr92Rkw_DC4a8SA7D-hEl2lM9YkkAgvnXGo51yhdPTGrkhaVcM2nSkvUX7qVvbdb4_g7BSUj7E3KjLVMeTPHhom58cHjw2ooMKH2KFnmWw1yER8W_YTgN5vWBR3P3QpGl0tQOdkfgfg2fWqZPxVBKHsTiNe8jeDxoZCSLA-JLg6sTLR7OBAp4VEC0iqyqb5vX8g236fH4rXxeXjjcexlFyaOnguruzntYZ5ghXxjQCmtic9cMPKcTTFDdPLTmOl_txcZhxfTVCp4OZY6LE5Y4Tlmnawkdd3vwsv8L2SKzcSFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کلیات توافق نهایی شده بود و برای افزایش اعتبار آن، قرار بود امضای نهایی از سوی ترامپ انجام شود تا امکان عقب‌نشینی از توافق وجود نداشته باشد.
🔹
اما کمتر از ۲۴ ساعت بعد، روند مذاکرات به‌طور کامل تغییر کرد و توافق به سرانجام نرسید. @Farsna</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/farsna/454910" target="_blank">📅 22:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d007d8a7.mp4?token=VF_-TTtC0wW0vVuBfIhQXdIZ058iF1Cq2nFy1OZ6DsPbFWboKJlN6inlplVZeeVqcHK6Ih3HFfbl-KAHGVRK-pu6sP-MdHkqRQZqcL6vAdi53_hhCFNLzxx2HkceczCb6TbWRzKMJEaXML4dgWx-f8ltcm1wdrCsEWd4NQwZFfw_w8l2f-vwlwGTUv7fsXZmL1Zmo3P9br6Ip5E0KKbDt8pF6GyU_WC3fnUwV83as4xbfE0P_cQyixfmlRUZnYQTHJxdsi5efIe6WU3mxZavmPslxUmltYHmaxab06aCAM8dr5_EdpBa8yhTvoYRZiL6GG8ENEEKKCM4rHZu0ALGrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d007d8a7.mp4?token=VF_-TTtC0wW0vVuBfIhQXdIZ058iF1Cq2nFy1OZ6DsPbFWboKJlN6inlplVZeeVqcHK6Ih3HFfbl-KAHGVRK-pu6sP-MdHkqRQZqcL6vAdi53_hhCFNLzxx2HkceczCb6TbWRzKMJEaXML4dgWx-f8ltcm1wdrCsEWd4NQwZFfw_w8l2f-vwlwGTUv7fsXZmL1Zmo3P9br6Ip5E0KKbDt8pF6GyU_WC3fnUwV83as4xbfE0P_cQyixfmlRUZnYQTHJxdsi5efIe6WU3mxZavmPslxUmltYHmaxab06aCAM8dr5_EdpBa8yhTvoYRZiL6GG8ENEEKKCM4rHZu0ALGrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: از قالیباف خواهش کردیم که رئیس تیم مذاکره‌کننده شود
🔹
همکاری و هماهنگی میان دولت، مجلس، قوه قضائیه و نیروهای مسلح، عامل اصلی عبور از شرایط سخت بوده است.
🔹
بی‌احترامی و تفرقه، خواستۀ دشمن است و باید با همدلی و احترام با یکدیگر رفتار کنیم. @Farsna</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/454909" target="_blank">📅 22:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825ae52635.mp4?token=gUGHxtXtAbKVwyYf2BHkUVx_lFf6dAkZiFrwBJa-gYvjFwafKOnn57HPlyi5ERoKgKsIznMiL_dbVX3j1Nz7CU9edqiRVLjIQ-au2UtMVzrWTcUtli27fNLmlUjZSA1KIg3iHXnLhIGNxjFwcNcz_5KSwO4B7jQkZHoW9BTiIPHFiDClR_MD-qzctliMes5IoHn38Sz7bJLp9q3THpLw9EohPyTqhjfG3-0e01-tZuVNt4_FqE4elDe5RF-Z-c1J8d5Yzcpm6CUuEbuPt5mI8-uTcWWrDGaKtietampeqrloSkoKPMnPhFJRy92d5zHNuVz38SFX0vGD03sgd3RQmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825ae52635.mp4?token=gUGHxtXtAbKVwyYf2BHkUVx_lFf6dAkZiFrwBJa-gYvjFwafKOnn57HPlyi5ERoKgKsIznMiL_dbVX3j1Nz7CU9edqiRVLjIQ-au2UtMVzrWTcUtli27fNLmlUjZSA1KIg3iHXnLhIGNxjFwcNcz_5KSwO4B7jQkZHoW9BTiIPHFiDClR_MD-qzctliMes5IoHn38Sz7bJLp9q3THpLw9EohPyTqhjfG3-0e01-tZuVNt4_FqE4elDe5RF-Z-c1J8d5Yzcpm6CUuEbuPt5mI8-uTcWWrDGaKtietampeqrloSkoKPMnPhFJRy92d5zHNuVz38SFX0vGD03sgd3RQmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هرگز استعفا نداده‌ام و نخواهم داد  @Farsna</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/454908" target="_blank">📅 22:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcf3016833.mp4?token=ugGHjwgA0XFwtAZGFlhOrzyxrz-ClFPwaFcyVkdKDgkpSS57D81bRTi8puWmY8iIPvg97bPbAwW2ovhAD2KW8e2uihHDFzUuEoJGwSJLUQ_fZ4jhWM3HWnnjh52I6icaPP2SqOVYml7prIQDei-VP473-MI6z87sQe5muj8laurb1b4Rw6sT-wTFouAFGuJTIXFy794fB6ZYIvmi8gm9vVanc4adSig5qVbgRC5cfm2BIm5m5RiUjOglX4HePDjkdReB1aUaBkWTq2ZvmGPxSnB2N4ID5ZQ7evBuBv5pNDLCZZsyG16o3D4gtSGiKEFcpGDRjfSTerWBDsHEEjof1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcf3016833.mp4?token=ugGHjwgA0XFwtAZGFlhOrzyxrz-ClFPwaFcyVkdKDgkpSS57D81bRTi8puWmY8iIPvg97bPbAwW2ovhAD2KW8e2uihHDFzUuEoJGwSJLUQ_fZ4jhWM3HWnnjh52I6icaPP2SqOVYml7prIQDei-VP473-MI6z87sQe5muj8laurb1b4Rw6sT-wTFouAFGuJTIXFy794fB6ZYIvmi8gm9vVanc4adSig5qVbgRC5cfm2BIm5m5RiUjOglX4HePDjkdReB1aUaBkWTq2ZvmGPxSnB2N4ID5ZQ7evBuBv5pNDLCZZsyG16o3D4gtSGiKEFcpGDRjfSTerWBDsHEEjof1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ دولتی به اندازۀ ما در جهت سیاست‌های رهبری قدم برنداشت
🔹
اینکه عده‌ای اختلاف‌سازی کنند و القا کنند رهبری چیزی می‌گویند و دولت چیز دیگری، هم در حق رهبری جفاست و هم در حق دولت. @Fasrana</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/454907" target="_blank">📅 22:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f3ea9adb1.mp4?token=RajI1-zAK574rGOLYn8M12b7AuEqz-BFzBi9qrn8YLSYGx392S-9Z-vpti-N_o7ADxRxzjnwAj_OXw_yUH486OqLG0s8t5CX69mmDCDcT9dnqtdb9OlEbAGFvT_0iJ5uIYZEb3u8MAgwX_noMKuG0OpM4e1fFOnfQGayKzuscyjYuVt55F-hw3CBTIKa0ip1Y_A7Pju9ukiU4xdnxYs3FzvlJcJ2yQoYs0kQjM-03WnJXiAFMCgBEXZGSyOGYa6hZUn7EbZJR3ZycSqqOoUuH2sxW6J1DrNpuf90422k4yOCC60AAUcz_zMp8cUJnIT815Uwlu3fFgfN3IHXrf_pyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f3ea9adb1.mp4?token=RajI1-zAK574rGOLYn8M12b7AuEqz-BFzBi9qrn8YLSYGx392S-9Z-vpti-N_o7ADxRxzjnwAj_OXw_yUH486OqLG0s8t5CX69mmDCDcT9dnqtdb9OlEbAGFvT_0iJ5uIYZEb3u8MAgwX_noMKuG0OpM4e1fFOnfQGayKzuscyjYuVt55F-hw3CBTIKa0ip1Y_A7Pju9ukiU4xdnxYs3FzvlJcJ2yQoYs0kQjM-03WnJXiAFMCgBEXZGSyOGYa6hZUn7EbZJR3ZycSqqOoUuH2sxW6J1DrNpuf90422k4yOCC60AAUcz_zMp8cUJnIT815Uwlu3fFgfN3IHXrf_pyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: تفاهم‌نامه آتش‌بس با هماهنگی، تفاهم و همدلی در شورای امنیت ملی شکل گرفت
🔹
ما با نیروهای نظامی کاملاً هماهنگ هستیم و پشتیبانی از آنان را وظیفه خود می‌دانیم.
🔹
کسانی که جانشان را کف دست گرفته‌اند و از این کشور دفاع می‌کنند، مگر ممکن است میان ما و…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/454906" target="_blank">📅 22:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92096f3d23.mp4?token=T1EqFAWQ6N9R0p6yjUIQDGCOtKDqWZpVSpjs8ZGGgaI8_9LF8VZcPIJ6IzvKyGnrqGwjFY9mulj4VZCvG0VC_pAiCTYJ4HvYYBd32GEcjLrZ_YkVWKLM-FMv_1XNv-__soazQn03KtdS8MMJDU72e7i4GMLO52XE_c590BMaIIWGl-D-fXFi5q6OdleCflTsa8OthRtxl3hJI62KsrK15_Q_vRxtRFfeFcpnzFec2EuZjIxkj1jI-Pb2C5aiQoiqisZAnyZ26RryG2lF2Jn4bBRw6hxEjvU5EsT-UsM5IUv0ucAjW1z0U39GG3w3nQKdVBFLGe2gEZB-joqDsgSwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92096f3d23.mp4?token=T1EqFAWQ6N9R0p6yjUIQDGCOtKDqWZpVSpjs8ZGGgaI8_9LF8VZcPIJ6IzvKyGnrqGwjFY9mulj4VZCvG0VC_pAiCTYJ4HvYYBd32GEcjLrZ_YkVWKLM-FMv_1XNv-__soazQn03KtdS8MMJDU72e7i4GMLO52XE_c590BMaIIWGl-D-fXFi5q6OdleCflTsa8OthRtxl3hJI62KsrK15_Q_vRxtRFfeFcpnzFec2EuZjIxkj1jI-Pb2C5aiQoiqisZAnyZ26RryG2lF2Jn4bBRw6hxEjvU5EsT-UsM5IUv0ucAjW1z0U39GG3w3nQKdVBFLGe2gEZB-joqDsgSwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: آمریکا از سرزمین کشورهای منطقه به ما حمله می‌کند و ما باید از خود دفاع کنیم
🔹
مبدأ حمله به مدرسۀ میناب در یکی از کشورهای مسلمان بود.
🔹
دشمن از پایگاه‌های آمریکا در برخی کشورهای منطقه علیه ایران استفاده کرد و ایران ناچار به دفاع از خود شد. @Farsna</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/454905" target="_blank">📅 22:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edbd6dc5c.mp4?token=REQJ_IvbXmCvvOEpI1aD7UgiH7vVGKYf2Rp_NzGn5iXUEl61g95C6ziXhVGQsIRZUn5RNufidNyAiq-fZzaktJEsjOq2pUF6JA7R_U2I_PVlYGPFrZux29Abmcub4Kbk3PhwPjHprqzkevpYt6s2uOICVx_A4aFRAUvJSoU96JBMt4S_CE-wGklxJST4hhxrY3M89VDsRiJzf-yN6aU4rUG37pHbkQ0AxhaElLoHP0yfuQ1--5MlHFWzVwubAU2tmRXR1ezmQggB7ImITGKlm5W0Pu7XHakJ77Lc2bCXQ6Q3GFzV5HWDJa60R3nqTbnDfNcbUd_7LP9yxT6Zv3G7mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edbd6dc5c.mp4?token=REQJ_IvbXmCvvOEpI1aD7UgiH7vVGKYf2Rp_NzGn5iXUEl61g95C6ziXhVGQsIRZUn5RNufidNyAiq-fZzaktJEsjOq2pUF6JA7R_U2I_PVlYGPFrZux29Abmcub4Kbk3PhwPjHprqzkevpYt6s2uOICVx_A4aFRAUvJSoU96JBMt4S_CE-wGklxJST4hhxrY3M89VDsRiJzf-yN6aU4rUG37pHbkQ0AxhaElLoHP0yfuQ1--5MlHFWzVwubAU2tmRXR1ezmQggB7ImITGKlm5W0Pu7XHakJ77Lc2bCXQ6Q3GFzV5HWDJa60R3nqTbnDfNcbUd_7LP9yxT6Zv3G7mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ امتیازی در تفاهم‌نامه ندادیم
🔹
می‌گویند آمریکا به تعهداتش عمل نمی‌کند؛ تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود. @Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/454904" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a5fb3640.mp4?token=cLqztr4VraG38VBaD6NRpMPq10Z50N0CJR8aBumJ-j7D-XbP0-j6uDluwLTguMI5Cf5aDYfu-yFyukuhcQKyf4Hm6UGQglsnWjk2vc2YuiQlqAAocx6v94smitZsj8V2O7F5T2XAfJ1Mb8kEciRO1VD2xH9ukYlje2hlV-B110O2L7TW2OOSFxrGN_TAuH_T80Q8IM5mirneC-uAVOuUnkyXmtOLVV8KsO-sLwUyQOUJjZDzSUFMhdEDWRv2mN5sKLBhxbghyvk2NSAQmNPUvXXJxzsjbl-tBO7sB1YhI5kuxZyXyXzhy9QqxThR3YiYwoOP5KMicW5MWpdMOwRwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a5fb3640.mp4?token=cLqztr4VraG38VBaD6NRpMPq10Z50N0CJR8aBumJ-j7D-XbP0-j6uDluwLTguMI5Cf5aDYfu-yFyukuhcQKyf4Hm6UGQglsnWjk2vc2YuiQlqAAocx6v94smitZsj8V2O7F5T2XAfJ1Mb8kEciRO1VD2xH9ukYlje2hlV-B110O2L7TW2OOSFxrGN_TAuH_T80Q8IM5mirneC-uAVOuUnkyXmtOLVV8KsO-sLwUyQOUJjZDzSUFMhdEDWRv2mN5sKLBhxbghyvk2NSAQmNPUvXXJxzsjbl-tBO7sB1YhI5kuxZyXyXzhy9QqxThR3YiYwoOP5KMicW5MWpdMOwRwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: هیچ امتیازی در تفاهم‌نامه ندادیم
🔹
می‌گویند آمریکا به تعهداتش عمل نمی‌کند؛ تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود.
@Farsna</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/454903" target="_blank">📅 22:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25623b3011.mp4?token=a_IbnyLuDDalGMDUSFsEFQ0xE3VVW9JvzkhqUwJdsQdgNsJpVwQHumr-qQaUGA8q3TUB_7dC41oEdTBaI0B6xNTi6LDu2sKTE2R8nHVcmlEez2IbSX2U7ibS4bCJK0-nm9Skyk9spohbZRF5gxgf348M2mFf81GVNsGKhJLm3R6Ky7C_47tbrBUHQuRv1c-XEF09vBh_R8e89xRSvwVNVu77IjK9g82twXRCm8kpWKK1X_paxviBtHimSMTQ4nWg2JzabISH0SzzNxvViD3VXn6qFZfPPrXDyXWHjP37pzAaXMmo_E9RmTD9-RhwbzSaqJowr_stXMOU537dSc9jZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25623b3011.mp4?token=a_IbnyLuDDalGMDUSFsEFQ0xE3VVW9JvzkhqUwJdsQdgNsJpVwQHumr-qQaUGA8q3TUB_7dC41oEdTBaI0B6xNTi6LDu2sKTE2R8nHVcmlEez2IbSX2U7ibS4bCJK0-nm9Skyk9spohbZRF5gxgf348M2mFf81GVNsGKhJLm3R6Ky7C_47tbrBUHQuRv1c-XEF09vBh_R8e89xRSvwVNVu77IjK9g82twXRCm8kpWKK1X_paxviBtHimSMTQ4nWg2JzabISH0SzzNxvViD3VXn6qFZfPPrXDyXWHjP37pzAaXMmo_E9RmTD9-RhwbzSaqJowr_stXMOU537dSc9jZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیر بار زور نمی‌رویم، اما به‌دنبال جنگ و تجاوز هم نیستیم
🔹
ایران به‌دنبال جنگ یا توسعه‌طلبی نیست و تنها از توان دفاعی و امنیت خود حفاظت می‌کند؛ اگر فشار و تهدید علیه ایران متوقف شود، دلیلی برای ادامه تنش وجود نخواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/454902" target="_blank">📅 22:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454901">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ab394bfe.mp4?token=Mko1jy5Ud7wFcuQc6e5EqyqYHhtLUcngUcZpkeieuUCIaBE_OceOCJX5bSZT2xyMOa14IkW17dEvp5HtwB_5-8PPo5_q_2DwoD1floE2MRfyrqEAWQaz4gVHzHiffB6G3nyBMNUF5J-4XuS8_THyE2zfbLl_q11oNjvFTyWksR5CZzPIDHKNRmRL0E4tkAjqCF7ljQ-yYdavUBEQAAxGvDf9zEZa5Nx63Lmk4BfM5HYXWt9TRO30twgAGazKHQmmbfoIqiTEtH8-Guy43b_9gEceXsf6eWjuFn_Bk60Rosc7ugze7EBzL9ii8M-JlUrctKhlfTU5lty7d0UxVocNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ab394bfe.mp4?token=Mko1jy5Ud7wFcuQc6e5EqyqYHhtLUcngUcZpkeieuUCIaBE_OceOCJX5bSZT2xyMOa14IkW17dEvp5HtwB_5-8PPo5_q_2DwoD1floE2MRfyrqEAWQaz4gVHzHiffB6G3nyBMNUF5J-4XuS8_THyE2zfbLl_q11oNjvFTyWksR5CZzPIDHKNRmRL0E4tkAjqCF7ljQ-yYdavUBEQAAxGvDf9zEZa5Nx63Lmk4BfM5HYXWt9TRO30twgAGazKHQmmbfoIqiTEtH8-Guy43b_9gEceXsf6eWjuFn_Bk60Rosc7ugze7EBzL9ii8M-JlUrctKhlfTU5lty7d0UxVocNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: شکافی بین دولت و نیروهای مسلح نیست
🔹
دفاع جانانه نیروهای مسلح با پشتیبانی مردم و هماهنگی همه بخش‌ها، محاسبات دشمن را برهم زد. @Farsna</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farsna/454901" target="_blank">📅 22:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454900">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876ed831cb.mp4?token=EHtyNEQeRM9zUAsCO0E1qhvXcxEhtBXac_QaP8ICfLOGa-s9tPdvEp_mcglmfp7JumHbhbYksBW7cLUlwRq5hVNiFUVxjL8C-dRhQiDwpARYZW2HVXeQgOHdbA0kqD90Rnpzc9ZK9zy-QAtkUZl1FiN21uZtqx497p3mcDsNIUowmVX6NdczAUmsExmc9TSAj_E-R6Gzh_jBkkERjnTdpo1SQB_F9gNsPl0-uQp6OvcSbt3wPRPAzBypJ-cVhvRysQ_RWwl4eCHxEOg7BQJ53qc71uKi7CqwLBI1O9ax5hF7Ab2kQqicWrrPBw3rriE-Aq6NsaZ6o4n-p5v-wuHOwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876ed831cb.mp4?token=EHtyNEQeRM9zUAsCO0E1qhvXcxEhtBXac_QaP8ICfLOGa-s9tPdvEp_mcglmfp7JumHbhbYksBW7cLUlwRq5hVNiFUVxjL8C-dRhQiDwpARYZW2HVXeQgOHdbA0kqD90Rnpzc9ZK9zy-QAtkUZl1FiN21uZtqx497p3mcDsNIUowmVX6NdczAUmsExmc9TSAj_E-R6Gzh_jBkkERjnTdpo1SQB_F9gNsPl0-uQp6OvcSbt3wPRPAzBypJ-cVhvRysQ_RWwl4eCHxEOg7BQJ53qc71uKi7CqwLBI1O9ax5hF7Ab2kQqicWrrPBw3rriE-Aq6NsaZ6o4n-p5v-wuHOwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: در جریان مذاکراتی که با فرانسه برای لغو اسنپ‌بک شکل گرفته بود به تفاهم رسیده بودیم اما آمریکا نگذاشت.
🔹
اروپایی‌ها اختیاری برای تصمیم‌گیری ندارند. @Farsna</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/454900" target="_blank">📅 22:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454899">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293aa3d819.mp4?token=XE6_HUX_0Ws0WQOpWHVBGIBMOmE4sg9Qf2_RX1lLYetgNT_6n7fm1wMX93smj0MK2O1E36Kjg34sO32wY25e-2Wt-7sCSqjLooJ1A-pqtDjGK1c5uSrmqVFt9ywyiZcaTibH9t8hyjG-DKp5EXo_YLn7ruE8nfZhN3UxdebV9cWDKFZfX3_DEV6I1OtLxmb-c8Eom1THH8efYgE0CKkbF3aiq6cthsYQGM1R2KQBATFhQDYLEhvBs_eu_oHc_lPIjH_Aof84a7Vvw_0JPTf6j-2VjdajsO_Uz_gNFpQ8_1_HfJk90MIzZVEXCX8s2fX8devbH45gyJEsaCCWbjwgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293aa3d819.mp4?token=XE6_HUX_0Ws0WQOpWHVBGIBMOmE4sg9Qf2_RX1lLYetgNT_6n7fm1wMX93smj0MK2O1E36Kjg34sO32wY25e-2Wt-7sCSqjLooJ1A-pqtDjGK1c5uSrmqVFt9ywyiZcaTibH9t8hyjG-DKp5EXo_YLn7ruE8nfZhN3UxdebV9cWDKFZfX3_DEV6I1OtLxmb-c8Eom1THH8efYgE0CKkbF3aiq6cthsYQGM1R2KQBATFhQDYLEhvBs_eu_oHc_lPIjH_Aof84a7Vvw_0JPTf6j-2VjdajsO_Uz_gNFpQ8_1_HfJk90MIzZVEXCX8s2fX8devbH45gyJEsaCCWbjwgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: با امر و نهی نمی‌توان جامعه را به درستی اداره کرد  @Farsna</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/454899" target="_blank">📅 22:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454898">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cda7947ea.mp4?token=a1DBQegfcOvTrzk24vLw8BKnnzNZP31Vbl4VntSpoR51XZVNwv3qlwuAe-_KSgw4Ff9IdLsynV_LYkS0QCw-J7tIU474j5r8tG5FZ3TIQ7SXiqdvPKxn1aS4YJfEgIBTw3sb6oBFTVPI5OYVdeYSs0WyGB1DqZSwtiIB8yF-NHw3jRCr9_Ei4QAfid-WNSzoN5H-XqMd6zfzlQB1cccK3au_bCy_Asa4-D37ekEwFpCbjubJBdLdkX5QFIigCHCtUiZKB36-GfUXCVPWscgHrZL0V034A4QUn-xJ0rNVrxb9F3W1-SvYRF5OhsrNuVHw0lRHouEC2VnzOY4frVoqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cda7947ea.mp4?token=a1DBQegfcOvTrzk24vLw8BKnnzNZP31Vbl4VntSpoR51XZVNwv3qlwuAe-_KSgw4Ff9IdLsynV_LYkS0QCw-J7tIU474j5r8tG5FZ3TIQ7SXiqdvPKxn1aS4YJfEgIBTw3sb6oBFTVPI5OYVdeYSs0WyGB1DqZSwtiIB8yF-NHw3jRCr9_Ei4QAfid-WNSzoN5H-XqMd6zfzlQB1cccK3au_bCy_Asa4-D37ekEwFpCbjubJBdLdkX5QFIigCHCtUiZKB36-GfUXCVPWscgHrZL0V034A4QUn-xJ0rNVrxb9F3W1-SvYRF5OhsrNuVHw0lRHouEC2VnzOY4frVoqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: خیلی از مشکلاتمان با کشورهای همسایه را برطرف کردیم اگرچه آمریکا و رژیم صهیونیستی با توطئه و جنگ اخیر به دنبال ایجاد اختلاف بین ایران و کشورهای حاشیه خلیج فارس هستند.  @Farsna</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/454898" target="_blank">📅 22:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454897">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993ce56811.mp4?token=b0BIkwOZh7ESWUg_76mBf9fj2elYYMLPggKwUFsPYEF97zmmtmBLT2VxlygNAgUzx6gEWn_aUqbpmw1IeUmmpjvLKcSyiAtj3lADFMFRvs5BMqt-cF7hBjKMHExig-jUU5MzZGKV8cF35Lgrg4ybYp6JtC0mE6Sa-RNrJHNcnnBCQ0KSgKKjQ3TFgtWgXGLnPhB30pruDNOa3BgO_vjg6J6dnEKkyikb-RW7ku4sBKgt7JDFUlc5qt94EVx_SMqMNwgtQdSNZS7K2X7KRG8B7BHrOhYVTHG3thcN1u1pDxGJOH8VGv3Gtc-PWtvitaGYNxmR0_wghHaKzo3mPKqk0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993ce56811.mp4?token=b0BIkwOZh7ESWUg_76mBf9fj2elYYMLPggKwUFsPYEF97zmmtmBLT2VxlygNAgUzx6gEWn_aUqbpmw1IeUmmpjvLKcSyiAtj3lADFMFRvs5BMqt-cF7hBjKMHExig-jUU5MzZGKV8cF35Lgrg4ybYp6JtC0mE6Sa-RNrJHNcnnBCQ0KSgKKjQ3TFgtWgXGLnPhB30pruDNOa3BgO_vjg6J6dnEKkyikb-RW7ku4sBKgt7JDFUlc5qt94EVx_SMqMNwgtQdSNZS7K2X7KRG8B7BHrOhYVTHG3thcN1u1pDxGJOH8VGv3Gtc-PWtvitaGYNxmR0_wghHaKzo3mPKqk0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: مساجد، مدارس، مراکز بهداشت و شهرداری‌ها پایگاه‌های عملیاتی هستند که دولت می‌تواند برای اجرای برنامه‌های خود در سراسر کشور از آن‌ها استفاده کند. @Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/454897" target="_blank">📅 22:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454896">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d09c66ced.mp4?token=H0aFxPACBVKG-5FzcUhNtNbVNBf3aQCeqhZLjOAydiTBMhHMR0f9J4ZZSMITw8HN_AnV6-TBpbdNxy6BXHWpxtCffBcIXHJ6cYL0fZwx87eoXe1gBSIhaoRwK7KvKybg7zzPCQp70k7O1VGJ6dmdFFhTJUKHgF9HI71_yeX2xzkiG5KiFfoEj2diOFbDZI5tiX8oYc4WqprjVeLId9bquF-KUhTCkNgnVgPxJOmK6e-j2eRfNLuhAH54-tNGxWgeq9gV956V8uOw_sqXd9RIwclPD-c8nwUed9pY0JUdAufLEcvK0_ApxsgqRLEwPX4QQu2o4LbmR5fj5Q9PQyyuNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d09c66ced.mp4?token=H0aFxPACBVKG-5FzcUhNtNbVNBf3aQCeqhZLjOAydiTBMhHMR0f9J4ZZSMITw8HN_AnV6-TBpbdNxy6BXHWpxtCffBcIXHJ6cYL0fZwx87eoXe1gBSIhaoRwK7KvKybg7zzPCQp70k7O1VGJ6dmdFFhTJUKHgF9HI71_yeX2xzkiG5KiFfoEj2diOFbDZI5tiX8oYc4WqprjVeLId9bquF-KUhTCkNgnVgPxJOmK6e-j2eRfNLuhAH54-tNGxWgeq9gV956V8uOw_sqXd9RIwclPD-c8nwUed9pY0JUdAufLEcvK0_ApxsgqRLEwPX4QQu2o4LbmR5fj5Q9PQyyuNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با مشارکت خود مردم در محلات مشکلات نیازمندان را برطرف کنیم  @Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/454896" target="_blank">📅 22:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454895">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/485f4ea84f.mp4?token=P1NXQq6V_NlTXCpk_NpFYnGASziO4KSaOs4niIYoF8cwknbBuwUO9HkcCadnx_s6sghpW3Btidf4iD9SqsgLp9QNKfId-7wsm2jvgDIDTYN1-mp9j3V181hIb_lBsL5E_rIdkzZKNfSAH6RnjLkx4ioB2Ty8sX4dfSUQZWMYAHcq1CZOui9ohO3H3e4fP83ktFVvZHPBnJdAPaC00SsxPk3XboygAm-uzfCoT-NZXaA-RucviBEgPA679d3OYNO2q72h2f7QHqEVLS7qAIh5Q52KybLuGLaxLDLTUfOwVIWC5nBveadL_p7szBLWnzAzbeannQ8trBhHRx_U5roRIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/485f4ea84f.mp4?token=P1NXQq6V_NlTXCpk_NpFYnGASziO4KSaOs4niIYoF8cwknbBuwUO9HkcCadnx_s6sghpW3Btidf4iD9SqsgLp9QNKfId-7wsm2jvgDIDTYN1-mp9j3V181hIb_lBsL5E_rIdkzZKNfSAH6RnjLkx4ioB2Ty8sX4dfSUQZWMYAHcq1CZOui9ohO3H3e4fP83ktFVvZHPBnJdAPaC00SsxPk3XboygAm-uzfCoT-NZXaA-RucviBEgPA679d3OYNO2q72h2f7QHqEVLS7qAIh5Q52KybLuGLaxLDLTUfOwVIWC5nBveadL_p7szBLWnzAzbeannQ8trBhHRx_U5roRIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: باید با مشارکت خود مردم در محلات مشکلات نیازمندان را برطرف کنیم
@Farsna</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/454895" target="_blank">📅 22:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454894">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اعتراف شرکت نفت امارات: ۱۵ نفتکش‌مان منفجر شد
🔹
شرکت نفتی امارات، ادنوک فاش کرد که از ابتدای جنگ رمضان، ۱۵ کشتی این شرکت هنگام عبور از تنگه هرمز مورد حملۀ موشک و پهپاد قرار گرفته‌اند.
🔹
این شرکت تایید کرد در هفته گذشته ۳ کشتی مرتبط با این شرکت هدف قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/454894" target="_blank">📅 21:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454893">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJshEFpq0ogYr7zZwbgl5UjXhj_pJKhGScy9lA41824jzh7CzbYBPQuzU0DOR9MayLYpT50JLZOokL7i1utw8cu9YIBYlH9ijK6DFuSXxmp4XskXlOrQ7mFjnRiU91MO4YcXAwgz869aeH0qw321i6q6GqJ2sAjJGCRH0bR445epd2v0e98nmCp7o2XaygMDIFrq0zrIz2iHVri75R8d-Plp8nYxgoNksbJ2dkJ6Kle1QTNtnlXDVMyuzNbrMsSf3ZqtG6XjZR1eTA82VVJWE3SOVhiAMViiSNec1texzfas1cNsBr_h6WPP59PIUM8e6mSOrFSYVxIR4vZ5G-HJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی خطاب به کشورهای همسایه: زمان آن رسیده که به خود متکی باشیم و برادری واقعی را درپیش بگیریم
🔹
نیروهای مسلح قدرتمند ایران، آمادگی، توانمندی و اقتدار خود را در برابر پیشرفته ترین نیروی نظامی جهان به اثبات رسانده‌اند.
🔹
هنگامی که مسلمانان در کنار یکدیگر متحد و یکپارچه باشند، می‌توانند در برابر هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، با قدرت و قاطعیت ایستادگی کنند.
@Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/454893" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454892">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8b23c4b0f.mp4?token=LI-YvQYIDvYTruyPxdunIsM2KMmhMF27QinpajaJlx8Dm3FfJYP5oipdqa9pyV1e3yrtOJVFO420gTfWqtOrz4isy1s-8QjpbzqYt1HJaXsjBq5UsC_LBpdMplBMmVAzpwYoU-I3tWrgjQj5dpGbBcFCUUqbSuwhgdvPqixFm7pKySJegDR98QiyPzI83ImEXaSSoDELh06aThLo6vioB2Nx9kPwD947w6JadTPPqGwdiihGmiI-U-7abeJJhNLI4dZ26DX60vGQig8BitfFYYNRLV_sHO5iHVrTo3aVthMIpaFaLJdaYD9mnshlMlX-fOgfesiJDm2m6XTygnQV8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8b23c4b0f.mp4?token=LI-YvQYIDvYTruyPxdunIsM2KMmhMF27QinpajaJlx8Dm3FfJYP5oipdqa9pyV1e3yrtOJVFO420gTfWqtOrz4isy1s-8QjpbzqYt1HJaXsjBq5UsC_LBpdMplBMmVAzpwYoU-I3tWrgjQj5dpGbBcFCUUqbSuwhgdvPqixFm7pKySJegDR98QiyPzI83ImEXaSSoDELh06aThLo6vioB2Nx9kPwD947w6JadTPPqGwdiihGmiI-U-7abeJJhNLI4dZ26DX60vGQig8BitfFYYNRLV_sHO5iHVrTo3aVthMIpaFaLJdaYD9mnshlMlX-fOgfesiJDm2m6XTygnQV8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۶۰ شب حضور فاروجی‌ها در سنگر خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/454892" target="_blank">📅 21:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454891">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHIB3-LUNiKxKbSENXLoH83-xDJzikjTFhsfqD8sM3daiWRZDxLunqHHMJELq4OCEvmE1QdD_PFHSYBjNTIv69zE2yfH5AYCKa4VXr-kgwr8nR0rZ25Ii5F-HsIKXJmO5Ri78-7MuSqlTukS_ZWl0JNdFX558W5eWbVUKgb_UbJWh-8PSV9_Rt5-dS9f12tn1SvzSq9h58_tmYrmw1yFQ4KEjkDgTSqVOe_0nnlCZSTwxNbfhaIZUkmuRXUJL-lLFUkVoZwA6EYeOD62xFV_OApcyzqRX6TtrpF3kZJ5ooBJ95NW1QlJ-udKV459ottF-lvNkNat1kB1dxCdFt1IcYS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHIB3-LUNiKxKbSENXLoH83-xDJzikjTFhsfqD8sM3daiWRZDxLunqHHMJELq4OCEvmE1QdD_PFHSYBjNTIv69zE2yfH5AYCKa4VXr-kgwr8nR0rZ25Ii5F-HsIKXJmO5Ri78-7MuSqlTukS_ZWl0JNdFX558W5eWbVUKgb_UbJWh-8PSV9_Rt5-dS9f12tn1SvzSq9h58_tmYrmw1yFQ4KEjkDgTSqVOe_0nnlCZSTwxNbfhaIZUkmuRXUJL-lLFUkVoZwA6EYeOD62xFV_OApcyzqRX6TtrpF3kZJ5ooBJ95NW1QlJ-udKV459ottF-lvNkNat1kB1dxCdFt1IcYS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای بازگشت یک زائر گم‌شده در سفر اربعین به ایران در برنامه پرچمدار
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/454891" target="_blank">📅 21:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454890">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHNQ8olow8wQtzSflRxguDWb3_NPeJF2RteXxi0njo08_UaYUihwvTgRzQZfUqRWOzBrIrYS0qTHU0NPG9WzsNO78LgtlGylQGbYxmZK2p0o_bQChw8JZqnoR-fsRvCyZZpdjnxlM2gVRAiShkNPtMIpT4JroFviSZMcArJJOTBUVU7bESF1K9gmTlVEJnjP4FtpGCrhroHQkJa4GRSroZDglOCg6ePHMOX69UcETsv8Ndze3tChf97iojbahMcXMo_OffJdlEpWfOs3rN4tsDFyuK48TgEdH6Uig9SUsjpV7GrhquK1rDvTq-FYvzJrtg7a89NIR3b3d0Fv_DdLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت عراق به محکوم کردن تجاوزگری آمریکا و عربستان اکتفا کرد
🔹
شورای امنیت ملی عراق در نشستی اضطراری به ریاست فالح الزیدی بدون اعلام اقدامی عملی، صرفا به محکوم کردن تجاوز هوایی آمریکایی-سعودی به مقرهای الحشد الشعبی بسنده کرد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/454890" target="_blank">📅 21:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454889">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87e079e9fa.mp4?token=kCmFpt6AZfk_joG9VMDOlustcimIx2TX2Pquv70-kZv-iNWtEgSnFiD5zcIwfJGAM856zx33TugV6nKUgeMjz5Mgq_VZ28MqBzRhl68Fs-gKkSK0vR8NfsjOUSlPRTSkj37XHFCtfXGWGRCusNYwc1eZO_zAQJ2cswWKQoNMJcw6ukTTLofgUoM5vwB5SRILZCjo9jN1j8NxkbiTDVudXRQ9sDX8O3Ommli-FpLDd3kxUelo9tgVLRLvADGo9egOuPmxcw1-wu48mhNaNscPLbV84QduUKqLD_Q6-644XGHVgWnEtiQMO55XBCGCJOk7b2tfXTM0Xh1gQNFSBbMNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87e079e9fa.mp4?token=kCmFpt6AZfk_joG9VMDOlustcimIx2TX2Pquv70-kZv-iNWtEgSnFiD5zcIwfJGAM856zx33TugV6nKUgeMjz5Mgq_VZ28MqBzRhl68Fs-gKkSK0vR8NfsjOUSlPRTSkj37XHFCtfXGWGRCusNYwc1eZO_zAQJ2cswWKQoNMJcw6ukTTLofgUoM5vwB5SRILZCjo9jN1j8NxkbiTDVudXRQ9sDX8O3Ommli-FpLDd3kxUelo9tgVLRLvADGo9egOuPmxcw1-wu48mhNaNscPLbV84QduUKqLD_Q6-644XGHVgWnEtiQMO55XBCGCJOk7b2tfXTM0Xh1gQNFSBbMNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رگبار باران در ارتفاعات مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/454889" target="_blank">📅 21:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454888">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">درس ماجرای مصر و «لحظۀ سوئز» برای ایران
🔹
سال ۱۹۵۶ جمال عبدالناصر رئیس‌جمهور مصر کانال سوئز را ملی اعلام کرد. این آبراه استراتژیک که خون حیاتی تجارت جهانی بود، تا آن روز توسط شرکت فرانسوی-بریتانیایی اداره می‌شد.
🔹
واکنش پاریس و لندن به عنوان ابرقدرت‌های ان زمان، تند و خشن بود و بریتانیا، فرانسه به همراه اسرائیل دست به حملۀ‌ نظامی به مصر زدند؛ هم‌زمان دارایی‌های مالی مصر در بانک‌های غربی بلوکه شد و کمک‌های خارجی، یک‌شبه قطع گردید.
🔹
با بستن کانال سوئز، مصر جنگ نهایی را برنده شد و این «لحظه سوئز» بود که در آن پایان عصر قدرت فرانسه و بریتانیا رقم خورد.
🔹
مصر گرچه امروز با واشنگتن متحد است، با اسرائیل صلح دارد و تحریمی در کار نیست اما اقتصادش همچنان در تب است و بدهی خارجی از ۱۶۰ میلیارد دلار عبور کرده است.
🔗
ماجرای آنچه بر اقتصاد مصر گذشته و انتخابی که پیش‌روی ایران است را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/454888" target="_blank">📅 21:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454887">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad891b3e3b.mp4?token=sGX_U5mmM0bZzWfi6nFjLFbxZvVxAJjSkrrmGi6OOjLFzG8hRIusA6SHRKFIUz9hGzVOAkzPBrWPbPA4ty-xDwRBm76T_WD9p08OKWZQZBjWDsEjN2bH_omntjJEMUbh7A5HTN7Xk53BZQZvUcxv-vsuxzGsPUAp_uNaB0pjZMehn7R7Ql6F_D59dKHxSVKCv2EtVMaj0urqcrHfbJsP57IaEkQOwvrF2si8uoGHlWAh1Cz-oL7lTHKgwnTQXzlzgfZtng9_BJkj1or7ln7FQjGweQ9dOm23pIoj8PaCzqdojmcSbIpPGdvuzf2hMjQAHpl-IdVx4BpiwzKiddrSipwbliRtdwtcUbtmIyt3OqZ_U1SxhpRuNj4Rhp8ODXPEJaqIXM_CCJVT_ipOsH14B_XQshrREoTZnRiw5R9QTmdMtICgS4SOpgpG6zO-wkwHaC6N245MM4n70gu_TJbMa_gnQG3FDZ0N7pXkJFlborseC1gEVRphxRGnh5H20RvvQ3Va-wA68IHpqf-oG6V1KIsekdfo6shBboER28fm_bwofgYNBuYVUSzdr7aTO1vIsSEio8dlIUZLSDreBXyViULoX3bf-Ccl08W9oGNFq0KWnttGdkrG7_sNj4G_AZeMOu1dKpVhH2_OowqITcgMXJL8yCmVM8GxY9C4qSA6TtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad891b3e3b.mp4?token=sGX_U5mmM0bZzWfi6nFjLFbxZvVxAJjSkrrmGi6OOjLFzG8hRIusA6SHRKFIUz9hGzVOAkzPBrWPbPA4ty-xDwRBm76T_WD9p08OKWZQZBjWDsEjN2bH_omntjJEMUbh7A5HTN7Xk53BZQZvUcxv-vsuxzGsPUAp_uNaB0pjZMehn7R7Ql6F_D59dKHxSVKCv2EtVMaj0urqcrHfbJsP57IaEkQOwvrF2si8uoGHlWAh1Cz-oL7lTHKgwnTQXzlzgfZtng9_BJkj1or7ln7FQjGweQ9dOm23pIoj8PaCzqdojmcSbIpPGdvuzf2hMjQAHpl-IdVx4BpiwzKiddrSipwbliRtdwtcUbtmIyt3OqZ_U1SxhpRuNj4Rhp8ODXPEJaqIXM_CCJVT_ipOsH14B_XQshrREoTZnRiw5R9QTmdMtICgS4SOpgpG6zO-wkwHaC6N245MM4n70gu_TJbMa_gnQG3FDZ0N7pXkJFlborseC1gEVRphxRGnh5H20RvvQ3Va-wA68IHpqf-oG6V1KIsekdfo6shBboER28fm_bwofgYNBuYVUSzdr7aTO1vIsSEio8dlIUZLSDreBXyViULoX3bf-Ccl08W9oGNFq0KWnttGdkrG7_sNj4G_AZeMOu1dKpVhH2_OowqITcgMXJL8yCmVM8GxY9C4qSA6TtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفتگوی بدون تعارف با آتش‌نشان بِهشهری و فرزندش که جان یک کودک را نجات دادند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/454887" target="_blank">📅 20:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454886">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWb919leniH6mC8KrG8y0thLsYoJPW4ay3vdIS1ZiMTBPJOWHO1ApHWr7Tf9KHrLeF2VwIC5DnTYJ3SJAoWSmvQ4YBBQzu1bfJdiKjv2wB-oLSogdMypBebq0NG49EP9719dcahzdlYm9JCoYoev-1XwRjiucVKpK9GprEwdR0HFJ1V1JKeZyRI2fq2ohW1qJgtBSN1NWos9il-syd240Tbsll6elaJ7pXkWUeE71m2QwK0cV_Ql8fU8O8sar_s3_Y6iiNNvrhP0RiUBzoTAISTRC52ztVZZHUsFo4QwEFsSXtZltVaAoXZRJ5fZV9gd17wZRoTjEy-uX2KDRVLCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
شمارش معکوس انتقام
@Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/454886" target="_blank">📅 20:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عملیات جدید یمن علیه پایگاه‌های سعودی
🔹
شبکه المیادین اعلام کرد که اطلاعات اولیه حاکی از آن است که نیروهای مسلح یمن یک عملیات جدید را علیه اردوگاه‌های سعودی انجام داده‌اند.
🔹
در همین راستا، نیروهای مسلح یمن اعلام کرده‌ به زودی بیانیه‌ای در این خصوص منتشر خواهد…</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/454885" target="_blank">📅 20:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7rlm1Lqnqe-VY-RTKMp_P0ufAs7fHbXtkDa8Qp_O19yGI6JS7zphQEgvVXZqAvgSTzOpcF4dAX_wxY_TkrrsvIsYTgZr9zXJCWwq6QYUmBeVVxHpM8arOzjwuGMopPi_L55aAAvDbiI4kURRb-qacIjxjSIOSz2FyrNgYahJYj_MZ20Bw0givvK_bp5B8eu6O1yffLz4kEwrZCMg5yjDFAD3DtEQqpZg1nfry9zgdujYXKexSqOpF3DQf049D3M4Evc29dn0K02TvRKt7Sj0S4hVkOpA5o8IWCpX-eRLOI_PUnfIDQ_b21xWyyjk1U_PIPY_i1PA93IJCSpGe7UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنایه بقایی به توهم نفتی ترامپ: اول باید واقعا پیروز شوید نه اینگه در هرمز گرفتار باشید
🔹
سخنگوی وزارت خارجه: رئیس‌جمهور آمریکا مدعی شده: «ما مقدار زیادی نفت از ونزوئلا می‌گیریم؛ میلیاردها و میلیاردها بشکه نفت؛ و همین کار را درباره جمهوری اسلامی ایران نیز انجام می‌دهیم.»
🔹
پیش از آنکه بتوانید مدعی غنایم جنگی شوید، باید واقعاً در جنگ پیروز شوید؛ نه اینکه در یک تنگه گرفتار شوید، در دستیابی به اهداف (شوم) اعلام‌شده‌تان ناکام بمانید، با کمبود تسلیحات مواجه شوید و در این مسیر اعتبار خود را نیز از دست بدهید.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/454884" target="_blank">📅 20:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454882">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌
🔴
مقاومت اسلامی عراق: پاسخ ما به عربستان و آمریکا قطعی است
🔹
برای حفظ امنیت زائران حضرت اباعبدالله الحسین(ع) و خادمان موکب‌ها و جلوگیری از هرگونه اخلال در مراسم اربعین، پاسخ ما به تجاوز آمریکا تا پایان این مراسم به تعویق خواهد افتاد؛ اما این پاسخ قطعی است…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454882" target="_blank">📅 20:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454881">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4iD5QV0XKPS8QaK6bapudKTCZQHq4_l3J7XQNZvpznFzVOj9hi4j71xyRP-e5Xa05wcrUPTfEwv84vhIkBtP8dVtOtDw2VWGesFcwf7tGfd5NwH84YPrWzdQKy5jPuKSMzCW0gOt3CeAMp6SBqWJGw832X6eS23kD1azbtDqFVNSla1prMW61S41e8GaAvrtGZspVQUzx4LQlCO226VW30aDAh82tUgFDnkRNzy32wO0GNjUffrgzsU7xpuuahFGkuKJdfE4c3m1E-51_z8Ii1_bowCAqoz1iR63vLhck-OGQapOARi5qcwkOhmuGsOWP4jcoWdSrjNvp8QU5zo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«بازی مرکب» دیوید فینچر در نتفلیکس متوقف شد
🔹
گزارش‌ها حاکی است پروژه مورد انتظار دیوید فینچر برای ساخت نسخه انگلیسی‌زبان سریال محبوب کره‌ای «بازی مرکب» (Squid Game)، از دستور کار نتفلیکس خارج شده است.
🔹
در واپسین صحنه از فصل سوم سریال پربیننده نتفلیکس، شاهد مواجهه‌ای معنادار میان شخصیت منفی سریال «فرانت من» (با بازی لی بیونگ-هون) و زنی ناشناس از لس‌آنجلس هستیم؛ شخصیتی که با بازی کیت بلانشت ظاهر می‌شود و ظاهراً مأمور جذب شرکت‌کنندگان برای نسخه آمریکایی این بازی‌هاست.
🔹
بر اساس این گزارش، نتفلیکس احتمالاً به جای این پروژه، توسعه نسخه‌های محلی و بین‌المللی دیگری از «بازی مرکب» را در اولویت قرار داده است. نتفلیکس و نمایندگان فینچر تاکنون واکنشی رسمی به این گزارش نشان نداده‌اند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454881" target="_blank">📅 19:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454880">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وزارت خارجه آمریکا از وضع تحریم‌های جدید علیه ایران خبر داد
🔹
وزارت خارجه آمریکا در بیانیه‌ای اعلام کرد اقدامات جدیدی برای قطع مبادلات مالی با ایران انجام داده است.
🔹
در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/454880" target="_blank">📅 19:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454879">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2cc38f78d.mp4?token=R0sR7Y6_K-e2DNwwWFGbj6B0bKXCLoytHaIUXMUMGiFxhqnxCDoZEwU8Qb16dq54bwrcw1tkqY3NUcTX-2QNe4zzNbJwz3gxYVy51WIheQqNpykg46qb3aPE8UKcKya1tmzOlBtMTVjwweRygsEcBfB9aKl0Y1v1ycfweyUpbquWMo88O9GVZPMPps5-JXkWlSrp734oi1lp7tMJ1uW1DxtVXavvKmaTLXF-MW8Q5hHrtDnnG5hm7jFLlyxTHp_ohN-K52z1RlPcz77lAq1UFS2uf3cop6ZwibkRGEB-tDLomRhJFI_qqi2-SZium1aFI3YY1gMByNFkYGLqYm2aHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2cc38f78d.mp4?token=R0sR7Y6_K-e2DNwwWFGbj6B0bKXCLoytHaIUXMUMGiFxhqnxCDoZEwU8Qb16dq54bwrcw1tkqY3NUcTX-2QNe4zzNbJwz3gxYVy51WIheQqNpykg46qb3aPE8UKcKya1tmzOlBtMTVjwweRygsEcBfB9aKl0Y1v1ycfweyUpbquWMo88O9GVZPMPps5-JXkWlSrp734oi1lp7tMJ1uW1DxtVXavvKmaTLXF-MW8Q5hHrtDnnG5hm7jFLlyxTHp_ohN-K52z1RlPcz77lAq1UFS2uf3cop6ZwibkRGEB-tDLomRhJFI_qqi2-SZium1aFI3YY1gMByNFkYGLqYm2aHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عصر بارانی تابستان در فاروج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454879" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454878">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
تصاویر جدیدی از توقف کشتی‌ها در شمال تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454878" target="_blank">📅 19:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454877">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJR0BA7aTwcGDaGzb5BQHygIR0j5JAn81YbVK0Wr5-hUtP1K93bNK-lyjC-ABarvva9x7jr2x2-sssmvK83lEFTjJm5S9SVT0EKRghrgn0VqKKQL5JSONLqLqXCmDmXkd2GoRegJjJx0O7S7hJkI6vJ-jn2okq8vorjDdQiEmcSyUAY_XaP7LszGcgy2_ZABip96C2g6O6zpaJhuXyvzYbY2pVj9wZ3XjeDLbR7pKMEpOGA0kaTLbZ14IrgeMXvzCRBKoegd95QBYBL3XDReS7dOX7rMBIb2GpPBOK76XNIlVvvIquAzP5cgteDS66fmh297KfF5bLg4F89nA9m0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید یمن به سرنگونی نظام حاکم بر عربستان
🔹
وزارت امور خارجۀ یمن به مسئولان عربستان سعودی هشدار داد که اگر به سیاست‌های استعماری خود ادامه دهند، باید منتظر نابودی نظام حاکم بر این کشور باشند.
🔹
یمن تأکید کرد عربستان با فعالیت‌های استعماری خود به سمت مسیر بی‌بازگشتی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454877" target="_blank">📅 19:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454876">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib1A-l8OMTWDIquJ-mTqGTpKIJ78gK6P6yf3Y1tN9Hd7LjG8PaDL0njkitkYsQkgYnOUXQ6SQz-hxC84YxDrD2M8kRruX4v3ytE34aZYDRL07z5VXo8YgmmPTiO_y7fas5A8yDiPEF5L5k5fRsqEoNgLOUJ3xCBqkkLvzt8AcOx7mUE_RoQ6m93tF4624BL48I06LuAdFuVT14Tq3jESuJiavEmf7csfU5QN4C-jGd6f3GpeATpkpP1NOWYsBl1pH5vmUVYjF9v4OULM0OvIYA7vuYz4X1DQ1CjP_8k5u1Nay67VF07GB3998TF3H1BCM0zlZ-9DmGJcK-Hpown3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقم تاریخی اجارۀ کشتی برای انتقال نفت عراق به خارج از هرمز
🔹
رویترز می‌گوید که شرکت «ریلاینس اینداستریز» هند برای اجارۀ یک ابرنفتکش برای حمل نفت خام عراق بین ۲۳ تا ۲۵ میلیون دلار به یک شرکت کره‌ای پرداخت کرده است.
🔹
پیش از جنگ، هزینه اجاره چنین نفتکشی حدود ۲ میلیون دلار بود، یعنی هزینه حمل‌ونقل از مسیر خلیج فارس اکنون ۱۲ برابر افزایش یافته است.
🔹
رویترز می‌گوید اسنادی به دستش رسیده که عراق برای ترغیب خریداران به بارگیری نفت از پایانه‌های داخل تنگه هرمز، نفت خام خود را با تخفیف ۲۵ تا ۳۰ دلار برای هر بشکه نسبت به شاخص عمان-دبی عرضه می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454876" target="_blank">📅 19:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454875">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Awu6DTWRUI9YOUoxG0ldXs_6WWUWoxnIjag8Y9J0Q_2EFQHhZRhWWZEUaTvnNRQkni2OCdZjjAcmqmltBqBdi5sP0U1MHAUZSjwF-W5i6hEH_hyLOLJpKXapJ9z66DMFRxUoGLvmmOvXe9eQX1YBWu3sLETt6DB7jMUaANaVT4LuwCqyIfH3DYlxD6GWBgLxgfRZSMaWZ_kMOHiasNiXFys8VK_NOKrGZKCjJmzYPg1ZLMBilARy4_T8Phug5Q8dxD9WD2lSdLlcU-mRPMwjs7G0yF8RWfBndZOMVQ3jtBVnRHwC77eXtCIVx-NKpMBHz0_GIJTaoIQgvrWh0SW3QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظرفیت نیروگاه‌های تجدیدپذیر ۴.۶ برابر شد
🔹
وزارت نیرو: ظرفیت نیروگاه‌های تجدیدپذیر کشور به ۵۸۰۰ مگاوات رسید.
🔹
این میزان که در ابتدای دولت چهاردهم ۱۲۵۰ مگاوات بود، اکنون با رشدی ۴.۶ برابری همراه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454875" target="_blank">📅 18:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454874">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سازمان سنجش: نتایج آزمون‌های ورودی مدارس سمپاد و نمونه‌دولتی اوایل هفتۀ آینده منتشر می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454874" target="_blank">📅 18:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454873">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6sKmJhd0J4E2F3v2KQdAkZlWxsIsMg15wlo6llT5WRgc8O-OiITojcaM1gmgyHs33IvL0X6Ls55pupDBDTMzYOlxoYfg41UBYEkRE0fw3TOTATmLmV_QYlst8pIY0_xPIGnItXEhfoGYwZx_IEjqxQCU6SSaRUhUy7ESeF4KCcjGjDljKfbzQo095kM5tGxK_oOidkpBmDFZ9DUBznj7Mu_yCUquXei5L9pRA4bouhCrhwd4sRH-7g6baFOSOT8u6tgz1TXeY6ZOdCiedADfKd-NQSZG-VUe4BcEFa6AHFVfEJ1kt4dHYChYb4-TaNJmKqIlim0jWAfp3ikOfKUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ۴۳ روز تا مرگ نفتی فاصله دارد
🔹
بر اساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیرۀ‌ استراتژیک نفت ایالات متحده به کمترین میزان از سال ۱۹۸۳ رسیده است.
🔹
این ذخیره هم‌اکنون تنها معادل ۴۳ روز مصرف نفت خام این کشور است و اگر نفت جدیدی به آمریکا نرسد این کشور با کمبود نفت مواجه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454873" target="_blank">📅 18:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454872">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PX7z2ACfIQi00UtdZkt5FZU8f41C4zRq-s2gRrNtDzKuXxVFDv5PQ81XSqI3rEnxh3KfyS5IwvFZL1xdnZi_n0RZZn6bJFtLcVUZaAZFmB4fr4pmxwiHHHkDSV5-df5clTf1AiHuqOMLgvaykilU_Ws9gnxFitPS3S8B8qnc4e_DljuCxg2hirnkvA4cIcUryPuRweURlf3B9gYyDtc9twj70aj59NtIL-OlJmSZb_aS9ltJYl4ottj1gPGeQtqSGiWvh323yB9nK8AZZx26HXyIELshIVmvL0PCtY87zAt7h28rOkG0sywg4JEeI4-hTnEP1V4K_JtaFrJAi8ahdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات جدید یمن علیه پایگاه‌های سعودی
🔹
شبکه المیادین اعلام کرد که اطلاعات اولیه حاکی از آن است که نیروهای مسلح یمن یک عملیات جدید را علیه اردوگاه‌های سعودی انجام داده‌اند.
🔹
در همین راستا، نیروهای مسلح یمن اعلام کرده‌ به زودی بیانیه‌ای در این خصوص منتشر خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454872" target="_blank">📅 17:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454871">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deebb7c7d7.mp4?token=dM-pLR7Q7GVdOC2VtGp3i2nvE_LReHvBHIsMum9yDhSKyjDSGmwSR7cXqpAlOfQATrf8KAxJGviub1LrVYQN7kB4YtPrsBXBeW0GC8RHPGnZA_ByN8DIsj-4ZChG0TjDh0l-gLQsx_uGU0RySlab4ZNhc4oxf9wboS0FXs_5RMl3xWp-Z6Hh43C96p6XyiIiXsmwrfhY4X-xyTNZbg3o9qv8lnKFRy1XHrMG7XBAMbSPmCoEdQmTqcNIzSuVKeuK5ZBuKnX0r98x6RiEr9e8LwS1xvCYX7sMK6gBEULwFmZH1YrwojlWYt13zN2bz8llqZDIYMlwKheRXFj2UTfE6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deebb7c7d7.mp4?token=dM-pLR7Q7GVdOC2VtGp3i2nvE_LReHvBHIsMum9yDhSKyjDSGmwSR7cXqpAlOfQATrf8KAxJGviub1LrVYQN7kB4YtPrsBXBeW0GC8RHPGnZA_ByN8DIsj-4ZChG0TjDh0l-gLQsx_uGU0RySlab4ZNhc4oxf9wboS0FXs_5RMl3xWp-Z6Hh43C96p6XyiIiXsmwrfhY4X-xyTNZbg3o9qv8lnKFRy1XHrMG7XBAMbSPmCoEdQmTqcNIzSuVKeuK5ZBuKnX0r98x6RiEr9e8LwS1xvCYX7sMK6gBEULwFmZH1YrwojlWYt13zN2bz8llqZDIYMlwKheRXFj2UTfE6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه نفت اسلواکی منفجر شد
🔹
انفجار در پالایشگاه نفت اسلونفت در شهر براتیسلاوا، پایتخت اسلواکی آتش‌سوزی گسترده‌ای در این تأسیسات به راه انداخته است.
🔸
در ماه‌های اخیر پالایشگاه‌ها و زیرساخت‌های انرژی در اروپا و اوراسیا هدف قرار می‌گیرند؛ از وقوع آتش‌سوزی در پالایشگاه‌هایی در اروپای شرقی تا تاسیسات بزرگ نفتی روسیه.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454871" target="_blank">📅 17:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454870">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67424e7ac.mp4?token=FGVujq2lmGLh-62ReaAnTumSlWG3Od2RjGrZ9LTxumtxYsC_ZYfZYa2iRjU1Nal1YosdwKjY-8L1FAlS4GnZAaTBpz49YuA14q6-HorRej3ZwfbVxD4h6ede8r2tW59Qthh2osnNXSYWy8WNOW2VcPEUpoFM96HabggRJq2hNumkrzRLtMCy5fP4dvfP49tr_RbJzwCr8BIS6YjNLcVy7eT-52x0WEAmV_rn4q0E5iq6e-BN3I-w8VqzaJe5KkzM6VG3P-jrylz360YT8qPzKSKJbNpQGMqlP6oss7U7EuNPMtp0R9kfbH-0cw9zV7ojRLIaqSOREPaEKbbDi6RN9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67424e7ac.mp4?token=FGVujq2lmGLh-62ReaAnTumSlWG3Od2RjGrZ9LTxumtxYsC_ZYfZYa2iRjU1Nal1YosdwKjY-8L1FAlS4GnZAaTBpz49YuA14q6-HorRej3ZwfbVxD4h6ede8r2tW59Qthh2osnNXSYWy8WNOW2VcPEUpoFM96HabggRJq2hNumkrzRLtMCy5fP4dvfP49tr_RbJzwCr8BIS6YjNLcVy7eT-52x0WEAmV_rn4q0E5iq6e-BN3I-w8VqzaJe5KkzM6VG3P-jrylz360YT8qPzKSKJbNpQGMqlP6oss7U7EuNPMtp0R9kfbH-0cw9zV7ojRLIaqSOREPaEKbbDi6RN9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رونمایی از مختصات جدید تنگۀ هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454870" target="_blank">📅 17:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTklnj3Pq56m8zUiOELdUcE5XhJK3pCcpi1mW-IcvYfQ3zPBlpXeAZzOlZ0FWzrGxLcH7cQOX-e7MsvHz6GkVfg2CdVCxkE2GQfG6du7KsBWpSblpZrZuBOKLV5b-A5_0cnXrX4MygjEVqcuh9YEDjjE-olFA7sdPmdQ3wjOvWEMZiwo9pjAqq-zXrsnrhO81eyJ1dXQtC5vMGMKSb4iV2QWcA-o6EahXUw9NG0JUwT-ZfrPoFsQPArcofpr43Rsv6KLwA3yDmXDmy9wR81mWv6Itl1l6-lVXyoMl4AJ8LYw3O1iDuE8VdXnV96mYPhyhaVbwKDTFxjyIqWBCMh_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلارزدایی چینی‌ها با خرید تاریخی طلا
🔹
جدیدترین آمارهای رسمی دولت چین که امروز جمعه منتشر شده است، نشان می‌دهد که پکن ماه جولای ۲۰ تن طلا خریده که بیشترین میزان در سه سال گذشته است.
🔹
از ماه مارس که جنگ علیه ایران شد، خرید طلا چین هم افرایش یافته است و ماه گذشته هم ۱۵ تن طلا خرید.
🔹
یک ماه و نیم پیش بود که آمار شورای جهانی طلا نشان داد حجم طلای نهادهای دولتی بالاترین میزان در نیم‌قرن گذشته است و آمارهای بلومبرگ هم از پیشی گرفتن ذخایر طلای بانک‌های مرکزی جهان از دارایی‌های دلاری حکایت دارد.
🔹
آخرین آمار وزارت خزانه‌داری آمریکا نشان می‌دهد که دارایی‌های چین در قالب اوراق قرضه آمریکا تقریبا نصف شده است حالا پکن با این خرید از ابتدای سال ۶۰ تن به ذخایر طلای خود اضافه کرده است و حدود ۲۳۶۶ تن طلا در اختیار دارد.
https://farsnews.ir/Sadeghi/1786109079785791668</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454868" target="_blank">📅 17:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBVQ9M6obQqeUdT20HTNJtwOnPIx0SRlgC9oaGo-naugAj6upc6tY62YfU4ndIXeB0iNNs6gAIlGggg5Du-gd7Q6gwtqSFtQSidVq4Nq2oCIwadNUwgjfv8OUyUOGHUjlMKfskXsfvGMdBFqteW7oggRi0p3ZZnvoxYrg7CT0z_tt_UnA2UReMj8J35PrU7H4uM7Fg1Gi9cEh2Q3xpp1x0t_g2EHCNxOO8Z0FOHrhlj5eUjV0gy9BUunGsI6dRUkzO3W4HmF5rTWf1O9TDq7ki-x3SLklRCVPo3mxOwvDGrN7v0voMkXUgt3epSyixlfzOXVL_eH_T792wEs2RIBzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش جوانان ایران در المپیاد جهانی هوش مصنوعی
🔹
اعضای تیم ملی المپیاد هوش مصنوعی ایران موفق به کسب ۲ مدال نقره و ۱ مدال برنز المپیاد جهانی شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454867" target="_blank">📅 17:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byDA2GxBv44xm0KhxijyVJ9kDrsjY-jOrMZHzLzbSgWFQd-kxUA3rUoa7kaZuFTddOyK1gvIBKX1jgrThyukq1QFpgZg976bOXN7zyXeYTfrM_8VzBCDe9qtxYtkzrkIlAFcPNc0NZHTBV0Np11lxl4gfEo1hDMDjqQj6g1-hpFK12sA2aG1yGGaF9xRa4ot0HlF1-y2MJYt1RcUzb_5G1kVTQ5fW4P57JYAe2pZ4VgZTK1DGk13R2_fr6b85CEyGcxougBB_UFzgrT0EvExABx9iuo0Si4yEsnZphuIZ-_OxMTaI92N-EiB-Qk-gaoEDDjMEciG93fwjLNM_EgcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مرد سه‌هزار چهره» و حماسۀ شیرعلی‌مردان‌خان در راه تلوزیون
🔹
نقویان، رئیس سیمافیلم در گفت‌وگو با فارس گفت تولید سریال «مرد سه‌هزار چهره» به پایان رسیده و این سریال بعد از ماه صفر به پخش خواهد رسید.
🔹
این اثر مهران مدیری، حدودا ۱۵ قسمت است و در مرحلۀ تدوین قرار دارد؛ در این فصل از سریال، شخصیت شصت‌چی در موقعیت‌های مختلف قرار می‌گیرد و اتفاقاتی رقم می‌خورد.
🔹
نقویان همچنین خبر داد که فیلم‌برداری سریال «حماسۀ زاگرس» که مبارزات شیرعلی مردان‌خان بختیاریرا به تصویر می‌کشد تا پایان سال به پایان می‌رسد و پخش آن به سال آینده موکول می‌شود.
🔹
همچنین ۲ اثر پخش‌نشده از زنده‌یاد اکبر عبدی به‌نام سریال‌های «ماه‌عسل» و «سبزواران» وجود دارد که مجموعۀ ماه‌عسل پس‌از ماه صفر در کنداکتور پخش قرار می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/454866" target="_blank">📅 16:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454865">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npLVhAP7JnO3U3omFQFDputREQlE0l_HXqgCnLLI2c9hDApxhK52JuH7kJ1KgNnfr1ZTUFh_be45SBF7CNcxOjCB_mh16KlM1b9IK_Q_mjXHB6XKpRjB6nY0UlVvL-fbY4X-oKuYRvF-yrIkAU0iY-5DRhY-bnhiUlBaY7hU3e6hi1XLDVSn4W2cVAHXyXFXgWbUput_KEpcrJ32kH3ImtVo1krh5Mc4Ira9y6Afs-ubWhR1n-wj4Ru8uJLweyfqkyWHuNzcUsOhOKUMzx4yHS77NO30eF0Zr9f9ZjUtvoK077cwongUOkZ7zdFfajdvP_1267OiQA9Ro5F03WMbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان تماس‌های تبلیغاتی مزاحم در فرانسه
🔹
فرانسه برای مقابله با تماس‌های تبلیغاتی مزاحم و کلاهبرداری‌های تلفنی، قانونی تصویب کرده که طبق آن شرکت‌ها دیگر حق ندارند بدون رضایت قبلی افراد با آن‌ها تماس تبلیغاتی برقرار کنند.
🔹
براساس قانون جدید، هر شرکتی که به‌طور غیرقانونی تماس تبلیغاتی برقرار کند، ممکن است تا ۳۷۵ هزار یورو برای هر تماس جریمه شود.
🔹
دولت فرانسه اعلام کرده که حدود سه‌چهارم مردم این کشور هر هفته دست‌کم یک تماس تبلیغاتی ناخواسته دریافت می‌کنند و بسیاری از آن‌ها با تماس‌های بیشتری مواجه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/454865" target="_blank">📅 16:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454864">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0AYtcPtK3fKgKkQ_yiyFaKleF4C8TUVmLxdnXA-GOozPxNfTQp9K_LFxdQLufYQmjlDjJEsUg_WURCLxaBYwsEiWXUTgqXOMLD8SR4ShEvuuJs_T3ffesgMlgndaowfCdYkPsw1vulodMBdjrSwr2neJsfyn-zvyIoHO2nGRoUTDNm1Lr6azaA-fmAYkCnoHsNInRA7XNm8KbiHsDqAiE5hkC0rMzIY0bo3Zlw9c6ZeSkLdE-6M0jq_dzHgsiX7iPku2Bo6lWzLA5WJPDbDxiyHtCGKZ_k2PT4l7GcKYVytc1S_O-blUT-hl1laQspkeQX4B1PIIjJ3FS5MYvl8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت سقف پیام در چت‌جی‌پی‌تی حذف می‌شود
🔹
اپن‌ای‌آی اعلام کرده از هفتۀ آینده محدودیت تعداد گفت‌وگوهای متنی در چت‌جی‌پی‌تی را برای کاربران رایگان حذف می‌کند.
🔹
همچنین مدل جدید جی‌پی‌تی۵.۶ لونا جایگزین جی‌پی‌تی۵.۵ به‌عنوان مدل پیش‌فرض برای همۀ کاربران خواهد شد.
🔹
بااین‌حال، اوپن‌ای‌آی اعلام کرده محدودیت استفاده از قابلیت‌هایی مانند بارگذاری فایل، تولید تصویر، مکالمۀ صوتی و ساخت تصاویر همچنان برقرار خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454864" target="_blank">📅 16:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454859">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UH4PF6ZKjXqO0388MrzSwU_962DHO48uDwsCX4P1J9BTQVXuYAVgkFs9ewCGJfYIOzKvYQj6YJsfY98_UJz9EXLPRrKwGhLye_SM2cdnA7LPQpsuMLcGfjCkVwijNrvEAqzSTCHXSc29RmGP1yayTNeyTMGBNMwiUo8kujBN0ECnx3iKvwNvJAN_5KSELcr9mjx9hH6C2kA4AIE20a0Qiv1kHQov0ZfLb28Jtf6jIQ1M_TnojWCM8QGK_qgkspFp-HM9xsN9Qa-8Aaw2Z-_Saso6GngHKmsTUn3WsnDjobWi9Ni4W4zA6OM8OozHcYOIVvo4SPsaGqO4UowPIEiGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDhIEBGYxqLQW3NBcph_y7fufOax61ss4lAmgHkOGaAjUBEbcIArFGd8NSm8L1mth-pIKxrEWeNhtaXZXGgCfO-kRHE1TyUYDw4fpGxrtx1ku1d13uRP7o5V7p9QOt6qlyOihH_adAhfiKOC9t_DkSa6Dxx7Et_rxdPavQsiiN2yl5yWNHVF8VTRCIlusishgWELg64b3isIdhe3ZqKJBvKZIwkxFXujYoH6tjgrkcLQNYPgWJ_i_Kt-YnFpspMo39HwfTfRrta4omegieWQbYGbkheZ9TvHeiBNr9CJg3XLTKKbt5-Iz3e3h6Z-M_GF6npHvYrnNFmSriQ3h-gc1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W0En9Gdkl4M2nn-Odguyou4aRbXN9MVTuG9nPxRmfcqyQ7isf45ntjrcWmXYICy4T5MPqeA2vDF9sX7immfkUUqf0wnkuOX3eA8-EEP-uuuLBm3BR0BkJ84XftUaG3zwg1C0oaq6BhN0LwodIapL48wQBTKRtPiAqTMTDvE4V-TZ0xK7TSQxkpojVbuIDHawyVcNf0y9LdCOQWWY4GSF2pPoZggIcNRdcMO39ACK-NBAOAVuK8PucBbXauQdQG_TQLExhpYgAaniXanjrzx3nCRZOJr_WGIJLTr2xj0kk2IEr9ZlfkM0MJJP5nO_Amfr8UfgxRueJ97OehQX_zSC5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rw_hoPEKJsiQcLX7Vx1WX7Du2JBRIhXXmUrFgozgN2MpVaF4yVMJN3uxzj7ZfZSC8DvEzJumYEyAZ_RkaQ7nMBVZXZvQfTrCkHjVxBdTzK__LLVc4sp3OkrYciWoPfO_Uxv1Ci8FrIaPMVgs4aUMX0la-RJ-mbuAYRhFBwKIMjt9i3tYgj88znLM4WMbw17IFzXPyd5usaj4cdYFMMQQZ7fs2k5dUS03Ll9s8jsNFOCWBoW8V5nqLPDoUugbc9TfGKKZEf_EtCzr6W8ah6MWPLkJzj8Wn0fgqFSugOVrry9WHFuypGmvqYlDGsXZLWKd9IwKH-wYk9548-oJgbKr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQ94Q2yURk5EsZYdma_03VCuO9Hm2AMgaMGvljqKPLU7pDSU-71KIXEMh-Izbh78ZVI7EujRLV0xEX44c8gh4I2PzNeUczXykkPxHkIwnULfdeuc-tFTnMIY9c5xYU8furnnEgdnSptfDeDvk4g0xUqqStN9Il4XmehWPeDQNX8FREqmAevsMHmP2NOXrPLIZAdA_YItlWKq3zIaE4StoZnXgtrVzpYBSe5XktOxFGKGsG4QTS65ke1tJkaIZncmjZH7dyynQnuQEKb7wagW5acLpZhUfXxrhXrWBnzWfiqVLQ_AhbPBtEIJnynaL5_utYKXVeS7_H7AgfltSCb0Pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم دعای کمیل شب گذشته در حرم امیرالمومنین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454859" target="_blank">📅 16:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454858">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3l1GjjYMuQ4ddPJeK_pcqW4g1GuOJsVm9oxUeoLoCmH52Da811vvjikpmrCOFt314XzbtkYkegvnqIUntU37vpzxXZDUS9Cj3631UZ3ywt4RKnFfbeQ_vs4B0WgdsCYML4I5VbiGY57qrZm2nWW5JjAZBWvD0RobpWyDPj5T1E0KQ9tGikrSPPptsRT_NJ9nZW8dWBZmiKNUKvfY25zoIJvd7fBEn30eA_8527x1RfLEILp36wi1esFl6WjTRLSSOg5fd5oSFY20FimI7FKL18Kl9LKQLw-MK_AXtajL4znr-oBBbNJiZJCHi1JRdsCPdByC-7F3T209zec4j-GJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان عمر ۵۰ ساله دلارهای نفتی به دست ایران
🔹
ماه پیش عربستان هیچ نفتی به آمریکا نفروخته است؛ اقتصاددان آمریکایی، استیو هانکه، در واکنش به این موضوع در صفحه‌‌اش نوشته: «خداحافظ پترودلار».
🔹
پترودلار از اواخر دهه ۱۹۷۰ میلادی شکل گرفت؛ جایی که پس‌از شوک نفتی، واشنگتن و ریاض توافق کردند که عربستان نفتش را فقط با دلار بفروشد و در اوراق و دارایی‌های آمریکا سرمایه‌گذاری کند؛ این دلارها به پترودلار معروف شدند.
🔹
حالا با بسته‌بودن هر ۲ تنگۀ هرمز و باب‌المندب به‌روی نفتکش‌های سعودی پترودلار عملا کاربرد خود را از دست داده.
🔹
ازطرفی با نبود معاملۀ نفتی بین عربستان و آمریکا، ذخایر نفت آمریکا به ۳۰۴.۸ میلیون بشکه در روز رسیده که با عدد بحرانی اقتصاددان‌ها یعنی ۳۰۰ میلیون بشکه تنها حدود ۵ میلیون بشکه فاصله دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454858" target="_blank">📅 15:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMeFO_WM0g5_S9puRhxtFyv9WD1pvcitVUGMIs2Ji7IW6mDvEpUdkuUDsDJx17fFRF8qAWx2D88mnLp-ebu3x6n8kHWiVVbdu5JtPmv2B113Hbrpc7T8V_gqBbokefQjo23JqMDOJt77yIdjCd-yYk3X5MQZd-ImlLhOkpCrLwqO_QMr2JbrcqyyNsA4m__oG0dthOIU1bR6Jot3h4Zkm8FxEBYdxhYwOsv-7C7c6MopiLsAgucU2pPTMcGYpTSk3hO-e9tguveHj6S7ijyKXYwNgww5gnVaQqizjh36OiUWqUYbTA9Sy3OB7g22NBgT1E2veyh-qa1Vyl2jokEIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آدان در آستانۀ بازگشت به استقلال
⚽️
بسته‌ماندن پنجرۀ نقل‌و‌انتقالاتی استقلال و بازگشت خلیفه به آلومینیوم باعث شده تا باشگاه استقلال دوباره به سراغ دروازه‌بان اسپانیایی فصل گذشتۀ خود برود.
⚽️
طبق شنیده‌ها مذاکرات با آدان مثبت بوده و قرار است مطالبات این بازیکن نیز پرداخت شود.
⚽️
این سنگربان احتمالا در هفته پیش‌رو راهی دوبی می‌شود تا آن‌جا طلب خود از استقلال را دریافت کند و سپس برای عقد قرارداد مجدد با آبی‌پوشان راهی تهران شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454857" target="_blank">📅 15:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b3b0b0091.mp4?token=r6-G5qPK5Vnq7lEI8EiqmG1nQMBAEUZJDvfFjd0RPs5nmVp4ds_B0jeKflQ1llUInOV3CWwUsxdvmU3vF6IyOGBqfgOzVEGAP6jOxlEELaN_B6I2C0dH-dvd4n8Dn15SF1jPfxchX87o_SlAWTKPnQvsVl2ASVn8_LNVZ549SREF12ADrSio2nEdJpusAIwuCgAErs4M2RuoWWvDGl4IBNR7p73GCgPEFXs_fR-TWifAzt70Yv3GHGQnw5kEZHJWl3_g8DGAFxiAXCUr5lfBCS-o5HTNWMao_sezTwuoT4fIWAq_tSoC8k09u--_xc06rVADE2YVxD94qe5o-TsTw0d-PqkV1w2RzeWUN2mIs-heMopvYgMAMr7ieCquwSEjsntekm8-ZlXuA0OMHBq6JIdwauidLfcau-m2Ap7rLGyQoxTMriNiMwDi7SkQ44w-b7bb8SkBlf1vtW_Ukcb_1_HXvMyGBvq7QHzhc_8NaN0dZ8HTYg4ZbYxUCp0_4pfOHKR5hG2Mdob15P-FjSEjFs8-ibzxRupxfKKmJ6LQv3hQUqWx3yg27zcmkzol9R7a02vu33Ch0WLj6RVbxOrgo8FX-DwdzYB4xOu1QUag4VNdgSSj1yHA162xowSk-pU72z-9vzsK_fEluRRFLnnQV9jb9ENZgfxqFggqxrf2HC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b3b0b0091.mp4?token=r6-G5qPK5Vnq7lEI8EiqmG1nQMBAEUZJDvfFjd0RPs5nmVp4ds_B0jeKflQ1llUInOV3CWwUsxdvmU3vF6IyOGBqfgOzVEGAP6jOxlEELaN_B6I2C0dH-dvd4n8Dn15SF1jPfxchX87o_SlAWTKPnQvsVl2ASVn8_LNVZ549SREF12ADrSio2nEdJpusAIwuCgAErs4M2RuoWWvDGl4IBNR7p73GCgPEFXs_fR-TWifAzt70Yv3GHGQnw5kEZHJWl3_g8DGAFxiAXCUr5lfBCS-o5HTNWMao_sezTwuoT4fIWAq_tSoC8k09u--_xc06rVADE2YVxD94qe5o-TsTw0d-PqkV1w2RzeWUN2mIs-heMopvYgMAMr7ieCquwSEjsntekm8-ZlXuA0OMHBq6JIdwauidLfcau-m2Ap7rLGyQoxTMriNiMwDi7SkQ44w-b7bb8SkBlf1vtW_Ukcb_1_HXvMyGBvq7QHzhc_8NaN0dZ8HTYg4ZbYxUCp0_4pfOHKR5hG2Mdob15P-FjSEjFs8-ibzxRupxfKKmJ6LQv3hQUqWx3yg27zcmkzol9R7a02vu33Ch0WLj6RVbxOrgo8FX-DwdzYB4xOu1QUag4VNdgSSj1yHA162xowSk-pU72z-9vzsK_fEluRRFLnnQV9jb9ENZgfxqFggqxrf2HC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات هوایی سنگین روسیه به مراکز کنترل پهپادی اوکراین
🔹
وزارت دفاع روسیه اعلام کرد جنگنده‌های سوخو-۳۴ نیروی هوایی این کشور با استفاده از بمب‌های هدایت‌شونده FAB چندین حمله علیه مواضع ارتش اوکراین انجام داده‌اند.
🔹
به گفته این وزارتخانه، این حملات مراکز کنترل پهپادهای تیپ‌های عملیاتی چهارم و پانزدهم گارد ملی اوکراین در منطقه دوبرپولیه در جمهوری خلق دونتسک و همچنین تیپ ۱۰۵ دفاع سرزمینی اوکراین در منطقه براتنیتسا در استان خارکیف را هدف قرار داده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454856" target="_blank">📅 15:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454855">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19e751166f.mp4?token=td9zvLa7lpbvKZkQRtvUXC1ExfPcWiXC-lDNCYyt23nPnXfRzujZoR04glLQkTWr8V6sUxAuul7p6Lq1iZlzme2IyupByFBwhirk5ZTSywbWJoyAwDj639d_xOQEypm6cLnzkmvp4O2yLTO7V41LcLN2pNXrSE5sWcpyYeWmVh1QbeeSJ3dDSlP-aIpxkrRy_mI5NUPo1kyLLysYTVwE3p92NJ3-BKaCajqTMqYepax2Ka2ATCDkVv83s3L5OtV2JN70pkhTmRqeQxYKVI3P4-vblH6FA7_oSIIk9XpfDzo88P_yQ_61WYZ7kvnSb65hAMpcxVfYBsvjKNKmdRU3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19e751166f.mp4?token=td9zvLa7lpbvKZkQRtvUXC1ExfPcWiXC-lDNCYyt23nPnXfRzujZoR04glLQkTWr8V6sUxAuul7p6Lq1iZlzme2IyupByFBwhirk5ZTSywbWJoyAwDj639d_xOQEypm6cLnzkmvp4O2yLTO7V41LcLN2pNXrSE5sWcpyYeWmVh1QbeeSJ3dDSlP-aIpxkrRy_mI5NUPo1kyLLysYTVwE3p92NJ3-BKaCajqTMqYepax2Ka2ATCDkVv83s3L5OtV2JN70pkhTmRqeQxYKVI3P4-vblH6FA7_oSIIk9XpfDzo88P_yQ_61WYZ7kvnSb65hAMpcxVfYBsvjKNKmdRU3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معترضان آرژانتینی پرچم آمریکا را پایین کشیدند
🔹
معترضان آرژانتینی در جریان تجمعی علیه لایحه «مصونیت املاک خصوصی» که پیشنهاد خاویر میلی رئیس‌جمهور این کشور بود، پرچم آمریکا را پایین کشیدند.
🔹
میلی در کشورش به دلیل داشتن دیدگاه‌های افراطی مشابه با ترامپ و وابستگی به اسرائیل، به «ترامپ آرژانتین» معروف است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454855" target="_blank">📅 15:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454854">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edef91be97.mp4?token=heEyQPfWoR-hl1n5zempfb72a2g7mWx0DWVasE3-rbM0AaDyJO4xJOlB90dXBP5a15JMs3LVkqTZW3aHELT9JFYD0o9NE754JijGVvqLaQpF32h6MF-C7UvSnSYcwLhs3cltzKgIsptfAWkgq-A1_V3NHTSYEDKDwGGfYRhAhRnWa3t1w1KccjxPos1g8Mdlgz2uEzBh32T4BKc_OJ3aeHghmtvSQNfv720cvMB7CsjRbqJnPlPbK2-7NaAPtEB9DbNG459lK6bwM4qMHYLf574__6c6CQZCEvTlxbYO1JoGhZM6YHH11RMiYVpu0db8DJbwaIuh9XQ887lrohC1hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edef91be97.mp4?token=heEyQPfWoR-hl1n5zempfb72a2g7mWx0DWVasE3-rbM0AaDyJO4xJOlB90dXBP5a15JMs3LVkqTZW3aHELT9JFYD0o9NE754JijGVvqLaQpF32h6MF-C7UvSnSYcwLhs3cltzKgIsptfAWkgq-A1_V3NHTSYEDKDwGGfYRhAhRnWa3t1w1KccjxPos1g8Mdlgz2uEzBh32T4BKc_OJ3aeHghmtvSQNfv720cvMB7CsjRbqJnPlPbK2-7NaAPtEB9DbNG459lK6bwM4qMHYLf574__6c6CQZCEvTlxbYO1JoGhZM6YHH11RMiYVpu0db8DJbwaIuh9XQ887lrohC1hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اوج‌گیری اختلافات داخلی در اسرائیل و آمریکا با شکست پروژه‌ها علیه ایران
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454854" target="_blank">📅 14:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bjy6Rohq4bTz9I0lyVlIU5G4ab035V_AA_3zU5ix4g3p_A0Vb--d-LItAntxjEMp5o59sk4VHbT1YZ1-fZBeajLL_hA4JRKqONy0m7oSXW_JZdB0j-EYtv_B58ft0VOG96kzQlseVy1xdzDe9Ps2_GdlKegYrmp4QpVtZPzBO5CU-5gQN0H9wSJw8oEWlSGyG8kLwQhAaUiqgU7DLmSRRYVroS5xQxE1Woi0LNwuUTSdkvYLLTETLuR5tnaIt5PGS_ZF5LL_urFzItF_YA1JnBdhPnSt_Z8qzQZeaazzrFeHJ82YnSNlQcx6LULfzXu4Ijg0vULMsZPDtXgBBMxkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfqL96dw9mbraOjsCs9pr6pIoTdzAAFWi2hApo2eS28E59YKLN-4VlfGa1xKoCeP56Uh65RsibL7aLn-_z29_0zxNm_qKIzGNxFf3jA6yVbmRk8zINtpTDfR4aPxJjPAgQsvewmaVbWWlFhItcJvswNAal6gng2NIaoiTYqZRaveEmWJwtuHyHUQks9V9Alp8O1wN6P9_LBgSNQ8prXOYsJb6horLRQXyFaNJE8mMAg33JRXRXBQlsr1SHSatcQeH9bhBWhEAzXOM2JtUP5z41VSPqi-HsZsz36v-CytsETDXv0nrvUJKQtxAcMU_70qYqK1KaQxtB9gHyq6EWDoPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454852" target="_blank">📅 14:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/148682d952.mp4?token=ZIOMqrxZm-8ebRPm8VsZKbZzH6NXyhScsJ34d4UF0quFHPfxUGmU-mfbonKOTCtyI2jGtLnlm8m9k2z-JVAJyZ2ukJIg26PMWXvBRQTd4VjzxA8tk8rdJSBoGYimSwiVz6oho8DLJdKGO-WJ58hZkRX7TMWdLcvzQAGaHSo1StxztY9kQWY9NPiu0QxjI5BeFswijAXXvH8cHV6CdPWgAQQE5_1lmE7DpvCNvDCNz1lOh_mdVInFZO3WHIDc5iHuT_35B-F0h2bl7y3LN-0dO2_ygFnCD2ke3oJZFQ2leZmBChLrHdSEduMLMr3E47Jex-nSpwVfOmU-C3jDwR8uVCv933uq2_Pj8jKzqIDOr_zNYe4Rw1TexpCt1R5taNcwcAuEYHqP7CyFAjNNl4cWVfj5Em7CIOppD3WhaEdxojm6zBIZpnotmLnQMHtH8R-vy2FV9C5y0BssKSrB57O_AsuOVYkcUu3pk0JHNygSV5NXS3UyG7J0D1yftPvg_ZJWglp3N5OHusFHGOad9oT6_k0pYg3HLPKFbPAQKKqqYDG_M5z8ddXFLupu2Fh2zqnof8h-EtwoxlbQBoJQ05PSm8GDsVxXVh5Vi8GluoKhKydi8jHX0mUFkVhcxXbERZ-3AACj1Ake5cSC3f2WVpew2mfGqgsv-xhTxLdE7E8vZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/148682d952.mp4?token=ZIOMqrxZm-8ebRPm8VsZKbZzH6NXyhScsJ34d4UF0quFHPfxUGmU-mfbonKOTCtyI2jGtLnlm8m9k2z-JVAJyZ2ukJIg26PMWXvBRQTd4VjzxA8tk8rdJSBoGYimSwiVz6oho8DLJdKGO-WJ58hZkRX7TMWdLcvzQAGaHSo1StxztY9kQWY9NPiu0QxjI5BeFswijAXXvH8cHV6CdPWgAQQE5_1lmE7DpvCNvDCNz1lOh_mdVInFZO3WHIDc5iHuT_35B-F0h2bl7y3LN-0dO2_ygFnCD2ke3oJZFQ2leZmBChLrHdSEduMLMr3E47Jex-nSpwVfOmU-C3jDwR8uVCv933uq2_Pj8jKzqIDOr_zNYe4Rw1TexpCt1R5taNcwcAuEYHqP7CyFAjNNl4cWVfj5Em7CIOppD3WhaEdxojm6zBIZpnotmLnQMHtH8R-vy2FV9C5y0BssKSrB57O_AsuOVYkcUu3pk0JHNygSV5NXS3UyG7J0D1yftPvg_ZJWglp3N5OHusFHGOad9oT6_k0pYg3HLPKFbPAQKKqqYDG_M5z8ddXFLupu2Fh2zqnof8h-EtwoxlbQBoJQ05PSm8GDsVxXVh5Vi8GluoKhKydi8jHX0mUFkVhcxXbERZ-3AACj1Ake5cSC3f2WVpew2mfGqgsv-xhTxLdE7E8vZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تبادل پیام خاص میان میدان و خیابان
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454851" target="_blank">📅 14:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وزارت خارجۀ پاکستان از امضای توافق دفاعی سه‌جانبه میان ترکیه، عربستان و پاکستان خبر داد.  @Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454850" target="_blank">📅 14:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454849">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83b26c79e5.mp4?token=SLWxmLeMvF2rWmJ_GsQyhdyI40cksv2TNExL2YayRqQYF-HUSfWyU8FWh_TKVXdakJBWOTq158kodzd8sGS4H_6I-8xpx3c_qqyR--tHt13MD5J5wIn1_vc9RlrtLOarP1I7brTfiJE35US9HQ119fI7HIv_tXVe8nGGhsdums9ZOO5zagIOCcBVdUYnNvc7Eq8ZYey1P_opfCeUAPlGTJj6zINNfPK5ofaSoi-xomf_hwMv5q-UTRz7OZSx7z54sp389IZfWl5taPBfxEagJOb0XeO8TRS3av9AKnak8Hi5D9GVKtsRBYjzH90O16IEJ3TBWqI2wP6KYBHm5y3oFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83b26c79e5.mp4?token=SLWxmLeMvF2rWmJ_GsQyhdyI40cksv2TNExL2YayRqQYF-HUSfWyU8FWh_TKVXdakJBWOTq158kodzd8sGS4H_6I-8xpx3c_qqyR--tHt13MD5J5wIn1_vc9RlrtLOarP1I7brTfiJE35US9HQ119fI7HIv_tXVe8nGGhsdums9ZOO5zagIOCcBVdUYnNvc7Eq8ZYey1P_opfCeUAPlGTJj6zINNfPK5ofaSoi-xomf_hwMv5q-UTRz7OZSx7z54sp389IZfWl5taPBfxEagJOb0XeO8TRS3av9AKnak8Hi5D9GVKtsRBYjzH90O16IEJ3TBWqI2wP6KYBHm5y3oFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ سوئیس را تهدید کرد؛ با یک امضا اقتصادتان را به هم می‌ریزم
🔹
رئیس‌جمهور آمریکا در ادامه جنگ تجاری خود، این بار سراغ سوئیس رفت و با اشاره به تراز تجاری منفی با این کشور تهدید کرد، فقط با یک خودکار می‌تواند اقتصاد سوئیس را دچار مشکل کند.
🔹
ترامپ در تازه ترین مصاحبه خود گفت آمریکا حدود ۳۹ میلیارد دلار کسری تجاری با سوئیس دارد و تأکید کرد: «می‌توانم با یک امضا این کسری را از بین ببرم و آن‌ها دیگر یک کشور ممتاز نخواهند بود.»
🔹
وی افزود: «کافی است بگویم ساعت‌ها و کالاهای شما را نمی‌خواهم؛ در این صورت آمریکا ۳۹ تا ۴۱ میلیارد دلار صرفه‌جویی می‌کند و سوئیس از یک کشور ممتاز به کشوری با مشکلات جدی تبدیل خواهد شد.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454849" target="_blank">📅 14:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454848">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt9pc434I-UTkc8g1SIuNePQHn0aozzLUPezdCAb1LkO8qdXN9UoRQ3Kwd34T-HZmJfvKH1VZmNTQQIu8TCn7TneZY-9Y3hoPYOWQ7Z8RIq-KQDz-oFb6DYjO5e-g_kzzrHnGJzwetftGnx_HuGFoFpwhJ8rbG_Y0as2r4QTqhQqmjoJ5i7PQJNkHzGLV_Or-UMDR1a72cdS9kf9My74w26lL5QCkt1_vh_VcyJyn94l-HwLwtv660G5G59NCLjmcmUcWx5V3PvWqUeQfAmsEi6GsCmR75CtQldevkmtONSY-HbSoN4lxlhJ6nL6Gp_CacWT_FUzV2T-3CQd8-F5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر اردوغان و شریف به عربستان؛ امضای پیمان سه‌جانبه دفاعی در دستور کار
🔹
رجب طیب اردوغان، رئیس‌جمهور ترکیه، روز جمعه در سفری یک‌روزه و کاری وارد عربستان سعودی شد؛ سفری که در بحبوحه تحولات منطقه‌ای و گسترش همکاری‌های آنکارا و ریاض انجام می‌شود.
🔹
بر اساس اعلام…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454848" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454847">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVEI85SChrBS-t6p70O_1JiRYoLi5Ih88zhjE-hccx6RK4UaGuS8xnqVKmkQ6AVANP03fX4hUh2Bj35tlHscLS7A2IzzaCSNtCPkyL--FoMOHQ9F0Ewdff3aQOZZVudM7z6JuIycBQO6D8ncNqihh5ue-PbQOG6Y2Fj_zokk_Kb6S2GNhmQLBXX7kC5gW8gp_dPh3ifCZIZxt1ZJWVb6qyCqxQilS3Sd6JjlDc2SzfnAR0bh8Syi_n7Ofywz3Tjt55rJExqntQgVTDosM2sygW8rd9phKeGCUuI9Zv7hT488h5awFJCw3z6kn4k9Gl2Qr0SXpJybRUJOlahTlnF0tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فردا به سوالات خبرنگاران پاسخ می‌دهد
🔹
نشست خبری مسعود پزشکیان با اصحاب رسانه فردا همزمان با ۱۷ مرداد، روز خبرنگار برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454847" target="_blank">📅 13:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">خطیب جمعه تهران: گزارش‌هایی از حمایت مالی خارجی از هنجارشکنی‌های فرهنگی وجود دارد
🔹
حجت‌الاسلام حاج‌علی‌اکبری: «زیست عفیفانه» صرفاً یک مسئله فردی نیست بلکه سنتی الهی، میراث همه پیامبران و حقی عمومی برای همه افراد جامعه است.
🔹
سلامت اخلاقی، اجتماعی و معنوی جامعه در گرو گسترش فرهنگ عفاف و حیاست و صیانت از آن از وظایف حکومت اسلامی به شمار می‌رود.
🔹
نوع طراحی دشمن در عرصه تهاجم فرهنگی از یک سو و برخی غفلت‌ها و کم‌کاری‌های داخلی از سوی دیگر، اهمیت پرداختن به موضوع زیست عفیفانه را دوچندان کرده است.
🔹
دشمن با برنامه‌ریزی سازمان‌یافته در پی ترویج برهنگی، بی‌حیایی و تغییر مرزهای عفت در جامعه است و حتی گزارش‌هایی از حمایت مالی خارجی از برخی رفتارهای هنجارشکنانه وجود دارد. این اقدامات با هدف تضعیف بنیان خانواده و فرهنگ عمومی کشور دنبال می‌شود.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454846" target="_blank">📅 13:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454844">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MKxl9OFF6JTWozxgLEiYRN3WGwJIo2wGc62F4ObMgxcB2kQ8UPby0EHGQgqEgw3ctu48nMzlS-j1m9uCiWDF5kNMzU17ZWMdts03c59tMcpuIkqR-T79yGSsxRF19st3Y2-cx_HPN6CAJxUejz7jWSQf72sh56Zomtx33VCd5X31NrFv5tv5F0e7BGWtJK5EfAI675-tfP0K_1BlksHn0WV_K2dJ4Pi6XQsLukWKBEHe9MAaWG_o0LvoxDRejyi6OeGy2-0rvykKOfEyCJ27tMWXGe7IVn3a_NQuSYXeaxta-f-FeC3cYFzvDnXxh5Daxfs6B9HixKIEw7d7FEsgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qwhgxYn4zBZK4rSPKFgcUIij2g4m7c1ClryJb1skHDvXLsOhWbaRiRNyRoC4bzEUTBqGdQ6t23xy19VywVVCDpKLur3x_MpNv_PKoOAFEnSvFsa8QLP-_hmeC_LIagFBCZrQ_fAhE-GgfhcxrSoGckdGl0X5RFGDsgYdNldprGmFl0caCme7tLDs0bw6aL4usNO9rHvIGhpsbmDzuALxY7SgQDhzCjdo6cs963LMQ-iT-35eKfu7gqcdXGcxqtIvisT3eF4FQgsGq_GzHqsrS7QlHZAy0uiZXe71o8hDk4E0l8TCTUsNBRlfOVRNwD7Oup99k-cvD2OkwYZq38_1Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454844" target="_blank">📅 13:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454843">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کشف ۱۰ قبضه سلاح جنگی در مرزهای سيستان‌وبلوچستان
🔹
فرمانده مرزباني سیستان‌وبلوچستان: مرزداران استان پس‌از اطلاع از ورود قاچاقچیان مسلح به مرزهای کشور با آنان درگیر شدند و طی این عملیات ۱۰ قبضه سلاح جنگی کلت کمری را ضبط کردند.
🔹
قاچاقچيان با استفاده از شرایط جغرافیایی از محل متواري شدند و تلاش مرزبانان برای دستگیری آنان ادامه دارد.
🔹
قاچاقچيان قصد داشتند اين سلاح ها و مهمات جنگی را جهت اقدامات تروريستي وارد کشور کنند که در دستیابی به اهداف خود ناکام ماندند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/454843" target="_blank">📅 13:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454840">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OuhHWWBB1Il5hLzxhnxpLSSbwSI0oJKzQkB6VVITeQlPsaqSgNRtTwX_QDaN_vjyG43ekPWl2BS4Egm9iok6So2kK0bn9RQZZuBt_Gv1URf-CfedPituLBPqr6d-pS7VA5gyBtS2dhK2tdUItbGJq28Y0fMiQTbsFHPDvtccArPiqnyG9yJ_JFrRyXlx6D1pA5nt_s4GTRldjrBETyTrs0oDxhFlBVHmh2BPU0u48wXgJtjCCGs94avVQ3FLLJsveHGGqK53dURyd8h9DMiQi7tFubBmcEOgR8Xsym_sye3b0BGf_13YdTrQHgcEmJLBO7lPEtUCQmwxKoICM_LNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq5Jy5w-kQ1RhmqXHVsYskRjKH_5aCzsyBfZ88GI32SbEIHIWALEziXc6LVU51H64K534oPIhQ1fghiUSI97MoJvMYXv3EMHtC6ASTU1pYZyjiub3_9tQAbCykxIBF4n5ZxqZLmaio9W3qgbBF-aiFsIjPRkhryefdi9uf7kM-ssxeLb7b95R9z-UN9bEzizEVp_xdMA3a5KiLLB9m-npbyVzsbZ7kse0Vky1lFFF6kBuGXiIrhZc6WvlSMTnVRuBkZUEC8YN6AjYBUOWsvJjIyKbVRssOrO61io4nadT8xEGhyggdlZKbvHwMyUU0LTxDGA1GwWFWauYdRw8OHMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFcxY6vR4qPYUWjbADXj0JEodPEyEV1Cw-6twBEeVprpnzXPW2NP0BMSnPxoucK6dJgPbl-vEA1WygI53CU1tUYBo0A-cOYw2FwoVf5vMNXBWtZcVgVkUR4s4zLjfswHihYC04itmB7uSH4i1XVOGoQxHv1njZ9WEFcNdxVa-k7jrGBgNO18YNYx-Yu39FJXuMpvf43HkhMPV2CeYtV2jQoleJ1NInOAm8_uwFChaTums_4Pc06Gydp6Lq-L0tyJiutwDYLrY3L4gtm3EV1nX0pehWZer4xRrtd3J82kG2s3SsbAuVLSI9IxceWBx3VzLgca3vpP4BVFpxPrvhV9UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری کمتر دیده‌شده از شهیدان حاجی‌زاده و باقری فرماندهان شهید هوافضای ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454840" target="_blank">📅 13:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454839">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6efdc140.mp4?token=EKohYMT4S8cHGi_mmTQqnsaws9TYqYcPf8Pts5DQ3AVLo_V6GBowk1uGvP0IPH1hF9RzPI3jTlJQ0rh7IO1qkge2QyIbHyRBNN2rzZ0w44z4hCe3TWhgu2tQv-PKeO-4XI9GmSKfP8Vg_Dd2wJ-NvT8kvuge0IE7zM2bn8kCejecaFO2TNhF_1_Ebg8iz4TASHTk3mHVpWnuafsTs-ybWJAqGcS-zv_CHfLbQ3p6j7rQRV63FvtpUpwuCRJihIYnp-2jUnHzOtNmfD8ML1OJD9m6-TdhLVLC92g0R9Uq9PdBaT5GK3rh3i6MS0Vou57IAnjdz7ooOoHsn1qNYBaGVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6efdc140.mp4?token=EKohYMT4S8cHGi_mmTQqnsaws9TYqYcPf8Pts5DQ3AVLo_V6GBowk1uGvP0IPH1hF9RzPI3jTlJQ0rh7IO1qkge2QyIbHyRBNN2rzZ0w44z4hCe3TWhgu2tQv-PKeO-4XI9GmSKfP8Vg_Dd2wJ-NvT8kvuge0IE7zM2bn8kCejecaFO2TNhF_1_Ebg8iz4TASHTk3mHVpWnuafsTs-ybWJAqGcS-zv_CHfLbQ3p6j7rQRV63FvtpUpwuCRJihIYnp-2jUnHzOtNmfD8ML1OJD9m6-TdhLVLC92g0R9Uq9PdBaT5GK3rh3i6MS0Vou57IAnjdz7ooOoHsn1qNYBaGVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای عملیات گسترده رژیم صهیونی در جنوب لبنان با استفاده از ۷۰۰ تُن مواد منفجره
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/454839" target="_blank">📅 12:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454838">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKHEX34leRg7_Z0mMfBfgpV2UZpy5cRXcd8YaoNrVwqs3G2hEOiQ45TI-AFMkC5qYdZ7PRhq1SDcvP0AjwdE9PCzMIVsBS8wb6hQTjoDNIP28QMNdDNwqa_nHJdNJiz3x7nsY7X5XU7rDlXRrpOdXzlxV89tuwr6w1_Mje5kZoDhArBsr49xpgRy2PPcb4RYGUnVmt4Dryz6sqx_ECgVept8tQt1U9QjOG4SynqZ-EKMbujKjGmyYZ74U620DOGB3TdsYW7i-Ey3Z3VriAt1sP-y-ucBIoqYUsFqcYcPNPXyfax9ndnqyPEtiFAe7CauFzk3V4KQKw33fSa56PTSFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه هرمز عربستان را وادار به تخفیف‌دهی نفتی کرد
🔹
عربستان نفت سبک خود برای فروش به مشتریان آسیایی در ماه آینده را با ۲ دلار تخفیف نسبت به شاخص عمان-دبی به فروش گذاشته است.
🔹
این تخفیف که درحالی اعلام شده که صادرات نفت این کشور به آمریکا بعد از ۵۳ سال صفر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454838" target="_blank">📅 12:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454837">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f80d850c2.mp4?token=LZvktvyHsAzbUVIsyqcugYSo-tKmYNU7P7TnkN_OMAbzhpqXwjt7y_ZO-xZ2tXLjAQ2-EAfc0-Bqgd8RtZpeb0p9u7MPRWEqvjjn9poDZI0re6uJr-5mn8WFyWSvkEpUT6zbJYOpy8ozUy43oDLiGtZKcTVhnvY_CiskY1CznzGMdKljX3qz5fY94YM6sVYdorppv8m_kISYTZy-QNPIRlR-bm4iUlItV10rr93eEg_eB6UA83y1y6OUlhoyJrUQBrzSr_R1rB6u9OJk1yHX56wAGHQpJj6QTF8UM5r17exsRPqWn0ELNabmZ26e8KjimYOUMsFv521k5TvahMxrPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f80d850c2.mp4?token=LZvktvyHsAzbUVIsyqcugYSo-tKmYNU7P7TnkN_OMAbzhpqXwjt7y_ZO-xZ2tXLjAQ2-EAfc0-Bqgd8RtZpeb0p9u7MPRWEqvjjn9poDZI0re6uJr-5mn8WFyWSvkEpUT6zbJYOpy8ozUy43oDLiGtZKcTVhnvY_CiskY1CznzGMdKljX3qz5fY94YM6sVYdorppv8m_kISYTZy-QNPIRlR-bm4iUlItV10rr93eEg_eB6UA83y1y6OUlhoyJrUQBrzSr_R1rB6u9OJk1yHX56wAGHQpJj6QTF8UM5r17exsRPqWn0ELNabmZ26e8KjimYOUMsFv521k5TvahMxrPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هر خانه در هرمزگان بخشی از شبکه مقاومت ایران
🔹
زنان هرمزگانی روزانه چنیدن وعده غذا و میان‌وعده برای رزمندگان تهیه و تأمین می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454837" target="_blank">📅 12:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2dd64f2e.mp4?token=GvWogahXwthc7dGrmKWCMj7NA23ArHUHwAxaGX8dsdG_9vAIy-xx4HE7eUc5PEpRC4IahN4Jh18Ylj4zp4RwrdeR97UPb-BL8qxtAqvOHNmbJGQQSwMSEzpbLYWo9AY814hRuMqAYa2F5fmMrd_blRunH7knIyehGcW1uJvrHXOw8_5sgpag3dR8lEoL4HF1HOqm4M2HdRbCftR2VBBB6Kz2ZgsuHFSXC7Ve4vowwXdrQtQqwe-e9ZtWjXXxwLXAQNGESABMJ7M86_hFuOy1_2ZLYMdfU4UW3OaLRSXeF2_sHE1-z6amscRxb7lRb4ija6D9GhQPDjS4YyBqpGvLbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2dd64f2e.mp4?token=GvWogahXwthc7dGrmKWCMj7NA23ArHUHwAxaGX8dsdG_9vAIy-xx4HE7eUc5PEpRC4IahN4Jh18Ylj4zp4RwrdeR97UPb-BL8qxtAqvOHNmbJGQQSwMSEzpbLYWo9AY814hRuMqAYa2F5fmMrd_blRunH7knIyehGcW1uJvrHXOw8_5sgpag3dR8lEoL4HF1HOqm4M2HdRbCftR2VBBB6Kz2ZgsuHFSXC7Ve4vowwXdrQtQqwe-e9ZtWjXXxwLXAQNGESABMJ7M86_hFuOy1_2ZLYMdfU4UW3OaLRSXeF2_sHE1-z6amscRxb7lRb4ija6D9GhQPDjS4YyBqpGvLbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت زائران اربعین حسینی از مرز تمرچین
🔹
برگشت زائران اربعین حسینی از پایانه مرزی تمرچین ادامه دارد و مواکب مستقر در مرز به زائران خدمت رسانی می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/454836" target="_blank">📅 12:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e733df5774.mp4?token=M8xl0cMgFvXuRGuTdmh73x05Oqzy2_ioOb-QOp4wWsTvq8A553Jvgt64y3YeqGMmKVaoo9yZnv3E5vQi7JDxiUWmr885nPG-ebkNcLSRGYCxjnHvZNWKUIL_hRezNMFUUb19QhKAyOhsKKDAnagKRbE4peOOhlx7rET5tLV39e_5K79H3R2tGSd6_muQVQh811OUmdLT9eYuSq1CYzvXKw-ArYqWtmT-9_WuFkvqWwuyMCKfhuENeFA4jiYW9d2q4k7pB-axbprI9FGUYP-Ldep86vcmeHekhjk1UijOXLjQsTo1kqVMLr3CDKaY1t69wD-84t--mcfQO1IG8xPnRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e733df5774.mp4?token=M8xl0cMgFvXuRGuTdmh73x05Oqzy2_ioOb-QOp4wWsTvq8A553Jvgt64y3YeqGMmKVaoo9yZnv3E5vQi7JDxiUWmr885nPG-ebkNcLSRGYCxjnHvZNWKUIL_hRezNMFUUb19QhKAyOhsKKDAnagKRbE4peOOhlx7rET5tLV39e_5K79H3R2tGSd6_muQVQh811OUmdLT9eYuSq1CYzvXKw-ArYqWtmT-9_WuFkvqWwuyMCKfhuENeFA4jiYW9d2q4k7pB-axbprI9FGUYP-Ldep86vcmeHekhjk1UijOXLjQsTo1kqVMLr3CDKaY1t69wD-84t--mcfQO1IG8xPnRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افزایش قربانیان تیراندازی در مدرسۀ تایلندی
🔹
طبق آمار وبگاه تایلندی «خوسود» در این تیراندازی حداقل ۷ نفر کشته و ۳۰ نفر زخمی شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/454835" target="_blank">📅 11:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkVsvd-dHLo2QIqFWZGDF7Iwmpwm30dU1KFm5K-L1C5eewDnoMq6AgEpZbky497EnSdQO44KhnIxkPnT5qhPhDwfAqecVjgWzizqtbXXdnMqFDQjaDYc8CW_abDEINAxhXLeM1ptdgafYt6I3O_WWt3pgrhg--_7YH6jUoozl0YfIy_zPIM1GHLqn2-zgYy0HhysFSICiFVAK3-tY8Zq2WH7QQvlZWyycno0mlMVsGuTSNIPyxMYuVG5tu_cqCpIzce3AimbDnoAGCWz087osZ_htqi4o1WbO_AGmZZ-BTfBWe87GOqOgp5MDUjZwPdpjZy-NOE2-S6klAZ5Rs9SJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت تاریخی‌ترین کاهش تردد در تنگه هرمز
🔹
باوجوداین‌که ترامپ از تسلط بر تنگه هرمز می‌گوید، داده‌ها حاکی از سقوط آزاد تردد در این منطقه به میانگین ۳ فروند کشتی در روز است.
🔹
براساس داده‌های امروز شرکت تحلیل دریایی کپلر، در هفتۀ جاری تنها ۶ فروند نفتکش از این آبراه استراتژیک عبور کرده‌اند.
🔸
براساس داده‌های کپلر، میانگین تردد روزانه کشتی‌ها از تنگه هرمز در دوران پیش از جنگ حدود ۱۲۰ تا ۱۴۰ فروند بوده  و این رقم در دوران اوج درگیری به میانگین روزانه به حدود ۱۰ تا ۱۳ فروند رسیده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454834" target="_blank">📅 11:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snJeiaMe4KaID6Bs2FABvmYOdkEzlLxh9H7-N3hhgJWDvR2Kyw84-dAPfmce4bkXFBXwFGlIr6673l0RIw_ndTqkD42t6kpleq_lS1K7RavMMhba7p-Zj-x3q5mkjviUnqlFHZNBT_tXjur76I8FE27cyOfkr351FATFfpFaP6BbU0aHyF9o5R1FV2sNC3kfQA7bsX4SC0uZVOXytF2cdt3L25bqBAmEo5Km3UHizTxxfe63IHjuNdzSfsnzKY2YRLSd76CVfjwKIE2Gie2mRMDN3838_NxQ8vFUuWxA5PHm7wUmQF2f6qoudvNdx1AXoFJpF0K5s0CVtakuKHQuZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی جدید تیم ملی: همیشه آرزو داشتم مربی ایران شوم
⚽️
گالیاردی، دستیار قلعه‌نویی: در زندگی ۲ آرزو داشتم؛ یکی مربیگری در ایران و دیگری مربیگری در ژاپن که به یکی از آنها رسیده‌ام.
⚽️
از وقتی ایران، آمریکا را در جام جهانی ۹۸ برد، اخبار فوتبال ایران را دنبال می‌کنم.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454833" target="_blank">📅 11:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454832">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZh8eOE8mR9XZTUFz4gb6jKaUQI4tsyheruvnmKHtaxD5mlPIQz0FaiQtjG_Xt0-s4xAqI8HZ95G9Uw_yocZD67CnZN5pFqmhYdCvtz-oQ42zdeEn3-Dx5ZRFZ7kpeh2jd1GFKJNGZXJI8efCq82YH9zWw0JRHstp2DIxEsXt0R-FWpX7GETYpuM1uw2eKyQL9XF5w5Jc713Ej1kYkGN8sDDRU9Gml7YINsahp90GYjZOCQvBJunuGYaRSH9i8Jq_wDzlGStMQFyMTVjkUBNZY3v7gSc8K7Iv1AYaRAK8WnjXqRmi9LW81EmbdBIhqqxJV4zvBY9bdvYE7JmkFPVCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار سرمربی پرسپولیس به جاسوس تیم
🔹
مهدی تارتار سرمربی تیم فوتبال پرسپولیس از همان روزهای ابتدایی حضورش در این تیم، با تأکید بر حفظ محرمانگی مسائل داخلی، به تمامی اعضای تیم هشدار داده که در صورت درز اخبار به بیرون، برخوردی جدی با عامل یا عوامل آن خواهد داشت.
⏺
سرمربی پرسپولیس به اعضای تیم اعلام کرده که هیچ‌گونه خبر، اطلاعات یا مسائل مربوط به رختکن و تمرینات نباید به بیرون از مجموعه منتقل شود و تأکید کرده است در صورت اطلاع از اینکه فردی اخبار داخلی را در اختیار رسانه‌ها یا افراد خارج از تیم قرار می‌دهد، بدون اغماض برخورد خواهد کرد.
⏺
این حساسیت تارتار در شرایطی است که طی سال‌های اخیر بارها انتشار اخبار محرمانه از تمرینات و رختکن پرسپولیس، حاشیه‌های مختلفی را برای این تیم به وجود آورده بود و حتی بحث حضور «جاسوس» در تیم نیز بارها مطرح شده بود.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454832" target="_blank">📅 11:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJsJCFm7-4qWM-96AfUkbQuJJtTiBm5HA9clIdWE0A0YDZexiDB9XgSE-ZGR3kSxFL5cgNqgY5t8GyCv-AubxLatqZ4IbVeTU83Jjj50-tctT2FR98xiw3lbA0PxCROl8wHFB_GU2CZU46ISbvaIZ4pLDz-0O1tQ3hZcBMMD_kGfSAlo-aoEroQ0-_UNH2Wz5EsLSSItVdGxGQiFBRyTTyabSEiOdQoz6Ni6XmENw8vAp3hzu7WXW_fixZlU5KqmdezTpcUY4dQLmTLrfV0tyq2KZXXA4AOlS5qoDw5aCxDQxTRN20knZ4paJA_mnfffo3fOVbO7Rdf1OwQpv5wWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار اطلاعاتی آمریکا: روسیه شاید به ناتو حمله کند
🔹
طبق گزارش وال‌استریت‌ژورنال، ارزیابی‌های جدید اطلاعاتی آمریکا نشان می‌دهد که روسیه ممکن است به یک کشور عضو ناتو، حملۀ محدود کند.
🔹
این ارزیابی که توسط مقامات آمریکایی در اختیار وال‌استریت‌ژورنال قرار گرفته و سنارویهایی ازجمله حملۀ زمینی، سایبری یا استفاده از گروه‌های مسلح ناشناس را بررسی کرده.
طبق این ارزیابی‌های اطلاعاتی آمریکا، حمله روسیه به ناتو در فاصلۀ پاییز امسال تا سال ۲۰۲۹ انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454831" target="_blank">📅 11:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454829">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9b363a67.mp4?token=t9PSRUyqTyUu5Av5tZsxd-54HMajTIy-ME46ssP9b2lF2oSCfjfuwr7Nb8QKnXQZm0eukF2OrF-naiYbJ27Dmr4NsdtG0oRTDzUFYfeQ5hkERS_dGrGlW70NnNKtgr-hxJdWrRBibm5fRepUFD6QqOxbvJNcqXlIcSRolTiM2aHstt62oPOH8VycTNYq6eSm0q-ScAhTUkiXaYs9kN9SYM6mM7u_vtBxavf06TVTkT_ff0smcK6BcY3_mwZfF6Aj5DcRaVd7J0nk3pywHJKRpBgdyxWYz2Gga-KTaxA1VM_CCy5WKm-veqFGVbxeefeKRV0nnIvNfh2laSaXG-XR3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9b363a67.mp4?token=t9PSRUyqTyUu5Av5tZsxd-54HMajTIy-ME46ssP9b2lF2oSCfjfuwr7Nb8QKnXQZm0eukF2OrF-naiYbJ27Dmr4NsdtG0oRTDzUFYfeQ5hkERS_dGrGlW70NnNKtgr-hxJdWrRBibm5fRepUFD6QqOxbvJNcqXlIcSRolTiM2aHstt62oPOH8VycTNYq6eSm0q-ScAhTUkiXaYs9kN9SYM6mM7u_vtBxavf06TVTkT_ff0smcK6BcY3_mwZfF6Aj5DcRaVd7J0nk3pywHJKRpBgdyxWYz2Gga-KTaxA1VM_CCy5WKm-veqFGVbxeefeKRV0nnIvNfh2laSaXG-XR3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عالم اهل‌سنت عراق: شهید خامنه‌ای دیگر در تاریخ تکرار نخواهد شد
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454829" target="_blank">📅 10:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454828">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe316dc0.mp4?token=RiepIaMnq1Qx8X1cMPZUf3n_d2Pcb_0bFz695sjjlF1YDyfPFUgax30dJ0We9dfE0a6IqjjFfseJ-jHOcVe7VR9c0FPvs2nXj-cZIrMyuKom8BQ9QCOnoqPXk3lj_c1hpGQIDW5ePBEmN8O0s9w1s2dDsJvgOcqHM5oWPbzwfGCj1_hEjlY5zFOUDnSj-5NzlA7x2G0BhXQV0FX8si0FjPb4TyG4LVUdplAPSGZbbTI-Pe4QS9KO4OJZdHGBA41FDKbrk_ga1f1j9qUurK2vWINqbSx13EJZyuN1zZG-dExliZpYy0HsjLE_d-T1yCMOA_7-3Er1PiTdKLWI1M4NQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe316dc0.mp4?token=RiepIaMnq1Qx8X1cMPZUf3n_d2Pcb_0bFz695sjjlF1YDyfPFUgax30dJ0We9dfE0a6IqjjFfseJ-jHOcVe7VR9c0FPvs2nXj-cZIrMyuKom8BQ9QCOnoqPXk3lj_c1hpGQIDW5ePBEmN8O0s9w1s2dDsJvgOcqHM5oWPbzwfGCj1_hEjlY5zFOUDnSj-5NzlA7x2G0BhXQV0FX8si0FjPb4TyG4LVUdplAPSGZbbTI-Pe4QS9KO4OJZdHGBA41FDKbrk_ga1f1j9qUurK2vWINqbSx13EJZyuN1zZG-dExliZpYy0HsjLE_d-T1yCMOA_7-3Er1PiTdKLWI1M4NQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع عربی از برخاستن ستون دود از مواضع مزدوران عربستان سعودی در مأرب یمن بر اثر حملات مجدد یمنی‌ها خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/454828" target="_blank">📅 10:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454827">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amT_ycdMZvRaqanb2LR4XOxPE_BrjeHZK6T8LSMbdKB_jMVownyNaWKw5tuhV2SwVxbLDw9h5p75OD52fwhQd2HK7AeRrTi4042THWeM5h4Qb_PifITiKDxNVFU0IAMqJdqmKaTd3Mf-K9lxz0l3hJ4oXOfNneSSl4SHnRBVDjfHHSPOdGgkWKtx5GCQwx4TS9qQGxOioaYpJK_ZiCb_U48DjbD2FQxL6fl1h1Xb1t_xIaD77GPVq40zW2nv5zpTjaqbUma69Mbv1AuqYNBh7kH7Gk9azL9RrWD6hbwD6HFUfF4GffqlJqC6HKy_tDgn2Alwf-1Ejyk8lOJmYsXuew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر اردوغان و شریف به عربستان؛ امضای پیمان سه‌جانبه دفاعی در دستور کار
🔹
رجب طیب اردوغان، رئیس‌جمهور ترکیه، روز جمعه در سفری یک‌روزه و کاری وارد عربستان سعودی شد؛ سفری که در بحبوحه تحولات منطقه‌ای و گسترش همکاری‌های آنکارا و ریاض انجام می‌شود.
🔹
بر اساس اعلام ریاست‌جمهوری ترکیه، اردوغان در جریان این سفر با محمد بن‌سلمان، ولیعهد عربستان، و شهباز شریف، نخست‌وزیر پاکستان، دیدار و گفت‌وگو خواهد کرد. به گفته مقامات ترکیه، محور این رایزنی‌ها روابط دوجانبه و آخرین تحولات منطقه‌ای خواهد بود.
🔹
رسانه‌های منطقه‌ای گزارش داده‌اند که امنیت دریایی، پیامدهای جنگ آمریکا و اسرائیل علیه ایران و همکاری‌های دفاعی از مهم‌ترین موضوعات این نشست سه‌جانبه خواهند بود، هرچند دولت ترکیه جزئیات بیشتری از دستور کار مذاکرات منتشر نکرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454827" target="_blank">📅 10:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a2df6454.mp4?token=s7La2Ag6yT7lYscIaiCrxd4Nbqz1D9luaYrGTDHz7CCCgMaGhSxcG_z1CaNv3lPaTJxATbZrvul2kKoqz8djzm4387PN3EJzgDokqgq41k5AEEgquSdPhNbjripcHCRelk49jbljrPmIJgIYYLjGIOMU9_oClzW8fG8IUAcM3P8E019OWyANASSadwhIdP-05MLSG73GWmVeq5JPkvgZzpBE7T0oJ2JNqN-Mr-1yWSHUEvSin65Zw6DeEQ4BW6eLhh1FpE89qf9TpZp-zusg_qiXBbFvVlx7KYm8uFSUoPmtncuuwOJMPjqpkIJluD2zzxgZT-GiqOd7Uaf2ajPBYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a2df6454.mp4?token=s7La2Ag6yT7lYscIaiCrxd4Nbqz1D9luaYrGTDHz7CCCgMaGhSxcG_z1CaNv3lPaTJxATbZrvul2kKoqz8djzm4387PN3EJzgDokqgq41k5AEEgquSdPhNbjripcHCRelk49jbljrPmIJgIYYLjGIOMU9_oClzW8fG8IUAcM3P8E019OWyANASSadwhIdP-05MLSG73GWmVeq5JPkvgZzpBE7T0oJ2JNqN-Mr-1yWSHUEvSin65Zw6DeEQ4BW6eLhh1FpE89qf9TpZp-zusg_qiXBbFvVlx7KYm8uFSUoPmtncuuwOJMPjqpkIJluD2zzxgZT-GiqOd7Uaf2ajPBYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سندرز: جنگ ترامپ با ایران یک فاجعه برای آمریکا بود
🔹
سناتور کهنه‌کار آمریکایی:  ترامپ، فاسد و زورگو است؛ جنگ علیه ایران یک فاجعه برای آمریکا بود.
🔹
ازنظر من، ترامپ خطرناک‌ترین رئیس‌جمهور تاریخ کشور است؛ او یک اقتدارگرا، یک دزدسالار و فاسد است که ما را درگیر یک جنگ وحشتناک کرده است.
🔹
وقتی به آن‌چه در آمریکا می‌گذرد نگاه می‌کنم، می‌بینم که مردم خواهان جایگزینی برای ترامپ هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454826" target="_blank">📅 09:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NASSF55JHHpKvge5d2NeHpX8BEwFT52pJm2ahYBL70I4Sb7HAzZxV5DfQHny-raE6wSMPHjB0uE7ENSLM9OSqnf4szZKtMy3wn6n8Wf1KUIWcKETeUcvtkmcXg9v8EgO1uJD3unBqL5RDOfrGr-ugIqFd3IdsDx7IMQ8Fs9cR-6L33wA2I7LpdWHm6uHbtyQSTnoEVN9yUTmvnVAwzK6nx5PfxyUcGwCIpbeUSUzBOnOytwTcxQs9MREk7TZjsan-kYEdr40skWq4vKgfaIi-sIDAjibJsUUf_7R5nuJVrDRXXVphyYFVHYXdP3UL88-METqkuQUsDdwOjb_FtjJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان: پروندۀ داعش را در افغانستان بستیم
🔹
سخنگوی طالبان: گروه تروریستی داعش در افغانستان به‌طور کامل سرکوب شده و تمامی مراکز و پایگاه‌های این گروه ازبین رفته است.
🔹
به هیچ گروهی اجازه داده نخواهد شد از خاک افغانستان برای اقدام علیه کشورهای دیگر استفاده کند.
🔸
آخرین حملۀ داعش در افغانستان مربوط به دی‌ماه سال گذشته بود که در یک رستوران چینی در کابل رخ داد و طی آن دست‌کم ۷ نفر کشته و بیش از ۱۳ نفر زخمی شدند و داعش خراسان مسئولیت آن را بر عهده گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/454825" target="_blank">📅 09:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57eed1925e.mp4?token=EFSxDVWfnlA_56o9bqy0lgMEWZXmUe89ZvePavq1iVxWkQopxZk7K-xpcqu2EMBdwoN0LwFga2vw5LDM-uy9Oqa-NHgh3R8KNs2cIHJQx2neoOmyUBZXCPSkas2jSe89f4vtx1bjP9CCfx25LafgwNhrXr7Xvcxj52Q72z-G-Zcj1oHlvITzTTcGWZ-ss_bflZMer41FHh_lauSb43tNA3VgwhJOQ5W94tyYNQ6iTfmg1miTQMgkIHWvg4RZDemA5CL0b8p6teWVmZ1zctJNQK5_UQA3_-biV7KBTszDJfytQa1YEdkEBAJaWNPQS6VErewsNkWmzXphKJ9QIeRlvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57eed1925e.mp4?token=EFSxDVWfnlA_56o9bqy0lgMEWZXmUe89ZvePavq1iVxWkQopxZk7K-xpcqu2EMBdwoN0LwFga2vw5LDM-uy9Oqa-NHgh3R8KNs2cIHJQx2neoOmyUBZXCPSkas2jSe89f4vtx1bjP9CCfx25LafgwNhrXr7Xvcxj52Q72z-G-Zcj1oHlvITzTTcGWZ-ss_bflZMer41FHh_lauSb43tNA3VgwhJOQ5W94tyYNQ6iTfmg1miTQMgkIHWvg4RZDemA5CL0b8p6teWVmZ1zctJNQK5_UQA3_-biV7KBTszDJfytQa1YEdkEBAJaWNPQS6VErewsNkWmzXphKJ9QIeRlvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدرسۀ تایلندی هدف تیراتدازی مرگبار
🔹
تیراندازی در مدرسه «دبسیرین نونتابوری» در شمال پایتخت تایلند، حداقل ۲ کشته و ۱۵ زخمی بر جای گذاشت.
🔹
پلیس تایلند فرد مسلح مظنون را شناسایی کرده و گفته او دانش‌آموز همین مدرسه است.  @Farana - Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/454824" target="_blank">📅 09:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aec540c79.mp4?token=mb0_6Af3dkLSOIEIJ1tnhKSkGdVPkECXG-y6UKHBAli40eb-g37vkqqS5SdfcbaO6aPjgEdzsui6Ftq6bWo6rD3eDOxniqejnbyxfHNXjcrlFMa6djcuupkVwUYbdGzJxtSEtwUU2a_WbB9eNnfWZ6IX4_mRaot7P1ZvzCPCYTeibGcV_aDUovZVboZvTmTzqVXCy7e82WRNsddIbAZru3cmPj3G5PdmAMSgqZj8IVV2TfhhYPl8C_hItSAJCBIGzsukyX5u4WXBaO-DiiOSNEREDT4Uyi8br8VFnHwcLwvrXrMp_sW8lPF4ssNCgx5B6ozXB9z79M-noJ3m0dF6Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aec540c79.mp4?token=mb0_6Af3dkLSOIEIJ1tnhKSkGdVPkECXG-y6UKHBAli40eb-g37vkqqS5SdfcbaO6aPjgEdzsui6Ftq6bWo6rD3eDOxniqejnbyxfHNXjcrlFMa6djcuupkVwUYbdGzJxtSEtwUU2a_WbB9eNnfWZ6IX4_mRaot7P1ZvzCPCYTeibGcV_aDUovZVboZvTmTzqVXCy7e82WRNsddIbAZru3cmPj3G5PdmAMSgqZj8IVV2TfhhYPl8C_hItSAJCBIGzsukyX5u4WXBaO-DiiOSNEREDT4Uyi8br8VFnHwcLwvrXrMp_sW8lPF4ssNCgx5B6ozXB9z79M-noJ3m0dF6Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدرسۀ تایلندی هدف تیراتدازی مرگبار
🔹
تیراندازی در مدرسه «دبسیرین نونتابوری» در شمال پایتخت تایلند، حداقل ۲ کشته و ۱۵ زخمی بر جای گذاشت.
🔹
پلیس تایلند فرد مسلح مظنون را شناسایی کرده و گفته او دانش‌آموز همین مدرسه است.
@Farana
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/454823" target="_blank">📅 08:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">انفجارهای کنترل‌شده در استان بوشهر
🔹
فرمانداری شهرستان دشتی اعلام کرد از صبح تا حوالی ۱۲ ظهر امروز، احتمال شنیده‌شدن صدای انفجارهای کنترل‌شده در حوالی شهر خورموج استان بوشهر وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454822" target="_blank">📅 08:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8e92a5bf.mp4?token=RLbJaM3GPq32Klx2x9bR9P6yIl1XU7JbQST-AOPZRj6NtGDjZ_BCOHEKXFEgQ8YGSdTkfQ6FlDc12YC4Hc1Z10xASo3Eh584apgIcA7dZng-eq5rfhU25biOr4z5RiIGIyl_uEMMfDMH8QjwLYqHyq_CfZPYxZkH9FjSSHl0y5HBKa-Msd69KzhziGLqC3caAoJ8tQDMHGI07N5rX5PHA-l1zmJ8zu--vc6QbEaIV1S0PT2T8BpO07C5U_6hu5LdfiXb96PzrFbGg2fN0cPQVK3LG4HIkeuiHzVZfsmtCFHD9DH-HKV0sO0fh_6WLIn592RDDEmLXu_EqEdHhqL7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8e92a5bf.mp4?token=RLbJaM3GPq32Klx2x9bR9P6yIl1XU7JbQST-AOPZRj6NtGDjZ_BCOHEKXFEgQ8YGSdTkfQ6FlDc12YC4Hc1Z10xASo3Eh584apgIcA7dZng-eq5rfhU25biOr4z5RiIGIyl_uEMMfDMH8QjwLYqHyq_CfZPYxZkH9FjSSHl0y5HBKa-Msd69KzhziGLqC3caAoJ8tQDMHGI07N5rX5PHA-l1zmJ8zu--vc6QbEaIV1S0PT2T8BpO07C5U_6hu5LdfiXb96PzrFbGg2fN0cPQVK3LG4HIkeuiHzVZfsmtCFHD9DH-HKV0sO0fh_6WLIn592RDDEmLXu_EqEdHhqL7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دختر شهید خلبان عباس بابایی از راز جاودانگی پدرش می‌گوید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/454821" target="_blank">📅 08:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454814">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I3Ju1pJ6Fbe7xs12wM3iBbskuYpq0489Auny4xS1dfwxsvCeXnMSQJfJKQQBc_dw4yP9Dnwq60A0uyRDli6ZZEQvWLQCMWxX8_kSCsryoxk8dxC0h-8Z_WUoUiZjmu52zY1f8RRG4RID8oXLVVdhKa6o4io1dAN3Xa_bx_wbeB41fIG3oPi-TjMu0jXpbCty086s0F6U5SSYhkUARtU02rtkBNs1rAwXV_qjC0WAQAK7GG8KoIGenHXyuauseNyzBOCG1mEv0o0N7exmmJwd4P7sTjhcMbWaJrX6JwGj_tcSLGi2mrLZCfiHmG6RyJcgAlgSKnL-m8TkId3dTyIahQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4W-WzPxLeHlStN8deWjBYxhR-OVE5WS-8qVPbI2CtdtLF7zCqQnwGSU3siHQYHXpW1k74F2yfiJEqoxExUc_wak5CErmMNnjYt_E33M3KnBYSnBr7M9wKcv3dYvXNhkb-_bLF8UkxISv13ZAQ4xYtu6BE7YaBQkIHvpm2A5xRFrUY1Udim3VAiyN9acXzsA1a6SiFJ-jj53fdzDMmxLFolcStCeIQlasR_TAQtXqD2x6NNxKJqoLi4rjrFHj8zKSyhAcgOKP_LoJKwhIdtBry3Zjk1rbCWfD4H3HZe-T_ZjWKw0cr_HuJw-RC3oLnpCuZux1U1xuCK0JtNeXSzPpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhHJKbv1uioU3aXBK870JCyb8pITaAIuKg1CQlzZxzvLvFd2ZsUWfgj-DoaXht_vuEIgDtOewX8xfWjmtXJSROVqXeKjwZmzQbXawCdH6ZM6yUY0-jet_KphwCnNyw06GlSg1_1f7BQsvlNeVRRdatExk1IEwVUKjvVSppmFIhcSHhiVLbICYb79NHDhdRZbRUQeY2GUzE9fNvZJG22hT1o19iWx2q-xNHJjV6Ko4B0CBAObtSkJZ64u_3D1DEr4V-hwPVkLprACGhdvRGQWPi8rPEJN04kewB2x7Sz9k1vKKhAtGm99vO_OCf0pTdqxe5RcCaTvLD9Alb8P8YNE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spdAySnG8pXnVCN6RJrc5tJB70xODwvx2rEVHdcLvD016RxvBLH2kJN69bfrjHc4ZT8yXDeqDZ4qPnRqmnj6Kfrkr2QIc5AjWU7TNa0I7V4t8R4xvPsM2DEd3TngfIte0WAvtYuk83vKhPJpeWBXw-Gfyr-Awo9Xko_8PPf3wVp8HQz0ghPRVHP959dqu0mGgpZTQi_DjeXRnotCZ1K9p-Bb4Oun6qB6oou7GpbA-gEXIgM4bxwFfqOru-Fg6rMY9OoMeYbY1OS7mie6RVg6HoH20xLAtOJ7bUp_iT1_Z6ymTJxsR7k9zqRjZzyS-Jnb6JPuwZ_XEV5zrmDEd4mfnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jwZjRXQmQWhxLI2CMVEBuJaNQ-cNkIffSidGFPJQwMwWXrHIXEoIU7S7OuOAkWMzZtbnsO_v0-wZMUdKOUV0gVDk768Pi2DwKHB2klTCUGhuoZWOt4N3wZaaXWe3joEujHAiZjOCso6zZuqiSlWrCaW-rXhCd9CbhKaFc30-9X-7oIJWyHfiFMJfh-tD6QLn_EOa4FW3R5SbFdekkCXbc5ca8c913WEvw0atGmYCH9AYsHgsVRdcuJ9hUxSDapuN-TaFX1a5ywBk4v8gqj07xzxVQGn3CHlZ3M5kCK0C-_bG9xc9tTgFbMCdCbvNb9eqnrjxzgDDFgChjJUCmzLlcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qy2e1YLV9irAoDzPyNkWhV0GiyoaP0OfIKXAfMSYJ78c7SYKbydnydGfAm8QWundOz1fN47nSSp38Zp42OoWe-BAOjGFfSOkoUgvOC7oojwxxMlEHG3kW86a-lDJZVoFYxdKPTH4Uq1ZxAsDjb0a9g0jIL6znLvtKE1yfg9zEIZBoVsgBJE6Twqsjjj4IIAXVgWTvQ550z6eltWMdCu_NDvUlc2rjV7cNcIxGUtDmjqkI-5JqjbIy4IIR42-QP-kU5YpJmfhkCF8FsWcPe9swxHlY9Ahxj7_9wZUDArEKwQJILw_ZLuzNebnOU4F49XmAWRt-Ytt_UwqdBFLsYEI8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWo9vsL0FFdAOrBI0KDtoGnm0doPpAdVtvh_5BCn53TJBB8bgccOcP2dfFFO5PSHvhIkDYPi4IRaQqPUAjUv0bg_-WK5KX54a8q-skOBikkKo-smJGAAF8E7L5iwWuGLHqExvUfdp8AuVxMK-hZG7UZd07BVM57Jdjow6H17DCLxqfek6Q8lZCX_rGzdqBx7LcqJdObeMH4Dw-GkFZmn2_t5KNKA2kEFBMBRAUz7syvM2b0_SkeoWy4As2rKCoUOMr9tIS_ctgYAwK-UYI5t6Q14vgP5DJYcjYZIovU2QSBtKZ8gQDzdMpHgmfyy2foOTSI9sZWY0fdrlIFZZN50Aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم عزای اربعین به میزبانی خانواده شهید سلامی در امام‌زاده صالح(ع) تجریش
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/454814" target="_blank">📅 08:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454813">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcxtdEE3fWZgnoVGfjPZ_AqXgPXWJSF5w5ZeBFETTo73cNH-DpgBrWmByox3lzCWWoNdevSJlv9rZMypDJppaxz1krHh6qquqkXcuDe2D1d-At31_buvaXaQ9tXd_4G39ca3VF_UME4EvqzVvTlMwYO-fv_YuQfnMU22sZC7cSR-7yQF9nl5zIvH6obu4TsN9tyrB_scwyzu-E_uULQzO_X1M77j45ZcZeqnHKAin54vNu4Lf4uJoeP1-Rm_bMGugbM67R0bpKgWgYW4XIig5z31IEdsyi3W2At3-dZPdKb130PwJgpLUZyuk_YZdvuhqnsZ6ShDBJZyW0c8upJPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ۵ دلیل اساسی: آمریکا بازنده جنگ ایران است
🔹
برتری نظامی آمریکا بار دیگر نتوانسته تضمین‌کننده پیروزی در جنگ باشد. با وجود گذشت ماه‌ها از آغاز درگیری با ایران، واشنگتن نه به اهداف خود رسیده و نه توانسته مقاومت ایران را در هم بشکند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/454813" target="_blank">📅 07:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454812">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX5G0jXv-hYoC-dEIKSKWnRVb2K44lwWa1IeADLwLznIkujDana7jfWEc8-GKuCK1TBxOS4n2pXG1kt-tkg19DB1iTTgcFnQfU_OX_kJpEHgDQqiO1Nvm0NxPxS5wxWDbiZLeuWkrBgGl0ArP62szVCPMxx1jxOOfruiCT7-dCViHGQFCzRu4wzJMTFXksxGyyIUAekyRnY6vxnqk8-bTQCUAVOcpwOfEwZkh4neiX7KQ_xqyN-wUb_4AolpjmgdD8mrVppEvvVHxPPpHHqPXvE4iRp6jUmUcjDnI1ZLfTkD1NL3vbnFzWh5ysD0-CmRWS2_a1u51f63njS0FULaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظارت سه سالۀ دولت آمریکا بر خالق چت‌جی‌پی‌تی
🔹
وزارت دادگستری آمریکا اعلام کرد اپن‌ای‌آی و شرکت استاتسیگ با توافقی حقوقی موافقت کرده‌اند که بر اساس آن، شیوه‌های استخدامی این دو شرکت به مدت سه سال تحت نظارت قرار می‌گیرد.
🔹
این توافق پس از ادعای مقام‌های آمریکایی دربار۸ محدود کردن فرصت‌های شغلی برای شهروندان این کشور و تسهیل مسیر اقامت دائم برخی کارکنان مهاجر انجام شد. هرچند دو شرکت تخلف را نپذیرفته‌اند، اما پذیرفته‌اند در مجموع ۳.۲ میلیون دلار پرداخت کنند که شامل جریمه و جبران خسارت احتمالی است.
🔹
طبق این توافق، اپن‌ای‌آی و استاتسیگ باید سیاست‌های استخدامی خود را اصلاح کرده و گزارش‌های دوره‌ای دربارۀ روند جذب نیروی داخلی و خارجی به وزارت دادگستری ارائه دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/454812" target="_blank">📅 05:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454811">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e4d1033f.mp4?token=pFqF-0hmPgY7N8hyaE9JDBoHEFMBINntrwL82jcq2ix7ipki_jfoKoBJPBP-r5Ac5G1ZxeaxIwci44SYS2a9JGq2O2aXjDNOPzgu5_tnDw7jY5GPvqOupSSG6TmvLVjBRIyI4vb5XlnKta_wGiXWeW6n0h0_MDsBpvXwX7FXqZehCgW7x4bV5QdBdQts6P5cfI3PVGo8mTZYlu6TUIjZdzxKvikBYdrEnlpqEf9jTqpa1OfTdFQYpy7NbgHbNUwyhfffgJ2wwEnJM38neWqaNU1lrPE9WU92Y2ZMPAUSoAPKZluHensc7tT4lhkvDAZiACEMTMeA6CwxgWsxSv2J6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e4d1033f.mp4?token=pFqF-0hmPgY7N8hyaE9JDBoHEFMBINntrwL82jcq2ix7ipki_jfoKoBJPBP-r5Ac5G1ZxeaxIwci44SYS2a9JGq2O2aXjDNOPzgu5_tnDw7jY5GPvqOupSSG6TmvLVjBRIyI4vb5XlnKta_wGiXWeW6n0h0_MDsBpvXwX7FXqZehCgW7x4bV5QdBdQts6P5cfI3PVGo8mTZYlu6TUIjZdzxKvikBYdrEnlpqEf9jTqpa1OfTdFQYpy7NbgHbNUwyhfffgJ2wwEnJM38neWqaNU1lrPE9WU92Y2ZMPAUSoAPKZluHensc7tT4lhkvDAZiACEMTMeA6CwxgWsxSv2J6YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانواده مستحکم می‌خواهی با همسرت مؤدب صحبت کن
🎙
آیت‌الله جاودان
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/454811" target="_blank">📅 04:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454810">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دستور ترامپ برای تحقیق دربارۀ عاملان افشای کمبود ذخایر تسلیحاتی آمریکا
🔹
روزنامۀ وال‌استریت‌ژورنال به نقل از منابع آگاه گزارش داد ترامپ دستور انجام تحقیقاتی دربارۀ افشای اطلاعات مربوط به ذخایر تسلیحاتی آمریکا را صادر کرده است.
🔹
در روزهای گذشته رسانه‌های آمریکا گزارش‌های متعددی دربارۀ کاهش ذخایر موشک‌های رهگیر این کشور منتشر کرده‌اند.
🔸
پیش از آغاز جنگ توسط ترامپ در پنج ماه پیش، رئیس ستاد مشترک ارتش آمریکا و دیگر مقامات ارشد به ترامپ اطلاع داده بودند که کارزار نظامی علیه ایران می‌تواند ذخایر موشک‌های پدافند هوایی و موشک‌های تهاجمی را به‌شدت کاهش دهد.
@Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/454810" target="_blank">📅 03:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454809">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ادعای سعودی‌ها درباره حملۀ انصارالله به نجران
🔹
ائتلاف عربستان سعودی مدعی شد بر اثر حملۀ انصارالله یمن به منطقه نجران ۱۱ غیرنظامی زخمی شده‌اند.
🔹
شبکۀ المسیره به نقل از یک منبع گزارش داد نیروهای مسلح یمن عملیاتی را علیه مراکز فرماندهی استقرارهای نظامی عربستان در مناطق الرویک، العبر و الثنیه انجام دادند.
@Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/454809" target="_blank">📅 03:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454808">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عربستان، ترکیه و پاکستان توافق دفاعی امضا می‌کنند
🔹
خبرگزاری رویترز به نقل از یک منبع آگاه گزارش داد که ترکیه، عربستان سعودی و پاکستان امروز در ریاض یک توافق مشترک دفاعی امضا خواهند کرد.
@Farsna</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farsna/454808" target="_blank">📅 02:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454807">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PjRBR3brWBMMB-NRC2O72SJo8g45EQVcSfHpfqHXGePtCvFrZGd8G9NYli0WQNwBMgzmWlNBVfmO2YG6UAizzY3h-ThBe8zJ6RiZbfX34nckcBOYwA_Brl5c14Pt-JeWbRN3GgCOG0IUsx-ardzhxEDKVvOBvj11iJ39x5howsceaMdb_BpgEwsZhCgLg8g_lVh937eJSz0k5-Bgf7VXJlGrfKeWp3ELKABfctvWWuUH98TlBC5iUd4rwcE_LkjGqvTSk1JIxHK2cFd_vgA9QpTCtJVY3W5y1GyCc0y5RvFjsrn6hqMWrBrsHXeBm8iUxa4ij2BH3Zt2KsClRN7ADg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رد پای موساد در بحران مهاجرتی اخیر اسپانیا
🔹
محافل اطلاعاتی و دانشگاهی چین گمانه‌زنی می‌کنند که اسرائیل بحران اخیر مهاجرت دسته‌جمعی در منطقهٔ خودمختار سئوتای اسپانیا را طراحی کرده است.
🔹
به گزارش روزنامهٔ ال موندو، در پکن گزارش‌هایی در دست است که بر اساس آن‌ها، هجوم مرزی یک عملیات حساب‌شدهٔ جنگ ترکیبی به رهبری موساد بوده که با همکاری مراکش برای بی‌ثبات‌سازی دولت اسپانیا اجرا شده است.
🔹
این ارزیابی راهبردی بحران مذکور را به طور مستقیم به تیره‌تر شدن روابط دیپلماتیک میان اسپانیا و اسرائیل مرتبط می‌داند.
🔹
اسپانیا به صراحت از نسل‌کشی اسرائیل در غزه انتقاد کرده و به صورت رسمی دولت فلسطین را به رسمیت شناخته است. این موضوع واکنش تند تل‌آویو را به همراه داشته.
🔹
«نادیا حلمی»، دانشمند علوم سیاسی اهل مصر و متخصص روابط چین و اسرائیل، گفت که تحلیلگران امنیتی پکن رویدادهای سئوتا را به‌عنوان یک کارزار فشار عمدی علیه دولت «پدرو سانچز»، نخست‌وزیر اسپانیا، ارزیابی می‌کنند.
🔹
نظریهٔ اطلاعاتی مطرح‌شده در پکن، در میان دیپلمات‌ها و تحلیلگران سیاسی نزدیک به نهادهای حکومتی چین به‌طور فعال مورد بحث است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/454807" target="_blank">📅 01:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454806">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تهدید یمن به سرنگونی نظام حاکم بر عربستان
🔹
وزارت امور خارجۀ یمن به مسئولان عربستان سعودی هشدار داد که اگر به سیاست‌های استعماری خود ادامه دهند، باید منتظر نابودی نظام حاکم بر این کشور باشند.
🔹
یمن تأکید کرد عربستان با فعالیت‌های استعماری خود به سمت مسیر بی‌بازگشتی حرکت می‌کند که ممکن است صفحۀ تاریخ جنایتکارانۀ آن را ببندد.
🔹
این نهاد یمنی مجدد هشدار داد که میل به استعمار، فقط به نابودی رژیم سعودی منجر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/454806" target="_blank">📅 01:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454805">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a338c308bc.mp4?token=k9D0wFeNCL5bRbq4Yb9aF4mDA_ixWpPfghL8CTqcbX-C-zTs77_a60jf8h9MEdxm3pkkGADXJurXoE239hAYL87z4DRnyuLBSRWaHn0jMKWodJMiJS7rQDoEa-CP96wLPKv-OPBu02MzlEWCVY_NRIA3qRJb74ix7DLrJXHwvyYuVy-91lbOibkUtLOZLJkowTu7M6EF1TTH-rlOyTrlr5N6tiMJQeMPwiMK1JqBM_Q-yMuTVuutfDi6m-L5dzp3xfqRwDZ60qxTf_3bEqyoowglJw20aWdwrjrtFdBA0cp1vI7Qg8tAZZf6vb11MFgKty-MsopgWxekbC0UXDn0x3vP5gMO7S2GTdqBh08qK1Ci_o44BFeQwdMw3ZK-RvnHUOWIItytkuewJIlmpNexULUj_9UyvuSb0_xEVQC6Hgv7AGSu5cv4sUjJo2pbXxtGf6wtqfSw07aNDcuWxSB6TtSBhYGbeFovUaff_vvM0v1WrL0hl6UnFXwTKhA_g60Ki5jKsyO-UlhesCMn8ttLgRHF6B6gnzFSanq7j9KVwb9LhEphrozrK7o5lV8OjNqathOE5avgrVRv_U4OTKc-KvzJklVihKjoFqUYIbDpKjz09PZrpkcXAIJLsAfA9DIYtVer3T8TsuNHoaZhyyqXUkyURRrr4Xd9hUFv3QhcstU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a338c308bc.mp4?token=k9D0wFeNCL5bRbq4Yb9aF4mDA_ixWpPfghL8CTqcbX-C-zTs77_a60jf8h9MEdxm3pkkGADXJurXoE239hAYL87z4DRnyuLBSRWaHn0jMKWodJMiJS7rQDoEa-CP96wLPKv-OPBu02MzlEWCVY_NRIA3qRJb74ix7DLrJXHwvyYuVy-91lbOibkUtLOZLJkowTu7M6EF1TTH-rlOyTrlr5N6tiMJQeMPwiMK1JqBM_Q-yMuTVuutfDi6m-L5dzp3xfqRwDZ60qxTf_3bEqyoowglJw20aWdwrjrtFdBA0cp1vI7Qg8tAZZf6vb11MFgKty-MsopgWxekbC0UXDn0x3vP5gMO7S2GTdqBh08qK1Ci_o44BFeQwdMw3ZK-RvnHUOWIItytkuewJIlmpNexULUj_9UyvuSb0_xEVQC6Hgv7AGSu5cv4sUjJo2pbXxtGf6wtqfSw07aNDcuWxSB6TtSBhYGbeFovUaff_vvM0v1WrL0hl6UnFXwTKhA_g60Ki5jKsyO-UlhesCMn8ttLgRHF6B6gnzFSanq7j9KVwb9LhEphrozrK7o5lV8OjNqathOE5avgrVRv_U4OTKc-KvzJklVihKjoFqUYIbDpKjz09PZrpkcXAIJLsAfA9DIYtVer3T8TsuNHoaZhyyqXUkyURRrr4Xd9hUFv3QhcstU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرۀ شنیدنی سردار شهید ایزدی (حاج رمضان) از حاج قاسم
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/454805" target="_blank">📅 01:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454804">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/254b28154f.mp4?token=tOAwFqJE3TKUXIZ0gaPDUPLEG8oUZZN6rmI7wKt7IgW7OY3kw7ETy4hzq7HUQw8T3gLbNbBUE3ID742lJoz9ifeC8_da5nOwm5EkFAtbg9g_Tcaj4CXeG3d6jfa-O0HZ1nFSdvVFJ1rHgccG-DjIE2AKMQDRmdeDyUso1kzdvlIOou_fQZy2EsrFubLeOoHC_isQp8g4MaRzoSbULg1Vex-28nWvb07M4zuYldwG-x9V88YBH7rrOIbvYwfPzZY-XlwyH4hAc_6_-8dCAXHu8_V9lsNLa6arH-5KrSEkEsZYn_kUUYJgqqd1OT-pb76_sbVTuSLjfaf9vcOpUOM6_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/254b28154f.mp4?token=tOAwFqJE3TKUXIZ0gaPDUPLEG8oUZZN6rmI7wKt7IgW7OY3kw7ETy4hzq7HUQw8T3gLbNbBUE3ID742lJoz9ifeC8_da5nOwm5EkFAtbg9g_Tcaj4CXeG3d6jfa-O0HZ1nFSdvVFJ1rHgccG-DjIE2AKMQDRmdeDyUso1kzdvlIOou_fQZy2EsrFubLeOoHC_isQp8g4MaRzoSbULg1Vex-28nWvb07M4zuYldwG-x9V88YBH7rrOIbvYwfPzZY-XlwyH4hAc_6_-8dCAXHu8_V9lsNLa6arH-5KrSEkEsZYn_kUUYJgqqd1OT-pb76_sbVTuSLjfaf9vcOpUOM6_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهید حاج قاسم سلیمانی: ما در زندگی خودمان باید به الگوهای بزرگ نگاه کنیم؛ عمر ما می‌گذرد، تمام می‌شود، همه می‌میریم؛ اما انتخاب راه درست خیلی مهم است.
@Farsna</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/454804" target="_blank">📅 01:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454803">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترفند سادۀ هکرها، غول‌های مالی آمریکا را غافلگیر کرد
🔹
گزارش جدید پژوهشگران امنیتی گوگل نشان می‌دهد گروهی از هکرها موفق شده‌اند به چندین شرکت بزرگ مالی و سرمایه‌گذاری در آمریکا نفوذ کنند و پس از سرقت اطلاعات حساس، قربانیان را با تهدید به انتشار عمومی داده‌ها تحت فشار قرار دهند.
🔹
به گفتۀ محققان، هدف اصلی این حملات دستیابی به اطلاعات محرمانه و سپس اخاذی از شرکت‌ها در ازای عدم افشای آن‌ها بوده است.
🔸
هکرها با تماس تلفنی با تلفن‌همراه شخصی کارکنان و جازدن خود به‌عنوان همکار یا کارشناس فناوری اطلاعات آن‌ها را فریب داده‌اند تا اطلاعات ورود و کدهای احراز هویت چندمرحله‌ای خود را در وب‌سایت‌های جعلی وارد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/454803" target="_blank">📅 01:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454802">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بمباران غزه توسط رژیم صهیونیستی
🔹
المیادین: توپخانه اسرائیل شمال شرق شهر غزه را بمباران کرد.
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/454802" target="_blank">📅 00:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454801">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoQdak9GynG0lI93PbxfTJRzhpd0Vn3zy70OG3FqOJQB0Jf_Dv0uPByDHMuCUmIcdzh3PrZYWP6teARZHebtCL1QhpkOrMJdyKi_jrnMxtBvZPrKOEQwDwGd2S5043S9HkvjbsAnq7bGHZ8Q-LLtnpPetLvJd2qkk7zBKw7RG8Rr8T9SFKZ42j_lKKh3ud5H2mrBS9wYXCPdzxCZy1uaNk2L5peZZdyrEkuBVUxZAds-CQMR8N2fk7TAxzL7i_vXIRASYqnQlxrie_0w5UVWlJcXUhjRtbdMhCkKcU_-IoPVAdS6vcQy68GvP_H76eYrhO1JvYBlrKd8rIqhrODp7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توقف بی‌سابقۀ صادرات نفت عربستان به آمریکا
🔹
در ماه جولای سال جاری صادرات نفت عربستان به آمریکا به صفر رسید؛ اتفاقی که در ۴۰ سال گذشته بی‌سابقه بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/454801" target="_blank">📅 00:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454800">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ: ایرانی‌ها علی‌رغم محاصرۀ دریایی آمریکا، قادر به کاشت مین در تنگۀ هرمز هستند
🔹
رئیس‌جمهور تروریست آمریکا مدعی شد که جنگ با ایران به زودی به اتمام می‌رسد.
🔹
او گفت هیچ‌کس نمی‌خواهد کشتی چند میلیارد دلاری‌اش را به خطر بیندازد و در تنگۀ هرمز به مین برخورد کند.
🔹
ترامپ بار دیگر با اظهاراتی متناقض گفت کنترل تنگۀ هرمز دست آمریکا است، اما اندکی بعدتر مدعی شد توافق بر سر بازگشایی تنگۀ هرمز به‌زودی حاصل خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farsna/454800" target="_blank">📅 00:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydtxjff2A8Jd9lrzYL4pk6FHa9uCoOSZjQHctcfLUD7IfHS5_Ynt3Qva_n__1XY_g8RvABbIU6l6Hp8xjOJcndic74WO2yopCMysL1mL3C3QuuZuiykVLV3JnAywVIuNGIUlmJe4Us3yULMVliIWllozHjjIdXwxsNXKR4Zi8YsUs7tCZsD0wf7TV1rh9dgdELiS5jRo3XZjKSdzkkVQpqwKECGTILDDnIBvy_dC5KoB_IKtT3YwS4dGT1sRvBnThIf5WTP2N_SUpfBqTjwcIJd-kkHdtL8YlAbJ6gZ0e7dcD-zeo-Y4aipOiCB-Jbnm4JVnQtafu4s0hJXHp1W5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل در دورۀ آتش‌بس غزه، ۳۰۰ کودک را به شهادت رساند
🔹
یونیسف اعلام کرد از زمان اعلام آتش‌بس در اکتبر ۲۰۲۵، حداقل ۳۰۰ کودک در نوار غزه به شهادت رسیده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/454799" target="_blank">📅 00:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454798">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGc9RNdbZWFJfucrVMV7_CVOuCs8AJ1IZJHo2UmTL_-OINwWkkx4CR9uoJAzQUhRTrUcCWmtVAzLMu4ZhAi4Yb0a8niVW6X_O29QYjco7Zy9BKmmqnZJy0rX9L5twvegWSyvF9fAXln3754rFzaI-gSXtgy_nbQRzyYt01ygOQaesxsc38jA_pzUbk2dFtOVV7DpGzHLE_NUS2Aoo-Dnm-ydrINbY2ZEwn4yx5XCOo81CqUCfgxdXKxSvVZ2xOT_dUDdPiNjW6-6Q7YUC_fEZMqp1qWNLf1wniT1PLSWnMnhgpjNNCjcnVwGhxVqKOtmb1ANXv0b-oxpTtzpPYHIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویۀ ۱۰ کشور در دریافت هزینۀ‌ خدمات دریایی از کشتی‌ها
🔹
در هفته‌های اخیر، هم‌زمان با مطرح شدن ایده دریافت هزینه از کشتی‌های عبوری از تنگه هرمز در ازای ارائه خدمات ایمنی، مدیریت ترافیک دریایی و راهنمایی ناوبری، برخی دولت‌های غربی و شماری از رسانه‌های بین‌المللی این اقدام را مغایر با حقوق بین‌الملل توصیف کرده‌اند.
🔹
با این حال، بررسی رویه‌های موجود در مهم‌ترین آبراه‌های جهان نشان می‌دهد که دریافت پول از کشتی‌های عبوری در ازای ارائه خدمات پدیده‌ای رایج و پذیرفته‌شده در بسیاری از کشورهاست.
🔹
گزارش اخیر روزنامه فایننشال تایمز نیز با استناد به تحلیل بانک JPMorgan تأکید می‌کند که اگر ایران و عمان دریافت هزینه را در قالب «هزینه خدمات ناوبری، ایمنی و مدیریت ترافیک دریایی» تعریف کنند، چنین سازوکاری می‌تواند از منظر حقوق بین‌الملل قابل دفاع باشد؛ الگویی که پیش‌تر در نقاط مختلف جهان نیز اجرا شده است.
🔗
مهم‌ترین نمونه‌های شناخته‌شده این رویه را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/454798" target="_blank">📅 23:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a322b4c6ed.mp4?token=OPWn_x6Ki0CDjXBWOXqJ-_tb18KH5jbqWXKHu_XgOS1qqTDVPC6BxR0Tzj5yXVGzB7xvn_6wWQx17OGjtdi5c1SabShGUV-8oy2KJJZ3U073O2AMGgcSkdKsHbS_KCFfs4iqoUUfq-_bZqxusJ8O3H2GM8Ku5xkQECadr18OyJOo2meONLAsK7zL5ngBxlnto7dV26Du7q6MFclJeAJQ1hotBJ5pPU7TwoiTBgCQLxc9hGwdHMDhfQ4C6kVl6RDMcN6-jxjq68AZsHDrvPS6OxepLkE2RJrGiT9pdggFQmOlPgqdslH55kTAWe5gvWsezDwI4MxVjzk34bM1nb_40iC5_qf2SX-jQY3U_TaedlS2_2WEQJmKIaAUBUCq3ozmBZFY_ZNDLnwrKRjAD3IZKYZop2Q1adIj7SQEl9x65V0ESnCnUAxjQn8W80NlXohvmHJsIHb2ENLWiKDobKrg2grGw8G7iJvqDu0S_WIN8GVr0YvMA4nJD_zhXilOCfki-WWZ3YHswSFXL-MK0KMxXxd1yxk2aDuCksMO4ADcyLaz1kCI398KmKG6mmoFMpve_HDHavEzkwi19hQP3i2Tm8von738_65ErnrGL1ZXMEhB7NbcfCyrSCtwpAMPiwRpr1CVEN2PnwwYxOTYJSttkaEuZW7ezE8jdwMoHBDaCK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a322b4c6ed.mp4?token=OPWn_x6Ki0CDjXBWOXqJ-_tb18KH5jbqWXKHu_XgOS1qqTDVPC6BxR0Tzj5yXVGzB7xvn_6wWQx17OGjtdi5c1SabShGUV-8oy2KJJZ3U073O2AMGgcSkdKsHbS_KCFfs4iqoUUfq-_bZqxusJ8O3H2GM8Ku5xkQECadr18OyJOo2meONLAsK7zL5ngBxlnto7dV26Du7q6MFclJeAJQ1hotBJ5pPU7TwoiTBgCQLxc9hGwdHMDhfQ4C6kVl6RDMcN6-jxjq68AZsHDrvPS6OxepLkE2RJrGiT9pdggFQmOlPgqdslH55kTAWe5gvWsezDwI4MxVjzk34bM1nb_40iC5_qf2SX-jQY3U_TaedlS2_2WEQJmKIaAUBUCq3ozmBZFY_ZNDLnwrKRjAD3IZKYZop2Q1adIj7SQEl9x65V0ESnCnUAxjQn8W80NlXohvmHJsIHb2ENLWiKDobKrg2grGw8G7iJvqDu0S_WIN8GVr0YvMA4nJD_zhXilOCfki-WWZ3YHswSFXL-MK0KMxXxd1yxk2aDuCksMO4ADcyLaz1kCI398KmKG6mmoFMpve_HDHavEzkwi19hQP3i2Tm8von738_65ErnrGL1ZXMEhB7NbcfCyrSCtwpAMPiwRpr1CVEN2PnwwYxOTYJSttkaEuZW7ezE8jdwMoHBDaCK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
واکنش پزشکیان به اقدام مادر کردستانی که پول دیه دخترش را خرج مدرسه‌سازی کرد
🔹
این که شما پول و سرمایه داشته باشی و ببخشی، یک موضوع معمولی است.
🔹
افرادی مثل این مادر عزیز وقتی که این عمل را انجام می‌دهند، در واقع همه چیزی که دارند را خرج می‌کنند و این مصداق…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/454797" target="_blank">📅 22:56 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
