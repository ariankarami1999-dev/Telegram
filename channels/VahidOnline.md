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
<img src="https://cdn1.telesco.pe/file/VMuBCn8sHRk0-TJDPxw05xn60MWRNHBN2jT8NOiWVhX7aoaBJauuNTWLn6A9sgilRl4oPLVZIRJqNHUbDC1wUBKMe61KnTYlBiFESrf6f6HaIEJYIS2uEWvvsEd2Z6sLqBvlTQttVd0ZfEEK-OQlowQ_3_26LDFI3iu2tAAbko8qn4noNnGm8RFsaR-HP_qPxlNsdtSU-Nj0ESgMr7zM4RVcIkfm3BQQjiq8P4AwZfaC9W5F4OTPAxju7et3dWBT6H-2Op1r7I8nt0Cu6RTaJo7O_0V0ES7A1XcZXESVXVHbNj8FAHY8aula0GKcpMg6rkbTppisIAtOUff9ZfsG8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 01:23:00</div>
<hr>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nPoNMZGvY6kPvEjbEr_2z17If7JYBQhhyyv_26Pre3QB_NIKlJpIvKWa9pANaX2dyaQgmXgHBOVcr0UXmxSrhyH5ef8tt-BMn4Y1GG_qI6pWkFAkZTpRTHs785HuTKgDNSbe0sNEEZrcfOaQtwH9B0QOSbPv5M11dKC0svcaawXZfZ6nYdagYrWMuaw4-nm72XE4V88SthGQ_JyjajAQT9OYlZjhY_0BovaMALW9ZxZ-cDBNVYw0_Ke8zE5wGXumcRLyJHzO3PQSyRLPpcYeG61vgBwHBizMW05hyxBl7XpdrCz8YqQV8MIgAawHYLkSoPhX14HzVGHukTvQ84DDjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/URAZ5VNRY91kd--LHiy_fXYF0Em45v6emGARq7xTb1NdlIfsBnpo-6EImj9CaSkwY2KPcl6MQothVTvoiukaGAM1Z1qpnitZCea2wMxidmqiZu-9ogEdvrSWI5q85Z3dxePPQzPV0JVtpJKsLyY_DzcHXdS4Kl9XNYYlr_6bKNC6Xt1S7_p_IU_mGB1RgU_hjmidusZZtnqxT7KzAz5OxjTMwSQqgD-RzsHQ96AqObS4GfqLXHK9eVJrraOu3Hd1bmV08aqFxZZM6Bf7gCzpniBcT-2bOpzKZEAonj1FRAiopNpz4K0BxIN5VLLH4-YrpSNaN4ar5n816umNU9YzAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s97Ldlpow-_9g2jfUp4RhICw4VTe0O4HOkDj6nJ4FztXqe1ZZDV4u4r__3m8qx8artGABJzdzAluBDe9o_INXesB64KTkQTJ07HToA09L0JPSK-l4abFh4QfjWia3XeRt7lAlZxJdp_rDY8DMyI-FchIbkt6YS-J0FdV97MDARB3nVAdo8IGF4JG85GFWxjfON_1Fbi6MmcPiXxnq2XasBHIRCN7Lyq0gsThlYdJ8iolyum2NI2Qaz9jpkRwRkfQcGprO0Uk2Sd0sCHbLHXo5ENbomkBJUnSj4XpUU0AMLIlpJ6SkFnU8FYBOxI-JSfxre2GiLkcc4l4YjICIFxQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WI8H9ZDZ-zdyhhFxtqp0Jl_AA3yHHM3LaflD3EIitg94GnNqhPoFYzEh0K5VDbZ21mx42ZGiIY8It5lxnMQ0ARRiAD8GevC_FlrEokeiojGDjjB7J94DVGRGmmy1X4WBR5bE6BvjfhYlw4GAsw4BcBpipsFB04EAOvhTZ5tui-xv2BvcXMOIkhbJbo7K7TkoIx4RewNVdBpfdCdqw8XTvIqnVyvBHApIR5j7WD7eUKa2AmPcrp_q9zoOY5Q7aO6ZwRZtvRWztK7AGkt6fmyHnwJnDuYB1dgAhdnvQo-_fAVq-tpzs7sQSykOhmZzNOB56wrsGJwBPKIP2of1JNW5IQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=ePkz07rnDSH7c9QUiSYLQLc5VTDMDlMdmhHFEQ7VaGds0AEUJApop3h8VQ_P5Kjf_7_8fWphSCxtnMYQ96x7h_FpUiVXfXdhMn5pGtJqFJAyF0bbrpFNLa02HqyRqZyvhpgglmRhLPp8VeyK7SKftbjVSsp7pqtLKOBzzfdpqMVXtp9sAcgGkfnuMl2Ki3vSD99QvEoSRvwWeYG7UiVDHZ8Bu3CW7PgEj-FInoRaL6sgfN0WAnlrHI5nH8_6PqIBpYgAet66DUs3eylj14ZFcoHhV_noxT9rl8DkRN59KhofodT04zrbW4Rl3C5vnYfs_eTduAidk4ppMk7mSYQQeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97d125f04d.mp4?token=ePkz07rnDSH7c9QUiSYLQLc5VTDMDlMdmhHFEQ7VaGds0AEUJApop3h8VQ_P5Kjf_7_8fWphSCxtnMYQ96x7h_FpUiVXfXdhMn5pGtJqFJAyF0bbrpFNLa02HqyRqZyvhpgglmRhLPp8VeyK7SKftbjVSsp7pqtLKOBzzfdpqMVXtp9sAcgGkfnuMl2Ki3vSD99QvEoSRvwWeYG7UiVDHZ8Bu3CW7PgEj-FInoRaL6sgfN0WAnlrHI5nH8_6PqIBpYgAet66DUs3eylj14ZFcoHhV_noxT9rl8DkRN59KhofodT04zrbW4Rl3C5vnYfs_eTduAidk4ppMk7mSYQQeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 134K · <a href="https://t.me/VahidOnline/75556" target="_blank">📅 22:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=vgn3MTkSmg6_LfanmOk4XVqqX7KcVofo1lrWN3DwHT_syZT_LYnRxoMB-CWm4xRZtpF0Kxy4xnXkfrFImAOrEvyojY9A1gsg4TpamrhbTBjwDy2-lWCJC0yfdBFwAE3OydvKp2M-TWDFqC6uwF2Sq_kJx31O8fLMeCMRwVbYrqEsx2ePb0NcJikAJqeALOsIjsBRO59Kc6h8xpiLvv8Uys9u-gy_3U7_mZR_dpZhSsx1N3-6_rMgdegXoBircTm26AlTdORDx3JHawTv0Y6y1WrxnoFqBhdhFX1yvjl67hyMtcVQYEjpxm-zqQMXNfYG2MAd67eWLRutmodoWITTAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83fd4e1acd.mp4?token=vgn3MTkSmg6_LfanmOk4XVqqX7KcVofo1lrWN3DwHT_syZT_LYnRxoMB-CWm4xRZtpF0Kxy4xnXkfrFImAOrEvyojY9A1gsg4TpamrhbTBjwDy2-lWCJC0yfdBFwAE3OydvKp2M-TWDFqC6uwF2Sq_kJx31O8fLMeCMRwVbYrqEsx2ePb0NcJikAJqeALOsIjsBRO59Kc6h8xpiLvv8Uys9u-gy_3U7_mZR_dpZhSsx1N3-6_rMgdegXoBircTm26AlTdORDx3JHawTv0Y6y1WrxnoFqBhdhFX1yvjl67hyMtcVQYEjpxm-zqQMXNfYG2MAd67eWLRutmodoWITTAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75555" target="_blank">📅 18:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=Q-fQCKsrXD6vVvvfVF2m1Yru-bIpu-SxifdC1a2KSrBWrKtr_QCicz-TiWr1RmVUYTlBMvlHjaLBnBhWeBUVjRup6MTzntix1ZdXKdj0pdUExIesO7a-hJeCvvaQVt_Gd29U_Nm3Fj4LvZyDY4sBci70PM7FYm8BvVFPesDXwKUSVppZARPREU0CToIsm7wJ2Z8JJtASSpfMuOAk9Jm3dbE03uTrUx0IaLsOLenqbnJlt2pIuMF6_ZkJ3Jugr0R4cIJSImiYPaLlSyQ3SMon29wvgdSZJwxRSKWZFDvFffB9NJ0gbaLcOB3sUZyhxmT7eRgqT1mfq5cRMOTL2a4TNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1d001deba.mp4?token=Q-fQCKsrXD6vVvvfVF2m1Yru-bIpu-SxifdC1a2KSrBWrKtr_QCicz-TiWr1RmVUYTlBMvlHjaLBnBhWeBUVjRup6MTzntix1ZdXKdj0pdUExIesO7a-hJeCvvaQVt_Gd29U_Nm3Fj4LvZyDY4sBci70PM7FYm8BvVFPesDXwKUSVppZARPREU0CToIsm7wJ2Z8JJtASSpfMuOAk9Jm3dbE03uTrUx0IaLsOLenqbnJlt2pIuMF6_ZkJ3Jugr0R4cIJSImiYPaLlSyQ3SMon29wvgdSZJwxRSKWZFDvFffB9NJ0gbaLcOB3sUZyhxmT7eRgqT1mfq5cRMOTL2a4TNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/75554" target="_blank">📅 17:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvgThDxGVe9wREfpAVrf45Xiks25QZ3V8uFRWAnSZ9ZSBmIlPzrxz-uiqAvlCFLkIqAK5DjTxas-4J4Rv8Xw821RpHWJaZwGAAl5e_JVo4Zc9X865OTtscvN76t6QWUPxtlL46yfHXOBGAtyIsdAcng8NiXZEYGsIQrr4je1zK8QWF9vaQmZT4WWqqW4oP1iHiiljeP5Vsl1_EZdtLqEq-PWwtDjTX7GUL3FXRgZjQwAP5utQfRhb6cJoRAhhEkw3QJAaJnXgtdqmzZnNDrXrJenUku4dzAtDVZeQfNrBwlHOVyNnZLHnrjjKY_WeufM5pOp3Gz-KOCxrW0RFmGT2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرش زاد
:
آمار نشون می‌ده در سه ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه.</div>
<div class="tg-footer">👁️ 197K · <a href="https://t.me/VahidOnline/75553" target="_blank">📅 17:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA8hFAbeYjXR_kUbazudYCENFwEL2uyQY-VnP91Fvxprx-oKxEjh724qdTTwfi1O6tlkTppQbUziAx-KH51B2YDY9JvlGVpEVgCsMzJVeptNz3tyiF0Vilb-GxgwbHgQbzV1ut-Bknzu-5lTMtsgjEChN6mKjqS4VsB7tI90Sj2-pwJCkuVqgHis05soTTejigZMF_m2UuD7CvuOMha6U91NholUe27zZJHT9dXyHtcVrYmV8Q6t6OaHcvkpTSt00-RMVHhII2bgAOlWdJ1wXfQpZV7j8f-HUEiyZdiQSO9TC5xzQfP_rDv7EGiN8VR_n0gX2kMg3AL1Y7bQyOd_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری دولتی ایرنا در گزارشی تصویری با عنوان «مهر مادری به عمر چهل روز»، داستان زنی را منتشر کرد که در جریان جنگ ۴۰ روزه، سرپرستی یک نوزاد رهاشده در بیمارستان را برعهده گرفته است.
در این گزارش، برای نخستین‌بار تصاویری از یک زن ایرانی بدون پوشش سر منتشر شد؛ موضوعی که بازتاب گسترده‌ای در افکار عمومی یافت.
با این حال، دقایقی پس از انتشار این گزارش، چهار تصویری که در آن زن بدون پوشش سر دیده می‌شد، از خروجی وب‌سایت ایرنا حذف شد.
@
VahidHeadline
آپدیت:
گویا نوزاد بازمانده جنگ هم نبود و تکذیب شد و مسائلی دیگر:
beehnam
،
FSeifikaran
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/75552" target="_blank">📅 17:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_ACG7pYJHMP-_XCA-VE5BwMtUai3Mn6BQ21hZDZZZag8S-7NFzxVQLgEfv1LGvRrL5SPbIbOQH-EP-sreA9gZKqBU11kqdUxQ2_VVq9FsS_1ow_W0FIeh8wJOudQwTP_52BrS3gbshisv2hvuxX73lDIPthcSNPsKPpwtJeua9FXZJuIal54-lY8U5HiotmlvnbOAYfxEwIKxo4dmntPnTO9GSSZRUWIRgQjdgpdR5RHlx5OBmbsOKZDyX2nWEf0j-1fGpnnABVX05kMTyJTS49nHZhvJ60XgPtx3Y04ur0DOSLx5thHNI-ALdZU0oUlGEJk4uXW0kSnHIGP1jxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایووت کوپر، وزیر خارجه بریتانیا روز سه‌شنبه ۲۹ اردیبهشت هشدار داد که جهان دیگر نمی‌تواند بیش از این برای بازگشایی تنگه هرمز صبر کند  و ادامه بسته‌ماندن آن امنیت غذایی کشورهای آسیب‌پذیر را با بحران جدی‌تری روبه‌رو می‌کند.
وزارت خارجه بریتانیا روز سه‌شنبه اعلام کرد کوپر در کنفرانس جهانی مشارکت‌ها در لندن، با اشاره به پیامدهای بحران جنگ ایران بر انرژی، کود کشاورزی و قیمت مواد غذایی، خواستار فشار فوری بین‌المللی برای بازگشایی تنگه هرمز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/VahidOnline/75550" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-ZXrgwN9OT7r0YiSgEblIfNMrMRg8WIk0ZuISS1ZiTKDVRkoY7PcX9e4aGVFUrlc7-6pz4yhCmc_p2Q3Ab7waPkDCCnaiRo6r9aHnF_ovTsGT_eBih1YoPU6qBtKWa2K46E4xflDvQrhIs90sB6KXE4TBgFH0_tjeykZdhXzRMnfzpBJY4dn3CTdILGcFTlun4zYfEGH7CCf0Li90x6GmBc_g99Q7aKAwqwcxgVt1jTmem3hgEqLeXGatCmC6oD2yATDWSOZsLJgPZv1SiH1_8wC2sa9kRAYZzuul7qZarUEU3qk_CTUFYRxsA4_V9edqEImFlVnYyzbKvzG-hL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه ایران می‌گوید تهران در پیشنهادهای اخیر خود به آمریکا برای پایان جنگ میان دو کشور، خواستار برخورداری از حق غنی‌سازی، خاتمه جنگ در تمام جبهه‌ها از جمله لبنان و خروج نیروهای آمریکایی از محیط پیرامونی ایران شده است.
کاظم غریب‌آبادی که روز سه‌شنبه ۲۹ اردیبهشت برای ارائه گزارشی در مورد روند مذاکرات میان تهران و واشینگتن، در کمیسیون امنیت ملی و سیاست خارجی مجلس حاضر شده بود، از دیگر شروط ایران را «رفع محاصرهٔ دریایی آمریکا، آزادسازی اموال و دارایی‌های ایران، تأمین خسارت‌های وارد شده در جنگ توسط ایالات متحده جهت بازسازی و خاتمه تمامی تحریم‌های یکجانبه و قطعنامه‌های شورای امنیت» اعلام کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/VahidOnline/75549" target="_blank">📅 17:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sohqcrfNbnR5d7wFnzmK6C7C7zqZ0Xg7B0bkoJ08JHwTdR1oMWxt7YJtZ7gVN3qeO9NhU4DfKv4lahif9N0EyRq2F4LFh0DbPrVvOvfMQ33k-94SnAt94yC-WiS0r4e7fPZY6VWLkgBUlBDB1_6OvoKhWvKq6gLnN5mgHAibUG5KO_tWFZWtLDR-T--Flj_4V9jVkUZUGS9wdn7rvFaPFZ1j_OaLLslcYRjjUyjBrZDhU69qpTQ_Bcuw3GaCawst_SN-b1vEBpoPUj7Hgxz_dh1ti-P_qut3if0rhi9WX4FrlgwxmX_jVmCSOcXzJsXHXcyi8PlpE5d_6RIcvrweTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان «کمک به گروگان‌ها در سراسر جهان» دوشنبه شب اعلام کرد شهاب دلیلی، زندانی سیاسی و کاپیتان پیشین شرکت کشتی‌رانی ایران، پس از آزادی از زندان اوین از طریق ایروان به واشینگتن منتقل شده و به خانواده‌اش پیوسته است.
این سازمان اعلام کرد دلیلی پس از گذراندن بیش از یک دهه «بازداشت غیرقانونی» در ایران، اکنون در سلامت کامل قرار دارد.
شهاب دلیلی که ساکن آمریکا بود، سال ۱۳۹۵ خورشیدی برای مراسم خاکسپاری پدرش به تهران سفر کرده بود اما هنگام بازگشت توسط نیروهای امنیتی بازداشت شد.
خانواده او گفته بودند جمهوری اسلامی او را با اتهام‌هایی از جمله «جاسوسی» و «همکاری با دولت متخاصم» به ۱۰ سال حبس محکوم کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/VahidOnline/75548" target="_blank">📅 17:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJHTNqEvTGDr-QgQhum7hIGKK1leDkT6r9b-UYwa-RZauIYj5MhVvyjWINT0Hpo6ExsmF3Go7AFzTRVuIJB6-4m3ykF01k-IO1BOybUFWEaoyY310SW4nMpV4Pzqt94BwydGNTayOxu_RLIgPEF_JcwVqmSwWF0BIX2c0t5RjMokI8QRI7FXVMQZ9FvRfclkKPU8j3qruZnqrOHeYUdAyXsP2Nzk6S0laelgsIDzVHSJ7UM4xsww0_sD-RSKMJRsK8HhBWZbJxoy2kvCS43oPuT5zU4CvY7Nd-ve-mH8QSMM2H1ti81QUE4ehtqmMGK-TKCsZZZgto-ln6zRJqEydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.
به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.
اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع و تبانی با هدف اقدام علیه امنیت ملی» عنوان شده است.
بازداشت او در پی انتشار مطالبی انتقادی درباره کشتار معترضان در دی‌ماه و همچنین اعتراض به اعدام‌ها در شبکه‌های اجتماعی صورت گرفته است.
آقای تیزرویان از عکاسان برجسته و سرشناس حیات وحش است و ثبت عکس‌های کمیاب از حیات وحش ایران از جمله خرس قهوه‌ای و مرال به عنوان گونه‌های‌ در معرض خطر انقراض، بخشی از کارنامه کاری این عکاس حیات وحش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 204K · <a href="https://t.me/VahidOnline/75547" target="_blank">📅 17:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qOyYoX7nXjydM1lK2HXU8aTgduI_FFrcurlqhvPjfMU3ad62_1BFTPXZeWdMERZT0_4wAsBNnk19FRZzDd3ey8JfAWsfeHW7KpmJDGaLe--zFI8sURRgyPCAR0FrI3s7PXvY85dxuFclLoSan0fe_tp5jnJ86LwhtId27HxhIFeeoxM8jpRhpknwfpInAjoTzr9rLR2vheCMz6ChRFvNE4Lb0GjL8mekILpUt8kDbZcinp5t4nVbwY8DKUG_oZnVZy2daX5GOiAQrEkcPJmQkGkgRnSRaXfNPBzzvXNOhmnAxtddRMHdPZiw1--GQBNURh1ow7kuy7FOGs2FKb106w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر صدا و سیمای جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75546" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vQZA1IoOxbmV5c6EG7rTn__d7DXJodjoE-bsKIdakVCy-oeigdbZ5H5cfzqnQ2qAihevUXfRCiQfe8AZRYwdtIZ9N9aSFQJnV6HCuBpC_DldDeTsJe5RSoo1AXeX0jJaqsK0cmNXr1GEyPfAYY24AAjOWWNwl72OpZLJ4RxxqtUv2xH4piI6eoNT1Nq48eoBFExjBbxNJFPcLWfh0ZN-kiuIrWJi1AJs9mJwSI81OXuH0OurBy5P9wOIrjYckAj1VoR-_ENWpIG-rDK9AHiiS4k0HBBYurFs1vQ-d-_OnHIa-I8atzG35ez_oLfP3CqCR4L95a8g9m49tEZsqASr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: حمله فردا را به تعویق انداختم
پست ترامپ ترجمه ماشین:
از سوی امیر قطر تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی  محمد بن سلمان آل سعود و رئیس امارات متحده عربی محمد بن زاید آل نهیان، از من خواسته شده است حمله نظامی برنامه‌ریزی‌شده ما علیه جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازم؛
زیرا مذاکرات جدی اکنون در جریان است
و
به باور آن‌ها، به‌عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین همه کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
این توافق، نکته مهمی را در بر خواهد داشت: هیچ سلاح هسته‌ای برای ایران!
بر اساس احترامی که برای رهبران نام‌برده قائلم، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک ارتش، ژنرال دانیل کین، و ارتش ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده فردا به ایران را انجام ندهیم؛ اما همچنین به آن‌ها دستور داده‌ام که آماده باشند، در صورت حاصل نشدن یک توافق قابل قبول، در یک لحظه و بدون درنگ، حمله‌ای کامل و گسترده علیه ایران را آغاز کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/75545" target="_blank">📅 22:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uylluMRRAzBvrNZ-YqtKq4dXa9Eapr2yeIZ93LtbJC-A_v_PpDVASRC9_W0YqGE0BU8_RbQhvkJur2L09v4Rl4WVOfRn-7EiatrJDrCQB4g_0UrGb08va_JdGKHNoKghcpOlx1dG9bjL3ZDrPsh_jOh9_p4nHwATYMA7CHXAO4BPbzDmgjtKiFZZHgOzHBGMJUs3LzRSiYBr-XNw4eIUHd-wJwx74j7UY44GgqEnwkfwpZkumCV1cYf8OmFR-RuV3ZCwtbwnJwPPd2GSxvrZ3TToS6uhKyw2wNluf9zawO4gVDsn1Lq1jSNvfZjgO7msn5XhsUqe3THnEBlT8-7SDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز دوشنبه در گفتگو با نیویورک پست اعلام کرد که پس از دریافت آخرین پاسخ ناامیدکننده تهران در مذاکرات توافق صلح، «به هیچ وجه حاضر به دادن امتیاز» به ایران نیست.
ترامپ در مصاحبه تلفنی کوتاه، ضمن ابراز نارضایتی از آخرین پیشنهاد تهران گفت ایران می‌داند «به‌زودی چه اتفاقی خواهد افتاد».
به گزارش نیویورک پست، وقتی از ترامپ درباره اظهارنظر روز جمعه‌اش مبنی بر اینکه مایل به پذیرش تعلیق ۲۰ ساله غنی‌سازی اورانیوم ایران است سوال شد، جواب داد: «در حال حاضر به هیچ وجه آماده دادن امتیاز نیستم».
ترامپ ادامه داد: «من واقعا نمی‌توانم در این مورد با شما صحبت کنم. چیزهای بسیار زیادی در حال رخ دادن است».
رئیس جمهوری آمریکا همچنین گفت از تهران «ناامید یا کلافه» نشده، اما هم‌زمان تأکید کرد ایران به‌خوبی آگاه است که ایالات متحده می‌تواند فشار بیشتری وارد کند.
ترامپ گفت: «می‌توانم به شما بگویم آن‌ها بیش از هر زمان دیگری خواستار توافق هستند، زیرا آن‌ها می‌دانند ما...به‌زودی چه اتفاقی قرار است بیفتد».
وقتی درباره ادعاهای منابع منطقه‌ای مبنی بر اینکه ایران تلاش می‌کند در قبال هر دو مسئله هسته‌ای و بازگشایی تنگه هرمز در برابر واشنگتن «سیاست صبر و انتظار» پیش بگیرد، سوال شد، ترامپ گفت «چنین چیزی نشنیده است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75544" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-dD4O__LjwWIBSxFyomf9liL7-g41TEWiLx_GLew5Y-BxWH7wJolVGLv2fEJjgcpf1SvDCQ4d1wdCvAcBEES_29H4J61zKO2RjTKqQUlkr9sX4v6Uu9SkrDr_5hgwrfixC5PYuUDTdv6wQHz9dItTuntiP2sB7nHFeA3LpKPNnTAXbWQGl7hBEQUjNkTzqDKA8H4d5MvLw_WIXsvlFhfz6JyV_yCXjnt81fcgykgOJj529X8Rw-ybkas5iuDwspO5IEMrGDPMgSDBxf72rW_JoUSrrjSFqbtMZ5m8KL30Z8-v8-YY27OGgRr6gWnt7Sn9ZtDTZhYbx3L9C-FdpuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، دوشنبه گفت که آمریکا در حال صدور یک مجوز عمومی ۳۰ روزه برای فراهم کردن دسترسی موقت به آن بخش از نفت روسیه‌ است که در دریا سرگردان مانده است.
بسنت در شبکه ایکس نوشت: «این تمدید، انعطاف‌پذیری بیشتری فراهم خواهد کرد و ما با این کشورها همکاری خواهیم کرد تا در صورت نیاز، مجوزهای مشخص صادر کنیم.»
او افزود: «این مجوز عمومی به ثبات بازار فیزیکی نفت خام کمک خواهد کرد و اطمینان می‌دهد که نفت به آسیب‌پذیرترین کشورهای از نظر انرژی برسد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/75543" target="_blank">📅 21:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75541">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cMwYsemP93JJCFip5hSbMUP2u0jvNQhU72rY5eM8OHrkaW0vW0dH21G-3XVRX7bqDLDxn7jorbzThW0juAMwr04k8Ime2MVF1p63U1C2ioM-s2ZMx3iBiBii2dJ6Rnj6RZfh7crYWNew5UH6oGCGH4lqze3YJB86oiONcb5KckHV3vkO5qcJ3uyxugPsiJeae_gPDNm4adbmQVE0SVg2tGc-ELxT8-JUHC7JyzhpvalxDJ4bPRI1yBfw1o2K82HvmhcrP7zQrg0n5MnF0Rz6_GwkwvfMTZIsZfRibzUm5k6J2NbjBmMIOD5QzvvZqb8nV0Jb9HGG8Pe2qhHz7StrLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/me4dkpq3G8Ew2Va4aYQwNjMQPCVxPaDRDJVF12wKs_QptTb-mMiixjqXK9_WLZUut0G0i3MlAnndtq67z6lsFsZb_XsMThH3jMrfbQeFNlHIEuUNl8dDpJ6ZCgvr6ritH1TgIsPN65NEa2J6Mr-2TJZdYyWWjzAnR8IcLf-RsOHsLdpjyy1S9K3VYD6AxT1kCtqQSXz6Xm2OdZj5651KQOAWtIu1Ceeo8D3l1Few9EuSFxOC-Pbxx8p3teQ2B6_TtZBbcVvYRzxSt_fP5-d5MM7vFfXi3SobUiOcX980_BHZQamqbIxjHCas6ISHpCP1sbvQ5sHFtBQnZa5ifTn-Hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وب‌سایت اکسیوس، روز دوشنبه ۲۸ اردیبهشت ۱۴۰۵ به نقل از یک مقام ارشد آمریکایی و یک منبع آگاه گزارش داد که تهران پیشنهاد تازه‌ای برای توافق ارایه کرده، اما کاخ سفید آن را «پیشرفت معنادار» ندانسته و برای دستیابی به توافق کافی نمی‌داند.
به گفته مقام ارشد آمریکایی، اگر ایران موضع خود را تغییر ندهد، مذاکرات «از طریق بمب‌ها» ادامه خواهد یافت.
بر اساس  گزارش اکسیوس، مقام‌های آمریکایی می‌گویند دونالد ترامپ خواهان دستیابی به توافقی برای پایان جنگ است، اما هم‌زمان به دلیل رد بسیاری از خواسته‌های واشنگتن از سوی ایران و خودداری تهران از ارایه امتیازهای قابل‌توجه در برنامه هسته‌ای، گزینه ازسرگیری حملات را نیز بررسی می‌کند.
دو مقام آمریکایی گفته‌اند ترامپ قرار است روز سه‌شنبه نشست تیم ارشد امنیت ملی خود را در اتاق وضعیت کاخ سفید برگزار کند تا گزینه‌های نظامی را بررسی کند.
آکسیوس گزارش داده پیشنهاد تازه ایران که شامگاه یک‌شنبه از طریق میانجی‌گران پاکستانی به آمریکا منتقل شده، تنها تغییرات محدودی نسبت به نسخه قبلی دارد.
بر اساس این گزارش، در پیشنهاد جدید، توضیحات بیشتری درباره تعهد ایران به نساختن سلاح هسته‌ای آمده، اما هیچ تعهد مشخصی درباره توقف غنی‌سازی اورانیوم یا تحویل ذخایر اورانیوم با غنای بالا ارایه نشده است.
در حالی که رسانه‌های دولتی ایران گزارش داده بودند آمریکا در جریان مذاکرات با لغو برخی تحریم‌های نفتی موافقت کرده، مقام آمریکایی به آکسیوس گفته است هیچ کاهش تحریمی «رایگان» و بدون اقدام متقابل از سوی ایران انجام نخواهد شد.
این مقام آمریکایی همچنین گفته است: «ما واقعا پیشرفت زیادی نداشته‌ایم. اکنون در نقطه بسیار حساسی قرار داریم و فشار بر ایران است تا به شکل درستی پاسخ دهد.»
او افزوده است: «زمان آن رسیده که ایرانی‌ها امتیاز واقعی بدهند. ما به گفت‌وگوهای جدی، دقیق و جزیی درباره برنامه هسته‌ای نیاز داریم. اگر این اتفاق رخ ندهد، گفت‌وگو از طریق بمب‌ها انجام خواهد شد و این مایه تاسف است.»
در ادامه این گزارش آمده است که ایران و آمریکا هنوز مذاکرات مستقیم درباره جزییات توافق ندارند و گفت‌وگوها به‌صورت غیرمستقیم برای رسیدن به چارچوبی مشترک ادامه دارد.
این مقام آمریکایی مدعی شده که ارایه پیشنهاد تازه از سوی ایران، با وجود تغییرات اندک، نشان می‌دهد تهران نگران اقدام نظامی بیشتر آمریکا است.
در مقابل، مقام‌های ایرانی همواره تاکید کرده‌اند که این ترامپ است که برای دستیابی به توافق عجله دارد و زمان به سود ایران پیش می‌رود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75541" target="_blank">📅 20:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75540">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MREcMBRfVYpKpAdzmhITixdxZZSfaNzcb_g25EnwE7P3nJyzVLY34662FFAbXAll0h0hNSWGk3YIKV0tJpFaCno5EXF_H4DbLlbPJORYYVltBsIQBk6Y-Ykj-0jNlFBuwhkvscCXhhcB34N1SRoSFPpT4CyDlYGhe9YwsqM9AbPK5cNUNQeCiB8oYAHWe4zQJAYgTjHGT_5kvOSAZHfyKhXm5Kf_YSF4Xl4Vqe7JMUG1YizB47JDmiyyZsezD_ovfUzHd4hKNT1ndoWUE0-csENCpKfFK282f5VaIcM8TGx4SozKFmDi9z-w43T0RJ5UxGq21EFgr3-_2znE8ZiRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در قعر دریا آرمیده است، و نیروی هوایی‌اش دیگر در میان ما نیست، و اگر تمام ارتشش از تهران خارج شود، سلاح‌ها را زمین بیندازد و دست‌ها را بالا بگیرد، هرکدام فریاد بزنند «تسلیمم، تسلیمم» و در حالی‌ که پرچم سفیدِ نمادین را دیوانه‌وار تکان می‌دهند، و اگر تمام رهبران باقی‌مانده‌اش همه «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال (وال‌استریت ژورنال!)، سی‌ان‌انِ فاسد و اکنون بی‌اهمیت، و همه دیگر اعضای رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران پیروزی‌ای استادانه و درخشان بر ایالات متحده آمریکا به دست آورد و حتی رقابت نزدیکی هم نبود.
دموکرات‌های احمق و رسانه‌ها کاملاً راه خود را گم کرده‌اند. آن‌ها کاملاً دیوانه شده‌اند!!!
پرزیدنت دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75540" target="_blank">📅 20:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75539">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEfl4IRQ-uNdyDPp-jLxNxQ11vJR3JcJ41TOfR4h2j-JGSAy018W5brj-s7PX4up4YEX5JWAKdYmGnrpwKdkGgNlTsXSURUAnNi3uhNcQHZF8D-FKbTErPcU21qOltsT8Kv_GKmVd1VJBbpTJez-FZ6-yvApNjkTKL_0P9h10hGoM5K82lnqDLvpyUpm_J1Tu0xWjc4g6NncoztFj4FmGuZkjetC7lI5M1IOhCMnVvk1k-g2Y4aUt-Kd1UfjnI3uct6i9F07jkBNxmau7qVltHbHV1KBgSRu2v0hwFsMavEq51V-aeiplLU_5SzI3efoVOeWtLZQdrNBwy-q_AM7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیر مرکز روابط عمومی وزارت بهداشت جمهوری اسلامی، روز دوشنبه ۲۸ اردیبهشت مدعی شد که در حمله اسراییل به بیت خامنه‌ای «اتفاق خاصی» برای مجتبی خامنه‌ای نیفتاده و زخم‌های او نه چهره‌اش را مخدوش کرده و نه به قطع عضو انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/75539" target="_blank">📅 19:08 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75538">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQoVGd75PgO_cZ6ELeZKZjlZ5O1YPKOKS8W-e-rEg1wg70242Rzu_AOTaOKhcYeHUDkGX1siJp6p7hp2sx-Wc5t02rSfgE2DZiGga8DoRQjSbmAOCJwckINGw5fWZGFBAPw2xONM2B63wQx1ADKDsp1AYvbFw5Q_IURHdzl2e2CZcjjKvKLBjnZbi6AhG6Wgc9TBzeQOxfdFViSGb3vaBzKEIvdrvuRBPYzz_uAdeSfCPrsBKtJCUAokvphiR0JbPj6oUeLNYNZr7W7097DZ3dojt5wjOOzQ5Cu06MPWl_94V1x0EyLfh756hngQNUJppnTX7HLLAFku8B8ADdRdJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردریش مرتس گفت که «ما حملات هوایی تازه ایران به امارات و دیگر شرکا را به‌شدت محکوم می‌کنیم.»
صدر‌اعظم آلمان در شبکه اجتماعی ایکس، حمله به «تاسیسات هسته‌ای» را تهدیدی برای ایمنی مردم سراسر منطقه خواند.
امارات متحده دیروز گفت که در حمله پهپادی، ژانراتور برق بیرون محوطه نیروگاه هسته‌ای براکه در نزدیکی ابوظبی آتش گرفته است. امارات در بیانیه‌هایش نامی از کشوری نبرد و فقط گفت پهپاد از «مرز غربی» وارد شده بود.
آقای مرتس در این پست نوشت که «ایران باید وارد مذاکره جدی با آمریکا شود، از تهدید همسایگان خود دست بردارد و تنگه هرمز را بدون هیچ محدودیتی مجددا باز کند.»
اظهارات آقای مرتس درباره مذاکرات ایران و آمریکا اخیرا به تنش لفظی او با دونالد ترامپ منجر شد. او گفته بود مذاکره‌کنندگان ایران آمریکا را «تحقیر» کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75538" target="_blank">📅 17:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P9oXs1Y6N-P3UY2wGp2soBXLPw7TVv-pCtmP6afZ4-dCNB3oO-x00tiBZc00r_kcWZygLzo-0STsqBkLRb5S9ZGvqs7J6HDxXEzsL8a5FbzOZY0O9c_Pyjxqs25fDsF_2WxJP5L97vNO9iUl_jA5azwHMVNpRuimbHQ5hiqkd34lM5OH0mhk7tKErX7KQFCOrRieDubirCCCqVYmoHLHE4Fi4gcoFxYeLzreLv9ln_q7XkM4p5_SgufKbgTklWUYx4dkHciRiLd4u_Mcbcf_mK4olAgiV0QH2gArHv3wFbeHSDEV5fhhXEiCkdfhMwqsSShbg9fWfDeFzWplSakHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aOT5vyVaHK6oAQfCT6gToBIzsQBC32_OTMCD_a0aArUqEBYbFRZt1M2aQ_8taMagGdYsrJK9RX3Grgsr4t9BolSEukkPaSuUWDmljN4luqUZlsmickkW_8aKlDmBs8XPAVT63cZt26hpA-n0thWVy6qBfJQr8wpYBdNQQBVQxf5HWAtFSY21a3W1LPRMSnJG3kBsny_wxhuUdw-zlrO9PswLLQ0Br2snOF0u-LxpQ4Qju4arSQEiDh5UsL0HSX8W8Ebj8Lhot3sKTRDvJ0N7ZuizAgTP8j9AOcwcffDci3qjlaISII37RPzNn0GNZHSuhAYj6twAJNY1FG0lg9_6UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت ماه به نقل از «یک منبع نزدیک به تیم مذاکره‌کننده» جمهوری اسلامی نوشت که تهران «جدیدترین متن خود را در ۱۴ بند به واسطه پاکستانی تحویل داده است و میانجی پاکستانی آن را به آمریکایی‌ها ارائه می‌کند.»
ساعتی پیش از انتشار این خبر رویترز به نقل از یک مقام پاکستانی گزارش کرده بود که اسلام‌آباد یکشنبه شب طرح پیشنهادی اصلاح‌شده جمهوری اسلامی ایران را به واشنگتن تحویل داده است.
@
VahidOOnLine
خبرگزاری العربیه، روز دوشنبه ۲۸ اردیبهشت ماه، بر اساس «جزئیات درزکرده» از آخرین نسخه پیشنهادی ایران به آمریکا، از مجموعه‌ای از خواسته‌ها و پیشنهادهای تازه تهران که بر آتش‌بس، تنگه هرمز و پرونده هسته‌ای تمرکز دارد، خبر داد.
طبق این گزارش، ایران خواستار یک آتش‌بس طولانی‌مدت و چندمرحله‌ای شده و همچنین درخواست کرده بازگشایی تنگه هرمز به‌صورت تدریجی و با تضمین‌های امنیتی انجام شود.
بر پایه این اطلاعات، تهران به‌جای برچیدن کامل برنامه هسته‌ای، با یک توقف طولانی‌مدت فعالیت‌های هسته‌ای موافقت کرده است. همچنین پیشنهاد شده انتقال ذخایر اورانیوم غنی‌شده به‌جای آمریکا، به‌صورت مشروط به روسیه انجام شود.
العربیه همچنین گزارش داده ایران از مطالبه دریافت غرامت عقب‌نشینی کرده، اما به‌جای آن خواستار تسهیلات و امتیازات اقتصادی شده است.
بر اساس این گزارش، ایران همچنین خواهان دریافت چندین تضمین بین‌المللی برای هرگونه توافق احتمالی است و تلاش دارد پرونده دریایی و موضوع تنگه هرمز را از پیچیدگی‌های مربوط به مذاکرات هسته‌ای جدا کند.
در بخش دیگری از این گزارش آمده است تهران خواستار نقش‌آفرینی پاکستان و عمان در مدیریت هرگونه تنش یا اصطکاک احتمالی در تنگه هرمز شده و همچنین بر استفاده از ادبیات و چارچوب سیاسی‌ای تاکید دارد که امکان «حفظ وجهه سیاسی جمهوری اسلامی» را فراهم کند
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 198K · <a href="https://t.me/VahidOnline/75536" target="_blank">📅 17:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_O4mTCPbwYP9Pa-MythVuvxYxbS_65zBMcsG-n1nJqToO7Lkp8EARdKuaVTA6JOpxjacCz2p54kJsAeNSx16w2rszFRAaIihMeQ6yMXLkG2ADKy-JFVZ80-AhXPJ67Nvenk12oj33Y3cgfFgft2Q2xaOB1cT0jpWKqMaf_uRjy71-QqPVZhr7dxjinXvLFsTczq6GmHoPwqIfo_NPg3y98ZAtetTvG36VRU5-18msw9yGzCjcA9vtJAsus7BBgIUY7zIIVThFJg2ORNOSv9wAbFuiLqGSBjIFBC7EOlRlObxl4oMtUYR9XmanSlzNF3S0fH_dxXjOJ_0i7Bmjc8bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرگزاری تسنیم وابسته به سپاه پاسداران، روز دوشنبه ۲۸ اردیبهشت، به نقل از یک منبع نزدیک به تیم مذاکره‌کننده گزارش داد آمریکا در متن جدید پیشنهادی خود، برخلاف متون پیشین، پذیرفته است تحریم‌های نفتی ایران را «در طول دوره مذاکرات» به‌طور موقت تعلیق کند.
به گفته این منبع، آمریکایی‌ها در متن جدید با «تعلیق موقت» (Waive) تحریم‌های نفتی ایران موافقت کرده‌اند. «ویو» به معنای معافیت یا چشم‌پوشی موقت از اجرای تحریم‌ها است و به معنای لغو کامل و دائمی آن‌ها محسوب نمی‌شود.
بر اساس این گزارش، تیم مذاکره‌کننده ایرانی همچنان بر این موضع تاکید دارد که لغو همه تحریم‌های ایران باید بخشی از تعهدات آمریکا باشد. در مقابل، واشنگتن پیشنهاد داده است معافیت‌های مرتبط با اوفک (دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا) تنها تا زمان دستیابی به تفاهم نهایی اعمال شود.
به گزارش تسنیم، این تغییر در متن جدید آمریکا نسبت به پیشنهادهای قبلی، تحول تازه‌ای در روند مذاکرات به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/75535" target="_blank">📅 17:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRAZWZ1oWxfrCy1w4Wwh5AuXcpWyPhCUZ_l5hWgMAAmfTEqOBP1CMiVzZH5ndLPjMHfZOfxHSxq1apyhKjq3-fg5QlBfFyfM0WxHjMDOU2WLzfApqqpT2FwPwE_qTLhSbrUCai78oaB_20_VnZF89j1Z_nCqtROH9YIaVzzLxtlan5ctyqgFAcUZuROdlWVANQFRx-RZCnDvYD6QGN2ivfOSeE6vVE07ji5Xna1qCjLwLuaaOdfamdDm1-V3vexhre7JjYXcbZrI5yyEDGmI2b-u8eRvoLbMnQ9L7DPfUVbh9VetoI98ztQAU47nFhHrbMkq3L9435EPSHKHDMiIdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع آگاه گزارش داد پاکستان در چارچوب پیمان دفاعی خود با عربستان سعودی، ۸ هزار نیروی نظامی به همراه یک اسکادران جنگنده و سامانه پدافند هوایی به این کشور اعزام کرده است.
به گزارش رویترز، این نیروها از توان عملیاتی برخوردارند و با هدف حمایت از عربستان سعودی در صورت ازسرگیری حملات علیه این کشور مستقر شده‌اند.
این تحرک نظامی در حالی صورت می‌گیرد که پاکستان نقش اصلی میانجی‌گری میان تهران و واشینگتن را بر عهده دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/75534" target="_blank">📅 17:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPj1BSoEfdKc8ZwxkuwsnFo0TmnsY6HFniggeZYuFZ7c8Qk1382HWsZGrLchCiwJDkzleiU_oiJE5eJsoxunkO2mDG-JhFZM-RZZYFVwQJRRkJG8bLHzv-XqEQBWXq49OM-w0b5qYWXAdOyh0jErdwLwBMGRSPCWkT143B9s2uiW9Ew_5R0fj4KHpvX0Dyx3Uvyk-p5y5-ugwFkG-iI_o6lyC1f4FVRDp_t5hCNs-fmfAOX93pAyOiVYPdvcQEPGL9sNg0KQ3IqezWoLPmN6RcQ48RIOmAZC0i6_jcCZ075ViWVMvnVRv4kE_EOYxgJZYicWEO7aFsgL9rnDpklhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس کل دادگستری آذربایجان غربی روز دوشنبه ۲۸ اردیبهشت از توقیف اموال ۱۲۹ نفر در این استان با اتهامات امنیتی خبر داد.
ناصر عتباتی از این افراد با عنوان «گروهک‌های ضدانقلاب و تجزیه‌طلب» نام برد و آن‌ها را به «اقدامات ضدامنیتی و همکاری با کشورهای متخاصم» متهم و اعلام کرد که اموال آن‌ها به «نفع ملت» مصادره شده است.
دادگستری آذربایجان غربی اسامی این افراد را اعلام نکرده و برای اتهامات علیه این افراد شواهد و مدارکی ارائه نداده است.
پیش از این نیز گزارش‌های متعددی از توقیف اموال شماری از روزنامه‌نگاران، فعالان سیاسی و مدنی، هنرمندان، ورزشکاران و چهره‌های شناخته‌شده با اتهامات مشابه منتشر شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/75533" target="_blank">📅 17:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7YvO5NADGaPv9kb_fBvJfPAbNrEM003nO8qGqiikgp9jtE_Yq5V8zfipnFFtjjhrA9UTjNiduSO-SY68uPrh_BYzKi-53ckTnXSzwVBBzpB3c3vt9N8ER453axZqWNPZKEwTp2vFXJ_O9tfxZHhFemasw7mYetbqRH1ULcrbXmjEtGrVmJnVOQqikRPvXMSGpRk6_P6hjr6hjAy1GrkXb6_xmMpzf-2eabBI1ILY64Y7DN_B0IgF5fZt8FZzKYr_LdpNjdMO4tfp_mj_LcmCnV75L71OjvnPuXp9hiKD3t8scr2YHJBXaH1JTj-o9asW4O5WByY76osEbnIu3wGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا می‌گوید مقامات حکومت ایران برای امضای توافق با آمریکا «می‌میرند».
او در گفت‌و‌گو با نشریه تجاری «فورچون» افزوده با این حال آنها در جریان مذاکرات، «روی یک چیزی توافق می‌کنند»، اما «بعد یک کاغذی برایتان می‌فرستند که هیچ ارتباطی با توافقی که کرده‌اید ندارد. من می‌گویم: ‘شما دیوانه‌اید؟’»
ترامپ در این گفت‌و‌گو همچنین بر این نکته تأکید کرده که مقامات جمهوری اسلامی «مدام فریاد می‌زنند» و سروصدا می‌کنند، اما در عمل «تشنه توافق» هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/75532" target="_blank">📅 17:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75530">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Zzz6okLn-FZMLhzGSpHwyuZbtCeO3E96zAJzXK5uSy62jTYKE5Ax215-BzuuERmdrWz4-KQCLeF-jjXUItcLfXyDhTM_p0X8B5hDYc3AhvCk-WYbrQ9pLl3PA2nNfo7vWZDpE8hVLCXmPNq5d_LHR2B34hEdcxXNJwOLnERgocHRn8ggs4-Sjz9V8JNvhf7dY2qFtp9i-UPeVUS0ea3QkPC6dBfCe1Pg0wTP3nS0Ph8gJKLKG_BqNzEsGjSlL-0wq_pFeow8vF1O9swMdqje16Fxj7raC-dOHfL9vv9-BlPVTlYJDTvC2urGdU6LKRdPVIXb5W2Cojm38glYefuQ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uvKZpE4MvUaUlJDmWFfLPzfNa710GZvOrtEPrOeWNHCIfiURrcYvI0ChMFx4OteKtZ5HZTQBHYMGO-mfck3m-G9qwQsMMcT0yEwWYdi6QUZ4fXSCCk4CHc1s74aeP4vEVU4H46F6Ik06dGMXtzSCfIYRno7ydAwsrbzyQcx9PTNhDSzqpbYqJSOHohD1rg440LbCuLPAUyfhcYz1ohS4Hq_2FbVCYw2JUjeyHkAwaAJNitad9HqUo0VuXYWlxXeiUpYQXVj28WK0e5Jx0gmVuep6BS6xoEi4Po6d2BonhkGDizwvG7j0fz6jyWI_LA75jDvRInboIbeBaasHhSr0JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سخنگوی وزارت خارجه ایران می‌گوید روند مذاکرات تهران و واشینگتن، «ادامه‌دار» است و حکومت ایران از ایالات متحده، «اصلاحاتی» در پاسخ به طرح پیشنهادی خود دریافت کرده است.
اسماعیل بقائی در نشست خبری روز دوشنبه ۲۸ اردیبهشت گفت: هفته گذشته، علی‌رغم این‌که طرف‌های آمریکایی به‌صورت علنی اعلام کردند طرح پیشنهادی ایران مردود است «اما ما از طرف میانجی پاکستانی مجموعه نکات و ملاحظات اصلاحی را از نظر آن‌ها دریافت کردیم».
او افزود ایران بعد از این‌که طرح ۱۴ بندی خود را ارائه کرد، «طرف آمریکایی ملاحظاتش را مطرح کرد. متقابلاً ما نیز ملاحظات خود را مطرح کردیم. از روز بعد از ارسال نقطه‌نظر آمریکایی از طرف پاکستان، ما با مجموعه‌ای از پیشنهادات طرف مقابل مواجه شدیم که در این چند روز بررسی شد».
سخنگوی وزارت خارجه ایران به‌دلیل آنچه تبادل «نقطه‌نظرات متقابل» طرفین به یکدیگر نامیده، تأکید کرد که «بنابراین، روند [مذاکرات ]از طریق پاکستان ادامه دارد».
بقائی جزئیاتی در مورد اصلاحات مدنظر ایالات متحده ارائه نکرد.
@
VahidHeadline
او همچنین آمریکا را به «خیانت به دیپلماسی» متهم کرد و گفت واشینگتن دیگر «به‌عنوان یک طرف معتبر» در عرصه بین‌المللی تلقی نمی‌شود.
سخنگوی وزارت خارجه جمهوری اسلامی تاکید کرد تهران در مذاکرات با آمریکا همچنان خواهان آزادسازی دارایی‌های بلوکه‌شده ایران و دریافت غرامت جنگی است و این مطالبات را «حق ایران» توصیف کرد.
بقایی همچنین درباره تردد کشتی‌ها در تنگه هرمز گفت موضوع ترتیبات جدید امنیتی در این آبراه صرفا «مالی» نیست و هدف اصلی، حفظ امنیت تردد دریایی و صیانت از «حاکمیت ملی ایران» است.
او همچنین در واکنش به گزارش حمله به یک کشتی کره جنوبی در تنگه هرمز، بدون اشاره مستقیم به عامل حمله گفت «نباید عملیات‌های پرچم دروغین را دست‌کم گرفت» و مدعی شد هنوز مشخص نیست این حادثه توسط چه بازیگری در منطقه انجام شده است.
@
VahidHeadline
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی، در پاسخ به پرسشی درباره گزارش‌ها از قصد امارات متحده عربی برای حمله به جمهوری اسلامی و سفر مقام‌های اسرائیلی به این کشور گفت: «ما قرار نیست با گزارش‌ها این واقعیت را از یاد ببریم که تهدید اصلی کدام طرف است.»
بقایی با تهدید کشورهای منطقه از جمله امارات متحده عربی گفت: « اماراتی‌ها از اتفاقاتی که در دو سه ماه اخیر افتاد باید درس بگیرند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/VahidOnline/75530" target="_blank">📅 17:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75529">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoVRYpWZfFpcSqV94C6ffiT3YXBXgurYL8DqrQvsXEz9OB2zgRW_TiCEHiDUmB-zpjc5jprZNxbyhAW3rdxiBTbrVdE5TJhF3Is5SS0A0K-DOiyaGAAfOv47AK1MAwW62o3nxiXCoea_Ki_f8WixxIpf0DQDyKRKVn_8GadVLxxd5JWgYlFQvYylSJsdyFBVUtpJpVmIMpe9lPvmhF1LGmGck9rt8900Js-a2IDCPJD8kyIHmGhonboqv3yCwYG1P_di-4cYeHbQZOoWKhlP_5OjD9EK5y0fZ0UPTZ69Lh_5E_XNlZxa4F128OrbBelcNuhYVj73gjj7dgWCDRZlcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نت‌بلاکس» نهاد ناظر بر آزادی اینترنت اعلام کرد قطعی و محدودیت اینترنت در ایران وارد هشتادمین روز خود شده و مدت این خاموشی تاکنون از ۱۸۹۶ ساعت عبور کرده است.
نت‌بلاکس همچنین گزارش داده که هم‌زمان با ادامه محدودیت‌های اینترنتی، محتواهایی در حمایت از حکومت، شبکه‌های اجتماعی در ایران را پر کرده است.
بر اساس این گزارش، برخی شهروندان ایرانی که تلاش کرده‌اند به اینترنت موسوم به «سیم کارت سفید» یا اینترنت ویژه (اینترنت پرو) دسترسی پیدا کنند، گفته‌اند از آن‌ها خواسته شده سهمیه مشخصی از پست‌های تبلیغاتی روزانه در حمایت از حکومت را در صفحات اجتماعی خود منتشر کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/75529" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nQnuv_gTdL1LnMwG9r3haGdz_UAJCoqmPtnuHIo6L2JCDH-Mn0Kf54s-td-tEHJXW50_WXGzx5eyg88CvLX6AOg8rvCCHfWb5jA2Ph5o_8-TYW4anH3qnAkrCPweUjOfbhulmWJZy-u_ZhbAE8M9enaJ-vWtkt-sYIF6p9PZWUDzNZr9uDfbab54KOycCjqsG4Dmz33VjMBmV-ddLgWvsz_bTjwOI4hIkoL3tY6X1mjx8Gis8iAPk3RONFSGlm9P2rw6phH1E1UClwf6HFKEBxGm_EGEe7x-a5ToSLQwbmVMc6dC_tZ-2ehhlEK6735X-diy_GFwqBq-EbNobHh6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عفو بین‌الملل روز دوشنبه ۲۸ اردیبهشت گزارش داد که ایران در سال ۲۰۲۵ تعداد «بی‌سابقه» دو هزار و ۱۵۹ نفر را اعدام کرده است؛ رقمی که باعث افزایش آمار جهانی تا بالاترین سطح از سال ۱۹۸۱ به این سو شده است.
این سازمان مستقر در لندن اعلام کرد که در سال ۲۰۲۵ دست‌کم دو هزار و ۷۰۷ نفر در سراسر جهان اعدام شده‌اند، هرچند اعدام‌های انجام‌شده در چین در این آمار لحاظ نشده است.
عفو بین‌الملل گفت «هزاران اعدام» در چین، که بیشترین استفاده را از مجازات اعدام در جهان دارد، انجام شده، اما جزئیات به‌دلیل «محرمانه بودن داده‌های دولتی» در این کشور کمونیستی نامشخص است.
این سازمان افزود که آمار جهانی سال ۲۰۲۵، شامل اعدام‌ها در عربستان سعودی، کویت، مصر، یمن، سنگاپور و ایالات متحده، نسبت به مجموع سال ۲۰۲۴ بیش از دو سوم افزایش داشته است.
در این گزارش آمده است: «این روند بیشترین شدت را در کشورهایی داشته که مقامات در آن‌ها با محدود کردن فضای مدنی، خاموش کردن صداهای مخالف و بی‌اعتنایی به حمایت‌های مقرر در قوانین و استانداردهای بین‌المللی حقوق بشر، کنترل خود بر قدرت را تشدید کرده‌اند».
به نوشته عفو بین‌الملل، «افزایش بی‌سابقه اعدام‌های ثبت‌شده در ایران» در حالی رخ داده که مقام‌های جمهوری اسلامی، به‌ویژه پس از جنگ ۱۲ روزه تابستان پارسال با اسرائیل، «استفاده از مجازات اعدام را به‌عنوان ابزاری برای سرکوب و کنترل سیاسی تشدید کرده‌اند».
عفو بین‌الملل و دیگر گروه‌های حقوق بشری گفته‌اند که پس از اعتراضات گسترده ضدحکومتی در دی‌ماه پارسال و همچنین پس از آغاز جنگ با اسرائیل و ایالات متحده در اسفندماه، استفاده از مجازات اعدام در ایران افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75528" target="_blank">📅 17:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJRp3QueMpvyS1jnXvbiESQPDhf8iwCJYDvb51KSF5QxEj79wRj7G5rPGJGLOquKV5REGW2S67iKYAh8PkeRhjt4UD7EFPpso3RoeVXtBiae6sBKLq-4D6wRpCcJZR5Jh5QJIxvq1RjoPBXGN_cZc1gGNpHpRefkqqSby6PgwoY6nciCq_X7f1SdIKolJVEW1UFLjmF6MVfbkYsqL0TH_FhBtAB8nKjGX_0j1998FWj5IHZlBLYF3K-qyWXILOEx9N6PwZsRvLbpUNdZ3kmD-3tRu8weWXXVwQV4WwpF-0hCsEdSolvr1hsMgDhPg_s5xCvog6te17oI-EqHD8EfEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی افزایش تنش‌های ژئوپولیتیک در خلیج فارس و نگرانی از تداوم فشارهای تورمی، قیمت نفت در بازار جهانی انرژی افزایش یافت.
قیمت نفت برنت در روز دوشنبه ۲۸ اردیبهشت با رشد ۱.۲ درصدی به بیش از ۱۱۱ دلار در هر بشکه رسید و نفت خام وست تکزاس اینترمدیت آمریکا نیز با افزایش یک درصدی بیش از ۱۰۸ دلار معامله شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75527" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJKfnimSEm2VhanQpGUNxZNbS_tuuGN0AuGwydgWQNekiDBUxVlNzM5BwpyNZLhO7BBg5CTQm1cml4T-6ABwKbADBc3oXXHMYlihi8gMvs8ASIiZhLNb9EvPfEnfQGRdUYyPz_NQDvEr8mQgKiFTDiwZclrPYIVrdC4p74WwKHT-nbL0IJodJGGeevl3ZHSoqhCssh_PjQWOGfx_cDV5Ud1btuaz7O-2Hfc2j_6TXJ43H_sD3Uk5Lzz2o-SpAggzX8Df98Jqx_mLG4_yhInEaC-esZkPCdIQWI33MIj5YDYf0p9-SH-rDE8JCAQwWcxVd9eh44FofprU394jGVOXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در مصاحبه با ان‌بی‌سی در پاسخ به مجری که از او درباره بازگشت «پروژه آزادی» (هدایت امن کشتی‌ها از تنگه هرمز از سوی ارتش آمریکا) و از سرگیری کارزار نظامی پرسید گفت: «ما پروژه آزادی را به درخواست پاکستان متوقف کردیم.»
روبیو افزود: پاکستان به ما گفت اگر پروژه آزادی را متوقف کنید، ما فکر می‌کنیم که می‌توانیم به توافق برسیم.»
او گفت که ما پذیرفتیم و رئیس‌جمهور هم دیپلماسی را ترجیح می‌دهد.
با این حال روبیو گفت ما در حال خارج کردن ناوشکن‌ها از تنگه هرمز بودیم که دیدید رژیم ایران آنها را هدف قرار داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75526" target="_blank">📅 08:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75524">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S2XMh8pc_aYfW40ZkkkTmIhjy-1xim_8kNYWLo3k6K8sA0FZD-golYx6NiqbvcaWSF4m5s3vtMzejCACqTSoJrthZZFN6GbH6RT1wXwVk9jzNNdx1HqJrDJ4jQ--LnEtP3NINPmNS-w2P19733ckc_oE-W3U7XSTrviRt_kwIPCLdA1_iyM7LfDWH1_MJekQVDmF_t-rXUIo5ophXT-RJ3KnrofIz0NqN0cKmYhPQNBGAx5jEl1oQ-CkEDy-VdxCblOJodvaWYtEM2lPhvr0AUDHqhnnzk1aW5k3dZ2bN4abXpXEXIQZPck_DX6Y6xUC7MNTxckq_pjAZL3CT8jDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ترامپ به فاصله چند دقیقه‌ چندین تصویر مرتبط با ایران را در تروث‌سوشال بازنشر کرد.
ترامپ همچنین یک تصویر جدید از پرچم آمریکا را منتشر کرد که در پس‌زمینه آن نقشه خاورمیانه به مرکزیت ایران قرار دارد و از همه کشورهای همسایه فِلِش‌هایی به سمت ایران نشان داده شده است.
او همچنین چند تصویر و پویانما را بازنشر کرد که ناوها و پهپادهای آمریکایی را در حال هدف قرار دادن پهپادها و قایق‌های تندرو جمهوری اسلامی نشان می‌دهد.
@
VahidOOnLine
طرحی که سه‌شنبه از قایق‌های جمهوری اسلامی
پست کرده
بود رو
دوباره
منتشر کرد. ساعتی پیش‌تر اون
انیمیشن دیروزی
رو هم
دوباره
پست کرده بود. تصویر ساختگی یا طرح گرافیکی دیگری هم
منتشر کرده
با عنوان اینکه نفتکش‌های خالی برای خرید نفت به آمریکا می‌آیند.
اون پستش
علیه اوباما و بایدن با طرح گرافیکی قایق‌هایی با پرچم جمهوری اسلامی در کف دریا رو هم دوباره
منتشر کرده
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75524" target="_blank">📅 00:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75523">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqSwM9BxlGw_vea962PEqETXqIRYvDsvl179N_dUUBOG7VREbpa0QtSl8OEfI9IQn_D9DNMqMoWGbVwxFqG6ySMQBjv4LaQTxY40giLe2EvXp0zd8yPfcXvkMBRBbVV2ZlWYrMdXewN2T00meJ9oYDkeFWGam60GkV0RiHmPvIN8hKkfl0I9Z5XypaSNLPLaj-4UIrn8sWxiya6PIuMvcd_Qmw2tXUq-Z_0sT60sHyQjUDQWYz4GxP_STNijgY90BjkSxIQs6nK8euF-vwMT8I6MoWk0DYnYB9JtpYaq1BZnH8Zd1nAK7ci3lOOqpxCrfLkx8CUDmG-S5Mzevx93IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکی المالکی، سخنگوی رسمی وزارت دفاع عربستان سعودی، یکشنبه ۲۷ اردیبهشت‌ماه اعلام کرد سه پهپاد پس از ورود به حریم هوایی این کشور از سمت حریم هوایی عراق رهگیری و منهدم شدند.
سرلشکر ترکی المالکی تاکید کرد وزارت دفاع عربستان سعودی حق پاسخ‌گویی را در زمان و مکان مناسب برای خود محفوظ می‌داند و تمامی اقدامات عملیاتی لازم را برای مقابله با هرگونه تلاش جهت نقض حاکمیت، امنیت و سلامت شهروندان و ساکنان این کشور انجام خواهد داد.
وزارت دفاع عربستان سعودی افزود این کشور برای مقابله با هرگونه تلاش جهت نقض حاکمیت و امنیت خود، اقدامات عملیاتی لازم را اتخاذ خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75523" target="_blank">📅 00:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75522">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vehTAlhMtVQbSe3i6mWwHLy_NmI81TPeN5LM8lN0bVm5jddsteHMWSFjzPe1WuPa1IMTXKxHIrWbnnzyP-ASQSOiAYZEIMW7BaxRZgx4VBtGOSjDpoE2BFa1gxdmejlA6YcpwYc7jhtO6dxgKePO06K1-Kl5SNdZtcN-ZdMr6PNeYwRCmvJcyTWBInzg4MhVZzLsFc4uYclParf0MPucKcd9TXEoDGdy4qj4uvnUxpaTvuZZPbfYECnNS3fBkxxLOqk6wFnM24FVd-uesDy_D7b47BqJdeP5w8ilKb7wgfqhe28aI_NVctsj121SmXcuM1YydCXbwBWONl5BVEhWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبح روز یکشنبه ۲۷ اردیبهشت ۱۴۰۵ یک دستگاه اتوبوس در محور عسلویه به کنگان، پس از پلیس راه سیراف، واژگون شد و جان هشت نفر از کارکنان مجتمع گاز پارس جنوبی را گرفت. پانزده نفر دیگر نیز  در جریان این حادثه مجروح و به بیمارستان منتقل شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75522" target="_blank">📅 22:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75521">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MegRGBJ6MFBYQHRJBBlRkUshOd5NAR8MujD8maNxThF74dK_I1zRFAUrRIuXjrv4RPBa_EfT6Dvisk1i6BbM92zLlou9Zjoy87J0RKlZVzXh3450A-AuJN9cPOpwcbPVBYXe8jdnJtTqq6Hgtg4CXXIrnjUWlQmX5CkeX0naYE7Cznltoxq90wiSLemmpYmQ0K2mGay6n1LYlk-1wJy7gYEuCUlph9Xx4Jy5jxbf-cFQ_9C6R2OaDSN1XMGJIz0yKZucH72HgjIi-Nq5J3QDaG449BAw66WSoV-Dg4v0CBSQdnzbNnLbIHSD3gq75tcss9wBz0wPqwuMjfdy7Z18Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
زمان برای ایران به‌سرعت در حال سپری شدن است و بهتر است هرچه زودتر اقدام کنند وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان حیاتی است.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75521" target="_blank">📅 20:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75520">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMtXiPly6N1U7dmXT7TJ-Q2uSbqEeV2ZcS_ElaXW1bsVMefIyp8yr9L3iGYPO8ICyhHsYpYYCWFDHznwqDeCVMPUUI0EERvG8YE9sLnWYzht2ODAWO1KlSWAuCx-S269MRUCZOgiyQqIzptK5ScAB10FWBA7MdgqBcPtfNqs7eZi6AxVlpP6NKQeKVz_6duSv4icWa3xA4PrAbK53Iu8Efo4bUFWyZtkzpawKkEy6zMWj2n_zdceR3HtoQ5eMUilkSUEWugLZ-zWLm6HrpKCmcr5IXXwc-eQz_uqMO8C4Dygn1BXalKml_ptxxpihrVoQy2rtegUAwayz9a4mLqzFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دفتر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد او روز یکشنبه و دقایقی پیش از برگزاری نشست امنیتی، در تماس تلفنی با دونالد ترامپ، درباره جنگ با ایران گفتگو کرده است.
به گزارش تایمز اسرائیل، این تماس در شرایطی که گزارش‌ها درباره آمادگی آمریکا و اسرائیل برای ازسرگیری جنگ با ایران منتشر شده است.
بر اساس گزارش رسانه‌های اسرائیلی، دو طرف در این تماس درباره احتمال ازسرگیری جنگ با ایران و همچنین سفر اخیر ترامپ به چین گفتگو کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75520" target="_blank">📅 20:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AQua48E476j8n-dptWwFfN8d9Rf7l0AQ-LangQntn1jiW4chQ8T0HudDFuFfRrAtxSYd7l0Kut8bWbq-uEZnobggTY8JzJ6e-x-dT3M5UBkywDoch0f7ZYym6R_k6KzaIUVRGqlGjoescNcY3UtlEWxac8StEmbqsztSD5kQrSr4ITqINha1RuN1kx1tRWQ4UumpWhf_ojbFcRzFy0hoVv55NiQ17r6TSTcUntlzfGzxxCKWuXeqrPkfsfbCkG0v8_v59QrwzxCoYz4J47XPFCq7fqvHXOKSLuW3ENe-ftMTD6NvTP0Tzo9JBP7JhADhvbjwIaGljdyXrKgpfiS-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WTuacxSbaIES2FQMfoXLi0vhWxO2bYItkEaOcJ_sS11MMH5juV6nP6j_sHwG-Z7roX5B4KAmsnvgW5oxnS2gLnscURrGxy4616WE2-uNKGAiTxh8JD28QWGUHpLhlUNwYaxWDhcPVd93xWkE2Cr2KqoPUMimAbfPvZHfzIFlKK1seJ6Buru0y-6gvqN7Vm016xTBxcXz9Tyftw5nvLgPcV13AhaGJoZ-D9Mjm2GhV5PAzK_lGBFmQXRIaXZTgx_YPepoDjniZXlH1vKdw_OaccFtpEzMJvKCLbMsof1G0nadzGknrzb4qtDTqsPZk6ueezQ08Q9-XBYlk6wExk0Xtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cOSumR0hDWmfBzjwQbJDLLTN-zCNOWLEQDqp9PwuvSyQnv7irm7-D_MUqT_TDias7h0gVTvYSK15ioNPoSgG3I-flPJnJoYtcMN9U2x3-xdA6eQVzMtMazbXeCQWDejLJAJYxbFVzF0I8fUUM32Ttd_Uh_OLrtgx2X9E65h-1927RO-LiIbahllC170xl65EPys25Mo2gSMzEEIsAhR-5DVBmn5fcZ48msKg4o07VfN7za_8Au9S9Cv8TgGCbQ6Xt4a59xfnYzrkSvyRyCvPEGEAI3qMlIPlN7zgfeBnNN0YP3I-0bZb0U2UqR_0g7ykqLS7N6InG7rCmMVc7PEy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pz5UyTFblaPGxavH8fuq3IWGc5LIdlYyQpsCKYuhKcT4B7mlqYiW_i46anvyi8V0h59-Z6VHwBhSD9jUpXVmsf8n_-6IVsJCZVrimUpZR2JbppWPkzF7yR7slqd1IEkrXWVeiSKRkXn95H-5fNNsg5owmjJFRUc8Fjzb3pZ5RD_CI4z3CRlvfuEtLEqhXJlQ801MQMHQCM6xKelLdb311kJvfqmxJvhyoASkCqrEFSYsFv6AjwBSu4eUBqNrCuv3Se3o5eJ0wis6oUfbmV97Cbv9jumCimGGOsu-uz72lzn7XJi74DZ6uUemgAVuikygYx2VwmbNcPBpMP4LSUb7gA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75516" target="_blank">📅 18:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75514">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NiYk--2xR15ThY9vo3t5JgOuLJ4EpDIv1EoyuUuL7iWjN2enEDCp0AnZ0HxIFnQgcSOR9aGiY0MgnPUmbncxT4sM0JBm4ur4lppN4ypEe9SprIbtmUXR_fSyNC5xTHZci-MtfxJmaipzqYK4QJNpA3LUXquObo5ybVZkekMCoPYbd3vK0VdoP9_J6g-yevo90eXFOz-C64QkFdysad3RnLm4M0IZ_JO74XNety7--rOcXFu88ZggOcbUTw_R_xN2NA_aGjQeuo5nBskhd5pRKSQ_qZc_cLgEdO0H8sZu_Hd-v1HEyI7vcJ_wQwZehxJr0A8Ts-e6YiE1kxxSalyWZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TLZRYU9lp-gwHuniIfzN9NbAbt9eHTl1kp82oDdAqt_mZcvnfO1Lxkt1MuXfAGcztKLeMMBN1rlcHE9V7wRdA5VC_Os55VU_GMXh7AlA_t5Nf53AMAcu9Upg6uKn45u2tnaz29i2wEqmeFk-Gtt-MIj_0YCA_5CIKX4abyUVnIf6ml8DVIH69ruu-SAr8XVI5MfiP9onBC545IDIflwiuAshApX0C9ecjK4mtyHdLPqJGjL8YZMADzvENntbvT7Y-89i1FByie5l4xMvVorhzHcaPNRNvYSSQAYXkfire_qIYiQfi53OxDA5V1d2xBMmrcxdmzlxlkMl3Pyce7qPIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن نقوی، وزیر کشور پاکستان، عصر امروز با محمدباقر قالیباف، رئیس مجلس ایران در تهران دیدار و گفت‌وگو کرد.
رسانه‌های ایرانی و پاکستانی گزارش داده‌‌اند که آقای نقوی برای از سرگیری مذاکرات به ایران سفر کرده است.
گفته شده او حامل پیام‌ آمریکاست و پاسخ ایران را هم دریافت خواهد کرد.
به گفته سفارت پاکستان در تهران، آقای نقوی دیروز پس از ورود به تهران «نزدیک به سه ساعت در نهاد ریاست جمهوری حضور داشت» و اسکندر مومنی، وزیر کشور، و عباس عراقچی، وزیر امور خارجه نیز «در جریان این دیدار در نهاد ریاست جمهوری حضور داشتند.»
علاوه بر این، محسن نقوی «دیداری خصوصی» با مسعود پزشکیان داشت که «حدود ۹۰ دقیقه به طول انجامید و با حضور وزیر کشور ایران همراه بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/75514" target="_blank">📅 17:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75513">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbC9DuDgv6hqlh2imHJAzVRSeWyjhzZQ5o0TI7Ow6PuOxVlBq5c8MDC3aiQVYeNnfV3v8F0Gyolj9eIQI2hRaugGSLrn-hT6K3ovvosrTHLwmMM4VdmASasupIJwFFYZ5xF0IFpbCIVZHXxeTP2_BA_SKxzcb9a5qoqYeG8aWvWQTq-jxQ-E-yMfMZRdHInIR3uVpWPYjktGE33ZGV5PFJmlAhVrJYwYDqt-H5PxqjIyqDOuq3sCnMJyeh2HkzQAzHs6mwyf_H7jiWJSvEdE4Aih41Ne0gtu0S4zruClZnJ7R3vCMpo0OmZbyBURCIXJXR0DrdmkVFqrSqaDOx2vcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس با انتشار متنی مدعی شد جزئیاتی از پاسخ آمریکا به پیشنهادهای ایران در جریان مذاکرات به دست آورده است؛ گزارشی که در آن از پنج شرط اصلی واشنگتن برای توافق با تهران سخن گفته شده است.
براساس شنیده‌های فارس، شروط اعلام‌شده از سوی آمریکا شامل موارد زیر است:
۱- عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
۲- خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
۳- فعال ماندن تنها یک مجموعه از تاسیسات هسته‌ای ایران
۴- عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شده ایران
۵- منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
به گفته فارس، در مقابل، ایران انجام هرگونه مذاکره را منوط به تحقق پنج پیش‌شرط اعتمادساز دانسته است: «پایان جنگ در همه جبهه‌ها به‌ویژه لبنان»، «رفع تحریم‌های ضدایرانی»، «آزادسازی پول‌های بلوکه‌شده ایران»، «جبران خسارات ناشی از جنگ» و «پذیرش حق حاکمیت ایران بر تنگه هرمز».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75513" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75512">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsbO-fj41NJhwYlrpbKkylJoTLYqy55KBv-ij7Jj43rc6BHSlp8dD1fXpa3Gpmkzijm3hnxtQJjf4PvLrKSh0J3s_NfiUKhv9-Im9Iu36wY8gmCbEvaHPFHBtuxH3omshrUoCYLdz0M6DbG-Ywm4jN1ZuCGT19GxBGnutFKX9fhzuWO256rO5UrLhz_esyy_W7q9vorLbT3NfaT4ph5Xx6uFSqust19HH9F_lJXj2Lb9aY5e8kowmgWwJx5NsSr9TAOzgbMn8E6AIGwIdbHtHTEJOFeb5JejiF8nBmqb5EZ-7cNjorWUWOShz3mW8Euj3d0tkaTiU20g-egS4u9tiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در کانال تلگرامی خود اعلام کرد که کتاب «قدرت مذاکره» او به چاپ پنجم رسیده و در چاپ جدید این کتاب، بخش جدیدی با عنوان «دیپلماسی زیر آتش» درباره روند «مذاکرات غیرمستقیم با آمریکا در جنگ ۱۲ روزه» به آن افزوده شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75512" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75511">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkubrnXmWg-Oa1h7BZlg74ia9m2-4gbtOUteedJTGFK0Z4wq1d4l-JGqERu319AQfTedZ510_bwPpemT8xELhO2Jic-W0zgKL3Ut-AGCcZzb8dydK40Kb6RAnnoO9EivEVadyyhpPO9y30YldE7jvMGzXvQVoE6WgNZRvCIYACrP3OvnmN3CdzAq3MCkKbJTKDGgEwI895ZeRzsuHsqgzUOGbSJOpT994y9ek4bab8mDcbtmSUF3runRgJBKG8U-roFY2A0S4ew_C5WyLsb7T_jZ-RbjJwm-_U3sV-0OzRDy722dAZ3GLY4x3LUOronFfsav7cXgE7IeO1WkeRpz3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اداره رسانه‌ای ابوظبی روز یک‌شنبه ۲۷ اردیبهشت در شبکه‌های اجتماعی از وقوع آتش‌سوزی در نیروگاه اتمی براکه در امارات متحده عربی خبر داد.
این آتش‌سوزی پس از حمله پهپادی به نیروگاه اتمی برکه در منطقه الظَفرَه آغاز شده، اما کشته و مجروح بر جا نگذاشته است.
بر اساس توضیح اداره رسانه‌ای ابوظبی، این حریق در ژنراتور برق خارج از محدوده پیرامون نیروگاه به راه افتاده و بر ایمنی سایت اثر منفی نداشته است.
در پی آغاز حمله مشترک آمریکا و اسرائیل به خاک ایران، امارات متحده عربی به بزرگ‌ترین هدف حملات تلافی‌جویانه سپاه پاسداران تبدیل شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/75511" target="_blank">📅 17:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75510">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UogdBLnr8BfAXdzb63vOP-YDNSy2g8rCDYnRb57mYbZtxElL1njG0gTVg4o1qdvQ0q3_NrJthGHkRkFMmt7jSzcZUYvEofI8elTGqUTiIQ2tf1EYaw3eDbFXh3SCG0IyOk-UIAyg3S9oZPACLMokTKtu60azuQKF6buvbl1T6Ut76xHYVjXAoRiiE4Fl9zyXiOOJjoSILsedMe2W7b6jhT9pvA9qdA4ru5iVEMRUEh7RH-uFsIBJtUintndUY8DklawxoIAIrdZQaoHy0n9k3PpB7TFCkt1xNXSA6SKLx-otGqUakoq9O40v1UiI1R5LedtXbt1yh9tgJ5QvRxVG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، نزدیک به سپاه پاسداران، روز یک‌شنبه ۲۷ اردیبهشت نوشت که محمدباقر قالیباف، رئیس مجلس شورای اسلامی و عضو سابق سپاه، به عنوان نماینده ویژه ایران در امور چین تعیین شده است.
این خبرگزاری امنیتی بدون هیچ توضیح دیگری تنها نوشته است:‌ «پیشتر علی لاریجانی و عبدالرضا رحمانی‌ فضلی چنین مسئولیتی را برعهده داشتند.»
🔸
در این خبر نه توضیح داده شده که چه کسی یا چه نهادی قالیباف را به این سمت منصوب کرده است و نه برهه کنونی چه اهمیتی دارد که حکومت تصور کرده است به این نماینده ویژه نیاز دارد.
اعلام تعیین قالیباف به عنوان نماینده ویژه در امور چین دو روز پس از دیدار رسمی رئیس جمهور آمریکا از کشور چین رخ می‌دهد که در آن یکی از موضوعات گفت‌وگو ایران و تنگه هرمز بود.
کاخ سفید روز پنجشنبه ۲۴ اردیبهشت اعلام کرد دونالد ترامپ، رئیس‌جمهور آمریکا، و شی جین‌پینگ، رئیس‌جمهور چین، در دیدار خود درباره گسترش همکاری‌های اقتصادی، باز ماندن تنگه هرمز و جلوگیری از دستیابی ایران به سلاح هسته‌ای گفت‌وگو و توافق کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/75510" target="_blank">📅 17:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75509">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MMy_sKFPMOWSA0zUsgXGcomtCnnA5ep2Ah9kJiy44nQwtETjPXP4wY94HYtTSgznygbSNrqq8YXnbkOnBBclM2F_DPI9ohKK3PZVIgqv_pf5qnLPIVyH-4Hh-oOILNHaClLzIzulyyWSfpqeeIgSa-cio65AaYbVsjwkxtLHscE4SuO2C4ke9jXlOlRkRTqT1f6ZDQ5hLoJ4E6tl65qyZZCUgaLpwXrS2th1mfhZk5SrAQIdBQFnGyaNjWXk7xtUKX_py8YL4jHwEf9EYER89nCX_1Am-tKYNlEhvCOB8Z2nuNbxQU-L8FXmvJB1fQlVlhr25tUvsbFw4YM_YvC3iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسه دادگاه صادق ساعدی‌نیا، مدیر کافه‌های زنجیره‌ای ساعدی‌نیا که در اعتراضات سراسری دی ماه گذشته به همراه پدرش، محمدعلی ساعدی‌نیا، بازداشت شده بود در دادگاه انقلاب قم برگزار شد.
کافه‌های ساعدی‌نیا از جمله کسب‌وکارهایی بود که در اعتراضات دی ماه پارسال که با اعتراض بازار به نابسامانی اقتصادی آغاز شد، مغازه‌هایشان را تعطیل کردند.
نماینده دادستان قم در این جلسه آقای ساعدی‌نیا را به «فعالیت تبلیغی یا رسانه‌ای برخلاف امنیت کشور»، «اقدام عملیاتی برای گروه‌های معاند نظام از طریق انتشار استوری و فعالیت مجازی و حضور در تجمعات غیرقانونی و تعطیل کردن کافه‌ها و مغازه‌های خود در کل کشور و تشویق تعدادی از کارکنانش در ارتکاب جرایم علیه امنیت کشور» متهم کرد.
به گفته نماینده دادستان و قاضی، موارد اتهامی بر مبنای اطلاعاتی است که از محتوای لوازم الکترونیکی ضبط شده از آقای ساعدی‌نیا و از جمله تصاویر و چت‌های او در واتساپ استخراج شده است.
نماینده دادستان گفت که آقای ساعدی‌نیا در واتساپ خود «برنامه‌ریزی برای تعطیلی کافه‌ها را همزمان با صدور فراخوان دشمن به مشورت گذاشته بود.»
قاضی به او گفت: «شما با فراخوانی که داده‌اید با اقداماتی که انجام داده‌اید، این تعداد جوان را به این مهلکه وارد کرده‌اید و نظام متحمل صدمات زیادی شده است. چطور می‌توانید جبران کنید؟»
@
VahidHeadline
نماینده دادستان، مواردی از جمله فعالیت‌های ساعدی‌نیا در فضای مجازی، تهیه کلیپی از یکی از کارکنانش با نوشته «جاوید شاه» روی دست، ایجاد و مدیریت گروه واتساپی کارکنان کافه‌ها، انتشار پیام صوتی درباره خاموش کردن گوشی برای جلوگیری از ردیابی، حضور برخی کارکنان در اعتراضات و برنامه‌ریزی برای تعطیلی کافه‌ها و کارخانه‌ها همزمان با فراخوان‌های اعتراضی را از مصادیق اتهامات مطرح‌شده علیه او عنوان کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/75509" target="_blank">📅 17:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IBIpoBDxofdednS4cgQhEJYpIrw8AOn1WxC4xSnKvXQ_RhWgVvjL-lpwZ0Wst3zqTGw7Mqs8BPwzaTVZJn8soP8GjpxWb43hzaGbWD92Ch8kRU2_cC6ABJvYMb83lBSW5aiSZRg_yYwPFq1kLL1pCbp5zztG9-MIY3u40KG8SpZ_Xv7JbIsXytZiPGwz1KaqMpAwEMzY15APcE8kthYOTEdl3QSMztd4Ueq0C2PzgzYPnbfRW_GrdHFLdsKMBjKnhGXjqROhT-Wwx1Xf1SrqE33rpllBQp3zBC2VmgmB74rKD9PoNyZqyCA0-U0BMNKKoDaZdv93XwjqBg59GKX_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه تصویری گرافیکی از خود در کنار یک فرمانده نظامی بر عرشه یک ناو جنگی، در فضایی طوفانی و در میان شناورهایی با پرچم جمهوری اسلامی، در شبکه اجتماعی تروث‌سوشال
منتشر کرد
که روی آن نوشته است: «این آرامش پیش از طوفان بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75507" target="_blank">📅 23:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2db463b161.mp4?token=oMxq-qM_DueQ7CaryujBRGpcpUY5RxaT_sHcNLJ8PB_2ctHZjBBA9MAsW3Fk-KqGbyGClu9lYVbaX2R1hS6XJx9hkt8C_adFS8nGmjNR9tQ15FBRHU6BC7QfygdcBxi6HHMCtfFe87DTOCj1qYSMVEHDP-HKjW5XsXFT9_apn5KzGQUJ26lj0qDMSc_nxDSsGz34cFKJRHJnI-8Zw0CzFCw7CGVE49er4ON10gFW-iodORJJYPHdnMoqhWHIueg8n6UmH2fzPTBggA1UGmUFzUKljMgXxNascum_iz7p9q_Ox4gwzbyDY8CT41oAKaVOyXJHCS46HE8QvF8Jpgqcuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2db463b161.mp4?token=oMxq-qM_DueQ7CaryujBRGpcpUY5RxaT_sHcNLJ8PB_2ctHZjBBA9MAsW3Fk-KqGbyGClu9lYVbaX2R1hS6XJx9hkt8C_adFS8nGmjNR9tQ15FBRHU6BC7QfygdcBxi6HHMCtfFe87DTOCj1qYSMVEHDP-HKjW5XsXFT9_apn5KzGQUJ26lj0qDMSc_nxDSsGz34cFKJRHJnI-8Zw0CzFCw7CGVE49er4ON10gFW-iodORJJYPHdnMoqhWHIueg8n6UmH2fzPTBggA1UGmUFzUKljMgXxNascum_iz7p9q_Ox4gwzbyDY8CT41oAKaVOyXJHCS46HE8QvF8Jpgqcuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، انیمیشنی در تروث سوشال
منتشر کرد
که در آن به ناو آمریکایی دستور شلیک به هدفی با پرچم جمهوری اسلامی را داده و می‌گوید: «در فهرست اهداف‌مان قرار دارد، آتش!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/75506" target="_blank">📅 21:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lrPQC45T_kYk_NU6B2vHWIJzjGtsdYWkZfKGinNVC-bEKQI19k0RfRGqp92cKOQXlcJpP1_wKF7ygFfStrUYMrEzNZklzV_ZZ9xj2ERNYyUDmDLkGz9N8YZkezGDVbvkPoP54KWrdcSdtgSNznDYI5BXKSyhCY6vzMswgY3EH4TMpaibO35sXIXL5XOTvjtbohIQi6AUTk05EmWqq3Hn9_WbdNfV3kZ4_XjCThrP9y1k5izZilIj-UhrPkDVHPGMUWTXO4AY1KZSJI5JiTn-qf856cbNu3v2pUST1a9QU-PXcOInCvoz0f1nRenGbQLmbSdRcmbCMAfDgwPKpTc0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n2J9QDuF5RHEy99VSs8pz9CBs2aI_l8y95EE_blm0MIgk9s10N0XDh6DkMhQfttzoNyswGwK-D5wR-u5iGLvbF87az8PJ-NPwqo-RQ2KCMg9IIa_e6FaSJTcS4ZNasFI_EDCW7yyPOYCtrkCTc05beX8ScbFsFwGLlScwfktOW1et_xc5LYuwI4ra8LJmVl9fL-TlIUYWKEP_EvLmnN9QMzMtNFQT0eGokWQi3HQLbEbC9aZH4hU_xgSNl8E0cSW2yzkN_b8n-UO4YaKxOc-X6Sbcvq-rje5AFvsIqckMi6q9FxPzNyxsE6fky4hhex0-Nk0Qp1g9WuqcB7-GpFOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gXtVwLNzsvjvfUfXb_RfIb2yJXj8ALoHiCwW3sLty-i5SppigA9CEzQZkAUXyzqSe__m8vQO3Eu3CmZz7ftRBQTzpcKozZE79FkFiDkfkT1rY3S5qB9SteB99B8ZLLSgvnskLbqd6_C-n_5AasR7uRht6-GvtVjK9cndod7ABf5oU-WgQWXgMxDksClkHbL1J7NPaGCuQnbQIA9uYHvuf1jw0KtSPiTVH9Dffcr38TJ7q8Xygw06cc2RYhbv0rXoR7t3k_z7DC1-Q2LBYvsea2F6Bm6J89xagfBcivwmwrWRmlHIk51f0MbxCzgHmO7j1mFL1GoBXwN_ckA87Z411g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EJ1kw5dnsAKms93SFX5PVMJEtXlO86xxCMJBfAN-MgAUe0reNk3AGTPDsXU12WN_8Deamse1-IXLSBZwlVb0qFlsMNBttLGDhvFA5xUFuHajJLf74qTwEwNHJ6B3JhkZKhDjdkkVBbGv48zn_kzvrxzwc2_qNn3bsuSOYzbJ-QrNYdAEgr77OfXrBh--WX9mAt3HtINmxXClDPK3KuMbn0uV-1K35tUBhyjX7vLSEoPMHbx_KpUFNPY6denPfwC7dv5tQIvDY0ldlzWIbPb-yAqT0upW3D4wfMLRRnluwC3MnIwgPXnB1JqZMQccdcCEcghROuf7pmt7wl-uqNx7MA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=ZpNO9i7OU9gFTqvcrxq5yAVcA9uCeatezGYWu7nGrAGWzxIEy54Yy-0EntacPpBnlNg3nd3b_Lg9wtJs4EymDqKLDaOrX8IA-1Hx_8B6Qh2onSt1oi755YDtiVZiXAGVU5gpxNXVk3z7ix7OT3NX664gj8m24ilyEU5uLoOK4fJS3mXU83EB1CUqTEPR057tKi2T6eExGN3_N2cc5dg9CQhDzxcTuzBycBhaVRCYybDtx6pn63WyQsXqWMMJEB71dSj6Cg784OP1zR7AfeZqK0-UPrQrobsPF4nO7oLfLacMg9_4R4q9cNEp0Ra24x8GwejpIQVtubdVamyvoJzkiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcb834d170.mp4?token=ZpNO9i7OU9gFTqvcrxq5yAVcA9uCeatezGYWu7nGrAGWzxIEy54Yy-0EntacPpBnlNg3nd3b_Lg9wtJs4EymDqKLDaOrX8IA-1Hx_8B6Qh2onSt1oi755YDtiVZiXAGVU5gpxNXVk3z7ix7OT3NX664gj8m24ilyEU5uLoOK4fJS3mXU83EB1CUqTEPR057tKi2T6eExGN3_N2cc5dg9CQhDzxcTuzBycBhaVRCYybDtx6pn63WyQsXqWMMJEB71dSj6Cg784OP1zR7AfeZqK0-UPrQrobsPF4nO7oLfLacMg9_4R4q9cNEp0Ra24x8GwejpIQVtubdVamyvoJzkiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر جمیله شفیعی:
JamilehShafiei
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/75501" target="_blank">📅 17:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=pILOyzVrhBhPpoxKXzl94fXVIFCi6gR9NZsbQR_u8WwVyaGcLSoC03mWgvg-JnLKcGgsB5mRGuyN9EjPCUsEj8koLBIqpH3kyp386F3-wzAXr788YTfYTLOnSMNIUeEERbAmfpk0Y-JG90bkg-ySUa6uwXHyaF92EpUovPMbB-BQtQePRK-Q2NVuiD4lTIfa22eN10QEiAlNjxTB36pDz2ZAQFl-4IPhgE5WtJxVlHjRRuQ-8Ch7JFnw-U1KIQFrlOj0K2uopExojU_hKSDECp6rn0HzSt_xQKP9hSLfX5SBiCQ8bpcg7G4qbttgayTabY49BlApHvfugdW_wQuaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ffe0351e23.mp4?token=pILOyzVrhBhPpoxKXzl94fXVIFCi6gR9NZsbQR_u8WwVyaGcLSoC03mWgvg-JnLKcGgsB5mRGuyN9EjPCUsEj8koLBIqpH3kyp386F3-wzAXr788YTfYTLOnSMNIUeEERbAmfpk0Y-JG90bkg-ySUa6uwXHyaF92EpUovPMbB-BQtQePRK-Q2NVuiD4lTIfa22eN10QEiAlNjxTB36pDz2ZAQFl-4IPhgE5WtJxVlHjRRuQ-8Ch7JFnw-U1KIQFrlOj0K2uopExojU_hKSDECp6rn0HzSt_xQKP9hSLfX5SBiCQ8bpcg7G4qbttgayTabY49BlApHvfugdW_wQuaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"مجری شبکه سه تلویزیون: یک راکت ۲۰۰ دلاری می‌تواند کل ارتش آمریکا را در منطقه به زانو درآورد"  ویدیو با تیتر بالا در منابع جمهوری اسلامی منتشر شده و خانعلی‌زاده متوهم رو نشون میده که مطابق معمول چرندیاتی در سطح خودش میگه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75500" target="_blank">📅 17:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=sCfC1LVE7A2vQCn5SK6DtpQFJA_Qca_l3VliAXW24lteIIyYLAazQ5mX3XbVDMXhGvrJHJJJCrVjPOPOqlUWrAuh6q9Gn2j72JDuwydVCdYsczdRozoGD-Oec7GPxidlWAWxdvysvjByTY2gL2chBuxbdUpURUdHCx1upWU8_1vuaQgK2-Y_Kd43Iuk_yRWobGicSMJqTZnfjTaGrKB6ln5Ple5CJ_fECb1MLOI_T5gm6ZSacRirlsUfPiXCzrKpRqqXDJ46C7t6lAmPI6a1TQVo6HKNc6KvGHZpETqtz5KDnu3u3ImCzG5c_otx2x_3d76iXsyM2zsoI9V8QT4a_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/46bd8e2257.mp4?token=sCfC1LVE7A2vQCn5SK6DtpQFJA_Qca_l3VliAXW24lteIIyYLAazQ5mX3XbVDMXhGvrJHJJJCrVjPOPOqlUWrAuh6q9Gn2j72JDuwydVCdYsczdRozoGD-Oec7GPxidlWAWxdvysvjByTY2gL2chBuxbdUpURUdHCx1upWU8_1vuaQgK2-Y_Kd43Iuk_yRWobGicSMJqTZnfjTaGrKB6ln5Ple5CJ_fECb1MLOI_T5gm6ZSacRirlsUfPiXCzrKpRqqXDJ46C7t6lAmPI6a1TQVo6HKNc6KvGHZpETqtz5KDnu3u3ImCzG5c_otx2x_3d76iXsyM2zsoI9V8QT4a_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک برنامه زنده تلویزیونی که از شبکه افق صداوسیما پخش شده است، مجری برنامه با اسلحه واقعی به پرچم امارات متحده عربی شلیک می‌کند.
در این برنامه که موضوع آن درباره آموزش شلیک با اسلحه کلاشنیکف است، فردی که لباس نظامی به تن دارد و صورت خود را با ماسک پوشانده است مراحل آماده‌سازی اسلحه و شلیک گلوله را به مجری آموزش می‌دهد.
مجری برنامه هم در مرحله شلیک تصمیم می‌گیرد به پرچم امارات که در بنر مربوط به دکور استودیو، شلیک کند.
@
VahidHeadline
صدا و سیمای جمهوری اسلامی جمعه چند برنامه پخش کرد که در آنها مجریان در بخش‌های استودیویی با در دست داشتن تفنگ ظاهر شدند و کار با سلاح‌های سبک آموزش داده شد. مجریان در این برنامه‌ها اعلام کردند که در صورت لزوم به جنگ خواهند پیوست.
این برنامه‌ها که دست‌کم در سه بخش پخش شد، در رسانه‌های داخلی بازنشر و در شبکه‌های اجتماعی با واکنش‌هایی همراه شد. برخی کاربران شبکه‌های اجتماعی این بخش‌ها را نشانه‌ای از بسیج در شرایط جنگی توصیف کردند.
جکسون هینکل، مفسر سیاسی آمریکایی، در شبکه اجتماعی ایکس نوشت تلویزیون دولتی ایران نحوه استفاده و شلیک با کلاشینکف را به‌عنوان «آمادگی برای تهاجم زمینی آمریکا» نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75499" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EN1JLUOr1iHcgKNYH7yaFnHJfiAFjThD769v7eUzJm7EB6Ow3by1jUlSkpG_mK_Yz2prFoCKDwSEbCV7YujE43UPl2uJQZo7Ip826FxMVlbTLv2LyAKZhTulg0kpNKrHqFkwNdHlE43Nqr0y83-sw2vQivEBQ_AkIQtIx588rVkbcEan4CbLssFk0yJOfM2Gg_4lRKiP9f6zR0QbyvvjSqYJaJyg0zP8ZBTakPkHJBiYR4mw9-uJrhIyBczNzQSXuvE8EwgD-PkLR_kFAirNEUk_WQwAY6rRG8xYoEYx6AZdRQ0surDrdPV2dIjZUC7rjHSYj-tpbVvlvL1J60_3ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه وابسته به قوه قضائیه جمهوری اسلامی اعلام کرد اموال ۵۱ نفر در استان یزد، با دستور قضایی و به اتهام آنچه «خیانت به وطن» و «همکاری با دشمن» خوانده شده، توقیف شده است.
بر اساس این گزارش، پرونده این افراد در ارتباط با قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی علیه امنیت و منافع ملی» در حال رسیدگی است و مقام‌های قضایی مدعی شده‌اند دارایی‌های توقیف‌شده قرار است برای «حفظ حقوق عامه» و بازسازی اماکن آسیب‌دیده از جنگ هزینه شود.
اموال توقیف‌شده شامل حساب‌های بانکی، دارایی‌های منقول و غیرمنقول، سهام شرکت‌ها و حتی اموال وکالتی عنوان شده است.
طبق گزارش میزان، از میان این ۵۱ نفر، ۲۰ نفر در داخل کشور حضور دارند و ۳۱ نفر دیگر در خارج از کشور به سر می‌برند.
این اقدام در ادامه موج تازه‌ای از مصادره و توقیف اموال شهروندان و مخالفان سیاسی صورت می‌گیرد؛ روندی که در عمل به ابزاری برای فشار، ارعاب و مصادره دارایی افراد تحت عنوان‌های سنگینی مانند «خیانت» و «همکاری با دشمن» تبدیل شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75498" target="_blank">📅 17:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75494">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EMQFHwS1GeMorT9l2oxN7V9KWRZbm_8MzZ3-UE6DinRa7ebdPk6RvFYa_NW4pXGPCZyIdN3u2XxXqNcmTzSmncb3jg-C9Z8Xa-tPfE1igRUh-eAn0ZKeIOGaGMdvyk9XOgxkKbS7KgxEKhYhQzntfntdmvy5_RPjSZg8BUry9sDAYzBc4wU5vWzBFNwJdTfCalGzrU9COHZX_ibm2ae76_DVOrnyigyxrrmp6zUUiNh8ikBokCLqVZBmZdUFiigWLH1VjZ7v1rfYdhtNeSYO6Zj3gEcQrZm3_MH6LMxyrQNAfRKjlujwC_grk5y5PTLbE0I-U3xSMrbWoD56w8WmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rgGomDLNrwp3CRv3B4vLQ_ImWaPHNxRBdyLgnqp_OEeEyx7Von6gs5wRW0h6AwpnmDjDYjAlXiXvpjmZM0OlH2n2T53D6XWwMkEcYA96n7Nnvrbs06j_dlRFACdlUW37Ev4aS1YVR_X0EdwIlB82MdISBG6hQBWeVMx4cFMY_ajkFRUk8cda0nc7FMyWkC6CczNvmUKLT6AqCbY8X1OVnlMxmQOOF5kJGhQSetV6yw0IvJHxf4ZjH3zRTGFM5PWDRC3_97KeepF2HoC683oYHDsn55pDNoM1JSYsYduub0cFipmX8aqasH5ny-JbuRIZVUbDABSycC6-gVWnkq-N6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T5PiCmsIcp2HnU0dNkUopxHIy0mGNw-vRfGPmhL-iXGP-FR8qJ3ImyvsK9GISEr4rxdsd9lLM9sd2jPD7Nx_Jw6CdKj88L28m8EYdoNbaNqedUHt1nWahBNMbNA1wZf9dalM0Ub_racIzG-8y_gzGfwuMQekzEnGNNzsUhqSC4EOgqnUiwyEYNEo1r-e05ZnhlgcTb1vp3uwOfUKL8S9HZ8iip9KYvYlCLVZFYNMzePWAQ96LoVi0IFFtVW1G9jbhAQEwELRvDsMnj76CYJFTpm7qw-QhpoJMLzn3HPNlGIqmyZcW1csUQlh8A2voURFTZTA-T1NM0BTQ4fYJiuzAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fhIRkBWx2Sy69QLwbAnmivzc8tdCq3s3aSmVzqdaYb25H76et6nWDnuhT8yI6hpYuSRCQZF0wiSVAVdDwaxhZb9lRI4CE98GOspYeqL_cJe6e2xYBumhP3wACYY2JUU3XxqcS-7gblviuWoFX4y3jl_1D86pGiU-6KVBOcHMfSZh-Q4240byeXe0TRWf7AvNbac8juooPcCeEQ5OKojpDR3baz_T6XU78thqgjUh_mGV_zaDz1mvd1y842dAJdiJwP7Ddr_2G3N23D_NL6s-_oezDTbyCqB3GlDe42iwcT6-FXZqnDvHHQFhPw3yj2nYCtI6ztzhgnnYi4seoBGSJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او تاکید کرد: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت حکومت ایران از نظر نظامی به‌شدت آسیب دیده و بار دیگر تاکید کرد: «آن‌ها دیگر نیروی دریایی ندارند. نیروی هوایی ندارند. همه‌چیز نابود شده است. نیروی هوایی‌شان از بین رفته است.»
او تاکید کرد: «تنگه باز خواهد شد. آن‌ها سلاح هسته‌ای نخواهند داشت و دنیا ادامه خواهد یافت.»
رییس‌جمهوری آمریکا گفت به درخواست مقام‌هایی از پاکستان، مرحله نهایی عملیات علیه ایران را متوقف کرده است. او گفت: «آن‌ها گفتند: می‌توانید متوقف شوید؟ ما قرار است به توافق برسیم. و واقعاً چارچوب یک توافق را داشتیم؛ بدون برنامه هسته‌ای.»
ترامپ در ادامه تاکید کرد تهران پذیرفته بود مواد باقی‌مانده از برنامه هسته‌ای خود را تحویل دهد، اما بعد از هر توافق عقب‌نشینی کرده است. او گفت: «هر بار توافق می‌کنند، روز بعد انگار می‌گویند چنین گفت‌وگویی نداشته‌ایم. این حدود پنج بار اتفاق افتاده است. مشکلی در آن‌ها وجود دارد. واقعاً دیوانه‌اند. و به همین دلیل نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا در بخش دیگری از مصاحبه، در پاسخ به این پرسش که آیا توان و مقاومت حکومت ایران را دست‌کم گرفته، گفت: «هیچ‌چیز را دست‌کم نگرفتم. ما به‌شدت به آن‌ها ضربه زدیم.»
ترامپ تاکید کرد آمریکا عمداً بخشی از زیرساخت‌های ایران را هدف قرار نداده است و افزود: «پل‌هایشان را باقی گذاشتیم. زیرساخت برق‌شان را باقی گذاشتیم. می‌توانیم همه آن را در دو روز نابود کنیم؛ همه‌چیز.» او گفت به تاسیسات نفتی و برخی زیرساخت‌ها در خارک حمله نشده، زیرا آسیب به آن‌ها می‌توانست موجب از بین رفتن نفت شود.
رییس‌جمهوری آمریکا درباره وضعیت مذاکرات با جمهوری اسلامی گفت افرادی که آمریکا با آن‌ها در حال گفت‌وگو است، به گفته او «منطقی» به نظر می‌رسند، اما توان یا آمادگی لازم برای تصمیم‌گیری ندارند.
ترامپ در پاسخ به این پرسش که آمریکا در حال حاضر با چه کسانی در ایران طرف است، گفت: «با افرادی طرف هستیم که فکر می‌کنم منطقی هستند، اما از توافق می‌ترسند. نمی‌دانند چطور توافق کنند. قبلاً در چنین موقعیتی نبوده‌اند.»
او در پاسخ به این سوال که آیا تا زمان دستیابی به توافق صبر خواهد کرد، تاکید کرد: «من کاری را انجام می‌دهم که درست باشد. باید کار درست را انجام دهم.»
او همچنین گفت مقام‌های ایرانی به او گفته‌اند محل نگهداری مواد هسته‌ای به‌شدت هدف قرار گرفته و «کوه گرانیتی» روی آن فرو ریخته است. ترامپ افزود: «آن‌ها گفتند فقط دو کشور می‌توانند به آن دسترسی پیدا کنند؛ ما و چین. گفتند خودشان توانایی دسترسی ندارند چون کاملاً نابود شده است.»
ترامپ گفت: «نمی‌توان اجازه داد ایران سلاح هسته‌ای داشته باشد. آن‌ها از آن علیه ما استفاده خواهند کرد. اول اسرائیل را نابود می‌کنند، بعد خاورمیانه را، بعد اروپا را.»
او درباره افزایش قیمت سوخت در آمریکا گفت فشار اقتصادی ناشی از بحران کوتاه‌مدت خواهد بود و افزود: «وقتی مردم توضیح کامل را می‌شنوند، همه موافق می‌شوند. این یک درد کوتاه‌مدت خواهد بود.» ترامپ گفت پس از پایان بحران، قیمت انرژی «مثل سنگ سقوط خواهد کرد.»
رییس‌جمهوری آمریکا در پاسخ به نگرانی‌ها درباره افزایش فشار اقتصادی بر خانواده‌های آمریکایی در پی جنگ با ایران و رشد هزینه‌ها، گفت شهروندان باید این فشارها را تحمل کنند زیرا به گفته او هدف، مقابله با تهدیدی بزرگ‌تر است.
ترامپ در واکنش به این موضوع که برخی آمریکایی‌ها افزایش هزینه‌ها و بدبینی اقتصادی را احساس می‌کنند، گفت: «باید تحمل کنند و باور داشته باشند که ما آن‌ها را به نقطه بهتری می‌رسانیم. اما من باید کار درست را انجام دهم.»
ترامپ در ادامه، فشارهای اقتصادی ناشی از بحران را با ضرورت مقابله با جمهوری اسلامی مرتبط دانست و گفت: «به مردم گفتم متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا همچنین گفت کشتی‌های حامل نفت ایران که چین در روزهای اخیر خارج کرده، با اجازه واشینگتن حرکت کرده‌اند. او گفت: «ما اجازه دادیم این اتفاق بیفتد.»
ترامپ در پایان در پاسخ به این پرسش که آیا حکومت ایران در نهایت عقب‌نشینی خواهد کرد گفت: «بله، قطعاً. هیچ شکی ندارم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75494" target="_blank">📅 07:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75493">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lREYotXeXlfjpTloWN4wt8s54RsVF2_cxCMTv_FOpwG7LOTtyqN0ry10lyXUxC0WwliO4abYNbQLjab-HN-Yve7N96BPf3WacRUFNRfrl1iiJ3YXEqB1B59sXXxiyyg_vjVE_Ffp8DoCizMrHa3IEmU3S4L1UYgtITI42WP6hwodtr9j0JIv8PI8Am81-vRItUsy7GcbaXID3r4A7IfI5rkX_XcWLL8y97iV7WSZPtnWKugTQksKP9U8ub7_GnRK89QnJVpsD2BVT9EZOxDLblL3W1vXH4WkwbcP-uQJxcM7UUIc4iSBNgx-gHWfWO8DRkC0_wRUbczmBINc0kR0dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، در واکنش به بالا رفتن قیمت انرژی در آمریکا، در ایکس نوشت: «در حال حاضر، افزایش قیمت بنزین و حباب بازار سهام را کنار بگذارید. درد واقعی زمانی آغاز می‌شود که بدهی آمریکا و نرخ وام‌های مسکن شروع به جهش کنند.»
او نوشت همین حالا هم میزان ناتوانی در بازپرداخت وام خودرو به بالاترین سطح خود در بیش از ۳۰ سال گذشته رسیده است، اما تمام این‌ها قابل اجتناب بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75493" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75492">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyufV3wkb4Cxy8ZZJ4sv5dn88Dlsn1OoSyjO4IofxXcAJltuhuJSmNKdeGuWjAyc1EM3HQ7pOeW-bmudGBuGVCQOffF_xSKk-e5D2Gptr89dIKl00VTGXtSaFJuvhBGrdJBXaTiDjXHrbib9BhBgmxiDf6D0-pzQZKu5YXny6DcbrX-HKckhbdvqqbE-iihcpcvBVita0l5R46_ymmQoEh2qxwIPlXbF012bhpyZYeNIt5nyykkWcfFGYHMu3sxLdx_WRsRdcU8_AjykcdlbopasWcku5g6FBkQpqReG3OnoFSoSjA7qLWzAfrzPVU1UU1PCnFWlQ7N3iMA15KjSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ نماینده چین در سازمان ملل و و رئیس دوره‌ای شورای امنیت، از پیش‌نویس قطعنامه پیشنهادی آمریکا و بحرین درباره تنگه هرمز انتقاد کرد و گفت که «محتوا و زمان‌بندی آن مناسب نیست و تصویبش کمکی نخواهد کرد.»
به گزارش رویترز، این پیش‌نویس قطعنامه از ایران می‌خواهد که حملات و مین‌گذاری در تنگه هرمز را متوقف کند. اما دیپلمات‌ها گفتند که اگر این قطعنامه به رای گذاشته شود، احتمالا با وتوی روسیه و چین روبه‌رو خواهد شد.
دو کشور ماه گذشته نیز قطعنامه مشابه مورد حمایت آمریکا را وتو کرده بودند و متن آن را علیه ایران «جانبدارانه» خواندند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75492" target="_blank">📅 07:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75491">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QQkd_9DDupJuCD47_Zbu_CaygSLHjAM-HvVkPhJIHKxV51KZOXpH6UBNybtwnEva3exY-vmzfp-lcbdIKRo4A1t_osgm4TfOsuwwQ9zb_hSyxg0mXnhA5Xi1wiiPgDYmBxxbTOEMRF3xQMP1W_QALqPO2212YNRQnoHnENULgVduBtN0sJf52uC41jEwGdygcBcEiFhxRsfUPbX028EnfCCHEE39pedNGdx7Ldc2L4uPWgPZXysDplo-S_DUzLGBiP6gz44BzZDWyndePVruaz-0qf3NT_3514Szw1dximGMqbwM3Xls0p1Bm7XR_Nf7NsWCXDQfiQ1hyqH0x0VAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرزند عبدالرحیم موسوی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، گفت که جنازه پدرش که در نخستین روز حملات اسرائیل و آمریکا به دفتر خامنه‌ای کشته شد، نزدیک به ۳۰ روز زیر آوار مانده بود.
موسوی پس از کشته شدن محمد باقری در جنگ ۱۲ روزه، به‌عنوان رییس ستاد کل نیروهای مسلح منصوب شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75491" target="_blank">📅 23:25 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75488">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uub44hcpfaMhL9IWhDoIZXPbPOGBvhUZjvnh23IeERKcuMw5MYktoe4nTyIL-1fYTg3jmU_Ti63vfqoRpxiFwAdhxRdvjMybDkkT0YRfwnPzGSaGbtu8UkRtCmwlGj57bh46vNEwvL__qFC8NXOaMsCyHSMBTws3HhjbudUZBA58JLIe2D23NhbJz0olwbpnNgZwmX7i-F50z5e6WZRg7WN80GYVeAsQsV9gV_LlANWtmvMvn-QijYCI_4Zbo5uhI29W233UD72niiyKGEkRmTvRI5UoWxYr185Gb-BBHUYo7ZuxlpYn8RGZ8MNtXyCWRGhpAKHIFGI9q-qterO3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db61779f21.mp4?token=mnFYeyeNM2b1HuY7vrIfl4FKdkmAyjIlXfScWepuJKKm1gSzypGl-MTPtsYwSG6jV7CJ_ICKFhRSEWlEqUKTPeUsCzAT3Wintbo8pDfzoEMM24nJ2n2Pv5exIxZVzRrWJ2obFnYCEopVeb2BPSS4o5goNCw_hbaZ15ntjmrc0g-G4easE0mFJ-ZcrE1e2on9aU8vpAR-dLwCpZslpN9KDVbtH_-bfv8NfqbgdjtHucWPgjzNLKrTVfy5ZZB45yMjBPOH7bUqVhpU1wmXBiZYJZLt8xaK0ENqGrZt_MMAmX3FcXLxdDQZYT2NGUQpoLNuwFGBiaEsW8vh3CYVM0IA_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db61779f21.mp4?token=mnFYeyeNM2b1HuY7vrIfl4FKdkmAyjIlXfScWepuJKKm1gSzypGl-MTPtsYwSG6jV7CJ_ICKFhRSEWlEqUKTPeUsCzAT3Wintbo8pDfzoEMM24nJ2n2Pv5exIxZVzRrWJ2obFnYCEopVeb2BPSS4o5goNCw_hbaZ15ntjmrc0g-G4easE0mFJ-ZcrE1e2on9aU8vpAR-dLwCpZslpN9KDVbtH_-bfv8NfqbgdjtHucWPgjzNLKrTVfy5ZZB45yMjBPOH7bUqVhpU1wmXBiZYJZLt8xaK0ENqGrZt_MMAmX3FcXLxdDQZYT2NGUQpoLNuwFGBiaEsW8vh3CYVM0IA_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر و یسرائیل کاتز، وزیر دفاع اسرائیل در بیانیه‌ای اعلام کردند ارتش این کشور، عزالدین حداد، فرمانده شاخه نظامی حماس، را در یک حمله هوایی هدف قرار داده است.
عزالدین حداد، از فرماندهان ارشد گردان‌های عزالدین قسام، شاخه نظامی حماس است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/75488" target="_blank">📅 22:26 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75487">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LInOzy4xNBPRXqP9WevZqag1-6J_DHGjy-rgJBk9Eo6zlloHf75vEoJ5fDAga1HhpeW4_tam0KM0M-OxMwv0YIgujBkbV0QzfZzW9K7ZtI1MUDGCz0vXW3uzh6yj_5RvTuOkAcnoCNrvNnFjUXuvXaIitGeGNwpLlsxEOKHS6V2EGBEWPkn2O766uMo50C6_X-bO16ZMqvwxC_G8V2Iv9yolcn6uSSsdOm7qkXwgRO3ePRWQ0fevaPJaFFtvkC62mfkQRQwpKfJisnpKwG7mnmFHbZKMNGREH08lnnXWHakQv35lH6KMXHoWlY_MPrSXJFsVROU_Vc1aKW_zea7kHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا سپهوند، عضو کمیسیون انرژی مجلس شورای اسلامی از کمبود روزانه دست‌کم «۲۰ میلیون لیتر بنزین» در ایران خبر داد.
به نوشته خبرگزاری تسنیم، این نماینده گفته که تولید روزانه بنزین در ایران بین « ۱۱۰ تا ۱۱۵ میلیون لیتر» و مصرف روزانه بین «۱۳۰ تا ۱۳۵ میلیون لیتر» است.
سپهوند با بیان اینکه «در کوتاه‌مدت امکان افزایش تولید وجود ندارد»، خواستار جدی‌گرفتن «مدیریت مصرف سوخت» شد.
پیش از این وزیر خزانه‌داری ایالات متحده گفته بود ایران به‌زودی با «کمبود بنزین» مواجه خواهد شد.
اسکات بسنت با انتشار مطلبی کوتاه در شبکۀ ایکس، نوشته بود: «در حالی‌که باقی‌ماندۀ سران سپاه پاسداران، مثل موش‌هایی که در لوله‌های فاضلاب غرق می‌شوند، گیر افتاده‌اند، به لطف محاصرۀ دریایی ایالات متحده، صنایع نفتی آسیب‌دیدۀ ایران، در حال از کار افتادن و توقف تولید است. پمپاژ نفت به زودی متوقف خواهد شد».
او سپس پیامش را به سبک دونالد ترامپ، با جمله‌ای که به‌طور کامل با حروف بزرگ نوشته شده، به پایان برده بود؛ جمله‌ای با این مضمون هشدار آمیز: «مرحلۀ بعد،‌ کمبود بنزین در ایران!»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/75487" target="_blank">📅 21:52 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75486">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=gMVsQ8Mv48srrQnJB5Q8Xeto_WIBiGgSegNHQOXdBhu3fo1IRWAyfCxwAZkOOBYMUzO75GLlrlIdh42PwLiTSW1y-awnkb7YgXfTf34LooGiQ82ylIEpdsvle3EPYxYKraSkDZ_EuFgDYdVhn_R_bENJVpJpATfXiUGfQYUaUMQfHH1qsQ2mgS69oFkJDvzYV3wydecmACWSceGWDdoqP1-uExzlyZ-r6aMqG75a88kDoS5rCB62G3EPdIn0QX1ymMMYsALfjlU76B6kUP3cTD3WcA1PMe2uoidhSlfn2HPlX7300Y-6CPIstMR-cwmi6BRufv85fLv2e91UoiLWHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/575f6be6da.mp4?token=gMVsQ8Mv48srrQnJB5Q8Xeto_WIBiGgSegNHQOXdBhu3fo1IRWAyfCxwAZkOOBYMUzO75GLlrlIdh42PwLiTSW1y-awnkb7YgXfTf34LooGiQ82ylIEpdsvle3EPYxYKraSkDZ_EuFgDYdVhn_R_bENJVpJpATfXiUGfQYUaUMQfHH1qsQ2mgS69oFkJDvzYV3wydecmACWSceGWDdoqP1-uExzlyZ-r6aMqG75a88kDoS5rCB62G3EPdIn0QX1ymMMYsALfjlU76B6kUP3cTD3WcA1PMe2uoidhSlfn2HPlX7300Y-6CPIstMR-cwmi6BRufv85fLv2e91UoiLWHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاوه مدنی: وضعیت دردآور جزیره مارو (شیدور) ملقب به «مالدیو ایران»
نشت نفت به
#خلیج_فارس
پس از حمله به تأسیسات نفتی جزیره لاوان در فروردین ماه عامل این فاجعه بود.
#جزیره_مارو
[با کیفیت بیشتر:
۶۰ مگابایت
]
KavehMadani
برشی از سی‌ثانیه سوم ویدیوی بالا درباره وضعیت ساحل بیشتر مورد توجه قرار گرفته:
AzamBahrami
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/75486" target="_blank">📅 20:06 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3P_QjRbPgq8PTzbF9eCbhf11lf-LMFsdzS18R_exrtFSl2uEO2OsUsRiiIf-13Z3XOEUHcv0EhE_HOZVfB8sK9tLrK60B5VCCy0o7fr8zGTrYiqXwyKBMR7KafbsJDJ1p80Ik0F25fUk6vK_Wj2NbKmm0c_ohLCq_kkHm5JxglNpoXpo8WiwrKyA8wa6FrJMJP3vAufOljj995ftkKWI3V7iE_r4_6wcrzqpWFGrFh4paUF5IEzwk2qwuj6dd4l8aWFGb97COxSSIwnz4FpaKwmLa6y48GFj9DnML9xCZ7Q2M77H2snikB9mP2YAZVpWt03NqfRCDBOcnawU1rXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه پاکستان اعلام کرد که یازده شهروند پاکستانی و ۲۰ شهروند ایرانی که در کشتی‌های توقیف‌شده توسط آمریکا در آب‌های آزاد گرفتار شده بودند، به اسلام‌آباد منتقل می‌شوند.
اسحاق دار افزوده که «تمامی این افراد از سنگاپور به بانکوک رسیده‌اند و اکنون سوار پروازی شده‌اند که قرار است اواخر امشب به اسلام‌آباد برسد. سپس بازگشت برادران ایرانی به وطن خود تسهیل خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75485" target="_blank">📅 19:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz3fLeA_MicA64zzy0FzcLOd5UN3DLpjWIPsk18cAY8Bw7cjqkusqwopQI1Y5vLXs6HPhK8Ayp8duQoQcR9wjMOzeJYNrFyAzd4uV2UMuR8qFGo6LHu0doF2Klxq0IQTh7a7BBVawy-XtkjWYDWBB-pqhCvSKLlz_3so0sWTKMHraoCsGv7H0TcMcjqndnicbvsdbyZi1CCY8qAFByEaihOkft7Vsm_HhA9Lqb3bLtEALxmpt259m2wJXO6o2u1UYkIURq4GudzExqbXJ2NBcZcLW5K-qFIGkTRwmoxlHZ3Io3jE69YKJ1TKMYd1_XFcT9R224xeEVQ2-m5dNQzKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدراعظم آلمان می‌گوید در جریان گفت‌و‌گوی تلفنی با دونالد ترامپ، رئیس‌جمهور آمریکا، هر دو بر سر ضرورت باز کردن تنگهٔ هرمز توسط ایران و ممانعت از دسترسی تهران به سلاح هسته‌ای، توافق داشته‌اند.
فریدریش مرتس روز جمعه ۲۵ اردیبهشت در شبکهٔ ایکس نوشت که در مسیر بازگشت رئیس‌جمهور آمریکا از چین، «تماس تلفنی خوبی» با او داشته است.
او افزود که آن‌ها توافق دارند که «ایران باید همین حالا پای میز مذاکره بیاید. باید تنگهٔ هرمز را باز کند. نباید اجازه داده شود تهران به سلاح هسته‌ای دست پیدا کند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/75484" target="_blank">📅 18:11 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75479">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nimp0WR9S4nmJRbKzbmYQ1tOmTAGevRBH2xEC41MCcttQkq6zfsT8d5LwA-nwQ_krisxZYDG84ZGseVDPPYWb7kQqVtLv8TOLZ2_ooiuhD4bYC4Dg2U7GJyfTazbFcwGShK0EFJwXcqwkWGnic46w0LnWmMwqxHMF3ThBZtXndHpKjw3LHaDZQ4_YLE790GLNxmlwqn5afmSvZAUNd-8HH41-zB30mMPpmskUUbCp0ShaKhPWSrM8Ll6rqCVs712RyOMxwVKQpKCRu2EQBArc00gRz9qUrOC0R0p0Rbbye4ZnQbStJs7WmYqx43LhCeV5q3fVJvD3Ef7oK6dWWuVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CQA0V7b56oROghjBOS6vz7JGKegEXXGFbnlrPao_lP69WowZxRxQn9CwzrNI_0zdWg7lbExbm9gLhylzvENvBQfuAzy_ciNMJhXw7wcSJeWMiYr9ww3nRWsLp5toTs8bBgj-TXYVYvKwxHZ54at6WuwsCc5tM5j_EqKR5b_ijL4kjKQr8oCtOLa2Vvf5yG4MFfEUSQjqbgBcS3Ex79qV7Qz7sZGEupmRUNmpgb6FcFG13-RWVmdNvQ13EvC2U6wLBS6-P_ETfr5ei9NPQJPdlwitEBoQcsU94IbM9ipHqN8eCD4VvazlviTbWXg24NlLd1umcGpPpvwffaTOjQh4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AWiRrACW7o5tDUJVqlYRDL3JkeZ3mK2fh0c8iPCMMayMQYaBCTua_98DhIknGj91yMFYtenwigfn4RPibiJbmB-yGajpwq-nEx_rZkFtPmJFf9yi2L0ORXVy0gMrUMhGp422ISm2YuWzl5M78ekPX1aoTKV7JpAX_c-p2bAUtWXE7n9wVZfVAuQ9Z0XZYnG6nmOrsfPrTH1oWJ3k8umcLd-T2bdzF26oimgKUpzrUq_HN4VidcBugpJ9js_M396Kxv8SNteOn3BKLMdnktEg60gFbt5CPOzj55fOqmCiKVtYiukWG_P2aG3h6tueODZw-7wXQRmM7sjBkm6WgtDFYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1948a10693.mp4?token=damLXFBy6aR15zy4VHhIe5sS3JDnInTXbIJQtG5qzUEemYFF_zqqQGDP9OjdoRh4ehU6PLDwkCnGHVlv6hWUB594hdYlKpg95y3PosE_DewOTEwpNvBd16S-Z0B6LQNO4Fvmqpx1bGwh42MQ87rdGckkc1qhshBUAjeISG3NoNxR1BD6eFqIBOFs_lIaFWYjJlRMwbXG-tzXeVsHRHpKHOqM6nOXZO66n2esCpU_4qJ8AOHtxrGnqFiBa_1w_t-e9zkL_hBG3-UCiCTRfMza6RZYFGhLGq6R86zj5wrE-3Rjk_hWVZ7owytiCMIdzQTgQj1ElESPfd_kpdxkIsB-CA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1948a10693.mp4?token=damLXFBy6aR15zy4VHhIe5sS3JDnInTXbIJQtG5qzUEemYFF_zqqQGDP9OjdoRh4ehU6PLDwkCnGHVlv6hWUB594hdYlKpg95y3PosE_DewOTEwpNvBd16S-Z0B6LQNO4Fvmqpx1bGwh42MQ87rdGckkc1qhshBUAjeISG3NoNxR1BD6eFqIBOFs_lIaFWYjJlRMwbXG-tzXeVsHRHpKHOqM6nOXZO66n2esCpU_4qJ8AOHtxrGnqFiBa_1w_t-e9zkL_hBG3-UCiCTRfMza6RZYFGhLGq6R86zj5wrE-3Rjk_hWVZ7owytiCMIdzQTgQj1ElESPfd_kpdxkIsB-CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز جمعه ۲۵ اردیبهشت در مسیر بازگشت از چین در پاسخ به خبرنگاران، درباره آخرین پیشنهاد ایران در مذاکرات هسته‌ای گفت که آن را «از همان جمله اول» رد کرده است.
او با بیان اینکه محتوای ابتدایی این پیشنهاد «غیرقابل قبول» بوده، افزود: «حتی ادامه آن را هم نخواندم.» ترامپ تأکید کرد که صرف تعیین بازه زمانی مانند ۲۰ سال کافی نیست و آنچه اهمیت دارد، ارائه تضمین‌های واقعی و قابل اجرا از سوی ایران است.
رئیس‌جمهوری آمریکا همچنین تصریح کرد که، هرگونه توافق باید شامل انتقال کامل مواد و سوخت هسته‌ای از ایران باشد و افزود که توافقی مبتنی بر «حرف‌های توخالی» قابل پذیرش نخواهد بود.
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره پیشنهاد اخیر جمهوری اسلامی گفت این پیشنهاد را بررسی کرده، اما به گفته او، اگر از جمله نخست یک متن خوشش نیاید، بقیه آن را کنار می‌گذارد.
ترامپ در پاسخ به این پرسش که جمله نخست چه بوده است، آن را «غیرقابل قبول» توصیف کرد و گفت مسئله اصلی از نگاه او این است که ایران نباید «هیچ شکل» از برنامه هسته‌ای داشته باشد.
در ادامه، خبرنگار از ترامپ پرسید آیا دوره ۲۰ ساله برای او کافی نیست. ترامپ پاسخ داد که «۲۰ سال کافی است»، اما به گفته او، سطح تضمین‌هایی که جمهوری اسلامی ارائه می‌دهد اهمیت دارد.
ترامپ گفت که اگر قرار است توافقی ۲۰ ساله مطرح باشد، باید «۲۰ سال واقعی» باشد و نباید به گفته او، توافقی مبهم یا ظاهری باشد.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا روز جمعه ۲۵ اردیبهشت و در زمان بازگشت از چین به آمریکا در هواپیمای ایرفورس وان به خبرنگاران گفت با وجود آنکه نیروهای مسلح ایران در جنگ نابود شده‌اند، ممکن است نیاز به «یک پاکسازی کوچک» وجود داشته باشد.
ترامپ ساعاتی پیش در گفتگویی با فاکس‌نیوز هم گفته بود که نیروهای مسلح جمهوری اسلامی در چهار هفته گذشته، تلاش کرده‌اند تا تعدادی از پرتابگرهای موشکی را از زیر خاک بیرون بکشند و جای بعضی تجهیزات را عوض کنند، با این حال «آمریکا قادر است در دو روز همه این‌ها را نابود کند.»
@
VahidOOnLine
دونالد ترامپ در پاسخ به پرسشی درباره اینکه آیا شی جین‌پینگ، رئیس‌جمهوری چین، تعهدی قاطع برای فشار بر جمهوری اسلامی به منظور بازگشایی تنگه هرمز داده است، گفت از کسی «درخواست لطف» نمی‌کند.
ترامپ گفت: «من درخواست هیچ لطفی نمی‌کنم، چون وقتی درخواست لطف می‌کنید، باید در مقابل لطفی انجام دهید.» او افزود که آمریکا به چنین کمکی نیاز ندارد.
رئیس‌جمهوری آمریکا در ادامه گفت نیروهای مسلح طرف مقابل «اساسا از بین رفته‌اند» و ممکن است به گفته او «کمی کار پاکسازی» لازم باشد. او همچنین به آتش‌بس اشاره کرد و گفت این آتش‌بس به درخواست کشورهای دیگر انجام شد.
ترامپ گفت شخصا چندان موافق آتش‌بس نبوده، اما آن را به عنوان لطفی به پاکستان پذیرفته است. او از مقام‌های پاکستانی، از جمله نخست‌وزیر و فیلدمارشال این کشور، با تعبیر «افرادی فوق‌العاده» یاد کرد.
@
VahidOOnLine
دونالد ترامپ گفت آمریکا ممکن است در مقطعی برای حذف آنچه «گرد و غبار هسته‌ای» نامید وارد ایران شود. ترامپ در مسیر بازگشت به آمریکا و در هواپیمای ریاست‌جمهوری، ایر فورس وان، به خبرنگاران گفت: «در زمان مناسب، یا وارد می‌شویم یا آن را به دست می‌آوریم. فکر می‌کنم احتمالا آن را به دست می‌آوریم، اما اگر به دست نیاوریم، وارد خواهیم شد.»
او افزود: «فکر می‌کنم آنها کاملا شکست خواهند خورد و ما هیچ خطری نخواهیم داشت. ما تجهیزات لازم برای خارج کردن آن را داریم، هیچ‌کس دیگر ندارد؛ شاید چین چنین تجهیزاتی داشته باشد.»
ترامپ پیش‌تر نیز در ماه مارس در کاخ سفید درباره ذخایر اورانیوم غنی‌شده جمهوری اسلامی هشدار مشابهی داده و گفته بود: «یا آن را از آنها پس می‌گیریم یا آن را برمی‌داریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75479" target="_blank">📅 17:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgPdOIDriYp7Nwh7DQgkVaHUI5Jbnt5z2KcJf_U_UeRvRTwmO2ScTOyGkYCSlcjfKNYr5Ck12TLwKrJvSPXFizUxfIbtkVpsWOD3BokXoojQsOF3f4aOH_x-YnuZtBEZRvjeeLkIQ3HYn8hc6osmKVkmj_ozBQq95KJGeeqwYUbQSV5gUabcfT3sJM9qGQ_cKmPwdStCK0_YZpQ-OKBDevZehCfbOmiW-WjggP0OT9CXxVyWK6Dd37b_1oOxQJnWT7Ee43vbNJ7Y5v4m0jh2TUNkkmNGxjjEmLbeNjPv9FIntxu5YE50Kx5W5EpxRDhe13gVj17_fzHnT3RfStoGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشست وزیران خارجهٔ کشورهای عضو بریکس در دهلی‌نو، پایتخت هند، به‌دلیل اختلاف‌نظر میان اعضا به‌خصوص بین ایران و امارات متحدهٔ عربی بر سر جنگ ایران، بدون صدور بیانیهٔ مشترک پایان یافت.
به‌گزارش رویترز، هند روز جمعه ۲۵ اردیبهشت اعلام کرد به‌جای بیانیهٔ مشترک، «بیانیهٔ رئیس» منتشر شده است، زیرا برخی اعضا دربارهٔ تحولات خاورمیانه دیدگاه‌های متفاوتی داشتند.
گروه بریکس شامل برزیل، روسیه، هند، چین، آفریقای جنوبی، اتیوپی، مصر، ایران، امارات متحدهٔ عربی و اندونزی است.
روز پنجشنبه رسانه‌های ایران از تنش لفظی در این نشست خبر دادند و نوشتند عباس عراقچی، وزیر خارجه ایران، امارات را به مشارکت مستقیم در جنگ آمریکا و اسرائیل علیه ایران متهم کرد و گفت میزبانی پایگاه‌های نظامی آمریکا از سوی ابوظبی و همکاری امنیتی این کشور با اسرائیل، آن را به بخشی از جنگ تبدیل کرده است.
روزنامهٔ لبنانی الاخبار نوشت که در مقابل، هیئت اماراتی خواهان آن بود که هر بیانیهٔ نهایی، حملات موشکی جمهوری اسلامی ایران به این کشور و توقیف کشتی‌ها را محکوم کند، در حالی که تهران بر درج محکومیت صریح حملات آمریکا و اسرائیل اصرار داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 222K · <a href="https://t.me/VahidOnline/75478" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gE7u0hizxUFoihEZPHdRewbtSSQWPfkFKs6oKIluOHtKqHGFsUcAnTC13Upc8a83YFQ2yDkIn9nkDYabj0C1HMGwvUq1u-8XnyZ49lbu1xSLAQs7rGH0bdlwSpgMQDrcUvxwcMYdIlMCjt3AyCKpSDa_lBndgdwrApsw_UjyblEQMZWYRUSeiVhdDzu61WS-Vl3jzZ7YuXTbw7pMbIPnhLkqIBx1MvoBJRBsWMIoLmh1nIF-4Dc68t4rFWWiTVteI87tHISmQka5FmSnbEvzoF0HxzhkbqGmIn2rPtm0Sa0qDRBDe8lGGpevSN7WhZ0ddZ03othKh8mU1D72XgBp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی اعلام کرد این کشور ساخت یک خط لوله جدید نفتی را برای دو برابر کردن ظرفیت صادرات نفت از طریق بندر فجیره تا سال ۲۰۲۷ تسریع خواهد کرد. این اقدام توانایی ابوظبی برای دور زدن تنگه هرمز را به‌طور چشمگیری افزایش خواهد داد.
دفتر رسانه‌ای دولت ابوظبی روز جمعه ۲۵ اردیبهشت اعلام کرد شیخ خالد بن محمد بن زاید، ولیعهد ابوظبی، به شرکت ملی نفت ابوظبی، ادنوک، دستور داده است اجرای پروژه خط لوله «غرب به شرق» را سرعت ببخشد. به‌گفتهٔ این نهاد، این خط لوله اکنون در حال ساخت است و انتظار می‌رود در سال ۲۰۲۷ به بهره‌برداری برسد.
در بیانیهٔ دولت امارات اشاره‌ای به زمان‌بندی اولیه این پروژه نشده است.
خط لولهٔ کنونی نفت خام ابوظبی، موسوم به «حبشان ـ فجیره»، ظرفیت انتقال روزانه تا یک میلیون و ۸۰۰ هزار بشکه نفت را دارد و نقش مهمی در افزایش صادرات مستقیم نفت امارات از سواحل دریای عمان ایفا کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/75477" target="_blank">📅 17:35 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75471">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mH2_Tsaj6AdA_I4k80uk7b_C7MHgv9vHra05RegBJVqPLwNEbmvSWCU6ruJfyhlHn76hp_82qPE5qyYz0IqVPi0ltG_qN9FJ9uGx1ZK5cRBokZgeqmHIQLDOLYQnA1NsLQZV2aPH1JZTfIGnYxpOvYU9V7-_WvNpRQsthKKRmoGaMBcVjEsneIGkI0pTUP33fEE57MKZhDsSdLyG2Pqr_XLXK77T-yYMCtlXBYXIS75dzClzh_sN7wwZ-nkIJnJlJeJeK5uT64GXnnKdZaH4IQEJQe1f9-BMaTLQk2tuKE2qeDnBF9oZ55uZRItVau7X14IBgx66fsD3e--VT-4Uag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EaodL9xHb90BmCAA8Ghq1zAZ8XffUDc3kMC-6yoaAR_AyM5WIJ2lcTeyasD8rA0tItejORvjtS00qNaedefaZUHrRah3wsDenIgrbVJWHj1L1OMPuH3pyYBYhDxRU1NVUym0fibWXeDFyjhvUvRduWAQpG7dxd1okvyhQOH7e2qKc8gOAvofw0lba1EhG0QidMtWq7UlUcuXPFsAXz6kmNZm4W_pkDU0ejl52cTEujfIzKsXeQH_IJA_ihOWTX2AZaKKvmav0ya6YmDtHX089-gdAgwIZ1jaQO5mOfufk6kYgI4NseDZXRpm_ZQi_hqZRmFr8jVaiVnIaQ_n6k4Mxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GEaBTpwYqXbEZwkTxBnEmH-aE79apti2yd4CVoMfnrQDoi4Elcq-7TAZkx8FwxMxloCXVWGCwtBRs-syzMT59yYn_4wa8eP-z1Lp0_44hb1-Gn-EuVuaXEuca2ca8stE3oKfzYDwEOjwmFBvyoFB4ISG905Bzv7wCpScbI3s_3ma4Vvg0f9qmD3mwR2mSS6RyvyDu2rOxHdQuyeSnmW7Q05BYjQ51u_rOO22hnsuZYrazWq84MT2Y1a2cwnz6nDe904a4_13x9MLwU0XrOnKDcHZCy0KqpWdz8WAiWWyK6OMOYHFXTovEqXQmoFZc211g3U_AsvbAVmb1G1kciAFvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BR3eI0-hESez7OrgXYM4lMk_mOzsiSoPqg9Q5KHZ7lKZKFDTaInfKYfyNMn-EAm0Jb437FPQbfOI53hU8KdmoBeOBpx5iJbzjzD7rrkDiN37v7rkiSx6Pa6kScNRbSd3gh9ooVtloRZ99POLt47st_mbDlkpKrVO8UtPvOowAVoUptwgpelUO8rgbpZ4rsLjQZfr21gYxEa_CaIW7qBIo4TBPIPY7h1O_gwwWEpX589OQ6vaY_I5kspdmYC2ARWcuvUzc5VQzcKNO4rpbSFmfXovfWxRfNpG7LUvR5hb-YKrpoVyiLHKyqmgUp7DkvGj6HPbwb5-gh1nYjySeJp7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eGGzhQOlEk32yQgLfMaS1KDesWpaB6Db1PXHdppVYg66kTspg2DIiKOzArX5bj2srgvfK4K4c_yB1FVObNTyplVXWbOYeovSWO-H6A7gLHJn4lC_eO9_GrEa4ccdYnJIAGCck2U24AU3ArKRt8N3WTLiaUcbWdoTPyByZyP0cTvKIMiFxl7NpwZBB5s7pusGhyb-aGu3-BzSqwA_1bn9z4lm7UGv2Udj5QqMJeOVrFhy0B4IkQvrfDp8LoBxzP59Sygv6gxM_-xTUSfmvNynwubslDYb560XGDwAlFgmNIAHpyNDYjfcHq-DJ8Hh2COj8CGyghvvIT4yKH-HRJecFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DDdFXrrFJQZ4cZfxSsx_5ZlT8VZrZvFj9Xwm1bqxDZ4vIF3FDgQFPGBVrbwE0Ba8Ci2pBfZvJPzdcRk4mG-IQxUXMpQ4EHAS7VmabngmCN8NRyj5JTYY1-uczqnGNIZU3oaD2RVs6hF_7gz-APT83QiaFGtWWHggcMOnQKc3ZlCkdq129yj9MzeynFbbKI2T5DqS65N8AN_r_7UcSn95H7JmJNKdEcYnL_WcPuTBWhEAVxW0DPJ3pUQ2tybFlzVB76ytgR_70pYrVsEKm4aOAsPptfBmE9bNWTt4Lu1EMGsdRDf7r_OzxjjY7jcHxRPkWsVGqenkfNQBY-2SGOt90A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در مصاحبه‌ای که با فاکس نیوز انجام داد گفت او درباره ایران با چین صحبت کرده است.
ترامپ افزود فکر نمی‌کند که چین هم خواهان این باشد که جمهوری اسلامی به سلاح هسته‌ای دست پیدا کند.
او گفت جمهوری اسلامی می‌تواند یا «توافق کند و یا «نابود» شود. رئیس جمهوری آمریکا گفت نمی‌خواهد چنین کاری کند اما آمریکا قوی‌ترین ارتش جهان را دارد.
ترامپ گفت ما در جمهوری اسلامی با «رده سوم» رهبرانش طرف هستیم. او گفت رده اول و دوم رهبری نابود شدند و فکر می‌کند رده سوم از رده اول و دوم «که دیگر با ما نیستند» «منطقی‌تر» و از لحاظی «باهوش‌تر» هستند.
او این تغییر را به‌نوعی با یک «تغییر رژیم» مقایسه کرد.
ترامپ با اشاره به اینکه جمهوری اسلامی «پنج روز» زمان صرف کرد تا به پیشنهاد آمریکا که «یک ساعت» هم زمان نمی‌برد پاسخ دهد، افزود جمهوری اسلامی در داخل خود «آشوب فراوان» دارد و «چیزی به جز آشوب» ندارند.
ترامپ در مورد حمایت چین از جمهوری اسلامی گفت که رئيس جمهوری چین، شی جین‌پینگ قویا گفت که به جمهوری اسلامی سلاح نخواهد داد.
...
او افزود «امیدوارم» جمهوری اسلامی این مصاحبه را ببیند چرا که آمریکا می‌تواند به سرعت همه تسلیحاتی که آن‌ها در طول آتش‌بس ممکن است به آن‌ها دست یافته باشند به سرعت نابود ‌کند. ترامپ گفت «ما دقیقا می‌دانیم چه کاری می‌کنند...و هر کاری که در چهار هفته گذشته انجام داده‌اند ما آن‌ها را در یک روز از بین می‌بریم.»
رئیس جمهوری آمریکا گفت جنگ را می‌توانست «چند هفته بیشتر» ادامه دهد و ماجرا تمام می‌شد اما به درخواست چند کشور آن را متوقف کرد. ترامپ گفت جمهوری اسلامی دو گزینه دارد: «یا توافق کند و یا نابود شود.»
ترامپ همچنین درباره خارج کردن اورانیوم غنی‌شده از ایران گفت این کار را بیشتر برای «روابط عمومی» انجام خواهد داد و او احساس بهتری خواهد داشت که آن مواد از ایران خارج شود.
رئیس جمهوری آمریکا افزود «به‌دست آوردنش پروژه بزرگی است، واقعاً پروژه بزرگی است.»
او گفت: «اوایل به انجام این کار فکر می‌کردیم، اما زمان می‌برد؛ حدود یک هفته و نیم طول می‌کشید، و این مدت زیادی است که در قلمرو دشمن باشید.»
دونالد ترامپ توضیح داد که «باید این حجم عظیم گرانیت را جابه‌جا کنید. می‌دانید، آنجا گرانیت است. گرانیت سخت‌ترین سنگ است. واقعاً شگفت‌انگیز است، چون بمب‌هایی که استفاده کردیم فوق‌العاده قدرتمند بودند. و یادتان نرود که علاوه بر آن، با موشک‌های تاماهاوک هم آنجا را زدیم.»
او گفت فکر نمی‌کند خارج کردن آن مواد از ایران «لازم باشد، مگر از نظر روابط عمومی. به نظرم برای رسانه‌های جعلی مهم است که ما آن را به‌دست بیاوریم. من همان کسی بودم که گفتم آن را به‌دست خواهیم آورد، و به‌دستش هم می‌آوریم. حواسمان به آن هست.»
ترامپ اشاره کرد که با «نیروی فضایی» آمریکا که ابتکار او بود همه تحرکات در اطراف سایت‌های هسته‌ای در ایران زیر نظر آمریکا است.
او گفت «من ترجیح می‌دهم آن را به‌دست بیاوریم، اما مراقبش هستیم. دقیقاً می‌دانیم آنجا چه اتفاقی می‌افتد. چند روز پیش مردی تلاش کرد وارد آن گذرگاه شود. دیدیم دری کاملاً متلاشی شده بود. و ما از همه‌چیز خبر داریم. اگر هرگز حرکتی انجام دهند، و این را هم به آن‌ها گفته‌ام، اگر نیرویی بفرستند و ببینم کسی تلاش می‌کند، تنها کاری که می‌کنیم این است که با چند بمب دیگر آنجا را می‌زنیم و کار تمام می‌شود. آن‌ها چنین کاری نخواهند کرد.»
ترامپ گفت: «به آن‌ها گفتم ما در آن محل، در آن سه سایت، ۲۴ ساعته ۹ دوربین داریم. دقیقاً می‌دانیم چه می‌گذرد. هیچ‌کس حتی به آن نزدیک هم نشده است. در ابتدا بررسی کردند و گفتند هیچ راهی وجود ندارد که کسی بتواند به آن غبار هسته‌ای برسد. اما با این حال، من ترجیح می‌دهم آن را داشته باشیم. ترجیح می‌دهم به‌دستش بیاوریم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75471" target="_blank">📅 07:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75470">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mV2uzxTmUFIH9iBi1hiHwBugGiA8RenC4U2W4ZSjeLK8I2MyQtefFiUlIrTTQTqU4E0cVsJa8hjny11wMloTNDOE4iA5-QrN0dSpwM6mTX1_cFPGVN-0SsH34-BNovc709R1HCCUDRX3wafoq4SHWAbweQQsNzT3OmaJEARcEX8lvBIvV7Nxj7jyRdXZgUv_GsnHNofcnDccziwR9bO4MzspvS6hc1SvjKbHj7-yAh_HhbroycgI6UZ6zQZVVL6SqyAkmvf8_1-UbDm_CDnNsf1N3Lwhqj4hHX7cr3mkn6UHvJFT3bDeYMUjEn-6rrMcpdZwZSx7v6GtqkKDM2VgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: منظور رئیس‌جمهور چین از آمریکای در حال افول، دوران بایدن بود
ترجمه ماشین:  وقتی رئیس‌جمهور شی با ظرافت بسیار از ایالات متحده به‌عنوان کشوری که شاید در حال افول باشد یاد کرد، منظور او خسارت عظیمی بود که ما در چهار سال دوران جو بایدن خواب‌آلود و دولت بایدن متحمل شدیم؛ و از این نظر، او ۱۰۰ درصد درست می‌گفت. کشور ما با مرزهای باز، مالیات‌های بالا، تراجنسیتی‌سازی برای همه، حضور مردان در ورزش زنان، DEI، توافق‌های تجاری وحشتناک، جرم و جنایت گسترده و بسیاری چیزهای دیگر، به‌شدت آسیب دید!
رئیس‌جمهور شی به خیزش شگفت‌انگیزی اشاره نمی‌کرد که ایالات متحده در ۱۶ ماه تماشایی دولت ترامپ به جهان نشان داده است؛ از جمله رکوردهای تاریخی در بازار سهام و حساب‌های بازنشستگی 401K، پیروزی نظامی و روابط شکوفا در ونزوئلا، نابودی نظامی ایران — که ادامه خواهد داشت! — قدرتمندترین ارتش روی زمین با فاصله‌ای بسیار زیاد، تبدیل دوباره آمریکا به یک ابرقدرت اقتصادی، با سرمایه‌گذاری بی‌سابقه ۱۸ تریلیون دلاری دیگران در ایالات متحده، بهترین بازار کار تاریخ آمریکا، با شمار افرادی که اکنون در ایالات متحده کار می‌کنند بیش از هر زمان دیگری، پایان دادن به DEI ویرانگر کشور، و آن‌قدر دستاوردهای دیگر که فهرست کردن فوری آن‌ها ناممکن است. در واقع، رئیس‌جمهور شی به‌خاطر موفقیت‌های عظیم بسیار در چنین مدت کوتاهی به من تبریک گفت.
دو سال پیش، ما در واقع ملتی در حال افول بودیم. در این مورد، من کاملاً با رئیس‌جمهور شی موافقم! اما اکنون، ایالات متحده داغ‌ترین کشور در هر جای جهان است، و امیدوارم رابطه ما با چین از همیشه قوی‌تر و بهتر شود!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/75470" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75469">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oR7GawGhjxz51H6SlFUFTcVEItjD1-btin5cPt1D5kZEt5BDDbcGQduYpijIxRZwqcNuVJSeLLMTfiuImMDbPql-dSZ-4m-mfYHmL-MFU_tUILpI-CmD4d4h7_6JTYAECcdrP6lSZJB5tPwdWBtT8yUgrSeT83BDgbGrO7OvBLwIsILCUXzUIrkRcBwPD8QAhRon9-b0Sy1AWbYXSIN_xmcaEdsPomWdNNhdGh9Q1O8dSCXMYk3EqTIgrQs-QPRJvEv_vN9ItIfbroLj3t4DnnMZS7VVwr9lXmLk5P8_4aM5VdbHyZDx-WziYbitfqLmgocd8Dwm-WjewfeOmLM9Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با سفر «دونالد ترامپ» رییس‌جمهور آمریکا به چین، رهبران ۲۶کشور دیگر نیز روز پنجشنبه ۲۴اردیبهشت۱۴۰۵ در بیانیه‌ای مشترک خواهان بازگشت وضعیت عادی دریانوردی در تنگه هرمز شدند.
این بیانیه که توسط کشورهایی مانند بریتانیا، فرانسه، بحرین، کانادا، آلمان، ژاپن، قطر و کره جنوبی امضا شده است بر «تعهد خود به استفاده از ظرفیت‌های جمعی دیپلماتیک، اقتصادی و نظامی برای حمایت از آزادی ناوبری در تنگه هرمز» تأکید کردند.
در این بیانیه آمده است: «کشتیرانی باید آزاد باشد، مطابق با مفاد کنوانسیون سازمان ملل متحد درباره حقوق دریاهاو حقوق بین‌الملل.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75469" target="_blank">📅 01:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75468">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJSii5GqVbRyEuWPl5XihdZ_Rg6kzFvs2ZICxSEG1aXA5naeZTLK1nVsy-LAtNjVULiy6iO_XpzZOhQIw-eMznprM8XErV-7y0iSpBsK7Gldk9BmjIBpkPhckVYEdoVvsscKQUDjBhFT6eqJLM7IMRR2V2A9J-l1Xhw0bd2TCIiL_9yANJf2osh4wwMxoEwo6daw0md44uvshvaoNkJRG8umCPZwTZjA-ahJfwIBp1m1luqSI6qwEKVAcaf2MB0sx9o21kTWTiwXjsy3SUrCh9dIxVFVRlzm9iLVFlVPC87KqizpbJ8CqK9RJ1Os6FkNSOhHNOlbdaIBrxj9eijoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، اعلام کرد که صنایع موشکی، پهپادی و دریایی ایران «۹۰ درصد تضعیف شده‌اند.»
او در یک جلسه استماع در سنای آمریکا گفت: «تهدید ایران به‌طور قابل‌توجهی تضعیف شده و این کشور دیگر مانند گذشته، در هیچ حوزه‌ای، قادر به تهدید شرکای منطقه‌ای یا ایالات متحده نیست. آنها به‌شدت تضعیف شده‌اند.»
کوپر اشاره کرد که نیروهای نیابتی مسلح ایران در ۳۰ ماه پیش از جنگ اخیر، بیش از ۳۵۰ حمله علیه نیروها و دیپلمات‌های آمریکایی انجام داده بودند؛ به‌طور میانگین هر سه روز یک حمله، که در نتیجه آن چهار سرباز آمریکایی کشته شدند.
برد کوپر با دفاع از جنگ اخیر  تأکید کرد: «امروز حماس، حزب‌الله و حوثی‌ها همگی از تأمین تسلیحات و حمایت ایران قطع شده‌اند. این نتیجه از پیش تضمین‌شده نبود.»
او همچنین گفت نیروهای آمریکایی دیگر برای سرنگون کردن پهپادهای ایرانی از مهمات پیشرفته و گران‌قیمت استفاده نمی‌کنند.
ذخایر سامانه‌های دفاعی پرهزینه برای مقابله با پهپادهای ایرانی در طول جنگ خبرساز شده بود، اما فرمانده سنتکام اعلام کرد ارتش آمریکا اکنون از مهمات ارزان‌تر استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75468" target="_blank">📅 19:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75467">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsOi6s1DaH0qENpYrAgrwkj0niSKY2-bR1Ef6zJwVkUuVQNRShL-XX_dro-Bkrfsna5de9NXyq-s_jt-F1fsi9ic8yntRHRhAyHLpNkTiZaxAMD6ZYYkFdtY2v6DNi0nerbarLi7tXO3v-kvFz4t9Wr2gUpSE6hk1MHl1nhXRt1kMHE_gnhtbD5fQg1y0lx0XaYYM4bdOvykF98cAdDDaSutGoChsPHncyu0mlS1I6N3q_PI-17LD9uXs4864LePsON7UmRcp6n3k_3NPC2OuxB0IJQFpKZp443b9Tnoz46bf_TaaWuFIGwcbJcJZomJUyPzVT1YhjC7-XTaJqAVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمید رسایی، نماینده تهران در مجلس، نوشت جریانی «شناخته‌شده» در دولت چهاردهم که راه‌حل را «آزاد کردن و گران کردن» می‌داند، قصد دارد سهمیه بنزین هزار و ۵۰۰ تومانی و سه هزار تومانی را کاهش دهد و قیمت بنزین پنج هزار تومانی را به ۱۵ تا ۲۰ هزار تومان افزایش دهد.
او افزود همان جریان در دولت چهاردهم پیش‌تر با حذف ارز ترجیحی ۲۸ هزار و ۵۰۰ تومانی و گران کردن ارز، به گفته او، «بالاترین تورم پس از انقلاب ۵۷» را به مردم تحمیل کرده بود.
رسایی نوشت محمدباقر قالیباف با «پلمپ کردن بدون توجیه و دلیل مجلس»، راه نظارت نمایندگان بر تصمیمات دولت را بسته است. او افزود انجام تکلیف نمایندگی سخت شده، اما تلاش می‌کند مجلس را از این «مرگ تعمدی» بیرون بیاورد و جلوی این تصمیمات «عجیب» را در موقعیت «سخت و جنگی» فعلی بگیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/75467" target="_blank">📅 19:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75466">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw9_nkadIOYDO6Iqy6gPnKxQ22PQAs52z_eGQ5z_a9wzLf6ZzhPe5JDAb8BKEQRSWqbCYyDDOBWGnXteqvWyrNGXurrFwlwiG3yebMzrF9sejqNKgTw1RIedJToWM6XKHimUKMSDSIU1RCKwSJfk64D6uiVxDqWrW5QUqwViL-TGRiBhzxFeDJhZjitXtlm8ZdJd1xTmJaE9-e24yIo-ZYk2aWXoTV33mCU4AGOR_Fj3VQQ-iIYnGd-up0gFDLDavvIEtJotRVeNRmMVJc8-z9o-AAoONATX24LC_-NHKNTUP_JqDup-xqDEuE-p6JuccChQdYwGc2Xr5e_sm1hPAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی پوردهقان، دبیر دوم کمیسیون صنایع و معادن مجلس گفته است که مصوبه شورای عالی امنیت ملی در مورد اینترنت پرو در اجرا به «قلکی برای همراه اول، ایرانسل و رایتل» تبدیل شده است.
او در مورد انتخاب محمدرضا عارف، به عنوان رئیس ستاد ویژه ساماندهی فضای مجازی گفت که «مجلس در این مورد چیزی نمی‌داند» و این حکم مسعود پزشکیان، رئیس‌جمهور را «تزئینی» خوانده است.
به گفته این نماینده مجلس این قبیل اقدامات بیشتر جنبه «روانی » دارد و قرار نیست که «اتفاق خاصی» در این مورد بیفتد.
آقای پوردهقان همچنین گفته است که بدتر از قطعی اینترنت، تعطیلی مجلس است و اکنون مجلس با بسیاری از وزرای دولت به لحاظ نظارتی هیچ ارتباط خاصی درمورد عملکردشان ندارد که یکی از همین موارد موضوع اینترنت است و هنوز یک جلسه ویژه نداریم که فردی بیاید و شرایط را توضیح دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/75466" target="_blank">📅 19:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75465">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuvN8xtguQ_jKDgYSM_XoB8kOki1cfJ0RsHhH4UnLDWLF3fz2FAg7uie7EgV-ZUKgI0boJ5GRIloeCGNBXri5VfwlIqV_DnPLIkgv4bZYSwLjnbQxdix_McIGi75kBd6t05ua-XJtLivmaWHrP8kYHMNc_rjGJYdfa95lGta17skERssPsbigKel42K3c6zYqb3yMxT7gBZSVhVwvEFb0wITQp6G9kqfXXDQwZzRNBRWs_47S-k9CPOIdfodGSSUao_Tkd4TAihNmkbFazX_xHqKfi0j9vLhguF2gjfNYPNL9LT-rfUOHsV9InPb5zwrFTdI7npOSigO4PqX3Eua9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل در یک سخنرانی گفت که ماموریت ارتش این کشور درباره ایران کامل نشده و برای این احتمال آماده است که شاید دوباره ناچار به اقدام شود.
یسرائیل کاتز تاکید کرد: «اگر اهداف‌مان تامین نشود، دوباره اقدام خواهیم کرد.»
پیش از این نیز ایال زمیر، رییس ستاد کل ارتش اسرائیل، گفته بود که «نبرد به پایان نرسیده و ارتش برای ازسرگیری جنگ در صورت نیاز آماده است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75465" target="_blank">📅 18:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75464">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmEil6j8CbMnX1x95Vi992UbpI6nCOeb5jlGlAuYmopydgO7tQ9ILEVP_s28Tpv7-nqOCi-NO64sVVcFcumttMOPW9Rvzqn5Qxk7VfnUWPyyFOXdqenYyng2riqCs0be9oPXmbKf7KYOLcsyzni7xAv3nDKXeFdnzT3qh6d1bcnSWeU7nDlT9umnnvgUu6Gkjn5UD4FaK3JMiB0XuTvLcK5dRjx4B6EAIkdtvuQIE2R6kxy9iIk9jZtnybO_EsW_EfJr0jg4kZmyajY6Ir62_vbDlAgQozNbs3lexqAlIRXov6LGpZGXQi_qqo6BcpnLZOM231z5BDgvsWYfW3ZuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر دارایی آمریکا، در گفت‌وگویی با شبکه سی‌ان‌بی‌سی در حاشیه سفر رئیس‌جمهور آمریکا، در یک مصاحبه از پیش ضبط‌شده گفت که معتقد است چین از نفوذش بر تهران برای بازگشایی تنگه هرمز استفاده خواهد کرد.
او گفت: «فکر می‌کنم آن‌ها (چینی‌ها) هر کاری از دستشان بربیاید انجام خواهند داد.»
آقای بسنت افزود: « بازگشایی تنگه هرمز بسیار به نفع چین است. فکر می‌کنم آن‌ها پشت پرده تلاش خواهند کرد، البته اگر اصلا کسی بتواند بر تصمیم‌های رهبری ایران تاثیر بگذارد.»
به اعتقاد وزیر دارایی آمریکا، چین به‌زودی سفارش بزرگی از هواپیماهای بوئینگ را اعلام خواهد کرد و افزود دو طرف در حال گفت‌وگو درباره بهبود روابط تجاری از جمله صادرات انرژی هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/75464" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75463">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBEoSvCs-IOQPLHS1LvfAShEe0IgzUN291BVft3QxlfMKcISskdpw7OJkfYLwa8yEqpcVvhRLjRxULnXsVecJzYNdMGWEeVKQnYW-syE2mb1xi456IgaQqB3H1-M9SGGKfkxC6WgdWBFZ8UVIoGfWDtHtzK5czsEenlctshpJGfDwT9vWNrdZO2PmfvhnZHbOsX1vgjC0ZrpUNZde1fIUmbiM_F2URz2Ie2z0U0ShNXYpbaSnx4WyVIWjPYXmkUqFS9D_CX2CoQkKwhArhYWNLxOWEuZoHO_jFIgvnr9zaFcOHpxEcpDeY9NdNXO5P38prWwse9pu9rzBk5NbHIPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران می‌گویند وزیر خارجه جمهوری اسلامی در نشست بریکس در دهلی‌نو، امارات متحده عربی را به «دخالت مستقیم» در عملیات نظامی علیه کشورش متهم کرد.
این تنش یک روز پس از آن رخ داد که امارات ادعای بنیامین نتانیاهو، نخست‌وزیر اسرائیل، مبنی بر سفر به این کشور حاشیه خلیج فارس در جریان جنگ ایران را رد کرد.
خبرگزاری مهر به نقل از عراقچی نوشت: «من به خاطر حفظ وحدت، در سخنرانی‌ام در بریکس نامی از امارات نبردم. اما حقیقت این است که امارات مستقیماً در تجاوز علیه کشور من دخیل بود. وقتی حملات آغاز شد، آن‌ها حتی آن را محکوم هم نکردند.»
رسانه‌های ایرانی مشخص نکردند که نماینده امارات چه اظهاراتی در این نشست مطرح کرده بود.
بر اساس این گزارش‌ها، عراقچی همچنین گفت که «نه پایگاه‌های آمریکا و نه اتحاد با اسرائیل برای امارات امنیت به همراه نیاورده و این کشور باید در سیاست خود نسبت به ایران تجدیدنظر کند».
عراقچی پیش‌ از این نیز گفته بود: «کسانی که با اسرائیل برای ایجاد تفرقه همکاری می‌کنند، پاسخگو خواهند شد.»
رسانه‌های ایرانی همچنین درباره اینکه آیا شرکت‌کنندگان نشست وزیران خارجه بریکس در هند خواهند توانست بیانیه نهایی مشترکی صادر کنند یا نه، ابراز تردید کرده‌اند؛ زیرا اختلافات میان ایران و امارات ادامه دارد.
در همین رابطه از کاظم غریب‌آبادی، معاون وزیر خارجه ایران، نقل شده که به دلیل حضور امارات در این نشست، «مشکلات و رایزنی‌هایی» وجود داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 190K · <a href="https://t.me/VahidOnline/75463" target="_blank">📅 18:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If7-cJODfn2E-Ugwe2reogndfP-rxuPFvn0TebV7W13ZyDxQKvTFOxkEduzUyDWBehu4DU91WWIT7n0M2FzKJ6LIRQOw55ZTiiUTRQq37yoIUfOcvq_wR11rk5a-ktp4136L4eW_NvPiRCHrODvpE5t8NVDpaiYi5dAPiLi53lLUFCsCUp_TjLQqCFybvDOe2w2USjDZMgWLLvYrJ-L-X1S8hEaWEcYfFddBiFoy0XS2qbz0ZDZT1hTomHf15NuoLhbgPxb_Qf0R4Fnqwfinw50Jc9CHohUu_SCvqTesn6RyMy3Le1YYywfPJpo_VG8Vcj0uq4jzcSW_5twpM_p19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یونهاپ، خبرگزاری دولتی کره جنوبی، روز چهارشنبه ۲۴ اردیبهشت به نقل از یکی از مقام‌های امنیتی این کشور گزارش کرد که بررسی‌های سئول نشان می‌دهد که به احتمال بسیار زیاد جمهوری اسلامی ایران مسئول حمله به کشتی باری این کشور در تنگه هرمز بوده است.
سفارت جمهوری اسلامی در سئول هفته گذشته هرگونه حمله جمهوری اسلامی به کشتی باری کره جنوبی در تنگه هرمز را رد کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75462" target="_blank">📅 18:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jodfKJ7dRDd55kXNYWHj94_oTR6hcQakcUAkniJWuympRveNUHNWCPc48KDVwXwDvXgkOViVmYyR0PiXnhh8ww9s_WpFWa6mCdrkh3baZYHeCxDSZ8tNwrICfWKzoKv5E57TXpf8v8Xf7S4JqTTMaw1avCSZi9H4_7IG1fnSm614MgUFdhFrTYi504myz3JTrBymTqwXf_F-SyUZR2-mAPM2LdrX4BgX6HfN0XM2QyWTIdN5X-ANUjJPQtMAnuYlO1YUyt6AtWA_IG6_6Csx1OsmuJDjFeZN00xnDEXxLXuUUqqj1rEamesrKwr3qwArdHBC6I8CkpAKMKHXEvJ17g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا روز پنجشنبه ۲۴ اردیبهشت اعلام کرد پس از وقوع حادثه‌ای دریایی در شمال شرقی امارات متحده عربی، «افراد غیرمجاز» کنترل یک کشتی در لنگرگاه را به دست گرفته‌اند و این کشتی اکنون به سوی آب‌های سرزمینی ایران در حرکت است.
این نهاد گفت گزارشی دربارهٔ حادثه دریایی در ۳۸ مایل دریایی (حدود ۷۰ کیلومتری) شمال شرقی بندر فجیره امارات متحده عربی دریافت کرده و پس از آن، کشتی به تصرف درآمده و مسیر آن به سوی آب‌های سرزمینی ایران تغییر داده شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 194K · <a href="https://t.me/VahidOnline/75461" target="_blank">📅 18:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVG-hlmSAEmuIn2_6c5bKBIhdWrYeUm9MojzCVtUXmSgsudNdsAYs0VTvSJzQ-7GAsQ6k9NfCAwH7WUL8gFhdalzGHhHEg6OYJ05EU1HeviAhrzvKN4CkBXnfZnpKlMZB0D6QSgLjYTn2nznct3ipsfPaIYsAfZTzhnUbb36Bbg6nOgxM-J3GhDHqpooprzT6pw3qMFK7v0gDqzRW-Gh9a2f5wPiEH1kzrFl7CCzTyXQ1Nt-YbJxN6_PHYPIIMugkQeufyVPj2zxBHKzUPfuKK5dEWifQOZWsdUVndm9f7-QNSK4U8-XZ8avgKxIpa7JBeDnIUib_CW10fwvyG0Olg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید اعلام کرد که دونالد ترامپ و شی جین‌پینگ، در پکن توافق کردند که ایران هرگز نباید به سلاح هسته‌ای دست پیدا کند و تنگه هرمز باید باز بماند.
آمریکا این گفت‌وگوی دو ساعته را «خوب» توصیف کرده و می‌گوید که دو رهبر در حال تلاش برای تقویت همکاری‌های اقتصادی هستند.
در بیانیه کاخ سفید، رئیس‌جمهور شی همچنین «علاقه‌مندی خود را» برای خرید بیشتر نفت آمریکا ابراز کرد تا وابستگی چین به تنگه هرمز را کاهش دهد.
همچنین گفته شد که مدیران برخی از بزرگ‌ترین شرکت‌های آمریکایی هم در بخشی از این دیدار حضور داشتند.
آن‌ها همچنین درباره اهمیت پایان دادن به ورود مواد اولیه برای ساخت ماده مخدر فنتانیل به آمریکا هم صحبت کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75460" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hr6PJ4WzMpbEgw6ToDKswGJLAbzcwWKJCkAnqVUmJ2BmR0q2qOmF_aT6vddeSaWq-dHNQAgWipHyaaclMC58pAst73mBNiprdP6njb-Xfs8ZfAyxu9zABDurgSS0RM-sLayTUElPRHYznBkFPaitEkACgI4Rb0aMTJg0GhBf7sxtepS1dKstcm9L3OaJhdZBN7ypYRgz2KNnG2K3PXO6mxM3K9u_4jMFQXoZaKYMZQGAKEV3t88dG8E1Rc2Vh7VoskGbhDf-nkbXR6ITUDPAAE1i8D0xGbZHk5lA4Gh6NOmKvIm3AcL1mBQD5-nGTccgl8S8zSqk1fYM7WNDqO4NPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، می‌گوید به نفع چین است که حکومت ایران را برای باز کردن تنگه هرمز تحت فشار بگذارد.
براساس گزارشی که فاکس‌نیوز از اظهارات روبیو در راه سفر به چین پخش کرد، او گفت: «ما این استدلال را با چینی‌ها مطرح کرده‌ایم و امیدوارم قانع‌کننده باشد. آن‌ها اواخر این هفته در سازمان ملل فرصت خواهند داشت دربارهٔ این موضوع اقدامی انجام دهند؛ زمانی که قطعنامه‌ای برای محکوم کردن اقدامات ایران در ارتباط با تنگه‌ها مطرح می‌شود.»
روبیو گفت حکومت ایران در حال ایجاد ظرفیتی بوده که بتواند با «انبوهی از موشک‌ها و پهپادها» سامانه‌های دفاعی کشورهای منطقه را از کار بیندازد و هرگونه حملهٔ احتمالی به برنامه هسته‌ای خود را با تهدید به وارد کردن خسارت گسترده به کشورهای خلیج فارس پاسخ دهد.
مارکو روبیو همچنین با اشاره به بحران تنگه هرمز، گفت این وضعیت بیش از هر کشور دیگری به زیان چین است و پکن باید ایران را برای عقب‌نشینی از اقداماتش تحت فشار بگذارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/VahidOnline/75459" target="_blank">📅 18:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75457">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jv_fLS5WXAnELtCauihLzahc19IfEzQDIF2uNtiXSnkqJNCWPtoAMzxbaCDamNKAY8yLdwVg71n3H2vCUB3lBqPWy49kRt-gK0sHMODvF9RNpWzXe10mzp0eQWuzvxWJ_Dmutir-k3JVeKyQMHf4OLX0a4WFquWIArxb8hC-W53hYn6RX-OKidCEf3xCZtV9T-j-Lj9vN5HUVVORxYq4FXT-H7zOYhlHuTPckgN4DKzhRyrdMbXlCkKwQcisl2IIskmg_6ygKc4IdMwmnDOmqqzM6XY-qH7ezx2waSdQLNoR6HZjzxMBnpUcAu1ka304H1Zh0SKXhFrbLvndMWb3aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P0O4XMjv8SAmB6VL_2WsJdnbLsVV4bNkwi_3QtxCQpkbyXj3RoW7QVw4naPsW1U8akyWP0eH8gNXt9kPzxoEBFNVrl5Oe0kgDNHqsL8HVbuWpvxwNfi8iLPi7zuQ1ZBMBcB0IgTGNbUpspk2zsLf_43zqWv5oCFmPVeYKFuOrpNSh4H436-MiekSLpFyJfjjbfVZtFMF8Af13BYn17Xfvk3kRorl-21bSKEL255Co_584yGTXMk0oZyCFlMw1_kxDdu5cTRE1s65WosREARQ_-oVzDYIyf-Rypy4n48cqr_fK7mz0Y_664TuHNQVEBIuo5oQKZwio2XU6kgkhbzxnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نت‌بلاکس، نهاد بین‌المللی پایش اینترنت، نوشت که پس از بیش از ۱۸۰۰ ساعت قطعی اینترنت در ایران، نظامی طبقاتی توسط جمهوری اسلامی برای دسترسی ایجاد شده است.
😋
💩
همزمان مهدی طباطبایی، معاون ارتباطات و اطلاع‌رسانی دفتر مسعود پزشکیان، ادعا کرده است که اگر همه‌پرسی برگزار شود، مردم در شرایط جنگی، امنیت را به سهولت دسترسی به اینترنت ترجیح خواهند داد.
@
VahidHeadline
روزنامه اعتماد گزارش داد که نخستین نشست «ستاد ویژه ساماندهی و راهبری فضای مجازی» هفته آینده به ریاست محمدرضا عارف برگزار خواهد شد.
هدف اصلی این ستاد، فراهم کردن زمینه‌های لازم برای رفع محدودیت‌های فضای مجازی است تا حداکثر تا میانه خردادماه، امکان اتصال مجدد شهروندان به اینترنت بین‌المللی فراهم شود.
عارف در این مسیر قصد دارد از ظرفیت نخبگان و اساتید برجسته ارتباطات نظیر هادی خانیکی و علی ربیعی [
🤨
] استفاده کرده و میان نهادهای حاکمیتی برای بازگشت سرویس‌دهی هم‌افزایی ایجاد کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/VahidOnline/75457" target="_blank">📅 18:06 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75456">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlWAmCVzvKkdrBJuOMmOfLaMX9Z1zi93jo8oqNTP6GnPD2f5yA38bOixhV9nT1ZxCrLztTA7CvMB9Ek8L6wm9caCuMBCr1c9ULHax3B6ManhCql21S-Gt0MAIpa90M9S6QBDwVtO4i8OnNv7ZPoplzC84y4P3YH1bW_rr-3NuWscftPRRRDU03qajb1gsBFL26VLXoz0WsyyWyUmC2RjgbypLgqUrhBPUlKDk8PLD0Dn9SxAVRYEPhyTJWHB57gH-5jPQoQIXYE7fsso6w2xHWvHiU3tlIlNJIyVoTXLutwA0yv8lRbegWr3IUQK1pcI_DjoRarOnmWFj0AD-3TIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی شفاخواه، فعال حوزه آموزش و حمایت از کودکان کار و ساکنان مناطق محروم، توسط نیروهای وزارت اطلاعات جمهوری اسلامی بازداشت شد.
این فعال حوزه کودکان عصر سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، ماموران وزارت اطلاعات بازداشت و به مکان نامعلومی منتقل شد. همچنین تمامی وسایل الکترونیکی و ارتباطی او و همسرش نیز توقیف شده است.
@
VahidHeadline
هنوز از دلایل بازداشت، اتهامات انتسابی و محل دقیق نگهداری شفاخواه هیچ اطلاع دقیقی در دسترس نیست و پیگیری‌های خانواده او برای کسب اطلاع از وضعیت سلامت او بی‌نتیجه مانده است.
مهدی شفاخواه طی سال‌های اخیر به صورت داوطلبانه در مناطق محروم و حاشیه‌نشین فعالیت داشته و از طریق آموزش ورزش و مهارت‌های اجتماعی به کودکان کار و نوجوانان آسیب‌پذیر، در راستای کاهش آسیب‌های اجتماعی از جمله اعتیاد و بزهکاری تلاش می‌کرد.
او برادر رضا شفاخواه، وکیل دادگستری و فعال حقوق کودکان و زندانیان سیاسی، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75456" target="_blank">📅 18:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75455">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=GaiEOc6Zh63_OuMOrsgb9rezRycoZ8eCZWRRZz9fWdoP5qcle2KZcIfBrEH8eK88nDx_XQfQgJUtmvn8VkZVJtUJRgU_2MGwJ9qJ1x02ZN3gOGE0T3y5u_zS4jTsP4m1C4on43lfZoQdVMDeNoS6rXeCUTF2zcMf8Wx0h_A3trkVpXRKFAidYl1jY-GiiTGGVNrPWuzt_F9hIU1u6otv1iMF5AEPC-HDRB7dweZqZK9jk8bHqqKlkURWpJ4OxqwA4IEKRkSltI8tRMSfRSbtBEYNjtTdAcnYQfwFVPyer5Gw5Wt2P5txkCIyPtnkoCO72-1P9Tpo4FKi_GNUL3CmYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6ed3795eb9.mp4?token=GaiEOc6Zh63_OuMOrsgb9rezRycoZ8eCZWRRZz9fWdoP5qcle2KZcIfBrEH8eK88nDx_XQfQgJUtmvn8VkZVJtUJRgU_2MGwJ9qJ1x02ZN3gOGE0T3y5u_zS4jTsP4m1C4on43lfZoQdVMDeNoS6rXeCUTF2zcMf8Wx0h_A3trkVpXRKFAidYl1jY-GiiTGGVNrPWuzt_F9hIU1u6otv1iMF5AEPC-HDRB7dweZqZK9jk8bHqqKlkURWpJ4OxqwA4IEKRkSltI8tRMSfRSbtBEYNjtTdAcnYQfwFVPyer5Gw5Wt2P5txkCIyPtnkoCO72-1P9Tpo4FKi_GNUL3CmYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر پرچم حزب‌الله را در ویدیوی مربوط به بدرقه فوتبالیست‌ها سانسور کرد.
FattahiFarzad
دیده شدن پرچم حزب‌الله تو اینستاگرام مساوی با پاک شدن ویدئوست و ممکنه حتی اکانتشون هم بن بشه.
Sam1Kia
اعضای تیم فوتبال چهارشنبه‌شب ۲۳ اردیبهشت‌ماه در میدان انقلاب تهران برای حضور در جام جهانی ۲۰۲۶ بدرقه شدند؛ رقابت‌هایی که خرداد و تیر ۱۴۰۵ به میزبانی مشترک آمریکا، مکزیک و کانادا برگزار خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/75455" target="_blank">📅 07:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75454">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qU2l3LHD_flEtF4SqaNT3Ip22pyc9KKiXGyK9h_pJIjfC2xqChqI5tFO_lCWvILIJxrP33VFEhrL7AQAdAspgy69wRUaZZX9mX7JVugkiPtacpivfKHCCIeUhGNZ8gxTOkv8VkBH9wQytCHvuV26pPScOrnmzNJVcb1Qs_JwensiYUWo_MZPVdTyBJxmWJMhlix7w1E01XOpkWTyJFGUFUg8OeR4by3Bm9T9yubLVyoFhAdqLD-Nwl9mL_cS52XVx1w4Pby35vqASc2deQUYT9kp3jhCer4nQRJqPwu0N-GXD4Q-drZbPKadXAd5-vzzPkxEYlXjey7_94mnJrwyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی اعلام کرد گزارش‌های منتشرشده درباره سفر بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به این کشور صحت ندارد.
پیش‌تر دفتر نخست‌وزیری اسرائیل اعلام کرد بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی، به‌طور مخفیانه به امارات متحده عربی سفر کرده و در این سفر با محمد بن زاید آل نهیان، رییس امارات متحده عربی، دیدار کرد.
وزارت خارجه امارات متحده عربی اعلام کرد روابط این کشور با اسرائیل علنی است و در چارچوب توافق‌نامه‌های ابراهیم که به‌طور عمومی اعلام شده‌اند، برقرار شده است.
وزارت خارجه امارات متحده عربی افزود این روابط مبتنی بر محرمانگی نیست و هرگونه ادعا درباره سفرها یا ترتیبات اعلام‌نشده «بی‌اساس» است، مگر آن‌که به‌صورت رسمی از سوی امارات متحده عربی اعلام شود.
عباس عراقچی در واکنش به سفر نتانیاهو به امارات متحده عربی در زمان جنگ، نوشت: همکاری با اسرائیل در این مسیر غیرقابل بخشش است. افرادی که برای ایجاد اختلاف با اسرائیل همکاری می‌کنند، پاسخگو خواهند شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75454" target="_blank">📅 00:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75453">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLlSbuu-cDHuHxatUqosSv_saw_c64kYQujIWzC55LbXuBjVoC2PgXpZEGiyv9UlcENDWP-JW9zml1hHG30Zqxz3pS3V6RJ5vE0bTDycZNHnE71NofX59xy5vxJIme0JYSd64UwJENeSKBL7146MTrdsvgv4ggjPgO77PWt7SVxmLyqgtT_4iTRIkZdoMOhieHQHeneqxEBf7ml8XnTKMjx3uCUX0bNXZ8w3GLW3N8msmbktuUIWSbOoFelXRNpfbLhOgkyj2Sq5mytI9IAphJF9eHfhXwHtByj3NaOPMclismGTbKGq2KeN-eXSGNPt_KZMRp_A36ErE8i8-DZq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد که واشینگتن معتقد است در مذاکرات با ایران «پیشرفت» حاصل شده، اما هنوز مشخص نیست این پیشرفت برای عبور از خط قرمز دونالد ترامپ کافی باشد یا نه.
آقای ونس روز چهارشنبه در کاخ سفید به خبرنگاران گفت صبح همان روز با جرد کوشنر و استیو ویتکاف درباره ایران گفت‌وگو کرده و همچنین با مقام‌های عرب در تماس بوده است. او افزود: «سوال اصلی این است که آیا این پیشرفت به اندازه‌ای هست که خط قرمز رئیس‌جمهور را تأمین کند یا نه.»
به گفته معاون رئیس‌جمهور آمریکا، خط قرمز ترامپ این است که ایالات متحده مطمئن شود «سازوکارهای کافی» ایجاد شده تا ایران هرگز به سلاح هسته‌ای دست پیدا نکند.
اظهارات ونس در حالی مطرح می‌شود که ترامپ پیش‌تر پیشنهاد تازه ایران در مذاکرات را «غیرقابل قبول» توصیف کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75453" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75452">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jkw03A7V74nTdzpNkGuApz9Iswwkt0x7MwCNqD7Qepo--ayfZkenlLAjwWA3YGuE4XnfGgUr3LpHQdkfIRcbdWCkJ0dehVGaJuqplE-mIjpwohwOvpHPPKfWYXFzjhVE4Ad5bT2xOQh_tQB5UdbqQNqVwAW_yhaYzMgbx55G22nAzyUNK4SxeVwFICDMyzIx1YJtpWGfD6euyzuF-DSOpZscAR2mgfAk0qB5vqMVoxbK2hJLHuj-6WSAEeZWXufxs01oq__QBt0m1-EWUSirKfvME4C-d6yPvRQG-Fqh0SFgGHiENphbW44GlD1k2QSpaPPTYc3UfdS7DnvetAIGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی شامگاه چهارشنبه ۲۳ اردیبهشت اعلام کرد که محمد عباسی، یکی از بازداشت‌شدگان اعتراضات دی‌ماه سال گذشته به اتهام قتل یک مأمور امنیتی اعدام شده است.
خبرگزاری میزان، وابسته به این قوه، گفته است که او بعد از تأیید حکم توسط دیوان‌عالی کشور و با توجه به «تقاضای اولیا‌ء دم»، «قصاص» شد.
ساعتی پیش‌تر، پایگاه خبری هرانا به نقل از یک منبع نزدیک به خانواده این زندانی نوشت که مسئولان زندان قزلحصار از خانواده محمد عباسی خواستند که برای ملاقات با او به زندان مراجعه کنند، «اما پس از حضور خانواده در زندان، این امکان از نزدیکان او سلب شد. پس از خروج خانواده عباسی از زندان، آنها در تماسی تلفنی از اجرای حکم اعدام محمد عباسی مطلع شدند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75452" target="_blank">📅 22:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75451">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XXXq8jUsKT1dV7yfQ2_BOwFJq9y3XraklSDXhcK-5GJAK80AukHCf60RMm1FAdWGKrgPjYt2RdJKDPnghDMb3-XIWi2BYEKOj-XIAWI-u7FdFxR3ldvldnhIPQ7G1oxwKKXcR1YoUrznoghI5ajR5rDVHIbBGX_zOaRdlF6bNlSXN3yIJXBCCSeVa3d8JbBqLwQUIfJb2YZzbdrbgcXL6siSD3bFqVI_MUDu4LzhvaAFJmU5L5Z_67friF0Z43B-Z6ObezkfZCnpd_T3JFL0APrbbVFdHSxBKIgaFpULv2uMBRhgTsXS9Fqo3Cnfxyi3XYZE_lTJknSTTidUwUKCkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر نخست‌وزیر اسرائیل روز چهارشنبه اعلام کرد که بنیامین نتانیاهو در جریان جنگ آمریکا و اسرائیل با ایران، به‌طور «محرمانه» به امارات متحده عربی سفر کرده بود.
در این بیانیه آمده که نتانیاهو با شیخ محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
دفتر نخست‌وزیر اسرائیل گفت: «این سفر به یک پیشرفت تاریخی در روابط میان اسرائیل و امارات متحده عربی منجر شد.»
پیش‌تر مقام‌های ارشد آمریکایی تأیید کردند که اسرائیل در جریان جنگ با ایران، یک سامانه پدافندی «گنبد آهنین» به همراه نیروهایی برای بهره‌برداری از آن به امارات اعزام کرده است.
همچنین به گفته مقام‌های عرب و یک منبع آگاه که با روزنامه وال‌استریت جورنال گفت‌وگو کردند، دیوید بارنئا، رئیس موساد، دست‌کم دو بار در طول جنگ با ایران به امارات سفر کرد تا دربارهٔ هماهنگی‌های مربوط به این درگیری رایزنی کند.
@
VahidHeadline
آپدیت:
امارات تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/75451" target="_blank">📅 21:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75449">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvSYiHLUJyh6_XXHGoCUBkR0GyT0BryEqGs8RFgriSpP3zFsgKaPMIUjkJELROk-m0d_fS_g0jnRr77OfTjivZPFD5pnO9NKKCroK8g9RH19ADF9eZaLfGHDaQME8aml9Xv2GnTRjjBrenhQe40vOp2vcOKgLUNOakMGIubgFJU2SQkkytO4AAu3i5ajAJUur6oQn1vgJ2Aj7LSt4R_kHqVGM9U3OeTlDhJ7JKsrwVXCuNLHYZJ9DPAjBxkbG4RhkhxqKwrH-H4yMMXvhNXak9AApVpVgaUZTuIrlEExNtEZpb640xxdeNap0bR8j3zqeZ5pj3ApjYyQOwWxFyFbVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده روز چهارشنبه ۲۳ اردیبهشت با تاکید بر ادامه محاصره دریایی بنادر ایران اعلام کرد که از زمان آغاز این عملیات، به ۱۵ کشتی حامل کمک‌های بشردوستانه اجازه عبور داده شده است.
سنتکام در پیامی در شبکه ایکس نوشت که نیروهای آمریکایی طی چهار هفته گذشته ۶۷ کشتی تجاری را وادار به تغییر مسیر کرده و چهار شناور را نیز برای اجرای محاصره «از کار انداخته‌اند».
این فرماندهی همچنین اعلام کرد اوایل هفته جاری، دو کشتی تجاری دیگر پس از تماس رادیویی و شلیک تیر هشدار از سوی نیروهای آمریکایی مسیر خود را تغییر داده و از ادامه حرکت به سمت بنادر ایران منصرف شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/75449" target="_blank">📅 19:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75448">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=h3XVPPQ6aRt-u_S_seHZyh98AxYAv5Or8GPUNp2shRnJk4yKbXUarNyu4Fn2Wwni5B0fDiL39Dn3qOcoeru1oig8xmOCgtUUGRJUdkeg7Er0As66wF5aCQlkZ2mN0bdJDoge9GJIw-S6xlfexHjxoAOQKVo_zdKE5ycJBUm0G1hRFVnD43NS4dVF3akwGsJzgoR4Jq-rOhD4V93ja5TZpU_8H5eYjTyIRiCE9ax_BG10ICb9hauRGwbEnVqu1A7Wec9D26sT5ui9WYzUn51qQg2IBT33mWMnn7F0nCyhS0x0L_SfMhGAQ9i6aMkMr7bPBpl8N-7_CyYkBZYSJMaiaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/928f9dddaa.mp4?token=h3XVPPQ6aRt-u_S_seHZyh98AxYAv5Or8GPUNp2shRnJk4yKbXUarNyu4Fn2Wwni5B0fDiL39Dn3qOcoeru1oig8xmOCgtUUGRJUdkeg7Er0As66wF5aCQlkZ2mN0bdJDoge9GJIw-S6xlfexHjxoAOQKVo_zdKE5ycJBUm0G1hRFVnD43NS4dVF3akwGsJzgoR4Jq-rOhD4V93ja5TZpU_8H5eYjTyIRiCE9ax_BG10ICb9hauRGwbEnVqu1A7Wec9D26sT5ui9WYzUn51qQg2IBT33mWMnn7F0nCyhS0x0L_SfMhGAQ9i6aMkMr7bPBpl8N-7_CyYkBZYSJMaiaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ‌های ملی‌پوشان فوتبال در صداوسیما درباره میزان تحصیلات دانشگاهی‌شان جنجالی شد.
در این گفتگو، یکی از ملی‌پوشان در پاسخ به سوال مجری که پرسیده بود «در کدام دانشگاه درس می‌خوانی؟» گفت: «نمی‌دانم، الان حضور ذهن ندارم».
در دوره قبلی جام جهانی نیز انتشار ویدیویی از دروازه‌بان تیم ملی فوتبال ایران که گفته بود «من دکترا دارم»، بحث‌برانگیز شده بود؛ دکترایی که بعدها مشخص شد به‌صورت غیرحضوری در رشته تربیت بدنی دانشگاه پیام نور اخذ شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/75448" target="_blank">📅 18:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75447">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTyAqvlDCozaeQP5IR1kG9-dR25y197cQ1C24ZgaMUFlpg54akxLm7g_6DQC8lc5oJ9ciLizj1gOno3ZJxZ28q51mwWmE7Jv8cImvI0bUWZ0FQ3vS8ZfTNtAadPmXhOA6zkdBnRVV6j3PkG7v2EvNO7j83crbkxQ-li4Or-AMueMtwJaGDdsFo__PzqWtMWtwyw1eDhYy1WJUBjabGGSyiqCX0_TFmPzQeX4LHvJTrQjc9iFY612WlWm4mF8HTZnLBmwvJ9Nadj-RBweHCsuKcj7EcwCaxJeGmitO9wNp7mqmcqmCWe5eQDA_m9jWo-DoNQYaYdQtVU9KEBJWsCCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز به نقل از دو مقام غربی و دو مقام ایرانی گزارش داد عربستان سعودی در جریان جنگ خاورمیانه، در پاسخ به حملاتی که در خاک این کشور انجام شده بود، چندین حمله اعلام‌نشده در ایران انجام داده است.
به گفته دو مقام غربی، این حملات توسط نیروی هوایی عربستان سعودی و در اواخر ماه مارس انجام شده‌اند. یکی از این مقامات گفت این حملات «اقداماتی تلافی‌جویانه در پاسخ به حملاتی بود که عربستان سعودی هدف آن قرار گرفته بود»
رویترز با اشاره به گزارش‌های پیشین درباره حملات امارات متحده عربی به ایران نوشت اقدامات عربستان سعودی و امارات متحده نشان می‌دهد کشورهای عربی خلیج فارس که هدف حملات جمهوری اسلامی قرار گرفته‌اند، به‌تدریج وارد فاز پاسخ‌گویی مستقیم شده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/75447" target="_blank">📅 18:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75446">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB9EzcFpCWWXrzzL61C96GoaY0vukrcQQZ57FA8tAaoX1qWQQag_bItxNawslURplyh4nEV-yxOhNWYb78xt7QlF3ifL5LFo1Ae-hFOl-uxITH2NBEpR8n1jiTOzRTYHSlOxhZNvmNNaqgnckqMiH_oprGJOxYOq-Tu8VDhrHqVsDGYWjqqX8Yu8FgMml8CSXMwfORDNq3qNSurGBgFHRpYQh--Q_BpPE0KmDZBri7M-KSXncOAQjNAErjGAQliXjCGNM1FJUhZIwjt9wlPrw5Zjw8DIWV9KZFbE_nc6bmDcyXsc4xS3ogYQlwX2sSQT9MGwdnf47jFKun9QJBvwmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کمیسیون مستقل اسرائیلی جزئیات تکان‌دهنده‌ای از خشونت جنسی «سیستماتیک و گسترده» توسط حماس و سایر گروه‌های مسلح فلسطینی در جریان حملات ۷ اکتبر ۲۰۲۳ و علیه گروگان‌ها منتشر کرده است.
گزارش ۳۰۰ صفحه‌ای این کمیسیون نتیجه‌گیری می‌کند که تجاوز و شکنجه جنسی «با هدف به حداکثر رساندن درد و رنج» انجام شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/75446" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75445">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UxcQ602FZ660wE4IwpPwyVxhCjaioyZQUSuF_DfK7uyE29CduHK1MzVO1NKys5QfczcnOgGzvluhNjR7CO1d8iEB7FmXN6iBrbRxXH-x47-UFK7It4HB1OvAGc4G_wfG60ama8t33KTP30fkGnJy0UQlLU5cq8yShW_SJckAhKt_2yE8xQ3WeuhTebereOLxs4aGOjKeJYm-0ggjlAbYdG4ODLxM0WwH77wCwQtp4gV7fECBnqeln6MnWJe1vWOTaleszYNqDc6YbuDNGs3OJtOtsW0yrqBK58A3BxzLsauF1rCmFpHuzPNpolJQMQPmz8E65xHqkJMaztLK0wTgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، محمدرضا عارف، معاون اول خود، را به ریاست «ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» منصوب کرد.
در حکم آقای پزشکیان بر «حکمرانی یکپارچه» در فضای مجازی، پایان دادن به «چندصدایی» و جلوگیری از «موازی‌کاری» میان نهادهای مسئول تأکید شده است.
این انتصاب در حالی انجام می‌شود که امروز هفتاد و پنجمین روز اختلال و محدودیت گسترده اینترنت در ایران است.
حکومت ایران از ۹ اسفند (۲۸ فوریه) و همزمان با حملات اسرائیل و آمریکا، دسترسی به اینترنت بین‌الملل را قطع کرد و تماس‌ تلفنی با خارج از ایران هم با اختلال جدی رو‌به‌رو است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/75445" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75444">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mt1SNqzJGZGB1GWB6rb-en8dmFcAsE_b4qiIljOT9vAhbt-84MtbH1H9IdXJShrhFx0ZOKqLSIl0uRwZoJ862fAmLQ3TF7Z7pugVjGkHFDgEln51VkW8D55903R5HQ42uK5cPnZPVESs2E86T1zTx0LrS2X5gURn9k3jQIw5JEYDOlwhwLR_uptUvC8g7e8gKExP6JChVAG143fMpCXcaR9QA84RP_q9eYikqyg32QHUr3c6e20Clkyy5aSragaSF-zvxJLwLeDBHZtA74Phz8F4oS7Y5kiM1dzJZ6kjsQJyW5UOXd30_tyV3qDmV4m6pqPk7TIKKYJRizA-dNstJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، وابسته به سازمان تبلیغات اسلامی، مهدی زارع، زلزله‌شناس و استاد پژوهشگاه بین‌المللی زلزله‌شناسی و مهندسی زلزله با اشاره به زمین‌لرزه به بزرگی ۷.۱ در قرن نوزدهم در گسل شرق تهران گفت: «وقوع زلزله‌های ۴ ریشتری اخیر در ۲۸ فروردین و ۲۲ اردیبهشت در پردیس نشان از تخلیه انرژی دارد. وقوع زمین‌لرزه‌های کوچک به صورت مستمر، بخشی از انرژی گسل را تخلیه می‌کند، ولی این لرزه‌ها می‌توانند نشانه‌ای از ناپایداری در پهنه‌ای وسیع‌تر باشند که مقدمه رویداد بزرگتری است.
به عبارت دیگر، لرزه‌های خرد و متوسط، هرچند تا حدی تنش را کاهش می‌دهند، اما نمی‌توانند به طور قطع احتمال وقوع یک زلزله بزرگ را منتفی کنند. در برخی موارد، چنین توالی‌هایی می‌توانند پیش‌لرزه (foreshock) باشند.»
@
VahidOOnLine
امروز پیام‌هایی از پس‌لرزه یا پیش‌لرزه ساعت ۱۲:۳۳ دریافت کرده بودم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/75444" target="_blank">📅 17:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75443">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtKk1b0PD6rGEeIh5csFTY2nalbIXdzmOXog9z3B0z-cltvzN4bUyFaK0Ttm3gV2-Ih-iCxMe6M8CKbRgtgDBBZ2BQJ98aOat5dd2fuCyDNHHM8jDDisG_lswhEibvesS3eZM09eyUbNrIqPdQ4AL1YCUdEaq5AyxBbJyXorqHwr24ZiZbMLZWoiTBCTMfMRdk_FOEcJcQUPtFgI1g2wvjjLJukxHCkRad1qM_pW7Rc1f1y01aAZ0WDSEyPUF5hY-R51iJllKONDmnozysmpQKZWRQJbabJfPHHfWf4-wr8BTzGJLRYBUyFdPmGtGz1wnL0SnhSWVdRx7_LALqjkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احسان شیرخانی، شهروند ۳۵ ساله اهل شهرستان ملکان در استان آذربایجان شرقی، بامداد روز سه‌شنبه ۲۲ اردیبهشت ۱۴۰۵، با شلیک مستقیم نیروهای بسیج در ایست بازرسی شهرستان بناب جان خود را از دست داد.
بر اساس گزارش رسیده به ایران‌وایر، نیروهای مستقر در ایست بازرسی بسیج شهرستان بناب، خودروی این شهروند را به بهانه «عدم توجه به دستور ایست» هدف تیراندازی مستقیم قرار داده‌اند.
یک منبع مطلع در این‌باره به ایران‌وایر گفت که نیروهای بسیج بدون رعایت قانون به‌کارگیری سلاح و بدون شلیک تیر هوایی، مستقیما به سمت اتاق خودرو تیراندازی کرده‌اند. به گفته این منبع، چهار گلوله به احسان شیرخانی اصابت کرده و او در دم جان باخته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75443" target="_blank">📅 17:50 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75439">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d2xpsMftKY7_X_hcBJnFIkSZBiGmR16DPLXn450rQMMfOh_G65snabBZGHOVY66xeRLdvVYfkwat2Am_7hNOBkJ5-nClY9NAv33UL5Jv__sWzimwoOEU72EoHqWOpdv_t91DIM8bEmlOUoWmgR46Vq5C2FPEpJJZSwlW7pHZ7_AaFVWo4RK11bVxqmUwHQmr9pixuQIwx-P-oSKbkmVtK-KRub8PCNjinMRD9TFNj-0QkrB2r5MaUjmunBFcGlMQMuoqMLsF_n0ASKTFss5eQ7Y6XG0tStQgJXua3_vR7YvW50ctmgIkUfrOe_TqUTmI8tqURf4GpIzNWHVllfHO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XXjmPn6_Tt_HPPFtidLzAvyIrR6lG1KKB9n2ao8LUtaTSx8wah_RPo-zQ5k_Sp4fLuH6H6zGxKmPLd30TCMKTNVQRZnqgbAeyBiCxvhpcVy8B53ks7eS2pM-C2EsHTqDwHZcHrCkJ7Wj2UebtgBYl2mmyNLbohu4avN4_o4Q7lu3G9jGDAkMpv3mf54eVT4uC3bTKrtXHwG70r6yGIisAitz4WuyLkniniB803gRPWeX-Dq-arpK_KiQMKuAxujq396tLl60hTooO601PhQhU89o0yRkxPSRzrsACDoFr7z2vPXQ8CIeXuwmODRdWcWNk_EtvoyMBwX1tLpIxSI_JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oO6EuXYp6CJnqZLPLIJY7w6LqAJveQ5ewgkRIRnti8hC-1XCRWFW7FJ61EGd6hepOY1asPGsM4PDatryUjOERn28BNNlR4_d3dxavZ4VtCwMq3evDdQxIFSwze2IyYoJ45jGCX0dwQ_hewK4ITwZi0YAlMRMt-ByDwtU_q8hV0TTJAt_KeaWAl7oGfmDPeJPOx6ViegEyZSnYpOpW3g4wSAU5gErhvWqhnKPXa_GRUGygHAWN0rh739SEF-y9az4Nd4-W8v0yw-NBNiWLI5frfsmOMtUnS5gFxAFCt0WDZDqExZRmzbpHtfCGRyzFgjdUOsOCM-cS00NT3jL3UuQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/URnDu6t6StZaOpI_b7_FJldqBksM4HM7mDO8R3wz2j439RAwLL2FzRsUHjwwuF3nYoy5ed-KPzefhvVPVki-Rddh6OHwqSiZKGniQICcA6WpVflP7m5KkYG5jKPjGXy_INyLiN8cRgAugTTcs74Nhw4N0Z_WWGhxDUB9cJYCdXI6iPSlmikJKJlIoFgmAFq01zLy4KkgeiWlq9__CJl9cd3wumcR5cVNRoPnRGRyT48NQiWcKv_tDNZoN80UV6R0HLFySUuHwZamCTvjgJTCH-mFpK43yT-yTaLMfPeRydRTQ_4BBnS2V236mjCSt7trtIm4Iyu6sd7-EvhIBULJdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قوه قضائیه ایران یک زندانی دیگر به نام احسان افرشته را به اتهام «جاسوسی» برای اسرائیل اعدام کرد.
میزان‌نیوز نوشته که افراشته که «در نپال توسط موساد آموزش دیده بود و اطلاعات حساس کشور را به اسرائیل می‌فروخت»، بامداد چهارشنبه ۲۳ اردیبهشت اعدام شد.
در بخشی از گزارش بدون اشاره به جزئیات آمده که او «به عنوان کارشناس سایبری در یک شرکت وابسته نهاد نظامی مشغول به فعالیت» بود.
با این حال در گزارش مفصلی که ارگان رسمی دستگاه قضایی ایران درباره این زندانی منتشر کرده، مشخص نیست که او چه زمانی بازداشت و دادگاهی شده و از جزئیات روند محاکمهٔ او نیز اطلاعاتی منتشر نکرده است.
شماری از وب‌سایت‌ها و نهادهای حقوق بشری نوشته‌اند که احسان افرشته، متولد سال ۱۳۷۲ و فارغ‌التحصیل کارشناسی ارشد مهندسی عمران و متخصص شبکه، اوایل سال ۱۴۰۳ پس از بازگشت از ترکیه بازداشت شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/75439" target="_blank">📅 08:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75438">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CuZ9zytqjkF4jJL71axB2b6MqEmDgc_cA_2OHHvlEeem_B7izVIJ3nkUEhu7UPHcVsWALaTjKhXvtfuHY_P6u0JWLmwQHYm0joI8W9TCUGutP9oIvlNjUViyPCY5FXO4EaNSMtb-Krne-DY4bh3Y8HbOne8ILdSqJgXS4Gcmo9WbzEHz7q7riCkchah2jAnAdfZserO34Tw_5rLtjXILa4F3ziDWrBq29sXdtSnVcgktQFi-NHx-VdxQt6GlYxDOfXoqlAishBPfPyQ5RnBKTSIo1KYiID4BTl0edlS_epDpzivSIa9RUDX7pJxGek1rQ-EclJ17bCevzRX68_903w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه چهارم۰۰:۳۳
پیام‌های دریافتی:
دوباره لرزید  شرق همین الان 12:33
بازم اومد ولی ریزتر از قبلی
همین الان دوباره لرزید (نارمک ) ۰۰:۳۳
من الان دوباره لرزیدم
وحیددد نزدیک چهاربار تو پردیس
#زلزله
اومد نمیدونی تختم چجوری میلرزید
آپدیت: تصویر دریافتی بالا و متن رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
بزرگی: ۳.۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان وقوع: ۳۲ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۱۰ کیلومتر
🔹
نزدیک‌ترین شهرها:
۱۰ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۱ کیلومتری تهران
۷۶ کیلومتری كرج
🔄
آپدیت ۳:۳۰
پیام‌های دریافتی درباره لرزش پنجم
زلزله دوباره
ساعت ۳:۳۳ شرق تهران باز زلزله اومد
پردیس،۵ دقیقه پیش برای پنجمین بار زلزله اومد وحید جان سابقه نداشته تا حالا خیلی مشکوکه
ساعت ۳:۳۵
پردیس دوباره لرزید سه و نیم
سلام وحید جان
ساعت ۳.۵ باز زمین لرزه اومد پردیس، با صدایی شبیه به ترکیدن
🔄
آپدیت: لرزش ششم ساعت ۵:۵۷
یه کوچولو دیگه زلزله سمت پردیس حس شد الان
و الان هم دوباره لرزید
٥:٥٧ دوباره پس لرزه اما خفيف تر
آقا وحید ساعت ۵:۵۵ دقیقه صبح، پردیس برای ششمین بار لرزش احساس شد
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75438" target="_blank">📅 00:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75437">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">زمین‌لرزه دیگری به بزرگی ۴
این میشه سومین بار ظرف چند ساعت گذشته! اولین باردر شرق استان احساس شد و پیام‌ها از پردیس و بومهن و دماوند بود و یکی هم از لواسان]
پیام‌های دریافتی لرزش سوم:
تهران مجددا لرزید
دوباره لرزید کمی خفیف‌تر
وحید جان دوباره لرزیدیم  شرق تهران .. ۲۷
دوباره! پس لرزه بود.
دوباره هم اومد ولی ضعیف بود خوشبختانه
وحید جان شاید باورت نشه اما سومیش هم همین الان اومد، منتها خیلی کوتاه و کم بود...
ان، زلزله، ۰۰:۲۷
باز اومد، کوتاه، شاید پس لرزه باشه
دوباره اومد
یعنی اون رفت این برگشت
دوباره زلزله اومد
باز هم لرزش ۱۲:۲۷
سلام بازم لرزید حدود دو سه دقیقه پیش طوفانم هست خدا رحم کنه تو این شرایط فقط بلایای طبیعی کم داریم
اینجا ازگل، ۱۲:۲۷دقیقه، دوباره لرزید
🔄
رسانه‌های داخلی به نقل از مرکز لرزه‌نگاری:
🔹
بزرگی: ۴
🔹
محل وقوع: حوالی پرديس
🔹
زمان: ۲۶ دقیقه بامداد
🔹
عمق زمین‌لرزه: ۸ کیلومتر
🔹
نزدیک‌ترین شهرها:
۹ کیلومتری پرديس (تهران)
۱۱ کیلومتری بومهن (تهران)
۱۲ کیلومتری رودهن (تهران)
🔹
نزدیکترین مراکز استان:
۴۰ کیلومتری تهران
۷۶ کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75437" target="_blank">📅 00:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75436">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TvL1x8duRsOcgWv8aGUQqZ2dJYybcI44dPRNQXds97WpD_KmMdRxVAsuVaLEeDxY5GWMPxEY4FFf6QQS6rhNeUhIxN2NK4caU1C6f0iwX0sxRfKzZttT2zJK7X9fuhwXX5gsgJCWi15bbV-x3QiqxIqLi98Oopejen2Dm9swRhAEgzR3msVrtKTVC6k23nLcbygOhAZbn2cOZGiP2lZ4B7GFow2p7hZKiG4oqMbTFUfwXKp-J5UuNv9VctY_6wyMiyKP3pwZNiQnviKpTfDLuktNR2WwMoo78tPM0SjHZqkyBCwPujcdT2EuAld4oI_JfzZMw6uFfODlcKoHTMFJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
وقتی «رسانه‌های جعلی» می‌گویند دشمن ایرانی از نظر نظامی در برابر ما عملکرد خوبی دارد، این عملاً خیانت است؛ چون چنین ادعایی کاملاً دروغ و حتی مضحک است. آن‌ها به دشمن کمک و از او حمایت می‌کنند! تنها نتیجه‌اش این است که به ایران امیدی واهی می‌دهد؛ در حالی که اصلاً نباید چنین امیدی وجود داشته باشد. این‌ها بزدل‌های آمریکایی هستند که علیه کشور خودمان طرف می‌گیرند.
ایران ۱۵۹ کشتی در نیروی دریایی خود داشت؛ تک‌تک آن کشتی‌ها اکنون در کف دریا آرمیده‌اند. آن‌ها دیگر نیروی دریایی ندارند، نیروی هوایی‌شان از بین رفته، تمام فناوری‌شان نابود شده، «رهبران»شان دیگر در میان ما نیستند، و کشورشان یک فاجعه اقتصادی است.
فقط بازنده‌ها، ناسپاس‌ها و احمق‌ها می‌توانند علیه آمریکا استدلالی مطرح کنند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75436" target="_blank">📅 23:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75435">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">"وحید تهران لرزید"
+ ده‌ها پیام دریافتی مشابه درباره احساس لرزش زمین در مناطق مختلف تهران
به نظر می‌رسه بیشتر پیام‌ها از سمت شرق و شمال شرق تهران هستند گرچه در غرب شهر هم کاملا حس شده.
حدود سه ساعت پیش هم در شرق استان تهران حوالی پردیس و بومهن و دماوند زمین‌‌لرزه خفیف‌تری حس شده بود و غیر از اون مناطق فقط یک پیام از لواسان داشتم و پیامی از خود تهران نداشتم.
🔄
رسانه‌های داخلی:
زمین‌لرزه‌ای به بزرگی ۴.۶  ساعت ۲۳:۴۶ امشب مرز استان‌های تهران و مازندران را لرزاند.
این زلزله در حوالی شهر پردیس و در عمق ۱۰ کیلومتری زمین به وقوع پیوسته و در بخش‌هایی از پایتخت نیز احساس شده است.
بزرگی: 4.6
محل وقوع: مرز استانهای تهران و مازندران  - حوالی پرديس
تاریخ و زمان وقوع به وقت محلی: 1405/02/22 23:46:07
طول جغرافیایی: 51.83
عرض جغرافیایی: 35.82
عمق زمین‌لرزه: 10 کیلومتر
نزدیک‌ترین شهرها:
8 کیلومتری پرديس (تهران)
10 کیلومتری بومهن (تهران)
11 کیلومتری رودهن (تهران)
نزدیکترین مراکز استان:
41 کیلومتری تهران
77 کیلومتری كرج
#زلزله
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75435" target="_blank">📅 23:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75433">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/giJVNgWdpvUy-MAHPjiE44DtvTq78yXeZgrx4vUFYwERVIgeQgYmdKYN1YmeuTlKbFOZQi1_ld6xMq5-a5mgOCeB_37fslbdNMDa8cZdlUrTv_On31-GXy_zG6vxbEvwXN_YyQT0Kgdt8uiXjLnh1weBEnJvfq14eVH9YpVOmK9HvJT-Oz5Zw_QOkKtLvZWlG13C3C1zQGJPdGjMKmEDGfb-bKiK5gnbT-dqbkHZcrtBILjg6YrzCX-WrcHC0Typri23fY1cmhbT9eOpFhcFYde5r_bSFzmTfs4XyPGwPP06z4DXZOJS8dmPbnPkYUisE-vKSSXPSfzyxu1axKuArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=vHibw8eTdujFoWvshuwI7ErGWgygMwtvO1oyWL9Hc7D1iU7BG_k04MdgL8imS5ED2FismhmfWLfcFOYmNPihascN3ki84X0AwlQoicABO4S4KXLoqlWKURnPDC2hgakRsQtr_wiXBBi9zRgfyoSNx-594TddUxK8Xaq4IGOjTxcdEVqEeywusIeKmbQCgwQWAX8qcYliFgJNbEDiAA9RUEVtRXR7MXSTTMBdQ0M31B-oIYRIiYkFae89aYtGNL9hu2sQ_Wnhb-ICFCN2qz7diWX9tinyBIA6kDMoUXRe-6xD4qz15MAEKfXHVG1Tk7lWtCsDEppO1--MoMYy8iFBOw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93a0dfa6c7.mp4?token=vHibw8eTdujFoWvshuwI7ErGWgygMwtvO1oyWL9Hc7D1iU7BG_k04MdgL8imS5ED2FismhmfWLfcFOYmNPihascN3ki84X0AwlQoicABO4S4KXLoqlWKURnPDC2hgakRsQtr_wiXBBi9zRgfyoSNx-594TddUxK8Xaq4IGOjTxcdEVqEeywusIeKmbQCgwQWAX8qcYliFgJNbEDiAA9RUEVtRXR7MXSTTMBdQ0M31B-oIYRIiYkFae89aYtGNL9hu2sQ_Wnhb-ICFCN2qz7diWX9tinyBIA6kDMoUXRe-6xD4qz15MAEKfXHVG1Tk7lWtCsDEppO1--MoMYy8iFBOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: خواهیم دید چه خواهد شد
دونالد ترامپ، رئیس‌جمهور آمریکا، پیش از سفر به پکن گفت که رئیس‌جمهور چین درباره جنگ ایران «نسبتاً خوب» عمل کرده است، اما واشینگتن به کمک او نیازی ندارد.
او روز سه شنبه در جمع خبرنگاران افزود که قرار است با شی جین‌پینگ «گفت‌وگویی طولانی» درباره ایران داشته باشد.
ترامپ تصریح کرد: «فکر نمی‌کنم ما به هیچ کمکی درباره ایران نیاز داشته باشیم. ما به هر شکلی که باشد پیروز خواهیم شد. یا به‌صورت مسالمت‌آمیز پیروز می‌شویم یا به شکل دیگری.»
رئیس‌جمهور آمریکا با اشاره به این که توان نظامی ایران در جنگ اخیر از بین رفته است، هشدار داد: ««ایران یا کار درست را انجام خواهد داد یا ما کار را تمام خواهیم کرد.»
او به جزئیات بیشتری درباره این هشدار اشاره نکرد، اما این اظهارات در حالی است که ترامپ پیشنهاد آخر ایران برای توافق پایان جنگ را در روزهای اخیر رد کرده و آن را «کاملا غیر قابل قبول» و «فوق‌العاده ضعیف» خوانده است.
رئیس‌جمهور آمریکا قرار است چهارشنبه برای دیداری رسمی وارد پایتخت چین شود. این سفر که قرار بود در ماه مارس انجام شود، به دلیل درگیری نظامی آمریکا و اسرائیل با ایران چند هفته به تأخیر افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75433" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75432">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CvwNZqOcBn8OBxYaPGy07QtYHVsB9RXkfPZ5wupl78lf43FbcQ7AsbOl7E0Og53KZUoCHSdsw5aJ4G3r9EZxQgqNdmk2RQ5NNYdIhNlf9zN25NTyWgMKJXGN7EFXRz3u0J6B2JYjZAJIUkd69y4ahfhtRjxVVW7eeoy6_5Oqk5_PTP1H7S_bF133sG9E4I0MsRheMI4HzEcmwMgAErFIl3ZxpGt-X56lP1EugoqmuQZGUkf4cUrI_7f8LfwbOIpSQiGHBt7z1IYuIK42fvqMZ1CLVp4_AEqKUeYtGU8eUVEMukv70S9GteWI5E5927BRYzM87G2TqdxRxm8t6SV95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در گفت‌وگو با برنامه رادیویی «سید رازبرگ» گفت: انتظار داریم اقتصاد ایران زیر فشارهای ناشی از محاصره بنادرش فرو بپاشد.
او افزود این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.
ترامپ گفت ایالات متحده در حال انجام ارتباطات مستقیم با مقام‌های تهران است و برای رسیدن به توافق عجله‌ای ندارد و او اطمینان دارد که تهران غنی‌سازی اورانیوم را به‌طور کامل متوقف خواهد کرد.
@
VahidOOnLine
دونالد ترامپ گفت حکومت ایران با انزاویی روبه‌روست که آن را از منابع درآمدش محروم می‌کند و انتظار می‌رود اقتصاد ایران زیر فشارهای ناشی از محاصره بندرها دچار فروپاشی شود.
او افزود: «این درگیری بدون نیاز به شتاب‌زدگی حل‌وفصل خواهد شد و جمهوری اسلامی با انزوایی روبه‌رو است که آن را از منابع درآمدی محروم می‌کند.»
دونالد ترامپ درباره اورانیوم غنی‌شده در ایران گفت مقام‌های جمهوری اسلامی به او گفته‌اند قرار است آنچه او «گردوغبار هسته‌ای» می‌نامد در اختیار آمریکا قرار گیرد، اما بعدا نظرشان را تغییر داده‌اند. او تاکید کرد در نهایت این مواد را به دست خواهند آورد و موضوع را جمع‌وجور می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75432" target="_blank">📅 17:47 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75431">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvk1redCxsBAx4Sfbc-h-xC4Y2KabmbqGyzNGLzI7iZtqdYOq6FUMwc7iRGKxbspGs-X6E8gaJYJBS8WRtSD81V5jlhxWU2GZqO2GkbNda1sxCjKkUi7qPkJ7VHoPiTVO2wpnDkgZd-xrU_Tm63H3g0O8fg_Pp1m8f6Zzo1MHs0LP-PmwvfIyRfMw_FBRLezrd3xtmZ6-AiAZMQim0Dxc1AoBt_UZNFipjlnKMMU-knAnIkQW7E0ZFHH8XKJDSrIkPCeXlBvlYl5USkxbl1qbYJUIs6IZjOp8BoLNYTs6icZDr_2hTWJAXG4C145Z6W5Cz3RFCmyumfkYAW1NMpX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد پنتاگون روز سه‌شنبه ۲۲ اردیبهشت اعلام کرد که جنگ ایالات متحده با ایران تاکنون ۲۹ میلیارد دلار هزینه داشته است، رقمی که نسبت به برآورد ارائه‌شده در اواخر ماه گذشته، چهار میلیارد دلار افزایش نشان می‌دهد.
به گزارش خبرگزاری رویترز، در حالی که تنها شش ماه تا انتخابات میان‌دوره‌ای کنگره آمریکا باقی مانده است، دموکرات‌ها در نظرسنجی‌های عمومی موقعیت بهتری پیدا کرده‌اند و تلاش می‌کنند این جنگ را به مسائل مربوط به هزینه‌های زندگی پیوند بزنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75431" target="_blank">📅 17:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ne2-eGckV6zoVhd77_AQeafqpweDzw3hYX3z1qdrR4AZ7PWSecu6nk5JQOvJ4cakSDe6tt_D7D3oC2wv6pjoHfHl9UDts9zuMrVnZ5yLK2RWN2RfqDK60HckIc6u1HixrqiesVLfeO4aSeCxa4iHWnF7vrb_y_UezkKZ0FM7uzviPUPo5sXbQTNtqyOkYZaqHB9fmOlKixkgRJoLl5qYjKKtb73pifQPUy6nXBDwXCxkdfjIuGWqKRVm1eYyII6HzifRs_CoQZDLeefQ08jMh6PoDCobHCbbRDKm4mLqk5G77pjfKXj5PL8Q6Gwy8lYNd6lDBm3yfcCM6QV9uuOEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز سه‌شنبه در تروث سوشال دو تصویر گرافیکی منتشر کرد که صحنه‌هایی از حمله به پهپادها و قایق‌های جمهوری اسلامی را نشان می‌دهد.
در یکی از این تصاویر، یک ناو آمریکایی با استفاده از سلاح لیزری یک پهپاد جمهوری اسلامی را هدف قرار داده و نابود می‌کند. در تصویر دیگر، یک پهپاد آمریکایی دو قایق جمهوری اسلامی را هدف قرار داده و منهدم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75430" target="_blank">📅 16:36 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=F5kLuLXaK0ZFgHiFRNeWHXkRG9p6K0zFoWBvtSyubvYwO3194-RrEe9hPU8nAuz5Fsm1-Q6VJVHtE-J5iILlrxEMlbJ16EFep0q6V8niEks0OU1sze1dCqnjMmWh_e45MXiYHMs_U-gBmsxIXjb2vLECQfzTqGdIbOLURW3ph1hHjHKVhoVd-iQ_Cy3TmDYnMgQSgGclVj5MytVWP7uTRU9audIssCzX-_hzQtBC99BxZtNZ0cOTOxWHmnmEcCPVR1I02MS0GrHLOpCqu0a1FGdOdqfJYaI-aTDIa7Df2q9ctmxIw04SVpsHJzRpK8mjz3zbo864u7xGEyvs3M26dA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4234e573f2.mp4?token=F5kLuLXaK0ZFgHiFRNeWHXkRG9p6K0zFoWBvtSyubvYwO3194-RrEe9hPU8nAuz5Fsm1-Q6VJVHtE-J5iILlrxEMlbJ16EFep0q6V8niEks0OU1sze1dCqnjMmWh_e45MXiYHMs_U-gBmsxIXjb2vLECQfzTqGdIbOLURW3ph1hHjHKVhoVd-iQ_Cy3TmDYnMgQSgGclVj5MytVWP7uTRU9audIssCzX-_hzQtBC99BxZtNZ0cOTOxWHmnmEcCPVR1I02MS0GrHLOpCqu0a1FGdOdqfJYaI-aTDIa7Df2q9ctmxIw04SVpsHJzRpK8mjz3zbo864u7xGEyvs3M26dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری سخنگوی دولت مسعود پزشکیان روز سه‌شنبه ۲۲ اردیبهشت به دلیل وضعیت اینترنت به بگومگوی خبرنگاران با فاطمه مهاجرانی منجر شد.
سخنگوی دولت تاکید کرد که «اینترنت پرو» با مصوبه شورای عالی امنیت ملی که ریاست آن را مسعود پزشکیان بر عهده دارد،‌ مورد استفاده قرار می‌گیرد.
او در عین حال تاکید کرد که این اینترنت ویژه کسب و کارها است. [در حالیکه خیلی از مردم بدون کسب و کار هم پیامک گرفتند بیاید پرو بخرید]
@
VahidHeadline
فاطمه مهاجرانی گفت با توجه به وضعیت جنگی، فعلا اینترنت عمومی وصل نخواهد شد.
مهاجرانی در پاسخ به پرسش‌های متعدد خبرنگاران درباره وضعیت اینترنت و به‌ویژه «اینترنت پرو» گفت ما در وضعیت جنگی هستیم. رئیس جمهوری به‌عنوان رئیس شورای عالی امنیت ملی پیگیر حقوق مردم است اما وضعیت جنگی است و بعد از پایان شرایط ویژه، اینترنت به‌حالت قبل بازخواهد گشت.»
پس از این سخنان، چند خبرنگار تلاش کردند تا با یادآوری تعهدات دولت پیگیر وضعیت وصل اینترنت شوند. مهاجرانی خطاب به آن‌ها گفت: «وقتی رئیس جمهوری آمریکا می‌گوید آتش‌بس به تنفس مصنوعی وصل است، انتظار شما چیست؟»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت جمهوری اسلامی، با اشاره به قطعی طولانی‌مدت اینترنت در ایران گفت اینترنت حق مردم است و عصبانیت مردم کاملا درست است. اما در ادامه تاکید کرد: «عامل این عصبانیت دشمنانی هستند که باعث می‌شوند فضای امنیتی ما مخدوش شود.»
او افزود: «رسانه‌ها کمک کنند که این ادبیات را جا بیندازند. دولت طرفدار دسترسی آزاد است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/75429" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i2TpQk_x_Z6bbSW8WR2iVJN8B5PVNVhFoa8irRs1XlO3WYg34L9Ldc45dvsZxmV1VRN3e9hZtlwzqij-wbkJiKJBzS-7zrM4Hk0eNIuhYez9D-NTumKMHTWuSpGXVqtMev1tcy9nDmi8zaSQnt-WUYXNZfeQyxjU3z4wAe_KKB5iIapt5y_twEYoJ_ZoKRhX6endQ9HH_8BYzL5hlql3n9Hi9IBHsHin-rOPc27QUSPQWKqENyQhtFnjytjB-5lqjcGfhZ5KQYsk5EeMsLEJCFDLziokwFkMfVOXIobgr1-CKBUr_phCgUwDdz5wmRQQ7-F5syKtl6Ax4x_6cQVpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه از اجرای حکم اعدام یک زندانی دیگر به نام عبدالجلیل شه‌بخش در بامداد سه‌شنبه ۲۲ اردیبهشت خبر داد.
ارگان رسمی نهاد قضایی ایران، شه‌بخش را «تروریست آموزش‌دیده» گروه «انصارالفرقان» معرفی کرده است.
از زمان حملات آمریکا و اسرائیل به ایران، جمهوری اسلامی اجرای احکام اعدام را افزایش داده است و در برخی روزها چند نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/75428" target="_blank">📅 16:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8SxopnvF5DX4gwW-zhhoaUDf_tKV3VPYVZSMn-JMGMXKL_DbSfyZA0tOQh6FcefAsO9oZFdNNvr2krGp1_FXVnud5_H16sCOMvbfJx1ZVXi5_y5EQjG_kIwLSpuAyedsJw8wUbEU8Ww3rxtPSoTWAD1kyd0qvPmiuJz51pvhjqfhMNj9FksMMU8_9mlkELC3njNI_41LTMnFz-s6jzkquRmySdnXBwJOe5MM7zcJeWRfgHOjCjrJ5wjkv3CqS7diyYOaldQ7fuO0wlwUOMM2_uNH4Tr3EjE9UQG4ZiMn2qHNZaTr3q4p9tZf6T2dPbArT2LF9caTzn0z9sMhgqpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نشریه آمریکایی وال استریت ژورنال، امارات متحده عربی به‌طور مخفیانه حملات نظامی علیه ایران انجام داده است؛ موضوعی که به گفته منابع آگاه به این نشریه، می تواند امارات را به یکی از طرف‌های فعال مخاصمه با ایران مطرح کند.
منابع آگاه به وال استریت ژورنال گفته‌اند حملاتی که امارات تاکنون به‌صورت علنی تایید نکرده، شامل حمله به یک پالایشگاه در جزیره لاوان در خلیج فارس بوده است.
در اوایل آوریل گذشته و هم‌زمان با اعلام آتش‌بس از سوی دونالد ترامپ چند حمله هوایی به تاسیسات نفتی ایران در جزایر این کشور و اصطلاحا مناطق فلات قاره شرکت ملی نفت ایران صورت گرفت که باعث آتش‌سوزی گسترده و خروج بخش بزرگی از ظرفیت پالایشگاه لاوان از مدار برای چندین ماه شد.
ایران در آن زمان اعلام کرده بود این پالایشگاه در یک «حمله دشمن» هدف قرار گرفته و در پاسخ، موجی از حملات موشکی و پهپادی علیه امارات و کویت انجام داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/75427" target="_blank">📅 03:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEBsaRKMmW1dV4e81LcTf5KcOJ3DniTE2lN03lbNt4PCt5J6cKTfgzJ1kGV6l4GIxCC2wYwTY68kaltBFYXuZqeUkWIRz397Gk814ov6pZh1T5s9QYUcRgk_jDz0UmA0rpGdTgOzO5N630bsYAD1YX4nE4Wip6oGbXu2eDuECfkz_C7mEucfGAS3bMYt8Qr7mZjSvZq5nYfKiZ7eSW8ABnmVqz2Awqr-mc_CnBZshxEgIQQp6AX0DqNa4YLjGDwVLdSezWTy8ohn5H9_7vRv3hTgss9E3uam6JMEET8orA3ie_EHtpPNchvPWUTEFUwPGO0cYNGuxI6CuWZJahSBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده، روز دوشنبه، ۲۱ اردیبهشت‌ماه، در بیانیه‌ای رسمی اعلام کرد که پاسخ اخیر تهران به پیشنهاد دیپلماتیک واشنگتن، نه‌تنها از نظر سیاسی غیرقابل‌قبول است، بلکه با استانداردهای لازم برای لغو تحریم‌های مالی و اقتصادی نیز همخوانی ندارد.
این وزارتخانه تاکید کرد که رویکرد فعلی ایران مانع از هرگونه گشایش در مسیر مبادلات بین‌المللی و آزادسازی دارایی‌های بلوکه شده می‌شود و تا زمانی که تعهدات شفافی در حوزه برنامه هسته‌ای ارائه نشود، فشارها بر شبکه مالی این کشور ادامه خواهد یافت.
در همین راستا، اسکات بسنت، وزیر خزانه‌داری دولت دونالد ترامپ، در اکس با بازنشر این بیانیه، موضعی قاطعانه اتخاذ کرد.
او با اشاره به اینکه پاسخ تهران نشان‌دهنده عدم تمایل این کشور به همکاری واقعی است، نوشت: «در حالی که دولت ترامپ با حسن نیت مسیری برای دیپلماسی باز کرد، تهران با پاسخی کاملا غیرقابل‌قبول به میز مذاکره بازگشته است.» بسنت تاکید کرد که وزارت خزانه‌داری، سیاست‌های مالی را به گونه‌ای تنظیم خواهد کرد که جمهوری اسلامی متوجه شود عدم پذیرش توافق، هزینه‌های اقتصادی سنگین و غیرقابل‌جبرانی برای نظام پولی و بانکی این کشور به همراه خواهد داشت. او نوشت: «زمان آن رسیده که تهران متوجه شود هزینه لجاجت، فروپاشی کامل اقتصادی است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75426" target="_blank">📅 23:58 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/brZOHdTnkosFrwDwED0JcEBjEQs9LP-w2cyDpxUVfhGRv5I_VcjqZ5o1dDxbO7vQ8zr41tEUzKd_xWkKWY8BJUy18hlQi2GZK6lTS-9OLXFvGZpQEJq50h8Bb17UjFjtTL7lWYwjK8-V8uFfZgy29THHEwZw7aOHigD21XfTyzPegx13XwoJZpUWERP0NRrwB06yjkQQrAjDR_aXqnODLKGAk9YoQDkewF2mmFkQLqVsyRYsgxEK-4xSfXABM9dWo4NhTd-40C7Zjo9jYzJIQUkElAJ-pv2rqTONKdfUH2XVeblZ0AaXTlBsSRUjstNTDxkZJcNHGPy_Xkm7IpvjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیات جمهوری اسلامی در مذاکرات با آمریکا، دوشنبه ۲۱ اردیبهشت‌ماه در شبکه اجتماعی اکس نوشت نیروهای مسلح جمهوری اسلامی آماده «پاسخگویی درس‌آموز» به هر تجاوزی هستند.
قالیباف نوشت: «استراتژی اشتباه و تصمیم‌های اشتباه همیشه نتیجه اشتباه خواهد داشت. همه دنیا قبلا این را فهمیده‌اند.»
او افزود: «ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75425" target="_blank">📅 22:19 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJ_KE9FzSHft2eQ6HLYup7OlvK_I_jVZWXPvckHieohrv9G6RFHdKvylIZXkcsdYMMUDd5TYk1-TfieG7Pa9ieT1qoWXluuL8Hn7h46a2yPa9fahYVhTaJmBxBecFvQVAz5EgPnP_OwbHEPcmNWkYye6nVLBgx1QwuHKRoJuj6QGsWm4Hn-kwGAWzlMabd9RtH-o-ir8TxK_qQTPYqNNXckw046uDMK-VUpibutQhyKlSCre6NS-va5eXj3t0SDkbsAIp-iKq4GM39IOyZCV3TKOi78JOhAUbhu48ZisNDiP3xZ1wjCvCPPIQy5_Z0Q56fMWP4YRNbHf35xoH1LKPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد دونالد ترامپ روز دوشنبه روز دوشنبه ۲۱ اردیبهشت ۱۴۰۵ با اعضای تیم امنیت ملی خود درباره ادامه جنگ با ایران و احتمال ازسرگیری اقدام نظامی علیه جمهوری اسلامی جلسه برگزار می‌کند.
بر اساس این گزارش، سه مقام آمریکایی گفته‌اند مذاکرات میان تهران و واشنگتن روز یکشنبه به بن‌بست رسیده و همین موضوع گزینه نظامی را دوباره روی میز قرار داده است.
اکسیوس به نقل از مقام‌های آمریکایی نوشت ترامپ همچنان خواهان توافق برای پایان جنگ است، اما رد بسیاری از خواسته‌های آمریکا از سوی ایران و خودداری تهران از دادن امتیاز جدی درباره برنامه هسته‌ای، احتمال اقدام نظامی را افزایش داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75424" target="_blank">📅 22:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ValdL1aFQScCj4b6LwSwsASbYJhIqCuN-8hDIDR2gYFZzyHNKrQW_CpsDg0Y_f8UiiAyzrE-v2kIqAcTzMg-si8ZYe-LdE2Acq5Zn51kwwkcOIL5r00IHVL7h30wOOa5MJstXcQKpbW2qC1HbEZOrrCSaDJq55NxnZtwYtWq_uxAV1xIuIdcNWtA9jLO32vQg7DudOck-DEcg8AVaMerukmZah8_-2X-GJ1Tqj4lgu_Xx0jPqKmYP7N9G01h8LgWgCrYJHQ5uKKnZ6rdVxVEhMTPCbIXQ-BYRPYSIfT1-mNVmYtIL4kKMvir2uLHT0zKVJ5hNPe7zu46K2kli_kTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r8gMt6qhf2-6vUgCrbZn2SzlLpz3pWNJwTAPkjhLGOYkw1MRU--qPlgs7SYUIXWVkl9Tb1P13T_qipdH3XhUanwJN1kWO7CsMN47qLKbaLgiysOF-xwe2rRtt5_VsGkQWbQp5u4fhPEjJaN1--Ug2Q_AMRtN_6cWQfobDqOAmvPkhT-2E6lppnA7_UVkN5_sJ1Keo9NMdEUa6P0lL-CjiG_XPAl9fq7mjwIucOfBL4p5G7wmsLNOwDr9dkCrlykrOfp0XeMIQNTQU3tPNlFc5ZFvlxof5kMT9I809YIV9xp9AMOXEO1aDMVd9dPXwt-PIEcXGDvrpkGcSn4wMoZSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/upH0OA_SXRNvRBeMUR-dwMqVRYPznAqpoqHk68jiaWhjQFo9nACDi55o_VvVa9MwFA3XHw6gVSp7zuwQF_19djBdGXMxHCKaQUFLDO6a7BJ-LXiZ52oBQKS8tK67x2EwVcuzmWT6T7ESnRryXiLRWPxumSWEyN7APLFtEdg9ctjw5dY8XQKenyau1LSmWyvM83yiNtmYyy2sdFkB53wBjc4k3AEwBaQedDTufhuVCxRk_NogeMOqdsVKwKqmWCdmE-hNVLorHAHavAV9zYJtNx8QEzTfKtQZyp8DTQbxVACdwOqotBEYoaO2PWayArsTQbWtKKWeQBrxeoZDxbH_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fkm_uQBs0h8-RemBooZQBhhzSoaEuYmALzfZZmdRpSsvh1asA0F5OLpepR7Nm47RzWEWZIjSxdE6mGqm3myCI4ELDe-Y0dejO3erN08k6Q-7M8U-DJS5RAVpJkx5JgGNXlPkcgQkgP_I078RY8TM6v5Dx94JTBYFmzrdU2jETtS5ZnfXXpMOWSpW7uF4depawiGibQ9quRJ_Zqg0OpfD45wVCOFEOw-_o22yVmbCdlfSQ6CQqRtTm9z903dpv7HKCNkX6XOaenaN6bcfF1ZYlIyrH4bZ6_C2xna198fFb5gNp_rh-E_iBmu-10IZ0_DOtllWJjvVLyDqC39m_8KWLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی حدود ساعت ۱۹:۳۰ به همراه تصاویر بالا:
▪️
وحید الان برام پیغام اومده که من جان فدا هستم و ثبت نام کردم ولی خودم در جریان نیستم
😂
▪️
آقا یه اتفاق جالب افتاده. ظاهرا بعد از هک شدن دیتابیس جانفدا دوستان یه فکر بکر به سرشون زده.
من هیچ وقت در این کمپین ثبت نام نکردم ولی پیام زیر رو برام فرستادن. فکر کنم خودشون به صورت پیش فرض همه رو تو این کمپین عضو کردند، حالا هرکی جرات داره انصراف بده… البته نمیدونم انصراف داره یا نه.
▪️
امروز این پیام برای من اومده در شرایطی که من اصلا ثبت‌نام نکردم.
حتی برای پدر خانمم که فوت شده هم اومده.
▪️
امروز عصر واسه من این پیام اومده
در صورتی که من حتی تا حالا سایتشو هم باز نکردم
حالا یا خودشون دارن روی شماره هایی که از یک سایتی یا صنفی داشتن ثبت نام میکنن، یا اینکه یک ادم [...] واسه من فرم پر کرده یا اینکه مسیج الکی فرستادن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75420" target="_blank">📅 20:53 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
