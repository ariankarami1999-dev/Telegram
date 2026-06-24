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
<img src="https://cdn4.telesco.pe/file/vb-4gCgT3fjuSRbbrnPOo42wGj4pGyxEtDkZ06V4ik093q8pDL0-97vf9pNkMpTavujGYx4-TpC4laDbZsX-esXgwHV-EfQK3lUhzrDqBd3lmpnO785yqPnWj2wjPULbqExc3jfyAo1lsdl7SbKwn6-XClM5yGntOL8EBvcrep1umNh-F7WTKHYqGxuvX5bo0_DdCHLa-qUjclpPFj2KJuluPltGrrbDOg90jfSbD6zqs2KuTzmGvBoNaI9MPbEX51Zk-nMdKmfU5ZYKziAm2si_9pQNbD2QN2zaoRo37M8qhajgAw7XfEfBd4Zu0GpKPnS62BENu4G2mxB0enpOjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 20:55:17</div>
<hr>

<div class="tg-post" id="msg-15737">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:ایران تاکنون 500 میلیون دلار مواد غذایی آمریکایی خریداری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/withyashar/15737" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15736">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxbFYJAmTj0YtJfCvjrCMSzwVq5eNOwkBup4T7j7XDT9MEFeXhUj2nrqdpWVVjsxYV3T79LrFKbWgkgqeT_ujfL_0FZdn1aWkr75U49xK6ovzCkO9NK-W_znLOtpnNFe1-mPL7URVCJ4HLziQttp5H7DkJuIRdI791eqg4nF1WnIRU0S8y-3ZssEUHRfk7wFXQo40a9BPZT6wgCwih2_x2mut9j54Q1hM01rFJMATTaUOCQUunvTvWMOyuIlx4egEGUy43UQY10Nk8xmMBDhWHO3_JFWgEsybKaKSTDTefaUuTTSiuCjtUMXxXWxmgQycqjb1XwCAGJGdKc-5ntlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیت‌کوین به زیر ۶۰٬۰۰۰ دلار سقوط کرد
@withyashar</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/withyashar/15736" target="_blank">📅 20:26 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15735">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مرحله دوم مذاکرات فنی ایران و آمریکا ۸ تیر برگزار می‌شود
وزیر خارجه آمریکا دقایقی پیش در اظهاراتی گفت که مذاکرات فنی ایران و آمریکا، روز ۲۹ ژوئن / ۸ تیر در سوئیس برگزار می‌شود. پیش از این نیز وزارت خارجه پاکستان اعلام کرد که مذاکرات ایران و آمریکا هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/withyashar/15735" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15734">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=V68eZh1GOc56Oj1VYrThch2gupZBNXipk3yhphU3fae7f7wjHXwELsnL-OOVJ2GWu8hvPpgbTDvvtAIC8VLkVv4UTFEPe1cyKgXHm6EfeiNVFUSD-qTC8PO5NHhKTbXb-zg03MPy1P46bDOHh6WHY_Qk8k8GjPOi3PRGDrad6IynN-mHzVGGcRkRa-ECx17DEqdOxYgNTf8bNAWexGsna9Ubzgj68Pt8SdRqYty1GUyw-ameadPcYhNJUvmhWEBMsA6eoItGydEH6ifeshxmNTvz-XGaNLimPYsSBv6tgNh0ZnDGrJ3mseyc8mATbAqQoOrRQL_rGHTBeScbqN58zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58bddbc88.mp4?token=V68eZh1GOc56Oj1VYrThch2gupZBNXipk3yhphU3fae7f7wjHXwELsnL-OOVJ2GWu8hvPpgbTDvvtAIC8VLkVv4UTFEPe1cyKgXHm6EfeiNVFUSD-qTC8PO5NHhKTbXb-zg03MPy1P46bDOHh6WHY_Qk8k8GjPOi3PRGDrad6IynN-mHzVGGcRkRa-ECx17DEqdOxYgNTf8bNAWexGsna9Ubzgj68Pt8SdRqYty1GUyw-ameadPcYhNJUvmhWEBMsA6eoItGydEH6ifeshxmNTvz-XGaNLimPYsSBv6tgNh0ZnDGrJ3mseyc8mATbAqQoOrRQL_rGHTBeScbqN58zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : من بیشتر دوران بزرگسالی‌ام را به جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای اختصاص دادم.
آماده نبودم اجازه دهم زنجیره‌ای از هزاران سال تاریخ یهودی به خاطر دستیابی این آیات‌الله‌ها به سلاح‌های هسته‌ای شکسته شود.
به همین دلیل بیشتر دوران بزرگسالی‌ام را به این هدف اختصاص دادم همچنین به عنوان نخست‌وزیر
@withyashar</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/withyashar/15734" target="_blank">📅 19:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15733">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارتش اسرائیل: یکی دیگر از تروریست‌های حماس که در قتل عام ۷ اکتبر به اسرائیل نفوذ کرده بود، از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/withyashar/15733" target="_blank">📅 19:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15732">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال 13 اسرائیل:
نتانیاهو امشب یک جلسه امنیتی درباره لبنان و سوریه برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/15732" target="_blank">📅 19:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15731">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو: از ترامپ اجازه‌ای برای حمله به ایران درخواست نکرده‌ام بلکه تنها آن را به او ابلاغ کردم.
ماموریت ما در لبنان هنوز پایان نیافته است.
@withyashar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/15731" target="_blank">📅 18:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15730">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/832f75f201.mp4?token=e0avm56Og5XrTszOxtxV3Xdz0ccFEC4hugfFnZWz5adTVm1ppNqw79qi-VFjJQwuN_bXs9KaxhqgVOJste0nbIpnP9eFZUPU-fmBCXc1MunfZU2wK71Ns7zKI3WiHsBR7N7LB2rjRKINkoSRUxjDEjKm7ll4cLqq25MWwT-mtKTtrynlWx7ATOlka390MtpTFVwsOME6UB9dCQEKjLWQ_P_iH-ANNfmqb0BZSxMPJpVNJLI6bxTGr39QpmizC3Blox4QhYLXr_93UR0CPMtXrpy3HxjObaG0r6czL8rC5hOs96w4EpCuANn7-bOqQ9JGsGYGH1xelpLxzfq9CemUnD6WgoSm3Ia37Qxri3x9yh0xByE2tnDXaQg_wl9rlIElV8NrfSR3B-U3CJv_b9T7PBwoFmAO9Pb5rvEJBsvc6TsOlIiXGwGQHGmCPBDXnsgfZ7sJ1CYBN59yZHGYV9J883Ou650QStHMUdxwfYHdMat0U0BXnLyjvb6NWcDPmfDZwC-wIa8JliMxxGRummuSxQpxYDffI2DsCzHhjPmifHBuiifX_CYjKxxjh99LSI6dYyhXU8mg8d6OBuy5PHNyEwsjm24wDajE_rzivbL2Ol_DNcGubsSBMYOqZ48CUyFBbgE9fn8KlspK3NL0vqPCxtwFvXCqIEht-MBEfOZARs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/832f75f201.mp4?token=e0avm56Og5XrTszOxtxV3Xdz0ccFEC4hugfFnZWz5adTVm1ppNqw79qi-VFjJQwuN_bXs9KaxhqgVOJste0nbIpnP9eFZUPU-fmBCXc1MunfZU2wK71Ns7zKI3WiHsBR7N7LB2rjRKINkoSRUxjDEjKm7ll4cLqq25MWwT-mtKTtrynlWx7ATOlka390MtpTFVwsOME6UB9dCQEKjLWQ_P_iH-ANNfmqb0BZSxMPJpVNJLI6bxTGr39QpmizC3Blox4QhYLXr_93UR0CPMtXrpy3HxjObaG0r6czL8rC5hOs96w4EpCuANn7-bOqQ9JGsGYGH1xelpLxzfq9CemUnD6WgoSm3Ia37Qxri3x9yh0xByE2tnDXaQg_wl9rlIElV8NrfSR3B-U3CJv_b9T7PBwoFmAO9Pb5rvEJBsvc6TsOlIiXGwGQHGmCPBDXnsgfZ7sJ1CYBN59yZHGYV9J883Ou650QStHMUdxwfYHdMat0U0BXnLyjvb6NWcDPmfDZwC-wIa8JliMxxGRummuSxQpxYDffI2DsCzHhjPmifHBuiifX_CYjKxxjh99LSI6dYyhXU8mg8d6OBuy5PHNyEwsjm24wDajE_rzivbL2Ol_DNcGubsSBMYOqZ48CUyFBbgE9fn8KlspK3NL0vqPCxtwFvXCqIEht-MBEfOZARs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا، بسنت : سلطه دلار خیلی مهمه
همه کارهایی که ترامپ داره انجام می‌ده، دلار رو دوباره محور تجارت جهانی می‌کنه
تو ونزوئلا و حتی مذاکرات با ایران هم می‌بینیم که معاملات قراره با دلار انجام بشه
درکل، همه این اقدامات جایگاه دلار رو دوباره تقویت می‌کنه
@withyashar</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/15730" target="_blank">📅 18:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15729">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به فاکس‌نیوز اعلام کرد که قرار است به بازرسان اجازه داده شود تا مکان‌هایی که اورانیوم ایران در آنجا نگهداری می‌شود، بازدید کنند. از سوی دیگر، ایران قصد دارد در اولویت اول، کالاهای آمریکایی به ارزش حدود ۵۰۰ میلیون دلار خریداری نماید. هیچ عجله‌ای برای ورود بازرسان وجود ندارد و تیم آمریکایی قرار است همراه با بازرسان آژانس برای یافتن اورانیوم غنی‌شده اعزام شوند.
@withyashar</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/withyashar/15729" target="_blank">📅 18:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15728">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
ترامپ: هیچ عجله‌ای برای دسترسی به این مواد وجود ندارد، زیرا پس از عملیات «چکش نیمه‌شب» در زیر زمین دفن شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/15728" target="_blank">📅 17:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15727">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ در تروث : شهردار ممدانی با حمایت سه کمونیست تمام‌عیار به پیروزی رسید و رسانه‌های جعلی هم با سروصدای زیاد و به‌صورت یکپارچه برایش کف زدند. تبریک آقای شهردار!
من دیشب ۱۶ برد از ۱۶ داشتم و به انتخاب میهن‌پرستان فوق‌العاده آمریکایی کمک کردم، اما رسانه‌ها حتی یک کلمه هم درباره‌اش نمی‌گویند.
در دو سال گذشته، حمایت و تأیید من باعث ۲۵۹ پیروزی در انتخابات مقدماتی شده و تقریباً هیچ شکستی نداشته است، با این حال هیچ توجهی از سوی رسانه‌ها دریافت نکرده‌ام!
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/15727" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15726">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=YqOobuRMV23SPN090bL65JqnkT0rV6scDFd18jpWnt1BNrGzDYJ2BwfxcutR3BCdnXmFuBtC9NJZwPdb_7J39Ayq4TsZETukPSS82Hi4EOu3BWyrs7eFshVkR5VEzu4ipU8AiT8hl4mfOY6hnBFNGHwywzWnP5EGiPnvYBCQXwMhLc_KOuL0WYjTDUF3JGjIwXuVB3eO_et1DHpOzxzMgXqciaKz83y2uMRqVvkX2cANFc1Xr4sOp2zAp45eqlGWACiRwmFYekDfx8jWmtSlIb14EUgWbYmdcvHoDqZiM3FfJt3gUXuiGxM-m3JBtg0P10axDQdsWrCbEa5vljvnwRQsgnMx_BtSvUbreRXRt6pxGtMKN4hvPhI2T0yHYvyxa9vWU7-vrJwj2eMo7r5U8EeDT54zoM4mViLP1i_NRqo8O-OIALplaPTQBbd7HMRzyJqcb-e5q_yrS4GUQA5u4qALNh-h4v9BOqq4pDw9nQ9ogK1RPKXCcmunHisqiZlwmu8dVGMVYKWhV7wNkTj6MwGPjkDx05r0gjrzsAje3cFm-D69JGhaecrIvCduiLmmRdrg6cTwVkOwXcsqq70qwkRC_AB_IduNVbX1walTUpwj9k2otkjGQV9y4F2icfPs3_AzPED3HfTGsNnME4m0wpweAd2dEPZ1WBdLxUIlLtE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6227a74ce9.mp4?token=YqOobuRMV23SPN090bL65JqnkT0rV6scDFd18jpWnt1BNrGzDYJ2BwfxcutR3BCdnXmFuBtC9NJZwPdb_7J39Ayq4TsZETukPSS82Hi4EOu3BWyrs7eFshVkR5VEzu4ipU8AiT8hl4mfOY6hnBFNGHwywzWnP5EGiPnvYBCQXwMhLc_KOuL0WYjTDUF3JGjIwXuVB3eO_et1DHpOzxzMgXqciaKz83y2uMRqVvkX2cANFc1Xr4sOp2zAp45eqlGWACiRwmFYekDfx8jWmtSlIb14EUgWbYmdcvHoDqZiM3FfJt3gUXuiGxM-m3JBtg0P10axDQdsWrCbEa5vljvnwRQsgnMx_BtSvUbreRXRt6pxGtMKN4hvPhI2T0yHYvyxa9vWU7-vrJwj2eMo7r5U8EeDT54zoM4mViLP1i_NRqo8O-OIALplaPTQBbd7HMRzyJqcb-e5q_yrS4GUQA5u4qALNh-h4v9BOqq4pDw9nQ9ogK1RPKXCcmunHisqiZlwmu8dVGMVYKWhV7wNkTj6MwGPjkDx05r0gjrzsAje3cFm-D69JGhaecrIvCduiLmmRdrg6cTwVkOwXcsqq70qwkRC_AB_IduNVbX1walTUpwj9k2otkjGQV9y4F2icfPs3_AzPED3HfTGsNnME4m0wpweAd2dEPZ1WBdLxUIlLtE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رشد دارایی ونس و هگس در طی سالها
@withyashar</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/15726" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15725">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=Wk9OqOrP-OKDbdH-YGR4hxJS54m6ihlE3YzJKcFnfKnGygK8shd-Rl4vYhNjGoskT8i2Ch75pP8OfMTcFOip-JKcYQvMXOlo3H-tdyI4j04VGdDVEcJGTBFpAbGX-Fer4BpEtu_i7AUxzaJNU7WNs5_VBWvA-9QPauusbROvp0Y7akTPKfw3pJoXesLtudzLSPvSEUKGTBGrkn4dTt6F3zIAH4zKSqBV8K1QWq9-EBYwy5fF4cba4ackjPD8-2JT2_cbNJAdhdyFGou5J6vcBGnEqzyjelUUlfPsyECv_wbw4tkXRkb9hc6jif7e8iNOXYRwwSiQ2e_pqWqqn8xUUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13a4e4286.mp4?token=Wk9OqOrP-OKDbdH-YGR4hxJS54m6ihlE3YzJKcFnfKnGygK8shd-Rl4vYhNjGoskT8i2Ch75pP8OfMTcFOip-JKcYQvMXOlo3H-tdyI4j04VGdDVEcJGTBFpAbGX-Fer4BpEtu_i7AUxzaJNU7WNs5_VBWvA-9QPauusbROvp0Y7akTPKfw3pJoXesLtudzLSPvSEUKGTBGrkn4dTt6F3zIAH4zKSqBV8K1QWq9-EBYwy5fF4cba4ackjPD8-2JT2_cbNJAdhdyFGou5J6vcBGnEqzyjelUUlfPsyECv_wbw4tkXRkb9hc6jif7e8iNOXYRwwSiQ2e_pqWqqn8xUUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری دولتی لبنان گزارش داد:
یک پهپاد اسرائیلی خودرویی را در نزدیکی شهرک کفررمان در جنوب لبنان هدف قرار داد و دو نفر کشته شدند.
پیش‌تر نیز سخنگوی ارتش اسرائیل اعلام کرد نیروهای ارتش دو عضو مسلح حزب‌الله را که تهدیدی برای نیروهای اسرائیلی در منطقه علی‌الطاهر در جنوب لبنان بودند، هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/15725" target="_blank">📅 17:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15724">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قیمت اونس طلا به زیر ۴ هزار دلار رسید؛ آیا سقوط ۱۵۰۰ دلاری از اوج تاریخی ادامه خواهد داشت؟
قیمت نقدی طلا روز چهارشنبه ۲۴ ژوئن (سوم تیر ۱۴۰۵) تحت تاثیر رشد ارزش دلار آمریکا و افزایش انتظارات مبنی بر تداوم بالا ماندن نرخ‌های بهره در این کشور، برای نخستین بار از ماه نوامبر ۲۰۲۵ میلادی، از مرز روانی ۴ هزار دلار در هر اونس پایین‌تر آمد.
تقویت ارزش دلار آمریکا باعث شد تا خرید شمش طلا که بر مبنای دلار قیمت‌گذاری می‌شود، برای دارندگان سایر ارزها گران‌تر تمام شود.
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/15724" target="_blank">📅 17:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15723">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=GFHn0Quc_QB85__t6dJwkB_Tg4g4wblBFm7vOwJStGNEsyoXRAclQzLmJ5LUBCqPFv7VSDDLrQwzE-bAJexKPAfFHMLX3v35mgCz_ljR4Ps_yEeFPv6rcZ19Iy6hqIL2hjx8FoXsidENfoP-FZXgo2KEBMdYO_F7Qa4iggP9A34o-0XGU2zdH0sCGxBEWljBkP7OvSPsdu4RWAedbpBoVxSNc5udISk9r7Cf9_5mBy3KKru6ZFuid7T5N847N_qf4w_SX6c9omZAXrXbX_ptAoPeGRTo0iMYQlwWINW3WJy1q6pdCfsgZm9-NhIAjKYqf_eotIiyqwTasj0FxcYoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5b8c6375.mp4?token=GFHn0Quc_QB85__t6dJwkB_Tg4g4wblBFm7vOwJStGNEsyoXRAclQzLmJ5LUBCqPFv7VSDDLrQwzE-bAJexKPAfFHMLX3v35mgCz_ljR4Ps_yEeFPv6rcZ19Iy6hqIL2hjx8FoXsidENfoP-FZXgo2KEBMdYO_F7Qa4iggP9A34o-0XGU2zdH0sCGxBEWljBkP7OvSPsdu4RWAedbpBoVxSNc5udISk9r7Cf9_5mBy3KKru6ZFuid7T5N847N_qf4w_SX6c9omZAXrXbX_ptAoPeGRTo0iMYQlwWINW3WJy1q6pdCfsgZm9-NhIAjKYqf_eotIiyqwTasj0FxcYoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، برای دومین مرحله از تور خاورمیانه خود به کویت رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/withyashar/15723" target="_blank">📅 17:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15722">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنتکام: «نیروهای فرماندهی مرکزی ایالات متحده در تاریخ ۱۹ ژوئن یک حمله هوایی در شمال‌غرب سوریه انجام دادند که به کشته شدن یکی از رهبران ارشد داعش منجر شد.
در این حمله دقیق، علی حسین العلوی کشته شد. این عملیات بخشی از تلاش‌های مستمر آمریکا برای مختل کردن و از بین بردن عناصر تروریستی است که در پی حمله به شهروندان آمریکایی در خارج از کشور یا خاک ایالات متحده هستند.
نیروهای سنتکام همچنان در همکاری با شرکای منطقه‌ای به عملیات خود ادامه می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/15722" target="_blank">📅 16:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15721">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بسنت وزیر خزانه‌داری آمریکا به سی‌ان‌بی‌سی:
هر پولی که رژیم تهران دریافت کند، متعلق به ایرانی‌هاست.
نسبت بسیار زیادی از پول برای خرید غذا و داروی آمریکایی استفاده خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/15721" target="_blank">📅 16:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15720">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس‌نیوز گزارش میدهد : پرزیدنت ترامپ روز شلوغی را در واشنگتن دی سی آغاز می‌کند و آماده می‌شود تا به کنگره برود، جایی که طبق گزارش‌ها قرار است با جمهوری‌خواهان سنا در مورد قانون متوقف شده «نجات آمریکا» ملاقات کند.
در طول اقامتش در کنگره، قرار است قانون «جاده قرن بیست و یکم به سوی مسکن» را نیز امضا کند.
همه این اتفاقات پیش از جلسه کاخ سفید بین ترامپ و مارک روته، دبیرکل ناتو، در اواخر امروز رخ می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/15720" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa3x8-5lXiWNn41KfW_NkCppWpJ1MV_Rqqh8O2KGhVHGlPBDCGiJmwlb6uqp2pF1O56plnWDpwhhhgl4ISw_mEBkq7x0nSu1vqa8SXVydgfYgneV-RXfogaL0tgdlASTwvs6-KRvBtISN-hQOmpksmL47VW63cwNU7q0r9X9Nr1mtAv1nK_S5e0I9pM1IUoYFY3HzfWtDeNN7ylSesN8Qw7ZPqT_Bqi2QQEKTtTYGJW1aO4byFqamH5ka3sLNAMJH2ostY0wBI40dujGWToSD8K69aIDclGVlFysH44C9ltA-1_zAL9DqHDrYFi0bkRoIPg8jgoZHIXSRf-DxVdNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در ‌تروث : «ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دردسرساز رسانه‌های جعلی، هیچ‌گونه عوارض، هزینه بیمه یا هیچ نوع هزینه دیگری از کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌کند. اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت.
همچنین، هیچ پولی از سوی آمریکا به ایران پرداخت نشده و هیچ بخشی از دارایی‌های ایران نیز مستقیماً در اختیار این کشور قرار نگرفته است. ما بخشی از دارایی‌های ایران را که همچنان کاملاً تحت کنترل ماست، برای پرداخت به کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا از آن برای خرید ذرت، گندم، سویا و سایر محصولات استفاده شود.
ایران به‌شدت به مواد غذایی نیاز دارد و ما این اقلام را منحصراً از ایالات متحده برای آن‌ها تأمین خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم.»
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/15719" target="_blank">📅 15:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6aaIA1uSc_AM4nZYcF3keX4tV2W0H77Nh5NFLh7DEve4gUlNMEx99WLLc1DjeaToCYOPWQY0EhhGCa10gKmQ_vZADE33xgK0rYEIQnHftG4eak-jDUionR4GbkEgicVEdTVzyiohftobP4taiBeeEa4VTImLwj_Q7WY7GCzfPAbiof3giTLeUg2gyhr9k6-oxqZXCuis1siH65MDjkv7RdhVBavM0CQouceu0519AfremvVEBOqvLvLH1Qp6cGKh-vYtqsg9OAg8qqC1jNxMfMzkfYs0o1WIvFtCYzMcal6FJ5VC6yLPZ7PewgdnE1-mGFEmiBlHrgbErs0SFwXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارن پالیسی:
توافق ایران زمینه درگیری‌های بیشتری را فراهم می‌کند
!
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/15718" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">با اعلام راکستار،قیمت بازی GTA6 مشخص شد.
نسخه Standard:
80 دلار، معادل 12 میلیون تومن.
نسخه Ultimate Edition:
100 دلار، معادل 16 میلیون تومن.
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/15717" target="_blank">📅 14:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حسین پاک، خبرنگار مستقر در لبنان: در نقض آتش‌بس دیروز اسرائیل در لبنان، ۳ شهید داشته‌ایم
دشمن درحال برنامه‌ریزی بلندمت جهت اشغال منطقه طیبه است.
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/15716" target="_blank">📅 14:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قالیباف در باکو: تفاهم‌نامه امضاشده برای پایان جنگ «اعلام شکست آمریکا» است
او در بیستمین کنفرانس اتحادیه مجالس کشورهای عضو سازمان همکاری اسلامی (PUIC) در باکو گفت: «تفاهم‌نامه ‌اسلام‌آباد نه نتیجه فشارو اجبار، بلکه حاصل مقاومت و اقتدار ملت شجاع ایران بود... یادداشت تفاهم اسلام‌آباد تبدیل به اعلامیه شکست آمریکا شد.»
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/15715" target="_blank">📅 14:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15714">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">غضنفری، نماینده تهران : امیدواریم قالیباف سر عقل بیاد و مجلس رو باز کنه.
@withyashar</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/15714" target="_blank">📅 14:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15713">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">معاون وزیرخارجه خطاب به ترامپ:
نمی توانید با هیاهوی رسانه ای، سیاست "راه بینداز و جا بینداز" را پیش ببرید.
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/15713" target="_blank">📅 13:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15712">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ee6905e4.mp4?token=gR4Fc7ad1NgJO1Fi4u19M9hGHppkUPywEf77TYSsKWXPKlt3Nt0UAfHyKmMkcbinIqXQMqKGjA8f-WCzU17RwDK1_nvu612Gz3kGjao6i7W1R5pUcyKeAy3TsYY0cawdWMjtLYqas4Rjn6f6gpSd2AhWclVlHzLK0Mh-lIdg3gQCPsuUsDJdqRdkUZ33V2CotRKQ5KZxvcXmv5hUBYsIoiPA1pD62XxFwwwBd-7piiIwPvzqPiGGr4Lv7Fz6LCgrnsKHJeSY5-l3H0y6O1kx86mfUocOG4rJ0NoS9lZh5TYCK9Cj8zlEn-YWT3EyOjHiYmerSD5i-s8_G1l1aFZuxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ee6905e4.mp4?token=gR4Fc7ad1NgJO1Fi4u19M9hGHppkUPywEf77TYSsKWXPKlt3Nt0UAfHyKmMkcbinIqXQMqKGjA8f-WCzU17RwDK1_nvu612Gz3kGjao6i7W1R5pUcyKeAy3TsYY0cawdWMjtLYqas4Rjn6f6gpSd2AhWclVlHzLK0Mh-lIdg3gQCPsuUsDJdqRdkUZ33V2CotRKQ5KZxvcXmv5hUBYsIoiPA1pD62XxFwwwBd-7piiIwPvzqPiGGr4Lv7Fz6LCgrnsKHJeSY5-l3H0y6O1kx86mfUocOG4rJ0NoS9lZh5TYCK9Cj8zlEn-YWT3EyOjHiYmerSD5i-s8_G1l1aFZuxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک سنگین در‌ جاده شمال
@withyashar</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/15712" target="_blank">📅 13:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15711">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر خارجه پاکستان: برای عبور از تنگه هرمز، هزینه یا عوارض یا اجازه یا کسب مجوز وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/15711" target="_blank">📅 13:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15710">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پایان شهادت نتانیاهو در پرونده فساد مالی
بنیامین نتانیاهو پس از ۹۸ جلسه استماع در ۱۸ ماه گذشته، دفاعیات خود را در پرونده اتهامات فساد و رشوه به پایان رساند و با اشاره به شرایط سال‌های اخیر، گفت که «۱۰ سال جهنمی» را تحمل کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/15710" target="_blank">📅 13:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15709">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند. @withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/15709" target="_blank">📅 13:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15708">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وقوع تیراندازی درپایتخت ترکیه،آنکارا
رسانه‌ها از وقوع حادثه تیراندازی در آنکارا خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/15708" target="_blank">📅 12:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15707">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اختلال بانک‌های کشور برطرف شد
با اعلام شرکت خدمات انفورماتیک، اختلال خدمات کارت محور بانک‌های کشور برطرف شد.
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/15707" target="_blank">📅 12:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15706">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آژانس ایمنی هوانوردی اروپا به شرکت‌های هواپیمایی توصیه کرد همچنان از پرواز در حریم هوایی ایران خودداری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/withyashar/15706" target="_blank">📅 12:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15705">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رویترز: قراردادهای آتی نفت خام برنت به ۷۵.۷۴ دلار کاهش یافت که پایین‌ترین سطح آن از ۲۷ فوریه گذشته است
@withyashar</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/15705" target="_blank">📅 12:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15704">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdtavdZa4ExuZWDdn9YXjEkIshwidM5Kov0GKLOO4qEAwjWtURfAAqMGfN114fN7uXUP2X13lPER3XntxerxiXGH_X2-KPT0GPZR2W3R5JpZyZQn0Gp75hPZjE8ENGrdXHSpHuWIXBu2IKgxU7nrQM3d6PRC7ci5EqXdGnAgHCnYcuxXy4sYKaUCK8slkZ2vztXriE1H_R_yG6ItA0cGenkpgwu9tRohg77zGsKbgRJ85_qofsq3Bsz7QdByBKelVqscKEZUVwxdop6Ie-mNnfcGajzzr2Ya2f_sRv-tHpnBZ2Z2rjp39HdGqJfuTg6QMTKm01Y34lKvCap0FvcY4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در تروث ‌: ایران رو کاملاً تحت فشار گذاشته بودم؛ در آستانه عقب‌نشینی بود، حاضر بود تقریباً هر چیزی که ما می‌خواستیم رو قبول کنه و واسه اولین بار تو چند دهه گذشته، احترام فوق‌العاده‌ای برای آمریکا و رئیس‌جمهورش، یعنی من، قائل شده بود.
ولی سنای آمریکا تصمیم گرفت تو بدترین زمان ممکن، یه رأی‌گیری بی‌معنی درباره قانون اختیارات جنگی (War Powers Act) برگزار کنه؛ رأی‌گیری‌ای که به بزرگ‌ترین حامی تروریسم تو جهان این پیام رو میده که آمریکا از کاری که من با اونا می‌کنم، راضی نیست و باید متوقفش کنم.
با این کار، عملاً به دشمن کمک کردن و دلگرمی دادن.
این سناتورها فقط کار من رو سخت‌تر کردن، ولی به هر شکلی که شده، کار رو به سرانجام می‌رسونم؛ چون من همیشه کارها رو به نتیجه می‌رسونم!
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/15704" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15703">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هم اکنون دلار در تهران به صورت ناگهانی از 165هزار تومان عبور کرد.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/15703" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15702">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjTtDFQ53jSxas752-zOrf2_eaOK9ZJsVvcVYZh_ZQb79wScp6ndeMaePRNZzlIkU_2TgzgUrvBKXIJIlntKOoCIBlL_xTndfy4vCHrl3bpYYO0qb7v0HTPKybLZwPQwDJlWWGswaDSdKZDq1vbCsWu4_fY_KS1vxjjcqe_HUzgv_VVrX9rU4RoKu3Bjvl803cWI82yqjAQkmups1hdxoC99HokrLW6O0tyHMqnZaz9kerGGR5860QQSsuTrMdwdtiUVx_nuHyOwQGcBbg2eabylkXERG_ujJf53GVWJnBzLOqG2DmtMAiN9AY8KKGNyqZRPaMPmsSp6YcscEj6K0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد @withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/15702" target="_blank">📅 11:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15701">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">هگست:  اولین آزمایش سامانه پدافندی جدید «گنبد طلایی»، با موفقیت انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/15701" target="_blank">📅 11:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15700">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پاکستان: مذاکرات فنی میان آمریکا و ایران هفته آینده از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/15700" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15699">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVYQu6_QTcKgAlP_BQyAywBB9zRp5nh0WfFc16ljuvnF0IIZ5vwoWjxG6onIcv9FW5XHJXtBXikOaF_7swIQM2w88ccvE4xa0JkIhM4drhztJJobvXY_Jo5-QQlu4IUwYQdzjJ3gnA10-NsG0EpRJxGvzWh55MCPAdT0gD8KxQCicv13XV1Q7J5LWrrKubGMKQdTBMZejw-C5aLRJywaNlyrMb41Fhe7QchU7qwE9V-ffqSQWgu4SoJempTxOtGcYzzfakr3m77oyj7uXxKOs8ShR5-pdo4uX4eg30pLTCNo9MzVLHJSmOFpEp9K2wByL7-XZVb66Ln1fNbMHbSBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین بروزرسانی از استقرار ناوهای نیروی دریایی آمریکا:
در منطقه سنتکام، دو ناوگروه لینکلن و بوش به همراه ناو آبی‌ـ‌خاکی تریپولی همچنان در منطقه حضور دارند و بخش عمده توان رزمی دریایی آمریکا را تشکیل می‌دهند.
دست‌کم ۱۷ فروند ناوشکن از کلاس آرلی برک نیز در دریای عرب، دریای سرخ و شرق مدیترانه حضور دارند که توان قابل توجهی در اختیار نیروی دریایی آمریکا قرار می‌دهند.
در غرب اقیانوس آرام، ناو هواپیمابر واشینگتن نخستین گشت عملیاتی خود در سال ۲۰۲۶ را در دریای فیلیپین آغاز کرده و ناو آبی‌ـ‌خاکی باکسر نیز در دریای چین جنوبی مشغول فعالیت است.
@withyashar</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/withyashar/15699" target="_blank">📅 10:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15698">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی: از تأسیسات هسته‌ای ایران بازرسی خواهیم کرد
ما معتقدیم که بازرسی از تأسیسات هسته‌ای ایران در اسرع وقت بهترین گزینه است
اولویت اصلی ما مشخص کردن محل ذخایر اورانیوم غنی‌شده با خلوص بالای ایران است.
ما از محل اورانیوم غنی‌شده با خلوص بالا اطلاع داریم، اما مهم است که ایران ما را از آن مطلع کند.
به زودی با ایران برای تعیین تاریخ بازرسی‌ها و جزئیات مربوطه مذاکره خواهیم کرد
آژانس ما بازرسی را انجام خواهد داد و این به تهران بستگی دارد که واشنگتن یا ناظران دیگر را دعوت کند.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/15698" target="_blank">📅 10:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15697">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15697" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15696">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca023fa4e.mp4?token=twlu8y7bj97P6fc98_8dMQPvXkvWrBlQoLZMoGNZ7IpXv1j98DCROVk68IiGjyFpEYOugZTa0eZt80BZvOms5WmdjiK5N4CywMAlZCA-ayxsP8GQU1jFpZ68yb4mEqwDuxZybKxpKWrR4Zx0nbhxSbqEGT4hl1Uo3ch9teo72cQftGKaOm96Z8tzX80MhcRXKSf2LWRbIsfzQ8Vyj_jkLxgSv1blvd402ydzabHmxfk93eGv1QPot76eXLd9PjJd5ANp4_R8GxjEIZ9IbFgSg5MGKQjG6maLUq6vgMTt_6DAeLD8DGHTtI0wz7MEtbJANxRya3iDJGNen6pmLv3AoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca023fa4e.mp4?token=twlu8y7bj97P6fc98_8dMQPvXkvWrBlQoLZMoGNZ7IpXv1j98DCROVk68IiGjyFpEYOugZTa0eZt80BZvOms5WmdjiK5N4CywMAlZCA-ayxsP8GQU1jFpZ68yb4mEqwDuxZybKxpKWrR4Zx0nbhxSbqEGT4hl1Uo3ch9teo72cQftGKaOm96Z8tzX80MhcRXKSf2LWRbIsfzQ8Vyj_jkLxgSv1blvd402ydzabHmxfk93eGv1QPot76eXLd9PjJd5ANp4_R8GxjEIZ9IbFgSg5MGKQjG6maLUq6vgMTt_6DAeLD8DGHTtI0wz7MEtbJANxRya3iDJGNen6pmLv3AoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ که توی پیجش قرار داده و مضمونش بر اینه که هیچوقت نمیزارم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/15696" target="_blank">📅 10:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15695">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6xgU1Bii5a_0FYHJDtvXFAW2tSWutSen6Usjhh-_FXDkpuN3ADICEAx4GEbABsWCscZ96rx5albT_UOrF6VOTkBNSmatU0sW0JQ_AeXlmcDQtvDrMgTttcTkutIdAI46PwHSBnaJrDGMeZyhJz9I_0ff3EL5zYXEcXLQLwP5fB3Q4Hp6uu9uNhX-Ljg7E39FWT3gSYluTS7fNSdByXzP8iYJb-dFMUautSWmJgaMdCc7VxnyZkOettzB6fI5oAqq7KZJjgUUVujPh_ZXHOoOFgpR7HSoAOCrBGT7rQL-I_ZXY-Ugff1eseHUaST3AQEmPdzqLt4Itox01l5ubjS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۳۰ نفتکش حامل نفت خام ایران که دستگاه‌های فرستنده و گیرنده AIS آنها فعال است!
اکنون به سمت آسیا، چین، ژاپن و کره جنوبی در حرکت هستند و بیش از ۵۰ میلیون بشکه نفت حمل می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/15695" target="_blank">📅 01:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15694">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ‌ در‌ پنسیلوانیا:  ایران قلدر خاورمیانه بود.
ما باید این مسیر را انجام می دادیم. باید به ایران می رفتیم.
شما نمی توانید اجازه دهید که خاورمیانه و سپس ما را منفجر کنند، اگر این امکان پذیر باشد. ما قبلاً آنها را می گرفتیم، اما آنها اسرائیل را منفجر می کردند. آنها می توانستند کل خاورمیانه را منفجر کنند.
به توافق صلح تاریخی با ایران دست یافتیم
ایران عالی بوده است. اگر ایرانیان هوشمند باشند، منطقی خواهند بود؛ در غیر این صورت، مجبور خواهیم شد کار را به پایان برسانیم که احتمالاً کمتر از یک هفته طول می‌کشد.
اما فکر می‌کنم همه چیز برای آن‌ها خوب خواهد شد. آن‌ها کاری که باید انجام دهند را انجام خواهند داد زیرا ما می‌خواهیم این کار انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/15694" target="_blank">📅 23:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15693">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد  سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است. @withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15693" target="_blank">📅 23:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15692">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سنای آمریکا به پایان جنگ با ایران رأی داد
سنای آمریکا تصویب کرد که ادامه عملیات نظامی علیه ایران مستلزم کسب مجوز کنگره است.
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/15692" target="_blank">📅 23:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15691">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال ۱۴ اسرائیل نقل قول‌های اختصاصی از احمد وحیدی، فرمانده سپاه پاسداران، خطاب به مقامات ارشد رژیم را منتشر کرد.
1 «ما رئیس جمهور ترامپ را به زانو درآوردیم. ما به آنچه می‌خواستیم رسیدیم. طبق معمول، غرب احمق فکر می‌کند که در عوض چیزی از ما دریافت می‌کند، که البته هرگز اتفاق نخواهد افتاد.»
2 «هدف ما در حال حاضر این است که آمریکایی‌ها را در تنگنا قرار دهیم. هرگونه تخلف، هر چقدر هم کوچک، به ما اجازه می‌دهد که تهدید به بستن تنگه هرمز کنیم و ترامپ و مردمش با هر چیزی موافقت خواهند کرد.»
3 «ترامپ فکر می‌کند پولی را که به ما می‌دهد صرف خرید کالاهای آمریکایی خواهیم کرد. این هرگز در طول عمر ما اتفاق نخواهد افتاد.»
4 «حالا باید به آمریکایی‌ها بفهمانیم که اسرائیل بازیگر بد خاورمیانه است. هدف این است.»
5 «از هیچ چیز دست نکشید. تهدید کنید. و در صورت لزوم، از مذاکرات کناره‌گیری کنید.»
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15691" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15690">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نخست‌وزیر پاکستان: هفته آینده با مجتبی خامنه‌ای در ایران دیدار خواهم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15690" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15689">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام…
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15689" target="_blank">📅 22:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15688">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان، زیر چنل تبلیغاتی از افرادی می‌آید که در بازارهای مالی شرکت دارند. اینها از طرف خود تلگرام است. حتی اگر من هم تبلیغی بگذارم، دلیل برای این که شما جایی پولی پرداخت کنید و تایید من باشد نیست. به هیچ وجه این کار را در هیچ شرایطی در هیچ کجای اینترنت انجام ندهید. در غیر این صورت مسئولیت با شماست و توسط حرص و طمع خود شما انجام گرفته. به این مسئله دقت کنید و
فقط از تحلیلها و مطالب آموزشی افراد استفاده کنید
. هیچ پکج یا هیچ پرداختی به هیچ بی ناموسی انجام ندهید.
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
از توجه شما به این مطلب سپاسگزارم، یاشار</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/15688" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15686">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoblTKJQgAB_SmQeUoigo_FB3C-EOr2Gd6IDToAQF9bW7TWtnbcSsoJrgPQ4rJhrBgoW-tAwI_fiJWvr4_idCoe77NFBLlGVdhq21iaf7qZzsQzWtZwS4X6BowwGMA49ARL7tcf4w2_NHyTQSV5p4f2EIDBi0eR9pp0j5Tuz7WnwQcfaQVa2MxW0eXWdTnX2OwHdy1hrHMzEssykYtyZkJZX3ZHDq0oUU2AyXOJvC37ajlBvNH_W31FB4vIFVkfz44dG3FR4kxaRURZno6BQeH_rkhUoR7m8bd-mWuZC58nIt028qoyoyW6BJd2vbmywYt7oJdqtcOYiMIonp7epBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل با انتشار نقشه تونل کشف شده جدید حزب الله نوشت:
حزب‌الله با حمایت مالی جمهوری اسلامی طی سال‌ها(صدها میلیون دلار) شبکه گسترده‌ای از تونل‌ها، انبارهای تسلیحاتی، سایت‌های موشکی و مراکز فرماندهی در جنوب لبنان ایجاد کرده ، هدف این زیرساخت‌ها حمله به اسرائیل بوده
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/15686" target="_blank">📅 22:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15685">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=aS4BnQnEPgUYW8udy6MC2XZRoYhHJFFXxvFUrm8z3Ee_cYx_q5QEwptC9BYN6JuevruE8FCzKy5D_DPibf9gy6qtBOSzaZ34xVvtZkCv5nj7Nc79xkzvzEN1uZ-WV5k2hH3pinnkQ8xBG6Mo2SPl3_C6jBAdEUpzKH8qgH5v9gCfBEXmGoqxnOB1O83RbfIpdyoWlXwUW2E9eTufzXjRrN73vlwO3CCLUeHoq0j_iqv0MMIHM4XCtJXQU1QHsbr2tKkhMxZn1uer2JEMwi3HnM60rHyc-eJWfNgSpTfPWFdXi1xV1twPc-ObcrD23vGAb2gK84Oixqfmk7-VjfaUSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7644ffed31.mp4?token=aS4BnQnEPgUYW8udy6MC2XZRoYhHJFFXxvFUrm8z3Ee_cYx_q5QEwptC9BYN6JuevruE8FCzKy5D_DPibf9gy6qtBOSzaZ34xVvtZkCv5nj7Nc79xkzvzEN1uZ-WV5k2hH3pinnkQ8xBG6Mo2SPl3_C6jBAdEUpzKH8qgH5v9gCfBEXmGoqxnOB1O83RbfIpdyoWlXwUW2E9eTufzXjRrN73vlwO3CCLUeHoq0j_iqv0MMIHM4XCtJXQU1QHsbr2tKkhMxZn1uer2JEMwi3HnM60rHyc-eJWfNgSpTfPWFdXi1xV1twPc-ObcrD23vGAb2gK84Oixqfmk7-VjfaUSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک یه ویدیو از محرم پست کرده
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15685" target="_blank">📅 22:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15684">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7cLNzmXhNDLDIDi57_gyEgV-wjgjzpn0Bq_QxwlQrRf2NO8f1Wyu4R5fJsec0K2nbar4QP5Gq2qAvEuRDKEBR7-47WO41Lllw0nZft2UH6Vj0GOJVluP5v4FmhLoK3-Xct-tMk-sJR3GNWwQuqdEJU1eL_CPhr4MZ-W4sxnBGae8HTIfvq6T7SymrVlWeoQk7ZPTt6fzTt3bkCcVQz4svhZOklNtMjycEaZ10EWtV6i3uHD6AdRttg-FkkFoQbEUS0Szd9K451150eVLbHtMfZtQ2NMoUXFIX2EQt9cKYbvprLyb_2DyBb_6LwBVQFYburs2fYdPb6SY6EKcRnFUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبینا محمدعلی‌پورثانی پس از ۱۰ روز پیدا شد
سیدامیر احمدی، دادستان عمومی و انقلاب بهارستان:
مبینا محمدعلی‌پورثانی، دختر ۱۹ ساله ساکن نسیم‌شهر، پس از ۱۰ روز بی‌خبری پیدا شد.
این دختر پس از پیگیری‌های قضایی و اقدامات انجام‌شده، پیدا شده و در سلامت کامل به سر می‌برد.
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15684" target="_blank">📅 21:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15683">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بنیامین نتانیاهو، نخست وزیر اسرائیل، در مصاحبه ای با شبکه سیان بی سی به وضعیت شکننده حکومت جمهوری اسلامی اشاره کرد و فروپاشی آن را اجتناب ناپذیر اما از نظر زمانی غیر قابل پیش بینی دانست.
وی با مقایسه شرایط کنونی ایران با وقایع تاريخي غير منتظره ای نظیر سقوط دیوار برلین و تحولات رومانی، تأکید کرد که شکاف های عمیق و پنهانی در زیر لایه های این نظام در حال گسترش است. نتانیاهو با بیان اینکه حکومت ایران در حال حاضر به شدت ضعیف شده است، تصریح کرد که اسرائیل همچنان بر موضع خود مبنی بر کمک به مردم ایران برای سرنگونی این رژیم پافشاری می کند؛ هر چند زمان دقیق وقوع این اتفاق در کنترل یا انتخاب آنها نخواهد بود و به روند گسترش این شکافهای داخلی بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/15683" target="_blank">📅 21:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15682">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: هیچ عجله‌ای برای ورود بازرسان آژانس بین‌المللی انرژی اتمی به ایران وجود ندارد
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/15682" target="_blank">📅 21:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15681">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رکورد تاریخی رونالدو در جام جهانی ۲۰۲۶ کریستیانو رونالدو با گلزنی مقابل ازبکستان در جام جهانی ۲۰۲۶، به نخستین بازیکن تاریخ فوتبال مردان تبدیل شد که در ۶ دوره متوالی این رقابت‌ها موفق به گلزنی شده است. این گل که در ابتدای بازی(دقیقه۷) به ثمر رسید، به انتقادها…</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/15681" target="_blank">📅 21:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15680">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رکورد تاریخی رونالدو در جام جهانی ۲۰۲۶
کریستیانو رونالدو با گلزنی مقابل ازبکستان در جام جهانی ۲۰۲۶، به نخستین بازیکن تاریخ فوتبال مردان تبدیل شد که در ۶ دوره متوالی این رقابت‌ها موفق به گلزنی شده است. این گل که در ابتدای بازی(دقیقه۷) به ثمر رسید، به انتقادها علیه این ستاره ۴۱ ساله پایان داد.
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/15680" target="_blank">📅 21:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15679">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرنگار : ایرانی‌ها می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
ترامپ: بلوف میزنن ، اونا داخل به ما گفتن و ما ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15679" target="_blank">📅 21:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15678">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ارسالی : یاشار جان بانک رفاه و سامان و بلو بانک هم از کار افتادند ، ساعت شش عصر
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15678" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15677">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=GQaXbaey5NSU88Y8D0VIXHUCuPXuY0EKhd5egYYxZ0tW0_CjTorm9ai9-ByvR4gcObPBHNVMxyZZNY-oYbw-iyvWNbdCbzCpuGA81dV8aa23giO94AdcIyxrR1rMyShD7_Xk2arjfk1qLhqNYpFCzPlh6vDmqW2IPzCNY9tCr1bxky9LP81Xd5qdpB3UqCtHLZVQYyItDe3U5QvNmFL5-cRELWfE5-LqsFwAk7MutAidne-b5awrCArYId10_NixjGMRDsqEr8otTDmUvtSjZZ93-WcOGtwhhPWyRYD9Vead0aDxJyxuqR6defN5VgoupOwDtmZ5UN43xZ6IbrGadw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26cd4a0fb.mp4?token=GQaXbaey5NSU88Y8D0VIXHUCuPXuY0EKhd5egYYxZ0tW0_CjTorm9ai9-ByvR4gcObPBHNVMxyZZNY-oYbw-iyvWNbdCbzCpuGA81dV8aa23giO94AdcIyxrR1rMyShD7_Xk2arjfk1qLhqNYpFCzPlh6vDmqW2IPzCNY9tCr1bxky9LP81Xd5qdpB3UqCtHLZVQYyItDe3U5QvNmFL5-cRELWfE5-LqsFwAk7MutAidne-b5awrCArYId10_NixjGMRDsqEr8otTDmUvtSjZZ93-WcOGtwhhPWyRYD9Vead0aDxJyxuqR6defN5VgoupOwDtmZ5UN43xZ6IbrGadw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان دکترای افتخاری از پاکستان دریافت کرد
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15677" target="_blank">📅 20:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15676">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تتر 163K
@withyashar</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/15676" target="_blank">📅 20:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15675">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/15675" target="_blank">📅 20:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15674">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcvFUIO9TM0iwWPRfJv-7xLI2GlNg_k9cLxicCPgaZmq-X0CV1ugTxGH76g7rG9dihV49cnS1bQn-vBW64Nf8-Enm3mr_Rc7LlX34_cUTm_sylpWXFvlLGvcyfSD8InMoadUo8bpVYA9oSg41RvCI7gqExMmkuHHMKHx3UxSSLua67Kw34lA3v_QPehtU-KiMnvyglRdRg-d2afxW3rJqsHVn4-dXPI3-n-rSOIspLKb0j1Adq877_1J8CYFu6PIgv8A8eA1WGbVCSXpk8Xvz9bhuOJT0yXP9qmUqwBGtZm66uUMdV8jhaw9EReZe5TX-wFPi7fviTrCeFEugpb4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شواهد نشان میدهد مدیران دفتر انتشارات مجتبی خامنه‌ای دقیقاً امضای ابزار یکسان ، نسخه یکسان و سیستم عامل یکسان دفتر انتشارات قالیباف استفاده کرده اند.
در‌نتیجه هر دو نامه قالیباف و مجتبی خامنه ای با یک کامپیوتر نوشته شده در ابتدا و بعد از اوایل ماه ۶ میلادی، اوایل خرداد ماه، رایانه را از مک به رایانه ویندوزی تغییر داده‌اند.
@withyashar
پیشتر در ویدیو اتاق جنگ گفتم که ای آی دست ممباقر هست!</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/15674" target="_blank">📅 19:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15673">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ریاست جمهوری لبنان:
ونس و وزیر خارجه آمریکا خواستار تشکیل یک کار گروه آمریکایی، لبنانی و ایرانی برای تثبیت آتش‌بس شدند
آن‌ها گفته‌اند که ترتیبات مربوط به حوزه اختیارات این کمیته و نحوه تشکیل آن، در دست بررسی است
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15673" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15672">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">هاآرتص به نقل از منابع آگاه: تل‌آویو علاقه‌مند است در مذاکرات واشنگتن راه‌حل‌هایی پیدا کند که مداخلهٔ ایران را از تحولات لبنان دور نگه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/15672" target="_blank">📅 18:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15671">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPI_CWAk4PmKyCqLrXSZBevdDl4W5_676ukBai5WYX1LjzOU4QXEX3esA77su0KpRSv6ZhWfSTF2diLeQoLb1r-EbdI0G0hz26_NewzGC27uTHzG4_E8ZuBMRZBdG-Qe5nTFtj60MAW_BigxiPHzSSDetp9zgOCgrCue71C2jzQm2gFIspz-sO_n47i0ByNRSF7K0D9fOdYgoJCEjdRkqbWmd-6oK0P3wNYqM2-qomnebt3ylIQzef-G3wM1CW82KXbmGr4liru7msNNKSwh2egAEVcgciYv3YviQpEqvTSoLgcwCXt-JiIHRD7gyYo9o31nR9vJjo4qaTYYrFL5Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ما هستیم ناو ها هم هستند نگران نباشید
ناو هواپیمابر USS جورج اچ. دبلیو. بوش (CVN 77) در دریای عرب(شمال‌غرب اقیانوس هند ابتدای دریای عمان جنوب ایران ) در حال حرکت است.
دو ناو هواپیمابر به فعالیت خود در خاورمیانه ادامه می‌دهند در حالی که نیروهای آمریکایی همچنان حضور دارند و هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/15671" target="_blank">📅 18:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15670">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">عمان و ایران بیانیه مشترکی منتشر کرده‌اند که در آن قصد خود برای ایجاد یک مدیریت مشترک آینده برای تنگه هرمز را تأیید می‌کنند
این بیانیه همچنین به طور ضمنی تأیید کرد که مطابق با استانداردهای بین‌المللی
هزینه‌هایی برای خدمات دریایی اعمال خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/15670" target="_blank">📅 17:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15669">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فایننشال‌تایمز
:
با وجود افزایش سطح تردد کشتی‌ها در تنگه هرمز، مالکان همچنان سردرگم هستند؛ این وضعیت در حالی شکل گرفته که ایران کشتی‌ها را تهدید به عبور از مسیر نزدیک سواحل خود کرده و آمریکا مسیر عمان را پیشنهاد می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/15669" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15668">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هم اکنون حمله پهپادی هدفمند به خودرویی در جنوب لبنان،گزارش ها از ترور چندین عضو حزب الله.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15668" target="_blank">📅 17:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15667">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شهباز شریف نخست وزیر پاکستان: مذاکرات ایران و آمریکا شامل دارایی‌های هسته‌ای، موشک‌های بالستیک و دارایی‌های مسدود شده ایران خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15667" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15666">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPVH9KB-_yl21H_uIIghFY2A1ZTNxyOT4DjVdB4gVbV_0-dk0O_OyHlrhAbhfYAY8H5yqahSLE2lyzwJ7oTjEX1FVpUUMrXRAYJsxPGj8jcdtLqGqb5aZqF2Nj76wo533EmUVcTrMTOmh_v8FfYjBBg1jc7Y5tKoxj_ayZDVI33KWuk9oMg_QSToyhhDURKj1gtH6Gcb2LqeX84Pt5DzyYPMBVxDNpihmnz4cBoiesYgVONxGdvqFwSQWBpsBUQxh1e9SJtsyzZwCpH6Wa7kJLHm1TbK0ARTRt8d0kr6t2ScghsxQy9HQgg59Qt7GV8RCW3aT05j4Yp3NveLnCVLgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز دایرکتی از طرف یکی از شما دریافت کردم که گفت از‌ کارمندان رتبه دار بانک است و این قطعی نه هک است نه چیز دیگری و به طور عمد از طرف خود رژیم انجام شده وی افزورد تقریبا با یقین میگم پایین اوردن دستوری قیمت ارز و طلا،حاکمیت و دولت با سرکردگی همتی و سیف میخواهند در قیمت های پایین فقط خودشون خریدار مطلق باشن و یک نوسان جانانه از بازار بگیرن با اختلال عمدی در سیستم(چون میدونن سرمایه دارها میدونن قیمت برگشت میکنه به بالا و پولشون رو میکشن بیرون که طلا بخرن،اما با قطع عمدی و به گردن هک شدن)
در نتیجه از دوستان هکر قدیمی دوران جوانی جوییا شدم که در امنیت سایبری بانکها کار میکنند. آنها به من گفتند که بعد از عملیات اکونومیک فیوری که آمریکا انجام داد که شامل محاصره دریایی هم میشود و تمام زیرساختهای اقتصادی رژیم را هدف‌ گرفت رژیم ضربه های مهلکی در رابطه با ارز خورده و این ادعا درسته و میخوان پول رو از جیب مردم جبران کنند دوستم گفت شعبه ها هم دسترسی به هر انتقالی را دارند ولی دستور این است که بگویند قطع هست
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/15666" target="_blank">📅 15:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15664">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNuwCXLU5em-kzrwEsO6OOG2hZh1J-bncWfDi5yOZUZOAmDNERFH2zrUnncBZqg8zxw8T_tKKsaz2EcfbWz9l_ziNBK0xS2vuj7oWAgnO0bdezs2l-m6JxHaCMSGntCjVhui4kNBomZAxHbeM7_DTBtP7kzr-z_jkEw4uG2jFPQWtjm-XS7tBsujqR2w4zAmwMvCBLvFYSjMLCtmYrCr2w3ygLF3v5sUOS3Sh_aTS0opFsC77oheuoGcfkH2sP8Oz7JyFpOFVxTIo98QOAVfyhwxSt-UICH-dCGv8uXwbygbCH4ADvhFt5yJvgeWn8UCWhsgaMhhFsoR0Ty6kh1JcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی جنگنده F-15 که در ماه آوریل بر فراز ایران سرنگون شد، به مقام‌های اطلاعاتی گفته است که پیش از اجکت کردن، چندین پهپاد ایرانی را دیده که به‌صورت هم‌زمان و هماهنگ در آرایشی شبیه «عروس دریایی» در حال حرکت بوده‌اند؛ به گزارش سی‌ان‌ان و به نقل از چهار منبع.
این روایت باعث بحث در جامعه اطلاعاتی آمریکا شده درباره این‌که آیا ایران توانسته قابلیت پیشرفته‌ای در زمینه پهپادها یعنی «شبکه‌سازی مش‌مانند یک‌به‌چند» (one-to-many meshed networking) را به نمایش بگذارد یا نه.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15664" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15663">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmC_ZZtq13TRoKLtn00VA3HFJEVHwT_lXNAGpfaUVaZxt0f3ov9OZH0Lr5yefk_WB2pXfm_vjb9iidEJ0MzLKCv_KnHahgG207SD6iF319Ki3PdppWddCrFwjlF4h2GXQZb0Au_9cf93UEzfyLfU7e742xzkvtDVJBpM4M59URW3Ep5bQh_qWG57s7NEhKZD8z1FjW22VA8zrfc_tGnoDtaCEqwWBYr3ohZdjkkvL1ZxTzV-hOd4hCXdfpNvR2mDTh0xFPO4IJRLXmy-pKZHioMEH78pQIs3Smaz3Vxe7woTtWIQMlxU_wcuu55U6NwpJiu1bXOIE-h1ixJ-7NtVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : با وجود اعتراضات و اظهارات نادرست آنها، همراه با تبلیغات مکرر اخبار جعلی که همه تلاش خود را می‌کند تا پیروزی آمریکا را کوچک و بی‌اهمیت جلوه دهد، ایران به طور کامل و جامع با بازرسی‌های هسته‌ای در بالاترین سطح برای آینده‌ای نامحدود (بی‌نهایت!!!) موافقت کرده است. این امر «صداقت هسته‌ای» را تضمین خواهد کرد.
اگر آنها با این موضوع موافقت نمی‌کردند، مذاکرات بیشتری صورت نمی‌گرفت! بر اساس این و دیگر امتیازات عمده‌ای که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و هیچ محاصره دریایی بیشتری اعمال نشود. با این حال، همه کشتی‌ها در محل باقی می‌مانند تا در صورت لزوم محاصره دوباره برقرار شود، که در این مرحله بسیار بعید به نظر می‌رسد.
پول و یا تحریم‌هایی که خزانه‌داری آمریکا آزاد می‌کند، در حساب امانی تحت کنترل آمریکا قرار می‌گیرد و صرف خرید غذا و تجهیزات پزشکی، به طور انحصاری از ایالات متحده، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما خواهد شد.
این‌ها چیزهایی هستند که ایران به شدت به آنها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است که اکنون کمک کنیم، قبل از اینکه خیلی دیر شود. مذاکرات به خوبی پیش می‌رود!
@withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/15663" target="_blank">📅 14:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15662">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDb75IuPxtMBFm1RhdXGFUahaYpdCQOy1D5RZfPuf4M5Q0mWn3nidwVr8B5zinhxNH9fbOs4b1DkKk16621kd8S8aGtqZ_WD7aj2bRzZVg79WTxyJw2my-9NAxy7NyJXd-XGnCMIhwu-r-kKxw5GZYwbnhX9tTsblD8gFhk1Ng6Xzknjp1z0Kugnn9396gXTRt_wRZIdd6MScoepYWTIILc4Omkr6vvusPGj6-67FW6xtligbM_n6VEibuNpQ0nwIYvibygpb4gWdQx29EhrCznZFU-Rp5dudGV49Jt5pA1CT9ZLv1ETO1KwoTgKa04xjFEn9zUxTfZ_W92fK2CKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد اسلام‌آباد شد
وی در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15662" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15661">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=baa3QtucvBE2vBRt4LoHq4VsuFQQunpcbDlrwi5ixPwaN3ckzi5ziGvKFULoOTMQpD8qAV-Z-VbbjqXMZhv5t7xAVjkZgkJjlfkIZh2QaHXdvjdIu7XnTcnJDwc1qyu6zTOALWy8fRVSbwuImf4mbs4zc16p31ExReCVB8M7n_gBcpD670XOoZKiAUx9IKzm_pX921cEmrEQjfNBEzfP-f9loZe5uE3Id-jFNQKsP7hzj-kx__0iOhvrnbdeMJdeurYAvo7g--lQbr7UIQcsPqy7iVhbp2Skuh_BOL_R-uqQWe4aDSOgZvpkfZMPZtBMKqN9OlGf2K-JxBlxwDDGnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9264c7b6d7.mp4?token=baa3QtucvBE2vBRt4LoHq4VsuFQQunpcbDlrwi5ixPwaN3ckzi5ziGvKFULoOTMQpD8qAV-Z-VbbjqXMZhv5t7xAVjkZgkJjlfkIZh2QaHXdvjdIu7XnTcnJDwc1qyu6zTOALWy8fRVSbwuImf4mbs4zc16p31ExReCVB8M7n_gBcpD670XOoZKiAUx9IKzm_pX921cEmrEQjfNBEzfP-f9loZe5uE3Id-jFNQKsP7hzj-kx__0iOhvrnbdeMJdeurYAvo7g--lQbr7UIQcsPqy7iVhbp2Skuh_BOL_R-uqQWe4aDSOgZvpkfZMPZtBMKqN9OlGf2K-JxBlxwDDGnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه ! شرکت خدمات انفورماتیک: تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود. ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی،…</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15661" target="_blank">📅 14:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15660">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رژیم : هک شدیم ، داریم روش کار میکنیم و مشخص نیست کی‌ درست بشه !
شرکت خدمات انفورماتیک:
تیم‌های فنی و متخصصان امنیت سایبری در حال رفع اختلالات ایجادشده هستند تا امکان بهره‌برداری دوباره از خدمات فراهم شود.
ضمن عرض پوزش بابت وقفه پیش‌آمده در انجام امور بانکی، از تمام کاربران و مشتریان محترم تقاضا می‌شود ضمن حفظ صبوری و شکیبایی، اخبار و اطلاعات تکمیلی در خصوص زمان بازگشت به وضعیت عادی را صرفاً از طریق درگاه‌های اطلاع‌ رسانی رسمی و مراجع ذی‌صلاح پیگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15660" target="_blank">📅 14:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15659">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است  معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است. @withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/15659" target="_blank">📅 14:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15658">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">روزهای شنبه و یکشنبه ۱۳ و ۱۴ تیر، تهران و دوشنبه ۱۵ تیر، کل کشور تعطیل است
معاون اول رئیس جمهور اعلام کرد در روز سه شنبه ۱۵ تیرماه استان قم و پنجشنبه ۱۸تیرماه استان خراسان رضوی تعطیل است.
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/15658" target="_blank">📅 14:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15657">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سفیر ایران در لبنان در واکنش به حمله به جنوب لبنان: هرگونه نقض تفاهم‌نامه در لبنان، چالش‌هایی را برای روند مذاکرات صلح ایجاد خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/15657" target="_blank">📅 13:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15656">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اختلال دوباره در بانک‌ها
@withyashar
🚨</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15656" target="_blank">📅 13:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15655">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vivqD06yUqj7If01BJhW8oZpSRytCxBBkxoTHjYOQLUTWS2KmeNP0oXBmyOOWl6Sd2VGXVMRee_1e8ziygZmQU5luhHh5h0dPcxwM3LLnXnRnnIj3binOJcbz2rhHJ-38G1Wo4E0LYPYuklR0PE-o5lQsYhF1gVpZK3uQg-KcQ4W4X8omcakkLzVTqJz0U9THdAZdoF1sN8qbFB5cyAhq-L_5rhUnjru6NSrDaJKSWXMztzspnrfaQFK2kyoRsF3THuuf-aJbH3x16tCDfF47etfstcl1kmNHHYBtztD_R_K-5Otax2LjowUMDgqXi5KSkA39LsDc6CYKw5LuJNX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقض دوباره آتش‌بس ،حمله اسرائیل به جنوب لبنان
@withyashar
🚨</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/withyashar/15655" target="_blank">📅 13:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15654">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم @withyashar</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/15654" target="_blank">📅 13:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15653">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رادیو ارتش اسرائیل: تا زمانی که حزب‌الله کاملاً منحل نشود، از منطقه الشقیف در لبنان عقب‌نشینی نمی‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/15653" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15652">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نتانیاهو: حمایت دوستان آمریکایی‌مان را بسیار ارج می‌نهم، اما نیازمند رهایی از وابستگی و ساخت یک نظام تسلیحاتی مستقل هستیم
@withyashar</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/15652" target="_blank">📅 12:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15651">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3AvVOABXHa9-opgMdqFBIryHwq8sMMc2pLBf6TtIGmC1t3j4ioNfjK5DIpTkQegR3OR7zofIX7McQDzFd6ll-Gm6xuY86HClsjWZ2pbuC2PkWYRFlJyjQIzO8IZxwMlGI21JKoIZowobIzzOFTA12q6lFs4BeTG6LyOfRjjmk6v85yaC-sRylotMl04ewBN6K7PultY62DjGQWe2VXLZDNrfutZmtwkEkTJKaN4QGTsaYM9aMLFjYz3Kb58jL8rV3Z0XtZxSl5FNEAdh1lt1MHrXoz-yhBlBt3u0FLBAmfMi08jKjZijneZHxOPTbm9YwgPQaQoP-nNSVXLheQPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون ۷ سوخت رسان شامل، ۵ فروند سوخت رسان KC-135R و ۲ فروند سوخت رسان KC-46A پگاسوس نیروی هوایی آمریکا در منطقه خلیج فارس فعال هستند.
همزمان، دو فروند KC-46A با نام عملیاتی BOBBY 81/82 از پایگاه RAF Mildenhall انگلستان به پرواز درآمده و برای الحاق به یک یگان جنگنده در حال عملیات‌اند.
همچنین بر‌اساس گزارشها پرواز CUBE 31 شامل چهار فروند جنگنده F-35 تفنگداران دریایی آمریکا در حال انجام مأموریت بوده و هماهنگی‌های عملیاتی و ارتباطی لازم را در جریان پرواز برقرار کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/15651" target="_blank">📅 12:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15650">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پلتفرم دریانوردی کپلر:
۳۶ کشتی دیروز از تنگه هرمز عبور کردند که این بالاترین میزان تردد در این تنگه از نخست مارس تاکنون است.
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/15650" target="_blank">📅 12:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15649">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل بن گویر:
اگر آمریکایی‌ها فکر می‌کنند ایرانی‌ها برنامه هسته‌ای خود را رها خواهند کرد، آن را لغو می‌کنند و از تمام رویاهایشان برای نابودی دولت اسرائیل دست می‌کشند، بسیار ساده‌لوح هستند.
@withyashar</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/withyashar/15649" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15648">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: خودروسازان آمریکایی تولید سلاح را آغاز خواهند کرد
رئیس جمهور آمریکا در کاخ سفید به خبرنگاران گفت: «آنها برنامه‌هایی برای تغییر کاربری کارخانه‌ها دارند. ما قصد داریم سلاح‌هایی از جمله موشک‌های پاتریوت، موشک‌های تاماهاک و موارد دیگر تولید کنیم.»
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15648" target="_blank">📅 11:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده پس از تخلیه از پایگاه هوایی العدید در قطر به دلیل جنگ ایران(یک روز قبل از جنگ)، به این پایگاه بازگشته‌اند. حداقل ۱۲ فروند در حال حاضر حضور دارند.
@withyashar</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/15647" target="_blank">📅 11:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15646">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بقایی: توانمندی دفاعی و موشکی ایران هیچگاه موضوع مذاکره با هیچ طرفی نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15646" target="_blank">📅 11:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15645">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الجزیره: «تغییری بزرگ» در سیاست آمریکا؛ ایران اکنون می‌تواند نفت خود را با قیمت کامل بفروشد
این اقدام صد‌ها میلیون دلار درآمد اضافی برای اقتصاد ایران به همراه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/15645" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15644">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مایک والتز، سفیر آمریکا در سازمان ملل:
جمهوری اسلامی ایران با بازگشت بازرسان هسته‌ای به ایران موافقت کرده و این اولین گام برای توافقی گسترده‌تره.
برخلاف برجام، این بار بازرسی‌ها باید در هر زمان و هر مکان ممکن باشه.
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15644" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15643">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عماد الدین باقی: طبق بند 2 توافق ایران و آمریکا، از این به بعد شعار مرگ بر آمریکا یا سوزاندن پرچم این کشور و لگد کردنش تو مراسم‌ها و اجتماعات رسمی (مثل نماز جمعه) ممنوعه.
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/15643" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15642">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">https://t.me/boost/withyashar
یه لول اومدیم پایین ایموجی کم شد لطفا اگر کاربر پرمیوم هستید بوست کنید و اگه نیستید از دوستانتون که هستند درخواست کنید بوست کنند</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/15642" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15641">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">@withyashar
FPV  آتش بس و</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/15641" target="_blank">📅 01:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">@withyashar
شصت روز سنگین</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/15640" target="_blank">📅 01:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15639">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=eSpz-fzfAQRwvV9po3F5qPAmKA9kqVq34Y2zu2Rb3BhD1ceJnj3UwpUnQoAviE9S0ag57mJCXvBiri0rSJ_iNCfy8yxpqiDSjQCXUsqc1dP3yEI4CNB81h4JxaZIPtTCozQL2JL4LNqngdvxDpUkxosj7JM8m-sTALxO1be76PA-5DlXcFRUH7p87f0QrURasqwVFJFYxZuyK9nNJxpm4ic3yaP9LXhxUzzOEA3wOZtL5-n39QTTxvSP3KnaKadYdsKBetitO6OBt_r-LsXqrP-yxQIicjngnI9uto2dQM0sfiXoDIg-LFFXeR0c5gfERnmBHB34WgGy29TFXybaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc8773aac7.mp4?token=eSpz-fzfAQRwvV9po3F5qPAmKA9kqVq34Y2zu2Rb3BhD1ceJnj3UwpUnQoAviE9S0ag57mJCXvBiri0rSJ_iNCfy8yxpqiDSjQCXUsqc1dP3yEI4CNB81h4JxaZIPtTCozQL2JL4LNqngdvxDpUkxosj7JM8m-sTALxO1be76PA-5DlXcFRUH7p87f0QrURasqwVFJFYxZuyK9nNJxpm4ic3yaP9LXhxUzzOEA3wOZtL5-n39QTTxvSP3KnaKadYdsKBetitO6OBt_r-LsXqrP-yxQIicjngnI9uto2dQM0sfiXoDIg-LFFXeR0c5gfERnmBHB34WgGy29TFXybaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا می‌توانید تضمین کنید که ایرانی‌ها از سود فروش نفت برای بازسازی ارتش خود استفاده نکنند و فقط برای دولت بعدی آماده شوند؟
ترامپ:
خب، آن‌ها قرار نیست این کار را بکنند، قربان. خواهیم دید، اما قرار است پول را برای خرید غذا برای مردمشان استفاده کنند، چون در حال حاضر مردمشان خیلی گرسنه هستند و آن را فقط از ما می‌خرند — ذرت، سویا.
تباید پول زیادی باشد. امیدوارم پول زیادی باشد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15639" target="_blank">📅 00:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من آنچه باید انجام دهم را انجام خواهم داد
با یک تماس تلفنی میتوانم محاصره را برگردانم
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/15638" target="_blank">📅 00:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ: هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران شود. @withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/15637" target="_blank">📅 23:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قالیباف: اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/15636" target="_blank">📅 23:54 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
