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
<img src="https://cdn4.telesco.pe/file/IK3PEpKuPD_xoIrT5MgbNFxjDQxU7HwvbnzhUJRqqlNJgZJaEHUox6T5MO1-s3WMeVc3PQ_9yIV1Vk-DJNORsodssZt_WlnaTg8wsKq0slQHrVAClAh5RKV3DKLzIqccbGdMTLsQSg3eQO5YdqKEORJ0mqaADJ8PvB0ROAKNYJ1TNL45N-h_zny7_mupqOCWr682jSEkx90Z2LVjHejUPHPLjkUEa7Gmbz4v6qz1PxjCc7DnCvP--oGVEQ4rEEqIr0pItaIh_OG1LdEFbzJMdPjpHcn22xsP6ryVxSnUa-7-EkJzKmKAFjI7vix2uHDs1Mn31m0t8lfimf99Fyep_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 18:20:19</div>
<hr>

<div class="tg-post" id="msg-82086">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=JLUGIKVSo3ibY0_yINOplG24mOTuZGdJAXY4qqyuwkbjzKW34_CBQIaoIc4wkC2XNJOmHfg2EdPQJkFwbGGA6obwxFsDrkseqNnJgEpwSAzGPmMDt3q2djN4bRzmqUG6aiuZAOcvz8Vj3XMcG3-KEvijwdLgSu0uSo2nR1POcW6wjkebcla5gOFW6i7gU4_QP9-3g0GTgUbHWV_s0hV1Pd3-fzlNXJbse8m3uEdi22H52a5XLWKz2m4kei8W06Y-2HOO4dqCEHHQI4j6zyJpth_YiJJ5iM7KdpyTU-Z-m-xWpUOyzbxXPCXvX8LlzLdTD5ocU9LIF2foL9dlbAhdew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc87bc1a00.mp4?token=JLUGIKVSo3ibY0_yINOplG24mOTuZGdJAXY4qqyuwkbjzKW34_CBQIaoIc4wkC2XNJOmHfg2EdPQJkFwbGGA6obwxFsDrkseqNnJgEpwSAzGPmMDt3q2djN4bRzmqUG6aiuZAOcvz8Vj3XMcG3-KEvijwdLgSu0uSo2nR1POcW6wjkebcla5gOFW6i7gU4_QP9-3g0GTgUbHWV_s0hV1Pd3-fzlNXJbse8m3uEdi22H52a5XLWKz2m4kei8W06Y-2HOO4dqCEHHQI4j6zyJpth_YiJJ5iM7KdpyTU-Z-m-xWpUOyzbxXPCXvX8LlzLdTD5ocU9LIF2foL9dlbAhdew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضاییان: طارمی بخاطر تیم جلو مصر پنالتی رو گل نکرد که زیر فشار نریم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/82086" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82085">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=aM9wwqLpS3edAZhEV5XgsDCo47Li6vyA4Qhe5vvogrN-Dd0Hg2tdDRJogILaR29AuHB0oh5wqiKmPa7eDNk9d8qJrn7LAQrExC6QPetIQ6njPc-zZ4_hncG18aywSc7W0GNx5qbxlZHgmypT78kUSBNvrfCUvH6bvhq0EyQh4Z6vX4q4E46Y8aRmvxE5EMcoGjBHpRS48f3u9NK_4yH1bWoS9OVc4SPFixctZ2z-GSh3yKapyvMxhLttkp8gSwDZgQl57vtCTlnv0dm8wAJ4oGd2VT29-Pm_nU5Z7qGY9ibtrFwi3M5ipEulDmgtczQJhP9wEJi_GghCc-boA9thaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d87d048c.mp4?token=aM9wwqLpS3edAZhEV5XgsDCo47Li6vyA4Qhe5vvogrN-Dd0Hg2tdDRJogILaR29AuHB0oh5wqiKmPa7eDNk9d8qJrn7LAQrExC6QPetIQ6njPc-zZ4_hncG18aywSc7W0GNx5qbxlZHgmypT78kUSBNvrfCUvH6bvhq0EyQh4Z6vX4q4E46Y8aRmvxE5EMcoGjBHpRS48f3u9NK_4yH1bWoS9OVc4SPFixctZ2z-GSh3yKapyvMxhLttkp8gSwDZgQl57vtCTlnv0dm8wAJ4oGd2VT29-Pm_nU5Z7qGY9ibtrFwi3M5ipEulDmgtczQJhP9wEJi_GghCc-boA9thaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران چقد عجیب شده، تو دیجی کالا مواد می‌فروشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/funhiphop/82085" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82084">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgcn8F6VhqAMQqNvPP1M5ygI8LAYbA2MzevpJmDe6rrGR6W8A0Mqnlm37cqU3KcL3EbA2CfeQMhBnyCdiCBs4O4Jezl-TsiiHAnsxgxlrEko1pq72iBwC9g5hdas6hwcllRd4rp8NeGZmRPnGsjvJ50OdVFHBY6BXv2BQTw5xurhZNYO7xcaMi6jD2HmAP4bDNrjqWK57h_P-aNdCSdtNs92E1aKJh2A687WuhDgagDXrI_khmqJqZ1ToZ8EIct47-FtvUm47xt19n45xgqD-O5C6G-KmVubTCaH25Tv06ZeVeGE6j-_GI7_OVR5H0b7kBRmdyjnMQzBLfxY4rIe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دورچیو
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/82084" target="_blank">📅 17:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82083">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد   YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/82083" target="_blank">📅 17:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82082">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dps5hyil2ID1RQ6Tyy4u6H018XqSy_c_eifXG8UyZnTPA1Jb2SBq6aI53S3UxgA0YF0CX-rZPzXR65Sarw2nbOsfQfY3uDsOb6paa3FF9_iYFu0zES5MgSjOg1JDRVBOUQgEQEDGPd_d610Jx2OiP3F5vlNB34FtN4oJEsUNKFi6lWfdu9pSr8xhYQzuxRXCLRQ5Du2OliRsBXNg3q3sJC4MHxymKWObUZTAH9uLUUFomWkxrSfkbCc24MoQFuqZRDy4O0FNNSVjAiSPaCuzwvhz5BhS2DAiu9vhIHTfuExXKMFRGa8YdIIIaGwaRcZCOkHXp5yoQsXBrosn5z_VfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید متین فتاحی و سجاد شاهی بنام دو سه سال ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/82082" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82080">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/funhiphop/82080" target="_blank">📅 16:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82079">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترک جدید سجاد شاهی و متین فتاحی یکم دیگه منتشر میشه</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/funhiphop/82079" target="_blank">📅 16:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82078">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8AMd_k9AmOTOeuz3p6cMA_S-63UJhzpRSs3yxPtuJ0VBqCIBNAnuJKSGKruG_rLquOigbA7ZfZkv-LvqrISBqvonvexSgF6f4LQGiZwVafKJNHZ_baEl9haUQIfJna8a7FHg9RT40ipg7OWcSxXwnWiz036mBA4WqqSWS9SgTbR_7tDy1HKwVJS1AGFeETqEnVKa83QFeoCx-HXWI8OAToTWX_BFTfjKWskFWhvMyJMWsqoZP8wYLt4h1MEcMt5HAxJZKuhHDUChmLGhzucCq_y2FcAoWe5RBk3ALJnRcwX8Uco-0ZasCKkgLPcUeEYpini2E59lLMbgLGBzpi18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/82078" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82077">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بوی خداحافظی از فوتبال میاد
مسی بعد فوت پدرش هیچ زمان بازگشت دقیقی به اینترمیامی اعلام نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/82077" target="_blank">📅 15:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw_uLJTY44PKJHAbdt5Q2eMAfH9yM6GpBu7GY0By5bnLnPCxSxQEcot2Ld3Vm3EsIAUawga4i4ArKd40NSOEIgdsj0YhOKOosq0t74c_7ZG-20WXbKeGfB6PBOpEYOwgQOjzjLRCnYZN34qgeEazpyQRe_qYGTu2kv4ze2mKGKhnilLFGbUE5cd7CzRTZ3RB51geeTGu6wKvFtRBVNWYMx_J7c0YeQkHbl2vq2W4DhxLi58xvrO31qLJFgs18n_bGRZUKsl6LB_oyEl0oUN6BKpvzcvN77riNcSR8I_ZrhgH-EKK1wtRumLYrAhwu2RIWLj4lmTLJ8gMvLPdTgvqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجشنبه میخواد بگه دکی بیا بدهیتو بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82076" target="_blank">📅 15:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AV81d8n7VI1nbbQIBEl-qFUpGs1gs_fP44W_Y2wQMcHv1gVD9_Vm45NppnIFAKN82FybWcCgQFZd0KwKbBF0eSpBGhI6yWdbU7T4XG_3vNM5yJSVt_W3GjpDnsig_lhw794mdEAIN00Zls1YMV66FAH4f4SXR-99ImoTiMQg0tLX7FafGuL3IyQFQf0Nq5Abd9DwEh3xHRzyt_kVo3BAYybF_KlDAB322qTfjatMfM5rsR8ZIXalt453PaxnpybDSpCzbhmpUSJZV2-o5I4AWQ_JAXEU9b1L44EqvJUVPMwVFDrGpvowqgbIDdzMQBdoJLqOguSqLNlJRHt743QpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7LF1cOz3cbVRUVnwKJQyqCf3HChcZy69UdEHpwtIvC5z2TcjwDWSM2ouGL6os0YJX0zIJUqQx0hemFEiBzVS29YoR8cI0yxobPXIcYbzXHDVvmJooC0rFgacadCItwR1f7LmFkyWUN2I0q2gM2HWZdZZAIaIGZXBLDYgMDOKUdQvOqkooEHSL0cpxlkeQqnIKr6dOuY8v4iTIl8XQqlGDeFfjIrT4waebXNw5jV_A3NNvoSzPGLbcV0FhJBxCIj9lX0yVgpzlJJ-gO4Q0PCO-sUYhQSIwqldq_SvZManRZ6Zd8JjNE13fdvZU8BgY2vAGtbgMu4NzQWm8IV9zOvlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/82074" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5IUmzvt_NPLKhAdTEV5wrYktelBvztgjf9V8h-QDIfGKMB57uUNdXZh8HgS2tUuAyG99QPWjFSwma70GdNfS91I3BdwTKKNJAuuuMd-wH01kz66d9B9bgCfyGIXhUQS5Qj46XnUDX4jQfzRy1G8-I8nmNbPca0m_N6FEq8K5DljPhNcY_d8nYChXjtJazO4KJPwBHeZre-xZGANHLD47Q11efcj9zXUeSrI_DWi7rYuIcxUNClF-EWFQPucci5VvilfdzMXp9TqoY8G-E-2UHrn1oG9X7R9UwSpTigNb_2fBSRd8Vx5kwNoiEiqk3RVr9aziXKwTllIOiDK9_rCFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیپ استیلر ۲۹ سالش شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/82073" target="_blank">📅 14:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82072">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82072" target="_blank">📅 13:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82071">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82071" target="_blank">📅 13:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82070">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oaey3u6TD_FbBj8DHVdYCgk6IrPDUJDaIdgF1tI2k4xf2N2H0CUL-so36YsjCserj_NWBrrC_9PtVTr-8lXsokHPbU0p5Hf0MRJDMIsIAqOj4zfTvi_22f0qkt2iau92Srsenxle1IgpKPWQBgvhFONZ2pqqxa_A524JuKCCXAWKJcJ-2UA_9PQ40WNKtKzPBwKMXWVaAa9QY_Bdbkk2-B1_rNCjeW2Lq3Yd-mLa2j00WH-t7xObX1UgxIaT_CDU9EUmSSNF7IkSvt0wNhHxSEcO4mS3bafjda3CkltYpkSyhAvggpxdShD9fr70SJSZFq-R7aEzrtvecVaxKOctgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک پولات به گا رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82070" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82069">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEWwLRJ2WIhXyAyN84UO-en-yQ5FqwtatWyGIFDqVefuBIKQUiKArchIqB8ginbRAwhlUCtD3C9gqEbqAbq4MPvPYDLST5bUTrBHquWIuTMxjEBEH5gG8_akLG31f2tmrDOjoUj4-Rj3OnFzqw2JoB0efj9-iUz2U7bREYFwml7evNPAkW1TyzveGoaUOXL-QKeZ8R9S-KuseB5DCRXvKniiJDOFOzmJCqrKSHhYm_vCFha5GuD__2jC7n2g9dTUUR6hH8F6o0WWIAYW1lCYeT7tYw07yLn9lnVxldedkRHo03D31VyDgMNwYkwZO4IB55rBFYVTcYcPh4Nef13fLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82069" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82068">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIks-Uden1rQEJmUZqWUNwnO-WPgEpIBvI4Rzzf62gOmI3vdx-OovOL5dwDmFgbZq_JH4SfLxUJ4Bn3ZF9XJ5nS0PdcIIkxARWOU7CRckJqJ94CwYqiNYDXnXFKmNV2l7onzFCF6IJky0g_ay9ZmUo5FWljrbZtyyhcy7Dw7-97i2jeH67x5jyZZhQle3VJKQrpOF31_a7xEmMoHHeyBAphGk3BbvxJIKNA1sD0FHHc0Q0Ff4uH-h4xAsL1KkccZr9WphSp_GVzWz7CdUe5zsGFH6rQ8_yoHgPGfgPN2Wvg3mnvmTpmyfaQqdRf00x2dwrHuLtzqAzTCVELxfn3RtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/82068" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82067">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hnu1ml4k4KPRcstNnU8_vfg8arsF-FlQ7eUmkyQVXuWp2Is5MOlhGxJB4Kgsw4vq4TYpGw0q0y-ii9Re40586c662qPntDpQy_q0k2ypzf7uAqwSrhzPaufKIrQ5CEs4N6Z-A0PXayvCyFPTDboSDkCNxcflp7SgYvBoIIfZXgs_sjRLBZxxwXRCLyTge6eCJcNeHV-VjoQGJZqH-j059hyPoqGf_Q9nYEm-vlEYI0UInN_4HKCqq8XHQZCPYHxQJxYQVgBhqKVEXchkY3VbLjMRfP4CmhyJXIScB0KwH9tf4JYDmN3vuakxX45djVkNs_R9-s3elynbN7WclnwD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری احمد خدایی همسر جاویدنام صالحه اکبری از پیامی مجاهدین خلق بهش داده شدن که در ازای پول علیه خاندان پهلوی استوری بذاره و اعلام برائت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82067" target="_blank">📅 10:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">داشت یادم میرفتا
کصمادر جی جی و دانیال ددان
کوروش
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82065" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKkVCyldFRKPsts910ClSAMsJ5u5zWfMxz_iRwxbDIXoKMmzXpSWFYMwt7Obp0ojeqvt60ePV8UquXsw89d9rjLBCvKax2wKcPJgNXmxRW7RO7OGGVerOpHYIOO3DFZq2SMNDbsGmBFd9ZgSSKPdWy7EO8DZCFzZWp61_tDd8-SWscaEjCq1XE7zXvZuNFAM4yRyi-ri2aanSmOa_j1gxM_XluDttG4kURehjAdWVFqPogCZKGm7IJQrnraTmzPqWpR8vndxjOMM6294nXrIRXDZlOLzbupQrGtLuLHOnHWSogtYNGmcQsGLeUKjaJ-bhbwUB_wHyNNYvSi8UvkFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریک پنج ستاره از ایران داره تکنیک های مارکتینگ یکی از موفق ترین آرتیست های تاریخ تو این زمینه رو زیر سوال میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82064" target="_blank">📅 01:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82063">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دیگه حتی دکل سیریکو هم نمیزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82063" target="_blank">📅 00:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82062">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_f4Dma7OlVcvgBgeYNFAnRoSllLM5Glr-W4cUxbq7Kg-5neYFZQ1YxXE5O6hXRtxoPVshkw8P8z5Lln5isc3v1lvpzjrgZ8OPK_kH2pUDle7lro2apL66Jb4Y0xe2Xl9NGkgmuFUVB04ObWKpAVIVtW6OIWveiZn5IB-TX0XU4Cs7KnnqOl0xD2iGtBb_zqleoQNfZ7AJMOLUOOaIwJ5mnKdycYSrZ5SuxwTrFwu2MPdI1ygJPTE_3iMPRLMinWj2iHfViWAXB9YB2L7mXbuQujDZA7tGfTs2cLtKocDSPJrjVrAnEHcFAFXYoJnYevgDLD0SNdiJ9JscP5ujhExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح امیدم به زندگی :
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82062" target="_blank">📅 00:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82061">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید. _چمن در خاک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82061" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82060">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/litlMH_6BOmtkGrYXVQ0TyApZ3fXD4fNV5Ydh7sCsgIpbKkG6q1xTG-EYG0dtLItqGzZDLXyjAeRZdjg_TpswImClSKlG6GNsEtjV1vITOP9vAA6R_enN_cEG_jpzmnO__tsNLOaiGS91ncShBXwHeepxpaNBpLPojAagmHelqqGO-O4exH0y5cortp-SkKKLOnEUQKgWfpNNZERVEZbSIN-I4ODvULtVd9-DIqe3RFjplrJDmfFofDFLcOgiEEzId4fC7XWSWTAkVhhgoJecZuPXxcD595f1AhUZfsAmSdSUWEcJx1_76t-y0gQNdxvwD55RIGcKBzDOaFeJs3wpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بی‌بال به نام آزادم زمان منتشر شد
YouTube
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82060" target="_blank">📅 23:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82058">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIcRiIok0pfMbbFZc1vQ_TqDnSJY5vmT06GkL5kME1jpfscy53zSxFCSJy0nWIocMGVkGd7OO_6ic-cuPrTV9CRsmTQFLhN8wTVRn_RI7_FGB8yaTWtwRx4UNzylZiYgVFetc7CzjhKsUMmazgtZi984jlZ1KJWDS7GddHj19V5zj2VCo2he3OD12k5PEvMV5XZPss6-QCmCpcuu0Bw6FAqp-3Tv7udffba_v6X1OeoAXnXxdJ0e_QmSpz0PFJ8UVFh4Q6AsY3fVxETUf7NepDsFoLAx9KZhyY0x8a45JdTs2mVwtA-aeH7yxNrpYzsCo35-xfP2wa6eSN_wM65cQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82058" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82057">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ عالیه
گفتن خب تنگه رو میبندیم فشار بیاریم، پاشد رفت یکم اونور تر محاصره دریایی گذاشت گفت اصلا خودم میبندم
گفتن خسارت بده، اومد گفت خب من که خسارت نمیدم هیچ شما باید به ۵ تا کشور خسارت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82057" target="_blank">📅 22:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82056">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید.
_چمن در خاک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82056" target="_blank">📅 21:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82055">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82055" target="_blank">📅 21:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82054">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=KpLfnNf3dYUV0p6cZxLgqQ--BWeUr77pfCtRRqMe0g9hM2zkEajp6Fe0cZajaNmN867T9D21ir0NFbmeN65tWYWBEBWTnqtYygSzOUThYSPCka6A612Wk3fIl2mz88sHXU0JzJJlB7Quh6o6iKKJMUG0_6DmqIsQyV1gXOm1h3UwnIha1xYD0VB4HRCKay2z8x9LYL9X9RzibZZjV66jlHlTY7wqDqNNLN55QzdJ9c5Z2QiKSPwWblnPwhRT1GRgGfaGqThyz90m-1OaLoSqVBAHHxGGHoHfC5QCnK2E9FIC9lVzDH95_evebeXlard8NQqnRcofz1QpCIMzosbGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=KpLfnNf3dYUV0p6cZxLgqQ--BWeUr77pfCtRRqMe0g9hM2zkEajp6Fe0cZajaNmN867T9D21ir0NFbmeN65tWYWBEBWTnqtYygSzOUThYSPCka6A612Wk3fIl2mz88sHXU0JzJJlB7Quh6o6iKKJMUG0_6DmqIsQyV1gXOm1h3UwnIha1xYD0VB4HRCKay2z8x9LYL9X9RzibZZjV66jlHlTY7wqDqNNLN55QzdJ9c5Z2QiKSPwWblnPwhRT1GRgGfaGqThyz90m-1OaLoSqVBAHHxGGHoHfC5QCnK2E9FIC9lVzDH95_evebeXlard8NQqnRcofz1QpCIMzosbGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82054" target="_blank">📅 21:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82053">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ:
-
من می‌بینم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماهه گذشته به آنها وارد شده است (آغاز شده است زیرا آنها سلاح هسته‌ای نخواهند داشت)، حتی اگر هرگز در هیچ یک از مذاکرات یا جلسات ما ذکر نشده باشد! اما این ایده جالبی است زیرا اکنون من نیز از ایران برای همه افرادی که با بمب‌های کنار جاده‌ای و بسیاری از درگیری‌هایی که به خاطر آنها مشهور هستند، کشته و به شدت زخمی کرده‌اند، از جمله خانواده‌های کشته‌شدگان در ناو یو اس اس کول و هزاران نفر دیگر که در جنگ کشته شده‌اند، غرامت می‌خواهم. علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است، غرامت پرداخت شود، و ۵۲۰۰۰ نفری که در پنج ماه گذشته کشته شده‌اند را هم نباید فراموش کرد. من به نمایندگان خود دستور داده‌ام که این موضوع را به طور جدی در هر مذاکره و تمام مذاکرات آینده قرار دهند.
-همچنین، در رابطه با مذاکرات ایران، ایران باید مسئول خسارات و مرگ‌ومیر ایجاد شده برای مردم لبنان، سوریه، یمن و غزه باشد! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82053" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82052">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0wCg4DgKPK8tbjkyQLHy6qv1Yagy_HhjZPinLY-CNfaMrvnXB46-JjgKjD07Y_hVnXhlYXVqOmWIW8EvtNm9Vv2bAcTbqe2QngqxfUENGJ1Hguv5tgx7Sf1DtJJrIlEaUPDsFpk5a8ufFUYapJFN6Fai3osZs3gwNFPObIgRNZ32HiV4OjBB4UgwUQ48we9YTXK_ifZ8y-6n_suWAgmHza3KdQ1LpYoa7NkKbN_5OO4k2N4niJLxzJFVDZYuJhQ4F1uvj5f6BWHlFqVJZ0GZCpg-QgpcMIOYx_Mt8oOjqfkhIlovwhObpFKdwWbuKRP3xtxUlHdFhI_eS4QdtOaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید امضا کنید لطفا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82052" target="_blank">📅 20:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82051">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8xnXTOjwbzs97rF6ku2G8HxOcFA4xnLL-ZGnx0agj4989nE6gdTXuuN0WO4lWV3hyE0yedAdoIiK7iDTCtcCLlzpPe1YaKZa_q9H3b0VcMvka5HhVhDE70SNMn52HJFY5OZ_dRuWDdMUrUtB66qlOrRhI4g3wcZp2ZMRTlpXymX9QD1yC7XC_E6Wm3-PyVInXzdiZkT417lm4kAqn4_mjN9WBPM_eGo_qVlHkfkQzNxMzxh-8uickcX5NbFYKe7y-XsqJ-OnDuxWsJhU_Iqg1FyylUenqIYiC2DQum5zgtTyKrW4JmLh1TJR0h_xVmzwNkJEuE6mWNoRHKSWt_33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش سه تیتر زده جهانبخش رفته تیم صدرنشین لیگ هلند، حالا چند هفته از لیگ گذشته؟ یک هفته، و تیمه پارسال ۱۳ ام شده بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82051" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82050">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKBK9HfOQ-vsbwBnHFgng2j7g0l3uKxTKDDsBCak9JfFjXpP_rFTSi_VnlbzD88uo7A3sre8N8gVup-fb3ENcdZcDKwhGNmz-h7kGgBd-KRH7l79RazwanRzvd8zLITY8FwuSJiD-18pqdy-GWhzKI9dav4bGNYqmIEy66Bss7I2-W2ZX8c3CknPaCp2Lurw0BslF87M7KcGTTcxdfoukhVFZPIGdRelTsUZo8yRJxWoHtxJy73F4grAFu7m7RSY7Wz0l45yoAo5lgARGdUWSgNILFeyTUX9GQFCPpZe7Ltp-JcDe11_WQBWpGO745fJPRoEsoJauI-TpcJPlTqc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82050" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82049">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_WAY4le-qs3U6lcFiXRrVQ13SMYCSthg5qMGXBvi7_ClYoberuza-bjcfy7SED5IFD1zm9qiMPctls_R-AqAAcsiRmtJziWa03v5h3XQ2pptEopIl_h7GX7jwi1y7S9QlfqTr6L8odNh1PDLYTm0lq8Fdjav-SpTnM5B7BVOpGt409bms2CumRnKnmBjAa5iSp8p3_768UFKR-z3QoClF0PRgOq7_6RUdljSm0rqvQdcQdCHN6X6ID6Gc408uZXoAF8g1DyfRW766dxpia_unGA0d_q9KWZKQM2x2G5Upqww5P5bk3mH-TCU5YboXaas8gp6XtTFQaeBNZOuvjDSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82049" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82048">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxW01M2YQFAEbYlKpAT1HkCKFrc1m9sbpnGf9E7j0O4EGBsz9rFWjtaY4F9B0j28ier6ilYKX-uPBBA69ydJ94lzacFN3ql8pmyPFAXmnNBWXNN4qNOq9yOz3aJcp3SK_412YxaqYGjJpUD01h3XhzOfuk7vplzpAEMdaOFU4SFm7GmLWU-dQ6OquOKUu-74HWjKnFF3gbcuYYdk9cQQpUXDw18xJTiJNB91mPcokAcXw2N1MX82tqFZ-U4xTqICA6fotHogik2fuxjOf9tCl9T_A0_52BccGcxDdvN9G_ydzgeIWp021W_0cj0Hml5jOeuaOdFygrTV4fN01uvhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید بانو لنا
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82048" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guZIJPuhohpQpSajd8q4npxzEe9nFUl2aVCKfLXomZHFUQhfQAk-CWCeiTW7jHEfQPyS5ARCa0PLIv9cHUkSt3Wl_iVieEemoVHZ913EvoMh7na5knOPsIoQtZYHTfiKPdjWqg2AUZXQtr_mK1mjiyaJ-cu0E76M3dR1XLTHxNQqjf-fOynhoyoqUeXwiKFiOmVuUaYB0j40kiSGjcmKIsRATmZDnN67skOx2I_B0IFcVA42uDed3env2arARROv1G5VpeYiflOqin3NhUUD1GIq3ZGhEtrBtjLgKqy84bGBcno-vXaCiKjdO3d-kbmmQpRobbVjunHynAp4yWNlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوماد‌های سابق و فعلی علم الهدی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82047" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زن ابراهیم رئیسی با احمد مروی, تولیت آستان قدس رضوی ازدواج کرد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82046" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ویناک میگه دکی لندن نیست، ترکیه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82045" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlHBRoIiK7y7KwTwSduQXXQQ-BLRBzl7hc_rUgJDr_gDRbBBHPFklOmNItD4gvOw9ku3B8sz3wSWZzsYeEZmhOT124DBQPs3GFVaOCWP_cf5PycUpGfGOsb69viQTpWp7sHShc4ENNFaIqulvuVGnkyt-fPHzyCCFGgcIlHg9ULWeLZMsDQZgloLMn06Et4vNh6iosSxWpSVnaIQxI2H2amVW7LMMrOiQJa2i1bBX230hK6jJ5yGyBmPCakzDcLznKdbEhhwT9X1EvDWsO-l4t9lohOIHiez8p-sBqdBOUGO8YO-rkuztAi6eXffvk7YPu_QTkH2il5wqSAfvB4_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو به روایت دریک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82044" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=iH3XTrVLXMUZXoj_VDfHlPZinds7Ewq0gJ_6r458cECfIE9D_ual2V4NdI9zsyZrqWZB_PtvyZTqBg8_Mwo6xuV7MCnaCc0chqg12-jwKoE8gte3lmm9p3K_yVGN7wrxZC3kHTG_xhrHRByGarfO3kxgEzG9qCumZG2aUbuFlXE7BJxKLpTnsG18P4hB82J7iNFBFRANnA6nkPK6hM06LGlwJzm2FzslZ2bf8hA_Rj-2rySrPsscJhGo07ngqH9zfNG2FyhsvYCHs2b8lg9VPZ-XpDejm8ba2yaGJ3mmyoS3T7mPVkG49xAjpQtAIxfP0qPvfl5mYaoiQK-FqkYfpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=iH3XTrVLXMUZXoj_VDfHlPZinds7Ewq0gJ_6r458cECfIE9D_ual2V4NdI9zsyZrqWZB_PtvyZTqBg8_Mwo6xuV7MCnaCc0chqg12-jwKoE8gte3lmm9p3K_yVGN7wrxZC3kHTG_xhrHRByGarfO3kxgEzG9qCumZG2aUbuFlXE7BJxKLpTnsG18P4hB82J7iNFBFRANnA6nkPK6hM06LGlwJzm2FzslZ2bf8hA_Rj-2rySrPsscJhGo07ngqH9zfNG2FyhsvYCHs2b8lg9VPZ-XpDejm8ba2yaGJ3mmyoS3T7mPVkG49xAjpQtAIxfP0qPvfl5mYaoiQK-FqkYfpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگتم بانو به روایت دریک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82043" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6XU4f337qU05kE9n_Z-G3A2-xyLBUDIMhH41QgaPHvWD6DUqoor2NYePMJLMsVQwbZOtfBc04Gx-4IReeKeSn7Y35KfuMc2XguKr595SWLQwSmKHNDLgC3y89zCkWGw7RqLhL0uvmDcq9jCWcb3W4j2ObkiZ1YrJTZrR0WjiP27ywHJIv1SQikJzwqgs7YAGnjRYJtIyKmH-SSHOB8nPyDwSGDWMZFYuHnGSTPufEKSpsuuI-uydmvGkLaseWIo8MGdYimEZ2oVC9mE8i_iCFZyEcpLXvnwRcFnbHHstdKtwUecV6tuAwwJFASRG4aKIZkYLvjPTm5c_ny_T7gpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۷  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82042" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فابریتزیو
رومانو و اهبر رومانو این روزا سرحالن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82041" target="_blank">📅 14:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW4Q555C_GloY0hVfZMyiJouJdDODRECNSh13J3Q5k-anQ05CtNyaO1jV5gG5qPO_ecrHNdPFvotELxtSO71PDeOKBVuUUgfTQdWG59f3KApyhCYyJXRFCNT3EShgeiPc3Sve1N_tuZGhZRQ0AFq9OnITcPDImHp-DULSFNiIJWw-scFVUpXOUsOgJEGfyY5TluQRMiEJWZBpWtE-p9zyKTFW2JVK93Y6yqcnDZO05A7W1s5WpH5RgVD5iuKgSTM5_X8Qnwq05-6xtNEyf5v5xPhX6GBrEXb6J5zD-MR1iS7vhbNuiVvyTLm16OlF6DwPZm09pLCFwVBil0XLJr0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی ترین رفتار پدر ایرانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82040" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gruH-bODUscCq-xlMSiuivdsuP-zdE4B5ZlUONHzvHmn2n7IFwPfdWFP9O-LOKJP7VeWef6QKvrbobefDZa3o_mq5DpQQ_H6X9x3FclFTSfVfuTVpnO9KKiYaIihl8q9lbfX9t_fxLv-Lfc1Xiv9dGpNQe7Wpoc8TLM8pKB_TOOqud_SDZw-yYypy4Ekun4-2xMsIJhSiYjzivmga8J2w-wydRr103OD1EyXh1YUcWx0wJr4yrffNiDzzuQqNwLOocUM0eLW_5x5ufTCVIl-I03gPkGd1f6r19cEJWhULl4h74uIvdfAD6JQL7UyJEjEmiSb8qKdxsq0dQpAlCSE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده خامنه ای در شعام، محسن رضایی: باید برای رفع تحریم ها بریم یه اکانت فیک از ترامپ بسازیم و توش بنویسیم تحریم های ایران برداشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82039" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO6vNMZhxttxsNkD4iJ7tcX3V_R0H2reDL7JGfcTOqB97Imw63fKHkR4cXytJB3vuDxGgb5_GZg8cuLEQ16XWr5L2C0FTVvc-VRej_oAkyOQmxMTP5rDRPthKZkxd4YueXkVhGvPZbQXkZVlt39CWplbuV-JOsnX7rnFm9g5n2eRCK2qW4gLjJ9wtF81STI5U4zUk8jxG1pBt8id49UcbF-K4iZnNb9J4ElUeXGXURL6pR_RV9KPl3yQmo_jXotqsD_TY32MqqV-U5lhYmRoriqHPIQNsrG594Qwq_JX0yJSfbbKvlmaj4dpUzs8wumal_sPkQpt7OLq4Ygdln3oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فداییو دیس کنید تقصیر اون کصکشه همش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82038" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwSr8wVncAXN9erRGbSCgrSoN4iRx9ufzmSLSJby4cMpep7-ucDxZrz3_wBZVHp6BHAqyMIEpXFAGvh9OnjU4who2HnlbaqfKcTCL1iVG5eWNf5LIe-Gkp3-ISaSTV3zX69ZGfPpdE3IeUEkuTumwJIregP0OGg6A-oPqqq444lpcPuOs3EBkDe9iPxO0A9iBrUQPWr2HRokLWQMvK9yHfnJtZKVM9UPVq4C53PSOrvnna57FO9KtC_VGhc-kubqlkq4m4HTjAFrD8aS5Kt41OEm8HDrq4S5o9EoD-FlJC8eOQhwQ6asgT80choCcQeWcNzOItNoJ9scuf300DSBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ راجع به ارزش پول ایران
کپشن: ۵۱ سال بد رفتاری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82037" target="_blank">📅 12:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uglEbAjxIolKSYuxu1C0Qr6HGD1P-sik4S-QbX125Av2GYBBQH1JU7yZTQV7tVRMUAhimmISrOhwJ6NFYNLMp036KNYp54PBSkBEPVaTsBooCOxPvjPy5v0mUisuZN1mFeE6iNH72fW0A29gsHihc--zp7AJmtHa_-L5egbKIRkjveMNbEjl6Sr6cTf8VC92Z7BuVFX7zcWI3MeH_1JA-xj_zvv4bqAvyUhPyHHGwmiVs5dixkOw_O7yJlOSxtfCHL8-9BGYkXXIFQxxGC7_XE6z7yoqE01FdShl4QgG_Ica0eNUBlCZ2b0l2c2uFG6iszsbPMUKlUKdCh-eqA_G0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به همین اسم که تو تصویر میبینید بزودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82036" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isgS5mV8UHAqOjjGiCRmEo26I4IgEoDExL5-lZqvpAaPxnHvIiW17ajlUYxXU60DIfTDJb5zVOYzZ9Gyg7MmxITdtQapt72dsyCJcN02wVvy_im-xlJdVsmICrGfZMw-FDoxOG57JK7ucUU18ogX5ynXYKCN8AiSPtkGV-tmCJ5RlyK_Kzer6YMEK7eNjWTTd5-tnPBgi-yBVBXTfCorN-0TVgdXTxfKJIU1HQwsagoYQiYEsw0DLi0oGo-V-2YgAG6y4rEdTs8K8RR01mn2Skxd3Tcm3vYQfDYxFtBKWmou8-Rsd1ju2fEMQA9wMleQ_-TNYLkKKTz7LwkSoOYE-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82035" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMYzyq4x2XbAvq_pBO-cO8VD-PnMFB3ZpGq1oSjHrWbIv5zPW-egZUoHoNltYlD9VNezNT4rYag37VOpyk3pIsDXP8GvEMVYbkvMFIOXL75VfbBJe2n4tND2dDK7V5G9XTYN7vaPLC_sYzzMfPKG4fcRdcQOJt_ZftcPWFNzRw3_yxmlpFQ_j8zuj-6qWjZWs-GabzOl3s6chgngXXvDWirwU2tIO5OKuTrM2O1KyTeZ3aZBSjptc2gtN9_fFBLzf4IpV_0Yh8ZGQyG3pyQclqCvbeSn8vSLGCh_hvaLlb9lMdmIOcGc2X8fiFLMCrs6_TqtEXnKL1YUBDlxHMTacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپو میخواستن دوباره تو زمین گلفش ترور کنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82034" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">از لحاظ روحی نیاز دارم قاف بیا بگه "قاف، مهدیار، ملتفت، تهران"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82033" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3RaNxScS0hApbRLjb1IEJVO6buOnBP7iNtgwiZL1lWRuRa9cSSEog5O8CJKV2aTB7-CLNkPaAGO3d0HpCEeBKMF_Zgokn9Y9rMbJ-vhdsra2p1xa934HYoa5sOB0bYIJrxgMxjLda4Oy7X-CFtjs-xpnQwNxeoaYPkjUl1B_oHgHU6W1kKKfkFWZJMj5m_7oL3_KGCzRUOygZLD7_VZDuxPF8fhU5JNEFAHLVaN6aMf33K4Ffpbk3t87i9sbP5AFQrraxCOt-q-BLFC6tTqCF30StqHvHaF7CvtsqkmDWoRvgrkuX4pdsa4gviv4YezrX28WLxrWr1CEmtWPRWDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار برای سروش، خطر در کمین است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82032" target="_blank">📅 02:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3-xiRSxnmUqr0TU58o2XUMkYwpSDi70siBFVL0C0J7UTZqAvmdZr_Ahfaf88JYivDIePT8PCj3j0bw0vaks1TrWodnOp8otBm0zJHo8dPLwPUFMyuOu_86Nv2kHAQu2zPkPzmQEOTxMmYZ_GOti1BZUMydIo7Wc7c8ioMlZtEkWdY1FS5X7uqFbckAxcbSaDvcl36OLof-vUC7r5WHUbrXWrK1x_wvm-Xzoe-heDdAV0Pr-EtdgmshE3oXgjlTK1OggjaGKwB59uayxYar7VC9jbBqCHSJIp3v84ITP3sDFoUsQhRl7A1YfDFiY-CdqLXszGFqsYZAPAgJLFwZdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی داداش آروم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82031" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">منابع امنیتی گزارش میدهند که ناموس سجاد شاهی ترور شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82030" target="_blank">📅 01:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">4 تا انفجار تو تنگه هرمز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82029" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سپاه زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/82028" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb6fwGKgJPeInTEz4YbiEwNl3FmZCvzWareAVHg_F2noBppxdTA0KES_041LKDOork025iSpz9HMRhkQnHTuJSzKMNBkAzdvolhabn5VjaVFJWBmNmq7UGwgFYwb9WWB27nVZ0ZULcJ19GQWq7vC6BBuXErfVhgF1ksOFUB3YLoLj5_G-aaN8GQJ77NvzOjmlCv38lczBf4_rU0Q9OSZyf5K-TXFkbPj0B7JwiCq6cQ_mzqBDoQ-iTzysxQVBCIpKWL_8wcyks0lACggXtymQr_kDWPWPCerFosSlf-6IBuuNemPGGNtsjJ0wtxVwigXI6zlOquFNR7HU0oGC9sKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد عجیبه این عکس دکی و صدف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/82027" target="_blank">📅 00:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ژنرال محسن رضایی رسما دبیر شورای عالی امنیت ملی شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82026" target="_blank">📅 23:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=UgHVT_MTfY17yHVtxeu4SN_Fw8uMKr1VK5HCzXMer6d3fACN5DpXlq6sJfuexkRwamCsIX9D9ZJKOk6d6ldbzPUpbZvNS3XF4L_Q9siANpsNLaQ03W3xfMKXkMUGuwZnVY8YZvxzkwareUdkKijan-cLbf7QX47oFitiYg2WIyVNyEOefXIPdiTZKVxbpoI-bSUaS8cnEbK2wU3omJjnfP0biGKgd7N5CtaatcselB5xk1jhi7xfIg1m-AY7oV_OFsj8zufV5nG7vlWPzC6wcGwzewViqlyLv6vG5pSU7ZfUhWuR2RDG6qNEPODzLX_GuXE27NVEOY-SYohFYF8NFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=UgHVT_MTfY17yHVtxeu4SN_Fw8uMKr1VK5HCzXMer6d3fACN5DpXlq6sJfuexkRwamCsIX9D9ZJKOk6d6ldbzPUpbZvNS3XF4L_Q9siANpsNLaQ03W3xfMKXkMUGuwZnVY8YZvxzkwareUdkKijan-cLbf7QX47oFitiYg2WIyVNyEOefXIPdiTZKVxbpoI-bSUaS8cnEbK2wU3omJjnfP0biGKgd7N5CtaatcselB5xk1jhi7xfIg1m-AY7oV_OFsj8zufV5nG7vlWPzC6wcGwzewViqlyLv6vG5pSU7ZfUhWuR2RDG6qNEPODzLX_GuXE27NVEOY-SYohFYF8NFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر قدیمی خلسه راجب شاهین نجفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82025" target="_blank">📅 23:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">۰۲۱کید تولدت مبارک ولی قبول داری شبیه شیپ استیلر تو خاندان اژدهایی؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82024" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=RMHmN9r_A7-3xR8zBOg8QKTm8b4XxcYnbnt__lspCeUq6XPUnhFO08EYpsM-EGp5ttXfc0EnlUHDXBeMCOBn0yKALJRxoW6By8m5og69tgtVrkd3tk4e6ZG9mm2snpT4BwlL52ZgCEV-xQS9CO9EsJH9mPjtIx1ITnOvXE2VVD7ZI0vicqy5t9mi-TYgdDTnL_qaA3Ap2yNS772cE-Wc50hOFG6imMcf9FXwhVHSgOYbXfMa71efM00d69l_y4W2_LCTkqXw8GM4b7CLg0221IflB8rqr_bUI8OwVKlAIM31O8DoKcio57LiXtsILNy40VpoVShdMhJYfnl36uvsAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=RMHmN9r_A7-3xR8zBOg8QKTm8b4XxcYnbnt__lspCeUq6XPUnhFO08EYpsM-EGp5ttXfc0EnlUHDXBeMCOBn0yKALJRxoW6By8m5og69tgtVrkd3tk4e6ZG9mm2snpT4BwlL52ZgCEV-xQS9CO9EsJH9mPjtIx1ITnOvXE2VVD7ZI0vicqy5t9mi-TYgdDTnL_qaA3Ap2yNS772cE-Wc50hOFG6imMcf9FXwhVHSgOYbXfMa71efM00d69l_y4W2_LCTkqXw8GM4b7CLg0221IflB8rqr_bUI8OwVKlAIM31O8DoKcio57LiXtsILNy40VpoVShdMhJYfnl36uvsAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای زدبازی، حصین، پوری و الباقی خایه‌مالا بعد از لیک شدن چت‌های مهدیار و فدایی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82023" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5K8XWcqrGTvFhsMi5F8ZEe64z9d12JYLAUlQsKnf9TmqauEY9pwpqLJwdsgG4MYKIC11BRcMtyZDvQk7gkF5W873DkE52Hj2feHdPiIVAX3-MKvKQaBLW5VU1fmKoV5lhJXQx8aEnZveHmfJbMWzgrbel6DzDhHofTWCtRC2I4FLgNbX4U3xET0I2Mio1eciuszMFEDn9oK-mONAtLMR2DbhyPyp4dXnBwUZvRl8PkaT-voYmb0G3PH8avPCf0OOIhClLs_AoYcvwkhh9hTDrvb1KEpExztYC3Tdq_Hgau6irn1_keOgXmGODaCOS-7GcrcNsHmbqt4gtDGZhgFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی امتحان سلامت و بهداشت امسال سوال اومده که یه مادر چطوری ایدز (HIV) رو به فرزندش منتقل میکنه؟
یکی از دانش آموزا نوشته: سکس مادر با فرزندش از جلو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/82022" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tpy8Vg972Iy9gYa1evyYV_i1sypXxgD_j9lxifC-nz3m0tdgJmjaxST690KCNIne4VadlKsxaDtgr4z58F85YKE8jOW6xal-O3cCONmYjEkmtSdahOvQGHUzmPwc-wZjDPthSYlOghmB6haPOeSnbPUeYEKHVkQC-mK_yOFPmwPpulMFt-hNYdB4zdbyJzzlaqUEDU8ibYMagIHVoBl1kw7SkgQxpKBnI86O3WNvyEQTkV6oK_GZF6-SNz1a3NwTXazCKbwYYoAUwD7Yhtj6Nbg0q4-ap_F3Z9RU94XV5HmbbVlOaCbUOZFfjA-W1gLLxnWFOh806zIxtojHqLlXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82021" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaaOhC3u5nmKeT8ukJtV5lWhp_ozSCdSLhnlA3elKkp8C2j-i-h4jHJQPuSoDybWeWmKFb_LgA-cTcZLBJMOS6woBjKI2gw_CUXK-4pf8AhC_p-lSBOjshZxmRg89v97ABS9k8ij80oNn5hJ5xnYpxGcVcY8Dw1ajFta2CtTFr-APB0TXsSLyez_7TMbpiTvoy4YYG3uAcJXbHufC43qLo7Sy__kzFDr-faxPWeKc0dHpkkpGmpcgB9-aCVTcjS8yKLY95SVzlrsGrxjn3l8Qz49ZtpKcGLj4_c3CTLHoZ-kWgMBC7H76XsqSzhul6LTkuIjMC2DO7MdRGUHb8aLpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82020" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6MfXXnXp-c6IsxFqSCVSs4pdurSSHnNoQk6Eyo2jBSIt6Es1xPQmbWZVGRH72w3oBM5IC01d5V5JZY0SxGp8IfvrI2mt1BBJPewMwUairAgq-ZoBoIjwEfJbUfgdSMnEAwtTNLoyGRK0lF21hl0KcIenz2Ai9u1mX27UZVJtYfj_wJWSiJXMQ8Kj2On0UjiVRVo110drZqtwVYWb7xjRO580L3ztknr6DR_nQj9qwSZffR67_7KRcA5YObuzUooZGCYyub3GDaCfkHJ7umg7C6vUyXe7FQMIa8BmuFX1mUxC6PWtbe1m65h0l78nRDXo946t4P4XMPTabkn1UPeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mR-c8Sq0ttqQZT3P2bwzAOFFCaveXNPorD25MAXjIaSnfH-Ji2WkLUslfjuKqlSWA2Vlr-8TgcgahWA8kStncTmfsdZtI-6rfzl8hJirPSh0cDRck3EkpXFoAvWaoVOXS3TNjYu4FYOUslt84uzcISSQuygZGQjj0Q5buQ9S6i7aBm8YhYqN3POgKjZdBXN1VUCGDxnPjQhedACBO1Zp3yWN03nCj5Imbni5a9f2zyFkGxkRDNqb_Qal87lEyIYY2FVuYlRTlKU_gkVdg-xbW2TmE91IWfE4V_hI_wTsDRgIv7An1gY6F0SW_8FqxrgJBmQZarTlL3tkKKVLxZhntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngHWXMNWUCuGT9CkHjK0VH80nZQqXtaXfoh3DTwpdcxfmUP_Xv-3qEKtYz4OZ_lkagjQR7T1450CPGSRHesMPrMleTX7tWwbvUukf0e6aWhcuoytdgsIoqMoWzY5GrIa2LJ6Xc6a0gtPwUwvPTdut1rBkzlfa7BQ_w4OsOxanMCcGDXPp2Ps7IAhyqMnjNAbZHC-3Yp2yy6-zqonSoTnuVLTQ4BCvRm8D5HERa3kjix5Hlujx-imgM8-JvWDY2Iuacgg_BsnA53J7se_1-R1ZM5gMY6u3uAOwLqjAwjjgG7L5xgZ5lX_TzWpwp8JRkHIdPwWnVVjZpuaCgjOqC5AxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=JdXx_MuMPzepp1dDIX6arqVuJMWYZ5RVCW2n97EQY2C_laOl0RSkBaZBFj7dt5pbn5OJH3JLvoZA9vOBu_dF8h_R4HQ1mLlmT2UoLV-FA7vsvSp-k6ue1xxi29DFYooeIpdSZ15xk0bEfEJw9iQHzaMTbBwgKq9te1_-dAf6YwTr9XuOmPcdgt1JjS_JabzKVksETrISfSrT5NL5ZORLbV_kRd_daEkPoXh4g5n8LH9kfwDJhKrPH_cWWpzdydkqt4iH1svhcX-y81bUlDE3XzZg0SOMSxmZm9CCQDnFGZYCZCYNgTqwQJeYeDJveNPTMfqJCOhKc4rnTaT1BmBSfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=JdXx_MuMPzepp1dDIX6arqVuJMWYZ5RVCW2n97EQY2C_laOl0RSkBaZBFj7dt5pbn5OJH3JLvoZA9vOBu_dF8h_R4HQ1mLlmT2UoLV-FA7vsvSp-k6ue1xxi29DFYooeIpdSZ15xk0bEfEJw9iQHzaMTbBwgKq9te1_-dAf6YwTr9XuOmPcdgt1JjS_JabzKVksETrISfSrT5NL5ZORLbV_kRd_daEkPoXh4g5n8LH9kfwDJhKrPH_cWWpzdydkqt4iH1svhcX-y81bUlDE3XzZg0SOMSxmZm9CCQDnFGZYCZCYNgTqwQJeYeDJveNPTMfqJCOhKc4rnTaT1BmBSfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیج اومده یه ادیت فیک زده که رونالدو بخاطر فوت بابای مسی عروسیشو عقب انداخته
حالا کامنتا ملت:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82016" target="_blank">📅 19:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82015" target="_blank">📅 17:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSnkV0rlqH49vTTYpdPEKgFgxLHBMsQzudpzX5MA7l70FZLvEcrlrpUB8F8qXo5GhRXI_9JrBM3NelsBNMhkW6raCYj3E8HfZp_oojniDzyyQidp3dyfYC6AS70u9_Pal5vlGoKv_I0XXsf6Lw2UbAX34TcpEG0tDR92InUPsArhYzdbS7Kaaj5SiRC3BO3S7O1vEBcwEl8kXacWbZ5cIrl_oS-Bbk9iJyclhZCVNjC3JnydMJVqN2-Ho1WcBW77_7DH0uCtWbMcoXHrdcuH9I5tDwDKg1kqI4oicWvewdP5hlHGUKqAN9uhQyqDcZ7hcqezOnJYLzD3-Efs8qf1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تیجی به نام لبه تیغ منتشر شد.
YouTube
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82014" target="_blank">📅 16:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82013" target="_blank">📅 15:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=r8KnvhoFFPj-BD0KoWa2R5zxkWNvsUoFxGsN3W0Nw_1YfdztBZ1l7bMvRZRic6lJnfHZrKxeGnwbc2S-M_EaQRX8Ar_w8fv4RvjNdJ5rhKg0pZti_pN8BJLFLtAMnc-5X4RN9PqGbiwjwVIkGjwWoaZ4yzbjnAEBCE-8jZ8EIquxeAZ617SHqDaEGDt0dJM6Iecnwx_93bWbH_qiSMi_UDUCBkuCaD4KAw2OxTUvxH0kpRHcnq0Fegh-RVX0lQHmm580NtM-cJidmIdB2iOW4ALzRMe_r-sFpZQXuFDlEZ0i2DCBhFyHbZTzxfH10T69ZHpxL2k8AAdaykQe8hZ1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=r8KnvhoFFPj-BD0KoWa2R5zxkWNvsUoFxGsN3W0Nw_1YfdztBZ1l7bMvRZRic6lJnfHZrKxeGnwbc2S-M_EaQRX8Ar_w8fv4RvjNdJ5rhKg0pZti_pN8BJLFLtAMnc-5X4RN9PqGbiwjwVIkGjwWoaZ4yzbjnAEBCE-8jZ8EIquxeAZ617SHqDaEGDt0dJM6Iecnwx_93bWbH_qiSMi_UDUCBkuCaD4KAw2OxTUvxH0kpRHcnq0Fegh-RVX0lQHmm580NtM-cJidmIdB2iOW4ALzRMe_r-sFpZQXuFDlEZ0i2DCBhFyHbZTzxfH10T69ZHpxL2k8AAdaykQe8hZ1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پهلوی و پوریا بشیری
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82012" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=FdD880b1eMfnFtEBYaqVdCLtLpCAAS7UAKDwyHAupQ721USH7veKQXY213EXvVtnSy3SxrFoP7m52nX_m-JBIrdXZlPCBmduaNr6x98Wq-evGpAeF2-3mGBMSiDqlcfqh-YBQjb_FyXtrzxIffPqeUVvo9YT4q6O2n47HZVpUdkLLRecfKGeScTxWMO9gM4FhgcIreyAGWXoGNf7pOYWAqr4nErAWE6VfuoA4qR2Q6xuaf3fDZXztyZ67A742p8iMm6jXrJCHI6DWLs1ouPKPmfixDqv98UIWnwONbQPBDo7LEKaVna7I0q2DAngcP1iHQsLth4z0e51yWwnW1EXvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=FdD880b1eMfnFtEBYaqVdCLtLpCAAS7UAKDwyHAupQ721USH7veKQXY213EXvVtnSy3SxrFoP7m52nX_m-JBIrdXZlPCBmduaNr6x98Wq-evGpAeF2-3mGBMSiDqlcfqh-YBQjb_FyXtrzxIffPqeUVvo9YT4q6O2n47HZVpUdkLLRecfKGeScTxWMO9gM4FhgcIreyAGWXoGNf7pOYWAqr4nErAWE6VfuoA4qR2Q6xuaf3fDZXztyZ67A742p8iMm6jXrJCHI6DWLs1ouPKPmfixDqv98UIWnwONbQPBDo7LEKaVna7I0q2DAngcP1iHQsLth4z0e51yWwnW1EXvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کشته‌شدن مداحِ سرکوبگر، حمیدرضا رجب‌زاده، این یارو با انتشار ویدیویی مردم رو تهدید کرده که اگه بازهم بیاید تو خیابون چنان تیکه‌تیکه‌تون میکنیم که پزشکی قانونی با کاردک جمعتون کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/82011" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جزئیات جدید از پرونده حمیدرضا رجب زاده:
به گفته رسانه ‌های داخلی؛ قلب حمیدرضا رجب زاده رو از بدنش درآوردن و مایع منی خودشون رو روی جسد این مداح ریختن و از تمام این لحظات فیلم گرفتند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82010" target="_blank">📅 14:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">محسن رضایی جای جلیلی رو تو شعام گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82009" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">جواد لالیگایی(نکونام) به تراکتور هیرویگو
@FunHipHop
| TaymazROMANO</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82008" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1jUOok1rSpl1_FgzxOpJHzG_YLVCjMDzDbH435wNzQ3SXMDN3drpx7nPSkAMocllha2a0w56O8LUY5AIp1c8T92Q7nlf8yCBK18S4gdLluF_CnYH7mFqOeqpoaUkk1Wm1I4W-eg_4O6IBeuftetV_fGmrWhwrJEcvvyAaMd9WW3Wl8AGuwlbaHucEP70pFyyom6AxsukKWvl-gKRwkbARSmRwKW5RO-1h0arTc5CEHRDX27QyFjdeH33IKn813fk93gQzL4zKqDdVKxSFyDgQ5vNUyhnFXZWF-quh5cDVhYaFc7wJlnuC9T0MlhKIe_-uYKlwoirrlYeZLOkyAqfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس سالام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/82007" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
وا
عراقچی: در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم، همش تبادل پیامه نه مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82006" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82005">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هنوز متتظرم تا انقلاب نشده آیسم نخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82005" target="_blank">📅 12:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82004">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oolKQK8e4_odvOvnv_dY3XvO-jdHHq29o4twJZ4Dgwllg-ZamSCZ5F2nuigiS7i_VUrDfUL2QkeRvvqEVsFWonjdUbKtptTkNMWNShmiENAomedzxaPVo4HL5dtzUjZa8OA_r_j0rdgQRvxgVy2QSN5tBpksWC17wyCkoWL9RP4hP-Q_-ymsVYV-lYcn6zDjYIFpOhz1pI-XLanYJF2HCKUdm6kXdPBo7xQG8fjOyhsV4eB2GNtve0JmlBTiihPK1mfsAlwfH7giofTBiqf-5esUZLHNhLpa_170rs438_qX_sgGMmwdmjVMIykowcuDhPO1wfSm-coqiT2pPp2GMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس Calvin Klein صاحب برند معروف لباس زیر به همین نام، کنارشم دوست پسرشه
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82004" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82003">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBoErxarR4EfGcrmW3NfmniPiNsy04lWH0W3r6nPBl-H-qRord7fBhYm6NLyPwzSPjukTCibRg0udWsX1TrQa9TXmUmRVrAB6_3Kt4iYCDdpMHaQrMlv8KT5P1egsObVHvMiyUDKmkz2xTqNFZDdLaHHTyIpZs7SYPXvhMbN9a9Cp9kvVohffUgQRDmL0zKLfFPc3am51OKVqTACfap5McQYxqUeEQvRWouJN_ZjIF2V7FMjwnBniMuSX2M_Zm5eLgB3wV947TJGwJidIaYs3GXGhZHROO2PdFW8cHU7jan-7rliyV8xro6lSJuKDdKcM6EpbSXk3W84zrbPR1FVQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82003" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lvPlM8PFNkkvWIpl29p9_OjGPKub0THDxZGf9gStOYACKFPMKzRsPPEEkBwfAiuqmsjGalx7h2ZEOlIwzjHIzvjZTrX7I5jDzVeEiABwkJ0hrrPw9YUic9orBcfi9kSA3VBA-H24lplmO8lNywWwqSAaJf4tCz2iH471G8igc5NZsRgACqfQ6Aor7yCkCrUCoYBHNmuw2vY5TaV_BPgbN5IIxVwGyv4ubgGF9A2CwYvLxWCgl254x_MQvQA0TBLPbx1QNRMqsX-YPPDrq6yYzfalvTMpeyNwSZN1UsS19qOVnsN7A-iQemucgeMzliJAVTLLkg2W0xIGKXmfPPnm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lvPlM8PFNkkvWIpl29p9_OjGPKub0THDxZGf9gStOYACKFPMKzRsPPEEkBwfAiuqmsjGalx7h2ZEOlIwzjHIzvjZTrX7I5jDzVeEiABwkJ0hrrPw9YUic9orBcfi9kSA3VBA-H24lplmO8lNywWwqSAaJf4tCz2iH471G8igc5NZsRgACqfQ6Aor7yCkCrUCoYBHNmuw2vY5TaV_BPgbN5IIxVwGyv4ubgGF9A2CwYvLxWCgl254x_MQvQA0TBLPbx1QNRMqsX-YPPDrq6yYzfalvTMpeyNwSZN1UsS19qOVnsN7A-iQemucgeMzliJAVTLLkg2W0xIGKXmfPPnm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد. عکس قهرمانان واقعی مردم همیشه بالاست؛ اما امثال هادی چوپان، جوری فراموش میشن که انگار هیچ‌وقت وجود نداشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82001" target="_blank">📅 10:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82000" target="_blank">📅 05:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81999" target="_blank">📅 05:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afCqrjbhkkbxDUm6Frqx2X0sgBd0eXUtng8LpqfOUgbDo2DCWmfd5wEVq_7zzYD4t8W3kW99LbMgOu6Trktt41WKSiPMyoJbul6MilJml1RkUNzUowf1E2ScdjZWrYTRYTDIDt-khXX36s8VJ1F-RRlfUb1Dod2z5388uJXb41GcWPDy3QUTQRUi57j4pOCsCyQK53vpfwN31LElyvlRY2asxlaKLSyTxHWjXhMMX2-u8q_Clj8KKsP2yqcxmFKlXQYBwl02IGFOvRh1-J-V4SQN1gYj5RfpssclXi5vIpcoIOMqNiX7XdlnNNiYMq_Z5xxczw64cC3hldIpCKNkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtpV918FrZ5uhjpjuGnEvb1p-FG8komFfzmNDaCsZ3JXBDOvnBgMPHz0tOpR_COxlTDICQqaUigtVOwdud30PnnisXb12GGDdJpWBvO64m7ONl-MbRm-ZOtTb7f5CgDucVP2lcsJ9MIgEnthJAUaPXacf0joQftAzZUvEMwIiMricbwdDPlNdjIhqaUnY-1gMR90w4hqfzzTjRmmldKG0ajAGye321qZbc37__tqnpZAL7Gk75PzJ4-ufQNdRj5nBQ8Y8Vw79WFeVfcqOswuqHa3AEjQCCMRovhiczXV4BGBNFCRTjI5f1Y4jqxddBef6BliW-R6uyusqrlxVwiUGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بر طبل شادانه بکوبید
جواد محجوب ملی پوش سابق جودو ایران که قهرمانی آسیا رو در کارنامه خودش داره با رکورد بدون باخت 0-5 به سازمان UFC پیوست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/81996" target="_blank">📅 02:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyQCsI_TARFRjKN8POp8jvUGS3xFSgjcH-hqTbm87-L2rMj1A4hSGushXDgbSs3GpkmYNJN8LTbvJwL_6VOqfoTxKYwMHYCphhz4Z8SMDTy0woQY-5JWiZaKWo5EIQaU8L3Pp6JXuOSfJOpU0QwzDyr1fvSGUDskak5yJ1309ONXwuD5FOe8FV4SIL2G8_LlQiGwmYmShWuCc3VT7GENzH9EjyQgOL1wzITlc758qo_SVv5qEL_BgXMhhZwh2A-wPhJEf6G6Cl1SHaU9BZ7JGODiV1DbPEW134HlszKWrqvabBn8hxpkpRAk7xO5yA25ZeQ9uQyIlHO4PBk0aoDktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کابوس و دیگرد به اسم انگ منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81994" target="_blank">📅 02:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81993">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMyg0wbL2yTc7W-babx755BstHg981MLrpc0zfKKAw537jlQCYlFaLsdQxNmSpcA9PGIbee3FFGUaIxvmjvvm3ESHFNG84I2v3MTOGWI5ZJaB2Hzw7KvpjIT__ddbJoxbGgkwOwMUf6Pj_z1Ci-u79t0vKQdrnbIXk40PUesa-6B1jDQaguPNwfPoS9Lp9598nJHVBFDv7cb4sKrM5LeUC0OPXYli-OXTMg-8L-o_NQhZREkSaEjEW-0J3GJFgExiObHdkdvW8KVcHplxC5pJLV0UAUCNY2bpZ2kpQW5G0JeiYEUl9OD7rieygfAjgAOjDoktg00UudQc6QnfHQ4bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اعضای سپاه پاسداران در شهر مهاباد با نام عمر دهقان در روستای «گاگش سفلی» از توابع این شهرستان کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81993" target="_blank">📅 00:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81991">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این کصکشی که چتارو پخش کرده چرا اسمشونو سیو نکرده مثل کصخلا تلاش نکنیم بفهمیم sha کیه z کیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81991" target="_blank">📅 23:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81990">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMDDiJcnsclxqLOa3kphgEQ6bvlbPu5kv5jDHnLjAinFMFQD77n42oGq7KPlVtmRQsfX9QlBgxZvFDjPCq2luJoKGq_hiA1qu2WfJR35QML6jeVWh-DrOnU1gwelg-_iq03dmwdUQW_jEduS2cB-3U_g2cgHxwVM3KuA0PTYPCKB4Kb1Ogsin9CeqTNGaOMd5rREcoYHuAE23kCStKD1bS8IyLeH0ggrJzI99JjjElBkPrxAuf_AIP01A9ySqr67_wP7lNpTSKwiw6Tj0l30wp1Z6mjrQFjvTJQW91ydEJt0OXTlA7WjMBG8xM5KeYOdDqfb0l0gxAeOjgH4ONsofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که پیشنهادمو دادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81990" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81989">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiWUoFAl1c-RbvdOtqUwu9YP8Eq26a0ug36zn3bMi5XUbyszGpabPp5T7BwtJIhXDR7wDtnJMOrZbDrEwGoBcaO02vVzJsEYRW4XmnfheW9fTWIwExD3kVwehuOVTJOSdYRhEvJU-CI4VTs3antvMSojqAHf3Y92ylILDSwGAUxAnUTPSotAU0WWRQYfe3usIlIG4uHUvO-qfr332Famvhs0hc38DVR95J-xGRWY1i4dgx4TG4_94rGqTAL9wlxjUoZkfSuk4CBRMrdHb68QSI45uRcXa1cRgqZ_cm5JUIxtUJ3fWE9hIvQ0NHdbEwYdTSflciiX7t8Bb2-ctesA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 کا اومد به لطف بیف با بشری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81989" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81988">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کار به هیچی ندارم ولی تا تلگرام هست سگ میره سیگنال کصکشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81988" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81987">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه مردی برای مراسم ختم خامنه ای از آلمان اومد ایران ولی موقع برگشتن نذاشتن برگرده چون کارت پایان خدمت سربازی نداشت.
مجبور شد سند یه ملک رو وثیقه بزاره تا خارج شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81987" target="_blank">📅 23:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81986">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLc0fLJMjua4cADnawmtvoSYdMPdp58bclIDUFa7QR2HTqHymMH8buRY9iMQzrRIMQ6x0szgRXo9c9oRv9Yv6dIgRobXOiDeLT_qLdza1pxRoUQ-78RKPgayYcXURvpqnGv2izEAicQ37PaiVYhahQO7YKs5LM7C9HVEgV1K_uK3SCfylPZ2Jn8kyG9cBh0E66xrC64_askJ5d15AqXo0d4JdESqonH_TXLJ888xMJrCN_WbjWyyK4cMifDlXevRyubHeMKJDHW058CqR0ohxUp6ujk1cHxZesYB6uH2u5yYk_nHDma6ZvBUyGWeKWltAinJ9hAHDDS8253szirQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81986" target="_blank">📅 22:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81985">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgOl5U37VUjKjyb0t1CQRBkTHVsi0QOQksb7h3imQk06CbMNEzC98k2YZHiE5MzY8gKS0Ewk-yzUEs1Hj8c3T48Ij0OniWSkp-sDmnf5g0by0rf7DCxsgxlPbMcGcKba5iLZSrcLCW_Cmjmintl2pwaKDTmVgGW0_fiKyKwbqbbYGsSUGtmS6Od-Lvy8U31C-nl0d4IDXQyNMi4R0lYJPysrnrObi81PBB-j4Tj1PAStYji8KHXaW5veZ40sJH-Q9BS_1J-EKzF8ExRfUyLiKrivVE9WJPDE2dKesxeHly4eaYJlB3wiP-p8yfDfngywkaNiPBphhmguCf-yC_w2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81985" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81984">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پوری تو ترک جدیدش یجا به مهدیار میگه رضا پهلوی رو انفالو کن صف تو با ما فرق داره
ما؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81984" target="_blank">📅 21:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81983">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این جمله که "فدایی موزیک داد جوون مردم و فرستاد زیر گلوله" همون اندازه کصشره که جمله "پهلوی فراخوان داد مردم رفتن بیرون مردن" کصشره، فدایی نبود مردم قرار بود بشینن تو خونه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81983" target="_blank">📅 21:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81982">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قدیم اینجا میگفتی کص ننه فدایی
خشتک رو می‌کشیدن سرت
الان چی</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81982" target="_blank">📅 21:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81981">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVX2InUjkVyqCFhoUaru3QarfiV5DIdjr-2fA3enn2gt1t6Q1W97OIyI0aL7aRztmEWELiCHV3BkEH6V8OTgdVgFhvcbGdumxUlWlYIVH2cX2Erzj171ufPZkA3hrTCZZcd4kpZ3QWYsljrGQBd9jfrIvBVtbZ0dwBHURfR0HbqRoPNFlkD4BzziFGEszjAYe6duV3q1Oyv6oE0QAmTretudQG3CcKm2Yzxy42qyOIC17Ko2B95XoQIufiHr7Xkzhe4y8eNO7Hljwvu-1Ycpny1WE0FyH-J2EiS2NcI_RqdUJWQm3Wkg2ikyNCK2H1wX49R73gFu2Pdb1Rh72lkBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی میگفتم کاگان چرا نظر نمیده، که اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81981" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81980">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اتاق اصناف کاشان اعلام کرد:
کاشت ناخن در کاشان ممنوع شد!
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81980" target="_blank">📅 21:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81979">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">جذاب مثل بیف آرتا و پوتک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81979" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنها سیاسی خونی که باقی مونده ویناکه فک کنم با این اوصاف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81977" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">من خودم تستش کردم
راضی بودم
👍
گفتم شاید به درد شما هم بخوره</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81976" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81973">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsBMc6dbwSbGg_DQriJHR30F_hB2kEJN6A-OKGQ7T9is0IUPghrJm6xINA_5bTdTwRfZ0_9lZosEi8XO3-9d7mGI-lmAw03FAFkUajZag2Lyon5Jq1WPKijWae9Kmo5NHJnNEMam_2jyZRFjTVnm8KDbPM_ONc8gEd_50YOB0H3sk1fJfwtL05h33BL9LoOzh1i2rKQyxVqqE_VhO_lc_CApBX73oKk61FBjV2l3Y0isnZP6fEbaAKYQDHYpFRntNOuKIOx4pLo1jjSu-MMv0tBwoy8AoFkzxsS5chSOkzV01cBORce9BedYfnMjVZjnaUcv8uML8QuM5JGnZSy0BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتشه بری دایرکتش آیدی دکی رو بدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81973" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mti4i5ABfLvNYtI6P1ADit6W66hA9kW_ST3hX52S4Wa0CLaFJm0rUV4wHXjK_ZWtcXeUjn4QZ04jbj59HUSgS46pxlHQbjAl34WF7b__FPFAK8kT7zM-RjWT2FjVRjyPZKWd0my3WcTgR9Ux6WS9PiPXg0653GiAXwXzpWiwDhIpp5-ENl62Qzv11UAObnfOG5JqKKMkDo2X9Crknqc1hm7f65N6_ZyZSK7VuB3SWBazN0DKQRCuE8rkXh38k8herViPzfMxEXRBoked7hxzizT8sruR0NHrd21uprFJa2eHOV_S4F1c4o0MYinKTLs9BpqfDVO7hnSltCxaGEQfrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پوری گفت جاوید شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81972" target="_blank">📅 19:24 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
