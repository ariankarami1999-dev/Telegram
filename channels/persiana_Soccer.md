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
<img src="https://cdn4.telesco.pe/file/UmLc1GfMjcWwOnQSCLQa3ob9e2yTwFetjC_h4JjTe0SiNpQjsMgDtXe0r7X8QsnrvqO5u2Mn2QFzt4ZIPxwBmB6wLu9YkrUDk1NuDdYOo_lx3pL2sSECjKTcCYdS2bz8fLrhFzlg2wb6DXc4_Rv4Zokkur8yYSab1KwvkPq7oz348quyy5bl-bQMPXdJlkqbfKpSC8rrhB7P-qcPBN7E3pnTk0VDNSMiLNebmjd9Ga4aQ7GMc8MOS8U1BFfihdkm5UcRM4dbgmEl7PCkPfY_GShkI9VmdKpRyQvRVhu6uNMXPpnTbBbVdzwNuMTGNzF5dvK8pNwxVwsPtvmC9hHp4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 629K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 17:19:42</div>
<hr>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=spbmxaiU1X2Ny2waH22WB-N1KTFNOa2ddzmhd5afZ_mjDkfb_7UAVB20OneEEf1lkV3e8n3z9BOXh7JxOgZmKIkBKavTbOgJ_iDwxmcjbBnnrjqQVEc49crFobwx3rYnI-rnpl-ImOpCkoMCxAwlrXgZqxqoK0IntxaqyqLYxc51UjwqPrjkjoBtBOCEDKdjGdcTxfpqZpl8-Ea7Mw1m5sDVrxmah9-vVbpweG2va8ftnOfo1HX4qYHI9NzOAtTpkFM_MW4yriX7h2LstPPCh8gkf9a2qFiLZmNXE9Ro-ge3_uMbH6_Lh_y9o4YDEuJud8pITSggOqAqfNECC4FJQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=pJcMFkVMdxvQsv7jjRkpadJ_lm56GjR7qQIiuC1lD5Rw2AtgXTLvfqSPYRathAd54D3Lpw_y9YkH8dX1_UtHaRvy-YexkXvNHrcga6KJMDO4GVTEzL4464u4VNgeofO9raSG1dmkfP6R23DCTdMVKmFV1DHHwpucfTYjFTLMk4xZCBFlXekx_JuOKRRr9xICSEbHQKh0c3HzCUi0eQjpqUVGOGvpo8BUJiC9HZ--eQhbpw650MCuWUeAa3njvLGJXRSNEKMBsQN-ASPIR_W_xh4ME47xL6zMn7fFxZPN1XUCbK8XHNHfYxz26GTz1suFxF7t4WP8vRefPxct9EcBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub71iKPswRgLY_pqQAnpWF1mflkhQfAMMTwaxcRGo2Ng5c5OUfApefUoJ8Kj5ymojBSskX9ufMRSGhTNRs4zM2XGCCoaIxiuS26aC1BgDYt7d4SSMLHcNMT72J_sye3JPROBZ9_8gU_5MpPoiL-5gHu5foc_WDiE56gaBw_6xNDpHZobpluluHvCLHtMFuYIKG_Kg1zdMXMNTfWarTxP-h9dH8bjl-ePOVU3zv6Hzrml_nunFTbTLcjNBs1ZQwnT_aXUVzyAhGSpDh0gn9TcVkDw_SKlPZoiRada1EkVwLKkDdXaiSTpOeKNktQgr7XA3VJplk79uvllVWnKCI2AbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=tJMs9_a1C74XTqOA17GB10lRolWV-6sQaXzb6dgPSxnwzxHeLn7dtwToeE1zza4SC9_QRGRWkdu7hPcl5tvv3gKm2pt6rhKB6O90_WkYRo7JBedVvKY9n8fBFW1MmobDvj1VWjSoMAoHKR10x5DG5aCrmoJob24pbgHWPicweh8xPhiF8mldaTCLNq9_M6QazZJyBItI_7xINyK2HI3sIJYUzzJsvBvPmy_4aS2Brhj07VDByQamFC3ocJl1pOP_cFrMVzLj3JBba2rh3mXJEFPxYI7v6AVaD7x-07wygC371F6BKv4IDODWwxCaJH9Zj6uUYbGVYcEd-MtVMmDR-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntd67xHqISAR5W5dG0dF_bUYZBjbSpxtrsw6x2qduNwK2hgzj0Tqv4M7euBEHTRXQaV-rG6a99RjIHAQylbiani7fIGSqHgXI8ppN_EoaX4xmIrq_fluY9Sz-MH7B7_IewnkUP2FHIkB7URKePcMkkTiY54yvSOu8ZaKNlAID5kR0Vcsf_YPfWL-_-p85N46yjDW5NpdqMqCu-HFZyVc7t7w8XflhItvEe_XKUgobp6P5HewTvtZ7PyHZBR_OGk25ZmX7UjcUO7xXWa8qTY9Go4HoMMofecTWpGuzoPcReVwNiGCXzaFAL875fHALPY4KNCvoFiRMR2sgZ00Qgkmdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTDN_x3QE3uP_JvF5TFkLLB_EDGieavdvxyAiiUNzkwZRYWXRHGjRpPOXXt_qLs8_IQ3zgky-brhVtANdzf-b8L7pPcB1oZGHxto3-QpDTlmIw5pSHrP69e7mVasqT1zi_ohujOJKubVXNvvNxvEgLgsYnb_MIzA8HEwxMZ-_prg4Ma2xxJR2Yhhn8-MEvXaISn1ljunE8Plg7RHv1rsLkzg6fK7ylENKqcLIyXx_HPAVzEq9pQcamPPv0suS1Qiwy53mjCkZbO_eNxPdxBOL6TMXcEH5v_W9rSYtfAt6trkCcNwI0Vtn8J4Ulyum160n7RhzKHS2JkpauHF5iwMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3q5es5ZJXPzY9caEIVD3wd1NdShJci-46wmrakSzImGF2hLeVYNM7CuohQdGg8ZRr013ukL6yDFJvkFgrQOVoLRz6wp-ba5lGo5xpbIjJ6FeukO7GOCLw5sQcCYwiyxby2SY-y8biayJMUypirmSbzWUdFGoFhPvxbCvz80fsKa2icAh9wgQSDz5yARiefEXL_p2OEq2o6dHP6x3Ebrx5CxMCLO4nev4HIxI4q_ypw5OpGPpkPJJdqT9S3TAO0mnzC79yWxn7N--17Y_rZYc12V2wQSjhXMat_Fzn5iPYxQM7OlJw_OkJXfEVYFk5ecEuoeeHXwzl2U9-nwetPBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/retUssdp_gfhy1ihfY55xqHPDRHRLzKuragYTz6un0tFHl38XQYOQq30ZqpDPzrqw19b79sv67Q9VgUn92AopM_3qfoRAzJDgMgGzeRUxtfk7bqhUPwVLHWmPMOqyZxmQFnGBNVHV27DdjbOCZwVyJ9F4FJUTyvL9rth2xNl2tk_cZ_mXxyP85fCPHPPlcvds4zX796obyFqZPaeosf8U5DPJGw-62eKV5thTGHRLb-XRmdD8RSGluQE3inAbi4BJ_oNHqIM-l2rEslYLyQfU5xHJ3a76GfaoAGLjKApcX4CuB8mOzqjujyJoU05wovyWRaFqkz_3MJ5h1ZKkbzIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d39tCvmdr27z7WLjfXiQOkJGi8rrSlvAu-JmpU_in267MKkDSvnH9stfeOJN3g0ekJJrA5FSBzoOnZuP88U8Z5VG70IkUIvA-MCVxa0R7PTW630ta57ldh1g1mJRS7NkCyamAQP5VddPerTDPq375TVhZA94-cbYso1DqGQMRm2NVV8V8XPoLM5K-oJWWE8YpM4uT4eu_DGSgzNQdt72QIDVDIXr32nmTSGx-YudUDAWvhTakMko9tRnCx5enbmwcsBOXwpxJc8kIMME_AGckdsgKq5OVJJcs3scUiMjQyuZte4Nkecr69vWV68WrYvzMTlTwjYjB0hH3shCqzEnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYTRdXCs3BXfRJb1LPdWxP0KEliF41D-w_dOG95CjOIIymS-NgEpoOesPNa7PgN5PZaZgQ92pPv_VVRb5X_BXI7BK-KjPVQQsoFkkBFCHh-MJmS1GxUcdcQ6vPmr0-i5BvwAbCg1Aivn9sFVOJ83sf_nj2nLrQ6vrFI0v1IxD_oRqzKeSOC9Qr9c84PB4V5HF99wiPlJxYcG7QI3ewYJcUM7rRpHztU1CJN4HjAVyk46-xflrmxDVDFUxuHiFHEGY7bKYjsBiWZC5tnQ-LnIZ39jcEg4-0azeBZw3rMreWWA0uk1iVu3qpiMsfXXOJddrZwsBdgm_fK6yaXuLRVvWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJvdcyCSPugtiPgFv6dr4N-G3hcs7QcHiyeoYlY5edVAcfvCI41c-G5jDLnaemM7fMJVHZ5iBBYl3iZV643wZ0i2O-4Epa3Vmb1d6HB69S5_l99O0810ZuyvSU2MXuI3DSC97dDFLL8oKxZp8mGgu9BED8iO-y3ZznuDau8sSypIdTdq-fRAclbzf1WNV55uueEwiJZmLnllJwPAXtGdO2enwwo0CYfm1ER6p3iF-pnrI26UGN_8JfeaTM0E94KrSPSjVQLR92eLPiVr2tnNKQ0YW2jYv1TnCbTEN-m8b9FgjXcHKV0wcDA-nwsH7SLrAPNc-oi6XAL3VAAwZYvA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fgc-Z9q_aOBXjeeBHJzmOKKhsLkP0WEB1VeDH7C_pWmOXZQwfjm-r9BPAcq6so5MrW7Aycbu_9pGvcNs82CfNFacUEIm2f9pQkopzTYydY_h7vFev9gyRdhyPtk070JCgdhX1z57vwvuMVluTE3tRno_mpKlkQX8ctn6PUYH2tja1zxgDj3ahbQy3EUsQ2ZYkoIR5nxCY3V85DyggXzJXAGIPofxTEzIgskfSUAsJwYjvyAMIolR4-GwmSV8LuYsM2WQwNePsPgxu_4LZPaDTtpwXOyvswB1GUthSKVmjbCMtchUDh7lkSh8Y05VaWmPBwoEdm5sOHZM98DuVFRBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=XrplykliL1HXjaLDUnCNlpIH_D2Eg5VZRMX-hiPakKmu9NEjLcTkGLR0EVfK7RCICswB-lPRP8iKYjhUj6Hk6CRDiTVqwvb0gdIFBb972eJFwTXhIBnlglXfke-krCpnmoqkqJ44J1zKMKj3_36i3CdbyRwVlD_iyMocOogtVMr4st2mgDclCNuWlg7cuCDeSLF35pG-557bc2atZE3rBbvh7iosZZEdYNVSAfp_oQD7V3S52mscKD_rOU75HikAobTcs6_vKHq-3hw4cCyE07kz4JphklFWrhcA69Zvh0RRtmjwzMK0AnGWTLwdA_Ji8mjzuG9t4HtlFTWQPInBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=cbIq-mxaHRHcedyn8yCBQHo5uwW5YnQdgnOyuqEvDMQ2J5p366t0ExVi-Sx2Gi7qrcmOULpiR83eMVwBAvDPJJ9Fm9vJJWX7YE_ZJEEJkwRR6qAK13iVi_-v4k1cFSivHX63WpEXdyqSZUrOprUpU3o2NkLRRiq-E4L9KmNKbVmohXxz-kttWufLhtVrbGQmmrC5vcJ0Y8Qwk0F7n4wfl74HFE4SXl-5YOvjeH2izDA1Az1b5xho8KaWBreefM0GKOGA6-wekPfYSftRf_fUeKaetlHxUoJmb-8sekl7_Vq1rE1mbBZnkm37i3aWl1bhHqDyS3r9TMKrAMmzGK9zFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-ndWL0x6t5fuhsDOdgVWHuv1SPu4wKVe3yKiVgl1JFuhHjSNdiLD5AJiDYekRZqA7QaIf5Y6Mk1y3dQjI_zo90IQ7BCKkL8RA1ZU43iwLiHuOkX6MNBq6G6gXhDnXcHxg3oPPFgBbx1rzoKkuWiU040EJZk-l_j6zSMfbaAIdRyaIfHAqhW6jt3pejFBagLluDJTH3yersQ7ewlR2z9W8DI91B8wMmgeSd_PlgGPekhEW4vbs47vG1FG1z1YjI0BYr2Gn5tspJume8cOJIzWyUdlHrReYfRzEp-p-jZuovxXELxPRywl46z7feqPvBzzkq7pLSMYdvNkmjVlSRvPN1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27088">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKA5Nx577lVIQpa1BqEE68BCWiSYC6cbIs6lUA0Y4jM05x2hDAr3VIHpvFFY5W-AXc2CBi3l-bsCYrPKA04F8uc_8zkxwRtwfjszX4p3fYnQl67aslEmyUet1_R0zl0C_GMbB6CfugYkEcK0-UXP3WDLaTn64QVA74OtusYwp5ez0OrJ0mDIY325GCzQXl6aYnsRUt9NNCaawVo0_3h59Kb9i7iZ2s7-c68TGPwFjNym7eRHmhonMk5dUPx6gPHKwhVYUT5WyWo2fsaEfxAARY4OEUq5dfPkx2zqhrLRxyziuIXM2qZeqqAIg7wbu8gOcTpkoAJZZJnnTHCwgGisUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/27088" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFGPBChoz1tQC4CJ5fGzY0Ax0FnCLMU9zr2OAZA1rM6vjNzc3H1YZvhlrw_ncEFANfnoEYL5R_yuvFak66ekPrU30GkAZqh5XtL8z58-8s63k50-R6JSNZzZeZF5WJp1CDWve55BV6pln5daMO3-C5VtvdJX32jo5fhCaQkB2NAKXBUwYIenhHCfydsNOXJjAFcztZnL1mGzEB-nknqLrrGf-VIOW8ViSySSQJ2SESmfrDGfrT2A8PSaAAWhDNrDZXDhinRp65dFbD7ZJ3gOscIMp8FfMsJeymOa0300cyXUOQvZsCpmuqOdO8Oe-ab1xPYSlY1Hc9rXk8K6xdR70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7kInltQnZitUpPE3rBlOE0CHQQ2mL-DguptyD7ePWVRXIj2TN6fUc8wZZpIDHJaHcuTggICeAcCq5WswGHXghokJpfr4yEBm-mb43osMRTeGpMDicj1G55W_zJpr_vm4xS2Jemx---8ENobTJhh2saxCOd8yPGYUey0f3qd_ByYKD0AVypujkjmUhVdXcPbUteqTLtEoEla3rQy3iZWd403XzB6zFWDw1hWkPDo5G_EcodHyEfhlVvHfc-IcrDid8TnAR1zKLPKhybno0X3M5H21vzjBaaTO6k5Gx6m7hz8iAOLANtfRW7cb4SwApyh7H7l6WvkPTD_YtDtAZqQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz_h5oWkQoJei4d8EFySMhfiRRYiNhFfbtwVoKCLOFu1cETFLQlWynW1MX5SFL1RuoPqNHx4nN5UTrV3tsR2Yd-Lt0VHNjRhu-59LFdQmty8FizZPsVT3ruGDCyAFFxLTmk_dRMGUP1sSLr90fpHxgWB5jRZy5yL8v1AvA2lHd0YSlEuxJbYGi_JbMSvjj_UdU1YuJHLp3cbWVZW7xS9t3J2MH0yH8i3fYu6s-Ga3TKMCcHM9FQp9zOWmhnqHv_TDdaOGo4VXQ09ot_NeUWBBQi8BBi9zgvcwBxDIVWtKaW_Jb0VWGVneip5r5mxlB9RSabgT2L4fhBncnLEhCtxvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMDeZ38zAfyLTVv431OG9uad6kU_Jn3hkgazI8qKd-WwJJM6P4BjXR4IaD8CzWLFmR0nyVzzLs-yhopsjVz1p0UqzVOa_T2ztKEOmrhRI38Yy21b7KJs4DMSx5WOvM0NEmgCfrHn8QHqvYI2CgMsGRKyUzan9TSo07z-tcBTUh7rPVTPx1ZuaKXZFbDKtxSJk6MOuQTeyfmxQrw2rstmzAOCYPYehXpQvJhD6iCM5aIxngxm_s_jB1bzkomxYo5RyFlcEnAVVsT3t9k3OaP90VaqJBGWUwkQq4stfwH_3PLPA8sbY4NqG5TVuEHHAD4haMen0Wbr4S62dcPCbvwaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=fnuhmhj_aiPpibHors_6D4Aj7oIZIHaLuzVA4HvqqvXDYG2SbA4ib_Oeptwspu68NYT2sK73-GOzMkkNlzawajvgE6-dpMENRB0W8Dq5cnGfQjYUZBDDM-q0QoHxhEO8BknXE0DNBWvrHfqiUU4DXO84BpJ1vkTBT7KQh43V23j2uONiPCFD6irKqTQ1SLWVOZprTEbK6bRyL6vdbwbgju_nQ2mPd9Ke1euWjruLNVFD4XdTffHrwxdav1BsgNAc0bcu5mro-gvwsY6X602g8W9fuXkbhwO6nrQem1_lHEZrjl1bF5jY87tBSAODsnTXBG1VdZQRZ8aOxxh2CMPf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa9f2DOZ-cSTeowMn8XFydmodTllQyxIoJph36QsdRmv8Gu1iRMtloao7dwEg3q8F1viH4AYphOGBMeJlCqqugckG1MIaDsRMcAr8Hy8zYQBAcnaj3V1HQ7xscYV9fcHK5TuLaNjZtVFpyEA3-UwDdqEcpQmb1zu1Or5KgMwYV6JptblknPFUOei2I_MwccfXs7k4UZgEeZSQq34aZzk_HNkExANw9X2HNGBAVZKHs84O4LJL2MHE4-mqebt5QfR970ijTAPU3JHBT74qbhmL2lfg9NkQqWsPq-m2K41hin6bz4RoCgRkMHQp_MNZuZYIp3kkTJlin5cTKGLEY496A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0hub9yQ0YJ1yJvtR6-Z9KiAza10A6iNcbxDW0XcADwNbgwe3YAb5eZncnI1ZPiSDWP8w-hUtjY6AZ_I4uyNAYqcGg5QwHjVxeBVCdYNbqkqO9npGnl_O3OlVW3ZpoL8iuYkEwWFk2VzGO7XmaqQ9cyZYnALSsR9cxo-GM5HCXwY2MCyJtdzH30ilNhnA9yWtHGATT-rUddcdrvf5P6FkxDTmhgFYNArePav7PUaRSRpWY1S9i4KhI5TAL3V5E1rxYX2NGw4-GqSENnAk-U0G2TZWZW250sP9t8C0wJlTJsZgv1WvbmHmbsSCEiTy1uiKpx2Wa3tCBT-iH3EQJmXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQ5T--nQO2DTR-6UeFS48C41uPWGu56djFlpnfyDcHu1WpZg0YrKEG9xEWwRSN8f2cIDAkWPbCXq4yFs7ciDO05S9uSyU2b6uaVF3nzhcItvzOWVXqbZ7vN-fjGzoYmMrb8oZ0ZlzgXONBxIW2ZavadQVaN034NDaoRU_QGBlWaKAsrqzR1qxWKDrC7i0Vz-DzFe5y0HQYJ_oFGU8hBM3usBmX365WrXROHgTL7Ay0-ncskxHRuvxa9yrNW2yZsrBr7SUVUEAtTZRVjnCl4UU6h5SVGrOeWplEHjmN4gv5gVa0BEokBHE0eMD4eAE4rX9si-awSyB-Kcf8thfgtXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsqwBc1QWM_j6DJbHuzEpPne8qAW-TfXuzf0GsXwlUiVbhKAgT9LAYaKGwHwrIEjVLmoQjzfEkCaTICooK8NfkIjuwtMNhhBhhYbZFKcntg-xxNYcdu-Pig9_yDmnXuvIKchzoiACW3sbsV8fX8n4qbpuw4qKSCHVxANWKPEg-IOh-a8i7LNiUsu7GAVi_K2qoVdAe44PfgORlwr6tnjQ6rWYUskVE72rKSKFvZV6MAJ0EiJMtMHvXvCGtPTb2n8uS4p3-TkfdOTLwadUEdBvQRJiESwpNOu43-2SZcBOTignbDsGyJl6okrGg-ZK9BYndfEW8vI0B8P5Wnnyjb99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI6Na56tW-jOn7jl1Z_heFEhwrRJU4-bC_GcLje5pYVEgv4cEqNXFxLw5QAFhba2h0ur7cC9MtbPFp5_z35hWn1R1ZujglHqowUfwHW9CMeW5hJzCs0n-iG8DrhT8hrZw8UrG94Hd007JZUnnrgR8zy84SEYTItTm7G-xZRaghzPKqkddcG1f8N8G9t7B7Nzy3cdokQaCxwz0DO4fUjvj1y3ZQr1D9yNNu1OMeTrZd5vLPKSED25mtiDuV2ruHwBHENbtt7IvloavUD53_OxkduoHUiANueIPPCVlh_j5FNmJZZh1M3pdqnbKiwWOCdYxiBoltLzyy_xgRUw6koY8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuijQeHuo-C9qr72MsX-ql7ph0259pMFYrVnyTROvUNeujvZPj7js6xtxxX5bMP4OXlBCcrSTDbSBTaixL8FHu2mMAWSd8oWzJryzjOCAEWq4m0zriJiYmmFA5QTugmCIAWDBFDzfAB-31iy-1XrBQhk-9RYtZx0oCaulKbhj_nCUFk6SaCBf_KokVyYUjFT54lgV8eHmfDZ6dNUQIWxLTacBje2TvXB2v4POJMoFtkzKDdB8eXZKhXRTmzoJ7YmcodQiu6FyZ5iu52R75__KpET739GPVMTtaVfcKczjBOSHtRlscKzCOX7iZ6GsklLx3B7QIU1meVZ_Mr1U4OTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPqpoTI_5z63JolSUxtZwW_BCuvOIGKRo-p8jSJu0TfQyjoNc6BXV-DS24qWqf-DvZeXrmVh8jJUJseVp9_Il0VqSoov2M71kp7DzxMPZyoVha7s3_bXPz6-tz-nPWhqZUH2OqKvfH_Fk3q9SJHwS73m8vsxnOSIWUjBbmhXcwxt7tYv7JynAtM95wnjisFp4CY15SCENkBWklnylJZkv18bkGeNb1XR7v8U481dWWCBf_3WXVcEl3rvK6WPeXba3pKxHWeLo19jRvmDld7-JLQJgeGOuA0EMDZGHL2rphWjSG8DFA0F6r6uLxPHaWpcWh-mHcyC3eBmbH4Y5SGBaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erNI72XVTHua2H7V1QXse6RjWMwv-EkSG7Hpxf1dPT1lbNKPURu902JhKOFwhvll4njT3uMyo_cJOK9gDMh2enDg2vf0g8VweZt_AzAPsswqaAolssu3CBAlPJq75wup8vqp7TnpkDRW1dHCoZiJ3hlNsLhediRCxfsU-wHSLmSgybrpmn37eqjC5Ymk-54l5eQrBTH5HluVc3DI98ehkQ3bJ98H1sgISv2S_rEDd3WJomei7JJFQgdQ_7zVq-ux6LQ18-coi2vCMAXxYabjEG2yt_1WL-0Q7_Oz7jE4DNHyyj8ZFpJVXUMdnvBHWh9FRNQZMET7bwgI2035vPAksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzON-oau3bTMOZWbrU_dK-fjiQnx8yuz7quhNOASTS5_Gu-g5a6G0lLaYBVZaz9iHEoF4tN4CueP1tf-ElsbDZy0gvi-29V4IGADggasQwJPx1dzieGh4GRLE7suil4qe5gwztpeT_lmZ9ekFWpofOXyirOqdnDXm1xSGsghssy349_9B1g7QKbJRytR_v1FF61-UyxUeBUgyK2706CAu5z18cv9eB0KLEk7ipFvOzOFlhzvqWLBMDh8ahGx4e0HHYR0xr8wFAoHrk9ma3uevYvUY4yNpQrtq6j1tNUF0_fca4NVHBlatQYLnxAivGnU58OunAyqaYVvkkcCPuPK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoTAKx3t7eBtnAjm3w9tnES8cZn8YJX4bjp4xDTJ4LdyjEax_8F4-RtypufwS-WZd8jOIgk7PQ1ohx71f7iaC-MA-xhFSzO3bRDlmOA15CJHYKEpxr80Ccgk1cmEdlpi9dO0ErzGPlaX3szQA1bZlep6ytYy6RHkwo9mGgoCOsnJtqLQ1DhchGIlyYc1PTsr-UT9_pZnUAVJVYWBKxWvrOESbgsNTJCmWsC8Km8lAIbytRFTly9Nq49VJ0V5f-rgdgUjosKGk5dCQTS0dZSfKQ62LmWx-2cFKZPiDHBMCvulHrSfrkAtj33kB0w2_3wJSgjW0UIK_o6r130BW8rJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULOflGez0cLn6l479rYSdmkvxbILjq5hepalA7e2oyu-GZRN0fVsjAPOw6GTAVk-Zvz2qGK1Nm-zYooNuz8YtYPRHGRBbTcGI5-3NwMEU10C2eSmd3HQyZcpjUMZQ9MpQ0qJqRjQz7vDLbg5Gwf9SmIyw51gyi-MaCNvKoH3ZAHQUEohgdDl-pkyQkq2S4CEko6wLnKqgxAshwGyS-ughU_d5AgqtVBjknJUmxNKknoHha0YIHA3_M7bR7aXFEIXBAm-gQAXeWcfjPo0bnCFHdqxfBHPrSWoZMFjqvQSKs0A8VMpljysY9ddijadc66m3MyJ6h6UHgHeXCLDavVKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a42Mh6ZuFzjqXC5NWhlHILUbQBzGLB0jdKkQIvTwPhIKuyiYbYzmxfbm9RncSjJbpW54bSgTL7UvwtL0UXFDBFWrcKvCAryuoJdR50ZtzWEaONLwMD2Sjr1YPeUS0d7THBVWGao6I2ir8T5-s8agnvztJRldViFDcnl1WB4k4jZw7WkKVnGF7PRsDR3UBF1XNGt1-85d7zNFr7Y3gBsX2jMuDHGwcBt2AoFOuXLqQdrnGOB1ab2XjyTYWDFtFQlVAdgaUcBkHI4ugnXadnB1TY3qw5GnHZF9RCHmh_Ha-K3D3zCpwpqFdqh9xf4MyPoXXBwp5Z2shinZtTKjtnwi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=gYU_Aw1TXmcUcgFQmxCV1f-3mmeFTSt7KrMETbptNWpHGa7uzyKhYHOdKdf4GCZPIZU6M2bSgvN5e5PRsYoN2RVjLWqKBNiWgrrb1NUipbQ3hrK0Zro5Px0dvGBCfPV_-3_nQNVpEv7g-ZY83Mv1vPPxtLK6GjoPWJIhKTI-N7cTyM9UQELMsiDIME6WMZu42JjzFRRjAGbM7DgYWE3nEw-u5DoGDBc6ywGiz0_1ulz-LRxU1VL9A86TpPhhElp2rtdqV7uxKwoHXcPkwU7sgV1yUHZdhve1Xrx1oLd5TZtJOmVow8eDPQUQKmTZJ9fsJax3IsCDygvF8Lp1L6kAyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=gYU_Aw1TXmcUcgFQmxCV1f-3mmeFTSt7KrMETbptNWpHGa7uzyKhYHOdKdf4GCZPIZU6M2bSgvN5e5PRsYoN2RVjLWqKBNiWgrrb1NUipbQ3hrK0Zro5Px0dvGBCfPV_-3_nQNVpEv7g-ZY83Mv1vPPxtLK6GjoPWJIhKTI-N7cTyM9UQELMsiDIME6WMZu42JjzFRRjAGbM7DgYWE3nEw-u5DoGDBc6ywGiz0_1ulz-LRxU1VL9A86TpPhhElp2rtdqV7uxKwoHXcPkwU7sgV1yUHZdhve1Xrx1oLd5TZtJOmVow8eDPQUQKmTZJ9fsJax3IsCDygvF8Lp1L6kAyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=AzZefiMMcl5y-dT6H7rB5DybOdUeguHLEyrr69hydlwAUzKxC6UmS7_bmQulh__6HR24GO3KlR_Pubvm6WpmQ-m2HONZEHMK_3XazabgkuWYw3c4Vhh3MXO8gowTWzXVkXkK4fCkfkGe_3VVmrYbfRSVOsL2sppQrhUWAkCIn3L0eBPBP9U-ZQKW-rbV7NymLwJCNYvgdN3nRr6p8JjA_kKzl5ULpvNN8gmMtma_vmD441lTiArC3w_vKOvdhpbsF79KNQcd8u8YlNjFkKeNcqdx9ZC9GzPmTfgOKYB0sChRYcMnAYSxD7T5951GJRgHDB8qGOAjfBhCMmUAoek1sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=AzZefiMMcl5y-dT6H7rB5DybOdUeguHLEyrr69hydlwAUzKxC6UmS7_bmQulh__6HR24GO3KlR_Pubvm6WpmQ-m2HONZEHMK_3XazabgkuWYw3c4Vhh3MXO8gowTWzXVkXkK4fCkfkGe_3VVmrYbfRSVOsL2sppQrhUWAkCIn3L0eBPBP9U-ZQKW-rbV7NymLwJCNYvgdN3nRr6p8JjA_kKzl5ULpvNN8gmMtma_vmD441lTiArC3w_vKOvdhpbsF79KNQcd8u8YlNjFkKeNcqdx9ZC9GzPmTfgOKYB0sChRYcMnAYSxD7T5951GJRgHDB8qGOAjfBhCMmUAoek1sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdjTfBxWekLRFgS_j_GgPnm5jEE4HkAW9smSQv5lQ38GhXgksMSk-PuGQQCvw443aUu8N7_-o67FO8t4ove3RHeK75_4SMW5nO5OBwNdvBl7s3jZ73crzTFzzKhvCu3NENOqrgE8iLyhJKNFRAzzgwP9IFpskN3w7KkErBwAlbpxbTy2OQDSxAXb1fOh8-ev_FKGv1kzpjgwtE5P6mw26iYRkGVGeP8bypNf2zKKyZCUBflxpdHATJqIgSQ1D7cCsnmAJHDiwuDy_l7vju9dJkMhwjldbDUDEaoirdP5o2cVi2Cdsb0hO5atIaFyDpGtSy4KY1uDLR-ezcWB5dYHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzqoBdFhR1nvTkz6FGlVy-XW06oQjACZCbomLqV-pLr6mRG5Qbfuqt6rYpbroH7JUMBssg1Oc3Gok9KIWi4gwEI-EjPG4nOGzEmjyEvf1BWmt2kfIUg25fvDrMEHt5rL13Iv3YPgFE2xg4AHDkY1jEFSqu72zAXHN5jDUiEw-Bz1mq6S7JoakwRtUTmHVO3liJZe_-EoYf7AJrP6zDI0dFE7TeCUdIskxdQQbnl7SziKLLlHj0hkvhUYKu6hOwbomWnXOWYxrNsxFeBn_YSUKaESFHdRXlQLnANFl5M6FT6OanSxriOjK0RYMBnJV3VXcn8JzaOLzK_W-PCqp07vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNwxbOY-UlT7oGjEruNbJyXMdkSPc2OkT0_sDsWxzyqTYpfK0bTTWf-tJh5SNwa7FfR_iMTWlz7W76ROuiKlJLXm0eOkPTTvm-p4SZNS5tN5gEjgja_gg_m0uZqR4OWXQ-K7GpBX4s0oGdmArzXdp1yUGFG5Gp2mjW7PvCPLMvThvArwdlzjOs8kYwg9Uq9SwlRmeJmPL2oqBb2XtCvyWorW9sssLv0Fu6uT64Yx7N9Odwm_K8eaPEnsNoTDN-eFYvhh6qgPJeCdJyKLLMVn9YFA5d_pU3KN9kBAwf9dugt9McIKcuamkf6sTk_e9jezDjLqgItt9aLT-Oooh66RDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEXlnbi2ahf17WGy8Y237MXlVjPLZM0UcqGQwY54_oBy3ZHbaj6deyoz7pQk6Jww180yBy1xt5iBFWKxSCN4nAMtpZQkOaR4r4exb7GgkmSyECO_CgwzJUOLEUbUzkIRMjhpTOmkUrop1zFXI7xREzKgmbw2IZ3Cw_KVHD7BudBR6dzfV3Y5zxRyCOKn_7NBKDjyAKMBmabG3YcfSHXcKQnTMR4MHbYDzkDMAq0SEPIp8Y0C5fUxeer_WFs-i-Yszz35Oo-0RZQOSl1BZvnhhqF1lEcvEUcXkCd1f3sBvBPl5OtK9vhMYEjO8QtPo6Mgw0Di5WVS1Tv72gRqqZMR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=XwcROUPlinLrMhQqfWMQ0s-XQ9tbedO9BYvfKJcTKo1YOjNCMYO-jxHr5wbA_SYLsCIL7A93Q7uJWTaRPhopxAAQ21ZLffoQPEAJGM0DP_L4e9FFwbUJY5Um6flljrAp64MYJhp5_CihogVv-tS17Tf3PgS9vMWXlfcAII8WOf-CPV3zGqwZ9wI61EpbTpWwDHcUWnbekl3Ogcz71dZ8LXn0NHEa6696JA_EO5-JafiywEftEk1q0UCUmmshhmdhSRSNFjHzhWjrLWTqEZRb4hiOOjyUw6ywMGfEjaRZqiTsPVKlxIPr_W1eXAWNAX6oOgnaoVsa-XgmwW2398zTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=XwcROUPlinLrMhQqfWMQ0s-XQ9tbedO9BYvfKJcTKo1YOjNCMYO-jxHr5wbA_SYLsCIL7A93Q7uJWTaRPhopxAAQ21ZLffoQPEAJGM0DP_L4e9FFwbUJY5Um6flljrAp64MYJhp5_CihogVv-tS17Tf3PgS9vMWXlfcAII8WOf-CPV3zGqwZ9wI61EpbTpWwDHcUWnbekl3Ogcz71dZ8LXn0NHEa6696JA_EO5-JafiywEftEk1q0UCUmmshhmdhSRSNFjHzhWjrLWTqEZRb4hiOOjyUw6ywMGfEjaRZqiTsPVKlxIPr_W1eXAWNAX6oOgnaoVsa-XgmwW2398zTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llYPRa680KfGxKTOGeUyUHSw7Mj2HQUCrsHzQNTSzfS9UEhx08iNoWbRzxHG6uuC1PUvNIYFO-T8r2c_8vxWR1x_pAdy-b9aQJ1YZbz7q1ahw2TL305DntkrJj8X7p_tzKm-GOIxzpTS-gICXqj6Onq87ALcGVj7uFOjBi7smgEb9SQGEqaI9QC0nZhETvvnkVucRzfDtK4BH4P4im7RuqJiiT8bJS3bsvLlWrYaD9vncb7wqP8V6uYwZhRaAAepxSyi8q5OJ5g_YMPLhYuC3QOi1eTCerToDyBLTRG1GCfGzF2NdLAeZ4jpjqgqTf_5Qjltfv4oUvhvjH1GQ11AYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8SZOmAKJ8reiHHB1Fnj_oFG94lK69nQ5-XHdIp3BnKquIVMkk_89LhFrKal-kIVBsgTyouBDwxMDRY_0STa53z9tlGvW9I8Wv5Icd9fCVraLHcYJibegT3UfG2KYbvNouDQkQNU5lk_Y8NrkJi6zU4ajvPOn6dy-KhfCjGxckwKtpt_QEP2SRR7SHWxDGWoRooXQyv3_-Kd-b_R8l0OGko8TtKlLUu_D0an-u1eGv7el14s31JyPr6oT_10cTT2fix3Xlr6PWhhjPKkcEvZwuo47VxUDrb4vGqyq_WuU9LXTjIhWlnMOj2APnPjCenMyV4wI1PASxCVXSyCWr3N-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpRzg9UuHqgChj74rFw0Wr-BO8nXO1tf9L-CCJjJfaDmv1mezDWerBmglSK7Pc5kDt3Utl0FkjOM_GX4EWCIPNmqUM0i-DSWdQ2O2wPeI1QSRrv-9tdfNcLcE0ERkZQb-W4Y4I72Mc_WMcUdfkUTJim_UojmvfLxOvAQtZBUUVANqIYqqojw4DQ807ccN8mLe5RfEURkoRyXaiIh5aDqi9cFLDaIsSBj2Tz2grMOqOmAO_nrZKszFANtzR-uYqGi-eKaDNBZELxpb6G2btesTyVCpC12TB4X7u6e6kQctdspuB0Jrs43qPGr06a4N-t6VvN8pYAMdi5dkN2vsozrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9qXyEnb7h1sUWdJJnnm4hCnsx6fxfFoSb_puzanjh-kLPfgrTfVzO1ZocrG3aZNM6_U1BqGHAtUYMjfTGtKfV4lXxaiZmPTi1TxVQtHAHa2eJZK55e5nlJh8Dhbj2rVZnmVM8u6BRZIoAQlRhj6VhZD8AWSlxiYz5FweUMAVH5vWiylVlNUMlN6BLHUECAX2kdtPgu4MIypfg1JhsVZgkyFY7y8eB1JCOjKlrVabjYprl2rZIMmhmBvy8E3gK04hRSvqv9rOLBQa2EIOsESUtuULDTWLMAvQmVnTMHU28naFPHshvkpehlPwbVXY6zz0624aN4eL8y6WnG3BoVpOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ4TXZmkWFebpMzpboGtR9Gjs4lqtBcQkvSO3PsTq0OO9374puWIdGKDUhtS6N9e7GemjB2IKbEzHCIH14xOSG_4VKIe77x19f1pAW9HeV5wKzwjZwORokQf16oxk264fqbGxsPw9QQW2gGqpFmp9AyPKC7CVx4FqD_OyiTZR33qAqyOvDsdZwmXvv4xnBx01sD5Md7BEBbDrolHSPL31lzLQPvbyX2B2MN-n22z_j_CQUyGmRR98z6iYHzaj97WakuFGGThhLD7znRoetP0vFHnNEGdOnaq7sHl6s3uyXb32WchHXbKiKdZgG1DJ66wQ0x5xToyYVCMjE8lc5Ivag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObFrx_lOWwrnZxHqc4eRRBTV0_2QJYGO20Z6ZBXnKOJOe6Efy8nJoIeePlI2SJjlIcDs1XKxuMGwIn16KzgTLukB3hdRv2q28qMzLwg8jNXBSBUr-f_lxNpcprN3gPIWFRRfh0Ctj7zi4lrOuvG2IKT5Lml2JzxIGTQKX2D3bsh7_N4Dab1QcOm07_aWoqQOkbgvut5Z5bvYmJ5xR6i4tp37GKSNTpMJpJ4mBmt0jQlHr7GpOZZlHEf7HHuY7CjUOjRtm4Wd-1YbspyoMHJPywPZgFmYYMEeNRUzzEvjJKiI2ai-vZh5OIXK7v2PRfljaqohkWFRlbS7pREE2cvwGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzzGvmPp1D7bhmR-ysyy-SOckGkVdgr7aZrcztWM8Ca3ug4k0VlzrbQN8vQv6GX1gF3OtPuM5lBAdryghoHbH5_qu8ZFeZNkeUrsZ0mSCxIB4aMktGhvgeY_IqOp-hQBXVgyy7KbCemrcsnLdVF3onMjBKhNHUz6P6NFpTMmvzgYjsfr2fejMAuH0SPf2BJhRO6mn86RtnHnG0Tc0HmH15qMlVPmjcdPoIwQhUD0Mf4VbdGp0LhP3jXsEt2P0i5H8F3l56BBHUmQ-YV6Eo-ZwgtcX9ZYP2qa_rxxMVyMhQuLx3NCH1tFdRAWFv0kjoFd0JRYifTB0U8CPb57Ac3OkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=l9Q2AHzhIcUHWUsAHucTUbmwqOstGtKCcpYI97a9PpQyjBDlBTpuzUd47hKTSXG1DSvbcDJ7LLcpiAEkSUsF6sB90krP4mhXGArXEfe8O5jRrz-zElNeVWgasJnlMgmGvUQm_2xHmOFQDsR3aRVK9rz4ZU1rwlnm78GN5pYDpFtxfZX8l-flddM_Xc8_o2B0fG0k-rfkf47S9NT4TlmUTloqJxqFhVsWCnGnTEK_IngI64JZH46joiDdvpgzC9_N8o4oF92TPmHh215PT6in8RLSB0iFwilcc9E3M2hCTrCBFnNM2aJ0kRLastKyXColCpVcllS2k431SNSUAoJ-pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=l9Q2AHzhIcUHWUsAHucTUbmwqOstGtKCcpYI97a9PpQyjBDlBTpuzUd47hKTSXG1DSvbcDJ7LLcpiAEkSUsF6sB90krP4mhXGArXEfe8O5jRrz-zElNeVWgasJnlMgmGvUQm_2xHmOFQDsR3aRVK9rz4ZU1rwlnm78GN5pYDpFtxfZX8l-flddM_Xc8_o2B0fG0k-rfkf47S9NT4TlmUTloqJxqFhVsWCnGnTEK_IngI64JZH46joiDdvpgzC9_N8o4oF92TPmHh215PT6in8RLSB0iFwilcc9E3M2hCTrCBFnNM2aJ0kRLastKyXColCpVcllS2k431SNSUAoJ-pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJJhWO6sbD--rzAjVxhgpTOD2T-N-CH28y-IQoyg3l0z03CaXgtAin9re432HROUba6C-ZVuegIqfDrsBIUt_nunG0Pz7cwQS0yvC1MD__FE2xUYjNuJNPQnqPv0t7ykv2_w6tGT1sWnn51qk_rO2oS_qyVu1CiarbMXhQU5d8JIs_iNUNnUPDHlmFz2NReGdYA-XYsFX267Py7OYIrL18YdmqZVyYSNTJa7ncC6yGYK0Mp9bP_0Ebj_qVc5zyE_0JOuWCiDcBFlzleUKLDkfppAcRKHXOnISKJDvcLzMf63UcotSlnBFRvSfQrjt3r3OJQ_kQpkHi-ZyMP3Ef983g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxOyoCUkFdi5XqO2dk1Ftr7HrnCbK0FNRU8vh-TfdYoTUggxbH8wfOL772VQBRe2ZrB_7yh-t87shY7iSmjuYst7usIPrznGTxF1jWXxKtP8ccqatxSMPRtcKseUbsHIWPgD3-klf7gKPiZswzfVXBC1Ic83LmTDBGvaefyiFzX17KckDO1o8n1ANN77Cb-QBRhV7hIzs3mzMUUtrdnVaOs2rS-RD_PiZ-remaS4D0P0Yrvwkn-d-_vlm2AFL9Rz7Jc2HeY7EfsD-PEirg5aMw9CoHh_grwxKLW8dUl1reHrYSGPVHJILHzA40VCeKeGuQfHlnXGw3UUsLA9zmc5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZpmensesyjeqf4Znx0TbdvkZ1C-1HY07EviDzVOPX4NQ6jen3B3410JRmJimCzUyb33h5RgR_gYjBH-IsqZP_n5MrAwwyrkcQ1sUoUcKIO7gRybb0e7ExxEE2nvHcGbUFvfzQ5KWQzl1UrZ8pQiL5ZwRnCV0OGgqx9wxQOuBsY6_M6iQVTteIQuMEiZQ_OcrwS4yo6AC0iEh7g26nX1_XGQOge01T4uWn0lrVma8SHwh_fXUJuVuxUe8k7YYJ2dP-LV9kmscwnX4gEr-LnNSTed9WZwmM60WVUggh0VDFPK-7laCPmr8kPXwRjM7cbfCGlmrwZhk43BgR56Zm4-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk_jVWoWZYG6bvFSZDq1RKpTiLNhX1HuV0zzmTH7ApYvA_8TUwZ_vnemWDU-nEY04axJQnyb-TzXkpl4CXx-VLssUdH8fL1AkO5Vm9W4aTAC9CJPMr1mXFPjkxPApiGDnOGlyurKzelrQ22_1AAZN2rfp2SrJtw9SOOeP5lnxCVph-fugAOebyPhHTRLFZMPcdGgNtXuiwzd4-ksz4xbvas_KBFQ1yg1KyOeQ9FoG7iwwj0vJXA517Mw4ownNSfb--Zwf5I3LnCD1GeAKBHLr9uUCNc7QW48U1T_LXQLiFb0bviYnWKxVsz45BDpEq8ZBKrJHtd-gih3DG-o3rlAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LHHRMjJf46MfPYWGHMJ9KKSuOw1TblrmAWVih2BJzu9jVdcCkWf70T3q2ZSDiVZXDPmFVbRecjivFVF-Wr-uCYZ4373CKB8gMwg6yCC4MOFOs95bddzdlb1GuKG1KK6GxsuuCGnt7nPWJaHtOcS4sNB2Ko2x4Pjbn1eo_4DgnlN-ZV84WDoorpOR7WPLG3Q84_tN75mPCPZQ6q1p0OE5jKHgi7-LKmZ5krFech9r-UQxzVHmEbMgjX_8GINRCdnN4hx_2XEXfQRkflcjbZLja1O_4S-nkLUB33WFETHK3kK4gsMbc6u2Aiey7xvluRYFwxSDhYPnmm7VNtaXKPhD9E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LHHRMjJf46MfPYWGHMJ9KKSuOw1TblrmAWVih2BJzu9jVdcCkWf70T3q2ZSDiVZXDPmFVbRecjivFVF-Wr-uCYZ4373CKB8gMwg6yCC4MOFOs95bddzdlb1GuKG1KK6GxsuuCGnt7nPWJaHtOcS4sNB2Ko2x4Pjbn1eo_4DgnlN-ZV84WDoorpOR7WPLG3Q84_tN75mPCPZQ6q1p0OE5jKHgi7-LKmZ5krFech9r-UQxzVHmEbMgjX_8GINRCdnN4hx_2XEXfQRkflcjbZLja1O_4S-nkLUB33WFETHK3kK4gsMbc6u2Aiey7xvluRYFwxSDhYPnmm7VNtaXKPhD9E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCBBui21jp1nxhCcCkcnXdiB00tRw2nwzfMzDxdi5qn1j1XriR8Ws6O9PdzWzCYrkPvGHknMY-lwhpkDOLynaPK-Dn-3uRmvgKHdnjFdFIrNVPw_X-ymlb4tv2o_dwWNANoefhVCbJ9t6phmG1XLd6JFjz67pB-QQqQfZ9NRBAzkI-AS3rumHrtnUpDyutDAgN27-a-1QMxdWrZxc_dz_02eUjPut6cvsQDS20AKQdcOw7ZkJH8Tz3KHm3u-t_uBfhbczRPq2xTSR5LJ5gWOt6xGtoifO92KRYGr0Qk7NvdAmEUmElO0Od_uoorX-whALBFykqXYcKoSO-3mSQyOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUkScpofzAA43DW5HoHF_4bQtsAP_Zxpgc8dxrmoBeKTxOgI_72lMnXHiK9rvzl_8mT2soY9T-ZJRGIa4TQl5hLTQEcC5nfbyBqbWEXk6RKda06U_WOrs6llrDZ12KXxRiV_DbsdCsV-VNILsEzl4SPMqAjAt-d5K3NXVJPHTN2bXM6NDlw2FQzNuFBfrOk4OMA5UVvh7dl7HE00VHuvqptFqhTzu5l1hDRIgruSNibI4iHnOxqt6cWQPHPzsaE8hySK-ddaGVQi2C_sKtDuVzFylD9B_bUBE1rLGeJNwhR8BW26FT5SoheCiC_HMApyy_9gCwtv2cqdIRz1OZmeFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Pvl4C-LO43MVOBz7cygHtPo9wmBDxUTaTVAG4-ywaOS-nMe_saMzqE3vB1xSqXKRwEmhsjIAN6m_lUIcPQybZXFnNitkt4f904g94VeodqJ_OcQB-JMJGi9YhjbNhcPl37T0MWPOsDR2h3XlrjJ-jWyWGsxH_ebew5Ppl1-EFhO_Y1RZgIsJWf5yW5AYisq5Ik5MJMVeaLXWtID4vbFOhJX0zp644SaYHSuUYvU3zj-x2YtkGXZ5LB5P6QpgRMxUE6tccXiUFyS5ts7MoRdbTH_52PvULGHHA-_7K0JpVxk4jcCYhCHnTYEbcMBT6ym4wp_hWSvZAK9CV7_V0-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=X00tv6W6XF2XtPaadCPUybRCitd6l7CfC29sV2eRw-6iRHdSeBrTHFzORCPAnLEr01MCzWzKmYV4-G4aHNg6jjEo4QTE5FpVCTyHFps3hGV1gRjzKSjr4pF72JHztESQJwk8q8HqxD4wtcZXeQEFA0CI4vB1R0HBQRfiqfwQOYMnf2mAPYWHmmWdoeAfodqJEObGg7XOAYCafGUZxiXiViWhL3lnLkjGLJJpLJtR1hzjCYM9OFxml_9o0qXBm5wmz0faBaSTzrycaD60G5BIkaYw-hi-hTPGLjcFA9cYKqWOXS_bZWQHYEKYrgx25wJfLII5t6o0CQTnBu6tsoP41Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=X00tv6W6XF2XtPaadCPUybRCitd6l7CfC29sV2eRw-6iRHdSeBrTHFzORCPAnLEr01MCzWzKmYV4-G4aHNg6jjEo4QTE5FpVCTyHFps3hGV1gRjzKSjr4pF72JHztESQJwk8q8HqxD4wtcZXeQEFA0CI4vB1R0HBQRfiqfwQOYMnf2mAPYWHmmWdoeAfodqJEObGg7XOAYCafGUZxiXiViWhL3lnLkjGLJJpLJtR1hzjCYM9OFxml_9o0qXBm5wmz0faBaSTzrycaD60G5BIkaYw-hi-hTPGLjcFA9cYKqWOXS_bZWQHYEKYrgx25wJfLII5t6o0CQTnBu6tsoP41Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8KLeZETDj-aqAdCR-Rp6dtGaNusTnBO9lH3JoMnMV54LEbbhWRUA10ZTGgB6kkBqMo_s_emOe9pMBhqNFmNqjtr_lgWx6cvVdkuh8oZ2C0xFG5vA4bUuluVeplXNjdOp7pYdVAbHZ6sOPbTzz3ucqcXk5lYey531AYaAx_TEumpMvgMOBpF3uYckOxlbkhas0I4twsHQqhBXp3lOTLMQW4YD6GGsC7GBEdKKZN1-c7r6cn8oJ28R0QiwakC0l4hdZYr_uxNym2HeH1M2V0iHqOWB5MxC9I7VB8whHFQmFqRWVsC0DOlfdIUZNDfIj66HBzfGYY1jBybYJQmJn6Bxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ62Mu215Je0cxsdDESfmKtpNyvONMxVs5sGfdfGT3nRlaK43qdKaJJebQbylDrx417l4EeCw6CnZ8cR9LHfq930KsZLoYopRLCbhBESwGlXK62e44CEt05Ih-FB5-TaDzgZnTOfq0Ukx74D4BttLz-ohoflrT0wFmsKVm7gv_vvjWIP5cUQem76iuLNxBR2DEsARI5EerGO5VqF_7oJwv3AgJPiYDSvPCnyaVgkIbECY-neZH5UfbFkUiGDqx5oPRCSAf1G6pCa6w3aXjmMhjUhYZDCniWjheqcrRCFrxQcrNA0FjuaOEb87tOLf7dXH68-WdLwjDDqc87sK9-Ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoIx3lVwybR7hZoHHIZ6tPlDgS2WrZHGrDRR5eMkHT6yJatPyuLaqQZX4RWEiPtm_woMLgZRsD8rbFlF3wgxKv8OV26-RRU6uqSz4Tb7Dv3YUagsNMXG8CijEiqQkVcBwDyhPpiIv-xMSJo-WJiFsg5jKcx_hKuc7YLzOka4kzfynZpJSdc7hRkihEEe6qdKiUJF3z98ehrAQinB-DMWEOOAGhSfeJ2kDyrkh6rsrUTYIPzeKuAQ5UVmvNPKT2joFBS5iljit_BkxKvmUIrQ4C3SLVfVVoJVntWNpR6bP6VPpnUfL1qyPnP6sC71I-Foi3vVOz80LZOGxZoJL3UcAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZoyQV9LAY9TeQ5T0aowT98YtO31tt8SA5OosrRTJCbTx9dh4Bb0wOhjOLC_XZA4_mRWDcCcmCP1AoT0CArtxz0m3ckLsJToltm_ipGQcw4ynlyeJ7CVTbZ4L0lKQuYobvuM4T5_71S9Z-0XAgSCl1cxOUwwO7t_kI1tLFiT0bihEHIiwTHBC9V1WVAlcTv9L_9S7jbXRqDc0CZJrQPsc1DS5hxmhvAFQ0PDYsrF1XeU95Enbx-JSNA27mB1N6ZRmHkJnR5Ri5bnXHJA0ecjJ-klGPO9LvkY4r9Igaqqrvh5ILmxsIXMfKY9svgze6uUak9z4RkakcOfOXZEwLCWOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKBwebqvcIXyvJ4tfye6tbxzyGK4gEtm6Sg_0CAvkq0LL6dxkP2gmi1ZMh-8Dyl4CI_0LsCFPYktr1nB9My-AO1boe3c2NgOeEHU4QYqIojC5M0Y-ABQUwwTMyrI4OlmXxUe6YRecP02Hgmb1ed3UNYKppIevBWzpxc-pn_8UHJQwF2LnrojorWjlKqyqyA4pC9kZuHZb9qtmaSkf1ohtg2RUcwUI1VgoyKHo_hk0TYfLrOhINAExDLGsATInZtiS3SouVVxk2kSvmPQxfn_vAvVmrZTMrv1tc6C9BZiy-hOkxRjxBxsgYzWdYwBDeDhQaA4wfI2mjfOu7gVnGFy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iu8Vj0lFmo_EFCzEN17DeCFXeoAWI82FOEelp6vfqcyoU1gLnzpj7TYj_xjTGNjnSNf-eEsUIXco2ytRlTL93jynC1JmESahiC5YvNzpvjfFGSwT5_5zFDnEyKu5bdsHPZTlMXGI6UEsnxBcbJwXsW_NEDAyKevT2COg_EoEVq5m1xSqprMPw4MLoElMSCNGbMv3j5N7cfMQmpaA8TH45Tfog1LQyCnSDaox1Nb_eOj38k7909Nb51Sa86DYIB4TiRs7oERZHQ4wPIbvQcsp5qC8GneFWAssH_xQMlABQbEUEx5njLMp-P5VFCwpI071wirP5YqvczOxJ3VUFgk-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQgxoJdKZG2kjuUti6VHwVMavxrqpsUtxe5sCwFTUhaz_q95vxaPsXgAaIYW1vhGe1RhCOkIf5VS5HDxgM3dPbU7N2DXzohybZV83ust3Woewr8yGGDBeIi-Ndqs474NoptLpcIEUtPQbgoDJ53OkZv5RHHyyqbx0LUJaNNU9nPGHfa9W8MekiTtBuuPabFebps0m7rDEcdDl9R__rOByJxC_UzHy7Vpqg9JC0WtX1syfZf6pe_o2PxBqzIidZtOAOpxwLgwNJIcddDeesbhB_Xhkgu9Iw2cNk3s1p8wkt6v4BjhfeynL8Kvt-bNDVO9n0Bchm_kXemwTPCX0CM0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teT-uDlMFAvNXZTLhfLLvswmdoRll7gJeTfZW34645sMmKX0O5XVvYnS_bbiVIPM9QY8hJmSioCj36hVivGTJ0tT8l_OMFgBMSFwZAbZNawYBzcv8_0sokoKnqjd4jl8QIG5QFZ0w5XQNlvbEFIas5ffA9ZUuhGhC9yvU5-vrpMI4EwprAYpcSwKkK3E8eC1Bcn6T9s7m5cEPxKSxf8kfegpGhvc27WHMt71Xr_gwdct-uesGttGsvMBj7_EjvanP-9zW_yH7qnAjHpf4TtSP-EimyavrpTizDsQ44AG1sX689bMAw_Kf_PahJIS-DpiF3co3Df_2yCZP0gxEM3l-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=FKAsyPLWLBjP9SwJ3ffiAYh4BqU87PS-EYgujOajN0VgpHK96fFV4WYl0u1tmZ_hWlHXfYoKdw5-JiDddz9brZmvL-mDRuoBeZhDw2JbPV_C5m_n88wS3oD_1ZpoC6LBox5Ajl2Ufql-WtCH3v-6W4qbUjrjK5t3FsPupMA0Alxvvd7EF1aHO-_6Ggsli2Pv3AFEoZ7QnZ-v6GdekhqexQ73PsNlRIMeuxG4pvEZmq271tIS0bx5TSsiebXX2jHsK0-bLlTbLNMWVVSYyaaMmNtOqrFCYDPxvJEf7L66oV9PRgOYhq6NxCSw5Q_m8dvaPzQgoOMP2ipfWbgDxtSG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=FKAsyPLWLBjP9SwJ3ffiAYh4BqU87PS-EYgujOajN0VgpHK96fFV4WYl0u1tmZ_hWlHXfYoKdw5-JiDddz9brZmvL-mDRuoBeZhDw2JbPV_C5m_n88wS3oD_1ZpoC6LBox5Ajl2Ufql-WtCH3v-6W4qbUjrjK5t3FsPupMA0Alxvvd7EF1aHO-_6Ggsli2Pv3AFEoZ7QnZ-v6GdekhqexQ73PsNlRIMeuxG4pvEZmq271tIS0bx5TSsiebXX2jHsK0-bLlTbLNMWVVSYyaaMmNtOqrFCYDPxvJEf7L66oV9PRgOYhq6NxCSw5Q_m8dvaPzQgoOMP2ipfWbgDxtSG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=s5QITUJFwoX6M7y7T8Nb4-RytTH02WD4-E3EAvJdtrDekmCX70g8oSUPfGuwg9gcu3wjdPyzvZfBTOtdTqPpmALNWpj6PxYsj3GVSmxD-8HBzfHZHfpq7daBcsqrPWBBU3hKFQNDesPHwTdaB5SbbErpC6FDQ0S--3soXSt7SIqNeQ9VNtaQjXrP76F7tXAenzIOG4pPplA4mikuFxDujG2KjCrUk8-HW1nHMsANP2YcLjXpMOCrpLkDoBro5gRPnzvJuS4mz2CJCyo5ue0STyy0YZF2CIFlYZAPLmh-VAq4Gj1pYiUqmwHaDr6oyKngJj-sM7D8GF18X_xcScML8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=s5QITUJFwoX6M7y7T8Nb4-RytTH02WD4-E3EAvJdtrDekmCX70g8oSUPfGuwg9gcu3wjdPyzvZfBTOtdTqPpmALNWpj6PxYsj3GVSmxD-8HBzfHZHfpq7daBcsqrPWBBU3hKFQNDesPHwTdaB5SbbErpC6FDQ0S--3soXSt7SIqNeQ9VNtaQjXrP76F7tXAenzIOG4pPplA4mikuFxDujG2KjCrUk8-HW1nHMsANP2YcLjXpMOCrpLkDoBro5gRPnzvJuS4mz2CJCyo5ue0STyy0YZF2CIFlYZAPLmh-VAq4Gj1pYiUqmwHaDr6oyKngJj-sM7D8GF18X_xcScML8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC5zoqhvOLF8JR1tybyRkAT-GpLbCs5gq2ZsL_NWymw0PJpRdk3ECTYGfoojWuDgE_uDTAT1HO5lro0aV6IhIGz4wFpOfxD9o7XUwJmbJguLOp8m7Epfqh0Z6zs-w8mcVgMimJvh7IeJ4xNUUVV8nRlHcrx_P37QI4c-1--LgEQqCfKBCwm-gys0g9IDQQ1Oi3gPwER8pm4U-AFJwGRDGx7GZkVHvJjh-_tBtK0pz0zWX2IdLyWCngOc6uZSsrdFns4hCcBJetEwveEJfSDgrb3Ifsu8NtPNdLtS3p2NpUbHv4_1rkcrUBYykRAPWvtzXjW-q-mIm9VtFvHGsjUwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=MyjRucMzPdz9NqBuQ4pwjOWw333UEEvfValLsADMSzjNnRiymzs9UvtIIHgzgKM9cMhJMG1fZN4p1CnGLvnoK_gmZwa2IGrTXdFiMsvaCT9hy-FZpV6XfrtII913SqG79mhD8XswD_C4Bl9mMlKFIn9luUNBK26PkBCPxGb7tN0I5ACET5XizQgBO-DOwKIZZT2NThbIQjNo4pi2rgMFHun1hRRMrLO0ICjyAkBF5sQOMLwLl45ofpBxyPQ0YAQvP-TuhFvSVXABen0DNxRMH2YliT34mR4p8UQL3hy_HTPeHS9O-KPWsAZYBIIZZeMiDsZf4189dnsV30ZrLl2D_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=MyjRucMzPdz9NqBuQ4pwjOWw333UEEvfValLsADMSzjNnRiymzs9UvtIIHgzgKM9cMhJMG1fZN4p1CnGLvnoK_gmZwa2IGrTXdFiMsvaCT9hy-FZpV6XfrtII913SqG79mhD8XswD_C4Bl9mMlKFIn9luUNBK26PkBCPxGb7tN0I5ACET5XizQgBO-DOwKIZZT2NThbIQjNo4pi2rgMFHun1hRRMrLO0ICjyAkBF5sQOMLwLl45ofpBxyPQ0YAQvP-TuhFvSVXABen0DNxRMH2YliT34mR4p8UQL3hy_HTPeHS9O-KPWsAZYBIIZZeMiDsZf4189dnsV30ZrLl2D_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZtgcbrBxkKgKsJaqM_N6x27h09CFWJ0JEtGE1RtxzcqoNaL2MKKFLnBnjTZChg_oOQpOeht4W_aH2Q9UsodPCRKO5vnU69sJzCWHD7eztOemdTwFH_EteV9ENT-prl3HA4WFgt6vB01w4P4gG-Dkf4hB57GFVKlIld-ETzDXxm-MlT3UWk1i5AcWG9N3Ere_CuEvwId9ps6yy-blVXMzx1NtHlpSCMg3mkjpn9hx2WO6JjsBC-t7sJSlWFkAa6wzASqN9yvEk-sUzXpu1_cdNmMocbFtVfTFi0-bBUfUXUtqzY44NGK1tmUtYFVHZkjs4aBb9KIA8EBA6Fe_dtkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijObUumHp1yZG_xOgGHe9zK0j5-1-2QR9GRaoKxR1QFoq_TJsMZ-oulzcwtHFq1cHEslxamiqMDotWPfmvVy3o-PtvbDrRMN6womoXpAQOa_9baiUyB3yt_cxLOJedBNBU_-QOE76grO3j-AuFfH51_bFAfekD6lr7cnLjAkHdb9NDlN8Dg05HvVukFmcD3PFz1srqDSnhRTZJI8j7e5VUI4FzAMVTC0QHCoiQUFQPKMBEkrtabvGdGaOkkPrEsk67k0aKXBic5GW7pUwdr9QDbX89dxa8RHJF_1Woef4s-CJDmioadq3NvWeU6KpJifYbPJBFUEdntQCyFf5p8hDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQTcIR0Cwv1arbg796jnkofk3m4TE-7pj5grV4jGCl1n_9KHlCeTi34U27N8F9oeIpq6zcf4D0EIXJEYkDZ6C4RqrAhWPjMZ0U77gcRpfrvrDtq39LnH-OtmUS0KfXnd8_6R5I21jGyXZ5OXM-skQrADWJNkVsWyp9WiZxzNVdPR5KXnwBP-OXJ0_TVyx1ipWg1cXLcgs3DaOvm6OK8iX7TDKQZV-P8XfAStTCOx86rWXuYOS0ZhjmFJ4O2Mw4adhLm1N6Pv_5aKYvNd73utVSCGyPkrO5fzI68etGC43hEx4RuX4xgRTuV-cIfPjzjdu5qMBy4MfMP1irkMlo8A2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-fATE2Y9rBOdwLNN3iA0IMbWK_wFrGpVqbn0Z21c7GqIEGfm2S4HOfFkQXMD2jJZt-7A6obvcnWtEr1S57rr0EmrJ9_VcaLEmY75UkKPvbjwlhQm5MdjcexQh--RLoIe46FzAvP733VsSZhvjJadflt6PcrMzVDwMKVr8i1cbKAbuPL1Je6CVRypCk1fOEPHy1erfOYHZXJot4samrasi_ivcNeMvoMCTPnXpURN8ZNonjWfGGPOe88S0yvz78YrRQv3XkREljeJo21j-9hT1sW0qrno3LX8o0rp5T8QLetMaevFqLtJqRVwWvV8-Q8to2nCDXL3vORkXNrd_T1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7IDVXukcydsBz6iTD-jewEi2ydjWT45VkXI8Xf57brkh-XcawADisZRaRBwhMOPcquK-W9ZPZtkEiIlXowdKjcHVfzrokYrUMU4eWAqqCUudrQI7MXEsWj18Tur2L6-q0GDhNRCoeGRFDiSg0wveKZbzkiwpAJfcRht8ZXKJV6b2FL9D7V2tUpqb8LFJ6SdeJnyewwSR7NzIObtk79FYipcw1s-SQ7Ks_3Q7aqCvgEJIvs_rrDts9BM3ngFL2t9p84roYLWFgJSqZjoutUCKzwDH1jPl5aUj1t7kcPb-kTp_-Sk-8nMiX697BMdD9jbzV-SroKWy43n90dsds6mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZE3_zYCoARuchiCOd2eYj9ITlhno8V-6DCYLbEByyuYLUGJx8hiUwPQrn_vgEvth_7yuUuhRScg0ByOXmG6jiIuIzQccvRQDDWUR7_Q8I0eGHph-CwA-nzaDiot85xIvq3zrLKrnbSO_K4oNFojjzn0m9Fckd3q-5Cu_NrGUCG0FS4NDkWG5b3kjbgqEX5aVcEK1FFvu2jtc_8rAV3rr6-aGpZqm3Zt5uZN-LJagp0Pf9tLjA-M3rzncYUBl24_BPC_q6YFHSd9MgqQqaMiKyA62E-ybSTp-8wIO5ZicD4ZyGryBzQVrXxiAT-hYb9e1SX26nuIxRnsOSFHnHYdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPctMvClUxT22HnEFBV0SSq_-XztSz3zBur1N5QR3IAPuxyAdaEAuJYE0tXBiIor8qMQE5YkPPerzso11qLbTuLCI-XPmCeg7fhOLeHGTa6AvfzgL8uZtyaW5sXHwkQcdFYdHnCTS8-P0IQZYer1dvfewgF_MYRJo8VukV3W9RNu6g6bxcn305UlKQMj4dZ3YdGaiPjK6fmSsXbV43L_MYHFso_sC0H6ZMX8vYVV9c6dgQBCf3NkGwgOmW7c98l0DM4Y5Pj4BRJiRQvFQf0M5-795Vgzbs8amgMMM3McM0OjX65ddY6_vyfeA4kndCr3ceM2H3hQ0PxxoF4QRemDVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BlCOXXQOpdJ62Q1q4QaWighyGYZo2Q8ym_JhIJSQ76uFPofZZdO9Y9wAgg-tFuAzW5ilP6x6piZzFzBLAahUoLE0FJmB9qM6Q6X4bIQfcS3EJfXONFe6HnbLb6Ar3VBvmEwoOS5Ac29P4lkAsqJT2Pzq2bycmT0joM9YArJeRafMpAS4XKqIo7x_7uXN5xjcoslsRNQdQFTRvhf81sZEMDbCIePhOa4o3MnsNxRIbr3fbXGukrVJKk3wE-j57CHUTGozNG-u0_HcgkDPYXKxIMk9FbMac79SevImW-jUFdNxaUSB_mF_ujV--VsZgjJpEcyyIVbnE9CM8_LWp-sdLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tr-M8PWnxTg7bwI9q9HtYQK7MLyEO7A5mZs8VIEQug3TDJK81Oa8hLjICaC7o0RFWdDvOU13SrHZBvHY7GC_NJUWQUZlIQDn8tfpi3NZ1LlUqdt9agrv9WFq7CoSqT5qx2nQqqURepP_A6xyv-jv-zspVkX_cWFRrkRKjhZmxIuLuNB3FY4X5rq10eJ6cNJx2i92CV85YKG8OAdqXr_7edv3VzQzzrikJQHD2FU55D-9-vDgEcEU8bE86iUv-siHXK8xa040h1_1leUzKnRjvakSiBp-TgxZZHuIR1S3rO2YQfoKAsIChkf8TLFVs95BoQ_kr8sNlB5XNzuuqsg6vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-984FQh84kmaxZvD6eian-ut_2xdENvDljyZ68GBW30sR4Zyx8OGaIBG4BIpJu6u4w0fQW3W0XQJMuE8ZETtUzypdFXzDuV2SQPoGxLbE1zGbtm5SZqVDyPhvDE2nOOizpA_2-9vp2gndRqwIZ9lPPAnE3A4XUkHsndTL3SIx-1iVh2wGBvAIpuiVSOJkmRunx2PnogSmNMQWc9U0RrjDbIujkNdh-QeaEYIN9hfYBMpI1IwAwydVS-2RS3UkAKtitg3dEvCx5iJtDEKLZMHzDctZGw8to798kbKmEXIGzRG9dxbRHkT7IbpatyyRN4f_-trNF3wX_KWKZSxuqabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=tyv3gFmYO-nzJr5iGr_i30KEJ8vRV-nuj-8qkN6DT1vkGtZ30yQ4tHZK1cVi4ZqfqJo_UvtTnYUdebGJEcuyVchQj_aUojcvp2Wh8AJQaq2rLilnCMPVQLRJ2Syij8BtS5Ah_ojOORSo23kpCDfqYQwP2fyAE7yoL5uQECuoIPBm3xB9p7Bzf8Qx1lLmLuQPftUPJhrP_w-8jJhzaMDYdiId2ZrPq-53p4v9Vvd9nyDN7geS1wmf0iZuWEj1yKdkwBA66xHxTOOzAM2FXTuRf6adQO-xHxJSIHUa9mP7x2qRxTkPnSbq8sWaq3C3jlEfeNglie7PfMGHpnz6x_jdroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=tyv3gFmYO-nzJr5iGr_i30KEJ8vRV-nuj-8qkN6DT1vkGtZ30yQ4tHZK1cVi4ZqfqJo_UvtTnYUdebGJEcuyVchQj_aUojcvp2Wh8AJQaq2rLilnCMPVQLRJ2Syij8BtS5Ah_ojOORSo23kpCDfqYQwP2fyAE7yoL5uQECuoIPBm3xB9p7Bzf8Qx1lLmLuQPftUPJhrP_w-8jJhzaMDYdiId2ZrPq-53p4v9Vvd9nyDN7geS1wmf0iZuWEj1yKdkwBA66xHxTOOzAM2FXTuRf6adQO-xHxJSIHUa9mP7x2qRxTkPnSbq8sWaq3C3jlEfeNglie7PfMGHpnz6x_jdroi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYB4y6aJxA2rwjTUqa5i-0HpWjWhtpDi3lME5ZoR8ImzpnosDcfKYEyUcs6Wn_b8hqA5vmFsjBJuUMw4BbCNFq2cPauZlMxlJMhpFATZi9paff7Wq45AMsiQT2NiDjx5lEI3pP9uUnKPFd-pzBe2jpulxwy7s6bGEMgQkyedrRag6GNLUYgEko2IiNdejlTDpaxhMkS3TY3PpHbbPqp56hFGU8OK6A64N0WMvUcxYALvbz48rJLR3sboVwvIKvmCYt3ZhNjLVWdxyoplH3X_xd63YdsKWGIg95G4SZmT4tde8PUWdEgfqQZsT-xpkAh3SAHjrU3znf88y4j2_plvPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZyL2_Kq0KYkTSzmyeCBPoHYwZppLH4hMucszKG9H4NZ7NY03gwxgwOWUW6DHXs2nbVZKp_bRBTqzrKFN0OTo564FVcqTD3hJMMPUwYXyXF1PkeNzi9kek2waa2v3vPNjfIx-foJDDJGuZEXzcVyHjg19UHrJV048KaM-W64uLGdcRkuhpe5R4mG61-KCrr82fFOw4KjuQMKmONvnKiEKyahasJFHzkm86jdFJtuO6STnTTk6a1WBgOjBMIL-2lQMxJaqqom9OjwnbyB2kC2gg05WjRh5IZLCd-2skw2fsanaEqIFrndJkSf1abN28XbBW5Mk1lJ7t16LPS_XSVZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJw22BRMmWYebUBk7ICerVgp-w9red86oTrxe55heY97AdN4Q11Rzp-80VY6EwzVIa5TSPfid-y1oIwpYRml2OwctaEwkzOZvkMzVkUsjaS7YYlWJC9bxjiRaxEEpeuWvCEQUZzSp8v-FpmVDyINmyg8dQ1xYJLCkNrYxEAgCPUWHPq-BDhDGopNmqLmsIok-OV42m5lx_ayVygKfdLCecq4sWR1EuRdXR0xjkhod4e5FtHr59EZ-o-YsFU7GS5VQMshGhabiJ2K96RBwd9E2NBqICcyXfpP0_obOjpwgW1IBBv2tZdyaoc9grIQtSX-xTNZQ5EGQ2zV_GTGy27_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdJmUi_bnbEvxQfnlA4GKsX7_EAriBsT7nOmpzRDYyjibzFe-ryzVRbB1RZ9BTazet4j2s_WtwUqEjz5mcC2FNtiUlCOpKCVJjIL448QkSEAOBNKlm2CQ6prTrWAlIYUc2kHDTtsFPtbV51r3ihCdQmMalBdNF1S5xLyWqNR4nthQ4qQfBOxHZsazQUJ4emNwLLita729wmgIxOHaogPTP1yU2eX4dwYLWWLMRxvIhA4_cF-r7rBfwSL1PyYuUioGya7n5EFmOCb2qA5-oENmagVPVQOQIbJnAQWI_vzA89FQGUFS6I-Jj_wmSaCwutsfa572vs-wt0wme0ZhWsEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=sBhP5HdWxy4iYWSB_OJ9aE4P9enG_CWY7_eDntYsw0ryYaABiRNE9xC2OxoHiYKXRtOV_BGyHHzioOi7lVrRQyiGCLYIEixzsr_F6nZQj9eJTMdTgt4K3Md_vtegZf6Rj-v8wTaQ_3cmR9FC51UdvlCejbqnNeZQKxOjByEF-9nJsaBhfxEGFI8N0TXDpZULQ3kK5yNIPJGA5kHBenj05su9wbcXUxZ114AwU9MGxLKS6SkclwHWHVYabZF7IGSOdUc0dzWf2GUhsDLrPkQwZt0awTD4Uykc1GtMdCp9K8kKt5UdhdxmwKgQxIAGZOd1VXKZ4t7IDjhP7yRmjpaFnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=sBhP5HdWxy4iYWSB_OJ9aE4P9enG_CWY7_eDntYsw0ryYaABiRNE9xC2OxoHiYKXRtOV_BGyHHzioOi7lVrRQyiGCLYIEixzsr_F6nZQj9eJTMdTgt4K3Md_vtegZf6Rj-v8wTaQ_3cmR9FC51UdvlCejbqnNeZQKxOjByEF-9nJsaBhfxEGFI8N0TXDpZULQ3kK5yNIPJGA5kHBenj05su9wbcXUxZ114AwU9MGxLKS6SkclwHWHVYabZF7IGSOdUc0dzWf2GUhsDLrPkQwZt0awTD4Uykc1GtMdCp9K8kKt5UdhdxmwKgQxIAGZOd1VXKZ4t7IDjhP7yRmjpaFnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktfbLMpK-AlEJ2PVPtyAKiNU9ZUOHc5_Vqz-KFC5BpQ_E5NOUrEkK9oQfvxHuaCmFGF5wZHMHCmNNVoP0uAxJ2lxdANh5Rc_bNfzZ1HrysvPryE3NvaiGN22rP9pUUzs8HiIl6RH9vjihUAtdIp_3SWoKG-K2qzUIaE2UvJCzuc0a507gyxGlQqRmPccF6PjRped2NG0VVDzTVWJfz0UVNUSxiOZp8MWH_MsSyRxI4JfeWcMP2HXXvRXWlYCIjITrabdpLgCfviQXdvamG8HGQ4mqj_C_l1BH71RvqNONEZcGGuHeRQ_S0fxiWWwvXCtWMTjQCCnx-l7-ZJE9d89-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWWuehUMIJYTRAzkth2-FEZb811wT48WNQ_v_ACYfPMKzZTlUMpp30wifINmoyFRop3T2HkCa7dwR7Re4-Qo_4KKryD3qoLKgCc-vNFRreZ8NQBgn5fQE8wdimOQv-VqZMp5XAjAEuX2iUtTn9FNj6ylKsH7Wy9BEgp1UrWT45pFSiKk2nMORbsm7ejp6Oyi7bLqbmknc1aSJXzrs0CEP4Zbpv4I52bQsaPqe-7pdFpuHDgqWNUjWO_MVjKQI_X9PCe3VkMgZOAoku3eUr3nQfGJyzUtHppHSuUK02vETgqmmA_kHhAVU8Bw4zO0u2lw1jpU34TmRaiuAy-M3DRANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDOb0t5WPLhszOyGBv8ph1MqEutt7NxSM_zFw4mQ81RZYRQu1PtunEn7LrG6l_McPV9wEmLAzIqdILrm2SePVKxmTjeJs08AHOiE_veD85fAYZpZ9YNe-8AwipxGcupR4WPwRgAT2bWceTILZ9nr6iM2M3ZAPo8T4is5XyAxfGn3eUproz4c37yhlWHiZFA-8HUkFo_5t_7z_ixNtxvph4G3guN3XDa1VtyQXVV7PQx4dmRmwVFIUaJ6ShwRYzBAd8H6Tq1e3Fj33-y9YSgN7u4liL1aiRJfkd7k4cJuQgCeIMbLYk19Ib9I7xNSEl4cAO0HXBuXmIy5Qz-E2iG9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YictTuQCSWYKbkkXFz3F2-ORJ4bmPlerABKANho9pqaoWTcJjWnO6LuqC_4ZK-6scH6QjbcvJrDcne1ADXUTyDT5NBxtOoNOoqH24ncXEF38i_dg2zRl5muKaQljQToKdV8JXlNsxu0rRQdNY_4am2QqMBH6jbcl-1e7Is-Tr7E_78oIvXvzbmpM0jZRdq9VXY3CnAhwkoEuf5dtUsrzsJVH_Fs2v6SsQ7r5my5hG9eRC1qQJxyI4L8DA4a3P4IqrRA1z3oh1WIkHgjCcUXxJj3UaZIq64lWOPMNZL1Ch7nE5hAPsEqbIyqUD9oy0jvnvXVCYHIL0LXMS0AGGn0wLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=i0KYUOVeWqsIG_PbYHZQ8r4niX5XKxHslvXs1D45JF_JiHDoz7B0WxCBkhN6ejTonfyIRO-OABidcZjIDt_tulxOPZbpK-fvdTags_eh0a4CUQzF5O9Jl-ts0X0Zb35Z21GAm8TGlXRLWXP5Y6w05c2yKL__GKk-jCyu1Z6hODdEksQJ0lO2WspCxefQHRpmgPwfR1UbF5GxG3hJKvYNFTNFxejUoy2Qi_fKWGWaYn05BYXGlkQzBpSMRAbQ_We3kt8RnqjJjpbRTT_xf6KyqcAFVtGDW5BOyBtH7ybncgLYn6aTjYF2glbSS3MXdPnIlK27_wKxG8-0GX6-oyPXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=i0KYUOVeWqsIG_PbYHZQ8r4niX5XKxHslvXs1D45JF_JiHDoz7B0WxCBkhN6ejTonfyIRO-OABidcZjIDt_tulxOPZbpK-fvdTags_eh0a4CUQzF5O9Jl-ts0X0Zb35Z21GAm8TGlXRLWXP5Y6w05c2yKL__GKk-jCyu1Z6hODdEksQJ0lO2WspCxefQHRpmgPwfR1UbF5GxG3hJKvYNFTNFxejUoy2Qi_fKWGWaYn05BYXGlkQzBpSMRAbQ_We3kt8RnqjJjpbRTT_xf6KyqcAFVtGDW5BOyBtH7ybncgLYn6aTjYF2glbSS3MXdPnIlK27_wKxG8-0GX6-oyPXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3rF5JcOdEmWFEK90_QuRUs0baGkQGTIAF0wNdXKsjRsu7gdOU38o7QkEpzE45OvGwpCSoVQLPN5AC95WKRth8oo21Q9KP-m6uSs6PImMbT5RMhGQi3IR4ARFXZzXZ6P1lVRR8VBRdpniTJg0-ajsbIwKtja5C_DGM8PZBMll_7D9r_ecEeGH6hx47QyjzF_JmcuYVRYN8T9f7TPUAsUEv4bET9opGTTVu4KHl0F3OxZUDUboz-qe2AWXd01XG0BINaua8gRJxxrs6ZPmXGyFfSVLytzf71z96P2zbOAUjug-diunbN-mXWuwqW629KmE9bxfkUyC6Jyacw2GGTKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi51y4zXDwMrPyBK70ZgvCz7Wmz_uwTo5TRKVdxK5cGCPKdUsQ1pk-xaXbg93zh_DpQvtvg8v3_rCY-npyDK5o1KTpsVZVKYk4KNJeUXOh-Ti5sMBiuyGimnzeWj_E0M9N6H1eaeI9ysTkB0I0wIEhgNmhE5Xtf1d8in2KoHlboRfdwJ1Tnt-_PiKlECv8J6Zk2QpMCoFS7Nvxryi8IXBT2XMep81O0Ki0ZQ27WSjprIB0MdVOd_jTEWiUwYcJxkD2JNLvM6wPrkzpPrEK12QVzyA8qnpUet40PTYulwv_lx1B5DZe_bKaM1Id2ivqDXSqBhR8pwVSr-a9Ud1fNiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kqs3MBmpVX3GDvuqjihvcLn5jqIdAENZLkhVMSENMNssyBsX_cEZx_-Mn_3dPPEg0tleZIrDDPjRN0CHvHqnHRcdLSRBI6aOigAu5_Y-aEYPc1ABymeGp6Jfww-xNvy-3r0P83E5pmztYVJN2I2Xp8Bdg4SiKS_dJIGDAfA6P43SbDULfaWj6-YbKn9KexNI_mDDQTf9uEHFmSYV6HEcEO-hxIxcwjT3aWt26xPB5lk7Xp9poC4AYYxzpL8EhV5MuqT2qBzoF6a4EdiMmL7EVVMKT9sRqNlAPUNXaL-zFFVxfYmKJeKAzlyBM8ier-UezlEdVQ9LEx7R2e0LF1C0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TO7GdsbfsyuE-SaYXQd4bp69RT1UU9hAsYaYM4mlx4ajEBhpkuV-XHx-PU_0fLEoICa56qsyeb-nVdr_wbKyhDUOYiKGKrx72gTL7A-fcPe6L2TEEJoI_Kv-LkjtLx3-XWBlGffAme705R1c9OJwjqL3PxnAqANPhr6eYUt9awJVC_3eY3F-JN6qiZ1Zlhr1aJoxSCHid7eF5nJ6vCHOohmtBK3QGOJGRwq6HKFPVSwQ9LPfpw-GEG0-S_fd_m6bMujzGLggOTO0wbpzmCnXct1WobIXN3nojq9gjquVA-y5-R9jztjTEVVlEOUMgAjucMbFB83pasRDjG-kvGijuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOSIACS65ANDZH1v9a2ts2cJf40VVrCb15_eAiMTA2AGSJ5Iu2FWHyJ0m53Wd1JsJW1wOymA-0kfbSr85P2tFUZ03IRq6WMPoC7cVjCK-QpAhrVXD3y7b6ALwP2T4KRZwGoVXnwhVa8ibJcjVoj5FhnSPCUud8BXozH4vjoFRnuRmZ8E6yXtMO5WPcR0NvykR8dXxVjS9TriUJ1-gnna9s0b8HCPQ7sWINbOq6Vrar_Ksk6hjJ4u8h7vD-9kUY0cBs2Dv2xf9TLTscNEN4j8_1CXE0kvRClvx5tM78ZZGZiNi87_aDTXafFSC2OVVuBKHQZhWEjfZjRjwkdkcCRQJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R64_ZmY5j3FY236SkiSRye_QIQhXRIeRUnJqM9JF_z9XTEWEI8OfbPyKEwPlsJc8bLxHmdxF70dcC5ppQl9T67txlAUETCdHOWq06oNEUbxGg0FzgiHGRVonldSkbeMCWGWHXTi2isGBVLV3mcSAOZNsraTnSAQwonKNy-J8e2D3sBPUzMgrMfqHBSf3eB809UHJMLV6lXrdDCUOK9jWFzJRn8pIvhSVnspbejAJM4v1ShM4fy5eB286_v-CmZjY6Dc_ajRkZdLSFuzY09oOglsqHAaasPR-NrCNN7SSbE2vzIbX3oYk9UBN7QuRan9fPmscC8_GvGKmbdma3DUW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzNAKTue42jcF2WNiR7xNNetllRPXy5bS-CMsIquobrLynTS9haJnPhtUJIYaIGaq_D07TN9f-YDyRHWO18e3wXAzJoukJ6qf5fNUaQ2eYNqUp_S_NajU-u3cSfmf2YRPYHHH_dgW3VhVb7GRw9YzwEXvVF0I8mvVyGobBB-6AFwp7JUbcJ2QHOnXR3zg6HbFP-ikexgrypgXkUJiivmwZ8MLC1uw9RZQjlN_T7Lfpp2m5guk_PRQKXSh6KqCUvSkbjDAlgQR52jA9F0I9Awfqx7W-8Par018BD-IRB-R1cub4RhA945h-4Rqjeq2bS88WF5tNsB82jVue8dRI9stQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnXHBzR0vW9lExhcfLd20puQ-37McyFVoSILoNTPB9hTqYedXrce-rlNJ3TPoOMdMTODjWkdSeIG7xe4y4_QD8MaQo4p31399YOIFOClly81d2W6ZERbah8XkJB6r3o4JBV2G-mCKqSXDEmwypAJKovqm5JjkQYQ-fL9L_PEmwbUV9pItqiC-7Wegz03APTznuzCo_gaehe-lysZRx9iauv-jr7phJPzIaH2CzmBmyc_IUxBskeOsxLSfGhNMXpoMxp5NluYm89LQB-QNnWDTN7fXgwZUxyf05zPRKfp9pgj59idiLwxgl9u1cwSKENkTunFMOy8xUr5OvOZs_D8Eg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiapcsQeA-ggNZkL2aGW8WzKw1PIdD_DJbXqGcthojTYeEEun_BvU0ZtYKTCNl3w4VoCBC_ZgGnAnmsESKizcBRJS7E6pZ2Y0KU5SFqg7cWV6U-sVOnWEHRg7RmEgazynHiYX3IxOjV_vjoyFOjnHl8W4BpWEBWktVZHcq1GtcJzjUeGWIL3w75pOoPPDQVN_gq821Wxmmn75D51KqLQZxouLoOq1Oy1JolZoR-ugXZySzwozqwGYCR66Q6QJpr0MeST2pOOV8CwaBKwa73aLAO5EeqHJcBAmx6-iceGXLMkMeS_s4uhd26zwPiIDRqt9U_nJP-DXsuHMKQsSiPRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
