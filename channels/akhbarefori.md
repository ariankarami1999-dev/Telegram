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
<img src="https://cdn4.telesco.pe/file/jnNIBoT0Zvav2-BPdLDskPicgRxBGg7VWJoqBzldU211QotPy8A9gfirYGFhBk2l51Pi6UojckdgLcPTG6Ru1nqPvIL8LlB3fvxj2D62At4rv3LcmA1JqiHa4gAAPRrdYCJ8bpANAuq7SIs0sLq6FzkJbRA5kxv58tblGhXzHBGjKr6P9_fxDyKF59MHVJaUmaTEANgNEkt1LMY7RjAV0HWNkcJaDN4hZkUpTenMEUd0oDfYAIGGQszpXP517msD42nVlFPdAEgbIhh35R8iP3wXiMrclyWPKBnmfggslqXmoAGLqOHqXsAUWTbEpnS-q34s-JpxZHuqkAfSUUUTOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.12M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 19:33:43</div>
<hr>

<div class="tg-post" id="msg-690177">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18e8e89d76.mp4?token=DP_OEzfHmnZ_XMUHcm7-GgrJ6oyvJnHM_E_00deC4Rp7gc7mTApW6NyqV0wkv-ums7OAaAnObVuvh8I3K6jesONH2rbKJKZTQu3-_4f4-vYpVtoYGdeSSrbWWruWrK4mJTrSbru6RdGRISZSR8qoiROXp_-KmQssJL3b-Nh2Lqsrg9yehVe8PDc0A9hlx-0x6RwGhVKgzvnW6HCUmyojWQ9eB1QkfPgefN1TkuMH3j1vxtktTBebNSiDqVOmK8lEBjbnfGBTyShWw-MWoM2GETU9piineAzkZlOXtZQwC2NhKVjzHiclgV2xVi8cE3ec6GUM6Kw7usTun3DZ2Q7h-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18e8e89d76.mp4?token=DP_OEzfHmnZ_XMUHcm7-GgrJ6oyvJnHM_E_00deC4Rp7gc7mTApW6NyqV0wkv-ums7OAaAnObVuvh8I3K6jesONH2rbKJKZTQu3-_4f4-vYpVtoYGdeSSrbWWruWrK4mJTrSbru6RdGRISZSR8qoiROXp_-KmQssJL3b-Nh2Lqsrg9yehVe8PDc0A9hlx-0x6RwGhVKgzvnW6HCUmyojWQ9eB1QkfPgefN1TkuMH3j1vxtktTBebNSiDqVOmK8lEBjbnfGBTyShWw-MWoM2GETU9piineAzkZlOXtZQwC2NhKVjzHiclgV2xVi8cE3ec6GUM6Kw7usTun3DZ2Q7h-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی‌های گسترده در تأسیسات ذخیره و توزیع عمده شرکت آرامکو در ابها، در جنوب‌غرب عربستان سعودی، پس از حملات پهپادی و موشکی روز گذشته ارتش یمن
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/690177" target="_blank">📅 19:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1awN_Fbm0vNYsS96EX0FeoWny1KMxdG_oPkR70q-kslxTvuSDz6E-l1vtqAOm543YhzT4vcHzrzuZJnuoACh5sGtnwRQZycqwScX9QF1V_Ul8cSYqTo9oWPpf-veiOMl9-YWqGEgSAl-wn2olpfFSVG0v-l8ajS4jGuCQLkgggkoMjZ7yjCHMA4odYPH34ykxB3LYv7tvg6neCl6p24ua6S0C_N_OGiS2yBffD5IcrWdauz5HMR9EJZntWpCtT_PLzVQC4ngtyBnCiN9BYo7x5R4qn11IXT7DsPjyrjOlBuGyPz6P_ec2__2URJxtKtOg05oxkR3_v5zsXlJZF9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cO2gcXFIKs5teGi8MUbdQxv5FPZkF6h5qROss1dGiy3CIblweYqTOnhxGBOzEBEFxHmwAwI1KN8qA67c-1x5ceGYq4Lh7njnjrllCq2bP5q-XaTlVfk55xONnX3J7x0LC11JodFWtoZTraarOQ56Tlon96dx9xA2ixjgMFgsK4E_-THsubhJcN3mWLdNR4NQQI8aZ8mOWfkIHnZtFwna4KkNQwxXQaYjSuBLVfq5WhymCKdme0Py8uriaCNDALXj5MgjLo7GthYAAsI080MqZIzuVmuhXfqg9lW4JiCsH2Tj_CSk0cEV0Ds-_NCDZgTZBqZcyrrKbvtTVSwSVbmQjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veO8EZ4dYZ-fPu3_NRBBW71XNGKIG7ifKYGLTAqUO60QvlDzcNOk0x_C9n7gY6SW_G-2bBjqsVF7e67eISz3lRin1UN2D_R57CUrl9Do-rsP7gtluabHxAj4oad5aR_ccr1pWTGVpPatphyG7lV6SNtoft8rAsXb-iA25Wnx7ZvKikpq4jlLQKZINrD5F7MRB1GN38chjh2klwQh69eBAPA9iLDMnI_WycAXdSTOzEju7AYp8NLgPI7MbQRTClAKVnXFW8ZF3Z8-ChYgbEYYAhnebAUCfUPXtiib4QmloUWxIbQ2hOZumD5kanNU6RWljyabW9ynX0jRI8p3cpKsLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEUZYYildH6Uj5pZrC47TJSDKBwTBgH5KXchPvHj5nVz5ES2tykirqeF0KfrNdceHWay28ks5UbYcrE4h0s1YxbAQfh1Byord4K7XhTudpS6rxz-r5S05J_TpYskn2gzs0ZXJgIp93yZy50iOx91_B4fN8m_BZSPCzVAshUot_aP3q2b2R2EtrnvUnBSxrs6EqjLJ4vf7jQwhNP5icwTnhSQdT30hTre2ykmAQG8-EKVbv2HG2G8EEVTzkuEIBYqKshdEbZ4P5vIFdhQ2QE1ir-sTavuDwDUuy2c_z4xIaxSdhdYvqDfPR481yRQHRdBwfaUgzlBTyW3YpksgslGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qdS9hp6HerOox-2ix5zyrq3Z8rEC5hUsY2HEO9yF9E8shxeTFeT_fWhgdyiWVGe4x1UJQhVa7wJ6kbBh68GM2e2mYGLSite1RKDy0mgMRbHMBPxvh7U0byUTkiIQa93z4pQAjAH7f9wtALMtaCa2z4JrbC7r-Vn7NRcreBB5biyoiHKAlyswwBrd3MBk-7ouHqvrwqhchXqCEN9GSMdWPx3gZe7pVBoETgQTw8iV9cPb1KyGohPOsqSMPzK1qcQ35L_16pgHAX7Q3Pgy5gHAxsQKj102OhJYX3y3gCLyaa_eLti5l5vaybSRxy51rtYkyUFhwvzwnhLRA7obaklHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DVBb0Z59O8OxkCHG7xEuUfNI2KHw2MxI-F66tZGRG7eUVcAXQc1bbVUlFk6XwVs4a-ss2x_A4cnSu5estuJmP2Pv-O0fUJEv1Dxvyh9XiG49ZNe6pYNMUxeFQyMfH7uL0B8F6Gy9VOMkdnWiR3fckoyxEzCvtqMbQJ7Y1NdZuuRjCfA3DrWvn1NYopU85cggFpHgBAC26EeU7KAUCLuhwK6wrW2t0z6mBcZyxEQKfGf7Ac6tWqaxnJlWdFMYCeOmY8AkAupmv726GykfYIp7cub2Yk2jQLWSFKYB6-j2Od2qpGiEX0nn-wBiG-DfO3V4_J31a9NKp-uWJzcYqOP1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROqlF9IgMlnIB7zfpUMpU1N4dLJtgT9IgOQjKzWWWmSeKEoOwKgchKmRXxjyyW4SGEbjuRG6lEBeWEEGrnr6pRQTOwy0ogB4Ws9stVAFkBt_WyD15cixlZD5cDu7K0ci6pRs_444eas6Gfwk_0uT8tiMMzlk96Adn5i-CIld3KqukMGx7xqww-Yw6YCFezPqbt6nvwBE5pz6aYCC4E9H99KwB8YSsF0Qqo2Ko2QDPtYXfgz0XFvB7DnDoO3ZqT_eKzSGFa-1uFTeUJeen284-eZVjbkYPlFFOqRlM3HdyPs_rKX8LE5kWSUsduiRHpkg2CxfOz1i0LBdIDL2gkDUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbbW5G3aAwz0VDoF9lJ9JK7UVswyQxgBGCtXAziXAkwQYv6TNVXFSE4gV5twGepr0xw5FMdhavJ14IeTeejKHbS6nWvUTuJm5VoX6R2H7UI1KiHJV17LK9yucVZr6kMSDXqrIZ7ldUh8mo5KWCuXktnn0R6GIa5nTnJ6bNE-WV3jK_MQwZVikeuHsauYYkaPtZnqn8azP_N78-j8SJPqPGgIzgoFNIW4f7exsdkSWZAf45INLBJNxW5pBQd-RkhHoJjsRo1XYM_yvYoSMDCNO3ADhM3RAdGQr1mr6F4eUADQ5Eut9qCAVQI0pnVR_gfMTTV4KXhQJAsuGfTeEKqDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEFL0ZYDoThqVnkyl1R8GFy782XHF7A98illfsYjTWfRcql_7QcxnCUXyLgcwN0km0Qmpf6Nw_23G8N-5-hfvE_fb12UaAgPuc7nYdGz6BiMt_pG0USYFcIlm_SeJd-dO2Cj3JtYMFfThK0hHvMEsCbHUr0iNJlK7ZalSoRLF67HAWotfqOla7fWpD1l2qu1Rc51E7M-Nzoc65RNrt-req_KGt4L_oZI1qVs512UwMl1fOCNoajHIwMI8uq9vYLvUSuJvnP5k6PWUIR68ShWRHnAdt-CTgNVyPzYKfDE4iKuAH_4_XwnwFAi7zpw8C8p8TBtqnj20c7Tfv8PY85IAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LAA3B6e1Rl9bICqSzEhPd2qcPDzoJWbcOMsWtkURTB7TSAQUfBv3jbKyyWPub_1Vjp6dyzq9XQzvpq_0CQSbAhrlTBKSXWXXtWnOzllw7wjEZ5Jh20msBxKaBx5Qa32W7fdHuka3eQy_AeROE_cfO0hpVUSUpOCv1CWtppLlEa21TeuBWX2p8f4cp7JdxxYJ1sEFjlHpEtr42S48wukuu3zyCdfYT1K5vWsyIlh3nh9nmJ1NgNelbNwp_yKeY5pm004rFk-V-TQS0dlIacgflzKcy6y9dJTrekYi17kWXqABfl6mOd1yifHECWeQOnp-lzP2fdXYzeUDwOZO9SHzyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
انعکاس دغدغه‌های مردمی از مشکلات ورود به سال تحصیلی جدید
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/akhbarefori/690167" target="_blank">📅 19:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690165">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: مذاکرات خصوصی خوبی با چین در مورد روابط مالی با ایران داشتیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/akhbarefori/690165" target="_blank">📅 19:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690164">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6acb873e3.mp4?token=TCHX1Gy-ZZCaYLV0G31DWxdgEcWmhslTHin1Iif1Sh-h4nEAbqPrPcAEZi_C4qE6Tqgwf5JOjVi5OtNhEvRk2mO9RgR4_l3Wua5g5181bKRfspa8Yf5wDOCNYV3Cxzp8mk4fg_Y469UzHwsIpBBoG2g1KQWlmYu2upHT35gByTsw6w0Mq8ZrGw2pi6mXI4NAg8zsmxR_ydF2DpKI9qJoJZjkqm2WISzUPtI3k4CJo79-JOYWDOnS9R-ddlr44humoPVXf8Ho6oTpY253x9WxiPsJ_jyHX2KFhEONYySRXsi-upsYDIrDZJxRFiUpUwYPiymZxdpfggnB9-o7qEj_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6acb873e3.mp4?token=TCHX1Gy-ZZCaYLV0G31DWxdgEcWmhslTHin1Iif1Sh-h4nEAbqPrPcAEZi_C4qE6Tqgwf5JOjVi5OtNhEvRk2mO9RgR4_l3Wua5g5181bKRfspa8Yf5wDOCNYV3Cxzp8mk4fg_Y469UzHwsIpBBoG2g1KQWlmYu2upHT35gByTsw6w0Mq8ZrGw2pi6mXI4NAg8zsmxR_ydF2DpKI9qJoJZjkqm2WISzUPtI3k4CJo79-JOYWDOnS9R-ddlr44humoPVXf8Ho6oTpY253x9WxiPsJ_jyHX2KFhEONYySRXsi-upsYDIrDZJxRFiUpUwYPiymZxdpfggnB9-o7qEj_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرکز امنیت دریایی عمان: نیروی دریایی عمان ۲۳ نفر از خدمه نفتکش الگایا را خارج کرده است. عملیات جستجو برای یافتن دو فرد مفقود شده در حال انجام است
🔹
فرماندهی نیروی دریایی سپاه نوشت سوپر نفتکش «ال گایا» که قصد عبور از منطقه ممنوعه در جنوب تنگه هرمز را داشت،…</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/690164" target="_blank">📅 19:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690163">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
اعتراف بسنت به جنایت اقتصادی آمریکا علیه ایران: اینکه مردم ایران باید چند ساعت در صف بنزین بمانند نتیجه محاصره اقتصادی ما است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/akhbarefori/690163" target="_blank">📅 19:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690162">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
پروژه‌هایی که در هلدینگ خلیج فارس آن‌قدر خاک خوردند که از «پروژه» به «سرمایه‌سوزی» رسیدند!
⌛️
سرمایه‌هایی که می‌توانستند به تولید، توسعه و سودآوری برسند، اما در چرخه‌ای از بلاتکلیفی و تأخیر، گرفتار شدند.
سؤال اینجاست: هزینه این سال‌ها توقف را چه کسی می‌دهد؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/690162" target="_blank">📅 19:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690161">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6DIgBO_dzQoHXQpaLrLoApwpmXiz-A4nrWy698lGK5uyNb5xZMKqKNtbuAMLEj9mQ2X6lq3ABQ5WpMRZMeiyMWP3sFqaExXY8tVq9Pf5DM9mDk9753SmTMrf9DoadLJSAODGH9n6fozSNNNjLs0oh0qrUlWHKSQFApwz6UapXu959tY-boaXuj2NU0fDME68WbM1J8uZqCxm6QzfOtSjQ6kK-fBd3_iCQPsU_JRePMYRLshzD7huMPI6GmwXjvoQNwHJL1aQGX9Ocjx0UUjh_y1LxoHLLVXX9N_lMZE_6a2YhzGEqzkmGZ99XtX_68iJYHYxzCXBU5HUtzNDvOidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ نوشیدنی برای سلامت کلیه
🥂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/690161" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029883431c.mp4?token=XpHIEjy9i_Dm5y537NvW6XtkyAkJDN2sN7VK89L6vgrbAzVnGOiOSxA5ZF9YLdg5aw87s4c4ArJn-wXDxyKbAKTacRZcEsGeXwGqOVOEsYE9EdIuvYrG44lYqWACJzmLNovjTvinYNr9iT6NIRzRLw8ihsbyrSTvVnSpz7eOkxCVx21gIKEUykY0dPD5H4ajEpgiJFmHNDFXVTVTOApqlLKk_B1x2RI8ca4aS8sbG3GiawSLmonIgpxN5vLahR65LMel2XaCG-K_FLsr0cMnb0hYKvjFBckmMmDnX67XVkqhfJLwMBWaedjC_nfgdy5cWbOl4hGF2-HE2o-_kMmYcQkr70SujZf3M06FG27lawuN44hIbJ1awDmJNTJI2nR1im2Av1eVQgeoEVQZaLy02AMHXIWT9Ls6b4QTnqli_nK-m05XGlOaCbdwcaPfoVbXH1pUVZkJ8uPx6bOYzPbiV8h4ZwumuWaZtkvepTh-ZIkqa7NpR2LdJy8Ed_XRQrkBZa0PZm1ABYHuXA1WlcwgqqqA_c12HQAXh3my9Y8KyWPFsDD8gi8PfgXkFsQjqTPwR9G_lEnZg7dWC24RXFt5oBjcLAZCNKRcLGgZVIMEaAmNTJvS6lkf9RUmhsc6W7FGVlERgRPz2vupS_3lgs-ZKY0T680btgYt394tBgvytYo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029883431c.mp4?token=XpHIEjy9i_Dm5y537NvW6XtkyAkJDN2sN7VK89L6vgrbAzVnGOiOSxA5ZF9YLdg5aw87s4c4ArJn-wXDxyKbAKTacRZcEsGeXwGqOVOEsYE9EdIuvYrG44lYqWACJzmLNovjTvinYNr9iT6NIRzRLw8ihsbyrSTvVnSpz7eOkxCVx21gIKEUykY0dPD5H4ajEpgiJFmHNDFXVTVTOApqlLKk_B1x2RI8ca4aS8sbG3GiawSLmonIgpxN5vLahR65LMel2XaCG-K_FLsr0cMnb0hYKvjFBckmMmDnX67XVkqhfJLwMBWaedjC_nfgdy5cWbOl4hGF2-HE2o-_kMmYcQkr70SujZf3M06FG27lawuN44hIbJ1awDmJNTJI2nR1im2Av1eVQgeoEVQZaLy02AMHXIWT9Ls6b4QTnqli_nK-m05XGlOaCbdwcaPfoVbXH1pUVZkJ8uPx6bOYzPbiV8h4ZwumuWaZtkvepTh-ZIkqa7NpR2LdJy8Ed_XRQrkBZa0PZm1ABYHuXA1WlcwgqqqA_c12HQAXh3my9Y8KyWPFsDD8gi8PfgXkFsQjqTPwR9G_lEnZg7dWC24RXFt5oBjcLAZCNKRcLGgZVIMEaAmNTJvS6lkf9RUmhsc6W7FGVlERgRPz2vupS_3lgs-ZKY0T680btgYt394tBgvytYo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با اعلام رسمی سخنگوی ستاد مردمی جانفدا ثبت‌نام گردان‌های ملی مقاومت ملی جانفدا آغاز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/690160" target="_blank">📅 18:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690159">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
وزیر خرانه‌داری آمریکا با توهم ساخت سلاح هسته‌ای توسط ایران محاصره جنایت‌وار خود را توجیه کرد: چون ایران قصد داشت بمب هسته‌ای بسازد، بزرگترین کارزار اقتصادی جهان را علیه ایران اجرا کردیم  بسنت جنایتکار:
🔹
تاکنون سه بانک کمک کننده به ایران را تحریم کردیم…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/690159" target="_blank">📅 18:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwInQ5_5NfFzI9cBY6byOjYdQq44CAeII-4RHOzEBQBgS_F9snVhexk6niKmLMlZcMdvFmxyK_VWd37vxt16tF9JeW7ZPJmjYlV4HdvIA9Ul7hW9sjhO3m-h-sH7TMQEFhEpFvUySdt5xQh3SXm7_tsWdBbXSkCFWfltkd-6-rh0HVinoNkzVq7Id08EZlSV1GuQnVkFzlE7xWF0gR_iNskA5un3oOq-c_ffKsPNCIazoKsDnAzWQoQhK3K_T1fk_WkkvUodzgyPqr5XaX9vnSXWXeX3bymI-UPx79KXNCr82eN419Zzf98qFs1OwMl2h5OqeTMi0d48rAbGe6qilg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
پک ویژه سوغات رضوی
یک هدیه معنوی و ماندگار از مشهد؛ ترکیبی از عطر، مهر، قاب‌فرش و تسبیح رضوی برای کسی که می‌خواهی یاد حرم را با خودش داشته باشد.
🤍
داخل این پک:
🌸
عطر گوهرشاد — ۸۵۰,۰۰۰ تومان
🕌
مهر تربت مشهد — ۱۸۵,۰۰۰ تومان
🖼
قاب‌فرش ۱۵×۱۵ — ۱۵۵,۰۰۰ تومان
📿
تسبیح رضوی — ۲۰۰,۰۰۰ تومان
جمع قیمت اصلی: ۱,۶۳۲,۰۰۰ تومان
🔥
قیمت ویژه پک: ۱,۳۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
قرار؛ تجلی هنر و ارادت
@ghararshop</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/690158" target="_blank">📅 18:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsaWqGCV3s9Q-k26IzDS8wbKGX0RXJuRZ-74NAPZqo74Mfdlo0z_C-jDpHHATJEYPW6amJbDJEt5qxVbDjuXkG5H7DLhZ_F6mxWxvO665ztx_vDnNEraz8SCPflFxMDryn1bWEdaCOvkV1bAd_pu92QVog2E2RyLNuLmXnV0EkvlIm5pQjP_5O9P_myqvuibvKDDmO26N77fg7qSiC33bgFnNkmWZnNb5SYSCdzDWjdgL-PIkeIOhk3yXq1e8rmrF9qXIXKiP8eCQMyCd2LQsdCMTo0_D94NCLxy7Y9Lld8Mf4P_x9zm1kQbHrzdTmIWErVwv2yyAuwaHZ4TND6cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در ویدیوی منتشرشده از سوی سنتکام درباره عملیات نجات خلبان آمریکایی، هلیکوپتر به سمت راست گردش می‌کند، اما سایه آن همچنان در مسیر مستقیم به حرکت خود ادامه می‌دهد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/690157" target="_blank">📅 18:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
محموله‌های نفت خام ماه سپتامبر عربستان لغو شد/ نفت برنت به ۱۰۸ دلار رسید   رویترز به نقل از سه منبع آگاه:
🔹
عربستان سعودی به مشتریان اروپایی خود اعلام کرد که برخی از محموله‌های نفت خام برای اواخر سپتامبر لغو خواهند شد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/690156" target="_blank">📅 18:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=NTnz20U3i7t7QMPx6YIUaQf_tnEKF3l1jI8wgRyFXwNBUwPGYUo0diU1M9Wgz7oFjYkO77rn6dW6h10hFvg4rr9ynaWdJf4_8sbmtMqcFBsi09kv8VQAtRAoKTSHQOt7cUK2oOn4XgWgzbeX1hH6jtS5MHcLaDW0VK7HZPLs8fn30DDxOWr0xfqa24CEYgoBu7TUr1SC-pPPsMQbABGmLaAEy7a2ibycn8br-Xeiw3x8dc7Er3io9j_rxB87GAUjWe6lIje73ivPQR20kwaxoInQYRXS9occV-avzLGX3tMo-m6zreuUri1YPkjGtMMg-yGt-pRQzd_E2biWKbGYRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a1a4b63c66.mp4?token=NTnz20U3i7t7QMPx6YIUaQf_tnEKF3l1jI8wgRyFXwNBUwPGYUo0diU1M9Wgz7oFjYkO77rn6dW6h10hFvg4rr9ynaWdJf4_8sbmtMqcFBsi09kv8VQAtRAoKTSHQOt7cUK2oOn4XgWgzbeX1hH6jtS5MHcLaDW0VK7HZPLs8fn30DDxOWr0xfqa24CEYgoBu7TUr1SC-pPPsMQbABGmLaAEy7a2ibycn8br-Xeiw3x8dc7Er3io9j_rxB87GAUjWe6lIje73ivPQR20kwaxoInQYRXS9occV-avzLGX3tMo-m6zreuUri1YPkjGtMMg-yGt-pRQzd_E2biWKbGYRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهکار عشایر برای عبور گوسفندها از رودخانه
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/690155" target="_blank">📅 18:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690153">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIrmZD6AGuHYVvy2KcmkbEcSZkpcrCfkCroc31XkJN_hP2LtIQnlsVByU7Zt2hdX2CwG-1YgEKT7yB6INI50sozM43BExOHlGzdqeqRoUwqE0FkD9pYxhgoablBlu0VGK3ooAOKoxpziWiM871vnbYGW6lNUGC4PEpIYj8-pGwZ-ZTesgY7NSyRuqv4YwtYxIunssHdZ8s7HnY8vvmx2osiFxyaMVcFEJlnUkRUdjHIqDwFnQo_0STImi0b4EX58I9KIslhWC8C8EjuTnaUZr73VGZPimMMpSisezSqF2nqGc3O9JH5QIRRvX6BFwHpAqFs5RJPJR6hhKbexTgUtiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محموله‌های نفت خام ماه سپتامبر عربستان لغو شد
/
نفت برنت به ۱۰۸ دلار رسید
رویترز به نقل از سه منبع آگاه:
🔹
عربستان سعودی به مشتریان اروپایی خود اعلام کرد که برخی از محموله‌های نفت خام برای اواخر سپتامبر لغو خواهند شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/690153" target="_blank">📅 18:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690152">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
حضار کنگره آمریکا با شعارهای (نه به جنگ علیه ایران)، بسنت را تروریست و جنایتکار خواندند و صحبت‌های او را قطع کردند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/690152" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690151">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d207f274.mp4?token=Ijia8mfywiwlAJo14WNhD4pJaLnhHivmiMpWMRD9qpM3ODnxtixJXXpdISgnHfVEsVzn4yoSow2L2b49SbUkf_RCieeIMdQ6amdtYGi3gzTJlgjHZbpqLubmrSgKOYJONDxGLY0B_C6bJY2X92DdTFku0juSukYIPZVkbLFgXTJitK31YS-wO4Tdry5NQ59axEcGW2QOnOdJ4KmjAk7uNBtAWqU4N1RdA1hERA3_ItRXLQSt3bI2B3klWu5qrZWjgU194W_BgPr-hSaEcCbsUuVT9f6lqVmFNV4c7Gk4ZDvil2XyjCNwCEmoMkGlRqTBmQLV57VAmnRm_CDnnFoBXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d207f274.mp4?token=Ijia8mfywiwlAJo14WNhD4pJaLnhHivmiMpWMRD9qpM3ODnxtixJXXpdISgnHfVEsVzn4yoSow2L2b49SbUkf_RCieeIMdQ6amdtYGi3gzTJlgjHZbpqLubmrSgKOYJONDxGLY0B_C6bJY2X92DdTFku0juSukYIPZVkbLFgXTJitK31YS-wO4Tdry5NQ59axEcGW2QOnOdJ4KmjAk7uNBtAWqU4N1RdA1hERA3_ItRXLQSt3bI2B3klWu5qrZWjgU194W_BgPr-hSaEcCbsUuVT9f6lqVmFNV4c7Gk4ZDvil2XyjCNwCEmoMkGlRqTBmQLV57VAmnRm_CDnnFoBXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضار کنگره آمریکا با شعارهای (نه به جنگ علیه ایران)، بسنت را تروریست و جنایتکار خواندند و صحبت‌های او را قطع کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/690151" target="_blank">📅 18:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
خبرفوری/ انهدام یک پهپاد MQ1 دیگر در شرق تنگۀ هرمز   سپاه:
🔹
لحظاتی قبل چهارمین MQ-1 در چند روز گذشته به وسیلهء آتش سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان شرق تنگه هرمز رهگیری و منهدم شد.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/690150" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvtr9ZTexWNhqvEe20B--ndoCrlOw6uNGlnU3JMifZCRtRwiCvuvCNWPaMHOsH8JTbMmto_hOYpwNbIT_E3kiwXbzjh130CjIU2pO_Z3IENU7rOUcckkQpqFIQ67KGOSQlRgLYTp9JO3FOOQinygorcvYDass5KwBP6hW62jq0wgEHaQHn5TKG0BSeORdf4tXzInCnEfbb8CyHMzpnLRFFS2bMhFoQ0WW_LqlDFZOEHT9HPQBneUjxEmwNMwJgY5LF_zZCaBa2kzCxk9lue0ql0-thuwwlax4FKjbKRNFk0Jy5u_39VUr92lxv5tVevdx-dkLJQueT7_u0ACimdFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همت راهداران از پسِ خرابی‌های جنگ برآمد؛ پل بیات به زودی زیر بار ترافیک می‌رود
🔹
مدیرکل راهداری و حمل‌ونقل جاده‌ای استان آذربایجان‌ شرقی گفت: پُل بیات در آزادراه تبریز ـ زنجان که ۱۸ فروردین ماه سال جاری بر اثر اصابت موشک‌های دشمن آمریکایی - صهیونی دچار آسیب شده بود، با پیشرفت فیزیکی ۹۵ درصدی در آینده نزدیک زیر پل ترافیک می‌رود.
🔹
عبدالحسین علی‌اکبری با اشاره به تخریب دو دهانه میانی پُل بیات، اظهار کرد: پس از گذشت حدود چهار ماه از آغاز عملیات اجرایی این پروژه، در حال حاضر مراحل نهایی بتن‌ریزی در حال انجام است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/690149" target="_blank">📅 18:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYrmV1FmicLHrLEb3f5fO162ttNQYV-tuvhVna-hUIbKrz01Tk0XoPXebbVH_7wnv0qlOaImGh570q_3_1p8jIgZUAMXcm9sTvxN1kdaQyv9lp5afLjG_6-1HTF0P2Q7dPIHvgVFAHzWEBckYDhEHnjU8vm06Xmu7kudPD8VCcDENrou_QjXyMmrVlMRMakf4AKcN30LlM3rQIJWrNfpZFX3agG40mnKyJPt4WZ8SJPz2yHjyjoeIBk6mKBPxJklvxlypgpWlxzZ4s6mbKjHLf-_Av5wQgGqxd61wCOzSoedRSSDl4bbibpjAGz9eUUzeP5wiK7S6AgZG9v8nsofgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنایات آمریکا، تروریست شماره یک دنیا
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/690148" target="_blank">📅 18:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a91ec24c8.mp4?token=l3UX2RRgy84bNlrU-paxoFz1GBJ23sOxtFf7LwETL9dQ3RzoVytPW2iRWoF0ZVEMPwLplFRl3UCr-HRLqfd6uVWPTKOow0V9WSzbtmYamv-ZJPW4gACiydG3ljdCfadOFHaG9ucpOH_E9BVs8NAEW7YXtXiRZZkF45Pgzz-zKstgWqtMVBLQt2nd2g5LKTIwgIKb69CsEw6XNHoNzHBkxEk3VZZORo8vSDsPy3Jy9aQlAbMkATlax6rmv2jzzxfhVmSVW9PVeRjqq5BFuk9_SdW_-fhO8HWNuv6wwntuSK5KK4ZNd6bahXPjJz_Stb7ZiI4NXKfRgPJUKXvkS_GMwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a91ec24c8.mp4?token=l3UX2RRgy84bNlrU-paxoFz1GBJ23sOxtFf7LwETL9dQ3RzoVytPW2iRWoF0ZVEMPwLplFRl3UCr-HRLqfd6uVWPTKOow0V9WSzbtmYamv-ZJPW4gACiydG3ljdCfadOFHaG9ucpOH_E9BVs8NAEW7YXtXiRZZkF45Pgzz-zKstgWqtMVBLQt2nd2g5LKTIwgIKb69CsEw6XNHoNzHBkxEk3VZZORo8vSDsPy3Jy9aQlAbMkATlax6rmv2jzzxfhVmSVW9PVeRjqq5BFuk9_SdW_-fhO8HWNuv6wwntuSK5KK4ZNd6bahXPjJz_Stb7ZiI4NXKfRgPJUKXvkS_GMwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین فیلمی که ادعا می‌شود مربوط به عملیات نجات خلبان F-15 سرنگون‌ شده آمریکا در ایران است
🔹
این تصاویر برای نخستین‌بار لحظات عملیات نجات خلبان پس از سقوط جنگنده آمریکایی در خاک ایران را نشان می‌دهد.
🔹
در این گزارش ادعا شد که خلبان آمریکایی با استفاده از…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/690147" target="_blank">📅 17:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=qxrdMkIPJIQd8OYrTlPDiZ0JWipht9Z7z7V6UKi1pJiUfZNBNi7dC4hjZbKV6AK8t1yFTyXj6kcU1Pvh1-5ApatRUZaAiNkzZ7SlgHrdXSAGiHOxxpQbpus_9VJ3w0jt98Amg319Yt5rbzYUytQJge86d_WNpqMwdxHXo8T4-n1Cyj8JtLQ0Mt4jXyvq-efiu4MRzOUeIX2ECejWpmUN90bEVCz1WBMvgZgY3sxwq18AUFckot_LX47aujpHscXt_fG9aQNMYuOikhW0iiEnVH6eQpC5CUhVM0JIVP6C8QVM_924NH1X2_MBfcSLU4tkqp-Woz7WaW8LfNK3yWEYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f9b252d2.mp4?token=qxrdMkIPJIQd8OYrTlPDiZ0JWipht9Z7z7V6UKi1pJiUfZNBNi7dC4hjZbKV6AK8t1yFTyXj6kcU1Pvh1-5ApatRUZaAiNkzZ7SlgHrdXSAGiHOxxpQbpus_9VJ3w0jt98Amg319Yt5rbzYUytQJge86d_WNpqMwdxHXo8T4-n1Cyj8JtLQ0Mt4jXyvq-efiu4MRzOUeIX2ECejWpmUN90bEVCz1WBMvgZgY3sxwq18AUFckot_LX47aujpHscXt_fG9aQNMYuOikhW0iiEnVH6eQpC5CUhVM0JIVP6C8QVM_924NH1X2_MBfcSLU4tkqp-Woz7WaW8LfNK3yWEYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اختصاصی شبکه ۳ از نفتکش هدف قرار گرفته‌ شده در نزدیکی سواحل عمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/690146" target="_blank">📅 17:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690145">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
وزارت علوم: دانشگاه‌ها در نیمسال اول پیش‌رو حتما حضوری خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/690145" target="_blank">📅 17:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
نیروهای مسلح یمن: یک کاروان نظامی وابسته به عربستان در منطقه «العبر» استان حضرموت هدف حمله پهپادی قرار گرفت؛ برخی رسانه‌ها از کشته شدن ۳ نفر و زخمی شدن چند تن دیگر در این حمله خبر داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/690144" target="_blank">📅 17:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMkCfPfQrOUp1wTJLSgf2UHd3a0WFx4ttT2iEOIVnIZiMtk_xPzYHL_KcsSF2MPTMzGXq3RQ3E2WcsrlFjjoVymUldsE8_1e_dS43hvB-XhFDTM1BAayQ5g8TfSDuOypYNv2dmHnYojLexBbH0TKR16EUAx_QDfzaMUTF0myujLln3xE0qPI3na--YPgjg2gUJHyB38GQdgwhhHgogWM6bUJrS5k_HYk1DANjNxaoBu00iK2D0yijDv6_BQuDtPaXpC0kaNj8akDUfmLxcbYoBW3w7hpN4YjdJPxyNl5F2mbiF1dYSMn79VgC9nJKlb0trICXWdv5i8Ktl_sYSiIWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا پرستاران مهاجرت می‌کنند؟
🔸
در این نظرسنجی بیش از ۲۸ هزار نفر شرکت کردند که سهم روبیکا ۴۸، بله ۲۵ و تلگرام ۲۶ درصد بوده است.
🔸
بیش از دوسوم شرکت‌کنندگان حقوق و مزایای پایین و ۱۰ درصد هم احساس تبعیض در نظام درمان را مهم‌ترین عوامل در افزایش موج مهاجرت پرستاران می‌دانند.
🔸
تداوم نارضایتی از شرایط شغلی پرستاران، مهاجرت آن‌ها را به تهدیدی جدی برای تأمین نیروی انسانی و پایداری نظام سلامت ایران تبدیل کرده است.
@amarfact</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/690143" target="_blank">📅 17:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690141">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f67759b99.mp4?token=tubHrLrR_7p6brUM07jpmXh7Ri31_GZWeANCnB-z9c5stEl1VW9AGHudA5NKd361rKsv0yuEKAYfqMXWB-RySLtOLnglebnjl5LA6ecL-sVrCfn3N69t1V5iQJ2pdAddM9BcMQ1IjvkJh3oVCUkuHR8UoeaOj8b6h1cbdBWMWIDyCxSlNMF_ipTdGW0B2aV9CwEWHZMJu8eFGjTlpcQeB85QQareGWz24uhOEQTl4xGKN_lAG3uK0ipNi-qX4dt9l_Dbc8WZVmvLfrEqIENDKoR11ciaP_F8VzQaIouTye-_A96y23Kzs3Vv50F2GzfDvo9sEVGJXaqHaB0OZMEKWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f67759b99.mp4?token=tubHrLrR_7p6brUM07jpmXh7Ri31_GZWeANCnB-z9c5stEl1VW9AGHudA5NKd361rKsv0yuEKAYfqMXWB-RySLtOLnglebnjl5LA6ecL-sVrCfn3N69t1V5iQJ2pdAddM9BcMQ1IjvkJh3oVCUkuHR8UoeaOj8b6h1cbdBWMWIDyCxSlNMF_ipTdGW0B2aV9CwEWHZMJu8eFGjTlpcQeB85QQareGWz24uhOEQTl4xGKN_lAG3uK0ipNi-qX4dt9l_Dbc8WZVmvLfrEqIENDKoR11ciaP_F8VzQaIouTye-_A96y23Kzs3Vv50F2GzfDvo9sEVGJXaqHaB0OZMEKWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خلبان آمریکایی که در ایران نجات داده شد: چتر نجاتم در حمله اولیه آسیب دید و به طور کامل باز نشد
🔹
با سرعت ۱۶۰ کیلومتر در ساعت به زمین برخورد کردم و در این حادثه، ستون فقرات، بازو و شانه‌ام شکست. با وجود این جراحات، از دره‌ای که فرود آمده بودم، یک مسیر کوهستانی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/690141" target="_blank">📅 17:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
مشاور دفتر رییس جمهور درباره لایحه مقابله با نفوذ: به مقدار کافی نهاد برای شناسایی نفوذ داریم/ با این طرح‌ها کسی در کشور نمی‌ماند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/690139" target="_blank">📅 17:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4775902ea2.mp4?token=Xe4GXY9bG_0H1q99Z84LEwDWMtUrGQw6De1QvGILzAK-vde6LI_QjyK--Myx8jc1cLHM8gwX_m-yfyJ0OZvRwd_1zKbcFAegICXimHf5o5MApMmL1_O6hI4A4sAciEErfNPS7ZuLXnyST2Y63mE6LNPQhyi6rkydhd5m-Ytk4wXT4OJpflG60IOi--B6RM1PBaCcuqJwJmAnZ1vSUKAcRYBWHpAAwZU9agt267lUegC6GpEI1Pd28s-FgeMLqXs1vVpMkromOF4BbQmn_Stgkp2LP0KxIlFzNKYI6hA2s5dF_5rLz6uNhrpTkLvxf_8iRwvkmjuNAdKOeNj47yyhdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4775902ea2.mp4?token=Xe4GXY9bG_0H1q99Z84LEwDWMtUrGQw6De1QvGILzAK-vde6LI_QjyK--Myx8jc1cLHM8gwX_m-yfyJ0OZvRwd_1zKbcFAegICXimHf5o5MApMmL1_O6hI4A4sAciEErfNPS7ZuLXnyST2Y63mE6LNPQhyi6rkydhd5m-Ytk4wXT4OJpflG60IOi--B6RM1PBaCcuqJwJmAnZ1vSUKAcRYBWHpAAwZU9agt267lUegC6GpEI1Pd28s-FgeMLqXs1vVpMkromOF4BbQmn_Stgkp2LP0KxIlFzNKYI6hA2s5dF_5rLz6uNhrpTkLvxf_8iRwvkmjuNAdKOeNj47yyhdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عامل پرتاب کوکتل مولوتوف در میدان پونک دستگیر شد  مرکز اطلاع‌رسانی پلیس تهران:
🔹
فردی که سه کوکتل مولوتوف به سمت شهروندان پرتاب کرده بود، هنگام تلاش برای خروج غیرقانونی از کشور شناسایی و دستگیر شد.
🔹
این فرد در جریان دستگیری با مأموران مقاومت کرد و از ناحیه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/690137" target="_blank">📅 17:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اف‌بی‌آی مدعی خنثی‌سازی حمله داعش در پنسیلوانیا امریکا شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/690136" target="_blank">📅 17:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAug2aoRdGazoxEBwjtQH_T0rAP92Oe8jn1GBxtP9mEl0U_zDANJFI9uxAqqpLEcFQLVd5W8hHChpW7xr6TOmfIAf3_zogEg9_Q2jzwpFoJzYuipxwhqoFDnyIobquFUxcQkLO5PjMtizouqPXgcRx2pc0NvGOVdkirJY44eBxuK1lUmp6ufP_L_cIbpXo58HQQRCq4kM7uSfZIMWfvXP1ATtd7KtzXLVRgoa7-yOCagoJ__1fKUlbXhIqWMPrDuXbzA90GNGDIHspMFmeU6-w8EYoDoA5wXVbvqj3qwO7bniorf5YNc5H03wvG6_wET35LAJuqbDAEus8VvzDAviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✈️
خرید قسطی خدمات سفر در فلای تودی
🔹
فلای تودی با هدف رفع دغدغه هزینه‌های سفر و ایجاد انعطاف در شیوه پرداخت،
سرویس خرید اقساطی
را به خدمات خود اضافه کرده است.
🔸
با این سرویس، کاربران می‌توانند بلیط
هواپیما،
قطار
،
اتوبوس
و
هتل
را در مقاصد داخلی و خارجی رزرو کنند و هزینه آن را با اقساط 4 تا 24 ماهه بپردازند.
🔹
این قابلیت بخشی از توسعه تجربه خرید در فلای تودی است. تجربه‌ای که در آن، علاوه بر انتخاب خدمات موردنیاز، شیوه پرداخت نیز متناسب با شرایط کاربر در نظر گرفته می‌شود.
برای مشاهده جزئیات و رزرو خدمات، به لینک زیر مراجعه کنید:
👇
🌐
خرید اقساطی خدمات سفر
کسب اطلاعات بیشتر
:
☎️
۰۲۱-۴۲۴۰۵۰۰۰</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690134" target="_blank">📅 17:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای آکسیوس به نقل از مقامات آمریکایی: ما دیروز دو قایق ایرانی را پس از تلاش سپاه پاسداران برای توقیف کشتی ما در هرمز، منهدم کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/690133" target="_blank">📅 17:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKtUbPAbV-UPE1Z-DKqyE-Z2FkSji4KQuJVhMHCUFYZwZaesbsF1ui1zqlAYCGdeNC1_RzXQQcYJcPOCVjVB4ZGuxHFbT8ZulC_CMqbcCrhoZE_L_2fEJMr5Z9CY3VBk983E3MG92zzqM4pe7AtqsNsXe0YQVUvZW7G9Rhybx7PKHKhC9Am1dGMIh71GVbuN2Tg5bS6sgU53aYajeeErf_V6fibpKOXWOpxQJktvejghQPN_ThxFsHy6yn6o6vMnqxDpxii5h2faB9Ztlv5AhbGEzli9jUzDWuXsB3vn1M9iZ-Ay_6y2UMDK8Norz4xz6Fzvyy5L9_xxCTaPC7Dh9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد: آقای پزشکیان! آقای کاظمی! زنگ مهر امسال را به نام دانش‌آموزان مدرسه شجره طیبه و با روایت قصه میناب به صدا درآورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/690132" target="_blank">📅 16:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eda0fef9.mp4?token=EMnkJxinla-sgLrJ2N2YL41VyakEuZCC9kZkn044hg7dAjbWUTh4FbKQMYGo_7Q5KpUAATESbDjrxYLD8_vX_Q5eeomCHxMxIn8cpix2IgArGsMJCNjZHOORYiM98qsvKPgGA_eIDAtpt8KOmEtCQCIDaJnIxcKObfu95HiKRu8LCwqSXSIA_AGZtTYGtBVBloAxHH1MPnTg4JvpDRDpsVFBbAMNJ7bYZao-M-yvUnrdhwWMtsTOrSeic54ZLMIEHRU8zTLIhrdbeCyQVmNWPZrGdJoSyUv7f6rYLupMIpKkUE-7vON7NqobNttZs2_NkSW0hjYrxXOWWeJqzcbu2in8mSPTB1cH2w_ijZgpLoFnpuNOxI1f5cHUGGqn19j3EbzW1AXaxmSxiCF9YI3bphgAdUtonqY069eNtAkmpIVvnveNkgnXHECa1_FU-btGdgEmJit6Re8MRxlN6XQVfYvpiXgp-qUKx80BSX1lJOWgLv5Pos5o7h_UvjJMbDZDyiunMklK-9kKzMroha5_igjJbjPdM17x5hRfaXTeDXXz_Xmg3F-8GOV1laFS62rzzaOANh0HThFwO05wumbXnpVGAI96lY-j7izzvQj-K3SSF_stz_VGzdPhCtveqXLLUIIklR-rp-WT7xv5lpNqoHnUv1kFB6ZvCUasOT0pVeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eda0fef9.mp4?token=EMnkJxinla-sgLrJ2N2YL41VyakEuZCC9kZkn044hg7dAjbWUTh4FbKQMYGo_7Q5KpUAATESbDjrxYLD8_vX_Q5eeomCHxMxIn8cpix2IgArGsMJCNjZHOORYiM98qsvKPgGA_eIDAtpt8KOmEtCQCIDaJnIxcKObfu95HiKRu8LCwqSXSIA_AGZtTYGtBVBloAxHH1MPnTg4JvpDRDpsVFBbAMNJ7bYZao-M-yvUnrdhwWMtsTOrSeic54ZLMIEHRU8zTLIhrdbeCyQVmNWPZrGdJoSyUv7f6rYLupMIpKkUE-7vON7NqobNttZs2_NkSW0hjYrxXOWWeJqzcbu2in8mSPTB1cH2w_ijZgpLoFnpuNOxI1f5cHUGGqn19j3EbzW1AXaxmSxiCF9YI3bphgAdUtonqY069eNtAkmpIVvnveNkgnXHECa1_FU-btGdgEmJit6Re8MRxlN6XQVfYvpiXgp-qUKx80BSX1lJOWgLv5Pos5o7h_UvjJMbDZDyiunMklK-9kKzMroha5_igjJbjPdM17x5hRfaXTeDXXz_Xmg3F-8GOV1laFS62rzzaOANh0HThFwO05wumbXnpVGAI96lY-j7izzvQj-K3SSF_stz_VGzdPhCtveqXLLUIIklR-rp-WT7xv5lpNqoHnUv1kFB6ZvCUasOT0pVeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نامه سردار سید مجید موسوی فرمانده هوا و فضای سپاه در پاسخ به نوجوانی که با پویش حفظ جزء ۳۰ محفل ستاره ها شروع به حفظ قرآن کرد
🔹
از اینکه شاهد رویش‌های نسل جدیدی از فرزندان مومن و متعهد در کشور عزیزمان هستم بسیار خرسند و مسرورم و مطمئنم تا زمانی که همچون شما دلیر مردان جوان، با ایمان به خدا و روحیه جهادی در این کشور رشد می‌کنند دشمنان ایران اسلامی ما عاقبتی جز شکست نخواهند داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/690131" target="_blank">📅 16:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
وزیر کشور، برای دیدار با مقامات ترکیه، عازم آنکارا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/690129" target="_blank">📅 16:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
استانداری هرمزگان: شامگاه دوشنبه دو فروند قایق صیادی در حوالی بندر کرگان در آب‌های خلیج فارس مورد حمله پهپادی دشمن جنایتکار آمریکایی قرار گرفتند
🔹
در پی این حمله، تعدادی از صیادان حاضر در این دو قایق مفقود شده‌اند و عملیات جست‌وجو و امدادرسانی برای یافتن…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/690128" target="_blank">📅 16:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc8c949d2.mp4?token=F8yYyvVs8Wa0dHCN0E2t-E0IhNoIXGlHMGWNUBarAGCXHd_zxnVqhqbNB_kAR_E7l2QSqz_y_mhu-0b6UWl4oViBC6TSagjvvmh54DG2bn0UsxJ10lUCPDaDT1qy22y1tk-yr5vOCyRgk3_5wLwqRwkx5ht5ZVLgNv-wXR3U0vcLZhPyXIToU1fwVz6MXwT88KhBan2BtS1VroMSAli53zjgqFFppYlg-gKF5Z8mdIFg2bEjoBRjZ5QJaGnAylkBtxPGB3cH1R6B1dAcInS-GzTUDjJVT-G82UhVz5y48NCTvbzz8_Lkzhbrvjg6m6fykUrYH6ZoCeYPLyvCrsDslg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc8c949d2.mp4?token=F8yYyvVs8Wa0dHCN0E2t-E0IhNoIXGlHMGWNUBarAGCXHd_zxnVqhqbNB_kAR_E7l2QSqz_y_mhu-0b6UWl4oViBC6TSagjvvmh54DG2bn0UsxJ10lUCPDaDT1qy22y1tk-yr5vOCyRgk3_5wLwqRwkx5ht5ZVLgNv-wXR3U0vcLZhPyXIToU1fwVz6MXwT88KhBan2BtS1VroMSAli53zjgqFFppYlg-gKF5Z8mdIFg2bEjoBRjZ5QJaGnAylkBtxPGB3cH1R6B1dAcInS-GzTUDjJVT-G82UhVz5y48NCTvbzz8_Lkzhbrvjg6m6fykUrYH6ZoCeYPLyvCrsDslg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
فیلم وحشت مسافران در پرواز کرمانشاه به مشهد
🔹
ویدیویی منتشرشده از داخل پرواز کرمانشاه به مشهد، لحظاتی پرتنش و دلهره‌آور را نشان می‌دهد؛ در جریان این اتفاق، بخش‌هایی از کابین هواپیما دچار آسیب و شکستگی شده و مسافران لحظات پراسترسی را تجربه کرده‌اند./رکنا
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/690127" target="_blank">📅 16:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
استقلال با نخستین پیروزی آسیایی مقابل السد، ۱۰۰ هزار دلار پاداش کسب می‌کند؛ حضور در لیگ نخبگان نیز ۸۰۰ هزار دلار پاداش دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/690126" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0bc4d3c9.mp4?token=pCCIUmKwK3nUv2DWBr5ES6d5N5-XDmhmrdzuHnMEgw72ra5d0TprvkQyVpPTfO2MkbEqASMjtqVa9KtJd6kbTzMW6FVIdRfrZKKqGJkqxfYNghGijcICurdyM8_-exx7c7YvfSXewgpeaNguhzlFsrQRG_nKvXjGykyCyf6GdMxW2xtkp7G6ElYwa6s8IM8YO4l0poQLvF6XJGbg6vIbbwKsXujSByc6a-ytGWSyi4aYJqS5v9ztb_fK9dHQWYGMYsU47J_Yj85U6GlAijdr-EqcldGbaAOaio1ls_4Jbke4GFxteWlDm6pQdvbq5ljcXhmT3buPmjg7Z_mnqJj74g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0bc4d3c9.mp4?token=pCCIUmKwK3nUv2DWBr5ES6d5N5-XDmhmrdzuHnMEgw72ra5d0TprvkQyVpPTfO2MkbEqASMjtqVa9KtJd6kbTzMW6FVIdRfrZKKqGJkqxfYNghGijcICurdyM8_-exx7c7YvfSXewgpeaNguhzlFsrQRG_nKvXjGykyCyf6GdMxW2xtkp7G6ElYwa6s8IM8YO4l0poQLvF6XJGbg6vIbbwKsXujSByc6a-ytGWSyi4aYJqS5v9ztb_fK9dHQWYGMYsU47J_Yj85U6GlAijdr-EqcldGbaAOaio1ls_4Jbke4GFxteWlDm6pQdvbq5ljcXhmT3buPmjg7Z_mnqJj74g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترکیب خوشمزه و مقوی با خرما برای یک میان‌وعده پرانرژی
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/690125" target="_blank">📅 16:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A37w4d_YUvuXv6iz_WAYth--wlWUv4xZaLUOTqynX4THTsWwRtyFhsno0mVzfYKQNgjTnQc_Cp4AxQSjxtT3FNUilb8vBYBc7-GkaDx1nJ8hp1fW-qZur-BB_gMQRj_xTvHeELEicDn-1t9mGS6-Zg74iIKyTFxxoh_T66DMUcHu2baaxiHLpSm1wzYmxb1dsJZZC_KPvJOHSAsVMDshi-AhwxJtlPtbLtkA-kujENAyDvqMwuhMaq4ab7dnae5k1tGbP5V4gQ6sp07YnkqrCKz4qzkMSyPSOc22Ztau98Jhe2yu_hzkArAqYuMdE0z2CAAEXIX_BYC6NqU5rvDKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دوره‌های آموزش نظامی و امدادی یگان‌های مردمی جانفدا امروز ساعت ۱۷ از طریق ارسال عدد ۱ به سامانه ۳۰۰۰۱۱۵۵ یا سایت
janfadaa.ir
🔹
نکته مهم: با توجه به محدود بودن ظرفیت دوره‌های آموزش مقاومت ملی جانفدا اولویت با کسانی است که زودتر ثبت‌نام کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/690123" target="_blank">📅 16:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0869ece7.mp4?token=RZNjqnFXUtOlfmAXXX6FTiE0iAqzEb8hba1dWzFiNKCoLrP8XEQEkGzhKOie4lEHONXGF1YJGSCueuhb2JHLX9gw3o5BqDIVpf4Aal1OVU9TNwKIVi6FuSSKbi8iNS59oyw1VeM4rUJAN6WUl4fYelPaYR0XlPCqy1Tc1jAjKTaSE7SeGuXf0TTCequHvcizRxQ9rJzu7GaCTJq2y_IbvfPTlmt-lhuhFCsMnvQFACsj5WCYiqmS1q7S6FYGjII-I3H3HTwdPyOsuXpiKLnNz9PU3zLlON3m_vagoMUdrHhZI1NVvfc-lwFlCN1AR5Q7a0GfvXS8qXee6jv2LcFSJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0869ece7.mp4?token=RZNjqnFXUtOlfmAXXX6FTiE0iAqzEb8hba1dWzFiNKCoLrP8XEQEkGzhKOie4lEHONXGF1YJGSCueuhb2JHLX9gw3o5BqDIVpf4Aal1OVU9TNwKIVi6FuSSKbi8iNS59oyw1VeM4rUJAN6WUl4fYelPaYR0XlPCqy1Tc1jAjKTaSE7SeGuXf0TTCequHvcizRxQ9rJzu7GaCTJq2y_IbvfPTlmt-lhuhFCsMnvQFACsj5WCYiqmS1q7S6FYGjII-I3H3HTwdPyOsuXpiKLnNz9PU3zLlON3m_vagoMUdrHhZI1NVvfc-lwFlCN1AR5Q7a0GfvXS8qXee6jv2LcFSJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ملک بخریم یا طلا؟ کدام تصمیم بهتری است؟
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/690122" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888f1a581f.mp4?token=LXl1WKAUd7h6gK2mc-A9NEzZqk25qYdojjg7-1awqceH4VVwltLJoeFAs53wWZu-75w5N4tZYFtPQbfoh6nCyGIkxHaMvDT6ecb05oCzZPtjlL8u5cyZqxEtfhfG1jEopEGfEDBDRtq2sEynD4A21XD82pqZsKOxMPmK00LRsDUTU61GYwWvfzKS2Qn8imblWCDwlyR2-4rFpevTX146xdkXKlj5yC0FcPZbNz83DfUt9kcKWFaPke2o0npmGwGt0LYR__suspg24Kp6Hv0bJlrsDWjgjMiVCLrQ-06egArmLMYBNldpw3YwJKGmhqDiqavnpaPKW_ajsMZrIupMlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888f1a581f.mp4?token=LXl1WKAUd7h6gK2mc-A9NEzZqk25qYdojjg7-1awqceH4VVwltLJoeFAs53wWZu-75w5N4tZYFtPQbfoh6nCyGIkxHaMvDT6ecb05oCzZPtjlL8u5cyZqxEtfhfG1jEopEGfEDBDRtq2sEynD4A21XD82pqZsKOxMPmK00LRsDUTU61GYwWvfzKS2Qn8imblWCDwlyR2-4rFpevTX146xdkXKlj5yC0FcPZbNz83DfUt9kcKWFaPke2o0npmGwGt0LYR__suspg24Kp6Hv0bJlrsDWjgjMiVCLrQ-06egArmLMYBNldpw3YwJKGmhqDiqavnpaPKW_ajsMZrIupMlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر: در فدراسیون کشتی جاسوس داریم؛ ۳ سال برای مجوزهای معدنی دویدیم وگرنه باید گشنگی بکشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/690121" target="_blank">📅 15:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/An8W2aYFUG73q8jMZTtxtzr5Y_C58pxYuLKCJsnIX3cCpSuEgXsvRq-2fGerQKjQCS0nkEp2J3x8vwYPGfGT-q3gVr_aH62pvVKgCCCfVv1zHAYJN5sHwt0LOfH4JHHzfXx6-QVPibWkgXqCzImi2mzEF3RL9XjsPYPuiyKKwqd4lFhZJhcY4qWA_DqbfVCJepsmdb7mJWCMFuIcS-QDh47NWsh0GtABtjK0xZAx_CcC1B4YwnDA5u1B6jCRU55Ysi2WJkyApHjrOWKORubC9yJU9WaIQdqXlCcRZScJp6WjrCecuRRLN4Xkom_BFaUxcdgWIyHF8iWtlx-qAQv_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بریکس؛ فرصت فعال‌سازی دیپلماسی معدنی
سیدعباس حسینی، عضو هیئت عامل ایمیدرو:
🔹
در بیانیه پایانی اجلاس سران بریکس در دهلی‌نو، برای نخستین‌بار بندی مستقل به «مواد معدنی حیاتی» اختصاص یافت. چندی پیش نیز چنین اتفاقی در اجلاس سران گروه ۷ رخ داده بود. این تحولات نشان می‌دهد اهمیت مواد معدنی حیاتی و رقابت جهانی بر سر آنها در اقتصاد سیاسی بین‌المللی، هر روز ابعاد گسترده‌تری پیدا می‌کند
🔹
از سوی دیگر، نخست‌وزیر هند، به‌عنوان رئیس اجلاس بریکس، نسبت به «تسلیحاتی‌ شدن فناوری و مواد معدنی حیاتی» هشدار داد. این موضع را باید در متن رقابت فزاینده بر سر عناصر نادر خاکی و دیگر مواد معدنی راهبردی فهم کرد. چین در بخش بزرگی از زنجیره فرآوری عناصر نادر خاکی، نقشی تعیین کننده و مسلط را ایفا می‌کند؛ هند به دنبال کاهش آسیب‌پذیری خود در برابر تمرکز زنجیره‌های تامین است؛ روسیه و برزیل از دارندگان مهم منابع معدنی جهان به شمار می‌روند؛ کشورهای آفریقایی عضو بریکس نیز از ظرفیت‌های معدنی بزرگی برخوردارند و در عین حال به سرمایه، فناوری و زیرساخت نیاز دارند.
ادامه خبر در
👇
https://www.titrtejarat.com/fa/tiny/news-10937
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/690120" target="_blank">📅 15:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6cfc2473a.mp4?token=WQNpFi0EnOPhi1_yWso-TvWaRxf-R6xTsbvMyN6P_vg35Gr-EF3SsJXGao9EaWGbJ2CHWp7erqDzdfzm3MGWFf1Xea5oH2FlyCwZzRef55MmKdZzOa1hMYlqs7PdAq5aTEjj1Xi7IXD2px83ZHU_dFMmcbOfakWCQnKyNr8PNKV1-voDaAkh9GySF3toKxdU1kGDaB4PiWcvbEiMY_bkpuGZJqDUlS46S9TkbxC6efTAS8DeJ45CFIWt-YWYTMyLabdqNlBIC3bvM2FMIekYSD58JuwzC2blE0VT9F6nFVnpSRQBMZHpuZwNLuTljVf-n5SNKaSXikXAT-hOBH0ywQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6cfc2473a.mp4?token=WQNpFi0EnOPhi1_yWso-TvWaRxf-R6xTsbvMyN6P_vg35Gr-EF3SsJXGao9EaWGbJ2CHWp7erqDzdfzm3MGWFf1Xea5oH2FlyCwZzRef55MmKdZzOa1hMYlqs7PdAq5aTEjj1Xi7IXD2px83ZHU_dFMmcbOfakWCQnKyNr8PNKV1-voDaAkh9GySF3toKxdU1kGDaB4PiWcvbEiMY_bkpuGZJqDUlS46S9TkbxC6efTAS8DeJ45CFIWt-YWYTMyLabdqNlBIC3bvM2FMIekYSD58JuwzC2blE0VT9F6nFVnpSRQBMZHpuZwNLuTljVf-n5SNKaSXikXAT-hOBH0ywQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون پزشکیان: حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و... را هم گران کنیم، می‌شود ۷ میلیون یارانه به هر نفر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690119" target="_blank">📅 15:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
واکسن آنفلوآنزا از اواخر شهریور عرضه می‌شود  سخنگوی سازمان غذا و دارو:
🔹
مردم به وعده‌های فروش واکسن آنفلوآنزا در فضای مجازی اعتماد نکنند. امسال واکسن‌ها از منابع مختلف از جمله چین، روسیه و فرانسه تأمین می‌شوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690118" target="_blank">📅 15:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsn7iJfqj9WD0yKVV-3cFgh0vpkJUJ0pFa1REAG8BGfLv7ZQIs_uNfeoSxx_dl2aCR2kv9NPW4JdN_xpXWw5Mn03xT1mzRoiziMU79_iui3GXpUKUEt1zfL_U5lcEUaktwp-x8w9yzB5FGHRg46bgYlU7GdXigSGUF2LMWQA_Y5y2jVn4rLQiQvaI0mNmAsz8T1Hqeo49igmh_Tyh25F10Q5ErvoFexOEXTMxtDXgu0scWRqCETgsN_fFmwEiZxu6WrAlOnu6Y6B8femyd9jAg4JOi3bwASOwOsnbacw50f3GSNkP-T9BgintBLxSCgeN0Dfp5oTa1MnKVb7fSGGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکوردشکنی قیمت گازوییل در آمریکا
🔹
میانگین قیمت گازوییل در آمریکا امروز به رقم بی‌سابقه ۶.۲۷ دلار در هر گالن رسید؛ رقمی که حدود ۲.۵۸ دلار بیشتر از قیمت گازوییل در یک سال گذشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690117" target="_blank">📅 15:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پاداش ریاست جمهور بدلیل فداکاری‌های نیروهای مسلح در جنگ رمضان، امروز واریز شد
🔹
ستادی: ۱۰ میلیون تومان
🔹
عملیاتی: ۱۵ میلیون تومان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/690116" target="_blank">📅 15:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690114">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JydaHfIyji_JyF8RWNGDgLvI7r2tFdn01sLh7x1Tzet8X6uh8oO2fCN50ziWTA3-TLrwrypNPg_7mjjnpmMY_DGMpvLp6w45OKL3QicTwAWNT8McSj-ORXVYrLTPHfE-7cmASokyXCgE11PhxVKQD3sFrfhzxjWszuUm0drDgKZ31BcTc3nhJKjbN9Z5t_AN7hDWXfqdi8DBSKUGRZ_3vC7jPUBiRyevW8Y7uNi87tys-PISN5ImYdvcecKnPlnDXU6AH3g2Qo394pRQgM1me_cpUnAp35z3_76IsdJedFM-c32lwHCiphndc14h40kMaT7aG3KZFDbgtJaYBqjttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F86NynLMNhZbNCxyZG43EYqVZJ3Dq0a4SzCyrfZv6MSp5oK00iHJESZ9S4HMF8zntVakJ_hagdxSXQQIzQeEFTfyv8WgNIKzswK9mbIOF5lIiEYzp_nB7JwTfWYTbWvaxQ-XwxQi1Cs-EYZa9Hp3YYPq-q3n6qi1EPSSM_vvi6NGNHW09RFPf4gHwey0cmdbM9Eq7xqmL1D8-EJduEkWxH6LPZ_DWeLyPnAAkO4RiUxJCU6IAFsWqXSbfePP6SW2Gxsnar-bz_O6sRCcOqRyReE0f_0GcTYlJDIO6Pe0OT0loK544zuwVNmRlI9rhQIgvvOyVanIWDuKqDBtwYefKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سوزش رسانه و ‌مجری شبکه ضد ایرانی اینترنشنال از فراخوان و سازماندهی داوطلبین جانفدا تحت عنوان آموزش های نظامی و امدادی
🔹
این جیغ بنفش رسانه آمریکایی-صهیونی پس از فراخوان آموزش نظامی و امدادی داوطلبین جانفدا که امروز ساعت ۱۷ از طریق سایت جانفدا
janfadaa.ir
انجام خواهد شد، درآمده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690114" target="_blank">📅 15:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690113">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIrK8U3K6IUVNhN-29A0wmm-6Pg7inDbQOUBAmcs1BTQ6Px6ms_E9DSRFHADRP7JFx02smE06Da3t8LXxxb8XIJtk8MBn_rzR5ZLT6bPE1mlj6hgRTFGULGjaX5LmAHsB4rvYJwWG-fr5LdFmn21_tivuaTXJS6PR-VvRD8K4VE8Y7jkVio1RiXlx7G-3XGBYexe4B9gzmuTQA9CF0gJHWOZiHiqnfYSQOqc1UU2fq01pdCZn3UhwoaiCz1Gl9d7EEATRl_4PBYyvKcBc8X9kiBhUqMWRwQQfabWXT6cKaE9thV-4bOdRiajkzHvBky4FyjBTHckkg5beX-h--TdpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا اصابت جنگنده اف-۳۵ خود با «آتش ایران» را تایید کرد
🔹
پنتاگون برای نخستین بار به‌طور رسمی تأیید کرد که یک جنگنده رادارگریز اف-۳۵ این کشور در جریان مأموریت بر فراز ایران، «هدف آتش دشمن» قرار گرفته و آسیب دیده است؛ موضوعی که پیش از این تنها به‌عنوان «فرود اضطراری» یک فروند اف-۳۵ اعلام شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/690113" target="_blank">📅 15:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNvaMx9g7JG5iTbDn6wL9XNYsVdA0ZlVpWVBegMbtGFkozcEBwbDLw_hVo9EQyiTOydJi3QAewGBRQGBXgMPivpcsPrfx4C5EscpJ1sBpNN6wgC9UZ4nVCu5boZh4By64ZExFuJk2kleH5ml-s1hbaHIafAsjxUv0_p2vmsAGpL4bGTFIWX9SKrgxq1Dc4rKXV6f3Nts4mpfFjKn-05ZpLKdF8QxyOJARJuByADfXofX_ay5sx840tmi0NJXMCTy1T6fUJoAjon6Ii2NOlgHGzvHn4kwYo0XxcZuz8rwZyq48MORobJqBah59tzgfaIJ3D69oX6sriNl0k_J-khplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BurpcgSZuMxxK21Q9FSO8ZNyePrd2h7yJTWMZI2VsU58jP5LXCW0jFXBtxeiqs-PqxTskIbpzRndZnLelgJ-xnIGM3DsiU22gelVyj62VlEfzV6N3eaS-s3WsSBHULpsSZK5KUHRx6CEsFk1pvH-iu4i3wFa2AcfwoOSEbh5KWB2QncnluLlJe9hbSEYu5gXwRBM3UCUdpWrOl-h1SRIPifNNUGHAuEk1tnhkvIlyictLRjCqxfD2ljcmqfAag3lxBytoWIJUNa-Fq5pIZFmvDzT9YHulF1r2rtCxgq1-BohaILZ2RRKGqedKyfOpYYt20JOGxJ0pHfqvvHUEekkww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افت تولید ایران‌خودرو و سایپا در ۵ماهه ۱۴۰۵
آمارها از کاهش قابل‌توجه تولید در هر دو خودروساز بزرگ کشور حکایت دارد. تولید ایران‌خودرو با کاهش ۱۸٫۴ درصدی و تولید سایپا با افت ۴۳٫۹ درصدی مواجه شد.
@titretejarat</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/690111" target="_blank">📅 15:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS6-DWJj_05Nd1BS-ExXbqhKnBRNAEqGxZEOSrYCpHI9H78PDQ_eOmBUJwOY8WZpmnX8W6x-dr_WZ9SdpXvsTGN2s6GbAI8B52rpYVJEC48eu4zUJc8K_Dvtk1RZMsiAtpcocKHhAj4ynfHuPqsq7l0Js1rU2ZgFkOKke-DPg5tLTaB7R_qpEiOPvb4tdp4yUnRIS1HVXUyx0lFwHDslkZGlQioULGHslmJefj0m-kxapM0C1sgKB3ZernyS935rztcSu3Gcl_Bki4ySRrIB9CVIDrKmtNdTzRv6wyNnUZ1ANqQ2LISyBicYRQsWVyiHI52NSYcxJ5icDNDcSYIxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار افت شدید درآمد قطر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/690110" target="_blank">📅 15:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vw5x07DsFdLZ35dn9Eaf7YdcfsRzt_8LCCfw7yY_BgbD0yrmkoO0jsigd788xZywWXVXdKOJj0zI0wmlJ492Ajx6tH-iHPyjpstF8fNIDspYkZ1YbrlEFQYuHYhnEBeH9z4Lcwiexqqk31RvojkKJH2Hq58TfWEbl7_p-pr7hZCO1eHH3b02fAxZS7z70IwDfqKqqAmpY1OBvzVv_xBYrUiCb0XRNKFGNQruOTXAPTbKzPHWETBDNub--DRoEbXuo4nJ3QWCv4mGIP38XIiCsHUpd8-yr8N1ITj3V9AGUc3YLyVrty4MqwxzIHQcBgrOBUnY9XInI3lHK--WImzEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqNd1l4OUSc-fOuJ-zipnPFwN9D03NikD0KP4xRHCSbbAc1Dc5xwAi_pv5QQMpQoz7fpVQYerjZxM9mJEoL6FO71SFD5wTNbSkGD1O66uRhNK0zASHp-6-KwN1LAHolaxPWRd6XiOYAng433F2t3GGK2SNQYnl2R44aZTAAdS60XV7AsXxQDU2g783I0uUdSAPRAU4F_t3_F02oUo-Os7vRAhKNdbjmHOMCnHRBBCMO3rBDO9CvUz86gpRZnMU9KfFSoDhsl_aXZGAl8VoDDiXeifoXEPlGtiWZCIZjacHWWUvtpPyMiSIHtYmH6MZpUYGXCA2LCjUHNoEInLs5OVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HErwarXiEUlqix-ZoNAaLzBfenhE_joq3NVyTnRywI3FGNL1ZJl51gYb4jcS-R-00x1_XRPaHbtUOU9VaxWItH3LgUpYlLIgZoAzEx2cMFJPCKTq4pk5NjfWje1RikTkJ6mvmJN4mFNiggoamfEf1NcmXeE5N829mLDhbb6UcInl4t2PpYUu2q8bKu0GqWyymTKJsNlg6lSAVqB1eEERGRks8m7tmpgFkKNgpmpFt7jiphi6ZnjedzsT4rB0tUlKXySjWnBKXs8VZ20LF8UHDRYBRealXjRynA0jPkeqhHz_rnHon7UobnYlH3I1z5utqtXi9iP6_UKbQRNUYXigJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هویت خلبان آمریکایی لو رفت
🔹
پنتاگون هویت خلبان اف‌-۱۵ سرنگون‌ شده بر فراز ایران را به دلایل امنیتی مخفی نگه داشت، اما نمایش چهره او در مصاحبه با شبکه سی‌بی‌اس، عملاً شناسایی این نظامی را ممکن کرد؛ اقدامی که کاربران و کارشناسان نظامی آن را یک تناقض و بی‌احتیاطی امنیتی دانسته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/690107" target="_blank">📅 15:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
مرکز امنیت دریایی عمان: نفتکش «الگایا» پس از اصابت پرتابه‌ای ناشناس، برای انتقال به یکی از بنادر عمان یدک‌کش شد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/690106" target="_blank">📅 15:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690105">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKICe744Z__mqe9giNTvUbdXuQwwgyZyhw5bGnOKtumyKr2jtjhAD93-DSaIi--o7GRjN8hTOFE99BP72kgjYdgI8gy9uG8oWvsFP2LXWVtZc3SznZ88LdsXRAXs9TsqBbfl_8AA81sj2htXvMAaqKtsCFDWGqQZ8ikARnzlaxt4LynEA75FHRhcsW5ZkUfCLjc--VN98eeTOrTSnhgkFc4ob_VBjUG45VuAiY8VawYt76kqWBNO9rnDTTjKcwjBKObvZdpEoAKHjvaNr-ufWDk4CUl27DPZTURgKWtKlLeBJRyMeJSS_mjaKxpJdDdQwlBHsBfSZueCb7J83ywiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد، اطلاعات کاربرانش را در دارک وب، به فروش گذاشته است
🔹
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع‌آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/690105" target="_blank">📅 15:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690104">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1715812e49.mp4?token=ZYusmByQVbqg3RfL6em1MQ8Fl-ZH-nYxfcwsWdnFZhUHAehSaId27fGqzqlofzMgqxa7inU0bd38DOh8N7XdPzpzzkgkMSXjUjqeCSaYlgyDeUyNG0Uy9c6eY_3bbCUEyPNd8BMIFb-cudJQXn-fjViQ6i9qZu_KqbyNEjOFrncQyN8OzH-MbjtxuJDYQaKePbeBfuBshR8GzG6ykUf-_vb7NTaCZRjFf5c3Bf_dleIxg7hkRoItbxsDBeq_JiSxAUnHBn2a8YfNMelo6X7MiEzxpBBUSHwIU2etsH3RJT7hjbDW5APFRdc8288mqCgMj7mp0sU30LnR9zBkvWZoRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1715812e49.mp4?token=ZYusmByQVbqg3RfL6em1MQ8Fl-ZH-nYxfcwsWdnFZhUHAehSaId27fGqzqlofzMgqxa7inU0bd38DOh8N7XdPzpzzkgkMSXjUjqeCSaYlgyDeUyNG0Uy9c6eY_3bbCUEyPNd8BMIFb-cudJQXn-fjViQ6i9qZu_KqbyNEjOFrncQyN8OzH-MbjtxuJDYQaKePbeBfuBshR8GzG6ykUf-_vb7NTaCZRjFf5c3Bf_dleIxg7hkRoItbxsDBeq_JiSxAUnHBn2a8YfNMelo6X7MiEzxpBBUSHwIU2etsH3RJT7hjbDW5APFRdc8288mqCgMj7mp0sU30LnR9zBkvWZoRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سکسکه فقط یک صدای بامزه نیست؛ یک رفلکس عصبی عجیب‌وغریب است!
😄
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/690104" target="_blank">📅 15:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690103">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpqNroOLsElhpHhqTLBI9JfRGs10yVddlizMP_8r41Zv3aLUlXDrrrPn18NaFPXsZkUt1ZP_67oEpy8APdCM_qyUcxXz2E-Sb8lusrR6dkiHpo3ckNRUHnfbxBhVFhNjy7q5lBevEQs6gg8pvqw9k4zNUS8MugBGHataB3vUTzlm3HSnL2a_zN-0s0ib7aofqO2TttdoamG2S52sn-1XNGmVMvdb8eiADClLIiXpi0LFfi_qPZeXKJ_p5I729Fz3-_WXYDllSDlvBP5x0oYK5C78SseVpi9yKY9x00_5IyA343jreL-QjrirZEcgznVb5IrDPoWYiGXTAX3xnIw0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان جذب نیرو در غرب تهران
🔹
فرصت همکاری برای حراست، انتظامات و مهماندار خانم در یکی از بزرگ‌ترین مجموعه‌های غرب تهران. اگر به رفتار حرفه‌ای، ارتباط مؤثر و محیط کاری معتبر علاقه‌مندید، رزومه‌تان را ارسال کنید.
واتساپ: 09309000316
#فرصت_شغلی
#مهماندار
#استخدام
https://jobvision.ir/jobs/1524386/استخدام-میهماندار---خانم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/690103" target="_blank">📅 14:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690102">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJp-3mJYTAxiI85MDOEWgMEQcrziZ-DEjBOvXb5x19ZOnLOBe946mLdBYeBmGbyXrCzkKFQ-cDpfepgZ0SZqr49eeKpmDelXX84gpwkNox219prbEXCmLSbG0D6-MH5gAPgL1PJ281n4MQRUHoz_SfXn-YRY97yC0SvUl6Pnfe0679Gsdo1CGSAIiHac3sW3PpJ1NlEjQHa-enXuxM99iHFF2FaX0p_S7TgHpEvqozIBpdEPX_KLec2EBcbP6wE83UI_CdnrCG6kqEKudA1KqzQlt311M6vTy9qu6PbpglAjepD3IobOf5-7HkrUPLZgdOQ0b_A4dmZA8tyIJRxPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خلبان آمریکایی: کل امیدم برای بقا این جمله بود: «هرگز اجازه ندهید کمبود انگیزه باعث شود که شما را در تلویزیون ایران ببینند»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/690102" target="_blank">📅 14:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690101">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
وال استریت ژورنال: بسته‌شدنِ خط لوله شرقی غربی در عربستان، یکی از خطرناک‌ترین موارد کمبود انرژی در تاریخ را رقم می‌زند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/690101" target="_blank">📅 14:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690100">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqUbhYVe3lFEWiDmSVV2Iubu3rkdq1olgOmzsMPzXe3fYzLCoGjmsRc8IuMeVMwq2zLxvJaQUj8EGLejbJxwNdFZlIxiFQ8U_9cF6FR_t5GOitSCfFQJCj9yGhjYGvvYv2L4HiY3UvZRmr0benCY3bXM3ngbGG1OKtSm0CKicBy4nlIMoW2Ueyu_zzH3BND2CLHXKxt5jCWr7ypzFrbkdjTQ9qmhvEyB7fzaj8f94q6F17Tc7f4uuUGGpt_0EGH_vZUW5ZhGEK0iX9HdqwO2ZPqFTZEjJ2oMVU1enBF-6Rf4OUfzecKF2S_Ah8M2tlxULP1VUxvpdNqcf33suXjf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب‌های طلایی سبزی‌ها با غذاها و ادویه‌ها؛ این راهنمای کامل رو ببینین
🌱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/690100" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690099">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GP39ctjccDi5vvYxe7YDBH6VUvypSux8YJTYiQlOxBGJOB4jifHyJwvud1bgNTWQsWGYy0BKNr-eovh0UN1yqvvRj8qfRqObl1SrpspVeaBxM5BAq2r0XEXRcTLq6UeKCxQRF9P9RJCPIqgnQA7Ge6OFZyJS3PQ7LUkErQbBdr8XLmn9HSoUd6XcTTA21bhrWYnzOlsIMXPer4al9z1tznrkMil1kSX6hQvjs5v4zkAoS56lMHQbU2O-p5R2kZQTkQDz_arCQbNUifJcB7zGK2ni2LdBkjC9AgV8jZ7ALIw3_icM8DxBHPJIDUJiBrONGe4o1cYFAY_g7vSQSX4cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت دفاع عربستان اعلام کرد در پی حملات هوایی اشتباه نیروهای ائتلاف یمنی(وابسته به عربستان) به مواضع ارتش این کشور چندین جنگجوی وابسته به ارتش سعودی کشته شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/690099" target="_blank">📅 14:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690098">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مرز تجاری چذابه همچنان بسته است
🔹
رئیس انجمن صنفی شرکت‌های حمل‌ونقل بین‌المللی از باز بودن مرزهای مهران، باشماق و خسروی و توقف کامیون‌ها در مرزهای میلک و دوغارون خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/690098" target="_blank">📅 14:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690097">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fd5f89d1.mp4?token=IxI9ScpifkzGPv8dt0SWcFbcW_ORcAwTqjRTQFwbMbSB77f9oI8GeP_C_0APaAtvPXbWnp9LswF_6MTkwnfiOJf7LgscYho31To1B6UfYkZ0Hf5PhoTan9DekBfb6Kda_VYmwhC9stEj-jDOYhZeTgAKbCZc8rHTdi0EJdsM58c1l0Wg_gZ1RIF8nXSj9-lLEJVaz0EranErT6i4s0ejeqGmcbKpXx9YbOk-sB_B1PR62bLxHSdp5Ynq0l8_v_vHPkM9CFzmdx8tONqXiT_CurRY7esnkVRVSjNBY2kOLBPd5il7DNg6fzeBsWdEExJ1pGlBYwSxeMjDbSTYiiL_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fd5f89d1.mp4?token=IxI9ScpifkzGPv8dt0SWcFbcW_ORcAwTqjRTQFwbMbSB77f9oI8GeP_C_0APaAtvPXbWnp9LswF_6MTkwnfiOJf7LgscYho31To1B6UfYkZ0Hf5PhoTan9DekBfb6Kda_VYmwhC9stEj-jDOYhZeTgAKbCZc8rHTdi0EJdsM58c1l0Wg_gZ1RIF8nXSj9-lLEJVaz0EranErT6i4s0ejeqGmcbKpXx9YbOk-sB_B1PR62bLxHSdp5Ynq0l8_v_vHPkM9CFzmdx8tONqXiT_CurRY7esnkVRVSjNBY2kOLBPd5il7DNg6fzeBsWdEExJ1pGlBYwSxeMjDbSTYiiL_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسی شگفت‌انگیز در دل یک کاسه باستانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/690097" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مشکل مدارس دولتی چیست؟</h4>
<ul>
<li>✓ کمبود امکانات و تجهیزات آموزشی</li>
<li>✓ تراکم بالای دانش‌آموزان</li>
<li>✓ کیفیت پایین آموزش و روش‌های تدریس</li>
<li>✓ فرسودگی فضای مدرسه</li>
<li>✓ بی‌توجهی به نیازهای روحی دانش‌آموزان</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/690094" target="_blank">📅 14:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690090">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6yaVqMuQ6IZ8_VkZkkCK8-u3PynbR_M3SALvVyzvI0MZ9-uHekb24ZJ3eGcZr3rmYAFUTJgK-nHkunwZcjZSISWvi8mg0sCssBJVXbu0upNJGd4OJ1iZY2sfhBSgCiv-egnIkhmUrc1Fl2VKi_Ri5FR9d9YZvtqR0zVykhg3cpMr6ixfJwqNXzikGEilH1t5L389VrUb_q6UMUzdNCGy1AD7oYUWR8gTjmTMiBt7qW8LxMTvfBYak1kMoGH-95shJSiT1eQG9bKnuoDYNFcMhHM1INrITj5YhCzRTUotDnQJkuVM61ZTcfltHBZCp5nVAtczZvFcM-2n6WxwIXleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzIkSyMtTgxBxKxS83H8LtxGIibP-o8WDkmkxaPwWJaIX35d7lnn_wZBbilsiZC-maxz8ESmpgLG8a20UKBP5pUi-G82C2cYY9YZ2b0ClGB2OHC6MVEscuqKGWCT5ryxxiJuG40gXsfAFZx1xZxjoozzholNsCJdlBUeRwivuvKwMLN5wFSpVhWDEpFL8azxNhRf4-fG75pMEBGS0vooRVlctujWqA9fl2quUmWGREZnx7qnPawdGT15wKkZxn8GOXprMulFPXuvI6fHOfxj8vaakIu81RK3z9wj6AqCVD1MoOd6LYH3Plk8ArQG7CVZvd_sGS618LD4nBu5KW6sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_AFfhCvZu-gzzzaO9jrd3eUSjlOd0LScl_RR2c1Nc4yMZDfspP6B6tUosuUnUNc4boOonqotww-fnqY1pI8jBSeWIuFLTpxMzo3-Ni69Q-z_Lm9a9hK6FSDH9qDMoPC-_3sZxDzoa7iblrPsurn8SUcZYfKAFkrnvcNL5FaqzVKapC39JnDfze3tAEBQFpC3vBUEBTlSZbHGTzgZJVIxf4UQYbX8JQ3DO26ZE_ofbcqIz0-tUsD7vBwJXmpCDVwtvCrNB9rVRXgjz2S5pQPyiCdjwjpyL3Fd8MPgNS6J3AHYn9kXYpL_17Zo0k_-ZEoDRw-Z69V5kSD2aombmLqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRDwknoY4Z3LsPpGAqRRT1TLkv0QIGjT2j2HCjyN6vPpzoRSMLWG2_XP7y3XcrRbOPFq43rDNSl221Ib2A63yTSEPCShHPZXwu74UXZjh0nS-ENqbanzHaQV_YyVwk7nnpohC4TztvBfxb0Oo7POaOojHpu_3rZIBSSjiVhtbfgb7Bf8BSXS4Z38hRDIrZ63KErELBxmm32MKE6wO_yGwaMLZ9pjiFUNdZQiJVK0wJ005J1knxUOSMRNaQcK6VfYHS7oLmeo9COXoHewg2S_bFXOLXAiPp6QwRefjQPVBcvvDhFbEEkMXRDFlCGNhkbnUxKew-SiwJTsaZ1vXp1oyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این ترفند ساده، دکمه‌های معمولی رو خاص کنین!
🍒
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/690090" target="_blank">📅 14:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690089">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بهادری جهرمی، کارشناس مسائل حقوق بین‌الملل: مطابق حقوق بین‌الملل وقتی راس یک کشور مورد هجمه قرار می‌گیرد ما نیز حق داریم اقدام متقابل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/690089" target="_blank">📅 14:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690088">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDrXvsIi304p1IgSxexN-9UXTaUP3ljC4ELVctBIbIzBKMNOV4_A9fSrL51XWeSAAXjyJXwQuDuSc4H8nvtoyvCthbsp5YALyaW6jHKqP760WHZXZP_Df5PwZiOutlh1qU5GksOHaoD_4JjVu-PqqQBozAt1SfRvqC0fmZoqdstbu-H2OlfqJOR2RhbJUCaskTx188-ImQ_KQGRC0b_j6GaXPw3CxnrfJjXi26oortlHOlYKHJefeMVVFrL8B861tiWl3CxJLab9HeW5abXIkM9hKlOTNy8IQyik0ThUbWzZrkkSWZ_N2Co_9sJ9oegctL3GMf2g6n5DkgtZUTkhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خلبان آمریکایی: کل امیدم برای بقا این جمله بود: «هرگز اجازه ندهید کمبود انگیزه باعث شود که شما را در تلویزیون ایران ببینند»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/690088" target="_blank">📅 13:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690086">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
عامل پرتاب کوکتل مولوتوف در میدان پونک دستگیر شد
مرکز اطلاع‌رسانی پلیس تهران:
🔹
فردی که سه کوکتل مولوتوف به سمت شهروندان پرتاب کرده بود، هنگام تلاش برای خروج غیرقانونی از کشور شناسایی و دستگیر شد.
🔹
این فرد در جریان دستگیری با مأموران مقاومت کرد و از ناحیه پا مورد اصابت گلوله قرار گرفت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/690086" target="_blank">📅 13:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
برخورد سوپر نفتکش «الگایا» با مین‌های دریایی  فرماندهی نیروی دریایی سپاه:
🔹
سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقهء ممنوعه در جنوب تنگه هرمز را داشت،بر اثر برخورد با مین های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/690084" target="_blank">📅 13:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690083">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhIQy5gkMDwqoxs87sj2IMexsvHhWDyzhi5LKEDRMnxqu9RTNKDapNv5BhLdeiUA4bFniMr5nAwYju88D3XOOiSYt1gcj3sljjBBUnf1TAVEmpb5_DuOx1ODgs1U33ucH44J7mmyY6c7RE_aWXbtEr9Ffk0ozTSIyxbDhbRC1k4v64BC3YZ5nJKxOwY12KQz6HpVZDsk9MILJojaV9ey8gVakF7mA3h3QwcAr1_md7E6hsQ0vowA3up85DHJ1Ht5uoiYmgoBpiQFCG0Mn5PYnoZGccP_GaNgAlPXb3HWBxEebkowbC9dXm3niIyTqKsbu_-jfA2oHQb4uunZpIso0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرایه روزانه یک ابرنفتکش در مسیر خلیج فارس به چین برای نخستین بار در تاریخ به یک میلیون دلار رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/690083" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690082">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
استاندار خوزستان: تردد مسافر در شلمچه و چذابه در حال انجام است/ تردد کامیونی از امروز صبح در شلمچه آغاز شده است
🔹
مساله حمل بار و تردد کامیونی از مرز چذابه در حال پیگیری است  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/690082" target="_blank">📅 13:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IO1m_k5Np6hwRFy6Y-SdBKUF_6ArDGDO8Kyiy6EMK7egXh63nZhwDyXZMd4v1tZq_K3tqjPfiBNp_trjnfDTnYXhgHo4tthVcSdQZJhpe6QX7MXTPP-3ADKd64oAYLk7tPphLJnvaZjyR6xJZXPJGKf69rzw13kaTlthvGvEKFjed-pZb6AvSnox2DfHB-F5F5Wultl128NPVUulRpQk3pOpUDpfFAzX5TdIoLUvvGQuvHu3vbWN8JNJaJPfhCSKyjonzwhapx_ntcwJlxjY9Yx0YSrDiWK4df3wc9Tr4QN-8YuJdEK-PrLMy8i4memVE0H_2SGeYHZKoaeMZQ_PkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSAA653kILdtc2sAozma2QCTtPzo9go1EeHbrVt8ZavFEasvTWdpl4jO2n56RIuTgacPSFG0x_H23sOda-QBnXx86z3ZzlBks1r0dP2Frcuy55SFcghRB6c0AGVSaovV9UJBbPdHP0Sj1hr91M-mb5lEZcu_Uw4s5MqogGI-dfnk4ZLbUbgrNxTAax2nQ4Q8tsASWuF4JXOrO-vUhNUwIcw564xkGozzVZiyfgs2kJBijwwek7IKGVJA8cqdkZg0Udx_Ihgyaj-D_R335vYZ9-5zY_djZvJm5FICba73sBcdYkpAyDaFlWxvaRrmkl2_PFRo1ecHOeUUe2B8SiHKew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بنز میباخ مجوز ورود به کشور گرفت!
🔹
فهرست جدید برندهای مجاز خودروهای سواری دارای خدمات پس از فروش برای واردات خودرو توسط ایرانیان خارج از کشور به گمرکات اجرایی کشور ابلاغ شد و نام یک برند لوکس دیگر (بنز میباخ )نیز به این فهرست اضافه شده است./ تسنیم
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/690079" target="_blank">📅 13:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS7IN2uheyMY53VexHFW12rqQvS7pZ-Z2o-u5-dciqgoH2EJOT6Hd1ZRdpO57VufiopsuECCuf_BFnOkbANH8gefg20HNQZMw3VaOhDkTmbgHQxeLdQSFAi1rR9hNB_-TFTjXQn94f7MQVwsBWO9VGIxob9nJmOMP2p3_HqCN4SRW-IrYm_OTc0UZnT-GnYnm5Ie3vne_B2HvTZ_hGWNhEPydbC8Ogv0Iv9ZUT7DXxWerkkq9SjlgD86-my_4K7_i1e9G1irOzuUgjBVYqdDO09QziF3nvsfa0JGuZ6RAAdLreNKPCEw1c-4pEQ2S4Fydm0ZoVsC60kt8tpFeKjiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای گروه تروریستی پژاک: ایران یکی از فرماندهان ارشد گروه پژاک را دستگیر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/690078" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690077">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
الجزیره: صدای آژیر خطر در شهر مکه فعال شد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/690077" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690076">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd45dc7b2.mp4?token=KXaccK2gCQ1eEIXxGwY6uTGYhxSXWWgmEPQ0FJMxF4O7DMQoBRMOk7O3Ct173dRDC4dX7ZbeFqhFN62XhriPd8GOho0kU9LVCyCog4YFrhOrSmLvuBlKOkNyOmurqb2fht-F3I86_D9mG1DQusU94otfpGUQyAL9qt6gJqKgG15mE5lOBWxcklnXsVxN1noWE4krzg8s5e9oRP3dKVZ7j2WiQvFKsrhUJRdr03avN-XfI827ybGS3PjFS2EZIRO9AUgaIutZR67z39XNsSqgfdHpCiRkpLaSO1t6rUI3NGG3_u4X0vkooLm_P0Qz-mKmPZV5LWk4Ey-irjoMKfog3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd45dc7b2.mp4?token=KXaccK2gCQ1eEIXxGwY6uTGYhxSXWWgmEPQ0FJMxF4O7DMQoBRMOk7O3Ct173dRDC4dX7ZbeFqhFN62XhriPd8GOho0kU9LVCyCog4YFrhOrSmLvuBlKOkNyOmurqb2fht-F3I86_D9mG1DQusU94otfpGUQyAL9qt6gJqKgG15mE5lOBWxcklnXsVxN1noWE4krzg8s5e9oRP3dKVZ7j2WiQvFKsrhUJRdr03avN-XfI827ybGS3PjFS2EZIRO9AUgaIutZR67z39XNsSqgfdHpCiRkpLaSO1t6rUI3NGG3_u4X0vkooLm_P0Qz-mKmPZV5LWk4Ey-irjoMKfog3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی افسانه‌ای Nokia N95 در زمان خود یکی از تکنولوژی‌های پیشرفته محسوب میشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/690076" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690075">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFQf6oFRn7ZfUzKoqMpLzdXlLwRj_IIOVzCgTimcAi51GFdjEmKz5WEWs_U0moQ0VIhI1KmM_a_RAwj3xz2wsKPxwsgnNFH8zkNFsHfx6Id6lPaJzJ1CjbbjHQRpgQVgt4lPk4SIIQ-CyeRTz6CmHUexrJt8sIi3CdLH6_w5nd6O_JqU3NlLHhi3RT1f3NUVRAGThn0KQyufcbjfE91F9buKAndjg-4qYK7VK0ZS0LkvbK_ny2yrInBpyn-uZIeFJB55q7txfDzA7HL8s3EcdbzPT0LJ76X2iLga6BBcePeT1ZMevKJ07hvqgH0Qw9PxpMNNeGO83RbV6hzdw-go6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
*۹۰ میلیون* نفر جمعیت و فقط *۱۰ میلیون* خط ۹۱۲
💎
📉
بخاطر *محدودیت* عرضه سیمکارت ۹۱۲ و اینکه دیگه قرار نیست هیچوقت تولید بشه و روزانه تقاضای خرید ۹۱۲ رو به *افزایشه*، در نتیجه قیمت اون *همیشه رو به بالاس*
از *پارسال* تا همین *الان* تمامی خطوط ۹۱۲ *حداقل
4️⃣
برابر رشد قیمتی* داشتند و انتظار میره همین اتفاق طی یکسال آینده *تکرار بشه*...
با خرید *قسطی* سیمکارت *۹۱۲* :
✅
سرمایه گذاری *مطمئن* کن
✅
*اعتبارتو* ببر بالا
✅
برای همیشه توی ذهن ها *موندگار* شو
مجموعه رندینو با *شرایط ویژه اقساط* درخدمت شماست
❤️
از بازار ۹۱۲ جا *نمونی* ...
😉
https://t.me/rondino0912</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/690075" target="_blank">📅 13:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690074">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
هواپیمای دولتی ایران وارد حریم هوایی عربستان سعودی شد
🔹
گزارش‌ها حاکی از آن است که یک هواپیمای دولتی ایران با شماره EP-IGF وارد حریم هوایی عربستان و وارد ریاض شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/690074" target="_blank">📅 13:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690073">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwSDGbNpHDyP7YNGG7TSp8ifqxvFy0e9cBdGfn71KJTAFn2GrvoMVPcm56j0307hX5ZheNW_SMs8dCWE9C561C2TJVIJQJOOG4ULxyuodzy1sP3ff5pehi17fVwzGWp6N7yZbFedErBrR1vTX5FOA890I0_tLw4ho5-g7zjLoJMK8mhvr5UCcHCrh4_rlkUA41NPw4gxEbHAEK-Bx3-OkMLKLuqQPz00APFGakDWN2qo_UZeNtjaeLb3hK8qMqNuHHUUQCFIZEz68KvR5JDZ3L135FzlQePTCi1Qu2maGAdZA36m8kHbf26LpzcUoH6yuIzs9lMv00Kh90RRsu3n5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بالاتر از مدال | بازیکن استقلال چه کرد که رسول خادم برای او پیام داد؟ | ماجرا چیست؟
🔹
اقدام خیرخواهانه سعید سحرخیزان، بازیکن جوان استقلال، بازتابی فراتر از فضای فوتبال پیدا کرد و این بار رسول خادم، قهرمان سابق کشتی جهان و المپیک، از این حرکت تقدیر کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245364</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/690073" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690072">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXEIFPgbDCP9vb-jJ7X_WMWoosK_0sXkWE0EKZCophiej1A7Cq8wBfzltAnI7h5gv0OAv2SCsEsLVem7EsUxPkvphXfqdI0FUkX96gr0YmsIIgcy-fzHVkHTtAdwkG43JL5LnXovWwsqTupo8qj5l5MkQKUf0NHi6CtFiC7r4ppXv3rPJ_0_zTLHBIAgFHJd2Z6ppz00nBlGJgjamklweUbDurdYGsChitKeIRQF6FY3LckH8V7XKXedX0Or_fsJ0JfF6bbOAsLfheRGEYdvLa4jiqdM3-xZo_Pi5zJwvt2_CGNXoJFcjL1xNbxj2snglkv5J3jgiNf7pUeynvv7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان عملیات تجارت دریایی بریتانیا از دریافت گزارشی درباره اصابت یک پرتابه ناشناس به یک کشتی در تنگه هرمز خبر داد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/690072" target="_blank">📅 13:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690071">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTExEjz0ANwnuP7wnWT1Mx-BTewK81YvMoqgwYDXxxNHeYn-XtVqqGx1qCXWBiSCoyfc4X5NCAvEXvYVwUCajTUwiJVeb5hH7zzN6s80yg2ykQYfAwyOUOPIiA6BYsElVimfBK-RxnEkmWEqS6TcU7xtMjn0gpr-G59SKHEDQKUBtObPk0k1GsjfUd6uFEJPDul1-0pzaycTelCCjqeQqqZyWgb3vb4wXzetx_81NmYTQ_yd50Tv4jIU2dQUvnX_IyK8ZmRD-NhdSmjMde5QSK0xkbLa5esSav7q9IQwIuSxMqxjeNuBgsnSbbEO6IxExDd2che227DfsGXm20s-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و ارز امروز ۲۴ شهریور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/690071" target="_blank">📅 12:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690070">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
جنایت جدید عربستان در یمن
🔹
منابع عربی گزارش دادند ساعتی پیش جنگنده های سعودی یک مدرسه در استان تعز یمن را هدف حمله قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/690070" target="_blank">📅 12:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690069">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiwb72Tw04GBG9nK1AtVfhp2JVwgvtjR_PgKdBrtBGP3Rp203F68d0DAzH2BHd0FtLh9Gng7lpedqF2SDIeqT3EFp_Fsu4TkdmZKoFvS0X4sQ9vfMuQDI7XJTrUQ-STW_y5CSJEBa6Etv2MHrVsKJWgAN9__nq6Vdo-EPXrdG-v5kZx5fddFaEC6vXSNT5sGLkMo1L4J2NTPpeetg7FI-Q2orZLfINtTqw19y28UQyG865DBy7odcvLbE0wXGdD8PVBDC8-J8rSLPGMfavthm3K4DqQJ3ZYtv1bM-D_ePqOITk0OwxneZNESMomCrJxP1QpsG78i3lNWv3Y6AThH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های عربی: ستون‌های دود در استان زرقای اردن دیده می‌شود
🔹
هنوز منشأ این آتش سوزی مشخص نیست./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/690069" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690068">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‼️
منابع عربی خبر از صدای انفجار در شهر طائف عربستان می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/690068" target="_blank">📅 12:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690067">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
منابع عربی خبر از صدای انفجار در شهر طائف عربستان می‌دهند
/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/690067" target="_blank">📅 12:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690066">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‼️
سازمان عملیات تجارت دریایی بریتانیا از دریافت گزارشی درباره اصابت یک پرتابه ناشناس به یک کشتی در تنگه هرمز خبر داد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/690066" target="_blank">📅 12:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690065">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGlKpaLjYV1-7j8ZpAOXycunw24rFCid6Hr-uZgOcBk9mHb2ulOb-lXsCxDZDUnJxZ6ae2YhAzdqhBw1zoZMQgSw8xuUOisgzGXtIjCJiAoocIqZNzDHAeX86TQmqt5yKyTzCsEEdUM30a4mqkBnuogZs3_CcL3EMtFA65NRMIaaaF2uB9Ly47cuQ1mUSZupVphE8N8oK4ffdZvClzobvjGNDghxt-nlwPbr3jU2TbO2bB_vLWy-sR7DgxPJJ1VmIwJYQIQLASt0bGHaU9ZBsqtCpTCSqiv3HwjDgaIy0whiZt-J1Nln0T61fKqJREGWuxzV-L7YtuuLm5fjKetH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از شوگر ددی تا موساد؛ حرف‌های جنجالی امیر نوری | پولدارم، می‌خورم و می‌خوابم!
🔹
امیر نوری در گفت‌وگویی تازه با مجید واشقانی، از وضعیت مالی و دلیل ازدواج نکردنش گفت و درباره روابط عاطفی، حواشی «موساد» و فیلترینگ و حضور احتمالی‌اش در جنگ زمینی اظهاراتی خبرساز داشت.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245356</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/690065" target="_blank">📅 12:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690064">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24e444f512.mp4?token=b6qT9cAEnYw9bCZlGNmtTT3OiGfJXNkImVup995pBWjjtqrd5TrYgdkH1dkJChDBv1i5r2qASZRJDHchzRuEAMX0fX9lp2M10X_DMFAjkcpqCsMKe1eZROTT82UFdXzqVkCZiDcyBwSTrkHxlQOn6BA62WXh0Lqko6zrtX3QqzY-FADk1EqUHcLxiEDoLWOgUQ3TZ4vN_w_G145ANKbNNfJtIOYldFGLipDtk47GMjkZXRdP1CdnhobCs3Cf6raRKhz62meFtaJvP7xjQ_ZLBPvLg2Zm4KkuHb9GnaRlzS3VCZPCSQh-7S9totTCSPUrSSKMfS9rM_s3U4fVxnXnZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24e444f512.mp4?token=b6qT9cAEnYw9bCZlGNmtTT3OiGfJXNkImVup995pBWjjtqrd5TrYgdkH1dkJChDBv1i5r2qASZRJDHchzRuEAMX0fX9lp2M10X_DMFAjkcpqCsMKe1eZROTT82UFdXzqVkCZiDcyBwSTrkHxlQOn6BA62WXh0Lqko6zrtX3QqzY-FADk1EqUHcLxiEDoLWOgUQ3TZ4vN_w_G145ANKbNNfJtIOYldFGLipDtk47GMjkZXRdP1CdnhobCs3Cf6raRKhz62meFtaJvP7xjQ_ZLBPvLg2Zm4KkuHb9GnaRlzS3VCZPCSQh-7S9totTCSPUrSSKMfS9rM_s3U4fVxnXnZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سقوط جرثقیل غول‌پیکر در شیلی
🔹
وزش شدید باد و بارش سنگین در شیلی، یک جرثقیل ساختمانی را واژگون کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/690064" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690063">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
گزارش خبرفوری از مراسم بدرقه تیم ملی مهارت ایران / کاروان ایران عازم مسابقه جهانی مهارت در شانگهای شد
🔹
چهل و هشتمین دوره مسابقات جهانی مهارت (WorldSkills) از ۳۱ شهریور به میزبانی شانگهای چین کلید می‌خورد؛ آوردگاهی بین‌المللی که حکم المپیک تکنولوژی، تخصص و مهارت‌های فنی را در دنیا دارد.
🔹
امروز ملی‌پوشان تیم مهارت ایران، با انگیزه صید مدال طلا و اثبات شایستگی‌های فنی کشور، بدرقه شدند.
🔹
فاطمه منصوری، سرپرست سازمان آموزش فنی‌وحرفه‌ای کشور، در حاشیه این مراسم در گفتگو با خبرفوری گفت: عدم حضور در تمامی ۶۴ رشته، ریشه در متغیرهای مالی، محدودیت‌های لجستیکی، زیرساخت تجهیزاتی و همچنین چالش‌های تحریمی در برخی حوزه‌های فنی دارد؛ با این وجود، ترکیب اعزامی امسال نسبت به ادوار پیشین به‌مراتب حضور گسترده‌تری محسوب می‌شود.
🔹
بر اساس آزمون‌های سنجش مهارت، میانگین امتیازات ۲۲ ملی‌پوش اعزامی نسبت به دوره قبل جهش معناداری داشته و پیش‌بینی قطعی ما، ارتقای رتبه و رنکینگ جهانی ایران در این تورنمنت معتبر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/690063" target="_blank">📅 12:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690062">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
هواپیمای دولتی ایران وارد حریم هوایی عربستان سعودی شد
🔹
گزارش‌ها حاکی از آن است که یک هواپیمای دولتی ایران با شماره EP-IGF وارد حریم هوایی عربستان و وارد ریاض شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690062" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690061">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJY43X5VtL1UEL7gfN7-oA8CTCXxByLKmYFDssRlAFDo3673_YCTd7kk-hplIc9RYHjssHFJul-3b92WHm4mnfBYeSvHtphKXOyk5FkvD4ojrGD6GXJBmAiLo6bebsQX7boXWHRkxf9F6whhdZWeE-DoZs8ZXTu_0A6iZZt0cURkJQqEGnzdm5E9lE_X0gtsYiS6f6TYfUibBYlOCRHp0xlmKmiS4PwSPI5LmlwdTfzrbcJV5iHr9BKo0841Z7YajdaWhX-IVMX8hSQCz7KK8p-FwixGA1V8w27pnz3d7Z_ameJSqTpxj_7MYtrFJvLeTAPAjLwahAwumb3ZXE7B5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسری بودجه آمریکا در ۱۱ ماه نخست سال مالی ۲۰۲۶ به ۱.۹۷ تریلیون دلار رسیده است؛ چهارمین کسری بزرگ تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/690061" target="_blank">📅 12:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690060">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c85078f1b.mp4?token=W1mySjHNVlbruEmXW6I7K6ardjQ3TkjUvXERkGyp3nmDnZlOhlPDhUTN7nH7kmfVfY4SmE-PlSpgYzhV17o2CKIa5fS_P5umViVYaXMiT9add5WcuiDeyjo10wC_PgJnXFWKo_NgaT0w3KzxkkFXRSz7ER5aiQYy67nv_KpV3PKhGe0cdjgmyauPbBcF_ljOF6QSYDKf1VbQ8PQEClF84xLa9EJ9-7RL3GQ2GtOmf5NdNgUDZ0xaq2-9oZ_M4VlsvlY46oBLcZBp8o_526dQNRJyIC4oqhq1r7WdniGszey3GecLaO-2fIfXYp1x_Rh9fK-7F4mAQgb8OeuUL0qHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c85078f1b.mp4?token=W1mySjHNVlbruEmXW6I7K6ardjQ3TkjUvXERkGyp3nmDnZlOhlPDhUTN7nH7kmfVfY4SmE-PlSpgYzhV17o2CKIa5fS_P5umViVYaXMiT9add5WcuiDeyjo10wC_PgJnXFWKo_NgaT0w3KzxkkFXRSz7ER5aiQYy67nv_KpV3PKhGe0cdjgmyauPbBcF_ljOF6QSYDKf1VbQ8PQEClF84xLa9EJ9-7RL3GQ2GtOmf5NdNgUDZ0xaq2-9oZ_M4VlsvlY46oBLcZBp8o_526dQNRJyIC4oqhq1r7WdniGszey3GecLaO-2fIfXYp1x_Rh9fK-7F4mAQgb8OeuUL0qHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خنثی سازی مین با دست خالی و بدون تجهیزات و دمپاییِ همیشگی، توسط یمنی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/690060" target="_blank">📅 11:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690059">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
رویترز: شورای امنیت سازمان ملل امروز سه‌شنبه نشستی درباره وضعیت تنگه باب‌المندب در دریای سرخ برگزار خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/690059" target="_blank">📅 11:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690058">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
پکن: عراقچی فردا به چین سفر می‌کند
🔹
سخنگوی وزارت امور خارجه چین امروز اعلام کرد که سید عباس عراقچی، وزیر امور خارجه ایران، ۱۶ سپتامبر (فردا ۲۵ شهریور) به چین سفر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/690058" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690057">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6aeoAbmcBQQRukuhdFtXslkd0GxDMskvkAGyXbzLV3--WzGAt6fqgHrvXPhkTvLqCnonBjHGJT4QzUftCNNbs-GSjuF57tL2KE7cu3KEQhYQaLq1Wda3YJwh9g-MhdzJLtHaA77dpuwtpvAxidskEvRCvfCIRA3UGiUPQaiYgdCAtk51wfG4aV0lBFcH6gjbJN8DX3sIIjdcvipVUfDA1F0O1EsEU75y6dgkqdGzxTYQUg2vzCfMKgzi9MYZbobUkCqaEjuTpkath4ynPuEMfDqiO2fM-snLJNJdsrOXpMtx9YCZSAVuDifv6ek1bI6QpG07cXE86Ay6VMEO6vOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحرک هواپیماهای سوخت‌رسان آمریکا بر فراز کشورهای خلیج فارس
🔹
حدود ۵ فروند هواپیمای سوخت‌رسان آمریکایی بر فراز کشورهای حاشیه خلیج فارس در حال فعالیت هستند./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/690057" target="_blank">📅 11:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690056">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49481d0554.mp4?token=ia9YhkkzLzV9LyxRXXcNY69T7J4A-ExC_twfWWYdl9upmkSSycMpRD68ARlUUcJtvMTvxEzCdzUA-Zz3s_8CqhPG_jZbBenuLlGPkbON4y0ZsvtC0FyaqZz2LtDPHo5HSQBYLWjw01g-nvQGP9lOXR8otYVJvUquqRXBMgnJa8ud4BGMAM0qtpnqtijQgkaauYfjuslU-FUG4J3KmFdsAMIfFt7TCLUu2-rWpFaag4f0VdDQ1fmEa2P4HP5b8kHd4gOj2qqyfgJJlsCAZaDRWSk-t_o1dqPGkTWOg3FOaVzQZbEbQrJfxYehM9kx2eoTSiMCAvjvp9hRgjDHUPvuqYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49481d0554.mp4?token=ia9YhkkzLzV9LyxRXXcNY69T7J4A-ExC_twfWWYdl9upmkSSycMpRD68ARlUUcJtvMTvxEzCdzUA-Zz3s_8CqhPG_jZbBenuLlGPkbON4y0ZsvtC0FyaqZz2LtDPHo5HSQBYLWjw01g-nvQGP9lOXR8otYVJvUquqRXBMgnJa8ud4BGMAM0qtpnqtijQgkaauYfjuslU-FUG4J3KmFdsAMIfFt7TCLUu2-rWpFaag4f0VdDQ1fmEa2P4HP5b8kHd4gOj2qqyfgJJlsCAZaDRWSk-t_o1dqPGkTWOg3FOaVzQZbEbQrJfxYehM9kx2eoTSiMCAvjvp9hRgjDHUPvuqYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک درباره هوش مصنوعی: اگر هوش مصنوعی بتواند کنترل سیستم‌های نظامی را به دست بگیرد و، مثلاً، یک سلاح هسته‌ای را پرتاب کند؛ این اتفاق، بد خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/690056" target="_blank">📅 11:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690055">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdiweEec5jvXrWEOC_AjIc-fanHBtVXafOh2xCPklipLoGn5tRLi1wyKWKUd-pH7Zy4kuL4BPsIKdgVH-fHIlQS6pzGSN7wGVvR9VZPBVBzPi7-J1Xn672I9Bl0tXHVRIgjagqP5jDcJrJC57mNZ78kc8Q-mAOiLuUu0grU_oo_z1bPLM473FfduuwW9KvPMd6HyVeVYfQ_rxSebIyXA4hOLra7H58E__dbFiKUjXOqLFs0s8Bgk92xWoWoqlxmuLZfKCb0wI5qG3UqnmVDocMXUkyccPdcwYKcVP1RIHtlgW2dFlxVYP2Jv8U4fan70d4pAA1tTYRTRzXCrJVbslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید هیراد پس از سال‌ها مبارزه با بیماری، صبح امروز درگذشت
🔹
مراسم بدرقه او، جمعه ساعت ۱۱ در قطعه هنرمندان برگزار می‌شود. @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/690055" target="_blank">📅 11:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690054">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxCo25KUdwNIaNENK80qpwoEcvw5dGNFvhxwQJlJ8-BdUNj-bPyOjUvRk192d6VHC0ub-bS4rBPjF90hssj9g_JCGjTpTaXEGDoRkDoBAACmZYKWl5p44qFdmSZMaRKxDoNI2opSo-20Mpuo5PmSWbUJDWkyY-MtpPfmgT6BxxrZEqfwB3ULpTvjb141ocC4A8b1riYZDzgE2lcLAN5TmbLPcdlS2YpbyoqbqjTOy_7c3Jy6tGp4CZ3cqzwY3odLL9RZO0SuITsxk5oQBekCosqmmeaOE1dgfDtr2Ps-agAHG8UVi4SuXjRVV0ReECtoJxtdjSBcfnX94Tl-YAvKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/690054" target="_blank">📅 11:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690053">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e877e5cddc.mp4?token=pntuhnhbE0HBhfmxkBwJHui220TDrjslOTS8Fu90vD4VQgPiXZS-t42DixUfFr_c857YhcZAa-pUlmdXFBWy1CmEqRxe1L8OzF5LHc7t4G0RzQdcUVUQRbWpmyiTA9umm7jje5gXXVT4O_h9cYvpO4SDoPM4IUoPFMNETIrqZZfAs1bJcvC5yIR1qHzpIgT8WQUGDNAvKLF5TxJsj2tIhxYJcdWgUhHisqEKk-iIaC5_I8c8HrfMxSBWFDkmP5R2dVhFLQZtCqIfYWYqIccykDJvSbg12OntPv_GTZmKvs5dBaA0zGYrp-1gIJ8Q5Umo6ZjgwYCDUE5sLBwnRchTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e877e5cddc.mp4?token=pntuhnhbE0HBhfmxkBwJHui220TDrjslOTS8Fu90vD4VQgPiXZS-t42DixUfFr_c857YhcZAa-pUlmdXFBWy1CmEqRxe1L8OzF5LHc7t4G0RzQdcUVUQRbWpmyiTA9umm7jje5gXXVT4O_h9cYvpO4SDoPM4IUoPFMNETIrqZZfAs1bJcvC5yIR1qHzpIgT8WQUGDNAvKLF5TxJsj2tIhxYJcdWgUhHisqEKk-iIaC5_I8c8HrfMxSBWFDkmP5R2dVhFLQZtCqIfYWYqIccykDJvSbg12OntPv_GTZmKvs5dBaA0zGYrp-1gIJ8Q5Umo6ZjgwYCDUE5sLBwnRchTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوری‌ها خواستار سرنگونی حکومت جولانی هستند
پیرمرد سوری:
🔹
لعنت بر جولانی و نیروهای او؛سرنگون باد جولانی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/690053" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690052">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
افشاگری وزیر نیروی هوایی آمریکا در خصوص نظامی کردن فضا
🔹
«تروی ماینک» وزیر نیروی هوایی آمریکا فاش کرد که ایالات متحده سلاح‌های کنترل فضایی را در مدار مستقر کرده است .
🔹
ماینک از برنامه‌های ماهواره‌ای نظامی مرتبط با دفاع موشکی و هدف‌گیری دوربرد نیز پرده…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/690052" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690051">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تصاویر هوایی از محل حمله آمریکا به مراسم عروسی کوهستک استان هرمزگان که برای اولین بار انتشار داده می شود/ مکانی کاملا غیرنظامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/690051" target="_blank">📅 11:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690049">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c192c460b.mp4?token=k5OVas2uN4JNPvzx_9LCjgAzE045Pm9t-KfZrnP-2BKEmKc9rbvvy8ktvoPpWiGAzlgSqxS1X0u8Biz06aCGpCSGImOwQafMyqhxX0CqnrLA82izhEJq2J5pMqKarFRxIGz7h41Ax3Ry1KuHu5PsYoh_pdhFP0-ldwSK0F7Ux0vIJC15CzjSsc7iXUsl_HAZhDZYreJtjpTQa2ae2xdP0HjI2-vmaGFQPbYMX1aYzWb8wEQeqbhqb1ZWl2xM8Ljrbp6IlNClI3MsRXTmmDgphEfYkvt1ENd2tBrvkqiPmxD5D7TnRPhfU2xFnsWRGSqwophUWItl-jA7Hf-02XkNYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c192c460b.mp4?token=k5OVas2uN4JNPvzx_9LCjgAzE045Pm9t-KfZrnP-2BKEmKc9rbvvy8ktvoPpWiGAzlgSqxS1X0u8Biz06aCGpCSGImOwQafMyqhxX0CqnrLA82izhEJq2J5pMqKarFRxIGz7h41Ax3Ry1KuHu5PsYoh_pdhFP0-ldwSK0F7Ux0vIJC15CzjSsc7iXUsl_HAZhDZYreJtjpTQa2ae2xdP0HjI2-vmaGFQPbYMX1aYzWb8wEQeqbhqb1ZWl2xM8Ljrbp6IlNClI3MsRXTmmDgphEfYkvt1ENd2tBrvkqiPmxD5D7TnRPhfU2xFnsWRGSqwophUWItl-jA7Hf-02XkNYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیگورات چغازنبیل؛ نیایشگاهی که حدود ۳۲۰۰ سال پیش به دستور اونتاش‌گال، پادشاه ایلام باستان، برای ستایش ایزد اینشوشیناک، نگهبان شوش، ساخته شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/690049" target="_blank">📅 11:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690048">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سرپرست سازمان تامین اجتماعی: معوقات اردیبهشت بازنشستگان تا آبان ماه واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/690048" target="_blank">📅 11:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbfd6eecf.mp4?token=Cw0bqaMAGkNdQemPJ6uYGpkQs-sZmBzptdoy7Ysc9-_OcavU6QcOinBAxhV8J6-s1Ljnyac_h-e7F0OqnJLQNn8GvQaEmrfIuGt5j_rx2tIn4_I9ad0SgTluIZUzmwyUWSIMvQU2c5hMIu9UrFPNVhLOPX0odpyVbHTzG3q-WOgL_8OtJvMiwtu9mLiLAfITN0gsmZa_MUfjqSAfXDLH0rhIYvBjGGSQyn4ZIckuvbVwDWmZf8SEQdEEuW0b35orhh5JicvA1DsfOf7TiIITZwNkP4OWZ-ZT5sNODOCzsEsdE4D4LJcYE4Jf5NW2Uef5e6BsZU6abE0ZlkWihG8DOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbfd6eecf.mp4?token=Cw0bqaMAGkNdQemPJ6uYGpkQs-sZmBzptdoy7Ysc9-_OcavU6QcOinBAxhV8J6-s1Ljnyac_h-e7F0OqnJLQNn8GvQaEmrfIuGt5j_rx2tIn4_I9ad0SgTluIZUzmwyUWSIMvQU2c5hMIu9UrFPNVhLOPX0odpyVbHTzG3q-WOgL_8OtJvMiwtu9mLiLAfITN0gsmZa_MUfjqSAfXDLH0rhIYvBjGGSQyn4ZIckuvbVwDWmZf8SEQdEEuW0b35orhh5JicvA1DsfOf7TiIITZwNkP4OWZ-ZT5sNODOCzsEsdE4D4LJcYE4Jf5NW2Uef5e6BsZU6abE0ZlkWihG8DOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وال استریت ژورنال: بسته‌شدنِ خط لوله شرقی غربی در عربستان، یکی از خطرناک‌ترین موارد کمبود انرژی در تاریخ را رقم می‌زند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/690047" target="_blank">📅 11:09 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
