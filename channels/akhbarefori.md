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
<img src="https://cdn4.telesco.pe/file/gfPRKWKhdEZ941-4Bot_YxMc9Ieum1kY164wcePbBaAyfrHStdqGS1rFIZRNP2mnxt7evizAG3OB0V8U8T3bwl4nKWjN_TQrS1DNAKu09R9Ny1EupijNpi4lKRY_qq55dAlhVgwP10FWyF74HxPXsoiX3sKG0qII9R_ZekNZQ6d4taoMhdh79zHFCiItVCHTMiiQ5_WTcjPRSmZFDowWYmgod1pj-VH8SrAZTkI6kTbvDrO27LT0iRQevySYZ3YalZKSiSHiVzuRd61cgAcMsODlGY0v_bMPiCIPonbtVCOI9wmJVyGeQJssGJIh2xcwheerXJlBo3_8XWOwMjxdRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.19M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 20:20:35</div>
<hr>

<div class="tg-post" id="msg-689591">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37590aebde.mp4?token=XbByW60VZMqMIkDxtEFHuaEYgNw8LfM_rwBbyU0hzpDqIrSJz1jVd8cIVsfjIHORI3mxPF493a1MAZLWtqYIjplXrbY892F0M_CfHZ5Rqf4WvciUzNofv3r_HhnUdTwUfpsBezeH7JC7Y058PPzBhOaWEBrC_EUSjPYj5u_LwDstKrWS2B-nFopT7NUgDAmvT7KLzuaM56YNKURkSDooApG2cPO7OQfXEhmyRY6v1IN7b8LB0fq41XZk3GTTAhs87LoY3DsrZdwatZpkDIQZ4v6e8kp8lVr6qwsT1FxYFpkh1Y1MNQqUmFu797pqcOPBlRkcOvlJ0hOyTs1kLJjZmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37590aebde.mp4?token=XbByW60VZMqMIkDxtEFHuaEYgNw8LfM_rwBbyU0hzpDqIrSJz1jVd8cIVsfjIHORI3mxPF493a1MAZLWtqYIjplXrbY892F0M_CfHZ5Rqf4WvciUzNofv3r_HhnUdTwUfpsBezeH7JC7Y058PPzBhOaWEBrC_EUSjPYj5u_LwDstKrWS2B-nFopT7NUgDAmvT7KLzuaM56YNKURkSDooApG2cPO7OQfXEhmyRY6v1IN7b8LB0fq41XZk3GTTAhs87LoY3DsrZdwatZpkDIQZ4v6e8kp8lVr6qwsT1FxYFpkh1Y1MNQqUmFu797pqcOPBlRkcOvlJ0hOyTs1kLJjZmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این ترفند حافظه گوشیتو پاکسازی کن #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/689591" target="_blank">📅 20:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689590">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d317143b9c.mp4?token=PQeFuoH4UMnJ25MswCVil3EfUTPWHpHcHxceP-cKBYUlim41FHRRPAuzJVh31VjVf8am-sUlydKVcFgY5hzLHdF2M1Qb0DmMth8m2NKU8gzZcJgUY8SNBXP8FEQhJ7vTFRGlCG6m8AyTmDjB6OJbEbVhdsbo9Ityee6U7dc_e2iST5OImetEAFctHPxoBl9hIpwZQVgbz9vuFYNysarvCUuiOtxdPZ10fwEpFtpawgjkEdVgapnUJnfPKYxEFV1mqR6JMhnmZDQzeHlmfkYwYKIC9iCx4sqNDif9TJtLhOLZ_itN-StlgjsKtqGwqOCiFSTg60hXm_cGMSxeGwQdGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d317143b9c.mp4?token=PQeFuoH4UMnJ25MswCVil3EfUTPWHpHcHxceP-cKBYUlim41FHRRPAuzJVh31VjVf8am-sUlydKVcFgY5hzLHdF2M1Qb0DmMth8m2NKU8gzZcJgUY8SNBXP8FEQhJ7vTFRGlCG6m8AyTmDjB6OJbEbVhdsbo9Ityee6U7dc_e2iST5OImetEAFctHPxoBl9hIpwZQVgbz9vuFYNysarvCUuiOtxdPZ10fwEpFtpawgjkEdVgapnUJnfPKYxEFV1mqR6JMhnmZDQzeHlmfkYwYKIC9iCx4sqNDif9TJtLhOLZ_itN-StlgjsKtqGwqOCiFSTg60hXm_cGMSxeGwQdGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش باران تابستانه در مکه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/689590" target="_blank">📅 20:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689589">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf565981.mp4?token=LN5yP_XQAy0nXOh0DeAvNajTofCO400gs2ly-pJL7j4c571-qQF60-7BsPlJbaexi9t6jnd54FK1HmgkHuaHfklvMeMSimLeWesLb7i8EPLS98YCkWZ8HdYvhijZ1SDPK3IKaQIbHSkzkgk2fuvFimTX19zBG_ejELO3idk6k8qrGQ_-8wd65kSOJH__PtEP_CN8fJ-5idDyq9LTFqtW6oA007L8AzAwLUAGty7lpOJT7y92VCHZTvbGMDxOCIQ46GsPubmzMKs4yd7CDfY0skPfl4ko4AWM_1B28CyUjRIPFEUOxzrF4TAhX1EwEAgFs74X9xUH_snYxZnxK6RMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf565981.mp4?token=LN5yP_XQAy0nXOh0DeAvNajTofCO400gs2ly-pJL7j4c571-qQF60-7BsPlJbaexi9t6jnd54FK1HmgkHuaHfklvMeMSimLeWesLb7i8EPLS98YCkWZ8HdYvhijZ1SDPK3IKaQIbHSkzkgk2fuvFimTX19zBG_ejELO3idk6k8qrGQ_-8wd65kSOJH__PtEP_CN8fJ-5idDyq9LTFqtW6oA007L8AzAwLUAGty7lpOJT7y92VCHZTvbGMDxOCIQ46GsPubmzMKs4yd7CDfY0skPfl4ko4AWM_1B28CyUjRIPFEUOxzrF4TAhX1EwEAgFs74X9xUH_snYxZnxK6RMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کاغذ از دست پزشکیان می‌افته؛ خم میشه که برداره؛ حالا هندی‌ها پخش کردن که پزشکیان پای راهب رو می‌خواست ببوسه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/689589" target="_blank">📅 20:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689588">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtjyK48yUbWfN6cPchFSd2x_HBOJD_At9d0wH-803ICWhrVY4dLhSwLAKeRCJWxonUO4-kUy9gv7dq5MZBzyPvblVyY51DlZ-8_OGkfv7pBBw2isgG96E-afmS_4MKQnla88ohaNmSZX7KR6fJuZAtSkp-Ys9gKePU6MMUTY52BP2MXth_7leWkCTmiMnT-hUhNlXNO4_uqFasOtuA-_44UgbqAXW9gAy6sZ1M0iXx6KaCB02lAO2uaLldZSqGa9lR_45ryBsuVkrqBFf-Nlkh0hSGLB09FfXlUMJ4resYOwfM-AIaLCnPi6EPNbNbzWX0AOvNX_kgQUtHN4T93UkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز ثبت‌نام دوره‌های آموزشی «جان‌فدا» از ۲۴ شهریور
🔹
علاقه‌مندان برای حضور در دوره‌های آموزش نظامی و امدادی و سازماندهی در گردان‌های مردمی می‌توانند از سه‌شنبه ۲۴ شهریور ثبت‌نام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/689588" target="_blank">📅 20:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689587">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UllXj5ibUuq0XEiDWAd1vQdzr_4W_6Thftg3Hr27wYnJ79YclesKvOtBq_ivJkelUyrWl9LHUhOEC9wOur_cHGQ7lsStB7bxf8l5IuxIvBaxMLFE8Nm-XyljuHnxcyhHqKx9rRCUbkCoShsb0vsPhg4WKUM-XdzG8Rz0FxcgXk1gqUMsYuqID7LNBXQgcgBQbauM_RtQEy2c3Fy5VilHjPQ-q1hyJW6134C6Prbl5aphBZvcueS-TCt5LysHxIjYXs3n_owZnjqq5tQfS2KyZI53lknoLvuajXrOFzk9va62Uv1l0NxRlbUrp4ImA0ls6uD_5YQJzq5dh9ed8IXiQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف لاشه نهنگ غول‌پیکر در ساحل چارک
کارشناس حفاظت محیط زیست هرمزگان‌:
🔹
به نظر می‌رسد این آبزی از گونه در معرض خطر «براید» باشد و بررسی دقیق علت مرگ منوط به جزر کامل دریاست.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/689587" target="_blank">📅 20:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689586">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4uWrnUELHfkK_GUk1B1BgRr9bw9cHVbvKG2BIUgVOLwgr2Uh0G-scHwDhRd2tOpWFvqjEsnZaGWXD_dst9xcWB1kE3WN1zWeiPP0oamaaZvo6i3YQijdUCKGr2GpnXmXYl0OL48kI9_SfEpsjiXyNqL1EQjDYtVSjEEOLq87uwFsfvPWWU-IFjFCptr7ecAGukKrx_HtO4334EvZ1PFNS4FpxNGDYj1IX4-MMa2QLjXMHegyA9QO4COWqWhOAECTaD7Bq3DD3Zf8kKcGHmkhFBXL3JPdOh2S_tm6Mmsxs2hS7BKdNukUcoMvxm8B1wqOQ4wStcYtygSArNplwjVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال سیاسی آمریکایی: جایگزین کردن ترامپ با جی‌دی ونس مثل اینه که شلوارت رو کثیف کنی و پیرهنت رو عوض کنی
🔹
برخی از تحلیلگران معتقدند که معاون اول ترامپ قرار است برای انتخابات آینده ریاست جمهوری آمریکا بعنوان جانشین ترامپ و نماینده حزب جمهوری‌خواه در این انتخابات نامزد شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/689586" target="_blank">📅 19:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689585">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
آژانس بین‌المللی انرژی: عرضه نفت جهان در سال جاری روزانه ۵.۷ میلیون بشکه کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/689585" target="_blank">📅 19:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689584">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X73KLPoQ1rIL_R9WcJAXns22p58dWjjUQ0HczNn9iI6gwEHqTEUpv7a5Cy4XTFwcD8Isk41vnNkpS0OdTk7JJ8f1z4X8hhP4MyF4wjBORi3Gs-SlsEKOxzG6dGGim5md1kC6vPFdfU5dmF2YKgyCoO5EcKCna0c2zyBgMUya0bVi5qj-FBUAsobtT3DCfJSTQhMBYW-EpMgzudW-QSnuwxDFcsvEuFNvQs-C92P6eSZVLsOeot6OWhoVzcbXLVo4LQsfuniiFBfG3eUpYT3eP7WrOT_LVAj6T-qsmpMGmnGM-T-zwe0BsuCmEWh_NXpGwDOw37SupeqCD2ZXjQYYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر سرد
🔹
امسال بوی ماه مهر، در هیاهوی گرانی و افزایش هزینه‌های مدرسه و سردرگمی والدین گم شده است. گرانی بیش از اندازه لوازم‌التحریر و وسایل ضروری، هزینه‌های تحصیل را افزایش داده و از سوی دیگر، تردید درباره حضوری یا مجازی بودن مدارس، برنامه‌ریزی خانواده‌ها را دشوارتر کرده است. والدین نمی‌دانند برای آغاز سال تحصیلی باید خود را برای هزینه‌های رفت‌وآمد، لباس فرم و لوازم مدرسه آماده کنند یا تجهیزات و اینترنت آموزش مجازی را فراهم کنند. مهر امسال، بیش از همیشه، رنگ نگرانی و سردرگمی دارد.
🔹
هشتصدوپنجاه‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/689584" target="_blank">📅 19:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689582">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkwIM8Tfl-nUD6R_0pDLDfSy9trUDiepsQdoSbrb6sOxx-WHQhsaYk3tL2FpcRK0PruaPUVays6AqQ217ipRnARbPOjBV-oA9FAuN5lFipofvNglP7XAPTkThsNy-GFH058GHeIM5TaIIZsgcR1HMqCJY1nty2ByRLsWwJ_fJVYNKp9e5DDiQHBaPCGFxoay32ar5Ynq9sLxQZbrQtJpFIbGK7dntytIuOFQCHJ3p3x-_525JTOfCuCFoysMb8sXp-WogsZFVLMuo0OpqmpvqiZeCw9ImOWVrUZXvOSPDKUcAPaMUfEoW-d7kHwJU-tU2T2hR8K5OpfXqp3TQtPTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484c04bfd4.mp4?token=RyYajic86_l4X6ncC0l1hhPPdsHA9CuGQBliCGQlN6taCWuQTU_Qr6gzu-0kaV19Q9bSTzreOXvkJkOQ-LxvtsrlhjaMQOb9maE1SR5C71zmH00k57I9jIbErGpyu5mG88V7Fq133udb1z-RxUgXUnr3ryc9i2NLQSanBeyBBrD7KNWCjCDKyPth-Ez8XnMgJFccsTerS0gtXdeyL_jITnYPvK5r24mEokawNrpfx5EKK8vIA2DXLJAPb48X6hNzXriyy-UgkCXbrYrqZzgid_4yRFgr-ybgkYQrCQBmubSsZwb9YUnYMyMEbSA6fgI3xAxVtMK2ko8g6eSR6bge2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484c04bfd4.mp4?token=RyYajic86_l4X6ncC0l1hhPPdsHA9CuGQBliCGQlN6taCWuQTU_Qr6gzu-0kaV19Q9bSTzreOXvkJkOQ-LxvtsrlhjaMQOb9maE1SR5C71zmH00k57I9jIbErGpyu5mG88V7Fq133udb1z-RxUgXUnr3ryc9i2NLQSanBeyBBrD7KNWCjCDKyPth-Ez8XnMgJFccsTerS0gtXdeyL_jITnYPvK5r24mEokawNrpfx5EKK8vIA2DXLJAPb48X6hNzXriyy-UgkCXbrYrqZzgid_4yRFgr-ybgkYQrCQBmubSsZwb9YUnYMyMEbSA6fgI3xAxVtMK2ko8g6eSR6bge2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنچه باید بدانید؛ Dive‑LD؛ زیردریایی هوشمند و بدون‌سرنشین آمریکا
🔹
زهپاد، Dive‑LD یک وسیله زیرسطحی خودکار بزرگ یا Large-Displacement AUV است که ابتدا توسط شرکت Dive Technologies ساخته شد و پس از خرید این شرکت، توسعه آن در مجموعه Anduril Industries ادامه…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/689582" target="_blank">📅 19:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689581">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOt_EN0J6Gjs81CujBlmNNT2wCgzgXtsRVs1xxVV7OGas2nBb7ENhIV9fVDZ27A71VX9u4-uKl4AYTXsSR0Z4K-di5fS4kRMaTnQR5-s3U6oxzY9nHvcLDC90G0reCBGcOWHfGVtWtKCj0lYuiiMXxq3p3hTdVMyTBKBl3uKtIehP9pKCoqsJp3xVHJfpEy8lMJEPDTa0XxKhSvhK-m1bql8jXgmN3YOQc6LOIepdjyJ_UZT73vjyE9kQIm4nEozc-W1H2gy0vCZMBTdic54BIlSXtZas-u6aXjgJFZ1jbmHbdoxWBgC-z9X059RHmfKQW-FIEgYaHJbF6am8ugvPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای تشخیص روغن هیدرولیک سالم
🔹
تغییر رنگ روغن فرمان هیدرولیک، ساده‌ترین راه برای تشخیص مشکلات داخلی و فرسودگی قطعات است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/689581" target="_blank">📅 19:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHvQwxBUa-Z1cMSL5muNoFi_EcOl7BgHXPCs_EaCnhsbMo21nHI7NuGMP3ll-ginVM1m6lPplHviLAC-mGpBGYuubVsxGt_-oCXSGWbqobH9FENCXMRPkazxI36UqyuTT-WWSBb0o25qtRLl5RZUy9wIZCxZM1GjrNjkpoq15Dvldmil-WrjWJ4X-IAJqPwmaJQ9cBVWwhwLxjCx16ZaVgxiI9P6DCvnYtj-Je0bbP7n5lVQt9W_k2_4CN4lo4-p9wZWDSnAisLRSKh31jxqtkg8k2wRtHH8Voy_rVNYFnkINQzUymTzFF1wwU04oKtRl-9-Pat7Hn29kbM6OqHwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق تازه در بازار طلای آنلاین ایران/ آغاز همکاری یک پلتفرم با بانک کارآفرین
🔹
همواره یکی از دغدغه ها در حوزه طلای آنلاین، انتخاب یک پلتفرم امن و دارای مجوز است. حالا بزرگ‌ترین دغدغه کاربران اما به نظر می رسد با ورود بانک کارآفرین حل شده و نظام بانکداری به این موضوع ورود کرده است. بانک کارافرین به تازگی همکاری خود را با پلتفرم وال‌گلد آغاز کرده و طرحی جالب شروع شده است.
🔹
در این طرح، تا ۳۰۰ میلیون تومان وام با پشتوانه طلا ارائه می‌شود و متقاضیان برای دریافت آن نیازی به ضامن، چک یا امتیازگیری ندارند.
برای مشاهده شرایط وام اینجا کلیک کن
برای مشاهده شرایط وام اینجا کلیک کن</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/689579" target="_blank">📅 19:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نیم‌رخ؛ چهره‌ای که هنوز کامل دیده نشده است
نگاهی به دو قسمت نخست سریالی که تعلیق را جدی گرفته است
برای قضاوت درباره یک سریال معمایی، دو قسمت زمان زیادی نیست؛ به‌خصوص وقتی روایت بر پنهان‌کردن اطلاعات و به تعویق انداختن پاسخ‌ها بنا شده باشد. بااین‌حال، دو قسمت نخست «نیم‌رخ» به اندازه‌ای هست که بتوان درباره شروع آن حرف زد؛ شروعی که نشان می‌دهد سازندگان می‌دانند چگونه کنجکاوی مخاطب را حفظ کنند.
«نیم‌رخ» اطلاعات را یک‌جا در اختیار تماشاگر نمی‌گذارد. بخشی از روابط و موقعیت‌ها همچنان مبهم است و انگیزه شخصیت‌ها به‌روشنی مشخص نیست. این ندانستن، در یک روایت معمایی می‌تواند مهم‌ترین ابزار داستان باشد؛ به شرط آنکه پاسخ‌های آینده به اندازه پرسش‌های ایجادشده قانع‌کننده باشند.
یکی از نقاط قوت سریال، پایان‌بندی قسمت‌هاست. هر قسمت در نقطه‌ای تمام می‌شود که موقعیت را معلق نگه می‌دارد و پرسشی تازه برای ادامه باقی می‌گذارد. «نیم‌رخ» به‌خوبی می‌داند تعلیق الزاماً به معنای پیچیده‌کردن قصه نیست؛ گاهی کافی است اطلاعات درست، کمی دیرتر به مخاطب داده شود. همین فاصله میان دانسته‌های تماشاگر و واقعیت داستان، موتور کنجکاوی را فعال نگه می‌دارد.
انتخاب بازیگران نیز قابل توجه است. حضور چهره‌های شناخته‌شده در کنار بازیگران کم‌دیده‌تر و تازه‌تر، پیش‌بینی رفتار شخصیت‌ها را دشوارتر کرده و به برخی نقش‌ها اجازه داده مستقل از تصویر قبلی بازیگر دیده شوند. بااین‌حال، بازی افشین سنگ‌چاپ در بعضی لحظات بیش از اندازه بیرونی و گل‌درشت به نظر می‌رسد؛ درحالی‌که فضای مبهم سریال به ظرافت و کنترل بیشتری نیاز دارد. واکنش والدین دختر در قسمت نخست نیز گاهی نمایشی به نظر می‌رسد و استفاده بیشتر از سکوت و مکث می‌توانست تأثیر عاطفی صحنه را افزایش دهد.
ادامه در سایت
https://www.khabarfoori.com/fa/tiny/news-3244760
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/689578" target="_blank">📅 19:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
منابع نظامی یمن: ادعاهای مطرح‌شده از سوی رسانه‌های سعودی درباره اصابت موشک‌های شلیک‌شده از یمن به یک مسجد در عربستان کذب و آن «اتهامی عاری از صحت» است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/689577" target="_blank">📅 19:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689576">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجار از تأسیسات عربستان سعودی در شهرهای خمیس مشیط و ابها خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/689576" target="_blank">📅 18:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689575">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baaffe8cfb.mp4?token=HqgC6ZR8fm9HTQXf2UPMwcd0kyzYm3Vtm_30-eV576zAVaov80g94Zm0CrIxwLTmaQoCcn1NJjldXD1a_XiqJ-pK2Mbfh0nN9XXflE6a5PTkSs6vS4wQJB1uRVqF3xBUGwdUcL-xXA9HtM1yabBlMslp9gGM8_z9ixBnvKyAy_MPV6rdWwNuRV5pUQfVjuS9-XQp9fmsG8BsEw3C4eUo2ImGTbYr1BvFB3Gl22sgrI38zQHp2bNPF_P_8TWfwgnODY58BRHqOjN7_mEKUtN1kA-X0K7Ci4zDaGPlNZVU2NzKvB7x0n1OQLSutt06od_moow-M75M9YZ13iuSdnQ1eUPTThiF6eYC-YpMhbHGd_4qmd1uXMQBF9w3pX1qGKu1xvMZDSFGu3_m-wenQ-mS1NuOQ9-7a5oN2YLqR4Plkz_nQ-mmv1dx0EZsXZggDqiZm00n50KsnQtvG9hrEv7hzU7N6TRTRTSycs0VYA8_5L45kf_d6oSVX5q7DJMVv40VVw9OdymII7xhqaB-2J1ARo8sIN9O0zecQ4TX0OKzxxDqbWhLBpgskks_iZX8mnG2abFrHXInrEgc4xJ3y5b0f--YTaI9a4-RIVKrF3ayL-fy3DMH-iSpPcsqdCpSA0_GSmqFyvRk20h8vmunNroMUrFWL3phb39_trPYiRL8Ows" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baaffe8cfb.mp4?token=HqgC6ZR8fm9HTQXf2UPMwcd0kyzYm3Vtm_30-eV576zAVaov80g94Zm0CrIxwLTmaQoCcn1NJjldXD1a_XiqJ-pK2Mbfh0nN9XXflE6a5PTkSs6vS4wQJB1uRVqF3xBUGwdUcL-xXA9HtM1yabBlMslp9gGM8_z9ixBnvKyAy_MPV6rdWwNuRV5pUQfVjuS9-XQp9fmsG8BsEw3C4eUo2ImGTbYr1BvFB3Gl22sgrI38zQHp2bNPF_P_8TWfwgnODY58BRHqOjN7_mEKUtN1kA-X0K7Ci4zDaGPlNZVU2NzKvB7x0n1OQLSutt06od_moow-M75M9YZ13iuSdnQ1eUPTThiF6eYC-YpMhbHGd_4qmd1uXMQBF9w3pX1qGKu1xvMZDSFGu3_m-wenQ-mS1NuOQ9-7a5oN2YLqR4Plkz_nQ-mmv1dx0EZsXZggDqiZm00n50KsnQtvG9hrEv7hzU7N6TRTRTSycs0VYA8_5L45kf_d6oSVX5q7DJMVv40VVw9OdymII7xhqaB-2J1ARo8sIN9O0zecQ4TX0OKzxxDqbWhLBpgskks_iZX8mnG2abFrHXInrEgc4xJ3y5b0f--YTaI9a4-RIVKrF3ayL-fy3DMH-iSpPcsqdCpSA0_GSmqFyvRk20h8vmunNroMUrFWL3phb39_trPYiRL8Ows" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هوش مصنوعی رایگان، تله وابستگی و سرقت نامرئی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/689575" target="_blank">📅 18:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689574">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پتروشیمی امیرکبیر از محدودیت‌های تولید عبور کرد
🔹
مدیرعامل پتروشیمی امیرکبیر از بهبود شاخص‌های تولید، فروش و مالی شرکت پس از عبور از محدودیت‌های ماه‌های ابتدایی سال ۱۴۰۵ خبر داد و گفت: روند فعالیت‌های تولیدی و تجاری شرکت در ماه‌های اخیر در مسیر بهبود قرار گرفته است.
🔹
حسام خوشبین‌فر با اشاره به توقف ناشی از حمله هوایی دشمن آمریکایی ـ صهیونی و محدودیت تأمین برخی سرویس‌های جانبی و برق در ماه‌های ابتدایی سال اظهار کرد: با کاهش آثار شرایط جنگی و بازگشت ثبات نسبی، تلاش کارکنان برای حفظ و ارتقای ظرفیت عملیاتی ادامه یافته است. بر اساس گزارش منتشر شده در سامانه جامع ناشران (کدال)، تولید شرکت در مردادماه به ۲۹ هزار و ۸۸۰ تن و مجموع تولید پنج‌ماهه به ۱۱۳ هزار و ۷۴۹ تن رسید؛ همچنین فروش مردادماه ۲۵ هزار و ۱۷۸ تن و مجموع فروش پنج‌ماهه ۱۰۷ هزار و ۷۶۳ تن ثبت شد.
🔹
عضو هیئت‌مدیره شرکت پتروشیمی امیرکبیر ارزش فروش مردادماه را ۳۷ هزار و ۷۸ میلیارد و ۱۵۰ میلیون ریال و مجموع فروش پنج‌ماهه را ۱۵۱ هزار و ۳۳۹ میلیارد و ۹۷۹ میلیون ریال اعلام کرد و افزود: در این دوره، فروش داخلی پلی‌اتیلن سنگین با رشد ۵۰ درصدی و پلی‌اتیلن سبک با رشد ۱۰۰ درصدی نسبت به مدت مشابه سال گذشته، به بالاترین مبالغ فروش ثبت‌شده رسید. خوشبین‌فر تأکید کرد استمرار این روند به ثبات شرایط عملیاتی، تأمین پایدار خوراک، سرویس‌های جانبی و برق و تمرکز بر بهره‌وری و رفع محدودیت‌های تولید وابسته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/689574" target="_blank">📅 18:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
نماینده ولی فقیه در کهگیلویه و بویراحمد: افرادی که در مراسم تشییع رهبری در مشهد حضور داشتند، شاهد حضور رهبر انقلاب بودند
حسینی:
🔹
ایشان در صحت و سلامت کامل هستند و روزانه بیش از ۱۰ ساعت فعالیت مستمر دارند./ همشهری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/689572" target="_blank">📅 18:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اداره امر به معروف و نهی از منکر طالبان، ۸۳۲ ساز و ابزار پخش موسیقی را جمع‌آوری کرده و آتش زد/ طبق اعلام این اداره نواختن و پخش موسیقی در افغانستان ممنوع است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/689571" target="_blank">📅 18:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689563">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsKHGH-oYj1zdfBG4dp1ys3tNMPjTtjDKvN1rjLjA9FHCj0TCaB9R6d__oAqeTvCEHxO50WrpIzna7MLrextdgL49BlkpoDMFMWu9txM0WahU6IV0MYs7PZ3cmDPxCFEdboAV-A1w16nyQhsIm8KP_cQWQj-LO3VDekS991_RkzEPZNHduhbhfjd3NG4fkQjCCwQrx9OzDPpiOGb1ii31xteiwaYKdB_-UND7smEXI3C24Nrv4MZt9hIeq1FcBK09Z9FskXsNdhq5sOGIWYIylXnjjdDckF62Xs5EZJdLG5eHnY3HBr7ALFug5yPrfm1atbmtJSnYzbEhocDbs4S3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhamKAC23ok6cbZ7vMBmGsiebhL-xSojyJ-LX-_U0U1MLPoAYg4qCOdEJyYs4_Pa3DTmiJMyfSoQcylkbqqfcPvGmanvbE4rSCnnZjmNbsnwjCgSFapYFpAbOoALifi7IAVvcH1P8ExbmwLg9XuzpeWcFbpGHmR3ImTq19NrYOMXk5jdbw6HyYGWTGDbQu1hHg6GpTZyJqWQogBgHkX4gZprxkI321NA7tYoEUwJrEHmjLsk6jcUdutH3M9OHqf1YYeXo3c4izNs_gEfqoKyEcsILzZaxk1NXoeq_ngJqQKjMin0F4o8rRCDBGBFKlGafOY1Un__EuONRm_ykGsV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HTe6KFMAVk_oHiSrel3e48kJ8RgSzDeLFkIUp1JmjUPxZo9sHLvntvEvSPsuhOMUlsh-jaGCwYJr6r_yE_gjVo_c9KoKDZCKoC3UVdAgWvqlL96J1uDdefJ-fNZE9tE_IDcVIYWIctTX9bkIPsznaYd-0JRdrWOpCZRc5xBSSlsUukdJ-w82DTTbQYfCd5EYpK14fK4mH39W10tP91lhGMYADFqolHyDWhT98MiAsCjObMvWo2OPFweVfKK_4yyzwqZxtyED7TOC5f8aLyL7r7kqDvhjVlm2xuDEuDWJ8At5V2-e0rvJrf8RXywwDHOkcgiuHse2BjniRp1YymKfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEQ2ZeuI9pXvzpwgEfAdKRmRq87GybUicM1IXhZUBvUcyb2zsmjXIo_B7yKDLcgOHY0RH6Wa1QYNGPNh1I45zZ-0-G0BHFw6EhSHZQMTqOfiOAr9Va7TM18N99MNaEGWYhT8EOfDoo673VNnlLPMCKpstXB-oXjMIV_kgnG8n5Goy292IJMnq8VT27UlGUfZa3GXxMozW5KTbYnh0Rb7YcPwZM1aZU1dDxEVYcqK26Jdb51BBHpL4T0fqQ1vzYY4OG2vXq_8r26lgNdSFlQ72DG929ugFPjnGY6i8Vp0VW_0zDgHMjAFn3SYs42Obf6RULgeXFc_RjaEkfD8OZ5Q3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rf9vz_EMm58Nshxtd11qG31S55cSuiyMeRqJdE2HnE3B4M0BM3nTPQ1UICyN1wOA5UYiCOvYu6YnLzptxNyeQpMZr-9Y_GOGP3UnBlm4Hxur3LgESYZwnvDM3n648vMtKPXscVR-jpfUGjwPxNmoLTgS3sxAeuVy5DWv3BbQPgERfuY1UOxFeLe_KN2Ea6qoTETO2nhxZji7D4Y6Yt1D9NtH2jq_jsnr1lnrfQuvphUpEJewShg-LHWo7IWphYSHTK94LKdNX2sbUg7f5iiS-f-7OEdaXsowxiGNQOr_2ffqjKjpVuWZsGL83whDXCcYClaP1SiHjhULEAZuUeJF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwIIra4mla-DwoyBGPaF5hQ4b93qKmrf3cs76-7D8BUgsLTlUqBbD6DF5GbgNGLBZUYynN7-YlGt9-6hi1EoHCKe-vNvuGLasp5LggX5FYAjlgrnUIk-INDOeuz6w2GBS9kAkCZ8q2AcAVOYHOXKzdP5HHarvQhfi0xe-h0SRt8egBi6kI4YRm4JV-ba6IbUIQGAWUgB9PM3YqO4TQARMRvJ4WC7wZaSkNynK9Ebd0_Q2A5fWtoQwha0L35zElrUr_7xcQuEWHdy-qfjq03g6X3Pfkr8vXkYDnxc9J-Yyl6ip-G2XUUOdYEYY53yHOM9qTDtdbNSuQ_2r_d40BYWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avfCj2xCBKeSYkzE-T-WlBU14LVCC4as7eFrRBLJziHytbulNauSUfn-tT84uc6IMgFCfglW5HiLI9rpWwbmtdgrfzTiHVfqusZ2uH8YBEPBmEqS5A4EpA_bhKX-e3qnzSrw7AUG2p2ZPoa7WyEWErgwccVp-A1zEXIV3psZ9aOlFrFZmZukcF74CQlN9Bo_r-CUKlpfoOeQ37ayOaB6zNYR7MRgrDp8DOvWXtxy0LS4PrvG1Sa_8Z7cc1LkJQyrgjndf9tdO44bVqIPpBQ2wrsqk6iIKJhjTALmJmrZqJqs2OdXwL9xjnABmAQlARMUS07IxsaIOhe8Alwo0hsA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJDQgehixQz2cgXFUtN3CmqUIVLaB-pz6DhpGkyeCee_txygKwrWqN6xKONSTuwUhZlZCvk0pTIGT9sn4TE6fsjMMT23DRvUbZsTkfz6nsh1O-nkN9dlwsrBux-x8g1ZWf0Kvw-K-XXX_VbNiWSPzCuqHcDPRxE_uFs_vIMzj5GetrfHPeO5IoV3twphxqJ3VOor94C950JBidzw3GLaAPZiuEatqa-MonnHot4xy5sB-mk8ogGRFQ6lf_16P8EUkOtv1wBS4Hxbs2v8bJQCcUgL1oC2zZZTRcwbD110wGo0eTJsKoqPjXF-wmc_R3jy5HkrvjfrXdNUvEHSo-Ymyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت چالش‌های روزمره بیماران برای تهیه اقلام دارویی حیاتی
🔸
در چند خط  روایت خود را همراه با نام، شهر و نام دارو برای ما ارسال کنید
👇
#درد_دارو
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/689563" target="_blank">📅 18:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689562">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e00884fc0f.mp4?token=eY_cmK9yNgepdJCO3bmjxtFzPevIYBHpMHhJG7GrZbLJoTNmelAv5OSHWrZQcZmVfbYms-1MWaznKT9YpTBLcuWUvBxilgF0xkyP5__CxEc-gGZnz-EpG6mKswdWtOsQuHQfKWzkTpO-4DQ6FEVfJzC4uunLbJ25Ic11DGuZUZIa93_fnf185N8-Z7v9iLse9LBbV7m3zi5vBSJ6Jy98uYFZo8LARSpzsg1nZRlS8vZp1SmtMQN-33wCI98yXD7bh9-wg6JuwUwOm3CvYT-l1u1hdCYkYuqKlrxv2Da8Hck_U37g3JA1btZBNy2VkUAZAdFB_FKXTtfAXPkFriivmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e00884fc0f.mp4?token=eY_cmK9yNgepdJCO3bmjxtFzPevIYBHpMHhJG7GrZbLJoTNmelAv5OSHWrZQcZmVfbYms-1MWaznKT9YpTBLcuWUvBxilgF0xkyP5__CxEc-gGZnz-EpG6mKswdWtOsQuHQfKWzkTpO-4DQ6FEVfJzC4uunLbJ25Ic11DGuZUZIa93_fnf185N8-Z7v9iLse9LBbV7m3zi5vBSJ6Jy98uYFZo8LARSpzsg1nZRlS8vZp1SmtMQN-33wCI98yXD7bh9-wg6JuwUwOm3CvYT-l1u1hdCYkYuqKlrxv2Da8Hck_U37g3JA1btZBNy2VkUAZAdFB_FKXTtfAXPkFriivmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوطی
بیسکویت باقیمانده از جنگ جهانی دوم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/689562" target="_blank">📅 18:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689561">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رئیس اتاق مشترک بازرگانی ایران و گرجستان: مرز گرجستان بسته نیست و کامیون‌های تجاری ایرانی در حال ترددند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/689561" target="_blank">📅 18:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689560">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
سخنگوی فدراسیون فوتبال:قرارداد امیر قلعه‌نویی با تیم ملی فوتبال؛ سفید امضا و بدون رقم
ارائه شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/689560" target="_blank">📅 18:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689559">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رسانه‌های غربی: ایستگاه پمپاژ نفتی عربستان به طور کامل نابود شده و بازسازی اولیه تا چند سال غیر ممکن است
🔹
خط لوله شرق به غرب هم منهدم شده و عملا بارگیری جدید در ینبع فعلا نداریم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/689559" target="_blank">📅 18:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689558">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74aa1d3fa1.mp4?token=erJtqpnU49uyXG5RhrgOJI-9NbFpVumEpvlFNzi-ZkLYdBD1-o9B2QbCLCNayD5OJ41TP8amIqwoatQwd_D1--LLsfzdKE-uXNd1af7APX4oi45qhBDdp8S-ex4rZm0SM75po5Ao7TuQezPwB_TqmqB8io_qNxizRHAB18hkmFOgKmNtQPsostDNFe2IlnLsgKQuQ8SyMJXY8zCUIUDdx8ww6rUGxDq9aMOtX1VsiFwRnn2Y3K3QWefd6jk5BtLu3oFZJIcQ-Dgu4uOCXU7Rt1fXog-3FH2DOkEeYKf002IO3IDtzBHJZTSPx3uDl4mWd2ePMqbRz5SMifzTKMVN-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74aa1d3fa1.mp4?token=erJtqpnU49uyXG5RhrgOJI-9NbFpVumEpvlFNzi-ZkLYdBD1-o9B2QbCLCNayD5OJ41TP8amIqwoatQwd_D1--LLsfzdKE-uXNd1af7APX4oi45qhBDdp8S-ex4rZm0SM75po5Ao7TuQezPwB_TqmqB8io_qNxizRHAB18hkmFOgKmNtQPsostDNFe2IlnLsgKQuQ8SyMJXY8zCUIUDdx8ww6rUGxDq9aMOtX1VsiFwRnn2Y3K3QWefd6jk5BtLu3oFZJIcQ-Dgu4uOCXU7Rt1fXog-3FH2DOkEeYKf002IO3IDtzBHJZTSPx3uDl4mWd2ePMqbRz5SMifzTKMVN-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن زنگنه، نماینده مجلس: من نماینده مجلس بی‌تعارف میگم ما رانت داریم؛ این مسائل قابل حل نیست
🔹
ما در مجلس بدلیل بده بستان با مدیران وامدار همه هستیم و به همین دلیل نمی‌توانیم نظارت کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/689558" target="_blank">📅 18:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689557">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
منبع موثق MES: مذاکرات بین گروه انصارالله و رهبران قبایل محلی در مأرب به مرحله پیشرفته‌ای رسیده است و به احتمال زیاد، این شهر هفته آینده به دست انصارالله خواهد افتاد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/689557" target="_blank">📅 18:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a96f95e59.mp4?token=v5b4-iBoOJrFnP4i5YNr3ZtUn8w_w4AUHu4IpU0RmuyfbAY_xdsea3XHPwf9qGDWDIYFpkyU7yc1LMJU-A0Ig-eycEKoa0tQLOIOUVVUeVxKhBnZLCydfkA_fnxsXwoTpMRVNBJqoDflHKWexV1ydeh5GoQ8-Gx0Ew2BXSh5j7yQ2rF8DQfXkqCwyA9xLg-yQRZOygvIqIFG5ATQGQqe11qJxKWukidWvsYhhOrKH0Kz4DaGNfn6FnhhCg1zOTYUGTCjzrAx9nwo9UJOSy2FCa-rxtFPwjveIjFagOtuChpTRC-tuI_3PPsle6R7GX9CwVF9oeBh8E5JtYcidr5MTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a96f95e59.mp4?token=v5b4-iBoOJrFnP4i5YNr3ZtUn8w_w4AUHu4IpU0RmuyfbAY_xdsea3XHPwf9qGDWDIYFpkyU7yc1LMJU-A0Ig-eycEKoa0tQLOIOUVVUeVxKhBnZLCydfkA_fnxsXwoTpMRVNBJqoDflHKWexV1ydeh5GoQ8-Gx0Ew2BXSh5j7yQ2rF8DQfXkqCwyA9xLg-yQRZOygvIqIFG5ATQGQqe11qJxKWukidWvsYhhOrKH0Kz4DaGNfn6FnhhCg1zOTYUGTCjzrAx9nwo9UJOSy2FCa-rxtFPwjveIjFagOtuChpTRC-tuI_3PPsle6R7GX9CwVF9oeBh8E5JtYcidr5MTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این اصطلاحات انگلیسی رو هیچ‌کس بهت یاد نمی‌ده #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/689555" target="_blank">📅 18:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689553">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f9400df0.mp4?token=Zs6Mf-MxS8_QNK2MCLbLz1TJFP7RcmFAHtA7xi2wUyUfprJGmxTWCtOJ_ftIerL6mE2L5CzkTvuiv6nPLRC6GsVgfYLZwtYoXdClo3psW8Hc7WVbc-p56WLcjRumzR3j_Us0yYyGacBvx63fvFCvuuUojQTB05n9jJNroWOEOhEioR1pETuInKd0svLd_j8WZn0p9LQI0wURxvXHhmkAOQpEkZ_34WBjW1TzdeJ0oCf7NH3wXGKYzU6hAlOq_0CM_YjRzjoGFqNPQ-IFsM8Bg8USu3_lYLXqyoZWe9cq7kw2ijYqtEOJBGLvLFer1CNmFbEXCR-hMkkyxHeFi5wBgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f9400df0.mp4?token=Zs6Mf-MxS8_QNK2MCLbLz1TJFP7RcmFAHtA7xi2wUyUfprJGmxTWCtOJ_ftIerL6mE2L5CzkTvuiv6nPLRC6GsVgfYLZwtYoXdClo3psW8Hc7WVbc-p56WLcjRumzR3j_Us0yYyGacBvx63fvFCvuuUojQTB05n9jJNroWOEOhEioR1pETuInKd0svLd_j8WZn0p9LQI0wURxvXHhmkAOQpEkZ_34WBjW1TzdeJ0oCf7NH3wXGKYzU6hAlOq_0CM_YjRzjoGFqNPQ-IFsM8Bg8USu3_lYLXqyoZWe9cq7kw2ijYqtEOJBGLvLFer1CNmFbEXCR-hMkkyxHeFi5wBgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ به‌دنبال فرار از فشار تنگه هرمز: افزایش قیمت گازوئیل تقصیر اوکراین است #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/689553" target="_blank">📅 18:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689552">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8K7Ixno5JYmK1SQAJ34QdTa9DdEoQ34HyvzrUCUKY89_Nv3M29d95aUbazs1BVZlaqtvtQI7APW2uxq08Wt5CmlQt-Ezpim3fey_C5xpV5LRfjenvW4plOy8YUuhJ9z60d9EPzm2zBu8O2gOJVcaAZcU3pPhufRihzSN-aiRhB3DXzt-Br7mHYUSVqGf3GfL1ByxA3dPPOdp0BGJ1MIaUglw3M9oCaqjCzBgJy7744TS6pMH2hnRMhEcas0tZOsrqhj_DsyXECbXBYvjUzlac_4JlrwgyZ5aM-5WLpkTZ69Nh-2wiJMG8xdbfdEOzUQ_nH7hC-DV5zTLmX9S68E5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هر شب، 1 میلیارد تومان جایزه نقدی!
🎉
شب‌های میلیاردی اسنوا شروع شد
🎉
—— 5 جایزه 200 میلیونی برای 5 نفر ——
با خرید از اسنوا، علاوه بر
دریافت هدیه
و
تخفیف
حین خرید، در هر یک از شب‌های جشنواره، شانس برنده شدن
۲۰۰ میلیون تومان جایزه
را خواهید داشت.
💰
⏳
فرصت خرید، فقط تا پایان شهریور
❗️
🔥
شرایط شرکت در قرعه‌کشی و جزئیات جشنواره رو همین حالا ببینید:
👇
👇
👇
https://lnk.snowa.ir/snowa-telegram</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/689552" target="_blank">📅 18:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689551">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromطلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf7d7bd89.mp4?token=hFHFgGaBpP9DM9vtB0cm1FxrO0fAoJB0HWIUwMLhJiV9LNjj0moOvXXs7tVjWURSskTVHHlcbuwXJduQEAw4b01gWvLfSf84LT1nC-IfGuzZ09RnklqSJrZPzbPMFr6mspBKrMdcMPSaHeoie2CBBHN5ySazfETD3h-TwURWFEDcX47krGH9X6DWQFs4PQUserQEkM9GYtLGPG5U4dvUSTk6Pc9rZDQsI5w4i0IfdCVzn6YStlKVGHnOh_pCq9hBgVBmyfVS3C77KRqAtk34rya7gOOsuetCEgAKMDg6j2T7V8r2IJi72AR-IeIdgqlt5o64uB6MVvtfoovsaQvXyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf7d7bd89.mp4?token=hFHFgGaBpP9DM9vtB0cm1FxrO0fAoJB0HWIUwMLhJiV9LNjj0moOvXXs7tVjWURSskTVHHlcbuwXJduQEAw4b01gWvLfSf84LT1nC-IfGuzZ09RnklqSJrZPzbPMFr6mspBKrMdcMPSaHeoie2CBBHN5ySazfETD3h-TwURWFEDcX47krGH9X6DWQFs4PQUserQEkM9GYtLGPG5U4dvUSTk6Pc9rZDQsI5w4i0IfdCVzn6YStlKVGHnOh_pCq9hBgVBmyfVS3C77KRqAtk34rya7gOOsuetCEgAKMDg6j2T7V8r2IJi72AR-IeIdgqlt5o64uB6MVvtfoovsaQvXyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر این مسیر چه خبره؟…
👀
🎡
گردونه آماده‌ست
🪙
طلاها منتظرن
🚗
و یک تویوتا کرولا هم می‌تونه سهم تو باشه!
ماموریت‌هارو انجام بده، وارد رقابت شو و گردونه رو بچرخون.
شاید مقصد این مسیر، طلایی باشه.
👇
شروع
🆔️
@taline</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/689551" target="_blank">📅 18:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689550">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای المیادین: گزارش‌های میدانی حاکی از افزایش قابل‌توجه حضور عناصر مسلح در مناطق مرزی مشترک با ایران است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/689550" target="_blank">📅 17:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689549">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfohlK_iWpKNWiH85GnYZYeV92MWDsIB_53mtV6r5snZ2CoWVrV-UcWYyznvdZt-M0AdDBoNtRLDAKds3qIJdsba2J79T3MKutB7DIXL0AvJ-CmRLOTvsA0YEvzXlLHGpF0ZSpmM_RgsatyiUbtWcvgxUZrnAFLx6SW13Xl9NcScUvmRorUMruPCTmekG_6Ft9jhbTFm6kxvjR9Y26JJsD2Ji4YhdphD5-EuK6Tl5-LzKXLO24jSwsBonbf_MA9pRyk5_9RDEpX8YBEDZl5uQyDInuPCR71_vGYFe-crqgfv-f24c5U2LzYzOX65TMZyjHfahuN0Kp9XBrosShn-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاله مرزبان جایزه بهترین بازیگر بخش «افق‌ها» جشنواره ونیز را دریافت کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/689549" target="_blank">📅 17:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689548">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1846966afa.mp4?token=jWmxJjj04zn2O7KUDL5bBdfrn40mQMjvNSIfdnsQQHGV0d4rTVR6XN3JH3TUoCYtlIqRpo_i7t5b5gWkvelDbjSjIxhYDz_lAOkNheZtiuJR5ODQdD_IYZ6whrIbUwZ2zNNkIUdn-BKAaDzMKmiaceWpHAtYN6MdWSAEGMq1U_US5zI6BEpT8zcEKhhz6AEM5I1sdytIGXxZ8KiRoElV8sKW-GLC5ZpqcCgZbDqZGrQigwBA1OoV63I4zGuXBeCqyWvuNe7thKpMHAG_XyrPgn2KrfHjX8BHQYxQa4kaF3VLHtpl6ethYfR78XqkSuOcPrslf6yM7bzK7sZBd7hrOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1846966afa.mp4?token=jWmxJjj04zn2O7KUDL5bBdfrn40mQMjvNSIfdnsQQHGV0d4rTVR6XN3JH3TUoCYtlIqRpo_i7t5b5gWkvelDbjSjIxhYDz_lAOkNheZtiuJR5ODQdD_IYZ6whrIbUwZ2zNNkIUdn-BKAaDzMKmiaceWpHAtYN6MdWSAEGMq1U_US5zI6BEpT8zcEKhhz6AEM5I1sdytIGXxZ8KiRoElV8sKW-GLC5ZpqcCgZbDqZGrQigwBA1OoV63I4zGuXBeCqyWvuNe7thKpMHAG_XyrPgn2KrfHjX8BHQYxQa4kaF3VLHtpl6ethYfR78XqkSuOcPrslf6yM7bzK7sZBd7hrOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن هاشمی: من خبر دارم مسئولین در طول دو جنگ ۱۲ روزه و ۴۰ روزه از ایستگاههای مترو به عنوان دفتر کار استفاده کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689548" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689547">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMyiy7M4VYjR9olRifVn5mrDepfc328Jhzxl6LaRzmEVgWtR6oSEgwLMSkd7bN0O36Uc63bDzUwS4RobszW_x_QWWwpNaSMX3Lo9evUzFhC2yOqDFriWRWwt_V5lSX002UZa9IBfE9bNKDSI4QVd3gRD7IKz6tkmR9g6sRkEAv5H_m_3TrSKWLP3ud8W8vrVaNx8OLbqXQ-1bT8YMyHYRrx9uoT6MtN8QxsM06hBGMtg4oJp8VjSFNKwT0QIYgwsI5SgI9bA-SP6zMG2yxpcfR0gqlUlhkbvZdEExjRf2tspMvAQFJFIRel24tRuSAsFabkXBkN3JIETNR_Li0FbfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات حمله به کشتی ایرانی در تنگه هرمز
🔹
یک کشتی کانتینربر ایرانی بامداد امروز در آب‌های قشم هدف پرتابه قرار گرفت؛ یک خدمه به شهادت رسید و ۴ نفر مجروح شدند.
🔹
۲ مجروح ایرانی و ۲ تبعه پاکستانی در بیمارستان قشم بستری هستند و حال عمومی‌شان مساعد است.  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689547" target="_blank">📅 17:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689545">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای‌ترامپ جنایتکار: ما در نهایت از جنگ با ایران خارج خواهیم شد، مگر اینکه تصمیم بگیریم بمانیم و نفت را برای خودمان نگه داریم! مثل ونزوئلا! #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/689545" target="_blank">📅 17:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689544">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a76aeee48.mp4?token=PeKjRC1CYOiCGKJwiJYBf2c_xLglipuLXPcwV33JMIHfkzbXV2guCaybobiNyy2E6XFTdk7hlwQHoygNUzJ-If32omlmegqUX_W-5iKf-3sWXP-Uqz0USvwthyh5p5jecQesWLRxOBdcroCGJyIrIBOzcDa8co7PjNNeVStoKOHYKe0Cp8djB9817Wv6t6jJaUDv2BVW6oXCsCbfp7QwRl6IzjWzsHs96rb2Am81UOSM5SpItvnDBqHvkgFUEuy8uEDWRTLS-w4xuPIjKGuFV_4uvVq4QeY2Cm1TMrkUugyd3lL8GKr--3rVlFyORxwtCNgHh-2OUGrrEhhFrXs81g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a76aeee48.mp4?token=PeKjRC1CYOiCGKJwiJYBf2c_xLglipuLXPcwV33JMIHfkzbXV2guCaybobiNyy2E6XFTdk7hlwQHoygNUzJ-If32omlmegqUX_W-5iKf-3sWXP-Uqz0USvwthyh5p5jecQesWLRxOBdcroCGJyIrIBOzcDa8co7PjNNeVStoKOHYKe0Cp8djB9817Wv6t6jJaUDv2BVW6oXCsCbfp7QwRl6IzjWzsHs96rb2Am81UOSM5SpItvnDBqHvkgFUEuy8uEDWRTLS-w4xuPIjKGuFV_4uvVq4QeY2Cm1TMrkUugyd3lL8GKr--3rVlFyORxwtCNgHh-2OUGrrEhhFrXs81g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار: نظر شما درباره دیدار کشورهای حوزه خلیج فارس با ایران چیست؟  ترامپ:
🔹
برایم اهمیتی ندارد. این به خودشان مربوط است. ما در نهایت از آنجا خارج خواهیم شد. مگر اینکه تصمیم بگیریم بمانیم و نفت را برداریم ، مثل ونزوئلا
🔹
دیروز بحرین اعلام کرده بود که…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/689544" target="_blank">📅 17:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689541">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoCOqfRGXp556WVyaxj9yobZRalzX__qGYXcW4-NAkVxljUnqzq69cSFvQ27AfPOMD-TAdA849W1d-zfu4qnjLKgMD061WSiIZmmguo_yiqQ7JeJA1uyAkBIRkYynIqGj7Bj6y_lX6cIHAve3djH6Fp7cqbkStD7BxAHVYr3dUHkGY3PGdIWmRbbu4mQQ347tuVIPoOpU6L0zDNvEwOPa4cNNzm8UqtRoRORk1qsAL-A816sbG6PBGIpEtjxd2Q4DzFD9deVrBwRZUlU5kFgWr404hdIRRd20ZBhOl3MFNrGxiAXbMZh-b8FUAjJ5Mgo1WGwNGNYAL61jgK7ZprMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4jkPdKBVwmnVsyCjYA89TVY8UsVJnbQTjTvsPZcmkZZbJPmA_7MaGVs5Xz3ERlT86rQK16i9tWNAcbq6PEHifWbUp8I5Y-8BY7dXMlKewQDOmAjKiC5igomRTNCmeh1crXLAQ7aIDhzLUzFsLTzdUE7su9XvFkbWxnzkQRx6CGp2SPIuj1c7YOmbJ0LAtSC2UniMY6trNu7iCj4SddRZ6AhZKDHWxeC64kfQUkRtT2VR_SdETvv6jixQH3PomN_JppKdnPErOiM0Ybf1kHKRj7uN5gL8WXH10JPmNDspKML44HgG6VYkTgC1BzHcsrjkd0m0UYpabpKOI4MRH-9vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: خودروهای بالای یک میلیارد تومان مشمول سهمیه نرخ یک و دو نمی‌شوند و تنها ۱۱۰ لیتر بنزین ماهانه با نرخ سوم (۱۰ هزار تومانی) در کارت هوشمند سوختشان شارژ می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/689541" target="_blank">📅 17:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689540">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ff84dc65.mp4?token=XOBiwZzMBtG8mIsNC53cM8W-RBMHbXhmLOpvWoK8rnTnYHkXBn7RqXqIzLP0XaW3C-B__ku8g7HWghcWInY1dROIhle5LI4RZ0RP_qJH1Flzg25_vRAa7-UQjCqRSE8Vx1geOQOxsaBIRvrCFx6vp7EXozzFYEJX_qTWyQaJbkxmop9qIJA1zVQpqWsgPAdTMw2_T2kUX_jp_GZLermMyd8lRfgO20ecMGJ5LiA8dqMwva8V69VTA3cDXsOCeHn0w0V7LTibUv-pwGc7HC2ubQ47ak0NKbybU7MaoGAz8J183xQkalXr1YfoTzE1dZk48bq37iVxJK5HsAU2ARvCd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ff84dc65.mp4?token=XOBiwZzMBtG8mIsNC53cM8W-RBMHbXhmLOpvWoK8rnTnYHkXBn7RqXqIzLP0XaW3C-B__ku8g7HWghcWInY1dROIhle5LI4RZ0RP_qJH1Flzg25_vRAa7-UQjCqRSE8Vx1geOQOxsaBIRvrCFx6vp7EXozzFYEJX_qTWyQaJbkxmop9qIJA1zVQpqWsgPAdTMw2_T2kUX_jp_GZLermMyd8lRfgO20ecMGJ5LiA8dqMwva8V69VTA3cDXsOCeHn0w0V7LTibUv-pwGc7HC2ubQ47ak0NKbybU7MaoGAz8J183xQkalXr1YfoTzE1dZk48bq37iVxJK5HsAU2ARvCd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار رادان: بیرانوند شامل قانون سرباز قهرمان نمی‌شود
🔹
دروازه‌بان تراکتور از اول مهر سرباز است و باید یکی از تیم‌های ملوان یا فجرسپاسی را برای بازی انتخاب کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/689540" target="_blank">📅 17:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689539">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epjIH4FnH6u7WgRAY0SXilg-U_jsPloj3G7Siejf2jcTy-xxdSn4v2Wy9x3CrYTcl_gaYczBDSl7ioTqt95KM75Gf-Lry_ke1fA-YeYlviHbLa8MVI9JKroKijgcM4LUPaXndWtzIOWg7TmzrB6qL0XAWoam4gNgZMxZH1N4EElbaHANQSGqpaxaPdGVcm9x3XHacyigkvgIK8XwYo6Lx_tCArpgiY04fQxxNXRZxKcYY4aqx27PKpUeK-FFYFxGDYt9WWR77JkRiaFiGccdzoCM26-f0XplTEbbXT7JlJuJL4tDZwJXGBUS3L1Qc5Vc3CFwtXUp8M-SAOlkESZsiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پر فروش‌ترین محصولات آرایشی در ایران
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/689539" target="_blank">📅 17:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689538">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
کرونا وارد محدوده هشدار بالا شد؛ آنفلوآنزا B غالب است
وزارت بهداشت :
🔹
میزان موارد مثبت کووید-۱۹ به ۱۱.۷ درصد رسیده و از آستانه هشدار بالا عبور کرده است. همچنین ۶۶.۶ درصد موارد آنفلوآنزا، نوع B گزارش شده و کودکان بیش از یک‌سوم موارد مثبت را تشکیل می‌دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/689538" target="_blank">📅 17:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689536">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMl_1HNmi_v8XqHD4q7Zz9ymYnou-_YiEiyzN_zTz2OvFV82LvGfNFdGHTYDgDe1X6LWHXK4muOZ1RVSRuC5lyY_yaGC_pQEo4Y24T5nA_7iWrkzAkoHVTbBzi2ttv-ISyM79DrCwy3cjS-2iqahFjCwVNJfad9mtP9dTBXEZIgNpGCrT-2YqdN_ety2wlJnUcydu-EfoujGa9XJSS684BprFaQDEEfpnMTsSepiJ1bG0WDLc-p1-DGGjs-BtZqQTCLoSW4F4BZXsBTzWfhqVcoqhCfdhw0SJ4P3yyxExax0Wzw2cTcXCcQ2qJMU_xjncd5IO8iFRbqh2ewFp8m07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
مهر تأیید اهالی بهارستان بر عملکرد بانک کشاورزی
🔹
بیش از ۱۰۰ نماینده مجلس بر نقش کلیدی بانک کشاورزی در امنیت غذایی کشور تأکید کردند
🔻
اهالی بهارستان طی یکسال گذشته با تأیید عملکرد بانک کشاورزی، تقویت این بانک را بخشی از سیاست کلان حمایت از تولید ملی و صیانت از امنیت غذایی دانستند؛ سیاستی که تحقق آن نیازمند افزایش منابع مالی، رفع موانع ساختاری و همکاری منسجم دولت، مجلس و سایر نهادهای مسئول است.
🔻
بیش از ۱۰۰ نماینده مجلس، با تأکید بر ضرورت افزایش سرمایه، تقویت منابع و رفع ناترازی بانک کشاورزی، این بانک را بازوی تخصصی تأمین مالی بخش کشاورزی، دام و طیور، صنایع غذایی و زنجیره‌های مرتبط با تولید می‌دانند.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/689536" target="_blank">📅 17:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689535">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc3b838e5b.mp4?token=mF-_q7hrgsyVopw451anKu0jxrUAgz6eyl2EHGn1_iB--Pvk46nRsuvpwrnez-wAa4LbZyOv68e2PDMfxbo9Eg2FKaypUrYDWfLX53JghlwOBV_iZVjY-coIeyzRdhYPVVVQNdnKflxthUnPML3TSGlgMsxCZ7MP0UVU8uVscj_N08UOZkV6lRXeirJrKaFyho7bxcu_hwJKm8fDSqam_bR-BktmiFFpL8eYBHdkX7BSn8mZV_WOH7BdGjytJs3pwGuE1A5IiTlqiArIZFWyVK4q7AMkLDXeavpFBMgugR6MKrJW1FGCfzZlZzx8d9s9oRk73gEwDP-4zLACRP3OQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc3b838e5b.mp4?token=mF-_q7hrgsyVopw451anKu0jxrUAgz6eyl2EHGn1_iB--Pvk46nRsuvpwrnez-wAa4LbZyOv68e2PDMfxbo9Eg2FKaypUrYDWfLX53JghlwOBV_iZVjY-coIeyzRdhYPVVVQNdnKflxthUnPML3TSGlgMsxCZ7MP0UVU8uVscj_N08UOZkV6lRXeirJrKaFyho7bxcu_hwJKm8fDSqam_bR-BktmiFFpL8eYBHdkX7BSn8mZV_WOH7BdGjytJs3pwGuE1A5IiTlqiArIZFWyVK4q7AMkLDXeavpFBMgugR6MKrJW1FGCfzZlZzx8d9s9oRk73gEwDP-4zLACRP3OQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قطار حامل مقامات اروپایی در نزدیکی مرز لهستان هدف حمله پهپادی قرار گرفت
🔹
یک قطار مسافری که مقامات بلندپایه اروپایی، از جمله بوریس جانسون، نخست وزیر پیشین انگلیس و مشاوران ارشد وی را حمل می‌کرد، در نزدیکی مرزهای لهستان مورد حمله یک پهپاد مهاجم قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/689535" target="_blank">📅 17:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689534">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1wjZHAZWU-FFQF0inQGkVbDks536OOWxV08lZa_kOExLckLnUHu9i4DH4ehfuvJeCkb_7TtCdzJ3_9qAnX-7TCUpXtUGavCBDNDTDzoHMmLl9kGbDf2vVdI_n3GISmpx3KtdoG5Rkl4NVNiCoRTZPQxmmhTYqAdO9bsRipKrkCMnHFLORgTFbTxzYlugf_0ab01HYf-bd0t76D9ZGJ8S4IhCXgJLLTapzr53NQKk91AhNXWqOkjIvPCl3_dCbUnTRQEiDx21PYk0xo4hl6ZY0yimpWR7-7IKn2ryedWRo1EQODMz3Qi4Cli9rAu_2F82lLydyB3Ksrm-t-dDgC1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شکست استراتژیک قاطع
ویل شرایور، تحلیل‌گر ژئوپلیتیک آمریکایی:
🔹
انصارالله کنترل کامل دریای سرخ و تنگه استراتژیک باب‌المندب را به دست گرفته. آن‌ها صادرات نفت عربستان از طریق خط لوله‌ای که از عرض شبه‌جزیره عبور می‌کند و به دریای سرخ می‌رسد را متوقف کرده‌اند. اکنون محور ایران و یمن عملا به دروازه‌بان/کنترل‌کننده مسیرهای استراتژیک سوئز، باب‌المندب و هرمز تبدیل شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/689534" target="_blank">📅 17:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khIY4rE8_TO1RnqCQTvw8t7M217_D0_sw5BdgoY4e6iclLjiteyovH2uVf1V0BeslI1XEILKMq3Kz08uiGEMxsZNbdW6TVPFNYhYa00Wo7e-0wA5CuUodlb6jJ1C1dt9qVrOUQMFu8gkROkb7b6oT2pEHi8CAMnhEG2412WWU6DCg_sSB5_QnBw1wryYm16UUPvn2wvEYDj4XP2zRHkCjwt5jhrTXNybnOdF-uqxwhEFLrgt3dmTQSJvk8RKHevzA_eJsxpKGPyTDec099ubfNDiNQdigcRDKcvMW7kGyAnI_ZYqBrVqZDeafakYrnqd-X4mELppeQ9OhBxl3JwB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنظیم‌گری رمزارزها تعیین تکلیف شد
🔹
مطابق مصوبه جدید شورای عالی فضای مجازی، تنظیم‌گری رمزارزها به صورت چندنهادی و با نطارت "کمیته تخصصی رمزدارایی‌ها" انجام خواهد شد.
محدود کردن خدمات کسب‌وکارها دیگر سلیقه‌ای نیست
🔹
روشن بودن اینکه چه نهادی درباره چه موضوعی اختیار تنظیم‌گری دارد، چه مرجعی اجرای این تقسیم کار را پیگیری می‌کند و محدودیت‌های عمومی بر فعالیت کسب‌وکارها با چه سازوکاری قابل اعمال است، هم برای سکوهای تبادل رمزارز و هم برای میلیون‌ها کاربر آنها اهمیت دارد.
منبع خبر:
تابناک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/689532" target="_blank">📅 17:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ: ایران می‌خواهد به هر قیمتی به توافق برسد، اما من توافقی را که بی‌نقص نباشد، امضا نخواهم کرد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/689531" target="_blank">📅 17:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
جولانی: گران شدن بنزین و اعتراضات در شهرهای سوریه بر می‌گردد به جنگ آمریکا و ایران و اوکراین که باعث گرانی سوخت در جهان شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/689530" target="_blank">📅 17:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689528">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLDCeA87xG94ZgUw8OAozgN8B830TklLbH6WzfpDwrT4A12PkWy9GEuPwDW8aTClgcfmKzYE9vL5WYfuPddxNB2BfL2-sMm2wCHWpXg9QQs4kD3cI2iUP8ZKGw3WvK7GdcsytP4ZkV3Ak0daX962pQyDNW2UVfhL2ld63VU9zTwVn0xrsXbhMn8WKs-BDRTSZII2KGEixOjwZL5b0MiHUM8DbufBQQHKF2BG-DfAS9buFsZbIYgyUpmrhJH9Vj7twb-7zz6VadmRVh2Xj8KW9qIQNQ973Wh_FbF_cZD3sqAR-cA-0N1U-vmb4iyRlGCux8khUXzRUXt_ZLaxb1_Qrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عوارض نوشیدن آب سرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/689528" target="_blank">📅 16:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
عباس باصفا: به‌زودی تاکسی‌های اینترنتی براساس پیمایش‌شان سهمیۀ بنزین می‌گیرند  مدیر سامانه هوشمند سوخت:
🔹
به زودی پروفایل سوخت ایجاد می‌شود و کارت اضطراری سوخت در کارت بانکی افراد قرار می‌گیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/689527" target="_blank">📅 16:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689525">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
دستور رئیس کل بانک مرکزی برای عزل روسای شعب متخلف بانک‌ها در نقل و انتقال پول‌های کلان
🔹
بانک مرکزی، عزم خود را برای برخورد با روسای شعب متخلف که ضوابط مبارزه با پولشویی را رعایت نکرده‌اند، جزم کرده و رئیس کل بانک مرکزی دستور داده که روسای شعب متخلف بانک‌ها که ارقام بالاتر از حد مصوب را برای خرید و فروش ارز و طلا جابجا کرده‌اند، عزل و به قوه قضائیه معرفی شوند.
🔹
خبر روز گذشته بانک مرکزی نیز حاکی از تذکر جدی همتی به مدیران عامل بانک‌ها درخصوص لزوم رعایت ضوابط در زمینه تراکنش‌های مشکوک بود.
🔹
آنچنان که رییس‌کل بانک مرکزی عنوان کرده، این بانک به صورت مستمر در حال رصد تراکنش‌های بانکی است. علاوه بر این، بانک‌ها نیز باید در سطوح مختلف به موضوع تراکنش‌های مشکوک حساسیت نشان دهند و در این خصوص، روسای شعب مهم‌ترین رکن می‌باشند که به صورت مستقیم با مشتریان در ارتباط هستند و بایستی ضوابط شناسایی مشتری و سطح تراکنش مورد انتظار آنها را به صورت دقیق بررسی کنند.
🔹
بر همین اساس، رئیس کل بانک مرکزی دستور داده رؤسای شعب متخلف بانک‌ها که بدون رعایت دستورالعمل‌های بانک مرکزی در انتقال و جابجایی پول‌های بسیار کلان و چند همتی برای خرید و فروش ارز و طلا همراهی کرده‌اند، عزل و به قوه قضاییه معرفی شوند.
🔹
مشاهده‌ها حاکی از آن است که بانک مرکزی برخورد با متخلفان این حوزه را با جدیت دنبال می‌کند و در هفته‌های اخیر، بازرسی شعب و واحد‌های بانکی به صورت حضوری نیز انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/689525" target="_blank">📅 16:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689524">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ: ایران می‌خواهد به هر قیمتی به توافق برسد، اما من توافقی را که بی‌نقص نباشد، امضا نخواهم کرد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/689524" target="_blank">📅 16:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689523">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02f41c06d.mp4?token=Ttmv5EjbZUuPdsdVsiYxKdkQSW9tjqb6vSZql7JJj7H-5m2GNGTvSrjTxJPNzH3qoIuhrntErCAsqlopoUw2VF8AHdRCpMBhtdWq6RhSec4fWs4krdm-ZMTNR6On_qgK2XjY7V4-AMQWY01Gu9-956tsfNAyEm9NxJGjOwjwwwIaoFT8Zr7fnhvt2vtkiS_ltR59VDcAHyL91t3s2g9w6gRw85MQT9ib2mcOtPJMACqHJnjXaDa540msBbVBHZ5JwD3anqUcfGljq8fwjlB7lgwonY8aT8L8lvoR08L0lcPUfw43AHLqvsW_qFB1BCwcJPQvDxM1q3EgnCz_VA4XCnOiVRnqmjV6hR1CXuWreYGno83DVGtbH-BRecrAz0eo7XhjqvJ1F_QVR2-HpYOP5VgOluyxjUMg6lMJZBPOqLYwbUULJxxRwKWYjk2MVyg2-yx2bGKgCHAv7wynsws4-l3UWEwP7pPz7uygzvVqFdbjyvC2duSyo1MI18T9n7aaIU7geI-i68iJrVnI-qtx_s3sZTsC2JDjALUEVmwb5NRf9vG0NdwlcyClS2PJ1hsM3bXUjYUAipI-qVt20gFUXmhRUPJ-HSzMAPY946ET1HBqBnk7xlaeg1yjqN8SH2ygM_1jn1LybZjbzxkxcd_96wJxy31GfzCblJzGpFF6vLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02f41c06d.mp4?token=Ttmv5EjbZUuPdsdVsiYxKdkQSW9tjqb6vSZql7JJj7H-5m2GNGTvSrjTxJPNzH3qoIuhrntErCAsqlopoUw2VF8AHdRCpMBhtdWq6RhSec4fWs4krdm-ZMTNR6On_qgK2XjY7V4-AMQWY01Gu9-956tsfNAyEm9NxJGjOwjwwwIaoFT8Zr7fnhvt2vtkiS_ltR59VDcAHyL91t3s2g9w6gRw85MQT9ib2mcOtPJMACqHJnjXaDa540msBbVBHZ5JwD3anqUcfGljq8fwjlB7lgwonY8aT8L8lvoR08L0lcPUfw43AHLqvsW_qFB1BCwcJPQvDxM1q3EgnCz_VA4XCnOiVRnqmjV6hR1CXuWreYGno83DVGtbH-BRecrAz0eo7XhjqvJ1F_QVR2-HpYOP5VgOluyxjUMg6lMJZBPOqLYwbUULJxxRwKWYjk2MVyg2-yx2bGKgCHAv7wynsws4-l3UWEwP7pPz7uygzvVqFdbjyvC2duSyo1MI18T9n7aaIU7geI-i68iJrVnI-qtx_s3sZTsC2JDjALUEVmwb5NRf9vG0NdwlcyClS2PJ1hsM3bXUjYUAipI-qVt20gFUXmhRUPJ-HSzMAPY946ET1HBqBnk7xlaeg1yjqN8SH2ygM_1jn1LybZjbzxkxcd_96wJxy31GfzCblJzGpFF6vLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار تعدادی از معتادان از کمپ ماده ۱۶ در مشهد
🔹
روز گذشته (۲۱ شهریور ۱۴۰۵) ۷۰ نفر از معتادان متجاهر یک مرکز ماده ۱۶ نگهداری این افراد، در ساعت استراحت و هواخوری، ضمن درگیر شدن با نگهبانان کمپ، فرار کرده و متواری شدند.
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/689523" target="_blank">📅 16:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689522">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e31d4e23.mp4?token=vxB_xLykUYDMKMQ-B3-DRpcqzgMarYfoC1DBHLm9a4214I4rxYxk3K899cew2JH-EVQ6e7H10Mki_NOYYt2to-C_o5qe3tYyxM_fkoP5O0ty0LnQ4Gs2SiwxIIBwqr1W0OF-A56qyNIxrw06gEP1R36jv1kV0YN4W0ISjlK7cXgliteJY2yii_nqVrhJR4h0fLLisTFVJXHtZ1l9DX0kxSAAZnlTVtjcTgCJgre9aekKwjY1rNmcbcHoTm3PPdXBHV4oO31AZzYHbtsbEf9Wi5tEXDZg97CU074qBPOOUrQOx_Jf1h-w5ge1WjoGbxWlbDg-ssm63CW902Djt66E-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e31d4e23.mp4?token=vxB_xLykUYDMKMQ-B3-DRpcqzgMarYfoC1DBHLm9a4214I4rxYxk3K899cew2JH-EVQ6e7H10Mki_NOYYt2to-C_o5qe3tYyxM_fkoP5O0ty0LnQ4Gs2SiwxIIBwqr1W0OF-A56qyNIxrw06gEP1R36jv1kV0YN4W0ISjlK7cXgliteJY2yii_nqVrhJR4h0fLLisTFVJXHtZ1l9DX0kxSAAZnlTVtjcTgCJgre9aekKwjY1rNmcbcHoTm3PPdXBHV4oO31AZzYHbtsbEf9Wi5tEXDZg97CU074qBPOOUrQOx_Jf1h-w5ge1WjoGbxWlbDg-ssm63CW902Djt66E-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ۴۵ روز اخیر، ۹ آتشفشان در نقاط مختلف جهان فوران کرده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/689522" target="_blank">📅 16:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689521">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای وزیر خارجه ترکیه: سوریه می‌تواند جایگزین مسیر تنگه هرمز شود/  سوریه می‌تواند از طریق اردن، عربستان و ترکیه، مسیر ارتباطی خلیج فارس با اروپا باشد؛ مسیری که قرار است با راه‌آهن، بزرگراه و خطوط لوله توسعه یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/689521" target="_blank">📅 16:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689520">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11ee1bed1e.mp4?token=Nq4_-FLW4N7d_Ft9Aqhk7QfN0lU5J_jH-jlb3ei_1j-GExQh4TMBk6UIsQMMMo4ViSvL0CoajjFGnHXB8zZGPbYKTNRhl2fITB1j_Ds6mk748TGnpicmDh16dOglMXDg-Q5AlZnjCs3QxAM9Wmdcfyp0Eths1JP-UsF5eqaK8NlFTEFa9EtFIdJZaymihz-nX12vDl0ov7_nFklFpx6JXlk17F1dx5yQxQEA1a8xFnqaGCpCKxYJzIukXaed1hgAV0uUkNs4dt5fVtSZRmQNtPUuHXL2leQ-k5YZCk8wZBL7QL4fDU8_L3LdqrGen9zwUu3h7BHfpYDD3NirvNJFug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11ee1bed1e.mp4?token=Nq4_-FLW4N7d_Ft9Aqhk7QfN0lU5J_jH-jlb3ei_1j-GExQh4TMBk6UIsQMMMo4ViSvL0CoajjFGnHXB8zZGPbYKTNRhl2fITB1j_Ds6mk748TGnpicmDh16dOglMXDg-Q5AlZnjCs3QxAM9Wmdcfyp0Eths1JP-UsF5eqaK8NlFTEFa9EtFIdJZaymihz-nX12vDl0ov7_nFklFpx6JXlk17F1dx5yQxQEA1a8xFnqaGCpCKxYJzIukXaed1hgAV0uUkNs4dt5fVtSZRmQNtPUuHXL2leQ-k5YZCk8wZBL7QL4fDU8_L3LdqrGen9zwUu3h7BHfpYDD3NirvNJFug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به دلیل افزایش شدید قیمت سوخت در سوریه، اعتراضات شدید به رقه و دیرالزور کشیده شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/689520" target="_blank">📅 16:24 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689519">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
گزارش اختصاصی شبکه سه و صحبت های جالب مجاهدان انصارلله یمن در تنگه باب‌المندب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/689519" target="_blank">📅 16:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689518">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
مهم‌ترین محورهای بیانیه نشست بریکس؛ از محکومیت حمله به تأسیسات هسته‌ای تا حمایت از الحاق ایران به WTO
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/689518" target="_blank">📅 16:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689517">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
مهم‌ترین محورهای بیانیه نشست بریکس؛ از محکومیت حمله به تأسیسات هسته‌ای تا حمایت از الحاق ایران به WTO
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/689517" target="_blank">📅 16:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689516">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: در دو استان کرمان و سیستان و بلوچستان خودروها علاوه بر سهمیه خود ۵۰ لیتر سهمیه بنزین ۱۰ هزار تومانی هم دارند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/689516" target="_blank">📅 16:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689515">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhaJxDnJNjf7-yAZCARlkdhInLv6gwbVYU0pwDvQJC5J90iBICy4Lje7StX2qX8bOIplC7t0knLdNDjk43WzlTE4LuvcFn7LV_lLlKfFxjLXr5_e8vb69FgwqbvyPhG8k99_KA02w2iEp7qLX5GbIeNq7sXFWGdylzOGrDTFHVi47-ltcEnMfDduED6IrqQeqWBNqqPvxgSbwod5AJkW4woaa-LMKBgwWiZjXydNLOWZXl9PTgVyxwQ9MBxLKHru3mkj6fTrpxKi-cwUR3rT3hPQlJZhbsz1Ge52v06pJdZCAXgTY-N8WDKG6ra40PidL2CHesx77WiQt7V6OI7lSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
لورا روزن: قیمت بنزین در واشنگتن ، برای دومین بار در هفته افزایش یافت
روزنامه‌نگار آمریکایی:
🔹
اکنون قیمت هر گالن ۴.۵۹ دلار است. این قیمت روز پنجشنبه ۴.۴۹ دلار و روز چهارشنبه ۴.۳۹ دلار بود !
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/689515" target="_blank">📅 16:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689514">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مدیر سامانۀ هوشمند سوخت: هر راننده فقط می‌تواند ۱۸۰ لیتر بنزین در کارت سوخت خود ذخیره کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/689514" target="_blank">📅 16:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689513">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82c725d14d.mp4?token=LE6r6iwYFvQBUajLn83HOr196B8TlnvqjpAuCLATjKzbNHsXVh_ltwD1hQh-AfKWgilbyQz0rki6BA1xOfnEYwDeUePi6mNb2bh2yftdYwDP5j5dIQMoE0CE1Wogy3YIg_mhjMSM1jeRQmg0_wvhfHZ10wVFj1xTV2vivJf6SY_B7MSG1v5cwTZXJnCv_miD5hWj8oiYbL4tS1yVpS3-VwmKnYpkpUZQ9P2bvyHBizyy30UEh71a-h4s0kfZmZtMgrMz57nowjkcwHrmlSgjQ8qvwCMlSRj3SgbbGQ7WiEHo7cjbv3-QPn7Thx2UPPp-T_stZS4sYZ4CZSlqlNsPvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82c725d14d.mp4?token=LE6r6iwYFvQBUajLn83HOr196B8TlnvqjpAuCLATjKzbNHsXVh_ltwD1hQh-AfKWgilbyQz0rki6BA1xOfnEYwDeUePi6mNb2bh2yftdYwDP5j5dIQMoE0CE1Wogy3YIg_mhjMSM1jeRQmg0_wvhfHZ10wVFj1xTV2vivJf6SY_B7MSG1v5cwTZXJnCv_miD5hWj8oiYbL4tS1yVpS3-VwmKnYpkpUZQ9P2bvyHBizyy30UEh71a-h4s0kfZmZtMgrMz57nowjkcwHrmlSgjQ8qvwCMlSRj3SgbbGQ7WiEHo7cjbv3-QPn7Thx2UPPp-T_stZS4sYZ4CZSlqlNsPvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: خودروهای بالای یک میلیارد تومان مشمول سهمیه نرخ یک و دو نمی‌شوند و تنها ۱۱۰ لیتر بنزین ماهانه با نرخ سوم (۱۰ هزار تومانی) در کارت هوشمند سوختشان شارژ می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689513" target="_blank">📅 15:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689512">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
وزیر راه: پروازهای خارجی برقرار است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689512" target="_blank">📅 15:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689511">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: خودروهای سواری شخصی ماهانه ۱۱۰ لیتر بنزین سهمیه‌ای دریافت می‌کنند که در سه نرخ (۱۵۰۰ تومانی، ۳۰۰۰ تومانی و ۱۰ هزار تومانی) در کارت هوشمند سوخت شارژ می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/689511" target="_blank">📅 15:43 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689510">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7efae34b51.mp4?token=HS1n2UDpRcOJervNEkGcYzpIORePlQGAbpL25RWKxbexDWLgR2PJZFcfpTaLcf9p0KCq1PCH-Q3oHAXEZKPFRupAf6pYDXldDG57eR5tMY7xtjwlbyeGdpfw5RyY3paMkkisA3pDeNvewWogumNGylEzKniIgQFj6agND9YGDrN94poVoNOpHg3lJCVvne5a4QsK37GbLbIe-NpFaDmABdhAT_D-OxNMEY0L0iK7-vv4G73qg3QC1ibX8X8-375F9DBoY4ehcGDGlsrCetOMM_MoRScuolwOLSM_JmVhDkPheCv-avYTXRcgeKI8t2SU9mkYJZNaTEsxTiD-XwXj-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7efae34b51.mp4?token=HS1n2UDpRcOJervNEkGcYzpIORePlQGAbpL25RWKxbexDWLgR2PJZFcfpTaLcf9p0KCq1PCH-Q3oHAXEZKPFRupAf6pYDXldDG57eR5tMY7xtjwlbyeGdpfw5RyY3paMkkisA3pDeNvewWogumNGylEzKniIgQFj6agND9YGDrN94poVoNOpHg3lJCVvne5a4QsK37GbLbIe-NpFaDmABdhAT_D-OxNMEY0L0iK7-vv4G73qg3QC1ibX8X8-375F9DBoY4ehcGDGlsrCetOMM_MoRScuolwOLSM_JmVhDkPheCv-avYTXRcgeKI8t2SU9mkYJZNaTEsxTiD-XwXj-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر سامانه هوشمند سوخت: خودروهای سواری شخصی ماهانه ۱۱۰ لیتر بنزین سهمیه‌ای دریافت می‌کنند که در سه نرخ (۱۵۰۰ تومانی، ۳۰۰۰ تومانی و ۱۰ هزار تومانی) در کارت هوشمند سوخت شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/689510" target="_blank">📅 15:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689509">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxMB1Aqkb0XSNerq5XxFmdJpqwXrKKeUx6AgMM87S6Eiv-eGBIXt3fHR2GputgFIGy8ywKD3CGYMPOJ1gSSS2dW8C0aY3lyRJU9lQZod6d7mzfDAoTfK2-Wy7k_-jM8Y5li4aGyZgkgzrkezePOHag-BWgTwMbw5SfQ3CbEXJTR4hZlwi7Kr8yqk51yA8fYvkXI3EgG5WGJC3p67FaxXf4dsi2ASWKkYyojkJN4cubS9nCuHdR9w954BVAUjh69Z1lYizCJ9n9GI_s3pvf8vn8BCnvQo3NyQJu71ZalaEOahXrpREt8vS57nfxWFAV2kXSQL4OQ2MDmS2BRvtwcLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس نظرسنجی‌های جهانی اسرائیل به منفورترین کشور جهان تبدیل شده است، با ۹۷.۵۵ درصد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689509" target="_blank">📅 15:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689508">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwSsDLNZj6-zmALD9Kbi-91YNzayOl9LbjqG5Meu57euPdKD-0HP6Wm_MGFOQ2KNwqb_VcQKl81C8amODWpa593hYz40j5NjitFdL5vcFupJLMtnJXd3zedeA9BPicoF0UWKzVcNe4ra3q2Cf1NlaQ4uLI1nztqEvnU1JUkxiHns3ifhyZopwRwLRVv6O-66ExjtcIbwA-elRIYJNb3tIX2ZvA29qE1j1_FFLKzuEA0Rg3v0Zap7vydey4aU-Tt7pVMnBc4drXTJja6PNuKtPxXDsjjKsn6N7nMrGARBblfeAAjAJXHZwbExMORdP4kkyq_B_79KoEplo5nxmxFhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نایب قهرمانی سهم شاگردان پیاتزا/ سامورایی‌ها بر بام آسیا ایستادند و سهمیه المپیک گرفتند
🔹
ژاپن ۳ - ٠ ایران
🇯🇵
۲۵ | ۲۶ | ۲۵
🇮🇷
۲۱ | ۲۴ | ۲۳
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/689508" target="_blank">📅 15:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689507">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b56220818.mp4?token=haiW8jmRHeb-IyNgV1csUtjo3zI9zWJiRfPnY9PUPymy7aX1Bt8ulLIAHyPjANdWvgO1DrnHZ9g697Hz8WtFkUsn9tq8ZLnh-fPLLKtNHWH6CE4vknfLwdr43EfnYPDYYypDyJLZ11XCyHaVYwhiiRWxPkaE99Xf0AkvHy1GyCLlrA8DQFMQzlBAeBSMA8-PozXhgJ8GaW-Ho0fomAvF6dAZfw6q8NO48ghkZflVbIM4E8fPXTfQYZJX7_OnddUvEYKzIZ0Yvq7F3aNU88qaf9qI48VDYPixlAmfubJhZGxvA9OtKe_flRXnwm5Eee_eBUgl7zOb56aWMIWn-_bxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b56220818.mp4?token=haiW8jmRHeb-IyNgV1csUtjo3zI9zWJiRfPnY9PUPymy7aX1Bt8ulLIAHyPjANdWvgO1DrnHZ9g697Hz8WtFkUsn9tq8ZLnh-fPLLKtNHWH6CE4vknfLwdr43EfnYPDYYypDyJLZ11XCyHaVYwhiiRWxPkaE99Xf0AkvHy1GyCLlrA8DQFMQzlBAeBSMA8-PozXhgJ8GaW-Ho0fomAvF6dAZfw6q8NO48ghkZflVbIM4E8fPXTfQYZJX7_OnddUvEYKzIZ0Yvq7F3aNU88qaf9qI48VDYPixlAmfubJhZGxvA9OtKe_flRXnwm5Eee_eBUgl7zOb56aWMIWn-_bxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: کشتی‌ای که پیش‌تر در هنگام عبور از تنگه هرمز هدف قرار گرفته بود، دچار آتش‌سوزی شده و نیروهای محلی در حال تخلیه خدمه آن هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/689507" target="_blank">📅 15:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689506">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b09d3e442.mp4?token=T2vbLg30Y8fhM57jcwWwja-VQe_9frVLkCqOJabe6jkZBBWfm4O9HQU3Ttg33Jxg6OejK0nao-YYHjGFeKmP0PC9fnECOmJ4AlFNpZMCFWSGb9xkuhJ5hqvEHLOHjbdTGuVSUrrmA3Sem73s9_49O6bsKvx1C66-qLAJ0kqQ2AlPCml1cbgBkE9qpbtALJfjsgdxfsCCykR1PKXLDLgOqTep-55p4b_9rLuG0iSdZygQeuAD8szis1x1Dg76nAMyfJRjRPIQTy-6eYWkmUmPONlZW-4L97d61uG9SpY2iCPvgNsiO20F7ZYe2eFt6Lggpf4aBac3ryS3DNuWlTRFqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b09d3e442.mp4?token=T2vbLg30Y8fhM57jcwWwja-VQe_9frVLkCqOJabe6jkZBBWfm4O9HQU3Ttg33Jxg6OejK0nao-YYHjGFeKmP0PC9fnECOmJ4AlFNpZMCFWSGb9xkuhJ5hqvEHLOHjbdTGuVSUrrmA3Sem73s9_49O6bsKvx1C66-qLAJ0kqQ2AlPCml1cbgBkE9qpbtALJfjsgdxfsCCykR1PKXLDLgOqTep-55p4b_9rLuG0iSdZygQeuAD8szis1x1Dg76nAMyfJRjRPIQTy-6eYWkmUmPONlZW-4L97d61uG9SpY2iCPvgNsiO20F7ZYe2eFt6Lggpf4aBac3ryS3DNuWlTRFqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی توهین صورت گرفته علیه شهید رئیسی، علیه عوامل برنامه «با ضیا» و مهمانان آن اعلام جرم شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/689506" target="_blank">📅 15:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689504">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
حمله دشمن تروریست به یک کشتی تجاری ایرانی   فرماندار شهرستان قشم :
🔹
یک کشتی تجاری حدود ساعت ۵ صبح امروز در محدوده جزیره هنگام و ساحل شیب دراز جزیره قشم مورد اصابت قرار گرفته است.
🔹
در این حادثه  یک نفر شهید  و سه نفر مجروح شده اند./ صداوسیما  #اخبار_هرمزگان…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/689504" target="_blank">📅 15:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689503">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3221d421e6.mp4?token=YOdODcSDZBPPgGNwJ_guixZ_4P5Hdles-gCGiSgkCy6ryhMLdWcwAlvuEukedHsSI78V8sf_Ns0oBJV3BEOo8ZQqlKMqEXeJ6ve8i8Qwilpalt_JTJ9CF0PggfP9LdBOQrTp6zGo-K9EFcqTlaP_DVPIpjyk0CRbXXzU0iutlP3uGDEKp_-MVvtSagH-qnOJzoU-rKtx16JInUeKJrazm2cQ1D6bi3ta0vnXzE5sEwLgFl5n5XcuRnPUoSUc5l_ivGbs-inN55wPcIqs1vGaF6cskucimmY0PF60vCLEByqzSAcVjsCeJKANGPlEBQJGj7GQBjpX9O8bGfLAvnrXcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3221d421e6.mp4?token=YOdODcSDZBPPgGNwJ_guixZ_4P5Hdles-gCGiSgkCy6ryhMLdWcwAlvuEukedHsSI78V8sf_Ns0oBJV3BEOo8ZQqlKMqEXeJ6ve8i8Qwilpalt_JTJ9CF0PggfP9LdBOQrTp6zGo-K9EFcqTlaP_DVPIpjyk0CRbXXzU0iutlP3uGDEKp_-MVvtSagH-qnOJzoU-rKtx16JInUeKJrazm2cQ1D6bi3ta0vnXzE5sEwLgFl5n5XcuRnPUoSUc5l_ivGbs-inN55wPcIqs1vGaF6cskucimmY0PF60vCLEByqzSAcVjsCeJKANGPlEBQJGj7GQBjpX9O8bGfLAvnrXcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیشنهاد روزنامهٔ عبری به جوانان آمریکایی: با ایران بجنگید تا بدهی‌هایتان بخشوده شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/689503" target="_blank">📅 15:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689502">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDKIjZeW4eCx5Q79beKOftvB1YKdUIyMJwExkBPKqkMOd4ALACnhtJIwz1M557lg2a2MmPHxK9tSvoAdT-C4VO1GXhEwR-cVSY4dlne4GiH20HJMqVPQ3t9jrYqtj85eA4M1F4l723HqMPxMj1QpXwHoRNwtEqOSwvBPEMltPv8FY0MYEaWceYStQk5WxUuPs0lepS5ehxBND5NzSmH9MvTNACfDf8hx_dLiv_5d3ZFUxT20Hqa1xhe14PyqiFvJCwPpgW2oZPakRSakzW_qR7Tdv3Mg26ERHqqI_jk7TOuzneLx4Hak5oKN13o92MGAgPvElE3brsPlvYwfu9nuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر بنیاد ملی نخبگان از دانش‌آموزی که جایزه البرز را به بازسازی مدارس طرح میناب اختصاص داد
🔹
سعید خدایگان، قائم‌مقام بنیاد ملی نخبگان، در سفر به مشهد مقدس با حضور در جمع خانواده نیایش امیرپرست، از این دانش‌آموز برگزیده جایزه البرز ۱۴۰۴ تقدیر کرد.
🔹
نیایش امیرپرست که موفق به کسب جایزه البرز امسال شده،
تمام مبلغ جایزه نقدی خود را به پویش «فرشتگان میناب» اهدا کرده است
تا این مبلغ برای بازسازی مدارس آسیب‌دیده در جریان جنگ رمضان هزینه شود.
🔹
خدایگان در این دیدار با اشاره به اقدام ارزشمند نیایش امیر سرپرست، بر اهمیت مسئولیت‌پذیری اجتماعی استعدادهای برتر کشور تأکید کرد و آن را نمونه‌ای از پیوند موفقیت علمی با خدمت به جامعه دانست.
🔹
در پایان این دیدار، هدیه و پیام تقدیر دکتر حسین افشین، رئیس بنیاد ملی نخبگان، به ایشان اهدا شد
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/689502" target="_blank">📅 15:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689501">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPt6l1NGRMwz9QzxutSizs7x_ecD7A7pPCH7faKngoMkDhGJcC6wZPCnsM02vYI0m9mQkGlhmlzo5TMQAFNRmXaqktKh_XtZ9vfchUxYDn8Uw9Eh-Pr6m8jRVuVrFMlUK-Uw632cxHdYRzhOpXrOsnOWFG-7rhc5xUfSUgTJxr6TxIdVoYtbUREhIqSkF8B8tzOJ3q2MyzEpU-Ke-p1hihyPUhp1lSOm52JlAnUQtzLnYMqsolSkOQXKJC7-4sqUsdrvE8E5C8fCBrKb4l7hCYpgXrRv74S2EGl0RUW5sHhLZ5G4Qa6QKYFhpI00sR9vua0aIu5S9qLjIizZTZfYsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت وام با وثیقه‌گذاری صندوق طلای «
رز ترنج
»
امکان دریافت وام و خدمات تأمین‌مالی با وثیقه‌گذاری واحدهای صندوق طلای «رز ترنج» برای اشخاص حقیقی و بنگاه‌های اقتصادی فراهم شد.
واحدهای «رز ترنج» از سوی بسیاری از بانک‌ها، مؤسسات اعتباری و سکوهای تأمین مالی جمعی به‌عنوان وثیقه پذیرفته می‌شوند و فرآیند توثیق آن‌ها به‌صورت آنلاین انجام می‌شود.
بازدهی یک‌ساله «رز ترنج» ۱۶۰ درصد بوده است.
سرمایه‌گذاری در این صندوق از طریق تمامی کارگزاری‌های بورسی، از ساعت ۱۲ تا ۱۸ امکان‌پذیر است.
☎️
اطلاعات بیشتر:
۰۲۱۷۹۳۲۶</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/689501" target="_blank">📅 15:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689500">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
خبرنگار الجزیره در تهران: نگاه‌ها به واکنش آمریکا به نشست مسقط دوخته شده
🔹
تهران نشست مسقط را اقدامی مثبت برای بازسازی اعتماد با کشورهای همسایه می‌داند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/689500" target="_blank">📅 15:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689499">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk3IJ_jt4pPrOaSyjUFiHrUOFN8n8vU96qJcPsoJ3nRJkKoyZ864WMpQ3adKJ-d0MH_kaE3pSXEgnA25HgDNiDXfNyJh8mIAoJcQuknA7JpG_Bw0l7bvv6bs3GkoW6YGFGAPZPa5wcbvBzBFQr-TzRsM7wajvjarIT5ErEkQSZwIhSbUC612dtF9wMU_yR5zCLwqHWHoSFcSQ57yVDV5JsYEiwoy9uLhxH7YcLk94YbZ_NYxMUONvXF94HENvgq9sQiV0-v3I8C8F2Zw_kr6wjEXRo1yFDkPXnn5IU3j0TDWgszfpcBpKbbeEDgfaMlAg-udjmxOcGjMop4RGRpIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش ۹۷ درصدی تردد در تنگۀ هرمز
🔹
روز جمعه تنها یک نفتکش از تنگه هرمز عبور کرد؛ درحالی‌که سال گذشته ۳۱ نفتکش تردد کرده بودند.
🔹
اقتصاددان آمریکایی: «به لطف ترامپ، تنگه هرمز عملاً بسته شده است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/689499" target="_blank">📅 15:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689498">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28dea74856.mp4?token=S0ipSXdTSdbt_jzr-bSDlKeLZ7AOLRGH-7B2urQ8C1sBP1hz3i52c9dXLbCwBqGN40aloxA37UFPyl8PSKRhhLW-BtZjE9cVciCw5CdmZBqrsv180dW1nnB1INaKziXln5K75p9tss_xfwlYN7C3vmD9TiCPKCeaPMLoTbic4kOrSRkn2Ss_CfUUfLHQM2Fb-7W5IOUfuNez__HYOBAsH6UEoHbMQ0eDAa9KgcsTarCo-CptpU6oDcK6rg7VEFZgbObCsuLKnmppAoVxSLUrlCROECEbmGpzNcxUlRt0y3Y6Kz8HIxdqBP42W26pwcjtWAqwnRS8ksQeSxyRIQCatA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28dea74856.mp4?token=S0ipSXdTSdbt_jzr-bSDlKeLZ7AOLRGH-7B2urQ8C1sBP1hz3i52c9dXLbCwBqGN40aloxA37UFPyl8PSKRhhLW-BtZjE9cVciCw5CdmZBqrsv180dW1nnB1INaKziXln5K75p9tss_xfwlYN7C3vmD9TiCPKCeaPMLoTbic4kOrSRkn2Ss_CfUUfLHQM2Fb-7W5IOUfuNez__HYOBAsH6UEoHbMQ0eDAa9KgcsTarCo-CptpU6oDcK6rg7VEFZgbObCsuLKnmppAoVxSLUrlCROECEbmGpzNcxUlRt0y3Y6Kz8HIxdqBP42W26pwcjtWAqwnRS8ksQeSxyRIQCatA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستین چرا انگشت‌ها داخل آب چروک می‌شن؟ #حواست_هست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/689498" target="_blank">📅 15:05 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سخنگوی قوه قضائیه: برای اولین بار حقوق بیماران پروانه‌ای از محل اموال توقیف‌ شده آمریکا داده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/689493" target="_blank">📅 14:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2ee587791.mp4?token=aYzj_mkzWHOucBaJGD9HAgd77n85vqPqSYspdyGFVOUiBOQZ_5G531vYAyuNL05b2S3JWF0lU9SKYAbhKfv6LDVoZOgXGfTtO1UjTmU_rvXxbUkNi3j5sio6ybuUm-vssBymlZ4izWBiibnO3HgFkQPXEs4-GG6hYK7JZR-hFjXQmnU3XTQko0avXjyO6XQ-37bMg9Z_6UoVX3g8DGcSMiTi4I0Y1Owt2Yn159d5bv6jo07xvrgv7B2CL_mudB-6MDrbfC4YZaunEgXWCmzF2-Vkk2ksZvmxtg3HJmcPvYesH31wumORXq2v2sn6U52NVdy2naXkVA8X3GWUigtq_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2ee587791.mp4?token=aYzj_mkzWHOucBaJGD9HAgd77n85vqPqSYspdyGFVOUiBOQZ_5G531vYAyuNL05b2S3JWF0lU9SKYAbhKfv6LDVoZOgXGfTtO1UjTmU_rvXxbUkNi3j5sio6ybuUm-vssBymlZ4izWBiibnO3HgFkQPXEs4-GG6hYK7JZR-hFjXQmnU3XTQko0avXjyO6XQ-37bMg9Z_6UoVX3g8DGcSMiTi4I0Y1Owt2Yn159d5bv6jo07xvrgv7B2CL_mudB-6MDrbfC4YZaunEgXWCmzF2-Vkk2ksZvmxtg3HJmcPvYesH31wumORXq2v2sn6U52NVdy2naXkVA8X3GWUigtq_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک مدل متفاوت برای بستن بند کفش اسپرت؛ ظاهر کفش‌تان را خاص‌تر کنید
👟
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/689492" target="_blank">📅 14:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
«بنیاد شهید آیت‌الله رئیسی» از این بلاگر اقتصادی به‌ دلیل طرح ادعاهای کذب دربارهٔ رئیس‌جمهور شهید شکایت کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/689491" target="_blank">📅 14:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YN7xlOprEAKd2YpU-Vi4NPolbHHb7JnU2V1Ssoji5uYoesq10LUr1yDqmpNInN92uF0aDSe0LKjPA52HCih6wqqx45TqoJ-frXSoxMJKoMd1EKbfnjCCXUDrGIDyrzsmxHbZhv6SHsns3xIKDaGXICIWhSZ9glmFN3PJiRBI2lEJw49iiWQ98pTo2R8gHKHEdZGxulM2iMoWN23AjZCLm6TEJJB89gPewhoNKrifU27exaWf1sMLIMy7jyE4u73LMRPyURIaH8p9nNBwu-3L5unJcRmqfWLfLZrpJ5B8TSLgntGaYQFIP85GYDlys8tjx9eRkTGC4GXCJnE-7vxiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای رویترز: سردار عبدالرضا شهلایی یکی از فرماندهان ارشد سپاه پاسداران، حملات ساحل جنوبی یمن را هدایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/689490" target="_blank">📅 14:38 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ct8EFCsT8bi-rwmzrrYtqNT5ymHeVJ11ig3WRJzEI39Qci0v4jjb3l6z0BKDIPzLHIEcE3iEs34NhrjB82Gc15kwclyv-0nHmQwFF23dI84gqoiHpUZv1uYTtCtJdG7Tqd7pneCJKApIdUAoyjnjt7h9OQC6iq-v3X_kyWJl48GTwhKYdg6Ty0r_DN2_BX_3OsKP8863osyvpPN9tMiB4K4QZdgfbcb0ix89CfEwcKyjVsd5xCAznVpTU7PVx68mDkBzGcKKqe64lHS2imDgLD-KiNC3PO9Nxie-O3j_rb9qTNsQ7UQIz9jkdUCA7DhM21kNs2AncDEBCOcE41CW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر مریم میرزاخانی روی جلد کتاب ریاضی دانش‌آموزان ایتالیایی
🔹
مریم میرزاخانی یکی از برجسته‌ترین ریاضی‌دانان ایرانی بود که در زمینه هندسه و سیستم‌های دینامیکی فعالیت می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/689489" target="_blank">📅 14:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
جزئیات توافق ایران و عمان برای تنگه هرمز
بهنام سعیدی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
مذاکرات روز دوشنبه ایران و عمان برای یافتن یک راه میانی و موقت برگزار خواهد شد که کشتی‌ها و نفتکش‌ها از آنجا عبور کنند. این یک مسیر میانی است؛ یعنی دو مسیر رفت و برگشت و یک مسیر جدید در تنگه هرمز.
🔹
مسیر ورود به خلیج‌فارس در آب‌های سرزمینی ایران و مسیر خروج در آب‌های عمان است. البته در مسیر خروج هم یک بخشی از نفتکش‌ها در آب‌های ساحلی ایران قرار دارد.
🔹
این طرح به نام «طرح جداسازی تردد» نام دارد و پیرامون دائمی شدن این مسیر عبور، هزینه خدمات و مدیریت آن نیاز به مذاکراتی است که در آینده انجام خواهد شد.
🔹
این توافق ایران و عمان به مثابه بازگشایی تنگه هرمز نیست و تنگه هرمز به هیچ عنوان باز نخواهد شد تا زمانی که آمریکا محاصره و تحریم‌ها را بردارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/689488" target="_blank">📅 14:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
قرارداد فروش نفت به «آقایاری» با مجوز وزیر نفت منعقد شد/ میلیاردها دلار پول حاصل از فروش نفت را پس داده نشده
🔹
ایلنا: معاون وزیر و مدیرعامل شرکت نفت در نامه‌ای به نهاد نظارتی، بدهی چند میلیارد دلاری «حسین آقایاری» تراستی را تأیید و اعلام کرد قرارداد فروش نفت به او با مجوز وزیر نفت و بدون اخذ تأیید کارگروه مقابله با تحریم‌ها منعقد شده است. در این فرآیند، مدیر امور بین‌الملل نفت مسئولیت را پذیرفت و تخلف در پنهان‌کاری این قرارداد از شرکت ملی نفت ایران محرز شد.
🔹
در این نامه، مدیرعامل شرکت ملی نفت ایران بر بدهی چند میلیارد دلاری آقایاری اذعان کرده و توضیح داده است که قرارداد با وی با موافقت وزیر نفت و بدون اطلاع و اخذ موافقت اعضای کارگروه مقابله با تحریم‌های نفتی به امضا رسیده است.
🔹
در این نامه اعلام شده که در زمان انعقاد قرارداد با آقایاری، تنها مدیر وقت امور بین‌الملل نفت از موضوع اطلاع داشته و این مسئله از شرکت ملی نفت ایران پنهان نگه داشته شده است.
🔹
این نامه به صورت رسمی وجود تخلف در فرآیند تنظیم قرارداد با این تراستی ابربدهکار را مطرح کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/689485" target="_blank">📅 14:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
منابع خبری از وقوع انفجارهای متعدد در شهر بندر ینبع در غرب عربستان سعودی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/689484" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f99f97e717.mp4?token=VLwbtDNcvCsOq-QAGDsJBN4lf6jdYwThsbT2vEEsdm4-0mlioUCPvfEIGOZuradflQrqNHgxxAblKY93fkUEYG6srVJ6RVapfRxzvofAoKgutpvhSKbtwDA8ka2EMmFtK55_YTT68cHvqG5McZfM8p_jP_Iw3A5TVEHpknGcDvezZDFr4ccy6mlnPcid6bJTGxtb9EEe6bogaL1ntbmKwXDdumyMMZBGr120NstNw6BXepJz9fVCWQw6Y6N0qetBjvy3Rn7k84Uskdn3aW21sTIHwpQPL8-Z0cIdPD2GiCZby7F7O_J2KyMUlzKxGTbW_IYYKQGvWu0hnbyNQWXF3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f99f97e717.mp4?token=VLwbtDNcvCsOq-QAGDsJBN4lf6jdYwThsbT2vEEsdm4-0mlioUCPvfEIGOZuradflQrqNHgxxAblKY93fkUEYG6srVJ6RVapfRxzvofAoKgutpvhSKbtwDA8ka2EMmFtK55_YTT68cHvqG5McZfM8p_jP_Iw3A5TVEHpknGcDvezZDFr4ccy6mlnPcid6bJTGxtb9EEe6bogaL1ntbmKwXDdumyMMZBGr120NstNw6BXepJz9fVCWQw6Y6N0qetBjvy3Rn7k84Uskdn3aW21sTIHwpQPL8-Z0cIdPD2GiCZby7F7O_J2KyMUlzKxGTbW_IYYKQGvWu0hnbyNQWXF3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی مهندسی، از دل دریا خشکی می‌سازد؛ راز ساخت جزیره‌های مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/689483" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxETk9zR3ypOZGqr_2Nusu3vpNhWB-bKtUiISQqmp3mtuSzJO1fNT4W5wVWuKO4Bp82h8Fs_Jl2ABnLeQR9oEM8kK9cTIiytQTjytBIc0H5-xX6ZUoJJADKb03KTk7tqFUmpg7bn_MyBPrM8FL6q44q58NeIi0uzeONNbUWoGZtRH7KDLk9z7zgtUhRPI6lSM1oUfUjqBcZxKM5kC3BsKWzd2DZYlnoJ0O7KjR56WXtmUk-u7cOKPHU-Evig9_hoIPylQqEndoBt0gaLAK9PHxNCJbsdMRTW240LHoJKDf3-eOMgqy_-fBDEFD3g44kyBwmVeJvRQoybdNV8c9XF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آقایون‌عزیز با این نکات قد ایده‌آل شلوارتون‌‌ رو تشخیص بدید #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/689482" target="_blank">📅 14:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689472">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EhhoSYOOwXNrop6zYGRviWNxYl7zWmS0hIO2a5NAj_DjBh-AUQQWc8_yYUinWnD7IZfjuY2ivPPqdz8Rw0V3zisHWmSW6e6Fakwv0_GTSzn2uWAbWM8qmJUFJD8oVdOpY_W6oRXaHmV9KFG26-T94ndCrHYzvCHpj5ONNNLSmav_q7EQq5wJmhqO-Wo27Sof_cEDYARGXycBK0WTAh-AanPJn_4m9b6xr_d7w6vlU-v6C_Bot0cDQwC2Wo7l4ZuZtZWCa8wjsywSegSRpaH2jozhIKQgtw4Ps-Wlxj1z5fyURKb-vxtMyyNm0noth4nvZz1MxEY7Fx3sd9L18PIWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLio1LmLJBaGLcJM1RFpssGdlSh4rTEvojYGMQVHKoJh_4VWWk4gtPzMK5tD6VYu-ikMrEs5R_33fvmtZeoCC1yqYPCEu6RQoVTcFasjeZhhG9bMklxPOGxm-AhFwXWy6t-0LBiCnuMh1b9C96N6GjZCyHw_31zNLGkDX7ddsiDiMRedj8zRxeF7-q-pjqqOuBqmG1leNNV2vIOOwPYIs-lYwJPOo7jZeCADPKjOx-rrlVn6VIPfVZbvpI2PxDFLVDdSdTuDAKsyaDEr6GezMCHQGfaCRmzI6VZ5KuJG5vlJ0YBBmK1yK4dJXrkwlXB58_WM5_K3nw-_uIZvrN86Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_F9Lwg9stGHVkc2J0LZSAYxW5s3m2qHz5qjmjsAmYN69cDk-H4VFOapZvHf2X6omaduysj6b4ju5HZb9vz-sfHnXhzh_HaqMr-sIc1c-ILO-_YjOZ2eVcy0pkWEGLOwYaCS8jYgVspFWbmEfdoXwGSvtzzKyqsDCtchUXrNluTIeCDpa2EdDiz2l2yKJvON2VGXbY2vvg6fTTDrnLAoiJCAdN_BYOHVi6vVdc5KeMy2eM1vXJLhKszdUkJaaWoOb5ed9GuiuhbdYswN4YHHZ3ywblmEDNMzO8l7EOkjcaKa44FwwH7ff8T7iNaMDiKJvUtthAvh1X9wfF50rTD8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bp23Wy5ZurpC1Qv0KUP4VHDXNPGumjr09Gj0opzBT_qeSv9UJlvd-pTR--lZpVlx_cLhsu2kimkwlMPqh1F4JtYEoD76j-xxm-caWx0QZazMtkJB0vuSigb6qgkoZNcSpJ_BwmHutEhdgLjtrvYR0ts-LYu1zg5LUDrmjmQq8pGLwP4I42x-DpXYe3umu32k4GFhcJ68aX_rSskIpL-BbzDTFBDuZQ5o0J9MMFloOPEiNg0Nz53xAzw2brW0yFCvl20pxW0pvSsZZ0E6wgkUnCsQf7LkdX6I821LhIRHqy5iMSlssatnmS9BAAFQzNuoBMRnyykGKYGWGsOtUV30Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XReeE7cCA-EkVUMCRC7217GxwTXXVXMxDzgqm26oS16USWBMdd6gYdoJNaCkSLLaK9C4Gz6pWb6jyxnCcRZFbZG_fRAa5g8Fd8wIvFEB6utjvAPndG1TNxt-PlfnGDRjfsjMzT7f8B7ex_N8r8JEw0UpuThkr4lklzr2riWNukN1x4y4Ole7--LeUdZUs1mS3FJfyZN4FhqgwQHk7gaws2Pn8O2d3A1h33yD4OQ8-HCuOqrRuvixLEzStohqZXX12ofALF9OJM5q0ccSloBUgdjf5CFhcs9pN-MVqT_ugip8CWKy_hdJ9ewGOFfD6uvNOhut0oY5Z5hF5-gewx4KEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UMxOHEJgxoto1cCtimWjOcmkRh2QPOhlcvJuA2HSCgvHpq6AgOUMhH7hNa4pVU5ZIva7DFzEOv65VUwZ522MfS3MbbjFfy0acdKQg-T-Gm9outLDqtBEcSn1T4WgnSX7ii-5iE_EFoFvW7_JcRA-EOfC4EEeDm_KgBIgEBDsm_cbmZUbWRj6AWeiFZlbBy7pIyiSsnkOWpSEQyopKf72kMraN1ht9BEqZR1vZvecqNtQLhPeqGisyIWlg_mHad1VnVxv8z13P2vMtVsWekKorj2badg9bzjmRVK2T2kBn-wGK7n4nRsnvXIOvWXZ8zcWK4D8GTv-pJnmgMHOVS9nQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAYHDzyOFmNiyWR_IK3FdUy8K4ic5CTvVjmfpZd2zAH2tfXgav8b5sOmhWyA_xGQ_5cHKDlDAazTjTfx7GmfkO-Y9rMicts04yJmew4eI5FUYo1zwrd29qWE3GRVg1quaN1OephYfAVsJ7XhGY8iPVIU7fvUrAsEOwOcpbbz05Zw8I6ZMiIFnNd3-U_PZh2lYWS5MHVoNdEQ60RMh416LFX8P4uKetwtribzSbxmKZBOZOItHP6fYGBnpU7pQc8QFbBDqJhsLQLaWa72pZq0byYOFSmWVIGV__cthkdpovb_kHroLrI8jhxs9sKAKYNQIdz-quN_9s0JkE1nZzSpjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9MzSf42H-LvVr8YDoi1QQf1QIXvGQuHQ2vQq6qtyv6WorGNgot8X2daQYuNljLnxAsxGcYCU4FAJyaelcocZQVikypNFwZpyOnyY0EREOGyg9uE0lQh8hXXSegWuHXGHbBzLaQrwnhupWJUlX5vPYwww8UZw-0A1cUHuocClvUaeCMacY3-vK_ON9ySY0iZ49I11SmYw-NUk-C_b3h4HN6xSB94-FsKbKgKH36jxarO0BMWus53Nub0PSlGfQhU4MItEptAUQziWeEL2Gr0cENvCCT63y1HzQP7em180bpO8XqUqhAu8ZZQdgNi0JB9iPGmp9MnOD3uaH4z54_shQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkPYiLaYloNh6ZKxBnSoRPSqGGY51g4_dvMvrQ3NVplqBB2LfoCJyikoZ-jy5ISlJXNdP92hnKjw-ZsdciqrBE-NpuDjbgT8qXJrhotiAghOQGEb5nD_LPltwc9REmbzbqhWWmoZmxJmjwoRHr52Jp9Zan5aYk5xTXHkk7G0yXaUb520nMZZ3M89eRXEpNs4xy7jvFWqtkO9TTgfJHEno4bi8eVOWMcEWsX29ziNCv29MioXgmahNyaaTIWu3yD4xtKdC6xU2hMIIpnmv0AnkJ-mIOO2QSmSfFRhpRdJKq15U3fd4_2DG3T3iKrHIcHJp__XCTt4Wg0kOH5P_uEpzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4wZWabK19mueaqkwE3aH51cMdcVsgAF5ueY9-7iH5xPLVK4PWM-rtBaWoaeI4TqIGvspQvK7jNEk8rNy61xNGsdgcqC7Zn5G7MPX97xbA7EaZeCZ7EEqA-McGuoguOJsRoJ2PCFCh-ShzGXq74_Re934sAXDq7U4PI1EtVrNdiJtSaQ0f7fTTG7ubOQRTt2DVh1Rw6igDSpaD6WPA88GXFI2QYctPhHNkUpFiUCmahVOERiBSyD7O-avHLb7-4lvqPd58HrJ0bN6FxJj8mfXFwiE0q_1ASOzpfOTEJfKePU7jzGBw-VDKj3s8zx0fxytpm3wHmvSldPSGGjas0ECA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
دغدغه‌ ی خانواده‌ها در آستانه بازگشایی مدارس
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/689472" target="_blank">📅 13:57 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689470">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e80b888.mp4?token=MNUscqhWXng4_Tc7Ch7lx3BVkn8VVTRpIZrXSAcZlI8ULpEMqO1rhN-v8yhYi41pW7zmmibqO10o_x6vOCTAy4ZUGIDsbdyAHDZBLr-HjVjneERKpAsUzG9R61OlG0pXwflXXdFG2cBcHcgUz7JxOWl8jqJkVrX4uc9CDJhqO84ZXkkTaIbDxzgKLy0pzK9Dxw4kHjCglCLGSqQPRm5hDd3aZRdkx1sbCsIyWf_3Mse93uJDdfQqJ6uMv8YooaxYACFqAUZ3y07d_PqV3ONCgCTDI8BjBGX1232LpXOAg_Dvkk2XvryPIXEUdMr6tFFjviFZPIRqzDVGQRbrLs60hUuutWW0Mq5W9AkQL2C5jygBCB8YD7SwfCo4YGzO6-AhLuii7kfD5Eu0YMfl_ZvT1j3NMbjLOwTX-e76qR27kbkcFnAfnISMi9qIuh4_GxH-QZdPxIFd6WAAEjnOyRNcJVpRkFXD4BJNWc6v_ut5HOnCPtZb3e_GW_AzTRmgMTHhIkyBD32V0aZSDTJTRATNtHOCTGrIw6S9CNIsMpJwVcHjOijZB9xSXky2YT6PmK5aMQymYcfUFVUUXAAYWp42YhVfTuhRoXOiJDVjRk3U3dxnEDyuZM5RJYUK3CfCAtq7mkjk_cdeIsi7KjyFvrXbM91qJY2PX6pgi82bTNXY_es" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e80b888.mp4?token=MNUscqhWXng4_Tc7Ch7lx3BVkn8VVTRpIZrXSAcZlI8ULpEMqO1rhN-v8yhYi41pW7zmmibqO10o_x6vOCTAy4ZUGIDsbdyAHDZBLr-HjVjneERKpAsUzG9R61OlG0pXwflXXdFG2cBcHcgUz7JxOWl8jqJkVrX4uc9CDJhqO84ZXkkTaIbDxzgKLy0pzK9Dxw4kHjCglCLGSqQPRm5hDd3aZRdkx1sbCsIyWf_3Mse93uJDdfQqJ6uMv8YooaxYACFqAUZ3y07d_PqV3ONCgCTDI8BjBGX1232LpXOAg_Dvkk2XvryPIXEUdMr6tFFjviFZPIRqzDVGQRbrLs60hUuutWW0Mq5W9AkQL2C5jygBCB8YD7SwfCo4YGzO6-AhLuii7kfD5Eu0YMfl_ZvT1j3NMbjLOwTX-e76qR27kbkcFnAfnISMi9qIuh4_GxH-QZdPxIFd6WAAEjnOyRNcJVpRkFXD4BJNWc6v_ut5HOnCPtZb3e_GW_AzTRmgMTHhIkyBD32V0aZSDTJTRATNtHOCTGrIw6S9CNIsMpJwVcHjOijZB9xSXky2YT6PmK5aMQymYcfUFVUUXAAYWp42YhVfTuhRoXOiJDVjRk3U3dxnEDyuZM5RJYUK3CfCAtq7mkjk_cdeIsi7KjyFvrXbM91qJY2PX6pgi82bTNXY_es" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا فیلمی از حمله به یک شناور غیرنظامی در تنگه هرمز منتشر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/689470" target="_blank">📅 13:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689469">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
نمایی زیبا از منطقه چشم‌چیت، دورود
😍
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/689469" target="_blank">📅 13:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689468">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
معدن با شعار زنده نمی‌ماند/ کمبود مواد ناریه و سوخت، نفس معادن را به شماره انداخته است
دکتر سید حجت زینلی، عضو انجمن مس ایران:
🔹
امروز بسیاری از معادن کشور، نه به دلیل نبود ذخیره و ظرفیت، بلکه به دلیل کمبودهای اولیه و موانع اجرایی، برای ادامه فعالیت خود می‌جنگند.
🔹
کمبود مواد ناریه و سوخت، نفس معادن را به شماره انداخته است. صدای معدن را باید پیش از آنکه خاموش شود، شنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689468" target="_blank">📅 13:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689461">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FSHUrM100fytq4Pdi4Lb91pm44_cs2ICBfMKSHhwgbliF7uAxnzHDSHiwm8zNHeBhCmoTDLLoJxvNz6gUbDEgnslzD1VVmct0UMGoK5yRhdwB5aQC21kIXsvs1coAc-efRoL9eWU3WojYCJDjGeZAx0hI25YFmARhR1jo9OysE2XRStjbnGfiIK8_1bJ2qN18lXuOvheQxGwc4iXD6SaB3iY3mHgcr7He3QTK28_13YZKtpv0MkJy0upyX3zaFQaEV33WW0fNBfxLfMboWYHIy_8_8Xn1a3h6GdFHrJjSFb42fbBPWCB8LpV9w2EYabIwiP0ISGU_hn3LmTccn9VEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v5fOiD31GWcHSB6PMlJgvenUMbG1gv3lCToeYUxmI1t_ncW4GPDjjTLcDuoK0KG41CAgiPmTD5x0jtFJ1eub-sJ1xcFdb0TEcI80gkP4BIr29YE-Zh9Kq80QFm-vhP7gxqozEcvkX2vthhDA9E8PGmI84LEK-fHoPKMYX5OOUawwsD-eZr7L8dKRNCRMyL9TI0__H-oMEr_c8VxfumSODCR8wB0oZG9A2bWK0YdxxPKm3MF6Z_eR9DNbpFjJhDKiYtr5LI2Cu7bpOMP6UETvBBWzPYBJxNGN1QR7Yc0NkGm41wb-YDOyDCjTtpvkztjoy-YRt4vFjmDKNS-UbuzsBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3RcVqNTenRLPh2ZdeyZ0BEPh1zhuIrnOKW1Md2tUFCtoaskHOSPDKy_omO5whYNSjjFTVFPiprvH85Bmfh2DLFP56P7pZGPVOuSe1cQUxgiqkXeSNf-gd4Uq7-rahmZz2W4u_8Zics2inyfPz1l694nlZr6xvKQP0KKsHCowx6NnsHb3efy0cpnmMnBCn7VY55MGL4i5INi745BtpejgAyRdFubGpnhimaY7OsXT734x-fbRCXreJrvdmmeKWp0bm1ob_gv9DeB-ChXP_b35cKKKH7PI88e_kaaCT29GcjslECP4rIHPI03Bhckr2GWzLOOo8a0X5l4lGTyk6SwLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nxf5aq_1v3EkI22b867FJU0Bm9DbO4WvwdiPosvkMrGSq81h_TapMkKcnx_e_xfzQU87SZ3Gs8l37tU8GVuomw7vUjE6vxMPvjEYDbP8GTYkR9UPi9_9sESkA8QLX4N3hlU8Ln7HQOsXvmovmgJZN5TrkodiLzP-HUFcUrORr0Fc5JAHXZmRuJY9eS20eI8SnIB5z36AaRzM-m5IV8rksKXm9BcO92Ltyn7HVrUySj3LuGxnq0-3mPqqhTLOoJxY5IJinqTBdYDbEPyzHWlA9RMQjXsjuKKiSsHqn0qLb2CLZHqOeGtTL_t8Hse9fLpCyLV3eJOIUZrI33AUMVyN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VozqLMbMQ5PpY25WRinKaijujRJDpyCSU3IWR8RcgeoK_J3M3fOdsgU6KLbnxQ9mCr24CZY2HTn8PkVsuJ8A-R6COxImbR8qoJKFbcZ9L-sQOA-zLslS0CkCXdF96EcPorLppioatqaSw-c1XNYo14GhmBzsBw383Sw9auVNGOwp47ovRsJ51izE7Ref_Llz1M8uINA8YaYrV3j4Y86n6dNaNDMJzHxPfhkZkh0TnYFn0wyST0C_HWWZfxWLPDSrnCvF9iHIPeaFjaVNXAGVBferthXGG7AGuEuvS5XBMvxNzfITDl7rqXg5Pcv2jFabhzdNFur8D53fBjppf9Wi4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDnB3WLNmf0a-CBFI8VT5UeSCl1hV8VGEwkMmTuUS0vQ6F1hpxwL40HcHtkecTmGJY3g77i52qaABGIa4v5kOo6VyW4SkVrRTpBssk_vf5VivFgE1CDln2B0ZltoZb4fdM02civs_YUneh3qYoZkAtbWEcMMiOlV565o3tYpYbqiqwZUsb8fgagjHnOqw24Y7OsYhw3BRsqXVkM1KalN8TFI65bJRt0CRYYeMORsz8wufy7X6ipaHDwmkiX9eoolBRK-iJkCg8OELHmtQzVhO6KcMNxgkfoMoCT-GQKXdBJN5urEEHUKfmaD-hP9kD2jecgeOzvREgJv-CuhCvYVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fPGT45y917yZsHaQYNx9ikDsAcHor_4SSY8xxEbQIGRi9Q7kQK0nvd4EnXGfb5RWsGzKOo3hitdRsnxdu2IbBCsrbgw03cWBUCbusxMIOxDyXvWPMFp_0h7NygS0iOfGZHCsakNRz_p-JhIT6CAnWRAh_q1F6futIh9zYwmcrnlwxtS4fvTkwrwspXc_SMxoUet2Ft5faSjIaJrWPBk7FvrqOzgI2DQ9l0voeDnk3cuBXjYpihYfjb2dxZNvl8xJKU7Px2WF4Dgsg0wdRXGFXzHlpcTS6MIja61G-72WW21nL0aAav40ahKFWQZ2Dv5rQ6tVGX0EAQqbT1yRE3-KrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار؛ chatgpt نباید این اطلاعات را درباره شما بداند!
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/689461" target="_blank">📅 13:42 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9f44dd96.mp4?token=Q6jb7atCk69CJYdM711i1WCVpb6WApD_1YlRlSJ1Sh5ILxEitKEJ8dvsquJF3fjACLMnVSx0935hBcEDuehYyLfLlfKHybbMYXZmMa2JC8pGArVBIAZefVStZ4cztARoaDAfN9nApVORMPamWGL6Z3RaT22pN7c3zLBY9nJbCnvCYKGl05uwdyAMLpsMyRuzuyIMTiWzOxHuJZKNhqanx1mviv5UTrNqPg1fmVfBtgl2vZY2xNVTr7t_2OVyEkGyCy5gyAhF-MuSO15_lpIMRphZG1HOAq8yjoLmaRFiXQwayADHR9HUM7TTyVyTiDShMuR46NDM-1b1vs91zUy9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9f44dd96.mp4?token=Q6jb7atCk69CJYdM711i1WCVpb6WApD_1YlRlSJ1Sh5ILxEitKEJ8dvsquJF3fjACLMnVSx0935hBcEDuehYyLfLlfKHybbMYXZmMa2JC8pGArVBIAZefVStZ4cztARoaDAfN9nApVORMPamWGL6Z3RaT22pN7c3zLBY9nJbCnvCYKGl05uwdyAMLpsMyRuzuyIMTiWzOxHuJZKNhqanx1mviv5UTrNqPg1fmVfBtgl2vZY2xNVTr7t_2OVyEkGyCy5gyAhF-MuSO15_lpIMRphZG1HOAq8yjoLmaRFiXQwayADHR9HUM7TTyVyTiDShMuR46NDM-1b1vs91zUy9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کم‌خونی داری، این خوراکی‌ها رو بشناس
🩸
🔹
این خوراکی‌ها می‌توانند به تأمین آهن و مقابله با کم‌خونی کمک کنند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/689459" target="_blank">📅 13:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
عراقچی: توافق با سلطنت عمان به هیچ وجه به معنای بازگشایی تنگه هرمز نیست
عراقچی در مصاحبه با العربی الجدید:
🔹
دستورکار نشست فردای عمان، مسیر دریایی جدید در تنگه هرمز است. جزئیات توافق با عمان و نقشه‌های مرتبط با مسیر جدید را در اختیار کشورهای شرکت‌کننده قرار خواهیم داد.
🔹
شرط ایران برای بازگشایی تنگه هرمز، بازگشت آمریکا به تعهدات خود در تفاهم‌نامه اسلام‌آباد است.
ایران معتقد است مسئولیت تأمین امنیت و ثبات منطقه صرفاً بر عهده کشورهای منطقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/689458" target="_blank">📅 13:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt5pLsuhiAiXBzTWPp1AQi4WysA7ciDsypcXF80dbP86UpCycX-BIWgaBHscKxeEGOprWX-pXsOw5xP73ndmZudQjR7sE-NCLe5CXAHXg8LrFd-JQEujVtsqT9dWHEYEe-NEK3yWpsGtW_aLYTUS57g5hCDG2z7QKNU-YfsZ_OopepT-I-6Or8u-XqZRTq2rmIbQhh3UQa-2Ygc4L508I1xjxMpT8AM3ML_tXw5L7-eAcBr6YOkIb2CW2OiGx1PKhu59kcWKwR9o_fr38F3skbwuBpb4OUNcBWi0nqb46UtG1xuyjIM1V8qJqaAbqx93JbXwtYq5QG0YY4ND0Y7auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دهک دهم ۹ برابر دهک اول بنزین مصرف می‌کند!
🔹
دهک دهم به‌ تنهایی تقریباً به اندازه مجموع دهک‌های اول تا چهارم برای بنزین هزینه می‌کند!
🔹
بررسی هزینه‌کرد خانوارها نشان می‌دهد هرچه دهک درآمدی بالاتر می‌رود، سهم هزینه بنزین هم بیشتر می‌شود. نکته قابل‌ تأمل اینکه هزینه بنزین در دهک دهم ۹.۳ برابر دهک اول است. طبق تحقیق سازمان برنامه و بودجه، حتی دهک دوم نیز حدود ۲.۵ برابر دهک اول برای بنزین هزینه می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/689457" target="_blank">📅 13:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35529d784e.mp4?token=F7re0WF50FwRPyonsFKlrdo8oOBkQ8acvtCCOm_O81dpRrVmBOp1Zkd4IUH_8Jay4_43-uLpU1lZpjL1GnprxmBlYrBH7SFfATYdPMniiPA6tmuev6UEholzW9deJEEl-MUO5B0LX54gTejmiM_spHlESarjj6bS_t9yXnb9Ilx7-iLa7MsUKvhKnwc1V0A9jKo44kfy1Tf5SN8i-65iwl53yP6tXTiIs2lM03stzFN5yvrW-bpe_9y432IJHUX99H6viyOMWrMo2WRJs5suEJXHcCIz6NwNE4gkQyjiXggauiOmPYZLKyCRk9zmeQw1NK8TJ4No-67xuqxpKiS8hAuDM1qTISz8oJNQDEV_B7bI0t-6d1Ab6hk3COHZKzZ0QDI-Dfr_dsG0-ftVN23dthgiMfZU8M7AleRIhHrEzoDVZqlZvX8M03kipJmLIV8boQ8jPW5sE3Wk6S1wW9kBrvuLbPe8N97oXBlm3ejAHFIE-BuSN4p5Or9MHtSgoQ6bwfOp86TSmGN2KPNQPIDcaK89H1cuOLdnqliJ8-n8OrJveYSbO-xr01-uWj2j-UDcmEevXBdw76sG8KQt0us_aQBgr2jT5W8QgL7OAMBDtcnwfnP11OrcKRUoeilYTYjo8oeSO03ZY1_qI9BE91hsAJk08xrPUAhxu-UxBg_W4M8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35529d784e.mp4?token=F7re0WF50FwRPyonsFKlrdo8oOBkQ8acvtCCOm_O81dpRrVmBOp1Zkd4IUH_8Jay4_43-uLpU1lZpjL1GnprxmBlYrBH7SFfATYdPMniiPA6tmuev6UEholzW9deJEEl-MUO5B0LX54gTejmiM_spHlESarjj6bS_t9yXnb9Ilx7-iLa7MsUKvhKnwc1V0A9jKo44kfy1Tf5SN8i-65iwl53yP6tXTiIs2lM03stzFN5yvrW-bpe_9y432IJHUX99H6viyOMWrMo2WRJs5suEJXHcCIz6NwNE4gkQyjiXggauiOmPYZLKyCRk9zmeQw1NK8TJ4No-67xuqxpKiS8hAuDM1qTISz8oJNQDEV_B7bI0t-6d1Ab6hk3COHZKzZ0QDI-Dfr_dsG0-ftVN23dthgiMfZU8M7AleRIhHrEzoDVZqlZvX8M03kipJmLIV8boQ8jPW5sE3Wk6S1wW9kBrvuLbPe8N97oXBlm3ejAHFIE-BuSN4p5Or9MHtSgoQ6bwfOp86TSmGN2KPNQPIDcaK89H1cuOLdnqliJ8-n8OrJveYSbO-xr01-uWj2j-UDcmEevXBdw76sG8KQt0us_aQBgr2jT5W8QgL7OAMBDtcnwfnP11OrcKRUoeilYTYjo8oeSO03ZY1_qI9BE91hsAJk08xrPUAhxu-UxBg_W4M8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از محل مراسم عروسی در روستای کوهستک استان هرمزگان پس از حمله آمریکا
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/689456" target="_blank">📅 13:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9SERKtb0jIOBxINEPUs5c48_PxZF0yey424RZYa8DiQtF_XJI0mlB2BhSsDqKdDvMRQ4PbiTflXMwN1ItUC-K5dmI7k5sIFIajlGZRz8vzgBHT5TwFvh3NkACMwySV1PuVGVSQ0_-MByfPoNG8brsgyKaH_08zQ6nrRuMoQUX60fn8U-adAeuytFsVk9Bql_tlNuhuK-6eWgkUhjkDPr2K6zN9ym-g5eXNeLuGsd57zxjtbg8G_OON8gQq7hvl1Tp9n6-t0oPhYz0-h3PEL4mPifnV85BRjjO5Hk9p6EcfBRXSzFKD1Bwta5Fwl7ITYgYGY44qm3IQi-MhakSJBcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا ۳۰ میلیون تومان اعتبار خرید دیجی‌کالا برای کاربران بلوجونیور
🔹
هر سال شهریور، تکاپوی شروع مدرسه را با خود به همراه می‌آورد؛ از خرید لوازم مدرسه‌ و آماده شدن برای شروع یک سال تحصیلی جدید گرفته تا جنب‌وجوشی که می‌شود آن را در کوچه‌ها و خیابان‌های شهر دید.
🔹
امسال، برای اولین‌بار، بلوجونیور با کمپین «همه چیز برای مدرسه» با خانواده‌ها در آستانه شروع سال تحصیلی همراه می‌شود.
🔹
در این کمپین، با ایجاد «قلک مدرسه» در اپلیکیشن بلوجونیور، پدر یا مادر می‌تواند تا سقف ۳۰ میلیون تومان «اعتبار مدرسه» برای خرید از دیجی‌کالا دریافت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/689455" target="_blank">📅 13:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689453">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
اعتراف یک سلطنت‌طلب از افزایش شدید هزینه‌ها در آمریکا؛ شهرام همایون: قیمت بنزین به‌شدت افزایش یافته و مردم آمریکا برخلاف ایرانی‌ها در برابر فشارهای اقتصادی مقاومت کمتری دارند و زودتر دچار مشکل می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/689453" target="_blank">📅 13:11 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689452">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
سازمان عملیات تجارت دریایی انگلیس: کشتی‌ای که پیش‌تر در هنگام عبور از تنگه هرمز هدف قرار گرفته بود، دچار آتش‌سوزی شده و نیروهای محلی در حال تخلیه خدمه آن هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/689452" target="_blank">📅 13:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689451">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6HmUbXJmegtAxnZ6aAuPNFy46M38kT_yAfqLWyupjFclpr8Lopp-NohnVDoV6jLU0kYq3HSx-m-7kLI7aCb85uqoDGWAlhsYzaFt_T9kQ1OB0y2vMJITOqFQN9wWhu2JU3i4BCJLO_ErsEY3Ryv0ddyhQwjjusbelflTr5MoATcc7AkHdA_21OXGGqGU91-EEum2LSpaguZPP0dMfD3I8JYoRf4Fjv4dAg1-bJVa8CJJPaNnmkJh_eh6esdAwx_2gBSF_LT9xv24SUiu-QsK-sQ0RwHSNvc5C27JFh-Ai73h0QLuZADpDiFiTelTXWoSWoQ5rI0e2a2tdT7gmEfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۲ شهریور ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
دلار آزاد در معاملات امروز با افت چشمگیر نسبت به دیروز، تا سطح ۲۳۱ هزار تومان عقب‌نشینی کرد.
🔹
اسکناس آمریکایی که روز گذشته روی رقم ۲۳۵ هزار تومان بسته شده بود، امروز تحت تأثیر سیگنال‌های مثبت سیاسی و اخبار مربوط به نشست روز دوشنبه ایران و عمان، وارد مدار نزولی شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/689451" target="_blank">📅 13:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689450">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQp1R8qvzn___oo92L6rtPPlcThCpfgvjOyOYxao15Kv39fIVG3j_OEgfl-tMZ7PxIXMjXiG6SP1N2tpWhfAOFTArjb4RF8taH-3FYhCPmD0tnDNZuXJM0uBGFj_9OKdQGV5Ndh49K37oMt1alLwjc_Cl2_bS8t4MbKSD5zbauuz5wqx7f01WqbOcsGr5cPjE-jZ3bdCJ_XAEZxgYh5jOozc_2xhFJUPGTOSP-PYSPE0OOutwRdTJ0TM_HJjyTs207Sx9yN_RN6lFPsCLl0Z8xu-tjlQPBtXuiGSLuZ8dgQg9V6MF7gEzHpAT1iLMkzXwkr2dko-G-BOk_tDCnaCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: پس از ماه‌ها ناکامی در هرمز، رهبری پنتاگون در مقطعی به ارسال ایمیل دسته‌جمعی برای کارکنان متوسل شد تا برایش «ایده رفع بن‌بست» بفرستند!
🔹
آمریکا زمان و شکل جنگ را انتخاب کرد، اما این ایران است که دست بالا را در تعیین زمان و شرایط پایان جنگ دارد و هرمز همچنان تحت کنترل تهران است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/689450" target="_blank">📅 12:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689449">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e29d26864.mp4?token=qW2KincSq_kRSPS9jDqYOHFOmS7pYwoT995ESXaCW2vDUjl1CYPdvjfWQVAKVaX25HI7wBbFVLtn4RnZJS2I_nPNrQmSv4IQ_Wm_MGYjphfUud7Z0fhDj9kiXGWkcsIQ0dZXgcRcxmFV2K5H-Y1FPFLQTLZMMdWw48A6dnBhPVDSVWlr1TN-P-OtX6F_GdMsWJDdvxc-fp0YLCRqGzIIF1Gfn7r4uwR78WQlRl9nH5MwwpeNF1hFRrbkMj7zDj2iVDEa7u6exg4O4jmuu4lgeDg0iLV4_z_sp_rDAOI3AhKjbvMFpTC4FFfRSmYAciD-ClFmfuh2ZAVpZGRz7uSfGUI8-XXAhu1WisigJBUl6MNOxZMmcNUvMSIQqh5YvV4QUudzi3zNgxV7t4c0d-PsK-yXGAlHKpv_uhcfDuvJKuQEegTFSt1xz2OdOGolJ-X57n75A7Q23KyEhas3V8Rm9E5sfTHefWAZtl5i157dXY3yDoNLMr4XytCxdgu_BFOEQBC1NlBGGH3AjcSObVY2-NUbuN6JbP51wRzNo_YJsQX9VFeVKqnbdKCCnAYcFyBsJAG65ggrxry_7ARfba3QwTpp7s9yYjr5kUhwZpmZDAAf3oHwwmYA5DQzV1Wm7AkByd4gUvU5LWNzdHPaLJt2heAOSmQOnz10lw1ZbC3p9lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e29d26864.mp4?token=qW2KincSq_kRSPS9jDqYOHFOmS7pYwoT995ESXaCW2vDUjl1CYPdvjfWQVAKVaX25HI7wBbFVLtn4RnZJS2I_nPNrQmSv4IQ_Wm_MGYjphfUud7Z0fhDj9kiXGWkcsIQ0dZXgcRcxmFV2K5H-Y1FPFLQTLZMMdWw48A6dnBhPVDSVWlr1TN-P-OtX6F_GdMsWJDdvxc-fp0YLCRqGzIIF1Gfn7r4uwR78WQlRl9nH5MwwpeNF1hFRrbkMj7zDj2iVDEa7u6exg4O4jmuu4lgeDg0iLV4_z_sp_rDAOI3AhKjbvMFpTC4FFfRSmYAciD-ClFmfuh2ZAVpZGRz7uSfGUI8-XXAhu1WisigJBUl6MNOxZMmcNUvMSIQqh5YvV4QUudzi3zNgxV7t4c0d-PsK-yXGAlHKpv_uhcfDuvJKuQEegTFSt1xz2OdOGolJ-X57n75A7Q23KyEhas3V8Rm9E5sfTHefWAZtl5i157dXY3yDoNLMr4XytCxdgu_BFOEQBC1NlBGGH3AjcSObVY2-NUbuN6JbP51wRzNo_YJsQX9VFeVKqnbdKCCnAYcFyBsJAG65ggrxry_7ARfba3QwTpp7s9yYjr5kUhwZpmZDAAf3oHwwmYA5DQzV1Wm7AkByd4gUvU5LWNzdHPaLJt2heAOSmQOnz10lw1ZbC3p9lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین را با عینک ایرانی تحلیل نکنید!
عسگر سرمست، مدیر اندیشکده اقتصاد دانش‌بنیان:
🔹
اینکه چین از تضعیف رقیب خود، آمریکا، در نتیجه جنگ با ایران منتفع شود، درست است ولی مشکل اینجاست که ما رفتار چین را از زاویه منافع خودمان تحلیل می‌کنیم./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/689449" target="_blank">📅 12:55 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=TCw7mIY20sIkcoH1j15XyfztZHc6JZ-FvELSbKqelGWQbqrLSkdnG4e8KByKnIs0FaO9DsXA_P2U27KzAeJol0F059FbC4M346tOaI2PP7NPg0AVGHiMSljAmiaEErAHLmAK0HZSi46KEEFPplNsY9cmBMK4Aki7Gnjct7m-RBkOG1auOSncEqg-W9KAGI7YgYnRAuxv-cHAqKIBO5YWittvHzZ6fwg1n6ye9dXPuQe3asngC_T9-j6f1wgFSyomnz0BkDKNfXy50JLVprPVaYUM4WbAYJ8ttHbala9xfE2HqhIiMkJQLpYv0E6irEIWdhDtl70AjLiua6MWa0_-3E3ufQiWforh56YEs93aWSvI8GCLHcKW8kUqNEl4VwM4pxziQv1wrkcbBw0OA-UBW0kqKM_htCEuiAHcF0Lwuv7dhRAXbtWGi70PVbNCEV6a_7lsPCVkNTqx8OGivduMjVlfo-gBAjU-ZoSlVmi6urj4yKlmuvKAXEVb0Ow-l0pJ3m_iQPS9DnpV0C3nSnmRk-oWlPOJ-HI_aKiyiGepoPRb5fTQPOEMualf1T8KZH-IFrvw9cVumzCtIZzN-KOTiB1W-IPdG9PI5vgbprn3U6dGC_HMqV6raj84ksXS9MPipoXDQJjtmjx6Od4hoSeir9XO_8BpTXdxDORurDX_Fk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1769cb0441.mp4?token=TCw7mIY20sIkcoH1j15XyfztZHc6JZ-FvELSbKqelGWQbqrLSkdnG4e8KByKnIs0FaO9DsXA_P2U27KzAeJol0F059FbC4M346tOaI2PP7NPg0AVGHiMSljAmiaEErAHLmAK0HZSi46KEEFPplNsY9cmBMK4Aki7Gnjct7m-RBkOG1auOSncEqg-W9KAGI7YgYnRAuxv-cHAqKIBO5YWittvHzZ6fwg1n6ye9dXPuQe3asngC_T9-j6f1wgFSyomnz0BkDKNfXy50JLVprPVaYUM4WbAYJ8ttHbala9xfE2HqhIiMkJQLpYv0E6irEIWdhDtl70AjLiua6MWa0_-3E3ufQiWforh56YEs93aWSvI8GCLHcKW8kUqNEl4VwM4pxziQv1wrkcbBw0OA-UBW0kqKM_htCEuiAHcF0Lwuv7dhRAXbtWGi70PVbNCEV6a_7lsPCVkNTqx8OGivduMjVlfo-gBAjU-ZoSlVmi6urj4yKlmuvKAXEVb0Ow-l0pJ3m_iQPS9DnpV0C3nSnmRk-oWlPOJ-HI_aKiyiGepoPRb5fTQPOEMualf1T8KZH-IFrvw9cVumzCtIZzN-KOTiB1W-IPdG9PI5vgbprn3U6dGC_HMqV6raj84ksXS9MPipoXDQJjtmjx6Od4hoSeir9XO_8BpTXdxDORurDX_Fk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد افزایش تولید هلدینگ خلیج‌فارس در سال وقوع دو جنگ تحمیلی
🔹
شرکت صنایع پتروشیمی خلیج فارس در سال وقوع ۲ جنگ تحمیلی توانست با وجود ۲ ماه توقف تولید به علت شرایط جنگی، تولید محصولات خود را نسبت به سال ۱۴۰۳ افزایش دهد و به ۲۷ میلیون و ۳۰۰ هزار تن برساند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/689448" target="_blank">📅 12:52 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
