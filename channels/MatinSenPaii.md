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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gd_m-KAzdFQL4jYzu2KoQvKNBS4ACvKVIURFmdn3pZte0-jwQNTNWcQfE5Qnn3t0nZSTrnDZ8Fn1Wkq4OdCiiNx4fwJ9tzMKgnhDJOqkylPPws5_QnYPxTHZgHqG1RG0QwhpLpiZYmfitS_qyQ6xXsmK73xaNXq4AyXt530DQaOFWuBgq0WAUONOAP0RKmPpzbCZqy5psK0EiEowlRG9bpcZgvqt_V0nU8wlkPhWLRV2DOTblMuYagcR8Z7mPXpJnx0ug57vyLC97GZdGhUrq641C4mBqdYK_mbNVLnJP5DMUYfZKykwf2PXUpDqYT1lV-pchELifvEv7dPNuJRXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MV2dts97hHvuvjFZkq9q-DamRbg15OYlhkk578ohHxdI5nqPCezVJU4OuCqKAdtt3OZtK1kqPB4UeY4iiYviL6nLZFMF9p9doS44zN-9FoV2tv3pQJwR4hyJTXNy5yb2LW5zgaJ3feWojujhbtUTTEy8J3qVOy5aROo6NdZwa3DBkxheRV_B6mkn_BXu20vfsi1UTFD9FiOygG8gfGaoDWNE21Tc7R8Zrmm_5NibdeA-e47RjDR5yAV7rZid2moqCoQKRT0xDpphEU9aApiPIR-gXZcirhicyJxs5Zq4LCMIxwQYdbeBq46VSYTJi8wJ3EnMnwfTi2cJoRBI3DOs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ufqB8AjSs5HYCs5I2YK7zVcuUEBsIDxQ3qckBK_Pwu77oYzlzE76KuZNJGk9xZTALE0zuhE_ziJCrffnRSKpqK-cg4pChlnbQVeMpyEYhVU4Yn8KXm_bYHbi0wZDKlRq1KI-5AN_J9Uwd86DO8HmNpiREAI5F0T2C2Um26Bl1u0FKbTV8toioOl8KgIX6P6cM3XIII4OTb1WcjgI65X0MqHyoedPPjlsD3rOsyoaud0PDPpTJc19IlUVSNX3vhBFeqcrDFrhVhp7tQUARv0FRUTmMEfWz_v_JkS7WdKV6sPOcKu3X5tq_icQA4-33Bw-WTtDv2eqLtgPGrWK293qiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ufqB8AjSs5HYCs5I2YK7zVcuUEBsIDxQ3qckBK_Pwu77oYzlzE76KuZNJGk9xZTALE0zuhE_ziJCrffnRSKpqK-cg4pChlnbQVeMpyEYhVU4Yn8KXm_bYHbi0wZDKlRq1KI-5AN_J9Uwd86DO8HmNpiREAI5F0T2C2Um26Bl1u0FKbTV8toioOl8KgIX6P6cM3XIII4OTb1WcjgI65X0MqHyoedPPjlsD3rOsyoaud0PDPpTJc19IlUVSNX3vhBFeqcrDFrhVhp7tQUARv0FRUTmMEfWz_v_JkS7WdKV6sPOcKu3X5tq_icQA4-33Bw-WTtDv2eqLtgPGrWK293qiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eAALLGBKhmHHX3yB9OYwKcqQyEhH7X-d6uwf3vthJqVqBS1cVxaOppEpShFLnji5jsGU2vRkAL2BNns7dX-_JOEqMkO5wmiVATepFSfr7aY8kO07M_3Zdw2z6xHJeV8fsWqIjztP7AHOrW0arZojvNgVg0hs8COdGRkqlESTjdB61TUYK80uiZAjOGqIwVGwXKEzvxvnSyGtg1lqqpWJ0aPcm3V0X4H5vRVziaSxyLxY9WhBWMLwO36pzLpaLrHM-S7_ZKYEEqMnVMSkkLn3LO6VMW9e5yKz__QtDfGqSuLwy-nBhZhMJfrAfNBTmL9ZzJ9GezZwpN05xo2BRtq2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uLiSjtkcox8vEbV_KsSxDZ7yvEezLfteJFfKiEpx1SMugF-aeiqDCdPzbao3cKjZCd8dJkcRpbgxnN8_PMtyIDWhI_SEEol0OWUl1_XwJEce5_nudvt9wMH7ZzBfUfU2KHv2xbUqSnjacaghEF7AepOt9n6IPPfcbKiCV47TXk-Qu9FGN05ASG5H92SVNG9KQiel1NEU0ZXjc3zDc6BGyu9paErcObxmEW28Jb64lkvsOjdFXSoGvHzgSghboWDzQJcSEC7FjXDqQ4Pa7iLfShWzm0uZg6Ot9wWofcya7IDQtGuExHkVis-pwVolJ7_3Uk4XPSxbxmjLStFVyCby-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/COHrRBWB8y-HDROicDStXL4_dhVWXuv_aw1P8_NVslm719wfWBz73s4DTe9ogq_0PiHtPMKwvknwLI3E5F4pi8E7IOl4L7Shr65JCPcJO4KBlObZWD7_oPJ5JZsxQz6BNJN8FzGVFLjvY157F-GE6qs0l8ufsiq2TwEEIzN034tW2KwGFgd_DhKSaS0U8eSn37PF69MgJ-fuKWspQgdfr1eKdYqrO6ZHdLPKNu9J3-IT7DqP8nRP4o27gtfSKiiE6yiYCDn3eqL5_Tn_Ob7f82mGmPjRCzB4JzJUoQPN5NNIVBaDuaJ4ZVqDSbWflaiZPUdjfK2eaXkzvDnrFjBNHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lA4G3MUbJGMBKCz-Iw_Ah4JiHWojY6A_tjH1ZBjPBcKvprIfh_vGEOVBbunOeE2LjbksXzcZ01g0XvQTo_TyQD6Wr1QSPlIwSNtrG6bWaEJq2br35J0y_ucDEXZlZyueznxExt23JGPDGWXHQJq14Do-NR0Tn5Xjm_4_teXON8hNJHVmCfAKymRvVl8pRF1c8mt0poU5-HvBzA0nRH00k3GwEivVUoENpswcCnsdv-vZXyy_VlTZR4dMl4rd2zmEZ-Kl0A-4ZDc8jQxpV1vKjXwr6PJ0_2fMUDMbV1bobGLlDpTAM1YwdbrFDasf84ABqbPen5u7CkiB0Qa1zKhBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c1-OfNeNyfuZddPvahYrlMCOZmWXA-UMWz6gc9ZOlgwU7yrk21Ey2BdigQgk8aU9HdahMM3uxoW1nDILDlJjm5p7BOcpKS1pfJ2YljKNBi2qYPVB5ws0tijp__Fd5wy2HvTo7CFjIzMdyiRkP9mjMWprVlmsqmBqOJFyuVPP4oMb3veeGPcs7OtXC-MHDV5-zzI8nYe2VExCwaDZXDXxzcfUTaBwEiBhJjMJ5_j_CMZgDdnXLZ7-SJXLQqc-AGgJkBNgqh0wYDVJjjU-TacD3BjcJV7rh_z6mjpOy8KwuIjVJ2d-gO3hd9jOcVqlL5MOmTNYGyytEno3RZUNQ9yAHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2T18PRGHgvMrzq9HI04daHLDQ1UxgswDCt7ZCsNwpW_1TyaB8p3ZjQ3scq_EFNEAx9A8nGzl4-u_6iIFfXBu8lrAN4VX72_d95w128mVhw9aaHDTLcl0BmqRw5SIUcbAxiJCA9RbE3JYovjluFJpzelUVa00eRGFWkFshkT9QdS5iR2GVSyG3_RISsS_gFqiiaqS77QVGno-57Xk2OS9-GMtWlOunZYm0uJG27jzaRKVpN2PCMLm7ULrkG6CR9dJjhikTNOEQZcfOJkU4C9aD9uVIzelNdIOC5y1jwCNNkX_kT7CQUJVqrsjsnPJSI7bO4rILtvDlDTTQaCjjSYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=EcW70PaL4r4nVzR-U8rRqMgiszBDZTKhC1ZMGO0JeEtF5sy4noQpgcbzI5H80vRJw_uFdExy0ar-wYhDLNTu99r0dQ48BSEVp6BE4KpbXJCC5r23ATEDylg89PbB05sRn1l0WpX4t2SYunQ8ADzxjqYZo9dvJ2GxBw1E8xVWSbq-g1KKuIESr1pEJhAb2uxYzpz6ZuniV24wOuWxXQNoRNUj_SUJmtegj5yHCinDh-7sPBx-aOqywHu3n6-zeZNhpIaA_XWm4qrCVRdamUkVouWUCM0F5PVYvP4xVM23_S-YmrMoxjEWkEKyymE-dmFe1M2tigliOTbks77H0FJUcw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=EcW70PaL4r4nVzR-U8rRqMgiszBDZTKhC1ZMGO0JeEtF5sy4noQpgcbzI5H80vRJw_uFdExy0ar-wYhDLNTu99r0dQ48BSEVp6BE4KpbXJCC5r23ATEDylg89PbB05sRn1l0WpX4t2SYunQ8ADzxjqYZo9dvJ2GxBw1E8xVWSbq-g1KKuIESr1pEJhAb2uxYzpz6ZuniV24wOuWxXQNoRNUj_SUJmtegj5yHCinDh-7sPBx-aOqywHu3n6-zeZNhpIaA_XWm4qrCVRdamUkVouWUCM0F5PVYvP4xVM23_S-YmrMoxjEWkEKyymE-dmFe1M2tigliOTbks77H0FJUcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CRJsaL9HjQXaRWKKPQZBfW8G7_XzJfSJuwH1wXHxV8v6PqbmzgzU_VJTQ_9083BNijNuBCpo8InWYcEDYuJBxffycdrxffGjrvHrQYcV_BKcIHuYBVZBnZW717sAVTO-4wpWU_M3zRvcsVW9R1Pbd3jr4SmdaHqLwRmQyuW4GATx7vCCnPFTEYdLgRmyG6Ynqu2VPlZbK-rQCHoIIP399YmFTkhwijSEByCKjpcaMs1Ie7GqGBwi03n71Bsxcsjd1Rhdb4DpQFTrMOho0WEurKUeOb69wB8BGCeH1XmDOA1StAY9EC72Y3oIdfLMR-1bcIStIO24BMDUiScV5IftKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iis4pXps3D_CIS-crOl2b4RsqJGmsNQhwJe27C_kLIVrq42v_pvvC0K4b6vVmRZ54oSUUO_a06Y3fjM6nQg5P4ifbj3j87Gs9duN1-TyOAE2JLsxjTWi3VqTfton1npRWFBdCdOe8dT0e0J6htnMxWg_wtmno4iKeIxtxxl_eUx_aozADmB4UcXxVFDuBQoMirKPUg3Jgl24n-mkk9wyZgleIamry6zeAXdIGctI4Te9EqmGq7CizRhS_pENiHdeyJlY2DTZw9Fi3gB8szBTB4Zq55CZ4Dvt5l-42YE2nZ47UjYyBQbJsRBOBWJA4_yDLfQR1MPsLcVWx5aoliZuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OzeIvwx9wFBX5sP5AMNT_STPMaIPiW3baofT8ID8Di6rhnmHWeGct0ZMfojo3HObXejp76PrLKXvIbRFhYyVbbzJUY2p5q_Dj-28pYkA-_hEHrnf1j-1PurYePY0ycsoMBMTH7ETn779Hpm5K5t20SNdUAhD_ZQPr37hJNFvLah7iiR-KhWNxeax9Jx-Iu-CE4C5cx4MbelaEQnzcuBP1BGRg4omJdS-SpRTwtDALFZUF1WfEj41FJwUsY3rOU2Prra2pVXnuboB0fkjgfuFmzdy0Jw3beWpl32wwdKqBzyAo95-7yhZZIsEAoRWrKH1gOsHVo7yNZAxK_pTy1FTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNKx3eK99_vGq-akPq0aG494cZTKkjkVPeRPtvonmkpwlzDbT67RRuUeKkVCeNazKOUD3QYhQdfekBAINJuzKG_Ow9mcGTuLPu8ebgqIG5u6WqAvqk8-Z5zMWcQPc_MI6ai8FNDCJDOAkMAKaYXgiyxuceexe_rvV9KWyG8MJA_qxc_ZZZidbsxblXoJ8_wtt_KvuJ3Eyt_3yymeE0Ttj-lsxbN1cHd9WYJQY7mVhYVn58qG4RVn5H_TMTllpgg6aC4t7QgPkEjXX_8QWXgPRJ1A__3Bb9SMDnC2IOkMDVMIDobHltl3eWfwVZUXMDiKPQBh2aUXF_7cAGOU-LnsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jbQQeLN0xdpzGreyNgrXqJPkc437cMmxX4AfUKDIXZZ4imUZIXCnaCwg3zXYDEBFlsjEf_GKmcKlByM0yiMhvNuZJdtV5QsOSvvAtesUPhbaituvBtnFoyuJPzBG4yT8M65RpL7wNvZ-9p6BUy_NsChTtpJPeA_WULX9ddk3fv3_aSR-WFc-AnMn3ih6RaPZoo64JSq7txoWkGHbyoGYDduOf7BiJvO7w3SCyppx_ZS2q_-wrDRzImswvQPchj6q9Hk2NNSJMqwVOyQKwTQh1n3Pe3MiWoQiZmOYQwArmDzScN5hIeRydobilu6mpSIYXuXUdYvulfoRvI5WvB5skQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-pFykxe9s8HOYqH6gXsb9RDhWTHaWehruTUElYGsSZzE2skklmCmG5LYvdmNkcjskk0QhfunT-Alvf-8A4s7VhRpL1nFPE6--OEM4pL9GpAdMBYMoOFfsWdccCKLPJScirgQ6bdvdkbZCF__7gy6iLTg6bfLcUVApL7vB64ber2GbtNgBilrBGfrNOSbo4vaQFFAZpxslJ7x5lEe-a5cETCHPftRlDuqQzQqB4b8e-S6XHJmoXGY993LCj5bu_dCmVOxz1jamdvpM2G92FbocO1Ee0--BjzzeC0ZYEUueSCvaw-_QnhDWCIKCdMt5-FHjn8WXkaQOAuuYtbGH3lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_tWQ5ZF5LQxBvtSzi2UMHHdVObj_xAr0VKle23A8GoyzaGr-thy4tb-bhQCzeaJBm1_ScN5N0fZ4C7Vnl1PlcZUqYaz7nldGlcIIR6PnFqHkBloIyY7KA-t-zwjaLNnzzJmBWgZB09AQgCxLrX6odlNOIV3UddU8VvuEzfCi7QIj6pAfR-nCG3yeupepUHyd5QYpmbOijft4eC7di78uSuVdi5aY5yZD4qBaXVjjwKt3A12kCuBmOoM121iBu-2_Y2sVcex2_r-hz5VDcNgzNsVxD5Sw5dOTqyEjUAW7paz9zxqDCpmUQ6wqBmx-mA8MqxA-av61vJDLqB6pg5WEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FqwNrm2ZjX1jUE2LInzMAnIq1s52rbvjz5kMfm7z1t6_VNSQ0svEiOjGbGdjVJvA90u3rLya4RyMtqmBw46Aw5DoHOc7M8PR1Ga4soJVCMbvYpT_gJv6YLUpt-BCJ3rV65gHIyvohDforaOmvYBa2Vim7sOeRB0OJ2u94t06ES-VXSs34QH3fXFOC79S3i9u7OLcP6N5GpYzSTCoW-VSWiOPdQrHUQoWUYR8SXT3lLKdzfAi_6CNZB2XL5zpcD0AJLKIiX2z6TKMlINzZpVAswbLatdyx-a7ghvuB0ccDNEqK4rRJ3aAasLRvgY5CuhyB5_uwnW2fhqWlaWD6-te6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f0fL-CmXPK2peP60HtIphg97_o_Svhm29oIAq1w4Rf2MVDzpZcUlAyhRUL_vMdSllTOdPTqsbEMQsjYXaau1tLNdjQwdbaFFydtw3wYhZpKJqv8wIMRJ9UVM0OeBEhl-9_6A5BhxtApwsKxFyNt902MFHDjOs96KU5RzxzNs01u-WSS6oYCelgVqVfkpWDorSBKYlqRzGbNUc58NoIb_zHUpQhBkefEyvgwIUTyam6GCWHg9u5xTzsZ5ocgza45TPmIQ57usTxJSXyK1ZxOGIHsRJd9FsJmfIJGV6zFnDVzqGVZFtZ6yZ035IfQHiaKcPTkRTk843ru0G4W_1OfEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D-7GmLeVz_UIwXXhH_XD5N1BcgSWWg7_jUsm3UJybEUoYJTMbbpjLT-r7vqJ5rCHmI9VCK6n-oS5JjsZc1ubbgzf-fjGL9BiyWHxbMmcIrLuYadHNJP08boYXARIPrPoW4rF4scKXjHmYTunom0ksVkG9FQ8rSd22uxWoDlihpnnh6MhEJabil-pvju5dbY442j2X3nI5MJzPevVOY263whcRRKDSIF-DBbw_plvmXwOtZuTBhPydwBeKMf0X9W2jN8XPEBOZVTqNuiJFyhsSBxXFy1pP8-MDiTwzo03NGfFWDqKn34Z9sI-SkhhzQsdI1MAgZIo96q65ItyltNm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jWZLY9KqH7PmT9M7HGzXvBaBx1D5yxot9Bg-aQrMM1ZHxkUuF07Kg3eQouvXigvbFjtec-qjhntn4XNcggt9l2RiXVQmPVcf7LJ6jOVIOyZsERjkAUHjPjstUHGPcbqL6hJ9pfR9wtirsWHSgdzwWBZe8eZEGKl2ifv5CkrfCB8WUEeOLrzLCHq5X-nMt7IoQYnBpvqWvSyEW6UQN74SczuViNU0_oJ2eBRjrFqzH4IdRtiwQO5uvYCb71oHTkFCJX8XiBcqTsO4FjlBl4PgGqQLzqM0hrtpe2LfRuKQhU-j43wrRC4Z4LYcvXkkIJc65u6YAVIAxFBa8DuVJRsP-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t1GBfaiHu-6yicPM_HLJEjENbZGfd2mlMTlGL9olFt2fh8mvf61tP-LX2CM5yOcSkmxTiqXfTOMukTGfZOpyxROTherEAJrsWcoVxb9O5WoxU2PC09VBMBVPkIbqWbdvcRlJkkSNBahx_hcx37dvRPyt6uD3o6vbwaDQgxuzOEzOVx6gf3Cvtio0Tni03rKKezStn34bzQmwijrb4MBNAr4VTY3G2xOtYFO4SEUownkDGEAuoYxvNrUB9tX-KuFYUDrYXmcwGKsaUZHvxA9HJ93-C7sn_yAtvx7cZFGqXiiUyelVnGCzz9HoHsq-zGOEU1XIJboPH9mXCodiD53iJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HoFM2IFd3QuCuwuDwC2mX5wrFNx_i-0Yz4-LPHFFj7NEP_h_5y1keO8OCzncTvCpa0-Z7PIJGfWN_Cs6dEhQZa8WHgHIOd0Uhfve9IP4A5UnnTS1h2FobjY5q26pWclG0tK4bOPfEuJsRKnu2u-Ce8n2Xb4nCGJGgNbDmskrigH37cRbsNg5D-orqzj_8jRvsTDaZ_92IBiLN3iwBpO72pih3x3-lv0bXtPm4ehlyi47GwWBQLEcVtNoAfWqMRCL1hV44W76jzVWZektikHbxUjDTWYKUU2VHQtm5Zoyryxa7pxF1YRH7dG3yqoW19cT5B88F2Htb3w3CSDFxwAotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IJyg4A4TIk8hF93sVllJvzw01Sn_nTcFQCSZmzuaamANAvSzMWI-MXg-YZwW8Ra0W6EKqginK6dvN8aJEQXYCxLibqcz4GL1Xm1whydcrTOlmhBPgxph3l8PfSOI22_vgy-TpwjufIXSeyQmuR1OsWa263jJBP93iFxBsDgQ-0MpJtr29HrEXkwWCZX1W2X0wU1gBp3vYmCu60fK9NewM1YupLyHUEzOh5yV6KooQo80RrchX78-oGwfclYNvMq7f_3un0KzHlO0kvGr9WQvtPlEReWY-vjtEvWDAMKPyAjNlLSvYyTST24eohojF9wRpQuPRGh3Qmk2PP_U6kGOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tNQQH7XZOuZrCQXZ-QQBUKZtkHFrJnRNkZxrycNCFpg10QmfDZTBcl-UwleDlRz8g7RFu1rrHILQ20wJxbgM88QPhmYJiOP5zTfOggrI766Z0WbCgD-5D3z0D7cQ9inrLDYQcIWjlW768FKnXw8uyyLfjg3dnIeBm2UJpgx5oSkkuUHfkEhOe-WY1nC8kOIfnWVdHp58oRupWAxBS4D6zyJoCgQHJDoQovDS7tNYTqft8BF2me5ioNdOm_JA0X91z0GLGja41Ol69M3SJj1xx1TKNOvjbMNOMmiZ756S3BJtdv-1zc3mwYtU1rJYTP2kYoanGdTtSeJj5OPHBbqNZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AMBJqegZmZPZMu7YPLOk_wbn0j190GXUh4sYLuhJU4CWVyeabGNz4tqsiaUS-5Z80TYBmthtgz968Xqb1IJ1cDurHlXjY-lzp6tvuc2jdTIndgzDqDWepGWtAjrJEG9N6MovWXk8DgtQmaV_NGLihX5oAkFXKZWJP2SDNLVbHoB3PFordSONpyfbtSbxezQioQDXWZbDRtcMFeDoLkiDA67cjwWV6exPxLe7q9Da_RgGanqzUETDQ4uTMbcvZsMwa14R27EbWqXUpjxMaJBe_1pLMKeKmmVD87f7kSFXDbY9GezFeHNcxrruKG0WWTwR7MjI1ziM4eJXAVLyeerbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hno2WJcK9-td6KAu1aKvEKZI4VW7W5K7f6lp6Y2Te9ER_nNW3wuqHYH-78OBWZbDzVlyzYAwc0VBMbft29_LDcJPbvNDce7_EIFd-Xg1Dkom33f9XugcqN8Wm6O8JvHWzaOQ4k4m_9vBNw2uqaFMSxx2ZuvIKLHPgNKiZKz4DaIIKGgGCSYFABWNQ3o6j_WiObR3pYC9YY0SdbbMk4Ojz4nBmKUUjDo60EaZyJIcNtt9ntRRYyXIU0AG-5GZQHYejKdbTI2DO8Z8sFYaJUuotrx9sSgApSY-4k7yCo8deA98hZsMFtsRQ0H4ugWt5ioujZdcDZvw2-vsUUXXX6zrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILXU2-k-XiW3BBYil_oOWdLrnY7LsXYPatLXMAftGBnSCekZ7jGhZfbhW03hMVLJ96RTWDk_ubsRdrwnFRykr3ZnJJMOGHUXSHFKXO_RZWbWAP1EGvGCvyUYAPuDqrbZWLCQGoCLKd2qRC7KR5iih4p3OudW0xziEhIlxqiY0Fg8uLMoRE1PBgcemtC3FPu1cwU2TvRzsh-Ywx3_XWTZ5csnKxp9fURfogpuBxT54SMy_dvczbAa4WuBR4zY-Mifmbnd3zCv7IJKr3hbJ0B00eXXwFhMEVfqeYjamD2bhAOOoeGe4uMeRku_S5WTCH8s94GoX6iLtOq66lWr_9lHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iICuNJxTVeHqLLg9ynuFK3ZfjWQMy95wcWoJ11-JLfyAxl5h1Tv7E8eN38YsGVRTGzZMi_CokGLQClUBjZbIpQktmMQWMS-oKzMr6mi0atvOEXhyOdyfeYv3kf6fPzMlKaFWqk0pxjditNPpZCIBnMxahkJ_Vz7QK1SWfoRLIHZGiqD7ovi9by2dkM00jNldVlrxCbR1Kt1wojgZqjiRJe3G05k5IjsP3vmuM8wucgLZLuQpSrnQUsCO8zlTcwUZM6grtRMJ5_l1yqc61MRxUxCZ21e4iAwb8y-NAz2-4iv6GIaBKaUoDmpODiSm6rGWu7OvLOXXLYcAFq8v-CT7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FiMKqPKIz_Jq6L1vA_qGwGI9vyLWaU-AkvrUS_cklKcW-A8649Hf1SPz0qZYy8cLL1so4Elqa2g9QgC47Aq4xyCHeH1x2KTjdls6zixoSpTM51JOFBYQxt2mLG9SDKYYeeN6HKnYU-iV9-gQ5fKQQt9kqfSjMoYArimD9I4w1XBcj35q85_icyV7IPbLQuMzE-_97Q4eKpnwJYTMKG39cWD3A0UdixzUrTUX8WC7WgQEAInfsHJZ81xxSi30BehunvL-V9v36qavYEZkac-dZAy9-6TvU5e1MP0mdST7CSK_H0EHHPcM8k7dZ17m0rOSQWPxOh7hilhAifJ2AIlO6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XpFB4MSqQYzfcZnnoONUjZ2Qe0qlUeNxxwRe6jTuzrL2umUL0-jzhxVkDO5kirlfdyVH2ugupNLziQk9189DQDaDYNBAflfxsLj7tq768WHc5c8_edII-uhviw_TkiBV4OmvxxavWA2YoxJILKZaYETpwkZyHh4dL4kvAVByljVLV8F96vn8tLu2wmkRR-pU_U1WXftnjG0EDe6ogvWYZtHhuAZfXPe6f5ngoRSw7k9vfgkvCQSczevil70nOAHqy62tJakndip5x2KyeqLW-WQtkHAvGWjfmBETGB6OUTR0gzRTdrUr-HBRB8qRC5zBWadVeabgzwZUdEOsKK_ykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_CXThXzsQYtpo7AKklwTszwEN8Rtf9lkyp95kmqReLthqPmT_txXBwbj4ayXiylbMjHgrPe0lannKAqq6bDb6P-P50uZwnRwUbVD1BXNcqtfo617Hi3f8mKqVV7EsLj08moIxBYz4ys5UiHnEAxeTjW7T5c3wqQbzZplqK6TOSvw37__i8v_1yVsl9dyPRiBm0rDZqv1exsfYAxNuC7jRqjgZWQ7o1-UQ3uYxF-8wKq9bC8K0jknBjwgSIwXp9xJTmIgN6G0bBrobKTNvvcpX98DbyZGAPm8_AA1Bvxhyc7cbqQ1dUZ42C6jAvc38CaeIvmxUbaJPe_Dn7fohCwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NaYQbMatdYVR-U8xYdjB5H_rKg_NhDSu_rCkObg3DN9zhOytZbXLFie8giqoS0SWmYLE_6-v5sn2dTwkZjhQFWBkYBrp-9fy7FSftLzfE-kLt028EQIoy7NhGnG_vv6kvi2Dpf1DDxk-4cKNxcQq-NKN5P5QOy0UCApGGY5NrSjsuXSDjCrk8BHUQgxyteqOsyYNlpJ1rtJQ5_JFiYUAJ_t1oszmBkH_xjOtsnvfDbz8dsKVFZ3UiTSiXQqMG50qnePZIjncY6iP9AU5GL2ontEklexOc8TOdVyrb1I8FkNer-WXKq46c5pDYnQMEt3zYAFunyXy-1NvSFs_7yFMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fsLSQ5T43lx7C376KO_2YrxjrmYAZxUj7Ik4xoKcXc-wkY1shjeA1L87KdI-ABOz4Cpdfly_iNWRAL6FOlmMdKXPqm_D_G1dUwURzfuMsXWtUmd-U-2Q-87hmf6Snill8PY6_HVg-OaFYgjwuG-eLEeNp3o_JHvQ3MPMPCFZWNnS24Yfpio48y82bCYZSln6_bJIa7aPelY-FvzZacAsqYOf3Z0rKAs4pg4fvS7zb0Z6rplPkqV826PqrYxcZ14NLO_GmOLx0v2CTQ4v--rFdTRQiHeGtTKWPt9IJGPdyn0Mk9yyWgYCuElSLzYg9EMIjVq7Rok_zcs4SSEXH632_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bqs3y98r0E2b9Aw6pu26jWmT-hDgzrhqC2jzTpiS77AehXbampaCizdxK_viyQX5bfCoXhxcZepdjBeR9_j_T-FMJ9wWsx6QPEYx1tX0VcdT14-ZDKyA_P0ynxYi1ZVDSmqM4MabAcwH_-oy4cXa9Xwf4KXK5_1kTakI4Jw5bI12yMMgT_ffZkOpjwjz3adqQbG6Jsbetruu3DUhyPgTJtPlR2KGj97xh_SpGXIwIFYn-zZlnR44Jfz-KJ6_6LuM8cvJE6oUCDybg2Ufn1lrX_qzYtcij8fYr8anvanXuTls9yhjVeYzAZ0nb9GX63Ih6LabxMgcCHtleiMJcfTEZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MJXcFwuS1xJbTHnZfHGL17YuM-v7Bcsk5BEyD1uDTrVY2R02aQTdTHOFPzfOl2icDaqFXET5N91YJlGkuQM_VpWRC5ufcPu15FPPBe2oXpJKiqoUzG-QpgT166KboyiqoC-LeXbSz5_htQ9zTXlPjc4zElt71dwFK6-yJmOKzKwGITTwGpWG0Kit7ay4ayx3e7uiiQumoJO-ln6COC9MV0eS8liIQrXEueJZNa9kQ5stxBSiT5KvFry_r5L6ldVmtepDyuVuC3PWA0yRqOZWeYkd84bS6BCYq3qU4hmepWl1eDTPRV_54294o-ryX-yBOElZ6XKUVVQzuoOK48klQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nDbmauuXcm_W0QwockZcyUuWgBwR4evM-aKcknw8wOaJKQ-4ueC39Wou6EbXfKeJPIhcwuOQSw3AZLrGEXoTSO2NpoOkSHLBZPFTDyr5EWkYQMI5CvZnv5a3WLEq_o132OkrlkfJ9VUC8gAYatRSgeShCGVp7A8B5b7Ba-6qllvYZYC3ePKjaIAMe_v4sa4Y7SYrDGOGDzKC9u77Ou6RV76V4CqxrxeaWIap5ZCq2bKQ_LehRqCaa5Dj9lzzjy3qa7io9EC1plep_R9cL2iZ4dEnxZPrssLTmZA9VQEroBZMqA-oFuDU5lvRj0iKtTtIpO-6OUcsIySg4yD-XvjV-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W7m8odwG9zokrFdGewf3Ho17rkFl1iFUmvH4-wjhp2a9xXAX7JiAyqXf00u9yx9AhqoCvmIVcCYWlfBpb8n8K_rieD3jM5rwatvKQRJqZSmySNs9jtwDmMFCuRWO7zh-KiJCElIW2isi-jdSVfDfB7V-VvSzMZLhShVni1tYt5-RWoAVVd4ki0GvOVy7D5k4fpgqynaAUSaSuhFnKhPti4E3sesAWLyvHJK6DwXDzsRznmaJrzdBB3_sXX9X6-5QeVjHIn9gxI_YzZnqn9b9GkW_urlX_UGvfsfK7gzsA10qQonTZHdc4P3EH4ZHcaSx94bVO8xsZKvzYLJOEkYDsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNxrHykzJPIVO0aRJHXXmfgT3uR4sEx2lE4Rl8AONIy3Pfb5twa3aMRVnx-u07kVyANdBqybdTU04XZQKy28crUnm7EXf1YLeAGVjjuDl0Q69btRCKhXtetKoDQeOpMy4omS-nv7CDwAQMBxnqWrAOjMI0fk5CbUc7_60Ly1gz8YH9KsbL213OuM8UsavQpj1WloLgq6Qmeee4v_X71hSl8TKnuH2c6Geny6z4kdKCiKfBuXDzedKRMYBegVUVfMAKfiqXvABJGkkksKhz71aySRKLRPWxSVBiaFL9ArvBTHa1RJ6IMHfLDEAbRbCEfQHxWDaDTAJzDv7oJoqaSFhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOzbPzzXI1HIptJFig11t-qFkv8K4Iy4QIfWcnNOROknPSu-TDg0II1uhC7wbGJpz7YjM1MTAmMHgfQCXI12S9QAZfy8LhBpBvHnCV7iG4IFOHQU8uvB5uRkexeDAGZIKqWmFdjZj9tlM1cS6ftBT-BQwqZmYEWg4FMqCj4vCTeGZT_bJARY8RFU0u1xZu0wkmcpeWcGTSViidAfXTpvjaEjAtZYNPLzeDMsgmqXoLu8aAsS8JSkTH2EX0ysNAvj8lynL9N7KlbphRIePlrbKVHSe8vimvC9SbmiJsKZ01VIdA_0TfgpHkHdridj92Fcr0WvK3-XF0Nh-C8aWMfpdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TtjIJqEkwqc_QbAyIfg5F6Zbtks5TD1jpnALWlLGnPR_OJUD32X1RiwCvhqJZ8tYNupk3pzvfHJf1zmSP6mprCSjz5HTvN-R5MT8bVV7QnluWvI8N2F82PCy_gUs1uPCmkYmJV5f5F9DuypUfKwwWseFX65edn4ZnY_fiIfD-vq7ftNRPO_YE5cRO_fzcbpK51Ypy-7xksJdA7h2HBIh_2s8K3vqI_TKj_sYiMDcf-9iqxtvsIfuZo80LfU6WSpGM6dStRPymecdphZLRDamvV9oH-Fxm468i0r3m8dNj6ZKv5by0j2Bv-zi_MHyzSHoPZ31da4Bqzdlu8tEU7zzIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s8u9SgLJs3ka3q6fCO0pf3EUNi3Sf3RR9iYAQbLjj0jn5Hs7FlXvPok71pTbrzk9kNTNfYJtNxmY2QCF6OiDHJDhXll2V5WY8kliWiBqR-H5RmrfKlOb1Rs1logkASST6gPSsewHogAZsbOA9wcxmv2OtLvDrLvsaefem0xEZP4slFS83FvYmMesS1VT_WWJg0QcmRfN95GJS9wdoRLP1wjj1HbtTe-w1jHkOnedBnlVXo3yF-grSLfV5tKOP-FsWnAC2D8HXY_IUqwGASS1r2IgKKSTLuwXZFqC25Xle-_OA7bqKwFZ3xFIO2xasbMoktfHOo1f15hcdkUkfwnSrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DcpZYsBFyhibY2Fx-FNpAu34deMtSUaxtjjL3885evQgS9KN9uSC95qJ6BMmMTYOIxR9jmYuFumpXKLR6dsOv3xLxZfpAYNIczvVkYGT-pJ8ZbkLz3y_VfeewsOY1JWAoRd0VV-dugVgIRegYuoO720v9ZoDdwpJeOQoWqOQ2U-FzNZtllFLIn2JVlWEdH-Dt9TyVxlmiuuLQUO-MnOw3-Xlp0jbRApWECdwW856AQwG0vstjVZwvkyEPWHsFqIrg1v-HAyOt4jbkMt0X8zsgQdJsm6Ngai-18qLVAUmrWIeyI_HX2Q76FFWrDQkpkQxhoydTI4gY09YkrrQq1Rahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Gp9dum0UUptkv0KVyV9RSqPUUMLUB9jNOjTQkl2chohH9TP6Zbw-rFChf1vLg0-w5XJgUMLUKy-s0kI5u00Fh3Y74VH4N--fIzcIB18e_D-S14aQO2YLL3VFWhceMRNX5xNXbuitPxXoBb9HGBKDhle5rTmsVu05wTPTz6807oOLaiwAaLTuNdv1C5N8WkKHAEI5uSuheJSBxE5FzupFxj2f-rS3Ee7mgCPLWDzB1IYSLBGvFPi7aWorf_Jf5LD4xvIOb0mdmwCRKYbjyGeVMj759nVzvlwEXnrVlNtO8lWrtAsXrLU_9J6hXZD_arsNxCkeR7sEH9DcBc5Uv3N8rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JpBxEecXwStU62-PNdVjajsJXgrSH6MxjACcr_xHUYNv-VMVNPVQRk91Cf2AvQ0jien6kFn5PP5nS6puuMMGJjG9jmlM_i7BCGQCGQsmYk4QX25GzgRPr2hOe5HclIMU5qxOmS3uOJ1rTvOy8L7vpmj3sXE0585QYmKlyGIsulnl35ZKXivIjiCiUghd15JeTusHI4WtkT1FqMOhCxfZqnxuT8z7QU16PowWVT8M9nW4eNfKa2MrmOJB0-BQCIcR556A4oA-LzLoZKPoP1OuvQbtCxwevjVyM6vEErmEup7Xaaw3Wy7BQXheP-ORTDlGCy2ICQy64xvL6K4OBGgrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iTpFlMJDr5xzbsSdG_pUJSEOFkfxKsjFehSmraHglCrdpc4t7yHf75QujsnVQPyMx_ZwI34yfxj6FPmJnC7w3yn59kWgIQsEmo9XBhr2AaVwYig2Zmw-8tmoeqG77TP10x9iWgZci-sI-tAjS9rhPAmUBrsx7bTMEW-6Y-2xJlsdoEV0ath5Vwz6P5vuFAkFrOiltKLD4SuKaacpTAFd2X9bfnDosWf_ex6gioeTFrRnw-WwuTSpaEcK_vTfKTzp2QOw_IaTGo95JUnmK9V_LgUwb5qVnPz2i808DjwBCi4d5NEZp7gkhf5TEZO_Fk1EOHx3qM-CHGUNoD1fFt23GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eWnkgan75N3U3PRpX1hYsCUah2vYCCaD1BU7sd63ZXbwhR0KeKZCWfVAAMPs-fuTbLeYfzOtJx_x6GYsjc97CMNLB3BKsJJwXMhxg5BdGhgtRqC8NOc-ZWYlBHhB9f0XlLv9pcDmpd9JkhKYOucvSzy5Nqbs7mMWKfecOrTX-luBWvtN0VVCngmvJPwG__27m-dFHOe61S0VQYmTfy1X37wrJmTj-eeOS7ebm5FRJcl5tZKR2JQVGbBDYj8tobLtLbYFCgWxKkusU3SHUy7s0IcwOvGfEN49MmBcjmTzuIFdtqdwmIAj4HN2HjFY7Oab-3CoESGap3RRs4QGccBFXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CsFZx1LdiL-is8AJLAzySgvs85j1QQuGVCpER1dDwJP1HTstRajC2Ba8U6hHgzZLaw5r2ucxZMrT9mSVD3fXj2ILDu050Iwg-mWnHxv1EnhuSdb5GP0FhE9-TRgEooEsF2Lub-lADWTnmo9-dbcD6Bbc5Ly4ozEn7ASFLNe7MEhonvvTNoisExGNsmWcxG5ndIAA1iOelLWnzU8p4FYPkdEGKVHU7zntkSExZ15CGA7xrwqU8kX73KVYjOLAgvpYw9mmkwzhpuur9jzts_PJviH_fqpywDJ-iM8iJ7uj8TcCoEnCM-TWd5ssGsqucshr5kar__1H8Myz1yJvVynLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VSqM0YzogBJLu5Gf5t4avds1ROpTC4MJEZmu_4653YhsjSuzbceNsVnz4CQ334cB6YqfnipfQ2DB45R8uObGF90iBGwtRf16Pvhheyr2gCdvscf2kY9VGH-cfuHHcuyDuSVNkMZBEgFUzIGJUFIOf7yOv7yDg_6GVXmk5A7sUY_7AjT4k_umvHGCmsIFvIJo8wyaCyyLm03ZQcuuEjRfGORleWQHWjMRpErCC7rEwW3SaH_TGz9NbbXRwkaHKxm9Df9Jtkk0F6vfcmOFgbye0e-ML7VNY2-hdrid0OMmSelMpjtD1fHbyn_EZd777GHjyO2o8geimLjqtkaN9RCYdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RBmJ_DQ3VKU6G_Xg5n1M_tGqbV21VgZXwoEd8aJoitj_dqH_6nhgwJJC325edgos0DD9xptXMpff7M4-fXJw2-UHlAMGT4V9vKkOotPiMs5yAAphgfIeyX6_YmoyWWwOpdSUKX4p5h8MprBl6aT30c9Zz6e2VXPNeY2Fnbc-mCVOlzOPV92Y7z6i4oQdHrzG96XXO3u_NZDTPYhpoz6RdPol00Bk7nXpebFt1y_3MF_TQWKBd7AzQbeDCBdfMosFtv1SaNCC9cVCt4VvJ3qKYkswOyVMPHlT3_mX4wXHIPstidms8LamWnOuK0pag8gJlrh9p5_2J1mJ-0stc0DgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fUVM28n5r6LVITC354EMEfgdTzcXJu060nhwv-jtx0Rh1SsU13STRY5SxPZk5ZNuDuXfgpGq19jZA7mbefJ3p-470Qn9OnlD3_JqNKbco0kH8I4R-MwhhXkRI-xJiN0_WNTrHKbZUsngiDHeJj4C_In5N5AexbsZSvfohQNbRUQwz3sYBNs-zH2ySnAnZ-icMegANs-TMZP6xm4Gh_MgLtbDPXWsdwl5f1RnryXN0SMj8fd_znEO_sGDtYSfIUlP53Qn9OFGIo5ZwZM_nnuauczVprX_ddc8DWJyBTo1Bs6FpF9aaB63xUnD2lwhq4Y6wcSQlVXM1WHchwjv_wt7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s1me79oU2bNVM1Ll6P8oT5kQQbXnN9wyh-3olZ5_RUUfLJVHyY5QigUWlno8Fyo3oISg3L6pSBl4gTScq9xPvH6UeJX5ly3qg7eeuoQvWh4OJkfpFpuj5CXJpXpE2LHE4U829dqKj4ilc1U59v6SWetzQnmz3ZIrbgs4vQXWSdB5kQxPgAhhSHTkIYqKtHI5Qe68sYQINAZ90LvSDdha_FKjoGpBAYh_Q60__0Ejp6ZrWKPQjUek1JFYUkkK426ejzs9s0XLiflNZnEVLWrDH3kDYkVpU9YuQFhPn7baaHr2PXZcY7vfyLaw1QTbR7Kz0Tx3Jd6vaB8xKMP95K2tNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kHMf87gVfuqcjgSDxbiid4Rquf2yzsht3eyoJWCEd-01YXSdI3eoyg5Av3G07VtnAekzFdZfdrAOP5HEmjHhcbKyvlyWaKRPc6OnnE9fKYwpUDAbB6wUczlv-3QPf3rMNrgiU2nB2D3Ytf9ZjLJxTGm5a9OOLzA90TreEqrGroo_KIYBqXxXzsZLcB9adnKLHuXxjXCuYHsZS7hKbfr3yBN_BuGrdP5rpGXeWdINq6IgGQgiwCpuj5fARzjeAnn4RT7WYYalHDyor8FROQCqRAO_NrYlYE6mB7HSgCWc3k4YfMLr39J2K8d97Z8RhcoztVwl-2grhDWT83XwJF4QjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H5r05pTOehD7TRqY5N7Xplj3sXVgeVLPw6BY2zLYmVGuY6LRnNKBFfd0q_AHJ3AQ3bc6WFKwnIe8vRYfWGW4ONP-Gs98st9Od-fXD5h_RUxdrZMrY6zopOnu4X7BDslnCzt7phUOdIGgij29LvX5fOwpa6resz1pZohxcgIeCoPuo_DFgo5nrpZSD5a_CgqUOgwYDzHjaT37L8Fww1JuIdLyFyno_hHhq9SV3goCX8Ya7ZX6xRhcL4F5QwRv39GU31WMr3La9EHSLrDKF8lDI0WU0xIbuCIm1jXzRvoeQ0wqgR17iDiCXD21L08VEFZprpjyp8QTrYtWAMUY7Vlnfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ekHCtAPbOFzK5748bMsra0YtPYjo_QEaftNPUwWxLWKVgiYN1Yu5pmOc15lwWrGXRil35yaNsN2kZPcxBAhDWKHx6ESXOTUkeuJnqFQP7NnLFyvynJimMl4_orA9ZERebY_2hYaeyC5UM_3bx95niIk-R_GTsYt0y2A-l7e-WMAVHtfZZaEI3JUs_U-vLHTXtVV7dDAxpq9SRUh1SD-e73dFxRmP4Sajsa5GaF7A7nBqnAuCtIzdJTR5Yd0yITL2jJ0ePlQTdeRC1q8JkZPl8Rw_IXRKBX8RBLq6ssjqFdsonbffKE_wfH8VbQvDgh_FlBG3JR3Uo1LtU3LnfZwUyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LyVpJm2dP1qQ94Nl7qaGZBZDDkLHryMIbYUaig6IN7N_s8wFj33Ujh404rz97LXFRpXBf9i6mF9JfwOsdutuKpnqbxPAO_ZV2d8yGP-EuThODkB6TUeko500PY33n1ogllFwtC2S-byMqWovO3_hg8EsoCIyFbcLS8N8Q0kvrjHsRj8u8uccIwoxgBVhI0vqHnquH4Peet6ZhRYGgocoVnv5ZFon-2gPsvORMJTiKR6ysjYKa7VFzVNn6SFjHdRiluLlUbQ-ENrQ-EFHi4nmwCFPOycM7xeiI0ZhxY00RSBOJr2oh5rnf7mqmCHZo0EdV5Lhjr-BTp4uTb66Eg3QGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gWhxqvl7NzWoG28HFXVwb6g0rtlg0hQ-2Sv_zFU8I25kuWMGIrGkK-ypTg_C0Hl85zAh8a5vPEnfSLldKeOdApQKhj0osWcWERy9gOleIhbFoiIi39MZPlCxM5bD5aNCsrZUE6lOUdIsPQX5ea5lBGJJwmfCZKa8lGFnGoBRH54gxkUuK4iLol61-P97SiowHmv9VLzu5Po0QI5XucwA99iuStsa7HUVZVxM3eTvETEfrxQQRgnBR17ngOyWizenoQ759cG9fhTtNzQfj8B0clHShGBU3UDjj-322-X4xODjko7UxorZI6hpSkJiwlVPA8DvTX3gIfvcd2yLQV5A7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
