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
<img src="https://cdn4.telesco.pe/file/Ml7TZqxbaiyyDsI-0ITTrK0lpT59cTsxjXnDQHGIjjpeEZ1cYn78JwS_B2gN7Virv6MT1fnrXY2duJxqYAqXYpXCSS2ZTJAr8VIyXcXkZzh4E9kSHEXApyMAqi6xnPB_CvbIBM3VPcAacmKlCVVgyb2XRSCx856OtAeUJZ9VJvJ9ZoUplQUUMU42_bGVlcHyt-HEC71SUox-xU6HBWtUBjkKptXr0BXs24YpNmxAXHKJ-chUNGTQMwZh0kNxwh4I-Z0JEkvcMx9O77u0l5tV9SZszdLkv6plL66TqWXsVzgdyq_JjOYWVvEZTEOWCgeUWOKk5svrnunin8fUSyP3zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 02:24:02</div>
<hr>

<div class="tg-post" id="msg-452044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/britaZeWyb782rGh0-GDotTgF2-Ni4zSkpkI7u5_iaSRw_Mz81l5dVoTwa4cGFMf4EHcX_B5NdVpzlmb5-klMIHtABlOtFKrEZiwBxRIczaIFUGrlaTBi4X4DbRdQpxSPfB4LvyOqBFthg_evZveWnSTuR9cH1OfateKTSTLeInjzHNsec5ve0OU672lisy3Y_E055gH5oMotHEhUalmtmxeMlgoOxiu48Qoer7C4pLvBXyHAJ07bkuKKe1HzLRhgZiPRGaw4kTNr1_ubMNef4Wsur9LZvzd3fhbDdML397v4NlGK1DHXJXlruXkMBRcoMOOTdC9nIPZG4BJGmZzqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌‌
🔴
منابع عربی: مواضع نظامیان آمریکایی در کویت هدف حملۀ پهپادی قرار گرفته است.  @Farsna</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/farsna/452044" target="_blank">📅 02:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تصویب بودجۀ میلیاردی برای تداوم جنگ آمریکا علیه ایران
🔹
مجلس نمایندگان آمریکا لایحۀ بودجه ۱۱۵۰ میلیارد دلاری پنتاگون که شامل بودجۀ اضافی برای تداوم جنگ تحمیلی علیه ایران است را تصویب کرد.
🔹
این لایحه شامل ۶۰ میلیارد دلار بودجۀ نظامی اضافی است که انتظار می‌رود بخش عمده‌ای از آن هزینه‌های مربوط به جنگ تحمیلی علیه ایران را پوشش دهد.
🔹
بر اساس گزارش‌ها، این لایحه اکنون باید به مجلس سنای آمریکا برود و در صورت تصویب، برای ابلاغ به رئیس‌جمهور تروریست این کشور ارسال می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/farsna/452043" target="_blank">📅 02:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452039">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z5iydWX1PrbWzhsJzQDgAu1HhAWzuoYFd7164VmutFRa80giQSW3TZppD7VQYspEY86XHSjE13LAB0Bjh8oXzmKs2VZYlulDX8xtotIuYmI4OeuA6JrjfDNR7v5qfPzD-q8DGMM-7ikFgkDB1s0hcZ2PG0mbVmhzWXWaOoHl4G8woIC35GWMRQ9sM4P_pa0GOOqdP5SIgQdIF4B5LVyHUiqf-e5ecNM31VeZfOY59Uv5KNqJnAXfxyCUCItYf0g0qtqn6OA_C_CJFgT4V5-kKveSYDsRj4-MWQLNActMnvwNbQEAoOpO5GEu165o2JrZcg9jCix9zFwJA5M6KkUmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5j1qU-7bqDb9JPqWyWLgnW9NhF7DfBqgwpVEZ50Jb01L3xp-hsp378JPgPdId-2g7bZfeD-98xXSlalnfcjhkbbDAtSGc45QVKInsd7X3ql5Zz1ReW9T6jUrICR09oNbe_MVelpQECx1jAU3zIWFaC-vCM-pIYkbAiDace8Gn2HFthJIzXp_s4dKzjOdMxjXZp7F_btkYDUfnHcWkjKLcrdwVxDDriMsOfuvu7cBVxAO4giad0rKI1tCVT-9hdJ6ZCjDDd5Ozry3KXaxxkEo6QhLzICpK-si43WyNxAz2VOyrIJW7-uXJpqWKpaGipg2g0KykMvkNwoufIeM9n37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgQfdiUmh2YhznvSqGrSaRwk5K7DCPyiiL3bQ7_9uRMt1iy_a5GwezF69zh4B_4VHEQ_TL9kK8SBdXoTFelBmF65VgJvHWgfOR0DgDpmeqSDGSuorLPDoU6OcaiJ8_6-VrnvpumwaZVGBLc4P5UfhrqIc4otd4a3k7xT8AgalbEK8rCS-5Q4opT0DwoeVtLp-qt0xEoqntNcKaFkcsbJJhx3jGrHlw7u5oF4UI3TGtNrgaUOj14gUUvMZOs_hGqquXWPWvQpx3qxAR8H4EacjGOYqIZKzqVI2pCGtowPFDv4rpyULjdYPGsTTOecz6DCbqbXLBj4GyV14gMfZXkVHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLRBnDJmZPAwlhJ0teBT9fd1wfSneCQsC1txrFxfJZWG_r_RrG5sdqqZx61UGDdjUzsepOPS81QY3G93wn4k2t5iwJki0NW0ERqV5Yd8lGkaP_9xxlB0mVESBsSCAkM089s1rbnzEV4RnQF0SArUF2b4gBBM1Gb2L2dI6HwH_Hby2qrTStc3IMePAd6paM6lWoaiAjL8sumwaKTiksfP913ejNyA78wSJXTOAedQGc5mqu119qNrGFqVfPBts7TkDPef-LGs65_DAgt5oSK-ACVDgQOPAs4eKPtwhSpLAwgIqHJFqXxv8vd3k-6W0wy3KccLDEdXEdQB0JR74lz-cA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۱ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/452039" target="_blank">📅 01:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452029">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mwDplfWRy4kQs2JzS9MLulpgqyz7A4CTn7JVYqjOA4_DVYrpj9tDNUZQqal5Y_j_L5KeoASJTRUlyoqV6ho5pgbo85FXktaDqIRzJUtZLgSwp3jQbK_NxC0EGPFN4XwtFJ2BhFK9NJzaWAnzdMB6VodNcqsQ4poRX746A9T282r4_m6Wxk1dliLu0gbrBgLbwd0rKRX4fgDWtjOGm29HM9x1LDIhq4tCSctEgr7zSJAGninTIUDrp7uZUeFcuui6I2eP9M4BQ8ych_yLHjeRrNKqKblSGXtlN9WOlxqgJqU9DAF4z-RhjScrx5YPf6IaUnpR2xYtluIvAS4M-7kOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oh_A7zg7g9gUmGxppKw6Bz1GcEQauHGVl_qN72fWQDKcguboAV0q3lE7ywze6G2Gy8NZfw6_ZbOSEnxxfTXkc4ZFw-vD3bElAi6r0FMGK-yxDsWpMbc7hbuohw3WoTMpPiNBxi06tI_696LjoGj1e2RPNEvkN0ZzjKBfJR3fy8qAim6wqnXzYBFcRzkRJAeA_Dw2p1c9NxOLa_CYOdhS9LW-rNwjqbNyPx2SV4di5oPl4y1GGgwMQ8ID_jU_GPOZK-xUv5GlqBRTaEagUTol82-ih4uF09PmYaA7ZJFM99Nj-BdzG8HJgsYG0MH3X90dq6hQoKcOedS9jhB3OQ8bEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YArPzdRIp5aEtR0jaqZVTTohsJWeN8JB0x2zChlrJjHq6nEaAdShyuPQWdFbaQgJx_MjqdQA8OWzXOth5_uVqgpszSOeCeIsqUMJaj6KUEyUIgaJySuBdEBnkh1_lD3bROKYSqLFUandnvihmctzx1h0R4l47VJEKI_aXdL4UA_pW45naOpXOoCdqVvcFG_ivvivzDwakMikunGpG43l2zMwE25YA6oNFwnnO5Zbu_kVa41Zkjxu4tk3Il2NEWZ1rZhSS-fcyZqqMg9yPqr77yCofPPYhxL8XW1MzvlhdFgQfffYPYJ-8SYLJaK8Jdx-2b25axqK7_4qMT30vXXmAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vc-WQ0yRzQ65x3UN2qoCrcD2UhQu6tIynBQWW9RvxmG6o1xtGWAAIUTRjCRoErbJ4kd5Lg7p8eTiXpr8RKJIzoAzUF0mW1kEbhy7Q9O8JAup-T_qydpEnutx0dbyqT4RYQ93lWVrRaLCELmTm4aguZ24KRQFiGPHGJrlRKpjampySU4JGd-hmqp32REBJxDB-qAe1iXU2yeYHqij_iSas6hgElS-fwPXJBeG4YNgny-1XsGOHdZBqAZgRjfikDLNhqDjaKO5TvB_oNIiJaXt3loOAjpDHWQrJCU3VV262-LGJbV4Ddp6nem6PQgwU8cNK9IX4uk8Y2lgUeDbTwDDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VkJu2eOk8pdvaN_EyVPLSO-4wDznFSQ49F4SzgwTVfAW3uJBL5FThRwH12H-kdV1JUhV6R_pZU3eGKDHfHK-MjgKt7yV1pzPslmlzY1NsUG7mD670XUvbgwJd3KVR1xMn1my-wWAPidvTjZgx4Hq9zXXY_qbVn6bKFvIVX_kC-6jz-ul_2IAMhVGYNZAOrlJPwzg5X6JgFcmBjBF70t48OjLb7PsFsXNrgyVR7f8-xmZfC1xMnzuGx7qb_BExJdoFZOALFY16_cu-HbxPbRFb5WweAXJMIObFQI4wDc7vznb_yBjVCesWNBOXyzJwTXErKr1uEvYHzMRLCCTBDR2WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kA1sEZBNuHEEDgM_NvKiPQPiX_pkWUDM-4gkHTDT4rHIEIYwsng7ukUi9tNLV7JoAFIa6lCVNgDcOAlyWfo33dzWJ9Bj2WInkClFWVzEZZMDmIXlAaa10gqMpGCw1dxCAMBFU0u8fwge_XKh1xy6yIgCRquBSK_OAsrVACCwO9JuS8Da0z-QEAxFhdkMPkx0KYYkm0aiDW9300CO23Bm5IopQbQrWpMJnkDKN5Ox9_EbelfLybv5k_LjthdlGbBqM0rTjvkGkAe-Nqho8z7VK9HRP9TpmsTY2emgNsOFuFhtIrs7zsKnyKhWMf4lwynbJ6XMUvxGOV-XBbkGLqps6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tv7UI2m6eIhMunB3jjPLnumLZemAb1To6ezNPyIpD9thCDn990fqH1E7pb1eQ4Szxw2Zap4E15ffGNFn-KRSi_FepRc3PMFZWLBlO4v1pjmIVJlNpw0LaoOteXJrIxnbLWqiwTBFAYZ_Q3UfoQNHmDuOyzV75AWk3KlpREEhyJ6G3y-Ynd27o2_JfsbNs7JysB9edmnQmy9bht-5ZvKwxjtj24rMN1eyOT34o-PzRRL1iZLQSrQIOY1VBPeAF3apKdYhYUoeEWIUmvpB3RD11bey5dUWzP3HV8zofpjDhZq0-uRWkd_yKb7D7Cq8f5fAHMJplFxExpWQu-9vKxHHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTElTFZKqtgTcEzC2GMNx0n311awIhYlh7x6LT-n7PlVHf6owB_amsKDf7EHeIh8DHh0-Gc72t5efEgTepQB786AiHvh-2qBvgBbIE6yIKWoquR6Cpd9NHkh5qOwR8SdlqLQ26i_V2QfAaTLwZpyeO0WOXNtTjC4C42V8RtMvjRdEc51ClrUuWiDxGuTN_O5ROfTajkoatXRipu5OZajWZ2RCR-cwFo-iYhv-IdJICHOn6z2F9GF-DWv3Fe48MUgkdc8s-tzyLHqhPVs0RQeRBRHNbimq7N11qBNEcPhwiw36NNCHaSF2r9v6dqmfKsW5D6_ozkO8iaCR11YWucI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RyEd57zed-Prm-nU-i301pfQ9wIirnYOjjd_KJFq7QYjYqMYPBt1k2BerxX7qN355hSn35uGwVUjblhL48SA4H8gevpp7RvDVND4deY6cdjjSHjyBuqOJmxr8mhdSxsx3e4bN6vOm5_3tdeDhH9nFENDVTH5DVE1ARL7fHi7rggvzs28JFqDy9NHS6z854oCWAfjlZzsSy9i3DQZP5Lx4rVDdv16ZFj0upEVcW2HuKUoGNE-geP9QnsSWYHS-Clvm0LyqaS24uNHUhZS0fWX5gFCg5k2nf-eu8uvnP3_lCDeGYzyOyIBVCTLDJR-0IgArmqgF1QZcD4g5rqEi8Iy7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xmc702q3iRpH8r-l-6NwaGlMUhseU18eL1SED8KIFUQVT-JLNDJfPPyiCcAivpfS-nS8mzMvPJj0CLTi0sIuD8pUtnpJW2iEtzBEHPqZaEUJDQUrn0SRg8kXWFnKOjL8wBU2FoTtMyifC-odeIBSAIQV4b05NZWABK246Lp6Wj3fyUTSyMYpW-Vf5RhZJbjjjxU8sgpKMFD0wIFTte7-etQkQGqG1nRCBaMz6GRjGc20jflSrV7yLkTdoGEUPMwivj05ONFuYYz-y04gnSF032r8IwQxrJfo1hdCRlXru1j50U88swMRkEk3e-KceSMyxfKIiFhqf4RdeetcXjs3bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/farsna/452029" target="_blank">📅 01:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452028">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQDkve-oB7X9_Esn2SRwJ99m3FoGhcjzvY_sN-IV3DP_k4R6hDGW5IIZEKw2jdK_UjMffDkrCD0oSbdMWKC6vqLlEdiBeYb3m0q6FpZD9pKYcQzGB-sm3cbmixRiR90jow8IG4KPY7syKMQSP-lRBZBnKpm6qmtGrzWXxu1NdLMbasiXrHApWAOqim1VmTJqsVACPX5YHJE8R3XzQ1cqxSiut4pBoRt3wUdDy9-Z48uo5Lbmx3XDtpzbV5V3zEZjrLxAHeUwMA6HTY_z4LafUMppo1qPNDO9s_6DoGGmTrO9sIfeiPw7QEPTQLSYi_mxIYmvQLRq-lg-1YNWWh7hew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: با دستور ترامپ، و با هدف تضعیف توانایی‌های نظامی ایران در تنگۀ هرمز، دور جدید حملات را‌ آغاز کردیم.
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/452028" target="_blank">📅 01:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452027">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=uiSx3kk5pc08rW-HhmN599PuRkXsY9DKBAZZymZd2Ap9o-3Z3ymhIL8vcflmxgA5IT-fO7b9E9ShWsmZL3oha66x5hhguI6jKm8l09RqgfBRGv945TZozWE5RjoZ-vGdvBeoR552YZv6hv6d1nSjVlj6tGGdWruT_p7w5apd8Y4mZGzSkQ_BfF_47Zcp1VbNx3RyOCL-Y9UrGPhgUopWmCabBhtwbX2qN2QCilYRntLZ70hOS7IrtbcHHD7wMu_N1lqe3wrhRL4ch1QKEJ7nq28wgdioFug7f90laF8Z0idVfAVUPymv9rOdigimm5qbp6wosH3Q-NMuk4Tw9b7bNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92215a25.mp4?token=uiSx3kk5pc08rW-HhmN599PuRkXsY9DKBAZZymZd2Ap9o-3Z3ymhIL8vcflmxgA5IT-fO7b9E9ShWsmZL3oha66x5hhguI6jKm8l09RqgfBRGv945TZozWE5RjoZ-vGdvBeoR552YZv6hv6d1nSjVlj6tGGdWruT_p7w5apd8Y4mZGzSkQ_BfF_47Zcp1VbNx3RyOCL-Y9UrGPhgUopWmCabBhtwbX2qN2QCilYRntLZ70hOS7IrtbcHHD7wMu_N1lqe3wrhRL4ch1QKEJ7nq28wgdioFug7f90laF8Z0idVfAVUPymv9rOdigimm5qbp6wosH3Q-NMuk4Tw9b7bNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادی که به‌یاد دانش‌آموزان شهید مینابی پرتاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/farsna/452027" target="_blank">📅 01:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452026">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/452026" target="_blank">📅 01:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452025">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صداهای انفجار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/452025" target="_blank">📅 01:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452024">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpOBhQLKrZLpAhKAg4RqcsbwpBC1b94gKy-xyHrUUg4i8KItmzfUFBVYuANoajhA1rWFJkX3wcs6ouGhmd3uMcDtScZJyXRBp6GGuzcnX8OnmJtsjmtxCMz0ir_UkeQ3eRqAJ16iYqRa-tuM-Kq1nrj5enQ-PG6xVANxtP6b2gKeAB-NKpqwaetq71iiSEVc5dYMcHht_xIj9PjTlgp8x2A-KPw5nBys6HB81TZoGQdUJRg2BJNOwBiSgdm96ZZTIU8aOyKNqqJiEG2C28VHQsNpShKGAv5MUDLPZliXgkbvXTWabV4fugnoVCnJxX372-GBSAqcBKD68YM4SmvIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منبع نظامی: تنگه هرمز همچنان مسدود بوده و ادعای سنتکام بی‌اساس است
🔹
یک منبع آگاه نظامی بامداد امروز در گفت‌وگو با خبرگزاری فارس، ادعای اخیر سنتکام درباره وضعیت تنگه هرمز را به‌کلی بی‌اساس خواند و تأکید کرد که این آبراه استراتژیک همچنان مسدود است.
🔹
این منبع نظامی در واکنش به اظهارات «سازمان تروریستی سنتکام» که مدعی شده بود کنترل تنگه هرمز در اختیار ایران نیست، گفت: «تنگه هرمز تا زمانی که اقدامات خصمانه و تجاوزکارانه آمریکا ادامه دارد، مسدود خواهد ماند و باز نخواهد شد.»
🔹
این منبع نظامی همچنین خاطرنشان کرد که مرجعیت مدیریت تردد در این آبراه منحصراً در اختیار ایران است.
@Farspolitics
_
link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/452024" target="_blank">📅 01:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452023">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
یمن: ۲ نفت‌کش عربستان را هدف قرار دادیم
🔹
سخنگوی نیروهای مسلح یمن: با اجرای یک عملیات نظامی ویژه، ۲ نفتکش سعودی به نام‌های «ENCELA» و «LAYLIA» را به‌دلیل نقض دستور ممنوعیت تردد کشتی‌های عربستان، هدف قرار دادیم. @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/452023" target="_blank">📅 01:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452022">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/452022" target="_blank">📅 01:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452021">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۲ انفجار در بوشهر
🔹
دقایقی قبل مردم بوشهر صدای ۲ انفجار از حوالی بوشهر شنیدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/452021" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452020">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30afc95033.mp4?token=iF_qP1-8mH1iGQ2tSnsdcyWbQJSC4v7Ti38rkrDeO5XipQbPC72qZ5-m0x6WfgIi1f4dLtS8EX9FL4oBY6AvemxZrcUyQEpTSyji_sp88yq4I18IDwIadlzKUTtjLHYVS-dRZRKcwxaV1OBz9HGxRYhO9HPSJpXc_ULysjICARkx7jqogzcQecNGu0HcHLl6lRqHOld5Se7v-pKUCZr9v4eojfzrLskjjDRRtjes_pJeFOBpD1Gks5JLDSFHX43uzKZwjwYTdYWGXV_Lsbq-QGdqmFOYehVQk1ct5eoVNFZzG9jHqZvOc0bZQu978gmgBPPagCpqp-59e6LypWXsXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30afc95033.mp4?token=iF_qP1-8mH1iGQ2tSnsdcyWbQJSC4v7Ti38rkrDeO5XipQbPC72qZ5-m0x6WfgIi1f4dLtS8EX9FL4oBY6AvemxZrcUyQEpTSyji_sp88yq4I18IDwIadlzKUTtjLHYVS-dRZRKcwxaV1OBz9HGxRYhO9HPSJpXc_ULysjICARkx7jqogzcQecNGu0HcHLl6lRqHOld5Se7v-pKUCZr9v4eojfzrLskjjDRRtjes_pJeFOBpD1Gks5JLDSFHX43uzKZwjwYTdYWGXV_Lsbq-QGdqmFOYehVQk1ct5eoVNFZzG9jHqZvOc0bZQu978gmgBPPagCpqp-59e6LypWXsXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
برخی منابع از حملۀ موشکی به یک کشتی نفتی در نزدیکی شمال مرز یمن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452020" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452019">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
حملۀ موشکی آمریکا به اطراف شهر اهواز
🔹
معاون استاندار خوزستان: یک نقطه در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452019" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452018">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در سیریک
🔹
حوالی ساعت ۲۴ صدای چند انفجار در حوالی سیریک در شرق هرمزگان شنیده شده است‌.
🔹
منابع محلی عنوان می‌کنند که صداها از محدوده بخش بمانی سیریک به گوش رسیده است.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/452018" target="_blank">📅 00:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452017">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
حملۀ موشکی آمریکا به اطراف شهر اهواز
🔹
معاون استاندار خوزستان: یک نقطه در اطراف شهر اهواز توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/452017" target="_blank">📅 00:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452016">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-my6ZqzdzcShCex48I_eZaF7cLWdYp1yf9xmRtdJJObOVQ6ZKGCN52KjpJivUNUUR9yefXLbJqmz78V3ae9lSremV2telmbrEI2hVLut4DRweUEQdxzw-XtTfxObLqFB6mgSWExrw0D59gtwai-Kxd-7LGZyFLj8sw41T0Bl1GACREWfJMaLHW2goos_pTgaQDfrw8iFhmChgCyP789cJAh9x5WKh0pCIpvNc3YfvDCQ2zUyP4gWMx0-WnreGByVRGX9vdHxyh1YSz5ucRe8pm_AZ3Ftwa1-PgDeeAlzp63k-O4pwmzF7TezQsjIKSpl-a3LihgIMrsAHuzOZCITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: ایران در طول جنگ چند مقر سازمان سیا را هدف قرار داده است
🔹
رویترز گزارش داد بااینکه منابع از افشای تعداد دقیق یا مکان تأسیسات سیا که مورد اصابت پهپادهای ایران قرار گرفته، خودداری کرده‌اند، اما یک منبع تعداد آن‌ها را «بیش از یک و کمتر از دوازده» عنوان کرده است.
🔹
به گفتۀ دو مقام غربی در منطقۀ خلیج فارس، تحلیلگران معتقدند حمله به ریاض توسط دو فروند پهپاد از نوع «شاهد» ایران بوده است. یکی از پهپادها بخش آسیب‌پذیری از نمای بیرونی سفارت را تخریب کرده و پهپاد دوم از همان روزنه وارد و منفجر شده است.
🔸
تأسیسات سیا در خارج از آمریکا که به‌طور سنتی در سفارتخانه‌ها قرار دارند، «ایستگاه» نامیده می‌شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452016" target="_blank">📅 00:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452015">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keJdYnoHjAEw-gibZ5w1y6lmwnTM9eR8INN0L5Iq99kHk1NUOM_dvNqyeTlTZGN7HhYamJvDBEKnEKqXEdb2xAF-LUtqAa4_9ixgj09isiMQOiUua1Kvq3Clc35cxVrwFn0p1crbnfH1hlT1W9E3JMqdIImmtIECkj-2L-o0H5qtsKtYZud0ChVnymwD2A9wM5ieC_SIlfwnO29cQoiFujdx_1RiMh5EQJyruFTblWpg-O1LL3w8AJL9QRzBsZzH5jExz0WsFrvd_H_JGTcqBm3OdMfvzCdLBqEUTeInAU1u1gD9xDUKT8Tid__XykAikTqrrwwnlrZgjzPBi4fwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه‌هایی که چراغ پایگاه‌های آمریکا در منطقه را روشن نگه‌داشته‌اند
🔹
به گزارش فارس، تهدیدات اخیر علیه زیرساخت‌های انرژی ایران، با نگاه به معماری امنیتی آمریکا در منطقه، پیچیدگی خاصی پیدا می‌کند. وابستگی عمیق پایگاه‌های نظامی کلیدی ایالات متحده به شبکه‌های…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452015" target="_blank">📅 00:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452014">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5NJ3GyT6FgANhIXCyqk4VCr8etSrlS1fHp657mW37bTES6vfQuAwq5dJ5YF2PN0uwfRsOLBxWLnVlYYHMXvZqERdiRVakdkllexu2TxIa5-3rHJ2GZsteVyI56ftmc5IaQogRNUxMRU3ZqdpxkNyO4icSiiN80CVyycCaw8MC4KyfBe-k80zorQ1cPST4oauuOt7XKZmlwop95Ms0TxQqTrnJpktDgsxi4dE2qMcM_Pp5H8_K7OfgxcMYmU055XgSN8ax9cx5GFTrnh-i06Ml3GpTF80xfydkGMcJN5Mi3LcFn_eBc7Is8wq1CKQg_p-WREZxkKiN7ZtW6WByqKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: در صورت آغاز جنگ علیه غزه، فوراً وارد عمل می‌شویم
🔹
رئیس ستاد کل نیروهای مسلح یمن در پیامی ضمن تبریک انتخاب خلیل الحیه به ریاست حماس، گفت که اگر دشمن اسرائیلی بار دیگر برای آغاز جنگ علیه نوار غزه اقدام کند، یمن آمادگی کامل دارد که فوراً به تشدید عملیات نظامی بازگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452014" target="_blank">📅 00:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452013">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سهمیه ۶۰ لیتری بنزین مرداد شارژ شد
🔹
۶۰ لیتر سهمیه بنزین مرداد ۱۴۰۵ خودروهای شخصی بدون هیچ‌گونه تغییری در کارت‌های هوشمند سوخت شخصی شارژ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/452013" target="_blank">📅 00:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452012">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb67e609d.mp4?token=giSd54pzcgvU5bHX1QuuURnoMq3KImjM9lBl_1ByCGbEmmOg9AVKcxCz7CMwwKgung4DajNDl3F12m6OWd1Y87Qy0WlWokcMgDjgJ5zuR9dTWBPciRRtt3YfvYhgbjJM5rgcJlZB207ALcWGF1TZZbJg0bJVhhO90WXqBAxfUCkkORKCNnOfLxMCwmMlgKVs_-kPhm63Qii9IRqf_SCrMP7TzzDj1NiamRSHbOpBBNeWW8NWGR_8Ikx6FGngg94qPsA-XczYeNdHwW0lQiUoHjkVyCet6FnTaY6Hz5fe6Yh4RD-V-S8qPwfBC35AXDCWvUhIB4UBVQSRvnfDqGjAOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb67e609d.mp4?token=giSd54pzcgvU5bHX1QuuURnoMq3KImjM9lBl_1ByCGbEmmOg9AVKcxCz7CMwwKgung4DajNDl3F12m6OWd1Y87Qy0WlWokcMgDjgJ5zuR9dTWBPciRRtt3YfvYhgbjJM5rgcJlZB207ALcWGF1TZZbJg0bJVhhO90WXqBAxfUCkkORKCNnOfLxMCwmMlgKVs_-kPhm63Qii9IRqf_SCrMP7TzzDj1NiamRSHbOpBBNeWW8NWGR_8Ikx6FGngg94qPsA-XczYeNdHwW0lQiUoHjkVyCet6FnTaY6Hz5fe6Yh4RD-V-S8qPwfBC35AXDCWvUhIB4UBVQSRvnfDqGjAOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت پردهٔ قتل زن جوان در شیراز چه بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/452012" target="_blank">📅 23:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452010">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITPd-fThIHe4UwkRErOo6W0SA-zcTtIjLg_NT-XmsOcX9lHLwd-pDeG1_Nd-Klka0hzOs5U9Z1kZUb6vcK5Iu3_AWrN-kYojpqImyrvB4eDDJm7OLxF1OlOUzfc3bLc4aSLhym65RIoX77hm8-WTF4Kn8qwQM-wrkZQfUsVcW5uBY70mFGIBKcZWOj-9eOipmxG6bKnazKtsrSxWsLobKHEtBhnqrBCR3FH60UyYN8iFqkrM9kFX7TChorKjdGGxMWLP72T5KVYtcnCMaYqGkHAYwHCtiOKx4YlwD3dlhHBP7YD8_dWfvyXOKA1xFLBHrUHdPy3GxFemj4KO3e6R9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مخبر: جنون آمریکا را با غافلگیری در فناوری‌های تهاجمی پاسخ می‌دهیم
🔹
هرگونه تعدی به زیرساخت‌های ایران، در قیمت انرژی ایالت‌های آمریکا تاثیر تصاعدی خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452010" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452009">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82765fb34b.mp4?token=XypT5Rt0YdqDbEy10KeSlUTgs9CvlGJl9z0g8QvqGHDsNAeaJwFx8GV_k0_FF0k9kSiP6y7QDN23JOP9AUt7Sh8FoknVoyq8Nwg2mZDLK4y97NrTz66xhZbb2qkIYNdLnzHzIyq48eq8TDp2DN1PVQpLit6gW_teM2T0gKsm0ndKigWtZrRt6ZWpbGeiGi-oddi5d9MfbuJSOXIDCTs_EcmpJ3coBFUtU4RktUkcH--2ehtc4K8i_ABOaamay86a8AyS_ord3FK4kTa8xLPgpFeE38lUl6ZfUWAvGOrqiX_310Qq2yGbWJfI6ulgZ1XyZCR6KLs9NiFiY5N6Vti9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82765fb34b.mp4?token=XypT5Rt0YdqDbEy10KeSlUTgs9CvlGJl9z0g8QvqGHDsNAeaJwFx8GV_k0_FF0k9kSiP6y7QDN23JOP9AUt7Sh8FoknVoyq8Nwg2mZDLK4y97NrTz66xhZbb2qkIYNdLnzHzIyq48eq8TDp2DN1PVQpLit6gW_teM2T0gKsm0ndKigWtZrRt6ZWpbGeiGi-oddi5d9MfbuJSOXIDCTs_EcmpJ3coBFUtU4RktUkcH--2ehtc4K8i_ABOaamay86a8AyS_ord3FK4kTa8xLPgpFeE38lUl6ZfUWAvGOrqiX_310Qq2yGbWJfI6ulgZ1XyZCR6KLs9NiFiY5N6Vti9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایستادگی مقدس مردم ایران به ۱۴۴ شب رسید
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452009" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452008">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a84232a.mp4?token=ZltCQkPvAc5kHZRi5Zha1UoQpnFQe38MgLbT_37247-j9JyxhBClHIuacHPoi6AekfBx1IIdDMzbmJrCLFthpWHiNt8Lu5azA1_5X0_xZu-LdaQJd35tmOWQ2M1k5f04k_wkbHrdZBhh_KNMpE9tar4uWRHmmaFYagQRMAb4eT8YoPp5OhgS0siMemHYMv-Aes2hLFiU7uxsm2zyq9rS25oAcxKneM5YEP2-ady09jIj1-5tlNquVVQfrPaYtgKWb95cK1QVQEC7428HXO2jl8pcYHSjaK_cDbDXYIdsvNbTShLO9q0tG0Xoud7J0QjST5oL2k5wB6aTqWiZQJJpMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a84232a.mp4?token=ZltCQkPvAc5kHZRi5Zha1UoQpnFQe38MgLbT_37247-j9JyxhBClHIuacHPoi6AekfBx1IIdDMzbmJrCLFthpWHiNt8Lu5azA1_5X0_xZu-LdaQJd35tmOWQ2M1k5f04k_wkbHrdZBhh_KNMpE9tar4uWRHmmaFYagQRMAb4eT8YoPp5OhgS0siMemHYMv-Aes2hLFiU7uxsm2zyq9rS25oAcxKneM5YEP2-ady09jIj1-5tlNquVVQfrPaYtgKWb95cK1QVQEC7428HXO2jl8pcYHSjaK_cDbDXYIdsvNbTShLO9q0tG0Xoud7J0QjST5oL2k5wB6aTqWiZQJJpMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میدان‌داری نیشابوری‌ها در ایستگاه ۱۴۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/452008" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452007">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88cbc0418a.mp4?token=XCRuiyUGJnJMU-QySBGw_SCdbUIQlaYiq-1ccizCGN3CWjb7lvgC-Nzo6OjxlDeykFjPkv_Sy90vPRhPnSUvko-Cdid1mlL08_8EEO9FyTwyD5EDieuKWwjt9KGlXXHa6XncT1sPcr2AyNNurZoZGKgc5WNAEEJJRJz7HE_SkstE9G3Ccpx6DzZ9UtlMkHUYToOHHybZJhlOEpb_OSq7kRYaRup0EmcI6bzTTh7Ei_NUVvrDcGuxwHhAEe89TW38owSAC2caJHXVdg5BDAUihX5mlCtZ7a7THBeB9gP085Sf5VQuSdgkQCJkBsTik6y2TVJyxwpFUhG8mbg3Xll-nh6pdvZoz5qUH9PTYf4YaAixyOLLaHx7rtXXVppqnRZS5uis_XMBlTSUlvegGc7c2loYMDIKnIufnke8XidG0al_Js8uyHIseDs1TKoNBVS87q5BVxryMe6xst9G32zIAtvQyo_D3gDSvlfp4VyeZKIGPpgc8731L6xPsoYrMhEHpSvG_EYOOE-Xu3HO4FT65HSCpPFB93FPxJS8xWZqUxUdrAgKvbWYzw0mvkpLIlzlCAsXw-z1ITX_J9U4Xe-Ul_MJSa9zmaHo8rZBDk2hLJBzCwxh7TuJOh5FszM7C75PQfmxPXPaSr6E76rR3uRGHSxN4ARgMg-oMLNGQRLknPs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88cbc0418a.mp4?token=XCRuiyUGJnJMU-QySBGw_SCdbUIQlaYiq-1ccizCGN3CWjb7lvgC-Nzo6OjxlDeykFjPkv_Sy90vPRhPnSUvko-Cdid1mlL08_8EEO9FyTwyD5EDieuKWwjt9KGlXXHa6XncT1sPcr2AyNNurZoZGKgc5WNAEEJJRJz7HE_SkstE9G3Ccpx6DzZ9UtlMkHUYToOHHybZJhlOEpb_OSq7kRYaRup0EmcI6bzTTh7Ei_NUVvrDcGuxwHhAEe89TW38owSAC2caJHXVdg5BDAUihX5mlCtZ7a7THBeB9gP085Sf5VQuSdgkQCJkBsTik6y2TVJyxwpFUhG8mbg3Xll-nh6pdvZoz5qUH9PTYf4YaAixyOLLaHx7rtXXVppqnRZS5uis_XMBlTSUlvegGc7c2loYMDIKnIufnke8XidG0al_Js8uyHIseDs1TKoNBVS87q5BVxryMe6xst9G32zIAtvQyo_D3gDSvlfp4VyeZKIGPpgc8731L6xPsoYrMhEHpSvG_EYOOE-Xu3HO4FT65HSCpPFB93FPxJS8xWZqUxUdrAgKvbWYzw0mvkpLIlzlCAsXw-z1ITX_J9U4Xe-Ul_MJSa9zmaHo8rZBDk2hLJBzCwxh7TuJOh5FszM7C75PQfmxPXPaSr6E76rR3uRGHSxN4ARgMg-oMLNGQRLknPs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کاشمر در شب ۱۴۴ قیام مردمی این‌گونه در میدان حاضر هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/452007" target="_blank">📅 23:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452006">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
برخی منابع خبر دادند که در اردن هم صدای چند انفجار شنیده می‌شود  @Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/452006" target="_blank">📅 23:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452005">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
برخی منابع خبر دادند که در اردن هم صدای چند انفجار شنیده می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452005" target="_blank">📅 23:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452004">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/452004" target="_blank">📅 22:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452003">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89683dc21.mp4?token=CMsJulP9Fz8WaiO0GBVeXtrtMBiKh09fHEyUomF7A4fArQDIUG8UrgnJDsIYrI5_0YNIm3rDBvA81QiQ3xMbBby47Ym4PcOIS5NYl8J6iZmG_cbJGnsmYMHENfxpBoP3IiaAKdCKKl_Tnf2PjCzaR1U5adX8S9nQmSNrtb-4N2ddCCH0_iWmfsljrQnSoOOWjiE_8TMVKBMwjpeNsJhlEdOzhY0Qfy7cWFoMIDsqxrOlUS71VjhTpeNm3MUxH6YIf4YgbZrMO7AVcv3ds0DPFpR40Ba-mq3Iptxi8U9WxIPdHKHlalwqwxHQKVNqH5emIjbqmhXwYqc4jy-ih_0OAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89683dc21.mp4?token=CMsJulP9Fz8WaiO0GBVeXtrtMBiKh09fHEyUomF7A4fArQDIUG8UrgnJDsIYrI5_0YNIm3rDBvA81QiQ3xMbBby47Ym4PcOIS5NYl8J6iZmG_cbJGnsmYMHENfxpBoP3IiaAKdCKKl_Tnf2PjCzaR1U5adX8S9nQmSNrtb-4N2ddCCH0_iWmfsljrQnSoOOWjiE_8TMVKBMwjpeNsJhlEdOzhY0Qfy7cWFoMIDsqxrOlUS71VjhTpeNm3MUxH6YIf4YgbZrMO7AVcv3ds0DPFpR40Ba-mq3Iptxi8U9WxIPdHKHlalwqwxHQKVNqH5emIjbqmhXwYqc4jy-ih_0OAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعا می‌کنم از پیکر پسرم چیزی نمانده باشد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/452003" target="_blank">📅 22:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452001">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFejudodXr4tuMDoJ3V0rcuCS_5ZUoPApdyZcpLcdyy-frpAdHr6LRiOwx5tNp3xG7A93W6IexfuhpciPwn__5VKzBP94YI3spRVpe7VLN2hEvtOKCjsDzjBxxgvcpuYSYewI8AkAoGrCLFk1sCPPhwu8ApQ5ppPCu81LvlG07jno8Nr1Ce8sDfRPSV4tM0uhG9jC6iAYLmAPe8jLS8OaDDbAddkHrFYL1PsOOuZSonJiWkGuTzYhOz3EIFSutG3O-YP6dU6hiCasS367QdBeMTovd5k0z5GHQ-YIWmTuqUWhKZHFuaZoLyT3mH_PburUizMxQitJ3RkfQkmtxqYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروگاه‌هایی که چراغ پایگاه‌های آمریکا در منطقه را روشن نگه‌داشته‌اند
🔹
به گزارش فارس، تهدیدات اخیر علیه زیرساخت‌های انرژی ایران، با نگاه به معماری امنیتی آمریکا در منطقه، پیچیدگی خاصی پیدا می‌کند. وابستگی عمیق پایگاه‌های نظامی کلیدی ایالات متحده به شبکه‌های برق کشورهای میزبان، یک شبکه وابستگی متقابل استراتژیک را شکل داده که هرگونه اقدام علیه آن، می‌تواند پیامدهای امنیتی گسترده‌ای برای منافع آمریکا در پی داشته باشد. در این گزارش، چهار نمونه بارز از این وابستگی حیاتی بررسی می‌شود.
🔸
۱. نیروگاه الطويله (امارات متحده عربی)؛ تأمین‌کننده برق پایگاه الظفره آمریکا
🔹
نیروگاه الطويله در ابوظبی، با تولید ۶,۰۰۰ مگاوات برق، سهمی معادل ۱۲ درصد از کل برق مصرفی امارات متحده عربی را تأمین می‌کند. این نیروگاه، نقش کلیدی در تأمین انرژی پایگاه هوایی الظفره دارد؛ پایگاهی که میزبان جنگنده‌ها و پهپادهای استراتژیک آمریکا مانند RQ-4 Global Hawk بوده و پیش‌تر سابقه هدف‌گیری توسط ایران را نیز دارد. هرگونه اختلال در برق این نیروگاه، به معنای اختلال مستقیم در توان عملیاتی الظفره خواهد بود.
🔸
۲. نیروگاه دیوا (دبی)؛ تأمین‌کننده برق پایگاه المنهاد
🔹
نیروگاه دیوا در دبی، با ظرفیت تولید ۹,۶۵۰ مگاوات برق، تأمین‌کننده ۸۵ درصد از برق مصرفی کلان‌شهر دبی است. این نیروگاه، شریان اصلی تأمین انرژی برای پایگاه نظامی المنهاد محسوب می‌شود. المنهاد به عنوان یکی از مراکز حیاتی حضور نظامی آمریکا در جنوب خلیج فارس، با هدف‌گیری این منبع تغذیه، عملاً از چرخه عملیاتی خارج خواهد شد.
🔸
۳. نیروگاه راس‌لفان (قطر)؛ تأمین‌کننده برق پایگاه العدید
🔹
نیروگاه راس‌لفان در قطر، با تولید ۴,۵۱۱ مگاوات برق، وظیفه تأمین انرژی پایگاه هوایی العدید را بر عهده دارد. العدید به عنوان بزرگترین پایگاه آمریکا در منطقه و مرکز فرماندهی هوایی سنتکام، نقشی بی‌بدیل در راهبرد نظامی واشنگتن ایفا می‌کند. اختلال در برق این نیروگاه، به معنای فلج شدن مرکز فرماندهی و کنترل عملیات هوایی آمریکا در غرب آسیاست.
🔸
۴. نیروگاه ریاض (عربستان سعودی)؛ تأمین‌کننده برق پایگاه الخرج
🔹
نیروگاه ریاض، با ظرفیت تولید ۹,۶۳۶ مگاوات برق، مسئول تأمین انرژی پایگاه هوایی شاهزاده سلطان در الخرج است. این پایگاه به عنوان یکی از مهم‌ترین مراکز پذیرنده دارایی‌های نظامی آمریکا در خاک عربستان، وابستگی کامل به شبکه برق پایتخت دارد و هرگونه بی‌ثباتی در این منبع تغذیه، امنیت عملیاتی آن را با خطر جدی مواجه می‌کند.
🔹
بررسی این چهار نیروگاه نشان می‌دهد که تأسیسات حیاتی انرژی در امارات، دبی، قطر و عربستان، نه تنها زیرساخت‌های غیرنظامی، بلکه حلقه‌های اتصال زنجیره تأمین قدرت نظامی آمریکا در منطقه هستند. بدین ترتیب، هر گونه تهدید یا اقدام علیه شبکه‌های برق ایران، با یک بازدارندگی متقابل آشکار مواجه است؛ چرا که این نیروگاه‌ها به عنوان شریان‌های حیاتی تأمین انرژی پایگاه‌های نظامی کلیدی آمریکا شناخته می‌شوند و هر گونه بی‌ثباتی در این منطقه، مستقیماً بر معادلات امنیتی و عملیاتی نیروهای آمریکایی تأثیر خواهد گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/452001" target="_blank">📅 22:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-452000">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b22afbf78.mp4?token=VvaLvzG7KKcMQH6bl_OARp7_gi7nj0vJeIBHxpif_0MtnqLs0epZeQUR98lPTfxVJXe1eLuudcPadDEPN_9xDAG-iQN83F3lumNkYROLzOHmlggtCZuMWg2GEnEU5NS8_dbo81hfP2lQb_Vvmf-whipdq4gLTYrY6srDWc8xbwAOTRkvjxirLgdr0xB5G76IUhZGI12BTyRFt_hZreI0RuJfm7qu5J_eqiQuAjLLvpIQbyhQ1rrAkXh1q0uFWS7cqkRZUaxLD-DvhEvfr-pA52hI6HVfNj0k8CIQ027XoXSaNWeG_3Hbut4VqLAncielinXpq_yAN6K14f6d747Q_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b22afbf78.mp4?token=VvaLvzG7KKcMQH6bl_OARp7_gi7nj0vJeIBHxpif_0MtnqLs0epZeQUR98lPTfxVJXe1eLuudcPadDEPN_9xDAG-iQN83F3lumNkYROLzOHmlggtCZuMWg2GEnEU5NS8_dbo81hfP2lQb_Vvmf-whipdq4gLTYrY6srDWc8xbwAOTRkvjxirLgdr0xB5G76IUhZGI12BTyRFt_hZreI0RuJfm7qu5J_eqiQuAjLLvpIQbyhQ1rrAkXh1q0uFWS7cqkRZUaxLD-DvhEvfr-pA52hI6HVfNj0k8CIQ027XoXSaNWeG_3Hbut4VqLAncielinXpq_yAN6K14f6d747Q_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌ها می‌خواهند شما برای اسرائیل بمیرید
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/452000" target="_blank">📅 22:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451999">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e1afe4b2.mp4?token=W_oiMdtVRcIibnb8LNH6q4wxEJDBKb8nqnaw1HF3xSEUPR0_FaV0WJcBTeaAhR1DLAToZsZPy1deiF3jncU_vLOn1cdRc-cIQBhVQlx7jzxA-IyLa1H1VKXQ6tKL93KqazSKM6UhkTyYL-KiWWx0Iu6l0hcBDWYvUJ_joMVUA9K-1U-dW2Psu6L2Kw4mvTGbux7ZxXwr7qF276TNIzHKvwFhDvrCnEFbY9KJqeujlzn-fJvH5-g-mwfQpkS1c1PbMrEg5G5Nj4Nz4TgOlvtFtb811rf_Vuj7Lwp0nbJDRu-UB3x76v-6yA7coKOy0KDThxhLk211IPfTOOYZJ24kmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e1afe4b2.mp4?token=W_oiMdtVRcIibnb8LNH6q4wxEJDBKb8nqnaw1HF3xSEUPR0_FaV0WJcBTeaAhR1DLAToZsZPy1deiF3jncU_vLOn1cdRc-cIQBhVQlx7jzxA-IyLa1H1VKXQ6tKL93KqazSKM6UhkTyYL-KiWWx0Iu6l0hcBDWYvUJ_joMVUA9K-1U-dW2Psu6L2Kw4mvTGbux7ZxXwr7qF276TNIzHKvwFhDvrCnEFbY9KJqeujlzn-fJvH5-g-mwfQpkS1c1PbMrEg5G5Nj4Nz4TgOlvtFtb811rf_Vuj7Lwp0nbJDRu-UB3x76v-6yA7coKOy0KDThxhLk211IPfTOOYZJ24kmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌سازمان بازرسی: اشخاصی از یک نهاد عمومی غیردولتی یک میلیارد دلار به جیب زده بودند که با پیگیری ما این اموال به بیت‌المال بازگشت.
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451999" target="_blank">📅 22:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451998">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFTOZyY_ziSVRYnW8fK04saY5rT2523weoTKe6SnjDIKN8bs9Zc_h9sbh-Yh3UVEeCAWZrCHihxdNJkgDeuJ5tkf7G_S20BNyQAPMOkheVOclsMAdcfM5XaGF_c-3i7VxjpXUF4lI9QR0YaQJCpQUoPEjP6OGdGsRpPhhaAm3-lHQoNEdi3NF0nuEXD3Up85JsLhKk0CCXJzBcsFVF7svs8IhgAwtToqMf89BW-D1m917HotP1P07DtA1RRZTIYqOC7j9JWD5wi4-U40ilzIzpr_g4pUPmmvwlGAjDMLInEV3IJ5hHQe2KEtgg-oKBb4fKyvfq38SaIUnopOnCX4lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
الهی هیچکی داغ شاخ شمشادش نبینه
🔹
صحنه‌هایی از وداع جانسوز مادران شهدای میناب با پاره‌های پیکر فرزندان شهید خود. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/451998" target="_blank">📅 22:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451996">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbf95ece1c.mp4?token=SnA8_OrS8K1DTDyUiZoGPbfSZcfazOkjaB-BOlr3X4KyfZciNvhrqQSs894F7S3tlrXFW-ug42Yqd8-Fut1ibKHDtg5gTw3hO75gIBNuRkBXNgzHcOME1Yv6duneJCj846fs-368myoxHInCntsWm2CWsMnFBUdvs7EHqrkHcpVTLANP_nAxV9s_lvcR7E5Q340DU3G2sIX4QunGEtUWhMSHf4FqtRTNqtdggb0jSKOQC4HYhM7RJS6w7U6_XEI3p1pHbNSzXcTzeTV71Nt6JWv0qz6v_UqQu7a_9AAF5WB4XGKceRw8kJZVlZu34jLmLhjqJ18ZkAlxFJMeZXAFCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbf95ece1c.mp4?token=SnA8_OrS8K1DTDyUiZoGPbfSZcfazOkjaB-BOlr3X4KyfZciNvhrqQSs894F7S3tlrXFW-ug42Yqd8-Fut1ibKHDtg5gTw3hO75gIBNuRkBXNgzHcOME1Yv6duneJCj846fs-368myoxHInCntsWm2CWsMnFBUdvs7EHqrkHcpVTLANP_nAxV9s_lvcR7E5Q340DU3G2sIX4QunGEtUWhMSHf4FqtRTNqtdggb0jSKOQC4HYhM7RJS6w7U6_XEI3p1pHbNSzXcTzeTV71Nt6JWv0qz6v_UqQu7a_9AAF5WB4XGKceRw8kJZVlZu34jLmLhjqJ18ZkAlxFJMeZXAFCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلبِ یک ایران برای جنوب می‌تپد
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451996" target="_blank">📅 22:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfClFMlBM6PZhwUP4_S-ZjH_iv2hspEtTwbgqeURpPJVvfCR9EkKPtyDHqb1CqQvYy2alXxDTuuXrXj8VI8JnLmIY_qVxNhOADPQ1R7UbqlXWxW3LAf-PGkeBgO6rFTzUgmyOKQ6DxsQInk8F39hOy7O8xOMogne3r4Y0MX88FAxzzgQw2gHNdyugW5X12nzScPPs-zKYKir-wPVfZnjAmT7f5NIsI7Z9n7vfXGZNzlGOaW92SmEZBH02Lp9l_CXAf22OXOY3DWsC0sZ5DREq1h4KeSu4tc1bOVzqT5Opgf_hD3lcxdIpMHXvgEOomg3E778AD995ubsP3IcwGAZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارگاه خاتم‌الانبیا: در صورت حملۀ آمریکا به زیرساخت‌ها، صادرات نفت منطقه متوقف و زیرساخت‌های حیاتی هدف قرار می‌گیرد
🔹
رئیس‌جمهور آمریکا بار دیگر ایران را به هدف قراردادن زیرساخت‌های کشور تهدید کرده است. پیرو هشدار شب گذشته، تنگه هرمز همچنان بسته است و در صورت عبور هر شناوری، تردد فقط از مسیرهای تعیین‌شده و مطابق ترتیبات اعلام‌شده قبلی مجاز خواهد بود.
🔹
در صورت عملی‌شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات حتی یک قطره نفت را نخواهند داد و زیرساخت‌های نفت، گاز، برق و اقتصادی منطقه را هدف قرار خواهند داد.
🔹
تداوم تهدیدهای آمریکا و ارتش این کشور، نتیجه‌ای جز گسترش جنگ در منطقه و حتی فراتر از آن نخواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/451994" target="_blank">📅 22:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToeD6qsnOd4dZFi9KKslNQZBhkv0ClVMtza_DzMrptV6z4EB-IDi2ehqEX3_dq-n-5iwUZNVVYp6qLOAdwzi-3FgkfAQSxBsJn6-pu0rDa_pVC3megkm2eg_6bzksgINbCphAv8VVO76_63ZFWuzSA3tCAv5NUfk-qKWE7e0GgqegAK3TBxDt_n0I4tK0B98jyberBzzkazChzqvjj1-P_1EdWKFWMmU8tXY3KCnUfMIjWVPSfbuv3u869aOA6775GY7fZPJnH-wkABGG3UzjLLA5JAitj8zWk9uKLyF8xp_cQmaqlonCihAEzI2LR7MW1z2p1UdFBkUwYMUifwKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
برگزاری مجمع عمومی عادی سالیانه بانک شهر با حضور بیش از ۷۴ درصدی سهامداران
⭐️
«بانک شهر» با تأیید قاطع سهامداران، کارنامه موفق خود را به ثبت رساند
⬅️
مجمع عمومی عادی سالیانه بانک شهر برای سال مالی منتهی به 29 اسفندماه 1404 با حضور بیش از 74 درصدی سهامداران حقیقی و حقوقی برگزار شد و عملکرد این بانک با استقبال و حمایت گسترده سهامداران مورد تأیید قرار گرفت.
⬅️
به گزارش روابط عمومی بانک شهر، این مجمع با حضور نمایندگان بانک مرکزی، ناظر فرابورس و جمع گسترده‌ای از سهامداران برگزار شد. همچنین امکان مشاهده آنلاین این رویداد از طریق پایگاه اینترنتی بانک شهر برای سایر سهامداران فراهم بود تا روند برگزاری مجمع را به صورت زنده دنبال کنند.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/451993" target="_blank">📅 22:13 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKkpPr6gA56TWWQxX4feZmApLxzk31SUwDrhbcBKr-QrOrbMbbhr9ydmZFIkJxXVH3VKgUeYVFBMg-KJipJoJ82EqL4_jHYL7sUu94oQW3S0q7vJ2JpdJqvKmk6LDaELNDsArrKzee0mXFq399svMyef27FEOdf3dpyZUxEz6_EfViXHdKzTgkP9YtKeRFI0etbONxZIgu8WqaUnReGWKJiIIVxPETZkHMEpH3n8usF6_V21aI8858dtuVy2IPMtFupdxlSn3Y6IIetQWZQk1aETX8jInelMm3nNMnjZCFIyADDl6-RLrGFo2UF5Kz_-YK8QjiXaUBjyaIuHJGKi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اسنپ‌بیمه قسطی هم بخری، تخفیف داری!
💰
برای خرید بیمۀ بدنه یا شخص ثالث تا ۲ میلیون تومان تخفیف بگیر و هزینه‌اش رو قسطی و بدون سود پرداخت کن.
✅
کد تخفیف: GT3F
برای استعلام و خرید به‌صرفه بیمه، اسنپ‌بیمه ۲۴ساعته کنارته
💙
برای خرید بیمه وارد لینک زیر شو:
👇
👇
https://l.snpy.ir/z0kq4
https://l.snpy.ir/z0kq4</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451992" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451991" target="_blank">📅 22:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATs01k_OiKN9iIgjLsUs1QLL5RHFn_hOOh5zauif2A_5gba5ZuL1LE89qFBG4YWtxVLfVTF_uER7FJ_zu6ChjEAyjYNYLUfsQOvIQy0aTBx0rdFWRZajPzq6XPT3YmoEKPuBmQjoEUAH3jvE_4te4H86zUxzW1G2-oQlXIA8E9Jkr1yo3YV2S8Jjpyf1mgzIpGVuU3xsf4GVRs7-Sw58kapW1oI93ynkqjHl8YDk4mVoTqY36XEu5CDM2TBOYYCC4aK9Mi2mydxlzLRuZ7JSlIGxOn-JV_1IpBuutdLjJr9JedpmazTRO1WVLIo_OTZuNH6ISnVweA4gCwktK1dm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: هرگونه تجاوز به ایران، از جمله به زیرساخت‌های ما، پاسخی قوی و قاطع را به همراه خواهد داشت
🔹
کسانی که به چنین تجاوزی کمک کنند، با هر نوع پشتیبانی که باشد، نیز اهداف مشروع تلقی خواهند شد.
🔹
دکترین دفاعی ما روشن است: چشم در برابر چشم.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451989" target="_blank">📅 22:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3d1564cc.mp4?token=PANSf8bF8Rz1RD5cHR9Hq5-fnTV-oPGyC1H2lkKhX5PJZkNQl6t76CWzPWtQmtcSuEuE9jRos7C4n3HZaa0oqSCA74jcHCQEz7zGl5Z-PGOZiFokUGUe1QnS4FCziEWcvUJ1O7y6cFjpuspPwdwxPEM0NppUNzVLMUUO1V9pC5i5WB4wwVhNjCoHo05IKEqo_SQOSFz7G363-C7x9ysiy0bc9BiSULHqgFfp50qEYg2V-I1r2Hrgud-7WOozrYEY1ej37xlp13m1V-dwN27HmjZx0rxI050VKwSs6iFSBSSUCNh3lfnozUHusIbKUKP8vjetyVuPflVFxU0WdEWaBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3d1564cc.mp4?token=PANSf8bF8Rz1RD5cHR9Hq5-fnTV-oPGyC1H2lkKhX5PJZkNQl6t76CWzPWtQmtcSuEuE9jRos7C4n3HZaa0oqSCA74jcHCQEz7zGl5Z-PGOZiFokUGUe1QnS4FCziEWcvUJ1O7y6cFjpuspPwdwxPEM0NppUNzVLMUUO1V9pC5i5WB4wwVhNjCoHo05IKEqo_SQOSFz7G363-C7x9ysiy0bc9BiSULHqgFfp50qEYg2V-I1r2Hrgud-7WOozrYEY1ej37xlp13m1V-dwN27HmjZx0rxI050VKwSs6iFSBSSUCNh3lfnozUHusIbKUKP8vjetyVuPflVFxU0WdEWaBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانی باخت نمیده یعنی این!
🔸
مسیر جایگزین کنار گذر پل هدف قرار داده شده توسط آمریکا در استان هرمزگان به منظور تردد روان خودروهای عبوری آسفالت شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451988" target="_blank">📅 22:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT7h2NJQGPPxtSXiw-YZ8PZVDmE4Mzr1m4sIZr9AxqzNBOu6yh2W50oMCD2Rd5yKOadBJep1R5sh8Lor3q4TEPli9nbNU3u-65RVehxrTLBzG9Gauh_J_pu4k-r5cfHYBIG8K_3N2BjQGr-Il94s_vv4KwwGOQZUELOkkch6bfQSdTtbjnW5ea7TdZhyXm_C4CyeMhknMo55tu3uFRTiGBTuCNasb-ax2xpx09EDJl67Jqak9x7aBqw_JlbPnWhzOY3t5F0iC5rpAcAxzTwgHOPfEvyORaTDoEACkWfzmfsdB23U_aNWuw7bA8FkZAWchQsAU8pFRyX0lYIaHhBuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویر جدیدی از مزار نورانی رهبر شهید انقلاب در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451987" target="_blank">📅 21:58 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451985">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9ab32bf5.mp4?token=BmvFL0FyJZnosHl1QoseOVF8qDsOSnWhHEfYmFJbT4M2XupdUvOyCLB-qywZVI4s3Hb9-U45tlMCqBjYlchiHM4mykDOzyRv-D5_TVj6g0NUVyc_C5jjUk9X7wpZJmdNHBy7Nw3EFiZ5fux9GF1pApEd5Ld3tTpHLSmnK-fuu0TozmteqWqS1mbU_C3sHHFfFjxdeSDa7XwDvltrDpkOHx5Bklte1d08GKn_9Vga3tb5cW6vXxhBWUclMRcWtax2_KPHu4MeY0G5bHK5_O-27GlkSUFNuFp_ONO1wOFfHfApWsddRKkEGWBmqfQGqIsDwk8FzhsobrY5KX5xGu0YPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9ab32bf5.mp4?token=BmvFL0FyJZnosHl1QoseOVF8qDsOSnWhHEfYmFJbT4M2XupdUvOyCLB-qywZVI4s3Hb9-U45tlMCqBjYlchiHM4mykDOzyRv-D5_TVj6g0NUVyc_C5jjUk9X7wpZJmdNHBy7Nw3EFiZ5fux9GF1pApEd5Ld3tTpHLSmnK-fuu0TozmteqWqS1mbU_C3sHHFfFjxdeSDa7XwDvltrDpkOHx5Bklte1d08GKn_9Vga3tb5cW6vXxhBWUclMRcWtax2_KPHu4MeY0G5bHK5_O-27GlkSUFNuFp_ONO1wOFfHfApWsddRKkEGWBmqfQGqIsDwk8FzhsobrY5KX5xGu0YPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهردار نیویورک: نتانیاهو باید دستگیر شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451985" target="_blank">📅 21:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-4vjsCRBU17yWWeBDuC_TW0Z8S0t_ZUAuqzC6ZkbCvFkTMbArELmTfkpeGGgS9SV4JMBJ4nCSDJYmibKLPipwqvE0KxLfsMIT12bxaI_UtZkivgh3hl6OHN-qtEDO2zK7hDXZajRo5U831KLLJOQMuUkQRVCqpjKiL80ImVdda0e7sxfu6rgqRYRQTIsQKWBYcolY9IlVn6f9QNHzdLJKl4dleUpO1-84gEAvj8MEN8MiO3wiHFVVHMFWQNZVg6kJXgrwXcjc6DfZ2jqoKSezIymMKLWu0MBP6Fn6r4ury4pp03LOAwYI4ImmdEazoxegnPRs9upRfifWY-dh1X8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی سپاه به شرکت‌های کشتیرانی: مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز مسیر نابودی سرمایه ی شماست؛ فریب آمریکای کودک‎کش را نخورید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451984" target="_blank">📅 21:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451981">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpYCrpke3lptUo83Eqh6rhWOkNEqXGMmKwBQIsFNm9eJa6bO4rQQM2hHAz-Z93QDL0R-NI01CJGPorNPpmvQQCwWWrYbGpS43cSwOTrRWXbKKTHYdOR4kIaB0fiR2oPWfabzPbuoeEXDNdyS-DyZ3IIor9VCx---tcwdO03fk144mEyP3grNoU7A9U588_3q49ja4xDosHtuJAEnthwfr8vhv69pIJZDGZlU3kAZEBxMdCPC9HATAkuCazwYhmFeV8vydc30aT3hCAMUWAJ63cK5kE11vLtQpqUSEGVJG8IUDB_GGhkzIr6ucwsw8q4ThdD_Zf80E-jA8SoR_opuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
فرمانده هوافضای سپاه: اگر به پل‌ها و نیروگاه‌های ما تعرض شود خاموشی برق متحدان و میزبانانِ کودک‌کشان، قطعی است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451981" target="_blank">📅 21:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451980">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=VcCu_dkyPJO7Hn_64vcDn9PWZSgKXLT50wNCJGOUOU6hO8-W-38CN4HR9XwEB7BKBLzva-ckdjKj2kznsAKjac8pGSOAy-14NHggKoN3mleL-0BKMGQ17m53zd1KV96xVgjXQdIMBHPfk_LRhXBwNZCGleGLkw72eI-qtpzlZMTKkINxSAC1-u7wnJj-lj7AFL1ZWsPOE6Nzp7h-yu-2nOh62G2_lJXaI7xYkSXYUdhE0w45UtUqZFtOY10FuoIG5OcpX_1S4ppzZM5qMoGMmZz4gKTqoIj46WiMnsEJEoQos6iOvg3LMoc0GT6ibX7C3cuBhEw61jnaJuW3ZnEjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3aa067437.mp4?token=VcCu_dkyPJO7Hn_64vcDn9PWZSgKXLT50wNCJGOUOU6hO8-W-38CN4HR9XwEB7BKBLzva-ckdjKj2kznsAKjac8pGSOAy-14NHggKoN3mleL-0BKMGQ17m53zd1KV96xVgjXQdIMBHPfk_LRhXBwNZCGleGLkw72eI-qtpzlZMTKkINxSAC1-u7wnJj-lj7AFL1ZWsPOE6Nzp7h-yu-2nOh62G2_lJXaI7xYkSXYUdhE0w45UtUqZFtOY10FuoIG5OcpX_1S4ppzZM5qMoGMmZz4gKTqoIj46WiMnsEJEoQos6iOvg3LMoc0GT6ibX7C3cuBhEw61jnaJuW3ZnEjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: حکام کشورهای عربی در جریان باشند ایران از عملیات زمینی نسبت به آن‌ها ترسی ندارد
🔹
ممکن است صبح بیدار شوند و با اتفاقی مواجه شوند که انتظارش را ندارند. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451980" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451973">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mTKxWEhzwWO6PfWg6vLYHjPz76DhQNd7rzcXTWruROKpt_v6QpNdhimzFSIwGuyurwEaumzTXl4iqsrN8Brnsf0iCxyGFb27pP2_UXaqw4fiiT_MZU1C4WZT5Ne5vg1RIO1iiq5z2sOc-rjBYwaGuRutnmlNNGWtuNdzr5ZGkigVD4g4jcRFFCGdeAZm5WaziB6Ixb7oDbbD-PHg8a3mpatURhRLUH67gE2nikw0RkjbIs8ol2nkBTIloJ7gbDVgRcL0zkf-owv-IJtN9KRy8Yq8kjWwbESGVK--Ypz01qQS4H0k-0VweS4_kEHTraWE6ZumOsAz3YCpJK_w8_dlfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnfRjEVhpGnWPuvKK_YNMWnH0cMmjw77Y8qV_JJzYEPo0Jy-wZuq15B8z3ZAk6C996H4FrN2b7K__oiqA-ZGm_B7tsDdREBqrUmMI_3o3GAvFiJP8w1k0IL9JJ8unCZQKHTuGW964XXBymg5txr0IB51SdQsVMrh1_tD1acdBHv49t_Q7BFHqWioGxxtHRDa0MeD0ly9S9Mu2Bzlui4U8anaZZHOo9jFg3AogrtfvTI1ih002l03xU6yYPXN9sqGS3AI59zgxMnk55EwJoTyKFDQAyHg7pks2RrEo_4s-Pz12Ti5pfTc51mjwBkyv68GcJdS-gIR6xEuhufbmOm-iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RORQBQeZsjenSe10NeaArjipPhTkj-AOEuR90Qsrvpom0whrqd95iUKQspvBsEXCbSpb29G0TGPVvjhYjg_fpVA_lWbLMOCqq_rAu9C2ofSIqCHLyvKqX_HD6pW98YdLhGeMeWK4oc0ymlH1Vm0TFLc3UNUmNWQV7LvrqMPOo-8wy9x2zQXXJk0TPwFqRpKKOCQjesDXZAL3o_ED-biKRJVomS56O_8ngUWZUjgR66kYtFGxva8i3LdVJ5prmYivFzwUqhQ-q32-oWyPEDHPmc1v8YYFiDv7_WlFOYJtALpQz3Mlw5L4mlA33UD2Th-URKZyJmZnR7PelmwYl_PN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qo2mD9GytheZczJp2SN3vHhm9IWSlahuha2-ETkV1AF7-mCchWKC8K09AUtxB7RSjVTyhAOev4RE20KPRxbVKQBJHZUg2eFIni6-rG6U2QKWgR8_XuU5rQpcHYX5DbcwWFnkuemBEx5zQLk-fBO-9o9hWSBCgmdylQ5pjsN8OkP0JbwzdoTMaD9sLWIYUrapsuGRA0IVUNPaMykLzKkKT931XMcv0VXS4PxqXdsj3rjZrR8JFLmtDszcun7kBvnWv_KQe9VcPM5yRJrPwa-HY2STthXAK9i8yuJ5eWccbIqKr01Fn8smFqvc8-JLhPjbPEj7bPx1FWKRMa3rQLn7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-bzXJESRKkV4AtI6PHpWbqnMZCfm1BNXkwpgThQHmoRudvi9BpyAP9uFlqWkUJHodATAQz4cn_mW1mShPOLjv7IiISDTNbVdZTSLEdKJHw6Rtc83LtGKYVtzFFPFvweX2451BUQopmUTpZpWjCroH8koDXdvGAVqgI2Rt1pV2Kx1aL5CPaf0--ipn6U4bHdpzmTMnJpeCvb5u9Yotjp8rrAXmeoBzXVwcL06kQagYPF-irkOgQqn7O43l9wq8H7DOkf2hpBLgK-meu7n1_oDi9DmD18xc4koLfcCNGNl-y4dUAyVT7Q6rqvJFdaqrhzzHPPc8yvtZ8IKcfGDurqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHDAZOA0GMx8yEqvPlIGamSFtGJXhA0SAtAifEXLQ8DhDsFQPioY1ATRZC4RRo4036sZm2CLJ_MD6Rj35V5waOkzXD1j5bZqBfxtDVvWEA1Ndxm3ywSN1cNLur-VqF7jdl2KLaTPtUBIMq7oA_JgKZzqi1qHPOcaFaxL2ZQ9zOjy_lC-gBVoDaJU0eN-VKm4NPfaXpOhAZY4ukf4AhIsmPzYdReCaFKFNk96GI3ETNGThMMJOCc8E73t5YHoe6-cSzWmJ5zx8to1xiisoOXEoPT-wGhrfiH9f8kFsMImervP0n2ux62n-7J1j_Wd61krIJSlLqvp9z0Jz8kEQZ_mzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVMmd757nwvgPtbHDFXMDQmiyxeVok56vjdZi6An1iKUV5aunREz1oOOF0jD-wfDudC6Mc7Us2ziNbNK_bHWULpsj3NK6rPfJLCftCwcgVgklpbINRr4rAV1KHtrzIuETr3UII39FFcv6vzLb2NgAO8oKVLvOzpgvdmUsq40rZ9Jqqr-cwSaoKE1BorXPJoWWXLsS0ZiL7NKmAXHKbH52HdYPKxdTA2ZjJR7vUY_f6kfS6PdA7qgG6uFGo5royIEiPXS4THKrHOhwmvXVgaq2DkqgRcUXB8O0d7t5_o3YmLX8xvDezefoJyttHQKYTT5vjw7NfmbStMzpO-gmi3srg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسم بزرگداشت شهید مصباح‌الهدی باقری‌کنی به میزبانی خانواده شهید
◾️
فردا؛ از ساعت ۱۷؛ مجتمع امام صادق(ع)؛ شهرک غرب، بلوار دریا  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451973" target="_blank">📅 21:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451971">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYGfCnOrMO16LrqPpFYLZkKI9YAO7UCRiQOBb8oxwlGY15SiwhrHi414Ns43onYmhGyTgMnkbsYwGWr4QezapUhwBTwndlvH9m_F_EJ4MhvugUea4wlmL71P-r_Z3aNfJPwsNClxLH9Zy_6b_ylJLCJRcVubPLZbGX1t9kOZA-1vDO-YPAqzlv-aojdWmdm1MqTz7niGpmgfwlYmmv-h3Abh0Bk5zra9nSrUuk_ThpH07iY-DCosclP8YZwj9zkmhlhpuM4dIWHYEO-ZJL3oWC3O3Y4oGAUYnliVldmK57kINNTLZqYJ4trOl39JWsg4rcQNeyA_hlFNGBdBQwc4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
نیروی دریایی سپاه: اخطار می‌دهیم که از مسیرهای جایگزین تنگۀ هرمز استفاده نکنید
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/451971" target="_blank">📅 21:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451970">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
منابع عربی: صدای چند انفجار در کویت شنیده شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/451970" target="_blank">📅 21:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451969">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c645e09a1.mp4?token=LFYClR7v35O-AbaTwArSPSGJj-fJND2sp0kjtusiyR8AnpXeIIchzCqAwyx99Pjtgrip5-5bkwTBVmCezbrE2-28KMtGkdL-c7nCihY5L0sm6qWgsZ1nWK4PIN8q4svOqwiwDJPFiKrFAQnSMi2fyI8wj7HncA_k3KExNzjnHGXVbSv7p0D1-KwDfBT_saGZ9QNZAdvTZ6W9921s0igbj-cp-VXvXWiTC56-4l--Lq0V-4SQgA6bTFQEh4NZnehkTE75-0ofMrrHqKXnlrfBrP0QuqsG_sYb8K6HAVItOLqbGnB2xu6lIhuBb2mk_RJQ1Efed7ATHFZqq7f9AsDWxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c645e09a1.mp4?token=LFYClR7v35O-AbaTwArSPSGJj-fJND2sp0kjtusiyR8AnpXeIIchzCqAwyx99Pjtgrip5-5bkwTBVmCezbrE2-28KMtGkdL-c7nCihY5L0sm6qWgsZ1nWK4PIN8q4svOqwiwDJPFiKrFAQnSMi2fyI8wj7HncA_k3KExNzjnHGXVbSv7p0D1-KwDfBT_saGZ9QNZAdvTZ6W9921s0igbj-cp-VXvXWiTC56-4l--Lq0V-4SQgA6bTFQEh4NZnehkTE75-0ofMrrHqKXnlrfBrP0QuqsG_sYb8K6HAVItOLqbGnB2xu6lIhuBb2mk_RJQ1Efed7ATHFZqq7f9AsDWxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سناتور آمریکایی: پنتاگون هیچ سخنی درباره تلفاتی که در حملات ایران به ما وارد می‌شود نمی‌گوید و پنهانکاری می‌کند؛ اداره این کشور به دست یک دیکتاتور افتاده و این یک وضعیت رعب‌آور و نگران‌کننده است
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451969" target="_blank">📅 21:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451968">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0079f094f.mp4?token=flImfblpKtTksGw4eD06qEVMF3G0laW4u-METgqbMCBEtisyfLcEEKrFzHrDCDctsZjH2bIZkCbJQ07GU_BlGLe0NEOnCewOTAEm5YNZJlcdghqJ4xfYpaAoG1JXgV8aCFfiWySuvFJ3e-sbQ4V6dBD5QlU8VW2G-PG4-rHKeD_T6XnVKKcGNgve6v_Igj9gTt4J9L3cHYKpb1WX6gaBYTRZRHtP5mJcal4EYeIfQ5euZEFVjzhlnROYz2tEzj74G85oulvMa8kkXJoaGjT1gdD7EptDWvPzkytObDyYLlU4xvP6m3CjAzxuvXx_kkbBA6nvrApWnS8JwmGOTqsG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0079f094f.mp4?token=flImfblpKtTksGw4eD06qEVMF3G0laW4u-METgqbMCBEtisyfLcEEKrFzHrDCDctsZjH2bIZkCbJQ07GU_BlGLe0NEOnCewOTAEm5YNZJlcdghqJ4xfYpaAoG1JXgV8aCFfiWySuvFJ3e-sbQ4V6dBD5QlU8VW2G-PG4-rHKeD_T6XnVKKcGNgve6v_Igj9gTt4J9L3cHYKpb1WX6gaBYTRZRHtP5mJcal4EYeIfQ5euZEFVjzhlnROYz2tEzj74G85oulvMa8kkXJoaGjT1gdD7EptDWvPzkytObDyYLlU4xvP6m3CjAzxuvXx_kkbBA6nvrApWnS8JwmGOTqsG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ‌۱۴۴ وفاداری در خیابان‌های لامرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451968" target="_blank">📅 21:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451967">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495f9c4e42.mp4?token=p937q1drLua1wUZJd-Ak8d2qu3YV8iTTjnyPxWkWU5uqF8g2IApqyUpy9DgNMUl9lOMFk61rptQepNGs32hKZ9yGOxuAywup7_axkXCQ30yAFjU2WTFHa05Q1pQ3Imiu9S3xts_3N8DvnZjUo7RaVOK3IWOG33mrl2FDEA796JoIug1hURn7rSD99PWmGnWoEDXx91xElbT-5scvK0uXUxgkGg5qIcareF2GqiaRwgcTQC-ykJgUC51N8YMahhZNZqojcTR64w1JjbfE1H_Qmppu9RMeLiZoBqHkGZoOwDVEcZyBltSfDW6Q8NHvJXbfmhDfGwq3oe2iqzCpdRl4CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495f9c4e42.mp4?token=p937q1drLua1wUZJd-Ak8d2qu3YV8iTTjnyPxWkWU5uqF8g2IApqyUpy9DgNMUl9lOMFk61rptQepNGs32hKZ9yGOxuAywup7_axkXCQ30yAFjU2WTFHa05Q1pQ3Imiu9S3xts_3N8DvnZjUo7RaVOK3IWOG33mrl2FDEA796JoIug1hURn7rSD99PWmGnWoEDXx91xElbT-5scvK0uXUxgkGg5qIcareF2GqiaRwgcTQC-ykJgUC51N8YMahhZNZqojcTR64w1JjbfE1H_Qmppu9RMeLiZoBqHkGZoOwDVEcZyBltSfDW6Q8NHvJXbfmhDfGwq3oe2iqzCpdRl4CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر صنعت: پروانهٔ واحدهای مستقر در شهرک‌های صنعتی که از ماینر برای سودجویی استفاده کنند، باطل می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/451967" target="_blank">📅 21:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHFng8fqhK5NhxsBa5p5FDVvf3btBK1O-YDpEByj5md8bYmC5bHjDEx6haszWQnViSvZuQFx4FeuXz_JP1GtCZshX7-PFb5evJ2YniqJJgRHVrvZmEfXtJAECZRPXDKR2Fd5IfCmsfEyYC6s_PGRPzoG0wzrOtnO0yWOPMecb33VoQDLl3yTBD7mhTYsc2uvY6Vz_8e7aP7A4ZZ8XqrKFvtNOEAXrVF8QPWA0tMn3h-__jd2CbBy1nn48A_71OAUUHyfswAC_fc-KaG8DZFruu6XhuyU21vDsNLP7pQnHtzi3yAqGYMblvmo8SKUU9uiB_p5KrPA63aIoF93UTmMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین پارکینگ زوار اربعین در خسروی پر شد
🔹
فرماندار قصرشیرین، از تکمیل ظرفیت نخستین پارکینگ مرز خسروی با بیش از ۲۰ هزار خودرو، پیش از آغاز رسمی عملیات اربعین خبر داد.
🔸
در قصرشیرین و خسروی، ۲۲ پارکینگ با ظرفیت بیش از ۳۰۰ هزار خودرو احداث شده که به برج نوری و دوربین مداربسته مجهز هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451966" target="_blank">📅 21:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581e56a147.mp4?token=CBisMYaZseh2FyyigSgUZWhVQvLwzDNlWoYO27KsDX8TH_jnTFY38OQL3TI6KXG0zFvpcc8gT_h6tGMo-34Ab-Smfw4AeqnaWdSVMvF57ge4pwvwvl2yls8EJ3oTApnnt_Fh_LaZB5nxpMaf4gg2LNibHn5boHhIzGRWMN4z16L3zdQx80WFfnt4BEb5OfHNXWjjVZbe3MVwaizbEOMDxJYrGaJR-RNQ7Ow5YP0AuNAZ1BDQdumqLzKQao9cQGShMNlG4Wt0cmthYUxJh19CoYzMVNb8indrGtrBseT3vl6JjZVEWDGtmMVTGLx8sDILaaSsyakvzZvALdonXVMSTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581e56a147.mp4?token=CBisMYaZseh2FyyigSgUZWhVQvLwzDNlWoYO27KsDX8TH_jnTFY38OQL3TI6KXG0zFvpcc8gT_h6tGMo-34Ab-Smfw4AeqnaWdSVMvF57ge4pwvwvl2yls8EJ3oTApnnt_Fh_LaZB5nxpMaf4gg2LNibHn5boHhIzGRWMN4z16L3zdQx80WFfnt4BEb5OfHNXWjjVZbe3MVwaizbEOMDxJYrGaJR-RNQ7Ow5YP0AuNAZ1BDQdumqLzKQao9cQGShMNlG4Wt0cmthYUxJh19CoYzMVNb8indrGtrBseT3vl6JjZVEWDGtmMVTGLx8sDILaaSsyakvzZvALdonXVMSTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازتاب داغ تازهٔ میناب در فضای مجازی
@Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/451965" target="_blank">📅 21:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cecb9a4af7.mp4?token=qvxJJZW6XWI11DxNKINreexJqY4DzA-x8KrfvGosUFUtgny1bdNkxUbtMFNVG91tc8c9ZxrGPbvl-nYHcLYtmMn6sqI3QAkgzU8FYu-BzvVvT7KEICO-X9bSWUhYtFln69nLKSGmWJ5H62acCiVzMQ4sgMWZxngi0yOL2qU_h0KRFFMM5oD_3LBvE4vy49K5KXbCq8HlLH8zLUg9qOeWe7RM0jq0kvR8VFo_odEwMamQdYusLhEjypdTs60usCRf_gyN4cdxTNv4_gqa7KX0tW9MOYNiTZxn3cibexhNxPKiDycNeElVI20MqVr5JEe-plY4FfC2lSu99R4FxXEAtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cecb9a4af7.mp4?token=qvxJJZW6XWI11DxNKINreexJqY4DzA-x8KrfvGosUFUtgny1bdNkxUbtMFNVG91tc8c9ZxrGPbvl-nYHcLYtmMn6sqI3QAkgzU8FYu-BzvVvT7KEICO-X9bSWUhYtFln69nLKSGmWJ5H62acCiVzMQ4sgMWZxngi0yOL2qU_h0KRFFMM5oD_3LBvE4vy49K5KXbCq8HlLH8zLUg9qOeWe7RM0jq0kvR8VFo_odEwMamQdYusLhEjypdTs60usCRf_gyN4cdxTNv4_gqa7KX0tW9MOYNiTZxn3cibexhNxPKiDycNeElVI20MqVr5JEe-plY4FfC2lSu99R4FxXEAtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیت‌کوین یارانه‌تان را قطع می‌کند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451964" target="_blank">📅 21:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6dQX2nTEFk4pgv7lSYfPAIGya1nueyI_ZeHgwTp41VJZhwjabvIqjkp0PJRWx01AAGHqN5PQfY7880RH9BtoPURhjxbC-o5NhhMdbMfoZs3Ne6sG-ds5utGfoDjF9wd8rplcEGRNT08E1JXhFqC8OdOFLW5thXd2NlgDV6W0VZlPWQwgInMeylBpjtmH9g0d_-z7Bb0JzVLrZU59jXNoxOxy3tLC2lFNgZDpBR4NinYRKdSZLpwJrf1QUcbRWiGjsPx2X2vJN6OeXyPKEldxF5LsoM_exLev7zY_eBeG-cefvKcFo8j63Zf9VYbW39mh3auZ7PnawRdYDnPotRnDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ولایتی: هرگونه خطای محاسباتی علیه ایران، بازار انرژی جهان را به آتش می‌کشد
🔹
جمهوری اسلامی ایران در مرحله جدیدی از بازدارندگی قرار دارد؛ تصورِ ضربه‌زدنِ کم‌هزینه به ایران، خطایی است که می‌تواند پیامدهایش بسیار فراتر از میدان نظامی به بازار انرژی و اقتصاد جهانی منتقل شود.
🔹
کاخ سفید  بداند که با تهدید ایران و بسیج متحدین منطقه ای و فعال کردن لابی اروپا، به امنیت و ثبات بیشتر نمیرسد بلکه پیامد خطاها را جهانی خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/451963" target="_blank">📅 21:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ccd5526f6.mp4?token=I2QzyPR61TRsHivZucYJRfEABvUK80qJKnnCZT0p_8VC2ronvmWiznZHXw6N2gaZK6OpbMbDOE4JOLmxRHYd1ct9z2NuYG62XndgMJncrjuxIKjuc9_BOVFEqiJtej22Gt3tzIg1kPZCtbC-pauDa0u_sxwN3PjNJh91QV4cCA0w2e-6G7CnqNdkjo5uOL1u-Hu-pIagjBwTj4u0nF6Jf6qafzoXoPITJQVUyyRBxIxma7W8A4oB-CBeI8I2DYr9n-j6EU8sAFOLXdti4hgWIS4sGASrwuaxXQ9mCvcD4yxH4_-99bXxmvqgD_NltAy7s3kIItHG3Y87nKAjbfCbDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ccd5526f6.mp4?token=I2QzyPR61TRsHivZucYJRfEABvUK80qJKnnCZT0p_8VC2ronvmWiznZHXw6N2gaZK6OpbMbDOE4JOLmxRHYd1ct9z2NuYG62XndgMJncrjuxIKjuc9_BOVFEqiJtej22Gt3tzIg1kPZCtbC-pauDa0u_sxwN3PjNJh91QV4cCA0w2e-6G7CnqNdkjo5uOL1u-Hu-pIagjBwTj4u0nF6Jf6qafzoXoPITJQVUyyRBxIxma7W8A4oB-CBeI8I2DYr9n-j6EU8sAFOLXdti4hgWIS4sGASrwuaxXQ9mCvcD4yxH4_-99bXxmvqgD_NltAy7s3kIItHG3Y87nKAjbfCbDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: اگر واقعیت و جزئیات عملیات اصفهان منتشر شود، خواهید فهمید دشمن برتری عملیات زمینی نسبت به ما ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/451962" target="_blank">📅 21:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f77170f3a.mp4?token=QFb-6WYRNK1rlpKXDn4HMVGvk_iFf-GPt-lqn6AVbAYalGBJq5EdQFRg5VACLQo87XCW95v0sr5lsg8q6oetI-MFuyMK6l9TveiRjWZ80Xc2ONk9lYqEvkSN6xMet2YzU5n40Rj8LIeLhSjrU8nEyiCqyYKm3kDA31ZAisWVqovYAF9BWE4Opbu-8ptvVpDB-w4Deal6cF_8P-ahXRogJHZia1G2zo-Y5-tdOMgvTR2CpI_kPviTFBT7Qjmazsqa0Rfp0P3ZUFvfq9dfoO0FLfvEPcGt6QabTjy_uuOFlAmB76n7vvks9k_XicSVSBawdoyg-_c50O0tYjAJvE9024aW2SKBvuYUpWLjvJQ4Bygrcvp1eWA5_gX_hciC9iQa-3k3MKsdgVRojPnT5mYgpN8gQDf1xiIb0aqpc3zShTzIKKaFwPg_ocpPOXuFLl74qlSBqPsSsB5xTllGwzD3QUy4p2_Cei03RTJ353b-ZU3phafiIYRRXc5I5Xfhw3YXA70T-fG4IvEnpc3RM9mEStTLqVfuHXN17_oEdVcV2IzQFlzHQEfQ0Ggje7zbcgqZN4QRqlCqgXxJqtyJM6a8stPr7YGNGu6jrOmMo5jM_LazYI7x2JdKO8jRc0hs6NpI9DhOf7gN3oklZSzKxmAnaeg5XAa80jWuac7yVPHxRs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f77170f3a.mp4?token=QFb-6WYRNK1rlpKXDn4HMVGvk_iFf-GPt-lqn6AVbAYalGBJq5EdQFRg5VACLQo87XCW95v0sr5lsg8q6oetI-MFuyMK6l9TveiRjWZ80Xc2ONk9lYqEvkSN6xMet2YzU5n40Rj8LIeLhSjrU8nEyiCqyYKm3kDA31ZAisWVqovYAF9BWE4Opbu-8ptvVpDB-w4Deal6cF_8P-ahXRogJHZia1G2zo-Y5-tdOMgvTR2CpI_kPviTFBT7Qjmazsqa0Rfp0P3ZUFvfq9dfoO0FLfvEPcGt6QabTjy_uuOFlAmB76n7vvks9k_XicSVSBawdoyg-_c50O0tYjAJvE9024aW2SKBvuYUpWLjvJQ4Bygrcvp1eWA5_gX_hciC9iQa-3k3MKsdgVRojPnT5mYgpN8gQDf1xiIb0aqpc3zShTzIKKaFwPg_ocpPOXuFLl74qlSBqPsSsB5xTllGwzD3QUy4p2_Cei03RTJ353b-ZU3phafiIYRRXc5I5Xfhw3YXA70T-fG4IvEnpc3RM9mEStTLqVfuHXN17_oEdVcV2IzQFlzHQEfQ0Ggje7zbcgqZN4QRqlCqgXxJqtyJM6a8stPr7YGNGu6jrOmMo5jM_LazYI7x2JdKO8jRc0hs6NpI9DhOf7gN3oklZSzKxmAnaeg5XAa80jWuac7yVPHxRs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاضری این پلاکارد را در دست بگیری؟
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/451961" target="_blank">📅 21:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef0b91dab.mp4?token=dim1lMhdNs7Z4evSoCs9ENYdBWwrZCxqIvL5_qjU_YedfI9hrNx5jtgU97guKoEcQgBnOF8h-dMviKakTQ5Kf04lJ2B0WFtarGksCPHZoh3DmOQuEcnMBMiDa--k_tplbhnS-lqCzkS3pcnxYJgDqJjIdaVhUWUrbXeZLqYKANi_PkNEg4Hgr6_lYNbKLLrDZR0vvKGv25ZT7DtAYEPyQ1dRkItoNIr9kZuGmDe0E16IS975p9lUKiGM9CkBMj8RxSwC4S1qUwaqMP4n_kOhLghXZelPurm7GYBUcHlfgswfPOCjCZfwRs6Qsy_CnuG7E3LF3DDgy6P3lwx-fDBxQKa1H1lbsyepcK1ZdOQUqjao0eiXAsOArF5zV2L1L0dsdYjH3RILaoQvYxbCMIJk583g06pLg8WIpEIbBBVDwcYG1k1zUVkNj0UdjBqisY93sIuAmXxhaXmlHHTeH1sPnIhNNGz8qqtkqv_ZaRfsL1OS1ocQ8jxE8Vd9IIUG7ouwVYrwVdJgD87Gjtzt415brmJhkz50GzAdquFNFDjW1xaxIOlSb9dbDs_OBoRVOtaObbIlsZ1Wvr32DLLlJlbiJsDVOECKh0b2AnFI96PuP-9zWHbMR_qEq2Ers-nA_xzkLkFexLSAgd89sgeqXvLuD6s3jTE5MTeRQWZv_ze7awc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef0b91dab.mp4?token=dim1lMhdNs7Z4evSoCs9ENYdBWwrZCxqIvL5_qjU_YedfI9hrNx5jtgU97guKoEcQgBnOF8h-dMviKakTQ5Kf04lJ2B0WFtarGksCPHZoh3DmOQuEcnMBMiDa--k_tplbhnS-lqCzkS3pcnxYJgDqJjIdaVhUWUrbXeZLqYKANi_PkNEg4Hgr6_lYNbKLLrDZR0vvKGv25ZT7DtAYEPyQ1dRkItoNIr9kZuGmDe0E16IS975p9lUKiGM9CkBMj8RxSwC4S1qUwaqMP4n_kOhLghXZelPurm7GYBUcHlfgswfPOCjCZfwRs6Qsy_CnuG7E3LF3DDgy6P3lwx-fDBxQKa1H1lbsyepcK1ZdOQUqjao0eiXAsOArF5zV2L1L0dsdYjH3RILaoQvYxbCMIJk583g06pLg8WIpEIbBBVDwcYG1k1zUVkNj0UdjBqisY93sIuAmXxhaXmlHHTeH1sPnIhNNGz8qqtkqv_ZaRfsL1OS1ocQ8jxE8Vd9IIUG7ouwVYrwVdJgD87Gjtzt415brmJhkz50GzAdquFNFDjW1xaxIOlSb9dbDs_OBoRVOtaObbIlsZ1Wvr32DLLlJlbiJsDVOECKh0b2AnFI96PuP-9zWHbMR_qEq2Ers-nA_xzkLkFexLSAgd89sgeqXvLuD6s3jTE5MTeRQWZv_ze7awc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشک مردم در وداع با جگرگوشه‌های ایران
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/451960" target="_blank">📅 21:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmlDkZ_dhicVU4KbEXA3Hej1h_0TLejnL33AtQ_GC7vzWo1iWkqHP7IfF_tI7rMSUdsmVa8ZlXVIz3-nVkSLK5veQROc3XluWCo46RUw834TpB7ZvdNlFjmlsLfQawTqJ3dELB9xEmSlUcQXI9HMiIuN8Tfzh9SzZs0QV2UyKAW24kBh5ft4ytDCViluM_MLTSkMJchbQwY6xT1vD5N_Uup52SXA0f3P_WYNVMjpoDYquezD3NKCOqyJ_Q5XT5KX_zirbjPJCwc5Z5sghytq8zMpa-66mS8_jLL61GcIJhaMapQUFPKwC93HoLNJa-ZsTbHHUEwfQKKHTQUkoJKPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: اگر ما نفت نفروشیم، کسی در منطقه نفت نخواهد فروخت
🔹
اگر امنیت ما تأمین نشود، هیچ زیرساختی ایمن نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451959" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fdcd5eb0c.mp4?token=OBeMMaysKIwsCWEr2JnJWmN4u1j356gaaQSKSR4aRz1zmKnKObntNI9woaVo8C_YnZy__GWPGiqpfbU566tZinn9VUpS7okMUDDeHJG39WdZYoIGQpqIRT3EDpY5SNj7Pdl0LPu0dwbHMDK-9UGUieG1D4uOLtgaFqSygaVnsvMpqR5quVlbxJYjjTuXEKIaC_-Ba28AeGrCqZ8u-3WBxBFzUp70W52zP0moJy8X9jirXMcb2_n2INZe4bdnNu-dF18Ph8f15rZ1bmHka__w1ypriKe_mK1CMmbweBvp1_O8PcJFlXhpMTc1PaIw1xPOwlZjIPaPZznbgOnSGk5fMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fdcd5eb0c.mp4?token=OBeMMaysKIwsCWEr2JnJWmN4u1j356gaaQSKSR4aRz1zmKnKObntNI9woaVo8C_YnZy__GWPGiqpfbU566tZinn9VUpS7okMUDDeHJG39WdZYoIGQpqIRT3EDpY5SNj7Pdl0LPu0dwbHMDK-9UGUieG1D4uOLtgaFqSygaVnsvMpqR5quVlbxJYjjTuXEKIaC_-Ba28AeGrCqZ8u-3WBxBFzUp70W52zP0moJy8X9jirXMcb2_n2INZe4bdnNu-dF18Ph8f15rZ1bmHka__w1ypriKe_mK1CMmbweBvp1_O8PcJFlXhpMTc1PaIw1xPOwlZjIPaPZznbgOnSGk5fMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این اهداف آمریکایی هدف حملات ایران قرار گرفتند
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/451958" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۱.pdf</div>
  <div class="tg-doc-extra">2.7 MB</div>
</div>
<a href="https://t.me/farsna/451957" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
دستِ پُر به میدان بروید
🔸
اگر برای اجتماعات انقلابی به‌دنبال شعر، شعار یا تک‌بیت‌های روز هستید، ویژه‌نامهٔ «خط» پاسخگوی نیاز شماست.
@Farsna</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/farsna/451957" target="_blank">📅 20:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749211c579.mp4?token=nIkCmpmo6_jePV_ABqvu4J0bEqmj5k8597iKR73TsVm6lj3TjCZM8F39x-Ve4u-YnolrhlWg8T6Sxbh8sueOXrDlOYUO4S-vYMKLJ35VvMaKf3coAjXJcZYAPv_GyDD1oK8ssUf7W80vbI5eGf5p0D8zey8MEWLxJHskZas2ez9MIa22aTV1xPJEJ3hNzLZ1lyutDDUoOprNFsBENAbX5aIB41BBhUCxPnirmW4S5S9aJF7rBXPbXn8v0WcjHUNRvYHeUMFZEcY0rDQ-GvpbImmbiEbUHpL1p7wFo0KpypEP2qbMEonNAXL2WoQBpxpSEbPFrSyCB2E0R5gcdvbRJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749211c579.mp4?token=nIkCmpmo6_jePV_ABqvu4J0bEqmj5k8597iKR73TsVm6lj3TjCZM8F39x-Ve4u-YnolrhlWg8T6Sxbh8sueOXrDlOYUO4S-vYMKLJ35VvMaKf3coAjXJcZYAPv_GyDD1oK8ssUf7W80vbI5eGf5p0D8zey8MEWLxJHskZas2ez9MIa22aTV1xPJEJ3hNzLZ1lyutDDUoOprNFsBENAbX5aIB41BBhUCxPnirmW4S5S9aJF7rBXPbXn8v0WcjHUNRvYHeUMFZEcY0rDQ-GvpbImmbiEbUHpL1p7wFo0KpypEP2qbMEonNAXL2WoQBpxpSEbPFrSyCB2E0R5gcdvbRJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: تلفات دشمن در حملات به اردن و کویت چشم‌گیر بود؛ آمریکا جرئت اعلام تلفات خود را ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451956" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451955">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ee193ace1.mp4?token=KLSgUTS0UNAy_YNp6897OHNLG09Eitp9aMI3hjcN6GUlQSHE3F4sakZUf83x4temnSVxqG7RKKeUxc6fhPBSJvryQUDEFII6io4r4pA5Ueh-ITKM7UovUVn36rAQJxIcFOxizC4eP3I3Kke4epDrkVyvhaq0TsXoeEpCR-fImgyzwPW4Gjp5eDYol6pZWwyPX3Yxk-mOQu_QxTwgYZ3ue-WZA9WjTWsfzwE-j6aY355lviyfQXhezgC37Jv28RFV8OVCZqu1-3KlPxV2PLqOkHec9PY5p5hME4WDlB7ePIcdf9ytXCPaV4xA12PJ78qGSAWEnoUuInbhgRDDESFRcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ee193ace1.mp4?token=KLSgUTS0UNAy_YNp6897OHNLG09Eitp9aMI3hjcN6GUlQSHE3F4sakZUf83x4temnSVxqG7RKKeUxc6fhPBSJvryQUDEFII6io4r4pA5Ueh-ITKM7UovUVn36rAQJxIcFOxizC4eP3I3Kke4epDrkVyvhaq0TsXoeEpCR-fImgyzwPW4Gjp5eDYol6pZWwyPX3Yxk-mOQu_QxTwgYZ3ue-WZA9WjTWsfzwE-j6aY355lviyfQXhezgC37Jv28RFV8OVCZqu1-3KlPxV2PLqOkHec9PY5p5hME4WDlB7ePIcdf9ytXCPaV4xA12PJ78qGSAWEnoUuInbhgRDDESFRcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، کارشناس حوزۀ مقاومت: تلفات دشمن در حملات به اردن و کویت چشم‌گیر بود؛ آمریکا جرئت اعلام تلفات خود را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451955" target="_blank">📅 20:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451954">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f01fb34c9.mp4?token=uvwhg8fDEh9YNhdwtGQVvrZLunYm2JVdUWYjwTFaJXZG7ZPckisVCQQduRyHR3SUmoAhlOX5l4fbBm4zQ2yek_sY5tHxDYwLUd3W9Q-1B31J5iWgxDZ2nbvsD-Ey8T3rRL5F4CJCCQdhfdQi9Kblj2M3AxZZ75sicXT3pBowQtZB_jcLTwPuyLWf6oGzXUTso909cqfn9YqqQdy6nfNm29W7A3QBM5QGqrBhninZXVUHmibjNK7QeUgelQv6uvO92bJK_iv-VYZ2N1ZIad1oxgOsRaefFvyK4lpzukNRf0oVNxtTNoMjCgmqPNDO3pfWMXo-bkAVbAN8RWBSxEEM0XTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f01fb34c9.mp4?token=uvwhg8fDEh9YNhdwtGQVvrZLunYm2JVdUWYjwTFaJXZG7ZPckisVCQQduRyHR3SUmoAhlOX5l4fbBm4zQ2yek_sY5tHxDYwLUd3W9Q-1B31J5iWgxDZ2nbvsD-Ey8T3rRL5F4CJCCQdhfdQi9Kblj2M3AxZZ75sicXT3pBowQtZB_jcLTwPuyLWf6oGzXUTso909cqfn9YqqQdy6nfNm29W7A3QBM5QGqrBhninZXVUHmibjNK7QeUgelQv6uvO92bJK_iv-VYZ2N1ZIad1oxgOsRaefFvyK4lpzukNRf0oVNxtTNoMjCgmqPNDO3pfWMXo-bkAVbAN8RWBSxEEM0XTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار بومی ایران بر سر پایگاه‌های آمریکا فرود آمد
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/451954" target="_blank">📅 20:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451953">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1tFojNqsJmxjLlmEegochPGCKzSQLdXOTvqF9TvKNovLmznyh36EUnwaWACZ5eLr1TxzRsTXd0n_7BcSMxkAcXYilHJPkfXr_kih7UACicYmxp_Hqg0hRxh0saW1rXzthYprN78NCShCVyGR6Y-HqNbe0ZwnFeaKuuFTiq8c4U_VkgSYLHGCW7TayjbgmbPhWgkD9eIsJ_il9EbsF6eJRJoQvSDmMEyVzH8ZtH1sJOMFLz3kMaM8zy-5QZPMN-qdtYPEqfiZzyhOhS5LS-PUnQrOyssYG4VCLu03s1EUZCujwsxR0B--pqNLQtyiFnBcl2b2qz5jGNgi0WFTZOkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مورفی، سناتور آمریکایی: ترامپ به‌هیچ‌وجه در دستیابی به توافق هسته‌ای با ایران جدی نیست
🔹
توافق هسته‌ای ترامپ با عربستان برای غنی‌سازی اورانیوم در این کشور موجب به‌راه‌افتادن یک رقابت هسته‌ای در منطقه خواهد شد و انگیزهٔ ایران را برای محدودکردن برنامهٔ هسته‌ای‌اش بیش‌ازپیش کاهش می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451953" target="_blank">📅 20:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451952">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78abbcf8a.mp4?token=R7xnaE5y8kIUCqntoGWOUKWL0LAGaN0G3AaNrgUSomt7djJKkP7-_BR_XmfMuh2KYqv0HTS18rblGWPRAsQyd6Q8stUTFpZnvLpb64ONURrI3P43vNnUZDASUSAegg4xeUjAmlUvHz-b1ks1sdjrY_ccrf3oFydMXg8eWIeL06qTMfckydYXnFbAnOvv3PtkUUmZRO6Y_MRljeRBg8HvYs6GY3vvF-BipIh1WWVyg-_PWX1gy69m-4MewfVtGuFrHj5RXbSpPd_df2s092aDNW599SVsvtnP6_BAji5vrmYTLw3xmylrnpDxpiOZIj86pXAGCAuIQGdsqT59YRop6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78abbcf8a.mp4?token=R7xnaE5y8kIUCqntoGWOUKWL0LAGaN0G3AaNrgUSomt7djJKkP7-_BR_XmfMuh2KYqv0HTS18rblGWPRAsQyd6Q8stUTFpZnvLpb64ONURrI3P43vNnUZDASUSAegg4xeUjAmlUvHz-b1ks1sdjrY_ccrf3oFydMXg8eWIeL06qTMfckydYXnFbAnOvv3PtkUUmZRO6Y_MRljeRBg8HvYs6GY3vvF-BipIh1WWVyg-_PWX1gy69m-4MewfVtGuFrHj5RXbSpPd_df2s092aDNW599SVsvtnP6_BAji5vrmYTLw3xmylrnpDxpiOZIj86pXAGCAuIQGdsqT59YRop6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همهٔ ایران، همدلِ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/451952" target="_blank">📅 20:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451950">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7S2Kgs6ZDNUIehYFMG8_LvFg6N2ciFUOAA-CYGBNdmvId4WeKR07FFyuhdyD0DIGV2EFhyUfMI4-6BDkHtvWDKSmrG4u8OQrETX7T7oyWUvF55qCHjwNgdzdvh_110aHsWqobuO2UjYDDBVfIJ_kOTYYYjZ3FU-l8r6Y2gfNsnDKZfFYOJ4DjNu7TiEztj0Bg35OKO_oXLRS3sxyM7MhgVyYNcZu-xjcl2j-bmyFs0gkWuK42eJQhmFuhhcnt9IijMO3g_VGyvphwCuSXqFtBmtH05hzrEKWkmsL3xkOpEwnY_f5XJ9WvZOjfZ_sMhQHH9PO_ACSPNVxVzosqcbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
مجمع عمومی عادی سالیانه با حضور همه سهامداران برگزار شد؛
🔰
مُهر تأیید بر صورت‌های مالی سال ۱۴۰۴ بانک مهر ایران
🔸
مجمع عمومی عادی سالیانه بانک مربوط به سال مالی ۱۴۰۴ با حضور ۱۰۰ درصد نمایندگان سهامداران برگزار شد.
🔸
سال ۱۴۰۴ نخستین سال اجرای برنامه جامع راهبردی بانک مهر ایران به‌عنوان سند چشم‌انداز افق ۱۴۰۶ بود و در این سال دستاوردها و توفیقات گوناگونی حاصل شد از جمله اینکه منابع بانک با رشد ۶۲ درصدی به ۷۰۳ همت رسید.
🔸
گزارش ارائه شده از سوی دکتر «غلامرضا فتحعلی» مدیرعامل بانک مهر ایران در مجمع عمومی حاکی از افزایش تعداد مشتریان به ۲۲ میلیون و ۷۰۰هزار نفر، پرداخت ۵ میلیون و ۳۳۷هزار فقره تسهیلات(بیشترین تعداد در شبکه بانکی کشور) به مبلغ ۵۰۶ همت، افزایش سرمایه به ۲۲ همت و حفظ کفایت سرمایه بانک در سطح مطلوب بالای ۸ درصد است.
🔸
در این جلسه گزارش حسابرس و بازرس قانونی قرائت شد و صورت‌های مالی مربوط به سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ به تصویب مجمع عمومی رسید.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/451950" target="_blank">📅 20:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451949">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🎙شرکت نفت سپاهان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjBQ8-aN6iAqSod6gm2E-1dOu7mqATpxEm1dsnyz11AfQlXSO4HhDLtN_QONzV5uRniD6UizdIqdqObsG3KHkX8_Cw4ZKSR6T1yKcBwbEHiXUZ426TeeK7ky7YLI2bDXFMtUOqykdOySsCxuQiio8OgbBg_Ia99WUT6Qfe0B5NvFYNxBQJFJdGhxWyPL_xag_7rKP9eeL0NZ5e1MFJWrgd5SprKUUwwppYxyCPt9deZt1Wdqp-X3VhqBUZ0BC3S1m1hWvRdq_SCy-tYr20oVYhmiKg4avyq1UJ4r4xzbdRT4l8SgJ3sN2rbl5DZKuiFxoHIv1tVA5lV0oI7PYoPVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#خبر
📌
در مجمع عمومی عادی سالانه شرکت نفت سپاهان که روز چهارشنبه ۳۱ تیر ماه برگزار شد به ازای هر سهم ۲۰۰ تومان سود نقدی تقسیم شد.
💢
شگفتی سهامداران از رشد ۷۹۴ درصدی نفت سپاهان در بهار ۱۴۰۵
✍
بر اساس این گزارش مجمع عمومی عادی سالیانه شرکت نفت سپاهان (سهامی عام) برای سال مالی منتهی به ۲۹ اسفندماه ۱۴۰۴، روز چهارشنبه ۳۱ تیرماه با حضور حدود ۸۵ درصد از سهامداران در مرکز همایش های بین المللی ایران برگزار شد.
🔗
متن کامل این خبر را از طریق پیوند زیر مطالعه کنید:
👇
https://sepahanoil.com/NewsDetails/3422dd53-9ebe-459a-db6f-08dee7c0a1d1
●•• روابط عمومی شرکت نفت سپاهان
•┈┈••✾❀
🍃
🇮🇷
🍃
❀✾••┈┈•
🌐
www.sepahanoil.com
🔗
t.me/PR_sepahanoil
.</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/451949" target="_blank">📅 20:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451948">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/451948" target="_blank">📅 20:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451947">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d47a6f8361.mp4?token=kCwdKjLaNej372zJ-5jmyKXpv_Pn7uDUMkOLp4ioz12e_Xa9owesd6nYFwEqC-BwmUsFJqaftsR_ogFBiRrXnRj9z8A4CnkvWupeALf5UGjzgn3w6tfWYxwFmcqNkSUEB28EoGYxTEkoBHeHXPFEviIY507Z-tBTV_O8rrH19nmvDqn9TXwPUj5vggg5d94U30jK3mnq9PPL6AP3kQ0rb8JJSZykmeOXDCVvnG3fr2rmn7ylDowNHzr4k7hHlUqRKtPlsZ9i4Nw6Dq3FrrXRP-ZBpuwemCwOBLUTYQ3vpyI2muiNvxmYzjnqZ2uqwy055nFwO2WwIjYiSjVtt5baOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d47a6f8361.mp4?token=kCwdKjLaNej372zJ-5jmyKXpv_Pn7uDUMkOLp4ioz12e_Xa9owesd6nYFwEqC-BwmUsFJqaftsR_ogFBiRrXnRj9z8A4CnkvWupeALf5UGjzgn3w6tfWYxwFmcqNkSUEB28EoGYxTEkoBHeHXPFEviIY507Z-tBTV_O8rrH19nmvDqn9TXwPUj5vggg5d94U30jK3mnq9PPL6AP3kQ0rb8JJSZykmeOXDCVvnG3fr2rmn7ylDowNHzr4k7hHlUqRKtPlsZ9i4Nw6Dq3FrrXRP-ZBpuwemCwOBLUTYQ3vpyI2muiNvxmYzjnqZ2uqwy055nFwO2WwIjYiSjVtt5baOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرنوشت سربازان آمریکایی؛ عمودی آمدند، افقی برگشتند
@Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/451947" target="_blank">📅 20:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451946">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNPlEP5tJcXfILZlndIbW7ZwoRTtOU19cPTUGvv7ka2wbfu4FNJ3IDwatwYZIEnQOWd56BETeUaPRlAwUYQKWzBACezajg2RNsc0ZfOqdIUAZbpLHH_kYgzsv_80WKhzeUU0cIU-XIuHr30Q-9ciDHbjCzPYFr2WX-RjwU5XCWQkUoLnzEBXm6vWE8EWj3T-g5UEsaaNN1z7e68KV9Rm3gpcqCxKvLVABY_M_0HHqk2pDsEYYg-1uf8nA0n6sj6oA4Uh7pwepnd1SuNIhtGR11Ws3EQ_JRkmJG7TQ3dY3Z70-E2tcFbB1wrm_HoZihN-pN2-RWDh3fiAVKs18KZB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قربانی اپستین از ترس انتقام ترامپ مخفی شده است
🔹
یکی از بستگان زنی که در پروندهٔ جفری اپستین، ترامپ را به تعرض جنسی متهم کرده، می‌گوید او از ترس انتقام ترامپ خود را پنهان کرده است.
🔹
این زن در سال ۲۰۱۹، ۴ بار با مأموران اف‌بی‌آی مصاحبه کرد. او گفت که در دههٔ…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/451946" target="_blank">📅 20:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451945">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT1tbbjkc1-Vk-or86OHD999kEIaue0mHl_cfUh7bCr0YdJeas1I7nQ-1Rcu4eXcBm3IpxE0UTaycTpxcpQPYujWlUPBMY5LOBMqCFy0dowqnt1SM5usUhfopgpGsXoZa1NHDjtFYXdLYtFY1rGUgnhbn4o4oFPR5geFkGTgXuGBr8Ny-RyxZ8Qq1CjQHj2HDaiQM2SvieyD-BLjgpNyTECT1AuOAi6vsPBia5Dtx9NYByaXf6ekEic9G9EwhmlHnUHxrcMtcsezZL2E8c7aeWn3N3_UMBAcWwoPZQDht99EBtFFyAgC88NPUJlyhJtG_pNyyLpK2bdrKAGb_sc2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ مصوبهٔ جدید دولتی برای کاهش قیمت گوشت
🔹
دبیر انجمن صنفی واردکنندگان فرآورده‌های خام دامی از ۳ مصوبهٔ جدید دولتی برای کاهش قیمت گوشت خبر داد.
چه اقداماتی تصویب شده؟
🔸
واردات گوشت از استان‌های مرزی بدون نیاز به مبادلهٔ ارز انجام شود.
🔸
ترخیص گوشت تنها با داشتن قبض انبار امکان‌پذیر باشد.
🔸
ترخیص کالا بدون نیاز به مجوز انجمن‌های تخصصی و مجوز شرعی سازمان دامپزشکی انجام شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451945" target="_blank">📅 20:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451944">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNrGVwSCTPe8InMccIW8m9mLfPc4vwgKYcIQ6zZkCjKfRf52RTK5nN8_Mseekaxbq3lixbt7o_afeK9gFkftqLNkav4dKBpdS_D1O_yql7HeoW46td9oCObg6w0cjkyljyz6ktVp_j4Qn-iELkqgZCjEZge3npk_1IXnoffVACAttx3siu_My7P7M-3NY8fxAYNV6YvVsExmPQHHy5JBrhGCt-EXjKP6Klumete3Wwt1UtxtlYNkBUfzzcEQH1rTN-KYCo6bsy6874iZs-HsZL5d04JTT579Xju4iHDIyJh4CvZnU1qIXhDqZoNp-yhGVF-4qXDpD0YEfvNZl-LGbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت عادل فردوسی‌پور از دسترس خارج شد
🔹
وب‌سایت «فوتبال ۳۶۰» که زیر نظر عادل فردوسی‌پور فعالیت می‌کند، از ساعاتی پیش از دسترس خارج شده و کاربران امکان ورود به این سایت را ندارند.
🔹
همزمان گزارش‌هایی دربارۀ احتمال فیلتر شدن این رسانه ورزشی منتشر شده، اما تاکنون…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/451944" target="_blank">📅 20:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451943">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeMSuz4EvNk5nAbb2DxNKumaShczHWQp3kAV0hAN_GaBXml0qOrHnu124112xZxLeaymBUCdWL_wxSUxQAzeLakM4pWhJskxOV4CVpjOnYZw4ZPZ2qpjC34Acozzff-wZHGnavFgwMZZfdRtZkCv_bOk5-fbUVpd4g1hF7nqGiJu0YhtCiqtw98f9jmnyoLn3Qt9MlkpLVQuly7ZtM318xKQ13bsblKp9KkuwZa62F0dbzDFDtX4h6z7cPD0MnHq6vWkOF0EjNWXLpuGGPC3iefvTtLW7I5xV9mN5xcGXm3PKLoJMqTuFpx79y2zDAaY3OKhu2XTM2YwmAH3lw6Qzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارکینگ بزرگ اربعین مهران آمادهٔ پذیرش خودروهای زائران شد
🔹
شهردار مهران: پارکینگ بزرگ اربعین شهرداری مهران پس از تکمیل مراحل آماده‌سازی، تجهیز زیرساخت‌ها و فراهم‌سازی امکانات مورد نیاز، برای پذیرش خودروهای زائران اربعین حسینی بازگشایی و آماده بهره‌برداری شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451943" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451942">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bdecbfc87.mp4?token=E2E6TECgHHbjBDZa4BGpax4_mZUHC6HnQe_IN2O8d9TQ9hnsDRC16ZPaFGEErOS72R8QDxQEokoGtXevgOsawWpCPMS29Yvj1mtstk8vYJwL64TtDil4IIy9dU-VH8jnTGjCPLHIm7ixDxiBs1Cu1KNoAHYA6sXHQ9u3opPENEcgmZ84XqCnAyHiIxQztv0TP8zyqBU5ACYVEUdoRcboQIvJYgWX5Iw8LmMgqSVf0vPf3LEIdLucv6M0j9Lb5iFGP7uzyRSlMhM2IgE4gXwyxzWm1qzgTO4EFZ5vf1aX4Bh0mLVuqyBy0fUtMkc3OMkWlAu_2Ji1AgWFftFaIFZNQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bdecbfc87.mp4?token=E2E6TECgHHbjBDZa4BGpax4_mZUHC6HnQe_IN2O8d9TQ9hnsDRC16ZPaFGEErOS72R8QDxQEokoGtXevgOsawWpCPMS29Yvj1mtstk8vYJwL64TtDil4IIy9dU-VH8jnTGjCPLHIm7ixDxiBs1Cu1KNoAHYA6sXHQ9u3opPENEcgmZ84XqCnAyHiIxQztv0TP8zyqBU5ACYVEUdoRcboQIvJYgWX5Iw8LmMgqSVf0vPf3LEIdLucv6M0j9Lb5iFGP7uzyRSlMhM2IgE4gXwyxzWm1qzgTO4EFZ5vf1aX4Bh0mLVuqyBy0fUtMkc3OMkWlAu_2Ji1AgWFftFaIFZNQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بالگرد ارتش آمریکا دچار آتش‌سوزی شد
🔸
یک فروند هواگرد ترابری نظامی MV-22 Osprey متعلق به ارتش آمریکا در جریان یک تمرین مشترک در فرودگاهی در آریزونا دچار آتش‌سوزی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451942" target="_blank">📅 19:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451941">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع عربی: مقر تروریست‌های تجزیه‌طلب در اربیل عراق هدف حملۀ پهپادی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451941" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451939">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
فعالیت پدافند هوایی در شمال شرق تهران
🔹
دقایقی پیش مردم تهران از شنیده‌شدن فعالیت پدافند هوایی در شمال شرق تهران خبر دادند.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/451939" target="_blank">📅 19:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451938">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnM-TP_wnQdXLg2cscTBMaRlrcVjqFJAIhNkc7Ol7xNTA6v_Tdh_fwEsucOlNCJScyCTBTkcHg787PScmMgo22LozmKHlyRdLBamjeQJRD_1a3YE19dRRNlhpJv85OBJdzyHHU_p0PAf-wwGfx_ghsNS9qRqSBzkCcbDf4OehAzs6zIy84erGueyu6ZukMg8HSbtTlcSFl82PImVh0UTkXKbHbqiwx5Qg13Z7L-6Jsl-7HfD-_wSLyCl4Z_NP9xCqXvMBFV1KrLs1y1WSJLsI5nINgjWl4MhnST1LhhCKnLLVOd0HOsgX5fNmiWxxli-Lbu_CXRwouNpp_zi_kV3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردوی خارجی پرسپولیس لغو شد
🔹
شورای برون مرزی وزارت ورزش مجوز لازم برای برگزاری اردوی خارجی پرسپولیس که قرار بود در ترکیه برگزار شود را صادر نکرد و برنامه سفر سرخ‌پوشان در شرایط فعلی لغو شد.
🔹
کادر فنی پرسپولیس تصمیم گرفته تمرینات این تیم را فعلاً در تهران…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451938" target="_blank">📅 19:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451937">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8943c4345a.mp4?token=XuXcpQfvC0kqV-nWPB_Qzwlxr0EPmw5bw0oozYr-VE1g1d-HJ2wXYyzQN9P-k8PRjpN8IJDoXuQ11JjxQVNOiLXk8_1xReH45QFGymo0OU4j0pDkTZVEW2x7cWRR4aCIHzwImUQtC4-B7rjkR9xJy4Lh32drs59cjCT0-6FM3EUX80zVOACMlnirdy21h0x13x5eXsfagZ3ih5rNvfTAThakX3at2N9QPxOoWksGP9uN3h_maJz3hOkqXpocraZvnODMgtxhP8oF7CeRmg5tJmPzSf63mW4dT9GPMD-H4z4sO_lD8gVqCcfl1qNj9XRxcGkPBUkB0KU97kG90Y_fS3G37YjKWWgH1TZTKBE1470OTlC1fmGfvfcYYDZDBjqZVDfmZEWLHadMDiiQ_aSRXULYNELL6swYzMPgnUjaxsUK7L3tUhWVLnYwlWi9JdboBgsS_h1YuiHsNv7P-9RjbeziNK_7OVrMQO63IWyOxWUdCGYArGXUpFdYOaCbE_0bNgb8pWwYmRxvyxuVtyqTZHAH-ub8dpoiYZjPSp3pSkeaSELm2yVA5r-1KykZ6hPXQyoZsHgp3NG8xfeE2mIyhnVs1c77_eTcMR-b3pGnulOU3CFuq_LQhs8580xg0_ZCDd1VA-BlrplC4ebwC-zDv3Y3GgLbbWmsqk4jv9SBWX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8943c4345a.mp4?token=XuXcpQfvC0kqV-nWPB_Qzwlxr0EPmw5bw0oozYr-VE1g1d-HJ2wXYyzQN9P-k8PRjpN8IJDoXuQ11JjxQVNOiLXk8_1xReH45QFGymo0OU4j0pDkTZVEW2x7cWRR4aCIHzwImUQtC4-B7rjkR9xJy4Lh32drs59cjCT0-6FM3EUX80zVOACMlnirdy21h0x13x5eXsfagZ3ih5rNvfTAThakX3at2N9QPxOoWksGP9uN3h_maJz3hOkqXpocraZvnODMgtxhP8oF7CeRmg5tJmPzSf63mW4dT9GPMD-H4z4sO_lD8gVqCcfl1qNj9XRxcGkPBUkB0KU97kG90Y_fS3G37YjKWWgH1TZTKBE1470OTlC1fmGfvfcYYDZDBjqZVDfmZEWLHadMDiiQ_aSRXULYNELL6swYzMPgnUjaxsUK7L3tUhWVLnYwlWi9JdboBgsS_h1YuiHsNv7P-9RjbeziNK_7OVrMQO63IWyOxWUdCGYArGXUpFdYOaCbE_0bNgb8pWwYmRxvyxuVtyqTZHAH-ub8dpoiYZjPSp3pSkeaSELm2yVA5r-1KykZ6hPXQyoZsHgp3NG8xfeE2mIyhnVs1c77_eTcMR-b3pGnulOU3CFuq_LQhs8580xg0_ZCDd1VA-BlrplC4ebwC-zDv3Y3GgLbbWmsqk4jv9SBWX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مامانی ۵ ماه دوریتو کشیدم
🔸
مادر شهید امیر علی کمالی از شهدای میناب، امروز بخش دیگری از پیکر فرزند کودکش را به آغوش خاک سپرد‌. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/451937" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451936">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">چین هم از محاصرهٔ دریایی یمن مستثنی نماند
🔹
ردیابی مسیر کشتی‌ها نشان می‌دهد یک کشتی خودروبر متعلق به شرکت چینی «کاسکو شیپینگ» نخستین شناوری بوده که پس از دریافت هشدار نیروهای مسلح یمن، از ادامه مسیر در تنگه باب‌المندب منصرف شده و تغییر مسیر داده است.
🔹
همچنین…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451936" target="_blank">📅 18:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ajs1QBBmjHsUvDrya_b8IrllCfeIeEP2VQ3AkDC48bpWpmyCZ9-OXAg-LItr5f-1SBBbFJNeAuaYMZLMFcWhnAQumajDj6TlJRRjXKIkjTK-R1uRDWFzOj4E_bFC9ROkxc1HE8XNGdoBkaZ7ifgH_TY-CqVavurfXVpC02u4bNzqUh6EwKb21ifBJdTNiduakfnmV4KK8EeMy5yTGSIuEyxtuOORbY_-ZBQGoJfzZz9w9iPRATljMVBg8Lex_dKYxz32IDgvrt9krmBjCqhYh482KviLfnsp4U7xV_BkBgf9NfuQvoA5VUcUVhIeAefIPDup4QH4nKgEksQH3xtOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت ۱۴ ماه نقش‌آفرینی بانک صنعت و معدن در توسعه‌‌ی‌کشور
بانک صنعت و معدن در دوره ۱۴ ماهه منتهی به پایان اردیبهشت ۱۴۰۵،  با رشد شاخص‌های کلیدی عملکردی، مسیر حمایت از تولید، توسعه تأمین مالی، تجهیز منابع، گسترش ابزارهای اعتباری و پشتیبانی از اقتصاد دانش‌بنیان را با جدیت دنبال کرده است.
این اینفوگرافیک، مروری بر مهم‌ترین دستاوردهای این دوره و روایتی فشرده از عملکرد این بانک در مسیر نقش‌آفرینی برای توسعه کشور است.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/451935" target="_blank">📅 18:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoPX4CffV3eGVnd424oZqSU2T9QQqfIRNRAlmpdnWmnQlchrCIaS-PT7haip1lrfLY3aoyaavYSZZEWWr4scGRx0jkuHETL4ZKJgTxhdR_w9R4QCMSCfDxdWYyYhTarpr0G2WeaaN79Afe2siOxTxPBG6oeKujOn0US8ab0iAeT7Rna1KRx4Eltwekln-PmUXlWbQloVRp5pxXa_dinkcBi1rC2Q81hH0kKk78iQsz4rfan3pPQfI2D-WYJJMQ-JGIzi-8D-xsnDA7letic8bWKZY9iYOuLuKE1fF5muRT867Mi6uYJgXIOyu3dIDU1IfFS2yuvfrfEZl7MfKzRNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان خرید ارز اربعین ۱۴۰۵ در اپلیکیشن بله
خرید ارز اربعین یکی از خدمات مهمی است که زائران سال‌ها در اپلیکیشن بله دریافت کرده‌اند. در اربعین سال ۱۴۰۴، بیش از ۹۵ درصد زائران ارز خود را از طریق بله تهیه کردند و امسال نیز این خدمت با هدف کاهش مراجعه حضوری و تسهیل فرایند دریافت ارز در اختیار کاربران قرار گرفته است.
زائران می‌توانند به‌صورت آنلاین و بدون معطلی، تا سقف ۲۰۰ هزار دینار عراق ارز اربعین خریداری کنند.
به صفحه خدمات در اپلیکیشن بله مراجعه کنید و ارز اربعین را تهیه کنید.</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/451934" target="_blank">📅 18:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/451933" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451926">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-9i2CYyQ_2lABY03BIkZgYX97PhC_E-TUYlbYoR9OlkBtqdwzEkZEJY0Ev1P3uIX_hB67MRnhcTzF2nLu5kzYlfXhxTFRvpZuQYLkdavPkmHz_SiKvq0PAsOAgj-pSmwjieWnzagExs6OvuVgW0ZdqegHdH0WMtukrHW27VW9M2LSV_319nIGtcc_oExplUC0HS_LxxrAsWO-0vSRF7WRGY-bMLq25Tpvaxb8G-b0pCRNOkX-cjlAUNL85fuPAAYahSSgAAkQrvTJEjOl5uZ52zjV-nyPXgkc1GjbIMpFHxluAzgDZiEcq6BVULS08zhqI2SRnyNUwgrCjhs5-tsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX1vymeQVuaEWv1mS86WYHxl2tzOQviI_0jBKdpGMYqFfkU3e7Y8L82OcYf_vh3xdBuwVYMdkZ3RyXzvSa_xImnyQtSMTHw-kFyOjp0e1XdZk0c0w1Jg9skxmC31TlxCBksRgNJtuwief_5Ycmp0z47h26OL6MvNP4gqnamfgw2QeoWeQU2lWsBlh-Witgg8fDisNLKSG1lp0wFucAvP0HhZ6yrWdD_Y22W00WUq_ZqWDruLXC_vG6Dx5Xtq4MPsUAAURVXGAYJF26FR0U-knp2ljmgUkLen8KNq2hQJGb_ejsKA-ntpTZMkzXE5x3CIMsJzN-oo5a3O8YmULbONJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lFyG8o1XxUdkdZ2wz5XCM0r6Jey_JazUnEhTVa_A8aqzW3gLOIRmgvemXkMJ6qfBv6gv6D3h7VvyzseVxL-tjuTt3FGP3bcWlz8OvwGQEpQpQ0spzyAi-L2B0qwXVUDcpbuqclkRtqQDncVJr--P0_UVoOn1uTv9zQ3fNT4GfiRRbgClvnjxlLIWz642R4r94EUModhtwjOSGhuVj3KGRIVJtnlIJDI1clU76FkZ93hF_gIWb6nZmvbMOnL8yBr7AfmJd0B9VXPHwbQxrE2uSokoNQovX_RoXhryE3eDLs1E35P-19o_V0IjtK22K1HI9JvNU3MoaEne87DCzsDGYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gPz3rJF9SN3hsNjyd87LIvNoFtI_yZsPzdiR99kpqQfcsH6FR9ed2L12ycEZITS77iPI4zczt6tPs2DRbXP6Ed_OFmOrHVs-xb2HWql9H8VrBd5_5HbRAGWFRnto_T2m9V1zRsZMhmKlR0FLvw3afEwi70QPf_yYYWb4Q04-F7SS1fA3bxrAuK1M-talXx0tffN0NWB1qIq3qDTxs2YnDiP1q5KszGt40UQR2s40oYn1dznRRyEqMnhifS75T5oyFEBQS0iuWideU9vFs9aufctG4bgonrSIy8ivW4ctfWRrSA6vpTdq0lmnMByACSgikWJQ61y1j2cogdqGqxudhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lfFTRoaaMCX0EnLXDhobFm092G_JWxQjbPcvXFwBeSN3z5LB6NbVs7STcpyYUKAfstcP8P6qyxC6cSlg31kdl6sv6rUXE23kIzM6oQq4KgtrmwcLVhhlARnAZmQSnMMHJi7YIvvDIg6hLFVO9iQV1uCWZZP1Wc2O_X3IO8p4UuPE5tFSTlkKKEvr1SXldLhK9VLrnItcK_XVCT53vGvRr5TO9ss-JhXyK04kaAUlBsIMJ4AW0PYNXBUjZ61KoZdrmpHMjEmaLU8uFutw50UG8sBnZ51hIquhLlSXbd1gIqlMMzhtJ_bCiWkMXdw7V4dnausaqzyyF_2vwTn6Xezlfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lDHH7FTEED4StdjF5VB6ujfNrPPELBPXTWR-vfy4TYfrFFej6tAD0u6PyZB-Fvetvg685XmjKGM-ved59wUfebigHsfzVOpPk8kIb-03NJgAZINQEyoAa5Q8ZRbbm_A3EGom2dDyr5DaoM7Zy5O7X7yWglZIvhs6uU1KwZ19s1p1rl4kSatmNRlgrDoOhHlg9PvCVokabrz4eG64mTNAOhmQ5CjqRQ7rZKI8pdNxcpkA3DWEG23SRKHapqXORSaR5-eGpciKuFaX_h1uforJpo7-wQRCKqmBeLP7XiGg4PCjcp0ZV4ketK0AA_xdbApbYUZWSpQ8qMkxjyoqMydGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRCnJ-RY-A2sl-lTrSP9T8vjqoPLxhIOwk8lawx9IqhHZShModtdd9uEtXHRW59YixNaRDrCMw43SCmzDVVKig8fD3D2L0KMpAwmhoG2ox--hl-m-PIlvmOvpPs1TmdNv-_zySXwfFpiHRVaBUlq7o-4tR2DDG0Pfz4ZcISOj0oHa4JRQY7YimrOODzVqMhM9Y7ZhcyZFUNu9sV15aDhetxxanywqXh0LtqADP14eXSBr3-j7b8XCuQkM-UsvszvL6QPFbkfdYtDudJAZrwtX4mQkMjCZlydGZQG1t67uZEHmg_UXJUEYCq4FmHc6-mKu-K3DkhFrBR96zVzcpBnQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رصد ماه در حرم حضرت شاه‌عبدالعظیم(ع)
🔹
شامگاه سه‌شنبه مرکز نجوم آستان حضرت عبدالعظیم(ع) برنامه رصد ماه با تلسکوپ را برای عموم زائرین برگزار کرد.
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451926" target="_blank">📅 18:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451925">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxrhsggMckuUcw2JSzkioVDGPZ1cIb1KvIswnW4cswKGrEZJAI7T8BMEH6CuviZHQ2Yn8nHgO_jLbxutdCjgVd-UYLcDt8UxZ899i6YaCMPHAZvSYj3vJGoty6XOtfvfwW6XWE2PpiolgM4zpGh284TLPy9XTiO5TpJ_gh9re3rjoRGWovITTwDtDDn4B5KXqkPCacIr7MLdfHp8CbnEestdAuZ5waZ6se_CHiU2cgfi1AbMzDRjOnuGIYkArYmYisVuYhQezD2KbkAhAtEBH44bMUrs1L-_YjXnwYUTuUc1PwaWhq9HldbIVXcS6Mv8k10ZfMxL2cz4cEx4IWjb2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش‌مصنوعی در آزمایشگاه از کنترل خارج شد
🔹
رویترز: اپن‌ای‌آی اعلام کرد یکی از عامل‌های هوش مصنوعی این شرکت در جریان یک آزمایش امنیتی از محیط ایزوله خارج شد، به اینترنت دسترسی پیدا کرد و زیرساخت‌های پلتفرم «هاگینگ فیس» را هدف قرار داد؛ رخدادی که این شرکت آن را «بی‌سابقه» توصیف کرده است.
🔹
اپن‌ای‌آی در یک پست وبلاگی توضیح داد این عامل هوش مصنوعی برای ارزیابی توانایی‌های سایبری مدل‌های پیشرفته در یک محیط کنترل‌شده در حال آزمایش بود، اما موفق شد محدودیت‌های محیط ایزوله را دور بزند، به اینترنت متصل شود و برای انجام مأموریت تعریف‌شده خود به سامانه‌های هاگینگ فیس نفوذ کند.
🔹
هاگینگ فیس، که یکی از مهم‌ترین بسترهای میزبانی مدل‌ها و مجموعه‌داده‌های متن‌باز هوش مصنوعی به شمار می‌رود، هفته گذشته از حمله‌ای خبر داده بود که به گفته این شرکت، از ابتدا تا انتها توسط یک «عامل هوش مصنوعی خودمختار» انجام شده و با حملات پیشین تفاوت داشته است.
🔹
کلمان دلانگ، هم‌بنیان‌گذار هاگینگ فیس، پس از افشای این موضوع اعلام کرد این شرکت از ابتدا احتمال می‌داد حمله توسط یکی از آزمایشگاه‌های پیشرفته هوش مصنوعی انجام شده باشد و خودکار بودن کامل این عملیات را «شگفت‌انگیز» توصیف کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/451925" target="_blank">📅 18:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451924">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c667af1999.mp4?token=sL9T6P4yjv0Wkf_N2AdQVp4PLUCC_0dp_gEhXNGHEkmH1N8hosKQ8rbjLp_6rDRi0C00eyyx2MpoM_0BKaIOXfFZHFuFRbV_aP76KL1cxelPTLLcCCi4v5G4M9Q8Je5lgbfMvma0xndg_pWsK1jQthy-KHizVVkDFEdTNZM0df4awAXpJTvtS0DPxxAY30GBctjZ3fhQc5lFtQUgHrLl1CdesGO9pgxV5yMKgcbLwt0Fto5_7b2uiZA55TZTRGL_X1xy5n_3jkNAlYP9oFa5BJj2aqhE8KeXJH7aU_L_tlepOw3DK53ST87Dgv6DqTbIftVoTcaJforWsk1lMVVvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c667af1999.mp4?token=sL9T6P4yjv0Wkf_N2AdQVp4PLUCC_0dp_gEhXNGHEkmH1N8hosKQ8rbjLp_6rDRi0C00eyyx2MpoM_0BKaIOXfFZHFuFRbV_aP76KL1cxelPTLLcCCi4v5G4M9Q8Je5lgbfMvma0xndg_pWsK1jQthy-KHizVVkDFEdTNZM0df4awAXpJTvtS0DPxxAY30GBctjZ3fhQc5lFtQUgHrLl1CdesGO9pgxV5yMKgcbLwt0Fto5_7b2uiZA55TZTRGL_X1xy5n_3jkNAlYP9oFa5BJj2aqhE8KeXJH7aU_L_tlepOw3DK53ST87Dgv6DqTbIftVoTcaJforWsk1lMVVvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران اسلامی منطقۀ خلیج فارس را ایمن خواهد کرد
@Farasna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/451924" target="_blank">📅 18:35 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451923">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4c2e067db.mp4?token=O61dkBlSl1PuOwUQHNRsdrjzJsAkFtKIDPEsCcLBd60kwSfOp12YIaFhelgF138mkT1F0BjBIrtxV5zgLMBTAj5ApMggNb9qLJ2zYi11MCfCGRRy-tLR0Fhsgn51m3fqeen_C3eCqYRsxOVzvrsZCkb9Q10TQbF7HGOLQ_2kGOPMFyPPYEQNNE5KvfLJid6LHaQb9-BT_n2PkLa9bLSeFIUT0ZCdNe6wUfLrjQxCmjQxj_BPCej1hy7A2O1IEuADsf9x339fr7DRGLRKFwCcIKWCINT-ytOS3TYFNmW1RbIPEAF61aA6m5ikaJcOSNNCNk4MNWtPa_JM39tkEg3NKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4c2e067db.mp4?token=O61dkBlSl1PuOwUQHNRsdrjzJsAkFtKIDPEsCcLBd60kwSfOp12YIaFhelgF138mkT1F0BjBIrtxV5zgLMBTAj5ApMggNb9qLJ2zYi11MCfCGRRy-tLR0Fhsgn51m3fqeen_C3eCqYRsxOVzvrsZCkb9Q10TQbF7HGOLQ_2kGOPMFyPPYEQNNE5KvfLJid6LHaQb9-BT_n2PkLa9bLSeFIUT0ZCdNe6wUfLrjQxCmjQxj_BPCej1hy7A2O1IEuADsf9x339fr7DRGLRKFwCcIKWCINT-ytOS3TYFNmW1RbIPEAF61aA6m5ikaJcOSNNCNk4MNWtPa_JM39tkEg3NKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار‌هایی درباره جنگ و ازدواج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/451923" target="_blank">📅 18:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451922">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎥
روایت رهبر شهید انقلاب از دوران مبارزات امام حسن مجتبی(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451922" target="_blank">📅 18:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451921">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa912f51f.mp4?token=ZTRCa62qmUVr8PaeZ-JVrh7YJEgMWD4O7kBWtxJXz5Lh1DMeXEF2kE9URn0eLJ-efbDNk7MMCsv4kPsxD_it0B8d0-SZRhxD1Fw3LV7e_1kTzTSxhJuFkUexQug2LM_K2c1xbyHiv6iQKbSGtxYyx2BrRfncnFRbVhBoiizj867jHBPBhAZqDw3ijL_e899ra9HBNFHl71YtPiUNL91wNV96w98CCFqJIzr3_sDEwTB0YJBcwta31Jz6xb0VRlBBEz9273xlgSbAqoMvYWnXmwXMXysJqTJiJqfTquBtMtd8iAcML4rJCl8DDo8rwBnkXtmsPhaJ5ipqkFbKn0DLzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa912f51f.mp4?token=ZTRCa62qmUVr8PaeZ-JVrh7YJEgMWD4O7kBWtxJXz5Lh1DMeXEF2kE9URn0eLJ-efbDNk7MMCsv4kPsxD_it0B8d0-SZRhxD1Fw3LV7e_1kTzTSxhJuFkUexQug2LM_K2c1xbyHiv6iQKbSGtxYyx2BrRfncnFRbVhBoiizj867jHBPBhAZqDw3ijL_e899ra9HBNFHl71YtPiUNL91wNV96w98CCFqJIzr3_sDEwTB0YJBcwta31Jz6xb0VRlBBEz9273xlgSbAqoMvYWnXmwXMXysJqTJiJqfTquBtMtd8iAcML4rJCl8DDo8rwBnkXtmsPhaJ5ipqkFbKn0DLzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آمریکایی‌ها مخالف جنگ نیستند اما قیمت بالای بنزین را نمی‌خواهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451921" target="_blank">📅 18:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451920">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c390169b87.mp4?token=Bs976G1Fphr8lg6WSQYp5tdxqEc5bSBd9miTecrBS_PmQ0x4rWbV7oe-mJCVxBNDWdje6iZi6yOAjhGrJloSCHNWmAsLTj18HC_FBVM5cIsyLyoXJgNCSYaR1he1LrJduj6lKm1XWVBwwG6Rx_ob-HSQlY3iHROI9jUyO3DAb5q4AkH4AxQC9d0wRcVmrcwADS2L3JVNcMjjrqKA6pH4QmHSTIaCBLcSvgJvCAYqEdtOXPG067QiXaiYO_jR1kbHG60UR8TcltJyU-GTKLgJ1GpEzLAKaOLLHtw8D2qZArn0cNIZ3OG1WxFuDKdtFM6DGQKGIM3GFKiY1i2v64lgJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c390169b87.mp4?token=Bs976G1Fphr8lg6WSQYp5tdxqEc5bSBd9miTecrBS_PmQ0x4rWbV7oe-mJCVxBNDWdje6iZi6yOAjhGrJloSCHNWmAsLTj18HC_FBVM5cIsyLyoXJgNCSYaR1he1LrJduj6lKm1XWVBwwG6Rx_ob-HSQlY3iHROI9jUyO3DAb5q4AkH4AxQC9d0wRcVmrcwADS2L3JVNcMjjrqKA6pH4QmHSTIaCBLcSvgJvCAYqEdtOXPG067QiXaiYO_jR1kbHG60UR8TcltJyU-GTKLgJ1GpEzLAKaOLLHtw8D2qZArn0cNIZ3OG1WxFuDKdtFM6DGQKGIM3GFKiY1i2v64lgJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فاطمه امینی (مجری تلویزیون) از حملهٔ موشکی در پخش زنده برنامهٔ کودک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451920" target="_blank">📅 18:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جزئیات یک‌طرفه شدن جاده‌های شمال در روز جمعه
🔹
تردد از ابتدای آزادراه تهران-شمال به سمت چالوس از ساعت ۱۴ ممنوع بوده و از ساعت ۱۵ نیز مسیر پل زنگوله به سمت چالوس مسدود می‌شود.
🔹
از ساعت ۱۶ تا ۲۴ مسیر شمال به جنوب مرزن‌آباد به سمت تهران به‌صورت یک‌طرفه در می‌آید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451919" target="_blank">📅 18:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d6d6eef1.mp4?token=ppF7pxSDUvr5RtGIe1aX6CWbCevk4zvoBj7FJJh7tZW_haGPQ13Ur5_PWAc0jYhk6DPPsLjVleRybwzYAdH3MObrrgdjLRIJv_dM8ckJVemyf83RxHSlQ-m0P3yuKzD8BKYKNnWkyRYvkn9SRTShJojVRaK_AuHRRJklHApELNgbkk2hMaWWnLxWzmBK4ZcGU2qEfuhQUAluE07p3vxx1hUDbbdZ53ko1lCY_TLMnAlBE_MVfOCGHTL3ejUMjn8ZFOCRR8zchoSE51dWQocoPQYzwKPLqbxAgvbg7I1-ZwjgAGbEKfvLsT9p74EkKPaVxpRrqaLUWKSD95mGAM6CHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d6d6eef1.mp4?token=ppF7pxSDUvr5RtGIe1aX6CWbCevk4zvoBj7FJJh7tZW_haGPQ13Ur5_PWAc0jYhk6DPPsLjVleRybwzYAdH3MObrrgdjLRIJv_dM8ckJVemyf83RxHSlQ-m0P3yuKzD8BKYKNnWkyRYvkn9SRTShJojVRaK_AuHRRJklHApELNgbkk2hMaWWnLxWzmBK4ZcGU2qEfuhQUAluE07p3vxx1hUDbbdZ53ko1lCY_TLMnAlBE_MVfOCGHTL3ejUMjn8ZFOCRR8zchoSE51dWQocoPQYzwKPLqbxAgvbg7I1-ZwjgAGbEKfvLsT9p74EkKPaVxpRrqaLUWKSD95mGAM6CHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: آمریکایی‌ها مخالف جنگ نیستند اما قیمت بالای بنزین را نمی‌خواهند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451918" target="_blank">📅 17:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH7bTf60m_HvdY2bSZrKBBj5-c9fDRC-VVtzizTrHL1vi4szgmAE0OZCA0BrI6K5yEFOuuYMrxWreho2ZWmILLopReOhjUO-lKdPdh-hL4Zxn9ZBWEoCbqLMGXE9ER8Cv6lNKZWmEwCOA5x7s1hdKU6FVqBlOfFImrSFLVO79pVqoVWEov7wSGH0xtSqhk1wpzvueb1g_JrkZcLguqzlV0eYzjPvYFAeF_zXWMFk0tjTcCC8-UZ4Rw2r-ePB0NMNuGDXn4EMXpNBqmSU8-ndlU29YGP0e7FmcKu6Xc-otjVheYaoOAnlJaLWz0-CmfSm-LVxUVXBaB5-E1UqFpDFMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
انتشار ارزیابی رگولاتوری ارتباطات از مراسم تشییع رهبر شهید؛ تمرکز ایرانسل بر مسئولیت ارتباطی جواب داد
🔸
رگولاتوری ارتباطات با انتشار گزارشی، عملکرد شبکه ارتباطی کشور در مراسم تشییع پیکر مطهر رهبر شهید انقلاب اسلامی را تشریح کرد. بر اساس این گزارش، ایرانسل موفق شده است در محدوده مصلی و مسیرهای تشییع تهران، رکوردهای قابل توجهی را در زمینه سرعت دسترسی کاربران به اینترنت ثبت کند.
🔸
بر اساس این گزارش و ارزیابی‌های انجام شده، مشترکان ایرانسل در ۹۵.۱۳ درصد از مسیرهای این مراسم، سرعتی بیش از ۵ مگابیت بر ثانیه را تجربه کرده‌اند.
🔸
نتایج اندازه‌گیری‌های انجام‌شده توسط رگولاتوری در محدوده مصلای تهران، نشان می‌دهد متوسط سرعت نسل چهارم ایرانسل ۱۹.۳۸ مگابیت بر ثانیه و متوسط سرعت نسل پنجم ایرانسل ۱۶۱.۸۵ مگابیت بر ثانیه بوده است.
🔸
در مسیرهای تشییع تهران نیز متوسط سرعت نسل چهارم ایرانسل ۱۵.۲۴ مگابیت بر ثانیه و متوسط سرعت نسل پنجم ایرانسل ۱۷۱.۱۹ مگابیت بر ثانیه ثبت شده که بیانگر عملکرد مطلوب شبکه در شرایط پرترافیک است.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451917" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOeMoqyb_NhlddS7qmVY3kL7gWyh0RcHu27YqYOaDAOFcCf2bvSDe8mbiV1YtjuLAGfaUnU-JIGKwdQoHrP2w4Dqul7gaGpRNKcFBWNGc5MWJN6WEiFLSFyNuIJ_WR-mldXJa5BjKrNOyNfflp-Shx79A5T3fVrNcgr-bQbXgCYINgym1VGvS0TN2UTWR2Og7964MmJ4AmB94aiS3nGSVtSP58IMCe6jhIG0Gcz5SyWYyhb7anonSRUPNhffJ4b0sdbkqR8OdpcPQeYbqV1dFJcufG-Hdjj2J8IJ7OXPU8Leae6mS0gmAqom1WTdbo0sgJCHd-sgeprwSrpkVEIR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گام های اثربخش بانک رفاه کارگران در حمایت از نظام آموزش عالی
🔹️
بانک رفاه کارگران با هدف حمایت از فعالیت‌های آموزشی و پژوهشی دانشگاه شهید بهشتی با این دانشگاه تفاهم‌نامه همکاری امضاء کرد.
🔹️
این تفاهم‌نامه به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران و دکتر آقامیری رئیس دانشگاه رسید.
🔹️
دکتر للـه‌گانی هدف از امضای این تفاهم‌نامه را پشتیبانی از برنامه‌های توسعه‌ای این دانشگاه برشمرد و گفت: بانک رفاه کارگران به عنوان بزرگ‌ترین بانک اجتماعی کشور در سال‌های اخیر اقدامات قابل توجهی در راستای حمایت از نظام آموزش عالی کشور داشته و با استفاده از ابزارها و محصولات نوین بانکی، گام‌های اثربخشی در مسیر حمایت از دانشگاه‌ها و تامین مالی طرح‌های اجرایی آنها برداشته است.
🔹️
دکتر آقا میری رئیس دانشگاه شهید بهشتی نیز با قدردانی از حمایت‌های بانک رفاه کارگران از این دانشگاه گفت: امضای این تفاهم‌نامه نقطه‌عطفی در مسیر همکاری‌های مشترک این دانشگاه و بانک محسوب می‌شود و می‌تواند بستر توسعه خدمات آموزشی و پژوهشی دانشگاه را فراهم کند.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/451916" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451915">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451915" target="_blank">📅 17:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451914">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e557418c.mp4?token=kJBkkf7FrhStjf8rXiQ9INcP0CqSIx9q0rXhZni3iWD688Q4WVemP0UObIeZZkBZIUvXV2c4VAOqzoGrOegnLx8oVZnmaqc-tgInFxaD7lLkD5eCKMqkIo92zJT53EWC818uY1gSLQHIPefWcy17er8nBpH0IJ91c4xTwYsQzL0by6pUBB2AGxKcVcpD5njJmphWI-_zuwXW7M6TpVRaDmN5Mp4P56JOVs0D1K4RU8shu7KwwQZEC4B9aUSG6ag0o2DrOZqE0BpxRv7nwBQaXZvdKk22ATDCWBYPLGLE3GfxSJLjDF0mR2eMogsIJVVlNnKZ3OLT5gpa9z9U04rnTgEYOWmIEWWPpVkou5By6dSBJymte_NV577yVyGEH3RHgkMqffnP2f3bz5p3cGrVSnFIJCNwJj3KR-NkEAfmA8yBoCO9DT5mf3LYO9QnX6x4BI-IxbZ9G0MlMSBb3vvkB4dBj1jmk8nzOFzIS_dktNbJJwJJDE0Yd0eOtWsrmi-zdcZRuA6jOYu95iaNLuZ4F28EZKF9yi1xjZHEk62HvcB0v9zbTulAgZ-EVg-8JKrjr8aQjZ233tM3X3EvE2tNuEUnH6PbUXwbcwquvCMYu36F7HDjZ-V3P_f1wO28OHnLXjdSFgXptek_cmom-nxQC9VJSMqjXblZc8UVlW_t4no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e557418c.mp4?token=kJBkkf7FrhStjf8rXiQ9INcP0CqSIx9q0rXhZni3iWD688Q4WVemP0UObIeZZkBZIUvXV2c4VAOqzoGrOegnLx8oVZnmaqc-tgInFxaD7lLkD5eCKMqkIo92zJT53EWC818uY1gSLQHIPefWcy17er8nBpH0IJ91c4xTwYsQzL0by6pUBB2AGxKcVcpD5njJmphWI-_zuwXW7M6TpVRaDmN5Mp4P56JOVs0D1K4RU8shu7KwwQZEC4B9aUSG6ag0o2DrOZqE0BpxRv7nwBQaXZvdKk22ATDCWBYPLGLE3GfxSJLjDF0mR2eMogsIJVVlNnKZ3OLT5gpa9z9U04rnTgEYOWmIEWWPpVkou5By6dSBJymte_NV577yVyGEH3RHgkMqffnP2f3bz5p3cGrVSnFIJCNwJj3KR-NkEAfmA8yBoCO9DT5mf3LYO9QnX6x4BI-IxbZ9G0MlMSBb3vvkB4dBj1jmk8nzOFzIS_dktNbJJwJJDE0Yd0eOtWsrmi-zdcZRuA6jOYu95iaNLuZ4F28EZKF9yi1xjZHEk62HvcB0v9zbTulAgZ-EVg-8JKrjr8aQjZ233tM3X3EvE2tNuEUnH6PbUXwbcwquvCMYu36F7HDjZ-V3P_f1wO28OHnLXjdSFgXptek_cmom-nxQC9VJSMqjXblZc8UVlW_t4no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زودباوری رضا پهلوی باز هم کار دستش داد
🔹
رضا پهلوی در مصاحبه با رویترز، ارتباطش با نیروهای بسیج و سپاه که پیش از این بارها ادعا کرده بود با این نیروها در تماس است را انکار کرده و ادعاهای قبلی خود را پس گرفته است.
🔹
پهلوی در این بخش گفته: «مدتی بود که در شبکه‌های اجتماعی پیام‌های مستقیمی از افرادی دریافت می‌کردم که می‌گفتند من یک بسیجی هستم، اما در قلبم با شما هستم، من عضو سپاه پاسداران هستم، از این حکومت متنفرم، با آن‌ها نیستم و فقط دنبال فرصتی هستیم که از آن جدا شویم و از این قبیل حرف‌ها.
🔹
وقتی به رسانه‌ها گفتم که با چنین افرادی در ارتباط هستم، منظورم همین نوع ارتباط‌ها بود؛ نه اینکه واقعاً با فرماندهان سپاه صحبت کرده باشم، اصلاً چنین چیزی نبود».
🔹
گفتنی است که حدود ۷ سال پیش، رضا پهلوی در گفت‌وگویی با شبکه اینترنشنال، ادعا کرده بود که با نیروهای ارتش، سپاه و بسیج در ارتباط است؛ البته هر بار که رضا پهلوی چنین ادعاهایی کرده، بلافاصله مورد تمسخر کاربران ایرانی در شبکه‌های اجتماعی قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451914" target="_blank">📅 17:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451913">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17da88c1da.mp4?token=enPYZiza0HA6xrR7fFRlKzT4mrPoU5shmxbIMoeBwgMesEkp4ZSquBA3ldZafDsFyw9TZYEkh-oOGhNyAyGspowEVv2T1MgdQLBtOR5xhoxgobwDux9WLhseICkQm0DnRC4ezqysB0nmmWbbX0Uy62qI1Lm5P5gSjXBt5Wnsx6u7vFkoB92h1_SuOEAuex5mcrftYWcn9uyrW2CHdsL_nu_2CxTxmnVZKyTqmXxVfuA_2Ckh_-DWeUfnbuxzxyn_YkmdvyS4O1y9up0cokmDu4jqkf9exQLevDw0S5O_-hosMR6wEqUECH_CNyW1dC0sORFeqjFKEKpwi2VzIGXYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17da88c1da.mp4?token=enPYZiza0HA6xrR7fFRlKzT4mrPoU5shmxbIMoeBwgMesEkp4ZSquBA3ldZafDsFyw9TZYEkh-oOGhNyAyGspowEVv2T1MgdQLBtOR5xhoxgobwDux9WLhseICkQm0DnRC4ezqysB0nmmWbbX0Uy62qI1Lm5P5gSjXBt5Wnsx6u7vFkoB92h1_SuOEAuex5mcrftYWcn9uyrW2CHdsL_nu_2CxTxmnVZKyTqmXxVfuA_2Ckh_-DWeUfnbuxzxyn_YkmdvyS4O1y9up0cokmDu4jqkf9exQLevDw0S5O_-hosMR6wEqUECH_CNyW1dC0sORFeqjFKEKpwi2VzIGXYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت پردهٔ طرح جدید آمریکا
چیست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/451913" target="_blank">📅 17:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451912">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664d0747c0.mp4?token=rux5GTCl0o0e2CBA_99Oykgu12jA7NCGwRH_z51qZKEY4lj0CpMVFKFI7LzlBjk45nqLbvpmEtrNYZdDE_NP-_r4MNjfKikR0RKRANSzqXiX6OOUuOhbnzMurT-XF5p70VWgwDh0JfobP7cevXoe0hkv-dyMb6TykDAsCsXvgLUEfK8hTl2xQW2E0csi9nIX160GdCDzybT5JcCj7XnINOoaKClmA7Sir79khYkfZXzQxij-y2GdnRB4Ctn3UnTGmrGGY3kC0KcFfHlHS-MEX7JtC6wB9Zj79c_3Td75xN_MLWJ8qvNpGZeclsOblijuGr3eJrkIRie7ow8UUv3wVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664d0747c0.mp4?token=rux5GTCl0o0e2CBA_99Oykgu12jA7NCGwRH_z51qZKEY4lj0CpMVFKFI7LzlBjk45nqLbvpmEtrNYZdDE_NP-_r4MNjfKikR0RKRANSzqXiX6OOUuOhbnzMurT-XF5p70VWgwDh0JfobP7cevXoe0hkv-dyMb6TykDAsCsXvgLUEfK8hTl2xQW2E0csi9nIX160GdCDzybT5JcCj7XnINOoaKClmA7Sir79khYkfZXzQxij-y2GdnRB4Ctn3UnTGmrGGY3kC0KcFfHlHS-MEX7JtC6wB9Zj79c_3Td75xN_MLWJ8qvNpGZeclsOblijuGr3eJrkIRie7ow8UUv3wVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ به تهدیدهای ترامپ از نقطۀ صفر مرزی
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/451912" target="_blank">📅 17:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451911">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d83b8117.mp4?token=eonDX1coMT00JTEg64Q7MoClCcFU1UYn17TGXTZ3NLXd4CBICgunRYggtO3fbhfb89kp1z5NoDoTU3UdB6HnduPzGyWWrEj7pr8wLabRGkBBO-hgcWMc3BdBdHOETgnj0_9hY4xMGTz12OTQs4YvX84nKjYr_kVgG5ExRQpheEJayC48H0UcPlRX31ppROcErncy43zwY-g-9KIW-K214ChEXcrksD0eYtekSCCzgM86MbxltFk5SAUU8eIyS9DR-wCdFKxcIn7oPGqF5UqxCzbtiFiBvZ95svpJb7TrtZQZUfeYtnQj1ztu_kwyVv9JJpD__QUXjpimilgjTAwZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d83b8117.mp4?token=eonDX1coMT00JTEg64Q7MoClCcFU1UYn17TGXTZ3NLXd4CBICgunRYggtO3fbhfb89kp1z5NoDoTU3UdB6HnduPzGyWWrEj7pr8wLabRGkBBO-hgcWMc3BdBdHOETgnj0_9hY4xMGTz12OTQs4YvX84nKjYr_kVgG5ExRQpheEJayC48H0UcPlRX31ppROcErncy43zwY-g-9KIW-K214ChEXcrksD0eYtekSCCzgM86MbxltFk5SAUU8eIyS9DR-wCdFKxcIn7oPGqF5UqxCzbtiFiBvZ95svpJb7TrtZQZUfeYtnQj1ztu_kwyVv9JJpD__QUXjpimilgjTAwZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت ثریا از مقاومت مردم جنوب در مقابل حملات دشمن آمریکایی در بندر خمیر استان هرمزگان
‌
🔹
امروز ساعت ۱۷:۱۵، شبکه یک
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/451911" target="_blank">📅 17:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
حملهٔ سنگین سپاه به پایگاه‌های آمریکا در اردن
🔹
سپاه: ملت عظیم الشأن و به پاخاسته ایران اسلامی؛ حماسه حضور الهام بخش شما در خیابان می‌رود تا منشأ بیداری بزرگ ملت‌ها گردد و عرصه را بیشتر از همیشه بر مستکبران تنگ کند.
🔹
حملات تجاوزکارانه آمریکا در شب‌های…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/451910" target="_blank">📅 17:07 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
