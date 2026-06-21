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
<img src="https://cdn4.telesco.pe/file/YnI1fTW4z5c5QNLGHFqp9BeD09X5cYMdChU-u8kGkF_ySypkIzktTofg2CpyD3YnsSb2co5-0vTsKbwbsEpDI3woqn9aWxjOD4UuukBT_Q3R3INCCgirxjTft7v8VjjKyHQsSAUNuAWh1al5u_sCkAWSu4hvpkSSX_evdlPxhKp3ij8APVt40rDBVpUz4-0BLShXHw1PizBDm9T3wWS1RNfHVY541ENF6xC4gHesWzlcLjyC4BYkFeL9Vp7UZWaCk0gWmSTpJPpkpQ_wg_OOWQoSbVGXpuzt_DOgkgszmQvEasevivi1lAVP6lAphOfIGo-2wlO_FzbuXXVtrdFYlg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 331K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-15514">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOE8XvYY-r8pii86CnlrzbgjXUiDn0cSY_B9pgm5krG-auY33UaLLTkCrMSdKqTNFbRHlTOk3jx-hQiGjOtKyVHiEO9p-mPq0PyC_IXuRi_7v-FZzQlofVxn36ogtixYyWEsuN9cdQX_U1NNbZiv3NiTeLk-Z65YyDZFasLUWImZzIzuIYr5bccW0C4IXczgNujnBBgCXzIVVr2CdhvoHubfMNMUo5o0GQwgLVkA2y_W55FpEa2jKq0HTKjSemo7AUp2HBENdyOtqLWOFyChfP60inxU2dMbguDBD3u43WdWUZ2sz45J4t33LIv3qCCANQxOhvRU0bobR1PUdF1YkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از ۸۰ دقیقه مذاکره، مذاکرات چهارجانبه بین آمریکا و ایران که با حضور میانجیگران پاکستانی و قطری برگزار می‌شد، موقتاً برای استراحتی کوتاه و مشورت‌های داخلی متوقف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/withyashar/15514" target="_blank">📅 18:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15513">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4f4a5bbf.mp4?token=hnKIRUh_EAvyuREJWAJts1hBuDk7njt3i9V0itlAu9nqh9YBB-Wv_z9X468Ca7Z8Sw8GCyrasGGC0bHOLP0qsLgsteo4XoQNyXNjzr9XyG0CuQ8_RyU1rxt761hrha9Pv9OlnjmEOlS9J6dKjCSqy11xec_8Z30ANOiKxz0P_oESyG4mNzw2UAt0UrqQdjZWOanWg-Uqq1rFr2kgA3O0SeMs3288BwTY5enma_M2gt2-o_dggTi3ZK_83CXOeOI0I2zLE28zs6xEmm0Geaa9FE7Ei3wbDxqZbNlUfcqcRmMHKL0DpmVI5MfBY4IxedkLHRVJUfOWxQHFt9k5cTOFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4f4a5bbf.mp4?token=hnKIRUh_EAvyuREJWAJts1hBuDk7njt3i9V0itlAu9nqh9YBB-Wv_z9X468Ca7Z8Sw8GCyrasGGC0bHOLP0qsLgsteo4XoQNyXNjzr9XyG0CuQ8_RyU1rxt761hrha9Pv9OlnjmEOlS9J6dKjCSqy11xec_8Z30ANOiKxz0P_oESyG4mNzw2UAt0UrqQdjZWOanWg-Uqq1rFr2kgA3O0SeMs3288BwTY5enma_M2gt2-o_dggTi3ZK_83CXOeOI0I2zLE28zs6xEmm0Geaa9FE7Ei3wbDxqZbNlUfcqcRmMHKL0DpmVI5MfBY4IxedkLHRVJUfOWxQHFt9k5cTOFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر ایالات متحده در اسرائیل:
من رسانه‌های اجتماعی ترامپ را بررسی کردم تا مطمئن شوم که این آخرین سخنرانی من در اسرائیل نیست.
او معمولاً افراد را نیمه‌شب از طریق رسانه‌های اجتماعی اخراج می‌کند، بنابراین می‌خواستم مطمئن شوم.
تا اینجا که خوب بوده.
@withyashar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/15513" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15512">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پایان نمایش مضحک رژیم در خیابون های ایران
معاون پزشکیان تجمعات شبانه امنیت روانی مردم رو مختل کرده و باید زودتر جمع بشه.
وزارت کشور رژیم :بعد تشییع رهبر، تجمعات شبانه جمع میشود
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/15512" target="_blank">📅 18:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15511">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPZjH7FwLmdDAG3-Bb25I6XIcvXcDIMx2MQ3YfyZ_C07Isv2A1tKwool-Mxj6L9mg5_yqH__JhFtg0rAKZq95seEo3Qi4ppc0HjUkBvBf1LCZ1av08lLfmaeLi5kFGv9y1hig_ybNAWKssN2sYfPsbVwdqzPhbmnyZBBGQfyabL-BGvyOLS9VlKmp9uSA4e538tjZj-BCn2yFDn2_x2dU18QRZg1V6s9wVFyE291uAF_DGyP-pSBebFc5Jjgjf84XJK5csIJx4R4JZqaYXvYo3XVHAsKj3cvozxbFKSYzURjsuyc12oD8ZRlU7_4rPvO5jFEVEC9yCfNoNXG2sqnxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی اسرائیل به اردوگاه البریج تو لُبنان، حمله کرد
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/15511" target="_blank">📅 18:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15510">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:
گزارشی از حادثه‌ای در ۵۰ مایل دریایی سواحل یمن
یک قایق حامل مردان مسلح به یک کشتی نزدیک شده و به نظر می‌رسید که سعی دارد سوار آن شود.
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/15510" target="_blank">📅 18:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15509">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شروط اسرائیل برای اعلام آتش بس کامل با حزب الله:
خروج تمام عناصر حزب‌الله از شمال رودخانه لیتانی
تخریب کامل زیرساخت‌های حزب‌الله در منطقه جنوب رودخانه لیتانی.
اعطای آزادی کامل حرکت و عملیات نظامی به اسرائیل برای خنثی‌سازی و از بین بردن هر تهدید آینده، که شامل عملیات زمینی و هوایی میشه.
@withyashar</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/15509" target="_blank">📅 17:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15508">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgV4_010NgZG45y75_ikW5IlfV4CHLgQzkMxGEuVS_ma5mY8l3p6eFfxO6o7rEv3rM-UPIxcwXpPS_r_hdZRIrm3ET5q9eR9GXbjOwfXUlE6gxGpn_u9nrz62B4U-n0LHo8-s8WgSc9PxltgcL2RdYMpzTU84OC5evaTdq7bZIYwepo7WuNHxJsIHdt3q630r7btMgD6teJGAvabsBz-RNodmii3l7DilAOEwfwJDXH0Km_p-KCgcbmCvpRs01upDchmWs7LIXl-tEYRWykK75LZn3elSA5vl9wr8awp_U8Cw6BxNqE9KZOA-xL2zFBsnUnwBoVi_eZMUxk2COC-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر استارمر از سمت نخست‌وزیری بریتانیا استعفا خواهد داد. او در دو موضوع بسیار مهم - مهاجرت و انرژی (باز کردن استخراج نفت دریای شمال!) - شکست سختی خورد. برایش آرزوی موفقیت دارم! رئیس‌جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/15508" target="_blank">📅 17:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15507">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل: آتش‌بس اعلام شده در لبنان «شکننده» است
@withyashar</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/withyashar/15507" target="_blank">📅 17:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: یادداشت تفاهم صرفاً تمدید آتش‌بس است
@withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/15506" target="_blank">📅 17:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ: از اسرائیل ناامیدم. اونا نمیتونن حزب‌الله رو از بین ببرن. حتماً باید چندین‌تا ساختمون رو نابود کنن. احتمالاً مسئولیت این‌کارو به الشرع و سوریه بدم.
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/15505" target="_blank">📅 17:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iql5Z_i64ZmnkPK9Qk9nfv82faOoN9t7pPsb4YtyNVQFsRvC4nbieF34Mg8epvBCXj7_5TE0afcadxKxkAbLgqYmcOvuPpSz87izqTA3wvcK53c2Z0U3Gdii7i6aVBPn6FtxuVXduPL0bm61cP9BFbjucJfN8Tc_5dxaA9iz41FWCDRxRnlZRJatvqgDQW2YwH_usyBJwyihbaQmgsrmSK-e6DEdz_J8I7q6GiajXZAifrTl_IEXF6AOGb91QIBNY2VMCif-yQmbJRLVlF5CRqDXOXlLgL9u9D5kHspzBloYyaZzrPMSMg7WcecezAVCITUmw2FRKj77-mCG6jrN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران باید فوراً جلوی دردسرسازی نیروهای نیابتی پردرآمد خود در لبنان را بگیرد. اگر این کار را نکنند، ما دوباره به ایران ضربه سختی خواهیم زد، درست مثل هفته گذشته، فقط شدیدتر!!! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/15504" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/303a07dbdd.mp4?token=QHdljTJdmRYvmMcs-aUZ-gK9rMdhoneVkj4mS67LZxcxM-D9cYzpRXgDABo0uyoJjJt-HKn22INPDkDwHk0bNPm8_1LUrCYjS_N2XnduyKVeMgiiWolPzr5Cj8D9C8Pj7FmTGjhbE8b6j6sXDeDaRiTGFhj-n3ZhmTMuIKvGYAnHnanYQDu-AaSqMgNiv-BHZ0aFvHtUYxxrl4dLYV80tD3UYe98EPgCYN-7u-U9oR5KJZaPbQz5Rg-_fqSOl0FAK9Tm9F20L25cX1GVvAe9YDgMsqQMVo13alskl7WYqC5H4pYJeKRxTMwTbgpocqQ5sAt4S9zWqu7BMbe6fGDTAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/303a07dbdd.mp4?token=QHdljTJdmRYvmMcs-aUZ-gK9rMdhoneVkj4mS67LZxcxM-D9cYzpRXgDABo0uyoJjJt-HKn22INPDkDwHk0bNPm8_1LUrCYjS_N2XnduyKVeMgiiWolPzr5Cj8D9C8Pj7FmTGjhbE8b6j6sXDeDaRiTGFhj-n3ZhmTMuIKvGYAnHnanYQDu-AaSqMgNiv-BHZ0aFvHtUYxxrl4dLYV80tD3UYe98EPgCYN-7u-U9oR5KJZaPbQz5Rg-_fqSOl0FAK9Tm9F20L25cX1GVvAe9YDgMsqQMVo13alskl7WYqC5H4pYJeKRxTMwTbgpocqQ5sAt4S9zWqu7BMbe6fGDTAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دیگری از لحظه ورود هیات ایرانی به محل برگزاری مذاکرات در ژنو
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/15503" target="_blank">📅 16:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fa6a9c9af.mp4?token=DqoXkQtTkD7nqIdCDlwOsUStQviZ6cTZ4ScZSLTrHBkfY8DqNgQJFQZihpKmgWTClGJl1qC6IK7YYdhE4k3vh1EcaWUcjgRnvMHsX7pQywVSQ1z4OIXOsfCYeio2eaIurWAs7592hfk4sSzrfyMpMUhFSa4JpVsldp7044qdMM6KsruI6NrxkKqdk5AT3i8vNZ21NGQ3OPHqeFRW-w1ib6mwbQHm8Xw00ES0usg32mATvO3jU2DWwHv_4FYM4cgciIkMXSuOY0iikAL2M3zfz9JEjh65AMqyRG4j1h2XLXNfmBwZBhZpjuVY9q1fCI5PG10NT_2WqeE2nSw9o6AwSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fa6a9c9af.mp4?token=DqoXkQtTkD7nqIdCDlwOsUStQviZ6cTZ4ScZSLTrHBkfY8DqNgQJFQZihpKmgWTClGJl1qC6IK7YYdhE4k3vh1EcaWUcjgRnvMHsX7pQywVSQ1z4OIXOsfCYeio2eaIurWAs7592hfk4sSzrfyMpMUhFSa4JpVsldp7044qdMM6KsruI6NrxkKqdk5AT3i8vNZ21NGQ3OPHqeFRW-w1ib6mwbQHm8Xw00ES0usg32mATvO3jU2DWwHv_4FYM4cgciIkMXSuOY0iikAL2M3zfz9JEjh65AMqyRG4j1h2XLXNfmBwZBhZpjuVY9q1fCI5PG10NT_2WqeE2nSw9o6AwSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکرات بدون حضور خبرنگاران شروع شده.
@withyashar
تصویر عباس عراقچی و جولی ونس در سالن نزدیک هم</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/15502" target="_blank">📅 16:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ به فاکس‌نیوز: آمریکا میتونه بشه فرشته نگهبان تنگه هرمز و 20 درصد نفتش رو برداره. اگه لازم بشه، خودمون تنگه رو تصاحب می‌کنیم.
اگه معامله نکنن، همه‌شونو به باد میدم و حسابی لهشون میکنم. اگه نخوان معامله کنن، عوارض راه میگیریم ازشون. اگر تنگه رو ببندید دیگه کشوری براتون باقی نمیمونه، حتی نمیتونید برگردید به اون مملکت لعنتیتون.
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/15501" target="_blank">📅 16:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">تسنیم: هیات ایرانی با عکس مشترک با هیات آمریکایی مخالفت کرد
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/15500" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فاکس نیوز: ترامپ گفت که دیشب با مقامات ایرانی صحبت کرده و بهشون درباره بستن تنگه هرمز هشدار داده.
ترامپ گفته اگر تنگه هرمز رو ببندید، دیگه کشوری نخواهید داشت و حتی نمیتونید به کشور خود بازگردید.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/15499" target="_blank">📅 16:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc459a9119.mp4?token=bDFXomXHuW5OfAbh6JQ5UkWRwkEpxswkb1zDnEuRwVxE2W_k1KeShFfxO2kMmrAsn-urQcfEDjtXjJbz4I2qOlxN1JgMoK4vLvUx9Zqoy4RvwWi6akZoRMY2V4AJq49USg4kv3oXKCVkEtIg83ScEaJE5tPJYLTBvuSErI32QZzm3iWB9h8BEoM_zI86q9modBp_9cbH6alQO8mV32ff7FdyFrTcQNZEoArnsAvgJPOsinT3ZTJKYAhmWWxxDauRf7-sizwjdkwwNt7keOZe-2eFTbDWaVAgz9XJGrEXH8wq6csz4vD-jF0_UT-QI5qg7crEmC4fsZlCwEokNzrG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc459a9119.mp4?token=bDFXomXHuW5OfAbh6JQ5UkWRwkEpxswkb1zDnEuRwVxE2W_k1KeShFfxO2kMmrAsn-urQcfEDjtXjJbz4I2qOlxN1JgMoK4vLvUx9Zqoy4RvwWi6akZoRMY2V4AJq49USg4kv3oXKCVkEtIg83ScEaJE5tPJYLTBvuSErI32QZzm3iWB9h8BEoM_zI86q9modBp_9cbH6alQO8mV32ff7FdyFrTcQNZEoArnsAvgJPOsinT3ZTJKYAhmWWxxDauRf7-sizwjdkwwNt7keOZe-2eFTbDWaVAgz9XJGrEXH8wq6csz4vD-jF0_UT-QI5qg7crEmC4fsZlCwEokNzrG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">..کشان آمدند
ورود قالیباف، عراقچی و همتی به محل مذاکره
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/15498" target="_blank">📅 16:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">جی‌دی ونس: به دنبال خاورمیانه‌ای متفاوت هستیم
وی اضافه کرد دولت ترامپ مأموریت دارد تا با دیپلماسی فعال، مسائل پیچیده خاورمیانه را حل‌وفصل کند.
ترامپ به دنبال ترسیم آینده‌ای متفاوت و باثبات برای خاورمیانه است.
نقش نخست‌وزیر قطر در رسیدن به نقطه فعلی مذاکرات، بسیار حیاتی و تعیین‌کننده بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/15497" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دلار ۱۵۷.۵۰۰
@withyashar</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/withyashar/15496" target="_blank">📅 16:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ونس:  از آنچه در لبنان به دست آمده راضی هستم تنگه هرمز بازگشایی شد
@withyashar</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/withyashar/15495" target="_blank">📅 16:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">رسانه‌های عبرى: حادثه امنيتی جدید برای نیروهای ارتش اسرائیل، در هنگام عملیات انتقال مجروحان دقایقی پیش از جنوب لبنان انجام شده است.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/15494" target="_blank">📅 16:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/759c397f4c.mp4?token=XPbJHB16kA_PpUrFQmUBAJiLyNw1RpAS1DU_EliJjGREoPd9UckiNAOn0Yy4CU6bYeg1kwzNNtRAxp0oFa3sa0YHKKZt-nJW3tVsAnYexci_v20_i-JxIxA03cq06Ek4U_M8JBMrOQm93BhgnLznByVVcIaBEtFjKpjOHSlMNwIDOv7Mf8G8SG3nG8Sc39zdRy1-CEpoBNCM8yPq_juitL2ztikX1Y1UqXjvsOZSpzv07Ue9QGt9ljJiCvfKvkUqd92yDxFUz5bDAp3xYBFmcoQ0b3n8nbmiDwz5utCDDXIc6YkNoSiuWJDMn0si6B1unlA3UZIBtutFxnSbNTdcfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/759c397f4c.mp4?token=XPbJHB16kA_PpUrFQmUBAJiLyNw1RpAS1DU_EliJjGREoPd9UckiNAOn0Yy4CU6bYeg1kwzNNtRAxp0oFa3sa0YHKKZt-nJW3tVsAnYexci_v20_i-JxIxA03cq06Ek4U_M8JBMrOQm93BhgnLznByVVcIaBEtFjKpjOHSlMNwIDOv7Mf8G8SG3nG8Sc39zdRy1-CEpoBNCM8yPq_juitL2ztikX1Y1UqXjvsOZSpzv07Ue9QGt9ljJiCvfKvkUqd92yDxFUz5bDAp3xYBFmcoQ0b3n8nbmiDwz5utCDDXIc6YkNoSiuWJDMn0si6B1unlA3UZIBtutFxnSbNTdcfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عن بازی همیشگی و انتظار هیات آمریکایی برای ورود تیم مذاکره کنندگان جمهوری اسلامی
@withyashar</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/withyashar/15493" target="_blank">📅 16:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">محل برگزاری مذاکرات چهارجانبه ایران و آمریکا با مشارکت کشورهای میانجی
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/15492" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWUVZfD91gEDLTvZVhw6Vws8l7kWS9DHZorFhpSbE8stR9ABpJdWiaa1M-o2mkWaZU8GtAdGuA2KD2jHnD4cHOSOYuEoooel_LFEmXA2o6aBgyKfL-4mxQGQYvNlT63aiz4n1Me0GWwE_5xSUvoIntW1ofgqece-hdX9gsj_-aM9uf_CacWFlFrYwgG9Ekq8zi8D--gLZjvBWUO6iiKKzCCVj63VXylvUycTK-4hbCadlJggz4cROpbVGV_IInsskqw8yjf8clMU5AR4oS54pjx6zKPAEfO-riVW4zbmYcGpPFw2l42IM85ePGC2VQz8O30RGXi8SvIQy3wI8J-WkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :
روز پدر مبارک!
کشور ما عالی عمل می‌کند. تعداد مشاغل و بازار سهام رکورد زده، بهترین اقتصاد تاریخ! بزرگترین ارتش جهان، تا به امروز. ما در همه جبهه‌ها پیروز می‌شویم، پیروزی‌ای بی‌سابقه. خدا همه شما را حفظ کند!!! رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/15491" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15490">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMiaCyYZDLzS5zRnmKUS4D9n-kd7Gs55qUd11b1FxWRU_WwuvZtZCZZsPLIj_hBLZM-QcWsDGQieINlrXlU5GfmcYSzeTzs7WmQvuoGZenfleq4a41LnUjlOBkcRSR5ddXstE9NLWnNYhxfKQVn3kBusAPmZ93_n7-9gWmforZGkhxnGdjfggvM-UAP5Mjctm7Y2qOvw9SL4lfpJ3yepPDIH5JVb-ieoTv2wRkGkKCJXNoAse4IAsnpFfNmxUotLk-rEAj-h30n5RCs1Z9D2GE3WCF6lx26CUiRJTyj4sT-wigkxP6GoMx64R_PUry5e9PJBY96wI0WxsMCtN4QaYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار شهباز شریف نخست وزیر و عاصم منیر فرمانده ارتش پاکستان با محمدباقر قالیباف رئیس هیئت
جمهوری اسلامی
- زوریخ سوئیس
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/15490" target="_blank">📅 15:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15489">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نشست سه جانبه ایران، امریکا و قطر با موضوع آتش بس فراگیر در لبنان و اموال بلوکه شده ایران هم اکنون در محل مذاکرات در حال برگزاری است.
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/15489" target="_blank">📅 15:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15488">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پزشکیان: مواضع ترامپ ۱۸۰ درجه نسبت به گذشته عوض شده
از حق غنی‌سازی نخواهیم گذشت؛ آنها هم مجبورند بپذیرند.
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/15488" target="_blank">📅 14:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15487">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صداسیما: اینترنت سوئیس ضعیفه ارتباطمون با خبر نگار قطع شد
@withyashar</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/15487" target="_blank">📅 14:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15486">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پزشکیان: اگر تورم ادامه پیدا کند و به تورم سه‌رقمی تبدیل شود، آیا جامعه توان تحمل چنین وضعیتی را خواهد داشت؟
@withyashar
😂</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/15486" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15485">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">العربیه: شهباز شریف و عاصم منیر پس از دیدار با ونس، با هیأت ایرانی دیدار خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15485" target="_blank">📅 13:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15484">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پزشکیان : از حق غنی سازی اورانیوم دست نمیکشیم
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15484" target="_blank">📅 13:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15483">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محاصره ستاد کل حزب‌الله در جنوب لبنان،به گفته کانال 14 اسرائیل:
نیروهای ارتش اسرائیل مرکز فرماندهی زیرزمینی و ستاد اصلی حزب‌الله در جنوب لبنان در ارتفاعات علی طاهر را که ایران در جنوب لبنان ساخته بود، تصرف کرده‌اند،
این مرکز فرماندهی اصلی که به‌عنوان عماد 4 شناخته می‌شد،بزرگ ترین پایگاه موشکی حزب الله در لبنان نیز محسوب می‌شود،گمان می‌رود صدها عضو حزب‌الله وسپاه ایران در داخل این مرکز گرفتار شده باشند.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/15483" target="_blank">📅 13:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15482">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسماعیل بقایی: موضوع اصلی مذاکرات امروز ما درگیری های لبنان هست نه مسائل ایران
@withyashar
بیا بد عرزشی هنوز فکر میکنه اینا برای ایرانن</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/15482" target="_blank">📅 12:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15481">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa86d8af0a.mp4?token=qtPWhW_agYxI1v1TS4U9T4aik9NoMJqRYF_ZQK6_rRUuVgGZbJ0-SfNR88S3R0_azQm_tfpPmqFOGY3GfIH4BnA276zmmo9nZsUjxSNwlJy7J8hWRRFXrJ52ksZiCojH3MH7v5chyCxH4_aVFJ3QPYnbOQcdoNOYbKoXku_EFsLv8329zVNaEWCcziR6Hp8-LGUYyog7j52x7lpUGNLyoaCzOqxN7aGGSEJF3prXibC5DpVN-93aMOmfDP14R2SHLoZZ-QQswRHngYZv8ae3DKMvstzJ82_C9WtRhXzEzq4htIXR4pywPujS5-XBWvmwVV3BjeoXBzl77wxboGI0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa86d8af0a.mp4?token=qtPWhW_agYxI1v1TS4U9T4aik9NoMJqRYF_ZQK6_rRUuVgGZbJ0-SfNR88S3R0_azQm_tfpPmqFOGY3GfIH4BnA276zmmo9nZsUjxSNwlJy7J8hWRRFXrJ52ksZiCojH3MH7v5chyCxH4_aVFJ3QPYnbOQcdoNOYbKoXku_EFsLv8329zVNaEWCcziR6Hp8-LGUYyog7j52x7lpUGNLyoaCzOqxN7aGGSEJF3prXibC5DpVN-93aMOmfDP14R2SHLoZZ-QQswRHngYZv8ae3DKMvstzJ82_C9WtRhXzEzq4htIXR4pywPujS5-XBWvmwVV3BjeoXBzl77wxboGI0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسکو دیدبان اتاق جنگ در شیراز
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15481" target="_blank">📅 12:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15480">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/667b5ddaab.mp4?token=SfychAutxnlgOXKQoxazng_NzgWrzcq70ol1cPrsWwfphMra7SYdkxXMZqjNuUBBZMoFFixWNL2vh5k0FM6oPAAqnxm0sMypRU9HccwIEO06tPHcca6QqtAEnHTk223P1z6i7IHySa0dCqoA2sjXmvo09LGI0eXG26y9pRxsxiSXuQbOSfgRMLD_qrfcCeBjKkpyGnIkXO4Y95UJgqPRTiDJ4TcxwBNkVJCIMxww-G5EqrLxALqQYf94QZyBs8kwwO26IaSPAFuYs8sQk-5lsbS7RTofU-W4Zy3sR7qEVuQEIrZJADBHQ-6rOgfFpZJ2sthFZUxL3mMf1wV-IswRMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/667b5ddaab.mp4?token=SfychAutxnlgOXKQoxazng_NzgWrzcq70ol1cPrsWwfphMra7SYdkxXMZqjNuUBBZMoFFixWNL2vh5k0FM6oPAAqnxm0sMypRU9HccwIEO06tPHcca6QqtAEnHTk223P1z6i7IHySa0dCqoA2sjXmvo09LGI0eXG26y9pRxsxiSXuQbOSfgRMLD_qrfcCeBjKkpyGnIkXO4Y95UJgqPRTiDJ4TcxwBNkVJCIMxww-G5EqrLxALqQYf94QZyBs8kwwO26IaSPAFuYs8sQk-5lsbS7RTofU-W4Zy3sR7qEVuQEIrZJADBHQ-6rOgfFpZJ2sthFZUxL3mMf1wV-IswRMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیات جمهوری اسلامی ایران عازم ساختمان محل مذاکرات شد
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15480" target="_blank">📅 12:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15479">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سخنگوی هیئت مذاکره کننده ایران:
برای اطمینان از اجرای یادداشت تفاهم به صورت مستمر از طریق میانجی‌ها تبادل پیام می‌کنیم
در جلسه بعد از ظهر، هیئت‌های نمایندگان هر ۴ کشور در یک اتاق حضور خواهند داشت
@withyashar</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/15479" target="_blank">📅 12:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15478">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ادعای فارس: تنگۀ هرمز همچنان بسته است و نیروی دریایی سپاه نیز تا اطلاع ثانوی هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/withyashar/15478" target="_blank">📅 11:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15477">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb280fa86.mp4?token=IT79q-FLQa2xjOeOjkrJ3ZmllVACrNYxZ8lQvCpq3Z4TP5rjyx60lNJSFfCfB83qyQeM-USpqnJ3qnuczdzJ1960N38tjAGz5A-nfonSqk8GTRW9h459uCMRQa6b3243PruZs_VeB4g64-v3xV-uFTUmwli8GpEyIQrmJpPYlhprpsOuJPEHMhHqU6YDGp227CM2jk39PABIRGZzulQ15htP_eIqyC3L5m5BwhPMOGI8BFu13WQd1-u45ndx_gAlGtw2AUNYeh18xntpmO_TP_dxIl3E81L3HUBOmczpGUakJFWt04xBPycMvg6pX2CZ8F1P8rjEK-iP7wva_Tx7kYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb280fa86.mp4?token=IT79q-FLQa2xjOeOjkrJ3ZmllVACrNYxZ8lQvCpq3Z4TP5rjyx60lNJSFfCfB83qyQeM-USpqnJ3qnuczdzJ1960N38tjAGz5A-nfonSqk8GTRW9h459uCMRQa6b3243PruZs_VeB4g64-v3xV-uFTUmwli8GpEyIQrmJpPYlhprpsOuJPEHMhHqU6YDGp227CM2jk39PABIRGZzulQ15htP_eIqyC3L5m5BwhPMOGI8BFu13WQd1-u45ndx_gAlGtw2AUNYeh18xntpmO_TP_dxIl3E81L3HUBOmczpGUakJFWt04xBPycMvg6pX2CZ8F1P8rjEK-iP7wva_Tx7kYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارک لوین رو به دولت ترامپ در ‌فاکس نیوز:
بس کنید به خراب کردن، بدنام کردن و زورگویی به دولت اسرائیل!
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/15477" target="_blank">📅 11:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15476">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراقچی و وزیر خارجه سوئیس در بورگن‌اشتوک دیدار کردند
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/15476" target="_blank">📅 11:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15475">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رادیو ارتش اسرائیل:
تغییر بزرگ در سیاست عملیات نظامی با محدودیت تقریباً کامل بمباران در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/15475" target="_blank">📅 11:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15474">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک منبع مطلع به ای ۲۴ نیوز:  یکی از اولین خواسته‌های آمریکایی‌ها در مسئله هسته‌ای - اجازه دادن به بازرسان آژانس بین‌المللی انرژی اتمی برای بازدید از سایت‌های هسته‌ای در ایران به منظور بررسی وضعیت به‌روز شده
@withyashar</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/withyashar/15474" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15473">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مدیر دفتر شبکه المیادین در ژنو: دیدار‌های دو و سه جانبه در بورگن اشتاک آغاز شده که مقدمه‌ای برای نخستین نشست رسمی میان ایران و آمریکا است
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/15473" target="_blank">📅 11:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15472">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">المیادین نخستین نشست رسمی در سوئیس ساعت ۱۶ به وقت تهران برگزار خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/15472" target="_blank">📅 10:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15471">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عاصم منیر، فرمانده ارتش پاکستان لحظاتی پیش وارد سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/15471" target="_blank">📅 09:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15470">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آمریکا می‌خواهد دسترسی ایران به پول‌های مسدودشده‌اش را فقط به خرید «دارو و غذا» محدود کند تا ایران قادر نباشد توان نظامی خود را بازسازی کند
روزنامه وال استریت ژورنال:
آمریکا پیشنهاد داده ایران فقط برای خرید دارو، غذا و کالاهای بشردوستانه به ۶ میلیارد دلار دارایی مسدودشده‌اش در قطر دسترسی داشته باشد؛ ایران هنوز این طرح را نپذیرفته است
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/15470" target="_blank">📅 09:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15469">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک جلسه اضطراری برای رسیدگی به مناقشه بین اسرائیل و حزب‌الله لبنان به برنامه اولین روز مذاکرات صلح در زوریخ اضافه شده است
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15469" target="_blank">📅 09:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15468">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">معاون رئیس جمهور آمریکا، جی. دی. ونس  وارد سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/withyashar/15468" target="_blank">📅 09:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15467">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/15467" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15466">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15466" target="_blank">📅 01:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15465">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حسین پاک، خبرنگار مستقر در لبنان: از ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15465" target="_blank">📅 01:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15464">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بر اساس آخرین اخبار، ساعت قلعه نویی در مکزیک دزیده شد.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15464" target="_blank">📅 00:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15463">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=ffMEb_RQvuOUMTvYCCCZPjl2Od5FFcqWKvbBHICaoq3fT3RhvE4sa6vLTZEQfkBknfj3790H9uh4wfCYfoqm2ZDCersV-B3VA0QWEIoBpUwj8kJkRoBEQB1NVe8az-5J14hd04PcyuEH6-1oH8Lls8z6Q_H0ANu7JiA2f8IZbESmEt_Q2R76Tf0mpfAnV0LIchQsxZam1X8ORhRVpN9Cu9QLYgfhwX_x6nok4dyNOOdT2z3-V7_Wpj-guluW8n-dBuGn63zZNNhjlDlkCXolwzTQT1KKWSFNC4NnJ-T4PjyS2LXd8nZaE8qFxQcOrDj9MvxiTnD5vuVAqzDdm_KgzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a879665e8e.mp4?token=ffMEb_RQvuOUMTvYCCCZPjl2Od5FFcqWKvbBHICaoq3fT3RhvE4sa6vLTZEQfkBknfj3790H9uh4wfCYfoqm2ZDCersV-B3VA0QWEIoBpUwj8kJkRoBEQB1NVe8az-5J14hd04PcyuEH6-1oH8Lls8z6Q_H0ANu7JiA2f8IZbESmEt_Q2R76Tf0mpfAnV0LIchQsxZam1X8ORhRVpN9Cu9QLYgfhwX_x6nok4dyNOOdT2z3-V7_Wpj-guluW8n-dBuGn63zZNNhjlDlkCXolwzTQT1KKWSFNC4NnJ-T4PjyS2LXd8nZaE8qFxQcOrDj9MvxiTnD5vuVAqzDdm_KgzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15463" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15462">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سی‌ان‌ان: «ونس» از پایگاه هوایی مشترک اندروز، برای شرکت در مذاکرات با ایران راهی سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/15462" target="_blank">📅 00:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15461">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11f0d58b03.mp4?token=rZuadmpGH-4CcXigepOi6aGeA0oJhpEeEkBI70E04AciUeVbynqvVRctGGzm1IxK6bsXgb0DkkT0Ttb30qenN97xfJZ4xp_eIHq93HWHs2gtmpzmI3R69fIoPa5jrjtRjqltJqhvmOlbku4-3VhtiExd4a-3tMwDfspVmTqOBbh1DQyh-p8noEhN7Ss8F5R8TSe057qlhM3WIEvh4rTqt6fZg2ZjJUtoMfk3cfysCv9CBNPhuXimLAAViDs_nBG4VJC21hvsc1yhqGAoI5A11tvhQDh-6lW9eUN1r_XpurMiYmU3UD4Bt8NxAbFSS4KUQP4FbvGUpz3tx1NnxtL7FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11f0d58b03.mp4?token=rZuadmpGH-4CcXigepOi6aGeA0oJhpEeEkBI70E04AciUeVbynqvVRctGGzm1IxK6bsXgb0DkkT0Ttb30qenN97xfJZ4xp_eIHq93HWHs2gtmpzmI3R69fIoPa5jrjtRjqltJqhvmOlbku4-3VhtiExd4a-3tMwDfspVmTqOBbh1DQyh-p8noEhN7Ss8F5R8TSe057qlhM3WIEvh4rTqt6fZg2ZjJUtoMfk3cfysCv9CBNPhuXimLAAViDs_nBG4VJC21hvsc1yhqGAoI5A11tvhQDh-6lW9eUN1r_XpurMiYmU3UD4Bt8NxAbFSS4KUQP4FbvGUpz3tx1NnxtL7FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت مذاکره کننده ایران، با اسم میناب ۱۶۸، وارد زوریخ سوئیس شد.
ونس معاون ترامپ برای شرکت تو مذاکرات با ایران،راهی سوئیس شد.
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/15461" target="_blank">📅 00:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTiti</strong></div>
<div class="tg-text">سلام یاشار جان
باور کن محرم شده میرن بیرون الواطی برای همین  ری اکشنا اومده پایین
😐</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/15460" target="_blank">📅 00:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from۞۩ ¥𝕒z∂𝓐Ｎ۩ ⓪⓪:①②</strong></div>
<div class="tg-text">شیفت شبی آ فوتبال میبینن</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/15459" target="_blank">📅 00:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15458">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895fd89b8b.mp4?token=tgD_5oG-q-5olshwsDMMn0vYkC0cy2h6Tn9mmM-yLiJ8MAJQiXpPCZ6bUMZL3EQ-NnNDk-hdiwwgJZ_EJj4A25DNCryaJVRBqw-sBaeH5d8mY0_qloy7qy5mwnhW9QA-H8mvqquIPtAuIomZL7Nc7RSwJqMPwz3Sdi7maZVikQiyOLilTnRXVRP76bu04JEH9o4ylasysbnmKbEiacwInwrjB9SOTFiY_usQ2VDv982V6G5GxHAHLqGOS0vvRS0aepBLwZtk6hafh6_K35myuKli0RO3TI2nxiUGGHtlaawtkdyd9mlcYySAgF4yo8qxkOEvIhjC_yaXcwMWnymEAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895fd89b8b.mp4?token=tgD_5oG-q-5olshwsDMMn0vYkC0cy2h6Tn9mmM-yLiJ8MAJQiXpPCZ6bUMZL3EQ-NnNDk-hdiwwgJZ_EJj4A25DNCryaJVRBqw-sBaeH5d8mY0_qloy7qy5mwnhW9QA-H8mvqquIPtAuIomZL7Nc7RSwJqMPwz3Sdi7maZVikQiyOLilTnRXVRP76bu04JEH9o4ylasysbnmKbEiacwInwrjB9SOTFiY_usQ2VDv982V6G5GxHAHLqGOS0vvRS0aepBLwZtk6hafh6_K35myuKli0RO3TI2nxiUGGHtlaawtkdyd9mlcYySAgF4yo8qxkOEvIhjC_yaXcwMWnymEAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن همای سعادت در ارتفاع پنج هزار متری دماوند
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/15458" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/15457" target="_blank">📅 00:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15456">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بی‌بی‌سی‌: کیر استارمز نخست وزیر بریتانیا دوشنبه استعفا میده
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15456" target="_blank">📅 23:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15455">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhbRZKAbkoodSrSC3zQQRp4iH-3EHI6SBVRsrSMrZD-ifLjeoAUSk2ibc3FkXSuSNfQ5bzjrmAvzqCuIqCivGYIDwOuS-cQLMiI--nRZed6eXfVPCMApOMcagg5A78xGP6f2QSS3J96l6oemTGxdBn5bVzgdVftMOi07oinsG4iFddHuZaihbQXUQhKtjQnYiMSxPlSK-E1Wljfq7o4AbZ--6nbY7gmRTZjQ2Vd1woaTTLvfBVnjjxfnV2r-qjPRviDVhg7CG-PCEi8Gv3Uc5DPRGFDEVZHHLrXD0CNlEfE7sEpS0lpaqPfW4hKubU6QQsRmstChywPJsvZdt7VM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ..  ..
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15455" target="_blank">📅 23:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15454">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K02VDIjDoenxYbc3Up0nJeWIVLvtxGL6ysNZyjpkbYVAEHq7zxxpUTbVqe5A0CxXQoggLV18JAPanXZBkJHWeHrQZFzRNlnvIS3IN8Z8QMeehwPrWBH66bOxxYnIHhF92M7a-h8yeeBBkp2wOr0nkJTsWSs0IcEHwLU5WWoAMiyDuhRhcu4lbkOBUfcbGy80hJAoW0R4rhVTDLg27STVcNFgmPuWc3Z3-mflbKNts8gFVhUlIGar5etyfsXEGTCIye7f57LveStZUDqavi0vSksyzTBVu7b8lJZ7f3zi35TvoiIL0d-YmO4WHYiODhQUdGB4sgjbFhtQ1ZJRmSXkGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت ایرانیش 15 دقیقه دیگر در زوریخ به زمین خواهد نشست. @withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15454" target="_blank">📅 23:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15453">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آی‌۲۴ نیوز نوشت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به وزرای کابینه این کشور دستور داده از حملات به دونالد ترامپ، رییس‌جمهوری آمریکا خودداری کنند، اما مقام‌های ارشد در محافل خصوصی می‌گویند واشینگتن درک درستی از ایدئولوژی جمهوری اسلامی و حزب‌الله ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15453" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15452">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اتاق جنگ با یاشار : مشروعیت حتما تا انتها ببینید  ، کلیک کنید کارای اداری یادتون نره  https://www.instagram.com/reel/DZ0c0MCxXpl/?igsh=cTR0Nm90ajdrbWRh</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15452" target="_blank">📅 23:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15451">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">️خبرگزاری مشرق:
نبویان، نماینده مجلس، به ۲ـ۱۰ سال حبس محکوم می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15451" target="_blank">📅 23:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15450">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ در‌تروث:  در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به…</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/15450" target="_blank">📅 23:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15449">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نایب‌رئیس شورای سیاسی حزب‌الله لبنان: تلاش‌های آمریکا و اسرائیل برای خلع سلاح حزب‌الله با شکست مواجه شده و تسلیم سلاح غیرممکن است
@withyashat</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15449" target="_blank">📅 23:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15448">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هواپیمای هیئت ایرانیش 15 دقیقه دیگر در زوریخ به زمین خواهد نشست.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15448" target="_blank">📅 23:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : مشروعیت حتما تا انتها ببینید  ، کلیک کنید کارای اداری یادتون نره  https://www.instagram.com/reel/DZ0c0MCxXpl/?igsh=cTR0Nm90ajdrbWRh</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15447" target="_blank">📅 23:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15446">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کاور
🔥
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15446" target="_blank">📅 23:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15445">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcX3SxO26YedCh6dK5ZsL-UHbBoEz6hNa6P_ivifzwplIYM_po9b7BKwZkAFJ8hswJpYL_HzrslpgF7omUMSOZi3dgihAazxWvm821qyNm6IjzEhJVVWJvOAZQ5gO5bUdj79ZpEHr2y0UnA6e_zqdv0dGG5iN2spbdgTco3Ip4205auAceLES2-qhbkorKg9aG6q7xOxwsK7wfFk0CROYJMatVCUVPR9ryFuL_tYf7KQ1US_NaSTVL2zd6Tn4YFKW6ex0URlt07HfBMs1-Oh8fewnuqSH7_fQBW5eYWYqqrtdDD4ZLnVuR96mMX4qMgPZnlW7wdMZabFES8RIhqRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث:
در طول دوره آتش‌بس به مدت ۶۰ روز هیچ عوارضی در تنگه هرمز وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز هیچ عوارضی وجود نخواهد داشت، مگر اینکه توسط ایالات متحده آمریکا و برای ایالات متحده آمریکا، در صورت عدم تکمیل توافق، برای خدماتی که به عنوان فرشته نگهبان به کشورهای خاورمیانه ارائه شده است، به منظور بازپرداخت هزینه‌ها در گذشته، حال و آینده، اعمال شود.
از توجه شما به این موضوع متشکرم!!!
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15445" target="_blank">📅 22:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15444">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us008Cjy-30kLFpekWShj8SJ00MdKTonQR0mC0Rs8WulIBHLmp3DIneDFFDyzG4dW3tJYCDI2xHUtE7dElLaO2hPv18wx5MjgUehIiNrDMhNhupMKjWcrYpY8WbEDkwuhtqdbehgX5MCZ5POKy9v2Hoy2UXLOXHSD4T5pMGxyLeyQRbz_P0vw9uwCFSHP3qT-zCfNjPv47SAXV9J3GMd-otstEmpnFBIsk4xqzEOX3LC-B76Iq9MAm66_ZSHxBG9t8no-0X7EtLk9KTJ_6wTZBep9z0X9pdpe5aXmNSwOWwxR0QIV_iA7Bbz47QQaIYJSu-7pgZUN-siHZJkZhVVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
🔥
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15444" target="_blank">📅 22:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15443">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15443" target="_blank">📅 22:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15442">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15442" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15441">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15441" target="_blank">📅 22:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15440">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/15440" target="_blank">📅 21:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15439">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره گفت که ارتش اسرائیل به سنتکام اطلاع داده است که به واحدهای خود دستور داده است که به آتش‌بس در لبنان پایبند باشند
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/15439" target="_blank">📅 21:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15438">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJdtxdV4e5mEDB0VF8J9ZpSQDuQMWzBTBUhRv79G2sFb0QAOp_9I-9vXKXwKdOQpmJ4agTm2vMgjts4kcLmSOrEjy2iTH4IaMs6Ru0vDjHXEZ-q4muywvfMaB9n9Sbk4m-ZEbIhkamzw-IsYOmRNrsjVIojE8FdGf8ljX24uKWuJ5c5MISB-gv5ddayUo7oUbiQaBeU6rC6jVh7OYLmnOLo0Fd5KkQHqFz-wCNfLicV6Evq3WzZZkRgAIrqEh-idLfB8En0QNCFUq4AowYDIEHqj1QLABpDlR4o7ihmq9bMGskmJ3-zqj4Uc2o87NzECC12XKK_rjiqqF1kfFZfRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار وزیر کشور پاکستان با پزشکیان
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15438" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15437">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cb82d210.mp4?token=Io1-U2OSKjHVootnRdZelcQBrKizEr1XdI6wFsCVvfrzfLThtFEPlOjLBr6XxXrhZ7aMgL7Uz9nzdkbQ0LmiLY6HRqWi8OFekdrpLGDcb9iJoA7ArbYDvTs5BL5mYrc-9MIjukvPIpOTUORUTaD7v18AVp_xoRa_79jnPa71DNKDm111cHIN1iycSdRmAl_F_28gkXLtdn0VJhQ-xxtojn7g0-11dC-XdR5-wZi6hOXnamKrKj-One8UDGB6_OhU78IrLn8UHoknAsYFoE0RyqsWdvJb6knVO8ScWQWai4JwjiZRFeN7DIOq3K8P5qeP4iXEddJ-z6umoi-Ghsu8Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cb82d210.mp4?token=Io1-U2OSKjHVootnRdZelcQBrKizEr1XdI6wFsCVvfrzfLThtFEPlOjLBr6XxXrhZ7aMgL7Uz9nzdkbQ0LmiLY6HRqWi8OFekdrpLGDcb9iJoA7ArbYDvTs5BL5mYrc-9MIjukvPIpOTUORUTaD7v18AVp_xoRa_79jnPa71DNKDm111cHIN1iycSdRmAl_F_28gkXLtdn0VJhQ-xxtojn7g0-11dC-XdR5-wZi6hOXnamKrKj-One8UDGB6_OhU78IrLn8UHoknAsYFoE0RyqsWdvJb6knVO8ScWQWai4JwjiZRFeN7DIOq3K8P5qeP4iXEddJ-z6umoi-Ghsu8Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قمیشی : به عمویم سیاوش قمیشی گفتم ترامپ برادرت را کشت
سیروس قمیشی
برادر سیاوش قمیشی (خواننده و آهنگساز مشهور ایرانی) بود و پدر «امیر قمیشی» (از تهیه‌کنندگان و برنامه‌سازان تلویزیون رژیم) به شمار می‌رفت. وی در جریان بمباران بیمارستان گاندی تهران کشته شد و طبق گزارش‌های خبری، تنها یک روز تا زمان ترخیص و پایان درمان وی باقی مانده بود
@withyashar</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/15437" target="_blank">📅 21:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15436">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">نبویان، نماینده مجلس: آمریکا بعد از شهادت آقا از طریق یکی از کشورهای اروپایی، پیام داد که بیایید مثل ونزوئلا تسلیم شوید!  وی‌در ادامه با دلایل بسیار گفت  ماجرای مذاکرات رسما کودتای آقایان علیه رهبری بود! و صدا و سیما هم حرفاشو قطع کرد ! @withyashar
🚨</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/15436" target="_blank">📅 20:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15435">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">@withyashar
ماجرای ببر از زبان امیر تتلو حالا شد جریان عاصم منیره پاکستان</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15435" target="_blank">📅 20:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15434">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الحدث به نقل از یک منبع آگاه: نخست‌وزیر پاکستان و مارشال عاصم منیر فردا در مذاکرات سوئیس شرکت خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/15434" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15433">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لیست هیئت اعزامی ایران به سوئیس به ریاست قالیباف
محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیئت مذاکره کننده ایران
سید عباس عراقچی، وزیر خارجه
علی باقری کنی، معاون بین‌الملل دبیرخانه شورای‌عالی امنیت ملی
عبدالناصر همتی، رئیس کل بانک مرکزی
حمید بورد، معاون وزیر نفت و رئیس شرکت ملی نفت ایران
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزیر خارجه
اسماعیل بقائی، سخنگوی وزارت خارجه
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15433" target="_blank">📅 20:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15432">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نبویان، نماینده مجلس: آمریکا بعد از شهادت آقا از طریق یکی از کشورهای اروپایی، پیام داد که بیایید مثل ونزوئلا تسلیم شوید!
وی‌در ادامه با دلایل بسیار گفت  ماجرای مذاکرات رسما کودتای آقایان علیه رهبری بود! و صدا و سیما هم حرفاشو قطع کرد !
@withyashar
🚨</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/15432" target="_blank">📅 20:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15431">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مقام اسرائیلی: ارتش اسرائیل طی دو روز گذشته به 300 هدف حزب‌الله حمله کرد و 100 نفر از نیروهای این گروه رو کشت.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15431" target="_blank">📅 20:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15430">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بلومبرگ: عراق به میادین نفتی بزرگ دستور داده است که تولید خود را به بیش از ۳ میلیون بشکه در روز افزایش دهند، زیرا صادرات از طریق تنگه هرمز به تدریج پس از توافق آمریکا و ایران بهبود می‌یابد.
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/15430" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15429">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مقامات ارشد ارتش اسرائیل به کانال 12 اسرائیل اعلام کردند:
عملیات نظامی در سراسر جنوب لبنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/15429" target="_blank">📅 19:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15428">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سنتکام بعد از ادعای بسته شدن تنگه : نیروهای آمریکایی همچنان در منطقه حضور دارند و هوشیار هستند تا اطمینان حاصل شود که همه جنبه‌های توافق با ایران رعایت، اجرا و به طور کامل اجرا می‌شوند و همچنین مرکز مشترک اطلاعات دریایی با صدور اطلاعیه‌ای، عبور ایمن برای همه کشتی‌ها در امتداد مسیر تعیین‌شده را که عاری از هرگونه ادعا یا مانع خودسرانه است، تأیید کرد.
تردد کشتی‌های تجاری در تنگه هرمز در ۲۰ ژوئن افزایش یافت، زیرا نیروهای آمریکایی به عملیات خود در منطقه عمومی برای حمایت از آزادی ناوبری ادامه دادند.
امروز عبور ایمن از این آبراه بین‌المللی همچنان برقرار بود و ۵۵ کشتی تجاری در حال عبور بودند و مقادیر زیادی بار و بیش از ۱۷ میلیون بشکه نفت را به بازارهای جهانی منتقل می‌کردند.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15428" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15427">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو با دستور توقف جنگ گفت که این دستورالعمل‌ها شامل عقب‌نشینی از مناطق تحت کنترل نیروهای اسرائیلی در جنوب لبنان نمیشه و مناطق تصرف شده، تحت تصرف باقی میمونه.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/15427" target="_blank">📅 19:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15426">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">محمد جواد ظریف: از مذاکرات استقبال میکنیم
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15426" target="_blank">📅 19:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15425">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjV3ItN5lpQtEm158d2B4dO9Phtzx7HaFY9pBajm7-RIuilbX0Z7XYQbTg813t9x1obv4SscCDjHCcRdopJw8lGvPtuqRm-UYA-kX1qAeEdbMDnXjshROj1x7I3vI_aA_N0Sk7hux-Y89T17ghOv0kt7GgFQU0mDkh8zvkG3p4apDiVuJRbXnYkBPz1ihmKdO0pVr23-jccinpTdBZr-eF3LiWxKpwAwtWpqW7eT8P_kwJ9FVHD2Z_QyD5S6K5KCoVhjiPr9ZgPGQHVyFWoDfc2BKOvJlYY2yZBY3xWk51XQk6xKIVVE5SIgXQYBnelXFIRPifpQTZE3byLeCTzvdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه اولین تیمی شد که از جام جهانی حذف شد.
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/15425" target="_blank">📅 17:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15424">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هم اکنون جی دی ونس به فاکس نیوز :
ما هیچ مدرکی مبنی بر اینکه ایرانی‌ها هنوز تنگه هرمز را می‌بندند، نمی‌بینیم.
@withyashar</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/15424" target="_blank">📅 17:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15423">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سخنگوی تیم مذاکره‌کننده: طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15423" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15422">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بقایی: سفر به ژنو فاز دوم مذاکرات نیست و صرفا برای امضای یادداشت تفاهم به صورت حضوری است
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15422" target="_blank">📅 17:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15421">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فاکس نیوز به نقل از ونس، معاون ترامپ: اوضاع در مذاکرات با ایران خوب پیش میره و انتظار دارم به سوئیس سفر کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/15421" target="_blank">📅 17:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15420">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ایسنا: هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/15420" target="_blank">📅 17:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15419">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">الحدث: عراقچی امشب همراه وزیر کشور پاکستان به سوئیس سفر می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/15419" target="_blank">📅 17:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15418">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تندروها معتقدن کودتای قالیباف تکمیل شده و الان قدرت اصلی کشور دست قالیبافه. چون با اینکه رهبر‌ گفته توافق خوب نیست ولی مجری های صداوسیما میگن توافق خوبه
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15418" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15417">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فایننشال‌تایمز: پایان عملیات نظامی اسرائیل در لبنان بعید است
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15417" target="_blank">📅 17:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15416">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سخنگوی وزارت خارجه:
هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد.
در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند.
ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است اسرائیل را به توقف حمله به لبنان وادار کند.
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15416" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15415">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=rJM4vF4j8fJNLsI--tQbEYPr_edBMb7k3dWz_3yHfREe898BfSmtaO0k0xJC9D9qsJu8DzLzt8L8YWuwv-T0pi48aKwGlg0nHOeNmwhZWYB9j0DSMpdOKN4NKVd0_nzOH4Vu1VyS3-RIOij-XqAeB95a90m9Ex9tsVD1AaYS8d-UjvBXWNo5FOxedMZ0sxa59C1HjtdN77nYkTEPb9H2dQCTYGm6zs2kOMulTW4gB8fQYbIAAdODQBQ8eHbZHnXDvCm6l2uplpGaGyNyRZaq6jkLNRFZJ2_DoVE2At4xpRG5lY8Y9PyNRZlbXsZXTxGlNc5ybng1r91khNwhPurdW6eBPwzHMb2FLkjgR_wUIih54TqtS4WLQwjDQeb9TyWnUlMJK0mTqyIndE4g2cXJ1glMzFNfKaNZXre7ewb-R8zO_YnZ9aBvzPkiYL7gww1MfsVWVxrayDB5ZEttsxpbcanutIRjawPYercSPAMjtSO3gKeCI2vLL55c5L4sGn4AetxFiJ-0ABFlfmqGzitKJ5fcv8cXScozqOH4o65fEmshROIgq3EfiDIWNU1jCip5UleHLgmDpFoSOm7voVJ9Rv6dk_MLJqqtR5lX8rVte3B31_nQacuw0nx_HOM5A1bzMCUXBdkWoFyAfvqEBkzDlIMokF9apIPeJ7zzolzLZec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=rJM4vF4j8fJNLsI--tQbEYPr_edBMb7k3dWz_3yHfREe898BfSmtaO0k0xJC9D9qsJu8DzLzt8L8YWuwv-T0pi48aKwGlg0nHOeNmwhZWYB9j0DSMpdOKN4NKVd0_nzOH4Vu1VyS3-RIOij-XqAeB95a90m9Ex9tsVD1AaYS8d-UjvBXWNo5FOxedMZ0sxa59C1HjtdN77nYkTEPb9H2dQCTYGm6zs2kOMulTW4gB8fQYbIAAdODQBQ8eHbZHnXDvCm6l2uplpGaGyNyRZaq6jkLNRFZJ2_DoVE2At4xpRG5lY8Y9PyNRZlbXsZXTxGlNc5ybng1r91khNwhPurdW6eBPwzHMb2FLkjgR_wUIih54TqtS4WLQwjDQeb9TyWnUlMJK0mTqyIndE4g2cXJ1glMzFNfKaNZXre7ewb-R8zO_YnZ9aBvzPkiYL7gww1MfsVWVxrayDB5ZEttsxpbcanutIRjawPYercSPAMjtSO3gKeCI2vLL55c5L4sGn4AetxFiJ-0ABFlfmqGzitKJ5fcv8cXScozqOH4o65fEmshROIgq3EfiDIWNU1jCip5UleHLgmDpFoSOm7voVJ9Rv6dk_MLJqqtR5lX8rVte3B31_nQacuw0nx_HOM5A1bzMCUXBdkWoFyAfvqEBkzDlIMokF9apIPeJ7zzolzLZec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگه بابا جنگه !!!
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/15415" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
