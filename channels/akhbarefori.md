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
<img src="https://cdn4.telesco.pe/file/L5Afs93IK0rhfbkIbzuPgX8LczS9TVhkJ5vXPv9N01EugmsKN5omL1KLLp9ITMoiJrtbxksLa-uoTxcwN8fXDjsSlEPnfaVJpAuxmyYwZHcvhT7x5OcoivclBUIq8uxqwLEnOinUwmvyDIukSLmFkzoeul0_6t4n4kVNjPQMFTMYzgmGBYjaURrVeUGZmzvQPKUB5buihupC5W8PHtiG2ktnqt29N357Jwy6V5krx8gz6-Wk8S9_EbILHl_cNO5I0uLxbLjTF6P0aots7tR5m01OfH6rYn8uF810ObCA8eCigIkHAQwb1xeOvDp3GLUuLFQ5HGcoCmLJ1fHXaMoV2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 09:53:06</div>
<hr>

<div class="tg-post" id="msg-665542">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8982ab33c.mp4?token=k-QGiS09TKc1b2ygJAG7xwITHNcnWDkbDU7Bi2oWrNNwak8JZ9D0U4W6JChsP4mvGHggUFQX2Ot8PtRIg7uYkSujLvBp0_CIXL5o68aLk7vRxfM2dwhRBYH5PYrAv4fZxpIuaINP375w3okwsc9b0fDCPGehRjahgTiaddZ8xIUDRmZq-KJ5SgdCOWvT16-MDZ31wZBZffFnRUKDXRhZ26iekle65PSbc-5-pNtG5XquO_La11M237SakgLVsAGRVcIZKXDPvcKLqFMV70OAuipdVVI-m0njDstvz_t7qcv_HZqsfjDz0NSKSLS_QVSy9l3p62nZi_X-kOl7Mq-0ymKmxxNz_IhOiuiPWTU9THwL4lvkZAA82hRyVS9EUhUIRx-5BgDT__o2QPx3sPym5Vp6Aq1eBCPwa7-_G9lUMjtv858yrTTESQBl0sN55jWNn3Ao-2677eO4kBEeEEWz9Gac7g2-qd2E3l5MUHio620EVJrsQqE-l25_xZ3JOXAwgBFiAa_JDazhbtLphEz4ED9pPQ7LmHH-dgK8aoeTQuzLAxRwGFDa919FGFZ-shRCWGgScApqRXG7ZDT6vwXvmd2pn7P_SAX9rXApljUvvmHHbJCaLtJxyoso_mCFyphlN8th3GLDblUOSQJCO5nYgH9jGRqMuu6DbpU3GpULmyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8982ab33c.mp4?token=k-QGiS09TKc1b2ygJAG7xwITHNcnWDkbDU7Bi2oWrNNwak8JZ9D0U4W6JChsP4mvGHggUFQX2Ot8PtRIg7uYkSujLvBp0_CIXL5o68aLk7vRxfM2dwhRBYH5PYrAv4fZxpIuaINP375w3okwsc9b0fDCPGehRjahgTiaddZ8xIUDRmZq-KJ5SgdCOWvT16-MDZ31wZBZffFnRUKDXRhZ26iekle65PSbc-5-pNtG5XquO_La11M237SakgLVsAGRVcIZKXDPvcKLqFMV70OAuipdVVI-m0njDstvz_t7qcv_HZqsfjDz0NSKSLS_QVSy9l3p62nZi_X-kOl7Mq-0ymKmxxNz_IhOiuiPWTU9THwL4lvkZAA82hRyVS9EUhUIRx-5BgDT__o2QPx3sPym5Vp6Aq1eBCPwa7-_G9lUMjtv858yrTTESQBl0sN55jWNn3Ao-2677eO4kBEeEEWz9Gac7g2-qd2E3l5MUHio620EVJrsQqE-l25_xZ3JOXAwgBFiAa_JDazhbtLphEz4ED9pPQ7LmHH-dgK8aoeTQuzLAxRwGFDa919FGFZ-shRCWGgScApqRXG7ZDT6vwXvmd2pn7P_SAX9rXApljUvvmHHbJCaLtJxyoso_mCFyphlN8th3GLDblUOSQJCO5nYgH9jGRqMuu6DbpU3GpULmyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نقش ایتالیا در جنگ آمریکا علیه ایران جنجال به پا کرد
🔹
مخالفان دولت ایتالیا می‌گویند اختلاف اخیر میان ترامپ و ملونی تنها یک نمایش بوده و نخست‌وزیر ایتالیا در تمام مدت از عملیات آمریکا علیه ایران حمایت می‌کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/665542" target="_blank">📅 09:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665541">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190a5dd598.mp4?token=dspIKAKV78zZi3xGupWf1ZrYTa4EmhcjnV0eWWPsnA3bjcWCKi9tcWC9IzLVFA55V5MN9xSpIvkYuAL9uG-oSOJiGI7pL3zHImi_IntVVdJ94LN0zZBNJQLE8lpdatcTZga7LWK0dMu8z5anXOQ3YtvZ41lSTXsxjYg3BY-2tka8a2BAozsBQ23chrpNY8W-I1giM_Rh9Se0upsoFQXxsQiy6bh391Vp4zp9L0p4tlyJdEWSsSnFcbY1DBPLqZFXbYVSANUOOLyIoXHtjxeCOPQ5MRJxxjvpMGljJHCKBeMGzgN6FBT7QDdnOQN9ylMpmUY2WcnBFlcV7oNz6lwQ8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190a5dd598.mp4?token=dspIKAKV78zZi3xGupWf1ZrYTa4EmhcjnV0eWWPsnA3bjcWCKi9tcWC9IzLVFA55V5MN9xSpIvkYuAL9uG-oSOJiGI7pL3zHImi_IntVVdJ94LN0zZBNJQLE8lpdatcTZga7LWK0dMu8z5anXOQ3YtvZ41lSTXsxjYg3BY-2tka8a2BAozsBQ23chrpNY8W-I1giM_Rh9Se0upsoFQXxsQiy6bh391Vp4zp9L0p4tlyJdEWSsSnFcbY1DBPLqZFXbYVSANUOOLyIoXHtjxeCOPQ5MRJxxjvpMGljJHCKBeMGzgN6FBT7QDdnOQN9ylMpmUY2WcnBFlcV7oNz6lwQ8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت آلودگی هوای شهر کرمان| پنجشنبه ۱۱ تیرماه
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/665541" target="_blank">📅 09:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665540">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
قالیباف: باید برخاست و ندای خون‌خواهی ملت را به جهان رساند
رئیس مجلس:
🔹
باید برخاست و ندای خون‌خواهی ملت را به جهان رساند تا دنیا بداند ملت شریف و نجیب ایران در مقابل ظلم و استکبار سکوت نمی‌کند و از خون امام خود نخواهد گذشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/665540" target="_blank">📅 09:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665538">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgMB-uT4WkfhXcvzqHvJQs7G1RKm84mYKN7zvPf_D8J3AXeFJ-r1P3v2DzaDd-F9NZjnHajClwbz3RIe6PjOB-701a40eRBvB5ywp-g4xLsSEd9oc55potro3iwJtqUlVE7974VyxBzmJ-OLK5JiPhdetCbB6Z8y3L1nL6B0trwmJbt1FI5sTGE2hS_5KQ6rC-P83CT63ZH7XdmlRQ9b-h3c75t64aYNiLUnq2DDb_ewkCGmBwBak5Kgc0C_oSy2hfx4-kiE6SVeJEG53bz9oPXKaDe1OR4vJ_KC9bbY4QPyvnAv9YepvVMbqB-PwJuqoMsAhj9OkOlNEvvka9lJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a702236dce.mp4?token=m9Kpftq8x9xUx-qNDhr-XDuvn54ux4653M377ovOnH-CaTSAN5kRyAN97WZqmWo5N-_0XoY9uoNE_46lEjFA8sluNrkx-SD4d_JJNZNAkrDDJlpiLHjdjhLM0UdMxi4tJATsyymXum0_Bd8HjyPsQFD0aa43Ex-jr-ugcNLIVBfDlT-hsDbJb7s_Exp79RYZt-swU_gvS_KYnMc0fUmBC9L_HbgDpljhhBYwIawbtV7CXtdLafWMHb5G2BhHsfx6WrWJG29lFXoZC1S_YMa_K3M7jfG7tpe3xEUxldvQ4riTq3FTuYmIT4lcncsSQReuc-2k8CCWwp6UtiL86pQ4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a702236dce.mp4?token=m9Kpftq8x9xUx-qNDhr-XDuvn54ux4653M377ovOnH-CaTSAN5kRyAN97WZqmWo5N-_0XoY9uoNE_46lEjFA8sluNrkx-SD4d_JJNZNAkrDDJlpiLHjdjhLM0UdMxi4tJATsyymXum0_Bd8HjyPsQFD0aa43Ex-jr-ugcNLIVBfDlT-hsDbJb7s_Exp79RYZt-swU_gvS_KYnMc0fUmBC9L_HbgDpljhhBYwIawbtV7CXtdLafWMHb5G2BhHsfx6WrWJG29lFXoZC1S_YMa_K3M7jfG7tpe3xEUxldvQ4riTq3FTuYmIT4lcncsSQReuc-2k8CCWwp6UtiL86pQ4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شادی متفاوت بازیکنان مکزیکی‌ با ماسک هالند
🔹
بازیکنان مکزیک پس از صعود به مرحله یک‌هشتم نهایی، با ماسک ارلینگ هالند شادی کردند؛ هالند هم با انتشار ویدیوی این لحظات در استوری، به آن واکنش نشان داد.
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/665538" target="_blank">📅 09:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665537">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منبعی بلندپایه به العربیه: توافق شده است که امکان استفاده از بخشی از دارایی‌های مسدودشده ایران فراهم شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/665537" target="_blank">📅 09:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665536">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb365f2ee.mp4?token=YL2X-Qo7gdyDaVMIiQhV1i0T9eC_bg7msxlb-GRyZdXPpVP1JZTN4lzmOE6kkk9SvSUtOPh4sTZYuw-kwlwIpbCdyjOVCxbJsKVAYw7uK-44IKhF_h_rvp-17JrLlkcsMpkt2Q5dRGzQExgsX0IJo-nBxXHBnsE_S3MrsGk3Ue7KU1If4K5HuXKamjeok4Mq71vSR-S-yeEtNanVzqzOBRW4FiRgMozlweyvGey6X5Dx7kLhwYCkd4nuiwRiesuLY65zhI_dUvz1Lf5VKQfe7X947Dmfy9L84vt-AHVaVxFmKvu83r_mvGTzq4OpSslilAiv3k2Ccx6Tbs4ogWHldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb365f2ee.mp4?token=YL2X-Qo7gdyDaVMIiQhV1i0T9eC_bg7msxlb-GRyZdXPpVP1JZTN4lzmOE6kkk9SvSUtOPh4sTZYuw-kwlwIpbCdyjOVCxbJsKVAYw7uK-44IKhF_h_rvp-17JrLlkcsMpkt2Q5dRGzQExgsX0IJo-nBxXHBnsE_S3MrsGk3Ue7KU1If4K5HuXKamjeok4Mq71vSR-S-yeEtNanVzqzOBRW4FiRgMozlweyvGey6X5Dx7kLhwYCkd4nuiwRiesuLY65zhI_dUvz1Lf5VKQfe7X947Dmfy9L84vt-AHVaVxFmKvu83r_mvGTzq4OpSslilAiv3k2Ccx6Tbs4ogWHldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پسربچه شجاع بلوچ بعد از گذشت ۵ روز در دل جنگل سالم پیدا شد
🔹
محمدصدرا، کودک سه‌ ساله‌ای که پنج روز در منطقه چشمه‌گل رامیان مفقود شده بود، با تلاش نیروهای امدادی و انتظامی پیدا شد و برای بررسی وضعیت جسمانی به بیمارستان منتقل شد.
#اخبارفوری_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/akhbarefori/665536" target="_blank">📅 09:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665535">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06be39591f.mp4?token=GxABFI5NDqgbRL9QBr5y8tdc3X0U1FES0UdiQ90pFLaDhy08t2lDHpgkY1aLl_4l4z43UIMiJFHxbXO8ZM-2-aHqvrnaFVYcR1dnTqELT34otT25XUpb5zdpjcoid4OSPVnZ5QovnSvaqipzIiEuTwMay0lg9d1TvxlPzXtzXnYH8FEelJ28_iK4OCtJovE8n4lhHKnAXLjTaT9U-MHBePqmm39SXP0RKvvSCuJGqtfcE30CWebdazc8whLBTuDq6T2txytFIA5z9coLw9lQLkrr0rk0qZaoQBGKZ-cCBoLE4CKyFigvQafHxYjgXgX60WEjo56I6bgnUvKTXmMpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06be39591f.mp4?token=GxABFI5NDqgbRL9QBr5y8tdc3X0U1FES0UdiQ90pFLaDhy08t2lDHpgkY1aLl_4l4z43UIMiJFHxbXO8ZM-2-aHqvrnaFVYcR1dnTqELT34otT25XUpb5zdpjcoid4OSPVnZ5QovnSvaqipzIiEuTwMay0lg9d1TvxlPzXtzXnYH8FEelJ28_iK4OCtJovE8n4lhHKnAXLjTaT9U-MHBePqmm39SXP0RKvvSCuJGqtfcE30CWebdazc8whLBTuDq6T2txytFIA5z9coLw9lQLkrr0rk0qZaoQBGKZ-cCBoLE4CKyFigvQafHxYjgXgX60WEjo56I6bgnUvKTXmMpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
♦️
مسیر نهایی تشییع و بدرقۀ رهبر شهید در مشهد اعلام شد  دبیر ستاد آیین تشییع رهبر شهید انقلاب:
🔹
طبق آخرین برنامه‌ریزی‌ها، آغاز مراسم در مشهد از میدان فرودگاه بوده و تمامی خیابان‌های اصلی شهر، محل وداع با پیکرهای پاک و مطهر خواهد بود.  #اخبار_مشهد در فضای مجازی
👇
…</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/665535" target="_blank">📅 09:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665534">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18700f826.mp4?token=falxWTLklaikYNesSNJDpiR279jXaSF5TVeD1Sa-vMRhZwpzbQ1Etyet8HRlRTYSZgI_kIZD1nEI_7KNqe-5Qnit-zSJijjIg8ZaHG9YI0PXtwCP6emYGQKoff56WNcV8hBZEIJbD58jzPOY5MR2qENiUHlJiPOr0z5k8Cg8UsJSdccdytP0CgOEjb7OkbtiYwr53m3WYPcmmIv77UcwJ7KQRkXCIZVfHbMr3F85b0iETe7eUQj0q971ysJus91bRO0v8NNKfNRKTm-LjMN6PugOxZApL1m8t_6Zb8Df1YJQZa2dAFVG7Rf9K-WoxjdH9mY5Mw_fk6m27q-3DC1Amg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18700f826.mp4?token=falxWTLklaikYNesSNJDpiR279jXaSF5TVeD1Sa-vMRhZwpzbQ1Etyet8HRlRTYSZgI_kIZD1nEI_7KNqe-5Qnit-zSJijjIg8ZaHG9YI0PXtwCP6emYGQKoff56WNcV8hBZEIJbD58jzPOY5MR2qENiUHlJiPOr0z5k8Cg8UsJSdccdytP0CgOEjb7OkbtiYwr53m3WYPcmmIv77UcwJ7KQRkXCIZVfHbMr3F85b0iETe7eUQj0q971ysJus91bRO0v8NNKfNRKTm-LjMN6PugOxZApL1m8t_6Zb8Df1YJQZa2dAFVG7Rf9K-WoxjdH9mY5Mw_fk6m27q-3DC1Amg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این دو قرص می‌توانند در لحظات اولیه سکته حیاتی باشند
🔹
در صورت مشاهده علائم سکته، قبل از مصرف هر دارویی با اورژانس تماس بگیرید و از مصرف خودسرانه دارو خودداری کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/665534" target="_blank">📅 09:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665533">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO4-4uAMhl7RxNKO0TSSAdLhz2gWJusqRxulTkdD-2sNmynw3a-WUiacyL-ciihTZFUs13Di0oQepoE-ayukFhVogulpdTde9dKxgdJPjYf7LJCUa5D34-0s9IrUNh2MqjXVR6xRgdbVdGTCMMUQ6TCVvLqF6ESOJ8MAwdHOB3CRxJ_-wrg8wE1_rNGjHsZrewRgXbNUFZIYT5dNfq9ZPf2LP84n995hpzeVxvLFLls82XfqkkDUuDMwktdgzIOlJ98O6ngo-jB-B0_I8t9hv_UXFH1DPv-3ZaVvNPzPfT3FfgDbGsZOxmcELgi2jHyPCZbIug2-V7-GJ-NtpMhVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای عجیب ماچادو: من رئیس‌جمهور ونزوئلا خواهم شد!  رهبر اپوزیسیون ونزوئلا:
🔹
من زمانی که زمانش فرا برسد، رئیس‌جمهور خواهم شد، اما نکته مهم این است که این موضوع باید در انتخابات و توسط مردم ونزوئلا تصمیم‌گیری شود.
🔹
در آخرین انتخابات، اجازه ندادند که من نامزد…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/akhbarefori/665533" target="_blank">📅 09:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665532">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDhgSL4_kvSbF7rhmbw5NFnli4s8UmLen1B_pJur39WqMFpHjOEW8JKXPDNazMRYCO0JWSRlLb3rWsyJw43W8WbPG-UNnj-v_oBE-m8joRy8aI-9VHEqb7MLw4-zGBjbWBhX79qYZTv1VEVhN02GAe-ULvcytVTqxZA3a_N-fSIFGy8atWjFTunib_X_JRAA01E_tO45idj6FCStyNKvzi8dPtrc1oV7Nzg7XMCFnqlxYm_D0zREuzdXAKc9rBXEFw3ZwdvSmKgz5ySxH1I02nU2nm1ZpWkAyPI_w7lDsQFWFjgEBtf8XCG5IANk8JHQfBWKrhKyxUkix_0QkT1S-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط قیمت نفت برنت به کانال ۷۰ دلار
🔹
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/665532" target="_blank">📅 09:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665531">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319b62d958.mp4?token=eadBCJu4mJN74XccL8Bl3sWW9-nwarbzyjaxpfqZpjDvLRUmHysciL0atsQc7QZ0Y27iPBGej0aMhQJcmOakh3U68QH7CZhg-KjMQqKR8pLqBjEf0LEK1Yxl8Aek7uNTkhWo12xHLZcuMN3b3jKpfEIO7fqUV_Btw5djB8WBsrdk26VuJV2lihcaxIB6k--LxsBqG16J3dKUgF7oKtWp3EpXchQ3_cwDDoTTJXHJFOVtKgzLC-vS3HwdSk8NKLX6az_ziJMjFEzoXmQliH9uw0gQRe84escmwBxTiyqu1nnq4suBfZ5TH8H3fapW4wtewNAWr0Q86vFso1K_iLcB7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319b62d958.mp4?token=eadBCJu4mJN74XccL8Bl3sWW9-nwarbzyjaxpfqZpjDvLRUmHysciL0atsQc7QZ0Y27iPBGej0aMhQJcmOakh3U68QH7CZhg-KjMQqKR8pLqBjEf0LEK1Yxl8Aek7uNTkhWo12xHLZcuMN3b3jKpfEIO7fqUV_Btw5djB8WBsrdk26VuJV2lihcaxIB6k--LxsBqG16J3dKUgF7oKtWp3EpXchQ3_cwDDoTTJXHJFOVtKgzLC-vS3HwdSk8NKLX6az_ziJMjFEzoXmQliH9uw0gQRe84escmwBxTiyqu1nnq4suBfZ5TH8H3fapW4wtewNAWr0Q86vFso1K_iLcB7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش به اظهارات پزشکیان درباره اختصاص ۲۰ میلیون بشکه نفت به هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/665531" target="_blank">📅 09:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665530">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62fbc3509c.mp4?token=lIGAjO3jukV1-rm6ZJeqZUBtkfpavujUHPBOFTox0K5SnS5JbmYQMFmzo16qfxHoBCcbYGis8VlRagdGJNRleTnbZ06DXqF08WophKe8x3Jyn5TMtX0ka4ygms9Z_do7aPoim-R18MO4H_i8s_4VdrQL-eJVIohyBSTRQBx9Aw19ebwCIa1k6hpR7DEpZYRBC8hg91xAcUxNyADp8d60DfgJ0LBsJIAUzp5mt3-JGyVHJqAiTy3ReWlWId3CxAVlz6xuX_DViVq2W-xy4zaX25glGgJ-SCvGPMakKnszQsoRPhJWwmW3F3LBDrlKW8Wwewe1Rm1eDwW_BkvL6RHyWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62fbc3509c.mp4?token=lIGAjO3jukV1-rm6ZJeqZUBtkfpavujUHPBOFTox0K5SnS5JbmYQMFmzo16qfxHoBCcbYGis8VlRagdGJNRleTnbZ06DXqF08WophKe8x3Jyn5TMtX0ka4ygms9Z_do7aPoim-R18MO4H_i8s_4VdrQL-eJVIohyBSTRQBx9Aw19ebwCIa1k6hpR7DEpZYRBC8hg91xAcUxNyADp8d60DfgJ0LBsJIAUzp5mt3-JGyVHJqAiTy3ReWlWId3CxAVlz6xuX_DViVq2W-xy4zaX25glGgJ-SCvGPMakKnszQsoRPhJWwmW3F3LBDrlKW8Wwewe1Rm1eDwW_BkvL6RHyWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترند جدید درمان افسردگی در تهران؛ بغل کردن درخت با هزینه میلیونی
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/665530" target="_blank">📅 08:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665529">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6_lNuORZmFvIKzzaeDcnVMRayI1Q6vq7yRMBjhLAdXX5HwkReZAzdf8DQibVSVrllEBCH9HEEdb3xsg-tGvZ2fNy9cg79lxdxZvnI8kykjFUzjRdD6H41z7Y5r3DmIvDtoygqPN2XZRbSVe9uh7DVCyxvvIjFRXv88idqax-eZcC_hV3nVFbTYiQOXBmrMNWE3bXTIieAgporyW7laNlaDw4_k1oJUMsEisuLH6k0bVol-BIE3lsqQ41C7I4m7MOLBSLIIgDHCY6GspVeH7hwBbhqKZyCPeOgSfQnVKNVlM4StTX4MZ3H6AVja2t-cdR3lEwYvOVAPFapbnQhKWGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی پیاپی قربانی می‌گیرد؛ ۷ سرمربی تا این لحظه برکنار شدند
🇪🇨
اکوادور - سباستین بکاسسه
🇺🇾
اروگوئه - مارچلو بیلسا
🇳🇱
هلند - رونالد کومان
🇨🇿
چک - میروسلاو کوبک
🇰🇷
کره جنوبی - میونگ-بو هانگ
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند - استیو کلارک
🇹🇳
تونس - صبری لموشی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/665529" target="_blank">📅 08:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665528">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fe1b73c3.mp4?token=uP-Bq3okO1uaNhjqpOseXSvLhamY6BAb_QmHp-PjiCwp96iGzTAbzhqOtLeoYpuUHjvREg44CwepRYh4aCJY4sIUlnidWKwi3SSGMvW4xxvLy2aVu-STy5ajcoxf2AfDKVufHfL2O4Z6igCvuZvl7Pfi7gXiTWJVZj1jTL8Q1bXUcIAMTgBEO7mgG1llfjw0a0aEQZRPTD2zpwzvocavas_ENrR7hPtkH6fNCsU1wyiqPQNzLSTYptyBztLcGiI7htRgKg1SYzWS9Ycgoieob2Ks8WlW8onVRD6-hu_ebFe75SFfvdDw_oVLDTmsuW-r8bpmy_W6oTlRJHR2Z9fv7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fe1b73c3.mp4?token=uP-Bq3okO1uaNhjqpOseXSvLhamY6BAb_QmHp-PjiCwp96iGzTAbzhqOtLeoYpuUHjvREg44CwepRYh4aCJY4sIUlnidWKwi3SSGMvW4xxvLy2aVu-STy5ajcoxf2AfDKVufHfL2O4Z6igCvuZvl7Pfi7gXiTWJVZj1jTL8Q1bXUcIAMTgBEO7mgG1llfjw0a0aEQZRPTD2zpwzvocavas_ENrR7hPtkH6fNCsU1wyiqPQNzLSTYptyBztLcGiI7htRgKg1SYzWS9Ycgoieob2Ks8WlW8onVRD6-hu_ebFe75SFfvdDw_oVLDTmsuW-r8bpmy_W6oTlRJHR2Z9fv7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگترین موزه آجری جهان در خراسان کهن
🔹
کاروانسرای رباط شرف؛ شاهکاری از معماری ایرانی در دل جاده ابریشم
#اخبار_خراسان_رضوی
در فضای مجازی
👇
@SedayeKhorasaniha</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/665528" target="_blank">📅 08:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665527">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e3f0226b.mp4?token=eWLZtWt0h8uOK5uUG15cetqdkdlpdy_u9YzMWhdG9wTjiUb6aMFfYPkR0s601xFnPq3QDH_41rGj25yPCzHiXx_PwF_gRvviPk6xeb4eP45d9MPbgLdoD5-1Y0-ENC8wP9WaSgjoZH0T6Jwh4WlU3otQ_dPIW5X3ewPt2C4L9PSAi2e9xi9i7a9OzkCYt-rvLQwdgv-FyNmf1urhy19-2ASQRZTHJ7ok442XPtjqE3KC8FOnoOX_aQK2TxnymOGrHqasp2LLCHI6tvkwA4LysaWw13VakgA6wusRuJkKkSBTZfkv_8cRsN5XFmeih6nPpK6z8CWbQgDuHyalR74Gpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e3f0226b.mp4?token=eWLZtWt0h8uOK5uUG15cetqdkdlpdy_u9YzMWhdG9wTjiUb6aMFfYPkR0s601xFnPq3QDH_41rGj25yPCzHiXx_PwF_gRvviPk6xeb4eP45d9MPbgLdoD5-1Y0-ENC8wP9WaSgjoZH0T6Jwh4WlU3otQ_dPIW5X3ewPt2C4L9PSAi2e9xi9i7a9OzkCYt-rvLQwdgv-FyNmf1urhy19-2ASQRZTHJ7ok442XPtjqE3KC8FOnoOX_aQK2TxnymOGrHqasp2LLCHI6tvkwA4LysaWw13VakgA6wusRuJkKkSBTZfkv_8cRsN5XFmeih6nPpK6z8CWbQgDuHyalR74Gpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات گسترده روسیه به مراکز نظامی و فرودگاه‌های اوکراین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/665527" target="_blank">📅 08:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665526">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85797dc071.mp4?token=XmaQzgIC5O5rZRg5VSK5lMOLV6dhiSJGbr4ovzfkFgTyjffoxen2x1Z0YexMq02xzG2d_Hg9CScHJSgM58HpevPMWUdv5ZO33W5VBzOniSgqAQKlV-TJAGpCZeWQ2WGdGPAbJwGgMu4-RSQsTjHXIJwnO6KZUIqUvVStwty8aHkbh5GRPyxQLMcNxAUmTGtH5hP5H0Mjz_FCTDSX9FHlyYu1K7Lhlu-FR2ksUNSaqK5ROKZoVsTL1O4Zptdqm8i0rHDV5lAYyH0JQrfep8JrK9VmqS-8CobMPNrQV2prMWiiYSZZZlyfF6MYCGeCJ2_H9T6-4RXvDd-RwRMZzOdMRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85797dc071.mp4?token=XmaQzgIC5O5rZRg5VSK5lMOLV6dhiSJGbr4ovzfkFgTyjffoxen2x1Z0YexMq02xzG2d_Hg9CScHJSgM58HpevPMWUdv5ZO33W5VBzOniSgqAQKlV-TJAGpCZeWQ2WGdGPAbJwGgMu4-RSQsTjHXIJwnO6KZUIqUvVStwty8aHkbh5GRPyxQLMcNxAUmTGtH5hP5H0Mjz_FCTDSX9FHlyYu1K7Lhlu-FR2ksUNSaqK5ROKZoVsTL1O4Zptdqm8i0rHDV5lAYyH0JQrfep8JrK9VmqS-8CobMPNrQV2prMWiiYSZZZlyfF6MYCGeCJ2_H9T6-4RXvDd-RwRMZzOdMRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم بلژیک به سنگال توسط تیلمانس
🇧🇪
2️⃣
🏆
2️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/665526" target="_blank">📅 08:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665525">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند  رئیس هیأت مذاکره‌کننده:
🔹
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/665525" target="_blank">📅 08:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665524">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
آسوشیتدپرس: پنتاگون پس از ۱۲۰ روز هنوز نتایج تحقیق درباره حمله به مدرسه میناب را منتشر نکرده است
🔹
ارتش آمریکا از ابتدا شواهدی در اختیار داشت که نشان می‌داد دست‌کم یک موشک آمریکایی به مدرسه «شجره طیبه» اصابت کرده است.
🔹
با وجود گذشت بیش از ۱۲۰ روز، آمریکا مسئولیت این حمله را نپذیرفته و نتایج تحقیقات پنتاگون نیز منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/665524" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665523">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a222302c5f.mp4?token=Fko3pwPBlwEFCAitpZOaCKHgnZm_lbVrwX5r7IIdbGX4IuAJWE6oDhxdqD8McYYernfCydflsIycgqhaCLqH2qCY8Lt65b0rXrzb0dbQCJaiuaucElKI50X6CNG8UG0fs10WEJRlKchwhRaejaE_ZWKVIwdyOlRaVrqQmD3slb1ITHwiFiQRm0UFFL-NtviiTRQ-No_IRSSnOEA3hz6idhhv7mg3j86dN6cdhoKdL9Vem0MFv0Lu710b6lnKWldT75lAUGIF-KJwpjPHLcpzu3lYc8h-eyap6HyKK4hwcnbkXJ25CV3p3hoEaRiKt7vjxXMalkVAqcpbsFAMaqlETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a222302c5f.mp4?token=Fko3pwPBlwEFCAitpZOaCKHgnZm_lbVrwX5r7IIdbGX4IuAJWE6oDhxdqD8McYYernfCydflsIycgqhaCLqH2qCY8Lt65b0rXrzb0dbQCJaiuaucElKI50X6CNG8UG0fs10WEJRlKchwhRaejaE_ZWKVIwdyOlRaVrqQmD3slb1ITHwiFiQRm0UFFL-NtviiTRQ-No_IRSSnOEA3hz6idhhv7mg3j86dN6cdhoKdL9Vem0MFv0Lu710b6lnKWldT75lAUGIF-KJwpjPHLcpzu3lYc8h-eyap6HyKK4hwcnbkXJ25CV3p3hoEaRiKt7vjxXMalkVAqcpbsFAMaqlETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۴ حرکت انفجاری برای تقویت شکم و پهلو که هیچ کس بهت نمیگه
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/665523" target="_blank">📅 08:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665522">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
مسئولان نگویند نقدینگی نداریم/ مسئولان نگویند در دوران محاصره دریایی نفت نفروختیم؛ این حرف‌ها یعنی ارسال پیام ضعف
🔹
یکی از مسئولان گفته است: «در دوران محاصره دریایی یک بشکه هم نفت نفروختیم» و مسئولی دیگر نیز از ناتوانی ایران در صادرات نفت طی آن دوره سخن گفته است.
🔹
این دست سخنان در چشم و گوش دشمن، جز ارسال پیام ضعف نیست؛ پالس‌های انفعالی که کارت‌های برنده را می‌سوزاند و واشنگتن را به پافشاری بر مواضع عهدشکنانه خود تشویق می‌کند./ روزنامه کیهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/665522" target="_blank">📅 08:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665521">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e7bfdc0c.mp4?token=D0k_P5deyWuIdRZ6Gt9DL1bVCWyhM22HcHrcEqpBDLqCBPb3BLC2JPFE9ARRGwJSzBQK5oi9GXkkPS75yahvMSDWEuKDyFOyvGawQON6HuW_Ymb5p0_CrhDIIl3508d6JAsHmDWNqPCamTDgDaVYMV0TcPdeK0HmYS_MQo8WqOvMjbKpvxBHP5QYZyI7epfx7rW2zL5GcVqDs3eA_BdYUuzCIGA7oUc8tk_-4Z5hRNVqyHRzfp1Ynw66mj2a6aBRbUN0Ptaovb5skj92S2_rcLfaWgujJGWhQoQvTtNf8uyAczNp4Tvvtq89bxaRDWBBEWEg6LzLOwLjiex0pE2ltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e7bfdc0c.mp4?token=D0k_P5deyWuIdRZ6Gt9DL1bVCWyhM22HcHrcEqpBDLqCBPb3BLC2JPFE9ARRGwJSzBQK5oi9GXkkPS75yahvMSDWEuKDyFOyvGawQON6HuW_Ymb5p0_CrhDIIl3508d6JAsHmDWNqPCamTDgDaVYMV0TcPdeK0HmYS_MQo8WqOvMjbKpvxBHP5QYZyI7epfx7rW2zL5GcVqDs3eA_BdYUuzCIGA7oUc8tk_-4Z5hRNVqyHRzfp1Ynw66mj2a6aBRbUN0Ptaovb5skj92S2_rcLfaWgujJGWhQoQvTtNf8uyAczNp4Tvvtq89bxaRDWBBEWEg6LzLOwLjiex0pE2ltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بستنی اورئو خونگی
🙏
ساده، خوشمزه بدون مواد نگه دارنده
مواد لازم :
🔹
پودر قند ¼ پیمانه
🔹
خامه صبحانه ۲ بسته
🔹
بیسکوئیت اورئو ۲ بسته
🔹
شیر عسلی ½ قوطی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/665521" target="_blank">📅 08:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665520">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تصویری از مراحل نهایی آماده‌سازی مصلی تهران جهت برگزاری مراسم وداع  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/665520" target="_blank">📅 08:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665519">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1kdJ0uGotgyReR_S7j6nTj6SAGX9_MV6aUpG_Adz7RJYc6OVLsWyJHWr85ZNZbIWzE2T420dz_-h8cfY2UQnB6ZXkwvN8Shu9TapJjPAZd5yUCNFFB0YOdmg7cEe2TQOfbbtHL54HqJetMmDnOW17lQd4ZbmlckDW2kJjjZ2SHHWpRZW1sCxLkdgkuq3BhN58tp4LWWJdLNVL__WdBSPmnHZDUx5K775eSU7m7AW2d_RMJskFSUisiDmGpkUf54IWxufi3uqgNDAjErlORVKHD1faFfXdHt6XYXFEG33_XCIAGkLPZdAtfkVXADXu93D3z6MI4I5pouAI3Z18Ei0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امن‌ترین کشورهای جهان در برابر حملات سایبری
🔹
در دنیای امروز، قدرت کشورها تنها به تجهیزات نظامی یا اقتصاد محدود نمی‌شود؛ امنیت سایبری به یکی از مهم‌ترین شاخص‌های قدرت ملی تبدیل شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/665519" target="_blank">📅 08:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665518">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suY2X1yQBbR6SzDupnLa82eYmGRvsW_JdATm-baFfhPpmrdDitXeQmcKehWfwvjUxmEPMFj6Ps52ZkLeydxRJ6YD9Q-Je8vWba7KgzxrZEjWy75KTEAELiEtSewTkTfupd7K9wPLoCiRYGPC2Jifu1_h_OvrZUJZHbVXy3amCpyqnYBagmLlneY_3H35_htD3ES5a0LF24xacN16ob2QvhCyqnb0Vju-L0qRTM0o5B785b6U3DOy0ND-9J_RiCtFM8ezZ187mIYU5FOsD5rHHmSW3MFD-AGLzJCI0hS1fFt14ePq_soAek8eei5Skwt5BToXjM168t_ax_-VxlZsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت سدهای تهران اعلام شد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/665518" target="_blank">📅 08:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665517">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نخست‌وزیر لبنان: حاصل گفت و گوها در آمریکا،نه توافقنامه بلکه تعیین چارچوب مذاکره است.
🔹
مقام عراقی: ۲ تریلیون دلار خسارت به اقتصاد کشور وارد شد
🔹
نیویورک‌تایمز: آمریکا محدودیت انتقال دلار به عراق را لغو کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/665517" target="_blank">📅 08:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665516">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn-_WMZHjw3gLDF1AbUPrJKKDZakZQbVOETMjxbyv9tSnDXAxzupj94sRh5ywF2YLqg_ue9PztKpuxkw-HCKm3Vs-fA-Xv65EIGCUBtkpQ73WXV0SMafFUrZjRjlAslsF7z6JeHXwxW5mWVlsA0I0cHj8JER6xhoJowKX_fVsE7-_1NKjcBrCRxxEK8tGL5AKqEEobITi3pjk9-ueGAjHRtRy_1G0YEpY25RtDcrWowSbgkMXIl-Caa7TUN0tEApgUdnp6Ac_AGk-tgdzrG5bexV7ozLe6ZTRmoBFXZ-h6JES1NsfU_tihbS0jslUOUnqBVKk9RTmp77FABHS8_Zwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش خبرنگار خبرفوری از آخرین روند آماده سازی مصلی تهران برای تشییع باشکوه رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/665516" target="_blank">📅 07:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665515">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIQYGSPIJOkU7J3XyQU8imrgQPckhYMF4URklRUyvfU-9ubcXMQpp-FPH6clc84Go3CgDpm1tTt_-6O4YWS44L-rLNueq8PMLDZM8oslflhAMdb6ftJA_B7duzMDh3QzZKEZAtpmD8jSN9aYuJ2_bhHpi7C-MGAMlroGI2zILA-1cQ2GsuK3lH49nqaVF_1Dbw5bkHJMXG8yeuuyoFTIAVQQs7yrsfVf4VevUT8PTNxLXX63KnuB1Yn311MPUagermxHEbN8V1tIOoBjSxJrZJoaxJAYC-I6UFmVNZP11mJfBM3H53yHDupijlSUTEtjFnQQHOUeaLJYobc_z4KzyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/665515" target="_blank">📅 07:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665514">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d6c89253.mp4?token=vqoNrogCtSSY3wY6ObfwYrZTaLnT5ZEtK_qHKo0ypKWfKBdT1PBM-Z_qCTMPHNoWVud5g2P9XZdS46jX9JHoxhQpYUAZ7-41eRhXYAi1-gyA1YWUGwEaJiMnhmemAYV6z6INs1HGeIcWdC5GDm4g9UUkO8nZyrg4r_aEHZpTb_o09frIwchindyRq-OfQC8wsBMmzjv641kNVZ55aI4dmG6FqjSquCJP9VnI9DupiPfN5OBGJUSYG2K0pLZxASVE_RUP2aUGhQNR7mtMfFIXShDP4suiLgtJw7KylChiI1OWjCHMexveYPEifCq6jkAAKZNkGRrSmPqNkAQwKknYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d6c89253.mp4?token=vqoNrogCtSSY3wY6ObfwYrZTaLnT5ZEtK_qHKo0ypKWfKBdT1PBM-Z_qCTMPHNoWVud5g2P9XZdS46jX9JHoxhQpYUAZ7-41eRhXYAi1-gyA1YWUGwEaJiMnhmemAYV6z6INs1HGeIcWdC5GDm4g9UUkO8nZyrg4r_aEHZpTb_o09frIwchindyRq-OfQC8wsBMmzjv641kNVZ55aI4dmG6FqjSquCJP9VnI9DupiPfN5OBGJUSYG2K0pLZxASVE_RUP2aUGhQNR7mtMfFIXShDP4suiLgtJw7KylChiI1OWjCHMexveYPEifCq6jkAAKZNkGRrSmPqNkAQwKknYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بلژیک به سنگال
🇧🇪
1️⃣
🏆
2️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/665514" target="_blank">📅 07:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665513">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
جی‌دی ونس درباره ایران: ما نگران مسئله هسته‌ای هستیم، درباره‌اش شروع به گفت‌وگو می‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/665513" target="_blank">📅 07:54 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665512">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
شکایت ۱ میلیارد دلاری از فیفا به دلیل حذف ایران
🔹
لطف‌الله کاوه افراسیابی، شهروند ایرانی- آمریکایی و استاد سابق دانشگاه هاروارد، به نمایندگی از ۹۱ میلیون ایرانی شکایتی ۱ میلیارد دلاری علیه فیفا، جیانی اینفانتینو و مقامات این سازمان تنظیم کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/665512" target="_blank">📅 07:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665511">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
معاون امور حقوقی و بین‌المللی وزارت امور خارجه: هرمز زیر فرمان ایران تعریف می شود نه سنتکام
🔹
نشست نظامی در بحرین نمی‌تواند برای خلیج فارس نظم حقوقی و امنیت بسازد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/665511" target="_blank">📅 07:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665510">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07348fb68b.mp4?token=Ktv8itJtwaDq8L4UDeqSL6Scja-l3npB5np_xYwwcwxvU7UjJnXoYmRPkuUGhnNCCZvqTsy4OqEwCc-TNpmS3GvT0qRZPHY1WHHW_-S2lZvrOwpXzMSztbaAsoOE79xy7_gXJ70Oc-PVv_ddv_9btw_DT7uUGju8K6cw1QL4F_N3tDlNCk8YYIIxYTDdDBtt7IYOcV_K6qGR2Q2stYsQauX3l8xbL-em-U8yQq-KcwVBZd2xSaaSxv9G85a7WqOMCWOJa12cqjiOlYeLZWJK3NCJBoVK7z0Mw93otJ6ysb4_swF7ny0l_xmKKK_aMdQzhUL-kSi8pDLF5WZBFEX5vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07348fb68b.mp4?token=Ktv8itJtwaDq8L4UDeqSL6Scja-l3npB5np_xYwwcwxvU7UjJnXoYmRPkuUGhnNCCZvqTsy4OqEwCc-TNpmS3GvT0qRZPHY1WHHW_-S2lZvrOwpXzMSztbaAsoOE79xy7_gXJ70Oc-PVv_ddv_9btw_DT7uUGju8K6cw1QL4F_N3tDlNCk8YYIIxYTDdDBtt7IYOcV_K6qGR2Q2stYsQauX3l8xbL-em-U8yQq-KcwVBZd2xSaaSxv9G85a7WqOMCWOJa12cqjiOlYeLZWJK3NCJBoVK7z0Mw93otJ6ysb4_swF7ny0l_xmKKK_aMdQzhUL-kSi8pDLF5WZBFEX5vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول بلژیک به سنگال
🇧🇪
1️⃣
🏆
2️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/665510" target="_blank">📅 07:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665509">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نقشه راه حضور در مصلای تهران برای مراسم وداع با پیکر رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/665509" target="_blank">📅 07:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K12jm8ZzuebCExSBNYn51XA9HS-gakWMhWtEQvKgiDlICc3Wf7mKaMX3ON18KMKxLWlf3D9qRek8DvnbmBV7ST3tThb_t2EG9QAZrb1MEiZTypUvathaMyNwNWbjE6PGgcDApbAEq9z1hxT-n6EJCLsmCWQkCp6OJzhX0BK8ckdq3jdhbEhFbNBStQnFWwjdDJAZb-6be25DdK-2kWiekjplVjtztJaBZRJULBuUFIKA5geRVTUzyaD8rz4Y0GDyDxt2ewUf0vzmACiKTgGw1vQSNfiCrbuJLrUCSj35i7KyWgIf8WV1vx-EjTrWqVlZnU5WzbNLzy2_jNv1QFUhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۱۱ تیر ماه
۱۷ محرم ۱۴۴۸
۲ جولای ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/665507" target="_blank">📅 07:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os95eWi6DrYpoBZpn501bgnk2Qgl3gTnhBJX_BXWIXWNZaEHqDRn3QeFaPHUYQ2CAdlMHmzXLub-fo8MMeRCrAHJo-w8_h_xilRkAKiRG-yTpk3Y64S6EK6xjNBuJrvhaFW-Bp7mdTVKqiOxStgdmFY3j4sg03-DjqnZxRtNG0T4yl-x5AJFiiwYRf4NGv6C0To4wbMwqB0ADFEwe2dK3ay5CrkI0NRDDQZAm3j1vRKpfmYg_xNR2QW2bti3qj29EStmwngvNdUFpJqJkJzrz7U9_yy-g74R7e9NX8jf5fTbLNB-QdoX4kQCsXsiP-3NpJptWgfM9PdSd-b2TeF_fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
پولت را پارک نکن!
پولی که راکد بماند، فرصت رشد را از دست می‌دهد.
با طرح درآمد ثابت کارینکس، سرمایه شما می‌تواند در کنار نقدشوندگی مناسب، بازدهی بیشتری نسبت به سپرده بانکی داشته باشد.
🔰
سودی بیشتر از بانک
🔰
نقدشوندگی مناسب
🔰
سرمایه‌گذاری با ریسک کنترل‌شده
👈
برای دریافت اطلاعات بیشتر کلیک کنید
📄
#درآمد_ثابت
#سرمایه_گذاری
#کارینکس
💎
با ما همراه باشید
اینستاگرام کارینکس
|
لینکدین
|
تلگرام
|
وبسایت
|
اینستاگرام آکادمی</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/665506" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromباروبندیل</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbvN2nsg7Bf9fHEmLqtQ92crxboR7iVEo3dDdskI1aEtkof_0HxXY2fc2OKSEr5QQU8TODazp6-AqazGb9lZnbPNmKV8WtER-mLFDdNg4FfdYxz2wa21QQp8rQ2V7xrbR6d0tNMDfX-1P6RxaXWf2vWi0wkwllKlc7ERwUMOBEjzWFPao4rFoBT7KzPhu-XGOzCpFlrNaMuzRZ9BmMUpYegXtjZBKHB2_ngTSHv-u4UnoublZEXtVC4SYrajEJz5eI491g7iq27h_E_hh6gPNGz4rp_mbAqogbBQ7UP3TDWy17yrCVhNlKufHdt3GpSCjm7rcN8Tu_RuiVUm_t7kSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
باروبندیل‌ت رو 4 قسطه ببند
باروبندیل
بزرگترین و تخصصی‌ترین فروشگاه کیف، کوله و چمدان
🔹
برای خرید از مجموعه باروبندیل، امکان استفاده از سرویس اقساطی اسنپ‌پی وجود دارد.
🔸
امکان خرید مستقیم و حضوری از فروشگاه
🔸
ارسال سریع به سراسر کشور
🔸
تضمین کیفیت و قیمت
باروبندیل؛ همراه استایل و سفرهای شما...
@Baarobandil</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/665505" target="_blank">📅 01:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
وزیر دفاع آلمان گفت که برلین خروج کشتی‌های خود از ماموریت مین روبی در تنگه هرمز را بررسی می‌کند/ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/665504" target="_blank">📅 00:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRQSMLHdVZzwagHX24LElI8HNwZvcrNFiwR3w4ap2gzShtiNxhh8Zz4KqRTeH4KtCM6L0N-9wWU37kxm55ZxiGaSES38UgKy9Eh1GpnGNhtcfCCzmkQlsZ12LJFIwMu7eFPcQ5xocHWiCgFP0eoXinr8cGh-K3IYbsGfWN6FqGGqc51HGIpnbUpzoWet6NBrX2NGi4LUWEv1RJYnWsO08ihMJHZkohfncogm0nFz8NasxviHMTy8oj2SVQ3eg4hl7hJU-L4_-24U5Aj2lH6TeuKyfUg6Io24c8fv8dmeOlXEmBJG9Szi-B1f7AKRcFYgdutClmPk0Bxc1JO1e5aJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانیا سر شوخیو با باراک راوید خبرنگار آکسیوس هم باز کردن
باراک راوید:
🔹
این روزا یه نفر (که فکر کنم ایرانی باشه) داره خودشو جای من جا میزنه و از یه شماره آمریکایی تو واتساپ برا آدمای مختلف تو اسرائیل پیام می فرسته.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/665503" target="_blank">📅 00:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5a9c7c5d.mp4?token=tQq6sIkzOzEzTNa16cU5BIHOuOB9bprhvHXryNxmr0fdO16UtuuSH6GP1PIFnpVmSPh_tq3x6KcnI_2A-Nl3JHAdQs90oyIz3kUAuFqvsy3ihPvGKKyYU4w7-5YDKAzsj1Ceq6qwjphlnneAkmJsfKgtitiIbuKsbFqSLWR50m5BxcEpx2cB1nLw8jfuCdVhElzcEhLxr1UepOWWoqVNpwl9t0Ub64IJOgY4F5UvZgZlwhV6IxBBBvdsH8ZOecCTqEjNsYSMB3GyWdZ1Gc9ba3w20w0UTzyyT5xTpw9poDycmPee3XqHsxhuLSEDpgiRlFDnxzug4esb41C4GM5uRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5a9c7c5d.mp4?token=tQq6sIkzOzEzTNa16cU5BIHOuOB9bprhvHXryNxmr0fdO16UtuuSH6GP1PIFnpVmSPh_tq3x6KcnI_2A-Nl3JHAdQs90oyIz3kUAuFqvsy3ihPvGKKyYU4w7-5YDKAzsj1Ceq6qwjphlnneAkmJsfKgtitiIbuKsbFqSLWR50m5BxcEpx2cB1nLw8jfuCdVhElzcEhLxr1UepOWWoqVNpwl9t0Ub64IJOgY4F5UvZgZlwhV6IxBBBvdsH8ZOecCTqEjNsYSMB3GyWdZ1Gc9ba3w20w0UTzyyT5xTpw9poDycmPee3XqHsxhuLSEDpgiRlFDnxzug4esb41C4GM5uRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع غیررسمی: مقر احزاب تجزیه طب در منطقة «ديكلة» در اربيل هدف قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/665502" target="_blank">📅 00:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665492">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZHb6S9mVnZhitrgjk9krKYo4hcYeK8ady4CAGWeOyGoCpUOckHGlh0j3pXjkAApjxQ4YS0rCv6fOBjCz7HDGg871FJMgFbTeFbkDAtWJj8mIYLcBfWYWA_WZQC6Gj62lZ5PZO3veGsBByqvXt5f3GVFMH_nBaP8CtnRUr_v0wI90k-v6KWiPV0PWT_sXWvKksRbjLFrW2aAOdzxBHQtpXXrMRvGXq2MZprzkRZCBw9d-YUO1MCGeBU4ML9Bq8kj6YIn64coP3JNWZ4RYH7QY5_3ME5EkRgWea0mQB9D5UIvsZYK8BkFAi81yP1hlfRFMixpPHOtlmRu5OywuwM2qqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbyzXI9lA8otjORQbLNKkmcJyEgl52IW2Wk6fmJssxiqBbsINdyio1zW6q3WpOPMUaQzRjA_gdYdlHJQW8MHmqamk6pYgm7jFhbmEm2r3VVDb6rLaxmWoGTgItuVYTpAm1ER5W0WBuNhU4w64ikvlHoLHp3JfGTSm-B7bapggBpT1aSt2oePj6msz-mRErAttE_Y9xY0xDM1S7-2oryC3o7qcVoTw6Gh7kwUfZcXjtdHroEw02feMYQV3Z-2heh1jJ_KjkNfB1b8Gl_0upfSXuvTP6jef67K1IO5HMzJIg-ZmXFmmAa2mDYpGiYnWzil-bKRL27fVvAE_ScnYIgUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbsBmnL8_GQkirNRSYkyM2Nuf1s0__D6vWt6XpF8xXiVh0Y-DL9qZmEFY1otZ8fD49K74Id2LvPAW61ymiVRkj553XLcG8nXN_DTqFDPZIk1NFSuq_a7wIGWWNswMOaFe8s_Yp7cOtiB3mKIVwud5NxFFcG8pWIx4kjLAKw9sr8O8RrYDfGyaJrMVMMhCbMWiVPjYGY7QShT9aVl_PqVc43jG1OM2JS_VdgMZ0jnEJVb5ku82isJRzspjv_68RrXDKOYoMpdjADfW0gCjEEJLT7v5MiII8tWqZVr-Z9dPl5Z8n-TOOxpeeA6hnboFLWaeAOVXWnO2asN4JDGBd3yjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5ez5UnAnex8VLb6zZxG7xJ8KS9lXSfAb8sy9LJtw2OY-DJV0IsuM4gG97OHBEErbstC9_jk59Oou_8POXOiaBOIAig_bK0QbsQUW9B_RsN-E7c41uB8pmFIiG-jJk6GiBNWE_fcJHl2J96fvfUFnMWmPNQIrfO_Ce5NYR-GDAL3Q12J-Fr-Jw2J55Se-aAbtVl7uPo1gtzfLZP7aVQ-k6L6awfAgOuWJre-mMiA-uMMiQlda8s6uCDGQrRdYajmop3R-VDZ8Xs6puqzv764l_GsTTRgjVQeqvpIjCYTU_W8Hc_goVqqU0IM2h0jXRSJ2XoRcenxz_MitJHRjnoyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ns2SxFeZmkUZrnSiHAR-hk-XgfkIQb9eLgyYobWqQB4_gslmlSH3aydtcTWKS-N4b1A_a3zSey29eLNsidD9JFCRlFAJJg1UwLEkkSv_7fIEmZCsqIGa94Y7D6jt0yYFgdBvnx5Koldd87210IturiSk8GF0E0De5rHE0MuAuI8itbHA-upHJ_ja5pdYTvog6QEhRM8lC9wXKPS9z-CbwUg14ck8Kd35P6FtLyPcRoWXo7XniGvBpN_hcEPIxe9qpJgTtGik8NZQOwZ9jffKhqOwM8lk2sUSa8DAc9uEn6wRIQtcKhO8J7AFnpNc4SKtjvgGabPTOUh2ojy4qD_MYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpRJ-TQMh8wVKWK3ZxjLeWytFkAxeE8JzDPaRAVf6xrYLy6MuV9GI8GY21qSD62Z_t-QGGWfRI8uA6a9t77c8NfksIbUkRxz7iHx35GUud_ebiP3iLkL4ZHbkyW7Tl86J6GZJGk1P-5HT4iLnlCHAoRAVGfITN57RCHqohBUtgunuE8AIKues7agDk6WO8OBA8WjzyrJB_h3O1UxG1u16wkV3n6_0jrkB9h-ylXDb_5K43dZOj77Waw1Pgww-qCABTl1XX7_QbCJtEFMYecJINbnHK-qpuazZHgAf9mDtXDOQEDeibP3qENziykt1e-DryC6-MlDsWYrhC394x2wpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzXfEC3FB3aW2ZCDmYBBOYIxjzkAhtR7hN_nbJBxzv0mEpD-bMHEDwKhG5sQEFzgnLZHeyecFFNwSCmFCfUdTsQpviE6Cm_Ve9zZF2Mtw27dqoukEhSCXR5irSvZVSnROjytsJAay05vRk7T5sdx30dBBvmQ6YzKZXc0BgleDTvsyZZhKxHRdzGyfJMU2Tx_-jZoAmKjL9FIYtIXqUAQOjQa-GE4MvLfzR7bDuuZSgHHDlU9chYs6navaQk5M2jnXxcWorISclA-91qWaCElPy5OAxwbQy2hBB1hTtoBceo0Br0F5qlOpPcufOlLinhmuAq6iH11lzKdRAi3PQmMpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJN4bg7pf6ctrcFqdIuYqOfSjZynVjT9qjbLh0XFH5g2FYQNufZj2LdzK_nPoNB3jvD4nsSA7idoWOoAqcukwj81ElXGHeY0SZtzmP_ALw8gcWudg9nnU8dpxVB-4IdKBAlQDf6nUgnFQBMoYNeDYKKGvMMGk_RJ-gTkTawHWXWQIHTmZHG5SCYHlKaoDkZ31URyd3iaCnn_h8-Bmd7ESfzMcIfevXH66mgyEmt2ZG7Nxj0gkNSgnngJ8zLNK0DVUP7NOnGJ8kbieR6VHIGfhitG7CE99YnMPL9nzz8_WReQFK23b_1g38wLN1T3A7P_PkrW-LEP7qAUp1-DBtVhaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xlh5p49ml4T9Na-sCShpaoA7LkOkdyicM7gbv8TbXXuUHiPTuiBcsj-CbShrc7-VFiPjjNwTQSEd6JuA0in-Iyu4QLX67NMtWMBGSdL5OarUTs-1pGuAwuo_1BNx3Pf7g6iWpUfqdIfKOvEK648t6H851pF6D1hNFoURsbwj3iZyfqPim5WWrQvsxpIWKY-O_kRlbIVqIwxZbxZ-Mk_cdJrlJAxK5TWtN_gaUkl0MMUG2WFRkflvlFInUNgSMAszPEYo2KqTbzJFMdBGBF2h6gVhb2dNNYfp2shHMNZLV-SMnT8Q6FOnSNzWDWSKZYPDwd17BtWSv6H7jkfzc9vXQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZiLdOkQx10gscMpcUHACSfxM4Lpty1JcPG2kuJSMgPom2dh8eb3zqtQ0oJqjXO2FmWHkvyUxG8yZQIjK6bWAEfOCN6RaWJ4u3Ee09OxHYAZPo3nx0XiDzY5TYaBHWq79gnHUeHTFi2QKLYPuusHs4TlkCcTorFfIkGt0SkLnH9TjuMh3zGE1Hl9Ln7_oTozsb0-a-lBK-zEvK37uqKtVBeNAqTNFXEl15KESJqWgBjY31BGr8zu0d3-kKJKBuZoEz0zhFmsI7PbqjHXcTghulIm5UxZmD1Rje-U78C1hZtbS06kSB7SRrzpoDFJ9v5B8ZqWugpRXErme7rzcCWiaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
طیف جادویی انواع رنگ ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665492" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665491">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f12a6b4bc.mp4?token=beTc1WK69TVQcFrtdmbSX6WNLuzsIKvDYpcclFsvY7uAlYGEMo9aOOqIwz8Lp24a6a5b_tG_tSOST8bPGmIC6qNROp2da--9L0i7yBRxV6ASwOAvgAY-qry38QKzHnP-18jZFcy9eEGsXSCYqyaArgMXO1Xt-oEuIrInIucOEBtd4_p_A0axzJBtm_ZrOSIIDyBGczE85dCvfvUIpauzKwzwZqvlKLUV-Oh3RBoryuLL0PX6QxxJ1C5R464TiH6muL3f0a9Q02HH-n8bi0SBHKCDON3_0fNBRC4iuhG3u3jq2JdsMxZ-CxBVLum8L9L_W38RAT5frERiPvi4C6voCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f12a6b4bc.mp4?token=beTc1WK69TVQcFrtdmbSX6WNLuzsIKvDYpcclFsvY7uAlYGEMo9aOOqIwz8Lp24a6a5b_tG_tSOST8bPGmIC6qNROp2da--9L0i7yBRxV6ASwOAvgAY-qry38QKzHnP-18jZFcy9eEGsXSCYqyaArgMXO1Xt-oEuIrInIucOEBtd4_p_A0axzJBtm_ZrOSIIDyBGczE85dCvfvUIpauzKwzwZqvlKLUV-Oh3RBoryuLL0PX6QxxJ1C5R464TiH6muL3f0a9Q02HH-n8bi0SBHKCDON3_0fNBRC4iuhG3u3jq2JdsMxZ-CxBVLum8L9L_W38RAT5frERiPvi4C6voCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم سنگال به بلژیک توسط اسماعیل سار در دقیقه ۵۱
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/665491" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665490">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/141968195f.mp4?token=mlZHYLePdckZ77g7O7_ihBF33CT8fhFH-arr-ugKe1Mb3pPZiOZHQuGuPW6IzlZRnVjylWfFpHLsZlT1Hbp6ywBAtzfGsHhb8CYwW-YqQ6zXhuyqYAu7zYevzMH2qaBarCvuH6ON2djvn4mloMq-oDzVO3YL0zkUAVYbNVvspN50y5WJ7MD6d9UjMSUlsFGT1l9F9F0Ck__aXT_o4s0Ek0VkQop86CDRf-gN-ky6z8m6sc0rmeJn6WFRBDZiBXI_TdWgGzzoe4p3VvwF79c4ux0sHadQ4v8NUfcWE7PepAL8M09BB8h5-4QcGZwkFBZ5M-7tq1Q7tyPx7HKOPPXGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/141968195f.mp4?token=mlZHYLePdckZ77g7O7_ihBF33CT8fhFH-arr-ugKe1Mb3pPZiOZHQuGuPW6IzlZRnVjylWfFpHLsZlT1Hbp6ywBAtzfGsHhb8CYwW-YqQ6zXhuyqYAu7zYevzMH2qaBarCvuH6ON2djvn4mloMq-oDzVO3YL0zkUAVYbNVvspN50y5WJ7MD6d9UjMSUlsFGT1l9F9F0Ck__aXT_o4s0Ek0VkQop86CDRf-gN-ky6z8m6sc0rmeJn6WFRBDZiBXI_TdWgGzzoe4p3VvwF79c4ux0sHadQ4v8NUfcWE7PepAL8M09BB8h5-4QcGZwkFBZ5M-7tq1Q7tyPx7HKOPPXGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت عبور و مرور از تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/665490" target="_blank">📅 00:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665489">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MD6RbEhG3WUANFXgKDts7639e5jhR9vIg3d6r4zP3VPi1pwykI2WXcumOMWjYkXPKLSr3shb47a4X35dMtGDzrAkrH-uO8HKtMdFAsgjV0GDtTBVCbN9l8FuvFDMg4_MLBA9rTjyHjnMyAYhr8kK-ZBvRw3V2NM7kThprbg84-pYACyljmntg2DH9MhaRtW147s7m09RyJHTe8lzLzfkXBGxe9Cdl0TYJymVwcxe6WXu2a7PZ9kdXq5kM5OcnPCSOI-4oqABIfsmSeEUrvs-cwNjKWqT0EqEUj2BNLCMSJL2m6FdGH_8wSTAXCKhtukGm6nb1mLT1bbGjW2T8UKdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در اربیل در شمال عراق
🔹
منابع خبری از شنیده‌شدن صدای انفجار در اربیل واقع در شمال عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/665489" target="_blank">📅 00:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665488">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در اربیل در شمال عراق
🔹
منابع خبری از شنیده‌شدن صدای انفجار در اربیل واقع در شمال عراق خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/665488" target="_blank">📅 00:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پورجمشیدیان: در برنامه دولت عراق است که یک مراسم استقبال رسمی از پیکر رهبر شهید انقلاب در یکی از فرودگاه‌های بغداد یا نجف انجام شود #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/665487" target="_blank">📅 00:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621185e0cc.mp4?token=p8A4aD6mZFOfhSwGTR-NSU9nb2OffPYBE4CGLEWMD1tkbjFvxwhSEZx7fyqyBDArhqqtxqLAvnWwOMPELIuHpPahuiIERlMtwh-bk8ywazotlrNdTC41ZYnQsW8Oz3Ely9v4PDOvrE5sM66IwS9k_L2A7SWC6jxjQfqkqq4bUoyOGfgdRovIZCObsJhaDxvHdG3QHs0WHqx1kby28-yQRBmajOgehwVS56k9Za4qrChn0dpA2k0f-Z_4Qxqrj1z-Mmj6q_gDC-7Fdp2Kf1DGU_lN5NjXWocVM4X37do9ag4jAwkVl5-ZaR1AGe3ZQjwS2Muu6xLNQIO-f5SGFW6uWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621185e0cc.mp4?token=p8A4aD6mZFOfhSwGTR-NSU9nb2OffPYBE4CGLEWMD1tkbjFvxwhSEZx7fyqyBDArhqqtxqLAvnWwOMPELIuHpPahuiIERlMtwh-bk8ywazotlrNdTC41ZYnQsW8Oz3Ely9v4PDOvrE5sM66IwS9k_L2A7SWC6jxjQfqkqq4bUoyOGfgdRovIZCObsJhaDxvHdG3QHs0WHqx1kby28-yQRBmajOgehwVS56k9Za4qrChn0dpA2k0f-Z_4Qxqrj1z-Mmj6q_gDC-7Fdp2Kf1DGU_lN5NjXWocVM4X37do9ag4jAwkVl5-ZaR1AGe3ZQjwS2Muu6xLNQIO-f5SGFW6uWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش رسانه‌های عبری به تشییع باشکوه و تاریخی امام شهید ایران، سیّد علی حسینی خامنه‌ای؛ ایرانِ پیروز و قوی پیام «باید برخاست» را مخابره می‌کند
کانال ۱۵ اسرائیل:
🔹
مراسم تشییع رهبر ایران، رویدادی عظیم و بزرگ‌ترین تشییع تاریخ این کشور خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/665486" target="_blank">📅 00:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8v_sNjkl1jPEV7CWVjtUXO2t4v_H3eRd-Y05O1JrkZSpWUhjcWxosbkZVI-fEULAFfYD-zDkbmqrlVaaGhCxJAWA295pDqI2OtfMDwhiQkLuJhbImQ2ExifwgdDcE5O4-Qr8PjdaSKuOfn84nXCHsQhqVDHizncfe8BfBXOkhWQP7_IC4EOXnguMNFJ2omrAUGSBsSjArXq2yaZqssc5Xzva1sS91qK8xXjB_huiRz5oWuBNuBHC987Ojj2y15ZpkqTW5wfKRSqk_7s8T0PxCwVP40jdbYtI1VqyC4WusCPkg9GOysEONi71SSwHYakdkyixM5QqvOo99dxHoAfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه راه حضور در مصلای تهران برای مراسم وداع با پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/665485" target="_blank">📅 00:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: طرفین توافق کردند که مذاکرات را در دوره آینده ادامه دهند، بر این اساس که زمان نشست بعدی در اسرع وقت پس از پایان مراسم تشییع پیکر آیت‌الله خامنه‌ای تعیین خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665484" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31a770eab7.mp4?token=adGeUAsgqUmYki1awdpH18pTGp8aOPIPzBpT3uYSGYe4XIlJmD8p_jlQLVywaa49XI31U8mjKgUNkEna-YfJjAJu-1dR6wgVqJ0ozyWZkqCQYs6Te_eiGGCUBLKJzla5K-jT4Quj7vYyeLhk7IorQNsjKl0EnDGFFoJlZSzJL07xYSpIIXnOZRT4wZ6K1XawweNfVRTTxa_th2QTTLYSxvv2dUgy3P8H3RdM4b5DXc99nguklsOZzd0RbBUr1NICMkeHEdGRZD5xBRVETu8aZZtWCoOAZ1oTXTlGxHjT6AgWb7xIaefSV3g2YyYD7AvujHsbLdpv-ghIt4lpZaK_4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31a770eab7.mp4?token=adGeUAsgqUmYki1awdpH18pTGp8aOPIPzBpT3uYSGYe4XIlJmD8p_jlQLVywaa49XI31U8mjKgUNkEna-YfJjAJu-1dR6wgVqJ0ozyWZkqCQYs6Te_eiGGCUBLKJzla5K-jT4Quj7vYyeLhk7IorQNsjKl0EnDGFFoJlZSzJL07xYSpIIXnOZRT4wZ6K1XawweNfVRTTxa_th2QTTLYSxvv2dUgy3P8H3RdM4b5DXc99nguklsOZzd0RbBUr1NICMkeHEdGRZD5xBRVETu8aZZtWCoOAZ1oTXTlGxHjT6AgWb7xIaefSV3g2YyYD7AvujHsbLdpv-ghIt4lpZaK_4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترکیب رنگ جذاب در کابینت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/665483" target="_blank">📅 00:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
ترامپ: کشتی‌ها به اعدادی از تنگه هرمز خارج می‌شوند که تا به حال کسی ندیده است و ما رکوردهایی را ثبت می‌کنیم و قیمت نفت در حال کاهش است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/665482" target="_blank">📅 00:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بغض و گریه سحر امامی هنگام یاد کردن از رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/665481" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665480">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-jngHLCdbjAnq0tI_AkiCpNiq2-J_114jwROQc1KMJrjn9ZGlygYs6ANLn31WoMkWByeShGc9W0OQX53FckaoYcDm9P5Lp3GQ-MQHbut1D5WOXwfxz1STl6GPl6V3Sbuki8-KxY2DSH-0z2mzZuNv8RoY8q9dvLMF6kkzn3MBmBCs6hYQ9soA356sVlVagPkL-336lF2eqIj75O0-fAPgChYs3D9ClHx7YT40CzXC596EU5eQYJA_5EUPXxcQgS9Tve2mo9wKgksSRbgiicwRjx_Qrrlf7hw5CzOO2jpPH2eLnTiAk2oecfcJPBOeJRzONoHIgv66UmDQ3u7muECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/665480" target="_blank">📅 00:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665479">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
پورجمشیدیان: ستادی در بالاترین سطح ممکن در دولت عراق تحت نظارت نخست‌وزیر این کشور به همراه عزیزانی که از ایران رفته‌اند برنامه‌ریزی می‌کنند که پیکر رهبر شهید انقلاب و خانواده عزیزشان ۱۷ تیرماه هم در کربلا و نجف طواف و هم تشییع شود #بدرقه_یار
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/665479" target="_blank">📅 00:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665478">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پورجمشیدیان، دبیر ستاد ملی تشییع وداع با قائد شهید امت اسلامی:  ۱۲۰ نماینده مجلس عراق با ارسال نامه‌ای، خواستار تشییع پیکر رهبر شهید در عراق شدند  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/665478" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf6b1a1d85.mp4?token=kWuKVezmfuChMX2cazo9GKDsLE4-K9x-0oaGmiGAxe92Qw3y3E937JvOV7YtUYItgp-RWyeN8lA-GAic6o6QRNB4aBC3ivxDrXWTkWr9qFHCD6Ihm2ehAuVXuhG-gA6KIeVyXX3i-Nis3WjOvE4BW6ZBy9-L4FRsAfU5nCtqLo471ZWq_m1D_g1fYI4WZU_4r_txkMDEPJ05uIcSYGVGtTKVCwDvTdDMgEBJpTfFHyWSBHLlpnJ-2vDef7zt4yBLO39Mup67g5rOVw67S03FVSvt_c6JzEyg5BZrLrv75sb5TntshqeNSEyJPE-yTeOOMd7V3xrxeZeMMRMAq_TC-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf6b1a1d85.mp4?token=kWuKVezmfuChMX2cazo9GKDsLE4-K9x-0oaGmiGAxe92Qw3y3E937JvOV7YtUYItgp-RWyeN8lA-GAic6o6QRNB4aBC3ivxDrXWTkWr9qFHCD6Ihm2ehAuVXuhG-gA6KIeVyXX3i-Nis3WjOvE4BW6ZBy9-L4FRsAfU5nCtqLo471ZWq_m1D_g1fYI4WZU_4r_txkMDEPJ05uIcSYGVGtTKVCwDvTdDMgEBJpTfFHyWSBHLlpnJ-2vDef7zt4yBLO39Mup67g5rOVw67S03FVSvt_c6JzEyg5BZrLrv75sb5TntshqeNSEyJPE-yTeOOMd7V3xrxeZeMMRMAq_TC-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیارا بلژیک را غافلگیر کرد؛گل اول سنگال
🇧🇪
0️⃣
🏆
1️⃣
🇸🇳
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/665477" target="_blank">📅 23:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665476">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
پورجمشیدیان، دبیر ستاد ملی تشییع وداع با قائد شهید امت اسلامی:  ۱۲۰ نماینده مجلس عراق با ارسال نامه‌ای، خواستار تشییع پیکر رهبر شهید در عراق شدند  #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/665476" target="_blank">📅 23:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665475">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
الجزیره: نیروهای مسلح ایران همچنان توانایی‌های نظامی قابل‌ توجهی دارند
🔹
با وجود مقیاس عظیم بمباران ایران، این کشور همچنان توانایی‌های نظامی قابل‌توجهی در اختیار دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/665475" target="_blank">📅 23:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665474">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4ca9e801c.mp4?token=alx-RrY962_dHLfRtO3OD2xwljpm4bPrRERNg6dyfHd86rhxdIyzsPiBXCDTg2ZWBFYXl7jbcW1nJzIQ_5AMXKj57HBL2K-oy7sx-9wTlBHix3fTY3G_zjq5pp8Qnl4QTN6dakuMhBzKaTSLH-iBS-JFcfqnAfT3B7HPU73JQpCK7QSITxtuqD36s5KdFcRFCjFIfQeHC3KJhBRaP8dI06S32KcQ_y_2VpTmsojtqbdIecxGtIcB1d-4iN1TwrEYJM4iRJWaKDZML1C7cG-xQtTohrbuFDwysdyLgNZ0_9IFG3axwd3hZT0ib2ZrhgJN4j9DJxCjv-k2UztVdKP8cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4ca9e801c.mp4?token=alx-RrY962_dHLfRtO3OD2xwljpm4bPrRERNg6dyfHd86rhxdIyzsPiBXCDTg2ZWBFYXl7jbcW1nJzIQ_5AMXKj57HBL2K-oy7sx-9wTlBHix3fTY3G_zjq5pp8Qnl4QTN6dakuMhBzKaTSLH-iBS-JFcfqnAfT3B7HPU73JQpCK7QSITxtuqD36s5KdFcRFCjFIfQeHC3KJhBRaP8dI06S32KcQ_y_2VpTmsojtqbdIecxGtIcB1d-4iN1TwrEYJM4iRJWaKDZML1C7cG-xQtTohrbuFDwysdyLgNZ0_9IFG3axwd3hZT0ib2ZrhgJN4j9DJxCjv-k2UztVdKP8cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه دیدنی و کم نظیر از شیرجه غازهای دریایی برای صید ماهی در نیوفاندلند کانادا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/665474" target="_blank">📅 23:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665473">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cec50432a5.mp4?token=DZusJWyTr6N1jOxUUi4Q8v37t0YCH0-8IAsssqv5m8fSpbUA251UNaA0TGY3mnTdtwniyZbOwQEblN0NTGRWC0zwYbkQ3HGZp-OhWzFuus_rO21jsoOh29s-kFbU1wjD7NfpO-hQX7bxdPC4evo2go_6zVB2ZRTYqBFIkWefX3H22hTk8LIMXVd5RzNEHaXzsXumnrYCLvAv9Pa4-3xZailG8RdlPm6kaOOlV0PxST_DL_G087vQiTCQ_90QNY8LdbzeyxzpvEFNClM1B0So_6yM-bPnSAhcTCodKAUQ-DOJjE1FbTJb0Yb6eultKSKwAmaI1UAFSl1W69UmqVFWJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cec50432a5.mp4?token=DZusJWyTr6N1jOxUUi4Q8v37t0YCH0-8IAsssqv5m8fSpbUA251UNaA0TGY3mnTdtwniyZbOwQEblN0NTGRWC0zwYbkQ3HGZp-OhWzFuus_rO21jsoOh29s-kFbU1wjD7NfpO-hQX7bxdPC4evo2go_6zVB2ZRTYqBFIkWefX3H22hTk8LIMXVd5RzNEHaXzsXumnrYCLvAv9Pa4-3xZailG8RdlPm6kaOOlV0PxST_DL_G087vQiTCQ_90QNY8LdbzeyxzpvEFNClM1B0So_6yM-bPnSAhcTCodKAUQ-DOJjE1FbTJb0Yb6eultKSKwAmaI1UAFSl1W69UmqVFWJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش شبکه آی۲۴: سیا و موساد در طرح استفاده از نیروهای کرد به عنوان بخشی از تلاش گسترده‌ علیه ایران نقش داشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/665473" target="_blank">📅 23:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665472">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290dd844e9.mp4?token=RT3u-4QTjKSFXBnGk7sCFnYgZE8sHFW5XB60EUyX3jw3Jl3N4TSIMM1w8lri0Sk0dV-2Iwh2SOeT9F-w_JVqyw_4fK82bIdVX9LACpZg7h1lAhDyFhl7XSovGLLbsA5OoQGec6rcYX3m9IRJPtv-mQGxzlVN-GCD9hk5C17tYiW8az0zvfnG-QqsCYus2DIPyuVOvDY8hYfkCaMJqbm7hns8eTqeTrTV7Mcv_vViyyzSZ4h5K-taMtmFMKijoIg5m9HuW5u3x4hfpE1m8lck07sWB-OTDS2y3Ce9C5Rti5NEkBi2YvDBmPVTo_jzNvI5xwNMh7resH5zXC7ZvZzd5oLMD1JQnYgWiPXNOLbUaUh9vrIlbKJtuKWeSNoWYtmh92fEr08sUomAeXevkP4EPZ-pwEl8yzmk9tVpWYdWjvRxxTbGo9-5KibuJIf5hnObZyGsI4-vWy0bdZtkhVPYURvlUQjAr3enCR23IQG-7Xp7LSsYT2zRU_U6OP8-J9d3iHJm7EhsIuwznNs5YnJmC1QQ6PMiCBEl1Utv58KACYtkdrF-EzvAJMQDRK1rXZM9JqcMrROfW1el3XhbrYSaQzuQso0sQDTpJEF4hFOsC_aHNrtFurRuTlXAeeq9BlE-E68J1DjfDRkOBQtjUY_12NRvMLWqZmSxKt1o9nxJQzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290dd844e9.mp4?token=RT3u-4QTjKSFXBnGk7sCFnYgZE8sHFW5XB60EUyX3jw3Jl3N4TSIMM1w8lri0Sk0dV-2Iwh2SOeT9F-w_JVqyw_4fK82bIdVX9LACpZg7h1lAhDyFhl7XSovGLLbsA5OoQGec6rcYX3m9IRJPtv-mQGxzlVN-GCD9hk5C17tYiW8az0zvfnG-QqsCYus2DIPyuVOvDY8hYfkCaMJqbm7hns8eTqeTrTV7Mcv_vViyyzSZ4h5K-taMtmFMKijoIg5m9HuW5u3x4hfpE1m8lck07sWB-OTDS2y3Ce9C5Rti5NEkBi2YvDBmPVTo_jzNvI5xwNMh7resH5zXC7ZvZzd5oLMD1JQnYgWiPXNOLbUaUh9vrIlbKJtuKWeSNoWYtmh92fEr08sUomAeXevkP4EPZ-pwEl8yzmk9tVpWYdWjvRxxTbGo9-5KibuJIf5hnObZyGsI4-vWy0bdZtkhVPYURvlUQjAr3enCR23IQG-7Xp7LSsYT2zRU_U6OP8-J9d3iHJm7EhsIuwznNs5YnJmC1QQ6PMiCBEl1Utv58KACYtkdrF-EzvAJMQDRK1rXZM9JqcMrROfW1el3XhbrYSaQzuQso0sQDTpJEF4hFOsC_aHNrtFurRuTlXAeeq9BlE-E68J1DjfDRkOBQtjUY_12NRvMLWqZmSxKt1o9nxJQzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پورجمشیدیان، دبیر ستاد ملی تشییع وداع با قائد شهید امت اسلامی:  ۱۲۰ نماینده مجلس عراق با ارسال نامه‌ای، خواستار تشییع پیکر رهبر شهید در عراق شدند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/665472" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665471">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سفیر آمریکا برای اجاره زمین فلسطینی جهت احداث سفارت در قدس، تنها یک دلار پرداخت
🔹
رسانه‌های عبری گزارش دادند که مایک هاکابی، سفیر آمریکا در اراضی اشغالی، در ازای اجاره زمینی در شهر قدس به مدت ۹۹ سال جهت ساخت ساختمان سفارت آمریکا، تنها مبلغ یک دلار پرداخت کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/665471" target="_blank">📅 23:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665470">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
اصرار دولتمردان لبنانی به تداوم مذاکرات سازشکارانه با اسرائیل
🔹
نواف سلام،  نخست‌وزیر لبنان گفته لبنان همچنان به‌دنبال  یک چارچوب توجیهی و مقدماتی برای مذاکرات است که مسیر گفت‌وگوها را مشخص می‌کند و هدف آن رسیدن به یک توافق نهایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/665470" target="_blank">📅 23:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665469">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYIMc8PeYdJcKFD-SOkgTBve65asEJuWCOygh6bM512cBG9qysPvVzA_gdcq6aZ--2GeKLsacYvBWDWcx_tFllmVsd-daMmkaPHO0pRzvTH_8OpiPK7TkkxpWPL4n7ZPIk-e2u_qEKMw5jVoM-jN46hOOSPhJVDS-p2xEpcUOWvDqiYn9RLzs_ZhkVRrOXHu96AimFZQJ8GptTFRic4XRQTW0CL13E2_UaSbFqlJPOx8_QvWHPsCzKb3AHH99b5tLc8qwPoHFRIUKAAvb9XUf4vtfo0_c1narjOyI6mJmE7FJinQP_rka4rU4xL7MLM-dpi0WGGZxg3j-sdZtl6LsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ۸۰٪ تخفیف خرید حضوری با اسنپ‌پی در ۴ قسط
!
🛍️
💥
🏊‍♀️
از استخر و باشگاه‌
🛍️
تا فروشگاه‌های متنوع
💆‍♀️
کلینیک‌های زیبایی، سالن آرایشی و…
با خرید حضوری اسنپ‌پی می‌تونی برای کلی برنامه‌ی حال‌خوب‌کنِ تابستونی
"تا ۸۰٪ تخفیف"
بگیری و هزینه‌ش رو
۴قسطه
پرداخت کنی؛ هم به‌صرفه‌ست، هم پرداختش آسونه.
😎
💙
✅
انتخاب از بین
۱۰,۰۰۰ فروشگاه معتبر
📱
پرداخت راحت، تنها
با اسکن یک بارکد
📍
مسیریابی آسان
تا نزدیک‌ترین شعبه
فرصت محدوده، از تخفیف‌های داغ جا نمونی:
🔥
👇
https://l.snpy.ir/8kk7y
https://l.snpy.ir/8kk7y
https://l.snpy.ir/8kk7y</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/665469" target="_blank">📅 23:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665468">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5929c3039.mp4?token=E2pEBVd1-AssPAxCKt5KAJ3aVUHj583gtdElbZbmKvIh0l6oIBOj8kY3dzTwMiOHJhLounNQFhAipgINATtaN3bnxhTjLRXDjT-EGR-cPo8mvb6ChI_a4V3MKwIp5nIVm-Tp3x17jz9aa626G7YgJPa8Rolia1qnNhkRtsRovhh1A2bzNwceb56pkdo8ry_KorwwgEJulTYbvSzYjtYHNOsbnOvkd5bUopkOtZXwWc3z54v9ZV8RKJEfK8rZZ5ExObgLp8efHKYc9g6YAPKtxt0XDKsB5LoCCuyO9eY3noGNsUrPMiUHVlNZIgxbeoUcSLrN_s_1oRYY4oQv639h8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5929c3039.mp4?token=E2pEBVd1-AssPAxCKt5KAJ3aVUHj583gtdElbZbmKvIh0l6oIBOj8kY3dzTwMiOHJhLounNQFhAipgINATtaN3bnxhTjLRXDjT-EGR-cPo8mvb6ChI_a4V3MKwIp5nIVm-Tp3x17jz9aa626G7YgJPa8Rolia1qnNhkRtsRovhh1A2bzNwceb56pkdo8ry_KorwwgEJulTYbvSzYjtYHNOsbnOvkd5bUopkOtZXwWc3z54v9ZV8RKJEfK8rZZ5ExObgLp8efHKYc9g6YAPKtxt0XDKsB5LoCCuyO9eY3noGNsUrPMiUHVlNZIgxbeoUcSLrN_s_1oRYY4oQv639h8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
🔹
چین در تلاش برای تصاحب آبراه پاناماست.
🔹
ما اجازه نمی‌دهیم این اتفاق بیافتد. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665468" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665467">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f4e163cf.mp4?token=gPnrTGDQ8E0W_sQwNwqssiGBRQyp7T6ZKlXnP81ub5pKlM_ZZbyUQ2-voC3IFTUGuIqFtGhcOvgLmqlmjWLOUIsexjMLtsNj0G8XRH8140qvQ63lzRR2DTDelUR01_rCymwpz5A36bqHwPJIKNg8ng6YMtwPbKR9xS2RTXrGQohdGjoNEKuAHxrHl_tECPWLDj37S6sNFq5exkOGJiWTI8UlKEC70ocEWr0DBWezbjGoIp1IrcjkvFC0DqDuvw9KqsBXmMOaxIyV6qWnpsCLPaFaY5ncNPzPB1ooI4DZbJWK1TGLR-f_VN2S2yeVDDu3eeWDgMNCWmsb_K45qb9BBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f4e163cf.mp4?token=gPnrTGDQ8E0W_sQwNwqssiGBRQyp7T6ZKlXnP81ub5pKlM_ZZbyUQ2-voC3IFTUGuIqFtGhcOvgLmqlmjWLOUIsexjMLtsNj0G8XRH8140qvQ63lzRR2DTDelUR01_rCymwpz5A36bqHwPJIKNg8ng6YMtwPbKR9xS2RTXrGQohdGjoNEKuAHxrHl_tECPWLDj37S6sNFq5exkOGJiWTI8UlKEC70ocEWr0DBWezbjGoIp1IrcjkvFC0DqDuvw9KqsBXmMOaxIyV6qWnpsCLPaFaY5ncNPzPB1ooI4DZbJWK1TGLR-f_VN2S2yeVDDu3eeWDgMNCWmsb_K45qb9BBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری جالب از اسکورت رئیس‌جمهور آمریکا با اسب در داکوتای شمالی
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/665467" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665466">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پیش‌بینی عجیب تحلیلگر مشهور چینی درباره زمان حمله زمینی آمریکا به ایران
اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3226986</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/665466" target="_blank">📅 23:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665462">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H78sN1BNFFAyi8Z7r3W3IWjF3znU__nhfKXXWQiOnYnEuD4ZzanpnOiDrbx9ix9dsV-RqEPuzSq5QXe57ynoQfdt47zSPjCLUb1ZSeLXVnSsu91bAlFgleYIs0Yw8uPzPpOfGWzBo65v3CQztr5LdrTWEWWdJX3z8rRgHEaXXHJSfAJo9ZuK0LHznV-oF1nLHiGcs1XXreVZLUty8PnnwrRQRLie180vsuJmtOAiFmTRyRO121g54IZVEzpxYVAk6b20BTKjqjGBpE0Bk_-Jgh1U8ggK_3RHrEkeXYyK2GWS6m6G-ZP361lVmpdl4D1sLbkop3_38hD1EyAkAMf28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLWeXFeXi_ucxSrl6GjT7i2JGYwpgpSbbmBRJhH6gE7l0PHwU35ssGd8D0JvazkEHdJPHv_ce46p9pZjRuS1ZDodosSm5LcAS22z-GBiTxDtGwfxoYtaKdjJ1BY9iWMhdaypCDxF38_4iADDKvxgn96gvLuPBrahNR7GN53j3EjXKoIbaCVj7eTM_AzSmWTC2bqCq-sqNX6j3StFbhyGVKkEgd9FJ8vB5xmoEaJn2VlcsI1cg47NYh0Btp4GcJ5-VwvJjFIMeYuANpo7YdGGfY_nfxsFgQnM11Rz_1mt0qtD63xK4rdBplXajKSOrptyTQqmnzguqHGSMEMPb6r_2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532830d055.mp4?token=ZFVIAAzgobi28CDXzGXBRWP-_X7WoJkt9SF3W1Ol1HxnZS0SUuwdasuyueB_E_tVhEJA62wcOqD0f16lOdGl-qvwtRWw7a_4aadk4_lelUhHl3D_SV-z7ZQ2tZTr7ndP1a3y2dj7G3CzuQFVkrKkKb5M3rkW9HwNjzNPgUYCtJwLoKW_y5riggcQlu9t8A_05v1wAl0BEUfz6iM1ht4sm4ZSYErMk9BV9P-_uDfQQD9uIXlMUGZgkg9st5cLiYu9X6zXqQgIq_RpRG_WeH8Wb_8ViBpwLuVu_KgfUOBdqXegLXa8SnWIDzbjNcF6dieuDtCuWWqzpWz1RQrSHNN8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532830d055.mp4?token=ZFVIAAzgobi28CDXzGXBRWP-_X7WoJkt9SF3W1Ol1HxnZS0SUuwdasuyueB_E_tVhEJA62wcOqD0f16lOdGl-qvwtRWw7a_4aadk4_lelUhHl3D_SV-z7ZQ2tZTr7ndP1a3y2dj7G3CzuQFVkrKkKb5M3rkW9HwNjzNPgUYCtJwLoKW_y5riggcQlu9t8A_05v1wAl0BEUfz6iM1ht4sm4ZSYErMk9BV9P-_uDfQQD9uIXlMUGZgkg9st5cLiYu9X6zXqQgIq_RpRG_WeH8Wb_8ViBpwLuVu_KgfUOBdqXegLXa8SnWIDzbjNcF6dieuDtCuWWqzpWz1RQrSHNN8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بالا رفتن از آنتن برج امپایر استیت نیویورک برای خواستگاری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/665462" target="_blank">📅 23:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665461">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
گروه کشتیرانی فرانسه: بازگشت به شرایط عادی در تنگه هرمز ماه‌ها طول می‌کشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/665461" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665460">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
این چند اتفاق سرنوشت ایران و منطقه را مشخص می کند/ شبه کودتا در عراق مقدمه «سونامی» است؟
👇
khabarfoori.com/fa/tiny/news-3227179
🔹
حجاب خاص دیپلمات ایرانی در ژنو
👇
khabarfoori.com/fa/tiny/news-3227227
🔹
تحلیلگر مشهور چینی: آمریکا در بازه زمانی آذر تا اسفند به ایران‌ حمله زمینی خواهد کرد
👇
khabarfoori.com/fa/tiny/news-3226986
🔹
۳ سناریوی دلار، طلا و سکه تا پایان امسال؛ طلای ۲۲ میلیون تومانی در دسترس است
👇
khabarfoori.com/fa/tiny/news-3227159
🔹
شوک به فوتبال ایتالیا | مدافع تیم ملی به فحشای کودکان متهم شد
👇
khabarfoori.com/fa/tiny/news-3227174
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/665460" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665459">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b4075f2b.mp4?token=qnzrAZayXNwACWhWRFyT40YHCWz0hJkPk0bX3katAsp51l030LwTHzhO10lRD5CAfVb--C81RHpsw5h0kwGIQEpucA4vBi6aVZj1YZR8zLUK8FLqolL5XW3wRfou3jwk0NHKAT9UzHd9YBLs3nSkn9AcfKBS4KD3-jfIweLWD0ybeEZS7b6N3EXI58RYylme6o3GlE-lMf6gzbNQgL_3YFQ5BM2BLOtCLZ-UGro_JHqKJ0TbS-f3rNVceAYQw3-u4I0RFqVY4_xov3n4er67DHHOMY5xU7ReVdh6HEFNWnsft02xqFGN9XTztwwAiC9D7t8sDZnKa86mWta5EGWEDBYPBQIPL57WbAYBUCpmpEhgQ6V4nW-SfgZ4MOQ1F8XRXyJgQR8xY_CqS9WFgq6Mpf8MFtfs_77aZQSNvF14RkLxISWd0Xq4_Z_VY_38g_mMHzLZevzMI9pryeBYFcHgQaUJemkyM6m0NURLnN-h-9dOA4mAz84RW_oypqQLiTMEMwgNzGnVtdFJ9KabNVpsBdkVATDDLr7XCuCEUOHTiCAkAZWzvrAGeoWFHi_INQ7vpofniTUfqABUyU6ul0Qzgc8j2dT8M33TgAl51WWv3knxTB6BGhS90kRO_MI-Mpiw11oKzuyGxoBchC-gHGa_OL4ElRsir0hKMZNBrdnLWUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b4075f2b.mp4?token=qnzrAZayXNwACWhWRFyT40YHCWz0hJkPk0bX3katAsp51l030LwTHzhO10lRD5CAfVb--C81RHpsw5h0kwGIQEpucA4vBi6aVZj1YZR8zLUK8FLqolL5XW3wRfou3jwk0NHKAT9UzHd9YBLs3nSkn9AcfKBS4KD3-jfIweLWD0ybeEZS7b6N3EXI58RYylme6o3GlE-lMf6gzbNQgL_3YFQ5BM2BLOtCLZ-UGro_JHqKJ0TbS-f3rNVceAYQw3-u4I0RFqVY4_xov3n4er67DHHOMY5xU7ReVdh6HEFNWnsft02xqFGN9XTztwwAiC9D7t8sDZnKa86mWta5EGWEDBYPBQIPL57WbAYBUCpmpEhgQ6V4nW-SfgZ4MOQ1F8XRXyJgQR8xY_CqS9WFgq6Mpf8MFtfs_77aZQSNvF14RkLxISWd0Xq4_Z_VY_38g_mMHzLZevzMI9pryeBYFcHgQaUJemkyM6m0NURLnN-h-9dOA4mAz84RW_oypqQLiTMEMwgNzGnVtdFJ9KabNVpsBdkVATDDLr7XCuCEUOHTiCAkAZWzvrAGeoWFHi_INQ7vpofniTUfqABUyU6ul0Qzgc8j2dT8M33TgAl51WWv3knxTB6BGhS90kRO_MI-Mpiw11oKzuyGxoBchC-gHGa_OL4ElRsir0hKMZNBrdnLWUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
🔹
چین در تلاش برای تصاحب آبراه پاناماست.
🔹
ما اجازه نمی‌دهیم این اتفاق بیافتد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/665459" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665458">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRiO1cfjll_6QvftZWuPNiMETgIsBjfGlyWW1x7fYGArE0B0ubyqaSrhQV_IfEzESYADagql4nA4rW6FMwoc2S9r7wUEw3XXVws1827rPXMJSunyiPXIN3yqnvigxJoU4VyL4kTGOSmajWbrAZZo_zjuYFXeBY37a6dx783G1KSeQ8iJ9dMDPSdM-GxX2OlXu6_HMSYwPoXRelps3YjzrEIPtTFKfHtEC3HkrrwSlgcI-FzIqJj9yXpUL1BPjsedDH2W5NxOPtqhxQ2m_cyFJ5xgRwck06IkHkefv1dkXRetCDODFO4Iu8oIR1hM4jxqlBUjZaCQSgs0J0SuItZVgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگه استرس و اضطراب شدیدی داشتین، این خوراکی‌ها رو بخورین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/665458" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665457">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
سخنان مهدی رسولی: ما از خون‌خواهی رهبر شهید انقلاب کوتاه نمی‌آییم و از ترامپ حتما انتقام می‌گیریم
🔹
باید به گونه‌ای انتقام بگیریم که دیگر کسی جرات نکند رهبر ما را ترور کند
#WillPayThePrice
#تقاص_خواهید_داد
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/665457" target="_blank">📅 23:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665456">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24616fdcb5.mp4?token=qTtaCrPJAe37FOsMpxqIuDsSo1c5ze055ZKo6pIjggf0h9pYdl4nMFQzQbCOxnufzE0ycx-uocJDkiLvolH-JhKLb4q34HMG8zGsAqQBgwrEXG0RSPOr5_Rnz1a0_q6FbGfxBkPFW-ctfAb4CoUB9MdCwbO4q7auvW2B13JShHcroa_Kf3aHQpfWiJ4OAZ5otRwwwYDV7iYMc9Urk9ziJs4hpN9jmLyzErxFETl1mZnrKo2FdHSzHHERS72-ZHpKHptSdJTAF8S60jUvtgNx2R4tuwwco9qN86ccBrWtwrIFoR35Lqib7glFrlJ36KT-dB06lfea025Cs6i2WRW3Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24616fdcb5.mp4?token=qTtaCrPJAe37FOsMpxqIuDsSo1c5ze055ZKo6pIjggf0h9pYdl4nMFQzQbCOxnufzE0ycx-uocJDkiLvolH-JhKLb4q34HMG8zGsAqQBgwrEXG0RSPOr5_Rnz1a0_q6FbGfxBkPFW-ctfAb4CoUB9MdCwbO4q7auvW2B13JShHcroa_Kf3aHQpfWiJ4OAZ5otRwwwYDV7iYMc9Urk9ziJs4hpN9jmLyzErxFETl1mZnrKo2FdHSzHHERS72-ZHpKHptSdJTAF8S60jUvtgNx2R4tuwwco9qN86ccBrWtwrIFoR35Lqib7glFrlJ36KT-dB06lfea025Cs6i2WRW3Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ امتیازی بیشتر از دسترسی‌هایی که شورای عالی امنیت ملی تعیین کرده، نمی‌دهیم
🔹
طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔹
در حال حاضر، آن‌ها فقط در دو مورد حق دسترسی دارند؛ یکی نیروگاه بوشهر و دیگری…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/665456" target="_blank">📅 23:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665455">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b2636460.mp4?token=Qw051YzZf1UarDsqzsyI_KISOWwxU0d1-HbQee204VFcPyy9BccZu4r5epgAOyh5frsiIRuKBFinEbpOkG_fEnKkDs_GusHGK2G_1auK0QhzWytuwQ0gmGueUhP7XXDb5Wxk1V-x8K-Nt9BGCfy_mzMOLEVAP3b26GFQKF1odHxAT37XM0lkc4YZVpR5nerDHlYSS4TRKgqPDGS99z8czLkSj1WsoxTb1LQdVFnEtwY6rnYf6ZS_jlfLkrGnilPN30-asqO3fAf-B7jvUx-Ejpe6hHLE8K7KiwMJ7sfRVjk03k5Xgxz8o-CdGBcw3xrcvMB5gZhlnHc5CG45Ap7tKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b2636460.mp4?token=Qw051YzZf1UarDsqzsyI_KISOWwxU0d1-HbQee204VFcPyy9BccZu4r5epgAOyh5frsiIRuKBFinEbpOkG_fEnKkDs_GusHGK2G_1auK0QhzWytuwQ0gmGueUhP7XXDb5Wxk1V-x8K-Nt9BGCfy_mzMOLEVAP3b26GFQKF1odHxAT37XM0lkc4YZVpR5nerDHlYSS4TRKgqPDGS99z8czLkSj1WsoxTb1LQdVFnEtwY6rnYf6ZS_jlfLkrGnilPN30-asqO3fAf-B7jvUx-Ejpe6hHLE8K7KiwMJ7sfRVjk03k5Xgxz8o-CdGBcw3xrcvMB5gZhlnHc5CG45Ap7tKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: روز بعد از امضا توافق در سوئیس، اسرائیل ۳۰۰ بمباران در لبنان انجام می‌دهد که ۲۰۰ نفر شهید می‌شوند/این در حالی است که تاکید ما آتش‌بس در تمام جبهه مقاومت بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/665455" target="_blank">📅 23:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665454">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند  رئیس هیأت مذاکره‌کننده:
🔹
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/665454" target="_blank">📅 23:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665453">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCDCFxjvq6MWuBN2nwByoQtwW74bJy0BdvlkLIlw26Yh1AkdOhhKfoknErc3DIfOmi51Dmcc0GjEcDbXmv3-xUs3vzD1vMJ8xnfAOStev7PlVrxQ630_0Mu8Hij8xwU_X1PB4Ddgb94MxfZO0v79t5vukQEDBs7w-qxFAdasxgWSwaKN9785bnlTwp1BfO4gqt-yxI-DEhLAF0frhkRGc4hPPSnx1e8mXdKdUc1uoImt-xI6uyt6Y547EsCfLX7Y4inUDo9L7_2F6BYV0kCY-R60VjFJA9WwtuUIuV0kaS8R08ahnWghHJa_vSVymCMz-Gm-4gqXmcSp28T_D4WqwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری | کمپین «جامانده»
🔹
اگر به هر دلیل امکان حضور در مراسم تشییع را ندارید و میخواهید در این مراسم حضور داشته باشید، یک فایل صوتی حداکثر ۱۵ ثانیه‌ای برای خبرفوری ارسال کنید تا یک همراهِ قلبی به نیابت از شما در مراسم شرکت کند.
🔹
در پیام صوتی، فقط نام خود، نام شهر محل سکونت و جمله‌ای کوتاه درباره همراهی و ادای احترام خود را بیان کنید.
🔹
منتخبی از پیام‌های صوتی ارسالی با عنوان «جامانده» در خبرفوری منتشر خواهد شد.
#بدرقه_یار
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/665453" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665452">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=E1vPtFbUHn8mphWg2cJcuD0nb5vOBmfnxexxc8aL5OvAOmC0M1Eewv3HZn-qZPLFNgmy9FwXzx9-VZ8YMC9mitMaTdMrAPg6K6l02twW0x-i9LXFHwObL7xQhM0mNMyS4F4vTuLujoABPgZIopJgqozI9x0gvQd-ee_HM0lQvLgot-0f2LMTZFiMhzj3cmxWHxdod4RILwZNnSHV6Om45PMp3cvSZhH0d27x2ug1aC_hdU1eXBR8CKPlixYQA7ChLHyPOpZdd4hMnGK9bl6vUs0OMD2CR_MhL8Y7RhuaAabgXGSXiR4JMKOkbdBvVW0CEhQTC2wgKckdHyVD9h60FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62044a23ee.mp4?token=E1vPtFbUHn8mphWg2cJcuD0nb5vOBmfnxexxc8aL5OvAOmC0M1Eewv3HZn-qZPLFNgmy9FwXzx9-VZ8YMC9mitMaTdMrAPg6K6l02twW0x-i9LXFHwObL7xQhM0mNMyS4F4vTuLujoABPgZIopJgqozI9x0gvQd-ee_HM0lQvLgot-0f2LMTZFiMhzj3cmxWHxdod4RILwZNnSHV6Om45PMp3cvSZhH0d27x2ug1aC_hdU1eXBR8CKPlixYQA7ChLHyPOpZdd4hMnGK9bl6vUs0OMD2CR_MhL8Y7RhuaAabgXGSXiR4JMKOkbdBvVW0CEhQTC2wgKckdHyVD9h60FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیر ستاد اسکان شهرداری تهران در برنامه پرچمدار: در تمام بوستان‌های تهران برای اسکان زائران مراسم تشییع رهبر شهید، امکانات مهیا می‌شود
🔹
هلال‌احمر قرار است در فضاهای باز شهر تهران مثل پارک‌ها، برای ۲ میلیون نفر چادر بزند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/665452" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665451">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
قالیباف: اگر به سوئیس نمی رفتم و برخی شروط محقق نمی‌شد آیا نمی‌گفتند قالیباف شروط چه شد؟ / کسانی هستند که نه در دیپلماسی به کشور کمک می‌کنند و نه در جنگ  اما من ایستاده‌ام تا هم بجنگم و هم دیپلماسی را انجام دهم/ بیشتر از این آزار ندهید و حرف‌های ترامپ را…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/665451" target="_blank">📅 23:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665450">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55053dff1a.mp4?token=A7eM8HgsqfqFEk-GDkOsgmuWhNlW_huiLE7PI1eek73NrC_OZirL3NdOlph1gwUYGzb5c8O_tKD5kl1f8r-vi18-Kvo0n5PCh-q9M66rmhFz2lsXYKCOjRyf_7_EUT1HU8UbRtfPdRaw8Sj5J6Dpj72xjZ8GuROl3G8Uac-VrjCzlta4r2TOKmTtAMBUEZDeNsl9P831GrR0gI4-MavKE_v0fxHEQzekPmVm0nEcFjG7hO3w0yxSxSXJVyZ6B4qePGRAiV5ASWDKCDuR7Pa0ZR4cp16h5T4mtEbvMzyjcVwKy8F9YJDZT9dmRHOE1aSBCEw7mRYoHfOOGKsUIB2d6jshYqeN_z9NavkvD08w127-CwuEb__I5qqfQpKgCueurpORLar-5_cwdnTDSAPG69fE5d_jiaKrCFdDNi5ZFfZugcRPiuAou4VTLvWlfcdwTPAXOwqRHOX-AQbSo5ralMRbaHEdRUPg4N-mBBkVTwUvT06SaXDn9a1Vijpj4FjXyDAsPH-OOlkpxz9GQXiJxhqF4PFyL-bErrtIpFyG5PDFPpVxnQ8IN3i5TJuASc2pwPeRjYXKqVrSIGaoJfCUIfBtIrV1btJpAsH3Dj5eqJqdPigbiuEDuEvfH9ZlR4NHM2QJCdKq5b4At5JrAT8wyY6gd41huobKdx8w2j3gF3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55053dff1a.mp4?token=A7eM8HgsqfqFEk-GDkOsgmuWhNlW_huiLE7PI1eek73NrC_OZirL3NdOlph1gwUYGzb5c8O_tKD5kl1f8r-vi18-Kvo0n5PCh-q9M66rmhFz2lsXYKCOjRyf_7_EUT1HU8UbRtfPdRaw8Sj5J6Dpj72xjZ8GuROl3G8Uac-VrjCzlta4r2TOKmTtAMBUEZDeNsl9P831GrR0gI4-MavKE_v0fxHEQzekPmVm0nEcFjG7hO3w0yxSxSXJVyZ6B4qePGRAiV5ASWDKCDuR7Pa0ZR4cp16h5T4mtEbvMzyjcVwKy8F9YJDZT9dmRHOE1aSBCEw7mRYoHfOOGKsUIB2d6jshYqeN_z9NavkvD08w127-CwuEb__I5qqfQpKgCueurpORLar-5_cwdnTDSAPG69fE5d_jiaKrCFdDNi5ZFfZugcRPiuAou4VTLvWlfcdwTPAXOwqRHOX-AQbSo5ralMRbaHEdRUPg4N-mBBkVTwUvT06SaXDn9a1Vijpj4FjXyDAsPH-OOlkpxz9GQXiJxhqF4PFyL-bErrtIpFyG5PDFPpVxnQ8IN3i5TJuASc2pwPeRjYXKqVrSIGaoJfCUIfBtIrV1btJpAsH3Dj5eqJqdPigbiuEDuEvfH9ZlR4NHM2QJCdKq5b4At5JrAT8wyY6gd41huobKdx8w2j3gF3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: در خصوص دسترسی و بازرسی آژانس به چیزی که از قبل متعهد شدیم، هنوز به همان پایبندیم اتفاق جدیدی رخ نداده
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/665450" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665449">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3306a1a6.mp4?token=r_tnRO9FcbvidymTA4wuPsAfFVuse8rksFddwiu74O6yz95Y-dqWCM7KcfpIAevSHI5wrF0dLik_f6Rzv2HkgQvO1XoiMGcNKThtdkOHZSlac2KyyriHSMpWE8FMDfEDqoiHtYKQZ2G-QF_LrD54Dze-pOZcoCn6raUx8vvnnrkZtXfl-gk8t98VSOf8SmL0Qkqo7g3bbmb-ytn0Bm5Wag7Ji09UE8vivgYcec2GGelpEULHwhVAFtDzks5MhJ1OuooJqA_qx42GXcmLLYq5dGfd78uMBnDVEzTyb00RUQc_AptGgXqM_IbYsnTlR3GGAQVQ3kaDpxWrisTDKnS3q1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3306a1a6.mp4?token=r_tnRO9FcbvidymTA4wuPsAfFVuse8rksFddwiu74O6yz95Y-dqWCM7KcfpIAevSHI5wrF0dLik_f6Rzv2HkgQvO1XoiMGcNKThtdkOHZSlac2KyyriHSMpWE8FMDfEDqoiHtYKQZ2G-QF_LrD54Dze-pOZcoCn6raUx8vvnnrkZtXfl-gk8t98VSOf8SmL0Qkqo7g3bbmb-ytn0Bm5Wag7Ji09UE8vivgYcec2GGelpEULHwhVAFtDzks5MhJ1OuooJqA_qx42GXcmLLYq5dGfd78uMBnDVEzTyb00RUQc_AptGgXqM_IbYsnTlR3GGAQVQ3kaDpxWrisTDKnS3q1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: ما به مذاکرات اسلام‌آباد رفتیم در حالی که اسرائیل اعلام کرد از حملاتش عقب نشینی نخواهد کرد/ از همان روز ۱۰۰۰ شهید در لبنان داشته‌ایم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/665449" target="_blank">📅 23:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665448">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
قالیباف: بحث دسترسی و بازرسی آژانس که این روزها مطرح شده کذب است
🔹
به هیچ عنوان دسترسی در سایت‌هایی که بمباران شده نمی‌دهیم، این قانون است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/665448" target="_blank">📅 23:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665447">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
قالیباف: اگر ضعیف باشیم، ذلیل می‌شویم؛ این زیبنده ایران ما نیست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665447" target="_blank">📅 22:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665446">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
قالیباف در گفتگوی تلویزیونی: بعضی نه در جنگ کمک می‌کنند نه در دیپلماسی؛ مردم را اذیت نکنید؛ با شعار، خونخواهی امام شهید محقق نمی‌شود این دشمن فقط زبان قدرت می‌فهمد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/665446" target="_blank">📅 22:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
قالیباف در گفتگوی تلویزیونی: بعضی نه در جنگ کمک می‌کنند نه در دیپلماسی؛ مردم را اذیت نکنید؛ با شعار، خونخواهی امام شهید محقق نمی‌شود این دشمن فقط زبان قدرت می‌فهمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/665445" target="_blank">📅 22:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
همه مسیرهای نفوذ و خرابکاری مسدود است/ حضور نمایندگان بیش از ۱۰۰ کشور در تشییع رهبر شهید  حجت‌الاسلام نیک‌بین، نماینده مجلس شورای اسلامی، در ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری:
🔹
تشییع رهبر شهید یک رفراندوم است. پیام اصلی هر کسی که در این تشییع…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/665444" target="_blank">📅 22:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a3d1da36.mp4?token=o6HsCmgHavcKbot2tSxVTl2P88DfOgVLwbzgDSP9d2eZZvWJEuv8Vi1TkCAZ12LoFRW0O8lsA0XTvcjGY4qQWSROnmuO_XWaKqZNsT_inA9GZ8BiQIdAYfUFxknzxlPDzy1VSzE7x0325KMGqJy_BMp4VZDtM0qNlrkYTHh4E2VEOFaIMg5F5UTIRFK00PWcQgdu_3UESomw_dW8ip4s5Lz8KxsMQQl63MOXWX4FwXZQ65_17TmhWOjmIJ4zly06aT8X6CVVijTWbX4c45FCnVBHLIuv8NGjAp7M3oo_FMu2bZn8BKKkZp60iNMPZtb97Z1jZcoz0qEbGK1k49a1og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a3d1da36.mp4?token=o6HsCmgHavcKbot2tSxVTl2P88DfOgVLwbzgDSP9d2eZZvWJEuv8Vi1TkCAZ12LoFRW0O8lsA0XTvcjGY4qQWSROnmuO_XWaKqZNsT_inA9GZ8BiQIdAYfUFxknzxlPDzy1VSzE7x0325KMGqJy_BMp4VZDtM0qNlrkYTHh4E2VEOFaIMg5F5UTIRFK00PWcQgdu_3UESomw_dW8ip4s5Lz8KxsMQQl63MOXWX4FwXZQ65_17TmhWOjmIJ4zly06aT8X6CVVijTWbX4c45FCnVBHLIuv8NGjAp7M3oo_FMu2bZn8BKKkZp60iNMPZtb97Z1jZcoz0qEbGK1k49a1og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار جبهه مقاومت: حمله به دکل مخابراتی در سیریک قابل تسری در کشور است/ از حمله به دکل شروع می‌شود و به پایتخت می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/665443" target="_blank">📅 22:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0YUHxsO3f2pz_dKZ6y9ywkH2_MUeA3xCTzlBRdkZXCKqTiruL3lcxyJUdxXHqvzXxWg44zbm4dFPndztCHWzNb5YKyKk-m9Trl8DD5TD-eVPFz0-baiW2mFU5txcGjGSITK2XLlQxAtHDFkCh5OUAyNtollrxZ7kwafPgwd0GCi_4rbPbAQls8i0H-OixveC0Zys_s9Ej2xqt0ZtuvqyHiEMpzEAwdnVcTw9zZnevd8pH6M2KAh8_lzd9ZGEH9ZSQ6Vyka4yNSXF7EwMF2Vk1CStBZlOMLIhLn6En_HW0AM6we425c6yp78wimIjZd2XknLnKTzk0sLacFjKM6Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدون تخفیف
🔹
صحبت‌های محمدباقر قالیباف در صداوسیما که به صورت ناقص پخش شد، واکنش‌های زیادی را در پی داشت. نکته قابل تامل صحبت‌های وی، رفع تحریم‌های نفتی و فروش آن است که نشان می‌دهدنفت حالا مثل قبل با تخفیف فروخته نمی‌شود. قالیباف گفت که از روزی که محاصره دریایی برداشته شده، بیش از ۴۰ میلیون بشکه نفت صادر کردیم. طبق اعلام صداوسیما، ادامه صحبت‌های رییس هیئت مذاکره کننده، امشب پخش خواهد شد.
🔹
هفتصدوهشتادوهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/665442" target="_blank">📅 22:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e96685e8d.mp4?token=HnHFeYEH0wMOHpQyc0vhgyuc17z_aseIuqCaqbvCCU9NBwxKylTbI2wHylG-xAP_wXIXkLdlWHyThlrdXEsbv7LhN72jmz7T6uM1dnuDMkE5-7Yqd-wT4Tg36Fa0I3STNV1CQkq-W6sYFzeRJeAodZvjHO1Eah4AzIkSn4GmAjCO_v-W2d9XvonBU3uqQ9odNsknbw3CYISagxfNE9FTsYvNgxEV7A7KGWAmrzPlhbawND_fHddYUPeVrofwqvUQL9uzyVkV9UT4wJ21PGEPh55oy4xMdBdetvfROLVun0qZI1qMcd1KfpHGhNhLmv7KsxtpKXTM7CGHeK97Ofp_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e96685e8d.mp4?token=HnHFeYEH0wMOHpQyc0vhgyuc17z_aseIuqCaqbvCCU9NBwxKylTbI2wHylG-xAP_wXIXkLdlWHyThlrdXEsbv7LhN72jmz7T6uM1dnuDMkE5-7Yqd-wT4Tg36Fa0I3STNV1CQkq-W6sYFzeRJeAodZvjHO1Eah4AzIkSn4GmAjCO_v-W2d9XvonBU3uqQ9odNsknbw3CYISagxfNE9FTsYvNgxEV7A7KGWAmrzPlhbawND_fHddYUPeVrofwqvUQL9uzyVkV9UT4wJ21PGEPh55oy4xMdBdetvfROLVun0qZI1qMcd1KfpHGhNhLmv7KsxtpKXTM7CGHeK97Ofp_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همه مسیرهای نفوذ و خرابکاری مسدود است/ حضور نمایندگان بیش از ۱۰۰ کشور در تشییع رهبر شهید
حجت‌الاسلام نیک‌بین، نماینده مجلس شورای اسلامی، در ستاد رسانه‌ای تشییع رهبر شهید در هلدینگ خبرفوری:
🔹
تشییع رهبر شهید یک رفراندوم است. پیام اصلی هر کسی که در این تشییع جنازه حضور پیدا می‌کند، مبارزه است. ما ایرانی‌تر از این آدم در ایران نداشتیم
🔹
خیلی‌ها می‌گفتند که مسئولان در جنگ فرار می‌کنند، اما من جایی ندیدم که کسی از مسئولان چنین کاری کند. این‌ها همه نتیجه رهبری شهید خامنه‌ای است.
🔹
پیش‌بینی می‌شود در تهران بالغ بر ۲۰ و در مشهد ۱۵ میلیون نفر در این رویداد حضور یابند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/665441" target="_blank">📅 22:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
افشای ارسال محموله مشکوک اطلاعاتی اسرائیل به سومالی
🔹
منابع راهبردی منطقه‌ای به شبکه المیادین خبر دادند که یک محموله مشکوک با اهداف جاسوسی و نظامی از مبدأ اسرائیل به سومالی ارسال شده است.
🔹
این محموله به وزن ۱۰۰۰ کیلوگرم در تاریخ ۲۱ ژوئن از تل‌آویو و از مسیر نایروبی وارد موگادیشو شده است.
🔹
اطلاعات تأیید شده حاکی از آن است که محموله مذکور، یک سامانه ارتباطی پیشرفته با اهداف اطلاعاتی-نظامی است.
🔹
این محموله به‌ظاهر تحت نام «دفتر سازمان ملل متحد» ارسال و توسط دفتر این سازمان در موگادیشو دریافت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/665440" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5abcf2028.mp4?token=iw2KmYXNy83e1xxDZAggqEwbSVg28k9BrtdWsdcVPyb0OGeB-hzAArrtOKCtMeUNw5aKqB02_8LvB5q7x4yAHpULRpDpkSSpJl7jP-q_bbHtnp7KM7hp7YfiCD7UuWaBVsMBuHk0LldmUVzm1BwGj73F7RabCStw2WOdeO1LDgztIz3gsjNC0odo5WH9hVFpTWcScymDTHQ5e3N4BATRC_A2mco4ycrgTt5Y8Ymla4KASQH0hQbMTtWSNg44iqg9nmOfBbdtQwh6kj3p6GMnD1vH9_yhAKkOG1dX__h4blnMItvhzXCg7uQcIKWXoq7D6ydUsNVZ48587hpWqxf1wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5abcf2028.mp4?token=iw2KmYXNy83e1xxDZAggqEwbSVg28k9BrtdWsdcVPyb0OGeB-hzAArrtOKCtMeUNw5aKqB02_8LvB5q7x4yAHpULRpDpkSSpJl7jP-q_bbHtnp7KM7hp7YfiCD7UuWaBVsMBuHk0LldmUVzm1BwGj73F7RabCStw2WOdeO1LDgztIz3gsjNC0odo5WH9hVFpTWcScymDTHQ5e3N4BATRC_A2mco4ycrgTt5Y8Ymla4KASQH0hQbMTtWSNg44iqg9nmOfBbdtQwh6kj3p6GMnD1vH9_yhAKkOG1dX__h4blnMItvhzXCg7uQcIKWXoq7D6ydUsNVZ48587hpWqxf1wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود ملی پوشان فوتبال ایران به فرودگاه
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/665439" target="_blank">📅 22:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665438">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
رویترز: پوتین آموزش محرمانه نیروهای روسی در چین را تایید کرده است
🔹
رویترز بر اساس اسناد و اظهارات دو مقام اروپایی اعلام کرد که آموزش محرمانه نیروهای نظامی روسیه در چین در سال گذشته با تایید مستقیم رئیس‌جمهور روسیه از سوی وزیر دفاع این کشور انجام شده و دست‌کم چهار ژنرال روس و چینی به طور مستقیم در آن مشارکت داشته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/665438" target="_blank">📅 22:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665434">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU758CJ3Uv81P8PqiyAqinwxzZCkFxvp4ocIqI1dip8E0HRPHccKFboTquy9sSq_qsG8xducZkiWPMU-5C7j0cazFiez7mbiDWuVwPg4nnDY9mVy9B0xUEPoY314QM8KCR45zgQYxjRPAXgnrcWq5eeKWj-OyCwqVmRJ2YHyyfEKBlrrMgniwe-nyOxa_Am7P8PWUv14J4ynDMpOh9Y00Ig7tRL4fsBjtp384RKLsiVck-q9nSR40EtC32SXs4k1nhAcPzIQMAJlnbui7e_bzlHIpTbaNDJzoRLpNI9LPPNyRapYVRCOR2kABOMVVruek4eb2f6-fCUuZ1KpkBk0ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEY96akUPEIqlpxkwm2Y7d6_NkX_2izySqlStI1calVlbQBhfR5L6SLKmmFFzg86gOjlzWdgWYoFyAftQxT24xR7guxVtyeebgB8RALGqOldLVHxbzTyScQwvJm6TOhelXYZIVJaDZ2FdrDz68MXea3CvqUhdLrheIQBoVKndAGP7WklkNgULKm_47goj41CoDfCMsDDVaseokH4Vh4NnFPTjgK3Su48tkdWweIpQVdLegYsunAbftub3gjWRA5OeO2Hp1LNi2FodGa9ozCQQOXJCJvPkTc_LhqT1mq-v_3JZrhbUm-r3VlNfu1B-Mumd9r7GI5JkLmoWzIqnjI4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NGNx8pg7WoNBP2eQQc0V7A9PSwLEIYV2YVOm4JmD4bPl89xTTpkCuHVWpFd1yYvj-xKt6fCsHOmb71g_b_8JnTR1NOm_S-OYbZ1vb3Zhepxjv9KVlZBKJyXDpIIiLxSsegsgnBzXal8bjOvFpbkjr-A_MH_WmkMZT26zcs-4HvxHScn0ZsLghJ_E90782OiK8Vf69ZArJW1ju19B-dIwD1ES8UYwsmFfUqmEYM5stg4fzGAusETrYHmtNt9Gq0yhg3Iu8e-deRBpRJ7zifLhcUHiRzpSHsaDGp2IPnZu1Jr9geq5Vpi00w09PIaELwKO2TdXJ_IvTuPkncKAp0WL5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9ncgq2hEjFNWmleEl0leW3J7y4guWEnn7sJaSpst0NoCy5LO5hTnQTdIatEy8cUv00q79m3qy4hBiX4S6PDynqY9XEwtW6tJojGww-gHA3QPlxJzd6mSuAX-MDrzGEOx87qpb6Mg8M5FGxGiQfOTSHXd-k_X-DbD4HoJz5hO9cchyg_3botqVxhHEEqMpBd3J4lZGjX-bQBR6mnwMz4AmQP0-d-vu0b_mbKQ-kBgSg81AhiNjuhNJTlxydsIfagKDPBEctiAlTCgh9MlbNYBX8N8GVRE-1JxzXnyRq4c3SDpamfUhiHW8TmkWXi1CdtKP7zL0Y5H1GGYKMhB1RU9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ساختمان
شمالی بهتره یا جنوبی؟
🔹
سوالی که همیشه موقع انتخاب خونه برامون پیش میاد، اما میدونی تفاوتشون چیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/665434" target="_blank">📅 22:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665433">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آکسیوس: آمریکا به ایران پول نقد نمی‌دهد، طرفین در مورد اولین قسط از دارایی‌های مسدود شده ایران به تفاهم رسیدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/665433" target="_blank">📅 22:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665432">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19424de197.mp4?token=HvaHDverBztjxJHYK7WgqHm2XuE8vwZjQAixXju1sPZk303jaDRW28M4UilbCkm_5EDZxablvKcRHxz82cSXb5dgT2EoGmQ8TddYIFgViftnWldpAdQwmD13rd9KZbWuQdxPpFArfNS274yCl1y-1gQR_q6g8_H_ylC9YsNVf0jAVAdr9KKEW0V4FrqjaIMxliJ7c49UM-O095nuldYV3RIzLx6cNeQ-cA3tuQ2PuM4VgjY3nW0CWgaa4-3NurpWThvbGe56krCqWS1OiMJjpNNJ7Q44cAvXO4672LXsV1V9PTIMPHVVCQVCPbjhNShRv-q49PFgPfVtVsc0IRfEfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19424de197.mp4?token=HvaHDverBztjxJHYK7WgqHm2XuE8vwZjQAixXju1sPZk303jaDRW28M4UilbCkm_5EDZxablvKcRHxz82cSXb5dgT2EoGmQ8TddYIFgViftnWldpAdQwmD13rd9KZbWuQdxPpFArfNS274yCl1y-1gQR_q6g8_H_ylC9YsNVf0jAVAdr9KKEW0V4FrqjaIMxliJ7c49UM-O095nuldYV3RIzLx6cNeQ-cA3tuQ2PuM4VgjY3nW0CWgaa4-3NurpWThvbGe56krCqWS1OiMJjpNNJ7Q44cAvXO4672LXsV1V9PTIMPHVVCQVCPbjhNShRv-q49PFgPfVtVsc0IRfEfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قائم‌پناه، معاون پزشکیان: اگر قرار باشد نظر رهبری هر آنچه که می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد، دیگر مجلس و شعام معنا ندارد
🔹
رهبری نظر می‌دهد و نظرش کارشناسی می‌شود دوباره برمی‌گردد یا می‌پذیرد یا نمی‌پذیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/665432" target="_blank">📅 22:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665431">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: استیضاح وزرای نیرو، کشاورزی و کار به قوت خود باقی است
مهرداد بائوج لاهوتی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
دلایلی مانند جنگ دوازده روزه، حوادث دی‌ماه و جنگ رمضان باعث شد شرایط استیضاح وزرا در مجلس فراهم نشود؛ اما استیضاح وزیر نیرو، وزیر جهادکشاورزی و وزیر تعاون به قوت خود باقی است و پس از بازگشایی مجلس و در نظر گرفتن عملکرد دولت در جنگ رمضان در‌ این‌ باره تصمیم‌گیری خواهد شد.
🔹
دولت از سال گذشته وارد کردن ۶ الی ۷ هزار مگاوات انرژی خورشیدی را آغاز کرده که این اقدام تا حدودی آسیب‌های ناشی از جنگ را جبران کرده است.
🔹
تصور من این است که قطع شدن چند مرحله‌ای برق در سال گذشته، امسال اتفاق نیفتد و در بدبینانه‌ترین حالت همان یک مرحله قطعی را داشته باشیم و با استفاده درست مردم بتوانیم بهتر از سال گذشته از این گرما عبور کنیم.
@TV_Fori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/665431" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665430">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aafaa66f0.mp4?token=SW8-FGmVM04fUK6HBBtN3IuoDXf9TjH1CRDpXJ6Nc-AK06m0tzsr5ZHQfUxq3PK4hdVyC7vX8Xn2N4MECvLZKd9uKKGOFg1hcaIx-zbsy0kB7IZy6Ae15BO9Q7RWhbsydo598MxkmrjlhjgeTcqrWykAj-oCa7crpYz6ppCaiBOSO4w_d1hrSKKyeIx2gGGzNMcgficq_9OEa-HnzgG8dZ6pNlkbUCJYP7DMi6jJkba1s4aLCRqDHwn0BEq-pm_a3d6Chw6HbmPup5zC-ERQD44G7aNcLsEm6iz_6rYclwVxrDUHVleXJqdlorIvR6GYAv_rRLT32bM6vu8RASqTAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aafaa66f0.mp4?token=SW8-FGmVM04fUK6HBBtN3IuoDXf9TjH1CRDpXJ6Nc-AK06m0tzsr5ZHQfUxq3PK4hdVyC7vX8Xn2N4MECvLZKd9uKKGOFg1hcaIx-zbsy0kB7IZy6Ae15BO9Q7RWhbsydo598MxkmrjlhjgeTcqrWykAj-oCa7crpYz6ppCaiBOSO4w_d1hrSKKyeIx2gGGzNMcgficq_9OEa-HnzgG8dZ6pNlkbUCJYP7DMi6jJkba1s4aLCRqDHwn0BEq-pm_a3d6Chw6HbmPup5zC-ERQD44G7aNcLsEm6iz_6rYclwVxrDUHVleXJqdlorIvR6GYAv_rRLT32bM6vu8RASqTAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما با قطع برنامه گزارش قالیباف درباره اجرای بندهای تفاهم، به‌جای فراهم کردن بستر پاسخ‌گویی، مانع آن شد   روزنامه خراسان:
🔹
قالیباف اگر سکوت کند، متهم می‌شود به پنهان‌کاری، اگر بخواهد گزارش دهد، صداوسیما ترمز پخش را می‌کشد. صداوسیما باید روشن بگوید،…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/665430" target="_blank">📅 22:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665429">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6fb81a0d.mp4?token=bATQ2C8RKp5nLG8E7vR3ngnc4gxIKh4ATJ4rt1W4oqekbz4ZjxHW8g8CuiDeX0oEggWhH60HeqFhzxl8O5pOetSCB5lHRqsmfugp4WGr5XqfdvjupLocQGbqmZC5KVfe9zxRJ7WgM-UcOpqPZwjubwc69c5LD7noXp15TOzTUjEdhzSt0yj5RPGWEFqAsRh96rS4eOuyvw3HdYQZEkOihG7S08M76lLX7GpuqidXZf39WtP7IjI2q2A8QoXKB84b5TDGGVI9alan1ZgFSEkrGzeyfK_6-mBiWDImwzmvGwvMou_BO2lpTNvRi_4FlIMed0MjfbFL-QHC0WEQFv4H_EeZV8tquXSZL9amPN2jMGP4V9H0IZ42M-Uw1RkF3dJnx2LMWiFXkuBBF3GbQAyFvy9HT6Gw_zCXWZSqjQ1pRzUS4NrEnMVDc61fl2h1IQKnBYq7pAlY4znY4D5Bj4QD2h3FRc9TX6rBLmvPyql0ymjC5NM5oJrbJfi4nEgVhivGsqplVW_OopYGivtlslQlZWMc03lvE68qH87pCd_olULjhZG15ggIsCxvyx_E0g734IXxv06ixE_53YSw2MEGGqNDpfcTBjL-EVd-toZgIFG4gCGzZjJqYvotPQY4UzgcHHWnv2yxOw9r2djpWpOBrWVDMMhG5Jtz07a252ij5dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6fb81a0d.mp4?token=bATQ2C8RKp5nLG8E7vR3ngnc4gxIKh4ATJ4rt1W4oqekbz4ZjxHW8g8CuiDeX0oEggWhH60HeqFhzxl8O5pOetSCB5lHRqsmfugp4WGr5XqfdvjupLocQGbqmZC5KVfe9zxRJ7WgM-UcOpqPZwjubwc69c5LD7noXp15TOzTUjEdhzSt0yj5RPGWEFqAsRh96rS4eOuyvw3HdYQZEkOihG7S08M76lLX7GpuqidXZf39WtP7IjI2q2A8QoXKB84b5TDGGVI9alan1ZgFSEkrGzeyfK_6-mBiWDImwzmvGwvMou_BO2lpTNvRi_4FlIMed0MjfbFL-QHC0WEQFv4H_EeZV8tquXSZL9amPN2jMGP4V9H0IZ42M-Uw1RkF3dJnx2LMWiFXkuBBF3GbQAyFvy9HT6Gw_zCXWZSqjQ1pRzUS4NrEnMVDc61fl2h1IQKnBYq7pAlY4znY4D5Bj4QD2h3FRc9TX6rBLmvPyql0ymjC5NM5oJrbJfi4nEgVhivGsqplVW_OopYGivtlslQlZWMc03lvE68qH87pCd_olULjhZG15ggIsCxvyx_E0g734IXxv06ixE_53YSw2MEGGqNDpfcTBjL-EVd-toZgIFG4gCGzZjJqYvotPQY4UzgcHHWnv2yxOw9r2djpWpOBrWVDMMhG5Jtz07a252ij5dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت بحرانی بنزین در روسیه
🔹
تاثیرات جنگ به پشت فرمون روس‌ها رسید. قرار بود سوخت اهرم فشار روسیه علیه اوکراین و اروپا باشه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/665429" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665428">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=tPQx2q_rG8h7ZWTPwKvnEGJNLqDzxZkPAOfwX1AS9wTU0nlYZWEY-JVe61y8u5r_pJiwyUsKtq_ERIwpfrgb5saJ2JPrlAfV4cyFUKL7-mQdp1bE95obpxkKZmniyjOlDHZG_CsiZt2BY3dahJvH9a3_f9pQCqq5IhXL4RdSRy6Q1KiOudT3xduHr5hJxzOX2DM6ZV-LVGrOLI6LnckdsjIHeuLJA0AP2SH-YgMxaTtoR8rSH0-i9xKdDV_KJLcRLzZaUPa8eLhQkd2Y3FeKEkdKbiOJLuJsDfQE-JG1iCfSW4an5WWHIk_uq6DymObdmH46JtdHixOJWQwwWgS_pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e623a8c6.mp4?token=tPQx2q_rG8h7ZWTPwKvnEGJNLqDzxZkPAOfwX1AS9wTU0nlYZWEY-JVe61y8u5r_pJiwyUsKtq_ERIwpfrgb5saJ2JPrlAfV4cyFUKL7-mQdp1bE95obpxkKZmniyjOlDHZG_CsiZt2BY3dahJvH9a3_f9pQCqq5IhXL4RdSRy6Q1KiOudT3xduHr5hJxzOX2DM6ZV-LVGrOLI6LnckdsjIHeuLJA0AP2SH-YgMxaTtoR8rSH0-i9xKdDV_KJLcRLzZaUPa8eLhQkd2Y3FeKEkdKbiOJLuJsDfQE-JG1iCfSW4an5WWHIk_uq6DymObdmH46JtdHixOJWQwwWgS_pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، خبرنگار حوزۀ مقاومت: دشمن در تلاش است به دستاوردهایی برسد که هنگام جنگ نتوانسته به آن دست پیدا کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/665428" target="_blank">📅 22:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTxiuTYdKDheWUz32KRYqDNyYMjs_413UUg_ZEEAktqcgLlqdr-1Y5XbH6ZeLw8iTPwwP6LBIeWtzHXptTAW_vyDRKEtwVv8giJJJ9A3C39IF9ImLuSAB6egI_mD2UFqKMrbkBNplSqV2yWZE-_9CcunWRhjNqYRPIeTHBLZj4vkQiyXfQMZdy0QU3t0GGJ3iHxHUHMjksmml8Ae4MeM6v5se3NCfYtrfqyleqxYcP05m96TXJOY4JkWpoo_nT0gZy2fmGWSEnoEx3BgzHQmoFQrr0P5J8F_IUzR2H-gvjk4ZAc0Yhsq1k-0rMzmarNQLSodBBwxTHuZqolL9SP1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpu_i6i1eEXt4VMdstmT_osr350PWfDgiGcMyZQCeSYULxzHlO3znNt16OpJZJSLI-AwXLV5pLeQYz9G68AoJ2imgghw3i9Tc75hPH95ofnnQ6gkozbJplnIWKIMyepBOx6hSBgDxoG06cOcazD5J2vP7c1UIEHnjuLn4Qe5Vd_a_wwsVPb0JYunfQFWb-lK1t8KHDpzn88y4G4hXNojf9ElNH6lv0pcBzfnci0XxcY-b7l6ZXZ12CDNsKY4oYKu8dgI5rpOtOmGexsLSQ3ZYL7zXVk5Exig2cOcUKFKKe7bZLAq0I1uOlrMT9EaCFiFtX5xgFn5jbZaAc0YMblPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byVAzQfvcvuN4nqVaMSx8g3m0LMeN4lLuSxqL6p7D4PX59J8dCduesinu_EfbFY_fpyaeNI18UXsd4V6dEl615Iohi_z4SzqJUoy6ysjvRdWUVO-Ew4RObsqn_zFdzMIAF51ppQLl53RiAZayBeAKoss6z9eLw7HkxuG47IjnY2eK08MaDtewUf7pO3t2_diwF-isfcHiwAnTS6PMDU3xF8xH_Qs-Cs0lWdp1XPu-Fg9mCl5S5BRgW5OXEuQcxvRTYx8tSSGj_6tecIh926azkwhLbAAtAdgHcnbQLqbBkNFTGwAgOY4a-PuXpGFbWzwRtE8bxNT7QocWt35mNjlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtbVhYlYPnDKhbgTURAhkPv0kM9qE0fJRb8zzYVgpPf8z7iJXevkVD38YniWmlwXFfbWSyLTWnrrR6SXTdNawCo27g-Kv6Qj00nkVizah-dYGXnoXBWdQJ_RdJW1CHSU2Cbt-AHaQk2AOb3bbqWZKcIkQdqBgRfZovIT9bciY9X-hD6NK2kAUvDwHr9-EmaA1W0vJoRrH2ukI0y2szOC83pmrFvlFmCkB26jepXEti-sA-L6KIs_JTfITuT3ucW0e5YY0wDb9MwOt4a7fVsTA6bhNN9ShHqlosWO_jljJhXjhYJJwBDuov2MknYeHeZMjNdoXxHs8XlS8I4Xir1h9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نمای زیبا و دل‌انگیز از بازار رشت
😍
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/665424" target="_blank">📅 21:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-665423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پزشکیان: هیچ‌کس نباید این‌گونه سخن بگوید که گویی دولت و نیروهای مسلح دو مجموعه جدا از یکدیگر هستند. این همان روایتی است که دشمنان جمهوری اسلامی ایران دنبال می‌کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/665423" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
