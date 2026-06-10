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
<img src="https://cdn4.telesco.pe/file/SsG_OQltecCAEmvZDhhlhhQWvM4D5lOciii9HaNkJHZ0jAUShxM6At604Kt5C8ezAocvFjWxFu8DnKpyOIs7uLLKaZ0Hd6_zVqfIcmQLOnNPokQ2UgFV3Es7HVkUd7D1_h9nH1shIpSi-BvqFmgzlsraJFlzomxVgKgUhcle7vNJ5w_biAEcVxJY9nSuaT9g2zoUbqhoJ_TCBD4CShgy-nICgh-x7-LSkl1tisu4womUOb55-pB3UIHAakY0R50z9CXp5hknr3YYCQ_yD6PZrrfhejbuoQ4-wty0lUByEBV3tdTPC7OpKQuVkNZu9jB7I5aVq5ExNLFjOXUJFsbXvw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-77557">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">موج جدید حمله‌ی آمریکا و فعالیت پدافند در بندر عباس.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/funhiphop/77557" target="_blank">📅 01:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77556">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۱ اسرائیل:
اسرائیل در این مرحله در حملات به ایران دخالتی ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/funhiphop/77556" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77555">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک تایمز:
امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/77555" target="_blank">📅 01:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77554">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یدیعوت آحارونوت:
احتمال آسیب به یک ناو نیروی دریایی ایالات متحده پس از درگیری‌های امشب با سپاه در تنگه هرمز وجود دارد.
گزارش‌ها هنوز بسیار تأیید نشده‌ و احتمالی هستند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/funhiphop/77554" target="_blank">📅 01:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی: امشب چند موج حمله دیگر نیز وجود دارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/77553" target="_blank">📅 01:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">با اعلام منابع دولتی، کارخونه پتروشیمی متعلق به مجتمع گاز پارس جنوبی تو عسلویه بمباران شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/funhiphop/77552" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایرنا: فرودگاه بندر عباس ایز دد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/77551" target="_blank">📅 01:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">با اعلام منابع دولتی، کارخونه پتروشیمی متعلق به مجتمع گاز پارس جنوبی تو عسلویه بمباران شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/funhiphop/77550" target="_blank">📅 01:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک سری گزارش تایید نشده از ترور علی لاریجانی داره منتشر میشه!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/77549" target="_blank">📅 01:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77547">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رشد شدید سهام فلافل پس از حملات آمریکا به جنوب.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/77547" target="_blank">📅 01:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77546">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آکسیوس:
تمام اهدافی که مورد حمله قرار گرفته‌اند در جنوب ایران واقع شده‌اند.
این اهداف شامل سامانه‌های پدافند هوایی، رادارها و واحدهای فرماندهی و کنترل پهپادها می‌شوند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/funhiphop/77546" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77545">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شلیک موشک های سپاه به سمت بیکینی باتم!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/funhiphop/77545" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77544">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الجزیره: اسرائیل هم امشب به ایران حمله کرده و تو عملیات حضور داره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/funhiphop/77544" target="_blank">📅 01:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رفتن سراغ زیرساخت زدن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/77543" target="_blank">📅 01:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77542">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مقامات آمریکایی به کانال ۱۲:
ما انتظار داریم پاسخ ایرانی ها مثل شب گذشته باشه و پاسخ خاص یا بزرگی رو شاهد نباشیم تا آتش‌بس فرو نپاشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/77542" target="_blank">📅 01:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77541">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">من که میدونم امشب هم آتش بس نقض نمیشه ولی نمیتونم ثابت کنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/funhiphop/77541" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77540">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رفتن سراغ زیرساخت زدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/77540" target="_blank">📅 01:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77539">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد نیم ساعت صداسیما انفجار های جنوب کشور رو تایید کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/77539" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77538">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش‌های تایید نشده از وقوع انفجار در کارخانه پتروشیمی عسلویه
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/funhiphop/77538" target="_blank">📅 01:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77537">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">من که میدونم امشب هم آتش بس نقض نمیشه ولی نمیتونم ثابت کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/funhiphop/77537" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAVKer6IkSq1YKo-7tLVycvn89ifJBX4GG3roci9-FlV1tbnbZZDgdujnl3LUyhDq567hVyzWmNl5iWsG_0CSMwXpud7mpuzwVRitQ-j2lFma2XqOhLtQTF9CcvsDXN15qBOF8kVZnpkN1-jGsrDxbqlTngCnzHWtC2S24vEnQ72djRC8UOFKEImDq-or306hy9OkKY9dN3jLS0EbR8io_rB8xmi2VppVybblwOCEeC1gKpZ0lgLCaa4eSY4i_CKl8abmayhlMoqcpIQr0TBwGGSIsrK7XmhY0w7YPumIdl-o1017Is3piecMNFyXu6I9GjTJvIq8-Arx93y4nV_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
حملات به ایران را از ۲۰ دقیقه پیش آغاز کردیم.
این حملات در پاسخ به تجاوزات بی‌دلیل و مداوم ایران است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/77536" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سه انفجار در قشم گزارش شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/funhiphop/77535" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دو انفجار در بندر عباس چند لحظه پیش.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/funhiphop/77534" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باراک راوید:
ایالات متحده حملات خود را به ایران آغاز کرده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/funhiphop/77533" target="_blank">📅 01:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فعال شدن پدافند ها در عسلویه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/77532" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تایید نشده:
لانچ موشک از سمت تبریز
احتمالا به سمت اسرائیل
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/funhiphop/77531" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجار در میناب
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/77530" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کانال ۱۲ اسرائیل رسماً شروع حملات آمریکا رو اعلام کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/77528" target="_blank">📅 00:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
ارتش اسرائیل سطح آماده‌باش خود را افزایش داده است تا برای احتمال ازسرگیری درگیری با ایران آماده باشد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/77527" target="_blank">📅 00:54 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فرید جان سیریک صدای انفجار بد اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/77526" target="_blank">📅 00:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تهران صدا انفجار شنیدید؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/77525" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77524">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری مهر: فعال شدن پدافند در غرب تهران.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/77524" target="_blank">📅 00:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77523">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حدود ۱۵ سوخترسان آمریکایی در آسمان منطقه درحال پروازن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/77523" target="_blank">📅 00:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77522">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فعالیت پدافند تو قشم گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/77522" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77521">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صدای انفجار تو کیش گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/77521" target="_blank">📅 00:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77520">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سری قبلی قرار بود ساعت ۲ بامداد حمله به زیرساخت هارو شروع کنن و آتش بس شد
پس این سری جنگ از ساعت ۲ شروع میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/77520" target="_blank">📅 00:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ: یه ساعت دیگه بالا باشید خیر نیس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77518" target="_blank">📅 00:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزیر جنگ آمریکا در ادامه:  سنتکام امشب شدیدا مشغول خواهد بود. ایالات متحده تأسیسات کلیدی در ایران را بمباران خواهد کرد. حملاتی که امشب رخ خواهد داد قوی و صریح خواهند بود.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77517" target="_blank">📅 00:21 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا:  همانطور که ترامپ امروز گفت جمهوری اسلامی معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار رو بسیار خوب انجام میده، بهتر از هر کس دیگری در جهان  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77516" target="_blank">📅 00:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا:
همانطور که ترامپ امروز گفت جمهوری اسلامی معامله نخواهند کرد، پس ما به شدت به آنها ضربه خواهیم زد. سنتکام این کار رو بسیار خوب انجام میده، بهتر از هر کس دیگری در جهان
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77515" target="_blank">📅 23:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/3f262c09ee.mp4?token=tZczUASVq4KCEfB5Ys6wZ2IgS4B3Hc9o8F4sb05OhSciVnXf_Ckc9qVpYRjNpo1dMqlJMnI8gPTpFLxU1BwY7ocNBjRy9FrKvxbtKGnouNGveYYLecTEwik6BumpojSijhKxJmzv9bXSZEEGds83ECaQdvgIl7XfNEKPM8hW-s9we704VHNrd7RPSA1ObDUBqwXVCClv8N-3pPKUu_w4GdgY27Dej1cXW8udgQsqL59rkHXAxkiUaoQhGEDwSpTJXYLzV0blkGrvd1jZm9vFR2WwGXvhoTd4hi7I6YwmK_k0XQ6se9CRGmzoEa95oete-xoKw4ndkO6udifn9zbRMw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/3f262c09ee.mp4?token=tZczUASVq4KCEfB5Ys6wZ2IgS4B3Hc9o8F4sb05OhSciVnXf_Ckc9qVpYRjNpo1dMqlJMnI8gPTpFLxU1BwY7ocNBjRy9FrKvxbtKGnouNGveYYLecTEwik6BumpojSijhKxJmzv9bXSZEEGds83ECaQdvgIl7XfNEKPM8hW-s9we704VHNrd7RPSA1ObDUBqwXVCClv8N-3pPKUu_w4GdgY27Dej1cXW8udgQsqL59rkHXAxkiUaoQhGEDwSpTJXYLzV0blkGrvd1jZm9vFR2WwGXvhoTd4hi7I6YwmK_k0XQ6se9CRGmzoEa95oete-xoKw4ndkO6udifn9zbRMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمام تصویر لو رفته از عاصم منیر همین الان:
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77512" target="_blank">📅 23:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77511" target="_blank">📅 23:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">معاون سیاسی امنیتی استاندار قم:در ساعات گذشته هیچ‌گونه فعالیت مرتبط با پدافند در استان قم انجام نشده و اخبار منتشرشده در این زمینه صحت ندارد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77510" target="_blank">📅 23:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سرور نامحدود واقعی!
⭐️
👑
پهنای باند ۱۰۰٪ نامحدود
👑
پینگ عالی، آپ‌تایم ۹۹.۹۹٪
👑
پشتیبانی ۲۴/۷  فقط ۲۹۹  هزار تومان ماهانه
🙂
💬
خرید
✈️
کانال مشتریان</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77509" target="_blank">📅 23:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77507">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VRAJGBjrRzo1aZRiAwdTkKRHLnuGoXeS1YAIBfP13Buy2MncYcExMqvfNnUh-RlCn0qAqYb-gBs6ppjdInPXS9fxZSAh01V_lMQcuFPWlNtr6QYvCf4oF0sfxobSRRrjso1dcaZSdZCLYdIDH97Q-PdQzb3AIl-pi5bu26Rx1P8MEoP6tuZpzw0pEqnDs1krLLd6UQMDrtgAAQuc6iD7C_VpzrNp1NEI0Il0h_Koy6ern4wSCpwkPI7EgfEtcndXNHnXdyktyeeSzWqZilWVE5AbyGu1TeveSwwd_QMhpHSfg1TxuLfQSmmEZsQGg3BvzZP0T-ySrZyZAUyLUe-GVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور نامحدود واقعی!
⭐️
👑
پهنای باند ۱۰۰٪ نامحدود
👑
پینگ عالی، آپ‌تایم ۹۹.۹۹٪
👑
پشتیبانی ۲۴/۷
فقط ۲۹۹
هزار تومان ماهانه
🙂
💬
خرید
✈️
کانال مشتریان</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77507" target="_blank">📅 22:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77506">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0anW3yOjSTlewdn0VOOF-gU-yTnNZO7myPxBMh-H5YRGuA5rVj4OostxEU2nwKB-c77t4A9TFviGPzBaWkklbxJUmEJTzunIrGIVyUUvlDukxTITUA-96BNdXcRfg_x3e_cCtani6bV3uU8rSFwMU2ErUtH1363MsMkXe3lRTFmqclb9TGAwCz7Z3qi_12ykshpRWLIc8zPOUGbF47cWhGYhiOmOs_J2qqGVXCmnGaC9l5pHmuxGX2If74O3oEVARb4eYo33ACHe3Yte5AdbwYck5n9j6ERl_5XZ_7YhqPBgPF8dTaCmt-OCfhO5wznf6RNFQRJUeylHcnjv1ZWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس رو نجات بده خواهشا:
در جنگ ۴۰ روزه، وسعت آب‌های سرزمینی ایران افزایش یافت؛ در جنگ بعدی، شاید وسعت خاک ایران افزایش یابد...
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77506" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77505">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس: مذاکره کننده‌های ایران به ترامپ قول داده بودن طی چند روز بهش جواب بدن ولی الان دو هفته‌ست که دارن زیادی طبق کتاب هنر مذاکره جلو می‌رن و برا همینه که ترامپ زده به سیم آخر.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77505" target="_blank">📅 22:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77504">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آکسیوس:
مذاکره کننده‌های ایران به ترامپ قول داده بودن طی چند روز بهش جواب بدن ولی الان دو هفته‌ست که دارن زیادی طبق کتاب هنر مذاکره جلو می‌رن و برا همینه که ترامپ زده به سیم آخر.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77504" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77501">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_PKJuqK773vp6Nnj1kFe4ZYAuNG8AZRXCD4JSYE4fS7qI_RLREZ20v01r3gy9YjdEyfynJF5ck2ImrtcZTLcBr3IO73Buyh8IjUfscvydre5nHeNBqIK6NrN807vVeRROhew2qJwlBUrWSQRxIzBo3h3gpMKftaQASjNloIr5aLpWRLZQKDJDD5-i7v9QcTnptvxO9qJPw4AQTE9284hgA-rh_swLYU-iisQWB_E9TggqKjmvIjTxdZWO0HUlhmjnaOhsTGozN_S3AmKt3JRTRR7W08vBodmbNQCTnjN982HAlsRUVes7QQj7EEryaDRODySEqill5jzM5bvOjc0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام وحید جان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77501" target="_blank">📅 22:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77500">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جواد خیابانی بالاخره ول کرد و بازنشسته شد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77500" target="_blank">📅 21:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77499">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77499" target="_blank">📅 21:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77498">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtBxyuDkClOZqgaB8tGwC6VXKTwfrt3grzTSIFxIm6fXmGYBP9r02eXm5RGs0b0aBs8MRctctOkDzVK1xvas0ShulYlDT0S4mzMak4R9IWam6XSEFC8gjtrIhY_nPK3OutIKQ_zxDkKa9c9T1el5oBghp9Rb6CSzyClZl8LukU90VBicSjMO2T4a3dA0YRuu_O9mlmR2ThApl6Om8eqAsIvZHJPxB5LW_N9obGVyd1R6PPXV0QPt61Sgjnz8-rtvUmfxBqRAMYI_Ovcczrpwnb4cstqZYVM4G0ZgbeiebXlwckiRjzE3KM_oHKYut_XVLRuF7oGkHCgojCwjBZcR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک بمب‌افکن هسته‌ای «B-52H» نیروی هوایی آمریکا که از ایتالیا حرکت کرده است، در حال حاضر بر فراز عربستان سعودی است و قرار است دقیقاً ظرف ۱ ساعت به منطقه عملیاتی ایران برسد.
🙏
🌹
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77498" target="_blank">📅 21:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77497">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlgcqvNcuf1FwVNJAxWJJDPuQNCk2AA0zMoHDZTTniu0kNXzlva2QVmlhTXWfsQSUL66DQZ1qkraWtoNp7iitaJOn9eOU1_4gfEarVPDH-XwfjroXVx20SvaZjmr4Pf0J1QDrdxnhYLLT_IX2IcCHcfWPcfOUSC6p6IiPPQZ8YaCjaz_ORdDEvPRhZBPM-J4SYja8zxD5nR3wvo8tOqhJF6xGEsDFony9jgN16PUnytY5daihRetEnhHOEFDrPaUBUAhxjYsAzy8MgT5fA7KPZsfGfoGtLbuLSwyJcGZ_re-8TaEWvbCWRe4xEP9P3K94U5NEjYxIseyatPXOcqwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
تو این یه ماه گذشته که گفتم پروژه آزادی تنگه هرمز متوقف شده دروغ گفتم.
☺️
ما داشتیم مخفیانه اون پروژه رو پیش می‌بردیم و ۱۰۰ تا کشتی تجاری و ۲۰۰ میلیون بشکه نفت از تنگه رد کردیم.
ایران نه کنترل تنگه هرمز رو داره و نه اقتصاد و نه نیروی نظامی.
کار ایران تمام است!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77497" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77496">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300a3fc2c7.mp4?token=SK3jmNWM1Ed8sEY0zECpl4Cqyw_7i3NcwKr1iHGBR32qbu9zx9E78ZgqxA4AoE9qhvFokqptVgZ-Ny4h5vSw1oF0T6zVWNZhhjuB2huTreMNtACfWFDkL0I28cO9O_D49R4V7mNhZp_Cs5eWKIEPHcUInNd2UoCI4m6-lRWS8b6YFAe3xA-bcep-_ha1dgaI0OvKX3w7OAICNtbBWm3M6hQrGz7erUqGQ-4SNw6lZsxoc_9KY1BNTaPXLh1lbbeVnOuPtBjU8dovIuNBoVfOz_Dgs5rBRNciJUf89dow55kHUQjhFsiCu_Ifw6vut0ybqhqh-8yNzfkjdj1kDFlOoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300a3fc2c7.mp4?token=SK3jmNWM1Ed8sEY0zECpl4Cqyw_7i3NcwKr1iHGBR32qbu9zx9E78ZgqxA4AoE9qhvFokqptVgZ-Ny4h5vSw1oF0T6zVWNZhhjuB2huTreMNtACfWFDkL0I28cO9O_D49R4V7mNhZp_Cs5eWKIEPHcUInNd2UoCI4m6-lRWS8b6YFAe3xA-bcep-_ha1dgaI0OvKX3w7OAICNtbBWm3M6hQrGz7erUqGQ-4SNw6lZsxoc_9KY1BNTaPXLh1lbbeVnOuPtBjU8dovIuNBoVfOz_Dgs5rBRNciJUf89dow55kHUQjhFsiCu_Ifw6vut0ybqhqh-8yNzfkjdj1kDFlOoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست هم اکنون
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77496" target="_blank">📅 21:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77495">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818b65b168.mp4?token=Wqd1byqL7oa0tax7glIF7KXsIvU06bG5d2PizFgQh8DBm65_dX0G3ACrhZCwTDBnP7ZnqzQFtcAHdZtIA42f5gGyb4Ekk9FbcQK3FDQjn5kamXhGA2fh_loC_Y4U2x43QzyQZIepb4NBh3JdMMDBHgxopqoL6W__-_dzQYjrIsDIvBai_ZnOwgMeYKHvWzK2EtiQUlP-8QM9Q51Age_gx10RaZJFSCaxi6CLrtV1JWCXzWWtSi8bzZlbP90Io8S6Cdk6iQZXau1-0uc2TjPQMcMNoNFo03etlcpf6OImE_sDi-toNdyVh6-srA7MuRQlHan3YxakOgs0LysCNpDD53pT5YnkeVTW7fBHuUwiuGbU06TVDillMLnFDGxciggxLlAJ7rBUmvfFQ26S0STZQ6jsZ4T80TsVtG5IziOTCmvX9--a6BITfx-MAgDIijFH_546mru5UnK_tw9PBHUTjKDvZ63wxvLnOZQD4P0g9xp1W7mVTMvMAkXuZNE8qXoAsAgn4O7mh6DkUkRxNKom0IcssHoC9vEzfWAIZ-l1Sq6UiOiGHvbudz3IAqlYpW-jKd3vzAXb9onEajfXVGZwa4QSlUhn6gdTOuANoS2tMcwyTE4QVxo0s181rTl4u1G6-sCwICmGBY06aHbR35oPTvCIJRcJVixGB7uAOG87v9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818b65b168.mp4?token=Wqd1byqL7oa0tax7glIF7KXsIvU06bG5d2PizFgQh8DBm65_dX0G3ACrhZCwTDBnP7ZnqzQFtcAHdZtIA42f5gGyb4Ekk9FbcQK3FDQjn5kamXhGA2fh_loC_Y4U2x43QzyQZIepb4NBh3JdMMDBHgxopqoL6W__-_dzQYjrIsDIvBai_ZnOwgMeYKHvWzK2EtiQUlP-8QM9Q51Age_gx10RaZJFSCaxi6CLrtV1JWCXzWWtSi8bzZlbP90Io8S6Cdk6iQZXau1-0uc2TjPQMcMNoNFo03etlcpf6OImE_sDi-toNdyVh6-srA7MuRQlHan3YxakOgs0LysCNpDD53pT5YnkeVTW7fBHuUwiuGbU06TVDillMLnFDGxciggxLlAJ7rBUmvfFQ26S0STZQ6jsZ4T80TsVtG5IziOTCmvX9--a6BITfx-MAgDIijFH_546mru5UnK_tw9PBHUTjKDvZ63wxvLnOZQD4P0g9xp1W7mVTMvMAkXuZNE8qXoAsAgn4O7mh6DkUkRxNKom0IcssHoC9vEzfWAIZ-l1Sq6UiOiGHvbudz3IAqlYpW-jKd3vzAXb9onEajfXVGZwa4QSlUhn6gdTOuANoS2tMcwyTE4QVxo0s181rTl4u1G6-sCwICmGBY06aHbR35oPTvCIJRcJVixGB7uAOG87v9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">I24NEWS:
آمریکا در حال آماده‌سازی موج گسترده‌تری از حملات علیه اهداف ایرانی در ساعات آینده است که فراتر از محدوده حملات قبلی خواهد بود.
حملات پیش رو با هدف فشار بر تهران برای پاسخ به توافق هسته‌ای که در حال مذاکره است، انجام می‌شود و نه به عنوان نشانه‌ای از بازگشت به درگیری تمام‌عیار.
تصمیم رئیس‌جمهور ترامپ تحت تأثیر حادثه اخیر هلیکوپتر، افزایش ناامیدی از عدم واکنش از سوی رهبر معظم، مجتبی خامنه‌ای و حلقه اطرافش، و فشار از سوی مقامات طرفدار رویکرد سختگیرانه‌تر بود، هرچند مشاورانی مانند جرد کوشنر و استیو ویتکاف از ادامه دیپلماسی حمایت می‌کردند.
این حملات با هدف شکستن بن‌بست دیپلماتیک انجام می‌شود، اگرچه دیپلمات‌های عرب هشدار داده‌اند که واکنش ایران غیرقابل پیش‌بینی است و ممکن است خطر تشدید درگیری به جنگی گسترده‌تر را به همراه داشته باشد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77495" target="_blank">📅 20:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77494">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">میدونید چرا آمریکا همش شب حمله میکنه؟ چون خلباناشون سیاهن تو شب معلوم نمیشن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77494" target="_blank">📅 20:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77493">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار: برای تولدت چه آرزویی میکنی؟
ترامپ: صلح در تمام دنیا.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77493" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77492">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
ما میلیون‌ها بشکه نفت را خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما قبلاً میلیون‌ها بشکه نفت را خارج کرده بودیم. هر شب نفت را خارج می‌کردیم.
اما حالا می‌خواهم به شما بگویم چون ایران تازه متوجه شده است.
حالا که فهمیده‌اند، می‌توانم به شما بگویم. برای من خیلی سخت بود. خیلی می‌خواستم بگویم، اما نمی‌خواستم خرابش کنم.
میلیون‌ها بشکه نفت خارج شده است و به همین دلیل است که قیمت نفت ۸۵ تا ۹۰ دلار به ازای هر بشکه است نه ۲۵۰ دلار
﻿
پ.ن: پوتین یه چیزو هیچوقت اشتباه نگفت، که این کصکش نابغه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77492" target="_blank">📅 20:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77491">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">فوری از علیرضا تنگسیری، فرمانده نیروی دریایی سپاه:
در صورت حمله آمریکا، تنگه باب المندب را خواهم بست!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77491" target="_blank">📅 19:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77487">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دخترا لطفا نترسین، میدان با ما آشپزخونه با شما
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77487" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77486">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDpRa6PbrQ17WEBEXp7n327K5fgq5QhnyiFCduz0sDQt1PBLDUh7xdj2kccdz45iJyTNVpR8KgdNNXoagxy0kdD51_5CUCB8MCFD2g57IXMtwBdl2sWSHZ_ph9HpLDNfwXCCCzJxWKEZSxf1FGgWY_PqmOb371vu8HjHjW0xnE_QomUntqNw3JFKh9BhY00i8qvoBVhdxiLTh36NmXpZ4JOTnVMOVWvOdS6MD3A9uJ-acdMAPpOE2rD62-YT3kg4ISc_pMrKnwvZHNiFOQD7Nzv71UMpmL42fbcJ99QoJZOy62cakgQM-CWiDiVR--Pq75Y17q4bIaGYtD94nKcN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد از تهدید جمهوری اسلامی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77486" target="_blank">📅 19:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77485">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ خیلی واضح گفت کصو کونو جمع کنین میخواییم کیر خایه پهن کنیم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77485" target="_blank">📅 19:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77484">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سردار سلامی هم اکنون در اتاق جنگ!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77484" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ:
امشب میزنیم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77483" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4Tho3et6FlIH6YCrqZnuEvxSMUr6QKMN9kq47vmZfSeS40yO_wyA7nqtry8o-5KwzMpn_vBfObfYAhrl59fbfsiJ1Ug6dobdhTzfD_I7GOi5nxot35nKvgrbRtsnu7ACEzDx7bh-jQlwQq4YfUqZeoh3mWwjd8F9I0dMwr1zlvIGV0iuk3sJiwhltRsSDJSpRzvGhAtZAm_cci9j-WWvQg4o03UQPnAt-rhvGd9kPHtkO5_7CkXi3YwFFUdDpgouW1bwEEoVglrhwMVFVY6KCoUB3y0Bdw8X5rY8n1bAfsZ1fZeS3Ts9ziV-C1AV-ekDOMYWkjMhGC7N8OW2Y-3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک ویدیو جدید آرون به نام "NoseBleed" ریلیز شد.
🎵
YouTube
🎵
SoundCloud
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77482" target="_blank">📅 19:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77480">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMX7utTE2a4HZIpLj6tCrRxyIM5vhM4tcLwmZ_pwv5MZteQgc_hm9Tg-F4SOL9Oa3A41xX8M_BrXOn1NWypWFH1z1pAsGsbJXZ9-gmq9viytjF9oRwON6BfjPf5_poVV35EkgybWO8jpUUIJJzhkfbD5_mzsjq6OnKrRyYphpeUSM0l1eOFqQszv980NJPhC07S2jO6AwySssW4mS1X4WB_aOAsIweoY-76V7GkUj1tt7nkPGqDTSQGgoOj8uuKSa7edyVKgrsVpC-tqLYVA1-MC6l1KC7KyXPLuUp9AZQyf7GyJuWUIZrOVLZJQhqd7ty_umQfOklEbKtppQaqkjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح سواد سیاسی اجتماعیت منو یاد اونایی میندازه که فکر میکنن آتوی پرونده اپستین دست یهودیا باعث شد ترامپ به ایران حمله کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77480" target="_blank">📅 18:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77479">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا، در یک سخنرانی اضطراری با مردم و رسانه‌ها صحبت خواهد کرد.  جزئیات و محورهای این سخنرانی هنوز اعلام نشده است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77479" target="_blank">📅 18:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77478">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قطعنامه پیشنهادی آمریکا با همراهی سه کشور اروپایی فرانسه، انگلیس و آلمان علیه برنامه هسته‌ای جمهوری اسلامی، در نشست شورای حکام آژانس بین‌المللی انرژی اتمی به تصویب رسید.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77478" target="_blank">📅 18:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77477">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا، در یک سخنرانی اضطراری با مردم و رسانه‌ها صحبت خواهد کرد.
جزئیات و محورهای این سخنرانی هنوز اعلام نشده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77477" target="_blank">📅 18:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126e9f8e6d.mp4?token=kjYGBlLqmrE8ojjVX_3byR9S79QGJEzwfBw1pJ3XNICTKAJe57jk74z3riGIuyW7vz9y6I21XRRmRij6YsDlCwvmYhNALtxTSGYTZP3BBjGKVP1hetOiCdQY625FNGFJ38BCfL8_XiF5L6SNOStDXvROzvuPDzNgzBtu4_7yM9BthVsggnaiKEetvz0SnasZ7zgCE5YubLw4emhZ5VwSZ5XYWBIZvtpljEuUiG2ko8-8AajKPhS8qkRLwNNGwldG0BkymdKBupY-gCRS8xmI9e5bMr649qB_FL8ea1hC5T2ZEekB6lj2R8lBpGYS8POA0wObNbuyXbE1ElCo-p9j1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126e9f8e6d.mp4?token=kjYGBlLqmrE8ojjVX_3byR9S79QGJEzwfBw1pJ3XNICTKAJe57jk74z3riGIuyW7vz9y6I21XRRmRij6YsDlCwvmYhNALtxTSGYTZP3BBjGKVP1hetOiCdQY625FNGFJ38BCfL8_XiF5L6SNOStDXvROzvuPDzNgzBtu4_7yM9BthVsggnaiKEetvz0SnasZ7zgCE5YubLw4emhZ5VwSZ5XYWBIZvtpljEuUiG2ko8-8AajKPhS8qkRLwNNGwldG0BkymdKBupY-gCRS8xmI9e5bMr649qB_FL8ea1hC5T2ZEekB6lj2R8lBpGYS8POA0wObNbuyXbE1ElCo-p9j1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناموس چموش: اغلب انقلاب‌هایی که از سر گرسنگی شکل گرفتند ناموفق بودند
تغییر باید با آگاهی شکل بگیرد. قربانی کردن دیگران برای رسیدن به هدف شرافتمندانه نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77476" target="_blank">📅 17:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77475">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شهربانو منصوریان چه کراشی شده پسر.  @FunHipHop | AmooFirooz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77475" target="_blank">📅 17:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpuM2hAxd04QPk0py2IMTC46UofQc25fagZa_05FXW5KkoqbimRHSXp8jb13MB-1yyEPV-Vx2-GlM-7lY8wbPWIVxKW49SV_RPGDIKx9fDt-aBTg-omEK8ExS6JQ7_QTynrZudyPeuIP-uVrlbujwoIkF0teguR4B4Dibp3e6Z8H5wOf6IVq6svEQznB17-xYxyRf8FELwW1Q0Of02_nXHaUTPYhfQO6RkyKIFGLexBnZq1lllzYUmVtwm8ZuKGTmXtM9aHSJ6a4IJrPHcP1mtFX_TjR3KDLygkj5gz3ob8wDSo1haUExZZmTdRtHmEBEy0P2uFwy_Bi47yIkJxm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهربانو منصوریان چه کراشی شده پسر.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77474" target="_blank">📅 17:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TERvtgIS-CP5BYshblsGaAzctDyltzqkIQ8uc299YUaJpSFK2fDg16C0MdguUyV54W74J7kKStIAAc_8wPK_koIeQW-QgccBe2x2vax5o7Z6OUe00-a1jRLOuEzgywf5tL_cQG1CLboz8-u5jHQ3D4jWTUf1tcTXP7wiT_-LsXdhNq6kaW-llrLuaBJ5MDTz5_ncDOL4qYRFfl8EyKle4s-TXzCw0KvuSX6K2eUUf7IZXslUTj7HJ-8xT8yLKIF0I0EJdLwVeVqgDI0GrFRpkqQiyhd2cneFXrey7kRuhB8sSpqRs52tE4XMiWGe249Y7bMuT1ncW7x6s3mLJ4lcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تو کون نرو» اگه آدم میشد :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/77473" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77472">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/77472" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77471">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBhTOjG_02Dbwd1lUI1yehwyZK3QRzXmouLHhjQPMpmAIAfvg2cpoPkP_WzyLYPWv1dji2B7edH_Yjtsm3B3COPlbhgtnw4VloJMgSyxk9-G7xnQwPdT5CPIbNl9gKNHEh9-e1IR0U8ZF-SQzkx-ELBFaiFKXaauhOWs2NZbeZ8uPj-Ri7a1wNKppujh_YmJP3ksFa-ERmNCGNBaNvI4JrMV5oFvam-jAHdTtFq9SDceMpOVSz_X_cT7XUtAn2NDiuPHqT1WguboyO7cENykxtzhlsLotyL6gKt2fuiDm60nxt_Ct84EnBOcrAETAmtxh5P6m7Y1QC5uPVg1VX8pew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g20
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77471" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/araUVRGaq3QzmdN_2-L6dJyjdeAtFSH4byhI2nWdh9-pTRcOQ_nuyQh2k-7P6h0XYiF9lyE1tJs7642d0JDD5P6ndn6JEH2Rmt4X1E_NG2wZ46kbtpcxksoaCT--9_QWw0xUg_aB01nrq3DICQ8P_n3HdisR0mvVxQNDbhT4y7F8_48lgoVLJRuWiN5NRGF25tRmRrsboi9lsvMhdYq2N1BdkVfrOaZv3vZmyKfUgIZF9Yl-9DcUuD02WWpg5ydlH0c40wIRIjCZuHtduVqAfiFvVq6QLWDyzxXHzFr-_kthe8MnxPMi_xOMk4dmUQKLVh1GAYKKhT4WuoCZlJB_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77470" target="_blank">📅 17:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77469">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ به کانال ۱۳:
به زودی حملات بیشتری علیه ایران پیش‌بینی می‌شود، احتمالاً از آنچه دیشب دیدیم، قابل توجه‌تر خواهند بود! علاوه بر این، یک گزینه واقعی برای حمله به تأسیسات برق در ایران وجود خواهد داشت.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77469" target="_blank">📅 16:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این دفعه بخدا عی ماخارنا ماخارنا ماخارنا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77467" target="_blank">📅 16:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">۸ ‏فروند جت جنگنده F35 B در راه خاورمیانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77466" target="_blank">📅 16:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چندین بمب افکن B52 در انگلستان مستقر شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77465" target="_blank">📅 16:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">میگن
ترامپ ۳ میلیارد دلار اسکم شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77464" target="_blank">📅 16:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فاکس نیوز:
مذاکرات آمریکا و ایران همچنان در جریان است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77463" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ:  هنوز با ایران کارم تمام نشده است.  ما ۵۵٪ از آنچه ایران در طول آتش‌بس بازسازی کرده بودند را نابود کردیم. این احتمال وجود دارد که من به حمله‌ی دیشب ایران به کشورهای عربی واکنش نشان دهم.  دارم به آن فکر می‌کنم. حملات بیشتر آمریکا به ایران یک گزینه‌ی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77462" target="_blank">📅 15:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ویویویویوی
I24NEWS:
ترامپ دیشب با نخست‌وزیر نتانیاهو صحبت کرد و او را در جریان حمله مورد انتظار امشب قرار داده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77461" target="_blank">📅 15:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ:
هنوز با ایران کارم تمام نشده است.
ما ۵۵٪ از آنچه ایران در طول آتش‌بس بازسازی کرده بودند را نابود کردیم.
این احتمال وجود دارد که من به حمله‌ی دیشب ایران به کشورهای عربی واکنش نشان دهم.
دارم به آن فکر می‌کنم.
حملات بیشتر آمریکا به ایران یک گزینه‌ی بسیار واقعی‌ست.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77460" target="_blank">📅 15:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWGRo0BnKYT3fa3Flqq1FmPx3SLRXBetB1DOVZUBhseyP-mK5gXk_I9_nLvf8bq1eCTDCSR3YWRuDMLwoeL3N9OCvqYqVWG9kyfjEdXYWVGJA4xz7MnOJueQX9GAhlKVYBNxAiGVEJERe6oaYCSoY70Gk_YphvPvPYHjIvBWiyDOonwAdLqRggTOLwUSYzoaGAYz0kf_WLqz4CzDlnsaJNxP9ujJSczSadB3y3FOl_c9XGM_8iLA0AeMGdCtT-g-oZOjB5gby8UWDz1HhC7N253hk5g1SvKmz2vEapPjgb-9D1el4o-01S9u-buEw401UCNuEK-Dz-BgtKCtUcDHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر بالا رو توصیف کنید (۲ نمره)
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77459" target="_blank">📅 15:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aewTbTA2bO_LLl9s51_igFWyPzxEe40W9JU34pfLd2ClYJzNZ_zURouXJCi-2o3wD6N-mWZzWYyFAd2IIcHlKLGzdfnZoXsbFLg3pc7f-aJi1ClJjAGy6z_sG6MqKg_dCq1u-vfnwr_LoL1bScK9BlGtVvt6erEZTnZNhQ6Ek_I3XET_880JKNDSKXtnHW6LlSPfxOWOrhsvwP4TNVrcN0ptziGA0Bp-vRoDdkGBUBs2lTwzX_Ee2RkgHCAY5r64amDP7MDjWdQIyOOBDZgxt30UFN3eSArE9LTPU5pFlApFMqF8JLWHO-pNVgwWz1jdZnFvlNXoZuZVoZQ-MaxeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز از الله تشکر کرد
🙏
:
رسانه‌های خبری جعلی از گزارش دادن دربارهٔ اثربخشی محاصرهٔ دریایی ایالات متحده خودداری می‌کنند، موفق‌ترین محاصره در تاریخ جنگ‌های دریایی.
هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است!
ایران هیچ کسب‌وکاری انجام نمی‌دهد، حقوق نظامیانش را نمی‌پردازد و هیچ یک از صورتحساب‌هایش را نمی‌پردازد و به سرعت در حال تبدیل شدن به یک کشور شکست‌خورده است! مقدار زیادی نفت در حال هدر رفتن است.
الحمدلله
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77458" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ باز می‌خواد بترسونه:
ترامپ به فاکس نیوز گفت که نزدیک است دستور حملات بیشتری را بدهد که به زیرساخت‌های انرژی و پل‌ها در ایران هم آسیب می‌رساند زیرا مذاکره کنندگان ایرانی بیش از حد همه چیز را کش داده اند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77457" target="_blank">📅 15:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">توماج صالحی به قیام دی ماه تیکه انداخته و گفته انقلاب هایی که بخاطر گرسنگی شکل گرفته همیشه ناموفق بوده
پ.ن: چقد یه نفر میتونه مادرجنده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77456" target="_blank">📅 14:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فاکس نیوز:
مذاکره‌کنندگان قطری امروز صبح به تهران سفر کردند، با هماهنگی ایالات متحده، تا با مقامات ایرانی دیدار کنند و تلاش کنند شکاف‌های باقی‌مانده در روند مذاکرات را پر کنند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77455" target="_blank">📅 14:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX7z9J-6FQwRIeaCSvJ7xTtxOTc2mS9Y3FI_KZD8P9K_mIHVf-5o9FeOP8byqspU4krYhMBtEyoTS-8zWRkcOt2okTd8mXcIcBxREQX5FhdBRGoMTKOQJqRttlszBnj2EnB9IEl9UC-oHSrB5OuQZX4gJQZonUn3xI0LTWnpaNGZc_uNJ_rwLDTNvlocr7ioSFskb2KpthfVtMazWaV9A7QBk0gecyLmC6bTGlPnpe9w11PPcixVrPWGwxfRuFFhKrheaUMdR6OlRaobrVVGVekTWpqv4DsOHlF554w1Wr_NMCEFK8nuIpS5juMlMZVIOGOQXEHRNju8NWtBUxAzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید ترامپ:
ارتش ایران یک آشفتگی کامل و کامل است. بسیاری از آنها، مانند نیروی دریایی و نیروی هوایی آنها، دیگر حتی وجود ندارند - آنها کاملاً شکست خورده اند.
ایران همه حرف است و هیچ اقدامی نیست. قلدر خاورمیانه مرده!!!
آنها برای مذاکره در مورد معامله ای که برایشان عالی بود خیلی طول کشیده است، حالا باید بهای آن را بپردازند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77454" target="_blank">📅 14:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فک کن معروف ترین آرتیست مملکت از پشت تلفن زندان موزیک خونده داده بیرون</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77453" target="_blank">📅 14:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">واقعا این ترک جدید تتلو رو گوش دادم خیلی ناراحت شدم، درسته خارکسه بود ولی اگه قرار بود خارکسه بودن جرم باشه نصف کشور الان میباید زندان میبودن
ول کنید این بدبخت روانیو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77452" target="_blank">📅 14:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دستاورد طلایی جنگ های اخیر تو سهمیه کنکور سالهای آینده شکوفا میشه
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77451" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیروز روز جهانی سکس بود برا همین تو خاورمیانه همو داشتن میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77450" target="_blank">📅 12:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سلام صبحتون بخیر، متاسفانه دیشب خواب بودم متوجه حملات سپاه به کشورای خلیج فارس نشدم.
#بیکینی_باتم_تسلیت
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77449" target="_blank">📅 11:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ممرضا بنازمت دیشب بعد از مدت ها خندوندیمون</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77448" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سوپرپانچ دیشب شایع که جنگ فیدش کرد : کونمو مشتی بخورید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77447" target="_blank">📅 09:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_k8R6u3TBljCv00fgejYmbazVL615bj_SdJHrBi4wNpmVLbz7szBMVXnMvKf_t3Rxp1c4e0vSqY0zPoyV3KsQQXO6b7zmUZyu5z_KM5YLLaT2fx83cyDwP1Be7mCoOBFi9MxWOWJ3QJkXaYGjXrFMxGU2PaA4u07Qh9JzQvVQXqLFTT2qnVzZFHHSNkUQDr5nQ27BSzTd2Qbpdcqx-_Rk_7IOS6PeIj7SJbuaJbhX1kFksha3bzfvJFod0oiVEjSlS5TOGBC3zYEKHII2Ihp4YnLfGABGbNH9JT4YO_u0uyGF-v7wSOhjdh6f7VQ5rl9Bel6fqfkBmv0gHCsW_K7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cp7nrcJOzV6yPLJ3UlkuGgfRy9z8PN3CBvbT3e9YPO5vF8F_vferfk-GyBCjM8lOPKnk1vKa-u7y6ReuDXf900PxG7Nr6CTcXec9IfmZ1dBSrDY4MKcya3ylqVd2ASgdy7W0Sj_nPHUO4TSrGVMGplg6GdsjkHoZKLTLGWA30ZAXngT3ALrOS1_-cu9RLkfSdSO-JLBsx7XGzZdUCErwGFUbjdscIQmdbTrL9D-uhy8720jxn4g9UrPlCYNUAQGN-kEA1rFL9aPdQfn6B5mxfOlCoWG5QzsikXlEiirJlvdgLIeOEUC8uLgtW0WPCUwADT2LoUNGGfufsNqHZ1ZBSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط و فقط یک روز تا شروع جام‌جهانی.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77445" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctGFVsdNVmAl1YWreeK5FYrTlc1dTnK510gVT3pjCtlRrm_pTxOYWTNPd1pB8_43trqbRnssozjkADDkDMiODYuhPeF66MpMfLOZTgUSii-E8rGBK5IbBNqbcC1d1yDeP1bCX1O7Dsu-vF1goUccGbgM7mrjJdLfYglYsjnD4QVVlUctG6Eju6XzXhisb4NEhzF84c2ihj0KEZEId7c4ry8uvJ1IxtHg1V5IbGKdtxP3j5Y934hLcwihOiKclw-rOcqzPuAuvLRBu_HVuObg9xpbkiBci8RWPd_XH9b2RAguU-YZORO6yvkMEXOdWzgch0vJKuYYPxT9dsSvFN_vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
👍
ورود به سایت با فیلترشکن
R20
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77444" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
