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
<img src="https://cdn1.telesco.pe/file/vGOjZDBTM-ZEQuZNRZapY6b6FT2mVSHjot6BbFKg6qI_vgRCWbwuzQp5CWrHWdHPt0e5UPk3seHa0cjEC1VjQDqDZOs_jdyF18Z0gh5n5xd6dHKU84XtO0NTIs1qLKnWXYNxgRSQH1d813oZGLv7P_jEG2S1JAStF5-Pc08h2smqdlY0LcaCj2cqvpCZKBl_JXL7KPX48Ud6vCKzr56qEAaSOCX293YsQSYABV44fiKVmeAhoE0mANKQbKkbbIAMt1JoE4WgF9qRYNMgrukdBcTexNlnwjoYaiNB2vfoSO8kjLIo3P29xwnizXNZCSeRkveCz_H7wxqMI2HaRCyWQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.43M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 05:16:35</div>
<hr>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=neSBoKz8h1M_Ky_8uTuw_08RZxS5sDRLjoO5hoOFS6tZzvOILAHe5PCtPES3A9LxIN2X-ZL6Q2nrrSQAdQNrDYQar3VcNg2M6s7Mcv5sfrw8RvNNfcwY2ke4YPHdLpkHuuNEUmRw_bL7g3b40SgZiQSJIr-J8wmxyW4sWFUF-iQIA40akNJTs0EcZ49qclP0PBj0TchRpek0EPH2yNvslxBIUm_dB0QsxSxr73sbK5Amz2NtnuVPJJwoyjCRIwvxDicqk_uKvhh_luyFEIkQzLW-c-reMYgdsRp7Yl3-ddgkAfnu5vSSRmvH_gIlgPxL7ZtaMxAVznXIdrGkoebz6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a0c029ac9.mp4?token=neSBoKz8h1M_Ky_8uTuw_08RZxS5sDRLjoO5hoOFS6tZzvOILAHe5PCtPES3A9LxIN2X-ZL6Q2nrrSQAdQNrDYQar3VcNg2M6s7Mcv5sfrw8RvNNfcwY2ke4YPHdLpkHuuNEUmRw_bL7g3b40SgZiQSJIr-J8wmxyW4sWFUF-iQIA40akNJTs0EcZ49qclP0PBj0TchRpek0EPH2yNvslxBIUm_dB0QsxSxr73sbK5Amz2NtnuVPJJwoyjCRIwvxDicqk_uKvhh_luyFEIkQzLW-c-reMYgdsRp7Yl3-ddgkAfnu5vSSRmvH_gIlgPxL7ZtaMxAVznXIdrGkoebz6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنرانی ترامپ، بخش مربوط به ایران،
تشخیص و ترجمه ماشین:
در ونزوئلا خیلی خوب پیش می‌رویم.
نفت زیادی از ونزوئلا می‌گیریم و رابطه‌مان با آن‌ها هم بسیار خوب است.
میلیاردها و میلیاردها بشکه نفت از ونزوئلا خارج می‌شود. ونزوئلا یکی از غنی‌ترین نقاط جهان از نظر نفت است.
و همان‌طور که می‌دانید، آن یک جنگ ۴۸ دقیقه‌ای بود؛ ۴۸ دقیقه طول کشید.
و هزینه جنگ را با آنچه از آنجا بیرون آورده‌ایم، چندین و چند و چند برابر جبران کرده‌ایم.
قبلاً کجا چنین چیزی شنیده‌اید؟ هیچ‌جا نشنیده‌اید.
همان روش قدیمی است، درست است؟ همان روش قدیمی.
غنائم از آنِ فاتح است، درست است؟
و ضمناً همین کار را در جمهوری اسلامی «دوست‌داشتنی» ایران هم انجام می‌دهیم.
داریم حسابی می‌کوبیم‌شان.
ترجیح می‌دهم توافقی انجام شود، چون نمی‌خواهم مردم را بکشم. نمی‌خواهم مردم را بکشم.
اما بالاخره در مقطعی قرار است... ما... ما برای بزرگ‌ترین حمله در میان همه حملات آماده شده بودیم و طی چند ماه گذشته ضربات بسیار سختی به آن‌ها زده‌ایم.
اما کاملاً آماده بزرگ‌ترین حمله از زمان جنگ جهانی دوم بودیم.
آن‌ها با من تماس گرفتند و گفتند: «لطفاً این کار را نکنید. بیایید گفت‌وگو کنیم.»
بعد می‌گویند: «ما هرگز چنین چیزی نگفتیم.»
می‌دانید چیست؟ رسانه‌های جعلی می‌دانند که آن‌ها چنین چیزی گفتند.
اما در حال گفت‌وگو هستیم. ببینیم چه اتفاقی می‌افتد.
ولی آن‌ها برای ما احترام قائل‌اند. به ما احترام می‌گذارند.
۴۷ سال گذشته است؛ ولی در واقع ۵۰ سال شده، چون سه سال است که می‌گویند ۴۷ سال. ۵۰ سال شده است.
هیچ رئیس‌جمهور دیگری کاری را که باید مدت‌ها پیش انجام می‌شد، انجام نداده است؛ زیرا ایران نمی‌تواند سلاح هسته‌ای داشته باشد. نمی‌تواند داشته باشد.
---
و به‌محض اینکه این وضعیت با ایران پایان یابد، قیمت نفت به‌شدت سقوط خواهد کرد. قیمت بنزین هم پایین خواهد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/VahidOnline/77760" target="_blank">📅 01:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8sTi_N3Kncp7220QgkrlAmc2tTtqzQDlmal4RCPBSXU0fnyVj_y2k9DPsakO-dH9Sy9tv4jeV2i5hSEBacyQN7g9Zvp5KTwtXbEp9Ut5f25dMGTHveZ5Lo06TJpfBJipkTYZYZaq6evborUCwzszdUZiCu0pXCyYGnAkhGiN-3AtK1OmaLy2NLgsB-mAQpsl9FMm1xlcgHgQp86vfzWPHsvynw0q7QeeMimp6NslMfB4o6aPyHnlwzui0GbMBghp3Aad8PCA-8WOWZssgMYjr-Bxml2JaEUu2G_glwP5qeCzZV2wl591HcX8w_4txbFCPCDpX93Z6TjqzLS7uNdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز چهارشنبه ۱۴ مرداد، حملات جدیدی را به جنوب لبنان آغاز کرد و دلیل آن را «نقض آشکار آتش‌بس» از سوی گروه حزب‌الله دانست. این حملات که با صدور نخستین هشدار تخلیه پس از هفته‌ها برای ساکنان شهرک «منصوری» همراه بود، دست‌کم یک کشته و ۱۱ زخمی بر جا گذاشت.
این رویارویی‌های جدید در حالی رخ داد که نمایندگان لبنان و اسرائیل با میانجی‌گری آمریکا در رم مشغول گفتگو برای پایان دادن به درگیری‌ها و عقب‌نشینی مرحله‌ای اسرائیل از جنوب لبنان بودند.
یک منبع آگاه از روند مذاکرات به خبرگزاری فرانسه گفت هیات اسرائیلی، سه ساعت زودتر از موعد مقرر خواستار پایان جلسه شد. به گفته این منبع، یحیئل لایتر، سفیر اسرائیل در آمریکا و رئیس هیات مذاکره این کشور، درز «اطلاعات گمراه‌کننده» از سوی طرف لبنانی را علت این تصمیم عنوان کرده است.
با این حال، انتظار می‌رود این مذاکرات روز پنجشنبه در سومین و آخرین روز خود استمرار یابد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77759" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXaL-JS4_HY5-GbyVA7jLtn2Qj_A42z2DZHQqk9HoBcm3gyI0mPxP3KZkeQPxYVL6PAryIWLEBbJGvzvsU7SSzJNo8wcbmsNg69yv7D4MLahTgSyVE-fsiMoC3fkkKJpTX9B3eSAC4On3xxLI1CS4jxva80A_tSaoJzcESoQ2d1bI3U8NWKufibh6EkzPkkDqOL2AtgM_La-OHwlODYZCeDpV7CRoaAFAeoExfAPdpn0e5Szpu6mV0alGHbipgQAC-EwF5o9DkmiB1O6dz8kBHAydhYIzzTWU6tXt5ks_YBoEVJ18VbTVQTbEpfzaBGEOrRWAtxnvBOrTG0A0F7MVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده روز چهارشنبه ۱۴ مرداد تحریم‌های اعمال‌شده علیه شرکت هواپیمایی عراقی «فلای بغداد» را که پیش‌تر به اتهام همکاری با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بود، لغو کرد.
ا این حال، تحریم‌های بشیر عبدالقاظم علوان الشبانی، مالک معرفی‌شده این شرکت، همچنان به قوت خود باقی مانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/77758" target="_blank">📅 19:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=VK_Hp53G3Rrjlo03VB8tR5B-veq9H3p0b8cbiwo4OZ8WWF7Imy6G2A6gqpH2QzbpOlxEkSdz2JgGfIHHVKdOGa47-5lDYwyhcyzrI5JvPnABsO-Ql9sGA8BP2AESxZJQKFn--JNNCR-aHp-Chh06nl4DEJEmw_PAM_jUXQINL-mKjDTSDyc4ju3QOUQwq7UmTMnAWrABRwPLf7sQ6-sHMJJrHnO7H3UNRi_fe89rp3ConKVVwRE83Kb5RdFFD0WHB_4djpzcYcZvFkDOgAGge0qVJEXn-p_8aPHArpUnSwJfqA2fY475sJOLsx7-OIMt5lbn4fQrA8ZC8sEPP-azbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d9414940c.mp4?token=VK_Hp53G3Rrjlo03VB8tR5B-veq9H3p0b8cbiwo4OZ8WWF7Imy6G2A6gqpH2QzbpOlxEkSdz2JgGfIHHVKdOGa47-5lDYwyhcyzrI5JvPnABsO-Ql9sGA8BP2AESxZJQKFn--JNNCR-aHp-Chh06nl4DEJEmw_PAM_jUXQINL-mKjDTSDyc4ju3QOUQwq7UmTMnAWrABRwPLf7sQ6-sHMJJrHnO7H3UNRi_fe89rp3ConKVVwRE83Kb5RdFFD0WHB_4djpzcYcZvFkDOgAGge0qVJEXn-p_8aPHArpUnSwJfqA2fY475sJOLsx7-OIMt5lbn4fQrA8ZC8sEPP-azbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل روز چهارشنبه ۱۴ مردادماه با انتشار پیامی ویدیویی اعلام کرد این کشور با طرح پیشنهادی آمریکا برای خلع سلاح حماس و مدیریت غزه موافق نیست.
نتانیاهو در این پیام گفت: ««رئیس جمهوری ترامپ و تیمش فکر می‌کنند می‌توانند حماس را به خلع سلاح و غیرنظامی کردن غزه وادار کنند. ما در حال بررسی این موضوع هستیم. آنها پیش‌نویسی برای ما فرستادند، ما موافق نبودیم، این پیش‌نویس ما نیست؛ ما نظرات خود را ارسال کردیم.»
حماس هفته گذشته اعلام کرد به شرط خروج اسرائیل از نوار غزه، خود را خلع سلاح می‌کند. با وجود واکنش مثبت ترامپ، اسرائیل همچنان با این پیشنهاد حماس مخالف است و چند وزیر کابینه ائتلافی، پیشاپیش تاکید کرده‌اند که ارتش این کشور از غزه خارج نخواهد شد.
@
VahidOOnLine
نخست‌وزیر اسرائیل در سخنرانی خود در خاکسپاری رسمی پدربزرگ و مادربزرگ تئودور هرتسل، با اشاره به تحولات جاری تاکید کرد که این کشور در میان رویدادهای حساس نظامی و سیاسی قرار دارد.
بنیامین نتانیاهو با تمجید از رئیس‌جمهوری آمریکا گفت: «می‌خواهم این موضوع را روشن کنم؛ رئیس‌جمهوری ترامپ بزرگ‌ترین دوست ما و بزرگ‌ترین دوستی است که تا کنون در کاخ سفید داشته‌ایم و ایالات متحده نیز بزرگ‌ترین متحد ماست.»
با این حال، نخست‌وزیر اسرائیل با تاکید بر حفظ منافع بنیادین تل‌آویو افزود: «اما موجودیت اسرائیل — چه با توافق و چه بدون توافق — قابل مذاکره نیست. من مصمم هستم که هر آنچه برای تضمین امنیت و آینده‌مان لازم است را انجام دهیم.»
اسرائیل در حال حاضر در میانه گفتگوها برای دو توافق قرار دارد: توافق با لبنان برای خروج تدریجی نیروهایش از جنوب این کشور و توافق صلح غزه برای واگذاری مدیریت این مناطق به هیات صلح مطابق طرح ترامپ.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز چهارشنبه ۱۴ مرداد، در جریان بازدید از مرکز جذب سربازان جدید با تاکید بر اتحاد داخلی این کشور پس از حوادث هفتم اکتبر، تصریح کرد که تل‌آویو اجازه تشکیل کشور مستقل فلسطینی را نخواهد داد.
نتانیاهو با اشاره به این موضوع گفت: «ما در اینجا یک دولت تروریستی فلسطینی تاسیس نخواهیم کرد؛ دولتی که می‌دانیم قصد نابودی کشور-ملت یهود را دارد.»
نخست‌وزیر اسرائیل در ادامه افزود طرف مقابل در پی نابودی اسرائیل است، چرا که این کشور ترویج‌کننده ارزش‌های پیشرفت، دموکراسی و آزادی است؛ ارزش‌هایی که به گفته او، مورد نفرت «دشمنان بربر» قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77757" target="_blank">📅 17:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9RVYot_mYY84Djb62faj5oWLvBnB7bP0MwyxNX28xGx-PVHpyMqyUXyXgUuor27PsFphTw9PjGwHhhoTs1LXY-KZi4IrNBFi26fT3fVvw75x1lCXV_5cXoC9EVJagkoHhSTxA9DksS8F5bPkSxYzDI7vSfzJxBoSx1-C_LE6veH9jwgw7Au4E048thL_kEhQ4DywryDQVFyl_keEe_Oh5jU7AC4H8Ir3WR8dWe3LiOZsziPAJwDb_ZTqxW42cgXhZvqILbdKsCdyL9lFYkOxkImdWF3v19F8I2bX1pz3P2ROnrJTTz0JyPL-Og3uAI16jdtk2Fu8KiyhHqBBhHcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77756" target="_blank">📅 17:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E94WEvBLfRskcDNBF8vP5-sS0Sg43JWAf6vd_6hacrBEBad4_FXx2gf36NjyZnCAzdhrLOOVSNw6P_PQ1db-ndBr879tX57Mg5pC7Wxq8vEYTVY9PcqBIbr05KOm-sHAiHLufvTwCGvsFX3XM8e0fjgaWmaxdqh557NkV84ufpMEotM3MEWOlqrN-i7iAxTwE_uukJi75s6sojGG2Ji3cz9iu42fXaFZU3izaxt-fLa5bCnAccqvsp8ALv3Mf4cxpGLOXB4qCptv5tzLG_XwY7iW68pv1oYvTC3PNohcJ1OWRPhCwPflXv7eh5jIQBz2tIN3H0nwAWCFOTqSVWqsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر خرازی، دبیرکل «حزب‌الله ایران»، در واکنشی دوپهلو به تکذیب دفتر مجتبی خامنه‌ای، اعلام کرد این تکذیبیه را می‌پذیرد، اما ابراز امیدواری کرد پس از «تغییرات مهم آینده» این دفتر نیز همچنان پابرجا بماند.
این واکنش شامگاه سه‌شنبه ۱۳مرداد۱۴۰۵، در صفحه اینستاگرام دفتر خرازی منتشر شد.
در بیانیه دفتر او آمده است: «گرچه به احترام قائد شهید و نیز رهبر معظم حاضر، تکذیبیه روابط عمومی و دفتر نشر آثار را حدوثاً می‌پذیریم، ولی امیدواریم پس از تغییرات مهم آینده در حوزه دفاتر فوق، این تکذیبیه همچنان باقی بماند.»
در ادامه بیانیه آمده است: «خداوند ما را در صورت استقامت و صبر در راه اهل‌بیت و ولایت معظم فقیه یاری خواهد فرمود.»
فرستاده است.
دفتر مجتبی خامنه‌ای ساعاتی پیش از انتشار پاسخ خرازی، ادعای او درباره هشدار رهبر جمهوری اسلامی به مسعود پزشکیان بر سر استعفا را تکذیب کرده بود.
در بیانیه این دفتر، بدون نام‌بردن از خرازی، آمده بود: «مطلب منتشرشده در فضای مجازی که در آن فردی، ادعایی را درباره واکنش رهبر انقلاب اسلامی به نامه رییس‌جمهوری محترم مطرح کرده، از اساس کذب و خلاف واقع است.»
دفتر مجتبی خامنه‌ای انتشار این ادعا را «زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه» توصیف کرده بود.
یک روز پیش از انتشار این تکذیبیه، ویدیویی از سخنان خرازی در شبکه‌های اجتماعی منتشر شده بود. او در این ویدیو مدعی شده بود مسعود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده است.
خرازی همچنین گفته بود مجتبی خامنه‌ای در واکنش به این موضوع نوشته است: «یک بار دیگر پزشکیان استعفا کند، استعفایش را می‌پذیریم.»
او مدعی شده بود پس از این هشدار، پزشکیان و دیگر مقام‌های دولت از مطرح‌کردن دوباره استعفا عقب‌نشینی کرده‌اند.
@
VahidHeadline
درباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/77755" target="_blank">📅 17:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fp-0eCUHLj2pMH6g035WmDkHj74irGmXoZj-Le_YPasC1bwwJQsJ1j-AeZGKe-SSzQwULtmWZA8A3gpN_IZZ2KvlHpcwntjjR2MzEoJ7ox1ijz84dmILx4ye6nXkquxp6LuC0_R71TKikxux0WcpsvxHF6akqDO8uI_pfHnh-NP1qwmXru2U8RVLDF-IPHGDE7Cnqsw9tbK7YI6QZLBWL5Tp9e0u3_h8odTD5ZG8VltFb_-ySWnhTOvafqauxO-c1xPC-Zzhul95l2kHJw77TghSVRzirgTzwCEMiMElty4xn2I4LveP-3-hxDS_49MwIrPDNK1wWKQHJIWbhWIRfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل متحد، اعلام کرد که از ۲۹ اسفند ۱۴۰۴ تاکنون، دست‌کم ۵۶ نفر در ایران با اتهام‌های امنیتی اعدام شده‌اند.
ولکر تورک با صدور بیانیه‌ای یادآور شد که از این تعداد ۲۷ نفر از معترضانی هستند که در تجمعات اعتراضی دستگیر شده‌اند.
او اعلام کرد که در این مدت روند صدور و اجرای احکام اعدام در ایران افزایش یافته است.
کمیسر عالی حقوق بشر سازمان ملل متحد از مقام‌های جمهوری اسلامی خواست تا همه اعدام‌ها را متوقف کنند و در مسیر لغو مجازات اعدام گام بردارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/77754" target="_blank">📅 17:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dv3DPCLsnwgsJbiRcyYFrUST4MgCt5Xj7XooT8781zhQ9QiE5rGkxCoFXCWklJFSsv-g8VfJEeNEB-Kxq8KeIbgV-uyfWX6JAceeJcBoKSHKcRBloRAT6Qi8j18aJSokHXg5pS2-P9-31HHcTO7fevei_RLMHuiF_FmgPq90rppFErkQAfh6nUbY9SjnjhSRLw3UqD5k9mkScWdRfnZrFQnUGQ5gMpbjQ4OpPYm_RFqCx9u_fEuRl83XmIsvgnU1RGtTm0G3WfP7i3edSVaJAqvbHGCNWbTU1Bj5Aks6mUlqKQ6xSqUpkxfSykJx6Va7olpsLG8NwNYLNtq4I9oDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی قاسمی حسنوند، شاعر، زندانی سیاسی سابق و شهروند اهل شهرستان الشتر، روز یکشنبه ۱۱ مرداد ۱۴۰۵ پس از اقدام به پایان دادن به زندگی خود مقابل دفتر سازمان ملل در اربیل جان باخت.
منابع آگاه به ایران‌وایر می‌گویند او پس از آزادی از زندان با مشکلات روحی و فشارهای ناشی از پرونده قضایی خود روبه‌رو بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77753" target="_blank">📅 17:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04787365a6.mp4?token=QO7AAEd_JkWMYpiFRGMRnIeu5kiJuZkeeNfKa1_grYxlQUaV5nwvGQwzn2_ryLniMO73oy4yuyzZGtSclst21uZTPTgPwN4ZKjyd-ypLJkO3KAGh7wUPejtOAE_ZBEqJQI0eIDg2_1sjgWZeg8iN-wcLljeVlrm6vAys28qtAra6Y-XvXpNNannbjqPbvKqtBo828-V7c03fCN2kULvs4wSnDoOyJuwVLmTFaT-f7VJ84N1611PBbeNRzf2rS6BP0VZBF5jyLwsrwXlyD1wTi1Cx3zwB9cgbxj-yo-N1ZogJ-U5YwswjF1vusgfDl1FXcc6udaeuNzY43Irsv1iPgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04787365a6.mp4?token=QO7AAEd_JkWMYpiFRGMRnIeu5kiJuZkeeNfKa1_grYxlQUaV5nwvGQwzn2_ryLniMO73oy4yuyzZGtSclst21uZTPTgPwN4ZKjyd-ypLJkO3KAGh7wUPejtOAE_ZBEqJQI0eIDg2_1sjgWZeg8iN-wcLljeVlrm6vAys28qtAra6Y-XvXpNNannbjqPbvKqtBo828-V7c03fCN2kULvs4wSnDoOyJuwVLmTFaT-f7VJ84N1611PBbeNRzf2rS6BP0VZBF5jyLwsrwXlyD1wTi1Cx3zwB9cgbxj-yo-N1ZogJ-U5YwswjF1vusgfDl1FXcc6udaeuNzY43Irsv1iPgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
▪️
تنگه هرمز به‌زودی باز خواهد شد
▪️
مذاکرات با ایران به‌خوبی پیش می‌رود، اما تهران تمایلی به تایید آن ندارد
▪️
اگر بار دیگر عقب بکشند، ضربه سختی خواهند خورد
ترامپ:
اگر به اقتصاد نگاه کنید، اگر به اتفاقاتی که در حال رخ‌دادن است نگاه کنید... برای نمونه، ایران هرگز سلاح هسته‌ای نخواهد داشت. همین حالا هم دیگر نمی‌تواند داشته باشد، اما قرار است این موضوع رسمی شود.
تنگه [هرمز] خیلی زود باز خواهد شد؛ وگرنه ضربه بسیار سختی خواهند خورد و پس از آن، تنگه باز خواهد شد.
ما آماده انجام حمله‌ای عظیم بودیم؛ بزرگ‌ترین حمله از زمان جنگ جهانی دوم. بعد آنها با من تماس گرفتند و بسیار مؤدبانه گفتند: «لطفاً، می‌توانیم صحبت کنیم؟ می‌توانیم گفت‌وگو کنیم؟» آنها نمی‌خواستند... [جمله ناتمام است].
من هم گفتم: «بله، می‌توانیم صحبت کنیم. بیایید بالاخره این کار را تمام کنیم. بیایید انجامش دهیم.»
این کاری است که رؤسای‌جمهور دیگر باید طی ۵۰ سال گذشته انجام می‌دادند. می‌دانید، مدام عدد ۴۷ سال را می‌شنوید، اما سه سال است که همین عدد گفته می‌شود؛ حالا دیگر بیش از ۵۰ سال شده است.
رؤسای‌جمهور دیگر یا کشورهای دیگر باید می‌توانستند این کار را انجام دهند.
من کاری را انجام دادم که مجبور بودم انجام دهم؛ چون اگر آنها سلاح هسته‌ای داشتند، تمام این جهان جای متفاوتی می‌شد.
خبرنگار فاکس‌نیوز:
اگر دوباره عقب‌نشینی کنند و زیر توافق بزنند، کارشان تمام است؟
ترامپ:
اگر دوباره زیر توافق بزنند، ضربه واقعاً سختی خواهند خورد. خودشان این را می‌دانند و درک می‌کنند. من انتخاب دیگری ندارم. آنها نمی‌توانند سلاح هسته‌ای داشته باشند. موضوع بسیار ساده است.
این‌طور نیست که بگوییم: «خب، بیایید درباره چیز دیگری فکر کنیم.» نه؛ رؤسای‌جمهور بسیاری باید طی سال‌های طولانی این کار را انجام می‌دادند، اما انجام ندادند. حالا من دارم انجامش می‌دهم.
اوباما را کاملاً سرکیسه کردند. او فکر می‌کرد می‌تواند با پرداخت پول خودش را از این وضعیت خلاص کند. میلیاردها، ده‌ها میلیارد دلار به آنها داد؛ آن‌هم به‌شکلی بسیار احمقانه.
۱٫۷ میلیارد دلار پول نقد، اسکناس‌های سبز، در یک هواپیمای بوئینگ ۷۵۷؛ هواپیمایی پر از پول نقد. احتمالاً وقتی آن را دیدند، گفتند: «حتماً شوخی می‌کنید!»
نه، نمی‌توانید با پول‌دادن خودتان را از چنین وضعیتی خلاص کنید؛ تنها راه این است که با جنگیدن راه خروجتان را باز کنید.
اگر ما این کارها را انجام نداده بودیم، آنها مذاکره نمی‌کردند. ما ضربه بسیار بسیار سختی به آنها زدیم. اما ضربه سخت‌تر هنوز در راه است و امیدوارم مجبور نشویم از آن استفاده کنیم. امیدوارم مجبور نشویم.
گفت‌وگوهای بسیار خوبی داریم. آنها دوست ندارند به این موضوع اعتراف کنند، اما این کمی آزاردهنده است. به افرادی مثل شما می‌گوییم که گفت‌وگوهای فوق‌العاده‌ای داریم، بعد یک نفر از ایران می‌آید و می‌گوید: «ما دیدار نکرده‌ایم، ما...» [جمله در زیرنویس ناتمام است].
تمام روز چنین دروغ‌هایی می‌گویند. متوجه هستید؟ باورنکردنی است. می‌گویند: «ما این کار را نکردیم.» می‌گویند درباره موضوع هسته‌ای صحبت نکرده‌ایم.
خب، پس درباره چه چیزی صحبت می‌کنیم؟ آنجا نشسته‌ایم و بی‌کار انگشت‌هایمان را به هم می‌زنیم؟
اما اهمیتی ندارد. اینها فقط حرف است. تنها چیزی که اهمیت دارد، عمل است. آنها می‌خواهند توافق کنند. خواهیم دید چه اتفاقی می‌افتد. اگر توافق نکنند، برایشان خیلی بد خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/77752" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SdeMzvCy4ixK_JEbyNKWKLbh8cbPQU59U0sGO9XZC0Ag9ufcsfYR-TJ1nUxCg_FtR5DVHUkfEx6xeC4uVRcDzrjNYMDluhyKl7gX8a4gWbNarZOT0l719jHSOx75YcvNDAPpnPtCMk2bxqFRh4gRLDN0rq2s4y_6_7McTjhHMVVjGj4G-ZPntUN4Whhb-ZVrepT_N2grSpPtaMuHPiyUmCOgfrfFy573ryO35yHw0rLdPkQsE-3bolsz8pQDZeRzn7I3yA-hmp6sNYhOc8F_DpLXNFjEitoqGqCwXCMgMyWhXUNjOSfxm1zwRQZamL4Qqol521bfYUhmMudGgB33Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"آمریکا به توافق درباره هرمز نزدیک شده و به‌دنبال اعلام آن در روز چهارشنبه است"
اکسیوس، ترجمه ماشین:
به گفته دو منبع منطقه‌ای و یک مقام آمریکایی، آمریکا، ایران و عمان به دستیابی به یک توافق موقت برای بازگشایی تنگه هرمز نزدیک شده‌اند و آمریکا قصد دارد این توافق روز چهارشنبه اعلام شود.
🔻
چرا اهمیت دارد:
هدف از این توافق که چند هفته است درباره آن مذاکره می‌شود، ازسرگیری آتش‌بس میان آمریکا و ایران و آغاز دوباره مذاکرات بر سر یک توافق هسته‌ای است.
▪️
رئیس‌جمهوری ترامپ روز شنبه تصمیم گرفت تهدیدهای خود برای آغاز یک کارزار بمباران گسترده را عملی نکند تا فرصت بیشتری برای دیپلماسی فراهم شود. با این حال، اگر به‌زودی توافقی حاصل نشود، ترامپ ممکن است با حملات بزرگ موافقت کند.
▪️
توافق در حال شکل‌گیری برخی از خواسته‌های ایران برای کنترل بیشتر بر رفت‌وآمد در تنگه هرمز را تأمین خواهد کرد؛ کنترلی که ایران پیش از جنگ در اختیار نداشت.
🔻
اصل خبر:
به گفته دو منبع منطقه‌ای، توافق مورد بحث یک سازوکار موقت ۶۰روزه میان عمان و ایران در تنگه هرمز ایجاد می‌کند که امکان تمدید آن نیز وجود دارد.
▪️
همه کشتی‌هایی که از طریق تنگه وارد خلیج فارس می‌شوند، از یک مسیر شمالی در آب‌های ایران عبور خواهند کرد.
▪️
همه کشتی‌هایی که از تنگه خارج می‌شوند و به دریای عرب می‌روند، با هماهنگی ایران از یک مسیر جنوبی در آب‌های عمان عبور خواهند کرد.
▪️
در دوره ۶۰روزه هیچ‌گونه عوارض یا هزینه‌ای دریافت نخواهد شد.
▪️
طرف‌ها تلاش خواهند کرد ظرف ۳۰ روز مین‌های دریایی را از مسیر میانی تنگه پاک‌سازی کنند.
▪️
پس از پاک‌سازی مسیر میانی، این مسیر بر اساس مفاد یک سازوکار دائمی که قرار است میان عمان و ایران درباره آن مذاکره شود، برای رفت‌وآمد کشتی‌ها در هر دو جهت مورد استفاده قرار خواهد گرفت.
🔻
بله، اما:
کاخ سفید، عمان و میانجی‌های منطقه‌ای سه هفته پیش تصور می‌کردند با ایران به توافق رسیده‌اند، اما ایران حملات به کشتی‌ها را از سر گرفت. این موضوع به دو هفته درگیری و وضعیتی نزدیک به جنگی تمام‌عیار منجر شد.
🔻
پشت‌پرده:
به گفته منابع منطقه‌ای، علاوه بر مذاکرات میان عمان و ایران، مقام‌هایی از قطر، پاکستان و عربستان سعودی نیز در تلاش‌های میانجی‌گرانه مشارکت داشتند.
▪️
منابع منطقه‌ای گفتند کاخ سفید به‌طور فعال در مذاکرات حضور داشت. در روزهای اخیر چندین تماس میان استیو ویتکاف، فرستاده ترامپ، عباس عراقچی، وزیر امور خارجه ایران، و بدر البوسعیدی، وزیر امور خارجه عمان، انجام شد.
▪️
دو منبع منطقه‌ای گفتند عراقچی در پایان هفته گذشته در اصل با توافق موافقت کرد، اما همچنان به تأیید مجتبی خامنه‌ای، رهبر جمهوری اسلامی ایران، و شورای عالی امنیت ملی نیاز داشت.
▪️
یک مقام آمریکایی و یک منبع منطقه‌ای گفتند رهبری ایران روز سه‌شنبه روند تأیید توافق را تکمیل کرد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77751" target="_blank">📅 06:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi190pEEi7vxDnToSXxrVgnOVNWQaAB1K5RnXASl65h3DdwaQ8tPi4cNV1NvdPFtyvBqoImL_PMaSqGq0g6bi8woU6LhT0OA6MYzZY4Q5W9M2bddYkXlG99gRRTgjd0blgkcvt_0a3p6aardZS1ORrg998tw-yu-fS6O4sbj08r4XcsaOwHN9qGOhKSMkPKuqm-ppBfY5_u1zecv4LjEcbx2uIA9sY0itDHbHDOPcHu1lZy3knJ3HpaFwU0Z1x506qUds_cxq6Zt36_Clw9_A3xTQT_RDQ8Mh3FX_js4LE6Bo9SaKJMa2sXtk_8tE60j73halpttWfgNyM6eD2qxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
مسیر جنوبی عبور از تنگه هرمز همچنان برای همه کشتی‌های تجاری که قصد گذر از این آبراه بین‌المللی را دارند، آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی با وجود تجاوز بی‌دلیل ایران، به بیش از ۱۰۰۰ کشتی کمک کرده‌اند تا با موفقیت از این تنگه عبور کنند و این ترددها امروز نیز ادامه دارد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77750" target="_blank">📅 01:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77749">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=pAh-kHVzvGjlntGg8G7Lxez241D_-VUJMKhMIvmxI0vPFHwuXrn7ctXHNlsCTTaHt3twXVi8GMuw4TYGS0hAg3IgThdsCRXKs3LJIGohHOGqi_g0lOTQ20S7cvCBI1cdJ67jUKSdNessgqtAkXE6zW9JpkXWIsB_uombzBSyRsZCBqCbjB2CcZkubafpCFArGBEQw69yFX8HID20ZcDSXp-ED2yAuPtWTpxiJXQe0I-H8pHOXUt_ePXe-pkHz7z9eY04plW4quT-nxWELP35dfoxK5W2P-IZQ-jLAPHrp-SBv1OTvyoJvJ4w7DXmOJ_HMLjn-_TptAVa_CXR1mU3toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9140bd7bd.mp4?token=pAh-kHVzvGjlntGg8G7Lxez241D_-VUJMKhMIvmxI0vPFHwuXrn7ctXHNlsCTTaHt3twXVi8GMuw4TYGS0hAg3IgThdsCRXKs3LJIGohHOGqi_g0lOTQ20S7cvCBI1cdJ67jUKSdNessgqtAkXE6zW9JpkXWIsB_uombzBSyRsZCBqCbjB2CcZkubafpCFArGBEQw69yFX8HID20ZcDSXp-ED2yAuPtWTpxiJXQe0I-H8pHOXUt_ePXe-pkHz7z9eY04plW4quT-nxWELP35dfoxK5W2P-IZQ-jLAPHrp-SBv1OTvyoJvJ4w7DXmOJ_HMLjn-_TptAVa_CXR1mU3toWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت امیرعلی حیدری و سروش کرمی، دو نوجوان کشته در اعتراضات دی ۱۴۰۴ که هفته گذشته برای دومین بار به خاک سپرده شدند.
یکی از خانواده‌ها بعد از هفت ماه متوجه شد جسد اشتباهی به آنها تحویل دادند و خانواده دیگر دریافتند فرزندشان در بازداشت نیست و کشته شده.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77749" target="_blank">📅 01:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=vIHikOPFbXKZ22HY_0AHd_wuNUIs7RTZr4avHR-ENFysKkVX65nOUqy7A0Tp0k8dvFZIG6kE69fSom8YNiTncGjtKcEDVxoJOv9X0nEQLO5RdnbyVIODm_ZkYjsmI9qK3B1kBLONHs2vRjT9Kw2AltD3-zeLSdxWziXppuPCi6D9eRve_r9Rg1BDdFxVYbRJDQP5c-gYx2Syo0Wwnwm1R_TCKrkO3AvviXJZsrjVjU5JNmJ3IJDpQNpQkQjlPFSUe-rR2QrbPsOl4g4FIiWbTvUbn8sqIAodzvhMkholIe3uEiq_CNa36h0KAgniirrX_ffpqznnb70XforyrDYCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae742191f.mp4?token=vIHikOPFbXKZ22HY_0AHd_wuNUIs7RTZr4avHR-ENFysKkVX65nOUqy7A0Tp0k8dvFZIG6kE69fSom8YNiTncGjtKcEDVxoJOv9X0nEQLO5RdnbyVIODm_ZkYjsmI9qK3B1kBLONHs2vRjT9Kw2AltD3-zeLSdxWziXppuPCi6D9eRve_r9Rg1BDdFxVYbRJDQP5c-gYx2Syo0Wwnwm1R_TCKrkO3AvviXJZsrjVjU5JNmJ3IJDpQNpQkQjlPFSUe-rR2QrbPsOl4g4FIiWbTvUbn8sqIAodzvhMkholIe3uEiq_CNa36h0KAgniirrX_ffpqznnb70XforyrDYCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه ۱۳ مرداد اعلام کرد نیروهای این کشور تا خلع سلاح کامل حماس، از خطوط فعلی در نوار غزه عقب‌نشینی نخواهند کرد.
نتانیاهو در ویدیویی که در شبکه‌های اجتماعی منتشر شد، گفت: «ترامپ و تیم او بر این باورند که حماس می‌تواند کاملا خلع سلاح و غزه غیرنظامی شود؛ ما در حال بررسی این موضوع هستیم.»
نخست‌وزیر اسرائیل همچنین با اشاره به طرح پیشنهادی آمریکا افزود: «آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم، چرا که پیش‌نویس ما نبود. ما پاسخ‌های خود را ارسال کرده‌ایم.»
او تاکید کرد که نظرات و پاسخ‌های تل‌آویو پیش از رسانه‌ای شدن این موضوع به طرف آمریکایی تحویل داده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77748" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZ75FkpZJYlxXf2sx5BrqN5LiNQq7ddK93wTj6Jj_nitzw3k2KT0ksJJZE-Ufu-D54QBFanhj9tiIsBzFa_gW0JqC0N1OZqBJp1QP4LZlqaSkvfgXIZzAQqltK324stmOC0ZIuUqzg5Zn2hPYhc2hQ1AzA46bR-zo0juFi_ryz7okSUzBeJwVmKkTCL_ee2GindljEWmfOiOBwtvkYpucAD3as_T6fnHAJcFZMqrz8notG_pEfVsvVxBdOxcSQbysBOcseQPq9pU1e7YviVYYmLGa45Kol09U9MnXq8V7d2ngbB_-jfrK3OU5q3MSEONlNKo99MXf7JklAuIJ_nmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی قطر گزارش داد تمیم بن حمد آل ثانی، امیر قطر، روز سه‌شنبه در تماس تلفنی با دونالد ترامپ، رییس‌جمهوری آمریکا، آخرین تحولات منطقه، به‌ویژه تلاش‌ها برای کاهش تنش میان آمریکا و جمهوری اسلامی و نزدیک کردن دیدگاه‌های دو طرف را بررسی کرد.
بر اساس این گزارش، ترامپ از نقش قطر در حمایت از تلاش‌های دیپلماتیک و تسهیل گفت‌وگو میان طرف‌ها برای تقویت امنیت و ثبات منطقه قدردانی کرد.
امیر قطر نیز بر اهمیت ادامه گفت‌وگو، استفاده از راه‌حل‌های دیپلماتیک و پایبندی همه طرف‌ها به مفاد یادداشت تفاهم میان تهران و واشینگتن تاکید کرد. او همچنین خواستار حمایت از ابتکارهای بین‌المللی برای مهار تنش‌ها شد.
دو طرف همچنین درباره شماری از موضوعات مورد علاقه مشترک گفت‌وگو و بر ادامه هماهنگی و رایزنی درباره تحولات منطقه‌ای و بین‌المللی تاکید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77747" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgQBZISCR4abwYooZos-l90Nrc7u7nXJ6Xqm0OcDIbVSzCwL0LiH4DQ91N8J8ppQPgtwBMnW32yU7SeB8waixGK_CtRdZ9t-pI6LLfU-W4VCbXfkdmkzeX6OiBBh7310ZMSwxMxvd5YaA99oVbi_griO8PDZ1FNMeu7YkxEb15pCLxNiheOihmejs7izPG3AzCRDE_EsStF7iwQyB8mXDe7gBlLRk-vqfUux2xCC3vYZFU0TZkqDAUG_00trRvsF7qVISB77nxRxR5AXbbOkRcx8anF2ltauZt0KhDLDH57vgbBLWyFhQJfHNLBtabB5cemE9jGxsaEFTCty81bzkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشتیرانی هند روز سه‌شنبه ۱۳ مرداد اعلام کرد که یک پرتابه به یک کشتی با پرچم هند در نزدیکی یمن اصابت کرد که باعث واژگونی و غرق شدن آن شد.
ساربانا‌ندا سونووال در پیامی در شبکهٔ ایکس نوشت که اما هر ۱۴ ملوان حاضر در کشتی، از جمله ۱۳ تبعهٔ هند، توسط گارد ساحلی یمن نجات یافته و به بندر مخا منتقل شدند.
وزارت خارجه هند نیز اعلام کرد که این کشتی تجاری به نام «ام‌اس‌وی فیض نور علیا» روز ۱۳ مرداد در دریای سرخ و در سواحل یمن غرق شده و این وزارتخانه در حال هماهنگی با مقام‌های یمنی دربارهٔ این حادثه است.
پالایشگاه‌های هند از زمان حملات حوثی‌ها به چند نفتکش سعودی، به دریافت محموله‌های نفتی خاورمیانه به‌صورت تحویلی روی آورده‌اند.
تردد در دریای سرخ در نزدیکی سواحل یمن به‌دلیل اقدامات حوثی‌های همسو با تهران مختل شده است. حوثی‌ها با ایجاد اختلال در صادرات نفت عربستان، دامنه درگیری میان آمریکا و ایران را گسترش داده‌اند. پیش‌تر نیز عرضه نفت از طریق تنگه هرمز مختل شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77746" target="_blank">📅 22:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SacsVaqvBA-TdquoVpWg0zEETEpmDZqUAGBh32xUQb0h-PrqsJ2s9UZUVcSE7yd5pAEY-m0ekFHSYQH1z-OAhLp8XSiUhQE95DwEOYrn-v1xDxA-ZPCs5JjVHvhSAWLK6shvifzovzkjqwwW45knGf1WwhzIxC1ZQEm0iQZ98F1rvhSP03eWmQRj5xHCtF6Kl9embrsdXqXzo9OqoGz3iF7YaHrgvL8UWC14a_wtcPuGk152OmRbLKkwsaIm0aTEWFpXiqCz4vGe0YqUJzniwPd0fwSBv-t24iWbC-QQQMR6FJGzxkRmwEQuhc2T60ler-xRb97ks5etS-_IF-B21g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pDL_0q-l8204TmYETRsStDzFJu2n7zbk-Gpcp_Bg6KfJQZNRrB9JxC0iGgZr1UzyzfXycBBKRt6awkrn6nOqv1OvYfn4oEFRybCU5HvL3_pMsdZGcBKuhclvgxxux2E8epu2inpmNPk9n5oTjQ-Tk5AK7j6YRGOvNhgsp4kl7hWsQ2C_b0fiZqmUhacntd7AqaPOF_OV1tSlGOmE2wE4nr4Pw9rVLPBW0naysVlJ2cdi4ahoOaNlIKck_13Cy7BCZa79MGr4STAOmSMg43cTlKFP4FyHjRkI7PLd7PPMmtIr0yYFdvNeWJ3RvFDo3JzxIPYutG41YoBySLKQj0a9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Du12G9bPPueMwa7HsqiA2COFmBRhf50MClsI_XhaG4FRH8J2kURF6W67j4zQHL8spsSMugERa411WsVg40IjvbhwZNbeaTEZXRg51kInlPzBqn2a_BiTkMeqSqAgF9CBd90pYv4cl_tgnd159iM9ok2VsmQBaMoOOmwXGdc-NK-3J0-SAFC3aktjCDhb09b3y7IVHiTNcymuwvqHHXPxx4bbA8xA_X4H80PmRq53tyuGaR0KeYy6JKl5S1TBclTkwfJKGd3UArP6WRpsW2iZRaCuAfJCn9ECgwoeqiR9oh8dGgwgK-qv8FurZKlz--X2Lc00Iw_RHBcMn7NYxF1s4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GuPoMV7jBboWSHIXEDPf9nvzLdb4NzpUsGPtllv6ynjU_pJK3_MSJ_V82f6YVRdLW4NzBKhLI6UlbH-YyfGuGZAvBldcfklHmvxjfO6zwgBixbEC_oT6Ag6JTGeU2fPh0vP7vJrci9Bg3JjYDEexoZuVzuwz8M5xlx3ai9xIEPtyuWoLa6s6lAra7oUlMBhmU2AAsjMvxcfJHUDLTXR-9HTf_zEfbR4lP5cX-y2Efvk8L63fT5NQmFnDFv_oOcp4kVIPisFSylTZDP2pLpGhTGSUl-2LoZOIGzTMJssklsSjMCnFm4N6AY6BcHPSh6LZmIqjGuczO5TddXkiEr1j8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=P5ZWe3duMXpAjoZ0juvAEwvLTgDb7H-esJIa07gUJ9OpFfMBAsfLiR6hA8bwjz3xwYTuSZeFKXB0-UpYePmEbwfxy2H1xe8g6p_zfejWvF85Sf5WDs_rGaOpX7sK6-7nDzuhQGdS1wloSEpgwf3yKNK7yWG11IH3WitXFdxHxiWpeuX8COH5sHU0itIprUkHqplvHCtzA7bi5iJAmpmIMnAPrI1kkY65rUpMziZVdxrLgqKtrhGUG_WjVPXFpcmbAio1eUZUEjAP7NDJuz7EJW84hvOJWRECcexwYSC35t-L9M1cHfrsmVifliDhYLrn-4hSssaHB5C1VIYDEKkO2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f1489028e.mp4?token=P5ZWe3duMXpAjoZ0juvAEwvLTgDb7H-esJIa07gUJ9OpFfMBAsfLiR6hA8bwjz3xwYTuSZeFKXB0-UpYePmEbwfxy2H1xe8g6p_zfejWvF85Sf5WDs_rGaOpX7sK6-7nDzuhQGdS1wloSEpgwf3yKNK7yWG11IH3WitXFdxHxiWpeuX8COH5sHU0itIprUkHqplvHCtzA7bi5iJAmpmIMnAPrI1kkY65rUpMziZVdxrLgqKtrhGUG_WjVPXFpcmbAio1eUZUEjAP7NDJuz7EJW84hvOJWRECcexwYSC35t-L9M1cHfrsmVifliDhYLrn-4hSssaHB5C1VIYDEKkO2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت ایالات متحده ممکن است تا روز چهارشنبه برای بازگشایی تنگه هرمز با ایران به توافق برسد؛ توافقی که به گفته او می‌تواند قیمت انرژی را تثبیت کند.
او روز سه‌شنبه در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «ما با ایرانی‌ها در حال مذاکره هستیم و فکر می‌کنم این احتمال وجود دارد که امروز یا فردا برای بازگشایی تنگه و حرکت به سوی وضعیتی عادی‌تر در این درگیری به توافق برسیم.»
بسنت در پاسخ به این پرسش که آیا چنین توافقی به ایران اجازه خواهد داد از کشتی‌های عبوری عوارض دریافت کند، گفت: «فکر می‌کنم منظور، آزادی رفت‌وآمد خواهد بود.»
@
VahidHeadline
مارکو روبیو، وزیر امور خارجه آمریکا، روز سه‌شنبه ۱۳ مردادماه اعلام کرد هدف نهایی مذاکرات با ایران، دستیابی به توافقی برای خلع سلاح هسته‌ای این کشور است و گفت توافق کنونی که تمرکز اصلی بر آن قرار دارد، به تضمین عبور امن کشتی‌ها از تنگه مربوط می‌شود.
روبیو با اشاره به ادامه تردد کشتی‌ها و انتقال نفت از تنگه گفت: «همین حالا کشتی‌ها از تنگه عبور می‌کنند و صادرات نفت ادامه دارد. تنگه باز است.»
او افزود: «خلع سلاح هسته‌ای ایران توافق نهایی است. توافق فوری، که اکنون بیشترین تمرکز بر آن قرار دارد، مربوط به تنگه است.»
روبیو همچنین گفت مذاکراتی میان عمان و ایران درباره فراهم کردن امکان عبور امن کشتی‌های بیشتر از تنگه در کوتاه‌مدت در جریان است که آمریکا نیز در آن دخیل است. به گفته او، این مذاکرات پیشرفت کرده، اما هنوز به نتیجه نهایی نرسیده و واشنگتن امیدوار است به‌زودی به جمع‌بندی برسد.
@
VahidOOnLine
قطر اعلام کرد تلاش‌ها برای دستیابی به راه‌حلی دیپلماتیک میان ایران و ایالات متحده ادامه دارد، اما هنوز توافقی حاصل نشده و هیچ مذاکره مستقیمی میان دو طرف برنامه‌ریزی نشده است.
ماجد الانصاری، سخنگوی وزارت خارجه قطر، روز سه‌شنبه ۱۳ مرداد ۱۴۰۵ به خبرنگاران گفت رایزنی‌های دوحه با ایران و آمریکا همچنان ادامه دارد. به گفته او، این رایزنی‌ها بر دستیابی به «راه‌حلی کوتاه‌مدت» متمرکز است تا زمینه ازسرگیری گفت‌وگوها و احیای کامل روند میانجی‌گری فراهم شود.
اظهارات سخنگوی وزارت خارجه قطر یک روز پس از آن مطرح شد که دونالد ترامپ، رییس‌جمهوری آمریکا، گفته بود مذاکرات با تهران در جریان است و ایران با «آخرین فرصت» برای دستیابی به توافق روبه‌روست.
ترامپ گفته بود این مذاکرات به درخواست ایران، عربستان سعودی، امارات متحده عربی و قطر انجام می‌شود و افزوده بود: «این آخرین فرصت آن‌ها برای امضای یک توافق خوب است.»
در مقابل، مقام‌های جمهوری اسلامی تأکید کرده‌اند که هیچ مذاکره‌ای با آمریکا در جریان نیست و گفت‌وگوهای کنونی ایران تنها با عمان و درباره تنگه هرمز انجام می‌شود. تهران همچنین اعلام کرده است که این هفته هیچ نشست مهمی برنامه‌ریزی نشده است.
@
VahidHeadline
قیمت نفت روز سه‌شنبه ۱۳ مرداد پس از اظهارات مقامات قطر و وزیر خزانه‌داری آمریکا که امیدها را برای حل دیپلماتیک مناقشه خاورمیانه و بهبود عبور نفتکش‌ها از تنگه هرمز افزایش داد، حدود ۴ درصد کاهش یافت و به پایین‌ترین سطح خود در سه هفته اخیر رسید.
@
VahidOOnLine
—-
ترامپ هم دوباره چندین پست پشت هم منتشر کرد که یکیش لینکی است مربوط به مطلب ۲ روز پیش
breitbart
با تیتر:
ترامپ: «توافق قریب‌الوقوع است»؛ مذاکرات با ایران درباره خلع سلاح هسته‌ای و هرمز دوشنبه از سر گرفته می‌شود
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77740" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4QQiF-GzLQfgR_SmWyxuW8SOEmxnODUGzvmfrYW9Kjsz1sywOLBahpYheIoGsGw1KA7yNUwfZlo0PhOQQv7Ci-5QJ9CEB-KOxyrYHCiHDA9HYfjUWcyRKxMBjZJeh0FseApNhOGT39-XKjESsgtYjEUhYHe7Hs2jaGy3_g9UXIB1eBcQq4w5Ws4B2DBHmbBf8K2bqqvhCJ1oNnVWS9s8cBrd2t2JQ-zDOQPGlcAgIxWNXayoyviKJpJuniytovNEcvlS-1NmfmlYkLf2EjL3hcm5kWQhf-s8qHV8BHsvBBGDjGGdQ79VxHnTQhMUrwkJp8nMJhw5LwqbScO3D3juA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=KsE7JL6wICKLMNd-XK0UeJxDyuqkcRa-JLLD8DZJaH1ddPR8-Otb_QGC4XV8CJKUyWHqhi1EL2GYAMpVi5Th5aN0bJc89nC0Ep2w27oYJCSQfEXAOko8Eb65_5Sf_HVoq1U-X8erbTsyioV7_ZipLghHpl5pbrzrdRJh8lDB0r16ghybddsdWnbG4Hjvg6fRAY45YlSu4Fb_tl72eW94V69JSzVVkaAH4VdF15JOF9GqarO6ei657jreA1nJoyGh8GRoXyAXM26aqu7Rmkp6hWfCQ0g6jbVjN9lJxW6OX0S9LAHEufxE9BriVNMeBzaOpW6k2ZsjiqW0XYWXUjglSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ae4cf2c87.mp4?token=KsE7JL6wICKLMNd-XK0UeJxDyuqkcRa-JLLD8DZJaH1ddPR8-Otb_QGC4XV8CJKUyWHqhi1EL2GYAMpVi5Th5aN0bJc89nC0Ep2w27oYJCSQfEXAOko8Eb65_5Sf_HVoq1U-X8erbTsyioV7_ZipLghHpl5pbrzrdRJh8lDB0r16ghybddsdWnbG4Hjvg6fRAY45YlSu4Fb_tl72eW94V69JSzVVkaAH4VdF15JOF9GqarO6ei657jreA1nJoyGh8GRoXyAXM26aqu7Rmkp6hWfCQ0g6jbVjN9lJxW6OX0S9LAHEufxE9BriVNMeBzaOpW6k2ZsjiqW0XYWXUjglSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوها از کانال‌های غیررسمی حکومتی
درگیری میان حامیان جمهوری اسلامی و مقلدان صادق شیرازی، از مراجع تقلید منتقد جمهوری اسلامی، در جریان مراسم اربعین در کربلا به بازداشت ۱۴۰ نفر و مجروح شدن ۵۴ نفر انجامید.
شبکه تلویزیونی «اشعائر» عراق، رسانه نزدیک به "آیت‌الله صادق شیرازی"، صبح دوشنبه ۱۲ مرداد ویدیویی از این درگیری منتشر کرد.
بر اساس گزارش این رسانه، گروهی با در دست داشتن تصاویر علی و مجتبی خامنه‌ای و پرچم‌های «یا لثارات الحسین» و «یا لثارات الخامنه‌ای» مقابل دفتر آیت‌الله صادق شیرازی در کربلا تجمع کردند و علیه او شعار سر دادند.
این رسانه می‌گوید حامیان علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، و فرزندش مجتبی خامنه‌ای هنگام عبور از مقابل دفتر صادق شیرازی این شعارها را سر دادند که با واکنش هواداران و مقلدان این مرجع تقلید روبه‌رو شد.
به گفته کاربران شبکه‌های اجتماعی، این درگیری ابتدا با مداخله پلیس عراق متوقف شد، اما در ادامه میان حامیان جمهوری اسلامی و نیروهای امنیتی عراق نیز تنش و درگیری رخ داد و پلیس عراق در نهایت با استفاده از قوه قهریه به آن پایان داد.
بر اساس گزارش‌های منتشر شده، در جریان درگیری مقابل موکب منتسب به آیت‌الله صادق شیرازی، ۱۴۰ نفر بازداشت و ۵۴ نفر مجروح شدند. این آمار تاکنون به‌طور مستقل تأیید نشده است.
همچنین در برخی گزارش‌ها ادعا شده است که حسین ستوده، مداح حکومتی، از چهره‌های حاضر در این تجمع بوده و تلاش داشته این مراسم را به موضوعات سیاسی پیوند بزند.
"آیت‌الله صادق شیرازی" از منتقدان نظریه ولایت فقیه است و رسانه‌های جمهوری اسلامی او و جریان منتسب به وی را با عنوان «شیعه انگلیسی» معرفی می‌کنند. او ولایت فقیه را محدود به امر قضاوت می‌داند و با تفسیرهای جدید از اسلام و مذهب تشیع مخالفت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77735" target="_blank">📅 18:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kW8XU4dEWwOb-9uMHUVil816g9XvAD3cZ0W3atIUxF-D2mCCsiU1KWJCFf_w8KrmQLhWt0qp6Q-XV0Eg7qrygS_bDHpgjExiJlIFG840i3ztLY-qZT9ZeDzPCKq5YrxHAX_5QQGKqO7Sy6msKrHHGrmSLZEt0pyhUSUiG8-fmVCRqA1kfxK-Fj9VGpnWMdWSW401kPBbZY7XoJVssSZi5wHt44yzU01JMje_c4Xyzz2smZKDzQNIHZLRLnXqV_1t7MFxccNrlZtF2R1PyHj79s8hcEXo-b9OpwYBFl1AEEIzlxgolHj8WjPsBOrlqJgJB-WXUleJZPxCSPwEY_n0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZNrzffySdNaCyo6lIFXaR1SGpi3gb9dLpZqWzpdOji-60u_LdNZZKo6UzfLTLylD897vR-mz45Oif6oKJXLQmN_ECqsKZj3ENtxlu2xo6esDfGzhdeSEaDCszGpH4CkopKtChiETfGJ1rE1EHHcj9hCTYN-HGRppPd-kgF_KSzsVBf6RMF8DuOGVmu9IiSdnbOen-bhokIOh_4FXrklLeSEfFTl2539Um0UIrV48PxyWnuUToEq0o48xpYcYPaUuo-eSCvZl8VA8ZTAmRCw2xD4gj2F29OU9oDG2pUH-ZRUGW2Cd1uT90iOXfjzvBDCtn-CLb-Lz-VtoHQi-OkfvIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شرکت نفتی آرامکوی عربستان سعودی روز سه‌شنبه اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال جاری، هم‌زمان با افزایش قیمت انرژی بر اثر جنگ خاورمیانه، ۴۴ درصد رشد کرده است.
بر اساس گزارش مالی آرامکو، سود خالص این شرکت از آوریل تا ژوئن به ۱۲۲ میلیارد و ۶۰۰ میلیون ریال سعودی، معادل ۳۲ میلیارد و ۷۰۰ میلیون دلار، رسید؛ در حالی که این رقم در دوره مشابه سال گذشته ۸۵ میلیارد ریال بود.
امین ناصر، مدیرعامل آرامکو، گفت این شرکت با وجود اختلال بی‌سابقه در عرضه نفت از مسیر تنگه هرمز، توانسته است با استفاده از خط لوله شرق به غرب، ظرفیت‌های ذخیره‌سازی و پایانه‌های صادراتی، فعالیت خود را ادامه دهد.
اعلام افزایش سود آرامکو هم‌زمان با انتقاد دونالد ترامپ، رئیس‌جمهور آمریکا، از سود بالای شرکت‌های نفتی صورت گرفت. او گفت این شرکت‌ها به‌دلیل کمبود نفت ناشی از جنگ «بیش از حد پول درمی‌آورند».
@
VahidHeadline
شرکت بزرگ انرژی بریتانیا، بی‌پی (از بزرگ‌ترین شرکت‌های نفت و گاز جهان)، اعلام کرد سود خالص این شرکت در سه‌ماهه دوم سال ۲۰۲۶، هم‌زمان با افزایش قیمت انرژی در پی جنگ آمریکا و جمهوری اسلامی، بیش از دو برابر شده و به سه میلیارد و ۹۱۰ میلیون دلار رسیده است.
سی‌بی‌اس به نقل از خبرگزاری فرانسه نوشت پنج شرکت بزرگ انرژی غربی، شامل بی‌پی، شورون، اکسون‌موبیل، شل و توتال‌انرژیز، در مجموع نزدیک به ۴۷ میلیارد دلار سود خالص در سه‌ماهه دوم سال ثبت کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77733" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O8jvYB0_wjAGCZopYSVjO9LkyK8wEXqnaY-7CBxM1waRvaZZ_HpL7Vms7yUXyXqMeZ007IvNVhxw1c--9Qlldomc55fuKcY8ufg8r2Jm9W7PH5K_1PX6dKdRKhwCimQ18Ys352io4XWmNrSqtgFTfEGXIkMO8zaio1hWaGqU_KADJd31bYfGKHlWKeG-Wo4zwlYhdvRd2DFBq_3rT_O80r2TcSVqif7KQKo9Jcn56bgCu1rGy9P1CfIK5bq8oz9a52itiC20lnhDKK7b426nabWSjzar1kSBlp3SKXBPpMONPDGE-oz96JuXzCbGSCoCops20445pTQi-YH681b2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/on2jbS3QARrV2zVoIjZpp0tN5h_rp0oy7_SLfBlEfkJSlKnjInzUnM6FbOEY3O-nMM5psIuSbACwQ-zskuK5mCTFFjiNBbBk1uJXVgr8VDDurm8raznLfN0oxdaiLse8H_6WopQsVCAkqt3YbtHRkOzHqhDqM1n3A-7YR9OMgIOtXdTdJwPO-9ExFcmCT2WbZX1v6DYl0vh-dsxMdFMTklNj-Q1YQOiZ1lO8FB1mS3OVusfyyMjLKXKD9Y3DPqK5vcF7dtcCuUowdzMlBLFDxmp9edm2eqrYIV--21a2aGQjgRoKZ0wWfExnPZLwllD9ZP3y4dSqQ4TS0pLF_CpKtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=XxeqQu2Wx1UdCNkxFGzHZI3_Hy0Qeirgrqvlt33i8lWCjDKx7x5IV4NINCXU9gU1KFs5jpg2Xro2VG4JXzV-mVSa8RaYj0ukbyiyZsTCI_5VRsRbluLp646bOABy6PaTMPeWQB_M3Ibmhxr13OkgqChVzqdq0UGa-FTaXEl1hpuIwkVxNZq_rf7X-9qkcoirnhmczF3Too8GYpPR3wdFQC-GI8g-mzZ-ckUFOeB7gvwsVIbNM7nGOQmOsr3X2VSSCO-LoA5YpEx8UVpfEVKNyBVE0PZu5LRwg1c9JOm3zYbtY9MBJogZAP65s-ZDgFOiY3pirPrzVQRLqwry4CiQUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/616a7ca97f.mp4?token=XxeqQu2Wx1UdCNkxFGzHZI3_Hy0Qeirgrqvlt33i8lWCjDKx7x5IV4NINCXU9gU1KFs5jpg2Xro2VG4JXzV-mVSa8RaYj0ukbyiyZsTCI_5VRsRbluLp646bOABy6PaTMPeWQB_M3Ibmhxr13OkgqChVzqdq0UGa-FTaXEl1hpuIwkVxNZq_rf7X-9qkcoirnhmczF3Too8GYpPR3wdFQC-GI8g-mzZ-ckUFOeB7gvwsVIbNM7nGOQmOsr3X2VSSCO-LoA5YpEx8UVpfEVKNyBVE0PZu5LRwg1c9JOm3zYbtY9MBJogZAP65s-ZDgFOiY3pirPrzVQRLqwry4CiQUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در تیزر تبلیغاتی حاوی بخشی از سخنانش که قرار است در چند قسمت و از امشب به وقت محلی از تلویزیون ایران پخش شود، ضمن رد گزارش‌ها درباره استعفایش گفت: «استعفا نخواهم داد و خواهم ایستاد. اینها می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و اینها یک چیزی می‌گویند.»
این سخنان یک روز پس از انتشار کلیپی پربازدید از سخنان محمدباقر خرازی، دبیرکل تشکلی موسوم به «حزب‌الله ایران» که برادر همسر مسعود، برادر مجتبی خامنه‌ای، رهبر سوم جمهوری اسلامی ایران منتشر می‌شود که او درباره «۲۸ بار استعفای پزشکیان» و «تهدید مجتبی خامنه‌ای به پذیرش استعفای بعدی» سخن گفته بود.
این سخنان واکنش‌های چهره‌ها، جریان‌ها و رسانه‌های حامی و منتقد دولت را برانگیخته است؛ از جمله حمید رسایی که از آقای پزشکیان خواسته بود برای راستی‌ازمایی سخنان محمدباقر خرازی استعفا کند.
مجتبی زارعی، نماینده عضو کمیسیون امنیت ملی مجلس ایران در واکنش به طعنه آقای رسایی نوشت: «از ۹۰ میلیون ایرانی فقط یک شاهد برای تهمت خرازی به امام سید مجتبی شهادت داد ؛ سرکرده شریان!»
@
VahidHeadline
حمید رسایی نیم‌ساعت پیش، یعنی پس از انتشار ویدیوی پزشکیان هم تاکید کرد که هنوز تکذیب نشده:
بعد از اینکه سیدمحمدباقر خرازی درباره نحوه برخورد رهبری با استعفای پزشکیان - که تاکنون تکذیب نشده - ادعایی کرد، اطرافیان رئیس جمهور برخوردهای متفاوتی و گاه توهین آمیزی داشتند.
تصور کنید اگر وی ادعایی برخلاف آنچه نقل کرده به زبان آورده بود (مثلا رهبری به پزشکیان گفته شما باید محکم ادامه بدی) چه اتفاقی می افتاد:
rasaee
👈
بعدش، یعنی دقایقی پیش، این خبر منتشر شد:
دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، با انتشار بیانیه‌ای، گزارش‌ها درباره هشدار به مسعود پزشکیان در خصوص استعفا را تکذیب کرد. این بیانیه یک روز پس از انتشار ویدیویی از سخنان خرازی منتشر شد که در آن مدعی شده بود پزشکیان تاکنون ۲۸ بار استعفا داده یا تهدید به کناره‌گیری کرده و مجتبی خامنه‌ای اعلام کرده در صورت تکرار این اقدام، استعفای او پذیرفته خواهد شد.
@
VahidHeadline
نسخه منابع حکومتی:
دفتر رهبر انقلاب: مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور مطرح کرده از اساس کذب و خلاف واقع است
🔹
متن اطلاعیهٔ روابط‌عمومی دفتر رهبر انقلاب:
بسم‌الله الرحمن الرحیم
🔹
با گرامی‌داشت اربعین حسینی و ادای احترام به روح بلند رهبر شهید انقلاب به‌اطلاع مردم شریف و مبعوث‌شدهٔ ایران می رساند در روزهای گذشته برخی نقل‌قول‌ها از رهبری معظم انقلاب اسلامی در فضای مجازی منتشر شده که متاسفانه زمینه‌ساز تشویش اذهان عمومی و ایجاد انشقاق و اختلاف در جامعه است.
بر همین اساس برخی نکات را درباره اخبار و مطالب مربوط به مقام معظم رهبری بیان می‌داریم.
🔹
مرجع رسمی انتشار پیام ها، اخبار و مطالب مرتبط با آیت‌الله سیدمجتبی حسینی خامنه‌ای، پایگاه اطلاع‌رسانی دفتر رهبر انقلاب و یا پایگاه حفظ و نشر آثار رهبر انقلاب است و هرگونه مطالبی که خارج از این چهارچوب منتشر شود، فاقد سندیت و صحت است.
🔹
رهبر معظم انقلاب اسلامی در پیام‌های خود از جمله در پیام اخیر بر حفظ اتحاد مقدس و حفظ حرمت مسئولان دلسوز و خدمتگزاران نظام اسلامی به‌ویژه دولت محترم تأکید داشته‌اند. مطالبی که برخلاف توصیه‌های مؤکد رهبری، موجب انشقاق و دودستگی در جامعه و زمینه‌ساز نسبت‌های نادرست به مسئولان محترم می‌شود، در جهت اهداف بدخواهان و دشمنان قسم‌خوردهٔ ملت ایران است.
🔹
بر همین اساس مطلب منتشرشده در فضای مجازی که در آن فردی ادعایی را دربارهٔ واکنش رهبر انقلاب اسلامی به نامهٔ رئیس‌جمهور محترم مطرح کرده از اساس کذب و خلاف واقع است.
روابط عمومی دفتر رهبر انقلاب اسلامی
۱۳ مرداد ۱۴۰۵
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77730" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q_Wkxo1XuM6m2_HWO3z723P_KyDBiXhGWaymg2ui6OqD5u8RkKmRPxhJcGtUI7CWjdSzcdA9IGfYqR6u9iFB5M79pJQtqvd45EmJRbTZJ-_J0H_0HUIasivymAXRejA5rDEEjvZFTmU-9z7XvGhLKx-BHy9Kk41tYFJsOLXYzz5LMTrWxdToFxWxbLyYqhOcLwEXvBBXxjMjQ3uFQx5cCa18tbqnZL6ip552yddvF1mGjsqhXLcmySfZh7ZT65W3jVnp-Y-GyOphCtzqs912kvlXem4hOH_vhg-Lo0Tsz3d5jJm3pojklUAoYs4_rJEJAKNQLxZY3jHb2mqMA1HouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساکنان شماری از روستاهای جزیره قشم حدود چهار ماه است به آب لوله‌کشی دسترسی ندارند و برای تامین آب مورد نیاز خود ناچار به خرید تانکرهای چندمیلیون‌تومانی یا استفاده از منابع نامطمئن شده‌اند.
براساس گزارش میدانی آوش، یکی از ساکنان روستای طبل گفته است: «چهار ماه است شیر آب خانه‌مان باز نشده. حالا فقط با تانکر زندگی می‌کنیم. من توانستم سه میلیون تومان بدهم و آب بخرم، اما خیلی از روستایی‌ها حتی همین پول را هم ندارند.»
پس از آسیب‌دیدن یکی از تاسیسات آب‌شیرین‌کن در جریان حملات ماه‌های گذشته آمریکا به نوار جنوبی ایران، وضعیت تامین آب در بخش‌هایی از جزیره به‌شدت بحرانی شده است. او گفته آب لوله‌کشی تقریبا قطع شده و مقدار آبی که با تانکر توزیع می‌شود نیز پاسخ‌گوی نیاز ساکنان نیست.
این اظهارات در حالی مطرح شده‌اند که عباس علی‌آبادی، وزیر نیرو، ۲۹تیر۱۴۰۵ و در جریان سفر به هرمزگان گفته بود همه آب‌شیرین‌کن‌های منطقه در مدار بهره‌برداری قرار دارند وهیچ‌یک از جزایر کشور با کمبود آب مواجه نیست.
او همچنین گفته بود با وجود آسیب‌دیدن زیرساخت‌ها در حملات اخیر، خدمات آب و برق پایدار مانده و شرایط مدیریت شده است.
عبدالرحیم رضوانی، نایب‌رییس شورای اسلامی بخش مرکزی قشم  گفته است ساکنان برخی روستاها بیش از سه ماه برای وصل‌شدن آب انتظار می‌کشند و پس از آن نیز تنها چند روز به آب شبکه دسترسی دارند. به گفته رضوانی، قیمت یک تانکر چهار هزار لیتری آب به حدود یک میلیون و ۴۰۰ هزار تومان رسیده است.
در همین حال، یکی از ساکنان قشم گفته است برخی خانواده‌ها که توانایی خرید آب ندارند، برای مصارف روزمره از چاه‌هایی استفاده می‌کنند که از سالم‌بودن آب آن‌ها اطمینان ندارند. او به نقل از یکی از اهالی گفته است: «آب تمیزی نیست؛ حتی حیوان داخل آن می‌میرد، اما به‌هرحال آب شیرین است. برای خوردن استفاده نمی‌کنیم، اما برای کارهای روزمره مجبوریم همین آب را به خانه ببریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77729" target="_blank">📅 18:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77728">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCyBafTP0Np4nkq4Th4Thpc16uZVdpE3PxztNBalV9lHBJvTrnQawgAJGH6Ir69IKjPPDLTGO5cfLTaEjMr0aiTnaeYhYZHIrAjqfFuDDFhgqDVkCwRFha-qDt-Yfs_Wyo34mB9TVCE2BhCgvJIsbTzOJhUZbVhKpbTAMGBMn_EzE0hJkMtwXIP7V-DynH3EeJPrS09p2JtTmuAjbo5hiq-lGFKl9a5T0ZonUlNSjvxhnx6tbnc45dDhxYh5isFy-NSit3O-j4JNhjhjzNm6hs-mO4LjTIo8xuK15mtU3JroPuGooMQEwXKoC4ZgZ8DSLKOSgoHZ3HpWuolrADcHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه موج پلمپ واحدهای صنفی و مراکز فرهنگی در ایران، در روزهای اخیر، دست‌کم سه مجموعه فرهنگی و صنفی در بابل، مشهد و تهران با دستور مقام‌های قضایی یا نهادهای ناظر پلمب شده‌اند.
هرانا خبر داد مجموعه «شهر کتاب» در شهرستان بابل، با دستور قضایی و به‌دست اداره نظارت بر اماکن عمومی پلمب شده است.
هم‌زمان، گزارش‌ها از پلمپ «کافه معماری سکنج» در مشهد حکایت دارند؛ فضایی تخصصی و فرهنگی که محل فعالیت معماران، هنرمندان و دانشجویان بود. تاکنون درباره علت پلمپ این کافه اطلاعاتی منتشر نشده است.
مجموعه «خانه ارغوان» نیز اعلام کرده است که به‌دلیل «پلمب موقت از سوی مراجع ذی‌ربط»، فعالیت خود را تا رفع محدودیت‌ها متوقف می‌کند. این مجموعه در خیابان فرشته تهران فعالیت داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/77728" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/utPJNHSFHkh_fhFWYeBdIjpUn0NDKB_nKSB83IQrPm5yP42AN_OvH7EoECJO23490eUSsFfrb7177Mep_7UGdFoZX-oMBZylg2Hv8cD13J3Bdfo9Cl_n2jwVMl2yi5OuXP1Ye-uyC4Y-YDVKXCoxqyCCU796-ExtMJRhpXQzTgeRLAIV-kc_b47_oOQKfWFWXQfc5Lwx8V_g6AAA1RFQSk9xQlzgoaWSrdXd_7PF-Hd0ccHLK-oW7l6BjnMnblBQe-9too-lRO7EnuOhEBeK4O8UkUFkhD16Bv66ruE-xqFDcCGBd2MMWjQYIbPc-kH_iFlj77KxQHgti_u5sDc1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سازمان حقوق بشر ایران» اعلام کرد «مهدی روشنی»، معترض بازداشت‌شده در ارتباط با اعتراضات ۱۶دی‌۱۴۰۴ در شهرستان ملکشاهی، با اتهام‌های امنیتی به اعدام محکوم شده است.
این سازمان روز دوشنبه ۱۲مرداد۱۴۰۵ گزارش داد مهدی روشنی روز یکم بهمن‌ماه در منزل خود بازداشت و به تهران منتقل شد. به نوشته سازمان حقوق بشر ایران، او پس از بازداشت، دو ماه در بی‌خبری مطلق نگهداری شد و برای گرفتن اعترافات اجباری تحت شکنجه‌های شدید قرار گرفت؛ اعترافاتی که به گفته این سازمان، مبنای صدور حکم اعدام قرار گرفته است.
سازمان حقوق بشر ایران به نقل از یک منبع مطلع مدعی شده که یکی از افرادی که مهدی روشنی را پس از بازگشت از تهران دیده، آثار گسترده شکنجه را بر بدن او مشاهده کرده بود.
این فرد گفته است: «اگر بدنش را می‌دیدید وحشت می‌کردید. جای سالمی روی آن نبود. پر بود از آثار شوک الکتریکی و شلاق، اما حاضر نشده بود اعتراف کند.»
بر اساس این گزارش، مهدی روشنی اواخر اردیبهشت‌ماه ۱۴۰۵ با تودیع وثیقه آزاد شده بود، اما حدود دو هفته بعد بار دیگر نیروهای امنیتی او را بازداشت کردند و از آن زمان تاکنون در بی‌خبری مطلق به سر می‌برد.
این منبع همچنین گفته است خانواده مهدی روشنی تحت فشار قرار گرفته‌اند و به آنها هشدار داده شده درباره پرونده او سکوت کنند. به گفته این منبع، حدود یک ماه پیش به خانواده او اطلاع داده شده که وی با اتهام‌هایی از جمله قتل «احسان آقاجانی»، مامور پلیس، به اعدام محکوم شده است.
بر اساس گزارش‌های منتشر شده، احسان آقاجانی در جریان اعتراضات ۱۶دی‌ماه در شهرستان ملکشاهی کشته شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77727" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ftlwUOEf8hzuUZcZNnfCLM9YsPEU_LNeabMW65qkV1joQ2A3XblVwkxQvo87JsmqO-k7rNEEjfbSvV9451dgkQ79IKLHpo-GNKrgQ4Hy2ouY9sXqa88J9154zqYz1wYeLmGN0cLKUa6R2zS0Sm8gB9KiYE_pL6fUD0kh7920xA0JmXlnYRnG0faVZgUlEknbS4KaDA3bBP2vZ6egPsfq2eWirgWWWHy7Wo6qnSy5jVQC7B0AzEMyBgeqUVqOq6X1lcxsxqTZ5ZkwgcrgPHO_E31h3awVuHk4hi8xGy-yHerM-euRJ2qi1Fhl0VU8BuTMGlw9T80cJO3k72-3iEOG_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
آپدیت: برگشت
پیش از آپدیت:
نرم‌افزار پیام‌رسان «تلگرام»، روز دوشنبه، به‌طور ناگهانی از فروشگاه «اپ‌استور» شرکت اپل در سراسر جهان حذف شد.
بر اساس اعلام کاربران شبکه‌های اجتماعی، جست‌وجوی نام تلگرام در اپ‌استور با هیچ نتیجه‌ای همراه نیست و
صفحات رسمی دانلود
این برنامه با «خطای ۴۰۴» مواجه می‌شوند.
اگرچه این پیام‌رسان روی دستگاه‌هایی که از قبل آن را نصب داشته‌اند کماکان بدون مشکل کار می‌کند، اما امکان
دانلود تازه
یا نصب مجدد آن روی آیفون و آیپد فعلا وجود ندارد.
تاکنون هیچ‌یک از شرکت‌های اپل یا تلگرام بیانیه رسمی درباره دلایل این تصمیم صادر نکرده‌اند و مشخص نیست که این اقدام دائم است یا موقت و آیا ناشی از بررسی‌های قانونی و محتوایی است یا یک نقص فنی.
پیش از این نیز در سال ۲۰۱۸ اپل برای مدتی کوتاه تلگرام را به دلیل «نگرانی از انتشار برخی محتواهای خلاف قوانین» از اپ‌استور خارج کرده بود که پس از اعمال اصلاحات لازم، این برنامه مجددا بازگشت.
@
VahidOOnLine
🔄
و آپدیت چند ساعت بعد:
شرکت اپل اعلام کرد پس از آنکه در یک بررسی مشخص شد محتوایی مغایر با قوانین این شرکت در رابطه با «ممنوعیت سوءاستفاده جنسی از کودکان» در تلگرام قرار گرفته، این پیام‌رسان را به‌طور موقت از «اپ‌استور»، فروشگاه نرم‌افزاری اپل حذف کرده است.
به گفته اپل، پس از آنکه تلگرام «محتوای متخلف را به‌سرعت حذف و حساب کاربری منتشرکننده را مسدود کرد»،  دوباره به اپ‌استور بازگردانده شد.
تلگرام نیز در واکنش به گزارش‌ها درباره حذف این پیام‌رسان، در شبکه‌ اجتماعی ایکس نوشت: «گزارش‌های مرگ من بسیار اغراق‌آمیز است.»
@
VahidOOnLine
🔄
پست پاول دورف، مدیرعامل تلگرام درباره این موضوع، ترجمه ماشین:
🍎
دیشب، اپل برای مدت کوتاهی تلگرام را از اپ استور حذف کرد، زیرا یک کاربر به‌تنهایی محتوای پورنوگرافیک غیرقانونی را در یک گفت‌وگوی گروهی عمومی جاسازی کرده بود.
⬅️
تلگرام ظرف چند ساعت دوباره در دسترس قرار گرفت. اما می‌خواهم توضیح بدهم چه اتفاقی افتاد؛ هم برای هشدار دادن به دیگر توسعه‌دهندگان اپلیکیشن‌ها و هم برای کمک به محافظت از جوامع آنلاین در برابر حملات مشابه.
🧹
از آنجا که تلگرام با استفاده از گزارش‌های کاربران، فیلترهای هوش مصنوعی، هش‌های محتوا و دیگر ابزارهای نظارتی، محتوای غیرقانونی را به‌سرعت از گروه‌های عمومی حذف می‌کند، مهاجم ناچار شد به یک ترفند فنی متوسل شود. او با ویرایش یک پیام قدیمی در یک گروه فعال، محتوای غیرقانونیِ تغییریافته با هوش مصنوعی را در آن قرار داد. در نتیجه، این محتوا عملاً از دید اعضای گروه پنهان ماند و آن‌ها نتوانستند آن را ببینند و فوراً گزارش کنند.
💰
مهاجم یک «باج‌گیرِ حذف محتوا» بود؛ کسی که از صاحبان گروه‌ها باج می‌خواهد و در ازای آن، جوامعشان را هدف قرار نمی‌دهد. این باج‌گیران با استفاده از حساب‌های خودکار، محتوای غیرقانونی را در گروه‌های عمومی قرار می‌دهند و سپس مستقیماً آن را به اپل گزارش می‌کنند تا باعث حذف جوامع مشروعی شوند که صاحبانشان از پرداخت باج خودداری کرده‌اند.
🤝
از نظر عملی، محتوای پورنوگرافیک غیرقانونی در گروه‌های عمومی تلگرام یک مشکل نظام‌مند نیست. نظارت ما مؤثر است (
https://telegram.org/safety
). همین که مهاجمان ناچارند به محتوای دارای تاریخ گذشته و عملاً نامرئی و دیگر ترفندهای فنی متوسل شوند، این موضوع را ثابت می‌کند.
⚠️
با این حال، دو درس مهم برای توسعه‌دهندگان اپلیکیشن‌ها و جوامع آنلاین وجود دارد:
— باج‌گیران راهی پیدا کرده‌اند تا اپل را وادار به واکنش افراطی کنند. اپل پیش از تماس با ما، تلگرام را از اپ استور حذف کرد. این موضوع برای هر اپلیکیشن موبایلی که میزبان محتوای تولیدشده توسط کاربران است، یک خطر بالقوه و نظام‌مند ایجاد می‌کند. اگر اپلیکیشنی که بیش از یک میلیارد نفر از آن استفاده می‌کنند بتواند بدون هشدار قبلی از اپ استور حذف شود، هر اپلیکیشنی ممکن است حذف شود.
— تاکتیک‌های مورد استفاده باج‌گیرانِ حذف محتوا در حال تکامل است و جوامع در سراسر پلتفرم‌های اجتماعی را در معرض خطر قرار می‌دهد. تلگرام تجربه گسترده‌ای در شناسایی ترفندهای باندهای هماهنگِ گزارش‌دهی و محافظت از جوامع مشروع دارد؛ حتی وقتی این کار خطر حذف موقت خود اپلیکیشن ما از اپ استور را به همراه داشته باشد. ممکن است دیگر پلتفرم‌ها به همین اندازه آماده نباشند.
هوشیار بمانید!
☝️
durov
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/77726" target="_blank">📅 05:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/avw92Npkw2z2HxuHrf68_EQWgHP2VuZtavzJ-qFvNDrh5XkB79tcVOnwQAuly81WdzNYinbKXHBdXOu0L2yXnZRAoGX4pwkmko4TpxgYjn6QMHWQdNIxgmYgOYv3eRVYGU7Vnb9Ovb82A3eFv4S5USSd9pR0YXObV3L2wrTTs8MRXpDh--5CxpIjfekOM-EWiCy8-f3Xk7wyZUtEfDna-piy2P252oDssPKl4v8IJ_DFXAsL22kMS8TVBM4uDSShmk9rtqnNFqCpPhrmRWjKdYHFSDDM-LOdNX0pPPuc0fzJbH4sEv0Rx7XKc8DUPwbhM9Qtsb-y2yZfd5zsD9e-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)  گزارشی درباره وقوع یک حادثه در ۲۰ مایل دریایی شمال‌شرق الخصب در عمان دریافت کرده است.
یک کشتی باری از طریق کانال ۱۶ بی‌سیم VHF اعلام کرده است که با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
مقامات در حال بررسی هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77725" target="_blank">📅 03:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu4FsOlmm6jrRU-0R25ZsHrtxlfBoBBPy80WgtW_eF0oPXtNXEIAveXP1WqZyj--3RpUU2fGqnbuqQv5oI-GTXC31xjHB6Ga_2ESWjjDCJ8cGfMmARP2MPpgQZ6TL64lwd4TGk7RNP7JITD3BrshEO8mxSnZtOcIduZFhTtl8goR49zuFryxPuZ7ksCAqhM-DcSBIvvUZYNJbTzfLzgz_Mx9rrsv_ebb7w1W2ejJM0G6f48sunno3ZNnY1e8oB6v3P4DIhUrPSTzbTsN21U75nrmubZ6-oyS6HXyZi9Ce0yDxDIUYicSS5SL_iPE7zNf4CS68yUL7vktYvOsXgnzD2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu4FsOlmm6jrRU-0R25ZsHrtxlfBoBBPy80WgtW_eF0oPXtNXEIAveXP1WqZyj--3RpUU2fGqnbuqQv5oI-GTXC31xjHB6Ga_2ESWjjDCJ8cGfMmARP2MPpgQZ6TL64lwd4TGk7RNP7JITD3BrshEO8mxSnZtOcIduZFhTtl8goR49zuFryxPuZ7ksCAqhM-DcSBIvvUZYNJbTzfLzgz_Mx9rrsv_ebb7w1W2ejJM0G6f48sunno3ZNnY1e8oB6v3P4DIhUrPSTzbTsN21U75nrmubZ6-oyS6HXyZi9Ce0yDxDIUYicSS5SL_iPE7zNf4CS68yUL7vktYvOsXgnzD2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفت‌وگوی ترامپ با خبرنگاران
بخش‌های مربوط به ایران
متن مکالمه با تشخیص و ترجمه ماشین
:
به دلایلی، وقتی در حال مذاکره‌اند، دوست ندارند بگویند که دارند مذاکره می‌کنند. من می‌گویم: «صبر کنید، ما در حال مذاکره‌ایم. چه اهمیتی دارد؟ داریم مذاکره می‌کنیم.» و آن‌ها گاهی آن را انکار می‌کنند، با اینکه ساعت‌ها و ساعت‌ها کنار یکدیگر می‌نشینند و مذاکره می‌کنند.
مذاکرات در حال پیشرفت است.
قرار بود دیروز آن‌ها را به‌شدت هدف قرار دهیم؛ بسیار بسیار شدید. حمله‌ای شدیدتر از هر حمله دیگری.
فکر می‌کنم می‌توانم بگویم—و ژنرال‌ها از روی آگاهی می‌گویند—شدیدتر از هر حمله‌ای از زمان جنگ جهانی دوم تاکنون. این خیلی بزرگ است.
ما آماده اجرای حمله بودیم که آن‌ها تماس گرفتند. علاوه بر آن، عربستان سعودی تماس گرفت، امارات تماس گرفت، قطر تماس گرفت و افراد بسیاری با من تماس گرفتند. نمی‌خواهم از کلمه «التماس» استفاده کنم، اما به‌ویژه ایران نمی‌خواست هدف حمله قرار بگیرد.
آن‌ها گفتند: «می‌خواهیم مذاکره کنیم. می‌خواهیم درباره تنگه مذاکره کنیم.» اما از دیدگاه من مهم‌تر از آن، می‌خواهیم درباره هسته‌ای‌زدایی ایران مذاکره کنیم، زیرا اصل ماجرا همین است. دلیل اینکه این کار را انجام می‌دهم همین است.
این کار باید مدت‌ها پیش انجام می‌شد. اکنون ۵۰ سال شده است. همیشه می‌گفتیم ۴۷ سال، اما سه سال دیگر نیز گذشته است. ۵۰ سال است که رؤسای‌جمهور دیگر باید کاری را که من انجام می‌دهم، انجام می‌دادند. یا کشورهای دیگر؛ لازم نبود حتماً ما باشیم، اما کشورهای دیگر باید این کار را می‌کردند. هیچ‌کس انجامش نداد و زمان آن فرا رسیده بود.
ما درباره تنگه صحبت می‌کنیم؛ بازشدن تنگه و اینکه به معنای واقعی کلمه تا فردا کاملاً باز باشد. این مرحله اول است.
مرحله دوم این است که پس از آن درباره موضوع هسته‌ای  صحبت کنیم. اساساً هسته‌ای‌زدایی ایران باید انجام شود. باید انجام شود. این مرحله دوم خواهد بود.
اما
مرحله نخست، بازشدن تنگه است. مرحله دوم هسته‌ای‌زدایی خواهد بود. آن مرحله کمی زمان می‌برد، اما ما در این زمینه بسیار قاطع هستیم.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد و من هرگز موضعم را در این‌باره تغییر نداده‌ام.
درباره کشتیرانی در تنگه هرمز: من اجازه نمی‌دهم از کسی پول بگیرند. ما طرفی هستیم که کنترل کامل را در اختیار دارد. ما کنترل کامل داریم.
می‌دانید، چیزی به نام محاصره داریم که با این نیروی دریایی اجرا می‌شود و به آن «دیوار فولادین» می‌گویند؛ «دیوار فولادین ایالات متحده».
نه، نه، هیچ پولی گرفته نخواهد شد. اصلاً درباره گرفتن پول صحبت نمی‌کنیم. پولی گرفته نخواهد شد.
فکر می‌کنم به این واقعیت بسیار افتخار می‌کنم که به مردم فرصت می‌دهم. به مردم فرصت خواهم داد. انجام حمله‌ای به آن بزرگی علیه یک کشور، تصمیم بسیار بزرگی است. ترجیح می‌دهم اکنون آن را انجام ندهم.
امیدوارم سر عقل بیایند
قرار بود حمله دیشب آغاز شود و مدت زیادی ادامه پیدا کند و در نهایت عملاً چیز بسیار کمی باقی بماند؛ هیچ‌چیز باقی نمی‌ماند.
اگر این فرصت به من داده شود که اجازه دهم افراد زیادی زنده بمانند، می‌خواهم آن فرصت را به آن‌ها بدهم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77724" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHqJPGvZ4rwGQmtsuMKOJJAdbZdDxmwEu0Vy0VLpnEFh2UtYg3Fn-yKsBCqk5vYstDhNpeQtQFr1MzonVhV9Qcl7_xmr6AFrCF0EUlTL4GEJ0JIW0-M8VHFyl2NZCQXty_ObdCAKPTFtoFCn4AdOtU-JOdtNiVcLh5xiAUgpHyruPtoM1xxcHjfyxBUmJvu5bpGpaU_L9Q1LDUd885Ufx85VFvmwbHsyk07-xRwhzAxFBvQ14XJrOPwEZv0JjdSXCMh3q_JIIRzXgYPFq6KdmH9zjSjKJ_26kG1g1wJuDmkQUhiaqlb9XDC0yDwQc-XHZ6Ip2YQ4yJ3zird0w8-utg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۱۲ مرداد در حاشیه نشستی در کاخ سفید، به خبرنگاران گفت مذاکراتی که در حال حاضر با جمهوری اسلامی ایران جریان دارد، «آخرین فرصت» تهران برای امضای یک «توافق خوب» است.
ترامپ که پیش‌تر حمله‌ای که به گفته او «بزرگ‌ترین حمله نظامی از زمان جنگ جهانی دوم تا کنون» بود علیه ایران را لغو کرده بود، با انتقاد دوباره از مقام‌های جمهوری اسلامی که انجام مذاکره با ایالات متحده را تکذیب کرده بودند، گفت: «ایرانی‌ها تماس گرفتند، بعد از آن از عربستان سعودی، قطر، امارات و بسیاری کشورهای دیگر با من تماس گرفتند که یک فرصت دیگر بدهم. نمی‌خواهم بگویم «التماس» کردند ولی ایران واقعا نمی‌خواست مورد حمله قرار بگیرد.»
ترامپ تاکید کرد که این مذاکرات «با درخواست ایران» و حمایت کشورهای منطقه و جهان انجام می‌شود و «آخرین فرصت» برای جمهوری اسلامی است که انتظارات او درباره برنامه هسته‌ای را برآورده کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/77723" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mSgSWpkZI71EJaE2-x2q7yc9n1m_ftqMAUvCUhW9kcBx_PJL0YHpF0u40lSoeNsVj5nXaetaQH_ZT1iAMSCNjm_roeX8dwZThJJz1H7PwV_HKllqw1ICgO0gl4-0y4DgwodpPNIPM1ytR3DZdtEd7eeqn4LD3HuYLoNMvJkEdS_11BdYVMeFA5IM97KV0mtxIPpU46QMoiQOCAhtkcXLTMEKaMAu0uWYRILlTqrg54Cev6aP6iqP9o-D5yjQOzQCx_WRb6YLt0X7YpJscZoSStYT_73ccofivugSOzdLLFsi_ecGLLUeV6pFQCUnhNmSAIIrPj9t099ue-pgX5z0WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رهبری ایران به‌طرز باورنکردنی دورو است!
آن‌ها درخواست جلسه می‌کنند ــ بعضی‌ها می‌گویند «التماس می‌کنند» ــ مذاکرات آغاز می‌شود و جلسات بیشتری نیز برای آینده بسیار نزدیک برنامه‌ریزی می‌شود، اما بعد آشکارا و با افتخار می‌گویند که هیچ گفت‌وگویی ندارند، درباره هیچ‌چیز صحبت نمی‌شود و فقط با «عمان» سروکار دارند.
سپس همان یاوه‌گویی‌های همیشگی‌شان را ادامه می‌دهند و می‌گویند تنگه هرمز با قدرت توسط آن‌ها اداره خواهد شد، در حالی که این تنگه همین حالا نیز کاملاً تحت کنترل نیروی دریایی ایالات متحده و «محاصره» ما قرار دارد؛ یا همان‌طور که بعضی‌ها می‌گویند، «دیوار فولادین ایالات متحده»!
هیچ‌چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ‌چیز نیز نخواهد رسید، مگر آنکه توافقی حاصل شود یا تسلیم کامل صورت بگیرد. چه ایران بخواهد این را بپذیرد و چه نخواهد، ما در واقع در حال گفت‌وگو درباره راه‌حلی برای مشکلی هستیم که آن‌ها طی چندین دهه ایجاد کرده‌اند.
موضوع بسیار ساده است: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/77722" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gocqdbrL2AolHmsh8u1W_FV_BVdd1P9Q6at2iO2Co7bh3PO0B-eDD_KFnnzlZbTAdiAFygR_Afoiq4aDaXiCq0DmjWGn6N__cgPxahqTc-JzYhLGAKdV3-tiufwWTu5YWoPyFywEP7D24-zSDfpKT0CMnbApEhZP7QeAYrAmSWhbtRXa77FOYCzSyi8zlbAOsyzojBov7pxb3h9L0xoNPgcCkS85YbNMib_M6bsZgr6mgY5N7e7vo7Qx_3fLYcBUlb45pV8tHzvXWydL0gK9y5oRKhma4XS_Kfh2Z9PaatM36C1b4-HdkEKMWKF12M2xFgGUIAwrLpdNjEyeVjmumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیران امور خارجه جمهوری اسلامی ایران و پاکستان در گفت‌وگویی تلفنی درباره تحولات منطقه‌ای و روند تحرکات دیپلماتیک رایزنی کردند. در این تماس، محمد اسحاق دار، وزیر امور خارجه پاکستان، از عباس عراقچی برای سفر به اسلام‌آباد در نخستین فرصت دعوت کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77721" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXzP9d_l0pP8A3PaBphrFGKjjtak0OpTQVm3IF5H3RW8K5z5xiWRshj7I1yLWXYlcARRr3sSiSv5N-8xr_oTNf0FCOaY4u8sLGR1TD0fM9itC58APsUCJ-HTos3bSqiWA-eo3U5og-RAtxYNeMK1THmCFVD6RUMtRcJ_3O2ruVUXzWwgEggNpg0aIG8A4QTGFXyN6zx6uj89tzUxgDs8329qEZx4asoUIYXDhWhGV_ahhuk3s098rRYPpitLt49RSmv_6CRub4NadOUKsJiVdIiIHyOrCUAAUYfA5dCqjykf2BMJY-GVcCKLWnpdqVLXuCtEH2Bw0usS8_5P_hgQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا روز دوشنبه ۱۲ مرداد بار دیگر از شرکت‌های نفتی خواست قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند و مایک ویرث، مدیرعامل شورون، را به‌دلیل قدردانی نکردن از تلاش‌های دولتش در حمایت از صنعت نفت مورد انتقاد قرار داد.
دونالد ترامپ در یک مصاحبه تلویزیونی، ویرث را سرزنش کرد که به نقش دولت او در کمک به شرکت‌های نفتی اشاره نکرده است.
او در پیامی در شبکه اجتماعی خود، تروث سوشال، نوشت: «تنها چیزی که او به‌راحتی از گفتنش صرف‌نظر کرد این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و حتی خود کشور ما نابود می‌شد!»
ترامپ افزود: «برای مثال، آن‌ها مایک و شورون را از ونزوئلا بیرون کردند، اما حالا بازگشته‌اند، بزرگ‌تر و قدرتمندتر از همیشه، و انتظار دارند ثروت هنگفتی به دست آورند!»
به گفته ترامپ، «این موضوع شامل سایر شرکت‌های نفتی هم می‌شود... و همین حالا قیمت نفت برای مصرف‌کننده را پایین بیاورید!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77720" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtDzIEexaAzB-Pnntq2yvW_RgPFcnweWbd0i9R3I-p0CdjnR5fp_4O2qwW1t91pxICK0nHNP-DDu9jh-KWkhBOfRT7T1rMquiJpPRYMPqkfkyH26vOg7zex2pUvH7tNWvMLYISGx5gMINfmpN311vUAXNlgnudDE9WFnpgzXWUJQeBZ-BnLzSu1z831J1o6JcMP3Kh3ttPtVr0JiDcWP_gleL2F3917XhGzLo7i_cC7iw0eHKqs0RvoKks9NB-AGhLeO7VEPeZMk6GbJBvMHrPsCe8GdP4WLd0bQyeCI43VMEiSVHehOzKCyIBKU7Fw4HRBFP977lj376HLOU12UuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی‌رغم افزایش امیدها برای دستیابی به پایان درگیری‌ها میان اسرائیل و گروه‌های فلسطینی، مقامات امدادی غزه اعلام کردند حملات هوایی اسرائیل برای دومین روز پیاپی به مناطق مختلف این منطقه در روز یکشنبه یازدهم مرداد، جان دست‌کم ۱۸ فلسطینی را گرفت.
به گفته مقام‌های بهداشتی فلسطینی، از بامداد یکشنبه، جنگنده‌های اسرائیلی شهر غزه در شمال، شهر دیرالبلح در مرکز و منطقه خان‌یونس در جنوب نوار غزه را هدف قرار دادند که بیشترین شمار تلفات روزانه در چند هفته اخیر را بر جا گذاشت.
این در حالی است که دونالد ترامپ، رئیس‌جمهور آمریکا، از دستیابی به یک پیشرفت در تلاش‌ها برای اجرای توافق آتش‌بس سال گذشته خبر داده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77719" target="_blank">📅 17:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GosSnAKj633K67VEft9OmV4HJJ4vOX1bijI7uvRLjh-t30EQZmx6kl6tw1C7JvGjs1z0pXzsEvOQWlywP5qEZfPOYzjAr1nAkoHqdZcRccl5J0T8uS2N6r7G5JY69Ue8viXsJC9vvhepIhS9TdnyYpbxhYAXMQJJ58qSLxXsP_x2ekCPb8X0AAKADhUsq2BV32aCKpB_EQotpBjuIV_6gICxnxmEq-jZWrV0CW84-MxiKmyJO4en_WJeMqEQToQXka2VZtbDZKwFw-1_ajlsfqcvjW7UlWNkdzTofmg3VYSgTZd245H779tWW8zX1ATC3YtZ7wvqOnckoP_yRSzu5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۱۲ مردادماه گزارش کرد که «سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه» یک پهپاد ام‌کیو۹ را در آسمان تنگه هرمز رهگیری کرده و «مورد اصابت» قرار داده است.
این خبر در حالی اعلام می‌شود که دونالد ترامپ، رئیس جمهوری آمریکا از توقف طرح یک حمله بزرگ به ایران به شرط توافق برای بازگشایی تنگه هرمز و اطمینان از دست نیافتن ایران به سلاح هسته‌ای خبر داده بود.
مرکز فرماندهی ایالات متحده (سنتکام) هنوز واکنشی به این خبر نشان نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/77718" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iO2NnLof1zuVFYCbTq4d9xo6fXj_VKDGdHAhRkk139fyM4xWJiA4botvdmKgrI-oB6hKyog5h7ksFKFkYmvausIs8Kjt5E1ZK3jSBP25nLPCd-z_5n4sUKg6D2P4EHZ6ivvSm3wbL-55ecaBIIphd2F2jr2-HIAst5HVUZyfINzI1wR4mGTX-wcmauWLJX40fTSMQ9i7Iwi3Pvrzows4hyQQYk1GO6UAy1Z1zmAzpPBPz_fpJZHW-zNEh0C4VX0Fbttt_gyGgO7V93FU1GwNCpgIM5v5w4GVG6OSVkiynI9Is_gq-oyqK_unsmSwBHcYZ70fXgMleeJgc2hA-4iG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=c86bn_yRwYKTXoBcE6_93ds0kJOa9fFkLK2N5x2Tq9pl2axysmzrTCxMhVDKpjDTJC6lsYukWJZyPFudx6WwOL7-wYa3I5aeWkWyC0sWDWY8-6SknGs0P6cyRgcTEhYJf4f-w-r9QeCIXgHAxfaaTgk4vJ0cPC5khDUQs4Qoi3c6P600A4bO_1OpszwMiQWc7oGhNPnwjObWLRGO9v6wAcwbJUso1HsIntzXTmoNdL2JttFu3usmtZvFC7Ih4iT9WBN0fz8O8fgig92a6fXzEobXuJx2J1aNds6cM-U_QhwDShpNKLwbTOG2Q8Uqz12q0VFscya4cVpT0CPuu1hjMw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30d5424a40.mp4?token=c86bn_yRwYKTXoBcE6_93ds0kJOa9fFkLK2N5x2Tq9pl2axysmzrTCxMhVDKpjDTJC6lsYukWJZyPFudx6WwOL7-wYa3I5aeWkWyC0sWDWY8-6SknGs0P6cyRgcTEhYJf4f-w-r9QeCIXgHAxfaaTgk4vJ0cPC5khDUQs4Qoi3c6P600A4bO_1OpszwMiQWc7oGhNPnwjObWLRGO9v6wAcwbJUso1HsIntzXTmoNdL2JttFu3usmtZvFC7Ih4iT9WBN0fz8O8fgig92a6fXzEobXuJx2J1aNds6cM-U_QhwDShpNKLwbTOG2Q8Uqz12q0VFscya4cVpT0CPuu1hjMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی، می‌گوید در حال حاضر مذاکره‌ای بین ایران و آمریکا در جریان نیست.
اسماعیل بقائی در نشست هفتگی خود با خبرنگاران در روز دوشنبه ۱۲ مرداد، افزود آنچه در حال حاضر در جریان است، مذاکرات دو جانبه و بین دو دولت ساحلی ایران و عمان است.
او  می‌گوید که «حضور دیگران در این مذاکرات می‌تواند سازنده یا مخرب باشد اما موضوع بین ایران و عمان است.»
اظهارات او در شرایطی بیان می‌شود که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرده که مذاکرات با ایران بعدازظهر دوشنبه ۱۲ مرداد آغاز خواهد شد.
با این حال او روز یکشنبه، هنگام بازگشت از تعطیلات آخر هفته در نیوجرسی به واشینگتن، به خبرنگاران توضیح نداد این مذاکرات در کجا برگزار می‌شود یا چه کسانی در آن شرکت خواهند کرد.
@
VahidHeadline
سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس می‌گوید در حال حاضر «هیچ بحثی» برای مذاکره با آمریکا در دستور کار قرار ندارد.
حسن قشقاوی در گفت‌و‌گویی که خبرگزاری دانشجو منتشر کرده، افزوده که حکومت ایران به‌ویژه در پرونده هسته‌ای، با واشینگتن مذاکره نمی‌کند.
او بدون اشاره به جزئیات افزود: «حتی در مسیر‌های احتمالی دیگر نیز بحث هسته‌ای مطرح نبوده و آینده این پرونده در متون مربوطه کاملاً روشن است».
این نماینده مجلس، اولویت فعلی جمهوری اسلامی را «لغو تحریم‌های اولیه و ثانویه در کنگره و بازگرداندن اموال بلوکه‌شده ایران» عنوان کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77716" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77715">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I45T-hD2HNDiEPzLqxLeyZQZgjTST1neulqCoA6B3Tvm0GUOo71KCeJwgeAy4xNjOjkdP9_0X0x1GCkHYp9E1K-OpfEgjbKnD0PCGGA-5YprwyAOq4mstSJ5wdXXa4UxubiM2JuRsL8DTWLFzwapMZiKkhmA6VD19vE_63ecBkXFEKmB2Z5incqu9W_N9F9R_WbYp2RG3l9CbzdHO6qNnew6TtWdducL4cn5XFKXBWQ2ZJudPHot6mrGdvriwf8rReqDjk9G5FHdUalJ7b7Ia2RWXIcIwAyC2TDRNX1x5YHxI1t4fLZFCnyF59DIdqqhwW_8MA6NsjvYECqcpsi1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر جنگ آمریکا، روز یکشنبه ۱۲ مردا گفت نیروهای این کشور همچنان در آماده‌باش هستند و آمادگی اقدام دارند؛ اظهاراتی که نشان می‌دهد تصمیم دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به‌تعویق انداختن حمله به ایران، تأثیری بر آمادگی نظامی نگذاشته است.
پیت هگست در شبکه اجتماعی ایکس و در کنار انتشار ویدئویی از رئیس‌جمهوری آمریکا نوشت: «وزارت جنگ آماده اقدام بود و همچنان در سطحی که از زمان جنگ جهانی دوم دیده نشده، آماده است.» هگست سپس گفت ارتش «کاملاً مسلح و آماده شلیک» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77715" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxBIkFhzIwFi-RNNWbElCtk0Swm93wOmQ3PxpBCcauONxEEb37Feo4EJi2CjXntPofuLuEeBgjF6-HPPckjNtLakGCiYB-VQpDnJvLRiy4hHSowyN-ITNu86-prFDe_3awvjgOX5FXaKinlBeifgvivObExMUS_O3yr5_G0OCxIHLSAxUegnrk7qRiRj1Hrbu1J0CMzIFU8favkdixTgpSOQB015haqIEgHEUDwE4AmZBuThqlqulW4EO-JAb_-UmA4NZUeQeRjhAdv_5NhRfPwisgszvs1m9-WmtPU6QDvf_fhZtQBLjhJ4yOm50GgbfLLkQBOa6y3ZfcS13NYQTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
خبرگزاری فارس از کشف یک خط لوله ۹۰۰ متری غیرمجاز انتقال نفت در استان بوشهر خبر داده و نوشته این لوله نفت سرقت شده را به مخزنی زیرزمینی منتقل می‌کرده است.
به گزارش فارس، فرماندۀ انتظامی استان بوشهر گفته است: «انشعابی با لولۀ ۴۲ اینچی به طول ۹۰۰ متر، و مخزن زیرزمینی ذخیرۀ نفت در شهرستان دشتی استان بوشهر شناسایی» شده است.
این مقام محلی به فارس گفت که «تاکنون بیش از ۵۰ هزار لیتر نفت خام به ارزش ۵۰ میلیارد ریال کشف و تجهیزات» مرتبط با این خط لوله غیرمجاز توقیف شده است.
در این گزارش به مشخصات فرد یا گروهی که در احداث و بهره‌برداری از این خط لوله غیرمجاز نقش داشته‌اند اشاره‌ای نشده است و معلوم نیست آیا آنها شناسایی و تحت تعقیب قرار گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/77714" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro7HAClJbOlfvUc2XW1qSu6gzfmZyD8TI7bYM7alTQZXBqWngR1WlVialzFesq4Jvp0ODPiIxSbNbVOGArgCRVvA1QT79lJF_oRBqDsk6vRuBrUJOXIdAFxR_T8MYFQGiuJI-GxT25sM5qiAUpPd_8HCWHdtl9tAuOd6gzXMXN9m8yV3dneOkYYs7vt-IRh4yMZidd9NrHsAVMQbpBbU5hHqi41OtTCfZhm1rcGLYr93MSzRJv1MOJCUsZ29Y1rmC8KoEwrnHkc0WbFiBf8XH6w9i9YHlDb4odWlChDQZ7kG5qN3nR2UhTStheOSOaoaHT4SlxjuvykjrcwH6SXOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت جهانی نفت دوشنبه ۱۲مرداد۱۴۰۵ پس از اعلام «دونالد ترامپ» مبنی بر توقف حمله نظامی آمریکا به ایران و آغاز دور تازه مذاکرات میان دو کشور، بیش از پنج درصد کاهش یافت.
خبرگزاری «رویترز» گزارش داده که بازارهای جهانی، کاهش احتمال درگیری نظامی در خاورمیانه و افزایش امید به دستیابی به توافق میان تهران و واشنگتن را مهم‌ترین عامل افت قیمت نفت می‌دانند. به نوشته این خبرگزاری، نگرانی معامله گران از اختلال در عرضه نفت و بسته شدن احتمالی تنگه هرمز، پس از اظهارات ترامپ کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77713" target="_blank">📅 17:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pFckgWHu0bBLvY1TKnMO8XloksWhmL_3l2rK4MpOfUqKI87c_puTOI6IU9khOgHnZn0ziRsSEhzdsB-7RfLx3aYmQwUFde7hIYqPFgUfWNdyF1tk2f5I4x8keAq-6VaeHOmsmKHj7TwvfM3rewkOmjMA8h0zPWCo3ihsYL5_vghaeIDVjmTRjIvvRY_YgXZyGbPCa7gYCiVzlb_MTayqvwvEQAQIndh0xj9k7iilt11J5vkIq3wMhbP_UOpj1pheWTOOpXJ9ijGCWJPCxpxJ38NMUXtz_yZZ9l5i8jBF7qnf4pv02UgFFpq4wMsWh5KkTrTrVwtDTqUXsQs5pTqRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری «میزان» رسانه وابسته به قوه قضاییه جمهوری اسلامی از اعدام دو زندانی به نام‌های «امید بهزاد» و «پوریا صفوت» به اتهام «جاسوسی» و «همکاری اطلاعاتی» با اسراییل از طریق «ارسال تصاویر مراکز امنیتی و نظامی» جمهوری اسلامی خبر داد.
خبرگزاری میزان، ارگان رسمی قوه قضاییه، اعلام کرد این دو زندانی بامداد دوشنبه ۱۲مرداد اعدام شدند.
به ادعای این نهاد، «بررسی‌های فنی» انجام‌شده روی تلفن همراه امید بهزاد این موارد را تایید کرده و او نیز «در جریان تحقیقات» به آنها اعتراف کرده بود. با این حال، مشخص نیست این اعترافات در چه شرایطی از او گرفته شده است. جمهوری اسلامی طی بیش از ۴ دهه حکومت خود، بارها اقدام به اخذ اعترافات اجباری کرده است.
در گزارش میزان، پوریا صفوت نیز بدون ارائه هیچ‌گونه سند یا جزییاتی، به همکاری «مستقیم با موساد» متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77712" target="_blank">📅 17:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=hZdjvk0ql9iS3lFNdJDhivs3ehk8QlchZSQS3MdqLPrEIW9kkqnKZ2PFVNUtjWbFx1qy-sgcSle_Tfgu4VmRL-idqWPqylUn9WQKGJxWsMnWXzeF2NRgh0Qd-j0FiBAEc0G2iU7eWygNU1F1Ya5QrCmxPdH-N_YqJwJDguQIGXu4XHshy3RQu0OsTchBEDoSFydXypqFw3QeeKk78hCZisF9z9XZkoBo8UF15eAYrdYtND9Kl07X8Vgd6YnWAztxtCYy2fUHxHPOtmd7urz3nsyUiE_rlLH8E0RibQVIDU8hD2OAjfdWPhEncrdJ6_-7fy-EceLroQgkftlK2vKOS2-fI2X5SFhJOfwpPd7Og-3CVzhQRdBjtkGj9H4ZD_p01QuRloXWTmkiY2Pv1JDkE9TkqCxCncG5ZwgSXKd2ns2fjfzUkiJrjd7ro7gBoBy5CcdkPHFWy4VoBQmJ9QpztslpyGM18UOyybMzLExaKj0oeeX2S-5MNjdD6EZCB1pmFBEpDVxln4pvV0Jjd0WkuJKUaToyFFgB9-cpOFU8U4PorMzjE-eV05jJ7V-ttzBiP2ZHq3FHd0zIHNbHXEPWNs6VFIhXSemaehqk3e4KHrjsEkmUyRTYVseNPRQQ8XXKcAWQguvrlC55vS75oVqG9mKsazIdcfA5kYknqjBE7io" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e5fb7b499d.mp4?token=hZdjvk0ql9iS3lFNdJDhivs3ehk8QlchZSQS3MdqLPrEIW9kkqnKZ2PFVNUtjWbFx1qy-sgcSle_Tfgu4VmRL-idqWPqylUn9WQKGJxWsMnWXzeF2NRgh0Qd-j0FiBAEc0G2iU7eWygNU1F1Ya5QrCmxPdH-N_YqJwJDguQIGXu4XHshy3RQu0OsTchBEDoSFydXypqFw3QeeKk78hCZisF9z9XZkoBo8UF15eAYrdYtND9Kl07X8Vgd6YnWAztxtCYy2fUHxHPOtmd7urz3nsyUiE_rlLH8E0RibQVIDU8hD2OAjfdWPhEncrdJ6_-7fy-EceLroQgkftlK2vKOS2-fI2X5SFhJOfwpPd7Og-3CVzhQRdBjtkGj9H4ZD_p01QuRloXWTmkiY2Pv1JDkE9TkqCxCncG5ZwgSXKd2ns2fjfzUkiJrjd7ro7gBoBy5CcdkPHFWy4VoBQmJ9QpztslpyGM18UOyybMzLExaKj0oeeX2S-5MNjdD6EZCB1pmFBEpDVxln4pvV0Jjd0WkuJKUaToyFFgB9-cpOFU8U4PorMzjE-eV05jJ7V-ttzBiP2ZHq3FHd0zIHNbHXEPWNs6VFIhXSemaehqk3e4KHrjsEkmUyRTYVseNPRQQ8XXKcAWQguvrlC55vS75oVqG9mKsazIdcfA5kYknqjBE7io" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، می‌گوید که «مذاکرات جدید» با ایران روز دوشنبه آغاز می‌شود.
آقای ترامپ گفت که در حال حاضر توافقی درباره تنگه هرمز وجود دارد و توافقی هم درباره هسته‌ای زدایی ایران حاصل خواهد شد.
@
VahidHeadline
گفت‌وگوی ترامپ با خبرنگاران در هواپیما
تشخیص و ترجمه ماشین:
🔺
خبرنگار:
چه چیزی باعث شد حملات دیشب را لغو کنید؟
🔻
ترامپ:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند این کار را انجام دهم.
ما تقریباً همین موقع کاملاً آماده اجرای عملیات بودیم و قرار بود حمله‌ای عظیم باشد. همه‌چیز برای اجرا آماده بود. اما وقتی متحدان می‌خواهند حمله را لغو کنید، ناچارید بگویید: «خب، ببینیم چه می‌شود.»
دلیل درخواستشان این است که فکر می‌کنند توافقی وجود دارد. توافقی دربارهٔ [واژه نامفهوم] وجود دارد و بعد هم توافقی درباره موضوع هسته‌ای حاصل خواهد شد؛ یا می‌توانید آن را «هسته‌ای‌زدایی از ایران» بنامید. من آن را هسته‌ای‌زدایی از ایران می‌نامم.
فعلاً آن را متوقف نگه داشته‌ایم. فقط باید ببینیم چه می‌شود. هر زمان بخواهیم می‌توانیم آن را انجام دهیم.
اما سه طرف اصلی از ما درخواست کردند. ایران هم با تأکید زیادی از ما درخواست کرد. گفتند: «مایلیم توافق کنیم.»
حالا نمی‌دانم بیرون چه می‌گویند، چون خیلی وقت‌ها این را به من می‌گویند و بعد بیرون می‌روند و می‌گویند: «نمی‌دانیم او درباره چه حرف می‌زند.»
بدیهی است که نمی‌خواهند مورد حمله قرار بگیرند. آن‌ها از وسعت حمله خبر داشتند، چون [عبارت پایانی نامفهوم است].
🔺
خبرنگار:
حالا چه اتفاقی می‌افتد؟
🔻
ترامپ:
کاری که اکنون انجام می‌دهیم این است که در قالب مذاکره با آن‌ها گفت‌وگو می‌کنیم. مذاکرات فردا بعدازظهر آغاز می‌شود و خواهیم دید آیا واقعیت دارد یا نه.
خیلی دوست دارم این اتفاق بیفتد. جان‌های زیادی نجات پیدا می‌کند و [ادامه جمله نامفهوم است].
سال‌های بسیار زیادی طول می‌کشید تا بتوانند آن را دوباره بسازند؛ البته اگر اصلاً امکان بازسازی‌اش وجود داشت. فکر نمی‌کنم حتی قابل بازسازی می‌بود.
حمله‌ای آماده کرده بودیم که اگر انجام می‌شد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
برای آن‌ها فاجعه‌بار می‌شد و نمی‌خواستند ما آن را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم آن را نمی‌خواست. آن‌ها فکر می‌کردند توافقی قریب‌الوقوع است.
🔺
خبرنگار:
آیا ضرب‌الاجلی وجود دارد، قربان؟
🔻
ترامپ:
توافقی قریب‌الوقوع است که به [واژه نامفهوم] و در نهایت به هسته‌ای‌زدایی از ایران مربوط می‌شود.
وقتی این را می‌شنوم، می‌گویم: «آیا می‌خواهیم تا این اندازه شدید عمل کنیم؟»
گروهی از مردم هستند که می‌خواهند من فوراً این کار را انجام دهم و گروه دیگری از مردم هم هستند که نمی‌خواهند من این کار را انجام دهم.
🔺
خبرنگار:
آقای رئیس‌جمهور، آیا ایران برای رسیدن به توافق ضرب‌الاجلی دارد؟
🔻
ترامپ:
باید ببینیم. ببینیم اوضاع چگونه پیش می‌رود. هر زمان بخواهیم آماده‌ایم وارد عمل شویم.
آیا ترجیح می‌دهم توافق کنم؟ من در پی کشتن مردم نیستم، چون مردم کشته می‌شوند؛ تعداد زیادی از مردم کشته می‌شوند و ما این را نمی‌خواهیم.
بنابراین آن‌ها از ما درخواست کردند؛ مشخصاً ایران. اما آن سه طرف دیگر هم گفتند که واقعاً...
از آن‌ها پرسیدم. [اشاره نامشخصی به پادشاه و سپس ولیعهد.] گفتم: «ترجیح می‌دهید چه کار کنیم؟ ترجیح می‌دهید ما این کار را انجام دهیم یا نه؟»
گفتند: «ما توافق را بسیار بیشتر از حمله ترجیح می‌دهیم، چون نمی‌دانید این [واژه نامفهوم؛ احتمالاً اشاره به حملات یا اقدامات] به کجا منتهی می‌شود.»
آیا کشورشان با ورود سیل‌آسای مردم و فاجعه روبه‌رو خواهد شد؟ اتفاق‌های بد زیادی ممکن است رخ دهد.
🔺
خبرنگار:
قربان، گزارشی منتشر شده است که می‌گوید نیروهای آمریکایی را از بحرین و کویت خارج می‌کنید. آیا نیروها از خاورمیانه خارج می‌شوند؟
[در ترنسکریپت هیچ پاسخی از ترامپ به این پرسش ثبت نشده است.]
....
🔺
خبرنگار:
بازگردیم به ایران؛ آیا آماده بودید اهداف انرژی را هدف حمله قرار دهید؟
🔻
ترامپ:
نمی‌خواهم این را بگویم. نمی‌توانم این را بگویم.
قرار بود حمله‌ای عظیم باشد. قرار بود حمله‌ای باشد که با فاصله بسیار زیاد، بزرگ‌ترین حمله از زمان جنگ جهانی دوم می‌بود.
اما از ما خواستند آن را انجام ندهیم. گفتند: «لطفاً این کار را نکنید.»
همسایگانشان هم همین را گفتند.
بنابراین فقط می‌خواهیم ببینیم آیا می‌توانیم درباره هسته‌ای‌زدایی به توافق برسیم یا نه.
🔺
خبرنگار:
[پرسش ناقص درباره اینکه مذاکرات فردا انجام می‌شود.]
🔻
ترامپ:
بله.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/77711" target="_blank">📅 01:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77710">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4oMLUf8An_ZVEyw_j3kL6rSqrsHthktAm5jM0Xg7SWo4ubeswn11M3UjYr3EhNQxHdEomI_BPXYpqZcATAbziK-acpEzpL0y2eciRMVc6e_FFnW4PeB4ql9v5MEJFFh4xN7BWf_X_JDa1JKsufTM1QtoghjIxyq_YHjHOZHTfrhxffkSZV2egSTrZrL2PTSrhQlS_0jP5uCn_SSaTa2qfzkvPyHJEulWlaI93muMMTCKo2jigM39Jx2fKDbBS0H52fwsWMLkxeqzRqUInaRlwW2Cwv-xmv-Dr2u1rXmfQ6iUqU553kdaalM2FjgNsRgrCWXDvxXLNwJocixhXrmwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رییس‌جمهوری ایران، در پیامی یادداشت تفاهم امضا شده میان تهران و واشنگتن را «حاصل خرد جمعی اعضای شعام» توصیف کرد و نوشت: «باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند.»
پزشکیان روز یکشنبه ۱۱ مرداد در شبکه اجتماعی ایکس نوشت: «تفاهم‌نامه‌ای که امضا شد حاصل خرد جمعی اعضای شعام بود و همه اعضا با آن همدل‌اند. باور دارم این تفاهم‌نامه مرکز ثقل روابط خارجی ما در آینده خواهد بود. باید بکوشیم دشمن را وادار کنیم به آنچه امضا کرده پایبند بماند. امنیت کشور، منطقه و هم‌پیمانان ما با این تفاهم‌نامه ارتقا می‌یابد.»
همزمان، کانال ۱۲ اسراییل به نقل از منابع آگاه گزارش داد کشورهای منطقه در حال میانجیگری برای بازگرداندن آمریکا و ایران به یادداشت تفاهمی هستند که ماه گذشته میان دو طرف امضا شد.
بر اساس این گزارش، توافق پیشنهادی شامل باز ماندن تنگه هرمز به مدت ۶۰ روز بدون دریافت عوارض و تمدید آتش‌بس میان تهران و واشینگتن است. کانال ۱۲ گزارش داد یادداشت تفاهم پیشین به دلیل اختلاف بر سر نحوه مدیریت تنگه هرمز از هم پاشید؛ به گونه‌ای که دونالد ترامپ بر باز بودن کامل این آبراه تاکید داشت، در حالی که تهران معتقد بود این توافق به جمهوری اسلامی اجازه می‌دهد مسیر عبور کشتی‌ها را تعیین کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/77710" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراقچی: مذاکرات ایران و عمان درباره تنگه هرمز به مراحل پایانی رسیده است
🔸
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یکشنبه خبر داد که مذاکرات با عمان درباره تنگه هرمز به «مراحل پایانی» رسیده است.
🔸
به گزارش خبرگزاری رسمی دولت ایران، ایرنا، عراقچی در جلسه هیئت دولت از وضعیت این گفت‌وگوها گزارشی ارائه داد و اعلام کرد که «مذاکرات در مسیر نهایی شدن قرار دارد و مراحل پایانی خود را طی می‌کند».
🔸
هفته گذشته وزارت خارجه ایران گفته بود که مذاکره میان تهران و مسقط همچنان ادامه دارد. این در حالی است که کاظم‌غریب‌آبادی، معاون عباس عراقچی، سه‌شنبه همان هفته اعلام کرد که جمهوری اسلامی پیشنهاد عمان مبنی بر تقسیم برابر مسیرهای عبور و مرور میان دو کشور در تنگه هرمز را رد کرده است.
🔸
پیش از آن، خبرگزاری رویترز پیش‌تر به نقل از یک منبع آگاه گزارش داد که عمان پیشنهادی برای ایجاد یک سازوکار مشترک منطقه‌ای با پرداخت داوطلبانه عوارض یا هزینه‌ عبور و مرور برای مدیریت تنگه هرمز به ایران ارائه کرده است.
🔸
همزمان با انتشار اظهارات روز یکشنبه عراقچی، سخنگوی وزارت خارجه در گفت‌‌وگو با تلویزیونی حکومتی ایران مدعی شد که مذاکره بین ایران و عمان دربارۀ تنگه هرمز «ربطی به باز یا بسته‌شدن تنگه هرمز ندارد».
🔸
اسماعیل بقائی همچنین گفت که مدیریت آینده تنگه هرمز با ایران است و با مشورت عمان انجام می‌شود.
🔸
این مواضع در حالی مطرح شده که دونالد ترامپ، رئیس‌جمهور آمریکا، بامداد یکشنبه اعلام کرد طرح جدید برای حمله به ایران را با درخواست جمهوری اسلامی و کشورهای خاورمیانه و برای تکمیل توافقی که به بازگشایی «فوری، کامل و تمام‌عیار» تنگه هرمز و «پایان تهدید هسته‌ای ایران» منجر شود، متوقف کرده است.
🔸
رسانه‌های ایران به نقل از منابع آگاه حکومتی درخواست از آمریکا برای توقف طرح حمله را رد کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77709" target="_blank">📅 23:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tBQ41_5MWn-N11ymDItBXvwcPc7YRykSab3von-RZdZmLzqA8QmoPE9ahJSQUGOaH-tUo0ZTgDGrGCbhYlmMhlUsCHhmgWPrjszp1vhPIAzHx0IBHbyU92aY5sL0RG4DsFA4xIML41YX5S7jcpTK8Lvk0FkUUjaafhAoql_0YW8yQ_8OkUHVhDDul-rZjskYH5bO-tEBQMsRJJuwSdLZEDlMWhY1lUrDY4XfRFvzlsVo2ax6pXnws7mWmo2xnGXlhI2Vd9uNNU57e_LefzK9UnTH2kuUrrzcK1kcsvO26RomE_rrPWAAgjBajPgEqtFQbnUj9mcK2OmjRma30QU3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MOlPLCkWZhRZ3PvOHcUt12o7n_LcfO35TSaDzOWnwYojY8Rs79oUl9eyfmrbPJrYoS8DcuymDURsgYlLV2Utud_52mzePx0PGKWLTtfJobRkhUaBBmKaZE8ad-JECui54KyxX5AafNAHTcmTewn5H6RtmG7KAMa7raSeb1OtojsW2MZd9sjE6c4A-0OSkKq1lFLjDJiGP6JuRuMGDKJTld7Xtqiqdxt2949WJ92iz1L16SurGy416pQvE12QZ68IB5pGIx-Ju1fpbQvALu4OeQS0svY3Rt2NpPLmx_5TODl8kUk9SkG63UIP-_rxzmnv897eonRrA-bwSyfLG4D_ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل یک‌شنبه ۱۱ مرداد گزارش داد عباس عراقچی، وزیر خارجه جمهوری اسلامی، شب گذشته با پیشنهاد مصالحه‌ای که میانجی‌های قطری و آمریکا درباره سازوکار بازگشایی تنگه هرمز تدوین کرده بودند، موافقت کرده است.
این شبکه به نقل از دو دیپلمات آگاه از جزئیات مذاکرات گزارش داد پاسخ مثبت عراقچی یکی از دلایلی بود که دونالد ترامپ، رییس‌جمهوری آمریکا، با لغو حمله به ایران موافقت کرد.
@
VahidOOnLine
خبرگزاری فارس به نقل از دو «منبع آگاه» گزارش کانال ۱۲ اسرائیل درباره موافقت عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، با طرح بازگشایی تنگۀ هرمز را تکذیب کرد.
یک منبع نزدیک به تیم مذاکره‌کننده هسته‌ای ایران به این خبرگزاری گفت هیچ توافقی درباره بازگشایی تنگۀ هرمز حاصل نشده و اخبار منتشرشده در این زمینه «کذب» است.
فارس همچنین به نقل از یک منبع نظامی نوشت تا زمانی که «اقدامات خصمانه آمریکا» ادامه داشته باشد، تنگۀ هرمز مسدود خواهد ماند و عبور شناورها تنها از مسیر اعلام‌شده و با مجوز نیروی دریایی سپاه پاسداران امکان‌پذیر است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77707" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77706">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O-nbaNvNg65UshvAsbLnR_uGVxElerFJFyOAX-yYNEg2RQY4cKQtS3Bv35Gx7ebrZ4W3kkkOl-N-cDRPkuxw2eySt6lPCzW-mkZyK29b_SNNvs5s6bO54rSH3aUSl3YgHGxnSRzYyO3LeKQcHZc46eDznR1LZT0NKnDnftzu9dPvBc55_78FXsNWytHzOtvJhq4j3lPwbcr-EDAL0XKrSeN02f7FdoQ2tTfvC1jA1A-cfSfixXLiT8PXrE8bzmgl9CKl0cLuczmM8_LkNGG_JjzC5x2T4SQ9jeZTrgFP-qrVowGgJiYPLFcqfuHWoGhBAON5F0mctwAyWY1vlMHqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در مصاحبه‌ای با فاکس نیوز که لارا ترامپ، عروس رئیس‌جمهور آمریکا، انجام داد، گفت حتی اگر در تهران به‌طور رسمی «تغییر رژیم» رخ ندهد، حکومت ایران «باید» روش خود را تغییر دهد.
وقتی از روبیو پرسیده شد آیا واشینگتن می‌تواند بدون تغییر رژیم در تهران، ایران را «هسته‌ای‌زدایی» کند، او گفت:
«فکر می‌کنم آنچه باید رخ دهد این است که حکومت باید تغییر کند. ممکن است تغییر رژیم نداشته باشید، اما حکومت باید تغییر کند.»
او افزود: «حکومت ایران به‌طور سنتی رویکردی توسعه‌طلبانه در خارج از مرزهایش داشته است. در اصل، دیدگاه آنها این است که نمی‌خواهند فقط بر ایران حکومت کنند؛ می‌خواهند بر منطقه حکومت کنند. آنها می‌خواهند انقلاب را صادر کنند.»
روبیو ادامه داد: «این رویکرد باید تغییر کند و تنها راه تغییر دادن آن این است که هزینه‌اش را آن‌قدر برایشان بالا ببرید که دیگر قادر به پرداخت آن نباشند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 446K · <a href="https://t.me/VahidOnline/77706" target="_blank">📅 17:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=L8OMtorICsOXJr9d7pOfmzCaNKyVPfl_YYgEt0qwwT1tjN7bXBWULjMnI7ahBytvIltzZBgenylRQ4Nku_prh7jRGqKra5t4asLafueI9HSsEajGBKnK8jaz7p5J0xu3woP8wNQaoYc0WcJLZX_RLrwfyPKNV3T5_b3NG524-dXcEQF7kcGxnrrNjpPhJPu9t24CHf5fktEo-T-BZgNBl_5lhFoSe_KCf-HSMLcE6kIUoPvByXVVUMSyWOXzV--gfVWWvlhKqp4byo6_vrcxGx1vWBbBGWrmqEDTNsHbkD8scjNUQC_ixcIFopMumAFxfWaSIejj4jZaOiiuUntiBw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3938f205b4.mp4?token=L8OMtorICsOXJr9d7pOfmzCaNKyVPfl_YYgEt0qwwT1tjN7bXBWULjMnI7ahBytvIltzZBgenylRQ4Nku_prh7jRGqKra5t4asLafueI9HSsEajGBKnK8jaz7p5J0xu3woP8wNQaoYc0WcJLZX_RLrwfyPKNV3T5_b3NG524-dXcEQF7kcGxnrrNjpPhJPu9t24CHf5fktEo-T-BZgNBl_5lhFoSe_KCf-HSMLcE6kIUoPvByXVVUMSyWOXzV--gfVWWvlhKqp4byo6_vrcxGx1vWBbBGWrmqEDTNsHbkD8scjNUQC_ixcIFopMumAFxfWaSIejj4jZaOiiuUntiBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوهای منتشر شده در رسانه‌های اجتماعی نشان می‌دهد بامداد روز یک‌شنبه ۱۱مرداد۱۴۰۵ پیکر آروین خیرخواهان معترضی که در جریان اعتراضات دی‌ماه۱۴۰۴ بازداشت و ۱۰مرداد در شاهرود اعدام شد به خاک سپرده شده است.
خاکسپاری در سکوت و تنها با حضور اعضای نزدیک خانواده او انجام شده است.
بازداشت، محاکمه، صدور حکم و اجرای آن برای این شهروند معترض ۲۰ساله در سکوت خبری رخ داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77704" target="_blank">📅 17:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77702">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNhf4Y1x2iCM1hSUzL0lzycd04oFDFXc_vod0eA4OwgV2DSMy8YhsuSn9suOvPTDC22pPdKxYQ5b4YQX5K9TXNo2HB1y_F9QKfUEUMGOG-EXmvg4DJnY4KFTH01EJ9WGe4mwmLDmRubMzlNSe6vvbfmhoSY_V6tOhA7lPuKzlV41BDiC2-wijBP3NsLgLXHOw5c5x9wI9OCktp7tUJrxHIlF23HpNpGyNxg8iFBJ_sInhIx4_fpMjRIRpmTUWMsCKKLAm1w-O-vWc1CvSMJI3dgnTLwvPog_BQBb43hS3PcL3dt7a8l9XRQHdWZyLQ9tPOKeCKzOToFwHl7D-uVPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به درخواست ایران و کشورهای منطقه، حمله را برای فراهم شدن زمینه توافق، متوقف کردم
ترجمه ماشین:
ایالات متحده کاملاً مسلح و آماده است تا با جمهوری اسلامی ایران مقابله کند؛ با سطحی از رعب نظامی، توان و قدرت که از زمان جنگ جهانی دوم تاکنون دیده نشده است.
با وجود این، ایران و دیگر کشورهای خاورمیانه همین حالا از ما خواسته‌اند که از هرگونه حمله دست نگه داریم، زیرا بر سر چارچوب‌های یک توافق تفاهم حاصل شده است.
این توافق شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
بر اساس این درخواست، برای منافع آینده جهان و همچنین بقای ایرانی موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانیم به‌سرعت به یک توافق دست پیدا کنیم.
کشور اسرائیل نیز در این تعهد با من همراه است.
همه دست‌به‌کار شوید و کار را تمام کنید. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
The U.S.A. is locked and loaded and ready to go against the Islamic Republic of Iran, at levels of Military Terror, Strength, and Power not seen since World War II. Despite this, we have just been asked by Iran, and other Middle Eastern Countries, to hold off any attack in that the perimeters of a deal has been agreed to. This would include the Immediate, Complete, and Total OPENING OF THE HORMUZ STRAIT, and an end to Iran’s  nuclear threat. Based on this request, I have agreed, for the future benefit of the WORLD and, likewise, the survival of a successful and prosperous Iran, to cancel the attack, subject to being able to rapidly make a DEAL. The Country of Israel joins me in this commitment. Get to work, everybody, and get it DONE. Thank you for your attention to this matter! President DONALD J. TRUMP
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 544K · <a href="https://t.me/VahidOnline/77702" target="_blank">📅 05:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77701">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vcF86pvUwXshgbUeCujctw6ixsvIbfEO8wKkmPwLJaDJ3lRSBOFlLZN_7GzSiGkI7vO7S2fotA152GcOAk1Wc90XDGHXokZgss2oToQ8vlNUHOm5iecZVhLK7hBEHAWMXCW0rQ2yZsMdViI4bOBWRB8LcV-ITcCLPDuAqpnIi8DiYuvB7fRpgLHaiB7dskVT8GT02m4YE_5hKhuUX6oOSyI9TReQzRL4Vsa1naUaQWQK7HERdC5qzseeifVRP4yY9qhQ6XcUaSvCgMHpJhaTjLwCzMnjWtNH0pgVsooqoVjn-g8gRYDyNcPnm4BNgTask9yVNFvE2VUArK2zduSo8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد بن سلمان درباره برنامه‌های ترامپ برای حملات گسترده به ایران ابراز نگرانی کرد
اختصاصی
اکسیوس، ترجمه ماشین:
محمد بن سلمان، ولیعهد عربستان سعودی، روز شنبه با دونالد ترامپ، رئیس‌جمهور آمریکا، گفت‌وگو کرد و درباره برنامه‌های او برای حملات گسترده جدید علیه ایران ابراز نگرانی کرد.
این خبر را دو مقام آمریکایی و یک منبع دیگر مطلع از این تماس اعلام کردند.
چرا اهمیت دارد:
ترامپ در واکنش به حمله موشکی ایران به یک پایگاه آمریکا در اردن و ادامه اختلال ایران در کشتیرانی از طریق تنگه هرمز، به‌طور جدی حمله به اهداف انرژی ایران در روزهای آینده را بررسی می‌کند. او هنوز دستور نهایی را صادر نکرده است.
تصویر کلی:
چنین حمله‌ای ممکن است به تشدید بی‌سابقه جنگ پنج‌ماهه منجر شود؛ جنگی که با باز کردن راه مذاکرات از سوی ترامپ بارها متوقف شده، اما پس از شکست این تلاش‌های دیپلماتیک دوباره از سر گرفته شده است.
جزئیات:
ایران تهدید کرده است که با انجام حملاتی علیه تأسیسات انرژی و زیرساختی در اسرائیل و کشورهای خلیج فارس تلافی خواهد کرد.
▪️
یک مقام آمریکایی به آکسیوس گفت: «سعودی‌ها ابراز نگرانی کردند و خواستار شفاف‌سازی درباره برنامه عملیاتی شدند.»
▪️
یک منبع دیگر مطلع از این تماس گفت محمد بن سلمان از ترامپ خواست تنش‌ها را کاهش دهد و از انجام این حملات خودداری کند.
▪️
کاخ سفید و سفارت عربستان سعودی در واشنگتن از اظهارنظر خودداری کردند.
مرور سریع:
ترامپ روز چهارشنبه با شاهزاده خالد بن سلمان، وزیر دفاع عربستان سعودی که با نام اختصاری «کی‌بی‌اس» شناخته می‌شود، دیدار کرد.
▪️
یک منبع مطلع گفت این دیدار پس از آن به برنامه سفر وزیر سعودی افزوده شد که او با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، دیدار کرد و به او گفت عربستان سعودی خواهان کاهش تنش با ایران است.
▪️
این پیام با وجود حمله مشترک این هفته آمریکا و عربستان سعودی به شبه‌نظامیان طرفدار ایران در عراق منتقل شد.
▪️
این منبع گفت هدف از این دیدارها انتقال دیدگاه‌های محمد بن سلمان درباره جنگ ایران و اوضاع گسترده‌تر منطقه بود.
در پس ماجرا:
عربستان سعودی یکی از مهم‌ترین متحدان واشنگتن در منطقه است. ریاض، با وجود دوره‌هایی از تنش طی پنج ماه گذشته، از زمان آغاز جنگ در چند مقطع حساس بر سیاست ترامپ در قبال ایران تأثیر گذاشته است.
عامل خبرساز:
دیگر قدرت‌های منطقه‌ای، از جمله قطر، امارات متحده عربی، ترکیه و پاکستان نیز آمریکا و ایران را برای کاهش تنش تحت فشار قرار داده‌اند.
▪️
عباس عراقچی، وزیر امور خارجه ایران، روز شنبه با فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان، که نقش میانجی مهمی میان واشنگتن و تهران داشته است، گفت‌وگو کرد.
▪️
عراقچی همچنین درباره احتمال حملات آمریکا با وزیران امور خارجه ترکیه و عربستان سعودی گفت‌وگو کرد.
▪️
عراقچی، بنا بر بیانیه‌ای در کانال تلگرامی خود، به همتای سعودی‌اش گفت: «هرگونه اقدام خصمانه از سوی آمریکا یا اسرائیل — یا مشارکت یا همکاری کشورهای منطقه در چنین اقداماتی — با پاسخ قاطع و متناسب نیروهای مسلح قدرتمند ایران روبه‌رو خواهد شد.»
آنچه باید زیر نظر داشت:
میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی برای بازگشایی تنگه هرمز، جداگانه با عراقچی، استیو ویتکاف فرستاده کاخ سفید و مقام‌های عمانی گفت‌وگو کردند.
▪️
یک منبع مطلع از مذاکرات گفت این گفت‌وگوها پیشرفت داشته است، اما هنوز مشخص نیست که آیا این پیشرفت برای فروکش کردن بحران کافی خواهد بود یا نه.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 492K · <a href="https://t.me/VahidOnline/77701" target="_blank">📅 03:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77700">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lQNQM4AFID_6VcTI5o0A64tV4fjeh9vBURwZfDpOv8SoNnScTJjG580scDMbeU4XOOISHRhsEE55Kcq5wHf9wadzUUaZw6ap6GrhK79P2Un0gXSzEauBz-yofl9UAT7PEjGcl7Kl2JWbG6lp9RmNOebSex2iqELF7LOqUdrpvwQBVfbL6FkjElqJgqelUzIZiTNkGse-h1S_cnwSHZyaj8uJpyfPOBjt2dGwFHIpQgwz7KskVPEQCbzGPDEFqO7x8gV9GbZWIGsZShitIfP1D4PoS5EcwtHGj1jPoHkGYNTj4OV3r0_eeT5h5i6ydQs2qulIbkYPa7jlZPHqkcqvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با افزایش تنش‌ها میان واشنگتن و تهران، «وای‌نت» روز شنبه گزارش داد، ورود و استقرار بیش از ۳۰ هواپیمای سوخت‌رسان نظامی آمریکا در فرودگاه بن‌گوریون تل‌آویو و افزوده شدن ۱۰ هواپیمای دیگر در روزهای آینده، موجب بروز اختلالات شدید، ترافیک سنگین هوایی و تاخیرهای روزافزون در پروازهای این فرودگاه شده است.
بر اساس گزارش سازمان فرودگاه‌های اسرائیل، میانگین تاخیر پروازها در ترمینال‌های مختلف به بیش از یک ساعت رسیده و دریافت بار مسافران نیز تا دو ساعت معطل شده است. وضعیتی که هم‌زمان با اوج سفرهای تابستانی و نقایص فنی اخیر در سیستم‌های کنترل ترافیک هوایی اروپا، مسئولان را نسبت به تشدید بحران و جدی‌تر شدن اختلالات در پروازهای بین‌المللی نگران کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 489K · <a href="https://t.me/VahidOnline/77700" target="_blank">📅 03:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RRlfpE66WMyrOCEFTItNfoUdcaNu0lRF71P8x4VdoiVzbtcCXFSo9A1_p5o5K44iEEobByXLB9zM820D8jUD0c6C3jRx-cFNnKXwLu-zsYk3XOfWEXJygVsnUHLlCEJNSaCzWawsNKlI5zMEVBU-VH3KRb0_ASIaoF3d9xerK8x0TuR4igVGDO-kCNOrAVxW0rEUxh8L1TsfzMpujn6hQwZwi4EOOlzdk4rqFrFdwvAgHon9hFnhby67P0W29B5H4Epz-IKi79qLElVJeP7xma3Q_3hV14Zomth_LsHsEBMTPZQ0GIo4T-vVrlMUB3N2dFr05suO79N3S4AJJNlonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر پست ترامپ:
ترامپ در حال نابود کردن ارزش پول ایران است
هم‌زمان با افزایش تنش‌ها در منطقه و انتشار گزارش‌هایی درباره احتمال از سرگیری حملات آمریکا علیه جمهوری اسلامی، دونالد ترامپ، رییس‌جمهوری آمریکا، تصویری را در تروث سوشال
منتشر کرد
که به کاهش ارزش ریال و افزایش تورم در ایران اشاره دارد.
در این تصویر با عنوان «ترامپ در حال نابود کردن ارزش پول ایران است» نوشته است که ایران با تورم شدید روبه‌رو است و ارزش هر دلار از حدود ۹۰ هزار تومان به ۱۹۰ هزار تومان افزایش یافته است.
ترامپ توضیح یا اظهارنظر دیگری درباره این تصویر منتشر نکرد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه شنبه دهم مرداد ماه، تصاویر ساخته با هوش مصنوعی را در شبکه تروث سوشال منتشر کرد که او را در لباس رزم جنگ استقلال آمریکا نشان می‌دهد. در مطلب دیگری، تصویری از ناوگان دریایی غرق شده جمهوری اسلامی در زمان ریاست جمهوری او دیده می‌شود.
در یکی از این تصاویر ساختگی، ترامپ با پوشیدن لباس فرماندهان جنگ استقلال آمریکا و در میان دود و آتش نبرد به تصویر کشیده شده است. در تصویری دیگر تحت عنوان «۱۵۹ کشتی ایرانی»، شناورهای نظامی ایران در دوره رییسان جمهوری سابق آمریکا روی آب نشان داده شده‌اند، در حالی که در به دوره ترامپ، تمامی این شناورها در قعر دریا غرق  شده‌اند.
این تصاویر در حالی منتشر می‌شوند که رسانه‌های مختلف از جمله
شبکه ۱۲ تلویزیون اسرائیل
از احتمال حمله گسترده ارتش آمریکا به ایران خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 563K · <a href="https://t.me/VahidOnline/77699" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-g-RXg7fRI33R1PD31dJDvlYssJ-OhH3lJrOLAphrUQRuN-6yZIR2aJSbVjD_EeR1Bm8yLeps4fy4lHzhoBHQtHHDYnGosY228BAW4BmfpNt3zpfYY1xNzFrS6nFGsPC--sNbh81jAgNtWLnO-bcf9HPSHxVTZFntbReUSv9nKM5-j9Rc6ycuGkpVAmP8am0XW9y150X3xM0b1hJSE0iUICZI21XOIYrGspN_Tq6GuW3l6ClVm2p-FC_j31Sch299PPhfLv22nTAQkqq-3aoMipezd8eliIWRqH7JKByMU5Y941fWm8287hzdj-utcsYRDiE85p16fyU78LXaPxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سحرگاه روز شنبه ۱۰ مرداد ۱۴۰۵، حکم اعدام آروین خیرخواهان، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در زندان شاهرود به اجرا درآمد. این جوان معترض، پیش‌تر از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شده بود.
به گزارش خبرگزاری هرانا، ارگان خبری مجموعه فعالان حقوق بشر در ایران، حکم اعدام آروین خیرخواهان حوالی ساعت چهار بامداد امروز اجرا شد.
یک منبع نزدیک به خانواده این زندانی با تایید این خبر به هرانا گفت که مسوولان زندان تاکنون پیکر او را به بستگانش تحویل نداده‌اند. به گفته این منبع، به خانواده اعلام شده است که ساعت سه بامداد فردا برای تحویل پیکر مراجعه کنند و مراسم خاکسپاری نیز باید ساعت پنج بامداد برگزار شود.
آروین خیرخواهان در جریان اعتراضات دی‌ماه ۱۴۰۴ بازداشت و سپس از سوی شعبه یک دادگاه انقلاب شاهرود با اتهام «محاربه» به اعدام محکوم شد. این حکم پس از اعتراض، در دادگاه تجدیدنظر و دیوان عالی کشور نیز بدون تغییر تایید شد.
تاکنون جزییات دقیقی درباره زمان و نحوه بازداشت، مصادیق اتهامی، روند بازجویی، دسترسی این زندانی به وکیل انتخابی و مستندات مورد استناد دادگاه برای صدور حکم اعدام منتشر نشده است.
هرانا نوشته است، آروین خیرخواهان هنگام اجرای حکم اعدام ۱۹ سال و شش ماه سن داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 576K · <a href="https://t.me/VahidOnline/77698" target="_blank">📅 18:13 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=qAEYGSJ6XnLLZvMD8stpZnVggnJ4Ut8-vhb8G-NK-mrXKdiBZlDxhUFlUmhDwqGSynBb_gTUWGDwJca2kHEnoBd-rYEDBGfz8BVOLa83d-QCA_MDZBQtk_MLxPVqcmz09rL23o4M32RVBJE99mvZGUTgCEuBXJa3u55ooH56H3LEHgrVOeFYLEtrgfgOkg9Xr2-D6vVe-wnGCfRBvKK672xR2J7XcCeyKsokMLDcOU8jO9oKDITmfxSKaemdpEzyJ5QG7xk71epevEARfYh1RG9cq-dEGP23EhlDLM0ebWCkjNYp9ZKgpWMT0xiCoC9jsG8XKRFDcRVEh5bMXeYEGA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f9d9bdf8e8.mp4?token=qAEYGSJ6XnLLZvMD8stpZnVggnJ4Ut8-vhb8G-NK-mrXKdiBZlDxhUFlUmhDwqGSynBb_gTUWGDwJca2kHEnoBd-rYEDBGfz8BVOLa83d-QCA_MDZBQtk_MLxPVqcmz09rL23o4M32RVBJE99mvZGUTgCEuBXJa3u55ooH56H3LEHgrVOeFYLEtrgfgOkg9Xr2-D6vVe-wnGCfRBvKK672xR2J7XcCeyKsokMLDcOU8jO9oKDITmfxSKaemdpEzyJ5QG7xk71epevEARfYh1RG9cq-dEGP23EhlDLM0ebWCkjNYp9ZKgpWMT0xiCoC9jsG8XKRFDcRVEh5bMXeYEGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر علی منوچهرآبادی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، با انتشار ویدئویی در اینستاگرام، تولد خود را کنار مزار فرزندش جشن گرفت و یاد او را گرامی داشت.
علی منوچهرآبادی، شهروند ۲۵ ساله کُرد اهل کرمانشاه، در جریان اعتراضات دی‌ماه ۱۴۰۴ در محدوده فلکه سوم تهرانپارس با شلیک گلوله جان باخت.
او پسرخاله میثم کُرانیان، از دیگر جان‌باختگان اعتراضات مردمی در کرمانشاه، بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 520K · <a href="https://t.me/VahidOnline/77696" target="_blank">📅 17:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ONJ-PPqtYSngTEnn0CsKHh2ZUH4305y1cDMBbUnerlK65K_H5zDUMNsqsPfAPW85dNkSDOAn0Mwog9HhqL1SgKO6gS5u1x2uY9ZaqWJjgoZl_x-EqJgxw3FUGaVa0TgC6Nu4doygTAgk8aMabYfXh3X3aJ0I3OotnBpzCnQBtOY2eTDe047ilXvly107EsFR_7ypKqAYW0GzV0vdoAEAjTKFJ3caWQ5NArcBwqfcxMauy5TUdRVJyWQAlahDf8x7tm0vvpFGPp9w5ptPiX03bnpVlOWNo-OmoV1hq8yjLDPPgnW02LrxKDDh8DwUN5E9l6Rz9iuMbis1RpZlEYwj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت ارتش کویت، ترجمه ماشین:
سامانه‌های پدافند هوایی کویت در حال مقابله با حملات پهپادهای متخاصم، در پی تجاوز جنایتکارانه ایران، هستند.
ستاد کل ارتش اعلام می‌کند که اگر صدای انفجارهایی شنیده شود، ناشی از رهگیری حملات متخاصم توسط سامانه‌های پدافند هوایی است.
از همگان درخواست می‌شود دستورالعمل‌های امنیتی و ایمنی صادرشده از سوی نهادهای ذی‌صلاح را رعایت کنند.
KuwaitArmyGHQ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 574K · <a href="https://t.me/VahidOnline/77695" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lT_VD5E9AkDc69h3baYxAp26fbPmw8kYMb-7rgKpNrrmvpDGvmn-ISMiHofeXQ4eT9jHN9QTW3bfdf1dlVQ_qXnWSRw--9wX4Ok9FKordZ0eZawXTXCB72cWCCneVaDCgsYbwGYqjgx9ws4Nu9cBDTvEhIVYAqg3m5GPLQq_CHJYpmMyVCE0pa2MN1PUSi3XFVpHVkfYsJ7CrdqNF-Qsau7_Ai8ABEVnsW25S41mCCIr0zdi9vaLAVu7bPkXt35lCaRrAhK_Sv2hF3C0EMHnKPHHXA8dCTbOxdXTSxC3eKaQrgaW-UFfhGBUv8DK7bLJk-gfeWCoUvWjmlB-eRZM0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا از وقوع یک حادثه دریایی در شمال شرق خصب عمان، در نزدیکی یک نفتکش گزارش داد.
ساعاتی پیش نیز گزارش شد یک نفتکش در ۱۱ مایل دریایی شمال شرقی لیما، در مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 512K · <a href="https://t.me/VahidOnline/77694" target="_blank">📅 09:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tT7SN7FpkLSWsN1HnzeIHbLTm3zkfNkEbT0TSw1lIsWFa8ac9VhVWvzBHfa_09nYNJ5ZVoEpd7b5--NQLp4_1V2lobWSo0XehD4wnlsqk4HaH23jHEmYtQV4ZEgku9J27n-cVDtDRrbEBLtrRpMayPCmtewfkpY_JLgdwXRNXWEXQ4eIrUXFExMJBRZCO3JpdOn8AskUgTNgQBIMBzlSLSd20DWVT7xeRXcwESTpSRNgDC2TKtMmZK1CnrA1l-IDgmjx6oR7ZKNZuO9ZZaCBT4C3XINdnRbO6rywsbOuL5XU9MLT9x4vOEH3puaSP-ByMMvjWKg4CXdNsA5tAUMA7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس گفت: در روز اول جنگ در ۹ اسفند، ما یک‌ساعت بعد از بمباران فهمیدیم که رهبرمان کشته شده است.
او ادامه داد: تا ما توانستیم سران قوه را جمع کنیم و لاریجانی هم بیاید، ساعت هشت شب شد، آن جا تصمیم گرفتیم اعلام خبر مرگ رهبری صبح فردایش باشد. بعد این جلسه هم سریع پراکنده شدیم.
او اضافه کرد: بعدتر تصمیم گرفتیم همان سحرگاه خبر مرگ رهبری را اعلام کنیم و به مردم بگوییم به خیابان بیایید.
قالیباف در حالی می‌گوید که همان ساعت اول از مرگ خامنه‌ای مطمئن شده که مقام‌های جمهوری اسلامی تا بامداد روز بعد خبر مرگ خامنه‌ای را تکذیب کرده و اعلام می‌کردند او در اتاق فرماندهی حضور داشته و مشغول راهبری جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 530K · <a href="https://t.me/VahidOnline/77693" target="_blank">📅 09:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dlhcleTLaoekRhQIQ4OWkRK_ovBjc5cfaRv_KdO7loPNQ_LQidybyuFClku0x1rBS_wqExVZsPuocXoy6xWJdF3QeA_59qpAcICFJ0ainQXkqghN4r-ZZ5DQENF6hc-qNkKBABu16HkMWWstqI9O3YaOW5g536ltI4LenIGccWpEzaBJZz4gs85gJigSpfQnsFP3hDZZ7cGXZMGHNdWTyoI7RUle9kVJGQmhfaPY4K9ZgA0LVpILHqTIxfdc1vdPvuk1cVXClJvAW7CiN3b6IpBvFa36B2Qc07ZVlohjQ9_ELGz1M-dKVGWBOWA4Yw0tvbFqQSbsexLDfSwkceAO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا اعلام کرد یک نفتکش در حدود ۱۱ مایل دریایی (بیش از ۲۰ کیلومتری) شمال شرقی لیما، در استان مسندم عمان، هدف اصابت یک پرتابه ناشناس قرار گرفت و پس از آسیب دیدن موتورخانه، از کنترل خارج شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 506K · <a href="https://t.me/VahidOnline/77692" target="_blank">📅 07:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SrsLPbHhVlezFauoC5iJJQCx_AM_-e3kZBV8Mbdnf47_Q9m-45w8MzeWXZF8JYP3HWdrwlLDAVCFrK_NkyQFAKyRkjb4q5LcuPf0lI_uW79az2eefX8ZjuZvLS96vWGcfuCXWwtkQNUtEw1AvqyqnRRWgavwkd9zXVyLcmu37zQlY59ArRD9LNX0ygjquzs3NQPGyeFZvaWi4QvDQR_XGY1qYfLWGNQ4ldc-fNQLTxY3o8jHnluY_My4kNb2XQ30sZha80xsIDiCCjd8CuEr_ZzyCBxipPIyYteQDFKhq26kKDluetZRHI5wR5dw1LHSUa7mQTAdn6_czwOfqLV4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقامات آمریکایی و اروپایی آگاه به «ان‌بی‌سی» گفتند که روسیه در حال به اشتراک‌گذاری اطلاعات ارزشمند الکترونیکی و ماهواره‌ای با ایران است که به تهران در جنگ جاری با ایالات متحده کمک می‌کند. به گفته این مقامات، ردیابی ماهواره‌ای و اطلاعات سیگنالی روسیه احتمالا ایران را قادر می‌سازد تا نیروهای آمریکایی را در حملات هوایی با دقت بیشتری هدف قرار دهد، دفاع هوایی خود را در برابر حملات ایالات متحده تقویت کند و در عملکرد تسلیحات ساخت آمریکا اختلال ایجاد نماید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 539K · <a href="https://t.me/VahidOnline/77691" target="_blank">📅 03:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3dXXe061muup6RF1iNib51QTmupplT_7fVEYrnEVP7sS33Zaa3jr0V-xBOSUHhlXDH7LrtLsBL8xFu74vdHHsotO4LspNpBC4I8DYn8WE4rptOVNvnL9XLU1HnG_oPp7xcEZCgmbSjNuMlrHvLv3DL0Q4rnIv5TrezMLhe5cn8YzTHHma3EcEW8OqTlNtjpRgMTgzj9o4zSF0kmQ_VM0OTAJM31-RwnmHDkHvj4qpNBw0gVm5-p6kJmhwtw7x9kO2JzoYW1Y1jlk9iD1b9fzDYzYFpr6SieADWhnacZidlR1Vvx03RdaZntRQjpvlzTFqp1q_-jYg5q_2V12dfNTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
ترامپ دستور حمله‌ای تازه به ایران را صادر کرد
"
وال‌استریت ژورنال
به نقل از مقام‌های آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهوری آمریکا، طرح حمله جدید به ایران را که در کمپ دیوید ارائه شده بود، تصویب کرده و این عملیات ممکن است از آخر هفته (شنبه و یکشنبه) آغاز شود و چند روز ادامه یابد.
به گفته این منابع، هرگونه پیشرفت فوری در دیپلماسی یا تغییر نظر ترامپ می‌تواند اجرای حملات را متوقف کرده و مسیر مذاکرات را دوباره باز کند.
این روزنامه نوشت یکی از گزینه‌های مورد بررسی، کارزار دو هفته‌ای حملات هوایی فشرده برای تضعیف توان موشکی جمهوری اسلامی است.
مقام‌های آمریکایی گفتند ترامپ معتقد است توافق موقت صلح کارساز نبوده و همچنان بر توقف برنامه هسته‌ای جمهوری اسلامی و پایان کنترل تهران بر تنگه هرمز اصرار دارد، در حالی که تهران از مواضع خود عقب‌نشینی نکرده است.
وال‌استریت ژورنال افزود مشاوران نظامی ترامپ کاهش ذخایر مهمات آمریکا را یکی از مخاطرات احتمالی این عملیات ارزیابی کرده‌اند.
@
VahidOOnLine
اکسیوس:
ترامپ حمله به اهداف انرژی ایران در چند روز آینده را بررسی می‌کند
ترجمه ماشین: دونالد ترامپ، رئیس‌جمهوری آمریکا، به‌طور جدی در حال بررسی انجام حملاتی علیه اهداف انرژی در ایران طی چند روز آینده است، اما هنوز دستور نهایی اجرای آن را صادر نکرده است؛ یک مقام آمریکایی روز جمعه این موضوع را به اکسیوس گفت.
چرا اهمیت دارد:
هدف از کارزار جدید بمباران آمریکا علیه اهداف انرژی و زیرساختی در ایران، تلاش برای واداشتن ایرانی‌ها به پذیرش شروط ایالات متحده در مذاکرات جاری آتش‌بس خواهد بود.
▪️
این حملات ممکن است برای نخستین‌بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدیدی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
▪️
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین رسانه‌هایی بودند که درباره حملات احتمالی گزارش دادند.
آنها چه می‌گویند:
ترامپ در آغاز جلسه روز جمعه کابینه به حمله احتمالی اشاره کرد و گفت: «خب، ما خیلی سخت به آنها ضربه خواهیم زد و می‌دانید، بالاخره در مقطعی خواهند گفت که دیگر نمی‌توانیم تحمل کنیم.»
▪️
او افزود هرچه ایالات متحده حملات بیشتری انجام دهد، ایرانی‌ها ضعیف‌تر می‌شوند «و بعد کم‌کم از پا می‌افتند.»
▪️
کارولین لیویت، سخنگوی کاخ سفید، به اکسیوس گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در جلسه کابینه گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 518K · <a href="https://t.me/VahidOnline/77690" target="_blank">📅 01:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P9Uw9x0BHlg8kUT6O2sia4Np2WDUsoqE6XobW8PmvI0tnMbvOb237jh2RI7G3BMwZ17pX2teUyeXUrkRQ6LviBvDqSjkfI0eq0H9V0XV0wavYs9yPj3VLfMS-Vr0fdU7rZjmBw-oBLV_zfhWVHtXjkMyarmqxgOuophhtMvVGu0t9LTB9Kyv98gysXrR6z05lwCZx1QltvdhVfkcPwwTSCAhS13sMGfEJw_7iWw6YFZ-kT3fghfqSHXNpHnPdPPY65hoa-kOvTwO17i44tvOLy5cihsbHFW3nqdTBCDSys9zvxLYD2WePDcZGwWw8JrxY0PnqkFtfsOta2tbO3kObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"
آمریکا و اسرائیل برای بمباران اهداف مرتبط با انرژی در ایران آماده می‌شوند
"
سی‌بی‌اس به نقل از منابع
ترجمه ماشین:
واشنگتن — چندین منبع به سی‌بی‌اس نیوز گفتند که ایالات متحده و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین کارزارهای بمباران تاکنون علیه اهداف زیرساخت‌های انرژی در ایران هستند و احتمال انجام حملات در طول تعطیلات آخر هفته وجود دارد.
بحث‌هایی درباره تلاش برای پایان دادن به عملیات تا زمان بازگشایی بازارهای مالی در روز دوشنبه مطرح شده بود، زیرا نگرانی‌هایی درباره تأثیر بمباران‌ها بر اقتصاد آمریکا و جهان وجود دارد، اما زمان مشخصی برای پایان عملیات قطعی نشده بود.
به گفته چندین منبع آمریکایی، اسرائیلی‌ها در جریان قرار گرفته‌اند و در حال هماهنگی با ایالات متحده هستند. این منابع گفتند رئیس‌جمهور هنوز دستور نهایی آغاز حملات را صادر نکرده است.
سخنگوی دولت اسرائیل به درخواست اظهارنظر پاسخ نداد.
یک عملیات مشترک به معنای بازگشت اسرائیل به عملیات رزمی خواهد بود؛ عملیاتی که این کشور در جریان آتش‌بس میانجی‌گری‌شده از سوی آمریکا متوقف کرده بود. از زمانی که تفاهم‌نامه از هم پاشید و ایالات متحده در اوایل ژوئیه عملیات رزمی را از سر گرفت، ایران اسرائیل را هدف قرار نداده است.
به گفته منابعی که بعداً در جریان قرار گرفتند، طرح حمله نظامی روز جمعه در نشست کابینه دونالد ترامپ، رئیس‌جمهور آمریکا، در کمپ دیوید مطرح شد. یکی از منابع گفت برخی از دستیاران کاخ سفید که بر مسائل سیاسی تمرکز دارند، به‌شدت با این طرح مخالف بودند.
زمانی که خبرنگاران در اتاق حضور داشتند، آقای ترامپ گفت: «ما آن‌ها را بسیار سخت هدف قرار خواهیم داد. بالاخره در مقطعی خواهند گفت: “دیگر نمی‌توانیم تحمل کنیم.”»
او در پاسخ به پرسش خبرنگاران درباره احیای دیپلماسی گفت: «فکر می‌کنم ما فقط می‌خواهیم پیروز شویم.»
دو منبع گفتند زیرساخت‌های انرژی، از جمله نیروگاه‌ها و پالایشگاه‌ها، احتمالاً هدف قرار خواهند گرفت.
کارولین لیویت، سخنگوی مطبوعاتی کاخ سفید، در بیانیه‌ای به سی‌بی‌اس نیوز گفت: «همان‌طور که رئیس‌جمهور ترامپ امروز در نشست کابینه خود گفت، ایالات متحده پیروز خواهد شد و در دوران ریاست‌جمهوری او، ایران به سلاح هسته‌ای دست نخواهد یافت.»
شان پارنل، سخنگوی ارشد پنتاگون، گفت پنتاگون پیش از آنکه رئیس‌جمهور تصمیم نهایی خود را بگیرد، درباره اهداف اظهارنظر نخواهد کرد.
پارنل در بیانیه‌ای گفت: «وزارت جنگ کاملاً آماده و مهیای عملیات است و می‌تواند در هر لحظه دستورات رئیس‌جمهور را اجرا کند.»
یک مقام پیشین نظامی آمریکا به سی‌بی‌اس گفت، فایده حمله به زیرساخت‌های انرژی این خواهد بود که بر توان نیروهای نظامی ایران برای ارائه خدمات و اداره مؤثر کشور تأثیر بگذارد.
یک مقام ارشد اسرائیلی گفت هنگامی که آقای ترامپ و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اوایل این هفته دیدار کردند، نتانیاهو او را در جریان سه گزینه برای جنگ قرار داد که یکی از آن‌ها حملات نظامی متمرکز بر مسیرهای تدارک‌رسانی زمینی بود. نتانیاهو همچنین با هگست، وزیر دفاع آمریکا، دیدار کرد.
یک مقام آمریکایی گفت ایالات متحده در جریان این درگیری پیش‌تر به پل‌هایی با کاربری دوگانه — که نظامیان و غیرنظامیان از آن‌ها استفاده می‌کردند — حمله کرده است.
روز جمعه گفت‌وگوهایی در سطوح عالی دولت آمریکا درباره قطع برق سراسر تهران انجام شد، اما تا بعدازظهر جمعه هیچ تصمیمی گرفته نشده بود.
هفته گذشته، آقای ترامپ در تروث سوشال نوشت که در ازای هر حمله به یک کشتی در تنگه هرمز، یک پل یا نیروگاه ایرانی را بمباران و نابود خواهد کرد.
این خبر فوری است و به‌روزرسانی خواهد شد.
cbsnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 465K · <a href="https://t.me/VahidOnline/77689" target="_blank">📅 00:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HAMjbzTvgYha-_3AXK69CxYse_IC0HM_qEtUvycdwxlrVq91zJRJ_7OC1SZ-JdRmniUa8B1zMjq9T_-KffmYauq5DoMljFaApLUZ-2FYrqMF2TC3_9soZnS23_HHq5dIebOZGTqptsjKKpejmPK4Tgvuk21ZpXpgoZ2IVPSYV1xX-y3CtIz4jacYjap5IYvsjjSX2HGMeRR6uVVYGFRJ6OTzkNAIgTl2hyAOpAmnLJWarw0WfcXUl-3XbpA2lCJzoeW6K4PX4-xrnwY0F8Nok3j71Yef3y_dvXLqKnIZXm9ljKxaPECZUCfH8DQRX1xqXP-zmgX6-5yaIpz5NJyI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد. این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های…</div>
<div class="tg-footer">👁️ 459K · <a href="https://t.me/VahidOnline/77688" target="_blank">📅 00:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNY-Kj_i2XNUEJa01EJ27MIcZjuc_uMsv__5fipMmjnocupZSRgy44iqdkwoBOdGqQOEcHguF6ujh65BC-PdLhlXPHLhFyjxzIMs8nvdmGvVrSArETei7CzVeWEZRBDJXeJyRuOk-xwAkeO7bzhliUW_rs_Eo10clHyNGhk5JJmmffGSdiAKoFu_WA2MPQvbGMgytvVtMSNWsK8bjJVzdY7eOngEQI9woT1ECmeVixh10J28W2eoFrZW9qGSKY4UB3tBXBUotIo8XU_WGEw5ha-TUEiutIMe8SrCZBKWS_MHzp0AJBxiAMCRyCgUgakvv35GqEXQ0DWMcbktcjtFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز روز جمعه ۹مرداد۱۴۰۵
گزارشی تحقیقی
منتشر کرده، از استفاده سپاه از شبکه قمار غیرقانونی ایران که با آن میلیاردها دلار را به رغم تحریم‌ها جابه‌جا می‌کند.در این گزارش به یک صرافی ارز دیجیتال مستقر در دوبی اشاره شده که  به مرکزی برای جابه‌جایی پول‌های غیرقانونی ایران تبدیل شده است.
در گزارش رویترز صرافی مذکور «شل‌بیت» معرفی شده و تایید شده است که این صرافی، یک شبکه گسترده قمار را که توسط دو اینفلوئنسر سرشناس و بین‌المللی در شبکه‌های اجتماعی اداره می‌شود، به فعالیت‌های استخراج بیت‌کوین و بانک مرکزی ایران مرتبط می‌کند.
بنابر گزارش منتشر شده، «شل‌بیت» صدها میلیون دلار ارز دیجیتال را به «بایننس»، بزرگ‌ترین صرافی ارز دیجیتال جهان، منتقل کرده است. دو شرکت تحقیقاتی حوزه ارزهای دیجیتال و یک تحلیلگر مستقل مدارکی ارایه کرده‌اند نشان می‌دهد نشانی ثبت‌شده صرافی بدون مجوز «شل‌بیت» دفتری در بالای یک هتل ارزان‌قیمت در محله‌ای معمولی و نه‌چندان مطرح در دوبی است. این صرافی توسط یک ایرانی مقیم خارج از کشور اداره می‌شود. رویترز اطلاعات ارایه شده در این زمینه را تایید کرده است.
در بخش دیگری از این گزارش آمده است که یکی از مشتریان اصلی «شل‌بیت»، یک شبکه قمار فارسی‌زبان متشکل از بیش از ۲ هزار وب‌سایت است که توسط دو اینفلوئنسر مشهور ایرانی در شبکه‌های اجتماعی تبلیغ و اداره می‌شود. گفته شده که این دو ارتباطاتی در سطوح بالای حکومت ایران دارند.
یکی از آن‌ها در یک ویلای گران‌قیمت در مادرید فعالیت می‌کند و دیگری تا همین اواخر در یک هتل لوکس در هنگ‌کنگ مستقر بود.
هر دو اینفلوئنسر اشاره شده و همچنین فرد اصلی اداره کننده صرافی «شل‌بیت» در سال ۲۰۲۳ در ایران به اتهام مشارکت در یک پرونده قمار غیرقانونی، محکوم شدند.
مطابق قوانین جمهوری اسلامی «قمار کردن» امری غیرقانونی است و مجازات‌های حبس و شلاق برای مرتکبان به‌دنبال دارد با این‌همه گزارش رویترز تایید می‌کند که این شبکه قمار تازه شناسایی شده به سیستم پرداخت آنلاین ایران که مستقیما تحت نظارت بانک مرکزی است دسترسی دارد.
شل بیت بر اساس گزارش رویترز در مرکز عملیاتی است که شبکه قمار، بانک مرکزی و دیگر نهادهای تحریم‌شده ایرانی را به بازارهای جهانی ارزهای دیجیتال مرتبط می‌کند.
یکی از چهره‌های اصلی این شبکه قمار، «ساشا سبحانی»، پسر یک دیپلمات و سفیر پیشین ایران و دیگری «پویان مختاری»، یک چهره مشهور شبکه‌های اجتماعی و خواننده است که پس از اخراج از دوبی در اواخر ماه آوریل، مدتی بین هتل‌های لوکس هنگ‌کنگ جابه‌جا می‌شد.
پویان مختاری اخیرا و در جریان جنگ آمریکا و اسراییل با انتشار ویدیویی گفت که مخالف جمهوری اسلامی نیست و دچار «تحول فکری» شده است.
تحقیقات رویترز آشکار می‌کند که سپاه پاسداران سال‌ها پیش کنترل بزرگ‌ترین وب‌سایت‌های قمار قابل دسترس در ایران را به دست گرفته و از آن زمان تاکنون از این وب‌سایت‌ها برای انتقال پول به خارج از کشور استفاده کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77686" target="_blank">📅 22:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xukn4tBU9qh8Emvib__S78vYPqgJkR42H7s-rjHXnRxjyIAn53aW_LZ2IoV7hF85g7QatWIbn65cPlBY8Kvt55goPL4lulTr3-jAjPYRrwaDhLcUJcrKgsBfm1Fy_b1X1_Zu-DolZR-u5HP94r8QJYbP214tPc6qMJcbtuvUDNqZ0W887D-QMwZsBVLRmrXjux4LTwfA3wyO5Zu9Wep2K3_Ip3qua5Xm6UYEV-p0AWvIMAnQEnusFFqKCp5V17_9wOpXMPmzGZhgwyMK4eoKymuH46ctzN-NyMwmmDj1B_AiCzD6VAJn8sRt4ID2NZOn0dpIrUhjWOvYx7fkTMp3oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q2lMSuaRNvVhj0-8HjjwVYWlLXXsE61IkF440zuoylOaa1QEwrvIJFbvdnJ2Nenk2Yma--KOTWrNBTTpEWV9QbdRVaSkaIhfluxHLwrRHmsxAdm_RBiQjHiWpZ9cm1DOxLYuZTEv4Ir6JnxamrGep2we0D9fiOfvybiRuQ20GVvurrHpugxW4FoVLv2xfFY9bSVWFeMrxWvRt5WKMqh_P3Vm3Huzh4VbBEv9vFr2rY-BBpvhqbmyWG5jHRrIBnhI7nXzVqMGE1h9frzU0RQLmhANL6xwPDAZFNdiQywMuPN0s7AHTL519eo17ijtK1mLekBxL_ParBykVEn9sY36wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=ZMmT7Cfyl8bxzhk5LnPQmHJCLVshbE-ibkB-0X0puuk5WSvH0mon8onpbsSn6B9FZXFykxi-XpCs_OIKbFOLhVibzvxUbHttkcGaUZFDuCwHE3Mlw4N-8lroDV4B7YjsZjtBl2sY0wPlknAuoka0wqenJTuvPtfI4qT4Pk232Wayt-vS5JtVVkCepb2gkwEoqdxQqDaw7ENAkFtbv0Wb94zT4ECEX8mY3WnM73LJQZKzf2Jes4e5eCY2gXQo5TgNB4ah0uLIHaOk77TPqDA-YUk7HIymOgocZYClfEGIR4im_xgTDf56cbbU30WYDeH-Uz_4pWOCQrgK_QwwpmG5og" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9f2fb35b.mp4?token=ZMmT7Cfyl8bxzhk5LnPQmHJCLVshbE-ibkB-0X0puuk5WSvH0mon8onpbsSn6B9FZXFykxi-XpCs_OIKbFOLhVibzvxUbHttkcGaUZFDuCwHE3Mlw4N-8lroDV4B7YjsZjtBl2sY0wPlknAuoka0wqenJTuvPtfI4qT4Pk232Wayt-vS5JtVVkCepb2gkwEoqdxQqDaw7ENAkFtbv0Wb94zT4ECEX8mY3WnM73LJQZKzf2Jes4e5eCY2gXQo5TgNB4ah0uLIHaOk77TPqDA-YUk7HIymOgocZYClfEGIR4im_xgTDf56cbbU30WYDeH-Uz_4pWOCQrgK_QwwpmG5og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایتالیا پس از بحران مهاجران در سبته، اجرای نظام تردد آزاد در منطقه شنگن با اسپانیا را به‌طور موقت تعلیق کرد.
این اقدام پس از آن انجام شد که مقام‌های اسپانیا روز جمعه اعلام کردند بیش از ۶۰ هزار نفر طی ۲۴ ساعت از طریق زمین و دریا وارد سبته شده‌اند. به گفته مقام‌های اسپانیا، پس از این موج ورود مهاجران، حدود ۳۷ هزار و ۵۰۰ نفر به‌صورت داوطلبانه به مراکش بازگشته‌اند.
در جریان تلاش برای عبور از مرز، دست‌کم ۵۷ نفر جان باختند؛ شماری بر اثر غرق‌شدن و برخی دیگر در ازدحام هنگام عبور از موانع مرزی.
پدرو سانچز، نخست‌وزیر اسپانیا، این رویداد را «نقض حاکمیت ارضی اسپانیا» خواند و گفت روند بازگرداندن مهاجران فاقد مدارک قانونی با همکاری مراکش تسریع خواهد شد.
اتحادیه اروپا در شرایط استثنایی به کشورهای عضو اجازه می‌دهد به‌طور موقت کنترل مرزهای داخلی منطقه شنگن را دوباره برقرار کنند.
@
VahidHeadline
پیش‌تر:
هزاران مهاجر از شامگاه پنج‌شنبه تا صبح جمعه با عبور از مرزهای مراکش وارد مناطق تحت اداره اسپانیا در شمال آفریقا شدند
ورود مهاجران در تمام طول شب ادامه داشته و صبح جمعه نیز همچنان ادامه پیدا کرده است.
همزمان، تصاویر خبرگزاری رویترز، هجوم جمعیتی از مهاجران به گذرگاه مرزی میان مراکش و شهر ملیلیه اسپانیا در شمال آفریقا، را نشان می‌دهد.
در سئوتا، دولت اسپانیا برای مقابله با صدها مهاجری که از مسیر دریا و خشکی وارد این منطقه شده‌اند، یگان‌های نظامی را مستقر کرده است.
تصاویر منتشرشده نشان می‌دهد صدها مهاجر با شنا کردن یا استفاده از تایرهای بادی از سمت مراکش تلاش کرده‌اند خود را به سئوتا برسانند و گروهی دیگر نیز با عبور از یک دروازه مرزی زمینی وارد شهر شده‌اند.
@
VahidOOnLine
وزیر کشور فرانسه روز جمعه اعلام کرد پاریس در پی ورود هزاران مهاجر از مراکش به سئوتا، کنترل‌های مرزی خود با اسپانیا را افزایش خواهد داد.
@
VahidOOnLine
فنلاند اعلام کرد از پیشنهاد ایتالیا برای تعلیق عضویت اسپانیا در منطقه بدون کنترل مرزی شنگن حمایت می‌کند. اقدامی که در پی ورود ده‌ها هزار مهاجر به منطقه سئوتا، تحت حاکمیت اسپانیا در شمال آفریقا، مطرح شده است.
@
VahidOOnLine
پدرو سانچز، نخست‌وزیر اسپانیا، روز جمعه نهم مرداد ماه، ورود گسترده مهاجران به سئوتا، منطقه تحت حاکمیت این کشور در شمال آفریقا، را «نقض و حمله به تمامیت ارضی اسپانیا» محکوم کرد.
سانچز پس از موج اخیر عبور مهاجران از مرز مراکش به سئوتا، این اقدام را محکوم کرد و تاکید کرد دولت اسپانیا از حاکمیت و مرزهای خود دفاع خواهد کرد.
@
VahidOOnLine
ایلان ماسک، میلیاردر آمریکایی و مالک شرکت‌های تسلا و اسپیس‌ایکس، در واکنش به ورود گسترده مهاجران مراکشی به شهر سئوتا در اسپانیا، با انتشار تصاویری از فیلم «جنگ جهانی زد»، این وضعیت را به «آخرالزمان زامبی‌ها» تشبیه کرد و نوشت: «وای، اوضاع اسپانیا واقعا دیوانه‌کننده به نظر می‌رسد!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/77680" target="_blank">📅 22:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نشست خبری دولت ترامپ در کمپ‌دیوید
ویدیوی کامل با زیرنویس فارسی:
۱۰۰ مگابایت
نسخه یک گیگابایتی:
اینجا
متن فارسی ۱۶ بازه از ویدیو
بخش‌هایی از متن لینک بالا:
🔻
ترامپ:
در مینه‌سوتا یک حمله سایبری رخ داده و آن را به ایران نسبت داده‌اند.
فکر نمی‌کنم چنین باشد. من مینه‌سوتا را مقصر می‌دانم، چون به‌شدت بی‌کفایت هستند. حمله‌ای سایبری به ۳۰ تأسیسات آب انجام شد و من مینه‌سوتا و فرماندار فاسد آن را مقصر می‌دانم.
آن‌ها دوست دارند بگویند: «اوه، کار ایران بود.» ایران باید خیلی خوش‌شانس باشد. ایران مشکلات بزرگ‌تری از نگرانی درباره مینه‌سوتا دارد.
....
🔻
ترامپ:
جنگی در جریان است. شاید شما آن را جنگ بنامید؛ من شاید آن را عملیات نظامی بنامم، چون آن‌ها دیگر نیروی دریایی ندارند؛ نابود شده است. نیروی هوایی‌شان نابود شده است. هواپیما ندارند.
بخش بزرگی از موشک‌هایشان از میان رفته است. هنوز مقداری دارند، اما بسیار کمتر از چهار یا پنج ماه قبل. ظرفیت تولیدشان تقریباً از میان رفته و ظرفیت پهپادی‌شان نیز تقریباً نابود شده است.
تعداد بسیار کمی دارند، اما هنوز مقداری باقی مانده است. از نظر من اگر حتی یکی داشته باشند، همان هم بیش از حد زیاد است.
🔻
به ویتنام نگاه کنید؛ ۲۰ سال آنجا بودند. به افغانستان نگاه کنید؛ سال‌های زیادی آنجا بودند. به جنگ کره یا هر جنگ دیگری نگاه کنید؛ سال‌ها طول کشید. ما پنج ماه است وارد شده‌ایم و توان نظامی آن‌ها را نابود کرده‌ایم.
باز هم مقداری برایشان باقی مانده، اما به‌زودی همان مقدار هم باقی نخواهد ماند.
🔻
مارکو روبیو:
نخستین موضوع، دادگاه کیفری بین‌المللی است؛ سازمانی بین‌المللی و نامشروع. خودشان را نامشروع کرده‌اند، چون ادعا می‌کنند حتی اگر عضو آن دادگاه نباشید، باز هم می‌توانند به سراغتان بیایند.
معنای واقعی آن این است که در آینده نظامیان آمریکایی، رهبران سیاسی و افراد دیگر ممکن است از سوی این دادگاه کیفری بین‌المللی تحت کیفرخواست قرار بگیرند. ...
🔻
ترامپ:
هیچ اطلاعاتی وجود ندارد که نشان دهد آن‌ها دنبال من هستند. البته ممکن است چنین اتفاقی بیفتد.
حرف من این است که این یعنی او نمی‌خواهد از من دفاع کند؛ می‌خواهد از بی‌بی و افراد مختلف دیگری دفاع کند.
افراد زیادی هستند که نباید به این شکل با آن‌ها برخورد شود، اما در حال حاضر هیچ نشانه‌ای وجود ندارد که من یکی از آن‌ها باشم.
....
🔻
پیت هگست:
... تعجب می‌کنید چرا حوثی‌ها در این درگیری حضور ندارند، با اینکه نیروی نیابتی ایران هستند؟ چون ۴۵ روز سنگینی قدرت آمریکا را احساس کردند. و شما شجاعت انجام این کار را داشتید.
🔻
اسکات بسنت:
... در مارس ۲۰۲۵ شروع کردیم. در دسامبر ۲۰۲۵، بزرگ‌ترین بانک ایران فروپاشید. بانک مرکزی مجبور شد پول چاپ کند و این باعث تورم شد.
اکنون تورم آن‌ها ۱۸۰ درصد است. قادر به پرداخت حقوق نیروهایشان نیستند و به دستور شما در سراسر جهان به‌دنبال دارایی‌هایشان می‌گردیم.
این پول به مردم ایران و آمریکایی‌هایی می‌رسد که از اقدامات ایرانی‌ها آسیب دیده‌اند؛ چه در ماجرای ناو یو‌اس‌اس کول، چه پادگان‌های لبنان، یا حملات ایرانی‌ها به آن کشتی‌های در حال خروج.
مشارکت در این کار برای من افتخار بوده و مشتاق ادامه آن هستم.
🔽
درباره ادامه جنگ:
🔺
خبرنگار:
آقای رئیس‌جمهور، در ۱۰ روز گذشته حملات میان ایران و ایالات متحده را دیده‌ایم. چگونه آتش‌بس را احیا می‌کنید و دیپلماسی را دوباره از سر می‌گیرید؟
🔻
ترامپ:
فکر می‌کنم فقط می‌خواهیم پیروز شویم. عملکردمان بسیار خوب است. تلاش می‌کنیم تا جایی که در چنین شرایطی ممکن است، ملایم باشیم، اما آن‌ها در حال نابودشدن هستند.
دیگر نیروی دریایی، نیروی هوایی یا پدافند هوایی ندارند. این به آن معنا نیست که هیچ توانی ندارند؛ مقداری دارند، اما بسیار اندک است.
فقط می‌خواهیم پیروز شویم. نمی‌خواهیم آن‌ها این توان را داشته باشند. موضوع بسیار ساده است.
آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند. ایران سلاح هسته‌ای نخواهد داشت و نمی‌تواند داشته باشد. اگر چنین سلاحی داشتند، خاورمیانه تا الان نابود شده بود.
اگر من برجام، همان توافق اوباما، را متوقف و لغو نکرده بودم، آن‌ها اکنون سلاح هسته‌ای داشتند.
فکر می‌کنم اسرائیل دیگر وجود نداشت؛ در بخش‌های بزرگی از خاورمیانه و شاید کشورهای دیگری در قاره‌های مختلف نیز، چون صادقانه بگویم این افراد دیوانه‌اند.
بنابراین نمی‌توانند سلاح هسته‌ای داشته باشند و نخواهند داشت.
🔺
خبرنگار:
[پرسش ناقص و نامفهوم درباره آنچه در چهار یا هشت هفته آینده باید انتظار داشت.]
🔻
ترامپ:
می‌دانید، به آن‌ها حمله خواهیم کرد؛ حملات بسیار سختی به آن‌ها وارد خواهیم کرد. بالاخره در مقطعی خواهند گفت: «دیگر نمی‌توانیم تحمل کنیم.»
🔺
خبرنگار:
آقای رئیس‌جمهور، بازگردیم به ایران. گزارشی منتشر شده که ارتش پیشنهادی داده است تا ظرف ۱۰ یا ۱۴ روز حمله‌ای بزرگ و سخت انجام دهید—
🔻
ترامپ:
ما همین حالا هم حمله بزرگ انجام داده‌ایم. منظورتان از «بزرگ» چیست؟
آن‌ها ۱۵۹ کشتی داشتند؛ تمام نیروی دریایی‌شان همین بود. هر ۱۵۹ کشتی، تمام نیروی دریایی‌شان، در کف دریا قرار دارد. من این را حمله بزرگ می‌نامم.
تسلیحات پدافند هوایی بسیار خوبی داشتند، اما کار نکرد و همه آن از بین رفته است. تمام رادارهایشان از بین رفته، رهبرانشان از بین رفته‌اند؛ همه‌چیز از بین رفته است.
🔻
ترامپ:
برای مثال، خواندید که پنج موشک شلیک شد. سرعتشان ۸۶۰۰ مایل در ساعت بود.
فکرش را بکنید؛ اگر با خودرو ۶۰ مایل در ساعت بروید، کمی سریع به نظر می‌رسد. این موشک‌ها ۸۶۰۰ مایل در ساعت سرعت داشتند و موشک‌های بزرگی بودند. به سوی اردن شلیک شدند و نیروهای ما آنجا بودند: بنگ، بنگ، بنگ، بنگ، بنگ.
[خنده حاضران]
این می‌توانست کلیپ صوتی خوبی باشد! پنج موشک شلیک شد و هر پنج موشک را پیش از آنکه نزدیک شوند، ساقط کردیم. هیچ کشور دیگری چنین توانی ندارد.
🔺
خبرنگار:
آقای رئیس‌جمهور، گفتید هنوز مقداری توان برایشان باقی مانده است. آیا آمریکایی‌ها باید آماده باشند که این حملات متقابل ادامه پیدا کند تا زمانی که ایران دیگر توان حمله فوری نداشته باشد؟
🔻
ترامپ:
ضعیف‌تر خواهند شد. شاید اکنون کمی قوی‌تر شوند، اما ضعیف‌تر خواهند شد.
🔺
خبرنگار:
و بعد به‌تدریج از نفس می‌افتند؟
🔻
ترامپ:
بله، فکر می‌کنم همین‌طور است. احمقانه است که بگویم نه. همیشه باید مراقب باشید.
🔺
خبرنگار:
وضعیت مذاکرات چگونه است؟ چه کسی از طرف دولت در مذاکرات حضور دارد؟
🔻
ترامپ:
آن‌ها همیشه می‌خواهند مذاکره کنند، اما بارها زیر قولشان می‌زنند. استیو در حال مذاکره است. جرد هم هست؛ افراد بسیار خوبی داریم. جی‌دی به‌شدت درگیر است. افراد فوق‌العاده‌ای در حال مذاکره هستند. مارکو هم درگیر است.
افراد بسیار خوبی داریم؛ بهترین‌ها را. اما آن‌ها توافق خواهند کرد.
برای مثال، درباره موضوع هسته‌ای صحبت می‌کنیم و هفت ساعت آنجا می‌نشینیم و درباره برنامه هسته‌ای حرف می‌زنیم. می‌گویم چرا هفت ساعت؟ ده دقیقه کافی است؛ پنج دقیقه وقت دارید، باید حلش کنید.
اما هفت ساعت صحبت می‌کنند، بعد بیرون می‌آیند و من می‌گویم درباره موضوع هسته‌ای گفت‌وگو کردند. آن‌ها بیرون می‌روند و می‌گویند: «ما هرگز درباره موضوع هسته‌ای صحبت نکردیم.»
می‌گویم چرا؟ چرا چنین چیزی می‌گویند؟ تنها کاری که می‌کنند این است که من را عصبانی می‌کنند.
🔺
خبرنگار:
با توجه به آنچه گفتید، باور دارید می‌توان با ایران به توافق رسید؟
🔻
ترامپ:
بله، می‌توان. ببینید، دارم اعتمادم را به آن‌ها از دست می‌دهم، چون دروغ می‌گویند و واقعیت را تحریف می‌کنند.
چند روز پیش پنج موشک شلیک شد. ما آن‌ها را ساقط کردیم، اما در میانه مذاکره بودیم. منتظر تماس استیو بودم تا ببینم مذاکرات چگونه پیش می‌رود؛ در عوض پیت تماس گرفت و گفت: «آن‌ها همین حالا پنج موشک به یکی از پایگاه‌های ما در اردن شلیک کردند.»
خوشبختانه نیروهای ما تجهیزات را به کار انداختند. کارکردن با این تجهیزات بسیار پیچیده است. از این افراد می‌پرسید کجا درس خوانده‌اند و پاسخ می‌دهند ام‌آی‌تی یا کلتک؛ دانشگاه‌هایی که معمولاً با نیروهای نظامی تداعی نمی‌شوند.
افرادی فوق‌العاده باهوش این تجهیزات را اداره می‌کنند. وقتی چنین افرادی نباشند، شلیک‌ها خطا می‌رود، سامانه ایمنی خطا می‌کند یا دقت کافی وجود ندارد. ما افراد فوق‌العاده‌ای داریم.
فکرش را بکنید؛ چند ماه پیش در یک بازه کوتاه ۱۱۱ موشک به سوی ناو هواپیمابر آبراهام لینکلن شلیک شد؛ ناوی بزرگ و زیبا و از نظر طراحی یکی از زیباترین کشتی‌ها.
هر ۱۱۱ موشک مدت‌ها پیش از رسیدن به ناو ساقط شدند. در چند مورد تقریباً همان لحظه‌ای که پرتاب شدند، سرنگون شدند. فناوری باورنکردنی‌ای است.
ناوی که میلیاردها دلار ارزش دارد و موشک‌ها به سوی آن در حرکت‌اند؛ هر ۱۱۱ موشک ساقط شدند. من با افرادی که این کار را انجام دادند صحبت کردم. دوست دارم به افراد پاداش بدهم؛ من رئیس‌جمهورم و با آن‌ها تماس می‌گیرم. آن‌ها کاملاً خونسرد بودند.
🔻
خبرنگار:
آقای رئیس‌جمهور، در دو هفته گذشته سنتکام حملاتی انجام داده است. سنتکام گفته هدف این حملات کاهش توان ایران برای مختل‌کردن تردد در تنگه هرمز بوده است. چند حمله دیگر لازم است تا این توان به‌طور چشمگیری کاهش یابد؟
🔺
ترامپ:
هیچ‌وقت نمی‌توان دانست. بیشتر مردم تا الان تسلیم شده بودند. آن‌ها دیگر نیروی دریایی یا نیروی هوایی ندارند. بیشتر مردم تسلیم می‌شدند، اما آن‌ها نشده‌اند. از این بابت به آن‌ها اعتبار می‌دهم. سرسخت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77678" target="_blank">📅 20:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oJXQhjLgZZNiYAxCdPO7KiqIxzRw6rbpB4IIEWZsVFQjd4_r1ibCKgMkYjS_MFj6dOBaPlmerhDaFKxBu5_nLxs2dAn7lX_h0mNQejYnmGy8jS1o8upg4ZbXbcbexKgviFXpgCTxpkpJsV2K0dz3-wyaFoiJrLv2GgJgPoFRmrBkzpGa1bP0IgC1UOZavHyP3YUqORBEk4vkRQhTODv-04UU1Z6G-f5V_o7zVYEZqKw6GBRezShZhPXBmjkJ0jQ-DP2A4MkrV66Ol3-egaNeHTqE7YCtYDuneUyOmNemSKpTEca6KUSQq3ilWEwOMnWdSlNnWxKg1jQ33iujTx0Q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: دولت ایران بار دیگر مدعی شده است که تنگه هرمز را بسته است. این ادعا نادرست است.
✅
واقعیت: تنگه هرمز همچنان برای عبور کشتی‌های تجاری باز است. ایران کنترلی بر آن ندارد. طی چهار ماه گذشته، هزاران کشتی از این آبراه بین‌المللی عبور کرده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/77677" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQz1elkDMv3o07LCfA1CQOo60djQ_7m1hoLdvLFZrbhtywrU-GK1ajZmcaFb8jZytXKzl6visCVt-QiIuXETGMwLZw4vopZMxg-eVTYFCd97w-sH9vlDyY_Q5NJ-OWez7d52knJLZBB6OY0gOiROSV4KUq1_XQfqUv_7-_tygx4NifZmBXcvAIi-vRnSYhqD-hj92NjeGrsD7gxnsdCcwKBIhd8jUWyIm00E_19f8dTXNk83mSpIWqqhnnL_KlTvudHGDPj4SdoBP4V2L0rss9986n3mKGSNuHFHtYgh_RpgyIzXIAh19GODVrWvuXf_SV7Lss0nEZilk6QUF8wSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دوروف، بنیان‌گذار تلگرام، یک روز پس از آنکه اعلام کرد روسیه او را به دلیل مخالفت با درخواست‌های این کشور برای اعمال سانسور و نظارت گسترده بر کاربران، در فهرست «تروریست‌ها» قرار داده است، با انتشار تصویری از ملاقات مقام‌های طالبان با سرگئی لاوروف، وزیر خارجه روسیه، به این اقدام واکنش نشان داد.
دوروف در این تصویر که در شبکه اجتماعی ایکس به اشتراک گذاشت، عکس خود را با برچسب تروریست، کنار تصویری از دیدار مقام‌های روسیه با مقام‌های طالبان قرار داد و زیر عکس دوم نوشت: «شرکای مورداحترام» و برای عنوان این تصویر از عبارت «گیج نشوید» استفاده کرد.
دوروف پیش‌تر در ایکس خبر داده بود که روسیه به دلیل خودداری او از اجرای خواسته‌های این کشور برای نظارت گسترده و سانسور در تلگرام، نامش را در فهرست «تروریست‌ها» قرار داده است.
او همچنین به کنایه نوشت که بر اساس قوانین روسیه از «انتشار اطلاعات در اینترنت» منع شده است و افزود: «به نظر می‌رسد مقام‌های روسیه درباره اینکه چه کسی می‌تواند چه کسی را از اینترنت محروم کند، دچار سردرگمی شده‌اند.»
روسیه تنها کشور جهان است که رژیم طالبان را به رسمیت شناخته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77676" target="_blank">📅 19:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY0kfUujUQXIH80fjFQrYCVMbB3jGT4xFpa1bTSdSJxY1cicAbyujUZO00ekBLHKGBq4eMKT7Rc_z4_q_-rQ4F_SE6E5kHSFhwEfg4njRobqksSd77LgUJwVqVOb0AUaXUQTBEvFagGJw-Ne16GXVkjY2JO42JsSn7xheoIy93Fw6yIbwApDaB-Gy2Hi6V80EJ69Fj_TbcwpFoDLphAajxeJtfxoQeTX2nr5RoRduaUujFzntCpqqiSEzu0Qlv6btgee_hCP1gMuPJePOkVrVVD34FI0nUeML-eK2DDEg1IfAjQnovW453jatartBk8mzkKav0wEdojd6InzeeNBLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن عاملی، امام جمعه اردبیل، در خطبه‌های نماز جمعه این شهر گفت: «نتانیاهو در دیدار با ترامپ گفته قدر مرا بدان، من جلوی موشکهای جمهوری اسلامی را گرفته‌ام. ایران موشک هشت هزار کیلومتری دارد و به راحتی می‌تواند خانه تو را با موشک بزند. من جلوی ایران را گرفته‌ام.»
او ادامه داد: «ترامپ همیشه از نتانیاهو گول خورده و حالا محل بحث است که آیا این بار هم گول خواهد خورد یا نه.»
امام جمعه اردبیل افزود: «ترامپ پهلوان رسانه‌ای است، عملیات ما کمر او را شکست. او هر وقت شکست می‌خورد به جنگ رسانه‌ای پناه می‌برد و خود را پیروز میدان نشان می‌دهد. اگر این کار را نکند دق می‌کند و می‌میرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77675" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED5r97PDSvQneCS2-WrM4-tM4CQ_wr1Wzbd05GoYh2Fg69VXBZ0J_u8k-sLQ_rFk2yCgYK0h53Kpx2L6C53EVaV_N-uXYiu_xbmrttBmu3e_nbNqtgDCAVNOzTR94Q-dXRXhLBdVqYAPAmg8-zoBDlATR_zV222SnN8nDNXppaKtAk7fB4o01kPwFDOJ5PkwoB3SmlhQysxsyBtiwSqxhYyi2uH6Qvs9KOphjMObfM2FxfwHRlTTs_B1XbXK5EmYxFuY3VXefDPP6J5Vvm3hAL3DejxLFjUJO6ON-jJpm9MOJUDdURG6O1MuJfgATgJ-GUAByJT2klP_9sp2aMI6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس‌جمهور آمریکا، روز جمعه ۹مرداد۱۴۰۵ در گفتگو با شبکه «فاکس‌نیوز» گفت درگیری با ایران «به‌خوبی پیش می‌رود» و با اشاره به حملات ارتش ایالات متحده اعلام کرد که ایران در نهایت چاره ای جز عقب‌نشینی و تسلیم نخواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/77674" target="_blank">📅 19:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVHbvb6GZD6F3mso7D9DkUwpbxqD5eXFGmWlmc1GK9StArORua1NIAEUvLN9GFVR5Y-dG3h5XwLxQaMnylLFG8_jZ23S73JGhxP4_YR5s_DC2wzZclmP2OacALIZiOXgckHtznUUQkq5uKhdX5jyIgcP5dEEdznIAWqTb00bht8Bo198N7dF84clrLgNK44sX-gK3Qe7IWRPcPttieNeF_Ua3GJx-KcyQfdnsYPmNq9V8NEVSoC4aImhHnwGt6OfHDJ3hlOvDNscAbTQ8qBda7przyUf5LvMD_Hw9fSxLA9Pxfjtk-s9ri0kbaYujQpL8FyNx0xz-HJSkrWuxvKBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری آمریکا روز جاری و در میانه تشدید تنش‌های خاورمیانه، نشست کابینه خود را در اقامتگاه کمپ دیوید برگزار می‌کند.
این نشست در شرایطی برگزار می‌شود که دونالد ترامپ در تلاش است راهی برای پایان دادن به جنگ با ایران پیدا کند و همزمان قیمت بنزین را که به تهدیدی برای جمهوری‌خواهان در انتخابات میان‌دوره‌ای نوامبر تبدیل شده، کاهش دهد.
انتظار می‌رود سیاست خارجی و موضوع جمهوری اسلامی بخش عمده دستور کار این نشست را تشکیل دهد. ترامپ درگیر حملات متقابل علیه اهداف نظامی در ایران است.
ترامپ برخلاف برخی رؤسای جمهوری پیشین، در دوره ریاست‌جمهوری خود کمتر به این اقامتگاه کوهستانی ریاست‌جمهوری در غرب ایالت مریلند رفته، و این سومین سفر او به کمپ دیوید در دوره دوم ریاست‌جمهوری‌اش خواهد بود.
@
VahidHeadline
چون جمعه هم هست و بازارهای مالی تعطیل میشن باعث توجه بیشتر هم شده. دیشب، توییتر:
فردا ترامپ قبل از رفتن به باشگاه گلفش در بدمینستر، توقفی در کمپ دیوید داره. در هر دو باری که به کمپ دیوید رفته اتفاق خاصی افتاده. اولینش حمله بمب‌افکن‌های B-2 به نطنز بهمراه داشت، دومیش هم توافق با رژیم...
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77673" target="_blank">📅 15:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNbCzXINKn7siGDGWHWCcgX5i8cGqeNo_6x9K3WH-q1j00LRH6QsM3eOSdfiv8xfOOv6mVFbFy4sPr21KxqsmIAMMVnS3naVslrP_tWiQsXBfynOn7XAhIMv1Y5eUyWaH2HT0j3TST8GtL_3ujDeMZ5v6IJq3YDZQpwVdPRYHvZVCPtGxPeQd4Rf4Vud9wcu0T9zqCw4ocf3hG4Ft1YACK5OIifxmGVk1fHf-EpAwMpHf2hh27HSJjqCI6EPICgS7ehFrwnsl7_7RCfAq_mVsk_B0GwJaF_B6jLM53wZp1KfJyi44wR8NrTLsO9WdqyTGeaw92SFu9r8bpfjQTxl2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی رسمی وزارت دفاع کویت اعلام کرد نیروهای مسلح این کشور، بامداد روز جمعه نهم مرداد ماه، چند پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده و آنها را منهدم کرده‌اند.
سعود عبدالعزیز العتیبی در بیانیه‌ای در شبکه اجتماعی ایکس نوشت: «تجاوز گناه‌آلود ایران تعدادی از تاسیسات حیاتی و نظامی را هدف قرار داد که اهداف متخاصم رهگیری و منهدم شدند.»
او افزود: «در نتیجه سقوط ترکش‌ها، خسارت‌های مادی وارد شد، اما هیچ تلفات انسانی ثبت نشده است.»
پیش از این بیانیه، ارتش جمهوری اسلامی با انتشار اطلاعیه‌ای از حمله به پایگاه احمد الجابر، محل استقرار ارتش آمریکا با «پهپادهای انهدامی» خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/77672" target="_blank">📅 14:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi8DIpQyM9aUhNTdCdAKAjgGUew_Cu2kZDdhE-JYjyx_OdcBHw5U2XsBjbmP4zxEibTcHHEhiXTz1PPxrOqzkk7qI4XqpxLu6ksHlmRgzKNaQBguNR-FViuMtxrBolCvFEOrI8zbfof5BVeZBB44kCiCleQ1kRa9KnlTF819HlFPW7qFq7wImO6YlrwG70UKYXmzwiJXUcnbk079fxJ7sLkTMfyTxP6NiprAVtIH1B2KdDzWyGhNTuuUIUc84aqnWU3M6KotBiTuCmD-p0OYCF3KlDd2NcUh3fVipsuZl9esIqyueIra2yQwr6q5jxXOmRJzDeh1xfP3OCIyzX8QSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی، در پی اعلام فرماندهی مرکزی ارتش آمریکا مبنی بر تکذیب ادعای سپاه دربارهٔ بسته بودن تنگه هرمز، با انتشار بیانیه‌ای دیگر با پافشاری بر ادعاهای قبلی‌اش گفت به دو نفتکش دیگر حمله و آن‌ها را متوقف کرده است.
سپاه در کنار این بیانیه که روز جمعه نهم مرداد منتشر شد، همچنین تصاویری از یک نفتکش را که در میان شعله‌های آتش در تاریکی می‌سوزد منتشر و تاریخ آن را روز جمعه اعلام کرد.
سنتکام بعدازظهر پنج‌شنبه سه ادعای مطرح‌شده از سوی سپاه پاسداران و رسانه‌های نزدیک به آن دربارهٔ بسته بودن تنگه هرمز، انهدام سه جنگنده اف-۳۵ و عبور یک نفتکش ایرانی از محاصره دریایی آمریکا را را «نادرست» خوانده و گفته بود این ادعاها با واقعیت مطابقت ندارند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77671" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=ukRmTA_ri7SCOEXj9JLlIMDIajZspMvTY19af_hUSPb81TLLPsgpbrL1XMz6x4smL0PKhniixmKakGxPcdVSZl53NfBN2WVJTE7T6Ykgj5RVlq7POa7ThI09eFCQvnhUh8XL_1Onw0mundYLA8D_IsZsjv3Ztjh57L_dsvzLWf8EoOyjtMp7tDanhzVV3Mm4HMuVOtdYrYZiMjBdTfp3Y9HmMHmwW8O7tJmWbJw9LyM8gl0DDZRzwndqf_lrrToekKbuRKoFqf3F6SfuqkP0AZSipD2Ipjmbr0tXt6RuxYHF57VbGNiFmanOGoLuOM9V2qijrxtNoqcOkfcXzweq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f37e7edd3.mp4?token=ukRmTA_ri7SCOEXj9JLlIMDIajZspMvTY19af_hUSPb81TLLPsgpbrL1XMz6x4smL0PKhniixmKakGxPcdVSZl53NfBN2WVJTE7T6Ykgj5RVlq7POa7ThI09eFCQvnhUh8XL_1Onw0mundYLA8D_IsZsjv3Ztjh57L_dsvzLWf8EoOyjtMp7tDanhzVV3Mm4HMuVOtdYrYZiMjBdTfp3Y9HmMHmwW8O7tJmWbJw9LyM8gl0DDZRzwndqf_lrrToekKbuRKoFqf3F6SfuqkP0AZSipD2Ipjmbr0tXt6RuxYHF57VbGNiFmanOGoLuOM9V2qijrxtNoqcOkfcXzweq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌تر در صبح جمعه:
ارتش جمهوری اسلامی ایران مدعی شده است بامداد جمعه ۹ مرداد، پایگاه هوایی احمدالجابر در کویت را با پهپادهای انهدامی هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای اعلام کرد در این حمله، آشیانه جنگنده‌ها، سامانه‌های ارتباطات ماهواره‌ای و انبارهای تجهیزات ارتش آمریکا در این پایگاه هدف قرار گرفته‌اند. این ادعا تاکنون از سوی فرماندهی مرکزی آمریکا، سنتکام، یا مقام‌های کویتی تایید نشده است.
احمدالجابر یکی از پایگاه‌های مورد استفاده ارتش آمریکا در کویت است و در گذشته نیز ارتش جمهوری اسلامی بارها از حمله پهپادی به مواضع آمریکا در این کشور خبر داده است. در یکی از حملات پیشین، ارتش جمهوری اسلامی مدعی شده بود ساختمان‌های اداری و سامانه‌های جهت‌یاب در پایگاه عریفجان، محل استقرار بالگردها در اردوگاه العدیری و ساختمان استقرار نیروهای آمریکایی در احمدالجابر را هدف قرار داده است.
ارتش جمهوری اسلامی حمله ادعایی بامداد جمعه را واکنشی به حملات اخیر آمریکا به ایران توصیف کرده است. رسانه‌های ایران پیشتر از حمله آمریکا به بخش‌هایی از جزیره قشم و کشته شدن شماری از غیرنظامیان در این حملات خبر داده بودند.
با این حال، تا زمان انتشار این گزارش، مقام‌های آمریکایی و کویتی درباره وقوع حمله یا میزان خسارت احتمالی آن اظهار نظر رسمی نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77670" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Exs3af_Oz1Gy9cx-l3OkXhj1TAyh8tB1yjykVPZpYbcHxKkQ8LR2diVxHOgglZ8CrTqpmT2rrOz1a6VQY0r2y6KVbcX5H-CRQlmuf4qHSL9hRfWtGbNZUlya5P6pHALHS46PTZISu3OMD0-t4C05uDUO9ROlYCeuW-suCdMxplBCL45uvpdUwSzNTrMc9FD_ZXqx670YbKCvkXYn_5ac1uCmPsjfn1-7x6I7yW39MMEAgBKkf1aUSEsDox73Rl5A-1AkPHDubobrOdChNsPOGQ97iVz6WhN6o0gleaQ8oF3ZixOsi2oX50LfNsDjnkXH3W7Z9-K0Gce19z2Q7TPc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SjW-ZhVvbWzG4lTN7USdIXhYD6W7U3CbWljYxqlWmRVcoOx2Z6pTMWJ8A_e14qq01m8cuCp3bX7Rl9Ij6xXSpIz9-7Jfp8b-_ZidBuxLCA1vwbyNZ2PQUgbykY2PSXl-FfwvxdEFh-PDqnfXKfda_JZJGUpZfd59q1X09Lal97iWJLFOM_gXC27pZViN6euHYkOVhg0VI429LD9sKfnk5fsZA3GjOf1JFBV0b2GwW2aLqoYqgUbmSgC1HGSz2Rf2T938acJfTkoSSrUBlvptxlv2wVEe6scehL4VqRCO3q85C2tplj6_4Ohm79ql7kCvOCyHshPMHWd6KFHwOZJzrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ib7DsPExSkbahrSP4OV74drI3QZeXbdcJqy328nroIWfOyMhJqq1Ex6VjvzgF0otQn1ZZ2x4XNl13kNX_bUH_AobiXbBhBuHyKvd-G37NW7JOr_W5-xood82KrW1UzoJFkm1KhpwgbBCPJr-Wj76q8KKWnLbGR-lan1421PcP2Oh5BPGTT2r8Y6sKIkreSL4sboOJSFZb8KfYELSIfNVl8pluercFuDLIZG07y7YJNRl4xKmnU6DsfgPMngj6UNStqh3oNQBT22Cmrd4UYdjILXFaYtfM4uwaaym0O0RTv_UF19HGIukJtXVBPWS7l-i1FXfesuFkSAOL-0y4Werag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HiLDRKASBrH1YKu9Jv37zH7mF-BMQm9zeYyJEthUU_H69XhcSA_5rgwjk71OWjt9ZgtsPJPXKsG53S73wVYyLi7l7a3BS0qvIglbMj5Z0tfC3OnQYdyS5vDN6YvfR1GS1mXp2enM93JkAehcAvapHb9DdmfVZ4SeAoUZ6na9ssRYy-HWR0t6QVUF2ejXd9ra5HSd1HDEUH7qXo7to6S4S5fJKJiBuiZI0AZFKfZjnY9078KzKRw6mZ8Df2HNLao38XJ3bCfSRyHCTVslPHsfV8HvFVOHtJygWZRlKHfL2kImGUF_wg1gJhetu8Ejf_C415uacFakEzIo5MnMY7t1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nx-k_h4GeSVehWYcCdCLIqbhEHP18mRgtjGNmoa_EpBlw3vM2mGSLKvYk70D5wJfJ1o5_B2Ztc3USjHsEK3gZpT5g_0CZh4Vvcog1MNt3rx0teVh_2AWd-p36gAmgo8P3En3e5dWYVGoohIjRYZC6gVerKwzaaEH-XITjl4bBaWjzW7frEk9crv2JzpkR_O1vfLslRKeAHcHfEAHIL7ok2GyVgvITYYn3zvwHnHxteD7RVw3M7HYmjhyHTAX0oOs-h-7vt_yBTbNWiAHSqKzJCcJOjb5uSJYivnZgBvpHfc96kf42mUqLZbGu1wdr_qaM8aIwpiJQ2oOJxhcOA6LlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=i9Q_a59Aqp7qrmRh5ftNyRwp7BFTBadSwbqmxMMrS8AARervPn--kg9ObruNB2oeP8VHZtcuy__zIZOHXHS5YLTTbnOe3Ud_36rcfisp5XyZwvKEZx-Bc0UgT6LxpkkkF-J_NuKV4abeXihhj9-OwHo6h-33jbwPRh5V4ir5CqZPOD4uvhidGvuYQFPUd0Ese3lEb5jfks87FOG7G70ZhfQ4XrQ-3zff84CAkfxsheMv_im1Y-q8a2h8zL8IiN333UWrtscis_-hgprlUDCCCLr5Wbh7rvWhLBAvWCApXRLlmmRo4KsrNzwP_b-plpUn2RPV7bCvtAg0EeJNNzGWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36c757e90b.mp4?token=i9Q_a59Aqp7qrmRh5ftNyRwp7BFTBadSwbqmxMMrS8AARervPn--kg9ObruNB2oeP8VHZtcuy__zIZOHXHS5YLTTbnOe3Ud_36rcfisp5XyZwvKEZx-Bc0UgT6LxpkkkF-J_NuKV4abeXihhj9-OwHo6h-33jbwPRh5V4ir5CqZPOD4uvhidGvuYQFPUd0Ese3lEb5jfks87FOG7G70ZhfQ4XrQ-3zff84CAkfxsheMv_im1Y-q8a2h8zL8IiN333UWrtscis_-hgprlUDCCCLr5Wbh7rvWhLBAvWCApXRLlmmRo4KsrNzwP_b-plpUn2RPV7bCvtAg0EeJNNzGWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۰:۳۷ درباره پرتاب موشک از یزد
همین الان از یزد موشک فرستادن ساعت10:37
۱۰:۳۵ پرتاب موشک از یزد
سلام الان موشک زدن از یزد
از یزد موشک بلند شد ۱۰:۳۷
از یزد موشک زدن الان
وحید جان همین الان ساعت ۱۰.۳۲ پرتاب موشک از یزد
وحید جان همین الان از یزد موشک زدن
جمعه ساعت ۱۰:۳۶
یزد ۱۰:۳۵ یه موشک زدن
بعد از مدت ها جالب بود سمت جنوب پرتاب شد
همین الان از یزد موشک شلیک کردن
۱۰:۳۷از یزد موشک زدن
همین الان از یزد موشک زدن
جمعه نهم امرداد ساعت۱۰/۳۰
سلام وحید جان همین الان از یزد موشک پرتاب شد
سلام خوبین الان موشک از یزد رفت
شلیک  یک موشک الان از یزد
وحید الان موشک از کشور یزد زدن
همین الان ساعت ۱۰.۳۶ دقیقه از یزد موشک زدن
شلیک موشک از یزد به سمت جنوب
ساعت ۱۰.۳۶
سلام ساعت ۱۰:۳۵ یک موشک از یزد بطرف جنوب کشور شلیک شد
از یزد موشک شلیک کردن ولی مسیر متفاوت از قبل بود
سمت بندر و جنوب میرفت
ساعت ۱۰:۴۰ صبح یزد  موشک پرتاب شد؛ صداش خیلی بلند بود
سلام جمعه ساعت ۱۰:۴۰ از یزد موشک پرتاب شد
۱۰:۳۷ از یزد موشک زدن جمعه ۹مرداد
سلام آقا وحید ۱۰:۴۲ از یزد موشک شلیک کردن
موشک از یزد زدند
وحید جان شلیک موشک از یزد
چند دقیقه پیش
ساعت ۱۰:۳۵ از یزد موشک زدن
از یزد همین الان موشک زدن
امروز جهتش سمت جنوب شرق بود
بر عکس روزای قبل که روی شهر رد میشد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77663" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اکسیوس:
ترجمه ماشین:
ترامپ از توافق «تاریخی» برای خلع سلاح حماس و بازسازی غزه تمجید کرد
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه اعلام کرد که «هیئت صلح» او با حماس به توافقی دست یافته است که بر اساس آن، این گروه خلع سلاح می‌شود و کنترل امور غیرنظامی و امنیتی غزه به یک دولت جدید فلسطینی متشکل از تکنوکرات‌ها واگذار خواهد شد.
چرا اهمیت دارد:
در صورت اجرا، این توافق تحولی چشمگیر در طرح صلح ۲۰ ماده‌ای ترامپ برای غزه خواهد بود و مسیر بازسازی این منطقه ویران‌شده را هموار خواهد کرد.
▪️
اما این توافق مستلزم آن است که حماس و اسرائیل طی حدود هفت تا هشت ماه، مجموعه‌ای پیچیده از اقدامات متقابل و مستقل را که اجرای آن‌ها راستی‌آزمایی خواهد شد، به انجام برسانند.
▪️
مقام‌های اسرائیلی همچنان به‌شدت تردید دارند که حماس سلاح‌های خود را تحویل دهد؛ در همین حال، اظهارات یک مقام ارشد حماس نشان می‌دهد که ترتیب خلع سلاح و عقب‌نشینی اسرائیل همچنان ممکن است محل اختلاف باشد.
آنچه می‌گویند:
ترامپ عصر پنج‌شنبه در شبکه تروث سوشال نوشت: «امروز، هیئت صلح به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی گروه‌های مسلح دیگر در غزه دست یافت.»
▪️
او افزود: «این گامی عظیم به‌سوی صلح و امنیت پایدار است.»
وضعیت کنونی:
دو مقام آمریکایی گفتند حماس پس از چند ماه مذاکره با میانجی‌گری قطر، ترکیه و مصر که یک مقام ارشد دولت آمریکا آن را «بسیار حساس» توصیف کرد، با مفاد توافق موافقت کرده است.
▪️
این مقام ارشد آمریکایی گفت انتظار می‌رود اجرای توافق طی هفته‌های آینده آغاز شود.
▪️
یکی از مقام‌های هیئت صلح گفت این نخستین بار است که حماس و دیگر گروه‌های فلسطینی در غزه با غیرنظامی‌کردن این منطقه و واگذاری مسئولیت امنیت و خدمات غیرنظامی به یک دولت تکنوکرات موافقت کرده‌اند.
بر اساس این توافق،
حماس از هرگونه نقش در اداره غزه صرف‌نظر خواهد کرد. «کمیته ملی اداره غزه» موسوم به NCAG به‌عنوان جایگزینی برای حماس و تشکیلات خودگردان فلسطینی فعالیت خواهد کرد.
▪️
مقام ارشد آمریکایی گفت: «این ساختار به نفع مردم غزه خواهد بود.»
بررسی واقعیت:
غازی حمد، از مقام‌های حماس، در گفت‌وگو با الجزیره تأیید کرد که مذاکرات «دشوار» به توافق منجر شده است، اما توضیحات او بلافاصله پرسش‌هایی را درباره نحوه اجرای آن مطرح کرد.
▪️
حمد گفت: «ما پیش از عقب‌نشینی اسرائیل از نوار غزه هیچ اقدامی در زمینه خلع سلاح انجام نخواهیم داد.» او افزود که کمیته ملی اداره غزه بدون دخالت اسرائیل خلع سلاح را اجرا خواهد کرد.
▪️
این موضع ظاهراً با توصیف ترامپ از یک روند مرحله‌ای و «با ساختاری دقیق» تفاوت دارد؛ روندی که در آن، هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی می‌کنند.
▪️
مقام‌های آمریکایی و هیئت صلح گفتند اجرای توافق از طریق اقدامات متقابل و مستقلی که راستی‌آزمایی می‌شوند پیش خواهد رفت، هرچند اذعان کردند که جدول زمانی عقب‌نشینی اسرائیل هنوز در حال نهایی‌شدن است.
تصویر کلی:
بخش‌های وسیعی از غزه در جریان جنگ ویران شده و بیشتر جمعیت دو میلیون نفری آن همچنان در چادرها یا سرپناه‌های موقت زندگی می‌کنند.
▪️
مواد غذایی و دیگر کمک‌ها در حجم زیادی وارد غزه می‌شود، اما وضعیت انسانی همچنان وخیم است.
▪️
وزارت بهداشت غزه که تحت کنترل حماس است می‌گوید از زمان آتش‌بس ۱۰ اکتبر ۲۰۲۵، نزدیک به ۱۲۰۰ فلسطینی کشته شده‌اند. برخی از آن‌ها از نیروهای حماس بودند، اما بسیاری دیگر غیرنظامی، از جمله کودکان، بوده‌اند.
نگاهی نزدیک‌تر:
این توافق بر این اصل استوار است که غزه باید یک دولت، یک نظام حقوقی و یک مرجع امنیتی مشروع داشته باشد. انتظار می‌رود روند غیرنظامی‌سازی بین ۲۰۰ تا ۲۵۰ روز طول بکشد و هر بار در یکی از بخش‌های غزه اجرا شود.
▪️
پلیس غیرنظامی حماس ابتدا سلاح‌های خود را به یک نیروی پلیس جدید فلسطینی زیر نظر دولت تکنوکرات تحویل خواهد داد.
▪️
پس از آن، سلاح‌های سنگین حماس از رده خارج و در انبارهای امن نگهداری خواهد شد و تونل‌ها و کارخانه‌های تولید سلاح این گروه برچیده خواهد شد.
▪️
سلاح‌های سبک مطابق قوانین فلسطینی جمع‌آوری خواهد شد.
▪️
تمامی گروه‌های شبه‌نظامی دیگر در غزه، از جمله گروه‌های مخالف حماس که اسرائیل در جریان جنگ آن‌ها را مسلح کرده بود، نیز ملزم به تحویل سلاح‌های خود خواهند بود.
کمیته ملی اداره غزه
تنها زمانی کنترل هر منطقه را در دست خواهد گرفت که یک سازوکار نظارتی تأیید کند تعهدات مربوط به آن منطقه اجرا شده است.
▪️
مقام هیئت صلح گفت در پایان این روند، دولت تکنوکرات و نیروی پلیس آن انحصار سلاح در غزه را در اختیار خواهند داشت.
نحوه اجرا:
بر اساس توافق، یک نیروی بین‌المللی تثبیت‌کننده به آموزش پلیس جدید فلسطینی کمک خواهد کرد، در جمع‌آوری سلاح‌ها مشارکت خواهد داشت و میان مناطق تحت کنترل فلسطینی‌ها و نیروهای اسرائیلی مستقر خواهد شد.
▪️
یکی از مقام‌های هیئت صلح گفت این توافق بر مبنای «اعتماد صفر» طراحی شده است، زیرا حماس و اسرائیل از همان ابتدا به‌صراحت اعلام کردند که به یکدیگر اعتماد ندارند.
▪️
این روند تا زمانی که ناظران تأیید نکنند هر دو طرف به تعهدات خود عمل کرده‌اند، از یک مرحله به مرحله بعدی منتقل نخواهد شد.
▪️
این مقام گفت هدف آن است که از وضعیتی جلوگیری شود که دولت تکنوکرات در طول روز غزه را کنترل کند، اما گروه‌های مسلح شب‌ها همچنان قدرت را در دست داشته باشند.
طرف مقابل:
عقب‌نشینی اسرائیل به‌تدریج و بر اساس جدول زمانی‌ای انجام خواهد شد که هنوز در حال نهایی‌شدن است.
▪️
ترامپ گفت هم‌زمان با تکمیل خلع سلاح و برعهده‌گرفتن مسئولیت امنیت از سوی نیروی بین‌المللی و پلیس جدید فلسطینی، نیروهای اسرائیلی عقب‌نشینی خواهند کرد.
▪️
اسرائیل همچنین عملیات نظامی و ترورهای هدفمند در غزه را متوقف خواهد کرد، مگر در مواردی که تهدیدی قریب‌الوقوع وجود داشته باشد.
▪️
مقام هیئت صلح گفت: «تمامی فعالیت‌های نظامی در غزه باید متوقف شود؛ چه از سوی اسرائیل و چه از سوی حماس.»
پشت درهای بسته:
مقام ارشد آمریکایی گفت دولت ترامپ در تمام طول مذاکرات هماهنگی نزدیکی با اسرائیل داشته است.
▪️
دولت آمریکا همچنین قصد دارد با وجود تردید اسرائیل درباره خلع سلاح حماس، اطمینان حاصل کند که اسرائیل به تعهدات خود در چارچوب توافق عمل می‌کند.
▪️
این مقام گفت: «ما از اسرائیل چیزی جز اجرای تعهداتش در چارچوب طرح ۲۰ ماده‌ای نمی‌خواهیم.»
▪️
او افزود: «اگر آن‌ها این کار را انجام ندهند، رئیس‌جمهور ترامپ بسیار ناامید خواهد شد. فکر نمی‌کنم اسرائیلی‌ها در شرایط کنونی بخواهند تنش‌ها با ما را تشدید کنند.»
در پشت صحنه:
به گفته دو منبع آگاه از مذاکرات، مصر، قطر و ترکیه فشار شدیدی بر حماس وارد کردند تا این توافق را بپذیرد.
▪️
مقام‌های آمریکایی و دیگر افراد آگاه از مذاکرات گفتند حسن رشاد، رئیس دستگاه اطلاعاتی مصر، نقشی کلیدی داشت. او میزبان مذاکرات بود و رابطه نزدیکی با خلیل الحیه، رهبر سیاسی حماس، دارد.
نکته قابل‌توجه:
به گفته یک منبع آگاه از این دیدار، هیئتی از حماس در جریان سفر اخیر خود به ایران برای شرکت در مراسم تشییع علی خامنه‌ای، رهبر پیشین جمهوری اسلامی، با مقام‌های ارشد سپاه پاسداران انقلاب اسلامی دیدار کرد.
▪️
این منبع گفت مقام‌های سپاه از حماس خواستند برای امضای توافق عجله نکند و با وقت‌کشی زمان بخرد.
▪️
یک مقام ارشد آمریکایی نیز مدعی شد ایران تلاش کرده است حماس را متقاعد کند که توافق را امضا نکند، اما گفت این گروه تصمیم گرفت به توصیه ایران گوش ندهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/77662" target="_blank">📅 06:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eJRB_QszccHzjOP67LyKVFImJoGQ-WdytRuT08pwGXK3Kb7hdSV1yp_WCeu0wcnRRUwsd0_mMYn0r-j1cqacjajtiOfiaBQ9swrgQ_qSLIuNayX1T01Ay9uKQIGaQ4c_ayjKQmFcdGa3sN_oiPMIDPNgKIcRyWp6-AHUDc8tw6mFvG6z5qWPdK7O51UAGpYTSx7y7n-99ysQS6JMu_ZfTLOaH88xgnrcJnFQZTCQdEXVUXBm_BsE4pbIKmfccu-o98GGi8hZuoxu1hB7SNNyUM-6QLEQ24En1TLRf1CK_7g9yfzx5GZf6aUdOkzh-irp_b-BF9h97--tzn8ZlnQH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
امروز، «هیئت صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و همه گروه‌های مسلح دیگر در غزه دست یافت. این گامی عظیم به‌سوی صلح و امنیت پایدار است.
این توافق، گامی حیاتی در مسیر آن است که غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای کمک به مردم فلسطین، از نزدیک با هیئت صلح همکاری خواهد کرد. هم‌زمان، اسرائیل نیز از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به‌عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این توافق، نقطه عطف بزرگی در اجرای طرح ۲۰ ماده‌ای ترامپ است. این توافق در مراحلی که با دقت طراحی شده‌اند اجرا خواهد شد. هم‌زمان با تکمیل خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات» با یک نیروی پلیس جدید فلسطینی همکاری خواهد کرد تا مسئولیت تأمین امنیت غزه برای ساکنان آن و همسایگانش را بر عهده بگیرد.
یک سال پیش، جنگی خشونت‌بار و مهارنشدنی، بحرانی انسانی و گروگان‌هایی در اسارت وحشیانه وجود داشت. ما پیشرفتی تاریخی کرده‌ایم و هنوز کارهای زیادی باقی مانده است.
می‌خواهم از میانجی‌ها—مصر، قطر و ترکیه—به‌خاطر تلاش‌های مهمشان تشکر کنم، و به‌ویژه از تیم فوق‌العاده‌ام که تلاش خستگی‌ناپذیرشان این دستاورد تاریخی را ممکن کرد.
تهدیدی که در ۷ اکتبر از غزه سر برآورد، اجازه نخواهد یافت دوباره شکل بگیرد!
بر اساس این توافق، غزه سرانجام در اختیار یک دولت جدید فلسطینی قرار خواهد گرفت که به مردم خود خدمت می‌کند.
این تحول شگفت‌انگیز را که همه می‌گفتند هرگز دست‌یافتنی نیست، به همگان تبریک می‌گویم!
دونالد جی. ترامپ
رئیس‌جمهور ایالات متحده آمریکا
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77661" target="_blank">📅 02:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-2E9VOs6qkwrBrNm2sGPnWwFD-T0XHX19z9JU1eUd1UU2RLc_16NpWitQ6l8p66Lb7lNitvgXJnluHD0b-QCa09hBjbmTbReErHZxi5Sia7WFj0HGdsTfdOlxJ5s0ukqcd9c9CsZ2TNnqt01nvtF6zflzRjo6JvulJaDiYtpDHCFEwKmsg2JGcpjQqQ6TNoul7zfkx0hm1CjI-WzOHIFeVdHYG0lt41QaeRGsKqK2kjUf7rlCJNLySAyqVt7DvENOsEA90eqJoICOKaJQOk2fNNmi1lZ8KRgCQU95L9p6DQDcQMMVg6yB2jWLSbAHu3Sw7aGdru74QUtHHPjFuOdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، با انتشار پیامی در شبکه اجتماعی اکس اعلام کرد افرادی که به سپاه پاسداران انقلاب اسلامی یا هواپیمایی ماهان خدمات مالی، پشتیبانی لجستیکی یا حمایت تجاری ارائه می‌کنند، به تداوم فعالیت یک سازمان تروریستی کمک می‌کنند.
او افزود وزارت خزانه‌داری آمریکا به شناسایی این افراد، افشای هویت آن‌ها و قطع دسترسی‌شان به نظام مالی ایالات متحده ادامه خواهد داد.
پیش از این، وزارت خزانه‌داری آمریک، شش فرد و نهاد در ایران، چین، هند و روسیه را به دلیل همکاری با هواپیمایی ماهان و سپاه پاسداران تحریم کرده بود. واشنگتن اعلام کرده بود برخی از شرکت‌های تحریم‌شده به‌عنوان نمایندگان فروش هواپیمایی ماهان فعالیت می‌کردند و در حفظ شبکه بین‌المللی این شرکت نقش داشتند. وزارت خزانه‌داری آمریکا همچنین شرکت «استودیوی استارت‌آپ داده‌نگار» را به اتهام همکاری با سپاه پاسداران تحریم کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/77660" target="_blank">📅 02:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
مصر دوست و شریکی مهم برای ما در منطقه است و امنیت آن برای ما از بالاترین اهمیت برخوردار است.
همه ما باید در برابر توطئه‌های اسرائیل و عملیات‌های پرچم دروغین که برای تضعیف صلح منطقه‌ای طراحی شده‌اند، هوشیار باشیم.
تهدید روشن و مشترک است و از همبستگی مسلمانان هراس دارد.
araghchi
پست قالیباف:
ایالات متحده هر روز دست خود را به جنایت جدیدی آلوده می‌کند؛ حملهٔ تروریستی به منازل مسکونی غیرنظامیان در جزیرهٔ قشم، ادامهٔ جنایات در میناب و لامرد است.
امریکایی‌ها عادت کرده‌اند که سیلی‌هایی را که در میدان نبرد می‌خورند با ریختن خون بی‌گناهان جبران کنند. تاوان‌ خواهند داد.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77659" target="_blank">📅 23:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ6twUlfS_7lPWN3DOc1aLaq48Hc4GcJk1TwlTV8eDHpbIv1ZIj4aWh0lXLgEaHQYmpVFkzWGXBU-Ex-dA55Y0GW3oPJIWzKOyoMSxtaWvalfUU1SmBwG1fR60GD0aOib7o0PWSyxtfEieVVY3N0GafJLHiyT_OOrf9sY9NgbK3FO18oYUXfL5k-iK1Xdm4012Uk1KDhFiPu_gzGNOhjxFguU0mku6rbCXnGddwXp8XuKjiuDcDE0BKfkZKyUBtfQ15kmHe5WgvVZpONgnE3I8gbq2L7Txm_Rz-VY2Hsehqdl6KkUlqXewCHPFCvGi8Odoeh5ENGg5z76JM_HO7EgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی روز پنج‌شنبه از طرح تشکیل یک ائتلاف بین‌المللی برای دفاع دریایی با هدف حفاظت از کشتیرانی و مسیرهای انتقال انرژی در دریای سرخ خبر داد.
وزارت دفاع عربستان اعلام کرد نمایندگان ۴۳ کشور و اتحادیه اروپا در نشستی درباره این طرح شرکت کردند. بر اساس این پیشنهاد، عربستان به‌عنوان کشور بنیان‌گذار و رهبر ائتلاف عمل خواهد کرد و مقر آن نیز در این کشور خواهد بود.
به گفته وزارت دفاع عربستان، این ائتلاف با هدف تقویت امنیت دریایی، حفظ آزادی کشتیرانی، تأمین امنیت مسیرهای تجارت و انتقال انرژی و حفاظت از منافع مشترک دریایی در تنگه باب‌المندب و خلیج عدن تشکیل می‌شود.
این طرح پس از آن مطرح شده که حملات حوثی‌های مورد حمایت ایران به کشتی‌ها، یکی از مهم‌ترین مسیرهای تجاری جهان را با اختلال روبه‌رو کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/77658" target="_blank">📅 22:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=kcF3XIaAEsiAz7Ey05v3VLSnlrDHHp-BbLlmCJZe7USlWCPk_Nx9PLxkRnSH54vRZhWcdwSxhUjoP8l2wg2KAOwwTwFoPQdcAeqoLA_bOTk3lH4p1sBY7kqoNY86LzwfGeqBWTsn3R1VuDWSxRktaYRrrNTBKY9ZMLbS9OAIY1R9B8a9fp1BnPZpwbPcyYyKK0avnHT2O5tRPLERMLunDQDPjav0QUaBXW2fz-jIe6a3Y5CpTU4cpXxkPWu-T45TorISfAvD7P8h9grWlUMb7b0KYY1ciJQT4X7SwxOhHucfN20B8TRVR-DinfsG90gb4a69OOWPQpaI3NjJlFJrOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b839da73e3.mp4?token=kcF3XIaAEsiAz7Ey05v3VLSnlrDHHp-BbLlmCJZe7USlWCPk_Nx9PLxkRnSH54vRZhWcdwSxhUjoP8l2wg2KAOwwTwFoPQdcAeqoLA_bOTk3lH4p1sBY7kqoNY86LzwfGeqBWTsn3R1VuDWSxRktaYRrrNTBKY9ZMLbS9OAIY1R9B8a9fp1BnPZpwbPcyYyKK0avnHT2O5tRPLERMLunDQDPjav0QUaBXW2fz-jIe6a3Y5CpTU4cpXxkPWu-T45TorISfAvD7P8h9grWlUMb7b0KYY1ciJQT4X7SwxOhHucfN20B8TRVR-DinfsG90gb4a69OOWPQpaI3NjJlFJrOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر جاویدنام آیدا حیدری، جوان معترض کشته‌شده به دست حکومت، در سالروز تولدش بر مزار او می‌گوید که آیدا حیدری «شیرزنی» بود که جانفدای میهن شد.
آیدا حیدری، دانشجوی رشته پزشکی دانشگاه علوم پزشکی تهران، در ۱۸ دی‌ماه ۱۴۰۴ در تهران با شلیک گلوله جان باخت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77657" target="_blank">📅 20:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=CE-fC5XlTR3eG7CjMW4tFiZ6dXxgsM5H3ohCdayDzTrQgc5DdtxJUeW0lLSc3pcajxmZfqe6yKpwDvtWy8k_5wmMdhyPsbzFjl_fCw5qTFyQHoX7Tx0I6OlzJi5H_wMfAYNH6qPQoT5Mt_T2lGKRUWL-RJbnrzRn8bLTrGYOmvO4yuw3NHtfA0Y8jlBmT5tjDrMwxl9_n8C_lV9EvNqr67qfoKCW8ZOalTUCjFpJToRz00QKV27ESBhSTL-XA2btk3Jgu86Fgo_Yry4w9CCwG5eB5eTTqDkXTl3V9vrcGcL0v3M-vttv8jOAFUfv7DO7OKUsbqBmGvSHgnRqPqnFYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9d7d99f314.mp4?token=CE-fC5XlTR3eG7CjMW4tFiZ6dXxgsM5H3ohCdayDzTrQgc5DdtxJUeW0lLSc3pcajxmZfqe6yKpwDvtWy8k_5wmMdhyPsbzFjl_fCw5qTFyQHoX7Tx0I6OlzJi5H_wMfAYNH6qPQoT5Mt_T2lGKRUWL-RJbnrzRn8bLTrGYOmvO4yuw3NHtfA0Y8jlBmT5tjDrMwxl9_n8C_lV9EvNqr67qfoKCW8ZOalTUCjFpJToRz00QKV27ESBhSTL-XA2btk3Jgu86Fgo_Yry4w9CCwG5eB5eTTqDkXTl3V9vrcGcL0v3M-vttv8jOAFUfv7DO7OKUsbqBmGvSHgnRqPqnFYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
در چند ساعت گذشته، رسانه‌های دولتی ایران همچنان ادعاهای دروغین سپاه پاسداران انقلاب اسلامی را منتشر کرده‌اند؛ به‌ویژه سه ادعای زیر:
🚫
ادعای نخست: سپاه پاسداران بار دیگر ادعا می‌کند که مسیرهای آزاد و باز عبور از تنگه هرمز برای کشتی‌های تجاری خطرناک است.
✅
واقعیت: خطرهای فوری برای کشتی‌های تجاری و خدمه غیرنظامی آن‌ها، تهدیدهای لفظی و تلاش‌های سپاه پاسداران برای حمله به آن‌هاست.
🚫
ادعای دوم: سپاه پاسداران مدعی است سه جنگنده رادارگریز اف-۳۵ آمریکا و سه هواپیمای دیگر در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✅
واقعیت: در تلاش‌های اخیر ایران برای حمله، هیچ هواپیمای آمریکایی منهدم یا آسیب‌دیده نشده است. همه موشک‌ها و پهپادها رهگیری شدند یا نتوانستند به مناطق هدف برسند.
🚫
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام M/T Nora محاصره آمریکا را شکسته است.
✅
واقعیت: این کشتی تجاری نتوانسته از محاصره «دیوار فولادین» آمریکا عبور کند. بیش از ۲۰ ناو جنگی آمریکا، صدها هواپیما و هزاران نیروی نظامی همچنان در آماده‌باش هستند و اجرای کامل محاصره را ادامه می‌دهند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/77656" target="_blank">📅 19:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ldOqEV5cwKljeQlYJdQxfVGPdwdyMMb2Fl7zDL58TCQscNSZ46_9MXbd4q9mNwhg9DoZowP5dZyAviLm6z56NfkOC82rXwh5p4vgcYKbkWNEatb4UKC_dOis0A5KQ0QjIQFqsl1dV5gVozHCvtS6ONHpY4zrGjzmKxHS2KVOAJG-AGCBlB04Y0WCYbgr3rGNUvbd5vM1hYacEPdtAQ_Dhv7lH_5jjzjD0KEdrcOBoq-67QWUIpiNIfYt3XTfSzVlxjaJI3W6QKcVeK5JVCpCuZ6TC2GApN1a7olq_pzra48OnpxX1n2G4jPWJJBn9iIbFgYXpLMIkBXR8ZwkjOFUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=gCkh5bJQsxfUdqRaAecEQbLfqYA2ZbRd4PVI16sLZke-PtTTJgT2gsiugH6Ob0o9URp5_vimCUReuSJi-nNBiiCec3vrw5sET4UwyL2WlYaQJWpduzKO4Aj7g-sXPZzF6Gry7HkYTlCQ8EE6RjXDCm_3t7TGLSyPmgfQerAe_1_3xt7EuUakISdcMXTqsoCOgq6hdTCi8utM-HAljA9BlwDxnvZM2T928mZd83sLKP40lFvG-DwcTkyrL5PqQdvPFwHAAyv2upmKbc31ETdjSsc53MoNjZfsGis22syL5Gcl3ApSu76zclFnq9WIUe4AzWoepFde5p9ypnhJXe-LgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/032c2aacd6.mp4?token=gCkh5bJQsxfUdqRaAecEQbLfqYA2ZbRd4PVI16sLZke-PtTTJgT2gsiugH6Ob0o9URp5_vimCUReuSJi-nNBiiCec3vrw5sET4UwyL2WlYaQJWpduzKO4Aj7g-sXPZzF6Gry7HkYTlCQ8EE6RjXDCm_3t7TGLSyPmgfQerAe_1_3xt7EuUakISdcMXTqsoCOgq6hdTCi8utM-HAljA9BlwDxnvZM2T928mZd83sLKP40lFvG-DwcTkyrL5PqQdvPFwHAAyv2upmKbc31ETdjSsc53MoNjZfsGis22syL5Gcl3ApSu76zclFnq9WIUe4AzWoepFde5p9ypnhJXe-LgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی قدیمی منتشرشده در شبکه‌های اجتماعی رقص علیرضا سپاهی در اصفهان را نشان می‌دهد.
قرار بود او بامداد سه‌شنبه اعدام شود اما پیش از انتقال به محل اجرای حکم دچار سکته قلبی شد و به بیمارستان الزهرای اصفهان انتقال یافت.
@
VahidOOnLine
یک شاهد عینی گفت پس از انتقال علیرضا سپاهی، معترض محکوم به اعدام، به بیمارستان الزهرا اصفهان، فضای بخشی از این بیمارستان امنیتی شده و شماری از ماموران امنیتی در آن مستقر شده‌اند.
بامداد سه‌شنبه، ابوالفضل سپاهی بادجانی و امیرحسین صفری حسین‌آبادی، دو نفر دیگر از بازداشت‌شدگان اعتراضات ۱۸ و ۱۹ دی‌ماه ۱۴۰۵ در اصفهان، با حکم دادگاه انقلاب اسلامی اصفهان اعدام شدند. ابوالفضل سپاهی بادجانی، پسرعموی علیرضا سپاهی بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77654" target="_blank">📅 19:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebec49421.mp4?token=ueH4yBocM0MJOqMbdMkVK82FPZkjCflxVbjIsAQkJbDAi3t3y8npVhmbVNnzJuF-sjw4OW_g2NQNCVP8rXEp5ZQZGq0ws381qEhQfyGhZMLFQIbgWtn2Htvl3P7MJj81zjeHyc1pnmkloEW1IRjpFrKASzImzFFKkz8MUMSlRIOIeJzpLjP1NTumouXbeHVSCXPg8oq3KRce342IslUtzDW2mpXaEAVC1Gurg4NDRrl7clXhmra7pbwJ3qMDrp6OPoB3hZo0MIGmn5C-ka6zBOfCQpBqAmCtlxMYZIgVbnyu4QAFLPtiRSPJUiMzHvCJh5b25YYk4HT2JUmMJTBXsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebec49421.mp4?token=ueH4yBocM0MJOqMbdMkVK82FPZkjCflxVbjIsAQkJbDAi3t3y8npVhmbVNnzJuF-sjw4OW_g2NQNCVP8rXEp5ZQZGq0ws381qEhQfyGhZMLFQIbgWtn2Htvl3P7MJj81zjeHyc1pnmkloEW1IRjpFrKASzImzFFKkz8MUMSlRIOIeJzpLjP1NTumouXbeHVSCXPg8oq3KRce342IslUtzDW2mpXaEAVC1Gurg4NDRrl7clXhmra7pbwJ3qMDrp6OPoB3hZo0MIGmn5C-ka6zBOfCQpBqAmCtlxMYZIgVbnyu4QAFLPtiRSPJUiMzHvCJh5b25YYk4HT2JUmMJTBXsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدار خانواده جاویدنام محسن رشیدی خانی‌آبادی و علی ایازی با خانواده عرفان اسفندیاری و امیر حسین صفری ـ گزارشگر (ویدیو صدا ندارد)
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77653" target="_blank">📅 19:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDhyPWMCDArrwtBXAo4jgGQ9WEPDVs2NCqoyGJzzPp9vVT8nAXAYlyXpIdjVDLimmof7_DS6rngv1TJQ0TZNKSBcvF0LeQ8agCNzHac5W8R4AxH_VP7WSSQGKDMWJcZqA3yXuMgve2BvVjJeZXzq7_e9mccQhPhor7m-8pquVcu-cGwNvsvb2C84ov6QX76nnOZ5RSeffAWGIf3Xl-YKyQPxQGlfiZAISkXatsEOOXp3czPW5vOnEbIy_xBZb1K-ju0X8iJrPEe9HUhJxuhKMZEE0aKypQVvGGwti6EM6v1XCdju0JuFjMp_zVI1luK4dkGnnl2b85ur111aVOfGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ان‌بی‌سی نیوز روز پنجشنبه هشتم مرداد، به نقل از یک مقام آمریکایی گزارش داد که دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در جریان نشستی در هفته گذشته از فرسایشی شدن جنگ، محدودیت گزینه‌های نظامی علیه ایران و دست نیافتن به توافق خشمگین شده و بر سر مشاورانش فریاد کشیده است.
به گفته این مقام مسئول، بر خلاف اظهارات عمومی ترامپ مبنی بر رضایت از روند جنگ، نه او و نه مشاوران ارشدش از وضعیت موجود راضی نیستند. یکی از متحدان ترامپ در این باره گفت: «رئیس‌جمهور کلافه شده است؛ او تصور نمی‌کرد گرفتن امتیاز از ایران تا این حد دشوار باشد و هیچ راهبرد مشخصی برای چگونگی رسیدن به نقطه پایان وجود نداشت.»
این گزارش می‌افزاید نبود شفافیت درباره اهداف نهایی واشنگتن—از جمله این‌که آیا هدف اصلی جلوگیری از دستیابی ایران به سلاح هسته‌ای، بازگشایی تنگه هرمز یا نابودی برنامه‌های موشکی و پهپادی ایران است—برنامه‌ریزی برای پایان جنگ را دشوار کرده است. یک مقام آمریکایی تصریح کرد: «ما پیروزی‌های تاکتیکی متعددی داشته‌ایم، اما بدون داشتن یک راهبرد روشن، با یک شکست راهبردی روبه‌رو هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77652" target="_blank">📅 19:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9Hw_gUDmL8n5rG3CcWvTgHt_tWKWdrOGdSMuPfKG1zjWYq0enuVhDlXCCaQD0sELkLD0w5WyDoxhriqcTCC0gBGLvyJ2F08JrU20EnHlf6Q7U0fYTeKtT9P1FQhoHNDDxgaEyY9WItXudpA-oXEI_5EHCGJ4IyTsxQvo7zG9kDuz0dU1fZGixiBQZG9fxmAdeJ3bbYUmHl0wfJrSmuIRM8IDMBnqqFH6WqZioHxbhuRYkihh2GFJN9In2Ohq7I-DdLOTFFLUwHfhnfXJEJcEdoEa7qR8QMJ-ON2XI-LPRDjd5v-KdfXjUeR4hK-eVizJkA4P8fxwzkGKZ7OzSn3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌وزارت دفاع چین گزارش‌ها درباره برنامه آن کشور برای تحویل صدها سامانه پدافند هوایی دوش‌پرتاب به ایران را رد کرده و آن را «کاملا نادرست و خلاف واقع» خوانده است.
جیانگ بین، سخنگوی وزارت دفاع چین، روز پنجشنبه در پاسخ به پرسشی درباره این گزارش گفت که ادعای مطرح‌شده صحت ندارد. وزارت خارجه چین نیز پیش‌تر گزارش مربوط به این معامله را «بی‌اساس» توصیف کرده بود.
رویترز روز چهارشنبه به نقل از سه منبع آگاه گزارش داد که ایران قرار است ظرف چند هفته نخستین محموله از مجموع ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل ساخت چین را دریافت کند. به گفته این منابع، قرارداد مورد نظر شامل موشک‌های کیودبلیو-۱۲ و اف‌ان-۱۶ است و ارزش آن بین ۶۰ تا ۷۰ میلیون دلار برآورد می‌شود.
بر اساس این گزارش، قرارداد با یک شرکت مستقر در هنگ‌کنگ امضا شده که گفته می‌شود میان ایران و تأمین‌کننده چینی نقش واسطه را ایفا کرده است. منابع رویترز گفتند که قرار بود محموله‌های اولیه از شهر ارومچی در غرب چین ارسال و از مسیر پاکستان به ایران منتقل شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77651" target="_blank">📅 19:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AByu62vIOfuXQpgxy7rYl-_T1T7S0cofwlNN3m0oAh2h990vJMabPjt8U5glhrVn2r15UHB7IadHdNF12Y2PUYc34M26BHEhOHoAFuuAnaXiKB1BDbU9Orn-eTOPfI0TOvqFYozyfuVERPKN334OnHz356NvUOv6ggPQLzH6Y6fSnSm1kZJAoAROfEP7vDWPY5COnSDhiofMMUssx2J3wXAH1gHeI9-6gezbzhYw69GHMqN9w_KgXcRxGgrD0ftV5JlI3tnI2uJ1sYlx0ey6CNWpx7lBXT883h1ErxTCBfcchSEKzfXSbYUGcZHRpXs5QZy-KRfcrxtvla_SkbKMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQaNUEEZbhoQwVkk3H6HDriPeSEHtABJB96HMxN_5JMIQybX1fjYaJ271n-dqg9J2-6PkPw0feoBy88aKpIVyldulwzLBFcdaAN-YSdfU2P-1FJ7eQFJrAamYWmg-OVUbTY1Rn4PRlRhuCm5iNkoSYRWT8IiIgtTlTN9Fq55CdWrkCgRqmWdQn_lhG9RXFphkbQvmncx1vrGUnE9dtcZSM0g_eENx5h97P8wwMHORDUlGaItwvtZsJTwLjsoWnY2UGVaTCue3ywFh7ErXvCyBQCNtMt9nHrwGqB2tgOjuAInC3Z3oPgmYJv6fQ4uZIBogQ3mUc6ydVu3o2lDNf0boA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: با شکاف عمیقی که پس از کشتار دی‌ماه بین مردم و رژیم ایجاد شد؛ حکومت ایران در نهایت سقوط می‌کند
بنیامین نتانیاهو، نخست‌وزیر اسرائیل در پاسخ به مجری ای‌بی‌سی که به او گفت طبق گزارش نیویورک‌تایمز شما به ترامپ گفته بودید که ظرفیت موشکی حکومت ایران ظرف چند هفته نابود می‌شود و تغییر رژیم ممکن است رخ دهد، گفت: این ارزیابی اولیه من نبود و این بیان نادرستی از آنچه گفتم است.
برآورد من این بود که باید برای جلوگیری از دستیابی ایران به سلاح هسته‌ای اقدام کنیم.
نتانیاهو گفت، من گفته بودم که می‌توانیم شرایط را برای ضعیف‌تر شدن رژیم فراهم کنیم اما بر عهده مردم ایران خواهد بود که سرنوشت خود را تعیین کنند.
او درباره احتمال تغییر حکومت در ایران گفت: «فکر می‌کنم ایران از همیشه ضعیف‌تر و اسرائیل از همیشه قوی‌تر است، اما نمی‌توانم بگویم رژیم هم‌اکنون فروپاشیده است.»
نتانیاهو گفت: بگذارید یک پیش‌بینی کنم؛ پس از چنین شکاف بزرگی که به دنبال آن قتل‌عام (کشتار ۱۸ و ۱۹ دی‌ماه ۱۴۰۴) بین مردم و رژیم ایجاد شده، فکر می‌کنم که رژیم ایران در نهایت سقوط خواهد کرد.
نتانیاهو هشدار داد اگر ایران، اسرائیل را هدف حمله قرار دهد، «اشتباهی بسیار خطرناک» مرتکب خواهد شد و اسرائیل «بسیار شدید» پاسخ خواهد داد.
او در پایان گفت: «هدف من این است که مطمئن شوم ایران با این حکومت به سلاح هسته‌ای دست پیدا نمی‌کند. این موضوعی است که من و رئیس‌جمهور ترامپ هر دو بر سر آن توافق داریم، زیرا در آن صورت جهان متفاوتی خواهد بود.»
@
VahidOOnLine
نخست‌وزیر اسرائیل روز چهارشنبه در گفت‌وگویی اختصاصی با لینزی دیویس از شبکه ای‌بی‌سی نیوز تأکید کرد که دونالد ترامپ تصمیم‌گیرنده اصلی درباره جنگ ایران است و او تلاش نمی‌کند ترامپ را برای ادامه حملات علیه ایران متقاعد کند.
نتانیاهو در عین حال گفت نسبت به امکان دستیابی به راه‌حل دیپلماتیک با جمهوری اسلامی تردید دارد.
او گفت: «نمی‌دانم این احتمال کم است یا نه، اما نسبت به شیوه عمل ایران بدبینم. آن‌ها همیشه دروغ می‌گویند، تقلب می‌کنند و زمان می‌خرند. آیا تحت فشار کافی ــ فشار دیپلماتیک و اقتصادی ــ ممکن است این رفتار تغییر کند؟ می‌توان امتحان کرد.»
او افزود: «واقعیت این است که ما شریک و متحد هستیم. او شریک ارشد است؛ فراموش نکنیم که او رئیس‌جمهور ایالات متحده آمریکاست و من شریک کوچک‌تر هستم. اما من نخست‌وزیر اسرائیل هستم و هر زمان لازم باشد از منافع و امنیت کشورم دفاع می‌کنم.»
نتانیاهو همچنین از نقش دولت ترامپ در مقابله با «دشمن مشترک» قدردانی کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77649" target="_blank">📅 19:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi4YzktlSbvz-O2YWRJsiyXtjuX3ARzfyLPZrKH5N45DEIgVB4TFcU5DinKlO1UI-kP9PAvTvHAOKOuPM25E-CeNQWkMqGwnLuoWhejs0knYFH_f-sUNsH6GCFEEJLV-dyJAjSwbRBV-hIZvQXm_p4zL-MKQokai3hNggShHZe68UNWG8EIqTYKuR-lpDZsePpFTnjP1hg5lj08aHGl65A54iaMPts21iTfxJFd1ed5lcCn8E-tk3-mBZSN6Gkuo1wb-2jFn-98cRF4jIGCKsjDB2xm-2ogwIGvb2rsQCzSuQ8vbyZvWQKXwe4r6mhG4kTd_EyYhvICKg4Q6dIlmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار ویدیویی از ضرب‌وشتم چند زن در ایران در جریان یک پخش زنده اینستاگرامی، موجی از واکنش‌ها را در فضای مجازی به دنبال داشته است.
به‌ گزارش خبرگزاری میزان، وابسته به قوه قضائیه ایران، پس از انتشار ویدیوی این لایو اینستاگرامی با دستور مقام قضایی برای این فرد پرونده تشکیل شده است.
سعید راستی، معاون بخش «مبارزه با شرارت و جرایم خشن» پلیس اعلام کرد که این ویدیو باعث واکنش گسترده شهروندان شده و اطلاعات ارسالی مردم در شناسایی متهم نقش داشته است.
آقای راستی اضاف کرد که این فرد بامداد پنجشنبه، ۸ مرداد ۱۴۰۵، «در عملیاتی» در مرکز تهران شناسایی شد و «به دلیل مقاومت در برابر ماموران» دو گلوله به پاها و یک گلوله به دست او شلیک شده و در پی آن بازداشت شده است.
هم‌زمان، ویدیوهایی از این فرد پس از بازداشت در شبکه‌های اجتماعی منتشر شده است که او را در یک مرکز درمانی نشان می‌دهد. در یکی از این ویدیوها، او در حضور پلیس از زنانی که در ویدیوی ضرب و شتم دیده می‌شوند و همچنین از  شهروندان و پلیس عذرخواهی می‌کند.
@
VahidHeadline
دیروز بارها اون ویدیو رو برای من فرستاده بودند و می‌خواستند پخش بشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77648" target="_blank">📅 19:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsEkUSUk5gccYhbVuVFG5L_Hog_0omJTpxP0isAHhfnivQg6EsdHoQKr9y8TU-5ze9j5jbNF6RpUYIBejXGltFNg9t0UIGdeaZzIW_D3gUCI-pzXzzOeFNLW1be86Dch-9r9ANeWO5AIMGgHStybRGhcAfLbo_Dp2dw3M1ykDx-Tg5MLj3fmngGclPrMpSMYoFwb6SwehzP3SE_yk6GbEH5MgYrdLEoNeWCzJMm4s2GY-DaU3u_bThLXTCGB-TBZd_9G-1a0cz09V7a2Ki1LsWMyyOjR7rNEDQuRGMrOu4Vg_F2W7KuVuO1F9n9ZitHuf4AfMUT7ZiQyaOpEwFj6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدعلی (آرمین) جنت‌خواه، فعال شبکه‌های اجتماعی، برای اجرای حکم قطعی سه سال حبس بازداشت و به زندان فشافویه منتقل شده است.
بر اساس این اطلاعات، آرمین جنت‌خواه روز ۳۰ تیر ۱۴۰۵ بازداشت و پس از انتقال به زندان فشافویه، اجرای حکم سه سال حبس او آغاز شده است.
اتهام منتسب به او در پرونده قضایی، «تحکیم مواضع اسرائیل» عنوان شده است.
جنت‌خواه پیش‌تر نیز در دی‌ماه ۱۴۰۲ توسط نیروهای امنیتی بازداشت شده بود. جزئیات مربوط به روند رسیدگی به پرونده و نحوه صدور حکم او به‌طور رسمی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77647" target="_blank">📅 19:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRFvdAmaBNeFtsoFdw6dLzS4EcalOKw8Ono-dBAvzbsksMAilFZ0Vb1wid3EnHQgJ8tu6eTMNS7hNdkqkUF2CchP365shfNw2yyPcz08D2yy0fYnk2UPsjUcMQKUT8gY93mAyexo_ifELtpnTFp1uf_PScozPrTJdmRFqRjm2tNHE2wW-HWU4PdtsJV-Rqm_NcuLt-6P-qG4qatY5dpivDW1qhF0nd3ImoxlLKlayKQ5Yjq60gcanZhOAhH1dMzPNZ6WrWQYd3S72ScK-nhFwvMCogzJN0n7Zk2x31N2_XB289wId2lUXPwg4n0trpxQfuQN891WdIQ29bNykpiUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران زنجان با انتشار بیانیه‌ای از کشته شدن سه نیروی این نهاد نظامی در حملات بامداد پنجشنبۀ آمریکا به نقاطی از ایران خبر داد.
در بیانیه روابط عمومی سپاه استان زنجان، به‌جز اسامی این اعضای سپاه پاسداران، جزئیات بیشتری درباره محل کشته شدن آنها و درجه و محل فعالیت‌شان اعلام نشده است.
این در حالی است که تا ساعاتی قبل، رسانه‌های ایران این مناطق را به‌عنوان نقاطی که هدف حملات بامداد پنجشنبه قرار گرفت، اعلام کرده بودند: «اهواز، آبادان، بندرعباس، قشم، بندرانزلی گیلان، کازرون و فراشبند استان فارس، چغادک بوشهر، شادگان و اروندکنار خوزستان و جزیره کیش»
@
VahidHeadline
پیام دریافتی بررسی‌نشده: در خود زنجان کشته نشدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77646" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtIIsL7AUY4seSZlVSEiqXj1dXsmL7u2IZohEkDDcTLQmExp7p_QuCSA3KQ7FGrRkN9mXzxeQRHefvQjZMkO_L1pO7jape-JEEnR7u6xEPkkgZ-rc-51mDlQqEh6lHNNXu7DjsKDeVb4VVpNN8h3sJuF_SnrocOWxy7c3k-A7Tkma23oRN2UtyRab27vnrbpJLB7G8P-tfzxPl4GqPM_SDxfBNLp1ZlffYIRNEkwXs7MoSwDbo2i71X0-yjkLOVgUGsKBaFIog64ZKXa653e0u_gN2cRTsBxSCb2m6nztgxpICqMKyRgoU65nV0e3ckiwhZiLJfTt8AnofoHYpm8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران ادعا کرد که در حمله به پایگاه الازرق اردن «سه فروند هواپیمای اف۳۵» را از بین برده است.
سپاه پاسداران در بیانیه خود ادعا کرد که پنج‌شنبه هشتم مردادماه، با حمله به محل استقرار و سوله تعمیراتی جنگنده‌های اف۳۵ آمریکایی در پایگاه هوایی الازرق با چندین فروند موشک بالستیک، «سه فروند هواپیمای اف۳۵ را به کلی منهدم و به سه فروند دیگر خسارت سنگینی» وارد شد.
سپاه همچنین ادعا کرده که در این حمله «چند افسر و کادر فنی و تعمیراتی» کشته شدند.
این ادعاها در حالی است که پیشتر ارتش اردن اعلام کرد که پنج موشک شلیک شده از سوی جمهوری اسلامی را در آسمان این کشور رهگیری و منهدم کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77645" target="_blank">📅 19:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsg55aYHskQMIbfoxj5xr_cZczslU8vkJiUNAK_8sRYZRUqM7JKg7iL2zB6OAbWbxFAZmkEf4CLry2ECp3NRjt8UKv59-m4ZEoewxvADvmhltP7Cabh3Vd-aMar7_i_Ay7ihcrUAnRQjiygnX5VHZRx-iCB7fYp61IqoEZQLwUVFK9-WJgvFD4fvRICboK6UDtcfRi4nMWeIe2KpOKRDp2L0A93m_9aKkR2tNP-niKhsQEbBzNn6lG-hHBjppk-bP6spLuDnjdCPWJW7EUDeggGZ4hbYLWO7WZaNQd4AiSrn3r2Z3JrZnWiqvdT_UtcTbrXUkiPxEexX-_lj6Cx9Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه ۴۱ دیوان عالی کشور حکم اعدام بنیامین نقدی، از بازداشت‌شدگان اعتراضات سراسری دی ۱۴۰۴، را که پیش‌تر از سوی شعبه اول دادگاه انقلاب شیراز صادر شده بود، تایید کرد. وکیل او می‌گوید با وجود ابلاغ این رأی، درخواست اعاده دادرسی به‌زودی به دیوان عالی ارائه خواهد شد.
بنیامین نقدی شامگاه ۱۳ دی‌ماه ۱۴۰۴ در جریان اعتراضات در شیراز بازداشت شد.
بر اساس گزارش‌ها، علت بازداشت او شعله‌ور کردن یک کپسول آتش‌نشانی در مقابل نیروهای انتظامی عنوان شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77644" target="_blank">📅 18:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nOP6_0C48sROF9wD8wJ2LQ2GoI-NC-TofIpQCADS_2fp-0n15Od5zuF8GAANfvl30I9P_RIoNAZQC-ej8Uv15dXhP7Acttwdj5dzVHWBU57YK6OlX1kGEASX9vfHDw0LdrxLP912mqaDgpGiTNQC3zyLckQv6H0vW0pOBUMBluORXNTS-jiF5iTwTlM2lYiXuwsZrMJGV_NnzkdOxFy0KLIfrbxYdSFyYcUqV5X5xYx9V8kVMg7lOpqnSZcj4m3jQug5W3rG11KOLVp4PsnbfLF5Q57Eq8zkRAJ4MUdwUqv_T_EprxNwBjjtGYFcKPLOdI2K3df37ouYo0B1SIQ15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: آتش‌سوزی پس از حملات آمریکا به نقاطی در
#اهواز
پنج‌شنبه ۸ مرداد حدود ساعت ۵:۵۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77643" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k94jk43QslIznvNfJ4QwcnKIFYXzzvzhQFMUQFqSIb__bILPuOABB3hFdDbIE-dfsaV3YJlEcQvOUH_3BYg-JcQuK6COMkUakhDTWUSdAsnT5i_aelvan3KeQ7oLbwMT1vK_a29-3gdC0PvuWV2jPSeraWD4nyufOrbuGK-z8GRySJxrXY7OgdsPGQDruhWO5h1zrKXTyN38zX3HZVlD9wdbkjNk4s5ym6G-9c9pUDeQ8KlCv7-llgM_02rGRRg9r813R5Ot_M8laJjzEoFGX7PoWWw8O9X8sSmGsbHhI7CeAdYB3hgXxNq6Uq3BbVfJPPn3TRUbtnAaVrX1veIOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اردن صبح پنج‌شنبه هشتم مرداد از مقابله با حملات موشکی ایران خبر داد و اعلام کرد پدافند هوایی این کشور «پنج موشک بالستیک» شلیک‌شده به این کشور را رهگیری کرده است.
سپاه پاسداران روز چهارشنبه نیز باوجود توقف چند روزه حملات آمریکا، به سمت اردن موشک شلیک کرده بود. پایگاه‌های ارتش آمریکا در اردن از ابتدای دور جدید حملات متقابل آمریکا و ایران از اهداف اصلی حملات موشکی و پهپادی سپاه پاسداران بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77642" target="_blank">📅 08:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=LlsMPdyI2uvkBBT8QCqwb645M6NxOCJkRcHvgqU5U1gUVh0wrNZnLF5TEya2bV4j9FKrf5RGzhkHFjpV7VpohdBmfxS3_kDwqiigy0K1gjE5xaFFHvCrtRX5fIaK9dYP59k_cET52Fe1WcUA_VNte2sjNCxsM39ulZgBuKW5Ti2z58L9x09-jMjdqPsWjZoADawQRRdCVYVjUREXJcvPiwqPoaI_46x-nMsNaYKLQifB--obFn94nV1IsiUnAf84oOaGDmmfPygfJg1WPEXsOvknVxcbh2wTnXWuOCsJyUODue_BdMUdJltmQu52A3Wh4JxLc8UvmoWo4qs5ETNCbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd4efa1761.mp4?token=LlsMPdyI2uvkBBT8QCqwb645M6NxOCJkRcHvgqU5U1gUVh0wrNZnLF5TEya2bV4j9FKrf5RGzhkHFjpV7VpohdBmfxS3_kDwqiigy0K1gjE5xaFFHvCrtRX5fIaK9dYP59k_cET52Fe1WcUA_VNte2sjNCxsM39ulZgBuKW5Ti2z58L9x09-jMjdqPsWjZoADawQRRdCVYVjUREXJcvPiwqPoaI_46x-nMsNaYKLQifB--obFn94nV1IsiUnAf84oOaGDmmfPygfJg1WPEXsOvknVxcbh2wTnXWuOCsJyUODue_BdMUdJltmQu52A3Wh4JxLc8UvmoWo4qs5ETNCbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77641" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0qpJJJnjvjn87klYf5a551GUKx6PqjJOqwlyDpY5ILisMivUjG27_1iz3Jhgyj0mxEO8wGlmJXYApnpIGAnKLRi15J6Hv2wygiveCjzmve7t0piwnAq8aqQA9GW8uF7P6UxUe3tQJLhmkaXZy0sSpMUR2QyY7lrRKpdtu3F0mp-PxNlvTYPbRKTtI-vbNAr9Lgg3A5s6JmsQZkwJ08GJiqw3IV20iGUFpQxsNIw2nKHS82_6kWVRu5kb79eOiTqzTYmvUCxwCs622jUeB0JPgqR0Ow5Z4lAEUBD3N9DJ8GU2kH8tkValJQHUmd2Cvn829x9Eb6cYl0UX6h7_lkxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از پیام‌های دریافتی درباره پرتاب موشک از اطراف خمین
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/77640" target="_blank">📅 07:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XSrgI6SWQh68v7_9IqZw1QSvv_UVORzbNH1ziyhiPZzU9Zt1dV9tfeHKjcs_RFa55kASoYpdWv_kX7zYs_-FspfBpBUN7fqRtFofkmY53MHB1MQ9T4EpWQ5gpF3e_qH8t6hA26XNCgQQkXK0tBvT7q90ywAyjPuX0PAb4PhziVOmPDOOm1iinoTWGEKx5vilRX9nu7OXgwoR30YUtHU_4yf4dhvG-EUzC3lvZvrB7VkW19mdbL4i1tjUQET2dWV87g3DwmxSCkPhivDelhBp1qfd341b1rbkj5VlEfUqinUK9HyKUoKFNDaAJp1r4bzF9HPdFAdtBXRMt_YYRzWdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از یزد
سلام وحید از سمت یزد دارن موشک میزنن
از یزد موشک زدن
سلام ساعت ۷:۲۱ صدای ارسال موشک داره میاد،
سلام از یزد موشک بلند شد ۷:۲۲
الان یزد 7:21 دقیقه  موشک فرستادن
سلام وحید. جان ساعت ۷و۲۰دقیقه از یزد موشک شلیک شد
وحید جان از یزد موشک بلند شد
۷:۲۱ پرتاب موشک از یزد
همین الان از یزد موشک زدن</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/77639" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPqiNbsl8PVKfq3cuDP_Vk6wJavmQxzPeVNuZXSxKhPI1No73trfkd5cjvjbHZueRetzxZhDxD7dlJfFj8sxW-8QWKtJ2MNEFDBc7UcB-3wR2El8KwizbqixULnWF8fgfQh-ptSDueuIjfyXvWJrpuJpJ06XPVpsqKfPYELU3f6ZitbRWdFcBpxnWTtWpHRVJwg-KssOksOg3dWUGv9NlNdgH-Vl1S6naCUBLXspHj2fnoHQ6rGqNR2X-HQ37o3tXS7i3EOhjUTUTf51SwSUN1scPPDA8hlJ2EsmBMQVBDQckJgWw22N3J4_IiWM2TAOOW0aHMV3Boyj4s0xjRSjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال در گزارشی نوشت آمریکا در پاسخ به حمله موشکی جمهوری اسلامی به نیروهایش در اردن، بامداد پنجشنبه حملاتی را علیه مواضع سپاه پاسداران انجام داد.
به گزارش این روزنامه، با وجود گسترده‌تر بودن این حملات نسبت به عملیات‌های پیشین آمریکا، یک مقام آمریکایی گفت این اقدام به معنای بازگشت به عملیات گسترده نظامی نیست. امیدها به دستیابی به یک پیشرفت دیپلماتیک فوری نیز با این حملات کمرنگ شد.
ارتش آمریکا این حملات را «پاسخی قاطع» به حمله روز سه‌شنبه جمهوری اسلامی توصیف کرد. این حملات چند ساعت پس از آن انجام شد که دونالد ترامپ، رییس‌جمهوری آمریکا، وعده داده بود به این حمله پاسخ خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77638" target="_blank">📅 07:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=E3h2np45FdJ-UWUCslUDymO5Jtaa9bddstwzyaX3cVLXFQSuqDjcYKR85GYVC_JB5g7aAvx7ZPjxh2htajlBjl5WYVkG12N4juwUZluFNTjE4hJm8NXpHG1fIjUJHtueiYngZPBiLPBkhN982vx-g5HJQryvPUk3eZfK1RBrFwJMbMD-qAp-wNGOrR-nIiAXu_Tplnzr5J0hr9atmYes0PD5SGOGBlW24q5wqqiYl06s-3CGslolBvBUQ-1qu3Mn4KpWw_by3nvQFucR3xKa5Lib6hlQNx1L5gsCmo9WehxXXZszAvjEyGHmNgkk8zL1WeSX1se8AUzeDq29PpBOig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79133fc57f.mp4?token=E3h2np45FdJ-UWUCslUDymO5Jtaa9bddstwzyaX3cVLXFQSuqDjcYKR85GYVC_JB5g7aAvx7ZPjxh2htajlBjl5WYVkG12N4juwUZluFNTjE4hJm8NXpHG1fIjUJHtueiYngZPBiLPBkhN982vx-g5HJQryvPUk3eZfK1RBrFwJMbMD-qAp-wNGOrR-nIiAXu_Tplnzr5J0hr9atmYes0PD5SGOGBlW24q5wqqiYl06s-3CGslolBvBUQ-1qu3Mn4KpWw_by3nvQFucR3xKa5Lib6hlQNx1L5gsCmo9WehxXXZszAvjEyGHmNgkk8zL1WeSX1se8AUzeDq29PpBOig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا پس از تلاش ایران برای حمله، مواضع سپاه پاسداران را هدف قرار داد.
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) ساعت ۱۰ شب ۲۹ ژوئیه به وقت شرق آمریکا، در پاسخ به تلاش‌های دیروز برای حمله موشکی به نیروهای آمریکایی، موج سنگینی از حملات علیه ایران را با موفقیت به پایان رساندند.
تجهیزات و نیروهای سنتکام ده‌ها هدف متعلق به سپاه پاسداران انقلاب اسلامی در ایران را هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، مواضع نظارت و دفاع ساحلی و توانمندی‌های دریایی. هدف این حملات، کاهش بیشتر تهدیدهای ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حاشیه خلیج فارس بود.
در ۲۸ ژوئیه، نیروهای سپاه پاسداران چندین موشک بالستیک را از ایران، در تلاشی برای انجام یک حمله غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، شلیک کردند. تمامی موشک‌های ایرانی با موفقیت رهگیری شدند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی آمریکایی در خاورمیانه مستقرند و همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/77637" target="_blank">📅 05:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پیام‌های دریافتی:
۴:۴۹ اهواز انفجار شدید
انفجار های وحشتناک و پشت سر هم در اهواز
خیلی وحشتناکه
پشت سر هم
حداقل ۴ انفجار
اهواز رو زدن صدای ۲ انفجار
اهواز و دارن میزنن شدید
صدای انفجار مهیب توی اهواز ۴:۴۹
همچنان ادامه داره
تا الان ۴ انفجار بلند
صدا انفجار پشت سر هم ۴ تا زد ۴:۴۹ اهواز مرکز شهر
سلام وحید ۴:۴۹ اهواز ۴تا صدای انفجار شدید اومد
اهواز سه تا انفجار ۴:۵۰
سلام وحید الان ساعت 4:50 اهواز زدن
5 بار صدای زیاد اومده تا الان
اهواز رو زد چهار بار الان!!!!
۴ تا انفجار سنگین ظرف ۲ دقیقه
همین الان اهواز چهارتا صدای انفجار شدید
ساعت ۴:۵۰
همین الان اهواز نمیدونم چند تا افتضاح بلنده
تمام شیشه ها داره میلرزه
اهواز همین الان ۶تا انفجار
۶ تا پشت سر هم اهواز
اهواز ۴.۵۰ دقیقه صدای ۵ انفجار شدید .
سلام وحید جان ۴:۴۹ ۵تا انفجار خیلی شدید اهواز
وحید واییییی خیلی بد بود چندبار زد اهوازو
۴:۵۰ وحشتناک نزدیک ۴ یا ۵ تا انفجار شدید شدید ماشینا به صدا درومدن
ما همین الان با صدای انفجار از خواب پریدیم اهواز ۴:۵۰
اهواز ۴تا اتفجارشدید پشت سر هم
اهواز تو چند دقیقه چندین انفجار شدید داشتیم و طوری که خونه میلرزید و برقمون هم به یک باره قطع شد
اهواز به گلستان خيلي نزديك بود ٤ بار
😭
😭
😭
سلام وحید جان، اهواز اطلاعات توی گلستان رو زدن ما اونجاییم
اهواز فکر کنم سپاه توی اتوبان گلستان بود، سایت اداری. ۴ انفجار.
اهواز کوی سعدی بعد انفجار دوم برق رفته الان ساعت ۴:۵۴
سلام وحید،4,49دقیقه4انفجارشدید دراهواز احتمالااسنگرشکن بودن،
سلام وحید جان ساعت ۴:۵۵ دقیقه صدای انفجار پشت هم از دور شنیده شد
ساختمان اطلاعات اهواز توی گلستان رو زدن
اهواز سمت سعدی و گلستان نورش بود،برق سعدی هم رفت
من اهوازم جفت خونمون چندتا پادگان هست الان زدن چهار بار
خیلی نزدیک بود و وحشتناک
اطلاعات اهواز واقع در پیچ گلستان  رو زدن
وحید تو کل جنگ همچین صدایی نمیومد اهواز به طرز عجیب و وحشتناکی زد در حدی که خونه میلرزه نه فقط پنجره ها
ساعت4:50دقیقه صبح هشتم مرداد
حفاظت اتوبان گلستان رو زدن
🔄
ترکوندنمون اقا وحید
این یکی خیییلیییی بد بووود
بازم انفجار اهواز. ساعت ۵:۲۲
صدای انفجار مهیب در اهواز 5:23
انفجار مجدد اهواز 5:23
5:23 اهواز انفجار خيلييييييىىى شديد
اهواز دوباره زدن شدیدتر از قبلیا
۵:۲۸ یکی دیگه
یه انفجار شدید دوباره اهواز
اهواز صدا انفجار دوباره
وحید همین الان اهواز رو زدن
وحید دوباره انفجار اهواز
وحشتناک همین الان
اهواز ۵ و ۲۳ دقیقه همین الان شرق اهواز صدای انفجار
مجددا اهواز ساعت ۵و ۲۲
۵:۲۱ یدونه صدا اومد،۵:۲۷ هم یکی دوتا صدا اومد
باز اهواز رو زد وحید
زیتون کارمندی ۲تا دیگه الان زد
اقا وحید دوباره زد اهواز
اهواز الان زدن دوباره شیشه ها لرزید
😭
خیلی صدا و‌لرزش داشتتتت
هم اکنون  بازهم زدن05:23
5:22دوباره اهواز و زدن
5,23حمله دوباره اهواز
سلام گلستان اهواز باز زدن.. ساعت ۵:۲۲، ۵:۲۷
5/22" بازم اهواز رو‌زدن شدید
۵:۲۳ اهوازو بازم زد
سلام ۱ انفجار دیگه گلستان اهواز ساعت 5:23
چرا ول نمیکنه
الان یکی دیگه زدن5:23
ساعت 5:22 انفجار شدید اهواز
سلام اهواز وحشتناک بود گلستان سعدی اگه چسب نداشتیم رو شیشه احتمالا شیشه های دو جداره خورد میشدن
ما هنوز برق نداریم
🙏🏼
🙏🏼
انفجار های آخری بشدت به ما نزدیک بودن
آسمون قرمز شده بود از اتیش و صدای ویراژ هواپیما میومد
راحت میچرخیدن
با انفجار دوم برق رفت
۵ و ۲۲ دوباره زد همین الان
🔄
الان دوبارههههه
یکی دیگه5:27
دو انفجار دیگه ۵:۲۸
دوباره زدن وحید
دوباره زد
خیلی شدیده
الان ساعت ۵:۲۸ دوباره بد زد
اهواز همین الان دوباره زدن خونه لرزید با همون شدت بود
باز الان صدا دو انفجار
۵:۲۸ دو صدای انفجار مجدد اهواز
بسیار شدید و لرزش شدید تر شیشه ها
دوتا انفجار دیگه تو اهواز ۵و ۲۸
آقا وحید انفجار به شدت  شدید موج های بسیار زیاد در خانه
بازم انفجار خیلی شدیدی اومد ساعت ۵:۲۸ خیلی ترسناکه
دوتا دیگه زد ۵:۲۷
بندرعباس ساعت 5.24صدای دوتا انفجار وحشتناک بندر
پایگاه هوایی رو دوباره زدن
به نظر میاد یک جا رو دارن چندین بار میزنن. احتمالا سمت گلستان
انفجارها پشت سر هم شدن دوباره
بازم دارن اهوازو میزنن خیلی وحشتناک تر
همچنان داره میزنه
۵:۳۰ دوتا انفجار شدید
سلام اهواز بد دارن میزنن برق رفته مثل اینکه اطلاعات سپاه زدن
هر ده دیقه یبار تا خوابمون میره یه قلمبه میزنن
افتضاحه خیلی نزدیکه صداش
همه شهر حسش می‌کنه
اهواز، همون اطلاعات توی گلستان رو همچنان دارن میزنن
۵:۳۵ اهواز
بازم انفجار سنگین
همه شهر رو بیدار کرد!
یجوری اطراف مارو زدن که کل هوش و حواسم پرید حالمون بده و دقیقا ۱ ساعت دیگه باید سر جلسه امتحان باشیم ...
اهوازیم .
پمپاران در اهواز تمام نمیشه مرتب داره میزنه
سلام وحید جان.
خواهر من دانشگاه علوم‌پزشکی جندی‌شاپور می‌خونه. خوابگاهشون  توی گلستانه، روبه‌روی اطلاعات. می‌گه بعد از انفجارهای مهیب و‌ پی‌در‌پی اهواز شیشه‌ی اناق‌ها شکسته و   همه‌ی بچه‌های خوابگاهی هراسون توی محوطه جمع شده‌ن.
صدای دانش آموزان خوزستانی باشید
نیم ساعت دیگه چطور به سمت حوزه های امتحانی راهی شوند؟؟
🔄
دوباره اهواز رو زد 5:43
ساعت 5:43 دقیقه ی انفجار
بازم زد همین الان صداش دور بود
اهواز ۵:۴۲ مجدد زدن
ساعت ۵.۴۳ صدای دو انفجار در اهواز
دوتا دیگه اهواز رو زد
وحید دوتا دیگه
بازم زد این یکی لرزشش بیشتر بود
.۵:۴۳ گلستان اهواز دور بود ولی دوبار زد
دو انفجار مهیب دیگه در اهواز
تمام خونه و شیشه‌هاش لرزید
اهواز ساعت ۵:۴۳ دقیقه صدای انفجار
اهواز ۵:۴۳ شدید ترین انفجار از ساعت شروع حملات بود
😭
یکی دیگه
سمت شرق خیلی شدید بووود
دوباره انفجار در اهواز ۵:۴۲
سلام همین الان ساعت۵:۴۳ دقیقه روز پنجشنبه  اهواز و زدن
ملی راه هستیم صدا خیلی نزدیک بود
۵:۴۳اهواز ۲انفجاد شدید دیگر
بسیار شدید سمت کیانشهر‌اهواز، دزدگیرا به صدا در اومدن و خونه کامل لرزید
۲ انفجار پشت هم اهواز خیلی سنگینن انفجارهاش
شدید کیانشهر ۵و۴۴دقیقه
صدای انفجار اهواز همین الان ساعت ۵:۴۳ صبح
وحید بازم زد اهوازو دو تا ۵:۴۳
اهواز، ۵:۴۳ …این یکی شدیدتر از بقیه بود
5:42 صداى انفجار در اهواز
ساعت ۵/۴۲ دقیقه انفجار فوق شدید در پدافند اهواز کیانشهر
5:44 یکی دیگه اهواز
دوباره اهواز انفجار شدید ساعت ۵:۴۴
وحید جان الان دوباره صدای انفجار اومد دوبار پشت سر هم اهواز
وحید زد همین الان زیتون اهواز لرزید
وحید مجدد زد دو بار یه صدا انفجار دیگه هم اومد اما لرزش نداشت و نزدیک بود خیلی ساعت 5.44
سمت کیان ابادیم ما شدید صدا اومد ۵و ۴۴ دقیقه
همین الان اهواز کیانشهرو زدن
جفت پدافند
ما کیانشهریم
فکردیم داخل خونمون رو زدن
تا الان ۸بار اهواز رو زدن ۶تاش اطلاعات اهواز بود دوتا دیگه خیلی دور بود معلوم نبود کجا بود
انفجار آخر پدافند بود کنار میدان تره بار
سلام وحید بالای۸انفجار در اهواز رخ داد صداهای خیلی وحشتناکی داشت تروخدا صدای مارو به برسونید بچه ها نیم ساعت دیگه باید برن امتحان بدن گناه دارن اهواز رو ترکوندن
اهواز هم ۴:۴۸ دیقه هم ۴:۵۰ دیقه
هم ۵:۲۰ دیقه هم ۵:۲۸ دیقه
دوتای دیگه هم الان ۵:۴۳
مجموعا حدود ۱۳ تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77636" target="_blank">📅 04:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI35Mf0BCDwL5DUBKi_W4ubKOewqz7C9CGj43t_JWQVzNRN6Kui3SloBCl5WyKGLy34ynYuW3j9GfL8NJrSH7dZeixH0ZwIDMs_AllNhuPsGbRQ3DR5DwJQHO6QMn300MTWEnXyf4T2aPz22H9CLgCLc79FGDy3LMP0uOATnOy7EkbtNOz0IuAyz5k6XWtXx4GQsVvzQnxYgHZIh16ATeMJojc0tO4yM5TyTsUDjulytlsdtiBWaXy15UQB80Llawm77mXmPE93AfIfBzgU2CGi9mdftlRT0KiZ1i-_8I229lI8k4CjZb8R5Zl3pEIw3N6XOUgyPrbGDStCXVVtEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری تسنیم، در پی شنیده شدن صدای انفجار در استان فارس، منطقه‌ای در اطراف شهر کازرون هدف حمله قرار گرفته است.
پیش از این رسانه‌های داخلی ایران از شنیده شدن صدای چندین انفجار درنورآباد استان فارس خبر دادند.
@
VahidOOnLine
پیام‌هایی که من دریافت کره بودم:
درود کازرون خونه ی ما لرزید
در نزدیکی کازرون صدای چند انفجار اومد ۳:۴۲
ساعت 3:41 - 3:42
کازرون چند تا صدای انفجار شدید اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77635" target="_blank">📅 04:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی:
‌
۴:۳۵ قشم دو انفجار
۰۴:۳۶ دو انفجار بندرعباس
وحید دوتا انفجار جدید بندر همین الان۴.۳۷
بندرعباس ۲ تا انفجار در حد لرزش در و پنجره ساعت ۴.۳۷
۰۴:۳۶ دو انفجار بندرعباس
صدای انفجار بندرعباس
دو انفجار شدید بندر عباس ۴:۳۷
بندرعباس شدید تر از قبل
دوتا همین الان
۴ تا انفجار مجدد بندرعباس ۴.۳۷ دقیقه
وحید جان صدای دو انفجار در بندرعباس ساعت 4.37
بندرعباس مجدد صدای مهیب ساعت ۴:۳۷
بندرعباس الان ساعت ۴:۳۷ صدای انفجار
وحید ۴:۳۷ زدن بندرعباس ۲ تا شدید موج داشت
الانم دوتا سنگین زدن از خواب پریدیم 4:36
سلام وحید جان همین الان دوباره صدای انفجار میشنویم
دو انفجار شدید همین الان بندرعباس
دوباره بندرعباس انفجار به همون اندازه ۳.۳۸
صدای سومی اومد شدیدتر۴.۳۸
دوباره ۴:۳۸
🔄
دوباره انفجار پشت سرهم ۴.۴۳
همین الان انفجار دوباره
درود ۲ دیگه زد ۴.۴۳ بندرعباس
چند تا دیگه هم زدن همین الان
دوباره ۴:۴۳ بندرعباس
این جدیدا فقط موج دارن
بندرعباس ساعت ۴:۴۳ صدای انفجار شدید
محله چاه تنگو درگهان چن تا خونه دچار آسیب شده انگاری ک زیر آوار موندن کسی بعد انفجار
ساعت ۵ و ۱۰ دقیقه باز قشم زدن
قشم محله ی نریمان،  زیرانگی و محله چاهتنگو رو زدن.. یه دکل هم زدن
سلام وحید داخل قشم محله چاه تنگو  یه خونه مسکونی رو زدن الان رفتم راه رو بستن معلوم نیست فعلا کی داخلش بود ولی خونه پودر شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77634" target="_blank">📅 04:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nSFhJMpDVueKbZbukHSDPTXTX347VrmpqoMlCJjMO2GUsDI8fVTVdg90rwBYzRGACSmj6j9EWJqS1VEL3rR4QA8j-M5lV238JycplbRnqdzWq-44OyiHdXWQFCZ7IS2QQK4_9Yt4O5h16Ut5ojRDmO4RbiMKG5Dr74bqv11w7bgw_sHvIuegJW0mRXlrghOhwpn7MjGzvdloGL36t5hqOi-injMvqf09wZFnA0wS38AH1D6oi2zhqjICbJeS5PCSAhsF5hkqdPaeEXr3nz7eMeiW_lrlUDo9_IkYJ3VNR_yHxfjJetahI79E7odb8Ks2m8NX3admQlFL2mYhTLMHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای ایالات متحده امروز ساعت ۸ شب به وقت شرق آمریکا [۳:۳۰ بامداد پنج‌شنبه به وقت تهران] حملات علیه ایران را آغاز کردند.
این حملات، پاسخی قدرتمند به تلاش‌های دیروز ایران برای حمله به نیروهای آمریکایی مستقر در خاورمیانه است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77633" target="_blank">📅 03:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان بندرعباس صدای 2 انفجار
3:40
سلام ۳ و ۴۰ دقیقه بندرعباس دوتا انفجار
۰۳:۳۹
بندرعباس
حداقل ۲ انفجار
درود
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
هم اکنون صدای ۳ انفجار بندرعباس ساعت ۳ و ۴۲ دقیقه
۴ ۵ تا انفجار توی کمتر از ۱ دقیقه بندرعباس
سه تا انفجار ذیگر
همین الان ۳:۴۱ صدای چند انفجار در بندرعباس
دوباره یک انفجار دیگه 3:41
دوباره یکی دیگه تند تند دارن می زنن
صدای انفجار بزرگ همراه با لرزه زمین بندرعباس
3:41 همین الان بندرعباسو دارن میزنن در و پنجره میلرزه
دو انفجار شدیدتر ساعت 3:41
بندرعباس صدای سه انفجار اومد ساعت ٠٣:٤١
سلام وحید جان همین الان انفجار شدید بندرعباس
سلام وحید جان بندرعباس رو داره میزنه سمت فرودگاه و پایگاه هوایی رو
قشم ساعت ۳و ۴۰ دقیقه انفجار در حد لرزش خونه ها
قشم همین الان با جنگنده بمب بارون شد
صدای سه انفجار شدید در شهر قشم
بندرعباس رو زدن همین الان ۲ تا صدای انفجار
شد ۴ تا
بندرعباس دو انفجار مهیب ادامه دار
صدا دور بود 3: 40
سلام وحید جان الان ساعت ۳ و ۴۰ دقیقه صدای انفجار اومد قشم ،برق ها نوسان پیدا کرد
بندرعباس همینننننن الانننننن خیلی شدید یا خدا
همین الان که دارم تایپ میکنم زدن
همین الان 3:40 دقیقه قشم با صدای انفجار بیدار شدیم
قشم صدا میاد پشت هم
سلام صدای انفجار۳:۴۳ شدید تر از قبلی
۳.۴۱ بندرعباس صدای انفجار
یه انفجار بزرگتر تر
با موجش در و پنجره لرزید
بندرعباس ۳.۴۳
قشم 2 انفجار نزدیک شهر
بندرعباس الان دوباره صدا اومد و خونه لرزید ۳ و ۴۳
بندرعباس ۵ تا انفجار پشت سر هم
انفجار بندرعباس ۲ تا شدیدددد بود صداش الان ۳.۴۲
+ ده‌ها پیام مشابه دیگر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/77632" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر انفجار
بوشهر زدن
بوشهر چندتا صدای انفجار اومد
جم همین الان دارن میزنن
۵ تا زد
دوتا صدای انفجار اومد
بوشهر ستا انفجار ۰۳:۳۸
سایت موشکی برازجان رو زد الان.ساعت ۳:۳۷
بوشهر، جغادکیم
همبن الان از خواب پریدم
دو صدای خیلی بلند
سلام ‌وحید ساعت۳:۳۰ چندتا صدای انفجار شنیدیم صدا خیلی زیاد بود پنجره هامون انگار تکون خورد
سلام برازجان همین الان صدای جنگنده و یک انفجار
وحید جان جم الان چندتا صدای انفجار با لرزش اومد
ٰ3:38
بوشهر دارن میزنن
درود، سه بار جم صدا اومد.
۵ انفجار بوشهر همین الان ۳:۴۰دقیقه
بوشهر -چغادک ۴ انفجار ۰۳.۳۷
اقا وحید بوشهر چند تا صدای انفجار شنیده میشه
ولی خیلی صداش دوره
سلام آقا وحید ساعت ۳:۳۸ دقیقه بوشهر رو زدن
صدای جنگنده توی برازجون چند دقیقه هست که تموم نشده و هی بلند تر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/77631" target="_blank">📅 03:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان سه انفجار در کیش
کیشو زدن همین الان ۳:۳۱
کیش دم بندرگاه ساعت ٣:٣٠ ٢ تا زدن
وحید جان کیش ۲ تا ۳:۳۲
سلام وحید
کیش رو الان زد
دوتا انفجار
وحید الان کیشو زد
۰۳و۳۰ دقیقه انگار  تووآب بود
سلام وحید کیش همین الان صدا اومد
سلام وحید جان
همین الان ۳۱:۰۳ کیش صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77630" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=ZFE97idWU7fH4eCcnf7uNURpyIauWaTqjEy98kwPEIEs0vqTMjUA5_6SKMofh0J_a9cd4WDlAo9Vh5-sn2Cy6lmBMxLceVSjRlhaRLKRAxHMP7rxxq1cz8YmzrUOSnnNIfRiVSy90-CKfH4vUn_NwGC-3zUJbeoBJUctpsYF9Uaduac2NwnbztReefQRk83i98FFcQVm-UV2qqEmgx2nLuZjSaYH5_TyRqJbRQcknRQbBzyDDESmYg9xkbQSkp3Rsxve1jeyya-9tNRnJJqMui6dDsv3tn0_FBF9fwGKRW_X7d4VBsh9bDc-0qSvS-prFuwmVPF9_1ug_Yzd70QsHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f5dd2ae3de.mp4?token=ZFE97idWU7fH4eCcnf7uNURpyIauWaTqjEy98kwPEIEs0vqTMjUA5_6SKMofh0J_a9cd4WDlAo9Vh5-sn2Cy6lmBMxLceVSjRlhaRLKRAxHMP7rxxq1cz8YmzrUOSnnNIfRiVSy90-CKfH4vUn_NwGC-3zUJbeoBJUctpsYF9Uaduac2NwnbztReefQRk83i98FFcQVm-UV2qqEmgx2nLuZjSaYH5_TyRqJbRQcknRQbBzyDDESmYg9xkbQSkp3Rsxve1jeyya-9tNRnJJqMui6dDsv3tn0_FBF9fwGKRW_X7d4VBsh9bDc-0qSvS-prFuwmVPF9_1ug_Yzd70QsHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
آبادان ترکوندن
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
صدای انفجار آبادان
سلام آبادان چندبار پشت سرهم صداهای وحشتناکی اومد زمین لرزید
سلام وحیدجان همین الان چهار بار صدای موشک شنیدیم آبادان ساعت ۰۳:۳۲
سلام آقا وحید تا الان آبادان ۸ بار صدای انفجار اومد ۳:۳۰ دقیقه
احتمالا دارن موشک هوا میکنن
سلام وحید، آبادان ساعت ۳:۳۱ پنج شیش تا صدای انفجار بلند شنیدیم
وحید سلام
۶ تا صدای انفجار
همین تلان ، ابادان
وحید سرساعت ساعت ۳:۳۰ ابادان صدای چندتا صدای انفجار اومد ولی دوره احتمالا خارج از شهره
حداقل ده تا انفجار آبادان ساعت ۳:۳۰
از ساعت ۳:۲۰ شروع شد
اقا وحيد صداي ٦ انفجار ساعت ٣:٣٠صبح در ابادان
وحید آبادان ۵ تا انفجار شدید ۳:۲۸
همین الان صدای ۶ الی ۷ تا انفجار از آبادان اومد
ساعت ۳.۳۰ بامداد
آبادان نزدیک ۴/۵ تا صدا شنیدم ... برای اطمینان حتی به دوستمم گفتم اونم شنیده
۳:۳۳ آبادان رو بیشتر از ۵بار زد. بیرون شهر یه چیزی آتیش گرفته، نمیدونم کجاست
آقا وحید آبادان رو ساعت سه نیم زدن شیش تا انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77629" target="_blank">📅 03:35 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
