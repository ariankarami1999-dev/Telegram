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
<img src="https://cdn4.telesco.pe/file/sld_673kh4cqwRQ_Uzy2UAs81Pb5pRvql94KTohnG722AylwY5UnsKifTmoMmd-L8VdBEWrtI9ONXOByhjciG3EsXC9Muv2DXHA_kNJWbDpcbRa41k7B-PNWRfZHYWpbE_f-Yq5Wqq1vfnJ94ZU695b6OF-OZ9q1tYDzdQckzq5l-hOAXh_pc6i0E8IIa7QUZ7L1-zIY68houllLR9VXRZX_VTAFNeal70Nj4fMbjO40QDHuWdbl8aqO0XhHHZPh_bcjqvcGj5NRRXbwqNilHA7quNHLBh45JhnPsz2FHPW8nQsHVK_NbKR11do3IPZnT4-o1SmtneFOClhlWThQZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 23:45:05</div>
<hr>

<div class="tg-post" id="msg-79957">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/79957" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">این بازی اسپانیا خیلی دراماتیک صعود میکنه مطمئن باشید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/funhiphop/79956" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79955">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بلژیک به پرتغال زدددد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/79955" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79954">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">داور به حدی به ضرر اسپانیاست که خیلی واضح به اولمو تنه میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/79954" target="_blank">📅 23:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79953">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلیل اصلی بازی ندادن پدری اینه که دلافوئنته احتمال میده که بازی میره وقت اضافه و از اونجا که پدری قدرت بدنی کمی داره و بازیکن ۹۰ دقیقه نیست نبودش در وقت های اضافه ضربه جدی به اسپانیا میزنه
برا همین ترجیح داده تعویضی بیارتش به بازی که ضربه نهایی رو تو وقت های اضافه به بلژیک بزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/79953" target="_blank">📅 22:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79952">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دکی بیا پیوی چارتا ویس بگیرم به ویناک فحش بدم فور بده چنلت فک کنن کاگانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/79952" target="_blank">📅 22:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79950">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاگان اون ۳۳۰ تومنو بگیر بده تتو رو سینتو لیزر کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/79950" target="_blank">📅 21:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79949">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این وسط که اینا دارن به هم میپرن من فقط به این فکر میکنم که اینا اون تتوی کیری رو میخوان چیکار کنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/funhiphop/79949" target="_blank">📅 21:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79948">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سکوت تونی وان کید این وسط خیلی عجیبه، کصکش بیا دخالت کن دیگه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/79948" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79947">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">کاگان: لطفا نگو من اینارو بهت گفتم
ویناک: حله خیالت راحت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/79947" target="_blank">📅 21:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بقیه ویسایی که کاگان به ویناک داده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/79946" target="_blank">📅 21:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/79945" target="_blank">📅 21:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/funhiphop/79944" target="_blank">📅 21:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قطعه گم شده پازل کاگانه، شاهد هردوشون برا پانچایی که میزنن کاگانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/funhiphop/79943" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قشنگ معلومه چند وقته آماده بوده، موزیک ویدیو اینا داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/79942" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">این بک دکی منو یاد دوتا بک کصشری انداخت که اول داد به پوری و بعدش بادپولی رو داد  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/79941" target="_blank">📅 21:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بابای صدف سپاهیه انگار، فک کنم دکی چون رو زنش کراش زده از ایران فرار کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/79940" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/funhiphop/79939" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/79938" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خلاصه اش اینه که دکی میگه ویناک کاگان و دکی رو فروخته بعدش فرار کرده ترکیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/79937" target="_blank">📅 21:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دکی راجب بدهیش: چاقال تر از اونی بکنی اخاذی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/79936" target="_blank">📅 21:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه نشونه هایی از دکی قدیم رو دیدم تو این ترکش</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/79935" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/79934" target="_blank">📅 21:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/79933" target="_blank">📅 21:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/79932" target="_blank">📅 21:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXyA66pBEtXB_34_rGTqYJxZqYBHtA0HD7NoVMSHPfDkIbWoH992WqvsV-YIGfer6CRDUEcwrMMBBMgnefFyXCtGRkPe0b61BsN92F2z8JLbFuxRCejM0uua4WE8E9cZqw-LxNX7m0HLXCZ43abPHGwme39KjOUjAsQiSjl72gCvHe1AchhPXw_hPucZMU2LUTPiOoXl5cfX1ZXZpQRrY0gEvR-7bT7_s-VOaGtaDBDwZJpIkuPJwBwUvd4JkkXlzOFg9mbgSkNv-gxharRd5eFW4TfwBLp5Y56VpCVGiC6g9ycGRo6UAU9CwgxYpQ6UWBguDgYm4DRuaXucB1QBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/79931" target="_blank">📅 21:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79930">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">همون بلایی پوری رو سرش اورد، این دیس جدیدش بیت به بیت پانچه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/79930" target="_blank">📅 21:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79929">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دکی دیس داد باز</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/funhiphop/79929" target="_blank">📅 21:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79928">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLKGOiDbs9e4Yvkq0m6RMHLSTWutdCpC4vJQnp4M7-CFF2401lb6En4O_HOeibuTseZrfjNgvHg9wzh_3mbUia0X5Sp2bO4lqfsW-eSKzOGmglrcpmTu-0OPUMYgeh4vTkUCj9HWaO2DKSFr92pmREBCHX3vtX9IBnjKiThyXPd0AIHZLfH_0F0BTm8LjIsBD_Tg4obYDaogRwSMzFWA1XzvheyHa6kB0SnWWVAafWdB_M-wGWtcqqfl6Vwd7JLGwIsjPM3fbpNit6NplWUfrlJx7Rnyfsw-3lYMf9YYjjD5Pl-86QhRNOv6f6rZumpubIbUiVohhCuAJdvBkPZh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری نیمکته امشب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/79928" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79927">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKhode Khalse</strong></div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/79927" target="_blank">📅 20:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79926">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGYYnRHrRQO44wPPduUMGkogWIMpHGdTwwcWzceY5-x7aJsyrYVnt5-lFnGmlyyYU5HagZmsNAI4Si9n0waN2tA3MDaFALLvwG5gpsJZdvXie4PAsjQ39R0t4ik9QcB7_pB5CNULfgnqreSSEwSX16wb_mIoDnFTUV0OyoDrO4YnH0k-03fEDz_L49-ukgx_T-MzV4l-9yZCH-9jh8UCjSDLDYROcd0w2KG6PaBxJnzqWNWy8lGS-RUl1PZ6TuDi8w_lZ5jlRu35Qkg7A-N3wForPolqs7jg1FCByfXkDUjjbJxCpY4nZmTV58jlWMVWS0IVBWXXUuVSscXkk_YsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم شاهین فلاکتو یادتونه یا نه ولی گفتم بزارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/79926" target="_blank">📅 20:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsWVfOz-mRwC1kVl21p2hjLwft2xic6xe4UzF_TRlwSPvgBP3lu47jOU43ipDo3jwrZz_dey1iVADawwNp6Zgi1a_WeqqS-St7UwrMLXDZ6bnrg91bAto8vp90slJawt-5uPVpUKnPCiPXHO0MXjGjfpCh1KpEySntUiqgu6_aPXJwkGszEcNeRr8-kriBm8oOl-2b0JNJd0DMcbyY4It3J9izzreV5w1SaYiQPsQgIHlv9TnzYEgQsbnQxfWt4bBoiNfiNZEPWK8oNTe41efFwhQCV109uOlgDcjPIqb5gN9HQxIrTpWXXVr1gi0AWa1MmZ6nXRHreL5VddlEWFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا عجب دزدی ای کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79924" target="_blank">📅 19:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79922">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">برای یبارم شده چیپس لیمویی(ترجیحا مزمز) رو امتحان کنید دوستان، مزه بهشت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79922" target="_blank">📅 19:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79921">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79921" target="_blank">📅 19:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79920">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این کصکشو تروخدا
جمله پایانی ترامپ در مصاحبه با نیویورک پست درمورد ترور شدنش توسط سپاه:
به هر حال واقعیت را نمی‌توان تغییر داد؛ امیدوارم دلتان برایم تنگ شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79920" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79919">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79919" target="_blank">📅 18:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79918">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGavNKFElSSC4p5CKFbhRJ_JzVtEEbjjn22HD53bNAIY17tLEojAsfbtfyLBfUvMgIINfaltLEKPE28Q-xcoDAE6uRxnNSlKuMT3T0NSCDrXHC0UlhQko4PATWNrRf6FdstqpW8MAwEB_RQ836lf-phC5vcPdClMMUWpMuP4Ww7FUkofg5Toye9FHPfsq7e5AkEDwPvB3gwkHx5gobxr2zc-mETa-qTYrg21Mhxp_MrZvTHtP2R9ESSFhuGNRb_FojbvJu524CUn-xyGmh2Imk_G0FCc5LatwdK5158E-eaFGDob9YJQHNqi0PeNundjSrUXEzrw6AA-_y8Vz_ysjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک چرا دندوناش انقد بزرگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79918" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79917">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf2d4hIhBbCP_NKNuIrBL8d6kYsVP2qzgJ3t7RWQfTlEydeEmoO2IKhK0Md7dZk_uuYaW6aCWGBmC06BQRlr9eI0mC3V-2lO-nXLkoqFP7ktelyaq74K5Nqhz4mfixLXvA1jtlZI-tlFvfrrMsusWDXbgirk4CeiqppNlF04stFyoBlhmv16UikaBiV77PfeOw0Vi3Z_hg50NTeCNW6K6IRXWWLOvWFZYd1-rTRPvns1kGGEOd_oBntWjR4fVb1ZTztHRpPo6ygwvPD_yapLvBs1jFd3RokGkHus9DPW6MqplI7_I-vsGcrLSCrYxENb8oPmDUvxzEbzjgRtcK8YUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇧🇪
بلژیک
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
جمعه ساعت ۲۲:۳۰
📍
ورزشگاه اینگلوود (سوفای)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در دور قبل در یک دیدار دراماتیک با نتیجه یک بر صفر پرتغال را شکست داد.
- بلژیک نیز در مرحله قبل آمریکا میزبان را با نتیجه چهار بر یک درهم کوبید.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی فرانسه و مراکش برود.
- با توجه به قدرت هجومی لاروخا و هافبک‌های خلاق این تیم، برد اسپانیا گزینه‌ای مناسب برای پیش‌بینی است.
🧠
هدف سرگرمی است، اگر تغییر کرد، مسیر را عوض کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
g19
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79917" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79916">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ریدم کنارک همین الان صدای انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79916" target="_blank">📅 18:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79914">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryEQk6ZStOD-sYT9bJvragiVKNp2oSYTHjp5fzYZq8KiCVzuIzrZluTUPo8XAE6FZrqefcd_3xstmaWOUD2BjC7LXYFNJTkIR8-ltYsFYiimKfuTw1P9I9m3mSTXVLe-7ehzU8V9y-Ghxh8VCb0xZdPjsorOZv5nYlGk7XhjQgK2DCpeP1aKdcmNNXvcGjvPG3MNlBWM1J6JryvgXhE3_d9H_J0HqFsKMKt7SPBaoXSKMUBLgP8YZXxVwUHc4dgNLnmh8I-yCe4AnXi6lsvmR-ejL5usdF53JIxJvqVrw_1mtASlSymv3QVMY-8LZkfsptEwr7Ncumfw0df2pbBNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PccYM0lo3cLj7SVnVtAIYeuP38IPjUevmyLq2ngT3BmRZdcjWumVjnawDQ7MU0PaNxFth5HyEdpWJyYgNwRCbLAYJc1j1d_3WGIOaiqTAkD-MmGtOnhPJERj_-PzW5negoly0NaEcTiidVD7WPgkz3zTFKlUC7Bfa1K8f17A9FqwMbLL8oXYxuNbRcx_utE6tW3nlV7eotrcZzdMHeCTSqGmvif4y0h-x2j6i9eqL0ICfTgXNEPgcRG2TAg4Wqd0p4KNznDrY8fSSn-E7O7rYVVnzU7jVMGLs01gVlERh5_0om-Av6fA4vZDhWPkfLZqhZS1TOuCSgS8D5DpvSHPWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ درمورد احتمال ترور شدنش به نیویورک پست:
من دستوراتی به ارتش داده‌ام – اگر اتفاقی برای من بیفتد، به سادگی آن‌ها را با شدت و شدتی بمباران خواهد کرد که قبلاً هرگز ندیده‌اند.
من مدت‌هاست در رتبه اول لیست ترورشان قرار دارم و این بخشی از زندگی من است و چیز جدیدی نیست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79914" target="_blank">📅 18:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79913">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هه  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79913" target="_blank">📅 18:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79912">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ریدم کنارک همین الان صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79912" target="_blank">📅 18:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79911">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpFxLEJtGL0K-uO5LkE5QEzmW1uytqFslABCq0yjA17KNnOr7ODPGkkMw7Sutx2FReQHUBLiZjFfeMODJlpfFuV4fDAbSZy6l8jb7zPBNSwKrQcUEP6IiQVBPbdz5in3IkwRafW05QFb2WPWSLtyaRFwLEimSkpy_TQHF3cq28vU60wXecwZ4fYGVm-k5uoJAN8EkTcb5f74hpVMbrtifaZLm4ydp9eFBNdN-M2xI5Ntx6MFrWxwW2EZT-0zq1kvGo6n8TQWsYwIbPa_g_q9y2d7un9brzyt9aUsIXgSae9W5UxBOzBGx080LrQ4I-pqizgoKpYYK7cZJ-EK71nsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79911" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79910">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVlTUlhIPUkrkcK-n1ZPdYonpwIFShGRzrpPnM5i0sz_Fs0E5P8Z4irgPvmkQrD75lgT-8QcIwJCPjCmE45IJnCkiiEGjhr0kA6Y0mQ5vql-RAXY_Qc8k7ow1AqJGM9ljMCovFFdlh6ocHqloQB_-C6IvzafecQn9OXG071IDrvSkR6WZXkNI7HvYRcsFHUGSxDi_phr3ct2ZZlLicxDZn7tMcvHdwsgwsN641mQTiDSyS909DB_SumsoxmJ1EBKGqZIau8u-U94D3L1e1MkHwJA_hKKTOr-WzKkLu75tgVh0SquTwjNVlSgztSfbnF72yGnqkbZFVtIquane5mQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه با همین ترکیب هافبک و خط حمله اش پارسال به اسپانیا باخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79910" target="_blank">📅 18:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79908">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0rJGZSaTcZPXO4fvXPsX4LpYl6GTt_fn2hyXHdnVA19ku2zv8-Zq_VO-g54fU1gde269nLIMS28AHLbkto078gtb4Srpv3ZFkbLMvb7eR1kvp5xAqA5YNrMKhOwhuqfVNp7sewYPICXLC52jGL4XcwmG9U1uLvrtM1M9PsCf80bGad3FVQugGLcopMcSDZ3P4yar2w-m5fTtnEx4IYwPd4xOYAFvGt9G49cqtMHX8wWKQyGk2IifKPT0qHzfDHYHFjayZ15Tk4mHEvZlsoSW7O9BWB-wE313Hk5mb9thxQQDAylRv_sKC6TDsBpGTQBLzMC3ox_OKxnO66ZcwXnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX3mtONa6Bgbd5NHTq6Coxa1-EvMU95qSoPh5OycipYD4JO9z94oLdNUOidvBs8NHa5ORssUvVfWxs_Z5PrQnF1R9cSGJtKATpUui8gLqqr0tOXViUBDms_gA_Yo6dnPaGrS-c0lsH3AGPkjJb9rvAmzujN0eax5jAHqKBpQEFHhVj6ilheqw1IdUkYGxhIaZnNBgPVWi0bVCubfqNoUnsvLrmV2ownvWXlOlj3J_Hh_TsgFnqLhR2MxHezESm45jcOLP0f1lgj-O9T8veM8Sjc3bCe7dUxhDGX3pR4Hr_lOq9YCLIvxz0D6oON1SFrRqY22jDmJ1Rgv55FQkaa2-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داره بامزه میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79908" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79907">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پلی بوی کارتیمون کم بود فقط تو رپفارس</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79907" target="_blank">📅 17:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79906">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اینو کجای دلم بزارم</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79906" target="_blank">📅 17:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79905">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTijay</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79905" target="_blank">📅 17:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79904">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvsGZsKkff2RqQ3QFy1Ge20pigfWh3xkS36V2GkCYK9azhhqr3EHDOSrTuE1-c4JJSpbR1STs6Hr9qAcbJAPbTIF8dFj6dwEH-3zGSVKVtYt6TsiqzYBt3IIoyLaw6MmsfW0McjCAMaJDQxJxJwZ45wbGC3t_eAL1MMFfL8TzDXbNtw364UZ7tOg0jZwdzEtKocRatZ1lnVrsxGZbNOhHAhjwMuT-T7jNQ8zk59HYzt1N1dmRoIn1Lx7LQYvEMb02EzCItqZjsfQSV2C8Dsc7MGu8F5gxCsb-LPqXrByflu6RySziApNd6OrufTqjNBsKTjnLMkX9hO9Q7J4v8K2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار به هیچی ندارم ولی ناموسا چه تحولاتی تو مغز انسان رخ میده که عکس امام حسین رو میگیره دستش باهاش عکس میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79904" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79902">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxlqPGOpwddQVgBj5IS0HdVXNYPX1ObKs5WhIv9skF57WmZicqGWuNfkAaR3PQF8WdbmVokFHeorZcuI6UEtGZBoqWHRKP7A5Lv5vw3_iVixnxAdu-S0AkzkIpShy1u_21_T7S2M6d-_z5Ztyp5vVQtBA_wxTGJaTEIhP1wnW_JXHd1koU-zC435XuaWYYtEnoTM0vc4zQK2fqa2aJokMZ-JDH28umIXETm8mwLbosbjcc-RLX1LACs4366OgvCfd4izEJn9HIEmz6ezZdSFT2QkPPtgwzVRMDNpkEGHxmt985QEN7iiFthn6mZAjGgDO5cx_gijQ_yGZcuLz8oXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0434cdafe2.mp4?token=aHFr8QQVLzK1cBfXLyePzjW3phgToCrYHt-gWI7JIDiow8vrRmRoaIOz-uCleknAtdWZcUZ2HWuE1nXvyd__wzhuHdUZ-rf58yMMzC-_tm8zVgOaqy07yOEEVEydqlUKXm58OYQwd_2aL8EInfuf62jqmyqQgV87k9DSOX3LkvWcovq1CVqxjGSD5M5hkOLT1y68ZIscMPeCaJA0MATTf_B3CrKRDrgNDJcK4bUSvFD7SAQ84WXUa1kUi0mZpeatqR4tUXLiGDtYqk1cn0Xse3Jil8El6YRJB5rVbHSXsxqnjTxMBM17npk2HDCMcxVG-6FH2D6bpfqL-ZN4WjbkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0434cdafe2.mp4?token=aHFr8QQVLzK1cBfXLyePzjW3phgToCrYHt-gWI7JIDiow8vrRmRoaIOz-uCleknAtdWZcUZ2HWuE1nXvyd__wzhuHdUZ-rf58yMMzC-_tm8zVgOaqy07yOEEVEydqlUKXm58OYQwd_2aL8EInfuf62jqmyqQgV87k9DSOX3LkvWcovq1CVqxjGSD5M5hkOLT1y68ZIscMPeCaJA0MATTf_B3CrKRDrgNDJcK4bUSvFD7SAQ84WXUa1kUi0mZpeatqR4tUXLiGDtYqk1cn0Xse3Jil8El6YRJB5rVbHSXsxqnjTxMBM17npk2HDCMcxVG-6FH2D6bpfqL-ZN4WjbkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکی هم اینارو پخش کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79902" target="_blank">📅 17:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79901">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBZpwAsINOJ_DvVD1wh_1YMYxFoFarGCy4E6R9V-DJPGLrGYVDnLHW1F6yi7gREEH7YN9jbeakxNv1zGanyquqbjVmwVdCzjuTmywXZQlVnHBT7kh_y-vMgbHiJJhymUvs78gVFkZnacVwvFeo-1sl4mhsG2oFO_AuSUzbo3x4tGJpbWfMrczhjYbfH9BMEw-HJcOsTWmAUfhf-8GszWnfYFJDpEEyz1yCIcOs2eWi4o8Gd4ZKzYwt2Y2ngxSWrtZWQZaXUN8YQaDKVnNSZxShPqeRxffr-A_i3OrSlnDSfEBFPkxEw1bEKuJhgpH3kJOTuPUhTtZ88oVymbzwirgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی که ویناک از دکی پخش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79901" target="_blank">📅 17:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79900">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkIA0EVJWPANxYp10Ks_Hr7tZ8xvcZEQ5wn5-IV2XNFDyxqMeL_UJbkAAToYwqSNA-1XmsOwEyHE-G7XWIrvKy7eEQWd0PDj_SkzGnli-F1iFNn_3eMSvFKcsIpDhIkGFNadH4R84zMlMi0WcxAgd5LDcGp6TJg0ejNRiI49O_poY8UAUpDZV9XOdy_G2S-T1bZPCJQLUyxfBJz55keY2gsYbOlJ6GA3JusaTv4i8fDnzfQaeSlyx9kzBfBOiCRC8AFOd7E_IyWDhkDU0Kb15fJx1onznjUZeu9ocrOUmNSbp85vbgN19Oc6zPQbrQQPTXrjA1cinV1tfCKlDfPMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاد
👌
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79900" target="_blank">📅 17:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79899">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کباب کوبیده با گوشت گوسفندی نود درصد تخفیف به همراه ارسال رایگان برای گیاهخواران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79899" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79898">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79898" target="_blank">📅 15:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79897">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwxSe78k6GHZnFjp1clwYd1tt0Nzgt_tqjlVGAgOA4DIYkdANqb8azmzwzXapKoSvhBUJkMFC7PPK1w_2aRsXi-bCYO_uF5cklCQl6xsdIWmyGMEF877LArLCFchTjgkam7WfTN6_RX_Qs63dvRMkg8oQqN4kXzPiH_tDEdAunQGffYQu840_Y7zRP6sijTe5crVts06cFI6IoQiNLEaNXFA6QNVWoKL0s-pF6i1RWZ6zrsh9XVL59gY1TfC-RvdnohKjCFBaAayBZKwa-BPhVjiD6bdA72JSy1mu04mAfmLbj_-VHukhGttMYNAovFKA8NhH4Tuw39yEuPdtaghMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79897" target="_blank">📅 15:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79896">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79896" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79895">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my-rJhG8zYTu2hJ8IBa404gwZRHlm5kgA2vH9mmmrxKtO_4s63ZMZONAJXtB7uiirIubBwaTdYSLdvjYdJ1mhCfuc0o1gkrSSE5umWXT6jqqwN_noixwbmt5CW_OAZwNIOFD80aYk79JE5_Y2CdNvy7-7WCS4ZpSqEiOKa5uwp-GaDae9TFoVJNLinfbeL7FeiBFgNNKAqrIdOn1hr485zA_MnZRj6nLOUXr_DXOiIHU1Wc8Cwkz-juNbxh_W6FVhI2URWISTH96YlgrVDkveGQsuha1g6gd0vPUVfBsZcd0Hvjoc3lh850Ue2x2DhZv5S-J0R_xPpcf2Wo3HhtBVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده
کلا دوساعت وقتش مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79895" target="_blank">📅 14:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79894">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79894" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79893">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رنگ شورتشم بگید دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79893" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79892">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یادآوری بدهی هیپهاپولوژیست به ویناک تا زمانی که تسویه کنه، روز اول.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79892" target="_blank">📅 14:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79891">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ولی خداروشکر لا این همه بگایی و دغدغه، نهایی و کنکور ندارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79891" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79890">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بیاید بگید ببینم وضع زندگی و حال روحیتون چطوریه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79890" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79889">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">واقعا بیف شاهکاریه، هم دکی صدفو دیس میکنه هم ویناک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79889" target="_blank">📅 12:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79887">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWMbzC7RS4i1bhmDnhO35Aw5CetNszunZyimoyx4SvHprLTQQ5Tuxw8imJRKtzwPBy0yMbTe-J-LNI9o9DLlnc9cr8IoB0MwdytWwFb9XY0eKNxJQ4FHaFpeTfFZTncP0KHzlgEGvmxCsoAp210aHZ0goDE0ZH7DATQ8NuTcNPbQ_TPlS-CdhZTvwbALMWrHPzxsxsSosqcGCBsb6AZ_2B4S2cXph2I9Rop55rE1ho8E22NjSwPdtxyE1aT0to86N5oSbwC1iz11EngrUuuqMHKZaZ94ty3aH15p8dnALpoDmC9uC_IgTR10qpC6izNCPmndeAfDdlv4Gq-BdADRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5748e213fa.mp4?token=M55XSK5vCM5KGwsUzuvxX4h6n3kT_aYRIyT7dquzuSukGaGWtpfe-89r1BSl6pizpcMLZq1aPU79E7wwjz9V9umo3Rb6o5VtbDGPsFcg61PmpGhZ1Lg4JG431R6HFLAJTLljAninLFBBOV8R5N4ZyCXzzZ-T3U-IsOBrsz7vPwfTIGPJIsnajQwljZk6M-pr0bi_daH-VYmjGGU8z_po76y-tpe8_8PWJaQXlEm37fiWXybsSdV5mNJtXnjyV8bWsel8nOprVQ4whEgR5NasUGHYO7nbxEY9yvVLPTFyAYoRNS3MgPK2CXjs21yzIK5Y4tTzW0VgJGT9CCs9lWfIRL0ctPzg8VInEVGPbatejuJaNJcmq_Qyj7YGWRhEBx2mQP-n4Cdq6SBq7LzxiNvG_OQh_l0TitokjuriWOLSDWBN-L1RgmpskDj7GWF0vpsJUfisMUgg073e0uV0ebeiSlU-FuxEGU7MqFjupoU2bk3_5wNbpxXWzoy8gJcbtpBIQnEAuWTJG_QD92JOERfAbN3TDSUpumi1-DhWIRjRpw-L7s-ROJlR-aOoRPsjGIvmuaETfr05Gj69Ye5HPBw05EoQWxgOjWXWgowkVytDsElcGPYh9NnbYfjpMF_jjHlXCXSJgemYKoW7UTzFoSJMmgihpHbVl66mYkFSaXTZ0L8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5748e213fa.mp4?token=M55XSK5vCM5KGwsUzuvxX4h6n3kT_aYRIyT7dquzuSukGaGWtpfe-89r1BSl6pizpcMLZq1aPU79E7wwjz9V9umo3Rb6o5VtbDGPsFcg61PmpGhZ1Lg4JG431R6HFLAJTLljAninLFBBOV8R5N4ZyCXzzZ-T3U-IsOBrsz7vPwfTIGPJIsnajQwljZk6M-pr0bi_daH-VYmjGGU8z_po76y-tpe8_8PWJaQXlEm37fiWXybsSdV5mNJtXnjyV8bWsel8nOprVQ4whEgR5NasUGHYO7nbxEY9yvVLPTFyAYoRNS3MgPK2CXjs21yzIK5Y4tTzW0VgJGT9CCs9lWfIRL0ctPzg8VInEVGPbatejuJaNJcmq_Qyj7YGWRhEBx2mQP-n4Cdq6SBq7LzxiNvG_OQh_l0TitokjuriWOLSDWBN-L1RgmpskDj7GWF0vpsJUfisMUgg073e0uV0ebeiSlU-FuxEGU7MqFjupoU2bk3_5wNbpxXWzoy8gJcbtpBIQnEAuWTJG_QD92JOERfAbN3TDSUpumi1-DhWIRjRpw-L7s-ROJlR-aOoRPsjGIvmuaETfr05Gj69Ye5HPBw05EoQWxgOjWXWgowkVytDsElcGPYh9NnbYfjpMF_jjHlXCXSJgemYKoW7UTzFoSJMmgihpHbVl66mYkFSaXTZ0L8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من یه سری سوال دارم جدی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79887" target="_blank">📅 12:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79886">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبر بد برای دبیرستانی ها: آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79886" target="_blank">📅 12:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79885">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبر بد برای دبیرستانی ها: آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79885" target="_blank">📅 12:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79884">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یزید این چه کاریه آخه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79884" target="_blank">📅 11:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79883">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db00a79d2.mp4?token=X8gR4yOei1xsPOtVhTIIPxmfXWieTKocjYCCqdKRbG52TfHCGHUArfr-8xWCkObIMkwxdnErreplIbJftegbeMrADPcHKPJZnVicMJvrFdHZJWf-9-th4s5MF3DrgKLoIsUNXeWJQ0fxFJwKf0kfMl6uE8-lHOCUlLMjrzRWz0NArrGspF3iiRVEAVhaL3fBeXPiBGnvey_IOI5uF9E4UmPlulbD3Sx1MvS9gSktyeashY8yAytVdPseaYqwL6PKLGLwUOxna1hbjgA2M9jgEcwIUZ8lVp2KwoqKpdR5aqZAGF2-FjTFTWjZEDJjtj2HO1w_Rb4x4nTfbIpbeweBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db00a79d2.mp4?token=X8gR4yOei1xsPOtVhTIIPxmfXWieTKocjYCCqdKRbG52TfHCGHUArfr-8xWCkObIMkwxdnErreplIbJftegbeMrADPcHKPJZnVicMJvrFdHZJWf-9-th4s5MF3DrgKLoIsUNXeWJQ0fxFJwKf0kfMl6uE8-lHOCUlLMjrzRWz0NArrGspF3iiRVEAVhaL3fBeXPiBGnvey_IOI5uF9E4UmPlulbD3Sx1MvS9gSktyeashY8yAytVdPseaYqwL6PKLGLwUOxna1hbjgA2M9jgEcwIUZ8lVp2KwoqKpdR5aqZAGF2-FjTFTWjZEDJjtj2HO1w_Rb4x4nTfbIpbeweBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یزید این چه کاریه آخه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79883" target="_blank">📅 11:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79882">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امروز 18 تیر سالگرد اعتراضات سال 78 کوی دانشگاه و ماه‌گرد قیام 18 دی ماه هست روح تمام جاویدنامان هر دو اتفاق شاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79882" target="_blank">📅 11:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79881">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گنده گوز اعظم بعد پنج سال برگشته که مکس کونش بزاره.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79881" target="_blank">📅 11:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79880">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ip7dBt39vDQtg2kCUtfWXMvWaN7FSnUD_kvoSsPWxqCSC-CQQz1Xui655W0IlmCPdZ0YJO1b4pjVETdlvheB4AsXOIKlyDI6_lLagwYyb3-zIYJDlY4gzjUTzSzv6aXgk7dVpxvRaSaFB1eY750kxue_13mpXR-NUuDkWXRDurH5bGPfbxgNg7rY6RZcNg62z8KsTipe-Or8dwjspRUC4FW62G92KPESJCQOlz7Yg8qEcnKoAR2NZui4_J6FSB0R0rkx0_5tkF3WGgCX0LRfAW2r5G0GAwCxKErbMHlcyTDFIuKPz2sF6mgUqOqGV77iE6poxQ1al07KchXauTEyZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇧🇪
بلژیک
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
جمعه ساعت ۲۲:۳۰
📍
ورزشگاه اینگلوود (سوفای)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در دور قبل در یک دیدار دراماتیک با نتیجه یک بر صفر پرتغال را شکست داد.
- بلژیک نیز در مرحله قبل آمریکا میزبان را با نتیجه چهار بر یک درهم کوبید.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی فرانسه و مراکش برود.
- با توجه به قدرت هجومی لاروخا و هافبک‌های خلاق این تیم، برد اسپانیا گزینه‌ای مناسب برای پیش‌بینی است.
🧠
هدف سرگرمی است، اگر تغییر کرد، مسیر را عوض کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r19
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79880" target="_blank">📅 11:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79879">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d7f15171e.mp4?token=XwPaN_hHvab4pi5NyIo0hxibmVlaecPKrz-SjgBT_K97j6brOV4BMv469t45ukkxyqaZoidFdD0VDchls_UvJUV4xctKQ1yDiGMBoS6dWOqwZbLI3HpkJg3QJt-7jaVGAgfUIIa7ZT-_nkg95lP9s_Hxba1RyLjuDdeQWo2ZSyumOb1IB4CW6hoU3-GbStYr2A7WOVg2vIdY9vXmTyFPUWKXZM0hwwOICL9MnfrDgqacP7TddkJsCXQbSjaCBr9ILgzSEeiZqLL-ozmbgn6tLisyIRSlynR1vqIdQ8jY9Ag_TcGQOHCfZUQbh9pfv-aGzgm6GVy7FkzQcqtnVMFQYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d7f15171e.mp4?token=XwPaN_hHvab4pi5NyIo0hxibmVlaecPKrz-SjgBT_K97j6brOV4BMv469t45ukkxyqaZoidFdD0VDchls_UvJUV4xctKQ1yDiGMBoS6dWOqwZbLI3HpkJg3QJt-7jaVGAgfUIIa7ZT-_nkg95lP9s_Hxba1RyLjuDdeQWo2ZSyumOb1IB4CW6hoU3-GbStYr2A7WOVg2vIdY9vXmTyFPUWKXZM0hwwOICL9MnfrDgqacP7TddkJsCXQbSjaCBr9ILgzSEeiZqLL-ozmbgn6tLisyIRSlynR1vqIdQ8jY9Ag_TcGQOHCfZUQbh9pfv-aGzgm6GVy7FkzQcqtnVMFQYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 5
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79879" target="_blank">📅 08:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79878">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بعد مرد مومن به صدف چیکار داشتی اینو خود هیپهاپولوژیست تو دو تا ترک دیسش کرده بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79878" target="_blank">📅 03:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79877">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اما اگه بخوام خلاصه دیس ترک رو براتون بنویسم: زنت جنده اس، بدهی داری، فائزه جنده اس، پولمو بده، زنت برام میپیچه، بدهی داری، حصین زنتو گایید، به علی ضیام بدهی داری.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79877" target="_blank">📅 03:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79876">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.  YouTube  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79876" target="_blank">📅 03:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79875">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.  YouTube  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79875" target="_blank">📅 03:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79874">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxNrpAce7jp1xKRwU79eSmXmHMCSqP6Oyky8p6E9GS90NQXuK3UNi6hsy80ZCAXnVNYRU54xn_8TR6x7sqcD5ay8iRHEg2pV2L4joV_Cqji6C6CuXfoKBtPPgqd0DWPU63jK-FvUifB6S0uLRqUzdtgTtH-D8OV52FfefzPiU5X5S-6frKwPG-s4MfE7wDuUF186oBiH1wOhPa1cPqUJqOd-N-xZyzl19Jvn6QeZ-wD6jP7ugILIHpBGwx0GZtd4ugT3E5aK1gk3GP3-F7LcI51vtbYVPvX3nYfa0cm2NZiraZrxo34XpFX9HXTIMZVk8isKOkTo5LbjpBAjeFTbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.
YouTube
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79874" target="_blank">📅 03:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79873">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیس بک ویناک امشب میاد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79873" target="_blank">📅 02:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79872">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فارس اعلام کرد که خامنه ای بعد ۱۳۱ روز و یک تور ایران گردی بالاخره دفن شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/79872" target="_blank">📅 01:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79871">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">البته دمبله زد یجا که یه ذره غم و ناراحتی وجود داشت ولی خب تقریبا از یه سوراخ زدن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79871" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79870">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کصکش یجوری زد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/79870" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79869">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کصکش یجوری زد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/79869" target="_blank">📅 00:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79868">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امباپه میزنه
سوپر گل هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/79868" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79867">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79867" target="_blank">📅 00:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79866">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محمد سامتینگ رفته برا تشیع جنازه تو حرم امام رضا، چند نفر ریختن تو سن با شعار مرگ بر سازشگر بزننش که مامورا باهاشون درگیر شدن، صدا سیما هم چند دقیقه پخش زندشو قطع کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79866" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">محمد سامتینگ رفته برا تشیع جنازه تو حرم امام رضا، چند نفر ریختن تو سن با شعار مرگ بر سازشگر بزننش که مامورا باهاشون درگیر شدن، صدا سیما هم چند دقیقه پخش زندشو قطع کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79865" target="_blank">📅 00:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79864">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مراکش عملا زورش نمیرسه طبیعی هم هست ولی فوتباله و هزار و یک اتفاق غیر منتظره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79864" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یاسین بونو
🔥
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79863" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تعداد حضورم تو جنگا داره از امام علی هم بیشتر میشه کیرم تو خاورمیانه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/79862" target="_blank">📅 23:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79861">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79861" target="_blank">📅 23:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79860">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ریدم حاجی فیروز کریمی تو شبکه جم چیکار داره میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79860" target="_blank">📅 23:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دکی سه دقیقه دیس دادی به ویناک یه کلوم توش نگفتی نمیخوام پولتو بدم کشیدمش بالا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79859" target="_blank">📅 23:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">راستی امشب ایرانو آمریکا نزده، کویت زده</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79857" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79853">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=FbFj9zW1VeeiJHH0cP-IcRm7B2PhAw94ERdOU1Kf5W5gY5jzIFbIt-4TIjuDlAw-rFAwXtmPmipyUEvodTR5d6g2QUiPkN6vRznaPeTukXP1Vq0taVe38uCNK3zgMxOaAay3ElCpCOzLVG6101z7gCkMbubcbcN3V0qHM3ye7-m61z38hXo4sVG6V8o4fi9iwJApapAOWerpbVm0k9bERSJFxaVtiUACQsx3DELAWeSDiKMfGU6qXXZH-ztEaQxiylF9SsZJp0ph76ph5Vo_TEfSgAdAUIPcrjKgyxmgiNMyxMI4lFNA18L1n3oxyXwnDZSdfVYKGk-_CqHrX3MDwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940935d4b2.mp4?token=FbFj9zW1VeeiJHH0cP-IcRm7B2PhAw94ERdOU1Kf5W5gY5jzIFbIt-4TIjuDlAw-rFAwXtmPmipyUEvodTR5d6g2QUiPkN6vRznaPeTukXP1Vq0taVe38uCNK3zgMxOaAay3ElCpCOzLVG6101z7gCkMbubcbcN3V0qHM3ye7-m61z38hXo4sVG6V8o4fi9iwJApapAOWerpbVm0k9bERSJFxaVtiUACQsx3DELAWeSDiKMfGU6qXXZH-ztEaQxiylF9SsZJp0ph76ph5Vo_TEfSgAdAUIPcrjKgyxmgiNMyxMI4lFNA18L1n3oxyXwnDZSdfVYKGk-_CqHrX3MDwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79853" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79852">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79852" target="_blank">📅 22:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79851">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حالا کی قراره ویناکو بگیره
هیشکی بک نمیداد بهش هفته ای یه دیس میداد الان که هیچی دیگه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79851" target="_blank">📅 22:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79850">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیس بک دکی به دلو از این دیس بکش بهتر بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79850" target="_blank">📅 22:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79849">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دکی به لیتو: خانومت خوشگله بزی لی تبریک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79849" target="_blank">📅 22:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79848">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79848" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79847">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اینو نمیداد سنگین تر بود</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79847" target="_blank">📅 21:56 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
