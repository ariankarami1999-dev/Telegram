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
<img src="https://cdn4.telesco.pe/file/FXi-aLiJUnzbmwAVwmdgR_u0OlQUW3LjpWqTzckKzWnA5WnaUiFBVUR33zGOrXc6HNTk8rru46K6xUtwVuZuxSp5mqGc1jmSyg0aTwAZqk7Z4uNqw1hgfc0pW_yfcH3w3jSmlan7Rdw8BAPoWZpRhxsWHdon1fNZ07UhWesOpDbiYrGdwCTGaId9I6oFZdALxcGAFvHkuEHmoAtwefagiQnj8cvKj6axjJn5-NOJIBgyXJHBxtYPJoN94BSRIf4EWgnHX7YSfKAIyiSuXQvV_jL9aq9FwlLqIRYy1_I9vT26ujeSVM_ZlrrTZ9wYHaqoARb-C8OKggcQsFGj0VrZHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 09:47:03</div>
<hr>

<div class="tg-post" id="msg-91540">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXTUcpCNuSEzgPRLAcYROjpKQ6BTeRvkT9u7_M1kSYGd-JpO7Ky0URwoveMLd1SdUIT6wc45RYzkBdHajauuTHY7OQPWlA5d1b0AMiuwIggZj4tfhWqRC15zS_fBoeGhTqV1-8RXFU5IJHCDD4MA_JRCzYfWT2kYnPz00EXM-i5cSr_C_p3zcOEDh1ew_fFykLRnKeWixkiwYm3XHQKQnlHob_zpLykRnNVyIBYrH7k_K17Al5-S9OUyIgDkQ_yW681XREJ44VwJ6Mq_c9gUpBlw1vVBWu-OX3G7GfiB19llimp4-lR45O9d-fxjOnhY14MwZO5PA99qs1JHLSSJew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 818 · <a href="https://t.me/naya_foriraq/91540" target="_blank">📅 09:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrlOIp0fO94K2YU-DjGs-_QVf7vndQjgr48nTM_2b4DCg9lsaqRR9Qu0wI7EFsh3vJqruSil4RO3D2rFJbS_ydQsW_yg_PfoK-UdGbdIKnq-9Xdw_OMKQve14h7XNBlR8btpWBJ1SA7l6YMeTazsbOOwVGas88GXm-qhTRgP6T7eldYb0_3QIv0pnJEnlP8ZhRuI7CWZvxYzZHBm_cDJHL3go8vOKz3nYYHOALNOqcCB4Ol7mEfyedqIKyxQweSwLcxslol_nVxnK2HXraFvHBIUrcySUn8tuXQ8CEyBVs6BIvODATovBGELn4wT99w8VtTlaLJYuEg2Gpe_17gmYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l-fymRgLoYVpa9mfvrwDjdNPI84h7RG2vldtneBc2qx4NKGLk-llQosR8pe_5gHIC0fqRvibSH9rmAH0H5e6MY0wzZHuc-IvqyCoEFb_B8GcGruzlPLm0f_ogahG5DL1rAZaMkKoiYkLI6FA6hWFkA6au6VzSQsBMmlWMvHHKxyUH_u2ikuSOuVfmGnmzbcOcu4VJ2BQrp5JGqjwYklxnuruLc3yKILK393q6OwYOw62kRa4SrIqHYZiFvpTBtgVP3BgpmB6Hd6tXEKly5EvEXQ-HRiJDHImex_q0TAxToYCuaAetduy9vroaiyprXoeXm6BGJhgWsQZmEWJBixkKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الصهيوني يعلن رسمياً عن مقتل جنديين وهويتهما إثر إنفجار مسيرة في قطاع غزة.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/naya_foriraq/91538" target="_blank">📅 08:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇷🇺
انفجارات عنيفة تضرب مدينة فورنيج الروسية</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/91537" target="_blank">📅 04:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/91536" target="_blank">📅 02:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات تهز جازان</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91535" target="_blank">📅 02:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
بزشكيان
:
-انصار الله مسؤولون عن أفعالهم ولا يتلقون توجيهات منا
-سنتخلى عن اليورانيوم المخصب بنسبة 60% في إطار القانون الدولي ومعاهدة عدم الانتشار
-سنلتزم بكل ما تنص عليه التزاماتنا بموجب معاهدة عدم الانتشار النووي</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91534" target="_blank">📅 01:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c28a1313b.mp4?token=Gt4S01oOMM9itzUy5pK9sYv5XW9T2xgWZIIkanKYAcV55THJCH4Z-1uqw2t3O7R16GfTHnIJjgf3BC2M_gpY7odx257qxcgEvYEFUg4UrViE_xtj82Mc1BwGBUS_G-wfKeYLHIuZcg5BvwO26QlawAfj4Dt_refG5gxzH4SSEmBxznExZpu5oAzbXzBHGe9-0RjZ7g5dGRn0ppO9BmR63zzeoT2CkVqEDLJwvpYWdpKF9F5Qqo2h5TEM5IILKBPZ7tXkhl4OUsojUwPg723j6WiQ1rn8p1Z_nQY4kIsvy2887LOurdFHlFsN9wP1vfOOR5WGzlUyxPn1r2EbGRFFCCJXbd4WbPCe_P0ypVFTvEHYNtfZoDYXX6Df3s2mhzJEyjC-fPivjZazQK7OYtaJGlt-VXZ5ZmjZZX9IXE9edalZBw5HAkTaIpngZf64E6FUUX9qW-QqQ-JA8eisfIkv1cVD5IddgMpAEeGJfZSYsyD_cwHG9AfunWl-kZy9pR8E8V72oJ5E7JswYq68zCfYYrHKGWXZGX8vcgfl-m_7bGeQws_Etms_X4MxpCqQdJfsmFeSdr5WgFx8srI1FGE4v99FzUaIttRRcw7dO9DViWnm_wHoQFeRRWUnGu-PWwyNfvo8tX0luSUXw3Jprn91NMBe90HsMwMYKpTkWQb8s6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c28a1313b.mp4?token=Gt4S01oOMM9itzUy5pK9sYv5XW9T2xgWZIIkanKYAcV55THJCH4Z-1uqw2t3O7R16GfTHnIJjgf3BC2M_gpY7odx257qxcgEvYEFUg4UrViE_xtj82Mc1BwGBUS_G-wfKeYLHIuZcg5BvwO26QlawAfj4Dt_refG5gxzH4SSEmBxznExZpu5oAzbXzBHGe9-0RjZ7g5dGRn0ppO9BmR63zzeoT2CkVqEDLJwvpYWdpKF9F5Qqo2h5TEM5IILKBPZ7tXkhl4OUsojUwPg723j6WiQ1rn8p1Z_nQY4kIsvy2887LOurdFHlFsN9wP1vfOOR5WGzlUyxPn1r2EbGRFFCCJXbd4WbPCe_P0ypVFTvEHYNtfZoDYXX6Df3s2mhzJEyjC-fPivjZazQK7OYtaJGlt-VXZ5ZmjZZX9IXE9edalZBw5HAkTaIpngZf64E6FUUX9qW-QqQ-JA8eisfIkv1cVD5IddgMpAEeGJfZSYsyD_cwHG9AfunWl-kZy9pR8E8V72oJ5E7JswYq68zCfYYrHKGWXZGX8vcgfl-m_7bGeQws_Etms_X4MxpCqQdJfsmFeSdr5WgFx8srI1FGE4v99FzUaIttRRcw7dO9DViWnm_wHoQFeRRWUnGu-PWwyNfvo8tX0luSUXw3Jprn91NMBe90HsMwMYKpTkWQb8s6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
العراق يستورد أول شحنة بنزين عبر المواني السورية باتجاه المعابر الحدودية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91533" target="_blank">📅 01:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAk9DnZRRGA0FtRk9QRyzt8hAbijuUwaAOqIHjA3eubJxA6iThFBRs8RFNv-Wq1Wm7EkXvYvZqIZSnpjfT8foL_OIT8IQ2TEDqLKRFtpOEiM0yebeoOlUOJpFFnqK8ZcLIdHdF8flBYobD8Ag9HRiAOoEIeY9hd3pImAMxoCdXoSaI7vUNPMs0TGBOLempIpU4iLSKEVn-xLDVphLAsC4JjXVPTpzmtMqEhA0p-qiHgKyR5z89RiEO6KdEys6C-aj27XnBHvz3PVzSqVtGm9kOhVYoZ4OztrN8QIe5xajKHYRWsisnfmZHvYy2AxG4yL0OonN4Kl0QE0eUAnvVOZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lemijTVTji0TmLVF3vLZDOqbV-VfHH4eK4hYypPjENn_x4adyjJfdkhuLDct2SSyEfHkXPXppkxzjCGUkp_krMjifxxFLsHSNClY5ytRcAQOOP6-mHkGHfa0SMTESzdnq3CB2yfMfv_8Q69bg8ljVgVnwJAv_9tThu8tZP0iyjwXdNIJsbPP9ukjyvb-cExvUt12sWsyp5kEFsaU7UIQGvMs8TwH2VuJtxb2SDwHlpwcttin6xUi2I__chdxwH2cl1lnh19DsikfVOXd7jFOtW0FKSfNLPdJqHQeSllCnjKqSkzyepbqkrOgTzIIbjMJqFeIwW3nheai701tLIWOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L8edDrZU7PsvwIA5hWBUGJNJhE4HRrtWxjqEz5y1uag14k75FA9lh2w5vtrs8r5dGKNAspLvSUOjVps7eEfPPN-v8U28_GxUfBLftRRowlwcygVZgwK58bgXD3OF8syuXkso52XpDSuy825E1yVn6Xmdegx3egex4-hV5cssaPGrg6LOXKSP0UHznQYuyy5PLpAFzs9CdDC9f5dC668laltpv1p2TkgxY8IbkfHjRL4OqM2XGgZERzFonygqhOObk2srbUxkZsbw-lWDewvEWR7wj2zTtDU1VzgNAnY7Gc7SmwmgaRVw0Ra5IeHvVmWXd6WBH_Vg9cVt_Ezzl3_9YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TI_hkSjnusGVRG26roB73Wty5WXrqLQqWbnkstOEPKrUwv1EVJiHQypSgbf_85jUnbNO5sR2L54Llp9JYi-0hUuvrStNyCWomxCRb3TfhWyh5RZ_C9p6Tas6czdbMFU0dcgSf8HR-704YTnIrr1KaS8oO_SG8E2b6sCYEFOnfaQDHZszo4ETVIfc4OB2_P-_rXREEeEqOaGHT9p2uO_RLf2c4mrosq-GJn0y9rUsh_nwji_cvg0V0yPssi6j3dV-U9JpghsnGbUrLr0z7XRtcDFVlRMZxeDXcFHQk7oH3fv0j3u9nr6fnxCuSb3RNXiyhlwTFJQoWG5BAS_rKzuQQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
🇸🇾
بعد فصل مناهج العرب والأكراد في سوريا..
نظام دمشق يبدأ بتوزيع المناهج الكردية الجديدة على الطلبة في شمال وشرق سوريا وتتضمن المناهج الجديدة أجزاء منها خرائط وتصورات لما يُسمى بـ"كردستان الكبرى" تشمل أجزاء من الأراضي العراقية إلى جانب أراضي من دول أخرى.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/91529" target="_blank">📅 00:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇮🇷
🇺🇸
رفض مجلس الشيوخ الأمريكي قرارًا يهدف إلى تقييد صلاحيات الرئيس دونالد ترامب فيما يتعلق بإيران، حيث بلغت النتيجة 49 صوتًا مقابل 50.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91528" target="_blank">📅 00:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91527" target="_blank">📅 00:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91526">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
🇺🇸
صواريخ كروز من طراز شهيد ابو مهدي المهندس باتجاه سفن معادية بمضيق هرمز</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91526" target="_blank">📅 00:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇶
🇮🇷
ايقاف حركة الطيران المدني بين مطار النجف الدولي والجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/91525" target="_blank">📅 00:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇾🇪
مستشار عسكري من انصار الله لوكالة فرانس برس إن اليمن سيهاجم المصالح الأمريكية في الشرق الأوسط إذا تدخلت واشنطن عسكرياً في اليمن دعماً للسعودية أو حاولت السيطرة على مضيق باب المندب، واصفة إياه بأنه "خط أحمر".
‏وقال المستشار إن اليمن "سيغلقون باب المندب تماماً أمام السفن الأمريكية" وسيعتبرون أي مصالح أمريكية حولهم أهدافاً.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/91524" target="_blank">📅 23:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPB4wpztDLGCazgoH4lEqnj4QKGdOf9xlVu-yJsTvcyO6B9VVekaPl_xRyOsuzFr5j5XvDrhAVNHBJ0ABGIFUxdRIHFU1DR7Y4xIa7Mte7WXFb7hGHtlpsz1bc2Q4q8NHMds-GN6pSlQwFx2Q02ywZQOZbDpz69fprqNtMXKLiYQSPchSXSuA2ipBu9Tq-NOTKSgOy_zIISQEl-jRpQUKlrC_JYTcehtGOvfNit-kMxBWu5p-T_hp4vnHb5R8VkqvBYNQ2o5CnCdgQBNY8sqLpsDD8c1QKCv1HvKJr-EXUCxalhXhxG7HJU8MnPLhpJ3pqzxNag4x_awXWe10jdd3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
‏
مفتي السعودية الى قوات التحالف التي تضم اجانب من الديانة المسيحية
😆
:
‏اعلموا أنكم تقاتلون عدوًا، قد أفسد في البلاد، وفرَّق العباد وخرج على ولاة أمره ورام شرًا بمقدسات المسلمين ولكنّ اللّه تعالى لهم بالمرصاد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/91523" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇶
القوات الامنية ترصد طيران مسير مجهول يحوم حول مزرعة شخصية مهمة في منطقة ابو غريب جنوبي العاصمة بغداد .</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91522" target="_blank">📅 23:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b3ff01b6.mp4?token=agrNhBj3nbZrSSIfT0c2ArzuQ262VrIi37Ke8CughOQjNTrTmqJ8fBt-y64l6G5J-M1tSMoKF7uyKw_VEophjnaLKXwNvO4u2K4aB8IzN8gkOLyKMGquaFzZfVZcZfubJ1PeP1YYNGffQp3uEno6zrlStX1n5yxD7qQQJyr_3TTJObU3bpLkB5KZc_Qd4oE5uMP40W_S-QdCEU_mp3IrwumEuxnCJ0Pr7AdUruQGkMLy1TvW_HWFvgBdpk93Ut9jbUqnCL3rIgDw7UvW-G_emeGpfVpYi5tzAiKO6vas76z9meinSvKFgpTPJLi0AHfGjSKZG6tXHmTjULrJ-Q2ZxEUz8AJ9eOGZJL6a47iyZ7Sn93wiHfirkCgA2XJbSIWg1q5UOgNHoWq7HRZBYJrmw8FwYO0MxetE4GJcwj93ZeJ01b6WnXfe_YTkPm_nkcN7qWlYIp0QaUJWuQjBmQVrTi-FFI_44TdeaJZK52XBO0RqJB8xJvJ-heNqNlPuj7LlsCZVAuI2C4uKuZP14QEEgF8HoYVuh5wd5-9Id6uBkafXh9Wmi2x7ItoXho1W7FlhOM9mspnmS68pVNiXGZsfJZUSiJYfdTZJ0HNXxFGFlVkQkd-Lto2_EBffGKqir2zOMFFr1qjQd1cYDA2qlgXlR2SgVufdPCY0XqM5IVXwPc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b3ff01b6.mp4?token=agrNhBj3nbZrSSIfT0c2ArzuQ262VrIi37Ke8CughOQjNTrTmqJ8fBt-y64l6G5J-M1tSMoKF7uyKw_VEophjnaLKXwNvO4u2K4aB8IzN8gkOLyKMGquaFzZfVZcZfubJ1PeP1YYNGffQp3uEno6zrlStX1n5yxD7qQQJyr_3TTJObU3bpLkB5KZc_Qd4oE5uMP40W_S-QdCEU_mp3IrwumEuxnCJ0Pr7AdUruQGkMLy1TvW_HWFvgBdpk93Ut9jbUqnCL3rIgDw7UvW-G_emeGpfVpYi5tzAiKO6vas76z9meinSvKFgpTPJLi0AHfGjSKZG6tXHmTjULrJ-Q2ZxEUz8AJ9eOGZJL6a47iyZ7Sn93wiHfirkCgA2XJbSIWg1q5UOgNHoWq7HRZBYJrmw8FwYO0MxetE4GJcwj93ZeJ01b6WnXfe_YTkPm_nkcN7qWlYIp0QaUJWuQjBmQVrTi-FFI_44TdeaJZK52XBO0RqJB8xJvJ-heNqNlPuj7LlsCZVAuI2C4uKuZP14QEEgF8HoYVuh5wd5-9Id6uBkafXh9Wmi2x7ItoXho1W7FlhOM9mspnmS68pVNiXGZsfJZUSiJYfdTZJ0HNXxFGFlVkQkd-Lto2_EBffGKqir2zOMFFr1qjQd1cYDA2qlgXlR2SgVufdPCY0XqM5IVXwPc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنية  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {ذَ ٰ⁠لِكَۖ وَمَنۡ عَاقَبَ بِمِثۡلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِیَ عَلَیۡهِ لَیَنصُرَنَّهُ ٱللَّهُۚ} صدقَ اللهُ العظيمُ  يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الإجراميَّ على…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/91521" target="_blank">📅 23:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91520">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6411165378.mp4?token=XD2TmHR-gY0bqAafKBiAHWzXQerqKOyKg86CIA5zzHhsOjAaAn2r0zawHk3R-WuitSGZEeQOqEwy-TI9reZ6JWxzWO2wKp-dMtmiWcy3sp1GZDKubEbCGkYz1KNSCGPTmcnNpNcW_dwodV7uuWXzTioglq5L3dvTdkblQjF7sFkbdQYZXRE5KNpGGX2aK7pTya7I50urg1ObUtfDRgTV91fKUFh8sNWYJwIFtQeuHBXTuCwgzFzksVXoy7WP4XQFGpYq2iIap9sQJAuWpBSWm-2DYGi4QqABXDgm7E3uyXE7aP9TlseVHvZpDJbAUYO-5L_zivO3C-WFOdRJNZD46g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6411165378.mp4?token=XD2TmHR-gY0bqAafKBiAHWzXQerqKOyKg86CIA5zzHhsOjAaAn2r0zawHk3R-WuitSGZEeQOqEwy-TI9reZ6JWxzWO2wKp-dMtmiWcy3sp1GZDKubEbCGkYz1KNSCGPTmcnNpNcW_dwodV7uuWXzTioglq5L3dvTdkblQjF7sFkbdQYZXRE5KNpGGX2aK7pTya7I50urg1ObUtfDRgTV91fKUFh8sNWYJwIFtQeuHBXTuCwgzFzksVXoy7WP4XQFGpYq2iIap9sQJAuWpBSWm-2DYGi4QqABXDgm7E3uyXE7aP9TlseVHvZpDJbAUYO-5L_zivO3C-WFOdRJNZD46g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تاكر كارلسون:
القطريون أعطوا ترامب طائرة. وما الذي حصلوا عليه في المقابل؟ لم يحصلوا على شيء.
لم تدافع الولايات المتحدة عن قطر. نقلت الولايات المتحدة بطاريات نظام "ثاد" من الخليج إلى إسرائيل.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91520" target="_blank">📅 23:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e96b19f5.mp4?token=MufwuzkqKgrFpZdV-X8G19vOnGaXWjJ-itDq4uQI0R_vrmC198x7dwSNtnj7AlIecwEIgbIdIO3wWDwIgQcRRgSXRMui7ff3sr4QxK6xCHJOAKjvfPFpWn_Bd__o7_lROg2ilBvpmyl8JrR05HbZJDWWdYBIYbEPwtnWD7avUbWGiOJhrVvdlS-shqX4qyaK_NkK8jtYRpvEfVKpaSpGhqjKTHeaQz0lTkhz3JTv4j-srm8BxgK93wklAlTHVp2aRsa4IbaCUDZLbo2tiG5g-WC8qw4s9ITj92C5dmqZtG5xe_0qI1E5kMIhdsN_3icK4CWGVthW3GXhxsZUz8B4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e96b19f5.mp4?token=MufwuzkqKgrFpZdV-X8G19vOnGaXWjJ-itDq4uQI0R_vrmC198x7dwSNtnj7AlIecwEIgbIdIO3wWDwIgQcRRgSXRMui7ff3sr4QxK6xCHJOAKjvfPFpWn_Bd__o7_lROg2ilBvpmyl8JrR05HbZJDWWdYBIYbEPwtnWD7avUbWGiOJhrVvdlS-shqX4qyaK_NkK8jtYRpvEfVKpaSpGhqjKTHeaQz0lTkhz3JTv4j-srm8BxgK93wklAlTHVp2aRsa4IbaCUDZLbo2tiG5g-WC8qw4s9ITj92C5dmqZtG5xe_0qI1E5kMIhdsN_3icK4CWGVthW3GXhxsZUz8B4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
أنباء عن اندلاع اشتباكات مسلحة وتحليق طيران حربي في أجواء الحدود الباكستانية الأفغانية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91518" target="_blank">📅 22:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔻
الأمين العام لحلف الناتو
: الحلفاء الأوروبيون مستعدون للهجمات الهجينة الروسية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91517" target="_blank">📅 22:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇾🇪
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنية
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {ذَ ٰ⁠لِكَۖ وَمَنۡ عَاقَبَ بِمِثۡلِ مَا عُوقِبَ بِهِۦ ثُمَّ بُغِیَ عَلَیۡهِ لَیَنصُرَنَّهُ ٱللَّهُۚ} صدقَ اللهُ العظيمُ
يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الإجراميَّ على شعبِنا من خلالِ حصارِه الظالمِ وشنِّ الغاراتِ الجويةِ العدوانيةِ والتي بلغت منذُ بدءِ التصعيدِ وحتى مساءِ اليومِ 1018 غارةً جويةً وصاروخًا من خلالِ طائراتِ F15 وتايفونَ أقلعتْ من قاعدتي خميسِ مشيطٍ والطائفِ والعدوانِ الصاروخيِّ من نجرانَ وجيزانَ استهدفَت محافظاتِ مأربَ وصعدةَ والحديدةَ وتعزَ والجوفَ والبيضاءَ وخلَّفت شهداءَ وجرحى بينهم نساءٌ وأطفالٌ وتسببت بخسائرَ في البنيةِ التحتيةِ المدنيةِ.
وفي إطارِ الردِّ على هذا العدوانِ نفذتِ القواتُ المسلحةُ اليمنيةُ بعونِ اللهِ تعالى عمليتينِ عسكريتينِ نوعيتينِ الأولى استهدفت هدفًا حساسًا في عاصمةِ العدوِّ السعوديِّ الرياضِ
والأخرى استهدفت شركةَ أرامكو في ينبعَ، وذلك بعددٍ من الصواريخِ الباليستيةِ والمجنحةِ والطائراتِ المسيرة، وحققتِ العمليتانِ أهدافَهما بنجاحٍ بفضلِ اللهِ.
إنَّ استمرارَ العدوِّ السعوديِّ المجرمِ في شنِّ غاراتِه على شعبِنا وبلدِنا لن يثنيَ القواتِ المسلحةَ اليمنيةَ عن ممارسةِ حقِّها المشروعِ في الردِّ المباشرِ والمناسبِ على هذا العدوانِ فكلُّ اعتداءٍ سيتمُّ الردُّ عليهِ وكلُّ تصعيدٍ سيُقابَلُ بمثلِه وما مصيرُ المعتدينَ المجرمينَ الظالمينَ إلا الهزيمةُ بإذنِ اللهِ تعالى.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 13 ربيع الثاني 1448هـ
الموافقُ 24 سبتمبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91516" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db132f7e43.mp4?token=Xu1ZVSNJSFFIJA1O8ygT3bQc68IGdC5tN2TTUfH3yRFtVipUy6cI8CEZkHjrRQnvooviXfoZ6c_OGgTOq1QN7mRutuuLMfl1lParjPhhOpVamYc0gqSBZhhvhIQ2AuJeJUCgvWNCtQ0dy2YdN0tBHJQcXsRZQB9_Vb2Twm-LLeYTwXOMRsic5ort2ujYeOTnEkBmmHQheP9KmjtFNFr95Qe3KEFkKvy9abSmQPk0pkeyTRw3P0SyCaukiVVqulK2vQmcra6gIKkgjLjAu42TQ1eZ6VTeh_WqjTDkJk_xRKpCO_o2-iLdIxod3jcNNncxUx88HKxAUTEzzlojU7R6cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db132f7e43.mp4?token=Xu1ZVSNJSFFIJA1O8ygT3bQc68IGdC5tN2TTUfH3yRFtVipUy6cI8CEZkHjrRQnvooviXfoZ6c_OGgTOq1QN7mRutuuLMfl1lParjPhhOpVamYc0gqSBZhhvhIQ2AuJeJUCgvWNCtQ0dy2YdN0tBHJQcXsRZQB9_Vb2Twm-LLeYTwXOMRsic5ort2ujYeOTnEkBmmHQheP9KmjtFNFr95Qe3KEFkKvy9abSmQPk0pkeyTRw3P0SyCaukiVVqulK2vQmcra6gIKkgjLjAu42TQ1eZ6VTeh_WqjTDkJk_xRKpCO_o2-iLdIxod3jcNNncxUx88HKxAUTEzzlojU7R6cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صورة الحاج قاسم سليماني تتوسط قاعة الجمعية العامة خلال كلمة نتنياهو.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91515" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9932ce34eb.mp4?token=Rxm-lWmBXsB9WL_2vJLkj3d7AZvipVkQfCvtqb2EFDeTYCjXvRuGgg-XGFAM2bxguu270Cqh0LMnVKE5bcB28h1wJYgRH9xEm1-aoz6kJuVzlR2BipxlHUX4TpwDULdUHQInQPVMOd0d4h_9N2jmaalDwRiLW1vixtzSbAlxa7QVEuW_70z-bQf6QPqWc6iw3lzBuiN0qMcE_ByHWLohi0yywnILZlMrKuJTr33TKiIROh07HvNRCBojnz9WgzsmGGKP9wz-IIII4a2YI7jR3vJgNxzMiczuL4p9LcgibeGjbeuPK_sRsf41ACDVBYUFCZX2XsDI7-LsaVsDODvisQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9932ce34eb.mp4?token=Rxm-lWmBXsB9WL_2vJLkj3d7AZvipVkQfCvtqb2EFDeTYCjXvRuGgg-XGFAM2bxguu270Cqh0LMnVKE5bcB28h1wJYgRH9xEm1-aoz6kJuVzlR2BipxlHUX4TpwDULdUHQInQPVMOd0d4h_9N2jmaalDwRiLW1vixtzSbAlxa7QVEuW_70z-bQf6QPqWc6iw3lzBuiN0qMcE_ByHWLohi0yywnILZlMrKuJTr33TKiIROh07HvNRCBojnz9WgzsmGGKP9wz-IIII4a2YI7jR3vJgNxzMiczuL4p9LcgibeGjbeuPK_sRsf41ACDVBYUFCZX2XsDI7-LsaVsDODvisQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇱
صورة لطاولة الوفد الإيراني خلال خطاب نتنياهو في الأمم المتحدة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91514" target="_blank">📅 22:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91513">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04338c831a.mp4?token=aObyYwZg_fwMPnwIb-_JgMn2zjMjjaeUvdGde2IDABc_S2wlPRJc-d3re6x0gnzyKb7XvUvMUICA1GMtgkCjhDDc5JnCmO8wanF7qigcjGZlWyb0H4dmt-C-fh0YCH_mEp1DGcG3iHdUCIe3_gMwNrirqf_ktCwmzUYjely-yK8RApT0B-fBmWuGqs9HD07cffrOn-H7K9zzrQ75sqy_uXT9Zhtd_iTuy7RgvqqVVCQv6kN9yN1heW9svGgFo9l07bPHT-TwUMH3YtJ2z0jLzpU2QXtwM0YvCMVoHQgY3ALuxTuyL1TcirgBGAP7k8W_qi_ArFgxVMgIntNAYoJ_uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04338c831a.mp4?token=aObyYwZg_fwMPnwIb-_JgMn2zjMjjaeUvdGde2IDABc_S2wlPRJc-d3re6x0gnzyKb7XvUvMUICA1GMtgkCjhDDc5JnCmO8wanF7qigcjGZlWyb0H4dmt-C-fh0YCH_mEp1DGcG3iHdUCIe3_gMwNrirqf_ktCwmzUYjely-yK8RApT0B-fBmWuGqs9HD07cffrOn-H7K9zzrQ75sqy_uXT9Zhtd_iTuy7RgvqqVVCQv6kN9yN1heW9svGgFo9l07bPHT-TwUMH3YtJ2z0jLzpU2QXtwM0YvCMVoHQgY3ALuxTuyL1TcirgBGAP7k8W_qi_ArFgxVMgIntNAYoJ_uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏يلوح نتنياهو بجهاز النداء ويقول: "لقد وجهنا ضربة قوية لحزب الله في لبنان".</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91513" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91512">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
ماكرون
: "سنرسل وسائل عسكرية وجنود لحماية طريق البحر الأحمر.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91512" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91511">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
بيان مهم للقوات المسلحة اليمنية للإعلان عن عدد من العمليات العسكرية النوعية داخل العمق السعودي، في تمام الساعة العاشرة مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91511" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91510">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUI93CSgv6ccYere_b2jJ7qeF_kIeKdufJTbrwXbkBoIH372qyHyjVsls2fYfbQ7yoQsD28qM4J7xwEpE2dm0hHUvPANxMGskW6qTkEnzfqGx7MZrm0zacJCwQx_wYh-S3750FzONpf4NYEhfdHw5cwyPfLJvfYsN-DcIpKF0iOu4TQup4pr5nm_1MHzccttTbZ5vEEey-t1k8ttVyZZ8CiXk0yq4104WDnKbw92a8cAokVoEKfu8iguxYZ8zh0M6WeX_JoHQabXU5BDWsEZLDlMWzXAA5CQx6CtirBPCC-xghWhHfMcBbUphT0pDbFL-Qud0wtRpTHbGjD_Bb3tpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
‏يلوح نتنياهو بجهاز النداء ويقول: "لقد وجهنا ضربة قوية لحزب الله في لبنان".</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91510" target="_blank">📅 21:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91509">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfGbiPYJJA8aWXpG_eCyFgTCwAAexD5BoynlUkDckGG1R_53xEQjIbCNpgZuSsq_8XuduCAsp-xPiET0LVQJ13RMC6ZpX0eWHuvwla7SsUH1bV8usDBwYtfnjvSEoH0siuE47oPoPIwhAX_-vaeZqbtQTs4nCVpThH28QV85GojSn9p9z-ZIS-qdQY2z5whoaB0aXGSXywmLRunXz2u9I3UUb4w5EijFjx8UmsGRIc9RfC7bLLidx8rpGvoGc_fj_uy9C9FSC9Q3TWrz-K_Oi8FwOSmjLMMCG2Ff01IbuknS5B8u-p0_PUBAgooyREqj-gOMfWumtL74CzF1MvYKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
‏نتنياهو: "على مدى السنوات الثلاث الماضية، كان جنودنا البواسل يقاتلون على سبع جبهات: حماس، وحزب الله، وإيران، والحوثيين، والميليشيات في العراق، والميليشيات في سوريا، والفلسطينيين".</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91509" target="_blank">📅 21:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91508">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇱
🇸🇾
نتنياهو: ‏يا سيد الشرع، يجب أن تعلم أن اليهود كانوا موجودين في مرتفعات الجولان منذ أيام موسى.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91508" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91507">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇱
‏نتنياهو: إذا كان هناك أي جبناء آخرين لم يغادروا القاعة بعد، فليغادروا الآن.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91507" target="_blank">📅 21:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91506">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f823df4c8.mp4?token=FWOL66P6GUjG908JQDLtoLn5B1ugi--Ni5EuDiyUwuONrQosaA9jx-vrrhmGDPk7iq4zgV5A6qUuCp2544pXyNEk1O5OAtZH7eJ-K1tk3c5v-Qlnc6tc_ttlSWH77MylqE9ApVslq60idG5tDUIL3VqA7xN46I8vyxryAk_xfdXvhEF0kHtg1hU583gCEu36jcDz2MsNJmemERbBArLQUw-c6eHh_kbUoJ4auCT2Tv9kJyDt_petW2adjWyZ_DQjw35Mg_m4C9xStS2a4SoEkFp0ZNpCjuTpXFGbpC1KR4wc84DDOjbBbEG9pzCG1iKcnm_VOulXkyc5HCKHFa6mSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f823df4c8.mp4?token=FWOL66P6GUjG908JQDLtoLn5B1ugi--Ni5EuDiyUwuONrQosaA9jx-vrrhmGDPk7iq4zgV5A6qUuCp2544pXyNEk1O5OAtZH7eJ-K1tk3c5v-Qlnc6tc_ttlSWH77MylqE9ApVslq60idG5tDUIL3VqA7xN46I8vyxryAk_xfdXvhEF0kHtg1hU583gCEu36jcDz2MsNJmemERbBArLQUw-c6eHh_kbUoJ4auCT2Tv9kJyDt_petW2adjWyZ_DQjw35Mg_m4C9xStS2a4SoEkFp0ZNpCjuTpXFGbpC1KR4wc84DDOjbBbEG9pzCG1iKcnm_VOulXkyc5HCKHFa6mSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏نتنياهو: بعض قادة دول التي انسحبت وفودها شكرونا سرا على إنهاء البرنامج النووي الإيراني.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91506" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91505">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇱
‏انسحاب وفود عدة دول من قاعة الأمم المتحدة عند صعود نتنياهو للمنصة لإلقاء كلمته.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91505" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91504">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ca26a1b3.mp4?token=OAA3ZycGAc9DcxJHltk7r5OpGLiZh_zK2kFce4RONva5lH1MlPNCUiUJHZbOwMW1Y4lF3i3kSs9PnvZ43jN_JCqSkfi-2RBOMD3VZ-KUiGo5VuQvBIbl71bHZaHMrjTmnehgry2D8Nf58WJW-7uo31svhfGCepvSuAbGP8jWAmYlQYjVqk7J-g39nHImZl7v8YUyP_e-WyPEMc6Jk8vAvwgcfgJkILXKkeZ-CKGcIb-ywXda7xRlNJbOhkSM6bG3nOUqyZ5-M253WO6puxyZntJva6SKjFtcSesKETH319cyo3Q7xES9YQkqjp_A5lTcFIBgHxH3hc9B7xgJ9F_56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ca26a1b3.mp4?token=OAA3ZycGAc9DcxJHltk7r5OpGLiZh_zK2kFce4RONva5lH1MlPNCUiUJHZbOwMW1Y4lF3i3kSs9PnvZ43jN_JCqSkfi-2RBOMD3VZ-KUiGo5VuQvBIbl71bHZaHMrjTmnehgry2D8Nf58WJW-7uo31svhfGCepvSuAbGP8jWAmYlQYjVqk7J-g39nHImZl7v8YUyP_e-WyPEMc6Jk8vAvwgcfgJkILXKkeZ-CKGcIb-ywXda7xRlNJbOhkSM6bG3nOUqyZ5-M253WO6puxyZntJva6SKjFtcSesKETH319cyo3Q7xES9YQkqjp_A5lTcFIBgHxH3hc9B7xgJ9F_56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
‏انسحاب وفود عدة دول من قاعة الأمم المتحدة عند صعود نتنياهو للمنصة لإلقاء كلمته.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91504" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91503">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxB7RUUmqc78saS301BSlMQRD_iRDzDtONJwJN_-Pe79Kb_hRRjS0lxPONek-YUzwpoLZlgUzYzAgDxFvbJTYMkfQfx5r-Isi60M3QV35IndXMIFuGCM0qNGWENgXyFtb0qFgymJlZidVBOKEv_1EgpLoM_aTFzh2f6rjzmaMJ7no2xjnLtUSApa-W_SYxE0DKXRunZCkhbCKCHOa69CBES5COf6OdZ5BbOWLN9p2oIr3p48xm16i2Qw0b8nDgpQUC-sRB3xfYokdpMIPJkh6ffWRJsCQl1-kB55RrCHWqqgA5yCPQE-Es-wFvEwmcbqP00kLtuTGxDw67-Qcupj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر بخصوص المنشورات المسيئة لآل الصدر الكرام.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91503" target="_blank">📅 21:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91502">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇮🇶
🇺🇸
العراق والولايات المتحدة يوقعان اتفاق تسليم موقع الدعم الدبلوماسي المسمى ب قاعدة فيكتوريا داخل مطار بغداد الدولي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91502" target="_blank">📅 21:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91501">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/91501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/naya_foriraq/91501" target="_blank">📅 21:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91499">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
🇮🇷
🇨🇳
الاعلام الغربي:
الرئيس الصيني دعا  الرئيس ترمب إلى حلِّ الخلافات مع إيران في "أقرب وقت ممكن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91499" target="_blank">📅 20:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91497">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEr-RltwZrqNd68bsEc1eolzMrLQfwOlAboE9vJfJQYXTc5bs8IVyuPMJMTdfRyJvuY77HxK6WxDu6ovErWn1CJni3aADY2SYPnOG18h1t7lPP7xIKKfgPYYMyXULlQuyVsumS1V94r_GAYHeOQOq8JBc33rmjO5Ur_HAMtznYa3itT2fOl3CNbtaY5GmX-8YSSX540pNer8VI2pVyxZqq2BrOF3Sx1SL7j2rHhqymrZihZ2wAAmjkGSCadgTeoMesRHm5N_3ZnHqXnCNSrH66iEOpnQcrDDMXg8Ks8VhHhw2uSxytJ8mMkGeTUgxjBidTsK7Pn8Api6SQ6BgeYGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb07d95383.mp4?token=qBlmLCYYcXlu2zsaXFE1qtBLKKycBJPS1BD8vRPF6Q1B7eO5vXvPHmiRkr9RP3Y95BMJBXHgoQZbQUHyGiUHT9sORpprrYsz9XZH4SO9ZPW9vo33irr6-4i-xNpb2Ohu7MWvDtJBhcX_A4PbYSaGxybjXlr1DZk3xEAKBe9LdeVS9uEmkToPKn8cgjdBAbAeaYx3zp7g2f9_LNFeHeNVS2a1l1GWRQX9qqMdbl9QUnBVJtgDzts6YWzhb6afB8e0HiDPqNhg7LFGqLpF3nmvXNfEgRgNZFNeJ4sx8jFls7MylpvYxWG1YSRFv3me4RsGkQlcK65ADEx6_5ut40_fWkx4OK2IqnA6JHnntNh250bvMxeS6F5JgljHySSyGf8YZDlEToRSvO_V1lNNcKBhdM2PDodq00Bw-o9_hbCWstgV-wc9vBO-Jk_xH_Aa7Oou3fA6pA19CfN-fBUbH7EhmLUCSRpDnW4DUOeAPNWG3YpuJHuCUfmTp6T6zQDXcHSgr3a8bYb96XcHn51xrbEuO9A0xuYjZmqwoa-qExOVQ2fFObwPEwN0kjEGJP8P5zH86PilPgST2S9azLZLVJXCpw2V1ax7ZcCfnilVlLspix4rR4AKJMXv-ZLgeaHvD288vOjm9FtYJro3zYK4eb4DCrCZIRRzvcANiPCZgvySJho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb07d95383.mp4?token=qBlmLCYYcXlu2zsaXFE1qtBLKKycBJPS1BD8vRPF6Q1B7eO5vXvPHmiRkr9RP3Y95BMJBXHgoQZbQUHyGiUHT9sORpprrYsz9XZH4SO9ZPW9vo33irr6-4i-xNpb2Ohu7MWvDtJBhcX_A4PbYSaGxybjXlr1DZk3xEAKBe9LdeVS9uEmkToPKn8cgjdBAbAeaYx3zp7g2f9_LNFeHeNVS2a1l1GWRQX9qqMdbl9QUnBVJtgDzts6YWzhb6afB8e0HiDPqNhg7LFGqLpF3nmvXNfEgRgNZFNeJ4sx8jFls7MylpvYxWG1YSRFv3me4RsGkQlcK65ADEx6_5ut40_fWkx4OK2IqnA6JHnntNh250bvMxeS6F5JgljHySSyGf8YZDlEToRSvO_V1lNNcKBhdM2PDodq00Bw-o9_hbCWstgV-wc9vBO-Jk_xH_Aa7Oou3fA6pA19CfN-fBUbH7EhmLUCSRpDnW4DUOeAPNWG3YpuJHuCUfmTp6T6zQDXcHSgr3a8bYb96XcHn51xrbEuO9A0xuYjZmqwoa-qExOVQ2fFObwPEwN0kjEGJP8P5zH86PilPgST2S9azLZLVJXCpw2V1ax7ZcCfnilVlLspix4rR4AKJMXv-ZLgeaHvD288vOjm9FtYJro3zYK4eb4DCrCZIRRzvcANiPCZgvySJho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
دخان مجهول في سماء محافظة كربلاء المقدسة وسط العراق.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91497" target="_blank">📅 20:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91496">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXbcaefyWcpYMNxXtXwa7IGP4YGADy4Tu3C0DaUxs8E2RfeSab54rxrWNxREOfkAvvoUaGBw2WQgm3wh_BfwVXYXhOrPq0ujBq58cL_6tPP7JgAGyRpyUGCfBubmh1ETd-y_OxwXm6yJNjrk7meBriTOwyNY9F9HhmfWICd49ZAY7JxmkBALMjnNJnLpukEPNE3xwG2xhiY6rKaCSqDaACx20VvOCpzdlqLcwTr6ODrAgVEPlI7KnwqpgfLYBYNd1fs0OF-W4R03eiGO-EUdPhx-N58kBrC1lng4v8ice1TmhvT75kL3yl88WIS1WSM0j7OTdCERLMiYaq18H9-oxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد للطائرة المسيرة السعودية التي تم اسقاطها بالحجارة في صعدة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91496" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91495">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
انباء عن اطلاقات صاروخية من عدة مناطق في الجمهورية الاسلامية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91495" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91494">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇶
‏
رويترز:
إن شركة فيتول اشترت ​ما لا يقل عن ‌25 مليون برميل من الخام العراقي في سبتمبر أيلول.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91494" target="_blank">📅 20:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91493">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7Ga3F4CdMcAWsHro-_siQ2zYlnzM1ZdQlQ75KRC7jOL1_xpAVKQvb5gwjZpcpSSpBKKS2W0iQrZEYV5BBy0-3gvfxelofhGRZtLvVk9pG5VPMRzw9t_q6gNmUiyrHqcgzCLq2o5HtS_JK_UsquRCcfgaBm5oSKPbz2c8t5115kxRqHB1FLqg1cPConTpYG1hRAz63S0pN1as1QiCJ6CZCwgRgZ0695NpBpNIwm0R7noJVTVTBoQj4IL8LwQ7le8z7jQlHhDXv-6x0uaTqtKiTUfEdEZyT3QWC3m2godwT55pYqInhFWEJmEEPdOJWvoE7QwSL1XHZTomz5jlqoYPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مئة يوم على عمر الحكومة العراقية بين إخفاقات و تحسن ببعض الملفات</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91493" target="_blank">📅 20:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91492">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVZDr4G1zdwoYU7oSZVXgd4sRr8o8SaXjD6dBlyqrJ0J7ZxhAdtWAe229VNF9lAeAnf5VBtqN-Hg3kSnftenIRT-Qm2yDFoXFzHOvgHcehEiYW_RHJJvxgDPf_FPG-Oj4kJvdWNUJeFfN_eqmZPrz5Q5AcxmJTGYmrksWuoEX8LQjrRfb1Aga7togf_uXtINFbjjtQ8rWTc60u8FbG29v28r82L_O-_qTGxDPnbrxYw_Fs4f4tnoviIMuTNE_OX30v16Wy4Q1TDUHzLIpXdjdDYF-imf0j0jr4Dk33fH_RNfqCOWFoPv5tL6rNme31rUbxG2XxzTes077AmCpLhYkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف:
تهانينا لأمريكا على تحقيقها نسبة 5.1% خلال عشر سنوات
🎉
. ما شاء الله. فلنحتفل: لقد وصلنا إلى أدنى مستوى لنا بعد عامين.
‏هل أردتَ إعادة إيران إلى سبعينيات القرن الماضي؟ ألم يخبرك أحد أن إيران ليست مكانًا للهواة المتغطرسين؟ سنعيدك إلى أسعار السبعينيات، بالإضافة إلى ارتفاع أسعار البنزين، ونقص الديزل، وارتداء البناطيل الواسعة من الأسفل. استمتع بالحنين إلى الماضي!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91492" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91491">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي يصرح بخصوص الاتفاق الاميركي الايراني الجديد:
المفاوضون الأمريكيون والإيرانيون في نيويورك يستكشفون مسارًا تدريجيًا للخروج من الحرب، يتضمن إعادة فتح طهران لمضيق هرمز، ورفع واشنطن لحظرها الاقتصادي على إيران، وفقًا لمصادر مقربة من المفاوضات.
أصبح المضيق هو نقطة التفاوض الرئيسية في الجهود الرامية إلى إنهاء الصراع الذي يشهده منذ حوالي سبعة أشهر بين الولايات المتحدة وإيران، حيث تسعى إيران إلى تخفيف الحصار الأمريكي الذي يعيق اقتصادها، بينما تسعى واشنطن إلى ضمان حرية الملاحة للسفن في طريق الإمداد النفطي العالمي الذي تمنعه حاليًا طهران.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91491" target="_blank">📅 19:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91490">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇷🇺
🇺🇦
أوقفت مصفاة كويبيشيف النفطية في روسيا عمليات تكرير النفط منذ يوم 22 سبتمبر، وذلك في أعقاب هجوم بطائرة مسيرة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91490" target="_blank">📅 19:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91489">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610cfa459d.mp4?token=gv37dEBXkofFsAWZYdzsNxnMd6q-RleZf0ztK8wB1lPqSLsvGNvHygPtR6iuV6cl8Rt9tzxKY35MkhziYgaNUGyOcBvzkiphjAP1C_IQ9rW2HJHRSB1odIwBq_405q6K0ReJwNxrRKMxWtc_s5UEn2Th0jIJHePvp2FAap75pBCZ_EUaQ1IAfnfOoBTviE_44VzYiA9l3yrFR0MFLy1gvm-VXhtDlD2yKo_-N5UNfFn10dWMfA2nyI9geAbcBzZGWVwGoE6GTCsVjG99XssOD_25aJMWhvxQwDr9i8q8GM_BTkZbLRq2xYFkmGoYbShaxE1dW261gX9ydNzXeQeXVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610cfa459d.mp4?token=gv37dEBXkofFsAWZYdzsNxnMd6q-RleZf0ztK8wB1lPqSLsvGNvHygPtR6iuV6cl8Rt9tzxKY35MkhziYgaNUGyOcBvzkiphjAP1C_IQ9rW2HJHRSB1odIwBq_405q6K0ReJwNxrRKMxWtc_s5UEn2Th0jIJHePvp2FAap75pBCZ_EUaQ1IAfnfOoBTviE_44VzYiA9l3yrFR0MFLy1gvm-VXhtDlD2yKo_-N5UNfFn10dWMfA2nyI9geAbcBzZGWVwGoE6GTCsVjG99XssOD_25aJMWhvxQwDr9i8q8GM_BTkZbLRq2xYFkmGoYbShaxE1dW261gX9ydNzXeQeXVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
كادر قناة cnn سمح لهم بالدخول الى البيت الابيض بعد قرار المنع الصادر من ترامب.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91489" target="_blank">📅 19:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91488">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTXNW345KXXH-gXljUk7wSr8fMqJEnOSzdnkGlSJxCr-YBadrJzpGXvtOJrWX31N-BYKiJKb7umTdMzUThyA2XT7o8LMY3cO4FwFWXAXx_xHZgQbpkH2WjTD-9EQxDTo8gUlpqJw6FuhIctXjOKt-bCeURcskdGfzNjQVtc-fUqlgw81b1AupMz__H8GXehHKqlfOTVSd-U15kUPs4gvc9XvG6dKXcLY74OlSYdyZDmiJRsBya7LIdUb4t-ZQ2jPYyE2qcQcEGCZUNW6iTIr6Y8hErXP1Wv_kmQS2cJbMWQgqwojsjScpWbxxHPS27py-QOXlCkJiRsmFLeelN4GaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النفط يعاود الارتفاع سريعًا ليتجاوز سعر البرميل 107 دولارات.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91488" target="_blank">📅 19:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91487">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇸🇦
رويترز:
تعمل السعودية على إعادة تدفق النفط الخام عبر خط أنابيب «الشرق-الغرب»، بعد توقفه في 11 سبتمبر إثر هجمات بطائرات مسيّرة، فيما لم تُستأنف بعد عمليات التصدير عبر الناقلات من ميناء ينبع على البحر الأحمر.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91487" target="_blank">📅 19:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91486">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqeiHiLKtuag1vJq8CQIjJMAkWvo1ocgYp2ttkAv8-vMC3UOVfLzGK6RV4hzAEf5PwTyBoyN2j7RQMRQ2Ak-Q3ktw9mcBdlvpreFKWHNrSiiVfLPPwbSmy3RouaOO4QLgTKaLEXrkKxzCs8FCKy3ksiHJKl_qe9vy7pmmSmgGL3eOjymCPd6gB-K3oTiblFyqLijKeXhhnE6Y6mO_HW2h3t1wjYR4wsZtCE0D51JU2fIlpHg68NpfPVZTPZerGQgFtjJp-VcFLlQzRsb0IqGs_cq5sRVzTsGD-KFh0mVAcWHB9lZaMXMOb2YAcKgVf-6A5ZJLIIATUJYRvg6IsjotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
استنفار في المستشفيات لاستقبال عدد من الجرحى في صفوف الجيش السعودي، إثر القصف اليمني المستمر على القواعد التي ينطلق منها العدوان.
بدري على الحوثي
يلمس اراضيك
😆</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91486" target="_blank">📅 19:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91485">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
كتائب حزب الله تصف الشركات المساهمة في إحكام الحصار على إيران بلا كرامة وتدعو إلى كسره عبر  دعم المنتجات الإيرانية وتشجيع تبادلها.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91485" target="_blank">📅 19:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91484">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇶
كتائب حزب الله تصف الشركات المساهمة في إحكام الحصار على إيران بلا كرامة وتدعو إلى كسره عبر  دعم المنتجات الإيرانية وتشجيع تبادلها.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91484" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91483">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3038b2edc.mp4?token=rxYclis4RbWm31IvC_xjQR6NoaDGW_-Iz4h6qRgQItaUV9AXD4qs7vNEK6tLD5NAsBdTl6nu9wI_uHcH24pFhkVdma79HPOzWo5OoBSF_V_9r-aF9gkTdaYN3xZKUueZX7XVCakxeAn6VA1bXNdVbB9LIAbax-LW2aeKu_3CznGKTreyqQnzSur35KrPZXoVVSwc7yGUMis1ScJXk3bzpgnOcEtwAOFSHSIxSbiEFwYgMqrBzSh3SFkEp_67ida-pr1nGQcbbpivva3EwWEh4Bv1E13PjatW67i049-HrbX2PFahIYWSAMW31vdGZF0u9Fj5_HIO_fp9ySu-MvsKAXT6W9YVvtGotYzg4wJpoLi4L8nwQ-WgktxYjm9rQV92-wCZ8PuSzcaxBv9qxra_HgJZr4Hk9cr5K5PV9eGacGvqkPxbJZu9pEHbvIuMO1Kqdxn1n7dRoHzsAsITQCSRJGM5BfOFglmfW5gseSQEE100cJVlP5RSKbbc_a44XihN6Bpg4T5vLULnqS_Qn4o0SaUj9V20JMn7KA2-4p1lkpi8pkbLfMKId2p_EjAPQJkjcJQ8dFAJdt_BSSUxLZz0sWfkWEn2w9UKSBYehUkpv6cmiQ0n_SsyUbjb6LSWwxxf0v7acPpcZ-N4pq9xMLEMkMw8ZKIjwjTm7lPwMPxtib4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3038b2edc.mp4?token=rxYclis4RbWm31IvC_xjQR6NoaDGW_-Iz4h6qRgQItaUV9AXD4qs7vNEK6tLD5NAsBdTl6nu9wI_uHcH24pFhkVdma79HPOzWo5OoBSF_V_9r-aF9gkTdaYN3xZKUueZX7XVCakxeAn6VA1bXNdVbB9LIAbax-LW2aeKu_3CznGKTreyqQnzSur35KrPZXoVVSwc7yGUMis1ScJXk3bzpgnOcEtwAOFSHSIxSbiEFwYgMqrBzSh3SFkEp_67ida-pr1nGQcbbpivva3EwWEh4Bv1E13PjatW67i049-HrbX2PFahIYWSAMW31vdGZF0u9Fj5_HIO_fp9ySu-MvsKAXT6W9YVvtGotYzg4wJpoLi4L8nwQ-WgktxYjm9rQV92-wCZ8PuSzcaxBv9qxra_HgJZr4Hk9cr5K5PV9eGacGvqkPxbJZu9pEHbvIuMO1Kqdxn1n7dRoHzsAsITQCSRJGM5BfOFglmfW5gseSQEE100cJVlP5RSKbbc_a44XihN6Bpg4T5vLULnqS_Qn4o0SaUj9V20JMn7KA2-4p1lkpi8pkbLfMKId2p_EjAPQJkjcJQ8dFAJdt_BSSUxLZz0sWfkWEn2w9UKSBYehUkpv6cmiQ0n_SsyUbjb6LSWwxxf0v7acPpcZ-N4pq9xMLEMkMw8ZKIjwjTm7lPwMPxtib4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇺🇸
استعراض اميركي خلال حضور الرئيس الصيني في الولايات المتحدة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91483" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91482">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rz-NPL_PkrVGHFI14SpZ6IFs_fJt6uQMOeasAeVgsNe_KetRDfWGhpJ-M6tM4Byo0pJywLGEdvG2M0_OruGbw8uQ3yCsBzcQ2XBdjOzo1JLDflK5X3Mikh1TzasQGBE8VcZNS5STdhs3SjBLOchQA9T5OQ-P5foPrtRZpq8gEHrny_BcwsmRTQwKwIWMaZqjkdS59hQKUa2ilAgHNiXEtJ8y69mz5dwVXjcF7TAwiMGge9HBUArjqO5AMp98Dz_RRBn5sedO4237os94ZWIW-9A1KwFHViAKatr22or3JdYBI8KjKEaWxhptch_NXilWXsepUr-LPaPhl3hCGi6Dhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انفجار جسم مجهول اخر في سماء العراق.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91482" target="_blank">📅 18:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91481">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
🔻
تعليق رحلات شركات الطيران الإيرانية من وإلى الإمارات بدءا من اليوم وحتى إشعار آخر.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91481" target="_blank">📅 18:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91480">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAETkI0-uItNjAkXCl7w_4SKp4JmjVbAiqKnn8ei1lCuvF9y2oOtrLA-g-PTmIMmd9RERgSkIorVPRulqX9U7fOmBsoAgtWWIwgEW0JVySnyURu-gNIzyOAnh4-V67uP8-j7zuWOFBun01RgVFu8gOC1tIDzgCbpS_0ursf_0X49Wf9mqzw1SDeU7RRAjdJmPMeRghKp4DBI5eK6uGqD9ngHjhp-fYeIXVSBct-_rKG6u35UIv18xFyj48v-wMiba5wnx_KmgCFjkkk9sT0AOMwSs0XHVME7WzCE7srkt_SQiE3qmCH3hD6zLUIKCo3-B1w_9_O6a1LJg9bcTN9LjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستمرار إرتفاع أسعار النفط حيث تجاوز سعر البرميل 106 دولار.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91480" target="_blank">📅 18:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91479">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية في تمام الساعة 5:50مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91479" target="_blank">📅 18:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91478">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بيان مهم للقوات المسلحة اليمنية في تمام الساعة 5:50مساءً، بعد قليل.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91478" target="_blank">📅 17:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91477">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏رئيس السلطة الفلسطينية محمود عباس يبدأ كلمته في الامم المتحدة عبر الفيديو بعد عدم منحه تأشيرة للمشاركة في اجتماعات نيويورك</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91477" target="_blank">📅 17:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91476">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
تبادل وزراء الخارجية الإيراني والأوكراني وجهات النظر حول كيفية حل مسألة الهجوم الأوكراني في يوليو على سفينة إيرانية في بحر قزوين.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91476" target="_blank">📅 17:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91475">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇱
مسؤول صهيوني:
إسرائيل تتابع الأنشطة الإيرانية في منشأة تحت الأرض بالقرب من نطنز وتقدر أن جولة جديدة من القتال قد تحدث مع الولايات المتحدة او بدونها.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91475" target="_blank">📅 17:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91474">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qfpc_3CpYugO6r4rjSvGQXmX4kcZ3DB-4iQbaXbkkoMYDj4CGYxArvG5wH-17gi-hy-Qlf6WnP1yLhmsO3B8VPe2IdkjN3TofUoeU-qtDZAZzC9uvTQUMqkYNJDWBwN4ec8dWNp2Wsl6yfEJ5fpxn9nqJkT8-CbND7KVPTkm4AYyC00ZrcZSU6o6aqQTAwvwQgMoOzhwOuDo4m06yooHQH2HYjHwvktD4YXwtX2yQbJBRMBJoqv5IR9BeFgiNAjCVVdbhyv-Fghnadw3iXVzXlwDz2TV2NbBiiHxsPcOXy__6Sxle83urZPcn-P6tggCm9JHNtGKzKuRKpn2nha2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحشد الشعبي يحبط مخططا ارهابيا لاستهداف مواقع عسكرية في محافظة الأنبار غربي العراق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91474" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91473">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سماع دوي انفجارين في مضيق هرمز</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91473" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91472">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">يمنيين يقومون باسقاط طائرة مسيرة سعودية بواسطة الحجارة في مديرية مران غرب محافظة صعدة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91472" target="_blank">📅 16:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91471">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a96ab0f7.mp4?token=W2VO56IEL8j8bxmMN--lsTmfqoivCWfoSURQKchAHjMkexwpCUgjoGD-t8wdOKLu-HnjC9bKEZEjzrm_BjlHATioaK22Hfl3GAYM99KsYOF63XX1GqwUqEMIYDPV-Ev4QGXJNGb_26C54Sh17RAvfuTlhpQCobXMczhwik0K41aTGV2nyJMahmLjVf0fVCAOpPohqpasxq6-SunnnGczvGoJYiRYJ7Zx0YFdZqFnNQx0_mSM20I1JAEkNUBhptJrXxfhH8AZhhd9IsNDTW8P0iJ1iAoidpfAsIOPFgerVUAFtHgjOrPGqMHmbSEdGkXodR0gk6ICppqk68RHke-zGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a96ab0f7.mp4?token=W2VO56IEL8j8bxmMN--lsTmfqoivCWfoSURQKchAHjMkexwpCUgjoGD-t8wdOKLu-HnjC9bKEZEjzrm_BjlHATioaK22Hfl3GAYM99KsYOF63XX1GqwUqEMIYDPV-Ev4QGXJNGb_26C54Sh17RAvfuTlhpQCobXMczhwik0K41aTGV2nyJMahmLjVf0fVCAOpPohqpasxq6-SunnnGczvGoJYiRYJ7Zx0YFdZqFnNQx0_mSM20I1JAEkNUBhptJrXxfhH8AZhhd9IsNDTW8P0iJ1iAoidpfAsIOPFgerVUAFtHgjOrPGqMHmbSEdGkXodR0gk6ICppqk68RHke-zGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يمنيين يقومون باسقاط طائرة مسيرة سعودية بواسطة الحجارة في مديرية مران غرب محافظة صعدة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91471" target="_blank">📅 16:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91470">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg9kdbtQAf25FOriYr_p7Hgi15HeyyfCvXpURZr61_8Y3fGsUD14nPpUdJcQMLQgB9bXAIytG02MmzNVvthAFcUV22PmcKTIeYrtqTke8lZ9mChCKKROv3IkYfIHEDQP3YTd60rb7BXysY3qqdthnVDyZ9aaR38vAPD2hRbTfcu0V1P6Y-oZ4R7dWzZlht3_4zblQSn4iKTPMdCmwjUAFEK_Asm0efRHglxpp8MIMLeA_PzhvFRG-UpxClQbAz4fagM3h9czYVjKotQWcVfvUPIH-ChURwEDqGaC24_5IRK-CjhuDAK9lxhZZayHa9hfe4r4kUQ8h5SBgXpbcPX2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
صواريخ يمنية تتجه لدك القواعد العسكرية والاصول الاقتصادية لنظام ال سعود.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91470" target="_blank">📅 16:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91469">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
🇾🇪
صواريخ يمنية تتجه لدك القواعد العسكرية والاصول الاقتصادية لنظام ال سعود.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91469" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91468">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLuC2-xWME4JSpGYv5IQhXTK7us2TmwrRBgK4t63E9buK6Xy6jKyUGZR5rj21i-cv6CQDIIpbIJamOsUaxoX92J1-RX1197LfD9wa1CfWUcRAb3OEQUReVcm-QdOxrAGsn5jlPVUvbegR8Npj01bLx7u_Z7kG20hnqa9dgExTmkZLP081JmUnBCTMLToYIc120I9r6PlnAEjyXwMvtPPiMeH4L4lQEmuc9GDGLAAlkVEiZEeutv7HbaDluYmHL9hoRYRv3-gQPdz56zmyXkFZAu3ZKkd4hioFKx5Mzk-hb5PBUKzplm8O-D_JBd0bOcMGaksOW6-7A_s6CXGef5eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل رئيس المجلس الانتقالي الجنوبي (جميل أحمد الأغبري) الموالي للامارات في مركز هجرة بمنطقة الأغبرة بمديرية المضاربة محافظة لحج خلال مواجهات مع القوات المسلحة اليمنية</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/91468" target="_blank">📅 15:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91467">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
وزارة البيئة العراقية تعلن حالة الطوارئ البيئية في العراق بسبب تلوث الانهار.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91467" target="_blank">📅 15:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91466">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgMt49OP_Q7BBCKlcxKQPJpHggSLOhpeehRGiuWWVNGkUI2uBfwlwvyIglLTzvch1tiTgFCG8yU78S75Mf4HUeRFAQ5BUvkD7QW5NXenICp9QC-fXGvqxXEb0bQ5Ud3i7h19_wK3otVhI0cqKY_winD3NyOKhW5LLUhgB9yskLwHr4wgPLALcL-eBwdPt5GmGApr7m_3aK51fOWExhO4XzGG7pfR-5yehVZ5-6kZYxqHRi54RI4coOU6YP-JNkhH2BZsGVNGJModQKYfbSSAkqVeHJmgZLCwFLTAUmMnFdHAk4oCUI1Sr_7xieEwffiXGcTMON48CIOoy525ItU0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
عصابات الجولاني تكلف الارهابي محمد صبحي بمنصب مدير قسم الإعلام الرقمي في الرقة.
يظهر محمد صبحي وخلفه عدد من الرؤوس المقطوعة رافعا سبابة ما يسمى بالتوحيد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91466" target="_blank">📅 15:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91465">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الانفجارات سمعت بوضوح قرب سيطرة دار الضيافة</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91465" target="_blank">📅 14:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91464">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سماع دوي انفجارات بالقرب من السفارة البريطانية في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/91464" target="_blank">📅 14:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91463">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سماع دوي انفجارات بالقرب من السفارة البريطانية في العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91463" target="_blank">📅 14:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91462">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d249860dd.mp4?token=Oaj2C3eJMIzveZQALQofjRZ9jX2Wv7zZV0KXNqlAeOFRLamuq-UnBsO2hXT3o5dYj5Xb2A7J5bLO4cf4pOqhw42Q7gU0fXeKKw7DIUbuCnope5FmBn8dOb8acQDYiggmggQxeqdiSI_SbA4FgZB-RW8hntQ8-JOqLcuGbxCh5i35QbYOqSWDfVzYJQzThq3pqxdMHE2UtYGruGvDBNvJ7mBA5BWJQz-NtBuN6Jn7OhZQupSy8BYOqU4Tm2Yuxqft_PhJI_9DXmE7nccd6xCn62bzJRekPCN1WhqjPxH1uafafSWnEi9byFxDrk-LtfBd3zhfgSVXq1I99PHOFoRSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d249860dd.mp4?token=Oaj2C3eJMIzveZQALQofjRZ9jX2Wv7zZV0KXNqlAeOFRLamuq-UnBsO2hXT3o5dYj5Xb2A7J5bLO4cf4pOqhw42Q7gU0fXeKKw7DIUbuCnope5FmBn8dOb8acQDYiggmggQxeqdiSI_SbA4FgZB-RW8hntQ8-JOqLcuGbxCh5i35QbYOqSWDfVzYJQzThq3pqxdMHE2UtYGruGvDBNvJ7mBA5BWJQz-NtBuN6Jn7OhZQupSy8BYOqU4Tm2Yuxqft_PhJI_9DXmE7nccd6xCn62bzJRekPCN1WhqjPxH1uafafSWnEi9byFxDrk-LtfBd3zhfgSVXq1I99PHOFoRSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في محافظة درعا السورية وانباء عن عدة قتلى وجرحى</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91462" target="_blank">📅 14:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91461">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بلومبرغ:
وافق ترامب والرئيس الصيني على تمديد فترة الهدنة التجارية حتى 10 يناير 2027، وتجنب التصعيد على الرغم من الخلافات حول المعادن النادرة، والقيود التكنولوجية، وقضية تايوان.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91461" target="_blank">📅 14:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91458">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇸🇾
انفجارات تهز محافظة حلب السورية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91458" target="_blank">📅 14:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91457">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al0aNCdgkt8L7HkkEee-QvjKebX2A_OYNRNgptAJutxXqUaGyU-FbSWPEt7MkCxnhQ3MYXeyoTOkjjhU9eLb4aoXZocfXpXDVWMjjpESU7ASQF-pP_Tt6vDbVWjBDapmqxc4yUYmGMqjT2eBev1aZVA0p1P5p8fm3ANXL9tsZ-XAPW4vnrQ8uge1gneu7126517J7OCORbnjWaM_TDgT2w4GRAiLO9PSNpNP_SRMLsFruZAWo_RvMo8jppWstuyDWs6tWWqV7Cw15R8lYPKXLZcNslYN0NVV0Rapn-RYpKDfneEdhKqg_QvtylC6bKiMEhGuyLdfw16eN_kQL0tgKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
عضو انصار الله حزام الاسد:
‏ماذا يحدث الآن داخل القواعد العسكرية السعودية ومنشآت أرامكو؟</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91457" target="_blank">📅 14:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91456">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات في جدة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91456" target="_blank">📅 14:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91453">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Br4v9XmBGOq4VJokpG1Vdi1SboNN7p5pPvOVUNRXGtViLTafebUI2Q0YCD-HKxsfwtdK2DuOiP-4Mu7eibot0eAk59y6Fzn7c_8Frn_ju6ZgmaWTAjF7gE6BmzbH1RrPuVbQI-5qaSFSbdw8HNzuBtqAQZ4Th7ueT8ioy7qs6UVrxXLvnORkbLR7wI59VJc7trVVdqG8qmqXLq2FNVx1BWxYR0zB7PAnESuwBj-F3KWff5vakDp3rR4i-PHMcVJTY659X9Na8LvD9l3hMV1hkpPpgfXX2AUi7HKt9v3ltvGeXk1MAZ6qm-jrcSyxwTaVc5-bTI-nAP1YkkR903xe0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف ميناء ينبع</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91453" target="_blank">📅 14:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91452">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ينبع تحت القصف</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91452" target="_blank">📅 14:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91451">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">القوات المسلحة اليمنية تدك القواعد العسكرية والمصالح الاقتصادية لنظام ال سعود في مختلف المناطق السعودية</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/91451" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91450">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تبوك تحت القصف</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91450" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91449">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نظام ال سعود يكرر الكذبة مجددا: تفعيل الانذار المبكر في مكة المكرمة</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91449" target="_blank">📅 13:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">انفجارات تهز الطائف</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91448" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات في جدة</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91447" target="_blank">📅 13:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91446">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91446" target="_blank">📅 13:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91445">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91445" target="_blank">📅 13:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91444">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
أمين مجلس الأمن القومي الإيراني محسن رضائي:
تصعيد أمريكي جديد قد يفتح جبهة ثانية في باب المندب إلى جانب هرمز.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91444" target="_blank">📅 13:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91443">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
رئيس المخابرات الدنماركية:
لا يمكن استبعاد غزو روسيا لدول حلف الناتو .
من المتوقع أن تزيد روسيا من تصعيد حربها الهجينة ضد الناتو والغرب في الأشهر المقبلة.
روسيا قد تستهدف دول اوربية بمسيرات مزيفة و باعلام أوكرانية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91443" target="_blank">📅 13:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91442">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7554bb0c65.mp4?token=qe2l2cKsRgMACyIj5Ui2X6ENTgdsgOSh5M_JmS52UO2U3BdIkyB-MerTnS6vWwvjl6F92sDIQsKJPpIuZB5iJ5rHOr8ikIRIFfxv1oOZDrJqK9-Qkq3vbERygaxmI3R4hfYMGK-zfmnEsXQApqYXfR4hZILAXZCuDRWGX2ERvL3O8R1noLVxDvl1vy0TIo3GiHKbLgUIt6urwA-_wepqnC5rxhDyyPcNRP2mkEwbBsYfciR76Lm6yh4dYVP8PDlg4xdwEM6SYwIdDuZwo7zk-a-m24T7_jW2iyToeC_zMnrhTOhKng90_JiRGbewTPF0wkJCNEqoDyB1jDvAvoP_fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7554bb0c65.mp4?token=qe2l2cKsRgMACyIj5Ui2X6ENTgdsgOSh5M_JmS52UO2U3BdIkyB-MerTnS6vWwvjl6F92sDIQsKJPpIuZB5iJ5rHOr8ikIRIFfxv1oOZDrJqK9-Qkq3vbERygaxmI3R4hfYMGK-zfmnEsXQApqYXfR4hZILAXZCuDRWGX2ERvL3O8R1noLVxDvl1vy0TIo3GiHKbLgUIt6urwA-_wepqnC5rxhDyyPcNRP2mkEwbBsYfciR76Lm6yh4dYVP8PDlg4xdwEM6SYwIdDuZwo7zk-a-m24T7_jW2iyToeC_zMnrhTOhKng90_JiRGbewTPF0wkJCNEqoDyB1jDvAvoP_fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تتمكن من دحر مرتزقة السعودية وتفرض سيطرتها الكاملة على خط تعز عدن.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/91442" target="_blank">📅 13:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91441">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇸🇦
عقب الضربات اليمانية..
‏
رئيس أرامكو السعودية:
وضع الطاقة في العالم سيزداد سوءا لأن الانقطاع كبير وليس محدودا.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91441" target="_blank">📅 13:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91440">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
منظمة الطيران المدني الإيراني: بسبب عدم إصدار تركمانستان تصريحًا للطائرات الإيرانية للمرور عبر أجوائها، لم تتمكن رحلة الطيران من طهران إلى دوشنبة من الوصول إلى وجهتها، واضطرت إلى العودة إلى مطار الإمام الخميني في طهران.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91440" target="_blank">📅 13:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91439">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
تماشياً مع القرارات الأمريكية الظالمة.. تم إلغاء رحلة شركة "وارش" الجوية من طهران إلى "دوشنبه" عاصمة طاجيكستان، وعودتها إلى مطار الإمام الخميني، بعد أن مُنعت من إستخدام المجال الجوي لدولة أذربيجان.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/91439" target="_blank">📅 13:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91438">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
المساعد والمستشار الأعلى لقائد الثورة الإسلامية "اللواء صفوي":  نحن مستعدون لمرحلة جديدة من الحرب المحتملة مع الولايات المتحدة.  قواتنا المسلحة تقوم بصياغة سيناريوهات بذكاء، وقد أعدت خططًا للأسوأ من السيناريوهات، بحيث إذا هاجم الأمريكيون والصهاينة مرة أخرى…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/91438" target="_blank">📅 12:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91437">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/399dabb06c.mp4?token=KRQB4RXc8lmG7ma2-hGS5sKrOv4dZ7ijUX_5yCSdTB-lK5dye7EFhSrwtnZvi5MZoNWegJ57sg5g2Ggzpex-57m5zvohfZDJExGhmjgrcf6yLr725xhtXMBqbEPZQGhSUWRZVkTg2hgSlst9FaoyVoSiqMStCM0jMZNsSWllviCxT0FK5jhQdMskC7clgTLMTwHwT_mNQFrChqd5Fpwe0skeTSVp8pKfIaO7ZRzI5Rdd3iNnV0GIVh2JOvncLYHjreKWf2dyVH8CYOhbmGK0UUM9eEFQTn8L8967-TMNU1PfnOefZISyCxzbhTY60-RByLH2u14tG0M2r8_R45Wx1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/399dabb06c.mp4?token=KRQB4RXc8lmG7ma2-hGS5sKrOv4dZ7ijUX_5yCSdTB-lK5dye7EFhSrwtnZvi5MZoNWegJ57sg5g2Ggzpex-57m5zvohfZDJExGhmjgrcf6yLr725xhtXMBqbEPZQGhSUWRZVkTg2hgSlst9FaoyVoSiqMStCM0jMZNsSWllviCxT0FK5jhQdMskC7clgTLMTwHwT_mNQFrChqd5Fpwe0skeTSVp8pKfIaO7ZRzI5Rdd3iNnV0GIVh2JOvncLYHjreKWf2dyVH8CYOhbmGK0UUM9eEFQTn8L8967-TMNU1PfnOefZISyCxzbhTY60-RByLH2u14tG0M2r8_R45Wx1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدث امني خطير في محافظة الانبار</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91437" target="_blank">📅 12:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91436">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حدث امني خطير في محافظة الانبار</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91436" target="_blank">📅 12:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91435">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685d72f92.mp4?token=YM5diDg7jPYamIVM0ih3F0g0YPZf6KMNUudzfeRuCkShEI0Y6JUOws_BRZBkQqYiSv9GG00yhvH9w-MMhl2vg0-GGjHriaAgompV7ngIygrcrgoohQu16S6MTappxHsj72RO2_S-rLMHjvB0fxUPyhNMjAiBNpUvYiNYCyzgrtmiDjI2JCXfpiGCjjXcuD95mijGOU4JF1ZPORlE6ew2bAOLT3vxjnX5aGFsocT3zEFLDnfZD-6E5IofZn4gDqzAY-QVUPWHdnpybbHmVO3l1DRAhNMCOnCvO1lIP31Tr-0SeLKUe6w3LKxt0RXLLRf2ZskyhuOPx6SwnLbbrDzsA0qaMg9xzedko_v2fF0IwT9Yec5V1w1eway2MeKGdeBlhntJY7aOXHaIsmwm3nYGCimp3ltQbpjKMTWUjNMbui5N02fc0MVr-8_cRrwfXRB2sc59n56bXyDQ1AZBGjg74sXFcgkPIw_v7b5QCeL9qVqeizk0REFNnCye99Mqq7J-d_jM-JCEjKC9zc7iFABgAYLSdiBXZj049wmwUMH2t16i0im5rZcsKhK9I1yF2yd5GlTf6slDR5iCfrVRgRp5m29IUhOonO28Iw8-tRaRy0ySkuEZRwqInJ1oEzDTIGcc6NNCUbWnco4tC5rwN2rYieFkE6Qfok6onwRr0rmBifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685d72f92.mp4?token=YM5diDg7jPYamIVM0ih3F0g0YPZf6KMNUudzfeRuCkShEI0Y6JUOws_BRZBkQqYiSv9GG00yhvH9w-MMhl2vg0-GGjHriaAgompV7ngIygrcrgoohQu16S6MTappxHsj72RO2_S-rLMHjvB0fxUPyhNMjAiBNpUvYiNYCyzgrtmiDjI2JCXfpiGCjjXcuD95mijGOU4JF1ZPORlE6ew2bAOLT3vxjnX5aGFsocT3zEFLDnfZD-6E5IofZn4gDqzAY-QVUPWHdnpybbHmVO3l1DRAhNMCOnCvO1lIP31Tr-0SeLKUe6w3LKxt0RXLLRf2ZskyhuOPx6SwnLbbrDzsA0qaMg9xzedko_v2fF0IwT9Yec5V1w1eway2MeKGdeBlhntJY7aOXHaIsmwm3nYGCimp3ltQbpjKMTWUjNMbui5N02fc0MVr-8_cRrwfXRB2sc59n56bXyDQ1AZBGjg74sXFcgkPIw_v7b5QCeL9qVqeizk0REFNnCye99Mqq7J-d_jM-JCEjKC9zc7iFABgAYLSdiBXZj049wmwUMH2t16i0im5rZcsKhK9I1yF2yd5GlTf6slDR5iCfrVRgRp5m29IUhOonO28Iw8-tRaRy0ySkuEZRwqInJ1oEzDTIGcc6NNCUbWnco4tC5rwN2rYieFkE6Qfok6onwRr0rmBifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تماشياً مع القرارات الأمريكية الظالمة..
تم إلغاء رحلة شركة "وارش" الجوية من طهران إلى "دوشنبه" عاصمة طاجيكستان، وعودتها إلى مطار الإمام الخميني، بعد أن مُنعت من إستخدام المجال الجوي لدولة أذربيجان.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91435" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91434">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
إل موندو:
الاستخبارات الأمريكية حذرت عدة حكومات أوروبية من أن روسيا قد تكون بصدد التخطيط لعملية باستخدام الطائرات بدون طيار ضد إسبانيا أو فرنسا أو إيطاليا.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91434" target="_blank">📅 11:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91433">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvedUod5-0qpjMsUieRvUoU3BoIGvNjmGDE66VNDbzqgXyF2sfkVXvnIj-1iel6yQjoq1_0EfNRoLwcxKbF2WALu9jny1ZvpSbUqQC-ta6MO3-hfPkM7WCxJxhy4yJqTtOmTAN3LeI9OERagnQ-M9DjbdRfWttfSS3qAlPPk6ZpZEusRgTGLPWIG5zXbGucdphgQg2dNE-g-l4Ks_EuTOoKxENgQol4SHsNrC2Z9qR5Z54kDs6pYX-w35j8pMZRYx-X9bRLR8St4xXl3iMpDVTyOXRAkCkjYR-sFvkcHhuk1V3ep6TuAZkaZKofyO92jmKzj9vYBXKF7TAgTfuPepg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية ترتفع إلى 105 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91433" target="_blank">📅 11:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91432">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رويترز:
اندلع حريق في محطة أرضية لشبكة "ستارلينك" للأقمار الصناعية في منطقة ماسوفيا ببولندا، مساء الأربعاء.
وكانت هذه المحطة توفر خدمات الاتصال لبولندا وأوكرانيا، بما في ذلك المستخدمين العسكريين الأوكرانيين.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91432" target="_blank">📅 11:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91431">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkztPNBLvccWUj0cEV5p5MkE9vWL0uoqx5wVl_DBzw6Ryt4OPKTSLJ_dmLril11vJenmd4-yz18M5Qj34TngQY5wdCnjCUkjw8KM1lSCA2NrPeqdrP-5wDMsyf1toBhGaG6kOpdV_JeX0JYDKiOQpd7M4yqpAKxh-f8maGWRzoT-nb8qFfLGlqv-030xtizRGQr-XR5uFuPpanz0h_PkfHRDOcYCE8DsxFkuV-r-sXA85RvTlWhUrSQzcdEmeu3V28d9T_LH8CkU_ed7RMufTWi_tCYw32CFYcLIvmo8yP6iwC9Szy5tarMrtAQEtKTrCjNeGyrFynbR6gkdNuF2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
أسعار النفط العالمية ترتفع إلى 105 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91431" target="_blank">📅 11:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91430">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇹🇷
هزة ارضية بقوة 5.6 ريختر في تركيا، شعر بها سكان الشمال والشرق السوري وبيروت ومحافظة دهوك العراقية.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91430" target="_blank">📅 11:15 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
