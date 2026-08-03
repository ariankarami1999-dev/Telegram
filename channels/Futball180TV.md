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
<img src="https://cdn5.telesco.pe/file/brtrORJalMfrrebJiXj9ESFbviE5gYZKclHTVBpmy43AiV9Jmr7f1TTryIeA8SacmQH9mowl3zJgWnC3E2tcWWRPjcqfUrJGijb2KBJ7eclEbviVvwY__SonjrrPX7Zvdea-z3asA6ki4wqF7txg_X2W2YWD91JZjozBRlRsqlGZ_Ytb_RmTLS0WcHMid36Puyh7G6Nirv1UWeyeLuUEgN5-d9GaQKgkv1qxDbmJupJGzxHJ3qkmuOpffG0hUnhXQ2ImcPgITbZFacSMxwFs5XrLHI_2ITbmMEwL7HGRBCg70NI1FsWKf1fIKStz28qOKYIVUUsDutT_Esr43fsWiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 500K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 11:56:10</div>
<hr>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjul3lpHp3q7ENDfyKmZ9RrIwFbbTur56-t1N3olLUO9EhaNJCcoehTtJbjBr8czMXgj1qVa9Yvt0jAwHYlfF_OPlLaIE2N3viOWLbQHBf_i8ftdcPTSHLGqjFcKx1r32qLc7Gl3hwGDf060fUFe9T7iWzvJ1EKNSDwvjDrtKiWkvZrB-27MJCbuRtJXpLa6_s-TBLXlMGYylrJfUX8apAZgcvOKzXxHXHiL0C3h8Qu0Vm6obG9StaS4hLAElthIYyHu-6GL3aISzomcgSOTZ3KDJ0UFPLSfoA-Y00P62Vx6qDFYrrbjmRmopjD5ZSXCUWl5duo12scqQuFTm-M3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUFBCnDvcbB91E7_KyoHpUsZQrVfXsMiIv8ucHrts4Cv_yb8V3Ll5LjdhVj6t1bhbrTuvRUfyCJdhyRJrt48JEKhwLMG9JYAEmR9vkXfkkxjeU1C_2Lp6zWlptbY6tPeg87VSKCPVAajfCfQquoDUsXIU9hyBiuH9KAYYDekf3ohB9FZihlBR0opuIUHJYvLtnzT1vhgjANj9C9LpqNTD43juxzLh72t1yb7rR8obVtGixUshS1Lzfe3cTruUD_dPlR7aDC4ySkBowv2l9_H7hvpX5uI3I_hSmeb4mHfghFzomzVUswjDsLrdEfAQCimYucABbXZXoopBs8FipoPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBZqillcVD2_apzjoS3sxrYxxM5Ol0rGWdn-oS25qFsEM6tHTXXGbmcfa49jwYBe9fk8_m5RooMXkNAj-DDXivLu9NUvTDmX4D4TezlHgSDmnKLL_xRPJSHMYCGl37tjpBRx8ZpRDtKsKLal_XdWDni0VFBKvPVtPaxWJVQUO6tzoL2qf7nlmngLqqx9BLxFwamrw9YK89u-fsHrlRqMQzqxBKV_CrDyEg051_YDQdDAtDYpV_5gMmyi5thBBUSmu2x9oGAhLIRIzTm3rp8iPPUvAL3Jws5vPnk7k_X7v963k1CxVelRb_9nJD0IR0hA49OalXZumDkyPDH31j4LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5GPY5T7G4CTRsrUQlWEvL11gURgwoyhZ0qFAHDt0299BJ3tcipUz2_GrRe0m7fa6ZUDwE5wdqT-hlT7YQf3P1ks4DGW49MPvWsD8rfJGEVJJbhGcqMjOU89HQWWj_9IYnDDiYR3fAfwZwh1ymR98RBrx2T1rhg1qIYy23IDKajGzS4507KjBwVJz8OTnI243eb1FAr98xc8oqCPDQa6ycfTXezjEBY1WobHNYmiOwCYbDBNPf4NV0RWCmAY3FjgnZdp_gJ8j9MlKCK0JCuwAmW1iKwiImDdXOKTAi224-dWDjXV__IYp01FL08UMcIOqr0xo3ZFbL4MQftoQzagXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-OzwQ05mh0nQ-PjOfV-RUyKwLPgsUzFzl6AjF8bZXhgcNfEC-e_gv6A-peld5WUgbmT59QzIErut_NK5YAQIGDjWklwi0oeLciFug3JRRbZ7w4bsTcHw0biW3KwtoqWoSaY---Lz3wa2VMAqzsB1jxf_9KAsFY3qT1qsHN_oQXhLXmnlt9drvYlYRJvqeBuYkyE65bfsLFe6OQEhiZHfR_i2pZ4bC2b5JJZRMoidI3FXUcNXc_OIfN0hngIOgGaMLO7USFfRPptVgSRrOJMCOQdvsW4f_Hhubf0L58gNBMMdTcvOV2nrtjvLDpFp033l9eI2yvnP27we3p7vCzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvoWGrKpkTncmSmE4W5sgwMFwKGWiTvZR74HxxgMJdeUFSwSt5KdsJjoZ-vybcB0gX7pnaF7_JsP4TsCYaJcevCJ5AvqPR5x547u8EtWLXTgnoDra9uc68ILi5zBSKkJNbM3NEkZRZK9YaKyfa4RyWMmKQZCBYGUKf2rsl9wUWRjNYF5IcmbmWUe4zPzBjdFYd9H4Om87QpSbwduqPLM35rkJf-gWre2btEfmdy3CXkGhQ321qB35sfOtQ4Fj1JNwqn0FsVjhLgg86mXfVeLqDl2wotSqbInAbgMd2fWtQlXihAw4qXtWXeMML5gw8Ca8A3pUGZ_qzvdnZBmhGzjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aciY3P9YX3YhtWuL15LXx4HG_txeo3NEBb5fH9fPd8X85RMPOAhVwl9iNFk80kDbQbWQgANE7LXeDzpGokZfr2PKAcsS8IVilN2jdc8tj4KPrRPg9NuCm99LtLCvS6tYZf-BE5cevsmu9eUCDfeyFZxbrkIfSmGt4_EbuEFwAJcapVoR68rd1FmhwdQfdKVWb9TbBIAvYg4HL8PKZGuxFtUqaoN99CaN3xyNxZXvF9kIe8YFDzM5m4gJG00fjMECVL2-Undtgr1sFVOHJt3r1_pV8gnR0qyNuOrbgryp1vbRlgLUG_XAYuB53yqDTibO5WMJirW1N_HeChSDqrJ7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE3ou-csGdduQBcPL3w1dVjemzPn2as8NdND-0mJfm0k0zyEkgOuJeYqLowVZjjYk6pQsdZNeU6JJytnmym0urI6c7_FjAqLxzW4OV_98nIXR3Jb5x6XQZ9MSMmy7VKFRzCccmYoKghLCTULxePCJtMy7jgzgVLEcYnmtT6qk7xa7kWjR85ZX3JdF_0-TDDnVs48HOQ0ockObe6S_CYL9jRtzAJsHBfhz28wVFMoZXdqQy3hdq9qKLScwI_PRgslAVtuuMkRUxGYQQSKrwokmewQjbAqzG9y0wsHfgPIjqLKijeeJbq_AtlxNfJAbcYvdoRtdq50_pK2QjQX0oG5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwrjqzJZLvYeQPrWUrGgVxTc0Q2d8OepgLor2EB05Co-f_AOG9uunLGwD_EKqUXuLIhfDRhFx7HsmHVJ5JivS9qdJ0lQBbVMoOhCvQLCJF17n9AFCpOZJwUoQDAnMnfApfn1OsnwLLbFB0xpsydGEK-HM0GGSotcTxHoXNyLPa0WcLnymWb4ZhemZIcyW_d3LyrJym4uQdms4Oy5gqraQ3eQUCGc-8RtKUfqvfHu8BYV2M_kOLR7NeJs3cIYvY_Qz-FqpL9MQi6Qi0lSfjG7pN5DbbC-yUBSlDioexWekoR30clhH1Aju2S0D31Bp96ih4lK6BpUUzeF1SCObHNGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=onijM0EG4GeRw-AQ86EiSqZE2-GKrgm0vOxKeiA1fgVJSioV7Vti0sU1C1V9yx5Ji3Ey9I4VLHTFUqrrck4dmc9jhKoy1SXdDD3_asKjrkQNbPfiCaa4rQioD3-ExuflpojBP2JuUy6vBEezH6tAlr6OqyiiX6aMYmKT8prte1RYnZdnvw2ZsdrddEwEITSz4b368Erm_W2B_6BQCaBuk26sd0fKn3jeNS3suDBolitY3cm__eb56WBF-FjUovnFbLFS31UnAQBErGZsg9B6XTA-os9b_tigcvQtGOJJ03ABY-QjuLNTNUmAmg81R--HeuvhkvL1FlU2fRH0QIM4ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/glryTqvJKAIoCivGtk5cF192CB0_AwtUdhGhBH0Tu3EousB5BpVUSM6aG5eL_UQmjD_dy1kOjKBuLr3WQ1IRoRd0lxeg5KHfJQd2HqDSuMw-l8srTJVdEOPaHjJBYZBOzYy0gQWMr0Llb4AJ3l1naP5UNqZcnB4WGHcoqXLUm1rRNPD_f3AYWKEqJqgnzbaEnO0SfYKAawXe0Uk9brS6keGm8TnJTjQq6rBA6KQUWuJ44mP3S-jQCTEN4NnkmPL41zJ98Fc5Y1bo14qoiMlWgRn6DV6vFoZBXz30Q0yXVoMXszBB3I2thvnU4oM7-6Gd9EsLvdh_zc4k9-lp6yCYkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCgWKCFaaaua0yMM7WwZVZT_LoFmW3gk69Y-KuW0Yq-t2T4YA0P-EN0zaeY79fiHVPjfgxUsj1bH0jUYZ3TYfSlEzw5XRNH-VsLlxbWrimI8YNspLi4BO5M5lPdB0_dJ55c9OuGmf9hrH6O-TWfQbEkAW4gLuneKR_Dpz7fZ8wyhKbuSvJlEf4Gl_ohRa2J1arJ6z3dZaNa3zVFryE9YOALZf7WXiF-k67oVfc0anzPpo2fnjA9D0lXg0_JdoNWeY01nbHmU0oZk3jgBJTT0pvp4vTHlH1RyouGkd84z7jjG3DzVPGNEDpRU60VYAi00y1EcjCaV91aWUZEFN8itYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=tx_Ypwpw8_cAtOLB7qo-CW_Tuuxyk4IgCrxUx_-vIqKH0vBdhx8sfsuWPn9MFTjOfG0uD0Im_vjRgmz1ey23yfGshGHtMjSQ_50tjw4QvOiML2wmZcdfTWeU5M185kU1WC_pZLjGXbr2FV1J9AO3YtHgSQyi7WVn_sqTpneFkDWt_ftyE-vcm12ZidcEioNraETY-tp_4iVa74oSCm4R8lApPaCUarWpe067EV4KXT0qbJ5iSFwxZFv7EzznAHn-BCJ7C2bM77JSi_wyzJWW5q3AxU2GWwzGU-_5H0zcrtAK2Q4q3KFybFXS1mJM4kdBH8GY_UQFmr2Ar-9F7o6LlYnqrkXUOOPF0IqclhQejfT8zlPidxTYyrLg9Bno-bl9_KcuRf1XigJpC9J7QMvHtCJfjUpQ0KHQAlwUbs4OZcfaGHKR9zKfVut8JG58sXq04z-lfVqJ4lNxFzVIh84poicvV7rxfuJVTzzcVR-7Sczz55CoeHRBt1P181HZC_VfUZV3YGwTEIllOtDjSHqWDWP7L9HhrMiy5X6dMZ35CCvA5O8qWWJGfeHU3orpOTq1C1R-C0LaIIbdWnNI9Y6LAYT_JrEEYHzeXv8123FwvQNynywsQoAT-fv0GhIMiWz-4K62p1b9z3fhTfXaSy4kNZo2mmb9mO3nUTTQPF5_jd8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtBuGxMX4z8Q4-7mtkGA1HK0mvta3V4T2H1bEOhj7v3uQvJ7uGSfSQVMunsTzwxce2-2FsGpNsKRZPp8Z8ts4Mn2ubC5ve6-vh4sf46lCnxoc2v-k59SK4rJ3vB2RZVrZccNsAyWH03Op1SFREfHM4xmUO83-ZUGuLZ-8glWLAAz94xK6DW9iA_Zq9iBdhlRzlUPTj9o9_HC8rKa4Z5Gsh1AGy_G6Gr08y2cIOl1Te9O8znxnpJitgtNVsFB1kCP-QPBOqKuv1PHj_T8iidHqaNIwZvjnDOnyVI4IOzi_pIPa_twOaLG1wdsj0WRfHvc-5v_yvYINnxKVmzs6m6YxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuwkUouDRqDTUE1FImiwbLac18WgGcd6Pfywfy49u7T7xbIJ-GqQU0LwuEQofxIGbYR7NdQHd68Xi7Ajc6q5ekwOhjxcTm3wLKKe-aUDLBbf2nqAJCW6vy-1hHVXiXwLSQhftZ5SIeMbk27VzYFVrjfdqP5aIBUpeg43336szcfi7ggSfZ85q1YUSVkjrscMtue9a6fYdQN6TlWP1wsPh1Ja0zPi0CsQh2_F0yy9l5Guehi0SPEnf5Czn45LcXjuzEsIaIJN2cYESh09liW4xvsptHoEclAzP1srLFJa7K2Snqipoxj9Xme54B8o3wwcPqV-p6IcQcOFF4k5TsmFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsJY7DmlZrVWgcCc36Wr1700qIQDod6evO_YlADCr3ubBe0ggikUEJp628MjeprEE7kKMi1pDmpA44fwGf1vETjUt0uwaj3QQYE-7AwfiiOU46Ckv5r3KHlSWDZsWPIvox3j5qRunj4Un9gFt9YDO82GFtwhBWK-ftlezefBag_nZO2BJm3G724Tmjsrw-VGzbIdrcsWzHogVtYlc0arZGtuOMJF_TZhLeQt-sz_LZMvuGQ_Q7efunUJdScf6NoCpQ1Y6z30JPMwjrl13CirTJIL50SidqToCBs72XlhBQA63X3QDcJ3qH_HwIf_s-sr5qXI-6vL6Y1-9WGc-bgg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ofCNhZ1eXlL7KTd0qoSpbRP16wSf9NTFvZa3r1yaLxObgyMuG1DyAPqzV4cVrdkT3pshFu13rlScWl7IsakMSeEZhLOnCYRs1ucpAaabNPYuG7P7cQbV3N7XataSg64968U4W8CSIpqfT-VBIxDHaLu4pxWVrxTUWYjvG-JxLHJ-UiWYyUUQ7M4i1oRV_fcrKXzHolJ0666WGa1Y6gXLAdl8Tg73S9_jp40jxO_wffbm4EATV_YiX6mLEfWn5ejynv9YvdLydl6QHRfHRTsXW8EEze_d-PKlSlEF9j9E7fAy9I0k4tm9a82b9_g7tjwhbysa8fr2pKxYfnSb57rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxmJjOyBZ0BmweILxNdcjJGf-C7iBaQqno2sGN-ynGvbJMWxLJeSbqyVgcG3QbPDqP8ZsUCIrOS619BbMJTKFNbVjVEuHOgRmgesIK3e2UWT_M3p7kLPzjXYvG7uAalJm6qbVBJuq9kt4VGCZ0WXGs99WGzPMT-f4g8PUU6Zsx9rWhSkcKvObUAyrr97ejf8l7YiMrK-KohPlNlKddRZtZNYbW_MBBYGICTRITwgFaVndHQz0A-bUCNilOJ3iKl6lTCzDzQWqbx7-lvFLG0OaQHDBuZTPoLDOTyLJErArSq8C0YuEfskUddrXDD9c1jr1-5Sf8BDs47wVbloI4NazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNd2CdItzmWQo6TQnbKw9Brd0z29wFc-gAxOfjlDA_wsojPV0bd3tKTi5q3XreUmdeUIGMoenMYyFskj1wihTGD0hgPMlfA9PXv3eDhWHvjpRDn1Rw5S3MND4iaD9Fq5ddGWWtVQ1fF5KZyTbx62VvUmzOUkUTOceTyB3ADP_z5CP-kooq3Lz57mVK90XCluycu4P8XEnQxjbDPITS1m_Xxa92glNOvnUENhg_OzpTnF8qyFHs1XgrGnXQGVsb6vBVePUtKWBZ4h-jb5N0GL8eWfXwM9ljakaoAhmb6WG1-NiLOoYuHm8tqWEl3_g1pIlOkBhrrEgtQ2fCJ-HzXn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DH_M--OTSpuK6xijkzCgM7EGKq80OhtwgVWGCmearlmC7aC1W7FFknIEq6nL_XcD2-1PRMa7TN_AvioWZgb1Y9Sw1E8lowh6vieTh8Pj8np6ZMteYWfrLAWVOR-hf2cydqxNpt5RoKdl-pDwSGaoaty0l91sblEiaxt8Z0O8zKVwaroAlkMGvzbWxUaclyhTnY7LJBWhYh5b0T3H0A_NzaUxzvLrudZfGUn9iRNmdHVbqT-qhABGowBUMuFm8THUJ9SKGkAKhzapsUIyry2AHAesAlXmkNKOcnvhwtHny1gbkn0Sqjo5bgwrHnjBoFTfKHH3SvosALF03ayGG7uAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=ds24SRlHXKSh60LAFLSmOYtUC-cW5OhsMcNFH4NITzlKn4wAgKtE-qyo-cMzCf0NiN6suVggFej3GgplHP9AbxOvD489-q1fXecr_ALUUY78_CacmbEK5ODyXOaEoKJ45Pd4yuLePKoMf80OzoTFiJuoA9RcJO_-fDMPBJ_81jQwHhItS9cFlwKHC-SOnhVVJHJkyXXxVflJS4q6vHk4bozdRBoY2crbVA1XBJ0Nu-zXHUsKEVBiVQ7hKiD3WI7W-A9ZMXnur1s60eNLGWs7qCxFA83pSGT7Xqyu77WDKgt6HkozH2AxALsLmPXtKrAzR844TzqlbXG3ohVpzY4ZrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=ArlM55ICu1J1ogYHP-6vgven7CN2MhfZa70IWLHc2q8MZmT4IfA223cVik5e4DG428qHDH16KxyXs3AnL9IOdPqaCOKvDBiAW7S9tspmjeov6E35QJMgKAEqNuEzEzTap6U1ZGfPM-BPdRM87LhJcv5eANOFwL1eRzU9yulNECDt7eIQt8y9c-mFD8ENlHRHDMxHT9P3cuX6XItwYTvlKm05qSUhDQBMW64L75GAmgC12StlkC7G0RGNEJG4nBx-c3TbdnOA2ndnFFtKhMoI6XXOK0Sv5mtYXaqq40rRrA1KSxzfz-GCLjqs0O1P27t0P1Z1fiiFTwWgDMOE1AAnrUAuDAml0vllLTFHnkfOon68FMhdCpwTP639nZ_Yz4oZwEDxWhIHiFnE2nRS6hXqP31rl5aFCG4YSrRDpBjN42-MNKX7aOdv4nCGI5a5qT2mEvWxODNF48VRUgVeOjDYT05UO-QljUf7IE0z5yEJ8PfzDeoaYYWP0nPoiiTkxkdxpXDnhhb6SNVsly_dIqxBQTdwlKRNuxi5y5JrSivwTN1aYAQrvHAAloRVIGAmtCeylylirmEMsGQbCj8mgf2V7TOXeuej9INjyHKcWP3Kl40Yd50jFc1xwOY5UuhiqDuKUSbW6D9MkVSLg4iYh-2RtdWvIp3WZDVcg9NXTY29Jf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C19gnHYhEj1VTaqLa_JsCTh_xcby803d97Nh6n4DhsNQgcavXnqfbwkMDEI42paHkYqeqZPoQ6SucfnB_FZJex5zIXOfPquHvm2Wz38IUdOeGzUGTOHxDktiv3VL-kI3MouDZ8WP1Lv8ZTJedzODGEoCXwCcmVohKL1InJw3qx_Y1_7gyL11FRNSZzdJBEXjEll2zt37BRgi3ceSpSC3-h3LOZmmwR_6wW84BBj8DuHTOh4QG3xUEuQ45FRJhnsbp9JZyfI5EVSVk_zBEiP_V4-4Dq7hNViPYIMu09llUbk-EH5TCczvdC6QRFq5KdRctf5Jbs_Iz6tXaurEgKkPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuH7kZqIo1KPVOKHCVJPbJrNzCiYbxfita9GVSnduXxjTzfi3AKR7QVqD2nd-eWJoNt7Kj_9PkQGXGn8UWeBozdYrnWboh3KRhAYx0KeZEtwFxuqq5M4jdgdPw2qB_T6l7o0U62X0tB8Jgw2fvxLiTlnGlrBI6tIUutdS2_iTbtp6rXArN_o3g-VJdo8kd6NFGJtBPwvzFJNFiou2cFRZ2_md5Uv7DzxLn74LMM7neTNxC9K9pAzd-TYLne0ZX0EjrkVdnU3VhR6E-E9IDaDHVv_A96DjcXfrIwlg3Kik3F141o20II0OP4z49ogoj43VGhubaaRIrXgQM0cjUA70A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cx67Yuy0o0FTpB4N8sJK3oDGHy_j7THIM9i-YoN5yu_GjjKxTYfYbSEsz4jE-d3MGf9ANyE2U7g02H78X_ldCmpmmYOLIoA4dOqHs8HQQrMO7I4_GQHECzPawzkkhg34kDnARRD4woG5CstP6V1hkm60EMOXUkkIFpqrwpMxsR4qhAiB8vw6Agkru-xxoAc62Pvty0qRFcvNB-rTr_il0TLB2N6Fgw0mmeX9YezTAqJuZQ_-BB1wDvt4xqAsCk3xJO6zWt_xd8cimQ-HPCASFS6ls6xoogG-VEBQcedBACp85U-qpNJ1gmjuqdGhrABlv9QFfa4qGOCKoT5lxuJTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpIfQ_GT7qrU7EH7jDyci5ZkzH0ZluY8vIFWDzsuErCDf_ePXKwpNjhpQl9fv1E3eO6mhKzNe2Op6fbLgWgzAjYSI08JT0hiFkiczU0tHW6QEVs3ba0dtWkQ8xV8BR194hsE-6XagNoLDBIEqhhTolLN4hJvDd3fVRo7FgamjxCRa7fuu_bpbfWFt0-oblVoMc8anPPnKPQxvjAsd4gXgwRdZZy_fYwaE2NM9UuBttZYv80W-Oc_BSU4DEGZpg8qCV8p_qfVu21B9-GcLCXPf5jMQACbQiWW_l7A0AaKAb7AS-OtfL5IaKxjNUSk9x0iH7ohFEKTBcHIul_g0GAV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Kjk8AzWIMD3PBgoxOLrO9voUfcxL3lDmgfXVbPAvfD55KHhxW-ymbvmBPjg65WHVwvAp7apMHePop_NJf9oNSHfy1eA2N5Sydo1qJrmli68QwhMVmntN_bvdqiBaaH_w-57z8XVhF-_D2xcpPDINxAicwhduzq-4pNgZhTVJXrDDvi58mykPKchZbvJXfcmd5TRCuhyau0jAufqTATHYVGFdaitsrzuYKIkTteezJllWsCj9c1vb0rFwUdB-zQiToCTHH_S96xXyE8wqWQKGj7t5I2c2oSyCiu1ZeXw5iFAwIdkHvquXtYQaa_Q92fwDXHkyT2uia3NVAMX9P-Ca-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=aYHycwckabuTxfu_Ck-00HOOrTkKF5UrCj-tci4oIiLnAclQ_Cl2kF7rikRps5_36HbmDcZtgPmtC1jNUNsuSy9iXprNnPcyNvkyZDBINYLun_gEZiCX0eY-Le_M-u4QbbmQ_lJfW0LGQmtvaA_z3maqQMzcIsIBO_LaNQfChTgZP8tvVOeUSH0XBHodQjM0KmjIpK9Tvg_wU44su3BWHrribkwVsJ3Fg8AOkwxAxMj7P4Mq3je4R5pE__BJyaquD69xXkVIiC29kwtaPPMKVSPMeHe_EdTrrS4tiW-jFiogXvqjDq3OgQieXhOAe7cdokxWmZyXandg1vBfUWlvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1git3DNZi4UbfRWiWLlD1mmu0NapExuNFU4qGBTdm-_vodScDPaAwNxC4nliw-K0Z8iJ4s4r5DWarkKZ6pDGbOd1FXw-jqVJYHgKotSo0cm-GfqEhQ3pQvpHatdzAIB-erj4llSZ62UtBUAZyXaLfNi2yf2mZLZk8y3sI_uHB_g6FEk4JRlcW79YR1TxjU_1UfcuZqGA5nEAJvI0g7l1-THdSkwEeVuehBoKquvSBklv699qzDuaZ8vINGtHK9-9FQzUgzcAy_RY6TpbAUsLcFKROFRoJeoL0FlTVV118_me78zNU7Re38yaFQSRnf_xCSkRFdzBCZhQ3UpJaRSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYdJqaiYXZyYi__F1XAM22YO67kdAKSV0F4hU1wqssDH9Vk7cwuQtWU69sDsUO99X4mp1aBkMjbJ0TmfrLcjVQ_3nCg3b3B5ZX-F9loeZl414NEvwOvVoEgrVOHJXZHtZXuDRrnkCUdkQJw5ToO-54vRfcZ2E1-DzaXQxkofDCjD3ZHTLHihzAr0JR4aKCjox3HAa0-tsXKieWvxWvDTLxoBr3UgU517HxgEARNp71_7cBEyQhEP53rBWZLemQliLNqaKorG3IGvyb7hy0TI-imKL1u_MBE3OWtENz2HpCDlnIjnBWVw7ARVjv9OGyAY3QyOIV9GgSD4XL1W98u-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWyRHGdSdije0HpZGADMkjPvQBjUAqjCQTuhjrTvgFA5h9wsQdvRzOupAYblL4RoSYFRUZBM_goRY31Z84Oq6fYpmzCChxLd8SZydJWdoM5xZUJbcYKi2MqrzRSgGDOYbsWL_76wWEtBaDoF_ckUF0hGU1JXexYFagQxZPWRGhVYQza3vfkEC8sgfz-nBOz4HdPWK5EPPN1_LKF6QokNu0MyGvwR14IHBdMNc7G1DNZj4_fu19NojruX7h_IUv5xq2a7AFgYY-GGAO4ChbhIRarEnc0uMeONnSHjyKPy3MvrTsM8krDFsFPIrjwzNjmlggiN7B9xoUjdmtt2Q4rgtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0HCDRgZIIq2HuulZtVyzYvfMi5IeDp_yshZ3Hq5trumVl9DKS2-yiKlleQpPuVcEvcjvhooiEBtifLvo18H1OUNfgkxTfvuLaDB790ZjOsF19TBniimJexe3vrIyknaoFMRsqPpTWceZkWwMeFA9LrNsKiRBO_Sx06-su-YHH4fcVQsX1j2X8ydqWYF9VLVYzrJve4N3ma1G7rBMnl_wyXdhK7rHR38ADbQIZVuB6GqEcJbZnwN3hvT4ILRRSfXpFkB3ruOYlyrXvWXkp27xqsmLLHOAggQqnka4ba3M4x0ZFDqHm1GoEhZ5N4-DLyJk0LYfOBNzdKgLhQI6dpNpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=I6STF2C0am2q7Ly7moa4UFc0TJMuEV3_uQeYH0QwLx5oFI2Rfhcp3ZG0fM6NDSM4fhB0GOknps13rNYKe4EL1ZpJzUvGtaYB3ofsZz_uZn87IKBWhXub9l_RmhtPY5nzfmHZBScrj00JwrRI9sGkPyr-gT7eDxEAZEZcHnF73kjnoTcFswuVfGD9nltsVzIbtUaGYwxM3fs6IKiVGOj-aUw66ANj4vPJzJPGoL7RunswDpjnm7YV1TH2JKijBBXP_MBwgEz4URFVJi-nnotc9FIBDZ0uTBi8PmU0YYRLKOCqQZMM0o5g_MlqygVKUkxg8Jcuj97iMgPi1tDRRNbMLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBjxBAM1LmO6x9esji0nAoK41Y-y7bqr8CqniZJlzNJQ1NH2wZQ2ynJpVOWfjjhjUEIxp-DVi5Q4_fjeMaPyGuzeIvinf2JDWSadi4dVoc8tTA5NEd1Rg6twC-z4uD1bY0RbqQywaZANpi5PwQAqfhPjxdPW_CHa-Jtf6Q_kPeDTqhKctCYkNOSHJugrkmvkXtt7Z_9P_zzyu5r9GMQERNHV7lkgEXqPSv14H_ROYu_kvV1Kr7mwRCnkgQUgEf1NBBThbTbuKn3vIuCZbm-mnp3yUhlloZ-6kvKA4Ns6hTwH_5PylIu3tYoOpDhepyF11_zg4rESUHMicZlcuUTGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=Fy8IvDgwd1AHtad6wEGmJW0vWWcMWVfJ8jMyHUUt5hs5k_kSRUmLsz1ANQXKQ5tQz1V4vXm4o0YpayYYnXSYU0NKna09KP2Lep_ce5TJj6pdt2qB6E9dpRjNtgU1MEXrzBWpQ1fJaPEosCZ4QmwKUZPHMPdhrZFsvGmMiWvC4zyq22o85l7RmKY_wfacWaNVgYPUrNylhG0WgtQ3akQrIExqvtW7hXMiEu1nvl1oTXSI_LsUnyd-BYneIA06duOYAMomsclSIpCVdV3qMCvGdNZ9YmXP9tgpmbp5boDTL87mUiNJNIeInhU0ObSUgVA7faQv2u_ByXZNL7KrGpreVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkJu-pC1D2nZ4xCt2__rRswUnVJq8M5dBBFvAPxB45yo4_My4a5lVBWXIDukVmonuiSyGDGBSfRvQddZBGg_apb8QljgMWT_SDGCmi7UdFHD0jmV2fNnX1n9FOQr2ou7oEqruNUF7fJyGoS5W9GuwVqT7c9h3xErR5ORVM8MbotSWbN78UySrfhIBIHnbzDWMoa6DQPNJ56QbMRDUJj3RXVCIkqtKNe4RwphIYOyJkVXCeg1az9ke7Mf1_-k0iHmZpGNJ5k3Y0zkO-jKqiwPs2mzKy1NOzsF-W5KDQOksuh6EwRe3pWfel1kSSJF_LNSueT2nuNC1vwQgCG6c2Pg9AmU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMjJ_qNfR6zo-B4GdnkAhHIIqK3JiGKAmQJH0AtVdW0y-ezq7K_o3o9rdbmafAJFiYp2m2Vu1oX6sKu5xlicb_5lTFuzoNTr9TaL3OxutBt_MfCzq0xOphfkFSYsN_5KXsbjTgqF5gk1dsSc39NB9OfjcIV-DmlO9F3jn52uMYTrOj_GfvzXiCLp7VhZQHdgCfOAZSyRyyPq5KHdTvPnBdD_QprZDyC6k0P4Co864YdMtFybtuu9ISRTJZJm9jZJd4qpcIU2eQH1QvdkJpi5YRwlEm0HUw1I5GqVs2Mr1LX7bkYp32Tq_ac_t2l7YUMJOS85a50B-H2S7JJYNUECWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn6Od9pp-UP1ZWfMdYNRmiEo2G87UABrsayd59oNFuSiX3xHOKJMpUy0FbHEha7ZGI3I42mZIX32KRXZQs7ohDUkiJuWEm_-53bBfIjnDo4KdCNbsFHNiUW8eIORpTiE2Ak23hKor-OGVwP3yQeOrBJnURiqBup0_4mTlclaE0Ij02v9DC7VOpypK0Mj9qfGRiMVo32MWL86FD2_wZoB9-2kV7TLmk8LRa3_30j9Hs6oVT19aC3BLDka7rcc7kIc_DfYfAb7jktbOfaqWk0pcRiG7ujEy5x45rn6j4e9k6Zig0KF1WYI4jS2jiWLXjfXcWTvV7u7JBtd-SlISOMKfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAbkOKEeVzbJs-rSYYFtOjGp1A88eyJrnipNsriCzb4bJau4ETL4oQNkcim9BjL_amaZBLGj8_a1TMVzJt9TIOoiDNmShR24-j8X5nqz-OhxNPrC4Jj8nSZY5-niIYQFimw2BLwVAah6Ftzkr_p9Z3tRDFqWco3FbTaX3iHBquIJupV0E0GIhT_UzEiiaVlqIwbUfKJpiTQvpqdAKorwvoNaxSQD3rOR4KDSCv0xl4rMCz1xGtD-sOPZUtyNeDPMzEy-A7PEvCq2--MvpnHRTRVYKLk5DHMyPzaOqcEBlHAM02zp3KJV85PilXh8OCMnq2NTS_2YHb7qvv6EJJQlXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La4aw83BIdKzZkY9mNQoyB0hwUESnbNXh7l6frFkio01kKL8LYd4M0RCgOGhU1uLHgysJ060d2CGchQjM_f5_VMbhUu7gm6_o4ISetVrQ8lVf6ivoZ1AsRzCClEzCpKezBdMtNzlhR8ZUqk7VJGa9OJid9pxNaIScsHAGOJOKh4cgLnysEVhDnn_4Qt9P0P_i5CvfALpE-F8ewnllO5GggLwmVqak68kspVvT-mpeldzRppPjm7_pgKGrdXedEJbkam_efXc4hQo42-bEQrojdKzWwYUkHq6RKKnTPUlXL_py4wts2g7EWkyG3TJqxg7z8ZdNgPTS2LSUgMqCyEY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbWpYUj6mrKFYAaIskFT2Bmr0zTJfJoyxk1QMRn0bRYspK79gEyC4Ui8Cg351pDGVRjKYTzClNOLzjNERUte11TgdMqYd_Q0uYFucdHjH-_DbLifbRYE2ePvIL6xnzAgpotLEgMGOw3eunQlFxJ2uvKovdTmUzf0JO_coqPROYc0ssS9QouZAQVEzhf9sjBd-8gN2d3D-xFHEPIKczIc6P921UFhwlT6TPnPuGpXwOvk_yD-0sa9ujO74puX7mnyAcVBf2vj0THcsgLS7lMv0ozFd20iZZuFk-dzpdgfhrmdPDxn_3zTdQJwbClCAsQulgxx3M7qlL7W8BPRWgpL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpMD_1FG6n3vd4aatAz4wQbDPL61KikOWUNgLMz6OcqbIcouug5_F_8InnD8NRM2mNRiRQasEm45dJkAVBb5q_occWGpw9aj0mg27J0Mw1L4Tcj201mKBn3psSMElUx97Z9EHyNHH1EtHzzlVU8NuGDF7XgLPXGcul3X6VuEyb9X6-ho8kI5E5sSVGgpadFTzJeQcHJBBLIsOxyh-ZGV3UwjAD1Az_qJr-x37Gfyh461L5O3t5d4KiuKN2AYRsJ8QPt0kS0ze7jvacwD8XXNuqKji1PRIIYdXTro13kG96hxLgt1P3AiZtAEdWu6saQaOEwzXaPERnqAp7zi5ylLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=fmM8ErJMyZU7WMiWpZ9GuXHNwWRKM3UuE1EIwt6CfA4ESrMEMBGtowdWramKjb-4gXfcTg9ydnzETn5TPmas9Qy8DqZenV4wGO8Q9x10qh25CZH9qWnM2R4gL9mYrALIB-6DBmO7ZBJBpJkVilYnf2Iu58sYmiRF9WrdfTdW2BvDO1KHoivP8vwSqi2lhqDp_XzJL-4qpU4iYjLbOM19tC6XX9Yw6QWu_cwhfVxJfMAMSYDAV5k6yhdo7AqisrKOreuaKJF87n5tZSde1fUJnTB1WDljyZv1I5vSYX2nGTgvgU85onfFMlMUnasvnoLklRUA781w2gjAKvoOTJba1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=fB2sbkcbEhfkONTgbL_4oWDzctYmqcdhpX_mscO51PV0527nROwxMo6MX1RF5sPA-ovAjy2B6HWjEe9zlKwYWb6DXQKUKBG3IpUjZ6c3guBpiS20oM5cl8bjwoGj6yGuLVfUmOC3SFAcgGFH-dKe1TfaOkBQnlHnsy4SlZ5DVXrZtwf8p7r1mqPGwcbOoKbBPSWXFeM3beT0ubHdaJXXEgKriYK4wqrR3IXUxL--i_qFfGqqpeOUHqBC8acpDKpKhQta5j-PJ9gkY4EdsywedcHO705iksr1Za4i_2eBQB1I2zLgpqLi4UlWda1Csmvp4xpM7c2YTzx4UBbJiJwijA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=fB2sbkcbEhfkONTgbL_4oWDzctYmqcdhpX_mscO51PV0527nROwxMo6MX1RF5sPA-ovAjy2B6HWjEe9zlKwYWb6DXQKUKBG3IpUjZ6c3guBpiS20oM5cl8bjwoGj6yGuLVfUmOC3SFAcgGFH-dKe1TfaOkBQnlHnsy4SlZ5DVXrZtwf8p7r1mqPGwcbOoKbBPSWXFeM3beT0ubHdaJXXEgKriYK4wqrR3IXUxL--i_qFfGqqpeOUHqBC8acpDKpKhQta5j-PJ9gkY4EdsywedcHO705iksr1Za4i_2eBQB1I2zLgpqLi4UlWda1Csmvp4xpM7c2YTzx4UBbJiJwijA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=PExtoJ63Il2QgM-3NmBVLhZFB0EVZrbrBhJCbXd42vxm9aBonB0X1CGFtR-7bwExhdT2jVhJXENiYSU5xMUOhkYCHmg0t2iPgx2LDiosFQtXlzD9T-CQnEcPmMc46jBVjGxIEf5gTCXOIygxGwG_Cl-kKhhqC1KwCOOcfCj0D-Xlps-BaP-wMaFdIXsOsagktSQQUtsbYU9hlvyMljc9jTDTq_k7JF8Vna-x9pLILeSyPoo7nl1WzOw7XmG6NrnwClT38VrsySUP88h_Iz0UfRZ5oKf_pOceMoQQYWswujsFWlNe63nai4linNacYQN-S9abe-AOxylzkxY7PKHbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=PExtoJ63Il2QgM-3NmBVLhZFB0EVZrbrBhJCbXd42vxm9aBonB0X1CGFtR-7bwExhdT2jVhJXENiYSU5xMUOhkYCHmg0t2iPgx2LDiosFQtXlzD9T-CQnEcPmMc46jBVjGxIEf5gTCXOIygxGwG_Cl-kKhhqC1KwCOOcfCj0D-Xlps-BaP-wMaFdIXsOsagktSQQUtsbYU9hlvyMljc9jTDTq_k7JF8Vna-x9pLILeSyPoo7nl1WzOw7XmG6NrnwClT38VrsySUP88h_Iz0UfRZ5oKf_pOceMoQQYWswujsFWlNe63nai4linNacYQN-S9abe-AOxylzkxY7PKHbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=R1SQnDBattwfVixKQ4DSgZU0H-Rj1YZ_jUPhrHmIBbJYTZ-xpRCQKjey9CdUFzxxUiCSL-NCMLpIm9ZqtWXRPnxBEDUX-WaOR1labgGpZ4N7t22fiucsEUq7jbvJ24ecU7I_C7AzJq4FrOEvOcJ2QvVtTlcoRdR998ytc1_Zs4B0_jSgCFvEvEU0YvBbrkfWrtKmisGIBocu3y8xR5UCub7NwS6HomMAaT624RRwCw_IbJmqNgKkpOTpXw3X3rTSugMMKGnSqXhnFF3R7mSfrXYDFJf3KYB6_AeaYw_uCznwSRFmvVLZ5NWNfmgGOnP4s5V2gRBhCVhB3lO0SZeBGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=R1SQnDBattwfVixKQ4DSgZU0H-Rj1YZ_jUPhrHmIBbJYTZ-xpRCQKjey9CdUFzxxUiCSL-NCMLpIm9ZqtWXRPnxBEDUX-WaOR1labgGpZ4N7t22fiucsEUq7jbvJ24ecU7I_C7AzJq4FrOEvOcJ2QvVtTlcoRdR998ytc1_Zs4B0_jSgCFvEvEU0YvBbrkfWrtKmisGIBocu3y8xR5UCub7NwS6HomMAaT624RRwCw_IbJmqNgKkpOTpXw3X3rTSugMMKGnSqXhnFF3R7mSfrXYDFJf3KYB6_AeaYw_uCznwSRFmvVLZ5NWNfmgGOnP4s5V2gRBhCVhB3lO0SZeBGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=t4vunyDnq731tAXEZOASjcuS_eQ33aNl0ZoI5Zl-ZWF_TOhJzoqCdmesis2-Ik8ywVrb-Mf7ojDI6wCGlmTvc8xD4Rg0e7PLT_HLeuLSORyaj0orVBmH-vamSovWSBXh7rLR0jko0bS0iVcKifPIGO7BjmlqwCOn_RS2cgtI4g9ai6yw_Dl9xXbbGKoZy3_VASdK2bV3oYcGxp5z_XGr5uXwfuBTn0r7V0ASHol34cjEbTcyCTSzcdqjiaH3wVzq2eOXJwX45d6BKIgNhi-Og_5OriNaETI-92BmwG4i_5neZxs-3-sjzWEkUHcvntdVFkNaFJh3vfQpmp1Y4i6TyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=t4vunyDnq731tAXEZOASjcuS_eQ33aNl0ZoI5Zl-ZWF_TOhJzoqCdmesis2-Ik8ywVrb-Mf7ojDI6wCGlmTvc8xD4Rg0e7PLT_HLeuLSORyaj0orVBmH-vamSovWSBXh7rLR0jko0bS0iVcKifPIGO7BjmlqwCOn_RS2cgtI4g9ai6yw_Dl9xXbbGKoZy3_VASdK2bV3oYcGxp5z_XGr5uXwfuBTn0r7V0ASHol34cjEbTcyCTSzcdqjiaH3wVzq2eOXJwX45d6BKIgNhi-Og_5OriNaETI-92BmwG4i_5neZxs-3-sjzWEkUHcvntdVFkNaFJh3vfQpmp1Y4i6TyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=Ryd8c1soYI3RY8L8uP6v0D2aO8LZujulNP7KINqE1kOOGJG633zwwSXwRTEgqSZuM24_xWKKmD1CApjaJgGI_GlXO2AdvIPb-_6xR-45jVa8p_ZFHgeuRkd917T0NxgpoHFTt7WDOro5Bp-LiaF6fkbt1w-hFtbkxOh_L99c5jNfTk49V7to5P9X9F4chJh9APXZt5xXc74fIxwqhCnXY5qkrCFS6w4tKIr_xevjF_T3dWPxr1trAHFZq5GEtpnXJNey-bO2-ynUJQwuPebj9uUUEphPO-3hQYWc2UAGF_nHJmJf1ZOBUdR3QCTghOlVh-mwaIrsuMkOfDW6Cl8TJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=Ryd8c1soYI3RY8L8uP6v0D2aO8LZujulNP7KINqE1kOOGJG633zwwSXwRTEgqSZuM24_xWKKmD1CApjaJgGI_GlXO2AdvIPb-_6xR-45jVa8p_ZFHgeuRkd917T0NxgpoHFTt7WDOro5Bp-LiaF6fkbt1w-hFtbkxOh_L99c5jNfTk49V7to5P9X9F4chJh9APXZt5xXc74fIxwqhCnXY5qkrCFS6w4tKIr_xevjF_T3dWPxr1trAHFZq5GEtpnXJNey-bO2-ynUJQwuPebj9uUUEphPO-3hQYWc2UAGF_nHJmJf1ZOBUdR3QCTghOlVh-mwaIrsuMkOfDW6Cl8TJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=u4D2aPc5xrosUxPCJU8yg6l-aKlU1gvw5K0VGVL1H2pw-nPKoTKSQLcblzcwXxIFzsH3G2hKOKxEA4s40Y7ane2DIvV847fI5PwNi-FIMSAUBwwo32J31Skgvgp7WJi4ilVh_gFHfO4P0D9_OB2F-F1bdze2UEDg4Sz1-NBoKT1bOEw-iVh_nfG2Eil7Yet9ka7oe3Cu_fr8EVQwKkNEHYHEyyTxsYAl2qF-dgLb16CtroMrVbamVzQWLcgsjqL1f9YeZbaMayDgKK6hKkcD0dPnGleQOJOxsCMBTM7BPkB9DBf70WFvqSZ4aqSBu5_26lN0_34ZcKYZsmyqe8DBVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=u4D2aPc5xrosUxPCJU8yg6l-aKlU1gvw5K0VGVL1H2pw-nPKoTKSQLcblzcwXxIFzsH3G2hKOKxEA4s40Y7ane2DIvV847fI5PwNi-FIMSAUBwwo32J31Skgvgp7WJi4ilVh_gFHfO4P0D9_OB2F-F1bdze2UEDg4Sz1-NBoKT1bOEw-iVh_nfG2Eil7Yet9ka7oe3Cu_fr8EVQwKkNEHYHEyyTxsYAl2qF-dgLb16CtroMrVbamVzQWLcgsjqL1f9YeZbaMayDgKK6hKkcD0dPnGleQOJOxsCMBTM7BPkB9DBf70WFvqSZ4aqSBu5_26lN0_34ZcKYZsmyqe8DBVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nPmEP0Ce7eSq2rDgmhbDp4i5JsfoOimUm8UXgxa7y8mlYLK-YAbdQLV14Lmp0bQ7um-1k78PajmBYL1-4BdQpjeTJpDpWp4MJ86jGKic2fQhsGiq8n4aME5bu6Jcd5rmLJoxE4x2S2dp_XPNI6n3lIBNKpjF0msQwnAKKVbf9dYm9yeb9e2EKnblDvGdltArnQMOxWucFInInANnLVI6QmZxUQRGKoQFE31DixipOPg7KJ6Dsudb3y2kAWLbhRzza_5hikVJm-z90gzvw8_BqlJIErXRA-S9vctd-iLWH8z_XbduSAxE5xD-khIATuuPbh935qyRNNKKVwqDIhTb5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=jpQ5PAg43W6lOwv12-fQdXrChG2o_CprOX20B6Wc_WkMGCfXXVGIO6hsPgf3VIJXYmTLOGtzNiLl2e9ibuI2gVEhorXMV6CV7wDjzv4UqrahHqw_W5xdmQRy8ZDOVGp1a39MJNCaQ5UracptIMaQlMwettDPAfC5ZL8z6-BkdoxTgckgO8LKjsZfcQfq1zw0vdc-iRpMhNDuhLeH8LM9fDS2l_i10u9kIdP5o4P8QcWJUvxKRnJuC0JcctB8JzbNeR9OWXxVuuqt-CnV7l8y_6VMb8iSCXLBM-4VjNhQkO7uThUmRga0Z0U52y-GSW8chCe6hg92SpF4zbkk5oeAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=jpQ5PAg43W6lOwv12-fQdXrChG2o_CprOX20B6Wc_WkMGCfXXVGIO6hsPgf3VIJXYmTLOGtzNiLl2e9ibuI2gVEhorXMV6CV7wDjzv4UqrahHqw_W5xdmQRy8ZDOVGp1a39MJNCaQ5UracptIMaQlMwettDPAfC5ZL8z6-BkdoxTgckgO8LKjsZfcQfq1zw0vdc-iRpMhNDuhLeH8LM9fDS2l_i10u9kIdP5o4P8QcWJUvxKRnJuC0JcctB8JzbNeR9OWXxVuuqt-CnV7l8y_6VMb8iSCXLBM-4VjNhQkO7uThUmRga0Z0U52y-GSW8chCe6hg92SpF4zbkk5oeAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTMc-Y21r0xJKbsEAbVDDRRfrdt6qMKPKXkeAt6cP7g7fjUvcvQ5w6_kgKtHqX2UPecPVPbWdg5dsBPwQ45Imov_zaXPLqbZr36TAiYonRas5fnMPn3H9roOo420LFJ4y66yF9zX3PVH3el6yWYx6pFeuwNMB4dz4zCQZ5POkiTSglUKkbb4AY64QZNX4V1TIOjmqN0GfNbNWdNFyaYf11Waw9qbPi7swO2ajkdc9Xb_aHwreTq-5dF7lCbz6rkyv_pDocpugHSTcDsZ3NnDqKCrfAz9wgu3pNawSD70X15YRm-T20CjiczRI_-MHlgbMFqZ4DFbxbrpFLjDW82BIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=dj424v9AH5VHInY7PdChzI4lE80_WzesVkwWXE__gZl7msnUn_tMg0bokQxChVjRqaK0zrOf5OYwMLtXPTDzeuBgY5hAkRwJ9N0IbWKN-NlmJSzaiVprsG3uSrpyOEDQrlgVnrgyaiOcU3yhmcCc6A78wcWsM85RhN36Er_ar0O51fMpvTjd_sRec1w1qnfUlNxhlQ8dGn1q6GBf_svEiStKlhjiFBGEzZCDjaVamWl4OwgE5stnEjljF_kriqRviaFkacvvnx9wKgDbEzhL_vXoWoa7puZlp8nuHvn6xnJOC5QVE8CyuOIMD-dGh8tLMNfip26q9IzVECncGFrG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=dj424v9AH5VHInY7PdChzI4lE80_WzesVkwWXE__gZl7msnUn_tMg0bokQxChVjRqaK0zrOf5OYwMLtXPTDzeuBgY5hAkRwJ9N0IbWKN-NlmJSzaiVprsG3uSrpyOEDQrlgVnrgyaiOcU3yhmcCc6A78wcWsM85RhN36Er_ar0O51fMpvTjd_sRec1w1qnfUlNxhlQ8dGn1q6GBf_svEiStKlhjiFBGEzZCDjaVamWl4OwgE5stnEjljF_kriqRviaFkacvvnx9wKgDbEzhL_vXoWoa7puZlp8nuHvn6xnJOC5QVE8CyuOIMD-dGh8tLMNfip26q9IzVECncGFrG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqAaoHAMWy0OWX3Vuth5-2VDiiEcr9WS6eGDBqRiQ9WYuJXboI2KnENTqZWgMBxF3em2230-FSnPEjVybAIttK5G17M32bg4BeAoMbbjv1wO_ilEyoDEfuBd02sufa9hcRggnbFtVmrXhgdGl_eC4jNimFFNWm4wOfezC-elqpQ2avEoHq0wN9BwLQT5gt-LipTCOrrTAi5-Iy4ETFbObCrPXz3N2CUkL_Hi0wBrLgB2SOB-lXjYwQsV0fYZTj0myJpNhJc988DckIlf_sLHNHLFzNjvaQH1IVt_NkO4x0LWc22NMCS4u7-YB8rQzzhLj3QRnEaVDajlFKh2RLZ5CfvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqAaoHAMWy0OWX3Vuth5-2VDiiEcr9WS6eGDBqRiQ9WYuJXboI2KnENTqZWgMBxF3em2230-FSnPEjVybAIttK5G17M32bg4BeAoMbbjv1wO_ilEyoDEfuBd02sufa9hcRggnbFtVmrXhgdGl_eC4jNimFFNWm4wOfezC-elqpQ2avEoHq0wN9BwLQT5gt-LipTCOrrTAi5-Iy4ETFbObCrPXz3N2CUkL_Hi0wBrLgB2SOB-lXjYwQsV0fYZTj0myJpNhJc988DckIlf_sLHNHLFzNjvaQH1IVt_NkO4x0LWc22NMCS4u7-YB8rQzzhLj3QRnEaVDajlFKh2RLZ5CfvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ke1WoX4zEaDieT9XmBCmTBccrCu72JWbvcS7-9aQiM_UCAzkQ6Ff3ztnPEp0OEhylLqtcl4mznM2qWrcAKyGGlo93W0XsGLS36VbdWpChyIDCHE_PyrDXRBMbF3d2kaeCBfmKaStbo20BYxFJ2NkyMKgLxamlTBOOH4ECYo7CGyprs_pTo0FxZ8XnqV74UUah79N1KVwk0mtlnrSZwjwc_mmjxh2NdgjlfDOlp2B4wvEaksJ8aqOjF8sVxJAa8M4c_MGvLUN_yrAjYsIBGWc7hPHJ_1DBB9V3UtwpVpsMNhYeqfOk-bNSwfxuOtVSLMIZNHCaNC11QyGVqt0UUf_3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=KGSpybnth9JXNbj1Zqf_RAk4SgSVi77QRdBxdF_S0_EvDDp1QAIGcxJzzGUxA3j03J4zqeBn8Qu32Vioh61sqOIgG6qdXZ5FU4gLQwUCCgO60qnIc0qf3nyz6fxHiyFeIvChbFICqp7KWFnx3J4G4f-t_zCvXaIoSQlYeAU0dQI-oWTRlySjS_JueAh2zYBRHfKYEwpjrqKQ8eMSYN9utQJ0tXCaNp2JMCRecn5Xw610kRCi3IBMZg6WzjxaHjo5PAsjqwY7Amv5VTRMN6oykXwfAMPnR557MjnPVPoEkthKxjL_r2hgJoJGwftHIGsapEMYPEZMfR0Sj0V1swMIxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=KGSpybnth9JXNbj1Zqf_RAk4SgSVi77QRdBxdF_S0_EvDDp1QAIGcxJzzGUxA3j03J4zqeBn8Qu32Vioh61sqOIgG6qdXZ5FU4gLQwUCCgO60qnIc0qf3nyz6fxHiyFeIvChbFICqp7KWFnx3J4G4f-t_zCvXaIoSQlYeAU0dQI-oWTRlySjS_JueAh2zYBRHfKYEwpjrqKQ8eMSYN9utQJ0tXCaNp2JMCRecn5Xw610kRCi3IBMZg6WzjxaHjo5PAsjqwY7Amv5VTRMN6oykXwfAMPnR557MjnPVPoEkthKxjL_r2hgJoJGwftHIGsapEMYPEZMfR0Sj0V1swMIxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rMPF3smVCpt1xpJjvUF8gEHC05nZZhrmlkj765XLa5ndpmv3QM9n0g1ieLHjKb_oyW4SQaKnju5ZzW7VBDsm-11RLnDPU3vF_doX5SlXS9WaARRxjtWnmAZxtSC-BcWOL5NxA5U40MDIhIdV_r_g10PKjAR6XG9PBMhOUa1DRcopTklzU-cnh-N2FS8Z2em76WOBOh6YOOC4qYRqrFkARjGYQIX8k1iTW2HRZgeouMf1GVaNkwgTb9XIH47AK6y2RZnDfsiLg1s0yY-jjY7AozyDGxLm95C3t5g1f6wLKxjZoaQOenTAX3uKR7dOu9cpPvfGDjtZv8xYO1F2RSSHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJBf402GQWhBdxFMht1OQ8LxEYKAWW7Lc8Po5Fm0ejf7hCigmMuRKYcOkj7yz4ji0mp1s9L5_ckcJzc3XWhYxZCWz6RXM5LWGBLTFIv2R2wq6t8E-470ZzSdkMKHrlHRJUjFIj_5AdEzLVxOIADTM4ZxIChltc87myD_3kOF3x2KKXJOlaSfNdpC7qcgcVDOCEu98MiWp-3iN4ObSf4tWmvIIoHVMZzWXNK_M6o2bRE8WNAM3exxg3iY-WzGVpKfYMaXqzjTNDR7s3vsrOog3cab_Duh90nC4Gr0Ju27wGujChDF3MVKUYrS9esVWgjmx3VcEFDbi90K3KbRpXw6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ehfLBxQgbDgFaUbL30SsJSn2ec90r0-vrpfQSr8wf9ZXcJ2mmzQhuezQ9KQismXfGD4wlUpgauI2W5XyRUwCYBe6_Jui4B1VMuzggptVwTNi69lMvzx9-mTIQUOxIvxA2nD84gcdq81iXz5KhLiIWBJpbwmieMeENokUFnqkgDVyJTN00AfBL8krS9zXA1ORGlyLKdEmKefj_Hgv6iAiVloGW25ddZsPN1WqyIwkK1bh6KKlhcDKv3X3gaRU-tFTyr2h8z6XX3BS2BnnPcHcyQ71xaMfv_zSSZ163ZPSxEAAASwGmblWPuG9KLh2jzuKgNnVTD3mKz1JK2hFQEtsWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j-y0_GdbBpngxhwRpRMNhPqUNRVasjOkmufaEQsBkbgupYhjljJDIjP4ZbVi14jZevdX4GCIcGtqvs_SXWrUcKojjHyRWmMtdYqDq-ZzNrlGs22pfKlrip-NKn3LjIhzoIMrqVuZBwu1ietwiBGyiJjVS3KDAd-N4NaCYJ5Xwc_hvCnWKGI598P7qDECVwmQvrNyz01GpPL2D0XaJsd04DKqYXd2jfWIFtCtJX2-XDFCrRAO8Zxxes_9XgFLQSqLGcEnqeQ5nwdJYYpth54UahxpI2uEgyReTHga4fmBxfdPFx7D98UKNyuJpYVoRXKP4hgPCdNypLLvzWhHN30aCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ik8SpJy-WCjghHQ0qGhWWtOiGB8tsG-e9NrKKDCuaU30sziMd_kH5sKrYpr6fyoAlgJNSpkVq2ibhxNapiCCPp9fiZAjPNCQcwnn7HR4RrfO1w5IaTKEw4dkdNGvsc_qeAP7_UYb2fVyRPLaeIshEXTYp8-RWg15okSfulgt-WUF0_3zLHpCvEI8p_UyugyRCZLcwGxE-Ih-VNAtW_SDLU7OwLvmaJkpEIUqW4cpV9DIWUWfkEdiOGcRWj_mWiMo3gtqPKnP_bRv8D9m5jffyihyTYM0GC9IhNrJWxsjsLsYolj29m3f_kP1j2vz0NeVJbAK_skbjdgybWoRwvyWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhzQD-CNhKZBmcDKyB_ajNKe0dKdsb-0beQf7gYnPM34m38J1UP2oFks0DnP_qGK8SiYgvC0-BDZMKAUyoKdK37zpDaF_7eMeF8xewdxLOal7kUAU3TA3uMx1lWiw6-URmx4lXdaj-SaFLGO8fu3vrq_Txx-TzA3-m2YX-RcPhlUnUjARkowWFpVYiRJVmP9rU8zNpWBdK18amAEjI2OmKG12rMB3T01SKKUqe_mCb1bwfmCqoTGnbIG6Pw2aNgF-9C5tn0JaLYWCh95-SFdbV7OrVLwvMUarodhokk8yZIjbM5PRFr_dOr1Yo5SIVTtR7AC_BnQgYDHSNAOAZgj6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNNIF2P6765VmCq3Ayi5_hkAc0qX3F9DNgA0mCQ4lOVfitdIa9rVrvJte5pI8xNKoEIwILcYK4sMOsmetLEl2TC_ov9xmFKPgJRYuhpzEVcVNs3JKJxrLyVrTxvSmEvV6bLUf_xtazuOiNTx9t1jd3wtRx5YXUsrR1z6kT4iPD31Wt3l5nKuFcARbEIjbhlYGwbi0xR6Ia-b5_nKNNLv-AfjgEWoPXGpgqFQZAIutNj2K-NS89f76anxPk1FmR2pUAKtUowscCrCP3Mos-1XrEO21Ahm6r8jP4KpmlqTXCXfdzr4aGsmXleXfdkLg4HCvMhLvaxd4WAsPmpBJ6iNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngLe0GHtcG9lmgKAK8KAKBcCZXae_Oe66ZmORdpMINmXHWG5fgbY-Ia1PCJFDS3nuyqUcwGvMksnYIoWtk0o1Bexl3EAiYW0SaR_kBd5u6UsekSzA6caMdHffEnlrpd8fSXjHJTjd6-XCBOBXK_1lSPOispkgXGRO2McQsZG8qLTXJEEvjFxry4SxOaTAXk404xpBPUxTEtywBVfPhWsZLjX0pCgPPH1tMcIUo4iizc1I_JjntZeMWFsB8AITEgCIR5Df1acZegIkKPfwLDqghfacLsIO9jEDQTpt86qCkP2KHUeJGPkH6owPAGrz5PqxjoHhQBvdiH2sy9vUBcD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjGmqgniLndfW0UAwhxhzM1qbJJR5bge32Vym7RIU1U4gPSVLId17LNjLunak0AdkF4R7YCgp2qT6nD0e1RNb2V84-Fb5_9oz9-P24nstOx02i45chO94iNYV2GmxhXUFTmQhA08LyKyTG4sOjirme9PJoNl-4Nh-JuEzkr_pFCoSKrpzH-wRGW5SnyM4ZLnbQDchfQv28bDMd9E1OSzmY5OGBkKP_1jxMUKGTi7qqEyk1z4GFy5DC1zZAALOv1FJncmwj3is69TS50o_M7QcDRZ0XQHGx5w8sDmdhsnL21FpyParxtyuCzvBUJh2GEOpui0SZaKpCVnukG3HTjU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmLLNKl8_HzGJzcfan8lUxJR6RUZ17RdKMrBp8FvLcKx1k0LOy8j2QNyu37vfzXLsNev07uIlFJX9H1uqKDuLxR5ywdwvo0liIB8hPMRHuG_PJGn4SDaGaVAjqJD4YxBQ2BsXqbK1LdDz_HuWi2cQBYp2NHYvhFOXDTTjZZ4_tqtSKDX4QuTXf1r93zNCS_HdMie8iZ7BtGfzV8jlvPzgF5-FQETaTrEcHkp55zonc1WBNlmWjqthJ7oJZgxhG2vQt535e5qCLmb9tZvHLIK6C3Dk4OBk03ZLgW5xAb2CZRE6cdAUG-FGVYh-bxfil0sCaKU14OA3iVYuviJ91N_Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_JEkGxeBiu96IAaMkS39p9D2Kz-gGOu4n4eulArXhPTnk2yjHM0In5PiERNdFVA8yfAij7OrNzxmnHXfUE__XyK_jb0LNhalVZLZbgFO5us7mmxxrTF51-SVAPUruODYh3dkKYQG6Bb8ohZ2Uf4vznwR3tbN76uXi8_F1lu8CzJY-j-xLfo_7G3slhR-DuDMtHddR5IMAC0ijHQrUf4W7Ersme03SwdlNgdJYKuRvx8-OT0K5qVoll6nAgkYx4bxl8QUZms3NQAMTgcmb0Di_2LnwWys0fQxA9-jsFySTj26V1DVNDjWLfogvJA6f0jqUIpGKva4YUTqT4juevdWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY9YcXgpwKdWXUtnRIljReAhcdoJT815ww6zJz3D520yvASV2iqv9Fuomilw8oOFjdqGO6i5U9A-ZieAA_-e83VWF56J2d_AQGjiNmIUG8pJ47i24ekBOCXeXCL46HQIXq0HnPdedx5zxZSwE2bLGvKiit3nxt2W31q6KXHR8wUx16SZ74qVn1ObiovzyTfiAAOVip8epnpM0bC8lB3vbfMDuCe12rIBminFSyG26rCTa7zILMAKjOr73HE_kfXyQFC8wPeXriMdvzaD3JctBLpPJNbRwiNlIbst59aNVcZmdBoqed4iZSgCqF-8W1Y9jx_b6ObMelHjnE3g1ET8Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0FItCMR8S-651wU-W0791ar5ics90iMhtsRG6kHpS4CA4tUUK7bXLcmpk4pdov3B6mSq5GOOYEZjdMZyOhwdnYXXyPJ3M3mn0y2rTlFeSCrbVeYYPtpWfhtaQ5pR8K0GUDmMktYS29ncyZLrZDnLEej-iNPTrmmSgfcvVbBIv7t45E4n0psvheUP4sQQiyAbuAmwut8PZqWheczgB1A697D795Q5fH9wToSXimfJNPK42cDrFuqPSi6J4czqFQtRjKRf6_dBlsPx3gis7Y-QPkh26wOVD4Si-u2OawbZj_bCQztj5N3093O9YzcC2Uh5pOGL5idOrD-4kIUhzpN2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCOeDpTXftbZPTxj6nP1h4E0d1DVscWCg7DeuU51nm8YaOaq7ksBr2xl5EBFYByBIDLugB6O6ZR77X1iTFnLFVolelVYq9lRN0Zt27WjxLxUDsK-c0Ki5Kj1EAtgg5ArePrD2_AjWtV2gB2pPSGbM4iHfE9_zGw9ZhjuDn_0MyR32skUhrGSMliOhf-P2E7IP2xqYXRgJB_q33yjSS7_jkh0BdQSTS4zyoriu90J3zTkQM_GgPuHmF07YcrbEEjxiTquos3ABWbedrWz3rpQLG-uOY4Y85X9E9N6kXQ3jZr27r-FTPnxoc6CmnX5CTY49ZuBP6V1r6wm-vYRZC7ZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwQxtEVOSt2rW3EaLQftfPdrg9Mi-sdMDm52IZQqIb7IRdLHLJ158Y_m0-TKUzmSpdgq6RxeB_VlLFUGK9Bz_yZUz0155hRYQYNQ-13fRHCqX167c2gad18rX0-75hCuUPSkVIK4cktSV0ZY0MKtL7WN7Uhwt0XHF8kFIVV_6Jq7Lyn2SiZQBC2bafnJ0aD5Ap93nomqTbb3Wn4UBznGALgRUXzc1L2N-6ekAERIIk1oX8m6ONAVcjTG3E0EfDgAGkwm01u-MJKvXIvhv6RO3loxAINxI18ccWf5JE10OAzwAh6MPF3CNbPzFG8Q_LKS-F-6MGSMUHlxHrE2qtzwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQGzBLS_fO5ynG96OCH_Nv-oTsY1z_lgpIm2h7Blfz5yRJSxH26pDW_G77zu4n88BOAkD1UcsraV-yLFxf4HwnNwiTnv_BUOu2Gl2nGiE_CaV1atKpK0iFs1L8pjyswARUWr5qfIkeEB0WGWfOSNyZX3nlw0MuNlgCc8jUMM_C-MnWNxoz9UJZnnf_7Siln0X6xH4KLSJFOGLULRPtUlRCW-lo7eMaxQNhWdliHZYvqRsNfdCGlocFR1cXa-s0Rr2yFjn8V9xgRbPLsQYq7kD2CDDGdpMnScEL9JBH5Hc9Phfq9Tich41BTi6u9oOtgJO2KrsL2l1IqjCzO4H8jVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
چلسی پیشنهاد سه باشگاه اروپایی برای جذب ژائو پدرو را رد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102519" target="_blank">📅 17:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXbLxqXQ5bX37nPPrRRwft8E6jahCCU_JHVxJ0dQJX9XsIyH_lYOscmikAlnVb_d8EKOvHU-xVTIZMmjZ1CrPkn3YudH_5M1dRasyI0ik0WYWbW9mol4SERM8_MI9gcokzhhUV4rZUzdRFoo72LhD5kJHBtDqLxtGh1vRkrVNYoUoxo06Lx8JWtNfMWMldO3aHpkDzBzrs7SMHP-yJVGP0wPBnlljx9zjZ1xOParw5R6TWljSamS-LENubJ1PPVjOaxhPUn4i53QJv-o0PQhEsdUIghmqeoHOt4E-FGJRWdJ4p_VIuvpvRDrPTfrKS0nDjUYH0zQeAe-6e5Af8taHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس طاقچه بالا میزاره و ممکنه بره آرسنال؟!
من یک ایده دارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102518" target="_blank">📅 17:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102517">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7Vg4owMt3NtX1Fz0MzUalOZk4sdBbDNQEEFWWbFl5LT_461WcReSuXFuOGKv3WHGEmD-a0jusGiPDWGhJ9uO-FcAdifyg0NhBvuPhgU0EtlrbfNh3nLVlOt1NbqK6qwYfn_rDLh2TZiMBLc2ttC8rj8AK9E8pNmLVD2sMR4akXqg6Jt0OmBJtmQZM4c-21W00EVVTuzR32_gyZDmXuFFKiHBVEjYG_z7MOjJwaNx-oD3a2__VZD8n_NTqYaJbI6qTSyZ-rpcFWpsuWnGpLPcng4dTulqpDyHJqcPoPZPMgbOZsCiJuK-3wRyj8M865d9d5Or3eoHfk7cyH9S_y_Ap-JpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb462e454.mp4?token=Jx5uPb2Nyl_48mk66BoRJeD7YsjMeNd3W9kDJp4_4glTi7Xzh9yPVrkr6MwF2oqgs_EBThO4KlrRQULCu-Y1oXPScnqpoJlNQll4dA7jSbt3L3Tunalef1Oo4cbmy3YL7GWCCTJC9H0dPznSMV7s-ukKlD3LfTEs6HF9Ay2tIH_7BmAqW7GB3GlenEmH9AgNrqcI0NTo_RRE4MB5LhwAylLslLu73UihjIQLZKM-XKPDRkR2bEXlXgdPEbp4sx0bVm3IB8sWXcg6_58YTU5TcXJio_qVQ-TTx5-pPCxHlnJXr-c1edIETTxivVprrIBsEkUPJavqVjJNeezOKO7Vg4owMt3NtX1Fz0MzUalOZk4sdBbDNQEEFWWbFl5LT_461WcReSuXFuOGKv3WHGEmD-a0jusGiPDWGhJ9uO-FcAdifyg0NhBvuPhgU0EtlrbfNh3nLVlOt1NbqK6qwYfn_rDLh2TZiMBLc2ttC8rj8AK9E8pNmLVD2sMR4akXqg6Jt0OmBJtmQZM4c-21W00EVVTuzR32_gyZDmXuFFKiHBVEjYG_z7MOjJwaNx-oD3a2__VZD8n_NTqYaJbI6qTSyZ-rpcFWpsuWnGpLPcng4dTulqpDyHJqcPoPZPMgbOZsCiJuK-3wRyj8M865d9d5Or3eoHfk7cyH9S_y_Ap-JpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چرخ تو اکسپلور میزنی میبینی پر شده از کلیپای عروسی ورژن ایرانی رونالدو و جورجینا
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102517" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102513">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxANKs80GbJUrPQPSFaxxUpGBG3KVSUrmsYE6uU9ZQ4ryAE84yNiYBhSiYqIN8UNpf11Y7w3cz5vGkNG8xlH6rnLZ8-M1twfqa0Bkok4Oo_YSRHaILB0TVSuAQQ9ZH7g7G3H0q2jtMlB7MpxniqVIvNpBvZwlSQc32vFTD3cFKwRiUTav-fvEb3olZNJo3ByhtfJM05dmLpXWizCum_SE6DedwiG224vjPExBcw8zLhh02kot7gtsDO4lrXS6a0eQlHJwbzoAax-zDKKCqDZkAeAyVTan0JwcTNdjkjA9I_nQ6Imje1V5KOOBCTcY7xDCdnvETF8Pz2uliyLtuf7Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMgjEJc_kD8vs1fdY5xTu6Hwl6UyEaU59KDDLinsiHDMYkmwsGpkkvSUKVeTRTVEup7TLVwKlRSQy8ihS3wb_ytO9zEGFVWNug79apqaLMh83T8GR02JIUIrXLtP30SffzAOhsRjaD_7VWQgl1arz5CZ9vUwUCAbFYuQhYmbwrUCXNvVcb4N3bue-OkPDrqlsEoodvaGlOcmacID3VzUXCPq9eZeP1youUGDds2HWzBcv2mJ5sOJDQUWCWVU7sk4lT14AD4YAWnX6g4BnoFD4aHrNc3QKZ1enomrMyMh-trPgJuTDystV36Ve4WCFkge-p4QkIKzgEwe6-ueZyhAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmF7p-7oEGHdLBR7LLQyqSNAX4gwKSm8nj-zk9jkNCRUeRExmxWMZ28TNRWNb0PCpEvV6SbRC0DoTXl2zvGSHCShTFlmdUtD30-Vn9NdPXXqxtPPIkrhP6nkn0JMeipR2dHgDiq4LOGH7jHG-itxYJFgJSkCt9SjEd-8EyX-hetm66Xxt4Axp-2im0JuNQlY7VrjRjk_HLCDXLRuNgsM1j-I6_cmwwFI_K_Ew0rYnHrlKjTMk08m3W2tuYlPQS6FcNQrbJBF9-ox59vXi__-ooHmnX0ZbBtlVOzEeyAdgDMblS_sKP4w7wSTM1MxWlnh8B9VF4WYYY294VoUo7tv6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TnsV87Gh-BJs9zO6mSl4Mr3u9WytZu2NW7RgSoWksG7Cz3BS9KieieE9pSzSIvQ_dLzSOA7R6z8va4xTyPTYM-VunUvFSLUlh7t118kGyVKWC5G3RJ6JbFJJoM7H6IRjMjTJpo8WwaM8yfrXfqAWJ0MsCe1_v8hVKB4oXIvK3_op-HRCZ-lElcepNPb5c0ygTWHTxGy9Dwl3x2XN-wd-ofYWQf93vKrfG5VLx_esfHb7yDUf_Fgc7Dpb8VnrLUyKQX6NWSGnsjyNBrZ9Bx3kkhRBQwOCMrX7Ap3tB27xdwIzUEhQmSyabgkfroC6Xrb73cJV07jig0UrjOHlAwVqlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پستای جدید جورجی جون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102513" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102512">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isW0hjsqz4lzLNauS8Wttmypw2zMYEvkNf3I4CUSoE0CIjHBAsk7VIN4_fDgvtNaIpHOlfB30rPQdS0XapXUI4KXP80D8tSJqzXW1WiWNSf2cpoGSwP_UChzuAw_FqM1vfxmqdlyy71c986Lvn5ioz68fRQUMot6cjT4tVKcMDmih_43uB3Z3xCwngAqkFJg-IofJefq9CU3iswLjs4u91YDO4ynLprLAiw0swKJ910KYjv8diiUlNSGoAJe4nD-PfwBsOdBFw3j8W0kfnFY7wtE_9sTEcv9ASNIpWhCvR0m8SJVTbdrGTk8PH5PPgB_ha1-CJ8cFI6JJp1jTpBaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔵
اینتر با نتیجه [3-1] در ضربات پنالتی مقابل منچسترسیتی پیروز شد. بازیکنای منچسترسیتی سه پنالتی رو خراب کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102512" target="_blank">📅 17:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102511">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=kpzQIJhUi7uQsVA_7b9cqHtwWOmL8Fh-1QrwH7iuT28Kq0hCukiaWavqv9pRTJpAjEY0ZWT3TsEEUegSBmfRZUeL4rfL2guT1eXt3kEIEk6d8SWZHhDEiF35HZiK2htSL1Gef2jeoGPuKmNf86fxW2QGunj8sI4I6s4G3am3Bp_0Rp9cd2905ZEgZakjFFjflzlAEMcrj3oKbkYNZ--8JU1Zr_Jr9P8HP7tM6GA5VbEprKGV0Frw5RF_FXe9sOnAKm36LiaR1f_O9DVdDMeQKNYKgdLEXkAXgUMzF2vXzM2uaLD4Oh6Y3TJxN58ED9HHiUZ2ViE1CGQhuOxHwgyr7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f1ded84b.mp4?token=kpzQIJhUi7uQsVA_7b9cqHtwWOmL8Fh-1QrwH7iuT28Kq0hCukiaWavqv9pRTJpAjEY0ZWT3TsEEUegSBmfRZUeL4rfL2guT1eXt3kEIEk6d8SWZHhDEiF35HZiK2htSL1Gef2jeoGPuKmNf86fxW2QGunj8sI4I6s4G3am3Bp_0Rp9cd2905ZEgZakjFFjflzlAEMcrj3oKbkYNZ--8JU1Zr_Jr9P8HP7tM6GA5VbEprKGV0Frw5RF_FXe9sOnAKm36LiaR1f_O9DVdDMeQKNYKgdLEXkAXgUMzF2vXzM2uaLD4Oh6Y3TJxN58ED9HHiUZ2ViE1CGQhuOxHwgyr7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اگر پاس گل پوشکاش داشت، اوزیل بیشترین رو توی افتخارات‌ش میداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102511" target="_blank">📅 17:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102510">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEUyeUweAgmPQ9vYU6paOYXsu5NdAhtB-VQ54zb5PQKqImivTVxgnKJaRrAy2LmpnhzCj99qFPFPBSypQx49ySZ4NoOVqeL4OJhIqelFu8r-y-V-P4uh8qjp1dqshxWEJJPd3jqMiOFfyHPWM6RrSd9GRkprsdEJ4Bx5qIMxXuH07uvQnMl5cQh2-UrmW-ruDffwi_tCbxiaAgNTL7yIIE07tWN0JOD50TvqmTJizA7S9UvQBZuVcezt4xVie05XLqZ49hhV8sTCqmfyOWWdDLvYvIu-9ioizKDUijN2HT2o6s2nRQ_iIHNicF40PsRLQNK3jBf0t5zdtUcGhTOIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اورنشتین | اگر وینیسیوس با رئال مادرید به توافق نرسه حاضره همین فصل به آرسنال بره.
ماریو کورتگانا: آرسنال ماه‌هاست که برای جذب وینیسیوس به طور مخفیانه حرکت می‌کند. آندریا برتا، مدیر ورزشی، با اطرافیان وینیسیوس گفتگوهایی داشته است. چهره‌های کلیدی آرسنال نیز به نمایندگان او اعلام کرده‌اند که او مهره کلیدی یک پروژه مستحکم خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102510" target="_blank">📅 16:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102509">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8Xc3IN95cNfnu0wk-CE612hs4c6v6CI2vLBUs9GTaLwc0Wz3cTgMOQXA7Kn0tMR9vJrMMZ_7h2xDfsB9zVxNjJ7UCT4uW72wJpUbuODYAsBbUHYUmhGiuNKz1pmitx5o_FDPtskxLgRli8azg-R-2kWXA_CdTraPYJBWKccvOxt1f1UuvXIb9I_2bVqMEKBDuSKjw2mb4CB9MMj6Lnd9SAaI7wq4NeTbP9-SMH-TvTUf152LnoMYTsccvO4tT7O8jnh54GlRH0-aj5g-U-i4jKDJxJRUWL3EJpGKEsOScDgjtz6jn-7tOJFJZ7HvZrjeJlZyNNy2NNQMYk91oC6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رودرا - ESPN:
طبق اطلاعاتی که به من رسیده، انتقال یان دیومانده به رئال مادرید با مبلغ ۱۲۲ میلیون یورو + ۱۰ میلیون یورو بند پاداش نهایی خواهد شد. همچنین انتقال رودری حدود ۶۵ میلیون یورو هزینه خواهد داشت و باشگاه در حال حاضر منتظر نهایی شدن انتقال بوعدی است.
⚽️
@Futball180TV
‌</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102509" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102508">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sff6yS7Bf1JWsrgf5j7UHwn8wp-oFC3Zval9bU2W5Xcm-31g_0Ocgj7PUoxIkOXVZWKvDa3R99W17hu3MIWmI7SPQas3pRfWLbv4w_vY11kfI6H-cEo0KxZOfctvL9mETJwlBXO2iJwOc0xH9D9l4W1WxMkjTZFzfUWMwqNRTDRtfF2o6LxVFsXvkaP-uZc8ANXpx79w_m0_k3YHkBheYYX66lbPYTkGQRcpPgot39ZvbHbjqxfkL_0HGmYI001N1Evr5cutkdaOO37PHvGe-RDnOn2w3kf4sof_UV0x1RJedHjJ5_7qtrnOT5JqydHPh5LA4KpFunHqIQtADt3L3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین شات از عشقتون وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102508" target="_blank">📅 16:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102507">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liqpIZdH-MOHUIDB2nHamCz9GhNps1WFh9JrYruUvVdWb2FLxiJ4U126kDlBHE8kkJsbferU4D-EOwzzr5qNXjQMl9wUBbHBtj5xkMq2-sEjJGckWlGc-StHBQNFfK6DCvwAR0D9veeiKz3dOTV7QA2Fg8rLVOmUJe1X3M1Uag7rTFq_NcwPcW6Gm3Mo7BGROoCASfJONhMAHeEpURyBv3A9qUrjVUV3VCPSs1cxvabefsNansP390tgtt1VrnMHRN88hpwSNPIbW47SQ5LQmDD2gb5J6frIXUXXQ9uh0XkBZw_DE1sSZkoWIgEiDUktamxnpEytekMBX_jGzKkIrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
چلسی در یک دیدار تماشایی موفق شد به تاتنهام 10 نفره 2-1 ببازه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102507" target="_blank">📅 15:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102506">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO7iIWgJ6isXWsvmMHLbPuJ5fHQvHNGRudhZpn7TKt9o-If_EaP2eU88DGnBOdooPVxfL1PS64Pzzh567qOragZgcGGwtq2ylLohhAUX8O-CExNxPg7gOy92d_i3EyH0eKeKXXkDGTqEk9JNUduvioELpQZyabiA-9MNMLdnGLrtQGxVIz7YbZU8AkrylpX8Yvm4nG3Q2dTKrFJgcHlWem3jgtNBEfelFbCvKn_hp3cU_d_MaeDjYVvmX5vDG-YOcC-2UM6SKIH05HSdieIvfJSHAzQwMNpzZA53h5TsM9byK8dKFrHew6nJhFqUUy9xEYNOTHtpHP7-6m_7TJzJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
تام هالند:
بدترین تصمیم عمرم که خیلی ازش پشیمون هستم اینه که طرفدار تاتنهام شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/102506" target="_blank">📅 15:07 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CJ4CRlP631mqj0mNxPX_6necjEZJqxdYS9EHryAf8Yp6GQ1dcVROgYJsG_AniUpIGr1Wbnqm6_TFowr58RyNVJ9o2JD9fru9c3IQxabf-nRUFeNqxJXAztJp9yDwfvYM2d5otf8_l9VOUFMXSYrQO81Wp9hmsqUDPLi3FxJuMDQ5w1iM8cZOWdnsr6plq1qRJhDeYj_l3ccwMb7xvJNdn_09_YlRapASzh5eHQXE03Gzr4kdjpCruHtc6Y4xvhsLEeNieN9gZ-k-JPFFhQ2M_HXoC_Ve-MDXVzXjaVwp4dfS5QMzn6LmxoyqbJUJ8LoAWVqX4Qj5_AjE54DWlWODNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTVkwJ64yEFdG-rqsPquL5O5jceJJvmqValZGhMfLAVmd0uc5evsp_l5eD_K-jVlof40vrvnbHLj6oZdaeo0_I7Jf7CY3nhHS1SWOGcRB69WikcojaWn7QwLzBFY6OSUehfiw0F1YgGSo60iCC-KfiqIADes9RG_6bWG3vsj-cmVulRxIud_fiaKwubVrChbOLbULZNlD3NnyELg00xEf5arWyicV2toWlLREiplQxn4loD-zSPNoiajCKhsyWvxTNWMLEhJwzJUvVmq2MSta3wrwXkdcSpXy58tE0LwG-GJKxJM3wDasL3Z5nMJigbr9sfoemqqZFS539KnAoBcRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
یه پستچی رفته بسته‌ کوکوریارو تحویل بده که کوکوریا نه تنها باهاش عکس گرفته بلکه بدین شکل یه عکس هم با مدال جام جهانی ازش گرفته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102504" target="_blank">📅 14:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102502">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNZxAi04WW1lImZx39PqOe5og9QOWXwG_xbbkPICyFQy4NuLlsIC713WeUbYRb-bZYXfQS6aJitzcJO1_lQxFQR89Fe8v5MToG2xzHAf4Ssz6KiNZ8a5hxQB2cd9NSweTTn25JpCJlV8u126UfQzxroHPre4tSw_dp-2Ash_C2f5W6_bBO7tX0thBVDrSi2Xx1M_2PZyUWa2Jn8CSnBi-u23_qiBD3xdAUzpYNiwTdYFSl9c6MivT5L40tbhBxyhoo2f-BRiUakgsZCeEP8lJjTpJ9rHO13f5jP4E3aSKw87msks8ALn8Z8T0dslfR1yWYTP3r98PKhh2jWLivkoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRyMlyhMyZbG2R0NonOCCDIoCMWcuGwMpbo-F7VAkRjSQTtu2P5X28fponaeFQceC0Q53cZV7OPjMuXVbg9SY8qBW9S08dGOC7Yu3eAO5svJPgNzO9ENKy-Lyp6cY1a8J4aogbR623ckfFaFrtDcj6axmlUJcOcOapgOpEX6znRgQARnz32999KrkT82cOoe2Qc2V6XEWpFeh0e_Yh9-bCil4cP9oqGjd-e1PsQJG6mA2xrcywfdKE9D77QkS50CRSC1YA4aKQzgnJ7zkg1WEd85LxKtp9s7pPNgPkG32A4TSNKyQDJtpSfesvhMZMse1Ne5LkBakQ2kaYCtdnOolA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
نقل و انتقالات بارسا و رئال تا به اینجا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102502" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102501">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIStyzJ0W9_GUG4iD4NVGNaNHFgHTeC8jxFPQqEtw3DFVPCu5TPS0kIkz9UWNgqRJ7cT7HZV6OAJDltTuZrw_Ck2BzyecArZBiyGR8ZZEtYjxlsbK15fwULlMm1gHp9QPMaYwyAF2IobYYMNfvbjvVVRZFbjf3Y_FNJ70KqkwV0xDdOZw-w7GXrpqvuqznW4hxsXUB4XYvdCNH_xGz2SsLOEzjqvE14wSYtTJle-COZB-ajuwRGMz5l8QtON7ySJn9D7zCEp2lIMB-hFhU0H74clbaabnidz2AH5PvsrUNZFxmWmUcys_4oTQBManJZ_Ng6xX7BDJ7YETGbGhBv6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
اطرافیان وینی هرگونه توافق بین این بازیکن و آرسنال رو تکذیب کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/102501" target="_blank">📅 13:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102500">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsU3W2ZMKV3Qc_Z8sD1NKcDmTffFvPaUOYKz0LzqWSrNU2h1SujmW7J16eHMe5AUC9o7oS1SEFPbBhgbDl-45T2_ulTBmCqSw3cwW-CkhGakfU2RCS_BhgCYz-m09xct9ifUsQygXzRh70byOsTZlyDVAh2NF64SKDF9lsaqvaUKVAWuJFEbV5r7C0B9scaPuU5Nzo7OEt3oheblftlUAzxBa3qmswo0DFWZAEkd3IQU8By29fRk05YWz9OmNlTAymkMZ-WtJr8qkpL5v8hw_zCv6qFeCc1RQbA8R92x2Oqvjg2tEw0iHZD89oc-ymnGXnzu0CUbuuw18iV_Gtfvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
• کریستیانو رونالدو به یک ویدیوی کوتاه در اینستاگرام که او را به عنوان مشهورترین ورزشکار تاریخ معرفی می‌کند، پاسخ داد:
"خیلی ساده."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102500" target="_blank">📅 12:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102499">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=hMMVKoKcq7kAyCU-lqWanEkc5NDqBJsy3yet4XZjYIwY5e5Iou8PPNDvayowpYm-HyaQUvSAiAN7nK6uRb5nXPcG1dObijGI1DA3BjhJn-2hJKAQCWnDalA6t8QTwKQrUenZ-Cwqd0kIkU3KBoMsISxDH311Pcd3rz6XDmdXjAYPuNlx83gX_4NcoX3yF12Ecm4yS9xFi5Was9GxqvnNfBUYvrEYI7SG4AuS_1fBRQLBZdTfrql5VB4ofKMxGJ6T_n0Xf5h0_pc_X_QG83J_0YJ1WflnIr6sJmzYbdNYtgC0o3bQoDAqSoge1N0tUB2ojdrhCZ4pz6HYdahbyCXWoaNv_0M6GNbC3Xv2gsky_omPQdfxn3RUVHuqdIew67SDlLUMT4KnjQMx35wcWWXd77mwMPLq5_CvRt-R8V0bLp8bPzGTK2yK5xT8XSBFM-iPqnPGO-uJQUwsEg9up23jY2OZ8sXzGsZI4RRaBYsDusqUgg-N1r6yfeCQcxMGKgMbPHACwllCugxCH7cnnD4kCP7_ZZuU5ccxFynC8OoJi3JdpWFs_S15SDLPR7Ek0pp4ikMTenLcXs0UhIkLcjU1GY2FyboAMwW1H8ni9D1n1F2s89TxUiaYZnUHAo7mC_Keu7GIKSIfsz2wXI7Vhsv7bEdvPO14M0LKcbscKFEUe3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d00a9ff8.mp4?token=hMMVKoKcq7kAyCU-lqWanEkc5NDqBJsy3yet4XZjYIwY5e5Iou8PPNDvayowpYm-HyaQUvSAiAN7nK6uRb5nXPcG1dObijGI1DA3BjhJn-2hJKAQCWnDalA6t8QTwKQrUenZ-Cwqd0kIkU3KBoMsISxDH311Pcd3rz6XDmdXjAYPuNlx83gX_4NcoX3yF12Ecm4yS9xFi5Was9GxqvnNfBUYvrEYI7SG4AuS_1fBRQLBZdTfrql5VB4ofKMxGJ6T_n0Xf5h0_pc_X_QG83J_0YJ1WflnIr6sJmzYbdNYtgC0o3bQoDAqSoge1N0tUB2ojdrhCZ4pz6HYdahbyCXWoaNv_0M6GNbC3Xv2gsky_omPQdfxn3RUVHuqdIew67SDlLUMT4KnjQMx35wcWWXd77mwMPLq5_CvRt-R8V0bLp8bPzGTK2yK5xT8XSBFM-iPqnPGO-uJQUwsEg9up23jY2OZ8sXzGsZI4RRaBYsDusqUgg-N1r6yfeCQcxMGKgMbPHACwllCugxCH7cnnD4kCP7_ZZuU5ccxFynC8OoJi3JdpWFs_S15SDLPR7Ek0pp4ikMTenLcXs0UhIkLcjU1GY2FyboAMwW1H8ni9D1n1F2s89TxUiaYZnUHAo7mC_Keu7GIKSIfsz2wXI7Vhsv7bEdvPO14M0LKcbscKFEUe3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ویدیو جالب و وایرال شده از رقص امین‌حیایی بازیگر محبوب سینمای مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/102499" target="_blank">📅 11:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102498">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=NrB4QQZRG4zYrSqbEvBXd9wjLSU0T_00sN7HiV1t9UfciWqRJmQBE7InvP5MjIlH3vavQaN9wHx2rzPWJfHbRef5AlU-yUoD0UOZ9NIeGxNAwKtt8c8Y3Ifz5x5CJxtbPnfv1YLmtLhyzQotEi3wzqHFxKuYgBDv27yW8Ja2NNWSfwHTwLw22fmG-JNq8MyQYwNyyi8XC2-1FIS53mBEJc7XeBm0f6aZNRTP2MOt9n6zXim5nd5nQss7yBYB3HC3tfAfF3ZU9tQIeSK7qVCIOKalu44bAVVY5p-x1bS6oIiRhMMV6rU3fk2aVSkvx8WofKtAMtfq8l5qaBUYfIHsrSIkynOQSm-49npA4fzi8WKH_-uPshtVTmTXf6hVgZQbjC98pQSGxKf7P19Vis4vVjhHkf0Z6xY3YOw8NAEUIWBKJxB_1OznUSfzKjKQ6QoITJNVabOM00ZKe9FJb14yIcBuWq8oIRefoEe_wje57xYz3eqMdgIU2wv2UVy3QIKWOjR2B5BHn9WCrKGTI25nj7Gss2JyMS0bkbT_JuJHhomw16sQIreqB9T1MEBm0iGSqOTx5UYO76QQYptBfYByjHyH2a4fT0ZH3i9Ldz5WjOlt-GrgxLYB6HPAc2NKLUvnib0FjgUSAagGfn_gwC9k-YRGm5YnCz8OZ2AihjQjr9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86343d5e54.mp4?token=NrB4QQZRG4zYrSqbEvBXd9wjLSU0T_00sN7HiV1t9UfciWqRJmQBE7InvP5MjIlH3vavQaN9wHx2rzPWJfHbRef5AlU-yUoD0UOZ9NIeGxNAwKtt8c8Y3Ifz5x5CJxtbPnfv1YLmtLhyzQotEi3wzqHFxKuYgBDv27yW8Ja2NNWSfwHTwLw22fmG-JNq8MyQYwNyyi8XC2-1FIS53mBEJc7XeBm0f6aZNRTP2MOt9n6zXim5nd5nQss7yBYB3HC3tfAfF3ZU9tQIeSK7qVCIOKalu44bAVVY5p-x1bS6oIiRhMMV6rU3fk2aVSkvx8WofKtAMtfq8l5qaBUYfIHsrSIkynOQSm-49npA4fzi8WKH_-uPshtVTmTXf6hVgZQbjC98pQSGxKf7P19Vis4vVjhHkf0Z6xY3YOw8NAEUIWBKJxB_1OznUSfzKjKQ6QoITJNVabOM00ZKe9FJb14yIcBuWq8oIRefoEe_wje57xYz3eqMdgIU2wv2UVy3QIKWOjR2B5BHn9WCrKGTI25nj7Gss2JyMS0bkbT_JuJHhomw16sQIreqB9T1MEBm0iGSqOTx5UYO76QQYptBfYByjHyH2a4fT0ZH3i9Ldz5WjOlt-GrgxLYB6HPAc2NKLUvnib0FjgUSAagGfn_gwC9k-YRGm5YnCz8OZ2AihjQjr9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
پنج گل برتر فصل‌گذشته لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102498" target="_blank">📅 11:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102497">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwcO9RPKVk6QFDqMO7llZPP9KNVyWLBdIA_H-cfOQaS-xKNrHiDsHoirokrE7HpapNr-vUFKP3F5TYKfhzrlx6SvCw5plz-oPOBvgDHl-az2YcGQxfVz1e1NH7p5vV_ncEdQjj3EVE7-Bl58ikBKHGr7ekOhAoJTH1ThMPi8wZdENqlV7p0oHaT0ivXKvyyNsjUriNuR5xvsJEavyhGTKC9K5rDqIHKpmZq6yEL4JL6DFHtxKmlC0iKeekhYI6RUGamf8NjZqWWX_n9JSRQlXmF4SLIStJ_Ui2v0JHvNUIJKjaea8WY8Ruk_q5mkZ7CsLpvIp3IMUlAMPnDSPK-I4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
اینفانتینو با انتشار بیانیه‌ای اعلام کرد که طرح فروش بخشی از سود جام جهانی به شرکت‌های سرمایه‌گذاری خصوصی، به طور کامل لغو شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102497" target="_blank">📅 11:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102496">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e324940235.mp4?token=q0z_mwNjdTqXwvgKFiMlfPiS3vJ_DePn_jZpC5LoUCGtflu7efS02q42yG3CUEkBwNxjhdJ_IEKWtU0BxsgwQ4YNkJbRmSf3ZauR4KBrugm412t6b3cXpwXmno40mBOVLl5T-j9wJlpP2TWLq5zG179aZ5TuJZVWzToqvm3d7oEcCv6wHLP-GoYjXzp_vFHv33rx6EX9-iHTJ5kg9Mp9buitdHCFrDHs8D4R-olhBBqJx7qIKSQSdlPJinjKVdXsjCZPWdZ7cPdWpzH7262X9T628oBq1BEI7uvjm5CSKKlO73oyuRazsTIvoaSFKhmZI5e4dYg5Bf-P6nTQmkxWFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e324940235.mp4?token=q0z_mwNjdTqXwvgKFiMlfPiS3vJ_DePn_jZpC5LoUCGtflu7efS02q42yG3CUEkBwNxjhdJ_IEKWtU0BxsgwQ4YNkJbRmSf3ZauR4KBrugm412t6b3cXpwXmno40mBOVLl5T-j9wJlpP2TWLq5zG179aZ5TuJZVWzToqvm3d7oEcCv6wHLP-GoYjXzp_vFHv33rx6EX9-iHTJ5kg9Mp9buitdHCFrDHs8D4R-olhBBqJx7qIKSQSdlPJinjKVdXsjCZPWdZ7cPdWpzH7262X9T628oBq1BEI7uvjm5CSKKlO73oyuRazsTIvoaSFKhmZI5e4dYg5Bf-P6nTQmkxWFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
و بالاخره تحقق رویای دوران فوتبالی کاسمیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102496" target="_blank">📅 11:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102495">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👀
🔥
هشت سوپرپاس‌گل ثبت‌شده فصول اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102495" target="_blank">📅 10:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102494">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl8ubTFxMVPVfshbVgplrNDuT4PgX4cbvRjRYH04swt9jadyTmplYoxQDHK1BfpLZy6V6ejMetLOY9y3HeM59ZYLOdOyE8CRMe6M5INGRJddPrjcYKhYVKuCKHN2oHKyeZc9m7xcp-TcBv5PBSOVohbdUIchftRZ40TWnKaKKibbqm-VCQ2zlwgKa7fyKtV0ybkGyN7iNB-fa0_W7WP_ca7417yFQVijJs8NW2cwcZQckEU5oAAqaWu8OtninsCAoxwi8HTW_Scm1i2haKGowHvuJhEch2PnjIN1Y6OgVvIgMuDcsNXX1MW7kjB2JeefGjcKXAU-iHhvZHspzP4fOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه آمار مسی و هالند زیر نظر پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102494" target="_blank">📅 10:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102493">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW0j_A_RGKdP-4PEUMInau_EFruL1Dj1MPocPpmvO32zcKxhYH7Kz2S0GrfeBzdpUkVQLQIghJArGG7356c654YrGtkVoQjDGgIP0iRIZlUIB-objNwIzHVaBnyMajIi2mCohgm6U4hEkgg9ufRIH0mmpD1ifm5PnmqRSQ0BJuQ1YFZMpJrKRZK46qBpekv23sSo5pZDkesMnSKATTpaY4tvQssxy1Onghp9sfnKsSkhEYKg_fNclAEkcEuukUYEHIrE70q6Z60hABgMmvmj2podBx886Mt_w0T8ZF6eqHgmrr7elqgcdGS08KTB1FeYRYwLYMw1i45oeJUpMxYEIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام قهرمانان ادوار مختلف پریمیرلیگ ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102493" target="_blank">📅 10:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102492">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCH-wTYom_KKg5O22PogcGQCABO8js8Eny4rcBw6Y1UUkpKbdbU5WHIGtrtGuqMA5o2b6JdRy3U72kQDXwxbxDr8IS_Xezw8BuymVKcIHMX0PVU2rvn37RErSkBh10UbLkfLdsIOj4PGkDDM33nPpGIdkI2WUfGggziPs367K8k7O4HwK8NH68Y465ONM65CcBPAbFc3JS-yxntjgePn1mqWguprOhVJ5AQVwUFi-rcMkGbY6326WBm7Rx3BGjG5gGhUoCsYWwx8sMAZLPfK7JhIC6isU9lUgGoOWt37Wb26JLB6dMS-jVYI_6kZSPqXhIuesTtTqY_KTXOR7UziqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
باورنکردنی است که برخی از زنان چه توانایی‌هایی دارند!
💪
ژوستین وانهائورمات، هافبک بلژیکی تیم زنان کریستال پالاس، در سه‌ماهه سوم بارداری خود همچنان در حال تمرین کردن است
❤️
او ۷ ماهه باردار است و همچنان با تمام توان به تلاش و فعالیت ادامه می‌دهد
👏
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102492" target="_blank">📅 09:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102491">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjFtwAeehyHZLS5XdjbjPhtGlHCJBz21WOWraOWJ183656rF-7ojoBJE8k9CrUDbKu2Oajl7htbZwHq6FVIAD18N0swpBzBu-JT5vy9HhUg75EZh0WHi41_PfFPpBb5t9ulUQtTDB7soS-g9ph6sX3XEzCiWyZ-o7hkF7l_-m0bYqMw8KYO6LMADLlcoTpaBb5yZvoWstP1iEX6rtfkCsnh8-UtiqUV8SJNgZ5hRxovhjV1Hs7hEK1vBkZnV4YRcgD229aS6RO1tRKWJUHj4SgQ4jNOHQPMK_qmgtRL1GebK2WhrXiaLllj2nAQosOEgLSGvvs-IwNUGESyTkJ7vQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇫🇷
فوریییییی از فابریزیو رومانو: پاریس بازم وینگر خرید! مگنس آکلیوش، وینگر راست ۲۴ ساله موناکو به پاریسن ژرمن پیوست. مبلغ انتقال ۵۰ میلیون‌یورو و تا سال ۲۰۳۱؛
هیر وی گو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102491" target="_blank">📅 09:39 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
