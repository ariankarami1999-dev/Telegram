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
<img src="https://cdn4.telesco.pe/file/CCWQH8JdQhBiELSG3Gt8eck_LSfys4AU2S6FDvPLF6mPK--70lCupGG8V5WPwPQQat7kMkR_UrhGR_AwFDixaVj-QpWdsJdXMsuip243LRcz-0_EWEQ-7iw5JwQpFdzUP9W2-EL_Lc-mVJUucRNOdWHNGm8_tlw--wn5sh6JDbIyLmbwe3ux7UrJrJ7g3i3or-D-GILtrDIMLPNCh4veEQyzX9AfY8PTOOYzrRW8jsRx6wmZob9o6I55CJs71FNu1wx55Ljcn4nUwu8s5SSgru85qusRgNxWNJOI42QdYXNxhEi3RYnPrB708v1k57E5-kYBSyrxTmnWc60FYdscIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 254K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 19:49:56</div>
<hr>

<div class="tg-post" id="msg-81403">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a94875ecfc.mp4?token=W6BKrXxrJca3Ynh0oBB0rxgY43SXNwDWY8FnXqpOtgdHFiNNObhpFeErIQfplGhewVS7wSdSGItIO2xUOy5Hjasp2WSqFu4mHWXHKnnM8I4loy8ikj1tP7nWmkOqPuR__vxWEwsk6IfpP24gzLQwE4_s5zI4E2ymKl6PfDUdD3XHzkHVG9E7NGonZtOtPNjd0mOySAZK2izgPA_iwLqELfFzYAx1uyIdprmKtPGb2Rg0wCuGZ2kuR6VHEgI466Zn7ijRk_XeHqgzI-9lZfIXrKn1wWCIatuv3pGvGDfSutbNgHfnFedmS3VMAr6pK4I0UaFYmB-IM11je7xUjLHykA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a94875ecfc.mp4?token=W6BKrXxrJca3Ynh0oBB0rxgY43SXNwDWY8FnXqpOtgdHFiNNObhpFeErIQfplGhewVS7wSdSGItIO2xUOy5Hjasp2WSqFu4mHWXHKnnM8I4loy8ikj1tP7nWmkOqPuR__vxWEwsk6IfpP24gzLQwE4_s5zI4E2ymKl6PfDUdD3XHzkHVG9E7NGonZtOtPNjd0mOySAZK2izgPA_iwLqELfFzYAx1uyIdprmKtPGb2Rg0wCuGZ2kuR6VHEgI466Zn7ijRk_XeHqgzI-9lZfIXrKn1wWCIatuv3pGvGDfSutbNgHfnFedmS3VMAr6pK4I0UaFYmB-IM11je7xUjLHykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول رئيس الوزراء الزيدي للنجف الأشرف</div>
<div class="tg-footer">👁️ 64 · <a href="https://t.me/naya_foriraq/81403" target="_blank">📅 19:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81402">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وصول رئيس الوزراء الزيدي للنجف الأشرف</div>
<div class="tg-footer">👁️ 550 · <a href="https://t.me/naya_foriraq/81402" target="_blank">📅 19:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اختناق فوق مونتي كارلو   تفهم ما تفهم مشكلتك</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/naya_foriraq/81399" target="_blank">📅 19:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">السيد الشهيد يغادر مع عائلته إلى النجف الأشرف.</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/naya_foriraq/81398" target="_blank">📅 19:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81501b3668.mp4?token=BOC8k9kG2ImL_3tS6HiBb0Ymi0QbJLozq8hFMKD3JYrZMdIDM3NitXClZsqzMhbIQ5kEOV1j0apn1JCcx091gwpnW10e1BI_S8xpbZ4c2vqstd6ZPaSkGV8v6vZy7cnA0B_vhpso5fYvDDKXndsSn9IyPW2koM_bi-P0jWt3eksHMQAlnj5DzEXmen-E_4pu5bp66vlUPvGvq_KfVLGTUiUZmkR3UukfblRxFyFRAEBFDGn_n9_vqF1rraBXWZCMx1BL4S1Mm-lf-GjNDYIUifTouSF2csBPSL0eHdAcnVYlnw5sxyc6aVxOB6Rr9ZwlHM1RFjOoPMeGLr6M2o3flw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81501b3668.mp4?token=BOC8k9kG2ImL_3tS6HiBb0Ymi0QbJLozq8hFMKD3JYrZMdIDM3NitXClZsqzMhbIQ5kEOV1j0apn1JCcx091gwpnW10e1BI_S8xpbZ4c2vqstd6ZPaSkGV8v6vZy7cnA0B_vhpso5fYvDDKXndsSn9IyPW2koM_bi-P0jWt3eksHMQAlnj5DzEXmen-E_4pu5bp66vlUPvGvq_KfVLGTUiUZmkR3UukfblRxFyFRAEBFDGn_n9_vqF1rraBXWZCMx1BL4S1Mm-lf-GjNDYIUifTouSF2csBPSL0eHdAcnVYlnw5sxyc6aVxOB6Rr9ZwlHM1RFjOoPMeGLr6M2o3flw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جحافل الحشد الشعبي الجهد الخدمي تزحف نحو التشيع في كربلاء والنجف الأشرف</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/naya_foriraq/81397" target="_blank">📅 19:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اختناق فوق مونتي كارلو
تفهم ما تفهم مشكلتك</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/naya_foriraq/81396" target="_blank">📅 19:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
انفجار لغم أرضي في بادية المثنى جنوب العراق ؛ مصرع شخص كحصيلة أولية</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/naya_foriraq/81395" target="_blank">📅 19:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SGw_MFqbJRGMibqq86wqhG-T78NAPyiRubORnBa2hYo2dairgVxEXR3HRJAUxcJQLvIeZGpU9QBJfTdoWsVjFTKpmRte5D7wiR1Ida_-G50Xl2CQ-HZ8Q3BH5y3ob2-KVLXUVWF04F09tczwm4FUDY6NbIEKfAVxJfszsxYhAw6EBJzY3YOaVzkVqEXE0ApZrj98yTfMCxK4GKJcStj5qqs65JNTc4jc5vpcQdiHKJqGmRjB_BKNGPF3UBcUN1_GofbhUon5DLkZXZGVpsdFENyKLX_7JfE5HYqeipr6QINmOpItctyZ9br2BZqTX_foF18xFs2p5IVIMDY6h-24Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5d_zZiznxZOHnHfACjfAaMdjrfQZUwpVNRnnAAguxg922CNxObQX6vTCqnw4qgnFaZcr3sz5zV6x4G1k_5A-EB6h5vrPtRxxuxf2lAj5sCkLaEIbxz3lcFSC6FEZDQRZ2AF7SwZXOqndVT5A90tdpqN-DjtzyjJOSe5f2NSzFOPFeREtuy6f8a3d-d9tpwR0mHHJ64cYfehhqO8_jE5rC8vCKT7YKU5E5LDPWZXEwrWPTbgy6iKm8EcFl1yXHxyrpwtImLUsWARADCScBORztepHzt5bLR82PGtmiULAQgdVdLU4BXqxOq77u02C_A236UXG48LrD3gdD6Q0qBMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYjbp5ohN3-VhKDO0N7u0GblZHfAbadqTLg5AHNInHi6L2ffOyDXy6N_oFHsJT42GFIxzTBuHjRpCUDISxvtq77MgXb5IUyTuyddZ-vCN6IaKLP-oh-m6KP2kvBzK4-RlBILE_TTSEdre9KfETiqk9waGMjy4QWdEBZUmQ3rQSOOn_3J8OW6AO1WWQ12IbN7UHo8UUwYoA8RFIZ_bC_FOZ-sLuvdESh8yY3l6oBTT92QbUFjVCPfEGggTos34HMJouqv9hnYpMfI9q9SRE0i5CkZXM8miaJD7Oxn4HXbdqecF_hqyizk5usrkSTnYViwyaRES5-IHu2vBNGONby1gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0WFaBoWMmqvvpLa_z7rt2m0L75fkodoN1dyDHqXvGEsSXqjudUCWGOP0mKgAoQIvu78K3kCkowg1iUnKbPsvDPYuV7m9nAyqlE1gVOqBKI5tOrVBrLpj82Lgi6Bp2W1OaAglOhcwJRo9byveNfcEAD-MbUWqtv4WNRUy59QFE2VyfjiONi9C4vhe6X1LdVavzoZdYbC3-KJP391A3x3GA77ePIjObmlXU7zUl7H3EvfckpJzMYVH4zGqz8U2V7xQpGGJFO62P36YMjeH2_xl2_2GBSvYOR2wwE3HNV8gBC9lLcwa9G2Dfq39IWO-UuDxA_nydS23ygfb6liqUSi5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tlretdsm1aGp2LvmMAkxtf4UMm671klvqxKaIAfBPBD2l3MMtMpuj-XjfutNDR7nu29mRbFhZ9vVrHzOjw0j_EhLxCpesvOkdFN-It7MTmJy_lmnmwmNTW3R9Wg3m8HcDqbYUFuVFj8I0BFEtlSiu6GbSZVtgASlNl4Tgn7WAXff5BQXMLfiEs1YtePcdiMJmzijRER3x2zmST9vHVtmTuDSdQFVq6XggoNYmjTvuqlFVMbhjlxlxL8q8qsvO520rEYr_egaDAwQ5HTcOCBL0_GvrIzbdO-p8fwSzNB8fm0hk_-CAFn1WOqj4nZS74drqPeYhbD-GEzqVcVfVh_rhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">أعلام صهيوني أوربي : شارك اربع صحفين أمريكان بتغطية جنازة الخامنئي اغلبهم مدعومين وهاربون في روسيا يحب القضاء عليهم</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/naya_foriraq/81390" target="_blank">📅 19:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b2d800e3.mp4?token=ofY2NjiNnPbyonqO3JCyX_AvxbyttdR5MJWOTEMJnAv-ITYlyov6fAMZFAeX6mSs4eIKcjuGj1MRoiPuCkEJkE62HVILJ7BRcMpB46keaENQmYrfpFxA5RH1EAwUszqg1ZRUodwQAuAOZ8O9BiXxp74PGd5_8SKN-j7QPSES62-Wddc_wNnYAG2Lisikeg1zb_uCRAdk8uPh9J_CSmO-YCpaei8AJ2geuhF4i6IuzZhD4bJvTKsxVtUfADI2n9j3OjOBuroVDyeAjOBqQw3W3Fa76n6QewAKPDt0Hd6PFn5zL7LcGrISpfhGxAxBMc3eYkeJN1xo1T6Ox5rS_tGBOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b2d800e3.mp4?token=ofY2NjiNnPbyonqO3JCyX_AvxbyttdR5MJWOTEMJnAv-ITYlyov6fAMZFAeX6mSs4eIKcjuGj1MRoiPuCkEJkE62HVILJ7BRcMpB46keaENQmYrfpFxA5RH1EAwUszqg1ZRUodwQAuAOZ8O9BiXxp74PGd5_8SKN-j7QPSES62-Wddc_wNnYAG2Lisikeg1zb_uCRAdk8uPh9J_CSmO-YCpaei8AJ2geuhF4i6IuzZhD4bJvTKsxVtUfADI2n9j3OjOBuroVDyeAjOBqQw3W3Fa76n6QewAKPDt0Hd6PFn5zL7LcGrISpfhGxAxBMc3eYkeJN1xo1T6Ox5rS_tGBOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطار النجف الأشرف خلال اللحظات الأخيرة قبول وصول جثمان الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/naya_foriraq/81389" target="_blank">📅 19:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f302a38eec.mp4?token=XbkxT1pFb6XrK4ZV74WHZeSKI9nJ0uKvvqmpGY0CT2pLZHa10UxDSvKOTd-kOrBQ86woOwSKESp5C4Gbzr5j9CKDbYIwt89vCg6OAPoePwiHw9o6G-IB-vFmcS8n_8JrUpGk7i-xYlaPvORIuGc_nz3sz9SiUNKIIwQ3iG9CL9d81PK8_uhkdxijUwk9lijqxs6AM4Bf3B43uRtIkoe0hz9jtvZKuTqWGCvzU6uYH7VQDWrQkoGEqgB9__tlaHP389HtZYeHVApfRRBLTXsm_RImWOkm9lenmaHxsvUGkZQ2V75AocDXpP_Yu1KKURBIftqsyGPHZSebRSIQC1gHmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f302a38eec.mp4?token=XbkxT1pFb6XrK4ZV74WHZeSKI9nJ0uKvvqmpGY0CT2pLZHa10UxDSvKOTd-kOrBQ86woOwSKESp5C4Gbzr5j9CKDbYIwt89vCg6OAPoePwiHw9o6G-IB-vFmcS8n_8JrUpGk7i-xYlaPvORIuGc_nz3sz9SiUNKIIwQ3iG9CL9d81PK8_uhkdxijUwk9lijqxs6AM4Bf3B43uRtIkoe0hz9jtvZKuTqWGCvzU6uYH7VQDWrQkoGEqgB9__tlaHP389HtZYeHVApfRRBLTXsm_RImWOkm9lenmaHxsvUGkZQ2V75AocDXpP_Yu1KKURBIftqsyGPHZSebRSIQC1gHmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجثمان الطاهر لقائد الثورة يغادر الى النجف الاشرف برفقة وفد ايراني رفيع المستوى يقوده الرئيس الايراني مسعود بزشكيان</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/naya_foriraq/81388" target="_blank">📅 19:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5bd2fe9d.mp4?token=kptsrcbgihL8XalhTohbVRCbIQvfPOoEheVQ458Jt2E5VOcB2qV7ZEqohh9lUMINAJVkdi-Dt5ZSx59fG2Qf3MnNn_zvx_A2k6wQnTn8PSLdD3NITTcpLOsymh8-8_KgvmlwbPbyKqAaoKyvd8BdVXB2_kqSrjD23e6FLta3oFPyPeXsx86c-ctpDXKuVyp7H8hWBlvtvrBpHtDzBNGHGav15C2kri7iTKu9gKcHsuWdh2QP40j3__zSAWFj4o30HSNKZpdyErt8wxINkI_LH3l4Sgx2Jm4CwFh44aXcFnENcHwsLQ0_l6_qHTWZ7G6m30htnuQYqPAtZqKkvkMorlPCyB0Ka7MXnUqFkLqbp20EDobFk6H9AwmkbCBYpO4O4-_aoq7zk6kUQoGPV0cIxDIeogrHUeG2h0t1blRkg6pDDO9IfQauxvItlvWHH1P4oltZIM8GnMNS5KWVx31xzk8-IJ1lvPhBCaTU9ocyng_kR4cuYeZGENk8lnHi3i3KbEOFDlwYOCFEItgkB4HvTGadNWX1fJXMhGhSn6l-7sdoi7ps6F_nJgoY2IK3WOZZIG4aIcVl9lz5-_OuEd2LhY7Hy92szALBDhsXj_j1jRogOF8-wmTgkM4ljpyLs0yTorHrepT_uzKt8hKImQLvVqTeZm0F5siOmcS0SHzKf3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5bd2fe9d.mp4?token=kptsrcbgihL8XalhTohbVRCbIQvfPOoEheVQ458Jt2E5VOcB2qV7ZEqohh9lUMINAJVkdi-Dt5ZSx59fG2Qf3MnNn_zvx_A2k6wQnTn8PSLdD3NITTcpLOsymh8-8_KgvmlwbPbyKqAaoKyvd8BdVXB2_kqSrjD23e6FLta3oFPyPeXsx86c-ctpDXKuVyp7H8hWBlvtvrBpHtDzBNGHGav15C2kri7iTKu9gKcHsuWdh2QP40j3__zSAWFj4o30HSNKZpdyErt8wxINkI_LH3l4Sgx2Jm4CwFh44aXcFnENcHwsLQ0_l6_qHTWZ7G6m30htnuQYqPAtZqKkvkMorlPCyB0Ka7MXnUqFkLqbp20EDobFk6H9AwmkbCBYpO4O4-_aoq7zk6kUQoGPV0cIxDIeogrHUeG2h0t1blRkg6pDDO9IfQauxvItlvWHH1P4oltZIM8GnMNS5KWVx31xzk8-IJ1lvPhBCaTU9ocyng_kR4cuYeZGENk8lnHi3i3KbEOFDlwYOCFEItgkB4HvTGadNWX1fJXMhGhSn6l-7sdoi7ps6F_nJgoY2IK3WOZZIG4aIcVl9lz5-_OuEd2LhY7Hy92szALBDhsXj_j1jRogOF8-wmTgkM4ljpyLs0yTorHrepT_uzKt8hKImQLvVqTeZm0F5siOmcS0SHzKf3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انتشار واسع لقطعات الحشد الشعبي استعدادًا لمراسيم تشييع الشهيد آية الله السيد علي الخامنئي في محافظة النجف الأشرف.</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/81387" target="_blank">📅 19:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5VNmBVpK6xUJ3CX8G8uoD7iiBvEcvAWE-Lx8M1wi0S5pGTP2qEbYfENxg6M--xSXLYvq6thZpl_UJvQsDeuJZx2SV1p7chzTx_F0xfg0i2h-BiyKIpYHvybYAND-hKsNRFPoHVTmVNXJMCIMjKn0YALLkpSVWQwnit8-gHRyF4dgRDuy0KpzUbJ15bUZ745_tUexQRs5fgOdwe_DF4V6pGS46zyqxq9W0uY0lQeMhNVSh5Jr2g9lLDePVTSbRFo0rzXLxCgFwQ5mWxAWT58JvJQRTFa4ouj70reyDAvJDQo58riUSmlP5u08icefjs_mWQ4-7eJTg8EJ1NnoZKC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز مدينة حلب السورية</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/naya_foriraq/81386" target="_blank">📅 19:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
الحشد الشعبي يباشر بتفويج المشيعين والمعزين إلى محافظتي النجف الاشرف وكربلاء المقدسة للمشاركة في مراسم تشييع جثمان آية الله العظمى المرجع الديني السيد علي الخامنئي (قدس سره الشريف).</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/naya_foriraq/81385" target="_blank">📅 18:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هيئة عمليات التجارة البحرية البريطانية: تلقينا بلاغا عن حادثة جديدة تتعلق بناقلة نفط في مضيق هرمز</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/naya_foriraq/81384" target="_blank">📅 18:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81381">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e78EhVB5OcRLfYUDOKI6o6G2VvOacb0O8RA0fAhw4feUSzQh6-hicfTOhotHpDHSVEXPQ-6MGR2m1SNayMuVCNu8M818r82Sco6654aEga9e-EPFSomUCScB_VJeZMkrZl78m0z6GV74ShSoFZqBd0N5K_idLmJPZ2Yplbu5IT12fMIQyJFuQQqVy-_pV14jNrNiBT6f94EJgNF4X3mBJ5MrjS1hc8yXtbTijyUO2hiNy3LIOCQ9KBY9suw6mWW903WpSSDeGxFSTyAmYNkz2bGkOJV7jnN-knmrxGrPmhx-LD8MxNV2DbHGEoJTxdYSEcu21-C9HmZ52dGlayZ4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMkSx-frD3DlaFFwkta1e2WOq2TuvgLQBRVJa5wiyKmp60ZBTUuemvbyzkLlxIHPeX8c6q8YvLE-fHPuhoDwZg06ofzIkMKFQaZn3_fucX698obecwLEmMSyMlz8rr4FmasWOJQDqQMOAfjhoGJVBw3BbcUszfoa7LExgVgpLnne4hDthdXMMYQkhLOQ4grHo7Hq_oJeFHTDvzPlNkS0LUhWbdAX-lmPKvHrUuTpv9vXsnggxuhdnMF7ExiT9jDJ0V9FyfQiI4Aq-pYWNBtKL0ojEpQYJtYRlPaFFP5Doam8SMz_KA-2ULDs__EuQgUK7BQ0D7NvkRJFr8Q0NDdV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anilszGjNVeZ-Ii478yI65VcsBVwSVx70EJ_pIoAD77CDVp0ZO_xHzYe-AxDNRxjl4P_1iky1Hbpb5qVhduB5cmRrIIiKFuKVkvvP1RlM-TR3Vl22N4jXWfM1NGMzU1AssiyjJ_k1pbL500ecNb41oJRpvxHPguvv1nFEqHVu0trKxDHE0VSnDxUwHQXmsUpPcjRZKVW2jSasF_Uiy5Ft1B2ionty6W2MErmRph2QgDPf1rXvMTgnYR_C4ptu6xo-Prc-zXXA8WiHVayKZxlTokADd0FRxecvi5PF5lG5AsNXwFKkCI-v5dEvYUCYrNFNI5jgFyMfnPOUiwkGQ5yKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
شوارع غزة تمتلأ بعبارات تصف شهيد القدس السيد على الخامنئي.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/naya_foriraq/81381" target="_blank">📅 18:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81380">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be17933fd.mp4?token=A0Hsf-cqZ7JjkLtUYCsexOA05JTJyAqRddi4dt8sjo_-_AvYbnHS67oKAK-kauCAnTCxnD59Q-ofFJ0HDQxpmc-ntxYbj0_WFDHx_2Rkil5hu23ZI9BinO2bfaQFYGzWvPiw6TonG2e9xv5Ih0gacoS82_7af99Udl972i9UTjqPER8hTIJ3r5XRp9w4DLYqSh92EOCAos-j6edTb2AoK_S2MSDqBC3r3tsqDCYTZC_FvnpzmZHb8_WIBS3EqRRpZOHkg3u-ZxlyI6xyaH3yzVAcShu-ixkjLzmWksgwyxq1rWDMla4XI0Z7xG9aQzTGqoF1MNXFG1lKmd9rObYywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be17933fd.mp4?token=A0Hsf-cqZ7JjkLtUYCsexOA05JTJyAqRddi4dt8sjo_-_AvYbnHS67oKAK-kauCAnTCxnD59Q-ofFJ0HDQxpmc-ntxYbj0_WFDHx_2Rkil5hu23ZI9BinO2bfaQFYGzWvPiw6TonG2e9xv5Ih0gacoS82_7af99Udl972i9UTjqPER8hTIJ3r5XRp9w4DLYqSh92EOCAos-j6edTb2AoK_S2MSDqBC3r3tsqDCYTZC_FvnpzmZHb8_WIBS3EqRRpZOHkg3u-ZxlyI6xyaH3yzVAcShu-ixkjLzmWksgwyxq1rWDMla4XI0Z7xG9aQzTGqoF1MNXFG1lKmd9rObYywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أهالي الناصرية يشدون رحالهم متجهين إلى محافظتي النجف وكربلاء المقدسة لتلبية النداء والمشاركة في تشييع الولي الشهيد.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/naya_foriraq/81380" target="_blank">📅 18:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81379">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/036c96ce36.mp4?token=ATVhsFXW8D3QF2Lqgi4S0AJYhwLQcpw3d1E-4_HJ1sIoog5Uv-ctbynImSMFYCRTR0QOkYAI_9pntQ1UIH8zemCzQTIuFoosB03QJrAWas82hbQBh58QP_tM_gr1ED8Hap5T1Mr-mNN8p2lYlCovOkbcq9jG8CfP1S-ewpm6-JhIhM4oYi4r0dS_L-j1sElbhTU174VZPruLw-_YP0XFzZFpd-8thKJj_MG48J9bhde6IohrBbtybbr2Yruub8g4AeG3_L83FjWHeSdsRxgGTSJFwHvPFKivh2dyaCtGZnDkgDgbA05QtoeGK9-9FpofC8n7CBSaAJFYEJdLLssM0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/036c96ce36.mp4?token=ATVhsFXW8D3QF2Lqgi4S0AJYhwLQcpw3d1E-4_HJ1sIoog5Uv-ctbynImSMFYCRTR0QOkYAI_9pntQ1UIH8zemCzQTIuFoosB03QJrAWas82hbQBh58QP_tM_gr1ED8Hap5T1Mr-mNN8p2lYlCovOkbcq9jG8CfP1S-ewpm6-JhIhM4oYi4r0dS_L-j1sElbhTU174VZPruLw-_YP0XFzZFpd-8thKJj_MG48J9bhde6IohrBbtybbr2Yruub8g4AeG3_L83FjWHeSdsRxgGTSJFwHvPFKivh2dyaCtGZnDkgDgbA05QtoeGK9-9FpofC8n7CBSaAJFYEJdLLssM0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قوات الحشد الشعبي تنتشر على طرقات مسار التشييع لتنظيم المراسم في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/naya_foriraq/81379" target="_blank">📅 18:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81378">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔻
إعلام إيراني: تقديرات تشير إلى مشاركة ملايين الأشخاص في تشييع تاريخي للسيد الشهيد خامنئي في محافظتي النجف وكربلاء العراقيتين.</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/naya_foriraq/81378" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bu7PpNjYdQYnud_V3EDCXLoQVzm2OxiquxiAdO6POTcw6OdvxfAEuqRZEsE1g7hmmyyln_dCRjuFgmEJjUB3HFeha2bsI__LV-YUn-NMgN8LdanOa-cFefzdK9n0OwnP4Pvxu6rZRdm__Fs8WN2qKMLtriv4NmquKTZc7DGjsar4PlUpDiw-UmY-0IRvvhe3UaYyehASyB3BLymM__RC5UbWi0y5JgwvgUBquB0cgN1fk1SkpuNUQXh252-UNWZuLF_c8qZU-QxCSvBc-N6l5b20vSkshGSG0sIRLAqOazF4_D65nLX0xIze41aRXDns3AV85UYVnAHW2HPSdDb5Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Guwokqx-D31oyMkWk_zK-b4oq5Kbwx4ZMP_TrrMJkfs4QvWxlIL48fqa4e6icUhEhk6e6ClboqMcHyIb8tvU72zQ3L6drAAE8kDijNNzAwgM6yZH8eH_s5u4v4qhFtA1loC74b-dGRLbf9wqeatJMOzDg5JeZ2oT9IIFwSrXfDd94JFxvXKr5N3Tb4cypKTK1vGUhGt5pHYg623q9E5JTaaTIoMOHflMukI0u9JteZ5wl0lfhk453y6AcMkoWGsTtZzn428fwl6VQVWo03KCmHytUYGZwLJxm0TdPJToCWf_B-lxZUAPx8XcGYqJ68OdM3aZCseKYLfd_8sFHFYTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibpMmVaQexxa3l6wp_Coy3_xcr_LCROcfmWzCbIr08c1A2g3gGFX1n0YeMCNG-yKVZ29oq21Zjxbs8LtmLBwc7KRRfTk6vPVuC6J2Fc1aUZMqQUcZZASYmHKj26c9XB7H_htWyD5UIwiLSFnbzDRl50kgVHMXl8AtBvSgKRXQKC3pcsS_uOJlEFD35B1EXgP5WA8aeAyWzVth9aHUfb6g1IdlaEI1aCwVJDYsy5cjhyAGizySu-jT6ZzhKrQxky_IIE4WrawykINDME3BjI9P9i0QdQ-VCr5YmFtFTI6yhfl48125M8GnvRJqiorHgGGJq0pfxkf1HCo4cSK_WDnyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
قوات الحشد الشعبي تبدأ بالانتشار على طريق مطار النجف الاشرف الدولي بما يسهم في تأمين مراسم التشييع وتنظيم حركة المشاركين.</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/naya_foriraq/81375" target="_blank">📅 18:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd6QsD4rALmuskDAWqaeIUEXtjGbRn9vUDv-IzAJwFLDukLUSSE6iHlNwOSMmsUPioTk2BXcBIXuw9CAhj4etct78wueeJsv-NXx0L0zIJ7FaqqBtzvXw-VReR3lEGheqqmf4GxC5hNreCR9G7ofi8vtdIY-Bt6rS1DX42KUjU3OrJoLMRbilVhk05I3LDNH9uES-gbGSwmRzXPNLoDzSuuz1cAzO3zKXdIlypaGT8Mo1QecNp_wlgA0zRPrDSnwaihUCYzSRRy9Vov14rCaGMwKBz8IxSaNtEB968pTpTLbNSW_yFfCYEl0eUDNEz1teVoMEoo1g6GeLEndJbPP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اللجنة العليا لمراسم تشييع الجثمان الطاهر للشهيد القائد السيد الخامنئي (رضوان الله عليه) تعقد مؤتمرين في النجف الاشرف وكربلاء المقدسة لوضع اللمسات الأخيرة والتنسيق النهائي لهذه المناسبة
​
عقدت اللجنة العليا المعنية بتنظيم مراسم تشييع جثمان الشهيد القائد السيد الخامنئي (رضوان الله تعالى عليه) مؤتمرين منفصلين؛ الأول في محافظة النجف الأشرف، والآخر في محافظة كربلاء المقدسة.
​ناقش خلالهما ،الدكتور إحسان العوادي، والفريق أول الركن الدكتور قيس المحمداوي، نائب قائد العمليات المشتركة
اللمسات الأخيرة الخاصة بهذه المناسبة في هاتين المحافظتين والتنسيق النهائي لها.
​وشهد الاجتماعان إيجازاً من القادة الأمنيين والجهات المعنية؛ بهدف إحكام النهايات المتعلقة بالخطط المرسومة، وتوزيع المهام والمسؤوليات بالشكل الأمثل على جميع القادة.
​وتم التأكيد على أهمية تكامل الخطط الأمنية والتنسيقية والخدمية بما يتلاءم مع مكانة العراق .
​كما جرى بحث التفاصيل المتعلقة بالتوقيتات، والمراسم، وأماكن التشييع في محافظتي النجف الأشرف وكربلاء المقدسة.
​وأكدت اللجنة من خلال جملة من التوصيات على تطبيق جميع الإجراءات والتوجيهات التنظيمية، ومسارات النعش الطاهر، وآليات توافد المعزين، بما يضمن انسيابية المراسم التي تليق بهذه المناسبة الأليمة.
٠٠٠٠٠
اللجنة الإعلامية لمراسم تشييع جثمان الشهيد المعظم السيد علي الخامنئي رضوان الله تعالى عليه.
7 تموز 2026</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/naya_foriraq/81374" target="_blank">📅 18:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏اللجنة الأولمبية الدولية تعلن إعادة روسيا إلى الألعاب الأولمبية بعد ان خرطت الوضعية واصبح التدخل السياسي في الرياضة محط سخرية لجميع العالم بسبب ترامب</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/naya_foriraq/81373" target="_blank">📅 18:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouTJHfSSabC7xxBs21inNfgnTsDMRzZNQbZ6pO579m8eztmnSYGjSrQlSYMnj2PtgzCkVHnt7JWlmUQ9ZVy4qPyolBuNa_ITK2kCYbp6_JWhdPnrbjlZpKf-vTdqKQjdkNRURMpKwsf0LE7OwAD-D_4-Gbp-ETTPClubnHEUeaEB5-XzvpXbCHIuyKE8d0Rzwf5GdJiY9IBxQ0_k_8CT6h0wjmmRzKnBa7PNMdTQyJRF7ObS_VANOhiHQbcsx_W5O1JrjQndHDlEZm41XklLvgv1YvYSXhBs3MOkZX9MrLW_nA6ngkZL4B6XrJKqdLuxrvhxaaqSVOLztokXh4l2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتفاع اسعار النفط على خلفية الاحداث في مضيق هرمز</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/81372" target="_blank">📅 18:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇾🇪
نائب رئيس الوزراء اليمني لشؤون الدفاع والأمن:
لسنا عاجزين في اليمن عن الاستمرار لـ10 سنوات أخرى في المواجهة العسكرية إنما نبحث عن إقامة الحجة، رابع المستحيلات هو أن يقبل الشعب اليمني باستمرار حالة اللاحرب واللاسلم وقد ضاق ذرعاً بهذا الوضع.</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/naya_foriraq/81371" target="_blank">📅 18:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f639792de.mp4?token=UkZm1GOt9oC7wFnOw0ihrJLobMjVut4mNG7xWSGqf83NBVNz58bBFLjfQeSbuB1yibdGFFGX2toCZbCPIB2lyWxypGhIIGYhechelyFZS69_f-rldkOYSSggB5NmIBo931COliwGg4YC_E-a9OGiA-M_Hz70D95KwhXb6cutPVzehyvmIfRwH7xhAA2JBYKGGENP5CfVmFB-fBshaI9Vof6GQi6M5Od_XYig9MJeQblyAHb9JQXDQ8hZe9rFTZxdqKuvzymwOrIxt0zOTUn88U_z0I_yd4wLucmLknMgEblU9eyiQjXezbTxx48IK8cqBIwf3a6AA4TwScHyoI9U5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f639792de.mp4?token=UkZm1GOt9oC7wFnOw0ihrJLobMjVut4mNG7xWSGqf83NBVNz58bBFLjfQeSbuB1yibdGFFGX2toCZbCPIB2lyWxypGhIIGYhechelyFZS69_f-rldkOYSSggB5NmIBo931COliwGg4YC_E-a9OGiA-M_Hz70D95KwhXb6cutPVzehyvmIfRwH7xhAA2JBYKGGENP5CfVmFB-fBshaI9Vof6GQi6M5Od_XYig9MJeQblyAHb9JQXDQ8hZe9rFTZxdqKuvzymwOrIxt0zOTUn88U_z0I_yd4wLucmLknMgEblU9eyiQjXezbTxx48IK8cqBIwf3a6AA4TwScHyoI9U5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد للنعش الذي سيتشرف بحمل جثمان القائد الشهيد للثورة الاسلامية السيد علي الحسيني الخامنئي في العراق</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/naya_foriraq/81370" target="_blank">📅 17:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81369">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هبوط طائرة ايرانية جديدة في مطار صنعاء الدولي لكسر الحصار عن المطار</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/naya_foriraq/81369" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81368">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLxI1ioUqEXUW2dkLHwq514csvEB5fKstxiKKCZA2X486HWop5Crfggg2CikhF1-n5iQlUBSMKNaE3dzpy8qJtYlvF4CdXHhKsbNAI2jm6EfkTnezFoae0jDF92LZIkQO3qNm1rUSlLpvV6SwLe-Eo16Yn18A1wwDRoek7bk3U9-4cohX6vvkjuz8LZQxZS9l0FFRxpzaZ_vM3EkRehR6pbHjnnWCK7eblHm2IfVzYDiQaTrfTm1OUqqbSOb5P3GJ8VVuCQ9jh_3ffRj9TsE_s-HHEt4Rc2X01F0OdpvxynkCnEFb8IO7rJSu7s0wPDaWKl9yg2H4MQrFx4DQ9sLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📅
برنامج تشييع الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكية) في العراق
▪️
#قوموا_لله
#تشييع_إمام_المستضعفين</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/naya_foriraq/81368" target="_blank">📅 17:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81367">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ايران تعطل الدوام الرسمي في محافظة ايلام الحدودية مع العراق لاتاحة الفرصة للمواطنين للمشاركة في تشييع قائد الثورة الشهيد بمحافظتي كربلاء والنجف المقدستين.</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/naya_foriraq/81367" target="_blank">📅 17:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
المتحدث باسم الخارجية الإيرانية إسماعيل بقائي:
القانون الدولي الإنساني قُتل خلال الحرب المفروضة على إيران، إذا كان الأوروبيون مدافعين حقاً عن القانون الدولي وحقوق الإنسان فما كان ينبغي لهم أن يقفوا متفرجين أمام الظلم.</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/81366" target="_blank">📅 17:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHB8fJeCJEPJrqdmeAvad_jItcQ6wHs4-mp3x_OQRHKX49bwjQcapK963HCnAMFjT8nP5LAoKEnjXeL_ZaA8BP2S50uRtxfkIuWXFd5gZv-JWGl14hTcpiWjf4tnKqdDUcIJ_HUSaj8agjSuN4pPyVAGm_JQO_dpFanPSZmFI9amnNgpICxDTgNI3SWh3IrxIv8OYgVz91jjwNvtpgx1jnNpTFU_s4Qct2e-gPxYGRSYKl4X-WxY5xJNUr_98CNa3kcCobpaatc_MGH48oZxT5YgrzO6wZMMECbgTwEKgcDPPkkNJEBr197XnLXOe2dCfG3kHONKxnzhrm_4nHkpuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">في أرضِ عليٍّ… يقيمُ علمٌ، ويُشيَّعُ إليها علمٌ،
خوش امديد سيد شهيد علي جانم فداى رهبر</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/naya_foriraq/81365" target="_blank">📅 17:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81363">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HM5KLthtCCGteTlt3QpvmCRK0xzGhgY86dgHE0Dj5f4VN-xEOrimz9SB_ZZAbExEyCvJmHB8jhlzkN8V2qdksDarOZzyNFy3UnYnEgWNc-5DH2UvqMom5b8IMD2JEtahMUnNhu1c7oqczj8TVK_XyI7EqSjpsKO_oEUgIpRP43lbiF_0xvrR5ynVf-KL64iaXm1VwozcD32wsvGH8k6PPzQNJNDaAp5u7YzkLjLXE3m-W-B3qAYiDMYgrD7D2oqjq-bsegIjBnPqg-G_lTtbsOB_dT-VFLvy-GI3e1gmQ6B8SbyY_E_JRkSVYxB5YNAms6wuUDbsU4CqFd5uOyHj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFPTEvcwBQ-ZYquX3Fqkeo69iOoTHaxx7X_x-tl5BOcdlJgNXSpKIEtDapFYw_BMUUCIhF1SLvzgdfX8mHcVNo5lxcPYHLYXXN1y4mh4ffDoBASARBjxS2F95lna3WYi3nAFTTJoK7r1H8vVFn6oELKuEdVLns2Y0mn81avBEnuETNR7mp_OHVgNlckNKldF9WVikuWS1Fr1HuSwisPyxsTbA8Jj59idoGBMZRxGHOvJyISF9c6hxegsbP9BhFuLbhqCbrv1RcT3BH2V5CY5eTUIbbDsUw-vzTkJ2pfwzvECBpdjrKKRbJiL1idtodoI-YMkLbjXB6TF9kkOXeXIfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
مطار النجف الاشرف الدولي يستعد لاستقبال القائد الشهيد للثورة الاسلامية.</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/naya_foriraq/81363" target="_blank">📅 17:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">العراق يدين تفجيرات دمشق</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/naya_foriraq/81361" target="_blank">📅 17:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
🇺🇸
اعلام العدو:
هل نشهد اليوم هجومًا أمريكيًا في جنوب إيران ردًا على إطلاق ايران النار على الناقلات في مضيق هرمز؟</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/naya_foriraq/81360" target="_blank">📅 17:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81359">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حدث امني جديد في مضيق هرمز</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/naya_foriraq/81359" target="_blank">📅 17:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSp_MJ8np7_1tDZS3QGPwkYDEcSaTAeN8f85GsUr1scHECPaSBYMcKVktF5tFlOFz4zh6vR4XpEfxM8gsx_Q6dLrYZEJSd4v7YGww8hQAOHDx-HNRyJbpGdyJA3dAmtdH-fudAnfcKA2sd2j_2sV4rWE53gtEmDeiFoMAsZvB7ymgWST5q_9z13vo8LJipmB1dLyYzPkSkhL81SA4RSM6Cvf1XLnVHo86Zo5ox8_Y9VWDrB6ZYX41pmt6sm-inbl0EDydXk5Tq3eD71XyQ-A_PB1P1MJwa37bn5RSyF-ee2jWBUUYRl9zl6yZC1eZEka_FY82HVodG6liM4PmPkppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني جديد في مضيق هرمز</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/naya_foriraq/81358" target="_blank">📅 17:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
قامت سفن تابعة للبحرية التركية مؤخرًا بالاقتراب من منطقة تدريبات كانت يجريها سلاح البحر الإسرائيلي في البحر الأبيض المتوسط، مما أدى إلى تعطيل التدريب ونتيجة لهذا الاقتراب، اضطرت السفن الإسرائيلية إلى تغيير مسارها.</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/naya_foriraq/81357" target="_blank">📅 17:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قوة امنية من بغداد تحاصر مبنى بلدية ناحية نفر في محافظة الديوانية جنوبي العراق وتلقي القبض على ثلاثة موظفين فيها</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/naya_foriraq/81356" target="_blank">📅 17:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81355">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
🇮🇶
اعداد ضخمة من شيعة امير المؤمنين (ع) في محافظة البصرة تنطلق صوب المدينتين المقدستين للمشاركة في مراسم تشييع القائد الشهيد للثورة الاسلامية</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/naya_foriraq/81355" target="_blank">📅 17:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqwxi_vArlEHGHHP86zb_dachJiiVxrE8NZKw70YCq3W-tjMtFkg0w52QyLCJ7LW-gYeNMF8FSb4mpg0K-AEm_onRgXUA9PjEwJP4wQBt0qj2utp3dZS4prPbsDIDi_OFNk2NgeFPv9NU4WfGOIEt_EtPMS_4JZdoexC28ZbDUqxa4FNjcB2-fymFXvsKE1GMkKXe_yznDHeb0eIYud2becJQ2zNwE_YQtSKRT2YFLeQjzvrSGVM3ikl3Q9q4vns_T4UmwEmeCdw6Ir252pAixF3U9ZZFUirUQbYaeOsapCoOybGPyPUwb8FIBTVfGtrOBQ8yEZMZPvc4ZaKg6zeOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جثمان قائد الثورة الشهيد يطوف حرم السيدة فاطمة المعصومة (ع) في قم بواسطة الطائرة قبيل توجهه الى العراق</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/naya_foriraq/81354" target="_blank">📅 17:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇶
النائب احمد الشرماني:
العراق يمر بمرحلة صعبة ويواجه وضعاً مالياً عصيباً، إذ لا تتجاوز الكتلة النقدية المتاحة حالياً نصف تريليون دينار، فيما تُقدَّر المبالغ اللازمة لتغطية رواتب موظفي الدولة شهرياً بنحو 8 تريليونات دينار.</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/81353" target="_blank">📅 17:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81351">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">زعيم الدروز في لبنان وليد جنبلاط:
اتفاق الإطار الثلاثي أحادي أملته إسرائيل على فريق لبناني في الخارج والداخل.</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/naya_foriraq/81351" target="_blank">📅 17:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حدث امني في مضيق هرمز</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/naya_foriraq/81350" target="_blank">📅 16:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6Jcl3QTWdORRsViDUd0DWPo6oq35eYIqFckXx8EA32NDUJfLJcm6NnGIEYZ2rpAm6TchZNquNPvgsikCwYFwOF1586AWg7WCG73EjWEwtgP8hh9LbnYWv31KaJZ7qs9y_GS_vhdoKwh4yM7SBtp49M9McPc2D1nLrXWpdf35Ag-vqoI7ET9J-tnNDuYAyyrmVP4VCntDTmNLQlrrIradA692nkS4yz0R_5ROWbdMkYBORAFX06bZow6ADhNlan8zdy3DLVoM3fYPVv2TGo9ngQbxWpPm4-u-d3eO2l5jKQpmktFnGXMG1Day-0YxyY3WmOWF4aC-K2k33B6xOLucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث امني في مضيق هرمز</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/naya_foriraq/81349" target="_blank">📅 16:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏ترامب: بفضل اردوغان، تربطنا علاقة جيدة جداً مع الجولاني. لقد وافقت عليه مع الرئيس اردوغان. كنا نحن الاثنين اللذين رغبنا به بشدة</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/naya_foriraq/81348" target="_blank">📅 16:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏ترامب: يجب أن تكون غرينلاند تحت سيطرة الولايات المتحدة وليس الدنمارك</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/naya_foriraq/81347" target="_blank">📅 16:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامب: ‌‏لقد كانت تركيا حليفاً عظيماً لنا. ‏كان بإمكانهم الدخول في المعركة من الجانب الآخر. إنهم أقوياء للغاية، لكنهم لم يفعلوا ذلك. ‏ربما لم يفعلوا ذلك بسببي.</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/naya_foriraq/81346" target="_blank">📅 16:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaSqzGCq_sVpKfeS5C7zYVCMMRrqOhsaUyG1U_h3cDE2LvzVPK5ZEJdxRupuDxwNhY-2Ygjq_h-v7Brir0B4mM4Mg_SYr2a1lyM54-rVx-n7Qg66Y5Ru-tmM84w-noxLx0gl5iF_Xy0We2wS7Bpb7K17_SX-duNUDHKG9e2U7LsIAF1-rFWT5DQbzcgyvHJV6P9lkDwuMp7d7Q1cMTHZ7o1_qNM2IOnW5OwgFLPkB4Jxo0RHRwAU-yaGbznVwjIgyDD69xF-V-4bhjaZi5uv27u3E6PcwDW5HfcK_lO5AfrYOlASeNqq8wItLs0-A66OB9w3X-FJ141Qjdvgdc9xxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eMG2RfyNEFJdQGpdm5M2c5mC-8ggT8lO0oBh7WF-LATZeR3IvaxTKEJrIVQTrjon8bKJaJ9I2xfDJXCSloTRelZBYFGR8jKzA1Hq1a4zgJGmVDIPppk3X2KdpgTZyfMDWEU9Xhs_P1H3TN3oJGtzs3KFrTzfzP7MiaP8BQPDAwHI2PdQiTZc-4dbuHrb_Z8Fos0PSbjikXgQhhlUExpcfZ0DUqsHSaHxGOw5xGAvMVNas-hn2shR9ZJzx2yYsy2Ew0jGfRcxae0Ony29BzpJUM0JXZBcO9bPa4MPInvvgUyQ3nVcIyoDLXu1DM93XFuwZxXLumtg90QM7YD1Lc9MjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxSIZDwC8gTOOWg70W6TUvfX4mBJ8MGQszV3AoZUL73Gyr1-sdYpzRnep3S8cQD5wYswebYiqUYGV43DOTowo1KTu2AVSfhXhtgZscZLkdHdbsmOPufZbfEc9XHXsFx8ebF2GFtdrIvaw2B_ekjftj57_Z8_eOeYMFcXl2uKztjBUbZT610V7BcXWcXmz1ufcCwPJcyEnR4oUW69poWEKguoL54juw0pj8LoXNJaG19NOJd2Kg40l2xeNPzk5-ekUF-UHb-WGLkxskQMqhogDZTv5RakJtGS4lrkcv6LAzYUwY2tURgIt2hWQ-d5An58bBKNv0HvrsyobzkbcOk-kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
الحشد الشعبي:
المديرية العامة للأمن والانضباط في هيئة الحشد الشعبي، تشارك بالتأمين والنقل والحماية للجثمان الطاهر للسيد علي الحسيني الخامنئي في أثناء تشييعه في محافظتي النجف وكربلاء المقدستين.</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/naya_foriraq/81343" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامب: تركيا لم تنخرط بالحرب في إيران بفضلي وهي لا تريد أن ترى إيران تحصل على سلاح نووي</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/naya_foriraq/81342" target="_blank">📅 16:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامب: ليس لدي مخاوف من أي نوع بسبب حصول تركيا على مقاتلات إف 35</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/naya_foriraq/81341" target="_blank">📅 16:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‏المراسل: هناك مخاوف بشأن أنظمة الدفاع الصاروخي الروسية في تركيا. هل لديك هذه المخاوف؟  ‏ترامب: ليس لدي أي مخاوف بشأن أي شيء.</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/naya_foriraq/81340" target="_blank">📅 16:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1c72a82d4.mp4?token=RnAYCoNPvJNUvU21x0JoMWmb5NgI2f3JyvwVVLaIRjHsiOXRJSIoRl0Gl5KTT1xTM0IOzAM9FYMKuGaS9H3vpoe35BuluK7RfCk_IbSXsDFiDcvNwLLJcS7_9eJdkjfTGehhaYMO2ZDpQAIfrnJKYntRM6aKxIWo8ouFKtC89vFbzUUhGvgvReimP2Hs_2ini2G1pggTFVRnbZEDv9VdwUgN51zkgOIoYPVdOWjHMpPDNYcXJ1c6GjW-InGkgrvV5Uh8u-Uj6faVobf84h13enF-nxn73dTC8MzUlTAe0YX4lpNrlusi-1GjxrP_e6D1SyNiGxfztEUM3tfKQpGGN76p8uI2dn1ct90ZS676jkOiYosH9yVcqwj8Z3fDtM1ttNvd-lMyL8Ve3WXIax6Zt_vi5QOPKPLAkMt985NfenaECIstezINv2NlwIFDWragDFnCKAXHZJ8gh7X6-XA8yugIEAe6QNGqGZoGm3rmlUef_RpwBvYd6iHFoE8IdHdcOvumaysdvYMiL1nqP0TsIAs9-Z0c5lIzjqCeLhitj9DGGuzcFTtDGHq_n_awG0CcVn8upg2U7HUO7-e6QCSxYnAOPKq2suigLwj07niVpQqMuZJnaWOaVyFcMkZ86ug8dtQ2A2LfBAXDHVbD4gd1t2REYChWDa9TAdnz-UgBGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1c72a82d4.mp4?token=RnAYCoNPvJNUvU21x0JoMWmb5NgI2f3JyvwVVLaIRjHsiOXRJSIoRl0Gl5KTT1xTM0IOzAM9FYMKuGaS9H3vpoe35BuluK7RfCk_IbSXsDFiDcvNwLLJcS7_9eJdkjfTGehhaYMO2ZDpQAIfrnJKYntRM6aKxIWo8ouFKtC89vFbzUUhGvgvReimP2Hs_2ini2G1pggTFVRnbZEDv9VdwUgN51zkgOIoYPVdOWjHMpPDNYcXJ1c6GjW-InGkgrvV5Uh8u-Uj6faVobf84h13enF-nxn73dTC8MzUlTAe0YX4lpNrlusi-1GjxrP_e6D1SyNiGxfztEUM3tfKQpGGN76p8uI2dn1ct90ZS676jkOiYosH9yVcqwj8Z3fDtM1ttNvd-lMyL8Ve3WXIax6Zt_vi5QOPKPLAkMt985NfenaECIstezINv2NlwIFDWragDFnCKAXHZJ8gh7X6-XA8yugIEAe6QNGqGZoGm3rmlUef_RpwBvYd6iHFoE8IdHdcOvumaysdvYMiL1nqP0TsIAs9-Z0c5lIzjqCeLhitj9DGGuzcFTtDGHq_n_awG0CcVn8upg2U7HUO7-e6QCSxYnAOPKq2suigLwj07niVpQqMuZJnaWOaVyFcMkZ86ug8dtQ2A2LfBAXDHVbD4gd1t2REYChWDa9TAdnz-UgBGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
الجولاني: التحقيقات مستمرة ‏بخصوص انفجارات اليوم في دمشق.</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/81339" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇸🇾
الجولاني:
التحقيقات مستمرة ‏بخصوص انفجارات اليوم في دمشق.</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/naya_foriraq/81338" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏المراسل: هل من المحتمل إجراء المزيد من عمليات سحب القوات في أوروبا؟  ‏ترامب: سنرى. لقد شعرت بخيبة أمل كبيرة من حلف الناتو. وبصراحة، لو لم يُعقد الاجتماع في تركيا حيث يتمتع صديقي بزعامة قوية، لكان من المحتمل ألا أحضر.</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/naya_foriraq/81337" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">أردوغان: لقد وعدنا ترامب بخمس مقاتلات</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/naya_foriraq/81336" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بعد طلب نتن ياهو.. ترامب: سنتخذ قراراً بشأن منح تركيا طائرات إف-35</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/81335" target="_blank">📅 16:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بعد طلب نتن ياهو.. ترامب: سنتخذ قراراً بشأن منح تركيا طائرات إف-35</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/naya_foriraq/81334" target="_blank">📅 16:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">تعطيل الدوام الرسمي في عموم العراق يوم غد الأربعاء تزامنا مع تشييع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/naya_foriraq/81333" target="_blank">📅 16:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بعد طلب نتن ياهو..
ترامب: سنتخذ قراراً بشأن منح تركيا طائرات إف-35</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/naya_foriraq/81332" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81331">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🌟
وزير الصحة اللبناني:
الدعم العراقي أسهم في صمود القطاع الصحي خلال الأزمات.</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/81331" target="_blank">📅 16:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81330">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📰
رويترز: اندلاع حريق في غرفة محركات ناقلة الغاز الطبيعي المسال القطرية "الريكات" التي تعرضت لهجوم والناقلة معرضة للانفجار.</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/naya_foriraq/81330" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81329">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/877d5b9907.mp4?token=AVlAG6-YPSZUNlu4kmYClbf5UL0aE2HMGHiV4IQDhID5naXRDe8MT_1auLo2cxY86Oi9L-q15Xph0k8a4dqM6WFnI--7JMjuLfr9kOqvjIvDhVFcWb9WVmkzaptEa5Z3t3R19ghGAiNlsxWWHjeSmdw3biAv8Qs7JJx0RqigPPGgfT4uB4mimezWIoLp4zuCraHShN7sUowltsr0olL_TGZdHEFsfxLwRsIXXRqhNwGL5tEffj11EHCY0MaLkRPM6qidbbVE-U3X4d4D5Eh0qW1xOZivId4TB7V1BVDidyZvsFGtH61MGA2C20nao54EW6JvamKBWJB5DY7i1thP6WRXlOC2cuDKZIysQzpLFMtbXg5NUxL-Ue8S5jInecR6au8CiRvmgKHf7E7FP7R6htB7TCU4cufS35Ciqa6dGsso45T7O5IV2DObtE3-vVYq4bS6XotOZvzFKWf6_5vw6ChlvypTaQQ-XG2T335UqSRiQGZ35IlRGEXJsNpV4KBEeQ5IvN1NxfpFf94jsA4kheqBZ5pcECZh3hQv6L3HGRE6akkAiJap7RANUC6h85oZJ2FYyMTCkGR1uTDtsRfsfPuPEAGLQJ_W4YcxmoKmahWeFi8vYRVehUoeM6raXF_OIklutX_4PzPlqH4bhXpD4isbpEoJYFYl2s0QEK4EOQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/877d5b9907.mp4?token=AVlAG6-YPSZUNlu4kmYClbf5UL0aE2HMGHiV4IQDhID5naXRDe8MT_1auLo2cxY86Oi9L-q15Xph0k8a4dqM6WFnI--7JMjuLfr9kOqvjIvDhVFcWb9WVmkzaptEa5Z3t3R19ghGAiNlsxWWHjeSmdw3biAv8Qs7JJx0RqigPPGgfT4uB4mimezWIoLp4zuCraHShN7sUowltsr0olL_TGZdHEFsfxLwRsIXXRqhNwGL5tEffj11EHCY0MaLkRPM6qidbbVE-U3X4d4D5Eh0qW1xOZivId4TB7V1BVDidyZvsFGtH61MGA2C20nao54EW6JvamKBWJB5DY7i1thP6WRXlOC2cuDKZIysQzpLFMtbXg5NUxL-Ue8S5jInecR6au8CiRvmgKHf7E7FP7R6htB7TCU4cufS35Ciqa6dGsso45T7O5IV2DObtE3-vVYq4bS6XotOZvzFKWf6_5vw6ChlvypTaQQ-XG2T335UqSRiQGZ35IlRGEXJsNpV4KBEeQ5IvN1NxfpFf94jsA4kheqBZ5pcECZh3hQv6L3HGRE6akkAiJap7RANUC6h85oZJ2FYyMTCkGR1uTDtsRfsfPuPEAGLQJ_W4YcxmoKmahWeFi8vYRVehUoeM6raXF_OIklutX_4PzPlqH4bhXpD4isbpEoJYFYl2s0QEK4EOQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اندلاع حريق كبير بالقرب من سيطرة شهيد سبهان في مدينة الموصل شمالي العراق</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/naya_foriraq/81329" target="_blank">📅 16:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81328">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🌟
هيئة النزاهة العراقية:
السجن (10) سنوات لموظف في وزارة النفط اختلس مبلغاً قدره (١,١٧٤,٢٨٧,٠٠٠) مليار دينارٍ في محافظة نينوى.</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/naya_foriraq/81328" target="_blank">📅 15:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaTMfAPNhPD2K4EJO3MAtxRU7-SiFdeMjKx97Ed834Xxi9EtMP4O-xrED0yFkSEDB0ruuK6DLAq8EOfeb5Uy7kx1o5-_P31H1bV1-7M1fe29LtJlY-gr5MspWNML5EJWoM9mQvEGDuwMotIYdiZkog4NxtPDY_i22-xl-MRxXmORFraTmnJ7_Z0_e2ngebDpuxGDnmaySuqiBepVpZRH32oZ5JL4lqy5c16hqk6n-lCXnDC-d123XGlS-guVYc0qXHkHm9IOvuUxolS8PGA0K75NdsLDuTBwDcVshZs-Ib9myBDgaJz7wgUKDntxq_5ES0vwIisuQS9OKluRcjqLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
‏
ترامب:
تويوتا تنتقل من المكسيك إلى الولايات المتحدة. التعريفات الجمركية هي السبب!</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/naya_foriraq/81327" target="_blank">📅 15:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
قسم الشعائر والزيارات المليونية في ديوان محافظة النجف الأشرف:
عدد المواكب والحسينيات التي فتحت أبوابها لخدمة المعزين والمشيعين بلغ 487 موكبا وحسينية، توزعت بواقع 351  موكبا ثابتا على امتداد طريق سير النعش في شارع كوفة – النجف وصولا الى مرقد الامام أمير المؤمنين عليه السلام، إلى جانب 123 حسينية منتشرة في الأحياء السكنية في خط سير التشييع خُصصت لمبيت الزائرين واستراحتهم.</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/81326" target="_blank">📅 15:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbxbOBr10bIOdqMGEac4YMxaGweKrwTg3p0qeWifMXsudunKi6zXCJ0nxHI3qlVU7-a-0fizL2Kz5jp9us7rIUv__JdgZ5JsWEHVW9WJsjLBdH2lJg1J2JIFzsqrOSIfKMh3MPs57s4M2ndtd0Hmj70ebwvtPCWak7mAEPzQySYQdlsyPVE23eknKrNDW5qzaeWYkhs9VmjkTMZH4C0awxRRTXk18URaS1DcrzAVaGdJdO60ewYHgyqONKNkj9yo2rqo9pPVPmexIwBqHEE-Bi86gOEd70GBACckdeRqch4OtdbnWRkDe74bLNt86vUlobfi9EcQKicvuUjZc16HCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفير إيران لدى موسكو: "كان آية الله خامنئي يعتبر الأدب الروسي ذروة الأدب العالمي. وقد استشهد مرارًا وتكرارًا بروائع دوستويفسكي وتولستوي وتشيكوف، موضحًا أسباب شعبية هؤلاء الكتاب في إيران. يكمن الجواب في روحنا المشتركة: قضايا أخلاقية عميقة، ورغبة في العدالة، وجوانب روحية متعددة، ورؤية تجمع بين المعاناة والإيمان بالله."</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/81325" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
🇮🇷
مكتب ممثلية منظمة الحج والزيارة وشؤون الزائرين الإيرانيين في العراق:
- الشعب الإيراني يتقدم بالشكر إلى حكومة العراق وشعبه لما قدموه من خدمات وتسهيلات لمراسيم ستليق بالشهيد السيد علي الخامنئي
- الإيرانيين لا يشعرون بأنهم في بلد آخر، بل يشعرون أنهم في إيران، لأن الشعبين العراقي والإيراني شعب واحد، وإن الأخوة والمحبة الموجودة بينهما ليست جديدة، بل تمتد الى زمن طويل
- جميع الخدمات والتسهيلات التي قدمها العراقيون تستحق الشكر والتقدير، سواء من جانب الحكومة العراقية أو العشائر الكريمة التي بادرت إلى نصب المواكب وتقديم الخدمات للمعزين والزوار
- الأعداد الموجودة حالياً من الزوار الإيرانيين داخل العراق تقدر بحوالي 100 ألف زائر، يتوزعون بين النجف الأشرف وكربلاء المقدسة
- نحو 100 موكب إيراني موجودة حالياً بين المحافظتين تقدم خدمات الدعم اللوجستي إلى جانب إخوانهم في الحشد الشعبي والعشائر والجهات الحكومية
- الحكومة العراقية لم تقصر في تقديم الدعم والتنسيق، وأن جميع الإجراءات والتنسيقات موجودة عبر المنافذ الحدودية والعلاقات العامة والجهات المعنية، بما يسهل حركة الزوار الإيرانيين
- نتوقع أن يتجاوز عدد الزوار حاجز الـ100 ألف، وقد يصل إلى 120 ألف زائر أو أكثر، وهذه الأرقام تبقى تقديرية لأنها قابلة للزيادة، خصوصاً بعد إقامة تشييع جثمان الشهيد السيد علي الخامنئي في العراق
- الأعداد النهائية للزوار ستظهر بشكل أوضح خلال الأيام المقبلة، مع بدء توافد أعداد أكبر من الزوار الإيرانيين عبر المنافذ الحدودية
- نجدد شكرنا للحكومة العراقية ومجالس المحافظات وأعضاء مجلس النواب وجميع الجهات الحكومية والشعبية على الخدمات التي قدموها، هذه الجهود ستسهم في إقامة مراسيم تليق بمكانة الشهيد السيد الخامنئي</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/naya_foriraq/81324" target="_blank">📅 15:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81323">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇸🇾
عصابات الجولاني:
هدف العبوة سياسي وليس امني.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/81323" target="_blank">📅 15:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📰
رويترز:
اندلاع حريق في غرفة محركات ناقلة الغاز الطبيعي المسال القطرية "الريكات" التي تعرضت لهجوم والناقلة معرضة للانفجار.</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/81322" target="_blank">📅 15:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">العتبة الحسينية تعلن استكمال استعداداتها لاستقبال موكب تشييع الشهيد السيد الخامنئي (قدس سره) داخل مرقد الامام الحسين (ع)</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81321" target="_blank">📅 14:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇶
‏العراق يرفع إنتاج النفط من حقلي غرب القرنة 1 والرميلة إلى طاقتهما الإنتاجية الكاملة.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81319" target="_blank">📅 14:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gt1bOvl4Tkq5NkMJKqlg0J_g6rf2GZXN45e4haqT-OpaSXa2_6GHJN3d3vgHg10HL1KbsnMWbrvvQ0WK-0IUUN5RSACy5g_EkItSiKRc8SMKL-XJjWVKN5BXjZxlrAFCQBwahIiE8T-0wXrkZqvBurQyo4eNf7GsWegyVkpNNJNXFGNOQjSNQDmwYAwzI3YqA1dp1QZIL9ZcfvTXXvRPN1cHd2ny4cu3ZaVi3FvklQrX-ck6qsNiiNtXrnSSOctBNdPlr3itNVDERXWntifCnK8elmpzKp2-jnNciz2SIFi_LstKOg-KHla45jDOL3rsTCdQuHbLG3QBYVFg0CPqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y9xVXQ3xLFzy8fjXSNVpajmKYnpfKXrp_c9gqlvV9rYDmMZ0Xltk0JmnVmWPDoFZGAHfCFmINjL0kERJgzgaRB0uYIYO4zdnBBnDAWEC3nqyB92urbu38jBGj4GJvuXK9Af35P7fupq4lFHQt3UlPQPyitht6QC3Rt7_LrZHg3CXgnh9Rm0w6is0aIAeiw54J98fnzh_ikp3UGERSMS7L9GHPmRWB2WN1AzN3D6stl_jRXy35vy1RRRMIUvyKzZBxsOqTprj6ZHBlMuL2fVOvHcILcCbBbhZH03Tm3PlYp3pL8DVKxbDIQb5CLerp4LZ35ryQBSCqgz3S91LsIyDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6EHHeEwhQNoIwHznEyoNYwIaWanuOqj4no8imXouggOiDn-U6HZ6nuh3ur6zyOGq58FnfIy95SFaVGUG72lgxrcflEQNq5wYWirYF3hko1PxyD2BS6pNuyOjhnG7oxq_KbN6d0B25H723tjwPfvhrclMDHJUwVSlyFiSZOLBMqq1F8o6w-iux-Osmpz70Vgz0Rr0zb4cGg3V2TkTxZRoLvg29qoItpTPDrLDESWYh6YtrgudPuaXbz8N_QR8zGFFUj-iQ04FbCRekNPfPLiWN9eRp0nCkmkwvrBpxD1saoA-OR5qjwnQUJAax4PpECOoMMtIoRAFgswYdjk0g3S7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
رئيس أركان هيئة الحشد الشعبي يترأس اجتماعا موسعا في كربلاء المقدسة لبحث آخر الاستعدادات الخاصة بمراسم تشييع السيد الشهيد الخامنئي
ترأس رئيس أركان هيئة الحشد الشعبي السيد عبد العزيز المحمداوي اجتماع موسع عُقد في مقر قيادة عمليات كربلاء المقدسة للجيش، إلى جانب مدير مكتب رئيس مجلس الوزراء ونائب قائد العمليات المشتركة، وبحضور عدد من القيادات الأمنية والعسكرية، لبحث آخر الاستعدادات المتعلقة بمراسم تشييع جثمان اية الله العظمى السيد الشهيد علي الخامنئي (قدس سره).
وشهد الاجتماع مناقشة الخطط الأمنية والتنظيمية الخاصة بالمراسم، وآليات التنسيق بين مختلف الأجهزة الأمنية والعسكرية، بما يضمن انسيابية تنفيذ الواجبات الموكلة إليها، والحفاظ على الأمن والنظام العام خلال فترة التشييع.
وأكد المشاركون أهمية توحيد الجهود وتكامل الأدوار بين جميع الجهات المعنية، ومواصلة الاستعدادات الميدانية واللوجستية لإنجاح مراسم التشييع وفق الخطط المرسومة، وبما يحقق أعلى درجات الأمن والتنظيم.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81316" target="_blank">📅 14:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">جيش الاحتلال التركي يسيطر على قمة جبل غارا الواقع شمال شرق محافظة دهوك في اقليم كردستان العراق بعد قيام حزب العمال الكردستاني باخلائها وتسليمها سلميا لجيش الاحتلال التركي</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81315" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-mQqvAwXDD-kEFziOnILLdONhy_UGtE8bwF4IYGVvSIV48x8BZwNUbT6T2k5N7MNkGjy2d3MoiV1QTABUYXHwacxThon23K4u_RTKRBbaAh6gHZHlTDw6XlcLM4-cEK9_q1oOrOT4Vi6ivZPaKurPpmdwV4egoSQmHwcCXvOJY1gwGukrt3_Fh1f1Z8ykq1nlP6U9fbqtNoaYb0QkyF0WMvLcUBiAXpzx0N5id2BcYlOUqh-vTzC0qVYcDL4G8_IENOv0QvYRQkTSBQtFRt9KRdjAT7VK3TXc-KBZqXOaYPdtGKmF7_hlhwsQUpn31dDfjS3nv8-AnFwCmxpraepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
تستمر إيران بتجنيد الشعب العراقي لصناعة جواسيس جدد مقابل مبالغ مالية من 25 الف إلى نصف مليون دولار واكيد حبباااااا بالعرائق.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81314" target="_blank">📅 13:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5KqtxQpvLRE3z_U7RupOWsZ57jgaTWexFJtCcNsNHuOhEQxyfXzPhUgGsOcYjOA-tIkyKrTZkHDX4gzccwtiT8seGj1-IVXe5KJa6Po22A6gv-SQO0b-GemPrC5tAZFiIZ_2tgnKlQIkAY46g7jqDrZjxtTD0uizNfR6jvnXBNLQLx6lCxhQYW8A7D5SrwYgj8S3bVZILto1WnPn8hp5UfhPPkE38l65WEVOt_Y-SBZ_sS_Ojz94PSnmgicaXm6PsUBRCso0czEwBXKuP3Nm2Ok9Mr3NcGVk_VGvgYh15cJl4w2C94XtDlrCp50e_1HXfA0qofTAyGr9-R-JMmf_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس اللواء "إسماعيل قاآني":
المطالبة بتشييع جثمان قائد الثورة الإسلامية الشهيد، والتخطيط المكثف لهذا الحدث التاريخي من قبل الحكومة والشعب العراقي، يظهر لجميع العالم عمق الروابط الروحية بين الأمتين العظيمتين، العراق وإيران.
دعم سماحة القائد الأعلى للشهيد للشعب العراقي الكبير، ومشاركة المرجعية الدينية الموقرة، أدى إلى خوض الشهيد سليماني معركة إلى جانب الشباب العراقي الشجاع ضد تنظيم داعش وأمريكا المعتدية، حتى ارتكب ترامب الجريمة بقتل البطل الذي يمثل الأمتين، إلى جانب القائد الأعلى لحشد الشعب، أبو مهدي المهندس.
تشييع جثمان الإمام الشهيد في العراق، على غرار تشييع جثمان الشهيدين سليماني وأبو مهدي، سيعزز تماسك قبضة الأمتين في مواجهة الفتن الأمريكية، ويسلط الضوء على خط الدم الذي يربط بينهما.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81313" target="_blank">📅 13:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba2f00bb9a.mp4?token=rvoPmQeKgI2kfwWKPjHO5H7Y6CdRp2XPxETKqLSH4uvrg5kfyDlMUlhm6OcbZgOqpkr8NPVYhsYOl1AcCrR2f-6shPLUt43x9KAjxGT2SiJPJJU7xZauScxoI4Q6s6J648wSvb0KagaCBEZF2ZoF-WS2zmi_QpNuM6F5oUijoQpJhJoCZobmk08SUOTmbwnBvCX_DGZDg7RgA1scgSBuPErdMzOCjswL1J2OjUQKhSFP49F_Lt_fh1WSOp_EKkfRTTYOPPXQRlY7GJUXMIDSCgG2GE9u83FRdYHd5iS0pDzh3mUk5_9HomKc5FsD1gllA4dyOcnvy3XHy0J6WtwnVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba2f00bb9a.mp4?token=rvoPmQeKgI2kfwWKPjHO5H7Y6CdRp2XPxETKqLSH4uvrg5kfyDlMUlhm6OcbZgOqpkr8NPVYhsYOl1AcCrR2f-6shPLUt43x9KAjxGT2SiJPJJU7xZauScxoI4Q6s6J648wSvb0KagaCBEZF2ZoF-WS2zmi_QpNuM6F5oUijoQpJhJoCZobmk08SUOTmbwnBvCX_DGZDg7RgA1scgSBuPErdMzOCjswL1J2OjUQKhSFP49F_Lt_fh1WSOp_EKkfRTTYOPPXQRlY7GJUXMIDSCgG2GE9u83FRdYHd5iS0pDzh3mUk5_9HomKc5FsD1gllA4dyOcnvy3XHy0J6WtwnVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
انفجار مجهول بالقرب من سجن “الكم الصيني” في مدينة الشدادي جنوب محافظة الحسكة السورية.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81312" target="_blank">📅 13:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
🇮🇶
التلفزيون الإيراني: سيصل جثمان القائد الشهيد إلى العراق اليوم، وسيُشيع غدًا ابتداءً من الساعة 6 صباحًا في النجف الأشرف، وفي فترة ما بعد الظهر بمحافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81311" target="_blank">📅 12:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
سيل بشري كبير يحيط بالجثامين الطاهرة خلال مراسيم التشييع التي انطلقت من مسجد جمكران وصولاً إلى حرم السيدة المعصومة (عليها السلام) بمدينة قم المقدسة.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81310" target="_blank">📅 12:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81309">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8966c8cc3.mp4?token=e_sRDRJLpOsNE9YCVe6CBILaK4Q9fCKKifYgtdpUXJepp4pdKk-jGEM5GaLoW-NXby-iBbKrjOgT2HxO92hh64UuMdXX2Hj5H3XOxEfelkkBeVAInm8MjYU5ZQ3Og_IZMXvjmz0ZbePsMSDXTG1Kl_dpH5JHI1a4FE9nD21Vg2DQtiKJI3vplZ3Lbuk7FdYQDvbH-BGCyNgHNYEh48SzzF2_GpckvXAJE_e9zTYRK6jW3NMCy15ZMwcgbXkdAZmRYNj8-mKWQt4vzDduQPNIfm3pKb9rA_ocwd24JQ0ltt-MoUPsXpCWoxLDFbL1BOoswtSbzQJfN8HNZuewiqo8nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8966c8cc3.mp4?token=e_sRDRJLpOsNE9YCVe6CBILaK4Q9fCKKifYgtdpUXJepp4pdKk-jGEM5GaLoW-NXby-iBbKrjOgT2HxO92hh64UuMdXX2Hj5H3XOxEfelkkBeVAInm8MjYU5ZQ3Og_IZMXvjmz0ZbePsMSDXTG1Kl_dpH5JHI1a4FE9nD21Vg2DQtiKJI3vplZ3Lbuk7FdYQDvbH-BGCyNgHNYEh48SzzF2_GpckvXAJE_e9zTYRK6jW3NMCy15ZMwcgbXkdAZmRYNj8-mKWQt4vzDduQPNIfm3pKb9rA_ocwd24JQ0ltt-MoUPsXpCWoxLDFbL1BOoswtSbzQJfN8HNZuewiqo8nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 قتلى و 18 إصابة من عناصر الجولاني بينهم معاون وزير السياحة "فرج القشقوش" جراء عدة تفجيرات طالت العاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81309" target="_blank">📅 12:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">4 قتلى من عناصر الجولاني كحصيلة أولية</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81308" target="_blank">📅 11:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adbe2b156b.mp4?token=MmfegoGc-mQXb90mft44NrfMrAH2795YyiJFj6SWKGn9vIfNriwG_fkuYanN2zkNfa4ihrWxHO1ug6-j5lEFrMkB181-9H1rxfBjYcvtxzrX0eQQ9RUNSebvyR22y1XvbV8jxCN8zST-88gtiD6Mx8HDHlEd0RftknQfRhLoXZTPuBCyy4mb_lQHxzAUZjUt7Z7HPmCtyXUzPTN5fgHQs00KZK9oNOQ8iz104UPqTNGaYzg5MeSy40krKgFER5oI8WmFuJv1PM5J9ngJiuPyvF97btj_RxFA-cKjj1sl2EJ-h7YiPDXYq64NuVsKSaGajJwqHHXyixjAafG8imL35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adbe2b156b.mp4?token=MmfegoGc-mQXb90mft44NrfMrAH2795YyiJFj6SWKGn9vIfNriwG_fkuYanN2zkNfa4ihrWxHO1ug6-j5lEFrMkB181-9H1rxfBjYcvtxzrX0eQQ9RUNSebvyR22y1XvbV8jxCN8zST-88gtiD6Mx8HDHlEd0RftknQfRhLoXZTPuBCyy4mb_lQHxzAUZjUt7Z7HPmCtyXUzPTN5fgHQs00KZK9oNOQ8iz104UPqTNGaYzg5MeSy40krKgFER5oI8WmFuJv1PM5J9ngJiuPyvF97btj_RxFA-cKjj1sl2EJ-h7YiPDXYq64NuVsKSaGajJwqHHXyixjAafG8imL35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق يظهر مرور موكب الرئيس الفرنسي ماكرون بالقرب من مكان الإنفجار في العاصمة السورية دمشق قبل حدوثه بدقائق.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81307" target="_blank">📅 11:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ced0fc60cf.mp4?token=VbD-FWZ6DuinPzOaBpDK4Wc-eEsexu5IYNoaYjP84ujTpPaCs7AtfQPCmBxk8IMwi4v57iMm8XIIcVMnTCOrj9jkDaU9FIg8LsJwyeu0FSXln4Nohk8fl7IegensPVEKJyO0MoRer8OMazkqn6ZV4LL8MYQtx3gWqEB6RDfbOCNWFozqz2rdCVCk0djEzhEXbhn7Ed_iz-SLlGlcuD8JntLy3Q4Zqw9HUVG6zX9mWjr3_8LCdBWnNbmYac5_VjiXhWKsPBQb9AH0gRcUM_MYi-AXfBd4tGlV4UOVUohq96mn-_SglE2IkdYvzS-N41exIxf_HIUrYFLQN7qCCRAX53EULpiNwjAf8b0j80xT1DNzTNuoztRh84D9IQwkdBVPzIcgUzPdmkn1DU2UmGaMu3KaeHN_tUFZpJs5P8Whuhuz-qLClAYUiJXc_gMQXfow6WKhhn02yJxQKJxodaUnEmrbh0Muhxc4lR525AvVYwfkzGB3D6uRCM__C6qH8eQpm8eKp5xS4tpNiomlz9jFXpCNP_gqAZSeDahpCo6-Ides_CgnfdJopXJj6yRxjESYyZUmjuzZl18uvfOx_-vM2MZJPSXmVezQO55kZN5SBwPyFOd7SaaxMRWlU6-35vA1ZR4s8vsdGXayqPqtAAHA_Llu27ieyDeXuOAYzuGMKsc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ced0fc60cf.mp4?token=VbD-FWZ6DuinPzOaBpDK4Wc-eEsexu5IYNoaYjP84ujTpPaCs7AtfQPCmBxk8IMwi4v57iMm8XIIcVMnTCOrj9jkDaU9FIg8LsJwyeu0FSXln4Nohk8fl7IegensPVEKJyO0MoRer8OMazkqn6ZV4LL8MYQtx3gWqEB6RDfbOCNWFozqz2rdCVCk0djEzhEXbhn7Ed_iz-SLlGlcuD8JntLy3Q4Zqw9HUVG6zX9mWjr3_8LCdBWnNbmYac5_VjiXhWKsPBQb9AH0gRcUM_MYi-AXfBd4tGlV4UOVUohq96mn-_SglE2IkdYvzS-N41exIxf_HIUrYFLQN7qCCRAX53EULpiNwjAf8b0j80xT1DNzTNuoztRh84D9IQwkdBVPzIcgUzPdmkn1DU2UmGaMu3KaeHN_tUFZpJs5P8Whuhuz-qLClAYUiJXc_gMQXfow6WKhhn02yJxQKJxodaUnEmrbh0Muhxc4lR525AvVYwfkzGB3D6uRCM__C6qH8eQpm8eKp5xS4tpNiomlz9jFXpCNP_gqAZSeDahpCo6-Ides_CgnfdJopXJj6yRxjESYyZUmjuzZl18uvfOx_-vM2MZJPSXmVezQO55kZN5SBwPyFOd7SaaxMRWlU6-35vA1ZR4s8vsdGXayqPqtAAHA_Llu27ieyDeXuOAYzuGMKsc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توثيق جديد يظهر لحظة الإنفجار الثاني في العاصمة دمشق بالقرب من محل إقامة الرئيس الفرنسي ماكرون</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81306" target="_blank">📅 11:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsqeDZmDNzTC9cxgxNKncP_hzJXcryIdNnCHa00P04fBVeK62ry4BC-hWBk7PBVBf2RXq9-4w0XL7N54WktZKsoekIttnh07PjFa75F7sbnsVWCqB-qXd_SNimB9tefK6QtNudWBAKJTfGNvm7J_Gkdxd_8-9vYV94qmzHBRJ8QP7AqvW_oMujdlFrLCQjIHn9071qT4tXkQ7LlMI0AY6l0DxMr1JrN_hcG7qnDwj4PMtfyS1jpFTBeFhKMpOto6-WjJvR02YQovnp2cjg2s1tv1in00IVSy53XOBYLcijCGi1gTTYqByatlU2v6fK9TMCJnDPUE8UCe85rBlH-pRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توثيق جديد يظهر لحظة الإنفجار الثاني في العاصمة دمشق بالقرب من محل إقامة الرئيس الفرنسي ماكرون</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81305" target="_blank">📅 11:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a2fa73c82.mp4?token=VvtzaUrSczPzhZTbtR7L6Z1fYe_5uVsH7ulocBOWVOk3anHfRlyvip92hfZ93DSbNEspnnlfiiw7QhSq_-6epBsNq0ygijr67y2HAkfIE5b3Q9dB8NYljjFPuVzr7qiAGWoIrFtu-6fpOfkGmAE2tVNwJJWgseJue5mupikSewETZHsKfR3kZ00kY1T2QqEh2pxN8dtaxzZ66IY7LdjnheTljc9OdganU7JAWQ_DJLWjcIBeKXg3Yc9Qngbzo1HtvWKf2pxE3fi4oL7yJnTZUthl0f54i12xZg0x-v44Tg6pPtU6Emn2G_sxwbToIJf-fRb53kdq07-LXY7olVxcDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a2fa73c82.mp4?token=VvtzaUrSczPzhZTbtR7L6Z1fYe_5uVsH7ulocBOWVOk3anHfRlyvip92hfZ93DSbNEspnnlfiiw7QhSq_-6epBsNq0ygijr67y2HAkfIE5b3Q9dB8NYljjFPuVzr7qiAGWoIrFtu-6fpOfkGmAE2tVNwJJWgseJue5mupikSewETZHsKfR3kZ00kY1T2QqEh2pxN8dtaxzZ66IY7LdjnheTljc9OdganU7JAWQ_DJLWjcIBeKXg3Yc9Qngbzo1HtvWKf2pxE3fi4oL7yJnTZUthl0f54i12xZg0x-v44Tg6pPtU6Emn2G_sxwbToIJf-fRb53kdq07-LXY7olVxcDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 قتلى من عناصر الجولاني كحصيلة أولية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81304" target="_blank">📅 11:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔻
مصادر لنايا: يعتقد أن المنفذين هم من جهاز الأمن العام كون المنطقة تم إغلاقها منذ يوم أمس بسبب زيارة ماكرون ؛ حيث يضم حهاز الأمن العام عناصر من تنظيمات النصرة وداعـSh التكفيرية.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81303" target="_blank">📅 11:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81302" target="_blank">📅 11:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
مصادر لنايا: يعتقد أن المنفذين هم من جهاز الأمن العام كون المنطقة تم إغلاقها منذ يوم أمس بسبب زيارة ماكرون ؛ حيث يضم حهاز الأمن العام عناصر من تنظيمات النصرة وداعـSh التكفيرية.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81301" target="_blank">📅 11:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81300">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c2d1ac86.mp4?token=RaTUJf9NgOOmvk_jTvqPcK0g2hGmxgczaXigHC0ET0EMIOGeMHCzfKKT5CQr7X-cTS9dDLt6MUTMyp3UUcBc5OBJC_dg9EfUHJ6hcPKlyLjGjbyBTS-r50WJ1A-kbINlfnOwizJC8Sjjzqi2nvF2a3OJzNSanbR54xDaTTuCgHyUGNKvS2H7AqkkCHzo4qBLr6OTrfwDWmPVD_NSsJZhvSHjvDT0WNm64qPvAbstSfjbeaiDto0mkfONjRgALIpT0cP9I4FiRiq3kPpHwsqapiQzHwZr-ZXMXPX7wK0xjnSAJoGRwG7rNeWv1-e7tlBMH6nqqVfE_1DJVvPnBh7frA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c2d1ac86.mp4?token=RaTUJf9NgOOmvk_jTvqPcK0g2hGmxgczaXigHC0ET0EMIOGeMHCzfKKT5CQr7X-cTS9dDLt6MUTMyp3UUcBc5OBJC_dg9EfUHJ6hcPKlyLjGjbyBTS-r50WJ1A-kbINlfnOwizJC8Sjjzqi2nvF2a3OJzNSanbR54xDaTTuCgHyUGNKvS2H7AqkkCHzo4qBLr6OTrfwDWmPVD_NSsJZhvSHjvDT0WNm64qPvAbstSfjbeaiDto0mkfONjRgALIpT0cP9I4FiRiq3kPpHwsqapiQzHwZr-ZXMXPX7wK0xjnSAJoGRwG7rNeWv1-e7tlBMH6nqqVfE_1DJVvPnBh7frA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضع الرئيس ماكرون لا يزال مجهول حتى اللحظة</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81300" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لحظة حدوث الانفجار في دمشق</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81299" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1453202c0.mp4?token=vzXlFXy24LzTSD6E_bZ7RkQD6VQCIJEgCGdfdOrfUg0jiktegkds4fPxPO2m-xqL3GZ491vcLBHr7ROPCZlpAgu18PVCQu4ni_8pG2vBvJw40m04sIXMRb2IjEGNLm3ji9NzJPm-3oDQBhZuVpc7hC9_aoZGAlhsQ4qvluiNFxpioU1IRQ4ZNRsepBRfkmO90eL62nTgvFe93JTi4p7PyajentSUJk3JfbWAj8SwL-qnT-uV301T9AawGs_tuQq7wreXRQGSb9qxrJxEtM8NqWhLzjT25e9Ki0DDw5LGSrUunPIvSSTxtNG8JBUllZHg02kFF1UoJ1sslmwJyBHm0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1453202c0.mp4?token=vzXlFXy24LzTSD6E_bZ7RkQD6VQCIJEgCGdfdOrfUg0jiktegkds4fPxPO2m-xqL3GZ491vcLBHr7ROPCZlpAgu18PVCQu4ni_8pG2vBvJw40m04sIXMRb2IjEGNLm3ji9NzJPm-3oDQBhZuVpc7hC9_aoZGAlhsQ4qvluiNFxpioU1IRQ4ZNRsepBRfkmO90eL62nTgvFe93JTi4p7PyajentSUJk3JfbWAj8SwL-qnT-uV301T9AawGs_tuQq7wreXRQGSb9qxrJxEtM8NqWhLzjT25e9Ki0DDw5LGSrUunPIvSSTxtNG8JBUllZHg02kFF1UoJ1sslmwJyBHm0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاع المدني يستيقظ ويتوجه إلى موقع الانفجار بعد أكثر من نصف ساعة</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81298" target="_blank">📅 11:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06afd021bc.mp4?token=UCVc2oln-Ok96HHfhfYtRjHGbeoJryj-ljqZ9SS2nhFlKea49wgc7l__0QWckPZMLfADeR4efL6gAWpMRGIwVwpePnyAW-YMww0uEY6ms3C2pEP-1KLa2_qcThOYlFoSbpBkZ1T9CHiw8HaQvK3tEJ7rw_vHHsbriOj5YlyNR-_S5dbEvuZB3y1fPgninc1tKUHJNRqGQGjG0Q8-42sLQhRl412gpnPfzlK_EBamwPJfTBTZfz9P_ANK3AWneIYx9MpjgN0vI-Z0r0ctjQ6tOCBQcYbAvlxnTwVvh_J0_WXcG29gLEa4crLd4wq05yfoWyEZOlE3UqdcQPsgqMnt3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06afd021bc.mp4?token=UCVc2oln-Ok96HHfhfYtRjHGbeoJryj-ljqZ9SS2nhFlKea49wgc7l__0QWckPZMLfADeR4efL6gAWpMRGIwVwpePnyAW-YMww0uEY6ms3C2pEP-1KLa2_qcThOYlFoSbpBkZ1T9CHiw8HaQvK3tEJ7rw_vHHsbriOj5YlyNR-_S5dbEvuZB3y1fPgninc1tKUHJNRqGQGjG0Q8-42sLQhRl412gpnPfzlK_EBamwPJfTBTZfz9P_ANK3AWneIYx9MpjgN0vI-Z0r0ctjQ6tOCBQcYbAvlxnTwVvh_J0_WXcG29gLEa4crLd4wq05yfoWyEZOlE3UqdcQPsgqMnt3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عجلة مفخخة في دمشق بالقرب من اقامة الرئيس الفرنسي</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/81297" target="_blank">📅 11:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6428c1e9ac.mp4?token=DJHp7zZ5zJ3vEilrtxkytIFh6mgl8sbyFP05E9t1u6qSYLsVFZ5jnQ9OOOxcs-1HvPSLrH2nP3Ng5SKHxO0ql1ZLV25M0N2y0It9p4HYrlp3m0l8zNsjGic__xd9Xg0FWTvODyF6LHbmD-zB6ST53mDikTF1_-leFJUoe0k3n-jJ1pvq6wn0ldAPJG-jEjcfDb411MJhgvws1emiZcwckodClHaWHwK6uPU7WdScYYNf8JoIsByd5-9Qgxysa3ZUHGK9uVzam_R4RKjZD63JNTZorEcpKr60bJZXA2YzZXFS6ijeYqU6fUT0gDhvA550P1YH_xfa5M1i2_Im_Blk9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6428c1e9ac.mp4?token=DJHp7zZ5zJ3vEilrtxkytIFh6mgl8sbyFP05E9t1u6qSYLsVFZ5jnQ9OOOxcs-1HvPSLrH2nP3Ng5SKHxO0ql1ZLV25M0N2y0It9p4HYrlp3m0l8zNsjGic__xd9Xg0FWTvODyF6LHbmD-zB6ST53mDikTF1_-leFJUoe0k3n-jJ1pvq6wn0ldAPJG-jEjcfDb411MJhgvws1emiZcwckodClHaWHwK6uPU7WdScYYNf8JoIsByd5-9Qgxysa3ZUHGK9uVzam_R4RKjZD63JNTZorEcpKr60bJZXA2YzZXFS6ijeYqU6fUT0gDhvA550P1YH_xfa5M1i2_Im_Blk9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجار طال باص نقل لوزارة السياحة قرب فندق الفورسيزن.</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/81295" target="_blank">📅 11:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجار عجلة مفخخة في دمشق بالقرب من اقامة الرئيس الفرنسي</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/naya_foriraq/81294" target="_blank">📅 11:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4f2e76af.mp4?token=mfP1GnP0aW6R6_8ttyOoEKMm6ad7qO69B9jmeLFxnY9C2SfsTxjf84IkrfKNV4gs69jn8z9dNIhMlkkQZjMSHm6rupMa2IVmolAaTa-EUvrFtp3o5bbJfhMJMKe4b4mnyhtmni6lX91De-qnaVDXe0jz-MgGo7KG2ndp1rpgOeTNrtp-Xw1LvnV1fpLR4HEboGjG5GpuRoXHrLoHpWMtkPaMmhRRYL27RhpDiHIcIQo8TGObakD_iU2Uif7KpJk0kjYU8KDSzYODl8G8_EYt6GRFoMCH3m01fwQY0cKBZtP3grsNz190g7_y7wvf4REYQY4vvyxhhL00rbZnushYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4f2e76af.mp4?token=mfP1GnP0aW6R6_8ttyOoEKMm6ad7qO69B9jmeLFxnY9C2SfsTxjf84IkrfKNV4gs69jn8z9dNIhMlkkQZjMSHm6rupMa2IVmolAaTa-EUvrFtp3o5bbJfhMJMKe4b4mnyhtmni6lX91De-qnaVDXe0jz-MgGo7KG2ndp1rpgOeTNrtp-Xw1LvnV1fpLR4HEboGjG5GpuRoXHrLoHpWMtkPaMmhRRYL27RhpDiHIcIQo8TGObakD_iU2Uif7KpJk0kjYU8KDSzYODl8G8_EYt6GRFoMCH3m01fwQY0cKBZtP3grsNz190g7_y7wvf4REYQY4vvyxhhL00rbZnushYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضع الرئيس ماكرون لا يزال مجهول حتى اللحظة</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/81293" target="_blank">📅 11:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/81292" target="_blank">📅 11:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwmnrF_xpE2tTn1kLvJPD9wQpCpWTSvuHw7WBcb6fbhf2bWGLCQPTos11iF_ruIkd_Y9Jgil1icUadwaRdqktTDO7vdBSwKyK5eY32V_ph0n8NNhdBJ4WzRL4xQ3v0Pnjdq-Oz8rKGW7v7PxLXj8fPiJKxF0lgjDDsjoEWkv5Krk2pWTFqfgxy1g_8WFDjLjL2joJ2OFx_4TJXHIrHaQJH6U_voNtFzXU4pZ2_C5MDg9Vv4Tyjjq0KXt9i6v6R2MWuunh1QguP7J30OSfPA2AAcAzH7OQNTxkYJi3DGlPUxGAAFHwmxh27ViDvdmsoDuxQ0s6qgnHuxHauP8XnoAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من فندق إقامة ماكرون</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/81291" target="_blank">📅 11:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/272c8263d3.mp4?token=AUYAtZpm5MwQ-b_TLaQHQaRZWuE1uXSiY9yTEyvkRe-Zt5ho_BJD9fMhohfA01FNRUcYxBUk59olBq8w22rSADYtq8AF46AAri1cOTt9djyghf6keTQ-fMlqWw40HrjL0rvn8pBgHo1UtHcJJxgc10dmIekwbSGZqNsvcaUGy-_zKljYQnhcNZL7nTQeU1Sg4xYEzs90lzhgEuwV4rAYuIhgRuh5e-K2mlk7GSuFdIuSum_iJpB9kv_5XqZK9D5gWiU-Q7OcLOUHrEREammKt9wHAdVPisRnv4RHIJzt0IKdB1bdLpiVECfZgtnvAzCWj_gLWOscDrUZtKgDScDd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/272c8263d3.mp4?token=AUYAtZpm5MwQ-b_TLaQHQaRZWuE1uXSiY9yTEyvkRe-Zt5ho_BJD9fMhohfA01FNRUcYxBUk59olBq8w22rSADYtq8AF46AAri1cOTt9djyghf6keTQ-fMlqWw40HrjL0rvn8pBgHo1UtHcJJxgc10dmIekwbSGZqNsvcaUGy-_zKljYQnhcNZL7nTQeU1Sg4xYEzs90lzhgEuwV4rAYuIhgRuh5e-K2mlk7GSuFdIuSum_iJpB9kv_5XqZK9D5gWiU-Q7OcLOUHrEREammKt9wHAdVPisRnv4RHIJzt0IKdB1bdLpiVECfZgtnvAzCWj_gLWOscDrUZtKgDScDd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من فندق إقامة ماكرون</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/81290" target="_blank">📅 11:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17b4513462.mp4?token=g2yQvZSMacIT7gEr3GvNQtfal9wuIJEzc0osB5CwPzDsCxUYTBqFY2pFXRrsJvDp7bqL2xTtu7d2hE_H2n10ggVQtUlJlqHsIFYZ4CXUcYf5jdf093ZpiUBAQQ-CqX3sjqFW8NlqX6ri7LCKKrKQ6Rl_mQUpalR7ZlNdC9R207Qhai1SClLCgU_RwMhA0vfGU2b1VM7z9BD6iHnBtBaLD0UKD0-dIbThS042-xwXPMlpIPu0Y_kvhjSrcwDM3CbOv65KIo1xab-yK6K6SbtPkIKa0RxMcrWq-A82IrCkE5dyYnyjHbCQmC4_hFyJ9E8eCZTaAOhxxQZe_pzgE6XXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17b4513462.mp4?token=g2yQvZSMacIT7gEr3GvNQtfal9wuIJEzc0osB5CwPzDsCxUYTBqFY2pFXRrsJvDp7bqL2xTtu7d2hE_H2n10ggVQtUlJlqHsIFYZ4CXUcYf5jdf093ZpiUBAQQ-CqX3sjqFW8NlqX6ri7LCKKrKQ6Rl_mQUpalR7ZlNdC9R207Qhai1SClLCgU_RwMhA0vfGU2b1VM7z9BD6iHnBtBaLD0UKD0-dIbThS042-xwXPMlpIPu0Y_kvhjSrcwDM3CbOv65KIo1xab-yK6K6SbtPkIKa0RxMcrWq-A82IrCkE5dyYnyjHbCQmC4_hFyJ9E8eCZTaAOhxxQZe_pzgE6XXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الانفجارات التي هزت العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/naya_foriraq/81289" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnnfgjFRCeJ4lDGZtdH232Sw-4cW43kEHge2WrvP-k0Poi0ms20qfJscD-yifKNBKSHSUp2Go-OZY_keeAD9xEmsuvgbTZF4k3RH721ctVX37CBXKyo55UQtgOtRb_L6ntoQfmS1kksU4Nm3oMtjGa0s1CdmzerHBZr_UkD9i-6vb2Jv8xVqPjzKnjbywByNkbHFRcgksihLQUBIb4dGcBsfibknhvuRbmRPVLF4IwvG0m1ZaltnUmYHQrLQ5Bq_I3ynURj7M5NtiygHhdph_ZqWsuPFii3B7PiYHpR41My46raX3Tpk8P4vkRweXDR9AUvjLIoLMkKC4sLnml1mNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من الانفجارات التي هزت العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/naya_foriraq/81288" target="_blank">📅 11:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyISyeWrtZTRMoARCZrrj1-NtsGQnewjzSIA5xYr5Pl6FT4RV6DnWjlekFsGQcvCtK4ipGucdo9ML6PnWvcq1c2-3QVoX_CtiG3ntnBBKmh5UQOe-rVzjp4Y9iPXOKW-ipt2Ogy6lKZN9iWL-OJ_vxA2TwvssdEHLpDBQx8qVXG5wlW-U4FTmFBS-Aps1GXnm1b-YvGBd66z2Q5688Hi4bguP5OfJAecVjDeIdpyLqYmmfitqZfI9PtWSB_YlrOb2_kykl9JMxsw8UG6hFEmMm2EfIVr7GRjLXFjyrtOFHAbAvQrOKwUjibtKRaUMBtSk-WsI4zFTiz4k47FGrHFng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keQ7C4pd7MrouQglkiB8uFuBDLadLpFP5_abIrETiqjYvwbLpkNDTLGyxbx-YDB1K2VgtvPwk3ZbVjPUC9kiSt3d0lRaTWx4QRtXhTqesPlxTht3isC0x1jlGv3pUu1qYCBx03XkS-qtmJc-401CRO65XTBdE3qOP8y9OMK78ijUT3-FOtBd1rkSom0yBb1pH8PfVpfmgBUZVm6D26FSG5ayPv-jU4tycDV-5IkhE_LuVvMdYiok2YJF0z1C76MZTrkz_5TTZjdTQeUVS-LDSBE4gvZGNzV8E-SHW1B9EOXev6VuYXiYl0adOQpUGnYBhWGddcHuXAxkK6GtQRAbrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاعد اعمدة الدخان عقب انفجار عنيف في دمشق</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/81286" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae08954e6.mp4?token=cHGYcs7fDPM16Klm2xEcQU7_-vaDZAUnqFBjoInKRdoNYcjdgiL9DJnWZjBKN7xw_fqkHLagUa4R-jSm2lEYBYpuhBUURgtbVeoPtuJOxl7eRBhaIcK2ENl3uuIShJVugGIPKmu-HiWPScYnqdfaGsWDYt3fcS__hR7eGqVbN7bh3scWOinX7NASh17T11bZkFs7VSDtnwWOOaRYUT8yMefEOipW4_xxRRy9KjKROFSrfp4Cf25Zbr4TRpRiKBX4ACnSn0OnJH_J8DD7aBIy3Z0DEqKynwr0BOqDNbA5bZLerqp5wdZHobtyME-xQ7OnhEYif_R9VA4EjZ1w-8wS4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae08954e6.mp4?token=cHGYcs7fDPM16Klm2xEcQU7_-vaDZAUnqFBjoInKRdoNYcjdgiL9DJnWZjBKN7xw_fqkHLagUa4R-jSm2lEYBYpuhBUURgtbVeoPtuJOxl7eRBhaIcK2ENl3uuIShJVugGIPKmu-HiWPScYnqdfaGsWDYt3fcS__hR7eGqVbN7bh3scWOinX7NASh17T11bZkFs7VSDtnwWOOaRYUT8yMefEOipW4_xxRRy9KjKROFSrfp4Cf25Zbr4TRpRiKBX4ACnSn0OnJH_J8DD7aBIy3Z0DEqKynwr0BOqDNbA5bZLerqp5wdZHobtyME-xQ7OnhEYif_R9VA4EjZ1w-8wS4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الانفجار قرب فندق الفورسيزن الذي يعد أشهر فنادق دمشق ؛ تزامناً مع زيارة ماكرون إلى دمشق.</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/81285" target="_blank">📅 10:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجار عنيف يهز العاصمة السورية دمشق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/81284" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
