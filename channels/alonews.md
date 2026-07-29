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
<img src="https://cdn4.telesco.pe/file/uY-NJy5aX6_IqawzALUZWRvW8UT_wjYfLj7vF5MtjvImJiXn9QHV1oBolL-j9sGN9TMfeQabH6eUjCUHpfCKA72Avr7eY-V_etHhNwCtn2787CMAzlOo7ltq8Wss_26SnJFXjJJkV_Jk-L1_mD5KOE9jDvWSYxBhtahc15vcW5zwjlIoIQpMdxvog04vRRgQLPuzsk0SKc1tHB-Q-zdjYndrhQR8kBnTwQ_eYlEFF2nE1nywKPpf7wRaWim3sQEYx9cP0Lp0lYYtCHCA__KNi9C2BCV9WzLVJqy70X3RNPKRIw3jk2l8pmQ7XZ8nQkdcNiAlUXDa8ptNF171hM8BDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 05:18:31</div>
<hr>

<div class="tg-post" id="msg-138336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/alonews/138336" target="_blank">📅 03:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138335">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اداره هوانوردی فدرال آمریکا:
شرکت هواپیمایی امریکن ایرلاینز در حال حاضر به دلیل اختلال در سامانه‌های فناوری اطلاعات، فعالیت خود را در سراسر ایالات متحده متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/138335" target="_blank">📅 02:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138334">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs2u003JlPLUZpgQuzGkFNVMmhhQNWQoA6_LsxwVgQkV6TsYK3ZIDhTnmZlhGwD9AWb_IiUy7A_7FIvK3CPk-IFuzfAGnbFalEXDhHg3AHt9J1EJ0HIq7vl-gEGMsTTTSQ2wrC8-jpjg5TZbletT-wRWmJw1TyI7UVUXSLOkhEEg-Smbek-jwITTSXnZNCJv6i4tb7dvDs9dO0Y7EJI81oB-ZOi0CqP0sEUIPWlD-fXajTyKpUwGtQLE831EjQ76gREc01Z2JyXeXGYDNedwPtYlRn35LbsG6-b8MNyhMKl4R3HgCnIV0lFQr9jGw2d87B0zfZMZ3ReiYMY7hL9ckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان آمریکایی پس از حمله موشکی ایران به پایگاه هوایی «موفق السلطي» در اردن، بر فراز خاورمیانه در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/alonews/138334" target="_blank">📅 02:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138333">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
اربیل رو هم زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/138333" target="_blank">📅 02:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138332">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV2QgWy2CZS6DWFZ2KpkylvxTsJ3Hfh6upqlbfs3fs7kZbqWxkLXh-dFs_18b58las5x4bTbP7n9DubvNNbNosL_ijhBc3ZCENsk8L4_Wt0wsoGrpy3fomq2BbZLK-to1jwESw6S6kG3rZfv8PL-D76t2c4enNNtsVqSryot9l8WolZxJRIvfw0KxNKlFClmRjXwmnbXcuo4vCXA8hluxXLO6BZjzKXTXOZGpisXUExLQmMVaBiI00vqCIr8re7ReVt4TDN4QerQdfVNPX7YpnPO-5m-1N-uP1PZLNhUuAL4FE7W-bf4WgVpbRCqo3x4emcdlCl_dyGDbFukhfLZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ساعت ۵:۴۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای سپاه پاسداران انقلاب اسلامی در یک حمله غافلگیرانه به نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از ایران شلیک کردند. همه موشک‌های ایرانی با موفقیت رهگیری شدند. نیروهای آمریکایی هوشیار و در آمادگی بالا هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/138332" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138330">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
منبعی آمریکایی به خبرگزاری i24NEWS گفت که ایران حداقل ۴ موشک بالستیک را به سمت پایگاهی متعلق به ایالات متحده در اردن پرتاب کرد و آن را یک «حمله بزرگ» توصیف نمود.
🔴
پ.ن: اینکه میگن حمله‌ای بزرگ بوده یعنی یه پاسخ قوی میخوان بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138330" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138329">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCNWjU9XCS0INN6WrAh_7AosNqK_BuF2zQzTaueK9hWZGZGELr9CdtQ5mB8Pbp0JyS3VDShD5B3XjRkgKhabJB5x7WD1yx3hE2Ftj_-Behb7cGfkDLbORVRIZDeM1Uf-Vne5Y8QMN16oTi1wD4ZBLGqxASfz7TEW7CcYcjnN0u1FRu1XJCeUDGPjgiC6JbHTkioefJrxx2Eq4OjIUmIZwcFIbhw6tkgOYa1y7UcZo7vwa70DTD3K-MX_-OpFLWiPQBLnstosgMjGeF-gz5wcnVXjwTbzkqJxIfcAAdT-Cm1F7pM50bt9s0a24UvHZ0wPFlGkaFJu8Ur1PMyNJUqzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا هیچی اصابت نکرده، فقط الکی الکی آتش بس نقض کردن و آمریکا بزودی بازهم جنوب رو میزنه با تفاوت اینکه اون هرچی میزنه میشینه و اساسیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/138329" target="_blank">📅 01:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138328">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
مقامات آمریکایی: موشک ها رهگیری و منهدم شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/138328" target="_blank">📅 01:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138327">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMYnVMyRl8f7xrqionILSxViIgky5BO9RGD5kAWi26hCMu85G1o1vU5A7zn6ce00mky9eWiOyUC8ErYoBwuVYJVhxJ1GvnZSgR_MKm_SG0WS7pL6w6ASMtLlHUxtgxI4IlqMq8lWObs-ZxjkxnSauUcxF28T_O6o42sxRj9BPCWuK9qztG9sHis4CyQPQrFqFEJ2wln7C0gnSKGhehP_wjUtVg_QZU8sD_w0W0ABIs2jdRaN8DU4AMqVMI5fdztH1eADRc0RrN-S6FGzs97ArQLTq3JUXZ-thWhAp-ZHGcT1FHS6LTQaLAA9VCQAeuuSYLgkcjj_O4fkoAI2eCFlaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید، خبرنگار آکسیوس: ایران موشک به سمت پایگاهی تو اردن شلیک کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/138327" target="_blank">📅 01:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138326">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOm_2l7Bo8pmwNUhc2k5MUU5RLmT2D_tiVh-6OMIPCaWp1ekc6SF1A_Ma_MNdixM92QijiBlAJxZGHQK5GoE2BMpxCLumyerAPZD56UkuyUb8Q9LIcmpSt4M_gNf13iJceVC1qXYLFefoJ0pZy2GhrREvfxw9QKf-KhM-OFhEgmQ0hQvZw2-dfXcG2J0SNuO5RX7kwSP6MJrrmlR-HHDByCfoNWvdrmvmHBSfgB63eV93w-4rcxHh2PrMaH-E542Pqbinv_YkwjkpvXfldp7lu9sSuaLF3brW0EAbMhuiA7WV9vyS39TsGRanUTidejL0fbF80zGuo9Ljuj3oxlrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی :
ایران برای جنگ تمام عیار کامل آمادستِ
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/138326" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138325">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxuRbw41ciRTtRH7D_lvDFzjIZge5jeimWIx-tMKjfF09sJflePmZoj0AWqdoduZPtf46GeXyjJz37Lq0mOrj-KM6LWpj7OPrY5-88niF3yxKtuRSqQa6YaERx0ESen5XI2xHgwkC70OMCEEF0rfNcyKEFLaEsPXxN4Nj5qUCcZP-6smSP6wAF_wtNwN6pmjg4LHMoOpqZTBD31EIs_yFY8cIGlNa21shggRPEQTLGjM59r07SnAPB2R4CZm-Pk_jM_z1llyLmTczFHyiuBkU8S-OAECxpV-RCUN7pG6ZcmLKlRlsGDYhN66Q1vGabhjTq9fm-gKscmDWqELdhYzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت آسمان منطقه هم‌اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/138325" target="_blank">📅 01:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138324">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
تصویری از ماهرخ عشق ابدی تو خونه تتلو که....... خیلیا نمیدونستن اونه اما خودشه
😂
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/138324" target="_blank">📅 01:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138323">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوووووری/شلیک مجدد موشک از غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/138323" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138322">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ الان میاد میگه ایرانی‌ها زنگ زدن و گفتن لطفا آقای رئیس جمهور بیایید مذاکره کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/138322" target="_blank">📅 01:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فووووری/انفجار مهیب در آسمان پایگاه موفق السلطی در پایتخت اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/138320" target="_blank">📅 01:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
✅
‏ ️فوری/ پرواز جنگنده‌های آمریکایی به سوی ایران
✅
@khat_akhbar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/138319" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7b89adab.mp4?token=cvsd5wgE6toWvcWoy1jC4pHqzjsUqOD1XFi_Nas7OxLcHsArU5g1A5A285ngNa2z3Qfpg1an7M7VbmUaByxmHmxiS7_jIi2v5TdHm6sUwE2d0b-ypJ9DFXYOrL817XCnAIfX6ApuVtuNAR9kVpvPOJ8B6dWWLpx0W54HXMeDcLrzI6XlW2159jXl65BDU_w_9i_6rNljL7K6PM9WSRI6J1AK9AKtu1cIVo_4tuuKcZeW75N0MZc1MzY-H-aktDHHyRTuJqR--82x4pMwJOXrymy1BZ5qJQbRSQ9uawRqYwNFtifJYI2K5xFrjh1-PmaeJaL1ej2PiAVhZp0BrAs1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7b89adab.mp4?token=cvsd5wgE6toWvcWoy1jC4pHqzjsUqOD1XFi_Nas7OxLcHsArU5g1A5A285ngNa2z3Qfpg1an7M7VbmUaByxmHmxiS7_jIi2v5TdHm6sUwE2d0b-ypJ9DFXYOrL817XCnAIfX6ApuVtuNAR9kVpvPOJ8B6dWWLpx0W54HXMeDcLrzI6XlW2159jXl65BDU_w_9i_6rNljL7K6PM9WSRI6J1AK9AKtu1cIVo_4tuuKcZeW75N0MZc1MzY-H-aktDHHyRTuJqR--82x4pMwJOXrymy1BZ5qJQbRSQ9uawRqYwNFtifJYI2K5xFrjh1-PmaeJaL1ej2PiAVhZp0BrAs1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اولین تصاویر از آسمان اردن هم اکنون
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/138318" target="_blank">📅 01:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سپاه بازهم آتش بس را نقض کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/138317" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=hytiGO-Orn5eVMsxhdVBvT6BS2cFKVN6bcJtF1teWF972ZInpIavg_SvCqlBgAOi9Ko_GpqG1ci-Uq7YojdLqKUq1odFg_C5g-xMZFBT0iNQRDvBQEz3Ku7Yo_2-quR0clJio8ExvB0cvFTaQ6gw9mwcQh9PmKxuH2VI5NHpZoBU_-qcONh_OrGo0szJbVncj2cj4sByd0o_LipMZ1akTcek6WjXwKTMBR4PDAg24I7-dfje-eI-HG2GXsBfhMWM_ahDAmNxctWHQBpVl66gz0bo0rMRNCSjMQXsMSlZhux8mw5ijAWiBuJ0m52cULCdbILI666qLJPimdVueo59Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=hytiGO-Orn5eVMsxhdVBvT6BS2cFKVN6bcJtF1teWF972ZInpIavg_SvCqlBgAOi9Ko_GpqG1ci-Uq7YojdLqKUq1odFg_C5g-xMZFBT0iNQRDvBQEz3Ku7Yo_2-quR0clJio8ExvB0cvFTaQ6gw9mwcQh9PmKxuH2VI5NHpZoBU_-qcONh_OrGo0szJbVncj2cj4sByd0o_LipMZ1akTcek6WjXwKTMBR4PDAg24I7-dfje-eI-HG2GXsBfhMWM_ahDAmNxctWHQBpVl66gz0bo0rMRNCSjMQXsMSlZhux8mw5ijAWiBuJ0m52cULCdbILI666qLJPimdVueo59Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
موشک‌ها به اردن رسیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/138316" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138314">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLfrZccynpS33fDwWTgS0Ua5t_2DGFSaOPKPVqnmMfUIxx4nYZJEoEBD3I79FQBsr0lClJdbxiJ-Me4icVQjBQWUEIqFd37BettR2ICeNOGs3uqk23j6QRBT9B3qdYsQg9EN-V07tJT2cMdLeM0Dalx-IHgDXB3TBBz3rdU24gWHMVYl2N5P0zNr2tP3HpTyqpnj-Za9CsZiSnnDoeo8cy0MwHK_xnYoedXrbcYvWLEIHQg5JEqnNiRSZYv6cX83Z5F-b8qcvYKC-OAbTLjfqNAPN5AkWLq1BKRPXyr4KjnZnlkaShR8VvIIa_fsZHCYQDnetiLAAic2I6YpnIhydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/شلیک موشک‌ها از خرم آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/138314" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138313">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گزارش شلیک موشک از زنجان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/138313" target="_blank">📅 01:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138312">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری/6 موشک تا کنون شلیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/alonews/138312" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138311">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/سپاه اردن رو زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/138311" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138310">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8StNUXgF7js0eXANr5xnALUp-tFwTRclEcp2EF-qeZWIC-Q3ocyWBlb1l_GHI-SsYPRCBDi9-xM59ynStHVIDRvv1yjHyIdVVO0oZaIwOC2QavWqREd6DB_nuyDjHKIkMQHVg_d9tuIjw3U8PIbymM_MJ7ro0_1I8KnZee_Bjo_fIhX0vNmfqTZga8aFN_JytUx27ocXZtRORz5jizVTsZeq84QWhBTpUvXj8ZbIbaqGjwo8XvZirwUaOGBwGYKRE1q1LpffqGzAXLQQv57XZCJVhWnKaFQIxBdjdaaQK2v3uJtJ4IdORFJ9nUYQvy5S6l-dvYR2XRPUF9XU1jxLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/دقایقی قبل از خمین ۳ موشک شلیک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/138310" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138309">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری/شلیک موشک از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/138309" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138308">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf75b734fc.mp4?token=BwFI3kSErsJsA9B_oA1DJ5TSRMB3PI1iNk6gwW47zCgrmRrTh8KmoYrG2UsWt9ekoF8-5Tp2Z1YaDrKvMSa6uenha5UXjOBlJaCkPsDIrskWOsCMU-qA4nLALheONyY_hPIytl1Gyb1q26XYfB1rafPL-NrDPvfJPqWtLj_W3RvVlq11T1u3wMMNOt_9Q1TzWmLQAy0YRl1JULt9zYcm5Jdueou5AE3zU1LHAA3sj3dL-4pFzWiPyS4Eqjk7vRz0v9Bc3wORh64IC-5pOIRz7Nm7S1-TAHsrV9K577eBGLfZXGgigyuYc4CvsH_stTxyfi-UXpPbADQGdVsr1j-FmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf75b734fc.mp4?token=BwFI3kSErsJsA9B_oA1DJ5TSRMB3PI1iNk6gwW47zCgrmRrTh8KmoYrG2UsWt9ekoF8-5Tp2Z1YaDrKvMSa6uenha5UXjOBlJaCkPsDIrskWOsCMU-qA4nLALheONyY_hPIytl1Gyb1q26XYfB1rafPL-NrDPvfJPqWtLj_W3RvVlq11T1u3wMMNOt_9Q1TzWmLQAy0YRl1JULt9zYcm5Jdueou5AE3zU1LHAA3sj3dL-4pFzWiPyS4Eqjk7vRz0v9Bc3wORh64IC-5pOIRz7Nm7S1-TAHsrV9K577eBGLfZXGgigyuYc4CvsH_stTxyfi-UXpPbADQGdVsr1j-FmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مجری: عموی عزیزم‌ محسنی اژه‌ای بابت اعدام‌ها دمت گرم
🔴
پ.ن: جواب با شما
#عموی_سوباسا
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/138308" target="_blank">📅 01:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138307">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082980e3dc.mp4?token=TBDHw9KgN6pBxPQwAubuzimNtY86NbmHN9GKyjl74QnduaEPcqlLPdBbteVTgvB8dJO3TWjt6mEV0VFX5cA3UVLizWWGDkO7eMvKpcNmdya-WZJzim6jdUdNWcCdy_HVZ48ulL_AyRnOXkM-Xv59lJsIIgswIcwyl9cV8qc7lWZoPgWoOMcgl3gSuHnJK0VCVM6lY46n6qP4RwhES20TgZknKOlozI4hkqmrN8vF5RIql3V9yRAVWie6LTZIqPEHvbBa3RSRANM5vOxs7b0Big9LVONVyao1Oq6JEC595t51spI11YFrSZ6-bFF_oGPhIn-7lwiAe1KraRDT-gdETTolSqic6DanqseNOZLvM1Wy6ZI0m6vnGejMOFoHKaRKQCH8QfmCOuSglMkIDIIgYNedB5kLypQpgLSIn3xHESFqE5xBzsJDFMng2PDIs1b5dl0u29zsxqzAQjX01naQEPTtfPF1m3uXZmpO21Qo1W9jo9IHvKWMSSIba8bq6jfC_b-dhdi4rOQkrqCT98LSmBHc1ef-_rJ4pdwYCLVo7OXIDA_zmQK7cEIxCxnnoQH_PVw42S3nhk-1ElXjieLIwbRENEah63SRBMsyMv-XNWXfwu_vpI7cNE7OKRg6hxvI5pFT41QUg7ZSxb5nje680BTCdPOgtOEpf40Fp36hyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082980e3dc.mp4?token=TBDHw9KgN6pBxPQwAubuzimNtY86NbmHN9GKyjl74QnduaEPcqlLPdBbteVTgvB8dJO3TWjt6mEV0VFX5cA3UVLizWWGDkO7eMvKpcNmdya-WZJzim6jdUdNWcCdy_HVZ48ulL_AyRnOXkM-Xv59lJsIIgswIcwyl9cV8qc7lWZoPgWoOMcgl3gSuHnJK0VCVM6lY46n6qP4RwhES20TgZknKOlozI4hkqmrN8vF5RIql3V9yRAVWie6LTZIqPEHvbBa3RSRANM5vOxs7b0Big9LVONVyao1Oq6JEC595t51spI11YFrSZ6-bFF_oGPhIn-7lwiAe1KraRDT-gdETTolSqic6DanqseNOZLvM1Wy6ZI0m6vnGejMOFoHKaRKQCH8QfmCOuSglMkIDIIgYNedB5kLypQpgLSIn3xHESFqE5xBzsJDFMng2PDIs1b5dl0u29zsxqzAQjX01naQEPTtfPF1m3uXZmpO21Qo1W9jo9IHvKWMSSIba8bq6jfC_b-dhdi4rOQkrqCT98LSmBHc1ef-_rJ4pdwYCLVo7OXIDA_zmQK7cEIxCxnnoQH_PVw42S3nhk-1ElXjieLIwbRENEah63SRBMsyMv-XNWXfwu_vpI7cNE7OKRg6hxvI5pFT41QUg7ZSxb5nje680BTCdPOgtOEpf40Fp36hyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعال رسانه‌ای نزدیک به اپوزیسیون: طبق اطلاعات محرمانه‌ای که به ما رسیده در دی ماه 378 هزار جاویدنام داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/138307" target="_blank">📅 01:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138305">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tk989u_w5Uz6WOnRBC40nMUv4Wz3OumBBmevjjkGN03ZC2mGjqn6gMwP-wXxTNT5NPbdgKfm8brSpdyv-SbYQTf6GvMlShZyoComsgpVGN7W4B6eTuQ1FKgXvNEEt9tbta6ip58c1anccMLmzXmM8mNZsmXJw_oMiyYjxQY729pzBF2HKETB1vkeiiuI7vB-xcsE07iM5z-tM52y9oLPiQ-yZyOOHSSTcnwp6iHfqeKTAmcpcV2PA4CSKOGIHOnReXGvPQscxckhvBWbOoyvNRCPGjya-iWOiVf_RtT6hpzEF7FyCcJ9dOGOFs327hv2nlHRGdyS5SD4t08rH4eYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ما میخواهیم زیرساخت‌های انرژی ایران را هدف قرار دهیم اما آمریکا ممانعت میکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/138305" target="_blank">📅 00:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138304">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خب بریم یه افشاگری خفن از ماهرخ عشق ابدی</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138304" target="_blank">📅 00:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138303">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
واکنش ماهرخ عشق ابدی به اعدام‌ با خنده:  «اگه میتونی برو جلوشونو بگیر، تورم بکنن جزو اونا، بشی چهارمی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/138303" target="_blank">📅 00:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138302">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vflMcb9ylxZ36mMpwr9fjUgBZ6zYSbynOrdzTBdLcSXr2vGoxaqtnAxHYBdUsaBqZMVO2NdjDs30xqAUxpdZe8Tyfj5BGIy7ZZesvYmw7o-TdEXDWPbvA3GZPkaeA14ilionVcMZCoPnwA1NxvoC3h8kIPDFBpI9PakIvuIiT-eyzj3GGwepJB6ECPRNBntgFLTRFzmYqFny72zFWUjLqJfUUKferLJn8q-4J_I0mjksq_-mR0ANgDytoS9iCsjZW-gJJ020yM-WRVVqmG30jdIvyPbnuigARVvQmIgWhEvXu90s6NHoyZ_Q237NR6peZIIdRReU0bHqghJZ_HGQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخوندا هم به درآمد دلاری رسیدن.
🔴
دولت اومده یه اپلیکیشنی طراحی کرده تا ایرانی هایی که خارج از کشورن و نمیتونن برن سر مزار عزیزانشون یک نماینده بفرستن تا قبر رو بشوره؛ شمع روشن کنه؛ قرآن براش بخونه و ....
قیمتشم از ۱۴ دلار شروع میشه تا ۱۲۴ دلار و هرچقدر کارای بیشتری کنه پول بیشتری میگیره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/138302" target="_blank">📅 00:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کانال i24 عبری:تنها چیزی که ترامپ را به سمت امضای توافق با ایران سوق داد، قیمت نفت بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/138301" target="_blank">📅 00:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با برادر خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
🔴
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/138300" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138299">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvHR4Sk0NpiOKp9Ouz2S-vWLzWEH70Jota4gF-p3TqA2w5OdWO4PshlqiGWTP_z3O_t9_WBRPoPQz4_65ycrsO3-eXvaZ6PttZxpjJ6TDAeBui93RxTLxMTqPmOA_SgUWFGi-QFjgc4zTRWft_CddPmhEsb-R6ABmUv07tCya6Dp3Wykn9y6R5_LWs1Db1BzWQdpYuk0ZqI18X5zWcPK8GfWxgkx6B6RHp3SfgCqFknT7A9Yw1tAQogCwGMCjhj1xssZKroXvAKhv9n82L3XXEH5ujkO2TPEvhbnYmIcLbJUbRM0z1EBt_LBUvRdVNy4EBXYLCF4urS6pgIP4Tmxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گفته‌ی محمدی، رئیس اتحادیه رستورانداران مشهد؛ از ابتدای سال تا الان ۳۰۰ رستوران تو مشهد تعطیل شدن.
حالا دلیلش چی بود؟
بخاطر تورم؛ گرونی؛ کاهش مشتری؛ مالیات سنگین و... که باعث شده بیش از ۲ هزار نفر هم بیکار بشن.
الان هم رستوران هایی که دارن کار میکنن اکثر دچار رکود هستن و مشتری ندارن و اگه وضعیت با همین فرمون پیش بره اونام تعطیل میشن.
تازه این مشهده؛ با وجود کلی زائر در سال که باید اوضاعشون بهتر باشه اینجوریه، وای به حال شهرهای دیگه...
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138299" target="_blank">📅 00:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBa8kSM7eJlezcpv8hbdkYteY09vi0WLSWuxOK_GgHi0M1ZZwvmADBsWZmC56uh3_NKkwo4IU2LL3hH6ARe-zp8ziGAlvxbdw5jbtjNQnGWW3riu-13KQlvOJKIrUkV61ORiO6P3I4G2UqHrxeYsKCRuyXj-FN-b9nT-Ej8WpSg-JwozX9BWIQnZJD-BkKkaMuRIhSk4vHY-jx90rQV629lrrqXcjLV7GojVVd8JEc0d8c40BVVTmcBkzzxaY-mYKLlGW6eZDKyFOGWUE93OVTvJ8m_-r4uJ6s5cmYpGpSUA3YqbDOMNdlVu3Erw7f9DMFA9LIN8pGTkqkdN3pnR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به نقل از رویترز، یک مقام آمریکایی گفت:ایالات متحده معتقد است که ایران در مطالبات خود در مورد تنگه هرمز اغراق می‌کند، به ویژه در اشاره به درخواست آن برای کنترل بیشتر بر تردد در این تنگه در جریان مذاکرات با عمان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/138298" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138297">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
عرزشی های حرام زاده میگن رضا پهلوی با فراخوان 18،19 دی باعث کشته شدن هم وطن هامون توسط حکومت جمهوری اسلامی شدن.
🤔
خوب پس طبق روایات خودتون میشه گفت حسین هم باعث کشته شدن مردم تو کربلا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/138297" target="_blank">📅 00:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138296">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مقام آمریکایی به رویترز: توافقی در مورد تنگه هرمز که بحث درباره آن جریان دارد به هماهنگی مربوط می‌شود و هیچ‌گونه اخذ تعرفه را شامل نمی‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/138296" target="_blank">📅 00:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال 13 اسرائیلی:مسئولان ارشد اسرائیلی اعلام کردند که "اسرائیل" شاهد یک عملیات بازسازی گسترده‌ای است که توسط ایران انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/138295" target="_blank">📅 00:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
در حال حاضر هواپیماهای ترابری نظامی فوق سنگین آمریکایی به صورت پی در پی از اروپا به سمت عربستان سعودی و اردن در حال حرکت می‌باشند،
یک پل هوایی نظامی تمام عیار از اروپا به سمت خاورمیانه در جریان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138294" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
رویترز: در حالی که ترامپ مدام از مذاکره با ایران حرف میزنه، طی چند روز اخیر گسترده‌ترین تحرکات نظامی و لجستیکی آمریکا تو منطقه گزارش شده.
به گفته برخی منابع نظامی، آمریکا در حال آماده‌سازی خودش برای یک جنگ تمام‌عیاره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/138293" target="_blank">📅 00:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
اولین تصاویر از بمباران آسایشگاه سربازان بمپور
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138292" target="_blank">📅 00:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138291">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس: وزیر خارجه(عراقچی) به جای اخراج کاردار سفارت اوکراین، به تلفن وزیر امور خارجه اوکراین پاسخ داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/138291" target="_blank">📅 00:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5MmvRgQcnncyW1rL2FZ9T7hKw_jAaX1vwI9-ZttrPsUFglVeok_o2dWamtfbMAwJmoqHK4lz6Ww3bFF0BQbQtrUlqw1H7Bq6Gk32JFWpLwzaq92rVrtsrM4uBgmlJY_TYPZ-E9lY8d5o07SCj7Wx91MhuKuvnTTM8_JYsvUusopWYK5msfSdXryJBulbWpTGi_q2JJ4LV9r-iSt9Q1Pl_bWCrUA2Sq_9-tAEkfL7uvek2g55UU0nACLdVGurBzML9SkBZMbLmvanpDCpuT3WdsQM6FBcgTENd06lIdWMApz7IuJ9YCMnWw0R84lheT06WSD287Wxu9jNRQji0grmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: اعدام هم جزئی از قانونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138290" target="_blank">📅 00:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVd_uzNTodClr6BkG7laXX8XBGgmZWmtdiqAaUL8GSgowZGd8YfK_bFFsnNN5qqvw2E3_Wb_AUc1PcdsrMBb-eaUl1NSozlC4d39Ve9EAuY2UdAmZN0dJ62M9kHg5zQCmymxsS4oBaCReDMXw10jtAH-HDJC7YGVBlji4b8o_u0dmYML0iJJkMWDs7knRbUQw3MRi8TWd6_C9C-kAbTvZYSrmWOxI2Czc7F7J2EGtkt2Xizsw-klJySmgtmu9S2yfJYy4fbGKXAlF2LsWW6iWI96f8xFzHkXGvRAOXRBqZOUQ9c8XCzGzbdXNzXiK2R5f332lQIptX8JIkuDlVq74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس:
نصف مردم آمریکا می‌خوان نتانیاهو رو حالا که تو کشورشونه، بازداشتش کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/138289" target="_blank">📅 00:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJE1sVRxgNmab_qXI_Fkx5F4OyXhoMtqhKjMyO_QWJu9n6M6AJl_538cQ5ZhI_SEhRlAqy4IMF4B-I9upw7CdHlg3nYC4HGh_CXi8vzVe8xSFSYFZPSZthkFTvZSGz8IKOTbLNLlp7Ifu7Dn76gliOfDBq4jK2w3fOLrE6hVBvqbkivjmgsEwjjjkiJZgvaLOUfjuo3B1xjySCl5KANvETrIoLUas0SJPb4GP9PqwVC93Ipcdftc992lGRjNsOOD2IlsaJIrIUwNaMSPkQKwz78bjv80i1qt3lXh21RGo0kCxB2AHUtFOC8r9I9dxa8RvXlW0uNBzwGx8SkWiojcDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏شریفی زارچی، استاد سابق دانشگاه شریف:
🔴
‏به محض آن‌که آتش جنگ اندکی فروکش می‌کند، چوبه‌های اعدام علم می‌شود.
‏جمهوری اسلامی باید سرنگون شود تا ملت ایران رنگ آرامش ببیند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/138288" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
عرزشی های حرام زاده میگن رضا پهلوی با فراخوان 18،19 دی باعث کشته شدن هم وطن هامون توسط حکومت جمهوری اسلامی شدن.
🤔
خوب پس طبق روایات خودتون میشه گفت حسین هم باعث کشته شدن مردم تو کربلا شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/138287" target="_blank">📅 00:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
واکنش ماهرخ عشق ابدی به اعدام‌ با خنده:  «اگه میتونی برو جلوشونو بگیر، تورم بکنن جزو اونا، بشی چهارمی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138286" target="_blank">📅 00:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138285">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2c14506f.mp4?token=nRSeD69ukQWjPzXeP1p8tioY3soe7w4Z2RQWbVLi8ItWaenE-VeZLSBLI8MLFnJs8TzO1Pq1w0Ru-idrF8MSA2pV-6ZjST7zjCkcrmE6fbIiCgtCUxx0goZwhpkMrjyBrMGlCX6oaqkIrN8Ub1Je7s5UiJIaflTGPA_vT1MKVQzL5UP1ocsM6212MBankOmgfVRFqCn608ADP09_50DlqqfM6IY2jDptJrSv_9LeiYb1FpFmAYOwum80B3huRmuOQ9vLH9CCJtpmSN_uB5hgKgh_pZ-gg4xHtLekXaF4iDszpqXPu_Mt1ccZ6Z06s_WpzKZO3oNdj-PG26ZX55rW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2c14506f.mp4?token=nRSeD69ukQWjPzXeP1p8tioY3soe7w4Z2RQWbVLi8ItWaenE-VeZLSBLI8MLFnJs8TzO1Pq1w0Ru-idrF8MSA2pV-6ZjST7zjCkcrmE6fbIiCgtCUxx0goZwhpkMrjyBrMGlCX6oaqkIrN8Ub1Je7s5UiJIaflTGPA_vT1MKVQzL5UP1ocsM6212MBankOmgfVRFqCn608ADP09_50DlqqfM6IY2jDptJrSv_9LeiYb1FpFmAYOwum80B3huRmuOQ9vLH9CCJtpmSN_uB5hgKgh_pZ-gg4xHtLekXaF4iDszpqXPu_Mt1ccZ6Z06s_WpzKZO3oNdj-PG26ZX55rW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش ماهرخ عشق ابدی به اعدام‌ با خنده:
«اگه میتونی برو جلوشونو بگیر، تورم بکنن جزو اونا، بشی چهارمی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/138285" target="_blank">📅 00:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138284">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXNDKzDTYm47FALR0ut4Qd_-FeBEH48NG-9yRRl4n0dhx0-50OUYJnu97ex78e41o6L_22B4iHVW0136-dnR3xYyK1BawsD5ax6EZ22spZ0bZJ1ubUO3mJlVbzQL706yZpewHch0yEuDvNEKMVX_XTe3eb0CyaJFY6NA9OOB_sQlPVuJLnRKfJJPKoP8vj8J0bN8tuABlrkyY15zjPpLkINtskOH3iaYf22jAqp8vtSrAEDGXbYC7WfDOYSGMzKtO52bLvB7jPUZTo-RVGjDO7gSpxWpDCId_Z5eUFkXlWocRg7RPkXiy36VQIF4Qq320LMd90G2_E2EsSXilqEtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
حضور رضا پهلوی در مراسم لیندسی گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/138284" target="_blank">📅 23:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138283">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bee079a9da.mp4?token=QK4RpoPNXVOhaIH5WOEdkOz-0t8v4X_OdKGkPDFvDXnV0dar6pgIhUc-VmR8wnVvBAVPR8CFQyT5gZN2vJsIYFTnVCCphZ57igo9SHGC1DFIy_wToRO73sMDTevBXra169phca7YOE1-XGlYDtdgE6wVgHyyJubdf7U6so8tRIUar6UeC9lQ5PotezZfdAlojhbasTZeKEzGqnbi2NdvFWWuRsK3qBK7opKqbVdqlVAUobiCtUe00ZdZ3cWQgNb-AaFitb9msgmMiZixDOBQe6lc60J3PJSesvoEr0XLRe-nPBnWjsLzu15I0qzgX9D-HkJp-qO7GV53VkcdPkVnYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bee079a9da.mp4?token=QK4RpoPNXVOhaIH5WOEdkOz-0t8v4X_OdKGkPDFvDXnV0dar6pgIhUc-VmR8wnVvBAVPR8CFQyT5gZN2vJsIYFTnVCCphZ57igo9SHGC1DFIy_wToRO73sMDTevBXra169phca7YOE1-XGlYDtdgE6wVgHyyJubdf7U6so8tRIUar6UeC9lQ5PotezZfdAlojhbasTZeKEzGqnbi2NdvFWWuRsK3qBK7opKqbVdqlVAUobiCtUe00ZdZ3cWQgNb-AaFitb9msgmMiZixDOBQe6lc60J3PJSesvoEr0XLRe-nPBnWjsLzu15I0qzgX9D-HkJp-qO7GV53VkcdPkVnYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بمباران مداوم مناطق نابتيه الفوقا در جنوب لبنان توسط توپخانه اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/138283" target="_blank">📅 23:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138282">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/919fe2f821.mp4?token=kFVgpqGxOziFmmNtPK46edRAQ-npOqxx6ZZztWQfbwhX8lQqbKuMThr4HtlQjr4hLuY8pggXyff1qZ01QbsFBgOmc5H9TRc5fDe5n4peyNZ3JpnDUCDpFkpmFbwLWVk44A3Sp1mD-ckeuqp0NZhL64Ffy9elvwDhhtZc3Yk09pE1JYaCSEO37lu_N7IEy4Y7gE_6JsaEnhLXYadSk9fg86U1xqSitVuYD146KyWFHOrm9P3Ml13MNNXT8iHqBy_JRPsYKzZDHfZ6c9v6a93BFbHcGFJPFwBLZ0tuOCD0p7bN-nEhh8HuvBnIkQVqwle8Vu5vX_4Qpt8PbbQQFCv60A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/919fe2f821.mp4?token=kFVgpqGxOziFmmNtPK46edRAQ-npOqxx6ZZztWQfbwhX8lQqbKuMThr4HtlQjr4hLuY8pggXyff1qZ01QbsFBgOmc5H9TRc5fDe5n4peyNZ3JpnDUCDpFkpmFbwLWVk44A3Sp1mD-ckeuqp0NZhL64Ffy9elvwDhhtZc3Yk09pE1JYaCSEO37lu_N7IEy4Y7gE_6JsaEnhLXYadSk9fg86U1xqSitVuYD146KyWFHOrm9P3Ml13MNNXT8iHqBy_JRPsYKzZDHfZ6c9v6a93BFbHcGFJPFwBLZ0tuOCD0p7bN-nEhh8HuvBnIkQVqwle8Vu5vX_4Qpt8PbbQQFCv60A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ تعدادی قرص "تیک تاک" (Tic Tacs) از جیب خود بیرون آورد و تعدادی از آن‌ها را به معاون رئیس جمهور، جِی. دی. ونس، در مراسم خاکسپاری سناتور لیندسی گراهام پیشنهاد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/138282" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138281">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیران امور خارجه اردن و پاکستان بر لزوم موفقیت آمیز بودن تلاش‌ها برای تضمین پایبندی به توافق آتش بس میان ایران و آمریکا تاکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/138281" target="_blank">📅 23:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138280">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgjVuPWpOToppH7NqUl9aq2UAFOSRQZbaB5bsGc5jqrEnFaq-pEeqezLo6c8thStw0_elgRL5k3cRJjhFySJxiISIlcYapH1c7A7T2Jlo8JEC7F4MD0hnHpkefk3B9m1T0ouD45cT9fyb36vjleQK25AirMJpycQpHJHp8La0zECcnl8K_VV-7k9GbUfHQfP7m5OHbL4QoO0oGlgwKw80spB42WjqWLfnmxUMvv4WGT3Kxa86JYkomX1N3hGqV0kDBVLmXURuytWC_6d5kiOlI6TOQbQbi46wV_xn5UcBtm4J5GIycgGEV5hhKPf1xue3cPINQvqo0SnAfVSNdvTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت 83 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/138280" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138279">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/692d5412da.mp4?token=m7Hl7G_te0EAelvqFnFiKkasApPtSSXvQLC1K6fCj16Whx2JIBgBEblMmH7LVHtyQGEXtsIR6ol-8cwIt0w3YoZUCTOrtWBRoTnFPSh4wHwMVL5HCJ0UnHDAgA2wMRh2H_HiTmQgELKVu9mYTBLjhyD4sH6RthUbqRWjJ3MuF9yWAnJQbybHrU1V6HG-PXujBmsYBc5a1wRvqRYKFet3YhBtKtWbjN1-HSTJF_SJUVWxA9tS0ljK-_rR3l7OrO19THZuULgD3uuOlfVvAGNAD6l97ujG02D0nqKgZVc1RqmA131NXCeY9HNN959_TCBGv-GAWdbyTnwUHjyuc_Yvew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/692d5412da.mp4?token=m7Hl7G_te0EAelvqFnFiKkasApPtSSXvQLC1K6fCj16Whx2JIBgBEblMmH7LVHtyQGEXtsIR6ol-8cwIt0w3YoZUCTOrtWBRoTnFPSh4wHwMVL5HCJ0UnHDAgA2wMRh2H_HiTmQgELKVu9mYTBLjhyD4sH6RthUbqRWjJ3MuF9yWAnJQbybHrU1V6HG-PXujBmsYBc5a1wRvqRYKFet3YhBtKtWbjN1-HSTJF_SJUVWxA9tS0ljK-_rR3l7OrO19THZuULgD3uuOlfVvAGNAD6l97ujG02D0nqKgZVc1RqmA131NXCeY9HNN959_TCBGv-GAWdbyTnwUHjyuc_Yvew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نرخ جدید دیه : (دعوا هم دیگه نمیصرفه)
🔴
دیه‌ شکستن کامل بینی : 2 میلیارد و 100 میلیون تومن
🔴
شکستن فک بالا : 160 میلیون تومن
🔴
شکستن فک پایین : 640 میلیون تومن
🔴
شکستن هر دندون : 105 میلیون تومن
🔴
شکستن دست : 160 تا 210 میلیون تومن
🔴
شکستن سر : 120 میلیون تومن
🔴
شکستن پا : 210 میلیون تومن
🔴
شکستن گوش : 350 میلیون تومن
🔴
کبودی صورت : 6 میلیون تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/138279" target="_blank">📅 23:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138278">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdvMlKMl7BTKhIJsbhQCAgcu--6awgCnES7gHrMdTSZEHjfLauZlpTjjB5FHbmdGxTVaWAKqkA1OeF_DCNCxVo8sCo6fCaSfcuy8yK2E3Pt1J4GrG16HQSIL26_5L7qmBnAM4tbJRdCTw2MlVqhpGIMpwxFKJOwZ2Zh3dcnoZvlj9woKat2nq8ZzmPJ9_ywbyOBf5Rvf532ju8Qn_TfmsyHy4ziF9Nw4rfnRH9xfX66WzdMp16jF8UINz8Q54iIyFRjDwNX4T8psekdUrReI9Qul262Y8c-lQV3ed4WmU0CLh-KgMfE2D507aYT0VS-T0JKnBo01Q7vaQveffHjfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار کوتاه زلنسکی و نتانیاهو در حاشیه مراسم لیندزی گراهام
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/138278" target="_blank">📅 23:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138277">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRoTs8r2eY_Zo6npCPCLoauL1MVazFk-P8A8hZrEfQ1gAq5MVIehw3u7oy_QK2veXQ6cAae1KBviDWAUOe1Fu2mZCvb4AtaT-k1ixrLLpz7qvFT0Oei-O6hQDEX7TxFaqaVe3SeYnL0fDGDOiK-ka28g1WdLl_zFwHQLEMst_vXLDVPTli6jyAUE4p8pqx1yC05_L7djCuvSEfn7Jch3jiXspWq4VeCNTLLgwH7Uv-iI5sFfY3FcgtbixPVUwS1bK2K_G3E7Cs2zBMm9GWtSc3RCXzm9q4M3k8qrxZnXj7WjLqq8h74CxYAtAPSWEZwTXkHRL6T-Izi4z6lRkY_JeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان UKMTO (سازمان دریایی تجاری بریتانیا) اخطاری را صادر کرده است، در سواحل شهرجازان، عربستان سعودی. این حادثه در تاریخ ۲۷ جولای (تقریباً ۷ مرداد) رخ داد. این اخطار پس از بیانیه‌ای از سوی گروه حوثی منتشر شد که امروز ادعا کرد به تانکر سعودی به نام "NCC Ghazal" حمله کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138277" target="_blank">📅 23:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138276">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
جروزالم پست: نتانیاهو به‌صورت محرمانه به ایالات متحده سفر کرد؛ پس از آنکه نهادهای اطلاعاتی درباره تهدیدی از سوی ایران هشدار دادند.
🔴
بر اساس گزارش N12، نهادهای امنیتی اسرائیل توصیه کرده بودند که پرواز نتانیاهو در شرایطی کاملاً محرمانه انجام شود؛ زیرا گزارش‌هایی وجود دارد که نشان می‌دهد ایران تلاش‌های خود برای هدف قرار دادن مقام‌های اسرائیلی را تشدید کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/138276" target="_blank">📅 23:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138275">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تسنیم: طبق آماری که به دست آوردیم ۷۵ درصد مردم خواهان کشتن ترامپ و نتانیاهو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/138275" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138274">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عربستان : چند پهپاد رهگیری و منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/138274" target="_blank">📅 23:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138273">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbvGZA2z9UuTBPYzUdk2XzvLsEwWqIIayAhOGObVtgNmkU-QLWqvPz-tcCdrh59QejlMPPqZWf0IbupnRJxo-TgEscDbMX-HLxpAXVzPrRsLhp8c7x1guln95yMunbads6lquL1HIFhmMLkoNcevM4kqWMfjrc5wyNqtegw94MHKJ3284xwCrHREHqRXzCI7ragSfMEOwuAr6Qeatak2aWBWmHvF7BmbyFoQshAhqShNCXZ-8IjdSRjgGCgxsyqOc_xsHcHXVmLuwouMnItqvcDvwUWmgzOlMYBAeKclIQu7OvnVmDh6ChWsFw6kzkZVDeyWYzXwYjV9fnZ-5c0fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">POUYAM SMART CITY
آینده از اینجا شروع می‌شود.
یک شهر هوشمند دیجیتال که در آن شبکه اجتماعی، هوش مصنوعی، سرگرمی و فرصت‌های جدید در کنار هم قرار گرفته‌اند.
به آینده متصل شوید.
🌐
https://t.me/POUYAM_APPBOT?startapp</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/138273" target="_blank">📅 23:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138272">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبرنگار المیادین: صدای یک انفجار در حومه اربیل در کردستان عراق شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138272" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138271">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
خبرنگار المیادین: صدای یک انفجار در حومه اربیل در کردستان عراق شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/138271" target="_blank">📅 23:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138270">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
طبق گزارش ها حساب روابط عمومی سپاه در تلگرام، حذف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/138270" target="_blank">📅 22:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138269">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb4c77ecf1.mp4?token=Uy6-il7N3ySBeKwjNJeJge-G_RI2NkP5JGinX9JV9ccM6_9_Cj9K6Qp7s5luaz0fFYf-WB2C2x8wsI8PE_qtV4DgNiTHo5ETFZ-QlkEzUjX_Xuay1H-JmwiIsI6YIAu3GIMsaA3Rm2ityREysOxs4otQG_ep3Euh9bT9fky0G1THbew1dYL2o_xBryVp7gR3ib26xFpBK-lBILxNq2YFPtE0wuPFyMWxoPKqjL2vx70msIRk4OOkYUN_lRtIiDrkKYz1enQXMosZ4RYwjGPO0Cm33mtOxPPLHbL_07q1JFcfWB95M9-zHYkJ6MP65zHrhYrGGEhSWzB_LyGAw2pJeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb4c77ecf1.mp4?token=Uy6-il7N3ySBeKwjNJeJge-G_RI2NkP5JGinX9JV9ccM6_9_Cj9K6Qp7s5luaz0fFYf-WB2C2x8wsI8PE_qtV4DgNiTHo5ETFZ-QlkEzUjX_Xuay1H-JmwiIsI6YIAu3GIMsaA3Rm2ityREysOxs4otQG_ep3Euh9bT9fky0G1THbew1dYL2o_xBryVp7gR3ib26xFpBK-lBILxNq2YFPtE0wuPFyMWxoPKqjL2vx70msIRk4OOkYUN_lRtIiDrkKYz1enQXMosZ4RYwjGPO0Cm33mtOxPPLHbL_07q1JFcfWB95M9-zHYkJ6MP65zHrhYrGGEhSWzB_LyGAw2pJeDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شان هنیتی، مجری فاکس‌نیوز، در مراسم خاکسپاری لیندزی گراهام خطاب به نتانیاهو گفت: لیندزی اگر می‌دید که شما (نتانیاهو) این مسیر طولانی را طی کرده‌اید تا امروز اینجا حضور داشته باشید، واقعاً تحت تأثیر قرار می‌گرفت.
🔴
او شما را دوست داشت.
🔴
او اسرائیل را دوست داشت.
🔴
او مردم اسرائیل را دوست داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/138269" target="_blank">📅 22:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138268">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7840f687c.mp4?token=Vcr5WuQoy15EW8jqNu3UIX8O27ivaRlvOMMQ0TUlrPo9cBsYIcYwa8VwSk7zAvgEAXCvOcECfpGnvpcqwpVVto7NkdchEGzP6bVFpSqdktviTvxBiStQ59ktSkGRghX0Hbk3Ypw5G4c8Zgyk9XmUYwbUdYNdTSFiXmkUT3lnajlQ-Li2GGN3ki9_gGzjZPoCErzh1fjlo6nGwmZRtb_yjqQuyKGrf7tQB0gS2C-3STuB67mC4Mqs5xhYj0yrK5Aa3JuqZr4K0ox4rw9W-B75v7E6mIt6x2wR_LqQRhlY-JVOgnOxUOb6zTocrdspgqb0KePG8iNZuN6jdlSj2l2Kkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7840f687c.mp4?token=Vcr5WuQoy15EW8jqNu3UIX8O27ivaRlvOMMQ0TUlrPo9cBsYIcYwa8VwSk7zAvgEAXCvOcECfpGnvpcqwpVVto7NkdchEGzP6bVFpSqdktviTvxBiStQ59ktSkGRghX0Hbk3Ypw5G4c8Zgyk9XmUYwbUdYNdTSFiXmkUT3lnajlQ-Li2GGN3ki9_gGzjZPoCErzh1fjlo6nGwmZRtb_yjqQuyKGrf7tQB0gS2C-3STuB67mC4Mqs5xhYj0yrK5Aa3JuqZr4K0ox4rw9W-B75v7E6mIt6x2wR_LqQRhlY-JVOgnOxUOb6zTocrdspgqb0KePG8iNZuN6jdlSj2l2Kkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مراسم خاکسپاری لیندزی گراهام: لیندزی، ما دوستت داریم.
خدا حفظت کند.
🔴
ما همیشه با تو خواهیم بود.
🔴
تو واقعاً فردی بسیار، بسیار ویژه بودی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/138268" target="_blank">📅 22:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138267">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c3ca77852.mp4?token=nRbVQNXvxTagnl3QoiRbtPjUGSlx2EVS4lKlARHR3eoJH_dZRa62WnnVOfl3cprMgIxwvy8XtwkofbBM4pD3UWdKOwWuxx8g0wX2k-UNRN9n_A9EtY-vhUp-9vzuSsxoReQDWVVcpcsEklBT1sWrkbsmK7K5SjIGEg2iz3vYp5qt0ZPQhqh9--VW1NnGB0_Grx4sRGoLl-2zlMGg7KDgrdEvJUwkeJu-0mcgeXWB_lih721TAhxuy1TdsAtfGWiFITwTVigO99qNUdjE67vmdlAQ3lKAEgbb0UsmT99B8kA2wIBwpazz48_jlUpj0HEPbmp6ozlMbPuSLZm6eEiabg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c3ca77852.mp4?token=nRbVQNXvxTagnl3QoiRbtPjUGSlx2EVS4lKlARHR3eoJH_dZRa62WnnVOfl3cprMgIxwvy8XtwkofbBM4pD3UWdKOwWuxx8g0wX2k-UNRN9n_A9EtY-vhUp-9vzuSsxoReQDWVVcpcsEklBT1sWrkbsmK7K5SjIGEg2iz3vYp5qt0ZPQhqh9--VW1NnGB0_Grx4sRGoLl-2zlMGg7KDgrdEvJUwkeJu-0mcgeXWB_lih721TAhxuy1TdsAtfGWiFITwTVigO99qNUdjE67vmdlAQ3lKAEgbb0UsmT99B8kA2wIBwpazz48_jlUpj0HEPbmp6ozlMbPuSLZm6eEiabg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لیندزی گراهام: کشور ما به مردان و زنان بیشتری مثل آن انسان بزرگ نیاز دارد.
🔴
فکر می‌کنم می‌دانم او اکنون کجاست؛
فکر می‌کنم او آن بالاست.
🔴
و فکر می‌کنم دارد ما را تماشا می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/138267" target="_blank">📅 22:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138266">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
به گزارش وال‌استریت ژورنال، دونالد ترامپ پس از موفقیت‌های اخیر اوکراین در میدان نبرد، به ویژه توانایی‌های پهپادی و مقاومت آن در برابر روسیه، نسبت به زلنسکی، رئیس جمهور اوکراین، رویکرد مثبت‌تری پیدا کرده است.
🔴
ترامپ که زمانی معتقد بود اوکراین شکست خواهد خورد و از زلنسکی انتقاد می‌کرد، اکنون او را به عنوان یک رهبر قوی‌تر می‌بیند و نسبت به ولادیمیر پوتین بدبین‌تر شده است. ترامپ همچنین به فناوری دفاعی اوکراین، از جمله تولید پهپاد و همکاری در زمینه موشک‌های پاتریوت، علاقه نشان داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/138266" target="_blank">📅 22:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138265">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
العربیه:
یک منبع ارشد در هیئت همراه نتانیاهو گفت نخست‌وزیر اسرائیل و رئیس‌جمهور آمریکا، در واشنگتن دیداری «بسیار مثبت» داشتند که در آن متعهد شدند اطمینان حاصل کنند ایران هرگز دارای سلاح هسته‌ای نباشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/138265" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138264">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d25d76fc.mp4?token=Fx9nZyIw43SIUbIDy7DeqZzRwMBCwWlnJZoI1C3W6hFNvcBmQTgQ_SnmXO9ongsnxIKd0p-9T4xR35IznnMp2vW0GoQNNTXSqdj3ImecPh1p8XlKjeeE_0LLMFfcNH3url7kVehZpkUWm_k5ZUmftDMdA72DRvnDqtzJhE09i27hAUrcDfXdv-fYhKU46VjQTuo6IdsoXXq16qB3Y4vdgJmBU1b_pnXqcz8PeIZngW7ul9jdacSxjpbhnHMkNIN0fjQjoWBksz0KbF7D_AVqQ4GY-rqU4Lteyx-l_5GeK1XoHnjgXR01IIHc78lCEYBRDw7vzqnzoyxXLV15evMjkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d25d76fc.mp4?token=Fx9nZyIw43SIUbIDy7DeqZzRwMBCwWlnJZoI1C3W6hFNvcBmQTgQ_SnmXO9ongsnxIKd0p-9T4xR35IznnMp2vW0GoQNNTXSqdj3ImecPh1p8XlKjeeE_0LLMFfcNH3url7kVehZpkUWm_k5ZUmftDMdA72DRvnDqtzJhE09i27hAUrcDfXdv-fYhKU46VjQTuo6IdsoXXq16qB3Y4vdgJmBU1b_pnXqcz8PeIZngW7ul9jdacSxjpbhnHMkNIN0fjQjoWBksz0KbF7D_AVqQ4GY-rqU4Lteyx-l_5GeK1XoHnjgXR01IIHc78lCEYBRDw7vzqnzoyxXLV15evMjkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره لیندزی گراهام گفت
:
او به‌شدت جنگ‌طلب بود.
راستش را بگویم، هیچ جنگی نبود که از آن خوشش نیاید.
فقط دوستان نزدیکش منظورم را می‌فهمند؛
اما او فکر می‌کرد همه این‌ها به نفع کشورمان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/138264" target="_blank">📅 22:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138263">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrgi2iXBqJALtvJEDSpCvin0YkkKDOneC3IRBfsAGWlPaACFwJiW-75NUPbWbMXoqBuQ61FCBXkokABbZ37rhXNthm4WaiyHhQlBeMW2mW76Vy-921ROYpzaCnp_xRGvTETnqwA1dJfM7tAjqo6n08UVz8vSBxDz1L8Vnedl2fRJkt7mfCFQggHbnafuo7Vctdh3Mw7bUb2OClZmhY9j0s4PNuCcB6gStvop0mAmjla14vFM7EYXWkMaqJXGfwL_-xJV5-FWnEHiZg8PwCvwbAM5Wor7K7CECeO9stXubs2FK8Asx9hprXQrtEC3RzPux2WoONDQ-Jq2oZJyg8Ic1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شکلات شیری خرگوشی در آستانه یک میلیون تومان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/138263" target="_blank">📅 22:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138262">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd212</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/138262" target="_blank">📅 22:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138261">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rh27TtMEmL62XfYOO-z5DXWjx3u7I8a0gg6-evigXxEiZvhVctpNL5XorGjzw7JLmonNbV9qV90WODKAa841pfzhNDV2fLjv3UtyXJuP6dVGnLvlRenH44fCJQawKylFp1mqFoxj_Y0aLJVS4QCezgRbJLoPal0L_mQk1kdBqO0IPyu1xXgquUpIjlINmKzDOOm5zyJwIzoLRkHgAoz2DBUK4aRUng4OaPWcGYkbikCZtMdu_VK_0BIRjwZaheE6rvy5yYZQDG8DIFRlNdTxalhe9aWd8CMaM-E6xYxKu0DsMMMR2zg3OTg6UgpChhdS2Fe1wtSsPxvEVXwIjz2X-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عراقچی: خواهان تشدید تنش با اوکراین نیستیم!
🔴
وزیرخارجه اوکراین اطمینان داد که حمله به شناور ایرانی غیرعمدی بوده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138261" target="_blank">📅 22:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138260">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
لحظاتی پیش صدای انفجار مهیبی در استان اربیل عراق شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/138260" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138259">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
غریب‌آبادی، معاون حقوقی وزارت خارجه: هر کس فکر می‌کند که می‌تواند، بالای ۵۰ میلیارد دلار از تنگه هرمز درآمد داشته باشد، کنترات می‌دهیم برود کسب درآمد کند و نصفش برای خودش و نصفش برای جمهوری اسلامی ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/138259" target="_blank">📅 22:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138258">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز:
چین به‌طور مستقیم با انصارالله یمن گفت‌وگو کرده تا برای نفتکش‌های چینی عبور امن از دریای سرخ را تضمین کند
🔴
پکن برای هر یک از کشتی‌های خود به‌صورت جداگانه از انصارالله مجوز عبور دریافت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/138258" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138257">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=nDFXuu-0P8bmKGdLDrSYld9XBamvjo3Mz9N90-8sMyoj3zoOWr4xfYKV27szdtWKldBg2KTC4g4eoc4DP6fyj-OsT7sGqZOau2NKn_XkmnKDLDm15px1IKOOjiD0R81gKx7v_tndT6X1di6CLTMZ4jCqw8cbLDwO-7Z555k8D20HsYNfx7NdbKJsbRRRloX1EtfOD79S8JPd-VE8tjG6rGTjlIcOO6-SXmqccDex8FKD650ONdFVLTvbS6PeWsw6Ycnc7I1eNseTc-YJCKE1Tr82HXUlHnrQ4cIaLZwUCnhheb60oBPWLjOGGn99eNKceiopiGr0vscv95jVZ14iDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=nDFXuu-0P8bmKGdLDrSYld9XBamvjo3Mz9N90-8sMyoj3zoOWr4xfYKV27szdtWKldBg2KTC4g4eoc4DP6fyj-OsT7sGqZOau2NKn_XkmnKDLDm15px1IKOOjiD0R81gKx7v_tndT6X1di6CLTMZ4jCqw8cbLDwO-7Z555k8D20HsYNfx7NdbKJsbRRRloX1EtfOD79S8JPd-VE8tjG6rGTjlIcOO6-SXmqccDex8FKD650ONdFVLTvbS6PeWsw6Ycnc7I1eNseTc-YJCKE1Tr82HXUlHnrQ4cIaLZwUCnhheb60oBPWLjOGGn99eNKceiopiGr0vscv95jVZ14iDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو و ولادیمیر زلنسکی پیش از مراسم تشییع سناتور لیندزی گراهام در حال گفتگو دیده شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/138257" target="_blank">📅 22:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138256">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
رویترز: چین به‌طور مستقیم با انصارالله یمن گفت‌وگو کرده تا برای نفتکش‌های چینی عبور امن از دریای سرخ را تضمین کند
🔴
پکن برای هر یک از کشتی‌های خود به‌صورت جداگانه از انصارالله مجوز عبور دریافت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/138256" target="_blank">📅 22:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138255">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4yw7Co4tZf4Rjdj94jtEJrCpl39To3LZIDK1MmFwW8kef-RL6cjhJNVlvoVFo0tt0WAMPay___ZccoqFc38zG9PjLS9zUpHV5iI44uy0a4It2JJJXlUpGpAZmmgxAYxpdD_vnRxrAM2RWC63WBwoEDeCB8boFPPImhb6xyftn7D4xNDu62yyvUXFUcaNkEKV21vK8stsRUbQvTeuQadYebRpQx3vwaZ_jklfPQ-vJGOjRJM_R5BxxuJyGPHfqo6-vWJ1vB7z509XKOzu9q8il2IeB5E0FedhwlUQKbftHYKO4okZKovRvQpcrceqsLQCMOppnpYTclM_S2umfdA1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش های متعدد، سپاه پاسداران در حال آماده شدن برای حمله موشکی بالستیک به اوکراین است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/138255" target="_blank">📅 22:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138254">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23353f0376.mp4?token=Yk0OW3U59LJqxjUVxlwWCsdM6tq_GQtpRP8zc8abLJEIDXSU1HegaCc_ECdO3Q4wHW7puN9V9KfsM8LQFO_mAuXm-ZiPIHa2oAslw4XPvv7kV4R1f-_n97XozLlzKjaBBODnzxO06XH-EYqnEDmwhob0wPW53eAL363lEy9hZYTyPaOb2u_Ca5vJtdQj2nhrbVxWp4-U_33tXHVGKLp0ax_OKjUON7Pvs128f5M0-dMVMtDFBmfs3SbqWyc7bQ4MEW3wpvP4F07tH-93dvQt26yxEAYTfrydWHFmSSPxJEOm0lxKPifQPTJFeyE2TwHQeOCs4hYPtGDBG8HYIbh34A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23353f0376.mp4?token=Yk0OW3U59LJqxjUVxlwWCsdM6tq_GQtpRP8zc8abLJEIDXSU1HegaCc_ECdO3Q4wHW7puN9V9KfsM8LQFO_mAuXm-ZiPIHa2oAslw4XPvv7kV4R1f-_n97XozLlzKjaBBODnzxO06XH-EYqnEDmwhob0wPW53eAL363lEy9hZYTyPaOb2u_Ca5vJtdQj2nhrbVxWp4-U_33tXHVGKLp0ax_OKjUON7Pvs128f5M0-dMVMtDFBmfs3SbqWyc7bQ4MEW3wpvP4F07tH-93dvQt26yxEAYTfrydWHFmSSPxJEOm0lxKPifQPTJFeyE2TwHQeOCs4hYPtGDBG8HYIbh34A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از دیدن این کلیپ متوجه میشید الماس چقدر میتونه از طلا گرون تر باشه.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/138254" target="_blank">📅 22:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138252">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h37vWiltPLLrR4anLUejspEtAv7KLyMzYllqE__DnUu1GwdNZMhk2vL5xBeySf6Aeaq5tdkmi9udnnpQ47i2CWtVjdDfr1bAuL1sf7AHXkGUaZnZVkadi7Wa_89x9vcXEe3BmsI2yik0T-Kj9n6xX0Pgz1v798PPffmVGqiCsVLNR4MRWJ6l5QPGK3BpxCqRtokMvSPFkqACZGV3wl02ZQEKiwV6D08idTWsqr07kSo8vKzxnaJBOUcOVLJukZFyBVOZ9bDGaG_RzTBC7ER66zp2GwgmP5fr0fAEgrSILAVl4-6aQiHPeP7GpXZ2c32jaOMuvvlKoT_ISk126fBh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950c5db38a.mp4?token=FtAC0B7GQO004zEve2AcrouMsuRehNvED5rcUr-B0AXP-yDyZg6YNt7fc4dUTVR33qQrqk20YRH2-XWw9ariJILRNrSoFZYyGscgX7WjA-SiylqU6Weugpzwa5gjKgOUAQACi5PSrfv_k5raNfOG3727Cybif5jtbFX-yQ0mNadLJQY80TPO56Zm-VpC4A1eTOx0uC8dxGGMaCF3uahm71ySHWfA_sGXJcuclMkn9ba4r-D18usev1fNzCwc1fowJoD-f08Mmwj3CSM-6SOO07gaxOaQmkPHuvVGAkQyTCRSqxSAUGL7ykbIy7DrfYQceDu1ENRjq6Ee9DE6Kd3JBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950c5db38a.mp4?token=FtAC0B7GQO004zEve2AcrouMsuRehNvED5rcUr-B0AXP-yDyZg6YNt7fc4dUTVR33qQrqk20YRH2-XWw9ariJILRNrSoFZYyGscgX7WjA-SiylqU6Weugpzwa5gjKgOUAQACi5PSrfv_k5raNfOG3727Cybif5jtbFX-yQ0mNadLJQY80TPO56Zm-VpC4A1eTOx0uC8dxGGMaCF3uahm71ySHWfA_sGXJcuclMkn9ba4r-D18usev1fNzCwc1fowJoD-f08Mmwj3CSM-6SOO07gaxOaQmkPHuvVGAkQyTCRSqxSAUGL7ykbIy7DrfYQceDu1ENRjq6Ee9DE6Kd3JBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فقط حقوق ها رو در آگهی استخدامی ببینین
🔴
جمهوری اسلامی با وقاحت تمام خود را مدافع وطن میداند درحالیکه کشور را به فلاکت رسانده
🤔
لعنت خدا بر حرام زاده هایی که مردم ایران و این کشور ثروتمند رو به این روز انداختن. شیاد هایی که آخرت را به مردم فروختند ولی برای خود کاخ های دنیوی ساختن. عرعر شما هم به سر میرسه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/138252" target="_blank">📅 22:18 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138251">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ : لیندسی، ما دوستت داریم
خدا ازت محافظت کنه، ما همیشه کنار شما هستیم، تو واقعاً خیلی، خیلی خاص بودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/138251" target="_blank">📅 22:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138250">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ درباره لیندسی گراهام : اون یه آدم خیلی تندرو بود. بهتون می‌گم، هیچ جنگی نبود که ازش خوشش نیاد
🔴
فقط دوستای واقعی‌اش می‌تونستن اینو بفهمن، اما اون این دیدگاه رو برای خیر و صلاح کشورمون داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/138250" target="_blank">📅 22:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138249">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
ترامپ : فرقی نمی‌کرد اوضاع توی واشنگتن چقدر پرتنش بود
🔴
تقریباً همه، چه جمهوری‌خواه چه دموکرات، لیندسی گراهام رو دوست داشتن
🔴
البته نه همه؛ ولی این حرف خوبیه, همه که نه
🔴
باید قبول کنم، اون شخصیت خیلی قوی و سرسختی داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/138249" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138248">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=sAcaX5PAQ06MacQZwWdfx1Na0vx2qaYo3Mmdz7_bvFfYykZcFQnkY_2WEa4b790paFrS33_3ocHuPx7n0Msfcvm-OMYymCCVbyUprDfiK5S3g7Le4nhrrYVbxMMjQEajHHhC1Nyl3r-xpZL2sbNXISEfZxsPGwP60sCSASlAbcy3zxtHk9p-jPFjI2ZAvuddgEuzIao3LMJKVn9MIJBDIGCgQB8q7KvrhbJTQV8R87Hwu-v0HQV15lOmRC29BLlKUqm9iH-3YEgpEebmhlVEgGa_BZJxckufYuw0-Q6mV1REIwJzvNHTzPC8ao0kWVJlypxVU0e2Se80NiOFpOne_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df79cbfe8.mp4?token=sAcaX5PAQ06MacQZwWdfx1Na0vx2qaYo3Mmdz7_bvFfYykZcFQnkY_2WEa4b790paFrS33_3ocHuPx7n0Msfcvm-OMYymCCVbyUprDfiK5S3g7Le4nhrrYVbxMMjQEajHHhC1Nyl3r-xpZL2sbNXISEfZxsPGwP60sCSASlAbcy3zxtHk9p-jPFjI2ZAvuddgEuzIao3LMJKVn9MIJBDIGCgQB8q7KvrhbJTQV8R87Hwu-v0HQV15lOmRC29BLlKUqm9iH-3YEgpEebmhlVEgGa_BZJxckufYuw0-Q6mV1REIwJzvNHTzPC8ao0kWVJlypxVU0e2Se80NiOFpOne_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو و ولادیمیر زلنسکی پیش از مراسم تشییع سناتور لیندزی گراهام در حال گفتگو دیده شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/138248" target="_blank">📅 22:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138247">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4a4e00d89.mp4?token=IZ4UVQ7EhpIvZ24ClOP5iT8pe2xh0ftx7tVLTzsFNvPWcSXQhXmWaCc9uGNKnZNhy50eXvO4oqBE2lEerOUinu8eNwTWEMSGBj7Q2lzgynuYoUxshPS6FNTVCkjWSWN8ds8xq73RddERBsO2msX17sZAztBG0m1D2trxMgm9spV5VjYcmBzn-ezikmVtihn2O4_sVlMtN-Nf1aom8N_RJf0ld_wNYb5v7uusCK4gDcAQziBqFr2ugD_esWX6k79IZrspdydX2uHM3xb8PMRUkFvgefQxa7liFF71uIHMbUwde2dlO3FZ1k4uTPKv_oAcD4p3vVGeamiOVNuDZYxhnZE92t_5H0TI_RBUqLgquGA8N4mT8wfiFJSBghyO4HdxiK6RYggWBSQzWE_-ox8N2wxI1mcWnNUuQMIou9ymwkskoM836KT1zvgnRmp3gyguc2XyFGnVzugWOWqwbilQLfbnqGcbnZMigBFsKcIYi15ys1K7ZpHKLt3F-QJyApz0YGU8bTXpZuPGZ_R1dwuBv9k7aPPAQ3g-7GAhuTl2fZM6mPF-nwXK_xsc_uVJ3sMYnKFS6Mi-Y-PzLu4v3cGyEqcCXnTbIX38Ro0HA21Vu-s7GhNl_L-ar0QTLDCjQpto98ZeTfcJ0R-iNTFEmBTC8fm5wIccK0KXZlTYfAn6_jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4a4e00d89.mp4?token=IZ4UVQ7EhpIvZ24ClOP5iT8pe2xh0ftx7tVLTzsFNvPWcSXQhXmWaCc9uGNKnZNhy50eXvO4oqBE2lEerOUinu8eNwTWEMSGBj7Q2lzgynuYoUxshPS6FNTVCkjWSWN8ds8xq73RddERBsO2msX17sZAztBG0m1D2trxMgm9spV5VjYcmBzn-ezikmVtihn2O4_sVlMtN-Nf1aom8N_RJf0ld_wNYb5v7uusCK4gDcAQziBqFr2ugD_esWX6k79IZrspdydX2uHM3xb8PMRUkFvgefQxa7liFF71uIHMbUwde2dlO3FZ1k4uTPKv_oAcD4p3vVGeamiOVNuDZYxhnZE92t_5H0TI_RBUqLgquGA8N4mT8wfiFJSBghyO4HdxiK6RYggWBSQzWE_-ox8N2wxI1mcWnNUuQMIou9ymwkskoM836KT1zvgnRmp3gyguc2XyFGnVzugWOWqwbilQLfbnqGcbnZMigBFsKcIYi15ys1K7ZpHKLt3F-QJyApz0YGU8bTXpZuPGZ_R1dwuBv9k7aPPAQ3g-7GAhuTl2fZM6mPF-nwXK_xsc_uVJ3sMYnKFS6Mi-Y-PzLu4v3cGyEqcCXnTbIX38Ro0HA21Vu-s7GhNl_L-ar0QTLDCjQpto98ZeTfcJ0R-iNTFEmBTC8fm5wIccK0KXZlTYfAn6_jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراسم خاکسپاری لیندیسی گراهام با حضور ترامپ درحال انجامه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/138247" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138246">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59af49fe1e.mp4?token=lZa-0ZZUjODNtmyq1EtHFCFHtI4p5huWXRnoKISXeztj8FzIev3r4D4RXBi_Vn9E_wTg2S6hdY6xwaKAn2oA-XY0Pa_1Oe-Kwu_RjWZ5iQD2vokLY4SBwE-goW020ymGojnt8gBI7dpwqRHlF4UVvp-bYYz_dpzlkUPu4f9d7GTCCpkGKQjV6VHh14viZeO3ZycvUW-EUPw4zcP6Vaao0cdfpzPV7m7sjnZ8nYsrLHCE2myGYw09wWBp5x1O4nGPjhwT-Wf30chCP7vsA-SDnwXMX1XZ6M7dpRckxpxMaC-uLUFzBFGyCs0zVFAnovosp72o2d5s_7pydUYQuUgIlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59af49fe1e.mp4?token=lZa-0ZZUjODNtmyq1EtHFCFHtI4p5huWXRnoKISXeztj8FzIev3r4D4RXBi_Vn9E_wTg2S6hdY6xwaKAn2oA-XY0Pa_1Oe-Kwu_RjWZ5iQD2vokLY4SBwE-goW020ymGojnt8gBI7dpwqRHlF4UVvp-bYYz_dpzlkUPu4f9d7GTCCpkGKQjV6VHh14viZeO3ZycvUW-EUPw4zcP6Vaao0cdfpzPV7m7sjnZ8nYsrLHCE2myGYw09wWBp5x1O4nGPjhwT-Wf30chCP7vsA-SDnwXMX1XZ6M7dpRckxpxMaC-uLUFzBFGyCs0zVFAnovosp72o2d5s_7pydUYQuUgIlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : همین الان یه جلسه خیلی عالی با رئیس‌جمهور ترامپ داشتم؛
- وقتی می‌گم عالی، فقط یه تعریف ساده نیست
- یه گفت‌وگوی صمیمی و کامل داشتیم، با حمایت متقابل و درک مشترک درباره هدف اصلی؛
- اینکه مطمئن بشیم ایران سلاح هسته‌ای نخواهد داشت و به اهداف دیگه هم برسیم.
- این یکی از بهترین گفت‌وگوهایی بود که تا حالا با یه رئیس‌جمهور آمریکا داشتم؛ با دوست‌مون دونالد ترامپ.
- تیم‌های ارشد دو طرف هم حضور داشتن و درباره اقدامات مهم برای امنیت و آینده اسرائیل هماهنگی و تبادل نظر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/138246" target="_blank">📅 21:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138245">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ادعای کانال ۱۲ اسرائیل: نتانیاهو به ترامپ تأکید کرده که حملات بیشتر علیه تأسیسات هسته‌ای بازسازی‌شده ایران اجتناب‌ناپذیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/138245" target="_blank">📅 21:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138244">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزیر خارجۀ اوکراین: با همتای ایرانی‌ام تماس گرفتم و گفتم هدف ما دفاع از کشورمان در برابر تجاوز روسیه بود و ما قصد هدف‌قراردادن کشتی‌های غیرنظامی را نداشتیم.
‏
🔴
هدف ما، اجتناب از هرگونه تشدید تنش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/138244" target="_blank">📅 21:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138243">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuu0-1OIt7uWB7-9k-EqD-z0HQz6AMkuoRRs7ukY2SfaZj46Wv9PfRkddAbS-Z7aurvgfVMuGkP1jPqJAMJa1V6U6b240rKvaAAijGXwqrV6L3ozYiWdeS3l9lLRgpRbqw1oFNhosk-SCQzv_WwdqK8VmAIWp8Kfzt_kqCnWHVStbAcf2h2CcyRYC9qj5nZ-leEOCzuyOPX01NI6rd81_rTYyTzTclNpBPFu94hNURASlZGKYrn93m2qvMQpYWgT1eVGiZwQJbs_LT8_-G0GPfg-6R-07mzfncsF0-O2Joq9wXxLRMRL2shxn2tUA7fd2opQ0et_B4uSHZBDSG-75w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف:
دنبال بهتر کردن زندگی مردم هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/138243" target="_blank">📅 21:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138242">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138242" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138241">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daaee7b635.mp4?token=bwTHalAq1YIuBxYHzlN-lOgS55UqZ9mYpmLSNJflSsoZ0XcwDx8sFrvGjmpWBCnIR91s3ybypXYY9xsZBoPJ2FaLVd_VjUe5OUNZn304G5EIJ0Wtfg_jEJKMFNocwDTUfSLwkmUax8TgJfO4beK7uLA5tsxvoA1qRvPG8yRH7aSljY6sC3e_227KDDMWVoNUu-JubJKEnqywGVLATCE4KxZqU8S4WAM-2KwzNOS9cdX9YZB7ISd5QtdQvVhXc_TqH9z0sOvZ9Uv7NIMvCKDDmsqhhNqNFepKcM_NG73sLapstUqRI54K06rx3HqJ0c7dcK74dZooUtot97n0RHr6ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daaee7b635.mp4?token=bwTHalAq1YIuBxYHzlN-lOgS55UqZ9mYpmLSNJflSsoZ0XcwDx8sFrvGjmpWBCnIR91s3ybypXYY9xsZBoPJ2FaLVd_VjUe5OUNZn304G5EIJ0Wtfg_jEJKMFNocwDTUfSLwkmUax8TgJfO4beK7uLA5tsxvoA1qRvPG8yRH7aSljY6sC3e_227KDDMWVoNUu-JubJKEnqywGVLATCE4KxZqU8S4WAM-2KwzNOS9cdX9YZB7ISd5QtdQvVhXc_TqH9z0sOvZ9Uv7NIMvCKDDmsqhhNqNFepKcM_NG73sLapstUqRI54K06rx3HqJ0c7dcK74dZooUtot97n0RHr6ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
المیرا شریفی مقدم: سینگلم یکی بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/138241" target="_blank">📅 21:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138240">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فاکس‌نیوز:
محور اصلی گفت‌وگوهای آمریکا و اسرائیل، تصمیم‌گیری درباره گام‌های بعدی پس از حملات اخیر به ایران بوده.
🔴
همچنین نتانیاهو احتمالا اسناد و اطلاعات تازه‌ای ارائه کرده که نشون میده جمهوری اسلامی با وجود صحبت از دیپلماسی، همچنان برنامه هسته‌ای خودش رو پیش می‌بره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/138240" target="_blank">📅 21:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKfpe7bFIyidUtybEBK-0vPPZoQthZap9MAUp2351wZpqAPpTJa_RSznQJDAYrR8fqRaYNapdSXEEkZ9_vzd8hmXXa2bnWpE-qV5ZX9yzeSafFEd7pa9mThckN2mdwn6nK3rrSoLB6LFC5k3u9kUvDsgznxPK-zf5BQKh-KkjR8JZVGn65y7I5obi7G9PdMrfdouee5yu3Uttvox2qzeUhu7gz8coDLvYmSZvf1gBT7czf8Vc8wIt6O-HzvJwDdum3pAVbWY3Ft2vcqNUygXFOmFRTm4C9PAUoPQGP8sBRCTeQzRVHYyxeBnTMBJLNojbGalOHIsXtSA7m_uMV2wLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: تا ۲۸ ژوئیه ۱۸ کشتی تجاری تغییر مسیر داده شده، ۲ کشتی از کار افتاده و ۲ کشتی هم بازرسی شده‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/138239" target="_blank">📅 21:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
👈
شبکه 11 عبری:
ایران تلاش‌ های خود برای آسیب‌ رساندن فیزیکی به مقامات ارشد اسرائیلی، چه فعلی و چه سابق، در تمامی سطوح و رده‌ ها را افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/138238" target="_blank">📅 21:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138237">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd1db5e6.mp4?token=uzBAxS3X88E67fUTgnktL9HzHySapMOPtZkJHaqKcdJHHber-xFutTpBSdavATsYMuwfCbbKYgj_aTl45I3kruvkGTu97sK_FJ7_-iU-3PZ9lpcMHU2nKO8nFoHQLD9CDgxiqyeAhtTkK3A7l-0oY-aDI3EOlL4cTyLvBJazTEezOQR0ulsqJY9Q0ykNWY7QW9CafMquLLEjBnQaMQswZrg4bml_6WDfCS4GIjC-1apySHT8YxPv7Yk-m9UUN0if2dZcHnP5J5vLMzUXcAzaDI9K76fk4r4AQhP3U0rcmIQ0sSiolPMmmYDGc64H-8oXnf_rARlX7NR8s3weIuaSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd1db5e6.mp4?token=uzBAxS3X88E67fUTgnktL9HzHySapMOPtZkJHaqKcdJHHber-xFutTpBSdavATsYMuwfCbbKYgj_aTl45I3kruvkGTu97sK_FJ7_-iU-3PZ9lpcMHU2nKO8nFoHQLD9CDgxiqyeAhtTkK3A7l-0oY-aDI3EOlL4cTyLvBJazTEezOQR0ulsqJY9Q0ykNWY7QW9CafMquLLEjBnQaMQswZrg4bml_6WDfCS4GIjC-1apySHT8YxPv7Yk-m9UUN0if2dZcHnP5J5vLMzUXcAzaDI9K76fk4r4AQhP3U0rcmIQ0sSiolPMmmYDGc64H-8oXnf_rARlX7NR8s3weIuaSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ژیلا صادقی به پژمان عشق ابدی : خیلی هوشمندانه بازی میکردیا تو عشق ابدی قشنگ مشخص بود رفته بودی اینارو بخاطر این برنامشون تخریب کنی.
🔴
پژمان : والا من رفته بودم ترکیه برای شرکت تو مسابقه ورزشی اون کنسل شد دیگه رفتم عشق ابدی ولی حیف شد الان یه برنامه مثل عشق ابدی طبق قوانین جمهوری اسلامی تو ایران نمیسازن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/138237" target="_blank">📅 20:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
یک نفتکش عربستان هدف حمله قرار گرفت
نیروهای مسلح یمن:
🔴
یک نفتکش سعودی را به‌دلیل نقض ممنوعیت کشتیرانی با چند موشک بالستیک هدف قرار داده و آن را مجبور به عقب‌نشینی کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/138236" target="_blank">📅 20:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کاخ سفید اعلام کرد که پایگاه مشترک چارلستون در کارولینای جنوبی به افتخار سناتور متوفی لیندزی گراهام به‌نام او تغییر نام خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/138235" target="_blank">📅 20:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/138234" target="_blank">📅 20:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coSs-sxOJtXrt8XFf__-spcpnLoHKexTV4zLpJQvnSMrwvYpCSLCZ_QvDkNh5G9NGa5ZgiQz1Y_yA13EZUXOpIEzWbqX-OBWWCvScB_rmsXM7z4166C7Mdk4taCb1xuWclne9LjbFEFTb99o3jYPZ8b_LxFDSvn77GoKjeb9gs00hWtj3tpHCRQ55bNNPUC0N1r3UniTcvWr71_Tk-CXrE-obKzbAI2Ai0rH4iDLwX3Y7gVgFoX6H84WcKJ5THoWkKzcJQrWhgst8Wuum4Pe2nGjVrZBvP_zkimdLS0RUIVxfzeur_rwTNu3ISOpstlhEZTPCt9uxYjLN4rXzhshRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خارجه اوکراین در مورد ایران
:
من با عباس عراقچی، وزیر امور خارجه ایران، برای یک گفتگوی صریح تماس گرفتم. دیپلماسی به معنای گفتگوی مستقیم است، حتی زمانی که این گفتگو دشوار باشد. من تاکید کردم که هدف ما اجتناب از تشدید غیرضروری است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً برای دفاع از کشورمان در برابر تجاوز روسیه است و هرگز به منظور هدف قرار دادن کشتی‌های غیرنظامی یا مردم عادی نبوده است.
این موضوع در مورد اظهارات ایران در مورد شهروند ایرانی که فوت کرده و همچنین کشتی غیرنظامی که در یک حادثه اخیر مورد هدف قرار گرفت، نیز صادق است. هدف ما مقابله با تجاوز روسیه است، که ریشه تمام این حوادث است، و روسیه است که مسئولیت کامل تمام تحریکات و تلفات را بر عهده دارد.
من بر ضرورت اجتناب از هرگونه اقدام تحریک‌آمیز، و همچنین پایان دادن به هرگونه حمایت از جنگ روسیه علیه اوکراین، تاکید کردم. این جنگ غیرقانونی است و باید پایان یابد.
موضع ما بدون تغییر باقی مانده است: اروپا و خاورمیانه شایسته ثبات، امنیت و صلح هستند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/138233" target="_blank">📅 20:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ :
- اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، رابطه خوبی با ایران بسازه
- بعد از اون، ایران رفت سراغ توسعه موشک‌های هسته‌ای
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/138232" target="_blank">📅 20:40 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
