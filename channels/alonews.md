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
<img src="https://cdn4.telesco.pe/file/jps70UmWBNGMv3gYiRllI7lmTGF_g0G669pexvfo9sPdIjwm0PpMRWG0EEBskWPK1zOyTaCcsCqutzErXhSZG1tKL46R0UoaXU1KUYZbFgsBSSSX_iPVxLlPvBZ-lu_XU4m5PBNU0oCsoSluMVju3_ou30nSehIjkQg3xjfE2lijmsiXAUMpsWP-IUn563-xt9VP_k8ZBLVkljaiQKe-SFQ6EDx1we89A160IEYzIEk1juyNieCvhlyPWbje4uENF5TYUis9WTLaskE5UMGbgTO_IQ2d0ZbB6ZPgYLKD1ZnSl1an71qZwz0SZ8uEDeBDgXA1go2OiC4OQ8-5llq9VA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 955K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 10:41:44</div>
<hr>

<div class="tg-post" id="msg-145118">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت امور خارجه پاکستان: ما نسبت به بازگشت آمریکا و ایران به میز مذاکره خوش‌بین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/145118" target="_blank">📅 10:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145117">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8lWQsRQkZGGVD3d4FztfhRuwKCj-gqJQtou2kHt-95j5lvYEV-SoV_kgXaJR4-a94ob4dp5ukvHjuOl73Tw9K-6UT6s17TNSAAGcOXyTQ0jEOUA5gPN8IzQQrsXBBMTfyLBSyt3y5iIB8vqkfGEsd1mkW1cYKjGhZ9KvUMCBtZHWNriWQNjBehujB9Je00bgirCg4Ui3tlmzXxaxhYf3vRdvGRF3lkVGzMtJh8xkzVQ-ljjSxK5omiEZG5AVMV2n8_rlKVe9YOyEFvdx8hftbN1GoImRt5EG9cB6VDS4RmC5jlJCtJ1sOWMdwRc4OAVzWLDxJ0nYM_hr_jgwy9U6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرعشی؛ دبیرکل حزب کارگزاران سازندگی:
قالیباف میخواست بره چین ولی راهش ندادن. گفتن اول این ۴ شرط رو اجرا کن بعدا بیا.
۱. تنگه هرمز رو باز کن.
۲. هیچ عوارضی از کشتی ها نگیر.
۳. مشکلاتت رو با عربستان حل کن.
۴. با آمریکا توافق کن.
🔴
گفتن تا اینا رو انجام ندادی این طرفا نیا. دیگه خوددانی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/145117" target="_blank">📅 10:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145116">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ارتش اسرائیل: در ساعات آینده حملات بزرگی به حزب الله در لبنان انجام خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/alonews/145116" target="_blank">📅 10:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145115">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
#بمب‌اتم     این ادعا که تو کانال های تلگرامی راجع به بمب اتم میگن مزخرفه. امریکا از بمب اتم استفاده نمیکنه، مگر در شرایطی که همه کشورها با هم درگیر و وارد جنگ بشن!  تنها رییس جمهور امریکا که از بمب اتم استفاده کرد “ترومن” بود.  هیچ تحصیلات دانشگاهی نداشت!…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/145115" target="_blank">📅 10:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87c5dd8a3.mp4?token=kJpP7Uvr3nj-_cZ9prYqWajP0UGjhUSxx8k_-2_gBUMtnLPTwlg1mwjdFc87c1CdmSeVaEe9oWCDoU39aKEmxmd67zuh25v0NMZ_A45c0mDnzPCLMk0spOFVAElM6i6KD6crVewKOdojwenaK1sHGBIHlzFYngvNCzcowfiDnDbZJxxWsax8Gz1zOB0U0q70nbJ58bMPEdl2JdC60Q_8Ky5draPdAG9PzlZdB-QxkjliN18l1T5iteMHxvATXda8q7VTxynvxNYFvTths4vIahlbzz_yd2YXsVuLoXlmGOkk7SdDDl6FQJWl58jZDV6kATm5vdqw6wHPgEm1xNnT2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87c5dd8a3.mp4?token=kJpP7Uvr3nj-_cZ9prYqWajP0UGjhUSxx8k_-2_gBUMtnLPTwlg1mwjdFc87c1CdmSeVaEe9oWCDoU39aKEmxmd67zuh25v0NMZ_A45c0mDnzPCLMk0spOFVAElM6i6KD6crVewKOdojwenaK1sHGBIHlzFYngvNCzcowfiDnDbZJxxWsax8Gz1zOB0U0q70nbJ58bMPEdl2JdC60Q_8Ky5draPdAG9PzlZdB-QxkjliN18l1T5iteMHxvATXda8q7VTxynvxNYFvTths4vIahlbzz_yd2YXsVuLoXlmGOkk7SdDDl6FQJWl58jZDV6kATm5vdqw6wHPgEm1xNnT2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسننت، وزیر خزانه‌داری:
بقیه جهان می‌خواهند بیشتر شبیه ما باشند.
🔴
ما اقتصاد بزرگی داریم و در حال شتاب گرفتن و فاصله گرفتن از بقیه جهان هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/145114" target="_blank">📅 10:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزارت خارجه قطر : ما بر ضرورت توقف فوری و کامل تمامی عملیات نظامی و حملاتی که امنیت و ثبات منطقه را تهدید می‌کنند، تاکید می‌کنیم.
🔴
ما خواستار بازگشت جدی به مسیر گفتگو و مذاکره و پایبندی به توافقاتی هستیم که از طریق تلاش‌های دیپلماتیک به دست آمده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/145113" target="_blank">📅 10:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رویترز، با استناد به داده‌های کپلر: ترافیک کشتیرانی از طریق تنگه هرمز همچنان کم‌تر از میانگین ۱۰ روزه است
🔴
دیروز چهار کشتی باری از تنگه هرمز عبور کردند که نسبت به ۱۰ کشتی روز قبل از آن کاهش یافته و کم‌تر از میانگین ۱۰ روزه ۱۳ کشتی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/145112" target="_blank">📅 10:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMKXOvAFhMycvyXDcmr2CFvQ-P545-qP5-HWIsFdy4aANSmfTXblH2m2o6IShq7YpjfDtlq6ON7993hJ-nhQXr5mM3mDwifhKHRrPwNd_oqwevSJvRfV_Tb-X60i0KgbAKon375ZClLqfB-jAELL68CNwcknHpKkC-qeLSnCHprZYhB0oxBcrQMTLx-HppjlOTHnQy5wZgGlSaNRrSirZwdFtVEuGF096W-jawDDV_BFvfNfmK6ohz7fF1XDEQEqHpMJr2ZwQWCugAJYfmCU99xooBiJlD2tr-L7_p804XiIHAbFZeO-6j4wOdV98Kof-WAm7xaBPwCn_LmLsD1JAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مناطقی که توسط سپاه پس از حمله آمریکا مورد هدف قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/145111" target="_blank">📅 09:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_ctH_0w7feQl7Ifzb9A8ZdRHSLHS20UyDSLSQHYIXnG9tEc_hditjLkjnrhycRzZ-4WoLZ1496qCtzCghx8zT0ahZgwauJcu9BlfNBWXealZeKKLDs5Ygh8lxrEzSfGII5NPU1CnjR8Oqm1CazTx-kUeqbwzfT6GYxf6clB5ZeGjOgnBDmJ3uPocSDbIIc_FeYWlWrf5IK-j6ht8SiNI3Znh1sTqz4jcn3qgtioiXP6C7vBjSXIUNjijzf7wrsraqjPp-J2A0OQt0aUps0TpF8s7LTvumgo9tRN-U55Sa07BlBKf2r7g2whtIx3cIh-49APZX-HQWa9nbDcec0m6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت‌های نظامی گسترده آمریکا در نزدیکی تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/145110" target="_blank">📅 09:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
صادرات نفت عراق و کویت نسبت به قبل از جنگ ۳۶ درصد، قطر ۴۸ درصد و عربستان ۴۸ درصد کاهش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/145109" target="_blank">📅 09:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
آکسیوس به نقل از مقام‌های آمریکایی: روز سه‌شنبه ایالات متحده دو نفتکش متعلق به ایران را هدف قرار داد
🔴
این اقدام بخشی از سیاست جدید «نفتکش در برابر نفتکش» است که ترامپ برای بازدارندگی حملات تهران به نفتکش‌های عبوری از تنگه هرمز، تصویب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/145108" target="_blank">📅 09:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
آژانس بین‌المللی انرژی اتمی مدعی وجود یک سایت هسته‌ای اعلام نشده در سوریه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/145107" target="_blank">📅 09:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: یک سوپر نفتکش عربستانی با ۲ میلیون بشکه نفت در تنگه هرمز مورد هدف قرار گرفت
🔴
قفل تنگه هرمز دست نیروهای مسلح کشور است و تا آمریکا به قانون جدید ایران تمکین نکنند، تنگه بازشدنی نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/145106" target="_blank">📅 09:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1o77ecc158wO3-BXx6M0VimbmsClA8qHiWpOxu_AehTCaJO8BHQyCMPCsi-riDr1S25ykqOUrc_re72Ul4dg8JITarkfOSX8-5bokempamP8pB6bfPUfEUCLvdW6JG5Smg5CFvRb0DEodn6FEMSd7SRmYqahbtEPYTCF8DYdyzjQ2SJRTlWnK9Hpn5ab9TjZrCGB0G4z6ZK2aQ79gbZhrLdIMT2NYlUMvad94W8FICKTjeGeSYayrofO9myKd-2F23VJT2kOgA5bc8bM3_rfH1efQyMSEnxXbWbsUayNFTKvQFtEivQ3Q6bpZRW24jxE3-K2sIa_CLFN0fkobgEPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: من اصلاً دنبال این نیستم که ایران رو مجبور کنم بیاد پای میز مذاکره.
🔴
برخلاف چیزی که ABC فیک‌نیوز گفته و اصلاً برام مهم نیست که بخوان یه توافق بی‌ارزش امضا کنن یا نه.
🔴
من شرایط الانمون رو خیلی بیشتر دوست دارم تقریباً کنترل کامل تنگه هرمز دست ماست و اقتصاد ایران هم داره کاملاً فرو میپاشه. اونا فقط دارن اتفاق اجتناب‌ناپذیر رو عقب می‌ندازن.
🔴
واقعاً مردم ایران کِی می‌خوان بلند شن و بجنگن؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/145105" target="_blank">📅 09:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
تانکرترکرز گزارش داده صادرات نفت عراق و کویت نسبت به پیش از جنگ حدود ۳۶ درصد کاهش یافته است.
🔴
براساس این گزارش، افت صادرات نفت قطر و عربستان نیز هرکدام به حدود ۴۸ درصد رسیده است.
🔴
این کاهش‌ها نشان می‌دهد اختلال در مسیرهای انرژی منطقه، فقط ایران را تحت تأثیر قرار نداده و صادرات نفت سایر کشورهای خلیج فارس نیز با فشار جدی روبه‌رو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/145104" target="_blank">📅 09:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: نمی‌خواهم ایران را به میز مذاکره بیاورم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145103" target="_blank">📅 09:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
عضو کمیسیون صنایع غذایی اتاق ایران:
محاصره دریایی تبعات اقتصادی و اجتماعی دارد و هرچند کالاهای اساسی کم نمی آورند، نگرانی اصلی از وضعیت انرژی است و دیگر زمان از دست دادن نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/145102" target="_blank">📅 09:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK53G9SVEPYhC1ynUgwaN1jjWKPpLl68wnr83XLJh7qAsZzANBOPHDATtCpD9Nu-Ye10-P7ley2V5iAPCXxcNVzwBjzL-N6B4hhRnop6wBnZU8eAADU_tRJgoAfXev1g9sutG5G2w8ERMW4rfleb8O9eI4tBquyix5EHb8osGynPesDKl2vLkhceqYSwAfFJjHAZJ0HY-wFxc09jTSEfsahG_SEnDO2_2kv5N_Oq_XuNLM4AaFyPa3jBlKXkhArtLlHIKREsrybyd82ieXooabvQIgU8kMaPDJd03DljPvrwv7IHcYgjjwHo4gTNmKU5Z5ny9zRNe3OJTs7MQG26AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۲۰ مقام ارشد نظامی آمریکایی در طول دوره تصدی پیت هگست (وزیر جنگ آمریکا)، استعفا داده‌ یا اخراج شده‌اند.
🔴
یک مقام آمریکایی: "هگست تعداد بیشتری از ژنرال‌های آمریکایی را نسبت به ژنرال‌های ایرانی کنار گذاشه است"
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/145101" target="_blank">📅 08:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0559400749.mp4?token=jgce8OKx0u13GFdm-y3SVxFQDRjvmrqSbQH2wB6U_9O_kmHmEYSV4eDDr31gBq3xdjdmcwHBP1wFl8mqoatLHTZyB4LI0cZHWyflA7KP0d9P1hn-ir4QEOI1Ff19TfAt3LBNXS0rrlTf3JW-k6aWpasli1QPeqvGXJAuSLPDL7WoQ4878wNA_e3HsFm0pZJrGPCnm0vNN9r_kZdJfYYro1jy01xByVrPyhzSuFDI2bf0LI2t-4si9mUSVBQJc-Iw7sGaaLssdvqcK5JSgllteiY2vV-_SK2p_QMoG30jfq8VxMj6IXUBK-0uidKTfrUfGmU2OoQSdxmsEbml1SAZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0559400749.mp4?token=jgce8OKx0u13GFdm-y3SVxFQDRjvmrqSbQH2wB6U_9O_kmHmEYSV4eDDr31gBq3xdjdmcwHBP1wFl8mqoatLHTZyB4LI0cZHWyflA7KP0d9P1hn-ir4QEOI1Ff19TfAt3LBNXS0rrlTf3JW-k6aWpasli1QPeqvGXJAuSLPDL7WoQ4878wNA_e3HsFm0pZJrGPCnm0vNN9r_kZdJfYYro1jy01xByVrPyhzSuFDI2bf0LI2t-4si9mUSVBQJc-Iw7sGaaLssdvqcK5JSgllteiY2vV-_SK2p_QMoG30jfq8VxMj6IXUBK-0uidKTfrUfGmU2OoQSdxmsEbml1SAZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله اسرائیل به شهرک المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/145100" target="_blank">📅 08:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آکسیوس: ترامپ دستور حمله به نفتکش‌های ایرانی را صادر کرده است
🔴
آکسیوس به نقل از مقام‌های آمریکایی مدعی شد ارتش آمریکا روز سه‌شنبه دو نفتکش ایرانی را در نزدیکی سواحل ایران هدف قرار داده است؛ نفتکش‌هایی که به گفته این رسانه، در شمال خط محاصره دریایی آمریکا لنگر انداخته بودند.
🔴
براساس این گزارش، پهپادهای آمریکایی با موشک موتورخانه این دو نفتکش را هدف قرار داده‌اند و این نخستین بار است که واشنگتن در اقدامی تلافی‌جویانه، نفتکش‌های ایرانی را مستقیماً هدف قرار می‌دهد.
🔴
یک مقام آمریکایی این رویکرد را بخشی از سیاست جدید دولت ترامپ با عنوان «نفتکش در برابر نفتکش» توصیف کرده؛ سیاستی که هدف آن افزایش فشار و بازدارندگی در برابر حملات به کشتی‌های عبوری از تنگه هرمز عنوان شده است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/145099" target="_blank">📅 08:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TT08lOgr9fOF9lEw2ajxbht0ESjQDySe8FgKkhFpTlw5QoWIYyXQYB-E5ujXPPNqcHlyy1-SDP8g2MY-HcTHhu3nw-bd1MR_QIArh_eCUSUZAnqVX1pOTRquLoU6XWsCbxOVhb2gBvP5sBJXtlxyarSHsMaVA-S-nj0RQc-2OLMNIxoE9zV94uBMKz4CoNxRJTYPcUsoRAMpzMw10EDBx7KYYB_KCNQCWag3qXsfxaU5tcmYEjZo-HP2gZH4-XodbJFozwv1KW4XKGpX4tElOCQHn1NH59_58W4BmhNJNoFTvqATFg1bPT_NaIoBWpSNs4kGr_cWiRrFUtcbEDWA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / الجزیره: ارتش اسرائیل اعلام کرد در پی ورود احتمالی چند پهپاد به منطقه ی«کفار یوفال»، آژیرهای خطر به صدا درآمدند و تحقیقات درخصوص جزئیات این حادثه درحال انجام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/145098" target="_blank">📅 08:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuTsWyu6ax2W4HmHtvSFbaMUrXkGKIUDxvKJmP415X-7JBvcHZj6MZY_PWbzu5rkDJ_XoSvw9nJw4MrBPpYek8JaabMHEnaF7m3GN98K1YhKce_3arh3D5yVpj-VkxoRvs318GIIs28vIZGyWh7e6roVLVUNQggfzLo_ohemXITMyzfoSzEROomQ_Pu9sjCYU1T5VU8izDTqeWYvMBOtIYByYxFtWKtcK7kEmjsW0Eiap8tn1v_6AizAk-FF8E7-CTeHnaryw7GGJVA1Kw3bfPJRZ7vO3XUyL7Q3JOzH0_78SPIb39fc2sAEzz4xK9QCvTI4LNXw51i_183feYXQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/145097" target="_blank">📅 08:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj-Zmm57zOFpqGu2cKx1lVRHqrIb5AEudW1j0Miy-crkupc58DSwpiZuV_wKoTkE0yOZacI6SAlE2-YL0s5dIgAn0wUB3kOGjBMVYIUtBfGQfUCwdPV-2VMeT9Ou72wFKXvXLkoequXshO5IXxe6uJzrvGAsLUKGOn-E9N2LvYjvvOjGVUt2zs0A6v83uAeNZ4t5jMLsIPui_8kr-iPK1YRBUBJ_yvmZPoazCUx3wL4MqPgFj8UR63ZUuPW22q7AoL_e5mh8J52NGoKmw0tNMbXXBxdJt6-Zp6JsbkeMVdfjFXg5cavrr2lbHc8ghJGQ4DJXZWSk7POwc7wdUWxtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت نفت برنت ساعتی قبل از ۹۶ دلار هم عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/145096" target="_blank">📅 08:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
فرانسه رئیس دوره‌ای شورای امنیت سازمان ملل: موضوع هسته‌ای ایران و تعهداتش محور اصلی بحث‌ها درباره ایران در این ماه خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/145095" target="_blank">📅 08:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_-Z8NmD9iZyF1z-4jjEXhA4mWrSpAFmUj9sUXuTxvV2_1h-xEZXzT3C_lhoVcsw2OYNxUxoMKcE8lrWB4NG7nuqToCGnQTFA9iyIWXGpZpwBOWgaPgsJrcC6-RDLeAxRzmAYW9S2Ua7WuGcDLGsimFP4nDC8JSP2uu9PkfB-o0be5EYzXWB2kj4EdskZei6ah-fRh9ywxSGbQoKg8xEhtSqCo9cma7txGJWcJEcY-sE6O9MJcTfxW_yAuRaR7WndLSndVhTdddJJkQ7HXXOd755toczgK87DfwwEL32vG9xoh8EafN5tUXCGg9FPv66Xt1ueSKhkIb4xkF4h3tqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوضاع اقتصادی به قدری خرابه که جانبازان شیمیایی هم مجبور به مسافرکشی شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/145094" target="_blank">📅 07:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69ee6e2c8.mp4?token=CBeAocYblVG0EJV5YMH86FVpqy19MD9hotekPSsIzN0Xybw4CRy-MR49d1wgZkNpZYnQzNGS46L-IdNYPNuHb3Btx-oHjqPUp9RPiiLg6Gxu3wNjWYTVRzW_2xJr-zT8qiCu7aufJlh0lZd-XOIZ61ws0mfho-GHCTflzHIGS32k96kdkHnroIS-mleDWZIg3XqKjUEJqSGoWpOI1L1tAzFLb56mTPMvbIFpHVFwmRoQRbPN3SYmOAZyMNV6_JjBc2A8apTJmr_vzApmxCsiLta5sYZ6H5QEtsDHOZUIVDw7zbZrQn2v-65Dilid9M-ZbN53KVya8AqtoIYfg4drC2FCY0Ba-JYjSEXXCdbFGCkvrLExTQImMu0pcgRSGyOzDZxMtytLn8_RXfuhVnEe9wE9zVPUi5mbqXfcURd2i89ClwftWg1b80vQyZH7lz6LpAKO8wca7ty45JxcLD9w6IqlS_L1bmF0Q860tGsA1EhYJqPTKKT54FycIcnph6oQA9iPBAGGmPKhZJ1RneL9SeJ-834yvQlPsugD7rqWqcFcdHUUHltPHnJbyU1Igj9zQUMxfzYMMzaDjIO65ZMdSz_WRNa-gBQRS7F4PbDLkDY267TQutGx3AqyrKRPMfD8R43RBQFWOKqnhxWAOTv7pLdvtJu2EOQ9-aTlCLbcvJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69ee6e2c8.mp4?token=CBeAocYblVG0EJV5YMH86FVpqy19MD9hotekPSsIzN0Xybw4CRy-MR49d1wgZkNpZYnQzNGS46L-IdNYPNuHb3Btx-oHjqPUp9RPiiLg6Gxu3wNjWYTVRzW_2xJr-zT8qiCu7aufJlh0lZd-XOIZ61ws0mfho-GHCTflzHIGS32k96kdkHnroIS-mleDWZIg3XqKjUEJqSGoWpOI1L1tAzFLb56mTPMvbIFpHVFwmRoQRbPN3SYmOAZyMNV6_JjBc2A8apTJmr_vzApmxCsiLta5sYZ6H5QEtsDHOZUIVDw7zbZrQn2v-65Dilid9M-ZbN53KVya8AqtoIYfg4drC2FCY0Ba-JYjSEXXCdbFGCkvrLExTQImMu0pcgRSGyOzDZxMtytLn8_RXfuhVnEe9wE9zVPUi5mbqXfcURd2i89ClwftWg1b80vQyZH7lz6LpAKO8wca7ty45JxcLD9w6IqlS_L1bmF0Q860tGsA1EhYJqPTKKT54FycIcnph6oQA9iPBAGGmPKhZJ1RneL9SeJ-834yvQlPsugD7rqWqcFcdHUUHltPHnJbyU1Igj9zQUMxfzYMMzaDjIO65ZMdSz_WRNa-gBQRS7F4PbDLkDY267TQutGx3AqyrKRPMfD8R43RBQFWOKqnhxWAOTv7pLdvtJu2EOQ9-aTlCLbcvJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه پاسداران تصاویری از حملات موشکی به اهداف آمریکایی در اردن را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/145093" target="_blank">📅 07:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMe_Ugg6l4p7Sax-kGLkbs-bICpx_uz9XupVuMJGoSp0DNljNsvmbW34WNNq0tkgW9bGA1YAJUOsFbHIoEQp8DCISGT7cdNBuw9eUibcdPVdtIsTLpbqWduN8CPQUiF_1AV7CftDoYtKZ4lmnDIpVdSYIMuvvBQz9pYx_w3ptwr5mEliB_2QuFhHWCnEDXTVOSwPjtvfsGJ6Jee_l6AMEag8E5VneZa7d2J_ehxjLESVwVpK2tCI6i0jw-b-4rKVnyYuPkzBblqc5IZKl4Txt6PJKe1L20CP6tVertB0TQRPGsfxcVz4mooeqKIGP_RCDEWr5sBB8hcRpYMZanW0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/alonews/145092" target="_blank">📅 02:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فرماندهی مرکزی آمریکا: موج حملات علیه اهداف نظامی ایران را با موفقیت به پایان رساندیم‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/145091" target="_blank">📅 02:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24346d9299.mp4?token=qqsJ92C033bnam3UcojGCx_8tp0aNe4jvf0HjOKH6zmhQ49kzpDQ2MqVRcWQyO00p1zgaw1O9IIE-NcYmzmrVIAv3tA2MFp0q5WB3D8TCePY8l6-2yLvw5JJZ1OrJcVPtnJLndSberAgp8hOmhSCgIeIafh1_hyw24Yexmh57hkReQj3uT_M71XIDn4i8B0GfE2Cb1fC6Eaor_SEWo9KA8vBA_r2kJlkzXWdV7aU2vbFBVpuZheRljId7nxfAX7eXsvihv2S82DxFzMdgp-MCp9adK-UkWZxG4FJl4st8xumyWp1BH4E2tfTQAdd1mYXJwSqzONduCTKooHsRoP7Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24346d9299.mp4?token=qqsJ92C033bnam3UcojGCx_8tp0aNe4jvf0HjOKH6zmhQ49kzpDQ2MqVRcWQyO00p1zgaw1O9IIE-NcYmzmrVIAv3tA2MFp0q5WB3D8TCePY8l6-2yLvw5JJZ1OrJcVPtnJLndSberAgp8hOmhSCgIeIafh1_hyw24Yexmh57hkReQj3uT_M71XIDn4i8B0GfE2Cb1fC6Eaor_SEWo9KA8vBA_r2kJlkzXWdV7aU2vbFBVpuZheRljId7nxfAX7eXsvihv2S82DxFzMdgp-MCp9adK-UkWZxG4FJl4st8xumyWp1BH4E2tfTQAdd1mYXJwSqzONduCTKooHsRoP7Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت:
یا سپاه پاسداران علیه یکدیگر برخواهند خاست، یا مردم علیه آن‌ها برخواهند خاست، یا به میز مذاکره خواهند آمد و خواهان توافق‌نامه‌ای خواهند بود که بتوانند به آن پایبند بمانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/alonews/145090" target="_blank">📅 01:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145089">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d43669ea.mp4?token=fa3qeNOKRdVycbDdB7G0AAB7dkMZBoX1ei-JGZYHHkVBJut1NupUlRZW3Fx9rmGsC4MvtM4rs7ANJ3K4AIINIxz6KbTDLDb3PNMpA_1mkI_-CENcz5lluBCsaTEg4vBf2NHSXSR1tsx-thny3nOmOHZxZFV-ATY4AcUKyALWTakif9DizbbDeQW1IjV0UcQZ__KbIGfSHlYCl2BWbMIrbOXE0ajp9titLoK-bj_PR5u91b8jWME06i417FHh-lyPZkFKi-SCzsL400002DJ3ME8qRmqpVYeSqAs6OvAwMGr3Kw4y4tF_rsr99KtoiTV6-YNPVlcPLWrmwNcHGQ04FFrI2E7xCLOw8iKuABQnyjlEt5wMLs6A9RDaEAFUYuX5Aw3n5-ECn3-XV3mCEn9-EEMMfYhL7WApCVKh1Gqerw-69vJ6wJLOLbCr1Z3-OEj62rFvilRmniU3fKRnfZPQ2jZ_RmaAMR8egdJY1KB3TLEZYFN3G0O3Sraon3pGLOgEJXJjrx3eiGiDCKMXJ2oT_5lODX1vnovSVwWyPjguXAuzWxbZ-hY1G0Kwl39M03YbdObZMHIn6kdq_s4KtK6gotYFJBmZQq3wJwQVvnbd91vQQDFt9sD0PqGhSbuvoDW_qIcpeT1uDAwuPzUE0ErAr796pomz7hyTV9CE3bRZ3gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d43669ea.mp4?token=fa3qeNOKRdVycbDdB7G0AAB7dkMZBoX1ei-JGZYHHkVBJut1NupUlRZW3Fx9rmGsC4MvtM4rs7ANJ3K4AIINIxz6KbTDLDb3PNMpA_1mkI_-CENcz5lluBCsaTEg4vBf2NHSXSR1tsx-thny3nOmOHZxZFV-ATY4AcUKyALWTakif9DizbbDeQW1IjV0UcQZ__KbIGfSHlYCl2BWbMIrbOXE0ajp9titLoK-bj_PR5u91b8jWME06i417FHh-lyPZkFKi-SCzsL400002DJ3ME8qRmqpVYeSqAs6OvAwMGr3Kw4y4tF_rsr99KtoiTV6-YNPVlcPLWrmwNcHGQ04FFrI2E7xCLOw8iKuABQnyjlEt5wMLs6A9RDaEAFUYuX5Aw3n5-ECn3-XV3mCEn9-EEMMfYhL7WApCVKh1Gqerw-69vJ6wJLOLbCr1Z3-OEj62rFvilRmniU3fKRnfZPQ2jZ_RmaAMR8egdJY1KB3TLEZYFN3G0O3Sraon3pGLOgEJXJjrx3eiGiDCKMXJ2oT_5lODX1vnovSVwWyPjguXAuzWxbZ-hY1G0Kwl39M03YbdObZMHIn6kdq_s4KtK6gotYFJBmZQq3wJwQVvnbd91vQQDFt9sD0PqGhSbuvoDW_qIcpeT1uDAwuPzUE0ErAr796pomz7hyTV9CE3bRZ3gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت:
یکی از بهترین متحدان ایران، رسانه‌ها هستند.
رسانه‌ها بلافاصله تمام دروغ‌هایی که ایران می‌گوید را منتشر می‌کنند.
هیچ مینی در تنگه وجود ندارد. دو کشتی به مین نخوردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/145089" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145088">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70bc81282a.mp4?token=GHTpEBvqPhMjY75kFdX5LSoIrQsysAJ-11sf4ciMVqzw4wupRqQo8JrzTU-jI0kEfwkuvnv8iOcmQ1YclwgoNIaZL9eA3xVvu_r_OTJOB3R2Z360SuO0TfQOy2SyS2yExzXZxduRvOXY-FbHExynBHC2rjtsoUeODxL_8PT7eUckNSgiz_r1RX9FpdrFVkxYUraZMkwrkH5gORvomxvEwhFop5iB_jSOlkJrMyC4_GbipEcuKD_VidxAP1gWN_zjfYcYUEgHCxXe-FENsGw9Z197CufW7vLRAY5hdy5h_mo1OfI_cIp3nOEJSF4gW-NTv5kPolc-VFbTWNPC6dM1ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70bc81282a.mp4?token=GHTpEBvqPhMjY75kFdX5LSoIrQsysAJ-11sf4ciMVqzw4wupRqQo8JrzTU-jI0kEfwkuvnv8iOcmQ1YclwgoNIaZL9eA3xVvu_r_OTJOB3R2Z360SuO0TfQOy2SyS2yExzXZxduRvOXY-FbHExynBHC2rjtsoUeODxL_8PT7eUckNSgiz_r1RX9FpdrFVkxYUraZMkwrkH5gORvomxvEwhFop5iB_jSOlkJrMyC4_GbipEcuKD_VidxAP1gWN_zjfYcYUEgHCxXe-FENsGw9Z197CufW7vLRAY5hdy5h_mo1OfI_cIp3nOEJSF4gW-NTv5kPolc-VFbTWNPC6dM1ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بِسنت:
فکر می‌کنم دیروز حدود ۱۷ میلیون بشکه نفت خام را خارج کردیم.
این کنترل تهران بر تنگه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/145088" target="_blank">📅 01:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145087">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114145c9fd.mp4?token=UX3NwZywpsQrQU4Vpvxu-1iI4IsHnhCxdDUaqnc_h5EHIwDYstDUkiA_zWWFVy7F5uRhgK37apnJAN3m6Iuog0xi6xoNpmPU5mg-lPoeRCtq3hZXe4V7w4eXlLiszDy8SnJ7bSm3caczSP0T92ggJS0a-IwXeYev2ri-87Ccao-0ZNIP-nqI9deMeEId80C1ubTS_XCYpci1dWDKV9AxG56b33agV2rcAAjAxseqsQSys2braFII-YB5iWjPNy_T_6SH7KDySoFgDmegco08qAS60J-QdXegzHzOzHUIBJIf2siWJX5yNhHrCWS3bU7vgrNDmnJwGl4yebejpf6E0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114145c9fd.mp4?token=UX3NwZywpsQrQU4Vpvxu-1iI4IsHnhCxdDUaqnc_h5EHIwDYstDUkiA_zWWFVy7F5uRhgK37apnJAN3m6Iuog0xi6xoNpmPU5mg-lPoeRCtq3hZXe4V7w4eXlLiszDy8SnJ7bSm3caczSP0T92ggJS0a-IwXeYev2ri-87Ccao-0ZNIP-nqI9deMeEId80C1ubTS_XCYpci1dWDKV9AxG56b33agV2rcAAjAxseqsQSys2braFII-YB5iWjPNy_T_6SH7KDySoFgDmegco08qAS60J-QdXegzHzOzHUIBJIf2siWJX5yNhHrCWS3bU7vgrNDmnJwGl4yebejpf6E0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر
: تهران تهدید به حملات تازه به پایگاه‌های نظامی ایالات متحده می‌کند.
🔴
اسکات بِسنت:
آن‌ها تهدید نمی‌کنند، آن‌ها در حال انجام آن هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/alonews/145087" target="_blank">📅 01:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145086">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گزارشگر
: آیا می‌توانید تهران را به میز مذاکره بیاورید، در حالی که چین همچنان از آن‌ها حمایت مالی می‌کند؟
🔴
اسکات بسنت:
فکر می‌کنم چارچوب‌بندی شما در اینجا نادرست است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/145086" target="_blank">📅 01:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ارتش کویت: درحال مقابله با حملات پهپادی از جانب ایران هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.8K · <a href="https://t.me/alonews/145085" target="_blank">📅 01:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
انفجار در کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/alonews/145084" target="_blank">📅 01:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=J1_Up-E1YCR5ENg6qqruGAf7yz8pIckCUEKDLymW72UB8PH1Btn2wi7EMWwmPUnZkyFp-4vVR5X9_pwHSocPsMiz-9RMwE6q0Ft68umPbhuOb-r6_8XS8c5CwKyezdoWx4JNWNnhEegV6C4tUGeGegjy_Ybn8N-Ibr0198dw8eO37mBvKHfkeD7C0pMdjvYI048hIsg7V5duesumwAe9LPp8tg_sgdxxZN_ZaHTmq78s3nVUNvn2DbJIG3ntvGXLkm1YaXjaMzf6YXe7Yhcc886_H5lXaJuX8l0lbaC70gv-dxip0X3H44x0XFqCN2aUz0iiHrlAFf8s9XhaIPxmbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=J1_Up-E1YCR5ENg6qqruGAf7yz8pIckCUEKDLymW72UB8PH1Btn2wi7EMWwmPUnZkyFp-4vVR5X9_pwHSocPsMiz-9RMwE6q0Ft68umPbhuOb-r6_8XS8c5CwKyezdoWx4JNWNnhEegV6C4tUGeGegjy_Ybn8N-Ibr0198dw8eO37mBvKHfkeD7C0pMdjvYI048hIsg7V5duesumwAe9LPp8tg_sgdxxZN_ZaHTmq78s3nVUNvn2DbJIG3ntvGXLkm1YaXjaMzf6YXe7Yhcc886_H5lXaJuX8l0lbaC70gv-dxip0X3H44x0XFqCN2aUz0iiHrlAFf8s9XhaIPxmbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه خبر خراسان رضوی دربارهٔ زیر گرفتن تجمع کنندگان پرچمی
:
🔴
تصادف بوده، عمدی نبوده، راننده حالت عادی نداشته‌.
پلیس راهور: یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/alonews/145083" target="_blank">📅 01:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145082">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏
👈
دادستانی مشهد: راننده مست حادثه پس از برخورد بازداشت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/alonews/145082" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145081">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
‏یک مقام آمریکایی به الجزیره گفت: حملات به سایت‌های داخل ایران هنوز ادامه دارد و ما پایان آنها را به محض تکمیل اعلام خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/145081" target="_blank">📅 01:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145080">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHxWoDfLKtlHhiXbcWWJ255zW8oL1CmMqCfQKP90ccwWLBjqgYsVuxiYnhUIcu5VmFdkeLyBAVcpqesnEnJ4CY0Rhul52jwPTAW20KbtLs3459WDguFFwKSnRJ-_U282Jxd8YhA8ZLSRVTGKYC1IPoO-70fPxwAYVpO1BW3UP3MHTnASA2Ea2IIRtW4-5gytvmHX1pGJmfHyXAuN_xm6LoMN15Y4YpfRS3Wq6mAaPFyBWczEW9B8Z3wv98-uSKgG98Xm3SMol7d6Fa23SlWEE7oasaTmmpIei7GLpyy0Py4Zf-Md2zyH7MkjaAzxdP4Mc_Y337j5OwTEsnFPbc0rFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از راننده‌های که با خودرو به تجمع پرچمی‌ها در مشهد حمله کرد
🔴
مشاهده فوری</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145080" target="_blank">📅 00:59 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
نیروهای مسلح اردن:
🔴
سامانه‌های پدافند هوایی ۱۳ موشک بالستیک را که وارد حریم هوایی این کشور شده بودند، دفع کردند.
🔴
۱۰ موشک رهگیری و منهدم شد، ۳ موشک در مناطقی دور از مراکز مسکونی سقوط کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/145078" target="_blank">📅 00:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
یه قانونی هست، وقتی هیچ جوره دفاع نمیتونی کنی بیجا میکنی دشمن تراشی میکنی و همش دنبال جنجالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/145077" target="_blank">📅 00:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یه قانونی هست، وقتی هیچ جوره دفاع نمیتونی کنی بیجا میکنی دشمن تراشی میکنی و همش دنبال جنجالی
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/145076" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری/شلیک موشک از اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/145074" target="_blank">📅 00:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8s3zSoU-LqgeLKlGxbic9TylhcKzimkZCNR_x26rVGlmlE3_hJKLK84vfUnGLFVveban6bRLNpjl4U3UbXferENrAKojeTwH-yVbIEv3m1MV2llFDNTfanBtPWOzRhCgjIdbf98ZqjvWlR1DS34euZX6MaP0p7DE60hdoc56f1o6watJGw9sKMw9BKxIVzXUxFVzDmJcOBApWkR8aMOWrM8iLmCOCNAMXErr7E7CNyefAlGiKS7YSOzyPZBN-2TYPeuqwX033DqPDHU7k_aSNf9SpmwvCSWSEe_Pf2xm6x2oWvRZvr1iKUs5WxLcYVFXEkzm2Zd0a2JlyA28OJvZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
متاسفانه در حمله ساعاتی قبل آمریکا به سیریک، یک کودک جان باخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/145073" target="_blank">📅 00:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
هشدار دلار   تارگت دلار رو چندبار تو این موج مشخص کردم!!!  الان دیگه چون سریع تر داره به اعداد میرسه به شدت پر ریسک تر شده یعنی حباب گرفته دلار هم!  یعنی یه خبر مثبت بیاد (که احتمالاً) میاد همتی نوسان رو گرفته رفته.   این هشدار رو جدی بگیرید!!!   @mahaneconomy</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/145072" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145071">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
تعداد زخمی‌ها در مشهد به 25نفر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/alonews/145071" target="_blank">📅 00:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145070">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/پروازهای نجف به ایران کنسل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/145070" target="_blank">📅 00:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145069">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بیانیه سپاه پاسداران در خصوص حملات امشب:
در پی حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن منهدم شدند.
🔴
عملیات انتقامی نیروهای اسلام ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/145069" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0s44TsyJaKHb0tc-TU7sRx147ImI0CgCudZvMAgcnFq8Vt_gdFDg1E3aQdQJrdCovXtQrUedcS69DKA4EI9CH5vbr2vblQKjBAWte2lTgzq7hBzFg-AdI3-EkArCswuAowAPfLztHRkMPgx3w5rHpFmBux1uLhIB8WVc9uJscT7PdqKKjdMVVwHt89pnzk2gNSgVhYAIk2uuFMD4Oh67T0MFNJ4OgfIT_a3lCisI_Oyh27Ra2KeQO19F9LKARXhGFV-uVFFBPtcYkJl1XBTmN_ooa0Fy8VUCagrgy6VbYokM60MlO5mSCB3_JJHUIofyyywLluhjR_RmZzxIHbMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ds6JNlWXEXxMMdfzX0MkqlZi5GE3GgvaJuHxZjsQ0jwUtGFYGvDo_1dage_AxhGJB2DranYNlbTVYTZJw9T-qgpEXK39eRC1CPBBxn0kEsC0rpNeZMA3TeJoNdp5CChgcplyzg6jzwSaG3Ocy9qdnGIpfPbzhlcRlT-J84NSZ2XPcJJOz16lqrau8UovpOB3Xy_MXxVDgWzeqarjSs0zi3QFkvsAnDTYrG1WLil5WdPdFyF9o5MvEQuuYFmHTSwM5tpQ49iQcGUetgi3OVl4uguXSbAh65l_qTykdKEa_tIHdus9t8wL3HOH83Ce3TK5G8o054wt8dmSTN2J8btZGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا حمله به تجمع شبانه مشهد دقیقا در همان مکانی بود که جاویدنام حمید مهدوی جان باخته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/alonews/145067" target="_blank">📅 00:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-5f1LJXxw_xMk-O_i8flAma9Ollq-N1VIyfFzIi4J_2MBZhXp1Zdi1xCVCRl8DwaAgIprtG2S5E1AlaNmfI7_DHgH_O7eUnOY_wSSotyGUMdw1XclPr2BGKLYAcaUEfWRUQ_um2Tra_LMoUfI1p-da8s2GlR8R0fgHZB9na8jeCv3A-rQIwDVtzEbqh9O5PXD1bcYyrg3SlokHbJAuUbl4HYShFWPMThNYfwRKEFqkwWsBBewQs7YNQIi8Khy8oqVmDSqDUbQyeJP7XvVOlc1H9nIshwnbjwNOCXv_ga0gHnZMtqAVEbMjeioQ3q7tk0U0G3HMRKj5va5WxhyeAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرگیری بسیجی‌ها اینبار در شیراز
‼️
🔴
یک خودروی ناشناس در شهرک گلستان شیراز، زنانی در خیابان تجمعات شبانه کرده بودند، زیر گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/alonews/145066" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/alonews/145065" target="_blank">📅 00:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
تعداد کشته و زخمی‌ها داره بالا میره
✅
@AloNews</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/alonews/145064" target="_blank">📅 23:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
تا الان ۴نفر تو مشهد کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/145063" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
سخنگوی سازمان هواپیمایی: هیچ نوتامی برای بسته شدن آسمان کشور صادر نشده است
🔴
سخنگوی سازمان هواپیمایی کشوری بسته شدن آسمان کشور را تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/alonews/145062" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145059">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=RD-SxWkNbnq04fAs82DuffX0BeJ5RIIgcXqWgWgCdIYrYPD5R1v7rDAQ3SdYAIcr6CfbKMesIz6IVEqvFWC_tFbYT5JzjtQ2Kk7aANmqQiBktWSVDUTIDmvReD4PZ0KLFJxI6FumeAv1uMZvRAWnpfbGWcGVr-7PljN1KNxW4nGa6x1QIJemmmHSHufb2lVekyNTHvN9cEJZVvy4y_X52x4_O2UOcbFK0fN-5KUh_gkQH3nZfXaB15v8mJm_2e9DjsQifEdLsehr_t4EYVhZ2VRIeVOqwhLRde15YwHcsktW5acWYV2Zgt1c87jV0mR9CmkXhEmx2oACojrEXTqxgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e410d017.mp4?token=RD-SxWkNbnq04fAs82DuffX0BeJ5RIIgcXqWgWgCdIYrYPD5R1v7rDAQ3SdYAIcr6CfbKMesIz6IVEqvFWC_tFbYT5JzjtQ2Kk7aANmqQiBktWSVDUTIDmvReD4PZ0KLFJxI6FumeAv1uMZvRAWnpfbGWcGVr-7PljN1KNxW4nGa6x1QIJemmmHSHufb2lVekyNTHvN9cEJZVvy4y_X52x4_O2UOcbFK0fN-5KUh_gkQH3nZfXaB15v8mJm_2e9DjsQifEdLsehr_t4EYVhZ2VRIeVOqwhLRde15YwHcsktW5acWYV2Zgt1c87jV0mR9CmkXhEmx2oACojrEXTqxgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دقایقی پیش تو مشهد، یه نفر با ماشین به یه تجمع شبانه حمله کرد و چندین پرچمی رو زیر گرفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/alonews/145059" target="_blank">📅 23:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145058">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
گزارش هایی از فعالیت پدافند در شرق و جنوب شرق تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/alonews/145058" target="_blank">📅 23:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145057">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارش انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/145057" target="_blank">📅 23:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145056">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=offJiyznG-HmIF-7JPPVDKlFDWTU2bEUMlJJaEe_XuQV6pEqY9R1zZCg8-DRgggggvSgeDPpPDPpl4bP6fAOv4z0b5KNlzK1G-LSPywsrx5EnWXSdsMNu2DJkE8fLEQLAaU3pfEHVJlFXuGB74htXeQaziBsC_qeal8DsgqKrQybvFvKQKjoWS7KM-CKhOKCalqivAA97CLH8NMbLcbWHzqguNloTfAP5SmnMm7BDAEF_vxC6nWJfgi3Pcn0qbg16mSNplyfSyfjLNMSHycSNC75T6cqscZgoN1G43Oup2VbkK1vRGT0TtK7sJHeTLRhu0_aszmuiEQlLw-Q0gsC6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=offJiyznG-HmIF-7JPPVDKlFDWTU2bEUMlJJaEe_XuQV6pEqY9R1zZCg8-DRgggggvSgeDPpPDPpl4bP6fAOv4z0b5KNlzK1G-LSPywsrx5EnWXSdsMNu2DJkE8fLEQLAaU3pfEHVJlFXuGB74htXeQaziBsC_qeal8DsgqKrQybvFvKQKjoWS7KM-CKhOKCalqivAA97CLH8NMbLcbWHzqguNloTfAP5SmnMm7BDAEF_vxC6nWJfgi3Pcn0qbg16mSNplyfSyfjLNMSHycSNC75T6cqscZgoN1G43Oup2VbkK1vRGT0TtK7sJHeTLRhu0_aszmuiEQlLw-Q0gsC6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/alonews/145056" target="_blank">📅 23:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145054">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ari2-OMXlH9veQBrKszBz9_KCQGNwJWHRKp96-V8WG99dxZoY3nr1QqouOgLinYSYzoz25QAmu3NlkFt2DxoC1EG8nSEHi2cJyxLSrFDsbJv4fLz8n4XtFIAMP_CMMD1vfx6IfhnaeM9_4A5LTg5fNEphNg6nI4V8lAv7Ydq7iDWJxzz4wHRZvSGbClpBPYKKbnPqdzegbUWBEqoeGuuGY5Rm3up6lzHju65N1LZv6Z7zdQkWUxd1JQfRmvtTc7pR61jQzoJrK_6_QR6TBxxUUuG20XMr6n5-JLCINhL44QJY1zMzHC8R3uovRhMO66SpiOcNvJ6v1JQ1XtZasaP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SgkjGi81esGoIgRQD7AExpUi0Xm3fm1-Ijo9S3RdLmDvOA1zsilYVsRwPHYU9vcQWCuldAZNp3iDh1WJm-kerFtG_NQSejkk5cu4xxbjVG7JdcHn158S0wdHcYOdQ8TaCjpi7hig2cEm18aCZ2ZSIxv-maJNG6BbvlqXls3GFcCwIrauwdat5oNwgXqbmJF9X5LyKXLysbl1BcSWzHsOO0kz0TV0nPNpajowAZ4eVZzRiRY4J91anhNYBxGWP2QqmfbLu0IpM81aCa6UicJAaAc7r6HbhHsV6aFt3gsVhMN457IF8lI1dxSep342IV-5wUsvaUMRo6J2Eb_Mrv8jEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصویری از دکل مخابراتی در کوهستک سیریک  که هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/alonews/145054" target="_blank">📅 23:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145053">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلار منفجررررر شد
‼️
هم‌اکنون قیمت دلار به 215 تومان رسید</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/145053" target="_blank">📅 23:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145052">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رسایی: هر چه سریعتر اینترنت رو قطع کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/145052" target="_blank">📅 23:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145051">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوووووری/پدافند شرق تهران فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/alonews/145051" target="_blank">📅 23:27 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145050">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf04fd5ed.mp4?token=e8NbQmXPlEMvthfI9IzdE-UqRPDHPua4uTLUNVuD2_a5AgaFTQWxiD-mJz9qw_ClLWzSMMFK2V4ej_hYhozV7EdDlyYww7hQRteBRr9H_WHFH4CuHRu98W4sSMo3DKK_y87ACh3kSLzdDJrRsZtWJ8MSq0FvAMNIq-d3pCQczcb5kb7FKWD6Ldd-ihrYZtnoMh0TMzpqWyP3808C-vf9yBag6J5Uts6JLmRVfgWbzOtGPe9tjWenB4XL5fGwH7uWPQ6ZmQXk2KUF96JLA4_aaTGRkZOasPF_7FXO3RiAPUCfSXC_1zPuK6dH12Jmxe9CKQPkw4RQZ0vL6nc_mxGkoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf04fd5ed.mp4?token=e8NbQmXPlEMvthfI9IzdE-UqRPDHPua4uTLUNVuD2_a5AgaFTQWxiD-mJz9qw_ClLWzSMMFK2V4ej_hYhozV7EdDlyYww7hQRteBRr9H_WHFH4CuHRu98W4sSMo3DKK_y87ACh3kSLzdDJrRsZtWJ8MSq0FvAMNIq-d3pCQczcb5kb7FKWD6Ldd-ihrYZtnoMh0TMzpqWyP3808C-vf9yBag6J5Uts6JLmRVfgWbzOtGPe9tjWenB4XL5fGwH7uWPQ6ZmQXk2KUF96JLA4_aaTGRkZOasPF_7FXO3RiAPUCfSXC_1zPuK6dH12Jmxe9CKQPkw4RQZ0vL6nc_mxGkoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیدگنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/alonews/145050" target="_blank">📅 23:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145049">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a92fa8fd.mp4?token=Kq27fWdi_Oe_OBH8K0sAAmHTPlYVFbHBCSodqV3fnjwQp_ywWjyQAe8hl2nAwagQ1THF6vNzaNrqGWOpbR96OJz2LKBjgiuHXgQpZrIbQzbq5SPsY_Ksp7o1WW9qR7B0AGIgYz1JOBmpklLFacS8dD4tCvROhYHtunZObauDyLml3aB5gllKoTI59hWz_C87GRIe9ZaGn_ZzOyIRUc9GVgzq2-7FJWobsV3BEnwsMWUxuz0wMgLTgJZCaRbMGS7L2zyCB9NFs3Zq4Whp-u_2641V_otVkJgzlj4Nqv8Soir_8keT_fyvvDNYCBZe-K2-txiZ1OqeRphnZ8fgb9FmpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a92fa8fd.mp4?token=Kq27fWdi_Oe_OBH8K0sAAmHTPlYVFbHBCSodqV3fnjwQp_ywWjyQAe8hl2nAwagQ1THF6vNzaNrqGWOpbR96OJz2LKBjgiuHXgQpZrIbQzbq5SPsY_Ksp7o1WW9qR7B0AGIgYz1JOBmpklLFacS8dD4tCvROhYHtunZObauDyLml3aB5gllKoTI59hWz_C87GRIe9ZaGn_ZzOyIRUc9GVgzq2-7FJWobsV3BEnwsMWUxuz0wMgLTgJZCaRbMGS7L2zyCB9NFs3Zq4Whp-u_2641V_otVkJgzlj4Nqv8Soir_8keT_fyvvDNYCBZe-K2-txiZ1OqeRphnZ8fgb9FmpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منتسب به شلیک از یاسوج
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145049" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145048">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پرتاب موشک بالستیک از استان لرستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/alonews/145048" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145047">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ستاد کل نیروهای مسلح: «ما پاسخی کوبنده به دشمن آمریکایی خواهیم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/alonews/145047" target="_blank">📅 23:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145046">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8374f239.mp4?token=i_McJxSkqaq8KomEhWs_k_4rwZ2_zbpyIN-xqapwqXsEflvdjA4mZx2jwTAiMtF72xx85dRFajG4t_xmOo5ia6kV7rbab0P4Rqy1VJ7ono1zqTuOaMt_80U9YQfaJPpMgkB3KZ8YiU8MKeutG-oQaznVmZM9Fc3pXcxY9OU7s6-TZbLlpgIAYL_K6U4_kl2c3ibUfyH4gquEK4fSkFqwm3bTADQ3Ma_IjoL2AqAnc3gQgmbEKXTDUzTIhX5WsTaf3jMvj1TsaJ4zMChHcmdYSFDLHPQ-pNmIYc_YaoSsTGgviz9Oi6MSi84s6jF2BMhKBF8Zw-lsuTR4tc8vXVXL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8374f239.mp4?token=i_McJxSkqaq8KomEhWs_k_4rwZ2_zbpyIN-xqapwqXsEflvdjA4mZx2jwTAiMtF72xx85dRFajG4t_xmOo5ia6kV7rbab0P4Rqy1VJ7ono1zqTuOaMt_80U9YQfaJPpMgkB3KZ8YiU8MKeutG-oQaznVmZM9Fc3pXcxY9OU7s6-TZbLlpgIAYL_K6U4_kl2c3ibUfyH4gquEK4fSkFqwm3bTADQ3Ma_IjoL2AqAnc3gQgmbEKXTDUzTIhX5WsTaf3jMvj1TsaJ4zMChHcmdYSFDLHPQ-pNmIYc_YaoSsTGgviz9Oi6MSi84s6jF2BMhKBF8Zw-lsuTR4tc8vXVXL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/شلیک موشک از اردبیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/145046" target="_blank">📅 23:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145045">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/شلیک چندین موشک از بیدگنه تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/alonews/145045" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145044">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری/شلیک موشک از کرج
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/145044" target="_blank">📅 23:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145043">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/از بسیاری نقاط ایران موشک شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/alonews/145043" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145042">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/شلیک موشک از کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145042" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145041">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/شلیک موشک از یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145041" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145040">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
هم اکنون ، صدای انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145040" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145039">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/شلیک موشک از اردبیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/145039" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145038">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
پدافند هوایی در اردن فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/145038" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145037">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‏یک موشک با دکل ساختمان وزارت اطلاعات سیریک (هرمزگان) برخورد کرد؛ شاهدان می‌گویند دکل متلاشی شده است.  @breakingpersian</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/145037" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145036">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_sEB1wqposAlmAGOZsKCVL8Sb70Rq7wfQGifJ4PQhmtDbdAFInVhz4XXCKVTPLUnwq117LIh1ZeUryFQwgYHAqEyzRHdP430cFrigXYCXzOL98WPTdwBi_Jij_xEdelcQzJHEvLjgmt8zCZAEhPAifeGxVKnRBUlyPlsFXeSpbE72V1RQ4XsPaok2nGJw2Lq8E7tAPyWSyx65P2OJF7Hv8UCZ4s2tj_vQ2r1-FZ7wxC7G2BmjLvGCEXrG2RBeGwAdxZ7wSkdIA7zKOqRN3hoqIJFdckxBKHtOSeafZpoUdES_Q5cTK_M-RjtrX4SDMktaq4lRTTfcK7uIL3rr3tRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور محسن رضایی: حملات امشب آمریکا گسترده بوده و به نظر می‌رسد ایران نیز در واکنش به این وضعیت، سطح پاسخ خود را گسترش خواهد داد. با توجه به شرایط موجود، تحولات مهم و داغی در پیش خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/alonews/145036" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145034">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فارس: پنجاهمین پهپاد پیشرفته MQ9 ارتش آمریکا رو منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/alonews/145034" target="_blank">📅 22:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145033">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
العربیه: حملات آمریکا تسلیحات و ادوات نظامی ایرانی در حال انتقال به تنگه هرمز را هدف قرار داد
🔴
آمریکا ارزیابی‌هایی در اختیار دارد که نشان می‌دهد ایران برای گسترش حملات علیه کشتیرانی طرح‌ریزی می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/145033" target="_blank">📅 22:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145032">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره: حملات به ایران همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/alonews/145032" target="_blank">📅 22:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145031">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
گزارش های مردمی حاکی از آن است که خدمات تلفن و برق در شهرستان کوهستک، استان هرمزگان قطع شده است
🔴
این گزارش هنوز به صورت رسمی تایید نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/alonews/145031" target="_blank">📅 22:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145030">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
هم اکنون؛ شنیده شدن دوباره صدای انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/alonews/145030" target="_blank">📅 22:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145029">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_2WQvgP_Vi7Uxxc85ZOusqvX4UBPeSu6JKfOYzE2LoueRWr8H1BfpahUacaB-NLew_QVtG_C3S0csnSZ7Nidl9X8UT8MJ7GxLI6m295I5KdTOlMVoRXesWyFOKQM0grzBmMKNiw_Wit2oKo892GVF_8gVxFZZlGZ3UR_mNKUfK09t1vBtG4fNL4HTcctMsC2ktf3ozdUqvZuWB84m0qC21vKNuzhcmz21izKWMgdyzxrPOmIH4dD4wMl2W8EcGmilmQTECdPSxdQ1I3dz6pm6igznmVPXjQCiCwg2swebeLFidYfH7vwHlhHaB34kAey7rWATooZyTJTdhxslTnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط هواپیمای پزشکیان درحال بازگشت به کشوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/alonews/145029" target="_blank">📅 22:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145028">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/موج جدید حملات شروع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/alonews/145028" target="_blank">📅 22:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145027">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سیستم‌های اسرائیل پرتابی به سمت اردن را شناسایی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/alonews/145027" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145026">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
خبرنگار فاکس نیوز: امشب چه اهدافی در ایران مورد اصابت قرار گرفت؟
🔴
ترامپ: تعدادی از رادارهای آنها
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/alonews/145026" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145025">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فوری
🔴
حمله بزرگتری در انتظار است و زمانی که به پایان برسد، تقریباً هیچ چیز از جمهوری اسلامی ایران باقی نخواهد ماند.  ترامپ:  ایالات متحده، در حال حاضر، به اهداف ایرانی در نزدیکی تنگه هرمز حمله می‌کند. این حملات گسترده و قدرتمند هستند و در پاسخ به تلاش…</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/alonews/145025" target="_blank">📅 22:26 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145024">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
معاریو به نقل از منابع: اسرائیل هیچ نشانه‌ای از تشدید درگیری با ایران یا ورود تل‌آویو به جنگ دریافت نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/alonews/145024" target="_blank">📅 22:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145022">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcH18tfGMekhFsiOZIgVWBHAy9-bQX1eMyP4oqeMzke7bphKgO_4ldWXzWz7paIRqBPy4mYFpdYJu8hjySYnwLiQE5qYbbuWZKDj3GVtFVra8du4mQ0O8DjDk8UlxIQ0yxNtOXFLiSFl1w1Z0xNwiuE2UzccR1m0tivH1nwfL_JXS2YUADuyuKFdxJWmKQ9-XjmwHgDWhv7uWww4dSiuRYoLvQQQ20wH9-ZUUaTTTsE_u9QVw4GfWEV4lpSqV_dCQLVw1raPJHnfUi5RxtKL54cT2WoqdWhEBXF6UtMLjldK_hHtKnN5hCLQdU1CVHSHoC77QW0gUCRLsgAVLYry-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره: ما شاهد بازگشت چرخه‌ای تدریجی از تشدید تنش‌ها هستیم،
🔴
چرخه‌ای که به طور قابل توجهی بی‌ثبات‌تر به نظر می‌رسد. یک تقابل تلافی‌جویانه می‌تواند به راحتی به یک رویارویی منطقه‌ای گسترده‌تر تبدیل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/145022" target="_blank">📅 22:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145021">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نفت خام آمریکا بیش از ۴ درصد جهش کرد و برای نخستین بار از ماه ژوئیه تاکنون از مرز ۹۰ دلار در هر بشکه گذشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/145021" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145020">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cO8kETsgEVt42sv9X2P1g4QQLNubwdAlseTVH2xpzZlDN4o1groLXax-meYLhBpZhXL3glJyNV8JUQX-lzgXhe5y0HKv0DAo9fPRyurKvhlbWE__DRTCdGrJ9Dgc8f15ngQbXofaUHLl1ieBFIFq9qCJqhifxZhHc_CbTedTw59PvSne04i1Sxd6d8GjV2SpAp6cgYc48wfFUvCeVHLf4etgBmCK-D8eR6FneHNrj3TsIk628DBnSG49q_ea90utlZm1HVspsjoyoQMyzaoMJkFThni_gqfj-Q-BW-WgJzibmK2SsLnIpmuBy1JSLzG7cNN5mKdLhlsNCqGt-0ntIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوخت‌رسان ها بالای تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/145020" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145019">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/145019" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145018">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnyBNA9pHUXoCFNVVAPCM4XIu_z2Dv3hWBcJ7UQ_ZTBWCWQ0kTMeuFjUQMcDGFlY3iuBW0YYbAw7ELTYwXcND6C6mlfZcNfsFXgTjbRWus7LBZkiJc9AFuVel3wk35unrwEVtBYCE4cHbWADOjJW09w3UPTh9hhiycGe4xu8hIpDrzwQX6naoXmKsM6T1npVLiuQH0MCzG3g3TU3rKF2Qd3w8znbw9IaQZ6Qn-iJt-Fm7CWeVhKoXDENcmb17lCHqPu4RJwLc-79u4hVdt_XMMgRyZL2MnhacoL69k9ZJ4EQvWDJjjqWpGsOJ9aqX9Hiwcc2K12opyhbLOxpQvux-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت فعلی آسمان ایران
🔴
تنها یک پرواز استانبول مشهد مشاهده می شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/145018" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145017">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fb757104.mp4?token=c8ieUmq0e5jFA__64tA0I_TWOHUp_5pnHrLI0QNP2M97m3ralHpbE6OPAGhjyLByX-lxSLHK5y1JKDPwPSSYmAvPE2r2NcYIfw8NZvUkNt8oV0G8gb1UNz76SeGmRtpVh1k1ns8G-S7ySatvSDexdFRPLH5-1CrL5F5iCE800B9OiQcg4d_vLFVtthDDr00c4ZRjLQQoMUthTbD5jurkVHQ_QlKXBsl5rKPmtrXgz4XYzgId7sgIvmXdjR46RNu0fPcangpDIhumQPoUOHOCLaVveBwTnXc6CLz0i2OhwZvF6T06KHhTA4hp5BrFWMnWAxxGEQEGsWRzbOWb-PfprA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fb757104.mp4?token=c8ieUmq0e5jFA__64tA0I_TWOHUp_5pnHrLI0QNP2M97m3ralHpbE6OPAGhjyLByX-lxSLHK5y1JKDPwPSSYmAvPE2r2NcYIfw8NZvUkNt8oV0G8gb1UNz76SeGmRtpVh1k1ns8G-S7ySatvSDexdFRPLH5-1CrL5F5iCE800B9OiQcg4d_vLFVtthDDr00c4ZRjLQQoMUthTbD5jurkVHQ_QlKXBsl5rKPmtrXgz4XYzgId7sgIvmXdjR46RNu0fPcangpDIhumQPoUOHOCLaVveBwTnXc6CLz0i2OhwZvF6T06KHhTA4hp5BrFWMnWAxxGEQEGsWRzbOWb-PfprA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرنگونی پهپاد آمریکایی در خمین
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/145017" target="_blank">📅 22:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145016">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/981e07149f.mp4?token=Jc7lAIS2_6GRJhtadxSu3K9WZz1IggaQO20EUbrtxg3hqsn-Q6gQq8SY0F0p-Tk-Xj2tekhK0I2d1RF8BrpnS1zcpJ1B8YGL3zfl2fz9yO-q9w-17Af9cQRiqrclTF-_sYvShMgLTG_03tbQHWH9_Ak_WvrBnOTa2GcWEtmq8Egqi8YAeN5SL-QM2-UyFRA6SPWvdAVvwf5PllMW_0YNEMRHwZMWBTeiOJdQ-Wr406_KvDduzjEp5we7B65aFyAyb9-8cp2AfSdYDCEfMUzZgef_zmoardP4z0z1SciXanTrYqj7EHoo422_t1cGy5MPnA7XUIx5rtrXIrw-hoI7V7gayJWOXoFeske-wgHmbmAQmZkecTH6H9YShsBhAvwgn1Abr-lvpQtaaGq9GCrJayFnSwpOw0SQ-avxqApcGSOM6g09aMdBnpCb5ntpCoroT_eLd-TmXiMcL1NhZCS1D_yg98ByddCaxsBffDmjbIsvyThDsozlhA9cdQPcSPzhpos0xf-KolfXHlUZn7K8goAo-p1vEl3jTxybf--7aDVbYQmLWFZwAEZ4_AftrDNaauHYlkVp923RGaVv7DDzVVVzb1wCOLCWH9tiJgSaVECVJP_pwOkwxvehNTDJI97iYeNqfaE0iI1hEfiuRxyyCwFE2Pel6hvdG0NDrPrZmTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/981e07149f.mp4?token=Jc7lAIS2_6GRJhtadxSu3K9WZz1IggaQO20EUbrtxg3hqsn-Q6gQq8SY0F0p-Tk-Xj2tekhK0I2d1RF8BrpnS1zcpJ1B8YGL3zfl2fz9yO-q9w-17Af9cQRiqrclTF-_sYvShMgLTG_03tbQHWH9_Ak_WvrBnOTa2GcWEtmq8Egqi8YAeN5SL-QM2-UyFRA6SPWvdAVvwf5PllMW_0YNEMRHwZMWBTeiOJdQ-Wr406_KvDduzjEp5we7B65aFyAyb9-8cp2AfSdYDCEfMUzZgef_zmoardP4z0z1SciXanTrYqj7EHoo422_t1cGy5MPnA7XUIx5rtrXIrw-hoI7V7gayJWOXoFeske-wgHmbmAQmZkecTH6H9YShsBhAvwgn1Abr-lvpQtaaGq9GCrJayFnSwpOw0SQ-avxqApcGSOM6g09aMdBnpCb5ntpCoroT_eLd-TmXiMcL1NhZCS1D_yg98ByddCaxsBffDmjbIsvyThDsozlhA9cdQPcSPzhpos0xf-KolfXHlUZn7K8goAo-p1vEl3jTxybf--7aDVbYQmLWFZwAEZ4_AftrDNaauHYlkVp923RGaVv7DDzVVVzb1wCOLCWH9tiJgSaVECVJP_pwOkwxvehNTDJI97iYeNqfaE0iI1hEfiuRxyyCwFE2Pel6hvdG0NDrPrZmTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: «آنها سعی کردند رادار خود را بازسازی کنند چون هیچ چیز را نمی‌بینند. ما صبر کردیم تا تقریباً ساخته شد و بعد آن را زدیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/145016" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145015">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
هم‌اکنون دو انفجار جدید در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/145015" target="_blank">📅 22:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145014">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8ea8cab388.mp4?token=C8QSNRjoFFHWcm5hwpIeveMLd5IfEaiJeaT-r4qsFeIh4TFXlGgLqfZyOqVx0koaQUqxTE-QHNLXnDF0y_aUUhE3u_cQsmYrI8CUq_KqG8RXC6QYTmngjMj9rPwyz147tUnLgzuYyL_oMF2laFnMIXPxJpuRjGw1BVNTacY_dDRN6Bo1IzHRpPtomTTt4SDOPRHludznJnFow4bl6BIMXbkVgUgrRfu1lysrYCCgefpbr-yLhZSn5AtRs5npMZ7XPVNcC4I6kLM3tchV4gwtAZ4ejV6eeMLBTNAKI5EoemAi1t5ZzG61Xv5gcST_OjCpiXSu9VQsuJGMvqUrb5m0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8ea8cab388.mp4?token=C8QSNRjoFFHWcm5hwpIeveMLd5IfEaiJeaT-r4qsFeIh4TFXlGgLqfZyOqVx0koaQUqxTE-QHNLXnDF0y_aUUhE3u_cQsmYrI8CUq_KqG8RXC6QYTmngjMj9rPwyz147tUnLgzuYyL_oMF2laFnMIXPxJpuRjGw1BVNTacY_dDRN6Bo1IzHRpPtomTTt4SDOPRHludznJnFow4bl6BIMXbkVgUgrRfu1lysrYCCgefpbr-yLhZSn5AtRs5npMZ7XPVNcC4I6kLM3tchV4gwtAZ4ejV6eeMLBTNAKI5EoemAi1t5ZzG61Xv5gcST_OjCpiXSu9VQsuJGMvqUrb5m0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شلیک موشک از تبریز
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/alonews/145014" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145013">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پرتاب موشک بالستیک از کرمانشاه، ایران.
✅
@AloNews</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/alonews/145013" target="_blank">📅 21:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145012">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صداوسیما از حمله آمریکا به فرودگاه جیرفت خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/alonews/145012" target="_blank">📅 21:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-145011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
گزارشی از حملات آمریکا به نقاطی در کشور
🔴
نقاطی از شهرستان کنارک در سیستان و بلوچستان
🔴
قشم (هرمزگان)
🔴
بندرعباس (هرمزگان)
🔴
سیریک (هرمزگان)
🔴
جاسک (هرمزگان)
🔴
بندرلنگه (هرمزگان)
🔴
نقطه‌ای در جیرفت کرمان مورد هدف آمریکای قرار گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/145011" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
