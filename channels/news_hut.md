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
<img src="https://cdn4.telesco.pe/file/DU2-na1WjWUc_h5KyPaiN5CZV4lQ2Xs6FneOJHQALp1Yn3RPFgJwfuziGqRfzEWKEty_iKoRFU_PtqFR-BknLcuNY11FstUuuMZvSM-szLVy8oPHYf0Gro6sAMro30qREdZ8dCNIIogTr-iARYUCg4FCbac21dDsfj9pG4HTaDI-5u1WHjAGgPvBod_rj6MdGJzEN8Nyx1s3yEsusTkNkV95YfscocmpwOtrhR9wPiqzVEHFc5EMJQl_g54o_jXXCybr5pn1lGRUmdBnDYVpsWxhZi8q8vvvlzH2HNQYnNQzBnQjov0QRYvB1jvJTKb5imHfnr6H36YL0G_Aa6aP0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 133K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 21:27:45</div>
<hr>

<div class="tg-post" id="msg-65120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">به گفته باراک راوید خبرنگار Axios، به نقل از دو مقام آمریکایی، یک تفاهم‌نامه ۶۰ روزه توسط تیم‌های مذاکره‌کننده ایالات متحده و ایران مورد توافق قرار گرفته است و در حال حاضر منتظر تأیید دونالد ترامپ، رئیس جمهور ایالات متحده و تصمیم‌گیرندگان ارشد در ایران است. طبق این گزارش، این تفاهم‌نامه شامل بیانیه‌ای مبنی بر «بدون محدودیت» بودن تردد دریایی از طریق تنگه هرمز، رفع تدریجی محاصره کشتی‌ها به بنادر ایران توسط ایالات متحده متناسب با افزایش تردد آزاد دریایی، تعهد ایران به عدم پیگیری سلاح هسته‌ای و تعهد به برگزاری مذاکرات در مورد از بین بردن اورانیوم غنی‌شده با خلوص بالای ایران در بازه زمانی ۶۰ روزه خواهد بود.
علاوه بر این، طبق این گزارش، این تفاهم‌نامه شامل تعهد ایالات متحده برای بحث در مورد کاهش تحریم‌ها برای ایران و آزاد کردن دارایی‌های مسدود شده ایران خواهد بود. همچنین قرار است در مورد از سرگیری جریان تجارت و کمک‌های بشردوستانه به ایران بحث شود
@News_Hut</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/news_hut/65120" target="_blank">📅 19:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⭕️
توییت جدید اسکات بسنت وزیر خزانه داری ایالات متحده.
دولت ایالات متحده هیچ تلاشی برای اعمال سیستم عوارض در تنگه هرمز را تحمل نخواهد کرد.
به ویژه عمان باید بداند که وزارت خزانه‌داری ایالات متحده به شدت هر بازیگری را که مستقیم یا غیرمستقیم در تسهیل عوارض تنگه دخیل باشد، هدف قرار خواهد داد و هر شریک مایل به این کار مجازات خواهد شد.
همه ملت‌ها باید هرگونه تلاش ایران برای ایجاد اختلال در جریان آزاد تجارت را به طور کامل رد کنند. روزهای ارعاب تهران در منطقه و جهان به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/65119" target="_blank">📅 19:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65118">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/65118" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65117">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2tQV-lgxsA2oY2yJ_D_r-did-9be8VQFHBWxbx_qX-BjAe--TvujKaPYUhxrNGmaQuBk11ooZnYHqXHIW0snH4KhYFqWQGsAPi0DJ7GdKr2By3VOeQ5gUrN5vm2FSdAx8Ka22h_ji5b8xIjmEnNpogZeiDdxG2WO1omkkAyx46An95Pip2YgvTyp3aNJ84dLTDD069zWXhAJ7V38QGa0uICmX5pExKltmtntfUdZHRd8pIvl2zyn-Ob84gQLhJeiI20WOgLMhp03DY1xcKFCI0SgdNqoHuzAAR2rzBVucjiLIhdX8t9DdT99IddHLMauwViFh02EZqwsxrkdUtj5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g7
📱
@winro_io</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/65117" target="_blank">📅 19:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65116">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyhvUhalEbSzvEkA92yYm_59-vnWPnL-iylKamg-dSPifr4MGj5OEX2JSE-ZBM2ezKVw3i6GkQ7ccLU3ydeQrxbUUdd_mexQgTa5HdmfPQKmuZP3L6IDkPBz6okw2AtUW99SfBh_eytLonqI3c28bzssRAiVSj22KbQvobreCrRlIy5ovLTI5N41QgPS4izIiaPiijhGyhyrbo2liUCw5dy2zkHC072g45ZNiv2_3NEtSKC8vjhPAUyLVuKIE_PiIZXd20GyXdEkbHZPZFoH6w8dcMUFi0fprSnLIOp2Qxpq2gZy6U_8Ek2N1EugeKWtF4kKSG-dDs6-5MjAVWYIXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📰
آکسیوس: اکثر شرایط تا سه‌شنبه نهایی شده بود و مذاکره‌کنندگان ایرانی بعداً اعلام کردند که تأییدیه‌های لازم برای امضا را دریافت کرده‌اند. ترامپ در جریان توافق قرار گرفت اما به میانجی‌ها گفت که «چند روز» برای بررسی آن می‌خواهد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/65116" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65115">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbGAXzDzNqJhpVmjsKH-nEbvcw7tVx7tIjPqajVVhw5_uURbRYaSplgkoH_YdyHL-Smar4bB12J7yWane_WwTjkj-pze5W_TSFsDBF0dfhwRt5yH1yFeNAAWifngBohokcugdVsc9h6bsDXmnG8NFzi0I9BONWce8SKvJOWA-BKc_xT87ggKYS5vVGKzB2lPbPJV1CjaVOOU84KvjJSPHzp1h2AaQT2ZeGCSXsf1AFzODoVvv6jmfAqsyFYzksrNps556cYHHVsfKuDNGCMELbuEAwd_HMqw4_aMBtHbFzo0Pz7iJlgwTo8E5HtyBuOpnKDyW4DHs8eOMpwFfhcSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوارنگاره جدید میدام فلسطین از حرف جدید مجتبی خامنه‌ای درباره اسرائیل؛
" رژیم صهیونیستی 15 سال آینده را نخواهد دید"
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/65115" target="_blank">📅 16:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65114">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fKaBv1jxVmO4oNYsfVUaCRP0jwUIGcc17LWpqAY4hkeMcsPqIiJ1fgugG1SX3ddQuOs3fSbGWmgwF5Jyu3mNXBdM301lAmk_-jPrzywuHXetY6jPBhwWhLoP7ON2N7Rs1ngUlDQGcod6rjmy4pGU4-X1VpLHxzzvIGMv0mqhFkhv7N_lB5146bQYxy5af60LP7bk5Wy0rvjqOMlSwwtK71KHrY1oQEqn0PMeLGm7YAavz3iEKGw-8GZuuS3BVgVT2QtdTW-KOuHnxFkAe42c0AWQU_LJ20hchjfYOCJcxsrBuwN9MZXbuY_r99fR8cxhkA5KQH-uZz6O-ak-7-mISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا پشمامم حقیقتا ریخت
✔️
➡️
تبانی نتیجه دقیق ضریب 15.00 رایگان
😳
10 میلیون ببند 150 میلیون ببر تضمینی
💸
فرمای تضمینی و صدرصد رایگان
⚜️
🌟
https://t.me/+BDjkK6j2gcQ3MGFk</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/65114" target="_blank">📅 16:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65113">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR15UxL4V-kYmpr-sXQs0Bg-uSh6QpfJ0ygnS_eBTROcKu1835FLlvFZitYM5AtWzw8iLw182epx5RthX2qIF3Qi9HdCf_LhLa0vDgnEuBAPnLx5IUEjb4d_wYbv0dLmSycEWVHrVVLMldFKqijBlwmg6ZCkcdQTpEakj53-iDX4aQ3PeGzq_imoIczdvsxrQA9JobE5aDO__LQnHYTf2D-8nT1sa9yeatT9AxeQqoTwshect_XiQ_qLD6-dg5wEmxn6BaIZFHdjlE0U-ntiZ6asGosmjd8uJcnIG7jre32EQgnQqoYgRKdy3ygett7Vl1tC-hdAcP0E1V1oEt6bFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⁉️
نت بلاکس
: سه ماه پیش در چنین روزی Iran دسترسی به
اینترنت جهانی
را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با
فیلترینگ
شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/65113" target="_blank">📅 16:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65112">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حملات تازه اسرائیل به جنوب لبنان؛ تل‌آویو از هدف قرار دادن زیرساخت‌های حزب‌الله خبر داد
ارتش اسرائیل اعلام کرد حملاتی را در جنوب لبنان انجام داده و زیرساخت‌های متعلق به حزب‌الله را در منطقه صور هدف قرار داده است.
ارتش اسرائیل در بیانیه‌ای کوتاه گفت این عملیات علیه «زیرساخت‌های حزب‌الله» صورت گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65112" target="_blank">📅 13:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65111">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👍
👍
#اختصاصی #وینرو :
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدون  واریز 500,000 تومان شارژ بی قیدو شرط میده #وینرو هست
💰
👑
#معتبرترین سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65111" target="_blank">📅 13:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65110">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kw8ni44abXblgwQAjbVFIBy_RQ-GCks9OdcxG8lOwPrWAFxw6e0GzLPukuYJg8Z1oTg2Xf6Hb6LL8lJiRaUzOJ99xLukZ8sYd99osKYV2zxqClfAx_lWh2JF8zzM7gxEjn-CWyPysP_jjzPQbwCCKIEcNROcZyKNs_0EBc-XES8dit4jLVvUR5_T2a3S0TksAzx5vxrm0hUErG4dKyMBAaZlCJGKTKV5QQQf6BBGq3cO5u9qzSz5Qvo4WSXMh0Sfvosq0xOvFlDa4Yxk1RHbTZf5aj5ccM5VgtIYKLPYYOFVBoh4mN2XNyu0vdHvlH7d1ld-CHEDArbjazocZqjUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👍
#اختصاصی
#وینرو
:
✅
ثبت نام کن
🤩
🤩
🤩
هزارتومان شارژ بی قیدوشرط بگیر!
💵
💬
به مدت محدود
📣
😮
تنها سایتی که با عضویت بدو
ن
واریز
500,000 تومان شارژ
بی قیدو شرط
میده
#وینرو
هست
💰
👑
#معتبرترین
سایت ایرانی
⬇️
🌐
Winro.io
🌐
Winro.io
📱
کانال اخبار و هدایا r7
🎁
📱
@winro_io</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65110" target="_blank">📅 13:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65109">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">باراک راوید، خبرنگار آکسیوس: ایران ۴ پهپاد یک‌طرفه به یک کشتی تجاری آمریکایی شلیک کرد. ارتش آمریکا این پهپادها را سرنگون کرد و پیش از پرتاب، یک واحد پرتاب پهپاد ایرانی دیگر را در زمین هدف قرار داد.  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65109" target="_blank">📅 13:00 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65108">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس  @News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/65108" target="_blank">📅 03:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65107">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
دقایقی پیش صدای ۳ انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65107" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65106">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چرا نت من قبل از وصلی ها بهتر بود، چه وضعشششه آخه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65106" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65105">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عمو Pishgiri بهم sms زده و گفته خشخاش نکارم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/65105" target="_blank">📅 15:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65104">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/65104" target="_blank">📅 15:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65103">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اگه کانفیگ های وصل دارین‌دایرکت بدین بزارم، چون هنوز بعضیا نتونستن وصل شن یا سرعت vpn های معمولی خیلی پایینه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65103" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65102">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:  @News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/65102" target="_blank">📅 08:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65101">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsVQpwxkSeoN-mkU4jS6q2D_UIGaZyxjgFZoWbE_Y7CiVRCm0FCmf8MBic3d9CsUWtFIHSf-7XEs7lzmHn2-JPHSyvukYGgBMy5XDe4MlyXpnJqeVFfwurY07UwYEjOFrbbdlA9r1rQ6fKRwpVaOjDhfIhMJOL9ilhSwNVZLCkrXclZTEKtPYIIjALJHXfBdEn0GjYLNh41hW2_7_lt17OLaD1eDWSuyXgHiczwTpjcA9zvnmvLNT7ha-yCv2r2beSIAAsYIk3jkGJXsCgUdKxKlzYA6tPpXaybHmC9KTaHIUHIx7b0o9OtorCswAZ_aqZfET1iTLBFaAU5zGQoebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج کنسل شدن پسرا آغاز شد:
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/65101" target="_blank">📅 08:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65100">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">امروز ۶ خرداد عید قربونه
@News_Hut</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/65100" target="_blank">📅 08:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65099">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF3LqSucpx2pnQiXWpHlEOM97g4hVRT9r0rCAM-Rh_Kyx0-kSoXM2T6GSP1WpOtN082cJcVZmRl9IQTF5j-BKa5FLYiM8WtpYtaTX-VZeai1Hh8usdPuZC8HE5mrXeV_PfLNQhLTq5QpVquUtTI-2kFPB4RyRrCb_HPNt72p1Q_Z62f5xOMT0lAgIlIjU38EC3yy0zHcEU1IlsVkZ0Y5W-j32DsHAixjvdkl5fIY7ASunvEykljKpghEfrzH0Vtn602liTQUXa0GRvHMz1jUyc2nwFfzbqCOroOwzedzbVTGpzzlheBdKrkePI6zuifOXFBKIegdmQl1-THhiDFVAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها پارمیدا دیگه بعدش آنلاین نشده
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65099" target="_blank">📅 08:30 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65098">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اولین صبحِ اتصال اینترنت بخیر جوون ایرانی
🫂
#hjAly</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/65098" target="_blank">📅 08:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65097">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جالبه یه یارو مثلا نورالدین الدغیر خبرنگار الجزیره تو تهران میاد توئیت میزنه همچی تموم شده و فقط امضا بین دوطرف مونده
خبرگزاری داخلی و وابسته به حکومت همینو بعنوان خبر میزنه ینی شما بیصاب شده‌ها به منبع ندارین خودتون؟
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/65097" target="_blank">📅 03:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65096">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-3cKKYcAhAqIfBMdPYPskNI20kTp1cLuTUpSWqAooBkwNHy6MwluUFJ_C5SOxiR1daAzLXcKa7OtO-5ubYY3_G6TAF9Ko-ps2WNUbPcKhfLmBaNUWoGdALZ5gQlR1aPKvGvJH_0px2Je1OJsWsJ_oAbaPhplJOmI8BXjY7W6JMBYcK8UXVSvl6hD53ASC3XMAs5BNGqc6fFsB5vbOp1QIRaBThOyGbSrll9A-SY5EzMPyQz-SzTVFErBp8qKAIrc7rO00DMAswUngis-NAB8KMrKewuVA0Kuq_rzMAXoC2HPgoJmfy4Rnex4ZSnqeglb_K5hk2AipgAER7WoImOTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  «اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در ته دریا است، و نیروی هوایی‌اش دیگر با ما نیست، و اگر کل ارتش‌شان از تهران خارج شود، سلاح‌ها را رها کرده و دست‌ها را بالا ببرند، هر کدام فریاد بزنند «من تسلیم می‌شوم، من تسلیم می‌شوم»…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/65096" target="_blank">📅 23:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65095">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اتاق اصناف: از این به بعد فروش سیگار نخی ممنوعه
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/65095" target="_blank">📅 22:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65094">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc9optVIq0MhnLpncLdqIim6wnILdahOwpsLwDaE1xhCKIlChxJRiXgv_nealHk7N5frblQ7d9YdWX1z5tPlfd7nrb2riuIYUKCJJN8FUnzWLXgg0wjZKG7hDKoXd6_4hl02tt_fFDoMkloYZCuWUECdrgMrAXNeM41wb-9MiyAxKcup65Y6t0iFYn2adUUILYAD_SsVbTIIvx-xO8C9KqmefT_zwryRWvSD0nsBSdRsfAts-B2XZVDD7FwXNhrwD3Vm-VlGClOzQP81MAK-lsV11wmW4xSGRHzABIQ_jah67xDQVi7pYkhgZjzl_4BQbve5NvZBZsRMoBusUlBU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: همین الان معاینه 6 ماهه‌ام تموم شد، همه‌چیز کاملا عالی بود از دکترها و کادر فوق‌العاده مرکز پزشکی نظامی والتر رید تشکر می‌کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/65094" target="_blank">📅 22:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65089">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نت خونگی.npvt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/news_hut/65089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
کانفیگ‌ها و سرور هایی که بصورت منطقی براتون وصله
،
در صورت عدم اتصال می‌تونید گوشیتون رو بزارید رو حالت هواپیما و بعدا امتحان کنید
.
🌐
‌ ‌
لینک دانلود NPV با نت ملی
🛒
‌ ‌
لینک دانلود مستقیم برنامه از گوگلپلی
🛒
‌ ‌
لینک دانلود مستقیم برای آیفون - 𝐍𝐩𝐯 𝐓𝐮𝐧𝐧𝐞𝐥
🚨
🚨
🚨
تعدادی از کانفیگ های V2RAY متصل منطقه‌ای؛ یکبار کلیک کنید همه رو کپی کنید.
vless://392c0d0a-157f-4fe0-b528-11586477cbe0@185.213.165.81:38024?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
vless://6202b230-417c-4d8e-b624-0f71afa9c75d@104.16.80.73:2096?path=%2F%3FTelegram%25F0%259F%2587%25A8%25F0%259F%258%D8%B97%25B3%2540WangCai2%3D&security=tls&encryption=none&insecure=1&host=sni.jpmj.dev&type=ws&allowInsecure=1&sni=sni.jpmj.dev#%40HutNewsPlus%20VPN
vless://e0a98968-eb18-417a-87e7-c8933aac5f13@31.59.40.53:52729?security=none&encryption=none&headerType=none&type=tcp#%40HutNewsPlus%20VPN
🚨
🚨
🚨
پروکسی‌های متصل منطقه‌ای با نت مخابرات:
https://t.me/proxy?server=62.3.12.2&port=8444&secret=ee6f7a6f6e2e7275f22c5421fa893965
https://t.me/proxy?server=91.107.169.174&port=8443&secret=dd104462821249bd7ac519130220c25d09
https://t.me/proxy?server=176.65.128.238&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=195.254.165.4&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=5.75.248.201&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
https://t.me/proxy?server=87.248.129.5&port=8443&secret=EERighJJvXrFGRMCIMJdCQ==
@HutNewsPlus</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/65089" target="_blank">📅 22:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW1VRF6ggc1e_-w_usxLeeWr0-EQt8dLI2gtOHRuB5Yk5sajjsu3i7wQNFlPxGpg2RrUhAxmlhkbwi9Rr-p3TYK44s5GaJ9AmnVuPkO55ZRooyKCJybt2qUUNLUhHGHNuIqsv011UvjgFCPagWRznBCwWDiJptD0uaGEubNoXYPQ7jxOeEL_gj5yD0Sld5F_GAwLUQW9JjmROBBqVwLqqWMniTz8a0l0EXANDtEyqCbQso5NpW29SNNu9xEnCtEchPKQcA-YfE8BaymS8X-k3R2NiRkqeHziDgSp6MkocRJWj2m-SyGnHfnDk3G-4Yu3aoUkZD29SU3HJv213BlZdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد عوده، فرمانده ارشد حماس، توسط اسرائیل ترور شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65088" target="_blank">📅 22:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-text">Barko VPN_v2.0.apk</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65087" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEsteghlalPage</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Barko VPN_v2.0.apk</div>
  <div class="tg-doc-extra">61.9 MB</div>
</div>
<a href="https://t.me/news_hut/65086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
فیلترشکن :
🟣
Barko Vpn
🟣
v2.0
(20260108)
🔹
🔹
🔹
🔹
🔹
🔹
🔹
📝
مشخصات :
🟡
بدون قطعی 100% پرسرعت
🟡
برای تمامی اینترنت‌ها
🟡
مناسب شبکه‌های اجتماعی
🟡
اتصال خودکار
🔹
🔹
🔹
🔹
🔹
🔹
🔹
✅
تست شده و متصل !</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65086" target="_blank">📅 22:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نت بلاکس: دسترسی به نت تو ایران به ۸۶ درصد رسید، اینترنت همچنان فیلتره ولی امکان دور زدنش فراهم شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65085" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=HWwmUfSmbofG4LDVRz4-bCUyBBPbRBsj-cwEXzBAE_bWqXNs25RoawEafnIg1g6m6PoHgofbz2a9A0tAxqtSNKQiTjZ8Y0HjkokS4EQjoz_XKwqu4pxwKUhOpTeVBkTMEtMZKyyUTW4o0_VPA4RPLou8nqFDuDSmIt28LXjE_fHDpW8ZKXeU8XsLOxIzhdrSMdgwXJQtBeHL2jQSLR8MThusgM84_cUL1aNwBSUUwo-qGVTmPYAcsN_cQKIlhaDoma7ZG5GJnf7UubKxIS0URj5pGS5NzlY7L74WyocjENlCcsynwaYW_Nnca51ZiIf_bKz0W8PeS7flTMh3vTTT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a691fae5a5.mp4?token=HWwmUfSmbofG4LDVRz4-bCUyBBPbRBsj-cwEXzBAE_bWqXNs25RoawEafnIg1g6m6PoHgofbz2a9A0tAxqtSNKQiTjZ8Y0HjkokS4EQjoz_XKwqu4pxwKUhOpTeVBkTMEtMZKyyUTW4o0_VPA4RPLou8nqFDuDSmIt28LXjE_fHDpW8ZKXeU8XsLOxIzhdrSMdgwXJQtBeHL2jQSLR8MThusgM84_cUL1aNwBSUUwo-qGVTmPYAcsN_cQKIlhaDoma7ZG5GJnf7UubKxIS0URj5pGS5NzlY7L74WyocjENlCcsynwaYW_Nnca51ZiIf_bKz0W8PeS7flTMh3vTTT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن  @News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/65084" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFudo.</strong></div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/65083" target="_blank">📅 17:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کم‌کم تمامی vpn های رایگان دارند وصل می‌شن
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65082" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMKPX</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foVAqEPm1clCdG5j41iAktMus3jlaONZVKjIF1UOA_n9Dz6B21cTUAmgO9h6yEMnQmvxE9bbjTO-Nf00GVSskQIAnanU9jOptMiJzRUDLwCH95rWBwSihqcNBzQDk8cYACuLxgBBAzN4H-A6KPvCMX4WSkRRzeM2HBgDsI7N80uuakBmIAHdtFaBw5Fc-_FrJG-uOmc1vlKVJuswdzKSU6A0VKoDfTVH398lfiPS2NL539vDhMLpz8QhK7l8JXj4zmmItakwArwHtbkHa7Ynu1j1ZZBOj0hWrudyL7VJp2J2-HS7ZwYHTE-CrJXCCwIbl2NHiF6X_sdiSrbNAlztwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/65081" target="_blank">📅 17:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMmdi</strong></div>
<div class="tg-text">درود
کسانی که نت مودم دارن میتونن با jump jump به اینترنت وصل بشن
ما هم بعد از سه ماه قطعی به جهان برگشیتم
بر باعث و بانیش لعنت
به امید آزادی ایران جونمون
❤️</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65080" target="_blank">📅 17:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.  @News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65079" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1-JttNWArrzdlXnRcHzxyi2LU2vX7YE2NC0p1cCgGCib6qnyUuuWy-DpsSSRNen4d2HByX31ViwpEH_NAJ88crarc8GXngRmGzTKbRO0OUSJMfZlwmrAfX-ZasZUGX3Se7dUumQJ5fCtEPBx1F69HbDujlOtrFFUnjKchPTZfYBC7Clgfgyockbg0V2B6UeQlvHcbjmaGZmXdgqiNnlD585aju83NO4fCToTiTy2DkhqPXFbS6x3DzQYR0XINNbm7u6S4NgOzWxJNJ2vaS_thPLNJEVZhbUw-lRNo95fKLmPvSgi4Rk0odTK8VfV5sXhEk9XC1FV69-wxS052rVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65078" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.   این چهار حروم‌لقمه عبارتند از: رضا تقی پور، نماینده مجلس کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی رسول جلیلی،…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65077" target="_blank">📅 14:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OelG-Nw5LlClRLc44ivmB7CPR3vSAL6gFLe4OSIjE5i0aZIVDKJccDYKRgKpZjIwUyGPztMGkB7ml78AfdmA5V3aL5hDFX35pwErRDdlyO8mOfPRk_sQvtGYeQdAvKmwy-PAc963zKKq3G5_x0w82N9Jz3UqX29LhjJUvkBBLSwcJy4sVkh2aUhJnN9n4CWEePIR7OxjvasYCPUqfbvLgLYKTLQmXMz5C9iUT0fNkdkt-Zub1XXK7YGKR8HyTCnf-eU3MLu5aP_71TAHMTQUlhl9Jzuu-TkHwBN9V-ItEXenwC-EhIbwb0604zYtd5wMGv3is1gnJHH-2FWBklbQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری انتخاب: ۴ شاکی حقیقی رفتن شکایت کردن و با دستور لغو مصوبه بازگشایی نت باعث توقف اتصال مردم به اینترنت بین‌الملل شدن.
این چهار حروم‌لقمه عبارتند از:
رضا تقی پور، نماینده مجلس
کامیار ثقفی، هیات علمی دانشگاه شهد و عضو شورای عالی فضای مجازی
رسول جلیلی، برادر سعید جلیلی و عضو شورای عالی فضای مجازی
محمد حسن انتظاری، عضو شورای عالی فضای مجازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/65076" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه  @News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65075" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/65074" target="_blank">📅 12:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=vSWLmWsKjebQm2BkO-lfBhJUFZWRIGiJpOUe-jXphrkH237cuFgQw-J4qtZqig3gX9DD-8kUtRPEDgyEs9Wz-ESXmBewEKiKmTjNc7zAXt_gVUqE3134nFOpGoECV0-8cJxAE61jH70wWaPim5UxRo0VZv2H10SsSkRr2KILxxKtEODBdJgwSil1ZoFFEk2FEb76YIgEf4AjlDSnnE1Y8lGeFKQtO05SOvZZIEqR6jMMQz_12_qQ0UugbH6yBxdxct9XBzIlKV3YwP6yhx98TTnPQUcFvJaFc9oOzUarj5ahC503bYtpfLwgsIAuKHWlR0XujXUGVM21vCUE7oKUxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ee692e46c.mp4?token=vSWLmWsKjebQm2BkO-lfBhJUFZWRIGiJpOUe-jXphrkH237cuFgQw-J4qtZqig3gX9DD-8kUtRPEDgyEs9Wz-ESXmBewEKiKmTjNc7zAXt_gVUqE3134nFOpGoECV0-8cJxAE61jH70wWaPim5UxRo0VZv2H10SsSkRr2KILxxKtEODBdJgwSil1ZoFFEk2FEb76YIgEf4AjlDSnnE1Y8lGeFKQtO05SOvZZIEqR6jMMQz_12_qQ0UugbH6yBxdxct9XBzIlKV3YwP6yhx98TTnPQUcFvJaFc9oOzUarj5ahC503bYtpfLwgsIAuKHWlR0XujXUGVM21vCUE7oKUxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگو دولت: بازگشایی اینترنت توسط پزشکیان به وزارت ارتباطات ابلاغ شد و امیدواریم تو روزهای آینده باز بشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65073" target="_blank">📅 11:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رهبر سوم جمهوری اسلامی: سه چارتا جنگ کردیم همه دشمنان‌مون رو تا ناموس شکست دادیم جوری که ویران و حیران شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65072" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
رهبر سوم جمهوری اسلامی: پدرم، علی خامنه‌ای خلف پیامبر بود و بعثت الهی یافته بود(از طرف خدا مبعوث شده)  @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65071" target="_blank">📅 11:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد  @News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/65070" target="_blank">📅 11:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PGXvY8fOyX8EkiabyEDAdLGJ3lfsEjzvgvqiFa8KtsewoGTt1q9T7t9pZxhYRZPD_GC36SyCt0dgFXYml9jMCAdTBRAcPU-jh5ds6Aw3P2CLwOzxK0pa8HD5ybMlMOZYsONzeOxQ9rKs0jq22kWQiOjzImX7pnh80FcAmzTkAHmymNZJIGL4tkTAohQfzW5fqTMAO8v3A_XCwn_OU9nrQWuUOoUjXPce_xz_6MUZL1dNFdBvszlhlUGSZfmIgwSxE3XtAnYfnKWyN-mTLl_unbTMLkBvuOtHpyGhnUbYfR_iwppTE1t6PYL2Qg8aRr0BU6O380cRf_4HF72HdzQCHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووری برای اولین بار رهبر معظم جمهوری اسلامی با سوییچ از فونت لوتوس۱۲ به فونت تیتر ۱۸ در جمع حامیان‌ خودش حضور پیدا کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65069" target="_blank">📅 10:57 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65068">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/icHHTpnOUtYBoyB35m1-fn_flSEJtvYV26N0yeciG5HQonl8A6UvKRyKzY4fLzOBl3I0WMV4R6xBMtYxKP9XV7b9muXCncECVa2kmpe9SWhUOAa_zz-BN1_DUEi3J9S0rp3jDquW62S3-ptKWZRhG8BlNqaZuZyDgez5zIAxIkqmtmbSr0K58zMvdOJ2fUCe65c4FCwPiOPPLRRccSRsu9zyzhiTSK2tO7A7BKTlu2gv_BG7e_fuaAuy7wRUQAnVnE4ebXTIlSdetBBBZf_FYXRd0ehm1ka_Ol9dSKASiGn3xmfrL8Mi5ngE8QhHLHSjlZWd6xbHbkxpnJGHbR1JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:  اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود. یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/65068" target="_blank">📅 08:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CDV59xEwBSgJcDo6p7UlRAkmU3dNI9zyMZFRSbqlNp06z36wZ2lnnOK5n_Ejydlxl-lAGxJ9vxDWlBZiUdQFYiJN0ZVVn7VKeXmV0omDpC-rRoRNvhHXHnPfcvOpW75HqIr73blVREySHZSgCcAaTIbctIeT9EJNPZw1lsHdyXnFVKI-_hxK65VJqCghd8zRDEcTMQ3l4SOFO4LbpdBTLhdtuFramH7Y7VFQWQ6leUQ4b-2pksh3R3jKJsg8BdQkXKSa_MtAj8ZnDiQwifCiGpV91ejDtCNoobGNzXZfu47pgk3ux4jZ6X7ysuSaS7kNm_4fOWAZnU_92watp4jbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/65067" target="_blank">📅 01:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صابرین‌نیوز: امریکا دو قایق تندرو سپاه رو با جنگنده زده و ۴ نفر هم کشته شدن</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/65066" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65065">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXFXrB7whIv1fUus_o_fmAXboBzs9YYB1tyaK4SWL4wpJYdmBh5sZ_17QoQ-Vd7sK6XdPVM7tYfqkL3M23dDHL90Oc1NKEa75nZwM_xZSWcBOgIjYujekjR3twxc3ynzHgfJFIlcuBOmhjgRVLklKyPmkB_FihIWor4buyRW11KbBw3G6OoMTLBz_xHSsH1rLyLV34W6Wz-V1AZ6fLDfEGmW5voe1GvedwXy447sTik5msWML-WuNpF9bcheCjKOUaZAcy-LWZmfxDa3GTxQOKfxWS5ikoNuCS1I652AUbX0c7eiIsuS1OwoVL_t9c70b5KfrF9wkKt3C0OFQhXxtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده می‌شود تا به کشور بازگردانده شده و نابود شود.
یا ترجیحا، با همکاری و هماهنگی با جمهوری اسلامی ایران، در همان مکان یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/65065" target="_blank">📅 01:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65064">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65064" target="_blank">📅 01:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65063">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzrmjHmENIz7iWzdW1c8HE1ASnHSTKJ2VPb3yOo-0YeiIoI4h8LiNvs52wOq9RcS-pmmwgrXS4LDRiBYA1sQL0m-wmnexuWpoP_cW38ZBdLIvAmbhVZoqWElPHL_gPXyX1IVgq7kNpojF90fZyKPa4XXIr3F3koWswUo_ICp0vArkexyQUlf4s-B5iqaFky5v3Ixu-9TGa6ncTZm2LaRWuaTZbe2c6qwN3tjzPdkCKzz9C4ljFXk7V_dBDz5j4suyAyJs1zhOw-Zhq6mMB1di8jOvTewlEwRkbIqMLmLS9Yw7z1r6ysUBSwbqXf_Jte17mEi5AYDNxaW4Tc1FY96Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری تایید نشده مربوط به انفجار لحظاتی پیش در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65063" target="_blank">📅 00:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65062">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
شنیده شدن ۴ انفجار در بندرعباس و شهرهای جنوبی سیریک و جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/65062" target="_blank">📅 00:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65061">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
📰
آمیت سگال، خبرنگار شبکه 12 اسرائیل:  ایران در حال حاضر فقط حاضر شده به توسعه سلاح‌های هسته‌ای رو متوقف کنه، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65061" target="_blank">📅 21:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65060">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">به صورت قانونی، ما یه "شورای عالی امنیت ملی" داریم که به "شورای عالی فضای مجازی" دستور میده که به بقیه اپراتورها بگه که اینترنت رو ببندن. به صورت غیرقانونی هم سپاه رو داریم که زنگ میزنه میگه اینترنت رو ببندن. زورش میرسه، میکنه! حالا دولت رفته یه "ستاد راهبری…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/65060" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65059">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ: من به صورت الزامی از کشورهای خاورمیانه درخواست کردم که پیمان ابراهیم را سریعا اما کنند تا «جمهوری اسلامی ایران» را در ازای بخشی از توافق پیمان ابراهیم داشته باشند  @News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65059" target="_blank">📅 19:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65058">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
ترامپ: توافق با جمهوری اسلامی ایران!! به خوبی درحال پیشرفته این یا توافقی بزرگ برای همه هست یا بازگشت به جنگ بسیار بزرگتر.  @News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65058" target="_blank">📅 19:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65057">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇺🇸
تروث طولانی و مفصل ترامپ درباره توافق با ج‌ا و پیمان ابراهیم:  مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است! این موضوع تنها یک توافق بزرگ برای همه خواهد بود یا اصلا توافقی صورت نخواهد گرفت؛ بازگشت به میدان نبرد و شلیک، اما بزرگتر از قبل و هیچکس…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65057" target="_blank">📅 19:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65056">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد @News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/65056" target="_blank">📅 19:02 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65055">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh5_Kuy61H6S0flvD0yquHG8nHV4qczi-g7k65NsqgraWeqOZfjSpSDMJWyPFsT-a-zw8g6EH9cyjxJkJo6r_p_9cpjh-VoSS-C7zkAkw0mKs3AOV1KyDsBfspk-PKCXeG0qwp3xtjqvUf4GkvH_QABUMiZVESrzscbc38sg2GxcbmoaTlR_rycZdNFO_ua67W_lgloEOFpbRJjvPJuH5o97scKdd-YMsML62wQFyZP-BXmPwOX0P8yYH3U81L_fwh4cbgzjGSQskUzeNcK6qsPc_47U08p1-PyfJJBdEKxVSWVe-Ztno_ChJ3ArSImkydNb16m44XSVKxvyquz0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم  در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟! #hjAly  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/65055" target="_blank">📅 18:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65054">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جمهوری اسلامی گفته یا اموال بلوکه شده تو قطر رو آزاد کنید یا حتی یک گام هم در راستای توافق بر نمی‌داریم
در واقع الان دست بالا با جمهوری اسلامیه نه ترامپ! اینطوریه که می‌گن می‌خوای حمله کنی؟ خب حمله کن ۴۰ روز کردی مگه ما چیزیمون شد؟!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65054" target="_blank">📅 17:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65053">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چه افتخاری هم می‌کنند حیوون های حرومزاده...  سه ماهه حق طبیعی مردم رو ازشون گرفتین و الان از بازگردوندش، دستاور می‌سازین؟ باید رید به سر تا پای دولت حقیر پزشکیان و امثالهم #hjAly</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65053" target="_blank">📅 17:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65052">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
فارس: همتی، رئیس بانک مرکزی برای بررسی و گفت‌وگو در مورد آزادسازی ۱۲ میلیارد دلار پول بلوکه شده تو قطر به دوحه سفر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/65052" target="_blank">📅 15:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65051">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65051" target="_blank">📅 14:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65050">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnM-KNl3CBECCPVrVorXtq9lglRijjovwH26_OuKnb76auI_ecFDWPW3Lp-FjeL5na_uLeY37uAyd4YyhRjpuHCyV6RDyu0ZJqPYKqaG5M8K6p8NxLjhkdNKOnWWSWoLPs-82YxRVoUG3xt38QHK1Eh7t2YhJp5U-SqwcVqeN5HtzFqpUaxDvY1zksub8k3cNWbT_vKWucHc4gwBEvzST9OWwdnyQcnRTblm9zshkP-B4ehwL19I8xDDOrVBEje_JEq_LH6sZFwoTBPwn2O4Wjuvr9ER8E9BYWfw7um8Ev-CMS45SsT53kT_Icn6R2OBlo5KbXZZ1L-3WVJugD3DWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: در جلسه ستاد ویژه ساماندهی فضای مجازی که با ریاست عارف برگزار شد بازگشایی اینترنت بین‌الملل با ۹ رای موافق و ۳ رای مخالف مصوب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/65050" target="_blank">📅 14:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65049">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=DHyGxeNDktjoflRj-q5u81PF0-lBPv3bigFQtAGmfHIMjcLYXpY2ge7t70u-xq_YglsVZrepRhqEKPFaAQwVRcke4L8cOCstX45K7AG72KBr5XYWIWDJTu-C4zirf7RtxMjmKqwOG1GzPjjzRbcYeunvqRP6ZTd658NbjAM7Qfaup0WCt4xeBaDzMbKdp1f2WsRmxCxTeFDeJG6cSfAjMlx2lxvWrmhZUB_OYSn3qeMiGtP8G3J1_wDkEibW-Ui8kVE-6A6WfkBrq51Dzycj9z1PKVrRc3ObuK8Sp93spa7I5phB1pH7C49Cr5_209p5hzqLkpv_LUfiIWHhyJBsjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df45acb25e.mp4?token=DHyGxeNDktjoflRj-q5u81PF0-lBPv3bigFQtAGmfHIMjcLYXpY2ge7t70u-xq_YglsVZrepRhqEKPFaAQwVRcke4L8cOCstX45K7AG72KBr5XYWIWDJTu-C4zirf7RtxMjmKqwOG1GzPjjzRbcYeunvqRP6ZTd658NbjAM7Qfaup0WCt4xeBaDzMbKdp1f2WsRmxCxTeFDeJG6cSfAjMlx2lxvWrmhZUB_OYSn3qeMiGtP8G3J1_wDkEibW-Ui8kVE-6A6WfkBrq51Dzycj9z1PKVrRc3ObuK8Sp93spa7I5phB1pH7C49Cr5_209p5hzqLkpv_LUfiIWHhyJBsjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
محمد نگینی‌پور، مستندساز حکومتی مستندی ۴ دقیقه‌ای از حضورش تو پزشکی قانونی کهریزک منتشر کرده از اعتراضات ۱۸ و ۱۹ دیماه‌،
تو خود مستند حکومتی که منتشر شده تعداد بالای کشته‌شده‌ها و کانتینتر های حمل جسد دیده میشه که جنایت خودشون رو به کار دشمن ربط میدن و ابعاد بزرگ این جنایت مشخصه!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/65049" target="_blank">📅 13:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65048">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/65048" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65047">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=uiWVAj_PrxsESNUrNASxMt45oV_1c5HgUlBB8stvBCeBj1OEf1gSV_kyjgEoE2LOk2tBoxtinsLaz11yyDVHtejR11kmbbw78VJaDhnz0G4iAXC7kteB3OT7O3N95jGurio0MVO-0ds5JI4OG8Yiyv3kEfHPlx6kOPOg7nllobsVax2VTdEZzdzHV_JtWykfow4qG2QErl3GhZUdlVTpcrXH0KAmvkG8kG6iyNAB1nYD_iWP_yfOaUZQiQMs6f6Es9w_A-OmpDmVuBQT6zIlkbLk7L2pQvVzSoEsS5l39kVzpeq-gjR-DsdHg5LTFxiZlMDq6DY--VF4Glowcfngng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d1b11fd8.mp4?token=uiWVAj_PrxsESNUrNASxMt45oV_1c5HgUlBB8stvBCeBj1OEf1gSV_kyjgEoE2LOk2tBoxtinsLaz11yyDVHtejR11kmbbw78VJaDhnz0G4iAXC7kteB3OT7O3N95jGurio0MVO-0ds5JI4OG8Yiyv3kEfHPlx6kOPOg7nllobsVax2VTdEZzdzHV_JtWykfow4qG2QErl3GhZUdlVTpcrXH0KAmvkG8kG6iyNAB1nYD_iWP_yfOaUZQiQMs6f6Es9w_A-OmpDmVuBQT6zIlkbLk7L2pQvVzSoEsS5l39kVzpeq-gjR-DsdHg5LTFxiZlMDq6DY--VF4Glowcfngng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو:
ترامپ قرار نیست توافق بدی امضا کنه. هیچ‌کس به اندازه ترامپ تهدیدِ هسته‌ای شدن ایران رو جدی نگرفته
خیلی مطمئنم که یا به یه توافق خوب می‌رسیم یا مجبور می‌شیم یه جور دیگه باهاش برخورد کنیم.
ولی ترجیح ما توافق خوبه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/65047" target="_blank">📅 13:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65046">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">قالیباف دوباره به عنوان رئیس مجلس انتخاب شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/65046" target="_blank">📅 11:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65045">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Fcq9pN2iQyktIGKNbcfcx-nSuaTk-mRZAiql2tSEXfZUjFscO1HaDHGZkt3x2sT6o7zfT0R_RUEggx0CJQwA9EoB78ZVfrw5u8UqyiU1-NCmFzBCIxNXvgF3UHH-uKV_0evYg23NN_Zf13dlgey9zkFleF0Cfga9zpA7uGrsAh0L0eH3i4es0yfUvsJpIkTpP6CFegioF0lmTtsPbnsFki2gCmdE7K8bmu2viJBZ32lzLxLJtyZj6Hx29Sp78vMCKQK9NR7NIIJokGZTUCF15IHiVvQkRu8tBAzrECo4j0ypiWvLoT6C2xQPnJOdByGv0qweLG-gMuvtm-GPnDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوج حقارت ارتش
ایران
به روایت تصویر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/65045" target="_blank">📅 10:19 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65044">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: توافقی برای پایان دادن به جنگ علیه جمهوری اسلامی ممکن است «امروز» حاصل شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65044" target="_blank">📅 10:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65043">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام: اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.  پیوستن…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65043" target="_blank">📅 00:42 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65042">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH2hABauxRhc7z6RRowJdMdpOILHdTj9kP4WHNyDuTTfAoug-UR2kv06YyXTuveShqswawFUslhE0lcHZ8sbg11J88i79VAzaDfBlrT13scv0n6CsH_7xp1VxSe_ICJqd7qf-_L1teClzAcXxbDIJ2Vry-33Lrj06BuaV8mASx2ke9WAg5yFm4vAVjIE1MisKFKLWWUQ5mC2mIAY5qO8HNdV6MW25iFeFS2qoFUqiB6e9iRbdGC2UkeGrxDSxlgevGPtJvta09Z81tTcEQ_MCwmd0z59o_JeR1OVsNorxXRtoe6VYEPoa6JGi_33kpw_NPGjTNchhouJzCQDLgwMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سناتور لیندسی گراهام:
اگر در واقع به نتیجه این مذاکرات برای پایان دادن به درگیری ایرانی، متحدان عرب و مسلمان ما در منطقه توافق کنند که به توافق‌نامه‌های ابراهیم بپیوندند، این توافق را به یکی از مهم‌ترین توافق‌نامه‌ها در تاریخ خاورمیانه تبدیل می‌کند.
پیوستن عربستان سعودی، قطر و پاکستان به توافق‌نامه‌های ابراهیم فراتر از تحول‌آفرین برای منطقه و جهان خواهد بود. این یک حرکت درخشان از سوی رئیس‌جمهور ترامپ است.
به عربستان سعودی و دیگران: اکنون زمان جسارت برای آینده‌ای جدید در خاورمیانه است. من انتظار دارم، همان‌طور که رئیس‌جمهور ترامپ پیشنهاد کرده است، شما در واقع به توافق‌نامه‌های ابراهیم بپیوندید و به طور موثر درگیری عرب-اسرائیلی را پایان دهید. اگر از رفتن به این مسیر که توسط رئیس‌جمهور ترامپ پیشنهاد شده است خودداری کنید، این موضوع عواقب شدیدی برای روابط آینده ما خواهد داشت و این پیشنهاد صلح را غیرقابل قبول می‌کند. علاوه بر این، این موضوع توسط تاریخ به عنوان یک محاسبه‌گری بزرگ دیده خواهد شد.
رئیس‌جمهور ترامپ: در گرفتن یک معامله خوب با ایران بر موضع خود بایستید. به همان اندازه مهم است که بر موضع خود در اصرار بر پیوستن عربستان سعودی و دیگران به توافق‌نامه‌های ابراهیم به عنوان بخشی از این مذاکرات بایستید.
دوباره، این یک پیشنهاد درخشان از سوی رئیس‌جمهور ترامپ است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65042" target="_blank">📅 00:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65041">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آیا دونالد ترامپ، باراک حسین اوبامای دوم خواهد شد و دستور آزادسازی ۲۵میلیارد دلارِ جمهوری اسلامی را می‌دهد یا خیر؟!  بزودی خواهیم دید! @News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/65041" target="_blank">📅 22:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65040">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNj1EdP9HlSylSqrigzjzK6POAUtZzjyNF3nmpIhCjysU88vVstljHZ1AHUsN8wWY-CdPnHj9tObM9Tz-KbN0lEfH5pEnOcL6ufx3Cjk149O_0rpc1EE64lXD5iDpIOrHRy3IobEHqRvEUvhZpNN68xWwEyU6fNbB_hC0s4kS6cqBJrFxeXocMF_wjip8eLWO3T_SrAjwydbVw265uoipCITEt4YGfSKYng2uniSI7W1HML1a6moPD85y8E30bSJIoKzIPSib9SGq_72eGi1lyzT90vrlDtl3f3WgwJpnbakElvtg4FffpuF2aiR4DrrMUEZHPWrA-6PRcssxOnTCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65040" target="_blank">📅 22:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65039">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktJSEz4wm3UkyKy4i4X-sXeHfQGzwIs39myFgUi8qC6ZRc87xVpdu8CFFoc-sDIRD8sRre3nXvy2wSYaMHxGH4LvHUdkFlQzxVJ33k1rFp6QMA4nowSuIG6C5shxqD0_Roa9aSf9-k0ImxwUGoGjtTQfU2mcA6lDOHHuylNf4wrggdxps1scnY44mlYegq3AspSAyVbZOTvWKMLI54IBdJvaKnoPAJ4CHJ871-qd6nnhf90PoUjS4u65PLDDyb4NwmvrfWVMgC0VMW1sD_c-wU5fXZwnqveUf47tHipg6trcSac5WwjtltlYZweoaswo9cmer46XQGAtDjfO38ltbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
اگر من با ایران توافقی انجام دهم، توافقی خوب و مناسب خواهد بود، نه مانند توافقی که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و مسیری روشن و باز به سوی سلاح هسته‌ای داد. توافق ما دقیقاً برعکس است، اما هیچ کس آن را ندیده یا نمی‌داند چیست. هنوز حتی به طور کامل مذاکره نشده است.
بنابراین به بازندگان گوش ندهید که از چیزی که هیچ چیز در مورد آن نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من بودند و باید سال‌ها پیش این مشکل را حل می‌کردند، من توافق‌های بدی انجام نمی‌دهم
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65039" target="_blank">📅 22:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65038">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو: توافق نهایی با ایران به معنای برچیدن تأسیسات غنی‌سازی هسته‌ای و حذف مواد هسته‌ای غنی‌شده است. من و رئیس جمهور ترامپ توافق کردیم که هرگونه توافق نهایی با ایران باید خطر هسته‌ای را از بین ببرد. این به معنای برچیدن سایت‌های غنی‌سازی هسته‌ای ایران…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/65038" target="_blank">📅 20:40 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65037">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: من معامله بد انجام نمی‌دهم؛ در مورد جزئیات توافق فعلا حرف نمی‌زنم، صحبت های خوبی در راه است
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/65037" target="_blank">📅 17:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65036">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تنها چیزی که ترامپ تغییر داد رژیم غذایی مردم ایران بود
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65036" target="_blank">📅 15:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65035">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=Jf32RiHXnxIal4RiMSkiCevPXMoBG1TEJG8QT8V-7L99BuvhJ07ObOCegIxLsrU6GccOmKjnSOUp1jK-ZNVlVycWy2vyg_MssYTKXB6yK9UQKZ6g2It8ZrouXn2sK2s5CmtadbS_iRpAHSG1JbMZ00slNF7Gu8iSpd8JGk-dRhiZ5bNEauIFZ0XzxPZG6YpM1-3Wqc5BycN8bIW2T6zw7nfQoefTsKeFq_P3PfnrTfXVacORWjpnFn-AI69dIgB-Lypjm7AucSHhlo81gVtjk5sgbNxmERaflLyNA5Z1FOSfM6MV01Vyf6wNRwb8idK9_t7vZPMU-5yFDls1pSKl6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79f15b4f.mp4?token=Jf32RiHXnxIal4RiMSkiCevPXMoBG1TEJG8QT8V-7L99BuvhJ07ObOCegIxLsrU6GccOmKjnSOUp1jK-ZNVlVycWy2vyg_MssYTKXB6yK9UQKZ6g2It8ZrouXn2sK2s5CmtadbS_iRpAHSG1JbMZ00slNF7Gu8iSpd8JGk-dRhiZ5bNEauIFZ0XzxPZG6YpM1-3Wqc5BycN8bIW2T6zw7nfQoefTsKeFq_P3PfnrTfXVacORWjpnFn-AI69dIgB-Lypjm7AucSHhlo81gVtjk5sgbNxmERaflLyNA5Z1FOSfM6MV01Vyf6wNRwb8idK9_t7vZPMU-5yFDls1pSKl6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مارکو روبیو: امروز اخبار بیشتری از توافق با ایران منتشر می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/65035" target="_blank">📅 14:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65034">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mz6Hc0N2BOtcu20DnuGstF1oxZ4krKUILovmCRVbbHY8xxo0CmXWpt9SPfecAiB8c-Du8u2cq5jgxj0jEbPTLVj7ArugnaTXTFnq-W1lBlvEU770vrI5xrjiS77scCl6sMr6zKfhTUJfjUz6pb61RX61Bv48f9pxhnxQjDE65sN5xqRaJuWQ5Z_FJH0H_HhZo1yaUFwJX2gpFIVJrWireMwWEHCSJE0o5E2K-3-rSGTsJRRxfyar2eOZyPoFXgFPThBjO_Tct-ZFAggdDTLLpQ69wcr9_2ZlbAcowLx-y1Oyk697CypzE7stOLTBAlgGh2xz8Jg13wqPGf1PEhDljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کجایند مردان بی‌ادعا؟
🗿
#Fun
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/65034" target="_blank">📅 14:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مراد ویسی: سپاه می‌خواد روحانی، احمدی‌نژاد و پزشکیان رو ترور کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/65033" target="_blank">📅 10:31 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65032">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aB2DzY7exYpEUA9jgHSp4RfXmqYG95br8_6MysFknZCBqn_hqB5duo1vZ0yfF9Ibf__MaXyPnlOo9Lolu7082Ud0DjB5n-4M69ur4JbKyCeQ-XiHNHhHqznGqgExddC-5ZyY42rhyyaTvJmZ-yC1UO5-TiVg1J179NOqEu8fsFLW-iHiZ7OcWRKJnP2PKwpaXSDTlbyMkjm-kG87Mh4XfKhryIiEvn-RqLanlXmJSGDuD0ply8cdlTk3VeYsGJ4xIOz46HTKbWPjLMJWFrneY5BMViXUTIPMYwjagoBLFwMhqkg-NEA61PUfjcOaEdohiA8VtVHCPcQ_IrY2vXnV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار تتر بعد از اخبار دیشب درمورد توافق تا زیر 170 هزارتومان ریخت
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65032" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65031">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
آکسیوس: توافق بین دو طرف امضا شد.
👎
این خبر فیکه و آکسیوس و خبرنگاراش همچین خبری نزدن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65031" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65030">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=Qw6-4oaWFxdTtXnpoFM8xmbbYWtCmtzn-UOnNNDUO3edNqAmeYfOPr7g1erCGEJe7NZcoGEnTsnm4GWQQ01cHA4P4oUIILcfLYxQcIVTVfz-K11GDpSYrQSmdVojMF6LOOhYeQfLkyP4rpSqfGXx3kjYOqY7SPimK02Oj8bmTvUYTZ_DwKO3VGBTNSgTFz0LH-Fg47oafUtWlSjMJOVd9BYz176xdFyEZIWy5c1LZD_StJBy6y6KeHnKWEYVO1cJBbO9_JS5NPquUoquMhTRvdFjSlVZXQrUhxkQdsQPkP45CNBYcAZxqINzTeWjcykhgoyQvx-UfMbjea37NQEixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43de325c3.mp4?token=Qw6-4oaWFxdTtXnpoFM8xmbbYWtCmtzn-UOnNNDUO3edNqAmeYfOPr7g1erCGEJe7NZcoGEnTsnm4GWQQ01cHA4P4oUIILcfLYxQcIVTVfz-K11GDpSYrQSmdVojMF6LOOhYeQfLkyP4rpSqfGXx3kjYOqY7SPimK02Oj8bmTvUYTZ_DwKO3VGBTNSgTFz0LH-Fg47oafUtWlSjMJOVd9BYz176xdFyEZIWy5c1LZD_StJBy6y6KeHnKWEYVO1cJBbO9_JS5NPquUoquMhTRvdFjSlVZXQrUhxkQdsQPkP45CNBYcAZxqINzTeWjcykhgoyQvx-UfMbjea37NQEixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/65030" target="_blank">📅 00:46 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65029">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=kVbTDFx3BI0pGb2_k0KMICV_cCK7pBOAqw0oH8C1FZgjyhNt_xEZOyWfTpfValeshWDKVYqKD6sRbGpEGXeiB5bQTi-6E46C6a4Y2uE9dwu5t29jrnGx0VmWQW44FobcVQa4g9YzVk2nyYanfGN76eYHkcAj-6Sn0T0bSUlBgUfe1cPXP1yir-lHQ6hkkCTvEKfCSA3ATt05o5DDZoFYLUlCjC6W15Qfr-zk0X4L4D8p5BkaLM3gm3GqY-RFvFxj7fWL4SGGXlgYfGDLcY2vyuzny4-MvsdpHgyD3m_-bOZ3A92yYoU4aIK_Tfc3u9npoXI7WXq0iPF6nCI2ri_5oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fad8544d2.mp4?token=kVbTDFx3BI0pGb2_k0KMICV_cCK7pBOAqw0oH8C1FZgjyhNt_xEZOyWfTpfValeshWDKVYqKD6sRbGpEGXeiB5bQTi-6E46C6a4Y2uE9dwu5t29jrnGx0VmWQW44FobcVQa4g9YzVk2nyYanfGN76eYHkcAj-6Sn0T0bSUlBgUfe1cPXP1yir-lHQ6hkkCTvEKfCSA3ATt05o5DDZoFYLUlCjC6W15Qfr-zk0X4L4D8p5BkaLM3gm3GqY-RFvFxj7fWL4SGGXlgYfGDLcY2vyuzny4-MvsdpHgyD3m_-bOZ3A92yYoU4aIK_Tfc3u9npoXI7WXq0iPF6nCI2ri_5oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همونطور که اکثریت رسانه‌ها گفته بودند، احتمالاً یک راستی آزمایی ۳۰ روزه در قالب توافق موقت، برای پایان رسمی جنگ و بازگشایی تنگه هرمز شکل خواهد گرفت، و بعد از این توافق طرفین به سراغ مسئله‌ی اصلی یعنی هسته‌ای و تحویل اورانیوم ها خواهند رفت  شما اینطور بخوانید…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/65029" target="_blank">📅 00:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/65028" target="_blank">📅 00:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65027">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fgg_VEVmZ5t0fheZk7fmWx_6oJZaS6FKrQmZ2UamibXufeuJZi2FzHmu2mCUoPmW4HC-OJ01CnVJ1ynznL7nEbgCqTSuCtTsrkNBrRMabCIoWsAKDxyk1m9-t3aiNB-p_UAhOCfFL48szZj_MJ3lvy1effb33hHVC5V5rna2KsIUSEyQlxFhgxgUI1JRau3oiLXpAmoSWT6hVHnZXjbMg0Rg9K6CRdh-ETBWMeq3PMrJRoRhg1VQUqj4OMJlDDnHUGOKAmRFmx5q8kRa3jLUO9Ls60qFF7iWC-CLbh2z-TJJcwRRm2G28qe4XW_uWO_U6JF2UrZGnU3hbNhGNE5qWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ:
من در اتاق بیضی کاخ سفید هستم، جایی که همین حالا تماس بسیار خوبی با پادشاه محمد بن سلمان آل سعود، عربستان سعودی، محمد بن زاید آل نهیان، امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی، و وزیر علی الثعادی، قطر، مارشال فیلد سید عاصم منیر احمد شاه، پاکستان، رئیس‌جمهور رجب طیب اردوغان، ترکیه، رئیس‌جمهور عبدالفتاح السیسی، مصر، پادشاه عبدالله دوم، اردن، و پادشاه حمد بن عیسی آل خلیفه، بحرین، در مورد جمهوری اسلامی ایران و تمام موارد مرتبط با یک تفاهم‌نامه مربوط به صلح، برقرار شد. توافق‌نامه‌ای به طور کلی مذاکره شده است، مشروط به نهایی‌سازی بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر، همان‌طور که در بالا ذکر شد. جداگانه، من با نخست‌وزیر بیبنتانی، اسرائیل، تماسی داشتم که به همان ترتیب بسیار خوب پیش رفت. جنبه‌های نهایی و جزئیات توافق‌نامه در حال حاضر در حال بحث هستند و به زودی اعلام خواهند شد. علاوه بر بسیاری از عناصر دیگر توافق‌نامه، تنگه هرمز باز خواهد شد. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/65027" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65026">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">بله  مگه چیه ما با ۹۰ هزار ... گواهینامه مون گرفتیم</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65026" target="_blank">📅 23:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65025">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گواهینامه شده ۱۵ میلیون تومن!!!!
الان یکی میاد می‌گه حاجی ما با ۵۰ تومن گواهینامه گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/65025" target="_blank">📅 23:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65024">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بستن تنگه‌ی هرمز در جنگی که ۹ اسفند آغاز شد، تمامِ معادلات آمریکایی هارو بهم ریخت، اون‌ها حتی چند روز قبل مین‌روب های خودشون رو هم از منطقه خارج کرده بودند! دومین مسئله‌ی شوکه کننده برای اون‌ها حملات وحشیانه به کشور های عربی بود  هر زمان آمریکا_اسرائیل به…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/65024" target="_blank">📅 22:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65023">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/65023" target="_blank">📅 22:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65022">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باز تو این دقایق فیک‌نیوز و نویز‌ها بشدت افزایش پیدا کردن، اخبار ضد و نقیض زیادی به گوش می‌رسه، اما کلیت ماجرا اینه که تهران آخرین پیام خودش رو به عاصم‌مونیر داده تا به آمریکایی ها برسونه، ترامپ نهایتا تا دو روز دیگه بعد از دیدارش با ویتکاف و کوشنر، تصمیم می‌گیره، یا از خواسته هاش عقب نشینی می‌کنه و یا اینکه دوباره جنگی برای اعلام پیروزی شکل می‌گیره، تا این لحظه طبق اخبار، الحدث، آکسیوس، نیویورک‌تایمز، سی‌ان‌ان، آسوشیتدپرس و... احتمال توافقِ موقت بسیار بالاست، یعنی توافقی که در اون توافق کنند برای به ثمر رسیدن توافق هسته‌ای!!!!
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/65022" target="_blank">📅 22:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65021">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/65021" target="_blank">📅 19:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65020">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ شنبه با ویتکاف و کوشنر دیدار می‌کند و یکشنبه تصمیم نهایی برای توافق یا جنگ دوباره گرفته می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/65020" target="_blank">📅 19:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65019">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
📰
ترامپ در گفت‌وگو با آکسیوس:  در حال حاضر احتمال کاملا 50 / 50 است که یا با ایران به توافق برسیم یا دوباره جنگ از سر گرفته شود. یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم + ترامپ شنبه با…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/65019" target="_blank">📅 19:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65018">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
فایننشال تایمز: ایران و امریکا به یک توافق آتش‌بس ۶۰ روزه نزدیک شدند!!  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/65018" target="_blank">📅 19:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-65017">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
📰
#مهم؛ فایننشال تایمز: میانجی‌ها معتقدند که به توافقی برای تمدید آتش‌بس به مدت ۶۰ روز نزدیک شده‌اند.  این پیشنهاد شامل: بازگشایی تدریجی تنگه هرمز گفتگو درباره رقیق‌سازی یا انتقال ذخایر اورانیوم غنی‌شده بسیار ایران کاهش محاصره آمریکا بر بنادر ایران رفع تحریم‌ها…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/65017" target="_blank">📅 19:08 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
