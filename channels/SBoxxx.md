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
<img src="https://cdn4.telesco.pe/file/eGbwzji4ecvrHl-kBLisQ_0ezKpfhXfnmRl8MSgweSojllJIYKyWv1XGT0I2pP_qZKJWKwRk6YzxbvDmsg6JilQ81Nb16P2fLYV7AXfzuPZ1ZFrpE3dpS2MnvwSpdT4QvGM17tCipWC1cAk5SvJMw7Zd4SN-Z0o8m8VrNw6Mm0AewiHCESxirk2Rwp7ooKSEFkfRJOKKG9cVTZkR2E06Vfa6_jBKB6Kfk9PGyHFJ65saWeSppeqkLgWM1Oi2bBmYvAXlL8LOxi1Vdi9sWsjS8NDpxF0wG8ILvv0VOdx-7dHHGjVpApq4U34k6nCGHNSHWeNm07aA9brqbEfF2LYx_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 23:42:46</div>
<hr>

<div class="tg-post" id="msg-20118">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">محسن رضایی:   مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SBoxxx/20118" target="_blank">📅 23:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20117">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محسن رضایی:
مردم در خانه‌ها و محلات شروع به تولید محصولات مورد نیاز جامعه کنند</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SBoxxx/20117" target="_blank">📅 23:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20116">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f676cce991.mp4?token=HXkNd49pDsDBesCTME24uHEmABOJgFbJkBhoibbTG6Woy5GnrhFhQq_GJzu666BdCWvrKYZFWCPMj-0Xu23UahvWmb97iFsaLxRZFHqT7nHz4Xn4lOBAji9o7UVuPQJukrsKhiPybHrh3R1oxe5oeW6SJD6WHr_gbJFhhgRvuwbPOu3yXah1dnLtDF33smdux2MU8J-kMrc-JiN2TawFIUJ-0cbp80yQe9ioStQh0XXF_C2cqBrpQ2pulpEKS8C2qO_8oS2edPuRxTj6huloisk5nSx9qJ-li-QZ9TTNoAdVeLRKLLoXZS5pkAVjXiwHJneIIkZ0SFOlf1ojxe1kSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f676cce991.mp4?token=HXkNd49pDsDBesCTME24uHEmABOJgFbJkBhoibbTG6Woy5GnrhFhQq_GJzu666BdCWvrKYZFWCPMj-0Xu23UahvWmb97iFsaLxRZFHqT7nHz4Xn4lOBAji9o7UVuPQJukrsKhiPybHrh3R1oxe5oeW6SJD6WHr_gbJFhhgRvuwbPOu3yXah1dnLtDF33smdux2MU8J-kMrc-JiN2TawFIUJ-0cbp80yQe9ioStQh0XXF_C2cqBrpQ2pulpEKS8C2qO_8oS2edPuRxTj6huloisk5nSx9qJ-li-QZ9TTNoAdVeLRKLLoXZS5pkAVjXiwHJneIIkZ0SFOlf1ojxe1kSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخستین تمرین رزمی جنگنده سبک یاک روسی در نیروی هوایی ایران    ‌
👍
جنگنده یاک در کنار دو فروند جنگنده میگ ۲۹، در عملیات رهگیری و منهدم کردن پهپاد هدف مشارکت داشت و خلبانان جنگنده‌های میگ ۲۹ با مهارت بالا موفق به شناسایی و رهگیری پهپاد هدف شدند.
👍
در ادامه، جنگنده…</div>
<div class="tg-footer">👁️ 1.78K · <a href="https://t.me/SBoxxx/20116" target="_blank">📅 22:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20115">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اسراییل در حال بمباران جنوب لبنان است.</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/20115" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20114">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMlnn4u32gRQckoCz1ZL80qv5aV2rmFnw7NU_1CPuO8qjaBhQu54ybIPRzxk_WYFKQn6s4gHE5zjFYbI5e7W7oEGfrA_GiwfnTZpPo8opGG3fzW0LhNKmolc9_ydQ9gXPF0_Q91idEuSTk2-ABO1UXBguxI4lT5vXt0Pi9rMZU5nR-viAw1mIs8gJgKnjueNEt-w2iTqV14qN5HBxCmJVW6FWo8_Ktsc7E8g8O_RqUtv7xIhULVW_74jrvq_OG1GH0Ydzr5CNzdKqT5RwzRSS2y6IPzDjKrQQz-DOy4hFUclN6-AkJPBrLMY8Po4nkq0xBMIefZ1FmcaQKDtSkZlvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقاله در روزنامه اورشلیم پست اسرائیل خواستار آن شده است که اسرائیل، ترکیه را به عنوان یک تهدید نظامی در سطح ایران در نظر بگیرد، و این جمله تحریک‌آمیز را مطرح کرده است:
از ادلب تا استانبول، اسرائیل در صورت لزوم، حمله خواهد کرد، نه اینکه دفاع کند.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/20114" target="_blank">📅 20:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یک صوتی مفصل در این خصوص خواهم داد.</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SBoxxx/20113" target="_blank">📅 18:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اوه اوه!    بنگلادش در حال بررسی امکان پیوستن به پیمان مکه است!</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/SBoxxx/20112" target="_blank">📅 18:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">باز سعودی ها دستکم کتک خوردن ترک‌ها در سوریه از اسراییل برای بار پنجم را محکوم کردند!  شهناز جوراب که کلا خودش را زده به کوچه علی چپ!   نه حملات یمنی ها به سعودی را محکوم کرد نه حملات اسراییلی ها به ترک‌ها را !  سبحان الله عجب پیمانی شد این پیمان ناتوی اسلامی…</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SBoxxx/20111" target="_blank">📅 18:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دلار فردایی تهران
⏳
192,300 تومان!  کاملاً مشخص است به صورت دستوری دلار را دارند بالا می برند تا جناح تندرو را به تسلیم وادارند یا دستکم گرانی ها را به گردن آنها بیاندازند.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/20110" target="_blank">📅 18:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SBoxxx/20109" target="_blank">📅 18:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خیلی عجیب است.   خود ترامپ در مارس ۲۰۱۹ منطقه جولان را به عنوان بخشی از خاک اسراییل به رسمیت شناخته آن وقت سفیرش در ترکیه صحبت از «اشغال» جولان می‌کند!  حدس میزنم عمر سیاسی  — و شاید زیستی — تام باراک (که عرب تبار است) بزودی به پایان برسد.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/20108" target="_blank">📅 18:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-poll">
<h4>📊 تاریخ شروع جنگ ایران و‌ عراق از دید عراقیها چه تاریخی است و چرا؟</h4>
<ul>
<li>✓ ۳۱ شهریور ۵۹ — حمله همه جانبه ارتش عراق</li>
<li>✓ ۳۰ شهریور ۵۹ — حمله هوایی ایران</li>
<li>✓ ۱۰ مرداد ۵۹ — سخنان تحریک آمیز رهبران ایران</li>
<li>✓ ۱۳ شهریور ۵۹ — گلوله باران مندلی و خانقین توسط ایران</li>
</ul>
</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/20107" target="_blank">📅 14:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این هم جواب آمریکا:  ایالات متحده در حال پیشبرد قانونی است که هلند را مجبور می‌کند تمام فروش و خدمات باقی‌مانده دستگاه‌های لیتوگرافی ASML به چین را ممنوع کند.  قانون MATCH به دستگاه‌های DUV قدیمی‌تر که هنوز تحت قوانین هلند مجاز هستند، هدف می‌گیرد.  چین ۳۳…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20106" target="_blank">📅 14:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SBoxxx/20105" target="_blank">📅 14:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/20104" target="_blank">📅 13:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20103" target="_blank">📅 13:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ایران اجازه عبور چندین تانکر نفتی عراقی از تنگه هرمز را پس از درخواست عراق صادر کرد: ایرنا  چنین اقدامی در اوج فشارهایی که روی اوراق قرضه خزانه داری آمریکا آمده به صورتی که باعث شده اسکات بسنت دست به طرح عجیب و غریب بازخرید اوراق قرضه بلندمدت بدون تقاضا بزند،…</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SBoxxx/20102" target="_blank">📅 12:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/20101" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.   اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/20100" target="_blank">📅 12:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNQUWCL4DDWd_WvFsbPTDcyKE8Vt-yod_RAmwloXJznowZJOPoK_KxPrH98Q1buZZniW8USGbIZKEs2_YdFHanVLXMMjH1jZbUNr4IILq8_zePmVRgiyJlY0kKzjc5E5z-eHBKO6IOO9sNrUO4u0x7i1WgPKTDOe6Wn0Zcc_k5aLyMz78sR8BCfmG8Lv18ThV9I9tq8UYPed5HgY6kyqdwQcHghR08W-Z1hQZR8HdD3WCZWt8VCNv5UxbuoC6R6VbBobGv7L27jh7gNpZLuKUGegB0SQQ8Sw5w1mMRXmKlR9A-3-I_LxXqrsbHFYTAUCGeoYcdwDE8tS6qTM5P_s0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌نظر می‌رسد در درون ساختار قدرت جمهوری اسلامی، شکاف میان جناح میانه رو و جریان تندرو و ضد امتیاز، در حال برجسته‌تر شدن است.
اگرچه این شکاف هنوز به تغییر رسمی سیاست حکومت منجر نشده، اما اظهارات اخیر دکتر پزشکیان، محمدباقر قالیباف و عبدالناصر همتی نشان می‌دهد بخشی از حاکمیت بیش از گذشته به این جمع‌بندی رسیده که ادامه جنگ و فشار اقتصادی می‌تواند هزینه‌ای سنگین تر از جنگ برای نظام ایجاد کند.
پزشکیان دیروز صراحتاً گفت بهتر است جنگ در مقطعی پایان یابد و «اکنون» پایان دادن به آن ترجیح دارد. قالیباف نیز هشدار داد که حتی قدرت نظامی بالا، بدون گردش مالی، رشد اقتصادی و تولید داخلی، نمی‌تواند کشوری را که مردمش تحت فشار معیشتی قرار دارند، پایدار نگه دارد. مهم‌تر از همه، همتی اذعان کرد که صادرات نفت ایران تقریباً متوقف شده و کشور با کمبود ارز، هزینه‌های بازسازی و افزایش بیکاری جوانان مواجه است.
این اظهارات را می‌توان نشانه‌ای از شکل‌گیری یک کارزار هماهنگ در بخش میانه رو جمهوری اسلامی برای مهندسی افکار عمومی جامعه ایرانی در جهت باز کردن دوباره باب دیپلماسی و فاصله گرفتن از فضای پرتنش کنونی ارزیابی کرد.</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/20099" target="_blank">📅 12:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SBoxxx/20098" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4df224890.mp4?token=gLu7y_tDfSS89Kb5ZYup2bZbX1GsLyyAuXRQMBhUcfvUmUHV8VR-YV-Ufp0U0ryxECkQBMOE-7psdr8HrQeAWj2Wlwm1zaMkDpnceMdQ1xK5a9yFIMFukv1vxs2m0OMmlKfvSFeVNiBRL75Yj5B2vJQDwk0f9U6n_fStKoStkcD8GTx3g2Z3KlNGG8ZSBUu2NIbFURWh9FPUM-kO6p0ztqI6pPOg4XR8y54Ly8vnt0TwxgezogfBMLIqZ-j4QzHae1gVPLV1rm-AuuPvX0cSD0uyggR3LEuanrl4Eh5V6ghAx22fPj2Z-RfCfp5EhcSSMkwvqVrqI8oq_oq_9xDkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4df224890.mp4?token=gLu7y_tDfSS89Kb5ZYup2bZbX1GsLyyAuXRQMBhUcfvUmUHV8VR-YV-Ufp0U0ryxECkQBMOE-7psdr8HrQeAWj2Wlwm1zaMkDpnceMdQ1xK5a9yFIMFukv1vxs2m0OMmlKfvSFeVNiBRL75Yj5B2vJQDwk0f9U6n_fStKoStkcD8GTx3g2Z3KlNGG8ZSBUu2NIbFURWh9FPUM-kO6p0ztqI6pPOg4XR8y54Ly8vnt0TwxgezogfBMLIqZ-j4QzHae1gVPLV1rm-AuuPvX0cSD0uyggR3LEuanrl4Eh5V6ghAx22fPj2Z-RfCfp5EhcSSMkwvqVrqI8oq_oq_9xDkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام وضعیت</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SBoxxx/20097" target="_blank">📅 11:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.   این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد…</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/20096" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مدیرعامل شرکت نفت ستاره خلیج فارس از عملیاتی‌شدن استفاده از متانول به‌عنوان جزء اکسیژنه در ترکیب بنزین تولیدی این پالایشگاه خبر داد.
این تغییر می‌تواند برای بخشی از خودروهای موجود در بازار، به‌ویژه قطعات لاستیکی و پلاستیکی مسیر سوخت، ریسک فرسودگی زودرس ایجاد کند.
به گزارش شبکه اطلاع‌رسانی طلا و ارز، مدیرعامل شرکت نفت ستاره خلیج فارس روز جمعه ۳۰ مرداد ۱۴۰۵ (۲۱ آگوست ۲۰۲۶ (۳۰ مرداد ۱۴۰۵)) از
افزودن متانول به بنزین
تولیدی این پالایشگاه خبر داد. به گفته او متانول در حال حاضر به‌عنوان یکی از اجزای اکسیژنه در ترکیب سوخت مصرفی خودروها به‌کار گرفته می‌شود.
اکسیژنه‌ها ترکیباتی هستند که به
بنزین
اضافه می‌شوند تا احتراق کامل‌تر شود و عدد اکتان سوخت افزایش پیدا کند. عدد اکتان بالاتر یعنی سوخت در برابر خودسوزی زودهنگام در موتور مقاوم‌تر است؛ همین ویژگی باعث می‌شود پالایشگاه‌ها از این نوع افزودنی‌ها به‌جای ترکیبات گران‌تر مانند MTBE استفاده کنند.
چرا متانول نگران‌کننده است؟
متانول
برخلاف بسیاری از افزودنی‌های رایج، خاصیت خورندگی بیشتری روی قطعات لاستیکی و پلاستیکی سامانه سوخت‌رسانی دارد. اورینگ‌ها، شیلنگ‌های سوخت، دیافراگم پمپ بنزین و برخی مخازن پلاستیکی از جمله قطعاتی هستند که در تماس طولانی‌مدت با متانول، سریع‌تر از حد معمول فرسوده می‌شوند. نتیجه عملی برای مالک خودرو، احتمال نشتی سوخت یا کاهش عمر همین قطعات و افزایش هزینه تعمیر است.
کدام خودروها بیشتر در معرض‌اند؟
خودروهایی که سامانه سوخت‌رسانی آن‌ها برای درصد بالای الکل یا متانول طراحی نشده، بیشترین آسیب‌پذیری را دارند. این گروه شامل بخشی از خودروهای مدل پایین‌تر و برخی خودروهای وارداتی قدیمی‌تر می‌شود که استانداردهای سوخت انعطاف‌پذیر (فلکس‌فیوئل) در آن‌ها رعایت نشده است. خودروهای جدیدتر با قطعات مقاوم به الکل معمولاً ریسک کمتری دارند.
مدیرعامل
ستاره خلیج فارس
تأکید کرده است که درصد متانول در ترکیب بنزین در چارچوب استانداردهای مصوب کنترل می‌شود. با این حال، جزئیات دقیق درباره سهم متانول در هر لیتر بنزین و نظارت مستمر بر کیفیت آن، اطلاعاتی است که مصرف‌کننده هنوز به‌طور شفاف در اختیار ندارد.
استفاده از افزودنی‌های داخلی به‌جای واردات ترکیبات اکسیژنه، برای پالایشگاه‌ها از نظر اقتصادی مقرون‌به‌صرفه‌تر تمام می‌شود. این رویکرد در سال‌های اخیر در چند کشور دیگر نیز با هدف کاهش وابستگی به واردات آزمایش شده، اما همواره با هشدارهای فنی درباره سازگاری آن با ناوگان خودرویی موجود همراه بوده است.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20095" target="_blank">📅 11:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این موشک های دوش پرتاب حرارتی صرفا برای زدن بالگردها، پهپادها و هواپیماهایی که در ارتفاع پایین پرواز می‌کنند مناسب هستند.  به نظر می‌رسد هدف از تسلیح ایران به این سلاح ها، ایجاد فرسایش در نیروهای آمریکایی است که محتملا در حمله زمینی به جنوب ایران درگیر خواهندشد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/20094" target="_blank">📅 10:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ:  آیا تا به حال کمونیست شاد دیده‌اید؟  آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.  ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20093" target="_blank">📅 03:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ:
آیا تا به حال کمونیست شاد دیده‌اید؟
آیا تا به حال دیده‌اید که یک کمونیست بخندد؟ من هرگز چنین چیزی ندیده‌ام. من با کمونیست‌ها آشنا بوده‌ام. آن‌ها افراد بسیار ناراحتی هستند.
ما می‌خواهیم شاد باشیم!</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20092" target="_blank">📅 03:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سفیر ایالات متحده در ترکیه، تام باراک:  اسرائیل هنوز جولان را در اشغال خود دارد، برخلاف قطعنامه‌های سازمان ملل، برخلاف کل نظم بین‌المللی که جولان را متعلق به سوریه می‌داند.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20091" target="_blank">📅 03:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20090" target="_blank">📅 03:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20089">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سفرای ترامپ مثل خودش متناقض حرف می زنند.  سفیر ترامپ در ترکیه یعنی تام باراک از اسرائیل شدیداً انتقاد کرده بود اما سفیر او در اسرائیل اینطوری قضیه را ماست مالی می کند.</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20089" target="_blank">📅 03:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20088">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانم با چه کسی در ایران مذاکره کنم. این واقعاً یکی از بزرگ‌ترین مشکلات من است.
هیچ‌کس نمی‌خواهد رئیس‌جمهور ایران باشد. می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور باشد؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور باشم.»</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/20088" target="_blank">📅 03:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20087">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشگر: با توجه به اینکه ایران به سمت جنگ اقتصادی پیش می‌رود، آیا این بدان معناست که گزینه‌های نظامی برای ایالات متحده محدود شده است؟
ترامپ: خیر، اصلاً.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20087" target="_blank">📅 00:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20086">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">روسیه برای اولین بار در بیش از یک دهه، هیچ کشتی جنگی در مدیترانه ندارد، زیرا مسکو کشتی‌ها را برای محافظت از تانکرهای نفتی تحریم‌شده از دستگیری توسط ناتو منحرف کرده است.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20086" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نماینده مجلس  ابراهیم عزیزی:
آمریکایی‌ها ثابت کرده‌اند که زبان دیپلماسی را درک نمی‌کنند، بنابراین نه تحریم‌ها را برمی‌دارند، نه منابع را آزاد می‌کنند و نه به دزدی دریایی در دریاها پایان می‌دهند.
اما تاریخ نشان خواهد داد که با زبان قدرت، نه تنها به این اقدامات مجبور خواهند شد، بلکه منطقه را با عذرخواهی از ملت بزرگ ایران ترک خواهند کرد.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20085" target="_blank">📅 19:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">افزایش تنش ها میان اسرائیل  و ترکیه    دولت ترکیه حکم بازداشت نتانیاهو را صادر کرد.  دولت ترکیه درخواست صدور اعلان قرمز اینترپل را برای بنیامین نتانیاهو  به دلیل جرایم علیه فعالان ناوگان جهانی "صمود"، از جمله جنایات علیه بشریت و نسل‌کشی، صادر کرده است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20084" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:  به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.  به نظر من، این بیشتر یک هشدار بود تا تلاشی برای…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20083" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اظهارات  هاکابی، سفیر آمریکا در اسرائیل، درباره حملات اسرائیل به سوریه:
به نظر من این کار عمدی نبود. اگر به آنچه واقعاً اتفاق افتاد نگاه کنید، تعدادی از مهمات در یک فرودگاه قرار داده شدند. هیچ تلفاتی نداشت.
به نظر من، این بیشتر یک هشدار بود تا تلاشی برای ایجاد تنش.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20082" target="_blank">📅 16:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اخبار تاییدنشده از حرکت انبوه نیروهای زرهی و توپخانه ترکیه به سمت سوریه</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20081" target="_blank">📅 16:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترکها در ظاهر می گویند اردوغان موفق شده ترامپ را متقاعد کند تا از این طرح جلوگیری کند اما به نظرم این پلن A شان بوده و پلن B شان شامل ورود مستقیم نظامی به ایران همراه باکو برای اشغال شمال غربی ایران بوده که پیشتر اشاره کرده بودم.  در هر صورت، در راند بعدی…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20080" target="_blank">📅 16:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دولت باغچلی، سیاستمدار ملی‌گرای ترکیه، نسبت به حمله هوایی اسرائیل به پایگاه هوایی در سوریه، هشدار شدیدی صادر کرد:  وقتی ملت ترکیه قیام می‌کند، هیچ نیرویی نمی‌تواند در برابر آن مقاومت کند.  ترکیه، کشوری نیست که در برابر حملات به حقوق حاکمیتی خود، منفعلانه عمل…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20079" target="_blank">📅 15:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-text">🔥
نفت ایران در بازار چین کمیاب شد و تخفیف منفی!
🔹
رویترز: پیشنهادهای فروش نفت ایران به خریداران چینی کاهش و قیمت محموله‌ها افزایش یافته.
🔹
برخی محموله‌های ایران به‌جای تخفیف معمول، با قیمت بالاتر از شاخص برنت عرضه می‌شوند.
🔹
صادرات نفت ایران در ماه جاری به ۵۳۴ هزار بشکه کاهش یافته؛ در حالی که میانگین صادرات در سال گذشته ۱.۴ میلیون بشکه بوده.
🔹
همچنین ذخایر نفت ایران روی آب از ۱۰۵ به حدود ۸۰ میلیون بشکه کاهش یافته و پالایشگاه‌های مستقل چین برای تأمین خوراک به دنبال نفت جایگزین از کشورهایی مانند عراق و برزیل هستند.
@khate_energy</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20078" target="_blank">📅 14:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDabaGW4mLtyDAV5e6rvL8w6Jzi7or3HB6LT_yRFROb7HCrZ-LMDZfrlTkxUDON6he32BVkVZsXQkez3_OOzfijGjR-2A4oILYh-Z1x4RzmsFFvvyfdNpZTfOpDIKi4CB7lGZV5RQYSvmsyZHI-F4vXYaJ9W1-fudQUlkFZ1BlRudybo_nf_IOQoDcmtMI_mBa3TCMyJvbC8qR_sFzn95Os90OrBUHG0M_PU-vL6vEPahAWC95brw1U-HH_54b1T4_-SjWWkzjZxzO2ilyQAAKZVFnUJCqLb8YcpMGCeA_dwf4VP2Vzj8XMOYBBppS2wzjMU2AMNZHToTno3AVmoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعات استخباراتی اسرائیل حاکی از آن است که ترکیه در حال آماده‌سازی برای ارسال سلاح‌های تهاجمی و دفاعی به سوریه، از جمله سامانه‌های پیشرفته دفاع هوایی، است</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20077" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWcJyjGBlJ8Im5_Gap5IzTpR9UgneQ0GO7aQ6qvhLI29BNM6CljEgraH14EuRZA08rSkaMkweJ7ODo3ZvGefAHOL3-aIkgOKRpFZhccF3P8KdRqsbmxSC9XY_hkY-1jEhcTo1qjuokQ2XtBTRFtHrwIJOG6TKy9-5k-EMEspsN-1EiGXUm9OkprAo-TkNFRUtkxpUH9Fwoysud0QSD6VB87LJkzhxRN5j_IJ2JYAgmoU57D_UWIurC5Br0YBBR660CdnigHaBjKvadodWuwzv2E9lremsL6H964vLqKrD6oq82ASRks7YWwJ7O0U7cHbVPMm5QeTri9FZVgiWmtQVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بالایی قرار دارد و پیش بینی می شود طلا یک اصلاح نزولی دستکم در حد 300 الی 500 پیپ داشته باشد.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20076" target="_blank">📅 13:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">– طبق گزارش رویترز با استناد به داده‌های کپلر، تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند همچنان در محدوده تک‌رقمی است.
فقط ۷ کشتی در روز پنجشنبه از تنگه عبور کردند که ۴ کشتی وارد و ۳ کشتی خارج شدند. برخی از این کشتی‌ها از مسیر ایران استفاده کردند، از جمله یک کشتی بزرگ حمل گاز. هیچ کشتی بسیار بزرگ حمل نفت خام (VLCC) در هیچ‌جا دیده نشد.
ترافیک در تنگه بابرالمندب نیز کند شده است؛ به طوری که تنها ۲۳ کشتی در روز پنجشنبه عبور کردند، در حالی که این عدد در روزهای سه‌شنبه و چهارشنبه ۳۴ کشتی بود.
این در حالی است که ترامپ و اکسیوس ادعا کرده‌اند که روزانه ده‌ها میلیون بشکه نفت با هدایت ایالات متحده از تنگه عبور کرده و به بازارهای جهانی رسیده است.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/20075" target="_blank">📅 09:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">- یک مقام ارشد ایرانی اظهار داشت که ایران در حال آماده شدن برای آسیب رساندن به ریاست جمهوری ترامپ از طریق جنگ اقتصادی است، با هدف اینکه او در انتخابات میان‌دوره‌ای نوامبر شکست بخورد.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20074" target="_blank">📅 08:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20073">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اطلاعات استخباراتی اسرائیل حاکی از آن است که ترکیه در حال آماده‌سازی برای ارسال سلاح‌های تهاجمی و دفاعی به سوریه، از جمله سامانه‌های پیشرفته دفاع هوایی، است</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20073" target="_blank">📅 01:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20072">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1CQtyg0UJnq7GQajqlQSMtOOjzJoe2BPliGW-eE07bW86urmqOZJaQFBSVs0CUf0_25xrwllDxe4CXsp6b9_wMYuE1Q15DOsPuloE6LKtJr9iXT3s9rTjzkHDOSTKnP5dckukDRtk4OODezUrvkrdcoep62SNjNpgTY5-QDEzyPpe4cGH7I8p_kkY_1CvWdz0bOQwXmLtM9MzSDSkT6IgJNygbnKGM4-E7iLJTs8bZQnoqqltPeyP2QW1e2I3fQIEATWjyaoAmeV--dZ-mBEB5Li-8CNDqxTi-qqcJ7si54CYCfc9tC7OIu57fxyKanqmcDXen55uetvXglF2IuyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلن ایر دیپلمات سابق ارشد آمریکایی خطاب به ترامپ</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20072" target="_blank">📅 01:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اظهارات معاون رئیس‌جمهور، جِی. دی. ونس، درباره ایران:
ما اکنون در یک مرحله جدید قرار داریم که موثرترین ابزاری که در اختیار داریم، فشار اقتصادی است که می‌توانیم بر آنها وارد کنیم.
این یک تعادل ظریف است، زیرا ما فشار اقتصادی بر آنها وارد می‌کنیم. آنها نیز تلاش خواهند کرد که فشار اقتصادی بر ما وارد کنند.
اما آنچه در چند هفته گذشته صادق بوده این است که آنها احساس فشار بسیار بیشتری نسبت به آنچه ما تجربه کرده‌ایم، داشته‌اند.
ما این روند را ادامه خواهیم داد، زیرا معتقدیم که این بهترین راه برای دستیابی نهایی به هدف مورد نظر است.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20071" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20070" target="_blank">📅 23:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20069">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBNZARFIC1oxJoDWFkH-pDt49wsnDdVBg-J7v02X9hevxCRfvHQzsn3gpP9cBodpIgtYunVYRcQ3XM5ypp65vVZkcN6qdBs8-7uBgT53EoHp4P0EgQmDvImboW108kv1wwiudf1h_aJiuEZHlE_TOnP4cMtNKnpUkkbt3KnQmRFClaNpoZNc_j2mNdRP-mWlEtX1dH2wAAaUYvFisj-pAiXIdiDgJeFc9Chm8fkoGP7snAbI9Z0W5tl3_vuWSG6IOgppQ_rHFHC6JFNTImx2FnitHgJ4IdEbYAEY17uCH6nsAZzZEbUeD8Yr7hNhcnrFjC7EDUCwVh_h_DE-F3P-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20069" target="_blank">📅 21:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20068">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایالات متحده آمریکا تحریم‌های جدیدی علیه حزب‌الله اعمال کرد و آن را مجدداً تحت یک قانون مربوط به تروریسم طبقه‌بندی کرد تا بر پیوندهای آن با نیروی قدس سپاه پاسداران انقلاب اسلامی ایران تأکید کند.
واشنگتن همچنین ۱۰ نفری را که متهم به قاچاق پول نقد برای حزب‌الله هستند، تحریم کرد.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20068" target="_blank">📅 21:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چین می‌گوید تهدید رئیس‌جمهور ترامپ برای آغاز «جنگ اقتصادی» علیه ایران و شرکای تجاری آن کارساز نخواهد بود.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20067" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20066" target="_blank">📅 20:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20065">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ضرغامی:   از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20065" target="_blank">📅 19:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20063">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ضرغامی:
از اول انقلاب تحریم بودیم ولی کشور رشد کرده، پیرزن رو از تاکسی خالی نترسونین!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20063" target="_blank">📅 19:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اسکات بسنت وزیر خزانه داری آمریکا درباره ایران: «ما این رژیم را سرنگون خواهیم کرد»</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/20062" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حوثی‌های یمن اعلام کردند که دو حمله پهپادی را علیه فرودگاه ابها و تأسیسات آرامکو در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20061" target="_blank">📅 17:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">— مرکز فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد که گروه ضربتی ناو هواپیمابر یواس‌اس جورج واشینگتن به خاورمیانه رسیده و اکنون در منطقه مسئولیت خود عملیات می‌کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20060" target="_blank">📅 17:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئیس مجلس عراق در واکنش به این عکس قالیباف، از خود عکسی منتشر کرد که در پشت سر او، بجای خلیج فارس، نام نجس خلیج عربی نوشته شده!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20059" target="_blank">📅 16:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF_QNUIYCKGFS-7em5XnB-6_s7aNzTWCp6FPsa4kMP5n02-Rm85nx5kisPtRPAtW0aMdVvC-vtw_VtTHBva1e-7OJczkFhWUY3B1LS-4LmhTh0yR61uJvQEl6QXnAp-EZTTehUADqxJNcAiBp5FGELI2WIgID2IPZ7q6wLcSNop7-9PI5EQTdueozUCuNVg6BqnaQB64MV4J6GpMoVbWcmQmq7hBUqB2mkjTsR3NyrAS9-K3cstCfZcBJRU1Br3N4SBoIPT8l_qsfQkCMBn1Lu20R-3g-czqXCc35etQmjqmwEmP_Kouh3I38gU2RH7MYr8RtXuUTUqJP1khheeSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!  انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/20058" target="_blank">📅 16:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اردوغان: «ترکیه در دامی که نتانیاهو برای سوریه چیده است، نمی‌افتد»</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20057" target="_blank">📅 15:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اردوغان:  «توافق مکه» علیه هیچ کشوری نیست و تمام دولت‌ها می‌توانند به آن بپیوندند  نباید این توافق را به بعد نظامی محدود کرد، زیرا هدف اصلی آن تقویت بعد بازدارندگی و امنیتی است</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20056" target="_blank">📅 15:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.  انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20055" target="_blank">📅 15:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAEdhspgWt3JStQiLkmrgFNGEygofsf7k-Eg4bktyAXQ6QtFTpOsyIULtcHmM4Ma6bWMxJFH1iqzdoCX2tUQNQmLvZFAIypb8WtTeNkbZErZvtGZx6UXPzHRWIBkIFldAJczj6fwfWvLxoU4xuAapEMSCzlCCfyx4H57jscYnkov1Eo2Oc-OioR9GUhSjgcpThPkfoqlNrRb-0VdKCgFib-9ZTaWzOTjKmBvZ2IfJ8o8UgadXOx8rNhfVKmOAJFrYMugvurhGnjCkN4SzmPIq2_jcMLfgzvn-NGQu8qmmp3wvaVydgaUmEuK14UW9hWrG1JtXPgAKHvckgsS5w7drQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله این چه فیگوری است دیگر!
انسان گمان می کند که نعوذبالله دارند با کله نورانی شان روده بزرگ کشورمان را کلنوسکوپی می کنند!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20054" target="_blank">📅 15:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بفرمایید:  ‏ فواد ایزدی: اگر ۲۰درصد نفت دنیا را حذف کنیم؛ اقتصاد آمریکا فرومی‌پاشد!  با این کار نفت ۲۰۰ دلار خواهد شد؛ باید تصمیم بگیریم که تاسیسات نفتی منطقه را طوری موشک باران کنیم که دو سه سال برای بازسازی زمان بگیرد. ‎</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20053" target="_blank">📅 14:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نه دارو داریم نه بنزین نه برق نه نت نه گاز با تورم 300 درصد و رشد اقتصادی منفی و ریاست جمهوری دکتر پزشکیان و 2 جنگ بزرگ در 1 سال اخیر با گرمای 50 درجه تابستان و سرمای 20 درجه زیر صفر زمستان اما دغدغه جوان ما این است که رامین رضاییان به آن دختره چی دایرکت داده!…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20052" target="_blank">📅 14:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20051" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20050" target="_blank">📅 14:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXAgN2lQFYs9wgZLMmSDcFg3QkQRTgXO6ShVi0-jdoVKVONrP5yo2l9h0vMzxsXM_e70a6r3bnn75rSD1P_vaPY7-op-gSjO1_03OxAj9Jz8Ycb_39A9Z4kMLbOE_PApDiQ9nUb3PrQjEH7VoneRtADLSNAVhiOZR7RJSEDcZ2mWrwCRxeDqs0DnYxFNEal8a89oH-pcQ0Vwu6qZZrZhz4mz-75_YmMdjPFBj9e1j86lIMBsxoUxlVSwW05vV2o1ZQXoHV817_S-Y2L7o9DcUJB3vNs16fO1LApi9ybPqYOD-kVz4uwoa3IrgziHV3eo0Jg3zFANJ0OdcEocCDHRNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثه برای یک نفت کش در خلیج عدن!
به نظر می رسد حوثی ها تصمیم دارند کشتی را بدزدند.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20049" target="_blank">📅 13:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اگر آلمانی ها به جای ما در این میهن اهورایی می زیستند تا الان نسلشان افتاده بود.</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20048" target="_blank">📅 13:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">طبق داده‌های دولتی، آلمان در این تابستان ۱۴۰۰۰ مورد مرگ ناشی از گرما را ثبت کرده است</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/20047" target="_blank">📅 13:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📌
وخیم تر شدن وضعیت صنعت آلمان در اثر جنگ خاورمیانه  صنعت آلمان که پیش‌تر هم تحت فشار بود، با آغاز جنگ خاورمیانه، افت تولید صنعتی، کاهش رشد صادرات و افت محسوس مازاد تجاری در مارس، وارد وضعیت ضعیف‌تری شده و احتمال بازبینی نزولی رشد اقتصادی سه‌ماهه اول را بالا…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20046" target="_blank">📅 13:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:  «ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.  ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20045" target="_blank">📅 12:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نماینده مجلس ایران، ابراهیم رضایی:
بهترین پاسخ به تشدید جنگ اقتصادی توسط ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است.</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20044" target="_blank">📅 11:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سخنگوی سپاه پاسداران انقلاب اسلامی:
قدرت تخریبی سر جنگی موشکهای مورد استفاده در موشک‌های جدید سپاه، بسیار بیشتر از سر جنگی هایی است که در جنگ‌های قبلی استفاده می‌شد.
اگر جنگی آغاز شود، سلاح‌های ما در تمام جنبه‌ها کاملاً با گذشته متفاوت خواهند بود.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20043" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20042">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcZyiFKlHeZ3cJKDU2toAARDrRTSpeLzynOxPUgaSxDKG2BW8Gvh8yiYeAZr3ODbF7R0-qGM2NO1nBLV8oSwBm8tMHClm9mcB4yxXiftn70IfiTZeg-i9xLBXmfprPzJR3IFnxh6GVlXH8OilLsMYAGLXJ90BHss5K-u7G3LUQbcrf8888506pSh7NRngcBIvXz1mPxEECG9Ni16pb1PnXHGYi1VkMXrxBA_XK8i9lzC_vNyfMYWStVT3B9A15JqGWdf7kML2cMBOdPeZDz7NeTEG1PxvMf8Qy0mkMmVA9EUCxwHKC-YaWcnWwGaF1-8i8iq6zntv-EPPE5_r9lrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در بالاترین سطح خود قرار دارد و تقریباً در چنین شرایطی محال است که امروز شاهد سقف جدیدی در طلا باشیم.
انتظار افت دستکم 400 پیپی دیگر در طلا دارم.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20042" target="_blank">📅 11:27 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20041">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20041" target="_blank">📅 02:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20040">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20040" target="_blank">📅 02:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20039">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SBoxxx/20039" target="_blank">📅 02:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20038">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ:  هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.   بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا…</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20038" target="_blank">📅 02:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20037">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ:
هیچ‌کس به جمهوری اسلامی ایران فرصت بهتری برای توافق نداده است، به اندازه من. و متأسفانه، آنها نتوانستند از آن استفاده کنند.
بنابراین، امروز من جامع‌ترین تحریم‌هایی را که تاکنون علیه هر کشوری اعمال شده است، اعلام می‌کنم. این یک جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی آنها نابود شده، نیروی هوایی آنها نابود شده، کارخانه‌های نظامی آنها ویران شده، پول آنها بی‌ارزش شده و کشورشان در آستانه فروپاشی است.
علاوه بر این، من امروز اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع حمایتی از ایران ارائه دهند، با عواقب شدید اقتصادی روبرو خواهد شد.
قاچاق نفت، خطوط مبادله، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی - همه اینها باید اکنون متوقف شوند. خودتان می‌دانید. این یک روز اقتصادی محوری خواهد بود و ما به همه متحدان خود نیاز داریم تا در کنار ایالات متحده بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها در آستانه فروپاشی هستند و این اقدامات تاریخی آنها را فلج می‌کند و توانایی آنها را برای گسترش ترور در سراسر جهان از بین می‌برد. ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع متشکرم.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20037" target="_blank">📅 02:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20036">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: من خردکننده‌ترین عملیات اقتصادی علیه ایران را اعلام می‌کنم</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20036" target="_blank">📅 02:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20034">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExciton Computer Missile Program</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=GbsqF9aRGGrtVca-8EEaiNr8hz9vGNJMupnQpwB6bX7H2QRHOVHhDnfGQx20RfWU7S_VUpthHXDh7US1iAX-PX3OHnKq_NbZACwIJQllyY_X_T8c8ciOd3K2Jx7pWgXQjhZu7Kc-Mp4mEPrfgv7WRr7CwUVlocabNxVWA6t-z1CxWOCK_LE_1Ja8agl0N5hukKrFlSytsXElflYB1rMG8hwJVyZTayA-EBsKcPYELemsHeylA4WVcnbuT1EHADzpY3RO8ikAXYCSSB8SWfFd0ZkfohxfftEvroNNHXxgihHS33Q0QT-beLE3sFIcV1LdEA5ZpatcHK0UJsAjigMAgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da68894d0f.mp4?token=GbsqF9aRGGrtVca-8EEaiNr8hz9vGNJMupnQpwB6bX7H2QRHOVHhDnfGQx20RfWU7S_VUpthHXDh7US1iAX-PX3OHnKq_NbZACwIJQllyY_X_T8c8ciOd3K2Jx7pWgXQjhZu7Kc-Mp4mEPrfgv7WRr7CwUVlocabNxVWA6t-z1CxWOCK_LE_1Ja8agl0N5hukKrFlSytsXElflYB1rMG8hwJVyZTayA-EBsKcPYELemsHeylA4WVcnbuT1EHADzpY3RO8ikAXYCSSB8SWfFd0ZkfohxfftEvroNNHXxgihHS33Q0QT-beLE3sFIcV1LdEA5ZpatcHK0UJsAjigMAgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حمله امشب به کیف این احتمالا موشک اسکندر نیست. این احتمالا موشک بالستیک سری KN کره شمالی است که با سرعت بیشتری روی هدف فرود می آید. مانور pull-up شاید کمتر باشد. اما باز هم زاویه نزدیک به عمودی و تیز را مشاهده میکنیم. سرجنگی هم مشخصا بسی سنگین است.
@Exciton_missile_program
🚀</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20034" target="_blank">📅 01:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نیروهای ایالات متحده به‌صورت پنهانی یک کریدور حمل‌ونقلی محافظت‌شده از طریق بخش جنوبی تنگه هرمز را گشوده‌اند که به ۱۵ تا ۲۰ کشتی تانکر اجازه می‌دهد هر شب از آن عبور کنند.  مسئولان می‌گویند این عملیات اکنون تقریباً ۱۰ میلیون بشکه نفت در روز را جابه‌جا می‌کند—که…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/20033" target="_blank">📅 00:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20032">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ:  ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20032" target="_blank">📅 00:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20031">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">— نتانیاهو، نخست وزیر اسرائیل:
«ما حضور نیروهای نظامی ترکیه در سوریه را که اسرائیل را تهدید می‌کنند، تحمل نخواهیم کرد.
ما به روشنی گفته‌ایم که حضور نظامی ترکیه در سوریه را تحمل نخواهیم کرد و به نظر می‌رسد که آنها حرف ما را خوب نشنیده‌اند. بنابراین، ما اقداماتی انجام داده‌ایم تا مطمئن شویم که آنها این موضوع را بهتر درک می‌کنند.»</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20031" target="_blank">📅 22:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20030">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نافتالی بنِت، نخست‌وزیر سابق اسرائیل:  ما ایالات متحده را از دست داده‌ایم. ما دنیا را از دست داده‌ایم.  ما در پایین‌ترین سطح ممکن از اعتبار بین‌المللی اسرائیل، از زمان تأسیس این کشور، قرار داریم.  باید روی این موضوع کار کنیم.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20030" target="_blank">📅 22:22 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20029">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">محمد رضا نقدی، فرمانده بسیج:
ما باید به بازدارندگی دست پیدا کنیم. برای ما خوب نیست که کسی بتواند تصمیم بگیرد به ایران حمله کند، و سپس، در صورت شکست، عقب‌نشینی کند، خود را سازماندهی کند و شش ماه بعد دوباره بازگردد.
ما باید امنیت خود را حفظ کنیم. چه این امنیت از طریق دیپلماسی و چه از طریق جنگ به دست آید، ما باید آن را به دست آوریم. این نکته اساسی است.
نه دیپلماسی و نه جنگ، به خودی خود ارزشی ذاتی ندارند؛ هر دو ابزار و روش هستند. ما باید بازدارندگی خود را بازیابی کنیم.
چگونه بازدارندگی ما بازیابی می‌شود؟ با این کار که مشخص کنیم حمله به ایران هزینه‌ای دارد.
اگر آمریکا این هزینه را از طریق دیپلماسی بپردازد – اگر بیاید و به این درخواست‌هایی که سردار رضایی به تازگی به آنها اشاره کرد، عمل کند، از طریق دیپلماسی عمل کند، غرامت پرداخت کند و بپذیرد که در هر صورت، باید هزینه‌ای را بپردازد – آنگاه به سادگی باز نخواهد گشت و دوباره تلاش نخواهد کرد. این می‌تواند بازدارندگی ما را بازیابی کند.</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20029" target="_blank">📅 20:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایران در حال بررسی حملات به  خارج از خاورمیانه  است   اهداف بالقوه شامل پایگاه‌های نظامی در بلغارستان و قبرس، به‌علاوه کابل‌های زیردریایی در تنگه هرمز است.  مسئولان ایرانی به‌طور فزاینده‌ای تعارض مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حملات به زیرساخت‌های…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20028" target="_blank">📅 19:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20027">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ:  ما کنترل کامل و بی‌چون و چرا را بر تنگه هرمز در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20027" target="_blank">📅 19:10 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20026">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اظهارات ترامپ درباره ایران:  ایران نباید سلاح هسته‌ای داشته باشد. شما می‌دانید چرا؟ چون آن‌ها از آن استفاده خواهند کرد.  ما اجازه نخواهیم داد که آن‌ها از آن استفاده کنند.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20026" target="_blank">📅 19:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20025">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارشگر: آیا قصد دارید مذاکرات را با ایران از سر بگیرید؟  ترامپ: شاید در یک مقطعی، اما در حال حاضر نه، فعلا اوضاع بسیار خوب است. اما شاید در یک مقطع زمانی دیگر.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20025" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20024">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارشگر: آیا قصد دارید مذاکرات را با ایران از سر بگیرید؟
ترامپ: شاید در یک مقطعی، اما در حال حاضر نه، فعلا اوضاع بسیار خوب است. اما شاید در یک مقطع زمانی دیگر.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20024" target="_blank">📅 19:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20023">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIgqN52viZ2Saz1AOpX2CCtVROU2lKZ1g4erOHRdGKiG3Mb0rhKLss3NFkO9hSRHPSoCTKfZ69xl9deIknVWk3k9QgzG-P5UAEtdSodiGh6LC2uO_xmPchS28COEwv3k9Ghzl5E7hS-hn-hzufMBQ4W2RFWWM6kepWqwE8hB4zDwix2HwPJcsO0m_Dxen-RLruTvZvlHcKxoLCMueOij_lLr0Uau--FccNirQQWqmE0ezyjyEQ4JQDrgH8fDmYDTEt6PY4Ta_syPpZh0_9_RA4pjBqwyBCm4h0kFgGXgWvzPRTPzenHM_LT2kPZvrH55j-l-wdZFSjWHCU89y2PM9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درین بازار اگر سودیست با درویش خرسند است</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20023" target="_blank">📅 18:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه پایینی است و برای طلا این موضوع به صورت نسبی مثبت است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20022" target="_blank">📅 16:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارتش اسرائیل در جنگ شدیدی با حزب الله برای تسلط بر تپه های علی الطاهر است که به شهر راهبردی نبطیه اشراف کامل دارند.</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20021" target="_blank">📅 15:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20020" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  ما باید اطمینان حاصل کنیم که رژیم ایران قبل از دستیابی به سلاح‌های هسته‌ای، سقوط خواهد کرد.  بنابراین، از یک طرف، ما مانع از دستیابی ایران به سلاح هسته‌ای خواهیم شد.  و از طرف دیگر، ما برای تسریع…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20019" target="_blank">📅 15:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اظهارات نفتالی بنِت، نخست‌وزیر سابق اسرائیل، درباره ایران:  اگر حزب‌الله به ما آسیب برساند، ما به ایران آسیب خواهیم رساند—به روش‌های مختلف.  هرگونه حمله از سوی بازوهای "اختاپوس" ایران در داخل مرزهای اسرائیل، منجر به مجازات‌هایی خواهد شد که در داخل ایران اعمال…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20018" target="_blank">📅 15:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یک جوری میگویند خویشتن داری کند انگار می‌تواند خویشتن نداری هم بکند  چیزی نمانده برای این وامانده های غارنشین حرامزاده تروریست</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20017" target="_blank">📅 15:28 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
