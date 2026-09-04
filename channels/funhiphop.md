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
<img src="https://cdn4.telesco.pe/file/ShaYEiRS6PDqfbaW6PlcXUPZYvGx3YGLtK_u04XaNbghF06yalGIPzxUm4k67pNgNoV1D9WIaO38K1gOvw6-LgjCp0ZLn8MLc5W8ea57udMoy-nDyfTztVqfTZHo0XQRFvnPON6UIBj3hhfcDkYv4scMm5ZlsEf4cXr71Vs_dDBj9YLX0g0X3ocsbpaWM5fBvp38h757GVPdYYQPgF6mrIYYqYeQ5PrIlBdH5WzTo3DkmSN7COiR4UfYf5lp49-kI-tSJFDfj5aAa4mTF6jLCL2xlssdz77jI23IThWsrZpTEIxWsSqWLmJqG-sFGa8-R7ebINuA6lBsRJ3fjG0ArA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 20:46:44</div>
<hr>

<div class="tg-post" id="msg-82994">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=H9i6rJySzrMK1TZ3BEIakm71wZ5cZFYVxjYNyKhn9A6Wbzi9Ec3CujnCCX4SjOb1uPS_Rly7zJ9_SpfCzoki3zabG1l92Wrn-s_gJnxgmExO1Ym0uDQRxOMhx1K_qySmfwwTQisD4PnkRdEYBeGyaYx_2tmYR6mVqDLNi8Xi6WMRbljvO4KwRzwl1Iz4c-Lxax1gy53FjmnyTERdJvBWpDW7AoTEcNV4YMTWO8NkvzseZRh3-49nwfJ9JwmVZZzKMKZXhiu6aFCnclzuK2_iGLKu1NBsthBHJzeiWNnPlzk1TZG85PQ9ELZrrmWb_1yP-s-cruR_OjBXTXAaEG4vgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce693d467f.mp4?token=H9i6rJySzrMK1TZ3BEIakm71wZ5cZFYVxjYNyKhn9A6Wbzi9Ec3CujnCCX4SjOb1uPS_Rly7zJ9_SpfCzoki3zabG1l92Wrn-s_gJnxgmExO1Ym0uDQRxOMhx1K_qySmfwwTQisD4PnkRdEYBeGyaYx_2tmYR6mVqDLNi8Xi6WMRbljvO4KwRzwl1Iz4c-Lxax1gy53FjmnyTERdJvBWpDW7AoTEcNV4YMTWO8NkvzseZRh3-49nwfJ9JwmVZZzKMKZXhiu6aFCnclzuK2_iGLKu1NBsthBHJzeiWNnPlzk1TZG85PQ9ELZrrmWb_1yP-s-cruR_OjBXTXAaEG4vgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به لطف هموطنای عاقلی که سطح IQ مثبت هزار دارن، لبوبو ایرانیزه شده و وطنی هم وارد بازار شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/funhiphop/82994" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82993">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/funhiphop/82993" target="_blank">📅 20:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82992">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">از اصفهان موشک زدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/82992" target="_blank">📅 19:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82991">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">از اصفهان موشک زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/82991" target="_blank">📅 19:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82990">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWymvoQ6DFNxWbfiWnQx2hYaO1iPgKlX3WggjGV0mGBnKhKZWlziCfQ3zR7nJWlmZ8p4DloYP_4G92vUeEk3Aj2_4wKAAHhT1_iePJQZjfSbtMxdOdduSqNgxEKCzTLKWQrv_WmqWdrZNHSbgfGbaC9Vs0W2UttSZ98ehSDywoZcjszf3hgsuFVIHuVgYk5SmbkdvtEIVZZNFNdAhBhv2oBKfd1zVLMHMuaLYejMLJbnbDeZugsEPFdBjNcsI4DwMd8YXamlIFs0jrZw8vHxCGgKP6y_U0Hkt2obS2lfty6WSDmZrDczMU4M9xJe7Rifo02ftBKWUW3YPdJdFo5Tnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوید محمدزاده از تئاتر "آرش" به دلیل استقبال کم مردم اخراج شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/82990" target="_blank">📅 19:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82989">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برو مارکت ترکیه خب مشتی، یکی از رپرای خوبمون رفت الان یک اونجاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/82989" target="_blank">📅 19:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82988">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hg30NzHGrxFYBr2aL5jdqcSdXKblwOs5bIkPfyHbami4jB9KpM4YZo3j45EFLjbo-AIJG4Xlk4japWM1s8Z9rE1YkrWIsKvGXY4GjMUst-HHTZ7OO4-TdSe28DL_oGGgrVyF3F8pJP8Y1pKPfS6aAYZpuJAqMH4rmQnTlE2hMbtVi3dcyOP3nuduYNCHYlQRCsInkXjJq1Bat2HjneawkP9ZNmNM1gh4vyh_UeLaV4L2HR2O8DPq6rMc3IppGkIqJpsnztbkAM26CBIAbYAtJ2ZaFx8Sagi2m-RrPQ6ZL2TbPX6HatSvkLhmLsNMVdb7D00cCwJxbpTJaen_SpzmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای چنل کوروش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/funhiphop/82988" target="_blank">📅 19:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82987">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=m1CxGqyDMY1klQx_FXQ3gKhM1ov9qdjXhvxdwJRCJWa3r_Tu4e6kvy3ifJUrRTw5S4X05og0JHXkel-d7ETm9hvbwPGGOj_dBqmaYmQvTV82Vfj_pXlUkSg8HFWD1DvLECTE63AviWpsZnxhKsotPHgQX2C89nbISNIbP5ggL_MwNuTFWzOsg5sxohTMh_kwb40i2gd4B-ICYjHBO0atjX8qoabfoU90TfS_ZZKfVadkxqR5E1vQlkd3Eua8CIQe-wMTQ324r3JMklTOyTJANdVLctNIl4mpqijhvrT9ciVnAHOJCiH_TFveBmcr90yXY35QcxN_LFqcwpJ5_dm9Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ed68f76d.mp4?token=m1CxGqyDMY1klQx_FXQ3gKhM1ov9qdjXhvxdwJRCJWa3r_Tu4e6kvy3ifJUrRTw5S4X05og0JHXkel-d7ETm9hvbwPGGOj_dBqmaYmQvTV82Vfj_pXlUkSg8HFWD1DvLECTE63AviWpsZnxhKsotPHgQX2C89nbISNIbP5ggL_MwNuTFWzOsg5sxohTMh_kwb40i2gd4B-ICYjHBO0atjX8qoabfoU90TfS_ZZKfVadkxqR5E1vQlkd3Eua8CIQe-wMTQ324r3JMklTOyTJANdVLctNIl4mpqijhvrT9ciVnAHOJCiH_TFveBmcr90yXY35QcxN_LFqcwpJ5_dm9Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست پاشینیان نخست وزیر ارمنستان تو اینستاش:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/82987" target="_blank">📅 18:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82986">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=XJI1ZEZhqeTrtDJX1DFkmrLaGllImuAfLeab6-SHS3zfarE2IxO3LrjtgRv0KSsHXoFNzBM4U5zFmml_7eDJN4hgfWd2s-lE4Hhyz45cz2-u_8hjqADB6gfytXkD5ZOGoT4h7WoFNOOgUnz82c71IK3UCcTxTpMadw_doCTswzP3j76BFra6ihGUUtM4_E1Im1GKcQsSAUD8T-NkRuqIwBES1K6Y1ICsoNyjCoJ-2x8GXmMcY9CnInLrIw-i5qRxA7wQRAaYX4MwqlZfsEKnadlK3UKTTNOkMaFjw-nMxxU_AyKfNaA_u5m1KLZ8wA_u6Zr_u3Vh_bEmznbr77mqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf87a5e3b1.mp4?token=XJI1ZEZhqeTrtDJX1DFkmrLaGllImuAfLeab6-SHS3zfarE2IxO3LrjtgRv0KSsHXoFNzBM4U5zFmml_7eDJN4hgfWd2s-lE4Hhyz45cz2-u_8hjqADB6gfytXkD5ZOGoT4h7WoFNOOgUnz82c71IK3UCcTxTpMadw_doCTswzP3j76BFra6ihGUUtM4_E1Im1GKcQsSAUD8T-NkRuqIwBES1K6Y1ICsoNyjCoJ-2x8GXmMcY9CnInLrIw-i5qRxA7wQRAaYX4MwqlZfsEKnadlK3UKTTNOkMaFjw-nMxxU_AyKfNaA_u5m1KLZ8wA_u6Zr_u3Vh_bEmznbr77mqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آزش آنالیز ببین کاراتو تروخدا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/82986" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82985">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/82985" target="_blank">📅 18:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82983">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5EaojwLlNM0_M7TD5ZcUCxu3Zq0by_1KoS4w_FpDD9q9UCilLH05jC4QZJ922IW5A8uEZ7vr7hKy_l3_4XSPEyAWk67XUwxXCo44HZApELkq_pLf052IDX-GxLoACkNc6eDos9a-sSfEFVVCTCL5ghZhcJDsW6g0u0rsGd4QKGGb8r--ipXya_GMYup0MQjGKceWu5Qeqx-pOBMupfjtV6jQ5M-JVz6QBZuKL3wzdh64GUb7vwcT5EjnYceXfj4gkLWZqWB_nJwgiQozRafriA7lnMAApOHiGHLiX1hv-2lfgn1P11-jv-CH0p7KRdyx19VPQYv9eOLIUUu8dScvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=chwV5RGSP3iHz5v2O-Awohb7DhcME5zkdJukJZ2kZBaODHhYoaY7S9f32dqxRG2fhr-fDKKMDxfOnxbJ6Htdt0uDdCANq4dJZPP8_Kp1sp-VV1sqCtH7bS4ugsqce2_uglMdQRx4VWm9sJQZzbUXSrkYyEUy9lWoNxuSzrzvJPfoEUcrcxSXpHEfZed5c2Rl6Y48_yIWGnYVfKkt6G5s4kWHRINXQQ99HvpZyClcGa6TsYrrZzhjGQYI0UwTqKRbvdnpi5DszXn5iT9qNUNVaJ4IRjlC6Vb9mMrALYKNEhtrR_wwIHccWslifMasvNozaSgydrKasXRs7Z3qRlqu1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b684e1d.mp4?token=chwV5RGSP3iHz5v2O-Awohb7DhcME5zkdJukJZ2kZBaODHhYoaY7S9f32dqxRG2fhr-fDKKMDxfOnxbJ6Htdt0uDdCANq4dJZPP8_Kp1sp-VV1sqCtH7bS4ugsqce2_uglMdQRx4VWm9sJQZzbUXSrkYyEUy9lWoNxuSzrzvJPfoEUcrcxSXpHEfZed5c2Rl6Y48_yIWGnYVfKkt6G5s4kWHRINXQQ99HvpZyClcGa6TsYrrZzhjGQYI0UwTqKRbvdnpi5DszXn5iT9qNUNVaJ4IRjlC6Vb9mMrALYKNEhtrR_wwIHccWslifMasvNozaSgydrKasXRs7Z3qRlqu1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید پخش شده از نازنین بیاتی کف تهران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/82983" target="_blank">📅 17:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82982">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpIiqxZabexwq-b5Io9BK4alLECEFrTnDpZtQII0qvGAJbhEYX14jJjFGm4p1GsrAs0atO5-p0fYQqJff4rdVIclfZrUODgtGJy3UW6rm2RxHbZtJ1mEIMG1GOR7io3B33w6hPIoKhKqj8ceXAo--u1NismgGzsoq68oMtE4qYw_iZ4MX3-MsKpupBP4MYbZCLjch50eb5ECL9M30U6PqT9tGOkwI1fax0DVLsTk-CtNkS-P0QEqE8tmRAwLQqMwCXQ6dmngHfvhkKtEUj7bz_n-6KC7XXnghdLmJRsOp8bCRhfJJfdQ939szUDrl8hERB87oZNLkcRgZ-2f459cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته سوم لیگ برتر انگلیس
💯
⏩
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های نفس‌گیر هفته سوم لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/PL3
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g13
💻
@BetForward</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/funhiphop/82982" target="_blank">📅 17:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJUem1kUjXEseERNWHIpJDywT4Fcu_iLZeQ3aO37a-Q78b12J5goXGLYI522EAgVtxyBVkwbN4l6Q4ZMFepAaF88N6UcAFk-1bNqS5taFh0ciejFbW5_ScjCrTzmCPcgLjmKwEgAE3ngKXiVInEuyYvhhVUTWeedbLChOJvlvDRkq7n_nY4lkY-1jzqC3BoF5t75tOH3YinTN7WAgugNhK4bKZSGiLEsceZEGpXZ-18sd0FJ26r4f7kY-sNDhwzxRJvEB4OuT8MHNvrBObhG5uzjzLaJUhL9cBlEWaDyQ5GcdVc9k5ueC2MizlcjYIRZaQ0BxdGS6mBgxVBbaf5TFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سیا به نام “چندتا؟” ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/82981" target="_blank">📅 16:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82980">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=cX-g_tB9U_RouNzB3HoZBezsvYUQB6qPIoEvGrIbcv2trW9rh8yhBu1RKRkYFMb0wy1RmBSswI5_hiLc1QXAuQ5pr2xoXYcwbboALCZElhY3blDLhbmwnziSpVTG8e-FAvhbkkkJUplT9w_zba1g3iflNQIoawRvxKHvqpvMXUyBicJ3x7Vetvrx6icjGPl0VLRSaNws46EOXLTyic-nJTfuLPYwN3g8b91u9LrdGQoVqEc8RwOJUDRba-Jl7pIz4YdnF-XLFMRSHWaG4sY_4OSgBs1L8iX2kTpSXbL1ioz31jjAZwx62gdokOV1K3doiTcyaLzoFqvHr2DdS_MCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=cX-g_tB9U_RouNzB3HoZBezsvYUQB6qPIoEvGrIbcv2trW9rh8yhBu1RKRkYFMb0wy1RmBSswI5_hiLc1QXAuQ5pr2xoXYcwbboALCZElhY3blDLhbmwnziSpVTG8e-FAvhbkkkJUplT9w_zba1g3iflNQIoawRvxKHvqpvMXUyBicJ3x7Vetvrx6icjGPl0VLRSaNws46EOXLTyic-nJTfuLPYwN3g8b91u9LrdGQoVqEc8RwOJUDRba-Jl7pIz4YdnF-XLFMRSHWaG4sY_4OSgBs1L8iX2kTpSXbL1ioz31jjAZwx62gdokOV1K3doiTcyaLzoFqvHr2DdS_MCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک‌ها از ایرانشهر به سمت چابهار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/82980" target="_blank">📅 16:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82979">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد. SoundCloud Spotify  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/82979" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82977">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwUf19dlbWzFWHtWdYJbTlwf5HhKCFTeX7E8oEUcMQdHfO9SYHvwm1ZU1lay4aPV7hsfEoS_8vqcUijXkeNdf8b2pfwpUVT6PRMkaG7HC1Dox6tKU3FrsdLGzOBB9PWq6xNLQfhIya8CVNQ7sup6GC0Yj3wAfWWwal0WvSmogldnDvKrRfTLuYieARxg8iesP1pvBLExPmEfXsk0E6w1mDbme3EbOgTkwydaFX7BW2fGSf_AcoVMKDLPW61EFAev6fh-Y4tUYzZi24Q9T_j9x9CIJAO3nFwECqI-NgqWuFVWWfCpoV_zihxgJBNy2rbnutbxzjDvoO9NoeUqrt3Iwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد.
SoundCloud
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/82977" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82976">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_54FsfO08TLC4Ym_t1SZ7dFQICmCsLh5eiyCH6B0KBi4Wr9KXuZcFYkCpkDz-N2IPOw8TTvzQ7dAZAgVkiIR929vLqEnf4kcM_WiJFAWax3RoXmM76PV3UwMo9h9NidYNtyMre8vWLENjr0eMYxVfpVx-fxQocS3G4iVk42UP0SV9JrekXnMel0AAyXYAVbO998wa9GlhKM-mvNBvTJyBo83b4kuCEowkdIEUzZk-lr8rHER8eDAs6gpJVapxgdoYaDhIuV5J9xHj_qO32bDu7ixwacdaMgnUXZfJ7TJFBqKDqSr74ubPaYpu-REYL6GncKKuCGzWDVJ9SyNlvb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهیار و خار مادرش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/82976" target="_blank">📅 15:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82975">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1dyD15hShyd3z6ADoQwOA4ZcnmbNJlIrUamU8_SyRnBD17HSU6RkjfciLDCwwbZKc1azkSNiMEIuKv7adueoaTv0frrC-RrfqckIlt5YT8RqyKigM0UDO9MEv7P2UJx7UzUGV_z3bd0UQmIZPVbFPb7L729PA4ZACvYaj_mLhX1caU211uq4hatO-VsaWGCvY1TashBLq23_Lku5SwSdetM687jCnQcQBJ6YvKAov6RWMTIqTNr4EDdg8b53gBSS8m2-p286-Pp4jywmRtR1fQoaZgwBeA_sLYkJ6NoHbsa1KuiuP_SWwofHWCLG_p2r7xsPN8CRT5f10g-hIQRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دکتر حسام خوشبختی تو کیر خلاصه میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82975" target="_blank">📅 14:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82974">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia6HRXbVxY01GNSXOCgHc7O6t3Y_xVCVtnKS6T8sn3kCSg39Mz3dd1a6tlySKl_j_wYfTnn5YWvyBwPPyLisO36e0pkvRZ_6RgP2sHNwrkynFsBMebyecowOKnQDiU0eSXl3N0ixZIyfGwaZKGFdJi-q9bEQqzJg-OhwNpeQ2jjiZ3nW7JYYwb7Vev-VRP1VLUfadqck-wZYY9KDbdrv6MCn7rXZ7fMdChWBjoiiLcJPMcifSL57EqtFmVb7OVi8XLo-29zK_zbDGnbCmuEo_TeFRgyItY4pq07N3SS6a8MBemn7cSPzY26NPoZoQjOCU-YEFL5yPydZA5v5aNk6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید عزیزان، کمبود محتوا تو سطح فضای مجازی و رپفارسی واقعا بی‌داد می‌کنه و ما چون دوست نداریم پرامپت و کصشعرای سه سال پیش رو پست کنیم، مجبوریم هر روز به پیج این اسطوره یه سر بزنیم، ممنون از صبوریتون.
🙏
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/82974" target="_blank">📅 13:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82973">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرگزاری مهر: موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82973" target="_blank">📅 12:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1SETWi-_aUK7FoR2lWShapkQfcgOl_ii3E2vZl2ZwO2IBPU1W4EV4X6sl8JojyvKBcl9t6PJLwnkhPeAGV28OGXfG_95XIedjZo2ExeZADk44BH9BB9XeYiIR7tWaWcYhy2HPYg8BWmM0gIr52EzIuLJP6FSGap8BqB7TnaNMYhTEGg9ToLfFFauas2gZB9CP-RjtPfwT5uYJvoLVkkopibGS5XaBVdFNYZTaH7hIuluVoPvZDNlyrvhsS_Mzp31y81D4BVS4i0B3-QVmtvMlLF3QLtdssVT1uwvGFh_WuepDiGjLva1KFh_fEiKwsGtrSzAsbmJTVijXy5uE4PtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=vO5ULkzATK_5YjK-CZqsCjCtbYUBQpH8zE27N_vmUGX2zTSDHKFhJ8XkUyyKnjC5OmgnibYx0MZyty_bnXqFZyuwRAl2AWnRCCx1Pz68Hxdtc2MK466M7rjrfcpTm6QwYM5C-jA_K1R8rJ9BorqpI3gq9RLg46tdhRaBh8kjGGPOfycSDcoJmxLZi-lh3gtoR5v-C94RHtPFoWClJ0a0jZ9t8c1ynhVU_4NpkMcTLoVn16Ez49TmDIjaWlXvavYTEeMKjzvO2Bn_fQGPGgVK-T6YWsE9o0XMH1gwOELf0GExnxUGVWwZj8hIT1dPQA7CzZaJtIlO1lWgfuH3HJYbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=vO5ULkzATK_5YjK-CZqsCjCtbYUBQpH8zE27N_vmUGX2zTSDHKFhJ8XkUyyKnjC5OmgnibYx0MZyty_bnXqFZyuwRAl2AWnRCCx1Pz68Hxdtc2MK466M7rjrfcpTm6QwYM5C-jA_K1R8rJ9BorqpI3gq9RLg46tdhRaBh8kjGGPOfycSDcoJmxLZi-lh3gtoR5v-C94RHtPFoWClJ0a0jZ9t8c1ynhVU_4NpkMcTLoVn16Ez49TmDIjaWlXvavYTEeMKjzvO2Bn_fQGPGgVK-T6YWsE9o0XMH1gwOELf0GExnxUGVWwZj8hIT1dPQA7CzZaJtIlO1lWgfuH3HJYbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسمی شد بچه‌ها، آه از دل‌های شکسته و حسرت‌های ما
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82971" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82970">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miYzaydBUFbJjNtdiHJNsrDhVeT8IwLcqhA1uIvt9wJLQn3GCw4wa3vKsW0bSDtCAzAmRWa_BxzE0p0xvAfMGIVTFVJcjGE99u2Q1hd9KQT4YpUBLCNJbPzaWI57-ZMODjxMYqhVoxLOUbpVOv7Ds2nhh101RPd2Tq1kXUNfN2bn4lAMzFIOu8Wqru4HhTPcsTA3aJkG58NJcfymcBDbQ7_l-0mhK7Q_M10iZ1Tc9-ZILg47XS7T5QV8mYmCfOEGn0dXw-HWK8497Cs8YSHizE0KdNdB6ec5NJVhmSi2gR_PqXqmdX_RPeSshzGuq44mKu9EIuAjGs7uQ1t76R3tZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته سوم لیگ برتر انگلیس
💯
⏩
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های نفس‌گیر هفته سوم لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/PL3
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82970" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82967" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=uB4imfOkCIN_3qAOc7LUAgZ0zp-ysi_hL_eg-JPukrj5hF68ryEdlZhB-t8hWkO_J_ybnR8smEdusJGDjVgy2gj93CU4XW0g-ZMm0_a6waQAg_BWZWYHfGX995aHv-ZShKXKcFJD9cUS9B4djRFgvWh36PmwpFRieDORLStYs04AEspNmPmlD5B7Goo1DmjGIr91ljWZf-HO04DteGi9p6IV6yxao8MydJ_yW0rt2JBEN2ryheN8bS9HMQismcxvZk0RRgaK4YNNLBAu1tyd9gizwvgFCelAnu70y3r-D2TbngxctfrAnJ3KDEGtCNvvTwVL0ubxCoZMRcBe-2JU3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=uB4imfOkCIN_3qAOc7LUAgZ0zp-ysi_hL_eg-JPukrj5hF68ryEdlZhB-t8hWkO_J_ybnR8smEdusJGDjVgy2gj93CU4XW0g-ZMm0_a6waQAg_BWZWYHfGX995aHv-ZShKXKcFJD9cUS9B4djRFgvWh36PmwpFRieDORLStYs04AEspNmPmlD5B7Goo1DmjGIr91ljWZf-HO04DteGi9p6IV6yxao8MydJ_yW0rt2JBEN2ryheN8bS9HMQismcxvZk0RRgaK4YNNLBAu1tyd9gizwvgFCelAnu70y3r-D2TbngxctfrAnJ3KDEGtCNvvTwVL0ubxCoZMRcBe-2JU3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82966" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=lXyi6Hv_MX1Bi-nTi1g44HQ2iUycqEC44klNkFsc4TBTYoAhDJgVt8VpLzWyNqpf4CAmV-Z_rpNqR3AZyKknET0w7OxN9L7zyr7DKPlbbkj-PvRb_iLVxuvBoI3MJs3V2SK6x0o6xwBgAlX3IRLz1dRfhKHtvUoB14qjUN8oQzfvZH8KKVid6N-_sHeoLR1MoZed2nz3oFhs-0gMO5rHzFYf6K3ys5u3vrg8e8kTwWZSv3_wEtDbtDFVFMvtYbPNKCEoNWcRLFCWdYZWCAHGNSDZXZc5eNvSgEwEgNoLrgv1D3DqCo4KvcfvsYwpVncldQqZ-hZEBA6WGk5yuwWMlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=lXyi6Hv_MX1Bi-nTi1g44HQ2iUycqEC44klNkFsc4TBTYoAhDJgVt8VpLzWyNqpf4CAmV-Z_rpNqR3AZyKknET0w7OxN9L7zyr7DKPlbbkj-PvRb_iLVxuvBoI3MJs3V2SK6x0o6xwBgAlX3IRLz1dRfhKHtvUoB14qjUN8oQzfvZH8KKVid6N-_sHeoLR1MoZed2nz3oFhs-0gMO5rHzFYf6K3ys5u3vrg8e8kTwWZSv3_wEtDbtDFVFMvtYbPNKCEoNWcRLFCWdYZWCAHGNSDZXZc5eNvSgEwEgNoLrgv1D3DqCo4KvcfvsYwpVncldQqZ-hZEBA6WGk5yuwWMlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از صفحه رسمی فدراسیون تکواندو ایران منتشر شده به مناسبت گرندپری کره جنوبی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82965" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82964">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🦁
سرعت و کیفیت را با قیمت مناسب تهیه کنید
🦁
💫
چرا دژنت وان ؟
⭐️
پشتیبانی قوی
⭐️
امکان خرید آنی در هر ساعت با سیستم تایید خودکار
⭐️
کیفیت در سرعت و پایداری
⭐️
قیمت مناسب + تست رایگان
⭐️
اتصال پایدار حتی در صورت قطعی اینترت                               …</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82964" target="_blank">📅 23:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82962">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM3ycYChQ1IGPkDIFDuE4FJpWW_akdTvkaerQyc8_NRmn2O6tbeXyOX-W9IKgfn4qqOoFpJyg3dfDvry1-SJQwJmcq59Q9q1fiR2-ICvDuKkljEAgig4ntl6n-ALcVeQhuqMok5wYxUGTOuratAdgD8fqL4wg1y_QXDy_Nm8F7WFX9sY7Hzmudg7LMTPwgvKEwzQKKVgW8YjN0WYli8j63w2Jg9Bgi_l1tDeGHazh_aSPt8iAlhW6UwM66JRJys0HPNuf0zv5mqFhl6X-WQ9zt9wlqvz29KXHfCb0zy52hJz83rSwVlWXeQ7jLjoBc4VXfza7epygzn6oqkKEvSFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
سرعت و کیفیت را با قیمت مناسب تهیه کنید
🦁
💫
چرا
دژنت وان
؟
⭐️
پشتیبانی قوی
⭐️
امکان خرید آنی در هر ساعت با سیستم تایید خودکار
⭐️
کیفیت در سرعت و پایداری
⭐️
قیمت مناسب + تست رایگان
⭐️
اتصال پایدار حتی در صورت قطعی اینترت
◀
️
ربات
🤖
|
◀
️
کانال
💙</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82962" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اون قسمت از جنوب لبنان که میگفتن اسرائیل حمله کنه میزنیمش
کنترلش دست اسرائیله دیگه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82961" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82959">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmnOH0OuF624BxU1FQC8m5sibQ9OJ3n8fncOyOptkWREXX9w0BNOdejOHt1Hyrsy3eSzLa3t6LhUqJ57Tr2fVkmBafZKF-vYJXsbBgl82bwHUPqNDxH29XW4_5MUD_RK5CDOsN0TYMG-W-XLOwS_sUH2JhL9koORWZI8VZPVD4JialfPBOEhOg5Su8G6nMewVeJn3yQTEygevJPaTd3oYT0uxGcf55BUg6R60B9sOa8Q0qpgueskId1ZhhgQipshsB0HMUF7nA_Pa4u9IY2VgoZm1gm26EKZOEr67jU74Q6SDyNAGWMNKlfK-MZ4Oc1sKCbeyRJ7WXaKDM6VqMhTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکوندی شاه عالی بودی شاه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82959" target="_blank">📅 22:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82958">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=G7jbzJ4eHPgBlkzGyMbdVERTj5OSUbW3GAorlujhWCLOosdSkR2SnzMbOaJN_UtRx9Rsh4f0I0fRczFQZsMslT-koCoeMk-Jzsp9DZSNJrcfo5pAACrrzwviykhTkce8Au6NcBYuo4Nv8gNCG_r5X22ku-o0PsZrz0FdBAFqady1AuLbNAaK9YF3_0lLs1Wd9YnCsXoGksAlrs1wRGg9lLVbEy59qIhm909Ead4M1WbwD0Ke7GApGJtXzh67AYLIaDATaj0qZda1WiqT33jIfZ9PCoFWVdN00e2KHLwmgIit5joszYG9vSKBO_OxNEyTqpaWeIZmEBt5YZJaxAZCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=G7jbzJ4eHPgBlkzGyMbdVERTj5OSUbW3GAorlujhWCLOosdSkR2SnzMbOaJN_UtRx9Rsh4f0I0fRczFQZsMslT-koCoeMk-Jzsp9DZSNJrcfo5pAACrrzwviykhTkce8Au6NcBYuo4Nv8gNCG_r5X22ku-o0PsZrz0FdBAFqady1AuLbNAaK9YF3_0lLs1Wd9YnCsXoGksAlrs1wRGg9lLVbEy59qIhm909Ead4M1WbwD0Ke7GApGJtXzh67AYLIaDATaj0qZda1WiqT33jIfZ9PCoFWVdN00e2KHLwmgIit5joszYG9vSKBO_OxNEyTqpaWeIZmEBt5YZJaxAZCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کافه ها هم مثل طلافروشی ها و صرافی ها جای منو مانیتور گذاشتن که هی بتونن قیمتو عوض کنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82958" target="_blank">📅 21:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbNC_G3Y4cWXZDAQgsz8RTmMBUeQdsWf-FvBncGgvB26hMAqPqrZFy_FZoRcSHkRNrfDwVBKcNniCPr_8kOuYzKJR1zPob_SCFolNwmMcCgGPxKIQwnmTRkuWM20pYo3aV3nWLdEsbdU0ZkXM1pvNJ7slH_bIigUndKQyqlKFC6BwStaBj-G1tUmrjk-wwPTTv1_v2EfT67Xg0581edOCXWDaTJSX-kqGcjWXTaVtF3FD2X8H5PzFCHIlz0ffxtQSiDSygZwkFVH-kKofddnEzmRi6Vud5NHgsckkKTMeMB2kmynwNX_TU75lnkbOYX9B_Z959FDmy1a3po3d70OfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال و پیدار به نام "Bipolar" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82956" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2DGzMOOxf_fOp7Iv7bB8ilncKc2-i_yim07NUi7S3YUDx2lYfMoIkAYjJ1I3XyXbR_hjQ1QqD5k1vE3G8hKAVBZy2wWK2_c6eb8WRWHMP2CSx5-PKTKmE7u-CUM8Jx4-9lvs3CBa3nlmbegcPWgcwiju1fx1zwgdpE338AlkQfhFjAx3-7T3RgVK1dYpXeE--OrurdGhIpQZYzAuqg5nCCHCEb9CqJz_l5nh2UjZrHtQvbCXDBbq1Be0Vt5Ahf3FBNdCBewW6MBLTSEKC92OhfqLgNB1ins8eKlAJxnOVLjKyJLV3BLQoWjFE0HgFI56_TO3hEaGvE7-WGe6LxBmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین بد سلیقه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82955" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZIjHQ0zrGpY7h8iM2awTImGYqah2hk7Bje8JRpLfZWQ5kJhB_kCA8G33XDeDPeW4vmVamDEtmaSumBWyeQL3wOnkBOm3g8J826N8cRYZWla-bLiPgVzoZURpeqYrA55WhC5DIb3UZvNqfQmAcIJc70BHxTmE8wq8XQQnbXoZSCtZ0n6EclOdkT-GVzcBqnDzGC5p8ao_Jmy_lfGaYkXTRkIX0Z6Wul6unF95_k644UPM6VPSK85akXru4zjtPnhfJ2rDzXDWbt0aFzEebwQawT-cGjL4bBqIxy8J5oFVld9augHXxMEJyak8VJIEwWU1jDjs76Cf7Ar-Jz8A0OQYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی و پسرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82954" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzZDkOV7m-bwXO_kqj2xium03rNeRrgbbZsxctjmj4T3tMhH_zrEzC55nwC7mJSMZI69ZI1fSKWQzJsYw11lnQgMNu3bY3TrWfbZ1CiUwVTZC27JbWw1BKI2ydPT5ZRixWG0P3kgNjGPMNutDRsgipAjlMehQqLsUm-dBtnwyFRpQz5zt8EcgZVpk5E5GIycGo7zXUmWp6dBstOO0tn3SKv0bCp1_Ds-LojGQMkFv1GtpcRGQy_bU6P-fE_Q0pMiJCGL64ekyI3R4RP-4pdpxDySf6Bo8BW5T_mljrv9xGtSd7r15dbP7ONAEv5jykcRH0Qxhvvv90rGRKInkgJvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=QK2gZ5OTuOZjA1Cn-Q4WZb6_BGkd-ZVDLFdqmrL8n787YqtbIQ_Ngd7qtp8dPCeNs3obYWfz_AtdKoLinGoBE0zCr80H94nVuJK16epLqb2REfNLVleJZTCiTB08HtS4FAsmbYsX4FIyYFvtSNPecKT0mG2xDEYINJuvWzvHnHj_RJ7kkaZQm5WN3l4r7sGG2GEipOYgas7uKgEqTC4tSUO6caGOVFageEFU3QCEfNyHyYTtRpNkpV12im8ggmcBgR9bUPjHJqsnhSFIQTtxk56S40ogXKSzo6jNp4SUXxBeHc50bkOMpVXvL9SNdZxBmJmbqmEgkfT1IOr7mgEg5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=QK2gZ5OTuOZjA1Cn-Q4WZb6_BGkd-ZVDLFdqmrL8n787YqtbIQ_Ngd7qtp8dPCeNs3obYWfz_AtdKoLinGoBE0zCr80H94nVuJK16epLqb2REfNLVleJZTCiTB08HtS4FAsmbYsX4FIyYFvtSNPecKT0mG2xDEYINJuvWzvHnHj_RJ7kkaZQm5WN3l4r7sGG2GEipOYgas7uKgEqTC4tSUO6caGOVFageEFU3QCEfNyHyYTtRpNkpV12im8ggmcBgR9bUPjHJqsnhSFIQTtxk56S40ogXKSzo6jNp4SUXxBeHc50bkOMpVXvL9SNdZxBmJmbqmEgkfT1IOr7mgEg5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شات های جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82951" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82950">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrpDI6iJVKUWjimrqikFFKGRUBw8FBqIG0ZNKFrsSdRHsCuzx6Y6w4W6xYJzUWav-pcogXaVm2sAdME-iSv-xkGudJM9v7fHUT7I9KnLgsR5zuCdL4jeqceSmNYV9dBz3eLkVoylu7yao7uICIUHFx98-_NlOgZcg-aV42vV9ROD2BTzqty1BcEig5-sMlITvDrB_gxFL0lOAL8mKdi-M3AET56bS0FEzdp3LMKOjkoI4m54hBDV0gV5wyZNsglC9gPJMPEd7BRlLsujnHGwoXRJ15eQrMOSebmmCXV972R8_t0-AtOSSsS-svzg3ndUcTt-a3wXNML1NUIAdvLrJB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrpDI6iJVKUWjimrqikFFKGRUBw8FBqIG0ZNKFrsSdRHsCuzx6Y6w4W6xYJzUWav-pcogXaVm2sAdME-iSv-xkGudJM9v7fHUT7I9KnLgsR5zuCdL4jeqceSmNYV9dBz3eLkVoylu7yao7uICIUHFx98-_NlOgZcg-aV42vV9ROD2BTzqty1BcEig5-sMlITvDrB_gxFL0lOAL8mKdi-M3AET56bS0FEzdp3LMKOjkoI4m54hBDV0gV5wyZNsglC9gPJMPEd7BRlLsujnHGwoXRJ15eQrMOSebmmCXV972R8_t0-AtOSSsS-svzg3ndUcTt-a3wXNML1NUIAdvLrJB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
بازی Chicky Choice، هر قدم، یک تصمیم تازه
🐔
⏩
در بازی هیجان‌انگیز Chicky Choice در بت‌فوروارد، مبلغ موردنظر خود را ثبت کنید، بازی را آغاز کنید و مرغ را با دقت از میان ترافیک و موانع عبور دهید.
🦊
در طول مسیر، مراقب ماشین‌ها و روباه‌ها باشید و با هر بار عبور موفق از خیابان، ضرایب بالاتری را کسب کنید.
⚡️
واریز و برداشت سریع
🎁
بونوس‌های ویژه روزانه
💬
پشتیبانی ۲۴ ساعته
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g12
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82950" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqtfEcdzxIjhvaFbet5U0dMkyW83jpKyIGKu38V7sVfVGJv7LEZ2eT5ovOCu4BkoVlLRyFkxfNK6WhEEmYgEhwXaT00P0qUUN00QMSi5n25AK-i-FgeCWGv6M-N4R1A6XMHJYmv06vmrGZBdXCYTkSDOhqWS-xpqtpS8Ar-AoCAGZCMmwqdpE5PpC0nmDBF_7OSMIfkPW7UVOwoo0qke3vLvAXAq36Sn4kHMDJ0GArM_zYnkdLbnpNPLHv18NZPKyayeIK1YrrV2rb8eSfzV8euKyo5P8uOtDXmwhHtpFEXjAPl6rGDrGUUiIQ9Iv1yilKnn-WYXz6jfqz4_8dB5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام “منو میشناسی” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82949" target="_blank">📅 17:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خلاصه بگم کونمون پارس
ترامپ میخواد پایان جنگ رو اعلام کنه و بزاره بره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82948" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFkeDhnJQmRYqkLNATNisCudsRguSPrvpoJ421cQ808LmMjBiG0R83kg9BguElAz87YpfT9E8MLfsXWcwHPO2Tm5HHtIeLLEZgi5SweE7im7_Ucas5VHfG6nPfKu498TW62xTnGvMV-NZDFnERgIASWJQuplmVCxEccOL3NNb240X7Ecsknbwjk8P_ePkYybOeio9EuAh5qrulm4MqWO_mYgtQ2ebHUs5Vr1j2m6QaMd1PF9e9I8QuNEHITXmz4lI4kx8TeFKdFnB3_lVneYLL69MG3VJksxo_pxo5-zY6PPT_aZBF4Ie7wadyenyBWyJ1Clc1z4tPd-rC8US7Y3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل دوم این شاهکار اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82947" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=bmhNh3tN7gyHIyM70Ho6AqY3X6UgN0BtsZsZcQteuplyu2x2o4tIP_cfkUspiBno0WziwWFSawQZTneDeFBWrZDhmlnHAo8iMTqaokuFnuA3yB1yWEpkg1HYz-lnwjXRARJEeViSs6QcfBLaiwZ2fh8E2MCHuBUhtkmNPYnbXU5BVOr6eUgMLoQVy0X6SIVs0TTa00KoStldWURppouZkff7F0VtCpcD-YtJj3mDqSCI2510AZkiAAxhPa8lXHVqMVCiGow6LmO0g737TKaD70hAN6gld8aYCDWsMdYUOorxkWz6M4F-aybYxUo4LV4gNJHUNrhh3wz__hLur6FU7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=bmhNh3tN7gyHIyM70Ho6AqY3X6UgN0BtsZsZcQteuplyu2x2o4tIP_cfkUspiBno0WziwWFSawQZTneDeFBWrZDhmlnHAo8iMTqaokuFnuA3yB1yWEpkg1HYz-lnwjXRARJEeViSs6QcfBLaiwZ2fh8E2MCHuBUhtkmNPYnbXU5BVOr6eUgMLoQVy0X6SIVs0TTa00KoStldWURppouZkff7F0VtCpcD-YtJj3mDqSCI2510AZkiAAxhPa8lXHVqMVCiGow6LmO0g737TKaD70hAN6gld8aYCDWsMdYUOorxkWz6M4F-aybYxUo4LV4gNJHUNrhh3wz__hLur6FU7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82946" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmjdGqHRpkOrnDaUpXQndN9nWjcyuO3FqwZFyKH5eWBynnZ-VAKfDsRKyC0qp6RvaE3fssVN_-S4zmaDsfSH_fZcCvtbn97PGvf6aFEOXozSQ1L8kPsIpiMqbyqy6GgkcS_EBCoCrtLX7Pr6jo8575eMFF18TYR5wFFvCt9pPyKHKKDTRobbLSOxHvpnjYJWSVXlHZepssNjpcLgvUalzkBYF3EijUpsB1XH9EkNu9nAEJ71nb47h6lY9oXjnI0iV5R-Wrqi_6LgFo9g3VJyr9eYSSL46gSdvCO-xNoz0_GKftasL17dd1AD5ImYFbzIsdLkc-9f0qRcJjJ14KaMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت تلگرام تو توییتر: امروز احساس میکنم خیلی کیوت شدم، شاید بعداً عکسای نودمو براتون بزارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82945" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmUOzZLGLlNXDjAkjFoEF9d7uPBGjb7cVqB22oXHkmrjuLSWb90V5YywKWVuB2oM6xAFkVK2Qs6Hf_m6fCtKGxGSSRckw28nI-ZXFUZobCHJmwaogrwAV8mCTLK_H_OO3c_UrzQWC6tKgj6t44XKoqzofGatvboaOYt4tRdgpyG6JV6_pBklxqxPb7ylLh549-yOFFM7hLoxO84rbbO5FCAnKUccfxkwiV0T5xR2hQ615bnCL5iqvuW4dtPDy_8GOfxwjTb__6IeHaLrrXzGVMuHeGhbl3fkF288UvSEzlAiQoKxWapw-cDjND78tBpuHrrZH6c9mFGocqy7vfmOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد توافق ونس رو دعوت کنید برا تحصیل بیاد حوزه علمیه قم حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82944" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=g5gOVOz-9bIo2LT3Gzm5xisQZHSzrHF4SV5o6dfn3kFCxqvHGnR5pWmczFnQOBtqCtUrnFmc8Oq-psuomUduivUj0Vsj2mrL-3m2k3uXftvlo9ETItoHan6UJWIMPOsHi8AQZa5NN-cNOBXlulfVIKp9TfNh9R_w8J0ILaWOcFVkbivxGLE0_Cfvx2as5NOEZtl_4ukUIjG1S2HCEeGzH9jsCl_vhryppXJckPgAQwg_TihKnLuB4hlMfJs0KDPzSlQjLikigzpzj5e5oPKY6V-fRFjeRxYen46mvlW1_8ru2U7LvJl2mnFx5adpXopzmE3juBzdCrtE4WsS8bUHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=g5gOVOz-9bIo2LT3Gzm5xisQZHSzrHF4SV5o6dfn3kFCxqvHGnR5pWmczFnQOBtqCtUrnFmc8Oq-psuomUduivUj0Vsj2mrL-3m2k3uXftvlo9ETItoHan6UJWIMPOsHi8AQZa5NN-cNOBXlulfVIKp9TfNh9R_w8J0ILaWOcFVkbivxGLE0_Cfvx2as5NOEZtl_4ukUIjG1S2HCEeGzH9jsCl_vhryppXJckPgAQwg_TihKnLuB4hlMfJs0KDPzSlQjLikigzpzj5e5oPKY6V-fRFjeRxYen46mvlW1_8ru2U7LvJl2mnFx5adpXopzmE3juBzdCrtE4WsS8bUHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بهت میگن اگه ناراحت باشی عامل خود فروخته دشمنی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82943" target="_blank">📅 14:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حاجی دوران شهید رئیسی، یادش بخیر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82941" target="_blank">📅 14:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZbIOVx1hoY8j0gIpQNx3AMliFbkGcg0O-zXmmNsjwFOLD63psKAk5PT_f_nDVVEOgiChUzkDgwCWcDOvyUMMP9JxSk-k-RcAlqj5sBUkN4EXSe3niqxIYTAbyl4oclaMxjJnavMIie4zUSWbwI81yTmsF0N2Xz2WVotW0fBR9rvjx-eRjAGNpU1WQrgQPYmqvqTqh02_oiRe4vIg1LkLFfZQRUASHFgber1VNrW7en0wlM1_8gOkesX6wj9mytxUieVlucv6Z2i8FckSNs-nubwwcUgyKnnjsD9tvvOGDcfCqAYhY8o3facBNwh81AahDJts-TB3DEhsvha_DRmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی از سنت خجالت بکش این ایموجیا چیه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82940" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه گدای ایرانی تو ترکیه با  ۵۸ هزار لیر (۲۷۰ میلیون تومن)  پول نقد گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82939" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_uzO_pbszXovLtbv5UlnCJrnaEbknbRc2wp-fmowAjdx4P4PapJGSWXQgB_JKEK43fZ3pTZRmfGPcYNln_dPflhp3ZzvnsmcWqpe7gFRb326tcuoyez5hIz7yCcLxGVecCkaCoOAHPam_JhKc_E5ach7Dy0MmB25Mcf5IvezAjLhH0U5e5nc1NHA89ZaZqNHDCj4Y8zUR4x5zphjCd5DJl8pHjgwT6QiyjnrLnlP2OZs10ExEW2R9J00Psrn3pkMotcjTC9fRKLXj3OMw_BJIv5wSlzw4Tsb6hBmXHEtkwssLMZlBjzr_erzYnyK23_5QfJ8dyyXn1m_7-2CDpxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=evSmKE-Nxhi1En1TkCqg8o--7W1uco8GRGmmY5YniiH0ZAzhsLBenTNa8aZD7DIeUJgwwHzYTiPNf2FXaSZJJAM175JDjCTPdeN4zHdoTpzzKMZ3AaSe1RCE0s3EkOmsJ8Hj_DXYd4We1LXoTxNxrk9IAPNLX95zb-_sMq8Asd0jSPoaOxuptBKRkh2Y1NDgnhqrt20Up4vraPsflegbqxfNzkdX98KRgh64ctiTYXMT2Qw84W0l4I8JmqV0Vs63_XEePMJnHITF3DT-ZNuKD70G007m-f_unxiybzUE8L-6PnGi3Rc9eh3r_7iZCIbIgsw3WVcEJh30C5mW-JR0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=evSmKE-Nxhi1En1TkCqg8o--7W1uco8GRGmmY5YniiH0ZAzhsLBenTNa8aZD7DIeUJgwwHzYTiPNf2FXaSZJJAM175JDjCTPdeN4zHdoTpzzKMZ3AaSe1RCE0s3EkOmsJ8Hj_DXYd4We1LXoTxNxrk9IAPNLX95zb-_sMq8Asd0jSPoaOxuptBKRkh2Y1NDgnhqrt20Up4vraPsflegbqxfNzkdX98KRgh64ctiTYXMT2Qw84W0l4I8JmqV0Vs63_XEePMJnHITF3DT-ZNuKD70G007m-f_unxiybzUE8L-6PnGi3Rc9eh3r_7iZCIbIgsw3WVcEJh30C5mW-JR0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مسی که قبول کرده GOAT خودشه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82937" target="_blank">📅 11:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk87K2llCC5IxFGdnn9Zuhcpoh7sdEunCsRkh5CQTqIGOQlhRzioGxfPFkUTFRFDE2aSAHEtftc4qgbKeBeeTk8a5Ub8yJ8iaky3vN-rKviz0JxfQmjeBfZ42iN4NLcDlNp0CHRyJaaeH6QEVGe6HNqDGVdgqm23b8pTegC12JYvOPXFnI_XmFeqEAEUtTZiJnoeVmgh0vfjhOqb2HAMP59_-qZ-7DXy6C10_5qga3RzbnpzDsC1N9xmh4t0uGKvVvN0TYvmAo4gR0Z2Nve8-dm1zzIs8HLnlnaoB-RwUj6Jk2Lw1j9NLEZANWbRz2JYleqKRLgWJ9AvN5-Ah0vfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام اینو توی باغچه خودش پرورش داده و به زنش کادوش داد، ایشالا که خیره
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82936" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82935">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrNOl-uUyDz5Gw3RqVB1Ibc--ESaxz0XEIxgeojq8mgg4wUWbciCcH3AiiqmLdQuHKVwvgWL14IXkPJktKL0AIJeoryCL0lNOurBLQyESVaG8toT7iO8MY23AMIXHlUOqUorQDR1Y-xOfr8SZ5V8Y6SP6ugRTMluZqli6w1D2ATdj6OEvZ5EkkkwK-0-l0VxDsq8XvhNOeEfO-PdAlLcyNLTo4eP-BMAbzQf80WW6gvjChcRdbFWXrQALduaX0lM_mpPyAYPyfDiOU9W7xDO9ZkdMJx9llUXVE1OaG0NGxfQHzFCd0ESZdA0WD2a15cP7XoZilojX2BMhRCunk0Rx9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrNOl-uUyDz5Gw3RqVB1Ibc--ESaxz0XEIxgeojq8mgg4wUWbciCcH3AiiqmLdQuHKVwvgWL14IXkPJktKL0AIJeoryCL0lNOurBLQyESVaG8toT7iO8MY23AMIXHlUOqUorQDR1Y-xOfr8SZ5V8Y6SP6ugRTMluZqli6w1D2ATdj6OEvZ5EkkkwK-0-l0VxDsq8XvhNOeEfO-PdAlLcyNLTo4eP-BMAbzQf80WW6gvjChcRdbFWXrQALduaX0lM_mpPyAYPyfDiOU9W7xDO9ZkdMJx9llUXVE1OaG0NGxfQHzFCd0ESZdA0WD2a15cP7XoZilojX2BMhRCunk0Rx9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
بازی Chicky Choice، هر قدم، یک تصمیم تازه
🐔
⏩
در بازی هیجان‌انگیز Chicky Choice در بت‌فوروارد، مبلغ موردنظر خود را ثبت کنید، بازی را آغاز کنید و مرغ را با دقت از میان ترافیک و موانع عبور دهید.
🦊
در طول مسیر، مراقب ماشین‌ها و روباه‌ها باشید و با هر بار عبور موفق از خیابان، ضرایب بالاتری را کسب کنید.
⚡️
واریز و برداشت سریع
🎁
بونوس‌های ویژه روزانه
💬
پشتیبانی ۲۴ ساعته
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r12
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82935" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g68Lw6nEzDo0uPGMf_0LzFoPet7ZR5F2dc1_foxkedhR8RHNULg_7EULGqE3trxIKt3zUKtUpIJxGFHzzjSl7IWpyAiV1vBh74kHQ7IkFWPNkpiyw7Td3X_W6zE7laegXROgXoREf6MFgnUpXbzFC1hzIMvcL_nHV36Pyj4M-_dldhLzG6Xvv9yhYRDE0Tv_0Um0LTpYhVf9bOfKD6EaR8z8bf58Q9B94_NhRzKBGh5Yk4bjH6zvgAzps7L7TdWtrdCLb19uAj7ByCTK_1TUq9IgU7Ftf_Mi2NwuwHZHRaBXajUbmmTtZeOruB71EKHxPRLAyG_5EnLFbIM6WHmFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرسی نکن پسر تو تازه ازدواج کردی
😐
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82934" target="_blank">📅 06:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82933">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=DVyOVWjBzb5P2xVgTQre3hO08IB4pZWRBAYz7vmVgaJ19G26VxLHEFZa0Nkx7_McuwKPqXHsLbewBm82bOLw9kk4oBE0e7F0ZAF__Ua9qjOE8F6nsHmAW23IyktQY2GpBJ9hrygqa8I9J4GK1gsGVeH8gui2EYgdqXGziP3a0eO6X6CIC8xDyRep1SrHez44EEfkApC_NPKgd5JNehJfNqmUdF2v0zTFXcMu07_mTav_bmCzGJYcza8e-f2V2avIobB1StlWOzWOgRvWJ2FExJQg5vsZa62VBLguovBFvjfiXmZiwdoG28Xmz1PQHFqaK7jH-e3GKSLhkqzvcudoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=DVyOVWjBzb5P2xVgTQre3hO08IB4pZWRBAYz7vmVgaJ19G26VxLHEFZa0Nkx7_McuwKPqXHsLbewBm82bOLw9kk4oBE0e7F0ZAF__Ua9qjOE8F6nsHmAW23IyktQY2GpBJ9hrygqa8I9J4GK1gsGVeH8gui2EYgdqXGziP3a0eO6X6CIC8xDyRep1SrHez44EEfkApC_NPKgd5JNehJfNqmUdF2v0zTFXcMu07_mTav_bmCzGJYcza8e-f2V2avIobB1StlWOzWOgRvWJ2FExJQg5vsZa62VBLguovBFvjfiXmZiwdoG28Xmz1PQHFqaK7jH-e3GKSLhkqzvcudoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش میخوای کلیپ غمگین درست کنی درست، ولی خب مشتی از وقتی یادمونه این بازی مساوی میشه خب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82933" target="_blank">📅 01:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgbXhu4pHQTMosKv1ZIpKAvCWnZpaKIHKbZROrClzwPflOk7kBA5rFQrYCQYzGSiCLwe6MzdLhZGRNlie-uZLajZgmLds-li3WijW5YWSxal84rcb8kvH60MnPyENKTzb0y3rvvU1BDZ_61bQ6UHnIE_0X4gjQxSRK0XmYEezh7Ue60oBK-PVHrfLt5lPkx3DYSkEP1-vM4X1pq8WMpa9K5iIbT3nUQU-rL7MA575RmaDrtFgpSuh_cJuUacC1hvkq62sh1VrVHn4jCfQ6LrI53Nj-oOFHx1C-bP6Acw_Mt0XIJozCU5p2xuFdZhyXvSEByQ-9IOS6dcjzAVbB8-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش بی‌خیالش شو نصف شبی بگیر بخواب، اون بی‌لیاقت بود تقصیر تو نیست که، لیاقت تو خیلی بیشتر از بودن با اون بود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82932" target="_blank">📅 00:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OngZYvSns3POk1GgSThoUpuUFJww2vCcqMP6KS0TNdL95jd0ud31y6qbWPt6wSGwSqnwfV2mWyA19REGXUVqEtOdS6XnDI__3LEAONUXXA3V4PzKbSy1Ei56I6zpBPocJiOyuvoBFtGie-IL9-fTwE8KEBrwbpDEpihb5MgbuxwzTD2HtoxLuq3Hbz_gflHHXB72k6aJ0Cu10URTg_ukTDFqFdggtRGXCz8_QxOgfh943aFcc0X0SmSvjIynSbsy1zQFJu3pZ3fpLZgE9W9PZmfqektaBNaaj4zvPgoWzY3mQj57WEW36KlAMb7eLX8WFRJq-v9iX9rMzZSppFY5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۰۳ سپتامبر ۲۶
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82931" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf4r_mKQpkKrxvLskUYNVp96HCWkSTFu1KjpjhVAsBFq6yn20QAQc736hjYSZ1VzI2rcSItjwR3FuWYr52c2G092MyZgs4TPmcz8DRfK3aDa03knkH_nnFrwcw_OHNlH7-k5zAF5ptC8FflTAp13U9CFAtF_Z--6VqsyNn2kV0pQEsvIPyJKgnOx2Qtm0UiSjsyQZdy6TpaAxVyRQCV0y1ijqIZ4NLup2LJeFzoHsA8rUr_933JZ4VDNbpxZTCGIDHAaqPfDcvugdSNSKfO2U3OEUlb0hrBcx9gRb25JRmxOFyg-5oyCNkVUfcZ9K0RuPNLmkSAH-Nsbcqr1M3gaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82930" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود:
عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82929" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0ZO79EdjwmRiyIOvhEDOuvnaPnGphZxkVDnvuoFVG6OXky_MSO7wapY9CJpsui3yKM4_OYX3Iqk4ielzx_yb0swr8cl4u2PlTswI18-2ojeIKUbVReI2wdDHfuYztP0INCbIHaznrSNC6tJ8iJmwksBaMDiGCCiGVgEtY3pM8pCAePneWYK9P9wLOq0rvYgjpNbcCqE82FsvwhbwPJoD7ILs03VQzU7YxoIkACkVsG8S3-O248SgUSir6KqdnFsGdhJsoTknPFHblO7zjuNu0kLrkky-jCxIwfl23q7Mnbi-yzGclfjhNE-jB546nQ2ypuFJViesjq44xqo9dUQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این پزشکیان بگه یه زمانی همین روسیه نقش آمریکای الان رو داشت اندازه دو تا اصفهان از ایران خاک غصب کرد</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82928" target="_blank">📅 23:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پزشکیان خطاب به پوتین :  قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن. حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82926" target="_blank">📅 23:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82925" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لطفا موقع بازی های حساس دنیای فوتبال، شو های مهم و حاشیه های بولد قیمت دلار رو ۵۰هزار تومن تصور کنید، تا کیر نکنید تو مغز جوون ایرانی ای که تنها دلخوشی هاش همین کصشراس اونم چون دلار گرونه نبینه، نکنه، نگه و...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82924" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سیگارا وینستون جدیدا بوی پهن گوسفند میدن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82923" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ4shZfqbWD0xUDHM5s5GmQ9szD2rrsJE6aIDaKCafqEHMhE9vFnjCCS-q9RZYuJcYx2tSHGcnX5PiKeR2KAF1yCEf4evq-osdRTDTDTDAe7IetFjkpfx8oHJEVBpxHnisjIWjBJv9YuKFuJBgGwKpx_DAxTVYSNhZne6PxPw4FgwAAJyOwNOw3IywNIP6xLr_L2l2h2nTyVdjxxFjN9kPwnLC6nkHfbZEP7ixG2vW2eE0n3wI5YnaoQQ1VN9rItxMb9ERdTgBcGzWWwdEfWWbO2faRd2wJJvRX_ABHy37rhF6WJg-L3PVI0zeIrFICDW68oxUfj51bAjzSJgUP0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUUmHemxe9lO2YCx05-JXbKxoMIc3TIOJ6TUCvyIA9kSPcRWclnqkbgXuvdYb3k7hIJxRY-P6LB2nItdSOit7c0tbw_cZSPJ-A6NgRqOV22qmq1c-QykxSOimJqV8jwguiqX2bFKEHC_HLNKlJym4uTKwakkd70B9Y-vbosgMRt9JPw9B7Imd5cXitrSrJXKI4kmu6qcuaeC9k6LJvv8xkMG18zITk20Q52JzylgN_tD7y6mleWqGhQ8wFTYiPEvP5R9MF7mHk0ASgrzPC31iukzU93LZ3fgsiWEKUyn57M55nwqpn-BSZPd00gO6Op8k-FdoZi8oMsX6E4LzBi_wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید لنا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82921" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خلاصه‌ی صحبت‌های امشب دونالد ترامپ، رئیس جمهور آمریکا درمورد ایران:
تقریباً سه ماه پیش، گزارش‌هایی وجود داشت مبنی بر اینکه ۵۲۰۰۰ معترض کشته شده‌اند. و اکنون می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر نیز به این تعداد اضافه شده‌اند.
به نظر می‌رسد نزدیک به ۶۵۰۰۰ معترض کشته شده‌اند. تنها توضیح این است که آن‌ها مورد اصابت گلوله قرار گرفته‌اند.
این رژیم روز به روز ضعیف‌تر می‌شود و به زودی به مرحله‌ای خواهیم رسید که دیگر نتوانند به راحتی مردم را به قتل برسانند، زیرا فکر می‌کنم مردم دیگر این وضعیت را تحمل نخواهند کرد.
اکثر حکومت‌ها نمی‌توانند این‌گونه با مردم خود رفتار کنند.
در اکثر حکومت‌ها، مردم تلاش می‌کنند، استدلال می‌کنند، صحبت می‌کنند و سپس ممکن است یک تغییر سیاسی و انقلاب و کودتا رخ دهد.
اما در ایران، آن‌ها مردم را می‌کشند. وقتی مردم برای اعتراض به خیابان‌ها می‌روند، آن‌ها را می‌کشند. آن‌ها با مسلسل و سلاح جنگی، درست به چشمان و سر مردم خودشان شلیک می‌کنند.
خبرنگار: اگر می‌خواهید مردم ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم در این مورد حرف بزنم. دلیلی ندارد چیزی را افشا کنم.
یه سری کصشعرم درمورد حملات محدود و تنگه هرمز گفت که اونا ارزشش پوشش ندارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82920" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">چقد غیرقابل پیش‌بینی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82919" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">0.000000000001 ثانیه فرض کن لیگ ایران ببینی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82918" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این دربی با اختلاف بهترین دربی ۴ سال اخیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82917" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چه موشکی ول داد یاسر آسانی</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82916" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82915">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82915" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPStDjwnXbdoE0RJfkSqfTthSrk1aSroKOuzN8gbhydl2L9RfC2mXkpiOyXVd3cwyfR11UXhe-MvaVPY0NQr6tC7nEE25Tjytzuz8mPFy9mT2V7sKh4cgoIlRhafLeHsif0iC9HSgJKDIruiKLRxj7e6p-zp2ysEBl9S-geV0qPMJAMwUDk1kvSGm86rk0Cmj6qFWPqJkB4A25YJnlf7EBc4VzgZJiljVAsb5OAa_tYEeMMw5zLgC9et1KtBBpVVQ6ffQPsMDjajht66eKvPNH7Lx_Hg70m3TooNaZT2xZ85n_1HqFteZ71wlFFe_EBGy9UpGNX1z9g6_65q1Gub-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82914" target="_blank">📅 20:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHI2BZ2IB-t2YnwngJsfn5G2vLSN7K5QLJmDsQfiS1vy7xU_vqj1xmlf_lQ7PAoyXzVvFx85gLpmYrdWu5sFTn9LlqEDd7gTQMQWBij-NcjzAvr23SxL4qSRsZpsqY7lqx52fO2KotcMTzViSaNjQmCUvqeV-Et8D6YG6OHI06fegrYsNzAgZ0EmusjC2PEdnSly8NPFH4tvJENsUxpAAkOYffI3wPpjzhILnlGus3iuWC8fcty-X1aBnkRjEYmL8t8R44SKcIJaaRjSsWFrRlfYcSl0QwRq-jX26T22Dinf7HYtbKxNhIXrIcVWsp3dWDqWrHGU6tHKomk3hAzPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکو ها جذاب تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82913" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1R8k7jgBe5gl2Ut2yaYzxhWrlhWVduXQ82CcH6JJQJPa5WzzDl2SIe8YWhBlwjfNch3luXTcQ-bc1GqdB8DHSxirfzId7vOSsTuUIh9QwxbsRCl7E2Vvlg2ins9_bj3SfPdTK4pV32KXjTjPkJR13DuQ6DY1zdBlvBvUIzuQudqb29YjmW6HZ7o09hGb7nOvI2yEEQqn_kpzeJuACakG_IH4QMmXqWD3Kwp9rAhXwxCXo4gpt8Axlmf2AZtv9wrEwlOfd6WOxdvJIoKw05d2PV75jjcDCmPnUTUlq9oGRySGq12y9q_rJFCgBwy13dg2-LfTOhuhkx9x6j5VaCcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت استقلالیا از دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82912" target="_blank">📅 20:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پرسپولیس از کون آورد که نیمه اول مساوی تموم شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82911" target="_blank">📅 20:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بیرانوند کص ننت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82910" target="_blank">📅 20:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خلاصه دربی تا الان: آقاسی به علیپور میگه بیا گل بزن علیپور میگه گوه نخور
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82909" target="_blank">📅 19:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">علی پور
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82908" target="_blank">📅 19:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">موقعی که پزشکیان زنگ زده گفته دربی باید مساوی شه صالح و آسانی دستشویی بودن فک کنم</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82907" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4l18EuNhLlUjDSNlafVrSELrU1X9F8y2jRIuX7Uo3JPJHKMcCbTFSk8iGlFfiFHTARuhW86grVtsD2QzSAnlMki7EwD6VSp2akq9ohXavRkRQZotdK4rQ5f0U9e0jp5Rl9XFPVFiDyWe4Di1Z74xz11bT8Ah6F6DwS0MoYfO6h3Fl-k1KyRfiS0gCYjXDHa9FkFR69qOoxGKlao-B95RYzmv12Olld6qdtC_P3vSjE1oXR3Hf-5M3wMtAyfoqmo06r3X2T4OhNhxHl0Kgh8gjD8F6Eaqm-PowY_29KjyDEEiHlHMtvkyueUyjxWmm0aLVJWSKCiJWkzCtEH9xWttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا مناطق خاورمیانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82906" target="_blank">📅 19:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82905">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد    YouTube  Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82905" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82904">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0MBZmcxZve3stQplQDDjMCldlrLV_-dQBMzg_TBuBk4wZHRo__t4PnZU_I9JTT1GquP4SIa_1wm5iZ9FsvDvNm5rciLa__WCPXP5-OOj8MT2air09Mf39yYQb0V_PFNOaGB0S2Kuq9TZnRPmxmVdrwYLYojmeC-WA8CayK9BShCHB8mObC2sUEauSdRUJvQJUh7IKwyutXTDsYRbd9NLcfJjfnatw2flmZmPC-HsXLJR9gEXo-6F5Z1JDCWsCS5yw8psvluXAiTvBJqSLrqps06_Slf9iNQ5OPVPmCIkHtfzPm3FmLnU38Oowo5K2nMnJIIDYisSQIuvenc6-pZ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد
YouTube
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82904" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82903">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آرون جزو معدود دلایلیه که رپفارسی رو دنبال میکنم هنوز</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82903" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82902">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82902" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82900">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpXX7miqEfZZZlt035OwmrU1eorEG7A7O3IY28bx0tbRh1PJ6aYS1J_xTmn-JKMuxgEmzNsLvpuYHgUiXeXawBrqV87IoXOw3lEDvIcI3vsfHcHRk0Smcxn2qtqanYN-TymQX1TWY1wruxKAaqmulArJJBBX0uiv6AN-gD3Lu90Da-nFQ7cjuenVLaDQh8v0843DX9heSrzyMlykCR8l7pNqQXBiO7jyDRn5mKrBkbkionlktjdk7HiU4I13lkxwYJdq-XmqOGQjt7MJZ6tO3Mzv0vRVpXESNX9jWQ2U9QVLp1U-hYiVVIAlfrVpm29XmIx88yFWUpVTTbcOeWvWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ln2aC5VlLH0Cp9Sk13rSeGRer0cyRgDc1DDstZQGc2o4UiEbNx2Sg7luUJrXsRhzaMrGMEX1ggMdbtfRR1rxmqMoONpkg5SNv3G5g5X6gIfzrsJ5J5vmw_j0DBSWdRP2pl-qtUGUOfXp2QXv-xJRnabNKOXdJRQfxsNo1ZSB2-8WjoNoIrzSo_-gS8Xy0MYd3z5tvm9QTU5QnHEaIc7Z88eo3I_l-otiHq3qMTkLMG0LJUiPiL1vmmDpjm0M6aURdXI5Lg96YLRkDjOttHTS2_dybN4_PLIN82PydBwSig90ArTGQJ5ZpF0R4ilBhtZrJFT4pu-hqXtElZtKuClNiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82900" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82898">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جدی نمیدونم تا وقتی رافینیا هست انسان ها چطوری میتونن فن بازیکن دیگه ای بشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82898" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82897">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_yaT7EA4T6BwUxinV5fuE0phZVz3zL3dUU6Ut0QK1ySo85IOfnItWBXvJkRIHUXhJ4P_Lm_boO3aERenWHif-Bv-43jE8cCOWBSIjuuSziWYAbgueOdcynrcg7oa8tFgSmuDzswsODJq9x5fWwdvi0hBhf3P8BvZ5_gxE1uHbCqozTJ3ta86ehlmmcKiGV1hM7tKv87vmx-KwXig_DjnKAhYB0Ds4PyNQfgMQp1eQY0RvcSb4BFfHaw9jNVfNvR6dIhxi2GtbZ_PDlY60e88ul3EmoXhAfvhJsTUdNpsXFfmFnUG4T0uyiyCdAYKEUdth3yah8Y8JrWcS74BS23OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82897" target="_blank">📅 17:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82896">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دربی ساعت چنده بچه ها</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82896" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82895">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خدایی چطور هنوز فوتبال ایرانو دنبال میکنید</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82895" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82894">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82894" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82893">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">شب هالووین امسال آلمان قراره یکی از ترسناک ترین شب های تاریخ خودش رو تجربه کنه.
کنسرت مشترک عرفان، ریری، هیپهاپولوژیست و ایمانمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82893" target="_blank">📅 15:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دلار هر 10هزار تومن که گرون میشه ویلسون 10تا ویس میگیره میگه "شما رپرای اونور آب اصلا چی میگید چاقالا"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82892" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">امروز در کنار دربی تهران، دربی شمال هم بین نساجی و ملوان برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82891" target="_blank">📅 15:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82890" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMN8Mr7TkHBU1Erv4uH7ACLFzGLBZOtvuJqdBeeAelN--Gnh7yw41ESIEsC6VFdWinfK0qPhCSyMkBL0YGLSLy1goVKB60us2pY_vMZdvjqEa_CePQuoP3Yvo8ESudL6h2HMwHQtH-fE6U7orZHkgyXVHNmFqd-NKH5-sgZ4UfYhNCc3lfmkNWBVC0iixcLHDfr58SyEIUsFqTeBe2h9yqKhBlprB96WaCZFY0IL6k_Yu0vJYjRPjP2FlkQCjt2bTXJ05Y5AEa1pZe3xd1jJmTccnH5cEvsQ70dXV4xUVWSnlaFFLKlW7sCabJXedokWRwwo_jes0hnUyH5bZK85tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82889" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82888">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فان هیپ هاپ بابت تشدید تنش ها در خاورمیانه ابراز نگرانی کرد و خواهان توقف حملات نظامی شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82888" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شاید باورتون نشه ولی زمان اعتراضات 401 دلار ی چیزی حدود سی هزار تومن بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82887" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIQEb_g0O1i3UVO9TbRORbCMo1sycVPM_6NewwRF-c0rbckJEazPAix3AohU-dxo2LYDP3OAjQrASLbRa4x214ev_rSss8sF2zgr718OyGKQtuoPWdrshbmfMUEAb2tvueZsivUphw3fg8Wek7HdtIMy0hFlJFMRfRfKv-a2XwbDRO5oMFdZts4Qt6DJRKqgB7C1RZAGKG9JR2z4o5jrCRe7GeHbKxva1v-33usJQSLIRSVKCEEoMgjZxS4Co2WpIhZqPaJD4YmHvsoEVncmQpIYbL4nECc0Iuv2OLopiCHKsQ3avhN6kP_I3fHGwq4X5kiFV1FKFEG3ZtdxGqmonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مال دیروزه امیدوارم الان گرون تر نشده باشه
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82886" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnbalF5gLpFqYT45Csn-UJbmtpF9tJun9ExUzERcJS90Bl31uN5Loh-V2fT8Wuha1KoZ5x-uQV2PODFqST7hs1B9SsG_412MMb-lvgggHs3nILpwyZyNEGPIxmYj7GHdd_1m2MlqO7SHkj3WHynx1U8qJgeSHQg4rlaJq1E2yLDS55iKulzRMHILmdMDlN8WHprggLfIX92PiqHiN-arE2y_fP-NBmE832xtInfpCIQy24yAiAo3Q0QUXdIm1uEpf1-CiQTDsPsr3c6MdMvceuCVbNQ3pJlVBHwzlyLYEZdvfWbjzTPpAUn-rYO6P7lFgaDunmctvDUAn9IeNoRj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان حاج‌رسولی‌ها و آرتا میرحسینی به نام "مست سر صبح" ریلیز شد.
SoundCloud
YouTube
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82883" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دلار 222</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82882" target="_blank">📅 12:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
