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
<img src="https://cdn4.telesco.pe/file/UibJvAdftkxWYNQsgq7kSKXEOcQQBc06qDqZXPf9OoDpB-mZ5I4ErEruzQdD3tTt1dfBnizZH8zSuhUclpOSTsyJtP42TjFcG9y9Jaanpqz2R7JHMztlHPGcOK59Bw62iWCMOABCOVXO5m95h-L6LsEPg-XpdELsaNE-ZSPdNcV0fwyi9asLZimtPzEwNLoDd0kclG_IqkbJjUXq_Z7Ze5V5dpcIU7OhpTUvcZlKZGs50ndmZnnMVncvS0nfd5GL46irIKK0YjzrTu6bIDUmt0CtE-Kc6I8jS-g7ruWnFY_YydbaYXSm34CcAQsqUp5Ih_28fthaFuLTgD99OMUrqg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 195K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 04:59:13</div>
<hr>

<div class="tg-post" id="msg-80379">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">متاسفانه طبق گزارشات، آسایشگاه سربازان در ایرانشهر با موشک هدف قرار گرفته و تعداد زیادی از سربازا جونشونو از دست دادن و آمار مجروحین هم خیلی بالاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/funhiphop/80379" target="_blank">📅 04:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">روزتون چطور گذشت؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/80377" target="_blank">📅 02:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">باز که شروع کردی تاجر
ترامپ: ما امشب، فردا و پس‌فردا به ایران با قدرت ضربه خواهیم زد و در مرحله نهایی، نیروگاه‌ها و پل‌ها رو هدف قرار خواهیم داد.
اگر اونا با بازگشت به میز مذاکره موافقت نکنن، تمامی پل‌هارو هدف قرار خواهیم داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/funhiphop/80376" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بهترین فرصته ویناک هم با یکی شرط ببنده سر پول جیگرای اونشبی که شاهی با دوس دخترش خورد و فرار کرد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/funhiphop/80375" target="_blank">📅 01:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اینام میدونن ویناک نمیگیره هی دنده میدن به همدیگه
اگه خیلی پولدارید ویناک نگرفت 333 میلیون بدید خیریه با سندو مدرک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/80374" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اقا رپفارسی درست شد
ادرویت و شاهی رو بازی فرداشب بستن
هرکی ببازه باید بدهی دکیو بده به ویناک
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/80373" target="_blank">📅 01:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/80372" target="_blank">📅 01:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تنها دلخوشیم ویسای شبهه علی داییه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80371" target="_blank">📅 01:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیکتاتور بعد از باخت سنگین از شدت خشم به ترامپ دستور داد به جنوب ایران حمله کنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80370" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سرنوشت دیکتاتور سقوطه امباپه جان</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80369" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80367">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بارها گفتم تو فوتبال تا خط هافبک درست حسابی نداشته باشی هیچ گوهی نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80367" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihOrlXsHWtm3AZExh3PMXESKCvC6UdaTEfF_DwSSgdHj108Pwf_3GfJu4DkcwSqUezGcxS8B_uH2EtkNe7jVbqTEjMhRpfvaV5kgSn66eP09eItsUHirAXv-Jsqq3nL1vQNKjJoOVQTt3aa_YCGiZan7zJvP_WuKQoR-gZyel22ZLkzJc7qp3eHdUgmT0RaY5kEsQ03q4F0lEJEIUuL8hqLVnyU7c6TuCK36JzSwlY_IvKJrqrJnooM18d4Q3vZArf-S-BHBmKwQsiWD38BoypGf4MkaClFjEPfC44JvrgTASbKkUCtepFPAoeY5Ah_MLdKRnREDTxQnX7sGNQBV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیرم تو این بازیکن اسماعیل، کیرم تو این بازیکن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80366" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFkVjx63JQb6t242WdpXfcvho-SzzM95KWdQXKaMlf_9n57s-pfhn1Cy3T5_BdjBQgfUI96_cMjZZvxnhFN8YcP5B9OnCo__msof0j8-MDu4wgM0BT8VTv9NqemI1RtB8r-cWHOVTWo4yz3bCtP5yNuj0k9isy3KQ-RTY8i7KhrGsLrD_FQZOzEUlQ10_l01S9RXEmVMSdxVzTeYvwwRgnLItGu3OtkpwEM_snTQC2HknOphonogJVed4Lc5qGxofSce3HaSCFdyy6ffzXw7fHyBbAxR82cMWCEeeE3g8klVagbawhQVxFBy_XG2I7qDA0AewRTWRA4_gqVFfAxOeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80365" target="_blank">📅 00:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80364">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سرنوشت دیکتاتور سقوطه امباپه جان</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80364" target="_blank">📅 00:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80363">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">با اختلاف این گوه ترین جام جهانی بود که تو زندگیم دیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80363" target="_blank">📅 00:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80362">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">امباپه فشاری رو
😂
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80362" target="_blank">📅 00:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">امباپه دیکتاتوری که ایستاده سقوط کرد (رید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80359" target="_blank">📅 00:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Shahi</strong></div>
<div class="tg-text">سنگین بستم رو فرانسه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80358" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded froma.r.m.27</strong></div>
<div class="tg-text">از وقتی شاهی گفت سوئگ دارم مایکل اولیسه یروز خوشم ندید</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80357" target="_blank">📅 00:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80354">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گریه امباپه ضریبش چنده ببندیم روش
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80354" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80344">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چه بتایی که امشب لوز میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80344" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80326">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سلام آقا فرید همین الان اهواز رو زدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80326" target="_blank">📅 22:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">امشب اگه فرانسه برد نفری ی شارژ بیست تومنی ازتون میگیرم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80323" target="_blank">📅 22:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">جنوب، همون همیشگیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80322" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بارسایی بدبخت شدی
دیونگ چون جلو مراکش با مصدومیت بازی کرده رباط زانوش پاره شده و نصف فصلو از دست داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80321" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اگر دنبال یه پلتفرم کامل برای فیلم، سریال، انیمه و انیمیشن هستی، وقتشه Meowvie رو امتحان کنی.
✨
امکانات Meowvie:
🎥
آرشیو گسترده فیلم، سریال، انیمه و انیمیشن
🤖
هوش مصنوعی اختصاصی برای پاسخ به سوالات و پیشنهاد محتوا
🌐
نسخه تحت وب (قابل استفاده روی iPhone، iPad و همه مرورگرها)
📱
اندروید
💻
ویندوز
🍎
macOS (Intel و Apple Silicon)
📺
Android TV
⚡
اگر فیلم یا سریال موردنظرت داخل آرشیو نبود، کافیه فقط درخواست ثبت کنی؛ پس از بررسی توسط پشتیبانی، در سریع‌ترین زمان ممکن (معمولاً تا ۳۰ دقیقه) به آرشیو اضافه می‌شود.
🇮🇷
حتی در صورت اختلال یا قطع اینترنت بین‌الملل، Meowvie برای کاربران داخل ایران در دسترس خواهد بود.
🔥
همین حالا می‌تونی وارد Meowvie بشی و تجربه‌اش کنی.
🔗
لینک دانلود و ورود:
meowvie.ir
@meowvie_ir</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80320" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80319">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبر خوب برای دانش اموزا
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/80319" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">طوری که بحرین رو زدن احتمالا امشب تهرانم میزنن</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/80318" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80317">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فرانسه فقط حملش سوپره مگر نه خط هافبک و دفاع جالبی نداره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80317" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaY9OAj4CyAWdXqadrsaG3JSTg2bitbdU8a0v5UH1pMkLh6wnxRXdKzSKeOMuCweQoc9eD7em7vfRBlxfqFrsekI8LG5SrFYlZ5Zgz5H8nsAwKyEQvl5LmgkaF5Lw_BOimlJhJl-kGrKjzs57T920gmWJ98MZJ6ZPQjeEdVgvwRmB9gTKqOlQvSFwLv5kYfc0snXNVpPqEq7WSNpgfFUeYyPRJVDgjLhMhia8d7ZawO2nI_U-cOIj0OW8WxkYTVmD9R-uPLal1gCi2xrJDUXF1Fdb_yz8w-ZvNbTVTxMmDVVU6P30YMemskminfApd2tMjAJ-_MVGds2iXreo21faw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80316" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80315">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gURlkB91p_WxsNEeHnnNGzn79WHJ9tKuBk3N1_EM1xskEwrMOCWJajAyt4w4bvuWPEtVszrc6WtqmoDlR8o2bJysZPqpDrgE0J2FxdOoHk7C--yqZlJQK3M8cTJIDZiwTiPpAVxhNGSxSeqJOvFpul4RUkggLvTCJgoX-aWU1GPhkRW2J2dLuPvCZnxaDUouFEz3IsvHXDS8fZFGvDNTL2iXgOTqxOGBEtPO8XgbHTTOSNryKsumFDYrXGvx_to62KElhDPpxFVYsDiYUgrVn7XmCb33Tj9dpxNwbL9WvZ_bK_Rge6-B9Z9BEmmJWDHNJE01qpOclNECtOcVAXOJwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کصمادرت با این ترکیب چیدنت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80315" target="_blank">📅 20:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80314">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">داش میدونیم مادرت کونیه لازم نیس یادمون بندازی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80314" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80313">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80313" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80312">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=vEgx6x5DuxJr7E2dlA574uGQBwQrbHaNnVs4v3jKKKORhPv64PwSs21xWDL13f4TjQxGHEBNBlyqVZrPJrDULmt5mL3L3hz7EC3fQpgH_Bek-ltTWOfN4VrIojMt1n_NF5Jt5okaZz-3leYUOdr6cGQsgVSXJ7yzxCnu3hpy7t8n4YQv9kUba1XtCQvvG4VPpD0DpXYQHolm-NfDhfyB0cvIbF69CHR0gvSADiEd61tgbuKK_0KBucylvfMMdujVfLVbJZyrP1rgwiG894WXrp2nnuVw0VA5-EF8cOZeU6qcK9ib4PW5TNxIf-olEUN9nSIKLacNn_8VuY-oC75YKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d014ea48.mp4?token=vEgx6x5DuxJr7E2dlA574uGQBwQrbHaNnVs4v3jKKKORhPv64PwSs21xWDL13f4TjQxGHEBNBlyqVZrPJrDULmt5mL3L3hz7EC3fQpgH_Bek-ltTWOfN4VrIojMt1n_NF5Jt5okaZz-3leYUOdr6cGQsgVSXJ7yzxCnu3hpy7t8n4YQv9kUba1XtCQvvG4VPpD0DpXYQHolm-NfDhfyB0cvIbF69CHR0gvSADiEd61tgbuKK_0KBucylvfMMdujVfLVbJZyrP1rgwiG894WXrp2nnuVw0VA5-EF8cOZeU6qcK9ib4PW5TNxIf-olEUN9nSIKLacNn_8VuY-oC75YKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین بد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80312" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80311">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg1xdwYTPbGTGRQAJEwN3d4K85n6N2jXHuG2DfCr466YWP0FoTPwR10dlpNxvkmg1l3kjZ4Z0N-Mk8zpOYXT8MmWYqye2z_cyNITTJMpgqc8fSGQ-glj-LaEwmDpgt_SvwYRLBCOLmH0DYAVIoIIidu2SVi4bXlL-IduR0wxMaKEf9-VCZkV-JacezUg31PsCUhGqkvGkOBfmSnVkFE8vqaPRSS6L1f1o5rHjIG1MhR4Tj9WQ_Naa2k4daw0Ysec2WpqckTAUECURoZy8k7wzn-8pUpiyQhcs7XocomEwVvunboZxsLQSgC7KWvYJ97SMm9lzpH8AhGkfLUqAgkGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال باز استوری گذاشت، هر چی دارید ببندید رو صعود فرانسه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80311" target="_blank">📅 19:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80310">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هرچی دارید بزنید رو صعود اسپانیا به فینال جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80310" target="_blank">📅 19:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80309">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بر اساس تحلیل های بخش نظامی سازمان فان هیپ هاپ، در موج های بعدی تهران، سمنان، کرج، مشهد، اصفهان و تبریز به شهرهای هدف حملات آمریکایی در ایران اضافه خواهند شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80309" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80308">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بنظرتون با پنج درصد شارژ میشه ۷۰ دقیقه دووم اورد؟</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80308" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80307">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=YZXp4Mxink5UMPvO_KHKfTbCF2W9IiooiBHS5JTH4p-ipBOxBVCEKp-OeM6wDj68cfpynpBOuMEuz9Z3mTeJs2FtTiHLM-6kJizwFURboEguUhKc7U6AqJZBTaFf50h0Q8f2g5CU8WaXfJmh8ombMzZxGBTbggmVWWGm8TER8JUOctrVWtHh177KI1xzEIv97ZPF-zYm4pJjS1DSOCDdmFPsWF_vFj6s4rfJ14MOg5aM9bphwNC44_E1mzAvYs-ik1E-RsoUw8_HNrxuiwcsT6w-a0ufmWzDsxK8z5z4MEu_GY3EwCK7kkEn8ZLlwjIPZX-mbch0db6hIXZ2e-MIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49901ac45.mp4?token=YZXp4Mxink5UMPvO_KHKfTbCF2W9IiooiBHS5JTH4p-ipBOxBVCEKp-OeM6wDj68cfpynpBOuMEuz9Z3mTeJs2FtTiHLM-6kJizwFURboEguUhKc7U6AqJZBTaFf50h0Q8f2g5CU8WaXfJmh8ombMzZxGBTbggmVWWGm8TER8JUOctrVWtHh177KI1xzEIv97ZPF-zYm4pJjS1DSOCDdmFPsWF_vFj6s4rfJ14MOg5aM9bphwNC44_E1mzAvYs-ik1E-RsoUw8_HNrxuiwcsT6w-a0ufmWzDsxK8z5z4MEu_GY3EwCK7kkEn8ZLlwjIPZX-mbch0db6hIXZ2e-MIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش لطفا نخون دیگه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80307" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80306">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">میگن پرستاران و کادر درمان در شیراز و یزد دست به اعتراض زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80306" target="_blank">📅 18:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80304">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YVTu0dF_pxX8bSTduacDbDaRabGF1GeN9pq6QDA1iuOTHB16RPVrsn3F0phhrbdj3h5fwss8cwAzxrv_eSuSW2meCHJcWkUYY2B0tBtVfqfx4gtLHEuGixWoZwr7XLzeXurYVG3Y_Q7gvAeWubMehPCt249VOIXUq4LEj6x4jlq1X5YC0VuGlQkuGCuB2TrJCfo-FdADe72bdVxK_o-s5w0-9b7XjgFRt7cNzI7BIgLxp7NxF7HEkcQyhbcgo0V4kWjEjrBHkqI83JqHTWv4SZS1PWrp2A68AkdJLbYQwztdbwPKStvrnJAQBX2AbAG5-MybIX7h_y2Fs3F6HUe6BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_VzBZuxDR-HNKralTniOJIM-xxTq7hDJyJxIqzuejCbizKdX70-WbxizBcDxrBu1GY-xWwaxKYztrUg9M5kFR0Xj91AOc6YgCAcSsKotBip0oLff2E1K_XmKoFjtcZUsPnLKkY42j2qVojXRSh8fKvd1ibc_fIqB3ZsQfEyQF4xc_PqdVHDRftKycz2-gF2KJhSNZSxEtfXe64q6_9AOktgXb3YzR_u-w_OhnXnsCi9qAq4ODnCRw98VIGRzyih4Jpu96pk3sUQ0ul7rH-GrXekRAO3aBlqX3C9Cxqe-0vZd55sZHhupZuPPs437PgJHLXH0c4mhbsHGxwkPTs5Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنیفر لوپز ۵۶ ساله.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80304" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80303">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9XBw5_y5IBxiEYrap4NQIJfanxZ2ZacUvFwqMv2Kspc8IZ3UbVOwRpXxaFGtZpxymjnmqmXU_KIu76pp4IbZRZqkNt34RHdav4o9Vxo61WIvi517-9V8PbODqs_IFtGnfTy6w3CeC9glu_gIuffZwnONGzOzUwBzMOm1dKHn3bXpIpE2mL8ljyNwRIYMQ3zXCdSoLrvYWvYFWsfBoRWB-Sj_OZXe1NLy048wF3bWlHuq1VxPgqhY_NHb4H7YL2ltgEduoAdpFoDCW7h8sEstaOBd48AsODGMA-_4MKcKiy3EyOvSPgAKGFWJAzBbSe4_2u1HygN609uM1p_RmA54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g23
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80303" target="_blank">📅 18:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80302">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPFgXhX4AxJ4J6xCDn0rCGFS_GDu_bTFnbvgIdmggzYovgDLC9qp-l8LldJZ1B3GqwPotL-Mriis_Wh2dH853h66MfsCgMKc3gVacQSk1iJ5oMpJq1iBUWrWtcJe9Me3rpLGLCz3sOWcbbl0LPOxKt7ZrsRmA11SZCum14z53n7zK66c_PaVISvlY1JbH9Cqd8cUYnayJ_THnNksfSTrkXupQ9MsUQ-mWBXJ10DTCCLHv4JF4kLqmB1eVZ16y9qTZ8hts-cxsWR6sM_EBzMJRU3-VH3BdyTCmdUK3gN5hwO7JcpJiQFmb_DCG9UuCMfO7iCgpvXp9SZ40M4XhxMIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80302" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80301">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxoAdfuMVQqDXBg6Id8QESouMATWPGMwvGTWqpGBfAWrIwyoYElenmI5FFO47HBfBLXUrGKl7TPtGT5PECtCFYikd5rY4juU_mfAXawGYsFGo4IvfuOj43Gz08mta3a9Np9MMkcUvvnz51Kr8eOM2DATrNB5HBaC6Ya7k8C2dGUZ879zIrc46zAyuVSfWdD8fqo0rmNL3t_J3Kq9QA9NTClcWQsgGgarsi8N5qkhn6sk8U6MgH6D-m6E5RyLg404neJQRv0HInPQCWkPplZVjy0u4Al18RgxfP9JUzCmdRb52yh7niYJdX37Q6MrmzgkbRUl1B_-hzLHFv7m24ReSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80301" target="_blank">📅 16:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80300">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoW_AGvWTCJ0B00NG7bZnH7OCBdyvx8mVwn8jGaygHQjvjbtMdizEtv8HHXGi2Eip8HRlGpbx1nR24aoWeUgeGAIdEpMxLV01fMqjfRxzeU5FKEE8TQkBIvJ-TW24s5L9_t7ppJjBuawXrIsR3qryIhGHiiOKDZoxvr04OE9l8IYmXvopJ7QBUj24XbY3h2aEfgMtBCi4Z7m1tLjjgna8aTz0Cmjm0mJ_Z_UgtaRcwmSQldHJtdpPk3ywGjOf-twQ3xQNv5Sek2Ql1ZLt2kYnkksKOc-rldO3blXm4L5jkDgSwqZG7cK3RNn86fcfA1QItZsfy_jWHRvDdBpe5tNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80300" target="_blank">📅 15:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80298">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKu-Z2pEgxmkw0ohrEH6r4spxvzPSR5Qhhpyv1PbC3JsZWMyL_9PBqlQ85npx6VaQt_JbvAxyQgw68nbENZ4Y8h_v-BGDOWLJiNvvhqrxNUWrdfovDV8Kcphm-yOdQ3D7WyIqutT2lz_BwW7nRVStWZ8Z2_NvNV-Xuke4DBJUF_ag_mPvEPZNmRpXe9poqq0RUkQrvKOmDBus81OvylBxFCvPAUhKil3m1yFa3lmDkadLvjftoy8kLtz_5YbUIIGHg-Y2syYzjFmKWxKEunPHIEPx435xeg-5-FKTqnMe3IHp6agyt93CLH9ITfpPwRQoTrQfDsKn6CDA0la6hCctA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WDU_BDWr5dtifEnFiKiDbqWqIBUApSiYghohhsvfmxDfyQNdk-8uo0RNDrGBtIBUMMYIgaABiufdITi1Q8KT4h451Mz3R0WGkvu-GzkKJoALIkptslu5md2lS8Reeu1w541FhgfwmMpzH7vvCdXt1zXEQSZgnM-eQshax9_LEYPDCNIc0u_F4RJE-8wNccwc6sd8VcaJkCvaN4HJXdTSXaddW1tuNCciwKZvBRxUHmhQ4go44lCRkIQ5D9Uf76mLHYoKz_g1Vatu1LBWx47mFBkiHB3Q6371hdEufNJ5_C_C79dd0yuKli9HPxZ3PY1L7KLfAI9Y9TolupQjOeFEYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80298" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80297">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80297" target="_blank">📅 14:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امتحان ادبیات امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/80296" target="_blank">📅 14:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان سکته میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80294" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80293" target="_blank">📅 14:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">چه فشاری شد حاجی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80292" target="_blank">📅 14:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz57XnwAdbT1VpwLzA5PzL3FG5OdVVD9YgSXqmcfxdBf0DIKd3cki_OoVoF7jyXhcTv4pkr1aXDMAdi0DEdR_dQGFY7AUff7Xi9DhVcMhNY-zmzUZC9K5qbCiU-61LiBOmAce7JhaUyAs-1vE-QXNeRQtwtaDEfLbNCjzFnIK4qWQSN9aXf2tETdq3FhbtwHVKuE2KPn65UN7deuAbD9MigyVDEpX8PKiiaaj65awhgI5mFlNUO5k2S_435BzDlSCcg3qCeDb3D7tMT6mnVUYgMP-kjOfj0_9K2-hobtDU8YCxbpby5SwodjX_6qhy5bjF_RGl8yAVpc43KxliNmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Shoti ke vinak az chateah ba kagan pakhsh karde.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80291" target="_blank">📅 14:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80290" target="_blank">📅 13:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پسر دوش آب سرد بگیر
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80289" target="_blank">📅 13:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80288">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مامان عمو پورنگ درگذشت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80288" target="_blank">📅 13:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80287">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Young Arash)</strong></div>
<div class="tg-text">امروز روز فلانه و کیرخر‌.
@FuunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80287" target="_blank">📅 13:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80286">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجار دوباره در جنوب برای ترور مجدد چرسی در جبران ترور ناموفق قبلی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80286" target="_blank">📅 12:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80285">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80285" target="_blank">📅 12:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80284">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80284" target="_blank">📅 12:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80283">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80283" target="_blank">📅 12:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80280">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا ویناک که گوز کونی نیست ولی همه این سلبریتیایی که دارید ازشون دفاع میکنید وقتی ایران بودن خایمال بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80280" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80275">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a2ctIhy5y0V3uBvDf99pMkbX1AHt0twPQdu75ZmSzq5lLMpw8sqmSeoC_BL0lXIYDRGUIFxM0UVb652vPNx37R_fYlWBNqCwu1PB5ABB41YhfxlSQAG4GMzVCiI0eg8R_1FiBdz_tyCbJrloxKTgJCcxJktNk48CyXhKTbvy_rAsS4609bhyixP3kztCIzPNwj9qgDA9O8T0Hv8NDtdUVZGk2Vdo9Q86wVopv_veaRfFQYGE9ana272cFw5KSw6-DqvzjAvQ53524Of2y3fVe7oP4RdgkwTmMAzudtqxSHFrzLihcP_yfAFYq65N4pWFNvMW6CpqdgMMvocdXpCevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gWLy8sepRsClU0qwShwNMVdlfI2iK2cZC4tlxOnCNa4yTYJm-KFeeK4BP26z8IYFpweeqdSvSP45Y_4xETIkXjRSjaaWqHg_crntekBU5Nh_paLrTgWupPg3mVZ4JlGSteP5fdha2CmBw9LhhnqwHCjSyAsnV9wlPv48gdpoNiLDYT0Jjne9CJZLCsfVRWnIydgjUEPlnkyPjOvaJwAnJ6b4ahzItPnRxITl0wppIvgQBgHtsgiuDds_PAcxc38-CH-n9HH1aA0XYFlA6pSvJSdPJZYRGMfgderUg2LGSkV9abscH0olezLSVBR8BHuLh5ehAJdPlcgqKWCzzKnURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOtNrcMT86iXm25DOF3jIdEH0tATGX4d1qMhig1bwUauIt1PJQrqLaCEtKQ8KTxSc38dylPlUVkCO3YqHZ1VZdHYc7K-cwM93hpmfyTOSLJvfKB01YdR6Uf-bByVjegFC1MGldEUhk_6AVKvSiLsRpZCbhKuVg4hLmGdZWpqk5Z-mv0Q_Du1yNbx_gTofKqxFAarRa-MAnpCfSVSwOxkcVt_xaPv9qPnIrwp8joO4w1nWspust-jRRDGIDWFZKGib8R9naB-l87F14tlBwWi0eXz-pYCW3gUDll_Yi-SiZvTLQJSZwK6rTpYJ7_YxZhTm9ewpYgaTbaGv9Rh28g_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEPO-sHMhcWgBcj8w2dcdeBkNFQfTxXC2H00jM6K7U1mLDP-ip8dm9JiC5k_F154qn3_QIBxke8q49PCR_iNsLmXiRdLjaogLc2gD5u9bDt0yOGeDojK1BauHlhLD_KLTTqYYD3EoRJ0WX7q4Rv7c1G3EjRyQ-vgsyb3PSmpzrvdsuYIuRuceNpsdccXqdPMqOlEalKGnkM3lLhaTnaVbXnFyPDpCu8Zdpk2kpk7IJPacX-oNfvdZIQdgVg-oEPy38F7kRAOWeYRl5a9qZ0ocRPxkQGA0yQ90wBcLh_2jzATmsqVNNqoaaJa0JNK5eXEguRJ43hdxA9-BZMrxoEk8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rSjdSqQ6t6fix4ICA2TksOj5nbcmkIjSFlEDlXaVyaJ6wJKcKychDWDigJTkw3_byQw-Zx8H1PaQeSZfOa6VOEixf-8--iKMHRysu0hbcK614mSlSZRYZ-w1FDjx1-bKDh7UGxS07SlR2bUyo2eHn3H1WkiQmtQcUeS1YjLbF-P1GpVmugaUYPmDV-S6i4DfZWxqLi5saQey8eaPeqLAf7BPaax9aXse-5qNGRE6Z9PvgWwometrDL3p958zvKHn42pLfLxGet1-Mql1G8S8rkepIX2c79uCJhaaKUmZKMYjn_N-BiuaX9HymLnvKMiyiPss8Aj7MhfYG8Cf454M-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ویناک اینارم از ۴۰۱ گذاشته و میگه من اون موقع هم خایمال نبودم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80275" target="_blank">📅 11:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80274">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=jUdsPuueAguDdNByj3IdRjZl2UfS5VdZ7VQMIJgdywEZwFBdRtFwqs8gen9_c69tLTSsBU-UAccgsGun8Oqi7NmqloErHnuEb9FqypJGbzaP97wL4iTKGptRKZQ_WMAyxyhqWnM07yXUe0dw5w_roY4_iCtbRXHmzHgyySGlNyoU6hWDzv7FbE0pLqICbPScBjPB7s1D0ck5B4XR-wYRVkYGFwJeIRZevkxfmyvU7Nd2lYPXBMQlZGOg2_6o5y_HTGf_ysjixb2VUC-Q_kGmyiZKnxL_wL88pxf1kzG2Mg_e8ebSUgzLyo1AEaQIWL98_X3Bf1O58aaG-oTAeCQ4Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73eef393f7.mp4?token=jUdsPuueAguDdNByj3IdRjZl2UfS5VdZ7VQMIJgdywEZwFBdRtFwqs8gen9_c69tLTSsBU-UAccgsGun8Oqi7NmqloErHnuEb9FqypJGbzaP97wL4iTKGptRKZQ_WMAyxyhqWnM07yXUe0dw5w_roY4_iCtbRXHmzHgyySGlNyoU6hWDzv7FbE0pLqICbPScBjPB7s1D0ck5B4XR-wYRVkYGFwJeIRZevkxfmyvU7Nd2lYPXBMQlZGOg2_6o5y_HTGf_ysjixb2VUC-Q_kGmyiZKnxL_wL88pxf1kzG2Mg_e8ebSUgzLyo1AEaQIWL98_X3Bf1O58aaG-oTAeCQ4Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناک یه اجرا از دکی گذاشت چنلش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80274" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80273">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ollp2gCQZxXEGKJwg0gM7KALZHDnq_lH8mLmbAZ46taow8GoaVruX33RtVbh2SxysB7lXK9-QQppziHbnXoFU0rwHA_bDOg9w82uFRsdjmDtmsjYS0R575f0yTEpxy6CJK96-lkUD9jJrdEEHWvX97OkF6nirea4Fso_Rw4nkQlk-WKZOWePl7QtJHhwEz0kW1OB0NtOhPNwzGNgnqRK17SFMeL5IsPzDcaqqJ_waPxshHd9V4nf2GMKr4LV17FQE8HFsZpLlSf3g8FlwqekU4TLOKcH7ok9K8u3bgDlEI-yZ2Cn6aolUvuLL7SKvzZ2lyLdxSglIYtIC8-tglET7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🇪🇸
اسپانیا
🏆
نیمه‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
سه‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در دور قبل در یک دیدار جذاب، با نتیجه دو بر صفر مراکش را شکست داد.
- اسپانیا نیز در مرحله قبل موفق شد در یک دیدار نزدیک، بلژیک را با نتیجه دو بر یک شکست دهد.
- برنده این دیدار باید در فینال به مصاف برنده بازی انگلیس و آرژانتین برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و نزدیک بودن بازی، تساوی یا پیروزی خفیف فرانسه گزینه‌های مناسبی هستند.
🧠
وقتی بازی با فکر انجام شود، باختی وجود ندارد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80273" target="_blank">📅 11:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80272">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7MoRtQTeuNiBKwvYOIHhSDnQnO-08ZsmBZjkKvS8LJ-1A7Vju7VjTcGhobOcjctiMjYh_yNKUnHi45Jg0ujgYO5mFUzrtdUCQTe1dJZgKVcBhwY1FHuujq2yXCXx_6AeRanFDHG4rSKEEXdP6NnCKxkOH9bRJXhpCxZAvvBJ8hgSXojy9uTkin_BfI6x_-3OFQbE-jyRA0zCm3CtNazGmUXmC02sTppN8hZLLBPQgGDQeJRaOLWnHbVzi3ulAz0R-0Xg5MligdobxUmXgSG7xWCtoz1qnOQ2LmVgKmDgrNAd5GJ8434wAZ1cQNxjFv9Z2WfQjym94cKQbPS0vNf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهر لیندزی گراهام جانشین او شد
فرماندار کارولینای جنوبی هنری مک مستر، خواهر لیندزی گراهام، دارلین گراهام را به عنوان جایگزین او ، سناتور این ایالت منصوب کرد.
با توجه به پیروزی لیندزی گراهام در انتخابات مقدماتی،خواهرش یک دوره شش ساله کامل در سنای آمریکا خواهد بود.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80272" target="_blank">📅 10:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80271">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ دلقک از تنگه هرمز هم میخواد بیست درصد تعرفه بگیره.
سازمان دریانوردی بین المللی اومده گفته این نقض فاحش حقوق بشره.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80271" target="_blank">📅 08:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80270">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اسرائیل نیست خوب لانچرا رو کشیدن بیرونا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80270" target="_blank">📅 04:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80269">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الان که شما خوابید آقا آرش بیداره و موج دوم حملات آمریکا به جنوب هم شروع شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80269" target="_blank">📅 03:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80268">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نفت شق کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/80268" target="_blank">📅 02:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80267">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کنکوری های عزیز ایران بخوابید، کمک در راه نیست.
ترامپ: معتقدم دستیابی به توافق با ایران همچنان امکان‌پذیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/80267" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80266">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حالا که مجبورید امتحان بدید حداقل بخونید تا دوازده سال از عمرتون که اینطوری گذشت بگا نره و ی ثمره ای داشته باشه، با آرزوی موفقیت برای تک تک شما در امتحانات پیش رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/80266" target="_blank">📅 01:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80265">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">من که میدونم این سری هم جنگ نمیشه ولی نمیگم که دانش آموزا همچنان امیدوار بمونن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80265" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایرانم به رسم همیشه عربارو داره میکوبه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80264" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80263">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آمریکا هم یاد گرفته ها
دیگه جنگنده بلند نمیکنه هزینه الکی داشته باشه
یدفه صدتا راکت شلیک میکنه</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/80263" target="_blank">📅 01:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80262">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv1qpc41Fib2rxMejeaWWHum3fAbJHLZfDL6xRdbZ-Y7F1nHtj5naxHbQdLosUAJG8ctQVJq7A9VvHG8vWhqknFcEQly6G-Bv90rwseq5-Zo2UAevrk3IpghWshJp0EDgcOqyqWKbkodteF1V75aMwzTU6cNS3E6uap2lOP6C0ITpS3Iihwgndtu1cf2EMgI5x2BfAgAHLEzXVypwb0tXmwIiOStBobFLXj7lt2v5Ij_1gglL3o1TNcnFX8ME-kQ3OLzwDpn3WBlYXaBstOhDbVafoMNtAQT_Df60DxNY1jC41wZ3lid1-LGN2PtlAipWDAi3ttTRFjDcSrzwW502w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا موشک کم اورده داره لانچر پرت میکنه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/80262" target="_blank">📅 01:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80261">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17049dea80.mp4?token=NKTF4gxPlUogbN-nFZAtp24AcQba1yzeXu204A775qrxIBbijbTE5JVSCHEzOjnU8VJLUq0-O17lfa0oB8d3sIUoC8Yh24HL2q4K2-NKUt3sdjZ1Bygy4gwvaWTeOH-w-I-5JWg--zXGS_hybVSRoY2wKq64TXwZcPmaB0cQ9dEZH8OT733A8J8dRcBy84wXiaZ1Y1otPHjOvDtz2p5nZsBxZPD0XNPsdJQPR3GAJ_D1FsfOMPPEgGYKhuQ-jNdascgnM6hv9fsY1INzsfY6Nbxir629jGDGpZ5nAMaaOiYQIOlnnbT5f30dPpFXOU3ayMUfMWxHjuqqOQFn03WtIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17049dea80.mp4?token=NKTF4gxPlUogbN-nFZAtp24AcQba1yzeXu204A775qrxIBbijbTE5JVSCHEzOjnU8VJLUq0-O17lfa0oB8d3sIUoC8Yh24HL2q4K2-NKUt3sdjZ1Bygy4gwvaWTeOH-w-I-5JWg--zXGS_hybVSRoY2wKq64TXwZcPmaB0cQ9dEZH8OT733A8J8dRcBy84wXiaZ1Y1otPHjOvDtz2p5nZsBxZPD0XNPsdJQPR3GAJ_D1FsfOMPPEgGYKhuQ-jNdascgnM6hv9fsY1INzsfY6Nbxir629jGDGpZ5nAMaaOiYQIOlnnbT5f30dPpFXOU3ayMUfMWxHjuqqOQFn03WtIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت حملات از جنگ ۴۰ روزه بیشتر نباشه کمتر نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80261" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80260">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حداقل کشورو بسپارید به فلیک شاید فرجی شد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80260" target="_blank">📅 01:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80259">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">جدی بعنوان کشوری که یدونه پدافند درست حسابی هم نداره بیش از حد کیرگوزی میکنید پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80259" target="_blank">📅 00:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80258">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80258" target="_blank">📅 00:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80257">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTheMojoMan</strong></div>
<div class="tg-text">مایی که خونمون نزدیک اسکله س چی؟</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80257" target="_blank">📅 00:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80256">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اگه جنوب کشورید به هیچ وجه نزدیک اسکله و ساحل ها نشید، وضعیت خیلی کیریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80256" target="_blank">📅 00:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80255">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسم نمیارم، خط جنوبی کشور کامل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80255" target="_blank">📅 00:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80254">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">جم رو دارن میزنن</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80254" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80253">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مشهد زلزله شد، این جدیده</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/80253" target="_blank">📅 00:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80252">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAꭑır</strong></div>
<div class="tg-text">این‌که تکراریه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80252" target="_blank">📅 00:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80251">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چندتا انفجار تو بندرعباس</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80251" target="_blank">📅 00:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80250">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شروع شد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80250" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80249">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه لفظی بود که یه ابرقدرت هیچوقت بلوف نمیزنه، مرتیکه قمار باز تو معنای اونم رید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80249" target="_blank">📅 00:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80248">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حرفای ترامپ بوی "من همین الان یه تماس از ایران دریافت کردم که میخوان توافق کنند پس یه فرصت دو هفته ای بهشون میدم" میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/80248" target="_blank">📅 00:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80247">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: به ایرانی‌ ها اطلاع دهید که ما در راه هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80247" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80246">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سلام پنج گیگ کانفیگ فروشی با قیمت باورنکردنی هفتاد و سه میلیون تومن، تخفیف ویژه  مناسب پنج خریدار اول.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80246" target="_blank">📅 00:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80245">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حاجی پشمام این B2 که زدن قیمتش ۱ میلیارد دلاره.
@FuunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80245" target="_blank">📅 00:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80243">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Young Arash)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIncC30kFLkLPWUTwMoDBCNeMY068g7rk38MGMYGa-fO3ynvMcliyFdb5j2pJMCMHH_eKVXm99qeawkODFOUXpWFPYMMFc0OVf-gOBQueh_4WJS34xUyVItlfpiTf6RMH8_UpXomX6vt6SV1VPR36zaVTY2k8-1MTO8BmSId_eHap97tmNlIdomyg74adcR6GNqpwGjtnwsmJKYf3GY0Vkk589RbI0nLRg-Zy2QlsTTUbLOEIOMp6IRlPMI03kSJ8mWetNBzlBCOH4-0QCT5tK5h3_sXhvY6zLTbZnknS0ZJA-ny0ec6QLEaE1lFncSVgKisk8crQxerdhH5_KQqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی انگار باز داره جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/funhiphop/80243" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80242">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صدای جنگنده هایی که تو تهران میشنوید مال خودیه، خایه نکنید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80242" target="_blank">📅 23:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80241">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ: امشب و فردا به ایران حمله سختی خواهیم کرد.
یادداشت تفاهم یک آزمون بود و ایران به آن پایبند نبود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80241" target="_blank">📅 23:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80240">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدای جنگنده هایی که تو تهران میشنوید مال خودیه، خایه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/80240" target="_blank">📅 23:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">به مرینو نگید کانته آخرین جام جهانیشه</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80238" target="_blank">📅 23:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80237">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اوه اوه بیبی اومد   ترامپ:  امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت.  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/80237" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80236">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عباس عراقچی:
رئیس جمهور امریکا کاملاً درست می‌گوید هر کسی که از عبور ایمن و محافظت‌شده کشتی‌های تجاری از تنگه هرمز اطمینان حاصل کند باید برای این خدمات  پاداش دریافت کند ایران همیشه و در آینده نیز نگهبان تنگه هرمز خواهد بود البته بیست درصد مبلغ بسیار زیادی است ما منصفانه عمل خواهیم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/80236" target="_blank">📅 23:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80235">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=vP3I4t4chuMWp_E6dZHOwS5prYSFMsv9xKuBG9OOxRswh0BvX1ixBnOlXF6FAzfX6HpCyKucRujoBi5dI8hZvP5LCNI7ZiHsRbNBKX66DhfkEfdE5WoGRJYn73V5V3pta2nQbUaXD_t9pLyaLhxafqnMC_mnEgVmW_HYeHNaUL2eV-VzGPdTsM9VrTFxrznalH_irEKUKz9E9JW4OMorupEi2UYJUM_0PJN9GyumFw_tyc8OKeE5vM_rFv9WAkpHjNbBEt556DtdaqJrQbAQdJCvkUJUf7Xdc5rmuMDzN2hCykMTN5z_3Y4AvBkp1xu6ftjdbnHksh-ZbFsl0Tu0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=vP3I4t4chuMWp_E6dZHOwS5prYSFMsv9xKuBG9OOxRswh0BvX1ixBnOlXF6FAzfX6HpCyKucRujoBi5dI8hZvP5LCNI7ZiHsRbNBKX66DhfkEfdE5WoGRJYn73V5V3pta2nQbUaXD_t9pLyaLhxafqnMC_mnEgVmW_HYeHNaUL2eV-VzGPdTsM9VrTFxrznalH_irEKUKz9E9JW4OMorupEi2UYJUM_0PJN9GyumFw_tyc8OKeE5vM_rFv9WAkpHjNbBEt556DtdaqJrQbAQdJCvkUJUf7Xdc5rmuMDzN2hCykMTN5z_3Y4AvBkp1xu6ftjdbnHksh-ZbFsl0Tu0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">براورد میشه رژیم داره بالای یه میلیون نفر برای جنگ زمینی با قوی ترین ارتش دنیا اماده میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80235" target="_blank">📅 22:57 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
