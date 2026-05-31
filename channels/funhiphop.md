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
<img src="https://cdn4.telesco.pe/file/oQliOaVH3QWR7vIbC25hx1AG6kcpCeBd15yOL1bYOaoyeVQdj24c7-TyLDpqHLruRgubFs5QlEg9ctvQLiIUE2Ey1YXw8GoszGTD536fnTtKece8cnKA3jbeA8dzxaDTffRx8uePGCaoDPLlCibfHDqXe7HFwx3oJGWaN9jZ4Zdu02t8tk349VaNsxlXpYZSehqYHEXu7bqasN8xlCPUwmcFP3_4Bp6OlkunXULNy_hB6OL2BhI_uWM56VU2lLxV3yGA3OHFmPFXHXCo2Qxjx-V5kSqphFAZHT4L4Es4XXVFEulScytPsnJidLvr9mOeXKKPRMMouBu0-NDEsw2T3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 178K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 22:11:35</div>
<hr>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/funhiphop/76497" target="_blank">📅 22:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYOy2JzNMLG5gtvwIWYE-pgu9NGx2OmX8YB5ZJb4Vw5Tq63ViAsRG0ZR7QUxgjsZnmSJ0YmY9JZElz0bEzrr3DhhD-nI53ozaKyjSGe3WCo1WE9EIOnmSgeJKs7sOMej_TUIy8KpXGRikirC-a5aumZSk65OhZ6GeMcgjZjgiAjE2-hW0Df-FVLdEKhTPoC-ZtjFNcVDiZrtkh3asnsoBPScacuuWb7nB8LoZcbN_5mgpOcZcvZeiSuQXOxn8kyiRHQ_RY2MiluT8L-LZOFWVYTijPuCeqQDmqDNMBmBakVwQC1k9PxuhiJB1PNkGJl-tBPI5SGG9Aqzn9dGFgpFmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/funhiphop/76495" target="_blank">📅 21:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آخه فکور (منیجر پوری) گوز کدوم کونه دارید استوریای دوماه پیششو پوشش میدید، خود پوری هم به کیر کسی نیست دیگه</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/funhiphop/76494" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پزشکیان زیر نامه نوشته
من نه استخر میرم نه با هلیکوپتر جایی میرم</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/76491" target="_blank">📅 21:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8R_0G5tjmvifB0pG8o_QqJpYYFOekITCiLcJbJDddT4JwK9naMKl1SRrpeOxjQWul0C-wvH_owpzlMerEauD692PdZ36zXFujhkdjqD8dsebB5FGER5fR3g2eHE0oAT1R4aAVNiIEqxUnJFpeEXXDel4Z9-iS8JxBWXcMvU8gzDvsDwtLpPvNvxZY5CKCM3hm57b0PrLD38OtlIS3fwVqi5xaWShGWFOdOh0Ae-SHNC80S8x4NsuxabXyNRTghLhk0v2L67PKSsa4BL2AyHD29F1ztdSx0IxkqlUi80WcMcZchh9qhSyVcG_9hArODhLKWzew1-ZBZTHjzGtg0sSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفا نامه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/funhiphop/76490" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فرض کن امشب هم قالیباف هم پزشکیان هم مجتبی ترور بشن
روحانی بیاد روکار هم رهبر هم رییس جمهور
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/76489" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop | ALI</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/76488" target="_blank">📅 21:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76486">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الان مثلا خیلی شفاف باقرشاه داره میره تو کونمون</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/76486" target="_blank">📅 21:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قبلا پشت پرده یچیو میکردن تو کونمون، الان جلو پرده میکشن پایین میکنن تو</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/76485" target="_blank">📅 21:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرگزاری بسیار معتبر تسنیم استعفای پزشکیان رو تکذیب کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/76483" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">در جریانید اگه مسعود استعفا بده نت قطع میشه و کانفیگ رو میکنم گیگی ۲ میلیون؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/funhiphop/76482" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/76480" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نمی‌دونن تا گودال ماریانا هم بگردن پیدا نمیکنن رهبرمونو  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/76479" target="_blank">📅 20:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بعید نیست این یه تله تروریستی باشه تا محل رهبر لو بره  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/76478" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/76477" target="_blank">📅 20:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مجاهدین خلق از 021کید به جرم تهدید به شلیک گلوله شکایت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/76476" target="_blank">📅 20:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76475" target="_blank">📅 20:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKPc7gONCjxgGXotiTKddOXDDFhj1cO2Ho3fT5ZlsZTsOl8x0Zq_n-Egme0mTK13S5CgKjExJu29x9z1FHTAfINn_Q5s8NktRrITgo2oY9Rnyhod97QmzYfo7aUIVb1CIbBWmhv0W-EbfEejWD42hEAJnoDWMEkUBupyktQrhkoIQZsQRA_5HHRvhS8J_BBHJQgzEeWx7PyH8LI_mRuoZJA9Dz7HcMe_PE0JEghF50lNbbZNULjkGUa91zDvwEUYH3BEPl9xWLkUJDXEHACpt8WDmXABT_KAfMPM-TGr2i09h3J7xl9Q-6TcgVIcr_fQyeTV2pm8gRco_-QGZ3coxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76474" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76473">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مسعودو تو یارکشی فوتبال آخر نفر انتخاب میکردن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/76473" target="_blank">📅 20:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76472">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حاجی دوران پزشکیان یادش بخیر بمولا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76472" target="_blank">📅 20:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال:
مسعود پزشکیان استعفا داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76471" target="_blank">📅 20:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">برنامه واشقانی توقیف شد
😂
😂
😂
خایمال تیر خورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76470" target="_blank">📅 20:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76469">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76469" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76468">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حسن و حسین امیری، دوقلوهای ۲۰ ساله، توسط دادگاه انقلاب تهران به اتهام جاسوسی برای اسرائیل به اعدام محکوم شده‌اند.
آن‌ها پس از بازرسی گوشی‌هایشان در یک ایست بازرسی دستگیر شدند و مشاهده تصاویری از ساختمان‌های آسیب‌دیده مبنای اتهام قرار گرفته است. هر دو در زندان قزلحصار کرج، به صورت جداگانه و بدون حق ملاقات با یکدیگر، نگهداری می‌شوند. نکته قابل توجه اینکه این دو برادر از کودکی در مراکز بهزیستی بزرگ شده‌اند و هیچ خانواده‌ای برای پیگیری پرونده‌شان ندارند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76468" target="_blank">📅 19:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76467">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhvvbRoJMGt7cneviRvo813nuyXGNdE8sy1N2iLbVkWB0Y4i8YCn1GLQhP8_pw6FkZ3d9fzsAnycZmvvI8rXRw7yWEiroBpU2VhU2UvGmPLutbc-F_pz9VaBAkim2k9fcG_tF-DmN_VMyWxsopW197IOJDUhYpjAJx-iYgzTyvZ0cqB3T_csH-z8IsHd2fMlyhf1FHKfnn5u-s3IHpOysqYyAXZL0bZEnWwVWJEyPl0t_2y6FNx5nckNIojeNh11Gzyknk9ghEVWJwDYAshezqLRMQFd3jegKqaejBRN5YOiA8UkhshKH-qjzph3SNv4yEGKmoaLhD9D3rTt77zoOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوآ لیپا و کالوم ترنر ازدواج کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76467" target="_blank">📅 19:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76466">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSeniorVpn</strong></div>
<div class="tg-text">😕
بهترین ارائه دهنده فیلترشکن
𝙑2𝙧𝙖𝙮𝙉𝙂
😀
آیپی ثابت ، مناسب ترید و وبگردی  (اینستاگرام - یوتیوب و....)
🛡
مولتی لوکیشن
🇺🇸
🇩🇪
🇨🇭
🇳🇱
✨
سویس آلمان امریکا هلند
✨
😀
| بالاترین سرعت روی تمامی اپراتور ها
☄️
تعرفه سرویس حجمی یک ماهه :
😀
50 گیگ   | سه کاربره         ⇐ 500 تومان
💭
70 گیگ   | سه کاربره         ⇐ 700 تومان
🔄
100 گیگ | چهار کاربره       ⇐ 950 تومان
🥇
150 گیگ | کاربر نامحدود  ⇐ 1,400 تومان
😀
تعرفه سرویس‌های بدون محدودیت زمانی( Lifetime ):
🥶
50 گیگ | کاربر نامحدود  ⇐ 800 تومان
🔵
100 گیگ | کاربر نامحدود  ⇐ 1,400 تومان
💢
💢
ارائه خدمات پنل ویژه همکار انجام می شود.
😀
خرید از طریق پشتیبانی :
✅
@VpnSenior_admin</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/76466" target="_blank">📅 18:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76465">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فایل صوتی وسط بازی عادلو رو فیلم گلدون گذاشتم خارکسه به اونم خورد و غمگین شد ویدیو
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/76465" target="_blank">📅 18:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76464">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شی سی‌د شی وز پرشین استارتد
اسپیکن فارسی و کیرخر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/76464" target="_blank">📅 18:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76463">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuk_d7I5FxwDPiADLzWHplfP-ytBtPSgEjXSltzx3VftGduWQk1aIholrHs7W2tY86fF-EowmVRJb3bdS-Afo9JrKM4K0NX9uqGVDhgVeuOE-WxuVkm0ex2SBXAGVvEjiHDi85XRzJKYUvuEFLsyxUN0v5mh7h-MCmh4PXX7at7t9gMipSA1PTmiKdEEK1mP3yVzKkUS4Fp9f6wWeA4hr7pfPS3GwW1Xt3GtPEsQ0hEqRwQLfkDPBQCJ-OUyeHn1_TV70kPcH_PsxdJhxWfHpYeD8z2tH23Du_etCFRoPoCuVTvthzefrY6DKeXGdVuaO0hoNyMP_8JUjZzj2cR6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف غلامی مادر میثاقی رو کرد تو چرخ گوشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76463" target="_blank">📅 18:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76462">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZN-8fRYjoc9MStz56hHcfaVkkAWtAozZMqH5UaI2CMbI0NQz-_aEX9cJr_OpvieRR3L7zoA__x6gaFhtn9vPHbg3Jd3izHZp9GkWP-hBSUo60LyyvLKd7PnJe0ZLWRmhryAGa5ifqYRSIJOQj3lwZh9qXu1WCZGscb-K0OikCTfM2J-JgBN7CGQv3eu5XM78cycoYPXTCq9lsEROI1RQMWcOLoT-YUPYPsE4EYz4ul6xobQuc1qc_dr6cOa9jHgPBImp3EogJPJMBC5VxD5BBaxwy4pHBv2G1iNNKgHlOHzYoQD7h2kLRx7ABpUf0kcYKMDD3ND2OxcuqNOWkqGTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالق مینیون‌ها فاش کرده که همه مینیون‌های تو انیمیشن مرد هستن، چون نمیتونست تصور کنه زنا اینقد احمق و نادون باشن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/76462" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76461">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vukHHkNf8N1jt7BLeg70cu46sZYlkpTeICeU2lRbqb3K14xGhVGhiK8YmmOwe9ZrZDdwlN3mo1KyeL9S0JBOPCadcRX-xGTfEu4db_gqdBmZGpawGIxyOEE4BYe-jDmLXgwTOgLwk7WDRApgF_z_lEwpgWF_-sT9jATOL_ab8sfel0oCqRdxDgLoZHfoL3JFmhjyWOrzfbp_-qc7OzmpQQpJdrlOZP3LqLd0vrwioOVpK_bqZKW2v15-9EFWNYTx64-EkLajiY9HFGYkVT4qrkJnd9a-Y7bZonIgMXm-NRmgGc4O9PT1gAZGJC-fA2giATYOT7ju8FnHT1IXResSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g10
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76461" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نیرو انتظامی تهران یه کافه ای که توش اسلیپنات پلی میکردن و پلمپ کرد و گفت: اینا شیطان پرستن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76459" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76458" target="_blank">📅 15:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76457">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چیه دوستان
میگم خبر مهم فکر میکنید روبیو بهم پیام داده از پلن های ترامپ گفته؟</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76457" target="_blank">📅 15:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تلخون از لیبل سابقش جدا شده‌.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76456" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبر مهم رسید دستم</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76455" target="_blank">📅 15:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امین منیجر یه دوتام به پوری بزن بلکه سفید شه برا چهارنفر
@FunHipHop
|  Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76454" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام های شما در چند دقیقه گذشته:
فرید جان سلام من بندرعباسم اینجا صدای انفجار میاد
درود فرید جان ما قشمیم اینجا چند بار صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76453" target="_blank">📅 14:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGT0C1cbWYBHh0Lu9TjuIw4R4vifSnyxIa3lMoaznsOeyADLegoDPCLYcGjzShY2V1ryjZ4dFC3g7-RiZ_Dc_2wVK62kK-sYyuLHmCFWFj6lRgz-92kAls_eI5DOUrf3_VAaxOXrBilObSZ34gXbSHFqPjTG_1CeFQZaclmMH42Prf2QjvUrVHTk24qlGSesclIOBHHWojIwaJia6I4a5R8WDjiS7SnxKSwA3St4FmdjBiUBScunq4cdlUAJMEMBY07uAK4ukACt2bzZE1DI39dab2O2pwbbYZ50VyOMzPGu0v0U-5p1J_t2hbs8eTXHnrWhj2hyKV6QKy8ViTYXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحث کالچره پسر
عکس خمینی میفته رو ماه
عکس اینا میفته رو گوشت
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76452" target="_blank">📅 14:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آقای باهنر یجای ثابت وایسید از رو موتور پیاده شید صداتون نمیاد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76451" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الان رسایی دوربین رو تنظیم کرده رو صورتش فقط عمامه گذاشته
نه لباس تنشه نه شلوار
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76450" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امروز مجلس مجازی بود  @funhiphop | reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76448" target="_blank">📅 13:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">امروز مجلس مجازی بود
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76447" target="_blank">📅 13:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76446">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزارت قطع ارتباطات دست به ماشه هست
ترامپ بگوزه نت رو باز قطع میکنن
کار مهمی دارید انجام بدید این روزا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76446" target="_blank">📅 13:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یکم دیگه اعلام نهایی توافق و مذاکره طول بکشه از لبنان فقط اسم "سیب لبنانی" تو میوه فروشی های ایران باقی میمونه.
اسرائیل امروز لبنانو شخم زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76445" target="_blank">📅 12:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مردی براي همسرش پیام داد   عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76444" target="_blank">📅 12:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">مردی براي همسرش پیام داد
عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده
زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76443" target="_blank">📅 12:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مطهرنیا:
واشنگتن به دنبال مدیریت ایران در دل یک نظم امنیتی و اقتصادی جدید است برای همین حذف کامل رژیم در دستور کار نیست
میفهمم چی میگیا ولی متوجه نمیشم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76442" target="_blank">📅 11:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76441" target="_blank">📅 10:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خاتمی جلو عادل اصول گراست
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76440" target="_blank">📅 10:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آکسیوس: ترامپ همچنان به خطوط قرمز خود پایبند است و تاکید داره که هیچ توافقی با ایران امضا نمیشه مگه اینکه ایران تضمین مشخصی برای عدم دستیابی به جنگ افزار هسته ای بده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76439" target="_blank">📅 10:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=agh1jYB5NBG7-NJXVrJ16oF0ZhxmXIMYZmWYT4anjNJm0yY4hwWV5cNlal-70S4bZ7ZrLaenwyok_WrDhMOLF891QEZzXmePf1eEdzFOwjMSdaI2tcbGbZSIYsHFPWtzvdgaB-fIDgHo2_caWvO89bcZtlafVeDT0pPzgO-HLMnwxawhuVMARJd9yJ9cVP2XuehPhjOizE4WUegvgNEbjDQcb_iroYIqHEaoBAewH4CM_mx0uHpe5P_MJaPGFGs3ZUSze3G2ETx_BfVQlxDAUTyje4ct3x8j-mrW27Tm6G10rg91G31HaNV4TVJfHqnsnG450UqEBi65SXn0a6uSuGizDFVwuX1K4GFayt4r9TSNSAfS2sS9RD1DLnDSFbSSkdU1Fj0-uO3KB1U0n-VVFV0ikakJ8NLQKiHBdxvxVowJbwnGQ1huZkhtaOaJQfSByIhPsCHiSMuZhdZRO5s0abZqyIl2WVFkksuL4muu5ZUXvjXttDaJ6Wj2J9T1UfLhVHa6V2wmOTOdb5ZgdE5bFiTujQUagQ9pJvCCr9DpcrVRHQjB46GuSXShwqNlBCJlXGy6RsYchs1w37wR3fU_n6ECtYXF7cdRxcETDYAdeZv6AfkS4-YdUKWIJ2fuKriZYljQQ3qEEOVgC2EGbOmob6Jxdvf0j6zLjlirvr0r-o0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d2dea055.mp4?token=agh1jYB5NBG7-NJXVrJ16oF0ZhxmXIMYZmWYT4anjNJm0yY4hwWV5cNlal-70S4bZ7ZrLaenwyok_WrDhMOLF891QEZzXmePf1eEdzFOwjMSdaI2tcbGbZSIYsHFPWtzvdgaB-fIDgHo2_caWvO89bcZtlafVeDT0pPzgO-HLMnwxawhuVMARJd9yJ9cVP2XuehPhjOizE4WUegvgNEbjDQcb_iroYIqHEaoBAewH4CM_mx0uHpe5P_MJaPGFGs3ZUSze3G2ETx_BfVQlxDAUTyje4ct3x8j-mrW27Tm6G10rg91G31HaNV4TVJfHqnsnG450UqEBi65SXn0a6uSuGizDFVwuX1K4GFayt4r9TSNSAfS2sS9RD1DLnDSFbSSkdU1Fj0-uO3KB1U0n-VVFV0ikakJ8NLQKiHBdxvxVowJbwnGQ1huZkhtaOaJQfSByIhPsCHiSMuZhdZRO5s0abZqyIl2WVFkksuL4muu5ZUXvjXttDaJ6Wj2J9T1UfLhVHa6V2wmOTOdb5ZgdE5bFiTujQUagQ9pJvCCr9DpcrVRHQjB46GuSXShwqNlBCJlXGy6RsYchs1w37wR3fU_n6ECtYXF7cdRxcETDYAdeZv6AfkS4-YdUKWIJ2fuKriZYljQQ3qEEOVgC2EGbOmob6Jxdvf0j6zLjlirvr0r-o0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی زرنگی عادل جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76438" target="_blank">📅 09:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW5VvTbqyUk24B8bZ48JcmYomidYpgJarW_t1gQ6-v6hzwtpT5JV0BODMpgQeuUiNnzYtwS5ga7RxeuO-REsksgILjaflVqlqTc1czMHOQt21NyhhPUbK62lEnmOmV3Qa2KoJhd0YT2Ejbrenbjb7pKElXnTUQ1k9TJV2D3VDQ6gLRU-jiEJnlBD4oqgEt7Jd5DaHMGUgS3LGwO1VBduASIMwBupEP1vNCphg-cdjgu9vwysXZofy9iig1ofiy1rQiEpE3DN-VSC_WzqAGjDvUk-QXnubx3wUf4I37Bpt5REozxoSZFOApD9o7SZmjdEAf6XF3eqzknzpa1kNQezJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صب وسط بسکتبال داشتن همو میکردن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76437" target="_blank">📅 09:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN7Rtt8-UPEgvsUogCgNoE9imJYHZt0W6rgnTjG45PR0XM8ASvEmTgHjDOMNW313jmIxWYFLivdxeh54qHNXrQ5XaJXCZrmHKFEsdSqt_UcRyH4vvh2qXR7c-UcnpdKuGoX5y-iUcqYPk7Kg9hOPNLwiiY7kOyY1CF_g6cbuZxZ7XXHGm5QElQjIsD3a3Fj1mOaKHoYSynech2POMKktplaoYboYqGGcja8tgA0Pjm7pZ8sYKvUXkkTqDrALww9-9hw7fz1f_IGkMN5s5W8g4PqCv2K2BpxQvUGbPy3aRpX31NknpdXBx-yTIPx0gsAovJcvpErvai-foQHyWDVVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=EpGwyJcfpiX8A6UXPnSrZYEYJq9Y_xQWftqjkmw6gRzvHhdbLjZO566TxOcgNzSl0vuZdMxibPxrl-Pvk5-SVMCyQZGPgvJVzrQshlDC_NXpZN-7Tf8p0E7WJMCOsfodkGX_AiNZALRF84eaz63IGXEvofgbJ6uNdnqaU7fGqiXa0kcAmY3L_pzuZL1v8HFtFSmBrztEE3xPjgYB22jjJrsZBhtVbz5BADeuA6XLSmzsTeWvIBxG4kL_X7fQZRThESiZCOqrWMapaVqWgn_H4Tl9-XZyNWn0jch7EVF0qu1cuFf2x8YMxj2iQe8SwTMu5DJaaJpm46xUDwUTcz1XJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce07890ba.mp4?token=EpGwyJcfpiX8A6UXPnSrZYEYJq9Y_xQWftqjkmw6gRzvHhdbLjZO566TxOcgNzSl0vuZdMxibPxrl-Pvk5-SVMCyQZGPgvJVzrQshlDC_NXpZN-7Tf8p0E7WJMCOsfodkGX_AiNZALRF84eaz63IGXEvofgbJ6uNdnqaU7fGqiXa0kcAmY3L_pzuZL1v8HFtFSmBrztEE3xPjgYB22jjJrsZBhtVbz5BADeuA6XLSmzsTeWvIBxG4kL_X7fQZRThESiZCOqrWMapaVqWgn_H4Tl9-XZyNWn0jch7EVF0qu1cuFf2x8YMxj2iQe8SwTMu5DJaaJpm46xUDwUTcz1XJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو پادکست جدید بنی بلانکو ، بنی جلوی سلناگومز میگه که از نظرش زیباترین سلبریتی زن دنیا سلنا نیست و مارگو رابی رو خوشگل‌ترین می‌دونه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76435" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76434" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76434" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5-GFwId2_uCh7HWlKl1b2JUFG5PY7sMB5AhqDYdNX86ClznlyFb5FQX6Mg_m21dFTZRvdBiLWo4PHx9tv4MTTAfIC_TAQJVyVOk381jN2A7WQPeS8AUYzDWAHXF3tjWtR0YkdNUjfrZEAfsb_nGqnmh_X_3-vcwC_xcNAQlQvs6oWA_4KGL5X98frHDYdosXAKIClB4_16yEmbbVBI4_OmtTTaJUXaegdL4WuepxKY43OziQmYWdApsCi5oyjvcG_Dadz4b_-Z5EmvnuN_06oPsJIuzXN6-ULiT48Q8YTrBeX4M8IXpzA6PduBBvOIgYiJ5JznMBoM3CV1LiKLa0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r10
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76433" target="_blank">📅 08:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ به «فاکس نیوز» درباره ارتش ایران: «ما آن را بی‌سروصدا رها کردیم، زیرا فکر می‌کنیم ارتش آنها تا حدودی میانه‌رو است. آنها افراد دیگری دارند که میانه‌رو نیستند و ما به هر حال از آنها مراقبت کردیم. ما انواع مختلف رهبری را حذف کردیم، اما اساساً ارتش آنها را بی‌سروصدا رها کردیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76432" target="_blank">📅 08:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmAZnJbk0Qlbg4Q7Lls33Zvs48eJInVH4LeV2ALCafR6md_akHAgfKY039faYYiHCutRigRu-B-5vsjjY6tOjvkkG01FtQuUhdWz92S1oQhF59iuc8IaKF6vur-D0tdI8ccc8pYBuftJSoN5tVEXmB6BGgRPBHfvd-kW7J5_kBfI0cBEWA4DGAAyBmjozkDLO0NOHzMvkZycGUsY9cnyuNYht5xqKPIQNzskIqa22-QvluMH2bF4lTwa9G8ZLeNfjjXLIEDsevyT0d8xZikS0ojGmuNZOzYr8UeUwvyR8Przq3G58Qz11OcA-ZQrEkVUAcYnuuV-QwpLQ6nrIzZ2lq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2028de58a.mp4?token=F7P-ID0aFrRV-X7UJRXnCGuCK598STYkCv7MDqQ1cFAMqi3gdxSrawb6iBuz61ggO1hBJH7yWlRe1ANNfGAuGSxMMAWAy9Mia6zVhTvx41jAA_aVLepIdUixxUgwyaf5tiC1wo3R6Y3OQhLWv0d1Y4kDZchL97MpdET1hn4Qa-tjoxL9rJ1oNS0Gw9LNx6Dsb2XpUtCf-WhOmzbnhIIINK3YcMyclNY-6c9TP2ovrjf2iQ8Q794j22FuqsFEbEaJ4WnHqoXxfhjVyc6kM58ejoEZh93oPGAW236MekfnvAk1O33kapHnYBAgU5xwo2rcuhGmOuqJTi2Q3rdctQvQbmAZnJbk0Qlbg4Q7Lls33Zvs48eJInVH4LeV2ALCafR6md_akHAgfKY039faYYiHCutRigRu-B-5vsjjY6tOjvkkG01FtQuUhdWz92S1oQhF59iuc8IaKF6vur-D0tdI8ccc8pYBuftJSoN5tVEXmB6BGgRPBHfvd-kW7J5_kBfI0cBEWA4DGAAyBmjozkDLO0NOHzMvkZycGUsY9cnyuNYht5xqKPIQNzskIqa22-QvluMH2bF4lTwa9G8ZLeNfjjXLIEDsevyT0d8xZikS0ojGmuNZOzYr8UeUwvyR8Przq3G58Qz11OcA-ZQrEkVUAcYnuuV-QwpLQ6nrIzZ2lq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باز خداروشکر فینال رو بردن میباختن چیکار میکردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76431" target="_blank">📅 08:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">MFGA
دیروز تو فرانسه مردم دست به اعتراضات زدن و  با پلیس درگیر شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76430" target="_blank">📅 08:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">داداشم ومبی ضرر دیشبو شست برد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76429" target="_blank">📅 06:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOmxIMy4isFdWAZrEIxfnVhLO7YdFk05epD5wbK9pskUHvvc6KJs4pnjvoiQ10OdfXtRP7aAocZWsOlsxCLlledRXaUC7dpSuIiDG8cRgKK6VOmetpyr0H678Gc3Mxw0THEuMKo5BtrYCw-UWBMn8eVX3kmF0eqaWazZNJeVCLOTn_2HYFz-sOTYkKCH8S0Tv6uC_4XSyd8L1ZR95UQz-1wdLOQCI4uDcK4xjcPz5In3gMUx2wpf85kR1joQCaNaSs4CW6H6pVy_88Y9vDjpalYfesxc_smyQyryFJ4RDrjabKeVRh8da7AWDR1gehHtrhRz_Kx9yhc5xC9qBcOahg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب با پست کردن یه عکس از جنگنده‌ها و ناوهای آمریکایی:
شما درحال سردرگم شدن هستید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76428" target="_blank">📅 02:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2SXQaC-SA6GKt6UJg13ezKn1Ued9Y2tlGnT2zdtcqoluhPzMnMzWSU_nL0xgVJff0jWup7fWJ5FiTd0nJuUyzQ9j0QaEyBE1fRJMiM1ztN-xAjulfstVRyn80xpfbIB5FxrK5N9lkuv7bRE0oYtmwS2Kf7vPh6kuttQxhVvyIl9oHyy4rG8pb_J2SfjVBkV3TJ2d8Squ5wGFKdQHMrETqWNUcdwJa-Lolj3XWfBrI2Y52viGPLEzCLx3JbVY4SpJiqzDe0lReM_pOHr4H6QFHQOD7yZ4bbK9TbEjw50r0Zu54OFnlpTdiSDUryax8aBcF916c_7PVwqZ_UfBmTyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد خشن حمایت نکن آرتا، بهشون رحم کن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76426" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zuq3BB8hmg7_bUE4jTslbPEhA5WDd7BBj02yaCONjKuLU6zcltrMGfM-FixpqxnWjfL_J3h1GGfUhPWJbEJ7WYNLqcGlIUyzGFBA18pgcs_zUje6FY1PukLvEXdw2SrAr0VadI2xJc_-54wV_VUO2dE9l8nau9E-bCY0c6G29ZI3n71OVtB6Jvjn4WulGCjnhLRC89g-WVzW2I441h-1vy_7p7LM3U1lUQ8dV2aFGrkKFARjqfG-rffFyU_BFNbxxopeuOxGEyIwD0cvFhVp12_cVwDqKGjyA8v6L8Y3pV2YNymQz-wDOaMoZYDiJyTdc2omrHByAwADBlWaJcEVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم با کپشن سه تا تیم نجس تو یه قاب بزارم یادم رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76425" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اینم توضیحات منیجر ویناک راجب حرفای امین منیجر
خلاصش اینه که برا ویناک پرونده سازی کردن ازش باج گرفتن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76424" target="_blank">📅 23:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMY6f_SRYUuL6EXNpHJDkrPiqXbPOioiTiu-CBboRA6gGB--3dJewKH-_PXBlmZVf6HInHkUaS47hMAzmKjkBKLQIbn6UtDp35xZwKoLsAGUTRbpbsf96Vz2TXlEK0_P2w28G3B7GgSmEoESp3guk_SPc60CaC0y7PdzhPGvJF3if8gvnpRSd0QNSHE4Yi7f0p6E_ruMOWRw8n6Bspnmml_BlZsl22dlPIdr3vqwb6yjiWn0jTAStwutGTr7kw_DWF6Q43uN6SIyU6F_-uBhFEInr7rnvd474S9VimgFEGxPZEAuvy26d_zlJzEIjYkJgTBp4PCx51PqeRg0TKXmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76423" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W16PKEcpUvk7JGTiMlgvLryZ0B7x2hat3Gxc6DbRjjNWMkHw-MP2TepdOHmIy0vpqZNY-LL7T-WAAXxA0kXmpOGl6DS1kLUXtbewXAk8mxbmCIVT8d-jvkqH0QCldBi7oNwXaCMZn-FrLhcJknzd6ExyhdT8w9oTRYdK80Pov-sXlGiucPTcKxjXlB5MUb1TetPoeyCFo8pX-R8_BfZBN_JRTP7GDKSMXCR8fnK9e3YrJ5jaVmU6gXDa8ga6sF-iiyx_RDHn4RAZpnbyOcPEwI-pXCu1DhoaFZtDCWQhlsGOkp_7qv8yj2tiIklug2SQt01hPbR5NGS5_fajKo5cKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام آرسنال قهرمان شددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76422" target="_blank">📅 23:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSNGMZI3OzWjR6CS-zv3uZHDbRsR7C9sxF0Rk3Ao4CMBacca0tXZbaIKNGotlGJeaIkpSR1ySDguZof-4d_3Ep9YOKM-p0SdoKokvM5_mQEsdrACON-wpquz8QXcSgR7jCnNq6g4ec-Sldep4QMFQrD4YbEW1Ib5cAMAVBN3xr1ytPlUjg3RzQ6owAQo2d-zs7IRHyDlT5NwxXzMnOQvXw8ivWsAx86kAS2Zn2blVjwQHjyFd2yaVLz1eso75ag7fd2Msz5M95Y2_GbrJpD_yGVZ9SZt4igKSyvZaMm15sPxSV-vNE0RkLAJw4mYList8HoF7pw6NNSZy4TMj-TLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم اینجا کیرخرم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76421" target="_blank">📅 23:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :   https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76420" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9FjsaMnW9e42nYH-m0TXI2QBPkaQOMPGgXsTbk9aA0ePL9PoDL8cCQnBA6iisWitQvz6QfaTK-r6PUYYJ1kn9p200Q1uH1MsXm3IMGphgLVK20lPt4G2RY8S3FBqvIsoGz6EnuGr6OesHeNODmTc4fxfCt6ks0q6cZir3qLLVawfaShgq7W_1LVYxNGX8bcbh1GnL-27pmHXdtTf_5LJduLjpe8My_g7lwOzq8cIfJmSiSK2gkLTykEgZstiJJKFZ8nWSAkvI3jN_Gyt4qSeW2IHltLBhai17zM24x63JSxCQQQhEik-a8mhEp21G6_wynBhact60ydyysEr4rrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه من همین الان با یه اکانت رندوم یه همچین چیزی با عکس خودم پست کنم زیر ۲۴ ساعت اکانتمو می‌بندن و میان میبرنم تیمارستان می‌بندنم به تخت
ولی این کصکش چون رئیس جمهور آمریکاست همه می‌گن پشمام دیدی چی گفت پسر
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76419" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLYj4xCKNDsTNCpVZ4qLD7xJVaam1PToBa5D-v-sREOxN6mcubAL5LTXPJa0TWlOMvbx1SjAEAd7ajyqUHKNljf5HHcj87vQQfsKZUDlX4JsjwPWrkiWjwyqQ8p3LXeFhZJDVKMKt1cKY18AvfUhKIoU2OwvHBQ4-iXuHEpcNi4vkOv_w-yQCSInAOk7o9Z_sloxNxFT0jr_TsMHIruR3kpbKGvnKnAcZebDsf2Yl4L36hbJlfdJD-IRoaBfL7Pn1OWxIJaehA_4y5bXbUIrn_vp67Tr7-R91hLTsRBQpZJzL4gn4OfjCbKNjsGQJkmChaxgOwvZ2KzrJgIKK1TMJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :
https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76418" target="_blank">📅 22:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">با این نتایج انریکه چندسالم نتیجه نگیره ناصر بهش دست نمیزنه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76417" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اما امباپه عجب آدم بدبختیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76416" target="_blank">📅 22:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihKF-_H_-s5En1WJZq-o6Ru3S1LWblTVeTRmwkjCEUaZvgKXDm_GynypOGfnyR9SfKklAC8-lc6aEVcaJ0xhY3BcNUQTU7r-ub2Mbj1k16U9OW_JwUJnU3kLTaLnWVTbv6WTxwqcR6qOFn5EUF8XD9m0hISet2CJtXzJA2KaixKNXlEKyPBpGBItXs3nqndPMVJ-UbcWj9BfIPNTZ0OCqWbXiS2f73Zq44PHS5xIvS7gbgUG2N1RyBfy_c5HzLtAmEBywYg1hK7ekmKj_ed6xb-jr2Rn2of8hDR446T0f0nWr6oEOvXLHCrEY-p5A5oVXjPOsyE3QfCuDqeuHzAuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده مشخص شد https://t.me/FunyHipHopGP/12247710</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76414" target="_blank">📅 22:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76413" target="_blank">📅 22:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هوادارای آرسنال الان یه دوش آب سرد برید حتما چون بشدت حالتون خرابه امکان خدایی نکرده سکته هست،حتما یه دوش آب سرد برید و سعی کنید گوشی رو بذارید کنار تا فردا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76412" target="_blank">📅 22:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIQbBszGNwV47SyxozY0pPWimTrVEjy8EIiJ_9kdR_VyUVpBdLOg8R-6vWWIB-JT0Gn9ZLUKV0657ANPy0lIzpY-e8MsSwJ-S4uNJbo1T3zV9kVzaOUNLNMbmXA1YCOH-0SZpGyauSsO-qiZLv00Bu_c3-DlKRSXMkP26WrCIlL0J3mf3K4Tej--rRX2upS_w-rY4KHFZHYxlATt5eckZ4QvuSvttsoePXpwJXQfkm2ntNR6Mhaz1HkddvHSHkHhxAo3P30YMoq4Ws0mpTHbWhfvqR5VzYKCg8UVI6PXHUqBF5eoHtE6nrj4P3t3hJJP2ufDxbyieD3OkgEU9Bk9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پروف
#غمگین
#شله
#نور_از_دل_عالم_رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76411" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76410" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76409">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">گابریل
❌
اوساگونا
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76409" target="_blank">📅 22:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پاریسن ژرمن برای دومین سال پیاپی قهرمان لیگ قهرمانان اروپا شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76407" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پنالتی  رو ریییید
❌
❌
❌
❌
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76405" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گابریل پشت توپ
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76404" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76388">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رفت پنالتیییی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76388" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آخرین بار که فینال لیگ قهرمانان به ضربات پنالتی کشیده شد برمیگرده به سال ۲۰۱۶
سن سیرو
رئال و اتلتیکو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76385" target="_blank">📅 22:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گربه های مشهد گرسنه موندن امشبو
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76379" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۹۰ درصد ملت لوز شدن</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76378" target="_blank">📅 21:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76377">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تمام
بازی رفت وقت اضافی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76377" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76376">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روح بن لادن رید به خودش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76376" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">روح بن لادن الان در آرامشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76366" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76365">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدا سیما باز اون پدر تپله که پسرش رو شونشه و هردو عینک دارن و دارن خوشحالی میکنن‌رو نشون داد
چیزی رد شد؟!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76365" target="_blank">📅 20:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76363">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دوستان من اشتباه پوشش دادم
آرشیو وار گفته قبل گل آرسنال باید هند تروسارد گرفته میشده نه پنالتی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76363" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تو ضد حمله های پاریس هم باز ۵ نفر تو دفاع ان</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76359" target="_blank">📅 20:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76358">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بازی همینطور ادامه پیدا کنه صد در صد گل مساوی رو میخوره آرسنال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76358" target="_blank">📅 20:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گویا اخرین باری که آرسنال تو فینال چمپ گل اولو زده بارسا قهرمان شده
بارساییا نا امید نباشن</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76355" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🛑
ازدحام جمعیت در مشهد بخاطر بوی شله</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76354" target="_blank">📅 19:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هاورتز متخصص گلزنی در فینال لیگ قهرمانان اروپا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76352" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ارسنال زد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/76350" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بازی داره کم کم شروع میشه
به امید قهرمانی رئال مادرید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76348" target="_blank">📅 19:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">هم فنای فوتبال عقب موندن هم فنای هیپ هاپ، برا همینم اکثر کسایی که رپ گوش میدن فوتبالی هم هستن و برعکس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76347" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستان به صورت قاطع فضای فان هیپ هاپ برا فوتبال مناسبه یا هیپ هاپ
فوتبال
💘
هیپ هاپ
🦄</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76345" target="_blank">📅 19:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شما منتظر فینال سی ال اید من منتظر گیم هفت سری اسپرز تاندر تو‌ Nba  پ‌ن: فهمیدید شاخم یا بیشتر ادامه بدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76344" target="_blank">📅 18:51 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
