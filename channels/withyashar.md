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
<img src="https://cdn4.telesco.pe/file/QH-zbGjjcljjsEvscO7RIcOD2BEuiev61JdkBIC55Rju-gozCDcJSxmzyxJ1k6PEKJYN50WcW-T0PVFpyZgByBfjQFTDFUdJyfDV97SMHVloOVx_xrYbLuzM6SgisUMQlUq-bKtEQJ5qlPLV3M4ciGO2ofTSdxqVzbWcNXuSdNAza36UIwC1dpFEb4IEzqN6AYmp6afnsli3w64G72UcNzXQQxgYUCe-hmoHBfKRuNR4NCDtDG09aSnqE_clHIBPO2ocoW8iTbwZfEewD1XIeqfJIdP6nKm8BJajOqSa5p7RjGz4pXt2gxzova-k3MtVAexrlnztXlFd3onkPXVumQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 441K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-21820">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taa-9yq-W-sVheBxbnQMkScQXcTl9xZoFfgQ0zJ7T_w29gXjSETn8sC4rs9ipiNYx_uwvBDimYB98eGwjZwT2mxBtvjUMnZGlDaVE9evtNkfUhmcQc54CCwubM_sbVCPFFA-4t8AHSpng7BergVLDIzw-Dd9xJOs0ibkA8Zr7pc8B8-h5jQJ9XQk7ddGjNbmusVFV-vflK9BlX6AvLJZ30EYd1ws4gNX61GhFi2PevQ4O4Mx_eCU72xD2lh9OYmr__beafBYFiF3Z_bWMVBJJjMnkHOzxAsPlx82GZuPJi36692mAz3JKaFq6IvwjWnJ5cigc7HILsT_kEOlRdYFZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه , عراقچی:
نتانیاهو با افتخار می‌گوید که موفق شده است دولت آمریکا را متقاعد کند تا به جای اسرائیل، علیه ایران جنگی را آغاز کند
. او در حالی که می‌خندد، درباره "تاثیر" خود بر ایالات متحده صحبت می‌کند، تاثیر ناشی از بیش از 1000 ساعت حضور در شبکه‌های تلویزیونی آن کشور. در عین حال، او با زبان انگلیسی، از رهبری ترامپ تمجید می‌کند.
او یک مار است.
@WarRoom</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/withyashar/21820" target="_blank">📅 12:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21819">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سخنگوی وزارت امور خارجه، کاظم دست کج غریب‌آبادی:
این اقدامات تهاجمی، پاسخ مناسبی را دریافت خواهند کرد.
باید حضور بیگانگان در این منطقه از بین برود، و آنها باید درس‌های جدی بگیرند تا از تکرار اقدامات تهاجمی خود علیه کشور ما خودداری کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/withyashar/21819" target="_blank">📅 11:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21818">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات آمریکایی:
نیروهای ما تنگه هرمز را تحت نظارت دارند و آماده‌اند تا به نیروهای ایرانی که امنیت کشتیرانی را تهدید می‌کنند، حمله کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/21818" target="_blank">📅 11:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21817">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اتاق جنگ با یاشار : رسانه‌ها به طرز عجیبی جدیداً قسمت صحبت‌های ترامپ که در مورد کشتار معترضان هست را حذف سیستماتیک می‌کنند. در صورت مشاهده رگباری گازعنبری برخورد کنید. @WarRoom</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/21817" target="_blank">📅 10:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21816">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امروز اگه بازار بودین از صف های صرافی‌ها و پمپ بنزین ها ویدیو درست و تمیز بگیرید ، همچنین محکم کاری کنید و حرفی در ویدیو نزنید دقت کنید تصویر خودتون در رفلکس شیشه یا آینه نیفته و ماشینتونن هم معلوم نباشه و دایرکت چنل ارسال کنید
@WaRroom</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/21816" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21815">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11404cd66.mp4?token=f80cBWzQaqoXYr_6XIKRsK5iz1S5O9FZZQH4BmE87Vt7qjU6BgaWuy0_OAiPWeIc_Zh6_NAox_SqaTSKBkSFybxdMXEKJg6sNt1s09HjfKIXtFRkJ4zRPsDuwsgUANZyQu7yCEmpbbYg3Wi3mG63DJW-Bv8ejIvcJ30xGafPKgyoBQgqNRIPUIX4Hz48JJ4YdRvsILSTr-nq084MfjqcA-M2Ix-mRyDk708zvjE1fkdcYT_iOJW9faACo2I9fLFZNim73B4UI7Zxicr0OszN9CahdtO1huJh5x_xF6RdCpLnbf-Bf7GDnb3xbI5RgEmkDQy3RwA5PTP9X-w1-tg9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11404cd66.mp4?token=f80cBWzQaqoXYr_6XIKRsK5iz1S5O9FZZQH4BmE87Vt7qjU6BgaWuy0_OAiPWeIc_Zh6_NAox_SqaTSKBkSFybxdMXEKJg6sNt1s09HjfKIXtFRkJ4zRPsDuwsgUANZyQu7yCEmpbbYg3Wi3mG63DJW-Bv8ejIvcJ30xGafPKgyoBQgqNRIPUIX4Hz48JJ4YdRvsILSTr-nq084MfjqcA-M2Ix-mRyDk708zvjE1fkdcYT_iOJW9faACo2I9fLFZNim73B4UI7Zxicr0OszN9CahdtO1huJh5x_xF6RdCpLnbf-Bf7GDnb3xbI5RgEmkDQy3RwA5PTP9X-w1-tg9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به‌محض اینکه در جنگ با ایران پیروز شویم، قیمت نفت مثل یک موشک به‌شدت پایین خواهد آمد.
ما همین حالا تقریباً کنترل کامل بر تنگه هرمز را در اختیار داریم.
@WarRoom</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/21815" target="_blank">📅 10:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21814">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وزارت دفاع امارات ادعا کرد که نیروی هوایی این کشور، یک پهپاد را در بدو ورود به آب‌های سرزمینی خود مورد هدف قرار داده
@WarRoom</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/21814" target="_blank">📅 10:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21813">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ به فاکس نیوز: آنها رژیمی سرسخت و باهوش هستند، اما بسیار شرورند. آنها ۵۲،۰۰۰ معترض را در چند ماه کشتند  اینها رژیمی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای داشتند، اسرائیل دیگر وجود نداشت. اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی…</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/21813" target="_blank">📅 09:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21812">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7948962027.mp4?token=SrWjRPHuR7vmT6rZBwld0GZhOOVtDtq6DS2jFYJH0WTVU6zTkhaB0z-TYCSXvZ4PghN4p4GZz0kvtbZGQ62st9SUM218W6ivh7drHRYOfdRR5T_kFwZCuUGbRWPXXnwGAw4mvDsixed-0We7PJ-XhMdGpA6d1dveb9oVdFKj7BpCHIqaRdd4jwdB7zWewS47EaHFCUMHz5pLKTuG0dTYXczhYzew8gTVScfAn32ef3O34devRpBiZPleresexFx7wIKxYRbPt6VtCfn-LcWJ3nfryf-ozr5UTzMAtJ5gdD7Pyxg0VmyQRVuhKpZq-YqAhjo7BuDQhCUv_626RWi2hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7948962027.mp4?token=SrWjRPHuR7vmT6rZBwld0GZhOOVtDtq6DS2jFYJH0WTVU6zTkhaB0z-TYCSXvZ4PghN4p4GZz0kvtbZGQ62st9SUM218W6ivh7drHRYOfdRR5T_kFwZCuUGbRWPXXnwGAw4mvDsixed-0We7PJ-XhMdGpA6d1dveb9oVdFKj7BpCHIqaRdd4jwdB7zWewS47EaHFCUMHz5pLKTuG0dTYXczhYzew8gTVScfAn32ef3O34devRpBiZPleresexFx7wIKxYRbPt6VtCfn-LcWJ3nfryf-ozr5UTzMAtJ5gdD7Pyxg0VmyQRVuhKpZq-YqAhjo7BuDQhCUv_626RWi2hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمونه‌ای از شیوه استقرار مین‌های دریایی توسط سپاه در خلیج فارس؛ راکت فجر-۵ با کالیبر ۳۳۳ میلی‌متر که به‌جای سرجنگی استاندارد، حامل محموله‌ای از مین‌های دریایی است. شب گذشته نیز احتمالا سامانه‌ای مشابه در جزیره لارک هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/21812" target="_blank">📅 09:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21811">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c78dd13214.mp4?token=AMw_40Hx-Uglso52ERVXmClGmH6K6nUVIO6JtjKt3tHbP9-mPY7WRmL-TlOyYDxzUOnJILwpmzR4c8zqYMev_HqRvhNQPDXKi185NvuWoG8gNwcttXBSICivP_TGUg78Pjs5oBPbmuzAdpIxuuISAztyDJnTgffYAkE_gZQfTIABToRGX0phFWAJ-UmrorF2emyLGk12Lb2awoC3plR7l1toj6CsALQuRQoZorSSZz8FrjLsxEyCxzSrdIVvLrenB9gAb1PG1G3JSVd5O7vtc_aClrpQKPSnvBvNwWLH1rNvObP89PcF8i--Jp_YvKp_FOvS6Dmw_Gprs9BRK03esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c78dd13214.mp4?token=AMw_40Hx-Uglso52ERVXmClGmH6K6nUVIO6JtjKt3tHbP9-mPY7WRmL-TlOyYDxzUOnJILwpmzR4c8zqYMev_HqRvhNQPDXKi185NvuWoG8gNwcttXBSICivP_TGUg78Pjs5oBPbmuzAdpIxuuISAztyDJnTgffYAkE_gZQfTIABToRGX0phFWAJ-UmrorF2emyLGk12Lb2awoC3plR7l1toj6CsALQuRQoZorSSZz8FrjLsxEyCxzSrdIVvLrenB9gAb1PG1G3JSVd5O7vtc_aClrpQKPSnvBvNwWLH1rNvObP89PcF8i--Jp_YvKp_FOvS6Dmw_Gprs9BRK03esTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
دموکرات‌ها می‌خواهند کشور ما در جنگ با ایران شکست بخورد؛ اما این اتفاق نخواهد افتاد، چون ما به‌طور مطلق و به‌راحتی در حال پیروز شدن هستیم.
تحریم های اقتصادی کمرشان را شکسته آنها محکوم به شکستند و در زمان مناسب، یا ما پیروز خواهیم شد، یا آنها دست به اقدامی خواهند زد.
من با پیروز شدن مشکلی ندارم. نیازی ندارم که امضای آنها پای یک تکه کاغذ باشد
@WarRoom</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/21811" target="_blank">📅 09:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21810">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa60f768ab.mp4?token=SPuNCkaHfbmI2lrKQfZBx_M-Rz3AgG5TIYvwA_2g8Fo5K05EFj5Cp3ewapVL0BiPRraPs6xNjAWRW_Wk4vcs6OGKs91ZMaVxB7iOhekSZ2pH9OtGv-rgu1XabWKbAuR6p_rEBlOiJj0Bx4yEXC9Nvsfy62RQUXL01p5XEV_Nx36bU2FFcwXeYVHgyFMs2joZ9BIqGVOuZlUXZC_C3s04JTkiOAw0_FJrBceIS3HPpgnURzurn1FuZA4OJRWYj-NgfemVAD7gvxsIJ8Map1ndlrXH3sLUaqbwzprwdyftl6Z9xNzjvtLyr7HSx5iHItlR1TkrAPAqMGiWrgQ1Esa5zpDOB0GPjwy2YrTaZNnWJ33k6mf0AtJrZsYFcWakEXqHfL1zFHQbOst0xEcjT3XaQaNhA0wJ7UxUZzfUxcSGJA7R_PJq6p0N9ymShqE1ZnhmMTLG6kl7rEKTPEbBnjWK2b0UBZJAY6-ZSpwte9b9nddQ45VMVsZVj6fvlPIxAPdGkb3D0vm_37LV_IzWClXPwUibU-HKsmBfxYYpdwpAfZ0Dt0gFs3AHTaI6tMzfHG2boqJr0f6JPghc3onrB7Lj-d34sCAVv5OgK6fPUKfDWPCVZrkaI4-YOiw-C2wRBs3XXIXt2Xwrr92VSfeGqV9E-r3QBNWeY8hkw59pTmPgyVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa60f768ab.mp4?token=SPuNCkaHfbmI2lrKQfZBx_M-Rz3AgG5TIYvwA_2g8Fo5K05EFj5Cp3ewapVL0BiPRraPs6xNjAWRW_Wk4vcs6OGKs91ZMaVxB7iOhekSZ2pH9OtGv-rgu1XabWKbAuR6p_rEBlOiJj0Bx4yEXC9Nvsfy62RQUXL01p5XEV_Nx36bU2FFcwXeYVHgyFMs2joZ9BIqGVOuZlUXZC_C3s04JTkiOAw0_FJrBceIS3HPpgnURzurn1FuZA4OJRWYj-NgfemVAD7gvxsIJ8Map1ndlrXH3sLUaqbwzprwdyftl6Z9xNzjvtLyr7HSx5iHItlR1TkrAPAqMGiWrgQ1Esa5zpDOB0GPjwy2YrTaZNnWJ33k6mf0AtJrZsYFcWakEXqHfL1zFHQbOst0xEcjT3XaQaNhA0wJ7UxUZzfUxcSGJA7R_PJq6p0N9ymShqE1ZnhmMTLG6kl7rEKTPEbBnjWK2b0UBZJAY6-ZSpwte9b9nddQ45VMVsZVj6fvlPIxAPdGkb3D0vm_37LV_IzWClXPwUibU-HKsmBfxYYpdwpAfZ0Dt0gFs3AHTaI6tMzfHG2boqJr0f6JPghc3onrB7Lj-d34sCAVv5OgK6fPUKfDWPCVZrkaI4-YOiw-C2wRBs3XXIXt2Xwrr92VSfeGqV9E-r3QBNWeY8hkw59pTmPgyVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
به فاکس نیوز
:
ایران در ابتدا جنگ به کشورهایی حمله کرد که به‌نوعی بی‌طرف بودند؛ عربستان سعودی، قطر، امارات متحده عربی، بحرین و کویت.
همه شوکه شدند. من هم تعجب کردم. فکر کردم این اتفاق از یک جهت خیلی خوب بود، چون آنها تمام حمایتی را که داشتند از دست دادند. آنها تا پیش از آن، تا حدی از حمایت برخوردار بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/21810" target="_blank">📅 09:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21809">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4845fda47.mp4?token=W124V48z7ZRT5obS2bLdGmgIVKzrOq6CS_BIxs15p4s00fZ-Ob32aGxR4XPrF4vC0H89D6n9RkjRyaD5ryNpG8YfIFiDSL7I-5ZrWh221xcieI2MkD4Ex18briNVner7KWULrsJyTR8hyLkk6q1n4-gDdxoPYbI6d4PywuTwXm3A-n-UTMYmbvWs_VHR9Ppz9Vq_aNIOXQbHlv-UwQUQdYbiFcTaPsO17n6tgTIJAmiFwZje8S3O2fKDrT7vlC5Tne8sPMZ2UovnYGu__HHpeKJ1rN_Z9-eflzvdUXQqy-6ZuBEyYWrKVhXggCtOOwI4mgbJCSScAGFtRukBFgDa_6mX3kUBnVNcNLAzOoDY-xqP7b6m8YMgVcxRR_Qx6p6xb70tXVAg2E_VQs0hRFTUGMGgZcXdnE31KSzuaetMr8jaTkJagDayC5bOUnIhBCQpvAaIhKKI_Cz-nc0PdCyQ_DcrlqFzouEpNvGuaWMo6P3BhzL4iRCJjWMiyMQGiT_tDcWY4u0ouY0DXnJ4orAwi9Zmsf-n84mLzHGyrFOe4PKLgP_XpeJAN9Umz15Y_jmrrSAlQ2deusSOGYFwB2B36u4wJ-hh2PcWdol9BhRnzM6EgKqQ-ZbfdLluL073E-mk8E5gy_e7E8qfkH9703sSLmSa0SUZyVpmtgFbdI71a94" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4845fda47.mp4?token=W124V48z7ZRT5obS2bLdGmgIVKzrOq6CS_BIxs15p4s00fZ-Ob32aGxR4XPrF4vC0H89D6n9RkjRyaD5ryNpG8YfIFiDSL7I-5ZrWh221xcieI2MkD4Ex18briNVner7KWULrsJyTR8hyLkk6q1n4-gDdxoPYbI6d4PywuTwXm3A-n-UTMYmbvWs_VHR9Ppz9Vq_aNIOXQbHlv-UwQUQdYbiFcTaPsO17n6tgTIJAmiFwZje8S3O2fKDrT7vlC5Tne8sPMZ2UovnYGu__HHpeKJ1rN_Z9-eflzvdUXQqy-6ZuBEyYWrKVhXggCtOOwI4mgbJCSScAGFtRukBFgDa_6mX3kUBnVNcNLAzOoDY-xqP7b6m8YMgVcxRR_Qx6p6xb70tXVAg2E_VQs0hRFTUGMGgZcXdnE31KSzuaetMr8jaTkJagDayC5bOUnIhBCQpvAaIhKKI_Cz-nc0PdCyQ_DcrlqFzouEpNvGuaWMo6P3BhzL4iRCJjWMiyMQGiT_tDcWY4u0ouY0DXnJ4orAwi9Zmsf-n84mLzHGyrFOe4PKLgP_XpeJAN9Umz15Y_jmrrSAlQ2deusSOGYFwB2B36u4wJ-hh2PcWdol9BhRnzM6EgKqQ-ZbfdLluL073E-mk8E5gy_e7E8qfkH9703sSLmSa0SUZyVpmtgFbdI71a94" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
به فاکس نیوز
:
آنها رژیمی سرسخت و باهوش هستند، اما بسیار شرورند.
آنها ۵۲،۰۰۰ معترض را در چند ماه کشتند
اینها رژیمی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای داشتند، اسرائیل دیگر وجود نداشت.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت
@WarRoom</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/21809" target="_blank">📅 09:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21808">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d72b70a62.mp4?token=BcSLj6n-1sF0MymQvtGSEnPmpOfGGjbgv_iHKJuGN5cjBIP6OX-WyE8DT0ERloURwCUS9GS8W9P40SlTRncMQ9tBz7dByxmyJtwPcyYhywO5UnG5WfSBYaH_ZBP1sjD_5T0hi60WldKyiiaaTVHIrnnVfBvJkNLl_BXE6XuM0lhwHdoa_51r0WzUTooW0AFBYrPo4p2nVzRAesWG8t93z-8Ue99GXNM8vOAsglDBeSBFkd1yhB0GAqQxu3H1gTi6ZiPA5Ph2n6vaGNAvwebNfT7ZhBFUW0BmfuZsJrG8ya_tqx2SNSM9LFqLBFGuQSuutRsGVfRkcy0Go19HORkhdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d72b70a62.mp4?token=BcSLj6n-1sF0MymQvtGSEnPmpOfGGjbgv_iHKJuGN5cjBIP6OX-WyE8DT0ERloURwCUS9GS8W9P40SlTRncMQ9tBz7dByxmyJtwPcyYhywO5UnG5WfSBYaH_ZBP1sjD_5T0hi60WldKyiiaaTVHIrnnVfBvJkNLl_BXE6XuM0lhwHdoa_51r0WzUTooW0AFBYrPo4p2nVzRAesWG8t93z-8Ue99GXNM8vOAsglDBeSBFkd1yhB0GAqQxu3H1gTi6ZiPA5Ph2n6vaGNAvwebNfT7ZhBFUW0BmfuZsJrG8ya_tqx2SNSM9LFqLBFGuQSuutRsGVfRkcy0Go19HORkhdTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس نیوز
:
تماشای واکنش سریع نیروهای آمریکایی و موفقیت آنها در رهگیری آتش ورودی «در لحظه و به‌صورت زنده، شگفت‌انگیز» بوده برایم!
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/21808" target="_blank">📅 09:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21807">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6da7ebc4e.mp4?token=qD1ZJci1Zvf5FR5wGnYEJDqdgKckxLzhNnL6iTyRNxTxWEn1RbNuBQhUGUVy9Arkf2Rn2FF2kl0_u0V6kvS2HQUMXu6qeL9OT07thJPFkMCvhsWFR_NaxhMJYx037sd5Mu31bDb62i6s-RDe_TaRnnXCJK9TYU5vbvak9zBfDJQfb4MWm9n8qikemppgvFUROvJadJwLyAd9pJtwPzVmDVV6S_jBOB1EJL3Unpa8m1lzrpoOamXEV282m_nDfQyBrKTgp0he0bRgREYjP3jfwhqLGHtXwXLXY6EdYAjN15HhR0yPiXaIrieQCspVbAtCuz1HgIEIeZzn_nGNFjM8Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6da7ebc4e.mp4?token=qD1ZJci1Zvf5FR5wGnYEJDqdgKckxLzhNnL6iTyRNxTxWEn1RbNuBQhUGUVy9Arkf2Rn2FF2kl0_u0V6kvS2HQUMXu6qeL9OT07thJPFkMCvhsWFR_NaxhMJYx037sd5Mu31bDb62i6s-RDe_TaRnnXCJK9TYU5vbvak9zBfDJQfb4MWm9n8qikemppgvFUROvJadJwLyAd9pJtwPzVmDVV6S_jBOB1EJL3Unpa8m1lzrpoOamXEV282m_nDfQyBrKTgp0he0bRgREYjP3jfwhqLGHtXwXLXY6EdYAjN15HhR0yPiXaIrieQCspVbAtCuz1HgIEIeZzn_nGNFjM8Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در تروث  : جزیره خارک دارد به‌طور کامل به تکه‌پاره تبدیل (با خاک یکسان) می‌شود!!!
@WarRoom</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/21807" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21806">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حقیقت یاب سنتکام : نیروهای آمریکایی اقدامات محدود و دقیقی را علیه نیروهای سپاه پاسداران که در حال نصب مین در تنگه هرمز بودند و تهدیدی فوری ایجاد می‌کردند، انجام دادند. به عبارت دیگر، ایران این تهدید را ایجاد کرد و ارتش ایالات متحده آن را از بین برد تا از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی محافظت کند
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/21806" target="_blank">📅 08:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21805">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عراقچی همراه پزشکیان
به منظور شرکت در نشست سران سازمان همکاری شانگهای عازم قرقیزستان شدند
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/21805" target="_blank">📅 08:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21804">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بیانیه سپاه : «یک نفتکش غول‌پیکر ناسازگار که می‌کوشید از مسیر جنوبی غیرقانونی تنگه هرمز بگذرد، با دو مین دریایی برخورد کرد، آتش‌سوزی گسترده‌ای رخ داد و کاملاً متوقف شد.»
سپاه پاسداران هشدار داد دیگر شناورهایی که قواعد امنیتی آن را نقض کنند با همین سرنوشت روبه‌رو می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/21804" target="_blank">📅 08:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21803">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNWMKyyFXBiI9ehewt6GD2i9iJGExxZzM67B-oChq-oQmKePtgltwD_l8ZMs9SW_YLiijIr8JTtlfq6apJusy0fwS-VF1ZF0351vm6LDFRWOIbvBQBbXUN9-uFYfXhwK05FVHBcSq82LG18lmAdHNA1BhkdnT6Jh4pRIbPqwCJbN46WbCVuuYyIfIKzGHWvtuWx6A_xZJdOeMGN29e0jvR1Wdi8FEOtEb5v31e9Nch9CgvKcbGA6JSEdz2uShQuHZnAv8tQ84jFew2YqBouyW3V-ikqN0Xpj3TuaVQVxFkn2bRxLHdlI8Oi88FI1MzRj9-q6c4ac_JyrqPmzePPl4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حال حاظر بر خلاف رسانههای رژیم که گفتمد هواپیما های امریکایی از منطقه فرار کردند،  ۴ سوخترسان که همه آنها از قطر بلند شده‌اند، مشغول عملیات بر روی تنگه هرمز هستند و یک سوخترسان هم از اسرائیل به سمت خلیج فارس در حرکت است.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/21803" target="_blank">📅 03:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21802">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21802" target="_blank">📅 03:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21801">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCU-RgBbEMzMkLWhue82Y7279009mClgfFrW6nQXMWC5fN69JgSzRx5ESjNpzaf7TGZp2VuH8aZONSNB0h8bGtcMSdZRo3J6sp12A8t_sXKaq6nY1_fFYNX1gG3PKqzpLotbhsIu_vKXvcFWPy-BQgTK2q4RaAdQ2xZGZ-cS_33aEsWQYbwh4yNb5am3FrAoYutBJrMe-TB7A6uSdlDQDA91Tv3yhDqfXX8oRjU3sfs5YBn2wjlmEzguJ2r2bIHQ3QtOJfv-GAunpN_Retg4uqUVD5wRwqlIrM-x5Fb4DgRAMlTnREe0zWoyHFgVK2XCC27P71j0bNf1lPqdoJmZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز فلای‌کیش‌که از مهراباد داره میاد امام ! آیا دارن تخلیه میکنند مهرآبادو ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21801" target="_blank">📅 03:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21800">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارش صدای‌انفجار از تنگه
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21800" target="_blank">📅 03:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21799">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ارتش اردن در بیانیه‌ای ادعا کرد که ۸ موشک را پس از نفوذ به حریم هوایی این کشور رهگیری کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21799" target="_blank">📅 03:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کانال 14 اسرائیل : تو حمله هوایی آمریکا به لارک ایران ده‌ها نفر از پرسنل سپاه پاسداران کشته و حدود ۱۰۰ نفر دیگه هم زخمی شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21798" target="_blank">📅 02:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21797" target="_blank">📅 02:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21796">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLS0q2pOO_gFzkiGP9mRj4VV-gmxHgpAAMAl_lLza40K8rCR6ZfCwC_1n0iWgY1nfTI9BJ80SlzBGGp1J9xfpfsxga-KGzkbjx0vIgKc928bD6ZJQmrWOFrI0Y2Dp5aZnPmewnyTakqV7FKK3k0RRjvF4AEPv3fg6HyvP7_y9uGWCUquUJnGm8N2bUJ-pHXVAb2oasUaloyxrfHn0ycyWE2WbQlg89PhhsI3-ITCqHkn-vq1JLGEx8HV8vpOJr4UDxzi7D9zqpoOBgeRMbKuVqW2yaGDKV-QKqAJiMivKbayKzUxVX_jMzXe_v6zWbBRdvNazjSfUOKBMaiOVNcUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21796" target="_blank">📅 02:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21795">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فردا ملت همیشه در صف ، در پمپ بنزین و صرافی ها ! قیامت می کنند
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21795" target="_blank">📅 02:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21793">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89022fc40e.mp4?token=VYtBSf7-sW-JUfvFHSTb6AtwRxwI6xSVbYpPRmzatZ34iJX2IbLtpVEnTbOMpfuJXLoPw7wduyLj5qhvvL0Ywta75TfeFqC_WJK2l6EdXNLsdI9sMwbqYW8wQb6l0uSpcB_syD5L9Phq3qEO0JckGjMWdB3WwArjY_L8zrIq8viHPkRFnKtgyC1ZDh9KngUISVJWU8FeodE47looI6pwUctJsQyS8nUMeLX4bP3lixnzhiL-RHdLTaGoXLA_5of18VWG_UMFeKZkG8fKXEE8n_z5looBaX5G7TId3eLNegxS0hbl5mzV6xQpxx6Zk1fLX1mEhd6ykPIV00O9Bik-AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89022fc40e.mp4?token=VYtBSf7-sW-JUfvFHSTb6AtwRxwI6xSVbYpPRmzatZ34iJX2IbLtpVEnTbOMpfuJXLoPw7wduyLj5qhvvL0Ywta75TfeFqC_WJK2l6EdXNLsdI9sMwbqYW8wQb6l0uSpcB_syD5L9Phq3qEO0JckGjMWdB3WwArjY_L8zrIq8viHPkRFnKtgyC1ZDh9KngUISVJWU8FeodE47looI6pwUctJsQyS8nUMeLX4bP3lixnzhiL-RHdLTaGoXLA_5of18VWG_UMFeKZkG8fKXEE8n_z5looBaX5G7TId3eLNegxS0hbl5mzV6xQpxx6Zk1fLX1mEhd6ykPIV00O9Bik-AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی سپاه با این ویدیو تایید کرد فقط اردن رو زده و نام عملیات امشب تنبیه متجاوز بوده
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21793" target="_blank">📅 02:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21792">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چنل‌تلگرام رو پین کنید بالا حتما و نتفیکیشن های اینستاگرام رو هم روشن کنید کاملا ، چنل یوتبوب رو ساب کنید این هفته هر جور شده استارت میزنم   https://youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21792" target="_blank">📅 02:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21791">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک منبع آمریکایی به فاکس نیوز گفت:
تاکنون تأثیرات جدی‌ای مشاهده نشده است. تقریباً تمام موشک‌های شلیک‌شده تا این لحظه مورد هدف قرار گرفته و منهدم شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21791" target="_blank">📅 02:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21790">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21790" target="_blank">📅 02:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21789">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21789" target="_blank">📅 02:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21788">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21788" target="_blank">📅 02:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21787">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خسته باشم ویس میدم تو دایرکت نده تو مخی</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21787" target="_blank">📅 02:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21786">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21786" target="_blank">📅 02:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21785">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/21785" target="_blank">📅 02:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21784">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21784" target="_blank">📅 02:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21783">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/21783" target="_blank">📅 02:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21782">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">امارات هیچ خیری نیست
😃</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21782" target="_blank">📅 02:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21780">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ادمین های فیک نیوز تلگرام کل کشور های حوزه خلیج فارس را با خاک یکسان کردند
😂
😂
😂
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21780" target="_blank">📅 02:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21779">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مقام ارشد آمریکایی به فاکس نیوز :
تمام‌ موشک‌های شلیک شده رو رهگیری کردیم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21779" target="_blank">📅 01:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21778">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدا و سیما : داریم پاسخ میدیم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21778" target="_blank">📅 01:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21776">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parandeh (IG @yashar)</div>
  <div class="tg-doc-extra">Martik (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/21776" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21776" target="_blank">📅 01:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21774">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تتر ۲۰۸.۰۰۰ تومان (رکورد تاریخی)
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21774" target="_blank">📅 01:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21773">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@WarRoom
جنگ مادر شوهری</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21773" target="_blank">📅 01:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21772">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219d2a6238.mp4?token=JQRTaAunttjuMQdKUkZ-xNuM3aeskWzLNV3NIvyghwAADujVtKmY8AUUmMyybYXDZ9V-lFCuM2uHiXBSZU7t6HdHFXQy3yLTFlF6qMy88hbdAgo_ff2VBnFgk3OQw_YaSGKeVws-_dvZQCvF1aEqeNhI5f89B-SzOV5E4LNRe9soW44dAYXWSLc89iMOp1JIQ8r1DbPdLiAvcAlo34kAvBGGaIDgXig9bc0yRZk1Cw7KWCkBihcd0ENGnM5RcKMXdLR7y5_MIk86En1SFGXCd2RQBnyCw-OPGbBPKPbcN6vquFSgXt-ebL6iFfSR2a_XrPusxoc0LoC-F9liBMCxpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219d2a6238.mp4?token=JQRTaAunttjuMQdKUkZ-xNuM3aeskWzLNV3NIvyghwAADujVtKmY8AUUmMyybYXDZ9V-lFCuM2uHiXBSZU7t6HdHFXQy3yLTFlF6qMy88hbdAgo_ff2VBnFgk3OQw_YaSGKeVws-_dvZQCvF1aEqeNhI5f89B-SzOV5E4LNRe9soW44dAYXWSLc89iMOp1JIQ8r1DbPdLiAvcAlo34kAvBGGaIDgXig9bc0yRZk1Cw7KWCkBihcd0ENGnM5RcKMXdLR7y5_MIk86En1SFGXCd2RQBnyCw-OPGbBPKPbcN6vquFSgXt-ebL6iFfSR2a_XrPusxoc0LoC-F9liBMCxpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن دقایقی پیش
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21772" target="_blank">📅 01:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21771">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=Nr7MGeaheWR7kViEhZE8RYCTXh1-T2yq45W-ruMnbXGsvxZ7tn4VWuLXVYcGCiKQoWbaNgG2WB8e6A7TFuHHRqnTAVY81kdooTB5jHGyK0JuYoaZnXi62pdQ4XiXigfJiPzKTHoyWMKSrCM9sXT7iEPYy3PDze7TkEyCPymdeX-E7LBGppNBD9IGvHRF_HXwkHyozPjubtE2vEfeoWDlj5uYtfUI8zZuVlEf2NxPs5DKF8_V1EjHGA0uE_e_U4O-gfM7Hxl9kFxi2wRGiK-4MdOQAJ_YQzkApL4wgAOt5X6MzpxdQe40M5BvjFgVe58nv8nkTEOXornL-o0-9nXXbbTT19xBEesLWi6V5lMq_mhlQEM4qWnp-DkDrOoS5kQ6aI6SO9tuNgepCAy0Zfd4KV60tgpSuRzim1JZAUPbq_jRHFG6O_ht_-hluApB31L2ae9nj0M-CKnF4r5quqvVQUceRvW48a-uZRhnqqik2Tv6_QnvduhJVnXtQ2qw6CPu9gzUfSnaZFXnyw3Ql4T_oJ6Gp1uMhm7s3hEVsMy2vxw2DBifFfwpPtOIbw6zqCXb8uo0Sq2pSjhI0fKTUkfpzZSdlD3THS64c7fABEfI2JGXdf0SPqk4CWXbq54nol4MJ9AkYKsLHkxM06-IXVkKPM0kXrFY7q9bX7Bc7V5yLQI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d9156929.mp4?token=Nr7MGeaheWR7kViEhZE8RYCTXh1-T2yq45W-ruMnbXGsvxZ7tn4VWuLXVYcGCiKQoWbaNgG2WB8e6A7TFuHHRqnTAVY81kdooTB5jHGyK0JuYoaZnXi62pdQ4XiXigfJiPzKTHoyWMKSrCM9sXT7iEPYy3PDze7TkEyCPymdeX-E7LBGppNBD9IGvHRF_HXwkHyozPjubtE2vEfeoWDlj5uYtfUI8zZuVlEf2NxPs5DKF8_V1EjHGA0uE_e_U4O-gfM7Hxl9kFxi2wRGiK-4MdOQAJ_YQzkApL4wgAOt5X6MzpxdQe40M5BvjFgVe58nv8nkTEOXornL-o0-9nXXbbTT19xBEesLWi6V5lMq_mhlQEM4qWnp-DkDrOoS5kQ6aI6SO9tuNgepCAy0Zfd4KV60tgpSuRzim1JZAUPbq_jRHFG6O_ht_-hluApB31L2ae9nj0M-CKnF4r5quqvVQUceRvW48a-uZRhnqqik2Tv6_QnvduhJVnXtQ2qw6CPu9gzUfSnaZFXnyw3Ql4T_oJ6Gp1uMhm7s3hEVsMy2vxw2DBifFfwpPtOIbw6zqCXb8uo0Sq2pSjhI0fKTUkfpzZSdlD3THS64c7fABEfI2JGXdf0SPqk4CWXbq54nol4MJ9AkYKsLHkxM06-IXVkKPM0kXrFY7q9bX7Bc7V5yLQI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگه بابا جنگه !!!
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21771" target="_blank">📅 01:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21770">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a23e19932.mp4?token=BPe5vDHI7AvDIk7HzZyQj79BV1TEQA-20k6DGSNWDSGIpXazimwKwS5OO2aUxLBBnjgp5TKZBJ2ZfYCHBmHf2QXgsrEwa-zV4N09EcWiov0CxGvrmb6SYBdwHAeTqEmvCR7MSxSquXOjFPR2nMw82X0CreRz5HH_1S6KqJ_5BlUdHvJv2fXBWl60VGj3ltVXEBdDLKeX6TmpHrbYJRgXs05Ax5bdR4himGeR9CVp5Rw-ejGwwOhyNQujbb6YBuZI9a9qBrWuOSp_mkFn9JAzVO9bxRfbKxcblOuexsmxfzGY4R61Jt79VEYU0sGSiS9ocZqiPsBQ-T1JwebU5fWluA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a23e19932.mp4?token=BPe5vDHI7AvDIk7HzZyQj79BV1TEQA-20k6DGSNWDSGIpXazimwKwS5OO2aUxLBBnjgp5TKZBJ2ZfYCHBmHf2QXgsrEwa-zV4N09EcWiov0CxGvrmb6SYBdwHAeTqEmvCR7MSxSquXOjFPR2nMw82X0CreRz5HH_1S6KqJ_5BlUdHvJv2fXBWl60VGj3ltVXEBdDLKeX6TmpHrbYJRgXs05Ax5bdR4himGeR9CVp5Rw-ejGwwOhyNQujbb6YBuZI9a9qBrWuOSp_mkFn9JAzVO9bxRfbKxcblOuexsmxfzGY4R61Jt79VEYU0sGSiS9ocZqiPsBQ-T1JwebU5fWluA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موشکهای جمهوری اسلامی‌به اردن رسیدند و پدافند درگیر شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21770" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21769">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">به گزارش دیدبانهای اتاق جنگ :  ۳ انفجار در ابتدا حدود ۸:۴۵ دقیقه شب و ۳ انفجار بعد از ۱۵ دقیقه ۹:۰۰ شب تهران در لارک اتفاق افتاد تهران @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21769" target="_blank">📅 01:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21768">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چنل‌تلگرام رو پین کنید بالا حتما و نتفیکیشن های اینستاگرام رو هم روشن کنید کاملا ، چنل یوتبوب رو ساب کنید این هفته هر جور شده استارت میزنم
https://youtube.com/yasharrapfa</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21768" target="_blank">📅 01:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21767">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">منابع عربی: پایگاه موفق السلطی اردن هدف موشک‌ها و پهپادهای ایرانی است
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21767" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21766">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گزارش صدای انفجار اردن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21766" target="_blank">📅 01:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21764">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رویترز ادعا کرد ایران از ۳۲ شهر در حال شلیک موشک است
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/21764" target="_blank">📅 01:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21763">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فاکس نیوز: جنگ بزرگ آغاز شد
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/21763" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21762">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از خرم آباد لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21762" target="_blank">📅 01:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21761">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش پرتاب موشک/پهپاد از تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21761" target="_blank">📅 01:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21760">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فرودگاه مهرآباد تا اطلاع ثانوی تعطیل شد @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/21760" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21759">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ابراهیم عزیزی رئیس کمیسیون امنیت ملی:یک بار دیگر اراده ما را آزمایش کنید و بهای سنگین تری بپردازید، انتقام در راه است؛ فقط بدوید!‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/21759" target="_blank">📅 00:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21758">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک مقام آمریکایی: برای نخستین بار در یک ماه گذشته، حملاتی را علیه ایران انجام دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21758" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21757">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال ۱۲ اسرائیل در خبری فوری اعلام کرد ارتش آماده هر سناریویی است و یک بانک اهداف گسترده دارد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/21757" target="_blank">📅 00:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21756">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرودگاه مهرآباد تا اطلاع ثانوی تعطیل شد
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21756" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21755">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ab68fe7d.mp4?token=aQcgozu-1VADUqPFUbImKaPQZ1hZzul8SgoIQWxdCABll49JNnxxwHDkHT7yG-RmsqaF3pidEYCRTShShldSDpasU8XVqr94hCMAvlzqazMQzcmzZO-3aEmezChJDMr6jfWCujEiFvZZVo9PxDRBdOilJDDeEgrR_TDLGGlD--TDW44HHNADpr5IaGx1snKixR4LVeSx11Ip294dhdgBLunWhu193MVJRBcEt6NNDr1hcnODlPuBT87qWzHPiw66etCGuOw9ssyk8Xl0rhz8Jy9Qw3J0IxjTj5XJTNLdrBCyQpcsQi49PB7HNu3S304w9P_uPY4SjQo3WYWbbE5Yv4FG6X7iNVLsAgaistdOJnLxF6fVz9ppmyBGRxWHxyQbV2jN7kfarvtrn1Z6aGq5QojDv2f3tYT2xAvMYQ5_bv44H7jrXw_eKuzZaHZoMRsk1kl1HePTJbetWpwtu4wEmH0ZqgvfaY8-DYaWdC2TPSesBxL4Hd3Tc5SVQo0Wv2oQgBaFA1wntigPoPLUwK5M0kbE5trCs0pBDFdnlg2aYJKf8W-4UtqBXrHHPObYlmSvYFob0-PAh0MQolQPate0HWUHISwvmGUKhrm8ms2LpoN0dK7dYb2-nJ0lbhYCI1EB_y_O8H-08I-YhPuzuSEGDGG2MtaFbYdfkKe_C53htmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ab68fe7d.mp4?token=aQcgozu-1VADUqPFUbImKaPQZ1hZzul8SgoIQWxdCABll49JNnxxwHDkHT7yG-RmsqaF3pidEYCRTShShldSDpasU8XVqr94hCMAvlzqazMQzcmzZO-3aEmezChJDMr6jfWCujEiFvZZVo9PxDRBdOilJDDeEgrR_TDLGGlD--TDW44HHNADpr5IaGx1snKixR4LVeSx11Ip294dhdgBLunWhu193MVJRBcEt6NNDr1hcnODlPuBT87qWzHPiw66etCGuOw9ssyk8Xl0rhz8Jy9Qw3J0IxjTj5XJTNLdrBCyQpcsQi49PB7HNu3S304w9P_uPY4SjQo3WYWbbE5Yv4FG6X7iNVLsAgaistdOJnLxF6fVz9ppmyBGRxWHxyQbV2jN7kfarvtrn1Z6aGq5QojDv2f3tYT2xAvMYQ5_bv44H7jrXw_eKuzZaHZoMRsk1kl1HePTJbetWpwtu4wEmH0ZqgvfaY8-DYaWdC2TPSesBxL4Hd3Tc5SVQo0Wv2oQgBaFA1wntigPoPLUwK5M0kbE5trCs0pBDFdnlg2aYJKf8W-4UtqBXrHHPObYlmSvYFob0-PAh0MQolQPate0HWUHISwvmGUKhrm8ms2LpoN0dK7dYb2-nJ0lbhYCI1EB_y_O8H-08I-YhPuzuSEGDGG2MtaFbYdfkKe_C53htmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : من رژیم ایران رو نابود میکنم، اینو بهتون قول میدم و مطمئنم این کار شدنیه.اونا خیلی ضعیف تر از قبل شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/21755" target="_blank">📅 00:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21754">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21754" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21753">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار من تو مسیر بندرعباس میناب بودم  از کنار دیوار خیاط دانشگاه هرمزگان موشک بلند شد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/21753" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21752">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سی‌ان‌ان: دور جدید حملات نظامی امریکا به ایران شروع شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/21752" target="_blank">📅 00:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21751">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارش صدای انفجار جدید از لارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/21751" target="_blank">📅 00:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21750">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه های عبری : جالب خواهد بود ببینیم رژیم ایران چگونه به حمله آمریکا واکنش نشان خواهند داد، زیرا عدم واکنش به این حادثه می تواند نشانه حقارت باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/21750" target="_blank">📅 00:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21749">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال ۱۳ عبری: اسرائیل به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی هزاران کورد را به اسرائیل برده و آموزش داده بوده است. ولی سه روز پس از آغاز جنگ ۴۰ روزه، پیامی از آمریکا به اسرائیل می‌رسد که طرح اجرا نشود. @WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/21749" target="_blank">📅 00:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21748">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بیانیه سپاه : دشمن در هر دو عرصه اقتصادی و نظامی، تبعات این محاسبه غلط را خواهد پرداخت
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21748" target="_blank">📅 00:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21747">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانال ۱۳ عبری: اسرائیل به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی هزاران کورد را به اسرائیل برده و آموزش داده بوده است. ولی سه روز پس از آغاز جنگ ۴۰ روزه، پیامی از آمریکا به اسرائیل می‌رسد که طرح اجرا نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/21747" target="_blank">📅 00:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21746">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام:ایران میخواست یه سری مین رو توی تنگه هرمز بفرسته که ماهم جواب کارشو دادیم.
@WarRoom
😁</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21746" target="_blank">📅 23:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21745">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21745" target="_blank">📅 23:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21744">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آکسیوس : دستکم ۷۰ تن سپاهی کشته شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/21744" target="_blank">📅 23:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21743">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اسرائیل جنوب لبنان رو داره برای فصل کاشت آماده میکنه و شخم میزنه
😂
🔥
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21743" target="_blank">📅 23:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21742">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس:ارتش آمریکا در خاورمیانه به حالت آماده باش درآمده است و برای پاسخ ایران آماده شده است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/21742" target="_blank">📅 23:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21741">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21741" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21740">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ادعای آکسیوس : ایران در حال آماده‌سازی برای پرتاب راکت‌های حامل مین‌های دریایی به داخل تنگه هرمز بود
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/21740" target="_blank">📅 23:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21739">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ادعای رسانه های رژیم :
حمله ای که آمریکا انجام داد با پهپاد بوده که از اردن بلند شدن، حداقل چندین پهپاد MQ9 از پایگاه موفق سلطی امروز به سمت منطقه تنگه هرمز آمدند.
فرماندهی سنتکام اکنون در آنجا می باشد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/21739" target="_blank">📅 23:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21738">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تسنیم: برخی گزارش‌های اولیه غیررسمی حاکیست که بر اثر جنایت دشمن آمریکایی تاکنون ۲ نفر به شهادت رسیده و ۲ نفر نیز مجروح شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21738" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21737">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سید محمد مرندی: رژیم ترامپ مرتکب یک اشتباه بزرگ شد.
@WarRoom
😂
🔥</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/21737" target="_blank">📅 23:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21736">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش شنیده شدن چندین انفجار در جزیره لارک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21736" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21734">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری های تروریستی رژیم ، فارس و تسنیم این حمله را تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21734" target="_blank">📅 23:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21733">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش های منتشر شده از کشته و زخمی شدن تعدادی از افراد سپاه در پی حمله نظامی آمریکا به جزیره لارک.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/21733" target="_blank">📅 23:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21732">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21732" target="_blank">📅 23:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21731">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">به گزارش دیدبانهای اتاق جنگ :
۳ انفجار در ابتدا حدود ۸:۴۵ دقیقه شب و ۳ انفجار بعد از ۱۵ دقیقه ۹:۰۰ شب تهران در لارک اتفاق افتاد تهران
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21731" target="_blank">📅 22:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21728">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/21728" target="_blank">📅 22:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21727">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رسانه های عرزشی : درحال حاضر قایق‌های تندروی سپاه در تنگه هرمز،از چراغ‌های جستجو برای خواندن نام کشتی‌ها از روی بدنه آن‌ها در شب استفاده می‌کنند و سپس با استفاده از رادیو، با نام کشتی‌ها تماس می‌گیرند تا به آن‌ها هشدار دهند که تحت نظر سیستم قرار دارند و از آن‌ها می‌خواهند که از عبور خود منصرف شوند،درغیر این صورت با آن‌ها برخورد خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/21727" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21726">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشاتی‌از‌ لارک هست ولی شب میلاد هم هست و عرزشی ها فشفشه بازی میکنن
😂
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21726" target="_blank">📅 22:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21725">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وقوع حادثه دریایی برای یک کشتی متعلق به بحرین @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/21725" target="_blank">📅 22:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21724">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5076i5YycexYsxkr9e0UUXzVsttck-hLyTBVSAX0m34eWZQBUrgrhnJGUINKsFFEMYP7HIPW-sKZVuHVVTHUdHliAPuiB0hGxNQr11Yvp7ub6uvrNlXrNS7fSJTEI0kdXY70cODqNnRgEDyo0TNNStbICQ84aMwXxCn7Hleq8uvsAEEzGuafQNatbR5b-wvqo0YwOt7D7APiOFjKvSu7H-bgykJew8K0Non1AJSakmiiSmtz3kCBeqU9hlovukEAAyzQVcTglHQIXQKKaJizrLYPTo0CDYSXuc1eDZabbucx-qHVhLQinjcWCTPzEYtxEtUZWv2G7WPFA8hvyaVQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگال کانال ۱۲ اسرائیل : مقامات ارشد رژیم ایران به دلیل وخامت اوضاع اقتصادی در کشور و ترس از بازگشت اعتراضات، در حال بررسی فرار هستند
مارک لوین به ترامپ ؛ اگر درست باشد، آقای رئیس‌جمهور، الان بهترین زمان است که مخالفان و نیروهای مقاومت ایران را مسلح کنید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/21724" target="_blank">📅 22:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21723">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وقوع حادثه دریایی برای یک کشتی متعلق به بحرین
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21723" target="_blank">📅 21:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21722">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شبکه I24NEWS:کشتی های جنگی ترکیه به طرز خطرناکی در دریای مدیترانه به کشتی های نیروی دریایی ارتش اسرائیل نزدیک شدند که باعث هشدار و سطح آماده باش رزمی در نیروی دریایی اسرائیل شده
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/21722" target="_blank">📅 21:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21721">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از تنگه صدا میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/21721" target="_blank">📅 21:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21720">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارش شنیده شدن چندین انفجار در جزیره لارک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/21720" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21719">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IyGJ_9Vr0og6DqKtH4-inLAgvC7wryzJS9rMjrLI6KudpeeSjbnn05mTSjPYZoDw6ro464MTSDe2pjVyD0RLoWe5KWgUjGpte3FroxzTPfHgJOQ2KIjgdP3pJWvEk2wjPlZ5gNjXEpaFnzhzvTnssyvhuqlW5U3SJV4w9zJ-d6kZTBVjNKRrspmDe_gQ4YwmsWloj8OqP6elCtxkMC-AkftBWgXXdeiZ9yqi9qc_5qikktJl4GTZHscTfyGn7IGQOUjdWa8qbOmgub4xZEBFeZybgXf0axxJ-p2-zS919Y7fcNMKGzFlu6Qe9hCDHv5-UI1rZNNgnG47p3fXsn5XKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی با تأخیر زمانی از حادثه‌ای در ۱۲ مایل دریایی شمال خصب، عمان دریافت کرده است.
یک نفتکش هنگام عبور از تنگه هرمز توسط یک پرتابه ناشناخته مورد اصابت قرار گرفته است.
این پرتاب دقیقاً رأس سه ساعت پیش از طرف دیدهبان‌های اتاق جنگ گزارش شده بود ولی من از ترس حرف مردم به علت این‌که ساعت، ساعت معمول حمله نبود گزارش نکردم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/21719" target="_blank">📅 20:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21718">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba3d0d56a.mp4?token=XxDYUxjOJNDua9RtWmuwLV-seUc6pmRWHr9hvRV1rycryXvDweEDk2wsp37Gz1D7zbbtojlv1gTSJu341S1dwSYb6TGG0LZScRkbyejieM6lxil_ntHu0AC140P936vFaP2AsLqp8E0no4WE_dYpj06y_sJ8-eCLaDTa40F_90s71wGlfJk-y5ixSy0PV4qNz1o0cuOSeCH1O341pA6KW0RgaEuaafFclFdZQObnZ2VPjv25IDJXyetcRd1rcjm3Y8vyNauPTj05AygS-g-MDReXNdLW2CbT6gszRfUaR0H4LzJorKnLZm4uVYnSdv2WCR26_Wiuq3D-_Nqfak8qAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba3d0d56a.mp4?token=XxDYUxjOJNDua9RtWmuwLV-seUc6pmRWHr9hvRV1rycryXvDweEDk2wsp37Gz1D7zbbtojlv1gTSJu341S1dwSYb6TGG0LZScRkbyejieM6lxil_ntHu0AC140P936vFaP2AsLqp8E0no4WE_dYpj06y_sJ8-eCLaDTa40F_90s71wGlfJk-y5ixSy0PV4qNz1o0cuOSeCH1O341pA6KW0RgaEuaafFclFdZQObnZ2VPjv25IDJXyetcRd1rcjm3Y8vyNauPTj05AygS-g-MDReXNdLW2CbT6gszRfUaR0H4LzJorKnLZm4uVYnSdv2WCR26_Wiuq3D-_Nqfak8qAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعزام بسیجیا با قایق‌ماهیگیری، برای مقابله با ناو‌های آمریکایی؛
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21718" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21717">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK1hRbVn0ZiCFDQb1YlwaH5tdRY2FqBfkoY4wuZm4QrBUKVz5xgvm-2C79_tMVMKPcNk1RPI6bWvOpYEfTF0Sd6T_vNstXKddu2d-FcddXOpqawNK8yEuxSUwbY3zY_s1r5Bn_EtjwONTsR2UUbs8zNtU_1mASHt2Se5F5v3ubjFkFkkFtIVFdTMdmSML5CDdvb_aWZQz3rJgK2qunSQDqFPN77fZtmfFH096WqiBqpxwkdWTEcrxSU864VnM6KURT6reh8BCcqfFhZZbtCC7ieGAMTzJgkln3Snh29vOHGnkyvs977bp6rP3aI72T0pKHxVrqlCSBdkW4fiFf_FRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرنده «CMV-22B Osprey» مستقر در ناو هواپیمابر، کد اضطراری ۷۷۰۰ را بر فراز خلیج عدن ارسال کرده و در حال حرکت به سمت صلاله در سلطنت عمان است
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/21717" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21715">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oy1pkXLSDPzePhnWMLlMnCaZWjZKPlW663t4Jz4VvTKDfF3f-TrT49xgtApAydVdOw7OlWFbVzExTreLpSH2ST6M5o-k1XHs-IxqZuKKf7UqnDnXVqc7HIj-5lnCp4-RIv9JM9TNO_VqHgRDwPCpgq3Gc34tqsNGt2-1oSZU1nz3MFIBnI5-aq7rJ7KhME1fuFaElYpnLd1ywYJLVu_o56cz8KoshxiZ04AXRnMjLwMpOOod1uB3P40fDgwqF5Pkwvi12N28g_9mUc2mmpFwjxHyQQwsCy11tY6PmcYbW_V9uQyDJYapdgey5VyDMIxATOD2Wuhcw3FEGPFYyDvZ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i91FBSu0a9UCFvzjcMUyTtURnsppXnSaEoqGuiJFggMZ4xQsnj6Qf4TwWq5QxkXttDMfzLZ-cZ7skIX2Xoooo6XsCg-QAmi8wvLKDxrzx530P9C8KypOOzjB0jh_puFHHrAcZ_0W-SHHovypbF25kMWI0ClnddjjqS7DNWqm5sdEJEi_BjejZEzRsxO_h7g8_R8oyUEkf2sLsKRcTG1j6fRbe-TdU1WnwplXADfjB_acGXt-pz6WSLDzBko2xI04nt4wQvqkO7jgOf18Mi225bw1Phx0025Wpa9mkYNNnkDtcLYSRabWvWZacHPNI2LQS0fS11mPD97aKRJWgPtODw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نیکلاس مادورو از زندان:
«این عکس‌ها را به‌عنوان هدیه‌ای کوچک برای همه نوه‌هایم، چه پسر و چه دختر، و برای همه مردم شریف و بزرگواری که ما را دوست دارند، می‌فرستم.می‌خواهم بدانید که ما استوار ایستاده‌ایم؛ با قلب‌هایی سرشار از عشق شما. عشقی که به ما می‌رسد و به دعا، کنش و تلاش همیشگی، همبستگی و حمایت واقعی تبدیل می‌شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21715" target="_blank">📅 17:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21714">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ناو هواپیمابر «آبراهام لینکلن» آمریکا، بامداد یکشنبه ۳۰ اوت، پس از بیش از ۲۵۰ روز حضور بی‌وقفه در دریا و پایان مأموریت طولانی خود در خاورمیانه، از آب‌های نزدیک سنگاپور عبور کرد و در مسیر بازگشت به آمریکا قرار گرفت. خبرنگاران در جزیره باتام اندونزی، این ناو را کمی پس از ساعت یک بامداد به وقت محلی در حال عبور از تنگه سنگاپور مشاهده کردند. این ناو در جریان مأموریت خود در خاورمیانه از عملیات نظامی آمریکا پشتیبانی کرده و یکی از طولانی‌ترین دوره‌های استقرار ناوهای هواپیمابر آمریکایی در سال‌های اخیر را پشت سر گذاشته است. آبراهام لینکلن قرار است پیش از بازگشت به پایگاه خود در آمریکا، برای استراحت و بازیابی خدمه در تایلند توقف کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/21714" target="_blank">📅 15:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21713">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یونیوز: ایران در صورت گسترش جنگ، شمال اسرائیل را هدف قرار می‌دهد
تهران هشدار داده در صورت گسترش عملیات اسرائیل در لبنان، فرودگاه‌ها و پادگان‌های شمال اسرائیل هدف حملات موشکی قرار خواهند گرفت و حمایت ایران از مقاومت ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/21713" target="_blank">📅 15:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21712">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaffcfacf3.mp4?token=Egi7ufwvGgfty7RqrAeMnYonR9XPaBQ0r3y7EwKgcki9CKDSFthRfC_DLswsgsZrDbR_uWt1gHL55Iu7CcvMFLmm35BPT03I3ut9WxA7yvIFCVTwQGBs5kUz5KhY7bDLkNNxUmWHhP9y01mBVnzg9sk9D-F_L2GPIU7Ta7rGF-LVb0Sx4cCAAHUyf2rQdisI5Yupkra9XHipX_olxNOnvDlm9CsohZwktJ6LeI-8eums13UD6nc_w2a9mZt1n6Mxx6SFLL65A8ZAYFiWiJM6c0TOhpNl8INCkEUglpkxlonq6AiJtEsqovkSTmjm6LJ4N4AHMSj2QP4pkiHKv0c3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@WarRoom
👺</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/21712" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
