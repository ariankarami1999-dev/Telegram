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
<img src="https://cdn1.telesco.pe/file/Y9vZ1uRvNDiTIo_a3_SROBlDZAYJeKyKOXrHWp1C0hLwMJeJ8PBSv_7AhwVWy74Bg2rQDdxUNPYep2qyXaNvDTVRR8IL8_eBhsHNwZ15j5EkmZiWwX2uVtifBp0eTVHkzaewY1RxUIB-t5Y2HIDHu4QP4RyXpUhMBtMdxH2hCMAlHI-nvKMtap8PQYnHRjizSywkNOPMVLmFEWo-wbdLuR-E0zxoyQ9pXoHYaKILIBf8TCQucOjb3BwZ4JvpOVu_8uMbvFHQFMZycsRyYlh-bukDInNTpLYyddZQMFEf0SJDR93818pyMZDWwcj0dqRWiB0YzzJgHnN7sQ--1Gq2Jw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 00:07:11</div>
<hr>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gd_m-KAzdFQL4jYzu2KoQvKNBS4ACvKVIURFmdn3pZte0-jwQNTNWcQfE5Qnn3t0nZSTrnDZ8Fn1Wkq4OdCiiNx4fwJ9tzMKgnhDJOqkylPPws5_QnYPxTHZgHqG1RG0QwhpLpiZYmfitS_qyQ6xXsmK73xaNXq4AyXt530DQaOFWuBgq0WAUONOAP0RKmPpzbCZqy5psK0EiEowlRG9bpcZgvqt_V0nU8wlkPhWLRV2DOTblMuYagcR8Z7mPXpJnx0ug57vyLC97GZdGhUrq641C4mBqdYK_mbNVLnJP5DMUYfZKykwf2PXUpDqYT1lV-pchELifvEv7dPNuJRXUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ex3PUSBhPyQz0T_8MQwvH9smV8SXfS7TyHyua7Jj8EfYggD-b2nu2CiX-5-UnfPPUnBrMZY8UCkD-JbxOT63InMar2B0A7WgDKTXxikVoCW0Xvanrxu7TnnCJYAP2jUHmcR1IwF8a96LVICj3fpOR7y0M29jx5XMuqcQGtGf1bScDGcGRSCH-k-VF34rAVNfJ1pLNh52jdeTTpE8npPDtFlJs4C5SAS_X8F-9s_evgbAbyuxehI_J2FoW2Ug7aEip0B-27nhKaUgLaSGZIq7IsI1jZZ2eOL48e3wgbw-L0snmk0jbsxCoW3OIEZZR9RewJ2Bed_L11kpC2JdrNAyAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ufqB8AjSs5HYCs5I2YK7zVcuUEBsIDxQ3qckBK_Pwu77oYzlzE76KuZNJGk9xZTALE0zuhE_ziJCrffnRSKpqK-cg4pChlnbQVeMpyEYhVU4Yn8KXm_bYHbi0wZDKlRq1KI-5AN_J9Uwd86DO8HmNpiREAI5F0T2C2Um26Bl1u0FKbTV8toioOl8KgIX6P6cM3XIII4OTb1WcjgI65X0MqHyoedPPjlsD3rOsyoaud0PDPpTJc19IlUVSNX3vhBFeqcrDFrhVhp7tQUARv0FRUTmMEfWz_v_JkS7WdKV6sPOcKu3X5tq_icQA4-33Bw-WTtDv2eqLtgPGrWK293qiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=ufqB8AjSs5HYCs5I2YK7zVcuUEBsIDxQ3qckBK_Pwu77oYzlzE76KuZNJGk9xZTALE0zuhE_ziJCrffnRSKpqK-cg4pChlnbQVeMpyEYhVU4Yn8KXm_bYHbi0wZDKlRq1KI-5AN_J9Uwd86DO8HmNpiREAI5F0T2C2Um26Bl1u0FKbTV8toioOl8KgIX6P6cM3XIII4OTb1WcjgI65X0MqHyoedPPjlsD3rOsyoaud0PDPpTJc19IlUVSNX3vhBFeqcrDFrhVhp7tQUARv0FRUTmMEfWz_v_JkS7WdKV6sPOcKu3X5tq_icQA4-33Bw-WTtDv2eqLtgPGrWK293qiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eAALLGBKhmHHX3yB9OYwKcqQyEhH7X-d6uwf3vthJqVqBS1cVxaOppEpShFLnji5jsGU2vRkAL2BNns7dX-_JOEqMkO5wmiVATepFSfr7aY8kO07M_3Zdw2z6xHJeV8fsWqIjztP7AHOrW0arZojvNgVg0hs8COdGRkqlESTjdB61TUYK80uiZAjOGqIwVGwXKEzvxvnSyGtg1lqqpWJ0aPcm3V0X4H5vRVziaSxyLxY9WhBWMLwO36pzLpaLrHM-S7_ZKYEEqMnVMSkkLn3LO6VMW9e5yKz__QtDfGqSuLwy-nBhZhMJfrAfNBTmL9ZzJ9GezZwpN05xo2BRtq2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K1lwUauonw5fvSrRF0uBN00dVNkWDwjD-o0QQva4NkYwKNcwZd0V92YBp3hKIabE6z0OMs4lwdLH6prACoTYN8heTzOfhHRWpIclzFEKdnie449XrxZ7KsMxnTlbrd9m8JUP2BD04uPakShq8GoKh3niI1vaiStPU3bRuAeNJ9lGNUrnTP3bRit_HkcJMTxk6HH9-2TU6aWAWC8ht5uZ067_a2SmLl0ogHDPMh6ap-_213-Yhmk09byY7LdillS_SZB707Jobo--g8T7mDGnTxMsK1l_RLveQR048vL1ieN-J4Qv3ewj19YlSH3C9XAihICdPqNiLaOotRvtEX3wFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ncdqz64P6O7ZHjIlfGh8FmtJCnwGtiYx8UdXofQlnSG6INCr8yP3Y4jSudzWk3uzJf8D-bzmBcbU4JFdE1jIh3lFTU4FVZNlQ_BfeTKQaFygNjNJVDAdV1FWt1pxlpeIwAH7LR7gOfYp8-RDuRO3GZy15YR_P4kUxqeGr9u0AY_vRDBLWPTu6yI7o8KEvLNkcbPTw8NKshH8s1V4fPUHJmp-gDOu72KH1bGQVuYJ5AOJO0YnXD8JKRTW11P_ePFU55beBkFYmaR1P-9Eoj9WBBoE--YWGyqklnabe5cDTzz8hIOrggcWuDUfaUoMgyaou2qCQOdfyVpXUOsp5LSmtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4p4yQtad1WlAEPwWLEouGUDeAZ2gTbOJxqV7amUOWYqfrMv96StA9O-7nPJXv8YHJRQaIHfxXzN4eBH8TNefM4dFWan0yW5vmeoGRrqSYecTeaeLDaJXPLjRO9Th6LhQ3oRotuo6Pv2uZV731VUcU5DCP420-zJDqFuNSg7pBbRwKdE29PrBV-AO1G-YXV21GWr0ZaayOVo7T6bBzYSK9fTmFgLj0DHMVikaQH3AD8GBCJUx_IH0vAnRQyNezOU2QOGk4B3KjVO3ThFdub5VK0Xs746KHCAbxKx5LCvldlKvjJ0fJUnWAK8uvycDbo90jGcqNbq6HWDPZz4BzOp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PDv2oIkn4B-nGKAx8yaMC-MTVIJIL1TM_-DPeUWH7M2oiDW_EVyEA_2B9TuYwwYdd-EUM9ncHr_8GH6DYiUshpxyQ1Kz1_8YKEzhM_qKwihgp7j7d3mKdy54Asqf7j0WyE9J0ygMtJ3dyVhLfDUXz0cidaRvqEQb3sCuSVSmFroia39AtAlKEyWvryu0POaYlysp0CVy0jg6RvZVMPQXaDCcm1_UpKuHzuOzlfJnOW3fCiLJdFGNR-r1j69AOgPOo7PeYmSVfKPQIUnwymq338ZZNauKiYfQEyXNG9U2DI5Ewd9Dmm0ctCm5ZRBcF5pQtnNDT9NKyZ9xys-DiymdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vT1317pXxIX_nXsjrF2JkEq7KK6wMJ5-1XP--b_IcFE8-Vthw17Ev0HoOycQGTRfMHiyOfV9H7AguNZ4Ygnhg2sk9i0uIDicSxinFcb5m9D7IcOAmIqefVk9f_QAOs2jOWWojud21wZekg9GH1clUFRBzuvIvXb9LW-WiuCagO9q0Fz2eY9SsK4i4w3r1A_C1cakNjsuayf272KHpbD90mfaZxXnvqWDE6_rSBvR-hsiYhfbeY7HJRsZYIk9rH-Yex5hBSR70OTgVCqfE1r3p078WPomOoez3IL-BthQXBHCzOgo4IvUIwvINEgD5Suz13lOLiGaU63FFlkEfiBFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rO6n-EZbz9PeDT9APMy_B5UEbU8jw1t1JC1sgTWIQ5lyk5REtxPAdZs4jICBdnYa1ztx-17rzlW5OJuvViQrAUFE7cTpVv0le7CtuNqPElKdKib7JnQIAmxi7cZX_-88I-u1pZkEKXvf-_yQCvFbHZwhqMwS8iSqYfAeNbMX4S3Y02_WrogEHlFZybY_M3XKbdEDF6113VrqMC-idnCzF8Csrd6AdZ7TumuQQ47thogeU7zTJN8JDeruYU70_JV3SwCVR4bzRT2bfb9F0dpqUzn6qYAwnKQA8tnbn1CImm_XDvumuZz3tGN3_eTWZYo91s5JdOhgF0nsQideoqEGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m2T18PRGHgvMrzq9HI04daHLDQ1UxgswDCt7ZCsNwpW_1TyaB8p3ZjQ3scq_EFNEAx9A8nGzl4-u_6iIFfXBu8lrAN4VX72_d95w128mVhw9aaHDTLcl0BmqRw5SIUcbAxiJCA9RbE3JYovjluFJpzelUVa00eRGFWkFshkT9QdS5iR2GVSyG3_RISsS_gFqiiaqS77QVGno-57Xk2OS9-GMtWlOunZYm0uJG27jzaRKVpN2PCMLm7ULrkG6CR9dJjhikTNOEQZcfOJkU4C9aD9uVIzelNdIOC5y1jwCNNkX_kT7CQUJVqrsjsnPJSI7bO4rILtvDlDTTQaCjjSYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5tP1RvO2jHaMyBixap2oVTcXbt-_HYtsAxtDG0Yy5i_Xt2UJGB810hdV7xwCzfktcfHw1fil0yToHu3lUvTqCk36c3ed_iwP2Yvm5b87zmsL19Oo4fROwLh0ixEIia7Tn2l7EWBUledOEw2VVnjx9fuIi6vHev1KDOa8MHQZI4OACav7pSpGzoziJB9Ob_URHPWRBu1z5q2JG6Y8dkmjb9HqkACEoiX0n5IFYBnNdHrorpw40VfKtY2YcIfrIFDBHHeRRf1LwUclFilGSvZ21xgglMkh1y5QjdTZ3DQsnp3b8stG2L-eUGo2BDFO8Q7Ogf20xwfekZ0pqLyTp-lUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Iis4pXps3D_CIS-crOl2b4RsqJGmsNQhwJe27C_kLIVrq42v_pvvC0K4b6vVmRZ54oSUUO_a06Y3fjM6nQg5P4ifbj3j87Gs9duN1-TyOAE2JLsxjTWi3VqTfton1npRWFBdCdOe8dT0e0J6htnMxWg_wtmno4iKeIxtxxl_eUx_aozADmB4UcXxVFDuBQoMirKPUg3Jgl24n-mkk9wyZgleIamry6zeAXdIGctI4Te9EqmGq7CizRhS_pENiHdeyJlY2DTZw9Fi3gB8szBTB4Zq55CZ4Dvt5l-42YE2nZ47UjYyBQbJsRBOBWJA4_yDLfQR1MPsLcVWx5aoliZuhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OzeIvwx9wFBX5sP5AMNT_STPMaIPiW3baofT8ID8Di6rhnmHWeGct0ZMfojo3HObXejp76PrLKXvIbRFhYyVbbzJUY2p5q_Dj-28pYkA-_hEHrnf1j-1PurYePY0ycsoMBMTH7ETn779Hpm5K5t20SNdUAhD_ZQPr37hJNFvLah7iiR-KhWNxeax9Jx-Iu-CE4C5cx4MbelaEQnzcuBP1BGRg4omJdS-SpRTwtDALFZUF1WfEj41FJwUsY3rOU2Prra2pVXnuboB0fkjgfuFmzdy0Jw3beWpl32wwdKqBzyAo95-7yhZZIsEAoRWrKH1gOsHVo7yNZAxK_pTy1FTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aNKx3eK99_vGq-akPq0aG494cZTKkjkVPeRPtvonmkpwlzDbT67RRuUeKkVCeNazKOUD3QYhQdfekBAINJuzKG_Ow9mcGTuLPu8ebgqIG5u6WqAvqk8-Z5zMWcQPc_MI6ai8FNDCJDOAkMAKaYXgiyxuceexe_rvV9KWyG8MJA_qxc_ZZZidbsxblXoJ8_wtt_KvuJ3Eyt_3yymeE0Ttj-lsxbN1cHd9WYJQY7mVhYVn58qG4RVn5H_TMTllpgg6aC4t7QgPkEjXX_8QWXgPRJ1A__3Bb9SMDnC2IOkMDVMIDobHltl3eWfwVZUXMDiKPQBh2aUXF_7cAGOU-LnsOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jbQQeLN0xdpzGreyNgrXqJPkc437cMmxX4AfUKDIXZZ4imUZIXCnaCwg3zXYDEBFlsjEf_GKmcKlByM0yiMhvNuZJdtV5QsOSvvAtesUPhbaituvBtnFoyuJPzBG4yT8M65RpL7wNvZ-9p6BUy_NsChTtpJPeA_WULX9ddk3fv3_aSR-WFc-AnMn3ih6RaPZoo64JSq7txoWkGHbyoGYDduOf7BiJvO7w3SCyppx_ZS2q_-wrDRzImswvQPchj6q9Hk2NNSJMqwVOyQKwTQh1n3Pe3MiWoQiZmOYQwArmDzScN5hIeRydobilu6mpSIYXuXUdYvulfoRvI5WvB5skQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I-pFykxe9s8HOYqH6gXsb9RDhWTHaWehruTUElYGsSZzE2skklmCmG5LYvdmNkcjskk0QhfunT-Alvf-8A4s7VhRpL1nFPE6--OEM4pL9GpAdMBYMoOFfsWdccCKLPJScirgQ6bdvdkbZCF__7gy6iLTg6bfLcUVApL7vB64ber2GbtNgBilrBGfrNOSbo4vaQFFAZpxslJ7x5lEe-a5cETCHPftRlDuqQzQqB4b8e-S6XHJmoXGY993LCj5bu_dCmVOxz1jamdvpM2G92FbocO1Ee0--BjzzeC0ZYEUueSCvaw-_QnhDWCIKCdMt5-FHjn8WXkaQOAuuYtbGH3lRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d_tWQ5ZF5LQxBvtSzi2UMHHdVObj_xAr0VKle23A8GoyzaGr-thy4tb-bhQCzeaJBm1_ScN5N0fZ4C7Vnl1PlcZUqYaz7nldGlcIIR6PnFqHkBloIyY7KA-t-zwjaLNnzzJmBWgZB09AQgCxLrX6odlNOIV3UddU8VvuEzfCi7QIj6pAfR-nCG3yeupepUHyd5QYpmbOijft4eC7di78uSuVdi5aY5yZD4qBaXVjjwKt3A12kCuBmOoM121iBu-2_Y2sVcex2_r-hz5VDcNgzNsVxD5Sw5dOTqyEjUAW7paz9zxqDCpmUQ6wqBmx-mA8MqxA-av61vJDLqB6pg5WEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FqwNrm2ZjX1jUE2LInzMAnIq1s52rbvjz5kMfm7z1t6_VNSQ0svEiOjGbGdjVJvA90u3rLya4RyMtqmBw46Aw5DoHOc7M8PR1Ga4soJVCMbvYpT_gJv6YLUpt-BCJ3rV65gHIyvohDforaOmvYBa2Vim7sOeRB0OJ2u94t06ES-VXSs34QH3fXFOC79S3i9u7OLcP6N5GpYzSTCoW-VSWiOPdQrHUQoWUYR8SXT3lLKdzfAi_6CNZB2XL5zpcD0AJLKIiX2z6TKMlINzZpVAswbLatdyx-a7ghvuB0ccDNEqK4rRJ3aAasLRvgY5CuhyB5_uwnW2fhqWlaWD6-te6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f0fL-CmXPK2peP60HtIphg97_o_Svhm29oIAq1w4Rf2MVDzpZcUlAyhRUL_vMdSllTOdPTqsbEMQsjYXaau1tLNdjQwdbaFFydtw3wYhZpKJqv8wIMRJ9UVM0OeBEhl-9_6A5BhxtApwsKxFyNt902MFHDjOs96KU5RzxzNs01u-WSS6oYCelgVqVfkpWDorSBKYlqRzGbNUc58NoIb_zHUpQhBkefEyvgwIUTyam6GCWHg9u5xTzsZ5ocgza45TPmIQ57usTxJSXyK1ZxOGIHsRJd9FsJmfIJGV6zFnDVzqGVZFtZ6yZ035IfQHiaKcPTkRTk843ru0G4W_1OfEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D-7GmLeVz_UIwXXhH_XD5N1BcgSWWg7_jUsm3UJybEUoYJTMbbpjLT-r7vqJ5rCHmI9VCK6n-oS5JjsZc1ubbgzf-fjGL9BiyWHxbMmcIrLuYadHNJP08boYXARIPrPoW4rF4scKXjHmYTunom0ksVkG9FQ8rSd22uxWoDlihpnnh6MhEJabil-pvju5dbY442j2X3nI5MJzPevVOY263whcRRKDSIF-DBbw_plvmXwOtZuTBhPydwBeKMf0X9W2jN8XPEBOZVTqNuiJFyhsSBxXFy1pP8-MDiTwzo03NGfFWDqKn34Z9sI-SkhhzQsdI1MAgZIo96q65ItyltNm6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jWZLY9KqH7PmT9M7HGzXvBaBx1D5yxot9Bg-aQrMM1ZHxkUuF07Kg3eQouvXigvbFjtec-qjhntn4XNcggt9l2RiXVQmPVcf7LJ6jOVIOyZsERjkAUHjPjstUHGPcbqL6hJ9pfR9wtirsWHSgdzwWBZe8eZEGKl2ifv5CkrfCB8WUEeOLrzLCHq5X-nMt7IoQYnBpvqWvSyEW6UQN74SczuViNU0_oJ2eBRjrFqzH4IdRtiwQO5uvYCb71oHTkFCJX8XiBcqTsO4FjlBl4PgGqQLzqM0hrtpe2LfRuKQhU-j43wrRC4Z4LYcvXkkIJc65u6YAVIAxFBa8DuVJRsP-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4TIYYeXeQzerCs48sfYfxdbio80j_zweRU1j3zM0H4pHFYSOdrtRWqxpWm61J6UXE70oIShyu_mVzxGK_uunBIIwiaR7q_mIw42NAY9kb-tcUD72u4NpeFt_mSSNFW-WAUJUwX10f9M4hBe-Jf_4PiRr5KHxRF1CuHBc_1qHgll56o3nE6-jRBryucH2AjF9H61PSjKeaKbUnSwF5u1JN7T2fU539S7Wp8Y6fgh8TJNhh4gm9rxqYsIJ9f2yib2vrChUXV2VOffvkPjiSKUBxg32Ss4AwtRq82-yxHTn0tDHSRelV-tienvt4Vty833Dmn9_yFWXPkuFlfgulyNcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vHmf4udMKCpge0SGnVUXJJcxCtjZOS5o9IGqyfOb24VEIhENg07DsW1_8TzXOKLOJH77rbRhX33Prm-LLG8r1_-g6pRcza2kx6R_qQqfeflfJN-7Hf4b4ZnH_RjcdGNW6WNiChSY75P9xrxpkjc3caUEqu1KK63GfWiIDHaVEs891QyZMwJYrImMyTTAESy1h6H7wKsU8XBk3bKUl3oBEPoPvo9IaPKvV7DvJtazO9qIrM8A1zCsUgUXNx684j4oIAWswNuGlp39rqJvxGYkEppXcblV4gapDSLZZsXvSgtAgQvz8BbJSupI9PBjQo5H0tBEl4Qldetkk4BCo7gaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KvC5VJqnvatEsFH9gYjFTNsVaNZQ3sMup81k70fX_WK2xmBAlNH8qo0hNTx2TrMVencxk03HSdVCSyy_4yQP1x5MA6RC9lHPkkZgSwzZsUMGyhqjm9KZg1rYIncW6Lqm_twgtj3yeAkxVNrVPE3CzpQtwT54DnizzhxrYi8It1PyxKn5PRs4_0hWF3CK45vVkfCkbAiHPcZkmnJpHkSgfqy31lfx1rnj3ui7pNJcHNrE1FleQ4STEI6ts_B7-W7n3Nr_5kTMov_9uZz3QW5heAj5irvTH834l1FqSZ7d42qDP80BbasVUE6y46exiBUx6hfmqX5bGzakiC9M3HUVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HoFM2IFd3QuCuwuDwC2mX5wrFNx_i-0Yz4-LPHFFj7NEP_h_5y1keO8OCzncTvCpa0-Z7PIJGfWN_Cs6dEhQZa8WHgHIOd0Uhfve9IP4A5UnnTS1h2FobjY5q26pWclG0tK4bOPfEuJsRKnu2u-Ce8n2Xb4nCGJGgNbDmskrigH37cRbsNg5D-orqzj_8jRvsTDaZ_92IBiLN3iwBpO72pih3x3-lv0bXtPm4ehlyi47GwWBQLEcVtNoAfWqMRCL1hV44W76jzVWZektikHbxUjDTWYKUU2VHQtm5Zoyryxa7pxF1YRH7dG3yqoW19cT5B88F2Htb3w3CSDFxwAotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GcFkpPfZG_eUqtzNPMvn0TcubuCDSsVt9VGNzghXVijt_4bXgQSqbDgWGxzaWZt13vyJ5JWxAgje-5uye_zDCD2YxoyJofUUNn_qNeH1sPsVzXuFXFeTIU829Irtqd01T-RLPb-C5Ya0S24zsn37J8tAkjL30OxuxLqcplyH4OhbYM8_wkS-yurNe6rQ7ytLXIF8Pe9_1lIPAuvxueV4B2wKkFO9qTgpaHRkV3QwbVlRVlLCNHuQaX-suSc1o8M1LM9_USDv5fPEO4ZTjnOzK7jAzw31tXGvzJ1tOMLcjSRwx7FnKaQZcuFLTsdlWc6239pkFc6tpnJN8o7AnbBjzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C4o6VrK16Fbkftebfmbz0Xg8BOYqdIJxcOyRVx8QBHSuz5cH3rxYEuEaONSe0g__-kd3Dl6HnYKIheRzb_EhIFIXxvAjCrICf0TL_FQIHNf8SIgIq4-iN_h5HhSiO_HaC_dk8ho3W2YQuXJePKw_2A6IbWvCKuHKkd_1U5OeA-lGrFr9mfscEEqzT_hPCyYewlAsnGnCb98A8R14kBDgM__uFj_kWP_kV0NBTnBIxTB7NYKcCyqf7Qz0VjEBpgUJYf9a3XS5rs9_zjFholztEtoeYNSjoyDARdz_aPlJJYn4Cmo_8nJl2992IT4yJiGeOGTGXBSDDiHBxYZyz8yP8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dYNMGmvU8TWSlY2UURQITJKoWo7cIHsSjMQLpiBu6kWmqrA-0C5uCeSrjVa8AC8LPyr5zxF1eAhgNmD2LMzLAt3VHXwS2kfcbHXw_jhr4eoWcCbP5GhKdTjdN-DHIzXk8IxSj6HQ7-3Gjgqcn9JJktVS5lmxCy3W8cXKCeMdXvvFQ-peWufsZGqTSeQ6WEqZqxhqMU02aP6jPDjoeLw6oc0N5MUL008SKMZh6mxP4MNNUYY_7rwrhyxNmwToYayGR4plM7pJ0-9NRPXX0-dc32wKZIRMdufkllXvv-zzKIp9Am0M1X7rT4v0ZTwGh13HxJl_Uy10UAG5HSSBSH2Ciw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9G8W9ve_rqqO6yX_PdJd51RdgIQ8YP8UxOFPTKkJbXgqf5N--0qofBOjy6hpKqHUvksq8MiNKrAb6A0rYgNLQ4MuNC4PS0yC81r2e7U9EOZPNaxeqt65oeBGaHSpC8BhiWcGlAfloFql2FSRtpS_CD-AjQzL7lfEcUL4urrlc3Poe8XvcqMIfpJ9BLyTMbh22zvFjXY3YUDeZRtSmdzy5m544WR4YcHjrgA3lqj1OEZQ5G5UULrHdNjhpYzTp2FOUqPuKwnypDRohbP8CgLUWsx0-SSbfMH0Y7vfR0SRbrleDu5WinwdRHPHRaD3oATi6PjSLVBYfQWeZ1Mk3HGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oNdtKDD9hPdjoKCSQkq6JGIMPcav6kvnoqY-Nza1XrxWg4vcCcuYMr75ADtqEHfoeK4Qa7F4bgOhT_XpB3g1RMg8G3XpGanJtjslb-dLHdu_tLkzqYnoPPeq7s961sCi4qlwnuD_SkeGJGOEhgkxqdcI1AyG6G-Hc8u_nlyWYdPoImTeJZb1WTDXjmc793kM8p8yQ1UhpLoH6mIbzVZPk_jdWkBfSwK690hZy77dR9Xh8WC5kca8_wDSDDjPXWOqX1p9osFdlbgw49xhtDKsSO0ZH7-4joJZ_s05ddj83wJp_X_vi7l1JbS4ZoPlQC5jRSdOScwLCOxj4rVIwkDAlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qnp2Xs6xwxoARjeiGylFaYRQSrYwV1v-WMT67DVWySM93hHPWuNDNjVrzUjb5Hr7TKgW1XY5CQXmXA27OBQoGimnOIbbaYHJka13wHk6tWKsYUEL-TcuSEEFwx7NbUcgJKER1BjVoHh1tOo0dIPgz8TjBO020eo1typgITKeC4Z4JeJToWKew40AzWdGzOOLVNwz1qWRghURwybH10dAyzN6EVHaJw4B_sx3nJMwqcXi8lFaiewRWR6SNtdDPJppvSCfGbwm5whgCKYd0634WU3RmPDnfWp3l1yV5tU5hL1ZNlUNWxPqhd8KS26PSFSE5ilHI58_k93GtPXc2aCi0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a0b-NMXBTwhKJ1Mwv16ep1AFauLynxSVrTHlv7M150nBzuLkcEiMmmcZbjotBNdCNcBc-JjRldEAeqOo_iqNAcuR5kAFGbgGQKRfZZNOzWY6WgOMCnCSOvvPGNTMGDgz5s4Jxijq1G0avD6LsQ1ML40gLUUAyBdL-AwcFF-ZpMmJt3KE_Zcr_CAAJk4e0KmXKF0gVjjPMtqEWzj7KEdTm0QVnDsQ4Ois_qopBa8geA0YnjdH26kNT7uRcxI5aBqQJw_F5QuDE9Q1BdkWWpnraJnSzQhrt4384Tbii5Z37iAo0ZLWKoFFaN99nUpI0qXPh4iH6uVIH9Q6A5urtSOLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MdBwLhW2FD0kIs7TEabXzw3jYQvxD-Hjd1TcIiu_386hKgWUMI7gm1g_C-vbfwIgiaxf8x2WRFzlRlD9AJiEa2TRE-DisJ4h8Tsrl8wO9RMgLfa20s5xXldWsOW1n_5XGYmZRs20_5Qo1aZNDG5fB5DRNcVKr-t9WEwHRkz46oaFC1_CMAsMYDbRwHjb5_RD33JGX_d2ghIVXn4beBvct7TuZsSHhxg5VTofl7dHLeNDL_QWDwk6lLVz6fTmcBmY7-cxhMyX7eQOWStQDU8N2vrvcknR1XNT-AwfmvViCAD6Tt70dOzVY0rmFr_AiozZwRwAHdkFtE3XQXSh_3h0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NQ_g-b6KC5zvjKJl-Co1AOKTzEUjmhQWcQfm4LrSe8vUKlmBg7YMOWupbFCa3HhiYP17Y1r8s_2VfCyEzyaVc5bd804n-WliOXmHRc-P-mEJfrjoKgmoweHxuhnsAViVr1mXHPiXOa2iVP40JZmI7vSW2ZvGMSGYMafle29sNgZVcbTWnvrQY03RW6TqUpNfznTIaSw67nUYT--bhxUS3_bMk-JfU7adtf7WA_qkjMFMfDEEaMPbymuCrhQ1aTA9I7lNTesmgcKyMYwHpHILJzQMK9U7wYf0lihQdNVy6x8JA0eD7a7R9D7e5sDIYRTVKLgcpwi7T5d3mB3zC2XCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PJ-cq0fveWsU94nxNV3T5sF7kpSwU1vHRlGbYQE0HmSnW1xjAK3TbzMLy4fQSQRfq2yRetYRXLF3o_oh3KQuwqYHLQM0-tallDLSo_XauKMX-4Zf8Tl1bcof3Jm1Qb-dnYtHoPrksheYpgnyabweFVGlAN-M0So27hz_A-0yCqh-biWKO6ae3oMZBT8NNAfYDHuAI-5IulqzFGHI7iZios3bmsUN3rPwkNw_v2JCIwkemiTwi4MqEf5yqrTtMYhPj_rlHnznu_QUScaFAt5m3oVav2o4QgYByOV6BPTg3EgI2DGsL6LBT0SqYxBlk0wrrTPw59Z9Ev66hMHwEIM3AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MUfS72oLQT5CIGH4gSxmEMLfB_VNZ7Jh496XzsIEj22PHTSeD5PH8Wh8M2tyQegKuN40eRcaYjn-mdrSTQAvWgRL4Sub5ZCafVqSRxYYegQMCVOyIqV-FR_y3kF1lKNdICxo6jIkhKigXrD-2-I3uKpMlgLcPYKp7eaEHOI0ZYxUOEL7VRoYA3J1Mx_19cXWvQRu409cjHDpt0qoiRwp8EVKVe4GL7Fm3hofm2j1seOT_Emu79mTDSQTD8ztSeg09PQQRSp1nk_Nakg06knmQelXW0UPR1lFbMYe8Ou_i4zfU_t4N7sorshuUr5xMKfHzrkFrBHqWynbbf0OUYEv1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jz_Fkc-ZXlgfDpZZo2qKGcP7bcbteS8jBnbZ2WxtxIR9uejsL8UmKBPxOnZEowXQTAGVlPLwG14w00x14cmCRiRUIOxUI7Oyv4n4DfgstVMz4t-Td6EOWRd1HBN599iStvpmC8SpTPS2EkO3taYuWMUdr62S7qs0qVWUAcmOGmwwxPMykvdlcVJ_IoyMbe9pVA8VTOeTIAADSemOfZ8zt7EKpVbhRavhez6OpUxKSFkCOaRw_xSAUYZYRpFRrizo33kKR6GPD2xFSvU-X2Zxx-qBWBnhUZKUsrEHvIrFXlCFmTaoBEqDbZ76bBK_frmcmj_x0kieSZSiVncqfX5NpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tM9461nMXRAgYX9MdivPOhIbVPNT7OJDyDj-ozbUfrlAqVX3v_8rVw_DqDEtYjNfjQqkDqjo20vQ2lU4GB3fBa89UKiC9eN0dRvPY00Jpw8I2YybGSeVz4GSsr0hxELI3FPJwCryxWoJFevyXYFXKtSHXjhlGD_gChyOourleMqNNSZKSjRlwrXrYXG_qLPvNPvQp_5QoN6-sN7cDjbPwevDQLncJyMzXiurezD4u80ed2c8bwH_X-z-bcg33y64iGL2fsqt3OEmwGZ-vsA4eZDWjOQBM5uCeb4WmFx0okBqq1ukZ-yHmX8Y54GVZhYgTh8MVN8HaxPwFT3ReXuXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eLK3CWNj4lkxYj-UhMhi26OVxwNkL4R3PvU6MvKvbpyt1-d7Ca_j1z9_sL7EePaO2a8hwaqtouaNQVbfOAseTCZQ8iRl00sii--3FKcgqVu2zrrP6wI41fGk6XEVK44kDBDKCJmazsWf_vE39re92A5ocfI-lHX_lM-Lealr-s6eZ7vXiViuQ-W7bXEd2QxGyYNA6x6464l-fjr8CFvXJ5PtYDiPqfgPtfxZsQocpmsHT0AJMR28b4tnnIByGUS7CVtbwp-29BTiar_vtDBNfhn74Bw47NJxY7GzyrhjkiJWPMaY0s7KlM7VUcB-5bIzsZ48QAdRILRh8M8HjfZqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UswFbwdFoy7WkY1VpFE9Csf7qcLXyH0cVT43I9gRN0EC7KJ8sWBl_bY-UebMqEO-Rw7VmWE0_3GD1WIeH4k1WQnBtg-bykyZRlp7-pTKhnYvuDAhzqoVMyHtmdeogaqg2n780aicOIAIkQCbQy4X8J94CL-TEmdHL-PSEe0RQ7l-FjzlcMs-eVt1vtKqo3zYxuBRyEaqXu4x0WDeZRKJhj8S-aMmsh5Q8uwcfpgKzU6-YHAM5Jwh6-TLzWvgRo1787T71TKtKR3QdRskTkM0fLGafcfR3Qq9dAvmnzz4FexumbsQ_0p-n29g6bPibDbp2_i6qVrnP96BPIOoO_AwOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mx4xLZDWRE46gJtlQbZYCS2H_dvKWB0AAAw1DkHTS4lpBuBLuxLaXU6E5Ur96sorZPd0Zx5kjucpbBDdSuRa_nicST7lehMpJ8oohw51qgjMlMq4zc1jBrKk3D_36zPTiRJo7Y86H7Y6X6UTHVhbwtSpizjluno4LHwog5YdDk3H0Iaf2YKTs2Ln87F0lmOBDSp4nmleNOu06UDDquSETKkaP4Xvoh9dkZjX78mS3H9n6XqU77BEoXdSmAd-ldPQ7Njy1Dn53b5iKA03Cgoa5nHsx5nE8V8w6MHNQ7e2YNYtqQdESbI-nrJ_1jeUYTobz2079EKIXuYpos3Lwga_5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiQycdtsuVoxpRg9FYhlX_iWkaK5p8vC1Vb1yOaXaqGGmW7pMtO7H4wRCDmOttVsIEnijeme0UZu0ogqRJlKYFJVdByJjDYhraNj11QsOdDmQj0no3He7hEUF_gM_asU25O3c5__pXPfFNH8UAc0-AqAjdU-2dKklRkbc3eCYq-Slk85m6Eip3lWe4ZczDlyUgT1N9QzD_0Qys1m0GNH6K2Bs5zDVhILpFnBpPuKJmIMX66YhF57E4HAOZPA8-3NOPoJjcthTT9fOQT-7oqrfwat-ASrvZi-KUp14cayp713wv_lDIGeu3NDVecKiGc6ino-_lv7f9xYGrQFATd71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUj1dqWZEjAfk8vnKt6GtV0M3x9CLjy4UnzlcBxILbWHV_tKIBzoGVNtJB59CnuNwS4NFTDEroI0n5ob4r1bgoDFrdS8jtRKZg8XiXYzoretR6TS265sQEapjhjnXnHryMb4pUBSCqtZDMvZu7H2iRVnBHfaUEg_Yi7o7m7JqwzkQqF2G2fBymWqtqk8YBUWBEUZrSwrFSIs3inqtbJUqx4u0JQ4Hk7IcPJekdAeXkXeJQSeHF47T3hyDv2x7IIi3wV1M38eKfAU6VdZutaJ3Nu6I0cJvE3Huo5n_UHYi5u_UCrGqBU0xjs8dOv4gHAGSyo6FDPQ0RgTOEuHhCmYog.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slu9NmH9L0SmdmxDmji6YyO3i3nDtBBxlwJsMpEzU08FzaJUk9cEVCmY34AJtmmDPGIVmLcv9rMRvPCzJmPwTNR1Q4LxTdr0Rhs8Un2Gwna3Pa3APnf0-hYTlBkI77_LkzvuPVpbexTjT9lcH-mEI41xkSwL7IxamezBw4yb0NGHjUEPwM2uLV9LoEmwq_4kXld4q74D9kX9NrPWnhDoT2sDmtfezBnfBh22-Yd0mVs49t4ChsLJqG1D5c8lxmZzVrE__RMF-KmE8kGyz8foZNW3Agluw9JJ0ywcyhU5UAuOWXrETpE3Q9t3zczd-4ANedgLFSGJP8uM2Zi99ifhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KzfiveFfmSkHbXPF_e4dLKPfyogq42BwW0p1u7MjzNVajVawBwbeDhKeuBh3Lh1vrPj1iI3GiCG4Shkn_F2i3Rm9n-5t1IZamap287s-xgDPu7QftOxU8EsyJ-5JzRYNqcMN3oBjf4kSBHOYp3N4W9Yf8kWMLy5oQ2lG7cS2iidLRGQ4kNZkIir4ZD9SCIryeAhPyTj2mW5zPabQmpC0eq3ppEPWZNJW1jMNApxgvNMSHppoVxtMJYEwy0t5jI0PqXt_4SZrbMBKZMUtnAomV1XU306W6irluzt2CZDW9zaYrMWWtRGxYAjqEGVAJwHlp7eekdA5tz4IlGA5ErWWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/L5rNv5NgYnd4i9jVDQ4OHTWEEUNz5K1HOBnjsAaxMsqG6yuUtvLnqXwRdmLqY5VQYTCCDF7dACZuxakO1wRrSaC3-HNC3cgqRD2JvmGJo4hVcSvUhcGR07ql90K9fU4KKiR3MDvqHP9U1tWDRCqLKXZ6I9OmeIG88kAOGlKtoiwPCjxsmpZlI5bSTKgKWKI94OQTixUM6SIe7A8Z1TXDG4_jFvW9J8WnhyI9uTtykeq7s7Q0nyMOvDATco83utfKm5vq-vmipm2smA6H990PObVJVBVXwObhseZRiQHqraBJeKsOYoVioH-jMFSAh7w-O08E_E1AYtpP_D1zAMlZ-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nYdTmQtEzM6tPt6OgcyfVfJInSl7P1o0oOtaxg0YEST28KMvQM2v5EI7NoV9BZhRu6DQLgkRwJhFjIt_UXUfmgrCP5X__FzqezVhN7vV4J3VJ8o2RB_04gnWMzwAGiSI5ZcyHA0MEUlpxg7QNmdUjlcJe9Dyh4N3Xrw2P2Dj5ri01Q1cTvcyqNMM6snlFPml0IVpW2qZx-65M7hmGJMHNcZGjI3Bbz-8FSwvhat9yrJAc9c64q5IU2ywpjNglJK84gTPCUPKtLEAPxlmhjfgOA8NNKpQmA-CrvpsUKpZ0nJ2Ihnq4JgFhdct29nTAy_cAIHFKXG0COK0JfIgaoBFTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HgjjiTgiUwvoR8VxxHtogkT_v1h88oRYeeyIO77ipWyVcaDdmsYEzlfHpr7vC587dQt7f7SHMqXnLO-CypC8t1tfWtj2oAA0Cj_SUb_cs3QVTOxhNOf90U61mhQwM4Kdg32_-uicorgtY26iTnx9B4QkbSHI-9SfouJCleK5KTXciKbvZPhWSH82EqdgqeTRT_TlEPOizgaCFBCRARFA-oMYXYlEX-zsBV7Oi5qlDChy9OO4YZLfKDIOv1OkzKI4mLVjTWtd2Yz3jPgy335x5oW4tvHZD1vRysF9lkBJCsxqvlgi4X9lfrgNDrWCUXsmnFYBdfzjeV6ejVo7BvW65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pMj8tjIxZ9E8SV_S0Vku-i3ZvPEuoIABlWV10bhvHXd9KTIm0REqmZxkClks3N19STKn-SwC8yC3z9uCg1BzA9PzDJ-eAHYGf5Vq7mtdGzbB1E9V0SJuwi7ZL_AgyK9mIZAyAGrvMF1_sXKOVUflQgLwPn3PdmR5zlWuuyfUU1mjcM3f76sOJt_BUn0-b_0fUqyJfK1BbSOdmWgToTU8GP42ffQdfidEKZS7TaMhO893o1Cewbb_C1T7SlksiQPOYVuTXxXXVLLe7CGxKIATammUcmBKN4UlA-IpWZ-a-1Te1mfmFy6NnERYz7KuKlDEa9NTflxeq9weP8jprGvU7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FEFZUNvnYedZUhKAm0BZXionQJG06oQOBN9g4sZf6LGnBR1JDHwV9TBi49t_TbpxxW-WZzbDakm2xdiPf-bE8xqiwh08ubBqSyxtsMGQjeVJuxyAhqPQ42R9j-9kWoirySq3Tjpv-hjqiA8hVqRCHY-4bnCPDrvjDPJQODPPABwxiAa5bIjNBCCN42Uq4dP_iCfphg-1kgN_oSJjP-vzS4Rz1JZpzbu-OYZVEqqQIs7ZRvLFD5p21XcrGFvcGiVp_I9QJIvrLDXoh6hmQMzQZh9s5qgfvP7CmpdvezFtGGfkTXpmTZCfZ_Y7AkQBgwtuhrb5sm_UnvNMm4AjuCKKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X4MS-ZWbW5fxom18Mcq4MFgdLdRDRLx_tJq18GtU8yMgoNON3YhGyjSG1x5ilKiaz9aeHMrmSGPsZ5jQOzashsD1VxsgUxHUfv0s0EJUmuAFTYeZOiP9E8ZkN90XZ6L2_XB9Y8FoedNnJsk_sB9gvuEtOMchUNo_detSRGtYOY-mILwkSGqW3YTe-CeBhJx-XubMvvGirmxlP7R-kI4BQ1Od11Z2PMH8xi8R7GCpgl1wCqx2AWTUZn8yEyBPJodLhpl_uW7pnmsKZx61mi3pWraVCmOvoTS_MLsDYl3ePT6hPE7xOcfAYhhgqcAzVIEmgJo_UsFexGRGhFLU0I2d0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/odhObVzjaoiqlKalxztnjOZC7CYwBqFyAcfe8Q4htcoSfvRLVG_1wgS1hjR7tqjhZI8ja32tWcqBuumtf1czxAhW3hEVyuI0YW3PPLIDbMifnrFdpzLRUzlIAHngs3PNsZgLsmkwIcyO28TIRGJZsLTZUp_MJaFFiOYBwBUDzIKGnGMJ47ERjMA4HBwr1bs282NKEYFRcCJSPqFZOTlkNceQCqgOSSk0-81z8vfcQWxWyNpAmXeNv-EGEgieb4LG5_794wiYvNXxMvbILzBfX3ntHsqLhunNwSUD8V7FFrCxHeXEFmuaZ4jJ3PWOGxVNDhmOWEpe8N-wYeT9gPqMtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XsCIsqtRbsRF7p68Vy3Yreo93Y5178McRY_IsnmjwlvzPKzGjQISLg7fPoanbbRPrq_FITYyYRyfKFcYpHwYnvFmtuKJlyEWxHWwpcOxSRdPsgR5maUNIEaHoEb5xsbHyfX8hvLFgfPuth9k-6-km6SZ5NazaAstLmXn4A_7hE7stzBRNapihDJIe-05Rmdnodb98Z8L1RUnrNca6mChc50_TvETSHQJrAfRvBpfZs9nnHXoiryWGztk87B6E4I1yL-2i5EwJrZUSnPGYCovVnWVq3tCV2OZxp_Pf6wsFI4rOJR7fyEo2PvV7MDqEk7SMc8OdVaDAfbhRUMqeZoi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rR2twHnrwWgCzRWIi-Uv15YA4FjwfGoD7XuwF4yWOVHkeBaCiiaipLrgtjjDpTMU-Gp8TX_S0nA2BW4I6A1Z9LB7MXHC8F8o04GaXl50ZFNnBWTZ5EUy-v77v7J1ZoMFJWAq1VeXIfSuCRWTsXTk1IDONq5fEiF_Lk-Vu4RnBiSKYSUkrurBVM14bb5pDvARM3m4d3J7hhaZF_3WlybTPbdwVecD3oRFulJ_U9MO7vw0G-W66E0h35Ldq4CpkLdfVSh5467gn8Ac09ZFFiYWX3HgiwEMcHDli4-i-AYo0ZrLX5m5ULb7eBzoCYMQU3WrFfJCgkoHW8Q7pl5D1WUOlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C-mD89yFmyofVZADfG0rTaupzOwKFFnTT7Koa0izJzSgEokOXN0HmqzjZlhpm8JeQbm19CJlx0oPyFQipyV08dIdRFdq5q9Z1Bq-jd-5vQYh3kdCnLXTCATK9FbiuYYE8U-tYdXDNVpexpVZX5TZcims0A7SiTk65a2a6TbQzXoFGCvx8CbXVzLENB75HcZ6qbTt0s7F1zP1iuAIB8C-nXAZ8TXaatuBs1b46Fp5S8vyuf4-D2XYmiDEkHRhvNIekym8b4g86YLHbFy3ArSh-7zyq3zM_tLmJ5WzVRybFIrG2D-GnAmb9rvHIcVRyFyYIjL7OCbOLOgnI11vAG4Mgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMVdLF1PZxyWmTYQmDvKxjXVWLyVAUn2QcdOlNX5VCisc9H6Gk_AkXYZhSi0-0KJQgHLow-UPdo5jnsXC5tZrlsSh2bZA3-Ok3odPT76aR7zHZg1IGz_v4QD8kePIOJJypnaXdnC7jmTru8-C0UJ5NlJfMMOORxGcs_6EVXebaG9Qo8U7l-R2DrIsW6PhT-abdpWvFjsnd0FPJetsXZu_5HIS1-QeCV9WmF4ujogc1U21CVMDbgN42J25QVu4ROmHWjjZXv1V8d9HWg7Fba3Fle6vGk_2-tbfjDuWG1HaCSj3vy3nhSvw2THOkztwrxHY3J3YHuYVTf-le9Lb3P8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vdmmmVh1jV3Q82K3Rrg3J3kfbAxU59wdfmyQMH3tYXJjnGVDu3xnEMEU3SeE7mRkAwYI9FfNDUFclUgRsRYRVheFsFjDPu5uSSywVOQwJVodMHaBJldX0v8O7ZUyl9doaZzN4eqie7GLZsrZSci9oRNhKMmOhQywUARPGzowgTJP7byUEshKaOVuE-4LelfZjMt3LCMTZ4PaBSnwDtUaJpk61Fz8PRFGpC4yHpBYEHQSMSNf7SKXlc33Y1U-GFEIemmXsMuQ6KErPffK7enStlpYul1GLk5t3ciHXFMBy7iYlB5MA_gwd6KQumvA1rGu5sgtCQLCOQYZAO1u2sRSDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IiiWXJ2WAG2SvAgoolhH9VkWWzOvQQdWVqh0W6cvDr0g3on6qoIPBz9GP8JcxoIqhW7kbF7ErxLDgPxOT35JUPyaj1a-ZL4CFxIPBa_bpoapHKil5xfBe9zMbgwV8vpr_FCKbZerl58lb2PA40tPgZ1LS1CGApig7MDbPLB72niFRoGBSVePZF80diANxJF15rSgi8zX7-nWRqKDo5xlwLCyUAXc2ACTEsRuSSMCs4uUh7nDOwDBeqpJNTQOKHU2vW1OpSy0W_UaG2eZqybRMhY5EVWHdJQ8duRilgfhw930x01VRMHpOWlvmyO8CEC0JuIsXx7s1eIqF0OJrZfbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jByawM64UT8c3nJeYDl4XYPqf5IRPx9zD-r59lWDd_J2i6rDqG2faUiND2HFhzIvdX39iV8I_tmZNNs2RDENmkJD0oxJkj0NdYK31aEAnAXd4akX2xynPRuO4bTlg0sjHjeR_VjaoD9bMvdyKPwMBZ8XD5gVn3eCxKaTBdy1yXrrEt2veFOr1bSHMSZOk02-48gf_qf9K1QvVsUWpBSRh4glFr5ATk44lagaiTerbrN2CxgwaV_UBC0dmMBzFoMw1jaKqFRy6kqv6Eqd-qU43nnZSYktEA4z-JKp4ZCnhJYxi-UWkTVm3EciKumYJxv43AtpQ2u7T-qt8oOrRzIolw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
