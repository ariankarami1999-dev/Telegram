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
<img src="https://cdn1.telesco.pe/file/rdq3bGEJ6FAAIGHw8Blxfm2BN7MSeKtVsSsoIqJEqnQqwfdkaNDVVGmC8cG5PbqDwOrR8BN6FV0hWmSVvrRbWqNqxmjz5B4aUnM-QH_6-6H0r93t00L_1vxY_1WioJtBxLfatqKLPwoXqOoxX9BixB9XJQSUjNw_bVRB5lBAjTZS1vgevY7QD7unTGtAy7OshMal7GnuUn_cif0KSdQg1pzbM6Mx68jocpQ-NxO2XiNfEARACeUAgqSJfRTPTh0m5XGfZlCiBX7j5i5o5WY_4_kcM7cj8MzOJopjEOAa2Or-NFbrfNmaPMbe1uiG7ZLeuVhx0M-EDHUz41a3j9bNQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 23:33:12</div>
<hr>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nfJXSxA9dZfjeTEZJmOQgwqTQawlm_Nng6qcj9mj12HIOEdQlO62EQaCE1mayLw4y4F4nZZ6tB5Kuf_F_-oGQ6mV79L7XHXXAlXmpfS7nKKfngddAzJZuwC5jVh6k0lra65bMLuH9ePfjvWvXcaBnjvRj-DwhdXhp-lf77HqS0Mq97BUZMVDs3aXcTFvoo6lkb0L8vfTKhJ0DE3MJw23KCk1UDgNNNmwtwPuNVfE7DujQteu5TZqmRKx0ygh6tLqP2UlsQgi9HL1QBtkzuU0ERW1tpb5qhHAsmsutApxA5jKWO8p5jyfysHlQA9LafcrdIQQnUl7VHjVv0h79djc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MV2dts97hHvuvjFZkq9q-DamRbg15OYlhkk578ohHxdI5nqPCezVJU4OuCqKAdtt3OZtK1kqPB4UeY4iiYviL6nLZFMF9p9doS44zN-9FoV2tv3pQJwR4hyJTXNy5yb2LW5zgaJ3feWojujhbtUTTEy8J3qVOy5aROo6NdZwa3DBkxheRV_B6mkn_BXu20vfsi1UTFD9FiOygG8gfGaoDWNE21Tc7R8Zrmm_5NibdeA-e47RjDR5yAV7rZid2moqCoQKRT0xDpphEU9aApiPIR-gXZcirhicyJxs5Zq4LCMIxwQYdbeBq46VSYTJi8wJ3EnMnwfTi2cJoRBI3DOs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=tP61uUYB7sXLUq1vEpli1wiaJGiadZ1p0ECt908r0gB1Gt8tndPj4x-oPnxwDBphYnG1kx8ZJ-Z9FkBP3xDucB_nFv54Jy4S-NhdgugUZ3QcESpQiCTshcwUlDie3S2F0oNxFjH38rsbFiv6OOtpAq_793R4X4CfM4tJkShGgTnHrbXqFYM332LgkdGp5RGnfjfK1e8jPTMlds4EB-nlF8O4unuNfQX3loWpEvvLnTTCC_7t1pzFV4lxAVIW44q7ez_4FqQA5JKVxZW_KLsb7GR9gvxiRgMY-F3HIH99MKtBuD6WGxMJyeBMF71lZ5hEUzKmas_Y4CRV5j-_AjTo0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=tP61uUYB7sXLUq1vEpli1wiaJGiadZ1p0ECt908r0gB1Gt8tndPj4x-oPnxwDBphYnG1kx8ZJ-Z9FkBP3xDucB_nFv54Jy4S-NhdgugUZ3QcESpQiCTshcwUlDie3S2F0oNxFjH38rsbFiv6OOtpAq_793R4X4CfM4tJkShGgTnHrbXqFYM332LgkdGp5RGnfjfK1e8jPTMlds4EB-nlF8O4unuNfQX3loWpEvvLnTTCC_7t1pzFV4lxAVIW44q7ez_4FqQA5JKVxZW_KLsb7GR9gvxiRgMY-F3HIH99MKtBuD6WGxMJyeBMF71lZ5hEUzKmas_Y4CRV5j-_AjTo0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJXyBYywcCBoMshdRyAd5_nUZLJ0XkWDhFiGfvA-9WIO-9drKlUg0DoLUF_7nEfBqozCdBLJogKv53o8JgPeJoCkJixtnNZjMce7yCygnkWXGq-vZ8GzXahi52uXrDaRzJgS5xp6b8UbXdptKEEfBzk0Tq9YiaMMB2dPjK6foFNqrdZKa891PsLdhRmDJraD9_GU3cEO9j5I5pNMCqkxn8zYFAyBpEuJereVzlFJdJPFO4S5T0KrlOsyGuyomqMLBf6wjdiGzmw_NrPu7bD0yz41KX8lyjWrZrqBPonbIUSlUx_P1KYc7yHZdet9ZyiBmyj9EqtqBZn4Q-ljTmlb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RsYeLetlg66nWEYQ12NtvaPlAA0UBIbj5db6TJ7HTJwM9uNDSZpP5H8g5yOtKAL3RdXL295VXWTOZktXvPVJJCt2dNZ1go0awPpC-qr_lombiBgne-mIqItPYdRZK_-3X7RzW5LGZzCTOgXXfAla7oe8_QztTOCEAN8AgWLikjrYPjf3ScI4R8xXDmESdgxAC6i0rDivMEJAoXdL9x9kwFcX1mGAbngDoZ2H2qoIqwlRsEAOS-hKXvlwrMbReaelpD43bDq-_2rOHWOcsCmDTRVha3UBG4FEWIGumxw6_HlvQ9gU6ogi5MUwWv6Sa85GwyV6lvjYVOQqS5nVBjdHSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUO4XsuFE07ziOgz3uQQGoYlWzGvv2yMrq-ul5IeQMBnyiTCW0EphPl83eLVju1nXA13HUNjPqVsRPFzq6_wAOnw5W3a21nYM55PRd3KHQVx6nRFr7xDcrs30Uy2yzzhWA4sXH1_SXrD2kJ-HBj69cUr6quMwD-pemQ6aD_YuDqanHeQLuQX6w7H7NudePrX1CybPm85fLCZ5FQAvwjk0nRoVsdtaq7MqOnVPKzXQ-P-4UZOQ8-Gyd48anUwo6AEIAWG6BMP_aQ-EqTJiThU8JUm-bBJZxQvahLuG2JJpx1ZG1gCiOP9JELTH4IMrbwy0j0zGB1yDlPXBWbWgnxMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwwnGZ5lBzMNSo_EL8hqGHUjVU2CYV7I2r0JRmdD1-MYTcUeKcFDqecjngFKhcw2GgV1KK9feSe4NjSOpHxtKXnimTtVHotukQuQn2_ILj_moydzcbjqxXEB_dXywp7t-XquvTqpEjS5_k8Y-js4nTWUgqsyxzKdpIgap0XemlgLpqFF6X_ZqfKWcJvnP8nnKLSBfJbvzlzet-lmEfxw5uD4vugdEuMUBwLIqO9lhZ2yUZTccGNXFbMQ4POmt2UR_lkAkx3SOc_x7u8txK8Cng9sFp1EKRim3YtpzTtEip_SkLmsnajekS5rt-L_scrhbhy9vC-LpeudXo8cBokGJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uLiSjtkcox8vEbV_KsSxDZ7yvEezLfteJFfKiEpx1SMugF-aeiqDCdPzbao3cKjZCd8dJkcRpbgxnN8_PMtyIDWhI_SEEol0OWUl1_XwJEce5_nudvt9wMH7ZzBfUfU2KHv2xbUqSnjacaghEF7AepOt9n6IPPfcbKiCV47TXk-Qu9FGN05ASG5H92SVNG9KQiel1NEU0ZXjc3zDc6BGyu9paErcObxmEW28Jb64lkvsOjdFXSoGvHzgSghboWDzQJcSEC7FjXDqQ4Pa7iLfShWzm0uZg6Ot9wWofcya7IDQtGuExHkVis-pwVolJ7_3Uk4XPSxbxmjLStFVyCby-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iWnRXAE31XV3KWDtoOXFg4mLW1aayPsjzxil8WY-wfEaMIVh0MclYPHz5jtlvQ7YNxILC5KM2g2xExkgF3CtsKDnhm08vVMIDx-jTq8ezsYQWPEAR1uKUi6Qin_F44sv47pK5PXVJUnA-Zez5V1appN_dGSeaTB30No_emPboQWgTrYysjMxzkEb4PEHzAi4R-JxKq17ZJhW5xakXa57Jxcu75hjaTh87J5Ky5wCwbZTKQ4t9WaEZFWqg6jrLnFrUATUwVhtVcZGqA6Hv0RymknGNKfQLjFKF6f_pf2i1visPm5sjJhi7hKRSwpG_Wp-1QoM36A3wc2OKYPERRjlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gh-O75f_X75xrDOV7hxvQmUrEGjEgAFTy89EATvwk2WdeCI0r9HT-SxaUjdl6rYxVgJ5q4dUVtfr6RHC1xCVeVAv2wJDyZ0amLz4AVx4upgWi9EdYUwx8mwp4UdZ2a2Ggm5S1UTyzTxqZ8FQn05Y8favI1n4y0KBgX5jwn5UHr3jYJcNorQ1s6_Ur8GdymkDrbixgEwXtGvFqEHyUxKB7SLvHbLEDUJ69lCGH2hFnKRyr1P1MhcrFS7rkLCfWL2SV6vVaq7e1Q10JCSDdo2dQiu7NWhiQlnq6YOdm7yOtVdPaTxqXzciHB4as426mSm4SpBcT3-BGsOf_P4M6Bq2TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NC1eqACPYL2PVgcrVVKyWTLZVpNbLxM_BLqgM6cj8sTUxaFBRlXfWetQi_bir21r_N7zwPW0nL1YAAHpkTd9gL7h3gAX_861OUXTHuMDM6cCyBOw3DSCIBkmRUg28Xwpmj0B440KKeDI_wUeAFA3lIWm8PSNxuWvct68VkwrJWeRvoS7zOYfolenSERE8HuGgyGnCpY4rQULKvYqaSupYu3siS42ZL2GbXfd6hCScDdmSjdqfXshz1IDLsplct6eeW1xkibD2MRpiN7xE32Iw_bOxYVL-WAwomQEpb6RDbWUcqBA8RnQir8_NE-gPorLhdI21Z93SPLXn_TbDD146A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gmp-i2r0I50tAOy9FFigjtWybH2oyp6m7dDrjb1-TiWT8uLuH9MC77d4SXO1JFNBi6RcDBDUVCbEt7HyroozdxeIJUyPzeYXA44V88mAWCUJkslRq1hQAhNUPKcxci386AsFAop2tJpEBZkBciRUm5jvjCno5ABqKVH1kt84YYjIsXEHFeQKK8ygl21BPgqQFFwjLJf-P0GsfzSO7hlWWRYqY2dIWverziYPJ-EsuklPi1BILkgpiOZ1aiY88SC4x4_YO-EZr3IY1VV3rrro5B96Od_tyoHr5GhQF3wcQyxavClCk_9_BtuxXxnwG_fBJ1U1i6_ZYRXkJLFj68hncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/atgCqAOt-9K5H1N6rRPd-lPfSyXL90hIDGtQ6qD-jizTcc-6g-ABFL268_9FdTYP2PCHQdk8HCQiezltUgf6h37fW8GIz03CjYYhDw_uOAwuoOOVG2mlkyy9lBSSHAJLWnPHLeOb8Q-NdzNkego4zDKEQ1QONdDcx-vRa-bmOvPVhNgbhdnQx-GxDD0plnAmSj9gZcexRm3N2pLPF1WClCECrPkmaBuFOSNd5EADWAHl6S9ahQY2V79tiPIibbe7dYcrbeFQ_Siv0BB_kMPKyBuFpc-naWwusiwi4U7cWwLTwbwtqL8Piv34VilQVYc5c_Zm-ZP2TTUgrBxtaxqTaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U0puHkuTOhx4RpCPolXzXwtRW-H9AyzIVmS_JgUUeCYeAmZ-7y0u0jhljWyAkROBoxnqlKvtnT98uV0-iDbU1IBOOJ5PTxBSOJTEDW6cSFMtCYoBkeSo2iCNoSSncE1Ild0oHZFc-5nh7w68EgaiG7a1YaTol_GCykeLCyJppdcmxyeS0SJN7wgFDgZhwKRTbVApWu0q51HypFwdRUmfxD-6nR_m4E9y7hzQtvJbi14SvBz-kbgPLMX3DBtCvtbm688hqjVax3z8g8Y7X5cvKsXxt7aNbwDUFdz3n20yEoWqNnEkXbyLQ8QCIptTkVkUfDCD8suRwep84Imdcz-Tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=L3x0Zu4yTy0SbQfaLMNnnNJZMAxXwJXtlk7KbgRdzSaHhBCU2mhAjtscYnBZis4jaBO9OmXXZnHdalGbynW0oTyIfflKhFeUBOWei6ye7AQYL79FbhaGQJnM93KeN0FGJeArl_8WQGsGjbVJ3i32r7aNtugOY-TiAi_n2yuKuSEqtBlaeUM8MKe9JJ2uUD6wfgDlZRzqAfHBa5pPEdn-M-BQryYVEYEad8gTlX6EA59N85nmsA2t3HJ1itphcmYVQTkR6TUGdVmzT-Epul4txRnWPm5jnhp8Bk_J7drPjGEdK7-Sb6xxsMVcUiuYJCMBJUorlQnnlUUA6a2s_dnW6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=L3x0Zu4yTy0SbQfaLMNnnNJZMAxXwJXtlk7KbgRdzSaHhBCU2mhAjtscYnBZis4jaBO9OmXXZnHdalGbynW0oTyIfflKhFeUBOWei6ye7AQYL79FbhaGQJnM93KeN0FGJeArl_8WQGsGjbVJ3i32r7aNtugOY-TiAi_n2yuKuSEqtBlaeUM8MKe9JJ2uUD6wfgDlZRzqAfHBa5pPEdn-M-BQryYVEYEad8gTlX6EA59N85nmsA2t3HJ1itphcmYVQTkR6TUGdVmzT-Epul4txRnWPm5jnhp8Bk_J7drPjGEdK7-Sb6xxsMVcUiuYJCMBJUorlQnnlUUA6a2s_dnW6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRJsaL9HjQXaRWKKPQZBfW8G7_XzJfSJuwH1wXHxV8v6PqbmzgzU_VJTQ_9083BNijNuBCpo8InWYcEDYuJBxffycdrxffGjrvHrQYcV_BKcIHuYBVZBnZW717sAVTO-4wpWU_M3zRvcsVW9R1Pbd3jr4SmdaHqLwRmQyuW4GATx7vCCnPFTEYdLgRmyG6Ynqu2VPlZbK-rQCHoIIP399YmFTkhwijSEByCKjpcaMs1Ie7GqGBwi03n71Bsxcsjd1Rhdb4DpQFTrMOho0WEurKUeOb69wB8BGCeH1XmDOA1StAY9EC72Y3oIdfLMR-1bcIStIO24BMDUiScV5IftKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FUDRHrlvL4l16v7BcC1MwbbOFL39AT_1yR3P6tVUlrgSvsYICYn_jZI-PohXZ7ALZuUpA7bv0yHcI2AS1la4ruBcXUVSkfCd-Nsz11Hx74lWNXaadoejEVWxtdDV5jFkDuqcPJzCQXmtDQr5gyuO0GJMfpJWjG65m_sgAcOufwtvE9YfnPZyjGzgKC86eYANulSiGHealYSzkxI_LGpJh0R-LEQNHafx2R8ng2YU2hvm3dJTXECaESAKuv9iNLMmc6SI5mp1wCdcoE4asImv-Xvyp9yonfF9qpwkwNvyfsZD6ON5yprIVYfIFkQyWZcjuUaOasprxIfqomPhGReLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tSd0mAbovJ5u96RF0yzV7lahqxUECTTEopVZtDuiKYa7Kw0Apv_YVH2rONERVndvDCxRGTo8_Nf_eJMaVJjicnnAo1VXNgaIiJ5QrJEOEsz6cl8vh5NMFyNMK8t6Blh5ApvI5o28RYvLxQU5uUlAI7TkTyzy7NduY3Pepf5-d18_Q2vXjLdn8kjsVPcjTFsn4LK8X9UknqjpaoNbna-s2sr-beJp6MxkPS2TXb24CxKv8YAIL4M1ihnzHBnHMj_fvUgB61spNyZ1pUCTHinXoZC9QF1ovmJ4uKKQf6S8dohJNIFdd-tRjCOsw8nUAcHlcbmp2lvb5QUgVdMk3wOZ5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUVHgztmjJSmbeAL6n07tnrDlH2qKSRxD_XAWkYrFvnxBPp7OJXQRhc-j1rMdzbRW0dLgf8Vdo1oahrMVNZVCsnCTbBv2TFJZzyee5YFqUv9TtVMpiJLY0z36i0mdgAODD9bMtSnauBr163vswbZ3YJhYR8p3-APEWT1k-QNocloWJQLmPYhbUl7ii4-ptUBxkK6WlOUky_9Wx61vVr4buTJjocK7hZGSVp0Xj2Au196o4TWC8RHm69NNdsT_tK8YngF1x6dUn0PlNoP_Hb_b3cQNIFrhKWUJBOo8SaeYaul7gdSEDCMAi2nG94sprskK7rNgADZ46HuCAy1YvTMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nves8kfRY0p2Y-vy8Km__Apki9caHpYD-pTYyq6FehlfW9xqKLoBLruJYvo350KMvi6cgYsBK200FuS4koUCAbzRjX2-S3z2fQWQnMi5Vkt7X-mdmSadikqjt4WbfYxZ4D-o5f-IgtBrGx7wCMuUvtzI2D-R1v6r0UMXKY2QqpG6Uv0N9JwLwybhx1EYdzCpITxvef_vn2VIlH7JeCWP_864avsKLFrXVTHqBbpXApMiuyL-DFl-n4hlBYbk3TQgjSAlfUECULOJhnV1NGXxsOBnSCMHtTgIWequNe2NgV_X6wXratoQGlLo-65WkrPcZ76FvaAPxk6VfrJbm4BCCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QChVfxIeusJRzfcsHDWsMUAYHyRKdG1v6Q_91egbrC8XF1q_6eZqoyJ2rUXn_mIYmLtyynqqsyXwRf2os05ZcBtXm7ZCDPfWEMV_j392aaPsqyWCrrM3F4eyVBHG47DjHr9NDvnIpuHg6gYPsS38so5q5COqOH7oFUZWfvfErditaEmmyvAXDgq0V5sykZtrsnogfeHlnxe3bgQ2ADdXd7ijWWh5QnEqYUqtc9XSrOWaSq9c3nRTjfRflF9ExQEMhPpZ8fOtLHjX47rdYnjXXEaskbX1cayRCdGgSWfV-991xHucjo7fXY44bLVUnun5r2FXgLwufDOjAvDq0GZlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TfQBqYMDymORuCjQZxUSZjuLsmjeMgue0fXiHyll55q7Y2kgXkMzz6fwaJIeEtcsRYgPD8_Kf5tUb8WfQ9jegtYCUd1QTeWJFWNklPH97IAXrXSUvAbhWYIZ8DDB0Cj4ntvJPFi-2slTj6_x0fUeEB_0jbBtNwVEzrje0f_a9iChk4hp2e-dFCfTPzSa6cOL4hNqVIc0vM1nfoN0qv691Hw_uaex6CgMBWxLy533lPb3R-O3DF4rujusCoBOaKnH8ZJWeWyNPCtkKpt9jlz3hYPPTDQPJao-Qpy44BUYtNtZPrEn4YmUUoPu7Ht4t931wlYH8Buabymk7F3mMSHIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Le7hWGr1g859RtrZzXrLQ_hSxxMS4jPYH_l9JvRBhkQvli3hmlVKvjhs1oGSh0I-ZC2UgkxREQt0EVLEwq7QkTCR8VsJEb8yWsFR9PF-YYQpEN62ARaxpGyJM1eaTcKd7xKhwfEkh90Aqv-RHQrYQ5k20a3cCNkdGOB_cMo2WnjqsVi-YL2fi8j3nESvp43CU4jxfqb2s3jtQ1G2iE8mjRtWkzt4lzlmJxIVfJJokAWHMgKBRcha_n348fxt8QvdxvlmTYf2B1OjQ7iERR2bNSgzrW_vbDbyTHt_huTju1E-cpoE8-YmjS9-wuA4XuodVoM-shxpvTt2-_10uUzLWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/exE7WS1qqV0OFibS0v9IFeRnw6shWtsc-zuVLGZ7ovjdHHySK3O7J4fvPe8VuHYqOZWtlIJ9ZlBKRag8PnWhJfXIjBuWLEXaEi2k_Q93ODSQfbYCdnac5s-igHnQ8KyWlhZNDqdIna-GC2PQBo2mmJEebD7dOg8jLb7AMSMONr6PQnl2Lw_zbX9YF7KdiE_6sxcfRiHeV2SigPGnUAhs89Hi0G_t0YueApElf0g8mu7EQfsNJXfielyzbSWgLAnCu2zo9Z5JX84WgNyKBWyhdek_VWi5MyMynF0jqXtjDAZORTGSKZYztsDK3xFkD26FbN9G70a1zrEyzJmBHXgb6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uk-_Kn795ia_1bAlJDl9FH0QKRn7evE0ED2AvlEeJxzv4gj0tf1Im6rzpV3sqvi4MtY__wX0zlsHnRjGcM1jrGhsTX_XrsfVgii1x8ILvQ0VrUWlMcfs5RBHv6x826Q7eP7vyX7VR8T6pAWjfAFlMtWOiFtYWlzRidolAOETxVmHdgvIRu0srlKQsA3GLElbpUyavzjUkW3MvDnh7qzW_MET61oDMxdCI4o0pUFKbCKEz-jpaDacVXCTcffNS5MsIQ415or8M53qbJPVKtX6AradJ9T1dUi8pKQMnugPOW44jT7LfoyBm55HISPAnNid8QJm0trH5UetnabFypP5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AyLoCvTJgFRZcxXooIYqcrFuW4l9tswbQ5KxUEh2hJR48DACJSk3XCoA09C1lNJlqjuu_17KXKjNKUX7kke65trpLg4_S0hjXRgDclhBJm89e66wMH0ydc0piLVgCsm2kSdiEh3TswdFSltoPNETi8b8wXLHl-7DTOP8wLMSwTq-9AqK9OAT7Xkgh2smInnSvQLvASY5Nd2T50ipXRqK44qgSbbd2EvUsNGHk033UNnd4TYfLH9s2WRLIjR8ovygy7wRXZLni_mLPdAxOvYWPviXarOXKGsoPSMxM2ScW6QKKu20kiZQGivH9cJ9JldnlQ7EakvDrlMdiagzGFdumw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A3lasXy6K2j4NnEP8PdhMiTRRTPrpFHtKZXxzxtTvSjfMXJfzyr-v3TyxUh7hhu1NGxcO0ovw9hrEmizndukdnDaZEe6On5c6NjAksJ3k21m4n0WfpjlCoaZjML96_wpMviuk9_Y_gjSbFGBeLKAeAGUOpYYYoUAjzcfagoEmxGJHcsLD_7FJXB99tchZwOD56KfxPTxXfqzC9OkVwcY2HsrWMU3ps2Z3mlf2k_qMqXPaforCJKcUV2Vzwt3JXr3fCBVINLG7nxcnJ9UpzgPzwj1FvbdSTogoYQpSGrvilVKDHzZtzY8rxXjIOlBYuhTKk9SLgEKK3J1zy2-F6oOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1GBfaiHu-6yicPM_HLJEjENbZGfd2mlMTlGL9olFt2fh8mvf61tP-LX2CM5yOcSkmxTiqXfTOMukTGfZOpyxROTherEAJrsWcoVxb9O5WoxU2PC09VBMBVPkIbqWbdvcRlJkkSNBahx_hcx37dvRPyt6uD3o6vbwaDQgxuzOEzOVx6gf3Cvtio0Tni03rKKezStn34bzQmwijrb4MBNAr4VTY3G2xOtYFO4SEUownkDGEAuoYxvNrUB9tX-KuFYUDrYXmcwGKsaUZHvxA9HJ93-C7sn_yAtvx7cZFGqXiiUyelVnGCzz9HoHsq-zGOEU1XIJboPH9mXCodiD53iJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IGuyd8RKg82PbHCE7qzsvBb87XQXW-OAi_OB4E4nlESDTZ6ccLyaYvjG5hsHoxw2mX-qG63OyRIQOEgySi2oTg-juixcUiS5xKDH7t8OAoDFUaYi-mhQzRSHLs-d_KBcTEA_G9sxztRGM8Z9EiD3lNNZUYSFy8HRb-JyUVHvX_55YD4m4-CWUru4t05aAsoGocDjsV8iDUo3CZvV4b7MYQfBylYeKWAe_jY7o7G3SNvCA9-b4OhTNJamadmaGfljaKfkq06X9kQBFGZ5eQEwxAOvZDAQmNywyT6LqJVhoc_EWUDmGgypD7bcPmLKcXKTuZuFniU45XaenOsaMO98ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BkS8euWoxmZaD5R9uFkrDoEU4TSEd2Ov_I_kLSi7N5V7PdxADEpiOtxHSM3Nwsvwx7Dxt8ez8OOa-417eZTJh47tpz2T2PpYc53TmoAajeuXchKatgc5AWW4SdSJLnPWtFiDJ0-gM2OjkLwcyF2MIjIh6J4_5y2Z4qFmSvGUnKVAcTnBMS__ZgwmK3sq4aUXPrJ276833XnzufkIxgeyBQqmVMMIByYSmOhb_znCOQefb_NB5K09hau12kjOHDLDsMwz9DDe9tGuRZ1yGTCiWHrH5SJRrW4rmeXN-f6XGdBbBQgnq-I3tb_nb_XH5OkdZ9jMdljmi7NJQTVJ9DLezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IJyg4A4TIk8hF93sVllJvzw01Sn_nTcFQCSZmzuaamANAvSzMWI-MXg-YZwW8Ra0W6EKqginK6dvN8aJEQXYCxLibqcz4GL1Xm1whydcrTOlmhBPgxph3l8PfSOI22_vgy-TpwjufIXSeyQmuR1OsWa263jJBP93iFxBsDgQ-0MpJtr29HrEXkwWCZX1W2X0wU1gBp3vYmCu60fK9NewM1YupLyHUEzOh5yV6KooQo80RrchX78-oGwfclYNvMq7f_3un0KzHlO0kvGr9WQvtPlEReWY-vjtEvWDAMKPyAjNlLSvYyTST24eohojF9wRpQuPRGh3Qmk2PP_U6kGOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tNQQH7XZOuZrCQXZ-QQBUKZtkHFrJnRNkZxrycNCFpg10QmfDZTBcl-UwleDlRz8g7RFu1rrHILQ20wJxbgM88QPhmYJiOP5zTfOggrI766Z0WbCgD-5D3z0D7cQ9inrLDYQcIWjlW768FKnXw8uyyLfjg3dnIeBm2UJpgx5oSkkuUHfkEhOe-WY1nC8kOIfnWVdHp58oRupWAxBS4D6zyJoCgQHJDoQovDS7tNYTqft8BF2me5ioNdOm_JA0X91z0GLGja41Ol69M3SJj1xx1TKNOvjbMNOMmiZ756S3BJtdv-1zc3mwYtU1rJYTP2kYoanGdTtSeJj5OPHBbqNZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TKSV-ZWaopkxXz4Et3SqrXekEzRzWbnaMc4GVRozdDl8rRZxcuK-tQqkyMQTraNmQnqdvWlfZBWYnPiPEsGMeAmFG096qA_KfYov11mq0KWIv8P-8GG1JSS5J-0QJsUNuWX9ec9sjPisj5hINaFMIftNrbDdoLwUtC32dscqMTzfadNDiNFVQJ-OJI6eKSNXGcm91sJyqrIV3efv6TaYAgr50KJ0FYRXXdGdRaJdrI0-MBWPsh9pHmdPTD2vgwxK6baqhDuYdDkAjYSfg9kHinlUwBjMWlTULAAzJqDgLKuhkzkuZ1Sa4BwOOc0be2QgpIDz0KN6Ds3IKHlLAVad9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OoNKBwz0iROg7BNDSCuQSNcBCMOCZhZmzHYBwijQsSDj_NEZMWCRM0RwR3ekVoY753jmM5qy_muMmBEuH7PSL4_068B67QkVYvtrbgj31ZJj2z_E-3lpo0yFRlf0zKhyN4UbQA9Wwz-JQFOTi2K5lua_J16MpQfnmxKjUCmtoYR5uAmLXJO5_Q6gyHo-sp3nf3EOQI8_9zb1v-qMgIMWr7bR5XyyTE6Q9zv5aGb11vSHrV_RXhGoNPAd5RXnbVUOaWVhiBVVVzw4VEqoNBb0m_D7O_LQOpOBx5BNXBAzMmhLGtGySlPj5JeIRay803YOkeVc30WzxashBMrzqxbIaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXNSGpaLeGhCYw6oB7FrAaUMBWkSGBbVO96TEknB2seNhoBGZwm3Hvc_Xjy8CJtoTk6AOU_qkdtf01od3oqxMJvBWYq80BTUUUf324zPGtkTX3cnWDYiOaXfucV08aNFowqbro_LyyoP4G3fweu2Qm_0fgXgT2Q_na4e6chythqXw1DzMBtvOlmAM1vHRC0qNg9eMhzAkHWAPAYxyLoBD6m0UIvz_cLWKq9jjArrWUcecFIcTUAhNVrpCMuwsDSuP_oULrI3hTqSGj8X2I0sn7cseFeDDRY1xV27rNfnTc3W03WW5qoFtXWtCJynXu_4KipbVTFeNINrQ38hcrwWXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hyeBY6L4P_QyGZVMJBnj7CIsN7U-aRq_tBgduxNTH5I1bnaGmGnPRwiyJ7jdvWxlu8GkPhN_X3WBjH448XlgzFvy_iHuVhKaMqqSybmp4vW7MtcER82mMTPVGKsZwZW7fkDnNhJsyoLoQSAw9MYltcHFmjwtcVWdvT2EpXi7ClmkP8Z9uPhr7D-8mBHJlPPsNZ_D2-2cnymoVxqabbN0nS2njYco1f0RphL_cSfcD2yWmDZk1lTSlxid_KMxhYNv-3HN2TeFRSz4gEtkGw9GxQVFtpNTNrqU1bEwDwz_dDFeflvb8Rh7hvDayrSzzGhmQ9TnzpCpgnRy1UDMWIrkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NnMrGisWMvXjVoFWTcnytWDx25Zy0TEZAlHJfR4L1QE3eLPMNt2OzBoM-Kt0mOr9Ck2b5y6-THW0AMjAAAMeId1-0ACoabx4oa018tvQ17J16PjYf2ivZY0yJcd6AFIDJGAK7WJ6U1zUqmRQdy4KTwAWBxmGbTmLo5BKb6ioSGWnWSdzxT8UJke7feg63Yj9H6DB-yv49XT2GlHL7Ww4FbEWiJgXNCsgld5f4UIStIBtdBDkOUlp0yF7hC1GqfUMvGcAjMO2y9ZHRMNAH4YmlesAEbUz1JfhyczmEkwgVrMSsnZbKG_KuhM9EY639ypzQU2scLCIK7rKaW1QFixyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AipGrSsfsZ5ckmMOs64WRwBAZMOX0yDJB-1761uwGt4StEJ2k2LHQtssvzQXKfPREi3tG8fWkBCxzZqIrTmNnU2eUtrthHrVL_fkU-F1NJax99Gy-R1445g_KUMBK70D-mDsxvBi7-ys3RxDXeVlqvW2pRfo8U2XHImQxBo5hvz5lL7k_W0VTIw_K1F_77ukVvqXolSPBnIdQvh8sxOqSR5x3FGTEjvLqzxafHOb34hn98GkzUsSqNTmwIbvUGPlvD-bctOdVgajq-Efh0vsFyl2Ev5niGctYG3iH55duosyXG4By0ey77iW1M325x56scW9aeztSUtNitLrd879-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PyEtkV7T6LHndzOt87cBkXXFV_3bQFdLHpyihJaifkFSnKT2iqQuSV4RepSvhL7d7lrUPSAErrK3ZRd6DW_sIZV0q7oOpA3fRnEWMk5qqisPT2IZBh1dLuW5TtQSNIR4txQw7ovWGGdlOiwxjOrK9Mi274Qwu-20IzMkcscrFal2xYbDvWfwKtptaJtishNUHLh7VJf3z_TiGfT4u6RPhD20cX9UwuulR6EFZjM_cukFxVTRXWgHl6gHt7LKlBPmvhCQ3KYadpCSOXIyKK78Y4gkgXdDe85BsQ7LBA-yMzHqH9o-bSXrD-621EyRPZSYzBhMfgKWDWLs3r0meyTjIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/peSneGmZPil2m2V1HxxMUa9wtvjs0bK15vEGZElAhi014srwt7OsCDku98IUofA4JlUEgcryBNsu_f-sH3tCZVK-V9KB9nD-Y4aYUraN2KoitgAMP748rVA7Yt2JqhoXgGl3kaFlLjJjnfGMJEeSpS2LCb-8sJykD-77Pp5OgdX4ZlwdT6G88JdJA3ozpOn57zlmTQIQYOZlB7UifeKTByy-fo-iAw1RvISddQASLCsULa_dxfjnAkTWKXURjv8we9a1re7aa1EipiqZeOtm1074tQun4r6J9gs2JlN444-4meP8pEG19HcKQMYZs_aAA7j3_N3MW19f6Lhfw6-jXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QJ_TvWe2qNgLKWvk82zBStDGIiU5lsqa2_T3U-eF-UYlQgLlmLKQFp0PFoWUyvpv6lXGdYlfm36zErNHzQ1qJqH1kso9fNv35p3ivs23XEReMJfn2mOsX4dYBfno-wCsu3lgpxQ_GalApcVo1VJMJcsWqVFtIfNGpGw9_tmAjpaQYhL-XcXitQz_1BFST7slebphg4RBU9ErC84rufuKgCJJMV5Ti3WbajwS29mpCAAwDpU19TUNp-3j4IEZeecZtuoeNzfXehdHoA4XJwGPbLBzzXcly0b7VgOmq_G2vXxZ7YTOGMSYuLjhiS-up3ZEkEhF4W10w-2OzX5_IJ0glA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QbcGqY5ECwQfU657qDljRD98NlE6X19CI1TP9gHjqiXg_uIYGflT4JfXUzpVtZeX9q3641EH1_SWNUo3_TfFwWuRLDatiCu58hdxQR-0jeTWaZ10yro1DPIaFsO78LJ4gwfuRsf_Ay7nIrYlz3aCtgRLn8hwC8cURciZnA3owtnSbmHACgQc5O0wqMKifJdhVTxTiytLOngCWe33OP91a1KjA3QumAF684IY4oFRnI0Qlxm2H3xlOFkfO9ix1KfPltqjAiBBEG8XzfJgEFA-t1cEsBmWLYu9vSgqNH2Mow3ZCbgjUZ41N5ZciUHINjRCAFkquQ64PWhVVA8Zegy-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Uypqqg361dhyN2HWzBODwzdQBs1M0ozFCJBsrM2vOT2pf9GWXcO3TQZI8dUyXhMcGpy_-1xOKngG3pTIGppnk1Mcwy5ITUIXOOPM6YWbZCLfLyQdpkZI3bof9lCAzx9N78iOaHd88fg9GyBczPmDlN5yRpNA6c0Kf95y2_xxbwDx7qo-R_K3w62g8Qturk2H11eRnRie0MI155AaQiPMLh-byWlwFbedg2gknNcVyK729Uae1tL6lY7ExQbvNQ_vxpvNguWYbuegLSE8dpIdbu16duiJ8XvBh7L9yuHzhaacGptAofPBhOxHYZiE-mNkOHn1v8PBwRDA5trUlg7O8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Rxw9XhYo8A9y0ebrgMqxemXCcdXQ-_Wn6pA9gZLdUj-0vEN1VAmLzbKgCmhHq4FgbhTXSqCPPItKuvSyaqJvF2qOOQNVJBpkSopWEqueFj2Q4gL3ajVLIjmS_YzcRejSoUMXB01Eo_HgxWdfAPDy3faNzBRHnoAXExkZWiKtqAK8gpi_4zniuFaypM2Y-tXMAQBQmy_Usbgb2rDcgkTL3Bw1URO83RVD3LqD-GFzL90djsYlOHHRaYSxnQAIPK6_fEM9SBxqplb9e-6McSSi-6Y2QZLNN5tqvF08wsWbzIJe7Q4ARZFHH2-hLzClTjsv7SH2G8Npg1lj37qjrmV-HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W89zXrTfLP_9hWhsEnrgoYe8RrNfcnYz5VA7HaYIutWV08pFNrjojTAeMqCuD6erEZFaVl3WR9rFCHE5_2l76BGIO8_ja11N5OOU7KD45GG8Q3pOhOYQAyqhIC1bi5iINCxXlHtpfTIyqnmi2NsMmPUGQP5etWyls487u5_dod0VcUFzWf0DxLMyhZou2LRwv4YgH6B0Dh53tn4zxrCJxDop38SLs4XC925pKzZjdzie2LEAd64ldqUH2U4KSi8vQHCUKNrLIwwL5gtfDTjhgGhnRWHNP3V3jbt3j_wIhVBID_CgI6oGCWWH6s0pALUO4cv21tCJV9hpZecB3FZhzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DHBpBl9WnpXDFKthFC6FryjAtegEXn4lxd1QHceJrfXmDNa-eCxucz5iR9YAcwdTK6SqgxCWcXQvz0yIViYf77ZXisunnZCTZs65QpmFBzrj9GvON0_KXltirH-Z5jUEJf4nIv_q9l5rXk9Fwx2dLzBTXFZvDbFjKbA43fgdiqtQaYQ_DufBPcp_USXdVWbSuXsjmzHFKJb_ap8YJLaUcw3cYR2g4XpsnVGjDNOnhdSF4r0RCdghi3xVUI7y-T0l0YLpaneu3wYQDUn1oFNCNo5E_bund6aWrXijfKzIRNWVaYfH9ZzMztnYxsxS9Y7IUqvcwKfU1WLuUa0iaVT_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/md71iFWpQLHxnUpZ3e1O3lJ9PUkwJ3o281bxHtjsyh3Dv9xF2gpYOW0-j9_2-38jXDQ4UiaALb6T7xs6gWWDx2zmQnPBdkV_lgl7zBTdK8OgTKtjDIyLOmK600lJ-D1cxz5uECGy4OeKl73Fxh9xDZx0FlpBm19dt63AU0eR__Wg61MLkp1v4kSwT6Ndob5eakrRO8S1tPP8AAIcN-Xqv7hoy8RGnY_ADPJ1BLBcbfSO9jNlR1SRpxLJcGKTBtFdcuuivKk_9XnsdKfsdCrFUlqOczb_KvgYU7ZwRR8gmDbkAUpIm1jw5xCx2Tdlu7LmBruje6F6vg3L_vlT07lqkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QM8qAeeoVr1KE3F-y1fRYqQLgic5E_lJPnwYZqGeaH4E3EAcNH9vDyPyU_MfZR7IcY_X3ESnZrfPiNlLc1SXjp9EfzMkqZsGjd4JG3LPLhzsRZ0mpkXlRz1aVtWh6ADq0whQ13VD4uhn_mTiHiRpDkD2_Abs9m6umNy4r6p_6KHfn8DuzsIuILh63Koq7giBY9ji3DbyFVuZyRfSs9K4awX3M9OyHp1NbWsUMG4m1uNTj6DCA_6eOiLs1VXMYwBTFl68X1wpZfganofLUS3RZreTnjs1A2f0AexW-uCzXAvNp3TvSWO2NZIs20xEJ-4lTuLR-TJ_TYITyG32XZmSRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CArmsod6cQR4vLCtemZVDOKsu_BkbC8CNAApos3hKAYqfpqbTXB44aWn7rRfpJwrMLroTW-gHliwBrXShYefkgbevEV2hLVU56BQDZM1pyvThCeZr6NpBtaUGOeFuWzPByuDeaAgY24GOaZ5cEmLRw-aOLxcdq1h-QB4JRt2l1v_Tlujllv2YJrnGsCTaU_g0X3vSqPmzbM7nxwo8pSK1H_6h7ZQeXd__Msh0sMRo76qCQBHdLvzPBWUkoHau4DxDlcGwMeCnO_kT0VjMIwfcYFgoMU9YUCR5pXuaFMILu_HPJPgHZexySw_TWAeyWmBlHzcb_rEpTr2WcxTzn7y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HLIivMbdHs16LpF87b2blyPUYCTBRFrCvAIvfe-mrCZzhfBcOfOluNDL1JWenkOCw9ddmpwPTqYJR9qrYjwSPyzlNcsk_GLxqgU0nfttXNPuQ7f2AzzkVvFSvoLo06DMmD07-GOA37pAGHEgen9TW0lrA-vS9lDGO8DjtE2WrCxPtPQ9vc2Ot_a7T42A9eZcjwULefxu-6OrTAwZP-Iq6-r7iQiZZdfRJ6v2EkGIwPa4Udd-T8svaJitqqDs3jIolR_4X2ZECx-4TRs73EHPi6cVzzxadoEsncYF8PxpVT3uhUJYYQgbLnebj0ViIGqPt91JoVThcBKbUHVLroF6Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Awc0oRG5bi4XMoFp7xTb4syA1n8i6p_r3HmtSr804VDD9XVkPHCQQNiXTi7oFDq_qd2B5qEFqxZy1vDMXKyQSJ7LRb2_wbQNdLub5nUtId4sOyCZAdt_WMg84uSGUVFy4GOofcn2ADGiIadxDyTh179mIZEeMh7gowCZNMm_bqEiLVku5i0wUU3v-z5UFk5ZVSCTnqfibcKF3tPMV3RnV7qxlGwImYVSGVC0Fle0gyQiFaK8dz354unS-MJAQ87ksa2xBzVTA_JwgAvTfhJ-Qu351CxuFibpFzoALZL3TV1JUwy9Hy4CHupDHo1qSsno0hOwgfSZdr6HrsA5mdb-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uZhburBT0-oWuJ5o49L7is3Lc3bR9gyCFNTKEsDYkpn5SHFnrMgegm2yGwrgRu-XaRWzNhH6KKHPSa_4eXuveYM2JWjxPoyluJsV8iwZnEH4CQsJlbqgFyo9surQ4YrO37ohCPq1gZ-93Nh160BTsXJ_-JhbEltArEl9ccsxIHA4m7JbIiIB3veosEcWONeGdDuzcaDPIes59FtHz8fDmwm-yWGb6zs3gShQZi1pSem7FB_xet_7p5cl_pLI2nWMrYNqhbaBJentuXUeXD4HZP8slKzHi9OANQbiWasR8-ogInu5Pq2EP61KlCp3X5QNaaNN7Qwoj8Je-p2fvo2ieg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r85jFx_cSCy4eRcRZ8USPLhVsxMAEEByflrcGI3P72gphUJL-9OLzJpTLspatbv4Ocm_-Aev21dTxQ41LVFSOlGLMUOm1Pb4p8jUM51owcLp2-h6FZcs27-3AbrrT5RCwkpjqTDWTI168xAyS2boD5j7l0ZPAQbx7TVHCQHZT6nOsBtqCSijJgRXne31TPFQI_2ddTfFUt1h-HkTbeUtPgj3iRuEoEuyacpYza-Rd4jq7M7mz_ewWN5gr1PXO5aULhqExtJ9ZB-HlLojth3pH72bUW7qXWMI0j5O2QHHCT8Sv8uuE0jsNY9rRm2fwWQH1T0rumDzUKYmSpqtRxM4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZU9XrI2PVthvHz2tGfxeqfhO0Ufzn_MjhqpVyYQCBtvwY8DbsTAoUXbMbqup4SXASpqQv2JfZ02EwI61dTXKqbxnf3JLea0FWTUDmKDJeRd_faP6-Y1SK55CbF7gpriIxOxhH2edBtI83iZDURoJi_30_0uTCOs48_rRiS_RMTz2yEcm9hJRSPi5wCKuKFdPU4-CxytYs7juym_ltXwPcByZZuMtGBSeJ_KzGVV4CJ_MbG1WO9ZCFEHH3Ntm2n5-9uyRR4US_jt897G-zhxvns93ftJe3owKu3Y9pgcEAXXXE0rSyazkYFibs5DSVO1i01YC8Gjvk-mNi6ZI0WNyaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v45OOzQ2SSCv7MA4f8gEMn2bfd0OeUcUrYus8yuFVqMCiLfq_7pjeMwH6qO7KpI8_QPeeQBQQEc_vsQl6hD-1nN5KUePu8Fhn8f_ijGLoLwQYgWzOJ6J_oV_uI-HHzHhznfNJ-oqAxYKmCdzRetBCVhezNnA8GwLq4YR2gTdWqec1A1jIFH-_2aU7LnkFAmJxqb2mRVUzsVRljcYB7AcjTxboWSjnT_27w9CNl9STL_6sZ2kiqRzkFqOpqpBUSpfIZ_L8H3koSuI_wPivQONQko-CXs-JgseDnDXnXJMTH2hQT0J4uxsWpHQ3-u_XQVuAWvu2QtxYAzoiNw3J9CmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ah_xYKmim03lfObnkIPDF8WguEldIYC1zVM-9pU7PYKyOu4OJi3Esob81qu8QMzf82lpSqw4y8C7YlznEvBYM7Ba9qWAc-8lk_AkD8cgkeOEr2KAI6vtvO3pC1vgM-1xB5wYaaqgjPtEwUPCcWQjrispyIbxZuXYz9_hsl205YzN6iVn0ZhIKQZZlR2iWTeRXLYbafHyTPwp7xz4KmapNykUWIi3h2YgXW-XzYcMiMJeAj9Aan4cUArjGrZmDSgu1Iz2kY-sXQhqeDX4YVQ2TJfl3F2fw-5REo8TpwEJfuzqn_k2RdP_hQlji_Y3qrJQN9qDWGbLlvq8LQlo0reE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iJrGYDwxyY6qEP3kLzlQjY5PDNPYguNng-FUpQ_3LgxtWx6Aqb5AInQSnPVt1b4_LnY-XdyHrt1yU0xAzjvK_TrwTwY1pPwuh7Zw0zNq0hFes5NKI8QRR5NHdEEduFoFq-c-IxC22PHvHl7d6kQs2vTudz7EJN01NTdNQO8Dm9QqewqtP9unZ31tVVjy6KDdBDiFUSNjtr8nOOgJIY7hz_LZ8uLO0eV6wqxe2gikojpkKUCjs-7IWORKXoNbfpS_enxfZSy5Cpm0_zrUn3ZXhwgr6BuDbhKRIFMgC63WA9-BZFMtN_arb3cbaga5nrbejVR0gl38PZE0WyX6Tb4ggg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbhobY59HU7BPi9aCM7Vhb5wzkXObXXm4g-0EMR4anImZYiNA9glQmxd_XEm7lVhuHX6bw1RT73tp27CpTljSOjnyNYG-iXoe_R-5xzzweKLlT-YaGPMyY3Waud8z5Zjha2OKWkdvAeJNgU-vDdp2ZnMMBzK6IIQo6VAdQD8-Q_IZBWTUewS2EpIaeIzK4n3RgRB9h2c-NoPjrIlqaFH9xOxn_7FeLHEd4NiBSrNAk2wXKP0wlWBCkH-VT3-MQksbM-r6wdmjbyk4NZYD8Tn__M1T_CRqJpEFjfIaIlp4CEVOsLPnHyqCo6DnoBU4Xgf4oauPLDr1UuzSVazh4TnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/boAWtUZexjv_dKJuHsYHae4eBqfZW1yo-vAhfLgzCVfqt79JRp83ZziVUTAd-th_27swvZYutlCakqTZUVlEX9pF99j14GHVCYURMlf5eGgLe-Q9JGLLIm0ysFHeSHPg6md_YR-BX7R4aB_eL1cK9X6Irc2ToDqSNXDYvWyn-phqVDiZcLVj7-gWTZ_cmFmYpmVfRyOWXTIDsTfjWVvbqDOIAsYrzB7wjHAUisT5f_mN-ykLSzJ2pNwgUuoQdR1IwhI7V02Qh6wFVfse1DWhaal2znRgueR9a9flEipIVW7tt0G3X0bHBIDp2y3YKXBsK8y8OkTiHSoGLeoYTFOpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vry2y2xlEablo4KFrvM7lpz_tX-F2G-M4SgkYdQArhh6UPq7J9AC8RuN_la1c4mUQ7h9aufJyMHp1jXknjgdxjRs9593Q7M3aysYdFN3mgJuS4-02XjTAlLJabXjUTZBJeeyQ40OKz0OKXOv7_xKJrFF43pV6KhKvivZKJk17ugciWLZHIWeSSlXpK1KijtNThDEhbbjNzxwD6YyrchrBXilkLA0HC-cPP0wvD2sb11i1wg5kwv7FiKI6p95DPq_9Mn_9eagzRpORjn5JqF9B1PRW0m9pQgdEq0mV0M4a-DXFRbu4tYrwGmM_J4mL5XsU4G4RjOmtyxyh1NbmhpzSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DIV-S1KjmnJLTDvuXlFZdnemb-8sOOQMhI67II3GG5jf5mJivFK9ugUYEk7i3HntojbeYxb4daylp_uzE4Ln46AJWRaxGw-7GRNdlGBEFvCq02QeV_MyMRHqGOiIKwx0SqRHxnSgfQAMfyLK2BWVsMkOEzSucNDtazu6OUPnrb5rdhYgSTbWBfHd0fhza6NUDHYYxn-kbMyEXVRn9B35UgcxzjUgFSbHFxgFXEQ4QeImCzTkvspmMifRK5i3wuZ8evnpi6QI8BS7mRg1OaRgWQ7FJNGg0t7rObyHyoY1f2XbATUMPjQp6VSQaBRln6xsMUeu0u54nGskAP4mRechpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O0QgZUPqPNIpQUd6S1U-NvcFvoRhAxGYx3_uogCnO9uDynTnYtGvn91jWQYmUgPDQDw7XD0pw28aI9ZfMxeY7LETLT55eqBQHx3f1k757KzY5Xq0HkTf1BnvOrT6Agw1AL6JW-q2BpyEhPqAV0mjNllbO7YiHjTCtIQl3tOAJzuzS2wFNz_GnDbucfYS6my8rivJQR_u7CCz85WygqBZsVMfWh36f7hkZFhNjlCWgiTPZAT71cJHgC4KzrovKklQ4jvtUzmUWDysi8FptdRsjwQBBZlWOW_M0D8UL0uFmAUiVP73yG3QXOiCniI0ri-51MgO6azBNhwoQR7dxQr4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UfCMRKwQHEQUaNEbX7-Zl48Um5IH29POY2Gb_L25k607f3n05WB_jOKV2316oWPl2SlmhPE1zi0OAeIME2e1rRksbaxdu-mtxmxBCec1l6hDX3Er9ZPfkpLejES0XghM-YQSYBnErRmxG5iGELDNdQAcmyzVfNbst6uZnGjQ4G-uubvlnkaIUYQPkfJgc9Z-Rpq1RpQG5tGkPY2p4BxM77119DjI5yDjt38xJRydghUYSe3mifxmTbNVy3MwoidHpLeGxlvcGidqZCcHk3KmHOc6lEOgPfH3bF8VtxmydNA31eB3mvoQ8BeUP7ofwSbuO3tqrOigd1-ndAS6iGnnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYhjpsvi_Cok4_DhriyoKDUggHVyMI9rlPHPMBdZ9JNuOSRbT8yaLjxuQXcqj-qt43jFFmka-ib9RlzEbo0t9KVB-UAU8jyHqpzwKUF4tjREg--HM74bLvbbMlWU7shBSYFgzbW5-Pb31bcKzDWdBuIpQjktKrVZWa6XyGdod01XxAPjEedyG3neFe7mzWOtiVAPdyeOBVABuRDCrTVsHLLQ_rpZ7wFDRHp8BwqFtMVHFuPRD66RnLW_k5ljbN7kJMskhhpDRCMFFJTf1e79s8lqYugj5krwFXonvSc0RwAvQmp_y8Sm0GTCQey29b6J9SA7jI3dE2ViFNqupF5uPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtclV6UUcFU3ZNlYnm9QyPvjZD3OK6sYEjihrFoMYliSRpfgGXBWOsYyHGtxCkeBIK_w1B1NMYDaeN60k-ZLk9sa364XiTNIVuvWdbFjFwfrcklwmqwCigL92-GAn3n9Y5oQXP65ecqdIYP11O6wFbaZ-eGA8o7omrpd8tSYXo5toVh-cG8ffj0yh2NY5oQVUFzuXU-m-MpqyXxrnCgaeuh8GOuzjyPgcyDbD6axVuZk6Fu2wj6iDFeRNorkkgqYLPimYvaqWrAof_iNikU9wrryyVOU_WwDOScxePW3nGtV0e-GiTNBhFkuN9CJgo3EKVnnu3doZmQ07ekMRSg-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
