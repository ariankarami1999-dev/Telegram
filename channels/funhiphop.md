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
<img src="https://cdn4.telesco.pe/file/YYyN4YLCDQY9xeyhYahq1h2fTtsurmpT6nPg5JKCl6KpI_1T7sT9cCffMJqQUAlfmJAAGDAxl7YDoeNc2Xp9GQq5T_6etbHufydjiQbAvl1d95udCexwWYgd-sQpSBg9TyqIPteEzQC8VidZ52EllYSL2EAJWvnT9lSy5z1-Xbgy2dlc1CfKBnxNA7jSfFCoYcaVHG71fsn3_TbQXtQix5QkZ84NnW4E7ATb-AZ6xEf0GJ-eHLqjLVS1t3Sm9_oXfa9_NUU1zit5OMTT9J6hhSjv6K7Q1iUoLRxa2BdA0h9M00U4bE5brIcOaST7CQAjJKLL2KrjoS5mEffFyd02ZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 20:25:29</div>
<hr>

<div class="tg-post" id="msg-75678">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
منطقیه
آکسیوس: نتانیاهو از ترامپ خواسته دور جدیدی از مذاکرات رو آغاز کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/75678" target="_blank">📅 20:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75677">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپو پوشش نمیدم من، خستم کرد</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/funhiphop/75677" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75676">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=Iep3NPpv39l0_Ms2dGaen1dHiHnKLVKVczhKFJs4M14ShU_qoCtqqc5zs3t3FTQl8fsxqnHPERwFGWRC3HpIcCOQ1S31WPa6sf-bBNsWEz3S8ZItEul_pq2oka2yhCnbne5_27Tu_lQCjpFlwZBO15WWBem4uoOBi9_jL22EL__Lok8mqaBQWOqV38O8eo-vbvJt_b4jk_yTMtuCB61kYBrsBtWNK_EdEjRGs2VprlglnRmYnNWoNQ8h6j5bzdV_FzpQL-AI31fjq_F9b29pRaaLcDIE_C31WUsHh1rBggGKw_wDpiuiFJyq6fvvk0xZun3jHzehRB2Z3gySclH0kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556efd3c71.mp4?token=Iep3NPpv39l0_Ms2dGaen1dHiHnKLVKVczhKFJs4M14ShU_qoCtqqc5zs3t3FTQl8fsxqnHPERwFGWRC3HpIcCOQ1S31WPa6sf-bBNsWEz3S8ZItEul_pq2oka2yhCnbne5_27Tu_lQCjpFlwZBO15WWBem4uoOBi9_jL22EL__Lok8mqaBQWOqV38O8eo-vbvJt_b4jk_yTMtuCB61kYBrsBtWNK_EdEjRGs2VprlglnRmYnNWoNQ8h6j5bzdV_FzpQL-AI31fjq_F9b29pRaaLcDIE_C31WUsHh1rBggGKw_wDpiuiFJyq6fvvk0xZun3jHzehRB2Z3gySclH0kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخدا من هزینه نمیکنم برم اینستا اینارو ببینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/funhiphop/75676" target="_blank">📅 19:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/funhiphop/75675" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75674">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j41sglQtxJrbai-wJaeD31ppSySzWwtIDOkPXZpcy81KOn_1qVBsVluq5ZsJ_ZJRkOOkmnUYeH3KF64y9GlaUqFOB5nf9s46mEzp5Ls18AtIhYWkI3P3VaOCxsYoaIMB68gb3ufVijSJJs9S4jMZs_NrUDzPbGoNIsAfKA-xvsgmGPnBrc__NV6Gp_kD_uVgM1oqm6N48INLOOdF2ugLKUa4gcjVNGF98Lqw-N5c8r-jYL6_-kyB3b6tjq0N2a-CBUj66jMcIzrK2fo4r436uP1pHokPR8JI3NF95aYhvtIR3KP_Xbx3TfzVGTgCVGifSQbN8EmG__94skI1ZF8ucw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/funhiphop/75674" target="_blank">📅 19:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">خبرنگار اکسیوس در توییتر: ترامپ میگوید پیش نویس جدید توافق با ایران را با مشاورانش بررسی میکند و احتمالا تصمیم نهایی را روز یکشنبه میگیرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/funhiphop/75673" target="_blank">📅 19:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نیویورک تایمز: فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند. این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/funhiphop/75672" target="_blank">📅 19:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75671">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فایننشال تایمز:
میانجی‌ها معتقدند که آمریکا و ایران به تمدید آتش‌بس به مدت ۶۰ روز و فراهم کردن زمینه برای مذاکرات هسته‌ای نزدیک شده‌اند.
توافق پیشنهادی شامل بازگشایی تدریجی تنگه هرمز، بحث درباره رقیق‌سازی یا تحویل ذخیره اورانیوم غنی‌شده بسیار ایران، و تسهیل محاصره آمریکا بر بنادر ایران، همراه با رفع تحریم‌ها و آزادسازی مرحله‌ای دارایی‌های خارجی تهران است.
یک مانع بزرگ همچنان درخواست رئیس‌جمهور ترامپ است که ایران ذخیره ۴۴۰ کیلوگرمی اورانیوم نزدیک به درجه تسلیحاتی خود را تحویل دهد و سه سایت اصلی هسته‌ای خود – نطنز، فردو و اصفهان – را از کار بیندازد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/funhiphop/75671" target="_blank">📅 18:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">من خودم بتمنم ولی الان بحث، بحث وطنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/funhiphop/75670" target="_blank">📅 17:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLRaAG1uBSO8I_B4Fd_ZOzMTwl5OKyE-LRssUqAE8i5NI4gVA5NaIXMMFh8PSL6fM6DYc09Ifu8DmXbSMX4Ak8e2nBgN_ZLifnOtleustI8S6IeYjDQTBkGIP7nalw975tO-l5MZB1SNzTvYRnRBp_K1ijJ_ma1-9LfA3loOnlQIZpUYgWvO_L4AKTbrDRJd0r13x-id8XJZdekpCJIfUJHio0lNU14oEDavAl1Nn5WPHJ4FOPRdqrfg4RPUhOJShRBqUvG48q54jotHyziedQIdpCBxNzjcYMnK9XuIe6I-cIPDRLCnAcEROgowwoEXlFsuQVqlSZdN8JJEEwmVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور پررنگ بتمن در تجمع اعتراضی دانش‌ آموزان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/funhiphop/75669" target="_blank">📅 17:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آخرین باری که اتابکی گفت میزنن ۸ روز بعدش زدن امیدوار شو ایرانی   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/75668" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75667">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/75667" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک مقام ایرانی به الجزیره:
ما به یک تفاهم‌نامه با میانجی پاکستانی دست یافته‌ایم و در انتظار پاسخ آمریکایی‌ها هستیم.
تفاهم‌نامه شامل پایان جنگ، رفع محاصره، باز کردن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه شامل مسائل هسته‌ای نمی‌شود زیرا این مسائل پیچیده‌اند و نیاز به زمان کافی برای مذاکره دارند.
پس از ۳۰ روز از امضای تفاهم‌نامه، ممکن است درِ مذاکرات هسته‌ای باز شود.
قرار بود رئیس ارتش پاکستان [عاصم منیر] تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی به واشنگتن رفت.
برای ایران امکان دادن امتیازات بیشتر از آنچه در تفاهم‌نامه آمده، وجود ندارد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/75666" target="_blank">📅 17:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا: آمریکای خاورمیانه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/funhiphop/75665" target="_blank">📅 16:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUIIsVN5Qemijzoj7T8Ynm84x0W4dLalBALcTezTMHCGxT5SaNgpnahJXlfJusoRqy9tI9uGlQ5F0r31mKVNpJjnD4DjWePWRbGxjaZWCxY8w1NU_J-zBGskMyrRIHzOi4pbiYEUxXqtrenJiApQdBotDYEJu7C4FxBfOjJ_DgfYgluY9-sf6QZ9Xoac1QzFU6vbHoxv43IE6o9aLBx43rSE8YLeJFl0xBxBH3VlyjvrQT4iX_E4GrSO589wFjqVl9ha3Ov71gSQAeVmqpZhRNG1EUlmDs4U8MaAA26YqhgarHJd20DuTAbaLkMX5U8XC433OCDQZbVFbGA1F3ixvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با انتشار عکس نقشه ایران با پرچم آمریکا:
آمریکای خاورمیانه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/funhiphop/75664" target="_blank">📅 16:48 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b026396695.mp4?token=OuhzMt3aR1MOMEK7B-FzkkN0mcouy52N0leXu9V_cIBvriG5_6WSeWzp_nH4d5tiZBpDqN20B3JRyEpqybVfyLJpOQ3p56G6kmB2Ru-LJAvt71BO_eg5O6SQIEsDHhZxKXE24UZDqalz5XH54kk_EPH-sbm65i1WrbWxGVzhyyX4JuCBJ2eLZy_K5R398kiuPNG9n3-7cA79wNaIKQq-RSayM5PPBlgbQqH4_0eOrskRtxDBF6VNmPpH4exRRP0m4cG2lZcljPTVbXXXurePWuLlVKJ3HHQWurxy_0IY72aT7XRSCYS9a8lMxdxtcRWKulAbLnO5gpAo5uX6Gggxnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b026396695.mp4?token=OuhzMt3aR1MOMEK7B-FzkkN0mcouy52N0leXu9V_cIBvriG5_6WSeWzp_nH4d5tiZBpDqN20B3JRyEpqybVfyLJpOQ3p56G6kmB2Ru-LJAvt71BO_eg5O6SQIEsDHhZxKXE24UZDqalz5XH54kk_EPH-sbm65i1WrbWxGVzhyyX4JuCBJ2eLZy_K5R398kiuPNG9n3-7cA79wNaIKQq-RSayM5PPBlgbQqH4_0eOrskRtxDBF6VNmPpH4exRRP0m4cG2lZcljPTVbXXXurePWuLlVKJ3HHQWurxy_0IY72aT7XRSCYS9a8lMxdxtcRWKulAbLnO5gpAo5uX6Gggxnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتابکی که سری پیش هم زودتر گفته بود آمریکا حمله میکنه بازم اومد گفت چند روز دیگه میزنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/funhiphop/75663" target="_blank">📅 16:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/funhiphop/75662" target="_blank">📅 16:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75661">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیدار عاصم منیر با پزشکیبان و قالیباف در تهران   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/funhiphop/75661" target="_blank">📅 16:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiAOA_Ejwfk0NCsIjKgpzRbFcgr_gDE1-ju8Sgdyx07XHQ1ViZNl9rZk6g3RYxnFWW96Jw2g54XPkThJ2MJZaqt7_FUHePoCDEPj8bFSC-i3opwvfiKT06OEAOvfZHNldzpbEFsC9NvRYpKn7kxAZBtYaf9okobDJzeHMdeYaIpoqhCvRlmWvKRdEAZp1UmZTkkVfympzlZKvsa94wG2oPIGMhQ0B32gqryko56wUCazYVNdvU7ioYHuBKnkJ8VimVJqMqzbLel0cmvYIIUddJGfYYSZrAdFTRDmeDe7kwBu8UQg1pmEgf-wCJ2XUexw1rhru7J65y2nN9qY6EdIMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا واقعا</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/75660" target="_blank">📅 15:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=SGzdqc7_O1wlo3qQR3c4gR8mEfBzQHuu5bJYEC2GQaACjpuByxPhQI1cceOmLebxl_e8PwuOKr2hkL-zPFts4wX6-ZR-cluu-uFxa1GqvbkQasaLeEmNeX9ks9_3mbDBDieP8BcDbBmts_9Of1g1UhIxqKzTYAHk7H3e-nB0hSk2A_XEV804aEFoYvUtAHg5U-P_B8kHR8WESbsoXiqyvz5wZSLGVgvFfqlzvnt08S3uFPggilu33B-IeAm-kNbKULnRLLEF_ggO0w4tF3WAFc0OOXkbDG-a3xzP_pIOFwDCxSNvPXlbX2IXcX9kT1or3pCiA-c7_syP7rq_q53tDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49046a9f4e.mp4?token=SGzdqc7_O1wlo3qQR3c4gR8mEfBzQHuu5bJYEC2GQaACjpuByxPhQI1cceOmLebxl_e8PwuOKr2hkL-zPFts4wX6-ZR-cluu-uFxa1GqvbkQasaLeEmNeX9ks9_3mbDBDieP8BcDbBmts_9Of1g1UhIxqKzTYAHk7H3e-nB0hSk2A_XEV804aEFoYvUtAHg5U-P_B8kHR8WESbsoXiqyvz5wZSLGVgvFfqlzvnt08S3uFPggilu33B-IeAm-kNbKULnRLLEF_ggO0w4tF3WAFc0OOXkbDG-a3xzP_pIOFwDCxSNvPXlbX2IXcX9kT1or3pCiA-c7_syP7rq_q53tDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ توی توییتر که با هوش مصنوعی یه مجری که مخالفش هستو میندازه توی سطل آشغال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/funhiphop/75659" target="_blank">📅 14:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تنها کلاینتی که تیم فان هیپ هاپ با بیش از ۷ سال فعالیت از لحاظ امنیت تأیید می‌کنه، کلاینت فاطمیون هست. به صورت رسمی از گارد جاویدان  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/75657" target="_blank">📅 14:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این همه پست زدم شرایط رو محیا کردم برا تبلیغ کانفیگ
ولی مهدی تبلیغی نزد
رسانه ی مردمی رو بشناسید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/funhiphop/75656" target="_blank">📅 14:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etM6_8Ud1woBhEUH33gZeQBy5rl9WsDVgUvIG-Yoc5UP5bIjRNk-9EFj_ryzKnYRiujAgPuRZHtCAv-8SS23UcF7P-OVgL76L09gohcE0HYfy90h-e8-0aWkrHTtMfJKPwtFSjxPbm1ZnHh2WQw05FGAf-VAlQYGZvLK25465UN92bnVh2RG8Yqz-LfwY6lmHG5RyU9mpjwU4tzv6EG8hZBFtGDwzMDXXUk_dG7Z6ab8m2xp-JdbBnDNCKeA293MFWsC-oCqZ2l4t9xsdt3p1jcesxwudQwklui32XGESe5KPCqmN-2LdttkryLqMIP5BRkBnKLnvHIosGaACmGg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کلاینتی که تیم فان هیپ هاپ با بیش از ۷ سال فعالیت از لحاظ امنیت تأیید می‌کنه، کلاینت فاطمیون هست.
به صورت رسمی از گارد جاویدان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/funhiphop/75655" target="_blank">📅 14:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان این بحثا برا کساییه که اطلاعات مهمی رو گوشیشون هست و آدم مهمین، شما به کیر هیچکس نیستید به راحتی میتونید از شیر و خورشید استفاده کنید.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75653" target="_blank">📅 14:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این اکانت داشت تبلیغ کلاینت شیر و خورشید رو میکرد  صرف نظر از حرفایی که قبلاً از شیر و خورشید زدیم، خواستم در جریان بزارمتون.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/funhiphop/75651" target="_blank">📅 14:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui7PqB2ALqg-26SqCI08yp-ZW8hN69O4Zpy97WH_GCiBvdw5dCyWM-oJhGz4LkFcwDg_sbpWdBhvrTKShKtkaf6_B8j08XUIOI0dHu1s7bjzAAvK08nTwlR-mAKFG7yqS-5pzaof0l9uCB5mPZoJWrVXtUOLIn7BX5l5AwRupRUTIOYTrPoUQjNJ6LupW3JF-yXoIxvTpmJ2-CO2TfaM0wOQQtmVDa1vHCTioix1PkALVg1GhYLrm__QJ1SELlEjfpuRXrtLiO7VwUz4kkyfTBfOjbN0JWy8NjRqKT0omwbZ_5A3winuwleNrmtsoSFW45sapufqoqJ5Ba64QBvFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اکانت داشت تبلیغ کلاینت شیر و خورشید رو میکرد
صرف نظر از حرفایی که قبلاً از شیر و خورشید زدیم، خواستم در جریان بزارمتون.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/funhiphop/75650" target="_blank">📅 14:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دیدار عاصم منیر با پزشکیبان و قالیباف در تهران   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/funhiphop/75648" target="_blank">📅 14:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75644">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7fzHfLFrF5QpN2mBLgJ1S3k9pAXnEE1xGz4s9sYtWsDjfYsfgm5aFrX55R8EEKbRBJy0gdLMzbGIhiL8-zht8Ka16YiaZ6soikxSO-YAYqHOGXX5H6Sgi7a2untiUM8hD2ZuZCEguznLZpkz9Zyavu5l-KJe955l4SesbNirKFNCpMATsg6Tv5zgwS18YAuEM1XU7YcHLpuF9LsRW5M_r3g1I-w1IrELquksh6rt_FtfHriJaC70UVVQp3RKZy0_MidOLPRsYGgWhyYqI6LZtjrY3RPVSgVJ2uIl5VbzfouWe98P_csJI6C2apGUwj44eLIkjbGgo-L6qB6AXVD9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/krIyaHp_ZX_3ZsnOlU8MUGzRl8OBhP2oT9kvx3d2jpdnFwqH4Nvffie7h_-mN0-MgRNMTZvYez-ZwINlyGXkIVZ4xNbUjK4Iuzy6LRzQbre-E4aOeAlheHOT0mnJf9ljujOpomTMFmVmZxg1H0RhRxp5w-0QkhQrozUWczQ8UEmlJDkAMDCjvkYCFpGS79cYDF2FJzz0aim2hC95Vfji3kAWPRzIBPeUMkwsnCX4yEGWl9dX3mLfxN6zlFhT2yIGlBp7i4HQS_dSX-JU47iYdZQsEopTqWT9lRpUzry2653fahtwDwqibzl-G_BlOaf5HPxitGpjZcFRpaJxG1rhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUmfYEZHSuD4IrGC3zvFkTap9yxlUUpYJ2Egy6zL1mDgku5Bv8Oq_QbCaWpymOUc054pUU3IMbh1ph00PYJwAl0iKH5eb7J2tq6d4ZmizIT2m-O9ezQkx0l0ykcW7UXM2pDygULreV48WdZpsTekIgcpHtuqsTgWBS6AOi3j1SEwAEQ6yAeWQAJq6KBQaUgLCDrFdIUhuDntzCS1bvFBweeFR2a1NyR3QExexaYMn-TzoxVCWYDzn7VzXXnIUe7z4MAiuOr_4YS9q6CtaTSn3sx91zUr7JVbY4r4SVOkUSOoAxoGKai9gKj3OqbfOEq6OQ79BhPJWvIcwnNmpu8ZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EsjwgcDB7twa19NkpeV0gVKRR3vrDAhOeMS54uIdIZyoQWdzudgDjq6XIb3U_gIGkNdVShgbd4rBylHphqzNk7wqW-xfjDd7SPXJQxZsFzrU3TEQPCLWpCPm9uJicrDIdQR7jAgkzan7q--XX9xNn1I1qGRqjcM5FK54C4LH47u2zhJIfg-WGHxNsaD0_oeDWHw8oZxl5JBQOOYPN2MRNeL6xczJo7X71-BOrbvK8CV8JQG_aWI9CZW9XNVV4SDTE5Cy-hGfooX-h-7LbZHwsMlOtP30QlNYFOMCs-TfLYcBnVqtv2RAGRi5FlISnvzBfqZ_vG-ReneXt_ZsblTmDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبر سفر عاصم منیر به ایران تکذیب شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75644" target="_blank">📅 14:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75643">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">العربیه بمب دراپ کرد:  کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران دیدار کند. ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/75643" target="_blank">📅 13:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75642">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6s-xr70H2NywA-1b4xhx4q_EU7c3sygzBz6-yYzlae5fzNnSc0ZlxnpniZDy2qmFTBXDSyQdfXbKETakOZJmWtTjNymK0JgAqDwMxw0mHd0g-g14O-OuTLm-S_9IoyYXRmS7wD1LfNsGcyNFYwAK0FyoC-93WooznHuMuKfpPVxF40Vyyzw8eZfcMBIXJN0P9iY2EGr-i93nsT5F1ba-bXnX5YrkvPofUw-tNw2wk20C6ArsV7QBHiwlu2eColC41FypDehsP4G991Dz8QX81ucTQayFHW8eP6FtsZ-XkkeMGXV4nKtpqz0nNXzv0o5MsdaqHPoYTjeAzeu9e6yKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف از خود نباشه ولی من تو چنین اقلیمی هنوز خودکشی نکردم. 4  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/funhiphop/75642" target="_blank">📅 13:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75640">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_lJsCOHiwfAbQKc07A0S9Y3PDAaV3KMQSBOVlkZQg61z5HVPSBWB8ginoxvB2NJHnK6rseMdGFLDEa5vGv-2GYfzT6BslnYCyzcLC8pCtyY9eZsklLpM7FcqvBE5qd7j0eRKsX7QI8cevKuJmWXlmvkZNqqSWee1neFX8hEnMgGBif05kxu5c9Hi6VMZ2SVUliV_cBzYrd2-VI5CRdi2T2uF-8cmpEgIIvNu6mtPfFsSeZmJPVvv3mQ5vDsDPtR16Vpewvm3VDfYJr9IhtE3SPUGHoypH7gmfF6Ynk1pJXgU_y47b6aDK_d9iSJ0KHPisBW0IsveqjvgwwV4xnffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد بی ادبید
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/75640" target="_blank">📅 12:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75639">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/75639" target="_blank">📅 12:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75638">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9YIv7tyqPkeHioGT4bmXglaepyLuu8NOJOX6_FWReo-RdKU4bYLjLGCPc5lts6UEJDP1mTQHNhEMbsvZ5PeiWc1arAmU0H8FGj_tNWG1leLKAHwNI7p-NZ8S7gykMrHF-Swn6ta8fmZtby7ry99zGn6wV5qtl2jvjfgTFAkFsTSUGf42pr4w-M1_tH3kFmDuip0wXcfTj2H6NRavOLjPm7iF190xYp1v4SiaOBFMuP8s1LxMzmHijUWU4uUz32oGjWowgLLXSAWoq4WcLibKQwnzQVemUiR0gwDmdvehCLNrKkvnjtt_gRoFuxdaox48jTvzR47-70GbAUA_pwe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت
گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی: 5GB | 950T
10GB | 1800T
20GB | 3500T
50GB | 7500T
100GB | 13,000T
📩
خرید و پشتیبانی:
@VeloraSupports</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/75638" target="_blank">📅 12:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75636">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thV3jmHZruesh2hHAmxNY-xVUIMwl1ayjYwfYrc9baba8UAaai9w1S-RHQlVqmoy0L-nIvoOCc0tkkWwRzld-ZJs710U7Y4MKOsEJyGnODCPbmcildKNm1ElFAK09_yrjGqzsZS37XMJZctdi0pGcOTK072_9IkzgI6bmxwQ8TJ931loJtIEg_b1dS_O6DoUZvvijQGzOzWq9m_5CVkotoskPtPvhXdd4Fu6f1vSU5b371T93qGxzvUuM9wEVSQdq0TSfRQSBC7Kx56lk3scK1xOa1kpjbzKmRFcQ60j3O9EOfZVHyIdSFbZrek1jYYOyxMK2Ah9D4HL83oERRTpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز اکانت اتاق جنگ اسرائیل دلقک بازیش گل کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/funhiphop/75636" target="_blank">📅 12:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش رویترز از شکست استراتژیک ترامپ:
سه ماه پس از جنگی که قرار بود در شش هفته با پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر کرده است و قادر به یافتن راه خروجی حفظ آبرو یا گسترش حملات نیست.
با وجود حملات نظامی آمریکا، ایران فرو نپاشیده است؛ کنترل مداوم آن بر تنگه هرمز — که یک پنجم نفت جهان از آن عبور می‌کند — همچنان اهرم اصلی آن است.
تحلیلگران می‌گویند رئیس‌جمهوری که به پیروزی‌های خود می‌بالد اکنون با چالشی روبرو است که می‌تواند جایگاه جهانی آمریکا را بیشتر از هر درگیری در دهه‌های اخیر تضعیف کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75635" target="_blank">📅 12:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سازمان هواپیمایی کشوری با صدور نوتام جدید، محدودیت پروازها و فعالیت فرودگاه‌های غرب کشور را تا صبح دوشنبه اعلام کرد.  @Funhiphop | ALI</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/75633" target="_blank">📅 12:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALKZN3g1fUNRgDHIqOYCV047uW_YZGE_4s86wqE_tYb0Hk-ViCkhzzijLlA0TKEtm81y1Qll4JkMc43E5ngU7_mVNNW0hWcr3PuXS3SuKyEKJ-WRMzYZaELCwN6tjU75iZyd7rDKRbinHt4fLkeMvuOxRaTVOJ5z4qeYSmAmT5Od7VN3FWgYbbJjnOwqJ1F4S9OtGLsPBKGXF85vV6Cpa5bVrkzfBDx3zCu8_KP8lpyn6dO-mRXWbytIGbHaTxzXijPhp9KE01CDBJYKm7LGaf_mNukg8dgryk9iXMLJi3u6-OfY3tX9DUaisscz19nJEjFdKZdWK9dqhbAAEt9W8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو سیناب ازت میخواد که همین الان سهم ناهارتو بهش ببخشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/funhiphop/75632" target="_blank">📅 11:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asSmDEJQUc4QPft1fOpvDJ2pUAW5_S19yQML6KK3LgD9i46mg0jjHdRp8QaUp0k7gL-Bd0lGQm0ro8hi5xsZqH5hM6xlfhFyfGBbu8a7Q-13XZIDA7_A9uNr3ZUsb52JaEMzRhptuBESZ9MaJDukAtX7dwhGWsHWcei047LoDUCSx4vMhl7L3agyfQgL3wj0K5gv1TK-mkXM4vebdfuswupkv25NzTwrLfKmgvxcy5O3VS1WrFoSpuW9wiFOmGlfHHPgpsFaswpJAS5oklH4AMqYzw5ofqk6XCvkhvS-xAJ6mJGRzXGGM-MUixhtz0GkJ0990pSL16cN_rer2XzwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه در جهان یکیست</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/75627" target="_blank">📅 11:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">بخت و اقبالتو گاییدم پسر  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/funhiphop/75626" target="_blank">📅 11:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2XG5FyZyT-wBbpXa2mZ-3kHFb-VPIybUT4-nRlpRp8OGGbIQTtRJDRhzF0emMoBOqPEUuHSg6Px3ltJrHwvEucwjIu_iZOlvacoXgB1T_OVWyfkx_OtW5OAHURM2EAaTll7zxiCl2yWBmobyButUPtGP8_LnhXwETdh_0Tbcn7dgjjXA-f09CWarKRJKDqSmEekGtwAZ-TKCLF1bM36EFfNZRCM47bfh0GX8wOiloeF9Z_KVo0xgvq6q3UODEBXloaNTXvC3iOygWXABrcPEfEs4zZ5lMcFAd4r4CbNT4ZTbbGu27og3SLsHzesnrdYEi9KW-SfeemhcVFVV_ssNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخت و اقبالتو گاییدم پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75625" target="_blank">📅 11:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">غیررسمی: آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی رو رد کرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/75624" target="_blank">📅 10:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75623">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">غیررسمی: آمریکا درخواست ویزای شجاع خلیل‌زاده، مهدی طارمی و احسان حاج‌صفی رو رد کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75623" target="_blank">📅 10:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75622">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سازمان هواپیمایی کشوری با صدور نوتام جدید، محدودیت پروازها و فعالیت فرودگاه‌های غرب کشور را تا صبح دوشنبه اعلام کرد.
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75622" target="_blank">📅 10:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الان رئیس صدا سیما داره فک میکنه چطوری جنگنده وارد استودیو بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75621" target="_blank">📅 10:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoEa09Kdmma6aKfGfgzAinfWKiPl5i0VW9P0kljitvRuwZ7zG5pakHanTGlwPhJG-5zfl9CVVagyr72XguQ_Xwp2SL6WlX04EzidrkBg2GmS_0auWq9Zvx6dPd3D_KTD5gWUpudCZDEHfE-CC7sn7-TTTXKFaqawtEMg4i5gv9tlBRjLDRGZsaYGUgQ51zugdiaUw_60UGWFA35VVvoLykf6TnugRi1cgHpsCpT72NGfm0k4jsZvA2tIOn-Ba3KYm6hxkRIYuqQEHrMxyxGwky5NwOiy5aVDhF832AILnPl4qbtdSmi84DlFG6yVesNBnAw8BMdaqPQveyGVix6_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعریف از خود نباشه تو چنین کشوری هنوز روانی نشدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/75620" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBcSXNHx9Lwn59PINTtT1Drtb42Ex8julhnYXUEYv2XGk_AD0RLPW8bnFL3QSQkNAxZ342qzFyF7LCmgcaC4F2yLx9BPWCt55vmEPL-UUDrTyGFIUtBIumfVRm803XAKhANlb9229aIStWEcoOsI7u8--RjZMkA7tUCBP7UcQr2l-pfxI90rU6FHjqu3Fi_ZTdglG9k2lDD_Zc0kZLejT0caJ4S7N-mPbZWYwNZgcOh6NTDt2CMXD79M081pnN0jvHvzz-upp0-g1sAtwpf6Z_UN6aRupz-M_cAWbhz3Z_yAeLj9qx93ZuLgmo3t2PvMqxg_5EONGbxIGONE2RIX1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه مادری از این دراز بد قواره‌ گاییده شد</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75619" target="_blank">📅 10:13 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75618">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTuCauov5RP-sk33I21Fz8AYqrCiG2aQTxI8_xE2UU_qwo4CxYvOyMa94l1wp2eOk6ZRVGAmYGDj-iidujBTqzioHTpM__qyy7LWnRmc1r97tVnHgrnMp2IMpv2lV8fO1-F0GJwmHtmMNo8Ko6j3Np61uAidJgoEf9t0Pc5iCdz-fe9KfGJMPER48zBZQeyJdoZBmMsD56SYCqWwQ6V7bETsVoqHuTf6CHuOez6m2jbtKwaT1P5qRdSgaqqjTkKbjlC_WpE8bsJAUwEKJfbWvT0aSr2by_o6NzVz6ePB2LtxserNrP0OePUAmR4s-Y47_7hFgeiUGI1mxoGvd2wcHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75618" target="_blank">📅 10:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75615">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سخنگوی وزارت دفاع و پشتیبانی نیروهای مسلح، سردار طلایی‌نیک:
ترامپ چاره‌ای جز پذیرش خواسته‌های مردم ایران و احترام به حقوق کشور ما ندارد.
عدم احترام حقوق ایران منجر به شکست‌های بیشتر برای ترامپ خواهد شد.
در میدان نبرد و دیپلماسی به یک اندازه، برآورده کردن خواسته‌های مردم ایران تنها راه خروج از جنگ سوم تحمیلی بر دشمن آمریکایی صهیونیستی است.
همچنین ترامپ باید با پذیرش پیشنهاد ایرانی، مراقب جلوگیری از خسارات و هزینه‌های بیشتر ناشی از ادامه جنگ باشد، چه برای مردم آمریکا و چه برای جامعه بین‌المللی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/75615" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75612">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb842b6ea.mp4?token=X4VE1f-FpH_sAakpepwRV1O6vywdMAVzYF2UDFH304fFRBy-DRr8SYop5hdJYu-YslCi7y8z6g01fwfwMKq_tBOiDdy2NIqPsgVtSDPKn5NBuzBlD4pPyCGSjhuFSmAj_F46bNbp6FbvghxoDGuMX5mZ6_FBfoFBVvOuHQZodGy-ykUyKjwQLXwCFiJoNt1tQTnEVxlGtLxSdIHAt73Ngh0mLiW1-RyjuJZrwrEZTj0cdapxLfRL9Ly5_NGFAeglbHmQ0YdICGAgDxKTmGt4y40mXb2eNcwQxIX1KuLJWOk3ygCH5xhgnYfnyIvvbnqY5dmI--0PbnDfHbhFBrRQwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb842b6ea.mp4?token=X4VE1f-FpH_sAakpepwRV1O6vywdMAVzYF2UDFH304fFRBy-DRr8SYop5hdJYu-YslCi7y8z6g01fwfwMKq_tBOiDdy2NIqPsgVtSDPKn5NBuzBlD4pPyCGSjhuFSmAj_F46bNbp6FbvghxoDGuMX5mZ6_FBfoFBVvOuHQZodGy-ykUyKjwQLXwCFiJoNt1tQTnEVxlGtLxSdIHAt73Ngh0mLiW1-RyjuJZrwrEZTj0cdapxLfRL9Ly5_NGFAeglbHmQ0YdICGAgDxKTmGt4y40mXb2eNcwQxIX1KuLJWOk3ygCH5xhgnYfnyIvvbnqY5dmI--0PbnDfHbhFBrRQwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دن اسکاوینو، رئیس دفتر کاخ سفید و مشاور قدیمی ترامپ، یه ویدیو از B-2 منتشر کرده.
آخرین باری که اینکار رو کرده بود (ویدیوی دومی) یک روز قبل از حمله‌ی ۹ اسفند بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/funhiphop/75612" target="_blank">📅 05:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75611">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کسکشا نکنه زمینی میخوان حمله بکنن
تا این لحظه، هیچ جنگنده اسرائیلی امشب بر فراز سوریه یا عراق پرواز نکرده است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75611" target="_blank">📅 05:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75610">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=APQr78rBFBZmLfN4ND2JhR1sxgqgWhpYLe7qZzbkCW0nEjAU4Hdzooq732oe8nxeF4bhdpnMLz5jVDdXBUQK4GZ1GA1l2imOpKDDArO1gWxU7Jq6Nt0fK6NuMPWamTKA94bEMiSamwO3XDWP1GGVLG7H7Cso9H27owOQeJn-Ca3A3fcOFtZGWw_7KjFpoC-pVVliOAHCXMk0FLU8i0cLtnUT3yHqF_7iaa1kAYLmW8wv6Iahyd90rE8icLkxCsJNfhJd6LN3DBCrB9qImwNMOaV3s6_LG0DFDqX1WErCtm7AVO72QSGq8oQ5Y1GCSlT-cpAc7Uv29CPRS3d7oQWK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=APQr78rBFBZmLfN4ND2JhR1sxgqgWhpYLe7qZzbkCW0nEjAU4Hdzooq732oe8nxeF4bhdpnMLz5jVDdXBUQK4GZ1GA1l2imOpKDDArO1gWxU7Jq6Nt0fK6NuMPWamTKA94bEMiSamwO3XDWP1GGVLG7H7Cso9H27owOQeJn-Ca3A3fcOFtZGWw_7KjFpoC-pVVliOAHCXMk0FLU8i0cLtnUT3yHqF_7iaa1kAYLmW8wv6Iahyd90rE8icLkxCsJNfhJd6LN3DBCrB9qImwNMOaV3s6_LG0DFDqX1WErCtm7AVO72QSGq8oQ5Y1GCSlT-cpAc7Uv29CPRS3d7oQWK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت قطری ایرانو ترک کرده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/75610" target="_blank">📅 05:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75609">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">هیئت قطری ایرانو ترک کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/75609" target="_blank">📅 05:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75606">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bd9ce2b9.mp4?token=hL0sMhAfJRX_1_mlkbVSxip0QDOyrj-en_xj8qS9ppPCY5e8W59khJYT2cPA-JfaGVfaYpjQy35Z6ctJ7acuP4d2SriHVZ-WFf3lr-VbHONRMKNOtji5mTsbpO4PaqJHse6rq347IU8xdVGVQyOUVzHcS78OhDr7bn6BeVfEHKUZwFRUjDHrIfTv7lV-nMevuM2i85FrjTzOzR86qBQ6tuD7_odM4CjyWJy53o-7lhd0JR0ItNTUTpjrxFJeoefZWl-9IK94x07TgKNjRgUM8rv5mbsi9jFFyXE3Q5ox8VlfG98l1Si1ufNncVaLTW0nEZDFKyufRElqjQIUFVqdEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bd9ce2b9.mp4?token=hL0sMhAfJRX_1_mlkbVSxip0QDOyrj-en_xj8qS9ppPCY5e8W59khJYT2cPA-JfaGVfaYpjQy35Z6ctJ7acuP4d2SriHVZ-WFf3lr-VbHONRMKNOtji5mTsbpO4PaqJHse6rq347IU8xdVGVQyOUVzHcS78OhDr7bn6BeVfEHKUZwFRUjDHrIfTv7lV-nMevuM2i85FrjTzOzR86qBQ6tuD7_odM4CjyWJy53o-7lhd0JR0ItNTUTpjrxFJeoefZWl-9IK94x07TgKNjRgUM8rv5mbsi9jFFyXE3Q5ox8VlfG98l1Si1ufNncVaLTW0nEZDFKyufRElqjQIUFVqdEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75606" target="_blank">📅 04:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75605">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reEr_QHQ_qysTRy4Li6coMFfXQr35nGIO4WQxmn5KcI8GCmhLWkMSMWu7qCaZxBEGJiuUsVa_V-DO6T6ziXB7t1f_LKzvxpgEyZD0e-lUBUP-jp9SIitrn1WOBCNPxtahC_1LZakKCMAgEdRzNhNgXs4KqVVqafAo455ny6APRP67LWbUJ4YH5VRV9YZgfuPSB0xgazQBEQIL5sLz3RX7WPIbOsq_GqDnwO7zMM3CS608n9iAbxYU7oyNGUHOU1aHfQSf_8ONaEqUfc13bUr1Pm_u1ZFEdX-dbhe5USAnUg1m2PdmiLTFc841igDvqM40TI6xZ8ti3uWLoeE9-ucJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست:
ایوانکا ترامپ، دختر ترامپ هدف ترور توسط یک تروریست آموزش‌دیده در سپاه پاسداران انقلاب اسلامی قرار گرفته است، در یک نقشه پیچیده برای انتقام‌گیری از ترامپ به خاطر حذف قاسم سلیمانی.
محمد باقر سعد داوود السعدی، که یک هفته پیش دستگیر شده، قسم خورده بود که ایوانکا را بکشد و حتی نقشه خانه‌اش در فلوریدا را به همراه داشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75605" target="_blank">📅 04:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75604">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سی‌بی‌اس: دولت ترامپ برای دور جدیدی از  حملات علیه ایران اماده شده
چندین عضو ارتش و جامعه اطلاعاتی ایالات متحده برنامه های روز یادبود خود را به دلیل حملات احتمالی لغو کرده اند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/75604" target="_blank">📅 02:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75603">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اسپویل:
این هفته هم نمیزنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/75603" target="_blank">📅 01:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75602">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیوزسیتی پرو:
حریم هوایی بخشی از غرب کشور تا روز دوشنبه بسته شد.
نوتامی که صادر شده یک استثنا داره که اون هم پرواز هواپیماهای روزانه تو روز هست. شب و ممنوع اعلام کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/funhiphop/75602" target="_blank">📅 01:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آخرشم نفهمیدیم لین کُس چجور سیستم عاملیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/funhiphop/75600" target="_blank">📅 01:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اکسیوس یه سر خط خبری دادی، یه جاش گفت مذاکره در حال پیشرفته یجاش گفت قراره جنگ بشه یجاش گفت نشانه هایی برای از سر گرفته شدن جنگ وجود نداره، به راستی که منطقیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/funhiphop/75599" target="_blank">📅 01:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خداوکیلی مهدکودک سر خیابون ما وضعیتش از اپوزوسیونای ایرانی بهتره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/funhiphop/75598" target="_blank">📅 01:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCC6DlrYlxvzsJQHrBe42pk2gAe6-4NAJGJSurP4nGAPG7hYGfm8ToC7dVyCHdB_qxcb3kMYzdEuDae0XZih3V8k2THIubniy58u1ofZj9usy0dL57klgy8eNX3hPFTDivHADNt0GCOhv0gidILqinPGdkiRS3P8bIm7NKfERCjqf_ir5OMPBNSQqXFI-SzOV3q4wX51gYrUbVwm5HCiSgiETPTz22kF5VwUNhSCYjD8cp7fuxBWRvDZ0pI-Fpg6QWn2TVdM2xuGfc_AQtEanCc1HcR-Pg7sF91l1Od52faCU1-eipWDCEiR0YITbL-GxN-nFXO56yyS0traOL2O0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/75596" target="_blank">📅 23:57 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OO7WX6FEvGy3iVPRJKRpEsoN1rZlmIf7vrMGcGsPrOR0c-TMR1mfVbYkBaSf3OyZAUL4FpFDA4hsUmkUfPXvcOluazGQYHUUYxqxsZs0DPr_0P_OJUqDZxu6HXHoNd2xbuowAtPnSZzAZjIVgY114NGghpr4qTLshGN5YaXgcbHBnmUzAA7R_u4A4wODYQjIMWTlR9pJ4WhbIa3b7qQc_teobBbFOakm_87lhsrhXAFSLesrUA7371Z4wzJC4tWd8LNE3rn8uPx1rAUnK8CPnLWXZFTznjZ6CozPEnCI2NwKHc8rpogon2-omUs4XHauuwJZgk_y5LRlwgh-keN4LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط به بنده خدا رضا پهلوی چیکار داشت این
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/75593" target="_blank">📅 23:47 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یادمه پیشرو پست زده بود تو چنلش:
این آخرین نبرده بعد بقیشو خالی گذاشته بود
بعد دید فدایی از شیر و خورشید و پهلوی حمایت کرد
ادیتش زد نوشت پهلوی بر میگرده
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/funhiphop/75592" target="_blank">📅 23:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هر جاویدنام یه شاهنامه شد... نور بر تاریکی پیروز داش رضا!
🤟🏽
👑</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/funhiphop/75591" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بنظرم یا جنگ میشه یا توافق میکنن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/funhiphop/75590" target="_blank">📅 23:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بزنید بعد آزادی، حداقل پیشرو خداحافظی کنه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/funhiphop/75589" target="_blank">📅 23:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSinab</strong></div>
<div class="tg-poll">
<h4>📊 دوست دارید آلبوم‌ها کی بشنوید؟!</h4>
<ul>
<li>✓ بعد آزادی</li>
<li>✓ بره پخش</li>
<li>✓ فعلا صبر....</li>
</ul>
</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/funhiphop/75588" target="_blank">📅 23:14 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">معاون آموزشی دانشگاه علامه طباطبائی: در حال حاضر دانشجویانی که در تهران حضور دارند، می‌توانند از اینترنت این دانشگاه استفاده کنند؛ حتی دانشجویان سایر دانشگاه‌ها نیز در صورت حضور در تهران امکان استفاده از خدمات اینترنتی دانشگاه علامه را دارند.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/funhiphop/75586" target="_blank">📅 23:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
70,00 تومان تخفیف فقط بنرو برامون ارسال کنید
💣
مثلا 1 گیگ میشه 120,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000
❌
120,000 تومان
✨
2G = 380,000
❌
310,000تومان
✨
3G = 540,000
❌
470,000تومان
✨
5G = 850,000
❌
780,000تومان
✨
10G…</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/funhiphop/75585" target="_blank">📅 22:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Mn9pzOFZ52VgHkqxRdx_WzL-M3UBSXAnbHFlF2Pp9rhwySMqsF3_Q7-0TrlGi9W3OY9NuWL_jh7RMlDfFP3BJ4oyjnK0EAAvgo7390NPh17ICjqLfJJ4oLiRplUdIWoGqARZC-bjWTqCHSb4EUJOzGaM88SFeXubOaGjq1cqT4XiKaynZU2ONY_lw3YUuuRRloAMtyJDqGoCor4sLDHf7uEUrk3fwaiNlD2Zu7ZFcAs0UmWdZL3_AU3OAZjKKTHIDdjhEwpZlpvkZAmW8gbFNIbgwwFtbIX9uGk649_lcmL_uVCt2KsH66TrRTQsJlJy9u_qNs5Ck1WLrCQMtb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔮
اینترنت آزاد با «ملوان زبل»
📦
تخفیف 24 ساعته
📦
70,00 تومان تخفیف فقط بنرو برامون ارسال کنید
💣
مثلا 1 گیگ میشه 120,000 تومان
😐
🔥
پلن ویژه:
✨
1G = 190,000
❌
120,000 تومان
✨
2G = 380,000
❌
310,000تومان
✨
3G = 540,000
❌
470,000تومان
✨
5G = 850,000
❌
780,000تومان
✨
10G = 1,600,000
❌
1,530,00تومان
☄️
تمام سرویس ها با ساب تقدیمتون میشه
☄️
⭐️
‌تا 100G هم موجوده
⭐️
کاربر و زمان نامحدود است
🌕
✅
تحویل سریع
✅
پشتیبانی
✅
مناسب آیفون و اندروید
⭐️
. فروش همکاری هم داریم
⭐️
🔴
برای دریافت این تخفیف حتما این بنر رو برای ما ارسال کنید تا از تخفیف بهره مند شوید
🔴
✍️
برای خرید پیام بده
🚀
«ملوان زبل»؛
@MalavanZ_SUPPORT
چنل
🦠
@MalavanVpn</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/75584" target="_blank">📅 22:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس:  یه مقام آمریکایی، مذاکرات رو به‌شدت «طاقت‌فرسا» توصیف کرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/75583" target="_blank">📅 22:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اکسیوس:
یه مقام آمریکایی، مذاکرات رو به‌شدت «طاقت‌فرسا» توصیف کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/75582" target="_blank">📅 22:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjpJdCh-P-QEn1M1En32E4aLI_P_9DLexMMYLl0VKZ2yeHV453uLvS885L_oikpipI7qzugy2nzKDESaeZtfp5Ke0K4Zb_MqVCqqEGgOb4o8BjmFaGvjLVglYPybAzI8anq3V3GeaP4LVBnwfQ0revh9qcFiUqESUCleA7MhupjYS2Rlt6o4UYNyNA2Xu5y0s-x6CPL_gdMTwAYuUdjHvJuAMOXEzrn4MG8JD1AX_WMcmxKsCmNfrRB8u2URAz_jE5Vbz_LM5wc9Yc1g8dOOYULDUr_MQyRCX8ytNbn-xm59av6meTvRCIKfDVlIx_24qbcPWyPYyEMehnNipJeH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد حضرت آقا تو یه کشور دیگ رویت شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/funhiphop/75581" target="_blank">📅 21:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ:
مهریه عروس خیلی زیاد بود‌ برای همین به نشانه اعتراض در مراسم شرکت نمیکنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/75580" target="_blank">📅 21:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75575">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ بازدید برنامه‌ریزی‌شده خود از باشگاه گلف ملی ترامپ نیوجرسی را لغو کرده و طبق برنامه به‌روزشده‌اش، در اقدامی غیر معمول در تمام مدت تعطیلات آخر هفته در کاخ سفید خواهد ماند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/75575" target="_blank">📅 21:23 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75574">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دکتر بگقایی در ادامه: اختلاف‌نظرها بین ایران و آمریکا آن‌قدر عمیق و زیاد است که نمی‌شود گفت با چندبار رفت‌وآمد یا مذاکرات ظرف چند هفته ما باید حتماً به نتیجه برسیم. تمرکز این مذاکرات بر خاتمهٔ جنگ است و در این مرحله قرار نیست راجع‌‌ به مباحث مرتبط با موضوعات…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75574" target="_blank">📅 21:16 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75573">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ تو تروث سوشال: من تو عروسی پسرم شرکت نخواهم کرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/75573" target="_blank">📅 21:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75572">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رهبری جمهوری‌خواهان مجلس نمایندگان آمریکا رای‌گیری درباره محدود کردن اختیارات جنگی پرزیدنت ترامپ در قبال رژیم ایران را لغو کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/75572" target="_blank">📅 21:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75571">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اورشلیم پست:
تهران در فکر یک حمله غافلگیرانه به اسراییل و کشورهای حاشیه خلیج فارس است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/funhiphop/75571" target="_blank">📅 21:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75570">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دکتر اسماعیل بقایی، سخنگوی وزارت خارجه: نمی‌توانیم بگوییم ضرورتا به جایی رسیده‌ایم که توافق نزدیک است. تمرکز مذاکرات بر خاتمه جنگ است. یک هیئتی از قطر درحال مذاکره با وزیر خارجه کشورمان هستند اما میانجی مذاکرات همچنان طرف پاکستانی است. سفر عاصم منیر به تهران…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75570" target="_blank">📅 20:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75569">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دکتر اسماعیل بقایی، سخنگوی وزارت خارجه:
نمی‌توانیم بگوییم ضرورتا به جایی رسیده‌ایم که توافق نزدیک است.
تمرکز مذاکرات بر خاتمه جنگ است.
یک هیئتی از قطر درحال مذاکره با وزیر خارجه کشورمان هستند اما میانجی مذاکرات همچنان طرف پاکستانی است.
سفر عاصم منیر به تهران و این رفت و امدها علی رغم اینکه پرترافیک تر شده، تداوم همان روند دیپلماتیک سابق است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/funhiphop/75569" target="_blank">📅 20:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75568">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ تو تروث سوشال: من تو عروسی پسرم شرکت نخواهم کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/75568" target="_blank">📅 20:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75567">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تو ترکیه اردوغان یه رقیب داره، ۱۵ بار نامزد شده و هر ۱۵ بار شکست خورده جلوش، الان این دوره باز اومده نامزد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75567" target="_blank">📅 20:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75566">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzEzJOpoEwqwRydyGLJc2EJWB4xdHDUeI3AU-_IkJ7SmoAaoWevc1dwEJPI1v4u37G60hC1OZQTzVt7yOjlfZBRlekfi5ej1yUPXhVMWGHhCwm-b6XB9h6ypazLl0MqrY2hq0zyx-QNE9J6n5xz4_2hFpO8klL01ATuKIoBY16Ys5upLcYmhjn3ouzJ3cPgY78Mc0XBKNmQLdZ_IF6EQUHytAxssXgq5wbWyEWj3Ahdp5O7UQAt_IJFONAPIwhA61xpP5qQlYKU_gLsEQtPhu3CWNY-r1Lq3XR5b6tj00ikfGXB0uV6ybdIflpbdY6luSuYg0n9ZOK4S580JTLxZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر سفر عاصم منیر به ایران تکذیب شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/75566" target="_blank">📅 20:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75564">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ: ایران مشتاق است که به توافق برسد.
ما به شدت به آنها ضربه زدیم. چاره‌ای نداشتیم چون ایران نمی‌تواند سلاح هسته‌ای داشته باشد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/75564" target="_blank">📅 19:37 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75562">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN7_azQ6ie14gINQOT2sGtaaabzOHMfxfHctOzY7UJ-KR__bXSTgfZf4uZv3_MiqnHT8_g7lQ-rbNlAqeMBPWsZggGqcFYWFZEcGyci0NxTJxXlseUcyYuc-qKQSE5MFtQlAIPHrHHeToZZtcsuwQiBJ5zntsRegerRCaZGdnn8blILdVucJ2mit0YC7vlTJSG8ckMZOC5f-K0TQDLwDdcZHknwxeryQl_j3sn_PRxkYMEkTd-tNfbpGCdjcOYIpWvQMjNJXyGtQMClP_tcByIwBZz1xFSF7cztCdYtr-lb-jpdcyys3iGiv1KV_dFTn6uifh9lvvnuZsYXmqz9ppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/75562" target="_blank">📅 18:41 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75561">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خبر سفر عاصم منیر به ایران تکذیب شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/funhiphop/75561" target="_blank">📅 18:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75560">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">برنا رو ادمین کنم؟</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/75560" target="_blank">📅 17:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75559">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e5cb903d7.mp4?token=kr-7NvT2c4BvGCUKldxK5KPGohtSC5nwfmjz2fwoYSvuqZsd4mKqwJnRDJtPhFnZlKW5YooZmZvAw-aCnJqxbBs6nqiNNy4zoIIc528yvWlrfKf06Z0OKWWA8d3LsG1iSBzmZEck66i72AgcQOs7VNrtmWMu3gtzhkGmHqg0dKJPDMMC4jh8IuCg1705QxktK8z1JrnGphkVMpRLmvaHyBtbztwQZsy9wZwut2a90_fOdYbHzh57-qulOMdFyXZkAOEMWARcUrOVUehFXvwB2hcEFxcgajOE43el2bNH3hkBZsQKJlPTJRTzHo81jM3le4SgllErmU6sZctGe4kPow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e5cb903d7.mp4?token=kr-7NvT2c4BvGCUKldxK5KPGohtSC5nwfmjz2fwoYSvuqZsd4mKqwJnRDJtPhFnZlKW5YooZmZvAw-aCnJqxbBs6nqiNNy4zoIIc528yvWlrfKf06Z0OKWWA8d3LsG1iSBzmZEck66i72AgcQOs7VNrtmWMu3gtzhkGmHqg0dKJPDMMC4jh8IuCg1705QxktK8z1JrnGphkVMpRLmvaHyBtbztwQZsy9wZwut2a90_fOdYbHzh57-qulOMdFyXZkAOEMWARcUrOVUehFXvwB2hcEFxcgajOE43el2bNH3hkBZsQKJlPTJRTzHo81jM3le4SgllErmU6sZctGe4kPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/75559" target="_blank">📅 17:56 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75558">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ادعای منبع نزدیک به العربی الجدید:
سفر فرمانده ارتش پاکستان، عاصم منیر، به تهران به این معنا نیست که توافق در دسترس است
گزارش‌ها درباره وجود پیش‌نویس احتمالی توافق صحت ندارد و اینها صرفاً گمانه‌زنی‌های رسانه‌ای است
وزیر کشور پاکستان پیام جدیدی از آمریکا به ایران منتقل نکرده است
سفر مقامات پاکستانی به تهران در راستای تقویت میانجی‌گری اسلام‌آباد و نقش آن و تمایلش برای جلوگیری از تنش‌زایی است
تهران همچنان خواسته‌های آمریکا را افراطی و غیرمنطقی می‌داند و معتقد است مشکل در واشنگتن است، نه تهران
@Funhiphop
| ALI</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/funhiphop/75558" target="_blank">📅 17:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeqEDgA5XogkZI1prLZ3KNwFK_z4Q97FKZ52boBZotfZMueXEAcZ6dvuEe79o3cBQtf3h7HkzsjFSskQJ0fRPc1gIcpnU2FT_rf94oMgAdLUc_D4XGrEP2dTBa81cCKxqGQvs11xD-IdIa5QulUPXixNPQXT0pjVmPgnvUnkG9HWDnPkiMQdKQbaSLXS7fNmwaihIJmNXz9vpiQrSg4-CwGTtk4L-_2jQu_z9gzO9vBpwLHfD9_4EOTuvbFfKsItcQspkZMWMATbMJY1HBGlA0QxcRZCv9Jbc-GrNNzP7wL5WNv3iH-b0kBma5ACCcvPpJ81DYDkA7FCYLp-TPwjDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیموتی کصکش زیدت کایلی جنره بعد هر شب میری بسکتبال میبینی؟
کونی تو اصلا نباید از خونه بیرون بری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/funhiphop/75556" target="_blank">📅 16:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75555">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsMOPY5KkW1ksNocIcW1yZOGYsgf2DHdNt9VMIQG6mwuSopkfzYB7ErUUHehUDk4J67Jhv3sv1esY0yTSAOeXqpntaFPWqiHjcB01joIkdUI5BKMIKiNCb5A4EjImmCOwpVhk3AJH-bqrWLgdpIUcD8MWoLu8NxHwalzRg1xvF1Bkh2HZsThA1itxTVljdkHpJuNAtpyhdz28eI5C9ja5orC2NY2TD4j-tqv6bZnOfDXWH7esdw8zpqI8z-C_PHsVmS_RnCPQke_b7BrA3Pbr8wh03YOkfvObcl4inaUfj-2gjhLAcexCfG_xBcfsXd0XMVw2EOJwCB8NK4R1mnZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاصم منیر که امروز نیومد تهران (العربیه گفت سفرش رو یهویی لغو کرده) نکنه تو این مدتی که نبودم توافق شده من هنوز داغم نمی‌فهمم؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/funhiphop/75555" target="_blank">📅 16:00 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75554">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggPrBOVFD2c1DOajDg9hQSJaaYTHV9SmgDl1FSBKE7YmG_PbiOB7nNB-KCNei9083onVmIpn9VZ_niKOAJb-bCwKJ3QRaMpzNDhSXmzBadOPrgT9H4HVCBHwR8ctY7V-UEhZOt8BsmAiilJ3bED1hHd7ElnWB-CQ8ljcStC-q-idgGDQYepcdLwTYDTvqvXKzepFupNUk4KHEFqxquFvrZHQg9Z0lDIDAAZBfVTEOHkH-KI2nTH_iUzOUc2foc2xnYtBmb8oCzxG5XAvwXHb9wOcDhfX_jZDSdRDTyvWWWn_gRPgxwQZc7f2pKR1oZl3rm9nnbQC8yTkzzSAJLyGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا یا کلا برید یا برنامه کیریتونو درست ادامه بدید، ماهی یبار خداحافظی میکنید، ابی هم انقدر خداحافظی نکرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/75554" target="_blank">📅 15:53 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75553">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">والا من هرچی لیست تیم ملی انگلیسو نگا میکنم تیم خوبیو جمع کرده، این بازیکنایی که دعوت نکرده فقط اسم داشتن وگرنه بازیکنایی که جاشون دعوت شدن سال بهتری داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/75553" target="_blank">📅 15:29 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75552">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FanM42cWcKSzPVDGPn7AkBoxPed6cpYBRrnQ81RlVVGda-fp5wqLHDNgQZP6pU5DhdVG6OaUopfvStOJmbdzCh6NE5ip5WFhpHEeVdgn-wyHDBpJuylhFV7X5JBX6tb_zWFKTEwciC221U2QWJEziNEMHYmghhVH2hfuwwOxmvl6P0biVrLKD91pIGQd_sbPfeqG1Q2hLBHrPeYHeESO_pvO97bYmcMoCX_DDxmyyrT9PYEgopnny6gX1k8ZrFAYEPg6mvEJPDczr_AcVmibaRB1BwpDNUT0-dpjfJxeitbqQv0ulWCNAplY-fuFGGOxZfczr3JAYI85e-gOyiJnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیمای ملی:
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/75552" target="_blank">📅 15:12 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75551">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آمریکا دید استقلال داره قهرمان لیگ میشه برا همین حمله کرد که باز حق به حقدار نرسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/75551" target="_blank">📅 15:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75550">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">میدونم بکیرتونه ولی با اعلام سازمان لیگ، لیگ برتر ایران نیمه تموم و بدون قهرمان به پایان رسید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/75550" target="_blank">📅 14:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75549">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آتش بس ۴۵ روزه امروز رسماً تموم میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/funhiphop/75549" target="_blank">📅 14:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75548">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">آتش بس ۴۵ روزه امروز رسماً تموم میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/75548" target="_blank">📅 14:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75547">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">العربیه: پاکستان روی میانجی گری چین حساب باز کرده که دیل آمریکا ایران و با کمکش ببنده شاید این چند روزی شهباز شریف بره چین یه صحبتایی با همتای چینی خودش داشته باشه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/75547" target="_blank">📅 13:44 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
