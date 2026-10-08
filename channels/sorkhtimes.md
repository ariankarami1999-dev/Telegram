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
<img src="https://cdn4.telesco.pe/file/gnaEFnK0wFd5Ae4KqCDoK9C0F9i8yJ5SocR_0uYgaalj5NrebynFDXPDNQzQFfaKooXA9mtbFGNpteuLUPusz582HWi0Zjt_jg-KzD7IjkyXu3PmdIJEpaVlKu0p-dwxOz5FGaFIhzLkmmK4R2N1RmzCdGqv2nCzBeidZ-SN6p3Qt0UUZb7mwdhEb842AOOXuczxnBwiaIAhJ8QbTvyXhKTRA69iPaikikDZEcrTxo7XHdD6-Rf2IkWoN3JBoOV84zOW-jGjjC6EISk6XFLMU0dOikXjEfvv-SS8OA2cIX7IGIx7e5dr4xKhg8C1FwqrX1ValZSZ206iHbgSWCQdnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 20:10:43</div>
<hr>

<div class="tg-post" id="msg-141121">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حجت کریمی مدیرعامل تراکتور : آسانی مقابل ما بازی کنه قطعا شکایت میکنیم و پرونده رو به دادگاه عالی ورزش میبریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 213 · <a href="https://t.me/SorkhTimes/141121" target="_blank">📅 20:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141120">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
فووووووووری گفته میشه که مصدومیت یاسر آسانی جدیه و ۷ هفته نیست
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SorkhTimes/141120" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141119">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
یاسر آسانی مصدوم شد و با گریه از زمین بازی خارج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/141119" target="_blank">📅 19:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141118">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b64ca5d3.mp4?token=FY_ih5znM1fTQbsiHZt0zsE4G7i3CPsEiQujKdlWnPxkBPpgmYOhRIaJSN8mrt_Zmuawizg9l_y6hO7JbDbW1zF0oH9YEqZ3o4ay392uZfX1dweh63SlcBxONDJEn8PBgnbS9ZjzQKuPSPKK61by_De1u6m64gOFqzpsic4R0L9xIu8F_lyfD9YYNW46Ca7FZS5KYr6hWFeAEvOTMpkhdKrCtACQ0bbFtMc05fXl3bouXtCAZhsPK_l6Clr8Ai25xO5MDhCXMKEXmSNLRhgS9gaap0KRZWhH66VI7uO8Qv5Rd0P1AbEsh6YnCMc4EyscWuL6tGq1J_Pd8IB4YncrRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b64ca5d3.mp4?token=FY_ih5znM1fTQbsiHZt0zsE4G7i3CPsEiQujKdlWnPxkBPpgmYOhRIaJSN8mrt_Zmuawizg9l_y6hO7JbDbW1zF0oH9YEqZ3o4ay392uZfX1dweh63SlcBxONDJEn8PBgnbS9ZjzQKuPSPKK61by_De1u6m64gOFqzpsic4R0L9xIu8F_lyfD9YYNW46Ca7FZS5KYr6hWFeAEvOTMpkhdKrCtACQ0bbFtMc05fXl3bouXtCAZhsPK_l6Clr8Ai25xO5MDhCXMKEXmSNLRhgS9gaap0KRZWhH66VI7uO8Qv5Rd0P1AbEsh6YnCMc4EyscWuL6tGq1J_Pd8IB4YncrRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراض مغانلو به نکونام بابت تعویضش پرت میکنه کاپشنش رو نیمکت
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SorkhTimes/141118" target="_blank">📅 19:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141117">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hemymzQiuRRCtv6Ra7dHFYozWCebUDtY54N78c17Lxhj_-8DxGlDtRa3y_va6V8vcnp1gkRZSkRVvRDHDj8Gnf42VmDBeMq-AunPlMRMsIPVCWgXAcmTijC9peXzvnYQSSkSt7faQ1wF8otcEeIJer_jBKMh8gXfNe4VMROUfUOMDfh-0iZAEzrb6MJSVou9i7D4JP-SHACLjnGPrXlIrs3K8-SokZPefGmnaoJuMo8FVwAV2kLgX65ZSeH2BPshKMlxsHKb8MH7RA1dz9GZdXzbCxxfdo0uGOG4Doe9VfXxa5MPim1P5DoOvNS_p-OPZjsCkwfS5qJ79xxNzLySCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصاویری از آخرین تمرین پرسپولیس پیش از دیدار فردا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/SorkhTimes/141117" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141116">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
یاسر آسانی مصدوم شد و با گریه از زمین بازی خارج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/141116" target="_blank">📅 18:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
کیسه نیمه اول و یک بر صفر برد و خداییش تراکتور هیچی نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/SorkhTimes/141115" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ساعت 17 بازی ترتر و کیسه شروع میشه ..بهترین نتیجه برای ما از نظر شما چیه ...مساوی یا باخت هر کدوم تیما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/141114" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
حجت کریمی مدیرعامل تراکتور : آسانی مقابل ما بازی کنه قطعا شکایت میکنیم و پرونده رو به دادگاه عالی ورزش میبریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/141113" target="_blank">📅 16:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e84fd67a.mp4?token=vIU4Vq6706_N5otebR9Y4LdD8PyZiS82qLL7RyzRID-wgWfB_0GbIwKv0oFD8vcDG40UETLd4UzVxobXPUNxwHAJojjX250UCSxnbDakogCikRUTMQGW56c7OG17FuzLHjhz5TH8yLcD9zg0OZsI6veSVP9VvQ0AAQxoOj8YFUwhsOcQZcimStBPJI0GKQXkv7LjGVrTUWMeOEQDVsSb95FB8uNlt85LKTMr5Q7Zfc2HdRH0GUdzV_0TPhQHK-8TwnteZ95fbRKnHNSelwm_l18N4SW2cnyNXPXgf2rsIyUpymx18dZeLCh6mrqiiRt4Q45HRrdGLQbjNMkt_HVPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e84fd67a.mp4?token=vIU4Vq6706_N5otebR9Y4LdD8PyZiS82qLL7RyzRID-wgWfB_0GbIwKv0oFD8vcDG40UETLd4UzVxobXPUNxwHAJojjX250UCSxnbDakogCikRUTMQGW56c7OG17FuzLHjhz5TH8yLcD9zg0OZsI6veSVP9VvQ0AAQxoOj8YFUwhsOcQZcimStBPJI0GKQXkv7LjGVrTUWMeOEQDVsSb95FB8uNlt85LKTMr5Q7Zfc2HdRH0GUdzV_0TPhQHK-8TwnteZ95fbRKnHNSelwm_l18N4SW2cnyNXPXgf2rsIyUpymx18dZeLCh6mrqiiRt4Q45HRrdGLQbjNMkt_HVPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حال و هوای سکوهای ورزشگاه یادگار امام (ره) تبریز در فاصله کمتر از پانزده دقیقه تا آغاز بازی تراکتور و استقلال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/141112" target="_blank">📅 16:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
بازی شروع نشده تراکتور از استقلال شکایت کرد
🚨
حجت کریمی نامه زده به پلیس مهاجرت و گفته رستم و ماشا و آسانی مجوز کار ندارن و حضورشون تو تبریز غیرقانونیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/141111" target="_blank">📅 16:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
حجت کریمی مدیرعامل تراکتور : آسانی مقابل ما بازی کنه قطعا شکایت میکنیم و پرونده رو به دادگاه عالی ورزش میبریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/141110" target="_blank">📅 16:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
یاسر آسانی گفته بود بمیرم هم از استقلال نمیرم ولی رفته خودش به حمید مریخ که ممنوع‌الکار هم هست، مندیت داده که شخصا با پرسپولیس بشینه و مذاکره رسمی کنه.
❌
با این ۲تا برگه که فاش شده، یاسر آسانی قطعا فسخ کرده و تایید هم‌شده. حالا هی شکایت‌ها رو رد کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/141109" target="_blank">📅 16:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
اعلام زمان نشست خبری تارتار پیش از بازی با نفت آبادان
❌
❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و نفت آبادان مشخص شد. بر این اساس، نشست خبری سرمربیان دو تیم، فردا در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:  • ساعت ۱۴:۳۰، محمد نوری…</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/141108" target="_blank">📅 16:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
واکنش مهدی تارتار به دزدیده شدن گوشی همراهش : انتظارم این است که با دزدها برخورد شود/ کسی که همه دارو ندارش در گوشی باشد به راحتی دزدها می برند/ تمام خاطراتم در گوشی بود و رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/141107" target="_blank">📅 15:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
تارتار: تعطیلی ۵۰ روزه لیگ منطقی نیست؛ حداقل تو این مدت جام حذفی رو برگزار کنید، حتی بدون ملی‌پوش‌ها. بازیکن‌ها هم باید برای تمدید قرارداد با پرسپولیس جلو بیان، چون پرسپولیس تیم بزرگیه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/141106" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141105">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
نامه ای از یاسر آسانی که نشان می‌دهد وی به مدیربرنامه های خود مندیت داده است تا با پرسپولیس مذاکره کند
🚨
🚨
همچنین در نامه ارسالی به تاریخ فسخ اشاره شده است و این یعنی آسانی با استقلال فسخ انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/SorkhTimes/141105" target="_blank">📅 15:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
مهدی تارتار: این قدر کار در پرسپولیس سخت است و باید زمان گذاشت که نتوانیم در مورد تیم های دیگر حرف بزنیم
🚨
در مورد تیم امید باید بگویم یکی از بهترین نسل های خود را سوزاندیم. نتایج و کیفیت بازی فاجعه بود و در همین حد حرف میزنم چون فردا بازی مهم داریم
🚨
تیم…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/141104" target="_blank">📅 15:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
مهدی تارتار: ما قبل از تعطیلات شرایط خوبی داشتیم اما تعطیلی به دلیل نبود بچه ها به ما ضربه زد. بازیکنان شناخت خوبی از کادرفنی و ما از آنها پیدا کردیم. فکر نمی کنم به جز مصدومیت یکی دو بازیکن مشکل دیگری نداریم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/141103" target="_blank">📅 15:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
تاتار: به فدراسیون فوتبال نامه زدیم که حاضریم بدون ملی پوشان بازی کنیم/ 50 روز تعطیلی هیچ چیزی به فوتبال ما اضافه نمی کند به غیر از تفریح و مسافرت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/141102" target="_blank">📅 15:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141101">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
اعلام زمان نشست خبری تارتار پیش از بازی با نفت آبادان
❌
❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و نفت آبادان مشخص شد. بر این اساس، نشست خبری سرمربیان دو تیم، فردا در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:  • ساعت ۱۴:۳۰، محمد نوری…</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/141101" target="_blank">📅 15:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141100">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
دو بند مهم از هفت بند نوتیس ارسالی توسط آسانی به شرح زیر است
👇
🔻
ماده ۲ - دلیل فسخ
✖️
✖️
این فسخ بر مبنای نقض اساسی تعهدات قراردادی باشگاه از جمله عدم پرداخت حقوق و مطالبات قراردادی معوق و نقض شرایط و توافقات مقرر در قرارداد صورت می‌گیرد.
🔻
ماده ۴ - آزادی بازیکن
✖️
✖️
از تاریخ لازم الاجرا شدن فسخ بازیکن از تعهدات ورزشی و کاری قراردادی خود در قبال باشگاه فوتبال استقلال آزاد خواهد شد، مشروط به رعایت تعهداتی که طبق قرارداد پس از فسخ نیز معتبر باقی می مانند.
🚨
حال با تمامی این تفاسیر می‌توان با قاطعیت نوشت فسخ آسانی با استقلال رسما اتفاق افتاده و طبق تاریخ ارسال نوتیس فسخ، فسخ قرارداد و پس از آن مندیت آسانی به مدیربرنامه های خود برای مذاکره با پرسپولیس این فسخ در فیفا نیز ثبت شده است!!!!! مگر‌ این که باشگاه استقلال بتواند خلاف این مسائل را ثابت کند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/141100" target="_blank">📅 14:13 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141099">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
۱۰ روز پیش از مندیتی که آسانی برای مذاکره با پرسپولیس به مریخ داده بود خبر دادیم و امروز این سند مهم منتشر شد
🔥
✅
نامه فسخ
✅
نامه مندیت
✅
استوری عضو هیأت‌مدیره شون
✅
مصاحبه‌های تاجرنیا
✅
اینها همه سند قرارداد مجدد استقلال با آسانیه
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/141099" target="_blank">📅 14:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141098">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
نامه ای از یاسر آسانی که نشان می‌دهد وی به مدیربرنامه های خود مندیت داده است تا با پرسپولیس مذاکره کند
🚨
🚨
همچنین در نامه ارسالی به تاریخ فسخ اشاره شده است و این یعنی آسانی با استقلال فسخ انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/141098" target="_blank">📅 14:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
نامه ای از یاسر آسانی که نشان می‌دهد وی به مدیربرنامه های خود مندیت داده است تا با پرسپولیس مذاکره کند
🚨
🚨
همچنین در نامه ارسالی به تاریخ فسخ اشاره شده است و این یعنی آسانی با استقلال فسخ انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SorkhTimes/141097" target="_blank">📅 14:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141096">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNB6ZobILmfPYsFK1w2Nq6niiPoijQfQFc1TnvD3koxAsKHkfnkogk05VMJ1rydM5Fo2UISLcPk7XrPTjTgR6COYgHLrTOZ0AqA4h_gMk-d9bJk1zF6tXpTyWFyAVtbfEiryX4McfAOeb02BVX9ig96WAaKpd0Q0Kl-essYVtZHIVs0Tg1uC9FSqqsLvYLfOo5hmOplWlMfG-wcar8zDn3-ZppL_pikEYzPzyAxYjVHfGuBimlKawxcXNMedd1jPNH76Ec0s0t7PgHxb0P6NLH8ZUTGQ7fDjhaawc5IbHdEUtGmINKeX9sK3usZqzIHa9Gz_SkxpTNYgfIi3PiReAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووری
✍️
حسین پنبه کار:
🔔
اگر لابی گری‌ و زد و بند های عجیبی در داخل صورت نگیرد ، یاسر آسانی حداقل ۶ ماه از فوتبال محروم و تیم استقلال هم ۲ پنجره نقل و انتقالات محروم خواهد شد.ضمن اینکه کسر‌ امتیاز و سقوط به دسته پایین تر هم میتواند شامل شود
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/141096" target="_blank">📅 14:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141095">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kg_1p1oPY4qA67X8a1KwCpOuAFOkjB0JuC2WkiUYnhdztl4_wfhDIAuUFRnDeHqppSO5kBkk_m7JUnwddgmqGXHePXz6KBxsmIl1OwIw9lanWEbSwQGLmLJUmi-qpNa6UDob7CFYs1KuMgN7Lw6joWNVkoJ8hJK9N1LMVLgJ-C9OkExpmKAwfCZ0Eg6-L5hWpvYry9RD4spsxDHaRvfjauGIALc6YoBUBT22EJ0cpVIn3gW2Bw4lsXxN3WT_U3i3SuQsXhV9a8yff9eLCaQMeWgsR3rSMfw-D5eRa1YW9jYFgNzK4SxH__jj21qHZ9ujWDx1j2oNlQRaDb23mrzIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد صدرنشین‌ها؛ تراکتور و استقلال برای یک شب سرنوشت‌ساز در تبریز!
🔥
⚡️
[
تراکتور
🔴
🆚
🔵
استقلال
]
⚽️
تراکتور با تکیه بر مالکیت و فشار در نیمه حریف، به‌دنبال کنترل ریتم بازی و ساخت موقعیت از کناره‌هاست. استقلال در انتقال‌های سریع و ضدحملات خطرناک‌تر است و اگر فضا پشت مدافعان تراکتور ایجاد شود، می‌تواند ضربه بزند.
سناریوی محتمل: بازی نزدیک و فیزیکی با حاشیه کم برای اشتباه؛ مساوی یا برد خفیف تراکتور محتمل‌تر به نظر می‌رسد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/141095" target="_blank">📅 13:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141094">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
«رسول باختر»کارشناس حقوقی فوتبال:  کسری طاهری چهار ماه محروم میشه اما نتیجه مسابقه تغییری نمیکنه. سپاهان هم یک پنجره نقل و انتقالاتی محروم خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/141094" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
⭕️</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/141093" target="_blank">📅 13:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔄
🔄
🔄
در پرونده شکایت سینا اسدبیگی از باشگاه پرسپولیس؛ این باشگاه به پرداخت مبلغ 14 میلیارد ریال بابت اصل خواسته و مبلغ 539 میلیون ریال بابت هزینه دادرسی در حق خواهان محکوم شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/141092" target="_blank">📅 13:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
بیرانوند به کمیسیون پزشکی رفت؛ در انتظار اعلام وضعیت نهایی
🖍
علیرضا بیرانوند، دروازه‌بان تراکتور، روز گذشته در نخستین جلسه کمیسیون پزشکی در تبریز حاضر شد.
🖍
بیرانوند که به دلیل خالکوبی به کمیسیون پزشکی اعصاب و روان نظام پزشکی ارجاع شده، همچنین برای بررسی…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/141091" target="_blank">📅 13:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141090">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔵
رسمی؛ رضا شکاری به پیکان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/141090" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZwn2OyedylJ1Lp7t2oLiQqZk85NwNf7HPXHmII3YWU3g0gFEMez9izbWOqsoy9Ae_GSKcWKBnKayRMDQcPREvYfP78MN5Bar2p30kXPRo4c6-J278LPqHE1mgmXEnmy_zI7oeoNqcPX4DvqPMiRUYDMyTmFKlxPNQu_PEwB_CF0GzKl2p9smDTng57kwbZVftdn-glTH-Xyfy5n6C7AG2JtyGVqsItOFSxeyfmcdj9emc5hDPrzlviUGGaO0K0Sw0ceiB0p7TfBsTn6G237AVMW8cHYe9xBYMdUf5cP7dRqXUPse8N8zbKqSf0xPRu1iNV5JAMDVj_CAS7Z82MxEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
9 بازیکن جدیدی که وارد تیم بزرگسالان پرسپولیس شدند
🔴
1-
شاهین کیادلیری دفاع وسط 20 ساله
🔴
2-
امیرحسین طاهری دفاع راست 19 ساله
🔴
3-
آرتین محمدی هافبک دفاعی 19 ساله
🔴
4-
محمدرضا میرشفیعیان دفاع چپ 21 ساله
🔴
5-
طاها نژادخیر هافبک وسط 18 ساله
⚪️
6-
ارشیا محمدآبادی وینگر چپ 19 ساله
🔴
7-
محمد بزرگی وینگر راست 19 ساله
⚪️
8-
محمد مومنی مهاجم 20 ساله
⚪️
9-
امیررضا سینیکایی مهاجم 19 ساله
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/141089" target="_blank">📅 12:26 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
فووووووووووووری از ورزش سه
✖️
جام قهرمانی دوره بیست و پنجم لیگ برتر فوتبال ایران به شهدای میناب اهدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/141088" target="_blank">📅 12:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
علوی سخنگوی فدراسیون: تراکتور، سپاهان و پرسپولیس پیشنهاد دادن جام قهرمانی فصل گذشته به شهدای میناب اهدا بشه‌ و فردا تصمیم فدراسیون در این مورد مشخص میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/141087" target="_blank">📅 12:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📊
فکت: پرسپولیس در تاریخ خود در خانه به صنعت نفت نباخته است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/141086" target="_blank">📅 10:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g8_zHosjOq3DU6L5-mKaw5P_BBhW-nJFAtf_sBoKzLaYbFZarR02yt4vZgNF4BEvhlURDexdGfI_njk3Iv6Ia1VNiO_Zrq2ou4v5c0j4F5iEATsxL9emzjQkzXY4OcL3kmEVeIB8t3YL7LSjlbxrBWDiVMNwYatpCuJ0NOcLXVNrRcTseJmSQm0k8GHNl9ush0bawXJHHACSVSjkJdruxnciAcwHTTLTllPS3WbxIwlETWAywU8zVFCxOH42JZjoHJ9rU253tJ7XiY6TKm5KBXDHoZZzvc5YHOXcZfOwfq_OeR-_PB6bgz1-mx7cjj6yqXiZFisukfIekVC-eYHMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
◀️
مجوز خارج شدن امتیاز باشگاه پادیاب خلخال از استان صادر نشده و باشگاه پرسپولیس برای خرید امتیاز این باشگاه با مانع روبرو شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/141085" target="_blank">📅 10:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WwEIdQbzqd3z7_x7jGcvWMso8hySioaUaNoI-c-XTZ8cF0MNOuzc4ZACqxDfUpqV79rvfY6fOYrEFokGh6_GyQHDHYsmBEYSljMnOHz84SfveOJcNZGpctysV0H0nGuRJiKlUGgYqLaMK3BK30S10Hn6AlKl7EZKm9X3anfj7JqFkp01QcgF2tMRG7BHJ-mXVri__7uiLxe1LRjcurdwh25t7iqnAN5ijFIRcbKDZP_m9ijEw5gwClv4ycLcnboZj8wKKCwKEnMs11ddH_y-IfRxdmczFoWCv0ZCvcyDGvPvW0xGiD71c3cg-7uuV4LekNRQ4U54wIe4HiLACnhJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
◀️
سقوط تیم ملی پس از ۲ شکست اخیر
⚪️
فیفا امروز رده‌بندی جدید تیم‌های ملی را منتشر کرد که ایران با یک پله سقوط در رده ۲۳ جهان و دوم آسیا قرار گرفت.
⚪️
ژاپن، بهترین تیم آسیا در رده ۱۷ جهان قرار دارد و استرالیا هم با ۲ پله صعود به رده ۲۶ جهان رسیده تا به ایران نزدیک شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/141084" target="_blank">📅 10:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPSw29UrKT2tyBpyk96ePicZeylKirk6tXUgeFJCa7EbAZKN0RrUDI5yfFlPxfnbIlAfA6gUi0gKm392SI9LYBd7AcHG2pALSwNlFIlwhJKGWoRyvF8TlHGDNKvZMS3j01rViq6BDdkK_6iKgFOG-ctvHBbmfT4iQjwC5a9bXkptb1IksJdTxb5MdQzmeHUNiRL94ws6IbbomN1Wwqtcc41UoB1rocmQF5usEw3jDUckcR-QVAq9UYa6wTNGkz9yMh27644Ws_Xx7laorox2VYBiVlJCGldFtqeKEM9IiVMM0CTwqyuz0Bv9oUadaOOk5T_i_-AcPtDQT8ZfpCVZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هفته‌ی هشتم لیگ خلیج‌فارس ایران
🔥
⚽️
هفته‌‌ی هشتم با چند تقابل نزدیک و کم‌ریسک از نظر گل آغاز می‌شود؛ تیم‌ها بعد از وقفه فیفادی معمولاً با احتیاط بیشتری وارد بازی می‌شوند و جزئیات تاکتیکی می‌تواند تعیین‌کننده باشد. تراکتورِ صدرنشین با خط دفاعی بسیار قدرتمندش مقابل استقلالِ بدون شکست قرار می‌گیرد و این دیدار می‌تواند یکی از فشرده‌ترین بازی‌های فصل باشد. در سمت دیگر، سپاهان برای تثبیت جایگاهش به دنبال پیروزی برابر فجر است و فولاد هم در خانه شانس خوبی برای کنترل بازی مقابل مس شهر بابک دارد.
سناریوی محتمل: بازی‌های فردا بیشتر به سمت نتایج نزدیک، نیمه‌های اول محتاطانه و تعداد گل پایین تمایل دارند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141083" target="_blank">📅 02:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
فارس: مجوز خروج پادیاب خلخال از استانش صادر نشده و همین موضوع باعث منتفی شدن این انتقال شده.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141082" target="_blank">📅 23:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
هیئت ورزش و جوانان اردبیل با فروش پادیاب خلخال به پرسپولیس مخالفت کردند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/141081" target="_blank">📅 23:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_2B0ImgVr9jOUR3O2pagRkOlmVuR2ECkZUQHGmgAWPs-vzCQkpKai7el_-g4LbjUoAzdCu8VdL6DdGKm6QYdkED7ZpbdFc6CceiVge2Bkg3bV4CIogHG2hkx-95UEV9zF1FWqql42yIWqNx5n5y6IQwdDwhl599HmTNLL7fjYdMgPZGSpuKVOkW86g1U522D-HD18vnBwB1N8LRWBDTHOO1CZ_iPcxbRroP5sL1Wu27sOSktehMIJdKr5CORQuDmhLuOl4HBbEd9UIaDI9z2PEhxO8SPHPDXLO_lOlRjecvF8CGzigc55p8mEcvLz1J_1oKLB_nbdiSnc0WD9_4vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فکت: پرسپولیس در تاریخ خود در خانه به صنعت نفت نباخته است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141080" target="_blank">📅 23:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFqXeq8z6Q4Omc_jGxHXNbZWQI5-ByQHfBJ8tHafUhSfA4YAP5BZn8sCSql0nu-ty01i8BeFK6RxYWCPHwCethWjGIaoWtSboY6nI2dgEsdeKKCHC45QiJ_DNFcGfFApP4NXZf8Xv8iz0WwTDytjNalla7f9JrxWp5CBbPjFQVAGHqWDgOc6u9Nfb_1Mzd-vORq9GUiiA5nUzHSzoZ08FKZrCkNoUD94zlLFepYY2Q8Rkjf8-P55WZ7EtgXm77Zj9r07pJCitLKamlrRQi7pOtDF9t70zviO_zaCSlzuONukWEL95YZC75CqkIcD1XAJz28T2Wk4gc6ITJh-GTnsdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
طرفداری
:
✔️
پرسپولیس در صورت ناکامی در جذب محمد قربانی و استقلال در صورت نرسیدن به محمدجواد حسین‌نژاد، ممکن است برای جذب دهقان هافبک الوحده اقدام کنند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/141079" target="_blank">📅 23:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
✅
امتیاز پادیاب خلخال به پرسپولیس واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/141078" target="_blank">📅 23:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPSwXejkCYUm_D1vy7rKCYq0pEfnADxO6Xsi15I1JJULfT3IMnX8ks0qogRpiTOLYdZTKs_mnInSDvAx0ulDWVrAZ7zvhoYteJ_vyJkjbQTVo0hvHih03tgt1Fxy250GoctxauMC2q2FkpVagJBO4PgA3RTue-9wFlWRKw62OAzm5Eb-QiZSu3zUGoZyy_Ku_7s2b9jiSNi9WnZA0xUJqAb9TyoCwuGjQ-JXcRKN0MJ7XnFVwYPX4ebuhMt9gYvflMiyB953dSmb7AZvErOBVi5275G9SHK1f1vV1QCcvDIqf0jf3_jtEJqx9c9qw9W-6-1Tm6aYkM3-_Fpq1nYs3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
❤️
بیرانوند صبح دیروز به کمیسیون پزشکی اعصاب و روان به دلیل داشتن خالکوبی رفت، همچنین دستی که از ناحیه تاندونش مشکل داره MRI گرفت تا ببینه نتیجه‌اش چی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/141077" target="_blank">📅 23:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrnnWXbjJFSoT2yxrKFpfrp9FG88C62e1WzL2VQjYTxfkNHhiQkHOnCxmFe514PgWwFsjSfypDYqrAixIkjk7IB9X7mLBkrn5lcgw7sFc4La0JBCENAPZpucFi53ZQ5CjIPvoofZe4KEhG5P5ax3Yc-bAqvk9ZT_zdNMJ6MnCD5eeuEUPr92QFLSha1ddpQJuQUzaNDaexVmiGUd0G4HVoLlBN0gSdJzKwLZdtN-ZhKAM5c8NyLvYAAR1vZhhZ8kBvavYZAHYXTYUQnF4Q2jn6ap_odC5LwwXHpRkn9KfAQn-cEc2h5Z_latxYSRXmNwowDonr3CT6p90966FJMYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#یادآوری
✅
✅
استقلالی‌ها بزرگترین خیانتکاران به‌منافع‌ملی هستن حالا اینا به ما پنداخلاقی از منافع‌ملی میدن
✅
✅
سال ۹۹‌ معاون‌استقلال مستقیماً به النصری‌ها خوراک میداد برای حذف پرسپولیس‌، صدای واعظ‌آشتیانی دراومد از این خیانت‌
⬆
⬆
ما مثل شما نه‌خوراک میدیم نه خیانت میکنیم از راه قانون ۳ امتیاز دربی رو ازتون میگیریم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/141076" target="_blank">📅 22:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141075">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
پرسپولیس و دانیل گرا بر سر فسخ قرارداد به توافق نرسیدن/فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141075" target="_blank">📅 22:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💥
#فوووووری  | #غیررسمی
🖍
یحیی گلمحمدی قراردادشو با دهوک عراق فسخ کرد و در استانه سرمربیگری تیم ملی امید قرار دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/141074" target="_blank">📅 22:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141073">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎙
🇦🇷
لیونل مسی: غمگین‌ترین روز فوتبالم است
✖️
✖️
امروز احساسات زیادی دارم، اما اولین کسی که به او فکر می‌کنم پدرم است.چیزی جز تشکر از این پیراهن برایم نمانده. ۲۰ سال، حتی در سخت‌ترین لحظات، هرگز دست از جنگیدن، تلاش کردن، تمام توانم را گذاشتن و خواستنِ حضور در…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/141073" target="_blank">📅 22:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k74YeMuiMIMN-UiY1UaTXMSSe-R8mnXhc4SXGURZBia5fQC9uay7dFRVwiXFhN3ZVNTMJUoJAE97q6jKelHcBIGrvM_dIBZwFaQGltK2Oe7naHXQHE3SiOF6BSiCodk1TEIn0fAIvmam71-EhQMXvAyXaDyCAmqAX2l2GGR3iNqB2wHQZLt9QiCtTa78LjXaYlpxleSZab2h9koob1Sze_TmChIX1TmyFyBpJxY_zrGq8wysSszheZ01E7hbq-IusCnaVOFXqGlu5EfUrV1g_p_cgXBiGTdFJtDXVq6LQtiU-h_C6RU21qIsRBlFgfMXidwDkRe4L1QA3_UnK8PKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اعلام زمان نشست خبری تارتار پیش از بازی با نفت آبادان
❌
❌
زمان و مکان نشست خبری پیش از دیدار تیم‌های پرسپولیس و نفت آبادان مشخص شد. بر این اساس، نشست خبری سرمربیان دو تیم، فردا در هتل المپیک و طبق برنامه زمانی زیر برگزار خواهد شد:
• ساعت ۱۴:۳۰، محمد نوری سرمربی نفت آبادان
• ساعت ۱۴:۴۵، مهدی تارتار سرمربی پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141072" target="_blank">📅 21:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141071">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUpk8HWWmSJIyWcysFzOPC-mH1YjN29IRj0z0EEsNhee_S7JD-Lq6Bzi_KYQFEm8-dY0NPX3cyvxVLe92MyEX6pfCNra9tbkkFka2wNe7Pfr2noEvS3K1kUvFIuuz5Lu37q4OkhADyMikDfyx9O7DNGeF8mPRjM319TfBvVE12LFT7gLPn_o0HqeMIdK5Fqf97vMzoJCuF6xMU7s6UtKWR2qFrLICBL6JZNbXcKnz9PaMdstVLcBdgxjuhtJXssNG-bHDGkmgbR5iqb2PeYwL6UABMnFdl7Wb1j8IYFBI_5g-53Mhe1GaENIr6bzkW96n7n-HfIaWfsGyMUduu8WXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری از تمرین امروز تیم پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/141071" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141070">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
رامین رضاییان دیدار مقابل پرسپولیس را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/141070" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79fbb819f6.mp4?token=DBDZt8AbWXnvHtFqIdQbYLNY27D3My-sIwZFzXGhVzzO8qr731O9RvH1MotS3TRLPNRrEGtUkQa9ZOtRcZixdWi1OIAXjrL471MipSAWzIQeyUEFcsNo8Fp3bjDD7eHVTrfhRTcOOt-PbxPTIUclvTtQfLa6WE96W-25fJ4-dQEEUPcflOBW8UbnC9xL5kwgIykxoZb1RW9CYPugBpExDPDm2jy-5iHsgpzksVpC__UiG5xwPium3K63Z2siDJviPBZGqCn-v_zxTHkeQdMLhPUrjNWan12XAMYwbDD8nAOM3GY3TCOqHYuQXbph_WOJNW8VJtcP2HLxarxXxcjDoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79fbb819f6.mp4?token=DBDZt8AbWXnvHtFqIdQbYLNY27D3My-sIwZFzXGhVzzO8qr731O9RvH1MotS3TRLPNRrEGtUkQa9ZOtRcZixdWi1OIAXjrL471MipSAWzIQeyUEFcsNo8Fp3bjDD7eHVTrfhRTcOOt-PbxPTIUclvTtQfLa6WE96W-25fJ4-dQEEUPcflOBW8UbnC9xL5kwgIykxoZb1RW9CYPugBpExDPDm2jy-5iHsgpzksVpC__UiG5xwPium3K63Z2siDJviPBZGqCn-v_zxTHkeQdMLhPUrjNWan12XAMYwbDD8nAOM3GY3TCOqHYuQXbph_WOJNW8VJtcP2HLxarxXxcjDoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل برتری تاجیکستان مقابل چین در بازی دوستانه توسط وحدت هنانوف، بازیکن سابق پرسپولیس و سپاهان
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/141069" target="_blank">📅 20:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
با اعلام جواد نکونام، سرمربی تراکتور؛ مهدی هاشمی نژاد وینگر این تیم به بازی فردا مقابل استقلال رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141068" target="_blank">📅 20:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
✅
احتمالاً در صورت غیبت کنعانی و علیپور، یکی از بین اورونوف و خدابنده‌لو کاپیتان پرسپولیس مقابل نفت آبادان میشه؛ بعد از اون هم پیام نیازمند بازوبند رو میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/141067" target="_blank">📅 20:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141066">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLOtqe7p8kXjA-TKfpWGxQnrvuH50-TIxmqYvdYnTEjGm6-akrUI4Hl8fwivTYRNOCATfESIB64lUEJ8vSy2qESmbkSCi0701L6Exh2BhU4siJlo_DVHnDijcd3sx-513IqESbPImwElKcrX1JS-XlamER-s3V4XY5ayj8t8RVqqMOiLUNhICc4MUVxxYas06X3jsnSplrgHYws8_JDKtiAulpl9LDEafMZvzHC9W5S0zfYEdeYQ8vE8L4NMd3FAB8icCgDgygegMOzThHD82YqAUQRpALCHt_EH7JYOfW2wmdpLd6dk4M1UAqLr4jcizJkoSB-uZocWcmz_iMzSQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت‌ نود
🔵
کازینو آنلاین
اسپورت‌ نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت‌ نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141066" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141065">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤩
✅
هفته‌هشتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
صنعت نفت آبادان
🇮🇷
🗓
تاریخ جمعه ۱۷ مهر
⏰
ساعت ۱۷
🏟
میزبان شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/141065" target="_blank">📅 20:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141064">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVXIHuzJ_QuA6e_RaORUVm_r7N9jCiRGclXz1-AjAGn5sa69laeuIKtjRlBHa74tSCohHYKaZXKRd3fpTPZVm8OJUAl9VdcPdNvYRwi1pm_T99Ql9X3IiEpyDZf9H-tesSpc7Pozd06zEp-aM6A62_nmoVjRXA6wlqDWjUnURceeWp0ywUI8r8h9njjKZTlYBAHj1X-lchl3ekbjW-xVVO1a_T3K0ZlMXFWcph3Tp6BjDG4Hlc_0gVPPL0WC53hcIHJl4FfeK_U_OvUE5TGEwB8oZKMuSxc9GB8c_m1WM_MM2jw5Rx0p4X9AqMWu6oa3Ht5jzPMOYRetHsmPlPzrhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
حضور پرسپولیس در رقابت‌های فوتبال ساحلی بانوان
❌
❌
باشگاه پرسپولیس با خرید امتیاز یک تیم، فعالیت رسمی خود را در رشته فوتبال ساحلی بانوان در لیگ برتر تهران آغاز خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/141064" target="_blank">📅 19:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141063">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfXEvtq83elisun5Cj-AtqjI_ghxy0-OP92OMvkT0SqaFcZyA0BwOmuPlH8fsCeRe5Buk4uhIrfIG6NPXnsd7Fra0LP6u0pH6AXp4G_ZXcrfU6Q_p6Mm7jBaH4SOkk56b883TM0e7PVX-UWN_5MTmyDLa4KgpvphOXqfLo7MubpV7mcakdrufPy1aZ8Wi5Y0__uhpErrSq37sukmB1anYnFy9TAAA2y3u-n9eaTGBgSLcEyQUM_p7SBm6ocWtFKuQtW6NrbCsGl8cuS2KnsNKuuawrfdGc6_hKnsn0gGKvXPcFCewMw33XAnEZYV9E8kbV-i5s3S4VeiucOhihAj8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
⚽
سیدجلال حسینی سرمربی تیم دوم پرسپولیس شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/141063" target="_blank">📅 19:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
بازگشت سیدجلال به پرسپولیس!
🚨
اگر اتفاق خاصی نیفتد سیدجلال حسینی به عنوان سرمربی تیم دوم پرسپولیس فعالیت خود در فوتبال را ادامه خواهد داد.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141062" target="_blank">📅 17:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWREwVApDu4SuTOno1MFSkuO2GAynjIo4gdgeaYZYKq2587ERIcabeffU1vlo7BlE9oX3GjRRgD_F60O6KKOjJg6hOfSVHHdqf3fguTo2QOonf_Bn6P5wgyeQvxCAj-IuE17H3b67nPExdnojTWsiEzND-kldP5b6WDJJ-4zgqwsMfBujzDofEJ_2VGSrTBzOot8AUeen-O3uXE81L5VbEvi_yBuJIHhET8MZJ3ZNbo9okJO5R3pHvl_re-yISlWkHyb_yg95lKriscAEJk-N4wC4zKurgdIUXSnRXf68cTYD-GdkiRNGGrB2nM2SEZZ5lc9gArbKmSb3mnpv3_FLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
❤️
بیرانوند صبح دیروز به کمیسیون پزشکی اعصاب و روان به دلیل داشتن خالکوبی رفت، همچنین دستی که از ناحیه تاندونش مشکل داره MRI گرفت تا ببینه نتیجه‌اش چی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141061" target="_blank">📅 16:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
✅
ترکیب پرسپولیس برای بازی با صنعت نفت دستخوش سه تغییر نسبت به آخرین بازی این تیم خواهد شد
🗣
حضور حسین ابرقویی بجای کنعانی‌زادگان
🗣
حضور تیوی بیفوما بجای اوستن اورونوف
🗣
حضور پوریا شهرآبادی بجای علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141060" target="_blank">📅 16:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✖️
مهدی هاشم نژاد به دلیل مصدومیت، بازی با استقلال رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141059" target="_blank">📅 16:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiStPEQcYPfe-TKTRrEJyWd5QAAAKAFLE8B4yR9i-Hp4YekGfhmNIqk-XweNEfSU0GmIVFUxPpbdwzJTvxY56LxFqcCNfhamzfqwZOdmMKy69QMpMi6vXc-T0sAYf2Amy8TgldxaJ_gDimEmcx-5tqZW7j1K57stB4yN6bBZkmqrCpXxHhWmGBR6phNAfOTBi3XdPmVS7b-_ov5V9TdXSEP6SoSyg-HlPijb04gAaxVWj2Orm4iU9lixlQK484IP2wfLf0LtEcH4ezgfELnpthWmUIPUV444vtFIi9LpGf31UqQc5Ag-VthQdt9XFf7aq3HU1L5yHvT3fNQdF7f9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بازگشت سیدجلال به پرسپولیس!
🚨
اگر اتفاق خاصی نیفتد سیدجلال حسینی به عنوان سرمربی تیم دوم پرسپولیس فعالیت خود در فوتبال را ادامه خواهد داد.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141058" target="_blank">📅 15:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyUI2Q8ujSHt5ac5BSO4E1bL-p08GoBHpUZxC4gJuDGcL3wFyc6Hk4j0MwozsuyMgtuaMM81h35XOvnxl8cz0HWDXB4wbDQu606ZHCTn9ymgrdgQ0JDP3BVZB1VfZbxUC5ostlb1qtr7zKJ5diGo5WGQHk86IcSZv31mOZ07TSD3YWw9cky7w03C8dR43oyDNtvSaZFYYgk23Z_MRhwCiRKwGi1j9MsFEqsd3cuaUgBs-dlcv4imAzBiD00xk72NwRULljhBKpE5JVZb8hTMrWYUVHI-i5rzmqPF5UODlRiL4iMedK2EQ0Mc1rOGW_l7nsNm5pnXpfqXo__nInCFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
احتمالاً در صورت غیبت کنعانی و علیپور، یکی از بین اورونوف و خدابنده‌لو کاپیتان پرسپولیس مقابل نفت آبادان میشه؛ بعد از اون هم پیام نیازمند بازوبند رو میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141057" target="_blank">📅 15:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141056">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
رامین رضاییان دیدار مقابل پرسپولیس را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/141056" target="_blank">📅 15:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141055">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFolVkJpVzrhAc7xuuPojZPVqsoGCzLzPCPp5dOck9_CtwQUvZWIG5i08KcPCChOEqGIyVT13LZdusCX-SYg_KH9ng8sIrvVKLVzoDfoRFSGzLDZ1qpo4CUBQNC6OwtV6VknuhZuikEWLteW1cv_PrqpJ3GwLoYmAeqfvqMcvDUDaqitvISr5hzV3GHThKxxYpSbUovTIQuYlo3tnxVwRbNUOF7rMfljfLx5-YXiZ8sG3B6GsKtj7-N7EwmAoqRRAoGUVuzDLQrJaaOM1XDzt-WaiIIH7YwWKKewtE4Jx7mH8Ig5rdM5iE5lPZU9_XlGz-ijuUHoQq-TZXNFciFfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
#یادآوری
‼️
همینایی که با حکم ٣ بر صفرِ شکایت‌شون از ملوان صدرنشین شدن و الان باهاش طلب جام میکنن‌، پرسپولیس رو منع میکنن که شکایت‌تون ملی نیست گذشت کنید‌. ما ذات شمارو از خودتون بهتر می‌شناسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/141055" target="_blank">📅 15:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141054">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/djHRZl9k36-4HLu1TCbePv2v5zoHrE4FJBs0I2dDyFqOfHh0kvV3lklsYUf0yjTLj6iyLTHvwS8PXsX6J9PbStJ-x-RL0oVz6Ki68yr1swtfwHDGL2BQb3f3dFtQAaORlj_h_h3Itlzus_9V62i0X7nKeNep30be0cVBG4Zn3nihlVE_gdjXwQdRUX266gUwisCGxBxCvSCYWFXHzv4To0OZesn3IjaJt4yxluRMIbm-nfN54Dh7XO4k4Dr2K0ldRrwhKHwfVOLHQnUqUNV5BuQeSj0y4867G1u86BJRdqWdOYDY6VeTr45Gv7gX5Vdh8DhRhBdwe9igw5fL_NOlJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبر ورزشی: ابوالفضل جلالی به احتمال زیاد در اردوی بعدی تیم ملی دعوت میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/141054" target="_blank">📅 14:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141053">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✖️
✖️
فوووووووری
✅
تیم پرسپولیس مشهد ( ب ) با خرید امتیاز پادیاب خلخال در لیگ دو فعالیت خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/141053" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141052">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
فوووووووووووری
🚨
🚨
مدیرعامل باشگاه لیگ دویی پادیاب خلخال امروز در باشگاه پرسپولیس حاضر شد و برای فروش امتیاز این تیم به مبلغ 33 میلیارد تومن با باشگاه پرسپولیس به توافق رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141052" target="_blank">📅 14:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141051">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff23e6127.mp4?token=AjcyktKOCjotsI4bTH8UbmOUTzZMDpWsJsGZgAnmliGOCbApg-Yu2qst8aLgmCrNXVsNeQKvf3juyOKa1UgQMKo6RTeagZ12gb3Wa2ko2-6pr_yPtUC-k1LFXGLkF7XtsTG_D8QLA8sNAa9IDFPrnTSk_1JB70B5bGeaciiGWrzmEGA65xBz11ZB1Hrm-_wO7rJYKD-2fhK-IM-3IjW2_qIm9pqZtZQHZZveKME_01uQ42JkTGNCU03t6sxI9D1Z6iT8PSaCyPsk7mCWsHw-2H1QOMSt75VqJj9h43h_L5XxqVS04OirGSBjwfVmdEBKBFg0dYNwKrgOlF4_r3AF9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff23e6127.mp4?token=AjcyktKOCjotsI4bTH8UbmOUTzZMDpWsJsGZgAnmliGOCbApg-Yu2qst8aLgmCrNXVsNeQKvf3juyOKa1UgQMKo6RTeagZ12gb3Wa2ko2-6pr_yPtUC-k1LFXGLkF7XtsTG_D8QLA8sNAa9IDFPrnTSk_1JB70B5bGeaciiGWrzmEGA65xBz11ZB1Hrm-_wO7rJYKD-2fhK-IM-3IjW2_qIm9pqZtZQHZZveKME_01uQ42JkTGNCU03t6sxI9D1Z6iT8PSaCyPsk7mCWsHw-2H1QOMSt75VqJj9h43h_L5XxqVS04OirGSBjwfVmdEBKBFg0dYNwKrgOlF4_r3AF9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141051" target="_blank">📅 14:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141050">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
فووووووری
✔️
💢
💢
💢
تاج دیروز با مدیران باشگاه پرسپولیس تماس داشته و گفته از پرونده آسانی بگذرید
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141050" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141049">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
ارسال پاسخ دوم فدراسیون به AFC بابت یاسر آسانی
🔺
فدراسیون فوتبال که با سؤال کنفدراسیون فوتبال آسیا در مورد شرایط قراردادی یاسر آسانی مواجه شده، پاسخ دوم خود را به این نهاد ارسال کرد.
🔺
فدراسیون فوتبال ایران در پاسخ دوم خود به دستورالعمل حاکم بر قراردادها…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141049" target="_blank">📅 12:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141048">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
نامه دوم AFC برای بررسی پرونده یاسر آسانی؛ پاسخ نامه اول قانع‌کننده نبود
🔹
کنفدراسیون فوتبال آسیا (AFC) پس از دریافت گزارش‌هایی درباره وضعیت یاسر آسانی و احتمال غیرمجاز بودن حضور او در ترکیب استقلال، در دو نامه از فدراسیون فوتبال ایران و باشگاه استقلال…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/141048" target="_blank">📅 12:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141047">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9DkigMkQm7usyqT14X2UXi3MrK25lYln0KzwqgO0jo0MqSBwVM1nfLrTOWMozJSizumuSMbpKipQQjaVUlW97_7egij6Fyw_ntbcsc5FEC5P21EuC7THtwVARLLJAOXCLgHxPxdj0yqMu-j_k5GLuFCg35nUKkDPjbThcf6BPU2lZ-jdgeaFa5cU8mLshoboR3qZTIdtBRKk3eF6o9Nm4NkNUe5fHCTQnb2oF_IYLA1FWFFZyoagQ8qJDAi68lS4Hl6ZroUT-d8ME_R4kjC56-J5BPG_EvLckKtvlPd1NlVa1gLJJpu-v5SpLeB5vCfL2ZgJ-Una0MkWgveNbv-vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس و دانیل گرا بر سر فسخ قرارداد به توافق نرسیدن/
فارس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/141047" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141046">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1cVAALAZE3M0F7j_QtpHLP56myoeHNUr94ERoseuiLCe_xkscFBElApI4e4Iy7KHNYKfT4jlfGZFHw6j8M7L5sqWu_K1t4qB68YCtfNn16z5IzD3DpjIex0XhxxOmAdta1ECFSvNtbdobxaP7HydTCYLh9SJXtAkvjQBVHBF9rNSibhIBLnnYGQqluUpcHmZ3miQbCluNIgBQVAus9LfZgAtDLrNSkWCt8JWeEoFwBzgughZRIhtQdUhD3BVIz64RPHsmgHFvDy5D5O1ityxAtfmZRVY_6ZCI_DIOQNbvRjyrT8d9b_-tc4GYCnnGQ9MyB2xzBSJxT6gXQelL3hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔹
🤩
| طرفداری:
🔴
🇮🇷
💣
علی قلی‌زاده تمایل دارد فصل آینده در پرسپولیس باشد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141046" target="_blank">📅 11:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141045">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeTeezFnkxf8dVbfKIzOJVjQnOclJKG26SL_oSfFAPhspAcfcXsNNuI1mwnsGCY5DwQgxFekoAT3vfj4bZl8JfSFkwogGRqWLrfRjeO5fxMIPA-6ORtH87Fhm-xLtiWUXjZm1gbA7QIOBSQSMhBcTaRxUdC8zKnC4yj1kalSVmi9lYYb_URwm2pVjtVTnHVXNvaGfxhlcxzeXmBp3JRO5o5M3tQU6Q_o42rnO8XvbSZLEwr6Um49a4i_vXThGRgDNLl4tC38ejquB68MGYDhGNPUUARYkACPWb_H5N_FEiSZ1a6UYboSfRNEqRkltYrLgWAJOBAzx5-dIG41l2E_qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حسین کنعانی کماکان شرایط حضور در میدان رو نداره و به صورت قطعی، غایب بازی پرسپولیس است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141045" target="_blank">📅 10:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141044">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHux9KOaAbHm99tg-BP5eFQWq06gAHcVrPj3_nKhT0q9-uKAvYz223ec6lMGumOvd6ObUCioMORx_ciKO9ux1i5dCr38dkxCsk6OizXT87POJ7BaKlBrIsdC29UJgtRI0omztmylx4cxip0wl9ALhEWSxdLrjO39s1xJjFCXJAeKEOx3sVURC8fgaCgrf2nvAAseKXnmisLinO2fYmnKiKCkZXbqNtRTZWkoVXvlLMG2JX7Xy8eyRquhx6526DsWezHJaeM4I1gI9LwY7_ZeW-gRLqo28ajkDR5ndteyDCb778Gf7rSwxWGsYazdaf6FCgh2gx-gMx5NnHfW3vCZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استقلال بیانیه داده راجع‌به آسانی و گفته رقابت را به‌خارج از زمینِ ورزش نکشونیم
❌
کسی این حرفو میزنه که خودش از گل‌گهر شکایت کرد بخاطر باگناما و حکم ٣ بر هیچِ انضباطی گرفتن با همون امتیاز مفتِ شکایتی قهرمان شدند‌. یقه‌تون رو سر آسانی‌ ول نمیکنیم‌
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/141044" target="_blank">📅 09:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141043">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UJfQEzI_JTJWYTRlq4rp_IvPsuL51s7C7Q9O1oxPx_OTuHvNFlzMu6fC0sr8DMMJtgfNvXhApL41Hlc6qQRLpXjy4f815y7dhk1QNTjEMkkj9SosdJciWpgoxp4anQKMlAVhTDi6o2LRVHViuMixABxi7wk3Ck_3et5Mqdma3j2j4qPQTFK0EsxgdeFbS6TLzb8Ta9ZTrZ3--NNOsBXcfmWJPLELUb1Zs567TwTYiPP7ATJFM42z0GDUT921SVCogZ9iBq5l9rroRvKttXfyMbQQdBgYH4hHqNDJN4nUcKRiXkQThZwakr5fMCJsCCQtKpjW6lYkOoKiVQ4l7yCzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی تو بازی خداحافظی‌اش، ۹۳۲مین گل دوران حرفه‌ایش رو زد؛ ۱۲۶مین گلش با پیراهن آرژانتین!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/141043" target="_blank">📅 09:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141042">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎙
🇦🇷
لیونل مسی: غمگین‌ترین روز فوتبالم است
✖️
✖️
امروز احساسات زیادی دارم، اما اولین کسی که به او فکر می‌کنم پدرم است.چیزی جز تشکر از این پیراهن برایم نمانده. ۲۰ سال، حتی در سخت‌ترین لحظات، هرگز دست از جنگیدن، تلاش کردن، تمام توانم را گذاشتن و خواستنِ حضور در اینجا نکشیدم.
✅
✅
اینکه دیگر با تیم ملی آرژانتین به اینجا نیایم، درد بسیار بزرگی خواهد بود. دوست داشتم تمام عمر اینجا باشم. بازی برای آرژانتین، زیباترین چیزی است که وجود دارد.فکر می‌کنم وقت خداحافظی من فرا رسیده. با هم رؤیای من و رؤیای تمام یک کشور را محقق کردیم؛ قهرمان جهان شدن در سال ۲۰۲۲.
✅
✅
امروز باید غمگین‌ترین روز دوران حرفه‌ای‌ام را تجربه کنم؛ روزی که با تیم ملی آرژانتین خداحافظی می‌کنم. دلم برای همه شما تنگ خواهد شد. از حالا فقط یک هوادار خواهم بود؛ آن طرف، کنار شما، تا از این بچه‌ها و هر کسی که بعد از آن‌ها می‌آید حمایت کنم. برای رسیدن به موفقیت‌های بزرگ، به گروه‌هایی قوی و متحد نیاز دارید. از خدا ممنونم که مرا آرژانتینی آفرید. به آرژانتینی بودنم افتخار می‌کنم و خوشحالم که توانستم این رؤیا را در کنار همه شما به حقیقت تبدیل کنم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/141042" target="_blank">📅 09:48 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141041">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7ZXnvMO2f0LW4xrdV1OvCs0q8xUJkcmarOTlShPz0fudR7kgzyqKcypqD6AK0mP8ziU4FXj4VQ8vRl7VINywBv5RCWHCUipkaZDP7UxQvR4mKe34mt3SdFQ9rGc5bEp3T5peWPpRubyLgZ3SXAjEJ5GC5WZRkQ0E9DkD1mUt0esneT3gs0W7ZhJXcpRf5NmBGZ6SE-BNyNEKQ-S4ObGhx-_2qV6PUDmxJjz413b6NwpwWEE_oz6MjH6UKUGR56ZVXU6gYrR_51qthUw2zkKE9exV1m4rhLCs7M9_6wJ9jEg1cV4GrPPs0jxbC8GbGie7-QYYV6FBuZi0mSeeVhiyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
ربات وینکوبت در دسترس تمامی کاربران
🟢
بدون اینکه از تلگرام خارج بشید میتونید مستقیم وارد سایت و بخش بازی‌ها و کازینو بشید، پیش‌بینی ثبت کنید و براحتی واریز و برداشت انجام بدید.
📌
حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر براتون باز میشه:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141041" target="_blank">📅 01:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141040">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
⭕️
ترامپ:
🟢
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141040" target="_blank">📅 00:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141039">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❌
❌
❌
کهریزی از استقلال دور شد؛
❌
❌
محمد محمدی، مدیرعامل آلومینیوم اراک، به‌دلیل اختلاف در انتقال خلیفه و گودرزی به استقلال قصد دارد رضایت‌نامه عباس کهریزی را برای باشگاهی غیر از استقلال صادر کند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس …</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141039" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141038">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
#تکمیلی؛گویاخبر آزادی امیر تتلو خواننده مطرح ایرانی از زندان تایید شد و بزودی او آزاد خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/141038" target="_blank">📅 23:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141037">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
فووووووووووری
🚨
🚨
احمدرضا براتی کارشناس حقوقی: حتی اگر آسانی فسخ کرده باشه نتایج سه بر صفر نمیشه و فقط پنجره استقلال بسته میشه و آسانی چهار ماه محروم میشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/141037" target="_blank">📅 23:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
نایب رئیس فدراسیون فوتبال پرتغال: رونالدو دیگه به تیم ملی برنمیگرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141036" target="_blank">📅 22:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OexoVVbi_1maQIYnam7UiiYK_n1tVdZfbGPpI-B6xKLYMp2yFW2n1Q1K0fcb676KR8IRDtLAtWauK9jHB87t10J5cSD3jVB6u60i_1ERfPv1Mmn6m4rJW2mbwTMjY_NQ8silZnFhCadOl2nrLga_6bkinYeXi4sRNEX9ZQs0S5IxxVmDuNE7tVqv9jm7GaGfbFrZMDbnkun1q57hfvP9xIF-xyl8d9rEI6i_HwTAxfIlLub9J8xU_ORbMj12b1MohR01veemK4rUOrOpAISt3I2rH6ElcIx6PYkAT1HKasyPSI4BJ6Poj0CkPzPuJeVpsxQS8bu0m-p_h-fEeWmg9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/141035" target="_blank">📅 21:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f02aed72d.mp4?token=hnoam4YdYrOpeNDMkfIJBsn6TLZJkAgHoSdim6eNwseRNuZw6MW2HFxO6_fL0Aesqmx1NqscP7LbuswUEb5cAt8NhOsZwzXOXP0BIF_cT1sVBVE8z2S-dlnekv7pJavdamLaqOJG71psGKBJRi3qh4xukVXlJHz-EK_Hw2OIPPEnyESmA245hy_EFttCDm566EE3I9n7mvNIcTtOuexAQsLqBCHJnXf9iu0Lb0Nhj_T06mqYejNqdwLh3BZnXUVMMLvjrBL-PvaNngZDBqv98TK_vN0oGsYDERyXjp5ccvwUtAwO7iBF0OHWexuIKAEysPMc9kw7YexGhLJ4IFt6VYXFW6KULoLB0ZjpUKtfsAvjA83ciZAObPJUuf4c4k5VEnNTYfSHMom_uxu5hKkbE2N0OBbyTgTD6lp4DemUz4tD0tcQuB-bHSoJKpqFVjkOHKAkMFSfJ3t5ZqxBybyai0ttrfiUVROqarqOZcJVhfoY7KqoiO4C9cD43bmAmmWgGSkSFN2dlMxfawl-CcAvbNwORTHLPWUzr47CHz4QN_HKLQoSjfzu84yBisPQGAFugjtgZ8OhBl6UrBdoh-zSEOxmjgEDlsE769Aci9s37-BYVzVmHnVhrTMBP4m46qqXNk5Qc0C9IKQ30SzJTsU8gxMHvtTNseHgGziJu8m_8pk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f02aed72d.mp4?token=hnoam4YdYrOpeNDMkfIJBsn6TLZJkAgHoSdim6eNwseRNuZw6MW2HFxO6_fL0Aesqmx1NqscP7LbuswUEb5cAt8NhOsZwzXOXP0BIF_cT1sVBVE8z2S-dlnekv7pJavdamLaqOJG71psGKBJRi3qh4xukVXlJHz-EK_Hw2OIPPEnyESmA245hy_EFttCDm566EE3I9n7mvNIcTtOuexAQsLqBCHJnXf9iu0Lb0Nhj_T06mqYejNqdwLh3BZnXUVMMLvjrBL-PvaNngZDBqv98TK_vN0oGsYDERyXjp5ccvwUtAwO7iBF0OHWexuIKAEysPMc9kw7YexGhLJ4IFt6VYXFW6KULoLB0ZjpUKtfsAvjA83ciZAObPJUuf4c4k5VEnNTYfSHMom_uxu5hKkbE2N0OBbyTgTD6lp4DemUz4tD0tcQuB-bHSoJKpqFVjkOHKAkMFSfJ3t5ZqxBybyai0ttrfiUVROqarqOZcJVhfoY7KqoiO4C9cD43bmAmmWgGSkSFN2dlMxfawl-CcAvbNwORTHLPWUzr47CHz4QN_HKLQoSjfzu84yBisPQGAFugjtgZ8OhBl6UrBdoh-zSEOxmjgEDlsE769Aci9s37-BYVzVmHnVhrTMBP4m46qqXNk5Qc0C9IKQ30SzJTsU8gxMHvtTNseHgGziJu8m_8pk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🎙
گرشاسبی:
🔻
تاجرنیا نباید دنبال این جام باشد.
🔻
قهرمانی پرسپولیس در سوپرجام با قهرمان سال گذشته استقلال در لیگ خیلی فرق دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141034" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
✅
#ورزش‌سه : حدادی پرز گفت پرسپولیس دنبال ترابی نمیره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141033" target="_blank">📅 21:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141032" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kqz6woKfnXiaG5ubox0x5EdIL-Ah80-JYSAzh04-vMUmFcUU-DV2Vj9kMeqx7RfIIt8YEajElqA-IWssJGyLenQkfNSyFMEy2INgojdhD7OKXVk3ADLgONytah6anP1aZdAJLdRE6il4we55ja1QmJJ7gOaBYIfe_WkvGG1TD9HN6zOAI-I87p6mRuKzL1TTApLpXXF2XIRNkaXQKe-DC8V6NHnsh3Q3UMDHLcdYRy-w3dJT3d6QIt5tddawvEq1GvgNM3fTFUO1JXwZZt3gA8g-AbwdL5ChHIWmzto0GDgGHT7wFaVFO2IiKACuV1slJ21Q-5Uah9K7a_IzSi4AwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Croatia -
🇪🇸
Spain
⏰
Tonight 22:15
🏟
Stadion Poljud
⚽️
اسپانیا با ۴۰ بازی بدون شکست و میانگین گلزنی بالاتر، از نظر فرم و قدرت هجومی برتری واضحی دارد. کرواسی در ۲ بازی اخیر ۱۱ گل دریافت کرده و مقابل اسپانیا هم در بازی رفت ۴ گل خورد؛ ضعف خط دفاعی مهم‌ترین نقطه نگرانی میزبان است. باتوجه به‌فرم دوتیم احتمال می‌رود ماتادورها در این دیدار هم براحتی پیروز میدان باشند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141031" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1vsfXmeBmXzIDNpbzuv0cIHvAbzbOLk8U-vb5nzmt6KKW5aQxmBnwGi8ScmDHCIbDEUQGIcnHDBq0A37Gv8GcJ50SwA-XNbAXRvDuomWi43exO1NeofgT7Fw62MjH814PAR2kCV3rDgTtC5MOEHfCVnY2_3v3TiPAKZabLAGa_GLk3Mxr_cK3ICJgcESJyoh_k7-kiSgQqdgKKZUea3iSN6dPeZsGj3XzKAjnLdX64Mp_wM4Xs1qFXlE3jNfTeZBy4P7smjypetRgEYYZFhtYIS5Gh9ekIpQb8Bn_cbqukCIBIZNay4tVBBnfTUMseLx_i4v4ysn-aiXej7-5qy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمودی: تمام تلاشم رو تو تمرینات پرسپولیس می‌کنم تا نظر کادرفنی رو جلب کنم. اول می‌خوام تو پرسپولیس بدرخشم و بعد بتونم برای تیم ملی هم بازی کنم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141030" target="_blank">📅 19:58 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✖️
✖️
✖️
مهدی تارتار با بازگشت مهدی ترابی مخالفت کرد/ورزش‌سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141029" target="_blank">📅 19:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141028">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3oAxYVNgBTMpFRRqhdQ9vK9czpxIQsiUReLfxO9VBLV7gWEEeY2tVs2tUhQKt6I-MhGhfeQUo1Wn7Z3Caf0pj0v49ESfGzZRyH_1HrZdRZE5Q5Mw77OtMYdYhOj0baNWf3T0-0wPru0l9hN8DnAqC9Kh2_moX-CGN9lSPKWwM58lePH8iI-d33N0Ezu5YUuOV1VCuz5H3JzaVtV_aJptM408we5Jjv7BzYuLxRFvolx-1f0TiG1BjrYiDTqmge8Z0PhYGijwl0Radnc6ZT3RBAiGqg4V1K3pxQTLgwmUyq8R9S8za5qH7zZZ5bwQ9gTC10g7rhoB5Ty8ghtMuuo2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
آمریکا ویزای تیم‌های کشتی ایران را صادر کرد
🔹
آمریکا به تمامی کشتی گیران و اعضای کادر فنی تیم‌های ایران به غیر از یک مربی روادید حضور در مسابقات زیر ۲۳ سال قهرمانی جهان را صادر کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/141028" target="_blank">📅 19:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141027">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/141027" target="_blank">📅 19:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141026">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/141026" target="_blank">📅 17:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141025">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOtY4yMwmSVJ976t0OzDbOQxHg6JL39aXvYSPhP2oxdEVfCSAEbiRXeyvMHY1dahI0OiiJIkHeJ8FoVx8eRzxbuu56yA2RaNtgqXl3K6W-LF2uyTMRBZV7960c-GWP9jkXO3fXs4zgHD9H9ReZkCV-AW8ldaOnNOckna5078DEEWh9u_ZVwNKhW-CQECEAS01zX92ZXsVLrgp0ugDICcalyNv7X_aDmoIAHY68udpTl_c4rYaGmsK5cmycTdV7taFW13Q_re2uJcE_sBcBOzg-Zb3Bt5CC5dcuFhpdt7JuYhGiXuZvEEuQ7tVp0mdIsSqL8MTN4we64pxiZ-0qNB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
✖️
دنیل‌ گرا در دفاع چپ؛ چراکه نه
🤝
🤝
باشگاه پرسپولیس برای دنیل‌ گرا هزینه کرده اما ماه‌هاست که از این بازیکن بهره‌ای نبرده است.‌ گرا بزودی وارد چرخه تمرینات گروهی و مسابقات خواهد شد و می‌تواند گزینه دیگری در اختیار تارتار باشد. او در دفاع راست رقیب تازه‌ای برای مجید عیدی خواهد بود اما همچنان یک بکاپ مناسب برای دفاع چپ نیز به حساب می‌آید. پرسپولیس در دفاع چپ همچنان دچار نگرانی و کمبود است و با مصدومیت‌های متعدد جلالی اوضاع کمی نگران‌کننده پیش می‌رود پس می‌توان به جابه‌جایی‌ گرا از راست به چپ و حتی روزهایی که عیدی روی فرم نیست حساب باز کرد
✍
ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141025" target="_blank">📅 17:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141024">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM08frnerekkurAYNV7ksg9e3YPXzsaVPVeWQu3htp3aw-SzPxHOoOkA_klo73Hwke19o7gNiIkkGGQKn6YdFTIQH-KfL4Y9Lik6L5vefLTGwe-WUbjupz0-4jPBUaiypQHeFce9zjSspuUTMvsEYjJj1Mm0BSYbxywd4jpjMme-aPRfQrfNvYQxuD4idNXQlLGwhpuc3ubay8kMl64AdrPu1VC6PpdmyRVI-1yeh6nGMdRXhgJBl7BuWci3nBqb3ELQk_YmQU9LODf2Lx0bCWn_SPCpK2T9xRerQvI0WnfIjwjdEwVRhB7VlWPl75z7Se4vBQtPW2s2rRM9Sk30Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
مجموع قرارداد بازیکنان پرسپولیس اعلام شد
⛔
⛔
مدیرعامل پرسپولیس: «جمع قرارداد پنج بازیکن خارجی ما ۴.۰۸ میلیون دلار است.»
🔹
با دلار ۲۷۰ هزار تومانی، این مبلغ حدود ۱۱۰۱ میلیارد و ۶۰۰ میلیون تومان می‌شود؛ یعنی حدود ۱۰۱ میلیارد تومان بیشتر از مجموع قرارداد ۲۷ بازیکن ایرانی.
🔹
مجموع قرارداد این ۳۲ بازیکن هم به حدود ۲۱۰۱ میلیارد و ۶۰۰ میلیون تومان می‌رسد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141024" target="_blank">📅 17:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141023">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✅
✅
مهدی ترابی به نزدیکانش گفته بعد از اینکه رباط پام رو عمل کردم، هفت ماه دوره نقاهت رو گذروندم و تمرین بازتوانی رو هم تمام کردم دوست دارم به پرسپولیس برگردم!//خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141023" target="_blank">📅 17:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141022">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
سرقت موبایل از سرمربی پرسپولیس
🎙
🎙
هفته گذشته موبایل پیمان حدادی در مسیر بازگشت از محل مسابقه به سرقت رفت و حالا این اتفاق برای مهدی تارتار تکرار شد.
🎙
🎙
امروز پس از تمرین تیم پرسپولیس، دو موتورسوار در اتوبان تهران کرج موبایل تارتار را سرقت کردند.  «سرخ…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141022" target="_blank">📅 17:40 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
