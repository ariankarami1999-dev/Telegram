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
<img src="https://cdn4.telesco.pe/file/nKaNqi6iKzOnoDu8z0qGSclrV0Q2_Naw51JvZEHTAtCZNDndLs_yPYvh5v6JA1TRE_3WRjj9DsZk7kTK1oLmjG5c1IzKm4F0ldIFn6hP--yUwG_MtVPysqgdWDODXgk_XEVbjEtoZIoKdotRAymdaEIy7iZHSixW3omNEuIwt-OQ6_10AfNX-rnSs4Ttn4Ki4UsQeRxYTtpvWJH6_NyFP-yshkrK4aKoMnoT5lmcU1dPnXTEzDvX3mOALSye-N3wmwn3aF9WsptL9KyxTnHNebzcwIcRzuJ4nQ4n3KvLL1ina76Cx7ec0RDfASs1i7gfGYA3c16vV_Ae4OYqbcF8qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 02:45:20</div>
<hr>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آژیرها و انفجارات دوباره در بحرین، کویت و اربیل عراق.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 623 · <a href="https://t.me/funhiphop/76707" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=gYrr16w1udcECmFbt3JkJcwEQJWP6ael2SsqfNtUXlQ2OufuELiqv7h5AkFV9wWhV0d3ZMz_Zb-ACIdp1b5yZr-_G2yfJmyv6W4GkEO5zpA3DD02NqbmFX_gv47W2FukwwkFL3n_TuSDUzClrH_NCeRldi6f3DrdENB7MOD8w7EVwrXwizPGVj9ut7DI0raJNfgQasOED-EE3Hbt2LZG0_TCRZIASf0cW9H4NZJQSFlJivYMDdC7XAxQOORGv72-7AHuGZKImMtZM7JM6mPBdO6098LTvVXxwC6z1d-r4KeBkKbtDjwnq1IkAH0P_fkrG51E97i_Tdwfh1qFiD3Bkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=gYrr16w1udcECmFbt3JkJcwEQJWP6ael2SsqfNtUXlQ2OufuELiqv7h5AkFV9wWhV0d3ZMz_Zb-ACIdp1b5yZr-_G2yfJmyv6W4GkEO5zpA3DD02NqbmFX_gv47W2FukwwkFL3n_TuSDUzClrH_NCeRldi6f3DrdENB7MOD8w7EVwrXwizPGVj9ut7DI0raJNfgQasOED-EE3Hbt2LZG0_TCRZIASf0cW9H4NZJQSFlJivYMDdC7XAxQOORGv72-7AHuGZKImMtZM7JM6mPBdO6098LTvVXxwC6z1d-r4KeBkKbtDjwnq1IkAH0P_fkrG51E97i_Tdwfh1qFiD3Bkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی درمورد روند مذاکرات امشب:
به قول آیت الله خامنه‌ای، دوران بزن در رو تمام شده است.
بسم الله الرحمن الرحیم
﴿با آن‌ها بجنگید که خداوند به دست‌های شما آن‌ها را عذاب می‌دهد و آن‌ها را خوار می‌کند و شما را بر آن‌ها یاری می‌دهد و دل‌های گروهی از مؤمنان را شفا می‌بخشد﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری‌های او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و گسترده موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را بمباران کرد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای بازگرداندن ضربه به ضربه، هشدار شدیدی با بالاترین سطح قاطعیت به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
هر حماقت جدید، یا تجاوز دیگر، یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌آور، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر می‌رود و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافع آن‌ها در منطقه به خاکستر تردید نخواهند کرد.
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿و پیروزی جز از جانب خداوند عزیز حکیم نیست﴾
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/funhiphop/76706" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سلام فعالیت پدافند و صدای مهیب مذاکره در بحرین.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/funhiphop/76705" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کویت صدای آژیر خطر میاد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/76704" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ادمینای اینجارو دیدم با ۱۹ تا بسیجی درگیر شده بودن و موتور بسیج رو بلند کرده بودن پرت میکردن سمتشون،
چقدر زود قضاوتتون کردیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/funhiphop/76703" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k04XX9Uu12g-mZraPy7LJvy3c1zSLgexegVDiDdrIOKY6O5UceBO1qAOCVIJAyzPuff_3utaYDCb_1OmMweougrHhkvYgXKZri2w9ahnMiFTnsdFMxfkeZCcrfOXG-Mr4IpD9bWg4xyt3Ks11wpHaWrAqAgRyNq2O2Li52I0ua-wc8kvNlbJ8XCifGPKyxq-5z2blgRbQGxKQRshNIbizZIHgDhs9IwqirK7w2rFpkZun8VAWNRjVUsr8fiCwWt3sR4-Njksdkl75FU3V9CaZBuESGbjaZ_VTlZ_lmDZr6bdXMpNxOmA3vX59KAy5f92HehjOwD9IIix8F2-43LezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ی اخرو محکم تر بزن، اِبی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/76702" target="_blank">📅 01:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوتا موشک از استان فارس داراب شلیک شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/funhiphop/76701" target="_blank">📅 01:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کویت صدای آژیر خطر میاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/funhiphop/76700" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/76699" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9zV85z5Y9rLliOW7BlvfRgwjpHJeBiEZSYXPsBWQkh-CzKHeWDHO4ZvOFbyMj7-cuK3F8dNxQiMnXov_0Nu6p4GZbxJbWUJV-zk1KxaxOmvLpjxLTJ8CzoQITcZkAG1BflvV7SmN5T-4YErc0mWk7gxILUJbhqXS0tbFuNwD3vLVgbGd5aCutHqdof3F-oopOxByDnzTLQH0pRW5nxlQ31M8AOlus_jnBUPvPTvWCgYsS_Oc926p5AvpIUs1C_ZFdHFSiKPScp6NPmXm50kPbYI6eqfRMrcEWoWFe5OPe3q2c0LJ8HJXj3_gqN3xG2lgoqA6XiWB_oZfOiM0Olo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ مورد علاقتونو زیر این پست بفرستید، شب خوش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/funhiphop/76698" target="_blank">📅 01:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دنزل دومفرایس دفاع راست هلند و سابق اینترمیلان به رئال مادرید پیوست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/funhiphop/76696" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ننه روبیکا رو کی دزدیده بهش برگردونه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/76694" target="_blank">📅 00:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76693">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این رپرایی که امین منیجر روشون نمیگیره بیشتر باید تلاش کنن خودشونو ثابت کنن تا رپرایی که روشون میگیره  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/76693" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این رپرایی که امین منیجر روشون نمیگیره بیشتر باید تلاش کنن خودشونو ثابت کنن تا رپرایی که روشون میگیره
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/funhiphop/76692" target="_blank">📅 23:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از نظر ویناک هرکی نگه جاویدشاه پشت مردم نیست و خایه مال سپاهه، عالیه وضعیت</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/76691" target="_blank">📅 23:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شوک قلبی به حصین:
وزارت خزانه‌داری آمریکا چهار صرافی ایرانیِ نوبيتكس، بيت پین، رمزینکس و والكس رو تحریم کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/76690" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/76689" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76688">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS2mXnTKu17xA08IfLyTyUAeiQoTbiJVNPPYa68z9fUc5fnMjMb-eIMqVypfgitIEUHbZrNgu6JtH45ED0sKy2CGsJhwX9amlzmHYZifgpGsU9B-qLPOoMdU8MImiKTzh0Bby-pdp-jdvrTjct6Fv4Dpj_J7AQiNAKdbF7yO6vM7l27paqeBqfZNXrJ4vw5pqGzXWhKm2wlf9vL93si-zVEvbvFtgASELpQXpApabsC-c_QNGoUeSQ7WNDAsRUlxdbxLe_-Yxy8YwbRweLdmM9TawXcrnoKxwARy6xjmQgthGZowofjRXKoxZcXs8uXcTx_kjR8InNp-c3dNMzSbjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76688" target="_blank">📅 23:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQWOq0eLYuIvrQsBC2nDOcd-_6nmSaQgHgeEGscZ_mIA6yuFT_RfwxF_2m20GYe48WqHMKBLEofzovBh2iTGBkGmeQXNzferuQ7ahJ7AZ4llWK6JpBsI3aI_7gfyhlWXkyE5UTszhxyTktkUYEhhU_1OO-Ry1M2CWca0CZIqWQfU9MjBerkOd3PqhPtGQlPpsTfX_SAY64shbMEGW-LtS_xhA6eJ9PE11MKwYmvbFg2krG94p3kQRt2VSuUUo3T5qBs7HBj-9KJiD0Bg6Sz0nMDU4pbsnSzSNga9mh3yXtvxLU1bjuWMT_5ZQ3l7vwwRuMas29dH4otSKarK7oNJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای سنگین دکی و ویناک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/76685" target="_blank">📅 23:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbP7431DjAYy6PmQxef_j14B6IDFrN8NG3MA8uOCHEfvvkn_Hl3WCUAgUc_XTJclpowpUhZxSQWIH3ShenSQFrlY2Tkm1W__3GfshCBQRHqE-3pBvlVb7buQCy6LlNqfLZwKUu4CO112d6lwgv9sbMPx5IXB7DpSeBxuYzTIkdxQoUqQ8VBx9TyaaEZ7GlHx1ZKbgus90I8bbBHuCb0kn70i_W7PnZwTCFKvE-8v6SCkjOY4F0cMN4svZQm7s7QWGZmea_oz2kpWvGjiIWHYWrk-JKDFaGvWM--KFCxElqm5MJcJh1s_GaJzprLMIvLefGDaLhfp3ZjMBguvofJwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/76684" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76683">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/76683" target="_blank">📅 23:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">رپفارسی دو بخش است
یه بخش مادرجنده
یه بخش خارکسه
یه فدایی ای هم این وسط هست که خداست</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/76681" target="_blank">📅 23:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgmFR75mAA56vcBHkHqGjsRzBZz_Rvx58WElPY2_JPjpHSH3oAZVNqMRv3fK5OhGyjMSf8bnmKMttnI98coPq6MOwWyiFb52HvvmdXlmS9vcZBLjABIBdw9OBl_5QUUAHv_ckfOGSXP8BwTH25xR64A_BWooy8Qm-5nR-w6LOf15TjRXCQ80TUM0Xo6iG1rw8j3jy_Nwa01dcQIXmTEWvkP0soMgiupBliV6D5co4jH8Vrq4URJVzKfMLrbGaTh6NhdjdDBsxyn6KweuVQ-1QzcpcsKZYQ1tq7DTBMgdVqeCAcHv8RChSln3SeGp9wToW96DBTD3eoNBqjQLC0sO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/76680" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ویناک گرفت رو دکی و حصین و سپاه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/funhiphop/76679" target="_blank">📅 23:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">چرا بی احترامی میکنی بی تربیت</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76678" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">من رپفارس رو دنبال نمیکنم اما ایشون دکتر چی هستن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76677" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76675">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=eZFdLnND-aRX9p5i3eVkfouGuUNhtfDr0iMxKUkRfMAl_Kbq3yStaUdDNCTDLwFydTTFWqNE6NmWj8Ygkru78iAz0uig0qhHeUEn47pTvbDIscRBYkjfZPLoqZneLLJ5t0lyIzlxmWzhgSt1zZdMvM8fH99aQEFhipwRkFEEwTf5edffaO2Ye7JgCLW3tkjcAxQkBo_WGM4fPARzkRgUVlH4EananeZfLchRbUf6EHf3xyMgDjx1tSAnDWzbN9De5RooVBBy5nxzAbqSMIqflovYskicrOb8-Mb_sWoM7MYV8EJyn_iTbzJWSRGs7JcrHC_Tl90vK69WE7gpGfiTq3xerg25S-3FbKIjtP9o70x4pdeFCIgulWSzXqxew37xcKCqLkYzZPMZXIjyaKGDwpk7YxEkc5CP03Q6PD05t2beyvefkj1nvMgQDeuRo3K5Y_NQxAh2zV_bNS-owxMkEY8IfOdsjRGnkZS9-65wAjmagRW1Lqqq_3w77rfscpsul3gPdrmArv5icxWRMDBGnX3simqe0e0wON3ZUEEmUybGmPMPvdf8WPF2lPx08785DO0DTTmBQ_Q9USY3BU9Y_nuLnrTFr3PkK1jkFltrj1qlIu6A2WqEkzd1spQsLPBJbLrFyTiu6in3EelzwJUGJSDZvjtZApmPTV2oGIf8ieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=eZFdLnND-aRX9p5i3eVkfouGuUNhtfDr0iMxKUkRfMAl_Kbq3yStaUdDNCTDLwFydTTFWqNE6NmWj8Ygkru78iAz0uig0qhHeUEn47pTvbDIscRBYkjfZPLoqZneLLJ5t0lyIzlxmWzhgSt1zZdMvM8fH99aQEFhipwRkFEEwTf5edffaO2Ye7JgCLW3tkjcAxQkBo_WGM4fPARzkRgUVlH4EananeZfLchRbUf6EHf3xyMgDjx1tSAnDWzbN9De5RooVBBy5nxzAbqSMIqflovYskicrOb8-Mb_sWoM7MYV8EJyn_iTbzJWSRGs7JcrHC_Tl90vK69WE7gpGfiTq3xerg25S-3FbKIjtP9o70x4pdeFCIgulWSzXqxew37xcKCqLkYzZPMZXIjyaKGDwpk7YxEkc5CP03Q6PD05t2beyvefkj1nvMgQDeuRo3K5Y_NQxAh2zV_bNS-owxMkEY8IfOdsjRGnkZS9-65wAjmagRW1Lqqq_3w77rfscpsul3gPdrmArv5icxWRMDBGnX3simqe0e0wON3ZUEEmUybGmPMPvdf8WPF2lPx08785DO0DTTmBQ_Q9USY3BU9Y_nuLnrTFr3PkK1jkFltrj1qlIu6A2WqEkzd1spQsLPBJbLrFyTiu6in3EelzwJUGJSDZvjtZApmPTV2oGIf8ieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینید این بنده خدای مو نارنجی چی میگه من بلد نیستم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76675" target="_blank">📅 22:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76674">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY7j9Xhgrm9rrksh0ZZOGfeeMvCz6DEhV7_7mnuqtWbDrVwSFpRVlZal9U9z1qPs58PdK1l6pib5GWiU_1Bs0-f-VnBQQpeCWkvQIBxu5hkV35N9e5IKLJ1nrlT95HP48yansYxIi8bqx2Y5FY7VB9WnI7ffaLjZQO4spOdCAW1kWiJvpvNUYW9eCUSBsTyd5-joVZui-_Xe65bwYV2eqSeYegg9NrxGzV61Ek-WSDSvZzRsaQxpCyPnMFK4AvRAwBET36l82mx_pc4r2-ZVeNMpDii5lanUm66UEnFqwcn89ZG9GurqDF9hKO2-WbjHmO4DPeYHRJAGY9BHz4vhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاقیت در ملت شریف موج میزند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76674" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">درگیری مرزی هندوستان با میانجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76673" target="_blank">📅 22:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzZBTYlKMZmtNucE7nGVAt9YJo9fZ5TNKGHZ0buab-qtvMSNnGdMXeDDTGKz4dTwq1SFNJXm-o_7XDDi-0CP351y168c69zE4vE5PCt7GxZRSIBLZ93fAnKxLPTRNSvX__uKrAAxoj-IxG9Ar28bK8TssklQ0EAVYVfO5kky3Ia7KzederO7b8SIcKp6ZCUcXXLA5d9SOCIK0Qq98zHOvabrmeKKSH0cSmmSKxDr0fgTPSZc3DQeVsnhcJyUiUCGETfXIeUuBWEESYI3GnHoye32cRUGgsKFPsqUQfrgBLVc7uHUuMPN-gJko4SrHJs4tpBvkJZ5c9gzi8pvekuXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغ جدید نایک با حضور لبرون جیمز و G.O.A.T
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76669" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76668">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIvGMYboqqLnINxSIx5V9pru-Pza1bsZxKrCdQopuQBqRBSB8y9faLc9bIkT7pGlxMhXBx9kfGboJNEVAICU9olfP9JMvBGVMAsSvz5WOk59NQoVHrWA0EMrn-JCsREoIhsHJwkNpwcmXCPPPOJfVTPDO6fnSCpMe4WC9kS0aWeCaCgZXOT0o5Y-APFzQpOd4UWc4yPQjvhuaQE-bl3MWKhqCMe1y4iirwYI5eWhBOYzO44Q0S-66xFMU0Z66sBAqCgCBQH04UWUeyotoFEGSjxQv8fM6_-jv69RFX19sXhcB6sedgOtkdd_XNcglR_xAHxYEo1lwScXcT600wCkCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین خارکسه اس، ولی به تو هم نمیرسه کصشر بگی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76668" target="_blank">📅 21:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76667" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱,۸۰۰ تومان
🚀
@suii_vpn
@suii_vpn</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76666" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyg9iDx8d7YGb_Jb1xReG3kY4lYYUkwAbMZN2jec4MrVca4chqCc4a58gTZDDympnKE3pEMorG4dJbfV3N85nDS18zvsQMtKb041cXcaOzRGpsfn-GoyU8rfGVsvcfzGHUfRWYyAxIbtH-6E2BgM85gPONOhVKhRQyEMEaucL7WObcW9AxcoNPBlJhavQH6yjB9oiJesxLFoRItGNgJqliR8cO9vtBGt0y3DlobqkHGkLxGQ0bfZHa59xG3bTBXa1gGyhRTQbrtnWAcgmHo6_kEdsWz401B3ZQX8EsYU8zJDcZujRZWp9iJBPvNyHzzuBkx-FdOPuXDDwafM0UQggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ح   ز   :
این چیزایی که فارس و تسنیم می‌گن مذاکرات متوقف شده دورغه بابا.
این حرفا نیست که اصلا.
ما الان یه مذاکرات خیلی خفن با ایران داریم که خب البته نمی‌دونیم آخرش چی میشه ببینیم چی پیش میاد ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76665" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">روبیو: شاید ظرف چندروز آینده خبری از توافق با ایران بشنویم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76664" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهوی جنایتکار در مراسم انتصاب رئیس جدید موساد:
رژیم ایران در نهایت از صفحه‌ی هستی پاک خواهد شد و و ما کمک خواهیم کرد تا این روند سرعت بگیرد.
در آن نقطه، این رژیم هرگز باز نخواهد گشت تا وجود ما را تهدید کند.
این دستور من است – و این مأموریت شماست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76661" target="_blank">📅 18:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز در گزارشی افشا کرد، ارتش تروریست آمریکا برای هدایت پهپادها و کشتار مردم ایران، از شبکه استارلینک استفاده کرده‌است/ رسانه‌های خارجی مدت‌ها استارلینک را ابزاری برای دسترسی به اینترنت آزاد معرفی میکردند/ چند هزار دستگاه استارلینک توسط عوامل اسرائیل به ایران قاچاق شده بود که عمده‌ی‌ آن توسط دستگاه‌های امنیتی توقیف شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76660" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuK2DpBQiaM1lJRM25ZD12J0QZ0zE2hDnu1W-44N78gHNyIT3peS3Zi-2NNcZktfDlApJZYfeQrjEXbmxRB_SdxS-t6f3l2jVVIkrIgNpKZPj3DC_d4h2RYXQjRgMVr6s_7TmIH--MXIgkTdNi2DWnpaZzhHh6FeoZyhVK6cTjLu3WbIhtZW7dSTeaMHHGNW37wG7OwRNDE-Td8ysKSx8cgBZ0HiZZ9BIP42WMyOx8kffvYVfpXH2fBOQU3r5C2xytQJ5FRyiYKTnVHEMsnmHal5OhF7YrUV1ODXQ85eU-Mp2L3fjDrBpqtDVwSCXd5eHvPaNdWO7kSIU-PKChDd_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیشد
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76659" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofwSAwO-MnDGPT5yrHjx1ia5dKbPHQO0wuoEmU4qLXzHfl34VLmikWardte7XiF9UOAsHv9kjIejbLQAA37ZsW36u9XJo4K76YXhWO5yyCuI0H2592VlnxJ1oKRweUUF5Yjv1JMOm73uE03g-6ErKefsDVEioPlPB2FWjq5KaImACilCuTjMycr5lSvP4DNXvOnRDpV1ZnKv3k1U1GwEwGtIxjQ03W9cg6yGmXfAh7S4msKDww6wZ_POllauRgLxuq5nzHATIUZeKTuHV5QNU51BT7PSl3NqYkZJHYueD9VpKQoj-DobEHD4gCYpcDEHwu-RShJ1qkYUrEBTxMXccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g12
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/76658" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رومانو:
کوناته به رئال مادرید
هیر وی گو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76657" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دور چهارم مذاکرات اسرائیل و لبنان توی واشنگتن در حال برگزاری هست.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76656" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">معاون شهردار تهران:
برای تشییع جنازه سید علی خامنه ای ۳ روز مراسم بدرقه در قم، مشهد و تهران برگزار خواهد شد
آمادگی حضور ۱۵ تا ۲۰ میلیون نفر را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76655" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">میگم اعتراضات امروز دانش آموزا به کجا رسید؟
انگار تاریخ امتحانات رو یه هفته انداختن جلوتر که
😂
😂
😂
😂
😂
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76654" target="_blank">📅 16:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حصین به نصف رپفارس رید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76653" target="_blank">📅 16:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76652" target="_blank">📅 16:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76651" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">چقد داشت تلاش میکرد وقتی میگه کون لباش غنچه نشه</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76650" target="_blank">📅 16:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozLqbGDKunCDyLasKhksS66tYpvJZAajuHbMgSvmhom8jrYLq026Tv2uQGGaHzA4o9bEElTb-d_qK0sNjXXvWwsLMrzmAQ5ofNUX2at12d6bQaH4jLTPPAkrTQCPQdJ52wizi969Ngtc8H-X3ZPUcKnNVUL-Bno6IGFLRs39hVupueKSvmbEOQesldFGMpnumpfZyzyM8ISa2P6vG0SDFS0d9CHdhJZmjaAyHsfQvIph8DPAoG4V-mRrg-I94ADyhmn5hClzjVyvf44jqi_l15MCcOukgnaEEmN-cT1bQBbvVA19U6Ae6KExDaK0waqzGbSCw8omSbXKjGTgZ4qdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ی مشت کونید همتون</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76648" target="_blank">📅 16:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76647">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حصین یجور میگه ویسایی که ازم پخش شده کار Ai عه انگار من موزیک دادم گفتم "گنگ مثل رهبری، مثل حماس پی حماسه و..." دهن سرویس محتوای ویسارو تو موزیکاتم میگفتی دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76647" target="_blank">📅 15:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76646">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کصکش دیسای پنج سالو جمع کرد تو یه ویدیو ۲ دقیقه ای جواب داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76646" target="_blank">📅 15:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76645">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حصین بنده خدا انقد فضای رپ کیرشه هنوز نمیدونه دکی مهاجرت کرده فک میکنه ساریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76645" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76644">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آنشرلی با موهای قرمز
😂
😂</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76644" target="_blank">📅 15:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76642">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76642" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76640">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">به حصین دیس بک بده</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76640" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76639">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پوری پاشو پسر</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76639" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گنگ مارو تروقران، به چاقو میگه نایف</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76638" target="_blank">📅 15:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حصین به نصف رپفارس رید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/76637" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWBHu6IRTz1ibPNKxGOoLX0Qcqho7okapvQuh069T3tXhlBFMqPa4U5D1qtgEsKszmu63bznV3e30HbO7STbpEPoeNo7IOq-_LxYUEqm1dNEFV5y7x9UKLlG7PTfPsOF8PLWxy1GlFiTLxjfafPTL3MazGd82Z5ZgAGzwRd2s44tkHQv5xe_FeyIfHucgWVogJdtHeRuOtgTJrq901_JdSI7EhzqXsFMT9MopuYJbJY9fN_Wl6uL7bAeS6Ehjjjvg9MnoOYdZjcN2CvbElY2nTSRZHzV34LzoWreWFxhivfd4AhNBy2BCCZTw0ETq1VrKUf7QboQvtG5UlvAWEQrNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط ابر بنده خدا چرا اوبش زد بالا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76634" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده، فروش سرور های نامحدود اختصاصی باز شد  یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰  برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76633" target="_blank">📅 14:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده،
فروش سرور های نامحدود اختصاصی باز شد
یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰
برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps
🔤
@Behdad_sps</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76632" target="_blank">📅 14:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اینترنت بین الملل باز نشده
درواقع فقط فیلترشکن های رایگان وصل شدن
#MVSGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76631" target="_blank">📅 14:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سفارت اسپانیا هم مثل سفارت فرانسه و آلمان تو ایران باز شدن و شروع و از سرگیری فعالیتشون رو اعلام کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76629" target="_blank">📅 14:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ12zxAdzKmCA_VGF0VuvRY7N6QNJMxqoJo1mXcU95-gmWOYaSW0XSEltuNQC9Oo9LdynVzeNEFhdpkPc9Rfwa6Fkxm6IchKBmKBtOVoLtXd1FnV3617MhjcYpWpvB7J5nQ2Kx-Oh0tkw-t1IrVC1NSwCpgNC5kFx5WDZ5s8v7rSOsLgLVQtRLaHrNVdEK-kcXyuQkC1YznSfdhDPdb8Y_p_hAYNHXKOIi3vULN02ve1TkBCQUiAPp69aspszwA0_vf8XZTkij12G848CgwvBsx0uXBBEZq3FZGNjWhx9yBEFPixRoJpG7JlqNPAQ1vWTBFSe1YleZ3ezzmb1Ijlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76628" target="_blank">📅 14:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۰۲۱کید من هی میخوام مسخرت نکنم، بعد تو رفتی کیت آرسنال پوشیدی با پرچم ایران داری آهنگ انگلیسی میخونی برای فیفا که پرچم شیر و خورشید رو تو استدیوم های آمریکا بن کرده، حله.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76627" target="_blank">📅 14:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تنگه کص نمکی رو باز کنید تا کیر اتمی نزدم بهتون</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76626" target="_blank">📅 13:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76625">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کارت فان هیپ هاپ هنوز استفاده نشده و زیر آستین ژنرال ها و پاسدار های ارتش دو کشور قایم شده، برای همین تو گزینه ها نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76625" target="_blank">📅 13:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76624">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوبار نوشتم در نهایت، ببخشید سواد ندارم شما یه بارشو بخونید</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76624" target="_blank">📅 13:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-poll">
<h4>📊 به نظرتون در نهایت کیا باعث میشن در نهایت خار این آتش‌بس و توافق گاییده شه؟</h4>
<ul>
<li>✓ تندرو های داخلی</li>
<li>✓ نتانیاهو و ارتش اسرائیل</li>
<li>✓ جمهوری خواه های تندروی آمریکا</li>
<li>✓ هیچکی نمیتونه کیر ترامپو باقرو بخوره و در نهایت آمریکا با ایران توافق میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76623" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فایننشال تایم: رافائل گروسی اعلام کرد قزاقستان آماده است تا ذخایر اورانیوم 60% ایران را در صورت دستیابی به توافق ایران آمریکا، تو خاک خودش نگه داره.
@FuunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76621" target="_blank">📅 13:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76620">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLE7VPPNYM-hkWC7vWdfLP0_O8S-AHjXzR3m4IDPyn549Db8d8o0T5x1IuIeko_xBGgLpy3GmvoemOmh_YIOdc_-Drm7EbndOtdHJaSiwRMu0N_b8kNoDDK3wBm8zacvIXBkwRhsm630L5DnJMmfWDSeBs-r6D1Z69imqRIqvE-O592z2dWO0CWa79x2rpuuM6uOLHC-vvvfSV4WDTZTgt0gC5UFb_v3LkYb55_b44LMBcBFPWzGGVzanh1PaFTjnykd1BkVlQJUoITyuicjVkAHm_shHM8jJ31o-RRt2BY7dEVK887tYUGOA1rZ3t2SJ3Y-lOd2qA7MR9U2QImjNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل دستور تخلیه کل نبطیه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76620" target="_blank">📅 13:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76619" target="_blank">📅 12:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🍓🦢</strong></div>
<div class="tg-text">میشه اینقدر با مزه بازی در نیاری این بچه یه سال تو اتاق درس خونده رفته برا حقش دختر بازیو جا دیگه هم می تونه با اینکه کنکوری نیستم قشنگ نبود حرفتون</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76618" target="_blank">📅 12:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76617">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76617" target="_blank">📅 12:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=N7lt6hqrtrhL9LBv9BCrw92a9Gm2UGa5BB47NLywHm9ZwoF8mwOwRhAocB57nVfCEp23pnpviksvUxHa7F-m4vemAwmP2DjsN6acagWbYHVZeNX8rDRRSH2pFl5Ih1gjb5eeuCoFgW3UISDHeCbw2-rTVjycXeGVMGontc2EJ5-6HJxLcysIjZwbiPx1KfIkZoI0nINuvxN_RAGbPYSN5sn9wU77tzSjuqxR5iz8lNnbW4EWFrf7GJEya5veGrzGNZcimVXl-y0ibk9vLRD5X8s08DZh0p446NuoVIhy9aqQt90dWbuaWJZtMxUlm9oMhTG-0NHGQNEdyaPuQYgEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d5a4fd22.mp4?token=N7lt6hqrtrhL9LBv9BCrw92a9Gm2UGa5BB47NLywHm9ZwoF8mwOwRhAocB57nVfCEp23pnpviksvUxHa7F-m4vemAwmP2DjsN6acagWbYHVZeNX8rDRRSH2pFl5Ih1gjb5eeuCoFgW3UISDHeCbw2-rTVjycXeGVMGontc2EJ5-6HJxLcysIjZwbiPx1KfIkZoI0nINuvxN_RAGbPYSN5sn9wU77tzSjuqxR5iz8lNnbW4EWFrf7GJEya5veGrzGNZcimVXl-y0ibk9vLRD5X8s08DZh0p446NuoVIhy9aqQt90dWbuaWJZtMxUlm9oMhTG-0NHGQNEdyaPuQYgEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون آغاز تجمع دانش آموزان مخالف تاثیر قطعی معدل
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76616" target="_blank">📅 12:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76615" target="_blank">📅 12:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76614">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYoung Roque</strong></div>
<div class="tg-text">حاجی توافق شد؟؟؟
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76614" target="_blank">📅 12:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76613">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czDZyKDcB2pm-PyIUR7sNwn5dJghamELgUyebFox32fSD4bS6onhcbAH2NjxkJxoWDMOA5GnEu2llL7WZzLT3tpcRGlISxMs5XuUCaos3a4OBhKx59dQLMGNu_YbrDdw1TnT6Do8TAByxfbQgNeOGapg62rd_5B8CjyNheRCemjQGH400h1SvYyGDw6wBK7MLoc8zI3DjgqfxfeBMubiAdOMf3RMJhWNmirk4KE4xSV3s3zT-SAxESQLi0p4iWCOPFRhGYioroVugGeKKfxdj2py3162pobRo6c876B4-7LzaKtV0lUQmzMPWvCP3fMaZ5SYnqt2VU4LRK6103ekSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: ترامپ به نتانیاهو گفته تو یه دیوونه روانی خل و چل هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان همین الان حملات به بیروت رو متوقف کن  @Funhiphop | ALI</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76613" target="_blank">📅 12:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76612">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دانش آموزان الان در مقابل وزارت آموزش و پرورش مشغول اعتراض هستند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76612" target="_blank">📅 12:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آکسیوس:
ترامپ به نتانیاهو گفته تو یه
دیوونه روانی خل و چل
هستی, اگه من نبودم تا حالا صدبار کرده بودنت تو زندان
همین الان حملات به بیروت رو متوقف کن
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76611" target="_blank">📅 11:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76610">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaiZDLv-9ercnJkwA-iWNwUXIhUaqXSl3DYrr4a57QpEGI7S67Jw_6MC9EKvm1IsHPSxDJsa4dyHs8X2GWpaO16qSh6uznSmKepmTP9WI5geH5VHpnM9SAm_ewq9Nsn4b_PkYuCbXFVW-Sw167kz27mCrHgCCmIuyd-YS5YNgpfSNRnaXvZDMUvrR3aWg2KTWZ1cw_VsqLbZTiei-GxWeR39t92jvIhEbxNtTWMxaSy6IkJbw0sCWm4jzzYAPgLyya9Gs500SF5qQjcXAm_6JbzdwIYqoUW4VmufZxlhiJSonNX9i1JL_HJCGM3vMtzg8FewdeGA-ny1FAbPLrDKcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه مادرجنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76610" target="_blank">📅 11:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76609">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVnRb2zpRuQtw-59qehLohs-g3jsOuCezhymMG5Gh89KCPYP8S3jApQHFaNA-ySptSIMptd4n5X693GQp3stlEdLAAjnoJy0AQx17qHD9OVNZ-Wi1XxOthciJyhO56NzUzPMp0xL-PsdhiNdvyrIyCrKobpVOISWE8PLpgTKZdFlqiN-xH6ZMWa29uAWlIn2nTiy9JaDSkkTfHo7wlzqGjPYMvdQc0Yg9ISAEOGqna06Id9htP4h0Xnc-BNWypRFgW1AlZ1b49PHQ8zBx-S6v9mwHJI6_bbAp7195z9dRlMb2t7JXxHwqImcBhlhuhOF3BhV3N7HVqtr1UIFbvZrFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون شبی که تل آویو اینجوری روشن بشه روز عید ماست !!
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76609" target="_blank">📅 10:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76608">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQBWbTInncCov7dyYH6IWhq97-BNvpzYJtKwebfjA5KY7Y_nj1KdxIuDG1b3iqTSti9W4trKgn6ijwLtNKYfNgEwYg9QK_O3XUbA-QApDtqiVCdGzKsCIZVuJJ8NcCnlQgkd7BhfVjFXKGzqi1vUVCXKlEf7LXLrl1CE3G0z1bCdEWCzlNQWfbLUaAMukgQt3MoN54jFaqHZJvvw2Ky0EZsG955qCnx8K2VPw6QCQAPCDc9oDM-YTaqDReyM53CAdssHYCj9hYhWl0q6H14-Rjr3WdSwl84OioQjSAJR0-cGmQ-j9vQW35vzi_x4Zplqlsbnc8W7tKOX_BI860KZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت رو بخونید و به پروفایلش دقت نکنید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76608" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76607">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76607" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/76607" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76606">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-cEXbHEUT7pgd5guvjD9nAF7i6axPWlhOOXiFbYdKYgoFfq_X-jVdUenB9f8k9Wy8nTGYbeokRKbEGHGqeuzj7oEYa6NUFKz5Ngsk5YG7qkU2xq3id8-GC2wS576RUYh6nXDUBWdacJv4BHAog4_fGUC_2DTY8w2AbM4LkQdEnJDcj-tFWHXfdF6_ffKTBJAuyH9QoVFfZRvrnkKWNsfFwV3F332V96Ja0Tw1M4ileyRHjMA8cLMHzZ6lAikLCKerc0ylBf6HkoBlEAr95knWOtdACHvOV23wRrLDS5ocil4zYa5-Kml7MKvSastHXW4cAa95HKT2TOCrNU-IQpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r12
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/76606" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76605">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جدی جدی یه لحظه داشتم فک میکردم بیبی و ترامپ با هم دعواشون شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76605" target="_blank">📅 09:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76604">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">امشب، امشب دیگه آتش بس نقض میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76604" target="_blank">📅 08:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">م   ج   :
ممکن است طی هفته‌ی آینده به توافق برسیم.
یک توافق صلح با ایران می‌تواند حتی بهتر از یک پیروزی نظامی باشد.
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر را بگیرم.
امروز یک مشکل کوچک پیش آمد — ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند.
پس من با حزب‌الله صحبت کردم و گفتم شلیک نکنید، و با بیبی صحبت کردم و گفتم شلیک نکنید، و هر دو از شلیک به یکدیگر دست کشیدند.
🥰
😊
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76601" target="_blank">📅 01:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBCooe1uP9PCC5sPqwjLD40uXfRvR89txsj7Cmsb2D6ZGT80lu_CSv9gZ9FmWPBJPaBK0ADUgPSLWKFPVzaX46qsw__wsYqI58yQwBm-r6zE6rS6D3hYWk_k7z-inZleybCzQcW9vc-UzXzlZ9Qy_9fyXmPz2yk7W3u6GTK0Lop5KAXM8GgJZFhZRkMwXklauewPE_kMF0CKZ469AbzSErleMAO2LqlAhdnEE6KkjeQzFsEM1a5BVWUHj_3MzbLqvwHv73zWT4QCQdz52KrKlwJ2nPnq2ht2kh_8PzyzJI--koHkHkBF2ClFfID6PNlsaE5kqth1uEHxDM2WctPAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76600" target="_blank">📅 00:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76599" target="_blank">📅 00:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76598">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس جزئی ترامپ را رد کرد
نماینده حزب‌الله در پارلمان لبنان اعلام کرد که پیشنهاد آمریکا مبنی بر توقف عملیات مقاومت در مقابل عدم حمله اسرائیل به ضاحیه جنوبی بیروت غیرقابل قبول است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76598" target="_blank">📅 00:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76596">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو:
امشب با رئیس‌جمهور ترامپ صحبت کردم و به او گفتم اگر حزب‌الله دست از حمله به شهرها و شهروندان ما برندارد، اسرائیل اهداف تروریستی در بیروت را هدف قرار خواهد داد.
این موضع ما ثابت است.
همزمان، ارتش اسرائیل به عملیات برنامه‌ریزی‌شده خود در جنوب لبنان ادامه خواهد داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76596" target="_blank">📅 23:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76595">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر دفاع اسرائیل:
واشنگتن ما را از دفاع از شهرهای شمالی باز نمی‌دارد و به هر جایی که در لبنان لازم باشد می‌رسیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76595" target="_blank">📅 22:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76592">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تشکر و قدردانی حصین از بچهای سپاه قدس که امین منیجر پخش کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76592" target="_blank">📅 22:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76591">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏تحرک جت های جنگنده در تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76591" target="_blank">📅 21:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76590">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76590" target="_blank">📅 21:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76589">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حزب الله پنج دقیقه بعد از توییت ترامپ به شمال اسرائیل حمله راکتی کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76589" target="_blank">📅 21:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دقت کردید که الگوی آتش بس لبنان هم دقیقا مثل الگوی آتش بس جنگ ۴۰ روزه بود؟
آتش بس بعد از یک تهدید بزرگ
احساس میکنم همه چیز داره طبق برنامه پیش میره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76587" target="_blank">📅 21:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد.
@FuunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76586" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">توئیت جدید ترامپ:
من یک تماس بسیار سازنده با نخست‌وزیر بیبی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده است. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردند که تمام تیراندازی‌ها متوقف شود — اسرائیل به آنها حمله نخواهد کرد و آنها نیز به اسرائیل حمله نخواهند کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76585" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یادتون باشه ترامپ داره یک شطرنج ۶۰ بعدی رو بازی میکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76584" target="_blank">📅 21:04 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
