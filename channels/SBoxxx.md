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
<img src="https://cdn4.telesco.pe/file/Cxwcb5h3xAUcTM3S3ZxSOXY_zDksSkslmAMShTJn8_MoJi6LrACJ5KgesmVPd1tZXy7MxtRrlcTtuLs0CZb5WTCr7G2-LUx87UnJk6lG7csZ_8ft9pR24cAcbEWPpAbwSMT82nGRFfBNzgnc33YJ2oFveBUKV8IXJOLQ-Re6DLgvy0yFFBgORy-L910On3sYG5oOLYdFzM2KkBQRu0aYwLqsgAJ1rgS65z43V5NVdKyJJbLeBTi6bfstVvsj476rJ-PBMUQhTuY6h2aVETq0lsAUV5ivXV98L4ySOikw8yUveEtZT8fCi08gHBK-x4Jh9-KE6lZrxY2dsFU_SoUFIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
<hr>

<div class="tg-post" id="msg-17545">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قالیباف:
آنها هرگز نمی‌توانند به تنهایی و به صورت ایزوله هر بخشی از ستون‌های محور مقاومت را بزنند</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/SBoxxx/17545" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17544">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گویا گروه‌های مسلح تجزیه طلب کردی با حزب الله طاق زده شده اند.</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SBoxxx/17544" target="_blank">📅 22:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17543">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نمیدانم که میزنیم یا نه اما میدانم اگر بزنیم آنها هم میزنند و بد هم میزنند</div>
<div class="tg-footer">👁️ 993 · <a href="https://t.me/SBoxxx/17543" target="_blank">📅 22:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17542">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خداوکیلی از دیوار هم صدا درمیاید از رییس جمهور مملکت نه!
بلند شو یک چیزی بگو مرد!</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SBoxxx/17542" target="_blank">📅 22:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17541">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فوری | محمد مخبر، مشاور رهبر ایران: به متجاوزان درسی خواهیم داد که پشیمان شوند.</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SBoxxx/17541" target="_blank">📅 22:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17540">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-poll">
<h4>📊 امشب:</h4>
<ul>
<li>✓ میزنیم!</li>
<li>✓ نمیزنیم!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/SBoxxx/17540" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17539">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SBoxxx/17539" target="_blank">📅 21:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17538">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ایران پیشنهادی از سوی دونالد ترامپ، رئیس‌جمهور ایالات متحده، مبنی بر آزادسازی وجوه مسدود شده ایران در ازای خودداری از پاسخ به اسرائیل را رد کرده و اعلام کرده است که انتقام خواهد گرفت.</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SBoxxx/17538" target="_blank">📅 21:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17537">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این مقر موساد در اربیل مثل درهای بهشت است
هیچ وقت تمام نمی شود</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SBoxxx/17537" target="_blank">📅 21:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17536">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مقر موساد در اربیل؟!</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/17536" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">محمدباقر ذوالقدر: لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد
پاسخ رزمندگان اسلام در پیش است. وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SBoxxx/17535" target="_blank">📅 21:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMHAiPn-LoGWpIz-juYbSOI-7kc3DUF6NvNUeZlTEn-sDqRehnIoWa3apfgUoVwkhtBi_jl1JiOM2cAWRVBfpBYyaVnpjcuxiuVEaSUFqa7RJx7YrjkZC05uFXizDzkSsxAnkQT0u99Tmv5sdpU-kw1S7sb7usaf4SHimjDpG2zZnOjKNgRxapsxGPg_iqdGsVeL3k5zRyzzf-N3PaBsNGv9Ll5vCZ3QL0JNqJX-oHydCoh8L9OjiQa4gG4uZVaXjGEXgi68BFNOCwiw6jPzKCW_XAdGCsa-i-4rggQyjepOSmVrSNVKu_VM5lYUNj9M49F0K9g4-wJ2-1W7sePf_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/17534" target="_blank">📅 21:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">«کانال ۱۳»: ترامپ با کلمات تند از جمله برخی ناسزاها به نتانیاهو حمله کرد</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/17533" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):  «انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.  ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/17532" target="_blank">📅 20:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">— سرلشکر علی عبداللهی، فرمانده ستاد کل نیروهای مسلح (ستاد مرکزی خاتم‌الانبیاء):
«انگشتان ما روی ماشه است و آماده شلیک به دشمن هستیم.
ما منتظر کوچک‌ترین اشتباه از سوی دشمن هستیم تا به آن‌ها درسی بدهیم که هرگز فراموش نخواهند کرد».</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/17531" target="_blank">📅 20:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اصابت موشک حزب‌الله به شهرک کریات شمونه
منابع خبری متعلق به شهرک‌نشینان اسراییلی از اصابت حداقل یک فروند موشک به شهرک کریات شمونه در شمال اسراییل خبر دادند.</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SBoxxx/17530" target="_blank">📅 20:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/17529" target="_blank">📅 20:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SBoxxx/17528" target="_blank">📅 20:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.  ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.  — شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/17527" target="_blank">📅 19:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17526">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">—رئیس‌جمهور آمریکا ترامپ می‌گوید که از ایران درخواست خواهد کرد پس از حملات اسرائیل در لبنان با حملات موشکی پاسخ ندهد.
ترامپ معتقد است که یک توافق‌نامه با ایران در عرض دو تا سه ساعت آینده امضا خواهد شد.
— شبکه فاکس نیوز</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/17526" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17525">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">آماده‌سازی حمله گسترده ایران به اسرائیل
اینتل واچ: یگان‌های هوافضا و دریایی جمهوری اسلامی ایران در حال آماده‌سازی یک حمله گسترده به اسرائیل هستند. بر اساس این اطلاعات، فرماندهان ایرانی از یک عملیات پنج‌مرحله‌ای با روندی تشدیدشونده سخن می‌گویند.</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SBoxxx/17525" target="_blank">📅 19:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17524">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ:  «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود،…</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SBoxxx/17524" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17523">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ:
«حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در یک روز ویژه که این‌قدر به توافق صلح با ایران نزدیک هستیم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در پاسخ به آن انجام شد، بسیار کوچک و بی‌اهمیت بود، هیچ‌کس آسیب ندیده بود، مجروح یا کشته نشده بود، و نباید این روند مهم را مختل کند.
ما بسیار به توافقی نزدیک هستیم که صلح را به منطقه از جمله لبنان خواهد آورد و همه طرف‌ها باید از اقدام خودداری کنند.
نباید حملات بیشتری از سوی اسرائیل در هیچ‌کجای لبنان انجام شود، اما همچنین نباید حملات بیشتری از سوی هیچ طرف دیگری از جمله حزب‌الله علیه اسرائیل صورت گیرد.
این می‌تواند آغاز یک صلح طولانی و زیبا باشد، بیایید آن را خراب نکنیم</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17523" target="_blank">📅 18:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17522">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">طبق گزارش خبرگزاری فارس، منبعی نزدیک به
تیم مذاکره‌کننده ایرانی، تنها چند ساعت پیش از حمله اسرائیل به ضاحیه، فاش کرد که تیم میانجی‌گری قطر در حال حاضر در تهران حضور دارد و بندهای مورد نظر ایران و جزئیات مشخص را به طرف مقابل منتقل می‌کند.
این منبع تأکید کرد که هیچ چیز نهایی نشده است و فرآیند مذاکره را دارای فراز و نشیب‌های قابل توجه توصیف کرد و بر این نکته تأکید ورزید که شرط بنیادین ایران این است که تمام ملاحظات آن در هر توافق نهایی به طور کامل منعکس شود.
این منبع افزود که حتی اگر تمام دیدگاه‌های ایران گنجانده شود، در زمانی که دونالد ترامپ اعلام کرده است، هیچ توافقی امضا نخواهد شد. این اظهارات پیش از حملات اسرائیل به ضاحیه بیان شد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/17522" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17521">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش اسرائیل برای احتمال آتش‌باری به سمت اسرائیل در ساعات آینده آماده می‌شود</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/17521" target="_blank">📅 17:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17520">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مرندی :
فعلاً مذاکره دیگری در کار نخواهد بود.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/17520" target="_blank">📅 17:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17519">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">معاون قرارگاه خاتم الانبیاء گفته ایران به حمله اسراییل به ضاحیه پاسخ خواهدداد</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17519" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17518">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">برخی منابع نظامی نویس ایرانی:
به نظر می رسد فرماندهی موشکی هوافضا در حال آماده سازی یک حمله گسترده تر از عملیات "اخطار" و "نصر" می باشد.
- اگر در سایر موارد مسئله ای دخیل لغو عملیات نشود، شاهد شلیک از مرکز و غرب کشور خواهیم بود.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17518" target="_blank">📅 16:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17517">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17517" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17516">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترور نعیم قاسم شایعه است.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17516" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17515">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قالیباف :
تجاوز صهیونیستها به ضاحیه بار دیگر نشان داد که آمریکا یا اراده عمل به تعهدات خود را یا توانایی آن را ندارد
با چراغ سبز نشان دادن به رژیم، نمیتوانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب، دیگر کهنه شده است.
اگر اراده و توانایی عمل به تعهدات خود را ندارید، صحبت از ادامه این مسیر به سادگی ممکن نیست.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17515" target="_blank">📅 16:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17514">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تلویزیون ایران به نقل از مسئول سازمان مدیریت تنگه هرمز در خلیج فارس: تنگه هرمز تا اطلاع ثانوی بسته است و اجازه ورود یا خروج به هیچ کشتی خارجی داده نمی‌شود</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17514" target="_blank">📅 15:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17513">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نیم ساعت پس از حمله در بیروت، گزارش شده که یک عملیات هدفمند دیگر انجام شده و این بار در شهر صور</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/17513" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17512">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17512" target="_blank">📅 14:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17511">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کارشناس صداوسیما:  با ما بازی کردند!</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17511" target="_blank">📅 14:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17510">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=hfExn4gxD3LFqBJdslPLlq6hB0Fqv4e6s50bTjv__AyIb2ryYy97GTCJ5LGU2warwV11BSF-TlyAhCFbNPH-VlnPMuhgEO3IPpMrYvNGxHgWeXAVaKkMzMivqLbJEp3HBRyfXvspKdyo4tPMYlIbtEk5dSxx95Mi9-U2K6DcRYRSlECW4FbjsFmaGVqk6KhryBAsq6a_WluhhUqVn0ScVoptupCfiOg4PpFOjsJppZ_MDQRSi4vQbjKWO-ScNnCWv9wbVEklQ3FZT00_G1bm8wfr2upg-r-JCkGl0INGgqn2GQyOdFXPI4Lh1pIGHsXbiyAoV_Xfw9TjG-_bCGJ5SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c773de9e0e.mp4?token=hfExn4gxD3LFqBJdslPLlq6hB0Fqv4e6s50bTjv__AyIb2ryYy97GTCJ5LGU2warwV11BSF-TlyAhCFbNPH-VlnPMuhgEO3IPpMrYvNGxHgWeXAVaKkMzMivqLbJEp3HBRyfXvspKdyo4tPMYlIbtEk5dSxx95Mi9-U2K6DcRYRSlECW4FbjsFmaGVqk6KhryBAsq6a_WluhhUqVn0ScVoptupCfiOg4PpFOjsJppZ_MDQRSi4vQbjKWO-ScNnCWv9wbVEklQ3FZT00_G1bm8wfr2upg-r-JCkGl0INGgqn2GQyOdFXPI4Lh1pIGHsXbiyAoV_Xfw9TjG-_bCGJ5SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17510" target="_blank">📅 14:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17509">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/864badacb8.mp4?token=sWWOal4LRhlZU7edbR9E0VmLAGwWer3V6wwr0AG_acNCQyB49wimz2jVimHiEmbFMX--V9dbW2UlT342rcs_5GzRMQLHCwWNnWIBoB9Oz5e00C_4fIr_4nh-f_G1TuYZa4u7592sOUKDUr9WWB6WQX3rDbB8dqjLJfUy0udRNKpLNbs9hABI3Fju95JJL27S8HqQlqfg8QwUopP0g22VBf5PvCyNy3KZRIr_xgKn6B3Nm2T2Yyz4CJDhNo3LnH7AJVtk-CWBMTTcbsv-C3PEB2bSq676CjF4QYOwd6MmeArC9wJbTwUxWheYNvDs4Zt9gdMekDbLtjZStD__EKWtbFNWJZBGjHFFjJYPnji9niT8EZ-gFnGA9KiPhDWXnOEdqaBo98fDpIeiS2DvFVPyTgdZK-2IEKWq5BM2Rm0f4j2yx3tBAuR-kXSyKQxL3uDuep2_dBvOJ4iMuOGHU-18Mf8nlw-MPSoSZcEOnYYm5VXET_dYh6FSk27A2Q28o1Faru8mxcS2FjwonL5uA3cV5TsHfq28ezbVoON0OxTtggXDdmck9JPISi78Xpgfsv4yC5EDhZzn8Y8RVq_5DUtWkc56l3PJ8aVx8m7-fLO-i4Ju0JPD-PfF0VTBZ6DiLYFg5OcT4049tl6EU0CxWAa0DHY_gGCZbFkyWeJnxLSSqaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/864badacb8.mp4?token=sWWOal4LRhlZU7edbR9E0VmLAGwWer3V6wwr0AG_acNCQyB49wimz2jVimHiEmbFMX--V9dbW2UlT342rcs_5GzRMQLHCwWNnWIBoB9Oz5e00C_4fIr_4nh-f_G1TuYZa4u7592sOUKDUr9WWB6WQX3rDbB8dqjLJfUy0udRNKpLNbs9hABI3Fju95JJL27S8HqQlqfg8QwUopP0g22VBf5PvCyNy3KZRIr_xgKn6B3Nm2T2Yyz4CJDhNo3LnH7AJVtk-CWBMTTcbsv-C3PEB2bSq676CjF4QYOwd6MmeArC9wJbTwUxWheYNvDs4Zt9gdMekDbLtjZStD__EKWtbFNWJZBGjHFFjJYPnji9niT8EZ-gFnGA9KiPhDWXnOEdqaBo98fDpIeiS2DvFVPyTgdZK-2IEKWq5BM2Rm0f4j2yx3tBAuR-kXSyKQxL3uDuep2_dBvOJ4iMuOGHU-18Mf8nlw-MPSoSZcEOnYYm5VXET_dYh6FSk27A2Q28o1Faru8mxcS2FjwonL5uA3cV5TsHfq28ezbVoON0OxTtggXDdmck9JPISi78Xpgfsv4yC5EDhZzn8Y8RVq_5DUtWkc56l3PJ8aVx8m7-fLO-i4Ju0JPD-PfF0VTBZ6DiLYFg5OcT4049tl6EU0CxWAa0DHY_gGCZbFkyWeJnxLSSqaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی اسرائیلی ها از لحظه حمله به ساختمانی که ادعا می کنند ستاد برنامه ریزی عملیاتی حزب الله بوده است</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17509" target="_blank">📅 14:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17508">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :  ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17508" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17507">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">از بندهای درخشان توافقنامه حاج عباس :
ایالات متحده موافقت می‌کند تا زمان دستیابی به توافق نهایی، تحریم‌های جدیدی علیه ایران اعمال نکند!</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/17507" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17506">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این مواضع ضد و نقیض تعریف همان موج کذایی 4 است.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SBoxxx/17506" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17505">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">العربی الجدید: تهران توافق را تأیید نکرده!
در پی سفر امروز هیئتی قطری به تهران برای گفت‌وگو در مورد یادداشت تفاهم، رسانه قطری العربی الجدید ادعا کرده که
ایران همچنان ملاحظاتی در مورد این متن یادداشت تفاهم دارد و هنوز تأیید نهایی خود را برای این توافق اعلام نکرده است.
العربی الجدید به نقل از یک منبع آگاه ایرانی نوشت که این منبع ا
حتمال امضای توافق در روز یکشنبه را منتفی دانسته
و تصریح کرده که همچنان گفت‌وگوها در مورد توافق در داخل ایران ادامه دارد و
موضوع به صورت کامل حل و فصل نشده است.
این منبع در عین حال تأکید کرده که ممکن است امروز توافق نهایی شود و تهران امروز تأیید نهایی خود را اعلام کند.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17505" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17504">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگر نتانیاهو بخواهد تسلیم این توافق بشود (با این فرض که اساساً چنین توافقی وجود داشته باشد و امضا بشود یکشنبه)، عملاً سند مرگ سیاسی خود را امضاء کرد و سپس باید ریسک دادگاهی شدن و زندان را هم بپذیرد.  اما میدانید که نتانیاهو سرسخت و سمج است و بعید است به چنین…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/17504" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17503">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsAlyuvBXj2JhtxMe_ghMwlGgPnsVlbX2xD1M6C0QeeBe4lIViE026lVgs_tDtv3CNE-lwAt1defUDpu1FWlf1FJPa5KhFusFc6Xo1xKATG9PBaVUicilgkZ4301ck4wsxUzW3SHS8uDS1l9Y9o1IWdSWIx4LJv5WH6sAVUIl-2e54TXioRHa5tM2vSs5NSF_rFpUooFR8yD--wSkUVhXpYEwsLlLZft6C8oP6LGItd2Werpp74VOud3SNM2T8bNfS_UVLZf83XEzAguaBHhCtFetU2bWyzr6LWx4vrSop92zZCZud1IaF57KmbjDr1pyCN35nTCbbBqkn939Q_JvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/17503" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17502">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت!</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SBoxxx/17502" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17501">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1668556cde.mp4?token=G8v_vjHYCWBcOWEmihkYzonraM8ot9eOtGL4lqaJ_5-Uzb2yiZUlqYgQffpQ7oPOh8vN5Zq-mfC1-tyEkTUGaY7MZEh-2Jppk7Ct2di6Ec_TishblXXk5XwLBBcjUsiUU1of0PWeOX1f3M_RJqYaOhj24zPA58kvo9L0IryE6DovDTTkEpoZG2S9gwMf34BeTKyAKHKMCBfvfjadyoY3s8GDLHj7h_g-vio_MLuIRi9cH5pPhHxRlPNY4srOVh-eADbsrV9fCwaxTIT0M6FM3iSWzxnce3AhaYE1_9F7ZzO3j2B0naHjT-4v9mMaUF207FAm3Z_XGivpMCmr3y_NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوبی است.  باید تدریجاً هرات از هر جهت در بوم ایران ادغام بشود.  چرا وقتی نظم مسلط فروپاشیده و همه دنبال گسترش مرزهای خود هستند ما بنشینیم و به مرزهای جعلی استعمارساخته احترام بگذاریم؟!  هرات؛ نگینی بود که توسط ناصرالدین شاه حمال از دست رفت و هیچ قرابتی…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/17501" target="_blank">📅 13:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17500">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfDkDDKc6c1gXOc3w_0pjnkEvgN8t9JuPLVF1VMCmSuz1jwt2nHWqjLf16K-RwygW-K47kAsX5hrrhZYujPcL7lpBJCmr7EplHSuKFOboRGkInn__SiBvd3rCPkVB4D57xghvMQcIifUuiXtnkFHcYFkY0sW5Zdch-q3io3688_BIpbsfbarb_RPNBpm2oxhPrZEmbNgPPyzdWpjRiPrlmAcZ22H2pdrj-XYxdjwfSXdC8MeToj04Vrg_yM2HwxdAf7CycV1jY2Kq5VpQpBupYsXbiV2Qco44edbGgYCGkfiBYQJRHpqz_xxb2I9eLk2H5rQL2OktZn19XRmlwvUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز هشتادمین زادروز این نکبت است.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17500" target="_blank">📅 11:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17499">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe0qg6Kjoo7hYbBY3W7v1UZtX6LMcySHPiZ7p6sPeUs0IR6ufLp_fGYe2XObSvm6Zxby097xRF0pgXOFxpLgguwFOtEGVeLQdKxXNH_4uiTCaWoCwd7Oz3vkI2zNyJkr3zkTS5cEvWWGkTIWbDEJ_F4FTuFkarh-zJJ7jNpSMdv0dPBURKfoO2H0rchY4Uen9sah7wadXHX-He2n4x75tuKA5OPnKXsTw26VxwApAnLY0BvE7kQAmUlWJ1e5CA1AJqXtrNstD7KgROh-5VyZwAWnW5Xojf1gPOrU9wM8scoN1_YTDSB6WgKUFd6an28zRD935RLuKp0y3eukwOdBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنا به گفته دو منبع آگاه که با شبکه CNN گفت‌وگو کرده‌اند، عالی‌ترین فرمانده نظامی ایالات متحده اواخر ماه گذشته سفری محرمانه و فوری به مقر فرماندهی مرکزی آمریکا (سنتکام) در فلوریدا انجام داد تا به‌صورت حضوری در جریان طرح‌های ارتش آمریکا برای اعزام نیروهای زمینی به ایران و تصرف اورانیوم با غنای بالای این کشور قرار گیرد؛ ماده‌ای که مؤلفه اصلی و ضروری برای تولید یک سلاح هسته‌ای محسوب می‌شود.
این منابع گفتند جلسات توجیهی آن‌قدر فوری و حساس بودند که ژنرال دن کین، رئیس ستاد مشترک ارتش آمریکا، ناچار شد در ۱۹ مه نشست مقام‌های ارشد ناتو در بروکسل را ترک کرده و به سرعت از آن سوی اقیانوس اطلس به تامپا در ایالت فلوریدا بازگردد. به گفته منابع، سطح بالای این جلسات و فوریت آن‌ها نشان می‌دهد که دولت آمریکا تا چه اندازه به صدور مجوز برای این عملیات زمینی پرخطر نزدیک شده بود.
سخنگوی ستاد مشترک ارتش از اظهار نظر درباره تدارکات مربوط به یک عملیات احتمالی خودداری کرد.
یکی از منابع نیز گفت که ژنرال کین پس از آن، رئیس‌جمهور دونالد ترامپ را در جریان گزینه‌های موجود برای انجام چنین عملیاتی قرار داد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17499" target="_blank">📅 10:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17498">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تحلیل من همین است که ۳ هفته پیش ارائه شد و امشب یا فردا یک صوتی هم در این کانال قرار داده می شود.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/17498" target="_blank">📅 09:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17497">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOI-bkfOWhVm4I8nGUMLKc8oogLqA_JvmFIQsJF_wzpKmcS5Nedzxaqt66YWvPtSJe4uf4DY9n01J2RUVDUYetiZj7-sJloCmAeBTfMh2yd2Jl89DBh4IHkP8vkwYpXPHVDuXo8dUUhcjDyNpp4BfJ7EOq48XZZma1kjuHwrndiAJy9sHn9QnMqm7h1nCSxhrl8Z1iHs00sb1LMswXiV3IgdkwkiVY0kSjxs-jPazkovOppSPy8UGy-Q1EkOFNa29YkwPdyw2_JLpoSJva_bPU8yOb29PbBDmQHih5SQIfKgygWNCMBjgI_L0dk26dsYmiv8nymzZHvlFlEvWysdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام یک رادار آمریکایی در بحرین بعد از حمله موشکی-پهپادی سپاه چند روز پیش</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17497" target="_blank">📅 01:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17496">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">خدایا درگیری جانفدایان کف خیابان با جان برکفان ناجا را هم دیدیدم اما قهرمانی .... را نه!</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/17496" target="_blank">📅 01:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17495">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ایران تمام دارایی‌های اقتصادی مدیریت شده توسط ایلان ماسک را به لیست هدف خود اضافه کرده است و شرکت‌های ماسک را متهم می‌کند که در حملات دیروز ایالات متحده علیه ایران کمک کرده‌اند.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/17495" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17494">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwtuGrT42HJOamQSQ4UW-Lw7wV0sIl6xHFMObC4GWXwpjqYc1CQqOExntX9gqokAF18G4Yiar0yJKPN5XX04c0QV-ojEHfthQmjzO7Rw_hVBUnKvU_9Sn7qu1AvKRs74hyRfxZ5Be0y48FDHVrlkwpatLrX-naXjBeBem-fW-vxKbrIXVGfM6ZCzH7gtOL5FmOMulLo1qayCAcuQhicIM_1SiIJxRYZx9TuybpxHyO4-dWodYO8ZLincb2JRHZxGeXQESoBpp93QLxgXkj4TnDZnB2MCHnlMnII1HGyciykjYzRciL139sGPkKx_otjmtk-Dfn2tYDdNOd-49zHOog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا همه دارند به تنظیمات کارخانه برمیگردند!
ُسبحان الله!</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/17494" target="_blank">📅 00:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17493">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjYMfE5lJKH-s6axX3Yec8RAq8MgFCUsIR1oDRUi0JsG0RpyV-xrTfjurHebjbwROGd0BwG6hVZxedQUlVGElXWHAwlTi6z9P7FLVv4V8MXoJBLQPSLVFDFvl_VCkurd1yhHnk4uip0TLG0f9F4mhIzVI4QbASrOUIhdMcw5MgKfy3b345ACArNyUAnoCv-vm9aUpzOwQ59wdg1AWCYZnbXuQ-bIc0BgYtG03kmh1l5V45nMA4QaCxIuHER5HAqWV0m918ajmaPiWt_wiPpflVT7FgjJ3zuTJbd3sXQ-U4JyUc4o_cXC5wbh5WpIq2Ajwus01O_v1mRjZUcDNy_4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!  فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17493" target="_blank">📅 23:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17491">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/17491" target="_blank">📅 23:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17490">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به نظرم قیمت تن ماهی کرش کند!
فقط آقای طاهرزاده شخصا ۸۵ بسته بزرگ تن ماهی خریده بود!</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/17490" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17489">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کی بشود وعده باقر اجرا بشود از شر این وضعیت راحت بشویم</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/17489" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17488">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کار خدا را ببینید که پاکت زاده های بدافزار «بله» آمدند کانال مرا بستند حالا تلگرام آزاد شده و بعید نیست خود بله و روبیگا فیلتر شوند!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/17488" target="_blank">📅 22:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17487">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:  "هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17487" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17486">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سردار احمدرضا رادان، فرمانده کل نیروی انتظامی جمهوری اسلامی‌ایران:
"هرکسی که در تجمعات شبانه علیه وحدت ملی و مذاکرات شعار یا حرفی بزند، بعنوان تفرقه‌افکن با او برخورد خواهد شد."</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SBoxxx/17486" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17485">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شرایط جدیدتر اینطوری است که ما کشتی های هندی را که از ابتدای تنگه هرمز  می خواهند عبور می کنند میزنیم. در پاسخ، آمریکایی ها هم کشتی های هندی را می زنند که از انتهای تنگه هرمز به سمت دریای عمان می خواهند عبور کنند. ِ  این وسط، گاهی کشتی های غیرهندی هم هدف قرار…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/17485" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17484">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خیلی جالب است؛
ترامپ می‌گوید نه پولی می‌دهند نه عوارضی از تنگه هرمز اجازه می‌دهند و بعدا اورانیوم غنی شده را هم خواهندبرد یا نابود خواهندکرد
مقامات  ما میگویند هم پول میگیریم هم مدیریت تنگه هرمز با ماست و هم بحث هسته ای الان مطرح نیست!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/17484" target="_blank">📅 21:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17483">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17483" target="_blank">📅 21:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17482">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">منطقی هم هست؛ امضای الکترونیکی که دیگر حضور فیزیکی لازم ندارد.   بوگندوهای فاکستانی فقط دارند می روند شام مجانی بخورند لابد.</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/17482" target="_blank">📅 21:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17481">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فوری | ترامپ:
ما امیدواریم که عملیات به راحتی و به سرعت پیش برود. اگر این اتفاق نیفتد، ما یک جایگزین نهایی داریم که امیدواریم دیگر هرگز مجبور به استفاده از آن نشویم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/17481" target="_blank">📅 21:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17480">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!
کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17480" target="_blank">📅 20:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17479">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ:  «توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.  امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17479" target="_blank">📅 20:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ:
«توافق من با ایران دقیقاً برعکس برجام است؛ دیواری در برابر سلاح هسته‌ای! در واقع، آن‌ها دیگر نمی‌خواهند سلاح هسته‌ای داشته باشند و نخواهند داشت، چه از طریق خرید، توسعه یا هر شکل دیگری از تأمین.
امضای توافق برای فردا برنامه‌ریزی شده و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد شد».</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17478" target="_blank">📅 20:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17477">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⛔️
دولت ترامپ ، دسترسی به 2 مدل هوش مصنوعی آنتروپیک را برای کاربران غیرآمریکایی مسدود کرد</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17477" target="_blank">📅 19:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17476">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خدماتمان اینطوری است که کشتی هندی با ملوانان بنگلادشی متعلق به میلیاردر یونانی دارد راهش را می رود، بچه های ما به کاپیتان آن زنگ می زنند که یا بیا از نزدیکی سواحل ما رد شو یا ما ترتیبت را می دهیم بعد کشتی وارد آب های ما می شود و ما اسکورتش می کنیم تا بچه های…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17476" target="_blank">📅 19:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17475">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سخنگوی وزارت خارجه: باید هزینۀ خدماتی که در تنگۀ هرمز ارائه می‌شود را دریافت کنیم!</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17475" target="_blank">📅 19:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این طرح واقعاً بامزه است.  کشتی ها باید هزینه «امنیتی» برای دریانوردی در تنگه هرمز پرداخت کنند تا نیروی دریایی سپاه پاسداران از آنها در برابر حملات نیروی دریایی سپاه پاسداران مراقبت کند.  سبحان الله!</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17474" target="_blank">📅 18:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزارت امور خارجه ایران:  «تیم مذاکره‌کننده ما برنامه‌ای برای سفر به ژنو یا هر مکان دیگری در دو روز آینده ندارد».</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17473" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/17472" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/17471" target="_blank">📅 18:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/17470" target="_blank">📅 18:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPdyIgTrjGihqjbrRw2SmjMPtEJyrsopuUZNL4yWJDkPmnJv9iVRGD29LF3PRzOFBtwnQ7oa6exWIZ6SC0qx_ch54oBcBMe3F3PY9tBQwZSmf2_RSY-eEXWlDbekxzo2PHcCoJCI3L2pr3RITT8cLjVIvYUrtTmEllqjupdh7Q8Gu2hhH83v_jAX8G4ysS4ERldk7GK-tcIAVqNww37cQODyzbwkVftNKWrurNVvFazKp-51c0UujLghYl3x6oKOzfDc8Me21SGSCksT-75KGFjfawM29FcDxj-WjNwA33xiwvfZH4zB7H7RM--C5UnJoMkLJMNhttt6TdOvHdQx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله! جانفدایان یک پویش توییتری راه انداخته اند با هشتگ نمیپذیرم!
که اشاره دارد به برائت از ائتلاف قالیباف-ویتکاف!</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/17469" target="_blank">📅 18:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گویا یک ستون از ارتش اسراییل نیز به سمت صور در حرکت است.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/17468" target="_blank">📅 18:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SBoxxx/17467" target="_blank">📅 18:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYHoX1yHSlP9WL3vMSfsqd9avDISxU8PuIZl5JCNGbAbE_8Y-gXALGsruLHWsOgfWQBlOVH7Py7qZLJinUxOTVK0ldN0jv3500b5oamteLvrMi_8PTmykbPtj1g1sNe9ACHjYbT1EJGghLcV47qPgbzJ_6Gg20IPGlL-AIO09qWu9zTJDwmRp5ZTPj0WmVxxqUZMi7kTCnsPLpEWaXgz4gN03SpyoQrzoenYujLEST9625Sq_9v88sgw42fuGAOXQKBiSf4zIGsDe0G46H8cLnuQrkeMRv1VyHlRAo_M5dGpYwmAdlCgIrfJVzCF-3laudfmbSuCD7l9XX1w6bOeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت را دوباره بخوانید:  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  پس در واقع تنگه هرمز برای همه باز است جز خودمان؟!  سبحان الله این که عکس چیزی بود که میخواستیم!</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/17466" target="_blank">📅 18:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">وزیر امور خارجه پاکستان می‌گوید مراسم امضای الکترونیکی برای فردا برنامه‌ریزی شده است، زیرا مذاکرات ایالات متحده و ایران به مرحله نهایی خود وارد شده‌اند.</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17465" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TY8VdEVJID8KchwGK9-nzplg10GJr44oCwQDk47DqojvRSQhcq40Hf-HG55hd9hJaS83j9HuRqx5vql-ptT8Fj5VJj2587OsNj1uaUocupn5bQ3ppQ9brzg2Po2Cog_0A4Vi6fj-R6ztbwMim9O-9Fdcvswrq8NoEXMNLK2VFaa-fsEyu0aWmNeM3sYZj8ld4knvzAJx2PQvoHKIglRWqWizxEU6vbGzXKlBY6nijW5l6Tw8K14ZS2D2LZ5O7gFxjyFNoa0pAenBP_PZvkvh4685HgCpLtHGxfFo3Yxt5IxUlgSwJ030VX-3__uBZ2ZbM3JRpf-YhNjFyEntfmmUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه جنگنده اروپایی (FCAS) در آستانه فروپاشی!  پروژه سیستم جنگ هوایی آینده (FCAS)، که با هدف ساخت جنگنده نسل ششم اروپا و با همکاری فرانسه، آلمان و اسپانیا راه‌اندازی شد، اکنون در آستانه فروپاشی قرار دارد. این پروژه، که در سال ۲۰۱۷ توسط امانوئل مکرون و آنگلا…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/17464" target="_blank">📅 15:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">13 و 14 تیر: وداع در مصلای امام خمینی.
15 تیر: مراسم تشییع در تهران.
16 تیر: مراسم تشییع در قم.
18 تیر: تشییع در مشهد و تدفین در حرم امام رضا.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17463" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5j91D0rr1RSLfLqktIVXsvrDUPfGNaW_p2aSiKxHAqKtSCfsAPmvy8yYAjPUGUVYbRE7aFfGrgFgmvHbX69803GtqTu0r9Rbh0BFBkd3uB1JtbO741hOg8Osuq2Wl_TkIAFZvFDwcH-dmN7m8wkIs8a43mlVLpEP9NlF0K8quXH62a9kwNpPDMRNjtdooKjh1Jfk2JpPImlExxrqHOREaZt4MU_woINkqvHrtnblwjpDUrosTE9pc505d9D9Lhx8rw6oNArarTOopJdxXbhH5DOrGigyy-JVi0XTcWp7O7_EgCx24Tn4Q-nnqq1FmQC-ENCXhVJ2adLLXoRBvhJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در جنوب تنگه هرمز هدف قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/17462" target="_blank">📅 14:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صحبت های جاناتان پولارد — جاسوس معروف اسرائیلی که در آمریکا دستگیر و 30 سال زندانی شد — درباره جنگ بعدی اسرائیل با ترکیه و مصر و لزوم استفاده از سلاح های نامتعارف کشتار جمعی.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17461" target="_blank">📅 14:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=tsmZeKWtXt4VlqryKHH2tV8CTwQ5-h_op5Mu1FNxYM0wY38-2ZS4mmRZaBzOYr3gx_p8oginuMNxgR2QqoZykxSsRLRSSr8kOVh7nMZckDv-wHUIqYTiCeXkcfXsTo0Prmid9iybx8_fcqPnfrc6Gs3hsNhimi7xYEQXrtHjG062XgiYu-SAUknT9Ibqf2aliPr_bblUoMsbNWM9M8D0EuGy5kgtPbjBpq9YL2fgVLYuJlJqc_x14YRA_I5Y12ajvZkYwvzGrClbTjYMraTR29N4UNq2UMBohxLqLJUdE4bLTAM6SzAevAlSNsimgJ7TfNJbWjLQOiF0WZk63ufmZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cc2b3576.mp4?token=tsmZeKWtXt4VlqryKHH2tV8CTwQ5-h_op5Mu1FNxYM0wY38-2ZS4mmRZaBzOYr3gx_p8oginuMNxgR2QqoZykxSsRLRSSr8kOVh7nMZckDv-wHUIqYTiCeXkcfXsTo0Prmid9iybx8_fcqPnfrc6Gs3hsNhimi7xYEQXrtHjG062XgiYu-SAUknT9Ibqf2aliPr_bblUoMsbNWM9M8D0EuGy5kgtPbjBpq9YL2fgVLYuJlJqc_x14YRA_I5Y12ajvZkYwvzGrClbTjYMraTR29N4UNq2UMBohxLqLJUdE4bLTAM6SzAevAlSNsimgJ7TfNJbWjLQOiF0WZk63ufmZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای این جنگ لحظه شماری میکنم…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17460" target="_blank">📅 14:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ارتش لبنان در حال عقب نشینی از شهر نبطیه به سمت شمال لبنان است.</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/17459" target="_blank">📅 13:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صلح دوست ترین ارتش دنیا را لبنان دارد.  به محض نزدیک شدن جنگ، مرزها را ترک می‌کند.</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SBoxxx/17458" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtreEj21G88jULE-M28l6xc7COnrVBmxijrgVhJ0IoPRxqIADac5vaMQBRwWb2isC6tzt0aT5EbRDw_CsMa3Xh2CRQEvwJ3r6uYOYqXTzAyapUdb1IJlZKg07_btmjMhK2KWSsgIJn8xvJo1FwpzJx-1n88pj8Zi8s6YcHtrD8S9tqLbNOUV3r8oB_yzc-60OLa-I2QbEj7LQ5zn53-tDqtS1CiANlr4rivqi8RLi_-_vCcwjxKb79hXyW7awYvzjK75aBqea-0ev4shrn6RbGQZVeUvLMjyuYdBSaFs6OpTWWCfRnhb68IFsZuCiZhCr90ek3G8WZyLTCvP-z9ZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/17457" target="_blank">📅 13:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خدمات الکترونیکی در چهار بانک بزرگ ایران — بانک ملی ایران، بانک تجارت، بانک صادرات ایران و بانک توسعه صادرات ایران — از صبح امروز مختل شده است و این اختلال بر بانکداری موبایلی، بانکداری آنلاین، خودپردازها، پرداخت‌های کارت و سایر خدمات بانکی تأثیر گذاشته است.
گزارش‌ها حاکی از آن است که این اختلال ممکن است نتیجه یک حمله سایبری باشد، اگرچه مقامات ایرانی هنوز علت را تأیید نکرده‌اند.
— خبرگزاری فارس</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/17456" target="_blank">📅 13:41 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">در هر مقاله اش ۸ سوال از خودش میپرسد آخرش هم نتیجه ای می‌گیرد که معلوم نیست اساسا چه ربطی به سوال های بی پاسخ ش دارد</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17455" target="_blank">📅 12:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17454" target="_blank">📅 09:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">CNN
:
گزارش‌ها حاکی از آن است که ایران ممکن است زیرساخت‌های تونلی مرتبط با اورانیوم را تخریب کرده و به تله‌های انفجاری مجهز کرده باشد.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/17453" target="_blank">📅 09:28 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">— مقامات اسرائیلی به یدیوت آهرونوت گفتند:
«اگر حزب‌الله شهرهای شمالی را هدف قرار دهد، ما به ضاحیه بیرون ‌حمله خواهیم کرد و در آن نقطه، واکنش ایران را خواهیم دید.
اگر ایران در حالی که ضاحیه‌ را هدف قرار می‌دهیم به ما حمله کند، ما پاسخ خواهیم داد و اصل آتش بس در همه جبهه‌ها را نخواهیم پذیرفت».</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17452" target="_blank">📅 09:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینفوگرافیک سنتکام از وضعیت تنگه هرمز:  تنگه هرمز برای عبور و مرور باز است  • مسیرهای امنی برای عبور کشتی‌های تجاری از تنگه هرمز ایجاد شده است.  • این مسیرها برای همه کشتی‌هایی که محاصره علیه ایران را نقض نمی‌کنند، در دسترس است.  • صدها کشتی در دو ماه گذشته…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/17451" target="_blank">📅 09:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sT8a3ML58esIXDzsFSneWxbzNuxo-O2zSn2fDEJWVggISoBrCByBbVTCa_el11ZAOottbJpZLJjEZhmvhMka44iuJnydh3FfCsdltxWdT72xKTSMPyjXYVDN2bbbsNK9U8lXlRBkpiJ1moIGtoSO5m3EvedVKkaC57ej8MzirSRXq0Ntvo1L2zkLAfcm0EKwKIVxH0xRWexBt2jpn_0NFwob3S5TDNkE0yJifwhd-CefoL-IL4V1LgP2u60a_B7P6AdImOMUspD7-PbmpIiJ7RIIxZVta9mKr0k26lWI8oLAzj106weazQr2lBCq2lO1uUT68YZlOUF8f7MCrThQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی از دیشب تا کنون ۳ کشتی دیگر را منحرف کرده و از ورود به بنادر ایران منع کرده اند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/17450" target="_blank">📅 09:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB8hhpMcLMt4sAXokVE2feXDF8bJu0wYklBkV0ZwylCfsC0_NIqgoUuM_1-sQbfS-2fPO5bFQIWc_8ukKP0Me1rMFyXQaP-lESnmByASRqN-xT4qgexeV10lSwFbe3slfhrnMgpVH7KT8w4juVXJYHkAXYT3NuXt4A7mg1ZwO9qgdF0gYAGl8vXLszb65THdKvHCTx1cbW1YPFSL0TjW_b1-qHx3MPEeC1CXfSgYAfBlEE41_k13MNNQd5gOgyIGkz5l4nJUneDnNdjX3D34xYGU8xxPYUlsaiZ-qyXkNc37EHxvaoo0Go-Hy7iniK_NTzfwkzpHGaSynkNNdca8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای انفجار در تهران شنیده می شود</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17449" target="_blank">📅 03:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پس چه کسی پول ما را می دهد؟!</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17448" target="_blank">📅 01:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امارات متحده عربی اعلام کرد هیچ دارایی مسدود شده ایران آزاد، منتقل یا از طریق این کشور جابه‌جا نشده است</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/17447" target="_blank">📅 01:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17446" target="_blank">📅 00:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شلیک به سمت تنگه هرمز از سوی ایران!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/17445" target="_blank">📅 00:24 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
