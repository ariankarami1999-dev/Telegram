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
<img src="https://cdn4.telesco.pe/file/TfjLwu_097OoJnoZ44M-Ji9pmihqQz1FjWjyseytQvM5kXS0ZGqnn8_cutxsxKo6T6jJgf8vd2CqPQVoj6t-G1NA56-GIdEWYH1wDV9JldK01dIJNphvdxIg3vvpd61JYlqgIg_Gf7JDWbSoqs_G652deWwyUjA1SbvITEbBfccgT0Pfnr7TpOKj6RTbp2kwHiIMl1nuBEMp63atZWC1zdiPSjMDDhJzf0JsL-yguXDWXTHpT_Mz89dRXcJtPqMadMYZlayostozdqb3OBK4RX9dO4Q0tmcVbIDtIpksecISNeSEsH4JrNXhk_4_GzGKJ3iolp7co1zWyncW9grGhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 133K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 13:59:38</div>
<hr>

<div class="tg-post" id="msg-69618">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=ofJmCq23j_lKgX7CW8VsxfzPuzXr4JPJ1ODXcRebO3tmvm0jh4TC9pQm0baeYj7IlL-HD1GNF75a0L7ES-to3Wvw0CNeEEZK6X_HTsu7LJvcQZLMk-nYDO94zxnysAKvni4o_1ssSUtqlCJpbIBRzZNYh0GSOw6p_t9_YGKZ4Bv0eaClf7i1MiRoh-U5GJsqnUgYrlfT93xPUfdyCshajd0U6WIDYUmn5jnq7yNnx__MajSCUKc7kk4lcVUST8vCTv04RvLm_SA7K4je_CgWbX4ORYkQG-kR_rfvy4epQyLEEX0irSKEa7NPr_rFU_nlpE1F51j6g47rWcihyXYWyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=ofJmCq23j_lKgX7CW8VsxfzPuzXr4JPJ1ODXcRebO3tmvm0jh4TC9pQm0baeYj7IlL-HD1GNF75a0L7ES-to3Wvw0CNeEEZK6X_HTsu7LJvcQZLMk-nYDO94zxnysAKvni4o_1ssSUtqlCJpbIBRzZNYh0GSOw6p_t9_YGKZ4Bv0eaClf7i1MiRoh-U5GJsqnUgYrlfT93xPUfdyCshajd0U6WIDYUmn5jnq7yNnx__MajSCUKc7kk4lcVUST8vCTv04RvLm_SA7K4je_CgWbX4ORYkQG-kR_rfvy4epQyLEEX0irSKEa7NPr_rFU_nlpE1F51j6g47rWcihyXYWyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از صحبت های یک دختر درباره مادرش:
❓
کی گفته هر مادری قابل احترامه؟
از میزان اشغال بودن مامانم اینو بگم که تو سن 13 سالگی پریود شدم و وقتی بهش گفتم منو تو خونه 3 روز زندونی کرد و گوشیم گرفت و کلی کتکم زد
بهم گفت تو چه گوهی خوردی تو هنوز بچه ای چرا باید پریود بشی؟ و این خون یه چیز دیگس!
از 12 سالگی هم منو میفرستاد سرکار میگفت باید خرج مدرسه و خونه رو کمک کنی بدی!
همینطور که اینارو میگفت تا اول دبیرستان بیشتر نذاشت درس بخونم و 15 سالگی ترک تحصیل کردم
مامانم گفت لازم نیست درس بخونی باید بیشتر کار کنی چون خرج ها رفته بالا اجاره خونه بیشتر شده باید بری کار کنی
به محض اینکه هم 18 سالم شد از خونه زدم بیرون و الان 6 ساله نه میدونم کجاست نه شمارش چیه نه باهاش حرف زدم
@News_Hut</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/news_hut/69618" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=UIgwHemPib2U-cUBxwwE6FqxkakvNFUZ7X5DZxpe8LHl6lOU2rWsZpDE44RE0v67dYLWTYhLXtoRyPTBLuhytWyjElE9pFtVrucUue0K4j8aiGw9zCspkS8-dUGpnB9TNLEBWXMLL2WeElTriSpnGtXIlbBrSHpsHsJF2EjJtzsflUdu1aRXkRUscLA4-ovOW3GjxAD1cYvhuBuxl0fD4qtTtzA9pcd0TYVC6dTqShtOvfBHTUU10HXk8f2I-u_vv3Q5vdyvwiCwSKQNNqHwKbSMaFt27w18NDV3Nw72K2yHoVftsGyzCBW4cvCl6Un5SdsazJeFAgYUQvpSLOO_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=UIgwHemPib2U-cUBxwwE6FqxkakvNFUZ7X5DZxpe8LHl6lOU2rWsZpDE44RE0v67dYLWTYhLXtoRyPTBLuhytWyjElE9pFtVrucUue0K4j8aiGw9zCspkS8-dUGpnB9TNLEBWXMLL2WeElTriSpnGtXIlbBrSHpsHsJF2EjJtzsflUdu1aRXkRUscLA4-ovOW3GjxAD1cYvhuBuxl0fD4qtTtzA9pcd0TYVC6dTqShtOvfBHTUU10HXk8f2I-u_vv3Q5vdyvwiCwSKQNNqHwKbSMaFt27w18NDV3Nw72K2yHoVftsGyzCBW4cvCl6Un5SdsazJeFAgYUQvpSLOO_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی که یه خانم حامله ایرانی از میزان تکون خوردن بچه‌اش توی شکمش منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/news_hut/69617" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK3zh7nVzGOzv8urkM6sKjUUAgz4zdXG7E-PH-y4LRdA6WbpUQQl2Sfho_mUSopr_nZsTr4Y6JQQp065Uc5Y0fYhNSIVKGfca3WE6ZW28fKrIUBhcl8gM9iLwILAlMJoDwodiZD4yB8eiQoQBRuACv5gk1s9U4PeNNrVwzCnH2SRh2p5OxcQZCDuU1_bnxH4KUmx6OO-PUdSn4WAu__hFAHaWJWCGqpn5Li_Oj3a2Jf-lzwTKJ5sMxAv2DPTAFCzytfpxxFa0HsFpe5p4lzR6Ydb8XMRSH0AWQRXEM1hshp5J2j8BJsM_RpJFWmde2lhNvpRjazHy21p-h0wQVp3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش واشنگتن پست
:
دونالد ترامپ، رئیس جمهور آمریکا، هفته گذشته در کمپ دیوید با پیت هگست، وزیر جنگ، درباره کمبود شدید مهمات در ایالات متحده به شدت صحبت کرد و از او خواست توضیح دهد که چرا به نظر می‌رسد او در مورد این کمبودهای شدید که اکنون تهدیدی برای محدود کردن گزینه‌های نظامی است، فریب خورده است.
ترامپ در جریان جلسه کابینه در کمپ دیوید به هگست گفت که فکر می‌کرد مشکل کمبود مهمات "حل شده است". هگست از خود دفاع کرد و استیفن فاینبرگ، معاون وزیر جنگ، را مقصر دانست و گفت که او اطمینان حاصل نکرده بود که ترامپ به طور کامل از میزان کمبودها مطلع باشد.
در همین گزارش، روزنامه واشنگتن پست به نقل از یک مقام آمریکایی، اعلام کرده است که بیش از ۱۳۰۰ موشک بالستیک تاکتیکی MGM-140 ATACMS ارتش ایالات متحده در جنگ با ایران مورد استفاده قرار گرفته و تقریباً هیچ‌کدام از این موشک‌ها باقی نمانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/news_hut/69616" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=hs0Ra1ODMt_VFgHfth0Ld5WDBR71YzjpBTQhDbpYp-33YMMrpA_Ace8Bp_MKzU4M7_MMan5E1SGj8YeegrjHy5FNFmw49cUdZeRLO6I7dJPD5P01W6WdYP7gzSjpkkWZODDqXQTySivR7erGu2PP4c1LWYdBbVzB9GrXDcNn4BiuAfZ4iIQ0S2r1-fBKffjtpBw0Ih-XzabhuZjVzaAWeduH_T5A9RFITpOHj4Xlvx-VcmGKQnQ--Jcz26VceFS77odXdiIx_4M59-R0cQTmPfdqooiE3rJF868l_s8ZTu4-C7jz5WgliIWcBcdY_cfiSkhgTptpoeKNUyV_lxCjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=hs0Ra1ODMt_VFgHfth0Ld5WDBR71YzjpBTQhDbpYp-33YMMrpA_Ace8Bp_MKzU4M7_MMan5E1SGj8YeegrjHy5FNFmw49cUdZeRLO6I7dJPD5P01W6WdYP7gzSjpkkWZODDqXQTySivR7erGu2PP4c1LWYdBbVzB9GrXDcNn4BiuAfZ4iIQ0S2r1-fBKffjtpBw0Ih-XzabhuZjVzaAWeduH_T5A9RFITpOHj4Xlvx-VcmGKQnQ--Jcz26VceFS77odXdiIx_4M59-R0cQTmPfdqooiE3rJF868l_s8ZTu4-C7jz5WgliIWcBcdY_cfiSkhgTptpoeKNUyV_lxCjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این نقاشی هنرمندانه با ایجاد خطای دید، باعث می‌شه دیوار صاف خونه طوری به‌نظر برسه که انگار داره به سمت بیرون خم می‌شه و برآمدگی پیدا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/69615" target="_blank">📅 11:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69614">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9KmAVsQxldQPBagcPvceFS3ti8kRj20gpAuRXVzRtq28R9SMfr_nj-IDQKdk0PoIa_pZkSMDrZp32AcyvfBVFsxCC7p0feMkRAJVWtFR7iR1eqSkIElBv-2gKrdGRxWjdnPZKacnKa58d8nzNQvSDE_rJH8o-FgUVTjMD5g59X_Yju_e2csyeSm5BmFC3VIVmVm9i_G0BvTBQZ-N3YQ6Per7rFpHFOz5Lss2HlpmHHqyIl_saKpV9OM2Nv5Y_hrotyrii7eclDEgzYPswcZK9iT4Vrl6pjc8P_1Xj1nlliNnBVjXNo1OSxY99EWFfNyRY6VpVu8Yc4KVbISN3Aasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرکز عملیات تجارت دریایی بریتانیا (UKMTO)؛
پس از دریافت گزارشی از ناخدای یک نفتکش در حال عبور از تنگه هرمز، هشدار صادر کرد؛
این ناخدا گزارش داده بود که صدای دو انفجار را در فاصله تقریبی ۹ مایل دریایی در جنوب شرقی «کومزار» عمان شنیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/69614" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=L2UgWNTcy5ZTHUm4SgJyCIcPXMfjYVvBx6IADUHUcQn4NdvFCBJPa2Nvyk9RZrumovA4bUQaX6BIQbDroVftJ_Ys8WF6nKG5X91--p1oGigf4-itp6_mQreOC7Y1LnnUw1-3NLpcror5dDi_OjNxnjyshKzHJufrenztCC4K8CIGL_GtNQ7luu9pSuXOEQasBERl6-7r5IJe5JDCpSu2keXWppD8_ZRSZs4nEVL55NXNa0NIBEpoSpjLTizr-uztshtG7Vky__XElBS9_x8jgxuoBgff-tS3ltmF1wahOat7sa0sDA1pSRBHL4bK0F2Ygq3MLlz4Nvn4sBpH6_nggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=L2UgWNTcy5ZTHUm4SgJyCIcPXMfjYVvBx6IADUHUcQn4NdvFCBJPa2Nvyk9RZrumovA4bUQaX6BIQbDroVftJ_Ys8WF6nKG5X91--p1oGigf4-itp6_mQreOC7Y1LnnUw1-3NLpcror5dDi_OjNxnjyshKzHJufrenztCC4K8CIGL_GtNQ7luu9pSuXOEQasBERl6-7r5IJe5JDCpSu2keXWppD8_ZRSZs4nEVL55NXNa0NIBEpoSpjLTizr-uztshtG7Vky__XElBS9_x8jgxuoBgff-tS3ltmF1wahOat7sa0sDA1pSRBHL4bK0F2Ygq3MLlz4Nvn4sBpH6_nggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حسن روحانی: اقلیتی می‌گوید اگر این جنگ تشدید شود، امام زمان زودتر ظهور می‌کند! می‌خواستند برای سخنرانی امام زمان در تهران جایگاه درست کنند.کاسبان تحریم ممکن است خوشحال باشند که جنگ ادامه پیدا کند.
عده‌ای دنبال کاسبی از جنگ هستند و از ادامه آن خوشحال می‌شوند.
در جامعه ما گاهی یک اقلیتی هستند که حرف‌های عجیب و غریب می‌زنند.
یک اقلیتی هستند می‌گویند اگر این جنگ تشدید شود و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم.
خب یک عده افرادی هستند که نه با اسلام آشنا هستند و نه با مهدویت آشنا هستند.
یک عده هم هستند که دنبال کاسبی هستند، همان کاسبان تحریم در واقع. آن‌ها هم ممکن است خوشحال باشند که جنگ و آشفتگی ادامه پیدا کند.
افرادی هم هستند که ممکن است یک تفکراتی داشته باشد که ما باید برویم جهان را بگیریم و تصرف کنیم و همه را به اصطلاح هدایت کنیم.
من در سال ۸۳ رفتم خدمت رهبری برای یک موضوعی، بحثی پیش آمد در آنجا، ایشان به مناسبت فرمودند که فلان آقا، اسم بردند، آمده بود پیش من و از من سؤال کرد که می‌خواهد یک جایگاه بزرگی درست کند در یک میدان بزرگ در تهران. گفتم جایگاه بزرگ برای چه؟ گفت برای اینکه وقتی امام زمان آمد و خواست سخنرانی کند یک جایگاه مناسب و باعظمتی باشد در شأن ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/69613" target="_blank">📅 11:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxGLgKUB5OwXoXrDgl1W5WfwLOBB1W-z8Jn3KuUQ0kXzLvqPZN_YNy5OiD-I3QWtwWBrCwDC7NAXXnuf8uCaCRWmpTc-cb4H2mI-ftuEGDaPUU-wZdvtsqJzYXHZ6RQjj-tTwa6xC0Ch90EVd64KXwlRbk00qs11xbSvNeNtA38RxhygkdaEBqQTOxBkDz4NBswDsffm1_8y1jR2XLTaYnz9-AngqZYMd0iEyFKj80taS4nuvfkZ2FYXiSlL9Q9_mXPqNsyPbHSxkTxfO-VShfCEMLNqOwORDNy_yQaZWKvZHVY1rop1Y1CYQfq_b4vnCCHyQiTIGpCQq0s9nKuSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
اکانت رسمی تلگرام زیر توییت یه کاربر:
یه نفر پرسیده بود: می‌خوام بدونم دورف(مالک تلگرام) کجا قایم می‌شه؟
تلگرام هم جواب داده:
درباره خودش چیزی نمی‌دونم، ولی معمولاً منو خونه مامانت می‌تونی پیدا کنی
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/69612" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پنالتی
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/news_hut/69611" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69610">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=qk-nFtGfPMCXwzYyQQwHRuHXTqBuwSWtMYmsaS-Ki8BZj23m4-9bkuploofbnJZKMJCIYJaRIW0U_6JsoX07Fbe8Ume-Zfc_58mg_PycZbbET02N77dFYSgyy_y37mh16PXiI5ysJpBeAWB6nkp6jG2n9-xc5FsKWkezHf-NpJfH5Oiz-8f1eQtXpVGaRx9mBmO3IF-KKlo3mu1Dbz9riVLDdxLP8kG1Evn93tfXXPI350afgecWvg7rnhvTIM9yp2ucz7ADz7sAaeOslQHJo0cfgthuRt2cpTXWZuZ8QWFJNw9XtoOmFmmap4fuKrHXck6LqD7_NODvkZwT55Rpa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=qk-nFtGfPMCXwzYyQQwHRuHXTqBuwSWtMYmsaS-Ki8BZj23m4-9bkuploofbnJZKMJCIYJaRIW0U_6JsoX07Fbe8Ume-Zfc_58mg_PycZbbET02N77dFYSgyy_y37mh16PXiI5ysJpBeAWB6nkp6jG2n9-xc5FsKWkezHf-NpJfH5Oiz-8f1eQtXpVGaRx9mBmO3IF-KKlo3mu1Dbz9riVLDdxLP8kG1Evn93tfXXPI350afgecWvg7rnhvTIM9yp2ucz7ADz7sAaeOslQHJo0cfgthuRt2cpTXWZuZ8QWFJNw9XtoOmFmmap4fuKrHXck6LqD7_NODvkZwT55Rpa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آقاآآ این بازی
#پنالتی
چقدر خفنه
⚽
🟢
بازی خیلی حرفه ای و‌
#پولساز
پنالتی فقط‌ پلتفرم جهانی و معتبر
#بت_اینجا
✊
همین الان ویدیو
#آموزش
پنالتی زدن ‌رو ببین و با شارژ اضافی
🤩
🤩
درصدی که سایت بهت میده.
💖
حتما ویدیو
#آموزش
رو ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r15
@betinjabet</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/news_hut/69610" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69609">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1558a77094.mp4?token=PY3bsXkG3DYkeJVIWBJLxSVhxirzLboyUVORauE7nzwN87mCDrGnUqmwMYEtqAke3xqqoQk0Iqhtx5t0GN5XQ7CgbCD1jM188yWMfipEi6OnIYFF_OqMynHV8ogjoSt8aLcC-vnbESvVSwGVVlX6ZZS1-lZW8YBVBTq0nRAbrJNjBS54Do0BIZ9UzOiNe2eGPxK5KzwFH9bTxWxdzxlZwm4A8J1lkxDJNgG07lKYqhlkT8C7pRjNAX6LTev8R151rVbOi1J4m79rT0eUlR8TwYkh1b_LiojTGoIsJPzB-6dJjGbT7E_jB8ChbI9Pz86j_X29RBMq03BWHp7_EWZqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1558a77094.mp4?token=PY3bsXkG3DYkeJVIWBJLxSVhxirzLboyUVORauE7nzwN87mCDrGnUqmwMYEtqAke3xqqoQk0Iqhtx5t0GN5XQ7CgbCD1jM188yWMfipEi6OnIYFF_OqMynHV8ogjoSt8aLcC-vnbESvVSwGVVlX6ZZS1-lZW8YBVBTq0nRAbrJNjBS54Do0BIZ9UzOiNe2eGPxK5KzwFH9bTxWxdzxlZwm4A8J1lkxDJNgG07lKYqhlkT8C7pRjNAX6LTev8R151rVbOi1J4m79rT0eUlR8TwYkh1b_LiojTGoIsJPzB-6dJjGbT7E_jB8ChbI9Pz86j_X29RBMq03BWHp7_EWZqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی که حامیان حکومت برای موشک‌ها درست کردن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69609" target="_blank">📅 10:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69608">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=bw1bdbN3MoYH_DqEGBQMWfi21YL7IxMKIN2tEVBuca0z9EsjhP71DRkBCCO4kABLdvcphhhgcchJyHYjCfB8AAX4hiXxdHoe8yJpnBhaIbvachwnEscblrIOX_R66W9XhqVFl9cJ1ZFmCNeyTaB8M3YRZo0OlrfZtD5Pdag4zz9-bi8L-RTyxtwSkXUtDKURuynv_TZIql0SBqh6xhuVJrx2xLSFyD9DiW8FQvDOUphYqE5QtKNCiWt-fZe2c79WrshvXpg8g_jD7UtuMeJFnDUoHQdsac8ZJHPb-34m8Yt6Dyu-fzN4kOdIKg51UyeIT6kXFbSp4d9ECvJ2NyZlRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=bw1bdbN3MoYH_DqEGBQMWfi21YL7IxMKIN2tEVBuca0z9EsjhP71DRkBCCO4kABLdvcphhhgcchJyHYjCfB8AAX4hiXxdHoe8yJpnBhaIbvachwnEscblrIOX_R66W9XhqVFl9cJ1ZFmCNeyTaB8M3YRZo0OlrfZtD5Pdag4zz9-bi8L-RTyxtwSkXUtDKURuynv_TZIql0SBqh6xhuVJrx2xLSFyD9DiW8FQvDOUphYqE5QtKNCiWt-fZe2c79WrshvXpg8g_jD7UtuMeJFnDUoHQdsac8ZJHPb-34m8Yt6Dyu-fzN4kOdIKg51UyeIT6kXFbSp4d9ECvJ2NyZlRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
پزشکیان:
حوادث دی‌ماه پارسال قابل فراموشی نیست؛
یه عده بیگناه هم قاطی اون اون افراد تو خیابون ها شده بودن
وقتی روند به شورش رسید اتفاقات سختی رخ میده و ما دیدیم شرایط اینطوریه گفتیم کد ملی اعلام کنن و هرکس اضافه تر میگه هست خب بگه
کسانی که کشته‌شدگان رو ۳۰-۴۰ هزار نفر اعلام می‌کنن، نامرد و وطن‌فروش هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/69608" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69606">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=k8WahlDW11x3V-jzss1ThYjcLQi1xxIU5Ohjs_RVrfbCnOhlpS1omaUAwl3mY-8Qt-F0HvIcmOrMDZotBzsahj-41Jj3BRE0J8SiNYRnEDXT5J1RsbotGa1TWA9SKWlHx_O6S5kTIi2ZolapO83d2oyuzV6vdd5JDagzfi4oNCgiaUjN4VxtREJkxP1P4gdqPuNUKqY1DbdCMycvjxl_Dai1aPo6mQT8dJnTTiZnRVbMyVf5bivgLbeb5cDRuQEyZitgudsVDjaxsdAZAlGRGAejlE6tQwoo5pj6JEcvGwaqOpbY_2qUO5y6MAconwDboC6PhX6SRLHPDmOgnxqS-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=k8WahlDW11x3V-jzss1ThYjcLQi1xxIU5Ohjs_RVrfbCnOhlpS1omaUAwl3mY-8Qt-F0HvIcmOrMDZotBzsahj-41Jj3BRE0J8SiNYRnEDXT5J1RsbotGa1TWA9SKWlHx_O6S5kTIi2ZolapO83d2oyuzV6vdd5JDagzfi4oNCgiaUjN4VxtREJkxP1P4gdqPuNUKqY1DbdCMycvjxl_Dai1aPo6mQT8dJnTTiZnRVbMyVf5bivgLbeb5cDRuQEyZitgudsVDjaxsdAZAlGRGAejlE6tQwoo5pj6JEcvGwaqOpbY_2qUO5y6MAconwDboC6PhX6SRLHPDmOgnxqS-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
باقر خرازی (برادرزن مسعود خامنه‌ای):
ما باید از جمهوری اسلامی گذر کنیم. علت اینکه این الدنگ (پزشکیان) رئیس‌جمهور کشور شده و بی‌حجابی کشور را گرفته این است که هنوز از جمهوری اسلامی به حکومت اسلامی گذر نکرده‌ایم.
خدا لعنت کند شورای نگهبان را که این "آشغال" را توی پاچه ملت کرد.
چهل سال است با آقامجتبی رفیقم؛ او بسیار تندتر از پدرش است؛ اما یار ندارد.
باید به نیت حضرت فاطمه از هر شهر ۵۳۰ نفر جمع کنیم و به تهران سرازیر شویم و کار دولت پزشکیان را تمام کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/69606" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69605">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ممکن است دوباره قیمت نفت را «بالا ببریم»:
«قیمت ۷۵ دلار است. ممکن است مجبور شویم دوباره آن را بالا ببریم. خودتان می‌دانید وقتی آن را بالا می‌بریم چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69605" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69604">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69604" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69604" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69603">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a14
@betinjabet</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69603" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69602">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=k9CAxU4EXlzUDPgejp9VsKrdy0Vf1ZXqSIqH2L6OFot0Dsb2pE8IPlWxYd2owpUtcTsLdXi_K32TtkhSa9znsvgNUaoXms3KjLrKrV8nhi0q3d1hS2kgrv8PyBchmcPphCtnmlRfebssQo5oAS6xGwnCi5bl2E-Q4NRO6V6QlrqBMBSC7nBNJyB-JEq44sfi7UGwfkP9qbiKKRCY6j7OekUsFqJs-vUFWbl8fPr7ThAr9P1-PJCR_OQq1bH1i-w5E_T8DpID3PEnHiJdb5p4Nj7Sitf0oeq-M45VkIgB-nDuD8tYVIuHXl7EW4K02qd47RyrxIBRy4w9qqqrJhBOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=k9CAxU4EXlzUDPgejp9VsKrdy0Vf1ZXqSIqH2L6OFot0Dsb2pE8IPlWxYd2owpUtcTsLdXi_K32TtkhSa9znsvgNUaoXms3KjLrKrV8nhi0q3d1hS2kgrv8PyBchmcPphCtnmlRfebssQo5oAS6xGwnCi5bl2E-Q4NRO6V6QlrqBMBSC7nBNJyB-JEq44sfi7UGwfkP9qbiKKRCY6j7OekUsFqJs-vUFWbl8fPr7ThAr9P1-PJCR_OQq1bH1i-w5E_T8DpID3PEnHiJdb5p4Nj7Sitf0oeq-M45VkIgB-nDuD8tYVIuHXl7EW4K02qd47RyrxIBRy4w9qqqrJhBOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ترجیح می‌دهم با ایران توافق کنم، چون نمی‌خواهم آدم بکشم.
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال گفتگو هستیم. ببینیم چه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69602" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69601">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
هیچ‌کس نمیدونه که کلمه «dumb» حرف «B» نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69601" target="_blank">📅 01:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69600">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇷🇺
🚀
ویدئو منتشرشده از شلیک گسترده موشک‌های اسکندر به کی‌یف و حومه آن در روز گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69600" target="_blank">📅 00:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69599">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTaJ9YZPScV5_S6PgHLPuPGYOCuh5GxbxtGcUQR0V3QXgMVcOw-oVPwmw1hbrQ0TdCE_O1wyAOitU94-MfXbvo-C7cah1vfDHvxH_vTRVah6OVFuUa0W_kUusOecySuinwcMtipDk16mfcjmK-cOUjD86xHJ1Wp7x_o27mfyj-AyCNach0GRqu1qOij5QuRVIIbbxWIQ-0wQUUg44iqztcaG4fkRuzbyAl3PXypvNiJmwUcBk7FB9MoGDKtNSq-elXVvfBL90kYXy4djLAV8LTaf73oT2xmUdCBzbUEnfRH8ks0rwIj0PRha9JyfuU4_HY7sBSssI7FWDc-frNNnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مود:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69599" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69598">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فیلم وایرال شده از یه کارگاه آموزش فن بیان توی تهران.
چه خبرا؟ به لطف شما:))
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69598" target="_blank">📅 23:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69597">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
دیروز یه خبرنگار از بقایی، سخنگوی وزارت خارجه پرسید چرا جواب صحبتای ترامپ رو نمیدید؟
بقایی گفت چون باید رفتار ایرانی داشته باشیم و حرکات زشت دیگران رو الگوبرداری نکنیم. آخرشم یه تیکه از یکی از حکایت‌های عبید زاکانی رو گفت : "فعل و عمل ما را و دعوی ایشان را"
🔴
حکایت کامل عبید زاکانی:
شخصی اَمردی به خانه برد و درهمی به دستش نهاد و گفت: بخواب تا بر نهم. اَمرد گفت: من شنیده‌ام که تو اَمردان را می‌آوری تا بر تو نهند. گفت: آری، عمل با من است و دعوی با ایشان. تو نیز بخواب و برو آنچه می‌خواهی بگوی.
🔴
حالا معنی حکایت:
یه مرَده یه جوون بی‌ریش رو پیدا کرد، یه سکه بهش داد و گفت دراز بکش تا باهات همبستر بشم [ کونت بذارم ].
جوون گفت: من شنیده بودم تو جوون‌ها رو به خونه میاری تا اونا باهات همبستر بشن [ اونا کونت بذارن ] نه تو.
مرد جواب داد: «درسته؛ عمل کردن از طرف منه، اما حرف و ادعا با دیگران. تو هم فعلا دراز بکش، بعدش هرچی خواستی برو درباره من بگو
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69597" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69596">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
ترامپ بهترین دوست ماست، اما می‌خواهم یک موضوع رو روشن کنم: "موجودیت اسرائیل قابل مذاکره نیست.با توافق و مذاکره یا بدون آن، هر کاری لازم باشد برای تضمین آینده‌مان انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69596" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69595">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/news_hut/69595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69595" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpAnE54Gyh5M_6D8K0T6vk3GsGNxEFlhNLz5wJ8dOj-RSoOXolR9UqMnz0zxBa5ZqC745bFQS1REPQazzsHQWQ-TLslDfXoO1AOmEYePxSmUf7_2oeDjrz-_4kBO6uLBH4d8nZs6_TLyyRnNogSlvNCF24MkleiZqWiWvcvP04SSxah30bBz7AMw1eRJ7KMx7TFaCVwZ1ZbNR0QJcYsrl4e-M-6GYsAJRpRy469A6wGLgSwu2vmwnazUuYH4KV-74F_zguBvOA5X3ED2h1kAmecd4QhKdoXM96HUul7Bq6ge7VIkFW1eavKeIAZ4zNn-1-4HPYMhzfJrPIqdgGfcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXvIEG8E64z7W5qzBTFGEZb-fvE0yIw42QuftCcgruFKFCX8ZICN1KfAo0KewKrzbEe2B8X9_EIOK3AO1JlF5DrgRls6WnlOTIWE0oBcaKEvj269Ms-y8Of9mRasPoD3OFj5Kin8SSmuymHPxbn0VOvoWYTYEpPGYuzDSkFJVDW4InP1sRIF4YCzVrwMIw95Vt7ufE_6ICzLtS8FMmmHC5N7rFu-u-snB6ZT2KzY3ymGPThm-dkdX42WykzG8-tTUjw_QRiTGjz8RnT86_zW_4c_ctwQIAD_3O9iFXhuM5arc4OYWxTm7Guh9N5qzb68Gg7u_k1JPiDW2LVLbuL_fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو لیگ دسته سوم تایلند، بارون میباریده، ولی همینطور فوتبال بازی می‌کنن
یهو یه صاعقه میزنه و صاف میخوره به یه بازیکن و اون بازیکن فوت می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69592" target="_blank">📅 22:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvWg1y3cP7Klh5_CAHbtXxpy_kF9jhy14KFi0X6m200jqjSvx6N2I_ajP803i9w0-EyZqS7dJwgAFujXPE7qfMrCfrYxhKCRyPCTpHeOcJkw84E0LYG0g7HkCHstoGwIdSSF56wwDU-GmNva9POxhZIeI_z7ZDG5HAooKJZfhcnvJZbQDnwMSYzp6sajYsg9inHDvZsXSHe2drNvkEvhEEwZLyt8262jy9Xm2SmQnEwKNoKGp2vn9Pw-BF1BFEqJ3LMKshvV-0uP2Y-qncQOji0uU9FZ0aijlnjLZeratz8oWs5V_OvWuHjRyCW5uwDJfSbMDh9c4Z9zAeHtO4lVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇶
وزارت خزانه‌داری ایالات متحده تحریم‌های اعمال شده بر شرکت هواپیمایی فلای بغداد و چندین فروند از هواپیماهای آن را که در سال ۲۰۲۴ به دلیل ارتباط ادعایی با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بودند، لغو کرد.
این لغو تحریم‌ها، شرکت هواپیمایی فلای بغداد (که با نام عراق اکسپرس نیز فهرست شده است) و دو هواپیمای بوئینگ ۷۳۷ (YI-BAF و YI-BAN) را از فهرست ویژه اتباع تعیین‌شده توسط OFAC حذف می‌کند و به تحریم‌های مرتبط با تروریسم آنها پایان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69591" target="_blank">📅 21:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPaw0qx88yQMq1jxFX5FY-nOAHIG8Gxx5aUMmCLDDRekkKKMOtLXhLl_C7HE6lzRfiGJTlfu2VgMizad0KFi7jkKvQ1honHiSLQmIzDtepNfoDoWg-W_xml1R7mJGi45kF5av7OR7icUBGSZ7Qrjay0YECSGn6pmGB0tKUm-0IJhnrUxM7fU-ylyP5xgH8T0SVQZrwKABnZiQ8Z-DVHNWoUdFd_ZAdRPonYFp4wnO8cDufZWYwUma_JFVISsRNPd8GiqrubIS1cfDMbtfgrab-_KXBCG19TltHPlTzZbOvFEiBYkgzKz4o5YPrUfnq8MvN4xQCcAkR95x-M9ijnM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی:
ایالات متحده تقریباً ۴ یا ۵ روز پس از آغاز دور جدید درگیری‌ها، پیامی مبنی بر درخواست مذاکره و حل‌وفصل مسائل ارسال کرد.
هرگونه توافق در خصوص تنگه هرمز باید صرفاً میان ایران و عمان باشد.
ما هیچ‌گونه دخالت خارجی در تنگه هرمز را نخواهیم پذیرفت.
با اجرایی شدن توافق جدید، مسیرهای موقت فعلی در تنگه هرمز بسته خواهند شد.
بخش قابل‌توجهی از مسیرهای تردد کشتی‌های ورودی و خروجی به آب‌های سرزمینی ایران از این مسیر عبور خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69590" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
❌
🇮🇱
امروز در پی وقوع انفجار در ساختمانی تله‌گذاری‌شده در «مجدل زون» واقع در جنوب لبنان، دو سرباز اسرائیلی کشته و هفت تن دیگر زخمی شدند.
حالا قراراست بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، ساعت ۲۱:۰۰ به وقت محلی نشستی امنیتی برگزار کنند. محور این جلسه، حادثه مرگبار امروز در جنوب لبنان است که منجر به تلفات متعدد در میان نیروهای اسرائیلی شده است.
به گزارش شبکه ۱۴، انتظار می‌رود مقامات سیاسی در این نشست درباره انجام یک واکنش نظامی قابل‌توجه گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69589" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله ایران تا آمریکا با موشک فقط چند دقیقه‌ست، اما پیاده باید نزدیک ۱۹٬۳۰۰ کیلومتر راه بری!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69588" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69587">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
ترامپ بزرگ ترین دوست ما هستش اما به صراحت میگم وجود اسرائیل قابل مذاکره نیست.
با توافق یا بی توافق هرکاری که برا آینده مون نیاز باشه رو انجام میدیم.
نیاز های الزامی سیاسی مجبورم میکنه این مراسم رو ترک بکنم.
در حال حاضر توی یه رویداد بسیار مهم نظامی سیاسی هستیم.
این جنگ موجودیتی هستش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69587" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69586" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1mVBnOY9Il_iowEyHWyypryntWUbv4xZG88JfOx5l82PU7NxP6LNl0T6UcoyZIqvwpvo7SwYBoi8FXN3KxZSpCE7qhyZS4pqjBHELpJTkf9cnvTp-tMSjTGpH8QAe-nIvmuyxzZoNWbtK8xZBGnmJIs_KEqOhvUbS0Wbts4F4ghFaXN_AfnGUmKSBQCGIn4BvU8yfAv2iI35kVRJaNQo7m3hGxWXD82eQW3iBtFLg6QuCPJamSikHcljwBqe5zv5fPkhNGxotQwPGEkYNSQtxV20hkEF9-Xy2wSanjTQ0H9q8b-XcXKiZgcfjrEFt6tz_dIm9jFX3kLLvi5nWp6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/69585" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پلیسِ رشت یه ون آورده وسط خیابون و شروع کرده داره به دخترها اخطار میده؛
بعد واسه مشروعیت دادن، یه مصاحبه از این خانم رشتی رو منتشر کرده که‌ با میگه:
گشت ارشاد رو دیدم احساس امنیت کردم.
امیدوارم این کار ادامه‌دار باشه چون اصلا از وضعیت سطح شهر راضی نیستیم.
چهره شهر اصلا عوض و زشت شده.
الان همه فکر میکنن رشت این شکلیه ولی خوب‌هاش رو نمی‌بینن.
گشت‌ارشاد دغدغه اکثر مادرهاست نه فقط چادری‌ها!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69583" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=LXxipzIWjFSgs5T6CDLXzcGO65-p-fmh8IGu0KITLh_p1Lxj-FBJ3NPs9rzx4-SKi9XGushnNu5o_QGMPjUta-4zg8CfQmuNxI9t22Hzvcz1xhE_M5HFpvc8P1QJ_8H1XwGJH9myFnJuuuzwKX6ssVheEX-e7Ymy3CrM21OnGJ_G2bFfQXo0yUOOptKJHQx-xR1sGvJmaboAX2gsfGmtQly5KWW_jZKvLfYbfhyYjIN_dSAsmgFrX26Pu3W9LLdUL4rI0f3LQ0Y0ZjwjsaMXpVHN5GM3HUh7xJR62RmVAoN4oXYppRuNkATzxQMjK_ipCC3PfRSfVW1_MbKdhE2fTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tky4zdmcB9VE41RQnjhJ6if7DzftinFqm_thjZMi7skQPtLA1Z3EDd6oRel9xfwlbjUUPBSF6lHykH3VGZkPLmtHLOd3rnreTsVTK_rFuK-S7xNiKQHsfqEvfJ-vZ1l6HEDblr9n1q1Da3uCkdqH4Uiw__KpvpkaETpMcoq7FXUEejds9Mx5-kqR4vqlJUTrWPtw8DGhgJNnPXA8uX2sHTcUm2X1nW39RZpoi71BsSR456VNeNU9UZFjtDYHryGxxCe37Dvt30l1nYKMzlPEbZfZaB2M8TnoljBoLBs-J6K3ZZfvbTpPh2h8UR9qlGKTc_W5Ad11mG4A-8v1iJYBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=Z8dg-Qx0OSbSFlT9LFhE0AYm6Py9IIbJbqPLnY4ORoENUS59po2so73tCinX_CfTzRbFQ0DIu7bAXgxD92Nry5C7mjYfPVlLClwqpcXbtPpCMMl8VPhlvhs8MY2I9Nf209WRECM7YidR5Kw6XCEElzOlO1DPV8gLdCF_KaYc6vuln3LzVVUNeRBD8BrAciTeo05Q1GAHA-nqevKTCUEnZUb6g7WJg5gsFrWuLH_-KX5z3dXWPSifQO5vT5qjT6y08f6pD77pqZnTodiDNvpkzYYTwgvaSLTOie6OW2ynUlv4OkUyc9V37qdV1GTkolOfDDBvtjqfm2UcvvFxJ1WZ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu2t8zjQ699wLlxessi_d8uj-0P7Q84GicATwCZDgeLDuPZurMdZQ08ErbJJWGiFikXSgX8e9lNmFvEZ5Aiqg5TlKZ3yPENSLZl_WbWaLP7LRFEcmpfiW4RX5ck7N3sD5nEt0ktwPijyHvNorm_FIjZJ7KPbHUHvNKMfKwGn6iz-cMJhABd5JtgA7cGtAVABKFut8IqiwROtMhuwW-AHkQhhzJ3Q6n1b1HC5gLisb1id7wMIPk9ZzUY3S6ZX6X1q0ey4jo79FJGikHiKyZ_emU3MfGhbZyoRTjxtfSqjNZLBPOaTk1BTx3m209liR8-nTswSnBdic0Hab333N0Tt9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66218d020e.mp4?token=ml2PrSx-0DZIjlXhT3z0o7URLgv-771a1UXxNa-IL4XsVf1ZXcJ1r-GZb5F2NQ_vcBzQzJnDnXzK3N-_VfJTxZQxqG1VwuqgVPOjq7pIWg7kufasSlcjUUzMRB1ZOj1rfAKZlqZgPpPguUApFDfNQpCsVtLIr9ZbyEUnu-5jInhRzB-Yq3A0AQWWzUI8ONww2zS5BsgfPMQjdduaMYw05PNVZ7PhbArxCW9uUxQ1Tb56PI3aeSYwK6gKeqKr2NitWdKvs2tknJalWajViSI7hiqGkEWQnTkHkQinRZ_-nTMDEPrK3Xmi3kvqPI-Hdf7EX_svG4ykb_3NuswwwpHcXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وزارت دفاع روسیه تصاویری از حملات پهپادهای جت‌سوار گران-۴ به سه کشتی باربری در دریای سیاه غربی منتشر کرد.
وزارت دفاع روسیه ادعا می‌کند که این کشتی‌ها تجهیزات مقصد ارتش اوکراین را حمل می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=f_RSnj2iP326U5dXMUV-51ERONSboqSfR1s-nPOHj_DxXuTDAJUtOdyANJZtQXs-2HPvE3PFqzNo9Lu-n8QYH5TlBEMnEytvazVKNGbGfbi6J3UpeCYn-eXhP4KnoRvgQYzOz6qTCZvPTO7WkZOXTQXFcVtz0JRg7xdZmxC6o1hoXxV29mP8XzB2Ze5QO8vX-Ofe4xtoPyJsfEiY-J6VvxHVsOm1tzm1t-QIZlrivFNkdYqtIYlw3VTjOGeaGTS5l1Kjwf6JUDu07d-ydl6zEWObMN8VFT6Vdo3QoSojWEzklIjsfjKIPdzai0J7KgMIcoiHbEH8Si4DI0g8bnFl4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی صداوسیما خبر کشته شدن ترامپ رو تمرین کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd7b_blE597c9V18S60V6KV18xaU2tgBsAhcL1z7icMSs-GIV1gfKogNqtbAHYj6JcFof4Gv21k_OWNiLjpHFIhfeZT7MDWTf7XXCOikGYEJ44tcSigW2b-dxVyqfmNwz229h2338vSfbH5Gcq1xSNTnYctxWV5ozx3U1Pt2hPMsV8OKykWuyYwGlc8kIzbF-qCm4WyRxDmace9hy3bOg8_rwZcM6HNfZ1Fg8Y62YneND2LnFdKuuUWYm15iJsIjiMd_sTRnob_GKfSgsOdvzjcR9AFpK_eJMsnPzmmBC-2iAK4q-3wRiZiyOTCX4PvZhXR4fvn7Uze5wNQRxP78fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqXC0b22XjlDhzWHAASMitc0FIlfUu7N2cMsZvX0F4SZSIhm7_CrfTZOvgGMfXnAmw1Mx0LoqtAC_Ez8ZOHZU7TIfYqUK3DdJN_lLAUQ9_GWHh1jp3dEDHbfGEjZwhaGMlBB5fDXYFGJIDVB3i26Y3mWJ_DaASeHXWvsMRw4AdYIyhDoI2BNmkPLX0GxDIw5e8xinLYKSSrF0Nr2FbWjaHSY1ublWHjzjN-sieAuqBmz-70l39On8ly_sNLtrB04i1SyWChQgU-7iyZOVSKIh2mJW7f365R-tknJjgcMUo5Q5xVkPOQDW59V9UFXMFBtbHvZg1HhBaWvpKQ9n-yBCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q177bzmUaAbbQ9U-sERREHRwvhXz4ZDpONDivU_OsEg_NrYATL1C0MwN7vYH3idtQWbKcAqdHfINxMcfcYsgkqWm_HepLpDw82-NW20AJ9a5Gkb8tKg9LG_Wsog4SgVwdulpDuqzbjk6xSVi_8V80yNbNoO4a2K21YXmI5eWXP2ZhsoNUBzwaOExj7uDd3gsdiOF4lxlfSZrrBhe_SzeM0tlDOWHQuIZSCr3gJqwnNbJoKOHp5uIrc1RHRgAiV1QiIWoON2X0vb88h3lBdnv5cf7OQ_ym8DiWL4QBlMzKKkzrOngfVaXnyTTSiN7Yp7XiAjIx1Ul9OSCsAz3mKYJLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NePd2AjrG-qIKCOGEwSRRJRBu8QPtCXKTg4Jr5xd-M6Al2hvwDNX_KJhsRUYgOP8lPq20xSjliPUH6R3r2mavzA3uHPQWlWiIbOziLmdg3MU65s01bBES8PdA-RlVKKIj9mhZPt0YdpkIPQebwRSo_8H7X1YdHL3-B_4t8EpFUWld94wWP-jENr_-aIvxqaWXPIFKojew1wGpCUUCaH2LII7m_XBcdQOgaHv_0r6XNAnhJLYVnM-OJq0NQb8W70dbbzjo6wnECG-xTuNNJSq8bxuX-vffIRjvyEKXSX1ZGFNThYrgJu2B7kSx6lvqW_yzfT2i4TL5w7siqgbFTgPzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
پست جدید و لاتی کریس رونالدو؛
"
اسباب بازی‌هام
"
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhK75q50Te0I-WOm_jBxJ5kce795u2l-mgemADFp8l-CUr7d1oyNUGGERUv_tt8Kb3h9GCsevBzkIE1UL8luLMPKkG_41hP26EVkoU9FTBDiy7-eXSQuOAhOQpC6Ovbd2mQJHHbX0aCQGhqD4QJOsM7yhgOEnMPr5mVUxuSK4FXwL1TW8PoFjMI08cOJINL962WcrteNJS_sv0v2OM01TrPYr_wrbJ2Z0hXqx3mhNY2jpIer3p8pPH-u9WH8qAjRPJswV_qF3ESEAwbjktuSJa2mITuR5Vssd4vh8KLa3aoui3JhmyqfXXUMeiBm_vm9UR5PS975jkqT8otft9sSMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8rSOLoaPE19Rm1BA8FW2ihapu6vIACx4LmXziCVgzPhQXm7xH_dWtpu3WENHTo8zgz8tel7rouppyOLguBrZRpclEAsApD4y24eQPcfkb1o5_VOGqWZopm618IupK6ZbZImWYbBRrLXj_yuOtqiu-K1sFpWplm7hM7wiNy-izooWKEWQahdrdTrJy-l96ZZqkcCJGS-KOPEKAAefyXNeqdMoTx7458Os9p-V8ES4UBOgUN0-BkCib7HQl_ICBrkY8aEP0OxJmH40G7s0iErIs0NGOjBXSNe_dDYu-zJl6K6fxD1ZR0MbN5Cl4vfataA-0NVCPwrhUrVgGJ5jG1V4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=OfSOX9eIWy5VtzhLnabZcjyYeeWX4CQhsAXeNNR6m05gzZWqqvy3VbqRw0PWWBZkO6hESZAHFpu-8jS2KcMNHKrcCN_dPTE6smQydOBpnaNXY_kL4Caz2FU8hm2OlrHdVKDztXEFq07uFcp0Xe8V5n7ICqeV3scT8R-dyVF0DpUUNKE9Ena2cYpvcR09aXciWtPf8HRaMikIgN1c88Sn6Pf2tSZRzTLoxBrCGThGQOZ_PpbHbfgfWn7Xejvu0PqmqPYJ_J5GSTmjpnIMAF0mWjrJ5AY2y_G9NcITVt_43ilOWEd2w2was1ZNp8HPBNmOnOeBuUQHoDfgBrb2vv65yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=OfSOX9eIWy5VtzhLnabZcjyYeeWX4CQhsAXeNNR6m05gzZWqqvy3VbqRw0PWWBZkO6hESZAHFpu-8jS2KcMNHKrcCN_dPTE6smQydOBpnaNXY_kL4Caz2FU8hm2OlrHdVKDztXEFq07uFcp0Xe8V5n7ICqeV3scT8R-dyVF0DpUUNKE9Ena2cYpvcR09aXciWtPf8HRaMikIgN1c88Sn6Pf2tSZRzTLoxBrCGThGQOZ_PpbHbfgfWn7Xejvu0PqmqPYJ_J5GSTmjpnIMAF0mWjrJ5AY2y_G9NcITVt_43ilOWEd2w2was1ZNp8HPBNmOnOeBuUQHoDfgBrb2vv65yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N84E8awy6fEv0M7Mn9dGRw2-35bSb5XhFsJWW1YxtVyKC7KXalpWujc3gfDjDI1cIYBnyQOaQX_zEXCacdEBD9E1Af24urGFWHuCw0xRP5KHa1OwMM3J_54E4IEifCXj95F5xrUEWHU4CwMl9Z1mhnbgzub-3ki38k6IK-9HyNEwQaZhfEuekJwsAnE74XgkqKv_fILZMMmPFF-E6pR_Zg3UwvtPuDwvQRe7ZyV8R0wSYuq1xehyPMNdTHIPyR9haBL7OMkmBqqUzseMIl_2srdVsMW1Mv0-f2dZGCyoiT6t0w7kKCeTc9M4K6P14aaGm_9Uiu15fhtDODr9kWYcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=gefABuqo7crofDC9f-95OQPqp_Spn6uZQ9hFZFR2aRlFktavoPZigkFSv5lI8Ca7TX5M0GemZjV3BZaQ4tOktgR5dgmXeX9S7pKWIy0BbGnYikcOniZYMCnu_xsZOSphT7A7XnBbEf4DXjKoXQoTIh1O7vzqdHWNOLR1uePeDtstft_7J3whIR7syikNHj0snHRQ6dl_M8qJxbKCHvtsVNQdc1jgviad7a4NP-XxN02VCBuhRF8wJ0he4qELGnjxg7hgvwTbIYW09FBwh9BF7awe2ryTpiGKmMsejsnx8hz0hjf57DCIVthgjSAn81qaPCGF6PRfR9nQRJXb645brg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=gefABuqo7crofDC9f-95OQPqp_Spn6uZQ9hFZFR2aRlFktavoPZigkFSv5lI8Ca7TX5M0GemZjV3BZaQ4tOktgR5dgmXeX9S7pKWIy0BbGnYikcOniZYMCnu_xsZOSphT7A7XnBbEf4DXjKoXQoTIh1O7vzqdHWNOLR1uePeDtstft_7J3whIR7syikNHj0snHRQ6dl_M8qJxbKCHvtsVNQdc1jgviad7a4NP-XxN02VCBuhRF8wJ0he4qELGnjxg7hgvwTbIYW09FBwh9BF7awe2ryTpiGKmMsejsnx8hz0hjf57DCIVthgjSAn81qaPCGF6PRfR9nQRJXb645brg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=XWIVcwqWRPDuEwRob2pN-TYfie4qpE13N_NYET9sRyJCePjOn_O3DndQRK7AXiD6qq9nJuI_PQ_L0oke5ANfY_9ruZBoUTIIf29-qxjUAEXPt7CiKlt-G422XnW5oxG71Y6iBhheYr3KljBCkZmGxoIDHdOaR9QumPe7e_9I2DeiExxXlIxgR-Lm1eG4EXqoDCz2cbGv_jD-A5Tuc4uqUtSDFb3KGnDGaMcPWVeZYRucnvE9DpI6t_DuCPLW61lvXIZm5TahLdKQq2VELD7pXuGTJYeGudPhnOnvOj197b5VMrzT0m_U4s_QhiEsRdqgqq0kMH_dN8E7-_ji0wmLGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=XWIVcwqWRPDuEwRob2pN-TYfie4qpE13N_NYET9sRyJCePjOn_O3DndQRK7AXiD6qq9nJuI_PQ_L0oke5ANfY_9ruZBoUTIIf29-qxjUAEXPt7CiKlt-G422XnW5oxG71Y6iBhheYr3KljBCkZmGxoIDHdOaR9QumPe7e_9I2DeiExxXlIxgR-Lm1eG4EXqoDCz2cbGv_jD-A5Tuc4uqUtSDFb3KGnDGaMcPWVeZYRucnvE9DpI6t_DuCPLW61lvXIZm5TahLdKQq2VELD7pXuGTJYeGudPhnOnvOj197b5VMrzT0m_U4s_QhiEsRdqgqq0kMH_dN8E7-_ji0wmLGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOuAi5HfoMf0IRhcJiHrJ0BxaIq4QtQ87cxB4RyfJcpIlC1QaOnwegJQa9amoBV_5ZdAdjjCRblL3RKFhPuUST3A7NAFWccCts921WDUoVfwtOmWskjzEHxfsv0gMO1F15LbrEMIetQwAeQ-TJIGi9LJnpxYTFU1h3fkLgD1Y-OCRZ6ECUXSjJFV0IldHDmuAmpJDrDDVU6zQe_tvBiIjkCuA0oXFxpbzj1-v8vP4VqxloJCKtLm88uIGRtUzA1Lctx1RU92tF3xYwdZko_Dt-QSjVAlNmdZKsyfXFt52Yf6ySlFVlYjHF550BShPHFBHgkK-v6C38mQ134J2wmDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=ozcH6R9oLCl_XHPT1HRQxtOTL1vYGksHE11RF6GStDyDVqGaXhS-hT-e-pwvRjxysua2AzQruCqWK2swkNUcqGM6A_rWSQ0sBnfag1jrSwjUovRhoN6SdXqkOQ7XWke93XkPuRmHBZAuZS1iBTgvWODfPEmx2AiG1McRh9zcmLK3B7GkqCUAHii-lJ27H8-ADUnfErf8iPMSlsrndKcpdS3KwbYxoMdjaRbtS2FHJEOG9pZYNwwa9-BiaoZ0aJxkc2KzZ84Ir-ZAnYQTPd4iIe8mnw1raBupydHydAQtBKGVvh-C-9hUZJjU3rOn14q9gF_lBBpLfVck94PrFt8Z-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=ozcH6R9oLCl_XHPT1HRQxtOTL1vYGksHE11RF6GStDyDVqGaXhS-hT-e-pwvRjxysua2AzQruCqWK2swkNUcqGM6A_rWSQ0sBnfag1jrSwjUovRhoN6SdXqkOQ7XWke93XkPuRmHBZAuZS1iBTgvWODfPEmx2AiG1McRh9zcmLK3B7GkqCUAHii-lJ27H8-ADUnfErf8iPMSlsrndKcpdS3KwbYxoMdjaRbtS2FHJEOG9pZYNwwa9-BiaoZ0aJxkc2KzZ84Ir-ZAnYQTPd4iIe8mnw1raBupydHydAQtBKGVvh-C-9hUZJjU3rOn14q9gF_lBBpLfVck94PrFt8Z-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=bNadDuZXyhE7j5l08Eh6eHUVxkSuBbjEZ5bjskHvVSHO32GVD2PvXQBfVKFmgX0y5Oo29BXcglmHfSVoBZ6kJmLkoaB8H34G1EwhGnNLDWQJy1MHgZEQ_UC7amCCykM8eGyy3dewSTJZvV1IPWZY9wv_dVJtqbuLp10dPauS12UAbtZVsvhBT1SV8DAiWdv9kt7499lbR1-cxr8RSwLngJnGCuJHizVsL0PoxtYOY_9o81EXoaltMrI9c2OgaYMslmfyYtEpOqYrz3w2-p2nQEBV8v87fcGIg8jmUfM3VDD-p32qJzfXyK-hR7QhQgpH-1AQehedZZHL3GhiUWXi8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=bNadDuZXyhE7j5l08Eh6eHUVxkSuBbjEZ5bjskHvVSHO32GVD2PvXQBfVKFmgX0y5Oo29BXcglmHfSVoBZ6kJmLkoaB8H34G1EwhGnNLDWQJy1MHgZEQ_UC7amCCykM8eGyy3dewSTJZvV1IPWZY9wv_dVJtqbuLp10dPauS12UAbtZVsvhBT1SV8DAiWdv9kt7499lbR1-cxr8RSwLngJnGCuJHizVsL0PoxtYOY_9o81EXoaltMrI9c2OgaYMslmfyYtEpOqYrz3w2-p2nQEBV8v87fcGIg8jmUfM3VDD-p32qJzfXyK-hR7QhQgpH-1AQehedZZHL3GhiUWXi8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gzmH1gUnEsrEc5NsPztP_1kUtHH0kycHsrbC4uugnzwHYqPcL1fDqg3b8AHpUWYx3XLpD4bjuQuR1zV0NMk5Sz3_XmWXIr9XU8MlOAlc3jlfhtMSfrVnXzFJSh6d2EWnOjLnKUFAYgjQQcV99hscMnYEQCDfhhYtghgM_d9egGvR3W_nbofbpsMRdiuqkbaibSv_PxsV6aa70_xjik19uyQR4w0rQOhgV7MvM4LB2jr0OKj7vubFwqLgxcWnzvx1IpTqQjaHspuBkN1c4uNssNFg33ZGgIb1p6S_mzBdkbxMK7C6SWc5p-ejkZDS4dt7xUQvK-BYn1RVrTiWvdoJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=JaJvoVcV9i1WoUc6oWftjMGWUPyDRiCDArTydOSB9Cags06IEETmBW6u-7YDKXqUPK1eyYsrrzNA7y6t9M5257t9jjjF6_4o44D84YP7NnXEbAJ1jUbeVpYLgny0o1v9FT_fMiHi7H6nnvgrhX1AV8tEVjOizhodHCxnXbW6fAg0ch2XTurQj2uNt6iEDGfvR8aOKU2c57XNHRnJPo8rRa6U7e_PevfV0pM6cj93MfW5cuKuph_wXJbMV5GXJXwN0LQtiJoepapvwIjtZJ9Yp-by8F-8pkG-7ZvT-PuFY-hj_kEeDyLHsdLlXjQg0DnKGMhH2T_6sjViMiulrALEww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=JaJvoVcV9i1WoUc6oWftjMGWUPyDRiCDArTydOSB9Cags06IEETmBW6u-7YDKXqUPK1eyYsrrzNA7y6t9M5257t9jjjF6_4o44D84YP7NnXEbAJ1jUbeVpYLgny0o1v9FT_fMiHi7H6nnvgrhX1AV8tEVjOizhodHCxnXbW6fAg0ch2XTurQj2uNt6iEDGfvR8aOKU2c57XNHRnJPo8rRa6U7e_PevfV0pM6cj93MfW5cuKuph_wXJbMV5GXJXwN0LQtiJoepapvwIjtZJ9Yp-by8F-8pkG-7ZvT-PuFY-hj_kEeDyLHsdLlXjQg0DnKGMhH2T_6sjViMiulrALEww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=JuHA6_34YrFl8YCXDRnYqJc33ZCUWt9xzlp8Un3ocWjqtkBTyA-VQfFsMPfg70K_5CdhoLxPVT97Qoyb1JTuzg7NuH3YCcPAqTXZm9YRLaObu4bjK9x4P61u6fis--2BFThdxk-q3rztIUMNwAFBcHBuIyp6KAZzWszcajPPCO41U0ZAwAkk_wpkjNHz7kpMVrmDAUAut6w-yOr2_LCQgkkoHhQw3HbMZJI7Rn42vF6Z2VDknLnO5gyZukLyu1jZJhw02FCgTGXDobTAwRZNaphG-nA1os0RpfJR0Al0T2Pq4w0Mb6IbfIrZg_CGpVzmwYSyZpFAHBRhclG3B-eN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=JuHA6_34YrFl8YCXDRnYqJc33ZCUWt9xzlp8Un3ocWjqtkBTyA-VQfFsMPfg70K_5CdhoLxPVT97Qoyb1JTuzg7NuH3YCcPAqTXZm9YRLaObu4bjK9x4P61u6fis--2BFThdxk-q3rztIUMNwAFBcHBuIyp6KAZzWszcajPPCO41U0ZAwAkk_wpkjNHz7kpMVrmDAUAut6w-yOr2_LCQgkkoHhQw3HbMZJI7Rn42vF6Z2VDknLnO5gyZukLyu1jZJhw02FCgTGXDobTAwRZNaphG-nA1os0RpfJR0Al0T2Pq4w0Mb6IbfIrZg_CGpVzmwYSyZpFAHBRhclG3B-eN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G17kvicxSW9TLwDqh_wsYgw28a8ex9wEEEjwnozUrMA3In2Z-u-eEid8ot_1aUaYH9LIY6dnLcPGvAkUFAqISGZ0v9V_Qbpvknbq_M3VXmr7m4zPYXxQBM2f3ZuSAZ9enkOosISqoiLQiH-C3ysyzETNvH3coVEVYriGs1k6LabCrznTGeAbtuj_I_0_2NPj8gPye64EsE5yfk58C5Rgslna3IpERvIjed7BTH-jKKE_JC3R9VrpyQ1wuZrcWxty-XT3k97ZnEpiJ-rqPFFnXQQ23V4LR9Ih0fhvsjaybO9kFqjhtjx3qN-ZRxoxUeBgUUA0aJKDWx4jElYRIZVfuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6kGxKGsxX7Id_Jj8J5pmWZXB2yULQJ2i1tOCF1PY1Jw4b09PlWU5ZJyHITAjfHhHov_AygB09q_cx0VS9ZrSZGXjljL_jWMmiK6PHmpauuoldfIUbsJKelmm6ZMDtkAAbQs4orHHwu2L60l1X4PXtCl0CkaBFJxd_rhY_yPS3wVvNjjv_JcZiLoKmeN5YWH2Q-NU4gvLXeqaufmSw-krdqtgMDwaM1BPygyjMKteamoZBkdVed8lGkUbnSFbjFqDtVmfXvzJQKLK4s04n8ZvEBxKxY2V_mR1hO-hWdSsOSXj6W7AV6MLWBcZpJRzDa0IC6EtlPNzCOEhLAia1ScR-xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6kGxKGsxX7Id_Jj8J5pmWZXB2yULQJ2i1tOCF1PY1Jw4b09PlWU5ZJyHITAjfHhHov_AygB09q_cx0VS9ZrSZGXjljL_jWMmiK6PHmpauuoldfIUbsJKelmm6ZMDtkAAbQs4orHHwu2L60l1X4PXtCl0CkaBFJxd_rhY_yPS3wVvNjjv_JcZiLoKmeN5YWH2Q-NU4gvLXeqaufmSw-krdqtgMDwaM1BPygyjMKteamoZBkdVed8lGkUbnSFbjFqDtVmfXvzJQKLK4s04n8ZvEBxKxY2V_mR1hO-hWdSsOSXj6W7AV6MLWBcZpJRzDa0IC6EtlPNzCOEhLAia1ScR-xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
تنگه به زودی باز میشه یا ضربه شدیدی بهشون وارد میشه ک باز کنن
اونا با من مودبانه تماس گرفتن گفتن میتونیم صحبت بکنیم؟
ضربه سخت ایران تو راهه ولی قدری دردناکه نمیخام ازش استفاده بکنم
خیلی بحث هایی خوبی داریم ولی اونا نمیخان اعتراف کنن چون یکم نگرانن
شما میگین مذاکرات فوق العاده داریم ولی اونا میگن دروغ میگین
اونا میخان معامله بکنن و بشدت خواهان توافق هستن
در عرض ۴۸ ساعت خواهیم دید چه خواهد شد
قیمت نفت و گاز دیوونه وار میاد پایین چون سه شنبه مذاکرات فوق العاده داشتیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=mwlStcfmyu06dvfVOh-hr7Vz4LlRDDgXtW7IJnO1T14qsUXHNo_3beKws8bF9KbdmswUaRXq2GK3r9CfGLL7EWh78mxb-ozEbWXsYbqhrGQNA4-Y7fChWKDLiE2Pa5Ox-Fn-_geqTVPRC0EcE_MqNI6ur33PHXFR8WF17MSquiDVrqYJupoPWma5-lRnRZ297bff5hqmyDRMf-kXeaX-MbMFBewW6SuYKsy7PXJXWGFpLWOegx_vV8M1G_WLjMZo1j0xzPa44Lai7LKhtyQxPvMh8w8IV0pBL3s4JTyvvl5NHX0eIkyRG1tI-J5FUR0NU2fkj0jX-iPOGeISd4Xs3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=mwlStcfmyu06dvfVOh-hr7Vz4LlRDDgXtW7IJnO1T14qsUXHNo_3beKws8bF9KbdmswUaRXq2GK3r9CfGLL7EWh78mxb-ozEbWXsYbqhrGQNA4-Y7fChWKDLiE2Pa5Ox-Fn-_geqTVPRC0EcE_MqNI6ur33PHXFR8WF17MSquiDVrqYJupoPWma5-lRnRZ297bff5hqmyDRMf-kXeaX-MbMFBewW6SuYKsy7PXJXWGFpLWOegx_vV8M1G_WLjMZo1j0xzPa44Lai7LKhtyQxPvMh8w8IV0pBL3s4JTyvvl5NHX0eIkyRG1tI-J5FUR0NU2fkj0jX-iPOGeISd4Xs3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اینترنشنال:پزشکیان و مجتبی خامنه ای باهم دیدار داشتن و این دیدار تو یه ماشین بوده
؛
مجتبی خامنه ای صندلی عقب ماشین نشسته و تو یک مکان نامعلوم و پزشکیان صندلی جلو نشسته و حق نداشته عقب رو نگاه کنه فقط صداش رو شنیده
.
پزشکیان از مکان هم بی خبر بود فقط برده بودن ببینه اونو.
پزشکیان قرار بود از فرماندهان سپاه از جمله وحیدی بهش اعتراض بکنه که زیاد در دولت دخالت میکنه.
مجتبی اجازه مذاکرات رو بهش میگه ولی با هماهنگی سپاه پاسداران.
پزشکیان کلی مشکلات اقتصادی رو بهش میگه و میگه که اینطور بره ورشکست میشه دولت.
پزشکیان از این دیدار خسته میشه و میگه میخام مجتبی رو ببینم ولی به هیچ وجه اجازه دیدن رو بهش نمیدن.
پزشکیان که فوقش یه ساعت میشد فقط صدا می‌شنید چهره ای از مجتبی ندیده بود.
پزشکیان اصلا از این کار رضایت پیدا نمیکنه وبه رئیس دفتر اعتراض میکنه.
میگه این کار جز خورد و حقیر کردن من نتیجه ای نداره .
بدجور عصبانی میشه و جلسه خیلی کوتاه تموم میشه.
تصمیم استعفا از این جلسه شروع میشه چون پزشکیان احساس میکنه دیگه قدرتی نداره توی اداره کشور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=t1Z4Zi8k6pgifI-J1ge6Zq0sRfLMXDan0lhoML32YWBUloL9QxTjeS3HqmXYxBckUkCRNwFjbk81GT1828vWK3AE4SPt872eFUgomWTBozY06NcsgKxFWnsUam_4NATD2eKc0uMaoquD0E865opSCONW9F54tAj67gfDcMNZ1RsJ7O6FbiZhxd9fWIZH7nC9-E6_Z0Y2c9gbYSsDy2ArrE1_Zd5OTDgFetPhRtOguRNIVNInLWkRdcKo4YyDoKbIdoh0U-Kcr9jeO3tVJFTyQph17yLBAE-nV7v1XEKrTXG9g2sQc6D124ms4jvw34Akt3N7kiUMR-IAbFgsU6ZNHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=t1Z4Zi8k6pgifI-J1ge6Zq0sRfLMXDan0lhoML32YWBUloL9QxTjeS3HqmXYxBckUkCRNwFjbk81GT1828vWK3AE4SPt872eFUgomWTBozY06NcsgKxFWnsUam_4NATD2eKc0uMaoquD0E865opSCONW9F54tAj67gfDcMNZ1RsJ7O6FbiZhxd9fWIZH7nC9-E6_Z0Y2c9gbYSsDy2ArrE1_Zd5OTDgFetPhRtOguRNIVNInLWkRdcKo4YyDoKbIdoh0U-Kcr9jeO3tVJFTyQph17yLBAE-nV7v1XEKrTXG9g2sQc6D124ms4jvw34Akt3N7kiUMR-IAbFgsU6ZNHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/avZKlBPrXUfjHQsfmNMZ7A9L1cZxSxnJLGocunXQSWRMMgz3D-8OkMbxIeKfMuVxVYOg1PzSwqjSFsTydFWyNfWv6ot8nsoai3kKjcxfD4sDgs0OlhKzPQM1qqX7BQEgIipeG1uRqKjOPUyMMrbCFLF7dnDUqFzB3odjeqMjQUzC8bPRv_ZJyZpPolOhgMb7uUceqmYqGTd6fuCdArxR-Z3oYF3ZnEXtisxdLZkn7PqcVNi-elwVXreqzfeqOiOWmtpPtAdG8f8p7R38vdpqXezFlMQZHxqPneTK61bmPj-poXU2Fzvc6MGjBdGdJSNJbph-LT73oWKv21ZH4fcnJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-V0ZuZpU_n3yUfZUB6XrqcDyXYaDFhzIr2jeMXjQ5-lXW7sMKlWUbgQlGn2Xe_4yQKXhI5fJyWvl56rPjJc0mpsCEpzs__f6-w2_Y0kF3syTA1F3nNgH9MK77CIBXkhnHA45v_GAVNP89IFXEIZnXXyYwFMECPVEeLQdMA1-tLGJO_2ghaug_yfL6xSZstOeSG0MeRf5mXszGdbHJhPqldRH5X2KoMP4fHQ5azFe8bwp2TA5q_6ijB7mvgKlP_7WfzKVoyvn-KXozuVDq1t5TUjyywEfaal3BbIBUj_HxdoEZkmRz_5rZZEtqWzbVZ21iFotxpkDkn85C16X-ymbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/maCzIQiToMMD8WEh_yEaZqiq9XtIQN2CEYIoIEcfHmLadZC3lPOPvUwWY_-lFP3DHfo8DYSfe7VMiwWerh6O6b1bLLWPWMPuYtFYws1tkQgZ6-rWd80RazjSDi5aklgBevJnGFrj8rCj49g-5bL5_bOU018Yp-596CG3mL7VeN1EAxC3uRzTCn1KVA0-fnPXr3ZaQyFSfhRjjTxzyBOrbjWsPhVap6P8BIXwBoQikYFkgYyWmTp5fLeK1PdftNLhsdv-WV1VCZdjcTist2NBPT77lSoVPTNjx8MmSkkh9aqxkoXvBuKRn20nq9qfoTwbsVWXkwP40rvSCFWNPbjrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7K0MHQZwdGO5awAe7HB2A_5PizQJLXzAxhwvGyavyZc8B_KeMOAoXi2GRDA7t8PdNkvB7pjPsvF_wh8uBTC5MDHNGcg_BXD6kQGYvuR54t4mQ-Lbe14JjYRwEe1YidndIl8OZgsVKzHu-86qdgofw009-YR1yBWPkDQApV3BHoQRyEFr1i-TT1-0Uu1nSXFwn5ievLMPyeINgO0tGewaNCSkibshQS7342Cdb6whlR0nD8djqxv8UdoR3Xvd2y8jGCZFIORtYZimUNGFUOuPJv4A1oKHSsf2wEQtbd16O3YlbOibQT5EXerC-01vGQmezAMY6apdrBjT_MoSaclMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=qbH289kp9jt8w3A5x1MGPZePtyuyQe-grUYKGBNRScQphzSpcNkte19UbcuwvH8cQ3ZxAlFzXA1AXOh8ltAHxCDbJX2HYtPBOsbLhrB6UoZKggu0snjDO4WwCGTGPVpUBhPfhascekpaRkBwtG1S6JnT5Yo3afE7jeDAy1GjOQrJYZZLvTs9wfS7FjfA1i8Lkcfz_IXn78sKh-dokq0Xup0nRq5vhOfz8tO_ghjRFgxthWotZnV1k0A7uV5JZKCP6beLBURKdXYBvjElnnadADGforzv-xaV_tSrQ_pU7Y321eRBvFUzPuPUvQDd5G9DeMWocubJa22vhfEdhxv4pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=qbH289kp9jt8w3A5x1MGPZePtyuyQe-grUYKGBNRScQphzSpcNkte19UbcuwvH8cQ3ZxAlFzXA1AXOh8ltAHxCDbJX2HYtPBOsbLhrB6UoZKggu0snjDO4WwCGTGPVpUBhPfhascekpaRkBwtG1S6JnT5Yo3afE7jeDAy1GjOQrJYZZLvTs9wfS7FjfA1i8Lkcfz_IXn78sKh-dokq0Xup0nRq5vhOfz8tO_ghjRFgxthWotZnV1k0A7uV5JZKCP6beLBURKdXYBvjElnnadADGforzv-xaV_tSrQ_pU7Y321eRBvFUzPuPUvQDd5G9DeMWocubJa22vhfEdhxv4pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdT0aTKxMmDM82GrU_Af4ekpp0YN8GGc78ej7SocwTInj-DCzK-S2lbzl895w_pV-zua2cr-B9rsTV13DmCOLn0Q0LRx8i07dqjNutLosO6EupR4iQyZ1cz4VhHo2v1bDwa_EYbkgUFJRXK9f2AXliq1TgT4FvfWXfSpgPhbydgOMlzIaMu8_qA89uG3a_eROa8OjICZdmQ_8Wkk4TnsyAAD9L4vSh4-Bj26ymXP-BgjxFq0GjD93jmQEbL3jBqcfr5QPWjmzParN_fn3ZO2MvT9uOvR4iJkC7puQK8nJZh3iaF6cpWy2wUrw7tdETxL6AiUrt7jIsIdlmzt7vLDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNwWYDIgNU61mwfl-6y3TnS5liSIgDj1rDRwPD06YhU8Kb4GmqEQTlxGnpf_C7mEo2IUXLn6btDvZ0Z9E4Zd4sM3sNs6e8yGAlVxrSKo-fSxYe2aUvVEPZcJSTxrBtiwfHTB3dPoPCU75x6dlBvVtZNdvBXDBC9cODIexJvwEVIoXOw04Fislg_Nll5f2b8AgD0-eTBOMx2MN_MWRj_SGQojwoXB0MLkzdUauF9Ei8Y7XAk-A3ZBiNyFFrzgNL7Grdb0PtqPBUDuShv-UPf1ZHwL15Fx49tWuT7g0ucyITDVR0EjU9-Ac4KRDhtui4hYD-APrsyQbFLMK-XlwmKgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLRtJxYQJK0Xtloy3LQSUo2tV8FWHNmlMh883PEoIkSgSDwDNiT6nDNUaTP4YEix2yek1dmlzmFYKEjKdgL3ZDuW3MY4hgVTqCENPGOs88odqHw2A2bUq9Xw1e6ZdMWoTmIOd_hzfCM6pAVU1uT15Yt39n3N6KhFWTnr6itNbTSPojX_l0L1ySV4wtqUc4fwOPbsNg8RwUqPJP6mimmSZ_euDW4s3L04PAXpyOXaZYkdUpbyarMrWlWINO0Km098oyzkghPQIGXL3IXQlXhGPZG9ZVSESZyhEMkwi7FVqQXaP7yO1XDO369nP-Kt1J3a5vZoiR5fTI-eyn7lsRoV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=ui8P3wEM5LtsdNcX6kU9DXlDwZMZ2O9Z63knX7Q8vVIRTBpqlUapj6aWU_grS7xuvvpHbBTCyrI1ER-g08iOkhst9bjAjIfmYjKREae-M9BPcKOLA4mW1cbpinkXRPXRdoptpyRRliH8-fxdxBvcPXCbNH__XStRsj_Y77L0pjmfV1FMVTQJdGlPItm4iNcSFjQuYyCumpSSEtE0xGwZYMv1HhlLMZaETbH-XkyT3GF-3BwF0wSh3JE_JMqiiEC83bSc1FG6t8cy1Wqh9igkX9lV6FzVjWi-x-O1cyjHFHS7m8rdblC0ng_GewhS6F_OvpO99Uqdyw_axydn0FAAzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=ui8P3wEM5LtsdNcX6kU9DXlDwZMZ2O9Z63knX7Q8vVIRTBpqlUapj6aWU_grS7xuvvpHbBTCyrI1ER-g08iOkhst9bjAjIfmYjKREae-M9BPcKOLA4mW1cbpinkXRPXRdoptpyRRliH8-fxdxBvcPXCbNH__XStRsj_Y77L0pjmfV1FMVTQJdGlPItm4iNcSFjQuYyCumpSSEtE0xGwZYMv1HhlLMZaETbH-XkyT3GF-3BwF0wSh3JE_JMqiiEC83bSc1FG6t8cy1Wqh9igkX9lV6FzVjWi-x-O1cyjHFHS7m8rdblC0ng_GewhS6F_OvpO99Uqdyw_axydn0FAAzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VlDC1DGHxgIr4p5PLFnmLyY5OfW2Lki6qaCGcVzbCWbPsZZzV_6aReXByYZb1zPFBkWb9LBxdyJzqoWXTTsQQqeTSzYRhGtoVDi_rPb8wAQvzvQMep46cy5_Eg-6Max26R18907gQnjlnhcYBQpYEMXS4cOEvLbjE6DfEyuovP_5ZJ6z0MKSeT8brQB7hPXqS4eeAdO7lkgD0LlBhmWbojzkb_RE7u0-VCJ8yGqCLiN0OzAxl90CAZJnoCsv_y8cjhTtU8O1miQkXc1rPslD658TebqB6vh_uV54GU6xHMavMhAMXyPausIiijYb07K9vH2PdHg3wgqslJrO5_rDiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ms0xWXbPSSYYhnMy7Qf6mF11580i7wppc0_p9nAdL66AwXF7vNBF60sIEWGJRGcU1lKqBBxJjp9lberimox15fOVjmJqjkP3R8ftoyDlSns7jBhvIbbkqbliK61OSIQsd8jmSTX9BdRomILWmjv9SIPnvNRcKW2VsCSIXLlAX6qQ8siSDrcv0GUpt73XBwrb-srdCfUWDJLPHnPBt5a5lb6E1s_4dUUv_zKDafLyj0eLD81M3_msWPsJCCTnI6bVtU2ArqgMLf4oE5DVV36TiH-W8sTL9ClDzQbK4-AhjwcyEGOQWXMXe4nLqtA3SXLGp1j7wGHKetBYDfNa0jIMNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2DdEkUCYqHcucs3tizKLwOfyMkBPZXlRXqSTedLhJefDGISrfdV6o9FYGQcT5gY_GrZC5bMOVFabampoN2PkLHH8vmgkWZKLZeBHhgaE0qDrTCB6G4p_W0YwG5raYqnaeyNkBrXyzMlJVGvZQQMltu6Ss_oHm6QC1E6ohdqNhzWQxe6aB2obJ0EI5bVPKyYmxsbK64TgQiG-0AW3sIuLY60Ajvls-TcLXwjwSwlIgfQeInP13zf-Jmcp-NI-OUlGJIHXLVK5Hjn6w8aP7WPaRWe14c49L-KogJf_V_WtPVib7umY6MqLNvlKRmZw8EFy5KybXMwU5bwBWOS0JnuvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=Sq5tMfndEJuoeynk-t1ewgTq879ML6jDZqTgi-amcF76rHhv5IVnEB0gDNvpWWRAt8xQ2qu8-o5RjB_mfpcb4QE5Azn0_DEVsk4Mjs-XlywwLdt5q3zOtloNWaZ8u1dWzl1lhAalEDh0w51ZbUO3WXTDTZ1aHqReTa76bIyrISNhp-3000RBTiVATqAWkXtpFDzIQxEItKO8nQDd4Ysy4GvUkfH-_7qaAlIrK0DABs2ZfSIcRQ-UROzUw-7VV7DUxwCXE7VQKCozklm-BhLCsxF4A8Vf96l_p-c0aUJWyIlVi5CzRJGNL2ymZy1z1qOZn9P6vw8k2aqSDRn2nvAMQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=Sq5tMfndEJuoeynk-t1ewgTq879ML6jDZqTgi-amcF76rHhv5IVnEB0gDNvpWWRAt8xQ2qu8-o5RjB_mfpcb4QE5Azn0_DEVsk4Mjs-XlywwLdt5q3zOtloNWaZ8u1dWzl1lhAalEDh0w51ZbUO3WXTDTZ1aHqReTa76bIyrISNhp-3000RBTiVATqAWkXtpFDzIQxEItKO8nQDd4Ysy4GvUkfH-_7qaAlIrK0DABs2ZfSIcRQ-UROzUw-7VV7DUxwCXE7VQKCozklm-BhLCsxF4A8Vf96l_p-c0aUJWyIlVi5CzRJGNL2ymZy1z1qOZn9P6vw8k2aqSDRn2nvAMQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=KiiFsfk-YRWMHkTmCmvJ-LrcyVAiNnP0voTqIlIKrES5tQIqb0SVHN-Ras-Ji_ZabPF7KDH8S3B_vGkB9iUXbTSQLRXnqSwlIMXHofoG4Piolo7thyx1fhBXd6EPaD5vupT0b-2Ev_r8y--DJvyN5CWS1E9FRS0P1YIIiw2OW1By1BM2VyISA9F2T399kRYkX9XGVe6RGdS1X-5yf8HYGv3SWYBEK2okem_7PPi4IeuhkmvY99STtdSIXFYu6gD-V-yJ59J0tU9xSpexwGGVS3SUBQjViQjcF7jRoMy293dTkNBpJOsRlGC-p-Bt9WTGATcibZCeUH-1NGwdcFOn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=KiiFsfk-YRWMHkTmCmvJ-LrcyVAiNnP0voTqIlIKrES5tQIqb0SVHN-Ras-Ji_ZabPF7KDH8S3B_vGkB9iUXbTSQLRXnqSwlIMXHofoG4Piolo7thyx1fhBXd6EPaD5vupT0b-2Ev_r8y--DJvyN5CWS1E9FRS0P1YIIiw2OW1By1BM2VyISA9F2T399kRYkX9XGVe6RGdS1X-5yf8HYGv3SWYBEK2okem_7PPi4IeuhkmvY99STtdSIXFYu6gD-V-yJ59J0tU9xSpexwGGVS3SUBQjViQjcF7jRoMy293dTkNBpJOsRlGC-p-Bt9WTGATcibZCeUH-1NGwdcFOn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=cUxDW3CXt9XZ4YH3o8mHWiyrNtRtp7o62oPA6M0Sz5GDix0KPIm-InXXI_PFDwPyPXdb9dilGHQWryK-w_FtcHRVjtmZuDIPVj4ApLlHjYZ3UcX8rRY2Z0jICUb1IQYM-w3jfrbDLSLQnNTbFLZd017iVnMxXMZc4MXYgSdfOZAe5fu-bbBaDiDDPGFT7CDuvks7lXVgmffZxwUmo2YT8wHZJeZ8Arh9nLR9Nksbtk42V-K9iR3vWXGrifHj09U25047d0j1k-CWLidnmypMMU0V8FyTlj5b7rhmxXtqa85awV5vocmcohaGHENQnG6OP0I-OnolhDMmSpRlsTR-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=cUxDW3CXt9XZ4YH3o8mHWiyrNtRtp7o62oPA6M0Sz5GDix0KPIm-InXXI_PFDwPyPXdb9dilGHQWryK-w_FtcHRVjtmZuDIPVj4ApLlHjYZ3UcX8rRY2Z0jICUb1IQYM-w3jfrbDLSLQnNTbFLZd017iVnMxXMZc4MXYgSdfOZAe5fu-bbBaDiDDPGFT7CDuvks7lXVgmffZxwUmo2YT8wHZJeZ8Arh9nLR9Nksbtk42V-K9iR3vWXGrifHj09U25047d0j1k-CWLidnmypMMU0V8FyTlj5b7rhmxXtqa85awV5vocmcohaGHENQnG6OP0I-OnolhDMmSpRlsTR-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLINKqjnO9fVEt4rK5DHnLFR7OCJ2JWSxJjdx_FyKtK1XmK6QW4nRHcu8rFmAskS16CoNQnikzW8XIeV0tK_oVhlTBnxIJq-TGyD1RhV2zQ265HDPNkCPmwYvn7i8MqwERsV2JnC38pFpM3y2uIhxTQH3KthmKej_6ZS4g8HKT5tsi_frod51kEIbdTD0CiiGFM8uH2y1cJLr1h8KLvu2f-MepZcEfxPoCi2OQT267dxrGXo1nUPAO1w9yeS-ZXulj2qvHMPhtVZpclDuVBMjXQjp5TaqvNgiugcLJyNoothdChsQqfwslcGwVwzu85-Y79kseVsDSQ3jaBOkUdRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPZVaunjat3JbXTHB7un8zFRhelG-jPfTH6IGXZjjHHXd_od01yA6xfS3kGBfeNe-OX18ca_DHbNGrM0bC8zN1bTmBsm_Tu7JNnvtaRnkvTPObwxzyvHfltDSjQymqEXGAG-RIv2_ogJiwHpxDnFO-xUiA5qxz9Ii5BEQuNxcPKCx5n2VnTu2q9P_qHXpjU0A58AtpVgvFkGdg4dmWUJkyi3uhf1l3D6muvT749HKAndjZmzONDV2tKlbXRO2hpKHtmBFIqT8Ptf_hf7ilTvALQIVPkXRRVH5-vUR3elBD5pEjaJQQ5eZUK32dfBMZY8xmnpoOVdDCDjKXRQJMZKQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=iFkwes36CcaYUV7WVLRXYe4bOz4BK1NosdGw7iN2wrGlA2Z22eGHXGmgYwBI7T_EwG0VgBhWEoV7uKrySun9FdOepUGko8wZB5WdotYeng5jZAx9GCy5U0z9dHr0puWJ9SYK66SI7f4hejFj2iwUOhHoMj7jgYkBD_t0RFw5arw9ALfnHmxXNkXdwOSZaXJPDrnUteuNkZ882u2LCm_r9SZpJMFbUq2sGuVul0Ynhj5TBb_H7IzKDN3gWrtx5BcmF-A-Te-tZyvkeNGsTiqOs9wP2CcAV1dx6YZyG-c0FC7j9XVqYjhUBsiJATxw4_AIThBuw5ijXjpOe7qlgyeKkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=iFkwes36CcaYUV7WVLRXYe4bOz4BK1NosdGw7iN2wrGlA2Z22eGHXGmgYwBI7T_EwG0VgBhWEoV7uKrySun9FdOepUGko8wZB5WdotYeng5jZAx9GCy5U0z9dHr0puWJ9SYK66SI7f4hejFj2iwUOhHoMj7jgYkBD_t0RFw5arw9ALfnHmxXNkXdwOSZaXJPDrnUteuNkZ882u2LCm_r9SZpJMFbUq2sGuVul0Ynhj5TBb_H7IzKDN3gWrtx5BcmF-A-Te-tZyvkeNGsTiqOs9wP2CcAV1dx6YZyG-c0FC7j9XVqYjhUBsiJATxw4_AIThBuw5ijXjpOe7qlgyeKkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANHSmF0RoDDek0HRVp-P42l-naPVepCRElZAkKM8WCDoOMwNEg86ah5O3-MFppgrJgVLh6qLrvd_abKxys7OxRgWZ8QXuPsMCRrCwH_K8ulXlK9aOUnFypCrwBlWAE5KtZh7z4_lA2ABJEyMLGzOJz1_sUe-XUdGRNGXs_ibumtX8_rYHJZpZshMohw7HmPBo6zBiVgQL3sMR4V-6WeWkXwilbxzwv_WTDfyiZpaAOj-lQEySicQGFmhn0mchmjFR5GRKhaYHxyWamyw1gFIoKYDAtjx5CZ4WOSFwA75rjA_0seVSwp0kN63znyfztTRqC8FrWlRLyHZNwSVPXHSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=FYP1C566zyuQNEmtfXGIk8SJ27323dmcaEI2ve12bu6Mj0Rno5XqDZ0asdig5aoR24CVo3PFn04VNIAzV9ycI7eWecBrctcJ5P__Gf-g9MYGcAc_NrT6kkOB5beRFbP56kcA0v0bp6LjWINXepb1hqy_dkWHEMsXVstlhz_tJuymg2uqdqhOwDkuaqMlQAfqhodxwD4Pm6h5b6bBsYzFTVQv-TxOMf1mPaaV82hGzGnsWqWnn_BiZ_RlMT6seU1nNblpbmecAyZMRCOO0OXJr5N8eCOrgu9IsLuVC9MhrqS19bjiahgePBdh15TiR7-Y6wY3eb9Qrq43Jks-c-4vKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=FYP1C566zyuQNEmtfXGIk8SJ27323dmcaEI2ve12bu6Mj0Rno5XqDZ0asdig5aoR24CVo3PFn04VNIAzV9ycI7eWecBrctcJ5P__Gf-g9MYGcAc_NrT6kkOB5beRFbP56kcA0v0bp6LjWINXepb1hqy_dkWHEMsXVstlhz_tJuymg2uqdqhOwDkuaqMlQAfqhodxwD4Pm6h5b6bBsYzFTVQv-TxOMf1mPaaV82hGzGnsWqWnn_BiZ_RlMT6seU1nNblpbmecAyZMRCOO0OXJr5N8eCOrgu9IsLuVC9MhrqS19bjiahgePBdh15TiR7-Y6wY3eb9Qrq43Jks-c-4vKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukrhoMK0zzwjsCJHKe8fzGLdftt1foyrs32Vn8OPLwnJWnyyGiwIxddZAIg5c7iEJSwl6VrpHV6zUp1BC0sftf7xKU7UQzmvk97PS1txLNzhvSmG3ZXgQFraEQ7RgKVpCwefh6u1lachUbXcxz1nw9SJMiwe5c-1KHl4Fo8l6_HWD_0_E3XkoqY8GEZCJVerkHNYj0UqFfYjHfdfXrND5_14p4DVHLtyzFEaQA5lXeo7IeOo2C4WfiyEhrorkBz16ovR-gseYEHF48IO6P2OKpzWAzG-OoA46Bzv_4yl72Nfw24fCAT32LFmTshi5M6hlP2XSxz2WUQWZQk4EhKRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=hXHZIKQhyknSwrMjNGi6JE7RmdVFmiGySKZccsPAdtcENNm28etKwV-qPZxVrLhC594TugvhyLe_KRxl_lcJfpOWgwTbVXb_B7zYZtvJGuCt0H4dg27v-GcctnegL95mecCZv9xQAoEJ5lL6Dspyv5_NKMQAcPJc88KV7u5gpF-UY144aRT6UYd0aU3DRwKjeJvkUyTO0EpIK2vItEhxplDPcFlN_i5z-teRjem8mmTHKm1LwamcI8kpHgr2bXZfQZV0Pef_i40SpDpWoyh496AKuvltgfuyBi8NriofDtm0ijnd3joDjzjJ3iW2qWr0REWhcHUrBMFhHLeHSlZEEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=hXHZIKQhyknSwrMjNGi6JE7RmdVFmiGySKZccsPAdtcENNm28etKwV-qPZxVrLhC594TugvhyLe_KRxl_lcJfpOWgwTbVXb_B7zYZtvJGuCt0H4dg27v-GcctnegL95mecCZv9xQAoEJ5lL6Dspyv5_NKMQAcPJc88KV7u5gpF-UY144aRT6UYd0aU3DRwKjeJvkUyTO0EpIK2vItEhxplDPcFlN_i5z-teRjem8mmTHKm1LwamcI8kpHgr2bXZfQZV0Pef_i40SpDpWoyh496AKuvltgfuyBi8NriofDtm0ijnd3joDjzjJ3iW2qWr0REWhcHUrBMFhHLeHSlZEEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAKjG8e9ACFDh0o4yWClAZ1MrcgIN5MX1MgPWNU8toSs_15wq_mB-5EnHW7Gx80yRbauAh6dyq2sOj9lFaL1fiCFeuGWEL9t_S3dqUiqjTRQQzR9I34y8zd0hij0Wqbf2QRxfzUBnzGt0OJQx2jpu6XxPRDvK9_ZcmpQ7TYjpTtn89kLEv5O8_90XisdOfStiqFg-5X9JgugTxayJRB4bBmAMremFMii5NbhhGXJNwTyWcpfcyfJMZgkmbmXK_zEyphK_r1cr9akbR28r_TgFNEq6OxJfSAN0sefS48LyL0d7MJ_-GP4V6hoi0-edO0uqbE27qLNVQNsHhfNIUU-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=Ti4j-NEDfe-vvJqUx0SvctvFnVC0sB2TYlSspMQFdZJmmIZtjiNvnzSdRR6IRAvq_MxfonjkBkIacFksKhdfTMrZI42UKP_zwhuXNj9-fvwyD3_IL4iJpBDPfvm_U8abPzSAvPsNNm4lODvM3vnMMXhr3I2Vk_vc3dzV00t5NNHM0JFtuj80kuacJTtZKiAO_9x2OnkbgpQl_4NrBvq5iwGap3sig07ieujmzt61eTsYsdgkJTRvhNQ_qyCQoYzMO0S_qw6C5nv-Ju7MWss5gy4HugbC6DatVJgmCfTdaUxcVLLEqg8XAaO6qBn77ndxcDY2GzVmAKxr2U1e7y5g7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=Ti4j-NEDfe-vvJqUx0SvctvFnVC0sB2TYlSspMQFdZJmmIZtjiNvnzSdRR6IRAvq_MxfonjkBkIacFksKhdfTMrZI42UKP_zwhuXNj9-fvwyD3_IL4iJpBDPfvm_U8abPzSAvPsNNm4lODvM3vnMMXhr3I2Vk_vc3dzV00t5NNHM0JFtuj80kuacJTtZKiAO_9x2OnkbgpQl_4NrBvq5iwGap3sig07ieujmzt61eTsYsdgkJTRvhNQ_qyCQoYzMO0S_qw6C5nv-Ju7MWss5gy4HugbC6DatVJgmCfTdaUxcVLLEqg8XAaO6qBn77ndxcDY2GzVmAKxr2U1e7y5g7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=RciK9UyQZu2hT40zrGECpeyTxcCW5kXOPgkSlSBbi5F9KnR7gljO_tkrrIYRwLI0qVl-pFLobCB9VyxUOecFb5Gb08NfpPhtzKglrHHzz8wpGCG1iIBQ3-SE5kUms6VFUGu14QnR4mu-9Lmv4z84DpTXEHNsIy9oIejlNO0Dmn37FPYnhKK9EnJFpmbYlJHqje4vvBbUErGhbTpjWJUMWAM-tBGGc9E0VQUbKQrdgJbnY-QfJNz9jYFTF5phIOl2DX5exg6X1QRzItOjD03T7ydaulMwHVC0_nOAaSdxAANi1hgh6zjHwdxWtMAn36jHCXJ04Se7m7uFuVJkih9YxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=RciK9UyQZu2hT40zrGECpeyTxcCW5kXOPgkSlSBbi5F9KnR7gljO_tkrrIYRwLI0qVl-pFLobCB9VyxUOecFb5Gb08NfpPhtzKglrHHzz8wpGCG1iIBQ3-SE5kUms6VFUGu14QnR4mu-9Lmv4z84DpTXEHNsIy9oIejlNO0Dmn37FPYnhKK9EnJFpmbYlJHqje4vvBbUErGhbTpjWJUMWAM-tBGGc9E0VQUbKQrdgJbnY-QfJNz9jYFTF5phIOl2DX5exg6X1QRzItOjD03T7ydaulMwHVC0_nOAaSdxAANi1hgh6zjHwdxWtMAn36jHCXJ04Se7m7uFuVJkih9YxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLGOWP14NMJxDNIskQanQNIRuwoV05wWYvJaoqJ464DZ1NaevA6IMI8xjAvpKQyli1u_x2Fzz7dbxFdRTIdlCOj539C6bgthzjXcUMgxFiEJmr9rPIKES-zBNAhxY8xAQaJm-G-iWQWN0bVfR6eb-7m1-HqrrxhNBmGmKRfM5SJkoOpxPlpm17jz-UTCI24MKHBrwkkU7CN9vClQZElbhugq0m9A2D3At4jrnnnU_5_YQA2Wf6atfuQF2WDBPrXM0gqno3LMBTQ7pZJxNnTe-YmZFDRGHaRaOd0FpizhtngtKA647D6PONW5qR4loxN3O_81iY5RmGGXrE1q_06OFiY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLGOWP14NMJxDNIskQanQNIRuwoV05wWYvJaoqJ464DZ1NaevA6IMI8xjAvpKQyli1u_x2Fzz7dbxFdRTIdlCOj539C6bgthzjXcUMgxFiEJmr9rPIKES-zBNAhxY8xAQaJm-G-iWQWN0bVfR6eb-7m1-HqrrxhNBmGmKRfM5SJkoOpxPlpm17jz-UTCI24MKHBrwkkU7CN9vClQZElbhugq0m9A2D3At4jrnnnU_5_YQA2Wf6atfuQF2WDBPrXM0gqno3LMBTQ7pZJxNnTe-YmZFDRGHaRaOd0FpizhtngtKA647D6PONW5qR4loxN3O_81iY5RmGGXrE1q_06OFiY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=dRLTVp3aOrb7_wOYpFOlQU1tyOXxL8_yuc817z3QGrQeKNzbVN0lt7jHGtsf6ppe758o3vzxLmzsrs-ToWU6uimQSlG3Q1bIkz2-u8ikR2x0H9_0Oya730pYvpYrZp8k4iiEVNNA5gTwTlpbsnzzW69uqfOXvISXe2UxpKO6zOc02YDBwCp1Bto4XhcFXPqd152ZzHo4vm3BatmiKu3bybn4qwMSEHM30e2ZfaFzogJ37k1xT9mChMCVq2uHJRwBEsV9FUw5Ek5QkaXIJkUjieaAiegCyWfkHX9jjDnE7-SSNpqLLRiOmBcR77ZNKXhRK987s-av_7dOpeqw091q2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=dRLTVp3aOrb7_wOYpFOlQU1tyOXxL8_yuc817z3QGrQeKNzbVN0lt7jHGtsf6ppe758o3vzxLmzsrs-ToWU6uimQSlG3Q1bIkz2-u8ikR2x0H9_0Oya730pYvpYrZp8k4iiEVNNA5gTwTlpbsnzzW69uqfOXvISXe2UxpKO6zOc02YDBwCp1Bto4XhcFXPqd152ZzHo4vm3BatmiKu3bybn4qwMSEHM30e2ZfaFzogJ37k1xT9mChMCVq2uHJRwBEsV9FUw5Ek5QkaXIJkUjieaAiegCyWfkHX9jjDnE7-SSNpqLLRiOmBcR77ZNKXhRK987s-av_7dOpeqw091q2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=lnQT3w6Df_k8E3Zv5l9gMGVCQmVdzTqJQbB_Ioljtr7VXPY2XRRrR3DXD17vZuoKpb2_8CyJhti9VdG-NOMbBFjksiGWpmPBZt1NJetPt9DI5SUvdHAjTBu481D-bd7V6RMNVv-AEPu_JYNMp65r8MdCN5Y-Y1QInIbqJ_obnQ2M8UFHjEE64Bi44jqKz-g89FRRURYlLB3PeMCJR4LZAHNTvjqil7GpS5eMiQXoPT0Weu3tZazF7foAxgH54oZrELsYLCZeS6IrHIe89ZMs6tttXY-o5bf3SxtGbhDllbsesW0U1XxjfvEKFFZxkxYoNq1l-R6lRLFnLtwCzDnoJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=lnQT3w6Df_k8E3Zv5l9gMGVCQmVdzTqJQbB_Ioljtr7VXPY2XRRrR3DXD17vZuoKpb2_8CyJhti9VdG-NOMbBFjksiGWpmPBZt1NJetPt9DI5SUvdHAjTBu481D-bd7V6RMNVv-AEPu_JYNMp65r8MdCN5Y-Y1QInIbqJ_obnQ2M8UFHjEE64Bi44jqKz-g89FRRURYlLB3PeMCJR4LZAHNTvjqil7GpS5eMiQXoPT0Weu3tZazF7foAxgH54oZrELsYLCZeS6IrHIe89ZMs6tttXY-o5bf3SxtGbhDllbsesW0U1XxjfvEKFFZxkxYoNq1l-R6lRLFnLtwCzDnoJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3-jouFhq0nro58evbq-YGqf1cFpp8TaAte1ZEPE0qY1Bs-CHPokL-JIhoAPmJ_1BRTOSs43BXJRKuhc_7jcPWbWvqkTzItY9-nQSJQWBAlZ1ZPDXl0opkWVNQcZCOcsOlKwu_SAtz7V1kbHAISYzIhr6rIEt_-WE88gtSAVFjd0flpoj6oHGIRLh4Ew3dsF7039hJSfAczHP7cY-kIXiWUgK5RNVM8fn7nxVyWuxq3NmnyeG_m6lNW28Ey6pVOkZ1D89Q04spigtnnhU-Wf-0o5VNTWsNcDQDNvF9Qr-bH_xUxWFUavOX1lY42ZoLc4noNqYjwnDSLUNCJLQyCK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi5veOyJdZLhRmn9ibiHF4pHe_AAH4_ODWdwn_kxpZQKyRNiUf2PkN9qAN-U8fv8z5XVrtsmjM11WFr2U-Zo6sXY_5MFu6QsXpoQfhQsFDHCEftXh2dniUtpGw-Z9tTxrNo5g87xqq8WhSJJ5wIIQwga_BXHC8mf-u1bVgpZEVOqW8lKQx2bXJHnr5SQiwAz8Jg2akGzb2BoXAL-hG7XiRlW1HhL4pUTdxCWBouBbdxr0JYEhYwVbeSO_hwNSF9mzjC4KpTj_gyELlmJj4p7WfX6v7MwhhCnXpQHqVDG7VY0FUUTy1TeDxGJ3dOaOO2eYPZYJ0NLIgrJQf-N-1mFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=FNQaJWZ7rLCHrdagJGfv3U7NQU6ZcwGbNZUb0hCeXDz_xELAeD1ip_KqEP12nmH99z-38Z2KaqKsExwzEQH3XDFMOopTbGWiTDEl3SNbLD_gpsHay_-Fkf-ejC6AP5x0URcbGBVsmrhnwfU7L58cf757lP1cUL2fOeMnTJ_48aOI5nidfjSQRB4sp3gHDcMpC78DpaK-OwMQpWFwQE1TaSo-eupIXMuZVE4FS-mD7oBsssuVObzm6bsE7d9VYHilkSPUyNPrZikmb0TdVqRF5zuiT7RPPumayOT8v7m_AKmiDKSXu-0e4EheZ7JVwzj89LejrxfAr3U_PLpe4FetwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=FNQaJWZ7rLCHrdagJGfv3U7NQU6ZcwGbNZUb0hCeXDz_xELAeD1ip_KqEP12nmH99z-38Z2KaqKsExwzEQH3XDFMOopTbGWiTDEl3SNbLD_gpsHay_-Fkf-ejC6AP5x0URcbGBVsmrhnwfU7L58cf757lP1cUL2fOeMnTJ_48aOI5nidfjSQRB4sp3gHDcMpC78DpaK-OwMQpWFwQE1TaSo-eupIXMuZVE4FS-mD7oBsssuVObzm6bsE7d9VYHilkSPUyNPrZikmb0TdVqRF5zuiT7RPPumayOT8v7m_AKmiDKSXu-0e4EheZ7JVwzj89LejrxfAr3U_PLpe4FetwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnUUGKAkfAhicTNtl9x3YbbB02eHn7Ya7MhB9RmrM9CBoga3OJ5D2GYKsfPVU6-p677eMPROvdwZ68zjnovgLvCV3Jt_UiAuzNi6D3iUl2gOixziRrBuVpg1YcPi3R2eHevJ8zGvLWo85KZXNcBLiIrVoVfAomdW24aRmsnSdYrSyS72Xxj1EqPQRowWWm7BgqEZTP9ii2d6jYQYYI7A994bt0AI0AYPxqQmZPYfQRJpPSvINoVm0QdMS4ZedI83jZfTgCLMeErYDgro1Do3lABIo4NDkPkjeT1k2SMMKHbtbadvWwS167t5ez_QXvyLJqWX3u1EACvcODoF1G1PQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NKW--d0ZQx0Ust-Zmjvn1iITjHWawL5mJ3Pf_euEDKFi4xZfsc9Hpi-Pn0iRrlbR-kOPd83NAfUWEXdzPthxrB3Ed7dK0RqdeRK71xL5UOxxY2ifWbza0AXorSD2BwXWMyZWSVGUTs4urMx_YMVdAyLcQycWWZeQLlfjM0jFKvzgTkZd1xRfpNojz2C3WIp2BAAJF2-0339pBi40_QQUIb3LoH684MFpHnVTSx_B0bgBDLStK_HpdJJJd_EP63wW5rL3rih6iJirTtpGWl6UWfDvr6evph12flHh5Jtd-cXhMEeqELVlGzAWG-0F9cNPnqTMlgkLCGYtY8Dhi93g0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RIo5kj8MJ6jbrkiJph4c3aTuAy7PKN2DOAsi5e6_mxYyFJ-gQeVmfdwat2yQY24K603ZKwVQiywymdyTmN0ytWhHxkUsfBhJlR-JCXPOnKmrSgmDCYUK5xOkK9Mk7nHornAl4ZGCs9hb33807aF1iHwbO3N46zqvJJXedCfJX7lyegsztkfG-pU_tjVKoUmvWnKhIwVzgy-73_b8rkg-kTJWJKHCZHFGI-oXsnudn5hlbG7k7vcVrxrRXGWGR3IUVv3bbgzaHab5JsXbRiQIeD5ieU4EcGRPTtKxE01UTUEVPtlcN4lAiCk6GqGfEMhUEKlcbAPgnQ91GIdMPq8O8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkF8zp8Vi0rAi2jChwX63ffJVBSIB1QS2q6Jc3yHNDM8bJoLhnyIiFmwhoSFjYYKFdyeQKEMpDpK16uBJTt5lGuP8EmzdFeBEFDoCDfHOgDaKj00L1SxVQbMifvwp1y-DizZkQk8dNsXRRmKWpP0FmWlKxsr-ELVan1SU1ewn99Dp0KVDMsMdwt4jvm2YUEbAnpF-i51bWc7thChl5engEP0UHurSM1qkogYkY1gfqz-yUdh_5n0d7d16Dv9Rx9YT_FoCc5PxR5UHxOOpXInmv90F7FvgUhVu_521UYlywmBWA3ofmRTO3J7BoyWkiu_-MOBfk0yqksqBbgLMvzKeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tt2aTNKt4rFLgBiY6Pza0uRb-e5gtaAwjllYjIuWe0aWWwKnFF5TJyghsrS4tbmoqwxNRvz3hkIMFbQiDrXgjyDZR9xElTrpTV0kUDpqxEBxZyrowS_0gpDe4auxwINdEf8DKJo9ckQ3svOTUlb6kFXvDAQm577YfgSzwXBXYIs_2VKRIesEQg2aI7nc6KGZ1NPjQ0pLX4s0AbP_MfGzEi_Pm970kvwsYvh9if9gALNcBY9ZST_PgpvDU6kD-nv4tfjH959382GssZivDU9vY9UnZkJ8PS4QvilUMJiHB-PMycIFjFZxA7tvgG95iDtfuhROKuC_ZF7zT3Uk7kwJpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=EM1d46wfOIUV2NIT-HNCZT5h5qbidQWxpAa07VElJYWebnDueunBrJzHmBKD6ImtUTUSt_UVOjmuyLqRd13zogzeZFJtPQf9HBF1ASXT_0B6gyyHmn18ZfpHGaPnmCgShDp2L2iFEF84IBDedX5ZnMyNYoU92UAbgWmtHFPmnpDi68P0SYckSwa4RRLmXzcLD7_NSejhrTsQF0BsOdX37-veEE-sD2eHWfa8rV6os-UNitzY9W-b7UKx-kUi2EXdVlsDRs5AbeIxJgqaI1e1QkSFZ379DgsiqfkCEWzNoR-pkfbqOGBBZWYhj2Awj7fOexI8NAFEpaVOr2w3mAHl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=EM1d46wfOIUV2NIT-HNCZT5h5qbidQWxpAa07VElJYWebnDueunBrJzHmBKD6ImtUTUSt_UVOjmuyLqRd13zogzeZFJtPQf9HBF1ASXT_0B6gyyHmn18ZfpHGaPnmCgShDp2L2iFEF84IBDedX5ZnMyNYoU92UAbgWmtHFPmnpDi68P0SYckSwa4RRLmXzcLD7_NSejhrTsQF0BsOdX37-veEE-sD2eHWfa8rV6os-UNitzY9W-b7UKx-kUi2EXdVlsDRs5AbeIxJgqaI1e1QkSFZ379DgsiqfkCEWzNoR-pkfbqOGBBZWYhj2Awj7fOexI8NAFEpaVOr2w3mAHl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=oJIr01x79AJhx5m82A5H_oiWlz7L2foVJk4V8ofoajrSH7DVHpBm3nQ6akCaPvkH9xdtzkftTgYcpsdaQlVAmyIOrCkXFNJGJudgOkVStkYjsJyw-7Y32umu66RqrPCxz7Av_cLpafLtGBiLe8fcYqpYQ-gOG5zurbvo98WZdaDVQvC4vKmuuA5qo2jh0GWo3gTr7fqfn-VeXNQdtlEqWCYFBG2l98DV3EtQ6qWtmROjL4uASmzH-Xr3VwELGacAzHMZHddJoYXScHcj8bd9Xo48mrw4RTAiIY1CQuXFRlDPQCmGUVXmyL7QSmuqvphVjS7NidkAiv3Sy7nmTiUbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=oJIr01x79AJhx5m82A5H_oiWlz7L2foVJk4V8ofoajrSH7DVHpBm3nQ6akCaPvkH9xdtzkftTgYcpsdaQlVAmyIOrCkXFNJGJudgOkVStkYjsJyw-7Y32umu66RqrPCxz7Av_cLpafLtGBiLe8fcYqpYQ-gOG5zurbvo98WZdaDVQvC4vKmuuA5qo2jh0GWo3gTr7fqfn-VeXNQdtlEqWCYFBG2l98DV3EtQ6qWtmROjL4uASmzH-Xr3VwELGacAzHMZHddJoYXScHcj8bd9Xo48mrw4RTAiIY1CQuXFRlDPQCmGUVXmyL7QSmuqvphVjS7NidkAiv3Sy7nmTiUbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=d-hFENatia2vW59RhlQL2WgFQqcXIlTJqmvt6Mqy6w0J_6IlHWarwxZyop5dh5DSlcD3nt6m_bHLMtSCRVlIqrh-Ye6s2OmPOitPVDquXXb3zkGeHhKXhtX4SPNu6RR4zQcOB7puOXFrVEbTNuiCfwSGnRE8s3LMXvbQWT7pFZBk-FUXcSml4FSA76PSJEqPu9IQxXNpSsCxUKPh2AGoNvhQ4d2HMXa5yN1sfxxbEeXEXv4gxd2YW9l-336raFXcXVUjQa1Y78Djfy-wCjdNyxvHiguDnNgCA507c3GrCBiVYx2xewTBddL_g1JQEnDi0y5pjLh8aHzEVuPDUamVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=d-hFENatia2vW59RhlQL2WgFQqcXIlTJqmvt6Mqy6w0J_6IlHWarwxZyop5dh5DSlcD3nt6m_bHLMtSCRVlIqrh-Ye6s2OmPOitPVDquXXb3zkGeHhKXhtX4SPNu6RR4zQcOB7puOXFrVEbTNuiCfwSGnRE8s3LMXvbQWT7pFZBk-FUXcSml4FSA76PSJEqPu9IQxXNpSsCxUKPh2AGoNvhQ4d2HMXa5yN1sfxxbEeXEXv4gxd2YW9l-336raFXcXVUjQa1Y78Djfy-wCjdNyxvHiguDnNgCA507c3GrCBiVYx2xewTBddL_g1JQEnDi0y5pjLh8aHzEVuPDUamVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu1gZXsnrWJLSK8-D8zIWdoYRAP8XT8JDhIsAdKqwdZ8VVu5h_SwrAXqxs_Z5PxnyLqUQqSq31yPvnvXZBdPO8x2sOeKwBa5INIqHY0ZFvodLLBZZwrryk_6Fho3uJm1kFfmEjuFsdOBVv3oV0uk4Eu8tSl7a4dNMhKGHZ_rhkUmGYuHYzRgKzcIK0AwT_QzZHeNiEVmnD8GM27TBnIeUaLZ8SfYjUhxD3KYhcYchdchI_dQ9EIQik9LTY_uwOoSA3qVbBUFoLNteQJo9ElK3R7nYb2_pmpKkDgwVoNdIJHjMTn73ZNTdZB5xqIIWWqmo-S_-g-bDLm7t9VPH1oUirdo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXu1gZXsnrWJLSK8-D8zIWdoYRAP8XT8JDhIsAdKqwdZ8VVu5h_SwrAXqxs_Z5PxnyLqUQqSq31yPvnvXZBdPO8x2sOeKwBa5INIqHY0ZFvodLLBZZwrryk_6Fho3uJm1kFfmEjuFsdOBVv3oV0uk4Eu8tSl7a4dNMhKGHZ_rhkUmGYuHYzRgKzcIK0AwT_QzZHeNiEVmnD8GM27TBnIeUaLZ8SfYjUhxD3KYhcYchdchI_dQ9EIQik9LTY_uwOoSA3qVbBUFoLNteQJo9ElK3R7nYb2_pmpKkDgwVoNdIJHjMTn73ZNTdZB5xqIIWWqmo-S_-g-bDLm7t9VPH1oUirdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=OE1Rn2rznlbmXZ2soeGniVPCuwtC_bFPoC0A0pVETItwjkcd4iYSxY2WhLWDKE3bokblL7MxcOvJFeYHgUuXDmshNsocN9buHcB3tqqXCRAsr4OItmwHSFZ6EfNihfUnARtIYftEL9zFm4HKtri3Si55FyCSomLgD88EUWJmVj3Df6JVcUJdPHy1pmrtRkSZ7tCPds0HCPHCL0QBUNMVy8DbavHXcpJXAFZx8AQUQWxXcuvPOTgD2hxgUuNvzIStjHXuROD8zGcBmFT9PmofQAIyIiOBZUlzqjUTlYG9zQPoAd7Bo-MfC-us1wkKvbQjF6J7tN_lypfM_k2zOUEc3ipC0hGX3At6obd3vT4i92VbGpNQuwY3IASFAsW3d-sRqkqlHZ4gsZGGIC3W1s9xFXCbGqzkAFN1ZybIFBZ5mpjUaACBctNCri-946v3HEIWI__h7bYAzeYBm-mjCEa4iqhAvCnmZrBs4qSF7LobSGSZSjrNDKCbwbeFyvownN53uX6PyuS9z22hf89Ik0DKgQt6MDuRtaEaQEEXLRmMzD9WGHCWPHlIuot0HVY9t5d13_0njKy7MtYsXpQaok5ipORnDNcS5b8kz96J602Rs8iTZsXEuK0swe0WQTlvy9pTe29Hk1VNXtTuO9Vq-lSbTIxRuDgi7fu87xfZgeAHs5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=OE1Rn2rznlbmXZ2soeGniVPCuwtC_bFPoC0A0pVETItwjkcd4iYSxY2WhLWDKE3bokblL7MxcOvJFeYHgUuXDmshNsocN9buHcB3tqqXCRAsr4OItmwHSFZ6EfNihfUnARtIYftEL9zFm4HKtri3Si55FyCSomLgD88EUWJmVj3Df6JVcUJdPHy1pmrtRkSZ7tCPds0HCPHCL0QBUNMVy8DbavHXcpJXAFZx8AQUQWxXcuvPOTgD2hxgUuNvzIStjHXuROD8zGcBmFT9PmofQAIyIiOBZUlzqjUTlYG9zQPoAd7Bo-MfC-us1wkKvbQjF6J7tN_lypfM_k2zOUEc3ipC0hGX3At6obd3vT4i92VbGpNQuwY3IASFAsW3d-sRqkqlHZ4gsZGGIC3W1s9xFXCbGqzkAFN1ZybIFBZ5mpjUaACBctNCri-946v3HEIWI__h7bYAzeYBm-mjCEa4iqhAvCnmZrBs4qSF7LobSGSZSjrNDKCbwbeFyvownN53uX6PyuS9z22hf89Ik0DKgQt6MDuRtaEaQEEXLRmMzD9WGHCWPHlIuot0HVY9t5d13_0njKy7MtYsXpQaok5ipORnDNcS5b8kz96J602Rs8iTZsXEuK0swe0WQTlvy9pTe29Hk1VNXtTuO9Vq-lSbTIxRuDgi7fu87xfZgeAHs5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=YzCxn6748ZzVQV8MIT5EWsNb20eXQUGHvGsQR_rTUv4fdik62-lnGVBWx0M0zKYAJORTKayDs63duyHA3CZYtxOrZ8ji6YlHbeMdp2wRFPXjFd5zqkMy7XDkbEBH5QW9YZJFoFDM40L3qUY2rHDzMtZxQgFeJ90RuHXsDNhYOPg1pv3Z2tjL_-t-sqwTeq-zXBC1-jQFTy6fArZvj9lKUG7xBcHeDwWE7DThgsopLtaDeQRa_hHRXolyx2dRAEUlADl1Xa5IrCq8weenV2DAHVMi88KanYvCfwVdda62JMUzC_hgdtYfqcTMxQYLfVaUPtJmZWhYX3vOsmqtwip43Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=YzCxn6748ZzVQV8MIT5EWsNb20eXQUGHvGsQR_rTUv4fdik62-lnGVBWx0M0zKYAJORTKayDs63duyHA3CZYtxOrZ8ji6YlHbeMdp2wRFPXjFd5zqkMy7XDkbEBH5QW9YZJFoFDM40L3qUY2rHDzMtZxQgFeJ90RuHXsDNhYOPg1pv3Z2tjL_-t-sqwTeq-zXBC1-jQFTy6fArZvj9lKUG7xBcHeDwWE7DThgsopLtaDeQRa_hHRXolyx2dRAEUlADl1Xa5IrCq8weenV2DAHVMi88KanYvCfwVdda62JMUzC_hgdtYfqcTMxQYLfVaUPtJmZWhYX3vOsmqtwip43Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
