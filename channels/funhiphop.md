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
<img src="https://cdn4.telesco.pe/file/Jpu_gqbddtMMvReKYupgzpQSUY1RPa1n8OHEOWanyUEkDDb7TtCK9yiQvsrlvjN30xfnLCOKagVVJ0ESog3jdRrzkDBZnNBypRX7PcVBA6939hAGeiiG5ozBkX3JWrK9SYWtvLO7kWXyPxWuUQ-YtYhEZ2sr7xgHLp2y6YYgliPWOcKycfcdp200Me3F5n1Lh6rvQPvkGpBrm_0JEO1zCqY5wDcRtJhD4SWl0RAJGzYjVkka6GZlPO7ts--jUlyXq-bF6SUZNwbI7mlZWtKP0Z7weewdjB02LOhlGQx8UvHPuiM-JV_7Bdb-b5IyeE3lQ7q-fhq8uKFTPQxp6ySgyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 178K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-76572">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:  اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/funhiphop/76572" target="_blank">📅 19:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76571">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">علی عبدالهی، فرمانده قرارگاه خاتم‌الانبیا:
اگر اسرائیل ضاحیه رو بمباران کنه، به شمال اسرائیل حمله می‌کنیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/funhiphop/76571" target="_blank">📅 19:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76570">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcheELuedRslSjUVja9CEYbjzQj8vqNIV-jF0IDb032Fa3G8vEq_dRfOzP61rQWK0bVXeRj-RYmoGjhq0sYz9tpkvo4aiOV8wYGfa1H4Xv3LkU4-wmmFlZlbXtk2iwMW3JVQ_ZEUsEZcC1cVuWVxbHGRdy1q0bT1bmvw6uUBBcJHkzRFN3_9hZ7jcV2uKtmQhZuZtxGuiTvAju_2w7gzJ9fQTj5uK9F9qI5YKu4bbm-xltDKIaKFWTzbhdPVfxxWJE9960bdbdZbhwdN-HsJFyglVaEYOm70qz2ALsRxVGa0xDAVaaca-O6JBN-3mg6BzpPzZc72hGIx9Mz2MbRHGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جهت حصول اطمینان اسرائیل از روند به شدت مثبت مذاکرات، الان ارتش اسرائیل برا جنوب پایتخت لبنان دستور تخلیه کامل داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/76570" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دفتر عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داده است که احتمالاً یک حمله موشکی به یک کشتی تجاری در خلیج فارس شمالی، ۴۰ مایل دریایی جنوب شرقی ام قصر عراق رخ داده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/76569" target="_blank">📅 18:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=u6Wpw6mX6uI5HuINxK53ZXwlDPwwCJZ0GW0I6fbtUlKgrSWTMrfY9YA6pYAJ5-2FjYmFeDaXHG88sVGx8KmjQ14lLAGvciK224Q_cCfUDD1lT-n8oBL94g-KXHIMzwfIXIIrvoOGB1ni1BXWYSCw2mTVkIIGc9eQkEo01JizEbgvoeuy5MysjrJJQulkmUqYTAXxFHwtj__q0WcoVgWyw5ipxGfb1AFS0czEki315p9PW4eR0mnMYlGwN7oebhUOFhH06G1LSOwhtadDcOgX5XL1bl9PhZonvOK-FOYO5cVu03YK90iv72cYFXJdSdOgpKOy9n22m4IGZJEZNB5lTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e1df4a9c.mp4?token=u6Wpw6mX6uI5HuINxK53ZXwlDPwwCJZ0GW0I6fbtUlKgrSWTMrfY9YA6pYAJ5-2FjYmFeDaXHG88sVGx8KmjQ14lLAGvciK224Q_cCfUDD1lT-n8oBL94g-KXHIMzwfIXIIrvoOGB1ni1BXWYSCw2mTVkIIGc9eQkEo01JizEbgvoeuy5MysjrJJQulkmUqYTAXxFHwtj__q0WcoVgWyw5ipxGfb1AFS0czEki315p9PW4eR0mnMYlGwN7oebhUOFhH06G1LSOwhtadDcOgX5XL1bl9PhZonvOK-FOYO5cVu03YK90iv72cYFXJdSdOgpKOy9n22m4IGZJEZNB5lTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوه قضاییه: مهرداد محمدی‌نیا و اشکان مالکی رو به جرم آتش زدن مسجد، تخریب اموال عمومی، مسدود کردن خیابان ها و درگیری با مامورین امنیت صبح امروز اعدام شدن.  @FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/76568" target="_blank">📅 18:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">فدایی تو تجمعات پاریس  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/76567" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=lDCN2vl2R9eWMQNpuIRQor5UNS1COLD_b6uo7CsfH0LTjRRSxsOf0rIn3JyxnfVhInRD4VeSqMj_SS2-LJRk_OGgDwChZz3TI7Ky6NE9RFDscO0FfYi0Y79G9XQlgobPFinLtFWbZ-cMyGdNbx7pbmlzxtgpxwLjzlvGJIz9v5ospvVqD7rLvOhTnevMbn7dtI2aR2rbBYGUxJHe8fOBEthjNZNuTmJ0qnq5g1pdDl3neMPxg4yCIDhRuwyYTGmio8D_v_p_KXnRbZxvenX6Vu0zJXdQwJTPwdwsKumxF55jtSOHZnX0igcGORyWQaQnBD2bIJJM594rF8WEnaGX0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b05997ae5b.mp4?token=lDCN2vl2R9eWMQNpuIRQor5UNS1COLD_b6uo7CsfH0LTjRRSxsOf0rIn3JyxnfVhInRD4VeSqMj_SS2-LJRk_OGgDwChZz3TI7Ky6NE9RFDscO0FfYi0Y79G9XQlgobPFinLtFWbZ-cMyGdNbx7pbmlzxtgpxwLjzlvGJIz9v5ospvVqD7rLvOhTnevMbn7dtI2aR2rbBYGUxJHe8fOBEthjNZNuTmJ0qnq5g1pdDl3neMPxg4yCIDhRuwyYTGmio8D_v_p_KXnRbZxvenX6Vu0zJXdQwJTPwdwsKumxF55jtSOHZnX0igcGORyWQaQnBD2bIJJM594rF8WEnaGX0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی تو تجمعات پاریس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/76566" target="_blank">📅 18:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">با اخباری که از سمت خبرگزاری های داخلی میاد بیرون
منتظر پرواز دلار به سوی بینهایت و فراترازآن باشید
@FunHiphop
| ALI</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/76565" target="_blank">📅 17:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzBSfnhlUrXuS2yDVm9KB_AkpYFY03uz59h1HTx25ApXtsUk6fg7uBLSUVjk4Xjd_ZNPjSf1_Cli09-m2lWTsSEh_NTW8Spm0LalsvIyB0RSAvtlmYkUWWoELeGtG4WaQABG648IHsG3_nyPHh0-pZV3iNeKcfZnHMqWruTRKEQyS0CqTjCJ5dG41CQD3eGtW41TGNekN8Hhdi-Rj4JkkzmQo54wvaRIoSRfdlfngG-zvkKVdXGUQ5_bHxW9t9cmUQwAG80BYoi3x8wKorIySWWmuKtpYhw-oSUfCXMAwp0RbUOYYXASpqHJq2eG5PgKi-Iqfvu3ya9Ijl4bHdZQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پنالتی هرموقع یادم میاد تخم میکنم.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/funhiphop/76564" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhPujhlD2TEfko7HYl0CX0mu3Vl3n2NvY-7rmwDv5Bem41fB9Lkrq0sdRCfiHl-Tf6__K8njQfW1BQz7k_LJ60b-BRV3FCML_QhadCFZEuuPM48gtu3Jq6jsOv8VhYqJTLAX0Zlgh0Ntw89ebe1ukV_ErOVFCHz4v0pmMx2pcKMmL3FJFSxjvurLhUjkBF8r55PAhSTwlIsKc3ER-3VY9eTPzKGfzvT1-kd_ci5SIyYzeEnGZ8KdsGHDUDxCPXPdjzYY5laq_vuwOwQOvInI2Ytj-vtc7oBiVIrEcNEhow6lF0y1WaN1cXPFf1OHdaYdQ20A4WpLZDkB94NFLHDHZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده چجوری روت شد با این وضعیت نت همچین پیامی بدی؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/76563" target="_blank">📅 17:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3SXCOQ2Ok15xuNV51K37k27gfpPcw_Cm7G1-3OOppxM2J4qvMoqXZYbzL3ZSiokHdphN-z_MNLV5WqyJMTxwAJXsNlyv3Cgj3X0ZYxXxbkiR1obWOaPfWOmijX1_0O58kz4WteJi5c2pfXNRSgPzMj7sP_YpcbiqC1O3HkmeDBtxv1XfC63W16-2YG69lzWr_pAlJmHcxtDUrA3K3HdL4-EHyB9TXOGlg7ZVcrCFJ9SqysumuV7cG-UDRGz9_zlpZbtlRtfBTYlLD56tqpKnpxu6BmLayhvtvZeKjJywlAiXWkXjdMtXcnkL_051EHaLk3rkFM5cO1c11mu8LltdQ.jpg" alt="photo" loading="lazy"/></div>
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
g11
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/funhiphop/76562" target="_blank">📅 17:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/islRATZdIZQReX8VD1I3ERQyWi9UnA8jEtpRsazqQSQLwxIFeDfWxNTxfXNhFlUYZ1GzIdE8oepC6eHFEjIibuwBazLzBWvtBdwfB6fbbKx9GUhaFv_YLxMjoO_PCzdDiOSxF1lYcXVjvv_2-C8y3EbzxpsmJr52YOMDxZRY7qTddF66m3P1MbvJ_5DLLUVhnLaavuvvmV8U0JgeAh6N0-I1SpeXDt1rZli50ifqXsOcDh783UdsaSHXhwvGOuCp9WGWma70TdR7dML2YQthodaybUBHrqw9M2itx3G5ncVE7thLsmwHavzHsuBz6zWCeyKl5TEBiURIsqRNXLwjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم: ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند  عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی…</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/funhiphop/76561" target="_blank">📅 17:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شبکه 15 اسرائیل:
ایران تو شروط مذاکرات علاوه بر لبنان، غزه رو هم اضافه کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/funhiphop/76560" target="_blank">📅 17:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76559">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری تسنیم:
ایران تبادل پیام با آمریکا را در اعتراض به جنایات صهیونیست‌ها متوقف می‌کند
عزم نیروهای مسلح ایران و تمام محورهای جبهه مقاومت برای واکنش به جنایات صهیونیستها و گشودن جبهه‌های جدید
▪️
کسب اطلاع تسنیم حاکیست که با توجه به تداوم جنایات رژیم صهیونیستی در لبنان و با عنایت به اینکه لبنان جزو پیش شرطهای آتش‌بس بوده است و هم اینک این آتش‌بس در همه جبهه‌ها از جمله لبنان نقض شده است، تیم مذاکره‌کننده ایرانی «گفتگوها و تبادل متون از طریق میانجی» را متوقف می‌کند.
▪️
توقف فوری عملیات تجاوزکارانه و وحشیانه ارتش رژیم صهیونیستی در غزه و لبنان و ضرورت عقب‌نشینی کامل رژیم از مناطق اشغال شده در لبنان، مورد تاکید مسئولان و مذاکره‌کنندگان ایرانی قرار گرفته و تا زمانی که نظر ایران و مقاومت در این زمینه تامین نشود، گفتگویی در کار نخواهد بود.
▪️
همچنین، جبهه مقاومت و ایران عزم خود را برای انسداد کامل تنگه هرمز، و فعال کردن سایر جبهه‌ها از جمله تنگه باب‌المندب، به منظور تنبیه صهیونیستها و حامیانش در دستور کار قرار داده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/76559" target="_blank">📅 17:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76558">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منابع داخلی میگن مذاکره گوز شد توش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/76558" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76557">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UePJU7leLVMrcIwOMmXjFb1tNr3uz8kNGfO4iWgXRxlCE2rlqyI3URm3o2LuZiPm5OdtB7Izisjtg-UQMRF_KDpdrtrDeL_pRWX64kw2fdyAkKspjoTcYTjFIu7lHBZtRwe-Db-NNuUYovKzc9nA710HTAxvc0ba2lcffXCRdhwLwFpQG16R4dnGMoc9Nv2hRr8xLJVPmxfANyxvZNA_rgBjo2LiZgAs81N5ec9nFi-_Lt8E9504nzUMIB-Aguua83pjGw8Lp9eGzBvyRP3lkM-UlhzA1CAprD5mljEVIrYk7LgYLmXqtLddMNEaCGUYmgZdN7I2vkzn98D8alQ6TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری رخ
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/76557" target="_blank">📅 17:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76556">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVAcm0Fk1khuRAYpO1EqGVhEBUst702pd-XzEYUsxbqNRyEndw645ttrVF_guzvw9EsM4Ily5g-mbwZpSI5Bq4RgFprR8sLDQFsGxg8O16Qia6D0pXGcXmxANnG_KRCLA7IcceyujedQJTTvP19EOHNupl5dU1Kz_9Cgw4IszhVxGSbSiqysqgSRg_FyicwvRZM0c1VTIxqpkPLh9-Lti1_vglOLgAkiQth_hLZjxTp3_iFzZJ88vq-NFcNhmFJCDCd8X8bk9F0JwtyyP_iq5Qyxg0P0Am_Vq_S-9Y6saD0qJrRSaBtZ3qNy9M7AjH1PcAnWWqlJU6psOUHrWsMAaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوزو انداختن وسط کفتارا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/funhiphop/76556" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76555">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دعوت تتلو به جام جهانی مطالبه ملی ماست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/funhiphop/76555" target="_blank">📅 16:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76554">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">آمار رسمی تورم اردیبهشت 1405 منتشر نشده.</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/76554" target="_blank">📅 15:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تتلو بعد از دعوت نشدن به تیم ملی:
کس ننه قلعه نویی
👿
۷۸!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/76553" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7UlvDIB9aj7ANxENkgTU5NqJ25lZ31PxDmZU9csycd-1ejnVxl4WWmTxlt9NqYERkkUx8d2ohGxT06lHkvqdYyavJme_wmcoSXSRIMaJhHvlJ8w80SsGNqVqlktczyBwmIxft_A2XtjzZlUMAcg_xTLGs2-dFjTxNOQP5sRjwk8ts2W7TN3E3ojvllsLhxLf1HkDiRkZHSqNEAw3WQorZwnAJgBumnMy4XkmjSLCBYWD7tyT43p4MA1ePWvtVtddGwwR21OblvCQMnqjNQJd8v_i74U-CYUkXL-8PmhwKdfbueOzlrnLZoBqshdwjv2lYo2Fg_EREkygGW3uNzEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست نهایی بازیکنان جمهوری اسلامی برای جام جهانی
پ.ن: حضور مهدی قایدی و خط خوردن سردار آزمون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/funhiphop/76552" target="_blank">📅 15:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">باقر جون چرا داره یجور رفتار میکنه انگار من پشت پرده لبنانو فروختم صداشم در نیاوردم</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/76551" target="_blank">📅 15:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترویس اسکات دیشب تو ترکیه کنسرت داشته، جای خودش یه سیاه پوست دیگه رو فرستاده براشون بخونه و نصف مردم اصلا نفهمیدن خودش نیست
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76550" target="_blank">📅 15:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA2G5XwQu4JW3AdluxknsfKxvbbFwK7AOszKCkwAz2cpVgBJfS77gdUO_tCGZmxU3qHfPU4b-MGQmAPWj7hTKQ6BIrQuRm-JfZ8WtYGtCvNz3ULVvF6f16L0BflEjk2goFJlqIBy5tc0N44tgb-x2u6mqa2fzxIHG0v6rlWlH1VujldDr3C8aOOjxoJrCVRSFCf4vdQsEV4yiUB0KtbnN0iZQhvOL3EVgqr2mCSWJkdqZAJdgnGX4rAuELdVqIKyd6WpADWoXASeClmuOaggThGiuxOvucdHEg7yHoCqDDYXTWyFQYx3C1HCqIPn1oEO1wUfkVuecv4ch05BMPjSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرفسور
عراقچی: نقض آتش بس در یک جبهه، نقض آتش‌بس در تمام جبهه‌هاست
آتش‌بس میان ایران و  آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمامی جبهه‌ها، از جمله لبنان، محسوب می‌شود.
نقض این آتش‌بس در هر یک از جبهه‌ها، به منزلۀ نقض آن در تمامی جبهه‌هاست.
آمریکا و اسرائیل مسئول پیامدهای هرگونه نقض این آتش‌بس خواهند بود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76549" target="_blank">📅 15:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حاجی اسرائیل داره لبنان و میفرسته قشنگ 1400 سال پیشا
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76548" target="_blank">📅 14:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76546">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HE5pCofikeR1dtznOxaEsqmPhjBbCShRBlk2BAfeOLEmmKc0BpP5VhM9NNAidKS421HhWMtjhoZZKMOGDGq5F9Mgpb4zqCfHlH3Py_OonaVG81BKL6n4wbppqkKlpz813kniQwdtnEeNdAszkHNJew8xbpskGwqcw6gYvUB0aBwwAYmYrJz9EvM-x1JReDteEzbFqbFQe3OmSVM9_1inMuo9cxTt7APYFSC4xCub8Jt9Q5RPrQgOS_Js_594x75yNZjiSRsHcgKxnxIRhqN1MGpY_S-AuPbAEkYqDQ5Sq_5yrlQL2gX6m_IQzWR_KpHD08qeulxPYsR7IirSmGh4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2HItj6nHW0JiIO0E5-lhvyvzd00wutobS3W7eUZ5E8XlKnImRiEKhasg6NpdfL2VRj5LkfLQ_DRnk0arfikrtmBk0U7zp0L5TB94d7F_Bul-R2Ox8ek_BMInotQY_xcBKpYx4U3PxxoeJfe9fBJgo52r9RqVDKN-5XQxdDI3JlrXe2YHYNcgaLRpXpOZB2YSurx5x2OBhD28vuwMcl3E8B875XeAqgpmE-Aizyu3cuxXECLZV3F2lRIKiMtmt70E49fppYukeAKHMc233WcRCO_n43JZHK9UB_o71omdmnzc97oFZ15NS2r7DhlLWwFc_-9Hc1VWYXr1-Q5ufvxAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76546" target="_blank">📅 14:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76545">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یکی به من بگه این رسایی کیه
اصلا چیکارس تو مملکت
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76545" target="_blank">📅 14:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76544">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز تو دانشکده دندانپزشکی گزوین یه مرده زنشو که دانشجو بوده با تیر کشته بعدم همونجا خودکشی کرده   @FunHipHop | blue</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76544" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76543">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امروز تو دانشکده دندانپزشکی گزوین یه مرده زنشو که دانشجو بوده با تیر کشته بعدم همونجا خودکشی کرده
@FunHipHop
| blue</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76543" target="_blank">📅 13:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76542">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قالیباف:
محاصره دریایی و تشدید جنایات جنگی در لبنان توسط رژیم نسل کش صهیونیستی، گواه روشنی بر عدم پایبندی آمریکا به آتش بس است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76542" target="_blank">📅 12:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76540">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpgRLhx3NQNQH-4LyrQP7ApZBLhYjlDRScuOPwPke1fcwWYZabxX2IATQUA-wSwnbb_lmNoDMrn43tlqOJfuwGE7julpaHxtZtdZwfuSofl_YHnj1PGW-e3MgWvsPslZuF_EIWPuM2slDV6r5E5re2PG04vLg1VogQbM-yScJwFT9fzzFW35XK6Op913QRqZHVK8ow8i65tLZn-0HPteAQcUNjeJAMz9k5P5V0JSd47MbeKf17rP__JmfsBNWljVVD8sS7y8VwXM3OgZA0lGcqMP_nBmz13-dDegHcdnIYELuAK4BSM0CYHB-fj2F5ZnSBcF_V3C-qeIC_Ivb66A3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQhi5Qi6EL3xFz1lxgoL7S6vi5zquFFzkYBJK6viclfFhQ0TgMMCQsoKMWgudyaEZLGgjH7cC0yp1fant6WOKXOOPny5H-HnUW8jJMpxlTMmgemp9ZLkgeGfcp2C9hQY80szSJAUaM774yZdmU5GkaDZEdev0_v1BLbZjFmxlbh9ewlDX7gMndBGW1vNFVHfQY3ypcLvWEMl4J92M1CbFhdAiEylQ3lCl01fufz9aB_g4Nas1F2rugdhMy3u3Ensc4KRMIjuCUKo8NKl9pLeOcSK2YsFHQwBTGKFRi3M3mHSdrIw2vi6Ekttpvz5XK5HnDTY7ay9k_2l6UTnZ2fzsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هکرهای سپاه رفتن اکانت اینستاگرام جان اف. بنتیوِنیا، درجه‌دار ارشد ارتش آمریکا رو هک کردن و این عکس رو پست کردن.
پ.ن: یه بار دیگه‌ام زمان اوباما کاخ سفید رو هک کرده بودن و عکس علی رو گذاشته بودن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76540" target="_blank">📅 11:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76538">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">من در کاخ سفید داشتم قدم میزدم ناگهان یک ایرانی از 300 متری به من سلام داد پس من تصمیم گرفتم به ایران 2 هفته مهلت بدهم
آنها آدم های فوق العاده باهوشی هستند ولی نباید سلاح هسته ای داشته باشند چون دیوانه اند و به محض تولید آن را به اسرائیل خواهند زد ما الان جذاب ترین کشور دنیا هستیم به پاپ بگویید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76538" target="_blank">📅 10:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76537">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تهران هم صدای جنگنده میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76537" target="_blank">📅 09:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76536">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oypgOH4rDAG92eLrh1JB7GVCWF7XLRt9LRUvfBhLZyCa5Xmd2GHb20f3Z0WY255gNzNfEeFg2SawVzOav6zTwy-TBDpK56OalmDYy4PYoiLixTjl2kbe7vrAltcQfXHTpGpDOb2-WmbqGJhbdOpHXnJP7cwPp1zApVFTH2uic-ptiliSrnEIZfBNiw4RaPktBVqs_RdzRfvr8isXvf7UNHnBSXkpScKKjL3y8tsiz_irMkx1dGnytPd31xsOy8DNm5ZXuubFy1xtNmE38OQ6fCf5bZfLmelLR1Lae6AsUtnvPnWldZY3HIUhwujiMwo3w7LfUJx6bLqd-BQXCmgG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه: مهرداد محمدی‌نیا و اشکان مالکی رو به جرم آتش زدن مسجد، تخریب اموال عمومی، مسدود کردن خیابان ها و درگیری با مامورین امنیت صبح امروز اعدام شدن.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76536" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76535">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76535" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76535" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76534">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJStrVwLUGfgqBKTcE4hDI9XdYcw9-mq8JZeIuv3FnD9UEaZiewvu1vmmKqxTnJ_IvwGzm4PZs2g8jvrJuy9zdvxNwWEgKVZEqkxnWfaCOicq4PhneufiJHpflJrdyAJ163dvncOT2QAltP6fK8mnaQdgV7CB5skTWrYYetFMwFCkdtv0Oy9lyhYfQSXFOj7au3cRhxlNdNhmmORQdqlJmVA-2rQs0Vd7DKsWPDmo8uy0hPFxq6_GSWgBWw5RHOfm1QNLBPNZTxCPgazM2oWwbfx7hae3Yew8VWIS0-Z7uGXjr5K8bAtKexWWvXHiJvufr_kjfK8AZJIJTH5mJqVzw.jpg" alt="photo" loading="lazy"/></div>
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
r11
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76534" target="_blank">📅 09:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بندر عباس انفجار
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76532" target="_blank">📅 09:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVnHhxTD2aDvAk2pBDs9TOamarqHl7g4RQPdWhT3V4j4wI7USf4DfxozYLIIUo15FROCcQIfu-zCiVDrVa0uib3qdws185FSWtoxzz3ATAlLMMkDNOrk486MgAuyPfQhe-HNRTgFUn6O_E4eTnosMFDwbxQFMzh6-Fb-K9nsZiL_9AA9o8W2vsMdgt9EnPd_6G1xhg5hR6E9TZp8NkQXWLZrxDc3j4S-Ix4prrfKyLcXOLSt-tChqG4GX84oRpwAfAG3b3sxlCjkHteEs8rNvVZvSTyYbIA4plZd-Rt1E-XI8W0zr1ZS12_F74z-1LnLvDLv_1YM3eyw-7zhmRqBMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ خ       :
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده و کسانی که با ما هستند، خوب خواهد بود.
اما آیا دموکرات‌ها و جمهوری‌خواهان ظاهراً غیرمیهن‌پرست نمی‌فهمند که انجام درست کار من و مذاکره برایم بسیار سخت‌تر است وقتی که سیاست‌بازان به طور مکرر و با سطحی بی‌سابقه منفی «جیک‌جیک» می‌کنند که باید سریع‌تر حرکت کنم، یا کندتر، یا به جنگ بروم، یا نروم، یا هر چیز دیگری.
فقط بنشینید و آرام باشید، همه چیز در نهایت خوب پیش خواهد رفت - همیشه همینطور بوده است!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76531" target="_blank">📅 08:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وقتتون بخیر، امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76530" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سپاه:
آمریکا به یه دکل مخابراتی ما تو جزیره سیریک حمله کرد؛
ما هم درجواب، پایگاه هوایی‌ که این حمله از اون انجام شده بود رو مورد هدف قرار دادیم و اهداف موردنظر را منهدم کردیم.
هشدار می‌دیم؛ اگه این حملات دوباره تکرار بشه، پاسخ بعدی  ما بسیار شدیدتر خواهد بود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/76528" target="_blank">📅 08:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXWfiYT4PMuF09FvoCqxxQomdsZbkgeuRrAkM-R0_XHZEQxElVO6iK_BXWhc91uMymnNJRr0QHlwBhlIXwHeYzRy5Hv9fePW7i6FVk8_OVv0ujiRThrG0yp_VaFlRJw7cijFr-ML9iK_ncRe3XEY1RnJBFSih8u4thLIe5QzfIqIQXBdO_qBL6wpTvXTiBtiH20yhQUKzEwQiR_3DHDtRzFBfo7dt3vNAAyqQrWvWJ4ln37vJ7ds1GJlNkdGXHWvIOe_ajn4TioZjGKvBlBJM-W8TlABoEqQTbh-kydf8ZTWynPE2TkGuOUAwx-QP5L7yjEkPSL0oKLePOVQjHJDtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامپا، فلوریدا - فرماندهی مرکزی ایالات متحده (CENTCOM) این آخر هفته حملات دفاع شخصی را علیه رادارهای ایران و سایت‌های فرماندهی و کنترل پهپادها در گوروک، ایران و جزیره قشم انجام داد.
این حملات سنجیده و عمدی در روزهای شنبه و یکشنبه در پاسخ به اقدامات تهاجمی ایران از جمله سرنگونی یک پهپاد MQ-1 آمریکایی که بر فراز آب‌های بین‌المللی در حال فعالیت بود، انجام شد. هواپیماهای جنگنده ایالات متحده به سرعت با از بین بردن پدافند هوایی ایران، یک ایستگاه کنترل زمینی و دو پهپاد تهاجمی یک طرفه که تهدیدهای آشکاری برای کشتی‌های عبوری از آب‌های منطقه‌ای ایجاد می‌کردند، پاسخ دادند.
هیچ یک از نیروهای نظامی آمریکایی آسیبی ندیدند. CENTCOM در پاسخ به تجاوزات بی‌مورد ایران در طول آتش‌بس جاری، به محافظت از دارایی‌ها و منافع ایالات متحده ادامه خواهد داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76527" target="_blank">📅 08:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JivsMGHXE0yKFEmwuaoJtlp8VRfGsJdcs9mJv9yeTsZnNUepaJkZz1l7AnjBL8tm7YzMxqi6kSMy4kka4cPTEtUI_bsiufQ3DD4GQ0R0adz2CDoFo6AjA2fKx-Z7_QnByE6gH4jgjQdcG9v-TppeM19wbFOLG3FZgmG11jycM_FLupPN5cZFtrxF0peChPgQZz4X_x6t3kE1UGGHc13W1BirBZof9h7msqtehsQT6qgIq0I_B7gqEc6Yd45a3bnXK2MInfgY7QT9WfUy0qqf4Samof17EAyW2fBpHsEaE7BvOHiVeUhyO9nIGmmF0nXmCE8P-IssoXerdZulUTWufQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر تتلو تو پست جدید یوتوبش برا حضور تو جام جهانی ۲۰۲۶ اعلام آمادگی کرد.
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76524" target="_blank">📅 02:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مرندی: اگر نتانیاهو در جنوب لبنان متوقف نشود، اقتصاد آمریکا در ماه ژوئن فرو می‌پاشد، زمان در حال تمام شدن است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76522" target="_blank">📅 00:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">جدی باور کردید یا دارید شوخی میکنید</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/76518" target="_blank">📅 00:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝕻𝖆𝖗𝖒𝖎𝖉𝖆💤</strong></div>
<div class="tg-text">مشتی کارت اصلا خنده دار نیست واقعا الان من بخاطر تو کل خانواده رو از ذوق بیدار کردم بعد ریدی تو ذوقم؟
زشته کارت اینجا چند نفر واقعا شرمنده شدن جلو خانوادشون بخاطر تو</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/76517" target="_blank">📅 00:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromarshia</strong></div>
<div class="tg-text">کیرم تو کونت من اقامو بیدار کردم رفت پای تلویژیون دید چیزی نیست یه پسی زد بهم</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/76514" target="_blank">📅 23:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkbvPkQ2x1kQleqtooFllTIQjYLVYnXlOFP2r0NyhDMqDh7rdD3VblYnqKGxZVlGH-CAw48wJI-lPIK_H_m_9ikgq83Lri1GwHbHEbjURAPoSLy09KgQPMQoWJELTZ0Ztl9d0DT0JRjX6Y2GzVT4BTySqeM5Vcem-j9Y5m7j4WgBbcidcVOzYq9GbGqicL0bjPddDxQJr4OUU30Lwz7TtjcAqpVkG_Zf8cXRcyDSJY5MhBC6KU_2ugUF269PtEkTcfWIKkY8w00YflT3fWbYpSDfSC7YtkFrg237mL577P6sMhTxItfkhRQ-nF5-Oo6R60yIIOJTjl3yb3886AsBKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی  ارتش اسراییل تایید کرد  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/76509" target="_blank">📅 23:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuo6qUQcI-Bk9gOwFiQoaLH-exigVo9bsGDdm6DoaP40zFwXwlE3vFcc954x8bP9FCIbqtZys_Yvxph_Y0YM4zB3M9LbAfP_kEbH5CVqK8iMO1h1lJPKkgYztmpCAyhnLk45FuzDbY6mECNGwdARqKVD2xVsFVwPMpgAo1mJBBWdo9DL88zrS6UsW9BzoyZ-3OhE5Ldzs4QFhE69WXj31IKdeLWN6U9x6qzD6jo4lZhewS9T9RtJger1YeIk5q7XCvNv6T4JFMdRfejTHCobvVL8HrlOUfessqLQ8BCFxEjT6pgTbF9pep5HNH9X_mkDSeZnjnktQkER17kHofPdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویویویویویوی
ارتش اسراییل تایید کرد
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/76506" target="_blank">📅 23:38 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/76504" target="_blank">📅 23:28 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/76503" target="_blank">📅 23:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کار اراکی هاست
یک ساعت پیش تو کرج فعالیت جت های جنگنده گزارش شده بود
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/76502" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تو اندیشه تهران یه خونه مسکونی لوله گازش ترکیده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/76501" target="_blank">📅 23:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جدی مگه فوتبالو مردم برا سرگرمی نگاه نمیکنن، چرا باید طرفدار تیمی باشی که خوشگل بازی نمیکنه، حالا اصلا هرسال ۱۰ تا جام بگیره
جام باعث میشه تو سرگرم شی؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/76500" target="_blank">📅 23:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQffNOCJjdziLF5IEyj3R-KG2m2lRzONpVoI4sYiARgQfk9v9jpEhd2mWrE2S9MlpiTfQXzto5DfIKlfDtge5T5hOMuSW7cvjQ7zKLaAUrwPuwFrtUHj2GZyfOwERQH3W4MvAbzyGwWKxbbS1Y1aHm8Ee_qzkl2UnQ398L2kllGTa-_CWf8oolS2tHDhUSYawuCthjBLdlnkGxbHjHnmtFJRtEoT0PWfzArGjDbV9Oqm2UiGsE0R-efuzeN1p1kFgTqPr71CtqNzfhiEl6kV4el-Ecz7GbObnlEnNdq2PhJ8hqECPqj5r1_Ga2uyfkxl0SPz6hu5FhmLJe1lc4VhyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال به اولین تیم تاریخ تبدیل شد که طرفداراش بعد از باخت تو فینال لیگ قهرمانان جشن قهرمانی میگیرن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/76499" target="_blank">📅 22:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پزشکیان :
استعفا از ریاست‌ جمهوری؟ من کارمو با قدرت ادامه میدم و فقط شهادت میتونه متوقفم کنه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76498" target="_blank">📅 22:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/76497" target="_blank">📅 22:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZWTIkpca_y15Y3N57XpBeuBuQkDld-aTMjNbHnK_0A6w3RgZuAOqhwR9908bhFJejAjQSxbpm1CzPolqIlpyOOBP4KTM6uFNcSarhXcf4SdgnkQYP006MItf6oROlCMPML1Wdb4Su1TqSeW9tORismvJW9LQ7jasmjPmbwEEzUXm9Ma1FULEtSC1S0TLncHvcA9x3Ojd1vMjb_2P5bQ1D-doKlRNZ4vbdUSOiZCYhEZuQUIz2EnXSc5uaLPC4tcf2ddE5G89GhbuaBcZC1GSKJGr_XQufg0iDxPgVi4cj9F2FOLyx4ERwialQZ5yE6NaEGzsMCI17zQeWJ8dPMKfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76495" target="_blank">📅 21:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">آخه فکور (منیجر پوری) گوز کدوم کونه دارید استوریای دوماه پیششو پوشش میدید، خود پوری هم به کیر کسی نیست دیگه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76494" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پزشکیان زیر نامه نوشته
من نه استخر میرم نه با هلیکوپتر جایی میرم</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/76491" target="_blank">📅 21:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9co1eqYs0-uUDr6zQlcrHzcv6wJrPIeqdOmhNdxkqPF9rl5dmKjSCErlpXzPUEWRKRMgIMhxAsfDH4EfG13priNVMaJWT8YO72iIDuelpvV-ySl9lzVb70c37i66NZzegRczTX30-TF3tAg0P9VtL3Buo0NGrWVGgqEqT6H6m0r8naSspZKU3scftJSAhV9WWzOeZHTzk7lJvpJDxEXHg5xjcj6hpgpGRcDDabuz9s12r6cj1J-wLmGZWSTXBm9AOp3sC6MEgBwG6mxBCjohr9vg5586EJ0Ph3nunJMjgWENzi1flUc6VYDwXYJ6PsCfaDLJRXylNmRWJhLepfZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفا نامه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/76490" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرض کن امشب هم قالیباف هم پزشکیان هم مجتبی ترور بشن
روحانی بیاد روکار هم رهبر هم رییس جمهور
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76489" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تا 1411 با پزشکیان
✌🏻
@FunHiphop | ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76488" target="_blank">📅 21:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76486">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الان مثلا خیلی شفاف باقرشاه داره میره تو کونمون</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76486" target="_blank">📅 21:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">قبلا پشت پرده یچیو میکردن تو کونمون، الان جلو پرده میکشن پایین میکنن تو</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76485" target="_blank">📅 21:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرگزاری بسیار معتبر تسنیم استعفای پزشکیان رو تکذیب کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76483" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در جریانید اگه مسعود استعفا بده نت قطع میشه و کانفیگ رو میکنم گیگی ۲ میلیون؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76482" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76480" target="_blank">📅 20:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نمی‌دونن تا گودال ماریانا هم بگردن پیدا نمیکنن رهبرمونو  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76479" target="_blank">📅 20:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بعید نیست این یه تله تروریستی باشه تا محل رهبر لو بره  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76478" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76477" target="_blank">📅 20:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مجاهدین خلق از 021کید به جرم تهدید به شلیک گلوله شکایت کرد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76476" target="_blank">📅 20:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76475" target="_blank">📅 20:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqvnHW9Zcr50ifpIyUURc7dJC9HDARbsIsJ5TKvBCWnC7qxCZD3kx224L3UP7zzKXQ8uNcGJEWWg2wM3bt1cVtw7hQNflWZg-KdR4dUk6VVdaLIkfKJ61BGji5ezgv7BzbDj7ekyRaelhpRDmQmQpH6-nh4d-qAvJaDf_hAyvSUVKjwMcY0rMAJcHwKSHAVuijk39MoCKqm6zD17OylUMaXZZ_iOItTq2PLeZ1DHZEPRbPgwi7AGSM3-sz-dMCTRIGUqtjb9cT2VUhoPxiII4eUisq0q-e6wYu7SKV4YD3vNGxrVj3_rxXTfCxIGTPr3jYFmY1Hn4BPOSKGoEjQadA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/76474" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسعودو تو یارکشی فوتبال آخر نفر انتخاب میکردن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76473" target="_blank">📅 20:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حاجی دوران پزشکیان یادش بخیر بمولا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76472" target="_blank">📅 20:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال:
مسعود پزشکیان استعفا داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76471" target="_blank">📅 20:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">برنامه واشقانی توقیف شد
😂
😂
😂
خایمال تیر خورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76470" target="_blank">📅 20:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76469">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سی ان ان:
ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76469" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76468">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حسن و حسین امیری، دوقلوهای ۲۰ ساله، توسط دادگاه انقلاب تهران به اتهام جاسوسی برای اسرائیل به اعدام محکوم شده‌اند.
آن‌ها پس از بازرسی گوشی‌هایشان در یک ایست بازرسی دستگیر شدند و مشاهده تصاویری از ساختمان‌های آسیب‌دیده مبنای اتهام قرار گرفته است. هر دو در زندان قزلحصار کرج، به صورت جداگانه و بدون حق ملاقات با یکدیگر، نگهداری می‌شوند. نکته قابل توجه اینکه این دو برادر از کودکی در مراکز بهزیستی بزرگ شده‌اند و هیچ خانواده‌ای برای پیگیری پرونده‌شان ندارند.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76468" target="_blank">📅 19:19 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76467">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pniisiQY8BV0eLAd3MjWjVbabKzFooR5aP1iAY1Jbrl902DnVveNUPRdb951CEBOrmmAeWyV-7TTxIScE0C4ciF1mxI-YQmX8AhxHVIALQFsImjioHDjVLjALQbCJaZWNQBLBfYTqHUep6RIba3Yhr6MqSK2-Wktu3-6uwbuqNx4d0PwoUrnXzLGPU7flYdnA345owo5wtmakG_yRqag5MxRJhag2e_JHzt2cwhlSgoCUpFPq_SRuw9EIXkdZajt6YIe0krSqGHH4SG0ZOQLdcqP1hT_qkJS8PLRvNOJj5PBsODKEimg6ugLB5fY1oMpnX575DTCJPpnMahSEO7lpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوآ لیپا و کالوم ترنر ازدواج کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76467" target="_blank">📅 19:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76466">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76466" target="_blank">📅 18:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76465">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فایل صوتی وسط بازی عادلو رو فیلم گلدون گذاشتم خارکسه به اونم خورد و غمگین شد ویدیو
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76465" target="_blank">📅 18:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76464">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شی سی‌د شی وز پرشین استارتد
اسپیکن فارسی و کیرخر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76464" target="_blank">📅 18:34 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76463">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZG5QX1i_QwArVm_LDcYUkUegeD6fEWtZrW7tmrLvZjtYk9PjA3RwzJRYlmz07NDB8Ljs_cvdB_mmH1qY_ZEnCFSqhVC18Pydp0JQSI8zL3mbTEaK6n37KeWXL8Oe7qlbKeU4PSI0L4aOLIud_E4UzKmD522cXEsHO0IWNQnv9OLPBtxqmAl8hKxtu0fSTECGOgZ9Ey4WgIlZoSVC-crE6KkfSuGSnxxZ6lYvXd6XpeyBZewcVQpY6LmdnIoIV5-fvk6oVfG2ep-HuHMPgy69puUtZ8ghO2IZhcWu3hn0AtfhghWREKjVa2Lh1EX4b4jaduwC4445xAeBzLQKW1T-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف غلامی مادر میثاقی رو کرد تو چرخ گوشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76463" target="_blank">📅 18:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76462">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKSvV6j6-YxdTYApoujVKXWU2IQRqmvogYE5ahjcKVsY-6F7ROEIVqK78AYmfAjv_leO8AfJ2Qkc5uIfXwiFPcACtt_xLKYk0qYfdHutQZOcp4dq1TQZ6L3S9hWGGvTr3iW7ftwKn05-Cuzgcjv83ZiMENXQZeSByh4ppj2wTai29k5JTK_aYTkqfV4EWPuk_QyfQ3Bu5daewJuG-o3lv-rEtvGs48_25TirONXVYx1zqjRekrjtB9OkdjHFe8UU4qfLU_ojg6YDo2B0d9kVJBxc8ejRsd_Bdl2RmsmFoWpgoJ2yXCYM79Ns_vvtZLMFPPNKEkTPWVGp4pYGyhZYfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالق مینیون‌ها فاش کرده که همه مینیون‌های تو انیمیشن مرد هستن، چون نمیتونست تصور کنه زنا اینقد احمق و نادون باشن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76462" target="_blank">📅 18:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نیرو انتظامی تهران یه کافه ای که توش اسلیپنات پلی میکردن و پلمپ کرد و گفت: اینا شیطان پرستن.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76459" target="_blank">📅 15:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">نیوزسیتی پرو: با گذشت ده روز از خرداد، همچنان آمار رسمی تورم اردیبهشت 1405 منتشر نشده.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76458" target="_blank">📅 15:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چیه دوستان
میگم خبر مهم فکر میکنید روبیو بهم پیام داده از پلن های ترامپ گفته؟</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76457" target="_blank">📅 15:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تلخون از لیبل سابقش جدا شده‌.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76456" target="_blank">📅 15:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبر مهم رسید دستم</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76455" target="_blank">📅 15:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">امین منیجر یه دوتام به پوری بزن بلکه سفید شه برا چهارنفر
@FunHipHop
|  Mmd</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76454" target="_blank">📅 14:43 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پیام های شما در چند دقیقه گذشته:
فرید جان سلام من بندرعباسم اینجا صدای انفجار میاد
درود فرید جان ما قشمیم اینجا چند بار صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76453" target="_blank">📅 14:25 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3mEcFq9eQ7YLrRyOv2owu9dbGPIgjXOvvnjZUA8Yo_lwy-8Mltds5XoWhjUlviauC9lo-1gN4ABeHgfGxUn5PDnogURy64rMTkZtgZnYcswzT8dZTgWbDkJrKd0OPCCzj_mq51V2LarXcBRYFwKfYHx1dOITylT_bH9WuEhkNKx4trZg7px90AdFqFZbhZcp35Uun-Ysr9t_hNbaMUjTDG4ZYhTJnXOQd_Sf52_j951FwCbzVkQpHWmEyJuWettoiffkfvfynuCV_tscle7Uc6Soaklbzdg35_eldRQLrbKZqeb337k4cT28HQvGZ4moeTA4Xk4r_bsUROQ_sSBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحث کالچره پسر
عکس خمینی میفته رو ماه
عکس اینا میفته رو گوشت
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76452" target="_blank">📅 14:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آقای باهنر یجای ثابت وایسید از رو موتور پیاده شید صداتون نمیاد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76451" target="_blank">📅 14:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الان رسایی دوربین رو تنظیم کرده رو صورتش فقط عمامه گذاشته
نه لباس تنشه نه شلوار
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76450" target="_blank">📅 14:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امروز مجلس مجازی بود  @funhiphop | reza</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76448" target="_blank">📅 13:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">امروز مجلس مجازی بود
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76447" target="_blank">📅 13:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزارت قطع ارتباطات دست به ماشه هست
ترامپ بگوزه نت رو باز قطع میکنن
کار مهمی دارید انجام بدید این روزا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76446" target="_blank">📅 13:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یکم دیگه اعلام نهایی توافق و مذاکره طول بکشه از لبنان فقط اسم "سیب لبنانی" تو میوه فروشی های ایران باقی میمونه.
اسرائیل امروز لبنانو شخم زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76445" target="_blank">📅 12:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مردی براي همسرش پیام داد   عزيزم تو چه كرده اي پيش خدا اينقدر عزيزي كه همسری همچون من بتو داده زن جواب داد نه نماز خواندم و نه روزه گرفتم و خدا از من انتقام گرفت:))
😂
😂
😂
😂
😂
😅
@FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76444" target="_blank">📅 12:26 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
