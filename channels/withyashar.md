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
<img src="https://cdn4.telesco.pe/file/J6r9tZxRO4eNbrP2lPqKH-RUN99cSDkWzpkN8GgCVLOJiefheeaat28s9bS-1dmjsem5Emjxwc4wlfNI51Ah_WL5hb_bj5NtpktWV3UgSnTy0-PsVcevBK219D19kueDwUQlL1xOfoMYCioomekLqJWdulzToze98Nq1Y8qeUHoWQENGOmbSfNdHOb8R-9MP9R-qpPjAjtFtmQuTeM76RmpA2x7AMUkVpdad0PaR1U12EpJDW1VGsvMTtluTlCSiisWGa18r3_-tdClU0_VBsmhJqBSuXD9Ko93jLV7jOfEQZhN1T838wEDkkk0zQhPjBhPhSUt_zwBrboWVjuAKDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 442K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 12:48:11</div>
<hr>

<div class="tg-post" id="msg-21330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رویترز : آمریکا روز دوشنبه تحریم‌های اقتصادی جدیدی علیه ایران اعلام می‌کند که احتمالاً خریداران بزرگ نفت ایران، از جمله شرکت‌های چینی، را نیز هدف قرار خواهد داد
@WarRoom</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/withyashar/21330" target="_blank">📅 12:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21329">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKnWTBCirpuSDjaGyVZWgEWOIah1xKNfqE18V4XJ44om26AefjcoL_skcraTj4fFs8T6p7XWfbANKCbHlCd4tUdAZRYFYA6oqWluzFhPV0dnriTGxNZxxjcZY9XbO3KTb95_oi-si8I--26hwDz3YjHsjGYZTOJJpYxzdiMm_8sh8gvHeqS9BUiBt4q7VX5Goq3Tc_yLXqaicW5GpYEz4XAtuK8nQGbPAyBuqr4EV4rVYppP1KUagIlOawXTi0-QFMZmRten0Ij-2GWFHl5_gBNvxwrXmNSPVHgsahMJFKzaVtg-QaRyVknRH0TRiTzLN2leVc615o5uV18ue48R6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">lكارنامه شاهزاده رضا پهلوی ، كتبى ١٨.٠٤ و معدل شفاهى ١٨.٧٢ ، انضباط ١٨!
@WarRoom</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/withyashar/21329" target="_blank">📅 11:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21328">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvWNHIM20BYV4FwigY12HUk_ekDJFSzeOdL3RCQFS5GsC908x4TuVd8YF9bClaykrjW5F2o1Hgx2p0nnEQlWIvstB8DDgu-KdHou7thotgtR0sUNSvSkQGl11TsqA8-XI6SQ-I4YYmL1gJMHxUB_hYxo2E_8fq1MLNrXTwlTTiaVMCU0_6wDgtpn9cnLmBUqqmC8SSjOqZCqSk8X1NbH_9Y7TdhPRP561TRgeJ7h3M27udFn6lzPwVI7KIONkrL4u7eaP_58tFmNRw2Befhw_OqPi2Vlz10rb3j6_iCXXzr8GbJys5nW3H-eh6JEr4PRXpbMwtVoIjEM1G8QYRD82A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک تانکر نفتی، با نام "ال ماقام"، شب گذشته تحت نظارت هوایی شدید نیروهای آمریکایی با موفقیت از تنگه هرمز عبور کرد، در حالی که سیستم AIS آن غیرفعال بود.
@WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/21328" target="_blank">📅 11:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21327">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یاشار : کتاب اوستا ، یسنا ۴۳.۱ آمده:
«اُشتا اَهمایی یَهمایی اُشتا کَهمایچیت»
«خوشبختی نصیب کسی می‌شود که برای دیگران خوشبختی بخواهد.»
@WarRoom</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/withyashar/21327" target="_blank">📅 11:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21326">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تابناک : گویا راه حل چهارمی برای بنزین پیدا کردن!
کیفیتو انقدر پایین آوردن که مردم از ترس خراب شدن ماشینشون دیگه بنزین نزنن… دولت با همین ترفند ساده، مصرف رو کنترل کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/21326" target="_blank">📅 10:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21325">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مدیرعامل شرکت نفـت ستاره خلیـج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
انجمن خودروسـازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متـانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.
مدیرعامل شرکت نفت ستاره خلیج فارس: استفاده از متانول در سوخت در کشورهایی مانند چین، آمریکا و اروپا تجربه شده و این ترکیب هیچ آسیبی به خودرو وارد نمی‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/21325" target="_blank">📅 10:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21324">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آمریکا و کانادا در تلاش خود برای دستیابی به توافق تجاری شکست خوردند و به همین دلیل واشنگتن از صبح امروز، 50 درصد تعرفه بر محصولات کانادایی به ارزش حدود 20 میلیارد دلار اعمال کرد. مارک کارنی، نخست وزیر کانادا، در پاسخ به این اقدام، تعلیق مذاکرات با آمریکا را اعلام کرد و گفت که کشورش به تعرفه‌های جدید «دلار در برابر دلار» پاسخ خواهد داد. این تصمیم پس از سه روز مذاکره متوالی در واشنگتن بین دومینیک لبلانک، وزیر کانادا، و جیمیسون گریر، نماینده تجاری ایالات متحده انجام شد ، تعرفه‌ها بر محصولاتی اعمال خواهد شد که حدود 5 درصد از صادرات کانادا به ایالات متحده را تشکیل می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/21324" target="_blank">📅 10:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21323">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پاکستان برای هزینه میانجیگری بین ایران و امریکا ‌۱۰ میلیارد دلار درخواست کرد
@WarRoom</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/21323" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21322">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8d76ce15.mp4?token=kkTbAGEEezKlCsPDbH6VhCTwaTxqgj71uQRA0pI3LMAOks2dag8VKloinbl3fXXfiV9r8MhU1r8E6yJoiOknBq6uHML4JSZ3vHYznrnCBehma-ovT039AhnQ7sLQH82hEFnBE9KlmC2LfAWFjuZtLUwbtNBviPMwp1NwdPLHxSrwD1Wi7e0jImDB0hUQlTo4Emi57qszoO1MLy6PZk0JzYN_wMFqtg063Ln8rsmOrlTcLq3h2T0jw6A7rz-znegc-hKXt9xorppn2vSRQ4vRb8eRtpT4mY3GP6gI-iEj540oL_u-WLe8-3vGFs26hd6nAAP8n_twKbS7UttPiwLbSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8d76ce15.mp4?token=kkTbAGEEezKlCsPDbH6VhCTwaTxqgj71uQRA0pI3LMAOks2dag8VKloinbl3fXXfiV9r8MhU1r8E6yJoiOknBq6uHML4JSZ3vHYznrnCBehma-ovT039AhnQ7sLQH82hEFnBE9KlmC2LfAWFjuZtLUwbtNBviPMwp1NwdPLHxSrwD1Wi7e0jImDB0hUQlTo4Emi57qszoO1MLy6PZk0JzYN_wMFqtg063Ln8rsmOrlTcLq3h2T0jw6A7rz-znegc-hKXt9xorppn2vSRQ4vRb8eRtpT4mY3GP6gI-iEj540oL_u-WLe8-3vGFs26hd6nAAP8n_twKbS7UttPiwLbSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ما مجبور بودیم سلاح هسته‌ای را از ایران بگیریم. ما مجبور بودیم این کار را انجام دهیم.
این باعث افزایش ناگهانی قیمت نفت شد، نه به آن بزرگی که مردم فکر می‌کردند، اما باعث افزایش ناگهانی قیمت نفت شد. قیمت‌ها خیلی زود حتی از قبل هم پایین‌تر خواهند آمد.
@WarRoom</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/21322" target="_blank">📅 09:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21321">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5a0b2336.mp4?token=E-EM9KVuDwAVmXAD7xCO5ixqbXMKqBuJepOuQvl4qyznR524DnF_5Ah3q9RkD37Ak-96oRmJg3mqreZSp6F2NXdEXZ0koDMp_JZa0kVMD-Y85MqPYsrZKCKbDj3Ud1fkZfWHvwjkP5UEphNYxXt3Dq6zzL_cqAVUZ9vxHcobkTitdgEh9I-NSMX2nASXhgYRQL2yp8r4BWg4CiSBbOnHK1XEYPatu5bRrZwSW8awO9nJdq0NtCZkhSECqJ_zhicYfYVHFlB6MuZPGLKgl1RQhz_sw_IUHIsRdKhKTbNgoueNGOkAdqSkmjV_Fb0Gqs353vbVs4tdVNqCgYZg7SmayA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5a0b2336.mp4?token=E-EM9KVuDwAVmXAD7xCO5ixqbXMKqBuJepOuQvl4qyznR524DnF_5Ah3q9RkD37Ak-96oRmJg3mqreZSp6F2NXdEXZ0koDMp_JZa0kVMD-Y85MqPYsrZKCKbDj3Ud1fkZfWHvwjkP5UEphNYxXt3Dq6zzL_cqAVUZ9vxHcobkTitdgEh9I-NSMX2nASXhgYRQL2yp8r4BWg4CiSBbOnHK1XEYPatu5bRrZwSW8awO9nJdq0NtCZkhSECqJ_zhicYfYVHFlB6MuZPGLKgl1RQhz_sw_IUHIsRdKhKTbNgoueNGOkAdqSkmjV_Fb0Gqs353vbVs4tdVNqCgYZg7SmayA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: الان میگین چه غلطی باید بکنم؟
برگردم، کمی بیشتر ایران را بمباران کنم؟
جمعیت : آررررررررره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/21321" target="_blank">📅 03:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21320">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e05213aef.mp4?token=NvakRGOp3ypTehXSAIHcO4OE4x9rsvyPVkcvJr54JYrJ_OJzQZMa0dJoAfy6FyL-Mn4Ca0KYCw8HXVXLvNgP0dcD0mzFDw3G6JSRPOn1UYjwUZy4biQJzdg9vZjupUsmIxgoMw-p93RfKP9zzTc5KFAx6sGc8QObWE-o5prXfvBNJnpJX_HFmghwOZwMAlnHqEaCpGQRmuU_QusjfIw5S-nJUsxvi0ArGBSHqQ-Zs3PAnyas3F7RwZjZUDjxcqOgrgA2yLRmwS0LMV2DRGCxnOZivixoZM_rl_i_brfUMCavMGv8OpXQFaQbCBlk5m8UrTh-Jb1hrOLmDahGTJFhmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e05213aef.mp4?token=NvakRGOp3ypTehXSAIHcO4OE4x9rsvyPVkcvJr54JYrJ_OJzQZMa0dJoAfy6FyL-Mn4Ca0KYCw8HXVXLvNgP0dcD0mzFDw3G6JSRPOn1UYjwUZy4biQJzdg9vZjupUsmIxgoMw-p93RfKP9zzTc5KFAx6sGc8QObWE-o5prXfvBNJnpJX_HFmghwOZwMAlnHqEaCpGQRmuU_QusjfIw5S-nJUsxvi0ArGBSHqQ-Zs3PAnyas3F7RwZjZUDjxcqOgrgA2yLRmwS0LMV2DRGCxnOZivixoZM_rl_i_brfUMCavMGv8OpXQFaQbCBlk5m8UrTh-Jb1hrOLmDahGTJFhmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
آن بمب‌افکن‌های B-2 یک سال پیش به امید ایران برای دستیابی به سلاح هسته‌ای پایان دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21320" target="_blank">📅 03:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21319">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33aa06c32.mp4?token=F0zmX0MpjPKR73PenA4h2C-qmVrBBVS7DofWt12ShOO1RdBDMlGuU6xfVcdLc_z_OVG1K0dbgNsIfqyLhJun2FsaDH3eFRKIJ4fiR4bJhRiZ6Z3JTB1J6hnfYA_r2mzTpH1TPSAgPuSZWqHxGHx7JKNwxUZDSXMnQ39niL8MSEq3IF3G_k1y8R_3omK7PLtYla-wk5zdXmwSzHYVdYQAHRIu46uQC3BQHOUq3UIOo-PRhZPOB6wWtW85vlC6P9aTyhhCGQxxFvrxXgntFnDuwnHr1IOn3flhO4sORZuX0zm5-oKsytTuXcNPKqhikX-hMn_l4oxiDIE_1p3mEYfqww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33aa06c32.mp4?token=F0zmX0MpjPKR73PenA4h2C-qmVrBBVS7DofWt12ShOO1RdBDMlGuU6xfVcdLc_z_OVG1K0dbgNsIfqyLhJun2FsaDH3eFRKIJ4fiR4bJhRiZ6Z3JTB1J6hnfYA_r2mzTpH1TPSAgPuSZWqHxGHx7JKNwxUZDSXMnQ39niL8MSEq3IF3G_k1y8R_3omK7PLtYla-wk5zdXmwSzHYVdYQAHRIu46uQC3BQHOUq3UIOo-PRhZPOB6wWtW85vlC6P9aTyhhCGQxxFvrxXgntFnDuwnHr1IOn3flhO4sORZuX0zm5-oKsytTuXcNPKqhikX-hMn_l4oxiDIE_1p3mEYfqww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اگر من در انتخابات میان دوره ای شکست بخوریم، استیضاح می شوم.
قرار است من را استیضاح کنند. آنها خودشان هم نمیدانند چرا.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/21319" target="_blank">📅 03:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21318">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5060626161.mp4?token=Wyp84fYC3DbJtbyYiKfL_ZUWQrPvy_KGuRq9FmQ4NU_38qQx-L0EDAm1RhIOIHbLjcsgrgD-63A7vn5H4OO51yBOF0Z6Yyp-sCMe1Sg1c3xeSNzNVjpOGS-oAdN-hds4hMIkMqhoHm8lEpHRT44MOVP9cmyW6FdizMS40TyQGO8LHMRw4rgLllV_nTpB2HtRputBlhYoMLFi9i2vJQAVpOZvk6Qx4iTRg8kPyu-C4oV4F0Yg8SxEU5-E4T4vo0RlvHZmQ-Mi-McUJAz9IgjFaE7K7ceQ8hMyy7D3lrZjH2jLkt8vp-TEB7TiQ910rLV1_BQ5qMtSq6SIpveKG7wHzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5060626161.mp4?token=Wyp84fYC3DbJtbyYiKfL_ZUWQrPvy_KGuRq9FmQ4NU_38qQx-L0EDAm1RhIOIHbLjcsgrgD-63A7vn5H4OO51yBOF0Z6Yyp-sCMe1Sg1c3xeSNzNVjpOGS-oAdN-hds4hMIkMqhoHm8lEpHRT44MOVP9cmyW6FdizMS40TyQGO8LHMRw4rgLllV_nTpB2HtRputBlhYoMLFi9i2vJQAVpOZvk6Qx4iTRg8kPyu-C4oV4F0Yg8SxEU5-E4T4vo0RlvHZmQ-Mi-McUJAz9IgjFaE7K7ceQ8hMyy7D3lrZjH2jLkt8vp-TEB7TiQ910rLV1_BQ5qMtSq6SIpveKG7wHzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
این در واقع یکی از بزرگترین مشکلات من است: نمی دانم با چه کسی در ایران برخورد کنم.
این تنها کشوری در جهان است که هیچ کس نمی خواهد رئیس جمهور شود.
آنها می گویند: "چه کسی می خواهد رئیس جمهور شود؟" نه، نه، من نمی خواهم رئیس جمهور شوم.»‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/21318" target="_blank">📅 03:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21317">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این خواهر پژی جمشیدی چه بی لولیه بی حیا دو زاری ، من ۹۹٪ فوتبالیستایی که دیدم دوزاری بودن ! این جماعت چرا اینجورین !</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/21317" target="_blank">📅 03:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21316">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سنت‌کام : نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را غیرفعال کرده‌اند و ۲ کشتی را برای اطمینان از رعایت مقررات به بازجویی و بازرسی برده‌اند. @WarRoom</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/21316" target="_blank">📅 02:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21315">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تکزاس زیر 1942 و Azul قبول نیستاااا</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/21315" target="_blank">📅 02:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21314">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJoshua Milani</strong></div>
<div class="tg-text">داش یاشار از کف تکزاس با تکیلااااا جات خالی</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/21314" target="_blank">📅 02:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21313">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtJXWs_2SZz7DCte3Z77UqFN7xG4ysfzvOzssSqEBveGcRUkPNs2JNeGgH6vHfmOpx-15dODJ7BM91nLLV_Q-F-wDBTTzV30UdovkJNt8XN6gPAuaAvCwLEfq2JrxtMUta1bLU5QvoUcp4pzUxasJKsJqZi3K_1uMF7gsAnhOiO6HLXQ0sjWPTFT88eGYqVnQMvtUcy3ZqWcQSVfL9m4zXi8folR-Ggk46hw574XrQse7F_KyUP27Z43gWy-9JHA3XZLufY-V2ApMK1l7bDHn-7gEvlMEqays1ZdM5ymxO8lHe43rBcMSHxMqS8CxSRDK6s4-FkhMUoJLlwLCzGaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگه شلوغ شد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/21313" target="_blank">📅 02:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21312">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جنگی
⚔️
⚔️
⚔️</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/21312" target="_blank">📅 02:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21311">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBaba barghi</strong></div>
<div class="tg-text">اقا یاشار گل مرد مردا
مارو از جنی واکرا بینصیب نکن مشتی
کاکو شیراز یه لشکری هوادارتن
🫡
🫡
🫡</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21311" target="_blank">📅 02:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from؛)</strong></div>
<div class="tg-text">یاشار ماهم داریم راکی میخوریم از غرب تهران مستیم مستت
🥃</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21310" target="_blank">📅 02:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق جنگ با یاشار : اول از همه باید به تغییر رژیم در افکار بوجود بیاد ، بعد اینام میرن ..</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/21309" target="_blank">📅 01:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/21308" target="_blank">📅 01:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۲ ساعت دیگه میرم بالای منبر اگه بیدارین
😎</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21307" target="_blank">📅 00:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nznd0hdd6-g76KFsXzxbHNvitOyDceLlm9PVm24YlIz1GCy25Wlfh__oW_FFqI--Jw1SSJzVgeVG-C1n0lvmFcVr-iJE_7AeQ5ns8ydHvHrpAscCOZ3USbDLyyr_XHh-fKkrbzSWvnBLwobZ3YXWlPk8au760Xjny1c2ADA6QIAah4_mgmajcnqGjAFYXooX8opusnQDqY4_2EXGj9feKkhptrye40lcmL5ZIgnmPZt2bPh_c3KSLcttjdQBx_ik8xp8U-DfFaBQaIPlR5GvLa05mewaMu0qHpJK7SLkT2mjD_C6h06JC6-Fma4FTXFB1Ia20oE456F4hV3NriH3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش، یک جت جنگنده F-35A Lightning II نیروی هوایی ایالات متحده هنگام فرود اضطراری کد اضطراری ۷۷۰۰  اعلام کرد…
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21306" target="_blank">📅 00:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b4cd2471.mp4?token=RhAGRWnSmY27oxSgoNrftPkFT5bCOSrrxjDt8m-nhltV62QWIjytd8cU9wKecVlWUoS_AbWWoSTztUiQCGR8tUY5FbZD5tGTIoWAsun1dASIaz3Md1qvjsIupHt2TX9SAI0rrUseesy0m0AD13ZvYFEARtzQVAHL3fr08qL_yUe14rqpuAyaNbN3i-sA5TZvjPkG9U-zU4_IeCmoPFAYF17M29JQ3vIFCyMOe6BCZVlgndSUw-U1h13I2XNBXfoOPjlL-oHF_IcS9zs6wGa4kiK7y26FX3GSWsOxEICl2zjUdxwypD6kX4-wbr63JmMfUqPuZZJla1BlMHHzy9R73g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b4cd2471.mp4?token=RhAGRWnSmY27oxSgoNrftPkFT5bCOSrrxjDt8m-nhltV62QWIjytd8cU9wKecVlWUoS_AbWWoSTztUiQCGR8tUY5FbZD5tGTIoWAsun1dASIaz3Md1qvjsIupHt2TX9SAI0rrUseesy0m0AD13ZvYFEARtzQVAHL3fr08qL_yUe14rqpuAyaNbN3i-sA5TZvjPkG9U-zU4_IeCmoPFAYF17M29JQ3vIFCyMOe6BCZVlgndSUw-U1h13I2XNBXfoOPjlL-oHF_IcS9zs6wGa4kiK7y26FX3GSWsOxEICl2zjUdxwypD6kX4-wbr63JmMfUqPuZZJla1BlMHHzy9R73g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: درباره حرکت ایران به سمت
جنگ اقتصادی
؛ آیا این به این معناست که گزینه‌های نظامی آمریکا محدود شده‌اند؟
ترامپ:
نه، به هیچ‌وجه.
ما
کنترل کامل بر تمام آن منطقه مرتبط با تنگه هرمز
داریم؛ و منظورم حتی مناطق خشکی در داخل آن محدوده هم هست.
آن‌ها بسیار مایل‌اند به توافق برسند، اما به نظر من هنوز آماده پذیرش
توافق درست
نیستند.
من فقط توافق‌های خوب (تسلیم کامل )انجام می‌دهم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21305" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">تنگه دعوا شده ، گزارش چند صدای انفجار / شلیک از غرب جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/21304" target="_blank">📅 00:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56ecd2c26.mp4?token=tHbTZTmQjeyDp3D1JuvA1UflLYNuxKxhN8HC9ugKmAQDZRXk_GK11vUgnBD5NZKqWLf-jalJx_V8V3UdLT79NICgNAofje4TsgOMAk6xBd0he3I_3YQwXRYj-ChDX9A61w7zk9rmFigFyNay0f5CmU64vnmGL38wUhjb6uUDvQJEWkc_-IXIj0jZD83cY3Q2ev6FkH0h6HTRZm_yRbf5xyGjNl3uBP3LdPPVyOL2I-cplmk3I3mxVAVksWF041EA8XiIgiqhrYhN7_urMX6q7erJqty9-Lp5OQkOfZPrQfmN4IQ9Ww-hXZpBf3pJ6z8WrTvYvZFSavmMcHTQOZ5_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56ecd2c26.mp4?token=tHbTZTmQjeyDp3D1JuvA1UflLYNuxKxhN8HC9ugKmAQDZRXk_GK11vUgnBD5NZKqWLf-jalJx_V8V3UdLT79NICgNAofje4TsgOMAk6xBd0he3I_3YQwXRYj-ChDX9A61w7zk9rmFigFyNay0f5CmU64vnmGL38wUhjb6uUDvQJEWkc_-IXIj0jZD83cY3Q2ev6FkH0h6HTRZm_yRbf5xyGjNl3uBP3LdPPVyOL2I-cplmk3I3mxVAVksWF041EA8XiIgiqhrYhN7_urMX6q7erJqty9-Lp5OQkOfZPrQfmN4IQ9Ww-hXZpBf3pJ6z8WrTvYvZFSavmMcHTQOZ5_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/21303" target="_blank">📅 00:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b84ef4f3f.mp4?token=WVVohmysqzcmJ3nshPyYE0V6ShQP0CQmX0l6EXcDNA1OmH0CDfi-QuiQW_MMIoy9bIMdBtLNCX0qClLqbCGqNGJo2PQ6sXWBsUBKRL_uW7uUNlw7QIthmAquRppBBEla6g-TUNFffdKdjRshHWBpm-UhLc4OTeEj7V25amGRCP6XXE2C1zbQw0amf24--_VgeMKkycPdgr3ceatqJBOo5st6Fus4Zesee_DZjPWTlwTATug-YE76EV-4OwAV4mJFFQbFPkuJyqmdyFRNCr_iQEJ8vEIgN8GFkWy-aYKUCvVRQYnZUTxx3kbrr61opMExYGng_Op4A5Su2VERjYrSsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b84ef4f3f.mp4?token=WVVohmysqzcmJ3nshPyYE0V6ShQP0CQmX0l6EXcDNA1OmH0CDfi-QuiQW_MMIoy9bIMdBtLNCX0qClLqbCGqNGJo2PQ6sXWBsUBKRL_uW7uUNlw7QIthmAquRppBBEla6g-TUNFffdKdjRshHWBpm-UhLc4OTeEj7V25amGRCP6XXE2C1zbQw0amf24--_VgeMKkycPdgr3ceatqJBOo5st6Fus4Zesee_DZjPWTlwTATug-YE76EV-4OwAV4mJFFQbFPkuJyqmdyFRNCr_iQEJ8vEIgN8GFkWy-aYKUCvVRQYnZUTxx3kbrr61opMExYGng_Op4A5Su2VERjYrSsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده، تصاویری را منتشر کرده است که نشان می‌دهد جنگنده‌های F/A-18E و F/A-18F Super Hornet همچنین E/A18 Growler نیروی دریایی ایالات متحده، که بر روی ناو هواپیمابر کلاس نیمیتز به نام USS George Washington در دریای مکران مستقر هستند، در حال آماده‌سازی برای انجام عملیات‌های شبانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21302" target="_blank">📅 00:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری فارس در یادداشتی با انتقاد از صحبت پزشکیان درمورد لزوم پایان جنگ نوشت: ایران جنگ را آغاز نکرده که پایان دادنش با ایران باشد!
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/21301" target="_blank">📅 00:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رویترز : فرسودگی پایانه‌های نفتی ونزوئلا نفتکش‌ها را تا یک ماه معطل می‌کند
پایانه‌های فرسوده بنادر نفتی ونزوئلا عملاً باعث محدودیت صادرات نفت خام این کشور شده‌اند و نفتکش‌ها به دلیل زیرساخت‌های فرسوده، قطعی برق و مشکلات کیفی، مجبورند تا ۳۰ روز برای بارگیری منتظر بمانند.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21300" target="_blank">📅 23:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21299">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">همکنون
موج شدیدحمله هوایی اسرائیل و بمباران در جنوب لبنان کوه علی الطاهر
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21299" target="_blank">📅 23:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21298">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شما هر صدای که بگی‌ در تهران داره گزارش میشه
🤠
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21298" target="_blank">📅 23:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21297">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به گزارش گاردین ترامپ برای هرگونه اقدام اقتصادی جدید علیه ایران، ناگزیر خواهد شد شرکای تجاری ایران، به‌ویژه چین، را هدف قرار دهد؛ همین مسئله رویکرد آمریکا را دشوار می‌کند
سفر رئیس‌جمهور چین به آمریکا در ماه آینده نیز ممکن است تلاش‌ها برای اعمال فشار بر پکن درباره واردات نفت ایران را پیچیده‌تر کند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21297" target="_blank">📅 23:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چند گزارش از صدای تیراندازی در غرب تهران
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21296" target="_blank">📅 22:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21295">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جی دی
ونس به اسکای نیوز : حضور ارتش آمریکا در خاورمیانه ادامه دارد!
واشنگتن ابزارهای فشار لازم برای مقابله با ایران را دارد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21295" target="_blank">📅 21:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbc6763df7.mp4?token=KoxOMHO2kK9CNYKH2bgrGABU2grl9VH_aNovY5cbZ2Om_FxUIQeAcCeA-l48HODUJZqYlloXamZvo0qSWWPCjGKCfLryWzG5CXKyrC3NNbMkTiZ7vtJyHKOgbZwuZ41A07seFGLdXTpusOnvNyKM-t0bipfzGXlYBb27TSvLJTq24Ky5uKnlamjSul8z2cKoJ8snwrH3PP__dhlhUeiskrP3Jhv0q3eBFIn4MKSVeDcR9CnV1mca0Wqq8cyl47laqzmn7b8mFJ3YhBXroSfcDSl_zAyncYfu0Ov5r8hlsv29MoKMzBkhqWsht9i22Pka7pJHJH9OVZiHUHb1Zci6vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbc6763df7.mp4?token=KoxOMHO2kK9CNYKH2bgrGABU2grl9VH_aNovY5cbZ2Om_FxUIQeAcCeA-l48HODUJZqYlloXamZvo0qSWWPCjGKCfLryWzG5CXKyrC3NNbMkTiZ7vtJyHKOgbZwuZ41A07seFGLdXTpusOnvNyKM-t0bipfzGXlYBb27TSvLJTq24Ky5uKnlamjSul8z2cKoJ8snwrH3PP__dhlhUeiskrP3Jhv0q3eBFIn4MKSVeDcR9CnV1mca0Wqq8cyl47laqzmn7b8mFJ3YhBXroSfcDSl_zAyncYfu0Ov5r8hlsv29MoKMzBkhqWsht9i22Pka7pJHJH9OVZiHUHb1Zci6vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت صحنه فوتوشوت از ترامپ
@WarRoom
😁</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21294" target="_blank">📅 21:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21293">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0YIDzqrexkdrTOWh7W90JvcUk4FNAJ30OVPk19ve8tZN1yQY9c0SGNqivTwUNzudwxD4O8MMiegQzPzW7IsaI9jbHWKyZcL9_o1bua3ZgHzds1MpAZ7XCaGrRxNEtMDPCtz9IgZv1dO3gDhJ1mNpDA7VVtXr16yJOlhRbcRNUI_HE0fHgZGI5iKvD4a5e7uqZKRlsRu8eypHUQUtMEhQ2IXGNZyIp7Lho1exKRLbUETy-d5JooEnXuCgaolBwVOP-E8Vea_5iLXKuoF9etAXYG43f3MxRwj9NzRWu2StNmiBKD7OMp-A8Emgat6Xq-XvbBNmpiqX5WRf7siQlSdKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث این مقاله را بازنشر کرد :
ترامپ از فشار همه‌جانبه بر ایران می‌گوید: «الحمدلله!»
دونالد ترامپ مدعی شد آمریکا
کنترل کامل تنگه هرمز
را در دست دارد و محاصره دریایی این کشور به یک «
دیوار فولادی
» تبدیل شده است. او گفت ایران دیگر
نیروی دریایی و نیروی هوایی مؤثری ندارد، بخشی از نیروهایش حقوق نمی‌گیرند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است
و رهبری جمهوری اسلامی نیز در وضعیت نامشخصی قرار دارد. ترامپ همچنین از
بی‌پولی و تورم ۳۰۰ درصدی
ایران گفت و مدعی شد جمهوری اسلامی دیگر «قلدر خاورمیانه» نیست و فقط حرف می‌زند. او تأکید کرد
آخرین کسی است که به ایران اعتماد می‌کند
و گفت اگر ایران اقدامی انجام دهد، با واکنش بسیار شدید آمریکا روبه‌رو خواهد شد. ترامپ در پایان گفت آمریکا اکنون در
«موقعیت بسیار خوبی»
قرار دارد و ایران پس از حدود ۵۰ سال دیگر «قلدر خاورمیانه» نیست و پیام خود را با عبارت
«الحمدلله!»
به پایان رساند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21293" target="_blank">📅 20:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس:
به زودی با قدرت به محاصره دریایی آمریکا علیه ایران پاسخ خواهیم داد و آمریکا منطقه را ترک خواهد کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21292" target="_blank">📅 19:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آکسیوس:
بازار نفت دیگر صرفاً با تهدید، وعده یا پست ترامپ معامله نمی‌کند؛
واقعیت میدانی تنگه هرمز، میزان واقعی اختلال در صادرات و عبور نفتکش‌ها اکنون تعیین‌کننده‌تر شده‌اند.
این موضوع همچنین برای ترامپ از نظر سیاسی اهمیت دارد، چون کاهش واکنش بازار به اظهاراتش می‌تواند توان او برای تأثیرگذاری فوری بر انتظارات انرژی را کاهش دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21291" target="_blank">📅 19:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07a22b837.mp4?token=F6m5ZiOcQU3oZsa2DpGQfqPGE2VxsKnpWBjS8t2__VlVFD0-pxBb-d_6FMDq4bKRpPxu-fMjsue2lDm0QSYoxFy1r9Tri_neb0dqZKuoIP5No8k2OSWm9zIQAq7f2KG5NvKqXKKs2VDGNDFMsDYqe5lNEdwt3dtncDySaJ4J8Huis9zfBG7iuX5CiZGfDyzI4Q-iSUeyqf144s6PNNO5gl_xGCkyb9h7pQ_WEoOOzGLhvEwWFgL124giR7a7lpndd8ObYp9owoXA-P1nbC9Rc0gPd73dpsDG1Q8okwrWOkIstv2c8cfTRqic7xdDiNK28kYEaCod78VhX6lGtqfMY3i5Er0xaCbUDbfAM_68tCPLsDd80Uomp4odysWnZ-xF4wjM0ubRiiQAX4dUh6q67dmo1XAuRiHc7C1UGCaRCOw-hAWBAf0kiEoTL7qOxRVV0HSl1ZVmPC3fRmsNeXOIddI_t4sYEcskP-PYrBLpjtLgDCzbFaxLhDRMjVV6WhTJbEwQJNGIaFJuvIeyrJGKGCb1NJsFVFyf2e4RZoL2TL8GvMs9bHmlpy_nl6jqhxke4SSX5cT6CoR1OO8Bb-gqTHDcE_pUuUioiV0SzX3amLYJsHsyeIL-MNwpp5yrXHHoUEh7WZcAMFkXIRSNQLm4xdK0usT6K1QA91gfv-PLECQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07a22b837.mp4?token=F6m5ZiOcQU3oZsa2DpGQfqPGE2VxsKnpWBjS8t2__VlVFD0-pxBb-d_6FMDq4bKRpPxu-fMjsue2lDm0QSYoxFy1r9Tri_neb0dqZKuoIP5No8k2OSWm9zIQAq7f2KG5NvKqXKKs2VDGNDFMsDYqe5lNEdwt3dtncDySaJ4J8Huis9zfBG7iuX5CiZGfDyzI4Q-iSUeyqf144s6PNNO5gl_xGCkyb9h7pQ_WEoOOzGLhvEwWFgL124giR7a7lpndd8ObYp9owoXA-P1nbC9Rc0gPd73dpsDG1Q8okwrWOkIstv2c8cfTRqic7xdDiNK28kYEaCod78VhX6lGtqfMY3i5Er0xaCbUDbfAM_68tCPLsDd80Uomp4odysWnZ-xF4wjM0ubRiiQAX4dUh6q67dmo1XAuRiHc7C1UGCaRCOw-hAWBAf0kiEoTL7qOxRVV0HSl1ZVmPC3fRmsNeXOIddI_t4sYEcskP-PYrBLpjtLgDCzbFaxLhDRMjVV6WhTJbEwQJNGIaFJuvIeyrJGKGCb1NJsFVFyf2e4RZoL2TL8GvMs9bHmlpy_nl6jqhxke4SSX5cT6CoR1OO8Bb-gqTHDcE_pUuUioiV0SzX3amLYJsHsyeIL-MNwpp5yrXHHoUEh7WZcAMFkXIRSNQLm4xdK0usT6K1QA91gfv-PLECQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخوندی در تجمعات شبانه: هنوز که از بغل بیت رهبری رد میشیم بوی گوشت سوخته آقا میاد!
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21290" target="_blank">📅 18:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل:
اردوغان یک دیکتاتور یهودی ستیز است که کردها را قتل عام کرده، تروریست های حماس را در خود جای داده است، نیمی از قبرس را اشغال کرده است، و تعداد روزنامه نگاران و سیاستمداران مخالف خود را به زندان انداخته است.
او اکنون به دنبال گسترش تجاوزات خود به اسرائیل به سوریه است. اسرائیل آن را تحمل نخواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21289" target="_blank">📅 18:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLau5sI7AUZOrknBw-K-PS9A-ncTT65XLr3yUUTSrlvmjAqeuzwU8gsfg_vhZylv82FsSLheV4djfc8UagnUzHU5MHpgAO1ievbGy1bIFJXl3Mm7KkaxNP0B-odNBuVGn8p79OoD15toIE2KJPJa-WqYVW5Ea2TBuj6CPGkARp-iC4PtJUvVpJtDhQMcVqZ2SEPu13FlFTp2alh_p_ZFcTHnYqm3ftVPtV3k0nb3W1LP6gW7Lem42jEgbYNFAOmly_zNI-CcNW_aUB4oecLdgBvJ3XA2OmAbRJhYqASrNcA_ywMFbvlgJaolDyEnR5ruuHaS8JKiQ5V-iMAM77UYUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحرکات جدید در العدید؛ ۴ سوخت‌رسان آمریکایی و ۵ فروند C-17 قطر در پایگاه
تصاویر ماهواره‌ای Sentinel-2 که امروز ثبت شده، حضور چهار هواپیمای سوخت‌رسان نیروی هوایی آمریکا در پایگاه هوایی العدید قطر را نشان می‌دهد.همچنین پنج فروند هواپیمای ترابری راهبردی C-17 گلوبمستر III نیروی هوایی قطر به العدید بازگشته‌اند؛
این نخستین بار از ۱۲ ژوئیه است که حضور این هواپیماها در پایگاه مشاهده می‌شود.
بازگشت همزمان هواپیماهای ترابری قطری و تداوم حضور سوخت‌رسان‌های آمریکایی، از ادامه فعالیت‌های هوایی در العدید حکایت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21288" target="_blank">📅 17:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امام جمعه رشت : برای افزایش جمعیت از مردم میخوام دست به دست هم بدن و به همدیگه کمک کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21287" target="_blank">📅 16:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=laY5b_ehKAg0qBRq1CI_ZUSkPXFpKE64DArJwgYXVOK6XvaDbXNqggxpt2zzF0_Aew7XgnINq5PlX_ON1xkTloeLDHWD7NWgxcjsOFPx_M0LrH9b3ezYR2YOSspYIc-xVQtnmr5d-MLRZgXHTVH9vwMt3yGsY3W0TfWETmiCCq0k--YKRyaVXb2Y_06jU_I-oPS2-GnyUBu5DacG5a72JowCwU1mc-0XHu0eSsTVftttlB2aCtCQTJs4zZf1fJzDbJUkiEW01o7_g5mspCVfbNFpkQfOMw9btcQ1N76zZD4BMxv40YL2Lt3YexPrAFAi47SB9NwpQbkD7Z0111IklEr31g43kgBV6nmjiadbeEIKNUfWVbwPsgjVmJ-Dm2XHqsqbwOXd56oi3t6JAS3VxM_OCvprtldVWS402HhKpHTxvQphHPeCU5JRWk-OWpucgsfMhWb6AFCZQtZ66hcin0NKKI1K6mGaNtGPFrDWrEumk0WRvhHduEFuKRfjx6Lax6XNtCYS1mXW4PtjbwowH3SHuPYuT9S71za0LuG8QR9oZ75yCdrb3Ipok6phF3rO5IcDwLWQ4UvQaYySdz0jjSnQPBng4gzsjQhiP_P7XsQQonA_odvL_LJK7vSxHMGLwlIZAyrC3n3CWLvqlzAFd1BJcHX_p9fYEW0hbwRZBSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e7e5ce77a.mp4?token=laY5b_ehKAg0qBRq1CI_ZUSkPXFpKE64DArJwgYXVOK6XvaDbXNqggxpt2zzF0_Aew7XgnINq5PlX_ON1xkTloeLDHWD7NWgxcjsOFPx_M0LrH9b3ezYR2YOSspYIc-xVQtnmr5d-MLRZgXHTVH9vwMt3yGsY3W0TfWETmiCCq0k--YKRyaVXb2Y_06jU_I-oPS2-GnyUBu5DacG5a72JowCwU1mc-0XHu0eSsTVftttlB2aCtCQTJs4zZf1fJzDbJUkiEW01o7_g5mspCVfbNFpkQfOMw9btcQ1N76zZD4BMxv40YL2Lt3YexPrAFAi47SB9NwpQbkD7Z0111IklEr31g43kgBV6nmjiadbeEIKNUfWVbwPsgjVmJ-Dm2XHqsqbwOXd56oi3t6JAS3VxM_OCvprtldVWS402HhKpHTxvQphHPeCU5JRWk-OWpucgsfMhWb6AFCZQtZ66hcin0NKKI1K6mGaNtGPFrDWrEumk0WRvhHduEFuKRfjx6Lax6XNtCYS1mXW4PtjbwowH3SHuPYuT9S71za0LuG8QR9oZ75yCdrb3Ipok6phF3rO5IcDwLWQ4UvQaYySdz0jjSnQPBng4gzsjQhiP_P7XsQQonA_odvL_LJK7vSxHMGLwlIZAyrC3n3CWLvqlzAFd1BJcHX_p9fYEW0hbwRZBSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما: نتانیاهو خیلی مرده؛ نه خسته شده از جنگ با ما، نه پشیمونه و هرآن ممکنه بهمون حمله کنه و بنظرم خیلی مرده.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21286" target="_blank">📅 15:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترکیه، حکم بازداشت اینترپل قرمز برای  نتانیاهو صادر کرد و او را به عنوان متهم در ارتباط با حادثه "ناوگان مقاومت" عنوان کرد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21285" target="_blank">📅 15:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21284">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=Kmhs4clyMbDnwYswN7DdE4993gH9wCzDHRljWHMVt6lFctJmL4idqBe6T4F1J1zSEtGb28p0_6ReAQX_wakO95U-sF1hoIM1rALPePlqLVbzT1UPvfGuoE4fKn-BCi6GAB27KmXZN1s7sDyX47k6IY2_gkSupLAfJcftHSdyoHgbFs8wDeAzR8tKxV2wkRwq2b-Sfzy52p2oVEntc7UJDAZBzxmmIIxb0iJcYENQzS390tYH24Rk8Gm-PS5MZSmQrp7OxDtNqTVcGVCFEBuF_-D82dC-2i4b-i_rkSgmXJxw5SKjy9Dhk2zmUZunKOsMx9Ty0NNjA0bTdhe1JfiwZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba907831b.mp4?token=Kmhs4clyMbDnwYswN7DdE4993gH9wCzDHRljWHMVt6lFctJmL4idqBe6T4F1J1zSEtGb28p0_6ReAQX_wakO95U-sF1hoIM1rALPePlqLVbzT1UPvfGuoE4fKn-BCi6GAB27KmXZN1s7sDyX47k6IY2_gkSupLAfJcftHSdyoHgbFs8wDeAzR8tKxV2wkRwq2b-Sfzy52p2oVEntc7UJDAZBzxmmIIxb0iJcYENQzS390tYH24Rk8Gm-PS5MZSmQrp7OxDtNqTVcGVCFEBuF_-D82dC-2i4b-i_rkSgmXJxw5SKjy9Dhk2zmUZunKOsMx9Ty0NNjA0bTdhe1JfiwZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس نیوز : ایران کم‌کم متوجه می‌شود که رئیس‌جمهور ترامپ و ارتش آمریکا در خارج کردن مخفیانه نفت از تنگه هرمز تا سقف ۱۰ میلیون بشکه موفق هستند.
بعضی شب‌ها به ۱۵ تا ۲۰ میلیون بشکه می‌رسد... این جریان قبل از جنگ است!
حتی سی‌ان‌ان هم مجبور شد اعتراف کند: ایران در حال از دست دادن کنترل خود است
همچنین رئیس‌جمهور ترامپ جبهه دیگری را باز می‌کند و کشورهایی را که به تهران کمک کردند تا سرپا بماند، تهدید می‌کند.
چیزی از ایران باقی نخواهد ماند.
ملاها این را خواستند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21284" target="_blank">📅 14:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21283">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21283" target="_blank">📅 13:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21282">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کارشناس صداوسیما:
علی خامنه‌ای یک پله از امام علی پایین‌تر بود و معجزه هم میکرد.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21282" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21281">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21281" target="_blank">📅 12:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwkYSRuo8wSRSiEVvUW2OTzwdOAh2tMY6nS1Ro3ZEPyG-uMkw0QZ3nfyaaIi2B9-s7wn0X4ZOewhhsaqMfkKkIUNaRQNREtLUTGzsDYN0CUiHbp9ueL1IEP_vyWq4nnbEu1z_foPvpk3fWtb7Pnl8pQsvNgmXyr-EmD53v4VsyiNn2El4-6bXWAJfri0Rw8znQsAHrJF9t-eMf3KvtoWtsJ9oZlOooft3ZU4WjUT_UysMnoC7FWz0dDPUoH6ifSEH8bfi_G_ZIVkiojv-4lWkweRNt3tOzQU9kQtR7C1kxmMLebeYMpkdCuHVkOYG1HkUg7m8qtuXRnbSyPSR_XPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRFQZHoLTYjUjkd5UNojliwgCr6QgGQILwRcrREqh0SuutlA6PNPLVzWth-0fa5Oa7uX8mdRcU5NkBiVCFWUJ38k88ffBB4jP_IZ3HJTDCcRod5idA60KhaBvkuOg3X7z3nt6tu4bizz4Sf3ztqeEV2BjWWsb23jlKqnD5h5Z9zWXDuNX-YlsgCOqq7qb_7MWbkkGbf1Efmpim93cNSVZaT0MUVgqtZY1GTzQzfEQAAeI-Y8MbM0UjyfdYirZb7GkHoVwfGGhtRCisx6FehkBPi2KcUilcngDq2WkMrdf419Q-gJlGgkSOejDPn74GCnL9Kg9bLizRGk6wHPd8DoJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیشب یک هواپیمای بویینگ E-3B سنتری  AWACS آلارم 7700 وضعیت اضطراری روشن کرد. ولی اکنون یک هواپیمای دیگر با همان مدل و مشخصات به پرواز در آمده که نشان می‌دهد که آمریکا تجهیزات کافی پشتیبانی در منطقه بسیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21279" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بیتکوین 77,000$ را شکست و در چند روز 15000$ گران شد
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21278" target="_blank">📅 11:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA0-6NdTgGaqO9jVb7Uuso0pTdLxMAQzAsbTIjfp0UsC4BGGsV9qKlaFLGsQFeYZdyx0NLBd-mGAPR61ykqC8dWa7oNmSdCMB3F7QmTTE9dRN6H-yn10AmC1T7YVT2Ilekw8fnBODPG7S6N5hbDd1kPozsLxu-fRZs6IpZruuqVFIgYmaI_9pLo_djIbK3s3w8jqyld0WZ2ptkKYzYMzr0uvJgrhCon2XaroMhjY2xdl4qdp026a8UAp0cIG8S1jlTGpOpiMiVzuc_uM6KNr0Vw_b80CnvFyuTbxLjY5Ci-GQbi0P3uF7TzHUH4oiIsqKIF2V_p4YcsIHbjxESqvgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده، دومین هواپیمای تانکر سوخت‌رسان را از مجموع شش فروند هواپیمای جدید، به نیروی هوایی اسرائیل تحویل داد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21277" target="_blank">📅 11:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش های بسیار از چندین صدای پرتاب از سیریک ، خونه ها لرزیدن و صدای انفجار از تنگه و صدای جنگنده ، همون فرمولی که گفتم جمهوری اسلامی میزنه نفت بره بالا  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/21276" target="_blank">📅 11:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏سقوط چشمگیر تردد در تنگه هرمز؛ تنها ۷ کشتی باری در روز پنجشنبه عبور کردند.
‏داده‌های شرکت ردیابی دریایی کپلر نشان می‌دهد تردد کشتی‌ها در تنگه هرمز روز پنجشنبه به نصف روز چهارشنبه کاهش یافت و تنها ۷ کشتی باری، شامل ۴ کشتی ورودی و ۳ کشتی خروجی، از این گذرگاه راهبردی عبور کردند. هیچ‌یک از این شناورها نفتکش یا حامل گاز طبیعی مایع نبودند، هرچند یک کشتی بسیار بزرگ حامل پروپان و بوتان از مسیر ایران از تنگه خارج شد. پرزیدنت ترامپ نیز طی روزهای اخیر بارها تأکید کرده است که ایالات متحده کنترل تنگه هرمز را در اختیار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21275" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏کانال ۱۴ اسرائیل: ترکیه با وجود هشدارهای نتانیاهو، محموله نظامی دیگری به سوریه فرستاد.
‏بر اساس این گزارش، ترکیه محموله تازه‌ای شامل حدود ۲۰۰ خودروی نظامی، از جمله ۲۰ تانک، به سوریه اعزام کرده است؛ اقدامی که با وجود هشدارهای نتانیاهو درباره تحرکات نظامی ترکیه در سوریه انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21274" target="_blank">📅 10:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز: در تهدید ترامپ علیه کسانی که به ایران کمک می‌کنند، حتی متحدان واشنگتن که در میانجیگری مذاکرات صلح نقش داشته‌اند هم ممکن است در این دایره قرار بگیرند و آن را شامل هر کشور یا نهادی کرده است که به تهران آنچه را او «شریان حیاتی» توصیف کرده، ارائه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/21273" target="_blank">📅 10:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21272" target="_blank">📅 09:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDr.t</strong></div>
<div class="tg-text">کجایی ؟ داشتم نگران میشدم</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21271" target="_blank">📅 09:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ : ما گزینه دیگه‌ای جز جنگ با جمهوری اسلامی نداشتیم و اگه لازم باشه ۱۰۰ بار دیگه‌ هم اینکارو تکرار میکنم چون آنها نباید به سلاح هسته‌ای برسند!
جمهوری اسلامی به کشورهای بی‌طرف مثل عربستان، قطر، امارات، کویت و بحرین حمله کرده!
اگه برجام رو پاره نمیکردم، الان سلاح هسته‌ای داشتند و ازش علیه همه کشورها استفاده میکرد!
رسیدن به توافق با آنها اصلا آسون نیست چون درحال حاضر هیچکس نمیدونه دقیقا چه کسی داره رهبری میکنه!
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21270" target="_blank">📅 09:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی پنتاگون به وال استریت ژورنال: ما تمام امکانات لازم را برای شروع حملات به ایران  را در زمان و مکانی که رئیس جمهور تعیین می‌کند، در اختیار داریم و هیچ کمبودی نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/21269" target="_blank">📅 09:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRdZJZ80HY_IMD7ePqga3-6jeWk5v1tQpk6XKstV9q0zEKKLWZVMheqacq7j_fx4Plo3gQ26Hv1hLj__cF1pQs8_IwMI4GfdNiwMMY_f5qy2zQxjKe5KI-K-xIUwH5ZEOIMHIYvH6BTp_JY9jXudvI_ZcFRKplZnTp1agh27yd6s7zJ93nJ22HcHMkRLCsRGwbtt4Z8HUSUfI-zqGdJTcsFf--I5jtr_c9gu7E6sP3skageVisfexr5WLfMwYXOZ5Qw496PamPkypHPTmwuRjxU4lLxeRZzVc4ybAiwOZrMsoYe7pZUsCxXvt_l_RO-MDQSzacKNEl4QWVpfnnIipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند مرفه رژیم جنایتکار ایران برای فرار از بازداشت ICE و بازگشت به زندگی لوکس در لس‌آنجلس پول جمع می‌کنند.
یک فعال ایرانی‌تبار که در جریان اعتراضات ایران بر اثر شلیک سپاه یک چشم خود را از دست داده، از
سید عیسی هاشمی، پسر معصومه ابتکار، معروف به «مریم جیغ‌زن»
، انتقاد کرده است. هاشمی ۴۳ ساله که از سال ۲۰۱۰ در آمریکا زندگی می‌کند، چند ماه پیش توسط
ICE
در کالیفرنیا بازداشت شده و روند لغو گرین‌کارت و اخراج او در جریان است؛ اقدامی که بنا بر گزارش با دستور
مارکو روبیو
انجام شده است. او اکنون با راه‌اندازی کمپین
GoFundMe
از مردم آمریکا کمک مالی می‌خواهد تا بتواند در این کشور بماند و به زندگی خود در لس‌آنجلس ادامه دهد
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21268" target="_blank">📅 09:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ در تروث بازنشر صحبتهای مقام ارشد کاخ سفید ، استفن میلر: او (ترامپ) ناامن‌ترین مرز تاریخ آمریکا را تحویل گرفت و ۱۵ ماه پیاپی، ورود غیرقانونی به کشور را به صفر رساند؛ برای انرژی و زنجیره‌های تأمین آمریکا دستاوردی تاریخی رقم زد، با کارتل‌های مواد مخدر مقابله کرد و آن‌ها را سازمان‌های تروریستی خارجی اعلام کرد؛ مانع دستیابی ایران به سلاح هسته‌ای شد؛ با ساخت خطوط لوله و افزایش تولید انرژی، قیمت بنزین را کاهش داد؛ تورم را به ۲ درصد رساند و با تصویب بزرگ‌ترین کاهش مالیاتی تاریخ آمریکا، مالیات بر انعام، تأمین اجتماعی و اضافه‌کاری را لغو کرد؛ یک پیروزی بزرگ و تمام‌عیار.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21267" target="_blank">📅 00:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یک مسئول دولت ترامپ به واشنگتن پست:
ایران "کاملاً ورشکسته" است و ترامپ ابزارهای متعددی در اختیار دارد که می‌تواند در هفته‌ها و ماه‌های آینده از آن‌ها به شکلی قوی‌تر استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21266" target="_blank">📅 00:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حملۀ هوایی اسرائیل به ارتفاعات علی‌الطاهر در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21265" target="_blank">📅 00:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کانال 14 اسرائیل: مجتبی خامنه‌ای «
ایزوله
» شده و سپاه کشور را اداره می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21264" target="_blank">📅 00:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارسالی تایید نشده : یاشار همین الان اهواز صدای شلیک موشک میومد قشنگ ی دودی توی هوا معلوم بود ولی دوربین گوشی اینقدر قوی نیست که بتونه دود رو بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21263" target="_blank">📅 23:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=rW5zPafrKOpCK-H1cpIFQxMXC4rMFDQxV5K5wtBVCycpa7Pg8lH6GsMWsPAdvzthCtm86pNxEd8HGIJNfm6ffbQTRXZrV4M6s1jB31YSf-VqsGclkdU887WPzYtuuKeEJAA6FqLc-q6xJH17FaPq5PRhx_N-TLxs-eysJnl7vpKKPSzBGXKvQsQbCkb21RQSgoVXohcLPqBdgTo76Rv9O7zKaigTbH5_BWQLvsxs9A1rglmWa6XhbEWDjXKWpneuplBaGZMDLKD5zZ2RRcIjzj432ekvwXVJv8VS8zJy2y9P_bAccOuZxpprzExdBtfZ5Qdxlgx7uVHrzBFDzAMRhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cf8ca15a.mp4?token=rW5zPafrKOpCK-H1cpIFQxMXC4rMFDQxV5K5wtBVCycpa7Pg8lH6GsMWsPAdvzthCtm86pNxEd8HGIJNfm6ffbQTRXZrV4M6s1jB31YSf-VqsGclkdU887WPzYtuuKeEJAA6FqLc-q6xJH17FaPq5PRhx_N-TLxs-eysJnl7vpKKPSzBGXKvQsQbCkb21RQSgoVXohcLPqBdgTo76Rv9O7zKaigTbH5_BWQLvsxs9A1rglmWa6XhbEWDjXKWpneuplBaGZMDLKD5zZ2RRcIjzj432ekvwXVJv8VS8zJy2y9P_bAccOuZxpprzExdBtfZ5Qdxlgx7uVHrzBFDzAMRhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملانیا ترامپ، بانوی اول: شنیدم دلتان برایم تنگ شده بود. من اینجا هستم.به کاخ سفید خوش آمدید
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21261" target="_blank">📅 23:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏تانکر ترکرز:‏ دلیل اینکه دیگر در خارک شاهد بارگیری‌های زیادی نیستیم، این است که تولید نفت خام ایران در ماه‌های اخیر به سطحی کاهش یافته که فقط اندکی بالاتر از میزان مصرف پالایش داخلی این کشور است. این یعنی ایران در حال حاضر فشار چندانی برای صادرات نفت ندارد.
‎
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21260" target="_blank">📅 23:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/471bef475d.mp4?token=uoMGAt73FOgbjG2bz-Fg8B2ps9Z9NUvKM02lOozh5babYOY3vdB5sFqhvKj3LzWBP2HtkMzMHkWtGRL9frtTQrbp5ct_KG3Dna8rstIR3yaoQNgz40ewFGT1_GgKBy8OMhTNbE9Ndytsjl_Fhl2fgWX2ynBlywzoQ7Yv4K3PnfV_gUcrG5VccTOJLmZvFql4WS5QUhyU1J_66T275TDeO2Mhe2W4c_nItFT4tVP65rdSPCP7iY9A0_aG72QiHtGfvmwsuVe4CXIqSY7B86TB4zItRJzxaRmgyy5AtymLoKQl1enUip4MMap2Mw8T4Yw2J7dth3T5Vww-VLQfYGG7cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/471bef475d.mp4?token=uoMGAt73FOgbjG2bz-Fg8B2ps9Z9NUvKM02lOozh5babYOY3vdB5sFqhvKj3LzWBP2HtkMzMHkWtGRL9frtTQrbp5ct_KG3Dna8rstIR3yaoQNgz40ewFGT1_GgKBy8OMhTNbE9Ndytsjl_Fhl2fgWX2ynBlywzoQ7Yv4K3PnfV_gUcrG5VccTOJLmZvFql4WS5QUhyU1J_66T275TDeO2Mhe2W4c_nItFT4tVP65rdSPCP7iY9A0_aG72QiHtGfvmwsuVe4CXIqSY7B86TB4zItRJzxaRmgyy5AtymLoKQl1enUip4MMap2Mw8T4Yw2J7dth3T5Vww-VLQfYGG7cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن وارد مرحله جدیدی در قبال ایران شده که در آن
فشار اقتصادی مؤثرترین ابزار آمریکا
است. ونس گفت ایران در دو هفته گذشته فشار اقتصادی بیشتری نسبت به آمریکا متحمل شده و واشینگتن قصد دارد این فشار را ادامه دهد. او تأکید کرد تأسیسات هسته‌ای ایران نابود شده‌اند، اما هدف آمریکا ایجاد
«واقعیتی جدید»
است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21259" target="_blank">📅 23:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c77add985.mp4?token=Zw9Xn0gn5eH-QZxJ2hMwKb4gbV72fH0_-HZgSC_BE1qxpr7srbi3zVNuq1F7FWEV4d5k8pbBC7uGHwPtwwjUbE3EG1lBoCeMnpHHc3HsPEsmjxDkgJzvCV_ipiOe7JPi4KLKBweJibSJocpQadtKAWQi4KoVvxbtsfpm4-KGquiWKK2NMqcIMzJPb7WVdGMBSyPeNKasmnGEOuodA-OYae7jckzg4sP8Gz9QbaHgjTqBQ0ZNrnMcPZ4OIlh4wkQvvyVPKb_VoEfavCRdbQDGbS4lRa3CNyPkraSfp-oMP0jAZty0h6alsql_Xu1lPozFXBKAvuVIy4fqjN-4ojlI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c77add985.mp4?token=Zw9Xn0gn5eH-QZxJ2hMwKb4gbV72fH0_-HZgSC_BE1qxpr7srbi3zVNuq1F7FWEV4d5k8pbBC7uGHwPtwwjUbE3EG1lBoCeMnpHHc3HsPEsmjxDkgJzvCV_ipiOe7JPi4KLKBweJibSJocpQadtKAWQi4KoVvxbtsfpm4-KGquiWKK2NMqcIMzJPb7WVdGMBSyPeNKasmnGEOuodA-OYae7jckzg4sP8Gz9QbaHgjTqBQ0ZNrnMcPZ4OIlh4wkQvvyVPKb_VoEfavCRdbQDGbS4lRa3CNyPkraSfp-oMP0jAZty0h6alsql_Xu1lPozFXBKAvuVIy4fqjN-4ojlI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل و شاباک فاش می کنند: سازمان تروریستی حماس در بیمارستان «ناصر» در خان‌یونس بازجویی‌های امنیتی و شکنجه انجام می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21258" target="_blank">📅 23:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ادعای نیویورک تایمز :
ناو هواپیمابر
آبراهام لینکلن
پس از حدود
۹ ماه استقرار و ۲۷۲ روز مأموریت
در خاورمیانه، که بخش قابل‌توجهی از آن در پشتیبانی از عملیات آمریکا علیه ایران گذشت،
منطقه را ترک کرده و در مسیر بازگشت به سن‌دیگو قرار دارد
. این ناو در
۲۱ نوامبر ۲۰۲۵
از سن‌دیگو حرکت کرده بود و هزاران ملوان آن تقریباً تمام این مدت را در دریا سپری کردند.
ناو هواپیمابر جورج واشینگتن
که از ژاپن به سمت غرب حرکت کرده بود، اکنون وارد منطقه سنتکام شده و قرار است جایگزین لینکلن شود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21257" target="_blank">📅 23:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش های بسیار از چندین صدای پرتاب از سیریک ، خونه ها لرزیدن و صدای انفجار از تنگه و صدای جنگنده ، همون فرمولی که گفتم جمهوری اسلامی میزنه نفت بره بالا
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21256" target="_blank">📅 22:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تنگه بدجور دعواشده
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21255" target="_blank">📅 22:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اد
میلیبند وزیر خارجه بریتانیا دیروز
از طرح اسرائیل برای ساخت‌وساز در منطقه
E1 در کرانه باختری
انتقاد کرد و آن را اقدامی «غیرقابل‌قبول و مخرب» خواند. او از اسرائیل خواست طرح را پس بگیرد و گفت بریتانیا در واکنش به گسترش شهرک‌سازی، اقدامات و تحریم‌های هدفمند بیشتری را بررسی می‌کند.
در پاسخ،
ایتامار بن‌گویر امروز،
در شبکه اجتماعی ایکس خطاب به او نوشت: «کسی باید اد را به‌روز کند که قیمومیت بریتانیا بر سرزمین اسرائیل در سال ۱۹۴۸ پایان یافت و اسرائیل کشوری مستقل است» و سپس با کنایه به میلیبند گفت به جای «بازی با دوران قیمومیت»، به لندن نگاه کند که به گفته او «به‌سرعت در حال تبدیل شدن به یک خلافت اسلامی است».
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21254" target="_blank">📅 22:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncNN9Tkh24BA2PLslH6JcvQepiFNNcgaD8KAa_-8ZVi34pHRhYwIBxzMoJSYi8aVSGpKMGtXNY4mKtzw6wl8cvAb3ViI7QUHOtArbLanbImff126L8cUYrAdCioAh-6IBqWlHzAh6JVXTF1rfR-AWYYWn9hs2-Up5IM9GZdAV5xXKGRZmdUjIL6QKj9GkpJyJwHlHJ1YpadVE2CDk3uqBw2fQLYmTD1kB0oyr-DuwQnspeYkVarXNY7zve0-7NyAmjZ_9eIYOKXAP-O4oz5bJI-oVQLwdmXRkx-lwNPl3n5w_iWb9iGUaU9E-ylJGskcX3T-nIXsr1tVZxzCOGWyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نظر یک کاربر اتاق جنگ
🫱🏼‍🫲🏽
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21253" target="_blank">📅 21:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بر اساس بیانیه‌ای که دقایقی پیش در وبسایت وزارت خزانه‌داری ایالات متحده منتشر شد، ۹ شهروند با پاسپرت ترکیه و یک شهروند ایرانی با نام مسعود مسافر به‌ظن ارتباط با حزب‌الله لبنان یا نیروی قدس سپاه به فهرست تحریم‌های ایالات متحده افزوده شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21252" target="_blank">📅 21:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کانال 15 عبری : نتانیاهو در حال حاضر جلسه‌ای خصوصی با حضور روسای سازمان‌های امنیتی، از جمله سازمان‌های اطلاعاتی، برگزار می‌کند تا در مورد تمام تحولات آتی، به ویژه در سوریه و در روابط با ترکیه، بحث و تبادل نظر کنند. این اقدام در پی اعلام ترک‌ها مبنی بر ادامه فعالیت‌هایشان در سوریه صورت می‌گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21251" target="_blank">📅 20:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
دوشنبه جزئیات اقدامات جدید را اعلام می‌کنم. اگر سیاست
حداکثر فشار اقتصادی
ادامه یابد، فعلاً احتمال آغاز دوباره عملیات نظامی گسترده کم است. آمریکا در عین حال کنترل تنگه را در اختیار دارد و می‌تواند جریان انرژی را مدیریت کند. ما در حال اجرای
بزرگ‌ترین عملیات هماهنگ انزوای اقتصادی در تاریخ جهان
هستیم و به کشورها هشدار می‌دهیم که اگر به تجارت، انتقال پول، خرید نفت یا انتقال کشتی‌به‌کشتی با ایران ادامه دهند، با تمام توان تحریمی آمریکا مواجه خواهند شد. هدف،
درهم‌کوبیدن اقتصاد این رژیم جنایتکار، قطع توان مالی آن برای حمایت از نیروهای نیابتی و تأمین هزینه‌های نظامی
است. بسنت تأکید کرد: «این روش در همه جا جواب داده؛ ما یک ضربه دوگانه شامل
محاصره و سخت‌ترین تحریم‌های تاریخ
وارد می‌کنیم و
در ایران نیز موفق خواهد شد. ما این رژیم را فرو خواهیم ریخت.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21250" target="_blank">📅 20:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بسنت ، وزیر خزانه‌داری آمریکا:  ما نظام ایران را سرنگون خواهیم کرد @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/21249" target="_blank">📅 20:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏وزارت جنگ ایالات متحده در حال بررسی برکناری مکس لدرر، ناشر باسابقه روزنامه نظامی «استارز اند استرایپس»، پیش از موعد بازنشستگی اوست. این اقدام پس از انتشار گزارش‌های انتقادی فیک این روزنامه درباره وضعیت خدمه ناو هواپیمابر «آبراهام لینکلن» در جریان جنگ علیه جمهوری اسلامی و همزمان با تشدید اختلاف میان این رسانه و مقام‌های نظامی آمریکا مطرح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/21248" target="_blank">📅 20:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_bm4ZG9_aLqbcOspG7oEpurX18X7rvP3ife6xx-8dAAMval1sQz81vqx1SBl70iWE9r9L3syhKS8ebAlnrYPq_EcNwF8UKOMQtuG6FU30R0Pa_fJTpCUDInmD6Rq5jsNDDOFbJMYv91-Rg51QBnMcw5QYv6jVYIBsLmhKC3J7LbP2QVDHh-lpG8Q4WCWrA8wnvySCIswzlelw65QTqPdoDIWgbb8SuPOqglbp_SXmjZKSF1ADalGQnVD5U9dXIJaHiRh2tMjgG3guIr-WsuaNc-NuPqBpcE4ndSMAGzoux4i2f0k9dcae89pRRLxMrGmHFC58ExdPGmQXWrcj29LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنت‌کام : نیروهای ایالات متحده از زمان تقویت محاصره بنادر ایران، ۶۷ کشتی تجاری را تغییر مسیر داده‌اند، ۳ کشتی را غیرفعال کرده‌اند و ۲ کشتی را برای اطمینان از رعایت مقررات به بازجویی و بازرسی برده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21247" target="_blank">📅 19:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کانادین پرس :
پیر پویلیور،
رهبر حزب محافظه‌کار کانادا و رهبر اپوزیسیون رسمی این کشور
، از رضا پهلوی، ولیعهد ایران، دعوت کرده است به کانادا سفر کند. پویلیور روز شنبه در مراسمی در بریتیش کلمبیا اعلام کرد که علاوه بر این دعوت، قرار است به‌صورت مجازی با رضا پهلوی دیدار کند. او در این مراسم گفت این دیدار فرصتی برای گفت‌وگو درباره
دموکراسی و امنیت ایرانیان خارج از کشور
است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/21246" target="_blank">📅 19:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی. @WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21245" target="_blank">📅 18:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=AcY5MJuFVwK0wXtQYGhGCiBosCHyIho7MHdqJJCC-HPVbzR6SmbI5ZY8G0PgR_A736npFsaDQBQYKoiajmHpIxbePmlyi6UTS0CfDf8Pby7EaFQ4VKa9EjmtgJFNCqii3KRGVcdP2hoTpAVdrTBNQzHE1Ru2A4ViSC-Rp9CVHzxxIweIMO_RxeJIDQ5uilU-5HrbzWCZplMYuYcsDGpz-t5YGy64bB7tfdaTKM4N3RRtPOn0UAR40IoLB4hlBX2c6Sp9oUU1moi9jAn5NNFPJEr29HyrC4-l7jAESVNZh9NXLj_It-ox0tLTnDugEr4xssrpiGw7xGU0UV6BcqK-FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3286979e.mp4?token=AcY5MJuFVwK0wXtQYGhGCiBosCHyIho7MHdqJJCC-HPVbzR6SmbI5ZY8G0PgR_A736npFsaDQBQYKoiajmHpIxbePmlyi6UTS0CfDf8Pby7EaFQ4VKa9EjmtgJFNCqii3KRGVcdP2hoTpAVdrTBNQzHE1Ru2A4ViSC-Rp9CVHzxxIweIMO_RxeJIDQ5uilU-5HrbzWCZplMYuYcsDGpz-t5YGy64bB7tfdaTKM4N3RRtPOn0UAR40IoLB4hlBX2c6Sp9oUU1moi9jAn5NNFPJEr29HyrC4-l7jAESVNZh9NXLj_It-ox0tLTnDugEr4xssrpiGw7xGU0UV6BcqK-FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسنت درباره ایران: ما از این وضعیت مناقشه با ایران عبور خواهیم کرد. نمی‌دانیم چه زمانی.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21244" target="_blank">📅 18:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مسرور بارزانی، نخست‌وزیر اقلیم کردستان عراق به المانیتور با اشاره به بیش از
۱۰۰۰ حمله موشکی و پهپادی
علیه اقلیم از زمان آغاز جنگ آمریکا و اسرائیل با ایران در ۲۸ فوریه، خواستار تقویت پدافند هوایی شد. او هشدار داد خروج سامانه‌های
پاتریوت و نیروهای آمریکایی
، اقلیم را آسیب‌پذیرتر می‌کند و از آمریکا و متحدانش خواست برای تأمین پدافند هوایی، سامانه‌های هشدار زودهنگام و تجهیزات مقابله با پهپاد کمک کنند. بارزانی همچنین گفت حملات اخیر به دفتر شخصی او و خانه رئیس شورای امنیت اقلیم با هدف
ارعاب و کشاندن اقلیم به درگیری
انجام شده است. او مدعی شد پهپادهای استفاده‌شده در این حملات
ایرانی و از نوع حدید-۱۱۰
بوده‌اند و هیچ کس دیگری ندارد؛ ادعایی که ایران آن را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21243" target="_blank">📅 17:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲ @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21242" target="_blank">📅 15:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">العربیه : ۳ نفر از نیروهای سپاه در حملات به مواضع حوثی های یمن کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21241" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">یک مقام آمریکایی و یک مقام کاخ سفید به خبررگزاری سمافور گفته‌اند که دولت آمریکا معتقد است
مذاکرات ایران و عمان از چند هفته قبل عملاً شکست خورده است
. احتمال دریافت عوارض از کشتی‌ها برای عبور از تنگه هرمز و پیشبرد سازوکاری جدا از مذاکرات مستقیم تهران و واشنگتن از دلایل اصلی نارضایتی دولت ترامپ عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21240" target="_blank">📅 14:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو: بازسازی نوار غزه تنها در صورتی امکان‌پذیر خواهد بود که حماس به طور کامل از سلاح‌های خود محروم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21239" target="_blank">📅 13:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو : شما سورپرایز خواهید شد
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21238" target="_blank">📅 12:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=fhal0ThTcsSJR2ylIVbPqWVbKVyRaMUEUsLadKyiwwvUBIFmjm33yiMvEnVyaqMTodqn56dwBl_3HieakhEysXfuquqXYRqLR5STceZqvuddco-XmtFxMPqv_zpNRqlVoE-5xVloZEb_qX8QP1p2m0M-1WEyl7wBabzyTlb7G4yd_Pd1Kn9_tsYA2L9SP3nz4flm8j82CKfydxRzlAJUsNROp-vs-JASjYgeQHdskvKZt3SgAaTVPH9FbO8NCviE-pzmtQfTUeExPEZhF_-f4PUx091Sabsccq_mKLFYBSpeZcNALdaNrKuxAG7mZJ3kxiZR3_UJx0Iw8UZRM0sLNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cd8ea5eb.mp4?token=fhal0ThTcsSJR2ylIVbPqWVbKVyRaMUEUsLadKyiwwvUBIFmjm33yiMvEnVyaqMTodqn56dwBl_3HieakhEysXfuquqXYRqLR5STceZqvuddco-XmtFxMPqv_zpNRqlVoE-5xVloZEb_qX8QP1p2m0M-1WEyl7wBabzyTlb7G4yd_Pd1Kn9_tsYA2L9SP3nz4flm8j82CKfydxRzlAJUsNROp-vs-JASjYgeQHdskvKZt3SgAaTVPH9FbO8NCviE-pzmtQfTUeExPEZhF_-f4PUx091Sabsccq_mKLFYBSpeZcNALdaNrKuxAG7mZJ3kxiZR3_UJx0Iw8UZRM0sLNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی پالایشگاه نفت تهران:
ستون‌های دود در آسمان تهران، ناشی از آتش‌سوزی در دو مخزن مربوط به بسته‌بندی و انتقال محصولات نفتی، در محوطه پالایشگاه نفت در پایتخت تهران است. هیچ آتش‌سوزی در داخل خود پالایشگاه رخ نداده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21237" target="_blank">📅 12:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رسانه‌های سعودی به نقل از منابع گزارش دادند:
دولت ترامپ از اطلاعاتی درباره یک طرح ایرانی برای عملیات‌هایی که فراتر از هدف قرار دادن کشتی‌ها است، و همچنین طرح نیروهای یمنی برای افزایش هدف قرار دادن کشتی‌ها در تنگه باب‌المندب، مطلع شده است.
ترامپ به تیم خود اطلاع داده است که در صورت ناکارآمدی تحریم‌های اقتصادی، احتمال انجام حملات گسترده علیه ایران وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21236" target="_blank">📅 12:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بیتکوین در حال پرواز است و با قدرت از مرز ۷۱،۰۰۰ دلار هم عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21235" target="_blank">📅 11:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRb_5mnr25GEO6cmgF6y6bCzP1SYL7nEMlzYTVFwhqxCBTwasyUBKhGfRe4lYDrMs9fy9DHceK3iXQzZyoEowTGGBqpLkAvij2ZdShG9GqJjWfaCyF38YZ5t2RyY_PM-KEZ5tVU9WEC2_hBKjYk9N8pa1NNw8WZOZW7m2wStdegjKQXknfTdq1x2xh5mTnE-gNVvqCdvEuVX1YFoPKg21C_OaXNDGpERRN7fDBz_p3Sg4lEKT4OR5sQ_WQXyZuNLYEdkNIzeZCPA8iTyZjJFfHOxFa4A7riPq--uuMTxhsjyrw60DbKEESk-NMNyDEa5ve3RWlO9LH6ii6ByL9AUt18w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e050dd4cf1.mp4?token=CfXFokdN_zRmiSS74QsKxJISX9G71-nPLImkYx4oUQExHo2PtNLLmZRbqlKDywGKvD_tWNFH3xcOd5BTcQN6KD4SciNyY8Zi9MLuhq82Sl4XVi0oABtyClMLLLgJL9VB_MHvcP3SCWqdQmtWzR8Kh7IQTZgr1_0-TTn2RD4yDtEr5Kag-ap7wnxwS-aJ7zn3hexO-3P1l8zZeN_lEJVO8xv-rhDAevtpW-bbV4BOBaSap21ptJemGvPFHvxq9t4gOgzyZIIRyeJQbHM9la56G1p-R9OB9t6BhHMcB4DRq7MA8dlr1TZ2BEDw8Y72VVwNOB69JmHByXBJDvhc-8AWRb_5mnr25GEO6cmgF6y6bCzP1SYL7nEMlzYTVFwhqxCBTwasyUBKhGfRe4lYDrMs9fy9DHceK3iXQzZyoEowTGGBqpLkAvij2ZdShG9GqJjWfaCyF38YZ5t2RyY_PM-KEZ5tVU9WEC2_hBKjYk9N8pa1NNw8WZOZW7m2wStdegjKQXknfTdq1x2xh5mTnE-gNVvqCdvEuVX1YFoPKg21C_OaXNDGpERRN7fDBz_p3Sg4lEKT4OR5sQ_WQXyZuNLYEdkNIzeZCPA8iTyZjJFfHOxFa4A7riPq--uuMTxhsjyrw60DbKEESk-NMNyDEa5ve3RWlO9LH6ii6ByL9AUt18w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : فلورا جون ۲
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21234" target="_blank">📅 10:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB1QAieVbQTs4xwAAB0KJcRebJt8YPiFjPBKJ5eUq2oqcq-tr9qrij2UFI_N3L9v1n_kMaHi2nRnHtJkLkUx0eJSRDIt5M2G1AAVzoy1VjcDMj-aRs5unNVyji3sdYBaryvkHbPNHxXeIeOz5YeqgfXEl1W5HfcgwduUyX2ewOTdiM4hlN2N7C-faL16bgwJQbk4r7_uf1vs3UrKkSr4_OV2lg7RQwO1lcaXMfpicrDbp2Z9gk3j4AGqdTTGSzXDmcxi3CmqP1z0r0NinN6t3KOva9E04IOUAgkO0sDusgleueWPg-hURRaVfeZKZmVIwhlm-ZnJJKieVQpPHGXRUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه اعلام کرد: حکم قائم حسینی معروف به آرین ، تبعه خارجی و از متهمان پرونده موسوم به «میدان علیخانی» اصفهان، اجرا شد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/21233" target="_blank">📅 10:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اکسیوس گزارش داد که ارتش آمریکا در اقدامی محرمانه، یک کریدور دریایی در مسیر ورود و خروج کشتی‌ها از تنگه هرمز ایجاد کرده است
تا روزانه میلیون‌ها بشکه نفت از این مسیر عبور کند؛ اقدامی که به گفته دو مقام آمریکایی، با وجود بن‌بست در جنگ، موفقیتی قابل توجه برای واشنگتن محسوب می‌شود.
بر اساس این گزارش، این عملیات طی چند هفته گذشته در جریان بوده و هر شب حدود ۱۵ تا ۲۰ نفتکش از طریق یک مسیر جنوبی در امتداد سواحل عمان وارد تنگه هرمز شده یا از آن خارج می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21232" target="_blank">📅 08:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTD4x88NLXjKt2GFSXkwdlz2MdZXxick1FsMSkVxarvWG2roGQQaHMuTJ-ahVtekU1EgGU_95E5hCqJHH5nk3exyR7SLDkq22vaugfleAW4VgcH3b5rDJrTnRw_Wr7dpz-vtcDGGn59ZPDMxrDbFI8F7YvRPig1BqncbwXZ9a56f7aWqgtEg00wOJJZN0Ta_K7G4zPTX80BYxbNyTOVKqPMxZriiciH31B436o5e9rJvFV4KvnLxA1ZLSoUFzvyG5LmW1efU9YIZoGAEf2wxG9Dup4RVURD2jw-W9-qabnqFwIUUVMr3L-l4eAyZfoG5-3J7ERf9eW07yIyLeKrQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : هیچ‌کس به‌اندازه من به جمهوری اسلامی ایران فرصت نداده است تا به یک توافق برسد. متأسفانه، آنها از این فرصت استفاده نکردند. بنابراین، امروز اعلام می‌کنم که
کمرشکن‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است
را آغاز خواهیم کرد! این عملیات، جنگ اقتصادی و انزوایی در مقیاسی بی‌سابقه خواهد بود. نیروی دریایی آنها از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان به ویرانه تبدیل شده و ارزش پولشان از بین رفته است؛ کشورشان نیز به تار مویی بند است. امروز همچنین اعلام می‌کنم که
هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هرگونه کمک حیاتی به ایران برسانند، خودش با پیامدهای اقتصادی بسیار سنگینی روبه‌رو خواهد شد.
قاچاق نفت، خطوط مبادله ارزی، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی —
همه اینها باید همین حالا متوقف شوند.
خودتان می‌دانید چه کسانی هستید. این یک
«روز دی اقتصادی»
خواهد بود و ما نیاز داریم همه متحدانمان در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند. این دیوانگان در آخرین نفس‌های خود هستند و این اقدامات تاریخی، آنها و توانایی‌شان برای گسترش تروریسم در سراسر جهان را فلج خواهد کرد.
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21231" target="_blank">📅 07:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بامداد نیک و خجسته ، پیج اینستاگرام رو برگرگردوندم ، خواب بودم
instagram.com/yashar
پیج دوم پشتیبان :
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21230" target="_blank">📅 07:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=sSj9_FHcs0iWi8mi4ZrVhfTcDHN415qBZxoAeUY9ISZid5XWbx66Xj_wPby537nOSoCelxz2XB2Xll9V16u6zNnIsaEHxxLQaBVB4yLFi9l7NOVkBfAWPiJLF0K2EWh2TDwfHNG-P428kpmg2y65RlEPMLeLlU4vFTDkXVG5LBCkizBFOnc8WLNIOpbbLFy9M74MlRt9fQGOAN8t94Npf5F8VCi6gODD4Omh9RVWYh82U3vXwMMZoHWdDIOXTsj6Ypb_flMJGrl2gEtwKEbXQ1dOxybyPla1L-s4wD5hIBD4T5pU7PIEDvRo2kzC979-sPcpD2ujPPyVGmzw_bfrGrjOTZR8kaDlGJ5tBBqBZm0adrMZF0IgJxbgyjhkYjzgoonVxfkCI1nMmBy6mWXGFM-u96YAQmQaA9m1g96nUE9C-3kJ34oT9himgmVmFviVr3dewhZtlYFP7AF9J_bZgMXifgt-RCBCmn18JDyF0qw2QgPRkc0uWUE7qbAKh32YKoj5rchxjOqwmMrNV6Cnprjvl-ELs8VuZ4DT6KW6y7Sq5OYYfD3eiCIq0HCKJ-Z8LGxlairKr0M2mn5Xh6qNiDDh63XPvAkYTy_g-zUmi2N8s3_Yrb28TcqDGrQ3a6MMdEe0Vz7-sSxnMgAR-KYBsrSZFXSRtNzKCCwpIyFy-4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b17a03cc01.mp4?token=sSj9_FHcs0iWi8mi4ZrVhfTcDHN415qBZxoAeUY9ISZid5XWbx66Xj_wPby537nOSoCelxz2XB2Xll9V16u6zNnIsaEHxxLQaBVB4yLFi9l7NOVkBfAWPiJLF0K2EWh2TDwfHNG-P428kpmg2y65RlEPMLeLlU4vFTDkXVG5LBCkizBFOnc8WLNIOpbbLFy9M74MlRt9fQGOAN8t94Npf5F8VCi6gODD4Omh9RVWYh82U3vXwMMZoHWdDIOXTsj6Ypb_flMJGrl2gEtwKEbXQ1dOxybyPla1L-s4wD5hIBD4T5pU7PIEDvRo2kzC979-sPcpD2ujPPyVGmzw_bfrGrjOTZR8kaDlGJ5tBBqBZm0adrMZF0IgJxbgyjhkYjzgoonVxfkCI1nMmBy6mWXGFM-u96YAQmQaA9m1g96nUE9C-3kJ34oT9himgmVmFviVr3dewhZtlYFP7AF9J_bZgMXifgt-RCBCmn18JDyF0qw2QgPRkc0uWUE7qbAKh32YKoj5rchxjOqwmMrNV6Cnprjvl-ELs8VuZ4DT6KW6y7Sq5OYYfD3eiCIq0HCKJ-Z8LGxlairKr0M2mn5Xh6qNiDDh63XPvAkYTy_g-zUmi2N8s3_Yrb28TcqDGrQ3a6MMdEe0Vz7-sSxnMgAR-KYBsrSZFXSRtNzKCCwpIyFy-4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خونثانیاهو
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21229" target="_blank">📅 00:15 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
