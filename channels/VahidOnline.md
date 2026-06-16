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
<img src="https://cdn1.telesco.pe/file/ew1M8w4zzRSxpWchzys-bogM6nRwEcOlEem-x61UIQEAKUmHKIM93Y8ii_TOSXPBK6XuyEDOrYaoTTi6oHSUsOwSoL20HkOv5POYwYUtLswKRf9Kvlm_L8Z0JeWIZ7QvtaSc12wvSyJZb-cBjzLqogi0jWYreehgEv8L3iIuvB4zv3xhBAopIW3LxNQWSj3SBdL1EDTDGNTOg8R4MWcwoy7kAbqFs1xihqhxzHCrLL3eqbwg5mwCcZJGQkxlHO8Y4EYj2Dr3_aq3PBL9AkqDgxRT2ipnmGi0pQN8FbgdDNU8MLQpsHnJd0nOjIDs8bznwHJdlQvR5-gW6A2B8qKgdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 21:43:22</div>
<hr>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDykJAPMZ2laKTl1ALSQXaCHNDZVbnM0GfpotzyLLb-DXqyR2QYB_0iOkYBvjoXeUk61766KF6UiNy5AXWXAhZHjuOsGcoCPW9aGDGtWDxGKm28dVvZ8iuUu0D7GnpkwaEo2ZrRj8FwK32hQba3jX7H_tpAd7T1cqb9MQxJi66rL0OjTtYRYnlvCoC5TwruvsLNkaXd6oJVN0B-8pDfkI64__blbIfXzTwfzuERvNyKOAVpumWnoZYu7g1HX-LgBMIWtYjwpPwjn5YuQx1Unyu6iuRTR_U-Vdj6psBuW6D5ULG-PflxYoJ5odqk-E6-Vh3kmTlEAs3pXEAPbqezphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طیبه نظری مکی آبادی، مادر دادخواه مریم آروین و از بازداشت‌شدگان مراسم هفتم خسرو علیکردی در مشهد، از سوی دادگاه انقلاب این شهر به پنج سال زندان محکوم شد.
بر اساس حکمی که در تاریخ ۲۳ خرداد از سوی شعبه اول دادگاه انقلاب مشهد به ریاست قاضی غلامرضا اکبری مقدم صادر و به این شهروند ابلاغ شده، او بابت اتهام «اجتماع و تبانی علیه امنیت کشور» به چهار سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم شده است.
طیبه نظری، مادر وکیل جوان، مریم آروین است که در جریان اعتراضات «زن، زندگی، آزادی» در سال ۱۴۰۱ در سیرجان به دلیل دفاع حقوقی از بازداشت‌شدگان دستگیر و مدتی پس از آزادی موقت، به طرز مشکوکی جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/VahidOnline/76428" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76427">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7Ax0wv2yc2ixnaJJQ1t4ZWB0VFfeaIclWtZsCGSuvZ5wV4jjOLqTB3zdwcb5Qc4gEDadrodfVLeorty7Amn3dqKRpfpGFHHohJXOvotHXN0JUZbA7F0q7y68TZAhY7f-7uKjMpYtqOKOs2pEz9Q1H_Nwg8GGwQ3d0fO7sSEE5UyskMbhSz7a7RdM-Yytmg1Fqx5F8OelafCA9HTfcj8JhC7LFJrNfenKooHG0d_nztBvKYxtvaxwWygVtWWYfrCj2hnXLeoVFt9CqfkU9fm12Rw0nN-JWzbNMToA77VAUbnej-JWMX8XXV4ki7eIDqnhAKuXs66_xVQkuBTaP-bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت جورنال و خبرگزاری رویترز روز سه‌شنبه به شکل جداگانه و به نقل از منابع آگاه گزارش دادند که یادداشت تفاهمی که ایران و آمریکا به آن دست یافته‌اند، به ایران اجازه خواهد داد «بلافاصله» فروش نفت و دیگر فرآورده‌های نفتی خود را آغاز کند.
منابع این دو رسانه گفته‌اند مفاد مربوط به لغو تحریم‌های فروش نفت ایران پس از امضای توافق در همین هفته اجرایی خواهد شد و خدماتی از جمله بانکداری، حمل‌ونقل و بیمه را که برای تسهیل این فروش‌ها لازم هستند، در بر می‌گیرد.
وال‌استریت جورنال به نقل از این افراد گزارش داد که با اجرایی شدن این یادداشت تفاهم، موانع ناشی از تحریم‌ها بر صادرات نفت ایران و خدمات پشتیبان مرتبط با آن برداشته خواهد شد تا امکان انجام این معاملات فراهم شود.
یک مقام آمریکایی نیز در گفت‌وگو با رویترز تأکید کرد که این توافق دارای شروطی مشخص است.
او که به شرط ناشناس ماندن صحبت می‌کرد، گفت: «این یک توافق مبتنی بر عملکرد است. ایران تنها در صورتی می‌تواند از مزایای این یادداشت تفاهم بهره‌مند شود که به تمامی بندهایی که با آن‌ها موافقت کرده پایبند بماند؛ از جمله نداشتن سلاح هسته‌ای، خنثی‌سازی مواد غنی‌شده خود و عدم مداخله در جریان آزاد کشتیرانی در تنگه هرمز.»
یادداشت تفاهم ایران و آمریکا که ۲۴ خرداد به صورت الکترونیکی امضا شد، قرار است روز ۲۹ خرداد در سوئیس با حضور مقام‌های ارشد دو کشور به شکل حضوری نیز امضا شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/VahidOnline/76427" target="_blank">📅 20:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7cMEwmd2cVKqiAhcmNeNamEdXJ3dZur_-ESYwbwiNAD-Ci4UTZiX2chGQI3RGXi9hna5I-sygvRWTruUwhJ1BwRgQPrBqHPVoYFTVFoRnzpxMhd3Vg0e9ANv6DB4PyDEoxzumegJsRGShP8e70H7r9ZqM9cp5mywkQDOb_LkRJ6CPGmKwFL1GjziWZEuKUzuNkhd0B0aLEzD0VgRFXnSvjDYrtg9qbExM7tJh8grYv1D3tQX0EOADQMhwaLAbCY_ERmxVWhpuzA5pn_PeOIv6GHgG_ts2XAQ_Irs4XMadh9tdyF4SJ86TGtmPMxaiUrqrKvJbNgTPaQMmSUNWJ5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی
آن گفته ترامپ
:
لیندزی گراهام، سناتور جمهوری‌خواه آمریکا، در شبکه ایکس نوشت گسترش توافق‌های ابراهیم و ایجاد ثبات و رفاه در خاورمیانه یکی از مهم‌ترین اهداف دونالد ترامپ است و این هدف زمانی محقق می‌شود که جمهوری اسلامی تضعیف شود یا رفتار خود را تغییر دهد.
او افزود که امیدوار است مذاکرات پیش رو برای پایان دادن به برنامه هسته‌ای ایران موفق باشد.
لیندزی گراهام اضافه کرد: «جمهوری اسلامی و نیروهای نیابتی آن به‌شدت تضعیف شده‌اند و توانایی آن‌ها برای رقم زدن رخدادی مشابه هفتم اکتبر دیگر وجود ندارد.»
او ادامه داد: «اگر درگیری با جمهوری اسلامی به گسترش توافق‌های ابراهیم، همگرایی منطقه‌ای و صلح پایدار منجر شود، این نتیجه یکی از موفق‌ترین عملیات‌های نظامی در تاریخ آمریکا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/VahidOnline/76426" target="_blank">📅 18:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ix3AlqYI9_TxAsj9ycTkeWWqFWDRgkl7_UvvH6323IulcXGb6e4ISQ-ynDiLE02nXVzdh70AfG_1jfMdx4A-TQ2kihDQ13zGg1Vev71xlYPjpRL7yH9aL-LGrDiIaevtNL378AfE0jLOOlyqmoPvXK4vCg8Jyk8hLSJkH7IZhf-Gpq5XCCpz-Q0mjdwbUYjMB1Aoj9-Dau3KXSv9e4rOh9jcHgtNNETywr-XJ3AWSvYgjuuZ6jSkq9xxEBbjo1CF5wFn4HIq8juRY7DA9VhqT4D53ojC3hXKN9bGsaWjITDvrNAuhqg0hgKi7ete5cjNYliBALqbeeYtRW-WKip4WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYq89RQ3l4ShdH1rm4jq5Vt-I3m-Y39R5PEc8D1E4bvLO3eVTxtfj3job7tA2mIcaRILo4TjNhJXQbzH43ihxiaNzKU0m-Xwy5soy6sThR9k1m4sR-_z4bA1frXAZ1O8H8wCTCsSgn3uuLqotlMAv4l8UpFnhn_FnHzhuVRfpRKdNBlmW883HYpqs5ZlhVl7HXpSdfX7BD1Nvp6VEkFfVmB6UD_XM8Dl_aH7xz-DGL9LMzsfLkAtsdRBzqgTwAZvcbkteQZmpHKjd3ohnRig8WKiZG1p8GVpeA-8Xveq3-gFMQGkykZY4A3ZuwxxOPBrtkTb9IcyMe2taol4s5lIbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پهلوان سازش ناپذیر
@mananey
مانا نیستانی</div>
<div class="tg-footer">👁️ 207K · <a href="https://t.me/VahidOnline/76424" target="_blank">📅 17:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_XJfkfvvGxZW2td20wTRDh-t5NwUIz4DVsJCwwCHcLRqL3NKWYwBt5Wif6NYIGJ5lta3kKDALzfGalzLnR-G4YdwcXJqnYgnRHG9EcBOztPLhAHY9lacPFcpJ-mVL7AqRvyWjIzZ6W4fFpmcs8TBcdvyPz2AIyVTNbpZ9RDcuv7mvalxCx1rP0ajvgcjVC0xd4BkKKAvyNtAyZIqJMvyr1SD7O0vsjvnSp0DGk1b57VTxhVpdUqwdEeeL2Lo-BYb6wqXQFGXQSQFWumcobhAHpFt2p7nVjGTYbLDcuoFcl0fL8KQqWJucZDOpxy2XDcqmeOjzQemEqAGwwYDZE7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r9TJ9it7clITcLCn8jRL81Nh3vu5NvsfFrjXaCwThlXuzFpj0jrriRpSj9NJ_8eOgF4iA7QgqzTVeKU-fERJaEkK80y1tfQ64Cx6xlwZI5YkIFn0Oc-TbW2jf9FXDgujIyV67KD4N_ZGtXpfY1D0_TZnjf1jGAPRSgbz68emI-9HBW16tjU6iXNFBrGtDWc5Dbbro3kqlUxyviEg2DJ1yMTmIzZoPWzmz7RTJ_YGpNJycukP-zPL2qf8nir9U31_tI69nWQ7eNkgLqAx6fwUsX9CsTb6FDpDfeUc03Rn1Eo2ZZKrpLPbmqkBTkLxbpO7MCH9HSdCHGRVkyDblPOmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIqFzZd6I7f4MICl5OKiUHTIFTO8dPwYdQG0tD8MJP3kbDrnLEuYsXOEu0Np0I1n7y80b_OjP3YTUtdJ4Dz8MDilvepfq1GKAgoX5jMkGE1-9ScJIOBXc5MTsAX6flt5g3VwD596HUR80aAB9QzpzK4wYnE4e42FnUpxdaC2WvOP0upgTA19kMNEQJG5hThB7ZcxRMT_hXYiPVb0XCiSv9vghmkgtki6WRn8zbnNBnIztkE9uXL8mvpR21f_hU87vhYe18qIN0Y9a8pY1ejyvnPwFtWHHoaizNr3PhHmp4JJxt5IC0SqDmKVujjPFCYysLUPhl1lTLtVc4Cu4i8Ckw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=VDPeqIVbqP7Cu1-oBcVd1maNGpPlKuiataqrtL28hiCvOp_1EV7lLsmrTbNNgHkQq3rT_NGUfnKzP0Qx1x5ccQm65wu2vgh4NHlnJXkgz2so2t_uPjpAXZ0Wf_Vh7pSlFe4qWnMvFUqR53jhwIJt4SLgjxVA16xwcjKOKu-VYRRUouK2KUbRct8x4epmZss530cugFpJylYeCq_B5PrK-4p9GMbzpcmFCsEAOWIj-JAR8td8SU1yfxbaOKOGDlVmQhMiJthvq82G9DMjIa0diYY5LzC3j4uX44ECodakNITIcCRf82jXtoo005B4L5XVn7kgIQ4SiyUd0aqP-cXptA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=VDPeqIVbqP7Cu1-oBcVd1maNGpPlKuiataqrtL28hiCvOp_1EV7lLsmrTbNNgHkQq3rT_NGUfnKzP0Qx1x5ccQm65wu2vgh4NHlnJXkgz2so2t_uPjpAXZ0Wf_Vh7pSlFe4qWnMvFUqR53jhwIJt4SLgjxVA16xwcjKOKu-VYRRUouK2KUbRct8x4epmZss530cugFpJylYeCq_B5PrK-4p9GMbzpcmFCsEAOWIj-JAR8td8SU1yfxbaOKOGDlVmQhMiJthvq82G9DMjIa0diYY5LzC3j4uX44ECodakNITIcCRf82jXtoo005B4L5XVn7kgIQ4SiyUd0aqP-cXptA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ که پیش‌تر در پیام‌هایی خطاب به ایرانیان از «کمک در راه است» سخن گفته بود، اکنون در گفت‌وگو با مقام‌های قطر، کشته‌شدن معترضان را عمدتا به «گروه‌های قبلی» در جمهوری اسلامی نسبت می‌دهد و میان بخش‌های مختلف رژیم مرزبندی تازه‌ای می‌سازد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76416" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db862b726.mp4?token=smJOdSNvA0RAcnen1MQpKsa-gXMj2P4CQ9lqVQDnERsjMIWanxbZDZjvS46bSj_iOSQvj3qghJDk2waasq0lsf5oAAIc3Ol6bdG6KS7jK-lQCQmU8usTNDUGwWlvFKGmCTWfpQZyRSYhfbAv0rqfcpy_36DJfYTsaa85EN2hxUba66HktcTeKnkU-AsId3XjUdNT5OTCcZ5CAHoWrcJwibUQj8kRTOc2XCKZv8B9gdXVvwvnn6NpPBkGOI_NTkrO-1GVSHGWgCLRGyyk0KG0FWUWFxOxfXQbHLYBvmL8HTNwwIrGfQOxxExAJF8dXdPtT_iL7fE1plpDer4V8o3xfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db862b726.mp4?token=smJOdSNvA0RAcnen1MQpKsa-gXMj2P4CQ9lqVQDnERsjMIWanxbZDZjvS46bSj_iOSQvj3qghJDk2waasq0lsf5oAAIc3Ol6bdG6KS7jK-lQCQmU8usTNDUGwWlvFKGmCTWfpQZyRSYhfbAv0rqfcpy_36DJfYTsaa85EN2hxUba66HktcTeKnkU-AsId3XjUdNT5OTCcZ5CAHoWrcJwibUQj8kRTOc2XCKZv8B9gdXVvwvnn6NpPBkGOI_NTkrO-1GVSHGWgCLRGyyk0KG0FWUWFxOxfXQbHLYBvmL8HTNwwIrGfQOxxExAJF8dXdPtT_iL7fE1plpDer4V8o3xfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حاشیه نشست سران گروه هفت (G7) در اویان فرانسه و در دیدار با امیر قطر، از رویکرد نظامی بنیامین نتانیاهو در قبال لبنان انتقاد کرد.
ترامپ با اشاره به حمله هوایی اسرائیل به بیروت، درست دو ساعت پیش از امضای توافق آتش‌بس با جمهوری اسلامی ایران، آن را «کور و بی‌هدف» خواند و گفت: «به آن‌ها فهماندم که اصلا از این کار راضی نیستم. برای کشتن یک نفر لازم نیست یک آپارتمان را با خاک یکسان کنید؛ آدم‌های زیادی آنجا هستند که همه‌شان حزب‌الله نیستند.»
رئیس‌جمهوری آمریکا با بیان اینکه اسرائیل زمان زیادی است که با حزب‌الله می‌جنگد و افراد زیادی کشته می‌شوند، پیشنهاد داد که کنترل این گروه به سوریه واگذار شود.
ترامپ با تمجید از عملکرد احمد الشرع، رئیس‌جمهوری سوریه در ساماندهی سریع این کشور گفت: «او با مشارکت من و اردوغان روی کار آمد. او از حزب‌الله خوشش نمی‌آید و این کار را بهتر انجام می‌دهد؛ اگر اسرائیل نمی‌تواند بدون کشتن دیگران کار را تمام کند، سوریه این کار را خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 202K · <a href="https://t.me/VahidOnline/76415" target="_blank">📅 16:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WphnJBdYa_C6BIgepgrpbhA2oWNOmNIqIfJ7bU3pqJNA8OWI2xSdId7AjBjAR2LXdIsrVpFdgkPDjfLKQzflXeUFeRpyBesCmtUvVeYVUh5iyzP6z1cIaUo1GX2GqcVHTpXshNJyujEiGcqQO-6SlLsb7cRi1JFvfmdmNntgr-kkJpEfy9ljZSlnYS6gsTGFOmyazFAOeI8lqhq-1r3mKB0wYDKPv6yhzAMFH3sAr-B7eSgjxCiHlnvmMd76wJ760MQLMA0aKyJdUqpsJFTedxGaZ54BrFD7FmowDMLdJSSsrGfFT6VodVcIrE7m-hyJ6CPMQGXtT7zlqzLIV9vBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به پرسشی درباره متحدان او که نسبت به چارچوب تفاهم با جمهوری اسلامی تردید دارند، از جمله لیندزی گراهام، سناتور جمهوری‌خواه، با لحنی طنزآمیز گفت: «لیندزی تردید دارد؟ باید با او صحبت کنم؛ دچار دردسر بزرگی می‌شود.»
ترامپ سپس تلاش کرد نگرانی‌ها در میان هم‌حزبی‌های خود را کم‌اهمیت جلوه دهد و گفت گراهام «آدم خوبی» است و مشکلی با این توافق ندارد.
او افزود: «این توافق یک موضوع مهم را به‌خوبی پوشش می‌دهد. ما بابت آن هیچ پولی پرداخت نمی‌کنیم.»
رییس‌جمهوری آمریکا ادامه داد: «بازارها اکنون نسبت به زمانی که کار را آغاز کردیم در سطح بالاتری قرار دارند.»
ترامپ گفت: «اختلاف فقط بر سر یک موضوع است؛ این‌که ایران هرگز سلاح هسته‌ای نخواهد داشت؛ هرگز، هرگز و هرگز.» او افزود: «بقیه مسائل اهمیتی ندارند.»
@
VahidOOnLine
آپدیت:
توییت گراهام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/76414" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fr23_bTjd7kkHtnzRj_zcGSOY3rvVq4agW4w10rW9dn68LPGNBRef-3ocXK_QJHPsgo5dolaCV78saNDZ-4dHUF59AMqYG5TF2SqNH4UN0P2JijyrHARagfCQ8-n8E4UpejKQrDfQ2bQ4d7P3tgWDFA363r6N4FfvBeTsCgKTU1zqyC76nmI3Hw_pqnu24RCsjUXQBHxGR81YTzBRqargw1cOfiR8PYUeYDNC23DT7bS5gaaeiyMrS8QFIgOuMlW46bSXHH1Kv8nK1wEconx58m-zCEZZkMY3rK9wC75dfqlbl9IqCqf73BGQkXTyHmUJ3ViB03vn3idxNgpION0Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m0hxoIR69WcfAYsmtbiLnbNHqYbSokzfyuvNyClMUbZHTVot76VuwnE0H-Bq2zq9DWXNUCQQKYfKNjcF8pf0jvTKXXfxYrilx8HrzaCsMYfjY5L3DvtOlQBPwg_ba9rZeXxdmDKrcaLWiPeTfrymdLb8qBH4J8gXSk6HUuAvQ1AXZs8g9iMJwNKbWExxaob-vTT8J35Qv6pHV04UVhXLtQXo7DaIDR5VF6eu02GaOdKmXPfjyEKGwBOzNsMi7mxaz2UBv5cG-nbVOe_DPOlOWBZ08WrvAJD0bNQfTTqTXqfYxOrV-xpl0EWVQsr1gwaexu3xKj0f44xMK2PEqYJ0Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی درباره دو پست قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/VahidOnline/76412" target="_blank">📅 16:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4cA7U2LhbFNBpvubJvazzDaGkaiIeMD-B6syqrf6jpe-5ztv5LMeYuSfzK5T_k3UiQvT7YfSR2AStRAbjswEoynYCTOFzoYdRFF0x-7Hvmz-RK9UTAqVNqd1vCfRC9owOqB2ZF3w9U5rSGPzSLUuup6-pDWoV8gh2J08c7WU5Uee1YYjau0EeyVynjTTBaMyv4C6JIC9gT93rexikC8JKHeg3KttVwZhNibF2Xbb_0xk9H0HJC-q6aPqoAiMX313CX1Gvj0Er1hmjCLTgYEvzWfUpmQiyCmwATTOgjp6Ibek9pFpt54sn0wD9QwqbksSXFX5VgWsO2zcV6bLRmqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز سه‌شنبه اعلام کرد توافق صلح با ایران را برای «بررسی» به کنگره آمریکا می‌فرستد.
او در جریان دیدار با محمد بن زاید آل نهیان، رئیس امارات متحده عربی، در حاشیه نشست گروه ۷ در فرانسه به خبرنگاران گفت: «هرگز به فرستادن آن فکر نکرده بودم، حتی یک بار هم به آن فکر نکرده بودم، اما این کار را خواهم کرد. آن را به کنگره می‌فرستم. از این ایده خوشم می‌آید.»
برخی قانون‌گذاران جمهوری‌خواه پیش‌تر خواستار بررسی متن این توافق شده بودند.
آقای ترامپ همچنین وعده داد که متن توافق با ایران را «ظرف یکی دو روز آینده» به‌صورت عمومی منتشر خواهد کرد و حتی این احتمال را مطرح کرد که کل سند را در برابر دوربین‌ها قرائت کند.
او گفت که منتظر فراهم شدن یک «فضای رسمی» برای انتشار عمومی این متن است.
رئیس‌جمهور آمریکا اعلام کرد: «دوست دارم ابتدا یک چارچوب رسمی برای این کار فراهم شود، اما هیچ مشکلی با انتشار آن ندارم؛ این یک سند عالی است.»
او در ادامه افزود: «محتوای آن این است: ایران هرگز سلاح هسته‌ای نخواهد داشت.»
ترامپ درباره مرحله بعدی مذاکرات با ایران که برای آن مهلتی ۶۰ روزه تعیین شده است، گفت: «فکر می‌کنم این روند خیلی سریع پیش خواهد رفت.»
او افزود: «ایران می‌خواهد این موضوع را نهایی کند. آن‌ها باید به فعالیت‌های عادی خود بازگردند و روابط اکنون عادی‌سازی شده است؛ بنابراین فکر می‌کنم این روند خیلی سریع پیش خواهد رفت.»
ترامپ در ادامه گفت: «ممکن است سریع‌تر پیش برود، ممکن است هم زمان بیشتری طول بکشد، اما می‌تواند خیلی سریع انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 188K · <a href="https://t.me/VahidOnline/76411" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BgjpBR5FPNslkpso2PXePYXO4JblN4DysYp0obFR2sIDheUQShSE5ig-_aj6pDiXpKr11BoG3BSAgES_TA7VJTTiFtXQKsO0PfELahxlFKDbdzaQgtQCchZbCgFtqJhlpu9QLIyveqIovCxfIUxeq4-rUPhU9zlIfwhBVa4c3Y1w7EfehnGyXtY_Kmx6veqBzo4aAc-RsSre4eH1ZL8mhIJOpxwdzStPxyFbA8EFa1gMedpIYqi9PnwwT7aib9JwEMOPO2xTqKNPEV5vwX-itYx1OaTU4DICUusqqDPbNJZdlkDt4r1I-2r8UH0s4jp-95HFBIFA0balGZj9Ei9PAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که روز سه‌شنبه ۲۶ خرداد دو نفر دیگر از معترضان دی‌ماه پارسال در شاهرود اعدام شدند.
خبرگزاری میزان، اسامی افراد اعدام‌شده را جواد زمانی و ابوالفضل ساعدی اعلام و گفته است که آن‌ها به اتهام «محاربه» و «افساد فی‌الارض» اعدام شدند.
این نخستین مورد از اعدام معترضان در ایران پس از اعلام توافق تهران و واشینگتن برای پایان دادن به جنگ ۴۰ روزه است.
در بیانیه رسمی قوه قضائیه، از قول محمدصادق اکبری رئیس دادگستری استان سمنان ادعا شده است که افراد اعدام‌شده «اقدام به تخریب و آتش‌زدن اموال عمومی و خصوصی، حمل و استفاده از سلاح سرد و گرم و اخلال در نظم و امنیت عمومی، اجتماع و تبانی علیه امنیت کشور و سایر اقدامات مجرمانه» در شهر شاهرود کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/76410" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/na4-mC3FoEv45PChInOVfH7pMt-72IfWrxC4LMB8JPwJUAyu923qisr8q4KDyZvTYYGnTZQ_1o4hyqRZB6hPmwAUJHI_WMeX0TbLlowqMw7IBBxRpD3AEVytyia0IncXV5cOJM4Zw64WkmsUCq7hCIwcu3RfJ-fEj61_K6XxPTzhQHYVi8v_d1Hd2rMRzjP5j71VA2-CiIouH80fju7oikDNltg_lqVwPciIHwSd5eQGTo6tskhnf9scIRSIGZ4vlJq5IEt26DCrjAvOAop863gB8zsyKLXxlwSIFrGANWdKwkgjqfen5M9o-HPMKRsRw4Yo8F0TpB-MqIDKdgvGyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VbecubBQaOkneM6eAtEr0C7LAamz4nQY3lMrF4iM9PdQDALplc-SJRdkQyZ_LECQnsM31eS6Tw6KD-06V7y4Y-QUgR3CuK-VnHOkzAJXR0PoLzaGs1iuzOcNrWXh21nlbKY0-hYCV8EQwJpfoBKxEFI30bFaIt-Oz1zS1tOWfhVz-vUzYzCzVX2_gcb0JMKtpXJVe8BrpA9D53GLIJnFMki-0NigsHGTjZW09YyAbRWs3UixfSLQINGoApMVnZIymfu_yND1fCjHVbztYlQF3lnY2R-vphFnwcjM4Am93yXuKOIUKt8QufDRLiF6AxgkUBiqyq510PE9Z2w1OUk7wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسابقه نخست تیم ایران در جام جهانی ۲۰۲۶ مقابل تیم نیوزیلند با نتیجه ۲-۲ پایان یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76408" target="_blank">📅 06:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=S1tylYFG-hgar4kw6OP38GiNqYg9zfjxUJ_domOKnwZP9n1yvzX5UN_KyfjG17iSpMCEruUoUpsDqA94gQpBiuiZWQEk_Sy-6-6B3kzEN085lcAiqhSZgTCN6mfwRWuX6L-o81i8S2IYqE_MNUyYwTay2mXsy9NzvXbo__NmEZUYtreBjPPj01Yuqg0Vuj1cVpO6bEGf2X4077HkNtf4GmvWCvobo9tZ_U37cPt6aTa7D-lXaMpRj2EoXhONmurioWNnwKm__ALsDdNIN3v_VnR0tFjspyJfjFYbQDMqq839mYO8W1dC4y1Q8VczfZ3NGWtqxFJ3wXD2jSWvQ8pqzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=S1tylYFG-hgar4kw6OP38GiNqYg9zfjxUJ_domOKnwZP9n1yvzX5UN_KyfjG17iSpMCEruUoUpsDqA94gQpBiuiZWQEk_Sy-6-6B3kzEN085lcAiqhSZgTCN6mfwRWuX6L-o81i8S2IYqE_MNUyYwTay2mXsy9NzvXbo__NmEZUYtreBjPPj01Yuqg0Vuj1cVpO6bEGf2X4077HkNtf4GmvWCvobo9tZ_U37cPt6aTa7D-lXaMpRj2EoXhONmurioWNnwKm__ALsDdNIN3v_VnR0tFjspyJfjFYbQDMqq839mYO8W1dC4y1Q8VczfZ3NGWtqxFJ3wXD2jSWvQ8pqzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس معاون رئیس‌جمهور آمریکا ویدیویی منتشر کرده:
رئیس جمهور از روز اول صریحاً گفته است: ایران هرگز سلاح هسته‌ای نخواهد داشت.
بار دیگر، تلاش‌های رئیس جمهور ترامپ برای برقراری صلح، علیرغم تلاش‌های بی‌شمار افرادی که از آمریکا و رئیس جمهور ترامپ متنفرند، برای مردم آمریکا نتیجه داده است.
JDVance
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76407" target="_blank">📅 03:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ef6Em01JhumiRMKDA_xTvEklKgVzWKDjkNzL3fP5hAR4gI-HOzm4Yl5uHeAxnlOfWEupDIOzhiEGen2Fp4IdHHN2Q0UOGJ8lfCCmuva2dEv6vpyppqF7jn3VXPFCm3M3eZaFt-mUb8TYjjk80wPbo1TKlotw7mdHQ_0jiZ34d3MYzlE6rBaGabrTR3GYu8C9C63K391AJw-ITkQa3LudD8xG_fk8KtLeYvgLrXDPFtslsS___0SASAG3drw3_FXA4IWU3eARGb69kPS_tOSKWKZWmBjttyCY6vJTJSnuuEqMLwH3TLJYBgmT32cTPhJKyUEeWsU2oHqHRjfDsVy7ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه و توضیح ماشین:
ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین، داستانی که می‌گوید آمریکا ۳۰۰ میلیون دلار به ایران پرداخت می‌کند، خبر جعلی است که دموکرات‌های احمق منتشر کرده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
(عبارت «Dumocrats» ترکیبی تحقیرآمیز از
Dumb
و
Democrats
است؛ یعنی چیزی مثل «دموکرات‌های احمق»)
realDonaldTrump
البته حرف از سیصد «میلیارد» دلار بود نه میلیون. ترامپ هم پرداخت از سوی آمریکا رو تکذیب کرده ولی
ونس هم نگفته بود که آمریکا قراره بپردازه
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/76406" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx77_MFz5TGOdoRSZTvQWgtpNSWaYym_3CzBXdqs9YXUij3PMcskL6pc3IdnTi4YvQqe5Nw6xVpsu3tjrBfO7oAjW74dN3dKBY0LgXY_tZp95owoj3HNoOuF4hpqUsvkPYsxXp2JXOlA2mJDDGX2NUs3xGDvbg5MeKuiIuT7hO31rFpSdNS-BfcUoLHfXBbNWbLcXgsXd-yKOdHjd3PFBu0HPUKzBBH4D0O5kODtPW-cd4k353sF0HSRgDPWeTivTUI3WdL-g7ZIwkq9BZlT3XikT7aYKiWwjctwWz-E5JsJ0rGfwmzWGUzTv55NHLHEHG_K9rDiOwnwtbEXb5UnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه منبع مطلع که با خبرنگار اکسیوس گفتگو کرده‌اند، می‌گویند: جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، به دونالد ترامپ و دیگر مقام‌های ارشد دولت گفته است اطلاعاتی که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده‌اند، درباره آمادگی ایران برای ارایه امتیازهایی که واشینگتن در یک توافق نهایی هسته‌ای میان دو کشور خواستار آن است، تردید‌های جدی ایجاد کرده است.
براساس این گزارش، رتکلیف تنها فردی نیست که در تیم ترامپ دچار تردید است. مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ، نیز در نشست‌های داخلی نگرانی‌ها و پرسش‌هایی درباره این توافق مطرح کرده‌اند.
در مقابل، جی‌دی ونس، معاون رئیس‌جمهوری، و استیو ویتکاف و جرد کوشنر، نمایندگان آمریکا، از توافق حمایت کرده‌اند.
به گفته دو منبع، ترامپ و تیمش اطلاعاتی را بررسی کردند که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده بودند و نشان می‌داد شیوه‌ای که مقام‌های جمهوری اسلامی در گفت‌وگوهای داخلی خود درباره توافق صحبت می‌کنند، با آنچه به میانجی‌ها و آمریکا گفته‌اند، همخوانی ندارد.
به گفته دو منبع، رتکلیف و روبیو اعلام کردند که بر اساس همین اطلاعات، نسبت به این‌که حکومت ایران با اقدام‌های هسته‌ای مورد نظر آمریکا موافقت کند، تردید دارند.
یکی از منابع مطلع گفت: «اطلاعات موجود نشان می‌دهد نیت‌های ایران با تعهداتی که در چارچوب توافق پذیرفته، همخوانی ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76405" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/luSoKwqbBJDLFfKOQU_CrHhmlyHkYZmnY4eDfaJSKm0qymV96G15juJh_LYfep7lmiOwPWr-NlS6p3rKakkC2V3IwxTOZTUneh_lFnwRSiwGmDt6PgxZn-ppB50k8ujLKlW40gppHymUgTUD3IeaPdSIFhxuimCp_vIaGsPtMgSNKsEY1bXIxBZYAy16tYJFH1mZRTBd8UyzeU1u-EE-CGSgP01UO0Nt_XZCxBdrobUlODEBgNI7elyFcyvdvdfgyBTHgK2xb3Jn16iGQEf28E_Ta8pAJ48h5U3gIJGjYlQ95WMHtpYYl6cQQ6h25wGAXRnD1pMAZdTbi4TKceCPrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cqx9F8MzgW_uIib0LQ2t9uYt-_5SRj4zOzh_Qvzk7qeYEgc1axODg-YbErig5JvsWvMbyMbxJoGu6hgkKDnvW0DtqfgK_PB1GeoAw9bXodIQRZVkpH8C0_vepx4rQ0g5SfJs_abrjulSt-s6VLNmwqN2TT0eos4ERZ2zpUjoUWewnYBIqJ3uhuzq9aQ_lhB-i_K3c1C5RTNshvsTyf4dz0DL11gLJGyCO2l-yrhuATfN-rbFrdi9Dn4WTfHBTMoepVa6T57_wiTPJGLMj-n-sc2Soxx5TJPoKFYIu7zDsOgV7WzKQsTekBYHoChAas0DzIr0IRB54CUf-ZzylzrE1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، روز دوشنبه در گفتگو با «سی‌ان‌ان» اعلام کرد که یادداشت تفاهم میان آمریکا و ایران سندی بسیار کلی و در حدود «یک صفحه و نیم» است.
ونس با اشاره به اینکه این متن تنها یک چارچوب کلان را تعیین می‌کند، تاکید کرد که جزئیات مربوط به موضوعات مختلف باید در طول مرحله مذاکرات فنی آینده مشخص و حل‌وفصل شوند.
به گفته او، این تفاهم‌نامه ساختاری را ایجاد می‌کند که بر اساس آن، ایرانی‌ها در صورت پایبندی به تعهدات خود، از مزایای این توافق بهره‌مند خواهند شد.
معاون رئیس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت که در همان «بند اول» این سند، انتظار واشنگتن مبنی بر تعهد ایران به «صلح و ثبات منطقه‌ای» به صراحت مطرح شده است.
او تصریح کرد که بر اساس این بند، همان‌طور که ایالات متحده به صلح متعهد است، تهران نیز متعهد می‌شود که تامین مالی سازمان‌های تروریستی خشن و دامن زدن به بی‌ثباتی در منطقه را به طور کامل متوقف کند.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، در گفتگو با «سی‌ان‌ان» ضمن تکذیب گزارش‌های مربوط به آزادسازی زودهنگام اموال ایران گفت: «تا این لحظه حتی یک دلار از دارایی‌های مسدود شده ایران آزاد نشده و هیچ‌گونه کاهش تحریمی از سوی ایالات متحده یا شرکای ما در خلیج‌فارس صورت نگرفته است.»
ونس با اشاره به گزارش‌های نادرست در این زمینه افزود: «تندروها و برخی عناصر در داخل ساختار سیاسی ایران، برای متقاعد کردن افکار عمومی خود، دستاوردهای تهران از این توافق را بزرگ‌نمایی می‌کنند، بدون اینکه به تعهداتی که ایران برای کسب این امتیازات باید به آن‌ها تن بدهد، اشاره‌ای کنند.»
معاون رئیس‌جمهوری آمریکا با تاکید بر اینکه این توافق در صورت اجرا شامل یک بسته کاهش تحریمی بسیار بزرگ برای مردم ایران خواهد بود، تصریح کرد: «این تفاهم‌نامه نحوه تعامل ایران با جهان و منطقه را به طور اساسی تغییر می‌دهد، اما تهران تنها زمانی از این مزایا بهره‌مند خواهد شد که به تمامی تعهدات خود عمل کند.»
او در پایان به مخاطبان توصیه کرد که نسبت به بیانیه‌های تبلیغاتی و پروپاگاندای حکومت ایران بدبین باشند و تاکید کرد که بهره‌مندی از این فرصت بزرگ، کاملا به پایبندی عملی ایران به وعده‌هایش بستگی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76403" target="_blank">📅 01:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TJ88KSp9RhT2StkmfAHkuzyN4ZgFNS6lsVqhf5cQ6KeMH_oNPrPvozWFG7yhw06t3Y6OxU7WUu7ewPIpNDuIv-_2aYyiWIIgcBfBejwysIjt48H_UztbndhdQIyUJo-ZIgVhnbM_JvVCCdr2qvWgAbAejUdzEgBdsvRBHEKBhhzILOVY928dX7nDITQMk_xxr0cixcw1Zc84VL28Nz78luwLwuQGdgwXgpv86Kx_nI_xNfAb4t8_IsCyaHeQcGX9E6SmnOjrtOmfwgudmVRnDMsJPt1gluK9zqpDo8GRLV3wWKEiuzUAmmdzHW67zEIo87LEWw5eTXFvWgOZ7A-LDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر:  منابع محلی از شنیده شدن صدای انفجارهایی در مناطق جنوبی جزیره قشم و تنگه هرمز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76402" target="_blank">📅 00:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMVVGf5fymJHrOlPl7J6YerdAHEIMM56G0bkK4JexeDX6A19cs7quUNx6zHC7wHFHXhuq55z0gUWBbiD46pJAd46YyQnDFCMFPlQMaFWYHp0N4TlhVDUvAZCVBmuB6bIQZPPn0Rvfk3L59cinTB3pyWZcC6s4pFvXxWUGQBzPGWczvonx1KOcSQGHkDp0S4bmUkxGIP9N5joWcDyNikSJdsC4Zv-Y4JFvEhtjmnESQ1NhgLtJ-jqm-IeRxQ5ZHPyedy3BttV6quK_yAIgzVJMP0Ae-UWselEhBcmpjjuXP2Kn-ytuFAhG9GJnBNOJCe6p6CFIWEHJWGwn2DMhqw3VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vyBa2oy0YauJIMiAR7-Rqb6zk1FytHw0LgJlERDm-vV38OM-GKVNsGlMfekku4q5UB7bW4isDLNdaBaFGSOB_9jq1buf_biCj8Tb8WErcsRSbI6tFDazrvpKu5USZEcCoxcanf73FM28R4NR2UWQt3Za0WHPUQJResderPvrH6sUGWo-VSHlyWtifb2lTg0sOQFmDjC3WCAj0uzmMr_c9-Ufc1xAOes6ONy0TUEwV3VLCdbkJRcgzl_rPzWB_10QM8Oz-2S8_JGBsbbbkEgPnOdcyLWCpxJWBOdSQ74Pam7LqOb9SN4FMc23KuzMNHkBVX0bMqgu09rCbDnq8GLllQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت: رفع محاصره دریایی عملیاتی شد و ۳ نفتکش و ۲ کشتی حامل کالای اساسی جمهوری اسلامی از محاصره دریایی عبور کردند.
پیش‌تر ‌‌ارتش آمریکا در یک یادداشت هشدار اعلام کرد که محاصره بنادر ایران تا زمان تکمیل یک توافق آتش‌بس با این کشور که برای ۱۹ ژوئن (۲۹ خرداد) برنامه‌ریزی شده است، همچنان برقرار است.
@
VahidOOnLine
بر اساس گزارش فارس، دیگر خبرگزاری وابسته به سپاه، یک نفتکش غول‌پیکر ایرانی (VLCC) به همراه یک کشتی حامل نهاده‌های دامی با گذر از منطقه محاصره در آب‌های آزاد به سمت بنادر ایران حرکت کرده‌اند؛ هم‌زمان یک نفتکش دیگر نیز با عبور از دریای عمان و خط محاصره، مسیر خود را به سمت مقصد صادراتی پیش گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76400" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی نیم‌ساعت پیش:
صدای انفجار سیریک ولی با فاصله تقریبا دور
سلام وحید
۲۳:۵۷ دوشنبه ۲۵ خرداد قشم
خودم یه انفجار و موج رو حس کردم، اما بچه‌ها میگفتن دوتا بوده و قبلش هم حس شده، جایی که من هستم نزدیک تنگه است، شاید از روی دریا بوده
۰۰:۰۴ سه‌شنبه ۲۶ خرداد
مجدد دوبار احساس شد
سلام وحید خوبی
ساعت ۱۲ و ۵ دقیقه سمت سیریک صدای انفجار از سمت دریا اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76399" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HntGbkvcHHjD7eRDd-Z3JQprMS7KX7DgF5CKmevhAe9kZDicP3YUVcfmLTCiusQnV0MKnO1lrSeRS8lX3T8nnDcjc--vn2hDzG4Fb-B6Tyi2rXe5mDgZXIXuWYVd4RVSsXJqjSxrwWxFl23EwQdXBugbDrZgBQarfuLGSaYlG8CqLTE_aPu63z6viEKCmK6QZqUyC0ZRTL-EhBNYurJ2eEZKXPavqSrKJMqVQVVNrx_wxptsVo0QLbMrMm67YKQqmRaaaqxdtX5ualO0w7sAeoJgoYhzXUWINYiRBkxGOQENIOVF8G96a5EN693eJ-XzhAjoNbbC4Blp-FqwdROXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/759110416d.mp4?token=hOFT54LFwXtZLI7TKt_zubDAkS2NqorkgzHwsQZJmIs7_KP6eJKamj-yCR7OdSB9DYAcS7pi9K9uaROfUIE4PnUIFaF9FPivpzQ8mJxL2ZEmRwqyONeAzICD850Za7xcr4qNOlGydT1IJvoWcxoESHEfNKYXP3MvhLhnXYE7cSo_KhYqO257PN2UDAQs9PLy-lZbMeeu9zDqfbZVAQwkjBsPIHC0GMuamQxdN2NuTNd7domYZZrWt0UGy6Uv6jqy1ySAWfiVEKpRUSOox44CvGQuAx2P2nbyI-2blQCUNxXTxXKzPMR1k9ziWFEEqQad6XJnc6JuWx2gR3cA-kZTfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/759110416d.mp4?token=hOFT54LFwXtZLI7TKt_zubDAkS2NqorkgzHwsQZJmIs7_KP6eJKamj-yCR7OdSB9DYAcS7pi9K9uaROfUIE4PnUIFaF9FPivpzQ8mJxL2ZEmRwqyONeAzICD850Za7xcr4qNOlGydT1IJvoWcxoESHEfNKYXP3MvhLhnXYE7cSo_KhYqO257PN2UDAQs9PLy-lZbMeeu9zDqfbZVAQwkjBsPIHC0GMuamQxdN2NuTNd7domYZZrWt0UGy6Uv6jqy1ySAWfiVEKpRUSOox44CvGQuAx2P2nbyI-2blQCUNxXTxXKzPMR1k9ziWFEEqQad6XJnc6JuWx2gR3cA-kZTfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه نیروی هوایی ادواردز آمریکا اعلام کرد یک بمب‌افکن بی-۵۲ روز دوشنبه ۲۵ خردادماه در ایالت کالیفرنیا سقوط کرده است.
بر اساس بیانیه منتشرشده از سوی این پایگاه، هواپیما «اندکی پس از برخاستن» از باند فرودگاه پایگاه ادواردز و در ساعت ۱۱:۲۰ صبح به وقت محلی دچار سانحه شد.
در این بیانیه آمده است: «تیم‌های امدادی بلافاصله به محل حادثه اعزام شدند و عملیات امداد و بررسی همچنان ادامه دارد.»
مقام‌های آمریکایی تاکنون جزئیاتی درباره علت سقوط، سرنوشت خدمه یا میزان خسارات احتمالی منتشر نکرده‌اند.
«بی-۵۲ استراتوفورترس» یکی از مهم‌ترین بمب‌افکن‌های دوربرد نیروی هوایی آمریکا است که از دهه ۱۹۵۰ در خدمت ارتش این کشور قرار دارد و توانایی حمل تسلیحات متعارف و هسته‌ای را دارد.
@
VahidOOnLine
آپدیت:
هر هشت سرنشین آن جان باختند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76396" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10d585b107.mp4?token=ev3SdQ5_x6jv5gOiQV-SIWvIFapMbbbmSk-0_kmw2pUpaj4txfHIIwkWE37LJCHkwH0Zt25cEkNMPAkvrvBCOgog8cvnY2Cl0VHtorHjPbpIZDeVBg6Z6aJEIy_0pWFMO3MoDqR5u2iCLmQLeMIxL-5ILxIVujs2MUydViE-TDD1Ba6DxjtTC3VQuK13J02zKO4Dk0redFflRwv12pbLyqRCOtAUoEva0pSc5GN2SE8ad8XN0YckII5W5QJNmpbdxWtSpFyl5Hi7apm2F4YFO5eLmyxyA7ty7Nr06y9LCJUJpjUEY3AEBA8y7auF-DH6TXTEYP6FwcNEyghM9eKK2jjJC032Gf7Yo0BK2EKyT7vyAAUO6mL_oXXeZ38UkKrlI8TYmfu4ngKwocfu58E06Bl7LxmDPldpwNKGbea1ql9k8ggmFraQkyU3FgrBEC7IIes4N94cW7MA8_n0HVtiASWWOgZnh3WA47n5tnKSyp90jm4jNpX6pGvxr9PyqWZ3K2_i5J1ECil8sqMOLkgiuinFZZX_QfFLjV7npmFby4nYdV-BfvIreHliGbQFkM3TTABmzteVJxEiSwh34e9A5K47nIE6Ul0TTPe0H-t2HiPTkE_-NjuGxvTUZqUV15bq01_XIfRPqVINmGE6OAIljAe1NBTQWNXM_iNQK9Kufeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10d585b107.mp4?token=ev3SdQ5_x6jv5gOiQV-SIWvIFapMbbbmSk-0_kmw2pUpaj4txfHIIwkWE37LJCHkwH0Zt25cEkNMPAkvrvBCOgog8cvnY2Cl0VHtorHjPbpIZDeVBg6Z6aJEIy_0pWFMO3MoDqR5u2iCLmQLeMIxL-5ILxIVujs2MUydViE-TDD1Ba6DxjtTC3VQuK13J02zKO4Dk0redFflRwv12pbLyqRCOtAUoEva0pSc5GN2SE8ad8XN0YckII5W5QJNmpbdxWtSpFyl5Hi7apm2F4YFO5eLmyxyA7ty7Nr06y9LCJUJpjUEY3AEBA8y7auF-DH6TXTEYP6FwcNEyghM9eKK2jjJC032Gf7Yo0BK2EKyT7vyAAUO6mL_oXXeZ38UkKrlI8TYmfu4ngKwocfu58E06Bl7LxmDPldpwNKGbea1ql9k8ggmFraQkyU3FgrBEC7IIes4N94cW7MA8_n0HVtiASWWOgZnh3WA47n5tnKSyp90jm4jNpX6pGvxr9PyqWZ3K2_i5J1ECil8sqMOLkgiuinFZZX_QfFLjV7npmFby4nYdV-BfvIreHliGbQFkM3TTABmzteVJxEiSwh34e9A5K47nIE6Ul0TTPe0H-t2HiPTkE_-NjuGxvTUZqUV15bq01_XIfRPqVINmGE6OAIljAe1NBTQWNXM_iNQK9Kufeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"خون آقامون رو چند فروختید؟"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76395" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=PYx32xybSPI8RuZOTJ-qiYrElfiMKa-6cL-kyqsmAF3RjvdWWSFhu4WGAfEUvVq2aN2rAhKD9zc0px5_QlXQjvD5lkH7YbcWgGs7dHi7QhVJebS6qbNoKT68Kre_00Zt_RxO4UnopaH_5JgAbe8_Pp_XatWbFO55yLddSVSbFI317uwrZOnZliQWKsykxPGQZt0qphgUL1TE2fH9fTHd_zkhAzsQmbFuh0noo2VfwMYsOTrGPYXQV0cueML6MsthGWPFVBCKQa5pAJtLwp2tKdWPPcZogvV2qnl5Al_onLs7ZxE8pmnQBdYegg6GI-inrYR_pxHWZnliQMIYmH3Dmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=PYx32xybSPI8RuZOTJ-qiYrElfiMKa-6cL-kyqsmAF3RjvdWWSFhu4WGAfEUvVq2aN2rAhKD9zc0px5_QlXQjvD5lkH7YbcWgGs7dHi7QhVJebS6qbNoKT68Kre_00Zt_RxO4UnopaH_5JgAbe8_Pp_XatWbFO55yLddSVSbFI317uwrZOnZliQWKsykxPGQZt0qphgUL1TE2fH9fTHd_zkhAzsQmbFuh0noo2VfwMYsOTrGPYXQV0cueML6MsthGWPFVBCKQa5pAJtLwp2tKdWPPcZogvV2qnl5Al_onLs7ZxE8pmnQBdYegg6GI-inrYR_pxHWZnliQMIYmH3Dmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه ۲۵ خرداد به خبرنگاران گفت که قرار است روز جمعه در کشور سوئیس که محل دقیق آن مشخص خواهد شد، دیداری بین هیئت‌های دوطرف انجام شود.
او توضیح داد که در این دیدار، «قرار است روسای هیئت‌های دو طرف ابتدا این یادداشت تفاهم را امضا کنند و پس از آن اولین دور مذاکرات بعدی را داشته باشیم.»
@
VahidHeadline
محمدباقر قالیباف، رئیس مجلس شورای اسلامی نیز در واکنش به امضای تفاهم‌نامه توقف مخاصمه خطاب به مردم این کشور گفته است: «با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76394" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76392">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=KCxhOMCUMbLnUYEDbiaa1-ZwuiarNiwPwOZRpq9SRjYwI7KFeicVCzLFX3p18lgszXdk31xDw8zRfXUxAo8uBNw5ckoCDbaWbU0z6asv1FLcnrCmTMj4Qr6nSfxOIqAFsnqafhsKn10QEwR33WmtnLNxn4K-W3YPIzb1C2fbNC55PW_bGKrNT24rkApXaCWJp4VulzrBGC1j2Q1QobMaepiMuED_RbbRJ4hXhWQbx5mltnlS6UO7Xh9ZCZrapYkSRRhKeN5tK6YsPJQjpkuOHYR67dblEbyXhFbtYRslJy6YZnVNiToAXuJP229qDcXo1ZMELlzIpteiomBOJ4y9-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=KCxhOMCUMbLnUYEDbiaa1-ZwuiarNiwPwOZRpq9SRjYwI7KFeicVCzLFX3p18lgszXdk31xDw8zRfXUxAo8uBNw5ckoCDbaWbU0z6asv1FLcnrCmTMj4Qr6nSfxOIqAFsnqafhsKn10QEwR33WmtnLNxn4K-W3YPIzb1C2fbNC55PW_bGKrNT24rkApXaCWJp4VulzrBGC1j2Q1QobMaepiMuED_RbbRJ4hXhWQbx5mltnlS6UO7Xh9ZCZrapYkSRRhKeN5tK6YsPJQjpkuOHYR67dblEbyXhFbtYRslJy6YZnVNiToAXuJP229qDcXo1ZMELlzIpteiomBOJ4y9-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفتگو با شبکه سی‌بی‌اس اعلام کرد ایران در صورت پایبندی به تعهدات خود ممکن است به صندوقی برای بازسازی دسترسی پیدا کند که از سوی کشورهای حاشیه خلیج فارس تأمین مالی خواهد شد.
ونس با اشاره به مزایای احتمالی توافق برای تهران گفت ایران «ممکن است» حدود ۳۰۰ میلیارد دلار منابع مالی برای بازسازی از کشورهای خلیج فارس دریافت کند، اما تحقق این امر را منوط به اجرای کامل تعهدات جمهوری اسلامی دانست.
او افزود آمریکا با سرمایه‌گذاری کشورهای حاشیه خلیج فارس برای بازسازی ایران موافق است، اما این اتفاق تنها زمانی رخ خواهد داد که ایران به برنامه هسته‌ای خود پایان دهد، فعالیت‌های مربوط به مواد غنی‌شده را متوقف کند و با یک نظام بازرسی و نظارت گسترده موافقت کند.
معاون رئیس‌جمهور آمریکا همچنین تاکید کرد رسانه‌های نزدیک به حکومت ایران بر مزایای توافق تمرکز خواهند کرد، اما از امتیازاتی که تهران باید در مقابل واگذار کند کمتر سخن خواهند گفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76392" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PqUe-DkQkZQZf1ZqB8v9Rc5cus2VO8-ptIlcKlsPA9jtol0PqEPLiGOYpGW5pJo8NODZmbQ7QqfGpW1XvKLnE6M7mYVjfOek0BDd4klHt3kA5EXoKegwTAGHIN_a6Orc3Svz7dqWnNxJ7UAW83JtDI9PVszmY5uGrSNuXhPHfnmwNjHrgdTevZl5CflR7pfi2JAEXmEDa04b4xcSKazs9Kkiu-qYFDW44p31b8-98Jg3NG5CSofTuaj9jnM15hkklgfE0iSdkAkaNF7VvKWnmtDlJ3uQESe1dRrlBKfVZVRd8BM3yxWkou3LUdLbZ_EA4aJ2RKM2IUUmOrBVtjV2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iZR_Yq3RtRZ2u6GlJjFhBv8Op1zBOnWk9ItayqiUBCTJoqS9chl6r9v-5AnJ3lJGGXh-dT6Y9FyjdZmpgYQKm5gciZ58f2OuepvF3h_zXFxZUDKcLoCeQG9-1Im5PtM_6T0GFdgemhLqMRNlmPhPOlGOxcvDJE34ywefCc4XIXmr0s1JiQvy51FsWlOorPGvIsFpvQdqGz66yC1PbFPvAAZKnuhssB-FPQrhOKjVlmVjXu3nxTGaGV1HRM4m1t_ukgcEqGZI6Qr1P9snZw_iTHdzmqB4392n7vB_p84u0Ud4fIQoMr8GZdkRt51Ey46PJmR2gtC6BZnI2QGUBX6S7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
ویدیوی قدیمی منتسب به تیراندازی به هواداران حکومت در تجمع شبانه
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که ادعا می‌کند صحنه تیراندازی به مخالفان توافق با آمریکا در تجمعات شبانه هواداران حکومت ایران را نشان می‌دهد.
🔹
این ویدیو قدیمی است و ارتباطی به تجمعات شبانه هواداران حکومت در ایران ندارد.
🔹
ویدیو مربوط به دهم اسفند ۱۴۰۴ و برخورد پلیس عراق با هواداران جمهوری اسلامی است که سعی داشتند به سفارت آمریکا در بغداد نزدیک شوند.
🔹
گزارش‌هایی از تجمع مخالفان توافق جمهوری اسلامی با آمریکا منتشر شده اما خبر تیراندازی به آنها در هیچ منبع رسمی منتشر نشده است.
🔹
این ویدیو پیش‌تر نیز با ادعای نادرست دیگری به اعتراضات دی ۱۴۰۴ منتسب شده بود.
🔹
بنابراین فکت‌نامه به ادعای مطرح‌شده درباره این ویدیو نشان
«نادرست»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76390" target="_blank">📅 22:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76389">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=W49Aa94tJ35QfnSM3J99qEJjIwwKMlFm6XfCxk6MIY5P7Sz0oAWOXgQTYsGKy1a8TVTqF179HsfE7lDPwrwgUz-dlUAt3NHOpMJRgMXjSJqv7j5HJeDBkMIxQQJ8Iid1ulv8Q6f8Q3hM_502r-XKUXJoCdGRVikGWpxdYw6VtcPLN-ztg-4hvEGtECoRdLHOUyrDc-fVWvhbo80dwvjF2xnMzXAJoAdv4gMpz6ks8HXgVZRDB5S5JZ27DNLuWABsL9pGAB9UhT6sh4CQVOh-clAq3EwGrKsE_pGQlUywP_X1wl5_1qzF08wt1CghMBw_iptuB5LPY7yNZV_cBVcgTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=W49Aa94tJ35QfnSM3J99qEJjIwwKMlFm6XfCxk6MIY5P7Sz0oAWOXgQTYsGKy1a8TVTqF179HsfE7lDPwrwgUz-dlUAt3NHOpMJRgMXjSJqv7j5HJeDBkMIxQQJ8Iid1ulv8Q6f8Q3hM_502r-XKUXJoCdGRVikGWpxdYw6VtcPLN-ztg-4hvEGtECoRdLHOUyrDc-fVWvhbo80dwvjF2xnMzXAJoAdv4gMpz6ks8HXgVZRDB5S5JZ27DNLuWABsL9pGAB9UhT6sh4CQVOh-clAq3EwGrKsE_pGQlUywP_X1wl5_1qzF08wt1CghMBw_iptuB5LPY7yNZV_cBVcgTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد نیروهای اسرائیلی در آنچه «مناطق امنیتی» در غزه، لبنان و سوریه خواند، تا زمانی که برای تأمین امنیت اسرائیل ضروری باشد، باقی خواهند ماند.
بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه در یک کنفرانس خبری تأکید کرد که به‌رغم امضای تفاهم‌نامه میان ایران و آمریکا، چالش کشور اسرائیل به پایان نرسیده و «ما باید گوش به‌زنگ بمانیم و در مواقع لزوم از خود دفاع کنیم».
به گفته دولت آمریکا، جمهوری اسلامی در قالب تفاهم‌نامه‌ای که روز یک‌شنبه امضا شد تعهد داده است که هرگز به دنبال سلاح هسته‌ای نرود.
نخست وزیر اسرائیل در ادامه سخنان خود تأکید کرد که «با یا بدون توافق، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت».
نتانیاهو در نشست خبری خود همچنین گفت که حملات مشترک در کنار آمریکا به ایران خساراتی سنگین وارد کرده و به گفته او «بعضی معتقدند که خسارت اقتصادی به ایران یک تریلیون دلار بوده است».
او در ادامه گفت:
ما به مردم ایران قول دادیم که شرایطی را فراهم آوریم که رژیم آیت‌الله سرنگون شود، نمی‌دانم چه زمانی این اتفاق خواهد افتاد، ولی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76389" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=uA6D_dUvXYmotnklNzlv3E77LzF5oi5bIRMBiHzCkoy1GUrTh2uLOiXrp-PutMfK435QGAVep8HV7g9cDMk_buGMU-OaTR5Uzv7B6llk77uyfSgDcjeY0JUaXpfJxle9NP3T2FvnA0XibTaSVPjk1r461LeS8Bma4b6Mirw3qUKooIZbHdGdSlOHZOeAGs-aUT6ZSViT3NE2aPdFqtTmU7FFQEdZyCd1qUVZdF0R9LwuBGGr4Cm6sc__nRvO86pED84k3kWWKDv_Ja5XA439dv8zfJtWG5i-DEjAihKJI4cnVzORexMxaxItbwOSYv9jSBDUd0XSQwZ1c9dZr0GP8A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d206f4a845.mp4?token=uA6D_dUvXYmotnklNzlv3E77LzF5oi5bIRMBiHzCkoy1GUrTh2uLOiXrp-PutMfK435QGAVep8HV7g9cDMk_buGMU-OaTR5Uzv7B6llk77uyfSgDcjeY0JUaXpfJxle9NP3T2FvnA0XibTaSVPjk1r461LeS8Bma4b6Mirw3qUKooIZbHdGdSlOHZOeAGs-aUT6ZSViT3NE2aPdFqtTmU7FFQEdZyCd1qUVZdF0R9LwuBGGr4Cm6sc__nRvO86pED84k3kWWKDv_Ja5XA439dv8zfJtWG5i-DEjAihKJI4cnVzORexMxaxItbwOSYv9jSBDUd0XSQwZ1c9dZr0GP8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'
#آتش‌سوزی
در  شهرک امید
#تهران
'
تصاویر دریافتی از شهروندان،‌ دوشنبه ۲۵ خرداد، حدود ساعت ۲۱
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/76386" target="_blank">📅 21:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=fooy1l1Wznbr5-wJudU2HY26eOw_zLuJcxmIQWwZROznPnCHHPAKb_akbBbnjuQ_R3bselms6RMw8G2UCq8SxHCt_CK-7eeUvzdZVNwKys0dRVkpi2qvdnMP-pQk6Ff1oDuBMAxj8Fv2tG5IMg6XpnHjyDtXZYoealfBnHjbeGMvxij4fZcdyY2JXN4aMXPIHwbM-k8U1T58dXgCIg6RcYCL2nk78dgbYCNswtc9GaX3GwcP9o08Sp7tq7WwSk5cq9HB_tZ7MrRxFjozkKDy3xQhpaz-B-M-D_Ya-sOf65Pl9LzY35EMLg3fE7ZG8IPD7zNNfZQ5bSlXBc9ThLelww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e8cc0eeaf.mp4?token=fooy1l1Wznbr5-wJudU2HY26eOw_zLuJcxmIQWwZROznPnCHHPAKb_akbBbnjuQ_R3bselms6RMw8G2UCq8SxHCt_CK-7eeUvzdZVNwKys0dRVkpi2qvdnMP-pQk6Ff1oDuBMAxj8Fv2tG5IMg6XpnHjyDtXZYoealfBnHjbeGMvxij4fZcdyY2JXN4aMXPIHwbM-k8U1T58dXgCIg6RcYCL2nk78dgbYCNswtc9GaX3GwcP9o08Sp7tq7WwSk5cq9HB_tZ7MrRxFjozkKDy3xQhpaz-B-M-D_Ya-sOf65Pl9LzY35EMLg3fE7ZG8IPD7zNNfZQ5bSlXBc9ThLelww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی از
#آتش‌سوزی
چیزی به اسم "موکب"
منابع حکومتی به نقل از سخنگوی آتش‌نشانی تهران: آتش گرفتن گاز پیک‌نیک در یک موکب مستقر در میدان تجریش
#تهران
باعث سرایت آتش آن به چادر شده و دود بلندی در منطقه  ایجاد کرده است. بازار تجریش از این آتش آسیبی ندیده و آتش به سرعت خاموش
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76385" target="_blank">📅 20:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O9FHJr6lxhF6DN1PeGdkoyi2C-DXnyvv0T9fyK6qkNC0aurJuycz3Gj1hJpUp13_7hlxcrbMg-h2CfiK3Um9ISlh0zizF9Ei1c0lTzCPM612THDYZPn6wUnO_h5w8AcAM6ArJXwk23RjLuJLnCfa90o0mFrwYETrTJXKRw6Quk9vb7jz2Jh-Q0Ac4jQlkupYiSVFnpx0sportOyBlCSs_07RASGwkwrugjeR2y_odNFNxbOgzewF91Z2xi8fb4rxFZ0uDPkHygICi66q2e67sCLB4i3r_AkQFN0Mtk-X5fBeKEV3T-XoGbX6Vgd7mll7gHrN2BiuDHIPVSdXvRzB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی روز دوشنبه اعلام کرد تفاهم‌نامه میان آمریکا و جمهوری اسلامی به امضای دونالد ترامپ، رییس‌جمهوری آمریکا، جی‌دی ونس، معاون رییس‌جمهوری آمریکا، و محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، رسیده است.
او گفت در مرحله بعدی مذاکرات، آرایش فعلی نیروهای نظامی آمریکا حفظ خواهد شد، اما در صورت دستیابی به توافق نهایی، کاهش نیروهای نظامی در نظر گرفته شده است.
این مقام همچنین گفت مذاکرات فنی از اواخر این هفته آغاز می‌شود و جزییات توافق طی ۲۴ تا ۴۸ ساعت آینده منتشر خواهد شد.
او افزود آزادسازی دارایی‌های مسدودشده و کاهش تحریم‌ها به اجرای تعهدات وابسته است.
این مقام ارشد آمریکایی همچنین گفت: «از عملکرد عمانی‌ها در مذاکرات پیش از جنگ رضایت نداشتیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/76384" target="_blank">📅 19:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=B65xVLk3GFivh9-_u1P27lbQ_tbKlamGIxU2tz59G3a9-SB33MteD99-Hmi3xlZT9-rPOJSypEgY0cxgJkR1hGIPXKBE8nl9iz6U-UhH4jh95Hj6dZGfn5KNA9iqPmbbMa3vTw5ULBZhee8w03ZKa9hpaqSd1MQLzERDfOe-5UnRWFTlG119Qi5ddDl3np5WiAmKLiNVIVk_tDcW6n9kLY5iu6qPqCNR5BXxvP3kTuE__RAuTMuVtxWwxTo8dA8Se1KUSvIMLsWth39nMWhYJ9bMMEIga7pR-iv6i1zJJEvwgUcnKxZ04Qdr1nKYG5u6MVW_UT-bmSpMUWl06QHqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e48597c90a.mp4?token=B65xVLk3GFivh9-_u1P27lbQ_tbKlamGIxU2tz59G3a9-SB33MteD99-Hmi3xlZT9-rPOJSypEgY0cxgJkR1hGIPXKBE8nl9iz6U-UhH4jh95Hj6dZGfn5KNA9iqPmbbMa3vTw5ULBZhee8w03ZKa9hpaqSd1MQLzERDfOe-5UnRWFTlG119Qi5ddDl3np5WiAmKLiNVIVk_tDcW6n9kLY5iu6qPqCNR5BXxvP3kTuE__RAuTMuVtxWwxTo8dA8Se1KUSvIMLsWth39nMWhYJ9bMMEIga7pR-iv6i1zJJEvwgUcnKxZ04Qdr1nKYG5u6MVW_UT-bmSpMUWl06QHqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رییس‌جمهوری ایالات متحده دوشنبه اعلام کرد که توافق با ایران امضا شده و متن توافق حاصل شده با ایران پس از مراسم امضای رسمی در جمعه منتشر خواهد شد.
دونالد ترامپ که در هنگام ورود به اویان در فرانسه، برای شرکت در نشست گروه هفت صحبت می‌کرد، همچنین گفت تنگه هرمز تا جمعه به‌طور کامل باز خواهد شد.
ترامپ در کنار امانوئل مکرون، رییس‌جمهور فرانسه، گفت مشخص نیست آیا در مراسم روز جمعه که قرار است در ژنو برگزار شود شرکت خواهد کرد یا نه، اما معاون رییس‌جمهور آمریکا، جی‌دی ونس، در آن حضور خواهد داشت.
او گفت: «توافق کاملا امضا شده است. و همان‌طور که می‌دانید تنگه اکنون تا حدی باز شده است. روز جمعه کاملا باز خواهد شد.»
ونس پیش‌تر گفته بود این توافق یکشنبه به‌صورت دیجیتالی امضا شده و هیچ‌گونه بودجه‌ای آزاد نشده است.
در پاسخ به این سؤال که متن یادداشت تفاهم چه زمانی منتشر خواهد شد، ترامپ گفت: «احتمالا خیلی زود. بعد از جمعه... فکر می‌کنم در آینده بسیار نزدیک.»
ترامپ همچنین گفت هرگونه کاهش تحریم‌ها علیه تهران «به رفتار ایران بستگی دارد. اگر آن‌ها کاری را که باید انجام دهند انجام دهند، این روند آغاز خواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76383" target="_blank">📅 19:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=rynlrnJjjVygDzwjH_27rndOGM2vCFevLQDay-Jvhqk_ubiEuMHa9sT7_sn-At1HE2L_agstTxc8ZmEYsE34Twm9aLa0IPiyNXkGkBYl5C5uyQn9dWXxVubj1wMvMv0ymdf3Y921NrtsNpsMW4Uxdb7rCDlgLpJocNzuiTA9VBiDAYQqJM9HWF9AiBVUlhWmJe0CBamL7MM6Qm86KUZVptl21mMAiVEd2yF0s-NSDc0_krpUh0Ne-6lAIQrT6ukWueO5oZMttxwT7V9m7FBvhIrbln8VJQcfx1dglLYrX-vAwGObOrY1hCvjdboRh8qrkhAe6PPvPg3RjloeoH6m0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/06a4a159c2.mp4?token=rynlrnJjjVygDzwjH_27rndOGM2vCFevLQDay-Jvhqk_ubiEuMHa9sT7_sn-At1HE2L_agstTxc8ZmEYsE34Twm9aLa0IPiyNXkGkBYl5C5uyQn9dWXxVubj1wMvMv0ymdf3Y921NrtsNpsMW4Uxdb7rCDlgLpJocNzuiTA9VBiDAYQqJM9HWF9AiBVUlhWmJe0CBamL7MM6Qm86KUZVptl21mMAiVEd2yF0s-NSDc0_krpUh0Ne-6lAIQrT6ukWueO5oZMttxwT7V9m7FBvhIrbln8VJQcfx1dglLYrX-vAwGObOrY1hCvjdboRh8qrkhAe6PPvPg3RjloeoH6m0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت فارسی وزارت خارجه آمریکا با انتشار ویدیوی بالا نوشت:
جی. دی. ونس، معاون رئیس‌جمهور ایالات متحده: توافق با ایران، «مبتنی بر عملکرد» است.
«باید به خاطر داشته باشیم که اقتصاد آنها اساساً نابود شده است. برنامه هسته‌ای آنها اساساً نابود شده است. اگر آنها [در چارچوب این توافق] اقدامات درست را انجام ندهند، از همان ابتدا هرگز پولی در اختیار نخواهند داشت که بتوانند برنامه هسته‌ای خود را بازسازی کنند.
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76382" target="_blank">📅 19:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OO0prxRupLiGPD0zbPmgbCmo53Ps3smSY_FmC-lBh0qAir3LAPkmObbg-CQJEdC2dkifYmUSYswFIQZ3ri-oL-eJArBJkBaynDK2ZjXICAgUZdg97id0X8phdhBENyBNOtJzow8zTPRvmrVBt6cdaFuzl59DXN-tzMncCbzBBuUXOnhnzPdOJxiLeduMF3olUXgjRvbeFhaiGCametx468smvqoRHrZpQTAEW_pQTr8HkSFJmHuDt92Fi-So4yRR66pg40_4622eZp2X8n94hsQhSGRGGCj53QntZhCgPZV0d7d5rl9DQyCe5JPFZ7NXmauBZUCrVPgREHk9BQzlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MUJ0_07EZ8Fs_W7FvLudkhyZQWS5_nt_Rhz7iWsu1TUIZQP9YqIm4F70hrQviU7B00qBfFRayxSFt_0Ty5BvjEJj286-izrJ1Zawh9qHZIQGNPyUfU2zGF_BtddFnzcqE8GeS_MvPyyv-ijCQDOdr2KsPTVFXq8jd7rf9obetxAkvYFNRvGVth3fjqUULV9gTAhrMytI4g-S3_HXqD7Gd_T6jS8JboEvH47zGAT3wDsgB84HgaCeGR3biHqMsH_2mjuXGe8hDod6wkZqEgvAnNbe7PXn5HEmXjxsBzBsDwr34R-0UQ8jTYRy5v7vXA8yhN6nCozkjbbI1X0m3-jgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g7Up20zad-7yMRBnwURTfjL-Aw_FZqG7cFkJj1RS3R0sAZkqJWBY4ikkVxYIh52JiG6KoqUSio_uXH-wKGxPCeTr6NZStaSFQB0Kua8AW_KyC-RiioD-Jg6h2UqXYI3QmHTJUhYWPGrYk8kX_NParKBmH2BRr0PXKo1Jj8DvO8WHBq5-HA01u6B8Pa-II2Ig4DqFApDU-SKrAAvug-CCT69qUuxEJRnKGLDMKkNHqNBpApaP-3vBwHQ44Ohl3G67jC9ua6DnrUnrY2Bc4lzEdQ7KfOYl7cS5Qj9OLqUyzK2ekEVnKGEtgY0J3iycUJp8T8ZQRJ-vVlSP4RwYgN0PgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع حکومتی با انتشار تصاویر بالا نوشتند:
کلاهک ۵۰۰ کیلویی موشک تاماهاوک سقوط کرده در اطراف ورامین خنثی شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76379" target="_blank">📅 19:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRPU1jYlntRG8IHjYGLdv_UHXUROYsDkm9vd4ue3qJ9AzxY4i2Gsnm3So0_v0TMItii2SbtxcnXhjcV_DdTkdlQGxUqb-N07yujxNnd8kUhb-UXitwnBoIucI0GBo_aR1CgeUWap-G6Mdb6O3s6JNHR0EMn2sCRV6alMulM0Bxk7x9gGfhl8JrW2CQHVN2NRfBosyHVzIm84GERFZwzhzScw75raCK0VxCGwf7KeblN58Xzz732U21XV0Hoktr60dqy28PNszFCmvmW_u7FeGbj1IoVrItHlNxQAerome7b0MUPbvbVCv2Vo0E9pXbrjmRRQJ_J7ki2vN6xONplOgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اطلاعات تهران، روز دوشنبه ۲۵ خرداد ۱۴۰۵ از بازداشت سه شهروند به اتهام انتشار مطالبی در شبکه‌های اجتماعی خبر داد.
خبرگزاری مهر به نقل از پلیس اطلاعات تهران بزرگ گزارش داد که این افراد در پی رصد فعالیت‌های فضای مجازی شناسایی و بازداشت شده‌اند. به گفته پلیس، بازداشت‌شدگان متهم هستند با انتشار مطالبی در شبکه‌های اجتماعی به مقدسات و آنچه «مدافعان وطن» خوانده شده، توهین کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76378" target="_blank">📅 19:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AWIJCaZl0ko8OfRfajyiVncfh7QOFgR2Jj6heF9pPQbP4DNB5j_WnICc8i6-k3zB3nxvud-2o5YIORBZJp06g4cfg39o8VEGpzNwr-MZWdQk9Jl5NKuEL_lWsoKpmaf_v2hVkVdbD2StcQLdRuMYDOQygG6y0Mq1nL6NxmxiO2_xqo03O98XGHTBdkUR706JRu8gj7l2HUO0Pa4ltq1FpAACLj24zNHfRlTgQK-RxeMNC_qg-NOar5ieh4XckQ6vGvjSFlVMHF5bA7_Pn0F2fd3DU4bkQII9qc5QNDoe_RUQQpsCkNXZTOO1uqkvRYA_mw4tKU4R2iFb_5sZBRJeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RKVFhtYlODkLWlaT8B84Jb9it6k8TQrPVzg68v0gcFrbfcwZoHz1g8ZvxFBZXKaP1E14KX0bAg5937eofB7Pa5YllkwNxSzKwfRCYQS_4VkFOQF5sN7i7xoNZ7BrIwhTGeSbPxLFT3WZ-hEef2z2UKWcPiNMWPurtF6AREKUjUdHMABjm7q9hpIVQExseLewRG0FSbcjqEzRRN8_F6hFIHbkZRc_WKv1k4q_w_owGMlpOvZjh3fjPsc3jQopojaDnAGhttr7qtswHa-Fq8xkcDWcobuJZ1-RObcQo64VdiiG6WAAIYuEzpY1xHTXcUpriyQF65rOQVTk_d3sqHc5zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pbe4ErtcoyNXV7-o3J4ECXJo-cD6JrF5yC-gPxCHz0l-eFbW-bbaa7gVcxx_Le_M7yMHJsV2Sl5KOm_XCfutwqcw7vP-g7yqaUcClLqnE_huFoTNUzltJkGOzj9s5BdpFGnKYVqmZCZQB7E9AmUWjrOEHwVQjxGKFTQo-tlL5OXt5lEwLSKL2OboafYll1chmI7nMToz3eeN_QcvrhwOHtEaBLWBm5p4Q8c5G66gZWmbpiUYmjhw_zgnkTFZ2nBlBpz86gq_N7f1uFWNH0l0DoFZoYmBRb4upqWfmVwM0ZHDlIzpkITUD0dQs7hq1FKn011MfGYkHk_xFLXms02_wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/65becd728e.mp4?token=hOLY0NAtIu1Hi6JXxmYXyaoq227N82K1sYXj9Y9J-gsAEe0zhLn4W3ac3JoRr_7njY6Rn4ZES20a2Xz_dXN9COBCogsEXKhsrWO33p6lS4-ndpZswaPUIDSWEMjOc2hNrl0R6NsoyZZcB6CxQxbt7LgejcK4t4tTpu-u7JhPex5DX328iwYfuFapEEp_4c5gkWBwdPG_7SnMFXSZZlwKqmgCSOENRw7b3sAaKSnPy0CK-DrdAPbl9YmRIZ7YeUsUTmK7oF7cca_stDBpxYrwsQ7oo73jUqc6q4A7y6jPqnL9V6fMArHjvly8GA1ZTi8fbkRhtF-8ixUcrXiF--Asbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/65becd728e.mp4?token=hOLY0NAtIu1Hi6JXxmYXyaoq227N82K1sYXj9Y9J-gsAEe0zhLn4W3ac3JoRr_7njY6Rn4ZES20a2Xz_dXN9COBCogsEXKhsrWO33p6lS4-ndpZswaPUIDSWEMjOc2hNrl0R6NsoyZZcB6CxQxbt7LgejcK4t4tTpu-u7JhPex5DX328iwYfuFapEEp_4c5gkWBwdPG_7SnMFXSZZlwKqmgCSOENRw7b3sAaKSnPy0CK-DrdAPbl9YmRIZ7YeUsUTmK7oF7cca_stDBpxYrwsQ7oo73jUqc6q4A7y6jPqnL9V6fMArHjvly8GA1ZTi8fbkRhtF-8ixUcrXiF--Asbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی از دود یک آتش‌سوزی 'در میدان تجریش
#تهران
دوشنبه ۲۵ خرداد، الان'
Vahid
آپدیت در پست‌های پایین‌تر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76374" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76373">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJzkXjiJnQmBqmc-HgJUrMGhHxHgXYla-KvsBSTkltYvxouvGaLBIONz273JlpDUFGAvPBBybgd8M7E8vxCsIBNPxX795SGDCZFc5OGXoP6_ItJECGWMgxf62bdt0jmw4r4Ino74ggOMQ_tLX3draW0OiXDtAu627M3Kz9WlVFcT2K_b6FkQj6W9OkqQUbUWhQTGOaPdzmQMlIaX22QJfg97nu7XUYG9HriT9d_5qjIJCoyCY6MlpDQekzNHOsFk0FU3-vYGBE8JMByq_aVZ-uyigeCETMzyTJ5QCMdnd4sn0N_vIlCKW2SJ_XRgJwU6JegEW_FjXnCvWxQhzTgKTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از منابع امنیتی لبنان و رسانه‌های دولتی این کشور گزارش داد یک حمله پهپادی اسرائیل خودرویی را در جنوب لبنان هدف قرار داد و راننده آن کشته شد.
این نخستین حمله مرگبار گزارش‌شده اسرائیل در لبنان از زمان اعلام توافق میان آمریکا و جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76373" target="_blank">📅 18:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76372">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlEo9ht1xYcymiSjPXFY2EdAqXkhPH4ZHLt8lAUBQm_HEeZLP9KMmV7T5pvYQqa3e4EQFhfJJsbGcqTvDyk9_iJf0AfEfxW8H1YA4tJbDwx1NgbAJinfCefdtDecJlX-tv2gS7ccnb8cwIOEygPBfpO_KYo1DreN4Sbnh3NwY-JB92HXURWy6mIQ10S7AMrCNuHzm8bQYf4CYy1QYG_rcjFfeHxq4sJewnpZn5nLuu4qXrqFkZEZRQmh5J96zHPrdPQMETvUYy9MgIgNE3Ayb-NvU96fVPU515zASg78tq3fXQhGZdk3zZYpZbB_2oL3t6DV2C512H4gaG-D90CsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، روز دوشنبه ۲۵ خردادماه اعلام کرد آمریکا و ایران پیش از مراسم رسمی امضای توافق، روز یکشنبه (به وقت آمریکا) آن را به‌صورت دیجیتال امضاء کرده‌اند.
ونس در گفتگو با شبکه ای‌بی‌سی گفت توافق روز یکشنبه «به‌صورت دیجیتال» امضاء شده و قرار است مراسم رسمی امضای آن روز جمعه در ژنو برگزار شود.
در همین حال، مسعود پزشکیان، رئیس جمهوری ایران نیز، روز یکشنبه در مراسمی دولتی با اعلام همین خبر گفته بود، توافق روز جمعه و حضوری امضاء می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76372" target="_blank">📅 18:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76371">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_WPx-6vdmnFCOhSi3NpRzHB4hX9MRIByQKqHGMyrfwNV_JwxMwGQZi1AI9ZOsp37WuNlw8lhm-rp1OR4AyH23UFH9bNScylz-bA6WblB2SBo9p_I_sTO_JShzGmqcgzwALGzksp5j5p6AbQkDElDpkv7cp_B4KofQovzj4d1KVizkBHD9s5CVBVqx5c0qj0UWhxp7YZxnO6Mv4RYrMXvhbCAwubvcXXTU9Scx0PkjZHpeyfXT0rFmTk1XNrd0T-8o9W7IzUItdXbRJRQoMuemf4LGLUXwHLWqr7uhLGbRDcsVK5l41ZtC-Ky8d3KDy7K0qn1BEKHP8FiUv_SijhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با وجود اعلام مقام‌های بانکی درباره رفع اختلال در خدمات بانک‌های ملی، تجارت، صادرات و توسعه صادرات، خبرگزاری فارس وابسته به سپاه اعلام کرد که بخشی از خدمات غیرحضوری و اینترنتی این بانک‌ها همچنان با اختلال مواجه است.
پیش‌تر این بانک‌ها در اطلاعیه‌های جداگانه اعلام کرده بودند که تمامی خدمات کارتی و سامانه‌های اینترنتی و موبایل‌بانک به حالت عادی بازگشته است.
فارس گزارش داد در حال حاضر خدمات مبتنی بر کارت در پایانه‌های فروشگاهی و دستگاه‌های خودپرداز این بانک‌ها فعال می باشد، اما بخشی از خدمات اینترنتی و غیرحضوری همچنان دچار اختلال است.
شورای هماهنگی بانک‌ها، وابسته به ساختار بانکی جمهوری اسلامی، روز شنبه ۲۴ خرداد حمله سایبری به سامانه‌های چهار بانک ملی، تجارت، صادرات و توسعه صادرات را تأیید کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/76371" target="_blank">📅 18:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76370">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYvbhNHrzx9vtbAdEDHeELl8l0DnFRKCZdANrW8K2IIce51SD75eLnMVBPRhLgR5i4PJD_ZGoGsx05wXwbhLncEFUdtISdnfLGMIlkyXgtGvKRNOjdhVpDQ78WR-C_H0rDsR6D99O4qTx24NyaUV1Kz-O-kH-S3khLcQ6oLEGJNlZHfgxyUk2rs9KjMEjWHOLZfH2pMsDW4-UM8ygLc41D6gDdohyko8pnL5rZLtZPHyRceHf6jHDqZ-aPBT0BYWY7bj67bbgJJt7rd7JZaTD0o-RyQ8E8K9NL5HzMmt5MGcMe0KfmGRwx88OOsuxbmTQjPWIdbRei1OjshlzEEYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه، به دنبال اعلام توافق ایران و آمریکا بر سر امضای تفاهم‌نامۀ پایان جنگ، قیمت ارزهای خارجی و سکه طلا در بازار آزاد ایران کاهش قابل توجهی یافت.
وب‌سایت‌های اعلام نرخ آزاد ارز و طلا، بعدازظهر روز دوشنبه قیمت هر دلار آمریکا را کمتر از ۱۶۲ هزار تومان اعلام کردند که نشان‌دهنده کاهشی در حدود ده هزار تومان از زمان اعلام توافق موقت است.
قیمت هر دلار آمریکا در روزهای گذشته بیش از ۱۷۱ هزار تومان گزارش می‌شد.
قیمت سایر ارزهای خارجی هم در بازار آزاد ایران کاهش مشابهی داشت.
همزمان قیمت هر سکه طلا در حدود ۱۶۷ میلیون تومان اعلام شد که نسبت به روز قبل کاهشی پنج میلیون تومانی را نشان می‌داد. این میزان کاهش در حالی رخ داد که قیمت طلا در بازارهای جهانی پس از اعلام توافق ایران و آمریکا افزایش یافته بود.
قیمت دلار و طلا در بازار ایران از زمان وقوع جنگ در ایران افزایش یافته و در روزهایی هر دلار آمریکا تا مرز ۱۹۰ هزار تومان هم معامله شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76370" target="_blank">📅 18:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76369">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVLAtHVz9G6Pv63jZrzP50TMr7G9RRX9xn8ThJJZzlSHyvfi4BlUsBtsuCVg3kFP57h2JRf6NQeC8sMs1X3qvND7m2L-mWStayfKcUEmsvJDFLZB01dDXe34q8eKBNcc0PVO2nzJzNed_TQOxqANTNfl8x83WRT76lti3q7i8aGiK0S4LDl4wzAX8y3yRIcCl4raykGvPIrbhKBcgCiUA4V_8AXhRaSaDKO7bb0j4T7_EzA1TOUK7YDWL7aniBd6bL0sI8Nd5oQ-Yls4S2y0DZ_nNiK5LlUJr7zbR-BE0rTKpIQuV7KaKq86seepSmdDMBOAlvo3E-eQiQmZJI0rAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه ۲۵ خردادماه در پیامی در شبکه اجتماعی تروث سوشال اعلام کرد کشتی‌ها، از جمله نفتکش‌های حامل نفت، حرکت از تنگه هرمز را آغاز کرده‌اند.
ترامپ نوشت: «کشتی‌ها در حال حرکت هستند؛ بسیاری از آن‌ها با نفت بارگیری شده‌اند و از تنگه هرمز خارج می‌شوند. آن‌ها از مسیر جنوبی حرکت می‌کنند؛ مسیری که کاملا امن، مطمئن و پاک است.»
رئیس‌جمهور آمریکا همچنین افزود: «مسیرهای دیگری نیز برای تردد وجود دارد.»
پیام ترامپ در حالی منتشر می‌شود که صدا و سیمای جمهوری اسلامی ایران، روز دوشنبه در گزارشی تصویری اعلام کرده بود: «بیش از ۹۶ ساعت است که نیروی دریایی سپاه هیچ مجوز عبوری صادر نکرده است.»
پیشتر رویترز گزارش داده بود، نخستین نفتکش حامل گاز طبیعی مایع پس از اعلام پایان جنگ جمهوری اسلامی ایران و آمریکا، صبح دوشنبه از تنگه هرمز عبور کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76369" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76368">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjPX7Ll9HVHZ1m79m6Bbydz7wjKLaHH96PjFCoFuF7HBrdW3CZpCCXbEM_qzhAHZ7RWhHl1bdhwu7DKrBYoS8_3i1k12e-VhTimCilAkR4xeiGqiB4C0p-s0dwkKz1e1uHLDj6JcklHEx9Hv33LuYU8QarN91ZfS6HMy87Y-ajgw1dDk5_5ChrMHfJ0KO0xKLk-5lgBhrgwXz40-MOMHWk1XxCieuaYsBIux6hplHaN6an3s3G9Aciz1agRPuLCmy8lcGTAreoN8tjEp029x7mk3qZ4ygbTnT6yr335b274XImAy3tQVxfKBcP1qtPAlol581c2QcdCu9DzJtFbIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور آمریکا می‌گوید تفاهم‌نامه ایران و آمریکا روز جمعه در حضور عباس عراقچی و محمد‌باقر قالیباف در سوئیس امضا خواهد شد.
جی‌دی ونس گفت که «جزئیات زیادی از توافق هنوز حل‌و‌فصل نشده است» اما آمریکا انتظار دارد که تنگه هرمز «در درازمدت بدون عوارض باز باشد.»
سخنگوی وزارت خارجه جمهوری اسلامی اما گفته است که هنوز مشخص نیست که چه کسی از جانب ایران تفاهمنامه را امضا می‌کند.
اسماعیل بقایی همچنین تاکید کرد که ایران «به‌دنبال گرفتن عوارض نیست» اما «هزینه ارائه خدمات» را دریافت خواهد کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/76368" target="_blank">📅 18:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76367">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTQDb4PXGEfnA_srTXPMQDBOuNfK433qdYEz1OU_kyBKzMx58D57f4QkuN1m8WRb52PRQ7aWw8uxoE-dhArS8sw8oeBTYgAYBrkzMP5s51M2vjS4RUQCBaJJJZXZw6BVcFctP7pXtFuJ_XQXcjQevSaiv2JbSw-ULXY7oLuV2DWLUJpHyJ92DXakIiL0wH_N8bsJxQp4Aw8ssyiBqhhsEvOh-9YhdhaJl2w-EwBob_yu9JsCISFMkHhXLU15frI6VerTsp5osCbNSGqKO0rRPfbLb7DQ76j-gdcqxUYl1pvBxxGjxoi3x71QaQ_zFWoDspGkJQ5quOGs2yDXoglm6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نوید عالم‌چهره» ۴۴ ساله، ساکن ملک‌شهر اصفهان و پدر دو دختر، روز جمعه ۱۹ دی‌ماه ۱۴۰۴ هدف شلیک گلوله جنگی قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله جنگی از پشت به پهلوی او اصابت کرده بود.
خانواده می‌گویند نوید عالم‌چهره هنگام مجروح شدن هنوز هوشیار بود و توسط اعضای خانواده به بیمارستان غرضی اصفهان منتقل شد.
به گفته آنان، کادر درمان پس از تحویل گرفتن او اعلام کردند که برای عمل جراحی به اتاق عمل منتقل خواهد شد.
نزدیکان نوید می‌گویند تا صبح مقابل بیمارستان منتظر ماندند، اما با باز شدن درهای بیمارستان و مراجعه برای پیگیری وضعیت او، دیگر اثری از نوید پیدا نکردند. به گفته نزدیکان، پس از دو روز جست‌وجو و مراجعه به مراکز مختلف، سرانجام پیکر او را در سردخانه باغ رضوان اصفهان پیدا کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76367" target="_blank">📅 18:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-RZm6kLu1k08hW53hvvjQfz8C9Xp44v7wbg0W8nkS82m9J1TFh-udLNJNYAtXvUKFkmUqJe6vmqQakpE1QBtdFDKgq0GvyQe74FpVEiJp3S8G1s0oS7EygJxaK4AZH-HmI2rc2Bgav5yVYUGCKGgeDlrxdeY6BfJGhvDsgrqbe-He6sT23Ld7JEYWtfLaOQdXWzqx1hStgG5ydVoFlgEsCXznm-rgVH166Ft99ZaMk-OSPPvMI1zecZzieMaO3S1ejfZalv6gsnkQToMvcdpKe4NWRwyM7V7lQWUS5BNn6Blo4cWUennB2sGf521ls1va0APH_lD6oQI-e7cm5THA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل اعلام کرد که از آغاز سال جاری میلادی تاکنون، دست‌کم ۴۰ نفر در ایران به اتهام‌های مرتبط با «امنیت ملی» اعدام شده‌اند که در میان آن‌ها ۱۸ معترض نیز دیده می‌شود.
ولکر تورک روز دوشنبه ۲۵ خرداد افزود: «مقامات دست به سرکوب شدید زده‌اند، هزاران نفر را بازداشت کرده و محدودیت‌های بیشتری بر فضای مدنی اعمال کرده‌اند».
او در بخش دیگری از اظهاراتش از اعلام توافق صلح میان ایالات متحده و ایران استقبال کرد و از همه طرف‌ها در منطقه خواست حداکثر خویشتنداری را رعایت کنند.
تورک گفت: «از اعلام این‌که ایالات متحده و ایران بر سر یک توافق صلح به تفاهم رسیده‌اند که شامل آتش‌بسی فوری و دائمی، بازگشایی تنگه هرمز و چارچوبی برای ادامه مذاکرات است، استقبال می‌کنم».
او افزود: «در این مقطع حساس، روشن است که همه طرف‌ها باید حداکثر خویشتنداری را به خرج دهند و برای اجرای سریع و با حسن نیت توافق حاصل‌شده تلاش کنند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76366" target="_blank">📅 18:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/beda093be0.mp4?token=rIMNlp3Z2ypqfcfZjZTKn71u77-RHo0LunPMCpGd1uYEG0vM6YjvAZZyUQczopzDemrRrQjMyoAbO-p_tSacmdPea5sfUuhKaRQTZSzjAY56PL9hkYc1UztKegAXqnrI58QfUoZ0BUblZnYM6I6kqja6XsB3QTOi7gdbEEC-yBQv050IZKE0qh85X68WYGi3w0YPtdts3vxlNKP05x6xPxM5-bed9qBqeppp2_6kT2hSJ4WCTYrn88JLoKSAY5Du9hzykTofRPk3vz7XbuviDzv-Of78NezArXybJyKhW7NixswTawOVMssTKOWJlT6G3Ba4B-vvCmMXqKLDy8HRFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/beda093be0.mp4?token=rIMNlp3Z2ypqfcfZjZTKn71u77-RHo0LunPMCpGd1uYEG0vM6YjvAZZyUQczopzDemrRrQjMyoAbO-p_tSacmdPea5sfUuhKaRQTZSzjAY56PL9hkYc1UztKegAXqnrI58QfUoZ0BUblZnYM6I6kqja6XsB3QTOi7gdbEEC-yBQv050IZKE0qh85X68WYGi3w0YPtdts3vxlNKP05x6xPxM5-bed9qBqeppp2_6kT2hSJ4WCTYrn88JLoKSAY5Du9hzykTofRPk3vz7XbuviDzv-Of78NezArXybJyKhW7NixswTawOVMssTKOWJlT6G3Ba4B-vvCmMXqKLDy8HRFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز رضوی، گوینده محبوب علی خامنه‌ای، درگذشت.
FattahiFarzad
بهروز رضوی، گوینده، صداپیشه، ترانه‌سرا و بازیگر، پس از دوره‌ای بیماری در ۷۸ سالگی درگذشت.
او فعالیت حرفه‌ای را از سال ۱۳۴۷ با گویندگی در رادیو آغاز کرد و طی بیش از پنج دهه فعالیت، به یکی از شناخته‌شده‌ترین صداهای رسانه‌ای ایران بدل شد. روایت مجموعه مستند «ایران» از جمله ماندگارترین آثار او به شمار می‌رود.
بهروز رضوی علاوه بر فعالیت در رادیو و تلویزیون، در سینما و دوبله نیز حضور داشت و در آثاری چون «گناه فرشته»، «سفر به چزابه» و «نجات‌یافتگان» ایفای نقش کرده بود.
او همچنین شاعر ترانه‌های «کویر دل» و «گمشده» با صدای مرجان بود.
این هنرمند متولد یزد از سال ۱۳۷۴ در کرج زندگی می‌کرد و برادر عاطفه رضوی، بازیگر و چهره‌پرداز، است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76362" target="_blank">📅 18:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHfhlxpsU5YQ8Jwr-_SgtjPE8dz6QCs9PtBcxY9WbIkx66r3BueqBG3eZv5cob_uSzVic-2aShMrSoHkXbFy_KE7b7vJxEhHasNP9tf2QoL_9pp3n0H7CMfcqK48yPVH-hYDF0TgczrfT3W6dU_QUJXcTSTDq24SoU25Hw52wccjF-sWlDYRLL8pvmmvW-ipaFQ70bMU5rU7PZ8CESpUq4EyvG26CIJf16kgZ9Az7t8GcTSIURjuUc-CQud8R5mSIW5sKTBqU2LYqqY0LSAuCxbmCCmSNwzG6c7Gn0oNpwRjryNecVL49ZUSvkaFToplnbeUW1hHFiArODuMOldPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گفته دو مقام جمهوری اسلامی که نیویورک‌تایمز نام آنها را اعلام نکرده، تهران تا پس از عبور ساعت از نیمه‌شب به وقت محلی صبر کرد تا توافق را نهایی کند، زیرا نمی‌خواست این رویداد مهم با روز تولد دونالد ترامپ، رئیس‌جمهوری آمریکا، در روز یکشنبه هم‌زمان شود.
بر اساس این گزارش، اختلاف زمانی هفت‌ونیم ساعته میان تهران و واشینگتن باعث شد هر دو طرف بتوانند روایت مورد نظر خود را از زمان نهایی شدن توافق ارائه دهند. ترامپ گفته بود توافق در روز یکشنبه نهایی شده، در حالی که ایران اعلام کرده بود این روند در روزی بعد از آن تکمیل شده است. دونالد ترامپ ۱۴ ژوئن ۱۹۴۶ به دنیا آمده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 454K · <a href="https://t.me/VahidOnline/76361" target="_blank">📅 03:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مصاحبه ترامپ با نیویورک‌تایمز، ترجمه ماشین:
رئیس‌جمهور ترامپ بعدازظهر یکشنبه در مصاحبه‌ای گفت توافقی که با ایران به دست آورده، در نهایت تضمین خواهد کرد که تنگه هرمز  «برای همیشه بدون عوارض» باشد و استدلال کرد که با وجود مخالفت‌های بنیامین نتانیاهو، نخست‌وزیر اسرائیل، او اسرائیل را از نابودی هسته‌ای نجات داده است.
آقای ترامپ همچنین اصرار کرد که اگر ایران نتواند به توافق نهایی هسته‌ای با ایالات متحده برسد ــ روندی که دستیارانش می‌گویند انتظار دارند روز جمعه در سوئیس آغاز شود ــ او حملات نظامی به تهران را از سر خواهد گرفت یا در ازای دریافت ۲۰ درصد از درآمدهای منطقه، ایالات متحده را به «نگهبان خاورمیانه» تبدیل خواهد کرد.
در یک گفت‌وگوی تلفنی ۲۸ دقیقه‌ای که آقای ترامپ از محل اقامتش در کاخ سفید آغاز کرد، و در یک تماس کوتاه بعدی، رئیس‌جمهور ادعا کرد که تصمیمش برای حمله به ایران در اواخر فوریه و محاصره دریایی بعدی بنادر این کشور پس از آنکه تهران تنگه را بست، خاورمیانه را به سود آمریکا دگرگون کرده است.
او که در روز تولد ۸۰ سالگی‌اش صحبت می‌کرد و صدای جمع شدن خانواده‌اش برای شام جشن تولد در پس‌زمینه شنیده می‌شد، از دو رهبر اقتدارگرا ــ شی جین‌پینگ، رئیس‌جمهور چین، و ولادیمیر وی. پوتین، رئیس‌جمهور روسیه ــ به‌خاطر کمک به این توافق تمجید کرد و
آقای نتانیاهو را به‌دلیل انجام حملاتی که نزدیک بود توافق نهایی را از مسیر خارج کند، به‌شدت مورد حمله قرار داد.
آقای ترامپ درباره نخست‌وزیر اسرائیل گفت: «او آدم بسیار دشواری است، و صادقانه بگویم باید بابت این کار از ما بسیار سپاسگزار باشد. چون اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.»
با اینکه متن توافق هنوز منتشر نشده است، به نظر می‌رسید آقای ترامپ در حال توصیف امتیازهایی از سوی ایران است که این کشور هنوز نداده، یا به مذاکرات بعدی موکول شده است. برای مثال، تفاهم‌نامه فقط عوارض عبور از تنگه را به مدت ۶۰ روز تعلیق می‌کند و سپس وعده گفت‌وگوی منطقه‌ای درباره آینده را می‌دهد.
ایران پیش از جنگ هرگز عوارضی دریافت نمی‌کرد، بنابراین آقای ترامپ در اصل در حال جشن گرفتن بازگشت به وضعیت پیش از جنگ است.
آقای ترامپ بارها تفاهم‌نامه جدید خود را با توافق سال ۲۰۱۵ میان باراک اوباما، رئیس‌جمهور وقت، و رهبری ایران مقایسه کرد و گفت توافق او تضمین خواهد کرد که ایران «نتواند سلاح هسته‌ای تولید یا خریداری کند». ایران زمانی که در سال ۱۹۷۰ پیمان منع گسترش سلاح‌های هسته‌ای را تصویب کرد، با این موضوع موافقت کرده بود و در صفحه نخست توافق دوران اوباما نیز دوباره بر آن تأکید کرد.
در سه ماه گذشته مذاکرات، که به رهبری استیو ویتکاف، فرستاده ویژه رئیس‌جمهور، و جرد کوشنر، داماد او، انجام شد، ایرانی‌ها اصرار داشتند که هرگز از حق خود برای غنی‌سازی اورانیوم تحت آن پیمان دست نخواهند کشید.
آقای ترامپ گفت هنوز بر سر این موضوع مذاکره می‌کنند که آیا ایران غنی‌سازی خود را برای ۲۰ سال تعلیق خواهد کرد یا نه ــ ترامپ تلویحاً گفت شاید به تعلیق ۱۵ ساله رضایت دهد ــ اما گفت ایران برای همیشه به غنی‌سازی در سطوح پایین محدود خواهد شد؛ سطوحی که «هرگز نمی‌تواند از سوی ارتش استفاده شود».
توافق دولت اوباما نیز همین شرط را داشت، اما پس از آنکه آقای ترامپ در سال ۲۰۱۸ آن توافق را کنار گذاشت، ایران غنی‌سازی در سطوح بسیار بالاتر را آغاز کرد؛ از جمله اورانیوم نزدیک به سطح مورد نیاز برای بمب، با غنای ۶۰ درصد.
در جریان این گفت‌وگو، رئیس‌جمهور حال‌وهوایی شادمانه داشت و درباره رویداد آتی «یو‌اف‌سی» که قرار است در محوطه جنوبی کاخ سفید برگزار شود و احتمال اینکه باران آن را مختل کند، صحبت کرد. او گفت: «در زمان جنگ چنین چیزهایی پیش می‌آید.»
nytimes
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76360" target="_blank">📅 03:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=BuvcOXm4GqWPF7_98jgskPhYduTKQdMabHJKsh2k5-TOirayuw9sOKuVD2V5lehi4m91AFEBmMmSLi2dbOQV37BqMPHCa9u2rTR1vucu2TGo7avU3U6EYqxxuSUvWADdF83JbPKLXb3H3RgZgknqUehewEatFpwbQIkqbL7ZCtxNt6ga-RG0F1krT4OldkcqOuU39hPJjzHBoCyqonE-iJ70HvxTb92Eof9ZctBaYBwh93UxARNGmt6KYfrMq0_rkadPqQ5fva-QQkcyQd0jZZIAmjalKxqaWytDk90gMkT0V3NAqtKtbsuAwE1IamGtTCi166hFLzaGYYF8yrzcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/129bb5a743.mp4?token=BuvcOXm4GqWPF7_98jgskPhYduTKQdMabHJKsh2k5-TOirayuw9sOKuVD2V5lehi4m91AFEBmMmSLi2dbOQV37BqMPHCa9u2rTR1vucu2TGo7avU3U6EYqxxuSUvWADdF83JbPKLXb3H3RgZgknqUehewEatFpwbQIkqbL7ZCtxNt6ga-RG0F1krT4OldkcqOuU39hPJjzHBoCyqonE-iJ70HvxTb92Eof9ZctBaYBwh93UxARNGmt6KYfrMq0_rkadPqQ5fva-QQkcyQd0jZZIAmjalKxqaWytDk90gMkT0V3NAqtKtbsuAwE1IamGtTCi166hFLzaGYYF8yrzcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف پیش از چنج‌رژیم: مذاکره با قاتل سلیمانی شرافتمندانه نیست
همزمان با انتشار خبر توافق میان واشنگتن و تهران، ویدیویی از اظهارات محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در روز شنبه ۲۰ بهمن‌ماه ۱۴۰۳ بار دیگر در شبکه‌های اجتماعی بازنشر شده است.
قالیباف در ششمین همایش ویژه فرماندهان و کارکنان ستاد فرماندهی سپاه، در پاسخ به پرسشی درباره تفاوت کامالا هریس و دونالد ترامپ گفته بود: «حتما فرق دارد، ترامپ قاتل شهید سلیمانی است. مگر ما می‌توانیم بی‌تفاوت باشیم؟ پس حتما برای ما فرق می‌کند.»
او همچنین با اشاره به مواضع علی خامنه‌ای درباره مذاکره با آمریکا گفته بود: حضرت آقا می‌فرمایند شرافتمندانه نیست، خب شرافتمندانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/76359" target="_blank">📅 02:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76357">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vozTAzUl8cs6KeJONHI93svw9zeVUH6g12N8m2MDsBs3RYmiitSjq3tjrr2TE3jJrVgFssc1FAN84rjF_6nQSj0gwEs_S8rAMn1zqKEBHhA8v55pSXfLMIgYIX7RDINY2sHirNBy5q9V7l8ocFKS40o0zfw7Tghujv_wtyFlNGWiUb-MoqKp1kYQeSXCQ0yU8AMHiMPczMIUWhq12dnYomv9tRL-EMTl6pURYe6lqDfM1_AfnvXK7NYh9Me5qq6OnysJ_dQo2rJHPdKVmKh9-0coysl2n-j8LPSMoMY9N-mRJosY1gTEOKLYmw03o8P7GzggAGZAvpUH5b_Eqh9-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TYvmA788HXnB3WNJRnD1L0JVQE6N8YqfMej46YDYvlPsuEvoA0Fatxg2mUx5Zg5DOcl-99gZZnzZiS0frES3E982ADSVlOZ7aztrGtKXG3hUat2Qz4MGNT3DFBS9uZMOH3S6E4EK1cH95G0kunBac_BvJkA0GGo1ubuIgugUWFWeNUuLCu3u0s9RcqjVICTemYGOTmXLTOYr8y93mArOG9J_za4po3Vs3JyVu63bOC-sDlGvvA7aYmHVsFbr5_C3t7vmLw9Riy_0sqbLOYnoESvCttCFaC04p1f0xdWZVPHzsRLC2enPIWbi9H0DOJIbE4yPJZnPqpS0MaVl23i7bA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کی‌یر استارمر، نخست‌وزیر بریتانیا، اعلام کرد که از توافق اعلام‌شده میان آمریکا و حکومت ایران «به گرمی استقبال می‌کند» و آن را «گامی بسیار مهم رو به جلو برای پایان دادن به جنگ، تضمین ثبات منطقه و بازگشایی تنگه هرمز» توصیف کرد.
استارمر در بیانیه‌ای که روز یکشنبه در شبکه‌های اجتماعی منتشر کرد، افزود: «ما آماده‌ایم از گفت‌وگوهای فنی که اکنون آغاز خواهد شد حمایت کنیم. اولویت ما این است که این توافق به صلحی پایدار و ماندگار تبدیل شود و برای تحقق این هدف با شرکای بین‌المللی همکاری خواهیم کرد.»
او گفت حمایت بریتانیا می‌تواند، در صورت نیاز، شامل «راه‌اندازی ماموریت دفاعی، مستقل و چندجانبه‌ای باشد که بریتانیا و فرانسه تاکنون نقش پیشرو در برنامه‌ریزی آن داشته‌اند؛ به‌ویژه برای ارائه کمک در زمینه پاکسازی مین‌ها» در تنگه هرمز.
نخست‌وزیر بریتانیا همچنین تاکید کرد: «موضع قاطع و دیرینه بریتانیا همچنان این است که ایران هرگز نباید به سلاح هسته‌ای دست یابد.»
@
VahidOOnLine
امانوئل مکرون، رئیس‌جمهوری فرانسه، بامداد دوشنبه ۲۵ خردادماه در پیامی در شبکه اجتماعی اکس از توافق حاصل‌شده میان واشنگتن وتهران استقبال کرد و خواستار اجرای سریع و کامل آن از سوی همه طرف‌های درگیر شد.
مکرون گفت این توافق باید زمینه بازگشایی فوری و بدون قید و شرط تنگه هرمز را فراهم کند. او افزود ماموریت بین‌المللی ایجادشده با همکاری بریتانیا آماده پشتیبانی از این روند است و ازسرگیری تردد دریایی بدون محدودیت و عوارض، برای ثبات منطقه‌ای و اقتصاد جهانی ضروری است.
رئیس‌جمهوری فرانسه همچنین گفت این توافق می‌تواند راه را برای مذاکراتی گسترده‌تر درباره برنامه هسته‌ای و موشکی ایران و مسائل امنیتی خاورمیانه هموار کند. او تاکید کرد فرانسه آماده است در کنار شرکای خود برای دستیابی به صلحی پایدار در منطقه نقش‌آفرینی کند.
مکرون در بخش دیگری از پیام خود بر حمایت فرانسه از تلاش‌های دولت لبنان برای بازگرداندن حاکمیت کامل این کشور تاکید کرد و گفت برقراری آتش‌بسی پایدار برای تحقق این هدف ضروری است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76357" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76356">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X6xHKov3g_efolBuHX57pAJQUtsSy0ae0YTgLTiGn84MMV7tqFrdRC9Aa4l_Aj9P6o5_oUpFj70IlN3jZq-CTlJJSAggttpPNbOL4YuOj0AwwtkzSkc6BPGiDO7Kn2jg-aRx38nAAxygbD49RlsL3KyFNTe6xG3yhgiEWtcSTP6m2sPR49bCGROa26uyEsYuAmge_nXDGmmwy1mUsrdc0kZQfcLsrD38KUEVED3v4oe3iXQbxmuNENJYvE5d-WCnpLk0m_UzlYgCBMO_y-S0K1zxyfQNYBl9TGeWMwED05n50NhYsI3s03AsUOJQ6lPhS1-n9HR_ZdRPVg2by7aiVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه معاریو به نقل از منابع اسرائیلی گزارش داد بنیامین نتانیاهو، نخست‌وزیر این کشور، در گفت‌وگو با دونالد ترامپ، رییس‌جمهوری آمریکا، به صراحت اعلام کرد که اسرائیل خود را به بند مربوط به لبنان در توافق میان آمریکا و حکومت ایران متعهد نمی‌داند.
بر اساس این گزارش، نتانیاهو گفت که ارتش اسرائیل از لبنان عقب‌نشینی نخواهد کرد، در مواضع فعلی خود باقی خواهد ماند و به اقدامات خود برای خنثی کردن تهدیدهای حزب‌الله، از جمله نابودی زیرساخت‌های تروریستی و پاسخ به هرگونه حمله علیه اسرائیل، ادامه خواهد داد.
به نوشته معاریو، برداشت منابع اسرائیلی آن است که «توافق احتمالی ایالات متحده با ایران، دست اسرائیل را در عرصه لبنان نخواهد بست. پیام اصلی این است: اسرائیل منافع امنیتی-راهبردی مستقلی در لبنان دارد و قصد دارد بر آن پافشاری کند.»
این روزنامه نوشت: «اکنون باید دید این شفاف‌سازی‌ها — فراتر از تماس تلفنی نتانیاهو و ترامپ — در بوته واقعیت چگونه عمل خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76356" target="_blank">📅 02:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بیانیه دبیرخانه شورای عالی امنیت ملی:
متن یادداشت تفاهم پایان جنگ پس از چند ماه مذاکره فشرده نهایی شده است
جنگ در تمامی جبهه‌ها از جمله لبنان از امشب به صورت فوری و دائمی پایان می‌یابد
متنی که در خبرگزارهای حکومتی منتشر شده:
بیانیه دبیرخانه شورای عالی امنیت ملی درباره توافق پایان جنگ
میان ایران و آمریکا
بسم الله الرحمن الرحیم
به اطلاع ملت شریف ایران می رساند:
▪️
جمهوری اسلامی ایران در پرتو راهبری رهبر شهید خویش، تفوق خود در برابر دشمن امریکایی صهیونی را تکمیل کرده و ذیل تدابیر رهبری عالی قدر نظام (حفظه الله تعالی)، حمایت های آحاد مردم و تلاش مجاهدانه رزمندگان اسلام، به دنبال یک دوره مذاکرات دشوار و فشرده چند ماهه، و بر اساس مصوبه شورایعالی امنیت ملی، متن یادداشت تفاهم در خصوص مذاکرات پایان جنگ (مذاکرات اسلام آباد) را میان ایران و امریکا در شامگاه 24 خرداد ماه، نهایی کرد.
▪️
بر اساس توافقات انجام شده، جنگ و عملیات نظامی در تمامی جبهه ها از جمله لبنان از امشب به صورت فوری و دائمی پایان یافته و به علاوه، محاصره دریایی علیه ایران بلافاصله و به طور کامل خاتمه می‌یابد.
▪️
امضای این یادداشت تفاهم در روز جمعه 29 خرداد به طور رسمی انجام خواهد شد.
▪️
مذاکرات برای توافق نهایی، به پس از اجرای تعهدات طرف مقابل وفق یادداشت تفاهم موکول خواهد شد. جمهوری اسلامی ایران از تلاش های جمهوری اسلامی پاکستان و دولت قطر قدردانی می کند.
والسلام علیکم و رحمت الله و برکاته
دبیرخانه شورای عالی امنیت ملی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76355" target="_blank">📅 02:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=MauoY9FwIx5D1iLgRWf_UMP_EDDu1LZRSaElCJnpmJyeY3RzXWt9YIKEw7pE5uB_dVWAx1mdjH3eQDNaHG8Dyg13H5mdiw-37RFco5XuAgmAmTxNjBJ7wKpITl5SllZgnNm24OhPGd5DYExflRU4wT2L61izqE3k67CmQ3s5DhBS3isSssCBZox4gMRv7g6J5b1mIF9cznQER5gCwqMf7BuomVWVfZc-6I4Gk2VPLy_5uOLDp7VW7ioZbkLVCkVIfrz2y3pZugFfduaiBElx5nQWL-uTOg_uwNj7QIZ3LVZFm3e_DscAZ6N1c-MKtshSlpUUc_C65oiMCdYxDXP9wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8a76f7084c.mp4?token=MauoY9FwIx5D1iLgRWf_UMP_EDDu1LZRSaElCJnpmJyeY3RzXWt9YIKEw7pE5uB_dVWAx1mdjH3eQDNaHG8Dyg13H5mdiw-37RFco5XuAgmAmTxNjBJ7wKpITl5SllZgnNm24OhPGd5DYExflRU4wT2L61izqE3k67CmQ3s5DhBS3isSssCBZox4gMRv7g6J5b1mIF9cznQER5gCwqMf7BuomVWVfZc-6I4Gk2VPLy_5uOLDp7VW7ioZbkLVCkVIfrz2y3pZugFfduaiBElx5nQWL-uTOg_uwNj7QIZ3LVZFm3e_DscAZ6N1c-MKtshSlpUUc_C65oiMCdYxDXP9wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری فارس:
‌غریب‌آبادی، معاون وزیر خارجه: در مذاکرات ۶۰ روزه در مورد چند موضوع بحث خواهیم کرد:
🔸
۱. خاتمه تمام تحریم‌ها و قطعنامه‌های شورای امنیت
🔸
۲. موضوعات هسته‌ای
🔸
۳. تعیین سازوکار نهایی بازسازی ایران
🔸
۴. تعیین سازوکار اجرایی برای نظارت بر تعهدات طرفین
خبرگزاری مهر:
جزئیات جدید از پیش‌نویس تفاهمنامه ۱۴ ماده ای ایران و آمریکا
جزییات این پیش‌نویس به شرح ذیل است:
۱- توقف دائمی و فوری جنگ در همه جبهه ها از جمله لبنان
۲- تعهد آمریکا به عدم مداخله در امور داخلی ایران و احترام به حاکمیت جمهوری اسلامی ایران.
۳- رفع کامل محاصره دریایی ظرف ۳۰ روز
۴- تعهد آمریکا به خروج نیروهایش از پیرامون ایران
۵- بازگشایی تنگه هرمز ظرف ۳۰ روز با ترتیبات ایرانی
۶- تعلیق تحریم های فروش نفت، محصولات پتروشیمی و مشتقات و دسترسی کامل ایران به منابع مالی آن.
۷- لزوم ارائه طرح های بازسازی ایران حداقل به مبلغ ۳۰۰ میلیارد دلار توسط آمریکا و متحدانش
۸- ۶۰ روز مذاکره برای رسیدن به توافق نهایی مبتنی بر موضوعات هسته ای و لغو کامل تحریم های اولیه، ثانویه، آمریکا و قطعنامه های شورای امنیت سازمان ملل و شورای حکام آژانس بین المللی انرژی اتمی
۹- تکرار تعهد ایران در پیمان ان پی تی مبنی بر عدم تولید سلاح هسته ای
۱۰- در دوره مذاکرات آمریکا متعهد شده به نیروهای خود در منطقه اضافه نمی کند و تحریم جدیدی هم وضع نخواهد کرد.
۱۱- آزادسازی ۲۴ میلیارد دلار پول های بلوکه شده ایران در دوره ۶۰ روزه مذاکرات نهایی. نیمی از این مبلغ قبل از شروع مذاکرات باید در دسترس ایران قرار گیرد.
۱۲- تشکیل سازوکار نظارتی برای اجرایی کردن توافق.
۱۳- توافق نامه نهایی توسط قطعنامه شورای امنیت سازمان ملل به تایید می رسد.
۱۴- مذاکره نهایی قبل از آزادسازی نیمی از پول های بلوکه شده ایران، تعلیق تحریم های نفتی ایران و رفع محاصره دریایی آغاز نمی شود و توافق نهایی صرفا در موضوع سرنوشت مواد غنی شده و غنی سازی، رفع تحریم ها، برنامه بازسازی اقتصاد ایران انجام می شود و بحث درباره برنامه موشکی ایران و حمایت از گروه های مقاومت به صورت قطعی از دستور کار خارج شده است/مهر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76354" target="_blank">📅 02:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76353">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eRerCYSjFrOnSuSqlLLmE3oy0j8mufaSp9wlIfLbsisbaLWKVCZb6LFp2eo_N0CbX-ZvlnoCUc660inUNEqXGFcpEa400A1S8a6HsStKKn8nM4L4MQ1zmM4T0ocUZ6AHNi85uuZEqZqLsPkj7cTJAune9Ow_9bAsL3GOB7sUl143JmRcSPOB9-ug19GTulIBGsbSKBgrzchrHd9xbreLsU3SGnibRpsUOBndbg4Sy9gnh-v-xCRBjbYAoHs2bj-KzdjlCybDS4lEGD87nutIXqnq3Y53As2qQmUkOt3jAHV2ZaBzxZnw_Osm5eF-KxR1_h1GVcyexAUHN75RuLIz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تنگه هرمز جمعه پس از امضا باز می‌شود
روسای جمهور پیش از من در رسیدن به صلح با ایران شکست خورده بودند
پست ترامپ، ترجمه ماشین:
این توافق بزرگ، صلح و امنیت را برای کل منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همه پیش از من شکست خوردند. رهبران منطقه، برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آن‌ها کمک کند به صلح واقعی دست پیدا کنند.
با باز شدن تنگه پس از امضای توافق در روز جمعه، برای مقاصد مربوط به پاک‌سازی مین‌ها، نفت دوباره از هر دو سوی آن برای منطقه و جهان جریان خواهد یافت!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76353" target="_blank">📅 02:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=kXnDzHGWAyz55k9a1FmlGG1TCLD0ZOV5lY7Vyoo-AoSO3J_DrvbSY9wbS9QSf23rh_8PxdxkQBbB-d4Euy_mox1bghodDMv5yBPO_ImDb_f9w33R-9m7nEs-hCS5lj70T2PvSdwbqGlIjJBRTQKQIrlQ-iVCqOGYgmmroy2A5mC_LMdird0TSzByA4IWCoss-x6xIvlKuv4FsW4z8ADTaW4vzZGh_J3SVwG5exvTz-yefSBHghYkPceA-InSTNU7RalYAQwR9KZ2HpAWxPhXSCT9dwIEiUYlSHKQhSu3Lgtkx4Bqai6ndrpnCIarPxfhUHOBRgJmXV6OTJGIu6TkMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/da696e6ada.mp4?token=kXnDzHGWAyz55k9a1FmlGG1TCLD0ZOV5lY7Vyoo-AoSO3J_DrvbSY9wbS9QSf23rh_8PxdxkQBbB-d4Euy_mox1bghodDMv5yBPO_ImDb_f9w33R-9m7nEs-hCS5lj70T2PvSdwbqGlIjJBRTQKQIrlQ-iVCqOGYgmmroy2A5mC_LMdird0TSzByA4IWCoss-x6xIvlKuv4FsW4z8ADTaW4vzZGh_J3SVwG5exvTz-yefSBHghYkPceA-InSTNU7RalYAQwR9KZ2HpAWxPhXSCT9dwIEiUYlSHKQhSu3Lgtkx4Bqai6ndrpnCIarPxfhUHOBRgJmXV6OTJGIu6TkMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، به شبکه خبری فاکس گفت: «بر اساس توافق حاصل‌شده میان واشینگتن و تهران، ایران به طور دائمی از دستیابی به سلاح هسته‌ای منع خواهد شد.»
او افزود: «تنگه هرمز بلافاصله بازگشایی می‌شود و محاصره دریایی آمریکا پایان خواهد یافت.»
به گفته معاون رییس‌جمهوری آمریکا، با اجرای این توافق، زمینه برای سرمایه‌گذاری‌های گسترده در منطقه فراهم خواهد شد.
ونس در عین حال تاکید کرد اجرای این توافق به پایبندی جمهوری اسلامی به تعهداتش بستگی دارد.
@
VahidOOnLine
جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت قصد دارد در مراسم رسمی امضای یادداشت تفاهم میان آمریکا و جمهوری اسلامی حضور داشته باشد، اما احتمال دارد دونالد ترامپ نیز شخصا در این مراسم شرکت کند.
ونس در گفت‌وگویی کوتاه با شبکه فاکس نیوز گفت: «فکر می‌کنم هنوز در حال بررسی جزییات و هماهنگی‌ها درباره افرادی هستیم که در مراسم امضا حضور خواهند داشت. من قطعا قصد دارم در آنجا باشم، اما این احتمال وجود دارد که خود رییس‌جمهوری نیز در مراسم حضور پیدا کند.»
سرویس مخفی آمریکا معمولا حضور همزمان رییس‌جمهوری و معاون رییس‌جمهوری را، به‌ویژه در سفرهای خارجی، به دلایل امنیتی و ملاحظات جانشینی توصیه نمی‌کند.
این اظهارات ساعاتی پس از آن مطرح شد که شهباز شریف، نخست‌وزیر پاکستان، از برگزاری مراسم رسمی امضای توافق میان آمریکا و جمهوری اسلامی در روز جمعه در ژنو سوئیس خبر داد.
قرار است دونالد ترامپ پیش از آن برای شرکت در نشست سالانه گروه هفت به فرانسه سفر کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76352" target="_blank">📅 01:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76351">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22e031404e.mp4?token=JYHoinJQE6iMbuuWGGC3ZyahQ9A4E2CHnlkt0CTWp29kwzbyNyE-9QYR37CtWdeBbnSwC-YUvMXfQ6TO4fXysF_FWGORMaijrJecqM_K3YIwQCBlRgkaqVMmyudaVOQPhHiUxbOG_W2c82t-jpeZkJNU7baH2alfXzeTOrFEdV3_fzUXKMDiKEsgK9h67Kgv3bYvAxQ1JiRWwRhMuhMRyRjMdzypYanUwx4gQh5l4uiZ3VHxpbWWP4YtRANlXMGFLkaBWvmys4yoEdrA_fsJqchefRscKahuZhP8uKAN7tLZAx-Nn82xjNJKDIbbCL6zhcriAH_pKmc6enXtrHWmYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22e031404e.mp4?token=JYHoinJQE6iMbuuWGGC3ZyahQ9A4E2CHnlkt0CTWp29kwzbyNyE-9QYR37CtWdeBbnSwC-YUvMXfQ6TO4fXysF_FWGORMaijrJecqM_K3YIwQCBlRgkaqVMmyudaVOQPhHiUxbOG_W2c82t-jpeZkJNU7baH2alfXzeTOrFEdV3_fzUXKMDiKEsgK9h67Kgv3bYvAxQ1JiRWwRhMuhMRyRjMdzypYanUwx4gQh5l4uiZ3VHxpbWWP4YtRANlXMGFLkaBWvmys4yoEdrA_fsJqchefRscKahuZhP8uKAN7tLZAx-Nn82xjNJKDIbbCL6zhcriAH_pKmc6enXtrHWmYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر توافق و توقف جنگ در شبکه خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76351" target="_blank">📅 01:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MLEfzljjUiQj1mrPFq_UxIE7Zrbep7-VarUlSfYEkiSBTYxQwvJs5FTqfk8hnhif3WQ7znFL1v6m-DX42FD5tX-qL4WLSdGMlKtV6bJOfmAV_EQPgVhEWHLrv_uTnl8uvMUZQlCqW5YroPnn1Y_gfjZzYMncV47E2I-4y_uw2D9Jyip2yM0XW36dylixPbqwa0Qwb1l_CVJmCC9T8hzO6re59tKW0vH1kuBQ5CULfaUEIQi0FooZL2s9vbyVoYNmZARYnEFBTefGlQ0KGjLWJ78clVnAEMeP91OvL0MAbteSUB8UAmSWsgOcbFTQk6U7vs-mychXa79LjFm0iFsclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: تبریک به همه، توافق نهایی شد
پست ترامپ ترجمه ماشین:
توافق با جمهوری اسلامی ایران اکنون کامل شده است. به همه تبریک می‌گویم!
بدین‌وسیله من به‌طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را صادر می‌کنم و هم‌زمان با این، مجوز برداشته شدن فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جریان پیدا کند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76350" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqvbVrfZjkqNG7hlQpgTwRFYvyAOF93ufLU1Ro_aR6sVgd518bQPXXRIvHJt9AF1lH2Bu_-F7EOzQinSYm0rypHtPFhnpR8p-WEROmDYCqkPGSY5apPOXiEdfYc68uc97NA2sje3n8xXq_ZT9DvDDoo-p-ibNQCooGeTZm2C3xjzc201KLpkAo8_YKy_ns-_tWglfdzPltmwwoLkckYmYCRtsNliHqkBw_FRjO-tR-GH3o0X5XEH6IA5yj8WW6Nsjdk4UY8MC0gPluKARfadCpbflKvpiv4zDqeX9IKbmLnRYpy4vIoxqJCIvsWuLWq6mcBuMrttWe5v5-2gjdgNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبر:
نخست‌وزیر پاکستان از دستیابی به توافق و پایان جنگ خبر داد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76349" target="_blank">📅 00:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QLc5wGGEj6CP3DTmV_5l26_LxSWTNUvTCCj5kPI5U-DM_xhtoH_V6649RXCfKoMMw39G-IRT19Fj58gMecffoawhQ119olGRkMsX7mhY3lD2FTIq9K1j1I7l7xIDeX3TOjFIBa3KiO1LrEkWZvoQOD8Sji5bvh8126waoz-lkiKGwXYU8zvmDvoTaLZ_aVv_E4et5ImXZcuubgoTe2776GfNqCLNNZUVDl4_u0YIF5gxOkbsFfXzYOuVXgZVgBzo6TkDxIYAoerWl9h7vSNRaq7iUQZGoyPzFf2_FDCj_PfbLegzd4P9s_hrO8sGBUmVoQ_vq7EDby1jAidP6Ah_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
نخست‌وزیر پاکستان: توافق حاصل شد
مراسم امضا جمعه در سوئیس امضا می‌شود
پست شهباز شریف، ترجمه ماشین:
در پی مذاکرات فشرده، خوشحالیم اعلام کنیم که توافق صلح میان ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف پایان فوری و دائمی عملیات نظامی در همه جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق روز جمعه، ۱۹ ژوئن، [۲۹ خرداد] در سوئیس برگزار خواهد شد.
مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به‌خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این مناقشه تشکر کنیم. همچنین مایلیم قدردانی صمیمانه خود را از برادرانمان در این تلاش میانجی‌گرانه، رهبری بزرگ دولت قطر، به‌خاطر حمایتشان در دستیابی به این توافق ابراز کنیم. به‌ویژه از رهبری دوراندیش پادشاهی عربستان سعودی و جمهوری ترکیه نیز به‌خاطر مشارکت‌های عظیمشان در این زمینه تشکر می‌کنم.
اکنون که توافق برقرار شده است، میانجی‌ها مجموعه‌ای از نشست‌ها را در این هفته تسهیل خواهند کرد. این گفت‌وگوهای پیش از اجرا، زمینه را برای مذاکرات فنی و مراسم رسمی امضا فراهم خواهد کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76348" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=WLbpjFHmMcC-GFbZQQ3hPJ1H8dRNuSGUl5aD41lQLr7Cdso6xMDccNPdfd5TINwsM38QQ1KeERQ_MT432r_XUsrs1aL03RYz1kJJNoQ-ZDdlQIAl6ppgjQs9aqJN9JemkTe2N5vFJZtCFVDOPiZxgIVhOmb0OMl0aemJIoAzRQxnuyT3-kSN8VthttWNq54tPUdxz8bQfORJyMIBSd_BQNv49NyN-2x7Fo4aahZDCX83-YuUwdHbJPrQbOHPlpL66eI8CBfxMzp2dj1qX-JMBZcO8eZsfv63W0-ak9pkfDnIrUzNgsgQTqea2Jz4qVI_GUxTV4Ii5GRllg5lqHpBQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb9bbe1383.mp4?token=WLbpjFHmMcC-GFbZQQ3hPJ1H8dRNuSGUl5aD41lQLr7Cdso6xMDccNPdfd5TINwsM38QQ1KeERQ_MT432r_XUsrs1aL03RYz1kJJNoQ-ZDdlQIAl6ppgjQs9aqJN9JemkTe2N5vFJZtCFVDOPiZxgIVhOmb0OMl0aemJIoAzRQxnuyT3-kSN8VthttWNq54tPUdxz8bQfORJyMIBSd_BQNv49NyN-2x7Fo4aahZDCX83-YuUwdHbJPrQbOHPlpL66eI8CBfxMzp2dj1qX-JMBZcO8eZsfv63W0-ak9pkfDnIrUzNgsgQTqea2Jz4qVI_GUxTV4Ii5GRllg5lqHpBQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده در شبکه‌های اجتماعی نشان می‌دهد جمعی از حامیان تندروی جمهوری اسلامی کفن‌پوش شده و در تجمعی مقابل استانداری زنجان شعار «اگر چیزی امضا شه، مسئول باید کشته شه» سر دادند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76347" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kR2gHkOOnqRmlflG-xGvlErPErhw1IQ8dokcXmOkvTnN-uCwvNgzHLlhyHgCmgZ1NKo17l8Brr8HPkhxYxByhhP5Td3jkzB93V3krJbmdqbNs4eoaakqlBu8fkrmPlYfi1Rch0DJnTnLitmfkHZJ6VVrONkswhPleUq3f73cUv5DzMN3xFMUaKjj-zqMRlK9XqZpAbDicyeE75pQQWUkkpR2PatWshrJVyvzc_POIKpm2s6V0XIzW-_yHUKmoPH_Qf02_FPjwZA3FigSJxUr8oLevOLsDFL0xTDNMKdhZFp5J_DFkFQ9bsE0dvEas94y8_n-jaiwcuYNKUm1Yfdhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با
وال استریت ژورنال
گفت توافق با جمهوری اسلامی قریب‌الوقوع است، اما تهران هنوز موافقت خود با آن را تایید نکرده است.
ترامپ افزود قصد دارد به‌زودی بیانیه‌ای صادر کند که در آن اعلام خواهد شد آمریکا با جمهوری اسلامی به توافق رسیده است.
او گفت این توافق، در صورت نهایی شدن، یا توسط خود او یا از سوی جی‌دی ونس، معاون رییس‌جمهوری آمریکا، به‌صورت الکترونیکی امضا خواهد شد.
رییس‌جمهوری آمریکا روز یکشنبه این توافق را گامی بزرگ در مسیر پایان دادن به درگیری نزدیک به چهارماهه توصیف کرد.
ترامپ همچنین گفت این توافق شامل تعهد جمهوری اسلامی به دست نیافتن به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود. او افزود عجله‌ای برای خارج کردن مواد هسته‌ای از ایران وجود ندارد و این موضوع می‌تواند در مرحله‌ای بعدی دنبال شود.
ترامپ گفت: «بعدا و زمانی که آماده باشیم وارد عمل شویم، مواد هسته‌ای را جمع‌آوری خواهیم کرد. به نظرم طی یک یا دو ماه آینده این کار انجام می‌شود و عجله‌ای وجود ندارد.»
@
VahidOOnLine
نقل خبرگزاری فارس:
ترامپ: به‌زودی بیانیه‌ای صادر خواهم کرد که تایید می‌کند آمریکا با توافق با ایران موافقت کرده است
🔹
این توافق به‌صورت الکترونیکی، یا توسط من یا توسط معاونم ونس امضا خواهد شد.
🔹
توافق شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای و بازگشایی فوری تنگه هرمز خواهد بود.
🔹
ایران هنوز موافقت خود با این توافق را تایید نکرده است.
🔹
هر زمان که آماده باشیم، مواد هسته‌ای را تحویل خواهیم گرفت و این اتفاق ظرف یک یا دو ماه آینده رخ خواهد داد.
🔹
من خواهان پایان یافتن حملات هستم و ایرانی‌ها هم می‌خواهند که جنگ تمام شود.
🔹
من هیچ‌وقت به دنبال تغییر رژیم ایران نبوده‌ام.
🔹
بازرسی‌های بسیار دقیق و شدیدی از ایرانی‌ها به عمل خواهد آمد.
🔹
در این توافق پولی به ایران داده نخواهد شد، اما احتمالاً تحریم‌ها لغو می‌شوند؛ باید ببینیم در عمل چگونه رفتار خواهند کرد.
🔹
محاصره دریایی اعمال‌شده علیه ایران موفقیت‌آمیز بوده و تاثیر آن از حملات نظامی هم بیشتر است.
🔹
نتانیاهو از این توافق حمایت می‌کند؛ این توافق برای او خوب است چون تحت هیچ شرایطی اجازه نمی‌دهد ایران به سلاح هسته‌ای دست پیدا کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76346" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZcCE0zcZiIfa1wZQ4x0ExJ1qGL3tAE2S8UhWbjc0geg9-EvxHFhZHN-YZcxsrEfqGiErQEgU-Kq63ytKO9Yg1t00x7HkgOGNasjo9WfHPClPXMTtitaXLUrr3RRi5Ok8MzkV_n5tLGvAcUo8xJj31O-zJUBaIRNZDHm4wze2M-dRJed2yp-FamvYAaAMn5cGF_Ljp55y0E2w-XlpZ5H_AfR63X5Fn1pAvvDWaRV4PdaBM8H6C0W6LVb-2NVJKpd2VvW4DRzKjOCsPIAhtLxvrMg8RNlFUUuqsbtWeD92GO_K_Nz86tSRs25HYEJi5yv6lMUBU71t0BJW1CD-COdL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «کانال ۱۲» اسرائیل، بنیامین نتانیاهو و دونالد ترامپ لحظاتی پیش به صورت تلفنی گفتگو کردند و رئیس‌جمهوری آمریکا، نخست‌وزیر اسرائیل را در جریان «پیشرفت‌های کلیدی برای امضای توافق با ایران» قرار داد.
مقامی ارشد اعلام کرده که احتمال امضای این توافق «حتی طی همین امشب» (بامداد دوشنبه به وقت تهران) وجود دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76345" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
سناتور جک رید، یک «دموکرات» از رود آیلند، وقتی گفت توافقی که ما همین حالا انجام دادیم به خوبی فاجعه اوباما، معروف به برجام، نیست، دروغ گفت.
رید یا یک کلاهبردار تمام‌عیار است یا بی‌کفایت.
توافق اوباما مسیری به سوی سلاح هسته‌ای برای ایران بود، همراه با پول نقد و همه چیز؛ یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا به حال انجام داده است؛ به همین دلیل هم می‌گویم «دموکرات‌های احمق»!
توافق ما دیواری در برابر دستیابی ایران به سلاح هسته‌ای است؛ درست نقطه مقابل اوباما.
جک رید را استیضاح کنید!
(توضیح ماشین: در متن اصلی چند غلط املایی عمدی هست: Dumocrats به‌جای Democrats برای تحقیر دموکرات‌ها و Obuma به‌جای Obama.)
realDonaldTrum
ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او موضوع را مثل تعداد کمی از دیگران می‌فهمد. متشکرم ویکتوریا.
ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز هم به‌زودی برای تجارت باز خواهد شد!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/76344" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XBoJFEOhdjjIhA-vc3geTSeB1vo2S85umXiidi4MG15imBmPcXhovRgPZ4mjiRb74cgUgfED_6o0nZn22h8kZuz1P0fXf2KwMP_r1711JsEI1BinZseKClRGzn4RIBPdoutXsH0EvNTpkil9eJ-z0V5Z6DxpvCw3mKxNhZzk_R5x-8tlkStQeC1baz7u5-QgbVIXTsRov7jHatXldXCy7PTqWo83OqXlZYZptjLOc-7G6zhZ8PMAIQR0EJQRWSorl0e8evEzD26gJxx-OPdhDIwD5s6OY2X4Pcfox-gSaXK1-CRHttfU823GLRgeOCUvAQ7535TZK5TlGgPM9Yeg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی، در واکنش به حمله اسرائیل به اهدافی در جنوب بیروت در
شبکه ایکس
نوشت: «مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی حاکمیت و تمامیت ارضی لبنان را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.»
قالیباف تاکید کرد که هیچ‌یک از ارکان مقاومت را نمی‌توان «تک و تنها» قرار داد و حاکمیت و تمامیت ارضی لبنان حفظ خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76343" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lKKwDE8DTEZ7SEeq8LV30ETp4Avp4ee5z4ZvhAv6OyNaA-Wxte-2q-rmEqEavGuwDhxvsm15eD3_jtOP2x4FI7AOdMXN60ZifZpJzcu2HbpL8ZJ0ZqhFQLpM-Yg6VoqZNaKo3VqkmpXd0ay1UTULHGjgI1rnhLUIaOB7FuqOZC7H0350TOkx0jgC9k-eGgnseETeSPILXo0bciX2G8LFJyDdxJX14BiCMcLO-C1bF7T8uqIvTNu3weG1VWU3vhuKc8h9s_MbXE4RlwKCk93qymEATva2sjOpG5C1c8opk-dKgRCwDikCHuQJ6CrC1W0Fppn_S4dbOT9s2tRhMt0lsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم و صدا و سیما:
پروازهای فرودگاه‌های غرب کشور تا اطلاع ثانوی لغو شده است.
این تصمیم در پی شرایط موجود اتخاذ شده است.
سازمان هواپیمایی تا این لحظه هیچ نوتامی منتشر نکرده است.
خبرگزاری مهر:
هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
🔺
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
🔺
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/76342" target="_blank">📅 22:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=DmjW9U2PhDv2KVX-ffu8yHGNeEKe_SsdZ3VKfJEDUVQJZcfQ0T5a5yEDnzE6zzjmMBJhd6rfuaCh2HSWZjMKnvt8RT0LrofE9_A38pnUCp86Zxd0mVSm3kM4cLUKYXf2DJr5-xaC8qgVRzc8XD9gGQnYsbSwMtteYBifaWpLiB5PNRL6tlloEsCGw7crtWyLOKP4xQTb_Nqi0X7TlCiZgf2SY_g8nFo-EilVJjz8448T1IUswazB0j23hxl0zYmZQzZhXQxsAH1TwlzBTnLykqhsnLEFdQ3Eo_1YLenVfTU-rNT-NF-s3t6XFW7rvhZjAzKIAX0FBIs-cs3ePThoJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/201a6972d8.mp4?token=DmjW9U2PhDv2KVX-ffu8yHGNeEKe_SsdZ3VKfJEDUVQJZcfQ0T5a5yEDnzE6zzjmMBJhd6rfuaCh2HSWZjMKnvt8RT0LrofE9_A38pnUCp86Zxd0mVSm3kM4cLUKYXf2DJr5-xaC8qgVRzc8XD9gGQnYsbSwMtteYBifaWpLiB5PNRL6tlloEsCGw7crtWyLOKP4xQTb_Nqi0X7TlCiZgf2SY_g8nFo-EilVJjz8448T1IUswazB0j23hxl0zYmZQzZhXQxsAH1TwlzBTnLykqhsnLEFdQ3Eo_1YLenVfTU-rNT-NF-s3t6XFW7rvhZjAzKIAX0FBIs-cs3ePThoJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شماری از حامیان جمهوری اسلامی و مخالفان توافق با ایالات متحده، در تجمع خود با سر دادن شعار خواهان اعدام عباس عراقچی، وزیر خارجه حکومت ایران شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76341" target="_blank">📅 21:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dq1IuVKHhpb2bY9mHtvGZ5q0sdftsjqwGHoZ1u1UQFrtUipQ1AFU8SPQKvMs6jJSkgBSbe3AF6hX37eJhUbc0m9FeajsLj4MfrvCubkZdPkde0c9dst7Mm9T6-4azH1fH54nZqn8cgDeXSLF9fM06l3SHODAk5FyCnBXwMsvaiVP-dF1yh7Yr_XwblGfH_o2vRFdaNrCVDJZxCzFuUIN6TBJd5kW30agth0pjFSalAK9Y6xw84vRP5KRlo6IdGBVqUc0zitSQ7lZjil1FiV517iUvVCpFPGYjIAYM2wBqg5OM4lZQAG1QrGPCOmzjbziuRSxmympAQbeBf1CP3H7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"‏پاسخ رزمندگان اسلام در پیش است."
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی در جمهوری اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/76340" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TnHynk2_6XwzJ8N4_ezrQXTaSaEmX59zD5zNllg_m99wtTUWPMXsRMzTS3HtU5fnVO7BKBKzIEzUfGMiI0GO_EzAsMwlhbHk3133oKd3TJB_aWH--1NlUHOrKgTH-r5axFKitScS_SIz4CndnrnrdOMtTphMCWf3gm4sKULDNzolKI0ff3ksqefq1Z3AycEXTOXnmprvYsCKmDEkXubIreb72Y2i_ZtBH76ah_6xGMtrLNU3EZ_P0OXaSd2Mg1wI2itHFeY5MTjlHrbfejq4mHjsxIQaQ5ggrHgLkUNOINyVLvN2FHAeijtyuS_M7D3XMLIZYw7vy1r2uM8bZqZh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب تصاویر #مجتبی خامنه‌ای و آدولف #هیتلر با هم عکس جعلی چهره رهبر جدید جمهوری اسلامی (دستکاری شده با هوش مصنوعی) رو با استناد و افتخار به سخنان جعلی و چرندیات هرگز گفته نشده آن جنایتکار دیگر منتشر می‌کنند. عکس دریافتی از بابلسر، سه‌شنبه ۴ فروردین Vahid
📡
…</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76339" target="_blank">📅 20:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX5uMtWOS0pn63MxUCQmk-zIvHLb-x9ryCPBHZ6PzzwSJDcS7dH4fmNgdBAx77PBGTUN2TiCGcsGXCsrrCxg8QGXIEdi9x3ic6dUqz2bWj8Kh1dRfYaFbwCU-kR1aXKCi9ObpHjW2pmdNRrLZGDJJT6se4jJ9v49hljEvdQqlElJ81MKhvpTl5CadnNT_INg0E4_8z9TSO9Cu1SNftfwE6-POm5BZy1nsXqSRNJeVcydSINVhqUkpodgZ19gNbyx-Gg3p_kU6TVH1qV2iSdguJafTDSbAZ9qtItv2ib2tQd3bdt7YZ-41aQrBsREA61gz8aNJpIoD71UCn--8AB3Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، در پی انتقادات برخی حامیان حکومت از محتوای توافق احتمالی با آمریکا، روز یکشنبه گفت که روند مذاکرات بر اساس مصوبات شورای عالی امنیت ملی و دیدگاه‌های رهبر جمهوری اسلامی پیش می‌رود.
او در دیدار با مدیران رسانه‌های داخلی افزود: «تصمیمات راهبردی کشور باید در چارچوب سازوکارهای قانونی اتخاذ شود و همه جریان‌ها و گروه‌ها نیز خود را ملزم به تبعیت از این تصمیمات بدانند.»
در آستانهٔ امضای تفاهم‌نامهٔ ایران و آمریکا برای پایان جنگ، اعتراض‌ در میان حامیان تندروی حکومت به متنی که به‌عنوان تفاهم‌نامه در برخی رسانه‌ها منتشر شد بالا گرفته و تجمعاتی نیز توسط گروهی از طرفداران جمهوری اسلامی علیه این تفاهم و مذاکره‌کنندگان برگزار شده است.
در یکی از این تجمعات در تهران، تجمع‌کنندگان علیه عباس عراقچی، وزیر خارجه، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، شعارهایی سر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76338" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c24456e9d.mp4?token=XezPAbczhkLb_c0Z6Cv1hXUz0mcLW0ZNjj5npyZewshNIX32VBr52mOJuZEhRxysFwZggOCg0Cwxv-vs56_L_LXpCvDfdiT6wxsOBKokJyBJJLrxz-3Md2aH1Q_r66JDHGyacrMy58-AcPvJ8RQyZJbciglbf-kss_XmxFD7BdV_R9MjEJX7MJEjjbCVhERvERNRyAV9md_pubKVtLw9t63HCC-pVkdbS_7vL1Da12svwu0rJRmvx7r1s-DJs2V2If7LQ_6Hvcrt6Kkb-6fHK8YGnUyS9vkK96gFsNls7pRKra2042B3dUDxVHw98fBtwaLIfe-5ODtDsmVqY0znqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c24456e9d.mp4?token=XezPAbczhkLb_c0Z6Cv1hXUz0mcLW0ZNjj5npyZewshNIX32VBr52mOJuZEhRxysFwZggOCg0Cwxv-vs56_L_LXpCvDfdiT6wxsOBKokJyBJJLrxz-3Md2aH1Q_r66JDHGyacrMy58-AcPvJ8RQyZJbciglbf-kss_XmxFD7BdV_R9MjEJX7MJEjjbCVhERvERNRyAV9md_pubKVtLw9t63HCC-pVkdbS_7vL1Da12svwu0rJRmvx7r1s-DJs2V2If7LQ_6Hvcrt6Kkb-6fHK8YGnUyS9vkK96gFsNls7pRKra2042B3dUDxVHw98fBtwaLIfe-5ODtDsmVqY0znqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: به نتانیاهو گفتم داری چه غلطی می‌کنی؟
ظرف دو سه ساعت آینده یک توافق بزرگ امضا خواهد شد
به ویدیوی بالا با هوش مصنوعی زیرنویس فارسی اضافه شده، متن دو دقیقه اولش:
«بله کوین، عصر بخیر. همین الان با رئیس‌جمهور ترامپ صحبت کردم. او به فاکس‌نیوز گفت که معتقد است یک توافق بزرگ با ایران ظرف دو تا سه ساعت آینده امضا خواهد شد.
از او درباره حملات امروز اسرائیل علیه حزب‌الله در پایتخت لبنان، بیروت، پرسیدم. او گفت با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، تلفنی صحبت کرده و از او پرسیده: “داری چه غلطی می‌کنی؟” ترامپ گفت به نخست‌وزیر گفته بود این حملات علیه حزب‌الله را انجام ندهد تا بر پیشبرد این توافق اثر نگذارد.
اکنون اسرائیلی‌ها، به گفته ارتش اسرائیل، خود را برای احتمال شلیک موشک‌های بالستیک ورودی از سوی ایران آماده می‌کنند. رئیس‌جمهور ترامپ به فاکس‌نیوز گفت از ایران خواهد خواست با شلیک موشک به سوی اسرائیل پاسخ ندهد، چون این توافق در آستانه امضا قرار دارد و انتظار می‌رود امشب امضا شود.
همه اینها در پس‌زمینه تازه‌ترین گفت‌وگوها برای رساندن این توافق نهایی به خط پایان رخ می‌دهد. رئیس‌جمهور درباره حملات میانه هفته گذشته هم صحبت کرد؛ زمانی که آمریکا بسیاری از مواضع ایران را زیر ضربه می‌برد و ایرانی‌ها را به میز مذاکره برمی‌گرداند.
شاید یادتان باشد، کوین، من با رئیس‌جمهور تلفنی صحبت می‌کردم، در حالی که او در اتاق وضعیت بود، و ایرانی‌ها با او تماس گرفتند و از او خواستند بمباران را متوقف کند. رئیس‌جمهور معتقد است همان لحظه توانست معادله را تغییر دهد و دوباره ایرانی‌ها را وادار کند این امتیازها را بدهند.
رئیس‌جمهور ترامپ گفت اگر آنها امشب توافق را امضا کنند، او فوراً دستور خواهد داد محاصره بنادر ایران برداشته شود و سپس وارد گفت‌وگوهای جزئی‌تر درباره برنامه هسته‌ای ایران خواهند شد.
اما دوباره، مهم‌ترین خبرهایی که اکنون می‌دانیم این است:
رئیس‌جمهور ترامپ به فاکس‌نیوز گفته معتقد است توافق با ایران ظرف دو تا سه ساعت آینده امضا خواهد شد. به گفته رئیس‌جمهور، این امضا به‌صورت الکترونیکی انجام می‌شود و حدود یک هفته بعد انتظار می‌رود مراسم امضای حضوری، احتمالاً در جایی در اروپا، برگزار شود.
باز هم تأکید می‌کنم: رئیس‌جمهور پس از حملات امروز اسرائیل به پایتخت لبنان، بیروت، واکنش نشان داد. اسرائیلی‌ها در پاسخ به آتش پهپادی این هفته از آن سوی مرز به سمت شمال اسرائیل، مواضع حزب‌الله را هدف قرار دادند. و رئیس‌جمهور می‌گوید از نخست‌وزیر اسرائیل پرسیده: “داری چه غلطی می‌کنی؟”»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76337" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z7rlfU4xNOolwL11oHKH-uwSLQMJYJTsxrn0XgXC33unPh-4qLWvBYXvbiRP4-OGCCQnmniZ-vJtjfnTjFGJ4apBQABUGiscD_NEqH9q9p3TQogZPxKddX2aaIYFOVWXG0Z0cbINDmKahn-dqdpHgN6oQPf_1nD7UivPu2gC6KINnRM6Z4wFP00_DjeLKgAu6MKHIcBn6FT-DHPj2eDrdKXoIVagXNFOVdLRD95O0SIUtor6NcF-8X-QLMNDjRRTuGsb0FAcTjb9-LD2IYGDPT8beuxb7fhkVEaXdVE1J-3gRZ84Sia3PkugUPE37TBTlDz4xblyAxzgzEn-xGaWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجید موسوی، فرمانده نیروی هوافضای سپاه پاسداران، در پیامی از حامیان جمهوری اسلامی خواست در مسیر تحقق آرمان‌های نظام، از مجتبی خامنه‌ای تبعیت کنند.
او نوشت: «ملت بصیر و غیور که در خونخواهی علی خامنه‌ای مبعوث شدید و در راه تحقق آرمان‌های بلند انقلاب اسلامی با مجتبی خامنه‌ای عهدی تازه بستید، هوشیار باشید که از شئون متعهد بودن، تبعیت کردن است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76336" target="_blank">📅 19:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PLyXZZiv6C8sqXhgXpqsEl31oBsp9BphMzDnWNBpKvokWtJ_FtmB_KZjxtnIElCk8DfL3gaaPnhz9WLLVdIUugaINF2stmG4u-u6cAONt92jBcVNUcyPQKAvIPTeoVyssnovBY67-QDCmy4HB3F0GiDr8b49Uf8J2E-pIkF2k_glU_63h5NDg08OMHcTB_Uyej4cfQvtXeYzsgwbOi43fJPR5ezBpEv_CoErQ72LMyEyPjAtCe5aLV_YViBPCwLQ3gOumuKV1NvXwu6mLoHb-qk6RxXUedXXm3IqKkqNWT0LuA7POPOeeIY10Ewoh0QRW27ypEpU8yEtDtpfZyaCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: بیایید خرابش نکنیم!‍
پست ترامپ، ترجمه ماشین:
حمله صبح امروز به بیروت نباید اتفاق می‌افتاد؛ به‌ویژه در روزی خاص که ما تا این اندازه به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد بسیار کوچک و بی‌اهمیت بود؛ هیچ‌کس آسیبی ندید، زخمی نشد یا کشته نشد، و نباید این روند مهم را مختل کند.
ما به توافقی بسیار نزدیک هستیم که صلح را به منطقه، از جمله لبنان، خواهد آورد و همه طرف‌ها باید عقب‌نشینی کنند. دیگر نباید هیچ حمله‌ای از سوی اسرائیل در هیچ نقطه‌ای از لبنان انجام شود، اما همچنین نباید هیچ حمله‌ای از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد — بیایید خرابش نکنیم!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76335" target="_blank">📅 18:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ex8sq9okPi547Qm6Vb8c_0619cQUqzZRqUJTP8DugcJqj92XcRn03w1M7LIxkVk5r_BuG99WKI4uNawoUzw8jNKtKSmew5aLgge6uhdHF4rbLIauF0Ntb2l4JBuTiW55o9nrXV5XH3KAkfEUbNcwsf1SHQ7fDhlOo_DQWYC9CNoyGcCQoGJP42YPgq4WQZOF-KIpICU240UrzltCMZ9lA5KsV0O5i5NIZ7bVY6EWEDYlcjxs7bcdl4zU8MaKzx50QnnO5dxZFXLV-MKAWE3c2T7cII2BcoKp6Kiw7Hu_qGy0XJikdqsFZaBcw0AwaLk7bwjwiz0ZnAMtikp_Q66dvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FHFN0gMP1GUEbJEXCmZe1rDGhFU3xHPXgMG4jYNl0mXzwDKXs-5rxpiMKT4DNpsT9KHwuW6jppQ0ZxoIIlV1txHabqiqquO4L1DtdnpOIloS7NHgdK38d_bnOfdiibsKAgz_YTHhnSEoWsXZ_XOJTpP_MWJZovKWwzLGzKgBEDr3J54M-P20EabmAQ9QyJKyuneRK1WEZH1SMgwtVrqe4bL0KyhSYMfYSle0_KIcPnk45QUvC6jbW676MlfoNjYxfaeSMmHNV3rcPpcxKs2cTewokmaXIUBQs6uZoOCsOWJbQsnTtkm3630PsxT02nvZkMkOWGQQqQYwZfUGhc1mzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ROjF4E7sUbzjTmLfYanaU1UtDZd6m_eVZ16324E9yT2c5SpgwaZ8afPx3JWBfmI2WZr9oA_gG6W9qmsq2mz26Mz5aH2-5Lf9pVHdHE9OhQVF9laJQozfVKlw2Qi7ZpYSoHR0zoBd1YzdFKhcG8fd__g9XM-fFlzrb9UIpAnIDg_OsPSFyUMeOQZKUIrOikABXkKdyBJtuRHu0oClspGxuohr5G_MfIWRG8nlLzTzpNOj3tyQ-dZOxUDEZWoj46Jkc-7fcLIuPi54cBiAR0fIx-kC0jgajx7TrTsjvjNwMZNTEbs9WclTBWhpnlOxg5iYPC6qNQQfT0WbKWnV-WdTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j90s5_UlrNAWevDHqkGG1iMg8g-g3HZSxOESjRVd8C2F8gJnO3BykufpRfqM5eD-xiU7n8J4BLEqYXfq6l5InIvwzRaWxBeUkia3MO7XhYB849JJUBAAWWNWfd7QMNO_38mRug23goFwKeXokVUncrtfUbxkfSsU8hZatbYbDcp6Kq3n6bKq1FeldT6i-ux0EFh3p-j4ANtB6fS0IYRUoIYmPcz4zEPmVSZEIzKo1lwGT7Kmx4i_jo9nDNu_aCJIPMaBrCYZUBjhRTh6ptdm9rTnL2SqqO2qvxHLhaDHrb_oD3-SVGmK4wcd2hBr9P5ZAPrYwXD7t2r4y8DPlp5uCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدجعفر اسدی، معاون بازرسی قرارگاه مرکزی خاتم‌الانبیا، در واکنش به حمله اسرائیل به ضاحیه بیروت گفت: «بدون شک این جنایات بی‌پاسخ نخواهد ماند.»
او در گفت‌وگو با دفاع‌پرس، حمله ارتش اسرائیل به منطقه ضاحیه را محکوم کرد و نسبت به پیامدهای آن هشدار داد.
ارتش اسرائیل در بیانیه‌ای یکشنبه ۲۴ خرداد اعلام کرد در واکنش به شلیک پرتابه از سوی حزب‌الله به شمال اسرائیل، اهدافی از این گروه را در ضاحیه بیروت هدف قرار داده است.
@
VahidOOnLine
محمد مرندی، از اصحاب رسانه همراه با هیات مذاکره جمهوری اسلامی در پاکستان، درباره ادامه مذاکرات تهران و واشینگتن، در شبکه ایکس نوشت: «فعلا هیچ مذاکره دیگری در کار نخواهد بود.»
@
VahidOOnLine
نظام‌الدین موسوی، سخنگوی پیشین هیات رییسه مجلس جمهوری اسلامی، در پلتفرم ایکس نوشت حمله اسرائیل به ضاحیه بیروت در روزی که قرار بود تفاهم میان جمهوری اسلامی و آمریکا امضا شود، با هدف بر هم زدن تفاهم انجام نشد، بلکه تلاشی برای «تحقیر جمهوری اسلامی» صورت گرفت.
او خطاب به تیم مذاکره‌کننده جمهوری اسلامی نوشت: «حضرات مذاکره‌کننده، به تحقیر تن ندهید و در شرایط تحقیر، هیچ چیز را امضا نکنید.»
@
VahidOOnLine
ارتش اسرائیل اعلام کرد ایال زمیر، رییس ستاد ارتش، پس از حمله به بیروت در حال برگزاری ارزیابی‌های مستمر از وضعیت با همه فرماندهان مرتبط است.
ارتش اسرائیل افزود بر اساس این ارزیابی‌ها، خود را برای احتمال شلیک به خاک اسرائیل در ساعات آینده آماده می‌کند.
این نهاد تاکید کرد در بالاترین سطح آماده‌باش قرار دارد و برای سناریوهای مختلف دفاعی و تهاجمی آماده است.
ارتش اسرائیل تاکید کرد شلیک به خاک این کشور را تحمل نخواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76331" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d-pexhkO1alu9JCT7YXa6ThFXoK4v3ps6qoFC2et2_REQgt9FjghNzD-6btQQK8badpqbCFeUhKmfT8x5JIe0sctGpkXO6g19FuzstQUpvTJm7y8SCRnjQhy6amsLkOaMGdyRun5EL5NxFfsmWzKrMFl3oF_oYHiXKLPsVwbQUPFDa-PYwEX7mDps2G_1GV-RInIWIeXBaAj_ZFkv9jX-FDQbh_OzZeu53q9mtM4xo7jr5pg6i4TnE5azlTcwEfOKG42uLb9kmBkUTjVoUt_N3huaWW7mwF7T-jt9RjcQAmMZJiKn9eDes7EaBSVwWhOhf3CCc6kCEIJV-hZzxb4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pLVM6vXRPxzJAiujgkJ0Ma1EJrzQ8bLZtP7GdMVW9evHBh2FFawUh9RKpkuXOx9jOLOyw3J2PNOBfDfjQS0fFqWG_WGZpfxdC5nx3PkmcU-wVl-wNN-mNMHgUo299LUUihBHN0Hxl_REw0n1mjcQQgNfmqKCw0dQIESIRlMLdCwbuS4kP64Nn0E6xZ3z97m-sv9se3WmNHY_Ziz76-Poi8_d4VpG9ww9Umdvlq_WuQzR2aiL5wKu4OGE8vesbrqn8itE-BSDnj8UlmVd1XPkH61qpW7sLzXMrZw7_nT3AN2QT9QYHMJQpEO52nD0inpCPEwCFPNhqPCy7BnBtN1UAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوهای توافق با آمریکا، اعلام کرد پس از حمله اسراییل به حومه جنوبی بیروت، ادامه مسیر توافق با آمریکا «ممکن نیست».
قالیباف روز یکشنبه در پیامی در شبکه اجتماعی ایکس نوشت حمله اخیر به حومه جنوبی بیروت بار دیگر نشان داد که آمریکا یا اراده لازم برای اجرای تعهدات خود را ندارد یا از توان انجام آن برخوردار نیست.
او افزود تلاش برای کسب امتیاز از طریق چراغ سبز نشان دادن به اسراییل نتیجه‌ای نخواهد داشت و سیاست «پلیس خوب و پلیس بد» دیگر کارایی گذشته را ندارد.
او تاکید کرد: «اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.»
@
VahidHeadline
حساب رسمی وزارت خارجه اسرائیل، روز یکشنبه ۲۴ خرداد ماه در واکنش به اظهارات محمدباقر قالیباف، رئیس مجلس شورای اسلامی در شبکه اجتماعی ایکس نوشت: جمهوری اسلامی «مثل همیشه دروغ می‌گوید.»
وزارت خارجه اسرائیل در این پیام با بیان آنکه اسرائیل شلیک به خاک خود را تحمل نخواهد کرد یادآور شد، حزب‌الله، صبح روز یکشنبه «بدون هیچ‌گونه تحریک قبلی» بار دیگر به اسرائیل حمله کرده است.
در این پیام آمده است حزب‌الله به طور مداوم غیرنظامیان اسرائیلی را هدف قرار می‌دهد و حتی پس از برقراری آتش‌بس نیز حملات خود علیه اسرائیل را متوقف نکرده است.
قالیباف در روزی که به گفته دونالد ترامپ قرار بود توافق پایان جنگ میان ایران و آمریکا امضا شود، در ایکس نوشت حمله اسرائیل «به ضاحیه بار دیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است. اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/76329" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V_zBzejJtVLwl_4O4VRkNuybyrG0GwgTZnSDxyTMScSl_zkWqbg6jgCzwt-MGX7CotKfc4gPQ7djUIXT4AcDJ2lssPffltqSw45xmg-LCzOYCtdWcoI0bsO4dBXWlpt8wsSEKAxeja3t2rmWjacy_E__K6keKjc_OcRuw5IL_LNmDtIUtnNekua6FDGMdU6bRGpaOH8IoOJiVpyBWg9-awzSFyv0zQK9ygTTM2_m6wEiTYc329I7dWB7c7hqdRKANdeB4gWiaUQr58K4MVYP3RFYRJP9kmyZkb1WS1hZYaNV2k243g38wtYpZx3qaB64vO4wGLSYosJnfsjJDcWzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NLeNzQKsxdwthquhyn2F1UtQI377pc9HLdlgGbSFet6oNmiBdKf2NYJAoiwLF_0y2zKK30jBHrAcCVB4H9ZeMv36L9Sj40VbEwpFtKtDZOF85OxhHvrE6URKMM9RYQSXvEojErEPgZV2o1tsTdH0C9EZQqU-byEHbiKw-PLi0IgcfdSCAnkxiTGOSmifukFpqTv1halfIUWQmC1Xk_JLO36gnBBwJzLG6Y3N8uW2HBIbQM8i8tUvwk6cNEDlh5TiM-qfRmzFwA3v5M6Zh4kwfCRpvHPBr3ayAqhxmGe5RaGDAIjk-JBD6xKbU3c5xmBdNdOhzRBF-0F9sblVRcDiRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tSA52YtVB9SMoSi1N8U3iheaDVvleTxamrOGZ9z99ga9QB1p-6x-N1oppHyUqOmbhMDknh09xLeb8DKtZ5U-SqqdYF1TjyKO_bWECWqi8xTXhwW6ewVMX07DPfco51Wlp7KbQ-PfGxsHgUuneVSr9pguOXktRSFXNLXogNms_X7dPAq7GUws7blu8eKAXyt8VRP1FgTNZqV5qLoBc9Ri2CgdlZYRaBQ6Z1o6ey-qaS6Kr6-ljcbHMYrs8kUzjsMd3UgHkb9jkmFk-4EFI9wHiGfKY-YPc_81cSEJ0ZhPROSRQVpS9jVpCJbw0rrlTWk6SYL0Y98nTB51AGyLsJipIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XZStGJZmwA95CWOsJ3MshsUHZh3OYahSi33F-p3S52YAOGh9O_3eNdHeCdvEDK3-nFvArXsgKTmh-lKMUFbUp-Wq1srPnuRgh6SMtrGMjT9dG1V77ZazLfP2uEL523OemI6l3t2FNZX-FumudrU0LpewD_ccvKpbtyrCDIYc6WFmloeUrjfPZwZyylrtph-QqfqrCrdylkBteAWrwdzX9vvNwZS3E8zeN9coP1-qXdOm7SHVJYoxwX_IeuIW31CXenee1cHQksfllZIva64KqepWUwHVt-0dNNcZxxfI-Vs2Nb7OngYjAtVEgjjpjyCCNrIwW8sf8xHibxYFwlwtsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50b9dacbb2.mp4?token=SDwOq71b4Iet3-FyBtjWMMOP3TLJMTPdU9qJHGqXg74dqNnII6p00ZZlCMxGB6vCYP31TaGUXV4z3yrjWBHOsCT1_LpC4cDe1szU6HS1iAfzmkmo0fToHw-bFgqs0TVNXR0V60ug7dZ-vlnASGeEOiJ-os1-GmGhTotvcogpVt4wruG8CuTYS-3K8hveElvMtpXLdOSpBvDoe8Rv-J55OJdhIhNr6lblp1Qn1O1bo0vzzWu5wGvLJc9LHArOlOEH9ctlU9uC8XbYwcrWwnz3F1N9F1uRsZ5Coxo__RAk_Kp_9R1_zH1ziioodbLEK6gd6GIekoDZwR7hzHb_w0d1Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50b9dacbb2.mp4?token=SDwOq71b4Iet3-FyBtjWMMOP3TLJMTPdU9qJHGqXg74dqNnII6p00ZZlCMxGB6vCYP31TaGUXV4z3yrjWBHOsCT1_LpC4cDe1szU6HS1iAfzmkmo0fToHw-bFgqs0TVNXR0V60ug7dZ-vlnASGeEOiJ-os1-GmGhTotvcogpVt4wruG8CuTYS-3K8hveElvMtpXLdOSpBvDoe8Rv-J55OJdhIhNr6lblp1Qn1O1bo0vzzWu5wGvLJc9LHArOlOEH9ctlU9uC8XbYwcrWwnz3F1N9F1uRsZ5Coxo__RAk_Kp_9R1_zH1ziioodbLEK6gd6GIekoDZwR7hzHb_w0d1Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر نخست‌وزیری اسرائیل روز یک‌شنبه، ۲۴ خردادماه، اعلام کرد که ارتش این کشور سایتی متعلق به گروه حزب‌الله در حومه جنوبی بیروت، محله ضاحیه، را هدف قرار داده است.
در بیانیه ارتش اسرائیل در همین باره اشاره شده است که به «اهدافی تروریستی متعلق به حزب‌الله» در ضاحیه حمله شده است.
اسرائیل دلیل این حمله را شلیک از طرف حزب‌الله به خاک اسرائیل عنوان کرد.
ساعتی پیشتر ارتش اسرائیل اعلام کرده بود که سه پهپاد روز یک‌شنبه به طور جداگانه به شمال اسرائیل پرتاب شده‌اند. اسرائیل گروه حزب‌الله را مسئول پرتاب این پهپادها اعلام کرد.
ارتش اسرائیل روز یک‌شنبه همچنین به ساکنان چندین روستای دیگر در جنوب لبنان هشدار داد که محل زندگی خود را ترک کنند.
خبرگزاری فرانسه به نقل از سخنگوی عرب‌زبان ارتش اسرائیل نوشت که ساکنان ۲۹ روستا در این منطقه باید به نقطه‌ای دیگر نقل مکان کنند. اسرائیل قصد حمله هوایی به این روستاها را دارد.
طبق این گزارش، اسرائیل صبح یک‌شنبه ابتدا به ساکنان ۱۳ روستا و سپس ساکنان ۱۶ روستای دیگر در جنوب لبنان اخطار داده است.
@
VahidHeadline
شبکه العربیه گزارش داد علی الحاج، از فرماندهان حزب‌الله، در حمله هوایی یکشنبه ۲۴ خرداد اسرائیل به ضاحیه بیروت کشته شده است.
دفاع مدنی لبنان نیز اعلام کرد در این حمله سه نفر کشته شدند.
العربیه همچنین گزارش داد ارتش اسرائیل یکشنبه سه حمله هوایی به شهر سجد در جنوب لبنان انجام داده است.
ارتش اسرائیل پیش‌تر اعلام کرده بود در واکنش به شلیک سه پهپاد از سوی حزب‌الله به شمال اسرائیل و آنچه نقض آتش‌بس از سوی این گروه خواند، یکی از مقرهای حزب‌الله را در ضاحیه بیروت هدف قرار داده است.
@
VahidOOnLine
خبرنگار آکسیوس، به نقل از مقام‌های اسرائیلی و آمریکایی گزارش داد اسرائیل اندکی پیش از حمله، فرماندهی مرکزی ارتش آمریکا (سنتکام) را از این عملیات مطلع کرده بود.
جمهوری اسلامی پیش‌تر هشدار داده بود هرگونه حمله اسرائیل به بیروت می‌تواند با واکنش تهران همراه شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/76323" target="_blank">📅 17:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A38xsUB10pFL_tEBIqGO3nxjBJT3ogpqO4IQ_JGGt2hsFjWfGF_zeAmfTUH1gE4blbmPk8lP5qNE-7mT63yUay2qc78nH6iZnJ0vaepDJOP2XKqLUsJvzAz3DYpMK_SmCi3rnDbquox5qYCrudhMtxCwK-blAY8xJsRzmpLZUj6Xgs_DRqTXIfd92ykuGeEyfHQf0hyWyplxsftTPWElIFANph-cm8qGiS3By46IHyv8057ynakWc7AaW6O5iRWPb4WRpA-M1vn7DSy7ngSFosuISn_kAgGi6jPW2WIJK8MxZg2-FQ6hvMVgyn5A_FQXu6PpAdXZWVj73-im0ej4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یائیر لاپید، نخست‌وزیر سابق و از رهبران مخالف دولت اسرائیل، در شبکه ایکس با انتقاد شدید از بنیامین نتانیاهو امضای تفاهمنامه بین ایران و آمریکا را «تکان‌دهنده‌ترین شکست‌ سیاست خارجی و امنیتی اسرائیل» توصیف کرد و مسئولیت کامل آن را متوجه نخست‌وزیر دانست.
آقای لاپید نوشت امیدوار است که «گزارش‌ها درباره توافق با ایران درست نباشد» و به ۱۳ مورد اشاره کرد و آنها را ناکامی و کوتاهی‌های آقای نتانیاهو دانست از جمله اینکه:
«او یک روایت بیش از حد خوش‌بینانه را به آمریکایی‌ها فروخت، بدون اینکه نقشه خطرات را کاملا برایشان تشریح کند و در میانه جنگ اعتماد آنها را از دست داد.»
او همچنین نوشت که آقای نتانیاهو «نتوانست آمریکایی‌ها را متقاعد کند که تاسیسات نفتی و انرژی ایران را بمباران کنند» و «مسئله موشک‌های بالستیک را در توافق یا حتی در مذاکرات بگنجانند.»
آقای لاپید همچنین نوشت که نخست‌وزیر اسرائیل «برنامه مربوط به کردها را پیش برد بدون آنکه واکنش قابل پیش‌بینی ترکیه و نفوذ رجب طیب اردوغان در واشنگتن را در نظر بگیرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76322" target="_blank">📅 17:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/coygV0EAGiFjuc6MJvWJuCpD6h0IwgKxb6z1BfGt7Da8MsXeJDlQYp74T0VZvFFlWb2191-Byh8Cd0X2930EUBJFj1FKNT60cNbEdPOsoksMRvNvPLdfYGDcLu9J4s4dMgAegimHm6nGnMoNXKnxnyAj_wIye3bSVQjqpFVjMgV5iF8I7JjR7oMOxuqFr5Uw2WM8PokUPTz-WReei2FFCKOoeTLQXFiJuHaj23XbNOK1FUNNYI-XHI7EQylnBpmJgV_7kWKgaBRfGGipDNgUNCS3ZO_sQzYEUt-nY4aBqJFM1FgVb-wA55-NPvJ5P7iAw9LXsv8YMnyqye_j_2U4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pE6eK5SNYn9k9B3PUPoWCFReDZihsDuRAJOXQMKp0Om-B9Uu8MD2G7cP7N_3ZmEM5_WZ9iBx4SSf_Hx2yXvMCCsVbPlc5dHF_WJp2Y7oLgVn5AsCm2q6Ht23HvpQVkbIh0jUPCgqN34D2XJrAvpjDM7Vlb-8GWpPFq1Ut--ARO9GXDWg95R7oPiUnI-4iSjqWFnEU4c52KvUF9pL02pnRScBBu9ID__XtNT1HkL2SVuK0lCYnJ2nIYiATEUnFbp1Nb2wi1w-Wo_9FYaYScuavRn7Rvr7fcB8-RhzYVQKAth-OfMMmistzLJNlQoYwz9tCvmF2Xi7xKh2jJrcRkOVUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در حالی که خبرها از داخل ایران اشاره به ادامه بررسی متن تفاهم‌نامه و نامشخص بودن زمان امضای آن دارد، خبرگزاری رویترز روز یک‌شنبه نوشت که دولت دونالد ترامپ در تفاهم‌نامه با آزاد کردن ۲۵ میلیارد دلار از دارایی‌های مسدود ایران موافقت کرده است.
رویترز خبر خود را به نقل از «مقامی ارشد» در جمهوری اسلامی نوشته، اما به نام او اشاره نکرده است.
به گفته منبع رویترز، دولت آمریکا همچنین موافقت کرده است که اورانیوم بسیار غنی‌شده ایران در داخل کشور رقیق شود.
این‌ها دو مورد از بحث‌انگیزترین موضوعات در مذاکرات جاری میان ایران و آمریکا بوده است: ترامپ بارها بر لزوم گرفتن یا انتقال یا از بین بردن اورانیوم ۶۰ درصد غنی‌شده ایران تأکید کرده و همزمان بارها گفته است که پولی به ایران نخواهد داد.
مسئله دادن پول به حکومت ایران به‌ویژه برای دونالد ترامپ حساسیت‌برانگیز بوده است،‌ چرا که او خود سال‌هاست به باراک اوباما تاخته که چرا در جریان رسیدن به توافق موسوم به برجام با انتقال پول به تهران موافقت کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76320" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E--7j5MvQc-7uBx2UXFKLVUKckYsfmIz31tWvp7JMmt4MFufegYM6fb0OgCl1X_IMxPmcasiXJd1wLY01zVGkW4lYCpPI46zKy5KtuV7o2ssV0lIDHv0N64vg9HYmATV5wKd_IduLhw7dwyXoTGlChadYSuUYRk0Y8akHvE7Nuysn1YLt7aVRWb5iRM5T2m2nixzWFwjNNRSdPnZWZ9C98LwuHwmQfPprcyOsLYyci8suiV4Ez0kXsna-JTJ1pdRcT4orEG2cI2_9cEryQMOouoH3b-Lrl1vM7x-yMvOJCJ3KkFl47_0-c0oqlOYmJ9T0LHr8bqQ9Zo840jum1vFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع دیپلماتیک گزارش داد مذاکره‌کنندگان قطری پس از رایزنی با آمریکا راهی تهران شده‌اند تا با مقام‌های جمهوری اسلامی درباره کاهش اختلاف‌های باقی‌مانده و نهایی کردن تفاهم احتمالی میان تهران و واشنگتن گفت‌وگو کنند.
رسانه‌های ایران نیز گزارش دادند این هیئت قطری به تهران سفر کرده است.
این سفر در ادامه رفت‌وآمدهای دیپلماتیک قطر انجام می‌شود. چهارشنبه گذشته نیز مذاکره‌کنندگان قطری پس از مشورت با طرف آمریکایی به تهران رفتند و درباره متن احتمالی تفاهم با مقام‌های جمهوری اسلامی رایزنی کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76319" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3bec2d43bc.mp4?token=r5Jx4B7-lG4se4i76AFxvCIwgQQxPBcL2og5aMvygcsx30PSB7-CQFKdWbztvVc0Lj90z6OSRDEQwjSvCfyl0RSUQp7iqnkHgafC-eSwM22iX130kvNJEXykF6le8envBPt9dw7KMZlX179w_qo6XTnbX-RdbVz71BfoPkm5zwuY286HF5bEqL0uXzdPTPvYauD6hXOxxIu9O7Rl3V2OHdAGMpHfzcin8gV0MfD42H9pDDqiD6ulh3gUA_sU-zFpm1B7g5U48J5s7hbb64_WkKqSMcVEC70IQL2oBwQwskiQik0j5M1r7D5W9Z4mVK5vF27sx8NL6L8j8PGhktAtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3bec2d43bc.mp4?token=r5Jx4B7-lG4se4i76AFxvCIwgQQxPBcL2og5aMvygcsx30PSB7-CQFKdWbztvVc0Lj90z6OSRDEQwjSvCfyl0RSUQp7iqnkHgafC-eSwM22iX130kvNJEXykF6le8envBPt9dw7KMZlX179w_qo6XTnbX-RdbVz71BfoPkm5zwuY286HF5bEqL0uXzdPTPvYauD6hXOxxIu9O7Rl3V2OHdAGMpHfzcin8gV0MfD42H9pDDqiD6ulh3gUA_sU-zFpm1B7g5U48J5s7hbb64_WkKqSMcVEC70IQL2oBwQwskiQik0j5M1r7D5W9Z4mVK5vF27sx8NL6L8j8PGhktAtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: مقاومت باعث جنگ شد
[اینطور برداشت شده که داره میگه نپذیرفتن شرایط طرف مقابل در مذاکرات منجر به جنگ شد]
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران شنبه ۲۳ خرداد در شبکه خبر و در پاسخ به پرسشی درباره علت دو جنگ اخیر گفت: «مذاکرات علت جنگ نبود، مقاومت تیم دیپلماسی در مذاکرات علت جنگ بود.»
این گفته‌ها که در تعارض با موضع رسمی نظام جمهوری اسلامی و شخص علی  خامنه‌ای، رهبر پیشین جمهوری اسلامی به شمار می‌رود، با واکنش تند رسانه‌ها و سیاستمداران جریان اصولگرا مواجه شد.
علی خامنه‌ای، رهبر جمهوری اسلامی ماه‌ها قبل و پس از «جنگ ۱۲ روزه» گفته بود دشمن هر جا احساس کند که ما ضعیفیم، حمله می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76318" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEdRKHTbLwNJnCp4wfMCKFkVL3BRCfK5Uq88Pus8cFCMPTaElZK_n2NHjU4N1EvOiXRHKET-0WCV0ON200WLy18vJZfhVXdfpjhP1V35SwdCV5V6Jg7S09eWVLhfXjmEDAAhiIFazkTz1ykE09IZmI0YujnmbPX6nlKRtK4-fdEnrMH0ppjH-DBjOD2RrkcD6JCq0jQ4Y-bHHCXkXyjQ7BijTS137kl0_IBTg9vWO-Zs16k_fsKNZ8x1cGUknFb_gsPkqPs_TerLCk0kzq6eJnvPFFZsbSZCMBxwocAydt8Q0KHHhlL93AwUsla7Dlnb6d79vboNa1xRsllMtCQCgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی در اطلاعیه‌ای مدعی شد یک فرد متهم به تلاش برای نفوذ به مراکز داده، یک هسته چهار نفره در جنوب شرق کشور و ۱۲۶ نفر از آنچه «لیدرهای میدانی شبکه خرابکاری خیابانی» خواند، بازداشت شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/76317" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q95SM7z3W0qCL3RY_uC1sWc01Jc0gbsfPMlAo9I6_ICBC2GxzXL8YElS-YuCbWKelJDpRhS5iK0QupRbJY2EG1wUiEsJy3TgXBhApOXi7vIM26vUixA5IqcqvAQmltSncN8eCHzbMPK8r5QrQTHnNe6Qvcq8looxyrMuLdhGEeJzI-gtLSNlTaKMDOhKPLVVURuv32rSmOveAjY6sZb-QxzKJ4fc0yR47aHiTvCmAiwKeqRVByxi3A8HbfWqe9dCZKyMAZEO0-BPeCom4rKgY1UX6D6ZiEFVv0kqxyqej8rRROZSBt4NVEkjooq717sAf-m9uHKvduym5_pwixQQQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود طراوت‌روی، نازنین سالاری و مسعود احمدیان، وکلای دادگستری، به حبس و به عنوان مجازات تکمیلی به دو سال ممنوعیت خروج از کشور همراه با ابطال گذرنامه نیز محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/76316" target="_blank">📅 17:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2ScgcnORtmdchtvY0sP1H6audW07dMh0pdqDo3ooisrYoFl4Q8dnXdMwmcfJEnjRK2jNhDoHQi8xbZp_iKxaSthPf-o94FFkSc3SAiBN73WJuwMDftTXckkTvkceQZLuXarSoQK7qUc5rJC5eX1R6Bg2TTXl-Oei6QFbFffoGuBz2OPig__O-OtBlLGL-uOSJe1t_W5DH3RNxYJn7kcFqargjVJPTWdA3Ruq_qhdaqSXZQLI3zaNvH2leGve_fsw-e8uMxz4GiUu-TFT5kzhccuydv7hXRd1O6QkydkIXsCbOtKrruDjRkGgVTbFMdyS1jZureFHLq7BbyfV89m4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماموران اطلاعاتی و نظامی جمهوری اسلامی در استان گلستان با یورش به منزل خانواده جاویدنام ابوالفضل میرآییز، اقدام به تفتیش خانه، طرح اتهامات بی‌اساس و تهدید اعضای خانواده او کرده‌اند.
طبق این گزارش‌ها، ماموران ضمن بازرسی کامل منزل، بخشی از وسایل شخصی خانواده را نیز با خود برده‌اند و آنان را به برخوردهای امنیتی تهدید کرده‌اند.
ابوالفضل میرآییز، ورزشکار ۳۴ ساله گرگانی، در جریان اعتراضات دی‌ماه با شلیک مستقیم ماموران حکومتی در خیابان‌های گرگان جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76315" target="_blank">📅 17:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76314">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان ساعت۰۳:۳۲ صداهایی میاد از تو دریا
ما چند کیلومتر از اسکله سپاه طاهرویی فاصله داریم
سلام وحید انفجار های پی در پی از یک ربع پیش تو دریای شهرستان سیریک
صدا انفجار شدید اینجا شرق سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 475K · <a href="https://t.me/VahidOnline/76314" target="_blank">📅 03:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76308">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o0OnLDKOnzRG9aRtHOlGddEWtXYXCk5oFa67ZZhoX3OeS_2GMJtqIGDfD4optu32PXGPZgNOYa70wIlk7C_BXBAfVhN9uU5qA1cWW3n0rcOZjZraBIob-iOBaChy3Ga3Dy4WnUwYMX0pIIZTIlsv2FPoBuMdtp46_V6cu0O4O_ZA0obr4SApA4cOqYM2dNPzp9o0G9MdASqhCUR5h8GKTvgMtkkwyRXMtQmyFYhEXnp7wXSPuQzLZ67jyinthOdVVKUWA_0poYBq4vS2sigcL6p1P4fDRxhCYB78WRFC0eah9OOYjdyHhmL-U8kY6fPZiHt8_mEqiyDtZREgP_iw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=T7kqN_19GgPfDNWrwjJENRpKK6M2fQQOwnhfre7KcD6YQuwI7OQQLvd3DU10bJAwFV6zIhTk486KaJi03drrYoyUWkmOiX_d3TM7lFCP-CtoxTx1Dt-qkP01njNhcQQTIKuPPkc6HiUfxbUW5LGBb0OrtgoSiNRwNfDRclgHSzriz8HJ7isB_565inBRr7MnL2Q7e-oGliBOwSrpcnohDuPZat4OTwYOCShFO9iQx_pG8kgcrNX4cTy_2Pq_bsHptdX-_g4ZRu3ZA4XxK1txSwN2qpVSeFtyWRLnS4TYCXzt60mEuc1TEEn5hszKWWSmD2dSVW-y7goc-k8PRGplbA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d60822ba5.mp4?token=T7kqN_19GgPfDNWrwjJENRpKK6M2fQQOwnhfre7KcD6YQuwI7OQQLvd3DU10bJAwFV6zIhTk486KaJi03drrYoyUWkmOiX_d3TM7lFCP-CtoxTx1Dt-qkP01njNhcQQTIKuPPkc6HiUfxbUW5LGBb0OrtgoSiNRwNfDRclgHSzriz8HJ7isB_565inBRr7MnL2Q7e-oGliBOwSrpcnohDuPZat4OTwYOCShFO9iQx_pG8kgcrNX4cTy_2Pq_bsHptdX-_g4ZRu3ZA4XxK1txSwN2qpVSeFtyWRLnS4TYCXzt60mEuc1TEEn5hszKWWSmD2dSVW-y7goc-k8PRGplbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف، عراقچی، پس حون رهبرم چی؟!
برخی رسانه‌های داخل ایران تصاویری از تجمع برخی طرفداران حکومت در شامگاه شنبه را منتشر کرده‌اند که در مخالفت با امضای توافق احتمالی با آمریکا علیه برخی مقام‌های جمهوری اسلامی شعار می‌دهند.
در یکی از این تجمعات که در میدان ابن سینا در تهران برپا شده، تجمع‌کنندگان علیه وزیر خارجه و رئیس مجلس شورای اسلامی شعارهایی مانند «عراقچی حیا کن مملکت رو رها کن» و «قالیباف، عراقچی / پس خون رهبرم چی؟» سر داده‌اند.
برخی رسانه‌های نزدیک به اصلاح‌طلبان این افراد را «نزدیکان به جبهه پایداری» معرفی کرده‌اند.
خبرگزاری دانشجو نیز عکس‌هایی از یک تجمع در مشهد منتشر کرده که در آن‌ها پلاکاردهایی در مخالفت با توافق و همچنین انتقاد تند از مذاکره‌کنندگان دیده می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 530K · <a href="https://t.me/VahidOnline/76308" target="_blank">📅 23:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76307">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری فارس، رسانه وابسته به سپاه پاسداران:
اصرار عجیب ترامپ بر امضای تفاهم با ایران در روز یکشنبه و آزمونی برای تیم مذاکره‌کننده
🔹
ساعاتی پیش، دونالد ترامپ، رئیس‌جمهور آمریکا، بار دیگر تأکید کرد که «یادداشت تفاهم» با ایران روز یکشنبه امضا خواهد شد. این در حالی است که مسئولان مذاکره‌کننده ایرانی صراحتاً اعلام کرده بودند که تفاهم هنوز نهایی نشده و یکشنبه قطعاً انجام نمی‌شود.
🔹
نکته قابل تأمل، همزمانی یکشنبه با چهاردهم ژوئن، روز تولد ترامپ است. برخی ناظران احتمال می‌دهند او با این اصرار در پی آن است که از این مناسبت بهره‌برداری نمادین کرده و آن را به یک رویداد تبلیغاتی برای خود تبدیل کند.
🔹
اما با توجه به مواضع شفاف مقامات ایرانی مبنی بر نهایی نبودن توافق، به نظر می‌رسد مسئولان مذاکره‌کننده کشورمان متوجه این لایه‌های پنهان هستند و اجازه چنین مانور رسانه‌ای و تشریفاتی‌ای را نخواهند داد. از این زاویه، سرنوشت امضای یکشنبه نه فقط یک آزمون فنی برای محتوای تفاهم، بلکه آزمونی برای صداقت و ایستادگی مسئولان ایرانی در برابر فشارهای نمایشی نیز خواهد بود.
@
VahidOOnLine
وب‌سایت خبری اکسیوس به نقل از منابع آگاه نوشت که دلیل امضای ویدیویی توافق آمریکا و جمهوری اسلامی، «ملاحظات اجرایی و لجستیکی» و عدم امکان سفر جی‌دی‌ونس به پاکستان است.
اکسیوس نوشت که یکی از دلایل اصلی امضای ویدیویی توافق آمریکا و جمهوری اسلامی این است که ونس در صورت سفر برای امضای توافق، نمی‌توانست قبل از عزیمت ترامپ برای شرکت در اجلاس گروه ۷ در فرانسه در صبح دوشنبه به آمریکا بازگردد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 485K · <a href="https://t.me/VahidOnline/76307" target="_blank">📅 22:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76306">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MBWOK6v0C8BC34l6as3ez1tXLk8oQDrlM2P-I6ra7m9x8jnscOFLUolKPg6pB2QL0cFOkzZcVoO13-B-r9D6yWq-UCIjpzzm0pzKDNgbzd6J1j1wA_uBPM76KlMYstSEvnihNYtxmWMtoK8hYRu-YfbM7Bzgn_Rg44mAlUeg7z8BiZzD5kxURe-Sy7tchVfROs62g0XVH86cjpNmR5PE6MNK0QXtZQydIGScNXXMg2nAs7bbGI1aJsebxmy18vx-LKp4wMtUkpD_WhsFHjTRFnKJ9bc25ucju0uNEkiNuSa9xuzphXlh3CIgFxLuOa-wBDl9StSsqNpSmmoKc_hc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: قرار است توافق فردا امضا و بلافاصله تنگه هرمز باز شود
پست ترامپ، ترجمه ماشین:
توافق باراک حسین اوباما با ایران، یعنی برجام، مسیری آسان، زیبا و هموار به سوی سلاح هسته‌ای بود؛ سلاحی که ایران شش سال پیش می‌توانست به آن دست یابد و مدت‌ها پیش از حالا از آن استفاده می‌کرد. توافق من با ایران درست نقطه مقابل آن است:
دیوارِ جلوگیری از دستیابی به سلاح هسته‌ای!
در واقع، آن‌ها دیگر سلاح هسته‌ای نمی‌خواهند و چنین سلاحی هم نخواهند داشت؛ نه از طریق خرید، نه توسعه، و نه هیچ شکل دیگری از تهیه و تدارک.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز به روی همه باز خواهد بود.
رابطه ما با ایران بسیار متفاوت و بهتر از رابطه‌ای است که دولت‌های پیشین داشته‌اند. برخلاف صدها میلیارد دلار پرداختی اوباما به آن‌ها، از جمله ۱.۷ میلیارد دلار پول نقدِ سبز و سرد،
هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، ما وارد خواهیم شد و «غبار هسته‌ای» را که در اعماق کوه‌های قدرتمندِ گرانیتیِ فرورفته زیر آفتاب دفن شده است ــ به لطف بمب‌افکن‌های زیبای B-2 ما و خلبانان درخشانشان ــ به دست خواهیم آورد و آن را
رقیق‌سازی و نابود خواهیم کرد؛ چه در ایران و چه در ایالات متحده.
ما مشتاق همکاری با ایران و سراسر خاورمیانه در آینده‌ای طولانی هستیم. امیدوارم این روند همگی سریع، آسان و روان پیش برود.
اگر چنین نشود، ما گزینه نهایی را در اختیار داریم؛ گزینه‌ای که امیدوارم هرگز دوباره به کار گرفته نشود!
از توجه شما به این موضوع سپاسگزارم!!!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 460K · <a href="https://t.me/VahidOnline/76306" target="_blank">📅 20:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76305">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شبکه الجزیره به نقل از سخنگوی وزارت خارجه پاکستان گزارش داد که مراسم «امضای الکترونیکی» توافق میان آمریکا و جمهوری اسلامی یکشنبه ۲۴ خرداد برگزار خواهد کرد. به گفته او، پاکستان میزبان این مراسم خواهد بود و مراسم از طریق «ارتباط ویدیویی و آنلاین» برگزار می‌شود.
او جزئیات بیشتری درباره شرکت‌کنندگان یا مفاد این توافق ارائه نکرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/76305" target="_blank">📅 19:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76303">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JVlNmD0jAgCmcmkxlxwfnPq74YUdxqV33ZCD0ifvhYPvP04gAsSxWjpa6LnK61lLPpDL1uVnT0-AYBW-qawOlTV66vROXCruJdujYwCRF07l7qILD3TdT-3HoxECouI4AK9QHJDVfhd3cwmA0Ij3S-1j7ax7GW-Fgyc9oKeC18QuCGOeSB1ShJv7vzMi-WJlSivp-fYn3nzTXK5gt6vwnwhjSu2gipqZAp_dEb0P_pA_5UmvUMkbOe0_9jV3DyzeSD7WanqWWyWZv9rNgLuxShlNLrsRTNGpUhKOEHULQOIctZFFXrBf06w-_1yp_fagZy1CaOkXbaQOxzIBfOJKag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ozPlR6WNXXiZotQa5ikGHPKPWjKjN3mq2xLFcu6ZPniFQEBQaThY65Uf_tYoNmojbVSonUu-OL_RHKeuaY_kwa0P-DXacrOz8Xx2-MP39jgbpywDwhLNS9WJ0-ot6Row9L3aN6m_WTZzpzRlfIjlolBhwl84X2t-gFfwS54mROEz8HGNKUcYWZU4o0Cdb3CE_tuWoqFmy5ySIrT5CD1GR8YyTyusV-rKaq6gPW7KBhT1KgRqS7EEHCHLC2MOm8G88GEgXXcx0Yie7LFbqFEvAumcYC8AtrvFSv7sylDPRr68csxhXw0Zm3pHQCsyxdeG34bJRji6BGbXWKa49QMr8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یک مقام ارشد دولت آمریکا به رویترز گفت که دونالد ترامپ، رییس‌جمهوری آمریکا، در نشست گروه هفت با رهبران امارات متحده عربی و قطر و برخی دیگر از رهبران خاورمیانه دیدار خواهد کرد.
به گفته این مقام، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در دیدارهای ترامپ با رهبران خاورمیانه هفت حضور نخواهد داشت.
نشست رهبران هفت اقتصاد پیشرفته جهان، موسوم به «گروه هفت» ۲۵ تا ۲۷ خرداد در شهر اویان فرانسه برگزار خواهد شد.
@
VahidOOnLine
اسماعیل بقائی، سخنگوی وزارت خارجه جمهوری اسلامی، در نشست خبری گفت احتمال نهایی شدن یادداشت تفاهم میان تهران و واشینگتن در «روزهای آتی» بالا است.
او در پاسخ به پرسشی درباره احتمال سفر هیات مذاکره‌کننده جمهوری اسلامی به ژنو یا اسلام‌آباد در دو روز آینده برای نهایی کردن یادداشت تفاهم، گفت: «درباره زمان دقیق امضا باید منتظر بمانیم.»
بقائی افزود: «برنامه‌ای برای سفر به ژنو یا جایی دیگر ظرف یکی دو روز آینده نداریم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76303" target="_blank">📅 19:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76300">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vF1OiDTbVL3vhAvMPLOoLbLmPtNvvwKc_34iqTSiPtzA3EfoBQ4Qq2dF1DQezx9QK1DnCN8dgejFbKQG7_tiPxeQ6-Npxwj88XtXpLddBNm2P4KQX7hX1meadbjUNDrDU9uXzJv9bv5ruU94JEZX9RRv0Tv9zLEQyH7mXqF_JFQoeuz_RUxlIyNf1mfMzHdRdHKKAsZrBSCbDwZSkvXsClXH9KXCTLdUwBxeRL9f7BbzZjO7Z1CNDMvQRu0uWRLB6vSbVi896QzclwBd3aBHr_-9bhegCp3PZ2CEe4Ab8CbwFEzqvq3y4coDW-ijY2RBHI5F3YJTtBtGbV0xxJdxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RgpF1_J86InzOSe90ycQ7rQaIdylPLSxz6VrL8S_19yzd4DO41v_AWNWTSobMdKCMz7kAyRfd2qlpGSiWbqg-fS-qAJsB70OSialUCvDqfIn9xQgX-z67qMg-RvFtvwimiMMLnljx9caw-Q7bwwB2W5RD0Vh8alKDTXpY69_dwbShuoJjpRe7UVRXcQriAU5QIfRg_7IM2sThV5Zg6tLhWPUQzLLOsVD79gDm3aWN6CvM8fEkqQDbS7kIj9STNZ1XMVe8Sn0Rj3_G-cEDFLLvGEczUSVSP5ppM2SNlet9UKqU1zAppDSBq0Y3sYZpzPVd_ZY5_Wk16x_295PGhRsqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نخست‌وزیر پاکستان: تفاهم‌نامه ایران و آمریکا احتمالا تا ۲۴ ساعت آینده نهایی می‌شود
نخست‌وزیر پاکستان می‌گوید ایران و آمریکا بیش از هر زمانی به توافق صلح نزدیک‌تر شده‌اند.
شهباز شریف دقایقی پیش در پستی در شبکه ایکس نوشت که انتظار می‌رود تفاهم‌نامه ایران و آمریکا ظرف ۲۴ ساعت آینده نهایی شود.
او گفت که پاکستان در حال فراهم کردن تدارکات لازم برای «امضای الکترونیکی» این سند است و پس از آن هم «گفت‌و‌گوهای فنی» آغاز خواهد شد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، شنبه ۲۳ خرداد، در شبکه اجتماعی تروت سوشال، پستی از شهباز شریف، نخست‌وزیر پاکستان، را بازنشر کرد که در آن به احتمال دستیابی تهران و واشینگتن به یک تفاهم طی ۲۴ ساعت آینده اشاره شده بود.
ترامپ این اظهارات را بدون توضیح اضافی در تروت سوشال بازنشر کرد.
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه، روز شنبه ۲۳ خرداد با تشریح آخرین وضعیت مذاکرات اعلام کرد: «یادداشت تفاهم اسلام‌آباد که در حال پیگیری است، به طور مشخص بر خاتمه جنگ تمرکز دارد و در این مرحله تصمیم بر این شده که هیچ بحثی در مورد موضوع هسته‌ای صورت نگیرد.»
بقایی درباره گمانه‌زنی‌های مربوط به زمان امضای این سند گفت: «درباره زمان دقیق امضای تفاهم‌نامه باید منتظر بمانیم؛ اگرچه این رویداد فردا نخواهد بود، اما احتمال اینکه ظرف روزهای آتی رقم بخورد کاملا منتفی نیست.»
بقایی ایالات متحده را به «تزلزل و بی‌ثباتی در اظهارنظرها» متهم کرد و گفت: «به دلیل تزلزل و عدم ثبات طرف مقابل در اظهارنظرها، باید در هرگونه موضع‌گیری درباره این روند محتاط باشیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/76300" target="_blank">📅 18:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPVwbTJE5oQtGkfwsD4IBmYFK0n3Wuz9N9AwXTsAfvGD3BKEemFMbULLSEG_oZyGANjXuxFzoTA3Mv6ajmY4962l_2uraAynWsYMGAO96Y6EWCKl5UJz-EVQDrUJAwuaCse58TnM6cuzmwyIQwA414lpU1-17-874MzTHoLLVXk2Drj6AZcOQNBoiJ4lhPH2ebj6jLBaj9BKSZO9vpLuZYuJqTPLU7RVMB8CKuEJfrdMIZ-jNp_cogwZgXAEdo2eZFDmWMkB5R4OS2Fm2yzqv5giv95iFJRAloHkCrwSAWDm7pRSe0MjMLUTVKeOECLJ_2o0XnmB663BUzRxO48UAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز پژوهش‌های مجلس در تازه‌ترین گزارش خود درباره وضعیت شبکه برق کشور هشدار داده است که با وجود افزایش نسبی ظرفیت تولید، ناترازی برق در تابستان ۱۴۰۵ همچنان ادامه خواهد داشت و احتمال بروز خاموشی، به‌ویژه در ساعات شب، وجود دارد.
بر اساس برآورد دفتر مطالعات انرژی، صنعت و معدن این مرکز، در سناریوی واقع‌بینانه میزان کسری برق در اوج مصرف تابستان به حدود ۱۳ هزار و ۶۰۰ مگاوات خواهد رسید. در این برآورد، توان تأمین هم‌زمان شبکه حدود ۶۸ هزار و ۴۰۰ مگاوات و میزان تقاضا بیش از ۸۱ هزار مگاوات پیش‌بینی شده است.
@
VahidHeadline
پیام دریافتی:
امروز روستاهای خشکبیجار  از ساعت ۱۶:۴۵ حدود ۱ ساعت و ۱۵ دقیقه برق قطع شد. بعد از قطع برق تماس گرفتم با ۱۲۱ که گفتن قطعی ۲ ساعته کنترل مصرف هست که امروز صبح از رشت شروع شده و عصر به شهرستانهاش رسیده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/76299" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oRuVt1vTFWCkOOtCTnxAqCpgHiBsIeQUCaBYcPYsamASMwtR7_6dVlabxNyFQjH0scXgsd4pdDzwHkiW_Zc-RgUQnhkKWBj4bT2VjOSEpS4IMsqMwlVqOZSrNqbuJv7PcCXCaB2X5rjhu96ZY8-iFG_6mt5nc9wJAJtJfWpr9joCF_OZwL9s5VEh2azFUztyP0oafv8XVXFJeWyIfqiUYA5yQ5LtMJZ0EMFxrVmp1-w_HlDt2-g4lmM9RCi4O2zlchAa1HN07L3iaMAdV9gl8pDg7IlRZBEbHm2UcOLYhUQXramrMiQPz0zbcwF79t1LD__WcJlTZXgO43N5bSKVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه تلویزیونی سی‌ان‌ان در گزارشی اختصاصی که روز شنبه، ۲۳ خردادماه، منتشر شد می‌گوید که حکومت ایران در هفته‌های اخیر بر تلاش خود برای سخت‌تر کردن راه‌های دسترسی به اورانیوم غنی‌شده مدفون در سایت‌های بمباران‌شده‌اش افزوده است.
این گزارش به نقل از پنج منبع «آشنا با اطلاعات و ارزیابی‌های دولت ایالات متحده» نوشته شده، اما به نام و منصب آنها اشاره نکرده است.
سی‌ان‌ان در گزارش خود نوشته است که جمهوری اسلامی در هفته‌های اخیر این تونل‌های زیرزمینی را منفجر کرده و در ورودی آنها مین کار گذاشته است تا دسترسی به آنها را هر چه بیشتر دشوار سازد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/76298" target="_blank">📅 17:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBGwRFu5bEavAfJ4np_Mx3k-tAwqkACRmSwphgeJkflHarphs5cICOFAaU8uyGpTJZg2rMX-7F1KNtS2ZPsI8fYaWHZVylW9O-vwhFoWMzVs0CODCLs9Q-bAgRJvuK5iatreLUaYyrtGTPX6AFMSJjGBALtfXpx_ilPQppBQ7z0jxZhdah78yR-8lyShliCYOWjs9bQT6pOdU2Qr6pdfzKF0WuFBTao4971B933Il7Li4U2mjdgnqyrmWZciqNAgAuOgpYDUZ-zVbJ23XagupLzT9JOaWKycLXv9SxcuOxa-B-E4yXwtmQY_Fas13wXFHzyzNUZzhe7azymQRXYGww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌ها و مقام‌های ایرانی روز شنبه خبر دادند که خدمات چند بانک ایرانی به شکل همزمان دچار مشکل شده و این اختلال تا بعدازظهر همچنان ادامه دارد.
خبرگزاری ایسنا اعلام کرد که «بانک‌های ملی، تجارت، صادرات و پاسارگاد» از جمله بانک‌هایی بودند که همراه‌بانک و دستگاه‌های خودپرداز آنها مختل شده است.
خبرگزاری فارس در این‌باره نوشت بانک «توسعه صادرات» نیز اختلال مشابهی دارد و افزود که «برخی منابع از احتمال وقوع حمله سایبری خبر داده‌اند، اما تاکنون هیچ مقام رسمی این موضوع را تأیید یا رد نکرده است».
ساعتی بعد علیرضا قیطاسی، دبیر شورای هماهنگی بانک‌های دولتی در گفت‌وگو با صداوسیما بدون اشاره به جزئیات درباره دلایل این اتفاق گفت: «رفع اختلال از خدمات بانک‌های ملی، صادرات، تجارت و توسعه صادرات در دست انجام است.»
حملات به شبکه بانکی ایران در سال‌های اخیر سابقه دارد و بارها اطلاعات مشتریان بانک‌های مختلف ایران هدف رخنهٔ سایبری قرار گرفته و در فضای مجازی و اینترنت خرید و فروش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76297" target="_blank">📅 17:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nMbVIi0RSKP4zz_3-G3o1jOK0G_C3lty_mwUSUxlFhhJS_-lm8L7bodJsROhtQ3M2oiB6qWPFxfAGWV945Q9nBXN83xyPbkJlbJy8dr5MLfsRK5dJm3A6u49IRK7IqBLmmJ0NtfObUDucM0SHKuZzfwJaG1dtKzMMrJlnRCoPshF2u6WV92T_ywuN8SiFT7n-YC9lX7HZPfVYkerSi_zcYx1GVDQxwNY5YiP-0jSxrIbKXiQ4obX5oG8f4x7BKHf5OmUxYVf5lAhEKKUmX-J5QWTBBIjhE6UeMc3UcTbHvRHYGHdwCpX9nc1bDdWtEv_pYqdor8OH9If3jIHxo9xQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش تازه «پروژه شفافیت فناوری» نشان می‌دهد یوتیوب میزبان ۸۴ کانال مرتبط با افراد و نهادهایی بوده که در فهرست تحریم‌های آمریکا قرار دارند؛ بخشی از آن‌ها همچنان از طریق نمایش تبلیغات در این پلتفرم درآمدزایی می‌کرده‌اند.
بر اساس این گزارش، ۵۶ کانال به اشخاص و اتباع تحریم‌شده در فهرست SDN و ۲۸ کانال دیگر به نهادهای دولتی و رسمی مرتبط بوده‌اند. در میان نمونه‌های شناسایی‌شده، نام‌هایی از نهادها و رسانه‌ها و همچنین برخی کسب‌وکارها و افراد قرار دارد.
پس از انتشار نتایج این گزارش، شرکت گوگل ۶۳ کانال را ظرف چند ساعت حذف کرده است. گوگل اعلام کرده که به قوانین تحریمی آمریکا پایبند است و اقدامات لازم برای اجرای مقررات را انجام می‌دهد.
در فهرست منتشر شده از کانال‌های شناسایی‌شده، نام‌هایی مانند نو‌بیتکس، و‌الکس، بیت‌پین، رمزینکس، گروه بهمن، ماهان ایر، فارس‌نیوز، پرس‌تی‌وی، ایرنا، بانک پاسارگاد، دانشگاه المصطفی و همچنین برخی چهره‌ها و کانال‌های سیاسی و رسانه‌ای دیده می‌شود. مانند علی‌اکبر ولایتی، امیرحسین ثابتی، بابک زنجانی و مسعود پزشکیان.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/76296" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F6_w8tFKKjtWflgvMJcvnu-XRAAGnYOYT0cgq2XbkdCLnSccYWGU3632iqn57Rs_WVcj2WhUo9BI8oWLCA826pDpV3viqdi4dDLvJgB5tq8ZhTmOVgpLtTq2tDYoWY5iT8kC7wrgKQAoyvntZBNesd2Vq96h4fR46OcSjWT9-S87nyIqAtbvk8-JTKjVZaYx4P6fI6HeNtlQsMZVRAlOfIHMgh0Cmv-1tUDgzZyKFTdegUnkU2XdLvqQyW750iRynjBZarSLQcz8m2vejwQgdCe6RhSo9MbJgMm5T2hqRu6njkFPIQb5eQPlxG2ngkUixuC3dH8XwNEgMnsMgBIyEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور کنترل صادرات با استناد به نگرانی‌‌های مرتبط با امنیت ملی، دسترسی «اتباع خارجی» را، چه در داخل و چه خارج از آمریکا، ممنوع کرده است.
شرکت آنتروپیک، سازنده دستیار هوش مصنوعی «کلود» (Claude)، جمعه ۲۲ خرداد اعلام کرد به دنبال دریافت یک دستور کنترل صادرات از دولت آمریکا، دسترسی به دو مدل پیشرفته خود، «فِیبل ۵» (Fable 5) و «مایتوس ۵» (Mythos 5)، را «برای همه کاربران» قطع کرده است.
این دستور با استناد به «اختیارات امنیت ملی» صادر شده و دسترسی هر «تبعه خارجی» را، چه داخل و چه خارج از خاک آمریکا و حتی کارکنان خارجی‌تبار خود آنتروپیک، ممنوع می‌کند.
آنتروپیک گفت این دستور را ساعت ۵:۲۱ بعدازظهر به وقت شرق آمریکا دریافت کرده است. از آنجا که شرکت نمی‌تواند به‌صورت لحظه‌ای کاربران خارجی را از دیگران جدا کند، ناچار شده هر دو مدل را برای تمام مشتریان غیرفعال کند.
دسترسی به سایر مدل‌های این شرکت، از جمله Opus، بدون تغییر باقی مانده است.
بنا بر گزارش اکسیوس و وال‌استریت ژورنال، نامه این دستور را هاوارد لاتنیک، وزیر بازرگانی آمریکا، خطاب به داریو آمودی، مدیرعامل آنتروپیک، فرستاده و با همکاری اداره صنعت و امنیت این وزارتخانه، تنظیم شده است.
متن نامه جزییات دقیق نگرانی امنیتی را مشخص نکرده، اما به گفته یک مقام دولتی، واشینگتن پس از آن که شرکتی دیگر مدعی شد توانسته سازوکارهای ایمنی مایتوس را دور بزند («جیلبریک» کند)، نگران خطرهای امنیت ملی شده است.
همان مقام افزود دولت پیش‌تر کوشیده بود آنتروپیک را به تعویق عرضه این مدل‌ها متقاعد کند و پس از ناکامی، نامه «کنترل صادرات» را صادر کرد.
آنتروپیک با این تصمیم مخالفت کرده، اما گفته است از آن تبعیت می‌کند.
به گفته این شرکت، روش افشاشده یک «جیلبریک محدود» است؛ در عمل یعنی درخواست از مدل برای خواندن یک کد و رفع ایرادهای آن؛ آسیب‌پذیری‌هایی جزیی و از پیش‌شناخته‌شده که مدل‌های عمومی دیگر، از جمله GPT-5.5 شرکت OpenAI، نیز قادر به یافتنشان هستند.
آنتروپیک تاکید کرد فِیبل ۵ با تدابیر حفاظتی‌ای به‌مراتب قوی‌تر از هر مدل پیشین عرضه شده و پیش از انتشار، هزاران ساعت با همکاری دولت آمریکا، موسسه ایمنی هوش مصنوعی بریتانیا و گروه‌های مستقل آزموده شده است.
این شرکت ممانعت از دسترسی برای یک مدل تجاری در دسترس صدها میلیون کاربر را به‌خاطر یک آسیب‌پذیری محدود «نامتناسب» خواند و هشدار داد اگر چنین معیاری به کل صنعت تعمیم یابد، عملا عرضه هر مدل پیشرفته‌ای متوقف خواهد شد.
این دستور، تنها سه روز پس از رونمایی فِیبل ۵ و مایتوس ۵ صادر شد. مدل‌هایی که آنتروپیک آن‌ها را قدرتمندترین سامانه‌های خود معرفی کرده بود. هر دو بر یک بنیان فنی ساخته شده‌اند، اما تنها فِیبل ۵ با محدودیت‌های سخت‌گیرانه، به‌ویژه در حوزه‌های امنیت سایبری و زیست‌شناسی، برای عموم منتشر شد؛ مایتوس ۵ بدون این محدودیت‌ها و تنها در اختیار شماری از شرکای مورد اعتماد، از جمله شرکت‌های امنیت سایبری و زیرساخت، قرار گرفت.
این دو ادامه «مایتوس پریویو» هستند. مدلی که بهار امسال با توانایی‌های پیشرفته سایبری توجه وال‌استریت و مقام‌های دولتی را جلب کرد و در چارچوب طرحی به نام «گلَس‌وینگ» میان گروهی محدود توزیع شد.
اما اهمیت این ماجرا فراتر از یک مدل و یک شرکت است: این نخستین بار است که واشینگتن از اهرم کنترل صادرات در مورد یک مدل تجاری پیشرفته استفاده می‌کند. این وضعیت نشان می‌دهد سرنوشت یک مدل را می‌توان نه با تصمیم سازنده، بلکه با دستور دولت رقم زد.
چارچوب «ملیت‌محور» این محدودیت نیز کاربران و شرکت‌های غیرآمریکایی را مستقیم هدف می‌گیرد.
آنتروپیک می‌گوید توقف عرضه‌های ناایمن توسط دولت را می‌پذیرد، اما در چارچوب فرایندی قانونی، شفاف و مبتنی بر واقعیت‌های فنی. اقدامی که به گفته این شرکت با چنین معیارهایی نخوانده است.
آنتروپیک این ماجرا را «سوءتفاهم» خوانده و گفته است طی ۲۴ ساعت آینده جزییات فنی بیشتری منتشر می‌کند و در تلاش برای بازگرداندن دسترسی است، هرچند زمان مشخصی برای آن اعلام نکرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76295" target="_blank">📅 17:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZmOITTAjNXtdQY1MqQuksTusFxE1ZsTssuxhUf2uY2PKsb5bOD9KGpZMkxmptvA2YEIskQQU2GOP7SCHyKnXWvVsBPUQcc1QWAF3lftyg0W66Ga0KbxcK-1wdzEU-o-ZosTX9c8AJW9xp6-iIx-Zt8E8qoCIH_4a3JSk3hd9uFeX75Y_HjzdapgjibOQzjjsHNagsxGmzYw9x0Fb-bXYnpuBURZxxdWGZnxFOL1bTT28jzQ0697_tx_qnjijqa6SBU9PVxOOKlI-_94_3bl84RKIE3ZxxX3VWgNSyH_pEtMALf37fTboMzR9lXrECYru0m5jTJeamo8Ue2JSxb-krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ecxfYzg7HkmGT17oTxTLtKAejBLXMlIIo7eKVAznwHHK7S46LQFfGyLZE_HO_lTx-eMeDxEEtrfY-PqWuLpwRvm3r71XASEDSJIn-CQF_bh_3zgxKAnj87LF_YuzflbB1_z-4_KVSKr6nWKryjHp3TYu7Go4ikZc5w6aS0gexdl21Utj49R9Af_WOsADaiHgeWwQdTdjdYid4ieIm8OqNPETUSBKEmI6ybVLVGGM--zvkVZTdBBArMEwOFgXdbVDvdvnvKZNxjtT4xP0MrxkPFrnOsOeHzEqXzYkiZM_oehWwJHHI8NmRQyUJC6I5a9nnjJdCQWGnnC7NYuyvCPgEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری رسمی لبنان روز شنبه ۲۳ خرداد خبر داد که ساعتی پس از صدور هشدار به مردم ساکن جنوب لبنان، ارتش اسرائیل به چند نقطه در این منطقه حمله هوایی کرده است.
ارتش اسرائیل روز شنبه صبح به ساکنان ۲۰ نقطه در جنوب لبنان از جمله شهر نبطیه هشدار داد که باید محل سکونت خود را ترک کرده و به شمال رود لیتانی بروند.
ارتش اسرائیل اعلام کرد این هشدار در پی نقض آتش‌بس از سوی حزب‌الله لبنان، صادر شده است
.
حال خبرگزاری ملی لبنان می‌گوید که هواپیماهای جنگنده اسرائیل چند نقطه از جمله دو روستای سجود و ریحان را در نزدیکی شهر نبطیه بمباران کرده‌اند.
اسرائیل در ماه گذشته میلادی تمام مناطق در جنوب رود لیتانی را «منطقه جنگی» اعلام کرد و از آن زمان این نقاط را بمباران کرده است.
اوایل ماه مارس یعنی تنها یکی دو هفته پس از حمله مشترک آمریکا و اسرائیل به خاک ایران،‌ گروه حزب‌الله در حمایت از جمهوری اسلامی به اسرائیل حمله کرد، حمله‌ای که بلافاصله پاسخ ارتش اسرائیل را به دنبال داشت.
درگیری این دو هنوز ادامه دارد و حتی پس از برقراری آتش‌بس حدود دو ماه پیش، هم ادامه یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/76293" target="_blank">📅 17:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76292">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbA6Cp_AWGGV8CuwQYLjIjmcTUFNo9gCBKwHjTozfO72aTfIZgfkw0kR7sNyaoikmsOTv21kbf0LZSYBmN2sDq6SmnUSO3IDkVq0WsH-vIY0-jc3a_bnArKN4cjGjdRnyQZ064bOToKOxV8HT0FNxi2aLS_CxLIiKhBCbfMX-n1t1vzQ2EevnJMcxnuxMQWUky374rj-zNCj3rfjROK6ry1YDuBETgIJI7e6mMtWqApnvSQwUvPFib0Iv-1jodI4l0Q41Zp9fQwmHi2YLR9i-WxX6nspDhd_csj977KDUR_-HeOxoXYMEceZklB9lpKDbp684IlvPuPdfBnZ9_ovaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر حفظ و نشر آثار علی خامنه‌ای با انتشار اطلاعیه شماره ۳ ستاد بزرگداشت «عروج خونین» او، جزئیات مراسم وداع، تشییع و تدفین دومین رهبر جمهوری اسلامی را اعلام کرد؛ مراسمی که قرار است حدود ۱۲۹ روز پس از کشته شدن او در ۹ اسفند ۱۴۰۴ برگزار شود.
بر اساس این اطلاعیه، مراسم وداع با پیکر علی خامنه‌ای و اعضای خانواده‌اش روزهای ۱۳ و ۱۴ تیرماه در مصلای تهران برگزار خواهد شد. تشییع پیکر او روز ۱۵ تیر در تهران، ۱۶ تیر در قم و در نهایت ۱۸ تیرماه، همزمان با شب شهادت چهارمین پیشوای شیعیان، در مشهد برگزار می‌شود و پیکر او در حرم هشتمین پیشوای شیعیان به خاک سپرده خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76292" target="_blank">📅 17:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76290">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVmecpuremn2jyHY3fcOGwpn2JkZaTHX2cMaWJFHuGDc_bphcKdBxwvTYPeeRxJ7MlI3dbd_I_NPp2azVJeBKCO8j6oQ-Tay9hY1ew91KwEwjkR-d40mdWCyz3fXdW--opQ-tAdve4wpM7ruZHwQcMkxKnaFL-DilkDc2cMFPehlocD645uqrm94YU8g4jwr7LLDXo5AZH6dVjsEKrfqzb1CvMisGutxFjecRs7Jk_y_v8et5lOoEpqb2SUnBLX3haWXT5awnCJvq1jPlj2oVF924YmASQu4ltpb2JNXs7B-VM55-21SuhTrFttovKQHVCy5stnUiRrgi2cq_V5lzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سید آرمان موسوی» ۲۹ ساله، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ در محله مسکن شهر کرمانشاه هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله جنگی به ناحیه قلب او اصابت کرده بود و در اثر شدت جراحات جان باخت. پیکر سید آرمان موسوی روز شنبه ۲۰ دی‌ماه در کرمانشاه به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76290" target="_blank">📅 17:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76289">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trolJwNCVUs_ZdI8HwyszWLH5SRIxHcPp_B_piqmCiBSHnrY9DKPZOFMJHp8W9z01cMVTxqaM9pTWkEE0453nUBLmjvad1ML4UYbuSk3TVh_moNg-NAlOx_to6zgI79rsxwXRzppjgWIlLqLOoxM0uS-W4DhLqeuQHQ5TAk-ZkIlNw0qWp63xEzo3czre8_DVcExhPM3MLBgJNOYuPRW7OriOeNKJ03iM531BzosVPbGXwcO6y2alZnafM-HOFJYGUaSHT_cqNHn2YHH3aeK8HBNAQVnMOklSOipCEucMkJbUXLSe1hbM3tD4eG7wwqqNfu9DxXN1JSW5d7EqRnbKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، در گفتگوی با «فاکس‌نیوز» اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته یا روز دوشنبه نهایی شود».
بسنت با اشاره به اینکه تصمیمات دونالد ترامپ برای جلوگیری از دستیابی تهران به سلاح هسته‌ای، هزینه‌ها و فشارهای کوتاه‌مدتی را به بازار سوخت و اقتصاد خانواده‌های آمریکایی وارد کرد، افزود: «ما درک می‌کنیم که در ماه‌های اخیر شرایط سختی سپری شد و افزایش بهای انرژی بخش زیادی از رشد دستمزدها را بلعید، اما ما در حال عبور از این وضعیت بحرانی هستیم.»
وزیر خزانه‌داری آمریکا با تاکید بر اینکه زیرساخت‌های اقتصادی کشور در حال حاضر بسیار قدرتمند عمل می‌کنند و بازار انرژی به خوبی تامین شده است، خاطرنشان کرد که با حل‌وفصل این مناقشه و مهار تورم، بهای جهانی نفت حدود ۲۵ تا ۳۰ درصد و قیمت بنزین در بازار داخلی بیش از ۱۰ درصد از اوج خود کاهش یافته و روند نزولی قیمت‌ها و کاهش هزینه‌های زندگی مردم با قدرت ادامه خواهد یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76289" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKUBYIIqAIvWjNKBm5K1n20GO1Nu4PKGKbyqU12AZg3sgK3IxwhmV-fSpPEaVXZGt34msTLIFjBX81IEADgya52xJ1nfxzpAMoecApqQj4hNp9XrnjuexxcVycueAQRvlWDOZmP-iBYTMhJHvfrZPsLZP6zWAGqgb2f9S3SWFALmijgo2K1l_2-ohbXl2pviIMvURJxdnCU2jLRdTOHXPRF0VkR3H14Fs1B5HoME5k5QdH8HWB71KGcsUo9CoONhomYVx3AziP0jO8BLJoLqdVN2mj0XkSecOm2RZlPHijYAUOyoWAb5i8hPPn28XdD1C65mQrnAHMoxljGjXaTkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
فرماندهی مرکزی ارتش آمریکا (سنتکام) اعلام کرد که ایران چند پهپاد انتحاری را با هدف حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورده است.
سنتکام در شبکه ایکس نوشت که نیروهای آمریکایی در ساعات اخیر همه این پهپادها را سرنگون کرده‌اند و تردد کشتی‌ها در تنگه هرمز بدون اختلال ادامه دارد.
در این پیام آمده است: «ایران چند پهپاد انتحاری را در تلاش برای هدف قرار دادن کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد. نیروهای آمریکایی در ساعات اخیر همه آنها را سرنگون کرده‌اند و جریان تردد در تنگه بدون مانع ادامه دارد. این گذرگاه مهم تجارت بین‌المللی همچنان برای عبور و مرور باز است.»
پیش‌تر نیز یک منبع آگاه به رویترز گفته بود نیروهای آمریکایی چند پهپاد ایرانی را که به سمت تنگه هرمز در حرکت بودند سرنگون کرده‌اند. این منبع گفته بود پهپادها تهدیدی برای کشتیرانی تجاری به شمار می‌رفتند.
این رویداد در حالی است که تهران و واشنگتن همزمان از پیشرفت در مذاکرات برای دستیابی به توافقی جهت پایان دادن به درگیری‌ها سخن می‌گویند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76288" target="_blank">📅 06:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXy0IXqw7LgU4CNh96SIEYxvzj33EpyANqMVfuoCdGRHtN9vofDig1nsQfrwnN9iqnzBTJP2LzDpcRDHHf6-oX_TJSvWajFq5EIWr0SWg-kf_HGkWDo6dWYYMEWdbZVZyqB-MUeBj0W29y4kWv3IrntcE0-3pv8dyvE8mmNOE87cUsjniPIKCVGxZMcVGUOFRQCmCQgNZPF2IYsCdHIn26m8t7epvR0bvkKXwi8Ec53psRXaIz-f-la8Fq0Gwcc84te2LI63PL_q47MbZ3PpVDFrS85vF7malKxDbmwYPdnIPZSuGgGnbnmVz5a5Ekt0vb5Ku-L_XUgQZ0ZyUj6I1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه امارات متحده عربی گزارش‌های منتشرشده در برخی رسانه‌های بین‌المللی درباره انتقال یا آزادسازی منابع مالی برای ایران را قاطعانه تکذیب کرد.
این وزارتخانه در بیانیه‌ای در شبکه اجتماعی ایکس اعلام کرد که ادعاهای مطرح‌شده درباره انتقال مبالغ مالی از امارات به جمهوری اسلامی ایران، از جمله گزارش‌هایی درباره انتقال ۳ میلیارد دلار، «نادرست» است و هیچ مبنای واقعی ندارد.
پیشتر
رویترز به نقل از چهار منبع آگاه گزارش داد که امارات متحده عربی با آزادسازی میلیاردها دلار برای ایران موافقت کرده و بخشی از این منابع مالی نیز در اختیار تهران قرار گرفته است.
اما وزارت خارجه امارات تاکید کرد که هیچ‌گونه دارایی یا منابع مالی ایران از طریق این کشور آزاد یا منتقل نشده است.
@
VahidOnline
بیانیه امارات، ترجمه ماشین:
امارات متحده عربی گزارش‌هایی را که از سوی برخی رسانه‌های بین‌المللی منتشر شده و مدعی انتقال پول از امارات به جمهوری اسلامی ایران هستند، از جمله ادعاهایی درباره مبلغ ۳ میلیارد دلار، قاطعانه تکذیب کرده است.
وزارت امور خارجه در بیانیه‌ای تأکید کرد که این ادعاها کاملاً نادرست و بی‌اساس هستند و تصریح کرد که هیچ‌گونه دارایی مسدودشده ایران از طریق امارات آزاد، منتقل یا تسهیل نشده است.
این وزارتخانه همچنین از رسانه‌ها خواست دقت را رعایت کنند، به منابع رسمی اتکا کنند و از انتشار یا بازنشر اطلاعات تأییدنشده و ادعاهای بی‌اساس خودداری کنند.
mofauae
درباره این خبر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/76287" target="_blank">📅 01:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76285">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m9tYiY1pWBLNQ_5AlCp6asZf_nLdX_FZstsQv0enJ3HWzNy8_tnR0klalPmFMWqItFNrwqaalA6Y7zXZyz8gLmsy9nx_hCrxd22cq2sxxT-T2BOABxPvKO9qKHOoiV4ObTh2zYugxoZNp_YX94lBUUPYnQmbjYgvYWNERXniYbnt52q9vTXksiA7nJqKZ0BsJ_YueEO8s9_02QuNgF6jCpOd_btZsTtWtT9aNRlFqqGZyHhT2qFelg3DjOMdb_m_fHcQniN0_2N2f8Evt3cafB1Ds6CzwhT00ODs3JxwmAiUY-KjnC2SSoqO9WO6R-0rOq5YnUH3QIj44WvZZJiTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dgErzaP9gRMs2GQmowpI0RE8gog5Lw1OOWMp56zcPAzmGc58X4vXJO3e5HxgdywxLbwEN9IsTWDzhW6VjuA9dAtB1OzuQZGZHA3NbJldz1SnbDx7iCFqdac8O4UyJYoMw70RRfN2L9_v8RuuNfhPv7B-okXtDHDsntv9wcL-7TEvY0RVYbsrLEWznz7XYublLRNEshI22q5QJXwgYdaKdkPmMq18abcyHO9dro34yH0npJ6uXKmB13BjbFtxqwzv2Js6XpnNRsviJ9-rj2kZSd4C48DmLm4e6L1gDtXFyVHJAEtxfeSfFpzgf9ghjq9usSJagHeYlBsQkOMown3JDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مالک شریعتی نیاسر، دیگر عضو مجلس شورای اسلامی نوشته:
خب وقتی در باز بشه و ببینن که می‌فهمن مویوم...
malekshariati
این طور برداشت شده که داره میگه قالیباف پشت همه تصمیماتی است که به اسم مجتبی اعلام میشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76285" target="_blank">📅 01:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76284">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tUeShtB2pYvYTi3j4rEjrJE32kgctGfQ7YEFYNs9v4ig2HIb-yWCcAch5NIYv8sSPeoOY09VSNDyzNJ79XjP0Jg_eZvUX2NrOD-xKGLLH75Zv4sc-Y4x9fArUKZ2eo_4_rggw5SeV5J70m3qxZqZqYjvpkZceVSNKHOIVd_lYZoeNZGkzHrhE0-46xuGZPEV1lICfyaAhiTOATWtbOUyDE8lmOscmR8QRzveDwaLcE7T2zLhlqfxoB6lagm-b1o0Ce1EyE8tXdesSqyAr271lKUTp9jE_750JQtdJKgOLsJjOxb5RSrl6qFrrLtQio3Fu37VCbQYYsEv5i9E_P9SvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم:
استانداری هرمزگان: صدای انفجار در حوالی بندر سیریک ناشی از شلیک هشدار در تنگه هرمز است
خبرگزاری فارس:
شلیک هشدار به کشتی‌های متخلف در تنگۀ هرمز
دقایقی پیش مردم در قشم، جاسک و سیریک در استان هرمزگان شنیدن صدایی شبیه انفجار گزارش کردند؛ گزارشی از اصابت در این نقاط مخابره نشده است.
به گزارش خبرگزاری فارس از بندرعباس، منابع محلی از شنیده شدن صدای انفجار در سه نقطه از هرمزگان خبر می‌دهند.
دقایقی پیش اهالی مسن قشم، مناطقی از سیریک و همینطور جاسک از شنیده شدن صدای انفجارهایی خبر می‌دهند.
بررسی‌های خبرنگار فارس از منابع آگاه حاکی است صداهای شنیده شده مربوط به انجام شلیک هشدار به کشتی‌های متخلف در محدوده تنگه هرمز است.
منابع استانی نیز وقوع انفجار بر اثر اصابت در این ۳ نقطه را رد می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76284" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76283">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwqIhB-cUc8X-BQQ1p_KFErocNKWalESc2FMKXjnXJ5-yO8_ojm1KSuUorsSo3UGtJ370BP7sQ-lvnWCktdkfzfmE0v_NZumv9NgKk4gSRRK_y11gorcoRyq5JMIt_tpixJXEnkI4ZupBiQySJTMb_fWjQk81aPYsZCF1DuH4pXfwqNBxhspeL27zQZHgQv5tDk6brdYxsTCv5_PN-kQ3jZdQiYxwK2aSYZ6FgGBDrdW5UGy_VoWIZQpXyKZQL7f-_8qYrcb7FHAjsFGecUS1jtR8hfgBVwsZFEsEse-9Dhmk_8Bq3qAMQmsQFLf28WyqP3GbpRASSzdH6R4k6xu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره تفاهم با آمریکا به صداوسیما گفت: «احتمالا در چند روز آینده تفاهم‌نامه میان ما و آمریکا امضا خواهد شد.»
او افزود: «امضای یادداشت تفاهم بعد از گذشتن از آخرین مراحل مذاکرات به صورت دیجیتالی و از راه دور انجام می‌شود که اعلام خواهد شد.»
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، شامگاه جمعه در یک برنامه زنده تلویزیونی اعلام کرد هنوز توافقی با آمریکا امضا نشده و مدعی شد که پرونده هسته‌ای ایران به مرحله دوم و نهایی این توافق موکول شده است.
او در گفت‌وگو با تلویزیون حکومتی ایران گفت توافق احتمالی با ایالات متحده شامل دو مرحله است و «موضوع هسته‌ای را به مرحله دوم انتقال دادیم».
این در حالی است که ساعتی قبل یک مقام ارشد آمریکایی به خبرنگاران گفت بر اساس توافق، قرار است اورانیوم غنی‌شده ایران در خاک این کشور نابود شود و سپس به خارج از ایران منتقل شود.
با این حال وزیر خارجه جمهوری اسلامی با اشاره به اینکه نتیجه مذاکرات یک «یادداشت ۱۴ ماده‌ای» است اعلام کرد مفاد آن بعد از نهایی شدن اعلام می‌شود.
وزیر خارجه ایران در گفت‌وگوی خود خبر داد که طبق تصمیم جمهوری اسلامی، «آینده تنگه هرمز و اداره آن مثل گذشته نخواهد بود‌» و ادعا کرد که ایران و عمان بیانیه مشترکی در مورد اداره این آبراه منتشر خواهند کرد.
او در ادامه اذعان کرد که طبق قوانین بین‌الملل گرفتن عوارض از کشتی‌ها در تنگه هرمز امکان‌پذیر نیست و افزود: «اما هزینه خدمات دریافت خواهد شد و این در مذاکرات تثبیت خواهد شد.»
عراقچی اعلام کرد طبق توافق، محاصره دریایی ایالات متحده علیه بنادر ایرانی به‌طور کامل رفع خواهد شد و دارایی‌های بلوکه‌شدهٔ ایران آزاد خواهد شد.
مقام‌های آمریکایی آزاد شدن این دارایی‌ها را به دفعات رد کرده‌اند. جی‌دی ونس، معاون رئیس‌جمهور آمریکا ساعاتی پیش تصریح کرد بعد از امضای توافق، هیچ‌گونه منابع مالی در اختیار ایران قرار نخواهد گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76283" target="_blank">📅 23:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76282">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/USfzDcwLxpWdrHts93zWG9sIxMMyqkqWTCvzdWhMMrm3JswYndz6-dHwQXJ-qtHy1RSmiTNgNhMVyiYfnbvW7AnzxWR19_qKamYYa1bhUOS5wH9hksBOq__rO5r16vWIRDb7FSlVsZmMYVuS4hC5lFb4QEnkG1b5R-Hw0xDAgQ2VP0mTi0T_3VDM_9luVErULgRlnlK5b6vWkfiHds-GbrWH3rchphaLyBE61M4f9uHNLKHd723ggyGkK57p5I6yWTT0CZiVz8559BpjMzKeZPwBxQcm_U0WTbhXFjvCdjKmTQs3XL3ba_5UE2R5h4XzQu7Xd6MfhIePE-Wspmjqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
تعهداتی که داده می‌شوند باید عملی شوند؛ نه اما و اگری، نه عذر و بهانه‌ای. برای توافق نهاییِ پیشِ رو، راه دیگری وجود ندارد.
هرچه بکاری، همان را درو می‌کنی.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76282" target="_blank">📅 22:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76281">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vg2CdDJ7VOEvWEXpzpdja-LRqcqG04nG5P0xi5PiymyrDusicsTdWFoJUqPftUsm7JC_1mxsx4Q1cPkUpKuBBKFCC32qt6TxwHN3TM46vL6PyVGaz_Eh4tOj7o_27XViDfrvv5oRMIfwmz9OGZr86NMp6aw2ThhMh-PEAXSWX8gMYZ6XFENWSLdGO5SLhCwTkw-wbBg_KR4RvlOoXsHmAsHdCk2PelCPXB1r2oPXraZwLK71m2Ux114a78-Y6-W1HdRWt4HA3hVSijoejH8Mol8fcci6mnAQZgioI4SGtJypjCJEjHpVwZXPYA-mCu-hzVVoGkX-_UzO9wjYp0apiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهار منبع آگاه به رویترز اعلام کردند که امارات متحده عربی با آزادسازی میلیاردها دلار برای حکومت ایران موافقت کرده است.
رویترز نوشت که این اقدام نشان‌دهنده تغییر تاکتیکی ابوظبی پس از هفته‌ها حملات حکومت ایران به این کشور ثروتمند عربی خلیج فارس در جریان جنگ آمریکا و اسرائیل با جمهوری اسلامی است.
دو منبع منطقه‌ای به رویترز گفتند که امارات با آزادسازی مجموعا ۱۰ میلیارد دلار موافقت کرده است که
بیش از ۳ میلیارد دلار آن تاکنون پرداخت شده است.
دو منبع دیگر که از این توافق آگاهی دارند، مجموع مبالغ مورد نظر را ۲۰ میلیارد دلار اعلام کردند و افزودند که این اقدام در ازای توقف حملات حکومت ایران به امارات متحده عربی مورد توافق قرار گرفته است.
یکی از این منابع نیز گفت که نخستین بخش به ارزش ۳ میلیارد دلار تاکنون در اختیار حکومت ایران قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76281" target="_blank">📅 22:11 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
