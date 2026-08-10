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
<img src="https://cdn4.telesco.pe/file/CiK7Gc-tPOuPvr9f9wXu7-OS6Bv9I2QLoJPRJ3LQsTLpQOuc5SRuXmEwWBVdGwW_zycYyPHKBslVVx4ZXGyxzJeUMvII8Erb57epjneDOQKjPdwys8cScJRKz6o4pUlnMzq3CY7Vto3huWA_hY-k3Tr702dWeYU7fsipE6TGzh8WNWzByfVn9Xdya6oPPASNajNIOJMUuYYoHS658wrsoa3EX7l3X5w1-9FUHsndR63XKS2yZz9SzvIZPYCDkIWgA5ECKJqSdhSSDcnBsxiZO2ZFIZOh3xN80Ers9eithMh3unjM8w3ZTo06tYxl6MsUyQchCA7O2KuNRUC0Xi0L_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 18:58:47</div>
<hr>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss1_gpckE_ITcLgrB_c8RUtQDDnVYiNTXRnwtIKWghqgfpgBVk8S11qci68CLZn7BwUqpgt3Lkpql8TulK9YcH-9X2OKxMSyVB6Xj-1U-_pH8T-uwGECYsSNiRoms8Q8GpC06GbBiGVzSYZShBWIIiVl8KUh1NeT5yOqwNtkylbI-PGVhUNl7bawBHmREDVrCJaKFtDwQy8b1yPbQli4eSYiD7wsborq4o4I5LnuwWNNJfJ86ftydZ52cf8_DoiIroWEI2AwGp7jWAsA4qATWue-R4ThvevxmWyDbuivu80Jhkq15qA7bSLLFvJph1e-k2QcFYKgRPE8o22KDqUuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوماد‌های سابق و فعلی علم الهدی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/82047" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">زن ابراهیم رئیسی با احمد مروی, تولیت آستان قدس رضوی ازدواج کرد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/82046" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82045">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ویناک میگه دکی لندن نیست، ترکیه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/82045" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82044">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZss7mBW3j4FxWeOpYgucN_T70WJIs5YnHRtol57gmfExDu3N-oBDeui8aP3JdQclRfqdzy0rLdoiq2L9D3-1n5zGX8-l9eHEv-qW8pZc2546Et5CMSUTj-nZ-opXB4I93M6Fekbz99fHj50x7T6pF3QwS7KhIbmA9m2KmKESfi6Joz9rJ4mMQ5R8-f2zRLQfPZM1Yr3GUET9kruCBN4vKmqmP3Po3kGk25Bna3ktxGev6ti_nzJsZWMxGNH_1_f3EgSiO6JnQFQChIpG0-auW1nowtmGg-gOUfK7mBDWPpvjDOqEfD_RxrwHvh-iKZsYTzrW-4LYadI4OLqAXsKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو به روایت دریک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82044" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82043">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=DVy3AlqKUmvO9o5Qq8RT9n-6pqk82WNXbCkpbvP6fJkP7Ko3qSRPVMHFCZQfynJT54gSLqdgks2D0B7Xw8bO1he4zn1dvSs1CWB8NKusEDKycCl0mR66o4WKccxU_FMTKk1buRrQjs4mdadLqC8_NVtbiPPiKxeh0m-TUvovwpLJAL2vwPo5oJYh-kWfWNjTclakTPPHbskEvhp2a_lvb9_IcM-m5oXit1TguOlw7ndkzciDhLogSsYGzAhaHLv2MlLKs8FU-N5GpiuI5FpYnBMWf7rXLjb05XCCi9RiLFQMOLaNqyaLQ8xhdrQPbglWyewqsSlVkAwASoKU0Ze01g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=DVy3AlqKUmvO9o5Qq8RT9n-6pqk82WNXbCkpbvP6fJkP7Ko3qSRPVMHFCZQfynJT54gSLqdgks2D0B7Xw8bO1he4zn1dvSs1CWB8NKusEDKycCl0mR66o4WKccxU_FMTKk1buRrQjs4mdadLqC8_NVtbiPPiKxeh0m-TUvovwpLJAL2vwPo5oJYh-kWfWNjTclakTPPHbskEvhp2a_lvb9_IcM-m5oXit1TguOlw7ndkzciDhLogSsYGzAhaHLv2MlLKs8FU-N5GpiuI5FpYnBMWf7rXLjb05XCCi9RiLFQMOLaNqyaLQ8xhdrQPbglWyewqsSlVkAwASoKU0Ze01g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگتم بانو به روایت دریک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82043" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82042">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3v37DpYU-Cx-FXcPfAtNmxIIG4HlaP_lQ0YOoRhu6JJkuDJOKCWk76fb3iVDMIizG0jj6zisdGKZhP6rjr4e6dR32AF8_sLibaC3gPv6qdUtNlmQqDxzWJFU_9Hp9cDPUOFI2tmC_T_uIDlrEalxk-h3uVp-Nv9H2hO5HhfoAEvH1g81ddSTDRpq3OXoyF9R238Wkiv0QKUQeIMTje6D1tZHeg2oxyonX34o7OConpR9q9PjAYrDZ05SSjei_VOlSOrMq1CRKcQ_DTIK1DyXV2LLUmtZTA_RldWBrGifhinZazBc50HD-qqtAZzpbp67z5ZXDJArhNcPPj9YeWOEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۷  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82042" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82041">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فابریتزیو
رومانو و اهبر رومانو این روزا سرحالن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82041" target="_blank">📅 14:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82040">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urbhRsjOQY8zn4_mmsYgdYAwGsERg6bk2w6ZVhxeHdyk7hYlC5NE3PckKAgTmPFgvm_QN2AqGFcV-3GdFEx2s9au-3r-ljvYTx6PVdXsZseyK0UG_oPYA5i9N3YEXpCuf-yJzC241E_IuJ9Q5xlQoD2fuczjy8urcapIGZXGWAh8OKYtHuyC9KYyJicc40rXyIZ7rcmHE0B3NVDT70bPK0_YZ7TwyYGFqm_hApS0_9T0lcx1NvhZvgFD_cKCDYrFFJst6DHrlS9rDIJ_rkRmYraG1QTJccnk5xe1r6q5tNAOSnhP-6mpbNwSQ06DBEsNp35pp_E4wucHyPDf2r32rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی ترین رفتار پدر ایرانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82040" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82039">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPkpIdTNuB0W2g_D58hjoW9cKfMZRNhRnqVsisUKrSwqKPwbu78J6FDKJT47ib-nuJ7leRHtCz-4wjs9ErAyNcO2nwUfIX-c8znMxMy09z0lb48vVgMke_M-gtz3A60ylInJHGoIbWnD2PjgNqTT2sakIdWnEm1wTRuM_ovL8qy8BW9gW85eJ_ceyuaI9B8_Y9tDNSZmeK45T2bi5E738uHpMXVzNq25J0TVFxt6QkjNRFVb4bpOizzFElP4ntWdo38zcxEYflDla5HuA7r9s5sloEVWsm4tvhj_Ssbyzro2e4QpGDSenv81dnOZoblYV2jO1pyMjWjAMxOSKsNy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده خامنه ای در شعام، محسن رضایی: باید برای رفع تحریم ها بریم یه اکانت فیک از ترامپ بسازیم و توش بنویسیم تحریم های ایران برداشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/82039" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82038">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYxg6JJUxw9UwIDGUr62WZGiRVl32F0ZEDSDMAT2D7hT0xJdQAEKKFo-qBelAZMABMfrWGuNI27g1pgcCNo7uI4eqE8Wa98kROtfvTYYLVH3z5_vqNf8T6tPeNVRPLa-BpXMiwlpAitBwL0gqHRbOtOSchi1OivowZDLzcDd4l_UfdZOrKDCoijYWkA8neGodvPMFc24DW8lJzd2a6kM5tZOmoEJ6YWTXuCWgs1V5X3Txr4xbBVKwiVEwD9f0SfYrbPwnX7g9EMKL6MyaQzfQ51DkrNm3IuLZh5BJ-nl1WyCwP7ohrsi4m5L0aVWHf5mfW1g5anwvoxWvGVxRJL2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فداییو دیس کنید تقصیر اون کصکشه همش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82038" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82037">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8TGyqZazKvED57tXgTzbY-c1f5tJQ4J-dwJWcZNOW7hoo8_6CIh-ogK0z9mp_sEnsQ8Y6dkKZfGs5V9n2E4vvtPfveoIH5K761q9HI_9TYizZpvIE2gTZ1ZY6pORdpIaBNDCQd7VbN6Ca-kDjPBKpDWphDJufrTcXqvTVVh9CCpTVkKiak25l_Zn5epJhuTOh1bSlQ_mxv0bd_0gl7RkowzDo8TlFXFH6DbtnY2s4r2F2I5IjQVEyo5tVLCWkKXMqMfmuP6Y0jFO4sT-qqw-pAe2RJudlmdKZQO7VuLB46FiCAv3T5VEWiwhDDfIl7QePiKGZ5fUo-M-xiRcYUPWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ راجع به ارزش پول ایران
کپشن: ۵۱ سال بد رفتاری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82037" target="_blank">📅 12:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82036">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5lB8_cE2cmsDWbUnDisGD9ln1vYUlkGh7zNrv1WHhaoJBsorWn4PBLqVB7K8uBHDPOp1O8Cb652opF-bBfNzdkBP4cq8BhI8vcm5vcXjQ6TB-84-EhwZP6fiOfxocwLfc8kcZ2aWjs1ElVsZ8JWyl-DWa9sNi1pT1iyTvA-whVT-gCbG21RAqwTcOWOIxQ5RwQKNggcPmzMz7jd-GdbS_oEDzGEdZqvwFB2veS8oVVM06w__b-gzm3cX9el3oLt3mQAEa8knq62pzCIpz3XJBePJaG-9121exOUmhpPA1wZwLs6glQsqVy8k7K-6Msy5nuobUI04BDXOXZ4SMcoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به همین اسم که تو تصویر میبینید بزودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82036" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82035">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gO43es6N-eDGgobT9cYZgKXkFwseG2s1wEHzQHip3zH1yC4v47wznie0WT1bo7qbml3DVzSh_eDmQmND_BnEJVzp0rluGx7msf5fp024gY7Dl6HmEeVM_SG8UDbFKTwaw38cYN7Rbn3a2l7ejyp3ccdEleVHidFGt8o-d93Lbx54mZhlwZb3mhhrIumrqWm0E4AgGtbQAzScHZJvDu3KxO6EZk4kHUyrese9skZeGLfMLW_0cM0BCV5DPg5L3D8sMHXU3t3L_lK05tfL7b73keMy7lwiKxgebquMuPZ_0PrRNgKoK37UGEo9aOPnY5t1PWx-7NuUdjDIZtyu6zThAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r19
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/82035" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82034">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLnS7dGLldGPf1Jha2N4r8PSJkxTYxinGqwKElVsWwfns35Ay0n6imPbJj-raEZYASWa2C_yMPdmheaWxZT2q25i1yxJtJEmaBKjl8rB61Ua_ZsPPFITWN9r-yWjLg3uXAsH37JNG6L4mndH3iXznQnUwQSkiNnj50-IZtx6z7dXRTIUHNJPGU-ZnR3jk2M5KQYtZwielhoigGQd32UohmTZwObRuv311uN787CLJ1uNxt4eqI_vY2knNoNc1Wu1M0GJd123EeTRB0kyyvTLQCcocjRy2KlMC5UjMFWWIUTJ7L-SKvNWijJbYOGe2nsqmfGiamoj-w8SgD_BFz92bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپو میخواستن دوباره تو زمین گلفش ترور کنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82034" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از لحاظ روحی نیاز دارم قاف بیا بگه "قاف، مهدیار، ملتفت، تهران"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82033" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEUHpg5J_-7xE9JO5gWmUQQd2_9SnqJQWYS2Yk6jmVRvN0D_9m0ZzZcG2xA8FYuUcvEtX_lQ9d0guGgYNVZMZ5BfnhOhLnJ5abfhK2c0aMFZam2IHkdysgqJqOYLaOrc6MhPZw3XX8Qq1fLGpUdjBqtqBWTFbVVZee-leIOn8LVcLOIpdLnhfbLRWXqrSX-thK8DItDxC7f_JGEatzpkaBmkpYTi26xp9PbTHkeTEPNSAh2wChZ7YetFRbvc82wV9-9LH1qVf3_QQpQgacRqQFKK36nFmG3PG9E7XVd9P4mxyPrb5OwYfqqZWXFMB-T8NklkCz_b011LknxsWTAhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار برای سروش، خطر در کمین است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82032" target="_blank">📅 02:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hp5iZvW90EYRbXI43VFiozcAYmmwjAkAfoKJcXrcpD_OyUGpeOqe5eQ-_SnBi6_HTwkB_wvRMYmvCuzeczQFJevk_L0uqVLjJ-GKlsiZGxsgPk1ZLxMiNduUlV7-ch21CW8WNzZ2OU8BGZ7tkV2YFInA-_tWPGjyqkl5sm1NEZId8nU7zxgXyCxC0reGyNdBS95-mCmYifI95VmsLK9IgFWyD2bn30HFgIGym-2TA7jFPm_yhQxqzfljyGqHP0YLmh2WKqAUWcyBuNPce4GRpB4ZmwY6f5Idf2E415-Hl1WalwNrGA7ivUOXRu_gL01u7LOzx3PJhJF7L9KcGSP8QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی داداش آروم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82031" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">منابع امنیتی گزارش میدهند که ناموس سجاد شاهی ترور شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82030" target="_blank">📅 01:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">4 تا انفجار تو تنگه هرمز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82029" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سپاه زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82028" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWU-AUruaBXSztQObPcV69K0CvR3ymh5OOf3a9VMyy16iJIZUuSkJBZXPFZaHwMmSx3i_Bab74Y3Fye1DuVm9olfqNaF9mNAR0DE5rV7tstIzrKCTCZlCJY9p6Su2YWiVqpS0rc1pG2FY8lKqGRho-DisYyji6l1LhopySUWi_50pTr6vGrRqato6NiL1ipxLEUm9xwMmRqWa12D89nB9XC24LZbiH8XZNEYuKjcx9T3o4CJKq-ZuLh42QV1D32JwnrGNd_kSs_iiv6VK8SZVQtB978_EPpCQadcGpyJgSsbQGs3P-NZRQOidSy1nE4z42xZ9cm1MAnZxIQ_OczupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد عجیبه این عکس دکی و صدف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82027" target="_blank">📅 00:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ژنرال محسن رضایی رسما دبیر شورای عالی امنیت ملی شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82026" target="_blank">📅 23:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=QVSj0k6HkKeq-Pw1OEckGzwezvq5AHJYSbhHhFrWcrNzOoDLzPhz-90ehrxirQ4fS8azm7RpDiTUGSvq2msMyJ4Jbq3zTPwuqMCc4hQvboFXRG8_cy5SbfOLqo92eFkuZFj9DtkDNB23hrT4E1TgdCYavZc-8AO_iz1ozS65l1MvVb1Kb9bmmCcNdW4Pv4YD4N9TlIafjZi63q0lPOF9VapTqW8jroEQdsAKBiBpFSi51e7kblQnApefqi2AvF005Q78eZaUfAu3FyxoR5UnPEk2Yc1-hqO0G3K-ZGKnug55vlb7pUwLcbpFNuz3HbymjRsp4zhPujJbDaD7lKdhIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=QVSj0k6HkKeq-Pw1OEckGzwezvq5AHJYSbhHhFrWcrNzOoDLzPhz-90ehrxirQ4fS8azm7RpDiTUGSvq2msMyJ4Jbq3zTPwuqMCc4hQvboFXRG8_cy5SbfOLqo92eFkuZFj9DtkDNB23hrT4E1TgdCYavZc-8AO_iz1ozS65l1MvVb1Kb9bmmCcNdW4Pv4YD4N9TlIafjZi63q0lPOF9VapTqW8jroEQdsAKBiBpFSi51e7kblQnApefqi2AvF005Q78eZaUfAu3FyxoR5UnPEk2Yc1-hqO0G3K-ZGKnug55vlb7pUwLcbpFNuz3HbymjRsp4zhPujJbDaD7lKdhIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر قدیمی خلسه راجب شاهین نجفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82025" target="_blank">📅 23:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">۰۲۱کید تولدت مبارک ولی قبول داری شبیه شیپ استیلر تو خاندان اژدهایی؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82024" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=vwwYkNIGRtSboQjNVUfQ1n8OVw71HaVSQFZ5TpW7sc-XMHuNbk0AloOYZaUa4BbkqV9SswKMCIfMowm1p20GEzb5oDsZPOuqNUFykhzg4PG-UQK6x9ZmFvbDz1npJmiQM8QlKhoOdv4VOPutIuBMXHhjjj5okHOkJYJk-YJ6CwTRj_ipQhBpx4qSYbBl3zws9vxHz_QaUS_6AHKQpxBSeQP_daXrbOFeKAVpyFDgXUk3ZdWxR1HK035YsAQgBUTypXVdx-paqHBQcpIsQK4jMaqZGZJUCNvlRLn0xfJHUgqZsA-qv-jAT8xdkuibSEZYfy0jABHq7r9_mxvgLP14HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=vwwYkNIGRtSboQjNVUfQ1n8OVw71HaVSQFZ5TpW7sc-XMHuNbk0AloOYZaUa4BbkqV9SswKMCIfMowm1p20GEzb5oDsZPOuqNUFykhzg4PG-UQK6x9ZmFvbDz1npJmiQM8QlKhoOdv4VOPutIuBMXHhjjj5okHOkJYJk-YJ6CwTRj_ipQhBpx4qSYbBl3zws9vxHz_QaUS_6AHKQpxBSeQP_daXrbOFeKAVpyFDgXUk3ZdWxR1HK035YsAQgBUTypXVdx-paqHBQcpIsQK4jMaqZGZJUCNvlRLn0xfJHUgqZsA-qv-jAT8xdkuibSEZYfy0jABHq7r9_mxvgLP14HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای زدبازی، حصین، پوری و الباقی خایه‌مالا بعد از لیک شدن چت‌های مهدیار و فدایی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82023" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjVg-MiXsEx-bCS1WuLImRogx8uoDR2Bd0bfr6PuycrYyoUgJKtAkTJhWny6f6uJqb1owXhX2110chJSGgGaMRvYS0gwcH1zEfF6Ofgtx4VWZaD4ZmnBYbmu0w53Fa6lwFfpUuzexJna_rSjisnB9FvTJXZYRRLOTEBS_vIGxRUDfcBV1aFnLw08PTb8wtcvzLReckjvcAnMquDiHo0CR2HQm73kBGpMfeORJNUj4MASNcMhJh0cbzKNYyl-t2xnlD064hs8WlHsE8Mlfa25MzANMgfeABmLM-NkPlaYWDI_3vqJKQ3tAuSDdZWAB5RHyOKZWyTYYANCGRQjfVg8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی امتحان سلامت و بهداشت امسال سوال اومده که یه مادر چطوری ایدز (HIV) رو به فرزندش منتقل میکنه؟
یکی از دانش آموزا نوشته: سکس مادر با فرزندش از جلو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82022" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFjj45JymGUX216F3Yek1JfzICvSYAaLDuXt6Q-lzFb3Ugl-QflDBPfgV_VoZUYuFfmTnV6mkfvqvC773wYbdVruNkC-x-onmn8y8mkEKVNoM4Ac7tHk_K8Y_EBcQ3lWdwxogrZJNuTE-a_2Af2rX7vQ8fI7YJHbzLYuvsOJyWzSN5VQXSZLHMTE5l4V_DorLKijT-3skApb2rNfuFKYY222jOvpBVbEIcR-nseyR91iK60RBOT63uLnHJiuF7e39B1st9A0cuUH_k8J37Dz5R27Q83Yq738e2AWveHqLl9V20NyChaDMDFB12csPN1eFYlPQHHp4vNXsdH4NMR2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82021" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8XqW8oEFRLP2sK2bGKsvC-6IVNC9HvHIbpPpTXQ_AEr280bHsEwvPIpDO0HH8zlAt9UhK-CNPFikA4hcNueLZpZR4nrKhDJAxHJVpQIleREv7wDfbgkrP2Dbvj2ChXSrGnLlwHIfzHgEIxi7h8xs0zUxLaSwThsKLMK2trJys4kFeHdDHWhE80vkqTCw2Z3M_3qk9-FCGXbi9Hi9uPVZnEArndj5aSSkaxZw1QUkI-3fSZzESFW19zRXxr5DF9ne8ieAPFXvWeQ_BrqIVQf-pb-UIPd8FU0vbbKxPCL3KQKJwlACre3Bc6qsUZwOS2JDwfcxAvzL6aE1OTRrYOWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
g18
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82020" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82016">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HsMofORy62VADLcPOaT3CzaufPrfEFN1bvx4Eadi2LITJzcG_1pZNmNK4grXBqUo8naHqKWp0iJcYiKyG-fILxh0F3B80kNnfhy5F89DMylLljavDDr1Ema3t790Ypo3ze7O_KHLa0XCkLUAbP3R_SsTKF7jYr-hMVVszNa9wYerfiCDu3maKkywLE81qqSKlD6WmAL1V9OKcwupI_MmG4JaE3bgOAPpy8yUpWptIt_HrAEu3jXqiIEHXgj51_Kf8GnW-J-dWcRvcOmsvkj34ZtJqSAEY_T8FVd9gsEo3IIShncNGQZetSjU2yhEFD4lWZxO0s7IYO08asQok_hlGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kv5FiLI-Bq-fuWdd0JTT5hURKXnlmhgII2K9Vt494jBlz_DHQuENx8bLdhNszaEjqP353Vm7kTnxWLbryoT1guinRJKlUMn_9RI7brJvnPriZZjmJgkaFE2msrmcXhwMq-3KInk6RcKkSFWOYWkPkDX5MOyPS3bQrX_8VzkjIvv1BDrFLTy-hjj8BtpjRYCA9AY3IE1or8ZD8MSb3ze7Vxzjt63qItoraFLioVfS4rFFnmc64r34TO4DFX82NPJwHdk3cQ1JWAfe0RBWweucVged7ZQIcdFoZRs_y2MdBJ2DswOjByCuyS5i-3i51yQmUMJmcJHGuK_e2xdCD_Goaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHybclasVVnPQUmI2rGaVijLN0QAXYHZCzSsOPP5x8fgkX1GBJrKB3l51sa3hUZfgNJGmGYcAFyoJyYVWc5JOxbpOjyd14RnHuI8gpsO_56H1X9CCGkMMcTTq-prSJEnmBra-RleJnodYKOb7g3iFHtHkgxz11Qf_EbJpIVFikxo9wKic_Q1VMYpIJ3Xq2o2PSHwbQX15RgV1uvqsH0G2nRtNREOE7zEZCmfA_SAu0eETh30o-HD9cr6I2nj49F5UE5kCR7rTyzSE5HTCgH7y1cw7BxlmJn8ugHgpZLdHZz0uV29zVNQEhKisVsQCduh0N_3c65Aot1z0g8tPZTXvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=amCbvHkjD8AxyI0j3x4cNEWDrTVYOLYzStiystjoWrnSsNqT9a-jE0rgJRwAypT5VwFyditSHEveS22GQHK9vya1ucOvzelUdPEtvdgsayIMNtDSoC411M7Av8oH1CRs2q733NO5yA7b-jRx57yREtfnP8heEaRGHCoC0Pd1WJPip-Pkzxg932PalltoitJ-odJJ-slwWZY8fbEpgOfkFuP_UvwYcv1cF5AUp29EoKy6xtp8i2Pq0hBrnV7Mo8Nc56YM478etn0niqs-I4usBA_VJJZe04vU_Wwha-XH-8vd88A_-BEi7Qh645h-9G6myFm3WSvR9dnkFwkXoWurMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=amCbvHkjD8AxyI0j3x4cNEWDrTVYOLYzStiystjoWrnSsNqT9a-jE0rgJRwAypT5VwFyditSHEveS22GQHK9vya1ucOvzelUdPEtvdgsayIMNtDSoC411M7Av8oH1CRs2q733NO5yA7b-jRx57yREtfnP8heEaRGHCoC0Pd1WJPip-Pkzxg932PalltoitJ-odJJ-slwWZY8fbEpgOfkFuP_UvwYcv1cF5AUp29EoKy6xtp8i2Pq0hBrnV7Mo8Nc56YM478etn0niqs-I4usBA_VJJZe04vU_Wwha-XH-8vd88A_-BEi7Qh645h-9G6myFm3WSvR9dnkFwkXoWurMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیج اومده یه ادیت فیک زده که رونالدو بخاطر فوت بابای مسی عروسیشو عقب انداخته
حالا کامنتا ملت:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82016" target="_blank">📅 19:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82015">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82015" target="_blank">📅 17:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXDz8SylHzpgvxQVDyKVRza0M3ZsddpRaltegRL7ejf0i4sJUWUJdpaEjZjffaKUjnJTqJ_QZjM9pFRAHc0qvOqt-6vJxvc3mpCJJLs2HwqL49i2Our2ZeLqjrlf5yaYGAysqfD_QhjP2NiD3yoBFpn-jngk0DvB9YUbrHNiCbnZZUMw7xx-i08qR5c9WmPmH4WC8hJGA0IU7-SaEgc-4CjDsw8OlsmnPmL-rIFijKHOU-r6AZfkXuWu32koWpYJaCEsQhKYig2iC0nosZdUKsowdpzGjAkrp8zOQWqECaAE_g2noB7MmnoSUG9ptzQCuCPS1t5lk4ZM32MrBYHgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تیجی به نام لبه تیغ منتشر شد.
YouTube
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82014" target="_blank">📅 16:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82013">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82013" target="_blank">📅 15:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82012">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=vEPuvE7gYov5G8RMvdKA6M2fkRgqdbizGK00t5ASWprlyxz2eLTbqffMVCNr-B7bUNxb8j1B1i1aj4FJ4mPEXtaXPar45jLYXJMd1WaNFd0CH2O7UMwHvtB1utE-qUD8hpKnRLicjJ_afO_Da_nUI-12ga9L19tgEfE-IdVQ-BZHUrBojRR4SaDjBSexOsicWSyjP69blYijafh0qTXfL3YmSk6nwzBfHCN_NgpH-nhKSWH3ZmCNwEJcSctQAIUfuLoAD7QE5aDNTttyPl5NZoNcUd3vszWGPyKf-G_8CEkDMeNI3trB-BVbivKcR8yo5Gcg6Wa3szIXW8ZO-YyNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=vEPuvE7gYov5G8RMvdKA6M2fkRgqdbizGK00t5ASWprlyxz2eLTbqffMVCNr-B7bUNxb8j1B1i1aj4FJ4mPEXtaXPar45jLYXJMd1WaNFd0CH2O7UMwHvtB1utE-qUD8hpKnRLicjJ_afO_Da_nUI-12ga9L19tgEfE-IdVQ-BZHUrBojRR4SaDjBSexOsicWSyjP69blYijafh0qTXfL3YmSk6nwzBfHCN_NgpH-nhKSWH3ZmCNwEJcSctQAIUfuLoAD7QE5aDNTttyPl5NZoNcUd3vszWGPyKf-G_8CEkDMeNI3trB-BVbivKcR8yo5Gcg6Wa3szIXW8ZO-YyNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پهلوی و پوریا بشیری
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82012" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=l9VMwVX8uSVA3s8HHHTaVsQonlWW7bo4TIcC-t1UVSqJf7eeob5CGKey6XFyZZQMrJo-Z1BTN8uScjpy43JYwd8VXld79k6JILqaRJ9OSK6Z3jTVwkyLKl6c7AJsk_oooii0pGA6gnqP4u13yLvgbr6O4nFQ686u0ZIapI2GjlsbUdmmKJUQA264gVc5FAD3qmYk3XRmvlgQxCRXtBFmBfK4H7od2WcDoDiEAb1Cua9gL4iP1tV-iB9W0n7Siv5d38TfZ8vkHCa6qXnE0Ve5pJUIhDMVIVh16sV1A00CnhqYlymKzExXo-aEIK3SqqxvGD6aG3IfpWSl0BLdvR-1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=l9VMwVX8uSVA3s8HHHTaVsQonlWW7bo4TIcC-t1UVSqJf7eeob5CGKey6XFyZZQMrJo-Z1BTN8uScjpy43JYwd8VXld79k6JILqaRJ9OSK6Z3jTVwkyLKl6c7AJsk_oooii0pGA6gnqP4u13yLvgbr6O4nFQ686u0ZIapI2GjlsbUdmmKJUQA264gVc5FAD3qmYk3XRmvlgQxCRXtBFmBfK4H7od2WcDoDiEAb1Cua9gL4iP1tV-iB9W0n7Siv5d38TfZ8vkHCa6qXnE0Ve5pJUIhDMVIVh16sV1A00CnhqYlymKzExXo-aEIK3SqqxvGD6aG3IfpWSl0BLdvR-1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کشته‌شدن مداحِ سرکوبگر، حمیدرضا رجب‌زاده، این یارو با انتشار ویدیویی مردم رو تهدید کرده که اگه بازهم بیاید تو خیابون چنان تیکه‌تیکه‌تون میکنیم که پزشکی قانونی با کاردک جمعتون کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82011" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">جزئیات جدید از پرونده حمیدرضا رجب زاده:
به گفته رسانه ‌های داخلی؛ قلب حمیدرضا رجب زاده رو از بدنش درآوردن و مایع منی خودشون رو روی جسد این مداح ریختن و از تمام این لحظات فیلم گرفتند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82010" target="_blank">📅 14:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">محسن رضایی جای جلیلی رو تو شعام گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82009" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جواد لالیگایی(نکونام) به تراکتور هیرویگو
@FunHipHop
| TaymazROMANO</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82008" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvFAzqB4O4zzYZu6YG_QpfgXNtzVuamCy6EY1dNTvEFHnbBuCgWMSnbZtrEJyy6F4NNqEyCbB_hs1TleGmsiHXFwDC9Plck1NdwnNH-TrJ4-03_6bd4FwFKfDJpIDy0UFYLiY9QnBU03SwNDIvC1rYp_ncEK9fOImu288kbz6FN4zEwcd06GLDx2z53VCb7WB9BO8be2--I_IMPQue73ar5tbstIr0I0dJrDvmbfJhXrIYPFHmqXTRLW6JkpZllwCNQ7pd25CoY28NvYnca_Sg3DzqwEo34cE_NxDjvDt2No9AE9o6vmi4KUVNgVkui4d2nPfDHkhHmG7DQg6XP5sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس سالام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82007" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
وا
عراقچی: در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم، همش تبادل پیامه نه مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82006" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82005">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هنوز متتظرم تا انقلاب نشده آیسم نخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82005" target="_blank">📅 12:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82004">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX8AK5ooJ-8hSfhAytzMX1JuC2PW9L3TohdVDdUD7t2YSsDU-e-ZI0QS_eV_cYtkgOX8RhSg7rj5tHr4exFEPVkdzCup2VEHy2TxxSzXHsUVx1OgvZaLR40bEq6Qb3yMiEwTNUJMkaV_DNF29derU1gJvKs2ZeNLiyEAQehTgsQ8GDUkP16gCdFx_wD5U-nSW4wcYgx6LvvgGCJXJSUx9KYhzEUFXOqIAp7NNEIHA4RfGWZ47MnA2-WylvWgTmMlaiGGZG3lM4jg5POW_x8ioLJ-Xg4rSlymlsdN5Tx3cpyJeYXIwVMD6CBfsWBqPAFvMYtbXvh30pTmLvvE7KyrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس Calvin Klein صاحب برند معروف لباس زیر به همین نام، کنارشم دوست پسرشه
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82004" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82003">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIzNyuIfFalD8cQJrmc51xJ-BDxq5OVhKFL6mbIaXWUFqMjKE_dZ36u_tMi-MzICzNq7wQSydfIJ4ZdWPgHKQdt2I1BbrMWmQjlqlrylomN8pjNeqFGZitl1IqqqBtQS6zyfA0SVA7CaSCyQVZ19sXVaIwQfLJd8TrJZctQwrTNW3G6OAKlNufgC6pGKHEtFVjIHTy5ZYAyuCjRzoJaNW06fyZ86cPMt30KJVyxGPSnMpRnXgQlWemLmq3IduVqOflF_2T9ARQDUd0POMiKG-yAJk6gloEW_clj5sR1eRuHZ9gxvVuiIhACCxxSGvGGaO6XaEmdaibI3Hx7RrHMF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
betforward_bot@
کلیک کنید
betforward_bot@
🅰
r18
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82003" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=eBciivf5nCFZYAo1GipLnVMXiiJOPxZwC92G7bu7QyrtZDOcrN0Y459yZEPCWADP72LcegQ4S-5kddf9KF9d7491X5S4mP5lbCzpSLUwLlToo55VP6A6UvTeUCEARiXtSEkDOE_Z0kHll6mZDUkwL00fP-09aqFihafDod8CpPBWgKeJUlkcvG00f1NxyoZ1MgdH-p4a7frgK6zXxlID-yUU0sfNm8SgWr8YOyB2_FzOu1i53qT-AsZRt9uHg2_n-xEqbfkSLVs6yUP5B8Tsp1dGPFwD9aABYwyFIWfrOmCUPat6QvNO9AgUZHbQdaBVPG9F6exwBRO7LKJDvsfEkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=eBciivf5nCFZYAo1GipLnVMXiiJOPxZwC92G7bu7QyrtZDOcrN0Y459yZEPCWADP72LcegQ4S-5kddf9KF9d7491X5S4mP5lbCzpSLUwLlToo55VP6A6UvTeUCEARiXtSEkDOE_Z0kHll6mZDUkwL00fP-09aqFihafDod8CpPBWgKeJUlkcvG00f1NxyoZ1MgdH-p4a7frgK6zXxlID-yUU0sfNm8SgWr8YOyB2_FzOu1i53qT-AsZRt9uHg2_n-xEqbfkSLVs6yUP5B8Tsp1dGPFwD9aABYwyFIWfrOmCUPat6QvNO9AgUZHbQdaBVPG9F6exwBRO7LKJDvsfEkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد. عکس قهرمانان واقعی مردم همیشه بالاست؛ اما امثال هادی چوپان، جوری فراموش میشن که انگار هیچ‌وقت وجود نداشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82001" target="_blank">📅 10:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82000" target="_blank">📅 05:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81999" target="_blank">📅 05:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o7Lap1jezi7d6khnkj9bgMuNW9If5t31Ufb8twXCj6AUA69OtCn_I3bWWcqIFJ6f16_J5MponYIvUkKGW5u9UFjNi4STNBUOiskT3JuQFKZ6DxwLwjYStBDln5xNITwaqwC6mK8DMtQev-F2P_m7V3ZO6FQp40eTA-0xIChWTPLutIcvmnvO1KXd-kb1ciaKs04cBl7LKdoho9ItIjCbO58bpJVAumy_BqedsKL84pPaiYoAhr-W8RtLaG2fuUfaVEG441zM-5ljEof3HmoBgariWOYaJAWav4rMK4vWBkOXNR5wOtDcmorUTXmbZYCezRYzqMYgZMa9UFldrjMrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OfOvPbGbPge9DVdIGKINqHiURnMDDaUGab5QVmI6EQmhp46bkxE5aHVofoTtRhgaGW7vHWPO7ovJmfI20Drx7-6aObeEHVW92ina1tFRFjk9d5cxDq7yqDSYdx-32gb2aPSx-7z6qgep2l5LiMq6_dahfs28WIcUTCohrram_dTkZkBefO-LCbijGJ-4-Oao2v_DGRmoxLPHs89JnCut6kjyNUWYAP63bzXpkd_dDtA0nLjT9v8u_mA2QTF4fOO01yQ9U2SJPkhZhufQlvPf4KS-FHumcT7LwRKSOcnyX5VGdgL9NG83kdyKVdY5rKeJywGUbBL_V4h3aHUYgE5oKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بر طبل شادانه بکوبید
جواد محجوب ملی پوش سابق جودو ایران که قهرمانی آسیا رو در کارنامه خودش داره با رکورد بدون باخت 0-5 به سازمان UFC پیوست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81996" target="_blank">📅 02:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i68wXcOo-faCNtQGnGWcB20--020XakweX8dPwSwGPHz8b1RpzVwjBY_nmQWLSTFEBxEWjfO2MJJXxb1xC2I3cV50UPKmewDVP4idghBYiywNXvVclybm1e-gFectNwP7l70BuKGrCVWv-tPN1ZWvKew3VYR_tGKsi-R3yuGW-KqzgiRfVL2incYfIGpjBGYlmMbno0cNMX6KudTifergpiTMJDDajBO4EFXShZ_H4DjkUXPvPL450NDTWG3KZpLTNaEy7m4wJ-ZtHFcWcMeOkGRqD8U5Zvvf1IoIC8w0NLDtMqF_qqs9KuFo4wPzlQdTQ6QJ3l4yd4DTwp4v6oMag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کابوس و دیگرد به اسم انگ منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81994" target="_blank">📅 02:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81993">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KX7cxrsGMGJy5kkdDqNILm9G3aNvOL2Ax0I53mBnS_cpyy4Km7IMjS7s8n6uMcu094YYNAchwWazpLl2wMoOxDVETaub-TIW_g9Jn9eXus9Ipq2KuNvLUu0qsGvyu-eBhODgTzp0OI4Ld29d7qfylM3_OcmKaSaGEJkULlpaeKhK8RepA_IiMexEpr_oHE1D8hYJzuxpoqWA2YEh0EEtjizqZ9afAwPOFMinCWZ-vWbbIV590bHUY6doE6ccdtYr57kyOmYA8XiqikssC9CtZR0aqZaRTCXnh_lqMNclBjTKSZyA1ORHOORnsGv4O6cuvPSDzr9C0B-R1th5xBV9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اعضای سپاه پاسداران در شهر مهاباد با نام عمر دهقان در روستای «گاگش سفلی» از توابع این شهرستان کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81993" target="_blank">📅 00:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این کصکشی که چتارو پخش کرده چرا اسمشونو سیو نکرده مثل کصخلا تلاش نکنیم بفهمیم sha کیه z کیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81991" target="_blank">📅 23:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81990">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_VI40DsuDCbDV7Ryx4U4P_K1joDRlxZrtHq3wfsH_BzKugCfB2Jwpj7jPbzJJeIzKHGbvh1llGZGbYJhssx-JZ2WS_Wn_dQrmMa-pgag-Yqd8SQjW8xvUY_lIJb0QvqwWI0i1WSue3UuKX5-FryEPd3gJGSGfpDWiPySJeJNL1Q3Cngd23imAGDG4ZUK2vh_urv99Dc0Kg_8QT5juIy-ADZdSvm6pLMKIEtdvG6JMiNWddY7x85wrbCE6ANB0fBxTcVssq52YphdkRUGJiOo9zR3I461l3RFFPQuTGooTMW8sXqPGV1IJBHdFZrVQS7d8WfZvGpmIlLPQp2SQxNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که پیشنهادمو دادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81990" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81989">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-84ukcRBRvTDXNCNijdobo3c2kwc_hZouj95XG968uAIrRYfGCQJePzJJkC1s2FLFH258I4UyR6bYGO_o7f-PNH5y0ExGQYUIc859T0K1jsKreI1wfbatBLpkzNu-r5ETpbPHvEVtNtDC4f4mfBeKoMLAPyfvo9uVTx9NnULD2FVj_7JAu5a_6gU56qpRUj79LdzAFnBUp1OVh4PLfLf5Ic0dN49k60yLmPIHiS4Hj9n2ZsiFKHEiwagKm0ll2u9ZV1arPLQFCLWq_HZCClAE_YDLX9j-s5nztVhAWZLdZIZEbiw1DETApl2fwvgVG1ViS_oi6TkEoftPQnmaietQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 کا اومد به لطف بیف با بشری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81989" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81988">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کار به هیچی ندارم ولی تا تلگرام هست سگ میره سیگنال کصکشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81988" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81987">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه مردی برای مراسم ختم خامنه ای از آلمان اومد ایران ولی موقع برگشتن نذاشتن برگرده چون کارت پایان خدمت سربازی نداشت.
مجبور شد سند یه ملک رو وثیقه بزاره تا خارج شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81987" target="_blank">📅 23:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81986">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfukmZwhaTBXy60v7-A5hacXcfH9Lcj_QrOY49PaKzyjeY5fKAoMBJIVEyraRED3FeF-BwEemjnk8CPQnAJbQcWUOlKTFCz6gyDosP8wyuZotQ1zELBjJKPuchTPkw7kUj0e297i9zsvadysdkqxWh1KtFqd7ghp0u4Fl5rCzB38TbCHRFrBNrBtKkmCmQMfpjHmkRvpS4I675VDLMGRXTuBC8tYDUIoZwFsI7GHv0XKncsOIB0Q_JS5ssTohDYEhQEZd3xRxNqK5kY7PkJ0qJn9fAAk1r3Uj3uBLAeib0SHV54SkBYhVJg154qAay5tRv8REkSBzDLldNZUygsxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/81986" target="_blank">📅 22:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81985">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbdkSgl5CPIl0aBQFnno3ArblhJypADtq3l2gGThVO2v79oc1-2QvD948-4c6EO-X0-VapZ-ftPKDg6rVQN_R_V9a5Ku7KmYzjtQu8s_qF8zEr1LVxcfyViQ0UoGFllgeIdHFeMACC7gD6LsfnEEwHsFSaFs-rlpnzVLK-t8hI9KuGzHJ78QBS9qzxEIbfcLSw2YAGZ8MX5J5ZmAnEfadpXvwAuxSGlHatwsSrnC6zCi44AUGchcNqTMRnsjEM265cVjd8-t5hkfDty2maiZuxOhn31vlEnbD8AZRdlr3yt16gD9YH3r_Xv7032FOMZ_3Ukhz9ePZ9HWhmylLfe6fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81985" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81984">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پوری تو ترک جدیدش یجا به مهدیار میگه رضا پهلوی رو انفالو کن صف تو با ما فرق داره
ما؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81984" target="_blank">📅 21:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81983">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این جمله که "فدایی موزیک داد جوون مردم و فرستاد زیر گلوله" همون اندازه کصشره که جمله "پهلوی فراخوان داد مردم رفتن بیرون مردن" کصشره، فدایی نبود مردم قرار بود بشینن تو خونه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81983" target="_blank">📅 21:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81982">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قدیم اینجا میگفتی کص ننه فدایی
خشتک رو می‌کشیدن سرت
الان چی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81982" target="_blank">📅 21:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81981">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbV-K1ZGzM1PkeziO8eOQCM0JcdVbd9ZdkKvBlHe0avBPJwleZBsSH8BcU3ebGdIw-cQk9XCqnSIYNVRkAscKNQJBNcZBC7fAPD1ThRLyh_OQGB9AWNmzf8f20Wft1qgWeGoL1C3kQ-PjxAcekzVISX8tQNWVCYX31s8bihUhu81QyG6fjcIpR5swXy-QC7TDLuKBj4waE-AXSHAgFIMECnZ7fIlb3cDbw38aiZVDOle8FqsfyMg4GzZmVcLkRIoQq8hsDyHCTZGW2d1PkOmodDoLYHB9peFR3v_wNHJEsK2nW0aymxtokZEIuuTufw6TgmD5s_rGgWO_QlKS9cyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی میگفتم کاگان چرا نظر نمیده، که اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81981" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81980">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اتاق اصناف کاشان اعلام کرد:
کاشت ناخن در کاشان ممنوع شد!
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81980" target="_blank">📅 21:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81979">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جذاب مثل بیف آرتا و پوتک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81979" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81977">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تنها سیاسی خونی که باقی مونده ویناکه فک کنم با این اوصاف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81977" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81976">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">من خودم تستش کردم
راضی بودم
👍
گفتم شاید به درد شما هم بخوره</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81976" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81973">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMnbpK1B2pzxXAPIFQ6yJ5Cc4FNy8Gzo8ddDqddMJdnhcoz32v_aN-iO3SUUymZJvPXLZvwixSiiPsfJcsNLXXBNIj_wERSBNMeaNkqfww2ma8miUl116-mKJAwos9Ql7lkEyf293ivXoxsqFcFa2ichg_EUKsi-6Bv5SRCTjklQSYVUax3BWgd8L8LYMBcH56LzZME2koin1asJXyAvZLXsexH9O9AmbzLXuVt8D7ixsOG1QPg74Cc_DQm8c1LdVMVYJEceT1s-dNMF14pv9NFXo01ra6wK7bTWPGiCghk8ekkz7q7-VSB4pYGKjvV2ZzwDxtKjAMqZs6503XSaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتشه بری دایرکتش آیدی دکی رو بدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81973" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81972">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhhZPRLjUsB9yAV-ZHwzZ4x4W_gs5uT00ZabjyRQbQL5XSNw2GkjvAjT-alRDtV3_xzFsjI1JSgMcecEpFc1iMHAR6UuoZEkf6IS5AQFzNC3xoowcnHGxxTS-f2nhulg4g03YImTB0FxyEj7BONKoLgbdIAOfITDUBq2cg8J8HxMqHGzvONI2taj91wpgSeXQ_gHz49K2ZHmSnnemDFHwCsAD-IBJvr2cmhMlDZm6a61SJ5_VM213wb5Yvx9ZV6zTQx84y8vWzLoV7881QsLB1Dza7J4h40FZ8m3NzAnBr1GC-YLacAdUeDeDlDeOkriPvTnURr7IqVsT6CG7P_spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پوری گفت جاوید شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81972" target="_blank">📅 19:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81971">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH4i3o-mQ-t0k9B6MrIQUz3ulPrtmXnxFrJdOjG-OJyMrWOQ-xVsvkXZ2qmd5tOba23Kg27bO-v85z9JekBIf0p6Scp3muMZoN2r3a9Q2i52Vv7AoDJfH82CeQlbn_f3nW5sKuTwYkUHB4A3-RPnPFgHlz-lrVedN_COpKOcZElE-7wGWdkLe4VnabGI4K4TUXcJaIf4MXWjZHoZIR-4d9KyKlBh1r5MU56pQGU5yPtzJy8v4RPWQL85S6rJ975_jw4Ri2VJi2zuc-O361C0nAeYhfVgXn-yuaCunHldvaKpF7uWPBtZ0yF-V7443FwQaTIHvMpeQlfPDyg6nm331A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس بک قاف به پوری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81971" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81969">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyeZx5-Qzcut44ZyqqVYspUG7TAAe8QrJ3s3l-shnDJW4gmBTA5AdeE_F0pPbyz2zVV3O5X3VnzZBgMWlDMtc2EKSt5XyXVB0SgOocILj4QacW_1Q5Z_4EEpzKa_11JeNFbjhoB4EZNl-vJBZZ0RAUow9UddH3v9VFH-YV3Xiu2G67gU628Hza_8rVx76hZKmSnLUKSbbtUeeuKrXXInWCzwjvQxA8S60WSEEFomoBVdUaxBV0OH-p8ftTPga38xs1zdDbzEDYBBynZXotsgmzqLu0otqgAWv-0zHvVy1tZo0Zf0bsgeDCJyglapg-rUeHVcKRRzaTnURCm5VicXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییتا اون یارو که چتای ملتفت رو پخش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81969" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81968">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMY0wwbkA6e4oK_smcrVcmXjrj7nPZfElGwe8ajDvHFzmFmlNxNNVTWQfzCK7olzKbeHTG20zc7hEztrcRhjgp_vjdoioD0yjLdE4IRltrs4fb7SQ07mjSUmyYYX3X67INeprG28nd9rifaJU60oGxZq5qqNVlwZIhdWnJfX-s7CXcomHR20V79BJlIeNiq8CnCs_b1hYzbBYuRIiJaxwWk2wG1aFsAfK01HjdEBTuEy8iLD8BO0ECHGG_a0WBAimwBd8SBfAYsVUPUTNiJFBVHe9spgk7JgfSkUyx9FPWvJw8us7iyqMsT-zDZIawrxJo6zODkSM8yShqGxlT_Cqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع کار بدجور خرابه.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81968" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81967">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خدا لعنتت کنه پوری ریدی تو کریر فدایی</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81967" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81965">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">برگردیم سر پستای غیر رپیمون بابا، رپفارس اونقدرا هم جذاب نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81965" target="_blank">📅 18:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81964">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA²</strong></div>
<div class="tg-text">فدایی 72 ساعت وقت داره بیاد تکذیب کنه
وگرنه دیگه مورد تایید من نیست!!!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81964" target="_blank">📅 18:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81963">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بعد یجوری از فحشاشون به پهلوی پشماتون ریخته انگار اینارو دوساله میشناسید، همیشه پابلیک اینارو گفتن دیگه، پارسالم برا اون اتحاده اومدن ازش حمایت کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81963" target="_blank">📅 18:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81962">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چتا هم احتمال زیاد واقعیه، ادبیاتشون خیلی شبیه فداییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81962" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81961">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">من کاری به هیچی ندارم، تو این سالها هم یاد گرفتم به هیچکس اعتماد نکنم تو این فضا چه فدایی باشه چه کس دیگه
ولی سوالم اینه، اگه فدایی کرج تا لنگرود رو نمیخوند اسم پژمان قلی‌پور انقدر ماندگار میشد که الان داداشش انقد معروف باشه که بیاد برینه به خود فدایی و همه ببینن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81961" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81960">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">من متوجه نمیشم، مادرجنده بودن فدایی باعث میشه که پوری مادرجنده نباشه؟ چه اصراریه داره برا ثابت کردن این.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81960" target="_blank">📅 17:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81959">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81959" target="_blank">📅 17:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81958">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خوبیش اینه کم کم دارن فدایی رو عصبی میکنن و بالاخره میاد تو بازی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81958" target="_blank">📅 17:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81957">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromㅤАмин.⚘️*</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2jnLHzcGN0G69riYXg6aWPBMff7CI3JZyGp2gcQLaj_qA2IupWki5ErM-Eog5yOUaO27uWIpwl9SynAzMDwu42ylhFZqcCb30U35dfvAxpSrcrTqbR3KdXGTN52pGzRHgks4M0woNoCsIUaBKsxxH7PQsWg_aTZvXmSyeRez0x98qFn0YEbJBU5Tga636GcOt-1MXjUVAmm_mFhfhfIuE6ZP5foZNBlIRqTjkNl2ENBmnLEXLVmFAUdp5mB-Z_QGUHmRZSJoZv0kIephSE8HzAODQlbZFViLc48T6HZ0A-enjcZgs_Nl1L0eQC_VpKTqEA2sfeTXV0LkL5uHXhkew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81957" target="_blank">📅 17:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81956">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81956" target="_blank">📅 17:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81955">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81955" target="_blank">📅 17:09 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81954">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81954" target="_blank">📅 17:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81953">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaTPkIjY-9-r0aE5Y9nV_-qso160V8aSrzT0N4CWdIy-S-NbhkJejsw__SFWjQqij-U-Jhc7CAcRYOKthMiuzyz4ijfMSB8He_CRZblF4SwTGhfh2XCcvUIIWX_XQJeSdqLdWVPFseFg8GXJP9NVz5lSwqB2qWIAsQL9tOpY5GWa_Av-iYS2UT1LQ-HoXAH6IyZr7oJ6pJj5DbsoL9rKH-fdaWf8nCbY0DXbgqltf6MTekVUMzoKtrCsLZ6xTpuCgmMEly4I9_Igz3u8ZP5BPVY8ga57Fyp3eobGYvetWJABvvH5zFBRRpZSCG_euGiRoxL6PmDdCibFn1uSf6CBTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد
YouTube
Aparat
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81953" target="_blank">📅 17:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81952">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">توروخدا به ملتفت دیس بده یکم بخندیم  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81952" target="_blank">📅 16:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81951">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مگه اپلود تو اپارات نیم بها نبود چرا طول کشید انقد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81951" target="_blank">📅 16:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81950">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81950" target="_blank">📅 15:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81949">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dL34Jrp7-AOhy0gfVQTZdbZr7Nl8OsFBE9zb9yhAf5tWP2yBUeRNFAE00Jn9tt-Ur3P9VQJj968EnfF7vcC2Br4dJhRPnWbdRyK08FxGzpM1Z7LIIaOlcZSiHHnWgFeRYCO6A1bFtqoq-S2I7taoti3BmdpXwpwYI2Q_mOsUrCDLgspjIhZG40hvxLnPW1DHkcJha9RwRYta6evqEx0ErpnIInByIZQA6JoipN9T1eAiaatIpb3jQi9Mvzjn1K5dLfyYzyx_s1jWLpTJ-JqckZTEd-PK2ce2qMCamDDKOc4wxu2etl-BXnZ4EO3gmn0HHVgeB2F_on78bvYhon4H_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
لینک حمایت از ارتیست
هست چرا یوتوب
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81949" target="_blank">📅 15:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81948">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81948" target="_blank">📅 15:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81947">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پریود شدی کسکش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81947" target="_blank">📅 15:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81946">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmaXkYrRUMyLXsN9B4RYTbtRN7qOEmvEGGsMayzSoTmOChdUtoN_4FSTRwuCcspgfKhxx2NujF0PUKUaXM6Qkk7OiJSZB5T_2UZdjfDuBOWl-b3vnVzs7z0FlvcqTZH2epOPJ_oqjJ3c5afcbDb9OWm-weqdfxIemXv4RP_wfW30MSNiIez56TskgsKj5Fi2GGE13mSRhLQCpTWk9O0rZGSFJ_i6-xd4GAixtF36S2BJLMiuBHK7ETlrCkQzk97UvDPwTBgWQc4aR3cPyhl6hP8apl90UW1Acw2C7Ez2Rxnf4XTocJGntPUHOf7kqZU-4xu7kw_rifESfr3yLMvzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریود شدی کسکش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81946" target="_blank">📅 15:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81945">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHCYvWDXbDjjJe7QwNVNJezeU7X-rkS-syFQVu09FgGeKmFTuj_Ip7fYjGxOtt8FFdg-iEHsCkgyzckLrNGWlCoCPfgPTciodI75MJ1K__2aE4xytexag8JT08wMxOVC6IEigaGKnaWQgzWJr94fv8Z6A5TCe3TVGnI0viIIWWje1G9by_je64ywV11I-xvQIdh9fDepPAToGn1F2T7GpCW_Y-99vGvop6jn7GXlU-qAo8VfoeeycW0_O9_c8yvLQCGIFDX_4Q0VusOh7HLXs0u0obcdnKhwE2wIs6i9E8oMoNLMKvrlHcsHxQBHI63tYMubd4wOLkjPkx1Er9I_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81945" target="_blank">📅 14:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81944">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبر اومده بابای مسی فوت کرده ولی هر چی چک کردم خبر مرگ مولرو جایی ندیدم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81944" target="_blank">📅 14:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81943">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صبر
صبر یعنی واکنش در بهترین فرصت
نه در اولین فرصت
پوری دوباره اینو گذاشته چنلش
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
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81943" target="_blank">📅 14:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81942">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=tBL4bHcD987y-Xgd2bqMQHwC7aWV0XHsyzVfV6DcvZhHBr7McC5M6lApMRUPk5lObQNL66CZKUSmEVvWTNMSX2QQb_RMXdSicnAL9G-g9MDFMOmsva00mioYkdgy0UedhVc0S96CZJHzCG6giiMHnLdMomSuVL42qXMRb-XUNZBmm3BJbftZnCKHlAjEEBhIokskn_egb42VPfQLwSRPhmMdcvaQS9obDuDcM2Np7m9uFbbyowftPA0q6M3LEcRu9WlHUOx4RnZelpYb3dfkgoO7LwrqT6IfavF1WwY5MKrmSA5orRvVrHLvHB-SYudMISmlBRuqoj066AwPDkmPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edcae0795c.mp4?token=tBL4bHcD987y-Xgd2bqMQHwC7aWV0XHsyzVfV6DcvZhHBr7McC5M6lApMRUPk5lObQNL66CZKUSmEVvWTNMSX2QQb_RMXdSicnAL9G-g9MDFMOmsva00mioYkdgy0UedhVc0S96CZJHzCG6giiMHnLdMomSuVL42qXMRb-XUNZBmm3BJbftZnCKHlAjEEBhIokskn_egb42VPfQLwSRPhmMdcvaQS9obDuDcM2Np7m9uFbbyowftPA0q6M3LEcRu9WlHUOx4RnZelpYb3dfkgoO7LwrqT6IfavF1WwY5MKrmSA5orRvVrHLvHB-SYudMISmlBRuqoj066AwPDkmPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هههههخخخخخقخخبخی۷خخخخخخیهیهییهیخخخخخ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81942" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81941">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zau_oR3XlF65t83HgH-5AD_Be5DO9DYYlnNO6kCzFjRqGh2wjZfKNOCF37hI4UrsNgKt2qX9AqxibFRMOiXp6X1Sr5JcU96p0SZcc-537Bd5vzv_MpkasIXBi69yRr-6vsN-dxYRspuhGTbodVOUjARvaUZ3I_o_Kbr9iLW-gdV-JS3ec6bs9kWGFf8KAtLNfjuyirHKJE5dBRXR_UmzHV-18Uqn43tpr5rd_hhrdjEdNnlGfNCnjo-QlJctygY6CZcu6-LPDOPB85aJZ1xTusMrXT42WG7TLBXESDcqMuwet4W83_CXZ4bUTD5Ik7jxabI-fwtx91Dv6vlrQKs9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81941" target="_blank">📅 12:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81940">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMtmhh06bmJ5NiDfSbLzXyZLmB1CJ8M82Hewq6MeN6aPmmP2VIKz2_v11kikdhRrSOzT80tDs3mgKN2Zm5JCZh_GlbRHZkLFQ7Nb5majiJEDKQd4g1wL9YpOE7-uifCbpkWo5WLlONuTZ3zLDAX2YyQz3Ww5SWyTR_rYTgFdGdBoQQfbhOoPiH-8spg81P3Hzs7s54qalWFy_K93A0-QL8VbtexExJwukycSHJU6KUiEP9hMYsBBFvskbtBN6qL9b3UtvzOnc_9B0KBRUBfK7Nfvvh3_qBsUKhUG_LbU33yvzzb6pSCjoBUA5V3Q-d4vpZzqWwOF7mRkaTxSuhAa9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ah shit, here we go again  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81940" target="_blank">📅 12:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81939">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Co5u-bQC4dVfAZ06r_6bJHFso38bcpkNBf-WXVsncH4xXfHx0VFQVxpYqtGjdfOywCsB26D9MY6ydQa-gtN0_8Ky6hEZ_YffCVlQm_8WJRQ_2Y7L1WDaF89lF3onAS_9E8S5RnhVnKV3S4JqJO4d9bIK6dMMSWL_-jAC5vO22pitHBscZodGxiXxuMSaGSGcdVTvhGS59Mv4CJr222XlFHx2QO4sODkAYRIzVVrxN-AhccFhEazgduO8osbPL12rumYG6sZt2hmjqaZ5gWetqJdxdzqnTqjeQ517FQe4kUmxAwqCEd1lzPxGn6xkSIV2GI-qnXiR3d9doi56uewvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی قوه قضائیه: همه اموال منقول و غیرمنقول ساعدی‌نیا مصادره می‌شود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81939" target="_blank">📅 11:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81937">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-UsoPWJrVNfzYBNT0gMn1ey2wOhY--jm94OmLoqvH2OOK7oYnwyIYQhH_2EoNxCW06p5JjhRT-TvDcAlQ1Xn_yBkQZUT5p7tdKwCCC5wO-ntDkGeXE4wn41f5ZfxVsDuipXSOiqmrlyugxGU2u-lWmzlpA-pz8RSNhzpAkW6-hUb_Jq2ulD2ienk-756KJ4zFGOrBeSq-SOHLdN9HwZVxjkBgjIgw_QSESgd3PukYKV_VxdVZa2xm24pqaC9RO7UlS502idlCJTs4oFTxo1jPxRmk4UIL2KX56MgOQyjyqHfze1yZC9v5094obV6G1NevUTR-CFfWF5dwSUYk6P9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک لیست و فیتای آلبوم خلسه که به زودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81937" target="_blank">📅 11:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81936">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZPI7aa3KLPBBEa_oG2sW5kU5uuhRso8dwUUyMYeMnodzTB6ojB-kpNNMYEr9YFA85UddrODd48WnzRMb4ireTX3FfA4Fr9xChUwgNr1aQjZg5XSYJqvN-pDmKi713MJHTOC2YVBJdOG__fhw93FRVmQ6T5-PCOWQfo5MKPOKct1OeoorfORlX7xvN7RK_frG9oQ3F0OYGEjFumQfvN0uj_qa2ay70tzP9Bb-kzI-jJSF-F2kYAAeTpoTjo9n30j2wnrrNdLdS_lkG-7AupuBV--L5mDvAQ5wC5fNhYxZkdbKCf_6jQFMNYmjFvKW4GMrj01tBHHLQJjoHjuQjNemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها حالتی که ممکنه پرز لحظه اخر رودری رو با ۱۵۰ میلیون یورو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81936" target="_blank">📅 10:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81934">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حمیدرضا رجب زاده، مداح حکومتی توسط گروهی از افراد ناشناس کشته شده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/funhiphop/81934" target="_blank">📅 01:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81932">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حاجی بارسا چرا این فصل اینطوری شده تو یروز بازیکن میخره تو یروز میده میره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/81932" target="_blank">📅 01:00 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
