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
<img src="https://cdn4.telesco.pe/file/pzGnC89cWHWwgTakiB4-wYMV4MyEG5q8n517ACjJFe8O_y54u4s-Lv2UGk_ADIvsibavbNG2EdUiWb0-0Zd1dA1eSfDWYioGeDqKSi98Xukxr6zrOQA8Q8EnJDc8_I4mj1iUHVgMOrpTkmMGxwel5cEihli0FDNhhuRw3eAeq1aEG-r_SHBX6vMJ7tKWh8SoI3I1BlBM0ShmqhfiX71uSsRpX-eOZF7AtVDjIrcmNHg6mC6N7J5xhg6kHTDmzQ_nchD3aJ3TtkTaksHSjRxKu-5vMY6_D0dcq3h5zqVLUkD0PUZmKKmsmCvH70T6XP--ky0-_gjoj5nb3_rD9t4yyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 05:12:38</div>
<hr>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrPU9VyT0U7GI94a7685QUHNF3n18UJIIJNL5zheb3jw3HYADZI6EWiNpGfTRzRB5jar6-86ozA2RmH1ZEYPhY1hQ8FL5WG33HZ0Jfmjf26YBnPD-fyFjGzLJWYFKRNb7y-pyT5MeTOjeQfWi8y8IQmpaMuOJIWkh2BCUwaGuKI-JAdXuyPDf8-A7o69FEIcGQw6ooE1E6Mtez5q3vw7lczSp-xENdJXJOXzQgfI7sqorjQmhkmy-H4NClThfVkipO8UVmoeRazn4bAKhmrI51GiW31MH_MAffs3MyydZt-EyRmHpi7GNw2UT0oJXtCCJp_Vf8itIBWe6I7RUSA4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمنا می‌کنم هر کجای این کشور نابغه پرور که هستید همین الان متوقف شید و سعی کنید یه مدت تحلیل و تفکر و کلا اینجور چیزا رو بذارید کنار ممنون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/funhiphop/77684" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یه کودن زاده‌ای هم نیم ساعت پیش اینارو گفته بود ولی از شدت کصشعر دلم نیومده بود بذارم:
ما امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود.
این ۹۵٪ از هدف ما بود. و، آنها این کار را به قدرتمندترین شکل ممکن انجام داده‌اند.
ما، آه، با ایران توافق کردیم.
معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
اه، نیروهای ما خیلی زود شروع به بازگشت خواهند کرد.
تقریباً، اه، تقریباً کامل شده است.
ما هر چیزی که می‌خواستیم را گرفتیم. نکته بزرگ این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت.
آنها بندی داشتند که توسعه نخواهند داد. من گفتم، «خرید چطور؟» آنها گفتند، «خب، ما آن را پوشش ندادیم.» پس دو روز بعد آنها با آن هم موافقت کردند.
ما هر چیزی که می‌خواستیم را گرفتیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/funhiphop/77683" target="_blank">📅 03:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77682">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عرازشه ای که میگید آمریکا نباید فوتبال و سیاست رو باهم قاطی کنه پس میشه بگید دقیقا سردار آزمون چرا دعوت نشد؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/77682" target="_blank">📅 02:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfAIyU0QqWzJC3rpjyXKwPtVpNC3RCDU3QDGHIDsK4K2mUNmpnZ6CNwbQXBBeXyIubdJy9DYo4XAmpQ1lmeK7H0YrsbhBO9KsNYomjCgJ30mXBic6-E22AqVlefuPzWwN_4SlAiUc_WR2-YrReAfYgmnzqsqlI4Mg4_3fjdXb19eExYYO77uveS81k2Vp8Ms_cpEJRN7G2Q_xrLVz86fEvKnZRBT4X30QhuLqLmhRPPTcUViUPoQUKcs6f31b6ILJ7FTj5Bd1fAG0d60Z1oVt0kmCqbKltYs0di7bGpJS7iplYPzOxmlEJXIb0IdYwYJ-kclbTi0-aOurVvTxKmhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ترور بیکینی باتم اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77681" target="_blank">📅 01:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">میناب انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/funhiphop/77680" target="_blank">📅 01:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تسنیم: متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/77679" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چه علاقه‌ای به گوز داری مشتی</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/funhiphop/77678" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بازم گوز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/77677" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/77676" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEjBHbIJDJaFkPv8pfWlwgzn0aY4BNIbSxy7naQHsZfza6gMkFqD89ut810JmS7IOq1535Ct2bpudKxD_JPWof-Ccy_w6SiExKBbpDqUcav4ugvL8fnl3J7bfWn7sbFgy-Qm9XZSevBLgr-yhLeOVXMIEzRGn9zYl3BneIl3ARUsHZdl43c-tBBZop9DwOVYaqLC4aijOqTvN3sKMohURFo0nPEMxvbYIT-QNEIQQMH1lRn8jn2o8RzwZ5Y4Kc54x2QasUTKRyOgingu4Hzox7C1olDMeOR1omJsyUA0RBRFwqrfyAQ1-Pz_hcznZnV0dk1T5zoSYyGBrVG5Hl6Hmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اواکس هم داره فعالیت میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/77675" target="_blank">📅 01:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پرواز سنگین جنگنده های آمریکایی برفراز عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/funhiphop/77674" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گناوه صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/77673" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">درگیری ارتش امریکا و سپاه در خلیج فارس
تایید نشده هنوز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/77672" target="_blank">📅 00:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلام فریب جان هم اکنون صدای توافق از خونه همسایه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/funhiphop/77671" target="_blank">📅 00:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/funhiphop/77670" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77669">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/funhiphop/77669" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرنگار: آیا رژیم ایران عوض شده؟
دالگخیز: بله، نه یک بار بلکه دو بار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77668" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">3 تا توافق رسان KC-135R هم از اروپا دارن میان خاورمیانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77667" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رسانه های مختلف خبر توافقو میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/77666" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77665" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77663" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
فقط برای مدت محدود
💢
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۴ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
---
📦
20 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۴۹ تومن
📦
30 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۷۲ تومن
📦
50 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۹۹ تومن
📦
100 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۱۶۹ تومن
📦
150 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۳۹ تومن
📦
200 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۹۹ تومن
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77662" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvzTrinj1cKhMXS69P41LPtTj61n9mCbsBrm11iqVTn_0xPFRXKiDgyHy7jlWE1WhKUQdiPXU172TWXngR4UIbl8CWkKYGxp-lFcafoXc-tIiqhexTcp9kfvO3_O3ywN6KVNvVMta0PusD2Xbx0g3rfNektCfeLGeKRoOFbmmF7xoEG7JcslG8ruYEi2kQDuytQgmgqJUS-mxE1VhyFCa5EMV_cq2qKCL865kIkWjXPiRjaeAa6F2-_svoF1toC7rOz7PARBnjk5I4LywLsPz3d-2I6OppElc-jUNjJuiq4tvwTiWlCLPLkfjbKHqoDPWic4dJWLIQM3kCW3CjTjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/funhiphop/77661" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/77660" target="_blank">📅 23:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromcина</strong></div>
<div class="tg-text">این برای امشبه؟؟؟؟؟</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/77659" target="_blank">📅 22:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=SqC-i4lOdtN-TTAg9p5XDMZrlagK4CruAVfJvBxd0cgDwbbq6eyT0p21nYTWfoFwXPlKALBvshqzmQLOeIM66M7g7lO9-bLn_0oeakD2CBedQiO-aYlq4c_XVBfCbVI3lFzXGObD9Ed_f0svL2KDCZ5aOR5MeZggo8j3cGTysIXCiVfYfaO6nPiXrfo2p__Xy14Ix-Vac4zISto0Sjsqpkgbtud1kX_1pdn8z8hcoULfyWPiokGlt9PEW9xuJA4obestBJRhkaOOtaif6XsK9ZOxddEAFzmCP67G-AIEsGZlPl4xb6K0ymySqmqzY0f8ZRGOW0Y3tg9S2kkCdy2dnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=SqC-i4lOdtN-TTAg9p5XDMZrlagK4CruAVfJvBxd0cgDwbbq6eyT0p21nYTWfoFwXPlKALBvshqzmQLOeIM66M7g7lO9-bLn_0oeakD2CBedQiO-aYlq4c_XVBfCbVI3lFzXGObD9Ed_f0svL2KDCZ5aOR5MeZggo8j3cGTysIXCiVfYfaO6nPiXrfo2p__Xy14Ix-Vac4zISto0Sjsqpkgbtud1kX_1pdn8z8hcoULfyWPiokGlt9PEW9xuJA4obestBJRhkaOOtaif6XsK9ZOxddEAFzmCP67G-AIEsGZlPl4xb6K0ymySqmqzY0f8ZRGOW0Y3tg9S2kkCdy2dnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته  باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/77658" target="_blank">📅 22:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته
باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/77657" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">توووی دروازه
مکزیک گل زد
اولین گل جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/77656" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77655">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جام جهانی شروع شدددددد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77655" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqHaj9mjjeZSTeZ53c3nAWpREtY8igG7LReMvl3YiM2IePK0YdoBpW65wQveApjJ_iGwpPeivbvsWNQQBckUKUWWJ6wz978X9PHRs4c_KXeU3EPdNjudc7qMKul3xUpvDqpQ-c4PIUNzs5hWcl_wIZLOSVab4xvpLubTJViMgwvnrefSHS4FEkStiV8hEvQKTHMVe4ApNydXhFTG0JGbE5lQCuLs4lR3-k-qCsaL4caCG_sSwkhwyNsSYuJJZjca0i4vBhOmiokieKdsxnYE_pcFUZ64iOSWvpGwLfKoTRuh76GjJHMYkhxYBp5BcGbATtZ8GJqwp3jGNOaxoCioeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس هنوز نمی‌دونه توافق نهایی شده:
من از نمایندگانی بودم که خلیج خارگ و نیروهای پشتیبان آن را از نزدیک دیده‌ام؛ پای ناپاک شما به آنجا نخواهد رسید و اگر بیایید، زنده باز نخواهید گشت.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77654" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77653" target="_blank">📅 22:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دالگخیز
🔙
عمو ترامپ  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77652" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیویورک تایمز: امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77651" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77650">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به نیویورک پست:
توافق مورد انتظار برای آغاز مذاکرات هسته‌ای با تهران «تقریباً کاملاً نهایی شده است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77650" target="_blank">📅 21:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دیبالا هم از خودشونه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77649" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ریدم
عادل فردوسی دیبالا رو بعنوان مهمون اورده برنامش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77648" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77647" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/77646" target="_blank">📅 21:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juG2IV81LYT0XvVTW8A7HTUIgupgD-ig63EQm_TqyHkfJdEpNvZ3Ep6FDIoXbEfoKRtXRZpuPlKBFxgbxYgmlxIpVn1F1q4EI4iutqVYZANYIJ41qQb61vbIOeI32fRusDD99cJ8Zn9nOG5ht0s6le9ZljdZjwkWAhS_7ttO-JXNdTCziVr-6lLK0uLUk12ruOFIqkttijQSalBp1pv_5pjaXp3oNsfw0r9wjPVAs7P_Hq0Wb1rGmqYhs1c6nazbSzC1drSxpWdNXyohefmK1bmznEoOCflZfks6TA_94abCjn0vOxoYvqW9jvmm0Sst9XYHFMCmdNdNP8H5Vyx_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل ادامه خواهد داشت — زمان و مکان امضا به زودی اعلام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/77645" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07. Pashmam</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/77644" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">06. Adama</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/77643" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">05. Khatereh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/funhiphop/77642" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">04. Setareh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77641" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/77641" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">03. Tehran</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77640" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/77640" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">02. Beef</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/77639" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">01. Dor Dor</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/funhiphop/77638" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBPIG8t8_6ZtTuNlxoKAeRDHknEg1Gh25z_VsN2Ep01z_KlAplDLNmzou7s2_vrDbV9rjzA4wjUWaWn68Wj9O5NuAXmAdBJZcO6SLPfFX7TgQlAHQUrFKJFVQayaOXGsc_iBwjxfkzfkSf_bUJiBCQji_Ct6g5vbHsvsUlpkMCgGHbhTBFmghsiQQnkIWGod8Vh2EX1zRB_xgNKBXcD8NjKscR0LT9XK_4jc1PIL61eLdCoK7Mj7DFVbINhmg2T5zK9qTCb8hhnt-NMeCnqPuepklcdohtkCnZAWZAjhs4GnCoXfpbtbaWrq_63t1TSRZ03F1lwH1Eh59ZLDX5KpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید مانیاک به نام تیریپ تو تهران منتشر شد
📺
YouTube
🪀
Spotify
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/77637" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بالاخره بعد مددت ها یه ترک خوب از تیجی شنیدم، همونم خودش نداده لیک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/77636" target="_blank">📅 19:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYC3xrw8HVoUKybKUesllK6YATQ-q4_bp8TaZaAEHRQ3Fvie9GjtJEyfMh55dPVqzM9-oDqWuJjXtJUT04A_WGIPJgJlEUljGgPW8Xz_ZnBglnmJbCxE_U2OFa99kghyQ1HRPJ8MPwEI2AeYZ4Bk4-FSz2RaPbQGFzxGSgq7QzcECfOyoS0ts-kA-YsWgc5YjZb3qjlqhs5BkE5HPfdULEcZkq8tPx8pIU1oc7hbjne7RqPbT61ge54_iEaOy59ojmlinP3mmXmeFp3VOXoyOkPQgb3JYb9Bx0f3Gi3IboBF29-0ZIQvC-zZ9Bb1P96tZeBPRydFFuI7tgFcFBSLuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندساله که اسم توییتر عوض شده و شده X ولی گوشیه من هنوز توییتر نوشته، حس نوستالژیک و قشنگی داره‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77635" target="_blank">📅 18:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رامین بچه کونی:
برای اتفاقات روی سکوها آماده هستیم و نمیذاریم بازی با انگلیس تکرار شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77634" target="_blank">📅 18:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">با اکانت توییترم که کنار اسمم
🇮🇱
🎒
🇮🇷
🇺🇸
هست،
توییت زدم وطنم وتنم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77633" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLxXmW65FRVFEWs3xDhP_TS9BJzyJIIpPW-5x4VAf0_drpBM5DCoxjb4y6v0aqGJI02SXJqMpNg3yENpfZS7Hf1e7KrdK-T9o4qEDm6CJyrfbaFIoCzH1MhzwJflZxW6V78KLM6UvPLcFPE_HkOR-X9_PLqqBydZ4tbVfGwIGooUjWTw0dQY3dgbwslPtlhb9wPNr_ceHvRXSjBS2WwCBRF7DEnctk97n9d5pg9O9W8zlUpddJ5PDHAr6PaINoJqPTk8t2Y9Gat6bsB1O1RKs2Mk1TnMmSLxxor6-VwdjDkE4YpRbpCnkbkZY-1Jr94oILbR-3LhUcvB5Ul_nX23ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جون عزیزتون این چطور پزشک شده</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77632" target="_blank">📅 18:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0UJ4N0dTukUJ95ZBzLZXHiB1yh92x0ct50fLCe9mFrH8XqK3X5BUKwfI8HMjMcafsqxWUXVcvrnUzZpjT7oCWzF3ZfDfi59SaPT4i53A8iYxoWlPn-H89moFJGTncO_3f7HrO-GqVj5vTa5lJnVmJhQ8Pm7Wwcm3dhCpn8xYnZaBZvQSHNPDgUI7MugXQEeJhNFn340YCALn6VNnZpQtdseJLihR8PdfTyIbJylIhe2Zu0xq1QFLrvrz5bZX0aJTJYXU3__s0c16ESAx7BpkBKH752eKU1YXBjxFaW1aZcFCyaQCkOcUqMBrgY-WhIpsw9v7EFU43efGYpmrXHHqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام اسراییل برای حملات امشب لیست ترور داده !!!!
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77631" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6rhph7xNVCLnasprwn-lL25Va6U86OKVXZGajtPe1YegkK0RNtP9Xjd71JOzcQQemIgH3PMnAnLj4vd8KF_sO8CyfzBVZM0i16keDb0PmgA7-WXP1VcC1Gwj6toniw5c9MUiC7ZYrWJ-GUEnJEQT-jG9xFTiagKh-52NKpDT0U_nWt7iDz9nOrMeMKoNuEr7F6BpnvEcxafl9Qaj98ABzptRoFulNs55IKwuAnffvY5kINJWzFWwLw7x4nNHaQofIsviN3f0XeVmHvvbUitgwSTqi5q9Wzs3O-0QyCKVpIf1T9eB4qW5iG9cs17OjtAMdTGJoAXPOxaThqUfGzm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد خیابانی : اسم اصلی من جمشید هستش نه جواد.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77630" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77629" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3W18AGIg6LQoAtC_SVyCyQJsQ17BPaFHvxMMIB7nJRsraiC9i242mp_iSDon1KFwaM4IYKs5rAtqVtDE4jx-nqGxqWTGmA-OlNeVdJHP3xSKIdPCsZtNMwt7_1B5GxLecwtrkLwjM1zpVcB47-ZsZxSEt9oTXeNidB_OtCjERahlQhPxzRKrQBAgDfwUvMWK-i_45f8-7tZC_rAXc4-5aEmKUmdSGaTrsAknJ5c5bPg_9KC3P-tjdodWu6Bwzf9tl3Q_T47PoYILTPKLkQUagsbzJRhM83yWlITwrQoCTzv_M656PT2iG49dXI17beSANLcrHBz2RihxRx_0NMWAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g21
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77628" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=aOBYFjvpB-THWFIAVqXo5nkW07_dlQwLWJugfkxQfUN1RSJylh9hzCMpLzJp4j2jnUbhkw5MlsbOUkvC2Q-T3hrcx7fD-exVNkxe05J6cJSutyWVbiHsdtuXo6tmjUsgZ2CccUuP_oSKdcgfMDbg1RCI-ylOt-o75IHnrcZH_5LhXNZnVuF-eXDOjlZTR3muSAlnSzY09xbvbOBRQPA7oV2tGlNZQtBfdyBiIzzBedyHnsbtwrn3Mr_luhRkGHwS2rYgK9qE8h6zaCfQ7jqSWOXpNZ2bYIdOFXSJ86ZoFjXICQc2enU5HIYyQPipMECFdrNCq9fo1BHEMm8nU96lww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=aOBYFjvpB-THWFIAVqXo5nkW07_dlQwLWJugfkxQfUN1RSJylh9hzCMpLzJp4j2jnUbhkw5MlsbOUkvC2Q-T3hrcx7fD-exVNkxe05J6cJSutyWVbiHsdtuXo6tmjUsgZ2CccUuP_oSKdcgfMDbg1RCI-ylOt-o75IHnrcZH_5LhXNZnVuF-eXDOjlZTR3muSAlnSzY09xbvbOBRQPA7oV2tGlNZQtBfdyBiIzzBedyHnsbtwrn3Mr_luhRkGHwS2rYgK9qE8h6zaCfQ7jqSWOXpNZ2bYIdOFXSJ86ZoFjXICQc2enU5HIYyQPipMECFdrNCq9fo1BHEMm8nU96lww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز درباره مدت زمان جنگ با ایران:
من دوست دارم همین حالا یک توافق انجام دهم، کمتر از 3 یا 4 هفته باقی مانده است؛ وقتی این کار را انجام دهید، می‌توانید یک قدم جلوتر بروید.
نمی‌دانم آیا آمریکا تمایل دارد کاری را انجام دهد که من واقعاً ترجیح می‌دهم انجام دهم یا نه (تصرف خارک). ما در دو جنگ 13 سرباز از دست داده‌ایم؛ هیچ‌کدام در ونزوئلا نبود، و ما کشور را تصرف کردیم. در ایران 13 نفر از دست دادیم.
در ویتنام، صدها هزار نفر از دست دادیم. آنها دیوانه می‌شوند چون من سه ماه در ایران بوده‌ام؛ من آن کشور را ویران کرده‌ام.
آنها به من گفتند که شما گفتید سریع‌تر از جنگ با ایران خارج می‌شوید. خوب، الان وضعیت بسیار بزرگ‌تری است چون ما بهتر از هر کسی که انتظار می‌رفت در چنین زمانی آن را انجام دهد، کار کرده‌ایم.
ببینید، ما 19 سال در ویتنام بودیم و کار را انجام ندادیم چون رهبری مناسبی نداشتیم، صادقانه بگویم. اگر من بودم، آن جنگ را ظرف 3 الی 4 ماه تمام می‌کردم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/funhiphop/77626" target="_blank">📅 17:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=ItAQOBqTkvihxaRA3TfQQ496hYTrryT_iiEGp12nrve1V5rKpfK2Q0hNFQoY2eabag_5DUM93zGZXsHJv25PK0NhjH18Sh3Bd7nW_ebYg__fWei8F5GaePCjGOyoh1akmuQ65lnODDrnp40aUdqHh_iu1wInzk1wICA05a94DMntxjwSTXTbLji8L1dhe3HHnBgR38ptW8CIKUpHMMC9LKpmcoJ9xGcpIZdmoW6DAV3d3YoqT4sl7ozMboplXggxNJsl3SO83YSmObxHFojne7Z7OKOTtVKM-KvPWW7VFl-rpeJO1jCog_w1TF10kJ-F_IFvlQpP3ZPzIsZvGXDF5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=ItAQOBqTkvihxaRA3TfQQ496hYTrryT_iiEGp12nrve1V5rKpfK2Q0hNFQoY2eabag_5DUM93zGZXsHJv25PK0NhjH18Sh3Bd7nW_ebYg__fWei8F5GaePCjGOyoh1akmuQ65lnODDrnp40aUdqHh_iu1wInzk1wICA05a94DMntxjwSTXTbLji8L1dhe3HHnBgR38ptW8CIKUpHMMC9LKpmcoJ9xGcpIZdmoW6DAV3d3YoqT4sl7ozMboplXggxNJsl3SO83YSmObxHFojne7Z7OKOTtVKM-KvPWW7VFl-rpeJO1jCog_w1TF10kJ-F_IFvlQpP3ZPzIsZvGXDF5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز درخصوص ارسال سلاح به معترضان ایران از طریق احزاب کرد عراق:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم؛ کردها ما را نا امید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.»
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند و فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد؛ کردها! من این را به یاد خواهم سپرد...
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/77625" target="_blank">📅 17:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee5717647.mp4?token=ZJSlwKjqLjdFEXGffO9y2HzQzU7g5ndSwqaLDbkLmy81jSrEjp9QgH4GmxVfiv4V8-d-F4ADZM_HEQE6VN1px69FkFMKLl8yjY1DkMLlD2j3JCYr4SE6vGWrmKebBXBkzFEYW_3DAFxDamMcV9SokS5uVeEqlsSwTx0jtn2OK5SDxamjuKJF3HI7pbsmsKsPLHyZ6Ya7_MiJDCbmExhmrPiwdnnSjWbWlTqv4hH1Bf3oQCr-LayD0F-VIILjxOMEi1SU1nJRbSQooeEQBst1oP7cmxgKKV1XRJKib7ZOcrYhocpmwH4DcN-lFrZ-SRYPDv5PNlQKU5kCoGmmIORtWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee5717647.mp4?token=ZJSlwKjqLjdFEXGffO9y2HzQzU7g5ndSwqaLDbkLmy81jSrEjp9QgH4GmxVfiv4V8-d-F4ADZM_HEQE6VN1px69FkFMKLl8yjY1DkMLlD2j3JCYr4SE6vGWrmKebBXBkzFEYW_3DAFxDamMcV9SokS5uVeEqlsSwTx0jtn2OK5SDxamjuKJF3HI7pbsmsKsPLHyZ6Ya7_MiJDCbmExhmrPiwdnnSjWbWlTqv4hH1Bf3oQCr-LayD0F-VIILjxOMEi1SU1nJRbSQooeEQBst1oP7cmxgKKV1XRJKib7ZOcrYhocpmwH4DcN-lFrZ-SRYPDv5PNlQKU5kCoGmmIORtWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز گفت:
امشب بمباران‌های بیشتر و قدرتمندتری (در ایران) خواهد بود. بزرگ‌تر، بزرگ‌تر و قدرتمندتر
فراموش نکنید، ما تمام سامانه‌های پدافند هوایی آن‌ها را از کار انداخته‌ایم و آن‌ها هیچ چیزی برای دفاع از خود ندارند.
منظورم این است که ممکن است سلاح دوش‌پرتاب یا چیز دیگری داشته باشند؛ اما در کل آن‌ها هیچ پدافندی ندارند.
آن‌ها تمام شده‌اند؛ اما روزنامه‌ها و رسانه‌ها از نوشتن آن خودداری می‌کنند. ما می‌توانیم فردا وارد ایران شویم؛ می‌توانیم سرباز بفرستیم. من نمی‌خواهم نیروهای زمینی داشته باشم، اما اگر بخواهم، می‌توانیم گروه کوچکی از سربازان را روی زمین بفرستیم و کل منطقه را تصرف کنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/77624" target="_blank">📅 17:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfcc7606c.mp4?token=k-ujZpDVMRgrrzCPNHZ6trdXggeFELVhddQIR16R9len_PYMMZPNobT-zqAXsfh5Qu1BWLp3ECTlGqSSRP8n8If4c2rQXBBUhciyVq3FpRGpcn0XiVC2GfBSZ9E3AuIQTdzhEXn0PclNpIiCjpJaTGYQY_sLjz5BKKSEDr1RHkvjR0GZ0MNim1nVfYvGY2CH9JcfGnCgASGTzka0dXJh5xhTSjMO2_yR5tKo5zzzF7Gnx9WeWbuQthvnTyn_2SHBIXEr9nyMtzTsDjmkDiyAttnKeOrrDHkN-RmhhXj6KZVlZqfLuYcHffyS5dl45J0LRO4Y_FoJwoTjS2h26NMvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfcc7606c.mp4?token=k-ujZpDVMRgrrzCPNHZ6trdXggeFELVhddQIR16R9len_PYMMZPNobT-zqAXsfh5Qu1BWLp3ECTlGqSSRP8n8If4c2rQXBBUhciyVq3FpRGpcn0XiVC2GfBSZ9E3AuIQTdzhEXn0PclNpIiCjpJaTGYQY_sLjz5BKKSEDr1RHkvjR0GZ0MNim1nVfYvGY2CH9JcfGnCgASGTzka0dXJh5xhTSjMO2_yR5tKo5zzzF7Gnx9WeWbuQthvnTyn_2SHBIXEr9nyMtzTsDjmkDiyAttnKeOrrDHkN-RmhhXj6KZVlZqfLuYcHffyS5dl45J0LRO4Y_FoJwoTjS2h26NMvj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز:
پیام من به مردم ایران این است: آن‌ها می‌ترسند چون اسلحه ندارند، و طرف مقابل اسلحه دارد، و آن‌ها اعتراض می‌کنند و تیر می‌خورند.
رژیم ایران حداقل 40,000 تا 50,000 نفر را کشته است و مردم می‌ترسند. می‌دانید، وقتی یک مسلسل روبروی صورت شما باشد یا وقتی چهار تک‌تیرانداز در چهار ساختمان مختلف به سر مردم شلیک می‌کنند، برگزاری اعتراض سخت است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77623" target="_blank">📅 16:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرنگار: یکی از چیزهایی که دیروز مطرح کردید این بود که اهداف بعدی، پل‌ها و نیروگاه‌های برق خواهند بود؛ آیا این مرحله بعدی است  دونالد ترامپ: ترجیح می‌دهم این کار را نکنم چون وقتی این کار را انجام می‌دهی، مردم هم آسیب می‌بینند. مثل اینکه شنیدم شما به آب اشاره…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/77622" target="_blank">📅 16:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4e5f9e8c.mp4?token=tuM72tDjQrqtT-hKD-GV2u1YqmLR2vpCrkb23EwNFsypjZNRRPyq7PGMSdEapsMJMnFrDxCERBAjrDyuQgDYtW2adl4SXfLPGQ_9vIooSwuZdgsS_Sx3AJ7cHH9j5Umr43oMl0bYayOGG8dXPFO2dVhBrUjGIgzBvBQ2aP4ytIWQ56B6NpJCfizFJLqSwcyzeayUTV4mdhUUMJzCbJW2AceSu0iZ8YgUfgaFV2mTN72HieLFLyZ1xkv5_K7qn9-8HvvCwd5qImtSfEVDg0GJ9e1k9OgaXtK2NxKkZy3OPtiKDotzwQdQc03bDGIqYcsT-0m9u8biUj8zuDUf75UeZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4e5f9e8c.mp4?token=tuM72tDjQrqtT-hKD-GV2u1YqmLR2vpCrkb23EwNFsypjZNRRPyq7PGMSdEapsMJMnFrDxCERBAjrDyuQgDYtW2adl4SXfLPGQ_9vIooSwuZdgsS_Sx3AJ7cHH9j5Umr43oMl0bYayOGG8dXPFO2dVhBrUjGIgzBvBQ2aP4ytIWQ56B6NpJCfizFJLqSwcyzeayUTV4mdhUUMJzCbJW2AceSu0iZ8YgUfgaFV2mTN72HieLFLyZ1xkv5_K7qn9-8HvvCwd5qImtSfEVDg0GJ9e1k9OgaXtK2NxKkZy3OPtiKDotzwQdQc03bDGIqYcsT-0m9u8biUj8zuDUf75UeZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: یکی از چیزهایی که دیروز مطرح کردید این بود که اهداف بعدی، پل‌ها و نیروگاه‌های برق خواهند بود؛ آیا این مرحله بعدی است
دونالد ترامپ: ترجیح می‌دهم این کار را نکنم چون وقتی این کار را انجام می‌دهی، مردم هم آسیب می‌بینند. مثل اینکه شنیدم شما به آب اشاره کردید. آب واقعاً برای آنها یک خسارت ویرانگر است. من می‌توانم این کار را در یک دقیقه انجام دهم، اما مشکل این است که مردم قادر به نوشیدن آب نخواهند بود، بنابراین نمی‌خواهم این کار را انجام دهم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77621" target="_blank">📅 16:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ باز از حکومت ناامید شد داره خایمالی مردمو میکنه</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/77620" target="_blank">📅 16:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چرا فرستادی واسه کردها؟ میفرستادی واسه بلوچ ها</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77619" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: کار برای ایران تمومه. امشب بمباران بزرگی انجام میدیم. اونا میتونن پرچم سفید رو بالا ببرن و بگن ما تسلیم شدیم، آمریکا بزرگترین قدرت دنیاست، الحمداله. واقعاً دوست دارم همین الان با ایران توافق کنم. هدف بعدی ما پل‌های ایرانه. من نمیخوام اینکارو انجام بدم؛…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77618" target="_blank">📅 16:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: کار برای ایران تمومه. امشب بمباران بزرگی انجام میدیم. اونا میتونن پرچم سفید رو بالا ببرن و بگن ما تسلیم شدیم، آمریکا بزرگترین قدرت دنیاست، الحمداله. واقعاً دوست دارم همین الان با ایران توافق کنم. هدف بعدی ما پل‌های ایرانه. من نمیخوام اینکارو انجام بدم؛ چراکه باعث رنجش مردم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77617" target="_blank">📅 16:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77616">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این ترامپ مادرکونی هروقت تهدید کرده نزده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77616" target="_blank">📅 16:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بنام خدای رنگین کمان، تولدت مبارک کیان.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77615" target="_blank">📅 16:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyra9zq9rSsdTQR4nnxCVSJD3FsHAfe8adRj8FUoGO6GeoIzQYsdASt7meozWRQe2_bhtkVj9833CAmwfWhl_PAsyg_Zr-NOTala2psRH0NhIqqIqoy96yVCYDvtZAAH5O-DtSf_GxaH45CISbGqhhpV0a8-0ItQceE_GPZNoo_iVbLeUo3wyv1D2uEaSLBJUN6DY2YWBUrgq7G-4X-eEOe9dCTGwAmGrr-wsu4lDEL2Hg4Hdw-WIOoSBlGR6fG58MTA2GXPCbafzTgekdhDKr5jyy2Acd3SpsGeiAdliyA7axM0tneYWlG23cfE8jvyg7RlvUpWNger8RACXJzAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنام خدای رنگین کمان، تولدت مبارک کیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77614" target="_blank">📅 16:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ:
ایالات متحده امشب بسیار سخت به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمامی دیگر اشکال دفاعی آن، به همراه بخش اعظم توانمندی تهاجمی‌اش از بین رفته است!) ضربه خواهد زد. در زمانی نه چندان دور در آینده، ما جزیره خارگ و سایر نقاط زیرساختی نفت را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت؛ بسیار شبیه به کاری که با ونزوئلا انجام داده‌ایم، که به شکلی عالی هم برای ونزوئلا و هم برای ایالات متحده آمریکا در حال نتیجه دادن است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77613" target="_blank">📅 15:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhv9k5mDHBaxA7cctBL-8Df8e21X0qj_KS0LVlTx2io5CF8xZFKtWqaX7XYMO2yhoQkUHVnZen4V8b6o2Tq9N2Gadvzg_wPtW3M9p9WXsr66YouUU-nyw1HBFSZEHwBwVahJ5gKsX0eIOy_ua1CYkIMzy-g1Evs9M3TNoWl-_Ah6b24NMnOMpsiJj1kq-qSMSaMKXnVx2XcpLejfdQGOB3gmsxKU9WR3PPsM8sArOmSnS-wU40MTCwW4opVX1zq6tn1o7Ya98_eBwH8oYkwnun9Qo91CLluBUs8TV_yo544-O6RkAz5RTcsicgzsQYAHzw2dxFpVI_n3xEGQAFtwYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای جام جهانی آماده اید؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77612" target="_blank">📅 15:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1QQAhg12iarvZ_JVWk_IcmnCoa1px1hnq5_p6vpOYSEuyL9gZnzgNVjo5hKMujpBTSiyqfgkiMDoT8385aoCxOsK7TQEsXWbIQO7SzlIp-lz2ASr_UpW-iY19ANCKEfAa5ObVv1dddTq09cIB1coo48J9gha7pXr2aVmGFimaOYom_3usO59zEgAOH6l3tTGPJvrZnv-rh3EIRhioxMX9Uo3Xu5ZntdQNbesU4W91h6cyN6Ws9_G5OcuLBu6eZc5v_7dMdLOwlGdvcNbIC32yBNVol-U45QCO6EHjKQXcu1lpJidT84Fo3rwv7PjG3JrA8FOCD_B1lsQZQr76cd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77611" target="_blank">📅 14:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX8VBvs8vY4_9sbMpHyKyljp864Du4E6hoQyylKt3RyfHHXfwTDhadX2wCAgorgNbsDmt9CdTXdM1H_070mx-3IvDUDl6a-buhiQ0A9kFgFsi9LC3EkbTDZ8-YOL4tPvRoS5na3olni6I7yJMBTx9jXpo8-CF0JJDizTe6ttStZwrCAG1zMch-_BYp4xCJDAVHr-2Bg0MB0IDWwYwnWKicmAfN6PaOmrtPMyq1T2z8JHsyj-ZV18EWFc6LbZlZ-5LNBvLmV45HOcytwXyd3LVqg4bBez64NCZbx52BFjAKS5aoOb1tEWweNSJ7uJVFAn6nUOlOWf9OJVtO-gzBRCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب داشتم این صحنه رو کابوس میدیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77610" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77609">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdeaXreaSa1miYyvJQ26S0QPhadLH8vqIi5CSKmK3z9acMZH_jatpKvXsa9EgUp9KBMutXY3PXl2qjyiWOZFERrSNc1gVV8vjikDNnEChv8OL8vNYU3WNcCxdPHFou6dHaUWBqfGGLULolOdc4-W7CIb8qiJRLPcgPbvXeTNrE7GBM81KFxM-vP1jHBkVaFjT3JgIFrRy5bXQjjPo7wqx2HGCv3uqqRW5CueKIrhM3g2CYi6N2wKRG43g1hLLps1OECGvtgSw9NVa5f_-pQaAPauwlAqSA3EXHaAaw2MYMakG-Dzdc8oqcu-cjCtdzuJTGL1KssxBOGxSyysegQ0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 گیگ فقط گیگی 2/800 تومان
💥
💥
💥
100 گیگ فقط گیگی 2/990 تومان
💥
💥
💥
50 گیگ فقط گیگی 3/600 تومان
💥
💥
💥
به مدت محدود، ارزان ترین قیمت
❤️
☄️
10 گیگ = 60/000 تومان
💵
20 گیگ = 99/000 تومان
💵
50 گیگ = 180/000 تومان
💵
100 گیگ = 299/000 تومان
💵
200 گیگ = 560/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77609" target="_blank">📅 13:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک خبرنگار آمریکایی:
ترامپ از تبدیل رژیم در حال بررسی سوییچ سیاسی به تغییر رژیم کامل است او معتقد است جمهوری اسلامی هیچگاه ممکن است حکومتی اهلی و عاقل نشود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77608" target="_blank">📅 11:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نقض نقض نقض، تا روز آخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77607" target="_blank">📅 11:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77605">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دریانوردی هند : سه ملوان هندی دیروز در حمله ارتش آمریکا به یک نفتکش نزدیک تنگه هرمز کشته شدند.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77605" target="_blank">📅 10:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77604">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDb_cv3Ag8iXztYYXJWRi5KB-CRLOkjVtwMDG4XUkTIbVFD6sUAH8WE3ESdbDZ4tLEnosnNNlzhRiJuy-WZBSsTSVu6S_q5UASJPj-yoGES7i_6ozRLbBddqIE6geT_B-V17H3LrVFzjVJuKRrWoEAc_XtKCZrfq4arnJ1HnmoxT7-FMbqEef-ZZyHCkFX8VlCPTJ3ZWcqJVOalPWs3x366xKcw5kivGf5hpjCh326h7TyzFl_iaef8yW3MJKWrbIwGS2ZOqiDiBpxRapHqQekY10Bg0kbSAfmwarijtsHk8x6lLPx5YDOvplvL7IExMMUKQ09kvqZHEApbH7VAMtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت یاس از ترک جدید تتلو :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77604" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77603">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77603" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77602">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDHqeFb7V4nDqfpLQsmivvsi_waa2kqJpPwyXhfviLl7fMAfbldHdwe807FlOW7VyGvCAruoJcGOl_n1_1eKoLIN7Gk9SD9PbVkeU2FqfONG-FxblFRtAKS-M2_VS_jCtE87XIIFMzkOje9Rtb_4i0xU_xDFfzzMRlqNfKnZk6Z3UUO2whB1SFmwbGVaKwPNAnayoErdYjR91QYjUkzHYsOVYGoeclZ-5gs8le1MglogF5aMCYNmxXxDBHondW1HPEeckGwhuE5sIPNw7R0UOncjEvX62SvUZhhoD5UjctpwFWihxxCMZw-zBZ7yxBWYncF6dI5oRVwm03qhYTaqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r21
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77602" target="_blank">📅 10:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77601">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57acb15649.mp4?token=fpj354arIdE7KJWCpqVGBFYZ_wemB6xJ9rzkiLoAgLw9mGat_yVNErlY5VmojLjVIr_17UgnobRHt_1PX49I4EHQIZMyQxCm4R_aoh3ONBGrkqfrK5P3Sov5aCzu4sdyLrR6OE_UUdIRdvRfY-t7cGXW48B99K1Vu8IFtHxTNixEeKkA0incYvXGcojiPd6iv_Ic2bGYoXnYv_7hiqW-DDe3TOs9inEvhVCWpRCf6ZfsWQ7-tgViLye6bc6pcO6ufwL48vt_aVCKPzptgsWgKdrvzQNv_JRGj6JgoE4B4h2WAwAikduZ_xQKBNzj6TLMaMQgArZwErk9ro5pvNW13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57acb15649.mp4?token=fpj354arIdE7KJWCpqVGBFYZ_wemB6xJ9rzkiLoAgLw9mGat_yVNErlY5VmojLjVIr_17UgnobRHt_1PX49I4EHQIZMyQxCm4R_aoh3ONBGrkqfrK5P3Sov5aCzu4sdyLrR6OE_UUdIRdvRfY-t7cGXW48B99K1Vu8IFtHxTNixEeKkA0incYvXGcojiPd6iv_Ic2bGYoXnYv_7hiqW-DDe3TOs9inEvhVCWpRCf6ZfsWQ7-tgViLye6bc6pcO6ufwL48vt_aVCKPzptgsWgKdrvzQNv_JRGj6JgoE4B4h2WAwAikduZ_xQKBNzj6TLMaMQgArZwErk9ro5pvNW13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77601" target="_blank">📅 09:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77600">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی: در جواب حملات وحشیانه رژیم جعلی و آدم‌خوار آمریکا و به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، با ۱۲ فروفند موشک محل استقرار جنگنده های F35، F15، F16 آمریکایی و همچنین…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77600" target="_blank">📅 07:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77599">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سناتور لیندسی گراهام:
امیدوارم امشب تغییر رفتاری از سمت ایران رخ دهد.
اگر این باعث نشود آنها پای میز مذاکره بیایند، باید استراتژی خود را تغییر دهید. تمام توان خود را به کار ببرید. آنها را از پا درآورید.
بگذارید مردم ایران به مرور زمان کشورشان را پس بگیرند.
اگر آنها همین الان توافق نکنند، باید اسرائیل را در مسئله ایران آزاد بگذاریم و خودمان هم از نیروی نظامی‌مان استفاده کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77599" target="_blank">📅 07:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77598">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75edca7aa.mp4?token=tvwyyOPAi4rjJrpS2x7PLQHQdzXoFZjA7Dp3EcaPoXTLZgnMFfatWP7WnEcAOC4Y0d46LFcIbDBmisfdDroszpulWn-wL1JCg5QsT2_2-AfWS3T4j_exAe5vSyXrWk-Uw-QpgrzetIkzpbxorMpCuvdToivZBxuLEsOChUbxQCenvgjY-NBZjJyMSRvB65kfYNcLVdWzPLENylSQ0VmdY0VBg1XZQf0JoeNjembxdvqGtiPR7gvU9fXksdf8NHoohbdBmpLsSryiUPj0PhpUC0wpcR3Su56mMmnRxjEmUlO3w2GS16Vvu1dFf4GIGihaw7tLfGFO0DPh6L81UAtoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75edca7aa.mp4?token=tvwyyOPAi4rjJrpS2x7PLQHQdzXoFZjA7Dp3EcaPoXTLZgnMFfatWP7WnEcAOC4Y0d46LFcIbDBmisfdDroszpulWn-wL1JCg5QsT2_2-AfWS3T4j_exAe5vSyXrWk-Uw-QpgrzetIkzpbxorMpCuvdToivZBxuLEsOChUbxQCenvgjY-NBZjJyMSRvB65kfYNcLVdWzPLENylSQ0VmdY0VBg1XZQf0JoeNjembxdvqGtiPR7gvU9fXksdf8NHoohbdBmpLsSryiUPj0PhpUC0wpcR3Su56mMmnRxjEmUlO3w2GS16Vvu1dFf4GIGihaw7tLfGFO0DPh6L81UAtoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
در جواب حملات وحشیانه رژیم جعلی و آدم‌خوار آمریکا و به دنبال افتخار آفرینی های سحرگاه رزمندگان اسلام در سرکوب دشمن متجاوز آمریکایی با توکل به خدای متعال، با
۱۲ فروفند موشک
محل استقرار
جنگنده های F35، F15، F16 آمریکایی
و همچنین تاسیسات مهم ارتش تروریستی آمریکا را هدف قرار دادیم و آن تاسیسات و مقدار زیادی از
جنگنده‌ها را منهدم کردیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77598" target="_blank">📅 06:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77597">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jncJPNwBU1u1JAuKwl4tapSztdVSashVzt7d05aYN75GvUCbQ5sA8j93ly9jPUKMjjs5mWBwX5uiFS_ACLoBF9iJP4rJXA__H8esogJqLvJSyhKTBD5VUNV9Rr-A2Uq5lKv4vxAZC4Hui6D4ROG-cF0XFHQdciLiyabvPBJe-94hmKqMNW51ntjQEIePdIXjHFQBZzGgSSgJ1FqZjeKR7TbjOmmXqI9NY2-LCQfBqTc6sBRJ7i8Cekq439jpA-MEGRMWC7x-CoS_clBRylg7S7ljXXdFSCgyf5eiiyfLq1lUD2GtQrgyD0lgblD7JcpiC984nDLYxci_RSrtD2lPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل نگارش کپشن
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77597" target="_blank">📅 05:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77596">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77596" target="_blank">📅 04:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77594">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=Vbeab0WXYqC19nJd4hidHCm1SdWHFKjlCm16TiD0qSGYZxp4ZTnXHzx4Mgheg_HgesbL-qOul1Ug242W2STz23IVhxZJfYdr5VKDxrUud-4GdJ7wmJWUZoWDMvp9dB1Y-fGCDsvdwipOORaGPcEOalOsm-xEvyL2rcfS74sdcIA8cMqdfT3rvIJOxX78N2scSb6ciLQr3gSKtk3FtMSxrJerYsMCS4QJeT5dZxVk8E_3cTxpCJmEYhiDdDl3k0a7hHp9gogvWPrtrFLxOPz4Z5EFXhDRl7pXK27hroC8IBG6FsNHUyaGqJPoSbpiijuMLCreBtS5xgm-cHyK0oiK_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8c4cfc6c.mp4?token=Vbeab0WXYqC19nJd4hidHCm1SdWHFKjlCm16TiD0qSGYZxp4ZTnXHzx4Mgheg_HgesbL-qOul1Ug242W2STz23IVhxZJfYdr5VKDxrUud-4GdJ7wmJWUZoWDMvp9dB1Y-fGCDsvdwipOORaGPcEOalOsm-xEvyL2rcfS74sdcIA8cMqdfT3rvIJOxX78N2scSb6ciLQr3gSKtk3FtMSxrJerYsMCS4QJeT5dZxVk8E_3cTxpCJmEYhiDdDl3k0a7hHp9gogvWPrtrFLxOPz4Z5EFXhDRl7pXK27hroC8IBG6FsNHUyaGqJPoSbpiijuMLCreBtS5xgm-cHyK0oiK_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام الان با انتشار این فیلم مثل دیشب اعلام کرد که فعلا حملات «دفاعیش» تکمیل و تموم شده تا ببینیم چه پیش خواهد آمد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77594" target="_blank">📅 04:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77592">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمالا الان آمریکا داره خود زنی می‌کنه که حملات سپاه به کرج فراموش شه ولی نه ما نمی‌ذاریم.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77592" target="_blank">📅 04:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77591">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قزوین و مناطق مختلف جنوب کشور باز صدای توقف حملات اومده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77591" target="_blank">📅 04:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77590">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpBF5cHOK3cjzU7gpg2csYuBQBeTkab8f0rMnuTddf3CVirugFl75eoSa-KfXTjhxkZqodG6qwoXINRAxrEqgSLK9rmIZePdNzBA_A-ic6ejnDHoMnwq0913anjWsS66RVJJ5MjAfUp6KuxWYScnM1aIjQz0Dn-jFfBvCwFBp32lP5ozoZVIfbMy8iPEN2cVy4g_x56uvkjTXJigpZh-fc3eDZkR3iYhRomfo8hjUNodt2ksr_fospWoactUhBgNZTw3Z-_kC7au5uigq4z8vGzZDULjtoNeWd38qgh3wfBwMFduOG81xKDAwKSzYnvQl3WSd6mCWf8_ZaFCqjS7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید مجید بالاخره بیدار شد:
تنگه مقدس هرمز را ناامن می‌کنید؟ از سراسر ایران منطقه را برای شما جهنم خواهیم کرد.
این پاسخ به جسارت آمریکایی‌ها در منطقه است، ان‌شاءالله.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77590" target="_blank">📅 04:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77589">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترامپ: بمباران به زودی متوقف می‌شود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77589" target="_blank">📅 04:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77588">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برزیل ۲ ۱ از ایران جلو افتاد تو والیبال
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77588" target="_blank">📅 04:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77586">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اوه اوه  هشدارها و درگیری پدافند در بحرین.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77586" target="_blank">📅 04:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77585">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اوه اوه
هشدارها و درگیری پدافند در بحرین.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77585" target="_blank">📅 04:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77584">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77584" target="_blank">📅 03:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77583">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدای دو انفجار ناشی از حمله‌ی مقتدرانه‌ی سپاه در بندر سیریک در استان هرمزگان.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77583" target="_blank">📅 03:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77582">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صدا سیما به نقل از سپاه پاسداران انقلاب اسلامی: مهر نیوز راست می‌گه، سپاه پایگاه آمریکا تو بحرین رو با پهپاد زده ولی بازی رسانه‌ای دشمن کاری کرد شما نفهمیدید.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77582" target="_blank">📅 03:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77581">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/946d468c47.mp4?token=KHI3D4k5qbs0Q9HJWiwc6p3fSSbPdqXw65gS6v_sbkA7z9WeTaPxQrHFsZYjUVrJJc0XAToh0gnmXKbNpIMZG4ftzh2LoQ7mb3iaa1YDyQJyHdWEmTIxgFjoYo5KqvB0_jozW_S50ZWJnWytN3oHwB1P3cJKnFHQ79-dDi-VgLKaG9vxw5hidhbdCG3SgCG9UUPk5pLECNi7pI4Y3Y3cmK9lfg7kyyVaeqHn8OxgLO2JxOPDj5fcw92gYCiczxeKuFvFax3MshfvNzXWP8dX4-qDChryTaVZQMS1Xe_CBmS_i9y-isTo9afSXmExAfYq5vn024uM5Pszq9bqcX0AwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/946d468c47.mp4?token=KHI3D4k5qbs0Q9HJWiwc6p3fSSbPdqXw65gS6v_sbkA7z9WeTaPxQrHFsZYjUVrJJc0XAToh0gnmXKbNpIMZG4ftzh2LoQ7mb3iaa1YDyQJyHdWEmTIxgFjoYo5KqvB0_jozW_S50ZWJnWytN3oHwB1P3cJKnFHQ79-dDi-VgLKaG9vxw5hidhbdCG3SgCG9UUPk5pLECNi7pI4Y3Y3cmK9lfg7kyyVaeqHn8OxgLO2JxOPDj5fcw92gYCiczxeKuFvFax3MshfvNzXWP8dX4-qDChryTaVZQMS1Xe_CBmS_i9y-isTo9afSXmExAfYq5vn024uM5Pszq9bqcX0AwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر: سپاه امشب هم اون وسط مسطا پاسخ‌هاش رو داده موشک‌هاش رو زده باز شما عقب مونده‌ها داغ بودید نفهمیدید: مرحله اول عملیات های تهاجمی موشکی و پهپادی هوافضای سپاه انجام شد.  پراکندگی مبدا شلیک ها و فراگیری بانک اهداف، جزو مهمترین ابداعات عملیاتی سپاه…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77581" target="_blank">📅 03:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77580">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/funhiphop/77580" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77579">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ممبرا می‌گن کرج رو ۶ بار بد زدن.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77579" target="_blank">📅 03:36 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
