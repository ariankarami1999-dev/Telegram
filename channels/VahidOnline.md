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
<img src="https://cdn1.telesco.pe/file/QojKhkAvxXv4Lp_AoHzoU2t7MAk9R2G_4v7T1d8mXuWgXjC6E3VGwpk6ezK7gNyuZGgOSiL5W5DiTf74Ou-ZItjI1kSCdWgvBEsuStsDXOhgSAz-EtU0jy6tRa5m2sfox-BbyLf-zx-tE7wqc_KfPKkTbb1vWrzbl7kcA-78m-E0M4bf5h4vf3AxGqP2EkcHCXUl9arn7GfxU9OXN3MDocNXNlbxRr2mdc4BltEGWkKsha1cFxX2n0l_haosxSjCAxWjMvboleMt_-PNXyA-xJHmudegBtgbTDOO4xEuvisQm1mi1o5r5RdAl7joBjx7o4uaoSYanTXY6xLGn5-HwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 18:16:54</div>
<hr>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SC_HKxC9by7A7fMDpn1w514SHGeJNzuG3umLVU0KTGEaG8LV6l42ZACiMR4J5nyZ-9UpCjXHs5ZmL1-Q0KsWEtSc_cw90KwF8_B9zbzwsgAmIwjbKw1HR2K4kkHbKCSTc3N52QMpuUzF9O14N8bowxJ8wAYL68Owr4Q1fpr_h83NSMt580r8UZCuExZO8J5CofLfVelep94iMTxiirnQWnk69wG4m44kYH_kftLXHmCbf7gCQlFjCCkSl_jCR5bspLAs0OuICFupP1Ap35wuaElHALlD8y23E78Uq8XrLQvX915phxadMIz3JlW23aMCJ9KAESO6Ay9KpOfOD3MX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
یکی از بدترین توافق‌هایی که کشور ما تاکنون انجام داده، توافق هسته‌ای ایران بود؛ توافقی که باراک حسین اوباما و افراد کاملاً ناشیِ دولت اوباما آن را مطرح کردند و به امضا رساندند. این توافق، مسیری مستقیم برای دستیابی ایران به سلاح هسته‌ای بود. اما درباره معامله‌ای که اکنون دولت ترامپ با ایران در حال مذاکره بر سر آن است، چنین نیست؛ در واقع کاملاً برعکس است!
مذاکرات به شکلی منظم و سازنده در حال پیشرفت است و من به نمایندگانم اطلاع داده‌ام که برای رسیدن به توافق عجله نکنند، زیرا زمان به سود ماست. محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت برقرار خواهد ماند. هر دو طرف باید وقت بگذارند و کار را درست انجام دهند. هیچ اشتباهی نباید رخ دهد!
رابطه ما با ایران در حال تبدیل شدن به رابطه‌ای بسیار حرفه‌ای‌تر و ثمربخش‌تر است. با این حال، آنها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای تولید یا تهیه کنند. مایلم تا این مرحله از همه کشورهای خاورمیانه بابت حمایت و همکاری‌شان تشکر کنم؛ حمایتی که با پیوستن آنها به کشورهای عضو توافق‌های تاریخی ابراهیم، بیش از پیش تقویت و گسترش خواهد یافت و چه کسی می‌داند، شاید جمهوری اسلامی ایران هم بخواهد به آن بپیوندد!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/VahidOnline/75683" target="_blank">📅 18:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-rynD_ZFvuCB5z_Qvh-Hv8DBs1sieGRSO884eyUkJ104HAuiKYDzXPUSobt-7VFanSL-R0i7WOQ_PnhpaJN7gAANsfboWIhu4IRCZCNJrufQ33TyYURfrKzeB-dQ-wWteTddn-J4GHSfnaL_1sCRyAdnZbwYpsw67fQx6GpaVfQ-yJWqzOCYi0pdnR9TVFqb1u_q2-Q3l6oBLB4zy3jAmJ0Ed1wYqvSNcmuD2NUXb9elqXzbaBFoapGHIsjrQQqwWFwh1ClqsWy2xoGuiEh4RYSYXkkF7HhGivgT_qJdY91WpQ-j0iemtzNj75b4amCoDz5O3oqhTlDhrI10h0Y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری ساخته با هوش مصنوعی را در شبکه اجتماعی تروث سوشال
منتشر کرد
که انهدام یک قایق سپاه پاسداران  به دست پهپاد آمریکایی را نشان می‌دهد.
بر این تصویر، واژه «حداحافظ» به زبان اسپانیایی نوشته شده است.
این تصویر در حالی توسط رئیس جمهوری آمریکا منتشر می‌شود که رسانه‌ها در انتظار نهایی شدن توافق احتمالی تهران و واشنگتن برای پایان جنگ هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/VahidOnline/75682" target="_blank">📅 18:15 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgIHtMVyaGQdRSPsfwz40Hy2aamEPgeMgtAFPZOq-9VV0A6kwIhwuJgQ7V-huCeMQgbGl9jrxlfoxzn_FNC173EflOofwuPSu5_FJNvB96aMaUZ06AyIfTZE7Lf96_ibBpGMBOZBOOWDM17UH6BD0dNzPnONkSVcfGhsBS6vpgEeETdZm6i4dFWDlp_oKTe7z_TGT7Ez7SLFAaPGYfAMPiuNr01SqkS2lD4GbgM6aXgGoNLJkPydQoR2MyePj5VEvPqYtDTHWrW2X0-ytT4rxNgUW_NJfgZMBow6i0WJ9Eb0epox5sc_SFcVIseoqiKr-AfBkZ68JRgLnCqoanXslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان گفت: «مدیران دولت تا زمانی که مباحث کارشناسی درباره مدیریت مصرف بنزین نهایی نشده است، حق اظهارنظر شخصی ندارند.»
او افزود: «اگر کسی از این دستور تخطی کند با او برخورد می‌شود، زیرا ابتدا باید نظرات کارشناسی بررسی و سپس جمع‌بندی نهایی حاصل شود.»
او ادامه داد: «مسئولان تا پیش از آن حق ندارند اظهارنظر شخصی کنند، چرا که نباید در جامعه التهاب یا نگرانی ایجاد شود.»
@
VahidOOnLine
این دستور در شرایطی صادر شده که شایعات درباره افزایش قیمت بنزین، تغییر سهمیه‌ها و تشدید سیاست‌های مدیریت مصرف بالا گرفته است.
همزمان، ناترازی بنزین و فاصله میان مصرف داخلی و توان تأمین سوخت، نگرانی‌ها درباره کمبود احتمالی یا فشار بیشتر بر شبکه توزیع را افزایش داده است.
عارف گفت دولت تلاش می‌کند تصمیم‌ها به‌گونه‌ای اتخاذ شود که معیشت مردم آسیب نبیند، اما واقعیات اقتصادی کشور و تحولات اخیر نیز باید در نظر گرفته شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/VahidOnline/75681" target="_blank">📅 18:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dOLxUFIaUWWk6w6Ii6X4vmw0q5pdnUuwWVYbZUP43BIlbue_mubWi5Xbb7ZEAMdtmtV4uMQBtleg7YFXwGzltHxsW8yY7mitXpZEnwmJwojbkyOdpmaDPQRJ1VZlsE1snlQH_D5xqQq6eRDpMq_JI3RFe3e2csG30mMbS7mWEI_VdqAZbsoe8gxHY07YtgzEyj6XMHKb1Yj_viwoPv6FlG4gTlVpVTnBham43PzK3Iy9m34S_HRVSYaXqIecSKzV3E49JLI69no6DtNCT5MYntfgPu4mWEV4HxVqzX2z-WvZtp4WOYkZ-EFSaslTI8gJW7zHEJJMsskp25Y_LHc7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dRVZGAiPqSkn6ibO76hM1byEuHNMRKW1EEkDLjQGDqmjKMjWwgwT8y4RaEgV9dv7aWNO1W4gKh_6zjyIhH7Amee9Gu1OmSkjdFEjVoyx8tfkfHWVQrdJzeudZKFUPelfa2umddplFzwuhuvQOe0cnFz-PcbJCFQmJKJrR7NhOMFd9eVN2QzyCkd7nQNyZD0Do21lmmE3lxZxs9Yq3WXUmlyeibsSG1SdgWyAiXOOQ9awzwJubX7pMprHVxXPJGldnvJ3ouLew9vloGGEvUqJ0hYHk6QJTP3vTYYMQfjf2cbstuM9rg0kLNWL4qwJwRDA6ciwXfREAwx5RmluPLvNeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران روز یکشنبه سوم خرداد با اشاره به توافق احتمالی میان جمهوری اسلامی و آمریکا، نوشت:  در پیش‌نویس توافق احتمالی ایران و آمریکا هیچ بندی درباره «تعهدات هسته‌ای ایران گنجانده نشده و تمام مسائل مرتبط با برنامه هسته‌ای به مذاکرات ۶۰ روزه پس‌از امضای توافق موکول شده است.»
فارس در ادامه تاکید کرده است که «ایران در این توافق هیچ تعهدی برای واگذاری ذخایر هسته‌ای، خروج تجهیزات، تعطیلی تأسیسات یا حتی تعهد به نساختن بمب هسته‌ای وجود ندارد.»
این در حالیست که نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت که شنیده‌ها از جزییات تفاهم اولیه «احتمالی»، حاکی است که واشینگتن متعهد خواهد شد در طول دوره مذاکرات، تحریم‌های نفتی ایران را به حالت اسقاط درآورد و جمهوری اسلامی در مقطع کنونی هیچ اقدامی را در حوزه هسته‌ای نپذیرفته است.
این گزارش افزود در صورتی که این تفاهم‌نامه مورد توافق قرار گیرد، بخشی از دارایی‌های بلوکه شده حکومت ایران باید در گام اول آزاد شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/VahidOnline/75679" target="_blank">📅 18:11 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BQCs6-SzeXEDPt0Qv7gGQG0kyTHmYtrmTOJn7p6a8UaCmYT7HPaq14GGAZn8RD4ULRNBUaa_rzubpXuiv6F9SW-nUe0-KSes6nxla-e5VIQWNlsn_6KF_VPBD5yjHQe6F3H66olD8tbuxzNER2O_NuI_BsN4UH4TJCw9jPOfD29Vydey4GYeB8cTeKVbyk-G_r3LBJOqi1uNH-dWDQBg0DqRKS5EHTCA2wTl_dcHH1OqS6nvKimERw7tHadSTrT2UYxd0Z_qFpd9-JY0J7pWi2wAM_cCjdyhlLHCdLnuMJRq1qO-a4_OmrFnnCnrZDr28OoNLX2rF6keH1f64pJw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=hFKPCP036o6ixXkhu6lQQw3lhJMDZsSqFCs8--_C0vDld3Ww-E8V49Y_U_ASZaDCs4wBbfjM2Pck7M_xllFl2lvwlaBFSAjGjlBjkKWmhTLAHxjW_tNgbKPScIqtHdyaonc7jtgPT48h-QRB9xNSKSLBiWtVGG_cYN3Q2WI6K8ydTUj4SJEjp_BDYZJf_-UlL_WQ8xeet3kM9VA4yn1mG9el9J9BgujqbTCKlS6n9_MPaeMfQsAz5TFzrsir22ZzM2RPruxmTXPZR2bUSly4PJOcun7U6Kd_2S8Bdh-LenBKEQxWOQWIAFh4SDWVirzA49IbhQ_wYws4cYh0gm__hw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/af3f5ad4b2.mp4?token=hFKPCP036o6ixXkhu6lQQw3lhJMDZsSqFCs8--_C0vDld3Ww-E8V49Y_U_ASZaDCs4wBbfjM2Pck7M_xllFl2lvwlaBFSAjGjlBjkKWmhTLAHxjW_tNgbKPScIqtHdyaonc7jtgPT48h-QRB9xNSKSLBiWtVGG_cYN3Q2WI6K8ydTUj4SJEjp_BDYZJf_-UlL_WQ8xeet3kM9VA4yn1mG9el9J9BgujqbTCKlS6n9_MPaeMfQsAz5TFzrsir22ZzM2RPruxmTXPZR2bUSly4PJOcun7U6Kd_2S8Bdh-LenBKEQxWOQWIAFh4SDWVirzA49IbhQ_wYws4cYh0gm__hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه در جریان نشست خبری مشترک با سابرامانیام جایشانکار، وزیر خارجه هند، در دهلی‌نو اعلام کرد که طی ۴۸ ساعت گذشته «پیشرفت قابل‌توجهی» در مذاکرات و رایزنی‌های مرتبط با بحران تنگه هرمز و پرونده ایران حاصل شده و احتمال دارد تا ساعاتی دیگر اخبار مهم‌تری در این زمینه منتشر شود.
او بدون ارائه جزئیات کامل، گفت هنوز توافق نهایی شکل نگرفته اما مسیر مذاکرات نسبت به روزهای گذشته امیدوارکننده‌تر شده است.
روبیو با تاکید بر اینکه دولت آمریکا همچنان راه‌حل دیپلماتیک را ترجیح می‌دهد، اظهار داشت دونالد ترامپ تمایل دارد بحران ایران از طریق وزارت خارجه و مذاکره حل شود، نه از مسیر درگیری نظامی.
با این حال او هشدار داد که واشنگتن در هر شرایطی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و این موضوع «خط قرمز» دولت آمریکاست.
به گفته او، رئیس‌جمهوری آمریکا بارها تاکید کرده که ایران هرگز نباید به توانایی ساخت سلاح هسته‌ای برسد و دولت ترامپ در این زمینه از همه دولت‌های پیشین آمریکا سخت‌گیرتر عمل کرده است.
وزیر خارجه آمریکا در بخش دیگری از سخنانش به وضعیت تنگه هرمز پرداخت و گفت این آبراه، یک مسیر بین‌المللی است و هیچ کشوری حق ندارد عبور و مرور آزاد کشتی‌های تجاری را تهدید کند. او اقدامات اخیر ایران در قبال کشتی‌های عبوری را مغایر قوانین بین‌المللی دانست و هشدار داد اگر جامعه جهانی در برابر چنین اقداماتی سکوت کند، یک «وضعیت خطرناک و غیرقابل‌قبول» به رویه‌ای عادی در جهان تبدیل خواهد شد، موضوعی که می‌تواند در مناطق دیگر دنیا نیز تکرار شود.
روبیو همچنین اعلام کرد آمریکا طی دو روز گذشته همراه با شرکای خود در منطقه خلیج فارس روی چارچوبی کار کرده که هدف آن باز نگه داشتن کامل تنگه هرمز، جلوگیری از اخذ عوارض یا محدودیت برای عبور کشتی‌ها و همچنین رسیدگی به نگرانی‌های مرتبط با برنامه هسته‌ای ایران است.
او توضیح داد که در صورت موفقیت این روند، نه‌تنها امنیت کشتیرانی و تجارت جهانی حفظ خواهد شد، بلکه نگرانی‌ها درباره برنامه هسته‌ای ایران نیز تا حد زیادی کاهش پیدا می‌کند.
روبیو در ادامه گفت هرگونه توافق احتمالی نیازمند پذیرش کامل ایران و اجرای عملی تعهدات خواهد بود و مذاکرات درباره جزئیات فنی برنامه هسته‌ای، روندی پیچیده و زمان‌بر دارد.
او افزود هنوز نمی‌توان درباره موفقیت نهایی مذاکرات با قطعیت صحبت کرد، اما «نشانه‌هایی از پیشرفت واقعی» دیده می‌شود و ممکن است جهان در ساعات آینده خبرهای مثبتی درباره تنگه هرمز و روند مذاکرات دریافت کند.
@
VahidOOnLine
روبیو گفت: «هدف نهایی این است که ایران هرگز نتواند به سلاح هسته‌ای دست یابد. ایران هرگز نباید مالک سلاح هسته‌ای شود.»
او تاکید کرد دونالد ترامپ، رئیس‌جمهوری آمریکا، در این زمینه موضعی «کاملا روشن» داشته و گفته است ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
وزیر خارجه آمریکا افزود: «قطعا تا زمانی که دونالد ترامپ رئیس‌جمهور است، این اتفاق نخواهد افتاد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/VahidOnline/75676" target="_blank">📅 18:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pw_qbBn-biCp7yzUz0FW5OlwKwEgiTPzNQY2TfAO4_kw2GBw6hrfNJzmSIt0ACBW8_AMtmRSfB6yN2zDbcxXHCjIj4zb4Dm5yvEzOfZDeTTi-vANKOPLlENJ2fpOorIYsLI258feK57_CS3o4YzZDiZbtEr3tGqh2AF0LTX9zY5lMH3jx503xaNi3Jxs2qQGtsMsrGlsk0l7nH728tTeLsKqu1gO8exgXhCwKa3JSKIEm9CI6CfaQdzOSu7KlPXLt-4YTo0K4btPfse2k7yQrOiI82WnBe2hU3B3fj2QayDRloVJjpbBaiZmaTPkhaeELCIIufQZ4rYCiVi6gCXtpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد سرافراز، رئیس پیشین سازمان صداوسیما و عضو کنونی شورای عالی فضای مجازی، می‌گوید بخشی از حاکمیت ایران با الهام از الگوی چین به‌دنبال محدود کردن اینترنت جهانی برای عموم مردم و ارائهٔ آن فقط به گروهی خاص و کنترل‌شده است.
او روز یک‌شنبه سوم خرداد در گفت‌وگو با روزنامه اینترنتی فراز گفت جمهوری اسلامی تجهیزات لازم برای «قطع دائمی اینترنت» را از چین خریداری و وارد کرده است.
محمد سرافراز توضیح داد که در چین اینترنت جهانی برای عموم مردم قطع است و فقط به‌صورت محدود در اختیار گروه‌هایی خاص قرار می‌گیرد. سرافراز با اشاره به الگویی که آن را «سامانه نیکان» در چین خواند، گفت هدف چنین سازوکاری این است که «روایت حکومت» بر کشور حاکم باشد.
او همچنین اپراتورهای عضو شورای عالی فضای مجازی را از عوامل پشت پردهٔ تصویب طرح موسوم به «اینترنت پرو» دانست و گفت ذی‌نفعان قطع اینترنت «یک روز فیلترشکن می‌فروشند و یک روز اینترنت پرو».
@
VahidHeadline
پس از ۲۰۴۰ ساعت قطعی اینترنت در ایران، نت‌بلاکس، نهاد مستقل و بین المللی پایش اینترنت، در حساب‌کاربری‌اش در شبکه اجتماعی ایکس نوشت که در حالی که دسترسی به اینترنت جهانی در طول مذاکرات صلح تا حد زیادی قطع است، کاربران منتخب در لیست سفید، تصویری مصنوعی از زندگی ایرانیان را به جهان خارج ارائه می‌دهند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/VahidOnline/75675" target="_blank">📅 17:51 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=CN7lbODM-lZJi4A65X8zV6lA7f6HI2FDnmD_2eCOYv5uB_QCDJNcyDkhM_ef61NGkN3O_x46r59iwEbpL91_-8LUMmWrgFgmqJHu7Z6NTpX_eb5SMZepI9xaAqpL_dE7jgULFJP63Ev9pwd0EjgdzaWtg143iPQax_gGgkWFE9V0mZ4VaB7ujMx28L6bfojFIkt7Q_Q30Urc5107bvlKYvmrDwkoc6AVyRnMDkBS_HCf-GZ2UNJxpPY5baVHnCkGzkJF1yDPobntE4Lkit2ClflesD2bG-_hE7IIDmwUmvP40BiHV9nmeSJc_odyBzTtDVkUvi15C6qF0D7oKTyVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9232e36d77.mp4?token=CN7lbODM-lZJi4A65X8zV6lA7f6HI2FDnmD_2eCOYv5uB_QCDJNcyDkhM_ef61NGkN3O_x46r59iwEbpL91_-8LUMmWrgFgmqJHu7Z6NTpX_eb5SMZepI9xaAqpL_dE7jgULFJP63Ev9pwd0EjgdzaWtg143iPQax_gGgkWFE9V0mZ4VaB7ujMx28L6bfojFIkt7Q_Q30Urc5107bvlKYvmrDwkoc6AVyRnMDkBS_HCf-GZ2UNJxpPY5baVHnCkGzkJF1yDPobntE4Lkit2ClflesD2bG-_hE7IIDmwUmvP40BiHV9nmeSJc_odyBzTtDVkUvi15C6qF0D7oKTyVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاری بزرگ در نزدیکی یک قطار که از گذرگاه چمن در شهر کویته در ایالت بلوچستان پاکستان عبور می‌کرد، تعداد زیادی کشته و ده‌ها نفر زخمی برجا گذاشت.
یک مقام ارشد پلیس بلوچستان و یکی از مسئولان این ایالت به محمد کاظم، خبرنگار بی‌بی‌سی اردو، گفت تاکنون کشته شدن ۲۰ نفر در این انفجار تأیید شده و دست‌کم ۷۰ نفر زخمی شده‌اند.
تصاویر منتشرشده پس از حادثه نشان می‌دهد که چندین خودرو در نزدیکی خط آهن آتش‌ گرفته‌اند و واگن‌های قطار نیز روی ریل واژگون شده‌اند.
گروه جدایی‌طلب «ارتش آزادیبخش بلوچ» مسئولیت این حمله را به عهده گرفته‌ است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/VahidOnline/75674" target="_blank">📅 17:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xh3DyxA0jIfmRqJecTu_XBywxgOVfqRg2AaUvNe5AapFmIC2_2WwVDNcRhDwxkpW4kIsb36hnKP2xRyU4F-5vXzkMoAXj_GUlN9omo7zWRRcHaO8h989eyv2b93dFLjzibft03_NVmlkZrlryWSDiXUMIA85JhEM1L0TVNNn9iCI0SZ8eAEO7630RwNN0tRWYP3BXpusE_ojyPK6Kdl9jThHXeF7t9o6_rhjCTU7VBVo4K3rPpo9m4Wmcljqaf4qCCHBDmnVrUdWlrCbw_6KnYxZbA_GKWDXuWzP3o_HoXEt1XNULAXQ3fCnlWKJZoC3K1AkSvFkdO6HH3ZW9yZ4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضائیه جمهوری اسلامی، اعلام کرد مجتبی کیان به اتهام ارسال اطلاعات مراکز تولید صنایع دفاعی به «دشمن آمریکایی ـ صهیونیستی» اعدام شده است.
قوه قضائیه مدعی شده کیان در جریان آنچه مقام‌های جمهوری اسلامی «جنگ رمضان» می‌نامند، اطلاعات و مختصات واحدهای مرتبط با تولید قطعات صنایع دفاعی را از طریق پیام به شبکه‌های وابسته به اسرائیل و آمریکا ارسال کرده بود.
میزان مدعی شده بررسی‌های فنی نشان داده سه روز پس از ارسال این اطلاعات، محل مورد اشاره هدف حمله قرار گرفته و به‌طور کامل تخریب شده است. قوه قضائیه گفته پرونده این متهم در دادگستری استان البرز رسیدگی شد و حکم او پس از تأیید دیوان عالی کشور اجرا شد.
بر اساس رأی دادگاه، مجتبی کیان به اعدام و مصادره کلیه اموال محکوم شده بود. میزان همچنین نوشت از زمان بازداشت تا اجرای حکم کمتر از ۵۰ روز زمان گذشته است؛ موضوعی که پرسش‌های جدی درباره سرعت رسیدگی، امکان دفاع مؤثر و فرصت اعتراض در پرونده‌ای با مجازات اعدام ایجاد می‌کند.
قوه قضائیه گفته دادگاه با حضور وکیل برگزار شده، اما روشن نیست این وکیل منتخب متهم بوده یا تسخیری، از چه زمانی به پرونده دسترسی داشته، آیا امکان ملاقات محرمانه و آماده‌سازی دفاع فراهم بوده و آیا متهم فرصت کافی برای اعتراض به ادله فنی، درخواست کارشناسی مستقل و پیگیری مؤثر در دیوان عالی کشور داشته است یا نه.
این پرونده در بستر موج گسترده‌تری از اعدام‌ها، احکام امنیتی، مصادره اموال و رسیدگی‌های شتاب‌زده پس از جنگ قرار می‌گیرد؛ روندی که منتقدان و سازمان‌های حقوق بشری آن را نشانه استفاده فزاینده جمهوری اسلامی از مجازات اعدام برای ایجاد بازدارندگی سیاسی و امنیتی می‌دانند.
@
VahidHeadline
خبرگزاری میزان هیچ اطلاعاتی درباره حرفه این فرد نداده و مشخص نیست که مجتبی کیان چگونه به «اطلاعات صنایع دفاعی» دسترسی داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/VahidOnline/75673" target="_blank">📅 17:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b3jInH-2zpgFhu9eMN26UiKU4PdKUvhmbxwP8te7QxKofjpTQ8y2s6gWhahHZ2uH1r84k7iMr4hVC35n7ZnvRa4KOvEjUbnSUVam5BoX5esPRuaF8WbWEueakhvcXwiUFcoqDuDwxDmudGBcnPRCovYfiTQLtSpXcbibyoaqlR_VcKqSqDW6iKlB02cGsWVaZgGxiAbayIA_wx36aPQ8cB6Riy3NPq9SeQAiGwF0WxIOekUCDQ2FaghSvmTNnG4SGOPHpBbuVGgFc7tSLWsr48T42c4Uil57WRrTYtVUkghDMFwJ5BWVAQlnbp7GQhuYxTrIUNHGSYYSkyezO2ljFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس: جزئیات توافقی که ترامپ در آستانه امضای آن با ایران است
ترجمه ماشین:
توافقی که آمریکا و ایران در آستانه امضای آن هستند، شامل تمدید ۶۰ روزه آتش‌بس است؛ دوره‌ای که طی آن تنگه هرمز دوباره باز خواهد شد، ایران می‌تواند نفت خود را آزادانه بفروشد و مذاکراتی برای محدود کردن برنامه هسته‌ای ایران برگزار خواهد شد؛ این را یک مقام آمریکایی گفته است.
🔻
چرا مهم است: این توافق از تشدید جنگ جلوگیری می‌کند و فشار بر عرضه جهانی نفت را کاهش می‌دهد. با این حال روشن نیست که آیا به یک توافق صلح پایدار منجر خواهد شد یا نه؛ توافقی که هم‌زمان خواسته‌های هسته‌ای رئیس‌جمهور ترامپ را نیز پوشش دهد.
▪️
وضعیت فعلی: هم ترامپ و هم میانجی‌ها گفته‌اند ممکن است این توافق روز یکشنبه اعلام شود، هرچند هنوز نهایی نشده و همچنان ممکن است از هم بپاشد.
▪️
این مقام آمریکایی طرح کلی مفصلی از پیش‌نویس فعلی ارائه کرده که بخش عمده آن را منابع دیگر نزدیک به مذاکرات نیز تأیید کرده‌اند.
🔻
چه چیزهایی در توافق آمده است؟
دو طرف یک یادداشت تفاهم امضا خواهند کرد که ۶۰ روز اعتبار دارد و با رضایت متقابل قابل تمدید است.
▪️
در این دوره ۶۰ روزه، تنگه هرمز بدون عوارض باز خواهد بود و ایران موافقت می‌کند مین‌هایی را که در این تنگه کار گذاشته پاکسازی کند تا کشتی‌ها آزادانه عبور کنند.
▪️
در مقابل، آمریکا محاصره بنادر ایران را لغو می‌کند و برخی معافیت‌های تحریمی صادر خواهد کرد تا ایران بتواند نفت خود را آزادانه بفروشد.
▪️
این مقام آمریکایی اذعان کرد که این موضوع به سود اقتصاد ایران خواهد بود اما گفت در عین حال کمک قابل توجهی برای بازار جهانی نفت خواهد بود.
🔻
این مقام آمریکایی گفت هرچه ایرانی‌ها سریع‌تر مین‌ها را پاکسازی کنند و اجازه دهند کشتیرانی از سر گرفته شود، محاصره هم سریع‌تر لغو خواهد شد.
▪️
اصل کلیدی ترامپ در این توافق «امتیازدهی در برابر عملکرد» است.
▪️
طبق گفته این مقام، ایران خواستار آزادسازی فوری منابع مالی مسدودشده و لغو دائمی تحریم‌ها بود، اما طرف آمریکایی گفت این موارد فقط پس از ارائه امتیازهای ملموس اجرا خواهد شد.
🔻
مسائل هسته‌ای هنوز باید مذاکره شوند
▪️
به گفته مقام آمریکایی، پیش‌نویس یادداشت تفاهم شامل تعهد ایران به این است که هرگز به دنبال سلاح هسته‌ای نرود و درباره تعلیق برنامه غنی‌سازی اورانیوم و خارج کردن ذخایر اورانیوم با غنای بالای خود مذاکره کند.
▪️
به گفته دو منبع مطلع، ایران از طریق میانجی‌ها تعهدات شفاهی درباره دامنه امتیازهایی که حاضر است در زمینه تعلیق غنی‌سازی و واگذاری مواد هسته‌ای بدهد، به آمریکا ارائه کرده است.
▪️
آمریکا موافقت خواهد کرد که در دوره ۶۰ روزه درباره لغو تحریم‌ها و آزادسازی منابع مالی ایران مذاکره کند؛ هرچند این اقدامات فقط در چارچوب توافق نهایی و پس از اجرای قابل راستی‌آزمایی آن عملی خواهند شد.
▪️
نیروهای آمریکایی که در ماه‌های اخیر در منطقه مستقر شده‌اند، در دوره ۶۰ روزه در منطقه باقی خواهند ماند و فقط در صورتی خارج می‌شوند که توافق نهایی حاصل شود.
🔻
نکته قابل توجه: پیش‌نویس یادداشت تفاهم همچنین تصریح می‌کند که جنگ میان اسرائیل و حزب‌الله در لبنان پایان خواهد یافت.
▪️
یک مقام اسرائیلی گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس تلفنی روز شنبه با ترامپ درباره این شرط ابراز نگرانی کرد. او همچنین درباره جنبه‌های دیگر توافق نیز نگرانی‌هایی مطرح کرد، اما به گفته یک مقام آمریکایی، دیدگاه خود را با احترام و لحنی محتاطانه بیان کرد.
▪️
مقام آمریکایی گفت این یک «آتش‌بس یک‌طرفه» نخواهد بود و اگر حزب‌الله برای مسلح شدن دوباره یا تحریک حملات تلاش کند، اسرائیل اجازه خواهد داشت برای جلوگیری از آن اقدام کند.
...
🔻
چه باید دید: به گفته مقام آمریکایی، کاخ سفید امیدوار است اختلافات نهایی در ساعات آینده حل‌وفصل شود و توافق روز یکشنبه اعلام شود.
▪️
این مقام گفت ممکن است توافق حتی کل ۶۰ روز هم دوام نیاورد، اگر آمریکا به این نتیجه برسد که ایران درباره مذاکرات هسته‌ای جدی نیست. از سوی دیگر، آمریکا معتقد است فشار اقتصادی بر ایران انگیزه‌ای برای رسیدن به توافق کامل به‌منظور رفع تحریم‌ها و آزادسازی منابع مالی این کشور ایجاد می‌کند.
▪️
این مقام آمریکایی گفت: «دیدنی خواهد بود که ایران واقعا تا کجا حاضر است پیش برود؛ اما اگر آن‌ها توانایی و تمایل تغییر مسیر خود را داشته باشند، این مرحله بعدی آن‌ها را وادار خواهد کرد تصمیم‌های حیاتی درباره این بگیرند که می‌خواهند چه نوع کشوری باشند.»
▪️
مشاوران ترامپ می‌گویند اگر خواسته‌های او درباره برنامه هسته‌ای ایران برآورده شود، رئیس‌جمهور آماده است برای بازتنظیم روابط با ایران و دادن فرصت به این کشور برای دنبال کردن ظرفیت کامل اقتصادی‌اش، که به نظر ترامپ «عظیم» است، اقدامات بسیار گسترده‌ای انجام دهد.
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75672" target="_blank">📅 07:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltWRvwNWMYWbvoSt6-az_2rm4ylfG07qlgRF3B7qnx99g3PLBcT8tztm8OuZx7knXJJsvSONoFoCwVFR3KbSFX0JXeKiCOCvzVp4hD5miPHZHP4UvIPkGyKhgDu_ZEKhBlemyFCR3KRYifKpMM6JH6dpyBGWb_wg0tv4w-5OyWRsFSfoOgVxkrmjTPbuL5GXJyjppvJmfIKbDqobIE_on6wP4ylftLVTx834kGMngSuvioAXQ-c_R1C7CVX15gBGqGd4XfnykEXOQZmlf_mFghlq7chL_Szs3lfOwyujg3JeXxAMc9uujKKRpDacEA0MpaiUqnABKPVe1A4lE3XxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1DYxRsZpZSngXo2QvmKif6DF6kAIHowBZR3mQKV6TqaaF1LmPWDJr_wO_7wwJCiIRQSJNuk3yq7iSe1vFHjx5E2DWZag2NtZfUlzYLeC-tWi5O0rXXCaVhWKYe0kxhtS-MRbZfKiUMipNNt2arV-U2gU8AaLrgvyfMg632I4lY6X2J104KJR1Alw3-oFXLkWShnowCQq5zn49XlGHKOe7KukcZ8FWxbk8AZ3fISPEpiEVD6tHtb3JiJotE33L90MRyTeuUG6XuHueCbpDWciXSHZejpgrm7hmp-7Jrj1Gl7MnRVSkhrv5hx-LDlcsfPRTiMuHqa4tYE01TGRuJMvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه، در پیامی در شبکه اجتماعی ایکس با درج تصویر سنگ‌نگاره پیروزی شاپور اول ساسانی بر امپراتور روم، نوشت: «وقتی ایرانیان مهاجمان متوهم را ناکام گذاشتند.»
او در این پیام که کنایه‌ای است به محاصره دریایی بنادر ایران توسط آمریکا نوشت: «رومیان تصور می‌کردند که رم مرکز عالم است؛ اما ایرانیان این توهم را در هم شکستند.»
پیام آقای بقایی که به نحو گسترده‌ای در کانال‌های تلگرامی رسانه‌های حکومتی ایران بازنشر شده است به نظر می‌رسد که با استفاده از سنگ‌نگاره پیروزی شاپور بر امپراتوران روم در نقش رستم استان فارس بازنقش شده است.
آقای بقایی که اخیرا با حکم محمدباقر قالیباف به عنوان سخنگوی هیئت مذاکره‌کننده ایران هم منصوب شده است با اشاره به لشگرکشی مارکوس یولیوس فیلیپوس معروف به فیلیپ عرب، امپراتور روم، علیه امپراتوری ساسانیان، نوشت که لشگرکشی او «منجر به پیروزی رومیان نشد بلکه به صلحی با شروط شاپور اول ختم شد؛ امپراتور ناچار شد با واقعیت کنار بیاید.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75670" target="_blank">📅 06:22 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pdOsVk93IEZ2RlS2pVWAbyoDYiWKutmDmXGc5e16aptkR_AUb0oc45pBqAXduJM8dSFuz96-JDx70FCv4Uz_65ihafP_Hzmrbuj1yzeiig6AZHalLCMIeCzCasG-YT4JTyT-E9hAoszRr1CmDTxGLjHQCi5qMsrVhQGfTqv8K11YLdJ-yRU48FngVJDEE9MJdcYHYAOLsO7gMPrkbmz5ug9DpFTlBf-mkqHM-TZ_0gsdx8yZYv_1Iq5e8Kdkjk5DrN43LmrUsxxLxulV-L5hUtb-9eJRIDAnN0qLSVxwZ_XT9GwtVi8MLWpNx-MgIatSUq3Rr3m8ZH18CwgGxrVsfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز به نقل از دو مقام آمریکایی گزارش داد، یکی از عناصر کلیدی توافق پیشنهادی میان واشنگتن و تهران، تعهد آشکار ایران به واگذاری ذخایر اورانیوم با غنی‌سازی بالای خود است؛
مقامات آمریکایی تصریح کردند که این پیشنهاد هنوز جزئیات دقیق نحوه واگذاری این ذخایر را تعیین نکرده و حل این مسئله را به دور بعدی گفتگوها درباره برنامه هسته‌ای ایران موکول کرده است، اما یک بیانیه کلی که ایران را متعهد به این کار کند، که هدف دیرینه ایالات متحده بوده، برای توافق بسیار حیاتی است، به‌ویژه اگر این توافق کلی با بدبینی جمهوری‌خواهان در کنگره مواجه شود. تا این لحظه، ایران هیچ بیانیه‌ عمومی درباره توافقی که ترامپ اعلام کرده، صادر نکرده است.
تهران در ابتدا با گنجاندن هرگونه توافقی درباره ذخایر اورانیوم غنی‌شده خود در این مرحله اولیه مخالفت کرده و خواستار موکول شدن آن به مرحله دوم گفتگوها بود، اما مذاکره‌کنندگان آمریکایی از طریق واسطه‌ها به صراحت اعلام کردند که بدون دستیابی به توافقی بر سر این ذخایر در فاز اولیه، میز مذاکره را ترک کرده و کارزار نظامی خود را از سر خواهند گرفت.
براساس این گزارش، بخش دیگری از این توافق محتمل شامل آزادسازی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران در خارج از کشور است؛ اما به گفته مقامات آمریکایی، ایران تنها زمانی به بخش عمده این دارایی‌ها که قرار است توسط ایالات متحده و متحدانش در یک صندوق بازسازی قرار گیرد دسترسی پیدا خواهد کرد که با یک توافق هسته‌ای نهایی موافقت کند؛ امری که انگیزه‌ای برای تهران ایجاد می‌کند تا پای میز مذاکره بماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75669" target="_blank">📅 05:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cgz-Nr4KMYa2KtFzgA1xJnsOT0GhKgmCb336K2uwmStLUSsVgXZHQ5K9rbVJeYLcic17AgkH1er_T5ADVB1Wfp923KwlvwxLPZf_UqOnvLU4QjSgWvvEghX60w_LSzu03KxX-Gybqdy9XaFHVOaRyCxSKk-gz1yIIzNvNUTeVBSeAvSPXaDNvu4FFJ--iZ7WBHvyLMpZu-0rmKFfDn3hY5IcvoMzti4vWS1TlvksevfEwBJ1IhI-NF6SKC9KwryoP22Adb4sLVw7EWRpmnKOQ47hlKH02fJwSe1H43gvzm18MP9pACg86EgJgb6bcATG07nrbOOrg0a7CsVotGvWUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف، نخست‌وزیر پاکستان، ابراز امیدواری کرد پاکستان به‌زودی میزبان دور بعدی گفت‌وگوهای تهران و واشینگتن باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/75668" target="_blank">📅 05:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DiuzKj4qPVSv1TVqdJ-WhvgFtmZyMo0j6tgp2RQs4lWXynVv_sUl-5xg8DWd8ZfT9fL-I0JPhrchfS3sEAEW7JQ68HIFpfL3MN7wt4uWAg9vzY7IgRhkWSUXvZR3ehGgMes0vXGeXTXJMkPPEhC4fZeW5XFk3asCrUG15T7p2FtyKY3_srwyosUvO4ENKZ_BxdQAYI86OQnLmBBRd7DbHO1Z6qnlFnVCLhLjeERiZjb3OnE5sN4dOO4-z8VI1xHJHAbahkMxxC2wHKYtUSkdx-U0EqP3krOPmiTASTHRkWrNv1ouUGJgNlYNur6KkvG5-kK_TqSDbQUcJZdCu9k2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lf2GBrGEwOir5L4oQu_3nv5yGW0OSmePmQiLkW6o3O4CsrHQqUKytsE3O8Ydxfh2O4IkzGnF2E_Q5AYBcpow1kvYhLyLFQ3bDHvV_K2xIRyJ8pQeK7bfjH2-EC0JC1c17LK_zxQSB_Jp_aVWEJUPh7BR2ZjJZhz8T76rGxjpLdvVWZNjshQyQanTuoHYXTQkguvKgx8HbMbvqTrGKaKWpegA9C1jh6fL1Ms52xEap9FulYdMhNTCSS4Yp0xzb5k5e2D8aHO0Kb1s19aGSwgZgUQ0VNiM6lh0QC_SJXPGcjIDgPHxsAOPXrIVv9Y65N57DYZNDjkwNlHuWJdqbRlaaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت‌های تد کروز و لیندسی گراهام در واکنش به اخبار منتشر شده درباره توافق احتمالی
tedcruz
,
LindseyGrahamSC
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75666" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7119557db8.mp4?token=H01QkQ_raA8wc6xWKsD0FdoB_01A-aVEh95cYlUA17EV0LDFThZx1_BY8X-vseCB8G-ktjAVkWYckp1WcE6qdxjpdUhuKWfiEHm2Gr8Llq4yR3LzBUOI4olamYzDEhKLtZTpSsE0ZpTU5WIhXLu6Y1Yi2So5ZhK0_xVNF4vbppi2klK2dpDVL4MrNHRN32wb3088RXN6bD3K2pgL_wQ0eE6BhUKhPXUW4EsgI_JHlMNP4RIgnkwFSg3hxPqr_sBqwyb2tT-DtgsDDDdYwDEh1WbpwNUprDBAz4mrtaRP-lHNJIAc_u94gZBSWkwLSWigEZnHiBTQF16PQmAHnsuDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7119557db8.mp4?token=H01QkQ_raA8wc6xWKsD0FdoB_01A-aVEh95cYlUA17EV0LDFThZx1_BY8X-vseCB8G-ktjAVkWYckp1WcE6qdxjpdUhuKWfiEHm2Gr8Llq4yR3LzBUOI4olamYzDEhKLtZTpSsE0ZpTU5WIhXLu6Y1Yi2So5ZhK0_xVNF4vbppi2klK2dpDVL4MrNHRN32wb3088RXN6bD3K2pgL_wQ0eE6BhUKhPXUW4EsgI_JHlMNP4RIgnkwFSg3hxPqr_sBqwyb2tT-DtgsDDDdYwDEh1WbpwNUprDBAz4mrtaRP-lHNJIAc_u94gZBSWkwLSWigEZnHiBTQF16PQmAHnsuDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنبه عصر، یک تیراندازی در حوالی کاخ سفید خبر روی داد که طی آن دو نفر از جمله یک عابر و فرد مظنون تیر خوردند.
سرویس مخفی ایالات متحده، در گزارشی اعلام کرد که اندکی پس از ساعت ۶ عصر روز شنبه، فردی در محدوده خیابان ۱۷ و خیابان پنسیلوانیا، (شمال غربی) سلاحی را از کیف خود خارج کرد و شروع به تیراندازی کرد.
سرویس مخفی ایالات متحده افزود پلیس سرویس مخفی به تیرانازی او پاسخ داد و به مظنون شلیک کرد.
به گفته سرویس مخفی،‌مظنون به یک بیمارستان محلی منتقل شد، اما در آنجا اعلام شد که جان باخته است.
به گفته این نهاد امنیی، در جریان این تیراندازی، یک عابر نیز مورد اصابت گلوله قرار گرفت و هیچ‌یک از مأموران آسیب ندیدند.
سرویس مخفی که وظیفه حفاظت از رئیس‌جمهوری آمریکا را دارد افزود دونالد ترامپ، رئیس‌جمهوری آمریکا، در زمان حادثه در کاخ سفید حضور داشت.
@
VahidHeadline
آپدیت:
رسانه‌های آمریکایی هویت عامل تیراندازی عصر شنبه در مجاورت کاخ سفید را «نصیر بست»، جوان ۲۱ ساله اهل مریلند، معرفی کردند که به عنوان فردی با اختلالات روانی و عاطفی شدید برای ماموران امنیتی شناخته‌شده بوده است.
بر اساس گزارش‌ها، این فرد که پیش از این در ژوئن ۲۰۲۵ با ادعای این‌که «خدا» است یک مسیر ورودی کاخ سفید را مسدود کرده و پس از آن به یک مرکز روان‌پزشکی منتقل شده بود، به دلیل تلاش مجدد برای ورود به حریم کاخ سفید در ژوئیه همان سال، حکم دادگاه مبنی بر «ممنوعیت ورود و نزدیکی به این عمارت» را داشته است.
گزارش‌های تکمیلی نشان می‌دهد که «نصیر بست» دست‌کم در یک پست رسانه‌های اجتماعی تمایل خود را برای آسیب رساندن به دونالد ترامپ ابراز کرده بود؛ او سرانجام پس از نقض حکم دادگاه، نزدیک شدن به ایست بازرسی خیابان هفدهم و پنسیلوانیا و گشودن آتش به سمت ماموران، در تبادل آتش متقابل با نیروهای سرویس مخفی هدف قرار گرفت و در بیمارستان جان باخت.
📷
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75665" target="_blank">📅 04:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q02VmD6ZWlVaQhAWv9493_uWUBfOTeydgqo7gW-oyim7CDwOgdQBkTdXGwbln7PFjBBt63nMeIWBuB2KDwdk9laIunoUEx2qTA8JjMi8ULoPgHjbFE3tJgG3NQxETknGgpggWG9VKooDv1gSKAFFBo42OWEECghOq6Cy-cllpFc_PzE917_6MIVbzLxwX6Zyn-EHFpJDXuL611Zjsp2P8Wuh40OqHA1UvuWfEsuoDu4EcvgyXDB9xelzofpgGeWSxdcBE5p_GASFF6XeaHJQuHRDuZAc_gDWSg7E4br_JpWscREdyozvs56h0MxvjHC0pfcmnQsfQeUAvOwh17xxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس، خبرگزاری وابسته به سپاه، در واکنش به پیام دونالد ترامپ، رئیس‌جمهوری آمریکا مبنی بر نزدیک شدن به توافق با ایران و بازگشایی تنگه هرمز نوشت: «این ادعا نیز با واقعیت‌ها فاصله دارد».
فارس در ادامه نوشت: «برخلاف ادعای لحظات قبل دونالد ترامپ در شبکه اجتماعی تروث سوشال مبنی بر بازگشت تنگه هرمز به وضعیت پیشین و آماده‌سازی برای امضای توافق‌نامه، پیگیری‌های خبرنگار فارس نشان می‌دهد که این ادعا نیز با واقعیت‌ها فاصله دارد؛ چرا که بر اساس آخرین متن ردوبدل‌شده، در صورت توافق احتمالی، تنگه هرمز کماکان تحت مدیریت ایران خواهد بود و اگرچه ایران موافقت کرده اجازه دهد تعداد کشتی‌های عبوری به میزان قبل از جنگ بازگردد، اما این به‌هیچ‌عنوان به معنای تردد آزاد به وضعیت قبل از جنگ نیست و مدیریت تنگه، تعیین مسیر، زمان، نحوه عبور و صدور مجوز، کماکان در انحصار و با تدبیر جمهوری اسلامی ایران خواهد بود.»
خبرگزاری سپاه در ادامه مدعی شد که برخلاف شروط پیشین ترامپ مبنی بر گنجاندن برنامه هسته‌ای در توافق، «هیچ تعهدی از سوی ایران داده نشده و پرونده هسته‌ای اساسا در این مرحله مورد بحث قرار نگرفته است.»
فارس همچنین ادعا کرد که «مقامات آمریکایی در پیغام‌های متعدد به ایران اذعان داشته‌اند که توییت‌های ترامپ عمدتا جنبه تبلیغاتی و مصرف رسانه‌ای در داخل آمریکا دارد و توصیه کرده‌اند که به این اظهارات توجهی نشود».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/75664" target="_blank">📅 01:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twpmWhQNneJcTP14J-QmVHRBJPd0YQdNV0dX3iC_YkLgiQVZkYZf01fucl8gX2I9EHR9McuepOfaeY8yBXhB9mcA7DC3drV__Mh5Jqf9flesn1t8dy8JbV0miVyhJCwPRPE7PclN3GVh6NxHHB7qhi5ODkXvBZJiLWGSjVuR_CeYJFuCDxZ6c6sWjHlMxN9aMNKFCfYUSz34T-Q-Kx7wCcYzIj6suLcl2a2FetUTLJa1zycjZY4aRlybVekVc4KpgLjnH7BLADIOEEonRFZ2OKidb7RGSY4oXrMGUS7W2s-QnqszYqmhSpJzccFs71TYnkw5iN-vLkLrw6Qxjx1vCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار الجزیره به نقل از «منابع خود»، مفاد کلیدی پیش‌نویس توافقی را که قرار است میان واشنگتن و تهران نهایی شود را اعلام کرد.
خبرنگار الجزیره مدعی شد، توافق پیشنهادی شامل «پایان جنگ در تمامی جبهه‌ها از جمله لبنان»، «آزادسازی چندین میلیارد دلار از دارایی‌های مسدودشده ایران»، «رفع محاصره دریایی آمریکا و بازگشایی تنگه هرمز» و همچنین «عقب‌نشینی نیروهای آمریکایی از مجاورت مرزهای ایران» است.
پس از اجرای این گام‌ها، طرفین یک مهلت ۳۰ روزه، که با توافق دوطرفه قابل تمدید است، خواهند داشت تا درباره مسئله هسته‌ای به توافق برسند که در طول این مدت نیز تردد از تنگه هرمز تسهیل خواهد شد.
به گفته این خبرنگار، از نظر ایران، مدیریت تنگه هرمز یک موضوع دوجانبه میان تهران و مسقط تلقی می‌شود و گفتگوها در این زمینه با عمان در جریان است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75663" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFwrnWn0-dHCSgoktSeMAUyub92ujDYUYO1S48PdLWowd5bnsfK60pwObDB3yZXuI9D6xFCtgbs9ys3eyP9_rJsyKUFvwtUvd51aps2BT5STsSlmBFuz4aadAyGgmrRgEPblOHrKRpHKfyHzbQrt6ChfvIIcd7vYLKBttEALIfuK-rEUvcD02Mt-mTgM2Xo-OH-QNJiwpDdLbEw1J338OpigVsqwvTauSIdpqBlcDIZTNBfuJgZbMdgVLvDK7459Lho6Vs0ojvJwxi_jdN5nVGmQcgnze8c6V3Nf8pWbb8wZg5M-oalw8UztKjorH3dnwibdAxB92tKv7UyRSa3wYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«یک منبع ارشد منطقه‌ای» از جزییات گفتگوی رهبران کشورهای عربی و مسلمان با دونالد ترامپ خبر داد.
خبرنگار آکسیوس نوشت: «یک منبع ارشد منطقه‌ای به من گفت که تمامی رهبران عرب و مسلمان حاضر در گفتگوی روز شنبه با ترامپ، از او خواسته‌اند تا برای پایان دادن به جنگ و مهار تنش‌ها در منطقه، توافق را پیش ببرد.»
این منبع تاکید کرده است که «پیام همه این بود: لطفا به خاطر کل منطقه، جنگ را متوقف کنید.»
به گفته این منبع، مذاکرات به خوبی در حال پیشرفت است و میانجی‌ها امیدوارند روز یکشنبه یک توافق چارچوب یک‌صفحه‌ای را منعقد و بلافاصله آن را اعلام کنند و پس از آن، قصد دارند ظرف چند روز مذاکرات را برای دستیابی به یک توافق دقیق و پرجزئیات آغاز کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75662" target="_blank">📅 00:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCQYzOuLM7dkztg1hmeABttCbWDFDTJ3FiMau-xnS5VaLGC15nOTrkyqPANZ1GJGspk2MVXQnd-rxQ-hjVrsAWI-k7pMufCB11jtgRYFqFU5WA5wynFHLQMkDBAEytB6NxADtJp9znAgS_6fcRo5SQVuh20EWLnXMCRJqPatPhx2jQZcjpLBrONw3Ok5JJsSp75TRR-KeiGfL47jca7AhT-Blj0FmgSrdJFgGVmF30mAt1mV_tMooYk-kVvpvITj_SFdQ3Q2OJ404I-0pSK3x0P23iDyteHfIkOYFfjkTEhXCdSCOMammyJM0dtzxI5nVuCFZFTnyh8Xf9DGfWiFXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: یک توافق تنظیم شده و اکنون در انتظار نهایی شدن است
پست ترامپ، ترجمه ماشین:
من در دفتر بیضیِ کاخ سفید هستم؛ جایی که همین حالا تماس بسیار خوبی با
▪️
پرزیدنت محمد بن سلمان آل سعود از عربستان سعودی،
▪️
محمد بن زاید آل نهیان از امارات متحده عربی،
▪️
امیر تمیم بن حمد بن خلیفه آل ثانی،
نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جبر آل ثانی و وزیر علی الثوادی از قطر،
▪️
فیلد مارشال سید عاصم منیر احمد شاه از پاکستان،
▪️
رجب طیب اردوغان رئیس‌جمهور ترکیه،
▪️
عبدالفتاح السیسی رئیس‌جمهور مصر،
▪️
عبدالله دوم پادشاه اردن،
▪️
و حمد بن عیسی آل خلیفه پادشاه بحرین،
درباره جمهوری اسلامی ایران و همه مسائل مربوط به یادداشت تفاهمی در ارتباط با صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده و نهایی شدن آن منوط به جمع‌بندی میان ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگری است که نامشان ذکر شد.
▪️
جداگانه، با نخست‌وزیر بی‌بی نتانیاهو از اسرائیل نیز تماسی داشتم که آن هم بسیار خوب پیش رفت.
جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بررسی است و به‌زودی اعلام خواهد شد. علاوه بر بسیاری دیگر از عناصر این توافق، تنگه هرمز باز خواهد شد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75660" target="_blank">📅 00:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KYsgrZ-fZAmJHrm5La_Pi5JK54B9WD6lpgJI4MjYAVW9x2EldPROqiUbbK-_ovEyvgqXradvzCF1vDuRNyagHWKhJtpY7OyrDywHHmlTysrBsfngR-04StIL3E6wjuy8Bj5Fhi5f7Ea7PgzBBi2HJnJn_kYPCxJMZ6Uk0s1Nqw5PaAK-6IIVRo7t98vXu6fHQddzy3FO-QNOwg_41sxnCUpDVAcjKTRbR7wHX8m5uNR_u7jLwpUrvnenl2sjJDCedWbi8NiBHmcp2_62vJN4kXSozUhMrGxKJKrqIWqv5MggeUcE1rvNaIwGHi-73ucRgAaRlzTHFQ3OQGs7GcLI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز شنبه دوم خرداد ۱۴۰۵ در تماس‌هایی جداگانه با رهبران عربستان سعودی، امارات، قطر، مصر، ترکیه، پاکستان و فرانسه درباره توافق احتمالی برای پایان جنگ با جمهوری اسلامی گفت‌وگو کرد. همزمان یک مقام آمریکایی آگاه از روند مذاکرات گفت واشنگتن و تهران به دستیابی به توافق نزدیک شده‌اند و اختلاف‌های باقی‌مانده عمدتا بر سر نحوه نگارش برخی بندهای توافق است.
به گزارش اکسیوس، چند تن از رهبران حاضر در تماس با ترامپ از او خواسته‌اند مسیر دستیابی به توافق را دنبال کند. با این حال، این مقام آمریکایی تاکید کرده است که هنوز تصمیم نهایی از سوی رییس‌جمهوری آمریکا اتخاذ نشده و او همچنان می‌تواند توافق را رد کرده و دستور حملات جدید علیه ایران را صادر کند.
همزمان، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و پیت هگست، وزیر دفاع این کشور، برای شرکت در نشست ویژه بررسی توافق احتمالی به واشینگتن فراخوانده شدند. ترامپ پیش‌تر گفته بود پس از بررسی آخرین پیشنهاد ایران با تیم مذاکره‌کننده خود، احتمالا تا روز یکشنبه درباره ادامه مذاکرات یا ازسرگیری جنگ تصمیم خواهد گرفت.
به گفته منابع آگاه، پیش‌نویس جدیدی که قرار است ترامپ آن را بررسی کند، حاصل مذاکرات اخیر میان ایران و پاکستان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75659" target="_blank">📅 23:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOl2XjDTv6dYBldMxj7ETajcN8PRlGQclLBUitNwVHkouQhF3sLCLdMRQu0Suo1_knDdmzg2wGtqozBp4TRLxXfTS6ubbcNdDKbxaQPYTQ1Ll5WGrjBGa_qv4kiSHbZ6otzE4IUI7uNCsLKfwkKBO6R4paYmkfWCSb28C5-1mAGsPOjLryZ4tAoz_rnUgO_Z8hc0czSmc96wseIp535FwqRO3zvwZqVypVrtJVVoZ1BcjrKB3kcwOE_ExLPE9_c3NJebjt_IQx74_azhdMXxD_nYSUur67MJ18DdAx-3Q59yZa8-Ino51Km1ckJEmKlBjWuX6MieK3v7KdZAzzxHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ۱۳ اسرائیل در گزارشی از روند گفت‌وگوهای ایران و آمریکا گفت مقام‌های اسرائیلی معتقدند ایالات متحده و ایران به دستیابی به توافق احتمالی نزدیک‌تر شده‌اند و گزارش‌های اخیر و اطلاعاتی که دریافت می‌شود، «در اورشلیم به‌طور فزاینده‌ای معتبر تلقی می‌شود».
بر اساس گزارش این شبکه، مقام‌های ارشد اسرائیلی گفته‌اند پیشرفت در مذاکرات برای بخشی از نهاد امنیتی اسرائیل «بسیار ناامیدکننده» است، به‌ویژه در شرایطی که به نظر می‌رسد تلاش واشینگتن برای رسیدن به توافق در حال تشدید شدن است.
این مقام‌ها همچنین معتقدند فشار برخی مشاوران رئیس‌جمهور ترامپ در روزهای اخیر افزایش یافته و انتظار می‌رود بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در پی این تحولات، نشست‌هایی مشورتی با وزیران ارشد و مقام‌های امنیتی برگزار کند.
نهادها و مقامات رسمی اسرائیل هنوز این گزارش را رد یا تأیید نکرده‌اند.
ارزیابی اسرائیل در دو هفتهٔ گذشته این بود که ترامپ خواهان توافق است، اما در نهایت به دلیل اختلاف بر سر مسائل کلیدی، موفق به دستیابی به آن نخواهد شد. با این حال، مقام‌های اسرائیلی اکنون معتقدند روند کنونی ظاهراً برخلاف چیزی است که اسرائیل در هفته‌های اخیر برای آن تلاش کرده بود.
این گزارش همچنین می‌گوید چارچوبی که دربارهٔ آن گفت‌وگو می‌شود، شامل یک توافق موقت ۶۰ روزه خواهد بود که ممکن است بعداً در حالی که مذاکرات درباره توافقی گسترده‌تر ادامه دارد، تمدید شود.
روز شنبه مقامات ایران و آمریکا و همچنین پاکستان که نقش میانجی را بین دو طرف بر عهده دارد، اعلام کردند که در مذاکرات برای پایان دادن به جنگ پیشرفت حاصل شده است.
روز شنبه، روزنامه اسرائیل هیوم نیز در گزارشی ادعا کرد پیش‌نویس توافقی که روی میز قرار دارد، شامل تعهد اولیه ایران به خودداری از توسعه سلاح هسته‌ای و تعلیق بلندمدت غنی‌سازی اورانیوم است و سایر مسائل، از جمله سرنوشت ذخایر کنونی اورانیوم غنی‌شده ایران، در مذاکرات بعدی در دورهٔ آتش‌بس بررسی خواهد شد.
این روزنامه همچنین به‌نقل از منابع آگاه که نام‌شان را نیاورده، ادعا کرد «رهبری سیاسی ایران پیش‌تر با تحویل اورانیوم غنی‌شده موافقت کرده بود، اما فرماندهان سپاه پاسداران با این اقدام مخالفت کردند و تصمیم‌گیری دربارهٔ این موضوع اکنون به تأیید رهبر جمهوری اسلامی بستگی دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75658" target="_blank">📅 21:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IGqjz8RKWounAZMYKlKK93Gj_jP31597EzqhNDbPWc2BSQngrXQliyCbfO_UKqR5yAQiVfvpohfZCrPV0APFQL71w0V3QY8pJHaZ3CiV7JjdDw1CzMSgZ-P7BxvnbWOv-ZWt34e0lnIJvqTtmH7W3QJiKQK0Xete3SIbq7JBPC-sx5gig50UjNzNgRaWYUmkkwa_THnVO9Mvih04mVzStxgr_OWcv27CKwNTbZoCtcCqbo8FVcEgKQ45nvdUHmDGSxvAaO-jNMFeJKwLleHMboUp4ayn3hMgGStGgzp7I3FLDaMxiIz1qoixf_ox9tx7lSFmBc_jyXgp-iM1rfI5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه و نزدیک به تیم مذاکره‌کننده، با تاکید بر اینکه اگر آمریکا انعطاف نشان ندهد، مذاکره شکست می‌خورد نوشت که موضوع هسته‌ای، پول‌های بلوکه‌شده و کنترل جمهوری اسلامی بر تنگه هرمز، سه موضوع اختلاف جدی در مذاکرات است.
فارس نوشت که تهران اعلام کرده که در این دوره وارد مذاکره درباره موضوع هسته‌ای نمی‌شود. تنها در صورتی که طرف مقابل شرایط اعتمادساز را اجرا کند، در دور بعد درباره مسائل هسته‌ای صحبت خواهد شد.
رسانه سپاه به نقل از این منبع نوشت: «پول‌‌های بلوکه‌شده باید واریز شود؛ شرط دوم و اساسی برای ورود تهران به مذاکره این است که پول‌های بلوکه‌شده ابتدا واریز و آزاد شوند. بدون این اتفاق، اساسا وارد مذاکره نمی‌شویم.»
در ادامه آمده است: «اختلاف دیگر بر سر نحوه عبور کشتی‌ها در تنگه هرمز است. آمریکا تاکید دارد که تنگه باید کاملا به شرایط پیشین بازگردد، اما تهران می‌گوید فقط خود را متعهد می‌کند که تعداد کشتی‌ها به وضعیت قبل بازگردد. معنای این حرف آن است که حکومت ایران با مدل خود، تعداد کشتی‌های مجاز برای عبور را تعیین می‌کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/75657" target="_blank">📅 19:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kDrnWO5WXSGxMJ4J-oXMyXdt5XGrAMNNFCVge7bYU6xwYaTv2fTbdqt2EgeD79qFM5mh_T3_ZHwudqDwpb5IB51BAeFg_37BYhHjGRrtBP7taLfUiVtbOVxAYFKO3-mwx0c2T63pgXd9ltGMndaQNevLfdl2O_ckSP7mBnMMzO2H2EazAiP_etcKtIYl2fzVhY0eY1waQYfhHZ5rPwPOlJvW60Xoztj5J11ovdIZs1ABbrt8d1ANxSrvTDxvLJezNlddm65JzQffMVre7CWNlz6V3onUEbUeDFxRRbTQue_C0HuyB24OgbMnKpsRerVjsamiToBiyew3OHQ_3krtSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: به توافق بسیار نزدیک‌تر شده‌ایم
ترجمه ماشین:
پرزیدنت ترامپ به شبکه سی‌بی‌اس نیوز گفت مذاکره‌کنندگان ایالات متحده و ایران برای نهایی کردن توافقی که به جنگ میان دو کشور پایان دهد، «بسیار به هم نزدیک‌تر شده‌اند».
منابع آگاه از مذاکرات به سی‌بی‌اس نیوز گفتند تازه‌ترین پیشنهاد شامل روندی برای بازگشایی تنگه هرمز، آزادسازی بخشی از دارایی‌های ایران که در بانک‌های خارجی نگهداری می‌شود، و ادامه مذاکرات است.
آقای ترامپ از ارائه جزئیات درباره این توافق خودداری کرد، اما گفت که «هر روز بهتر و بهتر می‌شود.»
آقای ترامپ در یک مصاحبه تلفنی به سی‌بی‌اس نیوز گفت: «نمی‌توانم قبل از اینکه به خودشان بگویم، به شما بگویم، درست است؟»
👈
آقای ترامپ گفت معتقد است توافق نهایی مانع دستیابی ایران به سلاح هسته‌ای خواهد شد و افزود که در غیر این صورت «اصلاً درباره آن صحبت هم نمی‌کرد».
👈
او همچنین گفت این توافق باعث خواهد شد اورانیوم غنی‌شده ایران «به شکل رضایت‌بخشی مدیریت شود.»
👈
او گفت: «من فقط توافقی را امضا می‌کنم که در آن به هر چیزی که می‌خواهیم برسیم.»
منابع به سی‌بی‌اس نیوز گفتند آقای ترامپ هنوز در حال بررسی پیشنهادهاست و هنوز تصمیم نهایی خود را نگرفته است. این منابع گفتند او با مشاوران خود رایزنی می‌کند و با رهبران خارجی، از جمله رهبران عربستان سعودی و دیگر کشورهای حوزه خلیج فارس، گفت‌وگو دارد.
آقای ترامپ گفت اگر آمریکا و ایران به توافق نرسند، «با وضعیتی روبه‌رو خواهیم شد که هیچ کشوری هرگز به اندازه ضربه‌ای که آن‌ها در آستانه دریافتش هستند، ضربه نخورده باشد.»
آقای ترامپ پیش‌تر ایران را تهدید کرده بود؛ او پیش از آغاز آتش‌بسی که در ماه آوریل آغاز شد، گفته بود بدون توافق «یک تمدن کامل نابود خواهد شد» و اخیراً نیز به این کشور هشدار داده بود که «ساعت در حال تیک‌تاک است.»
مارکو روبیو، وزیر خارجه آمریکا، نیز روز شنبه گفت ممکن است «بعداً امروز خبری» درباره وضعیت مذاکرات میان ایران و آمریکا منتشر شود.
روبیو پیش از یک شام رسمی در سفارت آمریکا در دهلی‌نو، هند، گفت: «پیشرفت‌هایی حاصل شده، همین حالا هم که با شما صحبت می‌کنم، کارهایی در حال انجام است. این احتمال وجود دارد که چه بعداً امروز، چه فردا، چه ظرف چند روز آینده، چیزی برای گفتن داشته باشیم؛ اما همان‌طور که رئیس‌جمهور گفت، این موضوع باید به یک شکل یا شکل دیگر حل شود.»
CBSNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/75656" target="_blank">📅 19:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cs_JOYsND-XFbsHf0jzhrl56DkiQ8BfdWUjuE8lDY4CEvyDWrRpCV1KcR46KYdqFGQHlYUUxh5d75z_vJhHVZz1-TEIoB8h2BRRxoV3U_pOLkZVYBZnCLv7oPe_FbJIYtu7PQybqT3XUy7uwe3HwCRVCWtbw3-gDztPBUtzIPgDLvIQ6510D-OYG-q4eJ7gyTzlKoqK5TGxet1k3bc7CNbOHk18OfPaQgWw9x5Y-Q8jQTMx_MaB53pKM2y8HMv03gPiNoHFlc3_2DXfNd6YnLKSpoRADbHxIKBG8be1VvJAub4PNO6dUmYLNgAfBPfUJYGHMZI5_lNg3k-fuVdph3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز شنبه دوم خرداد در گفتگو با آکسیوس اعلام کرد که اواخر امروز با تیم مذاکره‌کننده خود دیدار می‌کند تا آخرین پیشنهاد ایران را بررسی کند. او افزود که احتمالا تا روز یکشنبه درباره پذیرش توافق یا از سرگیری جنگ تصمیم‌گیری خواهد کرد.
ترامپ شانس دستیابی به یک توافق «خوب» یا در غیر این صورت، «نابود کردن کامل آن‌ها» را یک «۵۰-۵۰ محکم» توصیف کرد. به گفته او، قرار است اواخر روز شنبه نشستی با حضور استیو ویتکاف، جرد کوشنر و جی‌دی ونس، معاون رئیس‌جمهور، برای بررسی پاسخ اخیر جمهوری اسلامی برگزار شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75655" target="_blank">📅 19:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75654">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bli7-_wiNUCASYqgcNsq4tLWhLDGeP1g9ke-OydpX895Wd6cDUdel5ga9xG7CIZgZBHWlLk8U8wgXb05zA7aHo18MS5_V4oQEeS2mfum6FSpMyR2mMq7I4Em9jKykrjsdpDjNLobkyfOVnJlmLF-FjHOh5p5cEvL-CmQ_jKHde4vwOFESm0z2XIn6R7LrpRULbDVDOi81_Yo9voWN8d9D6PiO0Ufyl61HPalv_OPRT31p86qiAtJRA_qFCKX-YQSAZ4yqsHYjkz4_k9dgbGaZlOLAsUoyGNUkyyeAK_CLh9-IBKyup2gxwhe6bXVez_QU9yOdmJYtL92twrxdiumbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، رسانه وابسته به سپاه، درباره روند مذاکرات تهران و واشینگتن، با اشاره به اینکه هنوز اختلافات جدی در بعضی از حوزه‌ها مانند تعهد واقعی آمریکا به آزادسازی اموال و موضوع تنگه هرمز وجود دارد، نوشت: «با توجه به زیاده‌خواهی‌های آمریکا، احتمال عدم حل موضوعات بالاست.»
در این گزارش آمده که در صورت حل موارد اختلاف، احتمالا در گام اول یک تفاهم اولیه اعلام شود و سپس مهلت ۳۰ یا ۶۰ روزه برای گفتگو درباره موضوع هسته‌ای (بدون تعهد اولیه جمهوری اسلامی) اعلام شود.
تسنیم نوشت که آمریکایی‌ها در متون پیشین خود تاکید داشتند که تهران در همان گام نخست باید امتیازاتی در بحث هسته‌ای بدهد و موضوع تعطیلی تاسیسات هسته‌ای و تحویل مواد غنی‌شده به آمریکایی‌ها از جمله مباحثی است که مدام در متن‌های آمریکایی‌ها مورد درخواست قرار می‌گرفت اما حکومت ایران اساسا بحث درباره جزئیات هسته‌ای را در این مرحله رد می‌کند.
بر اساس این گزارش تهران بر ضرورت پایان جنگ و تهدید در همه جبهه‌ها از جمله لبنان تاکید دارد. و این موضوع باید مورد پذیرش طرف آمریکایی قرار گیرد اما آمریکایی‌ها در برخی از متن‌های پیشین خود با این موضوعات مخالفت کرده‌اند.
@
VahidOOnLine
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/75654" target="_blank">📅 19:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtzbRP19A_FHOODZost9I2UUc4FG2lMYi2IyXcURVKqbMqcsj2PbhvTOnQSsqq5WVpU-22_ldUL0kQeeaVhBeTMR5FQhvFpDJQ95ALsDRku50LAMuDsVEKvTbzNYhIpSfsm7ekZYJyGM79PjoXOTUVmFHg_ZujEZd1Eehjgf69z-F3S1c1N3_0S7f1ylZ5hhvchnkE-6CViTccFf8DLDe3yegYXFB5HEH-b-vcPC0xapgKukvsHuqIhOqAtvTkgvvbIFdnGkUob9h45NpS_UG2qhZuZyhw-XZO73KuidWtZYCLN57j55A2d35Kj5Z50mgUMJgb06-6ju5ltmEarVsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخش رسانه‌ای ارتش پاکستان (ISPR) آخرین دور گفتگوها میان میانجی‌های قطری-پاکستانی و مقامات بلندپایه جمهوری اسلامی را «کوتاه اما بسیار پربار» توصیف کرد.
بر اساس بیانیه منتشر شده، این رایزنی‌های فشرده در ۲۴ ساعت گذشته در فضایی مثبت و سازنده برگزار شده و پیشرفت‌های دلگرم‌کننده‌ای را برای دستیابی به یک تفاهم نهایی جهت پایان دادن به جنگ ایجاد کرده است.
ارتش پاکستان جزئیات بیشتری از مفاد دقیق این مذاکرات ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/VahidOnline/75653" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75652">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLPAzDqLubYNwmXo7nGFj3KRcMIPZeWTYrlYrrHLRZMl4i4egGMFOleaEtciZWYZGN4f-dWJsxwfoVYyVV7v7KmIMHC1MWqueh6V9sHfOLNbAd6jBSHwgFwoDYcX5IhPwuyYCN5K3_DvPiWEsZwgE5zgLd6ueuA2BGcDuNZmhivLrtYJjJQAdSycqL_rp06rYUsdRFeppFscDB6Nldp3PR4cwW_Z22n1IHSyREG0wK-OmKhekUqLwP4vLly5yIWfdrG3JprUYk5BbIigTs6IRicDSThTEjCdKiQeoK-AKygdWNwGs8qVGlJPpm9m4Lzo5C08q4QVNc-VpwGOhhh5oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال تایمز گزارش داد که میانجی‌های جنگ ایران معتقدند در حال نزدیک شدن به توافقی هستند که آتش‌بس میان واشینگتن و تهران را به مدت ۶۰ روز تمدید و چارچوبی برای مذاکرات درباره برنامه هسته‌ای جمهوری اسلامی ایجاد کند.
بنا بر این گزارش، افرادی که در جریان این مذاکرات قرار دارند به این رسانه گفتند این توافق شامل بازگشایی تدریجی تنگه هرمز و همچنین تعهد به بررسی رقیق‌سازی یا واگذاری ذخایر اورانیوم با غنای بالا خواهد بود.
فایننشال تایمز افزود که آمریکا همچنین محاصره دریایی بنادر جنوب ایران را کاهش می‌دهد و با کاهش تحریم‌ها و همچنین آزادسازی مرحله‌ای دارایی‌های مسدودشده تهران در خارج از کشور موافقت خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/VahidOnline/75652" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=tTX7hAVJI6p8iKnYeChcNrrKakRxfsYpiW2_FbSf1saZY-LLREtYQIxJrZ1uYl3brqTTi1vHAk8AzBrfp0ApqIQCNGBb0MnpgB9MQaO0NLtZq36YTslig0PEWOiAAsRSqgHjtiQP9oGPxGf6vXSRoM9RZBtUZnYAmXrKzRZNnc832Dw4Nk6t8O9Z4_rLQKD4A21Zsddriu7IZUrztERqi3aoP-MCUwVShOQfrePkV8xJDoBcyCj00T-wCoaZBWZXwARod-kW51PuzvI6dJUOLLBd_m_Ju1GiDEVWilpuD6ER0OllBsNkPnZglbxZyhOEtigHgIV_7fFA9w8sgWKUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d608f8c4.mp4?token=tTX7hAVJI6p8iKnYeChcNrrKakRxfsYpiW2_FbSf1saZY-LLREtYQIxJrZ1uYl3brqTTi1vHAk8AzBrfp0ApqIQCNGBb0MnpgB9MQaO0NLtZq36YTslig0PEWOiAAsRSqgHjtiQP9oGPxGf6vXSRoM9RZBtUZnYAmXrKzRZNnc832Dw4Nk6t8O9Z4_rLQKD4A21Zsddriu7IZUrztERqi3aoP-MCUwVShOQfrePkV8xJDoBcyCj00T-wCoaZBWZXwARod-kW51PuzvI6dJUOLLBd_m_Ju1GiDEVWilpuD6ER0OllBsNkPnZglbxZyhOEtigHgIV_7fFA9w8sgWKUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‌ویدیوهایی از اعتراض دانش‌آموزان در شهرهای مختلف منتشر شده است. این دانش‌آموزان به حضوری شدن امتحاناتشان اعتراض دارند.
دانش‌آموزان در شهرهای خرم‌آباد، یاسوج و دورود مقابل ساختمان‌های آموزش و پرورش این شهرها تجمع کردند و با شعارهای مختلف اعتراض خودشان را نشان دادند.
در جریان اعتراضات سراسری در دی ماه ۱۴۰۴ که به کشتار بی‌سابقه معترضان انجامید در بعضی استان‌ها مدارس غیرحضوری شد.
با شروع جنگ آمریکا و اسرائیل با ایران، مدارس در ایران تعطیل شد و بعد از تعطیلات نوروز کلیه کلاس‌ها غیرحضوری برگزار شد.
چند روز پیش عبدالرضا فولادوند، سرپرست مرکز ارزشیابی آموزش و پرورش در یک مصاحبه تلویزیونی از احتمال برگزاری امتحانات به صورت حضوری خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75651" target="_blank">📅 19:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JZ0aKc3U-DjFKNgz2B8dxw4lwl60bRkLIzZjxs6SbLoferDwvE_1EmDPnSYLJqi_jK9lnGToiQLztNxpKQpXz_gmYor4clyHE3bsZDHAsMVFFfQTBz7RhGV1k57f5uQQyxgIcFgPxlje5R1K0Xt-tlfYlxfVmOIBtSnl_nvA0j5Si2rtMKrg_NrGpGLmWpYqeWkitTQSP0uVpTYPjb9KZPkYpaPcC7se8HYfVE6pqpV1QCJry8KgpaPO3nDQCRWgvwLsO1HZ8boMx8KgNcc09GYYUVMvugPwtgYoz0g7f9h2GDSbACRR7UyotNlP7jDydP5lyCziAhUbN3sgW344rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام جمهوری اسلامی روز شنبه دوم خرداد، در گفتگو با شبکه الجزیره اعلام کرد که تهران با میانجی‌گری پاکستان با یک تفاهم‌نامه موافقت کرده و اکنون در انتظار پاسخ ایالات متحده است.
به گفته این مقام، مفاد این تفاهم‌نامه شامل پایان دادن به جنگ، رفع کامل محاصره دریایی، بازگشایی تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
او تصریح کرد که به دلیل پیچیدگی موضوع هسته‌ای و نیاز به زمان بیشتر، این تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود؛ با این حال، پس از گذشت ۳۰ روز از اجرای این توافق، درب‌های مذاکرات هسته‌ای باز خواهد شد.
این منبع آگاه همچنین اشاره کرد که قرار بود فرمانده ارتش پاکستان این تفاهم‌نامه را در تهران اعلام کند، اما او جهت هماهنگی با واشنگتن، ایران را ترک کرده است.
او با تاکید بر نقش اساسی دولت قطر در تدوین این پیش‌نویس افزود که ایران هیچ امتیازی فراتر از آنچه در این تفاهم‌نامه قید شده، واگذار نخواهد کرد.
@
VahidOOnLine
همچنین بر اساس این گزارش، تهران پیشنهاد داده غنی‌سازی اورانیوم بالاتر از ۳.۶ درصد را به مدت ۱۰ سال به حالت تعلیق درآورد.
@
VahidOOnLine
🔄
آپدیت:
خبرگزاری تسنیم، وابسته به سپاه، به نقل از یک منبع مطلع نوشت که خبر العربیه درباره اینکه تهران پیشنهاد تعلیق ۱۰ ساله غنی‌سازی اورانیوم بالای ۳.۶ درصد را مطرح کرده، «از اساس کذب است».
تسنیم به نقل از این منبع با تاکید بر «ساختگی» بودن خبر العربیه، نوشت: «اساسا تمرکز پیام‌ها و گفتگوها در وضعیت فعلی صرفا بر روی مساله پایان جنگ است و هیچ جزئیاتی درباره موضوع هسته‌ای مورد بحث قرار نمی‌گیرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75650" target="_blank">📅 17:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75649">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZnIMqluHE-78DWpidWaxebM9nWk0PvsO2cjJQZJXzwUrPa7hKQ58Nd-RzOQPTTQUO5e-gBC9KvAb3eVslRhknr0kAWKG2Wv_0qDLr87zjTX3_d9fGkkK6fNsOUqdyFbzSOnXMVF8aYY4SDFhnesXlRnhLL0s4v0X7Ahwa85ZHlvukUVOCMM0bp9SutXeBmyMLohFtw1deXScY8ZFT_4rN9lw71YwyIxI3ZdbpAum26uDJmcvKB0aSsXs67gXIigRilinQa-CrCtNbWgvGzyAhMqfnc3sO8dZA-ancfsz0emNE00G7hFES3IsUwrFvT989UBCVwsuyDBguSBq4FiuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه گزارش داد جمهوری اسلامی دو پیشنهاد به میانجی پاکستانی ارائه کرده که بر اساس آن، در ازای پرداخت غرامت از سوی آمریکا، تنگه هرمز را باز کند و پیش از امضای هرگونه توافقی، پرونده تحریم‌ها و دارایی‌های مسدود شده مورد بحث قرار گیرد.
دونالد ترامپ، رییس‌جمهوری آمریکا، پیش‌تر گفته بود که حاضر به پرداخت غرامت به تهران نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/VahidOnline/75649" target="_blank">📅 17:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QOrNlsI1XITpI7hIP3ivBgFlKUjZN_iLPGW3q2mTiA_E6lQ-UhDvo2me5RX8tFdcvE9Wmo5AVfZ1_brEwOngbq5KWzGDy1iEU-4lKCbFmGsjhxCLwo_87xLiWp3jDyUAw8q5B1aECFc73Gb8EI4-tc1eTfF0piFXLJyaHNUq5GKo6CkWPVo1Aq_gbWTIKph1YhqKrduFXjF3oodzHBJL700YZjoH7DJjIOLYus4VdOwOH38ea0wnfJxS7ZnW-FkK-Hhsbl54cEcYZhcJLkuMW4bQ_yKVxWeHPUZ_tE9PSBTJcGjYwYJKb9RJsmD1IQmWQPW8u8pIVaUvWmi4Ky2jAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ تصویری از نقشه ایران را که با پرچم آمریکا پوشانده شده، در شبکه اجتماعی تروث سوشال
منتشر کرد
. روی این نقشه نوشته شده است: «ایالات متحده خاورمیانه؟»
ترامپ توضیح بیشتری در این‌باره ارائه نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/75648" target="_blank">📅 17:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75647">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=OdqECFKkYH3kKMKn_RUMlS_YmWY_HcCEVJzK7RItpSGtt0P3f4qq8D7ZJpgZ4dLqeDG7PmEgYEduVjmuli8EDOUadM8t5QgXcB1T61VjEQwmNY1T9Fy6baFpbBlBnoEiPD_U0sAuOYXUtE8_m0J2k5s0iuBPwivoiRP-m1UOZIdmAIC-n1WO6dY5CilMF-x1MTT0wjrU670JV9ZBFir6PjdW9GyS_WtX4fBY6Ls990Mb5Q0onZjIuDuGo79xlNX0B85my_YQAkI4IMICj-hRA0FEu-niojI5SKTs0UdCPXWxuXGiPFlokGWDYwQVdBbSzLmytA3dbm82vMPNmKNeng" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028369f0dd.mp4?token=OdqECFKkYH3kKMKn_RUMlS_YmWY_HcCEVJzK7RItpSGtt0P3f4qq8D7ZJpgZ4dLqeDG7PmEgYEduVjmuli8EDOUadM8t5QgXcB1T61VjEQwmNY1T9Fy6baFpbBlBnoEiPD_U0sAuOYXUtE8_m0J2k5s0iuBPwivoiRP-m1UOZIdmAIC-n1WO6dY5CilMF-x1MTT0wjrU670JV9ZBFir6PjdW9GyS_WtX4fBY6Ls990Mb5Q0onZjIuDuGo79xlNX0B85my_YQAkI4IMICj-hRA0FEu-niojI5SKTs0UdCPXWxuXGiPFlokGWDYwQVdBbSzLmytA3dbm82vMPNmKNeng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان مارکو روبیو در سفر هند در پاسخ به سوالی درباره مذاکرات با ایران
ترجمه ماشین:
ممکن است امروز کمی دیرتر خبری باشد. در همین لحظه خبری برای شما ندارم، اما ممکن است کمی دیرتر امروز خبری باشد. ممکن است هم نباشد. امیدوارم باشد، اما هنوز مطمئن نیستم.
سؤال در مورد موضوع ایران است و همان‌طور که گفتم، پیشرفت‌هایی صورت گرفته، پیشرفت‌هایی حاصل شده. حتی در حالی که الان با شما صحبت می‌کنم، کارهایی در حال انجام است.
امکان دارد که چه امروز کمی دیرتر، چه فردا یا چند روز آینده، چیزی برای گفتن داشته باشیم. اما این مسئله باید حل شود، همان‌طور که رئیس‌جمهور گفته، به یک شکل یا شکل دیگر.
ایران هرگز نباید سلاح هسته‌ای داشته باشد. تنگه‌ها باید بدون عوارض باز بمانند. آنها باید اورانیوم غنی‌شده خود را تحویل دهند، اورانیوم غنی‌شده با غنای بالا.
ما باید به آن مسئله رسیدگی کنیم. ما باید به مسئله غنی‌سازی رسیدگی کنیم.
این‌ها نقاط مورد نظر رئیس‌جمهور به طور مداوم است. و ترجیح او همیشه این است که آن را از راه دیپلماتیک حل کند. ترجیح او همیشه این است که مشکلاتی از این دست را از طریق راه‌حل دیپلماتیک مذاکره‌شده حل کند.
این چیزی است که الان روی آن کار می‌کنیم. اما این مشکل حل خواهد شد، همان‌طور که رئیس‌جمهور به وضوح گفته، به یک شکل یا شکل دیگر. امیدواریم از طریق مسیر دیپلماتیک انجام شود. این چیزی است که روی آن کار می‌کنیم. و شاید چیزی برای صحبت در مورد آن موضوع در حالی که اینجا هستم، در طی این بازدید در زمانی داشته باشیم.
EricLDaugh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/VahidOnline/75647" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75646">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkVqHNpyZm6dKS90ME547SpKiIYCozBIrCSrVckkNqCxKJaQKGCE8U-80cMWxontaf3wduXEoiCxbmza6Nrr-w_PiBVN4Bzs6ds3qFkvHHTPekwMnsMmQrO5FgsCtcZZm13DhrQ2ZHUN-Igfq_UTXZ3VigQK52IEut4N-nixRyOIx-94HWNnN7g4DYFO-nLboTUv0oWB0J4ZaJxQG3xxTqruhizScdbKsa5uASzZBrHrc2WiMN-WwVY87AEZltpSWIPAQMQuWYPIMQ6hCrevy88W3G7BxrE9Ep9tY2AhrtOPjm5QTPeKFbpvFgxzmDMHb_lQUDEWLt2hNWuvdomMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در پیامی به شیخ نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «جمهوری اسلامی دست از حمایت حزب‌الله نخواهد کشید و همچنان از جنبش‌های مطالبه‌گر حق و آزادی پشتیبانی می‌کند. تهران پیوند آتش‌بس لبنان با هر توافق احتمالی را به‌عنوان شرط مطرح کرده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/75646" target="_blank">📅 17:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75645">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB9HZSIo9VZa-kUvxc-Ubj_BSCYHBOr6qY08ujmz725utU2Xjf4olTs8nYUZgudt2iRyVANOzGkWulJsbmr9mEbovppOGSQTxbF5MY9ckNpZvsHVOpo3DAapPjZLm3a0HeMxZ4MMlCrKEH5H_zVc0me6ff3mogQFF05dNhsjuoyVbDdmcu6Zh76qXyiO29IYgI3Q5wZ3riYsdDPdx8vtGRKkFsMt7ilfcD6_KTEuXfgTTm_X8MVfrpvZ5_6UqqtYgpHRfjwnqJW7BlJaUjTYPSFZceemrBK_lyqM845TuZOwB13BBLFy6M7Ccx4XxvXHIa4rLhLR-9ZAQ7SG6_LYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرویز قلیچ‌خانی، کاپیتان پیشین تیم ملی فوتبال ایران و فعال سیاسی چپگرا در ۸۱ سالگی درگذشت. او به آلزایمرمبتلا بود.
نجمه موسوی-پیمبری، «یار و همراه» پرویز قلیچ‌خانی به بی‌بی‌سی فارسی گفت: «قهرمان ملی و چهره همیشه زنده ایران در تاریخ بیست و سوم ماه مه ٢٠٢٦ مصادف با  دوم خرداد ١٤٠٥ در بیمارستانی در حومه پاریس درگذشت.»
آقای قلیچ‌خانی، پیش از انقلاب، علاوه بر تیم ملی، در باشگاه‌های تاج، پرسپولیس و پاس هم بازی کرد. او تنها بازیکنی است که با تیم ایران سه بار قهرمان جام ملت‌های آسیا شده است. پرویز قلیچ‌خانی بعد از انقلاب هم در خارج از کشور، مجله آرش را با گرایش سیاسی چپ اداره می‌کرد.
او فوتبال را از کوچه‌های محله صابون پزخانه میدان شوش تهران شروع کرد و بعد از مدتی کوتاه فوتبالیستی ماهر و بالاخره کاپیتان تیم ملی ایران شد.
ولی هنوز طعم قهرمانی فوتبال را درست نچشیده بود که توجهش به سیاست جلب شد و از پشت میله های زندان سر درآورد.
پس از انقلاب از فوتبالیست حرفه‌ای به فعال سیاسی و روزنامه‌نگار خارج‌نشین تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/VahidOnline/75645" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CpetI_1ZvWhuVBL6Qz94c9M8jUW6hP_oJsifbx6voaJ1tjZ2x2kkLUkXrWOLtKt5a6IP0OcI-zV0ADYDHLmV_hinZ2KjtQZtWJqKQt1e610LXSJG4vgtj5tQkKDnSwP4YA6t3Oi5zEMups8uk61fctJsZkAUkaN5v7t_4m6F7e2o0w5W4IOCLHUopQnSMtRONSQlhinVclPPwqME1LE4ULvlaSEcZJcl-uqwN70boCUtfJsvlAPSQcks11NXCa443-H4aembOYEcqpma5f9qorIbKrCmH60Wxu7eeugARwiG3fNL2AwBCMsBFuAy7CpFHAKc_L2L57feDsbhZ1uUbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/av5_J2I8K9cUMmolic3f-ZcZet5fPn6PuFI0wUpajNOdWsdtYvd-ZCT5lQvKP6C8878oteJoqU_sh7vNobJouj7Fqv-v1z0zQyZiMz4_DQvZq8GCPTK0esN7Odmi02JUsHztNe_DcOgbSrk-GCxv_puS587k0S9X6TTqofMyhvvDz9LVXXR6_CNu0WyIbSMdquv_LwUAqh4NrA68EbFfrYHyAfLLRRFwppJATs2fWG9-vMY9hY86C5F8VtWBJYXYsEaJ5dQkVLgVp1l3BiSOulSK6D9cK-84V71dqyJnXHG54xEvLcBc-WkeuSb7PdmMC-QUfTm7v5WkJiIWFMXuQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dL3QS4BSdn9x8tyJymOqFo2O9JPvmvDfo2o7QnJ_y4-mz_-QvnLJVOUdSuepfYx2nQAZ_vy4d80qAKm9O9Vc9n7Q6WWtQCrzxSL_W_ci1epBPgkSKkKZ_2Xifics5Dqh3H29dW99k5m9UZCXk5yHyGCoLorPX546RUUtlalI3hd6mdXPI_CMptdScjnwGk8R_5bTaTXrJAgHQjPd_vfPny2JXP_fPgLaQ95K33XynU6x7yvCOwvjeb5K9CH9GhuMkNQ_HumCa1RQw2AN6GIb6zc1Ro6Q_-gzoLAwlpe94h3HmdZwexFQg5Yzr7Ku8t1ZcqdTInh8zUdLwsk_N1fkFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pt0KiuaIUDonpGGksnCF17U-AElglooIhQz9bwmxEJXAknvMvOnWxD676FRCSNaylXhGx5pLAWIHsm2oazmONDB45k_MEAy2YjnwCJQoJYXvcga_jEzIUoyHGg2XUc39bJ1syOSvx-7AXWcSyffGPhgzxf1r4rmUan7IBO-jVGnAXTLPpKVMvulyKC144WHJZlyCc7w14CPdvXrasReVEQebUCFPu-UykyY2Ktt-joK7xghM77J5VQsZMhtl5sn9JejHLaBmMGmnCyHuKSC5dwqiv_GAC1JqQqDyIWq8mKUzPkau5NUtY53lA_HsUg3qVZjKH9-jSORQzSTvW8-14Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RlZvAaMma0QH_0A9w2cPu2JxMLtXF9KAml8ZEW_ryAFqADcO9LdmjMBsGYXzVCJibZJFvuoxi7ahVx-OTCG1QtFtGUR1V2DrozBD2luU4jGxT-rEAWcqRIyxY7L7weO25JAOuhC-INMzVTbkh-SwXNe9sDoarjGjarpTqdVcuVhvZiTJS_IZQYlrKwWgMfoLxCUZtjn8OfpBAZnti5cc_7vpe-EnFHkMbCf-SiVR_TrIncDbzzqOHU1_leDKHqAhlKcfHdbhpyVIIKtwhWqQ6cLVh4caC3OmYMr9TvMezoT6TAGZqTHoRr5OWMjiOJZwteVcVTNsWdbahrtWmRavRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OYcqedqf68WQrE9VoxF1GXIsTcTph5RNMy6KtJgt61i1Ytaby5qgHu3CzU4gsLZt_gVWnDTNhm47WkX47k-w4fJg_VPA6r7wdpjtXNsUn534l0qEamXBurNWF4PgkP66KvI8ais7wy2ixtdY0HUwpWLIwFH6v63EPJAKKngLrcL4-yMbJw1FKJ-iNEyRJkmqeSPVrQEe7aLlW3iZ7iskIBX756Ou4BAMOdDgacO7NE7SY3SGFdpYjKXaO9XFRk2iRX2yKuTNQWS5TfSvvSKNXa75pmA897PgrBhZWufr9JYQbLQbdbh6lnJda7He3d5H1k0KUox9EsapXI26hCYw7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cm8vc7iO1K3UFEeNQnb_4ceGXdDlcfa9zn8RFE5q4_UaiUIYF0XBNOgRn-ijf107pPGcAb6H1FVn9eVzjfUZPkbJnWwcDX5VxkNttgvGfX47P2lvIA3DAo8COKqqS3WoMJxr1i8ClIqxshuNDAokog_Dr4U6lY8sfQf3tf0C1fFN30t8auGV2RsXrRzoayqTe0IQjAlcwZZmiOVdH54wu4RKI0wEp8s-Q5L84tQWJd3M4Wgo2ejr53qmQwf0J8zJuDVg-KWNRXyauMxSXcEd4yTYqWi52hJ9qKAPa3qfEVDlFbM_ekIZqLZP5FsoOPPyt2Gn6x5GWsXKZbXrY24xvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C4t9of5a7edDRHjD-KYrx-kXA7ugmQ5pFjO7Sbpb_-wdA7O5c331f3FxMB4v7drAq1ZN05DzaXwvQOixFYGqeekrhhEh2vF350bTUMh8-0pvKOJ0cTzGG04BexWBjesXFYZRY-CxG841Y0ONse4r1rhr1xaz_jn9Xa2Yjnr99qZG8tIytW19QpHi22G_5Ah0h8B_3sWP-UINPl7tFDZmf7PbjZGx-0pUEqdKYMCPY3gSBRrcv60PoPzCQ2OjKVCXogMUYrBGAbYmntTidlW1XSFQecByOZMNQJKUbpn-AwUOx45ytXkMkj_NJ3goev5FpXwLJkKeXyDRNdzWPY1Dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S-Quo5OcWZXv-7AZMeZShrQf8-rj6M9t8moY_y1gLRFt5t8qOX56XFmcUzZwrEp6EwtP0yXxTU2ZhSNNd7ew_TP3eeLVQCAR7I7AjgNQtWNxoaJc8N9SDuBPY8C1wVnfQl0M6_5wRxJRA5W-bUq2_dbToGtpsJbqj5Y5PjBoL_LL0X6H2Q1e7evTgGYZ-ePQQ9YRdvbccPWPjCsFb2pOoiO6jGzVf9YYla5qELlBT1LBuvetuap3wJo8IbVfhnehE40skp3eIRLX8GNIkeHtk2-hxZYiXFAhLJmuZVUDImNVJxffvQMVoeQWcIi1j4K3iTIQo2ufxSXpoSWaABiMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/exvaaOrJDmTSr5AD-qwjPDA1TRRyz1OFEdkNfWKwVonw6O_MM8Zl9Cui-h-rW56cwMCYuNZgoLARJUZaV2uRWywyZikMntvo2PPpFMz8nVtm-PPWrjGkDeR_D2107pUZrRdojmzPpY7pNEIFu8ql9W-Ge53XKdedX8XoAz190NndmonULJUtBZ0gD343II34OPtf2n165i8uJd_iHXSNddKLZqM1g8zbDBkuhgLiZArNaJ9qSprt2B6ynfLc_q6iUyZJ2u0LfCcPZQKcgLTWbINX6QMvNOTdxHMZ-08yURX5DdVRoJQme_-QJkCVli2JHFaEyzOsd7CDI8yZXZWptw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد عاصم منیر، رییس ستاد کل ارتش پاکستان، پیام‌های آمریکا را به تهران منتقل کرده است و بخشی از این پیام حاوی تهدید به ازسرگیری جنگ بوده است.
در این پیام‌ها همچنین تاکید شده در صورت موافقت جمهوری اسلامی با توافق، حل مسائل اختلافی در مرحله بعدی انجام خواهد شد.
به گفته این منابع، آمریکا در پیام‌های خود تصریح کرده است تهران باید اکنون با توافق موافقت کند یا با پیامدهای منفی روبه‌رو شود.
@
VahidOOnLine
شبکه العربیه،  روز شنبه دوم خرداد ماه، به نقل از «یک منبع بلندپایه ایرانی» گزارش داد پیشنهاد ارائه‌شده از سوی تهران تاکنون نتوانسته رضایت آمریکا را جلب کند و همچنان از دید واشنگتن «غیرقابل قبول» تلقی می‌شود.
@
VahidOOnLine
عاصم منیر، رییس ستاد کل ارتش پاکستان، پس از سفری یک روزه به تهران، ایران را ترک کرد.
به گزارش ایرنا، او به همراه محسن نقوی، وزیر کشور پاکستان که از هفته گذشته در تهران به سر می‌برد، پایتخت ایران را ترک کرده است.
عاصم منیر در جریان این سفر با محمدباقر قالیباف، رییس مجلس، مسعود پزشکیان، رییس‌جمهوری ایران و عباس عراقچی، وزیر امور خارجه دیدار و گفت‌وگو کرد.
@
VahidHeadline
محمدباقر قالیباف در دیدار با عاصم منیر گفت نیروهای مسلح جمهوری اسلامی در دوران آتش‌بس بازسازی شده‌اند و در صورت آغاز دوباره جنگ، واکنش ایران شدیدتر خواهد بود.
او گفت: «نیروهای مسلح ما در دوران آتش‌بس به نحوی خود را بازسازی کرده‌اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده‌تر و تلخ‌تر از روز اول جنگ خواهند بود.»
قالیباف با اشاره به نقش پاکستان در میانجی‌گری افزود: «در آتش‌بسی بودیم که شما واسطه‌اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا به‌دنبال برداشتن آن است.»
@
VahidOOnLine
شیخ تمیم بن حمد آل ثانی، امیر قطر، روز شنبه دوم خرداد ماه در تماس تلفنی با دونالد ترامپ، رئیس‌جمهوری آمریکا، آخرین تحولات و رویدادهای فوری منطقه را بررسی کرد.
بر اساس بیانیه رسمی دیوان امیری قطر، این گفتگو بر «تلاش‌های منطقه‌ای و بین‌المللی برای حفظ آرامش کنونی و کاهش تنش‌ها» متمرکز بوده است.
«امنیت دریانوردی، حفظ ایمنی آبراه‌های راهبردی و تضمین تداوم روان زنجیره‌های تامین جهانی و انتقال انرژی» از دیگر محورهای این گفتگو توصیف شده است.
به گزارش رسانه‌های قطری، امیر قطر در این تماس بر موضع ثابت دوحه در اولویت دادن به راه‌حل‌های مسالمت‌آمیز برای بحران‌ها تاکید و اعلام کرد قطر از همه ابتکارهایی که با هدف مهار بحران‌ها از طریق گفتگو و دیپلماسی انجام می‌شود، حمایت می‌کند.
این خبر در حالی منتشر می‌شود که رسانه‌ها از گفتگوی تلفنی وزیرامورخارجه قطر با عباس عراقچی خبر داده‌اند.
همزمان گزارش‌ها از رایزنی‌های گسترده کشورهای منطقه برای جلوگیری از حملات احتمالی آمریکا به ایران خبر می‌دهد.
این در حالیست که شبکه خبری العربیه پیشتر از هشدار واشنگتن به تهران مبنی بر از سرگیری حملات به ایران خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/75635" target="_blank">📅 17:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75634">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFLC_c7eca_uIBkj_ZoPhnXeogQCXxzdy2jmYvphBJm6s0HoiDzEmkTqgcL-Jcnvo4dbAkwYw07asC7PQeAv4LbH7rR3btpQCKjlRXMR1XYOiUu5_L1WP-1ghQS17FV0HRIgqqDb7UQ_yzKokDw58UPW-_Gryqb9uKrv_rZs0UJlcnhUEC-Rk3HdCKXuHABZS87GTrAOKZMdaAP_lpIQTzXaTg7rthJFCFazIwOqXEsImHOa-k5NSL58H-a392SpLmf7qEEdmy6U_YnKhhw5YnI0meOuR3IYZEHAL_HcdfS6pHiVmWDKaILbC6PRsJedNDVk2PowuRuwRiFVAoFCMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان هواپیمایی ایران اعلام کرد این سازمان هیچ اطلاعیه رسمی هوانوردی جدیدی درباره اعمال محدودیت در آسمان کشور صادر نکرده است و شرایط پروازی عادی است.
او با تاکید بر تداوم وضعیت عادی پروازها گفت: «شرایط آسمان کشور همچنان مانند روال گذشته است و پروازها طبق برنامه انجام می‌شود.»
سخنگوی سازمان هواپیمایی بدون اشاره به جزئیات اطلاعیه هوانوردی (نوتام)، افزود: «نوتامی که اخیرا در فضای مجازی منتشر شده، تکذیب می‌شود.»
سازمان هواپیمایی کشوری ایران روز جمعه یکم خرداد در اطلاعیه‌ای اعلام کرده بود فعالیت فرودگاه‌های واقع در بخش غربی محدوده پروازی ایران، موسوم به «FIR تهران»، تا دوشنبه متوقف شده و تنها شمار محدودی از فرودگاه‌ها مجاز به فعالیت هستند.
بر اساس آن اطلاعیه، فرودگاه‌های ارومیه، کرمان، آبادان، شیراز، یزد، کرمانشاه، رشت و اهواز از این محدودیت مستثنی شده‌اند و فعالیت آنها نیز فقط از طلوع تا غروب آفتاب مجاز اعلام شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75634" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWNrH2aMRo3SGvpFHyO-mQUesWCt5zh0WmUMRu44kCCpiSrBpUpIBPKIw7cD_0JVBS3Ff8O0fZu4efvHadvVnFBZ9NPfKX0omxRxHq95buPWMDTyVxm4EcnjBljHSjm2Gkm0bd9YTL85AvDoPLYSdGlAHj8d01r7o4MpBpalKRLhNmG1FA-M0ZuuXMd0kPpR4IwPtPvBELQoIC7i6q6K2HkTYk9c2GGAmlAhkI82C0UgZN18Fr0reT47wAbavrexkBINX--EgN84nevhp3kNQyd4ZBWBcvv7i62hetQHI9nmOuY0W54tlDc1XZ4KUcy_dIKbRvsR-4XwBvB4t9bXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از دیدار فیلد مارشال عاصم منیر، فرمانده ارتش پاکستان با عباس عراقچی، وزیر امور خارجه ایران در شامگاه جمعه یکم خرداد خبر دادند.
بر اساس این خبر، دیدار این دو مقام تا پاسی از شب ادامه یافته و محور گفت‌وگوها «تلاش‌ها برای جلوگیری از تشدید تنش و خاتمه جنگ» و «راهکارهای تقویت صلح، ثبات و امنیت در منطقه غرب آسیا» بوده است.
جزئیات بیشتری از این دیدار منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75633" target="_blank">📅 08:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufQiW1kuJcUjlxo9JE47ptCsYUl5BgHCcb76wVLkLpjCYUQ3mtMWUxGyMWvIrT3EsQ0TZ7jSXPS2g07SuZrJKkeaXXfWkM_Tq2QAATSeT9uYGh28wpziR4nde3q4rihevD6pQW0lFmLnM93s76i0qwTQBJRTatSpJzsqN7XmJr1XZix0E4dtlPgs3eiEqaU9H8fBfkizYFHdne3-MTywaGIbJ9lfJke3rC2Ns_9CrHJyHVGcuRlMe7_9ePGjD-IIeKrG3GzRXEZbnW7YNgz2Pide8uvgEfGbkIBu_ab5Knj_bGa6h3xnzHAZAERevdkBFdGtIZFVySWG95rKj-w0iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ اعلام کرد که سیاست‌های مهاجرت به آمریکا تغییر می‌کند.
در یک تغییر اساسی در سیاست‌های مهاجرتی آمریکا، دولت این کشور اعلام کرد خارجی‌هایی که قصد دریافت اقامت دائم یا همان گرین کارت را دارند، باید خاک ایالات متحده را ترک و از طریق کنسولگری یا سفارت آمریکا اقدام نمایند.
زک کالر، سخنگوی دفتر مهاجرت دولت آمریکا، گفت که این سیاست «نیاز به یافتن و اخراج» کسانی را کاهش می‌دهد که درخواست اقامتشان رد شده است.
از سوی دیگر وکلای مهاجرت و گروه‌های امدادی می‌گویند که این تغییر احتمالا به «جدایی بیش‌ازپیش خانواده‌ها» منجر خواهد شد و قربانیان قاچاق انسان هم مجبور خواهند شد «به کشورهای خطرناکی بازگردند که از آن گریخته‌اند.»
این تغییر سیاست تازه‌ترین اقدام آقای ترامپ در محدود کرد مهاجرت به آمریکا است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75632" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75631">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLTiq7xVjqrtRbIv4ADraKBbRKD1gM8RBSMmKmo701lmKGLwuw74bzuQg4xJ5OELdRRvZVTmPDbKhz7IdhWvsW6ifsOS951MHDCfHn9WEiaaNYZpnLVfvKOOpujk3rOOrDTxYXWO0EPAdX6jwnwfFjI-8Q1_e5DjTPLT2mi7-My99QuU3_kt3rx6msSvcW5iqMsxYlT46nnf9hBbXDkBcLf2Mi8lxK9lsTtFDF47nZnDOlY1xDhlpw2vrJTRUNexdtVKjaPISyBmLrN0v6dfJUG9wYNDC9qQKmPn48z-K34nJR_abBd6bJ-WKkdEFkbFjgNLhXn2XtS6mvvdXujMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه «نیویورک‌پست» به نقل از منابع آگاه افشا کرد که ایوانکا ترامپ، دختر ۴۴ ساله دونالد ترامپ، هدف یک طرح ترور پیچیده از سوی یک تروریست تحت آموزش سپاه پاسداران انقلاب اسلامی قرار گرفته که با انگیزه انتقام‌جویی از کشته شدن قاسم سلیمانی طراحی شده بود.
بر اساس این گزارش، متهم که یک تبعه عراقی ۳۲ ساله به نام «محمد باقر سعد داوود الساعدی» است و به تازگی دستگیر شده، عهد کرده بود برای «به آتش کشیدن خانه ترامپ»، دختر رئیس‌جمهوری آمریکا را به قتل برساند.
منابع اطلاعاتی اعلام کرده‌اند که الساعدی حتی نقشه و جزئیات معماری عمارت ۲۴ میلیون دلاری ایوانکا ترامپ و همسرش جارد کوشنر در فلوریدا را در اختیار داشته و پیش از این با انتشار تصویری از موقعیت این خانه در شبکه اجتماعی اکس (توییتر سابق)، به زبان عربی تهدید کرده بود که «نه کاخ‌ها و نه سرویس مخفی آمریکا» نمی‌توانند از آن‌ها محافظت کنند و انتقام تنها مسئله زمان است.
وزارت دادگستری ایالات متحده اعلام کرده است که الساعدی از مهره‌های بلندپایه در حلقه‌های تروریستی وابسته به ایران و کتائب حزب‌الله عراق به شمار می‌رود که در تاریخ ۱۵ مه در ترکیه بازداشت و به آمریکا مسترد شد. او در ایالات متحده با اتهاماتی سنگین پیرامون هدایت و اجرای ۱۸ حمله و تلاش برای ترور در سراسر اروپا و آمریکا مواجه است؛ پرونده‌ای که شامل بمب‌گذاری در یک بانک در آمستردام، حمله با چاقو به دو شهروند یهودی در لندن، تیراندازی به ساختمان کنسولگری آمریکا در تورنتو و آتش‌سوزی عمدی در معابد یهودیان در بلژیک و هلند می‌شود.
این متهم که به دلیل وابستگی به قاسم سلیمانی او را مانند پدر خود می‌دانست، پس از کشته شدن سلیمانی در حمله پهپادی شش سال پیش آمریکا در بغداد، تحت آموزش‌های نظامی و اطلاعاتی ویژه سپاه پاسداران در تهران قرار گرفت و ارتباط نزدیکی نیز با جانشین او، سردار اسماعیل قاانی، برای تامین مالی شبکه‌های تروریستی خود داشته است.
اطلاعات فاش‌شده نشان می‌دهد الساعدی با وجود نقش برجسته‌اش در شبکه‌های تروریستی، حضور بسیار فعالی در شبکه‌های اجتماعی نظیر «اسنپ‌چت» و «اکس» داشته و تصاویری از رایزنی‌های نظامی خود با قاسم سلیمانی را نیز به اشتراک گذاشته بود.
او با تاسیس یک آژانس مسافرتی مذهبی و با سوءاستفاده از یک «گذرنامه خدمت عراقی» که سفر بدون تشریفات امنیتی و اخذ آسان ویزا را برای او ممکن می‌ساخت، به راحتی به کشورهای مختلف سفر کرده و با گروه‌های تروریستی ارتباط می‌گرفت.
الیزابت تسورکوف، پژوهشگر انستیتو «نیولینز» که خود ۹۰۳ روز در اسارت کتائب حزب‌الله بود، تایید کرده که روابط الساعدی با سلیمانی و قاانی فرصت بزرگی برای گروه‌های شبه‌نظامی عراقی ایجاد کرده بود. الساعدی که در زمان دستگیری در ترکیه در حال سفر به روسیه بود، هم‌اکنون در سلول انفرادی بازداشتگاه متروپولیتن بروکلین، در کنار دیگر زندانیان سرشناس نگهداری می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75631" target="_blank">📅 04:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75630">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKfvcv10B9KCgZ5CWG99pBrcj5EuTgZMaWXG9v3x7x7bhFrxbGxW5ndBGt3U9yzQpCK13KpAiGJnqAFE25lSiaT_kenll9wi5id4mLm1mdHMv0haVHXqFKqwLUgTTnImyOK1Jgafw6AylOaRr8qx9DuxfEk9j5FXo-saXOEG3HTNo0Q7kaN2-1uWFjxpt5kY7_x-civWyh_qAAJxf2O4ZcC53YkrHWN4uhdTcZtVGEFoBZSiKpLDYLW5yYPF-UmGPQUdoiIAyiUwPm2S1i6W6H0wUIbaSqkVHK1Tog0HfwFOyeni4KlU6Ew5hB2lm_9ddwTm8UApbrVA7ee3hn1hqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌بی‌اس گزارش داد که آمریکا در حالی خود را برای دور تازه‌ای از حملات نظامی علیه ایران آماده می‌کند که تلاش‌های دیپلماتیک همچنان ادامه دارد.
به گزارش سی‌بی‌اس نیوز، منابعی که مستقیم در جریان برنامه‌ریزی‌ها قرار دارند می‌گویند که دولت ترامپ روز جمعه در حال آماده‌سازی برای حملات تازه بود هرچند تا عصر جمعه تصمیم نهایی گرفته نشد.
آقای ترامپ در پیامی در شبکه‌های اجتماعی اعلام کرد که «مسائل مربوط به دولت» مانع از حضور او در مراسم ازدواج پسرش، دونالد ترامپ جونیور در روز شنبه خواهد شد.
او قرار بود تعطیلات آخر هفته را در مجموعه گلف خود در ایالت نیوجرسی بگذراند، اما اکنون به کاخ سفید بازمی‌گردد.
چند منبع نیز گفته‌اند که برخی اعضای ارتش و جامعه اطلاعاتی آمریکا برنامه‌های تعطیلات خود را لغو کرده‌اند؛ اقدامی که در انتظار احتمال حملات تازه انجام شده است.
به گفته این منابع، مقام‌های دفاعی و اطلاعاتی آمریکا در حال به‌روزرسانی فهرست نیروهای آماده‌باش در پایگاه‌های خارج از کشور هستند؛ همزمان با خروج بخشی از نیروهای مستقر در خاورمیانه، در چارچوب تلاش برای کاهش حضور نظامی آمریکا در منطقه و نگرانی از واکنش احتمالی ایران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75630" target="_blank">📅 04:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75629">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nR0A-rPDNrUQ4rd36AXq_kV5ZhTAtaYs9VxTb4D1uDrtaSL1mJcguYjFpkqHrsg4kbXQB6i124hyHVlsnplxXke40F96i0OSFmguf8gLQ9s3HuTQyth9euCGIkZ4CQpiVtNFOD8UtPPs5LuqTmShiWhrYId2Uxpj45KrWUCjFnJORaNuGfAIrzGXLg8R4yE-ctAgA1-aDgIb_rCngbFq2Hcpof7VeBa8fl_GRi5ullDnb3YEjq5lS5BstRfe7LRig2MO-m130sf2XE_LSBGIkWT-z3RlhsuRRJbegbVi2-Se7eC1t2Z431nh-JV7r-SvTTeLCut3dZy4wtnXIdpOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، دونالد ترامپ، رئیس‌جمهوری آمریکا، روز جمعه با تیم ارشد امنیت ملی خود در کاخ سفید دیدار کرد تا سناریوهای مختلف در صورت شکست مذاکرات و احتمال آغاز حملات جدید علیه ایران را بررسی کند.
در این نشست حساس که با حضور مقامات کلیدی از جمله جِی‌دی ونس، معاون رئیس‌جمهوری، پیت هگست، وزیر جنگ و جان راتکلیف، رئیس سی‌آی‌ای، برگزار شد، ترامپ در جریان آخرین وضعیت دیپلماسی قرار گرفت.
نشانه‌های جدی از تغییر برنامه آخر هفته رئیس‌جمهوری، از جمله لغو سفر به باشگاه گلف بدمینستر، بازگشت به واشنگتن و حتی عدم شرکت در مراسم عروسی پسرش، دونالد ترامپ جوان، نشان‌دهنده وضعیت اضطراری در کاخ سفید است.
منابع نزدیک به ترامپ می‌گویند او از روند کند مذاکرات ناامید شده و به سمت گزینه نظامی متمایل شده است، هرچند هنوز تصمیم قطعی برای از سرگیری جنگ اتخاذ نشده است.
در همین حال، تهران به کانون تلاش‌های دیپلماتیک «لحظه آخری» برای جلوگیری از شعله‌ور شدن دوباره جنگ تبدیل شده است.
عاصم منیر، فرمانده کل ارتش پاکستان، به عنوان میانجی اصلی، در سفری حساس وارد تهران شده و قرار است با احمد وحیدی، از فرماندهان کلیدی سپاه پاسداران دیدار کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75629" target="_blank">📅 00:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75628">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ms6Bm51yKBNogXeSHVKul08rPyHK9laIhbJzyoJ8hW_2PYipQfUL2kqjOLmXzaQe_YpXkHWCFj5flJQiAjrb3Zoiji9AGeKM8E0fhh7QANWbar35dr9HK6bY_LPCPvyeZz6VraTIexVW99i1PFwJRnIy9THSBB_xfiObl7mLhvAozCV9qVTeTjg1_RsYbxnN_PWbfLRPfhlzKxSaCDnTvEDZCSKsRfmbPS7r33KZNljzHYcIdmN3DCIFqRoLkBttUFXGtRWfEzyUKiO530687B3LJ__oZtEIkknLDH_2uFaom30F26S2B2HvvzOWirsjTGPpFpLj3GirJnYyqqyMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از یک منبع نزدیک به ترامپ نوشت که رییس‌جمهوری آمریکا در روزهای اخیر به‌طور فزاینده‌ای کلافه شده و احتمال انجام یک عملیات نظامی نهایی و گسترده را مطرح کرده است؛ عملیاتی که پس از آن بتواند اعلام پیروزی کرده و به جنگ پایان دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/75628" target="_blank">📅 22:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iaKuMewbHTWB-Lkbx9cOFnsGRbLBTMEHKkxUV9T33VQvZ6ZUxDYClyAQy6Xu38BcejDgSpR90ufqa97YPyHQYmioZQaBYJa_IJHcQA5ydzH9K71NbjAkjUPYo9DtPbScBDfHaJUj0kiXiwuHF0t-XfuUWDEuNPo3e6LLNNu9gLM0qJWCwe5G5cF41yQFuSaIhWHsdbSbOjnBojagQ_NVIzsOoLD95btxT2R-mGhRBw-JkMWj6gYi-SFFR6XGxpFrQdH_ErOCbhZntlF-BtTseqyxO18YRB_t0Hcu4vxW9HBtWfJBop71goHgerlcnL3VocWbTk1orScJiBBBUILssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی هیئت مذاکره‌کننده ایران با آمریکا روز جمعه گفت که موضوع پرونده هسته‌ای ایران در این مرحله مورد مذاکره نیست و از اختلاف نظر عمیق با آمریکا خبر داد.
اسماعیل بقائی گفت: «اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم.»
او گزارش‌ها درباره قریب‌الوقوع بودن توافق با آمریکا را رد کرد و اعلام کرد: «نمی‌توانیم بگوییم ضرورتاً به جایی رسیده‌ایم که توافق نزدیک است.»
بقائی بار دیگر موضع جمهوری اسلامی درباره برنامه هسته‌ای و اورانیوم غنی‌شده را تکرار کرد و گفت مواضع ایران قبلاً اعلام شده است.
@
VahidHeadline
سخنگوی وزارت خارجه ایران حضور هیئتی از قطر را در تهران تایید کرد
اسماعیل بقایی،‌ سخنگوی وزارت خارجه ایران تایید کرد که یک هیئت از قطر روز جمعه در تهران بودند و با عباس عراقچی وزیر خارجه ایران گفت‌وگو کردند.
او بدون ارائه جزئیات گفت که کشورهای مختلفی طی روزهای اخیر با وزیر خارجه گفتوگو کردند اما تاکید کرد که میانجی اصلی میان ایران و آمریکا همان کشور پاکستان است.
پیشتر رویترز به نقل از یک منبع آگاه گزارش داد که هیئتی از قطر در هماهنگی با آمریکا وارد تهران شده است.
قطر و امارات و عربستان سعودی سه کشوری بودند که آقای ترامپ روز دوشنبه گفت که به درخواست آنها فعلا حمله مجدد به ایران را متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/75627" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKAgO9FBdIbR1VDSSlJTUpbukmES7J2a4BO0vh1_CGrWjvVAIZ6Fk9MHsSygiB0Y9Fa7DPC3G2Xir5YDeDEiM8fVDX0oPWq-_3Ulec-haiigy8P-BxlqtBGZElws3aQv8WiDJ_231cvCovqDV4Fd1NaxkJOd-gvVCattWBjZfNgGvkTfwTB6OAvKZtw7j1jQKk2AUwoWvVEEaLe--fO8az7oyCTT_9UBKH4fl-Zdl4zMRq1BGP_Q2RfH2lWqxTbKkr0k1NmZZktKhD5Q0yx8x-VJYXJ15okz_y3dTVQGhaUNfNNT2y8cT0XjlqPAGiGsJeZkgrzoDDLp4LCMtv4Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از عاصم منیر، فرمانده ارتش پاکستان که امروز جمعه یکم خرداد۱۴۰۵ وارد تهران شد و مورد استقبال اسکندر مومنی وزیر کشور قرار گرفت. خبرگزاری آسوشیتدپرس پاکستان نیز به نقل از منابع امنیتی اعلام کرده‌اند که عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/75626" target="_blank">📅 22:26 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjRLLenF79QDd3JmthplPLpYKetFMk0OOESh6quhGZ_s99D-mXQGLZ1TXvZsUa-xoTdkJj_60GQXWklUDf1cOGxWTMYVtqkj6hvwX35e3MaZhtY_nLBveWxLyyLJHgigR6UW0OhzgRgEzEXlJRFoBGaclFAftZkBXqrOuXKBUWGt-CvZhoM8naZJmeTbkmwbapbfwrrhUAJad1H4rL-B7k7oEyS8J75fhIWbssh11tcZkq9PDXRT-eXin6exNnAcegVBvJApILVWCok-5ZaKa16GWJ13Bp8I94DriY841EBvnFiBG9Z7ycsihxAv552_eRPi_ugDr8VkuElkQIwxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فاکس نیوز»: تولسی گابارد از پست خود به عنوان مدیر اطلاعات ملی آمریکا استعفا کرد.
AlArabiya_Fa
پست ترامپ، ترجمه ماشین:
متأسفانه تولسی گبرد، پس از آنکه عملکردی بسیار خوب داشت، روز ۳۰ ژوئن دولت را ترک خواهد کرد. همسر فوق‌العاده او، آبراهام، به‌تازگی به نوعی نادر از سرطان استخوان مبتلا شده و او، به‌درستی، می‌خواهد در کنار همسرش باشد و در حالی که این نبرد دشوار را با هم پشت سر می‌گذارند، به بازگشت او به سلامتی کمک کند. تردیدی ندارم که او به‌زودی بهتر از همیشه خواهد شد.
تولسی کار فوق‌العاده‌ای انجام داده و دلمان برای او تنگ خواهد شد. معاون اصلی و بسیار محترم او در دفتر مدیر اطلاعات ملی، آرون لوکاس، به‌عنوان سرپرست مدیر اطلاعات ملی خدمت خواهد کرد.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
از سوی دیگر رویترز به نقل از یک منبع آگاه از موضوع، نوشته که او ادعا کرده کاخ سفید خانم گابارد را برای کناره‌گیری «تحت فشار» قرار داده بود.
پیشتر اختلاف دیدگاه‌هایی بین رئیس‌جمهور ایالات متحده و مدیر امنیت ملی‌اش، بخصوص در قبال ایران بروز کرده بود. دونالد ترامپ در فروردین‌ماه هم اشاره کرده بود که از نظر او، تولسی گابارد در قبال برچیده‌شدن بلندپروازی‌های هسته‌ای ایران، «موضع نرم‌تری» دارد.
خانم گابارد بیش از یک سال پیش، پنجم فروردین‌ماه ۱۴۰۴ به کنگره گفته بود که ایران در حال ساخت سلاح هسته‌ای نیست.
مدیر اطلاعات ملی آمریکا که برای ارائۀ گزارش سالانۀ نهادهای اطلاعاتی ایالات متحده به همراه رئیس سی‌آی‌ای و مدیر اف‌بی‌آی در جلسه استماع سنا حاضر شده بود، تأکید کرد که بر اساس ارزیابی نهادهای اطلاعاتی، علی خامنه‌ای رهبر وقت جمهوری اسلامی، درباره تعلیق برنامهٔ تسلیحات هسته‌ای ایران، که در سال ۱۳۸۲ فرمان آن‌را صادر کرده بود، تجدیدنظر نکرده است.
با این حال خانم گابارد بعد از مدتی، موضع‌گیری خود در این زمینه را تغییر داد.
تولسی گابارد که مسیر سیاسی پرفراز و نشیبی داشته، پیش از پیوستن به حزب جمهوری‌خواه و ورود به دولت دوم دونالد ترامپ، عضو حزب دموکرات و نمایندۀ هاوایی در مجلس نمایندگان بود.
او هفت سال پیش، زمانی که خود را برای رقابت به‌عنوان نامزد حزب دموکرات در انتخابات رباست جمهوری آماده می‌کرد، گفت که در صورت پیروزی در این انتخابات، ایالات متحده را به توافق هسته‌ای با ایران باز خواهد گرداند.
خانم گابارد در آن زمان در گفت‌وگو با شبکه تلویزیونی فاکس‌نیوز هشدار داده بود که ایالات متحده در آستانه جنگ با ایران قرار دارد.
تولسی گابارد نخستین و تنها مقام ارشد امنیتی یا نظامی دولت دونالد ترامپ نیست که کناره‌گیری کرده یا وادار به کناره‌گیری شده است.
در آخرین روزهای سال ۱۴۰۴، جوزف کنت مدیر وقت مرکز ضد تروریسم آژانس امنیت ملی آمریکا، که مستقیماً از سوی دونالد ترامپ منصوب شده بود و زیر نظر تولسی گابارد انجام وظیفه می‌کرد، در مخالفت آشکار با جنگ ایران، کناره‌گیری کرد.
@
VahidHeadline
خبر یک ماه و نیم پیش:
ترامپ قصد داشت گابارد را اخراج کند
به گزارش وب‌سایت آکسیوس، دونالد ترامپ تا آستانه اخراج تولسی گابارد، مدیر اطلاعات ملی آمریکا، پیش رفته بود، اما مداخله لحظه آخری راجر استون، مشاور قدیمی و نزدیک او، مانع از این اتفاق شد.
دلیل خشم ترامپ به شهادت اخیر گابارد در کنگره بازمی‌گردد؛ جایی که او برخلاف انتظار، از جنگ با ایران حمایت تمام‌عیار نکرد.
طبق گفته منابع آگاه، ترامپ از اینکه گابارد در اظهاراتش اعلام کرده بود برنامه هسته‌ای ایران پیش از آغاز جنگ «منهدم» شده بود (موضعی که توجیهات ترامپ برای حمله را تضعیف می‌کرد)، به شدت ناراضی بود.
همچنین استعفای اعتراضی جو کنت، دستیار گابارد که جنگ را غیرضروری خوانده بود، بر آتش خشم ترامپ افزود.
در حالی که ترامپ در حال نظرسنجی از مشاورانش برای جایگزینی گابارد بود و وفاداری او را زیر سؤال می‌برد، راجر استون در تماسی تلفنی از او دفاع کرد. یک منبع نزدیک به آکسیوس گفت: «راجر معامله را جوش داد و تولسی را نجات داد.»
استون نیز بعدا در شبکه اجتماعی ایکس تایید کرد: «خوشبختانه به موقع اقدام کردم.» با این میانجی‌گری، گبرد فعلا در سمت خود ابقا شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75625" target="_blank">📅 21:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gPMyymCZOYlsN_-oQICvgEjW2HJTb8l2V6nvAqvfCMqyvgUsTJa-qQAh4_savEUePfxUIjKg4P_YoW5L0OCWzTYrNiuYcxo1O7aHs3zzZHOWdFklc6Bd3wwZnqfnDHeR8l93hVo9HCX15a12hod4MZC5mgAE2aGEs_pCvE6FRcN9XNQ5MuEAQZwWIjYvMQOXND-qOflvzvLVe5I7Z8PRYHK6izLgIIExi65mO3O0JDYxqTvZpX1QEvu3UxANUxkDIc3OWj31t2YF0ZGW1pWyQ86qbkNZh_49TE2WoyKaCC_CSFXGQ9UgyentXW49naXZnkfqmpV0JbkhGrPwZ8kEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست
ترامپ درباره شرکت نکردن در مراسم ازدواج پسرش
ترجمه ماشین:
با اینکه بسیار دوست داشتم کنار پسرم، دان جونیور، و جدیدترین عضو خانواده ترامپ، همسر آینده‌اش بتینا باشم، شرایط مربوط به دولت و عشق من به ایالات متحده آمریکا اجازه چنین کاری را به من نمی‌دهد.
احساس می‌کنم مهم است که در این دوره مهم زمانی، در واشینگتن دی‌سی و در کاخ سفید بمانم.
به دان و بتینا تبریک می‌گویم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز:
ترامپ با اشاره به مشغله‌های شدید خود گفت: «به پسرم گفتم الآن زمان‌بندی خوبی برای من نیست؛ موضوعی به نام ایران و مسائل دیگر را در دست دارم. این از آن مواردی است که اگر در عروسی شرکت کنم، توسط رسانه‌های اخبار جعلی سلاخی می‌شوم و اگر شرکت نکنم هم باز من را می‌کشند!»
@
VahidOOnLine
رسانه‌های امریکایی نوشته‌اند که دونالد ترامپ جونیور، ۴۸ ساله، قرار است در پایان هفته جاری با بتینا اندرسون، مدل و چهره اجتماعی ۳۹ ساله در یک جزیره خصوصی در باهاما ازدواج کند.
بر اساس گزارش‌ها، این زوج در ابتدا به برگزاری مراسم عروسی در کاخ سفید فکر کرده بودند، اما بعداً تصمیم گرفتند مراسم کوچک‌تری برگزار کنند. دلیل این تغییر، نگرانی از واکنش عمومی به برگزاری یک مراسم پرزرق‌وبرق در زمانی خوانده شده که امریکا با تنش‌های مربوط به ایران روبه‌رو است.
afintl
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 216K · <a href="https://t.me/VahidOnline/75624" target="_blank">📅 20:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czFJI6l26DIoyCQJYBj1xlDSKIGotOs19Fb-bOz7xfPVFHATPxFRt6-R5L9DsaqVi5ZOVx-GKF5Q7rnTFkY2uDDwCv-0dWFq9Y77XjqWwYqCQSRmVmBOvTCgcv1k2JRYUAk3X3aEFSM_891V1yLu1noyOy_kmDYQuN5eQ2_Zhs7hTdKBJ41DKiSWcpKa1b41q06yX3L29vAoOckJ8CektwgzFNJGXMdvsuMmZbJgoWm4pzAIp4K9yecAV6r-XY4Dq59cRDCkWX7Wbs2TxNv5Xbv2S_m4lNNJfueslof7eC-Lss6LkmZI7X0u8cYuFh6WHNgUGFs1fDuced_Q1l9UQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7UCgS3NtVigRrnIAkFwcLfjjPEB-Qqojcj9khuYDni9s1isVl1beeuKE_tZ6AWjThftGjvxajJxnc__DrcTCAvbp_AvQuO9XUh8OhqQGk5w38K7LF3xwbzVijE1_RUX-_v6vSEJMHGaseh7PNkGg5zrfeno61bQGa3H1owZnjdirYitLhPQbkiFQnU_mrrVO3PVxXJ1haTdvDxMqm4lxDIKbUx6dit5I4wBaohyFNv7GqSVnDVoIVlrSx816DcOsoiEgRDnVyOc_ru48p4wTwIope4o4hgpj2pQiZSFmx0eXOWIMt916NlZxqIl_T5BYMTSnfGAcgtJugLLD-xnXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7EZIYjcZn2aUijAHFuplFQGXiZ_UCKUmdV_wWg2HUSzswUG1QT5EsF-M4NT2vTSkhZMcAU5-sXgaPjM2QxAPe3Frijb-1bjY1GJ4E-1rJKyhOyHBLtVZUEbLODUnwqf3WwTn5EYIC_meyKfCSsz9Dwr40RfrQGG-G2pEnboeqCl26sT5X0e-pzmxLsosRI358k6EJHMnwzMqh44qrTdUWyQSwGOabnkiNnzWEMLVvDNumc5x0_brzOyMDFWIMSI7hsu3l2zF-NnCXHr7DOC95863drAkkghn5ceMH8ko2vrC3vLytfNqkxsI_cSPPq5Zzp3YMrucejXcqdP3LPyJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بنیاد عبدالرحمن برومند تا کنون ۶۵۵ مورد اعدام را در سال ۲۰۲۶  ثبت کرده است، که ۳۴ مورد که از آغاز ماه می تاکنون اجرا شده است.. آمار واقعی احتمالاً بسیار بیشتر از این رقم است. جمهوری اسلامی در حالی این اعدام‌ها را پشت درهای بسته اجرا می‌کند که  ۸۳ روزه است که اینترنت کشور قطع شده است. حاکمیت با قطع ارتباط جامعه از ۹ اسفند ۱۴۰۴  صدای زندانیان، خانواده‌ها و شاهدان عینی را به شدت سرکوب کرده و نظارت مستقل بر وضعیت حقوق بشر را به‌طور خاص دشوار ساخته است.
🔸
از آنجا که دستگاه قضایی همواره تنها بخش کوچکی از احکام مرگ خود را به‌طور رسمی اعلام می‌کند، قطع اینترنت داده‌های فعلی را به شدت محدود به منابع دولتی ایران کرده است. بنابراین کاهش در آمارهای ثبت‌شده، تنها نشان‌دهنده خفقان اطلاعاتی است، نه کاهش کشتار.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/75621" target="_blank">📅 18:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SgF_H9QVigR0IaGywgy1VJ6zKScxjSGfSOPDV0-E8IN7cANfWGDkzc6zVzK8j2A4xr5yaKYvA_HjewPvhCBoGdwUEj7EB2UBmSSzuYgzy1-s6OF-K3Uo_Cx_DpHMTDCgNTU07xx9j-O364RfPLsXM5UImyTgNLT_4xbyhdKTBIoGfV8xzmBJra0ioPaB3ffA47RFT75Qg8ItAVGGmfrxJhXHq3brfnaR8xSD34ci5jcOju5n7nN-roU1FdJWLrAgFc0hlvHf9PSD3zGysGxUq8M2S6uZmWeyFSvpigj5kZf88vSXlQb4xLUTzUPAS-kAH8Mwu25eRzGqJJ53eLqh2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دختر حسین ناصری:
MNaseri23595
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75620" target="_blank">📅 18:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1vFbDB2V4zDnDZBUyM8Xrkz-Q6dxaRR8OoHBytRanuc9iPK77Ht6Ho-T-UlLc43V0BWCeUYg6SKuMsRp1gDuzvoYOMIJV_mF30Fbdg0x8_VjmrfjyOM_20Z3ikby2xS6Cz-xUm8Rd0HYGsg8glrmnt78HWi0IMsw2LtJuOHXRjIB-7crozDSCpYdwFpmmbLMs9XWQ9NxucK6owrI-KL1eD49mc2J4eN-r9HNQAdGt9CDnxFXLcnZIhA9jk-HbEkK_sq8Z4zex_ExY2gCFBSIE-Wigvywbrrs6UqDTibXGzM6H2obQoqk8s3w7KMHZy-RzXmrF8olqx-LtfyhiiEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های دولتی پاکستان، فیلد مارشال عاصم منیر،‌ فرمانده ارتش این کشور راهی تهران شده است.
خبرگزاری اسوشیتد پرس پاکستان به نقل از منابع امنیتی گزارش داده است که فیلد مارشال عاصم منیر در طول این سفر رسمی، درباره «مذاکرات جاری ایران و آمریکا و صلح و ثبات منطقه‌ و منافع دوجانبه دیگر» با مقام‌های ایران گفت‌و‌گو خواهد کرد.
فرمانده ارتش پاکستان چهل روز پیش هم در تهران بود و با محمدباقر قالیباف و اعضای تیم مذاکره‌ ایران و آمریکا دیدار و گفت‌وگو کرده بود.
این در حالی است که وزیر کشور پاکستان هم برای دومین بار طی هفته اخیر به تهران رفته و در حال گفت‌وگو با مقامات ایرانی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75619" target="_blank">📅 17:55 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75614">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JKiVdHkSpTygnidWSkjjLBnMGTAvIUS-OIkDYsWz9q4SP6TT2lPyvzyuvvIWjATY9-6DcMmIT4NJrygGhstMB0Pyb9zvY0gjb3BTi_CP3WPCQ4SkQBWG5LUG1CXNI0z5_B81g6t_QeKSKkWaAsZ5GlO5B4fbbHMX3Y2ofnreNvOOt7AsR6495LctzK5I7j9CJakf-JcZb5o1iSbtkHBAR3Kc-Z4YUWniS33Xj6wdF0_xPfbm3uP9lbtEtyX_Lyk02SkvDXI2ARKWDuF8uYucjmp-eVp_3rQJrIE1-I33748xI9j_XwQoSk-v6qiCNfqA4Rqvar_0cQHOEf9kFa3qLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hYSIBUxHXQtmKXTdULhmsO-lZngxwv4iNtLfe0WT8pRy0qzaVXHkVBmKwlmlc6FZosttdXhvNz8FXHYKxC6DlBGugHbHrPAzPAlRU1T4lT59NLIajl2c1fn7l3dUYbDdLx65g4kA4C_CBLkQmY2sidUkO20lq3o2c2c5t9BbHDfWV-0bbIWcEVWBZCIuQYxCAsVPt1J55Ijl3nItvHblvo-G3FPiNpqgHxyx3eg6JjHGcgaB8j0ZzUM-pgy_SQznwGrboA5wFikPMdGH48X1WS9871-OuDBssqw7Ph1VdPaCnr7yE7f-Cvvr74OzAh5SZimzyYZVlx4QHzOruSqChA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=Ro1Ogkz4tv6wwd3oa0KnhHy1jzRNqdDVjg-Y4o1PEYc5FU9MbMaBOnukCYL3egNWP91SRQYlcT-36OBnodChDg2AFAcf4Nyex6kqoYVVm7AOruLvv-dZgrnA9cCXaiiz_N9d9nSy60_zWO9UGzoWQRQ1NiA06GuJrOiRJFfjUxQbUi8k147WISkAeZ146RR7a0TxSgSbFtwn2CZ3rucgF5VcHGFzsLjQ33eNNobso_rkJ-J1et2H9RXvPSxwfWeFgs_0au3r8JMZU3tCVdkgCFwewSmUTDJgn7goMv2HcftMKSerc2EHgdWZydnm47dhsA7Mvl773rfJ252HjLFz1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9fabcfc83.mp4?token=Ro1Ogkz4tv6wwd3oa0KnhHy1jzRNqdDVjg-Y4o1PEYc5FU9MbMaBOnukCYL3egNWP91SRQYlcT-36OBnodChDg2AFAcf4Nyex6kqoYVVm7AOruLvv-dZgrnA9cCXaiiz_N9d9nSy60_zWO9UGzoWQRQ1NiA06GuJrOiRJFfjUxQbUi8k147WISkAeZ146RR7a0TxSgSbFtwn2CZ3rucgF5VcHGFzsLjQ33eNNobso_rkJ-J1et2H9RXvPSxwfWeFgs_0au3r8JMZU3tCVdkgCFwewSmUTDJgn7goMv2HcftMKSerc2EHgdWZydnm47dhsA7Mvl773rfJ252HjLFz1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، در حاشیه نشست ناتو درباره مذاکرات جاری با جمهوری اسلامی گفت که واشینگتن در انتظار نتایج گفت‌وگوهای در حال انجام است؛ گفت‌وگوهایی که به گفته او نشانه‌هایی از پیشرفت داشته‌اند.
او افزود: «ما در انتظار نتایج این گفت‌وگوها هستیم که نشانه‌هایی از پیشرفت دارد. نمی‌خواهم در این باره اغراق کنم؛ تحرک محدودی صورت گرفته و این مثبت است، اما اصول اساسی تغییری نکرده است.»
وزیر خارجه آمریکا تاکید کرد که حکومت ایران هرگز نباید به سلاح هسته‌ای دست یابد و گفت: «برای تحقق این هدف، باید به مسئله غنی‌سازی و نیز موضوع اورانیوم با غنای بالا رسیدگی کنیم و افزون بر آن، موضوع تنگه هرمز را نیز مد نظر قرار دهیم.»
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، جمعه یکم خرداد در حاشیه نشست ناتو گفت جمهوری اسلامی در پی ایجاد نظامی اختصاصی برای اخذ عوارض در یک آبراه بین‌المللی است و تلاش می‌کند عمان را نیز به پیوستن به این سازوکار متقاعد کند. روبیو تاکید کرد که این اقدام «غیرقابل قبول» است.
او افزود: «هیچ کشوری در جهان نباید چنین چیزی را بپذیرد. من کشوری را نمی‌شناسم که جز ایران از آن حمایت کند.»
روبیو با اشاره به تحرکات دیپلماتیک در سازمان ملل متحد گفت قطعنامه‌ای با پیشنهاد بحرین در شورای امنیت مطرح شده که آمریکا در آن نقش فعالی داشته و به گفته او، بیشترین تعداد هم‌پیشنهاددهنده را در تاریخ شورای امنیت دارد. او هشدار داد چند کشور در حال بررسی وتوی این قطعنامه هستند و افزود: «این مایه تاسف خواهد بود.»
وزیر خارجه آمریکا تاکید کرد واشینگتن برای دستیابی به اجماع جهانی جهت جلوگیری از اجرای چنین طرحی تلاش می‌کند و گفت: «باید دید آیا سازمان ملل همچنان کارآمد است یا نه. ما می‌کوشیم از این مسیر به نتیجه برسیم.»
او تصریح کرد اگر اخذ عوارض در تنگه هرمز اجرایی شود، ممکن است در دیگر آبراه‌های مهم جهان نیز تکرار شود و افزود: «این قابل قبول نیست و نمی‌تواند رخ دهد.»
روبیو با اشاره به اهمیت تنگه هرمز گفت این آبراه برای کشورهای حاضر در نشست و نیز برای دیگر کشورها، به‌ویژه در منطقه هند-آرام، حیاتی است.
او در پایان با ابراز امیدواری نسبت به نتایج نشست ناتو گفت این دیدار زمینه را برای نشست رهبران در حدود شش هفته آینده فراهم خواهد کرد و افزود که تا آن زمان کارهای زیادی پیش رو است.
@
VahidOOnLine
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست ناتو در سوئد درباره مذاکرات با تهران گفت: «همه ما دوست داریم توافقی با ایران شکل بگیرد که در آن تنگه‌ها باز باشند و ایران از جاه‌طلبی‌های هسته‌ای خود دست بردارد.»
او افزود: «این چیزی است که همه ما امیدواریم و همچنان برایش تلاش خواهیم کرد و همین حالا هم که با شما صحبت می‌کنم، کار و مذاکرات در این زمینه ادامه دارد.»
وزیر خارجه آمریکا با اشاره به این که باید یک «برنامه جایگزین» هم وجود داشته باشد، گفت که برنامه جایگزین در صورتی باید عملی شود که حکومت ایران از باز کردن تنگه‌ هرمز خودداری کند.
او گفت: «پس باید از الان درباره‌اش فکر کنیم. من امروز این موضوع را مطرح کردم. واکنش‌های تاییدآمیز زیادی دیدم. اما هنوز چیزی برای اعلام رسمی درباره اقدام مشخصی که در حال انجام باشد نداریم.»
وزیر خارجه آمریکا درباره برنامه جایگزین در صورت امتناع جمهوری اسلامی از بازگشایی تنگه هرمز افزود: «نمی‌دانم لزوما این می‌تواند ماموریت ناتو باشد یا نه، اما قطعا کشور‌های عضو ناتو می‌توانند در آن مشارکت کنند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/75614" target="_blank">📅 17:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NvKQSifWxJLDHo81gWPaqgvEPuRruIhvLm5WgQuElA5QrMoFx4cZVhG5ryqhEtVU849s6o8DibyjNrLcMkorBT3VGrg6N_LASN5gNnUkNmxqi_hVxLRPQ2lrNKhDi3_ep9HLPIDGd2t9B2j3kGJI5oa5ogBdqmzCjPOeeVl29XBwk_QqFaTzATNk9z9wT7r_5uHC-X7iNvftHrBLQz9ZBXT3c8ldaEKSVS9ZtbhMC8arP_-ecqSZdASm0gT992AqHWtP6WgUrjG4xznGxouHnpQvn6LB3DyDe7xBqM6RdPhxvpP5S8Xqv_O-24ha4QGoQhYekPXgE5w8on5nVLqsZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzDMeWBiiP7bArTZ55L9zgmIACUmk81Brh2aCtEJ2jDjsS-nEJkIjFLFzzrwKk-K5HnfTYXiO4B4JtgEtMeToSqhepm-wgJInl39HOBlmRnzLjRrPXJqLg0zYCoLIkL_Xv85vYAvdBig6EDCCKguAQ2a0QILJAYkkeHiuDlsGYFh8zhZbBNUFE-6O5EhdxBLs99S_HMJ-qU6QrC4ozW-gTxfMAKdmgUcSKXaI_3iA1npeXOJhc9ExN2vkLaHeKFuAW3893_kNhaVJy86DilQmC0bSN5XJylh-nn589k7JDAToMjlKiyJlXUp7eqXjCpUMWiGldBuzv1OON977ImORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cLzUER14xSqM-JDFW4Zw9sriN3of0B8F81oJ-WIXp4C4clCEo48TCf2sQ1yRF6MIbjBo2IrGIa_nZ_zgh0IZhudLcFSw_6xXfOQD9C0gQwdixVMQHQiavkjPqxpyAads9_EiuowFkmq94QSGvgawgQxyugi3wpFPir_UD7iZGvw2Z1rF2L2JYV__J-ygaeyOxjs1N2ufK9-9qJqCkOp1UeNEBgZtjdnvr8QC94_HZ2f7vLI-Es2zj6ILroAPqJ6uQR6crEmA_mQp6YrM9aWYrkXW4RbdHsu2uvLRH70zfTR0STQZ1wHo4iqgVizgsRU6y0uDylgQD02lFAgfxmHTfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اطلاعیه منوتو درباره پایان پخش برنامه‌ها
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75611" target="_blank">📅 17:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZXhqW3ecI7jGcrTOItn0ONXleb3meQQsokw8TUm1UCe7C951vIgN7M_LTIwzFkg-NULZha4DQ6leM93ijDaZXwJpABtqYXaEEkHv6AxG70B6Buop9M_id4jGQX0wjzxtncsmPJxeEJU6IFMMy-pLVbQq_dFKkPx9E36KdEbhf3PeHVfLpW0xg71FZRsKcTeFV4Cpc4SPFecNwn5YobQNGmn_RCXWrV55tyt41MI-yR8pgFTCX9XtciI0EJPKFGbYeYPx94V2G9M0-y5FjIblSAitq3Ug9Rd_mxEJpn9oZowLFqNcnCh0wI0sshOJOXI0sPJ1eB5APo4KXptToYUm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IxKTaWCK1KS_kCzK2i5klk8_0eSKcWjGRaaYAoe7TX4DisyruCbr5KC_Jg7gghYMOQ4M7Xe-nQNdm97GuWyowpKElnBo_lEAccfLw3pRcjblds0muPhqPYDJpfLNn6gnkCX2ARpNeBFPS2bU3K7A-kwRUZV_pBWsmTsdIYpQHJ3im_0-khR39yIur0JPCky-xnMbBMI0Pc4SABGJufDokz6hmJpNMh4A-6JOTe4UKAwSejUh0e4mMqFAC4jEJ87rl7wBzrt7ywI3B3s6BIm0gSmjHLW5aQLOnijMwYMEUjQVvByoWkPjMDpZDs09YmfYmByO-j-wu8El6kzodVap0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/spQIb1P4Mnf3I0HHct_bmzRXhQY1_2AxtySiBGrCvelxxE60iIiqFlbpTuRcxP7acf6WCHcTvCdmiQ4-M5d-4x0bGRPl-oSaISj_lin85Sh5OgoQgI0gAt0iXGW52x-4U-UigJI_slJRPclppPWQANZppM0tY93MTEo30gVbyrtir76aLq58N1Op8lEnZ_47di8LymPju9QH7GxeZVe1eUshJTi4UvBc66kmMxTRP78OX-IRNppp-pwJZ4bF3HxNPRKOZlGRmGAzhb-bhsuKoH6aTKFEb_Cfsway7ZyfaHentdqQ8RFzUEBxJC907Q7XlSI4TbFfMuAad7Klj1gjCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=VFePpDl3pAbS1aHEphUcyZaCI76qHJ4lxeKzAG6b4DpswX5wBtXKb67dxcBBZu4Ro_xSWQRIqqoxntQPSk26B7ayOqhi8606mmT1SuF8j-xcsShDOkJUNA6GUWqCyVhBmzzZerqmBidxxmMABmc6eaT91J9MCWuRaBKkhmoFq9YgCT_EE5a32qj0t_kBAVS8N5Li32BfdxntO2CUPfCzhHwL-Sd-tNa84-l-Pmb4_GCGEf5VINyS1Ss7wyj4p-p8C-kZoh3Q-sEihsyeYpMYEqa9VzkMIVX0Gl97nhYjlknqggKDtXIoRsfUEMo6EXUxU_Kn8d1HQ_dUE8kANQEW3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/abdcc0b736.mp4?token=VFePpDl3pAbS1aHEphUcyZaCI76qHJ4lxeKzAG6b4DpswX5wBtXKb67dxcBBZu4Ro_xSWQRIqqoxntQPSk26B7ayOqhi8606mmT1SuF8j-xcsShDOkJUNA6GUWqCyVhBmzzZerqmBidxxmMABmc6eaT91J9MCWuRaBKkhmoFq9YgCT_EE5a32qj0t_kBAVS8N5Li32BfdxntO2CUPfCzhHwL-Sd-tNa84-l-Pmb4_GCGEf5VINyS1Ss7wyj4p-p8C-kZoh3Q-sEihsyeYpMYEqa9VzkMIVX0Gl97nhYjlknqggKDtXIoRsfUEMo6EXUxU_Kn8d1HQ_dUE8kANQEW3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم مستند «تمرین‌هایی برای یک انقلاب»، ساخته پگاه آهنگرانی جایزه «چشم طلایی» هفتاد و نهمین جشنواره فیلم کن را از آن خود کرد.
«لوئی دور» یا چشم طلایی، مهم‌ترین جایزه بخش مستند جشنواره فیلم کن است.
پگاه آهنگرانی جایزه‌اش را به مردم ایران تقدیم کرد و گفت: «(مردم ایران) با وجود تمام سرکوب‌هایی که در طول این سال‌ها تحمل کرده‌اند، هرگز از تلاش برای حقوقشان، آزادی‌شان و آرزوهایشان دست نکشیده‌‌اند و مطمئنم که آنها هرگز تسلیم نخواهند شد. مطمئنم و یک آرزو دارم که می‌خواهم اینجا بگویم: این‌که روزی دختر کوچکم لی‌لی و همه بچه‌های ایران در آینده‌ای نزدیک در ایرانی آزاد و دموکراتیک زندگی کنند.»
به گفته خانم آهنگرانی او با استفاده از آرشیوهای شخصی، ویدئوهای خانگی، تصاویر اعتراضات خیابانی، روزنامه‌ها و صداهای ضبط‌ شده، بیش از ۴۰ سال از تاریخ ایران را بازخوانی ‌کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/75607" target="_blank">📅 17:38 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75606">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK7tKvA8gH8kV2HgN4RVVQ_t59w7L0BffFgdV7K7cqIGHEgtGCgo8VsccQ3uz3ecMpsKxc7NYzPssVb9vA2JeKX8K3mROihXHOoRreun9RUMZVh3TvrBb9gqRJ6uRwUMvQXyu92Qr2AU7Zw2mKfVjkzg6a4KIXrf_H4LzsBXJ6bgQhmCxf5HyNyu6eqEuP-Ze3HiFEchnmBsMvPyWhdoKQR0QKUicjOmN9a-kYfK8biYOA4xAvEFR0zOwYub5FMg0w3AC8sDzCVjYR5C2wZjtttXtEpUMcvLap-xPmLcArCN8CNSHvfA7m_T0RywMyEW8J7S4UaCLCcqr-NKebXOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشورهای عرب حوزه خلیج فارس از جامعه جهانی خواستند که طرح جمهوری اسلامی برای مدیریت تنگه هرمز را رد کنند.
به گزارش بلومبرگ، در میانه مذاکرات دیپلماتیک سازمان بین‌المللی دریانوردی با ایران و عمان پیرامون بازگرداندن آزادی تردد و امنیت کامل کشتیرانی در این آبراه راهبردی، کشورهای عرب حوزه خلیج فارس طی نامه‌های به اعضای این نهاد زیرمجموعه سازمان ملل، نسبت به طرح جمهوری اسلامی موسوم به «نهاد مدیریت آبراه خلیج فارس» هشدار دادند.
پنج کشور عربستان، امارات، بحرین، کویت و قطر در نامه خود گفته‌اند که به رسمیت شناختن مسیر پیشنهادی جمهوری اسلامی می‌تواند یک «سابقه خطرناک» ایجاد کند.
سفیر ایران در فرانسه روز گذشته تأیید کرد که تهران با عمان درباره اعمال دائمی عوارض عبور در حال مذاکره است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/75606" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75605">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp-1QTmlzssU7tnlWcgixLAHz9LgpKcwAbiK_mdRFayyJLck1JZOeZ9AzqgXqaGDinp2N8TiHoKOC3ycCIOS6paK9xSWjmzLJcBNbFpG8n4eliLY9vfVVmF90aAGRGIkLBvN_n1jrAZfv4jgHkfRx7lPcQMYARBrZoPDR5FV1a4xAUiflJbDiywHSEFsJOchA3hkKSgcf_06levC_H6N80X3WG8qnLsRc7FcWIAn8YFqizfVp0F6_yIvjPy4IVFdWtRuo56oB0TZKA22Oj_tQviruxJqY4EjEVzS11kHIYH-Od42fF8LJs2jYGlNx1kFua_d6BVQN05DBTIl3cR_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاد بین‌المللی ناظر بر وضعیت اینترنت، نت‌بلاکس، صبح جمعه اول خرداد اعلام کرد قطع گسترده اینترنت در ایران وارد هشتاد‌وچهارمین روز خود شده و بیش از هزار و ۹۹۲ ساعت است که دسترسی کاربران در ایران به شبکه‌های بین‌المللی همچنان قطع است.
این نهاد ناظر بر اینترنت نوشت با ادامه این وضعیت، شکاف‌های اجتماعی و اقتصادی عمیق‌تر می‌شود و هر ساعت از قطع اینترنت، ارتباط با جهان خارج را بیش از پیش به جایگاه، همراهی با حکومت و برخورداری از امتیاز وابسته می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75605" target="_blank">📅 17:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75604">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ksy5sonvjKjcyKLwIkpSRyTh17fu2AqnbipisUsQ6zClHn_GSp_yKJQDiNSBRaSYPH7FRLbAx8bu_YCIyqzMctLKTzucXJ1hcknGxAgC2uz5dtgvjhf5J0x1EZQ-jGlzBIhJtRDIJp5JhIBp2aglh11HkBocg16DwelWCQQ9dXdb-Kw03gBf3j4VC7qkywTEgFjyJ1uBj9kYQpbgA3z9Tmm6X8spyKPJecMpeXwCDuegdWJkVUZG73XejGOIYJblVZL3nk6h_Ip3TaacVfN43teOUkdGcj-PKL0c5wtah9zXEZwMWxVg-Za2jG9_YtTyXjjkdPaV8Tm0WqwIFCrUcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوان عالی کشور احکام اعدام محمدرضا مجیدی‌اصل و همسرش بیتا همتی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، را نقض کرد.
هرانا خبر داد که پرونده این دو متهم برای رسیدگی مجدد به شعبه هم‌عرض ارجاع شده است.
این دو پیش‌تر به همراه بهروز زمانی‌نژاد و کوروش زمانی‌نژاد با حکم صادرشده از سوی قاضی ایمان افشاری، رئیس شعبه ۲۶ دادگاه انقلاب تهران، از بابت اتهام «اقدام عملیاتی برای دولت متخاصم ایالات متحده و گروه‌های متخاصم» به اعدام محکوم شده بودند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75604" target="_blank">📅 17:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75603">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=C94Q7-dU-L5JEpkzMS1fkcMTUhCWkO4XedPMK7xf6sTijxy0l7_A5qHc31goMzrFDvgfn3AmaeQMnzS4VwCpdXHpP6gRQOaV-reuP7sH0yWIIZ2c42D0tjaEzzch1K8y7tORWIkgEfmxIzhLJ_c2tCXYJx1lbggUGINq7LNz9iRCljkFFksGQQhoPfX1AscQ0xrK08MGXtAZpWIJhnFONsoF6nvyh-TTLBuaO1lRjSd6EgD-aC-oFiudiEcd33y7SwgXPs0K-sagr3fOBn_pI4-XgHBom7FVsFZnvUN6s24rhicjQDB9GtlcAplr99yN5SlbRm5lpnqwXQvJRXQrSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23e07c2844.mp4?token=C94Q7-dU-L5JEpkzMS1fkcMTUhCWkO4XedPMK7xf6sTijxy0l7_A5qHc31goMzrFDvgfn3AmaeQMnzS4VwCpdXHpP6gRQOaV-reuP7sH0yWIIZ2c42D0tjaEzzch1K8y7tORWIkgEfmxIzhLJ_c2tCXYJx1lbggUGINq7LNz9iRCljkFFksGQQhoPfX1AscQ0xrK08MGXtAZpWIJhnFONsoF6nvyh-TTLBuaO1lRjSd6EgD-aC-oFiudiEcd33y7SwgXPs0K-sagr3fOBn_pI4-XgHBom7FVsFZnvUN6s24rhicjQDB9GtlcAplr99yN5SlbRm5lpnqwXQvJRXQrSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویرسازی از مجتبی خامنه‌ای
وزارت جنگ آمریکا روز پنجشنبه ۳۱ اردیبهشت، با انتشار
ویدیویی
بر ضرورت افزایش بودجه دفاعی کشور تاکید کرد.
در این ویدیو که ترکیبی از صحنه‌های واقعی، گفته‌های پیت هگست، وزیر جنگ آمریکا و تصاویر کارتونی است، تصویری از مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی نیز در کنار یک سامانه موشکی دیده می‌آشود در حالی که یک پایش قطع شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75603" target="_blank">📅 02:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75602">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s42-lPCtfsyE5Uk27JvsdC4--z4GnuJuVCOxYseJQUwjAUNFa9--tLMhnGJQtis4DsTa-h2J-eW9iePCPbKy6KRwTstDOoULgMTSNpFspC7VEo-2OfqwElekLQuus21k-3aCfphn5z335TFXZzGpDtm7NpBgp4xGkOxcbw_CR-m0y5qoYEdquHl6vXOxWOmRoEOTTpIC7MBG639xTEwOAE36NsnYQHhsGqPia8jaqPWt-kX85vZ4ZjD-xkNxGS9np8ML9WghQvtWRq-oc8gv8IsrWsvPCmAOkzlmNpUqmprr6oGbLwZDnK75ZevMCQLikn5jD453BMx-RXHXJdxNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
در تازه‌ترین تحولات بحران ایران و مذاکرات جاری، یک منبع بلندپایه به «العربیه» گفت که فرمانده ارتش پاکستان امشب راهی تهران نخواهد شد؛ این در حالی است که پیش‌تر گزارش‌هایی درباره احتمال سفر او در چارچوب میانجی‌گری‌های منطقه‌ای منتشر شده بود.
قرار بود عاصم منیر، رئیس ستاد ارتش پاکستان، امروز پنج‌شنبه در سفری رسمی وارد تهران شود؛ هم‌زمان با انتظارها برای تحویل پاسخ ایران به تازه‌ترین پیشنهاد آمریکا برای توقف جنگ و دستیابی به توافق میان ایران و ایالات متحده.
alarabiya
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75602" target="_blank">📅 23:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=UPwCGcdWBRbPL0BMj0TbsNDlVOmG2HITMOKpiGZUmdeJ2IdH8YMz2MlVFa4Fn-QncH2VosKSBN127cDy-JvHKJLNn6KO5sXXonADC90LcYfJJyYeYD8CoKWfT9sSE7GBruZ4bWjCqojecjJZxxmwatf7g_8T6aNwjcRZyoY8DvlsU9fm6N8Rf5GT8DmNShvjd7hYqiKszzdpHbnsc3DpkRujwDMswMf0q2EeLG4afa7FwqnKeMJi0y7HXXVG1encg6QH-4jAd2h4ercXPTZAxTvhyEUddhsK7635_ZeaCaEm1RCNia6DEOO4XXp_cwn2zrg_4GR7tVrblHvdO59QCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9702fd683.mp4?token=UPwCGcdWBRbPL0BMj0TbsNDlVOmG2HITMOKpiGZUmdeJ2IdH8YMz2MlVFa4Fn-QncH2VosKSBN127cDy-JvHKJLNn6KO5sXXonADC90LcYfJJyYeYD8CoKWfT9sSE7GBruZ4bWjCqojecjJZxxmwatf7g_8T6aNwjcRZyoY8DvlsU9fm6N8Rf5GT8DmNShvjd7hYqiKszzdpHbnsc3DpkRujwDMswMf0q2EeLG4afa7FwqnKeMJi0y7HXXVG1encg6QH-4jAd2h4ercXPTZAxTvhyEUddhsK7635_ZeaCaEm1RCNia6DEOO4XXp_cwn2zrg_4GR7tVrblHvdO59QCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفتگو با خبرنگاران در کاخ سفید تاکید کرد که هیچ کشتی‌ای بدون تایید ایالات متحده اجازه ورود به ایران یا خروج از آن را ندارد و نیروی دریایی آمریکا در این زمینه عملکرد فوق‌العاده‌ای داشته است.
ترامپ با اشاره به خسارت‌های سنگین مالی جمهوری اسلامی در پی این اقدامات گفت: «بر اساس پیش‌بینی‌ها، آن‌ها روزانه ۵۰۰ میلیون دلار ضرر می‌کنند؛ رقم بسیار زیادی است و چه ۲۰۰، ۳۰۰ یا ۵۰۰ میلیون دلار باشد، آن‌ها در حال از دست دادن پول گزافی هستند.»
رئیس‌جمهوری آمریکا با تاکید بر لزوم آزادی کشتیرانی افزود: «خواسته ما این است که این آبراه بین‌المللی، باز و آزاد باشد. تنگه هرمز یک مسیر دریایی بین‌المللی است، هیچ‌کس نباید در آن عوارض وضع کند و ما اجازه چنین کاری را نخواهیم داد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75601" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/011b067e31.mp4?token=ZpBGJvZQM4E65mByOXTVUuD4Le2AqojnOB04PsgFG5I2EOEdVA2-S-XFaByMrZaFUK6csn-1mixlTdw9Hh634IDdRtwGMzcNtqqGI1Rl5ooL6M_yjhGMfcUIhVTdcxVo_u61K0ISDtI2EdL-BH8MrQa5kYAlxZuyBVRHctf1KtUcFTtyPrAZNlhjPLXkmCyJke6-e8GkEs0RVOeWJGoH3ymArgNhch3jP9jGyPllPRZkeWFKllVra2OI5P45MlPYkXN3HmlCGZwcZ99TvC-GyUaqT37Wt2sZuYeCPDaIjLC0GE4oCv6VRJiQqflBeNhVbAirzxXpuYnOWe_AYjp4YA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/011b067e31.mp4?token=ZpBGJvZQM4E65mByOXTVUuD4Le2AqojnOB04PsgFG5I2EOEdVA2-S-XFaByMrZaFUK6csn-1mixlTdw9Hh634IDdRtwGMzcNtqqGI1Rl5ooL6M_yjhGMfcUIhVTdcxVo_u61K0ISDtI2EdL-BH8MrQa5kYAlxZuyBVRHctf1KtUcFTtyPrAZNlhjPLXkmCyJke6-e8GkEs0RVOeWJGoH3ymArgNhch3jP9jGyPllPRZkeWFKllVra2OI5P45MlPYkXN3HmlCGZwcZ99TvC-GyUaqT37Wt2sZuYeCPDaIjLC0GE4oCv6VRJiQqflBeNhVbAirzxXpuYnOWe_AYjp4YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید رسایی هم تلویحا وجود یا عاملیت داشتن مجتبی خامنه‌ای در تصمیم‌گیری‌ها رو زیر سوال برد.
بعد از شعار جماعت در لحظه 01:48 ، یک بچه میگه: مرگ بر دیکتاتور!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/75600" target="_blank">📅 22:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=bM5qCfjwxZOrdE8HJAoVM_UX6OK1JUEfxCYJ3jYhx04ofLWyN69z7OCj0BcJaCRFIme1dO3qpyB_FXXCUTpQhD77xgzMWUliG71G58jvokMy9bTlh98v9_9CGyK_54OW5mnZLbtccqYkEqzMxaZYeol3F6H64lQ05eNYY21jT2Q1iHuQWp1FQg2urkJ55D9CN77QTdg_PXlm1-zUzhnyWzL7B0BaXFVcgt8PicTT4Gtyg8lrMs4HpQOGw_QKjf7z--VRXkGEd5GBKsfE0ek5OLG_BtGl_effKx7ZLV6xOoJ9NZnlXp0UL15vsSeaOU8KrZM7jB-no00nr0G0RGBveQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/afe365b1c4.mp4?token=bM5qCfjwxZOrdE8HJAoVM_UX6OK1JUEfxCYJ3jYhx04ofLWyN69z7OCj0BcJaCRFIme1dO3qpyB_FXXCUTpQhD77xgzMWUliG71G58jvokMy9bTlh98v9_9CGyK_54OW5mnZLbtccqYkEqzMxaZYeol3F6H64lQ05eNYY21jT2Q1iHuQWp1FQg2urkJ55D9CN77QTdg_PXlm1-zUzhnyWzL7B0BaXFVcgt8PicTT4Gtyg8lrMs4HpQOGw_QKjf7z--VRXkGEd5GBKsfE0ek5OLG_BtGl_effKx7ZLV6xOoJ9NZnlXp0UL15vsSeaOU8KrZM7jB-no00nr0G0RGBveQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا، در کاخ سفید گفت: «جمهوری اسلامی قرار نیست سلاح هسته‌ای داشته باشد. ما نمی‌توانیم اجازه بدهیم.»
او افزود که در صورت دستیابی جمهوری اسلامی به سلاح اتمی، «در خاورمیانه جنگ هسته‌ای به راه خواهد افتاد، و آن جنگ به اینجا خواهد رسید، آن جنگ به اروپا خواهد رفت.»
رییس‌جمهور آمریکا تاکید کرد: «ما نمی‌توانیم اجازه دهیم چنین اتفاقی بیفتد، و چنین اتفاقی هم نخواهد افتاد. قرار نیست اتفاق بیفتد.»
ترامپ درباره محاصره‌ بنادر جنوبی ایران از سوی آمریکا نیز گفت: «کنترل کامل تنگه هرمز را در دست داریم. این محاصره ۱۰۰ درصد موثر بوده است. هیچ‌کس نتوانسته عبور کند. مثل یک دیوار فولادی است.»
او افزود: «هیچ کشتی‌ای نتوانسته بدون تایید ما عبور کند. و نیروی دریایی کار فوق‌العاده‌ای انجام داده است. و هیچ کشتی بدون تایید ما به ایران نمی‌رود یا از ایران خارج نمی‌شود.»
ترامپ درباره اورانیوم غنی‌شده ایران نیز گفت: «ما اورانیوم بسیار غنی‌شده را می‌گیریم. ما به آن نیاز نداریم. احتمالا بعد از اینکه آن را بگیریم نابودش می‌کنیم، اما اجازه نخواهیم داد آن‌ها (مقامات جمهوری اسلامی) آن را داشته باشند.»
دونالد ترامپ، رییس‌جمهور آمریکا پنج‌شنبه در کاخ سفید به خبرنگاران گفت که ایالات متحده خواهان دریافت عوارض در تنگه هرمز نیست.
پیشتر مارکو روبیو، وزیر خارجه آمریکا اعلام کرد که اجرای سیستم اخذ عوارض در تنگه هرمز از سوی جمهوری اسلامی، دستیابی به توافق دیپلماتیک را غیرممکن خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75599" target="_blank">📅 20:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=O-GPvBbbQqVt5sybdHTYNGLMtHGn-CRHDGlGvd7rxV_1Y4wuM0Y1AiCi3PJgsOjNIzlnOKzeTqoJVOfGrvNa9VwiiiwHY_N2OZpvwE1o6HbozwONz8LQ9ItV3W3VTTfI_KwPn9abK4_U9cGvJPXhdYjydNM3ob_S1cy5TlhO-coWFbKbiD7YbAwFBul3ExrvZCThO-fwmmhjOLjovAfPvKTX84OFF72widXgnEggrbvJFacLBouiDsxDeYUbKOYUntRB1XHbaY_7JGAKBok2SeBegLRYelxXwNTglcXBhyX_fClGWgtXIEhHX_A68xkslv8XERPe3QvRl0UJeuryMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e56ee3c30.mp4?token=O-GPvBbbQqVt5sybdHTYNGLMtHGn-CRHDGlGvd7rxV_1Y4wuM0Y1AiCi3PJgsOjNIzlnOKzeTqoJVOfGrvNa9VwiiiwHY_N2OZpvwE1o6HbozwONz8LQ9ItV3W3VTTfI_KwPn9abK4_U9cGvJPXhdYjydNM3ob_S1cy5TlhO-coWFbKbiD7YbAwFBul3ExrvZCThO-fwmmhjOLjovAfPvKTX84OFF72widXgnEggrbvJFacLBouiDsxDeYUbKOYUntRB1XHbaY_7JGAKBok2SeBegLRYelxXwNTglcXBhyX_fClGWgtXIEhHX_A68xkslv8XERPe3QvRl0UJeuryMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز پنج‌شنبه اعلام کرد اگر تهران طرح دریافت عوارض برای عبور از تنگه هرمز را اجرا کند، رسیدن به یک توافق دیپلماتیک میان ایالات متحده و ایران غیرممکن خواهد شد.
او در گفت‌وگو با خبرنگاران گفت: «هیچ‌کس در جهان از سیستم عوارض‌گیری حمایت نمی‌کند. چنین چیزی نمی‌تواند اتفاق بیفتد. غیرقابل قبول خواهد بود. اگر آنها همچنان دنبال اجرای آن باشند، رسیدن به یک توافق دیپلماتیک غیرممکن می‌شود. بنابراین اگر بخواهند چنین کاری انجام دهند، این تهدیدی برای جهان است و کاملاً غیرقانونی است.»
او همچنین خبر داد که در مذاکرات با تهران برای پایان دادن به جنگ آمریکا و اسرائیل علیه ایران، «پیشرفت‌هایی» حاصل شده است و به گفته او «نشانه‌های خوبی وجود دارد»، اما واشینگتن با «سیستمی روبه‌روست که خودش تا حدی دچار شکاف و چنددستگی است.»
وزیر خارجه ایالات متحده با اشاره به این که مقام‌های ارشد پاکستان به عنوان میانجی مذاکرات امروز به تهران سفر خواهند کند، گفت: «ترجیح رئیس‌جمهور آمریکا این است که یک توافق خوب حاصل شود... من اینجا نیستم که بگویم حتماً چنین اتفاقی خواهد افتاد، اما اینجا هستم که بگویم ما هر کاری بتوانیم انجام می‌دهیم تا ببینیم آیا می‌توانیم به توافق برسیم یا نه.»
او در عین حال افزود که اگر یک توافق خوب حاصل نشود، دونالد ترامپ «به‌روشنی گفته است گزینه‌های دیگری هم دارد.»
پیش از این گزارش‌هایی درباره سفر روز پنجشنبه فیلد مارشال عاصم منیر، رئیس ستاد ارتش پاکستان، به تهران منتشر شده است. خبرگزاری‌های رسمی ایران این خبر را یک روز پس از آن منتشر کردند که وزیر کشور پاکستان، برای دومین‌ بار طی هفته جاری وارد تهران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/75597" target="_blank">📅 19:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nnNCdVx4ihf0LeWCnlCHjmQ_Uk1grIC1fKeVj6vdzaW4Ks8wTJOAo3MDsksy57QPq4EM8LF5LSqx32WL0lskPvRG4Z63zcuxlVf-GbV45DFTZ00bWZrGFh22JxMFKJKtLEUv3_wqNLCopZocg0JNf2ngiUxtGFvo8fR8mU7i0FJe3hzBEjyFi6MdD35wUd-SjaDimN9aVMPxbm5FZK88iFViWrv4sO01KNvoS3JddRLBBjfX251puPBo69VMCIKE7VrizvFb_dIysmpPLTXmMeMp_4XJf275pppctb4JckF1cza9qsZ7HkoV8guQJB9Snk4InY8UARMsXbw_iKUIyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار فاکس نیوز به نقل از یک منبع آگاه از روند مذاکرات خبر داد که کاخ سفید گزارش خبرگزاری رویترز مبنی بر این‌که مجتبی خامنه‌ای دستور داده اورانیوم با غنای بالا در ایران باقی بماند را رد کرده و آن را نادرست دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75596" target="_blank">📅 18:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUgkR3X1wcu8ui5zPECdXiKdPH3buem6G_avPHfDkrYsWHWuxOCxVfZxCGsvIAm0BX8TJBSOdxBA0HgYg1NhF7SFbcleQ7ztwAFVBPbeJeqBqP0h1fM-mEjmYAKOPAnjhWLWSgz0WSrwgrpaI0Rs0CzIrDpmeP_h5f5D4WzvynHqZhFGIf6ntVfnroyf9objmL5Iy3Xtp3ICMSCUpVXxq_5UV0foa82OTA0U_R7Kw1-MsLVLJFY5amIPt_vzz4rHT_mCu07T2mlnB3QHcCpuTavbQjljw9bfHLlL1M2d1RIoZwAbjUtqbzSNNhc4W0775EXcR6nx4lmMHnlGxuVhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تحقیقی FTM هلند در
گزارشی
نوشته که توماس اردبرینک، خبرنگار هلندی نیویورک‌تایمز و شبکه NOS در ایران، همزمان مشاور شرکت آبجوسازی هینکن هم در ایران بوده و برای این کار ماهانه تا یک‌سال ۵ هزار یورو دریافت می‌کرد. اردبرینک دریافت مبلغ را انکار کرده.
طبق این گزارش این روزنامه‌نگار به طور منظم کارهای جانبی (پروژه‌ای) برای این شرکت آبجوسازی در ایران انجام می‌داده است و نه تنها کارمندان اعزامی و بازدیدکنندگان را در تهران می‌گردانده، بلکه گفته این شرکت آبجوسازی را با وکلا و مشاوران محلی نیز مرتبط کرده است.
FSeifikaran
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75595" target="_blank">📅 18:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75594">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W57jl-3vcGScQ9vo6B0vVdP1MPyiPmyvsfOB-YV6P9QtX7WgKbijAamOqk_yeoJxB4Kuj76SOJVcIq1pI3BfYOWerpr6Maax8WmdA9rYTrBQDA8hMXtOh0fjLtoleN_b4Duq1kYinweA8i4ffrWoWO2KdL3Pj1qFTN51zOcVl5NlQX4hCDSd1W_nVpbk5Bx0ijOAzQGtFUVe0Av1FL4aHc6VVo3JSrK7O24uk6VO4xqhfhIMrlqFbYedopyLRgB0pnrNh__uXgz84obTi0zo0VlD5ME6_H5uQbHqid_CzJleKHwuHuIhqEGErjcDcgJoCbkGWvByBQZx_ohva2Xg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انور قرقاش، مشاور ارشد رئیس دولت امارات متحده عربی، می‌گوید که برخی رفتارهای ایران در سال‌های گذشته باعث کاهش اعتماد میان کشورهای منطقه خلیج فارس شده است.
او در پیامی در شبکه اجتماعی ایکس نوشت که کشورهای منطقه طی سال‌های طولانی با «رفتارهای زورگویانه و تهدیدآمیز» ایران روبه‌رو بوده‌اند؛ رفتارهایی که به بخشی از واقعیت سیاسی خلیج فارس تبدیل شده است.
آقای قرقاش همچنین تاکید کرد که شکاف میان مواضع تند و ادعاهای دوستی از سوی ایران، باعث از بین رفتن اعتماد و اعتبار شده است «و امروز، پس از تجاوز وحشیانه ایران، حکومت ایران تلاش می‌کند واقعیت تازه‌ای را که از یک شکست آشکار نظامی به‌وجود آمده تثبیت کند؛ اما تلاش برای کنترل تنگه هرمز یا تعرض به حاکمیت دریایی امارات متحده عربی چیزی جز خیال‌پردازی و آرزوهای دست‌نیافتنی نیست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/75594" target="_blank">📅 17:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=sNNjBkRb9MhYCDWWbN-v61awIHZMewtZsgMNB2UqIV4dRCfP-xMBuPG-ygQfVbYDeWIXBFa0PmFpLc7682ETfUxl2yb9M3gz-zltcxjebfDkHXoM4SkJDgvaS3icZf99VTt-TgmIekCrtNe0zAAKQaMoPSlhLRRkMPtoNaDJJtYSF1dxcMU-q7Coy4SfLpPwd1Iwi6IUt16w8rsG0JnSeClzkK5rSPbpLdwx4X0CPXKumKjzdmWtO_hTggfyEuB42DTRC88t6gTJhbvL8oS9py1HPU4I0-WK0bTkufT9TPLc4CcYqv00YfMs9W2-hyt2kZaSJx6a7I4JC7408pfkvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f4f44e0c.mp4?token=sNNjBkRb9MhYCDWWbN-v61awIHZMewtZsgMNB2UqIV4dRCfP-xMBuPG-ygQfVbYDeWIXBFa0PmFpLc7682ETfUxl2yb9M3gz-zltcxjebfDkHXoM4SkJDgvaS3icZf99VTt-TgmIekCrtNe0zAAKQaMoPSlhLRRkMPtoNaDJJtYSF1dxcMU-q7Coy4SfLpPwd1Iwi6IUt16w8rsG0JnSeClzkK5rSPbpLdwx4X0CPXKumKjzdmWtO_hTggfyEuB42DTRC88t6gTJhbvL8oS9py1HPU4I0-WK0bTkufT9TPLc4CcYqv00YfMs9W2-hyt2kZaSJx6a7I4JC7408pfkvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بریتانیا از توافق تجاری ۵ میلیارد دلاری با کشورهای خلیج فارس رونمایی کرد؛ توافقی که در بحبوحه تنش‌های منطقه‌ای پس از جنگ ایران، به گفته لندن «پیامی از ثبات و اعتماد» به بازارها می‌دهد.
این توافق با شورای همکاری خلیج فارس شامل عربستان، امارات، قطر، کویت، عمان و بحرین است و قرار است سالانه حدود ۳.۷ میلیارد پوند به اقتصاد بریتانیا اضافه کند.
لندن می‌گوید ۹۳ درصد تعرفه‌های کشورهای خلیج فارس برای کالاهای بریتانیایی حذف می‌شود؛ از جمله محصولات غذایی، خودرو، صنایع هوافضا و الکترونیک.
در مقابل، بریتانیا نیز برخی تعرفه‌ها را کاهش می‌دهد، هرچند نفت و گاز کشورهای عربی پیش‌تر هم بدون تعرفه وارد بریتانیا می‌شد.
فعالان حقوق بشر از نبود بندهای الزام‌آور درباره حقوق بشر در این توافق انتقاد کرده‌اند و آن را «عقب‌گرد اخلاقی» توصیف کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75593" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y0cENEgIzfTRCKXeSEKm6S0HuVbdKiuVUwu73m7SGNPtXFLWUJEd1wT0FOWa6OYId3GGMF2Fuiu3x1jsajQUKxf0ThJPX_Kd2VlSpn9KIwZ_366KR7CZn09i0n-L6RbUHg3RO-aZByd2_suaC4V1XX1HGRn1gA9_1dm9-Ef7bOHeturiEIuSF6ZH9DYbrTDKgYAXdqsa4xKLQ30bLdryLGFBhU-Y8s39ytE-crAK0NRNYS7a_bXYnKtOv3vKR-5HSJGdc_TfLKQ_4yQFbygnYKKdKxdJEiE7sLjpllHuH-9t6Anul7M5Aqiz5V64wFSuJT_YkU3dYd6RAgI8Oz-9Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی یزدی‌خواه، نایب‌رییس کمیسیون فرهنگی مجلس، گفت در شرایط فعلی تصمیمی برای بازگشایی اینترنت جهانی وجود ندارد و محدودیت‌ها با «ملاحظات امنیتی» ادامه خواهد داشت.
یزدی‌خواه قطع اینترنت جهانی را به مصوبات شورای عالی امنیت ملی نسبت داد و گفت این تصمیم به‌دلیل «مسائل امنیتی، امنیت کشور و حفظ جان افراد» گرفته شده است.
با وجود اینکه نت‌بلاکس اعلام کرده خاموشی اینترنت در ایران وارد هشتادوسومین روز خود شده، یزدی‌خواه گفت بیش از ۹۰ درصد نیازهای مردم در وضعیت فعلی برآورده می‌شود و مراجعات گسترده‌ای در اعتراض به قطع اینترنت وجود ندارد.
او همچنین گفت در قالب طرح موسوم به «اینترنت پرو»، تاکنون بیش از یک میلیون نفر دسترسی دریافت کرده‌اند؛ طرحی که منتقدان آن را مصداق اینترنت طبقاتی و تبعیض‌آمیز می‌دانند، زیرا دسترسی به اینترنت جهانی را به گروه‌های خاص محدود می‌کند و شهروندان عادی را از حق برابر دسترسی آزاد به اینترنت محروم نگه می‌دارد.
نایب‌رییس کمیسیون فرهنگی مجلس همچنین گفت شرکت‌های صادرات و واردات، مراکز علمی و پژوهشی، آزمایشگاه‌ها و برخی اصناف در صورت نیاز می‌توانند برای دسترسی به اینترنت بین‌الملل اقدام کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 205K · <a href="https://t.me/VahidOnline/75592" target="_blank">📅 17:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75591">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bvy_E7O2vpkYSr35wZlypPeszSGGnBnNjZAYdLP40SQ-IDc4L7pBAeAPXeWSO0pU3lnYBmtAGWQNYu-kokkTWeEe0BiQb8jRLyB1nRsr_3cITWCN5Rm23YIRJyjk1_C8y504wJnWhkPxixb2LqyIwiZ-4pj4xaefV4RXEbBVWM0Tedz01VKAI91_Ju3QJBd5sb-oIXn6EjLJlEqWG53f36eZRzYjJ6jMdrW5KJiZctytWnK-0FtPVgNTPB_ElkZgS7ETJQccxMiF5LzaLPjoJLKMBRaea2sxn9cYSkF-6LF-uIURLf4-E8Z20tZkz8ATLk1Bf_VFlN1txVScGSc-9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع ارشد در حکومت ایران گزارش داد مجتبی خامنه‌ای، رهبر جمهوری اسلامی، دستور داده ذخایر اورانیوم با غنای بالا نباید از ایران خارج شود.
به گفته این منابع، این دستور موضع تهران را در برابر یکی از اصلی‌ترین خواسته‌های آمریکا در مذاکرات برای پایان دادن به جنگ آمریکا و اسرائیل علیه جمهوری اسلامی سخت‌تر کرده است.
مقام‌های اسرائیلی نیز به رویترز گفته‌اند دونالد ترامپ به اسرائیل اطمینان داده هر توافق احتمالی باید شامل خروج ذخایر اورانیوم غنی‌شده از ایران باشد.
یکی از منابع ایرانی به رویترز گفت دستور رهبر جمهوری اسلامی و اجماع در ساختار حاکمیت این است که ذخایر اورانیوم غنی‌شده نباید از کشور خارج شود.
به گفته منابع رویترز، مقام‌های جمهوری اسلامی معتقدند انتقال این مواد به خارج، جمهوری اسلامی را در برابر حملات احتمالی آینده آمریکا و اسرائیل آسیب‌پذیرتر می‌کند.
@
VahidOOnLine
دقایقی پس از این خبر رویترز بهای نفت در بازارهای جهانی نزدیک به دو دلار افزایش یافت.
قیمت هر بشکه نفت خام برنت دریای شمال بعدازظهر پنجشنبه ۳۱ اردیبهشت‌ماه در بازارهای اروپایی از ۱۰۵ دلار به بیش از ۱۰۷ دلار افزایش یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/75591" target="_blank">📅 17:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrmGGqhwEn7a6tx6WwvSqz6kPX8VRqFS9aE5KT3TMoTREsz7eMIkDZtqQ-BKyqVSfwVXJ5dBLj3FnoLwb3_YftjUVvBrGV9G8MdCYjy8YzBIamQtmC3OsGJDCLdkd8xPcPPoO-XBNVK5nMu63Cvtz4_oU_H8KjUyTvYpn_X-Nd874ZvQhMmV7yYs9bVfQG4Oqrx2ar_mnaSk-OBkIuG1tBvR_ifV6rEDZof3CDa-I-MSnBPGkpT77n4Abxl9n4Hdg4qGjmiFV_n4CjpOiNn9PYgHR5a91IR8LmblfsZtoYyPWeNG8w0kwZK9n5ayOcOcP48ZJE6z6C_J7_b8xMIeIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی کابی‌زاده، شهروند ۴۷ ساله و پدر یک دختر بود که در اعتراضات دی‌ماه در استان خوزستان بازداشت و پس از انتقال به مرکز درمانی به دلیل منع رسیدگی جان باخت. او دختری به نام حلما دارد.
بر اساس اطلاعات رسیده به ایران اینترنشنال از افراد مطلع از خانواده او، مهدی کابی‌زاده در اعتراضات اهواز به دست ماموران بازداشت شد و سپس به دلیل بیماری خونی و روده به بیمارستان منتقل و بستری شد. با این حال، مسئولان بیمارستان به دلیل سابقه حضور او در اعتراضات و بازداشتش از رسیدگی و درمان کافی خودداری کردند که موجب جان باختن او شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75590" target="_blank">📅 17:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75589">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrxuS0LRuHqmHBJ9ycclepFW4lipxDPgy1Xsp7dWPADolAgmVxuWg3xGcdKfkVPItrqGNqDP5tDsaDw1GBW3TfGxZmWAZqGkPm_IQjvZdDoCKU3sjR7QX5VKNcLP-SKQRPrsleZJVW0r2hLunaBtuDMatPW4LwbCpHE2RJqngiD1VK42_1rFiMCm1s3-nJ6Cf736tEyE2njDig_XfzZQcGjxet_L0C020z7ZMEgMuaxry5e1yeLQKT_0pxKCNxBeWUIuQ0ZntheZGqaKMVYZGleh2pikvmqBi2n6_1tOV_GA1adMtoesM53tWBX-CppBWMQqI2vpbqpx7u8NchSYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی دو زندانی را به اتهام عضویت در «گروه‌های تروریستی تجزیه‌طلب» و «قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه» اعدام کرد.
ارگان رسمی دستگاه قضایی ایران، میزان، هویت این دو نفر را رامین زله و کریم معروف‌پور معرفی کرده و نوشته که آنها صبح روز پنج‌شنبه، ۳۱ اردیبهشت، اعدام شدند.
میزان نوشته که رامین زله «پس از طی دوره‌های آموزشی از طرف گروهک ماموریت پیدا کرده بود تا در ناآرامی‌های کشور به عنوان لیدر شرکت کند».
ارگان رسمی قوه قضائیه ایران همچنین نوشته که این دو نفر «اعتراف» کرده بودند که «برای ترور فرمانده پایگاه سپاه یکی از شهرستان‌های غرب کشور» با یکدیگر «همکاری» داشته و برای این کار، «سلاح» نگهداری می‌کردند.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/75589" target="_blank">📅 09:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75588">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/622e876399.mp4?token=Y271AMJGSm-p-OZpIMruT7ajv5-bWC8_TmfHk1sc8Rg6Hg8lSlLQAYRnw-5fvTeBK2OJROpUTlZCN2r4h7WdwMXn7zlA1mDkrCaNwAWxDIeYiy-fp7C8vQQeldx5Tb0gEZfKX0sz2inKe5JhG83VcwsoADXUnGDcDOUwPn5kWR4Za2RTY--jbc9GvEQJ8zUnAMOms_zImxnWpplw3rCtXViDcXWvj1XHJj9XReEM1ThpUfigsG-nb_SHVocV06RqoHnPra_e04jsInfYU4kaxYgcK7RkQvp0VxdZZpV1qWSIshYjVOvIQLmrJWme9hICRKYz21kSI3loiXFEwHPgaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/622e876399.mp4?token=Y271AMJGSm-p-OZpIMruT7ajv5-bWC8_TmfHk1sc8Rg6Hg8lSlLQAYRnw-5fvTeBK2OJROpUTlZCN2r4h7WdwMXn7zlA1mDkrCaNwAWxDIeYiy-fp7C8vQQeldx5Tb0gEZfKX0sz2inKe5JhG83VcwsoADXUnGDcDOUwPn5kWR4Za2RTY--jbc9GvEQJ8zUnAMOms_zImxnWpplw3rCtXViDcXWvj1XHJj9XReEM1ThpUfigsG-nb_SHVocV06RqoHnPra_e04jsInfYU4kaxYgcK7RkQvp0VxdZZpV1qWSIshYjVOvIQLmrJWme9hICRKYz21kSI3loiXFEwHPgaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'من وطن‌فروش نیستم... زنده باد جمهوری اسلامی... تا آخر کنار ولایت می‌مانیم... این پرچم با طوفان نمی‌افتد... سقوط این کشور را به گور خواهند برد... عزت این ملت معامله‌شدنی نیست راه مقاومت ادامه دارد...'
تبلیغ «وطن»دوستی در «کشور جمهوری اسلامی» با شهروندان وارداتی از 'کمور، سنگال، غنا، کنیا، بورکینافاسو، ساحل عاج، نیجریه، تانزانیا، مالی'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75588" target="_blank">📅 03:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75587">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W4-sNttH3splMLvAheT9DH-9TjaRqa20NTghU109tkN9iFEIGo3JHucwAGCFqr4l1tFddpllBBDlilQPyhjaX2K-221mFyKy8LNUTzFldy_VEYXUL_5qeWqyAeKC-MsRWr3bEgJdmLd8l0fj4WANK1hfikJAP3VyBqkGQWPpI3_zH0zkrFd4gJ8EDR9-isRC_y3-hq2rfsc-1VOo-n4frMLCF86UDkyJM7A3ayO611ftNirNEksqoulwvk4HL8aAx6EB_WFTkgtauOxZV1GE9dU4c_ThpqSEFBgKsFNDG-CmDNXYEEHn712ImMOajgfrFUJwHzdBehmqD-ttMOK_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی کاخ سفید در شبکه اجتماعی ایکس، روز چهارشنبه ۳۰ اردیبهشت در پُستی، عکسی از رئيس جمهوری آمریکا، دونالد ترامپ را منتشر کرد که زیر آن تصاویری از «دشمنان خنثی‌شده آمریکا بدست پرزیدنت دونالد جی. ترامپ» دیده می‌شود.
در این پست تصاویری از علی خامنه‌‌ای رهبر کشته‌شده جمهوری اسلامی، نیکلاس مادورو رهبر دستگیر‌شده ونزوئلا، رائول کاسترو رهبر سابق کوبا، و ابو بلال المنوکی از رهبران داعش که به جای تصویرش پرچم داعش نشان داده شده، منتشر شده است.
کاخ سفید در مورد کاسترو، روی تصویر او نوشت که علیه او کیفرخواست صادر شده است. در مورد مادورو روی تصویر او نوشت که دستگیر شده است. و در مورد علی خامنه‌ای و ابو بلال المنوکی روی تصاویر آن‌ها نوشت که «کشته‌ شدند.»
حساب رسمی کاخ سفید افزود: «عدالت اجرا خواهد شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/75587" target="_blank">📅 03:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iDknWpHb2B59AamJLa4NDfPvniPuo-2sr8tymFz4dm3JmVfwjlSnoDCeESl7wCZhzG9OT22Ed2Idd17flLQEa-MfgpeXq4AJCk7vG4dlT6_gWhskWucXYajJ-suNYN-CLl8lkCb6mmVdIFgftsK349RLMJNqKdm6Vj6MwHqpPM0BCFCUAQJJsCteZk72_m_to-cTPfRe2SvkwgOBIxGFzmd0nr9Rn8adexIVYvdx6BEIG3J_lQqLVHOvK4fqxr8D3YD7QrDwrIQ54gmW0YmXG3-XXBcohRPkC50hprxHVudgAmktihGNzWzkkbixch7yNqSM5SMF7Tjo210lok3Sjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه اسرائیل هیوم به نقل از «منابع آگاه» نوشت جلسه چهارشنبه ۳۰ اردیبهشت در کاخ سفید درباره ایران با اختلاف‌نظر شدید میان مقام‌های ارشد دولت آمریکا همراه شد، اما رییس‌جمهوری آمریکا در نهایت، خلاف نظر وزیر جنگ و وزیر امور خارجه، و همسو با دیدگاه جی‌دی ونس و فرستادگان ویژه‌اش، ادامه مذاکرات با جمهوری اسلامی را تایید کرد.
این روزنامه راستگرا نوشت ارزیابی مارکو روبیو، وزیر امور خارجه، و پیت هگست، وزیر جنگ آمریکا، این بود که در این مرحله، بدون اعمال فشار قابل‌توجه، از جمله تهدید به حمله و تشدید تحریم‌های اقتصادی، نمی‌توان از جمهوری اسلامی امتیاز گرفت. در مقابل، ونس معتقد بود تازه‌ترین پیشنهاد تهران نشانه‌ای از انعطاف است و می‌تواند زمینه حرکت به سوی یک توافق اولیه را فراهم کند.
منابع آگاه از این جلسه به اسرائیل هیوم گفتند که استیو ویتکاف و جرد کوشنر، فرستادگان ویژه دونالد ترامپ نیز در این گفت‌وگو از موضع ونس حمایت کردند.
آنها پیش از این جلسه با رهبران عمان، قطر و عربستان سعودی گفت‌وگو کرده بودند.
به نوشته این رسانه تنش در این جلسه زمانی شدت گرفت که ترامپ از ونس و فرستادگان انتقاد و آنها متهم کرد که رویکردشان به جمهوری اسلامی امکان می‌دهد زمان بخرد و به تصویر ایالات متحده و نهاد ریاست‌جمهوری آسیب بزند. ونس با لحنی قاطع پاسخ داد که دولت باید به دنبال پایان دادن به این کارزار نظامی، بازگرداندن سربازان به خانه، کاهش قیمت نفت و تمرکز بر مشکلات داخلی آمریکا باشد؛ پاسخی که حاضران را غافلگیر کرد.
اسرائیل هیوم در ادامه این گزارش به گفت‌وگوی ترامپ با رهبران منطقه اشاره کرد و به نقل از دو منبع نوشت که رهبران اسرائیل و امارات متحده عربی، همزمان با تاکید بر ضرورت حفاظت از تاسیسات حساس خود در قبال حملات احتمالی جمهوری اسلامی، از پیش گرفتن «سیاست‌های سخت‌گیرانه» علیه جمهوری اسلامی حمایت می‌کنند.
در مقابل، رهبران عربستان سعودی و قطر ترجیح می‌دهند از بازگشت به درگیری‌ها پرهیز شود.
این روزنامه همچنین به نقل از یک مقام آمریکایی درباره تماس تلفنی ترامپ با نخست‌وزیر اسرائیل نوشت که نتانیاهو از رفتار جمهوری اسلامی و احتمال وقت‌کشی تهران ابراز سرخوردگی کرد، در حالی که ترامپ بر پیچیدگی شرایط و دشواری‌هایی پیشِ رو تاکید داشت. با این حال رییس‌جمهوری آمریکا بار دیگر گفت که به رفع تهدید هسته‌ای حکومت ایران متعهد است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75586" target="_blank">📅 02:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75584">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SiCrk-0sxeqKRGH8Sxe89eYByeCA64dBwhkD9ynoStiyHF0SVOjFCQ1CfjnOSao5h2PdYBCcFVYLy0IiOw7UUi9LPu2LnMV2bpHyrZhE14iJ8Pi3m5eIbm-M2Y468Age7B3gXCVd113v1XOa6hIYqd2R4qVOQlDx-Jyz34Oe_8mHap9L9T6FIHxMKsDBXMmSx7Kc_rCYCrayne-Ki1LHloYLD5D207wx0izWLx6hZiaZ2_xPCWulasNA42qWJz_ex91QEspgQJSZAGdLIGGLevnCEndZJ7tz72awto6YHvUU6uwIzMuDxx3gJ8vWX-LrLZ5Gyq1iY8ogl91OuPR6kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=LK-BuyT84vtFZ9oiUdmAYlWlD7Ht5JOQ1SEwnGW65w6dXUZFgRgXqmInrfXobVRWsYwKNjmuobhJ6CqKoNaRglLc3Jccb1f77Cch0-G9YN4AhYK_z04fFsPhxXAmHrjKxVtjzyY7AihcRBEdZid3YRjdqKfamsGWiQ9sthCz8pdMtLaC96wZVCyCsidEoyv7ErKzNFxsE9gh0k3Eez3QPtQzxCNUS62Rmos1hkBsYVm2mM9WxA7tvGNBlEyOpKCHI4GIk2BS2fGWhctbPjKYIisACyOlYb8lbGsU4YW3rjky3iy7jXDMj6QD-EDvfthMrLB2Hb1KDYbu0B17el_h9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4e82522f4.mp4?token=LK-BuyT84vtFZ9oiUdmAYlWlD7Ht5JOQ1SEwnGW65w6dXUZFgRgXqmInrfXobVRWsYwKNjmuobhJ6CqKoNaRglLc3Jccb1f77Cch0-G9YN4AhYK_z04fFsPhxXAmHrjKxVtjzyY7AihcRBEdZid3YRjdqKfamsGWiQ9sthCz8pdMtLaC96wZVCyCsidEoyv7ErKzNFxsE9gh0k3Eez3QPtQzxCNUS62Rmos1hkBsYVm2mM9WxA7tvGNBlEyOpKCHI4GIk2BS2fGWhctbPjKYIisACyOlYb8lbGsU4YW3rjky3iy7jXDMj6QD-EDvfthMrLB2Hb1KDYbu0B17el_h9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، شامگاه چهارشنبه گفت حاضر است «چند روز» برای رسیدن پاسخ ایران به پیشنهاد واشینگتن درباره توافق پایان جنگ صبر کند اما هشدار داد که این پاسخ باید «۱۰۰ درصد درست» باشد.
او بعد از سخنرانی در جمع دانشجویان نظامی به خبرنگاران گفت اگر پاسخ ایران درست نباشد، تشدید تنش به سرعت رخ می‌دهد و افزود: «ما آماده پیش‌روی هستیم. باید جواب‌های ۱۰۰ درصد درست و خوبی بگیریم.»
ترامپ اعلام کرد که آمریکا در حال حاضر با افراد «خیلی خوبی» از طرف ایرانی مواجه است که «استعداد و قدرت ذهن» دارند؛ افرادی که به گفته او جایگزین رهبران پیشین ایران شده‌اند.
این اظهارات ساعتی بعد از آن است که سخنگوی وزارت خارجه ایران اعلام کرد تهران در حال بررسی طرح پیشنهادی جدید آمریکا است.
این طرح توسط اسلام‌آباد به دست مقام‌های جمهوری اسلامی رسیده است؛ همزمان با سفر وزیر کشور پاکستان به تهران.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/75584" target="_blank">📅 23:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A0BNRqbkVrn0RVbkgQjvRZzL4v5GD8KUHc7kQilRW95lrYwmKRrtBz57Pdu2fvB6aVZGA6H4MF4EJbydPez0Z9iv1zHmb-KAkkT26rldMLUP28CnYx8OgI7jSw6_TmfTa05zfKtxs8hmP0CJjDMlaCNe1DKIE_pLEG8JihuCLXd4QueBtOUSbUY_InBcakhQW3rQ8r_DXU808QaZ-u_jxNBPZIzYTxkVsrXPNhJLFkvGdV9qNcI4G7yoRSUjBbqSQR4LWto2Dci7B6hlQX9kZrSFDimmCaTSOVh-5mQQopo76LaHGVTGhO-pBiL-4kiyJsLnSPZfkmG1fjlyRGraQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jrAj1LvTux3ub-0gOgN4WbgxtwXRqxfFRch67fopZWjKBbWcnEgCsX1XVDymgciPDqC0Qeois9FU3UqqUH8TPremBvywXwyx1NLP5cBsGLQi5OXNzY4G9jYG19ruNxLxVJwBqIjFbIf5e35K2f_9Hc7c3praofYuU7N1ESJ6-7iMwkrpksxjY8iM_Zjqr8ORybeD1Pcu6UM1KAcg1ZSVFLXF5TwLTUnGP38kAA_XcHEiBSllJ24GO6-3-5EwCcqN39igFYixm8MMut1ZWFINxmq3VHFb7msSQagCEqXFF8g2W28EtYmlkEq7Zg5N7tNmBD6zDphe9UhqCZfls--IEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آکسیوس در گزارشی اختصاصی اعلام کرد دونالد ترامپ در تماس تلفنی طولانی و «دشوار» خود با بنیامین نتانیاهو، از تلاش میانجی‌ها برای تدوین یک «تفاهم‌نامه» خبر داده است. بر اساس این طرح، آمریکا و جمهوری اسلامی با امضای این تفاهم‌نامه رسما به جنگ پایان داده و یک دوره ۳۰ روزه را برای مذاکره درباره برنامه هسته‌ای ایران و بازگشایی تنگه هرمز آغاز می‌کنند.
به گفته دو نفر از منابع آکسیوس، این پیشنهاد با مخالفت شدید نخست‌وزیر اسرائیل مواجه شده و دو رهبر درباره مسیر پیش‌رو اختلاف‌نظر جدی دارند. یک مقام آمریکایی وضعیت نتانیاهو را پس از این تماس، «بسیار خشمگین و آشفته» توصیف کرد.
آکسیوس به نقل از منابع خود نوشت سفیر اسرائیل در واشنگتن نیز نگرانی شدید نتانیاهو از این گفتگو را به اطلاع قانون‌گذاران آمریکایی رسانده است؛ هرچند سخنگوی سفارت این موضوع را تکذیب کرد. یکی از منابع با اشاره به بدبینی همیشگی نتانیاهو به روند گفتگوها گفت: «بی‌بی همیشه نگران است.» کاخ سفید و دفتر نخست‌وزیری اسرائیل از اظهارنظر در این باره خودداری کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75582" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=XQ4WxJiVXlWU2Pop5gzEx4S583dyJS-DmrSvL2klNiOQYVh7sOQDLg1izkcB24YGEySH3Q02xpwD0zVT2zSvUm8vz5G1_6MDWizHMVNOuCM54ATF06dn4okUqZotrOsKF40qUuNAyrIIygw_teXBIRhwrH-p3uI4aF1nGRF-59Aejj3yRD1Yc7NXIhwDdp6ZkVRCY-xYSmiDkR2HozS33zPeGGpfTopCfarB1NKvYGMsz3AcEmpYd0Bi9XyveiYu7osnY3IHegLTEqKf-AuwSYEA3a0bkY9Hgrv977reY6gbUEvP93kF3iExtP3ncJBWK8yQXJrSBSGCClei-sbIsA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a02e28e7c.mp4?token=XQ4WxJiVXlWU2Pop5gzEx4S583dyJS-DmrSvL2klNiOQYVh7sOQDLg1izkcB24YGEySH3Q02xpwD0zVT2zSvUm8vz5G1_6MDWizHMVNOuCM54ATF06dn4okUqZotrOsKF40qUuNAyrIIygw_teXBIRhwrH-p3uI4aF1nGRF-59Aejj3yRD1Yc7NXIhwDdp6ZkVRCY-xYSmiDkR2HozS33zPeGGpfTopCfarB1NKvYGMsz3AcEmpYd0Bi9XyveiYu7osnY3IHegLTEqKf-AuwSYEA3a0bkY9Hgrv977reY6gbUEvP93kF3iExtP3ncJBWK8yQXJrSBSGCClei-sbIsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز چهارشنبه ۳۰ اردیبهشت با تاکید بر این‌که نیروی دریایی و هوایی ایران از بین رفته‌اند، گفت اکنون تنها سوال این است که آیا آمریکا برای تمام کردن کار بازمی‌گردد یا جمهوری اسلامی پای امضای یک سند (توافق‌نامه) خواهد آمد.
ترامپ که در مراسم فارغ‌التحصیلی آکادمی گارد ساحلی آمریکا سخنرانی می‌کرد، گفت: «همه چیزِ آن‌ها از دست رفته است؛ نیروی دریایی‌شان نابود شده، نیروی هوایی‌شان از بین رفته و تقریبا همه‌چیزشان را از دست داده‌اند. اکنون تنها سوال این است که آیا ما پیش می‌رویم تا کار را تمام کنیم، یا اینکه آن‌ها یک سند را امضا خواهند کرد؟ باید ببینیم چه پیش می‌آید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75581" target="_blank">📅 20:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HPJX0P9XQHNX-wQi7mChWxBYo57xLktaAlSzhQArDpveG7FA41ZPz3mynM9a9YF0Z8vAiVyOWg2Ja0s7MHXvEzfcdte9qrQ0jj3FbERlpy_siMTn4RcZ7A_Kb7K6Y7g0NVY-1Zncb2EpAbdK5hXSeq07hND-cdrYRzgYR334F-canCvtWbVkII2I5qFjMiUz4mvG2_acq_9L7EgQHjfSojbzk6-OgV_PklTR_88Ri2DZr4puoUVVBCj6N2rlUcSB1o05qTstcxj7OlZjzro7eDKc0JkZsuYfv0KbT-ZhDge9dpUBIjVVPt68qrJtfKY4sO1mKMqQDa4DrZjTx_c8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت، چهارشنبه ۳۰ اردیبهشت پس از اظهارات خوش‌بینانه دونالد ترامپ درباره مذاکرات با جمهوری اسلامی بیش از پنج درصد کاهش یافت.
بهای نفت برنت به ۱۰۵ دلار و ۷۰ سنت رسید؛ زیرا معامله‌گران به نشانه‌هایی واکنش نشان دادند که حاکی از نزدیک‌تر شدن واشینگتن و تهران به توافقی است که می‌تواند از دور تازه حملات جلوگیری کند و نگرانی‌ها درباره اختلال طولانی‌مدت عرضه در خاورمیانه را کاهش دهد.
ترامپ گفت مذاکرات با جمهوری اسلامی در «مراحل نهایی» قرار دارد، اما هشدار داد اگر تهران با توافق صلح موافقت نکند، آمریکا ممکن است حملات بیشتری انجام دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75580" target="_blank">📅 20:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la5WpLLLfdBJ4NhhAxLkI9YLKFl_SsKSROe8bv4PZeuEJlRpAvbfRvnhRiXckaNxn2Xh1gBUaUJOE8HE6e9WvuRp4Mv_F60zwGR-yVArEW5_h5rwLK_fG9wh02lih3x7XLMAeCr25qNq4AL7n9gHtKUg7zJULyDwwb7a9Al4WizOElNyPmFMceQtkxWfCsaH_crKHCISOGLdSFem51FpkU_mMACCChPYb6QoLseG7bs_9lhJHKrXoHAsluPA_jRH6DfsOpBoZvCMRntmVLsOlKurc_HCP-7QM4nbyff_I8Se_YG22XihuWcITWrRZp4hn0Ar4k0dJ4Z2DcWC9CdVxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیصل بن فرحان، وزیر خارجه عربستان سعودی، نوشت ریاض از تصمیم رییس‌جمهوری آمریکا برای دادن فرصت دوباره به مذاکرات با جمهوری اسلامی به‌منظور دستیابی به توافقی که به پایان جنگ و بازگشت امنیت و آزادی کشتیرانی در تنگه هرمز به وضعیت پیش از ۹ اسفند ۱۴۰۴ منجر شود، قدردانی می‌کند.
او همچنین از تلاش‌های مستمر پاکستان برای میانجی‌گری در این زمینه تقدیر کرد و در شبکه ایکس نوشت عربستان سعودی امیدوار است جمهوری اسلامی از این فرصت برای جلوگیری از «پیامدهای خطرناک تشدید تنش» استفاده کرده و فورا به تلاش‌ها برای پیشبرد مذاکرات پاسخ دهد.
وزیر خارجه عربستان سعودی افزود هدف از این تلاش‌ها، دستیابی به توافقی جامع است که صلح پایدار در منطقه و جهان را محقق کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/75579" target="_blank">📅 19:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=MGRmrxdZqMht8gMjQYxqD35bu2HAwi2V57VUU70LTu_beCKdE2CUg602YlIywyMdVOpZl63umZF2X4zBg_RPXtRapp7D2NMkk0oOpvNZr1wiJ2bpN40Xk2Eaglg1G2fsisy2uy1T4ILF0YJWl8Zl6vXxK9L5t3fhKkeR-zAqTVNfzXTb0Ku8ecEA_BOP2sOchCXcyg_A2-QT1pFp3XOEa2jG5GoLtEWXU6OBlhHIjsTA_bykLgoLyC4j0oadDxnS5bO7Saa2i1fEV3R1McDu_oELJP2jVQ6QZ8nKkF79K8QRj8SYmcc-MdM0RS__5OG5XXZEvGLo_zeu_ER41z1jZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c1cd69554.mp4?token=MGRmrxdZqMht8gMjQYxqD35bu2HAwi2V57VUU70LTu_beCKdE2CUg602YlIywyMdVOpZl63umZF2X4zBg_RPXtRapp7D2NMkk0oOpvNZr1wiJ2bpN40Xk2Eaglg1G2fsisy2uy1T4ILF0YJWl8Zl6vXxK9L5t3fhKkeR-zAqTVNfzXTb0Ku8ecEA_BOP2sOchCXcyg_A2-QT1pFp3XOEa2jG5GoLtEWXU6OBlhHIjsTA_bykLgoLyC4j0oadDxnS5bO7Saa2i1fEV3R1McDu_oELJP2jVQ6QZ8nKkF79K8QRj8SYmcc-MdM0RS__5OG5XXZEvGLo_zeu_ER41z1jZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس ایران گفت که «تحرکات آشکار و پنهان دشمن نشان می‌دهد که به موازات فشارهای اقتصادی و سیاسی از اهداف نظامی خود دست نکشیده و به دنبال دور جدیدی از جنگ و ماجراجویی جدید است.»
او این اظهارات را در سومین پیام صوتی خود مطرح کرد و با اشاره به گذشت یک ماه از آتش‌بس، فضای سیاسی پیرامون دونالد ترامپ، رئیس‌جمهور ایالات متحده را از عوامل تأثیرگذار بر تصمیم‌گیری‌های او در قبال ایران دانست.
قالیباف در این پیام، با تاکید بر تداوم فشارهای اقتصادی و سیاسی، گفت که هدف این فشارها واداشتن ایران به عقب‌نشینی است، اما به ادعای او ساختار نظامی کشور برای بازسازی توان عملیاتی خود از فرصت این دوره یک‌ماهه آتش‌بس استفاده کرده است.
در بخش دیگری از این پیام صوتی ۱۲ دقیقه‌ای، رئیس مجلس ایران با انتقاد از برخی جریان‌های سیاسی، آنان را به «نادیده گرفتن شرایط امنیتی» و تمرکز بیش از حد بر نقد دولت متهم کرد و گفت که طرح این انتقادات می‌تواند به انسجام ملی آسیب بزند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/75578" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=jZ7X6UIvsLsehUEIx_knzumHJB-rSdLdORNqqhRDRX9rl6AogkpIKuMl_Mhm_u4PSHnZ4S7_ccLf7k5vUPwafp2KCSDxLJmi1xG0z-rMCQD0PYfvL_8zoD9L980K09rEZ-Zp4X8jJ-4kDJov_TXfLmLHXbBljsg3GntGXrCvzmQ4AU2ZXQtBzJ2WEVM0lg8LFZoh7Qyf61Q0-PkSnnpqTBi5BXw0H2juMt_G66E4HNF8XH4NTaAF-RK2bg9dkl_Orh7reTzXPjkhWdEjzgPpj7IjGp0WsEOAU2aKp5kN32V9GUugnDGTS2NQz1CUj79r6ZBantnagXq7LIclR6Cd_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0e7e12e55.mp4?token=jZ7X6UIvsLsehUEIx_knzumHJB-rSdLdORNqqhRDRX9rl6AogkpIKuMl_Mhm_u4PSHnZ4S7_ccLf7k5vUPwafp2KCSDxLJmi1xG0z-rMCQD0PYfvL_8zoD9L980K09rEZ-Zp4X8jJ-4kDJov_TXfLmLHXbBljsg3GntGXrCvzmQ4AU2ZXQtBzJ2WEVM0lg8LFZoh7Qyf61Q0-PkSnnpqTBi5BXw0H2juMt_G66E4HNF8XH4NTaAF-RK2bg9dkl_Orh7reTzXPjkhWdEjzgPpj7IjGp0WsEOAU2aKp5kN32V9GUugnDGTS2NQz1CUj79r6ZBantnagXq7LIclR6Cd_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، پیش از ترک واشنگتن به مقصد کانتیکت، در گفتگو با خبرنگاران در فرودگاه به تشریح وضعیت تقابل با ایران و گزینه‌های روی میز پرداخت.
او با اشاره به وضعیت داخلی ایران مدعی شد: «در حال حاضر خشم زیادی در ایران وجود دارد، زیرا مردم در شرایط بسیار بدی زندگی می‌کنند. ناآرامی و تلاطمی در آنجا جریان دارد که قبلا نظیرش را ندیده‌ایم؛ باید دید چه پیش می‌آید.»
ترامپ در پاسخ به سوال خبرنگار درباره احتمال انجام یک «توافق محدود برای تمدید آتش‌بس» گفت: «ما این شانس را امتحان می‌کنیم. من عجله‌ای ندارم؛ هرچند موضوع انتخابات میان‌دوره‌ای مطرح است، اما در حالت ایده‌آل ترجیح می‌دهم به جای افراد زیاد، آدم‌های کمتری کشته شوند.»
رئیس‌جمهوری آمریکا همچنین با ابراز تردید درباره نیت مقامات تهران گفت: «من متعجبم که آیا آن‌ها واقعا خیر و صلاح مردم خود را می‌خواهند یا خیر؛ رفتار آن‌ها نشان می‌دهد که به فکر مردم نیستند، در حالی که باید خیر و صلاح کل منطقه را در نظر بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75577" target="_blank">📅 18:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Iv24bJYc-stnBP8mt_Z3tPgCUiFpk3Z97HgapZ93KlfNCTkr5zECRKTrwatvucDpzLEMTdUi016W3RZX9E6er4y0QTZ099jQAovFSOSKY1mCHoyd1zbXgtsM4Vm_ZYH2Hof9Y4IJgJL2R4Rv059kifGKTHWciE6GWSQVbkqD2HJdWZTbGSn3vP9XKNIePOOz6O_8fa2jfpNOPGiiY1Rl6s6agC8rEKQqyts6fHvANK7MK7za4Nwf9dmituF5hM9fiWvHtyHJv1Z3DuPBe4hJwXA2Y11abvjk7OrzkXGLqEe8wSYh5JOXBKIaegtSidcCxGTIl7FZfoZZr5RWUZJSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jWyVwQKVF9gdR1bkX3azIIvo-aFXw78g42j6_ogy9J7XzoXAokPi6eHLvn99dQNKjwGQ0v8kE4rXpLqp416gzVZTOntOTlEsEfBtWmPoDBMXLzAAOev_UOZ2yuVPguOlI2jMVSr9zKTY5WHsCRI2wXEv6QgY3qdttVC2XY7hPWT9PhTucgqV6GSjofDjjvrqaHNQGnim_T50eCo6pvkkwoBnpmnk9rLrAbskNcS7-ZAIHCCxScpY9VQqHF8FmmGdA8HeHRJV2Sn43umL8ZzhD7kx5VQaGKsf5UGw3Tgmi-eTQyeV44yzdiBGVZlP-pTJCcvRHk_qYFWfPWpkxmSlzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=A9xSowbZWyGmMHQGxZ-6iC86oKGiBuWi526Hm0hZ1TVNWqaNiFso_2L_Hg3bIuk4NF3Wotxqw5OKpX8gyzwTTalBIFbLvyDLK9Y1U0lR_HAhqOnXYvvU35VvpOhz6DsWNXm8ckYtNd7yQka_Gu4uDjdnlFRQE72taUNRox4nCQipUR80Zaq-bdKCCNJUoC3DJOoPMac8N2veXggum0xUMtdtdGsnXFnrnrwLMry7HHYO_9NmAMJj0Vdlw7Z7VR8Ys_tquB2pm-01Dhffv8RAjDElpmBeQLQnotbftxeD736HcURx6SOB5N2qm5bes3jCM9iuzEqEAJ3fp7c27qIyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b8d594fa0.mp4?token=A9xSowbZWyGmMHQGxZ-6iC86oKGiBuWi526Hm0hZ1TVNWqaNiFso_2L_Hg3bIuk4NF3Wotxqw5OKpX8gyzwTTalBIFbLvyDLK9Y1U0lR_HAhqOnXYvvU35VvpOhz6DsWNXm8ckYtNd7yQka_Gu4uDjdnlFRQE72taUNRox4nCQipUR80Zaq-bdKCCNJUoC3DJOoPMac8N2veXggum0xUMtdtdGsnXFnrnrwLMry7HHYO_9NmAMJj0Vdlw7Z7VR8Ys_tquB2pm-01Dhffv8RAjDElpmBeQLQnotbftxeD736HcURx6SOB5N2qm5bes3jCM9iuzEqEAJ3fp7c27qIyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت امور خارجه جمهوری اسلامی، روز چهارشنبه ۳۰ اردیبهشت‌ماه درباره گمانه‌زنی‌ها راجع به سفر عباس عراقچی به نیویورک گفت:  «وزیر خارجه ایران برای شرکت در نشست شورای امنیت سازمان ملل درباره صلح و امنیت بین‌المللی دعوت شده، اما حضور او هنوز قطعی نیست.»
به گفته سخنگوی وزارت امور خارجه جمهوری اسلامی «این نشست به ریاست دوره‌ای چین در شورای امنیت، روز پنجم خرداد برگزار خواهد شد، اما با توجه به برنامه کاری فشرده وزیر امور خارجه»، تصمیم نهایی درباره سفر هنوز گرفته نشده است.»
این اظهارات پس از آن مطرح شد که علی خضریان، عضو کمیسیون امنیت ملی مجلس، در یک برنامه تلویزیونی نسبت به احتمال سفر عراقچی به نیویورک برای مذاکره درباره تنگه هرمز انتقاد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/75574" target="_blank">📅 18:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gcDEA7JRu1MZ9KNeS09W60b3mn7ZcJJ7NG2LCCi0hHIXqxY-kS7RpwVrNbevxzguKfMbehPOhs2Zc_KZx8zqQqRVIXy80jXF3jyQEIEjbzifEIf6ylQI-mXtvhE8b6UGsJ6UGLzb6YaLx0b2n275Bvr7R-TUQVvevI8DWf9afbIQNha0PfgzGtBEaMmThw2L-3vVP5jEvKXgtHLKAAqFN4Nu3UiBbVRlrXLGCTnKYyjz97EoBGqsqxuXa28FLrBnabACvgZ7yWQFCxBimw1DXgym11VJzV3nRlBh1VoxoYhpmVcD32xiCdTWRK2bHLGKHYSbJJ3TnU1A8QxsxulmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eMq4yUazucNnAswcztErceHTJMgSV6UNu-Dk_QRqgwF5q0lhh-hQ6SnaiamdBlTAJ0q6u0VzpUHcamzZnf2kaIJomZUn40t0_DsTtYTktmzaTIDp1yv8jz1_UrEKl6h3tqFe_mYVgomenIonG7Ab6JckyJTBOsZX-14i5JTGaaXpRtlfcqnyKveU7RQEJ6XONAbErB_jX5OMCr90nK948fHYCJ45uSFNaEllsr07Gn9YD4HY-RzSd8eAgFci5noQb1U6o23yX3LoPwRt1uNrdH_7PSLIM5uavxL1q7argSDnwwe5TNkJiNqTONsNK2EixPgCoGPY2UZ6HyR8Im97cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری قوه‌قضائیه گزارش داد رشید مظاهری، دروازه‌بان پیشین تیم ملی فوتبال و استقلال تهران، «هنگام تلاش برای خروج غیرقانونی از مرزهای غربی ایران بازداشت شده است.»
میزان در این گزارش رشید مظاهری را متهم کرده که «قصد داشته با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از کشور خارج شود.»
قوه قضائیه به زمان بازداشت این بازیکن پیشین تیم ملی فوتبال ایران اشاره نکرده است.
رشید مظاهری پس از کشتار معترضان در ۱۸ و ۱۹ دی، با انتشار ویدیویی در پنجم اسفند، علی خامنه‌ای را مسئول کشته‌شدن معترضان معرفی کرده بود. پس از انتشار آن ویدیو، تا مدت‌ها خبری از وضعیت او منتشر نشده بود.
خبرگزاری میزان گزارش کرده که مظاهری در «بند عمومی زندان» به سر می‌برد و قرار است به اتهام‌های «پرداخت رشوه به مامور دولت»، «فعالیت تبلیغی برخلاف امنیت ملی در شرایط جنگی» و «اقدام به عبور غیرمجاز از مرز» محاکمه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 233K · <a href="https://t.me/VahidOnline/75572" target="_blank">📅 17:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hX17pwXg7HSEQucXu00Q16olsBsrdaSslgvTM5VjpwO1HbwyXUq4gbdIkNuTvmQ01000grqMASiv7iF7QLmpiHZ4HbayakIrZKlbOJ3pp7_hwwmZNHlWEPU4NN4trnfM4eisXmNLsarAL7X2a-Z6POLM6lR-WIv9100BQPUwD6gfaYe6dqew5D3Z6-hJvyzWEmlLPVH4FyDZbS_3czD5t82OAwZYKIVgCvZXfdUOSahpkURUo0SD0BIpJa5wI1yMFhlUti-witRbpymTekfc4v1iWZouUCVp1odOJ85oOKtV6jlwse4fyOyAtvx-9Jaze8wdII3-tEhT2UyRo5vzFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در میانه اختلال در مسیرهای رسمی تجارت و فشار بر زنجیره تأمین صنایع، سازمان توسعه تجارت ایران واردات برخی مواد اولیه پتروشیمی و پلیمری را از طریق رویه‌های کولبری و ملوانی مجاز اعلام کرد.
این تصمیم نشان می‌دهد بحران تأمین مواد اولیه در صنایع پایین‌دستی به مرحله‌ای رسیده که حکومت برای جبران کمبود، به مسیرهای مرزی و غیرمتعارف متوسل شده است.
اما این تصمیم پرسش‌های جدی ایجاد می‌کند. مواد اولیه پلیمری و پتروشیمی کالای مصرفی ساده نیستند؛ واردات آنها نیازمند حجم بالا، کنترل کیفیت، استاندارد، ردیابی منشأ، بیمه، حمل‌ونقل تخصصی و تسویه تجاری منظم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/VahidOnline/75571" target="_blank">📅 17:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUdj6nYVVjoHVmWTF43cV94g-d0HEJzwEn6DxGJywxaw_iqJKYcpRFWnzmnyuwjTFGCvHJhNUxEzSjO8mfz8-TZQ3UahDhDdclFcnc3O-_9_4_b0hKAM41nAuNXl9Onh_OAErrMGeC_WZS6JFclLELdWIlCf0gVCjvTIBHaUIHn7A0kLrrmCm5RJHhfodeJL0Cb5jzdk4e7F4SaJct9slbqTw0Tehe4TP593X-tUoHwZD50EmPpfDIpnj5XgboZoxTxsbJSkW0f_4q7_QS6n-3R94MbGzJFP2diUkg9yNEoM2KDpVLWV_SPg3VOY44skraejTKqdljKvjJYdBoaHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران با انتشار بیانیه‌ای تهدید کرده که در صورت آغاز دوباره جنگ آمریکا و اسرائیل علیه ایران، جنگ «به فراتر از منطقه کشیده خواهد شد.»
در این بیانیه با اشاره به تهدیدهای دونالد ترامپ و مقام‌های اسرائیل برای حمله مجدد به ایران آمده: «اگر تجاوز به ایران تکرار شود جنگ منطقه‌ای که وعده داده شده بود، این بار به فراتر از منطقه کشیده خواهد شد و ضربات کوبنده ما در جاهایی که تصور آن را ندارید شما را به خاک سیاه خواهد نشاند.»
عباس عراقچی، وزیر خارجه ایران هم در واکنش به اظهارات تهدیدآمیز دونالد ترامپ، رئیس‌جمهور آمریکا، درباره احتمال از سرگیری حمله نظامی به ایران، در شبکه ایکس نوشته «با درس‌هایی که آموخته‌ایم و دانشی که به دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/75570" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRZJG0ogyKqAhXiR2Z8rCg0N5xf86mjWxKau6PWOgZavxdCWqgJcuz4B4a-v1sCTAYw3AlHD9yRP2n3me_EDF-lE96dzm9fSVzGh-EvXD11uC4unj2e1oBoFn7sklvnmX3WEV00Ozgz4VRuOAiuZZtirHH_gdkCpAi07SPzcVIvGWoIZ72GUzXQuK25nFRLF8SNeVx6oide-mWNoaikPpDQnOR-Mjk3HuB_oyycSh5YMh1wJglbqja_l5OYw3X7mPomg0ZWrQmMqyXg4SIfn32EnbMWXT5EDcYP8tvbTUNX4_KbsGskXr7DpidX_ifXXuRgHy-AhjsB5y7T9cUxa9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران روز چهارشنبه ۳۰ اردیبهشت خبر دادند که محسن نقوی، وزیر کشور پاکستان، وارد تهران شده است. او روز ۲۶ اردیبهشت نیز به ایران سفر کرده بود.
خبرگزاری ایسنا اعلام کرده که برنامه و اهداف سفر این مقام ارشد پاکستانی در ایران «مشخص نیست». خبرگزاری تسنیم نیز گزارش داده که آقای نقوی در بدو ورود به تهران با وزیر کشور ایران دیدار کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/75569" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nwfzr5D6hXAMMCYvHRlzpa7f-7nuARMSiXKemip1C91i5mkoUvJpoq58ZiG_MG3R5J-lvAC9IHbX0jwDM1vf3mK3ObSvb3kU4YjmVM6O961IGjqaa9I7wa7mMAK4KIRVUtsqrW7RJUppwWk4_97fML0GgXsn7aVS5_IKPyNW1c8uxQJfp8PPzIsg6v82v1tOX6oDzPXOoxCaf0KM0rSrhKvcBuWjvHTw2noU2JDytI0wxKTub98fcbQ3E46Jmw7hdXPfJsqA3y7jAWVPD0sGfiS49BUDN4mU4WzIIQ_nWpM0g0EgoplnuZdD0jWHKJG3Sdelen1ZJrBO2A4jHx00Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها در ایران از اجرای حکم اعدام قاتل الهه حسین‌نژاد، که جسد او اوایل خرداد سال گذشته در بیابان‌های اطراف تهران پیدا شد، خبر می‌دهند.
عصر چهارم خرداد ۱۴۰۴ الهه حسین‌نژاد ۲۴ ساله از سالن زیبایی که در آنجا مشغول به کار بود، بیرون آمد تا به خانه‌اش در اسلامشهر برود، اما ناپدید شد و وقتی خانواده‌اش اعلام شکایت کردند بررسی‌های تیم جنایی نشان می‌داد الهه از میدان آزادی سوار یک خودروی عبوری شده است.
جست و جوها برای یافتن الهه سرانجام پس از ۱۱ روز نتیجه داد و با دستگیری راننده خودرو به نام بهمن ۳۷ ساله و اعتراف به قتل الهه، جسد او در بیابان‌های اطراف تهران پیدا شد. متهم نیز پس از محاکمه به اعدام محکوم شد.
این قتل جنجال زیادی درباره امنیت زنان در ایران به پا کرد و تا مدت‌ها رسانه‌ها درباره آن مطالب مختلفی منتشر می‌کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/VahidOnline/75568" target="_blank">📅 17:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rPgNwIgDUVW1WcBzMueTAJoIk6X-DTzXF_Z1uBqeilsPnX4xUqv9c4h8HFxxECtcUbCQZz9L4lkqmGzhuG6DOJiq9esEOfQAuCGYaZJmA0_zTLY5n2omBAGR-lWtPHci6bGwhU5UPyuiy62byWoVVfthIr--pEK40tTSrOJy4e6yfmaL85s3kglESlhZhYpIZyN0cqXcSkpSiOPhJua_UEI1t05GZSnITbO6tbSuXW1gFHhhbJM6r3NydX-04x5SoqOGZK9QqrGMOsoK4MKPZknw1x-H398pdBuDq8Y4k0Z3vowc4jIb_Ay2mPpeitR9yIwUdLajBzLOvLc40cVIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حقوق بشری گزارش دادند دادگاه کیفری تهران پس از رسیدگی دوباره به پرونده شهرک اکباتان، سه معترض بازداشت‌شده در این پرونده را به دیه و پنج سال حبس محکوم و سه معترض دیگر را از اتهام مشارکت در «قتل عمد» تبرئه کرد. حکم اعدام این شش تن پیش‌تر در دیوان عالی کشور نقض شده بود.
سایت هرانا چهارشنبه ۳۰ اردیبهشت گزارش داد شعبه ۱۳ دادگاه کیفری یک استان تهران، میلاد آرمون، علیرضا کفایی و امیرمحمد خوش‌اقبال را بابت اتهام «مشارکت در قتل عمد» آرمان علی‌وردی، از نیروهای بسیج، محکوم کرد. هر یک از آن‌ها به پرداخت سهم مساوی از دیه کامل یک انسان و پنج سال حبس محکوم شده‌اند.
طبق گزارش هرانا، نوید نجاران، حسین نعمتی و علیرضا برمرزپورناک، سه متهم دیگر این پرونده، به دلیل «فقدان مدارک دال بر وارد کردن ضربه به ناحیه مشخصی از بدن علی‌وردی» از اتهام مشارکت در قتل عمد تبرئه شدند.
این حکم ۱۵ بهمن سال گذشته صادر و سه‌شنبه ۲۹ اردیبهشت به وکلای این افراد ابلاغ شده است.
این شش شهروند معترض در آبان ۱۴۰۳ از سوی همین شعبه به اعدام محکوم شده بودند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75567" target="_blank">📅 17:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=v2AZkw_-6hsvau68m2U00HRGDDmUC_g7bRe4GWXhnv-cflPmF-exLK8tLJq3RonBimXaQogZLl1fT_QTCgbP98vhF-UeNbFOaCi7fUwrEQsi5clYGbyENzZ1Yua50AKzv1tp3d5m9vgXuLjAkiKCkehu23j94UalJn7jJTaKVD7WEXeYkjZro9r5xlzlhKu89LdMWvtEI0kHRuRTg4DrH4gmswHSj81OggCWvJFEEkyM8j81ZaE9zWktaVrZJZchY2AjZpg8HmLPUjLg5_-EUUI2chK_bqxm9gXRVi300WtHASfcTvPXruJRWOLycJaJ1GlvLodoCYwqhLedyZTiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4724dd573.mp4?token=v2AZkw_-6hsvau68m2U00HRGDDmUC_g7bRe4GWXhnv-cflPmF-exLK8tLJq3RonBimXaQogZLl1fT_QTCgbP98vhF-UeNbFOaCi7fUwrEQsi5clYGbyENzZ1Yua50AKzv1tp3d5m9vgXuLjAkiKCkehu23j94UalJn7jJTaKVD7WEXeYkjZro9r5xlzlhKu89LdMWvtEI0kHRuRTg4DrH4gmswHSj81OggCWvJFEEkyM8j81ZaE9zWktaVrZJZchY2AjZpg8HmLPUjLg5_-EUUI2chK_bqxm9gXRVi300WtHASfcTvPXruJRWOLycJaJ1GlvLodoCYwqhLedyZTiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین هم به خدمت شی رسید.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75566" target="_blank">📅 07:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75565">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gh-gkRVvwEMH0TLDm6jmDlav3lXzRJsNe85sFKIU89wpED63HUZVD7jcW2nEHr8lo8O9mLORxqnlRvZ4u6sl6zvJNzNTvox6JePM4ojfrkQgrlANbig5NppQMXfXf6vXollqGZBKCWkV0ifr0OR1eXV0d1sDyZyEGFObROVwtJxwOnjSmnyI62nNCEREp64pH6gOLMfMP-ayOKS-Fu84ZH-Gl47cNrmh2shNz8U00bpsajTHQXuwXRHQoxISdQabsQK8DjngTshLk2NHIV2GJccDYY-tilN5mwf8QjYYNncci4zeOv-6wdUHGefFT4gnN4qknggQDUeSA3SEUe4bjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین
تیتر نیویورک‌تایمز: هدف اولیه جنگ، روی کار آوردن رئیس‌جمهور تندروی پیشین به عنوان رهبر ایران بود
بخش‌های خبری مطلب:
به گفته مقامات آمریکایی، حمله اسرائیل که با هدف آزادی محمود احمدی‌نژاد از حبس خانگی در تهران طراحی شده بود، بخشی از تلاش‌ها برای تغییر رژیم و به قدرت رساندن او بود.
چند روز پس از آنکه حملات اسرائیل در آغازین روزهای جنگ، رهبر ایران و سایر مقامات ارشد را به قتل رساند، پرزیدنت ترامپ علناً اظهار داشت که بهتر است «شخصی از درون» ایران کنترل کشور را به دست بگیرد.
اکنون مشخص شده است که ایالات متحده و اسرائیل با در نظر داشتن شخصیتی خاص و بسیار غافلگیرکننده وارد این درگیری شدند: محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران که به دلیل دیدگاه‌های تندرو، ضداسرائیلی و ضدآمریکایی‌اش شناخته می‌شود.
اما بر اساس گفته‌های مقامات آمریکاییِ مطلع از این موضوع، این طرح جسورانه که توسط اسرائیلی‌ها تدوین شده بود و با آقای احمدی‌نژاد نیز درباره آن مشورت شده بود، به سرعت با شکست مواجه شد.
مقامات آمریکایی و یکی از نزدیکان آقای احمدی‌نژاد اعلام کردند که او در روز اول جنگ بر اثر حمله اسرائیل به خانه‌اش در تهران - که برای رهایی او از حصر خانگی طراحی شده بود - مجروح شد. آن‌ها گفتند که او از این حمله جان سالم به در برد، اما پس از این خطر جانی، نسبت به طرح تغییر رژیم دلسرد و ناامید شد.
او از آن زمان تاکنون در انظار عمومی دیده نشده است و مکان و وضعیت فعلی او نامشخص است.
...
اینکه آقای احمدی‌نژاد چگونه برای مشارکت در این طرح به کار گرفته شد، هنوز در هاله‌ای از ابهام قرار دارد.
...
سخنگوی موساد، سازمان اطلاعات خارجی اسرائیل، از اظهارنظر در این باره خودداری کرد.
...
مقامات آمریکایی گفتند که این حمله - که توسط نیروی هوایی اسرائیل انجام شد - به منظور کشتن نگهبانان مراقب آقای احمدی‌نژاد و به عنوان بخشی از طرحی برای رهایی او از حبس خانگی صورت گرفت.
این حمله آسیب چندانی به خانه آقای احمدی‌نژاد که در انتهای یک کوچه بن‌بست قرار داشت، وارد نکرد. اما پاسگاه امنیتی در ورودی کوچه مورد اصابت قرار گرفت. تصاویر ماهواره‌ای نشان می‌دهد که آن ساختمان ویران شده است.
در روزهای پس از آن، خبرگزاری‌های رسمی روشن کردند که او جان سالم به در برده است، اما «محافظان» او - که در واقع اعضای سپاه پاسداران انقلاب اسلامی بودند و همزمان وظیفه محافظت و نگهداری او در حبس خانگی را بر عهده داشتند - کشته شده‌اند.
مقاله‌ای در نشریه آتلانتیک در ماه مارس، با استناد به منابع ناشناس نزدیک به آقای احمدی‌نژاد، نوشت که رئیس‌جمهور پیشین پس از حمله به خانه‌اش از حصر دولتی آزاد شده است؛ این مقاله آن رویداد را «در عمل یک عملیات فرار از زندان» توصیف کرد.
پس از انتشار آن مقاله، یکی از نزدیکان آقای احمدی‌نژاد در گفتگو با نیویورک تایمز تأیید کرد که آقای احمدی‌نژاد این حمله را به عنوان تلاشی برای آزادی خود تلقی کرده است. این فرد مطلع گفت که آمریکایی‌ها آقای احمدی‌نژاد را شخصی می‌دانستند که می‌تواند ایران را رهبری کند و توانایی مدیریت «وضعیت سیاسی، اجتماعی و نظامی ایران» را دارد.
این فرد مطلع اظهار داشت که آقای احمدی‌نژاد می‌توانست در آینده نزدیک «نقش بسیار مهمی» در ایران ایفا کند و اشاره کرد که ایالات متحده او را شبیه به دلسی رودریگز می‌دید؛ کسی که پس از دستگیری آقای مادورو توسط نیروهای آمریکایی در ونزوئلا قدرت را به دست گرفت و از آن زمان همکاری نزدیکی با دولت ترامپ داشته است.
...
در چند سال گذشته آقای احمدی‌نژاد سفرهایی به خارج از ایران داشته است که به گمانه‌زنی‌ها دامن زده است.
به گزارش مجله نیولاینز، او در سال ۲۰۲۳ به گواتمالا و در سال‌های ۲۰۲۴ و ۲۰۲۵ به مجارستان سفر کرد. هر دو کشور روابط نزدیکی با اسرائیل دارند.
ویکتور اوربان، نخست‌وزیر مجارستان در آن زمان، روابط نزدیکی با آقای نتانیاهو دارد. در طول این سفرها به مجارستان، آقای احمدی‌نژاد در دانشگاهی مرتبط با آقای اوربان سخنرانی کرد.
او تنها چند روز قبل از آغاز حملات اسرائیل به ایران در ژوئن گذشته از بوداپست بازگشت. زمانی که آن جنگ درگرفت، او حضور علنی کمرنگی داشت و تنها چند بیانیه در شبکه‌های اجتماعی منتشر کرد. سکوت نسبی او در مورد جنگ با کشوری که آقای احمدی‌نژاد مدت‌ها آن را دشمن اصلی ایران می‌دانست، مورد توجه بسیاری در شبکه‌های اجتماعی ایران قرار گرفت.
...
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/75565" target="_blank">📅 06:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dRqw2ooHxKPGXIzYcePriu9pkPIhkgz-ADEBrI2ikqOuq79YTYhcKDhbGoke46bSeeV1_soRFi8ZWNz0pltQ1vKMQbxhZbn8Qo1R0LBsko5rBJxHOqjEkTDSkWbbYXH3kI13oPMGhMViffmB_pueLf0WA1W_8CCx5x59H2-kxDoLlLVTgIqgsOXjDeL5G7gIiXBh2e8JeSLqQDnaL1Msk1nBtmeWYIK2XSmMfpe558uQySdVzvyYmVLGHjscjIZU6CdIpUOdrvgr6y_QK2lfpam1jXwnUGg7B51airc9ajue5vEZHD27Y8Ojcrxuzbs3MqLLiGWdkWI4RThbB41qWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در یک سخنرانی در کاخ سفید گفت  ایران قرار نیست به سلاح هسته‌ای دست پیدا کند. نمی‌توانند سلاح هسته‌ای داشته باشند. ما نمی‌توانیم چنین چیزی را تحمل کنیم و آن را تحمل نخواهیم کرد.
او گفت ما نیروی دریایی آن‌ها را نابود کردیم. نیروی هوایی آنها از بین رفته است. سامانه‌های پدافند هوایی آنها از بین رفته است. تمام تجهیزاتی که برای جنگ استفاده می‌کردند از بین رفته است. تقریبا همه چیز از بین رفته است.
ترامپ افزود: نمی‌خواهم بگویم رهبران آنها از بین رفته‌اند، چون بیان آن چندان خوشایند نیست، اما واقعیت همین است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75564" target="_blank">📅 03:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75563">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HIU6hZtGY3FOZcVXtyC9JiJcNyIpkF-0SmE-9tbhoQd_UeH8Upy5VE6exAn9EK0RT3PJJbsA78cwrYZ2oNR0sebvnYHrhNvaI-4JtPyjRWR0FbO711eOCxfhgizqpu40Ic3SgIUsaI6O3QyfhDRpRAdF1SF5Jkmx7qMirR-1LOcd8aknFAEp7qTBKJdnoEGZNZHWCAw70JEAdH7H2QRdETw34e6A4WH1DeMTYYZYlbz4l5Q5bWikshk36sZXCrpPGlgoz1UD1ed0hkNxsYUO-VmPKXtLqNgPct9DHyibVE_yyL-OfOoDCTMcnCocWWX4jc0EsrWVou8MVuzBmSOu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه در قشم
آپدیت:‌
تصویر بالا:
#زلزله
به بزرگی ۴٫۷ در عمق ۲۰ کیلومتری بندر لافت در جزیره قشم هرمزگان
پیام‌های دریافتی:
سلام وحید دو زلزله شدید بندرعباس رو لرزاند
ساعت ۳:۱۱ دقیقه بندرعباس زلزله اومد
همین الان ساعت ۳:۱۲ دوبار به مدت ۱۵ ثانیه وحشتناک بندرعباس لرزید
من بندرعباس هستم دو بار لرزید
زلزله اومده خیلی بد بود
زمین لرزه نسبتا شدید ساعت ٣:١٠ بامداد بندرعباس
بندرعباس هستم فکر کردیم باز زدن دقیقا ۲۰ ثانیه همه جا میلرزید
چند دقیقه پیش زمین لرزه نسبتا شدید اومد دوبار تو فاصله خیلی کم بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75563" target="_blank">📅 03:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DzOfM3ECnRGFCrHNE6E0O9waDeRRVEWH_Lw-AteQzdfkn8K5E5Qz3r6OSiB2V2CmYlqssN9MhFNFyBOr1tIc_QoEiKDfrFCNPRYNDxqaONlNas7VYbP6Qt_ejVzio3jESOjpbc7YQnJg0JHmFt3M7gOL0v5osz2XWS8S2lRCcPhfe6PCM8n2feM3s5xl8FmnngErSz0A9S4zUUuGxqJlBwrRAsjNNxAqQ7ICs8Lqnz8-rzq7AHghRdA2igPDGFi6dFZ2-oNUSkvHdUTJPaEJ5iKBWbzVvRpe3HEROi_FByaRDF10z4mFKyoN-aluueuSFn3Q6L7z1CI-SjX6VSiH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا روز سه‌شنبه قطعنامه‌ای را برای توقف اقدام نظامی در ایران پیش برد.
پیش بردن این قطعنامه پس از آن صورت گرفت که سناتور جمهوری‌خواه، بیل کسیدی از لوئیزیانا، به آن رای مثبت داد. کسیدی چند روز پیش، در رقابت‌های درون حزبی ایالتی برای ادامه حضورش در سنا، به نامزدی که از حمایت ترامپ برخوردار بود، باخت.
به گزارش سی‌ان‌بی‌سی، با وجود اینکه قطعنامه اختیارات جنگی با نتیجه ۵۰ به ۴۷ به تصویب رسید، اما هنوز احتمال کمی برای تبدیل شدن به قانون دارد. این قطعنامه باید ابتدا در سنا به تصویب نهایی برسد، سپس مجلس نمایندگان به رای بدهد و سپس نیز، دونالد ترامپ به احتمال قریب به یقین، آن را وتو خواهد کرد.
@
VahidHeadline
چهار جمهوری‌خواه هم‌حزبی ترامپ همراه با همه دموکرات‌ها به جز یک نفر، به آن رای مثبت دادند. سه سناتور جمهوری‌خواه نیز در رای‌گیری غایب بودند.
باوجود تصویب این آیین‌نامه، حتی اگر قطعنامه‌ای در سنا با ۱۰۰ عضو هم به تایید برسد، کار دشواری در مجلس نمایندگان خواهد داشت که تحت کنترل جمهوری‌خواهان است و پس از آن نیز باید دو‌سوم رای کنگره و سنا را داشته باشد تا بتواند گزینه وتوی احتمالی رئیس‌جمهور را دور بزند.
طبق قانون اختیارات جنگی آمریکا مصوب ۱۹۷۳ که در واکنش به جنگ ویتنام تصویب شد، رئیس‌جمهور آمریکا تنها ۶۰ روز می‌تواند بدون مجوز کنگره عملیات نظامی انجام دهد و پس از آن باید یا جنگ را متوقف کند، یا از کنگره مجوز بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75562" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/czU-AlnxnMxA1NGqCnD_hXXoR1X7oV_XhZCqTDawOSQgXz4P48qeKfSTVnDYfbKEokbegYe_qo8oyeGz-fmjnHCFOcLKezeWYvuXrWnlJ1nZWqGkk8HniAvWMGxtgnK38owEqXGxLkb_LmVi5YJX0wvNN6XBmcZ0xnERGU-zprqv9UqdMA3UD97xh43juQY5IoScAkMnzTfDID9T2p39XamV7HQA5ub0F3B9TeRIGwu0w-p_hsDX2Kti06_5AJQuLlFT7yWseHVGuStRQ9wWw8GX_bKnOEVJnCwqqbjBpSZ-SXa1aveU6CvVF7Wmr56jqAzg9r6iGOIvNz4doGLaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UZzLp5fdpZqWzX39miqFxrGTkbdHa122844l7HUoyXYmh-axNGGxc9f5IIAGpjdBUV0fzuC9nedGaaWQYh9-AGL3BjpD3k2vFdhfqYS1Quym08Rdox6f_YD5vFQ4YSOMf5tL8JJtB9eh10-rwrMWM45mT0uiU52jHFztbY18hjsLbXI8riOclK9fizd4u1NwS3qSQn9QBh4IV4p-LkxukEVRTeF8CGoyH7Rbp16ETylFYfhb0wP0XkiZsa8546XflmRfdisuxPZiw0RDpOHzUwRmEh4blLo2JpiaJRR0rGY04obPaSwDjaByhL6DiyTQp7BthpcIDir-Svz01OscNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f9KWuyYefq8lgeBJpNMsGJk7MtCrhuHfNCF0LFn1wh1bsYscj1jMOR-GlI00EUI5DSIb4M33sSooRCZ0S1uUDUl0r58z9g388_SOGHUKN3uZ8TBew5rNeNOyMW2D8QJOWgBFXKoz1lSMTNfIOLpLu8izrEN101i29dXJv2g8XCCBnBQR8bcfrC9Dd1B53dflsbpXRB_zODe1Bf8LY2CpR5mkhc_GvuhXAXi1jxmaC5kPWQ4QNDfNbNR0xZ_e6O-AJF_1IAPFT5_8sHn0pM1OTwiCJTJQttfCQVa0HlpS_u_bj_qe8BFSV4AEQA5DyeNcacpax8_7BFBPvVyeeXgQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D1Y8hRCX_GmVQrKCqXmOz39yx5gWzSRvn_bzioeUs6Xb1usLT0OKfF9c7rfehE6n_X3wXDwPSC8lms_MtZuMqwAD8YhjiegeNaZy7s-0mWKmMZ8WyVPWB6OH_9FCNl4dCIlpV1xD-MGFi4XYwbi3dtTR4WzkkcLd3caUFAiswTxw3C8l_9ZGBW3QI5CH9MMdq_WgIMLzdxYISvmxdVffVSBUhuLQXZrt_a7Bmt3w1MFIElhuhriHobpwzWoFAEwxEdGzO452McCa7y29Epx3ZAftZ_DNjvYQrw_qm2oI7PZYGqPWCUl5TArIFwrAeGiAAzKgSYQLTFIpofVkQkbAaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=OEKX8K-YFwcCviPPwgyVid3s4blAoqVerOiY_j3WOJgg-C3CnUCKTFUV16PjJSfhT5bXxiz_HR-kot9QY73Szp7LBTvBm4zwSFMh_k__Js53zr4DdNe59it-2DoTWVRKNIT88O2eJV6ZhOCKd1vjr5pxAnySao67CdlnkAeZZVpZMfkMoRjXaRIP-s0_Qytd-gw0YIq620u6aHdrRdLsHxvNtoqiKyz7iFhsq4KIsMfBIkV4CEi61grW0S4C9hqidmxPdnGbKyiLVlMHE_GKtgwgCZtMOzehS-dpdltB1AFlBoTaVpOErq52V4mK-AxFkN8Qq9uov_sIl6ykb4lP4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=OEKX8K-YFwcCviPPwgyVid3s4blAoqVerOiY_j3WOJgg-C3CnUCKTFUV16PjJSfhT5bXxiz_HR-kot9QY73Szp7LBTvBm4zwSFMh_k__Js53zr4DdNe59it-2DoTWVRKNIT88O2eJV6ZhOCKd1vjr5pxAnySao67CdlnkAeZZVpZMfkMoRjXaRIP-s0_Qytd-gw0YIq620u6aHdrRdLsHxvNtoqiKyz7iFhsq4KIsMfBIkV4CEi61grW0S4C9hqidmxPdnGbKyiLVlMHE_GKtgwgCZtMOzehS-dpdltB1AFlBoTaVpOErq52V4mK-AxFkN8Qq9uov_sIl6ykb4lP4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهور آمریکا، گفت واشینگتن و تهران پیشرفت زیادی در گفت‌وگوهای خود داشته‌اند و هیچ‌یک از دو طرف خواهان ازسرگیری کارزار نظامی نیستند.
ونس افزود: «ما فکر می‌کنیم پیشرفت زیادی داشته‌ایم. تصور می‌کنیم مقام‌های تهران نیز می‌خواهند به توافق برسند.»
او گفت آمریکا می‌تواند کارزار نظامی را از سر بگیرد، اما «این چیزی نیست که ترامپ یا ایران می‌خواهند.»
ونس همچنین گفت: «فکر می‌کنم جمهوری اسلامی می‌خواهد توافق کند، اما تا زمانی که توافق امضا نشود، نخواهیم دانست.»
@
VahidOOnLine
جی‌دی ونس اعلام کرد که دولت ترامپ برای دستیابی به توافقی جهت پایان دادن به جنگ تلاش می‌کند، اما او همچنان شاهد وجود شکاف و گسست در میان سران ایران است و موضع مذاکراتی تهران شفاف نیست.
معاون رییس‌جمهور آمریکا گفت: «خودِ ایرانی‌ها هم دقیقا مطمئن نیستند که می‌خواهند در چه مسیری حرکت کنند؛ آن‌ها در حال حاضر کشوری چندپارچه و دارای شکاف هستند.»
او در ادامه افزود: «در ساختار حاکمیتی این کشور، رهبر وجود دارد و در رده‌های پایین‌تر از او نیز مقامات زیادی هستند که بر روند مذاکرات نفوذ دارند. به همین دلیل، گاهی اوقات اصلا مشخص نیست که موضع واقعی تیم مذاکره‌کننده چیست.»
ونس  با اشاره به اینکه هنوز روشن نیست این تشتت آرا ناشی از ضعف در هماهنگی است یا سوءنیت، تاکید کرد که نتیجه این وضعیت، ایجاد فرآیندی مبهم و سردرگم‌کننده بوده است. ونس در پایان گفت: «با اطمینان می‌گویم که گاهی درک این نکته که ایرانی‌ها دقیقا می‌خواهند از این مذاکرات به چه هدفی دست یابند، بسیار دشوار است.»
@
VahidOOnLine
جی‌دی ونس گفت اعضای تیم مذاکره‌کننده جمهوری اسلامی برخی ویژگی‌های ایرانیان، از جمله «هوش و سختکوشی» را دارند، اما همزمان مواضع «بسیار تندروانه» نیز در میان آن‌ها دیده می‌شود.
معاون رئیس‌جمهوری آمریکا با توصیف ایران به‌عنوان «تمدنی بزرگ و پرافتخار» گفت مردم ایران «شگفت‌انگیز» هستند و جامعه ایرانی-آمریکایی در ایالات متحده نیز نمونه‌ای از این ویژگی‌ها را نشان می‌دهد.
او در عین حال افزود گاهی مشخص نیست تهران دقیقا چه هدفی را از مذاکرات دنبال می‌کند و ساختار تصمیم‌گیری در جمهوری اسلامی را «چندپاره» توصیف کرد.
ونس همچنین بار دیگر تاکید کرد واشنگتن اجازه نخواهد داد جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند و هدف مذاکرات، جلوگیری بلندمدت از بازسازی توان هسته‌ای جمهوری اسلامی است.
@
VahidOOnLine
جی‌دی ونس اعلام کرد: «فکر می‌کنم ما در حال حاضر فرصتی داریم تا رابطه‌ای را که طی ۴۷ سال گذشته بین ایران و ایالات متحده وجود داشته است، بازتنظیم کنیم.»
معاون رئیس‌جمهوری آمریکا که در نبود کارولین لویت، سخنگوی کاخ سفید، مسئولیت نشست خبری روزانه را بر عهده داشت، در ادامه افزود: «این همان چیزی است که رئیس‌جمهوری از ما خواسته و ما به تلاش در این مسیر ادامه خواهیم داد. اما برای این کار، همراهی هر دو طرف لازم است (یک دست صدا ندارد).»
ونس با تبیین خطوط قرمز واشنگتن تاکید کرد: «ما به توافقی که به ایرانی‌ها اجازه دسترسی به سلاح هسته‌ای را بدهد، تن نخواهیم داد. بنابراین، همان‌طور که رئیس‌جمهوری ترامپ به من گفت، ما در حالت آماده‌باش کامل نظامی هستیم. ما تمایلی به پیمودن این مسیر [از سرگیری جنگ] نداریم، اما اگر مجبور شویم، رئیس‌جمهوری آمادگی و توانایی پیشبرد آن را دارد.»
@
VahidOOnLine
ونس افزود که به‌تازگی با آقای ترامپ صحبت کرده و رئیس‌جمهور آمریکا تأکید کرده است که مسئله اصلی برای آمریکا این است که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند.
ونس یادآوری کرد که اگر چنین اتفاقی بیفتد، کشورهای حاشیه خلیج فارس نیز به‌دنبال سلاح هسته‌ای خواهند رفت و سپس کشورهای دیگر جهان هم همین مسیر را دنبال خواهند کرد.
او گفت: «ما می‌خواهیم تعداد کشورهایی که سلاح هسته‌ای دارند محدود باقی بماند، و به همین دلیل ایران نمی‌تواند سلاح هسته‌ای داشته باشد.»
وقتی از ونس پرسیده شد که آیا ممکن است روسیه مالکیت اورانیوم غنی‌شده ایران را در اختیار بگیرد، او پاسخ داد: «این در حال حاضر برنامه دولت ایالات متحده نیست. ایرانی‌ها هم چنین موضوعی را مطرح نکرده‌اند.»
@
VahidHeadline
جی‌دی ونس همچنین گفت واشینگتن می‌خواهد جمهوری اسلامی فرایندی را بپذیرد که تضمین کند ایران حتی سال‌ها بعد از دوران ریاست‌جمهوری ترامپ هم نتواند توان هسته‌ای خود را بازسازی کند.
او گفت: «ما می‌خواهیم نه فقط تعهد به عدم دستیابی به سلاح هسته‌ای را ببینیم، بلکه می‌خواهیم تعهدی برای همکاری در یک فرایند ببینیم تا اطمینان حاصل شود که نه فقط اکنون، نه فقط وقتی دونالد ترامپ رئیس‌جمهور است، بلکه سال‌ها بعد هم ایرانی‌ها به دنبال بازسازی توان هسته‌ای خود نباشند.»
او افزود: «این چیزی است که ما در مذاکرات در تلاش برای رسیدن به آن هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75556" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=vHRILnOsKoj9uZa0E5D4COyPugd5lO0ZgEnPxm26rOfZW-d125XH_bVIgJWjas85SWzFaGgvDJdOItJaw47periWFPS-sEZcNfFTq4NWQX9Q0rIovB_S-_98aMstRWPHoGJZ0D8F6zGrxPqgoJiRbLN19ZCddiNwb7LY07FjI5UjKRWaVxFWATP18tXRnIbMR_ppNmP8B6r4e-8iQBf8QIdoOcUeUYLnkfWgLZzNPSma1l0_AaWDPedcXRI5K3rQnM7G0t05ow8F7v62PnlvRj8r6jgRH3soO-bcBY8ItERXgH19l5xTbR0ocAR3SY1c-2KS_Uw2zpv6oQ4lsDsXuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=vHRILnOsKoj9uZa0E5D4COyPugd5lO0ZgEnPxm26rOfZW-d125XH_bVIgJWjas85SWzFaGgvDJdOItJaw47periWFPS-sEZcNfFTq4NWQX9Q0rIovB_S-_98aMstRWPHoGJZ0D8F6zGrxPqgoJiRbLN19ZCddiNwb7LY07FjI5UjKRWaVxFWATP18tXRnIbMR_ppNmP8B6r4e-8iQBf8QIdoOcUeUYLnkfWgLZzNPSma1l0_AaWDPedcXRI5K3rQnM7G0t05ow8F7v62PnlvRj8r6jgRH3soO-bcBY8ItERXgH19l5xTbR0ocAR3SY1c-2KS_Uw2zpv6oQ4lsDsXuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهور آمریکا سه‌شنبه به خبرنگاران در کاخ سفید گفت ممکن است مجبور شویم دوباره به  ایران ضربه بزنیم، مطمئن نیستم.
او گفت منظورم این است که دو یا سه روز، شاید جمعه، شنبه، یکشنبه، چیزی در این حدود، شاید اوایل هفته آینده؛ یک بازه زمانی محدود، چون نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای جدید داشته باشند.
رییس‌جمهور آمریکا ادامه داد که او دوشنبه تنها یک ساعت با تصمیم‌گیری برای انجام یک حمله فاصله داشت، اما این حمله را به تعویق انداخت.
او افزود جمهوری اسلامی برای رسیدن به توافق التماس می‌کند.
ترامپ درباره جنگ گفت: «همه به من می‌گویند این کار محبوب نیست، اما من فکر می‌کنم خیلی محبوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75555" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=klqNITqcBnGkJlovtWj7pi4FbV77DdnHnAraFnXPFiCvdKX7InnPbWC9OPPpL5tGDLKXR03e_0pIoatnBKQMG4NBdFlDa1XyPN0OHvh9_JgY-cJVUx8Hdak6SxLFNC4a-muTlA89wNRaUlML5bl21nUcX-jbImcAquC1p_F81jFmi5dImzAclgiqu1JejM3vNCKAEYhuOXIHyGiidT0YGsGi8ZtGkfjQOdeQU5JTRW53pk-MNVVxXB-yWOt495dNuWrTVRXJmdEQily2J0-SCnnAydxWEjRk0_ebDn24JOLPxo-qM7fot2-Jr6p_B322-o4ZU-gF9vpt4nISuTqjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=klqNITqcBnGkJlovtWj7pi4FbV77DdnHnAraFnXPFiCvdKX7InnPbWC9OPPpL5tGDLKXR03e_0pIoatnBKQMG4NBdFlDa1XyPN0OHvh9_JgY-cJVUx8Hdak6SxLFNC4a-muTlA89wNRaUlML5bl21nUcX-jbImcAquC1p_F81jFmi5dImzAclgiqu1JejM3vNCKAEYhuOXIHyGiidT0YGsGi8ZtGkfjQOdeQU5JTRW53pk-MNVVxXB-yWOt495dNuWrTVRXJmdEQily2J0-SCnnAydxWEjRk0_ebDn24JOLPxo-qM7fot2-Jr6p_B322-o4ZU-gF9vpt4nISuTqjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی کارزار ایران‌اینترنشنال برای یافتن هویت پیکر جاویدنامان در بیمارستان الغدیر تهران، ویدیویی از لحظه قتل جاویدنام آیدا عقیلی به دست ما رسیده است.
آیدا عقیلی، ۳۴ ساله، شامگاه ۱۸ دی ۱۴۰۴ در شرق تهران با شلیک دو گلوله ماموران به سرش کشته شد که پیکر او را پیچیده در پتویی چهارخانه در حیاط پشتی بیمارستان الغدیر یافتند.
@
VahidOOnLine
مربوط به این تصاویر تکان‌دهنده: @
VahidOnline
این ویدیوی دلخراش: @
VahidOnline
اعتراض‌های چهارشنبه ۱۷ دی:@
VahidOnline
#بیمارستان_الغدیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75554" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3lFc79KPuTKTJOIH3nw_nw4w-ulI2AD60iFmC9BUcGOH3fPm62SsLKWi_KTiq_1coIuqRrF-uI1k0w452Ch7rUpk4OeZt6bMCQz7a8S8X5qExWfhcSuY15iVftsUWZWwlHgglCVnVfcClZzGUpR2OyuKb0kzG8zArcfBpKXFTHgJoGsfPGq5UQQvDZLTIzf0uTAKrKvbh9XEBh2Ae89yZZF1ynSiYdoTWLjL_y7T4trRCJIX4XyJOypJfjlCYpmIM4BHXVVxZf8nI310IqPaBeN5OxHjyUqhOvgvmXX-Kvci8nY7HJxGfSq2ORVT2pMn6Ukg3PPPOacm880tlQNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرش زاد
:
آمار نشون می‌ده در سه ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75553" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iklZCcwq7q4UC8C72ZPUjczcjlXALUvVwYcRafLb0nmJSnRvWV76d8e7rjMlAERNyhaTVeMRtWnpS0CwSholVh6AikspUeEtvsvjm1c3rzePg8M0R9NzCTJt2cjuu24NkZKlPIZ9Z6gZ6MQUdMuxxpIMsYFQAw0dk4s2aL8TSUnOhoEGEb_sQmLYhv_qIsXARx9CoU1rUR9qSSCzESOkL3YsLb10StYAVDCn_ZJ-neaEbdY4hY-ldPsCxz2KiojwZUZXtRPpRTSVIElVTe44nXHMffP5qTzct2hWG9me7lL1bILoy2uSHlPpCKTW-4Nz0dkLlEOrow-09p6LOMCE5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی ایرنا در گزارشی تصویری با عنوان «مهر مادری به عمر چهل روز»، داستان زنی را منتشر کرد که در جریان جنگ ۴۰ روزه، سرپرستی یک نوزاد رهاشده در بیمارستان را برعهده گرفته است.
در این گزارش، برای نخستین‌بار تصاویری از یک زن ایرانی بدون پوشش سر منتشر شد؛ موضوعی که بازتاب گسترده‌ای در افکار عمومی یافت.
با این حال، دقایقی پس از انتشار این گزارش، چهار تصویری که در آن زن بدون پوشش سر دیده می‌شد، از خروجی وب‌سایت ایرنا حذف شد.
@
VahidHeadline
+ بحث‌هایی دیگر:
twitter
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75552" target="_blank">📅 17:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuIm3WSRJ6CeazkpXB_-bc_Ahw84Da3iA7WxV6fMfk9ydsW2u6HpCdi1pznDs_svsbXBRETO9UwjmOWPse1mzn1IYY7hlzgyMM9IJ4ZOAXRaYrTWMRm3RE1Gd6m84jFIjy9il5uG05B5dYFK9kE4tHXuc-d5uA2Mx5v-zDAZrXJtDGnANwoF0QMdpwD5Wu1G4AZW4asmPapqlKc0OQQO93xcM_40-c4dbSP4uATlqSYIaOUe_mS_uTG0m7PWYU6fSwbYwMJs8gH_yyElbEDK31_Dx_knxfXMWCHCb7DIcCZo754Gb9GhiSdxngTxDlRzuFgg-EmPswluLNvXf7t-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایووت کوپر، وزیر خارجه بریتانیا روز سه‌شنبه ۲۹ اردیبهشت هشدار داد که جهان دیگر نمی‌تواند بیش از این برای بازگشایی تنگه هرمز صبر کند  و ادامه بسته‌ماندن آن امنیت غذایی کشورهای آسیب‌پذیر را با بحران جدی‌تری روبه‌رو می‌کند.
وزارت خارجه بریتانیا روز سه‌شنبه اعلام کرد کوپر در کنفرانس جهانی مشارکت‌ها در لندن، با اشاره به پیامدهای بحران جنگ ایران بر انرژی، کود کشاورزی و قیمت مواد غذایی، خواستار فشار فوری بین‌المللی برای بازگشایی تنگه هرمز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75550" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_M1y-h2zCu0yYgtlpxA5HEAcQ5MGEMy_Oz6Cp2NAqHE1sCpNGCSFLOlQMQwoxE1xIz7kO-gMecG3ppmw2nyCR-1LX0zFkT78Mb1_PT42vbE2AdX7pK2ROkd_-KjhHR7htVnAxm6ItSvKq6cpMj6go1psitcmGi0xDFf7ASn_aSO0ZT1pPcLRmDOkQ6Q4dOomv8LznKT_o-hVNERkrb82k7ORK7SdJ6LznlFmUtucQp0JeB74gNmtT7zHeLaCmaGNNlR6XHoykxjmcIRQ447BeBXwborO5mvUFubhDn3_wXhnyTc25DGbLxcWblhhTJBXFYeujjGhagXn7edCSJHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه ایران می‌گوید تهران در پیشنهادهای اخیر خود به آمریکا برای پایان جنگ میان دو کشور، خواستار برخورداری از حق غنی‌سازی، خاتمه جنگ در تمام جبهه‌ها از جمله لبنان و خروج نیروهای آمریکایی از محیط پیرامونی ایران شده است.
کاظم غریب‌آبادی که روز سه‌شنبه ۲۹ اردیبهشت برای ارائه گزارشی در مورد روند مذاکرات میان تهران و واشینگتن، در کمیسیون امنیت ملی و سیاست خارجی مجلس حاضر شده بود، از دیگر شروط ایران را «رفع محاصرهٔ دریایی آمریکا، آزادسازی اموال و دارایی‌های ایران، تأمین خسارت‌های وارد شده در جنگ توسط ایالات متحده جهت بازسازی و خاتمه تمامی تحریم‌های یکجانبه و قطعنامه‌های شورای امنیت» اعلام کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75549" target="_blank">📅 17:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9ZtQr_Cy248lbzMVAxO_C39-UG3I-tNuZAHyNDCeWwszSn-eMuIJS_ALqes6zfjlE1C290VSnfNnGOMUID143h3PQ_2Y5xec4g4vDO6JXOgoagZIzDbBH3p_GkZVVCTkIUxCt2XisoFtJInMeQdt5LWi5irNwZusNwogQ0WWoz_JsyG_kwvcc9qOMGRyZCZt-KiuG3GAmhlsUzRlsyHwW91jhM3V_dD-WA6m0IcP54GgA3gxVCW7wEp1gaTRR_XeoHj64bBMmDYX7m-PIszfh6c1NQL1aI8fKBGpQTncWk63nK1BT95PtcuuSnmyaKa7GOL75IjLQnrzqXdBOD5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان «کمک به گروگان‌ها در سراسر جهان» دوشنبه شب اعلام کرد شهاب دلیلی، زندانی سیاسی و کاپیتان پیشین شرکت کشتی‌رانی ایران، پس از آزادی از زندان اوین از طریق ایروان به واشینگتن منتقل شده و به خانواده‌اش پیوسته است.
این سازمان اعلام کرد دلیلی پس از گذراندن بیش از یک دهه «بازداشت غیرقانونی» در ایران، اکنون در سلامت کامل قرار دارد.
شهاب دلیلی که ساکن آمریکا بود، سال ۱۳۹۵ خورشیدی برای مراسم خاکسپاری پدرش به تهران سفر کرده بود اما هنگام بازگشت توسط نیروهای امنیتی بازداشت شد.
خانواده او گفته بودند جمهوری اسلامی او را با اتهام‌هایی از جمله «جاسوسی» و «همکاری با دولت متخاصم» به ۱۰ سال حبس محکوم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/75548" target="_blank">📅 17:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyLAioJqMvPoaiK7ag5kTeOryWImd0hANuXvCk00m241R5baYXateVPzdwTlihXlblB315jEHK0V3IVSPrYd_lJhaA18TIKk8l66U3i37goUN1XNO3Ny_dzg1FJZUvQ6AyNgRN2xrjqhzNE3kunxyfb4A91ejDoWjQlciKYx7s_GHrk_dOYvhVz56Pwg8QIUc9VeTvPnYThvBjGz_-8tiJyUGx5sc6UxAkb-bs7vrbUKl2T7o3P4owR9qgyB2g3aHJLA-UuSW9wZP6GPbuJg5AI2RNzC-Ad2f90Ht1OvhBSZTav_3kGzowVwwVRl7JYzXhjrNhtW6v_T8DkGsfpMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.
به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.
اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع و تبانی با هدف اقدام علیه امنیت ملی» عنوان شده است.
بازداشت او در پی انتشار مطالبی انتقادی درباره کشتار معترضان در دی‌ماه و همچنین اعتراض به اعدام‌ها در شبکه‌های اجتماعی صورت گرفته است.
آقای تیزرویان از عکاسان برجسته و سرشناس حیات وحش است و ثبت عکس‌های کمیاب از حیات وحش ایران از جمله خرس قهوه‌ای و مرال به عنوان گونه‌های‌ در معرض خطر انقراض، بخشی از کارنامه کاری این عکاس حیات وحش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/75547" target="_blank">📅 17:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMGKPvblpQJaJjIbvLDChDQMqmy8_0Xf4rGWL2-iS1i73NwBGpXqOnt9LZ1cFx-3L7h1POLCKEf6bhRv7002NLFHhhP7B_6-Rt_dyDlzJ1zAJnJEy0fB8MAsi90Pkz-MViLg0dvyJYnmEhgDNByGfRbRZIQCLPSLL0MvKqJ_2kbIjuNZN2Ti2fB3YJOI616oAXNd21HY4N1OmRZ6T1jRt_hVuhXNyoDfrTgu50DoR4ujcf3OjOv9Vb9D2Y8aN3ys7youzxrwj8lnzOeVsUVYoBlUNzrfcgMGmoWOJ-3nqK_UIsLsihNMd_qXoiLDyqouxF4sjRaQvS2_pZzZ-wZ_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر صدا و سیمای جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/75546" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
